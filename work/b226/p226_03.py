from qb import *
b=Bank('p226_03')

# ---------------- 1760410 French Spanish Latin
b.add(1760410,1,r'''Of $100$ students, $56$ take French, $60$ take Spanish and $20$ take Latin, and every student takes at least one of these three subjects. What is the minimum number of students who take more than one of the subjects?''',
r'''Let $x_1,x_2,x_3$ be the numbers of students taking exactly one, two and three subjects. Then
\[
x_1+x_2+x_3=100,\qquad x_1+2x_2+3x_3=56+60+20=136 .
\]
Subtracting, $x_2+2x_3=36$, so the number taking more than one subject is $x_2+x_3=36-x_3$. Since everyone taking all three takes Latin, $x_3\le20$; and $x_2=36-2x_3\ge0$ gives $x_3\le18$. Hence $x_2+x_3\ge36-18=18$.

This is achieved: let $18$ students take all three subjects and nobody take exactly two; then $56-18=38$ take only French, $60-18=42$ only Spanish and $20-18=2$ only Latin, and $18+38+42+2=100$. The minimum is $\boxed{18}$.''',
'Sets and inclusion–exclusion|Venn diagrams|Bounding and extremal cases',3)

# ---------------- 1759490 3x+5y
b.add(1759490,1,r'''Prove that every integer $n>7$ can be written as $n=3x+5y$ with $x$ and $y$ nonnegative integers.''',
r'''The three consecutive integers $8,9,10$ can be written in this form:
\[
8=3\cdot1+5\cdot1,\qquad 9=3\cdot3+5\cdot0,\qquad 10=3\cdot0+5\cdot2 .
\]
Now let $n>10$ and suppose every integer from $8$ to $n-1$ is representable (strong induction). Then $n-3\ge8$ is representable, say $n-3=3x+5y$, and $n=3(x+1)+5y$ is representable too. Hence every integer $n\ge8$ is of the form $3x+5y$ with $x,y\ge0$. $\blacksquare$

(Equivalently: every $n\ge8$ is $8+3k$, $9+3k$ or $10+3k$ for some $k\ge0$. The bound is sharp, since $7$ is not of this form.)''',
'Linear Diophantine equations|Mathematical induction|Remainders and congruences',2)

# ---------------- 1760131 sum of cubes, combinatorial
b.add(1760131,1,r'''Give a combinatorial proof that for every positive integer $n$,
\[
1^3+2^3+\cdots+n^3=\dbinom{n+1}{2}^2 .
\]''',
r'''Count the ordered pairs $(S,T)$ of $2$-element subsets of $\{1,2,\dots,n+1\}$. There are $\dbinom{n+1}{2}^2$ of them.

Now sort them by $d=\max(S\cup T)$, which can be $2,3,\dots,n+1$. Fix $d$; all elements of $S$ and $T$ lie in $\{1,\dots,d\}$ and $d$ is the largest element of at least one of them.
\begin{itemize}
\item $\max S=\max T=d$: each of $S,T$ is $d$ together with one of $1,\dots,d-1$: $(d-1)^2$ pairs.
\item $\max S=d>\max T$: $S$ in $d-1$ ways, $T\subseteq\{1,\dots,d-1\}$ in $\dbinom{d-1}{2}$ ways: $(d-1)\dbinom{d-1}2$ pairs; the case $\max T=d>\max S$ gives the same number.
\end{itemize}
So the number with maximum $d$ is
\[
(d-1)^2+2(d-1)\cdot\dfrac{(d-1)(d-2)}{2}=(d-1)^2\bigl(1+(d-2)\bigr)=(d-1)^3 .
\]
Summing over $d=2,\dots,n+1$ counts every pair once, so $\dbinom{n+1}{2}^2=\displaystyle\sum_{d=2}^{n+1}(d-1)^3=1^3+2^3+\cdots+n^3$. $\blacksquare$''',
'Double counting|Combinatorial identities and binomial coefficients|Summation|Casework',5,
note='The post writes the identity as C(n,2)^2 = 1^3 + ... + n^3, which is false (n = 2 gives 1 vs 9); corrected to C(n+1,2)^2, the identity the poster means. The question "is there a combinatorial reason?" is posed as a combinatorial proof.')

