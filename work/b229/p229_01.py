from qb import *
b=Bank('p229_01')

# ---------------- 1746368 trees
b.add(1746368,1,r'''A contractor plans to plant $1800$ trees in a certain number of days, planting the same number each day. During the first third of the planned time, $120$ fewer trees than planned were planted in total. To meet the target, every remaining day $20$ more trees than the planned daily number were planted, and the work was finished one day earlier than planned. How many trees did the contractor plan to plant each day?''',
r'''Let the plan be $d$ days at $r$ trees per day, so $rd=1800$. In the first $\dfrac d3$ days the planned amount was $\dfrac{rd}{3}=600$, so $600-120=480$ trees were planted, leaving $1800-480=1320$. These were planted at $r+20$ per day in the remaining $\dfrac{2d}{3}-1$ days:
\[
(r+20)\left(\dfrac{2d}{3}-1\right)=1320 .
\]
Expanding and using $\dfrac{2rd}{3}=1200$ gives $1200-r+\dfrac{40d}{3}-20=1320$, so $\dfrac{40d}{3}-r=140$. Substituting $r=\dfrac{1800}{d}$ and multiplying by $3d$:
\[
40d^2-420d-5400=0\iff 2d^2-21d-270=0\iff (d-18)(2d+15)=0 .
\]
So $d=18$ and $r=\boxed{100}$ trees per day. Check: $6$ days at $80$ give $480$; then $1320$ trees at $120$ per day take $11$ days, a total of $17=18-1$ days.''',
'Work and rates|Quadratic equations|Equations and systems of equations',3,
note='Wording tidied ("plants could be less planted" read as 120 fewer trees in total during the first third of the planned time). Answer 100 confirmed.')

# ---------------- 1742979 MATHCOUNTS 2017 State 16, 17, 21
b.add(1742979,16,r'''If $x$ and $y$ are integers such that $(x-3)^2+(y+4)^2=25$, what is the greatest possible value of $x^2+y^2$?''',
r'''Expanding the condition gives $x^2-6x+9+y^2+8y+16=25$, that is,
\[
x^2+y^2=6x-8y .
\]
Put $u=x-3$, $v=y+4$, so $u^2+v^2=25$ and
\[
x^2+y^2=6(u+3)-8(v-4)=6u-8v+50 .
\]
By the Cauchy-Schwarz inequality, $6u-8v\le\sqrt{6^2+8^2}\,\sqrt{u^2+v^2}=10\cdot5=50$, with equality when $(u,v)$ is a positive multiple of $(6,-8)$, i.e.\ $(u,v)=(3,-4)$. This is an integer point, giving $(x,y)=(6,-8)$. So the greatest value is $36+64=\boxed{100}$.

(Without the inequality one can also list the twelve integer solutions of $u^2+v^2=25$, namely $(\pm5,0),(0,\pm5),(\pm3,\pm4),(\pm4,\pm3)$, and evaluate $6u-8v$; the largest value is $50$ at $(3,-4)$. Geometrically, $(6,-8)$ is the point of the circle diametrically opposite the origin, which lies on the circle.)''',
'Diophantine equations|Maxima and minima|Cauchy-Schwarz inequality',3,source=src('MATHCOUNTS',2017,'State',16),
note='The poster asks for a method without geometry; the solution is algebraic (expansion and Cauchy-Schwarz, or listing the 12 lattice points).')
b.add(1742979,17,r'''A positive integer $q$ is the product of a prime number and a perfect square. Additionally, $q$ is the product of a different prime number and a perfect cube. What is the least possible value of $q$?''',
r'''Write $q=pa^2=rb^3$ with primes $p\ne r$. For a prime $s\ne p,r$ the exponent of $s$ in $q$ is even and a multiple of $3$, so it is a multiple of $6$; such primes only make $q$ larger, so take $q=p^{\alpha}r^{\beta}$. From $q=pa^2$: $\alpha$ is odd and $\beta$ is even. From $q=rb^3$: $\alpha\equiv0$ and $\beta\equiv1\pmod 3$. The least choices are $\alpha=3$, $\beta=4$, so $q=p^3r^4$. To make this small, $r=2$ and $p=3$: $q=27\cdot16=\boxed{432}$ (the other assignment gives $8\cdot81=648$). Check: $432=3\cdot12^2=2\cdot6^3$.''',
'Prime factorisation|Perfect squares|Perfect cubes',3,source=src('MATHCOUNTS',2017,'State',17))
b.add(1742979,21,r'''The number $40{,}321$ is a five-digit positive integer that uses five consecutive digits, although not necessarily in order. How many such five-digit positive integers are there?''',
r'''The possible sets of five consecutive digits are $\{0,1,2,3,4\},\{1,2,3,4,5\},\dots,\{5,6,7,8,9\}$, six sets in all. For each of the five sets without $0$, every arrangement is a five-digit number: $5!=120$ numbers each. For $\{0,1,2,3,4\}$ the leading digit cannot be $0$: $5!-4!=96$ numbers. The total is $5\cdot120+96=\boxed{696}$.''',
'Permutations|Complementary counting|Digit problems',2,source=src('MATHCOUNTS',2017,'State',21))

