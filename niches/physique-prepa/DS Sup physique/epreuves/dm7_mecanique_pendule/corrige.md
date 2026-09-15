# corrigé du DM7 mécanique pendule


--- Page 1 ---

Corrigé DM7 PCSI2 2022-2023 
physique 
1/4 
Problème 1 : Récupération de l’énergie des vagues. 
a. Etude du pendule simple. 
 
1. On étudie le pendule dans le référentiel terrestre R supposé galiléen et attaché 
au repère (O, x, y , z). 
On se place dans la base cylindropolaire 
 yr eee  ,,  . 
Bilan des forces  : Le poids 
gmP 
  ; La poussée d’Archimède supposée 
négligeable ; La réaction de la tige 
T
 . 
Etude cinétique : 
reLOM   ; 
 eLv RM
 ./   ; 
 eLeLa rRM
 ..2
/   
On applique la loi de la quantité de mouvement dans le référentiel R galiléen : 
TPdt
pd
R
RM 




 /
 
2. On détermine l’équation du mouvement en projetant la loi de la quantité de mouvement selon 
e  : 
 sinmgmL 
  
ce qui donne pour équation du mouvement 
0sin2   O
  avec 
L
g
O  . 
3. On projette la loi de la quantité de mouvement selon 
re  ce qui donne : 
rTmgmL   cos2  
Finalement : 
 
2 cosr r rT T e m L g e   
  
b. Etude du système de conversion. 
4. Le bilan des forces devient : Le poids 
gmP 
  ; La réaction de la tige 
T
  ;  
la force de frottement linéaire : 
RMvf /

  ; force d’inertie d’entrainement : 
Oie amF 
 . 
5. Selon 
e  : 
 sinmgP   ; 
0T  ; 

Lf   ; 
    
2
, cos cos sin sinieF m a t t       
6. On projette la LQM selon 
e  pour obtenir : 
 
     sinsincoscossin 2 ttamLmgmL    
7. A l’ordre 1, les développements limités des fonctions sont : 
  osin  ; 
  o1cos  
8. On linéarise l’équation en fonction de θ ce qui donne  : 
     ttamLmgmL sincos2  
 
L’équation donne sous forme canonique : 
     ttL
a
Q
O
O sincos22    
Avec : 
L
g
O   et
L
gmQ   
Dans le second membre  de l’équation, on a alors deux termes sinusoïdaux d’amplitude  : 
2L
a  pour le premier 
et 
 2
L
a  pour le second. Dans la recherche d’une réponse au petit angle, on peut commencer par négliger ce 
second terme et on obtient alors la forme proposée sur l’énoncé. 
9. On obtient l’amplitude complexe en traduisant l’équation du mouvement  en notation complexe ce qui 
donne : 
 tjL
