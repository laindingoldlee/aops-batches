from qb import *
b=Bank('en02')

# ---------------- 1792312 last 3 digits of 2^178
b.add(1792312,1,r'''What are the last three digits of $2^{178}$?''',
r'''We need $2^{178}\bmod 1000$, and $1000=8\cdot125$ with $\gcd(8,125)=1$.

\textbf{Modulo $8$:} $2^{178}\equiv0$.

\textbf{Modulo $125$:} $\varphi(125)=100$ and $\gcd(2,125)=1$, so by Euler's theorem $2^{100}\equiv1$ and $2^{178}\equiv2^{78}$. Now $2^7=128\equiv3$, so $2^{78}=\left(2^7\right)^{11}\cdot2\equiv3^{11}\cdot2$. Since $3^5=243\equiv-7$, we get $3^{10}\equiv49$ and $3^{11}\equiv147\equiv22$, so $2^{178}\equiv44\pmod{125}$.

\textbf{Combine:} the numbers below $1000$ that are $\equiv44\pmod{125}$ are $44,169,294,419,544,\dots$; the first one divisible by $8$ is $544=8\cdot68$. By the Chinese remainder theorem $2^{178}\equiv544\pmod{1000}$, so the last three digits are $\boxed{544}$.''',
'Modular exponentiation|Euler\'s theorem and totient|Chinese remainder theorem|Units digits and last digits|Remainders and congruences',4)

# ---------------- 1791613 four points on circle (alias)
b.add(1791613,1,r'''Four points are chosen at random on the circumference of a circle. What is the probability that the quadrilateral formed by the four points contains the centre of the circle?''',
r'''The quadrilateral misses the centre exactly when all four points lie in a semicircle. For each point $P$, the probability that the other three lie in the semicircle starting at $P$ going clockwise is $\dfrac18$, and these four events are disjoint, so the points lie in a semicircle with probability $\dfrac48=\dfrac12$. The answer is $1-\dfrac12=\boxed{\dfrac12}$.''',
'Geometric probability|Probability|Complementary probability',4,
note='Repeat of an earlier record (aliased).')

# ---------------- 1791940 no two from same grade adjacent
b.add(1791940,1,r'''Three eighth graders, four seventh graders and two sixth graders (nine different students) stand in a straight line. In how many ways can they arrange themselves so that no two students from the same grade stand next to each other?''',
r'''First count the \emph{grade patterns}: strings of three $E$'s (eighth), four $S$'s (seventh) and two $X$'s (sixth) with no two equal letters adjacent. Then multiply by the $3!\cdot4!\cdot2!$ ways to place the actual students.

\textbf{Place the $S$'s into a pattern of the other five letters.} Write the five letters $E,E,E,X,X$ in some order $w$; there are $\dbinom52=10$ such words. The four $S$'s go into the $6$ gaps of $w$ (before the first letter, between letters, after the last), at most one per gap, since two $S$'s may not be adjacent. If $w$ has $k$ places where two equal letters are adjacent, each of those $k$ gaps must receive an $S$, and the remaining $4-k$ $S$'s go into $4-k$ of the other $6-k$ gaps: $\dbinom{6-k}{4-k}$ ways.
\begin{itemize}
\item $k=0$: $EXEXE$; $\dbinom64=15$.
\item $k=1$: $EEXEX$, $EXEEX$, $XEEXE$, $XEXEE$; $\dbinom53=10$ each, total $40$.
\item $k=2$: $EEXXE$, $EXXEE$, $XEEEX$; $\dbinom42=6$ each, total $18$.
\item $k=3$: $EEEXX$, $XXEEE$; $\dbinom31=3$ each, total $6$.
\end{itemize}
(The words with $k\ge4$ would need more than four $S$'s; there are none.) So there are $15+40+18+6=79$ grade patterns.

\textbf{Students.} In each pattern the eighth graders can be placed in $3!$ ways, the seventh graders in $4!$ ways and the sixth graders in $2!$ ways, so the answer is
\[
79\cdot3!\cdot4!\cdot2!=79\cdot288=\boxed{22752}.
\]''',
'Arrangements with restrictions|Casework|Multiset permutations|Combinations|Multiplication principle',5,
note='The students are taken to be distinguishable (the answer would be 79 if only the grade pattern mattered). Checked by enumerating all patterns.')

