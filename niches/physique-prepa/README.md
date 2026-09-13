# Niche — Physique Prépa (@physique.prepa)

Même moteur et même structure de carrousel que maths-prépa : 7 slides
maximum, énoncé avec étoiles de difficulté, une slide par étape, CTA.
Voir `../maths-prepa/README.md` pour le détail du fonctionnement, il est
identique.

## Ce qui est arrêté

| Point | Valeur |
|---|---|
| Moteur | `html-katex` (Chromium + KaTeX) |
| Gabarit | `gelules-aubergine.css` — structure Slack, palette aubergine d'origine |
| Format | 1080 × 1350 |
| Fonds photo | aucun, design plat |
| Compte | `@physique.prepa`, provisoire |
| CTA | « Une notion par jour, / la physique qui tient. » |

## Ce qui manque

1. **Le contenu.** `exercices.json` est vide, seul le schéma est en place.
   Objectif 40 à 60 exercices vérifiés, minimum 21 pour ne pas recycler dans
   la semaine. Même règle qu'en maths : rédaction à la main, relecture ligne
   à ligne, `verifie: true` seulement une fois relu.
2. **Les sources.** Aucun polycopié n'a encore été fourni pour la physique.
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
