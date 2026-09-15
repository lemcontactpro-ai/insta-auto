# Mise en place d'une niche

**Ce document est un script d'entretien.** Un agent IA le lit, puis pose à
l'utilisatrice les questions nécessaires au lancement d'un nouveau compte,
**une par une**, en indiquant à chaque fois où trouver la réponse. À la fin,
il produit un rapport de ce qui est prêt et de ce qui bloque.

Le code, les workflows et les deux moteurs de rendu existent déjà. Rien n'est
à développer côté rendu. Ce qui reste est de la configuration, du contenu, des
comptes externes, et, souvent oublié, les outils qui vendent réellement le
produit derrière le lien en bio.

---

## 0. Instructions à l'agent

Lis ce document en entier avant de poser la première question.

**Deux types de questions, ne pas les mélanger.**

- **Bloc A, séquence obligatoire.** Ces questions ont une dépendance stricte :
  la suivante est littéralement impossible à répondre avant la précédente.
  Impossible d'avoir un IG User ID avant que le compte ait le rôle de
  testeur Instagram, impossible d'avoir un jeton avant que l'app Meta existe. **Respecter
  l'ordre du bloc A à la lettre, ne jamais sauter en avant même si
  l'utilisatrice propose une info plus tard dans la liste.** Si elle donne une
  info hors tour (ex. colle un App ID alors qu'on est encore à la question du
  handle), la noter, la confirmer, mais continuer à poser les questions dans
  l'ordre là où l'entretien en était.
- **Bloc B, suivi libre.** Ces éléments n'ont pas d'ordre entre eux ni avec
  le bloc A : les fonds, la police, la palette, les hashtags peuvent être
  fournis au tout début, entre deux questions du bloc A, ou tout à la fin.
  Le rôle de l'agent est de **savoir en permanence ce qui manque encore dans
  ce bloc**, de le rappeler à chaque question du bloc A qui s'en approche
  (ex. juste avant le dry-run, rappeler tout ce qui n'est pas encore réglé
  dans le bloc B), et de ne jamais bloquer une question du bloc A en
  attendant une réponse du bloc B.
- **Bloc C, outils de vente.** Ce que la niche vend réellement (fiche
  produit, lien en bio). Sans rapport avec l'API Meta, donc pas de dépendance
  technique avec les blocs A/B, mais indispensable pour que la publication
  serve à quelque chose. Traité en fin d'entretien, jamais oublié dans le
  rapport final même si toute la mécanique technique est prête.

**Conduite de l'entretien.** Une question à la fois, jamais dix d'un coup.
Utilise l'outil de question à choix multiples quand les options sont connues,
du texte libre sinon. Après chaque réponse, écris immédiatement la valeur
dans `niches/config.json` (ou note le statut bloc B/C) plutôt que d'accumuler
pour la fin.

**Pour les questions A8 à A13** (compte pro, rôle de testeur, app Meta, IG
User ID, jeton), ne te contente jamais de dire seulement où chercher : demande si
l'utilisatrice l'a déjà fait, ou si elle veut le pas-à-pas, et donne-le
directement, il est écrit dans la sous-section « Tutos pas-à-pas » juste
après le tableau du bloc A, pas besoin de l'improviser à chaque niche.

**Ne demande jamais un secret dans la conversation.** Aucun jeton, aucune clé
API, aucun mot de passe ne doit être collé dans un chat ni écrit dans un
fichier du dépôt. Ton rôle sur les secrets se limite à dire : *voici le nom du
secret à créer, voici où le trouver, voici où le coller*. Si l'utilisatrice te
donne une valeur de secret quand même, ne l'écris nulle part et redis-lui de la
saisir directement dans l'interface GitHub.

**Ne saute pas une phase parce qu'elle a l'air faite.** Lance d'abord
l'inventaire de la phase 1, il te dira ce qui existe réellement, pour
chaque niche, y compris celles déjà entamées.

**Ce que tu ne peux pas faire à sa place**, et qu'il faut annoncer tôt pour
qu'elle s'organise :

