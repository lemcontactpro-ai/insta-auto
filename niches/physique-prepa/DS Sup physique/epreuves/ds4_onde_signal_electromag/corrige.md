# corrigé du DS4 onde signal electromag


--- Page 1 ---

Corrigé dS4 PCSI2 2022-2023 
physique 
1/6 
Problème 1 : Mesures de distance et de vitesse. 
a. Généralité. 
1. Une onde es t une perturbation d’un milieu qui se déplace dans l’espace, sans qu’il y ait déplacement 
global de la matière qui constitue le milieu de propagation. 
2. L’expression générale du signal a ssocié à cette onde s’exprime alors   
)/()(),( cxtgctxftxs 
 lorsque la propagation s’effectue dans la direction et le sens de 
l’axe Ox.  On introduit dans l’expression précédente la célérité c de l’onde qui s’interprète pour une 
onde progressive comme la vitesse de translation de l’onde le long de l’axe Ox. 
 
3. Dans le cas où on étudie une onde sinusoïdale, le signal s H(x,t) s’exprime en fonction de la période 
temporelle T et de la longueur d’onde λ sous la forme : 




  
 xtTstxs OH
22cos),( . 
Qu’on peut réécrire
2( , ) cosHO
xs x t s t Tc
        alors par identification on obtient 
Tc.  
b. Le sonar, un système employant des ondes acoustiques. 
4. Les grandeurs physiques associées aux ondes acoustiques sont la pression (acoustique) et la  vitesse 
locale de l’écoulement du fluide. 
5. La bande de fréquences à laquelle l’oreille humaine est sensible s’étend de 20 Hz à 20kHz.  
6. Au seuil de détection de l’oreille humaine, la surpression présente un ordre de grandeur de Pseuil 10-5 Pa 
et au seuil de douleur, elle présente un ordre de grandeur de Pdouleur=10 Pa. 
On construit alors l’échelle décibel en notant 
20logdB
seuil
PI P
 
  le seuil de détection est alors fixé par 
convention à 0dB, le seuil de douleur correspond alors à 120dB. 
7. Entre le début de  l’émission et la réception de l’onde, il s’écoule une durée n.T. L’onde sinusoïdale a 
alors parcourue une distance n.λ. La distance parcourue étant l’allé retour entre la surface et le fond du 
bassin, soit 2h, on obtient : 
n
h2  
Pour la célérité de l’onde acoustique dans l’eau, on traduit alors 
TcL.  pour obtenir 
fn
hc L
2  
A.N : 
13 .10.45,1  smc L  
8. On reprend la relation précédente pour obtenir : 
f
cnh L
2
'' D’où 
mh 310.55,1' . 
9. La masse molaire moyenne de l’air est le barycentre des masses molaires du diazote et du dioxygène 
affectées des poids relatifs 0,8 et 0,2 ce qui donne : 
  ))(2.(2,0)(2.8,0 OMNMM air 
 A.N : 
1.8,28  molgM air  
10. On obtient pour la célérité du son dans l’air : 
1.338  smcG . 
On constate alors que : 
22,0
L
G
c
c . La célérité dans l’eau est environ 5 fois plus grande que celle dans l’air. On 
pourra retenir ce résultat qualitatif pour sa culture scientifique. 
11. Le seuil de détection du récepteur étan t Pmin, on obtient la profondeur maximale théorique accessible à 
la mesure au sonar par la relation : 
 maxmin 2exp hPP O   
12. Ce qui donne : 






min
max ln2
1
P
Ph O
  A.N : 
mh 4
max 10.84,1  
On constate que h’< hmax, la mesure de cette profondeur était donc bien réalisable à l’aide du sonar étudié. 
s(x,t1) 
s(x,t2 >t1 ) 
x 
s c(t2-t1)

--- Page 2 ---

Corrigé dS4 PCSI2 2022-2023 
physique 
2/6 
13. On a supposé dans cet exercice que la réflexion de l’onde sur le fond marin était parfaite, c’est -à-dire 
que l’onde réfléchie présente la même amplitude et la même phase que l’onde incidente au niveau du 
plan de réflexion. 
14. Si l’onde réfléchie sur le fond marin est d’amplitude inférieure à l’onde incidente, la profondeur 
maximale explorable à l’aide du sonar étudié sera plus faible que celle qui a été estimée précédemment.  
L’éventuelle introduction d’un déphasa ge lors de la réflexion peut être une source d’erreur sur l’estimation du 
temps nécessaire à l’aller-retour de l’onde sonore. 
c. La diode laser, un système employant des ondes électromagnétiques. 
15. Pour une longueur d’onde de 845 nm, on se situe dans le domaine  du proche infrarouge, très près de la 
limite avec le domaine du visible. 
16. L’onde réfléchie est générée à partir de l’onde incidente sur la plaque 3. Les deux ondes sont donc 
générées à partir d’une même source primaire (ici la diode laser), elles seront do nc cohérentes. 
 Lorsqu’on considère la superposition de deux ondes cohérentes, on peut observer le phénomène d’interférence 
entre ces deux ondes. 
17. L’onde incidente s’exprime : 





 



  c
xtfEtxE OD .2cos),(  . 
18. L’onde réfléchie s’exprime : 





 



   c
xtfEtxE GOG .2cos),( ,  
Le coefficient de réflexion sur la plaque 3 est ρ, on en déduit que :  
OGO EE .,   
La réflexion sur la plaque 3 n’introduit par de déphasage, on en déduit que : 





 








 




c
Dfc
Df .2.2   
Finalement : 





 



  c
DxtfEtxE OG
2.2cos.),(  . 
19. Au niveau de la plaque 2, c’est -à-dire en x = 0, le déphasage entre l es deux ondes s’exprime  : 
c
fD
GD
.4 
. 
20. Au niveau de la plaque 2, on superpose les champs électriques des deux ondes cohérentes d’amplitude 
EO et ρ.E O, présentant un déphasage Δφ. L’amplitude du champ électrique résultant est donnée par la 
relation 
   cos21 2
OT EE  
21. L’amplitude sera minimale et on observera des interférences destructives pour : 
  12,   pP . 
L’amplitude sera maximale et on observera des interférences constructives pour : 
 pP 2,   . 
22. La fréquence fm s’exprime : 
m
m
cf  . D’où l’évaluation numérique : 
Hzf m
1410.55,3 . 
On constate alors que
410.4,1 
mf
f . On peut en déduire que la valeur de la longueur d’onde λ m au cours de 
cette mesure sera quasiment constante. 
23. Entre deux maxima consécutifs, le déphasage augmente de 2.π ce qui amène à l’expression  : 
42 D fc

 et finalement 
2
cf D  . 
24. Sur l’intervalle de fréquence Δf, il y a donc ND + α  intervalles de fréquence δf où 
10  . 
On obtient alors : 
2
D
f D fN fc 
    puis 
2
D
DfN c
  
25. A partir de la relation précédente, on obtient 
f
c
f
cND D
 22
  
On évalue alors la distance par la relation 
f
cND D
 2  et l’erreur de mesure maximale sera de 
f
c
2  
Lorsqu’on compte ND = 200, la distance D est située entre Dmin = 60,0 cm et Dmax = 60,3 cm. 
26. Entre deux maxima d’intensité en sortie, on a toujour s un décalage de phase de 2π. Les observations de 
deux maxima successifs seront donc séparées d’une durée δt telle que :

--- Page 3 ---

Corrigé dS4 PCSI2 2022-2023 
physique 
3/6 
 
  4 . 4 .2 ( ( ) mmf f v D t t D t tcc
       soit 
2
mt v
   
Sur une durée Δt, il y a donc NV+α intervalles de temps δt. On obtient alors : 
m
V
tv
t
tN   .2  
27. On obtient donc pour la vitesse : 
  tNv m
V
 2
 . L’erreur maximale sera 
15 .10.2,12
 smt
m  
28. On compte N 1 maxima d’intensité en sortie du système sur une durée T/2 et pour un balayage de 
fréquences alors de fm à fm+Δf. 
Le déphasage introduit est do nc de 
1.2 N  entre l’état initiale, distance D, fréquence f m et l’état final distance D 
+ vT/2 et fréquence fm+Δf, ce qui donne : 
   


 



  DfTvDffcN mm .2
4.2 1
  
De même on obtient la relation : 
    


 



  2
4.2 2
TvDffvTDfcN mm
  
L’hypothèse v « suffisamment grande » assure que l’expression  dans cette seconde relation reste positive. 
On obtient alors le système : 
 
 






DfvTffcN
DfvTffcN
m
m
..22
..22
2
1  
Par combinaison linéaire de ces deux équations, on obtient : 
 
   











 

2121
21
4
2
NNf
cNND
TNNv
m
m
m


  
A.N : 
mDsmv 112 10.99,5.10.88,3    
Problème 2 : Modes de vibration d’une corde. 
a. Etude des modes propres de vibration des cordes. 
1. L’onde stationnaire unidimensionnelle est de la forme 
  



  
 xftAtxs 2cos2cos),(  
Pour laquelle 
f
c   où c est  la célérité des ondes progressives dans le milieu étudié. 
2. La première condition est  : y T(x=0,t)=0 ce qui donne 
 cos 0  , on choit alors ψ = -π/2 et on peut 
réécrire l’onde stationnaire sous la forme : 
  2( , ) cos 2 sinTy x t A ft x  
   
La seconde condition est : yT(x=L,t)=0 ce qui donne : 
2sin 0 L

   
On obtient alors l’ensemble des solutions dénombrées par l’entier naturel positif n telles que : 
2
n
Ln    
Les modes propres de vibrations de la corde s’expriment alors :  
  




 xtfytxy
n
nnOn

 2sin2sin),( ,
 Avec 
2
n
L
n    et 
L
nccf
n
n
2   
3. Pour une corde de longueur L, la longueur d’onde du fondamental est 
  1;6 2 1,30k k L m     
On obtient alors la célérité de l’onde en exploitant la relation issue de la définition de l’onde 
stationnaire
.kkcf    
Numéro k=1 k=2 k=3 k=4 k=5 k=6 
Célérité (m.s-1) 428 321 255 191 143 107 
4. Les ventres de vibration sont les lieux où l’onde stationnaire présente une amplitude d’oscillations 
maximale. Ils sont localisés aux points tels que 
12sin 




 x
n


--- Page 4 ---

Corrigé dS4 PCSI2 2022-2023 
physique 
4/6 
Les nœuds de vibration sont les lieux où l’onde stationnaire présente une amplitude d’oscillations minimale. Ils 
sont localisés aux points tels que 
02sin 




 x
n
  
La distance entre deux ventres de vibration successifs est alors de λ n/2 et la distance entre un ventre et un nœud 
de vibration consécutifs est λn/4.   
5.  
 
  
  
n=1     n=2    n=3    
6. La célérité des ondes progressives est homogène à une vitesse d’où 
 
1.c L T  . 
La masse linéique µ est de dimension 
 
1.µ M L  . 
La tension du fil est une force, homogène au produit d’une masse et d’une accélération 
 
2..T M L T   
Dans la loi recherchée :
     

TµKc . , les coefficients α et β doivent respecter le système : 






12
0
1


 .  
On obtient pour solution : 







2
1
2
1

   d’où 

Tc  on en déduit que 
2
k k kT µ c  
Numéro k=1 k=2 k=3 k=4 k=5 k=6 
Tension (N) 76,9 56,8 56,3 74,3 77,5 84,7 
7. La forme imposée à la corde est reportée au-delà de l’abscisse x = L par symétrie par rapport au point S. 
On obtient alors le motif d’une fonction périodique de période 2L tenant compte de la forme de la corde.  
  
8. La forme  de la corde impose le motif d’une fonction périodique de période 2L. On pourra alors la 
décomposer selon l’analyse de Fourier.  
Le mode de vibration imposé à la corde sera alors exprimable par décomposition selon les modes propres de la 
corde par l’expression : 
 

 











1
2sin2sin),(
n n
nnn xtfctxy 
  
9. Le centre de la corde est un ventre pour les harmoniques telles que  : 
1sin 





n
L

 c’est-à-dire pour les 
entiers tels que 
12sin 



 n .  
On en déduit que le centre de la corde est un ventre pour les harmoniques impaires n = 2p+1. 
De même, le centre de la corde sera un nœud pour les harmoniques paires n = 2p.  
Dans le spectre du son émis, on observe bien qu’il ne fait intervenir que le fondamental et les harmoniques 
correspondant aux modes propres de la cord e, la vibration est donc bien expérimentalement la somme des 
vibrations associées aux modes propres de la corde. 
x L 
d 
y 
S

--- Page 5 ---

Corrigé dS4 PCSI2 2022-2023 
physique 
5/6 
En pinçant la corde en L/2, ventre de vibration pour les harmoniques impaires et nœud de vibration pour les 
harmoniques paires, on remarque que le spectre du son émis ne contient aucune harmonique paire. 
10. Dans le spectre de la corde pincée en L/5, on constate l’absence d’harmonique de rang étant un multiple 
de 5. L’abscisse L/5 est le lieu d’un nœud de vibration pour toutes ces harmoniques. Leur a bsence dans 
le spectre du son émis est donc cohérente avec l’observation faite à la question précédente.  
11. Dans la première situation, on pince et étire la corde au maximum sur le lieu du ventre de vibration du 
fondamental. Dans la seconde situation, on pinc e et étire la corde au maximum à une abscisse qui n’est 
pas un ventre de vibration du fondamental. 
Si on suppose que l’excitation d’un mode est proportionnel à l’amplitude de ce mode à l’abscisse où on pince la 
corde, comme le suggère les résultats qualita tifs des questions précédentes, on comprend alors que dans le 
second cas, on excite moins le fondamental que dans le premier cas. 
Pour l’harmonique de rang 2, lorsqu’on pince la corde en L/5, on se trouve relativement proche d’un ventre de 
vibration (situé  en L/4). L’hypothèse faite précédemment permet alors de justifier que cette harmonique soit 
excitée, et qu’elle présente une amplitude relativement forte. 
b. Etude d’un accordeur de guitare. 
12. Sur le graphique, on observe un signal variable quasi -périodique dont les valeurs sont comprises entre 0 
et une vingtaine de mV. La valeur moyenne semble être de l’ordre de 10mV. 
13. En prenant appui sur les pics double présents sur le graphique, présent aux instants 0,9ms, 4ms, 7,1ms, 
on peut estimer la période du fondamental à T=3,1ms. 
14. La fréquence du fondamental est alors de l’ordre de 322 Hz proche de la fréquence d’accord de la corde 
Mi aigu. C’est donc à priori cette corde Mi aigu qui a été pincée. 
15. On reprend le schéma en remplaçant le condensateur par un coupe circuit à basse fréquence et par un fil 
à haute fréquence. 
On observe alors que la résistance relie la sortie à la masse sans qu’aucun courant la traverse, la tension de sortie 
est alors nulle à basse fréquence. Le circuit coupe les basses fréquences. 
On observe qu’un fil relie l’entrée à la sortie, la tension d’entrée est donc transmise en sortie en haute fréquence. 
Le circuit laisse passer les hautes fréquences. 
On a donc affaire à un circuit passe haut. 
16. Par un diviseur de tension, on obtient : 
  1 1 1
1
11
1
1
1 1
R jR CHj jR CR jC
 

   
On met alors cette fonction de transfert sous la forme canonique : 
  1
1
1
1
O
O
j
Hj
j

 


   
où on fait apparaître la pulsation propre 
1
11
1
O
RC  . 
17. On fait l’étude asymptotique à basse fréquence de ce filtre  : 
 1
1
H j j  
 
D’où le gain en d écibel : 
 1,
1
20logdBG  
 
  on observe une 
asymptote oblique de pente de +20dB/dec. 
De même à haute fréquence  : 
 1 1Hj    d’où 
 1, 0dBG    on 
observe une asymptote horizontale. 
18. L’application numérique donne  : 
1
1 1,59.10f Hz  Cette fréquence est une décade sous la fréquence 
du fondamental du signal présenté  figure 1. Le fondamental et les harmoniques passent donc le filtre. 
En revanche, la composante continue (assimilable à une composante de fréquence nulle) est éliminée.  
Ce premier filtre permet d’éliminer la composante continue du signal enregistré.  
19. Les deux composants sont en parallèle : 
2
2
1 1 1 1
eq R C
jCZ Z Z R       
Finalement : 
2
221
eq
RZ jR C   .

--- Page 6 ---

Corrigé DS4 PCSI2 2022-2023 
physique 
 
6/6 
20. On emploi un ALI supposé en régime linéaire (la boucle de rétroaction sur l’entrée inverseuse 
permettant cette hypothèse), on sait alors que : 
VV  et d’après le circuit 
1Vu    
Par diviseur de tension (possible car aucun courant n’entre par l’entrée inverseuse)  :  
3
2
3 eq
RVu RZ
    
On obtient alors : 
21
3
1
eqZuu R

  ce qui donne : 
 
2
3
2
22
1 1
R
RHj jR C    
Cette fonction de transfert se met bien sous la forme 
  2
2
2
1
1
GHj
j
 


 . Avec 
2
2
3
RG R et 
2
22
1
RC  . 
21. Le comportement basse fréquence donne  : 
 2 21H j G   d’où le gain 
 21 G  à basse 
fréquence 
Le comportement haute fréquence donne : 
 2 1Hj    d’où le gain unitaire à haute fréquence. 
22. L’application numérique donne : 
2
2 1,13.10G   et 
2
2 4,98.10f Hz  
Ce filtre joue le rôle d’amplificateur pour les signaux situés d ans le domaine basse fréquence mais ne modifie 
pas les signaux situés dans le domaine haute fréquence. 
Cet étage permet donc d’amplifier le fondamental du signal et les premières harmoniques dans certain 
cas, mais sans amplifier les signaux hautes fréquences. 
23. On observe ici un filtre passe bande  qui présente les caractéristiques usuelles d’une pente de 
+20dB/dec à basse fréquence et d’une pente de -20dB/dec à haute fréquence. 
En utilisant le graphe de droite pour plus de précision, on lit la fréquence propr e au maximum de la courbe de 
gain. 
2
3 3,30.10f Hz  
24. Toujours en utilisant le graphique de droite, on lit deux fréquence de coupure  : 
2
1 3,20.10cf Hz  
et
2
2 3,40.10cf Hz . On en déduit le facteur de qualité : 
33
21
16,5
cc
ffQ f f f   . 
25. On lit la valeur du gain en décibel à la fréquence f=315Hz soit  : 
  6dB coG f dB   ce qui correspond à 
un gain 
  1
2Gf  . Si la corde est désaccordée à f=315  Hz, la composante spectrale fondamentale sera 
atténuée d’un facteur 2 en sortie de ce filtre. 
26. On observe sur le spectre : 
 Une composante de fréquence nulle d’amplitude 10mV qui correspond bien à l’observation 
d’une valeur moyenne de 10mV vue en q12. 
 L’harmonique de rang 3 est à environ 1kHz, l’armonique de rang 6 à environ 2kHz et 
l’harmonique de rang 9 légèrement avant les 3kHz. Cette observation est compatible avec la 
fréquence fondamentale évaluée pour le signal en q 13 qui était de 3 22Hz, ce qui donne une 
harmonique de rang 3 à 966Hz (1kHz à 3,4% près), rang 6 à 1932Hz, rang 9 à 2898 Hz.  
27. Le premier filtre (F 1) élimine la composante continue du signal et conserve toutes les autres 
composantes sans modifier leurs amplitudes. On en déduit que le spectre du signal u 1(t) est celui 
désigné par la lettre (a). 
28. En sortie du second filtre (F2) les composantes basses fréquences du signal u 1 sont amplifiées d’un 
facteur 114, les composantes hautes fréquences ne sont pas modifiées. On en déduit que le spectre du 
signal u 2(t) est celui désigné par la lettre (d) , le seul pour lequel le rapport d es composantes 
fondamentales est cohérent avec cette valeur de gain. 
29. On observe dans le signa l u2(t) une composante fondamentale d’amplitude 1,8V environ ce qui donnera 
une composante fondamentale d’amp litude proche de 1V en sortie du filtre  lorsque l’accord n’est pas 
parfait et la fréquence de la note de 322Hz. 
Pour l’harmonique de rang 2, de fréquence d’environ 6 40Hz, le gain en décibel lu sur le diagramme de Bode est 
d’environ -32dB soit une amplitude divisée par 400. L’amplitude de départ était de 2,0V, elle tombe à 5mV. 
Pour les harmoniques de rang supérieur, l’atténuation sera encore plus forte. 
On en conclut que le signal u3(t) est un signal quasisinusoïdal de fréquence f co=322Hz (si on prend la valeur 
obtenue en q13) et  d’amplitude proche de 1V. On peut évaleur son taux de distorsion en comparant 
l’amplitude de l’aharmonique de rang 2 à celle du fondamentale ce qui donne environ 5%.