# ---------------- 1759713 MATHCOUNTS handbook warm-up 12
b.add(1759713,1,r'''What is the greatest common divisor of $2563$ and $4147$?''',
r'''A quick route is the divisibility test for $11$ (alternating digit sums): $2-5+6-3=0$ and $4-1+4-7=0$, so $11$ divides both. Then $2563=11\cdot233$ and $4147=11\cdot377=11\cdot13\cdot29$. The number $233$ is prime (it is not divisible by $2,3,5,7,11,13$, and $17^2>233$), and it is neither $13$ nor $29$, so $\gcd(233,377)=1$. Hence $\gcd(2563,4147)=\boxed{11}$.

(The Euclidean algorithm gives the same: $4147-2563=1584$, and $\gcd(2563,1584)=\gcd(1584,979)=\cdots=\gcd(22,11)=11$, but it takes many steps here because the quotients are all $1$.)''',
'HCF and LCM|Divisibility rules|Prime factorisation',2)
b.add(1759713,2,r'''In a version of tag football a team earns $5$ points for every touchdown and $3$ points for every field goal. If Paul's team scored a total of $25$ points, how many different sequences of touchdowns and field goals could the team have scored?''',
r'''If there are $a$ touchdowns and $b$ field goals, $5a+3b=25$ with $a,b\ge0$. Then $5\mid3b$, so $5\mid b$: $b=0$, $a=5$ or $b=5$, $a=2$ ($b=10$ is too many). Five touchdowns give $1$ sequence; two touchdowns and five field goals can be ordered in $\dbinom72=21$ ways. The answer is $1+21=\boxed{22}$.''',
'Linear Diophantine equations|Multiset permutations|Casework',3)
b.add(1759713,3,r'''Five numbers form an arithmetic sequence with mean $18$. If the mean of the squares of the five numbers is $374$, what is the greatest of the five original numbers?''',
r'''The middle term equals the mean, so the numbers are $18-2d,18-d,18,18+d,18+2d$. The sum of their squares is
\[
5\cdot18^2+(4+1+0+1+4)d^2=1620+10d^2,
\]
since the cross terms $2\cdot18\cdot kd$ for $k=-2,-1,0,1,2$ cancel. So the mean of the squares is $324+2d^2$. So $324+2d^2=374$, $d^2=25$, $|d|=5$, and the numbers are $8,13,18,23,28$. The greatest is $\boxed{28}$.''',
'Arithmetic sequences|Mean',3)
b.add(1759713,4,r'''An oceanographer tags every dolphin that she sees during one week: at the end of the week she has tagged $1000$ dolphins. One month later she examines $2000$ dolphins and finds that $400$ of them are tagged. Assuming that each time she saw a random sample of the local dolphin population, estimate the number of dolphins in the local population.''',
r'''If the population has $N$ dolphins, the proportion tagged is $\dfrac{1000}{N}$, and the sample should show about the same proportion: $\dfrac{400}{2000}=\dfrac15$. So $\dfrac{1000}{N}=\dfrac15$ and $N=\boxed{5000}$.''',
'Ratios, proportions, and variation|Estimation',2,
note='The post asks for the "expected number"; this capture-recapture estimate is the intended answer, so the record asks to estimate the population.')
fig=r'''pair O=(0,0),A=(-13,0),C=(13,0);
pair B=A+10*dir(degrees(acos(10/26)));
draw(circle(O,13),linewidth(0.8));
draw(A--C,linewidth(0.8));draw(A--B--C,linewidth(0.9));
pair u=unit(A-B),v=unit(C-B);
draw((B+1.3*u)--(B+1.3*u+1.3*v)--(B+1.3*v),linewidth(0.4));
dot(O);
label("$A$",A,W);label("$C$",C,E);label("$B$",B,NW);label("$P$",O,S);
label("$10$",(A+B)/2,2*dir(-22));label("$26$",(A+C)/2+(4,0),S);'''
b.add(1759713,5,r'''Segment $AC$ is a diameter of circle $P$, which has radius $13$ cm. If $B$ is a point on circle $P$ such that $AB=10$ cm, what is the length of segment $BC$?''',
r'''An angle inscribed in a semicircle is a right angle, so $\angle ABC=90^\circ$, and $AC=2\cdot13=26$.
'''+asy(fig,'5.5cm')+r'''
By the Pythagorean theorem, $BC=\sqrt{26^2-10^2}=\sqrt{576}=\boxed{24}$ cm.''',
'Circles|Inscribed angles|Right triangles|Pythagorean theorem',2)

