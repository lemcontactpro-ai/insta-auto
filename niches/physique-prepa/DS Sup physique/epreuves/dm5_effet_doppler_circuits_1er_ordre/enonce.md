# DM5 effet doppler circuits 1er ordre


--- Page 1 ---

DM5 PCSI2 2022-2023 
physique 
1/2 
Problème 1 : Mesure de vitesse par effet Doppler. 
Un télémètre fixe en O, émet une onde électromagnétique sinusoïdale s(x,t) dans la direction et le sens de l’axe 
(Ox) d’amplitude s O, de fréquence f ref=34,7GHz, de célérité égale à celle de la lumière dans le vide 
c=3,00.108m.s-1 et qui sert de référence de phase dans tout l’exercice. 
 
 
 
1. A partir des renseignements précédents, donner l’expression du signal s(x,t) en fonction de s O, fref, c. 
2. Exprimer et évaluer numériquement la longu eur d’onde λ de l’onde émise. Indiquer alors le domaine 
des ondes électromagnétiques auquel appartient cette onde. 
 L’onde se réfléchit  sur une cible mobile  de position B(t)  de vitesse constante égale à  
O O xv v e
  le long de 
l’axe (Ox), de position initiale x O. Le point M situé à une abscisse x le long de l’axe (Ox) dans le référentiel de 
l’observateur, est situé dans le référentiel lié à la cible à une abscisse x’ le long de l’axe B(t)x. 
3. Exprimer l’abscisse x’ en fonction de x, xO, vO et t. 
4. Exprimer l’onde progressive sinusoïdale  s(x’,t) se propageant du télémètre vers la cible  dans le 
référentiel de la cible en fonction de sO, fref, vO, c, x’ et xO. 
Par réflexion sur la cible, on produit alors une onde s R(x,t) se propageant dans la direction d e l’axe (Ox) mais 
dans le sens rétrograde. Cette onde est synchrone de l’onde incidence dans le référentiel de la cible, et en phase 
avec l’onde incidente au niveau de la cible. Le coefficient de réflexion sur la cible est noté r, il donne le rapport 
de l’amplitude de l’onde réfléchie sur l’amplitude de l’onde incidente. 
5. Exprimer l’onde réfléchie sR(x’,t) dans le référentiel de la cible en fonction de r, s O, fref, vO, c, x’ et xO. 
6. Montrer finalement que l’onde réfléchie reçue par le télémètre s’écrit sous l a forme suivante et exprimer 
la différence de fréquence δf entre le signal envoyé et le signal reçu par le télémètre  : 
   2 2, . cos 2 1 2 O
R O ref ref O
vs x t r s f t f x x cc
     
 
Un radar portatif est utilisé pour déterminer la vitesse initiale d’un ballon frappé par un joueur lors de la mis e en 
jeu sur un terrain de volley-ball. Le décalage de fréquence mesuré est égal à δf=4,86kHz. 
7. Exprimer puis évaluer numériquement la vitesse vO du ballon de volley-ball en m.s-1 puis en km.h-1. 
L’affichage digital sur l’écran du radar portatif est en fait  donné en km.h-1  avec trois chiffres affichés et on peut 
lire dans la notice de l’appareil que la précision est égale à 1% de la valeur lue additionnée de 1digit. 
8. En déduire l’intervalle dans lequel la vitesse du ballon se situe et donner finalement une é valuation 
complète de la vitesse sous la forme d’une valeur mesurée accompagnée d’une incertitude type.  
Pour déterminer la vitesse du ballon, il faut donc l’extraire du signal reçu par le télémètre , en déterminant la 
variation δf de la fréquence de l’onde réfléchie par rapport à l’onde incidente. 
9. Evaluer numériquement le rapport δf/fref et commenter cette valeur. 
Pour extraire cette variation de fréquence, on utilise une détection hétérodyne à l’aid e d’un système de traitement 
constitué d’un premier étage multiplieur et d’un deuxième étage qui extrait du signal produit la composante de 
fréquence δf. 
On envoie en entrée du circuit multiplieur de gain 
K=1,0.10-1 V-1, le signal  générant l’onde produite  par 
le télémètre qu’on écrit sous la 
forme 
   cos 2ref O refv t v f t   et le signal obtenu en 
captant l’onde réfléchie sur la cible 
   
4cos 2
ref
e O ref O
fv t v f f t x c
      
. 
10. Exprimer le signal u e(t) à la sortie du multiplieur sous la forme d’une somme de deux composantes 
sinusoïdales en précisant les amplitudes et les fréquences de ces deux composantes. Tracer alors le 
spectre du signal ue(t). 
11. Expliquer alors qualitativement quel est le type de filtre à employer pour extraire la composante de 
fréquence δf du signal ue(t). 
Télémètre 
O x 
O O xv v e
 
B

--- Page 2 ---

DM5 PCSI2 2022-2023 
physique 
2/2 
Pour réaliser cette extraction, on envisage d’employer les filtres dont les circuits sont représentés ci-dessous : 
 
12. Par une analyse qualitative, déterminer la nature de ces trois filtres puis indiquer lequel de ces trois 
circuits doit être employé. 
13. Définir et déterminer alors la fonction de transfert H(jω) du filtre sélectionné. Exprimer le gain statique 
HO et la fréquence propre fO de ce filtre en fonction de R et C. 
14. Définir la fréquence de coupure à -3dB et déterminer proprement son expression dans le cas étudié. 
15. Donner les comportements asymptotiques d e la fonction de transfert  sur les domaines basse fréquence 
et haute fréquence.  En déduire les comportements du gain en décibel et de la phase sur ces domaines. 
Tracer alors le diagramme de Bode de ce filtre. 
Le télémètre employé est construit pour pouvoir mesurer des vitesses jusqu’à des valeurs de 150km.h -1. On 
souhaite que le signal haute fréquence contenu dans u e(t) soit atténué d’un facteur 10 3 alors qu’on veut conserver 
la totalité du signal basse fréquence. 
16. Evaluer numériquement  un ordre de grandeur de  la valeur maximale de δf. Dessiner alors sur un 
diagramme de Bode en amplitude, les contraintes associées à la réalisation du filtre envisagé. 
17. En utilisant le comportement asymptotiq ue adapté, déterminer l’expression de la valeur maximale f C,max 
de la fréquence de coupure à employer. Faire l’application numérique.  Vérifier que le signal basse 
fréquence sera bien transmis sans atténuation par ce filtre. 
On utilise un condensateur de capacité C=2,2pF pour réaliser le filtre. 
18. Exprimer puis évaluer la résistance à employer pour que la fréquence de coupure soit fixée à f C,max/5. 
Commenter la valeur obtenue.