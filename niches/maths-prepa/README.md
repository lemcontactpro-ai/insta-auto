# Niche, Maths Prépa (@maths.prepa)

Carrousels Instagram de **8 slides maximum** : un énoncé, la résolution
étape par étape, un CTA. Statut : template et moteur prêts, contenu à
enrichir, compte Instagram à créer (`actif: false` dans `niches/config.json`).

## Ce qui change par rapport aux niches langues

| | Niches langues | maths-prepa |
|---|---|---|
| Moteur | `generer.py` (Pillow) | `generer_maths.py` (Chromium + KaTeX) |
| Format | 1080 × 1080 | 1080 × 1350 (4:5) |
| Slides | 2 | jusqu'à 7 |
| Fond | photo dans `fonds/` | aucun, design plat, `fonds/` est inutilisé |
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
Jusqu'à 6 étapes : une par slide. Au-delà, `repartir()` regroupe les étapes
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
> `verifie: false` tant que ce n'est pas fait, `publier.py` ne publie que
> les exercices vérifiés.

Attention aux contre-obliques : dans le JSON on écrit `\sqrt`, pas
`\\sqrt`. Un échappement doublé ne provoque **aucune erreur KaTeX**, il
compose le nom de la commande en italique. Le contrôleur intégré détecte ce
cas, le lancer après toute modification :

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

1. Enrichir `exercices.json`, objectif 40 à 60 exercices vérifiés, répartis
   sur les chapitres et les 4 niveaux de difficulté.
2. Créer le compte Instagram professionnel (Entreprise, sans le lier à une
   Page Facebook ni au portefeuille business, voir `MISE-EN-PLACE.md`,
   « Trois interdits »).
3. Donner au compte le rôle de testeur sur l'app Meta « Niches Auto », puis
   récupérer l'IG User ID et le jeton longue durée.
4. Renseigner les secrets GitHub `IG_USER_ID_MATHS_PREPA` et
   `IG_TOKEN_MATHS_PREPA`.
5. Ajouter `IG_TOKEN_MATHS_PREPA: ${{ secrets.IG_TOKEN_MATHS_PREPA }}` dans
   le bloc `env` de `.github/workflows/renouveler_token.yml`.
6. Passer `"actif": true` dans `niches/config.json`. Le workflow de
   publication installe alors Chromium tout seul et la niche part.

## Règle de rédaction : rien de parachuté

Un post n'est publiable que si un lecteur qui **découvre** l'exercice peut
refaire chaque ligne sans rien deviner.

1. **Toute équation est établie devant le lecteur.** En physique : système,
   référentiel, bilan des forces, axe, projection, puis seulement l'équation.
   En maths : d'où vient l'expression manipulée, sur quel domaine, sous
   quelles hypothèses.
2. **Tout choix est justifié.** Pourquoi cet axe et pas l'autre, pourquoi
   cette forme canonique, pourquoi ce changement de variable, pourquoi une
   solution particulière constante. Le résultat sans le « pourquoi »
   n'apprend rien.
3. **Les astuces de calcul sont dites.** Contrôle d'homogénéité, identité
   remarquable à repérer, cas limite qui valide le résultat, raccourci qui
   évite la résolution complète.
4. **Le domaine de validité est nommé** quand il existe : frottement linéaire
   aux faibles vitesses, hypothèse de positivité, petits angles.

Un saut logique dans une correction est un défaut bloquant, au même titre
qu'une erreur de calcul : `verifie: true` ne se pose pas tant qu'il reste une
ligne qui tombe du ciel.

Six étapes sont disponibles (8 slides, énoncé et CTA compris). Une étape dense
vaut mieux qu'un raccourci : le moteur réduit la typo automatiquement (`--fit`)
jusqu'à 0,70.

### La mise en place se lit en lignes, jamais en paragraphe

En mécanique, le trio système / référentiel / bilan des forces s'écrit avec le
bloc `poser`, une ligne par élément. La méthode doit se voir au premier coup
d'œil, c'est ce qui montre qu'on la maîtrise.

```json
{"type": "poser", "lignes": [
  {"cle": "Système",         "valeur": "la bille seule, de masse $m$ constante."},
  {"cle": "Référentiel",     "valeur": "le laboratoire, supposé galiléen."},
  {"cle": "Bilan des forces","valeur": "le poids $m\\vec{g}$ et le frottement $-\\lambda\\vec{v}$."},
  {"cle": "Axe",             "valeur": "$Oz$ vertical, orienté vers le bas."}
]}
```

