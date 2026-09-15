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
OR = OR_FONCE = CREME = TEXTE = None
NOTO = PLAYFAIR = None
FILIGRANE = ""
_TEXTES = _PALETTE = None
_RTL = True
_DECOR = "arabe"   # cadre décoratif : "arabe" | "japonais" | "coreen"


def _f(chemin, taille, gras=False):
    """Charge une police. Si c'est une police variable, fixe un poids
    utilisable (Regular par défaut, SemiBold si gras=True et disponible) —
    sans ça, certaines polices variables (ex. Noto Sans JP/KR) s'affichent
    par défaut en Thin (poids 100), illisible en grand format."""
    if not Path(chemin).exists():
        for fb in [
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/Library/Fonts/Arial.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
        ]:
            if Path(fb).exists():
                return ImageFont.truetype(fb, taille)
        return ImageFont.load_default()
    police = ImageFont.truetype(chemin, taille)
    try:
        noms = [n.decode() if isinstance(n, bytes) else n
                for n in police.get_variation_names()]
        cible = "SemiBold" if (gras and "SemiBold" in noms) else None
        cible = cible or ("Regular" if "Regular" in noms else None)
        if cible:
            police.set_variation_by_name(cible)
    except Exception:
        pass
    return police


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


def _bloc_surligne_mots(d, phrase, mot, y, police, base, surlignage):
    """Phrase multi-mots en LTR (japonais/coréen), mot par mot, avec le
    mot-clé surligné. Même principe que _bloc_surligne_ar mais sans
    inversion de l'ordre des mots."""
    bb = d.textbbox((0, y), phrase, font=police)
    mots = phrase.split(" ")

    def larg(t):
        b = d.textbbox((0, 0), t, font=police)
        return b[2] - b[0]

    espace = larg(" ")
    largeurs = [larg(m) for m in mots]
    total = sum(largeurs) + espace * (len(mots) - 1)

    x = (TAILLE - total) // 2
    for m, w in zip(mots, largeurs):
        couleur = surlignage if (mot and (mot in m or m in mot)) else base
        d.text((x, y), m, font=police, fill=couleur)
        x += w + espace
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


def _cadre_arabe(d):
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


