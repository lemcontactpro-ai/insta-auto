# DS3 filtres mécanique PTSI


--- Page 1 ---

PTSI - Lyc´ ee Newton vendredi 8 d´ ecembre
DS no 3 de Physique-Chimie
Dur´ ee : 4 heures
L’usage de calculatrices est interdit.
Consignes : La pr´ esentation, la lisibilit´ e, l’orthographe, la qualit´ e de la r´ edaction, la clart´ e et la pr´ ecision
des raisonnements entreront pour une part importante dans l’appr´ eciation des copies. En particulier, les
r´ esultats non justiﬁ´ es et les applications num´ eriques dont il manque l’unit´ e ne seront pas pris en compte.
On encadrera les r´ esultats litt´ eraux et on soulignera les applications num´ eriques. Les copies
rendues seront num´ erot´ ees.
Ce sujet comporte trois probl` emes ind´ ependants.
Probl` eme I : Filtre de Colpitts
(45% du bar` eme environ)
On consid` ere le circuit ci-contre (en sortie ouverte), o` uR est une
r´ esistance,L une inductance et C1 et C2 deux capacit´ es.
Ce circuit est utilis´ e enr´ egime sinuso¨ ıdal forc´ e.
1. D´ eterminer la fonction de transfertH = u2
u1
et la mettre sous la forme :
H = K
1 + jQ
(ω
ω0
− ω0
ω
), (1)
o` u l’on pr´ ecisera les expressions deK, Q et ω0, trois r´ eels positifs.
2. Exprimer le gain G(ω) =|H| et la phase ϕ(ω) = arg(H) du ﬁltre.
Le diagramme de Bode en amplitude est donn´ e ci-dessous pourL = 31,6 mH et C1 =C2 =C.
2023-2024 1/9

--- Page 2 ---

PTSI - Lyc´ ee Newton vendredi 8 d´ ecembre
3. On s’int´ eresse ` a la pente des asymptotes :
(a) D´ eterminer la pente des asymptotes par lecture graphique. On reproduira l’allure du graphe
en expliquant dessus comme la lecture a ´ et´ e faite.
(b) Retrouver leurs valeurs ` a partir de l’´ etude asymptotique du gain.
4. Montrer que, dans les conditions choisies pour r´ ealiser ce diagramme de Bode, on a K = 1
2, Q =
R
√
C
2L et ω0 =
√
2
LC . On pourra admettre ce r´ esultat pour la suite.
5. D’apr` es l’expression du gain, pour quelle fr´ equence est-il maximal ? En d´ eduire la valeur deC.
6. D´ eterminer la constanteK ` a partir du diagramme de Bode. La valeur lue est elle-en accord avec la
valeur attendue ?
Aide num´ erique : 100.3≃ 2.
7. D´ eterminer le facteur de qualit´ e de ce ﬁltre ` a l’aide du diagramme de Bode. On exprimera clairement
la d´ emarche utilis´ ee. En d´ eduire une valeur approch´ ee deR.
8. Tracer le diagramme de Bode asymptotique pour la phase.
9. Ce ﬁltre peut-il ˆ etre utilis´ e en d´ erivateur ? en int´ egrateur ? Justiﬁer.
En entr´ ee du ﬁltre, on applique maintenant unsignal cr´ eneaude pulsation ω =ω0/3, de moyenne nulle
et d’amplitude Um = 1 V. Le signal u1(t) est d´ ecomposable en s´ erie de Fourier :
u1(t) = 4Um
π
[
sin(ωt) + 1
3 sin(3ωt) + 1
5 sin(5ωt) + 1
7 sin(7ωt) +...
]
. (2)
10. Dessiner l’allure du spectre en amplitude du signal d’entr´ eeu1(t).
11. On note fn la fr´ equence de l’harmonique de rangn, An l’amplitude de cette harmonique dans le
signa d’entr´ ee,A′
n celle de cette harmonique dans le signal de sortie. En utilisant la courbe de gain
fournie, on souhaite calculer l’amplitude des pics dans le signal de sortie u2(t). Pour cela :
(a) Donner l’expression de A′
n en fonction deAn et du gainG(f) ` a une fr´ equence que l’on pr´ ecisera.
(b) Donner l’expression du gain en fonction du gain en d´ ecibel.
(c) Recopier sur votre copie et compl´ eter le tableau ci-dessous, sachant que les valeurs des
gains en d´ ecibel ` a reporter dans le tableau sont{−6 dB ;−20 dB ;−28, 5 dB} (donn´ ees ici
dans le d´ esordre) et que celles du gain sont{0,04 ; 0,1 ; 0,5} (dans le d´ esordre ´ egalement). Vous
pourrez identiﬁer les gains correspondant aux gains en d´ ecibel sans les calculer explicitement.
n 1 3 5
fn (Hz) . . . . . . . . . . . . . . .
GdB(fn) . . . . . . . . . . . . . . .
G(fn) . . . . . . . . . . . . . . .
An A1 . . . . .×A1 . . . . .×A1
A′
n . . . . .×A1 . . . . .×A1 . . . . .×A1
12. Dessiner l’allure du spectre en amplitude du signal de sortie u2(t).
En d´ eduire une expression approch´ ee du signalu2(t), ne conservant qu’une seule composante du
spectre, et expliciter son amplitude et sa phase ` a l’origine. Quelle est la relation entre la fr´ equence
de ce signal de sortie et celle du signal d’entr´ ee ?
2023-2024 2/9

--- Page 3 ---

PTSI - Lyc´ ee Newton vendredi 8 d´ ecembre
Probl` eme II : Mod´ elisation d’une suspension de v´ ehicule
(37% du bar` eme environ)
Sur un v´ ehicule, les suspensions ont de multiples fonctions. Elles servent notamment :
- ` a am´ eliorer le confort des occupants ;
- ` a am´ eliorer la tenue de route en maintenant le contact entre les roues et le sol malgr´ e ses irr´ egularit´ es
(am´ elioration de la s´ ecurit´ e) ;
- ` a diminuer l’eﬀet, sur l’ensemble des organes m´ ecaniques, des vibrations et impacts dus aux irr´ egularit´ es
de la route (diminution de l’usure et du risque de rupture).
Il existe diﬀ´ erents types de suspensions et, dans ce probl` eme, nous nous int´ eresserons ` a un type tr` es
r´ epandu : les suspensions ` a ressorts. De mani` ere simpliﬁ´ ee, ces suspensions se composent d’un ressort qui
assure la liaison entre les roues (masses non suspendues) et la caisse (masse suspendue) et d’un syst` eme
d’amortissement.
Le but de ce probl` eme est d’´ etudier certaines caract´ eristiques des suspensions ` a ressort. En particulier,
nous ´ etudierons les mouvements verticaux du v´ ehicule dans diﬀ´ erentes situations : v´ ehicule non amorti,
v´ ehicule amorti en r´ egime libre, v´ ehicule se d´ epla¸ cant sur un sol non plat... Pour l’ensemble du probl` eme,
le r´ ef´ erentiel d’´ etude est le r´ ef´ erentiel terrestre consid´ er´ e comme galil´ een.
Le v´ ehicule est soumis au champ de pesanteur terrestre− →g .
Donn´ ees :champ de pesanteur : g = 10 m.s−2.
Hypoth` eses :tout au long du probl` eme, on consid´ erera que :
- l’extr´ emit´ e sup´ erieure du ressort est en contact avec le v´ ehicule et l’extr´ emit´ e inf´ erieure du ressort
est reli´ ee ` a une roue qui se trouve en contact avec le sol ;
- la roue reste en contact avec le sol ` a tout instant ;
- les dimensions de la roue sont telles qu’on la suppose ponctuelle de sorte qu’elle suit parfaitement
le proﬁl de la route, y compris lorsque le sol n’est pas plat.
Notations :
• fonctions complexes :
pour une fonction x(t) =Xm cos(ωt +ϕ), on notera x(t) =Xmej(ωt+ϕ) =Xmejωt.
Premi` ere partie : suspension sans amortissement
Le v´ ehicule ` a vide (masse suspendue) est assimil´ e ` a une massem = 1, 0× 103 kg.
La suspension est constitu´ ee d’un ressort de masse n´ egligeable, de raideurk = 1, 0× 105 N.m−1 et de
longueur au repos 𝓁0.
Dans cette premi` ere partie, on n´ eglige tout amortissement. On ne s’int´ eresse qu’au mouvement de
translation verticale du v´ ehicule.
La position du v´ ehicule est rep´ er´ ee par sa coordonn´ eez(t), l’axe Oz ´ etant vertical, orient´ e vers le haut et
muni d’un vecteur unitaire− →uz (ﬁgure 1).
z(t) repr´ esente la coordonn´ ee de l’extr´ emit´ e sup´ erieure du ressort.
`A l’´ equilibre, en l’absence de tout mouvement vertical, la position du v´ ehicule est rep´ er´ ee par sa
coordonn´ eeze.
1. D´ eterminer l’expression de la coteze ` a l’´ equilibre en fonction dem, g, k et 𝓁0.
2. Le v´ ehicule ´ etant en mouvement, d´ eterminer l’´ equation diﬀ´ erentielle (´ equation (2)) v´ eriﬁ´ ee parz(t).
L’´ equation (2) reliera les diﬀ´ erentes grandeursze, k, m, z(t) et ses d´ eriv´ ees temporelles.
2023-2024 3/9

