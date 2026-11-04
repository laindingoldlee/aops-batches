from qb import *
b=Bank('p233_02')

RA=r'''void ra(pair P,pair Q,pair R,real s){pair u=unit(Q-P),v=unit(R-P);draw(P+s*u--P+s*u+s*v--P+s*v,linewidth(0.5));}
'''

# ---------------- 1720756 problem 2: closer to origin than (4,4)
fig=r'''pair O=(0,0),P=(4,4);
fill((0,1)--(3,1)--(0,4)--cycle,lightgray);
draw((-0.6,0)--(6,0),Arrow(TeXHead));draw((0,-0.6)--(0,6.8),Arrow(TeXHead));
draw((0,1)--(5,1)--(5,6)--(0,6)--cycle,linewidth(0.9));
draw((0,4)--(4.6,-0.6),dashed+blue);
draw(O--P,dotted);
dot(O);dot(P);dot((3,1));dot((0,4));
label("$O$",O,SW);label("$(4,4)$",P,N);
label("$(3,1)$",(3,1),dir(-125));label("$(0,4)$",(0,4),W);label("$(0,1)$",(0,1),W);label("$(5,6)$",(5,6),NE);
label("$x+y=4$",(4.6,-0.6),SE,blue);
label("$x$",(6,0),N);label("$y$",(0,6.8),E);'''
b.add(1720756,2,r'''Consider the rectangular region with vertices $(0,1)$, $(0,6)$, $(5,1)$ and $(5,6)$. A point is chosen at random from this region. What is the probability, as a percent, that it is closer to the origin than to the point $(4,4)$?''',
r'''A point $(x,y)$ is closer to $O=(0,0)$ than to $(4,4)$ when
\[
x^2+y^2<(x-4)^2+(y-4)^2\iff 0<-8x-8y+32\iff x+y<4 ,
\]
i.e.\ it lies on the origin's side of the perpendicular bisector $x+y=4$ of the segment from $O$ to $(4,4)$.
'''+asy(fig,'6cm')+r'''
The region is the $5\times5$ square $0\le x\le5$, $1\le y\le6$ of area $25$. The part of it with $x+y<4$ is the shaded right triangle with vertices $(0,1)$, $(3,1)$, $(0,4)$, with legs $3$ and $3$ and area $\dfrac92$. The probability is
\[
\dfrac{\ \dfrac92\ }{25}=\dfrac{9}{50}=\boxed{18\%}.
\]''',
'Geometric probability|Coordinate geometry|Perpendicular bisectors|Percentages',3,
note='Problem 2 of the post (answer 18% as given). Problem 1 (ellipse with foci (0,0) and (-8,8) through (3,4); ratio of y-intercepts m/n with |m+n| = 8) is dropped: with these data the y-intercepts are about -3.057 and 8.676, whose ratio is irrational, so the stated data or answer are wrong and the intended data cannot be recovered.')

# ---------------- 1719974 absolute value system
b.add(1719974,1,r'''Solve the system
\[
|x-5|>3,\qquad (x-5)^2<25 .
\]''',
r'''Since $(x-5)^2=|x-5|^2$ and both sides are non-negative, $(x-5)^2<25\iff|x-5|<5$. So the system says
\[
3<|x-5|<5,
\]
i.e.\ the distance from $x$ to $5$ is between $3$ and $5$. Either $3<x-5<5$, giving $8<x<10$, or $3<5-x<5$, giving $0<x<2$. The solution is
\[
\boxed{0<x<2\ \text{ or }\ 8<x<10}.
\]''',
'Absolute value|Inequalities',2)