# ---------------- 1759128 local contest problems
fig=r'''real r=4,h=2;
pair O=(0,0);
real yw=-r+h; real xw=sqrt(r^2-(r-h)^2);
real t=degrees(acos((r-h)/r));
path seg=arc(O,r,270-t,270+t)--cycle;
fill(seg,rgb(0.75,0.85,1));
draw(circle(O,r),linewidth(0.9));
draw((-6.5,yw)--(6.5,yw),blue+linewidth(0.6));
draw(O--(xw,yw),dashed);draw(O--(-xw,yw),dashed);draw(O--(0,yw),dashed);
dot(O);label("$O$",O,N);
label("$4$",(xw/2,yw/2),NE);label("$2$",(0,yw/2),E);
draw((-5,-r)--(-5,yw),Arrows(4));draw((-5.4,-r)--(-0.3,-r),gray+dotted);
label("$2$",(-5,(yw-r)/2),W);
label("water level",(6.5,yw),N,blue);'''
b.add(1759128,1,r'''Squidward's clarinet is a solid right circular cylinder with radius $4$ inches and length $16$ inches. He drops it into his bath, and it comes to rest completely horizontal, with the water surface $2$ inches above the lowest line of the clarinet. What volume of water, in cubic inches, does the clarinet displace?''',
r'''The displaced volume is the volume of the part of the cylinder below the water surface: the length $16$ times the area of the circular segment of height $2$ in a circle of radius $4$ (the cross-section).
'''+asy(fig,'5.5cm')+r'''
The water line is at distance $4-2=2$ from the centre $O$, so its half-chord is $\sqrt{16-4}=2\sqrt3$ and it subtends an angle $2\cos^{-1}\dfrac24=120^\circ$ at $O$. The segment's area is the sector minus the triangle:
\[
\dfrac{120}{360}\pi\cdot4^2-\dfrac12\cdot4\sqrt3\cdot2=\dfrac{16\pi}{3}-4\sqrt3 .
\]
The displaced volume is
\[
16\left(\dfrac{16\pi}{3}-4\sqrt3\right)=\boxed{\dfrac{256\pi}{3}-64\sqrt3}\approx157.2\text{ cubic inches}.
\]''',
'Cylinders|Volume|Circles|Arcs and chords|Lengths, perimeter, and area',4,
note='"The water reached a height of 2 in. from the bottom of the clarinet" read as the water surface 2 inches above the lowest line of the horizontal clarinet; the clarinet is treated as a solid cylinder ("height" 16 is its length).')
fig=r'''pair A=(0,0),B=(0,3),C=(5,0);
draw(A--B--C--cycle,linewidth(0.9));
draw((0.35,0)--(0.35,0.35)--(0,0.35),linewidth(0.4));
draw(arc(C,0.8,180-degrees(atan(3/5)),180),linewidth(0.6));label("$C$",C,SE);
label("$A$",A,SW);label("$B$",B,NW);
label("$3$",(A+B)/2,W);label("$x$",(B+C)/2,NE);'''
b.add(1759128,2,r'''In right triangle $ABC$, $\angle A=90^\circ$, $AB=3$ and $BC=x$. If $\sin C=k$, express $AC$ in terms of $k$.''',
r'''$BC$ is the hypotenuse and $AB$ is opposite $C$.
'''+asy(fig,'4.5cm')+r'''
So $\sin C=\dfrac{AB}{BC}=\dfrac3x=k$, giving $x=\dfrac3k$. By the Pythagorean theorem,
\[
AC=\sqrt{x^2-9}=\sqrt{\dfrac{9}{k^2}-9}=\boxed{\dfrac{3\sqrt{1-k^2}}{k}}\qquad(0<k<1).
\]
(Equivalently $AC=\dfrac{AB}{\tan C}=3\cdot\dfrac{\cos C}{\sin C}$.)''',
'Trigonometry|Right triangles|Pythagorean theorem',2,
note='The post writes 90^\\cdot for 90 degrees.')
b.add(1759128,3,r'''Convert $540$ radians into degrees.''',
r'''Since $\pi$ radians equal $180^\circ$, $540$ radians equal $540\cdot\dfrac{180}{\pi}=\boxed{\dfrac{97200}{\pi}}$ degrees, about $30940^\circ$. (If the intended quantity was $540^\circ$, that is $3\pi$ radians.)''',
'Unit conversion|Trigonometry',1)
b.add(1759128,4,r'''How many terms are there in the expansion of $(3a+4b+6c+12d)^6$ after like terms are combined?''',
r'''Every term has the form (positive coefficient)$\cdot a^ib^jc^kd^l$ with $i+j+k+l=6$, $i,j,k,l\ge0$, and every such monomial occurs; since all coefficients are positive, nothing cancels. By stars and bars the number of such monomials is $\dbinom{6+3}{3}=\boxed{84}$.''',
'Stars and bars|Binomial theorem|Polynomials',2)
b.add(1759128,5,r'''John has to run $2$ laps around a circular track. On the first lap he runs at $x$ miles per hour. How fast must he run the second lap so that his average speed over both laps is $2x$ miles per hour?''',
r'''Let a lap have length $L$. To average $2x$ over $2L$ he must take a total time of $\dfrac{2L}{2x}=\dfrac Lx$. But the first lap alone already takes $\dfrac Lx$ hours. So the second lap would have to take no time at all: \textbf{it is impossible}; no finite speed works. (In general, with second-lap speed $v$ the average is the harmonic mean $\dfrac{2xv}{x+v}<2x$ for every $v>0$.)''',
'Distance, rate, and time|Averages and weighted averages|Harmonic mean',3,
note='The posted question has no finite answer; the record asks the question as stated and the solution shows it is impossible.')

# ---------------- 1759881 competition P3 (cookies)
b.add(1759881,3,r'''At Central Middle School the $108$ students who take the AMC 8 meet in the evening to talk about problems and eat an average of two cookies apiece. Walter and Gretel are baking Bonnie's Best Bar Cookies. Their recipe, which makes a pan of $15$ cookies, lists: $1\dfrac12$ cups of flour, $2$ eggs, $3$ tablespoons of butter, $\dfrac34$ cup of sugar and $1$ package of chocolate drops. They will make only full recipes, not partial recipes. Walter can buy eggs only by the half-dozen. How many half-dozens should he buy to make enough cookies? (Some eggs and some cookies may be left over.)
\[
\textbf{(A)}\ 1\qquad\textbf{(B)}\ 2\qquad\textbf{(C)}\ 5\qquad\textbf{(D)}\ 7\qquad\textbf{(E)}\ 15
\]''',
r'''They need $108\cdot2=216$ cookies. Since $14\cdot15=210<216\le225=15\cdot15$, they must make $15$ recipes, using $15\cdot2=30$ eggs. That is exactly $\dfrac{30}{6}=5$ half-dozens: $\boxed{\textbf{(C)}\ 5}$.''',
'Whole-number operations|Rates|Floor and ceiling functions',2,
note='P3 of a user-run competition, adapted from the AMC 8 cookie problems (without the attendance change of the original). P1 and P2 depend on missing figures and are not used.')

