# DS2 circuits RLC mécanique optique PTSI


--- Page 1 ---

PTSI - Lyc´ ee Newton vendredi 10 novembre
DS no 2 de Physique-Chimie
Dur´ ee : 4 heures
L’usage de calculatrices est interdit.
Consignes : La pr´ esentation, la lisibilit´ e, l’orthographe, la qualit´ e de la r´ edaction, la clart´ e et la pr´ ecision
des raisonnements entreront pour une part importante dans l’appr´ eciation des copies. En particulier, les
r´ esultats non justiﬁ´ es et les applications num´ eriques dont il manque l’unit´ e ne seront pas pris en compte.
On encadrera les r´ esultats litt´ eraux et on soulignera les applications num´ eriques. Les copies
rendues seront num´ erot´ ees.
Ce sujet comporte quatre probl` emes ind´ ependants.
Probl` eme I : ´Etude d’un circuit ´ electrique ` a trois mailles
(45% du bar` eme environ)
On consid` ere le circuit ci-dessous, compos´ e de deux sources id´ eales de tension (de f.´ e.m.E etE′ positives),
de deux conducteurs ohmiques de mˆ eme r´ esistanceR, d’un condensateur id´ eal de capacit´ eC, d’une bobine
id´ eale d’inductanceL et de trois interrupteurs K1,K2 etK3. L’intensit´ e du courant traversant la bobine
et la tension aux bornes du condensateur sont respectivement not´ eesi(t) et uc(t). Nous nous int´ eressons
` a l’´ evolution de ces grandeurs pendant deux phases : une premi` ere phase o` u seulK2 est ouvert et une
seconde phase o` u seulK2 est ferm´ e.
1 ´Etude du circuit pendant la premi` ere phase
On part d’une situation initiale dans laquelle les trois interrupteurs sont ouverts et le condensateur est
d´ echarg´ e.
1. D´ eterminer les valeurs dei et de uc correspondantes, que l’on notera i0 et u0 (on fera attention ` a
bien respecter ces notations). Justiﬁer soigneusement.
`A l’instant t = 0, on ferme les interrupteurs K1 et K3, l’interrupteur K2 restant ouvert.
2. Que vaut l’intensit´ e du courant dans la branche du haut de la maille centrale ?Justiﬁer soigneu-
sement.
Lors de cette premi` ere phase, le circuit ´ etudi´ e est donc ´ equivalent ` a deux circuits ` a une maille d´ econnect´ es,
tels que repr´ esent´ es ci-dessous.
2023-2024 1/6

--- Page 2 ---

PTSI - Lyc´ ee Newton vendredi 10 novembre
On s’int´ eresse d’abord au circuitA.
3. ´Etablir l’´ equation diﬀ´ erentielle v´ eriﬁ´ ee pari pourt> 0 ? On fera apparaˆ ıtre le temps caract´ eristique
τ du circuit, dont on donnera l’expression.
4. (a) D´ eterminer l’expression de i(t) lors de cette premi` ere phase.
(b) En d´ eduire l’expressionI0 de i lorsque le nouveau r´ egime permanent est atteint.
(c) `A partir de quel instant t1 peut-on aﬃrmer que le circuit A a atteint ce r´ egime permanent ?
5. Retrouver l’expression de I0 obtenue ` a la question pr´ ec´ edente ` a partir d’un circuit ´ electrique
´ equivalent.
On s’int´ eresse ensuite au circuitB.
6. Sans calcul (c’est-` a-dire sans r´ esoudre une ´ equation diﬀ´ erentielle), d´ eterminer l’expression de la
tension aux bornes du condensateur dans le nouveau r´ egime permanent qui s’´ etablit apr` es fermeture
de K3. Cette tension sera not´ eeU0.
7. `A partir de quel instant t2 peut-on aﬃrmer que le circuit B a atteint ce r´ egime permanent ?
2 ´Etude du circuit pendant la seconde phase
`A un instant t3 v´ eriﬁantt3> max(t1,t 2), on ferme l’interrupteurK2 et on ouvre les deux interrupteurs
K1 etK3. Dans la suite, l’instant t3 est pris comme nouvelle origine des temps : on consid´ erera donc que
t3 = 0.
8. Montrer que, pour t > 0 (= t3), la tension aux bornes du condensateur v´ eriﬁe une ´ equation
diﬀ´ erentielle de la forme :
¨uc +ω2
0uc =β,
o` u l’on pr´ ecisera les expressions deω0 et de β. Quel nom donne-t-on ` a cette ´ equation diﬀ´ erentielle ?
Comment appelle-t-on la grandeur ω0 ?
On souhaite r´ e-obtenir l’´ equation diﬀ´ erentielle pr´ ec´ edente ` a partir de consid´ erations ´ energ´ etiques.
9. On note EEM(t) l’´ energie ´ electromagn´ etique totale stock´ ee dans le circuit ` a l’instantt. Exprimer
EEM(t) en fonction de uc et de ˙uc.
10. Sans calcul, que peut-t-on dire sur l’´ evolution deEEM ? En d´ eduire l’´ equation diﬀ´ erentielle v´ eriﬁ´ ee
par uc en d´ erivant par rapport au temps l’expression EEM obtenue ` a la question pr´ ec´ edente.
Retrouve-t-on l’´ equation diﬀ´ erentielle ´ etablie ` a la question 8 ?
On souhaite maintenant r´ esoudre cette ´ equation diﬀ´ erentielle.
11. (a) D´ eterminer l’expression de uc(t) pendant cette seconde phase.
(b) Quelle est la p´ eriodeT0 des oscillations ?
(c) D´ eterminer l’expression de l’amplitudeA des oscillations de uc(t) en fonction de E, E′, R, L
et C.
3 Relev´ es exp´ erimentaux
Deux relev´ es exp´ erimentaux sont donn´ es ci-apr` es. Sur la Fig. 1 est repr´ esent´ ee la tension aux bornes de
la r´ esistance du circuitA pendant la premi` ere phase (0≤ t < t3), en convention r´ ecepteur. L’´ evolution
temporelle de la tension aux bornes du condensateur lors de la seconde phase ( t≥t3) est repr´ esent´ ee sur
la Fig. 2. Ces relev´ es ont ´ et´ e obtenus pour une valeur de r´ esistanceR = 150 Ω.
On souhaite d´ eterminer les valeurs deE, E′, L et C ` a partir de ces relev´ es.
2023-2024 2/6

