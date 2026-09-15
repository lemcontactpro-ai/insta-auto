"""Génère les palettes « gélules » par domaine de physique.
Structure inchangée (DA Slack), seules les couleurs changent."""
import colorsys
from pathlib import Path

def hex_vers_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16)/255 for i in (0, 2, 4))

def rgb_vers_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(*(max(0, min(255, round(c*255))) for c in (r, g, b)))

def ajuste(base, dl=0.0, ds=0.0):
    r, g, b = hex_vers_rgb(base)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return rgb_vers_hex(*colorsys.hls_to_rgb(h, min(1, max(0, l+dl)), min(1, max(0, s+ds))))

def pastel(base, l=0.80, s=0.30):
    r, g, b = hex_vers_rgb(base)
    h, _, _ = colorsys.rgb_to_hls(r, g, b)
    return rgb_vers_hex(*colorsys.hls_to_rgb(h, l, s))

def teinte_rgba(base, l, s, a):
    r, g, b = hex_vers_rgb(base)
    h, _, _ = colorsys.rgb_to_hls(r, g, b)
    r2, g2, b2 = colorsys.hls_to_rgb(h, l, s)
    return f"rgba({round(r2*255)}, {round(g2*255)}, {round(b2*255)}, {a})"

DOMAINES = [
    ("mecanique",        "Mécanique",             "#4a154b"),
    ("optique",          "Optique",               "#103a72"),
    ("electrocinetique", "Électrocinétique",      "#0c4f3a"),
    ("ondes",            "Ondes et signaux",      "#0b4a55"),
    ("electromagnetisme","Électromagnétisme",     "#2c2a6b"),
    ("thermodynamique",  "Thermodynamique",       "#6d2418"),
    ("chimie",           "Chimie",                "#6b4a0f"),
    ("methodes",         "Méthodes et ordres de grandeur", "#2b2f36"),
]

GABARITS = Path('gabarits')
for cle, nom, base in DOMAINES:
    css = f'''/* {nom} : palette « gélules » du domaine, dérivée de la charte Slack.
   Ne redéfinit que des couleurs, la structure vit dans structure-gelules.css.
   Générée par faire_palettes.py : ne pas modifier à la main, modifier la
   couleur de base du domaine dans ce script. */

@import url("structure-gelules.css");

:root {{
  --aubergine:       {base};
  --aubergine-press: {ajuste(base, dl=0.06)};
  --aubergine-tint:  {ajuste(base, dl=0.04, ds=0.05)};
  --accent:          {base};
  --accent-on-fonce: {pastel(base, l=0.80, s=0.32)};
  --cream:           #f4ede4;
  --lavender:        {pastel(base, l=0.965, s=0.55)};
  --mute-on-aub:     {pastel(base, l=0.80, s=0.32)};
  --mesh-a:          {teinte_rgba(base, 0.78, 0.55, 0.22)};
  --mesh-b:          {teinte_rgba(base, 0.86, 0.45, 0.24)};
  --mesh-c:          {teinte_rgba(base, 0.70, 0.35, 0.16)};
  --wash:            rgba(244, 237, 228, .85);
  /* papier quadrillé sur les slides claires :
     décommenter pour l'activer */
  /* --grille: {teinte_rgba(base, 0.30, 0.55, 0.05)}; */
}}
'''
    (GABARITS / f"gelules-{cle}.css").write_text(css, encoding='utf-8')
    print(f"gelules-{cle}.css  ({nom}, {base})")
