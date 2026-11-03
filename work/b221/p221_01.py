from qb import *
b=Bank('p221_01')

# ---------------- 1789388 five numbers, product divisible by 4
b.add(1789388,1,r'''Five positive integers $a,b,c,d,e$ have sum $2009$, and the sum of three of them is $1000$. Prove that the product $abcde$ is divisible by $4$.''',
r'''Name the numbers so that $a+b+c=1000$; then $d+e=2009-1000=1009$.

\textbf{Among $d,e$.} The sum $d+e=1009$ is odd, so exactly one of $d,e$ is even.

\textbf{Among $a,b,c$.} The sum $a+b+c=1000$ is even, so the number of odd numbers among $a,b,c$ is even, that is $0$ or $2$. Hence at least one of $a,b,c$ is even.

So at least two of the five factors are even, each contributing a factor $2$, and therefore $4\mid abcde$. $\blacksquare$''',
'Parity|Divisibility',2)

# ---------------- 1789275 circumradius of equilateral triangle
fig=r'''pair B=(0,0),C=(6,0),A=(3,3*sqrt(3)),D=(3,0),O=(3,sqrt(3));
draw(circle(O,2*sqrt(3)),gray+linewidth(0.7));
draw(A--B--C--cycle,linewidth(0.9));
draw(A--D,dashed);
draw(O--C,blue+linewidth(0.8));
draw((3,0)--(3,0.35)--(3.35,0.35)--(3.35,0),linewidth(0.5));
dot(O);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$D$",D,S);label("$O$",O,W);
label("$6$",(A+B)/2,NW);
label("$R$",(O+C)/2,N,blue);'''
b.add(1789275,1,r'''Triangle $ABC$ is equilateral with side length $6$, and $D$ is the point of $BC$ with $AD\perp BC$. Find the radius of the circumcircle of triangle $ABC$.''',
r'''In an equilateral triangle the altitude $AD$ is also a median and a perpendicular bisector, so the circumcentre $O$ lies on $AD$, and it coincides with the centroid. Hence $AO=\dfrac23AD$.
'''+asy(fig,'5.5cm')+r'''
Since $D$ is the midpoint of $BC$, $BD=3$ and by Pythagoras $AD=\sqrt{6^2-3^2}=3\sqrt3$. Therefore
\[
R=AO=\dfrac23\cdot3\sqrt3=\boxed{2\sqrt3}.
\]
(Check: $OD=\sqrt3$ and $OC=\sqrt{OD^2+DC^2}=\sqrt{3+9}=2\sqrt3$.)''',
'Equilateral triangles|Circumcircles and circumcentres|Medians and centroids|Altitudes|Pythagorean theorem',2)

# ---------------- 1683277 matches in a group of four
b.add(1683277,1,r'''The first round of the 2010 FIFA World Cup consisted of several groups of four teams each. Within each group, each of the four teams played each other team exactly once. How many matches were there in each group?''',
r'''Each match corresponds to a pair of teams, so the number of matches is the number of ways to choose $2$ of the $4$ teams:
\[
\dbinom42=\dfrac{4\cdot3}{2}=\boxed{6}.
\]
(Each team plays $3$ matches; $4\cdot3=12$ counts every match twice.)''',
'Combinations',1)

# ---------------- 1789230 clock and rolling disk (alias)
b.add(1789230,1,r'''A clock face is a circle of radius $20$ cm. A circular disk of radius $10$ cm is externally tangent to the clock face at $12$ o'clock, and an arrow painted on the disk initially points vertically upward. The disk rolls without slipping clockwise around the outside of the clock face. At what point on the clock face will the disk be tangent when the arrow is next pointing vertically upward?

$\textbf{(A) }\text{2 o'clock}\qquad\textbf{(B) }\text{3 o'clock}\qquad\textbf{(C) }\text{4 o'clock}\qquad\textbf{(D) }\text{6 o'clock}\qquad\textbf{(E) }\text{8 o'clock}$''',
r'''When the point of tangency has moved through an angle $\theta$ around the clock, the centre of the disk has turned through $\theta$ about the clock's centre and the disk has rolled an arc $20\theta$, so the disk has turned through $\theta+\dfrac{20\theta}{10}=3\theta$. The arrow points up again when $3\theta=360^\circ$, i.e.\ $\theta=120^\circ$: $\boxed{\textbf{(C)}\ \text{4 o'clock}}$.''',
'Circles|Tangent circles|Rotations',4,
note='P1 of an AMC 10 marathon; repeat of an earlier record (aliased).')

