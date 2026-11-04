from qb import *
b=Bank('p234_02')
FBH=lambda y,g,q: src('Junior Regional Olympiad FBH',y,'Grade %d'%g,q)
RA=r'''void ra(pair P,pair U,pair V,real s){draw(P+s*unit(U-P)--P+s*unit(U-P)+s*unit(V-P)--P+s*unit(V-P),linewidth(0.5));}
'''

# ---------------- 1715264 three problems
fig=r'''import graph;
pair P=(2,3),Q=(7,-7),X=(5,-3);
draw((-0.5,0)--(8.5,0),gray,Arrow(5));draw((0,-8)--(0,4.5),gray,Arrow(5));
label("$x$",(8.5,0),N,gray);label("$y$",(0,4.5),W,gray);
draw(P--X,red+linewidth(1));draw(X--Q,blue+linewidth(1));
draw(P--(5,3),dashed);draw((5,3)--X,dashed);
dot(P);dot(Q);dot(X);
label("$(2,3)$",P,N);label("$(7,-7)$",Q,E);label("$(5,-3)$",X,E);
label("$60\%$",(2.6,1.2),W,red);label("$40\%$",(X+Q)/2,SW,blue);
label("$3$",(3.5,3),S);label("$6$",(5,1.5),E);'''
b.add(1715264,1,r'''Let $(x,y)$ be the point that is $60\%$ of the way from the point $(2,3)$ to the point $(7,-7)$. What is $x+y$?''',
r'''Moving from $(2,3)$ to $(7,-7)$ changes $x$ by $5$ and $y$ by $-10$. Going $60\%$ of the way changes them by $0.6\cdot5=3$ and $0.6\cdot(-10)=-6$, so
\[
(x,y)=(2+3,\ 3-6)=(5,-3),
\]
and $x+y=\boxed{2}$. (No distance formula is needed: the point divides the segment in the ratio $3:2$, and each coordinate moves the same fraction of the way.)
'''+asy(fig,'4cm'),
'Coordinate geometry|Ratios, proportions, and variation',2,
note='Problem 1 of the post; the posted answer 2 is correct.')
b.add(1715264,2,r'''How many prime numbers less than $200$ can be expressed as the difference of two positive perfect cubes?''',
r'''If $p=a^3-b^3=(a-b)(a^2+ab+b^2)$ with positive integers $a>b$, then since $a^2+ab+b^2>1$ and $p$ is prime, we must have $a-b=1$. With $a=b+1$,
\[
p=(b+1)^3-b^3=3b^2+3b+1 .
\]
For $b=1,2,\dots,7$ this gives $7,19,37,61,91,127,169$, and $b=8$ gives $217>200$. Among these, $91=7\cdot13$ and $169=13^2$ are composite, while $7,19,37,61,127$ are prime. So there are $\boxed{5}$ such primes.''',
'Prime numbers|Sum and difference of cubes|Factoring|Perfect cubes',3,
note='Problem 2 of the post; the posted answer 5 is correct.')
b.add(1715264,3,r'''The expression $(a+b+c+d)^6$ is expanded and like terms are combined. How many terms are in the resulting expression?''',
r'''Every term of the expansion has the form $k\,a^ib^jc^kd^l$ with nonnegative integers $i+j+k+l=6$, and every such monomial actually occurs with a positive coefficient (the multinomial coefficient $\dfrac{6!}{i!\,j!\,k!\,l!}$). So the number of terms is the number of nonnegative integer solutions of $i+j+k+l=6$, which by stars and bars is
\[
\dbinom{6+3}{3}=\dbinom93=\boxed{84}.
\]''',
'Stars and bars|Distributions and integer solutions|Combinatorial identities and binomial coefficients',3,
note='Problem 3 of the post; the posted answer 84 is correct.')

