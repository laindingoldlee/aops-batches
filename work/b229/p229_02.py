from qb import *
b=Bank('p229_02')

# ---------------- 1744764 mass points
fig=r'''pair A=(0,0),B=(8,0),C=(2.5,5.5);
pair D=A+3/8*(B-A), Ep=C+8/11*(B-C);
pair G=extension(A,Ep,C,D), F=extension(B,G,A,C);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--Ep);draw(C--D);draw(B--F);
dot(D);dot(Ep);dot(F);dot(G);
label("$A$",A,dir(160));label("$B$",B,dir(20));label("$C$",C,N);label("$D$",D,S);label("$E$",Ep,NE);label("$F$",F,NW);label("$G$",G,dir(55));
label("$40$",A+(0,-0.75),blue);label("$24$",B+(0,-0.75),blue);label("$9$",C+(0.75,0.1),blue);'''
b.add(1744764,1,r'''In triangle $ABC$, points $D$, $E$, $F$ lie on sides $AB$, $BC$, $CA$ respectively, and the segments $AE$, $CD$, $BF$ meet at a common point $G$. If $AD:DB=3:5$ and $CE:EB=8:3$, find the ratio $FG:GB$.''',
r'''Use mass points: place masses $m_A,m_B,m_C$ at the vertices so that $D$ is the balance point of $A,B$ and $E$ the balance point of $B,C$. This requires $m_A\cdot AD=m_B\cdot DB$, i.e.\ $m_A:m_B=5:3$, and $m_C\cdot CE=m_B\cdot EB$, i.e.\ $m_C:m_B=3:8$. In integers, $m_A=40$, $m_B=24$, $m_C=9$ (blue in the sketch).
'''+asy(fig,'6cm')+r'''
The centre of mass of the three masses lies on both cevians $AE$ and $CD$, so it is $G$; it also lies on the segment from $B$ to $F$, the balance point of $A$ and $C$, which carries mass $m_A+m_C=49$. Balancing on $BF$,
\[
\dfrac{FG}{GB}=\dfrac{m_B}{m_F}=\dfrac{24}{49}.
\]
So $FG:GB=\boxed{24:49}$.

(Check with Ceva's theorem: $\dfrac{AD}{DB}\cdot\dfrac{BE}{EC}\cdot\dfrac{CF}{FA}=1$ gives $\dfrac{CF}{FA}=\dfrac53\cdot\dfrac83=\dfrac{40}{9}=\dfrac{m_A}{m_C}$, as it should.)''',
'Mass points|Ceva\'s theorem|Triangles|Ratios, proportions, and variation',4,
note='Answer 24:49 checked with coordinates.')

# ---------------- 1743694 divisors of 2006
b.add(1743694,1,r'''Find the number of positive integral divisors of $2006$.''',
r'''$2006=2\cdot17\cdot59$ with three distinct primes, so it has $2^3=\boxed{8}$ positive divisors.''',
'Divisor counting|Prime factorisation',1,
note='Apparently 2006 iTest Problem 1 (not named in the post); only choice (A) is quoted, so the record is free-response.')

# ---------------- 1744693 bus drivers
b.add(1744693,1,r'''Three bus drivers went to a grocery store. The first bought $4$ sausages, a bottle of cola and $10$ pieces of bread, and paid $16.90$. The second bought $3$ sausages, a bottle of cola and $7$ pieces of bread, and paid $12.60$. The third bought $2$ sausages, $2$ bottles of cola and $2$ pieces of bread. How much did the third driver pay?''',
r'''Let a sausage, a bottle and a piece of bread cost $s,c,b$. We have
\[
4s+c+10b=16.90,\qquad 3s+c+7b=12.60 .
\]
The individual prices are not determined, but the third purchase is a fixed combination of the first two. Seek $\lambda,\mu$ with $\lambda(4,1,10)+\mu(3,1,7)=(2,2,2)$: from $4\lambda+3\mu=2$ and $\lambda+\mu=2$ we get $\lambda=-4$, $\mu=6$, and indeed $10\lambda+7\mu=-40+42=2$. Hence
\[
2s+2c+2b=-4(16.90)+6(12.60)=-67.60+75.60=\boxed{8.00}.
\]''',
'Systems of linear equations|Money and currency',3)

