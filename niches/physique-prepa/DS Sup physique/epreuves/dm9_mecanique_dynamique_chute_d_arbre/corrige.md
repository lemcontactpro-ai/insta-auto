# corrigé du DM9 mécanique dynamique chute d'arbre


--- Page 1 ---

Corrigé du DM9 PCSI2 2022-2023 
physique 
1/3 
Problème 1 : Chutes d’arbres. 
a. Etude de l’arrachement d’un arbre mort par un bûcheron. 
 
1. Le bilan des actions mécaniques sur le bucheron vu 
comme un point matériel est : 
 Action de la gravité de vecteur force 
2 zP mgu
  
 La force de traction 
F
  
 La réaction du sol 
2 2 2 zxR N u T u
  
On écrit la condition d’équilibre pour le bucheron 
22 0P F R  
 et on la projette sur les directions
xu
  et 
zu
  d’où 
2 cosTF 
 et 
2 sinN F mg    
Les lois de Coulomb affirment alors que l’équilibre est possible 
si 
22T fN  d’où 
max
cos sin
fmgFF f   
2. On fait le bilan des actions mécaniques sur l’arbre vu comme un solide : 
 Action de la gravité de vecteur force 
1 zP Mgu
  vue comme un glisseur appliqué en G le centre d’inertie. 
 La force de traction 
F
 vue comme un glisseur appliqué en C le point d’attache. 
 La réaction du sol 
1 1 1 zxR N u T u
  vue comme un glisseur appliquée en O le « centre de rotation ». 
On obtient alors
1 cosTF   et
1 sinN F Mg  . 
L’équilibre est maintenu et il n’y a pas de glissement tant que 
 11T fN  soit 
'
max
cos sin
fMgFF f  . 
On constate aisément que 
'
max maxFF   et donc que le glissement a lieu d’abord pour le bucheron. Le glissement est 
donc impossible en O tant que 
max0 FF  
3. Pour l’action mécanique de gravité, le modèle de glisseur revient à applique r la résultante sur le centre 
d’inertie G de l’arbre situé en son centre de coordonnées dans la base cartésienne 
2
xz
HOG au u 
 . 
Le moment associé par rapport à
 , yOu
  est  
 1 .gy OG P u  
  ce qui donne 
 1 .gy OG P u Mga   
 . 
4. Le bilan des moments par rappor t à 
 , yOu
  se limite à celui exercé par le bucheron et à celui de la gravité 
puisque la réaction du sol est supposée appliquée en O et que son moment est donc nul.  
Pour que l’arbre commence à tourner autour de 
 , yOu
 , il faut donc que 
0Bg    d’où 
B Mga . 
5. Le moment exercé par le bucheron s’écrit 
     . sin cos sin .B y z x z yOC F u l u F u F u u        
   
Finalement 
 sin cos sin 2 2
B
FlFl      . Le moment exercé par le bucheron est alors maximal pour la valeur 
d’angle 
4
m
   
6. On suppose F=Fmax ce qui donne
sin cos
cos sin
B
fmgl
f

  c’est-à-dire
 
B
mgl
   avec
  11
sin cosf    . 
Le moment est maximal quand 
   est minimal. 
  22
cos sin
sin cos
d
df
  
 
 qui s’annule si 
33cos sin 0f  il y a donc un extremum de 
   quand 
 
3 1tan m
f 
. Je vais supposer que c’est un minimum et que la solution cherchée est 
1
3arctanm f
 
  
On vérifie bien que 
4
m
   pour f=1. 
7. L’A.N donne 
2
max 7,07.10FN   
La longueur de corde s’exprime en reprenant les résultats
max
2 14Mgalm F  soit une longueur inférieure à H… 
La force correspond à soulever 70kg ce qui est tout de même important (c’est un bucheron donc…). La longueur 
de corde interroge sur le devenir dudit bucheron lorsque l’arbre tombera…

--- Page 2 ---

Corrigé du DM9 PCSI2 2022-2023 
physique 
2/3 
 
8. A partir du schéma
2
r
HOG e ae 
  et donc 
cos sin2
G
Hza   
On cherche à écrire cette relation sous la forme donnée 
 cos cos cos sin sinGz A A A         
 
On en conclut que 
cos2
sin
H A
aA


 
   ce qui donne 