# ---------------- 1719786 coins fewer than eight
b.add(1719786,1,r'''In cents, what is the least amount that cannot be obtained using fewer than eight coins from a collection of pennies ($1$ cent), nickels ($5$ cents), dimes ($10$ cents) and quarters ($25$ cents)?''',
r'''\textbf{Every amount up to $68$ cents needs at most $7$ coins.} Write $n=25q+r$ with $0\le r\le24$. The remainder $r$ can be paid with at most $2$ dimes, at most $1$ nickel and at most $4$ pennies; this uses at most $5$ coins unless $r=19$ or $r=24$ (each of which uses $6$). If $n\le49$ then $q\le1$ and at most $1+6=7$ coins are used. If $50\le n\le68$ then $q=2$ and $r\le18$, so at most $2+5=7$ coins are used.

\textbf{$69$ cents needs $8$ coins.} The number of pennies must be $\equiv4\pmod5$, since all other coins are multiples of $5$. With $4$ pennies, the remaining $65$ cents would have to be made from at most $3$ coins of $5,10,25$; but $25+25+10=60$ and $25+25+25=75$ are the only sums of three such coins between $55$ and $75$ (others are smaller), and two or fewer such coins give at most $50$. With $9$ or more pennies we already have too many coins after adding the coins needed for the remaining $60$ cents (at least $3$). So $69$ needs at least $8$ coins ($25+25+10+5+1+1+1+1$).

The answer is $\boxed{69}$ cents.''',
'Money and currency|Casework|Bounding and extremal cases',4,source=src('MATHCOUNTS',2018,'School',25,rnd='Sprint'),
note='Repeat of an earlier record (aliased). 2018 MATHCOUNTS School Sprint #25 (number from the earlier record of the same problem). Answer checked by brute force over all coin combinations.')

# ---------------- 1719663 occurrences of 2013
b.add(1719663,1,r'''The numbers from $1$ to $30000$ are written one after another to form a long string of digits:
\[
123456789101112\cdots2999930000 .
\]
How many times does the block $2013$ occur in this string?''',
r'''An occurrence of $2013$ either lies inside one number or is split between two consecutive numbers $n$ and $n+1$ (a number with at least two digits is longer than the remaining part, so at most two numbers are involved).

\textbf{Inside one number.} The numbers up to $30000$ containing $2013$ are $2013$, $12013$, $22013$ and $20130,20131,\dots,20139$: $13$ occurrences.

\textbf{Split as $2|013$.} Then $n+1$ would begin with $0$: impossible.

\textbf{Split as $20|13$.} Then $n$ ends in $20$ and $n+1$ (ending in $21$) begins with $13$: $n+1=1321$ or $n+1=13d21$ for $d=0,\dots,9$. That is $11$ occurrences ($1320|1321$ and $13d20|13d21$).

\textbf{Split as $201|3$.} Then $n$ ends in $201$ and $n+1$ (ending in $202$) begins with $3$: only $n+1=3202$ (the next candidate $30202$ exceeds $30000$). That is $1$ occurrence.

Total: $13+11+1=\boxed{25}$.''',
'Digit problems|Casework|Systematic counting',5,
note='Checked by searching the actual string.')

# ---------------- 1640117 3-digit even numbers
b.add(1640117,1,r'''How many $3$-digit even numbers have all three digits different?''',
r'''Count by the units digit.
\begin{itemize}
\item Units digit $0$: the hundreds digit has $9$ choices and the tens digit $8$: $72$.
\item Units digit $2$, $4$, $6$ or $8$: the hundreds digit cannot be $0$ or the units digit ($8$ choices) and the tens digit has $8$ choices: $4\cdot64=256$.
\end{itemize}
Total $72+256=\boxed{328}$.''',
'Multiplication principle|Casework|Arrangements with restrictions',2)
b.add(1640117,2,r'''How many $3$-digit even numbers can be written using the digits $0,1,2,3,4,5,6$,
\begin{enumerate}
\item[(i)] if digits may be repeated;
\item[(ii)] if all three digits must be different?
\end{enumerate}''',
r'''\textbf{(i)} The hundreds digit can be $1$--$6$ ($6$ choices), the tens digit any of the $7$ digits, and the units digit $0,2,4$ or $6$ ($4$ choices): $6\cdot7\cdot4=\boxed{168}$.

\textbf{(ii)} If the units digit is $0$: $6$ choices for the hundreds digit and $5$ for the tens: $30$. If the units digit is $2$, $4$ or $6$: the hundreds digit cannot be $0$ or the units digit ($5$ choices) and the tens digit has $5$ choices: $3\cdot25=75$. Total $\boxed{105}$.''',
'Multiplication principle|Casework|Arrangements with restrictions',2,
note='Part (b) of the post does not say whether digits may repeat; the record asks for both readings.')