# ---------------- 1745995 rectangle PQRS
fig=r'''pair P=(-12.5,0),Q=(3.5,12),R=(12.5,0),T=(-3.5,-12);
draw(P--Q--R--T--cycle,linewidth(0.9));
draw(P--R,dashed+gray);draw(Q--T,dashed+gray);
dot(P);dot(Q);dot(R);dot(T);
label("$P$",P,W);label("$Q$",Q,N);label("$R$",R,E);label("$S$",T,S);
label("$20$",(P+Q)/2+0.5*dir(127),dir(127));label("$15$",(Q+R)/2+0.5*dir(37),dir(37));
draw((-12.5,-17)--(12.5,-17),Arrows(5));draw((-12.5,-1.5)--(-12.5,-18),dotted);draw((12.5,-1.5)--(12.5,-18),dotted);
label("$25$",(0,-17),S);
draw((-17,-12)--(-17,12),Arrows(5));draw((-5,-12)--(-18,-12),dotted);draw((2,12)--(-18,12),dotted);
label("$24$",(-17,0),W);'''
b.add(1745995,1,r'''Rectangle $PQRS$ is drawn on a coordinate plane. The $y$-coordinate of $Q$ is $24$ units greater than the $y$-coordinate of $S$, the $x$-coordinate of $R$ is $25$ units greater than the $x$-coordinate of $P$, and the $y$-coordinate of $P$ is equal to the $y$-coordinate of $R$. What is the perimeter of rectangle $PQRS$?''',
r'''$P$ and $R$ are opposite vertices, and they have the same $y$-coordinate, so the diagonal $PR$ is horizontal with length $25$. The diagonals of a rectangle are equal, so $QS=25$; its vertical component is $24$, so its horizontal component is $\sqrt{25^2-24^2}=7$. Place the centre (the common midpoint of the diagonals) at the origin: $P=(-12.5,0)$, $R=(12.5,0)$, $Q=(3.5,12)$, $S=(-3.5,-12)$.
'''+asy(fig,'6.5cm')+r'''
Then
\[
PQ=\sqrt{16^2+12^2}=20,\qquad QR=\sqrt{9^2+12^2}=15,
\]
and $\overrightarrow{PQ}\cdot\overrightarrow{QR}=16\cdot9+12\cdot(-12)=0$, as it must be. (Taking $Q=(-3.5,12)$, $S=(3.5,-12)$ instead just swaps the two side lengths.) The perimeter is $2(20+15)=\boxed{70}$.''',
'Rectangles|Coordinate geometry|Distance formula|Pythagorean theorem|Lengths, perimeter, and area',4,
note='Warm-Up 13 Problem 158 (MATHCOUNTS handbook). The two placements of Q give the same perimeter.')

# ---------------- 1745992 circles; area = perimeter
b.add(1745992,1,r'''What is the maximum number of intersection points when $6$ distinct circles are drawn in a plane?''',
r'''Two distinct circles meet in at most $2$ points, so $6$ circles have at most $2\dbinom62=30$ intersection points. This is attained: take six circles of radius $1$ whose centres are distinct points on a segment of length less than $1$. Any two of them meet in exactly two points, symmetric about the line of centres, and no point lies on three of the circles, because no point is at distance $1$ from three distinct collinear points. So the maximum is $\boxed{30}$.''',
'Counting intersections|Combinations',2)
fig=r'''pair C=(0,0),B=(8,0),A=(0,6),I=(2,2);
draw(A--B--C--cycle,linewidth(0.9));
draw(circle(I,2),blue+linewidth(0.8));
draw((0,0.4)--(0.4,0.4)--(0.4,0));
dot(I);draw(I--(2,0),dashed);label("$r$",(2,1),E);
label("$A$",A,N);label("$B$",B,E);label("$C$",C,SW);label("$I$",I,NE);
label("$6$",(0,3),W);label("$8$",(4,0),S);label("$10$",(4,3),NE);'''
b.add(1745992,2,r'''A triangle has its area numerically equal to its perimeter. What is the radius of the circle inscribed in the triangle?''',
r'''Let the inradius be $r$, the incentre $I$, and the perimeter $p$. Joining $I$ to the three vertices splits the triangle into three triangles whose bases are the sides and whose heights are all $r$, so the area is $\dfrac12 r(a+b+c)=\dfrac{rp}{2}$. The condition $\dfrac{rp}{2}=p$ gives $r=\boxed{2}$. For example, the $6$-$8$-$10$ right triangle has area $24$ and perimeter $24$, and its inradius is $2$:
'''+asy(fig,'5cm'),
'Incircles and incentres|Triangles|Lengths, perimeter, and area',2)

# ---------------- 1676476 Breaking Math II
b.add(1676476,1,r'''A student writes
\[
-1=\sqrt{-1}\cdot\sqrt{-1}=\sqrt{(-1)(-1)}=\sqrt{1}=1
\]
and concludes that a positive number can equal its negation. Find the error, and prove that no positive number equals its negation.''',
r'''The first equality is correct: $\sqrt{-1}$ denotes $i$, and $i\cdot i=-1$. The error is the step $\sqrt{-1}\cdot\sqrt{-1}=\sqrt{(-1)(-1)}$. The rule $\sqrt a\cdot\sqrt b=\sqrt{ab}$ is proved only for $a,b\ge0$: both sides are then nonnegative and have the same square $ab$. For negative numbers it fails, exactly as here: $\sqrt{-1}\cdot\sqrt{-1}=i^2=-1$, while $\sqrt{(-1)(-1)}=\sqrt1=1$. (Squaring both sides only shows that the two sides are equal or opposite.)

If $a=-a$, then $2a=0$, so $a=0$. Hence no positive number (indeed no nonzero number) equals its negation. $\blacksquare$''',
'Complex numbers|Radicals',2,
note='The post presents the fallacy and asks the reader to find the mistake and prove that a positive number cannot equal its negation.')