--- Page 3 ---

PTSI - Lyc´ ee Newton vendredi 10 novembre
Figure 1 – ´Evolution temporelle de la tension aux bornes de la r´ esistance du circuit A
pendant la premi` ere phase.
Figure 2 – ´Evolution temporelle de la tension aux bornes du condensateur pendant la seconde
phase.
12. `A l’aide de la Fig. 1, d´ eterminer les valeurs de E et du temps caract´ eristiqueτ du circuit A. On
expliquera clairement la d´ emarche utilis´ ee.
13. En d´ eduire la valeur deL.
14. `A l’aide de la Fig. 2, d´ eterminer l’amplitudeA et la p´ eriodeT0 des oscillations. On fera apparaˆ ıtre
ces grandeurs sur un graphe sur la copie.
15. Exprimer alors E′ etC en fonction des param` etres connus (donn´ es ou mesur´ es) uniquement. On ne
fera pas l’application num´ erique.
2023-2024 3/6

--- Page 4 ---

PTSI - Lyc´ ee Newton vendredi 10 novembre
Probl` eme II : ´Equilibre chimique
(15% du bar` eme environ)
1 Synth` ese de l’´ ethanol
L’´ ethanol est un alcool pouvant ˆ etre obtenu par fermentation, ce n’est donc qu’assez tardivement qu’on
l’obtint par synth` ese.
La premi` ere synth` ese dite “proc´ ed´ e sulfurique” est obtenue par absorption de l’´ eth` ene dans l’acide
sulfurique suivie de l’hydrolyse des sulfates obtenus. Une alternative consiste ` a eﬀectuer une hydratation
directe de l’´ eth` ene. La premi` ere unit´ e fut r´ ealis´ ee par la soci´ et´ e Shell en 1948 aux Etats-Unis. BP Chemicals
ﬁt de mˆ eme en Ecosse ` a partir de 1951.
On s’int´ eresse ici ` a la thermodynamique de cette alternative. L’´ equation-bilan de la r´ eaction est :
C2H4gaz + H2Ogaz=C2H5OHgaz.
La r´ eaction s’eﬀectue ` a 600 K sous une pression de 70 bars. La constante d’´ equilibre de cette r´ eaction
vautK◦ = 2, 6.10−3 ` a 600 K.
1. On introduit l’´ eth` ene et l’eau dans les proportions stœchiom´ etriques. D´ eterminer l’´ equation dont la
r´ esolution donne la composition du syst` eme ` a l’´ equilibre.
2. On introduit une mole d’´ eth` ene. Montrer que la composition du syst` eme ` a l’´ equilibre peut ˆ etre
d´ etermin´ ee grˆ ace ` a la r´ esolution num´ erique d’une ´ equationf0(x) = 0, avec f0 une fonction de la
forme : f0(x) = x(2−x)
(1−x)2−c, o` uc est une constante. D´ eterminer la valeur num´ erique dec. `A quoi
correspond la solution x de l’´ equationf0(x) = 0 ? Quelle est son unit´ e ?
Pour r´ esoudre l’´ equationf0(x) = 0, on choisit d’utiliser une m´ ethode par dichotomie.
3. ´Ecrire une fonction dichotomie(f, xg, xd, eps=10 ∗∗−8) pour laquelle f est une fonction dont on
cherche le z´ ero entre xg et xd avec eps la tol´ erance pour un crit` ere d’arrˆ et de l’algorithme sur les
ant´ ec´ edents.
4. ´Ecrire les instructions permettant d’obtenir la valeur de x solution de f0(x) = 0, en faisant appel ` a
le fonction dichotomie pr´ ec´ edente.
5. La r´ esolution num´ erique donnex = 0, 080 dans les unit´ es du S.I. D´ eterminer la composition ﬁnale
du syst` eme.
Probl` eme III : Microscope
(28% du bar` eme environ)
Le microscope est mod´ elis´ e sur la ﬁgure 1, par un syst` eme de deux lentilles minces convergentes, l’une
constituant l’objectif (lentille L1 de centre O1 et de distance focale image f′
1 = 5 mm), et l’autre consti-
tuant l’oculaire (lentille L2 de centre O2 et de distance focale image f′
2 = 15 mm).
On ﬁxe O1O2 =D0 = 120 mm. On choisit le sens positif dans le sens de propagation de la lumi` ere.
On rappelle une relation de conjugaison d’une lentille et l’expression du grandissement γ :
1
OA′ − 1
OA = 1
f′ et γ = OA′
OA
2023-2024 4/6