# ---------------- 1792157 zeta(3) in terms of odd part
b.add(1792157,1,r'''Let
\[
x=\dfrac{1}{1^3}+\dfrac{1}{3^3}+\dfrac{1}{5^3}+\cdots
\]
be the sum of the reciprocals of the cubes of the odd positive integers. Express
\[
n=\dfrac{1}{1^3}+\dfrac{1}{2^3}+\dfrac{1}{3^3}+\cdots
\]
in terms of $x$.''',
r'''Both series have positive terms and converge (for example $\dfrac{1}{k^3}\le\dfrac{1}{k^2}$ and $\displaystyle\sum\dfrac1{k^2}$ converges), so we may split and regroup terms. Split $n$ into odd and even terms:
\[
n=\left(\dfrac{1}{1^3}+\dfrac1{3^3}+\cdots\right)+\left(\dfrac1{2^3}+\dfrac1{4^3}+\cdots\right)=x+\sum_{k\ge1}\dfrac{1}{(2k)^3}=x+\dfrac18\sum_{k\ge1}\dfrac1{k^3}=x+\dfrac n8 .
\]
Hence $\dfrac{7n}{8}=x$, and
\[
n=\boxed{\dfrac{8x}{7}}.
\]''',
'Sequences and series|Summation|Algebraic manipulation',3,source=src('Alabama SHSMC',2009,None,None,rnd='Comprehensive I'),
note='The post writes both series with only three terms; they are the infinite series (as the title says).')

# ---------------- 1791558 circle through C and two midpoints
fig=r'''pair B=(0,0),A=(0,12),C=(16,0),M=(0,6),Nn=(8,0),O=(12,41/3);
real r=abs(C-O);
draw(circle(O,r),blue);
draw(A--B--C--cycle,linewidth(0.9));
draw(B--(0.9,0)--(0.9,0.9)--(0,0.9));
draw(O--C,dashed);dot(O);dot(M);dot(Nn);
label("$A$",A,W);label("$B$",B,SW);label("$C$",C,SE);label("$M$",M,W);label("$N$",Nn,S);label("$O$",O,N);
label("$6$",(0,3),W);label("$8$",(4,0),S);label("$8$",(12,0),S);'''
b.add(1791558,1,r'''Let $ABC$ be a triangle with $AB=12$, $BC=16$ and $AC=20$. Compute the area of the circle that passes through $C$ and the midpoints of $AB$ and $BC$.''',
r'''Since $12^2+16^2=400=20^2$, the angle at $B$ is a right angle. Put $B=(0,0)$, $A=(0,12)$, $C=(16,0)$. The midpoints are $M=(0,6)$ of $AB$ and $N=(8,0)$ of $BC$.
'''+asy(fig,'6.5cm')+r'''
The centre $O$ of the circle is equidistant from $N$ and $C$, so it lies on $x=12$; write $O=(12,k)$. From $OM=OC$:
\[
12^2+(k-6)^2=4^2+k^2\ \Longrightarrow\ 144-12k+36=16\ \Longrightarrow\ k=\dfrac{164}{12}=\dfrac{41}{3}.
\]
Then $r^2=OC^2=4^2+\left(\dfrac{41}{3}\right)^2=\dfrac{144+1681}{9}=\dfrac{1825}{9}$, and the area is
\[
\pi r^2=\boxed{\dfrac{1825\pi}{9}}.
\]
(Alternatively, power of the point $B$: $BN\cdot BC=8\cdot16=128$, so the circle meets line $BA$ again at $BM'=\dfrac{128}{6}=\dfrac{64}{3}$, giving the same centre.)''',
'Circles|Right triangles|Midpoints|Coordinate geometry|Pythagorean theorem|Lengths, perimeter, and area',3)

# ---------------- 1791573 system xy=2(x+y)
b.add(1791573,1,r'''The nonzero numbers $x$, $y$ and $z$ satisfy
\[
xy=2(x+y),\qquad yz=4(y+z),\qquad xz=8(x+z).
\]
Solve for $x$.''',
r'''Divide each equation by the (nonzero) product on its left:
\[
\dfrac1x+\dfrac1y=\dfrac12,\qquad \dfrac1y+\dfrac1z=\dfrac14,\qquad \dfrac1x+\dfrac1z=\dfrac18 .
\]
Adding all three, $2\left(\dfrac1x+\dfrac1y+\dfrac1z\right)=\dfrac78$, so $\dfrac1x+\dfrac1y+\dfrac1z=\dfrac{7}{16}$. Subtracting the second equation, $\dfrac1x=\dfrac7{16}-\dfrac4{16}=\dfrac3{16}$, so $x=\boxed{\dfrac{16}{3}}$.

(Also $y=\dfrac{16}{5}$ and $z=-16$, and these satisfy all three original equations: for example $yz=-\dfrac{256}{5}=4\left(\dfrac{16}{5}-16\right)$.)''',
'Systems of linear equations|Substitution|Fractions',3)