# ---------------- 1744133 perpendicular diameters
fig=r'''real R=8; pair O=(0,0),P=R*dir(55),Y=(P.x,0),Z=(0,P.y);
draw(circle(O,R),linewidth(0.9));
draw((-R,0)--(R,0));draw((0,-R)--(0,R));
draw(P--Y);draw(P--Z);draw(Y--Z,blue+linewidth(1));draw(O--P,dashed);
draw(Y+(0,0.8)--Y+(-0.8,0.8)--Y+(-0.8,0));draw(Z+(0.8,0)--Z+(0.8,-0.8)--Z+(0,-0.8));
dot(O);dot(P);dot(Y);dot(Z);
label("$A$",(-R,0),W);label("$B$",(R,0),E);label("$C$",(0,R),N);label("$D$",(0,-R),S);
label("$O$",O,SW);label("$P$",P,NE);label("$Y$",Y,S);label("$Z$",Z,W);'''
b.add(1744133,1,r'''The point $P$ lies on a circle with centre $O$. Perpendiculars are drawn from $P$ to two perpendicular diameters $AB$ and $CD$, meeting them at $Y$ and $Z$ respectively. If the diameter of the circle is $16$, what is the length of $YZ$?

$\mathrm{(A)}\,4\quad\mathrm{(B)}\,8\quad\mathrm{(C)}\,6\sqrt{3}\quad\mathrm{(D)}\,4\sqrt{3}\quad\mathrm{(E)}\,4\sqrt{2}\quad\mathrm{(F)}\,12\quad\mathrm{(G)}\,6\quad\mathrm{(H)}\,\text{none of the above}$''',
r'''The quadrilateral $OYPZ$ has right angles at $O$, $Y$ and $Z$, so it is a rectangle (if $P$ is an endpoint of a diameter it degenerates, and the statement below still holds).
'''+asy(fig,'5.5cm')+r'''
The diagonals of a rectangle are equal, so $YZ=OP=8$, the radius, wherever $P$ is on the circle. The answer is $\boxed{\mathrm{(B)}\ 8}$.''',
'Circles|Rectangles|Perpendicular lines',2,
note='Apparently 2006 iTest Problem 8 (not named in the post).')

# ---------------- 1743778 MATHCOUNTS 2015 Chapter Sprint 24
fig=r'''pair A=(-4,2),B=(1,2),C=(-1,5),A1=(4,2),B1=(-1,2),C1=(1,5),X=(0,3.5);
draw((-5,0)--(5,0),gray,Arrow(5));draw((0,-0.5)--(0,6.2),gray,Arrow(5));
fill(B1--B--X--cycle,lightgray);
draw(A--B--C--cycle,linewidth(0.9));draw(A1--B1--C1--cycle,blue+linewidth(0.9));
dot(A);dot(B);dot(C);dot(A1);dot(B1);dot(C1);dot(X);
label("$A$",A,SW);label("$B$",B,S);label("$C$",C,N);
label("$A'$",A1,SE,blue);label("$B'$",B1,S,blue);label("$C'$",C1,N,blue);
label("$X$",X,dir(15));label("$x$",(5,0),S);label("$y$",(0,6.2),E);'''
b.add(1743778,1,r'''Points $A$, $B$ and $C$ have coordinates $(-4,2)$, $(1,2)$ and $(-1,5)$, respectively. If triangle $ABC$ is reflected across the $y$-axis, what is the area of the region that is the intersection of triangle $ABC$ and its reflection? Express your answer as a decimal to the nearest tenth.''',
r'''The reflection is $A'(4,2)$, $B'(-1,2)$, $C'(1,5)$. Both triangles have their bases on the line $y=2$, and the overlap lies above the segment from $B'(-1,2)$ to $B(1,2)$, bounded by side $BC$ of the first triangle and side $B'C'$ of the second.
'''+asy(fig,'6cm')+r'''
Line $BC$ has slope $\dfrac{5-2}{-1-1}=-\dfrac32$, so it is $y=2-\dfrac32(x-1)$; by symmetry $B'C'$ is $y=2+\dfrac32(x+1)$. They meet on the $y$-axis at $X=(0,3.5)$. The other sides $AC$ and $A'C'$ lie outside this region (for example $AC$ is at $x\le-1$). So the overlap is triangle $B'BX$ with base $2$ and height $1.5$, of area $\dfrac12\cdot2\cdot1.5=\boxed{1.5}$.''',
'Reflections|Coordinate geometry|Triangles|Lengths, perimeter, and area',3,source=src('MATHCOUNTS',2015,'Chapter',24,rnd='Sprint'))

# ---------------- 1743701 ITEST
b.add(1743701,1,r'''Let $I,T,E,S$ be distinct positive integers such that the product $ITEST=2006$. What is the largest possible value of the sum $I+T+E+S+T+2006$?

$\textbf{(A) } 2086\quad\textbf{(B) } 4012\quad\textbf{(C) } 2144$''',
r'''$ITEST=I\cdot E\cdot S\cdot T^2=2006=2\cdot17\cdot59$ is squarefree, so $T^2$ divides it only if $T=1$. Then $IES=2006$ with $I,E,S$ distinct and different from $1$, so $\{I,E,S\}=\{2,17,59\}$ (a product of three integers greater than $1$ equal to a product of three primes uses exactly those primes). The sum is $2+17+59+1+1+2006=\boxed{2086}$, choice $\textbf{(A)}$; it is the only possible value, hence the largest.''',
'Prime factorisation|Factors and multiples',2,
note='Apparently 2006 iTest Problem 3 (not named in the post); the post quotes only three choices.')