# ---------------- 1789026 weighted-digit test for 2^n and 5^n
b.add(1789026,1,r'''Let $n$ be a positive integer, and let the last $n$ digits of a positive integer $N$ be $a_1a_2\ldots a_n$ (so $a_1$ is the digit in the $10^{n-1}$ place and $a_n$ is the units digit). A student proposes the following test:
\begin{quote}
$N$ is divisible by $2^n$ exactly when $n a_1+(n-1)a_2+(n-2)a_3+\dots+2a_{n-1}+a_n$ is divisible by $2^n$; and the same holds with $5^n$ in place of $2^n$.
\end{quote}
Prove or disprove the test. For which of the cases $2^1,2^2,5^1,5^2,2^3$ is it correct?''',
r'''\textbf{The correct test.} Since $10^n=2^n5^n$, every digit of $N$ beyond the last $n$ contributes a multiple of $10^n$. So
\[
N\equiv\overline{a_1a_2\ldots a_n}=10^{n-1}a_1+10^{n-2}a_2+\dots+10a_{n-1}+a_n \pmod{2^n}\ \text{and}\pmod{5^n},
\]
and $N$ is divisible by $2^n$ (or $5^n$) exactly when the number formed by its last $n$ digits is. The proposed test replaces the place values $10^{n-k}$ by the weights $n-k+1$; it is correct only when these agree modulo $2^n$ (or $5^n$) closely enough.

\textbf{$n=1$.} The weighted sum is $a_1$, the last digit, so the test is the usual test for $2$ and for $5$: correct.

\textbf{$2^2=4$.} The weighted sum is $2a_1+a_2$, and $10a_1+a_2-(2a_1+a_2)=8a_1\equiv0\pmod4$. So the two numbers have the same remainder modulo $4$ and the test is correct for $4$ (this is the familiar ``twice the tens digit plus the units digit'' rule).

\textbf{$5^2=25$: false.} $N=25$ is divisible by $25$, but $2\cdot2+5=9$ is not.

\textbf{$2^3=8$: false.} $N=104=8\cdot13$ is divisible by $8$, but $3\cdot1+2\cdot0+4=7$ is not.

So the test is $\boxed{\text{false in general}}$: it is correct for $2$, $5$ and $4$, and fails for $25$ (counterexample $25$) and for $8$ (counterexample $104$). The reliable test uses the number formed by the last $n$ digits.''',
'Divisibility rules|Counterexamples|Remainders and congruences',3,
note='The post\'s statement is garbled ("if the number a1*n+...+an is divisible by 2, then the original number is divisible by 2"); it is read as the claim that N is divisible by 2^n (or 5^n) exactly when the weighted sum is. The record asks to prove or disprove it: true for 2, 4, 5, false for 25 and 8.')

# ---------------- 1789002 digit sum of 3+33+...+33...3
b.add(1789002,1,r'''Find the sum of the digits of the number
\[
3+33+333+3333+\dots+\underbrace{33\ldots3}_{49\text{ digits}} .
\]''',
r'''The number with $k$ threes is $\dfrac{3\left(10^k-1\right)}{9}=\dfrac{10^k-1}{3}$. Hence
\[
S=\sum_{k=1}^{49}\dfrac{10^k-1}{3}=\dfrac13\left(\dfrac{10^{50}-10}{9}-49\right)=\dfrac{10^{50}-451}{27}.
\]
Write $10^{50}-451=100\left(10^{48}-1\right)-351$. Since $999=27\cdot37$, the number $10^{48}-1$ (forty-eight nines, i.e.\ sixteen blocks $999$) divided by $27$ is sixteen blocks $037$:
\[
\dfrac{10^{48}-1}{27}=\underbrace{037\,037\ldots037}_{16\text{ blocks}} .
\]
Therefore
\[
S=100\cdot\dfrac{10^{48}-1}{27}-13=37\,\underbrace{037\ldots037}_{14\text{ blocks}}\,03700-13=37\,\underbrace{037\ldots037}_{14\text{ blocks}}\,03687 .
\]
The digit sum is $(3+7)+14\cdot(0+3+7)+(0+3+6+8+7)=10+140+24=\boxed{174}$.''',
'Place value|Summation|Geometric sequences|Digit problems',4)

# ---------------- 1789143 trophies for 30 runners
b.add(1789143,1,r'''In a race with $30$ runners, $8$ distinct trophies (first place, second place, \ldots, eighth place) are given to the top $8$ runners. In how many ways can the trophies be awarded?''',
r'''The first-place trophy can go to any of the $30$ runners, second place to any of the remaining $29$, and so on down to eighth place, which has $23$ choices. So the number of ways is
\[
30\cdot29\cdot28\cdot27\cdot26\cdot25\cdot24\cdot23=\dfrac{30!}{22!}=\boxed{235989936000}.
\]''',
'Permutations|Multiplication principle',1,
note='P1 of a combinatorics marathon (later posts not included).')

