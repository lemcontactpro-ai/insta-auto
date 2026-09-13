# Mise en place d'une niche

**Ce document est un script d'entretien.** Un agent IA le lit, puis pose à
l'utilisatrice toutes les questions nécessaires au lancement d'un nouveau
compte, dans l'ordre, en indiquant à chaque fois où trouver la réponse. À la
fin, il produit un rapport de ce qui est prêt et de ce qui bloque.

Le code, les workflows et les deux moteurs de rendu existent déjà. Rien n'est à
développer. Ce qui reste est de la configuration, du contenu et des comptes
externes.

---

## 0. Instructions à l'agent

Lis ce document en entier avant de poser la première question.

**Conduite de l'entretien.** Une question à la fois, dans l'ordre des phases.
Utilise l'outil de question à choix multiples quand les options sont connues,
du texte libre sinon. N'enchaîne pas dix questions d'un coup. Après chaque
réponse, écris immédiatement la valeur dans `niches/config.json` plutôt que de
tout accumuler pour la fin.

**Ne demande jamais un secret dans la conversation.** Aucun jeton, aucune clé
API, aucun mot de passe ne doit être collé dans un chat ni écrit dans un
fichier du dépôt. Ton rôle sur les secrets se limite à dire : *voici le nom du
secret à créer, voici où le trouver, voici où le coller*. Si l'utilisatrice te
donne une valeur de secret quand même, ne l'écris nulle part et redis-lui de la
saisir directement dans l'interface GitHub.

**Ne saute pas une phase parce qu'elle a l'air faite.** Lance d'abord
l'inventaire de la phase 1, il te dira ce qui existe réellement.

**Ce que tu ne peux pas faire à sa place**, et qu'il faut annoncer tôt pour
qu'elle s'organise :

- créer le compte Instagram et la Page Facebook ;
- valider les écrans de consentement Meta et la Page Publishing Authorization ;
- saisir les secrets dans GitHub ;
- fournir les photos de fond ;
- décider du nom définitif du compte.

**À la fin**, produis le rapport de la phase 8. Ne déclare jamais une niche
prête si un point bloquant reste ouvert.

---

## 1. Inventaire, avant toute question

Lance ces commandes depuis `insta-auto/` et lis le résultat. Il détermine
quelles phases sont déjà couvertes.

```bash
# la niche existe-t-elle dans la config, et dans quel état ?
python3 - <<'PY'
import json
for n in json.load(open('niches/config.json'))['niches']:
    print(f"{n['id']:14} actif={str(n.get('actif')):5} compte={n.get('compte','?'):22} "
          f"moteur={n.get('moteur','pillow'):11} contenu={n.get('contenu','vocabulaire.json')}")
    if n.get('_todo'): print(f"{'':14} TODO: {n['_todo'][:120]}")
PY

# contenu et fonds présents ?
for d in niches/*/; do
  n=$(basename "$d")
  [ "$n" = "config.json" ] && continue
  c=$(ls "$d" 2>/dev/null | grep -E 'vocabulaire.json|exercices.json' | head -1)
  f=$(ls "$d/fonds" 2>/dev/null | grep -icE '\.(jpg|jpeg|png|webp)$')
  echo "$n : contenu=${c:-AUCUN}  fonds=$f images"
done

# la niche est-elle câblée dans le renouvellement automatique du jeton ?
grep -c 'IG_TOKEN_' .github/workflows/renouveler_token.yml
grep 'IG_TOKEN_' .github/workflows/renouveler_token.yml
```

Résume à l'utilisatrice, en trois lignes, l'état trouvé, puis annonce les
phases qui restent à couvrir.

---

## 2. Identité de la niche

| # | Question | Où trouver la réponse | Écrit dans |
|---|---|---|---|
| 2.1 | Quel est l'identifiant technique de la niche ? | Minuscules, sans accent ni espace : `coreen`, `maths-prepa`. Sert de nom de dossier et de suffixe de secret. | `config.json → id`, dossier `niches/<id>/` |
| 2.2 | Quel est le nom du compte Instagram ? | Le handle définitif, avec l'arobase. **S'affiche sur chaque slide**, donc il doit être arrêté avant la première publication. | `config.json → compte` |
| 2.3 | Que vend ce compte ? | L'ebook ou le produit vers lequel pointe la bio. Détermine le texte du CTA. | `config.json → textes` |
| 2.4 | À quelles heures publier ? | **Deux créneaux par jour, midi et soir**, identiques pour toutes les niches : 12:30 et 19:00, heure de Paris. Ne pas s'en écarter sans raison, le cron est commun à tout le dépôt. | `config.json → horaires` **et** le cron de `.github/workflows/publier.yml`, en UTC |

