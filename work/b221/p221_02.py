from qb import *
b=Bank('p221_02')

# ---------------- 1785447 fishing
b.add(1785447,1,r'''Timmy goes fishing from $3$ PM to $7{:}30$ PM. Assume that fish are caught at random so that the probability of catching no fish during any period of $t$ hours is $(0.8)^t$, independently for non-overlapping periods; in particular, the chance of catching at least one fish in any given hour is $20\%$. What is the probability that Timmy catches at least one fish? Give the exact value and a decimal approximation.''',
r'''Timmy fishes for $4.5=\dfrac92$ hours. The probability of catching no fish in that time is
\[
(0.8)^{\dfrac92}=\left(\dfrac45\right)^{4}\left(\dfrac45\right)^{\dfrac12}=\dfrac{256}{625}\cdot\dfrac{2}{\sqrt5}=\dfrac{512\sqrt5}{3125}\approx0.3664 .
\]
So the probability of catching at least one fish is
\[
\boxed{1-\dfrac{512\sqrt5}{3125}}\approx0.634 .
\]
(For comparison: if only the four complete hours counted, the answer would be $1-0.8^4=0.5904$; the half hour raises it.)''',
'Complementary probability|Independent events|Exponents',3,
note='The post gives a 20% chance "every hour" but a fishing time of 4.5 hours, so the half hour is ambiguous. The record states the natural continuous-time model (no fish in t hours with probability 0.8^t), which gives 1 - 0.8^4.5.')

# ---------------- 1786990 pyramid cut by a plane (alias)
b.add(1786990,1,r'''In right pyramid $PABCD$, $ABCD$ is a square of side $2$, and the distance from $P$ to the centre $O$ of the square is $1$. A plane through $A$ meets edges $PB$, $PC$, $PD$ at $B'$, $C'$, $D'$. If $\dfrac{B'B}{PB}=\dfrac14$ and $\dfrac{D'D}{PD}=\dfrac15$, find $\dfrac{C'C}{PC}$.''',
r'''For a plane through $A$ cutting the edges of a pyramid over a parallelogram, $\dfrac{PA}{PA'}+\dfrac{PC}{PC'}=\dfrac{PB}{PB'}+\dfrac{PD}{PD'}$. Here $A'=A$, $\dfrac{PB}{PB'}=\dfrac43$ and $\dfrac{PD}{PD'}=\dfrac54$, so $\dfrac{PC}{PC'}=\dfrac43+\dfrac54-1=\dfrac{19}{12}$ and $\dfrac{C'C}{PC}=1-\dfrac{12}{19}=\boxed{\dfrac{7}{19}}$.''',
'Pyramids|Solid geometry|Ratios, proportions, and variation',5,
note='"O" in the post is the apex P. Repeat of an earlier record (aliased).')

# ---------------- 1787427 normal distribution
b.add(1787427,1,r'''On a test whose scores are normally distributed, a score of $58$ is two standard deviations below the mean, and a score of $85$ is one standard deviation above the mean. What is the mean score?''',
r'''Let the mean be $\mu$ and the standard deviation $\sigma$. Then
\[
\mu-2\sigma=58,\qquad \mu+\sigma=85 .
\]
Subtracting, $3\sigma=27$, so $\sigma=9$ and $\mu=85-9=\boxed{76}$. (Check: $76-18=58$.)''',
'Systems of linear equations|Mean',2)