# ---------------- 1789170 formula for nCr (alias)
b.add(1789170,1,r'''Prove that the number of ways to choose $r$ objects from $n$ distinct objects ($0\le r\le n$) is
\[
\dbinom nr=\dfrac{n!}{r!\,(n-r)!}.
\]''',
r'''Count the arrangements of $r$ of the $n$ objects in a row in two ways. Directly, there are $n(n-1)\cdots(n-r+1)=\dfrac{n!}{(n-r)!}$. Alternatively, first choose the set of $r$ objects ($\dbinom nr$ ways) and then order it ($r!$ ways). Hence $\dbinom nr\,r!=\dfrac{n!}{(n-r)!}$, which gives the formula. $\blacksquare$''',
'Combinations|Permutations|Double counting',2,
note='The post writes the formula as nCr=n!/r!*n-r!; read as n!/(r!(n-r)!). Repeat of an earlier record (aliased).')

# ---------------- 1789162 operators marathon P1
b.add(1789162,1,r'''Insert operation signs from $+,-,\times,\div$ between the numbers below (keeping them in this order, and with the usual order of operations) to make a true equation:
\[
10\quad 8\quad 7\quad 6\quad 2\;=\;63 .
\]''',
r'''Multiplication and division are done before addition and subtraction. Since $63$ is close to $8\times7=56$, try $10+8\times7$, which is $66$; it then remains to subtract $3=6\div2$:
\[
\boxed{10+8\times7-6\div2=63},
\]
because $10+56-3=63$. (Other solutions with parentheses may exist; one is enough.)''',
'Order of operations|Construction',2,
note='P1 of an "operators marathon"; the rules allow any operations, and the record asks for one valid expression.')

# ---------------- 1789101 Brady's weights
b.add(1789101,1,r'''To weigh an object with a balance scale, Brady places the object on one pan and places some of his weights on either pan (or both) until the two pans balance. Brady's set of weights contains the minimum number of weights needed to be able to measure every whole-number weight from $1$ to $40$ pounds, inclusive. What is the greatest weight, in pounds, in Brady's set?''',
r'''\textbf{At least four weights.} Each weight is on the object's pan, on the other pan, or unused, so $k$ weights give at most $3^k$ arrangements. One arrangement is ``all unused'', and the others come in pairs (swap the pans) giving opposite net amounts, so at most $\dfrac{3^k-1}{2}$ positive amounts can be measured. For $k=3$ this is $13<40$, so at least $4$ weights are needed.

\textbf{Four weights suffice: $1,3,9,27$.} Every integer from $1$ to $40$ can be written as $\sum c_i3^i$ ($i=0,1,2,3$) with $c_i\in\{-1,0,1\}$ (balanced ternary); for example $40=27+9+3+1$, $20=27-9+3-1$ and $14=27-9-3-1$. A weight with $c_i=1$ goes on the pan opposite the object and one with $c_i=-1$ goes beside the object.

\textbf{The set is forced.} With four weights there are exactly $\dfrac{3^4-1}{2}=40$ positive arrangements, so every amount $1,\dots,40$ is obtained by exactly one arrangement (up to swapping pans), and the total $T$ of the weights is the largest amount, so $T=40$. Measure an arrangement by its \emph{deficit} $40-(\text{amount})$: an unused weight $w$ lowers the amount by $w$ and a weight beside the object lowers it by $2w$. So the deficits are exactly the numbers $\sum c_iw_i$ with $c_i\in\{0,1,2\}$, and they must be the $81$ numbers $0,1,\dots,80$, each obtained once. Now build up from the smallest weight:
\begin{itemize}
\item Deficit $1$ needs a weight $1$. With it, deficits $0,1,2$ are made; a weight $2$ would make deficit $2$ twice, so the next weight is at least $3$, and deficit $3$ forces a weight $3$.
\item With $1$ and $3$, the deficits $0,\dots,8$ are each made once; a weight between $4$ and $8$ would repeat one, and deficit $9$ forces a weight $9$.
\item With $1,3,9$, the deficits $0,\dots,26$ are made; likewise the last weight is $27$ (and indeed $1+3+9+27=40$).
\end{itemize}
So Brady's set is $\{1,3,9,27\}$, and the greatest weight is $\boxed{27}$ pounds.''',
'Digits and bases|Bounding and extremal cases|Logical deduction',4,source=src('MATHCOUNTS',None,None,None),
note='MATHCOUNTS problem (year not given); posted answer 27 confirmed. The solution also proves that the minimal set is unique.')