a
Qj O
O  exp222   avec 
 tjt O  exp)(   
On obtient finalement : 
22
2
O
O
O
Qj
L
a




  On en déduit : 
22
3
O
O
OO
Qj
L
aj
j




  
O 
M θ 
x 
z 
P

 
re  
e
 
T


--- Page 2 ---

Corrigé DM7 PCSI2 2022-2023 
physique 
2/4 
L’amplitude réelle est donnée par le module de cette expression : 
  22
2
222
3
1 


OO
O
Q
L
a

  
10. La puissance de la force de frottement s’exprime : 
2
//. RMRM vvfP 
  
La puissance est une grandeur quadratique de la vitesse, cette  dernière est une grandeur sinusoïdale, on en déduit 
que sa valeur moyenne s’exprime  : 
221
2
OL
  et on obtient bien après calcul que la puissance moyenne 
convertie en électricité s’exprime
 
26
22 2 2 2
2
1
2
1
O
OO
amQP
Q

   

  
11. Pour une valeur fixe de la pul sation ω, la puissance électrique moyenne produite est maximale lorsque la 
fonction
  222222
)(
 OO x
xxf

  est maximale. 
En dérivant par rapport à x on obtient : 
    
2222222
222
222222
21


 OO
O
OO x
x
xdx
df



  
Un extremum est obtenu lorsque 
0dx
df  c’est dire lorsque :  
  02 222222222   OOO xx
 qui présente une racine positive : 
 


O
Ox
22   
En supposant que cet extremum est un maximum, on obtient alors que la puissance extraite est maximale 
lorsque : 
 


O
Ox
22   c’est-à-dire lorsque
22 



O
OQ . 
 
Problème 2 : A propos des pendules. 
 
Etude dynamique d’un pendule simple. 
1. La base de projection adaptée est la base cylindro -
polaire 
 yr eee  ,,  . 
Bilan des forces : 
Le poids 
gmP 
  
La réaction de la tige rigide : 
T
  
Etude cinématique : 
relOM 
 ; 
 elv RM
 ./   ; 
221
2
CE ml 
  
 
2. La force de gravité est conservative associée à l’énergie potentielle  
, cosPgE mgz mgl  
 (car 
(Oz) est orienté verticalement vers le bas.  
La tension du fil est non conservative mais elle ne travaille pas car elle est constamment orientée 
perpendiculairement au déplacement du point matériel. 
On en déduit que la seule force qui travaille sur le point mat ériel est conservative et que le système est par 
conséquent conservatif. L’énergie mécanique est donc une grandeur conservée, un intégrale première du 
mouvement. 
L’énergie mécanique s’écrit
221 cos2
M C PE E E ml mgl    
  
Elle est conservée et donc 
0MdE
dt   ce qui donne 
sin 0ml mg  
  
D’où l’équation du mouvement du pendule simple : 
0sin   l
g  
O 
M θ 
x 
z 
P

 
re  
e
 
T


--- Page 3 ---

Corrigé DM7 PCSI2 2022-2023 
physique 
3/4 
3. On pose θ=0+δθ ; alors 
    et 
 sin  ; l’équation du mouvement est alors : 
0  l
g  
On obtient l’équation du mouvement de l’oscillateur harmonique de pulsation propre 
l
g
O  , la période d es 
petites oscillations autour de la position θO =0 sera alors : 
g
lTO 2  
4. On écrit tout d’abord la relation pour la nouvelle gravité et la nouvelle période  : 
2OO
lTT gg  
 qu’on réécrit : 
11
22
1 2 1 1O
OO
O
T l g gTT T g g g
 

                 
Par un DL1 on obtient : 
1
2 111 2
gg
gg


   ce qui mène bien à 
g
g
T
T
O
O 
2
1  
Etude énergétique d’un pendule de Holweck-Lejay. 
5. La vitesse du point A s’exprime de la même manière que pour le pendule simple.  
L’énergie cinétique est définie par : 
2
/
2
1
RMC vmE   ce qui donne ici : 
22
2
1 mlEC   
6. Bilan des forces :  
 
Le poids : 
gmP 
   
La réaction de la tige rigide : 
T
  ;  
la force de rappel modélisant le couple  exercé par le 
ressort spirale : 
 el
CF 
.  
 
7. La force de gravité est une force conservative associée à l’énergie potentielle  : 
cstemgzE gP ,  où z 
est l’altitude du point A ce qui donne ici : 
cstemglE gP  cos,   
Etudions alors le travail élémentaire de la force de rappel : 
  eldel
COMdFW 
....   
On obtient donc pour cette force de rappel 
 elpEdcsteCdW ,
2
2
1 



    
L’énergie potentielle totale pour le point matériel A s’exprime alors : 
csteCmglE p  2
2
1cos   
La référence 
0)0( pE permet alors d’obtenir : 
mglcste  Et finalement : 
  2
2
11cos  CmglE p   
La seule force restante dans le bilan est la réaction exercée par la barre sur le point A qui est par nature radiale 
alors que le mouvement de A est orthoradial. On en déduit que cette force ne travaille pas. 
On observe donc que seules les forces conservatives travaillent sur le point matériel A, le système est donc 
conservatif. 
8. Les positions d’équilibre sont des extréma de l’énergie potentielle vue comme une fonction du 
paramètre spatial θ : 
  0eq
P
d
dE   
Ici, on détermine : 
 Cmgld
dE P  sin . On peut évaluer la valeur prise en θO=0 ; soit : 
  0O
P
d
dE   
On conclut effectivement que la position θ O=0 est une position d’équilibre pour le pendule de Holweck -
Leiay. 
O 
M 
θ 
x 
z 
P

 
re
 
e
 
T
  
F


--- Page 4 ---

Corrigé DM7 PCSI2 2022-2023 
physique 
4/4 
De plus, une position d’équilibre est stable si : 
  02
2
eq
P
d
Ed  . On obtient ici : 
Cmgl
d
Ed P  
cos2
2 .  
On peut évaluer la valeur prise en θO=0 ; soit : 
  Cmgl
d
Ed
O
P  2
2  
La condition d’équilibre stable en θO=0 se traduit donc par la condition 
0 mglC  ou 
1mgl
C  
9. Le système est conservatif, l’énergie mécanique est donc une intégrale première du mouvement. On 
peut alors trouver l’équation du mouvement par la relation : 
0dt
dE M  
L’énergie mécanique s’exprime : 
  222
2
11cos2
1  CmglmlEEE PCM    
On obtient alors pour équation du mouvement : 
0sin 2  
ml
C
l
g  
10. On pose : θ=0+δθ ; alors 
    et 
 sin  ;  
L’équation du mouvement est alors : 
02 



   l
g
ml
C  
On obtient l’équation du mouvement de l’oscillateur harmonique de pulsation propre 
l
gml
C 
 , la 
période des petites oscillations autour de la position θO sera alors : 
gB
lT  2  avec 
ml
CB  
11. On applique la même méthode qu’en question 4 : 
gB
g
T
T
 
2
1  
12. La différence essentielle entre les deux formules est la présence du facteur B pour le pendule de 
Holweck-Leiay. En choisissant convenable la raideur C du ressort spiral, on peut prendre B proche de g 
tout en s’assurant que (B -g) reste positif. On peut alors accroire significativement la sensibilité du 
système. On pourra donc rendr e, en adaptant bien les caractéristiques du matériel choisi, le pendule de 
Holweck-Lejay beaucoup plus sensibles aux variations de g que le pendule simple.