# DS01 optique


--- Page 1 ---

DS 01 1/5
DS 01 - le 24 sept 2022 (2h)
Optique - Calculatrice non autoris´ ee
• Encadrez vos r´ esultats analytiques, soulignez vos applications num´ eriques.
• V´ erifiez les homog´ en´ eit´ es, les signes, les m´ elanges vecteurs/scalaires.
• Tracez un trait sur toute la largeur de la copie entre chaque question.
I. Questions de cours (15 min max)
1) Cf annexe ` a la fin de l’´ enonc´ e
2) Une lentille mince donne d’un objet r´ eel situ´ e ` a60 cm avant son centre une image droite de taille r´ eduite
d’un facteur 5. D´ eterminer par le calcul la position de l’image et les caract´ eristiques de la lentille.
II. Fontaine lumineuse (20-30 min)
Document (D’apr` eshttp://www.fontainelaser.fr/spip.php?article3).
La premi` ere fontaine lumineuse r´ epertori´ ee semble ˆ etre celle de Jean-Daniel Colladon, un contemporain de
Fresnel et Maxwell, au milieu du XIXe si` ecle. La gravure de l’objet que nous reproduisons ici est d’ailleurs
assez r´ epandue sur le web.
“Colladon est l’auteur d’une [...] invention c´ el` ebre : les fontaines lumineuses. Afin
d’illustrer au mieux les diff´ erentes formes que prend un jet d’eau sortant par des
orifices vari´ es, il fait construire vers 1841 un grand vase de 7 m` etres de hauteur dont
une des faces est munie d’une ouverture sur laquelle se vissent diff´ erents diam` etres
d’embouchure pour varier la taille des jets. Sur la face oppos´ ee, il installe une lentille
convexe destin´ ee ` a concentrer un faisceau lumineux destin´ e ` a ´ eclairer la base du jet.
Les rayons lumineux traversent la lentille et le vase vers l’ouverture o` u s’´ echappe le
liquide. Le r´ esultat est ´ etonnant : “la lumi` ere circule dans ce jet transparent, comme
dans un canal, et en suit toutes les inflexions” ´ ecrit Colladon. Grˆ ace ` a son dispositif,
le savant genevois d´ emontre du mˆ eme coup que la trajectoire de la lumi` ere pi´ eg´ ee
n’est pas forc´ ement droite comme on le croyait jusqu’ici, mais qu’elle peut aussi ˆ etre
courbe.” dit St´ ephane Fischer, du Mus´ ee d’histoire des sciences de Gen` eve (2010).
Notons qu’une exp´ erience similaire fut r´ ealis´ ee d` es 1840 par Jacques Babinet.
Ce dernier expliqua mˆ eme comment le principe du guidage de la lumi` ere pouvait
s’´ etendre ` a des cylindres de verre courb´ es, anticipant ainsi les futures fibres optiques...
1) Quel est le nom du ph´ enom` ene observ´ e ? Rappeler la condition sur les indices des milieux transparents
travers´ es pour qu’il puisse ˆ etre observ´ e.
2) Compl´ eter le sch´ emaen annexe repr´ esentant enI, en pr´ esence de la r´ efraction : le dioptre, la normale, le
rayon r´ efract´ e, l’angle d’incidencei1 et l’angle de r´ efraction.
3) `A quel condition sur l’angle d’incidence le ph´ enom` ene observ´ e se produira ?´Etablir la condition. Faire
l’application num´ erique pourneau = 1, 33 et nair = 1, 00.
4) Repr´ esenter (sur l’annexe) le rayon lumineux lorsque l’angle d’incidence enI est sup´ erieur ` a l’angle de r´ eflexion
totale.
Le filet d’eau est courb´ e, on l’assimile ` a un arc de cercle comme repr´ esent´ e sur le sch´ ema en annexe 1.. On
souhaite maintenant d´ eterminer la condition sur le rayon de l’arc de cercle pour permettre d’avoir r´ eflexion
totale en I.
5) `A l’aide d’un peu de trigonom´ etrie, relier l’angle d’incidence en I au rayon R de courbure du filet d’eau et au
rayon a du filet d’eau.
6) En d´ eduire que pour avoir r´ eflexion totale enI, il faut que le rayon de courbure v´ erifie : R > nair
neau−nair
a
Proposer une application num´ erique.
Lyc´ ee Thiers - MPSI2 - Laure Sandeau