# ---------------- 1788776 special factorisations
b.add(1788776,1,r'''\begin{enumerate}
\item[(a)] Prove the identities
\[
a^2-b^2=(a-b)(a+b),\qquad a^3-b^3=(a-b)(a^2+ab+b^2),\qquad a^3+b^3=(a+b)(a^2-ab+b^2).
\]
\item[(b)] Explain why one would expect $a-b$ to be a factor of $a^3-b^3$ and $a+b$ to be a factor of $a^3+b^3$ before multiplying anything out.
\item[(c)] Prove that $a^2+b^2$ cannot be written as a product $(pa+qb)(ra+sb)$ with real numbers $p,q,r,s$.
\end{enumerate}''',
r'''\textbf{(a)} Expand the right-hand sides:
\[
(a-b)(a+b)=a^2+ab-ab-b^2=a^2-b^2,
\]
\[
(a-b)(a^2+ab+b^2)=a^3+a^2b+ab^2-a^2b-ab^2-b^3=a^3-b^3,
\]
\[
(a+b)(a^2-ab+b^2)=a^3-a^2b+ab^2+a^2b-ab^2+b^3=a^3+b^3 .
\]
In each product the middle terms cancel in pairs.

\textbf{(b)} Think of $a^3-b^3$ as a polynomial in $a$. It is $0$ when $a=b$, so by the factor theorem $a-b$ divides it. Likewise $a^3+b^3$ is $0$ when $a=-b$, so $a-(-b)=a+b$ divides it. The other factor is then found by division, and its form is forced: it must be a quadratic whose leading term is $a^2$ and whose last term is $\pm b^2$.

\textbf{(c)} Suppose $a^2+b^2=(pa+qb)(ra+sb)$ for all real $a,b$. Put $b=1$: then $a^2+1=(pa+q)(ra+s)$ for all $a$. Comparing the coefficients of $a^2$ gives $pr=1$, so $p\ne0$, and then $a=-\dfrac qp$ is a real number at which the right side is $0$. But $a^2+1\ge1>0$ for every real $a$, a contradiction. So $\boxed{a^2+b^2\text{ has no factorisation into real linear factors}}$. $\blacksquare$''',
'Factoring|Difference of squares|Sum and difference of cubes|Algebraic expressions and identities|Remainder theorem and factor theorem',2,
note='The post asks how the special factorisations work (whether to memorise them); turned into proofs of the identities, the factor-theorem reason behind them, and a proof that a^2+b^2 does not factor over the reals.')

# ---------------- 1788416 11^12 mod 13
b.add(1788416,1,r'''What is the remainder when $11^{12}$ is divided by $13$?''',
r'''Since $11\equiv-2\pmod{13}$,
\[
11^{12}\equiv(-2)^{12}=2^{12}=\left(2^6\right)^2=64^2\pmod{13}.
\]
Now $64=5\cdot13-1\equiv-1\pmod{13}$, so $11^{12}\equiv(-1)^2=1\pmod{13}$. The remainder is $\boxed{1}$.

(This is also Fermat's little theorem: $13$ is prime and $13\nmid11$, so $11^{12}\equiv1\pmod{13}$.)''',
'Remainders and congruences|Modular exponentiation|Fermat\'s little theorem',2)

# ---------------- 1788191 geometric probability in a box
fig=r'''import graph;
real r1=2, r2=sqrt(15);
pair O=(0,0), Q=(sqrt(6),3);
real th=degrees(atan(3/sqrt(6)));
path reg=arc(O,r2,0,th)--(0,3)--(0,r1)--arc(O,r1,90,0)--cycle;
fill(reg,lightgray);
draw((0,0)--(5,0)--(5,3)--(0,3)--cycle,linewidth(0.9));
draw(arc(O,r1,0,90),linewidth(0.8));
draw(arc(O,r2,0,th),linewidth(0.8));
draw(O--Q,dashed);
dot(Q);
label("$O$",O,SW);label("$(5,0)$",(5,0),S);label("$(5,3)$",(5,3),NE);label("$(0,3)$",(0,3),W);
label("$Q(\sqrt6,3)$",Q,N);
label("$2$",(2,0),S);label("$\sqrt{15}$",(sqrt(15),0),S);
draw(arc(O,0.75,0,th),linewidth(0.5));
label("$\theta$",1.05*dir(th/2));'''
b.add(1788191,1,r'''A point $(x,y)$ is chosen uniformly at random from the rectangle with vertices $(0,0)$, $(0,3)$, $(5,0)$ and $(5,3)$. What is the probability that $4\le x^2+y^2\le15$?''',
r'''The probability is the area of the region of the rectangle between the circles $x^2+y^2=4$ and $x^2+y^2=15$, divided by the rectangle's area $15$.
'''+asy(fig,'7.5cm')+r'''
\textbf{Inside the larger circle.} Since $\sqrt{15}<5$, the circle of radius $\sqrt{15}$ does not reach the side $x=5$, but it crosses the top side $y=3$ at $Q=(\sqrt6,3)$, because $6+9=15$. The part of the rectangle inside this circle is the right triangle with vertices $O$, $(0,3)$, $Q$, of area $\dfrac12\cdot3\cdot\sqrt6=\dfrac{3\sqrt6}{2}$, together with the circular sector between the $x$-axis and $OQ$, of angle $\theta=\arctan\dfrac{3}{\sqrt6}=\arctan\dfrac{\sqrt6}{2}$ and area $\dfrac12\cdot15\,\theta$.

\textbf{Inside the smaller circle.} The quarter disc of radius $2$ lies inside the rectangle (as $2<3$) and has area $\dfrac14\cdot4\pi=\pi$.

So the shaded region has area $\dfrac{3\sqrt6}{2}+\dfrac{15}{2}\arctan\dfrac{\sqrt6}{2}-\pi$, and the probability is
\[
\boxed{\dfrac{\sqrt6}{10}+\dfrac12\arctan\dfrac{\sqrt6}{2}-\dfrac{\pi}{15}}\approx0.479 .
\]''',
'Geometric probability|Circles|Lengths, perimeter, and area|Area decomposition|Trigonometry',4,
note='Exact answer involves an inverse tangent; the value was checked by numerical integration and Monte Carlo.')

