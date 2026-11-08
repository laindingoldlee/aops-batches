from qb import *
b=Bank('p235_02')

# ---------------- 1709625 FBH 2018 G8 P5 square on arc
figs=r'''real r=sqrt(2);
pair O=(0,0),A=(-1,1),B=(1,1),C=(1,-1),D=(-1,-1);
pair Ep=(-0.2,1),F=(0.2,1),G=(0.2,1.4),H=(-0.2,1.4);
draw(circle(O,r),linewidth(0.8));
draw(A--B--C--D--cycle,linewidth(0.9));
draw(Ep--F--G--H--cycle,blue+linewidth(0.9));
draw(O--G,red+dashed);draw(O--(0,1),gray+dashed);
dot(O);dot(G);
label("$A$",A,NW);label("$B$",B,NE);label("$C$",C,SE);label("$D$",D,SW);label("$O$",O,S);
label("$E$",Ep,SW);label("$F$",F,SE);label("$G$",G,NE);label("$H$",H,NW);
label("$k$",r*dir(200),W);'''
b.add(1709625,1,r'''Square $ABCD$ is inscribed in a circle $k$. A second square $EFGH$ is constructed with vertices $E$ and $F$ on side $AB$ and vertices $G$ and $H$ on the arc $AB$ of $k$ that lies outside square $ABCD$. Find the ratio of the area of square $EFGH$ to the area of square $ABCD$.''',
r'''Put the centre $O$ of $k$ at the origin and let $ABCD$ have side $2$, with $AB$ on the line $y=1$; then $k$ has radius $\sqrt2$. By symmetry the small square is symmetric about the $y$-axis (the perpendicular bisector of $AB$ is the axis of symmetry of the figure, and the chord $GH$ of $k$ parallel to $AB$ has the same perpendicular bisector). If its side is $s$, then $G=\left(\dfrac s2,\ 1+s\right)$.
'''+asy(figs,'6cm')+r'''
Since $G$ lies on $k$,
\[
\dfrac{s^2}{4}+(1+s)^2=2\ \Longrightarrow\ 5s^2+8s-4=0\ \Longrightarrow\ (5s-2)(s+2)=0,
\]
so $s=\dfrac25$. The ratio of the areas is
\[
\dfrac{s^2}{2^2}=\dfrac{4}{25}\cdot\dfrac14=\boxed{\dfrac1{25}} .
\]''',
'Squares|Circles|Coordinate geometry|Quadratic equations|Lengths, perimeter, and area',4,source=src('Junior Regional Olympiad FBH',2018,'Grade 8',5),
note='"E and F lie on side ABCD" read as side AB; G and H on the minor arc AB. The figure uses the true size s = 2/5.')

# ---------------- 1709552 FBH 2018 G6 P1 ball
b.add(1709552,1,r'''Four friends bought a ball. The first paid half of the price of the ball. The second paid one third of the amount paid by the other three together. The third paid one quarter of the amount paid by the other three together. The fourth paid $\$5$. How much did the ball cost?''',
r'''Let the price be $P$. If the second friend paid $x$, the other three paid $3x$, so $4x=P$ and $x=\dfrac P4$. Similarly the third paid $\dfrac P5$. Then
\[
\dfrac P2+\dfrac P4+\dfrac P5+5=P\ \Longrightarrow\ \dfrac{P}{20}=5\ \Longrightarrow\ P=\boxed{\$100}.
\]
Check: $50+25+20+5=100$; $25=\dfrac{75}{3}$ and $20=\dfrac{80}{4}$.''',
'Fractions|Linear equations|Money and currency',2,source=src('Junior Regional Olympiad FBH',2018,'Grade 6',1))

# ---------------- 1709584 FBH 2018 G8 P4 inequality
b.add(1709584,1,r'''Let $a$, $b$ and $c$ be positive real numbers with $a\ge b\ge c$. Prove that
\[
\dfrac ab+\dfrac bc+\dfrac ca\le\dfrac ba+\dfrac cb+\dfrac ac .
\]''',
r'''Multiply both sides by $abc>0$. The inequality becomes
\[
a^2c+ab^2+bc^2\le b^2c+c^2a+a^2b,
\]
that is, $D=a^2b+b^2c+c^2a-a^2c-ab^2-bc^2\ge0$. This expression factors:
\[
D=(a-b)(b-c)(a-c).
\]
(Check by expanding: $(a-b)(b-c)=ab-ac-b^2+bc$, and multiplying by $a-c$ gives $a^2b-a^2c-ab^2+abc-abc+ac^2+b^2c-bc^2$, which is $D$.) Since $a\ge b\ge c$, all three factors are nonnegative, so $D\ge0$, which proves the inequality. Equality holds exactly when two of the numbers are equal. $\blacksquare$''',
'Inequalities|Factoring|Algebraic manipulation',4,source=src('Junior Regional Olympiad FBH',2018,'Grade 8',4),
note='Repeat of an earlier record (aliased).')

