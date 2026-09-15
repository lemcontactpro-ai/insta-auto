# corrigé du DS3 RSF filtres electromag


--- Page 1 ---

Corrigé DS3 PCSI2 2022-2023 
physique 
1/5 
Problème 1 : Mesures d’impédances. 
A. Mesure de l’impédance de sortie d’un générateur basse fréquence (GBF). 
1. L’oscilloscope est un appareil qui permet de mesurer une différence de potentiel (soit une tension) entre 
deux points du circuit étudié, c’est donc l’ équivalent d’un voltmètre, il est idéal si son impédance 
d’entrée est une résistance dont la valeur tend vers l’infini. 
2. Première expérience : 
 
L’intensité dans le circuit est nulle.  
La tension mesurée est donc 
( ) ( )U t E t  
Seconde expérience : 
 
On observe que R g et R sont parcourues par la 
même intensité. 
Le diviseur de tension donne 
( ) ( )
g
RU t E t RR   
3. La première expérience permet d’affirmer que 
 ( ) ( ) cos OU t E t E t   on en déduit 
8mOE E V  
La seconde expérience permet d’affirmer que 
 ( ) ( ) cos 2
CO
Cg
REU t E t tRR    
On en déduit que 
1
2
C
Cg
R
RR  , et finalement  
50gCRR    
B. Mesure de l’impédance d’entrée d’un oscilloscope. 
4. A partir du couple résistance RO, capacité CO, on peut construire un temps caractéristique
O O ORC   
5. Le circuit étudié peut être schématisé de la 
manière suivante : 
 
6. A basse fréquence, le condensateur est 
assimilé à un interrupteur ouvert et le 
circuit devient : 
Par un diviseur de tension, on obtient 
( ) ( ) O
Og
RU t E t R R R   et lorsque l’expérience donne une tension moitié  
1
'2
O
O C g
R
R R R 
 puis 
'O C gR R R  On observe alors que 
'1OCR R M    et on vérifie bien 
OgRR  
7. Le circuit à étudier est 
le suivant : 
 
Le diviseur de tension donne
1
( ) ( ) 1
O
O
jCU t E t
R jC



  
ce qui donne 
1
1
O m
O
UE jRC     
puis
 
2
11
1 1
O m m
O O
U E E jRC RC 
  

--- Page 2 ---

Corrigé DS3 PCSI2 2022-2023 
physique 
2/5 
La condition d’amplitude moitié donne 
 
2
1
11
2 1 ORC 

 Finalement 
3
OC R  A.N : 
14OC pF . 
8. Le temps caractéristique établi e n q4 donne une fréquence propre du circuit 
1 71O
OO
f kHzRC , ce 
qui place bien la fréquence de 1kHz dans le domaine BF à 1,8 décades sous la fréquence propre.  
Si on évalue l’impédance du condensateur à la fréquence de 300kHz, on obtient 
41 2.10C
O
Z C     
On rappelle que la résistance RO=1MΩ. Dans l’association parallèle de deux dipôles, le dipôle prévalent est celui 
d’impédance réelle la plus faible. Ici R O≈48.|ZC|, on en déduit qu’à cette fréquence, il est tout à fait raisonnable 
de négliger la résistance RO. 
C. Mesure d’impédances par la méthode des ponts. 
9. Lorsque le pont est équilibré, l’intensité traversant AB est la même que celle traversant BC, on en 
déduit que Z1 et Z2 sont associées en série et que Z3 et Z4 sont associées en série. 
10. Par application du diviseur de tension 
23
1 2 3 4
BD BC CD AC CA
ZZU U U U U Z Z Z Z      
d’où 
  
2 3 2 4 3 1
1 2 3 4 1 2
BD AC AC
Z Z Z Z Z ZU U U Z Z Z Z Z Z v
      
La tension 
BDU  et donc l’intensité mesuré dans la branche est alors nulle si 
2 4 3 1Z Z Z Z  
11. Pour le pont de Hay : 
1 11Z jL R   ; 
2 2ZR  ; 
3 3
3
1ZR jC  ; 
4 4ZR  
12. L’équilibre se traduit alors par
  11
2 4 3 1 1 1 3 3 1
3 3 3
1 LRR R R R jL R R j R LjC C C 
                
       
On en déduit le système suivant en identifiant les parties réelles et imaginaires 
1
1 3 2 4
3
1
31
3
0
LR R R RC
RRL C 
 
   
La résolution donne alors 
24
1
3 22
33
224
1
22
33
3
1,91
9,0.101
RRR
R RC
RRLH
RC C



   


    
Problème 2 : trains à sustentation magnétique. 
1. Pour l’association en série des trois composants soumis à la tension e(t). 
On applique le diviseur de tension pour obtenir 
1
12
1
L
L L R
Zue Z Z Z    
d’où 
 
