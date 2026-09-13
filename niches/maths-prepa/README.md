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

Deux chartes graphiques sont disponibles. Elles utilisent **les mêmes classes
HTML** : changer de charte, c'est changer une seule valeur dans
`niches/config.json`, rien d'autre.

| `"gabarit"` | Charte | Ce qui la caractérise |
|---|---|---|
| `structure-gelules.css` *(actuel)* | Slack | Aubergine `#4a154b`, mesh pastel, gélules 90 px, cartes lavande |
| `structure-tuiles.css` | Apple | Tuiles pleines alternées blanc / `#272729`, un seul accent `#0066cc`, aucun dégradé, cartes parchemin à filet 1 px, une unique ombre réservée à la formule clé |

### Palettes

Chaque structure se décline en cinq palettes. Une palette est un fichier CSS de
quinze lignes : il importe la structure et ne redéfinit que des couleurs.
Aucune règle n'est dupliquée.

| Palette | Fond profond | Accent | Caractère |
|---|---|---|---|
| Encre & Indigo | `#131a2e` | `#33469f` | bleu encre, le plus « copie et stylo » |
| Prusse & Sable | `#0e2439` | `#2a6ba8` | bleu scientifique, papier sable |
| Vert Académie | `#12241d` | `#2f6f52` | reliure ancienne, calme |
| Ardoise & Cuivre | `#1e2126` | `#a86432` | gris froid réchauffé par le cuivre |
| Nuit & Ambre | `#15161c` | `#a8792e` | presque noir, accent doré |

Fichiers : `gelules-<palette>.css` pour la structure Slack,
`tuiles-<palette>.css` pour la structure Apple.

Chaque palette porte une ligne commentée `--grille` : la décommenter ajoute un
quadrillage très pâle façon papier millimétré sur les slides claires. C'est le
signal « maths » le moins coûteux du système.

Chartes sources dans `../../../atelier/maths-prepa/design/`. Aperçus rendus
dans `../../../atelier/maths-prepa/apercu-template/` :
`palettes-structure-slack.png`, `palettes-structure-apple.png`,
`effet-grille.png`.

Pour essayer une charte sans toucher à la production :

```bash
python3 generer_maths.py --exercice llg-absurde-21 --sortie /tmp/essai
```

après avoir changé `"gabarit"` dans `config.json`. Une charte inexistante fait
échouer le rendu avec un message explicite plutôt que de produire une slide nue.

### La charte Slack en place


Repris de `../../../atelier/maths-prepa/design/DESIGN-slack.md` : aubergine
`#4a154b`, crème `#f4ede4`, lavande `#f9f0ff`, pills 90 px, Inter, mesh
pastel. Alternance sombre → clair → sombre : accroche, démonstration,
conversion. Tokens et composants dans `gabarits/structure-gelules.css`.

## Écrire un exercice

Tout est dans `exercices.json` (voir `_schema` en tête de fichier).

> **Ne jamais ouvrir les PDF de `sources/` ni de `bibliotheque/`.** Un poly
> scanné coûte plus de contexte qu'une session entière de travail. On travaille
> exclusivement sur les `.md`, et on rédige les mathématiques à la main.
>
> **Les `.md` de `atelier/maths-prepa/sources/` sont des OCR de PDF : toutes les
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