# ---------------- 1708983 rhombus
figr=r'''pair O=(0,0),A=(-22.5,0),B=(0,12),C=(22.5,0),D=(0,-12);
pair H=A+dot(O-A,B-A)/dot(B-A,B-A)*(B-A);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--C,gray);draw(B--D,gray);
draw(O--H,red+linewidth(0.9));
real q=1.4;pair u=unit(O-H),v=unit(B-H);draw(H+q*u--H+q*(u+v)--H+q*v);
draw((q,0)--(q,q)--(0,q));
dot(O);dot(H);
label("$A$",A,W);label("$B$",B,N);label("$C$",C,E);label("$D$",D,S);label("$O$",O,SE);label("$H$",H,NW);
label("$22.5$",(11.25,0),S);label("$12$",(0,-6),E);label("$h$",(O+H)/2,NE,red);'''
b.add(1708983,1,r'''The area of a rhombus is $540\text{ cm}^2$, and one of its diagonals is $4.5$ dm long. What is the distance from the point of intersection of the diagonals to a side of the rhombus?''',
r'''One diagonal is $4.5\text{ dm}=45$ cm. The area of a rhombus is half the product of its diagonals, so the other diagonal is $\dfrac{2\cdot540}{45}=24$ cm. The diagonals bisect each other at right angles at $O$, so $OA=22.5$ cm and $OB=12$ cm, and the side is
\[
AB=\sqrt{22.5^2+12^2}=\sqrt{650.25}=25.5\text{ cm}.
\]
'''+asy(figr,'7cm')+r'''
Let $h=OH$ be the distance from $O$ to side $AB$. Computing the area of the right triangle $AOB$ in two ways,
\[
\dfrac12\cdot22.5\cdot12=\dfrac12\cdot25.5\cdot h\ \Longrightarrow\ h=\dfrac{270}{25.5}=\boxed{\dfrac{180}{17}\text{ cm}}\approx10.6\text{ cm}.
\]
By symmetry the distance to each of the four sides is the same.''',
'Rhombi|Lengths, perimeter, and area|Pythagorean theorem|Unit conversion',3)

# ---------------- 1709567 FBH 2018 G7 P1 price
b.add(1709567,1,r'''The price of an item decreased by $5\%$. Then the price increased by $40\%$, and now it is $\$1352.06$ less than double the original price. What was the original price?''',
r'''If the original price is $P$, the current price is $0.95\cdot1.4\,P=1.33P$. Then $2P-1.33P=0.67P=1352.06$, so $P=\dfrac{1352.06}{0.67}=\boxed{\$2018}$.''',
'Percentages|Linear equations',2,source=src('Junior Regional Olympiad FBH',2018,'Grade 7',1))

# ---------------- 1709580 FBH 2018 G8 P3 abcd
b.add(1709580,1,r'''Find all four-digit numbers $\overline{abcd}$ such that $4\cdot\overline{abcd}+30=\overline{dcba}$.''',
r'''Since $\overline{dcba}\le9999$, we get $4\cdot\overline{abcd}\le9969$, so $\overline{abcd}\le2492$ and $a\in\{1,2\}$. The left side $4\cdot\overline{abcd}+30$ is even, so its last digit $a$ is even: $a=2$. Then $\overline{abcd}\ge2000$ gives $\overline{dcba}\ge8030$, so $d\in\{8,9\}$. The last digit of $4d+30$ is that of $4d$, and it must be $a=2$; this excludes $d=9$ (last digit $6$), so $d=8$.

Now $4(2008+100b+10c)+30=8002+100c+10b$, which simplifies to
\[
8062+400b+40c=8002+100c+10b\ \Longrightarrow\ 390b+60=60c\ \Longrightarrow\ 13b+2=2c .
\]
So $b$ is even; $b=0$ gives $c=1$, and $b\ge2$ gives $c\ge14$, impossible. The only number is $\boxed{2018}$. Check: $4\cdot2018+30=8102$.''',
'Digits and bases|Digit problems|Casework',3,source=src('Junior Regional Olympiad FBH',2018,'Grade 8',3),
note='Checked by brute force over all four-digit numbers.')

# ---------------- 1709569 FBH 2018 G7 P2 crossed digits
b.add(1709569,1,r'''A three-digit number with all digits different from zero is written on a blackboard. From it we make three two-digit numbers by crossing out its first digit, by crossing out its second digit, and by crossing out its third digit. The sum of these three two-digit numbers is $293$. Which number is written on the blackboard?''',
r'''Let the number be $\overline{abc}$ with digits $a,b,c\in\{1,\dots,9\}$. Crossing out one digit gives $\overline{bc}$, $\overline{ac}$ and $\overline{ab}$, so
\[
(10b+c)+(10a+c)+(10a+b)=20a+11b+2c=293 .
\]
If $a\le8$, the left side is at most $160+99+18=277<293$, so $a=9$ and $11b+2c=113$. Then $11b=113-2c\ge113-18=95$ forces $b=9$, and $2c=14$, $c=7$. The number is $\boxed{997}$. Check: $97+97+99=293$.

(If the three digits were also required to be distinct, there would be no solution at all: the largest possible value of $20a+11b+2c$ with distinct digits is $180+88+14=282<293$.)''',
'Digits and bases|Digit problems|Linear Diophantine equations',3,source=src('Junior Regional Olympiad FBH',2018,'Grade 7',2),
note='The translation "all three digits are distinct than zero" means "different from zero" (nonzero); with distinct digits the problem has no solution, which the solution remarks. Answer 997 checked by brute force.')

# ---------------- 1709312 average speed
b.add(1709312,1,r'''A car travels $300$ miles from Seattle to Spokane in five hours but returns the same distance in $270$ minutes. What is its average speed, in miles per hour, for the round trip?''',
r'''Average speed is total distance divided by total time. The total distance is $600$ miles and the total time is $5+4.5=9.5$ hours, so the average speed is
\[
\dfrac{600}{9.5}=\boxed{\dfrac{1200}{19}\approx63.2\text{ mph}}.
\]
The harmonic-mean approach gives the same value, because the two legs have equal distances: the speeds are $60$ and $\dfrac{300}{4.5}=\dfrac{200}{3}$ mph, and $\dfrac{2\cdot60\cdot\dfrac{200}{3}}{60+\dfrac{200}{3}}=\dfrac{8000}{\dfrac{380}{3}}=\dfrac{1200}{19}$.''',
'Distance, rate, and time|Averages and weighted averages|Harmonic mean',2,
note='The poster used the harmonic mean and asks for confirmation; both methods give 1200/19 mph.')