# ---------------- 1759676 handbook warm-up 11
fig=r'''pair A=4*dir(0),B=4*dir(60),C=4*dir(120),D=4*dir(180),Ep=4*dir(240),F=4*dir(300);
pair K=(C+D)/2;
draw(A--B--C--D--Ep--F--cycle,linewidth(0.9));
draw(A--K,red+linewidth(0.9));
draw(K--(K.x,0),dashed);draw(A--D,dashed);
pair H=(K.x,0);
draw((H+(0.3,0))--(H+(0.3,0.3))--(H+(0,0.3)),linewidth(0.4));
dot(K);
label("$A$",A,E);label("$B$",B,NE);label("$C$",C,NW);label("$D$",D,W);label("$E$",Ep,SW);label("$F$",F,SE);
label("$K$",K,NW);label("$H$",H,S);'''
b.add(1759676,136,r'''Regular hexagon $ABCDEF$ has side length $4$ cm. Point $K$ is the midpoint of side $CD$. What is the length of $AK$? Express your answer in simplest radical form.''',
r'''Place the centre at the origin with $A=(4,0)$; then $C=(-2,2\sqrt3)$ and $D=(-4,0)$, so $K=(-3,\sqrt3)$. Let $H=(-3,0)$ be the foot of the perpendicular from $K$ to the long diagonal $AD$.
'''+asy(fig,'5.5cm')+r'''
In right triangle $AHK$, $AH=4-(-3)=7$ and $HK=\sqrt3$, so
\[
AK=\sqrt{7^2+(\sqrt3)^2}=\sqrt{52}=\boxed{2\sqrt{13}}\text{ cm}.
\]''',
'Regular polygons|Midpoints|Pythagorean theorem|Coordinate geometry',3)
b.add(1759676,137,r'''At every lunch, three friends share their cheesy crackers but agree not to eat them until they all have the same number. At the first lunch, Axel gives Ben and Chloe as many crackers as they each already have. At the second lunch, Ben gives Axel and Chloe as many crackers as they each already have. At the third lunch, Chloe gives Axel and Ben as many crackers as they each already have, after which they each have $8$ crackers, so they eat them. How many crackers did Axel start with?''',
r'''Work backwards; each gift doubles the receivers' amounts.
\begin{itemize}
\item After lunch 3: $(A,B,C)=(8,8,8)$. Before Chloe gave: Axel and Ben had half, $4$ each, and Chloe had $8+4+4=16$: $(4,4,16)$.
\item Before Ben gave: Axel $2$, Chloe $8$, Ben $4+2+8=14$: $(2,14,8)$.
\item Before Axel gave: Ben $7$, Chloe $4$, Axel $2+7+4=13$: $(13,7,4)$.
\end{itemize}
Axel started with $\boxed{13}$ crackers. Check: $(13,7,4)\to(2,14,8)\to(4,4,16)\to(8,8,8)$.''',
'Working backwards|Process simulation',2,
note='"Bem" in the post is a typo for Ben.')

# ---------------- 1705149 factors of 400
b.add(1705149,1,r'''Find the total number of positive whole-number factors of $400$.''',
r'''$400=2^4\cdot5^2$, so a factor is $2^a5^b$ with $0\le a\le4$ and $0\le b\le2$. There are $(4+1)(2+1)=\boxed{15}$ factors.''',
'Divisor counting|Prime factorisation',1,
note='P1 of a number theory marathon; only P1 is in the post.')

# ---------------- 1758550 self-referential
b.add(1758550,1,r'''The answer to this problem is a positive number $x$ such that the cube of $x$ minus the square of $x$ equals $x$. Find $x$.''',
r'''We need $x^3-x^2=x$ with $x>0$. Dividing by $x$: $x^2-x-1=0$, so $x=\dfrac{1\pm\sqrt5}{2}$, and the positive root is $\boxed{\dfrac{1+\sqrt5}{2}}$.

(With the other order, square minus cube, $x^2-x^3=x$ gives $x^2-x+1=0$, which has no real roots; so ``the difference'' must mean cube minus square.)''',
'Quadratic equations|Polynomials',2,
note='The post asks for the positive answer that equals "the difference between the square and the cube of the answer". Square minus cube has no positive solution, so the difference is taken as cube minus square, giving the golden ratio.')