# ---------------- 1787424 circle with average radius
fig=r'''pair O=(0,0);
draw(circle(O,10),linewidth(0.8));
draw(circle(O,7),blue+linewidth(0.9));
draw(circle(O,4),linewidth(0.8));
dot(O);
draw(O--4*dir(200),linewidth(0.6));draw(O--7*dir(90),blue+linewidth(0.6));draw(O--10*dir(-30),linewidth(0.6));
label("$4$",2*dir(200),dir(110));
label("$7$",(0,4.6),E,blue);
label("$10$",8.5*dir(-30),dir(60));
label("$O$",O,dir(-95));'''
b.add(1787424,1,r'''What is the area of the circle whose radius is the average of the radii of two circles with areas $16\pi$ and $100\pi$?''',
r'''A circle of area $\pi r^2$ has radius $r$, so the two circles have radii $4$ (since $\pi\cdot4^2=16\pi$) and $10$ (since $\pi\cdot10^2=100\pi$). Their average is $\dfrac{4+10}{2}=7$, and the circle of radius $7$ has area $\pi\cdot7^2=\boxed{49\pi}$.
'''+asy(fig,'5cm')+r'''
(Note that this is not the average of the two areas, $58\pi$.)''',
'Circles|Lengths, perimeter, and area|Averages and weighted averages',1)

# ---------------- 1787422 mean increased
b.add(1787422,1,r'''The arithmetic mean of a set of $20$ test scores is $x$. If each score is increased by $y$ points, which expression represents the arithmetic mean of the revised set of test scores?

$\textbf{(A)}\ x+y\qquad\textbf{(B)}\ x+20y\qquad\textbf{(C)}\ x+\dfrac{y}{20}\qquad\textbf{(D)}\ \dfrac{x+y}{20}$''',
r'''The original scores have total $20x$. Adding $y$ to each of the $20$ scores adds $20y$ to the total, so the new total is $20x+20y$ and the new mean is
\[
\dfrac{20x+20y}{20}=x+y .
\]
The answer is $\boxed{\textbf{(A)}\ x+y}$.''',
'Mean|Algebraic expressions and identities',1,
note='Choices C and D, typed "x + y/20" and "x+y /20", are read as x + y/20 and (x+y)/20.')

# ---------------- 1787280 sum of 9 with two dice
b.add(1787280,1,r'''What is the probability of rolling a sum of $9$ with two fair six-sided dice?''',
r'''There are $6\cdot6=36$ equally likely ordered outcomes. The sum $9$ arises from $(3,6),(4,5),(5,4),(6,3)$, which is $4$ outcomes. So the probability is $\dfrac{4}{36}=\boxed{\dfrac19}$.''',
'Dice probability|Probability',1,
note='P1 of a counting and probability marathon.')

# ---------------- 1787277 tiles (alias)
b.add(1787277,1,r'''In a pile of $25$ tiles, each tile has one of the letters A through E and one of the integers from $1$ through $5$. Each possible combination of a letter and a number appears on exactly one of the tiles. Jessica selects three tiles at random, without replacement, from the pile. What is the probability that each of the three tiles Jessica chooses has a letter or a number in common with at least one of the other chosen tiles? Express your answer as a common fraction.''',
r'''Of the $\dbinom{25}{3}=2300$ equally likely triples, the good ones are: three tiles sharing a letter or sharing a number ($10\dbinom53=100$), and ``L-shapes'', in which one tile shares its letter with a second tile and its number with the third ($25\cdot4\cdot4=400$: choose the corner tile, then the second and third tiles). So the probability is $\dfrac{500}{2300}=\boxed{\dfrac{5}{23}}$.''',
'Probability|Casework',5,source=src('MATHCOUNTS',2017,'National',26,rnd='Sprint'),
note='Repeat of an earlier record (aliased).')

# ---------------- 1787262 y=-3x+b through a point
b.add(1787262,1,r'''Find the value of $b$ if the graph of $y=-3x+b$ passes through the given point.
\begin{enumerate}
\item[(a)] $A(-2,4)$
\item[(b)] $B(5,2)$
\end{enumerate}''',
r'''Substitute the coordinates of the point into $y=-3x+b$ and solve for $b$.

\textbf{(a)} $4=-3(-2)+b=6+b$, so $\boxed{b=-2}$.

\textbf{(b)} $2=-3(5)+b=-15+b$, so $\boxed{b=17}$.''',
'Linear equations|Substitution',1)