# ---------------- 1746150 crossed ladders
fig=r'''pair v=unit((0.35,1));
pair A=(0,0),B=(7,0),C=A+3*v,D=B+5*v;
pair Ep=extension(C,B,D,A);pair F=extension(Ep,Ep-v,A,B);
draw(A--B,linewidth(0.9));draw(A--C,linewidth(0.9));draw(B--D,linewidth(0.9));
draw(C--B);draw(D--A);draw(Ep--F,blue+linewidth(0.9));
dot(Ep);dot(F);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NW);label("$D$",D,NE);label("$E$",Ep,N);label("$F$",F,S);
label("$a$",(A+C)/2,W);label("$b$",(B+D)/2,E);label("$c$",(Ep+F)/2,W,blue);'''
b.add(1746150,1,r'''Segments $AC$ and $BD$ are parallel and lie on the same side of line $AB$, with $AC=a$ and $BD=b$. Lines $CB$ and $DA$ meet at $E$, and the line through $E$ parallel to $AC$ meets $AB$ at $F$.
\begin{enumerate}
\item[(a)] Prove that $EF=\dfrac{ab}{a+b}$, that is, $\dfrac1{EF}=\dfrac1a+\dfrac1b$.
\item[(b)] One painter can paint a fence in $x$ hours and another in $y$ hours. How long do they take working together? Explain how the answer corresponds to part (a).
\end{enumerate}''',
r'''Let $EF=c$.
'''+asy(fig,'6cm')+r'''
\textbf{(a)} Since $EF\parallel AC$, triangles $BFE$ and $BAC$ are similar (common angle at $B$, corresponding angles equal), so $\dfrac ca=\dfrac{BF}{BA}$. Since $EF\parallel BD$, triangles $AFE$ and $ABD$ are similar, so $\dfrac cb=\dfrac{AF}{AB}$. Adding, and using $AF+FB=AB$ (the point $F$ lies between $A$ and $B$ because $E$ lies inside both segments $CB$ and $DA$),
\[
\dfrac ca+\dfrac cb=\dfrac{AF+FB}{AB}=1,\qquad\text{so}\qquad EF=c=\dfrac{1}{\dfrac1a+\dfrac1b}=\dfrac{ab}{a+b}. \qquad\blacksquare
\]

\textbf{(b)} The painters paint $\dfrac1x$ and $\dfrac1y$ of the fence per hour, so together $\dfrac1x+\dfrac1y$ per hour, and the job takes $\dfrac{1}{\dfrac1x+\dfrac1y}=\boxed{\dfrac{xy}{x+y}}$ hours. This is the same formula: in (a) the reciprocal of $EF$ is the sum of the reciprocals of $a$ and $b$, just as the combined time is the reciprocal of the sum of the reciprocal times. (Both quantities are half the harmonic mean of the two given numbers.)''',
'Parallel lines|Similarity|Triangles|Work and rates',3,
note='Discussion post ("Breaking Math IV") about the crossed-ladders configuration and the work-rate formula; turned into a proof plus the rate question. The unrelated remark "show 1^2=0" is ignored.')

# ---------------- 1745919 tangents and midpoints
fig=r'''pair O=(0,0),A=(3,0);real c=1/3,s=sqrt(8)/3;pair B=(c,s),C=(c,-s);
pair D=(A+B)/2,Ep=(A+C)/2;
draw(circle(O,1),linewidth(0.9));draw(A--B,linewidth(0.8));draw(A--C,linewidth(0.8));
draw(O--B,dashed);draw(O--C,dashed);draw(O--A,dotted);
draw((D.x,-1.45)--(D.x,1.45),blue+linewidth(0.8));draw(D--Ep,blue+linewidth(1.2));
dot(O);dot(A);dot(B);dot(C);dot(D);dot(Ep);
label("$O$",O,W);label("$A$",A,E);label("$B$",B,N);label("$C$",C,S);label("$D$",D,NE);label("$E$",Ep,SE);'''
b.add(1745919,1,r'''Point $A$ lies outside a circle with centre $O$. The tangents from $A$ touch the circle at $B$ and $C$. Let $D$ and $E$ be the midpoints of $AB$ and $AC$. Prove that the line $DE$ does not meet the circle.''',
r'''Let $r$ be the radius and, for a point $X$, let $p(X)=XO^2-r^2$ be its power with respect to the circle; $X$ lies outside the circle exactly when $p(X)>0$.
'''+asy(fig,'6cm')+r'''
Since $DB$ is tangent at $B$, $p(D)=DO^2-r^2=DB^2=DA^2$. Likewise $p(E)=EC^2=EA^2$. Consider $g(X)=XO^2-XA^2-r^2$. Writing $X=(x,y)$ in coordinates, the quadratic terms in $XO^2-XA^2$ cancel, so $g$ is a linear function of $x$ and $y$. It vanishes at $D$ and at $E$, hence on the whole line $DE$. So for every point $X$ of line $DE$,
\[
p(X)=XO^2-r^2=XA^2 .
\]
The point $A$ is not on line $DE$: this line is the midline of triangle $ABC$, parallel to $BC$ and halfway between $A$ and $BC$. So $XA>0$ and $p(X)>0$ for every $X$ on line $DE$, i.e.\ every point of the line (in particular of the segment $DE$) lies outside the circle. $\blacksquare$

(In the language of radical axes: line $DE$ is the radical axis of the circle and the point-circle $A$.)''',
'Circles|Tangents|Midpoints|Power of a point|Radical axis',4,
note='Proved for the whole line DE, which contains the segment.')

# ---------------- 1745976 multinomial
b.add(1745976,1,r'''What is the sum of the coefficients of $(6x+2y+4z)^4$?''',
r'''The sum of the coefficients of a polynomial is its value at $x=y=z=1$: $(6+2+4)^4=12^4=\boxed{20736}$.''',
'Binomial theorem|Polynomials',1)
b.add(1745976,2,r'''What is the coefficient of $x^2y z^3$ in $(3x+4y+2z)^6$?''',
r'''A term $x^2yz^3$ arises by choosing $3x$ from two of the six factors, $4y$ from one and $2z$ from three. The number of ways to choose which factors is $\dfrac{6!}{2!\,1!\,3!}=60$, and each choice contributes $3^2\cdot4\cdot2^3=288$. The coefficient is $60\cdot288=\boxed{17280}$.''',
'Binomial theorem|Multiset permutations',2,
note='The post asks for quick methods; the multinomial-coefficient method is shown.')

# ---------------- 1745924 group probability
b.add(1745924,1,r'''A class of $24$ students is split at random into eight groups of three. What is the probability that Alex, Bill and Cody are all put in the same group?''',
r'''Look at Alex's group. Its other two members are a uniformly random pair of the remaining $23$ students, and there are $\dbinom{23}{2}=253$ such pairs, of which exactly one is $\{\text{Bill},\text{Cody}\}$. The probability is $\boxed{\dfrac{1}{253}}$.''',
'Probability|Combinations',3)