# ---------------- 1603119 BANANA
b.add(1603119,1,r'''How many arrangements are there of the letters of the word BANANA?''',
r'''BANANA has $6$ letters: three A's, two N's and one B. The number of distinct arrangements is
\[
\dfrac{6!}{3!\,2!\,1!}=\dfrac{720}{12}=\boxed{60}.
\]''',
'Multiset permutations|Permutations',1,
note='P1 of a counting marathon (only P1 is in the post).')

# ---------------- 1707844 pentagon diagonals marked dots
QF=r'''pair[] V; for(int i=0;i<5;++i) V.push(dir(90+72*i));
draw(V[0]--V[1]--V[2]--V[3]--V[4]--cycle,gray+linewidth(0.5));
for(int i=0;i<5;++i) draw(V[i]--V[(i+2)%5],linewidth(0.9));
for(int i=0;i<5;++i){dot(V[i],linewidth(4));
 pair X=extension(V[i],V[(i+2)%5],V[(i+1)%5],V[(i+3)%5]); dot(X,linewidth(4));}'''
b.add(1707844,1,r'''The $5$ diagonals of a convex pentagon are drawn. They meet in $10$ points: the $5$ vertices (where two diagonals meet) and the $5$ points where two diagonals cross inside the pentagon.
'''+asy(QF,'4cm')+r'''
We want to mark $5$ of these $10$ points so that each of the $5$ diagonals contains exactly $2$ marked points. In how many ways can this be done?''',
r'''Each of the $10$ points lies on exactly two diagonals, and conversely any two of the $5$ diagonals meet in exactly one of the $10$ points (two diagonals with a common endpoint meet at that vertex; two without one cross inside the pentagon). There are $\binom52=10$ pairs of diagonals, so the points correspond exactly to the pairs of diagonals.

Think of the diagonals as $5$ vertices of a graph and of each marked point as an edge joining the two diagonals through it. A marking is then a set of $5$ edges of the complete graph $K_5$, and the condition says that every vertex has degree exactly $2$. A graph in which every vertex has degree $2$ is a union of disjoint cycles, each of length at least $3$; with $5$ vertices the only possibility is a single cycle through all $5$ vertices.

The number of cycles through all $5$ vertices of $K_5$ is $\dfrac{4!}{2}=12$ (arrange the vertices in a circle: $4!$ orders starting from a fixed vertex, divided by $2$ for the direction). So there are $\boxed{12}$ ways.

(For example, marking all $5$ vertices or all $5$ inner crossing points both work.)''',
'Graph theory|Bijections|Counting principles',5,
note='Checked by brute force over all 252 sets of 5 points.')

# ---------------- 1601848 last two digits of sum of factorials
b.add(1601848,1,r'''Find the last two digits of $1!+2!+3!+\dots+66!$.''',
r'''For $n\ge10$, $n!$ contains the factors $2\cdot5$ and $10$, so it is divisible by $100$ and does not affect the last two digits. Hence we only need
\[
1!+2!+\dots+9!=1+2+6+24+120+720+5040+40320+362880=409113 .
\]
The last two digits are $\boxed{13}$.''',
'Factorials|Units digits and last digits|Remainders and congruences',2)

# ---------------- 1630167 7-digit integers from 0-6
b.add(1630167,1,r'''How many different positive $7$-digit integers can be formed if each digit in the set $\{0,1,2,3,4,5,6\}$ is used exactly once?''',
r'''There are $7!$ orderings of the seven digits, and those starting with $0$ are not $7$-digit integers. By symmetry, $0$ is first in $\dfrac17$ of the orderings. So the count is $7!-6!=6\cdot6!=\boxed{4320}$.''',
'Permutations|Complementary counting',1)

# ---------------- 1719597 product of digits even
b.add(1719597,1,r'''An integer $n$ is chosen at random with $1000\le n\le9999$. What is the probability that the product of its digits is even?''',
r'''Use the complement. The product of the digits is odd exactly when all four digits are odd. Each of the four digits then has $5$ choices ($1,3,5,7,9$; none is $0$, so the leading digit is allowed), giving $5^4=625$ such numbers out of $9000$. The probability that the product is even is
\[
1-\dfrac{625}{9000}=1-\dfrac{5}{72}=\boxed{\dfrac{67}{72}}.
\]''',
'Complementary probability|Parity|Probability|Digit problems',2,
note='Repeat of an earlier record (aliased). The poster tried casework on the position of an even digit; the complement avoids it.')

