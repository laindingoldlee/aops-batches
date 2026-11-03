from qb import *
b=Bank('p226_02')

# ---------------- 1761523 four numbers in ascending order
b.add(1761523,1,r'''Four different numbers are picked at random from $\{1,2,3,4,5,6,7\}$ and placed in a random order. What is the probability that the four numbers appear in ascending order?''',
r'''Whichever four numbers are picked, all $4!=24$ orders of them are equally likely, and exactly one of these orders is ascending. So the probability is $\boxed{\dfrac1{24}}$. (The size of the set, $7$, does not matter.)''',
'Probability|Permutations',2)

# ---------------- 1761483 mx^m = nx^n
b.add(1761483,1,r'''Let $m$ and $n$ be nonzero numbers with $m^2\ne n^2$, and let $x\ne0$ satisfy $mx^m-nx^n=0$. Find the value of
\[
\dfrac{1}{x^m+x^n}+\dfrac{1}{x^m-x^n}
\]
in terms of $m$, $n$ and $x^n$.''',
r'''From $mx^m=nx^n$ we get $x^m=\dfrac nm\,x^n$. Combining the fractions,
\[
\dfrac{1}{x^m+x^n}+\dfrac{1}{x^m-x^n}=\dfrac{2x^m}{x^{2m}-x^{2n}} .
\]
Now $2x^m=\dfrac{2n}{m}x^n$ and $x^{2m}-x^{2n}=\left(\dfrac{n^2}{m^2}-1\right)x^{2n}=\dfrac{n^2-m^2}{m^2}x^{2n}$, which is nonzero since $m^2\ne n^2$. Therefore
\[
\dfrac{1}{x^m+x^n}+\dfrac{1}{x^m-x^n}=\dfrac{2n}{m}x^n\cdot\dfrac{m^2}{(n^2-m^2)x^{2n}}=\boxed{\dfrac{2mn}{(n^2-m^2)\,x^n}}.
\]''',
'Exponents|Algebraic manipulation|Rational equations',3,
note='The conditions m, n nonzero, m^2 not equal to n^2 and x nonzero (needed for the expression to be defined) are stated; the answer also involves m and n.')

# ---------------- 1761140 dart closer to centre
fig=r'''pair O=(0,0);
for(int i=0;i<4;++i){
  pair K=rotate(90*i)*(1,1);
  path seg=arc(K,1,180+90*i,270+90*i)--cycle;
  fill(seg,rgb(0.8,0.88,1));
  draw(arc(K,1,180+90*i,270+90*i),linewidth(0.7));
}
draw((1,0)--(0,1)--(-1,0)--(0,-1)--cycle,dashed);
draw((-1,-1)--(1,-1)--(1,1)--(-1,1)--cycle,linewidth(0.9));
dot(O);label("$O$",O,S);
label("$(1,1)$",(1,1),NE);label("$(-1,1)$",(-1,1),NW);label("$(-1,-1)$",(-1,-1),SW);label("$(1,-1)$",(1,-1),SE);'''
b.add(1761140,1,r'''A dart is thrown at a uniformly random point of a square dartboard with side length $2$. What is the probability that the dart lands closer to the centre of the board than to any corner, but within a distance $1$ of some corner?
\[
\textbf{(A)}\ \pi\qquad\textbf{(B)}\ \dfrac{\pi-2}{4}\qquad\textbf{(C)}\ \dfrac{\pi-4}{\pi}\qquad\textbf{(D)}\ \dfrac14\qquad\textbf{(E)}\ \dfrac18
\]''',
r'''Put the centre at $O=(0,0)$ and the corners at $(\pm1,\pm1)$. A point $(x,y)$ of the board is closer to $O$ than to the corner $(1,1)$ exactly when $x^2+y^2<(x-1)^2+(y-1)^2$, i.e.\ $x+y<1$; similarly for the other corners, so "closer to the centre than to every corner" is the inside of the dashed square $|x|+|y|<1$.

A point within distance $1$ of the corner $(1,1)$ that also satisfies $x+y<1$ lies in the circular segment cut from the quarter disc of radius $1$ about $(1,1)$ by the chord from $(1,0)$ to $(0,1)$ (both endpoints are on the circle). Such points have $x,y\ge0$ and are automatically on the correct side of the other three lines.
'''+asy(fig,'5.5cm')+r'''
Each segment has area (quarter disc minus right triangle) $\dfrac\pi4-\dfrac12$, and the four segments (shaded) do not overlap. The probability is
\[
\dfrac{4\left(\dfrac\pi4-\dfrac12\right)}{4}=\dfrac{\pi-2}{4},
\]
answer $\boxed{\textbf{(B)}}$.''',
'Geometric probability|Circles|Squares|Lengths, perimeter, and area',3,
note='Checked by Monte Carlo simulation.')

