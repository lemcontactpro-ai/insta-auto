# CB1_corr signal élec méca


--- Page 1 ---

ÉLÉMENTS DE CORRECTION CB 1
I Analyse expérimentale des vibrations du verre
I. A Analyse qualitative de l’enregistrement
Q 1. Il s’agit du phénomène de décomposition/résonance en/aux modes propres de l’onde
stationnaire.
Le "pic" de fréquence la plus basse est le fondamental qui modiﬁe la note et les autres sont les
harmoniques qui modiﬁent le timbre.
Q 2. La fréquence du signal enregistré est la fréquence du fondamental : f1≈ 540 Hz.
Q 3. Les ondes doivent être en phase : ∆ϕ = 0[2π].
En terme de décalage spatial : ∆δ = 0[λ] avec δ la différence de marche.
Il y a interférences constructive sur le tour supérieur du verre de diamètreD : πD = nλ = n c
fn
En utilisant le fondamental (n = 1) : c = πD f1≈ 204 m.s−1
Q 4. Les fréquences des différents modes propres sont :
— Fondamental : f1≈ 540 Hz.
— Harmoniques : f2≈ 1, 09 kHz, f3≈ 1, 64 kHz et f4≈ 2, 18 kHz.
On retrouve que les fréquences des harmoniques sont des multiples de la fréquence fonda-
mentale : fn = n× f1 avec n entier naturel non nul
Q 5. Le microphone doit avoir un gain réel de 1 sur toute la gamme de fréquences étudiées.
D’après la Figure 2, le microphone a unGdB = 0⇔ G = 1 de 100 à 10 000 Hz.
I. B Estimation du facteur de qualité Q
Q 6. La force de rappel élastique pour le ressort de constante de raideur k et de longueur à
vide nulle est− →Fk =−kx ⃗ux avec x la position du bord du verre qui correspond à la longueur
du ressort équivalent
Q 7. x correspond aussi à la position de la masse mobile équivalente
PFD M(m)RT considéré galiléen .⃗ux : m d2x
dt2 =−kx− α dx
dt
Par identiﬁcation, ω0 =
√
k
m et Q = 1
α
√
km
Q 8. ω0 : pulsation propre, pulsation du système pour Q→ ∞, en rad.s−1.
Q : facteur de qualité, nombre d’oscillations amorties du système, sans unité.
Q 9. Le régime est pseudo-périodique car les oscillations sont amorties.
La condition pour que le régime pseudo-périodique soit observé est que :Q > 1
2⇔ α < 2
√
km
La solution générale est de la forme : x(t) = ( a cos(ωt) + b sin(ωt))e−t/τ
avec ω = ω0
2Q
√
4Q2− 1 et τ = 2Q
ω0
On a bien Q≫ 1 d’après le nombre important d’oscillations sur la Figure 3 (car Q nombre
d’oscillations amorties du système).
ω(Q≫ 1)≈ ω0
2Q
√
4Q2 = ω0 (on retrouve ω0 pulsation propre du système).
ω0 = 2π f1≈ 3, 39 rad.s−1
PCSI 1 & 2 Lycée Paul Cézanne
 2022-2023 1/ 8

--- Page 2 ---

ÉLÉMENTS DE CORRECTION CB 1
Q 10. x(0) = 0 car le verre est à sa position de repos à l’instant initial
en effet, pour un système masse-ressort horizontal la longueur à l’équilibre est la longueur à
vide et ici la longueur à vide du ressort est nulle.
Donc la solution approchée est x(t)≈ V0
ω0
sin(ω0t)e−t/( 2Q
ω0 )
Q 11. e−∆t/( 2Q
ω0 ) = 1
2 avec ∆t = 1 s donc τ = ∆t
ln 2≈ 1, 4 s et Q = ω0∆t
2 ln 2≈ 2, 4.103≫ 1
Q 12.
Le son d’un diapason est "pur" donc
On peut entendre des battements car les fréquences sont voisines.
Les fréquences du signal et de l’enveloppe sont : fsignal = f4+ ω0
2π
2 et fenveloppe = f4− ω0
2π
2
Q 13. e(−5)≈ 0, 01 et ∆t′ = 10Q
ω0
≈ 7 s
PCSI 1 & 2 Lycée Paul Cézanne
 2022-2023 2/ 8

--- Page 3 ---

ÉLÉMENTS DE CORRECTION CB 1
II Étude de la résonance en amplitude du verre en régime sinu-
soïdal forcé
II. A Approche théorique
Q 14. X est l’amplitude complexe d’oscillation :
— son module est l’amplitude de l’oscillation réelle.
— son argument est le déphasage par rapport à Φ.
En passant l’équation différentielle en notation complexe :
((jω)2 + ω0
Q (jω) + ω2
0)X = A0ejΦ donc|X| = A0√
(1− ( ω
ω0
)2)2 + ( ω
ω0Q )2
Q 15. Les limites de l’amplitude relative sont|X|
A0
(ω→ 0)⁄= 0 et|X|
A0
(ω→ ∞)→ 0
donc seul le Graphe 2 convient.
Q 16. La forme canonique d’un passe-bas du deuxième ordre est :H(ω) = H0
1 + jω
Qω0
+
(
j ω
ω0
)2
Q 17. Pour un passe-bas du deuxième ordre, il y a résonance si Q > 1√
2
et la pulsation à la résonance est alors ωr = ω0
√
1− 1
2Q2
Les démonstrations sont évidemment dans le cours !
Q 18. On en déduit que la pulsation de résonance est la pulsation propre : ωr≈ ω0.
Q 19. Le gain à la résonance est donc Xr≈ QA0.
Q 20. Les amplitudes de vibrations sont X1≈ A0 et X2≈ A0/100.
II. B Tracé expérimental
Q 21.
PCSI 1 & 2 Lycée Paul Cézanne
 2022-2023 3/ 8