# ---------------- 1719574 AMC 10A 2017 #17
fig=r'''draw(circle((0,0),5),gray+linewidth(0.6));
draw((-6,0)--(6,0),linewidth(0.4));draw((0,-6)--(0,6),linewidth(0.4));
pair[] L={(3,4),(4,3),(5,0),(4,-3),(3,-4),(0,-5),(-3,-4),(-4,-3),(-5,0),(-4,3),(-3,4),(0,5)};
for(pair p: L) dot(p);
pair P=(-4,3),Q=(3,-4),R=(3,4),T=(4,3);
draw(P--Q,blue+linewidth(0.9));draw(R--T,red+linewidth(0.9));
label("$P$",P,NW);label("$Q$",Q,SE);label("$R$",R,N);label("$S$",T,E);'''
b.add(1719574,1,r'''Distinct points $P$, $Q$, $R$, $S$ lie on the circle $x^2+y^2=25$ and have integer coordinates. The distances $PQ$ and $RS$ are irrational numbers. What is the greatest possible value of the ratio $\dfrac{PQ}{RS}$?

$\textbf{(A)}\ 3\qquad\textbf{(B)}\ 5\qquad\textbf{(C)}\ 3\sqrt5\qquad\textbf{(D)}\ 7\qquad\textbf{(E)}\ 5\sqrt2$

A student argues that $P=(-4,3)$ and $Q=(4,-3)$ give $PQ=10$, so the answer is $\dfrac{10}{\sqrt2}=5\sqrt2$. Find the error.''',
r'''The lattice points on the circle are $(\pm3,\pm4)$, $(\pm4,\pm3)$, $(0,\pm5)$, $(\pm5,0)$. For two of them, $X=(x_1,y_1)$ and $Y=(x_2,y_2)$,
\[
XY^2=x_1^2+y_1^2+x_2^2+y_2^2-2(x_1x_2+y_1y_2)=50-2(x_1x_2+y_1y_2),
\]
an even integer between $2$ and $100$.
\begin{itemize}
\item $PQ$ must be irrational, so $PQ^2$ is not a perfect square; in particular $PQ^2\ne100$ (diametrically opposite points give the rational distance $10$). The largest even value below $100$ is $98$, attained by $P=(-4,3)$, $Q=(3,-4)$: $7^2+7^2=98$.
\item $RS^2$ is at least $2$, attained by $R=(3,4)$, $S=(4,3)$, and $\sqrt2$ is irrational.
\end{itemize}
'''+asy(fig,'5cm')+r'''
So the greatest ratio is $\dfrac{\sqrt{98}}{\sqrt2}=\sqrt{49}=7$, answer $\boxed{\textbf{(D)}\ 7}$.

The student's error: $PQ=10$ is rational, which the problem forbids. That is exactly why the solution uses the nearly opposite points $(-4,3)$ and $(3,-4)$ instead of the opposite points $(-4,3)$ and $(4,-3)$.''',
'Lattice points|Distance formula|Circles|Coordinate geometry|Radicals',4,source=src('AMC 10',2017,'A',17),
note='The poster believed the official solution was wrong and the answer is 5 sqrt 2; it is not, because PQ = 10 is rational. The record asks for the answer (D) 7 and for the error. Checked by brute force over all lattice-point pairs.')

