# corrigé du concours blanc


--- Page 1 ---

Concours blanc  PCSI1 et PCSI2 2021-2022 
Physique  Février 2022 
1/8 
Partie 1 : Utilisation en capteur de forces. 
Les montages ci -après utilisent des amplificateurs linéaires intégrés (ALI) supposés idéaux et fonctionnant en 
régime linéaire. 
a. Mesure de l’intensité de la force exercée sur une lame piézoélectrique.  
1. Pour un ALI idéal, on considère que l’impédance d’entrée est infinie et que les courants i + et i- entrant 
dans les bornes inverseuse (-) et non inverseuse (+) sont nuls : i+=i-=0. 
L’impédance de sortie de l’ALI est quasi -nulle mais le courant de sortie ne peut pas d épasser une valeur appelée 
intensité de saturation usat≈25mA. 
On peut supposer qu’un ALI fonctionne en régime linéaire lorsqu’il y a une boucle de rétroaction sur l’entrée 
inverseuse (-). Pour un ALI idéal, les potentiels des bornes d’entrée sont égaux : V+=V-. 
2. Puisqu’il n’y a pas de courant dans la résistance R1, car i+=0 : Ve=V+. 
On peut faire l’hypothèse d’un régime linéaire : V+=V-. 
On peut alors faire un pont diviseur de tension en (-) : 
1
23
0 SVV Ve
RR
   On obtient : 
3 2 1
23
S
e
R V R eV RR   
3. On obtient 
19,5.10eVV  . 
4. On exploite la relation de l’énoncé
.. eq C V K F  pour obtenir
1. 7,6.10eCVFN K
 . 
b. Mesure de la fréquence d’une force excitatrice sinusoïdale s’exerçant sur la lame. 
 
5. A basse fréquence, un condensateur est 
équivalent à un coupe circuit. 
Le circuit est alors celui ci -contre et on observe que 
le filtre coupe les BF. 
  
A haute fréquence , un condensateur est 
équivalent à fil. Le circuit est alors celui ci-contre et 
on observe que le filtre coupe les HF. 
Le filtre est donc un passe bande comme le confirme la forme proposée dans la question suivante.  
6. On exploite le fonctionnement linéaire : V+=V-. On constate que V+=0. 
On écrit une loi des nœuds en terme de potentiel en (-) : 
2
1
12
0 11
e S SV V V V V V
RR jC jC
      
  
Puisque V-=0, on obtient : 
2
2
1
1
10 1
e
S
V V jC RR jC


   
   
puis 
 
12
12
1
11
S
e
VHj V R jC jC R


         d’où 
 
12
12
2 1 2 1
1
1
Hj
RC jR CR C jR C


     
On obtient alors : 
 
   
21
1 1 2 2
21 2 1 2
11 1 2 2 1 1 2 2
1 11
RC
R C R C AHj
R R C C jj R C R C R C R C

 
            
Par identification on obtient : 
21
1 1 2 2
RCA R C R C   ; 
1 1 2 2
1
1 2 1 2
R C R C
R R C C   ; 
2
1 1 2 2
1
R C R C    
7. Le gain s’exprime : 
   
2
2
1
1
AG H j





--- Page 2 ---

Concours blanc  PCSI1 et PCSI2 2021-2022 
Physique  Février 2022 
2/8 
qui passe par un maximum lorsque le dénominateur passe par un minimum ce qui correspond à annuler le facteur  
2
1
0O
O
 

 

 ce qui amène à l’expression 
12O   
8. La phase s’exprime : 
    
2
1
arg arctanHj     
    
  qui prend bien la valeur π en ωO. 