**Piège du cron.** GitHub Actions raisonne en UTC fixe. Le champ `horaires` de
`config.json` est documentaire : c'est le cron du workflow qui décide vraiment.
Convertir en UTC selon l'heure en vigueur, et prévoir le décalage d'une heure
aux changements d'heure (fin mars, fin octobre).

---

## 3. Choix du moteur de rendu

Deux moteurs existent. Le choix découle du contenu, pas d'une préférence.

| Le contenu comporte | Moteur | Format | Slides | Fonds photo |
|---|---|---|---|---|
| du texte court, un mot, une phrase | *(rien à déclarer)* Pillow | 1080 × 1080 | 2 | **oui, requis** |
| des mathématiques, des formules | `"moteur": "html-katex"` | 1080 × 1350 | jusqu'à 7 | non, design plat |

Pillow ne sait pas composer de fractions, d'intégrales ni de racines. Une niche
scientifique prend obligatoirement le second moteur. Détail dans
`GUIDE.md` §4 et §4 bis.

**Question 3.1** : la niche affiche-t-elle des formules ? Si oui, prévoir aussi
un fichier CSS dans `gabarits/` si la palette diffère de maths-prépa.

---

## 4. Contenu

| # | Question | Précisions |
|---|---|---|
| 4.1 | Quels types de posts, et dans quelles proportions ? | Niches langues : mot, étymologie, prénom, grammaire, conjugaison. Niches scientifiques : un seul type, exercice. Les poids sont relatifs, pas des pourcentages. |
| 4.2 | Le contenu existe-t-il déjà ? | L'inventaire de la phase 1 l'a dit. Sinon, c'est le gros du travail restant. |
| 4.3 | Quelles sources feront foi ? | Dictionnaires, manuels, polycopiés. Nécessaire pour la règle de vérification ci-dessous. |

**Volume minimum.** Deux posts par jour, anti-répétition sur 7 jours : il faut
au moins **14 entrées publiables** pour ne rien recycler dans la semaine.
Confortable à partir de 40-60. En dessous de 14, le script recycle et le prévient
dans les logs, ce n'est pas une erreur mais ça se voit dans le fil.

**Règle de vérification, non négociable.** Toute donnée factuelle (étymologie,
règle de grammaire, conjugaison, romanisation, démonstration) se vérifie par
recherche web avec une source citée, ou se rédige à la main et se relit ligne à
ligne. Jamais depuis la seule mémoire d'un modèle. Une première tentative sans
cette discipline a produit 8 erreurs sur 30 étymologies.

**Format.** Copier la structure d'une niche existante :
`niches/arabe/vocabulaire.json` pour une langue,
`niches/maths-prepa/exercices.json` pour une matière scientifique. Ce dernier
porte son schéma en tête de fichier.

**Contrôle avant de continuer.** Pour une niche scientifique :
`python3 generer_maths.py --valider`. Pour toutes : rendre réellement chaque
type de slide et **les regarder**. Un champ trop long ou une fonction de dessin
réutilisée sans adaptation casse le rendu sans lever la moindre erreur.

---

## 5. Ce qu'il faut fournir, et qui manque souvent

### 5.1 Photos de fond — niches Pillow uniquement

**C'est le manque le plus fréquent.** Sans elles, `publier.py` s'arrête sur
`Aucune image dans niches/<id>/fonds`.

| | |
|---|---|
| Combien | 15 à 20 minimum, 50+ idéal. Arabe en a 57 |
| Formats | `.jpg`, `.jpeg`, `.png`, `.webp` |
| Où les déposer | `niches/<id>/fonds/` |
| Quoi | Des images d'ambiance liées au thème, sans texte incrusté, assez sombres ou uniformes pour qu'un voile et du texte passent dessus |
| Droits | Vérifier la licence. Une image sous copyright sur un compte commercial est un risque réel |

Demander explicitement : *as-tu un jeu de photos pour cette niche, et où ?* Si
non, c'est un point bloquant à inscrire au rapport final. L'agent ne peut pas
les inventer.

Les niches `html-katex` n'en ont pas besoin : leur `fonds/` reste vide.

### 5.2 Police de caractères

Si la langue sort de l'alphabet latin, il faut sa police dans `polices/`
(déjà présentes : Noto Naskh Arabic, Noto Sans JP, Noto Sans KR, Playfair
Display).

