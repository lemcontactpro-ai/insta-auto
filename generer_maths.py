#!/usr/bin/env python3
"""
Génération des slides @maths.prepa — carrousel de 7 slides maximum.

Pourquoi un moteur différent de generer.py (Pillow) : les autres niches
n'affichent que du texte court. Ici il faut des fractions, intégrales,
racines, indices — Pillow ne sait pas composer de mathématiques. Le rendu
passe donc par Chromium (Playwright) sur un document HTML qui compose le
LaTeX avec KaTeX. Tout est embarqué dans le dépôt (vendor/katex,
vendor/inter) : aucun appel réseau au rendu, donc résultat identique en
local et sur GitHub Actions.

Structure d'un carrousel :
    slide 1        : énoncé + étoiles de difficulté
    slides 2..n-1  : étapes de résolution (5 slides disponibles au maximum)
    slide n        : CTA

Aucun appel à un modèle de langage. Déterministe à l'exception du choix
de l'exercice, fait en amont par publier.py.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

MAX_SLIDES = 7
LARGEUR, HAUTEUR = 1080, 1350

# bornes de l'auto-ajustement typographique (voir --fit dans le CSS)
FIT_MIN, FIT_PAS = 0.70, 0.04


# --------------------------------------------------------------- répartition

def _poids(etape: dict) -> int:
    """Coût visuel approximatif d'une étape, pour équilibrer les groupes.
    Une formule occupe bien plus de hauteur qu'une ligne de texte."""
    p = len(etape.get("titre", "")) + 40
    for b in etape.get("blocs", []):
        v = str(b.get("valeur", ""))
        if b["type"] == "formule":
            p += 180 + len(v)
        elif b["type"] == "astuce":
            p += 90 + len(v)
        else:
            p += len(v)
    return p


def repartir(etapes: list[dict], slides_dispo: int) -> list[list[dict]]:
    """Découpe les étapes en au plus `slides_dispo` groupes **contigus**, en
    minimisant le groupe le plus chargé (recherche binaire sur le poids max).

    Une étape peut forcer sa place avec "groupe": <int> — dans ce cas la
    répartition automatique est ignorée et l'auteur décide.
    """
    if not etapes:
        return []

    if any("groupe" in e for e in etapes):
        if not all("groupe" in e for e in etapes):
            raise ValueError(
                "Si une étape porte 'groupe', toutes doivent le porter."
            )
        cles = sorted({e["groupe"] for e in etapes})
        if len(cles) > slides_dispo:
            raise ValueError(
                f"{len(cles)} groupes demandés pour {slides_dispo} slides "
                f"disponibles ({MAX_SLIDES} slides au total, énoncé et CTA compris)."
            )
        return [[e for e in etapes if e["groupe"] == k] for k in cles]

    if len(etapes) <= slides_dispo:
        return [[e] for e in etapes]

    poids = [_poids(e) for e in etapes]

    def tient(plafond: int) -> list[list[dict]] | None:
        groupes, courant, total = [], [], 0
        for e, p in zip(etapes, poids):
            if courant and total + p > plafond:
                groupes.append(courant)
                courant, total = [], 0
                if len(groupes) == slides_dispo:
                    return None
            courant.append(e)
            total += p
        groupes.append(courant)
        return groupes if len(groupes) <= slides_dispo else None

    bas, haut = max(poids), sum(poids)
    meilleur = tient(haut)
    while bas <= haut:
        milieu = (bas + haut) // 2
        essai = tient(milieu)
        if essai:
            meilleur, haut = essai, milieu - 1
        else:
            bas = milieu + 1
    return meilleur


# ------------------------------------------------------------------ fragments

_MATH_INLINE = re.compile(r"\$([^$]+)\$")

FINE = " "   # espace fine insécable
NBSP = " "   # espace insécable


def typo(t: str) -> str:
    """Typographie française : apostrophe courbe, espaces fines insécables
    devant la ponctuation double, insécables autour des guillemets. Appliquée
    au texte seul, jamais au LaTeX (voir _txt)."""
    t = t.replace("'", "’")
    t = re.sub(r"\s*([;:!?])", FINE + r"\1", t)
    t = re.sub(r"«\s*", "«" + NBSP, t)
    t = re.sub(r"\s*»", NBSP + "»", t)
    t = re.sub(r"(\d)\s+(\d)", r"\1" + NBSP + r"\2", t)   # 1 000
    return t


