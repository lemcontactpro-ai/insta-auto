# DS2 circuits RLC elec


--- Page 1 ---

DS2 PCSI2 2022-2023 
physique 
1/3 
Exercice d’application directe du cours : RLC parallèle. 
 
 
Un condensateur est chargé et présente alors une 
tension constante U O sur l’intervalle de temps 
t<0. A l’instant initial, on le connecte à un circuit 
constitué d’un conducteur ohmique et d’une 
bobine en parallèle dans lequel ne circule aucun 
courant sur l’intervalle de temps t<0. 
1. Déterminer les conditions initiales de ce problème en exprimant u(t=0+) et ic(t=0+). 
2. Déterminer l’équation différentielle vérifiée par u(t) sur l’intervalle t>0. La mett re sous forme 
canonique et exprimer les paramètres introduits en fonction de C, R et L. 
3. Exprimer RC la résistance pour laquelle on observe un régime critique. 
On suppose que la résistance est égale à RC. 
4. Déterminer l’expression de u(t) sur l’intervalle de temps t>0. 
Problème 1 : étude d’une photodiode. 
On ét udie la photodiode dont le schéma est donnée sur la figure 1. ci -
contre. 
La photodiode est un capteur de lumière dont la caractéristique dépend de 
la puissance lumineuse qui l’éclaire. On donne ci -dessous sur la figure 2 la 
caractéristique I=f(U) pour des puissances lumineuses reçues allant de 
0mW à 10mW. 
 
Figure 1. symbole de la 
photodiode.
 
Figure 2. Caractéristique de la photodiode étudiée pour différentes puissances lumineuses reçues. 
1. Indiquer la convention dans laquelle la photodiode est étudiée. 
2. Pour une tension de U 1=0,5V, et une puissance lumineuse W1=8mW, lire la valeur de l’intensité du courant 
électrique I1 traversant la photodiode.  Exprimer alors la puissance  électrique P1 reçue par la ph otodiode et 
l’évaluer numériquement. 
3. Pour une tension de U 2=-1,0V, et une puissance  lumineuse W 2=6mW, lire la valeur de l’intensité du 
courant électrique I 2 traversant la photodiode, exprimer alors la puissance électrique P 2 reçue par la 
photodiode et l’évaleur numériquement. 
4. Quel est le comportement (générateur ou récepteur  ?) de la photodiode dans le cas étudié à la question 2  ? 
Reprendre la question dans le cas étudié à la question 3 ? 
5. Etablir à l’aide de la courbe proposée sur la figure 2. un tableau do nnant la valeur de I l’intensité du courant 
électrique inverse délivrée par la photodiode sur le domaine U<0, en fonction de la puissance lumineuse W 
reçue. Faire une représentation graphique de la courbe I=f(W) et apporter une conclusion qualitative à cet te 
étude. 
Pour utiliser la photodiode en capteur de lumière, il faut s’assurer qu’elle est toujours utilisée dans  le domaine U<0. 
On réalise donc un circuit où on alimente la photodiode (prise dans la même convention qu’en figure 1) à l’aide d’un 
générateur de Thévenin de force électromotrice E et de résistance interne r=250Ω. 
6. Faire un schéma du circuit d’étude. 
7. Donner l’équation caractéristique du générateur de Thévenin. 
On souhaite que pour toute valeur de puissance  lumineuse reçue inférieure  ou égale à Wmax=10mW, la tension aux 
bornes de la diode reste inférieure à Umax=-0,5V. 
8.  Reprendre sur une figure la courbe I=f(U) caractéristique de la diode pour une puissance W max=10mW. 
Tracer alors la courbe caratéristique correspondant au cas limite du générateur de Thévenin envisageable.

--- Page 2 ---

DS2 PCSI2 2022-2023 
physique 
2/3 
Déduire par lecture graphique  la valeur maximale  qu’il faut donner à E.  Vérifier ce résultat par un calcul 
bien justifié. 
9. Ajouter à votre circuit d’étude un voltmètre permettant de mesurer la tension U aux bornes de la di ode et un 
ampèremètre permettant de mesurer l’intensité I la traversant.  
10. Préciser la résistance de ces deux appareils dans le cas idéal puis dans le cas réel. Expliquer qu el biais de 
mesure est introduit dans le montage que vous avez proposé en question 9. 
Problème 2 : Thermistances et montages thermométriques. 
On cherche à comparer les performances de deux 
montages électriques pour mesurer les variations 
d’une thermistance en fonction de la température. 
Etude du montage simple : 
On étudie tout d’abord le montage de la figure 3. 
Le générateur est représenté par son modèle de 
Thévenin (e S, R S) et un voltmètre idéal mesure la 
tension V R aux bornes de la  thermistance de 
résistance R dépendant de la température T. 
  
Figure 3 : Montage simple.
1. En utilisant la relation d u diviseur de tension, déterminer l’expression de V R en fonction de R(T),  RS, R1 et 
eS. 
On suppose qu’à partir d’une température T O pour laquelle la résistance prend une valeur R(T O), la température 
augmente de δT et la résistance augmente d’une valeur δR. 
2. Exprimer la variation δVR de la tension obtenue aux bornes de la résistance en fonction de δR, R(T O), RS, et 
R1. Simplifier alors son expression en tenant compte du fait que δR est petite devant les autres résistances. 
Pour une température T A, la tension obtenu e au voltmètre est V R(TA)=2,35V, après augmentation de la température 
de δT, la tension lue au voltmètre est V R(TA+δT) =2,29V, on se trouve alors sur le calibre (2 à 20V) pour le quel la 
notice donne une incertitude évaluée à 0,1% de la valeur lue + 3 digits. 
3. Expliquer pourquoi ce montage ne permet pas de déterminer précisément la variation de tension observée.  
Etude du pont de Wheatstone : 
 
