# DS7 forces moments thermo


--- Page 1 ---

DS7 PCSI2 2022-2023 
Physique 
1 
Problème 1 : Etude d’un pendule de torsion. 
 
On note R le référentiel du laboratoire centré sur O et supposé 
galiléen dans cette sous -partie où l’objectif est la 
détermination de la constante de torsion C du pendule. 
On note J0 le moment d’inertie de la  barre par rapport à l’axe 
vertical (Oz), J1 le moment d’inertie d’une sphère par rapport à 
un axe passant par son centre et J le moment d’inertie du 
système S = {barre + sphères} par rapport à (Oz). 
On repère la position de la barre à l’instant t par l’an gle de 
torsion θ(t). On fait tourner le système d’un angle θm puis on le 
lâche sans vitesse initiale. 
Le fil exerce alors sur la barre un couple de rappel dont le 
moment par rapport à ( Oz) a pour 
expression
    ZOM fil C t   , l’angle θO repère la 
position de la barre en l’absence de torsion. 
On introduit également dans la modélisation une action mécanique dissipative dont on donne le moment par 
rapport à l’axe de rotation sous la forme 
   ZM dis t 
  et on fera l’hypothèse que le système est équilibré. 
1. Ecrire le théorème du moment cinétique pour le système S par rapport à l’axe de rotation Oz. 
2. Le traduire en théorème de l’énergie  cinétique et interpréter  les différents termes en faisant apparaître 
une énergie cinétique EC, une énergie potentielle élastique EP, et une puissance dissipée Pdis. 
3. Ecrire alors l’équation différentielle vérifiée par θ(t) en faisant apparaître une pulsation propre ω O et un 
facteur de qualité Q dont on donnera les expressions en fonction de C, J et α. 
On observe des oscillations très faiblement amorties. 
4. Rappeler la condition portant sur Q pour qu’on observe ces oscillations. Déterminer alors l’expression 
générale des solutions de l’équation du mouvement  lorsque cette condition est observée. Préciser 
l’expression des paramètres introduits en fonction de ωO et Q. 
On note T la pseudopériode des oscillations et TO=2π/ωO la période propre des oscillations. 
5. Déterminer l’expression de la pseudo -période T en fonction de T O et ε=(1/2Q). Obtenir un 
développement limité à l’ordre 2 en ε de cette expression puis déterminer  à quelle condition, portant sur 
ε, l’erreur relative introduite en approximant T≈T O reste inférieure à 1%. Donner alors la valeur de Q 
correspondante. 
On observe que l’amplitude des oscillations de la barre autour de la position θ=θ O a diminuée de moitié après 25 
oscillations. 
6. Déduire de cette observation une évaluation de Q. L’approximation T≈T O est-elle bien valide ? 
On admet que le moment d’inertie du système peut s’écrire sous la forme 
2
122OJ J J mL   . 
On mesure la période T des oscillations pour 
différentes valeurs de la longueur L avec des 
sphères de masse m=0,2kg.  
Les résultats sont donnés dans le tableau suivant : 
L(m) 6,0.10-2 7,0.10-2 8,0.10-2 
T(s) 436 509 581 
On souhaite exploiter ce tableau de donnée en utilisant une régression linéaire. 
7. A partir des résultats précédents établir la relation liant T, L, J O, J 1, m et C que l’on va chercher à 
vérifier par la méthode de régression linéaire. 
Le résultat de la régression linéaire donne un coefficie nt directeur a=5,27.10 7s2.m-2 et une ordonnée à l’origine 
b=103s2. 
8. Déduire de ce résultat la valeur numérique de la constante de torsion C du fil.  
Problème 2 : centrale électrique houlomotrice. 
Ce problème étudie différents aspects de la production électri que à partir de l’énergie houlomotrice.  On 
considère un système à corps oscillant avec une partie fixe au fond de l’eau et une partie mobile . 
On modélise ce dispositif par un pendule pesant composé d’un solide S 
en rotation autour de l’axe Oy et complètement immergé dans l’eau. Le 
pendule est fixé au sol (au fond de la mer) par un dispositi f non 
représenté sur le schéma. Le point O est donc fixe par rapport au sol. Le 
mouvement du centre de masse G a lieu dans le plan vertical (xOz). 
On note m la masse et V le volume du solide. J le moment d’inertie du 
solide par rapport à l’axe (Oy), d la distance entre l’axe de rotation et le 
centre de gravité du solide d=OG, µe la masse volumique de l’eau. 
On suppose que la poussée d’Archimède est modélisable par un glis seur 
s’appliquant en G, que la liaison pivot exerce un moment de frottement 
fluide linéaire par rapport à l’axe (Oy) de coefficient de proportionnalité 
α, que la houle exerce une action mécanique de type glisseur 
s’appliquant en G et de résultante
 cos xF t u
 .