# ---------------- 1788440 Connex
b.add(1788440,1,r'''The game of Connex contains one $4$-unit piece, two identical $3$-unit pieces, three identical $2$-unit pieces and four identical $1$-unit pieces. How many different arrangements of pieces (in a row) will make a $10$-unit segment? The $10$-unit segments made of the pieces $4$-$3$-$2$-$1$ and $1$-$2$-$3$-$4$ count as two different arrangements.''',
r'''First choose how many pieces of each size are used, say $a$ fours, $b$ threes, $c$ twos and $d$ ones, with $a\le1$, $b\le2$, $c\le3$, $d\le4$ and $4a+3b+2c+d=10$. Since pieces of the same size are identical, such a choice can be put in a row in $\dfrac{(a+b+c+d)!}{a!\,b!\,c!\,d!}$ ways. The possible choices are:
\[
\begin{array}{c|c|c}
\text{pieces used} & \text{number of pieces} & \text{arrangements}\\ \hline
2,2,2,1,1,1,1 & 7 & \dfrac{7!}{3!\,4!}=35\\
3,2,2,1,1,1 & 6 & \dfrac{6!}{2!\,3!}=60\\
3,2,2,2,1 & 5 & \dfrac{5!}{3!}=20\\
3,3,1,1,1,1 & 6 & \dfrac{6!}{2!\,4!}=15\\
3,3,2,1,1 & 5 & \dfrac{5!}{2!\,2!}=30\\
3,3,2,2 & 4 & \dfrac{4!}{2!\,2!}=6\\
4,2,1,1,1,1 & 6 & \dfrac{6!}{4!}=30\\
4,2,2,1,1 & 5 & \dfrac{5!}{2!\,2!}=30\\
4,2,2,2 & 4 & \dfrac{4!}{3!}=4\\
4,3,1,1,1 & 5 & \dfrac{5!}{3!}=20\\
4,3,2,1 & 4 & 4!=24\\
4,3,3 & 3 & \dfrac{3!}{2!}=3
\end{array}
\]
(Without the $4$-piece: with no $3$s we need $2c+d=10$, only $c=3,d=4$; with one $3$, $2c+d=7$ gives $(c,d)=(2,3),(3,1)$; with two $3$s, $2c+d=4$ gives $(0,4),(1,2),(2,0)$. With the $4$-piece: no $3$s, $2c+d=6$ gives $(1,4),(2,2),(3,0)$; one $3$, $2c+d=3$ gives $(0,3),(1,1)$; two $3$s, $2c+d=0$.)

The total is $35+60+20+15+30+6+30+30+4+20+24+3=\boxed{277}$.''',
'Multiset permutations|Casework|Partitions and compositions',4,source=src('MATHCOUNTS',2013,'State',None,rnd='Sprint'),
note='2013 MATHCOUNTS State Sprint (number not given). Counted by brute force as well.')