--- Page 4 ---

ÉLÉMENTS DE CORRECTION CB 1
Q 22. La différence de chemin géométrique est : δg = S′ M− SM
avec S′ M =
√
(x + ∆)2 + (d + 𝓁)2 = ( d + 𝓁)
√
1 + (x+∆)2
(d+𝓁)2 ≈ (d + 𝓁)(1 + 1
2
(x+∆)2
(d+𝓁)2 )
et de même, par le théorème de Pythagore et en utilisant l’approximation,
SM≈ (d + 𝓁)(1 + 1
2
(x−∆)2
(d+𝓁)2 )
Le déphasage vériﬁe bien ∆ϕ = 2π
λ δg + π
Q 23. Entre deux franges d’interférences successives d’ordrep et p + 1 (brillantes ou sombres) :
δp+1− δp = λ avec xp+1− xp = i
Q 24. La distance entre la source S et le plan du miroir varie avec le temps
telle que ∆(t) = ∆− xm(t)
donc l’interfrange varie également avec le temps
tel que i(t) = λ(d+𝓁)
2∆(t)
Q 25. On en déduit : imin = λ(d+𝓁)
2(∆+X) et imax = λ(d+𝓁)
2(∆−X)
et donc on extrait du système : X = λ(d+𝓁)
4 ( 1
imin
− 1
imax )
Q 26. Non car la persistance rétinienne de l’oeil caractérisé par sa rémanence correspond à
25 images par seconde ce qui est bien inférieure à 540 Hz
Q 27. L’effet stroboscopique fonctionne avec des sous-multiples de la fréquence :fi = 1
i
ω
2π
Q 28.
Q 29. On mesure : imin≈ 13 µm et imax≈ 30 µm et donc on en déduit : X≈ 3, 5 mm
Q 30. fr≈ 539, 6 Hz et Q≈ f0≈ fr
fc+− fc−≈ 2, 7.103 avec X
Xr ( fc) = 1√
2
Ces valeurs sont cohérentes avec celles de la partie précédente.
Q 31. La gamme de fréquences convient mais pas la précision sur les fréquences.
PCSI 1 & 2 Lycée Paul Cézanne
 2022-2023 4/ 8

--- Page 5 ---

ÉLÉMENTS DE CORRECTION CB 1
III Mise en résonance du verre par rétroaction : Effet Larsen
III. A Première analyse de l’effet Larsen
Q 32. D’après le spectre de la Figure 13, le signal électrique est un signal harmonique donc
une onde progressive sinusoïdale pour l’onde sonore convient.
Q 33. Il s’agit d’uneOPS vers les x croissants telle que la phase spatiotemporelle à l’origine
ϕ n’est pas précisée :s(x, t) = S0 cos(2π f (t− x
c ) + ϕ)
Q 34. On en déduit : s(0, t) = S0 cos(2π f t + ϕ) et s(d, t) = S0 cos(2π f (t− d
c ) + ϕ)
L’égalité proposée implique : 2π f d
c = 0[2π]⇔ fn d
c = n avec n entier non nul
Remarque : Les deux signaux sont en phase, c’est une condition d’interférences constructives !
Q 35.⇔ fn = n c
d avec n entier non nul donc par identiﬁcation dans l’équation des hyper-
boles : K = nc
Q 36. Les bornes inférieures et supérieures des fréquences mesurées sont f1≈ 2, 75 Hz
≤ fLarsen≤ f2≈ 3, 25 Hz :
III. B Le microphone électrostatique
Q 37. Le condensateur est équivalent à un interrupteur ouvert en régime stationnaire
donc u0 = 0 par la loi d’Ohm etuc0 = U0 par la loi des mailles.
III. B 1) Retour sur l’ampliﬁcateur
Q 38. Les propriétés de l’ALI idéal sont : Re→ ∞, Rs→ 0 et µ0→ ∞.
Le régime linéaire d’unALI est probable en cas de rétroaction négative.
Pour un ALI idéal en régime linéaire, on en déduit : V+ = V−
PCSI 1 & 2 Lycée Paul Cézanne
 2022-2023 5/ 8

--- Page 6 ---