# ---------------- 1743705 dancing couples
b.add(1743705,1,r'''Four married couples go ballroom dancing one evening. The men are Henry, Peter, Louis and Roger; the women are Elizabeth, Jeanne, Mary and Anne. Henry's wife is not dancing with her husband but with Elizabeth's husband. Roger and Anne are not dancing. Peter is playing the trumpet and Mary is playing the piano (so neither is dancing). Anne's husband is not Peter. Who is Roger's wife?

$\textbf{(A) } \text{Elizabeth} \quad\textbf{(B) }\text{Jeanne}\quad\textbf{(C) }\text{Mary}\quad\textbf{(D) }\text{Anne}$''',
r'''The people not dancing are Roger, Anne, Peter and Mary, so the dancers are Henry, Louis, Elizabeth and Jeanne, in two couples. Henry's wife is dancing with Elizabeth's husband, who is not Henry, so Henry's wife is not Elizabeth; being a dancer, she is Jeanne. Jeanne's partner is then Louis, so Louis is Elizabeth's husband. The remaining men, Peter and Roger, are married to Mary and Anne, and Anne's husband is not Peter. So Roger's wife is $\boxed{\textbf{(D)}\ \text{Anne}}$.''',
'Logical deduction',2,
note='Apparently 2006 iTest Problem 4 (not named in the post).')

# ---------------- 1743710 2^2006 mod 7
b.add(1743710,1,r'''What is the remainder when $2^{2006}$ is divided by $7$?

$\textbf{(A) }0\quad\textbf{(B) }1\quad\textbf{(C) }2\quad\textbf{(D) }3\quad\textbf{(E) }4\quad\textbf{(F) }5$''',
r'''Since $2^3=8\equiv1\pmod7$ and $2006=3\cdot668+2$, we get $2^{2006}=(2^3)^{668}\cdot2^2\equiv4\pmod7$. The answer is $\boxed{\textbf{(E)}\ 4}$.''',
'Modular exponentiation|Remainders and congruences',1,
note='Apparently 2006 iTest Problem 6 (not named in the post).')

# ---------------- 1743711 17 consecutive integers
b.add(1743711,1,r'''The sum of $17$ consecutive integers is $2006$. Find the second largest of these integers.

$\textbf{(A) }17\quad\textbf{(B) }72\quad\textbf{(C) }95\quad\textbf{(D) }101\quad\textbf{(E) }102\quad\textbf{(F) }111\quad\textbf{(G) }125$''',
r'''The sum of an odd number of consecutive integers is the number of terms times the middle term, so the middle (ninth) term is $\dfrac{2006}{17}=118$. The integers are $110,\dots,126$, and the second largest is $118+7=\boxed{\textbf{(G)}\ 125}$.''',
'Arithmetic sequences|Summation',1,
note='Apparently 2006 iTest Problem 7 (not named in the post).')

# ---------------- 1741712 9x+17y=541
b.add(1741712,1,r'''Find all pairs of positive integers $(x,y)$ such that $9x+17y=541$.''',
r'''Reduce modulo $9$: $17y\equiv541\pmod9$, i.e.\ $-y\equiv1$, so $y\equiv8\pmod9$. Since $17y<541$, $y\le31$, so $y\in\{8,17,26\}$, giving $x=\dfrac{541-17y}{9}=45,\,28,\,11$. The solutions are
\[
\boxed{(x,y)=(45,8),\ (28,17),\ (11,26)}.
\]
(All integer solutions are $(x,y)=(45-17t,\ 8+9t)$, $t\in\mathbb Z$.)''',
'Linear Diophantine equations|Remainders and congruences',2,
note='The post asks how to "factor" 9x + 17y = 541; read as solving it in positive integers.')

# ---------------- 1742347 necklace
b.add(1742347,1,r'''In how many ways can $3$ red beads, $5$ blue beads, $2$ orange beads, $2$ white beads and $4$ black beads be arranged on a necklace? Beads of the same colour are identical, and two necklaces are the same if one can be rotated or reflected into the other.''',
r'''There are $16$ beads; use Burnside's lemma with the dihedral group of order $32$ acting on the arrangements of the beads at the vertices of a regular $16$-gon.
\begin{itemize}
\item \textbf{Identity:} all $\dfrac{16!}{3!\,5!\,2!\,2!\,4!}=302702400$ arrangements.
\item \textbf{Rotations by $r\ne0$ steps:} the vertices fall into $\gcd(r,16)$ cycles of equal length $L=\dfrac{16}{\gcd(r,16)}\ge2$, and a fixed arrangement is constant on each cycle, so every colour count would be a multiple of $L$. But $3$ is odd, so no arrangement is fixed.
\item \textbf{Reflections through two opposite beads} ($8$ of them): the two beads on the axis are fixed and the other $14$ form $7$ pairs. The colours with odd counts (red and blue) must each have one bead on the axis: $2$ ways to place them. The $7$ pairs then get $1$ red, $2$ blue, $1$ orange, $1$ white, $2$ black: $\dfrac{7!}{1!\,2!\,1!\,1!\,2!}=1260$ ways. So $2520$ fixed arrangements each.
\item \textbf{Reflections through two opposite gaps} ($8$ of them): all $16$ beads are in $8$ pairs, so every count would be even; none is fixed.
\end{itemize}
The number of necklaces is
\[
\dfrac{302702400+8\cdot2520}{32}=\dfrac{302722560}{32}=\boxed{9460080}.
\]''',
'Burnside\'s lemma|Circular arrangements|Multiset permutations',6,
note='Burnside count; the method was checked against brute force on smaller necklaces.')