def _esc(t: str) -> str:
    return html.escape(typo(t))


def _txt(valeur: str) -> str:
    """Échappe le texte et transforme les $...$ en mathématiques inline.
    Le LaTeX est passé à KaTeX via un attribut, jamais interprété comme HTML."""
    morceaux, position = [], 0
    for m in _MATH_INLINE.finditer(valeur):
        morceaux.append(_esc(valeur[position:m.start()]))
        morceaux.append(f'<span data-tex="{html.escape(m.group(1), quote=True)}"></span>')
        position = m.end()
    morceaux.append(_esc(valeur[position:]))
    return "".join(morceaux).replace("\n", "<br>")


# --------------------------------------------------------------- validation

# Commandes courantes : si l'une apparaît sans sa contre-oblique, c'est
# presque sûrement un échappement perdu (JSON écrit avec \\ au lieu de \).
# KaTeX ne lève alors aucune erreur : il compose le nom en italique. Ce
# contrôle est le seul filet contre ce faux positif silencieux.
_COMMANDES = (
    "geqslant leqslant infty qquad quad frac sqrt text lim sum prod int "
    "mathbb mathcal times cdot cdots ldots dots displaystyle Longrightarrow "
    "Longleftrightarrow implies iff forall exists underbrace overbrace "
    "begin end left right alpha beta gamma lambda varepsilon partial "
    "operatorname binom xrightarrow to in notin subset cup cap"
).split()
_BARE = re.compile(r"(?<![\\A-Za-z])(" + "|".join(_COMMANDES) + r")(?![A-Za-z])")
_ENV_MULTILIGNE = re.compile(
    r"\\begin\{(cases|aligned|align|array|[bpvBV]?matrix|gathered|split)\}")


def _segments_latex(valeur: str, brut: bool) -> list[str]:
    """Les portions réellement LaTeX d'une valeur : la valeur entière pour un
    bloc 'formule', seulement les $...$ pour du texte."""
    if brut:
        return [valeur]
    return _MATH_INLINE.findall(valeur)


def verifier_latex(valeur: str, ou: str, brut: bool = True) -> list[str]:
    """Anomalies LaTeX. Ne contrôle que les portions mathématiques : les mots
    français ne doivent jamais déclencher d'alerte."""
    pbs = []
    if not brut and valeur.count("$") % 2:
        pbs.append(f"{ou} : nombre impair de « $ » — délimiteur non fermé.")
    for src in _segments_latex(valeur, brut):
        if "\\\\" in src and not _ENV_MULTILIGNE.search(src):
            pbs.append(f"{ou} : « \\\\ » hors environnement multiligne — "
                       f"échappement doublé (écris \\ et non \\\\ dans le JSON).")
        for m in _BARE.finditer(src):
            pbs.append(f"{ou} : « {m.group(1)} » sans contre-oblique.")
        if src.count("{") != src.count("}"):
            pbs.append(f"{ou} : accolades déséquilibrées.")
    return pbs


def verifier_exercice(exo: dict) -> list[str]:
    """Contrôles structurels et LaTeX sur un exercice, avant tout rendu."""
    pbs = []
    ident = exo.get("id", "?")

    for champ in ("id", "niveau", "chapitre", "titre", "enonce", "etapes"):
        if not exo.get(champ):
            pbs.append(f"{ident} : champ « {champ} » manquant ou vide.")
    if not 1 <= int(exo.get("niveau", 0)) <= 4:
        pbs.append(f"{ident} : « niveau » doit valoir 1 à 4.")
    if len(exo.get("titre", "")) > 60:
        pbs.append(f"{ident} : titre de {len(exo['titre'])} caractères (60 maximum).")

    try:
        repartir(exo.get("etapes", []), MAX_SLIDES - 2)
    except ValueError as err:
        pbs.append(f"{ident} : {err}")

    sections = [("énoncé", exo.get("enonce", []))]
    for i, e in enumerate(exo.get("etapes", []), start=1):
        sections.append((f"étape {i}", e.get("blocs", [])))
        pbs += verifier_latex(e.get("titre", ""), f"{ident}, titre étape {i}", brut=False)

    for nom, blocs in sections:
        for j, b in enumerate(blocs, start=1):
            t = b.get("type")
            if t not in {"texte", "question", "formule", "astuce", "filet"}:
                pbs.append(f"{ident}, {nom}, bloc {j} : type « {t} » inconnu.")
            pbs += verifier_latex(str(b.get("valeur", "")),
                                  f"{ident}, {nom}, bloc {j}", brut=(t == "formule"))

    pbs += verifier_latex(exo.get("conclusion", ""), f"{ident}, conclusion", brut=False)
    pbs += verifier_latex(exo.get("titre", ""), f"{ident}, titre", brut=False)
    return pbs