2
22
2
2 tan
H aA
a
H 
 
   
En prenant β sur [0,π/2[,
221 42A H a  ; 
2arctan a
H    
On obtient bien finalement 
2212 4 cos arctan2
G
az H a H       
9. L’énergie potentielle de pesanteur s’exprime alors
22 24 cos arctan2
PG
Mg aE Mgz H a H        
Cette énergie potentielle passe par un maximum quand 
2cos arctan a
H     passe par un maximum. 
On en déduit que 
2arctanS
a
H   , si θ<θ S et que le bucheron lâche le câble, l’arbre retombe sur sa base, si θ>θ S 
et que le bucheron lâche le câble, l’arbre tombe vers le bucheron (et même sur le bucheron  car l<H). 
Pour l’A.N
3S   
10. Bilan des actions mécaniques : Gravité 
 1 . sin 2
gy
HOG P u Mg    
  ; pivot idéal 
0pivot  
Le théorème du moment cinétique par rapport à 
 , yOu
  donne : 
sin2
HJ Mg
  d’où 
3 sin2
g
H
  
11. On obtient la vitesse en multipliant l’équation du mouvement par 

  et en intégrant : 
3 sin2
g
H  
 d’où 
213 cos22
d d g
dt dt H         
  et on intègre de l’état initial (θS,0) à l’état (θ, 

 ) ce qui donne  
 
213 0 cos cos22
S
g
H    
 et donne le résultat fourni 
 3 cos cosS
g
H  
  
12. Pour obtenir la durée de chute, on intègre par séparation des variables l’expression de la vitesse de rotation  : 
 
/2
0
3
cos cos
C
S
t
S
dg dtH






 ce qui donne 
54 3
C
Hts g  une durée à la fois longue et courte, ça dépend 
des réflexes et de la capacité de sprint du bucheron en environnement boisé.  
b. Etude de l’arrachement d’un arbre vivant par le vent. 
 
13. En ordre de grandeur pou r un vent violent, on peut proposer une vitesse de 100km.h -1 ce qui correspond à 
peu près à 30m.s-1. 
14. Le calcul donne 
   
2. 2 .v y Z x a x yd OM dF u zu aC U dzu u     
  d’où
22v x ad aC U zdz  
15. En intégrant sur toute la hauteur de l’arbre on obtient
2
0
2
H
v v x a
arbre
d aC U zdz      soit
22
v x a aC U H  
16. Avec l’inclinaison, la hauteur de l’arbre devient Hcosθ et si on ne tient compte que de cet effet
2n … 
17. Le couple 
2
245rO
CC
 
   
  prend pour valeur 
.rO     en θ=0+ et l’énoncé impose Γr(0+)=ΓO. 
On en déduit donc que 
1   
Ensuite, 
2
21 4 5rO
CC


   
  s’annule en θ=θC, on prendre donc 
10C    d’après la courbe. 
On détermine alors l’angle θm en cherchant le minimum du couple par annulation de la dérivée par rapport à θ. 
4 10Or
CC
d
d

  
  

 ce qui donne 
2
5
mC  on observe bien que θ m ≈ 4° sur la courbe en cohérence avec le 
modèle.

--- Page 3 ---

Corrigé du DM9 PCSI2 2022-2023 
physique 
3/3 
Le minimum du couple est alors 
  9 1,85
r m m O O       
18. Si 
1v
O
p    le couple exercé par le vent e st insuffisant pour incliner l’arbre qui reste donc en place, cet 
équilibre est alors stable. 
Si 
1 1,8p  le couple exercé par le vent est suffisant pour incliner l’arbre mais celui -ci ne sera pas déraciner 
puisque le couple de rappel des racines s’oppose au couple du vent. 
Si p>1,8 le couple racinaire ne peut pas compenser le couple exercé par le vent et il y a déracinement.  
19. Pour 
1 1,8p  il y a deux positions de l’arbre pour lesquelles les couples des racines et du vent se 
compensent, la première pour θ1<θm et la seconde pour θ2>θm. 
Pour θ 1 si l’angle augmente légèrement, le couple résistant augmente et ramène l’arbre en θ 1, cette position est 
stable. 
Pour θ 2 si l’angle augmente légèrement, le couple résistant diminue et le ve nt repousse l’arbre plus loi n, cette 
position est instable. 
20. Pour une position d’équilibre inférieure à θ m à priori stable, il est possible que l’énergie cinétique accumulée 
depuis la position verticale soit suffisante pour entrainer une sortie du puit de p otentiel.