Deux pièges déjà rencontrés, à vérifier au premier rendu :

- Une police **variable** sans poids explicite s'affiche en Thin (100),
  illisible en grand titre.
- Du texte natif dans un champ rendu par une police latine produit des carrés
  vides. Savoir quelle police rend quel champ.

### 5.3 Identité visuelle

| Élément | Question | Défaut |
|---|---|---|
| Palette | Trois couleurs RVB : accent, accent foncé, crème. Plus le voile de fond et son opacité | Copier une niche voisine et changer les teintes |
| Décor du cadre | `arabe`, `japonais` ou `coreen`. Un nouveau décor demande une fonction dans `generer.py` | `arabe` |
| CTA | Deux lignes d'accroche, un sous-titre, un libellé de bouton | Reprendre la mécanique d'arabe en adaptant le texte au sujet |

### 5.4 Hashtags

**Quatre au maximum dans `hashtags_base`**, plus au plus un spécifique par type
de post, jamais plus de cinq au total. Instagram plafonne techniquement à 5
depuis fin 2025 et les hashtags ne boostent plus la portée. Éviter les
quasi-doublons du type `#arabe` + `#languearabe` + `#coursdarabe`, qui se
chevauchent. Justification et sources dans `../Guide.md` §4.

---

## 6. Comptes externes et secrets

C'est la partie qui demande l'utilisatrice devant son écran. Aucun agent ne
peut valider un écran de consentement Meta.

### 6.1 Instagram et Facebook

| # | Question | Où |
|---|---|---|
| 6.1 | Le compte Instagram existe-t-il, et est-il en mode Professionnel ? | Instagram → Paramètres → Type de compte. Créateur ou Entreprise, pas Personnel |
| 6.2 | Est-il relié à une Page Facebook ? | Obligatoire pour l'API. Une même Page peut être administrée par le compte Facebook qui gère déjà les autres niches |
| 6.3 | La Page Publishing Authorization est-elle validée ? | Page Facebook → Paramètres → Général → Page Publishing Authorization. **Son absence provoque un échec silencieux**, sans message d'erreur exploitable. C'est la panne la plus pénible à diagnostiquer |

Un seul compte Facebook peut administrer toutes les Pages : inutile de
multiplier les comptes Meta pour six niches.

### 6.2 Valeurs à récupérer côté Meta

Les libellés de l'interface Meta changent régulièrement. Les chemins ci-dessous
sont indicatifs ; la méthode par Graph API Explorer, elle, est stable.

