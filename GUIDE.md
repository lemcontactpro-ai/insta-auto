# Automatisation Instagram — guide technique

Ce document décrit **comment le système fonctionne**. Il s'adresse à un agent
IA ou à un développeur qui reprend le projet.

| Pour | Lire |
|---|---|
| Comprendre et modifier le système | ce document |
| Lancer une nouvelle niche, pas à pas | `MISE-EN-PLACE.md` |
| Le business : modèle, prix, marketing, erreurs | `../Guide.md` |
| Une niche en particulier | `niches/<id>/README.md` |

---

## 0. Instructions pour l'agent exécutant

**Ne réécris rien depuis zéro.** Le code, la configuration et le contenu
existent. Les sections ci-dessous expliquent pourquoi les choses sont faites
ainsi ; les redécouvrir par essai-erreur coûte du temps déjà dépensé.

**Ne modifie pas sans instruction explicite :**

| Quoi | Pourquoi |
|---|---|
| `niches/arabe/vocabulaire.json`, en particulier `_etymologies_ecartees` | 8 étymologies ont été écartées après vérification. Ne jamais les réintroduire, la contradiction a déjà été tranchée (§5) |
| La règle de placement vertical mesuré dans `generer.py` | L'arabe vocalisé déborde de sa position nominale. Des coordonnées en dur produisent des superpositions (§4) |
| Les choix d'architecture (GitHub Actions, pas de Google Drive) | Les raisons sont en §2. Ne pas les reproposer |

**N'invente jamais la valeur d'un secret.** S'il en manque un, arrête-toi et
demande. Un secret ne se colle ni dans le code, ni dans une conversation.

**Ne lis jamais les PDF** de `../atelier/*/sources/` ni de
`../atelier/maths-prepa/bibliotheque/`. Un poly scanné coûte plus de contexte
qu'une session entière de travail. Les `.md` à côté sont les OCR et servent au
repérage.

**Vérifie tout contenu factuel** par recherche web avec source citée, ou
rédige-le à la main et relis-le ligne à ligne. Jamais depuis ta seule mémoire :
une première tentative sans cette discipline a produit 8 erreurs sur 30
étymologies (§5).

**Regarde les images produites**, ne te contente pas de valider le JSON. Un
champ trop long ou une fonction de dessin réutilisée sans adaptation casse le
rendu sans lever d'erreur.

---
## 1. Le projet en une phrase

Publier automatiquement 2 posts/jour, midi et soir, sur plusieurs comptes Instagram
thématiques (niches), chacun vendant un **ebook interactif** (jamais juste
un PDF — terminologie fixée le 2026-09-12, à reprendre partout : templates,
légendes, fiche Payhip, guides), sans intervention manuelle et sans que
l'ordinateur de l'utilisatrice soit allumé.

**Niche 1** : @arabe.academie — apprentissage de l'arabe, public francophone.
**Niches futures** : 6 au total prévues, même système, contenu et palette
différents à chaque fois.

---

## 2. Les décisions prises (et pourquoi)

### Hébergement : GitHub Actions
- **Gratuit**, illimité en dépôt public, 2000 min/mois en privé (largement
  suffisant : 6 niches × 2 posts/jour × 30 jours ≈ 360 minutes utilisées).
- Le code tourne sur les serveurs de GitHub, pas sur l'ordinateur de
  l'utilisatrice — condition impérative du projet.
- Alternative écartée : **Claude Code Routines** (fonctionnalité réelle de
  Claude Code, vérifiée en documentation officielle). Le plan Pro de
  l'utilisatrice plafonne à **5 exécutions par jour**, insuffisant dès la 2e
  niche à ce rythme. C'est aussi une fonctionnalité en *research preview*,
  au comportement annoncé comme susceptible de changer — pas le bon socle
  pour un système censé tourner indéfiniment sans supervision.