# ---------------- 1787120 chord AC, angle POB = 90
fig=r'''pair O=(0,0),A=(-2,0),B=(2,0),P=(0,1.5),C=(14/25,48/25);
draw(circle(O,2),linewidth(0.8));
draw(A--B,linewidth(0.8));
draw(A--C,linewidth(0.9));
draw(O--P,linewidth(0.8));
draw(C--B,dashed);
draw((0,0)--(0.22,0)--(0.22,0.22)--(0,0.22),linewidth(0.5));
pair u=unit(A-C),v=unit(B-C);
draw(C+0.22*u--C+0.22*(u+v)--C+0.22*v,linewidth(0.5)+gray);
dot(O);dot(P);
label("$A$",A,W);label("$B$",B,E);label("$C$",C,NE);label("$O$",O,S);label("$P$",P,NW);
label("$\dfrac32$",(0,0.75),E);
label("$2$",(-1,0),S);'''
b.add(1787120,1,r'''Circle $\omega$ with centre $O$ has diameter $AB$. Point $C$ lies on the circle and point $P$ lies on chord $\overline{AC}$ such that $\angle POB=90^\circ$. If the radius of $\omega$ is $2$ and $OP=\dfrac32$, what is the length of segment $\overline{AC}$?''',
r'''Triangle $AOP$ has a right angle at $O$, with $AO=2$ and $OP=\dfrac32$, so
\[
AP=\sqrt{4+\dfrac94}=\dfrac52 .
\]
Since $AB$ is a diameter, $\angle ACB=90^\circ$. Triangles $AOP$ and $ACB$ are right-angled (at $O$ and at $C$) and share the angle at $A$, so they are similar, and
\[
\dfrac{AC}{AB}=\dfrac{AO}{AP}\ \Longrightarrow\ AC=4\cdot\dfrac{2}{\dfrac52}=\boxed{\dfrac{16}{5}}.
\]
'''+asy(fig,'6cm')+r'''
(Check with coordinates: $O=(0,0)$, $A=(-2,0)$, $P=\left(0,\dfrac32\right)$; line $AP$ meets the circle again at $C=\left(\dfrac{14}{25},\dfrac{48}{25}\right)$, and $AC=\sqrt{\left(\dfrac{64}{25}\right)^2+\left(\dfrac{48}{25}\right)^2}=\dfrac{80}{25}=\dfrac{16}{5}$.)''',
'Circles|Inscribed angles|Similarity|Right triangles|Pythagorean theorem',3)

# ---------------- 1786975 79th number not divisible by 4 or 7
b.add(1786975,1,r'''$K$ is the set of positive integers that are divisible neither by $4$ nor by $7$. Find the $79$th smallest member of $K$.''',
r'''Whether a number lies in $K$ depends only on its remainder modulo $28=\operatorname{lcm}(4,7)$. Among $1,\dots,28$ there are $7$ multiples of $4$, $4$ multiples of $7$ and $1$ multiple of both, so by inclusion--exclusion $28-7-4+1=18$ numbers lie in $K$. Each block of $28$ consecutive integers therefore contains $18$ members of $K$.

Since $79=4\cdot18+7$, the first $4$ blocks ($1$ to $112$) contain $72$ members, and we need the $7$th member after $112$. Skipping $116$, $119$ and $120$, the members are
\[
113,\ 114,\ 115,\ 117,\ 118,\ 121,\ 122,\ \dots
\]
so the $79$th member is $\boxed{122}$.''',
'Sets and inclusion–exclusion|Divisibility|Remainders and congruences',3)

# ---------------- 1785652 factory
b.add(1785652,1,r'''To finish an order on time, a factory was supposed to produce $70$ items per day. After hiring three more workers, it produced $10$ more items per day than planned and completed the order $5$ days ahead of schedule. How many days was the order originally supposed to take?''',
r'''Let the planned number of days be $d$. The order consists of $70d$ items, and at $80$ items per day it took $d-5$ days:
\[
70d=80(d-5)\ \Longrightarrow\ 10d=400\ \Longrightarrow\ d=\boxed{40}.
\]
(Check: the order is $2800$ items; $2800\div80=35=40-5$.)''',
'Work and rates|Linear equations',2,
note='Read as: the higher rate held for the whole order ("details" in the post means items).')