# ---------------- 1743083 2018 AMC 8 variants
fig=r'''pair[] V;for(int i=0;i<8;++i)V[i]=dir(22.5+45*i);
draw(V[0]--V[1]--V[2]--V[3]--V[4]--V[5]--V[6]--V[7]--cycle,linewidth(0.9));
draw(V[0]--V[2]--V[4]--V[6]--cycle,blue+linewidth(1));draw(V[1]--V[3]--V[5]--V[7]--cycle,gray+dashed);
for(int i=0;i<8;++i)dot(V[i]);'''
b.add(1743083,1,r'''Four of the eight vertices of a regular octagon are chosen at random and joined to form a quadrilateral. What is the probability that none of the sides of the quadrilateral is also a side of the octagon?''',
r'''The quadrilateral (with its vertices in cyclic order) has a side of the octagon exactly when two chosen vertices are adjacent on the octagon. So we need $4$ of the $8$ vertices of a cycle with no two adjacent. Between consecutive chosen vertices there must be at least one unchosen vertex, and there are only $8-4=4$ unchosen ones, so exactly one unchosen vertex lies in each gap: the chosen vertices alternate. That gives $2$ sets, the two inscribed squares (one in blue, the other gray dashed):
'''+asy(fig,'4cm')+r'''
The probability is $\dfrac{2}{\dbinom84}=\dfrac2{70}=\boxed{\dfrac1{35}}$.''',
'Probability|Combinations|Regular polygons',3,
note='A variation (by the poster) of 2018 AMC 8 Problem 23.')
b.add(1743083,2,r'''How many powers of $4$ lie between $2^8+1$ and $2^{18}+1$, inclusive?''',
r'''The powers of $4$ are $4^k=2^{2k}$. We need $257\le 2^{2k}\le 262145$. Since $4^4=256<257$ and $4^9=2^{18}=262144\le262145<4^{10}$, the values are $k=5,6,7,8,9$: $\boxed{5}$ powers of $4$.''',
'Exponents|Powers of two',1,
note='A variation of 2018 AMC 8 Problem 25 (which asks for perfect cubes).')
fig=r'''real a=4; pair k=(0.42,0.55);
pair A=(0,0),B=(a,0),C=(a,0)+a*k,D=a*k;
pair Ep=A+(0,a),F=B+(0,a),G=C+(0,a),H=D+(0,a);
pair J=(F+B)/2,I=(H+D)/2;
fill(Ep--J--C--I--cycle,lightgray+opacity(0.6));
draw(A--B--F--Ep--cycle,linewidth(0.9));draw(Ep--H--G--F,linewidth(0.9));draw(B--C--G,linewidth(0.9));
draw(A--D,dashed+gray);draw(D--C,dashed+gray);draw(D--H,dashed+gray);
draw(Ep--J--C,blue+linewidth(0.9));draw(C--I--Ep,blue+dashed);
dot(J);dot(I);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,E);label("$D$",D,dir(160));
label("$E$",Ep,W);label("$F$",F,dir(-10));label("$G$",G,NE);label("$H$",H,NW);
label("$J$",J,dir(-50));label("$I$",I,1.5*dir(35));'''
b.add(1743083,3,r'''In cube $ABCDEFGH$, face $ABCD$ is the bottom face and $E,F,G,H$ are directly above $A,B,C,D$ respectively, so $C$ and $E$ are opposite vertices. Points $J$ and $I$ are the midpoints of edges $FB$ and $HD$. The plane through $E$, $J$, $C$, $I$ cuts the cube into two pieces. What fraction of the volume of the cube is the piece $EFGHICJ$ (the piece containing the top face $EFGH$)?''',
r'''Let $O$ be the centre of the cube. The half-turn (point reflection) about $O$ maps the cube to itself and swaps opposite vertices and opposite edges: $E\leftrightarrow C$, and edge $FB\leftrightarrow$ edge $HD$ with their midpoints $J\leftrightarrow I$. So it maps the plane $EJCI$ to itself. (The plane does pass through $O$, the midpoint of $EC$.)
'''+asy(fig,'5.5cm')+r'''
The half-turn also swaps the two sides of this plane: for example $G$, on the same side as $F$ and $H$, goes to $A$ on the other side. Hence the two pieces are congruent, and the piece $EFGHICJ$ has $\boxed{\dfrac12}$ of the cube's volume. (Its cross-section $EJCI$ is a rhombus.)''',
'Cubes and rectangular prisms|Volume|Symmetry',3,
note='The post (a variation of 2018 AMC 8 Problem 24) asks for "the volume of EFGHICJ" but gives no edge length and no figure; the labelling of the original problem is stated and the record asks for the fraction of the cube volume.')
fig=r'''real s=6; pair A=(0,0),B=(s,0),C=(s,s),D=(0,s),Ep=(s/2,s),F=(2s/3,2s/3);
fill(A--F--Ep--D--cycle,lightgray);fill(B--F--C--cycle,paleblue);
draw(A--B--C--D--cycle,linewidth(0.9));draw(A--C);draw(B--Ep);
dot(Ep);dot(F);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);label("$E$",Ep,N);label("$F$",F,dir(-20));'''
b.add(1743083,4,r'''Point $E$ is the midpoint of side $\overline{CD}$ in square $ABCD$, and $\overline{BE}$ meets diagonal $\overline{AC}$ at $F$. The area of quadrilateral $AFED$ is $45$. What is the area of triangle $BFC$?''',
r'''Let the side be $s$ and use coordinates $A=(0,0)$, $B=(s,0)$, $C=(s,s)$, $D=(0,s)$, $E=\left(\dfrac s2,s\right)$. Triangles $FAB$ and $FCE$ are similar (since $AB\parallel CE$) with ratio $AB:CE=2:1$, so $F$ divides $AC$ in the ratio $2:1$: $F=\left(\dfrac{2s}3,\dfrac{2s}3\right)$.
'''+asy(fig,'5cm')+r'''
Triangle $CEF$ has base $CE=\dfrac s2$ and height $s-\dfrac{2s}{3}=\dfrac s3$, so area $\dfrac{s^2}{12}$; hence $[AFED]=[ACD]-[CEF]=\dfrac{s^2}2-\dfrac{s^2}{12}=\dfrac{5s^2}{12}=45$, so $s^2=108$. Triangle $BFC$ has base $BC=s$ and height $s-\dfrac{2s}3=\dfrac s3$ (the horizontal distance from $F$ to $BC$), so
\[
[BFC]=\dfrac{s^2}{6}=\boxed{18}.
\]''',
'Squares|Similarity|Area ratios|Coordinate geometry',3,
note='A variation of 2018 AMC 8 Problem 22 (which asks for the area of the square, 108).')
b.add(1743083,5,r'''How many positive three-digit integers have a remainder of $2$ when divided by $5$, a remainder of $5$ when divided by $7$, and a remainder of $7$ when divided by $11$?''',
r'''Numbers $\equiv7\pmod{11}$: $7,18,29,40,\dots$; of these, $\equiv5\pmod7$ first at $40$ ($40=35+5$). So $n\equiv40\pmod{77}$: $40,117,194,\dots$; the first $\equiv2\pmod5$ is $117$. By the Chinese remainder theorem the solutions are $n\equiv117\pmod{385}$. The three-digit ones are $117$, $502$, $887$ (the next is $1272$): $\boxed{3}$ integers.''',
'Chinese remainder theorem|Remainders and congruences',3,
note='A variation (by the poster) of 2017 AMC 8 Problem 23 (remainders 2, 5, 7 modulo 6, 9, 11 in the original).')