# ---------------- 1715061 FBH 2016 G8 P3 trapezoid
fig=RA+r'''pair B=(0,0),C=(7,0);
pair D=C+3*dir(120),A=3*sqrt(3)*dir(30);
pair P=extension(B,A,C,D);
pair Ee=(A+B)/2,M=(B+C)/2,F=(C+D)/2,Nn=(A+D)/2;
draw(A--P--D,dashed+gray);draw(Nn--P,dashed+gray);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(M--Nn,blue+linewidth(0.8));draw(Ee--F,red+linewidth(0.8));
dot(Ee);dot(F);dot(M);dot(Nn);dot(P);
draw(arc(B,1.1,0,30));draw(arc(C,0.9,120,180));
label("$30^\circ$",B+1.55*dir(15));label("$60^\circ$",C+1.35*dir(150));
label("$A$",A,NW);label("$D$",D,NE);label("$B$",B,SW);label("$C$",C,SE);label("$P$",P,N);
label("$E$",Ee,NW);label("$F$",F,NE);label("$M$",M,S);label("$N$",Nn,dir(-75));
label("$7$",(B+C)/2+(1.2,0),S);label("$3$",M+0.25*(Nn-M),E,blue);'''
b.add(1715061,1,r'''In trapezoid $ABCD$ with $AD\parallel BC$, we have $\angle ABC=30^\circ$, $\angle BCD=60^\circ$ and $BC=7$. Let $E$, $M$, $F$ and $N$ be the midpoints of the sides $AB$, $BC$, $CD$ and $DA$, respectively. If $MN=3$, find $EF$.''',
r'''Extend the legs $BA$ and $CD$ to meet at $P$. Since $\angle PBC+\angle PCB=30^\circ+60^\circ=90^\circ$, triangle $PBC$ has a right angle at $P$; the same holds for triangle $PAD$, which is similar to it (as $AD\parallel BC$).
'''+asy(fig,'7cm')+r'''
\textbf{$P$, $N$, $M$ are collinear.} The dilation with centre $P$ that maps $A$ to $B$ maps line $AD$ to the parallel line $BC$, hence $D$ to $C$ and the midpoint $N$ of $AD$ to the midpoint $M$ of $BC$. So $N$ lies on segment $PM$.

\textbf{Medians to the hypotenuses.} In a right triangle the median to the hypotenuse is half the hypotenuse, so $PM=\dfrac{BC}{2}=\dfrac72$ and $PN=\dfrac{AD}{2}$. Hence
\[
MN=PM-PN=\dfrac{BC-AD}{2}=3\quad\Longrightarrow\quad AD=7-6=1 .
\]
\textbf{The midline.} $EF$ is the midline of the trapezoid, so
\[
EF=\dfrac{AD+BC}{2}=\dfrac{1+7}{2}=\boxed{4}.
\]
(Coordinates confirm it: with $B=(0,0)$, $C=(7,0)$ we get $A=\left(\dfrac92,\dfrac{3\sqrt3}{2}\right)$, $D=\left(\dfrac{11}2,\dfrac{3\sqrt3}{2}\right)$, $M=\left(\dfrac72,0\right)$, $N=\left(5,\dfrac{3\sqrt3}2\right)$ and $MN=\sqrt{\dfrac94+\dfrac{27}4}=3$.)''',
'Trapezoids|Midpoints|Right triangles|Dilations and homothety|Similarity',4,source=FBH(2016,8,3),
note='AD is the shorter base (forced by the angles: with these angles AD = 7 - 2s < 7 for the leg CD = s). Checked with coordinates.')

# ---------------- 1714787 consecutive product 3080
b.add(1714787,1,r'''The product of two consecutive integers is $3080$. What are the two integers?''',
r'''Let the integers be $n$ and $n+1$: $n^2+n-3080=0$. Since $55^2=3025$ and $3080=3025+55=55\cdot56$, the equation factors as
\[
(n-55)(n+56)=0 ,
\]
so $n=55$ or $n=-56$. The integers are $\boxed{55\text{ and }56}$, or $\boxed{-56\text{ and }-55}$ if negative integers are allowed. (Estimating $\sqrt{3080}\approx55.5$ leads directly to $55\cdot56$.)''',
'Quadratic equations|Factoring',1,
note='The post says "numbers"; read as integers, and both the positive and the negative pair are given.')

# ---------------- 1715130 sequence telescoping
b.add(1715130,1,r'''In the sequence $-1,1,4,8,\dots$, each term after the first is $n$ more than the previous term, where $n$ is its position (so the $n$th term equals the $(n-1)$st term plus $n$). Find the value of
\[
(a_{2018}-a_{2017})+(a_{2017}-a_{2016})+\cdots+(a_2-a_1),
\]
where $a_k$ is the $k$th term.''',
r'''The sum telescopes: all intermediate terms cancel and it equals $a_{2018}-a_1$. Also each bracket is known directly: $a_k-a_{k-1}=k$. Either way the value is
\[
\sum_{k=2}^{2018}k=\dfrac{2018\cdot2019}{2}-1=2037171-1=\boxed{2037170}.
\]
(Check with the given terms: $a_2-a_1=2$, $a_3-a_2=3$, $a_4-a_3=4$.)''',
'Telescoping sums|Arithmetic sequences|Summation|Recurrence relations',2,
note='The wording "the 2018th term, minus the 2017th term, plus the 2017th term, minus the 2016th term, and so on" is written as the bracketed telescoping sum. The same problem was also posted (topic 1713859) with first term 1; that copy is aliased here.')