def _bloc(b: dict) -> str:
    t = b["type"]
    v = str(b.get("valeur", ""))

    if t == "texte":
        return f'<p class="texte">{_txt(v)}</p>'

    if t == "question":
        num = _esc(str(b.get("num", "")))
        return (f'<div class="question"><span class="num">{num}</span>'
                f'<span>{_txt(v)}</span></div>')

    if t == "formule":
        classe = "formule formule--cle" if b.get("cle") else "formule"
        return (f'<div class="{classe}">'
                f'<span data-tex-display="{html.escape(v, quote=True)}"></span></div>')

    if t == "astuce":
        marque = _esc(b.get("marque", "Astuce"))
        return (f'<div class="astuce"><span class="marque">{marque}</span>'
                f'<span>{_txt(v)}</span></div>')

    if t == "filet":
        return '<div class="filet"></div>'

    raise ValueError(f"Type de bloc inconnu : {t!r}")


def _etoiles(niveau: int, total: int = 4) -> str:
    forme = ("M12 2.2l2.95 5.98 6.6.96-4.77 4.65 1.12 6.57L12 17.26"
             "l-5.9 3.1 1.12-6.57L2.45 9.14l6.6-.96z")
    out = ['<div class="etoiles">']
    for i in range(total):
        c = "pleine" if i < niveau else "vide"
        out.append(f'<svg viewBox="0 0 24 24"><path class="{c}" d="{forme}"/></svg>')
    out.append("</div>")
    return "".join(out)


_CHEVRON = ('<svg viewBox="0 0 24 24"><path d="M8.6 4.4L7.2 5.8 13.4 12l-6.2 6.2'
            ' 1.4 1.4L16.2 12z"/></svg>')


def _progression(courant: int, total: int) -> str:
    cases = "".join(
        f'<span class="{"on" if i <= courant else ""}"></span>'
        for i in range(total)
    )
    return f'<div class="progression">{cases}</div>'


# --------------------------------------------------------------------- slides

def _slide_enonce(exo: dict, niche: dict) -> str:
    blocs = "".join(_bloc(b) for b in exo["enonce"])
    chapitre = _esc(exo.get("chapitre", "")).upper()
    titre = _txt(exo.get("titre", ""))
    return f"""
<section class="slide slide--aub">
  <div class="tete">
    <span class="handle">{niche['compte']}</span>
    {_etoiles(int(exo.get('niveau', 1)))}
  </div>
  <div class="corps">
    <div><span class="pill">{chapitre}</span></div>
    <h1 class="titre-exo">{titre}</h1>
    <div class="filet"></div>
    {blocs}
  </div>
  <div class="pied">
    <span></span>
    <span class="swipe">La correction {_CHEVRON}</span>
  </div>
</section>"""


def _slide_etape(groupe: list[dict], index: int, total: int, niche: dict) -> str:
    parts = []
    for e in groupe:
        interne = []
        if e.get("titre"):
            interne.append(f'<h2 class="titre-etape">{_txt(e["titre"])}</h2>')
        interne.extend(_bloc(b) for b in e.get("blocs", []))
        parts.append(f'<div class="sous-etape">{"".join(interne)}</div>')
    corps = "".join(parts)
    return f"""
<section class="slide slide--clair">
  <div class="tete">
    <span class="compteur">Étape {index + 1} / {total}</span>
    <span class="handle">{niche['compte']}</span>
  </div>
  {_progression(index, total)}
  <div class="corps corps--haut">{corps}</div>
  <div class="pied">
    <span></span>
    <span class="swipe">{'Suite' if index + 1 < total else 'Le bilan'} {_CHEVRON}</span>
  </div>
</section>"""