# ---------------- 1791997 slanting lamp post shadow
fig=r'''real a=60,bt=60;
pair P=(0,0),T=4*dir(a),Q=(4*sin(radians(a+bt))/sin(radians(bt)),0);
draw((-1.5,0)--(Q.x+1.5,0),linewidth(0.6));
draw(P--T,linewidth(1.6));
draw(T--Q,dashed);
draw(P--Q,linewidth(2.2)+gray);
for(int i=0;i<3;++i){pair s=(-1.6+1.1*i,4.6); draw(s--s+1.2*dir(-bt),orange,Arrow);}
draw(arc(P,0.6,0,a),linewidth(0.5));label("$\alpha$",P+0.95*dir(a/2));
draw(arc(Q,0.7,180-bt,180),linewidth(0.5));label("$\beta$",Q+1.05*dir(180-bt/2));
label("$P$",P,S);label("$T$",T,N);label("$Q$",Q,S);
label("$L$",(P+T)/2,NW);label("shadow",(P+Q)/2,S);'''
b.add(1791997,1,r'''A straight lamp post $PT$ of length $L$ stands on level ground at $P$ and leans, so that it makes an angle $\alpha$ ($0^\circ<\alpha<90^\circ$) with the ground. The sun's rays make an angle $\beta$ ($0^\circ<\beta<90^\circ$) with the ground, and the post leans \emph{away} from the sun, in the vertical plane that contains the sun's rays.
\begin{enumerate}
\item[(a)] Find the length of the shadow of the post.
\item[(b)] Is the shadow of a slanting post always of a different length from the post? Find the condition for equal lengths and give an example.
\end{enumerate}''',
r'''(a) The ray through the top $T$ meets the ground at the tip $Q$ of the shadow, and the shadow is the segment $PQ$. Because the post leans away from the sun, $Q$ lies on the same side of $P$ as the foot of the perpendicular from $T$, and in triangle $PTQ$
\[
\angle TPQ=\alpha,\qquad \angle TQP=\beta,\qquad \angle PTQ=180^\circ-\alpha-\beta .
\]
'''+asy(fig,'6.5cm')+r'''
By the law of sines, $\dfrac{PQ}{\sin\angle PTQ}=\dfrac{PT}{\sin\beta}$, so the shadow has length
\[
\boxed{PQ=\dfrac{L\sin(\alpha+\beta)}{\sin\beta}}.
\]

(b) Not always. The lengths are equal exactly when $\sin(\alpha+\beta)=\sin\beta$. Since $0^\circ<\beta<\alpha+\beta<180^\circ$, this means $\alpha+\beta=180^\circ-\beta$, i.e.\ $\alpha=180^\circ-2\beta$, which is possible for $45^\circ<\beta<90^\circ$. For example, with $\alpha=\beta=60^\circ$ the triangle $PTQ$ is equilateral and the shadow is exactly as long as the post (this is the case drawn). In general the shadow is longer when $\alpha+\beta<180^\circ-\beta$ and shorter when $\alpha+\beta>180^\circ-\beta$; for instance, with $\beta=45^\circ$ it is always longer, and with $\beta=80^\circ$, $\alpha=60^\circ$ it is shorter. The shadow is the projection of the post along the sun's rays, and a projection along a slanted direction does not preserve lengths, but it can happen to match.

(If the post leans \emph{towards} the sun, the same argument gives length $\dfrac{L\,|\sin(\alpha-\beta)|}{\sin\beta}$, again sometimes equal to $L$.)''',
'Law of sines|Trigonometry|Triangles|Angle sums',3,
note='Conceptual question ("does the shadow of a slanting lamp post have the same length as the post?") turned into a law-of-sines problem in the plane of the sun\'s rays. The poster\'s guess that the length is always different is not quite right: it can be equal (e.g. alpha = beta = 60 degrees).')

