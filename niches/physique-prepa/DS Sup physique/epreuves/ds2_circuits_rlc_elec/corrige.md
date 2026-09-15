# corrigé du DS2 circuits RLC elec


--- Page 1 ---

Corrigé DS2 PCSI2 2022-2023 
physique 
1/4 
Exercice d’application directe du cours : RLC parallèle. 
 
1. Le condensateur est chargé avec une tension UO 
sur l’intervalle t< 0. Par continuité de la tension 
aux bornes d ’un condensateur, on en déduit que 
   00 Ou t u t U   
 
Le courant dans la bobine est nul sur l ’intervalle t<0. Par 
continuité de l’intensité traversant une bobine, on en déduit 
que iL(t=0+)=0. Le courant dans la résistance soumise à une 
tension UO présente une intensité iR(t=0+)=UO/R et par la loi 
des nœuds on obtient alors 
 0 O
C
Uit R
   
2. On écrit la seule loi de structure ici, c’est la loi des nœuds
      0C R Li t i t i t    
Relations caractéristiques des composants 
   C
dui t C t dt  ; 
   Ru t Ri t  ; 
   Ldiu t L t dt  
On exploite alors la loi des nœuds pour obtenir : 
2
2
11 0d u du udt RC dt LC    
Soit l’ED 
2
2
2 0O
O
d u du udt Q dt
     par identification 
1O
Q RC
   et 
2 1
O
LC   d’où 
1
O
LC
 
CQR L  
3. Pour observer un régime critique, il faut que le facteur de qualité soit égal à ½ ce qui donne une 
expression de la résistance correspondante 
1
2
C
LR C  
4. Dans le cas du régime critique, pour un facteur de qualité de ½, on obtient une racine double pour le 
polynôme caractéristique 
22 20 OOrr     soit 
dOr   ce qui donne la solution générale de 
l’équation étudiée dont on observe qu’elle est homogène sous la forme : 
     expHOS t At B t     
Les conditions initiales donnent alors pour la tension 
 ( 0) 0 HOu t S t B U      
        exp expH
O O O
dS t A t At B tdt        
  
d’où 
   10 0 2 OH
O C O O
UdS t A B i t Udt C RC         
On obtient donc 
OBU  et 
OOAU   et finalement 
     1 expO O Ou t U t t     
 
Problème 1 : étude d’une photodiode. 
1. La photodiode est étudiée en convention récepteur. 
2. En exploitant la courbe correspondant à 8mW pour une tension de 0,5V, on lit  l’intensité I1≈-3,0mA.  
La puissance électrique s’exprime 
1 1 1 1,5P U I mW   
3. En exploitant la courbe correspondant à 6mW pour une tension de -1,0V, on lit l’intensité I2≈-2,4mA.  
La puissance électrique s’exprime 
2 2 2 2, 4P U I mW  
4. Dans le cas étudié question 2 , la puisance reçue est négative, la photodiode fournit donc de la 
puissance, elle se comporte en générateur. 
Dans le cas étudié question 3 , la puisance reçue est positive, la photodiode reçoit donc de la puissance, elle se 
comporte en récepteur. 
5. A l’aide des 6 courbes proposées sur la figure 2, on peut construire le tableau suivant : 
 
W (mW) 0 2 4 6 8 10 
I (mA) 0 -0,8 -1,6 -2,4 -3,2 -4,0 
 
On obtient alors la courbe cicontre pour la représentation graphique de I=f(W). 
Bien qu’on n’ ai pas représenté tous les ou tils permettant une étude appro fondie, une analyse qualitative de 
l’alignement des points montrent une tendance linéaire pour l’évolution de l’intensité du courant électrique 
inverse en fonction de la puissance lumineuse reçue.

--- Page 2 ---

Corrigé DS2 PCSI2 2022-2023 
physique 
2/4 
 
6.          
 
 
 
7. L’équation caractéristique du générateur 
dans le modèle  de Thévenin étudié ici 
s’écrit 
U E rI   
8. On reprend la courbe utile, à savoir la plus basse.  
On ajoute la droite correspondant à la caractéristique du générateur de Thévenin de pente -1/r ce qui donne pour 
l’application numérique -5mA/V passant par le point  limite donné soit une puissance luminseuse de 10mW, une 
tension de -0,5V ce qui donne une intensité de –4mA. On lit alors la force électromotrice correspondante à 
l’intersection de la caractéristique et de l’axe des abscisses ce qui donne Emax=-1,5V. 
Par le calcul, on impose le point de coordonnées (U=-0,5V, I=-4mA) et on utilise l’équation caractéristique du 
générateur de Thévenin ce qui donne 
1,5E U rI V    
 
9. Il faut placer l’ampèremètre en série avec la 
photodiode et le voltmètre en parallèle. 
 
10. Dans le cas idéal, le voltmètre est de 
résistance infini, et l’ampèremètre est de 
résistance nulle. 
Dans le cas réel, le voltmètre présente une résistance 
de l’ordre de 10MΩ (donc «  très grande  ») et 
l’ampèremètre présente une résistance de l’ordre de 
1Ω (donc « très petite »). 
Dans la proposition faite , le montage est dit «  courte 
dérivation », pour laquelle on mesure bien la tension 
aux bornes de la diode mais on mesure le courant 
passant dans l’associa tion parallèle de la diode et du 
voltmètre. On pourra avoir un biais dans la mesure 
de l’intensité avec ce montage. 
E 
r I 
U 
A 
V 
E 
r 
I 
U

--- Page 3 ---

Corrigé DS2 PCSI2 2022-2023 
physique 
3/4 
 Problème 2 : Thermistances et montages thermométriques. 