# ---------------- 1745621 handbook problems
b.add(1745621,1,r'''Alvin plays mini-golf with four friends. The median and the unique mode of their five scores are both $10$, and the range of the scores is $16$. If the mean of the five scores is $15$, what is the sum of all possible values of the lowest score? (Scores are positive integers.)''',
r'''Let the sorted scores be $s_1\le s_2\le s_3\le s_4\le s_5$, with $s_3=10$, $s_5=s_1+16$ and $s_1+s_2+s_3+s_4+s_5=75$. Since $10$ is the mode, it occurs at least twice, so $s_2=10$ or $s_4=10$.

\textbf{Case $s_2=10$.} Then $s_1+s_4+s_5=55$, so $2s_1+s_4=39$. If $s_4=10$, then $2s_1=29$, impossible. So $s_4>10$ and $s_4=39-2s_1$.
\begin{itemize}
\item If $s_1<10$, the score $10$ occurs exactly twice, so $s_4\ne s_5$ for the mode to be unique: $10<39-2s_1<s_1+16$, i.e.\ $8\le s_1\le 14$, so $s_1\in\{8,9\}$, giving $8,10,10,23,24$ and $9,10,10,21,25$.
\item If $s_1=10$: $s_4=19$, $s_5=26$, giving $10,10,10,19,26$, where $10$ is the unique mode.
\end{itemize}

\textbf{Case $s_2<10$, $s_4=10$.} Then $s_1+s_2+s_5=55$ gives $2s_1+s_2=39$. Since $s_2\le9$, $2s_1\ge30$, so $s_1\ge15>s_2$, a contradiction.

So the lowest score is $8$, $9$ or $10$, and the requested sum is $8+9+10=\boxed{27}$.''',
'Median|Mode|Range|Mean|Casework',4,
note='MATHCOUNTS handbook problem; scores assumed to be positive integers. All solutions were found by brute force.')
b.add(1745621,2,r'''Cayley has a fair six-sided die whose faces are numbered $-2,-1,0,0,1$ and $2$. She rolls the die three times. What is the probability that the sum of the three numbers she rolls is $0$? Express your answer as a common fraction.''',
r'''Count the $6^3=216$ equally likely ordered outcomes (the two $0$ faces are different faces).
\begin{itemize}
\item Three zeros: $2^3=8$ outcomes.
\item One zero together with $a$ and $-a$ ($a=1$ or $2$): $3!=6$ orders, $2$ choices of the zero face, $2$ values of $a$: $24$ outcomes.
\item No zero: the values must be $2,-1,-1$ or $-2,1,1$: $3$ orders each, $6$ outcomes.
\end{itemize}
In total $38$ outcomes, so the probability is $\dfrac{38}{216}=\boxed{\dfrac{19}{108}}$.''',
'Dice probability|Casework|Probability',3)
b.add(1745621,3,r'''A local college has $985$ students, of whom $460$ play a varsity sport and $571$ belong to a club. What is the absolute difference between the least and the greatest possible numbers of students who play a varsity sport and belong to a club?''',
r'''Let $x$ be the number in both. By inclusion-exclusion, $460+571-x\le985$, so $x\ge46$; and $x\le460$. Both extremes occur ($x=46$: every student is in at least one group; $x=460$: every athlete is in a club). The difference is $460-46=\boxed{414}$.''',
'Sets and inclusion–exclusion|Venn diagrams',2)

# ---------------- 1745770 faulty odometer
b.add(1745770,1,r'''A car's faulty odometer never shows an odd digit: it counts $0,2,4,6,8,20,22,\dots$, so a distance of $1$ mile is recorded as $2$ and a distance of $5$ miles is recorded as $20$. The car starts a trip with the odometer at $0$, and at the end of the trip the odometer shows $8866$. What is the actual distance travelled, in miles?''',
r'''The odometer uses the five digits $0,2,4,6,8$, which stand for $0,1,2,3,4$; so it writes the distance in base $5$ with each digit doubled. The reading $8866$ corresponds to the base-$5$ numeral $4433_5$:
\[
4\cdot125+4\cdot25+3\cdot5+3=500+100+15+3=\boxed{618}\text{ miles}.
\]''',
'Digits and bases',3)

# ---------------- 1574955 pentagon
fig=r'''pair B=(0,0),D=(2,0),C=(0.6,-0.5);
pair A=rotate(120,B)*C, Ep=rotate(-60,D)*C, P=rotate(120,B)*D, M=(A+Ep)/2;
fill(B--P--D--cycle,lightgray+opacity(0.4));
draw(A--B--C--D--Ep--cycle,linewidth(1));
draw(B--D,linewidth(0.6));draw(B--P,dashed);draw(P--D,dashed);draw(A--P,blue+dashed);draw(P--Ep,blue+dashed);draw(A--Ep,blue+dashed);draw(A--D,blue+dashed);
dot(A);dot(B);dot(C);dot(D);dot(Ep);dot(P);dot(M);
label("$A$",A,W);label("$B$",B,SW);label("$C$",C,S);label("$D$",D,SE);label("$E$",Ep,NE);label("$P$",P,N);label("$M$",M,dir(255));'''
b.add(1574955,1,r'''Let $ABCDE$ be a convex pentagon with $AB=BC$ and $CD=DE$. If $\angle ABC=120^\circ$, $\angle CDE=60^\circ$ and $BD=2$, find the area of $ABCDE$.''',
r'''Orient the pentagon counterclockwise. The rotation $\rho_B$ about $B$ through $120^\circ$ maps $C$ to $A$, and the rotation $\rho_D$ about $D$ through $60^\circ$ maps $E$ to $C$. Let $P=\rho_B(D)$; then triangle $BAP$ is the image of triangle $BCD$, so $[BAP]=[BCD]$, $BP=BD=2$ and $\angle DBP=120^\circ$.

The composition $\rho_B\circ\rho_D$ is a rotation through $120^\circ+60^\circ=180^\circ$, i.e.\ a half-turn about some point $M$. It maps $E\mapsto C\mapsto A$ and $D\mapsto D\mapsto P$, so $M$ is the midpoint of both $AE$ and $DP$. Hence the diagonals of quadrilateral $APED$ bisect each other: $APED$ is a parallelogram, and therefore $[APD]=[ADE]$ (each is half of the parallelogram).
'''+asy(fig,'7.5cm')+r'''
Now split the pentagon along $DA$ and $DB$, and the triangle $BPD$ along $AB$, $AP$ and $AD$ (signed areas make this valid in every position of the points):
\[
[ABCDE]=[ABD]+[BCD]+[ADE],\qquad [BPD]=[ABD]+[BAP]+[APD].
\]
The right-hand sides are equal term by term, so
\[
[ABCDE]=[BPD]=\dfrac12\cdot2\cdot2\cdot\sin120^\circ=\boxed{\sqrt3}.
\]''',
'Rotations|Parallelograms|Area decomposition|Quadrilaterals and polygons|Isosceles triangles',6,
note='The area is the same for every such pentagon; checked numerically for many random positions of C.')