# ---------------- 1791167 mock chapter
b.add(1791167,1,r'''Find the sum of the last three digits of $9^{2018}+9^{2019}$.''',
r'''We have $9^{2018}+9^{2019}=9^{2018}(1+9)=10\cdot9^{2018}$, so its last three digits are $10$ times the last two digits of $9^{2018}$. Modulo $100$: $9^2=81$, $9^4\equiv81^2=6561\equiv61$, $9^5\equiv61\cdot9=549\equiv49$, $9^{10}\equiv49^2=2401\equiv1$. Hence $9^{2018}=\left(9^{10}\right)^{201}\cdot9^8\equiv9^8=\left(9^4\right)^2\equiv61^2=3721\equiv21\pmod{100}$. So $9^{2018}+9^{2019}\equiv210\pmod{1000}$, the last three digits are $2,1,0$, and their sum is $\boxed{3}$.''',
'Modular exponentiation|Units digits and last digits|Remainders and congruences|Factoring',3,
note='Problem 1 of a user-written mock MATHCOUNTS Chapter set.')
b.add(1791167,2,r'''A subset (possibly empty) of the twelve numbers $7^0,7^1,\dots,7^{11}$ is chosen uniformly at random from all $2^{12}$ subsets. The probability that the sum of the numbers in the subset is divisible by $8$ can be written as $\dfrac{m}{2^n}$, where $m$ and $n$ are positive integers and $m$ is odd. Find $m+n$.''',
r'''Since $7\equiv-1\pmod8$, the six even powers are $\equiv1$ and the six odd powers are $\equiv-1\pmod8$. If the subset contains $a$ even powers and $b$ odd powers, its sum is $\equiv a-b\pmod8$. As $0\le a,b\le6$, we have $|a-b|\le6$, so $8\mid a-b$ only when $a=b$. The number of such subsets is
\[
\sum_{a=0}^{6}\dbinom6a^2=\dbinom{12}{6}=924
\]
(Vandermonde's identity). The probability is $\dfrac{924}{4096}=\dfrac{231}{1024}=\dfrac{231}{2^{10}}$, so $m+n=231+10=\boxed{241}$.''',
'Probability|Remainders and congruences|Combinations|Vandermonde\'s convolution',4,
note='The empty subset (sum 0) is counted, as required for the probability to have a power-of-2 denominator with all 2^12 subsets equally likely.')
b.add(1791167,3,r'''Four indistinguishable $12$-sided dice (faces $1$ to $12$) are rolled. How many different outcomes are possible in which the four values are distinct and no two of them differ by less than $2$?''',
r'''An outcome is a set $\{a<b<c<d\}\subseteq\{1,\dots,12\}$ with consecutive differences at least $2$. Put $a'=a$, $b'=b-1$, $c'=c-2$, $d'=d-3$. Then $1\le a'<b'<c'<d'\le9$, and this is a bijection with the $4$-element subsets of $\{1,\dots,9\}$. So the answer is $\dbinom94=\boxed{126}$.''',
'Combinations|Bijections|Dice probability',3)
b.add(1791167,4,r'''The six numbers $0,1,2,3,4,5$ are randomly assigned to the six variables $a,b,c,d,e,f$, one number to each variable, with all assignments equally likely. Find the probability that $\dfrac{a+b+c}{d+e+f}$ is an integer.''',
r'''Let $s=d+e+f$; then $a+b+c=15-s$ and $s\ge0+1+2=3>0$. The quotient $\dfrac{15-s}{s}=\dfrac{15}{s}-1$ is an integer exactly when $s\mid15$. Since $3\le s\le12$, we need $s=3$ or $s=5$. The $3$-element sets with sum $3$ or $5$ are $\{0,1,2\}$, $\{0,1,4\}$ and $\{0,2,3\}$. All $\dbinom63=20$ choices of the set $\{d,e,f\}$ are equally likely, so the probability is $\boxed{\dfrac{3}{20}}$.''',
'Probability|Divisibility|Combinations|Systematic counting',3,
note='The post says "Four numbers, 0, 1, 2, 3, 4, 5"; corrected to the six numbers, one per variable.')
b.add(1791167,5,r'''In how many ways can five people, A.M.C.~VIII, A.M.C.~X, A.M.C.~XII, A.I.M.E.\ and Bob, sit around a round table with five chairs if Bob does not want to sit next to A.I.M.E.? Two arrangements are the same if one is a rotation of the other.''',
r'''Up to rotation there are $(5-1)!=24$ arrangements. Count those with Bob next to A.I.M.E.: glue the two into a block, which can be ordered in $2$ ways; then $4$ units sit around the table in $(4-1)!=6$ ways, giving $12$. The answer is $24-12=\boxed{12}$.''',
'Circular arrangements|Complementary counting|Arrangements with restrictions',2)
fig=r'''real k=2*sqrt(3)-3;
void blob(pair c,real R,int lev,bool blue){
  if(lev==0) return;
  real r=k*R;
  for(int i=0;i<3;++i){pair cc=c+(R-r)*dir(90+120*i);
    filldraw(circle(cc,r),blue?rgb(0.35,0.55,0.95):white,black+linewidth(0.4));
    blob(cc,r,lev-1,!blue);}
}
draw(circle((0,0),2),linewidth(0.9));
blob((0,0),2,4,true);
draw((-2,-2.25)--(2,-2.25),Arrows(4));label("$4$",(0,-2.25),S);'''
b.add(1791167,6,r'''An infinite fractal is made as follows. A large white circle of diameter $4$ is drawn. Inside it, three mutually tangent blue circles of equal size are drawn, each tangent to the large circle. Inside each blue circle, three mutually tangent white circles of equal size are drawn, each tangent to that blue circle; inside each of these, three blue circles in the same way, and so on forever. Find the total area of the blue part of the figure. Express your answer as a decimal to the nearest thousandth.''',
r'''\textbf{The scale factor.} Let three mutually tangent circles of radius $r$ lie inside a circle of radius $R$, each tangent to it. Their centres form an equilateral triangle of side $2r$, whose centre is the centre of the big circle, at distance $\dfrac{2r}{\sqrt3}$ from each small centre. Hence $R=r+\dfrac{2r}{\sqrt3}$ and
\[
k=\dfrac rR=\dfrac{\sqrt3}{\sqrt3+2}=2\sqrt3-3,\qquad k^2=21-12\sqrt3 .
\]
'''+asy(fig,'5.5cm')+r'''
\textbf{The blue area.} With $R=2$, the three blue circles have total area $3k^2\cdot4\pi$; the nine white circles inside them have total area $9k^4\cdot4\pi$, which must be removed; the $27$ blue circles inside those are added back, and so on. So the blue area is
\[
4\pi\left(3k^2-9k^4+27k^6-\cdots\right)=4\pi\cdot\dfrac{3k^2}{1+3k^2},
\]
a geometric series with ratio $-3k^2$, where $3k^2=63-36\sqrt3\approx0.646<1$. Now
\[
\dfrac{3k^2}{1+3k^2}=\dfrac{63-36\sqrt3}{64-36\sqrt3}=\dfrac{(63-36\sqrt3)(64+36\sqrt3)}{64^2-36^2\cdot3}=\dfrac{144-36\sqrt3}{208}=\dfrac{9(4-\sqrt3)}{52},
\]
so the blue area is $\dfrac{9\pi(4-\sqrt3)}{13}\approx\boxed{4.933}$.''',
'Geometric sequences|Tangent circles|Circles|Lengths, perimeter, and area|Equilateral triangles',5,
note='Problem 6 of the mock set; its diagram was attached but the text determines the figure, which is redrawn (four levels shown). The garbled phrase "those blue circles each three smaller mutually tangent white circles" is read as each blue circle containing three white circles.')