--- Page 5 ---

PTSI - Lyc´ ee Newton vendredi 10 novembre
1. Les relations pr´ ec´ edentes sont valables ` a condition que les rayons lumineux satisfassent les conditions
de Gauss. Donner ces deux conditions.
2. Si F′
1 est le foyer image deL1 etF2 le foyer objet deL2, on d´ eﬁnit l’intervalle optique par la grandeur
alg´ ebrique ∆ =F′
1F2. Exprimer ∆ en fonction de f′
1, f′
2, D0, puis calculer sa valeur.
3. Un objet r´ eelAB perpendiculaire ` a l’axe optique est ´ eclair´ e et plac´ e ` a une distanced de L1, ` a sa
gauche, de fa¸ con ` a ce que l’imageA′B′ donn´ ee par l’objectif, appel´ ee image interm´ ediaire se trouve
dans le plan focal objet de l’oculaire. L’observation se fait ` a l’œil plac´ e au contact de l’oculaire.
(a) Exprimer d en fonction de f′
1 et ∆, puis calculer sa valeur.
(b) Exprimer le grandissement γ1 induit par l’objectif en fonction de f′
1 et ∆, puis calculer sa
valeur.
(c) Quel est l’int´ erˆ et pour l’observateur de cette position de l’objet ?
(d) Faire une construction g´ eom´ etrique faisant apparaˆ ıtre l’objet, l’image interm´ ediaire, ainsi que
l’angle α′ sous lequel est observ´ ee l’image ﬁnale ` a travers le microscope.
4. Le grossissement commercial du microscope est d´ eﬁni par G =
⏐⏐⏐⏐
α′
α
⏐⏐⏐⏐ o` uα est l’angle sous lequel
serait vu l’objet ` a l’œil nu plac´ e ` a une distanceD = 250 mm.
L’objet ´ etant de tr` es petite taille, ces deux angles seront bien sˆ ur tr` es faibles.
Exprimer G en fonction de ∆, D, f′
1 et f′
2, puis calculer sa valeur.
5. On utilise ce microscope pour mesurer l’´ epaisseur e d’une mince lame de verre ` a faces parall` eles,
d’indice n = 1, 5.
On colle une petite pastille bleue (B) sur la face gauche de la lame et une petite pastille rouge (R)
sur sa face droite.
On positionne d’abord la lunette (ensemble objectif+oculaire) du microscope de fa¸ con ` a faire la
mise au point sur la pastille rouge R (Figure 2, Position 1). Puis, grˆ ace ` a une vis microm´ etrique
(ﬁgure 3), on translate la lunette d’une distance ε, de fa¸ con ` a faire la mise au point sur l’imageB1
de la pastille bleue B (Figure 2, Position 2) :
On mesure ε = 0, 08± 0, 005 mm.
En tenant compte du ph´ enom` ene de r´ efraction et en consid´ erant les rayons lumineux tr` es peu inclin´ es
par rapport ` a l’axe optique, exprimere en fonction de n et ε, puis calculer sa valeur.
Probl` eme IV : ADN
(12% du bar` eme environ)
Ce sujet s’int´ eresse ` a des propri´ et´ es m´ ecaniques de l’ADN.
1 Raideur
On mod´ elise d’abord un simple brin d’ADN par une succession de bases reli´ ees par des ressorts.
On rep` ere le d´ eplacement deA par rapport ` a sa position d’´ equilibre parx1, et le d´ eplacement de
B par rapport ` a l’´ equilibre parx2. On pourra consid´ erer que la longueur ` a vide de ces ressorts est la
longueur qui s´ epare les pointsA et B lorsqu’ils sont ` a l’´ equilibre, on note cette longueur𝓁0. La raideur
d’une liaison covalente G-C est not´ eek1 et celle d’une liaison C-C est not´ eek2. Dans tout l’´ enonc´ e, les
eﬀets de la gravit´ e sont n´ eglig´ es.
2023-2024 5/6

