# corrigé du DM3 élec optique lunette astronomique


--- Page 1 ---

Corrigé DM3 PCSI2 2022-2023 
physique 
1/3 
Problème 1 : Modélisation d’un générateur. 
Un générateur peut être étudié grâce à la 
modélisation de Thévenin. 
Le circuit proposé est le suivant. 
L’équation caractéristique associée est 
U e rI  
où e est la force électromotrice de la source  de 
tension idéale et r est la résistance interne du 
générateur.  
On peut alors exploiter les valeurs données dans l’énoncé pour obtenir :
2* 22
1, 2* 30
er
er

    
on obtient alors les valeurs numériques suivantes pour la fem et la résistance : 
10
42
r
eV

   
Problème 2 : Etude d’un défibrillateur. 
Charge du défibrillateur. 
1. On applique la loi des mailles dans le circuit : 
( ) ( ) 0RcE u t u t    
Les équations caractéristiques des dipôles donnent alors : 
( ) . ( )RU t R i t   
( ) ( ) cdui t C t dt  
Dans la loi des mailles on obtient alors l’équation différentielle :
11( ) ( )C
c
du t u t Edt   avec 
RC   
2. Les solutions de l’équation différentielle déterminée précédemment sont de la forme  : 
)()( tSStS HP 
 avec : 
PSE  et 




 
tAtS H exp)(  
On applique la condition initiale donnée par la charge nulle du condensateur avant que l’interrupteur K 1 soit 
fermé et par la continuité de la tension aux bornes d’un condensateur : 
0 EA  
La tension aux bornes du condensateur s’exprime alors : 
( ) 1 expc
tu t E 
       
3. On trace la tangente à l’instant initial de la courbe représentative et on observe à quel instant cette 
tangente passe par l’ordonnée uTagente(τ)=E ce qui donne ici : 
0,5s   
On peut aussi déterminer l’instant pour lequel 
 ( ) 1 0,63.cu E e E    ce qui donne évidemment le même 
résultat
0,5s  . On en déduit 
1,1Rk C
    
4. L’énergie stockée dans un condensate ur s’exprime
21
2
Stockée cE Cu  ce qui donne en fin de charge 
2
,
1
2
StockéeE CE  
 A.N : 
2
, 5,29.10StockéeEJ    
Décharge du défibrillateur. 
5. On reprend la démarche de la q1. 
On applique la loi des mailles dans le circuit : 
( ) ( ) 0Rc cu t u t   
Les équations caractéristiques des dipôles donnent alors : 
( ) . ( )RCU t R i t   
( ) ( ) cdui t C t dt  
Dans la loi des mailles on obtient alors l’équation différentielle :
1( ) ( ) 0C
c
C
du t u tdt   avec 
CC RC   
6. Les solutions de l’équation différentielle homogène sont de la forme : 
( ) expH
c
tS t A 
 
  
On applique la condition initiale donnée par la tension avant que l’interrupteur K 2 soit fermé et par la continuité 
de la tension aux bornes d’un condensateur : 
 cOu t E   
La tension aux bornes du condensateur s’exprime alors : 
( ) expc
c
tu t E 
 
  
r I 
U 
A B 
e

--- Page 2 ---

Corrigé DM3 PCSI2 2022-2023 
physique 
2/3 
7. On observe que la tension arrête sa décroissance à l’instant t 1 lu pour la valeur 
1 16,5t ms  et la tension 
aux bornes du condensateur est alors 
1( ) 750cu t V   
8. On souhaite qu’une énergie W soit délivrée et donc l’énergie restant dans le condensateur après 
décharge sera : 
 
2
1
1
2
stockéeE t CE W   d’où 
 
22
1
2
C
Wu t E C  et 
 
2
1
2 740C
Wu t E V C    
L’instant t1 est tel que 
21
1
2( ) expc
c
t Wu t E E C
   
  ce qui donne 
1 2
2ln 1 16,6c
Wt ms CE     
 
Problème 3 : Etude d’une lunette astronomique. 
1. Lorsque l’œil observe des images sans accommoder, on réduit fortement la fatigue oculaire car il n’y 
pas d’effort musculaire sur le cristallin. 
L’image finale A 2B2 est alors nécessairemen t située à l’infini puisque c’est le point observé par un œil 
emmétrope sans accommodation. 
La lunette fait donc d’un objet à l’infini une image à l’infini, il s’agit d’un système afocal.  
2. L’image intermédiaire est conjuguée d’un point objet à l’infini et s e forme donc dans le plan focal 
image de l’objectif. 
Pour que l’oculaire en fasse une image renvoyée à l’infini, elle doit se située dans le plan focal objet de 
l’oculaire. 
On en conclut que A1=F1’=F2, et donc que 
1 2 1 1 1 2 1 1 2 2 'O O O A A O O F F O      
Finalement : 
12''ff   A.N : 
10 710mm  et 
25 725mm  
3. Schéma de la lunette :  
 
4. Dans le triangle O1I1F1 : 
11
1
tan '
AB
f   ; Dans le triangle O2I2F2 : 
11
2
2
tan '
AB
f   
Dans les conditions de Gauss, tanα≈α et tanα2≈α2 d’où : 
21
2
'
'
fG f

  A.N : 
10 70G   et 
25 28G   
5. On constate pour la lunette astronomique que le grossissement est très important et qu’il est négatif.  
Pour ce type d’instrument il est alors contre -intuitif de se déplacer dans le champ d’observation puisqu’un objet 
vu à gauche en sortie de lunette est en fait à droite dans le champ d’observation. De plus le fort grossissement 
rend le champ observé très instable quand on bouge la lunette à la main. Le che rcheur est une lunette de moindre 
grossissement en valeur absolue mais de grossissement positif  qui permet de se repérer dans le ciel et de 
recadrer le champ d’observation de la lunette plus facilement que par une observation directe dans la lunette.  
6. Pour déterminer
2 'FC  avec C conjugué de O1 par l’oculaire : 
On constate qu’on connait
2 1 1 1 1 ''F O F O f   et par une relation de conjugaison de Newton, on obtient  : 
2
2 2 1 2''F CF O f 
 ce qui donne : 
2
2
2
1
'' '
fFC f  
7. Pour obtenir le diamètre de ce cercle oculaire, on écrit alors une relation de grandissement avec origine 
au foyer image : 
2
12
'
'
Ca FC
af   . On constate que le grandissement est négatif et que le diamètre 
du cercle oculaire s’exprime alors : 
2
1
1
'
'
C
faa f  
B1 
B 
F1’ = F2=A1 
F1 F2
’ 
B2 
α2 
A 
A2 α O1 O2 
I1 I2

--- Page 3 ---

Corrigé DM3 PCSI2 2022-2023 
physique 
3/3 
8. A.N : 
,10 1Ca mm   et 
,25 2,5Ca mm . Ces deux valeurs sont bien comprises entre a min et a max. La 
lunette est donc bien conçue pour ces deux objectifs. 
On envisage maintenant d’utiliser la lentille de Barlow, qui est une lentille  divergente de distance focale f B’ et 
qui permet d’obtenir un grossissement multiplié par deux des objets célestes observés.  
9. La lentille de Barlow est divergente, on peut en conclure que sa distance focale sera négative.  
10. Dans le système à trois lentilles on a maintenant : 
12
1 1 2 2, ' BL L L
BA A F A F A         
A1’ est situé en F1’ et AB situé en F2 et les deux foyers ne sont donc plus superposés. 
11. Le grandissement de la lentille de Barlow est : 
 
2,2
111
' 1
'
BBB
B
fAB rGfGAB
 
    d’où 
B r   
12. On utilise la relation de grandissement avec origine aux foyers : 
2
1
''
' '
BB
B B
fFFr f FF
    
D’où 
2''BBF F rf  ; 
1
1''BBF F f r   
13. On établit la première distance par la relation de Chasles : 
1 1 1 1 1
1' ' ' 'B B BF O F F F O f f r     
Et la seconde par la relation de conjugaison avec o rigine aux foyers pour la lentille de Barlow  : 
2
11. ' 'B B B BF O F O f 
 d’où 
2
2 1 2 1
1
'' ' ' ''
B
B B B B B
B
fF O F F F O rf ff r
   
   et 
2
1
21
1
''
''
B
B
B
r f fFO rf f   
14. On exploite les relations de grandissement avec origine aux foyers  : 
,, 22
1 1 1 2 1 1
' ' '. '
C B C B BB
B BB
aa a f f f
a a a rf F O F O
  
 ce qui donne bien 
,
C
CB
aa r  
15. On obtient un cercle oculaire de diamètre
, ,10 0,5CBa mm   pour l’oculaire de focale 10mm pour un 
grossissement de -140. On reste dans l’intervalle autorisé pour le diamètre du cercle oculaire.  
On obtient un cercle oculaire de diamètre
, ,25 1,25CBa mm   pour l’oculaire de focale 25mm pour un 
grossissement de -56. On reste dans l’intervalle autorisé pour le diamètre du cercle oculaire.  
La lentille de Barlow x2 est donc bien adaptée pour les deux oculaires et l’ensemble proposé est donc cohé rent. 
16. Pour une lentille de Barlow x3, le diamètre du cercle oculaire serait de 
, ,10 0,33CBa mm   trop petit 
pour l’oculaire de 10mm et il serait donc contre-productif d’envisager un tel équipement.  
Le diamètre du cercle oculaire serait de pour 
, ,25 0,83CBa mm   toujours acceptable pour l’oculaire de 25mm 
pour un grossissement comparable à celui obtenu pour l’oculaire de 10mm. 
Dans tous les cas, il semblerait peu rentable d’investir dans cette optique supplémentaire et un sage conseil serait 
de l’inciter à renoncer à son achat.