# ---------------- 1790899 Henry
b.add(1790899,1,r'''Henry drove $100$ miles to visit a friend. If he had driven $8$ miles per hour faster than he did, he would have arrived in $\dfrac56$ of the time he actually took. How many minutes did the trip take?''',
r'''For a fixed distance, time is inversely proportional to speed. Taking $\dfrac56$ of the time means driving at $\dfrac65$ of the speed $v$, so $\dfrac65v=v+8$, giving $\dfrac v5=8$ and $v=40$ miles per hour. The trip took $\dfrac{100}{40}=2.5$ hours $=\boxed{150}$ minutes.''',
'Distance, rate, and time|Ratios, proportions, and variation|Linear equations',2)

# ---------------- 1791941 gold pieces; inequality
b.add(1791941,1,r'''Mr.\ Zero bought a number of gold pieces for $\$60$. He kept $15$ of them and sold the rest for $\$54$, making a profit of $10$ cents on each piece he sold. How many pieces did he buy?''',
r'''Let him buy $n$ pieces, at $\dfrac{60}{n}$ dollars each. He sold $n-15$ pieces for $\dfrac{54}{n-15}$ dollars each, which is $0.10$ dollars more than the cost:
\[
\dfrac{54}{n-15}=\dfrac{60}{n}+\dfrac1{10}.
\]
Multiplying by $10n(n-15)$: $540n=600(n-15)+n(n-15)$, i.e.\ $n^2+45n-9000=0$, so $(n-75)(n+120)=0$ and $n=\boxed{75}$. Check: each cost $\$0.80$, the $60$ sold pieces went for $\$0.90$ each, a total of $\$54$.''',
'Rational equations|Quadratic equations|Money and currency',3)
b.add(1791941,2,r'''How many integers $x$ satisfy $4(x-4)^2+2\le2x+6$?''',
r'''Expand: $4x^2-32x+64+2\le2x+6$, i.e.\ $4x^2-34x+60\le0$, or $2x^2-17x+30\le0$. This factors as $(2x-5)(x-6)\le0$, so $\dfrac52\le x\le6$. The integers in this interval are $3,4,5,6$: there are $\boxed{4}$.''',
'Quadratic equations|Inequalities|Factoring',2)