# ---------------- 1786099 fraction modulo 25
b.add(1786099,1,r'''The expression ``$\dfrac49\pmod{25}$'' means the residue $x$ modulo $25$ with $9x\equiv4\pmod{25}$. Explain why such an $x$ exists and is unique modulo $25$, and find it with $0\le x\le24$.''',
r'''\textbf{Existence and uniqueness.} Since $\gcd(9,25)=1$, multiplication by $9$ permutes the residues modulo $25$: if $9x\equiv9x'$, then $25\mid9(x-x')$, and so $25\mid x-x'$. So exactly one residue $x$ satisfies $9x\equiv4$.

\textbf{Inverse of $9$.} We need $9y\equiv1\pmod{25}$: $9\cdot14=126=5\cdot25+1$, so $9^{-1}\equiv14$.

\textbf{The fraction.} $x\equiv4\cdot14=56\equiv\boxed{6}\pmod{25}$. Check: $9\cdot6=54=2\cdot25+4$.''',
'Remainders and congruences|Linear Diophantine equations',2,
note='The post asks how to take a fraction modulo 25 (example 4/9 mod 25); the record defines it via the modular inverse and computes it.')

# ---------------- 1786616 circular table
b.add(1786616,1,r'''Five people sit at a round table with $6$ identical seats; seatings that differ only by a rotation of the table are considered the same. In how many ways can they sit? More generally, in how many ways can $k$ people sit at a round table with $n$ seats ($k\le n$)?''',
r'''Treat each empty seat as a placeholder. Seat the people in a row of $n$ labelled seats first: there are $n(n-1)\cdots(n-k+1)=\dfrac{n!}{(n-k)!}$ ways. Each seating around the table corresponds to exactly $n$ labelled seatings (one for each rotation), and these are all different, because a rotation by $1,2,\dots,n-1$ places moves at least one person to a different seat. Hence the number of seatings is
\[
\dfrac{1}{n}\cdot\dfrac{n!}{(n-k)!}=\boxed{\dfrac{(n-1)!}{(n-k)!}} .
\]
For $k=5$, $n=6$ this is $\dfrac{5!}{1!}=\boxed{120}$. (Equivalently: fix the first person's seat to remove the rotations; the other four people can then be placed in $5\cdot4\cdot3\cdot2=120$ ways in the remaining five seats.)''',
'Circular arrangements|Permutations',3,
note='Read with rotations of the table identified and the empty seats indistinguishable.')

# ---------------- 1765739 a^3+b^3+c^3 >= a^2b+b^2c+c^2a
b.add(1765739,1,r'''Let $a,b,c$ be positive real numbers. Prove that
\[
a^3+b^3+c^3\ge a^2b+b^2c+c^2a .
\]''',
r'''By AM-GM for the three positive numbers $a^3,a^3,b^3$,
\[
\dfrac{a^3+a^3+b^3}{3}\ge\sqrt[3]{a^6b^3}=a^2b .
\]
In the same way $\dfrac{2b^3+c^3}{3}\ge b^2c$ and $\dfrac{2c^3+a^3}{3}\ge c^2a$. Adding the three inequalities,
\[
\dfrac{3a^3+3b^3+3c^3}{3}\ge a^2b+b^2c+c^2a,
\]
which is the claim. Equality requires $a=b$, $b=c$ and $c=a$, i.e.\ $a=b=c$. $\blacksquare$''',
'AM-GM inequality|Inequalities',3,
note='The post also asks for a general explanation of AM-GM and practice problems; only the stated inequality is used.')

