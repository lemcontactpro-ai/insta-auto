# Automatisation Instagram — Guide complet et instructions d'exécution

Ce document est autosuffisant : il ne suppose aucune conversation préalable.
Il s'adresse à la fois à l'utilisatrice (Amy) et à tout agent IA exécutant
la mise en place (Claude Code, Antigravity, ou autre).

---

## 0. Instructions pour l'agent exécutant

Si tu es un agent IA chargé de mettre en place ce projet, lis cette section
en premier.

**Contexte de départ :** ce dossier contient déjà tout le code, la
configuration et le vocabulaire nécessaires. Rien n'est à réécrire depuis
zéro. Ta mission est d'exécuter la mise en place décrite en section 7, pas
de redessiner l'architecture.

**Étape à faire en premier — localiser les photos de fond :**
Le dossier de travail contient, quelque part, un sous-dossier avec des
photos destinées à servir de fond aux visuels Instagram (architecture
marocaine/arabe, ruelles, mosaïques, etc.). Ce sous-dossier n'est **pas**
`niches/arabe/fonds/` — il faut le localiser (cherche un dossier contenant
des fichiers `.jpg`, `.jpeg`, `.png` ou `.webp` en dehors de l'arborescence
du projet décrite en section 3), puis **copier toutes ses images** dans
`niches/arabe/fonds/` (ce dossier existe déjà, vide, avec un fichier
`.gitkeep` à conserver ou supprimer selon convenance).

**Ne modifie pas** sans instruction explicite de l'utilisatrice :
- Le vocabulaire dans `niches/arabe/vocabulaire.json` — en particulier ne
  jamais réintroduire les entrées listées dans `_etymologies_ecartees`
  (voir section 5).
- Le template visuel dans `generer.py` — en particulier la règle de
  placement vertical mesuré (voir section 4).
- Les choix d'architecture (GitHub Actions, pas de Google Drive, pas de
  Cowork, pas de Claude Code Routines) — les raisons sont données en
  section 2, ne pas les reproposer sans qu'on te le demande.

**N'invente jamais** de valeurs de secrets (jetons, clés API). Si un secret
manque, arrête-toi et demande à l'utilisatrice de le fournir — voir section
6 et étape F.

**Sur la vérification du vocabulaire :** si on te demande d'ajouter des mots
ou des étymologies, vérifie systématiquement chaque étymologie par une
recherche web avant de l'ajouter. Ne te fie jamais à ta mémoire seule sur ce
point — une première tentative sans vérification a produit 8 erreurs sur 30
(détail en section 5).

---

## 1. Le projet en une phrase

Publier automatiquement 3 posts/jour sur plusieurs comptes Instagram
thématiques (niches), chacun vendant un ebook, sans intervention manuelle et
sans que l'ordinateur de l'utilisatrice soit allumé.

**Niche 1** : @arabe.academie — apprentissage de l'arabe, public francophone.
**Niches futures** : 6 au total prévues, même système, contenu et palette
différents à chaque fois.

---

## 2. Les décisions prises (et pourquoi)

### Hébergement : GitHub Actions
- **Gratuit**, illimité en dépôt public, 2000 min/mois en privé (largement
  suffisant : 6 niches × 3 posts/jour × 30 jours ≈ 540 minutes utilisées).
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

### Structure des conversations Claude : par sujet, pas par niche
Si l'utilisatrice travaille aussi dans un Projet claude.ai en parallèle :
une conversation par sujet technique (GitHub, Meta, contenu, template),
réutilisée pour toutes les niches, plutôt qu'un jeu complet de conversations
dupliqué à chaque nouvelle niche.

### Cowork : non pertinent ici
Cowork est un outil de travail collaboratif humain-Claude sur des tâches de
connaissance, pas un planificateur de tâches récurrentes. Aucune utilité
pour ce projet.

---

## 3. Architecture technique

