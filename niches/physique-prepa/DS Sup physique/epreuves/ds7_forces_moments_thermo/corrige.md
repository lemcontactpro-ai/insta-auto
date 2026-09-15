# corrigé du DS7 forces moments thermo


--- Page 1 ---

DS7 PCSI2 2022-2023 
Physique 
1 
Problème 1 : Etude d’un pendule de torsion. 
1. Les actions mécaniques sur le pendule sont : 
 Action de gravité de moment nul car le système est équilibré par rapport à (Oz).  
 L’action du fil de torsion de moment 
    ZOM fil C t   . 
 L’action dissipative de moment 
   ZM dis t 
  
On applique le TMC au système de moment d’inertie total J par rapport à l’axe (Oz)  : 
  OJ C t     
  
2. On peut traduire le TMC en TEC en multipliant toute l’équation par la vitesse de rotation ce qui donne  
  
2
OJ C t      
 qu’on réécrit   
  
22211
22
Od J C t      
  
Et qu’on interprète terme à terme sous la forme  
    ,C P elas dissd E t E t P   
Où  l’énergie cinétique s’exprime
 
21
2
CE t J 
 , l’énergie potentielle s’exprime 
    
21
2
POE t C t   
Et la puissance dissipée par l’action mécanique correspondante est 
2
dissP 
  
3. On reprend le théorème du moment cinétique et on l’écrit sous la forme 
O
CC
J J J
     
  
Puis on la met sous forme canonique 
22O
O O O
Q
       
  avec 
O
C
J  et
CJQ    
4. Pour qu’on observe des oscillations, il faut que le système présente un régime transitoire 
pseudopériodique. Il faut alors que le facteur de qualité vérifie 
0,5Q  
Pour exprimer les solutions, on commenc e par écrire le polynôme caractéristique  : 
22 0O
Orr Q
    , puis le 
discriminant 
2
2
1 40O
Q     négatif à cause de la condition Q>0,5. Les racines s’écrivent alors sous la 
forme 
 
2 11 4 12
Or j Q jQ
 
        
On écrit alors la solution générale d e l’équation homogène 
   exp cosH
tS t A t 
     et la solution 
particulière de l’équation complète 
 POSt   et alors
       exp cosG H P O
tS t S t S t A t    
        
Les paramètres introduits s’expriment  
1
2
O
Q

   (ou 
2
O
Q  ) et 
2
11 4
O
Q    
5. La pseudopériode s’exprime 
1
2
2
2 2 1 1 4O
T Q



     ce qui donne 
 
1
2 21OTT 

  
Le DL2 de cette expression donne 
2
1 2
OTT     
La condition sur l’erreur relative est alors 
2
2102
O
O
TT
T
    ce qui donne 
1 35
0, 2 2
Q  
6. On traduit l’observation par la relation 
25 1exp 2
T

 ce qui donne 
25 ln 2OT
  et 
25 113ln 2Q   
L’approximation T≈TO est bien valide. 
7. On reprend les résultats précédents : 
2O
JTT C  et la relation donnée 
2
122OJ J J mL    
Par régression linéaire, on va alors chercher à vérifier le comportement affine de 
 
22T f L  puisqu’en théorie 
la relation s’écrit 
 
22
22
1
48 2OO
mT T J J L CC
     
8. On exploite le coefficient directeur pour obtenir 
2
7 2 28 3,00.10 .mC kg m sa
  .

--- Page 2 ---

DS7 PCSI2 2022-2023 
Physique 
2/5 
Problème 2 : centrale électrique houlomotrice. 
1. Le bilan des actions mécaniques sur le système est : 
L’action de gravité pris comme un glisseur s’appliquant en G :
 , . yP OyM OG P e
   
Dans la base cartésienne
sin
0
cos
d
OG
d




  ; 
0
0P
g


  ce qui donne
, sinP OyM mgd 
  
L’action de la poussée d’Archimède qui est obtenue par la même démarche 
 , sinOy eM µ V gd 
  
L’action de la houle toujours par le modèle de glisseur 
 , cos cosF OyM d t   
  