# ---------------- 1705943 power of 2
b.add(1705943,1,r'''A problem asks to express $4^6+8^3-32^2$ as a power of $2$. Write this number in the form $m\cdot2^k$ with $m$ odd, and decide whether it is a power of $2$.''',
r'''Write each term as a power of $2$: $4^6=2^{12}$, $8^3=2^9$, $32^2=2^{10}$. Then
\[
4^6+8^3-32^2=2^{12}+2^9-2^{10}=2^9(2^3+1-2)=\boxed{7\cdot2^9}=3584 .
\]
Since the odd factor is $7\ne1$, the number is \textbf{not} a power of $2$ (it lies strictly between $2^{11}=2048$ and $2^{12}=4096$). The problem as posted cannot be answered as stated.''',
'Exponents|Powers of two',1,
note='As posted ("express as a power of 2") the problem is impossible: the value is 3584 = 7 * 2^9. The record asks for the form m * 2^k and whether it is a power of 2.')

# ---------------- 106088 jellybeans (alias)
b.add(106088,1,r'''Billy Bob has a jar of jellybeans. Every day he eats $20\%$ of the jellybeans that are in the jar at the start of that day. At the end of the second day, $32$ jellybeans remain. How many were in the jar originally?''',
r'''Each day leaves $80\%=\dfrac45$ of the jellybeans. After two days $\left(\dfrac45\right)^2=\dfrac{16}{25}$ of the original number remains, so the original number is $32\cdot\dfrac{25}{16}=\boxed{50}$. Check: $50\to40\to32$.''',
'Percentages|Working backwards',2,
note='"On the second day, Billy Bob had 32" read as 32 left at the end of the second day. Repeat of an earlier record (aliased).')

# ---------------- 1702869 3-digit cyclics
b.add(1702869,1,r'''How many three-digit numbers $N$ have the property that $\dfrac43N$ is the three-digit number obtained from $N$ by moving its last digit to the front? (For example, $243\cdot\dfrac43=324$.)''',
r'''Write $N=10x+c$, where $c$ is the last digit and $x$ is the two-digit number formed by the first two digits ($10\le x\le99$). Moving $c$ to the front gives $100c+x$, which must be a three-digit number, so $c\ge1$. The condition $\dfrac43N=100c+x$ becomes
\[
4(10x+c)=3(100c+x)\ \Longrightarrow\ 37x=296c\ \Longrightarrow\ x=8c .
\]
We need $10\le8c\le99$ with $1\le c\le9$, so $c=2,3,\dots,9$. This gives the numbers
\[
162,\ 243,\ 324,\ 405,\ 486,\ 567,\ 648,\ 729,
\]
for example $162\cdot\dfrac43=216$. There are $\boxed{8}$ such numbers.''',
'Digit problems|Digits and bases|Linear equations',3,
note='Checked by brute force over all three-digit numbers.')

# ---------------- 1708628 folded rectangle
figf=r'''pair A=(0,0),B=(8,0),C=(8,6),D=(0,6),O=(4,3),Ep=(1.75,0),F=(6.25,6);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(B--D,blue+dashed);
draw(Ep--F,red+linewidth(1.1));
real q=0.35;pair u=unit(F-O),v=unit(D-O);draw(O+q*u--O+q*(u+v)--O+q*v);
draw((8-q,6)--(8-q,6-q)--(8,6-q));
dot(O);dot(Ep);dot(F);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);
label("$E$",Ep,S);label("$F$",F,N);label("$O$",O,dir(8));
label("$8$",(4.5,0),S);label("$6$",(8,3),E);'''
b.add(1708628,1,r'''Rectangle $ABCD$ is folded along a line $EF$, with $E$ on side $AB$ and $F$ on side $CD$, so that point $B$ falls on point $D$. If $AD=6$ and $AB=8$, find the length of the crease $EF$.''',
r'''When $B$ lands on $D$, every point of the crease is equidistant from $B$ and $D$, so the crease $EF$ is the perpendicular bisector of $BD$. Let it meet $BD$ at $O$, the midpoint of $BD$. Since $BD=\sqrt{8^2+6^2}=10$, $OD=5$.
'''+asy(figf,'6.5cm')+r'''
\textbf{Why triangles $BCD$ and $FOD$ are similar.} Both are right triangles: $\angle BCD=90^\circ$ (corner of the rectangle) and $\angle FOD=90^\circ$ (the crease is perpendicular to $BD$). They also share the angle at $D$, because $O$ lies on $DB$ and $F$ lies on $DC$, so $\angle ODF=\angle BDC$. Two equal angles make the triangles similar, with $O\leftrightarrow C$, $F\leftrightarrow B$, $D\leftrightarrow D$. Hence
\[
\dfrac{OF}{OD}=\dfrac{CB}{CD}=\dfrac68\ \Longrightarrow\ OF=\dfrac34\cdot5=\dfrac{15}{4}.
\]
By the symmetry of the rectangle about $O$ (a half-turn about $O$ swaps $B,D$ and swaps the lines $AB$, $CD$), $OE=OF$. Therefore
\[
EF=2\cdot\dfrac{15}{4}=\boxed{\dfrac{15}{2}}.
\]
Check with coordinates $A(0,0)$, $B(8,0)$, $D(0,6)$: the crease passes through $E(1.75,0)$ and $F(6.25,6)$, and $EF=\sqrt{4.5^2+6^2}=7.5$.''',
'Rectangles|Similarity|Perpendicular bisectors|Pythagorean theorem|Paper folding',3,
note='The poster asks why triangles BCD and DOF are similar; the solution explains it.')