# ---------------- 1715046 FBH 2016 G7 P2
b.add(1715046,1,r'''Let
\[
w=\sqrt{1+\sqrt{-3+2\sqrt3}}-\sqrt{1-\sqrt{-3+2\sqrt3}} .
\]
Prove that $w=\sqrt3-1$.''',
r'''Let $u=\sqrt{-3+2\sqrt3}$. Since $3<2\sqrt3<4$ (because $9<12<16$), we have $0<-3+2\sqrt3<1$, so $0<u<1$ and both outer roots are defined. Moreover $1+u>1-u$, so $w>0$.

Square:
\[
w^2=(1+u)+(1-u)-2\sqrt{(1+u)(1-u)}=2-2\sqrt{1-u^2}=2-2\sqrt{1-(-3+2\sqrt3)}=2-2\sqrt{4-2\sqrt3}.
\]
Now $4-2\sqrt3=3-2\sqrt3+1=(\sqrt3-1)^2$ and $\sqrt3-1>0$, so $\sqrt{4-2\sqrt3}=\sqrt3-1$. Hence
\[
w^2=2-2(\sqrt3-1)=4-2\sqrt3=(\sqrt3-1)^2 .
\]
Since $w>0$ and $\sqrt3-1>0$, it follows that $w=\sqrt3-1$. $\blacksquare$''',
'Radicals|Algebraic manipulation',3,source=FBH(2016,7,2))

# ---------------- 1715043 FBH 2016 G7 P1
b.add(1715043,1,r'''Last year a company made a profit equal to $112\%$ of the expected profit. What percent of the profit actually made was the expected profit?''',
r'''Let the expected profit be $E$; the actual profit is $1.12E$. The required percentage is
\[
\dfrac{E}{1.12E}\cdot100\%=\dfrac{100}{1.12}\%=\dfrac{2500}{28}\%=\boxed{89\dfrac27\%}\approx89.29\% .
\]''',
'Percentages',2,source=FBH(2016,7,1),
note='The company is from Tesanj in the original; the place name is omitted.')

# ---------------- 1715049 FBH 2016 G7 P4
fig=RA+r'''pair C=(0,0),A=(0,6),B=(8,0),D=(A+B)/2;
pair Ep=(0,4);
pair F=extension(D,D+rotate(-90)*(Ep-D),C,B);
pair Ep2=2*D-Ep;
draw(A--B--C--cycle,linewidth(0.9));
draw(Ep--D--F,linewidth(0.8));draw(Ep--F,linewidth(0.8));
draw(D--Ep2,blue+dashed);draw(B--Ep2,blue+dashed);draw(F--Ep2,blue+dashed);
ra(C,A,B,0.4);ra(D,Ep,F,0.4);ra(B,Ep2,C,0.4);
dot(D);dot(Ep);dot(F);dot(Ep2,blue);
label("$C$",C,SW);label("$A$",A,N);label("$B$",B,SE);label("$D$",D,N);
label("$E$",Ep,W);label("$F$",F,S);label("$E'$",Ep2,E,blue);'''
b.add(1715049,1,r'''In right triangle $ABC$ with the right angle at $C$, let $D$ be the midpoint of the hypotenuse $AB$. Points $E$ and $F$ lie on the legs $AC$ and $BC$ respectively, such that $DE\perp DF$. Prove that $EF^2=AE^2+BF^2$.''',
r'''Let $E'$ be the reflection of $E$ in $D$.
'''+asy(fig,'6cm')+r'''
\textbf{$BE'=AE$ and $BE'\parallel AC$.} The segments $AB$ and $EE'$ bisect each other at $D$, so $AEBE'$ is a parallelogram (if $E=A$ then $E'=B$ and everything below is trivial). Hence $BE'=AE$ and $BE'\parallel AE$, i.e.\ $BE'\parallel AC$. Since $AC\perp BC$, also $BE'\perp BC$, so $\angle E'BF=90^\circ$.

\textbf{$FE'=FE$.} $D$ is the midpoint of $EE'$ and $DF\perp EE'$, so $DF$ is the perpendicular bisector of $EE'$ and $FE'=FE$.

\textbf{Pythagoras.} In the right triangle $E'BF$,
\[
EF^2=FE'^2=BE'^2+BF^2=AE^2+BF^2 . \qquad\blacksquare
\]''',
'Right triangles|Pythagorean theorem|Reflections|Midpoints|Perpendicular bisectors|Parallelograms',4,source=FBH(2016,7,4),
note='"Shorter sides" means the legs. Checked numerically for random positions of E.')

