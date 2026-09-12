#!/usr/bin/env python3
"""
Publication automatique multi-niches.

    python3 publier.py --niche arabe
    python3 publier.py --niche arabe --dry-run
    python3 publier.py --toutes

Aucun appel à un modèle de langage : tout est déterministe.
Coût en tokens : zéro.
"""

import argparse
import json
import os
import random
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

import generer

load_dotenv()

RACINE = Path(__file__).parent
CONFIG = RACINE / "niches" / "config.json"
API    = "https://graph.facebook.com/v21.0"

FENETRE_JOURS = 7


# ------------------------------------------------------------------ config

def charger_config():
    if not CONFIG.exists():
        sys.exit(f"Config introuvable : {CONFIG}")
    return json.loads(CONFIG.read_text(encoding="utf-8"))


def trouver_niche(cfg, ident):
    for n in cfg["niches"]:
        if n["id"] == ident:
            return n
    dispo = ", ".join(n["id"] for n in cfg["niches"])
    sys.exit(f"Niche '{ident}' inconnue. Disponibles : {dispo}")


# -------------------------------------------------------------- historique

def chemin_historique(niche):
    return RACINE / niche["dossier"] / "historique.json"


def charger_historique(niche):
    p = chemin_historique(niche)
    if not p.exists():
        return {"posts": []}
    return json.loads(p.read_text(encoding="utf-8"))


def purger(hist):
    limite = datetime.now(timezone.utc) - timedelta(days=FENETRE_JOURS)
    hist["posts"] = [
        p for p in hist["posts"]
        if datetime.fromisoformat(p["date"]) > limite
    ]
    return hist


def enregistrer(niche, hist, cle_mot, fond, lien=None):
    hist["posts"].append({
        "date": datetime.now(timezone.utc).isoformat(),
        "mot": cle_mot,
        "fond": fond,
        "lien": lien,
    })
    chemin_historique(niche).write_text(
        json.dumps(hist, ensure_ascii=False, indent=2), encoding="utf-8"
    )


# --------------------------------------------------------------- selection

def choisir_exercice(niche, hist):
    """Sélection pour les niches à moteur HTML/KaTeX : le contenu est une
    liste d'exercices, pas un vocabulaire, et il n'y a pas de photo de fond."""
    base = RACINE / niche["dossier"]
    fichier = base / niche.get("contenu", "exercices.json")
    items = [e for e in json.loads(fichier.read_text(encoding="utf-8"))["exercices"]
             if e.get("verifie") is True]
    if not items:
        sys.exit(f"Aucun exercice vérifié dans {fichier} "
                 f"(chaque exercice doit porter verifie=true).")

    vus = {p["mot"] for p in hist["posts"]}
    dispo = [e for e in items if f"exercice:{e['id']}" not in vus]
    if not dispo:
        print("    (tous les exercices vus cette semaine, on recycle)")
        dispo = items

    entree = random.choice(dispo)
    return "exercice", f"exercice:{entree['id']}", entree, None


