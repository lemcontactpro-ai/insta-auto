#!/usr/bin/env python3
"""
Génération des slides @arabe.academie
Reprend le template validé : empilement mesuré, filigrane en haut,
cadre doré, zone sûre Instagram.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, features

HAVE_RAQM = features.check("raqm")

TAILLE = 1080
SANS      = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_G    = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SERIF_I   = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"

BLANC      = (255, 255, 255)
MARGE_SURE = 130   # zone sûre Instagram

# Remplis par creer_post() depuis la config de niche
OR = OR_FONCE = CREME = None
NOTO = PLAYFAIR = None
FILIGRANE = ""
_TEXTES = _PALETTE = None
_RTL = True


def _f(chemin, taille):
    if not Path(chemin).exists():
        for fb in [
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/Library/Fonts/Arial.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
        ]:
            if Path(fb).exists():
                return ImageFont.truetype(fb, taille)
        return ImageFont.load_default()
    return ImageFont.truetype(chemin, taille)


def _bloc(d, texte, y, police, couleur, rtl=False):
    """Dessine un texte centré à partir de y. Renvoie le bas réel des glyphes."""
    kw = {"direction": "rtl", "language": "ar"} if (rtl and HAVE_RAQM) else {}
    bb = d.textbbox((0, y), texte, font=police, **kw)
    largeur = bb[2] - bb[0]
    d.text(((TAILLE - largeur) // 2, y), texte, font=police, fill=couleur, **kw)
    return bb[3]


def _bloc_surligne_fr(d, phrase, mot, y, police, base, surlignage):
    """Phrase française avec le mot-clé dans une autre couleur."""
    i = phrase.lower().find(mot.lower())
    if i == -1:
        return _bloc(d, phrase, y, police, base)

    avant, cible, apres = phrase[:i], phrase[i:i + len(mot)], phrase[i + len(mot):]
    bb = d.textbbox((0, y), phrase, font=police)
    x = (TAILLE - (bb[2] - bb[0])) // 2

    def larg(t):
        if not t:
            return 0
        b = d.textbbox((0, 0), t, font=police)
        return b[2] - b[0]

    if avant:
        d.text((x, y), avant, font=police, fill=base)
    d.text((x + larg(avant), y), cible, font=police, fill=surlignage)
    if apres:
        d.text((x + larg(avant) + larg(cible), y), apres, font=police, fill=base)
    return bb[3]


def _bloc_surligne_ar(d, phrase, mot, y, police, base, surlignage):
    """Phrase arabe, mot par mot en RTL, avec le mot-clé surligné."""
    kw = {"direction": "rtl", "language": "ar"} if HAVE_RAQM else {}
    bb = d.textbbox((0, y), phrase, font=police, **kw)
    mots = phrase.split(" ")

    def larg(t):
        b = d.textbbox((0, 0), t, font=police, **kw)
        return b[2] - b[0]

    espace = larg(" ")
    largeurs = [larg(m) for m in mots]
    total = sum(largeurs) + espace * (len(mots) - 1)

    x = (TAILLE + total) // 2   # RTL : on part de la droite
    for m, w in zip(mots, largeurs):
        x -= w
        couleur = surlignage if (mot in m or m in mot) else base
        d.text((x, y), m, font=police, fill=couleur, **kw)
        x -= espace
    return bb[3]


def _fleche(d, y, couleur, longueur=34, alpha=190):
    cx = TAILLE // 2
    d.rectangle([cx - 1, y, cx + 1, y + longueur], fill=(*couleur, alpha))
    p = y + longueur
    d.polygon([(cx, p + 11), (cx - 8, p - 3), (cx, p + 2), (cx + 8, p - 3)],
              fill=(*couleur, alpha))
    return p + 11


def _carre(img):
    l, h = img.size
    c = min(l, h)
    return img.crop(((l - c) // 2, (h - c) // 2,
                     (l - c) // 2 + c, (h - c) // 2 + c)) \
              .resize((TAILLE, TAILLE), Image.LANCZOS)


def _voile(img, couleur, alpha, flou=2):
    fl = img.filter(ImageFilter.GaussianBlur(flou))
    return Image.alpha_composite(
        fl.convert("RGBA"), Image.new("RGBA", fl.size, (*couleur, alpha))
    )


def _cadre(d):
    m, lg, ep = 50, 85, 2
    coins = [
        [(m, m, m + lg, m + ep), (m, m, m + ep, m + lg)],
        [(TAILLE - m - lg, m, TAILLE - m, m + ep),
         (TAILLE - m - ep, m, TAILLE - m, m + lg)],
        [(m, TAILLE - m - ep, m + lg, TAILLE - m),
         (m, TAILLE - m - lg, m + ep, TAILLE - m)],
        [(TAILLE - m - lg, TAILLE - m - ep, TAILLE - m, TAILLE - m),
         (TAILLE - m - ep, TAILLE - m - lg, TAILLE - m, TAILLE - m)],
    ]
    for paire in coins:
        for r in paire:
            d.rectangle(r, fill=OR)

    m2 = 68
    for r in [(m2, m2, TAILLE - m2, m2 + 1),
              (m2, TAILLE - m2, TAILLE - m2, TAILLE - m2 + 1),
              (m2, m2, m2 + 1, TAILLE - m2),
              (TAILLE - m2 - 1, m2, TAILLE - m2, TAILLE - m2)]:
        d.rectangle(r, fill=(*OR_FONCE, 60))


def _centrer(hauteur_contenu):
    """Renvoie le y de départ pour centrer verticalement un bloc."""
    return max(MARGE_SURE, (TAILLE - hauteur_contenu) // 2)


# ------------------------------------------------------------------ slides

def _slide_mot(fond, e):
    img = _voile(fond, tuple(_PALETTE["voile"]), _PALETTE["voile_alpha"], _PALETTE["flou"])
    d = ImageDraw.Draw(img)
    _cadre(d)

    y = 200
    y = _bloc(d, FILIGRANE, y, _f(SANS, 26), OR_FONCE) + 40
    y = _bloc(d, e["ar"], y, _f(NOTO, 175), OR, rtl=_RTL) + 45
    y = _bloc(d, e["fr"].upper(), y, _f(SANS, 30), OR_FONCE) + 32

    d.rectangle([(TAILLE - 65) // 2, y, (TAILLE + 65) // 2, y + 2], fill=OR_FONCE)
    y += 34

    y = _bloc_surligne_ar(d, e["phrase_ar"], e.get("surligne_ar", ""), y,
                          _f(NOTO, 46), (*OR, 210), BLANC) + 24
    y = _bloc_surligne_fr(d, e["phrase_fr"], e.get("surligne_fr", ""), y,
                          _f(SERIF_I, 30), (*OR_FONCE, 200), BLANC)
    return img


def _slide_etymologie(fond, e):
    img = _voile(fond, tuple(_PALETTE["voile"]), _PALETTE["voile_alpha"], _PALETTE["flou"])
    d = ImageDraw.Draw(img)
    _cadre(d)

    y = 160
    y = _bloc(d, FILIGRANE, y, _f(SANS, 26), OR_FONCE) + 40
    y = _bloc(d, e["ar_origine"], y, _f(NOTO, 100), OR, rtl=_RTL) + 26
    y = _fleche(d, y, OR_FONCE) + 22
    y = _bloc(d, e["intermediaire"], y, _f(PLAYFAIR, 80), (*OR_FONCE, 210)) + 10
    y = _bloc(d, e["intermediaire_langue"], y, _f(SANS, 24), (*OR_FONCE, 170)) + 24
    y = _fleche(d, y, OR_FONCE) + 22
    y = _bloc(d, e["fr"], y, _f(PLAYFAIR, 80), OR) + 30

    d.rectangle([(TAILLE - 80) // 2, y, (TAILLE + 80) // 2, y + 2], fill=OR_FONCE)
    y += 34

    for ligne in _couper(e["explication"], 34):
        y = _bloc(d, ligne, y, _f(SERIF_I, 32), BLANC) + 12
    return img


def _slide_prenom(fond, e):
    img = _voile(fond, tuple(_PALETTE["voile"]), _PALETTE["voile_alpha"], _PALETTE["flou"])
    d = ImageDraw.Draw(img)
    _cadre(d)

    y = 190
    y = _bloc(d, FILIGRANE, y, _f(SANS, 26), OR_FONCE) + 40
    y = _bloc(d, e["ar"], y, _f(NOTO, 165), OR, rtl=_RTL) + 40
    y = _bloc(d, e["fr"], y, _f(PLAYFAIR, 54), OR_FONCE) + 32

    d.rectangle([(TAILLE - 80) // 2, y, (TAILLE + 80) // 2, y + 2], fill=OR_FONCE)
    y += 30

    y = _bloc(d, f"« {e['sens']} »", y, _f(SERIF_I, 36), BLANC) + 24
    y = _bloc(d, e["note"], y, _f(SERIF_I, 30), (*OR_FONCE, 210))
    return img


def _slide_cta(fond, type_post):
    """Slide 2, adaptée au type de post."""
    l1, l2 = _TEXTES["cta_ligne1"], _TEXTES["cta_ligne2"]

    img = _voile(fond, tuple(_PALETTE["voile_cta"]), _PALETTE["voile_cta_alpha"], _PALETTE["flou"] + 2)
    d = ImageDraw.Draw(img)
    _cadre(d)

    y = 250
    y = _bloc(d, FILIGRANE, y, _f(SANS, 26), OR_FONCE) + 45
    y = _bloc(d, l1, y, _f(PLAYFAIR, 56), CREME) + 22
    y = _bloc(d, l2, y, _f(PLAYFAIR, 56), CREME) + 55
    y = _bloc(d, _TEXTES["cta_sous_titre"], y, _f(SANS, 24), OR_FONCE) + 45

    texte = _TEXTES["cta_bouton"]
    pol = _f(SANS_G, 22)
    bb = d.textbbox((0, 0), texte, font=pol)
    lb, hb = bb[2] - bb[0] + 70, 56
    xb = (TAILLE - lb) // 2
    d.rectangle([xb, y, xb + lb, y + hb], outline=OR, width=2)
    _bloc(d, texte, y + 16, pol, OR)

    return img


def _couper(texte, largeur):
    mots = texte.split(" ")
    lignes, courante = [], ""
    for m in mots:
        test = f"{courante} {m}".strip()
        if len(test) <= largeur:
            courante = test
        else:
            lignes.append(courante)
            courante = m
    if courante:
        lignes.append(courante)
    return lignes


# ------------------------------------------------------------------ public

def creer_post(type_post, entree, chemin_fond, dossier_sortie, niche, racine):
    """Génère les 2 slides selon la config de niche."""
    global OR, OR_FONCE, CREME, NOTO, PLAYFAIR, FILIGRANE, _TEXTES, _PALETTE, _RTL

    p = niche["palette"]
    OR       = tuple(p["or"])
    OR_FONCE = tuple(p["or_fonce"])
    CREME    = tuple(p["creme"])
    _PALETTE = p
    _TEXTES  = niche["textes"]
    _RTL     = niche["polices"].get("rtl", False)

    dp = Path(racine) / "polices"
    NOTO      = str(dp / niche["polices"]["etrangere"])
    PLAYFAIR  = str(dp / niche["polices"]["titre"])
    FILIGRANE = niche["compte"]

    dossier_sortie = Path(dossier_sortie)
    dossier_sortie.mkdir(parents=True, exist_ok=True)

    fond = _carre(Image.open(chemin_fond))

    fabricants = {
        "mot": _slide_mot,
        "etymologie": _slide_etymologie,
        "prenom": _slide_prenom,
    }
    s1 = fabricants[type_post](fond, entree)
    s2 = _slide_cta(fond, type_post)

    p1 = dossier_sortie / "slide1.jpg"
    p2 = dossier_sortie / "slide2.jpg"
    s1.convert("RGB").save(p1, "JPEG", quality=95)
    s2.convert("RGB").save(p2, "JPEG", quality=95)
    return p1, p2
