# DS Sup Physique — Bibliothèque d'épreuves classées

Ce dossier rassemble l'ensemble des devoirs surveillés (DS), devoirs maison (DM) et concours blancs (CB) de physique en CPGE scientifique (Sup / MPSI / PTSI / PCSI).

Toutes les épreuves sont numérisées et appariées dans le sous-dossier [`epreuves/`](epreuves).

---

## Structure de chaque épreuve

Chaque sous-dossier contient systématiquement :
- `enonce.pdf` : Sujet original au format PDF.
- `enonce.md` : Transcription Markdown intégrale via OCR Apple Vision pour consommation sans consommation excessive de tokens.
- `corrige.pdf` : Corrigé détaillé officiel au format PDF.
- `corrige.md` : Transcription Markdown intégrale du corrigé.

> **Règle d'économie de tokens pour l'agent IA** : Ne jamais charger directement les PDF volumineux dans le contexte. Toujours consulter les fichiers `.md` correspondants pour le repérage et la sélection des exercices.

---

## Index des 30 Épreuves (par Thématique)

### 1. Optique Géométrique & Ondulatoire
| Dossier | Type | Thèmes abordés |
|---|---|---|
| `epreuves/dm1_optique_snell_descartes_gaine/` | DM 1 | Lois de Snell-Descartes, fibre optique à saut d'indice, gaine |
| `epreuves/dm3_elec_optique_lunette_astronomique/` | DM 3 | Lunette astronomique afocale, grossissement, électronique |
| `epreuves/ds0_analyse_dimentionnelle_optique/` | DS 0 | Analyse dimensionnelle, optique élémentaire |
| `epreuves/ds01_optique/` | DS 01 | Optique géométrique, miroirs, lentilles minces |
| `epreuves/ds02_chimie_optique_lentille/` | DS 02 | Chimie des solutions & systèmes optiques centrés |
| `epreuves/ds1_optique/` | DS 1 | Optique géométrique approfondie |
| `epreuves/ds1_ptsi_optique/` | DS 1 (PTSI) | Réfraction, dispersion, instruments d'optique |

### 2. Électrocinétique, Filtres & Signaux
| Dossier | Type | Thèmes abordés |
|---|---|---|
| `epreuves/dm4_filtre_elec/` | DM 4 | Filtres passifs, fonction de transfert, diagramme de Bode |
| `epreuves/dm5_effet_doppler_circuits_1er_ordre/` | DM 5 | Circuits RC / RL du premier ordre, onde sonore & effet Doppler |
| `epreuves/ds2_circuits_rlc_elec/` | DS 2 | Circuits RLC série/parallèle, régimes transitoires |
| `epreuves/ds2_circuits_rlc_mecanique_optique_ptsi/` | DS 2 (PTSI) | Synthèse RLC, analogie électro-mécanique, optique |
| `epreuves/ds3_chimie_circuits_rlc/` | DS 3 | Résonance en courant/tension RLC, cinétique chimique |
| `epreuves/ds3_filtres_mecanique_ptsi/` | DS 3 (PTSI) | Filtrage linéaire, étude temporelle et fréquentielle |
| `epreuves/ds3_rsf_filtres_electromag/` | DS 3 | Régime Sinusoïdal Forcé (RSF), filtres actifs |
| `epreuves/ds4_circuits_2nd_ordre_mecanique/` | DS 4 | Oscillateurs du second ordre électriques et mécaniques |
| `epreuves/ds4_onde_signal_electromag/` | DS 4 | Propagation d'ondes, paquets d'ondes, signaux |

### 3. Mécanique du Point & Oscillateurs
| Dossier | Type | Thèmes abordés |
|---|---|---|
| `epreuves/dm6_mecanique_chute_libre/` | DM 6 | Chute avec frottement quadratique/linéaire |
| `epreuves/dm7_mecanique_pendule/` | DM 7 | Pendule simple, portrait de phase, approximations |
| `epreuves/dm9_mecanique_dynamique_chute_d_arbre/` | DM 9 | Théorème du moment cinétique, chute avec point fixe |
| `epreuves/ds3_h4_mecanique_optique/` | DS 3 (H4) | Problème type Henri IV mécanique & optique |
| `epreuves/exos_oscillateurs_harmoniques_oscillate/` | Exercices | Recueil d'oscillateurs harmoniques et amortis |
| `epreuves/oscillateurs_couples/` | Problème | Modes propres, battements, oscillateurs couplés |
| `epreuves/physique_devoir_surveille_2_mecanique/` | DS 2 | Dynamique newtonienne complète, énergie mécanique |

### 4. Électromagnétisme & Chimie
| Dossier | Type | Thèmes abordés |
|---|---|---|
| `epreuves/dm2_electrolyse/` | DM 2 | Électrolyse, oxydoréduction, aspects quantitatifs |
| `epreuves/dm8_electromag/` | DM 8 | Force de Lorentz, champ magnétique, spectromètre |
| `epreuves/ds6_mecanique_electromag/` | DS 6 | Induction, couplage magnéto-mécanique |

### 5. Thermodynamique
| Dossier | Type | Thèmes abordés |
|---|---|---|
| `epreuves/dm10_thermo_calorimetrie/` | DM 10 | Premier principe, calorimétrie, modélisation Python (scripts inclus) |
| `epreuves/ds7_forces_moments_thermo/` | DS 7 | Statique des fluides, premier et second principes, bilans d'énergie |

### 6. Concours Blancs & Épreuves de Synthèse
| Dossier | Type | Thèmes abordés |
|---|---|---|
| `epreuves/cb1_signal_elec_meca/` | CB 1 | Épreuve complète de synthèse signaux, élec et mécanique |
| `epreuves/cb_concours_blanc/` | CB Blanc | Épreuve de concours blanc type Mines-Ponts / CCINP |