- Alternative écartée : **Google Antigravity** comme moteur d'exécution
  récurrente. Antigravity est un IDE agentique local (Gemini), utile pour
  la mise en place ponctuelle (créer le dépôt, pousser les fichiers), mais
  ce n'est pas un service d'hébergement cloud — il ne fait pas tourner de
  cron indépendamment de la machine de l'utilisatrice une fois la session
  fermée. Son rôle ici s'arrête à l'étape de mise en place initiale.
- Autres alternatives écartées : Oracle Cloud, PythonAnywhere — demandent une
  administration manuelle (SSH, mises à jour) pour un gain nul face à GitHub
  Actions.

### Stockage des images et du vocabulaire : dans le dépôt GitHub
- Pas Google Drive : ajoute une authentification qui expire et un
  téléchargement à chaque exécution, pour aucun bénéfice.
- Les images doivent être envoyées une fois dans `niches/<id>/fonds/`. GitHub
  Actions ne peut pas lire un dossier sur l'ordinateur personnel de
  l'utilisatrice — le script tourne sur les serveurs GitHub.

### Coût en tokens/appels IA : zéro à l'exécution, à vie
- Le script `publier.py` ne fait aucun appel à un modèle de langage lors de
  ses exécutions automatiques. Sélection aléatoire, génération d'image par
  Pillow, légende par gabarit à trous. Entièrement déterministe.
- Un agent IA (Claude Code, Antigravity, ou autre) n'intervient que pour la
  mise en place, la maintenance, ou l'enrichissement de contenu — jamais à
  chaque publication.


---

## 2 bis. Outils utilisés et répartition des rôles

Ce projet est construit et maintenu dans **Google Antigravity** (l'IDE
agentique local de Google), où tournent deux agents complémentaires — pas
un seul :

- **Gemini** (accès gratuit 1 an via l'offre étudiante Google AI Pro) :
  la **recherche et la vérification de contenu**. Toute donnée factuelle
  d'une niche — étymologie, règle de grammaire, conjugaison, romanisation,
  signification de prénom — est rédigée par Gemini avec recherche web et
  citation d'une source fiable (CNRTL, Littré, Académie française,
  Wiktionnaire, ou équivalent selon la matière), jamais depuis sa seule
  mémoire. C'est la même exigence que la règle de vérification de la
  section 5 ; elle s'applique à **toute** niche, pas seulement l'arabe —
  une première tentative sans cette discipline a produit 8 erreurs sur 30
  étymologies (section 5).
- **Claude Code** : tout ce qui touche au **repo et à l'exécution** —
  édition de `generer.py`/`publier.py`/`niches/config.json`, rendu et
  vérification visuelle des slides Pillow, mise en place et débogage de
  l'automatisation GitHub Actions (workflows, secrets, incidents Meta/
  Cloudinary comme celui du 2026-09-12). Contrairement à Antigravity, qui
  reste local (section 2), Claude Code a accès direct au terminal, à git et
  à GitHub pour exécuter et corriger sans intervention manuelle à chaque
  étape.

**Pourquoi cette répartition et pas un seul outil pour tout :** Gemini via
l'offre étudiante est gratuit et fiable pour de la recherche factuelle
citée, mais Antigravity ne fait pas tourner de cron indépendant de la
machine (section 2) — il n'a donc aucun rôle dans l'exécution récurrente,
seulement dans la préparation du contenu. Claude Code prend le relais pour
tout ce qui doit s'exécuter, se déboguer ou se répliquer sans supervision.
Aucun des deux n'intervient à l'exécution des publications elles-mêmes :
le coût en appels IA reste nul à vie une fois une niche activée (section 2,
« Coût en tokens/appels IA »).

---

## 3. Architecture technique

```
insta-auto/                          (dépôt GitHub, à créer)
├── .github/workflows/publier.yml    # cron 2x/jour (midi, soir), appelle publier.py
├── publier.py                        # orchestrateur multi-niches
├── generer.py                        # génération des slides
├── requirements.txt
├── .env.example                      # liste des secrets à créer sur GitHub
├── polices/
│   ├── NotoNaskhArabic.ttf
│   └── PlayfairDisplay.ttf
└── niches/
    ├── config.json                   # UN fichier central : une entrée par niche
    └── arabe/
        ├── vocabulaire.json          # mots, étymologies, prénoms — vérifié
        ├── fonds/                    # photos de fond (à remplir, voir section 0)
        ├── sortie/                   # slides générées (temporaire, généré à l'exécution)
        └── historique.json           # généré automatiquement, anti-répétition 7 jours
```