# ---------------- 1761230 at least 3 heads in 4 flips
b.add(1761230,1,r'''Four fair coins are flipped. A student argues: ``For at least $3$ heads we need three heads and do not care about the last flip, so the probability is $\left(\dfrac12\right)^3=\dfrac18$.'' Find the correct probability that at least $3$ of the flips are heads, and explain the error in the student's argument.''',
r'''There are $16$ equally likely outcomes. Exactly $3$ heads occurs in $\dbinom43=4$ outcomes and $4$ heads in $1$, so
\[
P(\text{at least }3\text{ heads})=\dfrac{4+1}{16}=\boxed{\dfrac{5}{16}}.
\]
The student's $\left(\dfrac12\right)^3$ is the probability that three \emph{particular} flips (say the first three) are all heads. But the three heads may be in any three of the four positions: the outcomes $THHH$, $HTHH$ and $HHTH$ have at least three heads but are not counted by ``the first three are heads''. Conversely, one cannot fix ``some three flips'' in advance, since the events for different choices of three flips overlap (all of them contain $HHHH$). Counting the outcomes directly gives $\dfrac5{16}>\dfrac18$.''',
'Probability|Binomial probability|Combinations',2)

# ---------------- 1761162 7^2010 mod 100 (alias)
b.add(1761162,1,r'''What is the remainder when $7^{2010}$ is divided by $100$?''',
r'''Since $7^4=2401\equiv1\pmod{100}$ and $2010=4\cdot502+2$, we get $7^{2010}=\left(7^4\right)^{502}\cdot7^2\equiv49\pmod{100}$. The remainder is $\boxed{49}$. (The method: find a small power of the base that is $\equiv1$ modulo $100$, then reduce the exponent modulo that power.)''',
'Modular exponentiation|Remainders and congruences|Units digits and last digits',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1761197 cylinder from rotating a rectangle
fig=r'''real R=10,H=9,k=0.3;
pair c0=(0,0),c1=(0,H);
path bot=ellipse(c0,R,k*R), top=ellipse(c1,R,k*R);
fill(c0--(R,0)--(R,H)--c1--cycle,rgb(0.85,0.9,1));
draw(subpath(bot,0,2),dashed);draw(subpath(bot,2,4),linewidth(0.8));
draw(top,linewidth(0.8));
draw((-R,0)--(-R,H),linewidth(0.8));draw((R,0)--(R,H),linewidth(0.8));
draw(c0--(R,0)--(R,H)--c1,blue+linewidth(0.9));
draw((0,-4.5)--(0,H+4.5),dashed+red);
label("$10$",(R/2,0),S,blue);label("$9$",(R,H/2),E,blue);
label("axis",(0,H+4.5),N,red);'''
b.add(1761197,1,r'''A $9$ by $10$ rectangle is rotated about one of its shorter sides. Find the volume of the circular cylinder formed.''',
r'''The side of length $9$ is the axis, so the cylinder has height $9$, and the side of length $10$ sweeps out the base, giving radius $10$.
'''+asy(fig,'5cm')+r'''
The volume is $\pi r^2h=\pi\cdot10^2\cdot9=\boxed{900\pi}$.''',
'Cylinders|Volume|Solid geometry',1,
note='Science Bowl question.')

# ---------------- 1761161 partial fractions
b.add(1761161,1,r'''Find constants $A$ and $B$ such that
\[
\dfrac{1}{n(n+2)}=\dfrac An+\dfrac{B}{n+2}
\]
for all $n\ne0,-2$.''',
r'''Multiplying by $n(n+2)$ gives $1=A(n+2)+Bn=(A+B)n+2A$ for all $n$. Comparing coefficients, $2A=1$ and $A+B=0$, so $\boxed{A=\dfrac12,\ B=-\dfrac12}$. Indeed $\dfrac{1}{2n}-\dfrac{1}{2(n+2)}=\dfrac{(n+2)-n}{2n(n+2)}=\dfrac{1}{n(n+2)}$.''',
'Partial fractions|Rational equations',2)

# ---------------- 1760139 seeds in pots
b.add(1760139,1,r'''Harry has $10$ flower seeds: $6$ daisy seeds, $2$ rose seeds and $2$ lily seeds; seeds of the same kind are indistinguishable. He plants all of them in $3$ pots, two of which are identical while the third is different. A pot may receive any number of seeds, including none. How many different ways are there to plant the seeds?''',
r'''\textbf{Three distinguishable pots.} Each kind is distributed independently by stars and bars: daisies in $\dbinom82=28$ ways, roses in $\dbinom42=6$ ways, lilies in $6$ ways, a total of $28\cdot6\cdot6=1008$ ways.

\textbf{Two pots identical.} Call the special pot $P$ and the identical pots $X$ and $Y$. Swapping the contents of $X$ and $Y$ gives the same planting. Count the plantings in which $X$ and $Y$ receive the same contents: for each kind, $P$ gets a number of seeds that leaves an even remainder, split equally. Daisies: $P$ gets $0,2,4$ or $6$ ($4$ ways); roses: $0$ or $2$ ($2$ ways); lilies: $2$ ways. So $16$ plantings are unchanged by the swap, and the other $1008-16=992$ come in pairs. The number of different plantings is
\[
16+\dfrac{992}{2}=\boxed{512}.
\]''',
'Distributions and integer solutions|Stars and bars|Symmetry|Multiplication principle',4,
note='P1 of a counting marathon. The post does not say whether seeds of one kind are distinguishable or whether pots may be empty; the record takes seeds of a kind as identical and allows empty pots. Verified by brute force.')

# ---------------- 1761117 factors of 5 in 201!
b.add(1761117,1,r'''Find the exponent of $5$ in the prime factorization of $201!$. Explain why $\left\lfloor\dfrac{201}{5}\right\rfloor$ alone is not the answer, although for $10!$ dividing $10$ by $5$ gives the right exponent $2$.''',
r'''Each multiple of $5$ up to $201$ contributes at least one factor $5$; there are $\left\lfloor\dfrac{201}{5}\right\rfloor=40$ of them. But multiples of $25$ contain $5^2$ and contribute a second factor each: there are $\left\lfloor\dfrac{201}{25}\right\rfloor=8$ of them. Multiples of $125$ contribute a third factor: $\left\lfloor\dfrac{201}{125}\right\rfloor=1$ (namely $125$). There are no multiples of $625$. So the exponent is
\[
40+8+1=\boxed{49}.
\]
For $10!$ the only multiples of $5$ are $5$ and $10$, each containing a single $5$; no number up to $10$ is a multiple of $25$, so the extra terms $\left\lfloor\dfrac{10}{25}\right\rfloor,\dots$ are $0$ and $\left\lfloor\dfrac{10}{5}\right\rfloor=2$ is already the full answer. In general the exponent of a prime $p$ in $N!$ is $\left\lfloor\dfrac Np\right\rfloor+\left\lfloor\dfrac N{p^2}\right\rfloor+\left\lfloor\dfrac N{p^3}\right\rfloor+\cdots$ (Legendre's formula).''',
'Factorials|Prime factorisation|Floor and ceiling functions|Trailing zeros',2,
note='The attached problem is not given; the poster\'s question (why the repeated division by 5 is needed for 201!) is answered.')

# ---------------- 1760928 MATHCOUNTS 2011 National Sprint 19
b.add(1760928,1,r'''Five different single-digit numbers have sum $31$. If such a set of numbers is chosen at random from all possibilities, what is the probability that it contains exactly two prime numbers? Express your answer as a common fraction.''',
r'''Find all sets of five different digits with sum $31$. Without $9$, the largest possible sum is $8+7+6+5+4=30$, so $9$ is in the set.
\begin{itemize}
\item With $9,8,7$: two more digits from $0$--$6$ with sum $7$: $\{1,6\}$, $\{2,5\}$, $\{3,4\}$.
\item With $9,8$ but not $7$: three digits from $0$--$6$ with sum $14$; the maximum is $6+5+4=15$, so only $\{6,5,3\}$.
\item With $9$ but not $8$: four digits from $0$--$7$ with sum $22$; the maximum is $7+6+5+4=22$, so only $\{7,6,5,4\}$.
\end{itemize}
The five sets and their primes ($2,3,5,7$):
$\{1,6,7,8,9\}$: one prime; $\{2,5,7,8,9\}$: three; $\{3,4,7,8,9\}$: two; $\{3,5,6,8,9\}$: two; $\{4,5,6,7,9\}$: two. The probability is $\boxed{\dfrac35}$.''',
'Probability|Prime numbers|Systematic counting|Casework',3,
source=src('MATHCOUNTS',2011,'National',19,rnd='Sprint'),
note='"A list of five different single-digit numbers" read as a set chosen uniformly from all such sets (orderings do not change the probability).')

# ---------------- 1759738 means
b.add(1759738,1,r'''The arithmetic mean of $a$ and $b$ is $5$, the mean of $b$ and $c$ is $7$, and the mean of $a$ and $c$ is $12$. Evaluate $a+b+c$.''',
r'''We have $a+b=10$, $b+c=14$ and $a+c=24$. Adding, $2(a+b+c)=48$, so $a+b+c=\boxed{24}$.''',
'Mean|Systems of linear equations',1,
note='P1 of a MATHCOUNTS marathon; only P1 is in the post.')

# ---------------- 1760504 equilateral triangles on a parabola
fig=r'''import graph;
real f(real x){return x^2+2x+4;}
draw(graph(f,-4.1,2.1),linewidth(0.9));
pair A1=(-1,3),B1=(sqrt(3)-1,6),C1=(-sqrt(3)-1,6);
pair A2=(0,4),B2=(1.3005,f(1.3005)),C2=(-3.0670,f(-3.0670));
draw(A1--B1--C1--cycle,blue+linewidth(0.8));
draw(A2--B2--C2--cycle,red+linewidth(0.8));
dot(A1,blue);dot(B1,blue);dot(C1,blue);dot(A2,red);dot(B2,red);dot(C2,red);
label("$y=x^2+2x+4$",(2.1,f(2.1)),E);
draw((-4.5,0)--(3,0),Arrow(4));draw((0,-0.5)--(0,13),Arrow(4));
label("$x$",(3,0),S);label("$y$",(0,13),W);'''
b.add(1760504,1,r'''How many equilateral triangles have all three vertices on the graph of $y=x^2+2x+4$?''',
r'''The answer is: \textbf{infinitely many}. In fact every point of the parabola is a vertex of such a triangle.

Since $y=(x+1)^2+3$, translating by $(1,-3)$ (which preserves distances) turns the graph into the parabola $\mathcal P:\ y=x^2$, so we work with $\mathcal P$. Fix $A=(a,a^2)$ on $\mathcal P$ and let $\rho$ be the rotation about $A$ through $60^\circ$ counterclockwise, $\rho(A+(p,q))=A+\left(\dfrac p2-\dfrac{\sqrt3}{2}q,\ \dfrac{\sqrt3}{2}p+\dfrac q2\right)$. For a point $B\ne A$ on $\mathcal P$, the triangle $A,B,\rho(B)$ is equilateral; we need $\rho(B)$ to lie on $\mathcal P$ as well.

Put $B=(t,t^2)$ and $\rho(B)=(u(t),v(t))$:
\[
u(t)=a+\dfrac{t-a}{2}-\dfrac{\sqrt3}{2}(t^2-a^2),\qquad v(t)=a^2+\dfrac{\sqrt3}{2}(t-a)+\dfrac{t^2-a^2}{2},
\]
and let $g(t)=v(t)-u(t)^2$, so $\rho(B)\in\mathcal P$ exactly when $g(t)=0$. Then:
\begin{itemize}
\item $g(a)=a^2-a^2=0$, and $g'(a)=v'(a)-2u(a)u'(a)=\left(\dfrac{\sqrt3}{2}+a\right)-2a\left(\dfrac12-\sqrt3a\right)=\dfrac{\sqrt3}{2}+2\sqrt3a^2>0$, so $g(t)>0$ for $t$ slightly larger than $a$.
\item As $t\to\infty$, $u(t)^2$ grows like $\dfrac34t^4$ while $v(t)$ grows like $\dfrac12t^2$, so $g(t)\to-\infty$.
\end{itemize}
By the intermediate value theorem $g(b)=0$ for some $b>a$. With $B=(b,b^2)$ and $C=\rho(B)$, both on $\mathcal P$ and distinct from $A$, the triangle $ABC$ is equilateral.

So every point $A$ of the parabola is a vertex of an inscribed equilateral triangle. Each triangle has only three vertices and there are infinitely many points $A$, hence infinitely many such triangles. Two of them are drawn: the one symmetric about the axis, with vertices $(-1,3)$ and $(-1\pm\sqrt3,6)$ (side $2\sqrt3$), and the one with a vertex at $(0,4)$.
'''+asy(fig,'6cm'),
'Parabolas|Equilateral triangles|Rotations|Coordinate geometry',6,
note='The answer (infinitely many) is proved by a continuity argument; checked numerically by constructing the triangle through several vertices (e.g. (0,4), (1.3005, 8.2923), (-3.0670, 7.2724)).')

# ---------------- 1760988 units digit of sum k(k+1)(k+2)
b.add(1760988,1,r'''When the sum
\[
(1\cdot2\cdot3)+(2\cdot3\cdot4)+(3\cdot4\cdot5)+\cdots+(2018\cdot2019\cdot2020)
\]
is evaluated, what is the units digit of the result?''',
r'''Since $k(k+1)(k+2)=\dfrac14\Bigl[k(k+1)(k+2)(k+3)-(k-1)k(k+1)(k+2)\Bigr]$, the sum telescopes:
\[
\sum_{k=1}^{2018}k(k+1)(k+2)=\dfrac{2018\cdot2019\cdot2020\cdot2021}{4}=1009\cdot2019\cdot1010\cdot2021 .
\]
The factor $1010$ is a multiple of $10$, so the units digit is $\boxed{0}$.''',
'Telescoping sums|Summation|Units digits and last digits',3,
note='The posted solution (working modulo 10 in blocks of five terms) also gets 0; the record gives the shorter telescoping argument.')

# ---------------- 1760858 lattice point probability
b.add(1760858,1,r'''Consider the lattice points $(x,y)$ with $x,y$ integers, $0\le x\le7$ and $0\le y\le7$. Two points are selected at random from this set, independently, each point equally likely, and the two points need not be distinct. What is the probability that the triangle (possibly degenerate) formed by the two points and $(0,0)$ has integer area (possibly zero)? Express your answer as a decimal to the nearest thousandth.''',
r'''For points $(x_1,y_1)$ and $(x_2,y_2)$ the area is $\dfrac12|x_1y_2-x_2y_1|$, an integer exactly when $x_1y_2-x_2y_1$ is even. This depends only on the parities of the coordinates. Each of the four parity classes $(x\bmod2,y\bmod2)$ contains $4\cdot4=16$ of the $64$ points, so the parity vectors $u=(x_1,y_1)\bmod2$ and $w=(x_2,y_2)\bmod2$ are independent and uniform over the $4$ classes.

Count the $16$ pairs $(u,w)$ with $x_1y_2-x_2y_1\equiv0\pmod2$: if $u=(0,0)$, all $4$ choices of $w$ work; if $u$ is one of the $3$ nonzero vectors, the determinant is even exactly when $w=(0,0)$ or $w=u$, i.e.\ $2$ choices. That gives $4+3\cdot2=10$ pairs. The probability is $\dfrac{10}{16}=\dfrac58=\boxed{0.625}$.''',
'Probability|Parity|Matrices and determinants',4,
note='Verified by enumerating all 64^2 ordered pairs.')

# ---------------- 1760752 income tax
b.add(1760752,1,r'''In Alaya's home state, income tax is $4\%$ on the portion of income up to $\$10{,}000$, plus $5\%$ on the portion above $\$10{,}000$ up to $\$30{,}000$, plus $6\%$ on the portion above $\$30{,}000$. If Alaya paid $\$3200$ in state income tax, what was his income?''',
r'''On the first $\$30{,}000$ the tax is $0.04\cdot10{,}000+0.05\cdot20{,}000=400+1000=\$1400$. The remaining $\$3200-\$1400=\$1800$ is $6\%$ of the income above $\$30{,}000$, which is therefore $\dfrac{1800}{0.06}=\$30{,}000$. The income was $\boxed{\$60{,}000}$.''',
'Percentages|Piecewise functions|Money and currency',2,
note='The figure for a $42,000 income is only an illustration and is not needed.')

# ---------------- 1760885 tan^2(arcsin(2/3))
fig=r'''pair A=(0,0),B=(sqrt(5),0),C=(sqrt(5),2);
draw(A--B--C--cycle,linewidth(0.9));
draw((B+(-0.15,0))--(B+(-0.15,0.15))--(B+(0,0.15)),linewidth(0.4));
draw(arc(A,0.5,0,degrees(C-A)),linewidth(0.6));
label("$\theta$",A+0.75*dir(degrees(C-A)/2));
label("$3$",(A+C)/2,NW);label("$2$",(B+C)/2,E);label("$\sqrt{5}$",(A+B)/2,S);'''
b.add(1760885,1,r'''What is $\tan^{2}\left(\sin^{-1}\dfrac23\right)$?''',
r'''Let $\theta=\sin^{-1}\dfrac23$, an acute angle with $\sin\theta=\dfrac23$. In a right triangle with hypotenuse $3$ and side $2$ opposite $\theta$, the adjacent side is $\sqrt{9-4}=\sqrt5$.
'''+asy(fig,'4.5cm')+r'''
So $\tan\theta=\dfrac{2}{\sqrt5}$ and $\tan^2\theta=\boxed{\dfrac45}$. (Equivalently, $\tan^2\theta=\dfrac{\sin^2\theta}{1-\sin^2\theta}=\dfrac{4}{9}\div\dfrac{5}{9}$.)''',
'Trigonometry|Right triangles|Pythagorean theorem',2)

# ---------------- 1760574 cars and Johns
b.add(1760574,1,r'''Ten distinguishable people split into three different cars, with $3$, $3$ and $4$ people respectively (seating within a car does not matter). Four of the ten people are named John. In how many ways can the people be assigned to the cars so that every car has at least one John?''',
r'''The numbers of Johns in the cars (sizes $3,3,4$) are positive and add to $4$, so they are $(2,1,1)$, $(1,2,1)$ or $(1,1,2)$.
\begin{itemize}
\item $(2,1,1)$: choose the Johns $\dbinom42\dbinom21=12$ ways, then fill the remaining $1,2,3$ places with the $6$ others in $\dbinom61\dbinom52=60$ ways: $720$.
\item $(1,2,1)$: likewise $720$.
\item $(1,1,2)$: Johns $4\cdot3=12$ ways, the others fill $2,2,2$ places in $\dbinom62\dbinom42=90$ ways: $1080$.
\end{itemize}
Total: $720+720+1080=\boxed{2520}$.''',
'Combinations|Casework|Multiplication principle',3,
note='"3 different cars" read as distinguishable cars, the first two holding 3 people and the third 4. Verified by brute force.')

# ---------------- 1760770 Chinese remainder theorem
b.add(1760770,1,r'''State the Chinese remainder theorem for two moduli, and use it to find the smallest positive integer $x$ with
\[
x\equiv2\pmod3,\qquad x\equiv3\pmod5,\qquad x\equiv2\pmod7 .
\]''',
r'''\textbf{Statement.} If $m$ and $n$ are relatively prime positive integers, then for any integers $a,b$ the system $x\equiv a\pmod m$, $x\equiv b\pmod n$ has a solution, and the solutions form exactly one residue class modulo $mn$. (Reason: the $n$ numbers $a,a+m,\dots,a+(n-1)m$ have different remainders modulo $n$, because $n\mid(i-j)m$ forces $n\mid i-j$; so exactly one of them is $\equiv b\pmod n$.) Applying it repeatedly handles any number of pairwise relatively prime moduli.

\textbf{The example.} $x\equiv2\pmod3$ and $x\equiv2\pmod7$ together say $x\equiv2\pmod{21}$, so $x\in\{2,23,44,65,86,\dots\}$. The first of these that is $\equiv3\pmod5$ is $23$. All solutions are $x\equiv23\pmod{105}$, and the smallest positive one is $\boxed{23}$.''',
'Chinese remainder theorem|Remainders and congruences',2,
note='The post asks what the Chinese remainder theorem is; the record asks for the statement and applies it to the classical example of Sunzi (answer 23).')

# ---------------- 1759320 Hill cipher
b.add(1759320,1,r'''A $2\times2$ matrix $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ is generated by choosing each of the four entries independently and uniformly from the integers $0,1,\dots,25$. For the Hill cipher the matrix must be invertible modulo $26$, which happens if and only if $ad-bc$ is relatively prime to $26$.
\begin{enumerate}
\item[(a)] What is the probability that the matrix is \emph{not} invertible?
\item[(b)] More generally, an $n\times n$ matrix with entries chosen the same way is invertible if its determinant is relatively prime to $26$. Find the probability that it is not invertible.
\end{enumerate}''',
r'''\textbf{Reduction to primes.} $\gcd(\det,26)=1$ means $\det\not\equiv0\pmod2$ and $\det\not\equiv0\pmod{13}$. The determinant modulo $p$ depends only on the entries modulo $p$. By the Chinese remainder theorem, an entry uniform on $\{0,\dots,25\}$ corresponds to a pair (entry mod $2$, entry mod $13$) uniform on $\{0,1\}\times\{0,\dots,12\}$, with the two components independent. So the events ``$\det\not\equiv0\pmod2$'' and ``$\det\not\equiv0\pmod{13}$'' are independent, and the matrix mod $p$ is a uniformly random matrix over the field $\mathbb Z_p$.

\textbf{Counting over $\mathbb Z_p$.} An $n\times n$ matrix over $\mathbb Z_p$ has nonzero determinant exactly when its rows are linearly independent. The first row can be any of the $p^n-1$ nonzero vectors, the second any vector outside the $p$ multiples of the first, the third outside the $p^2$ combinations of the first two, and so on. So the probability of a nonzero determinant is
\[
\dfrac{(p^n-1)(p^n-p)\cdots(p^n-p^{n-1})}{p^{n^2}}=\prod_{i=1}^{n}\left(1-\dfrac1{p^i}\right).
\]
(b) Therefore
\[
P(\text{not invertible})=\boxed{1-\prod_{i=1}^{n}\left(1-\dfrac1{2^i}\right)\left(1-\dfrac1{13^i}\right)}.
\]
(a) For $n=2$: modulo $2$ the probability is $\dfrac12\cdot\dfrac34=\dfrac38$ (there are $6$ invertible matrices out of $16$); modulo $13$ it is $\dfrac{12}{13}\cdot\dfrac{168}{169}=\dfrac{2016}{2197}$. Hence the probability of being invertible is $\dfrac38\cdot\dfrac{2016}{2197}=\dfrac{756}{2197}$, and the probability of not being invertible is
\[
1-\dfrac{756}{2197}=\boxed{\dfrac{1441}{2197}}\approx0.656 .
\]
(In counts: $6\cdot168\cdot156=157248$ of the $26^4=456976$ matrices are invertible.)''',
'Matrices and determinants|Probability|Complementary probability|Chinese remainder theorem|Independent events',6,
note='The bonus question is part (b). Part (a) verified by enumerating all 26^4 matrices.')

# ---------------- 1760552 2^(16^x)=16^(2^x) (alias)
b.add(1760552,1,r'''Find $x$ if $2^{16^x}=16^{2^x}$.''',
r'''The right side is $16^{2^x}=2^{4\cdot2^x}=2^{2^{x+2}}$, and the left side is $2^{16^x}=2^{2^{4x}}$. Comparing exponents twice, $2^{4x}=2^{x+2}$, so $4x=x+2$ and $x=\boxed{\dfrac23}$.''',
'Exponents',3,
note='Repeat of an earlier record (aliased).')

b.save()