# ---------------- 1785946 square, AX = AY, area 1/4
fig=r'''real t=sqrt(2)/2;
pair A=(0,0),B=(1,0),C=(1,1),D=(0,1),X=(1,t),Y=(t,1);
fill(A--X--Y--cycle,lightgray);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--X--Y--cycle,linewidth(0.8));
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);
label("$X$",X,E);label("$Y$",Y,NW);
label("$t$",(1,t/2),E);label("$t$",(t/2,1),N);
label("$1-t$",(1,(1+t)/2),E,fontsize(8pt));label("$1-t$",((1+t)/2,1),N,fontsize(8pt));'''
b.add(1785946,1,r'''Square $ABCD$ has side length $1$. Point $X$ lies on $BC$ and point $Y$ lies on $CD$ so that $AX=AY$, and the area of triangle $AXY$ is $\dfrac14$ of the area of $ABCD$. What is the length of $XY$? Express your answer in simplest radical form.''',
r'''Right triangles $ABX$ and $ADY$ have $AB=AD$ and $AX=AY$, so they are congruent (hypotenuse-leg) and $BX=DY=t$, say. Then $CX=CY=1-t$.
'''+asy(fig,'5cm')+r'''
The triangle $AXY$ is the square minus three right triangles:
\[
[AXY]=1-\dfrac t2-\dfrac t2-\dfrac{(1-t)^2}{2}.
\]
With $u=1-t$ this is $u-\dfrac{u^2}{2}$, and setting it equal to $\dfrac14$ gives $2u^2-4u+1=0$, so $u=1\pm\dfrac{\sqrt2}{2}$. Since $0\le u\le1$, $u=1-\dfrac{\sqrt2}{2}$. Finally $XY$ is the hypotenuse of the isosceles right triangle $XCY$:
\[
XY=u\sqrt2=\sqrt2-1 .
\]
So $XY=\boxed{\sqrt2-1}$. (Check: $t=\dfrac{\sqrt2}{2}$ and $[AXY]=1-\dfrac{\sqrt2}{2}-\dfrac{\left(1-\dfrac{\sqrt2}{2}\right)^2}{2}=\dfrac14$.)''',
'Squares|Congruence|Lengths, perimeter, and area|Area decomposition|Quadratic equations',4)

# ---------------- 1786360 series 2 + 5/11 + 9/11^2 + 14/11^3 + ...
b.add(1786360,1,r'''The numerators $2,5,9,14,\dots$ of the series
\[
2+\dfrac{5}{11}+\dfrac{9}{11^2}+\dfrac{14}{11^3}+\cdots
\]
continue so that their consecutive differences are $3,4,5,6,\dots$ (so the next numerators are $20,27,\dots$). Find the exact value of the series.''',
r'''Let $x=\dfrac1{11}$ and $S=\sum_{n\ge0}a_nx^n$ with $a_0=2$ and $a_n-a_{n-1}=n+2$ for $n\ge1$. All series below converge absolutely since $|x|<1$ and $a_n$ grows only quadratically.

Multiply by $1-x$:
\[
(1-x)S=a_0+\sum_{n\ge1}(a_n-a_{n-1})x^n=2+3x+4x^2+5x^3+\cdots=\sum_{n\ge0}(n+2)x^n .
\]
Multiply by $1-x$ again:
\[
(1-x)^2S=2+\sum_{n\ge1}\bigl((n+2)-(n+1)\bigr)x^n=2+\dfrac{x}{1-x}.
\]
With $x=\dfrac1{11}$: $\dfrac{x}{1-x}=\dfrac1{10}$ and $(1-x)^2=\dfrac{100}{121}$, so
\[
S=\dfrac{21}{10}\cdot\dfrac{121}{100}=\boxed{\dfrac{2541}{1000}}=2.541 .
\]''',
'Sequences and series|Summation|Geometric sequences|Pattern recognition',4,
note='The post gives only four terms; the rule for the numerators (differences 3, 4, 5, ..., i.e. a_n = (n+2)(n+3)/2 - 1) is stated in the record.')