# ---------------- 1791855 make 20
b.add(1791855,1,r'''Using each of the six numbers $2,2,2,6,8,10$ exactly once, together with addition, subtraction, division, exponents, square roots, factorials and parentheses (but \emph{not} multiplication), make $20$.''',
r'''One solution uses only addition, subtraction and division:
\[
10+8+\dfrac62-\dfrac22=10+8+3-1=\boxed{20}.
\]
The numbers used are $10$, $8$, $6$ and three $2$'s, each exactly once.''',
'Order of operations|Whole-number operations|Construction',1,
note='Problem P1 of a "make the target number" marathon; the allowed operations are those listed in the post (multiplication is not among them). Any valid expression is accepted.')

# ---------------- 1791322 MATHCOUNTS Trainer probability
b.add(1791322,1,r'''A bag contains red balls and white balls. Five balls are drawn from the bag with replacement. The probability of getting exactly three red balls is $32$ times the probability of getting exactly one red ball. What percent of the balls in the bag are red?''',
r'''Let $p$ be the fraction of red balls and $q=1-p$. With replacement the draws are independent, so
\[
P(3\text{ red})=\dbinom53p^3q^2=10p^3q^2,\qquad P(1\text{ red})=\dbinom51pq^4=5pq^4 .
\]
The condition $10p^3q^2=32\cdot5pq^4$ gives (with $p,q\ne0$, since both probabilities would otherwise be $0$ and the condition would not determine anything) $p^2=16q^2$, so $p=4q=4(1-p)$ and $p=\dfrac45$. So $\boxed{80\%}$ of the balls are red.''',
'Binomial probability|Sampling with replacement|Percentages',3)

# ---------------- 1787964 squares and rectangles in grid
b.add(1787964,1,r'''An $n\times n$ grid is made of $n^2$ unit squares.
\begin{enumerate}
\item[(a)] How many squares (of all sizes) are formed by the grid lines?
\item[(b)] How many rectangles (including squares) are formed by the grid lines?
\end{enumerate}
Find formulas in terms of $n$, and evaluate them for the $8\times8$ chessboard.''',
r'''(a) A $k\times k$ square is determined by the position of its top-left corner. Its left edge can be on any of the first $n-k+1$ vertical grid lines and its top edge on any of the first $n-k+1$ horizontal lines, so there are $(n-k+1)^2$ such squares. Summing over $k=1,\dots,n$,
\[
\sum_{k=1}^{n}(n-k+1)^2=1^2+2^2+\cdots+n^2=\boxed{\dfrac{n(n+1)(2n+1)}{6}}.
\]
(b) A rectangle is determined by choosing $2$ of the $n+1$ vertical grid lines (its left and right sides) and $2$ of the $n+1$ horizontal grid lines (top and bottom), so there are
\[
\boxed{\dbinom{n+1}{2}^2=\left(\dfrac{n(n+1)}{2}\right)^2}
\]
rectangles. For $n=8$: $\dfrac{8\cdot9\cdot17}{6}=204$ squares and $36^2=1296$ rectangles. (For an $m\times n$ grid the same arguments give $\dbinom{m+1}{2}\dbinom{n+1}{2}$ rectangles and $\displaystyle\sum_{k\ge1}(m-k+1)(n-k+1)$ squares, summing while both factors are positive.)''',
'Counting shapes in figures|Combinations|Summation|Multiplication principle',3,
note='The post asks for formulas for the number of squares or rectangles in a grid (it also mentions triangles, which a square grid does not determine); the record asks for both formulas with proofs.')