# ---------------- 1719242 rotation of a line
fig=RA+r'''pair O=(0,0),F=(0,-2),Fp=rotate(60)*F;
pair u=unit(Fp); pair d=rotate(90)*u;
pair P=extension(F,F+(1,0),Fp,Fp+d);
draw((-1.6,-2)--(3.2,-2),linewidth(0.9));
draw(Fp-1.6*d--Fp+1.9*d,linewidth(0.9)+deepgreen);
draw(O--F,dashed);draw(O--Fp,dashed);
ra(F,O,P,0.22);ra(Fp,O,P,0.22);
draw(arc(O,0.55,-90,-30),linewidth(0.6));label("$a$",O+0.85*dir(-60));
draw(arc(P,0.45,0,60),linewidth(0.6));label("$a$",P+0.75*dir(30));
dot(O);dot(F);dot(Fp);dot(P);
label("$O$",O,N);label("$F$",F,S);label("$F'$",Fp,dir(-20));label("$P$",P,dir(-60));
label("$l$",(-1.6,-2),W);label("$l'$",Fp+1.9*d,N,deepgreen);'''
b.add(1719242,1,r'''A line $l$ is rotated about a point $O$ through an angle of measure $a$, where $0^\circ<a<180^\circ$, to give a line $l'$. Show that $l$ and $l'$ intersect, and that one of the angles between them has measure $a$.''',
r'''\textbf{Case 1: $O$ lies on $l$.} Then $O$ is fixed by the rotation, so $l'$ also passes through $O$, and the ray of $l$ starting at $O$ in a chosen direction is turned through the angle $a$ into a ray of $l'$. So $l$ and $l'$ meet at $O$ at the angle $a$.

\textbf{Case 2: $O$ is not on $l$.} Let $F$ be the foot of the perpendicular from $O$ to $l$, and let $F'$ be the image of $F$. A rotation preserves distances and angles, so $OF'=OF$, $OF'\perp l'$ and $F'$ is the foot of the perpendicular from $O$ to $l'$; moreover $\angle FOF'=a$.

Turning a line through $90^\circ$ about any point gives a line perpendicular to it. Turn line $OF$ through $90^\circ$: the result is parallel to $l$. Turn line $OF'$ through $90^\circ$ in the same sense: the result is parallel to $l'$. Since line $OF'$ is line $OF$ turned through $a$, the line parallel to $l'$ is the line parallel to $l$ turned through $a$. As $0^\circ<a<180^\circ$, these directions are different, so $l$ and $l'$ are not parallel and meet at a point $P$; and the two lines through $P$ make the angles $a$ and $180^\circ-a$ with each other. So one of the angles between $l$ and $l'$ is $a$. $\blacksquare$
'''+asy(fig,'5.5cm')+r'''
In the figure ($a=60^\circ$) the quadrilateral $OFPF'$ has right angles at $F$ and $F'$, so $\angle FPF'=360^\circ-90^\circ-90^\circ-a=180^\circ-a$, and the angle between $l'$ and the extension of $FP$ beyond $P$ is $a$.''',
'Rotations|Geometric transformations|Angles and lines|Perpendicular lines',3,
note='The post asks to show that l and l\' "intersect in an angle with measure a"; the record restricts to 0 < a < 180 degrees (for a = 180 the lines are parallel or equal) and reads the claim as: one of the angles formed is a.')

# ---------------- 1719384 phi(x)=24
b.add(1719384,1,r'''Find a natural number $x$ such that (i) the prime factors of $x$ are exactly $3$ and $5$, and (ii) $\varphi(x)=24$, where $\varphi$ is Euler's totient function.''',
r'''Write $x=3^m5^n$ with $m,n\ge1$. Then
\[
\varphi(x)=3^{m-1}(3-1)\cdot5^{n-1}(5-1)=8\cdot3^{m-1}5^{n-1}.
\]
Setting this equal to $24$ gives $3^{m-1}5^{n-1}=3$, so $m=2$ and $n=1$. Hence $x=9\cdot5=\boxed{45}$, and it is the only such number. Check: the numbers up to $45$ coprime to $45$ number $45\cdot\dfrac23\cdot\dfrac45=24$.''',
"Euler's theorem and totient|Prime factorisation",2)

# ---------------- 1719274 telescoping
b.add(1719274,1,r'''Find
\[
\dfrac{1}{1\cdot2\cdot3}+\dfrac{1}{2\cdot3\cdot4}+\dfrac{1}{3\cdot4\cdot5}+\dots+\dfrac{1}{98\cdot99\cdot100}.
\]''',
r'''Since $\dfrac{1}{n(n+1)}-\dfrac{1}{(n+1)(n+2)}=\dfrac{(n+2)-n}{n(n+1)(n+2)}=\dfrac{2}{n(n+1)(n+2)}$,
\[
\dfrac{1}{n(n+1)(n+2)}=\dfrac12\left(\dfrac{1}{n(n+1)}-\dfrac{1}{(n+1)(n+2)}\right).
\]
Summing from $n=1$ to $98$, the sum telescopes:
\[
\dfrac12\left(\dfrac{1}{1\cdot2}-\dfrac{1}{99\cdot100}\right)=\dfrac14-\dfrac{1}{19800}=\boxed{\dfrac{4949}{19800}}.
\]''',
'Telescoping sums|Partial fractions|Summation',3,
note='The title says "geometric series" but the sum is telescoping. Checked with exact fractions.')