--- Page 4 ---

PTSI - Lyc´ ee Newton vendredi 8 d´ ecembre
Figure 1 – suspension sans amortissement
3. Donner la solution g´ en´ erale de l’´ equation (2). D´ eterminer les expressions litt´ erales de la pulsation
propre ω0 et de la p´ eriode propreT0, de la suspension en fonction des param` etres du probl` eme.
D´ eterminer les valeurs num´ eriques deω0 et T0.
4. On suppose qu’un op´ erateur appuie sur le v´ ehicule et l’am` ene dans une position rep´ er´ ee par la cote
z0 avecz0<z e. `A un instantt = 0, choisi comme origine du temps, le v´ ehicule est lˆ ach´ e sans vitesse
initiale. D´ eterminer alors l’expression dez(t) en fonction de t, ze, ω0 et z0.
5. Tracer l’allure de z(t) et faire apparaˆ ıtre sur le graphique les cotes minimale zmin, maximale zmax
et moyenne zmoy ainsi que la p´ eriode propreT0.
Donner les expressions des cotes minimale zmin, maximale zmax et moyenne zmoy en fonction de ze
et z0.
Deuxi` eme partie : suspension avec amortissement
On suppose dans cette partie que la suspension d´ ecrite dans la partie pr´ ec´ edente comporte maintenant
un dispositif qui exerce, sur le v´ ehicule de masse m, une force d’amortissement visqueux donn´ ee par− →F =−h− →v o` u− →v repr´ esente la vitesse verticale du v´ ehicule par rapport ` a la roue eth un coeﬃcient appel´ e
coeﬃcient de frottement ﬂuide (ﬁgure 2).
6. Quelle est la dimension de h dans les dimensions de base du syst` eme international ?
7. D´ eterminer l’´ equation diﬀ´ erentielle v´ eriﬁ´ ee par la coordonn´ eez(t) au cours du temps. L’´ equation
reliera les diﬀ´ erentes grandeursze, k, h, m, z(t) et ses d´ eriv´ ees temporelles.
8. ´Ecrire les conditions portant sur les param` etresm, k et h pour que la suspension se trouve respec-
tivement dans les r´ egimes pseudop´ eriodique, critique et ap´ eriodique.
9. V´ ehicule en charge et vieillissement de la suspension.
9.1. Si l’amortissement est tel que la suspension se trouve en r´ egime critique lorsque le v´ ehicule est ` a
vide, dans quel r´ egime se trouve-t-il lorsque le v´ ehicule est en charge ? Justiﬁer qualitativement
la r´ eponse.
9.2. D` es lors, comment choisir la valeur de l’amortissement pour ´ eviter les oscillations, mˆ eme lorsque
le v´ ehicule est en charge ? Justiﬁer qualitativement la r´ eponse.
2023-2024 4/9

--- Page 5 ---

PTSI - Lyc´ ee Newton vendredi 8 d´ ecembre
Figure 2 – suspension avec amortissement
Le v´ ehicule se d´ eplace maintenant sur un sol non plat. La position verticale du point bas de la suspension
(roue) est rep´ er´ ee par la variablezs(t) (ﬁgure 3). Il est rappel´ e que, par hypoth` ese, la roue est consid´ er´ ee
comme ponctuelle et reste ` a tout instant en contact avec le sol.
Figure 3 – v´ ehicule sur un sol non plat de proﬁl quelconque
10. Nous nous placerons pour cette question dans le cas particulier o` u le v´ ehicule se d´ eplace sur une
route telle que :
- pour t<t 1 : zs =z1, o` uz1 est une constante positive et t1> 0 ;
- pour t>t 1 : zs(t) = 0.
Pour illustrer la situation, on pourra imaginer qu’` a l’instantt1, le v´ ehicule descend d’un trottoir de
hauteur z1, et rejoint une route plane et horizontale de cote nulle.
2023-2024 5/9