Etude du montage simple : 
1. La relation du diviseur de tension donne ici : 
1
()
()
RS
S
RTVe R T R R   
2. La variation s’exprime : 
11
( ) ( )( ) ( ) . ( ) ( )
OO
R R O R O S
O S O S
R T R R TV V T T V T e R T R R R R T R R
 
             
Ce qui donne après calcul : 
 
  
1
11
.( ) ( )
S
RS
O S O S
R R RVe R T R R R R T R R
 
        
En tenant compte de la faiblesse de δR en comparaison des autres résistances : 
 
 
1
2
1
.
()
S
RS
OS
R R RVe
R T R R

 
  
3. La variation de tension observée prend la valeur : 
2
1 6.10VV   
L’incertitude sur les lectures de tension pour ce calibre du voltmètre s’évalue alors à 
 
32
1 2,3*10 3.10uV   
lorsqu’on traduit la phrase (0,1%+3digits) ce qui donne 
 
2
1 3.10u V V  . 
La différence de tension à étudier est de l’ordre de l’incertitude sur la valeur affichée par le voltmètre. Dans ces 
conditions, on ne pourra évidemment pas d’étudier précisément la variation de la tension. 
Etude du pont de Wheatstone : 
4. On décompose la tension UAB par la relation : 
AD DBU U U  
Par la relation du diviseur de tension, applicable car aucun courant ne circule dans la branche AB, on obtient les 
expressions : 
SAD eRTR
TRU
1)(
)(
  et 
DBSBD UeRR
RU 
34
4  
On obtient finalement pour expression de la tension demandée : 
  
3 1 4
1 4 3
( ).
()
S
R T R R RUe R T R R R
   
5. L’équilibre du pont est réalisé si la tension U est nulle ce qui donne comme relation entre les résistances  : 
0).( 413  RRRTR
 
6. On exprime la tension : 
 
  
3 1 4
1 4 3
( ) .
( ) ( ) 0
()
eq
eq eq S
eq
R T R R R R
U U T T U T e
R T R R R R
 

    
    
Après développement et utilisation de la relation d’équilibre du pont : 
  
3
1 4 3()
S
eq
RRUe
R T R R R R
 

    
On peut alors simplifier en supposant δR petite devant les autres résistances 
  
3
1 4 3()
S
eq
RRUe
R T R R R
 
  
7. Le pont de Wheatstone permet de partir d’une valeur nulle de la tension et permettra donc de régler le 
Voltmètre sur un calibre adapté à la mesure de δU , on règle ainsi le problème qu’on obser vait dans le 
montage utilisant une simple configuration diviseur de tension. 
Problème 3 : Diode de roue libre. 
1. Lorsque l’interrupteur est ouvert la tension aux bornes de la diode est directement imposée par la source de 
tension idéale et elle s’exprime UD=-E. On en déduit que U D<0 ce qui implique que la diode est dans l’état 
bloqué et qu’elle est équivalente à un interrupteur ouvert. 
2. En régime stationnaire, une bobine est équivalente à un fil. 
3. Le circuit correspond à la source de tension idéale de fem E alimentant directement le conducteur ohmique 
de résistance R. On obtient alors
 0L
Eit R  
4. L’énergie stockée dans la bobine s’exprime 
 
2
211 022
LL
EE Li t L R
      A.N : 
250LEJ  
5. Par continuité de l’intensité traversant une bobine, on peut affirmer que
 0L
Eit R
  
Puisque l’interrupteur est ouvert, on observe que iD=iL et que cette intensité est donc positive.

--- Page 4 ---

Corrigé DS2 PCSI2 2022-2023 
physique 
4/4 
 
 
 
6. On écrit la loi d’Ohm pour le conducteur ohmique en convention 
générateur
LU Ri  
On écrit la loi de comportement de la bobine
LdiUL dt  
En réunissant ces deux relations, on obtient 
0L
L
diL Ridt   
On obtient bien 
1 0L
L
di idt    
Où par identification 
L
R   A.N : 
35,0.10 s    
7. La solution générale de cette équation différentielle homogène s’écrit 
  expH
tS t A 
   
Il n’y a pas de second membre, on applique donc directement les conditions initiales 
 0L
Ei t A R    
On obtient finalement 
  expL
Etit R 
  , ce qui donne bien une intensité positive sur l’intervalle (t>0). 
8. Pour la courbe on obtient l’ allure ci des sous 
pour E/R=1kA et τ=5ms. 
 
9. On observe à nouveau que la diode est passante 
après que l’interrupteur K soit ouvert. Le 
circuit équivalent est alors le suivant : 
 
10. On écrit la loi des mailles : 
0S r R Lu U U U     
La loi d’Ohm donne : 
r d LU r i  et 
RLU Ri  ; Pour la bobine : 
L
L
diUL dt  
On obtient alors : 
 L
d L S
diL r R i udt     
Sous forme canonique, on obtient : 
 
1 SL
L
d d d
udi idt r R   Avec par indentification
d
d
L
rR    
11. La SGEH s’écrit 
  expHd
d
tS t A 
 
 , la SPEC s’écrit 
S
P
d
uS rR  ,  
la SGEC s’écrit donc 
expS
Gd
dd
u tSA rR 
      
On applique les conditions initiales 
 0 S
Ld
d
uEi t A R r R      d’où 
  expSS
L
d d d
uu Etit r R R r R 
                
12. La diode reste passant tant que l’intensité du courant reste positive, on peut donc déterminer l’instant t b à 
partir duquel la diode repasse en mode bloquée par 
  0Lbit   ce qui donne 
 ln 1 d
bd
S
r R Et Ru  
  
R 
iL 
UL 
UR 
L uS 
rd Ur 
R 
iL 
U 
L