# ---------------- 1715033 FBH 2016 G6 P4 angles
fig=r'''pair O=(0,0);
real a=105,c=70,d=42;
pair A=4*dir(a),C=4*dir(c),D=4*dir(d),B=4*dir(0);
draw(O--A,linewidth(0.9));draw(O--B,linewidth(0.9));draw(O--C,linewidth(0.8));draw(O--D,linewidth(0.8));
draw(arc(O,1.2,c,a),red);draw(arc(O,1.5,d,c),blue);draw(arc(O,1.2,0,d),heavygreen);
label("$\dfrac54x$",O+1.85*dir((a+c)/2),red);
label("$x$",O+2.0*dir((c+d)/2),blue);
label("$\dfrac32x$",O+1.9*dir(d/2),heavygreen);
label("$O$",O,SW);label("$A$",A,N);label("$C$",C,NE);label("$D$",D,NE);label("$B$",B,E);'''
b.add(1715033,1,r'''Points $C$ and $D$ lie inside angle $\angle AOB$ so that the rays $OA$, $OC$, $OD$, $OB$ occur in this order. If $5\angle COD=4\angle AOC$, $3\angle COD=2\angle DOB$ and $\angle AOB=105^\circ$, find $\angle COD$.''',
r'''Let $\angle COD=x$. Then $\angle AOC=\dfrac54x$ and $\angle DOB=\dfrac32x$. With the rays in the order $OA,OC,OD,OB$,
\[
\angle AOB=\angle AOC+\angle COD+\angle DOB=\dfrac54x+x+\dfrac32x=\dfrac{15}{4}x=105^\circ ,
\]
so $x=\boxed{28^\circ}$ (and $\angle AOC=35^\circ$, $\angle DOB=42^\circ$).
'''+asy(fig,'5cm')+r'''
(If instead the order were $OA,OD,OC,OB$, then $\angle AOB=\angle AOC+\angle DOB-\angle COD=\dfrac74x$, giving $x=60^\circ$; the order is specified to make the answer unique.)''',
'Angles and lines|Linear equations',2,source=FBH(2016,6,4),
note='The original does not state the order of the rays; the order OA, OC, OD, OB is stated (the other order OA, OD, OC, OB would give 60 degrees, which is mentioned in the solution).')

# ---------------- 1715057 FBH 2016 G8 P1
b.add(1715057,1,r'''If $a>b>c$ are real numbers, prove that
\[
\dfrac{1}{a-b}+\dfrac{1}{b-c}>\dfrac{2}{a-c}.
\]''',
r'''Put $x=a-b>0$ and $y=b-c>0$; then $a-c=x+y$. We have
\[
\dfrac1x+\dfrac1y=\dfrac{x+y}{xy}\ge\dfrac{4}{x+y},
\]
because this is equivalent to $(x+y)^2\ge4xy$, i.e.\ $(x-y)^2\ge0$. Since $\dfrac4{x+y}>\dfrac2{x+y}$, we get
\[
\dfrac{1}{a-b}+\dfrac{1}{b-c}\ge\dfrac4{a-c}>\dfrac{2}{a-c}. \qquad\blacksquare
\]
(The stronger inequality with $4$ in place of $2$ holds, with equality when $b$ is the midpoint of $a$ and $c$.)''',
'Inequalities|AM-GM inequality|Substitution',2,source=FBH(2016,8,1))

# ---------------- 1715070 FBH 2016 G8 P5 sphere pyramids
b.add(1715070,1,r'''$605$ equal spheres are divided into two groups. From the first group an upright pyramid with a square base is built (each layer is a square array, with $1,4,9,\dots$ spheres from the top), and from the second group an upright pyramid with an equilateral triangular base is built (each layer is a triangular array, with $1,3,6,\dots$ spheres from the top). Both pyramids have the same number of layers. How many spheres are in each pyramid?''',
r'''With $n$ layers the square pyramid uses
\[
1^2+2^2+\cdots+n^2=\dfrac{n(n+1)(2n+1)}{6}
\]
spheres, and the triangular pyramid uses the sum of the first $n$ triangular numbers,
\[
1+3+6+\cdots+\dfrac{n(n+1)}{2}=\dfrac{n(n+1)(n+2)}{6}.
\]
Their total is
\[
\dfrac{n(n+1)\bigl[(2n+1)+(n+2)\bigr]}{6}=\dfrac{n(n+1)\cdot3(n+1)}{6}=\dfrac{n(n+1)^2}{2}=605 ,
\]
so $n(n+1)^2=1210=10\cdot11^2$. The left side increases with $n$, so $n=10$ is the only solution. The square pyramid has $\dfrac{10\cdot11\cdot21}{6}=\boxed{385}$ spheres and the triangular pyramid $\dfrac{10\cdot11\cdot12}{6}=\boxed{220}$ spheres ($385+220=605$).''',
'Summation|Triangular numbers|Sequences and series|Factoring',3,source=FBH(2016,8,5),
note='"Equal numbers of sphere rows" is read as the same number of layers.')