1
1
12
jLue j L L R

   et 
 
2
2
12
jLue j L L R

   
2. Pour un modèle idéal d’ALI, la résistance d’entrée tend vers l’infini  et les intensités des courants i+ 
et i- dans les bornes d’entrée inverseuse et non inverseuse sont nulles . La résistance de sortie tend 
vers zéro , l’intensité sortant par la borne de sorti e est limitée à la valeur i sat prenant typiquement la 
valeur de 25mA. 
3. On peut faire l’hypothèse d’un fonctionnement linéaire de l’ALI car il y a une boucle de rétroaction 
sur la borne d’entrée inverseuse. On peut alors écrire la relation V +=V-. 
4. On peut évaluer le potentiel de la borne non inverseuse par un diviseur de tension car l’intensité entrant 
dans l’ALI par cette borne est nulle d’où 
1
1
2Vu 

--- Page 3 ---

Corrigé DS3 PCSI2 2022-2023 
physique 
3/5 
On peut alors faire une loi des nœuds en terme de potentiel à la borne d’entrée inverseuse en tenant compte du 
fait que l’intensité entrant dans l’ALI à cette borne est nulle :
2
22
0SV u V u
RR
   
En combinant les deux équations, on obtient alors 
12Su u u  
5. On obtient avec le résultat de la q4 et celui de la q1 : 
 
 
12
12
S
j L Lue j L L R


   
On l’écrit sous la forme 
 
 
 
12
121
S
LLju RT j e LLe j R




   à identifier avec 
 
1
O
O
O
jT
Tj
j






 
  
Ce qui donne 
121
O
LL
R
  et 
12O
O
T LL
R
  ce qui donne 
12
O
R
LL    et 
12
12
O
LLT LL
   
En reprenant les expressions fournies pour L1 et L2, on obtient alors 
2
O
e
R
L   et 
O
zT 
  
6. HF, 
  OT j T   alors 
  OGT   ; 
  20log OGT   et 
   arg OT   
BF, 
  O
O
jT j T  
 
  alors 
  O
O
GT  
 
  , 
  20log 20logO
O
GT  
 
  et 
   arg 2
OT    
En ω=ωO : 
  1
O
O
jTTj j    alors 
  2
O
O
TG    ; 
  20log 3OOG T dB   et 
   arg 4