9. On vérifie expérimentalement que deux 
signaux sont en phase en utilisant un 
oscilloscope. On connecte le signal V e(t) 
sur la voie (CH1), le signal V S(t) sur la 
voie (CH2) et on passe en mode (XY). 
Les signaux connectés sont alors en opposition de 
phase si la  courbe observée sur l’écran se réduit  à 
un segment de pente négative. 
10. Lorsque la résistance R 1 est réglée pour que V e et Vs soient en opposition de phase, la pulsation ω=2πf 
de la force excitatrice s’identifie avec la pulsation ωO. 
On obtient alors : 
12 2
1 2 1 2
1 3,2.1022 2
Of Hz
R R C C

 
     
Partie 2 : Utilisation dans un airbag. 
a. Principe d’un accéléromètre. 
On considère une masse m susceptible de se déplacer par rapport à  une voiture qui subit tout au long de l’étude 
une accélération constante égale à 
xa ae
 par rapport au référentiel terrestre supposé galiléen. 
 
La masse m se déplace horizontalement et sans frottement solide sur un support lié à la voiture. Le ressort a une 
constante de raideur k et une longueur à vide L O. L’amortisseur exerce une force de frottement fluide sur la 
masse m, son expression est donnée 
gfv 
  où 
g g xv v u
 est la vitesse de glissement de l a masse sur le 
cadre lié à la voiture. Le vecteur unitaire de l’axe des x, orienté dans le sens des x positifs, est noté 
xu
 . 
Toute l’étude se fait dans le référentiel terrestre supposé galiléen. 
11. D’après le schéma, le ressort connecte A  d’abscisse x A(t) et la masse d’abscisse x(t) 
d’où
( ) ( ) ( ) aL t x t x t  
La vitesse de glissement est la vitesse relative de la masse par rapport au cadre et donc par rapport au point A, on 
en déduit que 
( ) ( ) ( ) ( )gav t x t x t L t  
  
On dérive l’expression préc édente pour obtenir  : 
( ) ( ) ( ) aL t x t x t
 ce qui donne 
( ) ( )L t x t a
  car 
l’accélération de A est celle de la voiture c’est-à-dire 
xa ae
  d’où 
axa
 . 
12. Les forces qui agissent sur la masse sont : 
 Le poids 
zP mg mge 
  où 
ze
  est vertical vers le haut. 
 La réaction du cadre sur la masse pour laquelle on néglige les frottements solide et qui ne comportent 
donc pas de composante tangentielle : 
zR Ne
  
 La force d’amortissement 
()gxf v L t e 
  
 La force de rappel élastique : 
 ()el O xF k L t L e 
  
On applique alors la seconde loi de Newton pour un système de masse constante 
 
/
/
MR
M R el
R
dp ma P R f Fdt
     
  en projection sur 
xe
  
 ( ) ( ) Omx L t k L t L  
  
On introduit alors 
( ) ( )x t L t a
  et on obtient l’équa diff de l’énoncé : 
OmL L kL kL ma   
 .

--- Page 3 ---

Concours blanc  PCSI1 et PCSI2 2021-2022 
Physique  Février 2022 
3/8 
13. On introduit X(t) et on obtient bien : 
2
2
2
O
O
d X dX Xadt Q dt
      
Avec par identification : 
O
Qm
   et 
2
O
k
m   d’où  
O
k
m  et 
1 mk . 
14. En régime stationnaire, la solution de l’équation précédente est : 
2O
O
aX  . 
15. Lorsque le facteur de qualité est de valeur 1/2, on observe un régime critique. 
On pose l’équation caractéristique e t on détermine le discriminant qui est ici nul. On obtient alors une racine 
double qui s’exprime 
Or  , la forme générale de l’équation homogène s’écrit alors
 () Ot
HS t At B e  . 
Le temps caractéristique τ du régime transitoire est alors le temps caractéristique de décroissante de 
l’exponentielle ce qui donne : 
1
O
   
16. Avant le freinage X(t<0) est nulle puisque 
le ressort est non étiré avant le freinage. 
Puisque tO est supposé grand devant τ 
 OOX t X   
