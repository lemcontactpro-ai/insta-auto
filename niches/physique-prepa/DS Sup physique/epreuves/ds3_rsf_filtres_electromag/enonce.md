# DS3 RSF filtres electromag


--- Page 1 ---

DS3 PCSI2 2022-2023 
physique 
1/4 
Problème 1 : Mesures d’impédances. 
A. Mesure de l’impédance de sortie d’un générateur basse fréquence (GBF). 
On modélise un GBF par un générateur idéal de tension de force électromotrice 
 ( ) cos mE t E t   en série avec un 
résistor de résistance Rg. 
On réalise le protocole expérimental suivant : 
 A l’aide d’un oscilloscope, qu’on supposera ici idéal, on observe la tension à vide aux bornes du GBF. On mesure 
alors une tension sinusoïdale d’amplitude EO=8V. 
 On réalise ensuite un circuit en alimentant un conducteur ohmique de résistance variable R à l’aide du GBF. On 
observe alo rs la tension aux bornes du conducteur ohmique  à l’aide de l’oscilloscope, toujours supposé idéal . 
Lorsque la résistance prend la valeur R=RC=50Ω, on observe une tension sinusoïdale d’amplitude E O/2=4V. 
1. Traduire l’hypothèse d’un oscilloscope idéal (dont on rappelle qu ’il mesure une te nsion) introduite dans le 
protocole expérimental. 
2. Réaliser un schéma des  circuits mis en œuvre dans les deux expériences et en déduire dans chaque cas 
l’expression de la tension visualisée sur l’oscilloscope. 
3. Déterminer alors les expressions et les valeurs numériques de E m et Rg. 
B. Mesure de l’impédance d’entrée d’un oscilloscope. 
On modélise l’impédance d’entrée d’un oscilloscope par l’association en parallèle d’ un conducteur ohmique de 
résistance RO et d’un condensateur de capacité CO. 
On réalise alors le protocole suivant : 
Le GBF précédent alimente l’association en série d’un conducteur ohmique de résistance variable R et de 
l’oscilloscope.  
 Lorsque le GBF émet  une tension sinusoïdale de fréquence f=1kHz, et que la résistance variable présente une 
valeur nulle, la tension observée aux bornes de l’oscilloscope présente une amplitude EO. 
 Lorsque le GBF émet une tension sinusoïdale de fréquence f=1kHz, et que la ré sistance variable présente une 
valeur R=RC’=1MΩ l’oscilloscope observe une tension d’amplitude E O/2. 
 Lorsque le GBF émet une tens ion sinusoïdale de fréquence f=3 00kHz, et que la résistance variable présente une 
valeur R=R1=63kΩ, la tension observée aux bornes de l’oscilloscope présente une amplitude EO/2. 
4. Quel sera le temps caractéristique associé à l’impédance d’entrée du circuit, en dédui re la fréquence propre 
associée en fonction de RO et CO. 
5. Faire un schéma du circuit étudié. 
6. Simplifier le circuit dans le domaine basse fréquence et exprimer alors la  tension aux bornes de l’oscilloscope 
en fonction de R O, R et R g.  Montrer que R g est négligeable devant R O et déterminer l’expression et la valeur 
de RO. 
On suppose que pour la dernière expérience, l’impédance d’entrée de l’oscilloscope peut être simplifi ée au seul 
condensateur de capacité CO. 
7. Exprimer la tension complexe U(t) aux bornes de l’oscilloscope. En déduire son amplitude complexe UO puis 
l’amplitude UO de la tension réelle. Déterminer alors la capacité CO et faire l’application numérique. 
8. Vérifier que la fréquence f=1kHz est bien située dans le domaine basse fréquence. Vérifier que la résistance de 
l’oscilloscope est négligeable à la fréquence f=300kHz. 
C. Mesure d’impédances par la méthode des ponts. 
On souhaite déterm iner les caractéristiques de différents dipô les en 
régime sinusoïdal forcé. Le pont est a limenté par un générateur idéal de 
tension sinusoïdale de  pulsation ω  et d’amplitude E O. Le pont est à 
l’équilibre si le courant circulant dans la branche BD est nulle. 
9. Si le pont est équilibré, comment sont ass ociées les impédances 
Z1 et Z2 ? Comment sont associées Z4 et Z3 ? 
10. Montrer alors que la condition d’équilibre du pont s’écrit sous la 
forme Z1.Z3=Z2.Z4. 
Pour le pont de Hay : 
 La branche AB contient une bobine de résistance R 1 et d’inductance 
L1. 
 La branche BC contient un conducteur ohmique de résistance R 2 et la 
branche AD contient un conducteur ohmique de résistance R 4. 
 La branche DC contient un condensateur de capacité C 3 et un 