--- Page 2 ---

DS 01 2/5
III. Lecteur d’empreintes
2019-05-13 08:40:06 Page 1/12
2019
Physique-chimie 2
MP
4 heures Calculatrice autorisée
Les deux parties de ce sujet sont indépendantes. Certaines valeurs numériques sont regroupées en fin d’énoncé.
Certaines questions peu ou pas guidées, demandent de l’initiative de la part du candidat. Leur énoncé est repéré
par une barre en marge. Il est alors demandé d’expliciter clairement la démarche, les choix et de les illustrer,
le cas échéant, par un schéma. Toute démarche engagée, même non aboutie, et toute prise d’initiative seront
valorisées. Le barème prend en compte le temps nécessaire à la résolution de ces questions.
I Capture d’empreintes digitales par réflexion totale frustrée
Figure 1 Capteur d’empreinte digi-
tale (Wikimedia, Rachmaninoff, 2009-10-21)
Il existe différentes technologies de capteurs d’empreinte digitale, c’est-
à-dire de dispositifs permettant d’obtenir une image numérisée d’une
empreinte digitale, le plus souvent à des fins d’identification. Certaines
de ces technologies sont embarquées dans des smartphones. La techno-
logie dite « capteur optique d’empreinte digitale » est très employée,
elle repose sur le phénomène de réflexion totale frustrée qui est l’objet
de cette étude.
Le doigt est posé à plat sur l’hypoténuse d’un prisme droit isocèle taillé
dans un verre d’indice optique noté 𝑛. Il est éclairé par une diode laser
de longueur d’onde 𝜆0 dans le vide. L’image de l’empreinte digitale
à travers un système optique est formée sur un capteur CCD puis
numérisée. La figure 2 décrit le schéma de principe de ce dispositif.
Système optique
CCD
Port sérieRAMCPULSI
LED
Figure 2 Principe d’un capteur optique d’empreinte digitale
En première approche, le système optique se résume à la traversée d’un dioptre (𝒟) et d’une lentille convergente
(ℒ) (figure 3). Si 𝐴 est un point objet de l’empreinte digitale, alors on note 𝐴1 l’image de 𝐴 à travers le dioptre
(𝒟) et 𝐴′1 celle de 𝐴1 à travers la lentille (ℒ) :
𝐴 →→→→→→→→→
(𝒟)
𝐴1 →→→→→→→→→
(ℒ)
𝐴′1.
On définit également les longueurs algébriques suivantes :
𝐷1 = 𝐴1𝐴′1, 𝐷 = 𝐴𝐴′1, 𝑝 = 𝑂𝐴1, 𝑝 ′ = 𝑂𝐴′1.
Les sous-parties I.A.1 et I.A.2 sont indépendantes du reste du problème. La sous-partie I.A.3 introduit la
suite. Les sous-parties I.B et I.C sont liées par une analogie qu’on souhaite établir entre deux situations, l’une
se présentant en physique quantique et l’autre en optique ondulatoire. Néanmoins, en dehors des questions
développant l’analogie, les sous-parties sont conçues de manière relativement autonomes.
Il existe diff´ erentes technologies de capteurs d’empreinte digi-
tale, c’est-` a-dire de dispositifs permettant d’obtenir une image
num´ eris´ ee d’une empreinte digitale, le plus souvent ` a des fins
d’identification. Certaines de ces technologies sont embarqu´ ees
dans des smartphones. La technologie dite “capteur optique
d’empreinte digitale” est tr` es employ´ ee, elle repose sur le ph´ e-
nom` ene de r´ eflexion totale frustr´ ee qui est l’objet de cette
´ etude.
Le doigt est pos´ e ` a plat sur l’hypot´ enuse d’un prisme droit
isoc` ele taill´ e dans un verre d’indice optique not´ en. Il est ´ eclair´ e
par une diode laser de longueur d’onde λ0 dans le vide. L’image
de l’empreinte digitale ` a travers un syst` eme optique est form´ ee
sur un capteur CCD puis num´ eris´ ee. La figure 2 d´ ecrit le sch´ ema
de principe de ce dispositif.
2019-05-13 08:40:06 Page 1/12
2019
Physique-chimie 2
MP
4 heures Calculatrice autorisée
Les deux parties de ce sujet sont indépendantes. Certaines valeurs numériques sont regroupées en fin d’énoncé.
Certaines questions peu ou pas guidées, demandent de l’initiative de la part du candidat. Leur énoncé est repéré
par une barre en marge. Il est alors demandé d’expliciter clairement la démarche, les choix et de les illustrer,
le cas échéant, par un schéma. Toute démarche engagée, même non aboutie, et toute prise d’initiative seront
valorisées. Le barème prend en compte le temps nécessaire à la résolution de ces questions.
I Capture d’empreintes digitales par réflexion totale frustrée
Figure 1 Capteur d’empreinte digi-
tale (Wikimedia, Rachmaninoff, 2009-10-21)
Il existe différentes technologies de capteurs d’empreinte digitale, c’est-
à-dire de dispositifs permettant d’obtenir une image numérisée d’une
empreinte digitale, le plus souvent à des fins d’identification. Certaines
de ces technologies sont embarquées dans des smartphones. La techno-
logie dite « capteur optique d’empreinte digitale » est très employée,
elle repose sur le phénomène de réflexion totale frustrée qui est l’objet
de cette étude.
Le doigt est posé à plat sur l’hypoténuse d’un prisme droit isocèle taillé
dans un verre d’indice optique noté 𝑛. Il est éclairé par une diode laser
de longueur d’onde 𝜆0 dans le vide. L’image de l’empreinte digitale
à travers un système optique est formée sur un capteur CCD puis
numérisée. La figure 2 décrit le schéma de principe de ce dispositif.
Système optique
CCD
Port sérieRAMCPULSI
LED
Figure 2 Principe d’un capteur optique d’empreinte digitale
En première approche, le système optique se résume à la traversée d’un dioptre (𝒟) et d’une lentille convergente
(ℒ) (figure 3). Si 𝐴 est un point objet de l’empreinte digitale, alors on note 𝐴1 l’image de 𝐴 à travers le dioptre
(𝒟) et 𝐴′1 celle de 𝐴1 à travers la lentille (ℒ) :
𝐴 →→→→→→→→→
(𝒟)
𝐴1 →→→→→→→→→
(ℒ)
𝐴′1.
On définit également les longueurs algébriques suivantes :
𝐷1 = 𝐴1𝐴′1, 𝐷 = 𝐴𝐴′1, 𝑝 = 𝑂𝐴1, 𝑝 ′ = 𝑂𝐴′1.
Les sous-parties I.A.1 et I.A.2 sont indépendantes du reste du problème. La sous-partie I.A.3 introduit la
suite. Les sous-parties I.B et I.C sont liées par une analogie qu’on souhaite établir entre deux situations, l’une
se présentant en physique quantique et l’autre en optique ondulatoire. Néanmoins, en dehors des questions
développant l’analogie, les sous-parties sont conçues de manière relativement autonomes.
En premi` ere approche, le syst` eme optique se r´ esume ` a la travers´ ee d’un dioptre(D) et d’une lentille convergente
(L) (figure 3). Si A est un point objet de l’empreinte digitale, alors on note A1 l’image de A ` a travers le dioptre
(D) et A′
1 celle de A1 ` a travers la lentille(L) :
A
(D)
−→ A1
(L)
−→ A′
1.
On d´ efinit ´ egalement les longueurs alg´ ebriques suivantes :
D1 = A1 A′
1, D = AA′
1, p = OA 1, p′ = OA′
1.
2019-05-13 08:40:06 Page 2/12
(𝒟
𝑛
(ℒ)
écran
CCD
axe optique
𝐴 𝐴1 𝐻 𝑂 𝐴′1
𝐿 𝐷
Figure 3 Schéma optique
I.A – Optique géométrique
I.A.1) Conception du système optique
L’objectif ici est de choisir la distance focale 𝑓′ de la lentille et sa position, par exemple en déterminant 𝑝′. À
cet effet, on donne 𝑛 = 1,5, 𝐿 = 3cm, 𝐷 = 10cm et le grandissement transversal 𝛾 = 𝑝′/𝑝 du système optique.
Q 1. Montrer que, dans les conditions de Gauss, la relation de conjugaison entre 𝐴 et 𝐴1 par le dioptre
plan formé par la face de sortie du prisme s’écrit 𝐻𝐴1 = 1
𝑛 𝐻𝐴.
verre indice 𝑛 air indice 1
𝐴 𝐴1 𝐻
𝐼
Figure 4
Q 2. Exprimer 𝑝 et 𝑝′ en fonction de 𝐷1 et de 𝛾. Déterminer alors 𝑓′ en fonction de 𝐷1 et de 𝛾 à l’aide de
la formule de conjugaison de Descartes : 1
𝑝′ − 1
𝑝 = 1
𝑓′ .
Q 3. On souhaite déterminer la condition portant sur la distance focale 𝑓′ d’une lentille convergente si
l’on veut former l’image réelle sur un écran situé à une distance 𝐷1 d’un objet réel. En remarquant qu’il faut
𝛾 < 0pour obtenir une image réelle d’un objet réel, montrer que le rapport 𝐷1/𝑓′ est inférieurement borné. En
déduire l’inégalité vérifiée par 𝑓′.
Q 4. Applications numériques . On suppose 𝛾 = −2. À quelle distance place-t-on la lentille devant l’écran
et quelle est sa focale ?
Q 5. On souhaite avoir une image la plus agrandie possible ( |𝛾| maximal), mais sans augmenter l’encom-
brement du dispositif, ce qui impose de ne pas augmenter la longueur 𝐷1. Dans quel sens faut-il faire varier 𝑓′ ?
En pratique, quelle limitation rencontre-t-on ?
I.A.2) Résolution de l’image
Dans cette sous-partie, on fait abstraction du prisme, on considère que l’empreinte est positionnée en 𝐴1 au lieu
de 𝐴.
Une empreinte digitale est faite de sillons de profondeur moyenne 𝑒 = 30 µm et dont deux crêtes voisines
parallèles sont distantes de 𝑎 = 100 µm. On note 𝑙𝑐 la largeur d’un pixel (considéré comme étant de forme
carrée) du capteur CCD. On cherche à obtenir l’image des crêtes du sillon sur le capteur CCD : la lentille
conjugue le plan des crêtes, où se situe 𝐴1, à l’écran CCD (figure 5).
Sur la figure 6, les points 𝑀1, 𝑀2 et 𝑀3 détaillent le motif de l’empreinte et leurs images respectives 𝑀′1 , 𝑀′2
et 𝑀′3 détaillent l’image de l’empreinte. On remarque que le point 𝑀′2 ne se forme pas tout à fait sur la surface
du CCD, les rayons lumineux délimités par la monture de la lentille viennent former une petite tâche circulaire
de diamètre 𝜙.
On note 𝑝′ la distance entre la lentille et la surface du CCD et |𝑝| avec 𝑝 < 0, la distance entre la lentille et le
plan formé par les points objets 𝑀1 et 𝑀3. On note alors 𝛾 = 𝑝′/𝑝 le grandissement entre les couples de points
conjugués (𝑀1,𝑀 ′1) et (𝑀3,𝑀 ′3). On a 𝛾 = −2.
Q 6. À quelle condition sur 𝑎 et sur 𝑙𝑐 peut-on distinguer deux crêtes successives ? Quelle taille de pixel
recommandez-vous ?
Lyc´ ee Thiers - MPSI2 - Laure Sandeau

--- Page 3 ---

DS 01 3/5
A. Conception du syst` eme optique
L’objectif ici est de choisir la distance focale f′ de la lentille et sa position, par exemple en d´ eterminantp′. `A cet
effet, on donne n = 1, 5, L = 3 cm, D = 10 cm et le grandissement transversal γ = p′/p du syst` eme optique.
0) D´ efinir les conditions de Gauss et pr´ eciser leur int´ erˆ et pour les syst` emes optiques centr´ es.
1) Montrer que, dans les conditions de Gauss, la relation de conjugaison entre A et A1 par le dioptre plan form´ e
par la face de sortie du prisme s’´ ecritH A1 = 1
n H A. Ce r´ esultat pourra ˆ etre utilis´ e par la suite mˆ eme s’il n’a
pas ´ et´ e d´ emontr´ e.
2019-05-13 08:40:06 Page 2/12
(𝒟
𝑛
(ℒ)
écran
CCD
axe optique
𝐴 𝐴1 𝐻 𝑂 𝐴′1
𝐿 𝐷
Figure 3 Schéma optique
I.A – Optique géométrique
I.A.1) Conception du système optique
L’objectif ici est de choisir la distance focale 𝑓′ de la lentille et sa position, par exemple en déterminant 𝑝′. À
cet effet, on donne 𝑛 = 1,5, 𝐿 = 3cm, 𝐷 = 10cm et le grandissement transversal 𝛾 = 𝑝′/𝑝 du système optique.
Q 1. Montrer que, dans les conditions de Gauss, la relation de conjugaison entre 𝐴 et 𝐴1 par le dioptre
plan formé par la face de sortie du prisme s’écrit 𝐻𝐴1 = 1
𝑛 𝐻𝐴.
verre indice 𝑛 air indice 1
𝐴 𝐴1 𝐻
𝐼
Figure 4
Q 2. Exprimer 𝑝 et 𝑝′ en fonction de 𝐷1 et de 𝛾. Déterminer alors 𝑓′ en fonction de 𝐷1 et de 𝛾 à l’aide de
la formule de conjugaison de Descartes : 1
𝑝′ − 1
𝑝 = 1
𝑓′ .
Q 3. On souhaite déterminer la condition portant sur la distance focale 𝑓′ d’une lentille convergente si
l’on veut former l’image réelle sur un écran situé à une distance 𝐷1 d’un objet réel. En remarquant qu’il faut
𝛾 < 0pour obtenir une image réelle d’un objet réel, montrer que le rapport 𝐷1/𝑓′ est inférieurement borné. En
déduire l’inégalité vérifiée par 𝑓′.
Q 4. Applications numériques . On suppose 𝛾 = −2. À quelle distance place-t-on la lentille devant l’écran
et quelle est sa focale ?
Q 5. On souhaite avoir une image la plus agrandie possible ( |𝛾| maximal), mais sans augmenter l’encom-
brement du dispositif, ce qui impose de ne pas augmenter la longueur 𝐷1. Dans quel sens faut-il faire varier 𝑓′ ?
En pratique, quelle limitation rencontre-t-on ?
I.A.2) Résolution de l’image
Dans cette sous-partie, on fait abstraction du prisme, on considère que l’empreinte est positionnée en 𝐴1 au lieu
de 𝐴.
Une empreinte digitale est faite de sillons de profondeur moyenne 𝑒 = 30 µm et dont deux crêtes voisines
parallèles sont distantes de 𝑎 = 100 µm. On note 𝑙𝑐 la largeur d’un pixel (considéré comme étant de forme
carrée) du capteur CCD. On cherche à obtenir l’image des crêtes du sillon sur le capteur CCD : la lentille
conjugue le plan des crêtes, où se situe 𝐴1, à l’écran CCD (figure 5).
Sur la figure 6, les points 𝑀1, 𝑀2 et 𝑀3 détaillent le motif de l’empreinte et leurs images respectives 𝑀′1 , 𝑀′2
et 𝑀′3 détaillent l’image de l’empreinte. On remarque que le point 𝑀′2 ne se forme pas tout à fait sur la surface
du CCD, les rayons lumineux délimités par la monture de la lentille viennent former une petite tâche circulaire
de diamètre 𝜙.
On note 𝑝′ la distance entre la lentille et la surface du CCD et |𝑝| avec 𝑝 < 0, la distance entre la lentille et le
plan formé par les points objets 𝑀1 et 𝑀3. On note alors 𝛾 = 𝑝′/𝑝 le grandissement entre les couples de points
conjugués (𝑀1,𝑀 ′1) et (𝑀3,𝑀 ′3). On a 𝛾 = −2.
Q 6. À quelle condition sur 𝑎 et sur 𝑙𝑐 peut-on distinguer deux crêtes successives ? Quelle taille de pixel
recommandez-vous ?
2) Exprimer p et p′ en fonction de D1 et de γ. D´ eterminer alorsf′ en fonction de D1 et de γ ` a l’aide de la
formule de conjugaison de Descartes.
3) On souhaite d´ eterminer la condition portant sur la distance focale f′ d’une lentille convergente si l’on veut
former l’image r´ eelle sur un ´ ecran situ´ e ` a une distanceD1 d’un objet r´ eel. En remarquant qu’il fautγ < 0
pour obtenir une image r´ eelle d’un objet r´ eel, montrer que le rapportD1/ f′ est inf´ erieurement born´ e. En
d´ eduire l’in´ egalit´ e v´ erifi´ ee parf′.
4) Applications num´ eriques. On supposeγ =−2. `A quelle distance place-t-on la lentille devant l’´ ecran et quelle
est sa focale ?
5) On souhaite avoir une image la plus agrandie possible (|γ| maximal), mais sans augmenter l’encombrement
du dispositif, ce qui impose de ne pas augmenter la longueur D1. Dans quel sens faut-il faire varier f′ ? En
pratique, quelle limitation rencontre-t-on ?
B. R´ esolution de l’image
Dans cette sous-partie, on fait abstraction du prisme, on consid` ere que l’empreinte est positionn´ ee enA1 au lieu
de A.
Une empreinte digitale est faite de sillons de profondeur moyenne e = 30µm et dont deux crˆ etes voisines parall` eles
sont distantes de a = 100µm. On note lc la largeur d’un pixel (consid´ er´ e comme ´ etant de forme carr´ ee) du
capteur CCD. On cherche ` a obtenir l’image des crˆ etes du sillon sur le capteur CCD : la lentille conjugue le plan
des crˆ etes, o` u se situeA1, ` a l’´ ecran CCD (figure 5).
Sur la figure 6, les points M1, M2 et M3 d´ etaillent le motif de l’empreinte et leurs images respectivesM′
1, M′
2 et M′
3
d´ etaillent l’image de l’empreinte. On remarque que le pointM′
2 ne se forme pas tout ` a fait sur la surface du CCD,
les rayons lumineux d´ elimit´ es par la monture de la lentille viennent former une petite tˆ ache circulaire de diam` etreϕ.
On note p′ la distance entre la lentille et la surface du CCD et |p| avec p < 0, la distance entre la lentille et le
plan form´ e par les points objetsM1 et M3. On note alors γ = p′/p le grandissement entre les couples de points
conjugu´ es(M1, M′
1) et (M3, M′
3).
6) `A quelle condition sur a et sur lc peut-on distinguer deux crˆ etes successives ? Quelle taille de pixel recommandez-
vous ?
Lyc´ ee Thiers - MPSI2 - Laure Sandeau