17. Sur l’intervalle [tO, 2t O], la voiture est 
arrêtée donc l’accélération est nulle, on 
observe un régime transitoire de retour au 
repos sur une durée τ et on a atteint le 
retour complet à l’équilibre en t=2t O. On 
en déduit que 
 20OXt  . 18. 
b. Utilisation du matériau piézoélectrique. 
19. On calcule l’accélération moyenne par : 
12
1 1,0.10Va ms t
  
20. On calcule l’accélération moyenne par : 
22
2 1,7.10Va ms t
  
21. On utilise la relation de l’énoncé : 
2
11 2,8.10F ma N   et
1
22 4,7.10F ma N  . 
Puis à nouveau d’après l’énoncé : 
1
11 1,7.10V F V   et 
22 2,8V F V  
La différence est tout à fait décelable, il sera facile de distinguer le freinage d’urgence décrit d’un choc.  
22. Le choix d’un facteur de qualité Q=1 /2 nous assure d’avoir un temps de réponse minimal du système 
électronique de détection du choc. Il est important d’avoir optimiser ce temps de réponse pour que le 
système atteigne le régime stationnaire rapidement et que la tension atteigne bien la valeur  attendue 
proportionnelle à a donné par : 
V ma . 
Si ce n’était pas le cas, la tension mesurée serait dépendante de l’accélération a et du temps de réponse du circuit 
rendant la détection de choc de durée très courte beaucoup plus aléatoire. 
Partie 3 : microgénérateur piézoélectrique. 
23. On traduit l’équation différentielle pour la cote réelle z(t) en une équation algébrique pour le signal 
complexe Z(t) pour obtenir : 
   
2 2 jtOO
O
Fj Z j Z Z e Qm
      
On obtient alors : 
22
O
m
O
O
FZ
mj Q

    
On en déduit : 
 
 
2
222
O
mm
O
O
FZZ
m Q


   
Et
 
 
22
22
arctan
arctan
O
O
O
z
O
O
O
si
Q
si
Q
 


   

 
              
24. A la pulsation propre, on obtient donc : 
  2
O
mO
O
QFZ m   et 
2
z
 

--- Page 4 ---

Concours blanc  PCSI1 et PCSI2 2021-2022 
Physique  Février 2022 
4/8 
On en déduit que : 
 22( ) cos sin 2
OO
OO
OO
QF QFz t t t mm

     et 
 ( ) cos O
ZO
O
QFv t t m   
25. La capacité C O modélise l’aspect ca pacitif de l’élément piézoélectrique comme il est décrit dans ce 
problème depuis la première partie. 
Le facteur β est appelé facteur de force, c’est le rapport de la tension aux bornes de la lame piézoélectrique par la 
force appliquée sur celle-ci. 
26. Si on suppose que β est le rapport d’une tension divisée par une force, on obtient :
    FU   
On sait que 
UI est la puissance reçue par un dipôle électrique alors que 
/MRFv est la puissance mécanique d’une 
force sur un point matériel : on en déduit que 
     U I F v  et donc que 
      U I U v   
Ce qui donne bien 
    Iv   le produit βvZ est alors bien homogène à une intensité électrique. 
27. On se place en notation complexe et on associe  à la vitesse v z(t) une vitesse complexe vz(t) telle que 
vz(t)=Re(vz(t)). 
On étudie alors l’association en // de CO et R en notation complexe : 
11
OO
eq
jCZR   
On exploite alors la relation : 
 ( ) . ( )eq zV t Z v t   et on obtient 
1
O
m
O O O
QFRV jRC m

   
28. On obtient : 
 
2
1
1
O
mm
O OO
R QFVV m RC

 

  
La puissance instantanée dissipée par effet joule s’exprime alors  
 
2
2cosm
JO
VPt R   et par calcul de la 
valeur moyenne on obtient : 
 
22
2
1
22 1
mO
J
O OO
V QF RP Rm RC

 
     
Partie 4 : oscillateurs électriques. 
29. Par définition des fonctions de transfert 
 Sev H j v   et 
   1 eSv v K j v   