--- Page 2 ---

DS7 PCSI2 2022-2023 
Physique 
2/5 
1. Effectuer le bilan des moments dynamiques sur le solide en rotation autour de l’axe (Oy) et établir 
leurs expressions. 
On étudie d’abord la position d’équilibre du solide en absence de houle. 
2. Vérifier que la position θ O=0 est une position d’équilibre. Déterminer un critère portant sur m, V et 
µe pour que cette position soit stable. 
On reprend l’étude du mouvement du solide lorsqu’il est soumis à la houle. 
3. Déterminer l’équation du mouvement du solide. 
On étudie alors les oscillations de faible amplitude autour de la position d’équilibre stable θO=0. 
4. Montrer que l’équation du mouvement se met sous la forme 
2 .cos( )O
OO tQ
      
  où on 
précisera les expressions de ωO, Q et ΩO en fonction de µe, V, m, J, g, d, α, β. 
5. Calculer la fréquence propre f O avec les données suivantes  : g=10m.s-2, d=10m, µe=1,03.103kg.m-3, 
V=103m3,  m=300 tonnes. On prendra J≈md2. 
On se place maintenant en régime sinusoïdal forcé. 
6. Introduire le signal complexe θ(t) et traduire l’équation différentielle précédente. En déduire 
l’amplitude complexe θO(ω). Quelle est l’opération de filtrage réalisée par le système ?  
7. Commenter les caractéristiques du système sachant que la période typique de la houle est de l’ordre 
de 10 à 20 secondes. 
8. En reprenant le théorème du moment cinétique,  effectuer un bilan de puissance sur le 
fonctionnement du système et indiquer quel élément de la modélisation per met d’envisager une 
conversion de l’énergie mécanique en énergie électrique. 
9. En déduire l’expression de la puissance mécanique P diss(t) dissipé e dans ce système, puis 
déterminer sa valeur moyenne <Pdiss>(ω). 
10. Tracer l’allure de <Pdiss>(ω). 
Problème 3 : compression d’un gaz. 
 
On souhaite mener l’étude de la compression quasi-statique (réversible) d’un gaz à l’aide d’un système à piston  
supposé parfaitement calorifugé . L’objectif est de prélever du gaz sit ué dans un réservoir R 1, de grandes 
dimensions, maintenu à la pression P1 et à la température T1 constantes, de le comprimer, puis de le refouler dans 
un second réservoir R2, lui aussi de grandes dimensions, maintenu à la pression P 2 et la température T2. 
On considère le gaz parfait de masse molaire M et de rapport des capacités calorifiques 
1, 40P
V
C
C   constant. 
Données : pour le réservoir R1 : T1=300K ; P1=105Pa ; pour le réservoir R2 T2= (?) K P2=3.105Pa. 
La constante des gaz parfaits : R=8,31J.mol-1.K-1. Masse molaire moyenne de l’air : M=29,0g.mol-1. 
La transformation s’effectue en trois étapes : 
 L’admission (I) : La soupape d’admission S 1 est ouverte, la soupage S 2 d’échappement est fermée. Le 
piston Π est initialement au fond du cylindre ( position A), le volume interne du cylindre est alors 
négligeable. Par déplacement du piston, une masse m de gaz est aspirée dans le cylindre jusqu’à ce 
qu’on atteigne un volume V1 (position B). 
 La compression  (II) : Les deux soupapes étant fermées, la mass e de gaz est comprimée, par 
