# Niche, Physique Prépa (@physique.prepa)

Même moteur et même structure de carrousel que maths-prépa : 8 slides
maximum, énoncé avec étoiles de difficulté, une slide par étape, CTA.
Voir `../maths-prepa/README.md` pour le détail du fonctionnement, il est
identique.

## Ce qui est arrêté

| Point | Valeur |
|---|---|
| Moteur | `html-katex` (Chromium + KaTeX) |
| Gabarit | `gelules-aubergine.css`, structure Slack, palette aubergine d'origine |
| Format | 1080 × 1350 |
| Fonds photo | aucun, design plat |
| Compte | `@physique.prepa`, provisoire |
| CTA | « Une notion par jour, / la physique qui tient. » |

## Ce qui manque

1. **Le contenu.** `exercices.json` est vide, seul le schéma est en place.
   Objectif 40 à 60 exercices vérifiés, minimum 21 pour ne pas recycler dans
   la semaine. Même règle qu'en maths : rédaction à la main, relecture ligne
   à ligne, `verifie: true` seulement une fois relu.
2. **Les sources.** 30 épreuves complètes de Sup (CB, DM, DS) sont disponibles et organisées dans `DS Sup physique/epreuves/` avec énoncés et corrigés en PDF et en Markdown OCR pour faciliter la rédaction des exercices sans surconsommation de tokens.
3. **Le compte Instagram**, l'app Meta et les secrets GitHub.

## Particularité de la physique

Contrairement aux maths, la physique manipule des **unités** et des **ordres
de grandeur**. Deux conventions à tenir dès le premier exercice :

- Écrire les unités en romain, jamais en italique : `\mathrm{m\,s^{-1}}` et
  non `m s^{-1}`. KaTeX compose sinon les unités comme des variables.
- Séparer valeur et unité par une espace fine : `5{,}0 \times 10^{3}\;
  \mathrm{N}`.

Le contrôleur (`generer_maths.py --valider`) ne détecte pas ces deux erreurs.
Elles se voient au rendu.

## Commandes

```bash
python3 generer_maths.py --valider                       # contrôle exercices.json
python3 publier.py --niche physique-prepa --dry-run      # chaîne complète
```

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