# ---------------- 1758680 1..9 around a circle
b.add(1758680,1,r'''Can the numbers $1,2,3,\dots,9$ be arranged around a circle so that the sum of any two neighbours is never divisible by $3$, by $5$ or by $7$?''',
r'''\textbf{Yes.} Call two numbers \emph{compatible} if their sum is divisible by none of $3,5,7$. Listing the compatible partners of each number:
\[
\begin{array}{c|ccccccccc}
k&1&2&3&4&5&6&7&8&9\\\hline
\text{partners}&3,7&6,9&1,5,8&7,9&3,6,8&2,5,7&1,4,6,9&3,5,9&2,4,7,8
\end{array}
\]
Each of $1$, $2$, $4$ has only two partners, which must therefore be its two neighbours: $3$--$1$--$7$, $6$--$2$--$9$ and $7$--$4$--$9$. These link up into the chain $3,1,7,4,9,2,6$. Now $7$ already has its two neighbours $1$ and $4$, so $6$'s other neighbour must be $5$, and the remaining number $8$ goes between $5$ and $3$. This gives the circle
\[
\boxed{1,\ 7,\ 4,\ 9,\ 2,\ 6,\ 5,\ 8,\ 3}
\]
with neighbour sums $8,11,13,11,8,11,13,11,4$ (the last is $3+1$), none divisible by $3$, $5$ or $7$. The argument also shows this arrangement is the only one up to rotation and reflection.''',
'Logical deduction|Construction|Divisibility|Graph theory',4,
note='Verified by computer: the arrangement is unique up to rotation and reflection.')

# ---------------- 1759512 Fibonacci over powers of 2
b.add(1759512,1,r'''Evaluate
\[
\dfrac12+\dfrac14+\dfrac28+\dfrac{3}{16}+\dfrac{5}{32}+\dfrac{8}{64}+\dfrac{13}{128}+\dfrac{21}{256}+\dfrac{34}{512}+\cdots,
\]
where the numerators are the Fibonacci numbers $F_1=F_2=1$, $F_{n+1}=F_n+F_{n-1}$ and the $n$-th term is $\dfrac{F_n}{2^n}$.''',
r'''By induction $F_n\le\left(\dfrac53\right)^n$ (true for $n=1,2$, and $F_{n+1}=F_n+F_{n-1}\le\left(\dfrac53\right)^{n-1}\cdot\dfrac83\le\left(\dfrac53\right)^{n+1}$ because $\dfrac83=\dfrac{24}{9}<\dfrac{25}{9}$), so the $n$-th term is at most $\left(\dfrac56\right)^n$ and the series converges. Let $S$ be its sum. Then
\[
S-\dfrac S2-\dfrac S4=\sum_{n\ge1}\dfrac{F_n}{2^n}-\sum_{n\ge2}\dfrac{F_{n-1}}{2^n}-\sum_{n\ge3}\dfrac{F_{n-2}}{2^n}=\dfrac{F_1}{2}+\dfrac{F_2-F_1}{4}+\sum_{n\ge3}\dfrac{F_n-F_{n-1}-F_{n-2}}{2^n}=\dfrac12+0+0=\dfrac12 .
\]
So $\dfrac S4=\dfrac12$ and $S=\boxed{2}$.''',
'Fibonacci sequence|Sequences and series|Recurrence relations',4)

# ---------------- 1759213 subtraction of rational expressions
b.add(1759213,1,r'''Perform the subtraction and simplify:
\[
\dfrac{x}{1-x^3}-\dfrac{x}{1+x+x^2}.
\]''',
r'''Since $1-x^3=(1-x)(1+x+x^2)$, use the common denominator $1-x^3$:
\[
\dfrac{x}{1-x^3}-\dfrac{x(1-x)}{1-x^3}=\dfrac{x-x+x^2}{1-x^3}=\boxed{\dfrac{x^2}{1-x^3}}\qquad(x\ne1).
\]''',
'Sum and difference of cubes|Algebraic manipulation|Factoring',2,
note='The post writes "x/1-x^3 - x/1+x+x^2", read as x/(1 - x^3) - x/(1 + x + x^2).')

# ---------------- 1759331 point on line equidistant
fig=r'''pair A=(-6,0),B=(0,4),P=(-29/7,26/7),M=(A+B)/2;
draw((-8,0)--(2,0),Arrow(4));draw((0,-1)--(0,6),Arrow(4));
draw((-6.6,-1.2)--(-2.9,6.2),linewidth(0.9));
draw((-29/7-0.9*1.4,26/7+0.9*2.1)--(M+1.4*(2,-3)),dashed+blue);
draw(A--B,gray+dashed);
draw(P--A,red+linewidth(0.8));draw(P--B,red+linewidth(0.8));
dot(A);dot(B);dot(P);
label("$A(-6,0)$",A,SE);label("$B(0,4)$",B,E);label("$P$",P,W);
label("$y=2x+12$",(-2.9,6.2),W);
label("$x$",(2,0),S);label("$y$",(0,6),W);'''
b.add(1759331,1,r'''A line with slope $2$ passes through $A(-6,0)$. Let $B=(0,4)$. Find the coordinates of the point $P$ on the line such that $PA=PB$.''',
r'''The line is $y=2(x+6)=2x+12$. The points equidistant from $A$ and $B$ form the perpendicular bisector of $AB$ (dashed, blue). Its midpoint is $(-3,2)$ and $\overrightarrow{AB}=(6,4)$, so the bisector is $6(x+3)+4(y-2)=0$, i.e.\ $3x+2y+5=0$.
'''+asy(fig,'6cm')+r'''
Substituting $y=2x+12$: $3x+4x+24+5=0$, so $x=-\dfrac{29}{7}$ and $y=-\dfrac{58}{7}+12=\dfrac{26}{7}$. Thus $P=\boxed{\left(-\dfrac{29}{7},\dfrac{26}{7}\right)}$. Check: $PA^2=\left(\dfrac{13}{7}\right)^2+\left(\dfrac{26}{7}\right)^2=\dfrac{845}{49}$ and $PB^2=\left(\dfrac{29}{7}\right)^2+\left(\dfrac{2}{7}\right)^2=\dfrac{845}{49}$.''',
'Coordinate geometry|Perpendicular bisectors|Linear equations|Distance formula',3)