- créer le compte Instagram ;
- accepter l'invitation de testeur Instagram et valider les écrans de
  consentement Meta ;
- saisir les secrets dans GitHub ;
- fournir les photos de fond ;
- décider du nom définitif du compte ;
- créer la fiche produit (Payhip ou équivalent) et le lien en bio.

**À la fin**, produis le rapport de la section 8. Ne déclare jamais une niche
prête si un point bloquant du bloc A reste ouvert, et signale toujours l'état
du bloc C séparément même si le bloc A est complet, une niche qui publie
mais ne vend rien n'est pas terminée.

---

## 1. Inventaire, avant toute question

Lance ces commandes depuis `insta-auto/` et lis le résultat. Il détermine
quelles questions sont déjà répondues.

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
grep 'IG_TOKEN_' .github/workflows/renouveler_token.yml

# la niche a-t-elle une étape de publication dans le workflow principal ?
grep -A1 "Publier (" .github/workflows/publier.yml
```

Résume à l'utilisatrice, en trois lignes, l'état trouvé, y compris la
dernière commande, souvent oubliée : une niche peut être `actif: true` dans
`config.json` sans jamais se déclencher si elle n'a pas d'étape dans
`publier.yml` (voir A16).

---

## Bloc A, Séquence obligatoire

Ne pas réordonner. Chaque numéro suppose les précédents résolus. Les
étapes déjà répondues (vues à l'inventaire) sont annoncées comme telles et
non reposées, mais on ne saute pas les suivantes pour autant.

| # | Question | Où trouver la réponse | Écrit dans |
|---|---|---|---|
| A1 | Quel est l'identifiant technique de la niche ? | Minuscules, sans accent ni espace : `coreen`, `maths-prepa`. Sert de nom de dossier et de suffixe de secret (`IG_USER_ID_<ID>`, `IG_TOKEN_<ID>`). | `config.json → id`, dossier `niches/<id>/` |
| A2 | Quel est le nom de compte Instagram **visé** ? | Le handle qu'on va effectivement créer ou déjà créé. Il s'affiche sur chaque slide, donc doit être arrêté avant tout rendu définitif. | `config.json → compte` |
| A3 | Que vend ce compte ? | Le produit vers lequel pointe la bio. Détermine le texte du CTA et prépare le bloc C. Terminologie : « ebook interactif » pour une niche de langue, **« cahier d'exercices »** pour une niche scientifique (maths-prepa, physique-prepa), jamais « PDF » dans les deux cas. | `config.json → textes` |
| A4 | La niche affiche-t-elle des formules mathématiques ? | Détermine le moteur : Pillow (texte court, 1080×1080, 2 slides, fonds photo requis) ou `html-katex` (formules, 1080×1350, jusqu'à 8 slides, pas de fonds). Détail `GUIDE.md` §4 et §4 bis. | `config.json → moteur` |
| A5 | Quels types de posts, et dans quelles proportions ? | Niches langues : mot, étymologie, prénom, grammaire, conjugaison. Niches scientifiques : exercice. Poids relatifs, pas des pourcentages. | `config.json → poids_types` |
| A6 | Le contenu existe-t-il déjà, sinon quelles sources feront foi ? | L'inventaire de la phase 1 l'a dit. Sinon c'est le gros du travail restant : dictionnaires, manuels, polycopiés cités, jamais depuis la seule mémoire d'un modèle (règle non négociable, une première tentative sans cette discipline a produit 8 erreurs sur 30 étymologies). **Deux posts par jour, anti-répétition sur 7 jours : minimum 14 entrées publiables**, confortable à 40-60. | `niches/<id>/vocabulaire.json` ou `exercices.json`, structure copiée d'une niche existante |
| A7 | Bloc de config écrit, `actif: false` | Agent : copier un bloc voisin dans `niches/config.json`, remplacer les valeurs A1-A6. `horaires` reste `12:30`/`19:00` Paris, commun à toutes les niches, ne pas s'en écarter sans raison (le cron est partagé). Créer `niches/<id>/fonds/` et `niches/<id>/sortie/`. | `config.json` |
| A8 | Le compte Instagram existe-t-il, en mode Professionnel (Créateur ou Entreprise, pas Personnel) ? | Instagram → Paramètres → Type de compte. **Utilisatrice.** Rien de plus loin n'est possible sans ça. **Ne jamais le lier à une Page Facebook, ni l'ajouter comme élément du portefeuille business**, voir les « Trois interdits » ci-dessous. |, |
| A9 | Le compte a-t-il le rôle de testeur Instagram sur l'app Meta partagée, et l'invitation est-elle acceptée ? | App Meta « Niches Auto » → cas d'utilisation « Gérer les messages et les contenus sur Instagram » → lien **Rôles** → ajouter le compte comme testeur Instagram ; puis, depuis l'app Instagram connectée sur ce compte, Paramètres → Applications et sites web → Invitations de testeur → accepter. **Utilisatrice.** |, |
| A10 | Les autorisations `instagram_business_basic` et `instagram_business_content_publish` sont-elles actives sur l'app ? | Même écran, section « Autorisations et fonctionnalités » (bouton en haut de l'étape 1). Normalement déjà actives si une autre niche tourne déjà, vérifier plutôt que reconfigurer. **Utilisatrice.** |, |
| A11 | App ID et App Secret Meta | [developers.facebook.com](https://developers.facebook.com) → l'app « Niches Auto » → Paramètres de l'app → Général. **Une seule fois pour tout le dépôt**, si une autre niche a déjà ces valeurs, les réutiliser, ne pas créer une nouvelle app. Sert uniquement de repli dans `renouveler_token.py` (cas rare d'un jeton jamais échangé), pas au fonctionnement courant. **Utilisatrice** (l'agent ne fait que vérifier si elle existe déjà côté secrets GitHub). | secret partagé `META_APP_SECRET`, déjà en place si une niche tourne déjà |
| A12 | IG User ID | Affiché directement sous le nom du compte, sur l'écran « Générez des tokens d'accès » de l'étape A9, pas besoin du Graph API Explorer. **Utilisatrice.** | secret GitHub `IG_USER_ID_<ID>` |
| A13 | Jeton longue durée | Sur ce même écran, cliquer **Générer un token** en face du compte. Le jeton obtenu est déjà longue durée (60 jours), aucun échange manuel nécessaire. **Utilisatrice.** Renouvelé automatiquement ensuite une fois A15 fait. | secret GitHub `IG_TOKEN_<ID>` |
| A14 | Secrets saisis dans GitHub | Dépôt → Settings → Secrets and variables → Actions → New repository secret. **Utilisatrice**, jamais collé dans ce chat. | `IG_USER_ID_<ID>`, `IG_TOKEN_<ID>` |
| A15 | Câbler le renouvellement automatique | Ajouter `IG_TOKEN_<ID>: ${{ secrets.IG_TOKEN_<ID> }}` dans le bloc `env` de `.github/workflows/renouveler_token.yml`. Le script lit `config.json` et ne traite que les niches `actif: true`, rien d'autre à changer. **Agent.** | `.github/workflows/renouveler_token.yml` |
| A16 | Câbler l'étape de publication | `publier.yml` n'exécute que les niches qui ont explicitement une étape `Publier (<id>)`, `actif: true` seul ne suffit pas. Copier le modèle de l'étape `Publier (maths-prepa)` (gate `actif`, secrets `IG_USER_ID_<ID>`/`IG_TOKEN_<ID>` + les trois `CLOUDINARY_*` partagés). Les deux déclenchements `schedule:` du workflow (12:30 et 19:00 Paris, convertis en UTC) sont communs à toutes les niches, rien à ajouter ici sauf si cette niche a une vraie raison de s'en écarter. **Agent.** | `.github/workflows/publier.yml` |
| A17 | Dry-run passé et **images regardées** | `python3 publier.py --niche <id> --dry-run`, ou Actions → Publier Instagram → Run workflow → case dry-run. Regarder les images produites, pas seulement la sortie texte : c'est la seule façon de voir un débordement, un carré vide ou un ordre de mots inversé. Nécessite le bloc B réglé (fonds, police) pour un rendu représentatif. **Agent, avec validation visuelle de l'utilisatrice recommandée.** | `niches/<id>/sortie/` |
| A18 | Poussé sur GitHub | Contenu, fonds et config doivent être dans le dépôt : GitHub Actions ne voit jamais l'ordinateur de l'utilisatrice. **Agent.** |, |
| A19 | Première publication réelle | `python3 publier.py --niche <id>`. Vérifier que le post apparaît sur le compte. **Agent puis vérification utilisatrice.** | `niches/<id>/historique.json` |
| A20 | `actif: true` | Une fois A19 confirmé. **Agent.** | `config.json` |
| A21 | Cron confirmé | Onglet Actions doit montrer les deux exécutions programmées suivantes (12:30 et 19:00 Paris). Rien d'autre ensuite. |, |

### Tutos pas-à-pas, A8 à A13

Pour ces six questions, ne te contente pas de pointer vers une interface : **à
chaque question, demande explicitement si l'utilisatrice a déjà fait l'étape
ou si elle veut le pas-à-pas**, et donne-le directement si elle le demande,
ne l'oblige pas à aller chercher un tuto ailleurs. Les libellés Meta bougent
souvent ; si une étape ne correspond plus à l'interface réelle, chercher le
mot-clé indiqué entre parenthèses plutôt que d'abandonner, et le signaler
pour mettre ce tuto à jour.

**Trois interdits, valables pour toute niche (incident du 13-14/09/2026) :**

1. Ne jamais ajouter un compte Instagram comme élément du portefeuille business.
2. Ne jamais lier un compte Instagram à une Page Facebook.
3. Ne jamais lier un compte Instagram de niche à un profil Facebook personnel dans l'Espace Comptes.

Aucun des trois n'est nécessaire au fonctionnement (le moteur publie via
« Instagram API with Instagram Login », pas Facebook Login) et chacun
recrée le même problème : le compte réapparaît comme « personne » avec
accès total dans le portefeuille partagé, donnant à chaque niche un accès
croisé aux éléments des autres.

**A8, Compte professionnel**

1. App Instagram → profil → ☰ (menu, en haut à droite) → **Paramètres et
   confidentialité**.
2. Descendre à **Type de compte et outils** (ou « Pour les professionnels »)
   → **Passer à un compte professionnel**.
3. Choisir une catégorie, puis **Entreprise** plutôt que Créateur.
4. À aucun moment accepter de lier une Page Facebook si l'interface le
   propose, passer outre cette étape si elle apparaît.

**A9, Rôle de testeur Instagram**

1. [developers.facebook.com/apps/2589702121477142/dashboard/](https://developers.facebook.com/apps/2589702121477142/dashboard/)
   (app « Niches Auto »).
2. Menu de gauche → **Cas d'utilisation** → cliquer sur la ligne « Gérer les
   messages et les contenus sur Instagram ».
3. Étape « 2. Générez des tokens d'accès » → lien **Rôles** dans le texte →
   onglet Rôles → ajouter le compte comme testeur Instagram (recherche par
   `@handle`).
4. Depuis l'app Instagram, connectée sur ce compte : Paramètres →
   Applications et sites web → onglet **Invitations de testeur** → accepter
   l'invitation « Niches Auto ».

**A10, Autorisations**

Sur l'étape « 1. Ajoutez les autorisations de messages requises » du même
écran : vérifier que `instagram_business_basic` et
`instagram_business_content_publish` sont cochées (`instagram_business_manage_comments`
et `instagram_business_manage_messages` sont gardées pour un usage futur,
pas strictement nécessaires à la publication). Généralement déjà en place
si une autre niche tourne déjà, ne reconfigurer que si l'étape 1 affiche un
état incomplet.

**A11, App Meta (App ID / App Secret)**

1. [developers.facebook.com](https://developers.facebook.com) → **Mes
   apps**. Une seule app pour tout le dépôt (« Niches Auto », App ID
   `2589702121477142`), vérifier si les secrets `META_APP_SECRET` existent
   déjà côté GitHub avant de rouvrir cet écran.
2. Si besoin malgré tout : **Paramètres de l'app → Général**, App ID et App
   Secret y sont affichés.

**A12 + A13, IG User ID et jeton longue durée**

1. Revenir sur l'écran de l'étape A9 (« Générez des tokens d'accès »).
2. Repérer la ligne du compte : le nombre affiché sous son nom est l'IG
   User ID.
3. Cliquer **Générer un token** en face de ce compte. Le jeton retourné est
   directement un jeton longue durée (60 jours), aucun échange manuel,
   aucun passage par le Graph API Explorer.
4. **Ne pas coller ce jeton dans ce chat**, il va directement dans le
   secret GitHub `IG_TOKEN_<NICHE>` (A14).

---

## Bloc B, Suivi libre

Pas d'ordre entre ces items ni avec le bloc A, demandables dès le début de
l'entretien si l'utilisatrice les a sous la main, ou juste avant A17 sinon.
**L'agent doit connaître à tout instant leur statut** et les rappeler avant
A17 et A5/A6.

| Élément | Question | Où / défaut |
|---|---|---|
| Photos de fond *(niches Pillow uniquement)* | As-tu un jeu de photos pour cette niche, et où ? | 15-20 minimum, 50+ idéal (arabe en a 57), `.jpg/.jpeg/.png/.webp`, dans `niches/<id>/fonds/`. Ambiance liée au thème, sans texte incrusté, assez sombres/uniformes pour qu'un voile et du texte passent dessus. Vérifier la licence, image sous copyright sur un compte commercial est un risque réel. **Sans elles, `publier.py` s'arrête sur `Aucune image dans niches/<id>/fonds`.** C'est le manque le plus fréquent : si absent, l'inscrire au rapport comme bloquant pour A17. |
| Police | La langue sort-elle de l'alphabet latin ? | Déjà présentes dans `polices/` : Noto Naskh Arabic, Noto Sans JP, Noto Sans KR, Playfair Display. Sinon la trouver et l'ajouter. Deux pièges à vérifier au premier rendu : une police variable sans poids explicite s'affiche en Thin (100, illisible) ; du texte natif rendu par une police latine produit des carrés vides, savoir quelle police rend quel champ. |
| Palette et décor | Trois couleurs RVB (accent, accent foncé, crème) + voile de fond et opacité ? Décor de cadre ? | Défaut : copier une niche voisine et changer les teintes. Décor : `arabe`, `japonais` ou `coreen` existants dans `generer.py` (`_DECOR_FUNCS`) ; un nouveau décor demande une fonction dédiée, le dire clairement si c'est le cas, ce n'est plus juste de la config. |
| CTA | Deux lignes d'accroche, sous-titre, libellé de bouton ? | Défaut : reprendre la mécanique d'arabe en adaptant au sujet. À faire correspondre au bloc C une fois la fiche produit connue. |
| Hashtags | Quels hashtags ? | Quatre au maximum dans `hashtags_base`, plus au plus un spécifique par type de post, jamais plus de cinq au total (Instagram plafonne à 5 depuis fin 2025, les hashtags ne boostent plus la portée). Éviter les quasi-doublons (`#arabe` + `#languearabe` + `#coursdarabe`). Détail `Guide.md` §4. |