# ---------------- 1743378 AIME 2015 I #10
b.add(1743378,1,r'''Let $f(x)$ be a third-degree polynomial with real coefficients satisfying
\[
|f(1)|=|f(2)|=|f(3)|=|f(5)|=|f(6)|=|f(7)|=12 .
\]
Find $|f(0)|$. Justify in particular why $f$ takes the same value at $1$, $5$, $6$ and the opposite value at $2$, $3$, $7$.''',
r'''Each of the six numbers $x\in\{1,2,3,5,6,7\}$ is a root of $f(x)-12$ or of $f(x)+12$. Both are cubic polynomials, so each has at most three roots; hence each has exactly three of the six numbers as roots. Write
\[
f(x)-12=a(x-p)(x-q)(x-r),\qquad f(x)+12=a(x-u)(x-v)(x-w),
\]
with $\{p,q,r,u,v,w\}=\{1,2,3,5,6,7\}$ (the same leading coefficient $a$). Subtracting, the $x^2$ coefficients agree, so $p+q+r=u+v+w=\dfrac{1+2+3+5+6+7}{2}=12$. The triples from the set with sum $12$ are $\{1,5,6\}$ and $\{2,3,7\}$ (and these are complementary), so one of $f\mp12$ vanishes at $1,5,6$ and the other at $2,3,7$. (This is the precise form of the ``bends'' argument: a cubic cannot alternate more often.)

The $x$ coefficients must agree too, and they do: $1\cdot5+5\cdot6+6\cdot1=41=2\cdot3+3\cdot7+7\cdot2$. The constant terms then determine $a$. Say $f(x)-12=a(x-1)(x-5)(x-6)$ and $f(x)+12=a(x-2)(x-3)(x-7)$. Subtracting,
\[
-24=a\bigl[(x-1)(x-5)(x-6)-(x-2)(x-3)(x-7)\bigr]=a\bigl[(41x-30)-(41x-42)\bigr]=12a,
\]
so $a=-2$, and $f(0)=12+a(-1)(-5)(-6)=12+60=72$. (With the roles exchanged, $f$ is replaced by $-f$.) Hence $|f(0)|=\boxed{72}$.''',
'Polynomials|Polynomial roots|Vieta\'s formulas|Absolute value',6,source=src('AIME',2015,None,10,paper='I'),
note='The post asks about a step of the AoPS wiki solution; the record states the problem and gives a rigorous version of that step.')

