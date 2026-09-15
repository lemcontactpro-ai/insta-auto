# corrigé du DM5 effet doppler circuits 1er ordre


--- Page 1 ---

Corrigé du DM5 PCSI2 2022-2023 
Physique. 
1 
Problème 1 : Mesure de vitesse par effet Doppler. 
1. L’onde sinusoïdale de fréquence f ref, d’amplitude s O se propageant à la célérité c dans la direction et le 
sens de l’axe (Ox) et qui aura une phase nulle en (x,t)=(0,0) s’écrit : 
 , cos 2O ref
xs x t s f t c     
2. La longueur d’onde s’exprime par la relation : 
.
ref
ccT f   A.N : 
38,65.10 m  . 
On est dans le domaine des ondes radio dans le sous domaine des micro -ondes. 
3. On applique la loi de Chasles : 
OM OB BM  où 
OM x , 
'BM x  et 
OOOB x v t  on obtient 
donc que : 
( ) '( ) OOx t x t x v t    ou 
'( ) ( ) OOx t x t x v t   . 
4. Dans le référ entiel de la cible, on exprime le signal en exprimant x en fonction de x’  ce qui donne : 
   
2'', cos 2 cos 2 1 '
refO O O
O ref O ref O
fx x v t vs x t s f t s f t x x c c c
                     
. 
5. L’onde réfléchie se propage dans le sens rétrograde, elle s’exprime sous la forme f(t -x’/(c+vO)). Avec le 
coefficient de réflexion r, on aboutit à la forme :
 
2', cos 2 1 '
refO
R O ref
fvs x t rs f t x cc
       
L’onde réfléchie est en phase avec l’onde incidente sur la cible et donc à l’instant initial t=0, on en déduit que : 
2 ref
O
f xc
 
 et finalement : 
   
2', cos 2 1 '
refO
R O ref O
fvs x t rs f t x x cc
       
6. On reprend la relation 
'( ) ( ) OOx t x t x v t    pour aboutir à 
   
2, cos 2 1 2
refO
R O ref O O
fvs x t rs f t x x v t cc
      
 ce qui correspond bien finalement à la 
forme donnée dans l’énoncé : 
   
22, cos 2 1 2
refO
R O ref O
fvs x t rs f t x x cc
       
Le décalage de fréquence entre l’onde incidente et l’onde réfléchie est alors  : 
221 OO
ref ref ref
vvf f f f cc    
 
7. La vitesse vO s’exprime 
.
2
O
ref
cfv f
  A.N : 
112,10.10 . 75,6 /Ov m s km h   
8. En exploitant la donnée sur la précision, on e n déduit que la demi largeur de l’intervalle de mesure est 
égale à δv=1,6km/h. on en déduit que 
 74,0;77,2 ( / )Ov km h . 
L’incertitude type est alors évaluée en appliquant une distribution des résultats uniforme sur l’intervalle de 
mesure et elle s’exprime sous la forme 
  0,93 1,0
3
vuv     en arrondissant à la valeur supérieure. 
Finalement on a l’évaluation : 
75,6 /Ov km h  avec une incertitude type 
  1,0 /u v km h  
9. L’évaluation numérique demandée donne  : 
71, 4.10
ref
f
f
  . Il est donc parfaitement exclu d’envisager 
une mesure directe de cette variation de fréquence. 
10. On exploite l’énoncé pour obtenir : 
 
       
2 42cos 2 1 cos 2
refO
e e ref O ref O ref
fvu t Kv t v t K v f t x f t cc
           
En utilisant les relations de trigonométrie, on transforme le produit de cosinus en somme de cosinus  : 
       
22 44cos 2 2 cos 222
ref refOO
e e ref ref O O
ffK v K vu t Kv t v t f f t x ft x cc
                  

--- Page 2 ---

Corrigé du DM5 PCSI2 2022-2023 
Physique. 
2 
On obtient donc un signal à deux composantes 
sinusoïdales : 
 Une composante d’amplitude 
2
2
OKv  pour 
la fréquence 
 2 refff   
 Une composante d’amplitude 
2
2
OKv  pour 
la fréquence 
 f  
Le spectre correspondant à ce signal est alors donné 
ci-dessous. 
 
