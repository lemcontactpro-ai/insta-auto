# Niche — Maths Prépa (@maths.prepa)

Carrousels Instagram de **7 slides maximum** : un énoncé, la résolution
étape par étape, un CTA. Statut : template et moteur prêts, contenu à
enrichir, compte Instagram à créer (`actif: false` dans `niches/config.json`).

## Ce qui change par rapport aux niches langues

| | Niches langues | maths-prepa |
|---|---|---|
| Moteur | `generer.py` (Pillow) | `generer_maths.py` (Chromium + KaTeX) |
| Format | 1080 × 1080 | 1080 × 1350 (4:5) |
| Slides | 2 | jusqu'à 7 |
| Fond | photo dans `fonds/` | aucun — design plat, `fonds/` est inutilisé |
| Contenu | `vocabulaire.json` | `exercices.json` |

Pillow ne sait pas composer de mathématiques (fractions, intégrales,
racines). Le rendu passe donc par un document HTML que Chromium
photographie, avec KaTeX pour le LaTeX. KaTeX et la police Inter sont
**embarqués dans le dépôt** (`vendor/`) : aucun appel réseau au rendu, donc
un résultat identique en local et sur GitHub Actions.

## Structure d'un carrousel

```
slide 1        énoncé + étoiles de difficulté   (aubergine)
slides 2 … 6   résolution, une étape par slide  (clair)
slide 7        CTA « Lien en bio »              (aubergine)
```

**Répartition des étapes.** 5 slides sont disponibles pour la résolution.
Jusqu'à 5 étapes : une par slide. Au-delà, `repartir()` regroupe les étapes
**contiguës** en 5 paquets en minimisant le paquet le plus chargé (le poids
d'une étape compte les formules bien plus que le texte). Deux étapes sur une
même slide sont séparées par un filet. Pour forcer un découpage à la main,
donner un `"groupe": <entier>` à **toutes** les étapes de l'exercice.

**Auto-ajustement.** Si un contenu dépasse la hauteur de la slide, la
variable CSS `--fit` réduit la typographie par paliers de 4 % jusqu'à 70 %.
Le rendu signale toute réduction, et refuse de se taire si ça déborde encore.

## Design

Repris de `../../../maths-prépa/design/DESIGN-slack.md` : aubergine
`#4a154b`, crème `#f4ede4`, lavande `#f9f0ff`, pills 90 px, Inter, mesh
pastel. Alternance sombre → clair → sombre : accroche, démonstration,
conversion. Tokens et composants dans `gabarits/maths_prepa.css`.

## Écrire un exercice

Tout est dans `exercices.json` (voir `_schema` en tête de fichier).

> **Les `.md` de `maths-prépa/sources/` sont des OCR de PDF : toutes les
> formules en affichage ont été perdues et le LaTeX inline est mangé.** Ils
> servent à repérer les exercices, jamais à copier du contenu. Chaque
> exercice est rédigé à la main depuis le PDF, puis relu ligne à ligne.
> `verifie: false` tant que ce n'est pas fait — `publier.py` ne publie que
> les exercices vérifiés.

Attention aux contre-obliques : dans le JSON on écrit `\sqrt`, pas
`\\sqrt`. Un échappement doublé ne provoque **aucune erreur KaTeX**, il
compose le nom de la commande en italique. Le contrôleur intégré détecte ce
cas — le lancer après toute modification :

```bash
python3 generer_maths.py --valider
```

## Commandes

```bash
python3 generer_maths.py --valider                    # contrôle tout exercices.json
python3 generer_maths.py                              # rend le premier exercice
python3 generer_maths.py --exercice sl-suites-1       # rend un exercice précis
python3 publier.py --niche maths-prepa --dry-run      # chaîne complète, sans publier
```

Prérequis local : `pip install -r requirements.txt` puis
`python3 -m playwright install chromium`.

## Reste à faire

1. Enrichir `exercices.json` — objectif 40 à 60 exercices vérifiés, répartis
   sur les chapitres et les 4 niveaux de difficulté.
2. Créer le compte Instagram professionnel + la Page Facebook + la PPA.
3. Créer l'app Meta, récupérer l'IG User ID et le jeton longue durée.
4. Renseigner les secrets GitHub `IG_USER_ID_MATHS_PREPA` et
   `IG_TOKEN_MATHS_PREPA`.
5. Ajouter `IG_TOKEN_MATHS_PREPA: ${{ secrets.IG_TOKEN_MATHS_PREPA }}` dans
   le bloc `env` de `.github/workflows/renouveler_token.yml`.
6. Passer `"actif": true` dans `niches/config.json`. Le workflow de
   publication installe alors Chromium tout seul et la niche part.