# ---------------- 1718720 MAXIMUM
b.add(1718720,1,r'''In how many ways can the letters of the word MAXIMUM be arranged so that no two M's are next to each other?''',
r'''MAXIMUM has three M's and the four different letters A, X, I, U. First arrange A, X, I, U in a row: $4!=24$ ways. This creates $5$ gaps (before, between and after them), and the M's must go into $3$ different gaps: $\binom53=10$ ways. Total $24\cdot10=\boxed{240}$.''',
'Arrangements with restrictions|Multiset permutations|Combinations',3)

# ---------------- 1718086 trains
b.add(1718086,1,r'''A train $1000$ feet long is going east at $20$ mph. On a parallel track another train is going west at $40$ mph. The trains take $30$ seconds to pass each other completely. How many feet long is the second train?''',
r'''The trains approach each other at the relative speed $20+40=60$ mph $=60\cdot\dfrac{5280}{3600}=88$ feet per second. From the moment the fronts meet until the backs separate, the total relative distance covered is the sum of the two lengths. In $30$ seconds this is $88\cdot30=2640$ feet, so the second train is $2640-1000=\boxed{1640}$ feet long.''',
'Relative speed|Unit conversion|Distance, rate, and time',2)

# ---------------- 1711163 ELEMENT
b.add(1711163,1,r'''If the letters of the word ELEMENT are randomly arranged, what is the probability that the three E's are consecutive? Express your answer as a common fraction.''',
r'''ELEMENT has $7$ letters: three E's and L, M, N, T. The number of distinct arrangements is $\dfrac{7!}{3!}=840$. If the three E's are glued into one block, we arrange $5$ distinct objects: $5!=120$ ways. All distinct arrangements are equally likely, so the probability is $\dfrac{120}{840}=\boxed{\dfrac17}$.''',
'Probability|Multiset permutations|Permutations',2)

# ---------------- 1717423 xyz=1
b.add(1717423,1,r'''Find the value of
\[
\dfrac{1}{1+x+xy}+\dfrac{1}{1+y+yz}+\dfrac{1}{1+z+zx}
\]
if $x$, $y$, $z$ are real numbers with $xyz=1$ (and the denominators are nonzero).''',
r'''Multiply the numerator and denominator of the second fraction by $x$ and of the third by $xy$ (both nonzero, since $xyz=1$), and use $xyz=1$:
\[
\dfrac{1}{1+y+yz}=\dfrac{x}{x+xy+xyz}=\dfrac{x}{1+x+xy},\qquad \dfrac{1}{1+z+zx}=\dfrac{xy}{xy+xyz+x\cdot xyz}=\dfrac{xy}{1+x+xy}.
\]
So the sum is $\dfrac{1+x+xy}{1+x+xy}=\boxed{1}$.''',
'Algebraic expressions and identities|Algebraic manipulation|Substitution',3,source=src('Junior Regional Olympiad FBH',2014,'Grade 8',2),
note='Checked numerically for random x, y with z = 1/(xy).')

# ---------------- 1717407 hexagon two colours
b.add(1717407,1,r'''Let $ABCDEF$ be a hexagon. Each of its sides and diagonals is coloured blue or yellow. Prove that there is a triangle with vertices in $\{A,B,C,D,E,F\}$ whose three sides all have the same colour.''',
r'''The sides and diagonals together are all $15$ segments joining two of the six vertices. Look at the five segments from $A$. By the pigeonhole principle at least three of them have the same colour, say $AX$, $AY$, $AZ$ are blue.
\begin{itemize}
\item If one of $XY$, $YZ$, $ZX$ is blue, say $XY$, then $AXY$ has three blue sides.
\item Otherwise $XY$, $YZ$, $ZX$ are all yellow, and $XYZ$ has three yellow sides.
\end{itemize}
In either case there is a monochromatic triangle. $\blacksquare$''',
'Pigeonhole principle|Graph colouring|Graph theory|Proof by cases',3,source=src('Junior Regional Olympiad FBH',2014,'Grade 6',5))

