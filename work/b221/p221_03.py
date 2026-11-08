from qb import *
b=Bank('p221_03')

# ---------------- 1786013 factor (2a)^2-12ab+(3b)^2-x^2
b.add(1786013,1,r'''Factor completely: $4a^2-12ab+9b^2-x^2$.''',
r'''The first three terms form a perfect square: $4a^2-12ab+9b^2=(2a)^2-2(2a)(3b)+(3b)^2=(2a-3b)^2$. So the expression is a difference of two squares:
\[
(2a-3b)^2-x^2=\boxed{(2a-3b-x)(2a-3b+x)} .
\]''',
'Factoring|Difference of squares|Algebraic expressions and identities',2,
note='The post writes (4a)^2 - 12ab + (9b)^2 - (x)^2; as typed, 16a^2 - 12ab + 81b^2 is not a perfect square (the middle term would have to be 72ab). The intended expression 4a^2 - 12ab + 9b^2 - x^2 is used.')

# ---------------- 1785283 bar melted into balls
fig=r'''real L=6, rr=0.5;
draw((0,rr)--(L,rr),linewidth(0.8));draw((0,-rr)--(L,-rr),linewidth(0.8));
draw(ellipse((0,0),0.2,rr),linewidth(0.8));
draw(shift((L,0))*scale(0.2,rr)*arc((0,0),1,-90,90),linewidth(0.8));
draw(shift((L,0))*scale(0.2,rr)*arc((0,0),1,90,270),dashed+gray);
draw((0,-rr-0.35)--(L,-rr-0.35),Arrows(5));
label("$729$ cm",(L/2,-rr-0.35),S);
draw((-0.45,-rr)--(-0.45,rr),Arrows(5));
label("$4$ cm",(-0.45,0),W);
pair Cs=(L+2.3,0);
draw(circle(Cs,1.2),linewidth(0.8));
draw(ellipse(Cs,1.2,0.3),gray);
dot(Cs);
draw(Cs--Cs+1.2*dir(-40),linewidth(0.6));
label("$9$ cm",Cs+0.55*dir(-40),SW,fontsize(9pt));
label("(not to scale)",(L/2,rr+0.25),N,fontsize(8pt));'''
b.add(1785283,1,r'''A cylindrical aluminium bar $7.29$ m long and $4$ cm in diameter is melted down and recast into solid balls of radius $9$ cm. How many balls can be made from it?

$\textbf{(a)}\ 3\qquad\textbf{(b)}\ 4\qquad\textbf{(c)}\ 5\qquad\textbf{(d)}\ 81$''',
r'''Work in centimetres: the bar is a cylinder of radius $2$ cm and length $729$ cm.
'''+asy(fig,'8cm')+r'''
\[
V_{\text{bar}}=\pi\cdot2^2\cdot729=2916\pi\ \text{cm}^3,\qquad V_{\text{ball}}=\dfrac43\pi\cdot9^3=972\pi\ \text{cm}^3 .
\]
Since $\dfrac{2916\pi}{972\pi}=3$ exactly, the metal makes $\boxed{\textbf{(a)}\ 3}$ balls.''',
'Cylinders|Spheres|Volume|Unit conversion',2,
note='The post says the aluminium bar is made into "iron balls"; the record says balls (of the same metal).')