conducteur ohmique de résistance R3. 
 
 
11. Ecrire les expressions de Z1,Z2, Z3 et Z4. 
12. En supposant que le pont soit à l’équilibre, déterminer les expressions de R 1 et L1 en fonction de C3, R2, R3, R4 
et ω. Faire les applications numériques pour ω=1,0.10 3rad.s-1, R2=2,0kΩ, R3=1,4kΩ, R4=3,0kΩ et C3=15nF.

--- Page 2 ---

DS3 PCSI2 2022-2023 
physique 
2/4 
Problème 2 : trains à sustentation magnétique. 
Un train à sustentation magnétique utilise les forces magnétiques pour léviter au dessus de la voie ; il n’est donc  pas en 
contact avec des rails, contrairement aux trains classiques. Ce procédé permet de supprimer la résistance  au roulement 
et d’atteindre des vitesses élevées. 
Parmi les technologies, on peut isoler le transrapid qui 
lévite par attraction magnétique grâce à des aimants.  
La seule r éalisation commerciale du Transrapid est à 
l’heure actuelle la ligne de 30 kilom ètres qui fonct ionne 
depuis 2004 entre Shanghai et son a éroport international 
de Pudong. Le trajet s ’effectue en moins de 8 minutes,  à 
la vitesse moyenne de 245 km/h. Sur ce parcours le train 
atteint la vitesse de 430 km/h, il a la capacit é d’accélérer 
de 0 à 350km/h en 2 minutes. 
 
Photo du transrapid.
 
Représentation du système de sustentation magnétique du transrapid. 
L’instabilité de l ’équilibre de la rame en sustentation n écessite l ’asservissement en position de l ’entrefer. Cet  
asservissement est réalisé en utilisant un capteur de position. On se propose dans cette partie d ’étudier le principe d’un 
capteur de position à inductance variable. 
La figure suivante décrit le schéma de principe d’un capteur inductif à entrefer variable dans un montage « push-pull ». 
Le capteur comprend un circuit magn étique composé d’un noyau solidaire du rail fixe et de deux bobines B 1 et B2 sur 
deux noyaux ferromagn étiques en vis -à-vis, solidaires de la rame. Les bobines B 1 et B 2 du capteur sont identiques et 
placées de fa çon symétrique par rapport au rail lorsque la rame est à l’équilibre (à gauche). Ces bobines B 1 et B2 sont 
indépendantes des bobines assurant la lévitation. Elles sont constituées de NC spires de surface 𝑆. 
 
On envisage une variation Δz de la position du train par rappor t à la position d’équilibre z e=δ. En considérant que 
Δz<<δ, on montre que l’inductance des deux bobines situées de part et d’autre du rail s’expriment : 
1 1e
zLL 
 
 et 
2 1e
zLL 
   
Les deux bobines sont alimentées par un générateur de tension idéal de force électromotrice
 ( ) cose t E t  en série 
avec un conducteur ohmique de résistance R. 
 
1. Déterminer les expressions des tensions électriques complexes u1 et u2 en fonction de R, L1, L2, ω et e(t).  
Ces tensions u1 et u2 sont placées à l’entrée du montage présenté sur la figure suivante. L’ALI est pris dans le modèle 
idéal.

--- Page 3 ---

DS3 PCSI2 2022-2023 
physique 
3/4 
 
2. Rappeler les hypothèses attachées au modèle idéal de l’ALI. 
3. Expliquer pourquoi on peut faire l’hypothèse d’un fonctionnement linéaire de l’ALI. Rappeler alo rs la relation 
vérifiée. 
4. Exprimer la tension électrique uS en fonction des tensions u1 et u2. 
5. Déterminer la fonction de transfert complexe T(jω) sous la forme
 
1
O
OS
O
jT
uTj e j






 
  où TO et ωO sont deux 
paramètres à exprimer en fonction de (L1, L2 et R) puis en fonction de (Le, R, Δz et δ). 
6. Effectuer l’étude asymptotique de la fonction de transfert T(jω) à basse fréquence puis à haute fréquence. Pré ciser 
le comportement du filtre à la pulsation ωO.  
7. Tracer le diagramme de Bode asymptotique puis le diagramme de Bode réel de ce filtre. Préciser le type de filtre et 
la bande passante. 
8. Dans quelle gamme de fréquences doit-on travailler pour que T(jω) soit indépendant de la pulsation ? Montrer alors 
que la fonction de transfert est réelle et s’exprime
z

 ?  
On prend pour valeur numérique : R=750Ω ; Le=60mH et une fréquence d’exploitation f=4kHz. 
9. Montrer que le signal de sortie se met sous la forme 
   cosS
zu t E t 
 . Exprimer le déphasage φ. 
Pour pourvoir corriger la position de la rame 
lorsqu’elle s’écarte de sa position d’équilibre, on 
souhaite construire une tension continue qui soit une 
image de l’écart Δz à la position d’équilibre. On utilise 
pour cela un circuit multiplieur de constante de 
multiplication Km=1,00V-1. 
 