# ---------------- 1708605 trees in a row
b.add(1708605,1,r'''Ten maple trees, three oak trees and three birch trees are to be planted in a row. Trees of the same kind are indistinguishable. In how many ways can this be done so that no birch tree is next to an oak tree?''',
r'''Place the $10$ maples first; they create $11$ gaps (including the two ends). The oaks and birches go into the gaps, and inside a gap no oak may touch a birch, so each gap receives trees of only one kind (or none).

Suppose the oaks occupy $i$ gaps and the birches $j$ gaps ($1\le i,j\le3$). Splitting $3$ identical oaks into $i$ nonempty groups in order can be done in $\dbinom{2}{i-1}$ ways, and the same for birches. Choosing the gaps: $\dbinom{11}{i}\dbinom{11-i}{j}$ ways. So the count is
\[
\sum_{i=1}^{3}\sum_{j=1}^{3}\binom{2}{i-1}\binom{2}{j-1}\binom{11}{i}\binom{11-i}{j}.
\]
Row by row:
\begin{itemize}
\item $i=1$: $11\,(10+2\cdot45+120)=11\cdot220=2420$;
\item $i=2$: $2\cdot55\,(9+2\cdot36+84)=110\cdot165=18150$;
\item $i=3$: $165\,(8+2\cdot28+56)=165\cdot120=19800$.
\end{itemize}
The total is $2420+18150+19800=\boxed{40370}$.''',
'Arrangements with restrictions|Multiset permutations|Combinations|Casework',5,
note='Trees of the same kind are taken as indistinguishable (the usual reading). Checked by brute force over all 160160 arrangements.')

# ---------------- 1708235 nine numbers
b.add(1708235,1,r'''Nine different positive integers are given. Adding any two of them, various sums can be obtained; the smallest of these sums is $123$ and the largest is $456$. Find the greatest possible sum of the nine integers.''',
r'''Order the numbers $a_1<a_2<\cdots<a_9$. The smallest pairwise sum is $a_1+a_2=123$ and the largest is $a_8+a_9=456$. Since $a_8<a_9$, we have $2a_8<456$, so $a_8\le227$, and then, the integers being different,
\[
a_7\le226,\quad a_6\le225,\quad a_5\le224,\quad a_4\le223,\quad a_3\le222 .
\]
Hence
\[
a_1+\cdots+a_9\le123+(222+223+224+225+226)+456=123+1120+456=1699 .
\]
Equality is possible, for example with $1,\ 122,\ 222,\ 223,\ 224,\ 225,\ 226,\ 227,\ 229$: the smallest sum is $1+122=123$ and the largest is $227+229=456$. The greatest possible sum is $\boxed{1699}$.''',
'Bounding and extremal cases|Inequalities|Construction',3,
note='Hong Kong contest problem in translation. "Different sums can be obtained" is read as: the nine numbers are different positive integers (the pairwise sums need not all be distinct).')

# ---------------- 1708041 2018 National Sprint 21
b.add(1708041,1,r'''What is the greatest integer less than or equal to
\[
\dfrac{3^{19}+2^{19}}{3^{15}+2^{15}}\ ?
\]''',
r'''Let $D=3^{15}+2^{15}$. Since $3^{19}=81\cdot3^{15}$,
\[
3^{19}+2^{19}=81D-81\cdot2^{15}+2^{19}=81D-65\cdot2^{15}.
\]
So the fraction equals $81-\dfrac{65\cdot2^{15}}{D}$. Here $65\cdot2^{15}=2129920$ and $D=14348907+32768=14381675$, so $0<65\cdot2^{15}<D$. So $0<\dfrac{65\cdot2^{15}}{D}<1$, and the fraction lies strictly between $80$ and $81$. The answer is $\boxed{80}$.''',
'Exponents|Floor and ceiling functions|Estimation',3,source=src('MATHCOUNTS',2018,'National',21,rnd='Sprint'))

# ---------------- 1708456 line and plane
figp=r'''pair P1=(0,0),P2=(6,0),P3=(8,3),P4=(2,3),X=(4,1.5);
fill(P1--P2--P3--P4--cycle,palegray);
draw(P1--P2--P3--P4--cycle,linewidth(0.8));
draw(X--(4.6,4.5),blue+linewidth(0.9));draw(X--(3.7,0),blue+dashed);draw((3.7,0)--(3.6,-0.5),blue+linewidth(0.9));
draw((0.9,0.4)--(3.0,2.5),red+linewidth(0.9));
dot(X);
label("$P$",X,E);label("$\Pi$",(5.6,0.45));label("$\ell$",(4.6,4.5),N,blue);label("$m$",(3.0,2.5),E,red);'''
b.add(1708456,1,r'''Can the intersection of a line and a plane be a line segment? Prove your answer by describing all possible intersections of a line and a plane.''',
r'''\textbf{No.} We use the basic fact of solid geometry that if a plane contains two distinct points of a line, it contains the whole line.

Let $\ell$ be a line and $\Pi$ a plane. There are three cases.
\begin{itemize}
\item $\ell$ and $\Pi$ have no common point: the intersection is empty ($\ell$ is parallel to $\Pi$).
\item They have exactly one common point $P$: the intersection is the single point $P$ ($\ell$ pierces $\Pi$, like line $\ell$ in the sketch).
\item They have at least two distinct common points: by the fact above, $\Pi$ contains all of $\ell$, and the intersection is the whole line (like line $m$ in the sketch).
\end{itemize}
'''+asy(figp,'5.5cm')+r'''
A line segment contains more than one point, so it could only occur in the third case; but there the intersection is the entire (unbounded) line, which is not a segment. Hence the intersection of a line and a plane is never a segment: it is $\boxed{\text{empty, a single point, or the whole line}}$. $\blacksquare$''',
'Solid geometry|Proof by cases',1,
note='Conceptual question turned into a short proof.')