# ---------------- 1742862 triangles with perimeter 30
fig=r'''pair A=(0,0),B=(12,0);real a=8,c=10;real x=(12^2+c^2-a^2)/(2*12);pair C=(x,sqrt(c^2-x^2));
draw(A--B--C--cycle,linewidth(0.9));
label("$c$",(A+B)/2,S);label("$b$",(A+C)/2,NW);label("$a$",(B+C)/2,NE);'''
b.add(1742862,1,r'''How many non-congruent triangles with integer side lengths have perimeter $30$? Find a method that organises the count.''',
r'''Let the sides be $a\le b\le c$ with $a+b+c=30$. The triangle inequality reduces to $a+b>c$, i.e.\ $30-c>c$, so $c\le14$; and $c\ge\dfrac{30}{3}=10$.
'''+asy(fig,'4cm')+r'''
For each $c$, the pairs $a\le b\le c$ with $a+b=30-c$ have $b$ running from $\left\lceil\dfrac{30-c}{2}\right\rceil$ to $c$:
\[
\begin{array}{c|ccccc}
c&10&11&12&13&14\\\hline
a+b&20&19&18&17&16\\
b&10&10,11&9..12&9..13&8..14\\
\text{count}&1&2&4&5&7
\end{array}
\]
The total is $1+2+4+5+7=\boxed{19}$. (A closed form: for even perimeter $n$ the count is the integer nearest to $\dfrac{n^2}{48}$; here $\dfrac{900}{48}=18.75$, giving $19$.)''',
'Triangle inequality|Systematic counting|Partitions and compositions',3,
note='The post asks for a method faster than casework; the organised count by the longest side is given, with the known closed form as a remark.')

# ---------------- 1742840 blue pencils
b.add(1742840,1,r'''I have nine pencils. At least one of them is blue. In any group of four pencils, at least two have the same colour. In any group of five pencils, at most three have the same colour. How many pencils are blue?''',
r'''If there were four different colours, one pencil of each would form a group of four with no two the same colour; so there are at most three colours. If some colour had four or more pencils, four of them plus any fifth pencil would be a group of five with at least four of the same colour; so each colour has at most three pencils. With nine pencils, at most three colours and at most three per colour, there are exactly three colours with three pencils each. Blue is one of them, so there are $\boxed{3}$ blue pencils.''',
'Pigeonhole principle|Logical deduction',3)

# ---------------- 1729666 race to 5 points
b.add(1729666,1,r'''Alice and Bob play a game in which Bob repeatedly flips a weighted coin: on heads Bob gets a point, and on tails Alice gets a point. They play until one of them has $5$ points. If the probability of heads is $\dfrac23$, what is the probability that Bob reaches $5$ points first?''',
r'''Bob wins exactly when his fifth point comes before Alice's fifth, i.e.\ when the game ends on a head with Alice having $k\in\{0,1,2,3,4\}$ points. The game then lasts $5+k$ flips, the last being heads and the first $4+k$ containing $k$ tails in any order:
\[
P=\sum_{k=0}^{4}\dbinom{4+k}{k}\left(\dfrac23\right)^5\left(\dfrac13\right)^k=\dfrac{32}{243}\left(1+\dfrac53+\dfrac{15}{9}+\dfrac{35}{27}+\dfrac{70}{81}\right)=\dfrac{32}{243}\cdot\dfrac{526}{81}=\boxed{\dfrac{16832}{19683}}.
\]
(Equivalently: imagine all $9$ flips are made; Bob wins exactly when at least $5$ of the $9$ are heads, so $P=\sum_{j=5}^{9}\dbinom9j\left(\dfrac23\right)^j\left(\dfrac13\right)^{9-j}$, which gives the same value, about $0.855$.)''',
'Binomial probability|Probability',4)

# ---------------- 1742842 Chip and Dale
b.add(1742842,1,r'''The houses of a market are arranged in a circle. Chip and Dale each count the houses clockwise, starting from different houses. Chip's $4$th house is Dale's $16$th house, and Chip's $12$th house is Dale's $7$th house. How many houses are in the market?''',
r'''Let there be $n$ houses. Since Dale counts a $16$th house, $n\ge16$. Both count clockwise, so Dale's number of a house is Chip's number plus a constant $c$, modulo $n$. Then $16\equiv4+c$ and $7\equiv12+c\pmod n$, so $c\equiv12$ and $c\equiv-5$, giving $17\equiv0\pmod n$. With $n\ge16$, $n=\boxed{17}$. (Check: with $c=12$, Chip's $4$th is Dale's $16$th, and Chip's $12$th is Dale's $24-17=7$th.)''',
'Remainders and congruences|Logical deduction',3,
note='"Chip\'s 4th house is 16 of Dale\'s house" read as Dale\'s 16th house.')

# ---------------- 1742992 pig pen
b.add(1742992,1,r'''A farmer builds a rectangular pig pen against a long barn, which serves as one side; the other three sides use $42$ feet of fencing. What is the maximum possible area of the pen?''',
r'''Let the two sides perpendicular to the barn have length $w$; the side parallel to the barn is $42-2w$. The area is
\[
A=w(42-2w)=-2\left(w-\dfrac{21}2\right)^2+\dfrac{441}{2},
\]
which is largest at $w=10.5$ feet (with the side along the barn $21$ feet), giving $\boxed{220.5}$ square feet.''',
'Quadratic equations|Maxima and minima|Completing the square',2)
b.add(1742992,2,r'''A farmer builds a rectangular pig pen against a long barn, which serves as one side; the other three sides use $42$ feet of fencing. If the pen must have area $200$ square feet, what is the length of each of the two sides perpendicular to the barn? Give the smaller of the two possible answers, to the nearest tenth of a foot.''',
r'''With perpendicular sides $w$ and the side along the barn $42-2w$, we need $w(42-2w)=200$, i.e.\ $w^2-21w+100=0$, so
\[
w=\dfrac{21\pm\sqrt{441-400}}{2}=\dfrac{21\pm\sqrt{41}}{2}.
\]
The smaller value is $\dfrac{21-\sqrt{41}}{2}\approx\boxed{7.3}$ feet (the larger is about $13.7$ feet).''',
'Quadratic equations',2)