30. On doit éliminer ve des deux relations précédentes : 
 
S
e
vv Hj   
On substitue 
   1
S
S
vv K j vHj 
   et on obtient
   
   1 1
S HjvAj v K j H j
    . 
31. On constate que 
   
 
1
1 . S
K j H jvv Hj


 . Pour avoir une tension v1 nulle et une tension vS non nulle, 
on constate effectivement qu’il faut que 
   1 . 0H j K j . 
32. On en déduit alors 
   .1H j K j   ce qui impose  
   
     
.1
arg arg
H j K j
H j K j

  
     
33. On appelle Z1 l’impédance de R et C en série et Z2 l’impédance de R et C en parallèle : 
1
1ZR jC
 ; 
2
11 jCZR   ; par diviseur de tension : 
2
112
2
1
1
S
e
uZ
Zu Z Z
Z
    
On obtient donc : 
 
111 3
1 111 3 11 3
Kj jjRC RCjC R jRC RCR jC

   
                
On obtient bien 
 
1
O
K
K
KKj
jQ



    où par  identification  
1
3
OK   ; 
1
3Q  et 
1
K
RC 

--- Page 5 ---

Concours blanc  PCSI1 et PCSI2 2021-2022 
Physique  Février 2022 
5/8 
34. A BF 
  O
K
KK j j Q
 
 
  d’où 
 
     20.log 20log 20logdB O
K
G K Q  
   
  
A HF 
  O KKK j j Q
 
   d’où 
     20.log 20log 20logdB O
K
G K Q  
   

 
A la fréquence propre  ωK, 
  OK j K   d’où 
   20.logdB OGK  
 
Le point d’intersection des asymptotes est en  : 
   20.log 20logO dB OG K Q  
 
On obtient le diagramme de Bode suivant : 
35. On se place à la fréquence propre ωK alors : 
  1
3
OK j K   fonction de transfert calculé en bouclé 
ouverte avec une intensité en sortie nulle comme rappelé sur le schéma de l’énoncé.  
Puisque i+ l’intensité du courant entrant dans la borne non inverseuse est nulle, on observe bien que 
1
3
Svv . 
36. On étudie la fonction de transfert du circuit à ALI. En régime linéaire : V+=V-=v ;  
on fait une loi des nœuds en terme de potentiel en (-) : 
 
12
0
e Sv v V vV
RR
     
ce qui donne
 
12
0
e Sv vv
RR
  et finalement 
2
1
Se
Rv v v R  
37. On associe les deux relations précédentes pour obtenir : 
2
1
1
3
S S e
Rv v v R  et donc 
  2
1
3
2
RHj R   
 
38. On veut respecter les conditions énoncées en q32. 
   
     
.1
arg arg
H j K j
H j K j

  
    
 
La seconde est bien vérifiée lorsque 
  2
1
3
2
RHj R   et 
  1
3Kj    
Il reste à respecter la première, il faut donc que 
    2
1
12
RH j K j R   
On peut donc proposer pour valeur de résistances raisonnables en TP  : 
1 2 11 2 2R k et R R k      
39. A BF, le condensateur est un coupe circuit et la bobine est une fil ce qui donne pour dipôle équivalent 
au quartz un interrupteur ouvert. 
A HF, le condensateur est un fil et la bobine est un coupe circuit de qui donne pour dipôle équivalent au quartz 
un fil. 
40. On commence par associer R, C, L en série : 
1
hautZ R jL jC     qu’on associe en // avec CO 
1 1 1 1
1
O
O
AB haut C
jCZ Z Z R jL jC

 
   

 d’où
11
1
1
O
AB
jC R jL jC
Z R jL jC
 
 
   
  
Alors  
   