# ---------------- 1708333 300th post, problem 3 only
b.add(1708333,3,r'''A traveller comes to a magic bridge. Each time he walks across it, his money triples, but after each crossing he must pay $\$30$ toll. He crosses $10$ times, paying the toll each time. On his eleventh crossing his money triples to exactly $\$30$; he pays the toll and is left with nothing. How much money did he start with? Give the answer as a fraction.''',
r'''Let $m_k$ be his money after $k$ crossings (and tolls), so $m_k=3m_{k-1}-30$ and $m_{11}=0$. Working backwards with $m_{k-1}=\dfrac{m_k+30}{3}$ is possible, but it is quicker to notice that $15$ is a fixed point: $3\cdot15-30=15$. Hence
\[
m_k-15=3(m_{k-1}-15),\qquad\text{so}\qquad m_{11}-15=3^{11}(m_0-15).
\]
With $m_{11}=0$: $m_0=15-\dfrac{15}{3^{11}}=15-\dfrac{5}{3^{10}}=\dfrac{15\cdot59049-5}{59049}$, so he started with
\[
\boxed{\$\dfrac{885730}{59049}}\approx\$14.9999 .
\]
(Working backwards from the end: before the last crossing he had $\dfrac{30}{3}=10$, before that $\dfrac{10+30}{3}=\dfrac{40}{3}$, then $\dfrac{130}{9}$, and so on, which gives the same value.)''',
'Working backwards|Recurrence relations|Exponents|Fractions',3,
note='Problem 3 of the post. Problem 1 (Bernie\'s canning factory) is dropped: (x+1)(x-5)=300 and (y-2)(y+1)=200 have irrational solutions (x = 2+sqrt309, y = (1+sqrt809)/2), so the "number of things canned" is not a sensible value. Problem 2 (the wallet thief) is dropped: the statements are contradictory (William\'s statements force Fred and William innocent; then Jenny\'s first statement is her lie, so "Jenny does not know where the wallet was" is true, but Al\'s statements force "Jenny knows where the wallet was" to be true as well).')

# ---------------- 1708321 isosceles perimeter 2008
figi=r'''pair B=(0,0),C=(6,0),A=(3,4.2);
draw(A--B--C--cycle,linewidth(0.9));
real t=0.25;
pair m1=(A+B)/2,m2=(A+C)/2;
draw(m1+t*unit(rotate(90)*(A-B))*(-1)--m1+t*unit(rotate(90)*(A-B)));
draw(m2+t*unit(rotate(90)*(C-A))*(-1)--m2+t*unit(rotate(90)*(C-A)));
label("$a$",m1+0.6*unit(rotate(90)*(A-B)));label("$a$",m2+0.6*unit(rotate(90)*(C-A)));label("$2008-2a$",(3,0),S);'''
b.add(1708321,1,r'''The side lengths of an isosceles triangle are natural numbers (in cm), and its perimeter is $2008$ cm. How many such triangles exist (counting congruent triangles once)?''',
r'''Let the two equal sides be $a$ and the third side $b=2008-2a$.
'''+asy(figi,'4.5cm')+r'''
We need $b\ge1$, i.e.\ $a\le1003$, and the triangle inequality: $a+a>b$, i.e.\ $2a>2008-2a$, $a>502$. (The other inequalities $a+b>a$ are automatic.) So $a=503,504,\dots,1003$, which gives $1003-502=501$ triangles. No triangle is counted twice, because an equilateral triangle would need $3\mid2008$, which is false, so each triangle has a unique pair of equal sides. The answer is $\boxed{501}$.''',
'Isosceles triangles|Triangle inequality|Systematic counting',3,
note='Checked by brute force.')

# ---------------- 1294839 1+3+9+...
b.add(1294839,1,r'''A student argues as follows. Let $S=3^0+3^1+3^2+3^3+\cdots$. Then $3S=3^1+3^2+3^3+\cdots$, and subtracting,
\[
S-3S=3^0=1,\qquad\text{so}\qquad S=-\dfrac12 .
\]
What is wrong with this argument?''',
r'''The argument treats $S$ as a number, but the series has no (finite) sum. The partial sums are
\[
S_n=1+3+\cdots+3^n=\dfrac{3^{n+1}-1}{2},
\]
which grow without bound ($S_n\ge3^n$). An infinite sum is \emph{defined} as the limit of the partial sums, and here there is no limit, so ``$S$'' is not a real number. The rules ``$3S$ is the series multiplied term by term'' and ``$S-3S$ can be computed term by term'' are only valid for convergent series; applied to a divergent one they produce nonsense (the same steps applied to $T=1+2+4+\cdots$ would give $T=-1$, a negative ``sum'' of positive numbers). So the error is the very first step, assuming the sum $S$ exists.

Done correctly with finite sums, the same idea works: $3S_n-S_n=3^{n+1}-1$, which gives the formula for $S_n$ above. For a ratio $r$ with $|r|<1$ the partial sums $\dfrac{1-r^{n+1}}{1-r}$ do converge, and then the trick legitimately gives $1+r+r^2+\cdots=\dfrac1{1-r}$; for $r=3$ it does not.''',
'Geometric sequences|Sequences and series',3,
note='Conceptual "what is wrong" post kept as an error-finding question.')

# ---------------- 1707812 apples
b.add(1707812,1,r'''Najeera bought some apples for her friends. If she gives $4$ apples to each friend, or $5$ apples to each friend, or $6$ apples to each friend, in each case she is left with $7$ apples (for some number of friends, at least one). What is the least number of apples she could have bought?''',
r'''Let $N$ be the number of apples. Then $N-7$ is a positive multiple of $4$, of $5$ and of $6$, hence a positive multiple of $\operatorname{lcm}(4,5,6)=60$. The least possibility is $N-7=60$, so $N=\boxed{67}$. (Then she has $15$, $12$ or $10$ friends' worth of apples to hand out respectively.)''',
'HCF and LCM|Remainders and congruences',2,
note='The post does not say the number of friends is the same in the three cases (it cannot be); read in the usual way: N - 7 is a positive multiple of 4, 5 and 6.')