| Valeur | Où la trouver |
|---|---|
| **App ID** et **App Secret** | [developers.facebook.com](https://developers.facebook.com) → ton app → Paramètres de l'app → Général. **Une seule fois pour tout le dépôt**, elles sont partagées entre les niches |
| **IG User ID** | Graph API Explorer, avec l'app sélectionnée : appeler `me/accounts` pour lister les Pages, puis `<PAGE_ID>?fields=instagram_business_account`. Le champ `id` renvoyé est l'IG User ID de cette niche |
| **Jeton longue durée** | Générer un jeton utilisateur dans l'Explorer avec les permissions `instagram_basic`, `instagram_content_publish`, `pages_show_list`, `pages_read_engagement`, puis l'échanger contre un jeton 60 jours via `oauth/access_token?grant_type=fb_exchange_token` |

**Le jeton expire tous les 60 jours.** C'est la cause numéro un de panne
silencieuse. Le renouvellement est **automatisé** depuis le 12/09/2026 par
`.github/workflows/renouveler_token.yml`, exécuté deux fois par mois, à
condition d'ajouter la ligne de la niche dans son bloc `env` (voir 6.5).

### 6.3 Cloudinary

Sert d'hébergeur intermédiaire : l'API Meta télécharge les images depuis une
URL publique, on ne peut pas lui envoyer les octets directement.

**Déjà configuré pour tout le dépôt.** Les trois secrets `CLOUDINARY_*` sont
partagés entre les niches, il n'y a rien à refaire. Si le compte n'existait pas :
[cloudinary.com](https://cloudinary.com), gratuit, cinq minutes, les valeurs sont
sur le dashboard d'accueil.

### 6.4 Secrets GitHub à créer

Dépôt → **Settings → Secrets and variables → Actions → New repository secret**.

| Secret | Portée | Valeur |
|---|---|---|
| `IG_USER_ID_<NICHE>` | par niche | l'IG User ID de 6.2 |
| `IG_TOKEN_<NICHE>` | par niche | le jeton longue durée de 6.2 |
| `CLOUDINARY_CLOUD_NAME` | partagé | déjà en place |
| `CLOUDINARY_API_KEY` | partagé | déjà en place |
| `CLOUDINARY_API_SECRET` | partagé | déjà en place |
| `META_APP_ID` | partagé | déjà en place |
| `META_APP_SECRET` | partagé | déjà en place |
| `GH_PAT_SECRETS` | partagé | déjà en place. Jeton GitHub *fine-grained*, limité à ce dépôt, permission Secrets en lecture/écriture. Seul moyen d'écrire un secret par API : le `GITHUB_TOKEN` automatique n'en a pas le droit |

`<NICHE>` est l'identifiant en majuscules, tirets remplacés par des underscores :
`maths-prepa` donne `IG_USER_ID_MATHS_PREPA`.

**Rappel à faire à l'utilisatrice** : ces valeurs se saisissent directement dans
l'interface web GitHub. Un jeton collé dans un terminal reste dans l'historique
du shell ; collé dans un chat, il reste dans l'historique de conversation ; écrit
dans le code d'un dépôt public, n'importe qui peut le prendre.

### 6.5 Câbler le renouvellement automatique

Ajouter une ligne dans le bloc `env` de
`.github/workflows/renouveler_token.yml` :

```yaml
IG_TOKEN_<NICHE>: ${{ secrets.IG_TOKEN_<NICHE> }}
```

Le script lui-même n'a rien d'autre à changer : il lit `niches/config.json` et
ne traite que les niches `"actif": true`.

---

## 7. Mise en service

Dans cet ordre, sans en sauter une.

**7.1 Écrire le bloc de configuration**, `"actif": false` pour l'instant.
Copier un bloc voisin dans `niches/config.json` et remplacer les valeurs
collectées aux phases 2 à 5.

**7.2 Créer les dossiers** : `niches/<id>/fonds/` et `niches/<id>/sortie/`.

**7.3 Dry-run local ou par GitHub Actions.**

```bash
python3 publier.py --niche <id> --dry-run
```

Ou depuis GitHub : onglet **Actions → Publier Instagram → Run workflow**, case
« Tester sans publier » cochée.

**Regarder les images produites**, pas seulement la sortie texte. C'est la seule
manière de voir un débordement, un carré vide ou un ordre de mots inversé.

**7.4 Pousser sur GitHub.** Le contenu, les fonds et la config doivent être dans
le dépôt : GitHub Actions ne voit que lui, jamais l'ordinateur de
l'utilisatrice.

**7.5 Première publication réelle.**

```bash
python3 publier.py --niche <id>
```

Vérifier que le post apparaît bien sur le compte.

**7.6 Passer `"actif": true`** dans `niches/config.json`, et committer.

**7.7 Confirmer le cron.** L'onglet Actions doit montrer les deux exécutions
programmées. Rien d'autre ensuite.

---

## 8. Rapport final

Rendre ce tableau, rempli, à la fin de l'entretien.

| Point | État | Qui |
|---|---|---|
| Identifiant et handle arrêtés | ☐ | utilisatrice |
| Moteur choisi et configuré | ☐ | agent |
| Contenu ≥ 14 entrées vérifiées | ☐ | agent + vérification |
| Photos de fond ≥ 15 *(niches Pillow)* | ☐ | **utilisatrice** |
| Police disponible dans `polices/` | ☐ | agent |
| Palette, décor, CTA, hashtags ≤ 5 | ☐ | agent |
| Compte Instagram Pro + Page Facebook | ☐ | **utilisatrice** |
| Page Publishing Authorization validée | ☐ | **utilisatrice** |
| IG User ID et jeton récupérés | ☐ | **utilisatrice** |
| Secrets GitHub saisis | ☐ | **utilisatrice** |
| Ligne ajoutée dans `renouveler_token.yml` | ☐ | agent |
| Cron ajusté en UTC | ☐ | agent |
| Dry-run passé et **images regardées** | ☐ | agent |
| Première publication réussie | ☐ | agent |
| `actif: true` | ☐ | agent |

Puis, en clair :

- **Ce qui bloque** : la liste des cases non cochées qui empêchent la
  publication, avec pour chacune ce qu'il faut et auprès de qui.
- **Ce qui peut attendre** : ce qui n'empêche pas de démarrer.
- **Prochaine action concrète**, une seule, celle qui débloque le plus.