11. On observe deux composantes sinusoïdales dans le signal dont on veut extraire la composante la plus 
basse, on va donc employer un filtre passe-bas. 
12. On remplace le condensateur par un coupe-circuit dans le domaine BF. On observe alors que le circuit 1 
et le circuit 3 coupent les BF alors que le circuit 2 transmet les BF. 
On remplace le condensateur par un fil dans le domaine HF. On observe alors que le  circuit 2 et le circuit 3 
coupent les HF et que le circuit 1 transmet les HF. 
On en conclut que : 
 Le circuit 1 est un passe haut. 
 Le circuit 2 est un passe bas et sera celui qui doit être employé pour réaliser l’opération de filtrage.  
 Le circuit 3 est un passe bande. 
13. La fonction de transfert d’un filtre , étudié en régime sinusoïdal forcé, est définie comme le rapport de la 
tension en sortie du filtre par la tension en entrée du filtre en notation complexe : 
   
 
s
e
utHj ut   
Pour le circuit 2, on réalise un diviseur de tension, puisqu’il est étudié comme d’habitude en boucle ouverte pour 
déterminer la fonction de transfert ce qui donne :  
   
C
se
CR
Zu t u t ZZ   ce qui aboutit à : 
  1
12H jf j fRC 
soit 
 
1
O
O
HH jf fj f

  avec 
1OH   et 
1
2
Of RC  
14. La fréquence de coupure à -3dB est la fréquence pour laquelle, le gain en décibel prend une valeur 
située 3dB sous la valeur maximale prise par le gain en décibel. 
  ,max 3dB c dBG f G dB
 ce qui revient en gain à dire que 
  max
2
c
GGf   
Dans le cas qui nous concerne : 
  2
1
O
O
HGf
f
f


  on en déduit que 
COff   
15. Sur le domaine BF, la fonction de transfert est approximée par : 
  1OH jf H   
 Le gain en décibel adopte comme comportement asymptotique :
   20log 0dB OG f H   
 Et la phase devient : 
   arg 0 OfH   
Sur le domaine HF, la fonction de transfert est approximée par : 
  O
O
HH jf j f
f
  
 Le gain en décibel adopte le comportement : 
   20log 20log 20logdB O
OO
ffG f H ff
         
     
 Et la phase devient : 
   arg 22
OfH      
Amplitude 
(V) 
f (Hz) 
2
2
OKv
0 δf 2fref+δf

--- Page 3 ---

Corrigé du DM5 PCSI2 2022-2023 
Physique. 
3 
On aboutit alors au diagramme de Bode suivant : 
  
  
En pointillé, le diagramme asymptotique, en trait plein le diagramme réel. 
16. On évalue la valeur 
maximale de δf avec 
la relation : 
32 9,6.10O
ref
vf f Hzc 
  
on fixe donc 
4
max 10f Hz   
 
On établit alors le gabarit ci-
contre pour le filtre : 
 
17. On souhaite atténuer d’un facteur 103 l’amplitude du signal de fréquence 2fref (en négligeant δf devant 
fref). Cette composante doit être placée dans le domaine HF pour lequel 
  O
O
HH jf j f
f
   
et le gain est donc 
 
32 10 2
OO
ref
ref
HfGf f
 . Puisque fO et fC s’identifient, on obtient donc  
3
;max
210
C ref
O
ff H

  
L’application numérique donne : 
7
;max 7,0.10Cf Hz    
on observe que 
4max
,max
1,4.10
C
f
f
  , la fréquence à conserver est donc presque 4 décades en dessous de la 
fréquence de coupure évaluée. La composante à conserver sera alors bien transmise sans atténuation puisqu’elle 
est située loin dans le domaine BF du filtre passe bas de gain statique unitaire.  
18. La fréquence de coupure s’exprime : 
,max 1
52
C
O
f f RC  d’où 
,max
5
2 C
R fC  A.N : 
5,2Rk  
Cette valeur  de résistance est raisonnable puisqu’on obse rve une valeur usuellement rencontrée en TP. Cette 
résistance donnera la résistance d’entrée du filtre et e lle est suffisamment forte pour qu’on évite des problèmes 
d’adaptation d’impédance. 
Log(2fref) 
log f 
GdB 
-60 
Zone 
interdite 
0 
Zone 
interdite 
0 
Log(δfmax)