ÉLÉMENTS DE CORRECTION CB 1
Q 39. Montage A : il s’agit d’un montage ampliﬁcateur inverseur
VoA
Vi
=− R2
R1
et RA = R1
Montage B : il s’agit d’un suiveur avec un montage ampliﬁcateur inverseur
VoB
Vi
=− R2
R1
et RB→ ∞
Le montage B n’appelle pas de courant dans la boucle de rétroaction.
Q 40.
Vi = V+
V+ = V− (régime linéaire)
V− = R1
R1 + R2
VA (pont diviseur de tension car i+ = 0 ALI idéal)
VA =
V−
R2
+ VoC
R3
1
R2
+ 1
R3
+ 1
R4
(loi des noeuds en terme de potentiels en A)
On a donc : VoC
Vi
(R1→ ∞) = 1 + R3
R4
comme un montage ampliﬁcateur non-inverseur.
Q 41. Le montage C garantit une impédance d’entrée inﬁnieRC→ ∞ (donc pas de courant
dans la boucle de rétroaction) et un gain réel pur supérieur à l’unité| VoC
Vi
| > 1 (car R1→ ∞).
Il ne faut pas conclure avec les arguments suivants :
Une relation entrée-sortie négative assure aussi un gain positif
mais ici R1≫ R2 donc| VoA B
Vi
|≪ 1.
La relation R3 > R4 qui est ici inutile puisque pour un ampliﬁcateur non-inverseur la relation
entrée-sortie est de la forme 1 + (> 0).
PCSI 1 & 2 Lycée Paul Cézanne
 2022-2023 6/ 8

--- Page 7 ---

ÉLÉMENTS DE CORRECTION CB 1
III. B 2) Réponse du circuit électrique en régime permanent sinusoïdal
Q 42. Par déﬁnitions : i(t) = dq(t)
dt et q(t) = C× uc(t) donc i(t) = d(C×uc(t))
dt
Q 43. U0 = uc(t) + u(t) (loi des mailles) et i(t) = u(t)
R (loi d’Ohm)
donc u(t)
R = ( U0− u(t)) dC(t)
dt − C(t)× du(t)
dt
Q 44.
Par continuité de la tension aux bornes d’un
condensateur : uc(t∗) = u0
D’après la question 37. : u0 = 0 donc
u(t∗) = U0− uc(t∗) = U0− u0 = U0
Donc u(t≥ t∗) = U0e−ω0t
Q 45. En passant l’équation différentielle en notation complexe :
((jω) + ω0)U = ( jω) U0X1
e donc U = U0X1ω
e
√
ω2
0 + ω
Q 46. On retrouve un passe-bas du premier ordre :
Pente de−20 dB/décade pour ω≪ ω0 et Gain en dB constant pour ω≫ ω0
ce qui est compatible pour des fréquences inférieures à 10 kHz sur la Figure 2.
Q 47. D’après la Figure 2, la fréquence de coupure du microphone est fc≈ 50 Hz.
C0 = 1
2πR fc
≈ 0, 32 µF
Q 48. D’après la Figure 2, la fréquence de résonance du microphone est fr≈ 20 kHz.√
ke
me = 2π fr≈ 1, 3.105 rad.s−1
Q 49. D’après la Figure 14, les fréquences Larsen sont autour de 3 kHz alors la fréquence
de résonance du microphone est de 20 kHz.
PCSI 1 & 2 Lycée Paul Cézanne
 2022-2023 7/ 8

--- Page 8 ---

ÉLÉMENTS DE CORRECTION CB 1
III. C Rôle du hautparleur dans la cavité acoustique
Q 50. D’après la Figure 17,Um( f→ 0)→ 0 et Um( f→ ∞)→ 0 donc il s’agit d’un ﬁltre de
type passe-bande.
Les fréquences de coupure vériﬁent Um( fc) = Um max√
2 avec Um max≈ 13, 5 V
Les fréquences de coupure du ﬁltre sont : fc1≈ 2, 4 Hz et fc2≈ 3, 5 Hz
Q 51. Les fréquences Larsen (f1≈ 2, 75 Hz≤ fLarsen≤ f2≈ 3, 25 Hz) sont toutes comprises
dans la bande passante du hautparleur ( fc1≈ 2, 4 Hz≤ f HP≤ fc2≈ 3, 5 Hz).
Le hautparleur est responsable de l’effet Larsen (et non le microphone et non le verre).
Q 52. Dans la cavité laser, le faisceau laser doit faire l’aller-retour d’où le facteur1
2
Q 53. Les fréquences possibles vériﬁent fn = nc
d
et doivent être comprises entre 2, 00 et 4, 00 kHz
donc correspondent à n ={8; 9; 10; 11; 12; 13; 14} :
Q 54. Ces deux points expérimentaux de fréquences du sifﬂement de la Figure 14 sont pour
les fréquences possibles de la cavité acoustique f10 et f11.
Q 55. Lorsque la distance d de la cavité acoustique augmente, la fréquence fn (à n ﬁxé)
diminue jusqu’à être trop atténuée (car n’appartenant plus à la bande passante du hautpar-
leur), alors c’est la fréquence fn+1 qui est ampliﬁée ( fn+1 > fn), autrement dit on passe de
l’hyperbolen à l’hyperbolen + 1.
PCSI 1 & 2 Lycée Paul Cézanne
 2022-2023 8/ 8