# ---------------- 1606524 continued fraction 40/(3+...)
b.add(1606524,1,r'''Evaluate the infinite expression
\[
\dfrac{40}{3+\dfrac{40}{3+\dfrac{40}{3+\cdots}}},
\]
understood as the limit of the finite expressions $x_1=\dfrac{40}{3}$, $x_{k+1}=\dfrac{40}{3+x_k}$.''',
r'''\textbf{The value must satisfy an equation.} If the limit is $x$, then $x\ge0$ and the expression repeats itself inside: $x=\dfrac{40}{3+x}$. So $x^2+3x-40=0$, i.e.\ $(x+8)(x-5)=0$, and since $x\ge0$, $x=5$.

\textbf{The limit exists.} Every $x_k$ is positive, so $x_{k+1}=\dfrac{40}{3+x_k}<\dfrac{40}{3}$ for all $k$, and hence $x_{k+2}=\dfrac{40}{3+x_{k+1}}>\dfrac{40}{3+\dfrac{40}{3}}=\dfrac{120}{49}>2$. So for $k\ge2$ we have $3+x_k>5$ and
\[
|x_{k+1}-5|=\left|\dfrac{40}{3+x_k}-\dfrac{40}{8}\right|=\dfrac{5\,|x_k-5|}{3+x_k}\le\dfrac{5}{3+\dfrac{120}{49}}\,|x_k-5|=\dfrac{245}{267}\,|x_k-5| .
\]
The distance to $5$ shrinks at least by the fixed factor $\dfrac{245}{267}<1$ at every step, so $x_k\to5$.

The value is $\boxed{5}$.''',
'Continued fractions|Quadratic equations',2)

# ---------------- 1786041 derangement recurrence
b.add(1786041,1,r'''Let $D_n$ be the number of derangements of $n$ objects (arrangements in which no object is in its original place), with $D_1=0$ and $D_2=1$.
\begin{enumerate}
\item[(a)] Prove that $D_{n+2}=(n+1)\left(D_{n+1}+D_n\right)$ for every positive integer $n$. So in the recurrence $D_{n+2}=aD_{n+1}+bD_n$ given by this argument, $a=b=n+1$; what is $\dfrac ba$?
\item[(b)] Show that there are no constants $a,b$ (independent of $n$) with $D_{n+2}=aD_{n+1}+bD_n$ for all $n$.
\end{enumerate}''',
r'''\textbf{(a)} Consider derangements of $1,2,\dots,n+2$ (object $i$ must not be in place $i$). Object $1$ goes to some place $k\ne1$: $n+1$ choices, each giving the same count. Fix $k$ and look at object $k$.
\begin{itemize}
\item If object $k$ goes to place $1$, objects $1$ and $k$ simply swap, and the other $n$ objects form a derangement of their own places: $D_n$ ways.
\item If object $k$ does not go to place $1$, then the remaining $n+1$ objects (all except object $1$) must fill places $\{1,\dots,n+2\}\setminus\{k\}$ with each object $j\ne k$ avoiding place $j$ and object $k$ avoiding place $1$. Treating place $1$ as object $k$'s ``forbidden'' place, these are exactly derangements of $n+1$ objects: $D_{n+1}$ ways.
\end{itemize}
Hence $D_{n+2}=(n+1)\left(D_{n+1}+D_n\right)$, so $a=b=n+1$ and $\dfrac ba=\boxed{1}$.

\textbf{(b)} The first values are $D_1=0$, $D_2=1$, $D_3=2$, $D_4=9$, $D_5=44$. Constants $a,b$ would need $D_3=aD_2+bD_1$, so $a=2$; then $D_4=aD_3+bD_2$ gives $9=4+b$, so $b=5$; but then $aD_4+bD_3=18+10=28\ne44=D_5$. So no constant coefficients work, and $a$, $b$ must be read as depending on $n$. $\blacksquare$''',
'Derangements|Recurrence relations|Recursive counting',4,
note='As posed (constants a, b with D_{n+2} = a D_{n+1} + b D_n for all n), the problem has no solution, as part (b) shows; the intended recurrence is the standard D_{n+2} = (n+1)(D_{n+1} + D_n), giving b/a = 1. The record proves it and explains the issue.')

