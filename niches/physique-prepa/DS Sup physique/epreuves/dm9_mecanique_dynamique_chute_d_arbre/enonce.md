# DM9 mécanique dynamique chute d'arbre


--- Page 1 ---

DM9 PCSI2 2022-2023 
physique 
1 
Problème 1 : Chutes d’arbres. 
a. Etude de l’arrachement d’un arbre mort par un bûcheron. 
Un bucheron assimilé à un p oint matériel B de masse m souhaite 
abattre un arbre mort assimilé à un cylindre homogène de masse 
M>m, de hauteur H et de section droite carrée de coté 2a 
représenté sur la figure ci contre. 
Pour cela, il tire sur un câble fixé à l’arbre en C, de longueur  BC=l 
et de masse négligeable, afin de faire tourner l’arbre autour de 
l’axe 
 , yOu
  dirigé par le vecteur 
y z xu u u
 . 
L’arbre étant mort, on néglige l’action de ses racines, de telle sorte qu’au mom ent où l’ arbre commence à 
tourner, les action s de contact qu’il subit se limitent à une force de réaction 
1 1 1 xzR T u N u
  appliquée en O et 
satisfaisant aux lois de Coulomb avec un coefficient de frottement f. De même, les actions du sol sur le bûc heron 
sont décrites par une force 
2 2 2 xzR T u N u
 appliquée en B et satisfaisant aux lois de Coulomb avec le même 
coefficient de frottement f. On notera que N 1, N 2, T 1, T 2 sont des grandeurs algébriques, le câble est supposé 
tendu. On note
F
  la force exercée par le câble sur l’arbre au point C, supposée parallèle au câble et F sa norme. 
Les angles sont orientés positivement dans le sens trigonométrique autour de
 , yOu
  c’est-à-dire le sens horaire 
de la figure et on note finalement α l’angle (positif) entre 
BO
  et 
BC
 . 
On rappelle les lois de Coulomb  : un solide en contact  ponctuel sur un support subit des actions de contact 
équivalentes à une force
R
 décomposée en une composante normale 
N
 et une composante tangentielle
T
 . 
 En l’absence de glissement, on vérifie 
T f N
 où f est le coefficient de frottement. 
  En présence de glissement, la composante tangentielle est dirig ée dans la direction oppos ée à  celle du 
vecteur-vitesse de glissement et on vérifie 
T f N
 . 
On suppose que l’arbre est immobile dans la position verticale initiale. 
1. Le bucheron  est supposé ne pas glisser dans la situation initiale décrite par la figure  ci-dessus. 
Exprimer N2 et T2 en fonction de F, α, m et g. En déduire l’expression de F max le maximum de F pour  que 
cet équilibre soit possible en fonction de f, m, g et α. 
2. L’arbre est supposé au repos dans la situation initiale décrite par la figure  ci-dessus. Exprimer N1 et T1 
en fonction de F, α, M et g. En déduire que pour 0<F<F max, le glissement n’est pas possible en O. 
3. Rappeler en quoi consiste le modèle de glisseur appliqué à  l’action mécanique de gravité sur l’arbre. 
Préciser les coordonnées du centre de masse puis e xprimer le moment Γ g de l’action de gravité sur l’arbre 
par rapport à l’axe 
 , yOu
  dans la situation initiale.  
4. Soit ΓB le moment par rapport à l ’axe
 , yOu
  exercé par le bûcheron sur l’arbre via le câble.  Quelle est la 
valeur minimale qu’il doit prendre pour permettre à l’arbre de pivoter  dans le sens horaire  autour de 
l’axe
 , yOu
  ? 
5. En supposant F constant, justifi er qu’il existe une valeur  optimale α m de l’angle α rendant le moment 
maximal. 
6. On suppose maintenant que, quel que soit l’angle α, l’action du bûcheron est telle que l’on est à la 
limite du glissement  : F prend donc la valeur F max. Montrer que le moment Γ B par rapport à l’axe
 , yOu
  
exercé par le bûcheron via le câble s’écrit
 
B
mgl
  où
  11
sin cosf    . En déduire l’expression de α m 
en fonction de f. Vérifier que αm=π/4 pour f=1. 
7. On donne g=10m.s-2, M=103kg, H=20m, a=0,5m, m=10 2kg et f=1. Calculer la force Fmax et la longueur de 
corde l nécessaires pour initier la rotation de l’arbre. Commenter. 
 
On suppose que l’arbre a commencé sa rotation autour de l’axe
 , yOu
 , repéré 
par l’angle θ que fait 
OC
  avec
 , yOu
 . 
