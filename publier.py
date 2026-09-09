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

def choisir(niche, hist):
    base = RACINE / niche["dossier"]
    vocab = json.loads((base / "vocabulaire.json").read_text(encoding="utf-8"))

    correspondance = {
        "mot": "mots",
        "etymologie": "mots_francais_arabe",
        "prenom": "prenoms",
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
            f"{e['ar']} — {e['fr'].lower()}\n\n"
            f"{e['phrase_ar']}\n"
            f"« {e['phrase_fr']} »\n\n"
            "Un mot par jour, et en trois mois tu lis tes premières phrases.\n"
            "L'ebook complet est en bio."
        )
    elif type_post == "etymologie":
        corps = (
            f"Tu dis « {e['fr'].lower()} » tous les jours sans savoir que le mot "
            f"vient de l'arabe {e['ar_origine']}.\n\n"
            f"{e['ar_origine']} → {e['intermediaire']} → {e['fr'].lower()}\n\n"
            f"{e['explication']}\n\n"
            "Le français en compte des centaines. L'ebook les recense.\n"
            "Lien en bio."
        )
        tags += " #etymologie #histoiredesmots #languefrancaise"
    else:
        corps = (
            f"{e['ar']} — {e['fr']}\n\n"
            f"Signification : « {e['sens']} »\n\n"
            f"{e['note']}\n\n"
            "Ton prénom a peut-être aussi une racine arabe. "
            "Dis-le en commentaire, je te donne son sens.\n\n"
            "Ebook complet en bio."
        )
        tags += " #prenomarabe #signification #prenom"

    return f"{corps}\n\n.\n.\n.\n{tags}"


# ------------------------------------------------------------- hebergement

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
    )
    return res["secure_url"]


# --------------------------------------------------------------- instagram

def _post(url, data):
    r = requests.post(url, data=data, timeout=60)
    if not r.ok:
        raise RuntimeError(f"{r.status_code} — {r.text}")
    return r.json()


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
        })
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

    etiquette = entree.get("fr") or entree.get("ar")
    print(f"[1] {type_post} → {etiquette}   fond : {fond.name}")

    s1, s2 = generer.creer_post(type_post, entree, fond, sortie, niche, RACINE)
    print("[2] slides générées")

    legende = construire_legende(niche, type_post, entree)

    if dry_run:
        print(f"\n--- LÉGENDE ---\n{legende}\n---------------")
        print(f"Images : {s1}  {s2}")
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
    urls = [heberger(s1), heberger(s2)]

    print("[4] publication")
    lien = publier_carrousel(ig_id, token, urls, legende)
    print(f"    → {lien}")

    enregistrer(niche, hist, cle, fond.name, lien)
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
        try:
            traiter(n, a.dry_run)
        except Exception as exc:
            print(f"[ÉCHEC] {n['id']} : {exc}")


if __name__ == "__main__":
    main()