--- Page 4 ---

DS 01 4/5
2019-05-13 08:40:06 Page 3/12
empreinte
image(ℒ)
CCD
𝐴1 𝐴′1
|𝑝| 𝑝′
Figure 5
(ℒ)
CCD
𝑀1
𝑀2
𝑀3
𝑀′1
𝑀′2
𝑀′3
𝑎
𝑒
|𝑝| 𝑝′
𝑒′
𝜙𝑑
Figure 6 Formation de l’image d’un sillon d’empreinte digitale
Q 7. On note 𝑑 le diamètre de la monture de la lentille (ℒ). Montrer que 𝜙 = 𝛾𝑑𝑒
𝑝 , dans l’approxima-
tion 𝑒 ≪ |𝑝|.
En notant 𝑒′ la distance de 𝑀′2 à la surface du capteur CCD, on pourra montrer 𝑒′ ≈ 𝛾2𝑒.
Q 8. On voudrait que seules les crêtes soient nettes sur l’image et donc que les creux apparaissent flous.
Pour cela, il faudrait que le diamètre 𝜙 de la tache excède la distance 𝑀′1𝑀′3 . Quelle inégalité doit alors vérifier
le diamètre 𝑑 de la monture ? Montrer, en argumentant sur les ordres de grandeur, que c’est contraire au respect
des conditions de Gauss.
I.A.3) Réflexion totale
Un montage simple avec une lentille ne permet donc pas de capturer facilement les empreintes digitales de sorte
que seules les crêtes apparaissent sur l’image. On reprend donc le dispositif complet, incluant le prisme.
Q 9. Énoncer soigneusement les lois de Snell-Descartes.
Q 10. Définir la réflexion totale et en donner les conditions.
Q 11. Étant donné la position de l’empreinte digitale, si on s’en tient strictement à l’énoncé des lois de
Descartes, peut-on éclairer le doigt, afin de former son image sur le capteur CCD ? On rappelle que 𝑛 = 1,5.
Dans le montage proposé, la lentille permettra d’obtenir l’image du doigt sur l’écran du CCD. Néanmoins, il
faut aborder l’optique ondulatoire pour comprendre comment le doigt est éclairé au travers du prisme.
I.B – Passage d’une onde électromagnétique sur un dioptre
I.B.1) Relation de dispersion
Q 12. Rappeler les équations de Maxwell dans une région vide de courant et de charge. En déduire l’équation
de propagation d’une onde électromagnétique, sa relation de dispersion, sa vitesse de phase. Le vide est-il
dispersif ?
Q 13. On admet que dans un milieu linéaire, homogène, isotrope et parfaitement transparent, tout se passe
comme si l’on remplaçait dans la relation de dispersion précédente la permittivité du vide 𝜀0 par la grandeur
𝑛2𝜀0, appelée permittivité du milieu, où 𝑛 est l’indice optique du milieu ( 𝑛 est un réel supérieur à 1). On rappelle
que la valeur de l’indice optique d’un matériau varie avec la longueur d’onde 𝜆0 dans le vide. En déduire la
nouvelle relation de dispersion et l’expression de la vitesse de phase. Le milieu est-il dispersif ?
I.B.2) Coefficients de réflexion et de transmission
On considère une onde électromagnétique monochromatique incidente polarisée rectilignement selon la direction
⃗ 𝑒𝑦 et se propageant dans la direction donnée par son vecteur d’onde ⃗𝑘𝑖 = 𝑘𝑖𝑥 ⃗ 𝑒𝑥 + 𝑘𝑖𝑧 ⃗ 𝑒𝑧. On note 𝑖1 = ( ⃗ 𝑒𝑧, ⃗𝑘𝑖)
l’angle d’incidence de cette onde sur le dioptre plan d’équation 𝑧 = 0. Le champ électrique s’écrit
⃗⃗⃗⃗⃗𝐸𝑖(𝑀,𝑡) = 𝐸0 ⃗ 𝑒𝑦exp(−𝑗(𝜔𝑡− ⃗𝑘𝑖 ⋅ ⃗ 𝑟)) où ⃗ 𝑟 =⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗𝑂𝑀.
7) Question plus difficile On note d le diam` etre de la monture de la lentille(L). Montrer que ϕ≃ γd e
p, dans
l’approximation e≪| p|.
Pour cela, en notant e′ la distance de M′
2 ` a la surface du capteur CCD, on pourra montrer e′≃ γ2e. On
rappelle que 1
1 + x≃ 1− x si|x|≪ 1.
8) On voudrait que seules les crˆ etes soient nettes sur l’image et donc que les creux apparaissent flous. Pour
cela, il faudrait que le diam` etreϕ de la tache exc` ede la distanceM′
1 M′
3. Quelle in´ egalit´ e doit alors v´ erifier
le diam` etred de la monture ? Montrer, en argumentant sur les ordres de grandeur, que c’est contraire au
respect des conditions de Gauss.
C. R´ eflexion totale
Un montage simple avec une lentille ne permet donc pas de capturer facilement les empreintes digitales de sorte
que seules les crˆ etes apparaissent sur l’image. On reprend donc le dispositif complet, incluant le prisme.
9) ´Enoncer soigneusement les lois de Snell-Descartes.
10) D´ efinir la r´ eflexion totale et en donner les conditions.
11) ´Etant donn´ e la position de l’empreinte digitale, si on s’en tient strictement ` a l’´ enonc´ e des lois de Descartes,
peut-on ´ eclairer le doigt, afin de former son image sur le capteur CCD ? On rappelle que n = 1, 5.
Dans le montage propos´ e, la lentille permettra d’obtenir l’image du doigt sur l’´ ecran du CCD. N´ eanmoins, il
faut aborder l’optique ondulatoire pour comprendre comment le doigt est ´ eclair´ e au travers du prisme.
Lyc´ ee Thiers - MPSI2 - Laure Sandeau