8. Faire un schéma de la situation et montrer alors que l’altitude du centre 
d’inertie G de l’arbre, supposé de masse volumique constante, s’exprime 
2212 4 cos arctan2
G
az H a H     
. 
9. En déduire l’expression de l’énergie potentielle de pesanteur et en déduire l’angle θS pour lequel le bucheron 
peut lâcher le câble pour laisser l’arbre tomber… (de son côté, même si ce n’est pas très malin).  Faire 
l’application numérique.

--- Page 2 ---

DM9 PCSI2 2022-2023 
physique 
2 
On suppose maintenant que l’arbre est en rotation autour de l’axe 
 , yOu
 , axe autour duquel la liaison pivot est 
supposée parfaite, sous la seule action de la gravité. On néglige alors la largeur a de l’arbre devant sa hauteur H. 
On note 
21
3J MH le moment d’inertie de l’arbre par rapport à l’axe
 , yOu
 . 
10. Etablir l’équation du mouvement de rotation de l’arbre autour de l’axe 
 , yOu
 . 
11. En déduire que la vitesse de rotation de l’arbre s’écrit sous la forme :
 3 cos cosS
g
H  
 . 
12. En déduire l’expression de la durée de chute de l’arbre. Faire l’application numérique pour H=20m.  
On donne 
/2
5,0
cos cos
S S
d





  
b. Etude de l’arrachement d’un arbre vivant par le vent. 
Dans cette partie, on s’intéresse à la chute d’un arbre vivant, de hauteur H, sous l’effet d ’un coup de vent violent. 
On néglige le rô le du poid s de l’arbre : son mouvement résulte uniquement d’une compé tition entre l’action du 
sol via les racines et l’action du vent. 
13. Proposer un ordre de grandeur de la vitesse minimale U pour un « vent violent » en km/h puis en m.s-1. 
 
L’arbre étant pris dans sa position initiale verticale  comme sur la figure ci-
contre, on suppose que la force exercée par le vent sur une portion de l’arbre 
située entre les altitudes z et z+dz s’exprime 
22v x a xdF aC U dzu
  où ρa est 
la masse volumique de l’air et Cx un coefficient aérodynamique. 
14. Exprimer le moment élémentaire dΓ v par rapport à 
 , yOu
  associé à la 
force 
vdF
 . 
15. Montrer alors que le moment résultant s’exprime 
22
v x a aC U H . 
 
Lorsque l’arbre commence à pencher, on repère son mouvement par l’a ngle θ 
représenté sur la figure ci -contre. Le moment Γ v(θ) varie en fonction de θ et 
on constate qu’il est proportionnel à 
 cos
n
 où n est un entier. 
16. Proposer une valeur de n en justifiant votre réponse. 
Dans la suite, on néglige la dépendance de Γ v par rapport à θ car l’angle reste 
petit, et on l’identifie avec sa valeur en θ=0 (position verticale de départ).
 
L’action du sol sur l’arbre est décrite par un moment 
résistant Γ r par rapport à l’axe
 , yOu
  qui met en jeu des 
phénomènes complexes à modéliser. On effectue donc un 
relevé expérimental, par traction à l’aide de câble, dont la  
courbe d’évolution est donnée ci -contre en fonction de θ. 
Cette figure fait notamment apparaître une variation brutale 
au voisinage de θ=0 que l’on modélise par une discontinuité 
telle que Γ r(0)=0 et Γ r(0+)=ΓO. Par ailleurs, au -delà d’un 
certain angle θ C, l’arbre est totalement déraciné, de telle 
sorte que Γr(θ>θC)=0. 
Dans le domaine 0<θ<θ C, on modélise les mesures 
expérimentales de Γ r par un polynôme du deuxième degré 
de la forme 
2
245rO
CC
 
   
  avec 
0O . 
17. Quelles valeurs doit -on donner aux paramètres θ C et β afin qu’il rende compte des mesures  ? Exprimer 
l’angle θm pour lequel Γr atteint sa valeur « minimale » et exprimer ce minimum. Vérifier la cohérence entre 
les résultats expérimentaux et les valeurs issues du modèle. 
Du point de vue dynamique, l’arbre est assimilé à une barre mince en rotation autour de l’axe
 , yOu
  avec un 
moment d’inertie J, soumis au moment Γ v constant et au moment Γ r(θ) décrit par le modèle précédent. 
Initialement le modèle est au repos e n θ=0 en présence d’un vent de vitesse U indépendante du temps et on 
s’interroge sur son évolution. On définit 
v
O
p   . 
18. Discuter graphiquement selon la valeur de p la possibilité pour l’arbre de rester en équilibre en θ=0. Cet 
équilibre est-il stable ? 
19. Discuter graphiquement selon la valeur de p l’existence et la stabilité de positions d’équilibre en θ e≠0. 
20. Dans le cas où il existe une position d’équilibre inférieure à θ m, expliquer sans calcul pourquoi on ne peut 
néanmoins pas être certain que l’arbre résiste au vent.