# ---------------- 1743013 horizontal line in triangle
fig=r'''pair A=(0,8),B=(2,0),C=(8,0),T=(1.5,2),U=(6,2);
draw((-1,0)--(9.5,0),gray,Arrow(5));draw((0,-0.8)--(0,9.3),gray,Arrow(5));
fill(A--T--U--cycle,lightgray);
draw(A--B--C--cycle,linewidth(0.9));draw((-0.6,2)--(9,2),blue);
dot(T);dot(U);
label("$A(0,8)$",A,E);label("$B(2,0)$",B,S);label("$C(8,0)$",C,S);label("$T$",T,1.5*dir(145));label("$U$",U,NE);label("$y=t$",(9,2),N,blue);'''
b.add(1743013,1,r'''Triangle $ABC$ has vertices $A(0,8)$, $B(2,0)$, $C(8,0)$. A horizontal line $y=t$ meets segment $\overline{AB}$ at $T$ and segment $\overline{AC}$ at $U$, forming triangle $ATU$ with area $13.5$. Compute $t$.''',
r'''Since $TU\parallel BC$, triangle $ATU$ is similar to triangle $ABC$ with ratio $k=\dfrac{8-t}{8}$, the ratio of their heights from $A$.
'''+asy(fig,'5.5cm')+r'''
Triangle $ABC$ has base $BC=6$ and height $8$, so area $24$. Areas scale by $k^2$: $24k^2=13.5$ gives $k^2=\dfrac9{16}$, $k=\dfrac34$, so $8-t=6$ and $t=\boxed{2}$. (Then $T=(1.5,2)$, $U=(6,2)$, $TU=4.5$, and $\dfrac12\cdot4.5\cdot6=13.5$.)''',
'Similarity|Area ratios|Coordinate geometry|Triangles',2,
note='The poster asks for a slicker method; the similarity (area ratio) method is given.')

# ---------------- 1742873 AMC 8 2013 #25 (alias)
b.add(1742873,1,r'''A ball of radius $2$ inches rolls along a track made of three semicircular arcs of radii $100$, $60$ and $80$ inches, joined smoothly. On the first and third arcs the ball rolls on the concave side, and on the second arc on the convex side. How far does the centre of the ball travel from the start of the first arc to the end of the third?''',
r'''The centre stays at distance $2$ from the track, so it moves on semicircles of radii $100-2=98$, $60+2=62$ and $80-2=78$. The distance is $\pi(98+62+78)=\boxed{238\pi}$ inches.''',
'Circles|Arcs and chords',3,source=src('AMC 8',2013,None,25),
note='The post asks why 2 is subtracted on the first and last arcs; repeat of an earlier record (aliased).')

# ---------------- 1742771 MATHCOUNTS 2015 Chapter Team 9
b.add(1742771,1,r'''On a coordinate plane, a path consists of a series of moves, each in the positive $x$- or the positive $y$-direction. The first move is $1$ unit long, the second $2$ units, the third $3$ units, and so on. How many such paths start at the origin and end at $(14,14)$?''',
r'''The moves have lengths $1,2,\dots,m$ with total $1+2+\dots+m=28$, so $m=7$. A path is determined by the set of move lengths that go in the $x$-direction, which must sum to $14$ (the rest then also sum to $14$). Count subsets of $\{1,\dots,7\}$ with sum $14$, sorted by size:
\begin{itemize}
\item three elements: $\{7,6,1\},\{7,5,2\},\{7,4,3\},\{6,5,3\}$;
\item four elements: their complements $\{2,3,4,5\},\{1,3,4,6\},\{1,2,5,6\},\{1,2,4,7\}$;
\item two or fewer elements give at most $7+6=13$, and five or more are complements of those.
\end{itemize}
So there are $\boxed{8}$ paths.''',
'Combinations|Systematic counting|Lattice paths',4,source=src('MATHCOUNTS',2015,'Chapter',9,rnd='Team'))