# ---------------- 1787416 altitude and areas
fig=r'''pair B=(0,0),C=(14,0),A=(9,12),D=(9,0);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--D,linewidth(0.8));
draw((9,0)--(9,0.7)--(8.3,0.7)--(8.3,0),linewidth(0.5));
fill(A--D--C--cycle,lightgray+opacity(0.5));
draw(A--B--C--cycle,linewidth(0.9));draw(A--D,linewidth(0.8));
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$D$",D,S);
label("$15$",(A+B)/2,NW);label("$13$",(A+C)/2,NE);
label("$12$",(9,6),W);
label("$9$",(4.5,0),S);label("$5$",(11.5,0),S);'''
b.add(1787416,1,r'''Triangle $ABC$ is acute-angled with $AB=15$ and $AC=13$. The point $D$ is the foot of the perpendicular from $A$ to $BC$, and the area of triangle $ADC$ is $30$. If the area of triangle $ABC$ is an integer, what is it?''',
r'''Triangle $ADC$ has a right angle at $D$, so
\[
AD^2+DC^2=13^2=169,\qquad \dfrac12\,AD\cdot DC=30\ \Longrightarrow\ AD\cdot DC=60 .
\]
Then $(AD+DC)^2=169+120=289$ and $(AD-DC)^2=169-120=49$, so $AD+DC=17$, $|AD-DC|=7$, and $\{AD,DC\}=\{12,5\}$.

\textbf{Case $AD=12$, $DC=5$.} In right triangle $ADB$, $BD=\sqrt{15^2-12^2}=9$. In an acute triangle the foot of an altitude lies between the other two vertices, so $BC=BD+DC=14$ and
\[
[ABC]=\dfrac12\cdot14\cdot12=84 .
\]
'''+asy(fig,'7cm')+r'''
\textbf{Case $AD=5$, $DC=12$.} Then $BD=\sqrt{225-25}=10\sqrt2$, and the area $\dfrac12\cdot5\,(10\sqrt2+12)=30+25\sqrt2$ is not an integer. (This triangle, with $BC=10\sqrt2+12$, is not even acute: $15^2+13^2=394<BC^2$.)

Hence the area of triangle $ABC$ is $\boxed{84}$; it is the $13$-$14$-$15$ triangle.''',
'Triangles|Right triangles|Pythagorean theorem|Altitudes|Lengths, perimeter, and area',4,
note='The post says the triangle is "right-angled", which is impossible: with the right angle at B or C the foot D is a vertex (area ADC = 0), and with the right angle at A the area of ADC would be 169*195/788, not 30. Replaced by "acute-angled", which puts D between B and C. (Without that condition D could also lie outside BC, giving BC = 4 and area 24.)')

# ---------------- 1788621 same number of digits in base 5 and base 8
b.add(1788621,1,r'''How many positive integers have the same number of digits when written in base $5$ and in base $8$?''',
r'''A positive integer $m$ has $d$ digits in base $5$ exactly when $5^{d-1}\le m<5^d$, and $d$ digits in base $8$ exactly when $8^{d-1}\le m<8^d$. Both hold when $8^{d-1}\le m<5^d$ (since $8^{d-1}\ge5^{d-1}$ and $5^d<8^d$). The number of such $m$ is $5^d-8^{d-1}$ when this is positive:
\[
d=1:\ 5-1=4,\qquad d=2:\ 25-8=17,\qquad d=3:\ 125-64=61,\qquad d=4:\ 625-512=113 .
\]
For $d=5$, $8^4=4096>5^5=3125$, and for larger $d$ the gap only grows, since $\dfrac{8^{d}}{5^{d+1}}=\dfrac{8}{5}\cdot\dfrac{8^{d-1}}{5^{d}}$. So the total is $4+17+61+113=\boxed{195}$.''',
'Digits and bases|Exponents|Systematic counting',3)

# ---------------- 1788511 Kangaroo proper divisors
b.add(1788511,1,r'''A divisor of a natural number is called \emph{proper} if it is greater than $1$ and smaller than the number. For how many natural numbers is the largest proper divisor $45$ times the smallest proper divisor?

$\textbf{(A)}\ 0\qquad\textbf{(B)}\ 1\qquad\textbf{(C)}\ 2\qquad\textbf{(D)}\ 3\qquad\textbf{(E)}\ \text{more than }3$''',
r'''Let $n$ have a proper divisor, and let $p$ be its smallest prime factor. Then the smallest proper divisor is $p$ and the largest is $\dfrac np$. The condition $\dfrac np=45p$ gives $n=45p^2=3^2\cdot5\cdot p^2$.

For $p$ to be the smallest prime factor of $n$ we need $p\le3$, since $3\mid n$. Both values work:
\begin{itemize}
\item $p=2$: $n=180$, smallest proper divisor $2$, largest $90=45\cdot2$;
\item $p=3$: $n=405$, smallest proper divisor $3$, largest $135=45\cdot3$.
\end{itemize}
So there are exactly two such numbers: $\boxed{\textbf{(C)}\ 2}$.''',
'Factors and multiples|Prime factorisation|Divisibility',3,source=src('Math Kangaroo',2009,'Grade 7-8',25))

# ---------------- 1788057 four consecutive integers
b.add(1788057,1,r'''How many sets of four consecutive positive integers are there such that the product of the four integers is less than $100{,}000$?''',
r'''Let the integers be $n,n+1,n+2,n+3$ with $n\ge1$. Pair the outer and the inner terms:
\[
n(n+3)\cdot(n+1)(n+2)=(n^2+3n)(n^2+3n+2)=(n^2+3n+1)^2-1 .
\]
So the product is less than $100000$ exactly when $(n^2+3n+1)^2\le100000$, i.e.\ $n^2+3n+1\le316$, because $316^2=99856\le100000<317^2=100489$. The left side increases with $n$; for $n=16$ it is $256+48+1=305\le316$, and for $n=17$ it is $289+51+1=341>316$. Hence $n=1,2,\dots,16$ work, giving $\boxed{16}$ sets. (Check: $16\cdot17\cdot18\cdot19=93024$ and $17\cdot18\cdot19\cdot20=116280$.)''',
'Algebraic expressions and identities|Inequalities|Perfect squares',3)