--- Page 6 ---

PTSI - Lyc´ ee Newton vendredi 10 novembre
Figure 3 – Une portion d’un simple brin d’ADN (ici “GCC”) est mod´ elis´ ee par une succession de deux
ressorts.
1. Les deux points ( A et B) sont d´ eplac´ es de leur position au repos. Faire l’inventaire des forces qui
s’exercent sur le pointA. Donner leur expression vectorielle. Faire de mˆ eme pour le pointB. Donner
vos r´ eponses en fonction dex1, x2 et des param` etres de l’´ enonc´ e.
On tire sur le point B avec une force − →F 0 = F0− →ux jusqu’` a ce que l’ensemble se retrouve dans une
nouvelle position d’´ equilibre.
2. Montrer que tout se passe comme si le point B ´ etait attach´ e ` a l’origine via un unique ressort dont
on donnera la raideur.
On suppose que les liaisons covalentes qui relient une paire de bases (par exemple G-G, G-C, T-A, etc)
ont toutes une raideur ´ equivalente identique. Dans l’exemple de la ﬁgure 2, cela signiﬁe quek1 =k2 =k.
3. Quelle est la raideur d’un brin de s´ equence : GCTGAGG ?
Un double brin d’ADN est en fait une succession de “paires de bases”. Chaque base est reli´ ee ` a une base
compl´ ementaire (G avec C, T avec A) via des liaisons hydrog` ene :
Figure 4 – Figure 3 : Sch´ ematisation d’un morceau d’ADN double brin.
On n´ eglige l’eﬀet des liaisons hydrog` ene qui relient deux bases oppos´ ees. On tire sur une extr´ emit´ e du
double brin, l’autre restant attach´ ee.
4. Quelle est la raideur d’un double brin constitu´ e de 7 paires de bases, exprim´ ee en fonction dek ?
2023-2024 6/6