# ---------------- 1745630 congruence
b.add(1745630,1,r'''Prove that for every integer $n\ge1$,
\[
(-13)^{n+1}\equiv(-13)^n+(-13)^{n-1}\pmod{181}.
\]''',
r'''Factor out $(-13)^{n-1}$: the difference of the two sides is
\[
(-13)^{n+1}-(-13)^n-(-13)^{n-1}=(-13)^{n-1}\bigl((-13)^2-(-13)-1\bigr)=(-13)^{n-1}(169+13-1)=181\cdot(-13)^{n-1},
\]
which is divisible by $181$. $\blacksquare$

(So the powers of $-13$ modulo $181$ satisfy the Fibonacci recurrence: $-13$ is a root of $t^2\equiv t+1\pmod{181}$.)''',
'Remainders and congruences|Factoring',2,
note='The post writes -13^{n+1} = -13^n + -13^{n-1}; read as powers of (-13), the reading for which the statement is true (with -(13^k) it would require 169 = 14 mod 181, false).')

# ---------------- 1745141 factors of 6!
b.add(1745141,1,r'''Two distinct positive divisors of $6!$ are selected at random. What is the probability that their sum is divisible by $6$?''',
r'''$6!=720=2^4\cdot3^2\cdot5$ has $5\cdot3\cdot2=30$ divisors, so there are $\dbinom{30}{2}=435$ equally likely pairs. Sort the divisors by their remainder modulo $6$.
\begin{itemize}
\item A divisor not divisible by $6$ lacks the factor $2$ or the factor $3$. Those of the form $2^a5^c$ with $a\ge1$ are $2,4,8,16,10,20,40,80$, with remainders $2,4,2,4,4,2,4,2$: four $\equiv2$ and four $\equiv4$.
\item Those of the form $3^b5^c$ with $b\ge1$ are $3,9,15,45$, all $\equiv3$.
\item Then $1$ and $5$, with remainders $1$ and $5$.
\item The remaining $30-14=16$ divisors are multiples of $6$.
\end{itemize}
The sum is divisible by $6$ for pairs of remainders $(0,0)$, $(1,5)$, $(2,4)$, $(3,3)$:
\[
\dbinom{16}{2}+1\cdot1+4\cdot4+\dbinom42=120+1+16+6=143 .
\]
The probability is $\boxed{\dfrac{143}{435}}$.''',
'Divisor counting|Remainders and congruences|Probability|Factorials',5)

# ---------------- 1745554 x^6+y^6
b.add(1745554,1,r'''Real numbers $x$ and $y$ satisfy
\[
x^6+y^6=6969,\qquad x^9+y^9=69 .
\]
How many distinct values can $\dfrac xy$ take?''',
r'''Let $a=x^3$, $b=y^3$; since cube roots of reals are unique, real pairs $(x,y)$ correspond exactly to real pairs $(a,b)$ with $a^2+b^2=6969$, $a^3+b^3=69$. Put $s=a+b$, $p=ab$. Then $p=\dfrac{s^2-6969}{2}$ and
\[
69=a^3+b^3=s^3-3ps=s^3-\dfrac{3s(s^2-6969)}{2}\iff f(s):=s^3-20907s+138=0 .
\]
For $a,b$ to be real we need $s^2-4p\ge0$, i.e.\ $s^2\le13938$. Let $m=\sqrt{13938}$. We have $f(-m)=6969m+138>0$ and $f(m)=-6969m+138<0$. The derivative $3s^2-20907$ vanishes at $\pm\sqrt{6969}$, both inside $(-m,m)$; $f$ increases on $[-m,-\sqrt{6969}]$ (so it stays positive there), decreases on $[-\sqrt{6969},\sqrt{6969}]$, and increases on $[\sqrt{6969},m]$ up to the negative value $f(m)$. Hence $f$ has exactly one root $s_0$ with $s_0^2\le13938$ (in fact $s_0\approx0.0066$), and then $s_0^2<13938$, so $a\ne b$ are the two distinct real roots of $t^2-s_0t+p_0$.

The real solutions are therefore $(a,b)$ and $(b,a)$, giving the ratios $\dfrac xy=\sqrt[3]{\dfrac ab}$ and $\sqrt[3]{\dfrac ba}$. Neither $a$ nor $b$ is $0$ (that would force $6969^{3}=69^2$), and these two ratios are reciprocals, equal only if $\dfrac ab=\pm1$; $a=b$ is excluded and $a=-b$ would give $a^3+b^3=0\ne69$. So $\dfrac xy$ takes exactly $\boxed{2}$ values.''',
'Equations and systems of equations|Vieta\'s formulas|Polynomials|Substitution',5,
note='The post does not say whether x, y are real; the real reading is used (over the complex numbers the count would be different and the post gives no answer). The answer is a count, not an expression in 6969 and 69 as the post suggests.')

