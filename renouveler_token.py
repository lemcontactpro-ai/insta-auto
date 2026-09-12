#!/usr/bin/env python3
"""
Renouvelle les jetons d'accès Meta longue durée avant leur expiration à 60
jours, pour chaque niche active. Met à jour le secret GitHub correspondant
(IG_TOKEN_<NICHE>) avec le nouveau jeton, pour que publier.py n'utilise
jamais un jeton périmé.

Lancé par .github/workflows/renouveler_token.yml, deux fois par mois.
"""

import base64
import json
import os
import sys
from pathlib import Path

import requests
from nacl import encoding, public

RACINE = Path(__file__).parent
CONFIG = RACINE / "niches" / "config.json"
API = "https://graph.facebook.com/v21.0"
REPO = "lemcontactpro-ai/insta-auto"


def chiffrer(cle_publique_b64, secret_clair):
    cle_publique = public.PublicKey(cle_publique_b64.encode("utf-8"), encoding.Base64Encoder())
    boite = public.SealedBox(cle_publique)
    chiffre = boite.encrypt(secret_clair.encode("utf-8"))
    return base64.b64encode(chiffre).decode("utf-8")


def maj_secret_github(pat, nom_secret, valeur):
    headers = {
        "Authorization": f"Bearer {pat}",
        "Accept": "application/vnd.github+json",
    }
    cle = requests.get(
        f"https://api.github.com/repos/{REPO}/actions/secrets/public-key",
        headers=headers, timeout=30,
    ).json()
    chiffre = chiffrer(cle["key"], valeur)
    r = requests.put(
        f"https://api.github.com/repos/{REPO}/actions/secrets/{nom_secret}",
        headers=headers,
        json={"encrypted_value": chiffre, "key_id": cle["key_id"]},
        timeout=30,
    )
    if r.status_code not in (201, 204):
        raise RuntimeError(f"Échec mise à jour secret {nom_secret} : {r.status_code} — {r.text}")


def renouveler(app_id, app_secret, jeton_actuel):
    r = requests.get(f"{API}/oauth/access_token", params={
        "grant_type": "fb_exchange_token",
        "client_id": app_id,
        "client_secret": app_secret,
        "fb_exchange_token": jeton_actuel,
    }, timeout=30)
    if not r.ok:
        raise RuntimeError(f"Échec renouvellement : {r.status_code} — {r.text}")
    return r.json()["access_token"]


def main():
    app_id = os.environ["META_APP_ID"]
    app_secret = os.environ["META_APP_SECRET"]
    pat = os.environ["GH_PAT_SECRETS"]

    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    echecs = []

    for niche in cfg["niches"]:
        if not niche.get("actif"):
            continue
        nom_secret = niche["secrets"]["ig_token"]
        jeton_actuel = os.environ.get(nom_secret)
        if not jeton_actuel:
            print(f"[{niche['id']}] {nom_secret} absent de l'environnement, ignoré "
                  "(ajoute-le au step 'env' du workflow si cette niche est active).")
            continue
        try:
            nouveau = renouveler(app_id, app_secret, jeton_actuel)
            maj_secret_github(pat, nom_secret, nouveau)
            print(f"[{niche['id']}] jeton renouvelé, secret {nom_secret} mis à jour.")
        except Exception as e:
            print(f"[{niche['id']}] ÉCHEC : {e}")
            echecs.append(niche["id"])

    if echecs:
        sys.exit(f"Échec du renouvellement pour : {', '.join(echecs)}")


if __name__ == "__main__":
    main()