# ---------------- 1787875 meeting in the park
b.add(1787875,1,r'''Alice and Bill hope to meet at the park. Each arrives at a random time (uniformly and independently) between 11{:}00 AM and 6{:}30 PM, stays for exactly $45$ minutes and then leaves. What is the probability that they are at the park together for at least $10$ minutes?''',
r'''Measure arrival times $x$ (Alice) and $y$ (Bill) in minutes after 11{:}00; the pair $(x,y)$ is uniform on the square $[0,450]^2$. If $|x-y|<45$ the two visits overlap for $45-|x-y|$ minutes, and otherwise not at all. So they are together for at least $10$ minutes exactly when $|x-y|\le35$.

The complement $|x-y|>35$ consists of two right isosceles triangles with legs $450-35=415$, of total area $415^2$. Hence
\[
P=1-\left(\dfrac{415}{450}\right)^2=1-\left(\dfrac{83}{90}\right)^2=1-\dfrac{6889}{8100}=\boxed{\dfrac{1211}{8100}}\approx0.150 .
\]''',
'Geometric probability|Complementary probability',4)

# ---------------- 1788156 magic square
b.add(1788156,1,r'''Complete the $3\times3$ magic square below, in which every row, every column and both main diagonals have the same sum.
\[
\begin{array}{|c|c|c|}\hline 25 & b & 10\\ \hline d & 14 & f\\ \hline g & h & i\\ \hline\end{array}
\]''',
r'''\textbf{The magic sum.} Let the common sum be $s$. Add the middle row, the middle column and the two diagonals: every entry is counted once except the centre, which is counted four times. So $4s=(\text{sum of all entries})+3\cdot14=3s+42$, and $s=42$; in general the centre is one third of the magic sum.

\textbf{The entries.} The diagonals through the centre give $25+14+i=42$ and $10+14+g=42$, so $i=3$ and $g=18$. Then:
\[
b=42-25-10=7,\quad h=42-7-14=21,\quad d=42-25-18=-1,\quad f=42-10-3=29 .
\]
\[
\boxed{\begin{array}{|c|c|c|}\hline 25 & 7 & 10\\ \hline -1 & 14 & 29\\ \hline 18 & 21 & 3\\ \hline\end{array}}
\]
Check: rows $42,42,42$; columns $25-1+18=42$, $7+14+21=42$, $10+29+3=42$; diagonals $25+14+3=42$, $10+14+18=42$. (The solution is forced, and it contains the negative entry $-1$; with only positive entries the square would be impossible.)''',
'Magic squares|Systems of linear equations',3,
note='The entries are all forced; the square necessarily contains the negative number -1, which the post does not forbid.')

# ---------------- 1786814 USAMO 1984 quartic
b.add(1786814,1,r'''The product of two of the four roots of the quartic equation
\[
x^4-18x^3+kx^2+200x-1984=0
\]
is $-32$. Find $k$.''',
r'''The product of all four roots is $-1984$, so the other two roots have product $\dfrac{-1984}{-32}=62$. Group the roots into these two pairs; then the quartic factors as
\[
(x^2+ax-32)(x^2+bx+62)
\]
for some numbers $a,b$ (minus the sums of the pairs). Expanding,
\[
x^4+(a+b)x^3+(30+ab)x^2+(62a-32b)x-1984 .
\]
Comparing coefficients: $a+b=-18$ and $62a-32b=200$. Substituting $b=-18-a$ gives $94a+576=200$, so $a=-4$ and $b=-14$. Therefore
\[
k=30+ab=30+56=\boxed{86}.
\]''',
'Polynomials|Polynomial roots|Vieta\'s formulas|Factoring',5,source=src('USAMO',1984,None,1))

# ---------------- 1787435 square on a circle (alias)
b.add(1787435,1,r'''A square of side length $1$ inch is drawn with its centre $A$ on a circle with centre $O$ and radius $1$ inch, such that a side of the square is perpendicular to $OA$. What is the area of the region inside both the square and the circle? Express your answer as a decimal to the nearest hundredth.''',
r'''Put $O$ at the origin and $A=(1,0)$; the square is $\dfrac12\le x\le\dfrac32$, $|y|\le\dfrac12$. The region is the circular segment cut off by $x=\dfrac12$ (area $\dfrac{\pi}{3}-\dfrac{\sqrt3}{4}$) minus the two caps outside $|y|\le\dfrac12$, which gives $\dfrac{\pi}{6}+\dfrac{\sqrt3}{4}-\dfrac12\approx\boxed{0.46}$.''',
'Circles|Squares|Lengths, perimeter, and area',4,source=src('MATHCOUNTS',2013,'State',10,rnd='Team'),
note='The shaded region is only in the missing figure; the reading "inside both the square and the circle" matches the official answer 0.46. Repeat of an earlier record (aliased).')