def _cadre_japonais(d):
    """Filet double façon montage de rouleau (kakejiku) + repères d'angle
    façon tombo (croix d'alignement typographiques) + sceau hanko plein."""
    m, m2 = 54, 66
    d.rectangle([m, m, TAILLE - m, TAILLE - m], outline=OR_FONCE, width=2)
    d.rectangle([m2, m2, TAILLE - m2, TAILLE - m2], outline=(*OR, 130), width=1)

    lg = 26
    for cx, cy, sx, sy in [(m, m, 1, 1), (TAILLE - m, m, -1, 1),
                            (m, TAILLE - m, 1, -1), (TAILLE - m, TAILLE - m, -1, -1)]:
        d.line([(cx + sx * 10, cy), (cx + sx * (10 + lg), cy)], fill=OR, width=2)
        d.line([(cx, cy + sy * 10), (cx, cy + sy * (10 + lg))], fill=OR, width=2)

    s = 30
    x0, y0 = TAILLE - m - s - 6, m + 6
    d.rectangle([x0, y0, x0 + s, y0 + s], fill=OR_FONCE)
    d.line([(x0 + 6, y0 + s // 2), (x0 + s - 6, y0 + s // 2)], fill=CREME, width=2)
    d.line([(x0 + s // 2, y0 + 6), (x0 + s // 2, y0 + s - 6)], fill=CREME, width=2)


def _dessiner_fleur(d, cx, cy, rayon=16, coul_petales=(255, 105, 160), coul_coeur=(255, 225, 60)):
    """Dessine une fleur mignonne à 5 pétales."""
    import math
    for i in range(5):
        angle = i * (2 * math.pi / 5) - math.pi / 2
        px = cx + int((rayon * 0.95) * math.cos(angle))
        py = cy + int((rayon * 0.95) * math.sin(angle))
        pr = int(rayon * 0.65)
        d.ellipse([px - pr, py - pr, px + pr, py + pr], fill=coul_petales)
    cr = int(rayon * 0.45)
    d.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=coul_coeur)


def _dessiner_coeur(d, cx, cy, taille=11, couleur=(255, 120, 160)):
    """Dessine un petit cœur mignon."""
    r = taille // 2
    d.ellipse([cx - taille, cy - r, cx, cy + r], fill=couleur)
    d.ellipse([cx, cy - r, cx + taille, cy + r], fill=couleur)
    d.polygon([(cx - taille, cy), (cx + taille, cy), (cx, cy + int(taille * 1.3))], fill=couleur)


def _cadre_coreen(d):
    """Cadre épuré aux angles arrondis (toit courbe de hanok)
    sans fleurs parasites sur le cadre."""
    m, m2, rayon = 56, 68, 44
    d.rounded_rectangle([m, m, TAILLE - m, TAILLE - m], radius=rayon,
                        outline=OR_FONCE, width=2)
    d.rounded_rectangle([m2, m2, TAILLE - m2, TAILLE - m2], radius=rayon - 12,
                        outline=(*OR_FONCE, 80), width=1)


def _dessiner_etincelle(d, cx, cy, r=10, coul=(255, 238, 160)):
    """Dessine une petite étoile étincelante à 4 pointes."""
    pts = [
        (cx, cy - r), (cx + r * 0.25, cy - r * 0.25),
        (cx + r, cy), (cx + r * 0.25, cy + r * 0.25),
        (cx, cy + r), (cx - r * 0.25, cy + r * 0.25),
        (cx - r, cy), (cx - r * 0.25, cy - r * 0.25)
    ]
    d.polygon(pts, fill=coul)


def _appliquer_stickers_coreen(img, racine, seed=None, is_cta=False):
    """Incruste automatiquement et de façon aléatoire variée les personnages et cliparts kawaii."""
    import random
    dir_stickers = Path(racine) / "niches/coreen/stickers"
    if not dir_stickers.exists():
        return img

    persos = sorted(dir_stickers.glob("perso_*.png"))
    cliparts = sorted(dir_stickers.glob("clipart_*.png"))
    if not persos or not cliparts:
        return img

    if seed is not None:
        rng = random.Random(seed)
    else:
        rng = random.Random()

    perso_file = rng.choice(persos)
    clipart_file = rng.choice(cliparts)

    calque = Image.new("RGBA", (TAILLE, TAILLE), (0, 0, 0, 0))

    # Varier la position : aléatoirement en bas à droite ou en bas à gauche
    align_droite = (rng.random() > 0.5)
    px = rng.randint(840, 880) if align_droite else rng.randint(60, 100)
    py = rng.randint(840, 880)

    # Position clipart : coin haut opposé
    cx = rng.randint(60, 100) if align_droite else rng.randint(840, 880)
    cy = rng.randint(60, 95)

    rot_p = rng.randint(-5, 5)
    rot_c = rng.randint(-5, 5)

    # Coller le personnage
    im_p = Image.open(perso_file).convert("RGBA")
    taille_p = rng.randint(165, 185)
    im_p.thumbnail((taille_p, taille_p), Image.LANCZOS)
    if rot_p != 0:
        im_p = im_p.rotate(rot_p, resample=Image.BICUBIC, expand=True)
    calque.paste(im_p, (px, py), im_p)

    # Coller le clipart
    im_c = Image.open(clipart_file).convert("RGBA")
    taille_c = rng.randint(140, 160)
    im_c.thumbnail((taille_c, taille_c), Image.LANCZOS)
    if rot_c != 0:
        im_c = im_c.rotate(rot_c, resample=Image.BICUBIC, expand=True)
    calque.paste(im_c, (cx, cy), im_c)

    # Petites étincelles kawaii autour
    d = ImageDraw.Draw(calque)
    nb_etincelles = rng.randint(4, 7)
    for _ in range(nb_etincelles):
        ex = rng.randint(50, TAILLE - 50)
        ey = rng.randint(50, TAILLE - 50)
        if 210 < ex < 870 and 200 < ey < 880:
            continue
        r_sp = rng.randint(8, 14)
        _dessiner_etincelle(d, ex, ey, r_sp, (255, 238, 150))
        _dessiner_etincelle(d, ex + 2, ey + 2, max(4, r_sp // 2), (255, 255, 255))

    return Image.alpha_composite(img.convert("RGBA"), calque)


_DECOR_FUNCS = {
    "arabe": _cadre_arabe,
    "japonais": _cadre_japonais,
    "coreen": _cadre_coreen,
}


def _cadre(d):
    _DECOR_FUNCS.get(_DECOR, _cadre_arabe)(d)


def _centrer(hauteur_contenu):
    """Renvoie le y de départ pour centrer verticalement un bloc."""
    return max(MARGE_SURE, (TAILLE - hauteur_contenu) // 2)


# ------------------------------------------------------------------ slides

def _bloc_decomposition(d, decomp, y, font_native, font_son, col1, col2, rtl=True):
    if not decomp:
        return y

    items = list(reversed(decomp)) if rtl else decomp

    block_data = []
    for item in items:
        cle = item["cle"]
        son = item.get("son", "")
        kw = {"direction": "rtl", "language": "ar"} if (rtl and HAVE_RAQM) else {}
        bb_c = d.textbbox((0, 0), cle, font=font_native, **kw)
        bb_s = d.textbbox((0, 0), son, font=font_son)
        w_c = bb_c[2] - bb_c[0]
        w_s = bb_s[2] - bb_s[0]
        w_item = max(w_c, w_s, 60)
        block_data.append({
            "cle": cle,
            "son": son,
            "w": w_item,
            "h_c": max(bb_c[3] - bb_c[1], 40),
            "h_s": max(bb_s[3] - bb_s[1], 25)
        })

    gap = 40
    total_w = sum(b["w"] for b in block_data) + gap * (len(block_data) - 1)

    cur_x = (TAILLE - total_w) // 2
    # Ensure generous vertical height for diacritics (harakat above & below)
    max_h_native = max((b["h_c"] for b in block_data), default=60)
    if max_h_native < 60:
        max_h_native = 60

    # Increased vertical spacing to prevent overlap
    vert_gap = 26

    for idx, b in enumerate(block_data):
        # Alternating 2-tone colors (no rainbow!)
        couleur = col1 if idx % 2 == 0 else col2
        kw = {"direction": "rtl", "language": "ar"} if (rtl and HAVE_RAQM) else {}

        # Native letter / character
        bb_c = d.textbbox((0, 0), b["cle"], font=font_native, **kw)
        w_c = bb_c[2] - bb_c[0]
        x_c = cur_x + (b["w"] - w_c) // 2
        d.text((x_c, y), b["cle"], font=font_native, fill=couleur, **kw)

        # Corresponding phonetic sound directly below with generous vertical space
        bb_s = d.textbbox((0, 0), b["son"], font=font_son)
        w_s = bb_s[2] - bb_s[0]
        x_s = cur_x + (b["w"] - w_s) // 2
        d.text((x_s, y + max_h_native + vert_gap), b["son"], font=font_son, fill=couleur)

        cur_x += b["w"] + gap

    return y + max_h_native + vert_gap + 35 + 25


def _slide_mot(fond, e):
    img = _voile(fond, tuple(_PALETTE["voile"]), _PALETTE["voile_alpha"], _PALETTE["flou"])
    d = ImageDraw.Draw(img)
    _cadre(d)

    y = 180
    y = _bloc(d, FILIGRANE, y, _f(SANS, 26), OR_FONCE) + 30
    y = _bloc(d, e["ar"], y, _f(NOTO, 150, gras=True), OR, rtl=_RTL) + 20

    # Phonétique globale si présente (même couleur OR que le mot en coréen)
    coul_cible = OR if _DECOR == "coreen" else CREME
    if e.get("phonetique"):
        y = _bloc(d, f"[{e['phonetique']}]", y, _f(SERIF_I, 34), coul_cible) + 15

    # Traduction française (même couleur OR que la langue de base et la phonétique)
    coul_fr = OR if _DECOR == "coreen" else OR_FONCE
    y = _bloc(d, e["fr"].upper(), y, _f(SANS, 34, gras=True), coul_fr) + 25

    # Décomposition lettre/son si présente (2 teintes alternées Or & Crème)
    if e.get("decomposition"):
        y = _bloc_decomposition(d, e["decomposition"], y, _f(NOTO, 70), _f(SANS, 26), OR, CREME, rtl=_RTL)

    d.rectangle([(TAILLE - 65) // 2, y, (TAILLE + 65) // 2, y + 2], fill=OR_FONCE)
    y += 34

    fn_surligne = _bloc_surligne_ar if _RTL else _bloc_surligne_mots
    if _DECOR == "coreen":
        # 1. Phrase native avec mot surligné en OR
        y = fn_surligne(d, e["phrase_ar"], e.get("surligne_ar", ""), y,
                        _f(NOTO, 44), TEXTE, OR) + 12

        # 2. Phonétique de la phrase avec mot surligné en OR
        ph_lecture = e.get("phrase_lecture") or e.get("phrase_phonetique")
        if not ph_lecture:
            try:
                import sys
                from pathlib import Path
                sys.path.insert(0, str(Path(racine) / "../template-ebook/langues/coreen"))
                from phonetique import translitterer
                ph_lecture = translitterer(e["phrase_ar"])
            except Exception:
                pass
        mot_ph = e.get("surligne_lecture") or e.get("surligne_phonetique") or e.get("phonetique", "")
        if ph_lecture:
            y = _bloc_surligne_fr(d, ph_lecture, mot_ph, y,
                                  _f(SANS, 24), (*TEXTE, 190), OR) + 12

        # 3. Phrase française avec mot surligné en OR
        y = _bloc_surligne_fr(d, e["phrase_fr"], e.get("surligne_fr", ""), y,
                              _f(SERIF_I, 28), TEXTE, OR)
    else:
        y = fn_surligne(d, e["phrase_ar"], e.get("surligne_ar", ""), y,
                        _f(NOTO, 46), (*OR, 210), TEXTE) + 24
        y = _bloc_surligne_fr(d, e["phrase_fr"], e.get("surligne_fr", ""), y,
                              _f(SERIF_I, 30), (*OR_FONCE, 200), TEXTE)
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
        y = _bloc(d, ligne, y, _f(SERIF_I, 32), TEXTE) + 12
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

    y = _bloc(d, f"« {e['sens']} »", y, _f(SERIF_I, 36), TEXTE) + 24
    y = _bloc(d, e["note"], y, _f(SERIF_I, 30), (*OR_FONCE, 210))
    return img


def _slide_grammaire(fond, e):
    img = _voile(fond, tuple(_PALETTE["voile"]), _PALETTE["voile_alpha"], _PALETTE["flou"])
    d = ImageDraw.Draw(img)
    _cadre(d)

    y = 175
    y = _bloc(d, FILIGRANE, y, _f(SANS, 26), OR_FONCE) + 34
    y = _bloc(d, _TEXTES.get("tag_grammaire", "GRAMMAIRE"), y, _f(SANS_G, 24), OR) + 40
    y = _bloc(d, e["titre"], y, _f(NOTO, 90, gras=True), OR, rtl=_RTL) + 30

    d.rectangle([(TAILLE - 70) // 2, y, (TAILLE + 70) // 2, y + 2], fill=OR_FONCE)
    y += 30

    for ligne in _couper(e["regle"], 36):
        y = _bloc(d, ligne, y, _f(NOTO, 30), TEXTE) + 10
    y += 20

    if _DECOR == "coreen":
        y = _bloc_surligne_fr(d, e["exemple_natif"], e.get("surligne_natif", ""), y,
                              _f(NOTO, 42), TEXTE, OR) + 18
        if e.get("exemple_lecture"):
            mot_lec = e.get("surligne_lecture") or e.get("surligne_natif", "")
            y = _bloc_surligne_fr(d, e["exemple_lecture"], mot_lec, y,
                                  _f(SANS, 24), (*TEXTE, 190), OR) + 18
        y = _bloc_surligne_fr(d, e["exemple_fr"], e.get("surligne_fr", ""), y,
                              _f(SERIF_I, 28), TEXTE, OR)
    else:
        y = _bloc_surligne_fr(d, e["exemple_natif"], e.get("surligne_natif", ""), y,
                              _f(NOTO, 42), (*OR, 210), TEXTE) + 18
        if e.get("exemple_lecture"):
            mot_lec = e.get("surligne_lecture") or ""
            y = _bloc_surligne_fr(d, e["exemple_lecture"], mot_lec, y,
                                  _f(SANS, 24), (*OR_FONCE, 200), OR) + 18
        y = _bloc_surligne_fr(d, e["exemple_fr"], e.get("surligne_fr", ""), y,
                              _f(SERIF_I, 28), (*OR_FONCE, 200), TEXTE)
    if e.get("astuce"):
        y += 20
        for ligne in _couper(e["astuce"], 40):
            y = _bloc(d, ligne, y, _f(NOTO, 22), (*OR, 190)) + 8
    return img


def _slide_conjugaison(fond, e):
    img = _voile(fond, tuple(_PALETTE["voile"]), _PALETTE["voile_alpha"], _PALETTE["flou"])
    d = ImageDraw.Draw(img)
    _cadre(d)

    y = 155
    y = _bloc(d, FILIGRANE, y, _f(SANS, 26), OR_FONCE) + 32
    y = _bloc(d, _TEXTES.get("tag_conjugaison", "CONJUGAISON"), y, _f(SANS_G, 24), OR) + 36

    y = _bloc(d, e["verbe_natif"], y, _f(NOTO, 74, gras=True), OR_FONCE, rtl=_RTL) + 10
    y = _bloc(d, f"{e['verbe_lecture']} — {e['verbe_fr']}", y, _f(NOTO, 24), (*OR_FONCE, 190)) + 20

    y = _fleche(d, y, OR_FONCE) + 20

    y = _bloc(d, e["conjugue_natif"], y, _f(NOTO, 90, gras=True), OR, rtl=_RTL) + 12
    y = _bloc(d, f"{e['conjugue_lecture']}  ·  {e['forme']}", y, _f(NOTO, 24), (*OR, 200)) + 28

    d.rectangle([(TAILLE - 70) // 2, y, (TAILLE + 70) // 2, y + 2], fill=OR_FONCE)
    y += 28

    for ligne in _couper(e["regle"], 36):
        y = _bloc(d, ligne, y, _f(NOTO, 28), (*OR_FONCE, 210)) + 8
    y += 16

    if _DECOR == "coreen":
        mot_natif = e.get("surligne_natif") or e.get("conjugue_natif", "")
        mot_lec = e.get("surligne_lecture") or e.get("conjugue_lecture", "")
        mot_fr = e.get("surligne_fr") or ""
        fn_surligne = _bloc_surligne_ar if _RTL else _bloc_surligne_mots
        # 1. Ligne coréenne avec mot conjugué surligné en OR
        y = fn_surligne(d, e["exemple_natif"], mot_natif, y, _f(NOTO, 42), TEXTE, OR) + 12
        # 2. Ligne phonétique avec verbe conjugué surligné en OR
        ex_lec = e.get("exemple_lecture")
        if ex_lec:
            y = _bloc_surligne_fr(d, ex_lec, mot_lec, y, _f(SANS, 24), (*TEXTE, 190), OR) + 12
        # 3. Ligne française avec verbe conjugué surligné en OR
        y = _bloc_surligne_fr(d, e["exemple_fr"], mot_fr, y, _f(SERIF_I, 28), TEXTE, OR)
    else:
        y = _bloc(d, e["exemple_natif"], y, _f(NOTO, 38), TEXTE, rtl=_RTL) + 14
        y = _bloc(d, e["exemple_fr"], y, _f(SERIF_I, 26), (*OR_FONCE, 200))
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
    global OR, OR_FONCE, CREME, TEXTE, NOTO, PLAYFAIR, FILIGRANE, _TEXTES, _PALETTE, _RTL, _DECOR

    p = niche["palette"]
    OR       = tuple(p["or"])
    OR_FONCE = tuple(p["or_fonce"])
    CREME    = tuple(p["creme"])
    TEXTE    = tuple(p.get("texte", (255, 255, 255)))
    _PALETTE = p
    _TEXTES  = niche["textes"]
    _RTL     = niche["polices"].get("rtl", False)
    _DECOR   = niche.get("decor", niche["id"])

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
        "grammaire": _slide_grammaire,
        "conjugaison": _slide_conjugaison,
    }
    s1 = fabricants[type_post](fond, entree)
    s2 = _slide_cta(fond, type_post)

    if _DECOR == "coreen":
        import random
        sel = random.randint(1, 9999999)
        s1 = _appliquer_stickers_coreen(s1, racine, seed=sel, is_cta=False)
        s2 = _appliquer_stickers_coreen(s2, racine, seed=sel + 777, is_cta=True)

    p1 = dossier_sortie / "slide1.jpg"
    p2 = dossier_sortie / "slide2.jpg"
    s1.convert("RGB").save(p1, "JPEG", quality=95)
    s2.convert("RGB").save(p2, "JPEG", quality=95)
    return p1, p2