--- Page 6 ---

PTSI - Lyc´ ee Newton vendredi 8 d´ ecembre
On consid` ere que, pourt<t 1, la cote z(t) du v´ ehicule est constante, c’est-` a-dire que le v´ ehicule se
d´ eplace en r´ egime permanent.
Dans les deux graphiques demand´ es ci-apr` es, on pr´ ecisera clairement sur chaque graphique la valeur
de z pour 0 <t<t 1, et la valeur de z pour t tendant vers l’inﬁni :
10.1. Donner l’allure de z(t) pour t variant entre 0 et t≫ t1, lorsque la suspension est en r´ egime
pseudop´ eriodique. D´ eterminer l’expression de la pseudo-p´ eriodeTpp en fonction de T0, h, k et
m, et l’expression du temps caract´ eristique d’amortissement τ en fonction de h, k et/ou m.
Faire apparaˆ ıtre ces grandeursTpp et τ sur le graphe.
10.2. Donner l’allure de z(t) pour t variant entre 0 et t≫ t1 lorsque la suspension est en r´ egime
ap´ eriodique.
Troisi` eme partie : r´ egime forc´ e
Dans cette partie, le v´ ehicule se d´ eplace horizontalement avec une vitesse constantev1.
Il est rappel´ e que, par hypoth` ese, la roue est consid´ er´ ee comme ponctuelle et reste ` a tout instant en
contact avec le sol.
Ici encore la position verticale du point bas de la suspension (roue) est rep´ er´ ee par la variable zs(t)
(ﬁgure 4).
Dans cette partie, le v´ ehicule se d´ eplace sur un sol ondul´ e horizontal sinuso¨ ıdal.
On a donc zs(t) =z0 cos(ωt).
Figure 4 – r´ egime forc´ e
La suspension comporte un dispositif d’amortissement visqueux ; son action sur le v´ ehicule est mod´ elis´ ee
par la force − →F =−h− →v o` u− →v repr´ esente la vitesse relative des deux extr´ emit´ es de l’amortisseur eth le
coeﬃcient de frottement ﬂuide.
On a donc− →F =−h( ˙z− ˙zs)− →uz.
11. ´Etablir l’´ equation diﬀ´ erentielle v´ eriﬁ´ ee parz′ = z−ze (o` uze repr´ esente la longueur du ressort ` a
l’´ equilibre statique calcul´ ee ` a la question 1). On remarquera que le second membre s’exprime en
fonction de zs, ˙zs, k, h et m.
Dans la suite de cette partie, on utilisera les notations complexes rappel´ ees au d´ ebut de l’´ enonc´ e.
12. Pour simpliﬁer les notations, on posera :
ω2
0 = k
m et 2 λω0 = h
m.
2023-2024 6/9