```
insta-auto/                          (dépôt GitHub, à créer)
├── .github/workflows/publier.yml    # cron 3x/jour, appelle publier.py
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

## 6. Contraintes API Meta (Instagram)

- Compte Instagram **Professionnel**, lié à une Page Facebook.
- **Page Publishing Authorization (PPA)** obligatoire — son absence cause un
  échec silencieux, sans message d'erreur clair.
- Images à une **URL publique** : l'API Meta les télécharge, on ne peut pas
  lui envoyer les octets directement. D'où l'usage de Cloudinary comme
  hébergeur intermédiaire d'images (gratuit jusqu'à 25 crédits/mois, largement
  suffisant pour ce volume).
- **50 publications maximum par 24h glissantes.** Un carrousel compte pour 1.
- Le jeton d'accès expire tous les **60 jours** — cause n°1 de panne
  silencieuse si on oublie de le renouveler.
- **Un seul compte Facebook peut administrer plusieurs Pages**, donc gérer
  les 6 niches prévues sans multiplier les comptes Meta.
- Ces étapes (création app Meta, PPA, jeton) nécessitent des écrans de
  consentement humain sur le site Meta/Facebook. Aucun agent IA ne peut les
  compléter à la place de l'utilisatrice — il peut seulement l'expliquer
  pas à pas et l'aider à câbler la valeur finale dans les secrets GitHub.

---

## 7. Étapes à suivre, dans l'ordre

### Étape A — Localiser et copier les photos de fond
Voir section 0. Copier toutes les images du dossier personnel de
l'utilisatrice vers `niches/arabe/fonds/`. Minimum recommandé : 15-20
photos pour une rotation correcte, idéalement 50+.

### Étape B — Créer le dépôt GitHub
Créer un nouveau dépôt (public ou privé, les deux fonctionnent — public
donne un quota d'exécution illimité). Nom suggéré : `insta-auto`.

### Étape C — Pousser les fichiers dans le dépôt
Initialiser git dans le dossier de travail (s'il ne l'est pas déjà),
committer l'ensemble de l'arborescence décrite en section 3 (avec les
photos maintenant présentes dans `niches/arabe/fonds/`), pousser vers le
dépôt GitHub créé à l'étape B.

### Étape D — Connecter Instagram à l'API Meta
Étapes nécessitant l'utilisatrice elle-même (voir section 6) : compte Pro,
Page Facebook, PPA, création de l'app Meta, permissions, récupération de
l'IG User ID, génération d'un jeton longue durée. Un agent IA (Claude Code
via terminal, par exemple) peut guider pas à pas à travers chaque écran,
mais ne peut pas cliquer à la place de l'utilisatrice sur les écrans de
consentement Meta.

### Étape E — Créer un compte Cloudinary
Gratuit, sert à héberger temporairement les images le temps que Meta les
récupère. Compte en quelques minutes sur cloudinary.com.

### Étape F — Configurer les secrets GitHub
Dans le dépôt : Settings → Secrets and variables → Actions → New repository
secret. Créer chaque secret listé dans `.env.example` avec sa vraie valeur
(`IG_USER_ID_ARABE`, `IG_TOKEN_ARABE`, `CLOUDINARY_CLOUD_NAME`,
`CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`).

**Un secret n'est jamais écrit dans le code ni collé dans une session
d'agent IA.** Il doit être saisi directement dans l'interface web GitHub par
l'utilisatrice, pour éviter qu'il reste visible dans un historique de
terminal ou de conversation. Si le jeton se trouvait dans `publier.py`,
n'importe qui consultant un dépôt public pourrait le voler.

### Étape G — Tester en simulation
Localement, ou via le déclenchement manuel du workflow GitHub Actions
(`workflow_dispatch`, avec l'option `dry_run` déjà prévue dans
`.github/workflows/publier.yml`) :
```bash
python3 publier.py --niche arabe --dry-run
```
Vérifier l'image générée et la légende, sans rien publier.

### Étape H — Première publication réelle
```bash
python3 publier.py --niche arabe
```
Vérifier que le post apparaît sur Instagram.

### Étape I — Confirmer l'activation du cron
Une fois poussé dans le dépôt, l'onglet **Actions** du dépôt GitHub doit
montrer les 3 tâches programmées (8h, 13h30, 19h heure de Paris, converties
en UTC dans le fichier). Aucune autre action nécessaire ensuite — ça tourne
seul, indéfiniment.

**Point de vigilance saisonnier** : GitHub Actions raisonne en UTC. Le
fichier est calé sur l'heure d'hiver (UTC+1). Au passage à l'heure d'été
(UTC+2), il faudra décaler les horaires cron d'une heure dans
`.github/workflows/publier.yml`.

### Étape J — Répéter pour les niches suivantes
Une fois Arabe stable depuis quelques semaines : copier un bloc dans
`config.json`, créer le dossier `niches/<nouvelle-niche>/` avec son
vocabulaire (vérifié selon la règle de la section 5) et ses photos, répéter
les étapes D à F pour le nouveau compte Instagram.

---

## 8. Contenu de ce dossier / de cette archive

- `GUIDE.md` — ce document
- `publier.py` — script d'orchestration
- `generer.py` — générateur de slides
- `requirements.txt` — dépendances Python
- `.env.example` — modèle des secrets à créer sur GitHub
- `.github/workflows/publier.yml` — planification GitHub Actions
- `niches/config.json` — configuration centrale des niches
- `niches/arabe/vocabulaire.json` — vocabulaire vérifié (317 mots, 34
  étymologies, 30 prénoms)
- `niches/arabe/fonds/` — dossier vide à remplir (voir section 0 / étape A)
- `polices/` — les deux polices nécessaires au rendu
- `exemple_etymologie.png` — rendu de référence à jour du template

**Rien d'autre n'est nécessaire.** Ne pas régénérer le code, la config ou
le vocabulaire depuis zéro : tout est déjà prêt, seule la mise en place
(sections 0 et 7) reste à exécuter.
