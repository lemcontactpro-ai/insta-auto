# corrigé du DM4 filtre elec


--- Page 1 ---

Corrigé DM4 PCSI2 2022-2023 
physique 
1/3 
Problème 1 : Filtre de Hartley. 
a. Etude de la fonction de transfert. 
1. Par construction du circuit équivalent à basse fréquence, la bobine étant équivalente à un fil, on montre 
que s(t)=0. 
De même à haute fréquence, le condensateur est équivalent à un fil, on a donc u A la tension aux bornes 
du condensateur qui est nulle. L’étude générale du circuit fournit que u A(t) = 2.s(t) et on obtient donc 
que s(t)=0. 
On en conclut que ce filtre est probablement un passe bande. 
2. Les équations de départ sont les suivantes : 
Un diviseur de tension « en sortie » fournit la relation 
su A .2  
Une loi des nœuds en A fourni la relation :  
 00AA
A
u e u s jC uR jL  
      
On obtient alors : 
R
esjLjCR 




   122  d’où 
 




 





 

L
RRCjjLjCRjH
21
21122  
On obtient bien la fonction de transfert sous la forme : 
 





 






O
O
O
jQ
HjH
1  
Avec, par identification : 
2
1OH , 
RCQ
O
  et 
L
RQ O
2 d’où 
LC
O
2
1  et 
L
CRQ 2  
3. Le gain en décibel est défini par  : 
  )(log.20  jHGdB   ce qui donne pour le filtre étudié  : 
  












 
2
21log10log20 


 O
O
OdB QHG
 
La phase est définie par : 
   )(arg  jH  ce qui donne : 
  arctan O
O
Q  
       
4. A la pulsation propre, on obtient : 
  OOdB HG log20  et 
  0O  
A basse pulsation
0 , on obtient : 
  





O
OdB QHG 
 log20log20log20  et 
  2
   
A haute pulsation
 , on obtient : 
  





O
OdB QHG 
 log20log20log20  et 
  2
   
 
5. Application numérique  : 
2
1OH , 
14 .10.07,7  sradO
, 
7,70Q  
Pour le diagramme de Bode asymptotique, on fait 
figurer le point de coordonnées  : (logωO, 20logH O) 
et les droites asymptotiques de pente +20 dB/dec 
sur le domaine ω<ω O, et -20dB/dec sur le domaine 
ω>ωO, passant par le point de coordonnée (logω O, 
20logHO-20logQ). 
 
6. La largeur de la bande passante est alors donnée par 
O
Q
  A.N : 
13
12 .10.0,1  srad  
b. Effet sur un signal périodique. 
On envoie en entrée de ce filtre un signal créneau impair de période T =6π/ω O de moyenne nulle et d’amplitude 
E.

--- Page 2 ---

Corrigé DM4 PCSI2 2022-2023 
physique 
2/3 
7.  
  
La valeur efficace de ce signal est définie par  : 

T
eff dttfTe
0
22 )(1
  
on obtient donc 
2
0
22 1 EdtETe
T
eff    la valeur 
efficace du signal est alors 
Eeeff   
8.  ωf est la pulsation fondamentale du signal. Elle est reliée à la période par : 
T
f
 2  d’où
3
O
f
    
9. Les valeurs efficaces pour les composantes sinusoïdales peuvent être recalculées, ou bien on peut les 
exprimer directement comme résultats du cours par : 
 12
22
,
 k
Ee effk  
Le tableau des valeurs efficaces pour 
 4,0k  est le suivant : 
k 0 1 2 3 4 
ek,eff (V) 1,8 0,60 0,36 0,26 0,20 
Et le spectre présente l’allure suivante : 
 
10. Le filtre présente une bande passante de située entre 
O 99,01   et
O 01,12  .  
Puisque 
3
O
f
  , la seule harmonique dans la bande passante du filtre est celle correspondant de rang 3 
correspondant à k=1.  Qualitativement, les autres harmoniques sont éliminées par le filtre et on obtiendra en 
sortie du filtre la réponse de ce dernier à l’harmonique de rang 3. 
Pour déterminer son amplitude et sa phase, on applique la fonction de transfert au signal en notation complexe 
associé : 




  23exp3
4).3()(  tjEjHts ffO   
ce qui donne par retour aux notations réelles : 
 tEHts f
O  3sin3
4.)(   
11. La valeur efficace de la composante k est exprimée par 
.)( ,, effkfeffk ejkHs   
ce qui donne alors l’expression suivante : 
 12
22
12
3
3
.121 2
,







 k
E
k
kQ
Hs O
effk  
Les applications numériques sont fournies dans le tableau suivant : 
k 0 1 2 3 4 
sk,eff (V) 4,8.10-3 3,0.10-1 2,4.10-3 9,6.10-4 5,3.10-4 
12. Les rapports demandés sont évalués à :s0,eff/s1,eff = 1,6.10-2
  et s2,eff/s1,eff = 8,0.10-3
 . 
Le taux de distorsion en sortie est évaluable grossièrement par 
eff
effeff
eff
effeff
s
ss
s
ss
,1
,2,0
,1
,1 


  A.N : 
%4,2  
c. Effet sur un échelon de tension. 
13. En reprenant la fonction de transfert 
 
22
1 



















 

OO
OO
O
O
O
Q
j
Q
jH
jQ
HjH  
On obtient l’équation algébrique liant la sortie à l’entrée : 
  )(22 teQ
jHtsQ
j
OOOO 









    
Le retour aux notations réelles donne : 
)()()()( 2
2
2
tdt
de
Q
Htstdt
ds
Qtdt
sd OO
O
O  

--- Page 3 ---

Corrigé DM4 PCSI2 2022-2023 
physique 
3/3 
14. e(t) est un signal constant égal à E sur l’intervalle ]0, +∞[.  
L’équation demandée est donc 
0)()()( 2
2
2
 tstdt
ds
Qt
dt
sd
O
O   
15. Le polynôme caractéristique est alors : 
022  O
O rQr   de discriminant : 
 2
2
41 QQ
O 




   
La valeur du facteur de qualité Q>1/2 indique alors que les racines peuvent s’écrire so us la forme  : 
 1412
2 QjQr O
, on pose alors : 
O
Q
 2  et 
142
2  QQ
O
e
  
La solution générale de l’équation est alors donnée par : 
    tBtAttS eeH  sincosexp)( 



  
16. Avec Q=70,7, on obtient bien 
417,07.10 .eO rad s   et 
42,0.10 s   
17. Pour t<0, e(t)=0 et on suppose qu’on a atteint un régime permanent d ’où u A(t) = 0 et s(t) = 0. On en 
déduit également que l’intensité dans les bobines de sortie est i L(t)=0. 
L’intensité dans la bobine étant continue, on en déduit que i L(t=0-) = i L(t=0+) =0. Tout se passe comme si la 
branche contenant les deux bobines était coupée et on se ramène donc à l’étude du circuit RC « d’entrée ». 
On étudie alors ce circuit RC soumis à l’échelon de tension ce qui donne l’équation différentielle sur l’intervalle 
]0, +∞[ : 
RC
EuRCdt
du
A
A  1  
La solution de cette équation est : 





 



 RC
tEtuA exp1)(  ce qui donne : 




 RC
t
RC
Etdt
duA exp)(  
On en déduit alors : 
0)0(  tuA  et 
RC
Etdt
du A   )0(  
La relation 
)(.2)( tstu A   est toujours valable et donne : 
0)0(  ts  et 

 E
Q
E
RC
Etdt
ds O  
22)0(  
18. La première condition initiale donne : 
Ats   0)0(  
         1( ) exp cos sin exp sin cos O O O O O O
ds t tt A t B t A t B tdt        
               
 
La seconde condition initiale donne : 
( 0 ) O
ds A EtBdt 
     
On obtient : 
0A  ; 
O
EBE   et le signal de sortie : 
 ( ) exp sin O
ts t E t 
 