# ---------------- 1759297 minimum 8x^3+36x+54/x+27/x^3
b.add(1759297,1,r'''What is the minimum value of $8x^3+36x+\dfrac{54}{x}+\dfrac{27}{x^3}$ over positive real numbers $x$?''',
r'''The expression is a perfect cube:
\[
\left(2x+\dfrac3x\right)^3=8x^3+3(2x)^2\cdot\dfrac3x+3(2x)\cdot\dfrac{9}{x^2}+\dfrac{27}{x^3}=8x^3+36x+\dfrac{54}{x}+\dfrac{27}{x^3}.
\]
By AM-GM, $2x+\dfrac3x\ge2\sqrt{6}$, with equality when $2x=\dfrac3x$, i.e.\ $x=\sqrt{\dfrac32}$. Since $t\mapsto t^3$ is increasing for $t>0$, the minimum is $\left(2\sqrt6\right)^3=\boxed{48\sqrt6}$.''',
'AM-GM inequality|Algebraic expressions and identities|Maxima and minima',4)

# ---------------- 1759282 odd number of factors up to 2000
b.add(1759282,1,r'''How many positive integers less than or equal to $2000$ have an odd number of positive factors?''',
r'''Factors of $n$ pair up as $d$ and $\dfrac nd$; the only unpaired factor occurs when $d=\dfrac nd$, i.e.\ $d=\sqrt n$. So $n$ has an odd number of factors exactly when $n$ is a perfect square. Since $44^2=1936\le2000<2025=45^2$, the squares $1^2,\dots,44^2$ qualify: $\boxed{44}$ numbers.''',
'Divisor counting|Perfect squares|Pairing and grouping',2,
source=src('MATHCOUNTS',2012,'Chapter',6,rnd='Target'))

# ---------------- 1759220 minimise AP+BP
fig=r'''pair A=(1,2),B=(3,4),A1=(1,-2),P=(5/3,0);
draw((-0.5,0)--(4.5,0),Arrow(4));draw((0,-2.6)--(0,5),Arrow(4));
draw((-0.5,0.5)--(4,5),linewidth(0.8));
draw(A--P--B,red+linewidth(0.9));
draw(A1--P,red+dashed);draw(A--A1,gray+dotted);
dot(A);dot(B);dot(A1);dot(P);
label("$A(1,2)$",A,W);label("$B(3,4)$",B,SE);label("$A'(1,-2)$",A1,E);label("$P$",P,2*dir(-60));
label("$y=x+1$",(4,5),E);label("$x$",(4.5,0),S);label("$y$",(0,5),W);'''
b.add(1759220,1,r'''The points $A(1,2)$ and $B(3,b)$ lie on the graph of $y=x+a$, where $a$ is a constant. A point $P$ is chosen on the $x$-axis so that $AP+BP$ is as small as possible. Find the coordinates of $P$.''',
r'''From $2=1+a$ we get $a=1$, so the line is $y=x+1$ and $b=4$. Reflect $A$ in the $x$-axis to $A'(1,-2)$. For every $P$ on the $x$-axis, $AP=A'P$, so $AP+BP=A'P+PB\ge A'B$, with equality exactly when $P$ lies on segment $A'B$.
'''+asy(fig,'5.5cm')+r'''
Line $A'B$ has slope $\dfrac{4-(-2)}{3-1}=3$, so it is $y=3(x-1)-2$, which meets $y=0$ at $x=\dfrac53$. Hence $P=\boxed{\left(\dfrac53,0\right)}$, and the minimum of $AP+BP$ is $A'B=\sqrt{4+36}=2\sqrt{10}$.''',
'Reflections|Coordinate geometry|Linear equations|Maxima and minima',3,
note='From a Korean grade-8 book (per the post).')