def _slide_cta(exo: dict, niche: dict) -> str:
    t = niche["textes"]
    note = exo.get("conclusion", "")
    bloc_note = f'<p class="cta-note">{_txt(note)}</p>' if note else ""
    return f"""
<section class="slide slide--aub">
  <div class="tete">
    <span class="handle">{niche['compte']}</span>
    {_etoiles(int(exo.get('niveau', 1)))}
  </div>
  <div class="cta-corps">
    <h2 class="cta-titre">{_esc(t['cta_ligne1'])}<br>{_esc(t['cta_ligne2'])}</h2>
    {bloc_note}
    <div class="cta-sous">{_esc(t['cta_sous_titre'])}</div>
    <div class="cta-bouton">{_esc(t['cta_bouton'])}</div>
  </div>
</section>"""


# ----------------------------------------------------------------------- page

_SCRIPT = """
<script>
(function () {
  // 1. composition du LaTeX
  var erreurs = [];
  document.querySelectorAll('[data-tex]').forEach(function (n) {
    try { katex.render(n.getAttribute('data-tex'), n, { throwOnError: true, displayMode: false }); }
    catch (e) { erreurs.push(n.getAttribute('data-tex') + ' :: ' + e.message); }
  });
  document.querySelectorAll('[data-tex-display]').forEach(function (n) {
    try { katex.render(n.getAttribute('data-tex-display'), n, { throwOnError: true, displayMode: true }); }
    catch (e) { erreurs.push(n.getAttribute('data-tex-display') + ' :: ' + e.message); }
  });

  // 2. auto-ajustement : on réduit --fit tant qu'un contenu dépasse
  var FIT_MIN = %FIT_MIN%, FIT_PAS = %FIT_PAS%;
  var rapport = [];
  document.querySelectorAll('.slide').forEach(function (s, i) {
    var fit = 1, deborde = function () {
      var c = s.querySelector('.corps') || s.querySelector('.cta-corps');
      return s.scrollHeight > s.clientHeight + 1 ||
             (c && c.scrollHeight > c.clientHeight + 1);
    };
    while (deborde() && fit > FIT_MIN + 1e-9) {
      fit = Math.round((fit - FIT_PAS) * 1000) / 1000;
      s.style.setProperty('--fit', fit);
    }
    rapport.push({ slide: i + 1, fit: fit, deborde: deborde() });
  });
  window.__rapport = { erreurs: erreurs, slides: rapport };
})();
</script>
"""


def construire_html(exo: dict, niche: dict, racine: Path) -> tuple[str, int]:
    slides_resolution = MAX_SLIDES - 2
    groupes = repartir(exo.get("etapes", []), slides_resolution)

    corps = [_slide_enonce(exo, niche)]
    for i, g in enumerate(groupes):
        corps.append(_slide_etape(g, i, len(groupes), niche))
    corps.append(_slide_cta(exo, niche))

    script = (_SCRIPT
              .replace("%FIT_MIN%", str(FIT_MIN))
              .replace("%FIT_PAS%", str(FIT_PAS)))

    # Le gabarit visuel est un simple fichier CSS, choisi par niche.
    # Les classes HTML ne changent pas : changer de charte graphique, c'est
    # changer cette seule valeur dans niches/config.json.
    gabarit = niche.get("gabarit", "gelules-aubergine.css")
    if not (racine / "gabarits" / gabarit).exists():
        raise ValueError(f"Gabarit introuvable : gabarits/{gabarit}")

    page = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<link rel="stylesheet" href="vendor/katex/katex.min.css">