**Contrôle avant A17.** Pour une niche scientifique : `python3
generer_maths.py --valider`. Pour toutes : rendre réellement chaque type de
slide et les regarder, un champ trop long ou une fonction de dessin
réutilisée sans adaptation casse le rendu sans lever la moindre erreur.

---

## Bloc C, Outils de vente et lien en bio

Sans dépendance technique avec A/B, mais **une niche qui publie sans que le
lien en bio vende quoi que ce soit n'est pas terminée**, à ne jamais omettre
du rapport final même si tout le reste est vert. À traiter en fin d'entretien,
une fois le produit connu (A3).

| # | Question | Où / précisions |
|---|---|---|
| C1 | La fiche produit existe-t-elle (Payhip ou équivalent) ? | C'est l'outil déjà utilisé par les niches existantes (voir `Guide.md` §1, terminologie fixée : « ebook interactif » pour une niche de langue, « cahier d'exercices » pour une niche scientifique, jamais « PDF » dans les deux cas, y compris sur la fiche). Si absente, c'est bloquant pour que la niche génère un revenu, mais pas pour que les posts se publient, le dire clairement à l'utilisatrice pour qu'elle priorise. **Utilisatrice.** |
| C2 | Le lien en bio du compte Instagram pointe-t-il vers cette fiche ? | Directement vers le lien Payhip, ou via un agrégateur (Linktree, Beacons...) si plusieurs liens doivent cohabiter sur ce compte. **Utilisatrice**, à vérifier après A19 (une fois le compte réellement actif). |
| C3 | Le texte CTA de `config.json` correspond-il à ce qui est réellement en vente ? | Comparer `textes.cta_ligne1/2`, `cta_sous_titre`, `cta_bouton` (bloc B) à la fiche produit réelle (C1). Un CTA générique laissé par défaut qui ne colle pas au produit final est un bug silencieux, invisible dans les logs. **Agent, à valider avec l'utilisatrice.** |

---

## 8. Rapport final

Rendre ce tableau, rempli, à la fin de l'entretien.

| Point | Bloc | État | Qui |
|---|---|---|---|
| Identifiant et handle arrêtés | A1-A2 | ☐ | utilisatrice |
| Moteur et types de contenu choisis | A4-A5 | ☐ | agent |
| Contenu ≥ 14 entrées vérifiées | A6 | ☐ | agent + vérification |
| Bloc de config écrit (`actif: false`) | A7 | ☐ | agent |
| Compte Instagram Pro + rôle de testeur accepté | A8-A9 | ☐ | **utilisatrice** |
| Autorisations app vérifiées | A10 | ☐ | **utilisatrice** |
| App Meta ID/Secret | A11 | ☐ | **utilisatrice** |
| IG User ID et jeton récupérés | A12-A13 | ☐ | **utilisatrice** |
| Secrets GitHub saisis | A14 | ☐ | **utilisatrice** |
| Renouvellement du jeton câblé | A15 | ☐ | agent |
| Étape de publication câblée dans `publier.yml` | A16 | ☐ | agent |
| Photos de fond ≥ 15 *(niches Pillow)* | B | ☐ | **utilisatrice** |
| Police, palette, décor, CTA, hashtags réglés | B | ☐ | agent |
| Dry-run passé et **images regardées** | A17 | ☐ | agent |
| Poussé sur GitHub | A18 | ☐ | agent |
| Première publication réussie | A19 | ☐ | agent |
| `actif: true` | A20 | ☐ | agent |
| Cron confirmé (12:30 et 19:00) | A21 | ☐ | agent |
| Fiche produit (Payhip) en place | C1 | ☐ | **utilisatrice** |
| Lien en bio pointe vers le bon produit | C2 | ☐ | **utilisatrice** |
| CTA cohérent avec le produit réel | C3 | ☐ | agent + utilisatrice |

Puis, en clair :

- **Ce qui bloque** : la liste des cases non cochées du bloc A qui empêchent
  la publication technique, avec pour chacune ce qu'il faut et auprès de qui.
- **Ce qui peut attendre** : le bloc B non résolu (n'empêche pas de démarrer
  l'entretien, mais bloque A17) et le bloc C (n'empêche pas de publier, mais
  la niche ne vend rien tant que c'est ouvert).
- **Prochaine action concrète**, une seule, celle qui débloque le plus,
  normalement la prochaine question non répondue du bloc A, dans l'ordre.