# ---------------- 1759193 seven consecutive Fridays
b.add(1759193,1,r'''If Friday the 13th occurs in a month, then the sum of the calendar dates of the Fridays in that month is $6+13+20+27=66$. What is the largest possible sum of the calendar dates of seven consecutive Fridays in a year?''',
r'''Split the seven consecutive Fridays into blocks of Fridays in the same month. Inside a block the dates go up by $7$. Months have at most $31$ days, so a block has at most $5$ Fridays, and seven Fridays span at least two months.

\textbf{First block.} If it has $i$ Fridays, its dates end at most at $31$, so its sum is at most $31+24+\cdots$ ($i$ terms): $F(1)=31$, $F(2)=55$, $F(3)=72$, $F(4)=82$, $F(5)=85$.

\textbf{Later blocks} start at the first Friday of a month, date at most $7$, so a block of $j$ Fridays has dates at most $7,14,\dots$ and at most $31$: $G(1)=7$, $G(2)=21$, $G(3)=42$, $G(4)=70$, $G(5)=3+10+17+24+31=85$ (a fifth Friday needs the first one on day $3$ or earlier). Since $G(j)+G(j')\le G(j+j')$ whenever $j+j'\le5$, merging later blocks only increases the bound.

\textbf{Cases} for the size $i$ of the first block:
\begin{itemize}
\item $i=1$: the other $6$ Fridays need at least two later blocks: at most $31+\max(G(5)+G(1),\,G(4)+G(2),\,G(3)+G(3))=31+92=123$.
\item $i=2$: at most $55+G(5)=140$.
\item $i=3$: at most $72+G(4)=142$.
\item $i=4$: at most $82+G(3)=124$.
\item $i=5$: at most $85+G(2)=106$.
\end{itemize}
So the sum is at most $142$, and $142$ is attained when a $31$-day month has Fridays on the $17$th, $24$th and $31$st: the next Fridays are the $7$th, $14$th, $21$st and $28$th of the following month, and
\[
17+24+31+7+14+21+28=\boxed{142}.
\]
(For example, the Fridays from July 17 to August 28, 2015.)''',
'Calendar and clock problems|Bounding and extremal cases|Casework',4,
note='The poster\'s 130 is not the maximum; the stated answer 142 is correct and was confirmed by checking actual calendars.')

# ---------------- 1759180 dog park logic (alias)
b.add(1759180,1,r'''Three dogs (a Dalmatian, a Schnauzer and a Poodle) arrived at a dog park at three different times with their three owners, a 6th grader, a 7th grader and an 8th grader, using three different leash colours (red, green and blue). The Dalmatian arrived next after the Schnauzer. The dog with the red leash is owned by the 7th grader. The Poodle was not the first to arrive. The Schnauzer does not use a green leash. If the 6th grader owns the Dalmatian, then the Poodle's leash is blue. The 8th grader arrived first. What is the product of the grade levels of the student who arrived second, the student who owns the Poodle and the student who uses the green leash?''',
r'''The order must be Schnauzer, Dalmatian, Poodle (the Poodle is not first and the Dalmatian follows the Schnauzer). The 8th grader, first, owns the Schnauzer, whose leash is neither red (the 7th grader's) nor green, so it is blue. Then the Poodle's leash is not blue, so the 6th grader does not own the Dalmatian: the 7th grader owns the Dalmatian (red leash) and the 6th grader the Poodle (green leash). The product is $7\cdot6\cdot6=\boxed{252}$.''',
'Logical deduction|Casework',2,
source=src('MATHCOUNTS',2018,'School',5,rnd='Target'),
note='Repeat of an earlier record (aliased).')