déplacement quasi-statique et réversible du piston, de l’état (P1,V1,T1) à l’état (P2,V2, T2). 
 Le refoulement (III) : La soupape S 1 est fermée, la soupape S 2 ouverte. Le gaz est refoulé à P 2 et T2 
constantes dans le réservoir R2 jusqu’à ce que le piston soit ramené à la position A. 
Les variations éventuelles d’énergie de pesanteur et d’énergie cinétique sont négligées.  
1. Caractériser la transformation (II)  subie par la masse m de gaz lors de l’étape de compression  avec un 
vocabulaire précis. Nommer et écrire la relation qui est alors vérifiée par les états (1) et (2) en fonction 
du couple de variables de votre choix. 
2. Déterminer la température T2 en fonction de T1, P1, P2 et γ. Faire l’A.N.

--- Page 3 ---

DS7 PCSI2 2022-2023 
Physique 
3/5 
3. Représenter sur un diagramme (P,V), dit de Clapeyron, les transformation associés aux trois étapes d e 
fonctionnement du compresseur en  précisant soigneusement  la loi P=f(V) vérifiée par le gaz sur 
chaque étapes. 
4. Déterminer W I le travail reçu par la  masse m  de gaz de la part du piston  lors de la phase (I) en 
fonction de P1 et V1. Déterminer alors de même W III reçu par la masse m de gaz de la part du piston lors 
de la phase (III) en fonction de P2 et V2. 
5. Déterminer WII le travail reçu par la masse m du gaz de la part du piston lors de la phase (II ) en fonction 
de P1, P2, V1, V2 et γ. 
6. Préciser sur le graphique de la question 2 comment on peut visualiser le travail reçu par le gaz de la part 
du piston sur un cycle de fonctionnement du compresseur. 
7. Déterminer WPiston le travail total reçu par le gaz de la part du piston  sur un cycle, et montrer la relation 
21pistonW H H
 
8. Exprimer alors le travail massique w fourni par le piston pour faire passer une masse unitaire de gaz 
depuis R1 vers R2 en fonction de γ, R, M, T1 et T2. Faire l’A.N. 
Problème 4 : stockage du CO2. 
a. Exploitation du diagramme (P,T). 
Les activités humaines ont accru sensiblement la concentration en CO 2 de l’atmosphère terrestre, autour de 
280ppm il y à 250 ans, il est actuellement de 387ppm (soit une augmentation de 38%).  
Afin de ne pas dépasser la limite de 450  ppm au -delà de laquelle les conséquences le plus dramatiques du 
réchauffement climatique seront inévitables, de nombreuses options sont envisagées afin de limiter le rejet de 
CO2 dans l’atmosphère. 
Une proposition, discutable dans l’état d’esprit et dans la forme, consiste à former des blocs de CO 2 solide à 
l’aide d’installations frigorifiques puis de les laisser tomber dans des fosses marines.  
Pour l’océan, on fournit les données suivantes : température TO=280K, masse volumique ρO=280K. 
Pour le CO2, on fournit le diagramme des phases présenté dans l’annexe 1. 
1. Compléter le diagramme fourni en annexe 1 en précisant  l’état physique stable pour le CO 2 dans les 
domaines (1), (2) (3) et (4). 
2. Nommer les points (c) et (d) et préciser leur particularité. 
3. Est-il envisageable d’observer une transition de phase vapeur→liquide à la température de T O=280K ? 
Si oui, déterminer une valeur numérique de la pression de vapeur saturante du CO 2 à la température TO. 
4. A quelle pression observe-t-on la solidification du CO2 à la température de 280K ? 
On fournit la loi donnant l’évolution de la pression dans les océans en fonction de la profondeur z  : 
  OOP z P gz 
 où PO=1bar à la surface, ρO=1,03.103kg.m-3 et g=9,81m.s-2 est l’accélération de la pesanteur. 