OO T    
7. 
         
  
Il s’agit d’un filtre passe haut d’ordre 1, dont la fréquence de coupure s’identifie avec la fréquence propre. 
La bande passante s’étend alors sur l’intervalle [fO, +∞[. 
8. Pour que la fonction de transfert soit indépendante de la fréquence, il faut travailler à haute fréquence et 
alors 
  O
zT j T 
  la fonction de transfert est bien réelle. 
9. La fréquence de coupure du filtre s’exprime 
24
O
O
e
Rf L

  A.N : 
1,0Of kHz , on peut donc estimer 
que f=4kHz est dans le domaine HF pour lequel 
O
zTT 
  
On en déduit que 
S
zue 
  et par retour aux notations réelles 
 cosS
zzu e E t 
  On obtient
0   
10. Le circuit multiplieur fournit la tension 
 
22( ) ( ) ( ) cosmS
zs t Ku t e t K E t 
  
11. Il faut linéariser l’expression précédente : 
 
22( ) ( ) ( ) cos 2 22
mS
zzs t Ku t e t K E K E t 
    
On obtient donc deux composantes : 
 Une composante continue (donc de fréquence nulle) d’amplitude 
2
2
m
zS K E 
  
 Une composante de fréquence 2f de phase à l’origine nulle et d’amplitude 
2
2
zKE


--- Page 4 ---

Corrigé DS3 PCSI2 2022-2023 
physique 
4/5 
12. On doit extraire la composante de fréquence nulle d’un signal comportant cette composante et une 
coposante sinusoïdale de fréquence 2f. Il faut utiliser un filtre passe bas, dont la fréquence de coupure 
est nettement inférieure à 2f. 
13. La sensibilité du capteur s’exprime alors 
2
2
mS K Ez   
Le plus petit déplacement détecté sera alors exprimé par 
,min 4
2
2 5,6.10
mSz
KE
  soit un écart à la position 
moyenne d’1/2 millième de l’écartement total !! 
Problème 3 : lissage d’une tension hachée. 
A. Tension en sortie du hacheur. 
1. La valeur moyenne est définie par 
1 ()
O
O
tT
T
t
e e t dtT

   alors ici 
0
1 0
TT
T
T
e Edt dt ET


  
  
2. On retrouve la valeur moyenne du signal en relevant la composante constante dans le développem ent en 
série de Fourier qui est bien égal à αE. 
3. Il faut conserver la composante continue et éliminer les autres composantes de fréquences plus grandes, 
on va donc employer un filtre passe bas , de fréquence comprise entre 0 et f, la fréquence du 
fondamental de la décomposition. 
B. Cellule de lissage. 
4. On fait les schéma du circuit en comportement asymtotique : 
BF, le condensateur est un interrupteur ouvert, la bobine est un fil, alors s=e  
HF, le condensateur est un fil et la bobine un interrupteur ouvert, alors s=0. 
La cellule permet bien de réaliser l’opération de filtrage passe bas voulu.  
5. On associe C et R en parallèle pour obtenir : 
11 jCZR   
La fonction de transfert étant toujours calculer en sortie ouverte, on effectue un diviseur de tension po ur obtenir : 
L
Zse ZZ 
 ce qui donne 
  1
11
Hj
jL jC R


    et on identifie avec 
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
On obtient : 
1OH   ; 
2
1
O
LC   et 
1
O
L
QR   et finalement 
1OH   ; 
1
O
LC
   ; 
CQR L  
6. Définition : La pulsation de coupure ωC est la pulsation pour laquelle le gain est égal au gain maximum 
divisé par 
2 , ce qui revient à dire que le gain en décibel est égal au gain en décibel maximum -3dB. 
  max
2
C
GG  
 soit 
  ,max 3dB C dBG G dB   
Puisque 
1
2
Q , il n’y a pas de résonnance et donc 
max OGH  .  
De plus le calcul donne 
 OOG QH   donc lorsque 
1
2
Q
  2
O
O
HG    et la pulsation propre 
s’identifie bien avec la pulsation de coupure 
OC . 
On en déduit que 
1
2
CR L  ce qui donne 
1002
LR C    
La fréquence propre qui donne la fréquence de coupure est alors 
21 1,1.10
2
Of Hz
LC
  
C. Lissage de la tension hachée. 
7. Puisque f O=1,1.102Hz est inférieu re à la fréquence f du fondamental du développement en série de 
Fourier, on peut supposer en première approximation que le fondamental et les harmoniques du signal 
sont entièrement éliminées du signal en sortie.

--- Page 5 ---

Corrigé DS3 PCSI2 2022-2023 
physique 
5/5 
Le signal en sortie est alors (quasi) constant. On pe ut déterminer son amplitude en appliquant la fonction de 
transfert sur la composante constante du signal en entrée ce qui donne  
 0.O TS G e E    en tenant compte 
de HO=1. 
8. On calcule les amplitudes du fondamental et de l’harmonique de rang 2 par le même principe que 
précédemment. On suppose qu’on peut employer la forme asymptotique HF pour déterminer le gain 
pour ces deux composantes ce qui donne : 
   
2
11
2. sin O
O
f ES G f E H f 
 
  et 
   
2
22 2 . sin 2 2
O
O
f ES G f E H f 
   
Alors 
 
 
22
1
sin 2 7,8.108 sin
S
S


  L’amplitude du fondam ental est alors environ 13 fois plus grande que 
celle de l’harmonique de rang 2, il est donc raisonnable de négliger l’influence de l’harmonique sur le taux 
d’ondulation résiduelle. 
9. On peut exprimer les grandeurs 
max 1 OS S S  et 
min 1 OS S S  d’où 
 
2
1 sin2 O
O
fS
Sf
 
   
L’évaluation numérique donne  
21, 2.10   la tension sera donc quasiment continue avec des variations de 
valeurs de l’ordre de 1,2% de la valeur moyenne. Le lissage semble donc correctement ré alisé même si il faudrait 
en fait avoir une idée de la tolérance du moteur sur ce paramètre. 
Analyse d’un diagramme de Bode en amplitude. 
 Tracer les asymptotes BF (on obtient une pente de +20dB/dec) et HF (on obtient une pente de -
20dB/dec). On en conclut qu’on a affaire à un passe bande d’ordre 2. 
 La fonction de transfert s’écrit sous la forme 
  2
1
O
O
O
HHj
ffjQ ff
 
 
  
Le comportement asymptotique BF donne alors
  20log 20log 20logdB O
O
fG f H Q f
   
  
Le comportement asymptotique HF donne alors
  20log 20log 20logdB O
O
fG f H Q f
   
  
Les deux se croisent donc en f=fO pour une ordonnée égale à 
20log 20logOHQ  
 On en déduit par lecture graphique que la fréquence propre est fO=5kHz. 
Le comportement à la fréquence propre donne 
  20logdB O OG f H   
 Par lecture graphique 
  0dB OGf   et on en déduit que le gain statique vérifie |HO|=1. 
 Par lecture graphique à l’intersection 
20log 20log 20OH Q dB   on en déduit que le facteur de 
qualité est Q=10.