# ---------------- 1743700 harmonic mean
b.add(1743700,1,r'''Find the harmonic mean of $10$ and $20$.''',
r'''The harmonic mean of $a$ and $b$ is $\dfrac{2}{\dfrac1a+\dfrac1b}=\dfrac{2ab}{a+b}$. For $10$ and $20$: $\dfrac{2\cdot200}{30}=\boxed{\dfrac{40}{3}}$.''',
'Harmonic mean',1,
note='Apparently 2006 iTest Problem 2 (not named in the post); only two of the answer choices are quoted, so the record is free-response.')

# ---------------- 1743708 perpendicular line
fig=r'''import graph;
real f(real x){return 3-2x;} real g(real x){return 3+x/2;}
draw((-8,0)--(4,0),gray,Arrow(5));draw((0,-2)--(0,7),gray,Arrow(5));
draw((-0.5,4)--(2.5,-2),linewidth(0.9));draw((-8,-1)--(3,4.5),blue+linewidth(0.9));
pair X=(-6,0),Y=(0,3),Z=(0.6,3.3);
dot(X);dot(Y);
label("$x$",(4,0),S);label("$y$",(0,7),W);
label("$(0,3)$",Y+(-1.4,0.5));label("$(-6,0)$",X,dir(-60));
label("$2x+y=3$",(2.2,-1.4),E);label("$y=\dfrac12x+3$",(-5.6,3.2),blue);
pair H=(0.6,1.8);'''
b.add(1743708,1,r'''A line has $y$-intercept $(0,3)$ and is perpendicular to the line $2x+y=3$. Find the $x$-intercept of the line.

$\textbf{(A) }(4,0)\quad\textbf{(B) }(6,0)\quad\textbf{(C) }(-4,0)\quad\textbf{(D) }(-6,0)\quad\textbf{(E) }\text{none of the above}$''',
r'''The line $2x+y=3$ has slope $-2$, so a perpendicular line has slope $\dfrac12$. With $y$-intercept $3$ it is $y=\dfrac12x+3$, which meets the $x$-axis where $\dfrac12x=-3$, at $(-6,0)$. The answer is $\boxed{\textbf{(D)}\ (-6,0)}$.
'''+asy(fig,'6cm'),
'Perpendicular lines|Slope|Coordinate geometry',2,
note='Apparently 2006 iTest Problem 5 (not named in the post).')

# ---------------- 1731039 Dulce
b.add(1731039,1,r'''Dulce eats mints at a uniform rate of $10$ mints every $11$ days. At the end of each day her cousin adds one more mint to her supply. She starts on a Monday with $2018$ mints. On what day of the week does she first finish all of her mints?''',
r'''Each day Dulce eats $\dfrac{10}{11}$ of a mint and then receives $1$ mint, so her supply never decreases over a full day. More precisely, at time $t$ days after the start (with $k=\lfloor t\rfloor$ cousin's mints received so far) she has
\[
2018+k-\dfrac{10}{11}t\ \ge\ 2018+k-\dfrac{10}{11}(k+1)=2018+\dfrac{k-10}{11}>0
\]
mints left. So she \textbf{never} finishes the mints: there is no such day. (The supply grows by $\dfrac1{11}$ of a mint per day on average.)''',
'Rates|Bounding and extremal cases',2,
note='Problem 1 of a "Devil\'s Night" set, kept as stated: with these numbers the supply grows, so the answer is that she never finishes (the poster gives no answer). Problems 2 and 3 are dropped (see screening).')

# ---------------- 1742448 train and bus
b.add(1742448,1,r'''Walking at $5$ km/h, I miss the train by $7$ minutes. If I go by bus at $30$ km/h, I arrive $13$ minutes early. How far is the station from my house?''',
r'''Let the distance be $d$ km. Walking takes $\dfrac d5$ hours and the bus $\dfrac d{30}$ hours; the difference is $7+13=20$ minutes $=\dfrac13$ hour. So $\dfrac d5-\dfrac d{30}=\dfrac d6=\dfrac13$, and $d=\boxed{2\text{ km}}$. (Walking takes $24$ minutes, the bus $4$ minutes.)''',
'Distance, rate, and time|Linear equations',2)

# ---------------- 1745435 Rickards wand
fig=r'''pair O=(3,3),P1=(9,11),P2=(-5,-3),H=(2,4);
draw((-9,0)--(15,0),gray,Arrow(5));draw((0,-9)--(0,15),gray,Arrow(5));
draw(circle(O,10),linewidth(0.9));
draw((-8,-6)--(12,14),blue+linewidth(0.9));
draw(O--H,dashed);draw(O--P1,dashed);
draw(H+0.7*dir(-45)--H+0.7*dir(-45)+0.7*dir(45)--H+0.7*dir(45));
dot(O);dot(P1);dot(P2);dot(H);
label("$O$",O,SE);label("$P$",P1,dir(100));label("$Q$",P2,dir(280));label("$H$",H,NW);
label("$10$",(O+P1)/2,SE);label("$y=x+2$",(12,14),E,blue);label("$x$",(15,0),S);label("$y$",(0,15),W);'''
b.add(1745435,1,r'''A line passes through the points $\left(\dfrac{27}{2},\dfrac{31}{2}\right)$ and $\left(-\dfrac{36}{7},-\dfrac{22}{7}\right)$, and a circle has centre $(3,3)$ and radius $10$. What is the distance between the two points where the line intersects the circle?''',
r'''The slope of the line is
\[
\dfrac{\dfrac{31}{2}+\dfrac{22}{7}}{\dfrac{27}{2}+\dfrac{36}{7}}=\dfrac{\dfrac{261}{14}}{\dfrac{261}{14}}=1,
\]
so the line is $y=x+2$ (check: $\dfrac{31}{2}=\dfrac{27}{2}+2$). The distance from the centre $O=(3,3)$ to the line $x-y+2=0$ is $\dfrac{|3-3+2|}{\sqrt2}=\sqrt2$; the foot of the perpendicular is $H=(2,4)$.
'''+asy(fig,'6cm')+r'''
$H$ is the midpoint of the chord $PQ$, and in right triangle $OHP$, $HP=\sqrt{10^2-2}=7\sqrt2$. So $PQ=\boxed{14\sqrt2}$. (Indeed the intersection points are $(9,11)$ and $(-5,-3)$.)''',
'Coordinate geometry|Circles|Arcs and chords|Distance formula|Pythagorean theorem',3,source=src('Rickards High School Math Tournament',2018,'Geometry'),
note='Story about a wand removed.')