2
2
1
AB
OO
jRC LCZ
j C C jC jRC LC

   

    
41. On souhaite que le quartz présente une impédance réelle, on veut donc annuler la partie imaginaire. On 
en déduit que les deux pulsations ω1 et ω2 envisageables sont celles pour lesquelles la courbe présentée 
coupe l’axe des abscisses. 
On obtient un comportement capacitif du dipôle si la partie imaginaire de l’impédance est négative, c’est -à-dire 
sur les domaines [0, ω1] et [ω2, +∞].

--- Page 6 ---

Concours blanc  PCSI1 et PCSI2 2021-2022 
Physique  Février 2022 
6/8 
Partie 5 : émetteur et récepteur piézoélectriques d’ultrasons. 
a. Propagation d’une impulsion. 
42. On mesure 8 pseudopériodes sur une durée de 0,2ms. On obtient donc une pseudopériode de  2,5.10-2ms. 
La (pseudo)-fréquence associée est alors : 
1 40f kHzT .  
La largeur totale de l’impulsion τ est égale à τ=0,2ms. 
43. Le domaine de fréquences audibles s’étend de 20Hz à 20kHz, la fréquence obtenue de 40kHz est donc 
bien dans le domaine des ultrasons, non audible de fréquence supérieure à celles du domaine audible.  
44. L’onde se propage dans la directi on et le sens de l’axe (Ox), elle dépend donc de la variable 
temporelle
xt c
  qui prend l’expression 
0t c
  en x=0. 
On en déduit que 
( , ) cos 2 . xxs x t P t f t cc                
45. A l’instant t=3τ, le front d’onde parti de x=0 en t=0 
aura attei nt l’abscisse 3cτ ≈, et la fin de l’impulsion 
partie de x=0 en t=τ aura atteint l’abscisse 2cτ. De 
plus l’impulsion se propage sans déformation dan le 
modèle porposée d’où le profil ci contre. 
A l’instant t=τ/2, seule la moitié de l’impulsion a été produite  
d’où l’allure du profil ci-dessous. 
On prend τ=0,2ms et c=340m.s-1 pour réaliser ces graphes. 
46.  Le maximul du profil P(t) est émis à l’instant τ/2, et il se propage avec l’impulsion à la célérité c, on 
obitnet alors : 
2
MMx c t   d’où 
2
M
M
xt c
  
On obtient le tableau suivant 
xM(cm) 20 40 60 80 100 
tM (ms) 0,70 1,27 1,87 2,44 3,02 
c (m.s-1) 333 342 339 342 342 
On utilise la calculatrice pour faire un traitement statistique : 
 La moyenne fournie par la calculatrice donne une évaluation de la célérité. 
 L’écart type fourni par la calculatrice donne l’incertitude type sur la célérité.  
On aboutit à l’évaluation suivante : 
1340 .mc m s   avec 
 
14.u c m s   
47. Le profil de l’impulsion s’est étalé dans le temps lors de la propagation, entrainant une diminution de la 
valeur maximale atteinte. 
Cette évolution peut être la conséquence de deux mécanismes différents : 
 La dispersion qui entraine une variation de la célérité de l’onde en fonction de la fréquence et entraine 
un « étalement » de l’impulsion. C’est probablement le contributeur principal dans le cas étudié. 
 L’atténuation qui diminue l’amplitude de l’onde par absorption de l’énergie transportée par l’onde par 
le milieu de propagation. Dans l’air, ce second effet doit être relativement faible. 
 Notre modèle fait une prédiction assez différente de l’allure du profil en x M=40cm, l’influence de la 
dispersion semble assez importante et notre modèle semble tout de même mauvais sur l’évolution du 
profil. On peut toutefois remarq uer que l’exploitation de la q46. donne une évaluation de la célérité 
correcte et que dans le cadre de cette exploitation notre modèle reste cohérent.  
b. Propagation d’une onde sinusoïdale. 
48. La demi largeur δl1/2 est évaluable à 1% de f et 1digit soit 0,4kHz +0,1kHz. 
En faisant l’hypothèse d’une distribution uniforme des valeurs sur l’intervalle de mesure on aboutit alors à 
l’évaluation suivante : 
 