--- Page 5 ---

DS 01 5/5
IV. Annexe ` a rendre avec votre copie
1. Annexe exercice 1
Physique−DS n °1
Page 5 / 8
PCSI
Année 2021-2022
NOM : Prénom :
ANNEXE À RENDRE A VEC VOTRE COPIE
Exercice 1 Tracés d’images par une lentille
Q1. Après avoir placé les foyers principaux de la lentille convergente, représenter l’image de l’objet AB.
⊕
O
F F′A
B
Que peut-on dire de l’objet et l’image?
©Objet réel ©Objet virtuel ©Image réelle ©Image virtuelle
Que peut-on dire du grandissement transversal?©γ >0 ©γ <0 © |γ|> 1 © |γ|< 1
Q2. Après avoir placé les foyers principaux de la lentille convergente, représenter l’image de l’objet AB.
⊕
O
A
B
Que peut-on dire de l’objet et l’image?
©Objet réel ©Objet virtuel ©Image réelle ©Image virtuelle
Que peut-on dire du grandissement transversal?©γ >0 ©γ <0 © |γ|> 1 © |γ|< 1
Page 5
2. Annexe exercice 2
Lycée Camille Vernet− PCSI Physique − DS n°1 Page 5 / 5
ANNEXE − À RENDRE A VEC VOTRE COPIE
NOM : __________________ Prénom : __________________
Annexe 1.
O
Annexe 2.
O
Annexe 3. Fontaine lumineuse
I
R
O a
5
Lyc´ ee Thiers - MPSI2 - Laure Sandeau