# ---------------- 1785634 popcorn1's rejected AMC 8 problems 1-5
b.add(1785634,1,r'''What is $\dfrac{\dfrac12}{\dfrac13}-\dfrac23$?''',
r'''Dividing by $\dfrac13$ is multiplying by $3$, so $\dfrac{\dfrac12}{\dfrac13}=\dfrac32$, and $\dfrac32-\dfrac23=\dfrac{9-4}{6}=\boxed{\dfrac56}$.''',
'Fractions',1)
b.add(1785634,2,r'''How many times does the digit $0$ appear in the sum $555{,}555{,}555{,}555+555{,}555{,}555{,}555$?''',
r'''Add column by column: the units column gives $5+5=10$, so write $0$ and carry $1$; each of the other eleven columns gives $5+5+1=11$, so write $1$ and carry $1$; the final carry gives a leading $1$. The sum is $1{,}111{,}111{,}111{,}110$. So the digit $0$ appears $\boxed{1}$ time.''',
'Whole-number operations|Place value',1)
b.add(1785634,3,r'''For a positive integer $n$, let $n\bigotimes$ be the number of ways to arrange $n+1$ distinct objects in a row, divided by one less than the number of objects. How many times does the digit $1$ appear in the decimal representation of $10\bigotimes$?''',
r'''With $n+1$ objects there are $(n+1)!$ arrangements, and one less than the number of objects is $n$, so $n\bigotimes=\dfrac{(n+1)!}{n}$. Hence
\[
10\bigotimes=\dfrac{11!}{10}=\dfrac{39916800}{10}=3991680 ,
\]
whose digits are $3,9,9,1,6,8,0$. The digit $1$ appears $\boxed{1}$ time.''',
'Factorials|Permutations',2,
note='"the number of ones in the representation" is read as the number of digits 1 in the decimal representation.')
b.add(1785634,4,r'''A fly is at the centre of a cubical room whose walls (edges) have length $3$ feet. The fly travels $8$ inches up, then $6$ inches to its left (horizontally, parallel to two of the walls), then $2\sqrt2$ inches down. It never hits a wall. After it moves, the distance from the fly to each of the six faces of the room (four walls, floor and ceiling) is measured. What is the average of these six distances?''',
r'''The room is $36$ inches on each side, so for any point inside it the distances to two opposite faces add up to $36$ inches. The six faces form three opposite pairs, so the six distances add up to $3\cdot36=108$ inches wherever the fly is, and their average is $\dfrac{108}{6}=\boxed{18\text{ inches}}$.

(Explicitly: the fly ends $8-2\sqrt2$ inches above the centre and $6$ inches to the left, so the distances are $18+8-2\sqrt2$ and $18-8+2\sqrt2$ to floor and ceiling, $12$ and $24$ to the left and right walls, and $18$ and $18$ to the front and back walls.)''',
'Unit conversion|Averages and weighted averages|Symmetry',2,
note='"the center cubical room" is read as the centre of a cubical room; the faces include floor and ceiling.')
fig=r'''real s=4*sqrt(2);
pair A=(0,0),B=(0,s),C=(s,s),D=(s,0),P=(1/sqrt(2),1/sqrt(2));
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--C,dashed+gray);
draw(P--A,blue+linewidth(0.8));draw(P--B,blue+linewidth(0.8));draw(P--C,blue+linewidth(0.8));draw(P--D,blue+linewidth(0.8));
dot(P);
label("$A$",A,SW);label("$B$",B,NW);label("$C$",C,NE);label("$D$",D,SE);label("$P$",P,dir(-45));
label("$1$",(P+A)/2,NW,fontsize(9pt));
label("$5$",(P+B)/2,E);label("$7$",(P+C)/2+(0.15,-0.15),SE);label("$5$",(P+D)/2,N);'''
b.add(1785634,5,r'''The distances from a point inside a square to the vertices of the square are, in clockwise order, $1$, $5$, $7$, $5$. Find the area of the square.''',
r'''Let the square be $ABCD$ (clockwise) and the point $P$, with $PA=1$, $PB=5$, $PC=7$, $PD=5$.

Since $PB=PD$, $P$ lies on the perpendicular bisector of the diagonal $BD$, which is the other diagonal $AC$. As $P$ is inside the square, it lies on segment $AC$, so
\[
AC=PA+PC=1+7=8 .
\]
'''+asy(fig,'5.5cm')+r'''
A square with diagonal $8$ has area $\dfrac{8^2}{2}=\boxed{32}$.

Check: the side is $4\sqrt2$, and with $A=(0,0)$, $B=(0,4\sqrt2)$, $P=\left(\dfrac{1}{\sqrt2},\dfrac{1}{\sqrt2}\right)$ one gets $PB^2=\dfrac12+\dfrac{49}{2}=25$, as required.''',
'Squares|Diagonals|Perpendicular bisectors|Lengths, perimeter, and area',3,
note='Problem 6 of the post is not given ("I do have a problem 6, but it is quite bad"), so only problems 1-5 are used.')