# ---------------- 1787556 missing coordinates and slope
fig=r'''import graph;
real f(real x){return (2-3x)/9;}
draw((-1.7,0)--(1.4,0),Arrow(6));draw((0,-0.45)--(0,0.8),Arrow(6));
label("$x$",(1.4,0),E);label("$y$",(0,0.8),N);
draw(graph(f,-1.6,1.3),blue+linewidth(0.9));
pair A=(-1/3,1/3),B=(2/3,0);
dot(A);dot(B);
draw((-1/3,0)--A--(0,1/3),dashed+gray);
label("$A$",A,N);label("$-\dfrac13$",(-1/3,0),S);draw((0,1/3)--(0.04,1/3));label("$\dfrac13$",(0.03,1/3),dir(20),fontsize(9pt));
label("$B$",B,SW);label("$\dfrac23$",(2/3,0),2*N);
label("$3x+9y=2$",(1.3,f(1.3)),SE,blue);'''
b.add(1787556,1,r'''The points $A\left(\ ?\ ,\ \dfrac13\right)$ and $B\left(\dfrac23,\ ?\ \right)$ lie on the line $3x+9y=2$. Find the missing coordinates, and then find the slope of the line.''',
r'''\textbf{$A$.} With $y=\dfrac13$: $3x+3=2$, so $x=-\dfrac13$ and $A=\left(-\dfrac13,\dfrac13\right)$.

\textbf{$B$.} With $x=\dfrac23$: $2+9y=2$, so $y=0$ and $B=\left(\dfrac23,0\right)$.

\textbf{Slope.} Through $A$ and $B$,
\[
m=\dfrac{0-\dfrac13}{\dfrac23-\left(-\dfrac13\right)}=\dfrac{-\dfrac13}{1}=\boxed{-\dfrac13}.
\]
(Equivalently, $y=-\dfrac13x+\dfrac29$.)
'''+asy(fig,'7cm'),
'Linear equations|Slope|Coordinate geometry',1,
note='The post reads "6.3x+9y=2"; the "6." is read as the exercise number, so the line is 3x+9y=2 (with x = 6.3 the y-coordinate of A would give no tidy answer).')

# ---------------- 1787527 dice and primes
b.add(1787527,1,r'''What is the least number of standard six-sided dice that must be rolled so that there is at least an $80\%$ chance of getting at least $2$ prime numbers?''',
r'''The primes on a die are $2,3,5$, so each die shows a prime with probability $\dfrac12$, independently. With $n$ dice, the probability of fewer than two primes is
\[
\left(\dfrac12\right)^n+n\left(\dfrac12\right)^n=\dfrac{n+1}{2^n}.
\]
We need $\dfrac{n+1}{2^n}\le\dfrac15$. For $n=4$, $\dfrac5{16}=0.3125$ is too large; for $n=5$, $\dfrac6{32}=0.1875\le0.2$. Since $\dfrac{n+1}{2^n}$ decreases for $n\ge1$, the least number is $\boxed{5}$ (probability $\dfrac{13}{16}=81.25\%$).''',
'Binomial probability|Complementary probability|Dice probability',3)

# ---------------- 1787633 last two nonzero digits
b.add(1787633,1,r'''What are the last two nonzero digits of $1^{100}\cdot2^{200}\cdot3^{300}\cdot4^{400}\cdot5^{500}$?''',
r'''Since $4^{400}=2^{800}$, the product is
\[
2^{1000}\cdot3^{300}\cdot5^{500}=10^{500}\cdot2^{500}\cdot3^{300}.
\]
The number $M=2^{500}\cdot3^{300}$ is not divisible by $5$, so it does not end in $0$, and the last two nonzero digits of the product are the last two digits of $M$, i.e.\ $M\bmod100$.

\textbf{$2^{500}\bmod100$.} It is $0\pmod4$. Modulo $25$: $2^{10}=1024\equiv-1$, so $2^{20}\equiv1$ and $2^{500}=\left(2^{20}\right)^{25}\equiv1\pmod{25}$. The number in $0,\dots,99$ that is $0\pmod4$ and $1\pmod{25}$ is $76$.

\textbf{$3^{300}\bmod100$.} $3^{10}=59049\equiv49$ and $3^{20}\equiv49^2=2401\equiv1\pmod{100}$, so $3^{300}=\left(3^{20}\right)^{15}\equiv1$.

Therefore $M\equiv76\cdot1=76\pmod{100}$, and the last two nonzero digits are $\boxed{76}$.''',
'Units digits and last digits|Modular exponentiation|Chinese remainder theorem|Remainders and congruences',4)

b.save()