# ---------------- 1791264 three dice sum < 8
b.add(1791264,1,r'''Three standard six-sided dice are rolled. What is the probability that the sum is less than $8$? Explain also which question the expression $\dfrac{\dbinom83}{216}$ answers.''',
r'''We count ordered triples $(a,b,c)$ of die values with $a+b+c\le7$. Since each value is at least $1$ and the sum is at most $7$, each value is at most $5$, so the upper limit $6$ never matters. Introduce a slack $s=7-(a+b+c)\ge0$ and put $a'=a-1$, $b'=b-1$, $c'=c-1$:
\[
a'+b'+c'+s=4,\qquad a',b',c',s\ge0 .
\]
By stars and bars there are $\dbinom{4+3}{3}=\dbinom73=35$ solutions. (Directly: sums $3,4,5,6,7$ occur $1,3,6,10,15$ times.) So the probability is
\[
\boxed{\dfrac{35}{216}}.
\]
The expression $\dfrac{\dbinom83}{216}=\dfrac{56}{216}$ comes from the same method with slack $8-(a+b+c)$: it counts the $56$ rolls with sum \emph{at most} $8$ (sum $8$ occurs $21$ times, and again no value can exceed $6$). So $\dbinom83$ is the answer to ``sum at most $8$'', not ``sum less than $8$''.''',
'Dice probability|Stars and bars|Distributions and integer solutions|Probability',3,
note='The math-club teacher\'s formula 8C3/216 = 56/216 counts sums at most 8; for "less than 8" the count is 7C3 = 35, probability 35/216 (checked by enumeration).')

# ---------------- 1791227 two dice
b.add(1791227,1,r'''Two standard dice are rolled. What is the probability that the number shown on one die is greater than the number shown on the other die? An answer key gives $\dfrac{13}{18}$; is it correct?''',
r'''One number is greater than the other exactly when the two numbers are different. Of the $36$ equally likely outcomes, $6$ are doubles, so the probability is $\dfrac{36-6}{36}=\boxed{\dfrac56}$. (By symmetry, the first die is greater with probability $\dfrac{15}{36}=\dfrac5{12}$ and the second is greater with probability $\dfrac5{12}$.)

The key's $\dfrac{13}{18}=\dfrac{26}{36}$ is not correct: it would require $26$ favourable outcomes, but there are $30$.''',
'Dice probability|Complementary probability|Probability',1,
note='The posted answer 13/18 is wrong for the question as stated; the correct probability is 5/6.')

# ---------------- 1788394 2015 Nat Sprint 11
qfig=r'''pair B=(0,0),A=(4,0),C=(0,4),D=(4,8),Ee=(8,4);
draw(A--B--C--cycle,linewidth(0.9));draw(A--C--D--Ee--cycle,linewidth(0.9));
draw((0.5,0)--(0.5,0.5)--(0,0.5));
label("$A$",A,S);label("$B$",B,SW);label("$C$",C,W);label("$D$",D,N);label("$E$",Ee,E);
label("$4$",(A+B)/2,S);'''
sfig=r'''pair B=(0,0),A=(4,0),C=(0,4),D=(4,8),Ee=(8,4);
draw(A--B--C--cycle,linewidth(0.9));draw(A--C--D--Ee--cycle,linewidth(0.9));
draw((0.5,0)--(0.5,0.5)--(0,0.5));
draw(B--Ee,red+linewidth(0.9));draw(A--(8,0)--Ee,dashed);
draw((7.5,0)--(7.5,0.5)--(8,0.5));
label("$A$",A,S);label("$B$",B,SW);label("$C$",C,W);label("$D$",D,N);label("$E$",Ee,E);
label("$4$",(A+B)/2,S);label("$4$",(6,0),S);label("$4$",(8,2),E);label("$F$",(8,0),SE);label("$4\sqrt5$",(5.6,2.8),NW,red);'''
b.add(1788394,1,r'''The hypotenuse $AC$ of isosceles right triangle $ABC$ is a side of square $ACDE$, and the square and the triangle lie on opposite sides of $AC$, as shown. If $AB=4$ units, what is the length of segment $BE$? Express your answer in simplest radical form.
'''+asy(qfig,'4.5cm'),
r'''Place $B=(0,0)$, $A=(4,0)$, $C=(0,4)$. The vector $\overrightarrow{CA}=(4,-4)$; turning it through $90^\circ$ away from $B$ gives $(4,4)$, so $E=A+(4,4)=(8,4)$ and $D=C+(4,4)=(4,8)$.
'''+asy(sfig,'5cm')+r'''
Then $BE=\sqrt{8^2+4^2}=\sqrt{80}=\boxed{4\sqrt5}$. Without coordinates: drop the perpendicular from $E$ to line $BA$, meeting it at $F$; triangle $AFE$ is congruent to triangle $CBA$ rotated, so $AF=FE=4$, and $BE^2=(4+4)^2+4^2=80$.''',
'Squares|Isosceles triangles|Right triangles|Pythagorean theorem|Coordinate geometry',3,source=src('MATHCOUNTS',2015,'National',11,rnd='Sprint'),
note='The figure was attached; the text "as shown" is made explicit (square on the side of AC away from B), consistent with the answer in simplest radical form. Redrawn in Asymptote.')