# ---------------- 1706974 simplifying congruences
b.add(1706974,1,r'''\begin{enumerate}
\item[(a)] Solve the congruence $9\equiv b+4\pmod{20}$ for $b$. A student claims that it simplifies to $b\equiv4\pmod{20}$. Is this right?
\item[(b)] Explain why $1\equiv b+2\pmod3$ gives $b\equiv2\pmod3$.
\end{enumerate}''',
r'''A congruence can be treated like an equation as far as adding or subtracting the same integer on both sides is concerned: if $x\equiv y\pmod n$ then $x-k\equiv y-k\pmod n$, since $(x-k)-(y-k)=x-y$ is still divisible by $n$.

\textbf{(a)} Subtract $4$ from both sides: $b\equiv9-4=5\pmod{20}$. So the solutions are $\boxed{b\equiv5\pmod{20}}$, i.e.\ $b=\dots,-15,5,25,45,\dots$. The student's $b\equiv4$ is wrong: for $b=4$, $b+4=8\not\equiv9\pmod{20}$.

\textbf{(b)} Subtract $2$ from both sides: $b\equiv1-2=-1\pmod3$. Since $-1\equiv2\pmod3$ (they differ by $3$), this is $\boxed{b\equiv2\pmod3}$. Check: $b=2$ gives $b+2=4\equiv1\pmod3$.''',
'Remainders and congruences',1,
note='The poster proposes b = 4 (mod 20) for 9 = b + 4 (mod 20); corrected to b = 5. The textbook system (x = 1 mod 3, x = 2 mod 4) itself is already in the bank, so the record asks only about the two simplifications.')

# ---------------- 1707260 partition function
b.add(1707260,1,r'''For positive integers $N$ and $r$, let $F(N,r)$ be the number of ways to write $N$ as a sum of $r$ positive integers when the order of the summands does not matter (so $F(5,2)=2$, from $1+4$ and $2+3$), with $F(N,r)=0$ when $N<r$. No simple closed formula for $F(N,r)$ is known for general $r$, but small $r$ can be handled.
\begin{enumerate}
\item[(a)] Prove that $F(N,2)=\left\lfloor\dfrac N2\right\rfloor$.
\item[(b)] Prove that $F(N,r)=F(N-1,r-1)+F(N-r,r)$ for $2\le r<N$.
\item[(c)] Prove that $F(N,3)$ is the integer nearest to $\dfrac{N^2}{12}$ for every $N\ge1$.
\end{enumerate}''',
r'''\textbf{(a)} Write $N=a+b$ with $1\le a\le b$. Then $a$ can be any integer with $1\le a\le\dfrac N2$, and $b=N-a$ is determined, so $F(N,2)=\left\lfloor\dfrac N2\right\rfloor$.

\textbf{(b)} Split the partitions of $N$ into $r$ parts by their smallest part. If the smallest part is $1$, deleting it gives a partition of $N-1$ into $r-1$ parts, and this is reversible: $F(N-1,r-1)$ partitions. If every part is at least $2$, subtracting $1$ from each part gives a partition of $N-r$ into $r$ parts, again reversibly: $F(N-r,r)$ partitions (zero if $N-r<r$).

\textbf{(c)} By (a) and (b), for $N\ge4$,
\[
F(N,3)=F(N-1,2)+F(N-3,3)=\left\lfloor\dfrac{N-1}{2}\right\rfloor+F(N-3,3),
\]
and $F(1,3)=F(2,3)=0$, $F(3,3)=1$. Let $g(N)$ be the integer nearest to $\dfrac{N^2}{12}$. The value of $N^2\bmod12$ depends only on $N\bmod6$, and
\[
g(N)=\dfrac{N^2-c(N)}{12},\qquad c(N)=\begin{cases}0,&N\equiv0\\ 1,&N\equiv\pm1\\ 4,&N\equiv\pm2\\ -3,&N\equiv3\end{cases}\pmod 6,
\]
because $N^2-c(N)$ is then divisible by $12$ and $\left|\dfrac{c(N)}{12}\right|<\dfrac12$. Then
\[
g(N)-g(N-3)=\dfrac{6N-9-c(N)+c(N-3)}{12}.
\]
Going through $N\bmod6=0,1,2,3,4,5$ (so $N-3\bmod6=3,4,5,0,1,2$), the value of $c(N-3)-c(N)$ is $-3,3,-3,3,-3,3$, which gives $g(N)-g(N-3)=\dfrac{N-2}{2}$ for even $N$ and $\dfrac{N-1}{2}$ for odd $N$, that is, $\left\lfloor\dfrac{N-1}{2}\right\rfloor$ in every case. Also $g(1)=g(2)=0$ and $g(3)=1$. So $g$ and $F(\cdot,3)$ satisfy the same recurrence with the same starting values, and by induction (in steps of $3$) $F(N,3)=g(N)$ for all $N\ge1$. $\blacksquare$

For example $F(12,3)=12$ and $F(20,3)=\text{nearest integer to }\dfrac{400}{12}=33$.''',
'Partitions and compositions|Recursive counting|Floor and ceiling functions|Mathematical induction',5,
note='The poster asks for a general formula for the number of partitions of N into r parts; none is known in closed form. The record proves the poster\'s property F(N,2) = floor(N/2), the standard recurrence, and the formula for r = 3. All checked by brute force for N <= 60.')