# ---------------- 1758725 Xmas problems (made self-contained)
b.add(1758725,1,r'''Santa has $6$ identical dolls and $6$ identical trucks to hand out to $3$ brothers and $1$ sister. Each child must receive the same number of toys. In how many ways can Santa distribute the toys?''',
r'''Each child gets $3$ toys, so a distribution is determined by the numbers of dolls $d_1,\dots,d_4$ the children get, with $0\le d_i\le3$ and $d_1+\cdots+d_4=6$ (the rest of each child's toys are trucks). Without the upper bound there are $\dbinom{9}{3}=84$ solutions; those with some $d_i\ge4$ number $4\dbinom53=40$ (two values $\ge4$ are impossible). So there are $84-40=\boxed{44}$ ways.''',
'Distributions and integer solutions|Stars and bars|Complementary counting',3)
b.add(1758725,2,r'''If I eat none of the cookies I baked, each of my $6$ guests gets the same number of cookies with none left over. If instead the $7$ of us share them equally, $3$ cookies are left over. What is the least number of cookies I could have baked?''',
r'''We need a positive $N$ with $N\equiv0\pmod6$ and $N\equiv3\pmod7$. Checking multiples of $6$: $6,12,18,24$ leave remainders $6,5,4,3$ modulo $7$. So the least is $\boxed{24}$.''',
'Remainders and congruences|Chinese remainder theorem',2)
b.add(1758725,3,r'''Four elves each throw a cupcake at one of the other three elves, chosen independently and uniformly at random. The probability that some two elves throw their cupcakes at each other is $\dfrac mn$ in lowest terms. Find $m+n$.''',
r'''There are $3^4=81$ equally likely outcomes. For a given pair of elves, the outcomes where they throw at each other number $3^2=9$ (the other two elves are free). There are $\dbinom42=6$ pairs. Two pairs can both be mutual only if they are disjoint, and then all four throws are determined: $3$ such outcomes (one for each way to split the elves into two pairs). By inclusion--exclusion the number of outcomes with a mutual pair is $6\cdot9-3=51$, so the probability is $\dfrac{51}{81}=\dfrac{17}{27}$ and $m+n=\boxed{44}$.''',
'Probability|Sets and inclusion–exclusion|Counting principles',4)
b.add(1758725,4,r'''Ms.\ Bindergarten lines up all of her students in rows every day, with the same number of students in each row and no student left over. On day $1$ there are $44$ students in each row, and on day $2$ there are $24$ students in each row, and she has the least number of students for which this is possible. If she uses a different number of students per row every day, for how many days in total (including days $1$ and $2$) can she do this without repeating a row length?''',
r'''The number of students is a common multiple of $44=2^2\cdot11$ and $24=2^3\cdot3$, and the least one is $\operatorname{lcm}(44,24)=2^3\cdot3\cdot11=264$. A row length works exactly when it divides $264$, so the possible row lengths are the divisors of $264$, of which there are $(3+1)(1+1)(1+1)=16$ (including a single row of $264$ and rows of $1$). She can go $\boxed{16}$ days.''',
'HCF and LCM|Divisor counting|Prime factorisation',2,
note='Problem 4 of a chain where a_1 = 44 and a_2 = 24 are the answers of problems 1 and 2; the values are substituted. The question is read as the total number of days, including days 1 and 2 (the intended answer 16).')
b.add(1758725,5,r'''Dasher, Dancer and Prancer run laps on a circular track, starting together. Dasher takes $44$ seconds per lap, Dancer $16$ seconds and Prancer $24$ seconds. After how many seconds will all three first be together at the start again?''',
r'''They are all at the start at times that are common multiples of $44=2^2\cdot11$, $16=2^4$ and $24=2^3\cdot3$. The first such time is $\operatorname{lcm}(44,16,24)=2^4\cdot3\cdot11=\boxed{528}$ seconds.''',
'HCF and LCM|Prime factorisation',2,
note='The lap times a_1 = 44, a_4 = 16 and a_2 = 24 are substituted. "Meet again" is read as all being at the starting line together.')
b.add(1758725,6,r'''Ebenezer Scrooge will take a whole number of dollars, less than $1000$, to give away outside the church. He wants to give all of it away with every homeless person receiving the same whole number of dollars, but he does not know how many people will come. To make this possible for as many different numbers of people as possible, how many dollars should he take?''',
r'''An amount $N$ can be shared equally among $k$ people exactly when $k\mid N$, so we want the $N<1000$ with the most divisors. If $N=2^a3^b5^c7^d\cdots$, the number of divisors is $(a+1)(b+1)(c+1)\cdots$, and for a given exponent pattern the smallest $N$ uses the smallest primes with exponents in decreasing order. Below $1000$:
\begin{itemize}
\item Five or more distinct primes give $N\ge2\cdot3\cdot5\cdot7\cdot11=2310$: impossible.
\item Four distinct primes: $32$ or more divisors needs an exponent at least $3$ (as $2^4=16<32$) or two exponents at least $2$. The smallest such numbers are $2^3\cdot3\cdot5\cdot7=840$ ($32$ divisors) and $2^2\cdot3^2\cdot5\cdot7=1260$; every other choice is larger than $840$ and in fact exceeds $1000$ (e.g.\ $2\cdot3^3\cdot5\cdot7=1890$, $2^3\cdot3\cdot5\cdot11=1320$).
\item At most three primes: $32$ or more divisors needs exponent patterns such as $(3,3,1)$, $(7,1,1)$, $(5,2,1)$, $(3,2,2)$ or $(7,3)$, whose smallest values $1080$, $1920$, $1440$, $1800$, $3456$ all exceed $1000$; patterns with fewer divisors, such as $720=2^4\cdot3^2\cdot5$ ($30$ divisors), do not reach $32$.
\end{itemize}
So $840$ is the unique number below $1000$ with the maximum number, $32$, of divisors. So he should take $\boxed{840}$ dollars.''',
'Divisor counting|Prime factorisation|Bounding and extremal cases',4,
note='Read as: choose N < 1000 with the largest number of divisors (840, with 32 divisors; checked by computer for all N < 1000).')

# ---------------- 1759073 tunnel
b.add(1759073,1,r'''I am jogging in a train tunnel. When I am $\dfrac25$ of the way through it, I hear a train approaching the tunnel entrance behind me at $60$ mph. Whether I run back towards the entrance or ahead towards the exit, I will reach that end of the tunnel at exactly the same moment as the train. What is my speed, in mph? (I run at a constant speed.)''',
r'''Let the tunnel have length $L$. If I run back, I cover $\dfrac25L$ and meet the train exactly at the entrance. If instead I run ahead, in that same time I cover $\dfrac25L$ and reach the point $\dfrac45L$ of the tunnel just as the train arrives at the entrance. From then on, I cover the remaining $\dfrac15L$ while the train covers the whole tunnel $L$, and we arrive together at the exit. So my speed is $\dfrac15$ of the train's: $\dfrac{60}{5}=\boxed{12}$ mph.''',
'Distance, rate, and time|Ratios, proportions, and variation',3)

b.save()