def choisir(niche, hist):
    if niche.get("moteur") == "html-katex":
        return choisir_exercice(niche, hist)

    base = RACINE / niche["dossier"]
    vocab = json.loads((base / "vocabulaire.json").read_text(encoding="utf-8"))

    correspondance = {
        "mot": "mots",
        "etymologie": "mots_francais_arabe",
        "prenom": "prenoms",
        "grammaire": "grammaire",
        "conjugaison": "conjugaison",
    }

    familles = []
    for type_post, poids in niche["poids_types"].items():
        if poids <= 0:
            continue
        items = vocab.get(correspondance[type_post], [])
        # Les etymologies non verifiees ne sont jamais publiees
        if type_post == "etymologie":
            items = [e for e in items if e.get("verifie") is True]
        if items:
            familles.append((type_post, items, poids))

    if not familles:
        sys.exit("Aucun contenu publiable. Vérifie vocabulaire.json "
                 "(les étymologies doivent avoir verifie=true).")

    mots_vus  = {p["mot"]  for p in hist["posts"]}
    fonds_vus = {p["fond"] for p in hist["posts"]}

    type_choisi = random.choices(
        [t for t, _, _ in familles],
        weights=[p for _, _, p in familles],
        k=1,
    )[0]
    items = next(i for t, i, _ in familles if t == type_choisi)

    dispo = [(i, e) for i, e in enumerate(items)
             if f"{type_choisi}:{i}" not in mots_vus]
    if not dispo:
        print(f"    (tous les '{type_choisi}' vus cette semaine, on recycle)")
        dispo = list(enumerate(items))

    idx, entree = random.choice(dispo)

    dossier_fonds = base / "fonds"
    images = sorted(p for p in dossier_fonds.iterdir()
                    if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"})
    if not images:
        sys.exit(f"Aucune image dans {dossier_fonds}")

    libres = [p for p in images if p.name not in fonds_vus] or images
    fond = random.choice(libres)

    return type_choisi, f"{type_choisi}:{idx}", entree, fond


# ---------------------------------------------------------------- legendes

def construire_legende(niche, type_post, e):
    tags = niche["hashtags_base"]

    if type_post == "mot":
        corps = (
            f"✨ {e['ar']} : {e['fr'].capitalize()}\n\n"
            f"📖 Exemple d'utilisation :\n"
            f"{e['phrase_ar']}\n"
            f"« {e['phrase_fr']} »\n\n"
            "💡 Un mot par jour, et dans 3 mois tu lis tes premières phrases en arabe ! 🚀\n\n"
            "📚 Retrouve l'ebook complet dans le lien en bio !"
        )
    elif type_post == "etymologie":
        corps = (
            f"💡 Le savais-tu ? Le mot « {e['fr'].capitalize()} » vient de l'arabe {e['ar_origine']} !\n\n"
            f"📜 Évolution : {e['ar_origine']} ➔ {e['intermediaire']} ➔ {e['fr'].lower()}\n\n"
            f"{e['explication']}\n\n"
            "✨ Le français regorge de mots d'origine arabe ! Retrouve toute la liste dans notre ebook en bio 🔗"
        )
        tags += " #etymologie"
    elif type_post == "prenom":
        corps = (
            f"✨ Prénom : {e['ar']} ({e['fr']})\n\n"
            f"🤍 Signification : « {e['sens']} »\n\n"
            f"{e['note']}\n\n"
            "👇 Ton prénom est-il d'origine arabe ? Dis-le-moi en commentaire et je te donne sa signification ! ✨\n\n"
            "📚 Ebook complet disponible en bio !"
        )
        tags += " #prenomarabe"
    elif type_post == "grammaire":
        corps = (
            f"📘 Grammaire : {e['titre']}\n\n"
            f"{e['regle']}\n\n"
            f"✏️ Exemple :\n{e['exemple_natif']}"
            + (f" ({e['exemple_lecture']})" if e.get("exemple_lecture") else "")
            + f"\n« {e['exemple_fr']} »\n\n"
            + (f"💡 {e['astuce']}\n\n" if e.get("astuce") else "")
            + "📚 Toutes les bases expliquées dans l'ebook en bio !"
        )
        tags += " #grammaire"
    else:  # conjugaison
        corps = (
            f"🔤 Conjugaison : {e['verbe_fr'].capitalize()} ({e['verbe_natif']})\n\n"
            f"➡️ {e['forme']} : {e['conjugue_natif']}"
            + (f" ({e['conjugue_lecture']})" if e.get("conjugue_lecture") else "")
            + f"\n\n{e['regle']}\n\n"
            + f"📖 {e['exemple_natif']}\n« {e['exemple_fr']} »\n\n"
            + "📚 Le guide complet des conjugaisons dans l'ebook en bio !"
        )
        tags += " #conjugaison"

    return f"{corps}\n\n{tags}"


# ------------------------------------------------------------- hebergement

def _attendre_url_accessible(url, essais=8, delai=1.5):
    """Certaines URLs Cloudinary ne sont pas immédiatement servables par le
    CDN juste après l'upload (propagation). Meta échoue silencieusement si on
    lui passe une URL pas encore prête ('Only photo or video can be accepted
    as media type'), donc on vérifie nous-mêmes avant de la transmettre."""
    for tentative in range(essais):
        try:
            r = requests.get(url, timeout=15, stream=True)
            if r.ok and r.headers.get("content-type", "").startswith("image/"):
                return
        except requests.RequestException:
            pass
        time.sleep(delai)
    raise RuntimeError(f"URL hébergée jamais devenue accessible après {essais} essais : {url}")


def heberger(chemin):
    import cloudinary
    import cloudinary.uploader

    cloudinary.config(
        cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
        api_key=os.getenv("CLOUDINARY_API_KEY"),
        api_secret=os.getenv("CLOUDINARY_API_SECRET"),
        secure=True,
    )
    res = cloudinary.uploader.upload(
        str(chemin),
        folder="insta-auto",
        public_id=f"{chemin.stem}_{datetime.now():%Y%m%d%H%M%S}",
        format="jpg",
        resource_type="image",
    )
    url = res["secure_url"]
    _attendre_url_accessible(url)
    return url


# --------------------------------------------------------------- instagram

# error_subcode Meta renvoyé quand son propre fetcher ne peut pas encore
# récupérer l'URL Cloudinary tout juste uploadée (souvent transitoire côté
# propagation CDN, même si Meta le classe "is_transient": false). Notre
# propre vérification d'accessibilité (_attendre_url_accessible) tape le
# CDN depuis le runner GitHub Actions, pas depuis l'infra de fetch de Meta :
# elle peut passer alors que Meta touche un edge différent, pas encore
# propagé. D'où un retry sur l'appel Meta lui-même, seul test fiable.
ERREUR_MEDIA_NON_SERVABLE = 2207052


def _post(url, data, essais=1, delai=10):
    for tentative in range(essais):
        r = requests.post(url, data=data, timeout=60)
        if r.ok:
            return r.json()
        try:
            sous_code = r.json().get("error", {}).get("error_subcode")
        except ValueError:
            sous_code = None
        if sous_code == ERREUR_MEDIA_NON_SERVABLE and tentative < essais - 1:
            print(f"    (URL pas encore servable côté Meta, nouvel essai dans {delai}s...)")
            time.sleep(delai)
            continue
        raise RuntimeError(f"{r.status_code} — {r.text}")


def attendre(cid, token, essais=20):
    for _ in range(essais):
        r = requests.get(f"{API}/{cid}",
                         params={"fields": "status_code", "access_token": token},
                         timeout=30).json()
        s = r.get("status_code")
        if s == "FINISHED":
            return
        if s == "ERROR":
            raise RuntimeError(f"Conteneur {cid} en erreur : {r}")
        time.sleep(3)
    raise TimeoutError(f"Conteneur {cid} jamais prêt")


def publier_carrousel(ig_id, token, urls, legende):
    enfants = []
    for u in urls:
        rep = _post(f"{API}/{ig_id}/media", {
            "image_url": u,
            "is_carousel_item": "true",
            "access_token": token,
        }, essais=5, delai=10)
        enfants.append(rep["id"])

    for cid in enfants:
        attendre(cid, token)

    parent = _post(f"{API}/{ig_id}/media", {
        "media_type": "CAROUSEL",
        "children": ",".join(enfants),
        "caption": legende,
        "access_token": token,
    })
    attendre(parent["id"], token)

    pub = _post(f"{API}/{ig_id}/media_publish", {
        "creation_id": parent["id"],
        "access_token": token,
    })

    d = requests.get(f"{API}/{pub['id']}",
                     params={"fields": "permalink", "access_token": token},
                     timeout=30).json()
    return d.get("permalink", pub["id"])


def quota_restant(ig_id, token):
    try:
        r = requests.get(f"{API}/{ig_id}/content_publishing_limit",
                         params={"access_token": token}, timeout=30).json()
        return 50 - r["data"][0]["quota_usage"]
    except Exception:
        return None


# --------------------------------------------------------------- programme

def traiter(niche, dry_run=False):
    print(f"\n=== {niche['id']}  ({niche['compte']}) ===")

    base = RACINE / niche["dossier"]
    sortie = base / "sortie"
    sortie.mkdir(exist_ok=True)

    hist = purger(charger_historique(niche))
    type_post, cle, entree, fond = choisir(niche, hist)

    if niche.get("moteur") == "html-katex":
        import generer_maths
        print(f"[1] {type_post} → {entree.get('titre')}")
        slides = generer_maths.creer_post(entree, sortie, niche, RACINE)
        legende = generer_maths.construire_legende(niche, entree)
    else:
        etiquette = entree.get("fr") or entree.get("ar")
        print(f"[1] {type_post} → {etiquette}   fond : {fond.name}")
        slides = list(generer.creer_post(type_post, entree, fond, sortie, niche, RACINE))
        legende = construire_legende(niche, type_post, entree)
    print(f"[2] {len(slides)} slides générées")

    if dry_run:
        print(f"\n--- LÉGENDE ---\n{legende}\n---------------")
        print("Images :", "  ".join(str(p) for p in slides))
        print("Mode test : rien publié.")
        return

    ig_id = os.getenv(niche["secrets"]["ig_user_id"])
    token = os.getenv(niche["secrets"]["ig_token"])
    if not ig_id or not token:
        sys.exit(f"Secrets manquants pour '{niche['id']}' : "
                 f"{niche['secrets']['ig_user_id']}, {niche['secrets']['ig_token']}")

    restant = quota_restant(ig_id, token)
    if restant is not None and restant < 1:
        print("Quota Instagram atteint (50/24h). Abandon.")
        return

    print("[3] hébergement")
    urls = [heberger(p) for p in slides]

    print("[4] publication")
    lien = publier_carrousel(ig_id, token, urls, legende)
    print(f"    → {lien}")

    enregistrer(niche, hist, cle, fond.name if fond else "-", lien)
    print("[5] historique à jour")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--niche", help="identifiant de la niche")
    ap.add_argument("--toutes", action="store_true",
                    help="traite toutes les niches actives")
    ap.add_argument("--dry-run", action="store_true",
                    help="génère sans publier")
    a = ap.parse_args()

    cfg = charger_config()

    if a.toutes:
        cibles = [n for n in cfg["niches"] if n.get("actif")]
    elif a.niche:
        cibles = [trouver_niche(cfg, a.niche)]
    else:
        sys.exit("Précise --niche <id> ou --toutes")

    for n in cibles:
        traiter(n, dry_run=a.dry_run)


if __name__ == "__main__":
    main()