# ---------------- 1707676 geometry questions 1, 4, 5
figt=r'''real h=sqrt(216);
pair D=(0,0),C=(18,0),A=(3,h),B=(15,h);
pair Ep=D+(2.5/15)*(A-D),F=C+(2.5/15)*(B-C);
pair Q=(6,0),P=extension(A,Q,Ep,F);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(Ep--F,linewidth(0.9));
draw(A--Q,blue+dashed);
dot(Ep);dot(F);dot(P);dot(Q);
label("$A$",A,NW);label("$B$",B,NE);label("$C$",C,SE);label("$D$",D,SW);
label("$E$",Ep,W);label("$F$",F,E);label("$P$",P,NE);label("$Q$",Q,S);
label("$12$",(9,h),N);label("$18$",(12,0),S);label("$5$",(Ep+P)/2,N);label("$12$",(11,Ep.y),N);'''
b.add(1707676,1,r'''In trapezoid $ABCD$ the bases are $AB$ and $CD$, and $EF$ is a segment parallel to them with $E$ on $AD$ and $F$ on $BC$. Given that $AB=12$, $CD=18$, $EF=17$ and $AD=15$, find $ED$.''',
r'''Draw the line through $A$ parallel to $BC$; let it meet $EF$ at $P$ and $DC$ at $Q$. Then $ABFP$ and $ABCQ$ are parallelograms, so $PF=QC=AB=12$, hence $EP=17-12=5$ and $DQ=18-12=6$.
'''+asy(figt,'7cm')+r'''
Since $EP\parallel DQ$, triangles $AEP$ and $ADQ$ are similar, so
\[
\dfrac{AE}{AD}=\dfrac{EP}{DQ}=\dfrac56\ \Longrightarrow\ AE=\dfrac56\cdot15=12.5 .
\]
Therefore $ED=15-12.5=\boxed{\dfrac52}$.''',
'Trapezoids|Similarity|Parallel lines|Parallelograms',3,
note='Question 1 of the post. Questions 2 ("how do you find the internal tangent of a circle") and 3 ("is there a formula for the goat-grazing problem") give no specific problem and are dropped.')

figfr=r'''real ex=0.3;
draw(ellipse((0,96),6,6*ex),linewidth(0.8));
draw(shift(0,48)*scale(16,16*ex)*arc((0,0),1,180,360),linewidth(0.8));draw(shift(0,48)*scale(16,16*ex)*arc((0,0),1,0,180),dashed);
draw(shift(0,0)*scale(6,6*ex)*arc((0,0),1,180,360),linewidth(0.8));draw(shift(0,0)*scale(6,6*ex)*arc((0,0),1,0,180),dashed);
draw((-6,96)--(-16,48)--(-6,0),linewidth(0.8));draw((6,96)--(16,48)--(6,0),linewidth(0.8));
draw((0,0)--(6,0),blue);draw((0,48)--(-16,48),blue+dashed);draw((0,48)--(0,96),red+dashed);
draw((6,96)--(16,96),gray+dashed);draw((16,96)--(16,48),gray+dashed);
label("$6$",(3,-2),S,blue);label("$16$",(-8,39),blue);label("$48$",(-0.5,72),W,red);label("$10$",(11,97),N,gray);label("$l$",(13.5,72));'''
b.add(1707676,4,r'''Two congruent frustums of right circular cones are joined at their larger bases. Each frustum has smaller radius $6$, larger radius $16$ and height $48$. What is the total surface area of the resulting solid?''',
r'''The surface of the solid consists of the two small circular faces and the two lateral surfaces (the large bases are glued together and are inside).

The slant height $l$ of each frustum is the hypotenuse of a right triangle with legs $48$ (the height) and $16-6=10$ (the difference of the radii):
\[
l=\sqrt{48^2+10^2}=\sqrt{2404}=2\sqrt{601}.
\]
'''+asy(figfr,'4.5cm,8cm')+r'''
The lateral area of a frustum with radii $r,R$ and slant height $l$ is $\pi(r+R)l$ (the difference of the lateral areas of two similar cones). So each lateral surface has area $\pi\cdot22\cdot2\sqrt{601}=44\sqrt{601}\,\pi$. The two small circles have total area $2\cdot36\pi=72\pi$. The total surface area is
\[
\boxed{(72+88\sqrt{601})\,\pi}\approx2.31\times10^3 .
\]''',
'Cones|Surface area|Pythagorean theorem',3,
note='Question 4 of the post; "they both a smaller radius" read as each frustum having these dimensions.')

figpe=r'''pair[] V;
for(int i=0;i<5;++i) V[i]=dir(90+72*i);
pair A=V[0],B=V[1],C=V[2],D=V[3],Ee=V[4];
draw(A--B--C--D--Ee--cycle,linewidth(0.9));
draw(A--C,blue);draw(B--D,blue);
pair P=extension(A,C,B,D);
dot(P);
label("$A$",A,N);label("$B$",B,W);label("$C$",C,SW);label("$D$",D,SE);label("$E$",Ee,E);label("$P$",P,E);
label("$2$",(A+B)/2,NW);label("$2$",(B+C)/2,W);'''
b.add(1707676,5,r'''A regular pentagon has side length $2$. Find the length of its diagonals, using similar triangles.''',
r'''Let the pentagon be $ABCDE$ and let the diagonals $AC$ and $BD$ meet at $P$; let $d=AC=BD$. Each interior angle is $108^\circ$. Triangle $ABC$ is isosceles with $AB=BC=2$, so $\angle BAC=\angle BCA=36^\circ$; similarly $\angle CBD=36^\circ$.
'''+asy(figpe,'5cm')+r'''
\begin{itemize}
\item In triangle $PBC$, $\angle PBC=\angle PCB=36^\circ$, so $PB=PC$ and $\angle BPC=108^\circ$.
\item $\angle ABP=108^\circ-36^\circ=72^\circ$ and $\angle APB=180^\circ-108^\circ=72^\circ$, so triangle $ABP$ is isosceles with $AP=AB=2$. Hence $PC=d-2$.
\item Triangles $PBC$ and $BAC$ both have angles $36^\circ,36^\circ,108^\circ$, so they are similar, with legs $PC=d-2$, $BC=2$ and bases $BC=2$, $AC=d$ respectively:
\[
\dfrac{d-2}{2}=\dfrac{2}{d}\ \Longrightarrow\ d^2-2d-4=0\ \Longrightarrow\ d=1+\sqrt5
\]
(the positive root).
\end{itemize}
The diagonals have length $\boxed{1+\sqrt5}\approx3.24$.''',
'Regular polygons|Diagonals|Similarity|Isosceles triangles|Quadratic equations',4,
note='Question 5 of the post asks for "the length of a regular pentagon with side lengths 2"; read as the length of a diagonal.')