L’action de la liaison pivot qu’on écrit sous la forme 
,pivot OyM 
  
2. On écrit une condition d’équilibre, donc le système est immobile et on ajoute l’hypothèse sans 
houle, donc seul la gravité et la poussée d’Archimède interviennent :
,, 0OyP OyMM 
  
On obtient 
  sin 0em µ V gd  , on observe bien que la position θO=0 est une position d’équilibre. 
Si on écarte le système d’un petit angle δθ par rapport à la position θ O=0, la position est stable si le moment 
exercée ramène le système à la position d’équilibre, il doit donc être négatif.  
On en conclut que la condition pour que la position d’équilibre θ O=0 soit stable est 
eµ V m  
3. On écrit le théorème du moment cinétique pour le système par rapport à (Oy) pour obtenir 
l’équation du mouvement du système : 
   sin cos coseJ m µ V gd d t        
  
4. On effectue la linéarisation des différents terme autour de la position  θ O=0 ce qui donne  
   coseJ m µ V gd d t       
 qu’on met sous la forme fournie 
2 .cos( )O
OO tQ
      
 où
 e
O
µ V m gd
J   
 eµ V m gdJQ 
   et 
O
d
J
 . 
5. On exprime et évalue 
11 1 2,5.102
e
O
µV gf Hz md
   . 
6. On introduit le signal complexe 
   expOt j t    pour lequel l’équation différentielle se traduit 
par 
 
22 .exp( )O
OOt j j t Q
        On en déduit
 
22
O
O
O
O j Q
   

  
On observe que le module de cette amplitude tend vers une valeur nulle lorsque ω→∞ et tend vers une valeur 
non nulle 
2
O
O
  lorsque ω→0. On en déduit que le système réalise un filtre de type passe bas.  
7. Le système laisse passer les basses fréquences et sera donc mis en mouvement par la houle de 
fréquences typiques 10-1Hz puisque ces fréquences se situent sous la fréquence de coupure du filtre. 
Il resterait à vérifier le facteur de qualité pour que l’amortissement ne soit pas trop fort . 
8. On reprend le TMC ce qui donne  
   
2sin cos coseJ m µ V gd d t          
   
et on réinterprète terme à terme    
   C P diss houle
d E E P pivot Pdt     
Où 
CdE Jdt 
  ; 
    sinP
e
dE t µ V m gddt 
  ; 
2
dissP 
  et 
 cos cosHouleP d t    
  
La puissance fournie par la houle entraine alors des variations périodiques de E C et EP non extraites du système 
et le seul terme réduisant l’énergie mécanique en permettant d’envisager une conversion en énergie électrique est 
celui tenant compte de la dissipation par la liaison pivot  . 
9. 
   cosOtt     ; 
   sinOtt    
 avec 
 
2
222
O
OO
O
O
Q

  

   
ce qui donne 
 
 
22
2
2
222
sinO
diss
O
O
Pt
Q
 
  

   puis 
 
22
2
222
0,5. O
diss
O
O
P
Q

  

 

--- Page 3 ---

DS7 PCSI2 2022-2023 
Physique 
3/5 
10. On obtient l’allure suivante  pour la courbe  d’évolution de la puissance moyenne dissipée en 
fonction du temps. 
 
Problème 3 : compression d’un gaz. 
1. Lors de l’étape (II) de compression, la masse 
m de gaz subie une transformation 
adiabatique puisque le système est 
calorifugé et quasistatique réversible. 
Puisqu’on utilise le modèle du gaz parfait , 
on peut alors écrire la loi de Laplace qui 
s’écrit 
1 1 2 2PV PV . 
2. On exploite la loi de Lapla ce mais pour le 
couple de variables Température, Pression ce 
qui donne
11
1 1 2 2P T P T     , on obtient donc 
1 1
1
21
2
411PT T K P
 
 

 
3. (Voir schéma ci contre) 
 
