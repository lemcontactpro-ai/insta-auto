# corrigé du DS6 mécanique électromag


--- Page 1 ---

Corrigé du DS6 PCSI2 2022-2023 
physique 
1/6 
Problème 1 : Ceinture de Van Allen. 
a. Mouvement d’une particule chargée dans un champ magnétique uniforme.  
1. La force de Lorentz s’exerce sur la particule, dans un champ magnétique elle s’exprime : 
BvqF

   
Cette force magnétique est perpendicu laire à la vitesse de la particule, sa puissance est donc nulle. Il n’y a pas 
d’autre force envisagée dans le système, on peut en déduire, d’après la loi de la puissance cinétique que 
l’énergie cinétique EC est conservée au cours du mouvement, c’est donc bien une constante. 
2. On applique la 2LN à la particule dans le référentiel R supposé galiléen :
BvqFdt
pd
R





  
On projette alors dans la base cartésienne associée au repère spatiale (Oxyz) ce qui donne :






0zm
xqBym
yqBxm


  
3. On intègre 
0zm   avec la C.I. v Z(0)=vOL pour obtenir  : 
OLZ vtv )( . On obtient bien une vitesse 
longitudinale 
OLL vv    constante au cours du mouvement. 
On intègre à nouveau, avec la condition initiale z(0)=0 pour obtenir : 
tvtz OL.)(   
4. On reprend les équations du mouvement transverse : 





xqBym
yqBxm

  ce qui donne 





)2(
)1(
xy
yx



  
Où on a posé pour expression de la pulsation cyclotron : 
m
qB  
5. On pose u = x+jy, vérifiant l’équation (1)+j(2) : 
0 uju    
On intègre alors cette équation pour obtenir avec la C.I. 
 Ovu )0(  : 
 tjvu O   exp  
On extrait la partie réelle et la partie imaginaire pour obtenir : 
 tvtv Ox cos)(   et 
 tvtv Oy  sin)(  . 
6. On peut alors intégrer ces équations avec les C.I. x(0)=0 et y(0)=0 pour obtenir :  
 tvtx O  sin)( 
 et 
  1cos)(   tvty O   
7. On établit à partir des coordonnées 
précédentes l’équation  : 
22
2 )( 







  

OO vvytx
  
qui est l’équation d’un cercle Γ de ray on 

 Ova
 et de centre C 




  

Ov,0 . 
8. Les trajectoires projetées dans le plan 
transverse ont les allures ci dessous. 
 
9. L’énergie cinétique transverse s’exprime 
  




  2
222
22
2
1
2
1
2
1
m
aBqmammvE OC   
On peut alors mettre l’énergie cinétique transverse sous la forme 





 2
222
2
1
m
aBqmµBEC  avec
m
Baqµ 2
22
   
10. Pour un électron d’énergie cinétique ECe, la vitesse prend la valeur : 
18 .10.4,12  smm
Ev
e
Ce
e  
Cette valeur numérique représente près de la moitié de l a vitesse de la lumière, une cinématique relativiste 
devrait être appliquée pour mener son étude.  
La pulsation cyclotron prend la valeur : 
14 .10.8,8  sradm
eB
e
e   
Cas de L’électron 
Cas du proton 
x 
y

--- Page 2 ---

Corrigé du DS6 PCSI2 2022-2023 
physique 
2/6 
Sa vitesse transverse s’exprime : 
e
Ce
O
m
Ev 11
20
 , le rayon du cercle est  : 
mEmeBa Ceee
310.5,111
201   
De même pour le proton, on trouve 
17 .10.0,1  smv p  inférieur au dixième de la vitesse de la lumière, une 
cinématique non relativiste est alors correcte pour l’étude du mouvement de ce proton.  
La pulsation cyclotron prend la valeur 
11 .10.8,4  sradP , le rayon prend la valeur
ma P
510.0,2  
11. Dans la situation étudiée, le champ magnétique est de la forme 
zeBB 
 ,les lignes de champs sont donc 
des droites parallèles à l’axe Oz, on peut donc construire un tub e de champ par un cylindre s’appuyant 
sur une courbe quelconque dans le plan xOy et d’axe Oz.  
12. Dans son mouvement, la particule se déplace à la vitesse v OL selon Oz en même temps que sa trajectoire 
est projetée dans xOy dessine le cercle Γ. Sa trajectoire est alors une hélice s’enroulant autour du tube 
de champ construit sur le cercle Γ de rayon a. 
La vitesse longitudinale est constante, une révolution sur Γ  s’effectue en T =2π/ω ce qui donne une distance 
parcourue 
 OLvb 2  On évalue alors 
0,2
10
22 


O
OL
v
v
a
b  
b. Mouvement d’une particule chargée dans un champ magnétique non uniforme.  
13. On reprend l’évaluation de la force exercée sur une particule  chargée par le champ magnétique pour 
cette nouvelle situation. 
BvqF

  
En coordonnées polaires, la trajectoire restant quasiment circulaire : 
 la particule présente un vecteur vitesse de norme v ┴ dans la direction orthoradiale dans le sens horaire 
pour une charge positive et trigonométrique pour une charge négative. 
 Le rayon de cette trajectoire quasi-circulaire est a(z)   
 ce qui donne : 
Z
Z
Z B
dz
dBza
v
vqF 0
2
)(
0 


 
 on obtient alors selon l’axe Oz : 
dz
dBvzaqF z
z
2
)(   .  
L’expression du rayon étant la même qu’en première partie 
)()( z
vza 
 , elle devient 
dz
dB
z
qvF z
z
)(2
2

   
L’expression de la pulsation étant 
m
qBz Z )( , on arrive bien à 
dz
dB
zB
mvF z
Z
z
)(2
2
  
14. En passant de O à M 1, les lignes de champs se resserrent,  l’intensité du champ magnétique augmente 
donc lorsque z augmente. On en déduit que 
dz
dB z  est positif dans cette région. 
De même l’intensité du champ augmente lorsqu’on passe de O à M 1’ et elle diminue lorsque z augmente, on en 
déduit que 
dz
dB z  est négatif dans cette région. 
15. Dans la région z>0 la composante de F Z de la force est négative puisque la figure 2 nous montre que B Z 
est positif et que 
dz
dB z  est positif.  Dans la région z<0 la composante de F Z de la force est positive 
puisque la figure 2 nous montre que B Z est positif et que 
dz
dB z  est négatif. On en déduit que la force 
magnétique exerce une force de rappel sur la particule chargée cherchant à la ramener vers le point O. 
16. L’énergie cinétique de la particule s’exprime : 
22
2
1
2
1
LZLCC mvµBmvEE    
On obtient alors que 
 ZCL µBEmv  22 . Cette grandeur est nécessairement positive ce qui implique que B Z 
doit rester inférieur à une valeur maximale donnée par 

C
Z
EBB  max  
17. Si le champ prend la valeur B max en M1 et M1’, le centre guide ne peut pas franchir ces points et reste 
confiné au segment [M1’ M1].

--- Page 3 ---

Corrigé du DS6 PCSI2 2022-2023 
physique 
3/6 
La vitesse du centre guide est donnée par 
   ZZCL BBm
µµBEmv  max
22  
Par symétrie de la carte de champ, B Z, et par conséquent v L, est une fonction paire de la cote z, justifiant la 
périodicité du mouvement. Un quart de la trajectoire est parcourue sur l’aller de O en M 1, et on peut  écrire : 
 ZL BBm
µvdt
dz  max
2
 et par séparation des variables on obtient : 
 
dt
BBm
µ
dz
Z

max
2  
L’intégration donne alors : 
 
 

4/
00
max
1
2
Tz
Z
dt
BBm
µ
dz  finalement on a bien 
 

1
0 max24
z
ZBB
dz
µ
mT  
Problème 2 : A propos de la sonde Rosetta. 
Questions préliminaires 
1. La force gravitationnelle exercée par le soleil s’exprime
  2
S
S
GmMF M u r
 . 
2. Le travail élémentaire de la force s’exprime alors : 
2. SS
S
mGM mGMW F d OM dr d rr     
  
On met ainsi en évidence que la force de gravité est conservative associée à l’énergie potentielle  : 
() S
P
mGMEr r
 en prenant pour convention une énergie potentielle nulle à distance infinie. 
3. On applique le théorème du moment cinétique en T pour le satellite dans le référentiel R G supposé 
galiléen :
0
S
O
S
R
dL OM Fdt
   

  
D’après les propriétés du produit vectoriel, le vecteur 
OM
  est toujours perpendiculaire  à 
OL
 , M est donc 
astreint à se déplacer dans le plan normal à 
OL
  et passant par O qui est unique. La trajectoire est plane. 
En introduisant la constante des aires C et le 
vecteur unitaire
Ze
 , le moment cinétique s’écrit : 
ZT emCL 

. 
4. On introduit alors la base polaire (voir 
schéma ci-contre) dans laquelle : 
rOM re
 
Mrv re r e 
  
   
2 2Mra r r e r r e      
 
5. La loi des aires découle de la conservation de la norme du moment cinétique. 
On obtient en utilisant la cinématique : 
2
O M z zL OM v mr e mCe    
  d’où 
2rC 
  
D’autre part, l’aire élémentaire balayée par le vecteur position lors d’un déplacement élémentaire s’exprime  : 
drOMdOMdA 2
2
1
2
1 
  on obtient alors : 
22
1 2 Crdt
dA    
D’où la loi des aires : L’aire balayée par le vecteur position est la même si on considère deux intervalles de 
temps égaux au cours du déplacement de M.  
6. On exploite l’hypothèse d’un rayon constant égal à R 1 et on applique la 2nd loi de Newton : 
S
M
T M S
R
dp M a Fdt
 
 qu’on projette sur 
re
  et
e
  pour obtenir 
2
1 2
1
1 0
SGMR R
R


 
 
  
On en déduit que la vitesse de rotation est constante et s’exprime 
3
1
S
T
GM
R . 
On exprime la période de rotation de la Terre  
2
T
T    d’où la troisième loi de Kepler : 
22
3
1
4
S
T
R GM


--- Page 4 ---

Corrigé du DS6 PCSI2 2022-2023 
physique 
4/6 
7. On écrit l’énergie mécanique : 
 
2
1
1
1
2
TS
M C P T T
GM ME E E M R R     d’où 
12
TS
M
GM ME R  
8. On exploite la troisième loi de Képler en util isant la période de révolution sidérale de la Terre autour du 
soleil T=365,25jours ce qui donne 
2
113
1 2 1,50.104
SGM TRm   correspondant bien à 1ua. 
On déterminer alors numériquement 
41
1
1
2,98.10 .S
TT
GMv R m s R
     
9. La troisième loi de Kepler donne pour un satellite autour de la Terre
22
3
4
T
T
R GM
  
10. Par définition, u n satellite géostationnaire est constamment situé à la verticale au -dessus d’un même 
point de la planète Terre. 
Si on suppose que le plan de la trajectoire n’est pas le plan de l’équateur, le satellite sera nécessa irement au-
dessus de points situés dans l’hémisphère Nord la moitié du temps et au -dessus de points situés dans 
l’hémisphère Sud l’autre moitié du temps. Il n’est donc pas toujours au -dessus du même point. On en 
conclut que le seul plan orbital possible pour un satellite géostationnaire est le plan équatorial. 
Pour qu’il soit géostationnaire il faut alors que sa rotation soit synchrone de la Terre ce qui donne une 
période de 24h. 
Le rayon de la trajectoire géostationnaire est alors : 
2
73
2 4, 22.104
T
Geo
GM TRm   
Budget énergétique pour transfert orbital. 
11. D’après la figure 
12
2
RRa   
12. Sur une trajectoire circulaire de rayon R1 : 
1,
12
S
MR
GmME R  par analogie 
,
12
S
Ma
GmME RR   
13. Sur la trajectoire circulaire de rayon R1 : 
1 1 1, , ,M R C R P RE E E   
avec 
1,
12
S
MR
GmME R  ; 
1,
1
S
PR
GmME R  et 
1
2
,1
1
2
CRE mv  d’où 
1
1
SGMv R  
Sur la trajectoire elliptique 
2
,
1 1 2
1
2
SS
C a e
GmM GmME mv R R R     d’où 
2
1 1 2
22 SS
e
GM GMv R R R   et 
12
1 1 2 1 1 2
222SS
e
GM GM RRv R R R R R R   
 On en déduit bien 
2
1
1 1 2
2 1S
e
GM Rv v v R R R
        
14. On sait que a=3,5ua et R1=1ua, on en déduit 
21 26R a R ua    puis 
319, 2.10 .v m s   
Lien entre budget de vitesse et carburant. 
15. On exploite l’équation différentielle proposée et on l’intègre entre un état initial où le système prése nte 
les caractéristiques (v i, mi=mO+Δm) et un état final (vf, mf=mO) avec Δm la masse de carburant utilisée 
et mO la masse du système propulsé grâce à la combustion de ce carburant ce qui donne  : 
11
ff
ii
tt
ett
dv dm
v dt m dt
  puis 
 1 ln
f
fi
ei
mvvvm
  
  ce qui donne bien 
ln 1e
O
mvv m
    
  
16. On obtient directement : 
exp 1
e
vr v
 
  
17. L’évaluation numérique donne
313,0.10 .ev m s   
18. Pour réaliser directement l’injection, il faut produite une 
variation de vitesse Δv=9,2km.s -1 ce qui correspond sur la 
courbe de la figure 2. à un coefficient r=12, 5 et une masse 
totale embarquée 
 
41 1,75.10OOm m r m kg     
Cette masse est égale à 2,5 fois la charge utile embarquable 
dans ariane 5, l’injection directe est impossible.

--- Page 5 ---

Corrigé du DS6 PCSI2 2022-2023 
physique 
5/6 
19. L’énergie mécanique du système dans le référentiel g éocentrique est conservée, ce qui donne  le bilan 
suivant entre l’état 1 (r→∞, v1) à l’état 2 (r→∞, v2) : 
12mmEE 
 soit 
22
12
11 0022mv mv    et finalement
12vv . 
20. La vitesse dans R S d’un point immobile dans R T est donné par
Tv
 , pour un point animé d’une vitesse 
1v
  
dans RT, la vitesse dans RS sera 
1, 1STv v v
  et de même 
2, 2STv v v
  
On obtient alors 
1, ..S T y xv v e v e
  d’où 
22
1,STv v v   
et 
1, . cos . sin .S T y x yv v e v e v e   
  d’où 
22
2, 2 sinS T Tv v v v v     
Finalement
2 2 2 2 2 sinT T Tv v v v v v v        
21. On obtient 
2 2 2 2 2 sinT T Tv v v v v v v       A.N : 
13,3. .v km s   
22. On observe que sur les 9,2km.s -1 nécessaire pour atteindre la 
trajectoire de la comète, 3,3km.s -1 sont obtenue par une simple 
assistance gravitationnelle sans qu’aucun carburant soit 
nécessaire. En revanche pour obtenir cet effet d’assistance 
gravitationnel, il faut que la trajectoire de la sonde soit 
synchronisée sur la trajectoire des planètes utilisées (Terre, 
Mars et deux fois Terre pour R osetta ce qui entraina une 
trajectoire de Rosetta qui est composée de trois rotations autour 
du Soleil) ce qui demande plusieurs années de voyage. 
23. On obtient le polynome suivant en exploitant la relation donnée dans l’énoncé  : 
2
2
2
20
tan 2
RR     
, on en déduit le discriminant  
   
2
2
22
1441
tan sin 22
 

  et les 
racines
 
1 1
sin 2
r  


    et puisque R est positif on obtient : 
 
1 1
sin 2
R  

   
L’application numérique donne
42,6.10R km  ce qui donne
4 0,6T GéoR R R  
La trajectoire n’entre pas en collision avec la Terre (ouf) mais sa distance d’approche minimale est tout de 
même nettement inférieure au rayon des satellites géostationnaires ce qui demanderait de prendre des 
précautions. 
Analyse de données : chariot dans un parc d’attraction. 
1. Avec les unités fournies sur l’axe de s ordonnées, on est assuré que R n est associée à la courbe 4 où on 
représente bien une force dont l’unité correspond bien au (10 5N). 
Pour les trois autres courbes, on a évidemment la même unité (MJ)… 
Lorsqu’on lance le chariot, on s’attend à une diminition  de E P sur la rampe suivie de variation 
pseudopériodique sur le looping ce qui correspond à la courbe 2, on s’attend à une croissance de l’énergie 
cinétique sur la rampe suivie de variation pseudopériodique sur le looping ce qui correspond à la courbe 3, 
on s’attend à une énergie mécanique constante si le système est conservatif, ou strictement décroissante si le 
système présente des facteurs d’amortissement ce qui correspond à la courbe 1. 
Ces considérations permettent donc de suggérer que : 
 La courbe 1 es t celle de l’énergie mécanique, qui décroit au cours du temps, le système présente donc 
des facteurs dissipatifs, comme par exemple des forces de frottement. (ce qui répond à la Q2).  
 La courbe 2 est celle de l’énergie potentielle de pesanteur. 
 La courbe 3 est celle de l’énergie cinétique. 
2. (Oui car Em décroissante). 
3. On évalue la hauteur initiale en écrivant l’énergie potentielle sous la forme usuelle 
 PE z mgz , on 
obtient pour l’instant initial 
,PiE mgh  avec E P,i=6,3MJ, g=10m.s -2
 et m=10 4kg ce qui donne une 
hauteur 
,
63
PiEhm mg

--- Page 6 ---

Corrigé du DS6 PCSI2 2022-2023 
physique 
6/6 
Pour les vitesses, on écrit l’énergie cinétique sous la forme 
 
21
2
CE v mv , on obtient dans l’état initial 
une énergie cinétique nulle et donc une vitesse initiale nulle 
, 0CiEJ   ; ensuite on obtient une énergie 
cinétique maximale
,max 5,5CE MJ   ce qui conduit à une vitesse maximale de 
,max 1
max
2 33 .
CEv m s m
  
4. On repère l’instant où le chariot quitte l’armature du looping en observant quand la composan te normale 
de la réaction s’annule, ce qui donne t déco≈32s. Le chariot se trouve alors au maximum de l’énergie 
potentielle c’est-à-dire en haut de la boucle du looping. 
Il semble évident que ce n’est pas le moment idéal pour «  dérailler », un système de récupération du chariot 
est donc prévu pour éviter que l’ensemble tombe avec les passagers sous le chariot… 
On compte alors deux tour entiers complets effectués sur le looping avant de remonter sur la boucle et d’être 
dévier vers une piste de récupération du chariot. 
5. La durée du premier looping est évaluée entr e le premier minimum de l’énergie potentielle et le second 
ce qui donne approximativement tO=19s et t1=24s et une durée du looping de 5s. 
Si évalue une valeur moyenne de l’énergie cinétique sur le premier tour, on obtient une énergie cinétique 
moyenne EC,moy≈4MJ ce qui donne une vitesse moyenne v m≈28m.s-1. 
Le périmètre du looping est égal à π.h ce qui donne un tour effectué en 
7
m
hts v
    
Le modèle est très grossier, il permet tout juste de retrouver le bon ordre de grandeur de la durée du loopi ng. 
Il faudrait tenir compte des variations de la vitesse en fonction de la position pour obtenir un meilleur 
modèle et une meilleur estimation de la durée de ce tour.