# ---------------- 1717974 Euclidean algorithm
b.add(1717974,1,r'''For positive integers $a\ge b$, the Euclidean algorithm divides $a$ by $b$ with remainder, $a=qb+r$ with $0\le r<b$, replaces $(a,b)$ by $(b,r)$, and repeats until the remainder is $0$; the last nonzero remainder is the output. Prove that the algorithm stops and that its output is $\gcd(a,b)$.''',
r'''\textbf{Key lemma.} If $a=qb+r$, then $\gcd(a,b)=\gcd(b,r)$. Indeed, if $d\mid a$ and $d\mid b$, then $d\mid a-qb=r$; and if $d\mid b$ and $d\mid r$, then $d\mid qb+r=a$. So the pairs $(a,b)$ and $(b,r)$ have exactly the same common divisors, hence the same greatest common divisor.

\textbf{Termination.} The successive remainders satisfy $b>r_1>r_2>\dots\ge0$. A strictly decreasing sequence of non-negative integers cannot go on forever, so some remainder is $0$.

\textbf{Output.} Write the steps as $(a,b)\to(b,r_1)\to(r_1,r_2)\to\dots\to(r_{k-1},r_k)\to(r_k,0)$, where $r_k$ is the last nonzero remainder (if already $r_1=0$, read $r_k=b$). By the lemma the gcd is the same for every pair in this chain, so
\[
\gcd(a,b)=\gcd(r_k,0)=r_k .
\]
Hence the algorithm stops and outputs $\gcd(a,b)$. $\blacksquare$

(Example: $\gcd(84,36)$: $84=2\cdot36+12$, $36=3\cdot12+0$, output $12$.)''',
'HCF and LCM|Divisibility|Remainders and congruences|Invariants and monovariants',3,
note='The post asks for a proof of the Euclidean algorithm; the record states the algorithm and asks for the proof.')

# ---------------- 1717400 3ab4 divisible by 9
b.add(1717400,1,r'''If $a$ and $b$ are digits, how many $4$-digit numbers $\overline{3ab4}$ are divisible by $9$? List them.''',
r'''A number is divisible by $9$ exactly when its digit sum is. Here the digit sum is $3+a+b+4=7+a+b$, with $0\le a+b\le18$, so $7+a+b\in\{9,18\}$, i.e.\ $a+b=2$ or $a+b=11$.
\begin{itemize}
\item $a+b=2$: $(a,b)=(0,2),(1,1),(2,0)$: $3024,3114,3204$.
\item $a+b=11$: $a=2,\dots,9$: $3294,3384,3474,3564,3654,3744,3834,3924$.
\end{itemize}
There are $\boxed{11}$ such numbers: $3024,3114,3204,3294,3384,3474,3564,3654,3744,3834,3924$.''',
'Divisibility rules|Digit problems|Systematic counting',2,source=src('Junior Regional Olympiad FBH',2014,'Grade 6',1))

# ---------------- 1717405 primes 3p^2q+2pq^2=483
b.add(1717405,1,r'''Find all prime numbers $p$ and $q$ such that $3p^2q+2pq^2=483$.''',
r'''Factor: $pq(3p+2q)=483=3\cdot7\cdot23$. So $p$ and $q$ are primes dividing $483$, i.e.\ each is $3$, $7$ or $23$, and $3p+2q=\dfrac{483}{pq}$.
\begin{itemize}
\item $p=q$ would need $5p^3=483$, impossible.
\item $\{p,q\}=\{3,7\}$: $pq=21$, so $3p+2q=23$. With $p=3,q=7$: $9+14=23$. With $p=7,q=3$: $21+6=27\ne23$.
\item If $23\in\{p,q\}$, then $3p+2q\ge46+3>\dfrac{483}{pq}$ (as $pq\ge69$, $\dfrac{483}{pq}\le7$). Impossible.
\end{itemize}
The only solution is $\boxed{p=3,\ q=7}$. Check: $3\cdot9\cdot7+2\cdot3\cdot49=189+294=483$.''',
'Prime factorisation|Prime numbers|Diophantine equations|Factoring',2,source=src('Junior Regional Olympiad FBH',2014,'Grade 6',4))

