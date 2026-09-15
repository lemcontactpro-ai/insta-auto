# DM10 thermo calorimétrie


--- Page 1 ---

DM10 PCSI2 2022-2023 
physique 
1 
Problème 1 : Calorimétrie. 
Le calorimètre est un récipi ent fermé par un couvercle percé de  petites ouvertures permettant d’introduire un 
agitateur, un thermomètre , une résistance chauffante. Le système Σ constitué de  la cuve intérieure et de son 
contenu est relativement bien isolé et on peut négliger sur la durée d’une expérience de travaux pratiques les 
échanges thermiques avec l’extérieur. 
Pour appliquer le premier principe on devra tenir compte de la ca pacité thermique du calorimètr e. Les 
expériences dans un ca lorimètre se font à pression extérieure constante, le système étant en contact avec 
l’atmosphère par les petites ouvertures laissant passer le thermomètre et l’agitateur. 
Données :  
Capacité thermique massique de l’eau liquide : cL=4,18kJ.K-1.kg-1 et de l’eau solide : cS=2,09kJ.K-1.kg-1. 
1. Lister les hypothèses qu’on suppose vérifiées par la transformation thermodynamique ayant lieu dans le 
calorimètre. Ecrire alors le premier principe de la thermodynamique appliqué au système Σ. 
a.  Mesure de la capacité thermique du calorimètre. 
On souhaite déterminer la capacit é thermique du calorimètre, notée CCalo. Pour cela, on utilise la « méthode des 
mélanges ». On place dans le calorimètre une mas se m1=95g d’eau, et on considère que l ’ensemble constitué est 
à l ’équilibre thermique à la température T1=20°C. Puis on ajoute une masse m 2=69g d ’eau à la température 
T2=50°C. Après mélange, on mesure la température dans le calorimètre et on obtient TF=31,3°C. 
2. Exploiter le premier principe de la thermodynamique pour exprimer la capacité thermique CCalo du 
calorimètre en fonction de m1, m2, cL, T1, T2 et TF. 
On suppose que la capacité thermique massique de l’eau est connue sans incertitude, et on suppose que : 
 La mesure d ’une masse à la balance présente une valeur mesurée m mes et une demi largeur de 
l’intervalle de mesure δm=(1% de mmes +0,1g). 
 La mesure de la température présente une valeur mesurée Tmes et une demi largeur de l ’intervalle de 
mesure δT=(0,1°C). 
3. A l’aide du programme Python accompagnant ce devoir, estimer l’incertitude u(m1), l’incertitude u(m2), 
l’incertitude u(T1) et l’incertitude u(T2). 
4. Proposer alors une évaluation numérique de CCalo accompagnée d ’une incertitude u (CCalo) (on pourra 
aussi utiliser le programme Python). Commenter ce résultat. 
Parfois on donne plutôt la valeur en eau du calorimètre, notée μ, souvent donnée en grammes, définie comme la 
masse d’eau qui aurait la capacité thermique totale Ccalo, ainsi on écrit Ccalo = μcL. 
5. En déduire une évaluation (valeur numérique et incertitude) de la masse équivalente en eau µ du 
calorimètre. 
b. Mesure de la capacité thermique massique d’un solide 
On souhaite déterminer la capacité thermique massique cFe d’un échantillon de fer.  On verse dans le calorimètre 
meau =250g d’eau t rès froide et on mesure la température  T3 = 2 ,0°C. On introduit dans le calorimètre 
l’échantillon de fer, que l’on a préalablement pesé (sa  masse est mFe = 200 g) et qui est initialemen t à la 
température d’une étuve thermostatée, T4= 85, 0°C. On vérifie que  l’échantillon est bien entièrement recouvert 
d’eau. On attend que la température se stabilise et on mesure la température finale TF2 = 8,1°C. 
6. Etablir l’expression de cFe en fonction de µ, meau, mFe, cL, T3, T4 et TF2. 
7.  Procéder à une évaluation  de cette capac ité thermique et de l ’incertitude associée  à l ’aide d ’un 
programme python, en supposant que les mesures sont effectuées avec les m êmes précisions que 
précédemment. Commenter sachant que la valeur tabulée est de 440J.K-1.kg-1. 
c. Mesure de l’enthalpie massique de fusion de l’eau 
On souhaite déterminer l’enthalpie massique de fusion Δfush de l’eau à la pression PO=1,0 bar et à la température 
Tfus = 0°C. On verse dans le calorimètre mliq = 50 g d’eau chaude et on mesure la température  T5=74°C. On 
introduit ensuite dans le  calorimètre un glaçon de masse  msol = 19 g  sortant du congélateur, à la température 
T6=−18 °C. On attend que la température se stabilise et on mesure la température finale TF3 = 38°C. 
8. Etablir l’expression de Δfush en fonction de µ, mliq, msol, cL, cS, T5, T6, Tfus et TF3. 
9. Procéder à une évaluation de cette enthalpie massique de fusion et de l’incertitude associée à l’aide d’un 
programme python, en supposant que les mesures sont effectuées avec les m êmes précisions que 
précédemment. Commenter sachant que la valeur tabulée est de 330kJ.kg-1. 
d. Une autre mesure de la capacité thermique du calorimètre 
La capacité thermique du calorimètre a été mesurée précédemment avec une précision assez mauvaise . On se 
propose de la réévaluer en utilisant une méthode électrique. Une résistance chauffante de valeur R = 10Ω. 
On remplit le calorimètre avec une masse m=50 g d’ eau. On place la résistance dans le calorimètre sans la 
connecter. On laisse l’équilibre s’établir et on mesure la température : T7 = 21°C. On branche la résistance sur 
l’alimentation réglée sur U = 12,0 V et pendant une durée τ = 2 min. On attend que l’équilibre soit établi et on lit 
la température finale : TF4 = 27 °C.On négligera la capacité thermique de la résistance. 
10. Etablir l’expression de CCalo la capacité thermique du calorimètre en fonction de cL, T7, TF4 U, R et τ. 
11. Obtenir une évaluation  de la capacité the rmique et de l ’incertitude associée en supposant que la durée 
est mesurée à 1 seconde près et que la tension est mesurée avec une précision de 1%±1digit, l’affichage 
sur le multimètre se faisant avec 4 chiffres. Commenter le résultat obtenu.