# ---------------- 1791188 leading coefficient
b.add(1791188,1,r'''What is the leading coefficient of the trinomial $-7x^2+3x-19$?''',
r'''The leading term is the term of highest degree, $-7x^2$, and its coefficient (including the sign) is $\boxed{-7}$.''',
'Polynomials',1)

# ---------------- 1791115 make 100
b.add(1791115,1,r'''Using each of the numbers $50,2,4,1$ exactly once, together with $+,-,\times,\div$, exponents, parentheses, square roots and factorials, make $100$.''',
r'''For example,
\[
50\times(4-2)\times1=\boxed{100}.
\]
(Other expressions work too, e.g.\ $50\times2\times1^4=100$.)''',
'Order of operations|Whole-number operations|Construction',1,
note='Problem P1 of a "make 100" marathon; any valid expression is accepted.')

# ---------------- 1499461 3pq | n^{3pq}-n
b.add(1499461,1,r'''The primes $p$ and $q$ are such that $3pq$ divides $n^{3pq}-n$ for every positive integer $n$. What is the minimum possible value of $p+q$?''',
r'''Let $N=3pq$.

\textbf{$N$ is squarefree.} If $r^2\mid N$ for a prime $r$, take $n=r$: since $N\ge2$, $r^N-r\equiv-r\not\equiv0\pmod{r^2}$, a contradiction. So $p$, $q$, $3$ are distinct; in particular $p,q\ne3$ and $p\ne q$.

\textbf{The condition for each prime.} For a prime $r\mid N$, let $g$ be a primitive root modulo $r$. From $r\mid g^N-g$ and $r\nmid g$ we get $g^{N-1}\equiv1\pmod r$, so the order $r-1$ of $g$ divides $N-1$. Conversely, if $(r-1)\mid N-1$ for each prime $r\mid N$, then for every $n$: if $r\mid n$ clearly $r\mid n^N-n$, and otherwise $n^{N-1}\equiv1\pmod r$ by Fermat's little theorem. As $N$ is squarefree, the three primes then give $N\mid n^N-n$. So the condition is equivalent to
\[
2\mid 3pq-1,\qquad (p-1)\mid 3pq-1,\qquad (q-1)\mid3pq-1 .
\]
The first says $p$ and $q$ are odd. Since $3pq-1=3q(p-1)+(3q-1)$, the second is $(p-1)\mid3q-1$, and similarly the third is $(q-1)\mid3p-1$.

\textbf{Search.} The odd primes other than $3$ are $5,7,11,13,17,19,\dots$. The pairs $p<q$ with $p+q<28$ are $(5,7)$, $(5,11)$, $(5,13)$, $(5,17)$, $(5,19)$, $(7,11)$, $(7,13)$, $(7,17)$, $(7,19)$, $(11,13)$, and each fails:
\begin{itemize}
\item $(5,7)$: $6\nmid14$; $(5,11)$: $10\nmid14$; $(5,19)$: $18\nmid14$;
\item $(5,13)$: $4\nmid38$; $(5,17)$: $4\nmid50$;
\item $(7,11),(7,13),(7,17),(7,19)$: $6\nmid32,38,50,56$ respectively;
\item $(11,13)$: $10\nmid38$.
\end{itemize}
For $(p,q)=(11,17)$: $10\mid3\cdot17-1=50$ and $16\mid3\cdot11-1=32$. So $N=561$ works, and the minimum is $p+q=\boxed{28}$.''',
'Fermat\'s little theorem|Multiplicative order|Prime numbers|Divisibility|Remainders and congruences',6,
note='The post\'s "n^3pq - n divides 3pq" is read as 3pq divides n^(3pq) - n. Answer 28 (N = 561 = 3*11*17, the smallest Carmichael number), checked directly for n up to 561 and by search over primes.')

b.save()