--- Page 7 ---

PTSI - Lyc´ ee Newton vendredi 8 d´ ecembre
D´ eterminer l’expression de la fonction de transfertH =
Z′
m
Zsm
de la suspension en fonction de ω, ω0
et λ.
13. Montrer que le gain est donn´ e par l’expression :
G =
√
1 +ax2
(1−x2)2 +bx2
o` ux = ω
ω0
et a et b sont des param` etres dont on donnera l’expression en fonction deλ.
Par la suite, vous pourrez utiliser l’expression pr´ ec´ edente du module de la r´ eponse complexe, mˆ eme si
vous n’ˆ etes pas parvenu ` a la d´ emontrer.
14. ´Etude de la r´ eponse complexe.
14.1. D´ eterminer le comportement asymptotique du gain ` a basse fr´ equence. D´ ecrire dans ce cas le
comportement de la masse m par rapport au sol.
14.2. D´ eterminer le comportement asymptotique du gain ` a haute fr´ equence. D´ ecrire dans ce cas le
comportement de la masse m par rapport au sol.
14.3. On consid` ere pour simpliﬁer :
- que la valeur maximale de G est atteinte pour une pulsation ω1 non nulle telle que le
d´ enominateur de l’expression pr´ ec´ edente est minimal ;
- que l’on se trouve dans le cas o` uλ< 1/
√
2.
D´ eterminer l’expression deω1 en fonction de ω0 et λ (ou de ω0 et b si ce dernier n’a pas ´ et´ e
d´ etermin´ e).`A quoi correspond physiquement le cas o` u la pulsation est ´ egale ` aω1 ?
Remarque : en r´ ealit´ e, la d´ etermination de la pulsation qui correspond ` a la valeur maximale deG
aurait dˆ u prendre en compte le fait que le num´ erateur deG d´ epend ´ egalement de la pulsation. Le
calcul complet conduit ` a des r´ esultats sensiblement ´ equivalents.
15. Donner les expressions des asymptotes du diagramme de Bode en gain, GdB en fonction de log(x).
Repr´ esenter alors l’allure des diagrammes de Bode en gain, r´ eel et asymptotique, sur le mˆ eme graphe.
On fera apparaˆ ıtre les valeurs particuli` eres d´ etermin´ ees dans la question pr´ ec´ edente.
Probl` eme III : Cin´ etique de la dissolution du carbonate de calcium
dans une solution acide
(18% du bar` eme environ)
On s’int´ eresse ` a la vitesse de la r´ eaction de dissolution du carbonate de calcium selon deux m´ ethodes.
Pour cela on ´ etudie l’´ evolution de la r´ eaction entre le carbonate de calcium CaCO 3(s) et un volume
V0 = 100 mL d’une solution d’acide chlorhydrique de concentration ca = [H+] = 0, 10 mol.L−1.
L’´ equation de la r´ eaction s’´ ecrit :
CaCO3(s) + 2H+
(aq) = CO2(g) + H2O(l) + Ca2+
(aq)
On consid´ erera que la totalit´ e du dioxyde de carbone form´ e se d´ egage.
Premi` ere m´ ethode
Dans une premi` ere exp´ erience on mesure la pression du dioxyde de carbone apparu en utilisant un capteur
de pression diﬀ´ erentiel. Le gaz occupe un volumeV = 1, 0 L ` a la temp´ erature de 25°C. Les r´ esultats sont
regroup´ es dans le tableau ci-dessous :
1. ´Etablir la relation donnant la quantit´ e de mati` ere en dioxyde de carbonenCO2 ` a chaque instantt
en fonction de pCO2.
2023-2024 7/9

--- Page 8 ---

PTSI - Lyc´ ee Newton vendredi 8 d´ ecembre
t (s) 10,0 20,0 30,0 40,0 50,0 60,0 70,0 80,0 90,0 100
pCO2 (Pa) 1250 2280 3320 4120 4880 5560 6090 6540 6940 7170
t (s) 10, 0 20, 0 30, 0 40, 0 50, 0 60, 0 70, 0 80, 0 90, 0 100
x (mmol) 0, 50 0, 92 1, 34 1, 66 1, 97 2, 24 2, 46 2, 64 2, 80
2. ´Etablir la relation entre l’avancement molaire x et n(CO2(g)). Eﬀectuer l’application num´ erique ` a
t = 100 s aﬁn de compl´ eter le tableau de valeurs suivant.
On prendra 1
RT ≃ 4× 10−4 J−1.mol
Deuxi` eme m´ ethode
Dans une deuxi` eme exp´ erience on mesure le pH de la solution aﬁn de d´ eterminer [H+
(aq)] en fonction du
temps. Les r´ esultats sont regroup´ es dans le tableau ci-dessous :
t (s) 10, 0 20, 0 30, 0 40, 0 50, 0 60, 0 70, 0 80, 0 90, 0 100
nH+ (mmol) 9, 00 8, 20 7, 30 6, 70 6, 10 5, 50 5, 10 4, 70 4, 40 4, 20
3. Quelle relation existe-t-il entre nH+ et [H +
(aq)] ` a tout instant ? ´Etablir la relation entre nH+ et
l’avancement x. Eﬀectuer l’application num´ erique ` at = 10, 0 s aﬁn de compl´ eter le tableau de
valeurs suivant
t (s) 10, 0 20, 0 30, 0 40, 0 50, 0 60, 0 70, 0 80, 0 90, 0 100
x (mmol) 0, 90 1, 35 1, 65 1, 95 2, 25 2, 45 2, 65 2, 80 2, 90
4. Les deux m´ ethodes sont-elles coh´ erentes ?
Une fois les r´ esultats exp´ erimentaux obtenus on d´ esire d´ eterminer l’ordre de la r´ eaction par rapport ` a
H+
(aq). On utilisera comme expression de la vitesse :
v =k[H+
(aq)]α
o` uα est l’ordre de la r´ eaction.
5. D´ eﬁnir la vitesse de la r´ eaction par rapport ` a [H+
(aq)].
6. ´Etablir la relation entre [H +
(aq) ] et le temps en supposant que la r´ eaction est d’ordre 0 par rapport
` a H+
(aq). ´Etablir alors la relation suivante :
x =kV0t
7. ´Etablir la relation entre [H +
(aq)] et le temps en supposant que la r´ eaction est d’ordre 1 par rapport
` a H+
(aq). ´Etablir alors la relation suivante :
lncaV0− 2x
caV0
=−2kt
8. ´Etablir la relation entre [H +
(aq)] et le temps en supposant que la r´ eaction est d’ordre 2 par rapport
` a H+
(aq). ´Etablir alors la relation suivante :
1
caV0− 2x− 1
caV0
= 2kt
V0
On obtient les graphes suivants :
2023-2024 8/9

--- Page 9 ---

PTSI - Lyc´ ee Newton vendredi 8 d´ ecembre
9. `A l’aide des graphes d´ eterminer l’ordre de la r´ eaction et la constante de vitesse dont on pr´ ecisera
l’unit´ e.
2023-2024 9/9