**Ajouter une niche** = copier un bloc dans `config.json`, créer
`niches/<id>/` avec son vocabulaire et ses fonds, ajouter 2 secrets GitHub.
Zéro ligne de code à modifier.

**Commandes du script :**
```bash
python3 publier.py --niche arabe --dry-run   # génère sans publier, pour tester
python3 publier.py --niche arabe             # publie une fois
python3 publier.py --toutes                  # traite toutes les niches actives
```

---

## 4. Le template visuel (validé, ne pas redessiner)

- 1080×1080 px. Fond photo flouté + voile sombre. Cadre : équerres dorées aux
  4 coins + filet fin intérieur.
- Slide étymologie : le nom du compte (`@arabe.academie`) est affiché en tête
  de slide, 30px, or foncé `(200,149,90)`, à la place d'un ancien texte de
  catégorie qui a été retiré. Pas de filigrane latéral sur cette slide.
- Slides « mot » et « prénom » : filigrane vertical côté gauche, lecture
  bas→haut, conservé tel quel.
- Palette arabe : or `(232,185,122)`, or foncé `(200,149,90)`,
  crème `(245,230,210)`.
- Polices : Noto Naskh Arabic (arabe, RTL), Playfair Display (titres latins),
  Liberation Serif Italic (phrases), Liberation Sans (étiquettes).
- Marge de zone sûre Instagram : 130 px.
- Voir `exemple_etymologie.png` joint pour un rendu de référence à jour.

**Règle technique impérative** : le placement vertical est **mesuré, jamais
codé en dur**. Chaque fonction de dessin dans `generer.py` renvoie le bas
réel des glyphes ; l'élément suivant part de là plus un espacement fixe.
L'arabe vocalisé déborde largement de sa position nominale — fixer des
coordonnées à la main produit systématiquement des superpositions. Ne pas
redécouvrir cette contrainte par essai-erreur : elle est déjà résolue dans
le code fourni.

---

## 4 bis. Le second moteur de rendu : HTML + KaTeX (maths-prepa)

Le template de la section 4 (Pillow) couvre les niches de langues. Il ne
convient pas aux matières scientifiques : Pillow ne sait pas composer de
mathématiques — pas de fractions, pas d'intégrales, pas de racines. Un
second moteur coexiste donc, choisi par niche via `"moteur"` dans
`niches/config.json` :

| `moteur` | Rendu | Niches |
|---|---|---|
| absent (défaut) | `generer.py`, Pillow, 1080×1080, 2 slides | arabe, japonais, coréen |
| `"html-katex"` | `generer_maths.py`, Chromium + KaTeX, 1080×1350, jusqu'à 7 slides | maths-prepa |

**Comment ça marche.** `generer_maths.py` compose un document HTML (un
`<section>` par slide, style dans `gabarits/structure-gelules.css`), le charge dans
Chromium via Playwright, fait composer le LaTeX par KaTeX, puis photographie
chaque section en JPEG.

**KaTeX et la police Inter sont embarqués dans le dépôt** (`vendor/katex/`,
`vendor/inter/`, ~900 Ko). Aucun appel réseau au rendu : le résultat est
identique en local et sur le runner GitHub, et ne casse pas le jour où un
CDN change. Ne pas les remplacer par des liens externes.

**Deux garde-fous, tous deux nécessaires** — ils remplacent la règle de
placement mesuré de la section 4, qui n'a pas d'objet ici puisque le
navigateur fait la mise en page :