<link rel="stylesheet" href="gabarits/{gabarit}">
<script src="vendor/katex/katex.min.js"></script>
</head><body>
{''.join(corps)}
{script}
</body></html>"""
    return page, len(corps)


# ------------------------------------------------------------------- rendu

def creer_post(exo: dict, dossier_sortie, niche: dict, racine) -> list[Path]:
    """Rend le carrousel en JPEG. Renvoie la liste des chemins, dans l'ordre."""
    from playwright.sync_api import sync_playwright

    racine = Path(racine)
    dossier_sortie = Path(dossier_sortie)
    dossier_sortie.mkdir(parents=True, exist_ok=True)

    pbs = verifier_exercice(exo)
    if pbs:
        raise ValueError("Exercice invalide :\n  - " + "\n  - ".join(pbs))

    page_html, nb = construire_html(exo, niche, racine)
    if nb > MAX_SLIDES:
        raise ValueError(f"{nb} slides générées, maximum {MAX_SLIDES}.")

    # le fichier doit être dans la racine du dépôt : les chemins vers
    # vendor/ et gabarits/ sont relatifs.
    tmp = racine / "._rendu_maths.html"
    tmp.write_text(page_html, encoding="utf-8")

    chemins = []
    try:
        with sync_playwright() as pw:
            nav = pw.chromium.launch(args=["--font-render-hinting=none"])
            pg = nav.new_page(viewport={"width": LARGEUR, "height": HAUTEUR},
                              device_scale_factor=1)
            pg.goto(tmp.as_uri())
            pg.wait_for_function("window.__rapport !== undefined", timeout=30000)
            rapport = pg.evaluate("window.__rapport")

            if rapport["erreurs"]:
                raise ValueError("LaTeX invalide :\n  - "
                                 + "\n  - ".join(rapport["erreurs"]))
            for s in rapport["slides"]:
                if s["deborde"]:
                    print(f"    /!\\ slide {s['slide']} déborde encore à "
                          f"--fit={s['fit']} : allège le contenu.")
                elif s["fit"] < 1:
                    print(f"    (slide {s['slide']} réduite à --fit={s['fit']})")

            for i, el in enumerate(pg.query_selector_all(".slide"), start=1):
                p = dossier_sortie / f"slide{i}.jpg"
                el.screenshot(path=str(p), type="jpeg", quality=92)
                chemins.append(p)
            nav.close()
    finally:
        if tmp.exists():
            tmp.unlink()

    return chemins


# ---------------------------------------------------------------- légende

def construire_legende(niche: dict, exo: dict) -> str:
    etoiles = "★" * int(exo.get("niveau", 1)) + "☆" * (4 - int(exo.get("niveau", 1)))
    lignes = [
        f"{exo.get('titre', 'Exercice')} — {etoiles}",
        "",
        f"📐 {exo.get('chapitre', '')}",
        "",
    ]
    if exo.get("accroche"):
        lignes += [exo["accroche"], ""]
    lignes += [
        "➡️ Balaie pour la correction détaillée, étape par étape.",
        "",
        "💬 Tu l'as trouvé tout seul ? Dis-le en commentaire.",
        "",
        "📚 Méthodes, exercices et corrigés complets : lien en bio.",
        "",
        niche["hashtags_base"] + (" " + exo["hashtags_extra"] if exo.get("hashtags_extra") else ""),
    ]
    return "\n".join(lignes)


# ------------------------------------------------------------------- essai

if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Rendu d'un exercice maths-prépa")
    ap.add_argument("--exercice", help="id de l'exercice (défaut : le premier)")
    ap.add_argument("--sortie", default=None)
    ap.add_argument("--valider", action="store_true",
                    help="contrôle tout exercices.json sans rien rendre")
    a = ap.parse_args()

    racine = Path(__file__).parent
    cfg = json.loads((racine / "niches" / "config.json").read_text(encoding="utf-8"))
    niche = next(n for n in cfg["niches"] if n["id"] == "maths-prepa")
    base = racine / niche["dossier"]
    exos = json.loads((base / "exercices.json").read_text(encoding="utf-8"))["exercices"]

    if a.valider:
        total = 0
        for e in exos:
            pbs = verifier_exercice(e)
            total += len(pbs)
            etat = "OK" if not pbs else f"{len(pbs)} anomalie(s)"
            print(f"[{etat:>14}] {e['id']} — {e.get('titre','')}")
            for p in pbs:
                print(f"                 · {p}")
        print(f"\n{len(exos)} exercice(s), {total} anomalie(s).")
        raise SystemExit(1 if total else 0)

    exo = (next(e for e in exos if e["id"] == a.exercice) if a.exercice else exos[0])
    sortie = Path(a.sortie) if a.sortie else base / "sortie"

    print(f"Exercice : {exo['id']} — {exo.get('titre')}")
    for p in creer_post(exo, sortie, niche, racine):
        print("  ", p)
    print("\n--- LÉGENDE ---")
    print(construire_legende(niche, exo))
