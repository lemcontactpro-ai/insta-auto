# corrigé du DM1 optique snell descartes gaine


--- Page 1 ---

Corrigé DM1 PCSI 2 2022-2023 
Physique 
 1 
Exercice 1 : fibre optique. 
Question de cours : 
1. Les lois de Snell Descartes sur la réflexion : 
 Le rayon réfléchi appartient au plan 
d’incidence. 
 Le rayon réfléchi est symétrique du rayon 
incident, autrement dit, l’angle de réflexion que 
fait le rayon réfléchi av ec la normale à la 
surface est de même valeur absolue et de signe 
opposé. 
ri  
Les lois de Snell-Descartes sur la réfraction : 
 Le rayon réfracté appartient au plan 
d’incidence. 
 L’angle de réfraction que fait le rayon réfracté 
avec la nor male à la surface vérifie  : 
sin 'sin 'n i n i
 
Etude d’une situation de TP :  
2. Schéma : 
 
3. On est susceptible avec ce système 
expérimental d’observer le phénomène de 
réflexion totale sur l’interface plane plexiglass -
air, pour laquelle la lumière traverse dans le 
sens milieu le p lus réfringent vers le milieu le 
moins réfringent. 
La transmission d’un rayon est possible si  : 
sin sin 'plexin i i 
 le cas limite correspond à i=i L 
quand i’= π/2 ce qui donne  : 
1sin L
plexi
i n  et 
1arcsinL
plexi
i n

 
 
4. On évalue l ’indice optique en utilisant les lois de Snell-Descartes
sin '
sin
in i  et l’incertitude sur cet indice 
en exploitant la relation donnée 
2 2 2() pau n u u . A.N : 
1,40n  avec 
( ) 0,05un   
Etude d’une fibre optique à saut d’indice :  
5. Le rayon pénètre toujours dans la fibre en O car 
on passe de l’air au verre du cœur avec (1<n c). Ce 
rayon est alors réfléchi totalement sur l’interface  
cœur gaine (n c>ng) si l’angle d’incidence α est 
supérieur à iL ce qui est le cas si θ<θL. 
La condition de réflexion totale est 
sin g
LL
c
ni avec i n  . 
Dans le triangle rectangle, on obtient alors : 
' 2
      et donc 
' 2
  
On exploite alors la loi de Snell-Descartes 
 sin sin ' cosCCnn    
Lorsque α est minimal égale à i L pour assurer la réflexion totale, cosα est maximal et donc θ est majoré par une 
valeur θL telle que 
 sin sin cos L C L ni  
puisque 
 sin
g
L
c
ni n , 
 
2
cos 1
g
L
c
ni n
 
  alors
22sin sin L c g nn    d’où 
 
22arcsinL c g nn   
L’application numérique donne 
12L 

--- Page 2 ---

Corrigé DM1 PCSI 2 2022-2023 
Physique 
 2 
6. Le rayon le plus rapide est celui le long de l’axe de la fibre. On en déduit Lmin=L et 
1
cnLT c  
7. Le rayon le plus lent est celui incliné de l’angle θL’ tel que 
 cos ' sin
g
LL
c
ni n  . La distance parcourue 
est la somme des segments tous inclinés de l’angle θ L’ par rapport à l’axe de la fibre qu’on établit à 
Lmax=L/cos(θL’) ce qui donne 
2
2
c
g
nLT cn  
8. On en déduit 
21 1cc
g
n L nT T T cn

      A.N : 
75.10Ts   
9. On souhaite que les impulsions ne se recouvrent pas, il faut donc que la durée ΔT entre deux impulsions en 
entrée soit supérieure à l’étalement δT des impulsions lorsqu’elles traversent la fibre afin que la fin d’une 
impulsion arrive avant le début de l’impulsion suivante. 
On en déduit que  
minT T T     et donc 
 
max
1 g
c c g
ncff T n L n n  
  
10. Pour un débit fixé D, la longueur maximale de la fibre s’exprime 
 
2
max 2,0.10
g
c c g
ncLm
n D n n

  
Cette distance est bien trop courte pour que la t echnologie de fibre à saut d’indice permette le transport 
d’information à haut débit sur des distances nationales ou internationales. 
Quelques éléments sur une fibre à gradient d’indice :  
11. On évalue  
(0) 1,500cnn   ; 
( ) 1,485cgn r n
 et l ’allure ci -contre pour la 
courbe. 
12. On fait l’application numérique  : 
'2T ns   
qu’on doit comparer à 
75.10Ts  . δT’ est 
250 fois plus faible que δT et donc les fibres à 
gradient d’indice pourront être ininterrompues 
sur les distances d’environ 250.L max soit 
environ 50km. Cette technologie est déjà 
beaucoup plus employable dans un réseau à 
l’échelle nationale. 
Pertes associées à l’usage de la fibre optique 
13. On souhaite que 
210
f
i


 
 . Il faut donc que 
10
10 log
f
i
L A


 
  vérifie : 
max
20 100L L km A    
14. Sur la courbe fournie, on observe que l’atténuation est minimale lorsque la longueur d’onde de la lumière 
envoyée dans la fibre est proche de 1,6µm  ce qui explique l’emploi de lumière dans ce domaine pour 
minimiser les pertes de signal. Cette longueur d’onde de 1  ,6µm classe la lumière utilisé e dans le domaine 
des infra-rouge. 
 
15. Pour que la perte de courbure soit évitée il faut 
que l’angle d’incidence α sur l’interface cœur -
gaine reste supérieur à l’angle  limite iL. 
16. On observe que 
sin
gc
r
r r r     
et on rappelle que
sin
g
L
c
ni n  
Alors 
Li  implique 
sin sin Li  ce qui donne 
g
g c c
nr
r r r n    
d’où 
 min
g
gc
cg
nr r r r nn     A.N : 
min 10r cm . Dans une installation domestique, on évitera de tordre la 
fibre avec des rayons de courbure inférieur à cette valeur ce qui n’est pas toujours évident.