# ---------------- 1717720 three dice prime or even
b.add(1717720,1,r'''Three fair $6$-sided dice are thrown. Find the probability that the sum is a prime number or an even number.''',
r'''The sum is between $3$ and $18$. Use the complement: the sum is neither prime nor even exactly when it is an odd composite number, i.e.\ $9$ or $15$.
\begin{itemize}
\item Sum $9$: the multisets are $\{1,2,6\},\{1,3,5\},\{2,3,4\}$ ($6$ orders each), $\{1,4,4\},\{2,2,5\}$ ($3$ each) and $\{3,3,3\}$ ($1$): $18+6+1=25$ outcomes.
\item Sum $15$: by the symmetry $x\mapsto7-x$ it has as many outcomes as sum $21-15=6$: $\{1,1,4\},\{2,2,2\}$ and $\{1,2,3\}$, i.e.\ $3+1+6=10$ outcomes.
\end{itemize}
So the probability is $1-\dfrac{35}{216}=\boxed{\dfrac{181}{216}}$.''',
'Dice probability|Complementary probability|Prime numbers|Probability with dice',3,
note='Checked by enumerating all 216 outcomes.')

# ---------------- 1717424 bisector BK=KC=2AK
fig=RA+r'''pair A=(0,0),B=(0,2),C=(2*sqrt(3),0),K=(2/sqrt(3),0),M=(B+C)/2;
draw(A--B--C--cycle,linewidth(0.9));draw(B--K,linewidth(0.9));
draw(K--M,dashed);
ra(A,B,C,0.18);ra(M,C,K,0.15);
draw(arc(B,0.5,degrees(K-B),-90),linewidth(0.5));draw(arc(B,0.58,degrees(C-B),degrees(K-B)),linewidth(0.5));
pair t1=(B+K)/2,t2=(K+C)/2,n1=unit(rotate(90)*(K-B)),n2=(0,1);
draw(t1-0.09*n1+0.03*unit(K-B)--t1+0.09*n1+0.03*unit(K-B));draw(t1-0.09*n1-0.03*unit(K-B)--t1+0.09*n1-0.03*unit(K-B));
draw(t2-0.09*n2+(0.03,0)--t2+0.09*n2+(0.03,0));draw(t2-0.09*n2-(0.03,0)--t2+0.09*n2-(0.03,0));
label("$A$",A,SW);label("$B$",B,N);label("$C$",C,SE);label("$K$",K,S);label("$M$",M,NE);'''
b.add(1717424,1,r'''In triangle $ABC$, $BK$ is the bisector of angle $ABC$ ($K$ on side $AC$). Find the angles of triangle $ABC$ if $BK=KC=2AK$.''',
r'''Let $\angle C=\gamma$. Since $BK=KC$, triangle $BKC$ is isosceles and $\angle KBC=\gamma$; as $BK$ bisects angle $B$, $\angle ABK=\gamma$ and $\angle ABC=2\gamma$.

By the angle bisector theorem, $\dfrac{AB}{BC}=\dfrac{AK}{KC}=\dfrac12$, so $BC=2AB$. Let $M$ be the midpoint of $BC$; then $BM=AB$. Since $KB=KC$, the median $KM$ of the isosceles triangle $BKC$ is also an altitude: $KM\perp BC$.
'''+asy(fig,'6cm')+r'''
Triangles $ABK$ and $MBK$ have $AB=MB$, $\angle ABK=\angle MBK$ and the common side $BK$, so they are congruent (SAS). Hence $\angle BAK=\angle BMK=90^\circ$.

Now $90^\circ+2\gamma+\gamma=180^\circ$ gives $\gamma=30^\circ$. The angles are
\[
\boxed{\angle A=90^\circ,\quad\angle B=60^\circ,\quad\angle C=30^\circ}.
\]
Check: with $AB=1$, $AK=\tan30^\circ=\dfrac{1}{\sqrt3}$ and $BK=KC=\dfrac{2}{\sqrt3}=2AK$.''',
'Angle bisector theorem|Congruence|Isosceles triangles|Angle sums|Triangles',4,source=src('Junior Regional Olympiad FBH',2014,'Grade 8',3))

b.save()