- *Auto-ajustement* : la variable CSS `--fit` réduit la typographie par
  paliers de 4 % (jusqu'à 70 %) tant qu'une slide déborde. Le rendu affiche
  toute réduction appliquée, et se plaint si ça déborde encore.
- *Contrôleur de contenu* (`--valider`) : dans le JSON on écrit `\sqrt`, pas
  `\\sqrt`. Un échappement doublé ne lève **aucune erreur KaTeX**, il compose
  le nom de la commande en italique — un faux positif parfaitement
  silencieux, déjà rencontré en développement. `verifier_exercice()` le
  détecte, ainsi que les accolades déséquilibrées et les champs manquants.

**Sur GitHub Actions**, l'étape `Publier (maths-prepa)` lit `actif` dans
`niches/config.json` et sort immédiatement si la niche est inactive :
Chromium (~1 min d'installation) n'est téléchargé que le jour où elle part.

**Coût en tokens** : toujours nul à l'exécution. Chromium et KaTeX sont des
outils déterministes, pas des modèles.

**Pour une future niche scientifique** (physique-prepa, physique…) : reprendre
`"moteur": "html-katex"`, un `exercices.json` au même schéma, et un fichier
CSS dédié dans `gabarits/` si la palette change. Aucun code à réécrire.

---

## 5. Le vocabulaire (état vérifié)

Fichier : `niches/arabe/vocabulaire.json`

| Famille | Nombre | État |
|---|---|---|
| `mots` | 317 | prêts |
| `mots_francais_arabe` (étymologies) | 34 | **toutes vérifiées par recherche web** |
| `prenoms` | 30 | prêts |

**8 étymologies ont été écartées** après vérification (une première liste
non contrôlée en contenait de fausses) : jardin (vient du francique, pas de
l'arabe — confirmé par l'Académie française et le CNRTL), riz (italien/latin/
grec, pas arabe), tulipe (persan, pas arabe), moutarde (latin), nacre et
tabouret (chaînes étymologiques contestées selon les sources), échec
(persan), safari (chaîne trop indirecte, passage par le swahili). Elles sont
listées avec leur motif dans `vocabulaire.json → _etymologies_ecartees`.
**Ne jamais les réintroduire, même si une recherche web semble les
confirmer ailleurs — la contradiction a déjà été tranchée.**

**Règle pour toute nouvelle étymologie** : vérification systématique par
recherche web avant ajout, en citant une source fiable (CNRTL, Littré,
Académie française, Wiktionnaire). Jamais depuis la mémoire seule d'un
modèle de langage — c'est exactement l'erreur qui a produit les 8 rejets.

---

## 5 bis. Règle hashtags

**4 hashtags maximum dans `hashtags_base`**, plus **au plus 1** spécifique au
type de post dans `construire_legende()`. Jamais plus de 5 au total.

Instagram plafonne techniquement à 5 depuis fin 2025 et les hashtags ne
boostent plus la portée. Éviter les quasi-doublons (`#arabe` + `#languearabe`
+ `#coursdarabe` se chevauchent tous). Ce qui compte davantage : Instagram
indexe le texte de la légende comme un moteur de recherche, d'où l'intérêt de
légendes riches en mots-clés naturels.

Justification complète, études et sources : `../Guide.md` §4.

---
## 6. Contraintes API Meta (Instagram)

- Compte Instagram **Professionnel** (Créateur ou Entreprise, pas Personnel).
  **Depuis le 14/09/2026, plus aucune Page Facebook liée, plus aucun ajout du
  compte comme élément du portefeuille business** — l'app utilise le cas
  d'utilisation « Instagram API with Instagram Login » (pas « Instagram API
  with Facebook Login »), qui ne requiert ni Page ni ces liaisons. C'est un
  changement délibéré suite à un incident (voir « Trois interdits »
  ci-dessous) : lier une Page ou ajouter un compte au portefeuille recrée un
  accès croisé entre niches. La Page Publishing Authorization, spécifique au
  chemin Page Facebook, ne s'applique plus.
- Images à une **URL publique** : l'API Meta les télécharge, on ne peut pas
  lui envoyer les octets directement. D'où l'usage de Cloudinary comme
  hébergeur intermédiaire d'images (gratuit jusqu'à 25 crédits/mois, un
  crédit valant environ 1 Go de stockage, de bande passante nette, ou 1000
  transformations). **« Par mois » décrit la fréquence de vérification, pas
  une remise à zéro** : la bande passante et les transformations sont bien
  réinitialisées chaque mois, mais le stockage est évalué chaque mois sur la
  quantité *actuellement* stockée — comme rien n'est jamais supprimé de
  Cloudinary, ce total grossit mois après mois et c'est lui qui finit par
  heurter le plafond, pas un dépassement du volume mensuel ajouté (voir le
  calcul ci-dessous). Vérifier de temps en temps le tableau de bord
  Cloudinary réel, les conditions du plan gratuit pouvant évoluer.
  **Combien de niches ce système supporte** — mesuré sur un vrai slide
  générés : **183 Ko/slide** pour une niche langue (Pillow, fond photo,
  1080×1080) et **107 Ko/slide** pour une niche scientifique (KaTeX, design à
  plat, 1080×1350). À 2 posts/jour sur 30 jours, cela donne ~22 Mo/mois de
  **nouveau stockage** pour une niche langue (2 slides par post) et ~45 Mo/mois
  pour une niche scientifique (7 slides par post). Les images ne sont **jamais supprimées** de Cloudinary, donc ce
  stockage s'accumule indéfiniment — c'est la seule contrainte qui compte
  réellement à terme (la bande passante, remise à zéro chaque mois, et les
  transformations, quasi nulles ici puisqu'aucune transformation Cloudinary
  n'est appliquée à la livraison, restent négligeables face au plafond de
  25 Go). Sans aucun nettoyage, temps avant d'atteindre les 25 Go de
  stockage selon le nombre de niches actives, toutes au même rythme (3
  posts/jour, 2 slides, taille d'image comparable à celle d'arabe) :

  | Niches simultanées | Stockage ajouté/mois | Plafond 25 Go atteint dans |
  |---|---|---|
  | 6 (plan actuel) | ~147 Mo | ~14,5 ans |
  | 10 | ~246 Mo | ~8,7 ans |
  | 16 | ~393 Mo | ~5,4 ans |
  | 20 | ~491 Mo | ~4,3 ans |
  | 30 | ~737 Mo | ~2,9 ans |

  **En pratique : jusqu'à ~16 niches simultanées tiennent au moins 5 ans sans
  rien nettoyer**, et les 6 niches prévues ont largement plus d'une décennie
  de marge. Au-delà, ou pour repousser l'échéance indéfiniment, il suffira
  d'ajouter un nettoyage automatique (supprimer l'image Cloudinary une fois
  la publication confirmée) — pas nécessaire tant qu'on reste dans ces
  ordres de grandeur. Ce calcul suppose des images de taille comparable à
  celles d'arabe ; un template beaucoup plus lourd (résolution plus haute,
  photos non compressées) déplacerait ces chiffres à la baisse.