# ---------------- 1742540 five problems
fig=r'''pair O=(0,0);pair u=(3,4)/5,v=(5,12)/13,w=unit(u+v);
draw((-0.3,0)--(5,0),gray,Arrow(5));draw((0,-0.3)--(0,5.4),gray,Arrow(5));
draw(O--5.2*u,linewidth(0.9));draw(O--4.9*v,linewidth(0.9));draw(O--5.3*w,blue+dashed);
draw(O--u,red+linewidth(1),Arrow(4));draw(O--v,red+linewidth(1),Arrow(4));draw(u--u+v--v,red+dotted);
label("$y=\dfrac43x$",5.2*u,E);label("$y=\dfrac{12}5x$",4.9*v,N);label("$y=\dfrac74x$",5.3*w,NE,blue);
label("$x$",(5,0),S);label("$y$",(0,5.4),W);'''
b.add(1742540,1,r'''What is the slope of the line that bisects the acute angle formed by $y=\dfrac43x$ and $y=\dfrac{12}{5}x$?''',
r'''Both lines pass through the origin. Their unit direction vectors in the first quadrant are $\left(\dfrac35,\dfrac45\right)$ and $\left(\dfrac5{13},\dfrac{12}{13}\right)$, and the angle between these is acute (their dot product $\dfrac{63}{65}$ is positive). The sum of two unit vectors lies along the bisector of the angle between them (the parallelogram they span is a rhombus):
\[
\left(\dfrac35+\dfrac5{13},\ \dfrac45+\dfrac{12}{13}\right)=\left(\dfrac{64}{65},\dfrac{112}{65}\right).
\]
'''+asy(fig,'5cm')+r'''
The bisector has slope $\dfrac{112}{64}=\boxed{\dfrac74}$. (Check: the tangent of the angle between lines of slopes $m_1,m_2$ is $\left|\dfrac{m_1-m_2}{1+m_1m_2}\right|$; for $\dfrac74$ with $\dfrac43$ this is $\dfrac{\dfrac5{12}}{\dfrac{10}3}=\dfrac18$, and for $\dfrac74$ with $\dfrac{12}5$ it is $\dfrac{\dfrac{13}{20}}{\dfrac{26}5}=\dfrac18$.)''',
'Angle bisectors|Slope|Coordinate geometry|Vectors',4)
b.add(1742540,2,r'''What is the largest integer $k$ such that $100!$ is divisible by $8^k$?''',
r'''By Legendre's formula the exponent of $2$ in $100!$ is
\[
\left\lfloor\dfrac{100}2\right\rfloor+\left\lfloor\dfrac{100}4\right\rfloor+\left\lfloor\dfrac{100}8\right\rfloor+\left\lfloor\dfrac{100}{16}\right\rfloor+\left\lfloor\dfrac{100}{32}\right\rfloor+\left\lfloor\dfrac{100}{64}\right\rfloor=50+25+12+6+3+1=97 .
\]
Since $8^k=2^{3k}$, we need $3k\le97$, so $k=\boxed{32}$.''',
'Factorials|Prime factorisation|Floor and ceiling functions',2)
b.add(1742540,3,r'''A solid cube is formed from $125$ unit cubes. A set of unit cubes is removed, leaving behind a smaller solid cube. In how many different ways can this be done? (For example, there are $8$ ways to remove $61$ unit cubes from the original $5\times5\times5$ cube to leave a cube with edges of $4$ units.)''',
r'''The remaining cube has edge $k\in\{1,2,3,4\}$, and its position is fixed by choosing its starting position in each of the three directions, $6-k$ choices each. So there are $(6-k)^3$ ways for each $k$, and the number of ways is
\[
5^3+4^3+3^3+2^3=125+64+27+8=\boxed{224}.
\]''',
'Counting shapes in figures|Perfect cubes|Multiplication principle',2)
b.add(1742540,4,r'''For how many integers $n$ with $50\le n\le99$ is the sum of the first $n$ positive odd integers a factor of $n!$?''',
r'''The sum of the first $n$ odd numbers is $n^2$, and $n^2\mid n!$ exactly when $n\mid(n-1)!$.
\begin{itemize}
\item If $n$ is prime, no factor of $(n-1)!$ is divisible by $n$, so $n\nmid(n-1)!$.
\item If $n$ is composite and not the square of a prime, write $n=ab$ with $1<a<b<n$; both $a$ and $b$ appear in $(n-1)!$, so $n\mid(n-1)!$.
\item If $n=p^2$ with $p\ge3$, then $p$ and $2p$ are distinct factors of $(n-1)!$, so $p^2\mid(n-1)!$. (In fact no square of a prime lies in $[50,99]$, since $7^2=49$ and $11^2=121$.)
\end{itemize}
So we count the composite numbers in $[50,99]$. There are $50$ integers, and the primes among them are $53,59,61,67,71,73,79,83,89,97$, ten in all. The answer is $50-10=\boxed{40}$.''',
'Factorials|Prime numbers|Divisibility|Summation',4)
b.add(1742540,5,r'''Four distinct positive integers have six pairwise sums, which take exactly five distinct values: $27,41,44,47$ and $61$ (so one sum occurs twice). What is the smallest of the four integers?''',
r'''Let the integers be $a<b<c<d$. Then
\[
a+b<a+c<\{a+d,\ b+c\}<b+d<c+d .
\]
Each integer appears in three of the six sums, so the six sums total $3(a+b+c+d)$. With $a+b=27$ and $c+d=61$ (the smallest and largest sums), $a+b+c+d=88$ and the six sums total $264$. The five distinct values total $220$, so the repeated sum is $44$, and the sums are $27,41,44,44,47,61$. Thus $a+c=41$, $b+d=47$ and $a+d=b+c=44$. From $a+b=27$, $a+c=41$, $b+c=44$ we get $2a=27+41-44=24$, so $a=\boxed{12}$ (and $b=15$, $c=29$, $d=32$, which check).''',
'Systems of linear equations|Logical deduction',3)

b.save()