5. Déterminer la profondeur minimale à laquelle doit être effectué le stockage du CO 2 pour qu’il reste sous 
forme solide. Faire l’application numérique. Commenter le résultat obtenu.  
b. Exploitation du diagramme (P,v). 
Le diagramme de Clapeyron du dioxyde de carbone est donné en annexe 2 , on y a représenté les isothermes 
dites d’Andrews pour les températures 235K, 250K, 265K, 280K, 310K, 325K, 340K.  
On fournit également les données suivantes : 
Constante des gaz parfaits : R=8,31 J.K-1.mol-1, Masse molaire de CO2 : M=44,0 g.mol-1. 
Données thermodynamiques pour les phases liquide saturant et vapeur saturante pour le CO2 : 
T(K) 235 250 265 280 295 
Psat (Bar) 10,7 18 28,1 41,9 59,5 
vL (m3.kg-1) 9,0.10-4 9,6.10-4 1,0.10-3 1,1.10-3 1,3.10-3 
vV (m3.kg-1) 3,6.10-2 2,1.10-2 1,3.10-2 8,1.10-3 4,7.10-3 
hL(kJ.kg-1) 113 144 177 213 256 
hV(kJ.kg-1) 435 437 435 427 408 
6. Placer sur le diagramme  fourni en annexe  le point critique C, identifier alors clairement la courbe de 
rosée et la courbe d’ébullition. Préciser l’état du système dans les différents domaines. 
7. Indiquer sur chaque isotherme la température correspondante. 
8. Vérifier pour la température T=280K la cohérence entre le diagramme (P,v) et le d iagramme (P,T).  
9. En justifiant au préalable votre démarche, rajouter au diagramme l’isotherme T=295K. 
10. En appliquant un modèle de gaz parfait au dioxyde de carbone, déterminer le volume massique de la 
phase vapeur saturant à T=295K. Comparer alors à la valeur tabulée et commenter le résultat o btenu.

--- Page 4 ---

DS7 PCSI2 2022-2023 
Physique 
4/5 
Une masse m O=18,0kg de CO 2 initialement en phase vapeur (sèche)  est soumise à une compression isotherme 
qui l’amène dans un état (II) d’équilibre liquide vapeur correspondant à la situation de stockage dans une 
bouteille de volume fixe 54L. On envi sage ensuite une surchauffe accidentelle du local de stockage qui l’amène 
dans l’état (III). 
 Etat  (I) Etat (II) Etat  (III) 
Température (K) 280 280 310 
Volume 270L 54L 54L 
 
11. Placer sur le diagramme les points représentatifs des états (I), (II) et (III) , en déduire l’état physique 
dans lequel se trouve le CO2 dans chaque cas. 
12. Pour l’état (II) déterminer la composition du système en exprimant puis en évaluant numériquement les 
masses de CO2 mL en phase liquide et mG en phase vapeur. 
13. Evaluer numériquement H(II) l’enthalpie puis U(II) l’énergie interne du système dans l’état (II). 
Pour évaluer l’enthalpie du système dans les états (I) et (III), on exploite le modèle de gaz de Van der Waals  qui 
se traduit par : 
 l’équation d’état 
 2
a RTP v bvM
     avec a=1,88.102 USI et b=9,70.10-4USI. 
 l’expression de l’énergie interne massique de la forme 
VO
au c T u v     avec cV =6,48.102J.K-1.kg-1 et 
uO=2,35.102kJ.kg-1. 
14. Rappeler l’équation d’état du gaz parfait et en déduire l’approximation qui est faite. Déte rminer alors 
l’expression de l’énergie interne molaire pour le gaz parfait à partir de celle donnée pour le gaz de Van 
der Waals. 
15.  Evaluer numériquement l’énergie interne du système dans l’état (I) et dans l’état (III) avec le modèle de 
Van der Waals et avec un modèle de gaz parfait. Commenter les résultats obtenus. 
16. Déterminer le transfert thermique à fournir au système pour effectuer  la transformation de (II) vers (III) 
en exploitant les résultats des questions 13 et 15.

--- Page 5 ---

DS7 PCSI2 2022-2023 
Physique 
5/5 
 
NOM :    Prénom : 
 
 
ANNEXE 1 : 
 
 
 
 
ANNEXE 2 :