# ---------------- 1785779 train (alias)
b.add(1785779,1,r'''A train travels a distance of $300$ km at constant speed. If the speed of the train is increased by $5$ km per hour, the journey takes $2$ hours less. Find the usual speed of the train.''',
r'''With speed $v$: $\dfrac{300}{v}-\dfrac{300}{v+5}=2$, so $v(v+5)=750$, $v^2+5v-750=0=(v-25)(v+30)$, and $v=\boxed{25}$ km per hour.''',
'Distance, rate, and time|Quadratic equations|Rational equations',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1780989 P1 isosceles triangle from six points on a circle
fig=r'''pair O=(0,0);
pair[] V; string[] nm={"$A$","$B$","$C$","$D$","$E$","$F$"};
for(int i=0;i<6;++i) V.push(dir(90-60*i));
draw(circle(O,1),gray+linewidth(0.6));
draw(V[0]--V[2]--V[4]--cycle,blue+linewidth(0.9));
draw(V[0]--V[1]--V[5]--cycle,red+dashed+linewidth(0.9));
for(int i=0;i<6;++i){dot(V[i]);label(nm[i],V[i],dir(90-60*i));}'''
b.add(1780989,1,r'''Six points $A,B,C,D,E,F$ are equally spaced, in this order, on a circle. Three of the six points are chosen at random. What is the probability that they are the vertices of an isosceles triangle? Express your answer as a common fraction.''',
r'''The points are the vertices of a regular hexagon, and any $3$ of them form a triangle, so there are $\dbinom63=20$ equally likely choices.

Up to rotation and reflection there are three kinds of triangle:
'''+asy(fig,'4.5cm')+r'''
\begin{itemize}
\item three consecutive vertices, such as $FAB$ (dashed red): sides $s,s,s\sqrt3$, isosceles; there are $6$ of these (one for each middle vertex);
\item alternate vertices $ACE$ or $BDF$ (blue): equilateral, hence isosceles; there are $2$;
\item the remaining $20-6-2=12$ triangles, such as $ABD$, contain a diameter: sides $s$, $s\sqrt3$, $2s$, all different (a $30$-$60$-$90$ triangle).
\end{itemize}
So $8$ of the $20$ triangles are isosceles, and the probability is $\dfrac{8}{20}=\boxed{\dfrac25}$.''',
'Probability|Isosceles triangles|Regular polygons|Circles|Combinations',3,source=src('MATHRAPIDS',2013,'State Finals',4),
note='The post says only "six concyclic points"; for arbitrary positions the probability is not determined, so the points are taken to be equally spaced (a regular hexagon).')

# ---------------- 1780989 P2 marbles
b.add(1780989,2,r'''A bag contains $101$ marbles, each green or black. When two marbles are drawn at random without replacement, the probability that both are black is $\dfrac{29}{50}$ when rounded to two decimal places (that is, it is $0.58$ to two decimal places). How many green marbles are in the bag?''',
r'''Let there be $b$ black marbles. Then
\[
P(\text{both black})=\dfrac{b(b-1)}{101\cdot100}=\dfrac{b(b-1)}{10100}.
\]
No integer $b$ makes this exactly $\dfrac{29}{50}$, which would need $b(b-1)=5858$ (but $77\cdot76=5852$ and $78\cdot77=6006$). Rounded to two decimal places, we need
\[
0.575\le\dfrac{b(b-1)}{10100}<0.585,\quad\text{i.e.}\quad 5807.5\le b(b-1)<5908.5 .
\]
The only product of consecutive integers in this range is $77\cdot76=5852$ (probability $\approx0.5794$). So $b=77$, and there are $101-77=\boxed{24}$ green marbles.''',
'Probability|Sampling without replacement|Inequalities',3,source=src('MATHRAPIDS',2011,'Nationals',2,rnd='3rd Elimination'),
note='As posted (probability exactly 29/50) no whole number of marbles works: b(b-1) = 5858 has no integer root. The intended reading, signalled by "to the nearest whole number", is that 29/50 = 0.58 is a rounded value; the record states this, giving 24 green marbles.')

# ---------------- 1785255 seven clues
b.add(1785255,1,r'''I am thinking of a positive integer. Find it from these seven clues.
\begin{enumerate}
\item One third of my number is a prime.
\item The sum of the digits of twice my number is $12$.
\item My number is greater than $50$ and less than $500$.
\item The first digit of my number divided by the number formed by the remaining digits equals $10$ divided by the sum of the digits of my number.
\item None of the digits of my number is a prime.
\item The sum of the first two digits of my number is $15$.
\item Apart from $1$, the only divisor of my number less than $10$ is $3$.
\end{enumerate}''',
r'''By clue 5 every digit is one of $0,1,4,6,8,9$. By clue 6 the first two digits add to $15$, and the only such pairs from these digits are $6,9$ and $9,6$ (the pair $7,8$ uses the prime $7$). So the number starts with $69$ or $96$.

By clue 3 it is below $500$, so it cannot have three digits starting with $6$ or $9$; it is $69$ or $96$. Clue 1 rules out $96$, since $\dfrac{96}{3}=32$ is not prime. The number $69$ satisfies every clue:
\begin{enumerate}
\item $\dfrac{69}{3}=23$ is prime;
\item $2\cdot69=138$ and $1+3+8=12$;
\item $50<69<500$;
\item $\dfrac69=\dfrac23$ and $\dfrac{10}{6+9}=\dfrac23$;
\item $6$ and $9$ are not prime;
\item $6+9=15$;
\item the divisors of $69$ are $1,3,23,69$.
\end{enumerate}
The number is $\boxed{69}$.''',
'Logical deduction|Prime numbers|Digit problems',3,
note='P1 of a "7 clues" marathon. Clue 4 is read as first digit divided by the number formed by the other digits; clue 7 as "the only divisor less than 10 other than 1".')

# ---------------- 1785658 TMSCA number sense P1-P3
fig=r'''pair O=(0,0);
pair[] V; for(int i=0;i<12;++i) V.push(dir(30*i));
for(int i=0;i<12;++i) draw(V[i]--V[(i+1)%12],linewidth(0.8));
draw(O--V[0],linewidth(0.7));draw(O--V[1],linewidth(0.7));
draw(arc(O,0.35,0,30),blue+linewidth(0.7));
label("$30^\circ$",0.55*dir(15),blue+fontsize(8pt));
dot(O);label("$O$",O,W);'''
b.add(1785658,1,r'''What is the measure of the central angle of a regular dodecagon?''',
r'''A regular dodecagon has $12$ equal central angles (each subtended by one side at the centre), and together they make a full turn. So each measures $\dfrac{360^\circ}{12}=\boxed{30^\circ}$.
'''+asy(fig,'5cm'),
'Regular polygons|Angles and lines',1,source=src('TMSCA',None,'Number Sense',None))
b.add(1785658,2,r'''The two solutions of $|x-c|=d$ are $-5$ and $33$. What is $c+d$?''',
r'''The solutions of $|x-c|=d$ (with $d>0$) are $c-d$ and $c+d$, the two points at distance $d$ from $c$. So $c$ is their midpoint, $c=\dfrac{-5+33}{2}=14$, and $d=33-14=19$. Hence $c+d=\boxed{33}$ (indeed $c+d$ is the larger solution).''',
'Absolute value',2,source=src('TMSCA',None,'Number Sense',None))
fig=r'''import graph;
real f(real x){return (7-3x)/2;}
real g(real x){return (2x+7)/3;}
pair Pp=(4,5), Q=(7/13,35/13);
draw((-2.5,0)--(6,0),Arrow(6));draw((0,-2.5)--(0,7),Arrow(6));
label("$x$",(6,0),E);label("$y$",(0,7),N);
draw(graph(f,-1.5,4.8),linewidth(0.9));
draw(graph(g,-2.3,5.5),blue+linewidth(0.9));
pair u=unit((2,-3)),v=unit((3,2));
draw(Q+0.3*u--Q+0.3*(u+v)--Q+0.3*v,linewidth(0.5));
dot(Pp);label("$(4,5)$",Pp,SE);
label("$3x+2y=7$",(4.8,f(4.8)),E);
label("$2x-3y=-7$",(-2.3,g(-2.3)),W,blue);'''
b.add(1785658,3,r'''The line $Ax-3y=C$ is perpendicular to the line $3x+2y=7$ and passes through the point $(4,5)$. Find $C$.''',
r'''The line $3x+2y=7$ has slope $-\dfrac32$, so a perpendicular line has slope $\dfrac23$. The line $Ax-3y=C$ has slope $\dfrac A3$, so $\dfrac A3=\dfrac23$ and $A=2$. It passes through $(4,5)$, so $C=2\cdot4-3\cdot5=\boxed{-7}$.
'''+asy(fig,'6cm'),
'Slope|Perpendicular lines|Linear equations|Coordinate geometry',2,source=src('TMSCA',None,'Number Sense',None))

# ---------------- 1785804 marbles in a beaker
fig=r'''real R=3.5, h0=4, h1=h0+5.6, top=11.5;
draw((-R,top)--(-R,0)--(R,0)--(R,top),linewidth(0.9));
draw(ellipse((0,top),R,0.5),linewidth(0.6));
draw(ellipse((0,h0),R,0.5),dashed+gray);
draw(ellipse((0,h1),R,0.5),blue+linewidth(0.8));
for(int i=0;i<5;++i) for(int j=0;j<2;++j) draw(circle((-2.8+1.4*i,0.7+1.4*j),0.7),gray);
draw((R+0.6,h0)--(R+0.6,h1),Arrows(5));
label("$5.6$ cm",(R+0.6,(h0+h1)/2),E);
draw((-R,-0.8)--(R,-0.8),Arrows(5));
label("$7$ cm",(0,-0.8),S);
label("old level",(-R,h0),W,gray);label("new level",(-R,h1),W,blue);'''
b.add(1785804,1,r'''Marbles of diameter $1.4$ cm are dropped into a cylindrical beaker of diameter $7$ cm containing some water. How many marbles must be dropped into the beaker so that the water level rises by $5.6$ cm? (Assume the marbles end up completely under water.)''',
r'''The volume of the marbles equals the volume of the cylinder of water displaced, which has radius $3.5$ cm and height $5.6$ cm.
'''+asy(fig,'5cm')+r'''
\[
V_{\text{rise}}=\pi(3.5)^2(5.6)=68.6\pi\ \text{cm}^3,\qquad V_{\text{marble}}=\dfrac43\pi(0.7)^3=\dfrac{1.372}{3}\pi\ \text{cm}^3 .
\]
So the number of marbles is
\[
\dfrac{68.6\pi}{\dfrac{1.372}{3}\pi}=\dfrac{205.8}{1.372}=\boxed{150}.
\]''',
'Cylinders|Spheres|Volume',2,
note='The assumption that the marbles are fully submerged is stated.')

# ---------------- 1785113 2008 MATHCOUNTS State Sprint 25
b.add(1785113,1,r'''Monica reduced $\dfrac{154}{253}$ to lowest terms by cancelling the middle $5$s to get $\dfrac{14}{23}$. This answer is correct, but the procedure is not. Kia found another example for which Monica's incorrect procedure works: the fraction $\dfrac{242}{x}$, where $x$ is a three-digit integer, is equal to the fraction obtained by cancelling the identical middle digits of $242$ and $x$. What is the greatest possible value of $x$?''',
r'''The middle digit of $x$ must be $4$, so $x=100a+40+c$ with digits $a\ge1$ and $c$, and cancelling gives $\dfrac{22}{10a+c}$. We need
\[
\dfrac{242}{100a+40+c}=\dfrac{22}{10a+c}\iff 11(10a+c)=100a+40+c\iff 10a+10c=40\iff a+c=4 .
\]
So $x\in\{143,242,341,440\}$; for example $\dfrac{242}{440}=\dfrac{22}{40}=\dfrac{11}{20}$. The greatest value is $\boxed{440}$.''',
'Fractions|Place value|Linear Diophantine equations|Digit problems',3,source=src('MATHCOUNTS',2008,'State',25,rnd='Sprint'))

# ---------------- 1785758 sum of remainders 2019
b.add(1785758,1,r'''The sum of the remainders obtained when each of $n,n+1,\dots,n+k$ is divided by $5$ is $2019$. Find the smallest possible natural numbers $n$ and $k$.''',
r'''The remainders of consecutive integers modulo $5$ run cyclically through $0,1,2,3,4$, so every block of $5$ consecutive integers contributes $0+1+2+3+4=10$. Write the number of terms as $k+1=5q+r$ with $0\le r\le4$; then the sum is $10q+s$, where $s$ is the sum of the remainders of the first $r$ terms $n,\dots,n+r-1$, and $0\le s\le1+2+3+4=10$.

Since the sum $2019$ ends in $9$, we need $s=9$ and $q=201$ (if $s$ could be $19$ we would need $r\ge5$). Sums of $r<5$ cyclically consecutive remainders equal to $9$: $r=3$ with remainders $2,3,4$, or $r=4$ with remainders $2,3,4,0$; $r\le2$ gives at most $3+4=7$. In both cases $n\equiv2\pmod5$.

\textbf{Smallest $k$:} $k+1=5\cdot201+3=1008$, so $k=1007$. \textbf{Smallest $n$:} $n\equiv2\pmod 5$ forces $n\ge2$, and $n=2$ works with $k=1007$: the numbers $2,3,\dots,1009$ give $2+3+4$ and then $201$ full cycles, total $9+2010=2019$.

So both minima are attained together: $\boxed{n=2,\ k=1007}$.''',
'Remainders and congruences|Bounding and extremal cases|Summation',4,
note='"smallest possible" is read as minimising both n and k; the two minima are attained by the same pair, as shown.')

# ---------------- 1695399 2012 National Sprint 25, 29, 30 and Target 6 (all aliases)
b.add(1695399,25,r'''In a round-robin chess tournament every player is scheduled to play one game with every other player. Five participants withdrew after playing two games each; none of these five played a game against each other. A total of $220$ games were played in the tournament. Including those who withdrew, how many players participated?''',
r'''The five withdrawn players played $10$ games, all against remaining players, so the $m$ remaining players played $\dbinom m2=210$ games among themselves; $m=21$ and the total is $\boxed{26}$.''',
'Combinations|Quadratic equations',3,source=src('MATHCOUNTS',2012,'National',25,rnd='Sprint'),
note='Repeat of an earlier record (aliased).')
b.add(1695399,29,r'''If $x$ and $y$ satisfy $(x-3)^2+(y-4)^2=49$, what is the minimum possible value of $x^2+y^2$?''',
r'''The point $(x,y)$ is on the circle with centre $(3,4)$ and radius $7$; the origin is at distance $5$ from the centre, inside the circle, so the nearest point of the circle is at distance $7-5=2$ and the minimum is $\boxed{4}$.''',
'Circles|Distance formula|Maxima and minima',3,source=src('MATHCOUNTS',2012,'National',29,rnd='Sprint'),
note='"(y - 4)2" in the post is (y - 4)^2. Repeat of an earlier record (aliased).')
b.add(1695399,30,r'''Eight identical unit cubes are stacked to form a $2\times2\times2$ cube, and $A$ and $B$ are opposite vertices of the large cube. A ``short path'' from $A$ to $B$ consists of six one-unit moves, each right, up or back, along the edges of the unit cubes on the surface of the large cube. How many short paths are possible?''',
r'''All $\dbinom62\dbinom42=90$ monotone paths of the $3\times3\times3$ lattice except those through the centre $(1,1,1)$, of which there are $6\cdot6=36$: $90-36=\boxed{54}$.''',
'Lattice paths|Complementary counting',4,source=src('MATHCOUNTS',2012,'National',30,rnd='Sprint'),
note='"as shown": A and B are opposite vertices. Repeat of an earlier record (aliased).')
b.add(1695399,6,r'''A lattice point is a point $(x,y)$ whose coordinates are both integers. A triangle is formed by the points $(1,1)$, $(9,1)$ and $(9,n)$. For what integer value of $n>0$ are there exactly $560$ lattice points strictly inside the triangle?''',
r'''With $m=n-1$, Pick's theorem gives $4m=I+\dfrac{8+m+\gcd(8,m)}{2}-1$; $I=560$ leads to $7m-\gcd(8,m)=1126$, so $m=161$ and $n=\boxed{162}$.''',
'Lattice points|Pick\'s theorem',4,source=src('MATHCOUNTS',2012,'National',6,rnd='Target'),
note='Target round problem 6 of the post (part number 6). Repeat of an earlier record (aliased).')

# ---------------- 1785284 front and back wheels
b.add(1785284,1,r'''The front wheels of a truck have circumference $3$ m and the back wheels have circumference $4$ m. Over a certain distance the front wheels make $5$ more revolutions than the back wheels. Find the distance travelled by the truck.

$\textbf{(a)}\ 30\text{ m}\qquad\textbf{(b)}\ 45\text{ m}\qquad\textbf{(c)}\ 60\text{ m}\qquad\textbf{(d)}\ 75\text{ m}$''',
r'''Each revolution moves a wheel forward by its circumference, so over a distance $d$ metres the front wheels turn $\dfrac d3$ times and the back wheels $\dfrac d4$ times. Then
\[
\dfrac d3-\dfrac d4=5\ \Longrightarrow\ \dfrac{d}{12}=5\ \Longrightarrow\ d=60 .
\]
The answer is $\boxed{\textbf{(c)}\ 60\text{ m}}$ ($20$ and $15$ revolutions).''',
'Linear equations|Ratios, proportions, and variation',2)

# ---------------- 1785275 tangents from P, OP perpendicular bisector of AB
fig=r'''pair O=(0,0),P=(3.2,0);
real r=1.5;
real ang=degrees(acos(r/3.2));
pair A=r*dir(ang),B=r*dir(-ang),M=(A.x,0);
draw(circle(O,r),linewidth(0.8));
draw(P--A,linewidth(0.9));draw(P--B,linewidth(0.9));
draw(O--P,linewidth(0.8));
draw(A--B,linewidth(0.8));
draw(O--A,dashed);draw(O--B,dashed);
pair u=unit(O-A),v=unit(P-A);draw(A+0.18*u--A+0.18*(u+v)--A+0.18*v,linewidth(0.5));
u=unit(O-B);v=unit(P-B);draw(B+0.18*u--B+0.18*(u+v)--B+0.18*v,linewidth(0.5));
draw(M+(0.18,0)--M+(0.18,0.18)--M+(0,0.18),linewidth(0.5));
dot(O);dot(M);
label("$O$",O,W);label("$P$",P,E);label("$A$",A,NE);label("$B$",B,SE);label("$M$",M,dir(-135));'''
b.add(1785275,1,r'''Two tangents $PA$ and $PB$ are drawn to a circle with centre $O$ from an external point $P$, touching the circle at $A$ and $B$. Prove that $OP$ is the perpendicular bisector of $AB$.''',
r'''\textbf{Equal tangents.} A tangent is perpendicular to the radius at the point of contact, so $\angle OAP=\angle OBP=90^\circ$. The right triangles $OAP$ and $OBP$ have the common hypotenuse $OP$ and equal legs $OA=OB$ (radii), so they are congruent (hypotenuse-leg), and $PA=PB$.
'''+asy(fig,'6cm')+r'''
\textbf{Two points on the perpendicular bisector.} The perpendicular bisector of a segment is the set of points equidistant from its endpoints. Since $OA=OB$, the point $O$ lies on the perpendicular bisector of $AB$; since $PA=PB$, so does $P$. As $O\ne P$, the line through them is that perpendicular bisector. Hence $OP$ meets $AB$ at right angles at its midpoint $M$: $AM=MB$ and $OP\perp AB$. $\blacksquare$''',
'Circles|Tangents|Perpendicular bisectors|Congruence',2)

# ---------------- 1785367 2004 National Target 5
b.add(1785367,1,r'''What is the least integer $N$ greater than $2004$ for which the positive difference between the square of $N+5$ and the square of $N$ is a perfect square?

A student writes $(N+5)^2-N^2=M^2$, i.e.\ $5(2N+5)=M^2$, argues that $2N+5=5X^2$ for an integer $X$, so that $2N=5(X-1)(X+1)$ with $5(X-1)(X+1)>4008$, and finds $N=2720$ by trial. The official answer is $2100$. Find the correct answer and the error.''',
r'''The student's algebra is right. From $5(2N+5)=M^2$, the prime $5$ divides $M^2$, so $5\mid M$; writing $M=5X$ gives $2N+5=5X^2$. Then $X$ must be odd (since $2N+5$ is odd), and
\[
N=\dfrac{5\left(X^2-1\right)}{2}.
\]
We need $N>2004$, i.e.\ $X^2-1>801.6$, so $X^2\ge803$ and $X\ge29$. The least odd $X\ge29$ is $X=29$, which gives
\[
N=\dfrac{5\cdot840}{2}=\boxed{2100}.
\]
Check: $2105^2-2100^2=5\cdot4205=21025=145^2$.

The value $2720$ comes from $X=33$ ($5\cdot32\cdot34=5440=2N$); the trial search skipped $X=29$, where $(X-1)(X+1)=28\cdot30=840>801.6$ already works. ($X=31$ would give $N=2400$, also larger than $2100$.)''',
'Difference of squares|Perfect squares|Diophantine equations',3,source=src('MATHCOUNTS',2004,'National',5,rnd='Target'),
note='The post asks why the method gave 2720 instead of the official 2100; the method is correct but the trial skipped X = 29. The record asks for the answer and the error.')

# ---------------- 1782142 garden visits
b.add(1782142,1,r'''Joey visited his garden one day each week for four weeks. Each visit lasted $1.5$ times as long as the preceding one. In the fourth week Joey spent $135$ minutes in the garden. How long was his visit in the first week?''',
r'''If the first visit lasted $t$ minutes, the visits lasted $t$, $1.5t$, $1.5^2t$, $1.5^3t$ minutes, a geometric sequence. So
\[
1.5^3t=\dfrac{27}{8}t=135\ \Longrightarrow\ t=135\cdot\dfrac{8}{27}=\boxed{40\text{ minutes}}.
\]
(Working backwards: $135\to90\to60\to40$, dividing by $1.5$ each time.)''',
'Geometric sequences|Working backwards',1)

# ---------------- 1784530 rows of numbers mod 7
b.add(1784530,1,r'''Numbers are grouped in rows as follows, each row continuing by adding $7$:
\[
\begin{array}{ll}
A: & 1,\ 8,\ 15,\ \dots\\
B: & 3,\ 10,\ 17,\ \dots\\
C: & 2,\ 9,\ 16,\ \dots\\
D: & 11,\ 18,\ 25,\ \dots\\
E: & 13,\ 20,\ 27,\ \dots
\end{array}
\]
If the pattern continues, in which row will $86$ appear?''',
r'''Each row adds $7$ each time, so all numbers in a row have the same remainder on division by $7$: row $A$ has remainder $1$, $B$ remainder $3$, $C$ remainder $2$, $D$ remainder $4$ ($11=7+4$) and $E$ remainder $6$ ($13=7+6$). Since $86=7\cdot12+2$, the number $86$ has remainder $2$ and appears in row $\boxed{C}$ (as $2+7\cdot12$, the $13$th term).''',
'Remainders and congruences|Arithmetic sequences|Pattern recognition',1,
note='The post asks for the "column"; the groups are labelled A-E, so the record asks for the labelled row.')

# ---------------- 1781243 grasshopper
b.add(1781243,1,r'''A mechanical grasshopper is placed $42$ inches from the door of its cage. Each time a button is pressed, the grasshopper jumps one third of the remaining distance towards the door.
\begin{enumerate}
\item[(a)] How far from the door is the grasshopper after the third jump?
\item[(b)] What total distance has the grasshopper travelled after five jumps?
\end{enumerate}''',
r'''Each jump covers one third of the remaining distance, so it leaves two thirds of it. After $n$ jumps the distance to the door is $d_n=42\left(\dfrac23\right)^n$, and the total distance travelled is $42-d_n$.

\textbf{(a)} $d_3=42\cdot\dfrac{8}{27}=\dfrac{112}{9}=\boxed{12\dfrac49\text{ inches}}$.

\textbf{(b)} $d_5=42\cdot\dfrac{32}{243}=\dfrac{448}{81}$, so the grasshopper has travelled
\[
42-\dfrac{448}{81}=\dfrac{3402-448}{81}=\boxed{\dfrac{2954}{81}=36\dfrac{38}{81}\text{ inches}}.
\]
(The jumps themselves are $14,\ \dfrac{28}{3},\ \dfrac{56}{9},\ \dfrac{112}{27},\ \dfrac{224}{81}$ inches, a geometric sequence with ratio $\dfrac23$, and their sum is the same.)''',
'Geometric sequences|Fractions',2,
note='"How far does the grasshopper travel after the fifth jump" is read as the total distance travelled in five jumps; the length of the fifth jump alone (224/81 inches) is also given.')

# ---------------- 1785265 tan(A+B), tan(A-B)
fig=r'''pair P=(0,0),Q=(1,0),R=(1,sqrt(3));
draw(P--Q--R--cycle,linewidth(0.9));
draw((1,0)--(0.88,0)--(0.88,0.12)--(1,0.12),linewidth(0.5));
draw(arc(P,0.3,0,60),blue+linewidth(0.7));
label("$60^\circ$",0.48*dir(30),blue);
label("$1$",(0.5,0),S);label("$\sqrt3$",(1,sqrt(3)/2),E);label("$2$",(0.5,sqrt(3)/2),NW);'''
b.add(1785265,1,r'''Angles $A$ and $B$ (in degrees) satisfy $A,B\ge0^\circ$, $0^\circ<A+B\le90^\circ$, $\tan(A+B)=\sqrt3$ and $\tan(A-B)=0$. Find $A$ and $B$.''',
r'''In a $30$-$60$-$90$ triangle with legs $1$ and $\sqrt3$, the angle opposite $\sqrt3$ is $60^\circ$ and its tangent is $\dfrac{\sqrt3}{1}=\sqrt3$.
'''+asy(fig,'3.5cm')+r'''
On $0^\circ<\theta\le90^\circ$ the tangent is increasing (and undefined at $90^\circ$), so $\tan(A+B)=\sqrt3$ gives $A+B=60^\circ$. Since $A,B\ge0$ and $A+B=60^\circ$, we have $-60^\circ\le A-B\le60^\circ$, and in this range $\tan\theta=0$ only for $\theta=0^\circ$. So $A-B=0^\circ$. Solving,
\[
\boxed{A=B=30^\circ}.
\]''',
'Trigonometry|Special right triangles',2,
note='The assumption A, B >= 0 is added so that tan(A - B) = 0 forces A = B (otherwise A - B could be a multiple of 180 degrees).')

# ---------------- 1784529 pyramid of blocks
b.add(1784529,1,r'''The top level of a pyramid has $1$ block, the next level has $3$ blocks, the next has $9$ blocks, and so on, each level having three times as many blocks as the level above it. If the total number of blocks is $3280$, how many levels are there?''',
r'''With $n$ levels the total is the geometric sum
\[
1+3+9+\dots+3^{n-1}=\dfrac{3^n-1}{3-1}=\dfrac{3^n-1}{2}.
\]
Setting $\dfrac{3^n-1}{2}=3280$ gives $3^n=6561=3^8$, so there are $\boxed{8}$ levels.''',
'Geometric sequences|Exponents',2)

# ---------------- 1784580 point on y-axis equidistant
fig=r'''pair P=(7,6),Q=(-3,4),M=(0,15);
draw((-4.5,0)--(8.5,0),Arrow(6));draw((0,-0.8)--(0,17),Arrow(6));
label("$x$",(8.5,0),E);label("$y$",(0,17),N);
draw(M--P,dashed+blue);draw(M--Q,dashed+blue);
dot(P);dot(Q);dot(M,red);
label("$(7,6)$",P,E);label("$(-3,4)$",Q,W);label("$M(0,15)$",M,E,red);
label("$\sqrt{130}$",(M+P)/2,NE,blue);label("$\sqrt{130}$",(M+Q)/2,W,blue);'''
b.add(1784580,1,r'''Find the point on the $y$-axis which is equidistant from $(7,6)$ and $(-3,4)$.''',
r'''A point on the $y$-axis is $(0,y)$. Equal squared distances give
\[
(0-7)^2+(y-6)^2=(0+3)^2+(y-4)^2\ \Longrightarrow\ 49+y^2-12y+36=9+y^2-8y+16 ,
\]
so $85-12y=25-8y$, $4y=60$ and $y=15$. The point is $\boxed{(0,15)}$. Check: both distances are $\sqrt{49+81}=\sqrt{9+121}=\sqrt{130}$.
'''+asy(fig,'5cm'),
'Distance formula|Coordinate geometry|Perpendicular bisectors',2)

# ---------------- 1784598 is 300 a term of 102, 106, ...
b.add(1784598,1,r'''Is $300$ a term of the arithmetic progression $102,106,110,\dots$? Justify your answer.''',
r'''The $n$th term is $102+4(n-1)$. If $300$ were a term, then $4(n-1)=198$, i.e.\ $n-1=49.5$, which is not an integer. (Equivalently, every term is $\equiv2\pmod4$, while $300\equiv0\pmod4$.) So $\boxed{300\text{ is not a term}}$; the nearest terms are $298$ and $302$.''',
'Arithmetic sequences|Remainders and congruences',1)

# ---------------- 1781932 reverse marathon example P0 (alias)
b.add(1781932,0,r'''Find all positive integers $n$ such that, when $n^2$ and $n^3$ are written down, each of the digits $0$ to $9$ is written exactly once.''',
r'''The digit counts force $n^2$ and $n^3$ to have $10$ digits in total, which gives $47\le n\le99$; checking the candidates (with the digit sum condition $n^2+n^3\equiv45\equiv0\pmod 9$) leaves only $69^2=4761$, $69^3=328509$. Answer: $\boxed{69}$.''',
'Digits and bases|Perfect squares|Perfect cubes|Systematic counting',4,
note='Example problem P0 in the rules of a "reverse marathon". Repeat of an earlier record (aliased).')

# ---------------- 1784461 2^(16^x)=16^(2^x) (alias)
b.add(1784461,1,r'''Find $x$ if $2^{16^x}=16^{2^x}$.''',
r'''$16^{2^x}=2^{4\cdot2^x}=2^{2^{x+2}}$ and $2^{16^x}=2^{2^{4x}}$, so $4x=x+2$ and $x=\boxed{\dfrac23}$.''',
'Exponents',3,source=src('Mandelbrot',None,None,3),
note='Repeat of an earlier record (aliased).')

b.save()