### Deux interdits contrôlés automatiquement

**Le tiret cadratin «, » est banni**, dans toutes les niches et dans tous les
champs affichés. On écrit une virgule, un deux-points, une parenthèse, ou une
phrase de plus. `--valider` refuse l'exercice, et `publier.py` refuse la
légende.

**Le texte ne sort jamais du cadre.** Le rendu réduit la typo tant qu'un
contenu déborde, en hauteur comme en largeur, formules comprises (elles ne
s'enroulent plus, elles rétrécissent). S'il n'y arrive pas, il lève une erreur
au lieu de produire une slide tronquée. À passer avant toute publication :

```bash
python3 generer_maths.py --niche physique-prepa --controle
```

### Unités : point de multiplication obligatoire

Une unité composée s'écrit avec un point de multiplication, jamais avec une
espace : `\mathrm{m\cdot s^{-1}}`, `\mathrm{kg\cdot s^{-1}}`,
`\mathrm{J\cdot K^{-1}\cdot mol^{-1}}`. Une unité posée en « m s-1 » se lit
comme un produit de variables et trompe le lecteur. `--valider` refuse
`\mathrm{m\,s^{-1}}`.

Un résultat se donne toujours en entier, valeur **et** unité complète,
exposant compris. Si la ligne est trop longue, on la coupe en
`\begin{gathered}` : jamais de valeur sans son unité pour gagner de la place.

### Une couleur par domaine

Le champ `chapitre` d'un exercice doit valoir exactement une clé de
`domaines` dans `niches/config.json`. Il décide de deux choses : la palette du
post, et les lignes obligatoires de la mise en place.

| Domaine | Palette | Mise en place imposée |
|---|---|---|
| Mécanique | aubergine | Système, Référentiel, Bilan des forces |
| Optique | cobalt | Système optique, Sens de propagation, Conventions |
| Électrocinétique | émeraude | Circuit, Conventions, Régime |
| Ondes et signaux | sarcelle | Système, Grandeur étudiée, Hypothèses |
| Électromagnétisme | indigo | Système, Champ, Orientation |
| Thermodynamique | brique | Système, Transformation, Hypothèses |
| Chimie | ocre | Système, Réaction, Conditions |
| Méthodes | graphite | Grandeur cherchée, Données, Hypothèses |

Les palettes sont générées par `faire_palettes.py` : pour changer une couleur,
on modifie la couleur de base du domaine dans ce script et on le relance.

Le contrôleur refuse un exercice dont le chapitre n'est pas un domaine connu,
et un exercice dont la première étape ne porte pas le bloc `poser` avec les
lignes imposées. La méthode ne dépend donc plus de la vigilance du rédacteur,
elle est vérifiée à chaque publication.

### Les titres portent le nom de la notion

Ces posts sont des **cartes de révision** : le titre doit faire écho
immédiatement à un chapitre de cours. On écrit « L'effet Doppler », « Chute
verticale avec frottement fluide », « Le théorème des gendarmes », jamais
« L'ambulance qui change de note » ni « La bille qui cesse d'accélérer ».

La formule imagée n'est pas perdue : elle va dans `accroche`, qui n'apparaît
que dans la légende Instagram, là où elle sert à accrocher le lecteur. Le
titre, lui, sert à ranger la carte dans sa mémoire.

Les 50 exercices de maths ont été renommés sur cette règle le 15/09/2026,
leurs anciens titres sont devenus des accroches.

### Chaque post de physique porte un schéma

Une carte de révision sans figure est incomplète. Le bloc `schema` contient un
SVG écrit à la main dans le JSON :

```json
{"type": "schema",
 "legende": "Axe orienté dans le sens du mouvement.",
 "svg": "<svg viewBox=\"0 0 560 300\"> ... </svg>"}
```

Trois contraintes, vérifiées par `--valider` :

- un `viewBox`, sans quoi la figure ne se met pas à l'échelle ;
- aucune ressource externe (pas d'`<image>`, pas d'URL) : le rendu doit être
  identique en local et sur GitHub Actions, sans réseau ;
- tracé en `currentColor`, pour que la figure suive la couleur de la slide et
  reste lisible sur fond sombre comme sur fond clair.

Le schéma est obligatoire dans tous les domaines sauf `Méthodes`
(`schema_obligatoire` dans `niches/config.json`). En maths il reste
facultatif, mais une figure vaut mieux qu'un paragraphe dès qu'il y a une
géométrie, une courbe ou un encadrement à visualiser.
