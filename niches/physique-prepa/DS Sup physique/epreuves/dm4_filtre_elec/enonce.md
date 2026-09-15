# DM4 filtre elec


--- Page 1 ---

DM4 PCSI2 2022-2023 
physique 
1/1 
Problème 1 : Filtre de Hartley. 
a. Etude de la fonction de transfert. 
On souhaite étudier la fonction de transfert 
  )(
)(
te
tsjH   du filtre de Hartley représenté sur la figure suivante. 
 
1. Déterminer qualitativement la nature 
probable de ce filtre. 
2. Montrer que la fonction de transfert peut se 
mettre sous la forme :  
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
 
Préciser les expressions du gain statique H O, de la 
pulsation propre ω O et du facteur de qualité Q en 
fonction de R, C et L. 
3. Donner la définition puis exprimer le gain en décibel GdB(ω) ainsi que la phase φ(ω) de ce filtre. 
4. Etudier les valeurs du gain en décibel et de la phase à la pulsation propre  puis les comportements 
asymptotiques lorsque 
0  et 
 . 
Le circuit utilisé présente les valeurs suivantes : L = 1,00 mH, C = 100 nF, R = 10,0 kΩ. 
5. Déterminer les valeurs numériques de H O, ω O et Q. Effectuer la const ruction du diagramme 
asymptotique en amplitude en précisant les coordonnées des points d’intérêt et les pentes des droites qui 
y figurent. 
6. Exprimer la largeur de la bande passante du filtre et faire l’application numérique. 
b. Effet sur un signal périodique. 
On envoie en entrée de ce filtre un signal créneau impair de période T =6π/ω O de moyenne nulle et d’amplitude 
E=2,0V. 
7. Faire une représentation graphique de ce signal. Définir et déterminer la tension efficace eeff associée. 
Ce signal étant périodique, il est décomposable en série de Fourier, et il peut alors être exprimé sous la forme  : 
  



0
12sin12
14)(
k
f tkk
Ete 
. 
8. Que représente le paramètre ωf ? Déterminer son expression en fonction de ωO.  
9. Déterminer les valeurs efficaces e k,eff pour chacune des composantes sinusoïdales de ce signal . puis 
représenter le spectre associé au signal e(t) en y faisant figurer les valeurs numériques des valeurs 
efficaces associées au fondamental et aux quatre premières harmoniques non nulles. 
10. Quelle(s) harmonique(s) sont situées dans la bande passante du filtre étudiée  ? En ne conservant que les 
harmoniques dans la bande passante du filtre, exprimer alors le signal en sortie du filtre . 
11. Déterminer quantitativement la valeur efficace s k,eff de la composante numéro k du signal en sortie du 
filtre. Faire les applications numériques pour 
 4,0k . 
12. Déterminer numériquement les rapports s 0,eff/s1,eff et s 2,eff/s1,eff. Evaluer alors grossièrement le taux de 
distorsion défini par la formule approchée 
eff
effeff
s
ss
,1
,1  du signal de sortie en ne tenant compte de ses 
trois premières composantes. 
c. Effet sur un échelon de tension. 
13. A partir de la fonction de transfert, déterminer l’équation différentielle vérifiée par la tension de sortie 
s(t) lorsqu’on impose en entrée du filtre un signal e(t) quelconque. 
On suppose maintenant que la tension d’entrée est un échelon de tension passant de la valeur nulle à la valeur E à 
l’instant t=0. 
14. Déterminer l’équation différentielle vérifiée par s(t) sur l’intervalle ]0, +∞[. 
15. En tenant compte de la valeur du facteur de qualité déterminé à la question 5, donner l’expression 
générale des solutions de cette équation, on introduira un temps d’amorti ssement τ et une pseudo -
pulsation ωe dont on précisera les expressions en fonction de Q et ω O.  
16. Vérifier que ωe≈ωO et évaluer numériquement ωe et τ.  
Il faut maintenant déterminer les conditions initiales respectées par le signal s(t). 
17. Montrer qu’à l’instant t=0, le circuit se ramène à un simple circuit RC. Etudier alors la réponse de ce 
circuit RC sur l’intervalle ]0, +∞[ et d éterminer la valeur de u A(t=0+) et 
)0( tdt
duA . En déduire que 
s(t=0+) = 0 et de 

Etdt
ds   )0( . 
18. Déterminer les expressions des constantes introduites à la question 1 5 et exprimer alors s(t) en fonction 
de E, τ et ω O. On tiendra compte dans l ’expression finale du fait q ue ωOτ≈1. Faire une représentation 
graphique.