# ---------------- 1744310 3^2006
b.add(1744310,1,r'''What is the last (rightmost) digit of $3^{2006}$?''',
r'''The last digits of $3^1,3^2,3^3,3^4,\dots$ repeat with period $4$: $3,9,7,1$. Since $2006=4\cdot501+2$, the last digit of $3^{2006}$ equals that of $3^2$, namely $\boxed{9}$.''',
'Units digits and last digits|Modular exponentiation',1,
note='Apparently 2006 iTest Problem 21 (not named in the post).')

# ---------------- 1745417 papaya box
fig=r'''real s=4.6; pair k=(0.45,0.3);
pair o=(0,0);
path front=(0,0)--(s,0)--(s,s)--(0,s)--cycle;
draw(front,linewidth(0.9));draw((0,s)--(0,s)+s*k--(s,s)+s*k--(s,s));draw((s,0)--(s,0)+s*k--(s,s)+s*k);
draw((0,0)--s*k,dashed+gray);draw(s*k--(s,0)+s*k,dashed+gray);draw(s*k--(0,s)+s*k,dashed+gray);
real t=s-2; pair q=(1,1)+1*k;
draw(shift(q)*((0,0)--(t,0)--(t,t)--(0,t)--cycle),blue+dashed);
draw(shift(q)*((0,t)--(0,t)+t*k--(t,t)+t*k--(t,t)),blue+dashed);draw(shift(q)*((t,0)--(t,0)+t*k--(t,t)+t*k),blue+dashed);
label("$s$",(s/2,0),S);label("$s-2$",q+(0,t/2),W,blue);
draw((s+0.15,0)--(s+0.15,1),Arrows(3));label("$1$",(s+0.15,0.5),E);'''
b.add(1745417,1,r'''A solid papaya has the shape of an ellipsoid with semi-axes $\dfrac3\pi$, $4$ and $5$ inches. It is to be reshaped into a hollow cubical box whose walls are $1$ inch thick (on all six faces), using exactly the same volume of material as the ellipsoid. What is the outer edge length of the box, in inches?''',
r'''An ellipsoid with semi-axes $p,q,r$ has volume $\dfrac43\pi pqr$, here $\dfrac43\pi\cdot\dfrac3\pi\cdot4\cdot5=80$ cubic inches. A box of outer edge $s$ with walls $1$ inch thick has an inner cavity of edge $s-2$:
'''+asy(fig,'4.5cm')+r'''
So the material has volume
\[
s^3-(s-2)^3=6s^2-12s+8=80\iff s^2-2s-12=0\iff s=1\pm\sqrt{13}.
\]
The edge is positive (and greater than $2$), so $s=\boxed{1+\sqrt{13}}\approx4.61$ inches.''',
'Volume|Cubes and rectangular prisms|Quadratic equations',3,source=src('Rickards High School Math Tournament',2018,'Geometry'),
note='"Same volume as the ellipsoid" is read as the volume of the walls (the material), the reading that makes the thickness relevant. Story details trimmed.')

# ---------------- 1744972 pigs
b.add(1744972,1,r'''A farmer has $107$ pigs, all kept in two pens, with no pig in both pens. Prove that the two pens cannot both contain an odd number of pigs.''',
r'''If the pens held $2m+1$ and $2n+1$ pigs, the total would be $2(m+n+1)$, an even number. But $107$ is odd, a contradiction. $\blacksquare$

(The riddle in the post is answered by putting one pen inside the other, so that some pigs are counted in both pens; that is exactly what the condition ``no pig in both pens'' rules out.)''',
'Parity|Proof by contradiction',1,
note='Lateral-thinking riddle turned into the underlying parity statement.')

# ---------------- 1734050 self-counting sentence
b.add(1734050,1,r'''Fill in the blanks with numbers written as words (such as ``seven'') so that the following sentence is true, counting letters regardless of case:
\begin{center}
``This sentence contains \underline{\hspace{1.5cm}} e's, \underline{\hspace{1.5cm}} t's, and \underline{\hspace{1.5cm}} s's.''
\end{center}
What is the sum of the three numbers?''',
r'''Without the three number words, the sentence ``This sentence contains e's, t's, and s's.'' has $4$ e's (three in ``sentence'', one in ``e's''), $4$ t's (in ``This'', ``sentence'', ``contains'', ``t's'') and $7$ s's (one each in ``This'', ``sentence'', ``contains'', ``e's'', ``t's'', two in ``s's''). If the blanks are the words $X,Y,Z$, the conditions are
\[
x=4+e(X)+e(Y)+e(Z),\quad y=4+t(X)+t(Y)+t(Z),\quad z=7+s(X)+s(Y)+s(Z),
\]
where $e(W)$ counts the e's of word $W$, and $x,y,z$ are the numbers named by $X,Y,Z$.

Try $X=$ six, $Y=$ five, $Z=$ eight: then $x=4+0+1+1=6$, $y=4+0+0+1=5$, $z=7+1+0+0=8$. All three conditions hold:
\begin{center}
``This sentence contains six e's, five t's, and eight s's.''
\end{center}
This is the only solution: a number word below $100$ has at most four e's, three t's and two s's, so $x\le16$, $y\le13$, $z\le13$, and checking all the finitely many candidates leaves only $(6,5,8)$. The sum is $6+5+8=\boxed{19}$.''',
'Logical deduction|Systematic counting',4,
note='Letters are counted case-insensitively (the T of "This" counts). The uniqueness of (6,5,8) was confirmed by an exhaustive check of all triples up to 49.')