# ---------------- 1715059 FBH 2016 G8 P2
b.add(1715059,1,r'''Find all positive integers divisible by $8$ whose digits have sum $7$ and product $6$.''',
r'''The product of the digits is $6$, so no digit is $0$, and the digits greater than $1$ are $6$ alone, or $2$ and $3$. The digit $1$ does not change the product, and the sum $7$ fixes the number of $1$'s:
\begin{itemize}
\item digits $6,1$ (sum $7$): the numbers $16$ and $61$;
\item digits $2,3,1,1$ (sum $7$): the twelve arrangements of $1,1,2,3$.
\end{itemize}
A multiple of $8$ is even, so it must end in $6$ or $2$. From the first group, $16=8\cdot2$ works. From the second group the candidates end in $2$: $1132$, $1312$, $3112$. A number is divisible by $8$ exactly when its last three digits are: $132=8\cdot16.5$ fails, while $312=8\cdot39$ and $112=8\cdot14$ work.

The numbers are $\boxed{16,\ 1312,\ 3112}$.''',
'Divisibility rules|Digit problems|Casework',3,source=FBH(2016,8,2),
note='Checked by searching all numbers below 10^7.')

# ---------------- 1715027 FBH 2016 G6 P1
b.add(1715027,1,r'''Find all digits $a$ and $b$ such that the five-digit number $\overline{a783b}$ is divisible by $56$.''',
r'''Since $56=8\cdot7$ with $\gcd(7,8)=1$, the number must be divisible by $8$ and by $7$.

\textbf{Divisibility by $8$.} The last three digits $\overline{83b}=830+b$ must be a multiple of $8$. As $830=8\cdot103+6$, we need $b+6\equiv0\pmod 8$, so $b=2$ ($832=8\cdot104$).

\textbf{Divisibility by $7$.} Now $\overline{a7832}=10000a+7832$. Since $10000=7\cdot1428+4$ and $7832=7\cdot1118+6$, we need $4a+6\equiv0\pmod7$, i.e.\ $4a\equiv1\pmod 7$, so $a\equiv2\pmod7$. With $a$ a nonzero digit, $a=2$ or $a=9$.

So the possibilities are $\boxed{a=2,\ b=2\ (27832=56\cdot497)\ \text{and}\ a=9,\ b=2\ (97832=56\cdot1747)}$.''',
'Divisibility rules|Remainders and congruences|Digit problems',3,source=FBH(2016,6,1))

# ---------------- 1715038 FBH 2016 G6 P5 torn leaves
b.add(1715038,1,r'''The pages of a book are numbered $1$ to $100$, so each sheet (leaf) carries two consecutive pages $2k-1$ and $2k$ on its two sides. Several sheets were torn out of the book, and the sum of the page numbers on the torn-out sheets is $4949$. How many sheets were torn out?''',
r'''Sheet $k$ ($1\le k\le50$) carries pages $2k-1$ and $2k$, with sum $4k-1$. The sum of all page numbers is $1+2+\cdots+100=5050$, so the sheets that remain have page sum $5050-4949=101$.

If $m$ sheets $k_1<\dots<k_m$ remain, their page sum is $4(k_1+\cdots+k_m)-m=101$. So $m\equiv-101\equiv3\pmod 4$ and $k_1+\cdots+k_m=\dfrac{101+m}{4}$.
\begin{itemize}
\item $m=3$: $k_1+k_2+k_3=26$, possible (for example $k=1,2,23$).
\item $m\ge7$: then $k_1+\cdots+k_m\ge1+2+\cdots+m=\dfrac{m(m+1)}2$, but $\dfrac{m(m+1)}{2}>\dfrac{101+m}{4}$ for $m\ge7$ (already $28>27$ at $m=7$). Impossible.
\end{itemize}
So $3$ sheets remain and $50-3=\boxed{47}$ sheets were torn out.''',
'Arithmetic sequences|Remainders and congruences|Summation|Bounding and extremal cases',4,source=FBH(2016,6,5),
note='"Double pages" is read as sheets (leaves) carrying pages 2k-1 and 2k, and the sum 4949 as the sum of the torn-out pages, as written. (If 4949 were the sum of the remaining pages, the same argument would give 3 sheets torn out.) Checked by exhaustive search over the number of sheets.')