Pour obtenir des mesures de bonne préci sion des 
variations de la résistance R(T), on préfère utiliser le 
circuit avec pont de Wheatstone présenté sur la figure 
4. Dans cette modélisation, on suppose le générateur 
de résistance interne négligeable. 
On suppose qu’aucun courant ne circule dans le 
voltmètre qui est pris comme idéal. 
4. Déterminer la tension U  mesurée entre les 
points A et B en fonction de e S, R1, R3, R4 et 
R(T). 
5. L’équilibre du pont est réalisé lorsque la 
tension U=0, déterminer alors la relation 
liant R1, R3, R(Teq) et R4. 
 
 
Figure 4 : montage à pont de Wheatstone. 
6. Déterminer la tension δU lorsque la résistance prend la valeur R(T eq)+δR puis simplifier son expression en 
tenant compte du fait que δR est petite devant les autres résistances. 
7. Comparer alors les expressions de δU et δVR Quel avantage y a-t-il à utiliser le pont ? 
Problème 3 : Diode de roue libre. 
Le comportement d’un moteur peut -être modélisé par 
l’association série d’une résistance et d’une bobine 
idéale. Lorsqu’on ouvre le circuit, une surtension peut 
apparaître aux bornes du moteur et peut provoquer u ne 
étincelle de rupture, au niveau de l’interrupteur, qui 
peut-être dommageable. Pour prévenir ce phénomène, 
on installe une diode, dite de roue libre en parallèle du 
moteur comme sur la figure 5. 
Cette diode court -circuite le moteur à partir du moment 
où on ouvre l’interrupteur correspondant dans la suite à 
l’instant initial (t = 0). 
On notera également le fait que E > 0.  
 
Figure 5 : montage avec diode de roue libre.

--- Page 3 ---

DS2 PCSI2 2022-2023 
physique 
3/3 
En convention récepteur, on donne la caractéristique 
de la diode sur la figure 6 :  
 uS est la tension seuil de la diode, 
 rd est sa résistance interne. 
La diode présente deux régimes de fonctionnement : 
 diode bloquée si  «  u < u S » : la diode 
équivaut alors à un interrupteur ouvert  
 diode passante si «  i > 0  » ⇔ « u ≥ u S » : la 
diode équivaut alors à l’association série 
d’une source de tension uS et d’une 
résistance rd. 
 
 
Figure 6 : caractéristique de la diode. 
On étudie d’abord le régime stationnaire avant modification du circuit c’est-à-dire avec l’interrupteur fermé. 
1. Quelle est la tension UD aux bornes de la diode dans cette situation ? En déduire le dipôle équivalent. 
2. Quel est le dipôle équivalent de la bobine en régime stationnaire ?  
3. Dessiner alors le schéma équivalent du circuit et donner l’expression de iL(t<0). 
4. En déduire l’expression de l’énergie stockée dans la bobine en fonction de L, E et R. Faire l’application 
numérique pour R=0,1Ω, E=100V et L=0,5mH. 
Dans un premier temps, on considère que la diode est parfaite : rd = 0 et uS = 0. 
5. Déterminer i L(t=0+) en précisant bien l’argument utilisé. En déduire en précisant proprement le 
raisonnement que la diode est passante. Dessiner alors le circuit équivalent qu’il faut étudier. 
6. Montrer que l’équation d ifférentielle vérifiée par i L(t) sur l’intervalle t>0  s’écrit comme ci -dessous et 
préciser l’expression et la valeur numérique  du temps caractéristique τ : 
   1 0L
L
di t i tdt   
7. Résoudre cette équation pour obtenir l’expression de i L(t). Vérifier que la diode reste toujours passante. 
8. Tracer alors proprement iL(t).  
On reprend l’étude du régime transitoire en supposant que rd  0 et uS  0. 
9. Proposer un circuit équivalent pour l’étude du régime transitoire sur le domaine t>0. 
10. Montrer que l’équation différentielle vérifiée par i L(t) se met sous la forme suivante  en précisant 
l’expression du temps caractéristique τd : 
 
1 SL
L
d d d
udi idt r R    
11. Exprimer alors l’intensité iL(t). 
12. Montrer qu’il existe un temps t b à partir d uquel la diode change de régime et donner son expression en 
fonction de rd, R, E et uS. 
Résolution de problème. 
On charge initialement un condensateu r à une tension 
UO=5V. Au bout d’une demi heure, on constate que 
le condensateur est déchargé. 
On cherche alors à déterminer la résistance de fuite 
de ce condensateur par deux expériences différentes : 
 Dans la première, o n suit la tension aux 
bornes d’un c ondensateur de capacité 
C=1,0.10-7F à l’aide d’un voltmètre et on 
obtient la courbe donnée figure 8. 
 Dans une seconde expérience, on mesure 
bien la tension de 5V , on retire alors le 
voltmètre, puis on remesure la tension aux 
bornes du condensateur après cinq minutes. 
On mesure une tension de 2,0V au moment 
où on connecte le voltmètre. 
 
  
1. Analyser le problème et déterminer les valeurs de résistance associées aux différents composants.