4. Lors de l’étape d’admission  (I),  la transformation est réversible et s’effectue à pression du gaz 
constante égale à P1, le volume dans le cylindre passe de 0 à V1, on en déduit que le travail du piston sur 
le gaz est 
11IW PV  De même lors de l’échappement : 
22IIIW PV  
5. La transformation est adi abatique, le transfert thermique reçu par le système est donc nul. Le premier 
principe appliqué au gaz qui est alors un système fermé donne 
21 IIU U W . 
On écrit alors pour le gaz parfait 
 2 1 2 1
1
nRU U T T      Les LGP donnent 
1 1 1nRT PV  ; 
2 2 2nRT PV  
Ce qui donne finalement 
2 2 1 1
1
II
PV PVW 
  . 
6. On visualise le travail reçu par le gaz de la part du piston au cours d’une transformation comme l’aire 
sous la courbe associée si on observe une compression et l’oppopsé de  l’aire sous la courbe si on 
observe une détente. A partir de ces deux observations, on peut en déduire que le travail reçu par le gaz 
de la part du piston est l’aire délimitée par le cycle hachuré sur le diagramme de la q3.  
7. On obtient le travail total reç u par le piston sur un cycle par la somme des travaux sur chaque étape ce 
qui donne 
1 1 2 2 2 1Piston I II IIIW W W W PV PV U U        
Avec la définition de l’enthalpie
H U PV , on obtient 
21PistonW H H  
8. On reprend la relation de la q7 et on l’adapte au trava il par unité de masse ce qui donne 
    
1 1
11
2 1 2 1
2
111
RT PRw h h T T M M P


       
 A.N : 
511,1.10 .w J kg   
 
 
 
V 
P 
P2 
P1 
V1 V2 
Compression (II) 
P=C/Vγ 
Admission (I) 
P=P1 
Refoulement (III) 
P=P2

--- Page 4 ---

DS7 PCSI2 2022-2023 
Physique 
4/5 
Problème 4 : stockage du CO2. 
a. Exploitation du diagramme (P,T). 
1. Voir diagramme. 
2. Le point (c) est le point triple du dioxyde de 
carbone, il donne les conditions de 
température et de pression nécessaire pour 
observer un état d’équilibre où les trois 
phases solide, liquide et gaz sont réunies. 
Le point (d) est le point critique qui marque la fin de 
la courbe des équilibre liquide vapeur. Au -delà de 
cette limite, on obse rve plus réellement de transition 
de phase à deux états liquide -gaz mais un fluide dont 
le volume massique évolue de manière continue 
lorsque la température et la pression sont modifiées. 
3. On trace sur le diagramme (voir annexe) l’isotherme T O=280K (placé à 2,9cm sur l’échelle horizontale 
en exploitant l’échelle linéaire) , on observe qu’elle coupe la courbe des équilibres liquide -gaz, on peut 
donc envisager une transition vapeur→liquide à cette température. 
On reporte alors l’intersection de la courbe des équilibres avec l’isotherme sur l’axe des ordonnées pour lire la 
pression de vapeur saturante (voir annexe). On lit alors l’échelle logarithmique pour obtenir 
4
()log2,8 1
106,9 log 1
Sat OPT
  
Ce qui donne 
2,84* 16,9( ) 10 4, 2.10Sat OP T bar  
4. On observe que le CO2 réalise la transition liquide-solide au point (a) du diagramme ce qui permet d’en 
conclure directement que la pression à laquelle la solidification a lieu à la température de 280K  est 
donné par l’énoncé à 
34.10aP bar  
5. On exploite les données fournies pour obtenir 
 min mina O OP P z P gz      
ce qui donne
min 39,6aO
O
PPz km g
 , cette profondeur n’est pas atteignable puisque la fosse des Mariannes, le 