# ---------------- 1714156 sum of first 50 even integers
b.add(1714156,1,r'''What is the sum of the first $50$ positive even integers?''',
r'''\[
2+4+\cdots+100=2(1+2+\cdots+50)=2\cdot\dfrac{50\cdot51}{2}=\boxed{2550}.
\]''',
'Arithmetic sequences|Summation',1)

# ---------------- 1714863 ANGELA
b.add(1714863,1,r'''In how many ways can you arrange the letters of the name ANGELA?''',
r'''ANGELA has $6$ letters, with A appearing twice and N, G, E, L once each. Arrangements that differ only by swapping the two A's are the same, so the number of arrangements is
\[
\dfrac{6!}{2!}=\dfrac{720}{2}=\boxed{360}.
\]''',
'Multiset permutations|Permutations',1,source=src('Math Is Cool',None,None,None))

# ---------------- 1714665 square table (alias)
b.add(1714665,1,r'''How many distinct ways are there to seat $8$ people around a square table with $2$ people on each side, if seatings that differ by a rotation of the table are the same?''',
r'''There are $8!$ ways to fill the $8$ seats. Each seating has exactly $4$ rotations of the table ($0^\circ,90^\circ,180^\circ,270^\circ$), all giving different seat assignments, so there are $\dfrac{8!}{4}=\boxed{10080}$ seatings. The poster's answer $10080$ is correct.''',
'Circular arrangements|Permutations|Symmetry',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1570243 intersection points of lines through n points
b.add(1570243,1,r'''There are $n$ points in a plane. Each pair of them is joined by a line (extended indefinitely in both directions). Suppose no two of these lines are parallel or coincide, and no three of them pass through the same point, except at the $n$ given points. Find the number of points of intersection of the lines other than the $n$ given points.''',
r'''There are $\dbinom n2$ lines. Since no two are parallel, every pair of lines meets in exactly one point. Two lines meet at one of the given points exactly when they share an endpoint; through each given point pass $n-1$ lines, which form $\dbinom{n-1}2$ pairs. All other pairs of lines meet at distinct new points (no three lines are concurrent away from the given points).

Alternatively count the new points directly: two lines meet at a new point exactly when their four endpoints are distinct. Any $4$ of the given points determine $3$ ways to split them into two pairs, i.e.\ $3$ pairs of lines with no common endpoint. Hence the number of new intersection points is
\[
3\dbinom n4=\boxed{\dfrac{n(n-1)(n-2)(n-3)}{8}}.
\]
This agrees with the first count: $\dbinom{\binom n2}{2}-n\dbinom{n-1}{2}=3\dbinom n4$. For example, $4$ points give $6$ lines and $3$ new intersection points.''',
'Counting intersections|Combinations|Combinatorial identities and binomial coefficients',4,
note='The general-position wording is kept; the identity C(C(n,2),2) - n C(n-1,2) = 3 C(n,4) is checked for n up to 40 and the count by explicit random point sets for small n.')

# ---------------- 1711485 fence around equilateral triangle
fig=r'''pair A=(0,0),B=(6,0),C=6*dir(60);
real d=6;
pair[] V={A,B,C};
draw(A--B--C--cycle,linewidth(0.9));
pen fp=blue+linewidth(1.1);
for(int i=0;i<3;++i){
  pair P=V[i],Q=V[(i+1)%3];
  pair nrm=unit(rotate(-90)*(Q-P));
  draw(P+d*nrm--Q+d*nrm,fp);
  pair R=V[(i+2)%3];
  pair n0=unit(rotate(-90)*(P-R));
  real a1=degrees(n0),a2=degrees(nrm);
  if(a2<a1) a2+=360;
  draw(arc(P,d,a1,a2),fp);
}
pair n1=unit(rotate(-90)*(B-A));
draw(A--A+d*n1,dashed);draw(A--A+d*unit(rotate(-90)*(A-C)),dashed);
label("$6$",A+0.5*d*n1,E);
label("$6$",(A+B)/2,N);
label("$A$",A,dir(210));label("$B$",B,dir(330));label("$C$",C,N);'''
b.add(1711485,1,r'''Johnny is building a fence around his dog house. The dog house is an equilateral triangle with side length $6$ inches, and every point of the fence is exactly $6$ inches from the dog house (that is, from the nearest point of its sides). What is the total length of the fence, in inches?''',
r'''The points at distance $6$ from the triangle form three straight pieces and three circular arcs.
\begin{itemize}
\item Opposite each side, the fence is a segment parallel to that side at distance $6$, with the same length $6$. These give $3\cdot6=18$ inches.
\item Around each vertex, the fence is an arc of radius $6$ centred at the vertex, joining the ends of the two adjacent straight pieces. Its angle is $360^\circ-90^\circ-90^\circ-60^\circ=120^\circ$, so the three arcs together make $360^\circ$: one full circle of radius $6$, of length $12\pi$.
\end{itemize}
'''+asy(fig,'5.5cm')+r'''
The fence has length $\boxed{18+12\pi}$ inches (about $55.7$ inches).''',
'Circles|Equilateral triangles|Lengths, perimeter, and area|Loci and geometric constraints',3,
note='"Exactly 6 inches away from the sides" is read as distance 6 from the triangle (outside it).')

# ---------------- 1714155 Nora and Mary
b.add(1714155,1,r'''Three years ago, Nora was half as old as Mary is now. If Mary is four years older than Nora, how old is Mary now?''',
r'''Let Nora be $n$ years old now; then Mary is $n+4$. The condition says $n-3=\dfrac{n+4}{2}$, so $2n-6=n+4$ and $n=10$. Mary is $\boxed{14}$ years old. (Check: three years ago Nora was $7$, half of $14$.)''',
'Age problems|Linear equations',1,
note='The doubled word in "Three three years ago" is a typo.')

# ---------------- 1713999 glide reflection (alias)
b.add(1713999,1,r'''In the figure, $AB=DA=5$ units, $AC=DE=4$ units and $BC=AE=3$ units, and point $C$ lies on segment $AD$. It is possible to move triangle $ABC$ onto triangle $DAE$ by reflecting it across a line $m$ and then translating the image in a direction parallel to $m$. Line $m$ divides triangle $ABC$ into two regions. What is the ratio of the area of the smaller region to the area of the larger region? Express your answer as a common fraction.''',
r'''Put $A=(0,0)$, $D=(5,0)$, $C=(4,0)$, $B=(4,3)$; then $E=\left(\dfrac95,-\dfrac{12}5\right)$. The axis of a glide reflection passes through the midpoints of $AD$, $BA$ and $CE$, namely $(2.5,0)$, $(2,1.5)$, $(2.9,-1.2)$, all on $y=-3x+7.5$. It cuts off from triangle $ABC$ the triangle with vertices $A$, $(2,1.5)$, $(2.5,0)$, of area $\dfrac{15}{8}$; the rest has area $6-\dfrac{15}8=\dfrac{33}8$. The ratio is $\boxed{\dfrac{5}{11}}$.''',
'Reflections|Translations|Coordinate geometry|Area ratios',5,
note='Repeat of an earlier record (aliased); official answer 5/11.')

# ---------------- 1712630 area of DEF
fig=RA+r'''pair A=(0,0),C=(10,0),B=(0.2,sqrt(528.96));
pair D=(B+C)/2,Ep=(B.x,0),F=A+(2/7)*(B-A);
filldraw(D--Ep--F--cycle,rgb(1,0.85,0.85),red+linewidth(0.8));
draw(A--B--C--cycle,linewidth(0.9));
draw(A--D,dashed+gray);draw(C--F,dashed+gray);
dot(D);dot(Ep);dot(F);
label("$A$",A,dir(-135));label("$B$",B,N);label("$C$",C,SE);
label("$D$",D,NE);label("$E$",Ep,dir(-45));label("$F$",F,W);
label("$23$",(A+B)/2+(0,4),W);label("$25$",(B+C)/2+(0.6,3),NE);label("$10$",(A+C)/2+(1.5,0),S);'''
b.add(1712630,1,r'''Triangle $ABC$ has $AB=23$, $AC=10$ and $BC=25$. Let $D$ be the foot of the median from $A$ (the midpoint of $BC$), $E$ the foot of the altitude from $B$ to $AC$, and $F$ the foot of the angle bisector from $C$ on $AB$. Find the area of triangle $DEF$.''',
r'''Place $A=(0,0)$ and $C=(10,0)$, and let $B=(p,q)$ with $q>0$. Then $p^2+q^2=529$ and $(p-10)^2+q^2=625$; subtracting gives $-20p+100=96$, so $p=\dfrac15$ and
\[
q^2=529-\dfrac1{25}=\dfrac{13224}{25},\qquad q=\dfrac{2\sqrt{3306}}{5}
\]
(as $13224=4\cdot3306$). Now:
\begin{itemize}
\item $D=\dfrac{B+C}{2}=\left(\dfrac{51}{10},\dfrac q2\right)$;
\item $E=\left(\dfrac15,0\right)$, since $AC$ lies on the $x$-axis (and $0<\dfrac15<10$, so $E$ is on side $AC$);
\item by the angle bisector theorem $\dfrac{AF}{FB}=\dfrac{CA}{CB}=\dfrac{10}{25}=\dfrac25$, so $F=\dfrac27B=\left(\dfrac{2}{35},\dfrac{2q}{7}\right)$.
\end{itemize}
'''+asy(fig,'4.5cm')+r'''
With $D-E=\left(\dfrac{49}{10},\dfrac q2\right)$ and $F-E=\left(-\dfrac17,\dfrac{2q}7\right)$,
\[
[DEF]=\dfrac12\left|\dfrac{49}{10}\cdot\dfrac{2q}{7}-\dfrac q2\cdot\left(-\dfrac17\right)\right|=\dfrac12\left(\dfrac{7q}{5}+\dfrac{q}{14}\right)=\dfrac12\cdot\dfrac{103q}{70}=\dfrac{103q}{140}.
\]
Substituting $q=\dfrac{2\sqrt{3306}}5$:
\[
[DEF]=\dfrac{103\cdot2\sqrt{3306}}{700}=\boxed{\dfrac{103\sqrt{3306}}{350}}\approx16.92 .
\]''',
'Coordinate geometry|Angle bisector theorem|Medians and centroids|Altitudes|Shoelace formula|Triangles',5,
note='The post gives five answer choices (3125 sqrt1653/8057, 25 sqrt1653/49, 343 sqrt1653/625, 7 sqrt551/5, 2147 sqrt3306/3500) and no key; none of them equals the area, which is 103 sqrt3306/350 (about 16.92; the choices are about 15.77, 20.74, 22.31, 32.86, 35.27). The record is free response. Checked with exact and floating-point coordinates.')

# ---------------- 1712753 AK:KN (alias)
b.add(1712753,1,r'''In triangle $ABC$, $AB=11$, $BC=12$ and $CA=13$. Let $M$ be the midpoint of $AC$ and let $N$ be the point on $BC$ such that $AN\perp BC$. If segments $BM$ and $AN$ intersect at $K$, find the ratio $AK:KN$.''',
r'''With $B=(0,0)$, $C=(12,0)$: $A=(4,\sqrt{105})$, $N=(4,0)$, $M=\left(8,\dfrac{\sqrt{105}}2\right)$. Line $BM$ meets $x=4$ at $K=\left(4,\dfrac{\sqrt{105}}{4}\right)$, so $AK:KN=\dfrac34\sqrt{105}:\dfrac14\sqrt{105}=\boxed{3:1}$.''',
'Coordinate geometry|Altitudes|Midpoints|Triangles',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1714043 mutilated chessboard (alias)
b.add(1714043,1,r'''Two diagonally opposite corner squares are removed from an $8\times8$ chessboard. Prove that the remaining $62$ squares cannot be covered by $31$ dominoes, each covering two adjacent squares.''',
r'''Opposite corners have the same colour, so the remaining board has $30$ squares of one colour and $32$ of the other. Each domino covers one black and one white square, so $31$ dominoes cover $31$ of each colour. Impossible. $\blacksquare$''',
'Colourings, tilings, and coverings|Invariants and monovariants',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1713813 x^2+1 >= 0
b.add(1713813,1,r'''Prove that if $y=x^2+1$ for a real number $x$, then $y\ge0$. (In fact, prove $y\ge1$.)''',
r'''For every real $x$, $x^2\ge0$: if $x\ge0$ then $x^2=x\cdot x\ge0$, and if $x<0$ then $x^2=(-x)(-x)>0$. Hence
\[
y=x^2+1\ge0+1=1>0 .
\]
So $y\ge1$, and in particular $y\ge0$, with $y=1$ exactly when $x=0$. $\blacksquare$''',
'Inequalities|Perfect squares',1,
note='The post asks to prove y >= 0; the record also asks for the sharper bound y >= 1. x is taken to be real.')

# ---------------- 1713859 sequence with typo (alias)
b.add(1713859,1,r'''In the sequence $-1,1,4,8,\dots$, each term after the first is $n$ more than the previous term, where $n$ is its position. Find $(a_{2018}-a_{2017})+(a_{2017}-a_{2016})+\cdots+(a_2-a_1)$.''',
r'''The sum telescopes to $a_{2018}-a_1=\sum_{k=2}^{2018}k=\dfrac{2018\cdot2019}2-1=\boxed{2037170}$.''',
'Telescoping sums|Arithmetic sequences|Summation',2,
note='The post writes the sequence as 1, 1, 4, 8, ..., where the first term 1 contradicts the rule (it would make the second term 3); the poster reposted the problem with first term -1 (topic 1715130). Aliased to that copy.')

b.save()