# ---------------- aliases (repeats of earlier records)
b.add(1786654,1,r'''What is the probability that three real numbers chosen independently and uniformly at random between $0$ and $1$ have a sum less than $1$? Express your answer as a common fraction.''',
r'''The region $x,y,z\ge0$, $x+y+z<1$ is a tetrahedron of volume $\dfrac16$ inside the unit cube, so the probability is $\boxed{\dfrac16}$.''',
'Geometric probability|Volume',3,source=src('MATHCOUNTS',2018,'State',25,rnd='Sprint'),note='Repeat of an earlier record (aliased).')
b.add(1786839,1,r'''Ivory writes down three two-digit numbers, each with units digit $7$. The tens digit of the product of these three numbers is $5$. What is the tens digit of the sum of the three numbers?''',
r'''With tens digits $a,b,c$, the product is $\equiv90(a+b+c)+43\pmod{100}$, so its tens digit is the last digit of $9(a+b+c)+4$; this is $5$ exactly when $a+b+c\equiv9\pmod{10}$. The sum of the numbers is $10(a+b+c)+21$, whose tens digit is the last digit of $a+b+c+2$, namely $\boxed{1}$.''',
'Units digits and last digits|Remainders and congruences',4,source=src('MATHCOUNTS',2018,'State',24,rnd='Sprint'),note='Repeat of an earlier record (aliased).')
b.add(1786904,1,r'''If $x$ and $y$ satisfy $(x-3)^2+(y-4)^2=49$, what is the minimum possible value of $x^2+y^2$?''',
r'''The origin is at distance $5$ from the centre $(3,4)$ of the circle of radius $7$, so the nearest point of the circle is at distance $2$ from the origin and the minimum is $\boxed{4}$.''',
'Circles|Distance formula|Maxima and minima',3,note='Same problem as 2012 MATHCOUNTS National Sprint #29. Repeat of an earlier record (aliased).')
b.add(1786656,1,r'''Oliver rolls three fair standard six-sided dice. What is the probability that there is at least one pair of dice whose top faces sum to $6$? Express your answer as a common fraction.''',
r'''Counting the $216$ outcomes directly (pairs summing to $6$ are $\{1,5\},\{2,4\},\{3,3\}$) gives $\boxed{\dfrac{19}{54}}$.''',
'Dice probability|Casework|Complementary counting',4,source=src('MATHCOUNTS',2018,'State',27,rnd='Sprint'),note='Repeat of an earlier record (aliased).')
b.add(1654926,1,r'''Find the missing term of the sequence $1,\ 11,\ 21,\ 1211,\ \_\_\_,\ 312211$.''',
r'''This is the look-and-say sequence: each term reads off the runs of digits of the previous one. $1211$ is ``one $1$, one $2$, two $1$s'', so the missing term is $\boxed{111221}$, and indeed $111221$ reads ``three $1$s, two $2$s, one $1$'' $=312211$.''',
'Pattern recognition|Sequences and series',2,note='Repeat of an earlier record (aliased).')

b.save()