point le plus profond recensé dans les océans est situé à 11km de profondeur. La technique est donc inapplicable 
et en un sens on pourrait dire tant mieux !! 
b. Exploitation du diagramme (P,v). 
6. (Voir diagramme) 
7. (Voir diagramme) 
8. A la température de 280K, on observe bien le plateau de transition de phase liquide -vapeur, il est situé 
sur le diagrmme (P,v) à une pression de v apeur saturante P sat(TO)=42bar tout à fait cohérente avec la 
valeur trouvée dans la première partie. Les diagrammes (P,v) et (P,T) sont cohérents. 
9. Pour T=295K, on lit dans le tableau un volume massique en phase gaz de 4,7.10 -3m3.kg-1 permettant de 
placer l e point G sur la courbe de rosée ainsi qu’un volume massique de la phase liquide de 1,3.10 -
3m3.kg-1 permettant de placer le point L sur la courbe d’ébullition. On trace alors le plateau de la 
transition de phase liquide -gaz. On trace alors une isotherme da ns le liquide de forte pente et une 
isotherme dans le gaz de faible pente en marquant les passages de la courbe de saturation par une 
rupture nette de pente (voir diagramme). 
10. On applique le modèle de gaz parfait au CO 2 : 
sat G
RTPv M  avec T=295K , P Sat=60bar lu sur le 
diagramme ce qui donne 
3 3 19,3.10G
sat
RTv m kgMP
  la valeur tabulée est de 4,7.10 -3m3.kg-1 ce qui 
est quasiment la moitié du volume estimé avec le modèle de gaz parfait qui ne s’applique évidemment 
pas pour la phase vapeur saturante dans ces conditions. 
11. (Voir diagramme). 
On calcule les volume massique suivant 
2 3 11,5.10Iv m kg   et 
3 3 13.10II IIIv v m kg   
Dans l’état (I) le CO 2 es ten phase gaz, dans l’état (II) il présente un état d’équilibre liquide -gaz, et dans l’état 
(III) il est en phase fluide supercritique pusiqu’il est situé au dessus du point critique. 
12. On connait le volume du système V=54L et la masse du système m=18kg. Grâce au tableau les volumes 
massiques des phases liquide et vapeur saturants 
3 3 11,1.10Lv m kg   et 
3 3 18,1.10Gv m kg   
On  exploite alors l’extensivité du volume pour écrire 
L L G GV m v m v  et on écrit aussi 
LGm m m

--- Page 5 ---

DS7 PCSI2 2022-2023 
Physique 
5/5 
On résout le système d’équations ainsi établi et on obtient : 
13G II
L
GL
vvm m kg vv
   et 
5II L
G
GL
vvm m kg vv
   
13. L’ennthalpie est également extensive, on en déduit 
()II L L G GH m h m h  et à l’aide du tableau de 
données thermodynamiques fourni on obtient : 
3
() 4,88.10IIH kJ  
On en déduit l’énergie interne du système 
3
( ) ( ) ( ) ( ) 4,65.10II II II IIU H P V kJ    
14. Pour le GP, l’équation d’état est 
GP
RTPv M  ce qui correspond à négliger l’influence des paramètres a 
et b, alors l’énergie interne massique s’exprime
GP V Ou c T u  en négligeant l’influence de a. 
15. L’enthalpie du système s’écrit dans l’état (I) qui est  un gaz sous la forme suivante pour les deux 
modèles 
( ) ( )IIU mu   
 
 
3
( ), ( ) 7,5.10I GP V I OU m c T u kJ    et 
3
( ), ( ) 7, 27.10I VdW V I O
I
aU m c T u kJ v
   
  
On obtient un écart de 3% entre les deux valeurs estimées ce qui reste acceptable. 
 De même 
3
( ), 7,85.10III GPU kJ   et 
3
( ), 6,72.10III VdWU kJ   
Cette fois, on obtient un écart bien plus important de l’ordre de 15% qui est cette fois-ci très important. C’est 
assez logique puisque le fluide est alors en état supercritique. 
16. On effectue un bilan énergétique sur la transformation (II) vers (III) qui est isochore, on obtient alors 
par le premier principe : 
( ) ( ) ( ) ( )III II II IIIUUQ   ce qui donne avec le résultat de la question 13. et la 
valeur obtenue par le gaz de Van der Waals en question 15. 
3
( ) ( ) 2,07.10II IIIQ kJ 