10. Exprimer la tension électrique sm(t) en fonction de Km, e(t) et uS(t) puis en fonction de E, Δz, δ, ω et t. 
11. Transformer l’expression précédente et aboutir à la description du signal s m(t) sous la for me d’une décomposition 
harmonique en précisant les amplitudes, les pulsations, et les phases à l’origine des différentes composantes.  
12. Quel filtre faut-il placer en sortie du montage multiplieur pour récupérer une tension continue S m proportionnelle au 
déplacement Δz ? Préciser la nature du filtre et préciser  qualitativement les contraintes sur les paramètres de ce 
filtre. 
13. Exprimer la sensibilité du capteur définie par la relation 
mS
z . Application numérique  : le capteur permet de 
mesurer la tension de sortie à 10mV près. En déduire la plus petite valeur de Δz/δ détectable. On prendra E=6,00V. 
Problème 3 : lissage d’une tension hachée. 
De nombreux moteurs électriques doivent être alimentés par une tension constante E, dont la valeur contrôle la vit esse 
de rotation du moteur et/ou le couple qu’il exerce. Comme la tension d’alimentation est porteuse d’une forte puissance 
électrique, il n’est pas possible de contrôler sa valeur à l’aide de ponts diviseurs de tension, comme on le ferait en 
électronique des signaux : dissiper une forte puissance par effet Joule serait trop coûteux pour l’utilisateur.  
On utilise alors un dispositif nommé hacheur, reposant sur l’utilisation d’interrupteurs commandés, qui permet de 
couper la tension d’alimentation pendant un e durée contrôlable. Cette tension doit ensuite être filtrée par un dispositif 
appelé cellule de lissage pour n’en garder que la composante continue, et pouvoir alimenter le moteur.  
A. Tension en sortie du hacheur. 
Le hacheur délivre la tension e(t) dont le chronogramme est donné ci-dessous. On appelle rapport cyclique de la tension 
e(t) la quantité α=T’/T qui décrit la fraction de période pendant laquelle la tension prend sa valeur haute.  Le hachage est 
fait à la fréquence f = 1,0 kHz.

--- Page 4 ---

DS3 PCSI2 2022-2023 
physique 
4/4 
 
1. Rappeler la définition de  la valeur moyenne d’un signal. Etablir l’expression de cette valeur moyenne
Te pour le 
signal délivré par le hacheur. 
Le développement de Fourier de e(t) s’écrit 
   
1
sin2( ) cos 2 n
n
nEe t E nft n
  


     
2. Retrouver la valeur moyenne
Te en utilisant le développement de Fourier. 
3. Pour obtenir une tension continue à même d’alimenter le moteur sans l’endommager, quel type de filtrage faut -il 
réaliser ? 
B. Cellule de lissage. 
 
Le lissage du signal haché e(t) est effectué par la c ellule représentée ci -
contre où L = 200 mH et C = 10μF. 
4. Montrer sans calcul que la cellule permet de réaliser le filtrage voulu. 
5. Déterminer la fonction de transfert et l’écrire sous la forme : 
  2
1
O
OO
HHj
j
Q




 

 où on exprimera HO, ωO et Q. 
6. Donner la  définition de la pulsation de coupure. Vérifier que la pulsation de coupure s’identifie avec la 
pulsation propre  lorsque le facteur de qualité prend la valeur 
1
2
Q . En déduire la valeur à donner à  R. 
Exprimer et évaluer numériquement fO la fréquence de coupure. 
C. Lissage de la tension hachée. 
On s’intéresse maintenant à l’installation complète : la tension d’entrée de la cellule de lissage étudiée partie B est la 
tension de sortie du hacheur étudiée partie A. 
7. Expliquer sans calcul pourquoi  la tension de sortie s(t) est pratiquement constante et déterminer simplement sa 
valeur S0. 
On s’intéresse à l’ondulation résiduelle, c’est-à-dire aux petites fluctuations de s(t) autour de sa valeur moyenne S0. 
8. Déterminer les amplitudes S1 et S2 du fondamental et de l’harmonique de rang 2 du signal de sortie  en fonction de 
α, E, f, f O HO et Q. Exprimer alors le rapport S 2/S1 et évaluer le numériquement pour α=0,6. Justifier qu’en 
première approximation il est raisonnable de ne considérer que le fondamental pour étudier l’ondulation résiduelle. 
On appelle taux d’ondulation résiduel du signal de sortie le rapport
max min
2 O
SS
S    
9. Déterminer l’expression littérale de η en fonction de , f, f O et Q puis sa valeur numérique. Conclure sur la qualité 
du lissage. 
Analyse d’un diagramme de Bode en amplitude. 
 
 
 
 
 
 
1. Analyser ce diagramme de Bode en amplitude 
pour déterminer la nature du filtre,  l’ordre du 
filtre, le gain statique, la fréquence propre et 
l’éventuel facteur de qualité.