1 12 3.10
3
l
u f kHz

 . 
49. On doit exprimer une onde progressive  non dispersive sinusoïdale soit  : 
( , ) cos 2 .O
xs x t s f t c     
en prenant pour référence une phase nulle en x=0 à l’instant t=0. 
50. On en déduit que : 
 11( ) cos 2 .OU t U ft   et 
22( ) cos 2 . M
O
xU t U f t c   

--- Page 7 ---

Concours blanc  PCSI1 et PCSI2 2021-2022 
Physique  Février 2022 
7/8 
En supposant qu’aucun déphasage n’est introduit par d’autre m écanisme que la propagation de l’onde de x=0 en 
x=xM. 
51. Sur l’oscilloscope on visualisera deux 
fonctions sinusoïdales synchrones. 
Lorsqu’on déplace le micro dans la 
direction et le sens de l’axe (Ox), on verra 
la tension U 1 qui sert de déclenchement 
restée fixe sur l’écran et on observera une 
translation de la tension U 2 dans la 
direction et le sens de l’axe du temps 
puisque le retard temporel s’accumule au 
fur et à mesure de la translation du micro 
le long de l’axe (Ox). 
52. Le déphasage entre les deux tensions s’exprime : 
2/1 2 Mxf c   
Les deux tensions sont en phase si ce déphasage est multiple de 2 π. On en déduit que : 
2/1 22 ixif c   
 ce qui donne 
.i
cx i i f   
Sur l’oscilloscope, on repère facilement les positions pour lesquelles les deux tensions sont en phase en se 
plaçant en mode XY. On observe alors que la courbe sur l’écran s e ramène à un segment de pente positive 
lorsque les tensions sont en phase. 
53. On conclut de la q52. Et du texte de l’énoncé que
NOxx
N   qu’on exploite pour évaluer λ. 
On peut estimer l’incertitude sur la lecture de xO et xN à 1mm environ, et on peut estimer l’incertitude sur λ par la 
relation de propagation des incertitudes sur une formule de type somme : 
     
221
NOu u x u xN   
On obtient alors : 
8,58mm   et 
 
24.10u mm   
54. On exploite : 
.cf   et la relation de propagation des incertitudes 
     
22
u c u u f
cf


       
      
Et on obtient 
1343 .c m s   avec une incertitude type 
1( ) 3 .u c m s   
Partie 6 : échographie. 
a. Propriétés générales des ondes ultrasonores dans les liquides. 
55. La norme de la for ce pressant étant donnée par le produit de la pression et de l’aire de la surface sur 
laquelle elle s’exerce, on en déduit que Pa ~ N.m-2. 
Il faut encore traduire le Newton en se souvenant que la force de gravité présente une norme qui est le produit 
d’une masse et de la norme de l’accélération de la pesanteur ce qui donne N ~ kg.m.s -2. 
Finalement, en traduction dans le système d’unité fondamentale, on obtient 
21.  smkgPa  
56. On obtient que la compressibilité  χ s’exprime en kg -1.m.s2 et que la masse volumique s’exprime en 
kg.m-3. La célérité des ondes ultrasonores s’exprime en m.s -1. 
On cherche alors la formule donnant c en fonction de χ et ρ sous la forme : c = χAρB. 
En raisonnant sur les kilogrammes puis sur les mètres, on obtient que (A,B) doit vér ifier le système suivant et on 
en déduit l’expression de c en fonction de ces deux paramètres : 





13
0
BA
BA
 ce qui donne 
2
1 BA  d’où 

1c  A.N : 
13 .10.48,1  smc  
La célérité du son dans l’air est d’environ 340m.s-1. On constate que les ondes sonores se propagent 4,3 fois plus 
vite dans l’eau que dans l’air. 
b. Mesure de vitesse du flux sanguin. 
57. On considère le globule à l’instant t O et on 
suppose que son déplacement pendant le 
temps de propagation aller retour  de l’onde 
est négligeable car v S<<c . L’onde réfléchie 
est donc captée à l’instant 
c
Ltt O
OO
2' 