# ---------------- 1706187 alternating squares
b.add(1706187,1,r'''Find $50^2-49^2+48^2-47^2+\cdots+2^2-1^2$.''',
r'''Group the terms in pairs and use $a^2-b^2=(a-b)(a+b)$:
\[
(50^2-49^2)+(48^2-47^2)+\cdots+(2^2-1^2)=(50+49)+(48+47)+\cdots+(2+1),
\]
since each difference $a-b$ is $1$. This is $1+2+\cdots+50=\dfrac{50\cdot51}{2}=\boxed{1275}$.''',
'Difference of squares|Summation|Pairing and grouping',2,
note='From a school math team selection test.')

# ---------------- 1707744 restricted distribution
b.add(1707744,1,r'''In how many ways can $12$ identical balls be distributed among $3$ people so that each person gets at most $5$ balls?''',
r'''Let the people get $x_1,x_2,x_3$ balls, with $0\le x_i\le5$ and $x_1+x_2+x_3=12$. Put $y_i=5-x_i$; then $y_i\ge0$ and $y_1+y_2+y_3=15-12=3$, and conversely any such $y_i$ give valid $x_i$ (since $y_i\le3\le5$). By stars and bars the number of solutions is $\dbinom{3+2}{2}=\boxed{10}$.

(Alternatively, by inclusion-exclusion: $\dbinom{14}{2}-3\dbinom{8}{2}+3\dbinom{2}{2}=91-84+3=10$.)''',
'Distributions and integer solutions|Stars and bars|Complementary counting',3)

# ---------------- 1707054 dollar menu
b.add(1707054,1,r'''There are six different choices on the dollar menu at Burgerboy: fries, apple pies, onion rings, chicken nuggets, hamburgers and cheeseburgers. You decide to buy four items (you may buy several of the same item). How many different combinations of four items can you buy? Explain how to solve this with stars and bars.''',
r'''A combination is determined by how many of each of the six items you buy: nonnegative integers $x_1,\dots,x_6$ with $x_1+\cdots+x_6=4$. Represent a combination by $4$ stars (the items) and $5$ bars (separating the six kinds), e.g.\ $\star\star|\,|\star|\,|\,|\star$ means $2$ fries, $1$ onion ring and $1$ cheeseburger. Every arrangement of $4$ stars and $5$ bars in a row of $9$ symbols gives exactly one combination and vice versa, so the number of combinations is
\[
\binom{9}{4}=\boxed{126}.
\]''',
'Stars and bars|Distributions and integer solutions|Bijections',2,
note='The repetition of items (implied by the posted answer 126) is stated explicitly.')

# ---------------- 1704985 2005 National Sprint 14 rods and connectors
figrod=r'''pair a=(0,0),b=(2,0),c=(4,0),d=(1,sqrt(3)),e=(3,sqrt(3)),f=(2,2sqrt(3));
pen rp=gray+linewidth(2.2);
draw(a--b--c,rp);draw(d--e,rp);draw(a--d--f,rp);draw(c--e--f,rp);draw(b--d,rp);draw(b--e,rp);
dot(a,black+linewidth(6));dot(b,black+linewidth(6));dot(c,black+linewidth(6));dot(d,black+linewidth(6));dot(e,black+linewidth(6));dot(f,black+linewidth(6));'''
b.add(1704985,1,r'''A two-row triangle is created with a total of $15$ pieces: $9$ unit rods and $6$ connectors, as shown. What is the total number of pieces that would be used to create an eight-row triangle?
'''+asy(figrod,'3.5cm'),
r'''In an $n$-row triangle, row $k$ (from the top) contains $k$ upward-pointing unit triangles, so there are $1+2+\cdots+n=\dfrac{n(n+1)}{2}$ upward triangles. Every rod is a side of exactly one upward triangle, so the number of rods is $3\cdot\dfrac{n(n+1)}{2}$. The connectors sit at the lattice points, which form rows of $1,2,\dots,n+1$ points, so there are $\dfrac{(n+1)(n+2)}{2}$ connectors.

For $n=2$ this gives $9$ rods and $6$ connectors, as in the figure. For $n=8$: $3\cdot36=108$ rods and $\dfrac{9\cdot10}{2}=45$ connectors, so $\boxed{153}$ pieces.

(The ``Newton's little formula'' of the official solution is the method of finite differences: the totals for $n=1,2,3,4$ are $6,15,28,45$, with first differences $9,13,17$ and constant second difference $4$, so the total is a quadratic in $n$, namely $2n^2+3n+1=(2n+1)(n+1)$; for $n=8$ this is $17\cdot9=153$.)''',
'Pattern recognition|Triangular numbers|Counting shapes in figures',3,source=src('MATHCOUNTS',2005,'National',14,rnd='Sprint'),
note='The figure was an image in the post; it is redrawn from the text (2 rows, 9 rods, 6 connectors). The poster asks what "Newton\'s little formula" is; the solution explains finite differences.')

b.save()