# ---------------- 1744827 lcm(700,n)
b.add(1744827,1,r'''Find the largest three-digit positive integer $n$ such that $\operatorname{lcm}(700,n)$ has exactly four digits and at least one digit of $n$ is a $7$.''',
r'''Write $g=\gcd(700,n)$ and $k=\dfrac ng$, so $\operatorname{lcm}(700,n)=700k$. This has four digits exactly when $2\le k\le14$. Then $g=\dfrac nk\ge\dfrac n{14}$.

Suppose $n\ge876$. Then $g\ge\dfrac{876}{14}>62$, so $g$ is one of the divisors $70,100,140,175,350,700$ of $700$. The multiples $n=gk$ of these with $876\le n\le999$ and $k\le14$ are $910,980,900$ (from $g=70,140,100$), and none contains the digit $7$. (Multiples of $175$, $350$, $700$ in that range do not exist.)

For $n=875=7\cdot125$: $g=\gcd(700,875)=175$, $k=5$, and $\operatorname{lcm}=3500$ has four digits. So the answer is $\boxed{875}$.''',
'HCF and LCM|Factors and multiples|Digit problems',4)

# ---------------- 1744022 cube with holes, falcon
fig=r'''pair k=(0.5,0.35);
void face(pair o,pair u,pair v){
 for(int i=0;i<=5;++i){draw((o+i*u)--(o+i*u+5*v),linewidth(0.5));draw((o+i*v)--(o+i*v+5*u),linewidth(0.5));}
 fill((o+2*u+2*v)--(o+3*u+2*v)--(o+3*u+3*v)--(o+2*u+3*v)--cycle,black);
}
face((0,0),(1,0),(0,1));
face((0,5),(1,0),k);
face((5,0),k,(0,1));
draw((0,0)--(5,0)--(5,5)--(0,5)--cycle,linewidth(1));
draw((0,5)--(0,5)+5*k--(5,5)+5*k--(5,5),linewidth(1));draw((5,0)--(5,0)+5*k--(5,5)+5*k,linewidth(1));'''
b.add(1744022,1,r'''Unit cubes are stacked to form a cube of edge length $5$. A square hole with side length $1$ is made through the centre of each face, straight through the entire figure (so three perpendicular tunnels meet at the centre). The resulting solid is dipped in paint and then taken apart into its unit cubes. How many of the unit cubes have exactly two faces painted?''',
r'''Use coordinates $0,1,2,3,4$ in each direction; the tunnels remove the unit cubes with at least two coordinates equal to $2$, i.e.\ $3\cdot5-2=13$ cubes, leaving $112$. After dipping, a face of a unit cube is painted when it is on the outside of the big cube or on the wall of a tunnel.
'''+asy(fig,'4.5cm')+r'''
\begin{itemize}
\item \textbf{Edge cubes} (not corners) of the big cube: $12$ edges with $3$ each, $36$ cubes. Each has two outer faces and touches no tunnel, so exactly two painted faces.
\item \textbf{Face cubes} (one outer face): on each face, the four cubes sharing an edge with the hole have their outer face and one tunnel wall painted: $4\cdot6=24$ cubes. The other face cubes have one painted face.
\item \textbf{Interior cubes} (the $3\times3\times3$ core, minus the $7$ tunnel cubes in it): the $12$ cubes at the middles of the core's edges, such as $(2,1,1)$, touch two tunnels (at $(2,2,1)$ and $(2,1,2)$), so they have exactly two painted faces; the $8$ core corners such as $(1,1,1)$ touch no tunnel.
\item Corner cubes have three painted faces.
\end{itemize}
The total is $36+24+12=\boxed{72}$.''',
'Cubes and rectangular prisms|Counting shapes in figures|Casework',5,
note='Checked by a direct computer count over the 112 remaining cubes.')
fig=r'''real a=3; pair k=(0.5,0.35);
pair T=(a,a)+a*k;
draw((0,0)--(a,0)--(a,a)--(0,a)--cycle,linewidth(0.9));
draw((0,a)--(0,a)+a*k--T--(a,a),linewidth(0.9));draw((a,0)--(a,0)+a*k--T,linewidth(0.9));
draw((0,0)--a*k,dashed+gray);draw(a*k--(0,a)+a*k,dashed+gray);draw(a*k--(a,0)+a*k,dashed+gray);
draw(circle(T,a),blue+linewidth(0.8));
draw(shift(T)*xscale(a)*yscale(0.35*a)*unitcircle,blue+dashed);
dot(T);label("$T$",T,NE);draw(T--T+(0,a),blue);label("$30$",T+(0,a/2),E,blue);
label("$30$",(a/2,0),S);'''
b.add(1744022,2,r'''A falcon is tied to an upper corner of a cube-shaped house with edge length $10$ yards by a rope $30$ feet long. Find the volume, in cubic feet, of the region in which the falcon can fly.''',
r'''The edge is $10$ yards $=30$ feet, equal to the rope length. Put the corner $T$ at the origin, with the house occupying the octant region $0\le x,y\le30$, $-30\le z\le0$, the ground being the plane $z=-30$.
'''+asy(fig,'5cm')+r'''
With the rope taut in a straight line the falcon reaches every point within $30$ feet of $T$ that is not inside the house, and it can never be farther than $30$ feet from $T$. The ball of radius $30$ about $T$ lies entirely above the ground (its lowest point is at ground level). Its eighth in the octant $x\ge0,y\ge0,z\le0$ lies inside the house, since each coordinate of such a point has absolute value at most $30$. Points of that octant outside the house have a coordinate beyond $30$ in absolute value, so they are more than $30$ feet from $T$ even when the rope wraps around the house. So the region is the other seven eighths of the ball:
\[
\dfrac78\cdot\dfrac43\pi\cdot30^3=\boxed{31500\pi}\text{ cubic feet}.
\]''',
'Spheres|Volume|Cubes and rectangular prisms|Unit conversion',4)

b.save()