--- Page 8 ---

Concours blanc  PCSI1 et PCSI2 2021-2022 
Physique  Février 2022 
8/8 
On considère ensuite le globule à l’instant t O+T, il s’est donc déplacé d’une distance v ST en remontant l’axe (Ox) 
et on reprend l’hypothèse précédente. L’onde réfléchie est donc captée à l’instant 
c
TvLTtTt SO
OO
)(2''   
On obtient bien que 
c
TvTtTt S
OO
2')''(   et on montre, dans l’hypothèse vS<<c, que 




  c
vTT S21'   
58. On en déduit que : 




  T
TTcv S
'
2  
59. A.N : 
sT 710.33,3   ; 
sTT 1010.67,1'   ; 
11 .10.75,3  smvS  
c. Aspects techniques de l’échographie. 
60. La longueur d’onde est évaluée par
f
c  à la valeur 
m410.0,4   
On constate alors que la largeur a du transducteur est de l’ordre de grande ur de la longueur d’onde . On 
observera donc un phénomène de diffraction de l’onde ultrasonore à son émission. 
61. Le demi angle au sommet du secteur dans lequel l’amplitude de l’onde s’annule une première fois est 
exprimé par : 
a
 sin   AN : 
 90 . On constate alors que la diffraction de l’onde ultrasonore 
s’effectue dans tout le demi espace situé devant le transducteur. 
 
62. Le déphasage introduit entre les ondes produites par (I) et (II) lors de la propagation s’exprime d’après 
les données de l’énoncé par  : 
L
 2
12   où la différence de marche s’exprime
sindL , on 
obtient donc bien finalement que 

 sin2
12 d  
63. Pour que deux ondes soient en phase, il faut que leur déphasage vérifie : 
Zpp  .212  . 
Les angles pour lesquels on obtiendra une amplitude de l’onde importante vérifient  :  
dpP
 sin  
Ce qui donne trois possibilités par évaluation numérique : p = 0 
0O  ; p = 1 
 531  ; p=-1 
 531  
Pour p supérieur à 1, il faudrait que le sinus de l’angle soit supérieur à 1 ce qui est impossible.  
64. Avec la relation donnée dans l’énoncé, on obtient que A 1=A-1 = 0,23.A O. L’onde présente une 
amplitude quatre fois plus importante dans la dire ction θ O =0 que dans les deux autres. On peut en 
conclure que la direction privilégiée dans laquelle est générée l’onde est la direction θ O = 0. 
65. L’évaluation numérique donne :  
 36,0N . Grâce à la barrette, on peut concentrer dans un secteur  
angulaire très faible l’onde générée par le système d’échographie. 
66. On écrit la phase pour (I) puis (II) sous la forme  : 
11
22 dft 
   et 
  22
22 dttf 
   
permettant de tenir compte du retard introduit pour (II) par rapport à (I). 
On obtient alors : 

 sin2212 dtf   
67. La direction privilégiée dans laquelle on produit l’onde d’amplitude la plus importante est 
supposée être toujours celle pour laquelle l’ordre d’interférence est p=0. D’où : 
012    
Finalement on obtient que le retard temporel à introduire pour produire une onde de forte amplitude dans la 
direction θO s’exprime par :  
OOO
c
d
f
dt  sinsin   
68. Le dispositif de retard temporel permet d’effectuer un balayage spatial dans un secteur angulaire 
s’étendant autour de la  direction θO = 0 sans avoir à déplacer la sonde échographique. Il faut cependant 
se placer dans des conditions pour lesquelles l’amplitude de l’onde dans les deux pics secondaires mis 
en évidence à la Q 63 reste petite devant celle du pic principal. Pour c ela il faut que θ O reste petit ce qui 
donne un secteur angulaire pour lequel θO reste dans l’intervalle [-10°, 10°].