- **50 publications maximum par 24h glissantes.** Un carrousel compte pour 1.
- Le jeton d'accès expire tous les **60 jours** — cause n°1 de panne
  silencieuse si on oublie de le renouveler. **Depuis le 2026-09-12,
  automatisé** par `.github/workflows/renouveler_token.yml` (exécuté deux
  fois par mois via `renouveler_token.py`) ; **depuis le 14/09/2026**, ce
  renouvellement passe par l'endpoint Instagram Login
  `graph.instagram.com/refresh_access_token` (`ig_refresh_token`), qui ne
  nécessite que le jeton lui-même (pas d'App ID). Un repli sur
  `graph.instagram.com/access_token` (`ig_exchange_token`, avec l'App
  Secret) existe pour le cas rare d'un jeton encore court, jamais échangé.
  Le script met à jour le secret GitHub `IG_TOKEN_<NICHE>` directement par
  API. Deux secrets suffisent, une seule fois pour tout le dépôt (partagés
  entre toutes les niches) : `META_APP_SECRET` (Meta for Developers → l'app
  « Niches Auto » → Paramètres de l'app → Général) et `GH_PAT_SECRETS` (un
  token GitHub personnel *fine-grained*, limité à ce dépôt, permission
  Secrets en lecture/écriture — c'est le seul moyen d'écrire un secret par
  API, le `GITHUB_TOKEN` automatique des workflows n'en a pas le droit par
  sécurité). **Pour activer une nouvelle niche**, ajouter sa ligne
  `IG_TOKEN_<NICHE>: ${{ secrets.IG_TOKEN_<NICHE> }}` dans le bloc `env` de
  `renouveler_token.yml` — le script lui-même n'a rien d'autre à changer,
  il lit `niches/config.json` et ne traite que les niches `"actif": true`.
- **Une seule app Meta partagée** (« Niches Auto ») porte toutes les niches :
  chaque nouveau compte n'a besoin que du rôle de testeur Instagram sur
  cette app (onglet Rôles du cas d'utilisation Instagram Login), plus aucune
  gestion de Page Facebook ni de portefeuille business par niche.
- Ces étapes (rôle de testeur, génération du jeton) nécessitent des écrans
  de consentement humain sur le site Meta. Aucun agent IA ne peut les
  compléter à la place de l'utilisatrice — il peut seulement l'expliquer
  pas à pas et l'aider à câbler la valeur finale dans les secrets GitHub.

---

## 7. Lancer une nouvelle niche

La procédure complète est dans **`MISE-EN-PLACE.md`**, écrit pour être lu par
un agent qui conduit ensuite l'entretien avec l'utilisatrice : quelles
questions poser, où trouver chaque valeur côté Meta, Cloudinary et GitHub,
quels secrets créer, et le rapport de ce qui bloque.

En résumé, ce qui change quand on ajoute une niche :

| Fichier | Modification |
|---|---|
| `niches/config.json` | un bloc, copié d'une niche voisine |
| `niches/<id>/` | contenu, `fonds/` (niches Pillow uniquement), `sortie/` |
| `.github/workflows/renouveler_token.yml` | une ligne `IG_TOKEN_<NICHE>` dans `env` |
| `.github/workflows/publier.yml` | une étape, si la niche a son propre moteur |
| GitHub → Settings → Secrets | `IG_USER_ID_<NICHE>` et `IG_TOKEN_<NICHE>` |

Aucune ligne de `publier.py` ni de `generer.py` n'est à toucher.

---
## 8. Inventaire du dépôt

```
insta-auto/
├── GUIDE.md                    ce document (technique)
├── MISE-EN-PLACE.md            script d'entretien pour lancer une niche
├── publier.py                  orchestrateur multi-niches
├── generer.py                  rendu Pillow — 1080×1080, 2 slides
├── generer_maths.py            rendu Chromium + KaTeX — 1080×1350, 7 slides
├── renouveler_token.py         échange du jeton Meta avant expiration
├── requirements.txt
├── .env.example                liste des secrets attendus
├── .github/workflows/
│   ├── publier.yml             cron 2×/jour, midi et soir + déclenchement manuel
│   └── renouveler_token.yml    2×/mois, écrit le nouveau secret par API
├── gabarits/
│   └── structure-gelules.css         système visuel du moteur HTML
├── vendor/
│   ├── katex/                  KaTeX + ses polices, embarqués
│   └── inter/                  Inter, embarquée
├── polices/                    Noto Naskh Arabic, Noto Sans JP, Noto Sans KR, Playfair Display
├── exemple_etymologie.png      rendu de référence du template Pillow
└── niches/
    ├── config.json             une entrée par niche
    ├── arabe/                  actif — 317 mots, 34 étymologies, 30 prénoms, 57 fonds
    ├── japonais/  coreen/      contenu prêt, comptes à créer
    ├── maths-prepa/            moteur prêt, 2 exercices, + README.md
    └── physique-prepa/           réservé
```

**Une seule copie des photos de fond arabes existe**, dans
`niches/arabe/fonds/`. Le générateur de l'ebook y pointe par chemin relatif.
Toute nouvelle photo va là, nulle part ailleurs.
