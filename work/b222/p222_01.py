from qb import *
b=Bank('p222_01')

# ---------------- 1784477 temperature scales
b.add(1784477,1,r'''On the Celsius scale water freezes at $0^\circ$ and boils at $100^\circ$. On the Sulesic scale water freezes at $20^\circ$ and boils at $160^\circ$. Both scales are linear. What is the temperature on the Sulesic scale when it is $215^\circ$ on the Celsius scale?''',
r'''Between freezing and boiling the Celsius scale rises by $100$ degrees and the Sulesic scale by $160-20=140$ degrees, so one Celsius degree corresponds to $\dfrac{140}{100}=1.4$ Sulesic degrees. Since $0^\circ\text{C}$ is $20^\circ$ Sulesic,
\[
S=20+1.4\,C .
\]
For $C=215$ we get $S=20+1.4\cdot215=20+301=\boxed{321^\circ}$ on the Sulesic scale.''',
'Linear equations|Ratios, proportions, and variation|Unit conversion',2,
note='The (standard) assumption that the scales are linear is stated.')

# ---------------- 1784575 isosceles, QR^2 = PR*XR
fig=r'''pair Q=(-2,0),R=(2,0),P=(0,6),X=(1.2,2.4);
draw(P--Q--R--cycle,linewidth(0.9));
draw(Q--X,blue+linewidth(0.8));
dot(X);
label("$P$",P,N);label("$Q$",Q,SW);label("$R$",R,SE);label("$X$",X,E);
// equal sides PQ = PR
pair m1=(P+Q)/2,m2=(P+R)/2;
draw((m1-0.18*unit(rotate(90)*(P-Q)))--(m1+0.18*unit(rotate(90)*(P-Q))));
draw((m2-0.18*unit(rotate(90)*(R-P)))--(m2+0.18*unit(rotate(90)*(R-P))));
// equal segments QX = QR (double ticks)
pair m3=(Q+X)/2,m4=(Q+R)/2;
for(int k=-1;k<=1;k+=2){
 pair o3=0.08*k*unit(X-Q),o4=(0.08*k,0);
 draw((m3+o3-0.18*unit(rotate(90)*(X-Q)))--(m3+o3+0.18*unit(rotate(90)*(X-Q))),blue);
 draw((m4+o4-(0,0.18))--(m4+o4+(0,0.18)),blue);
}'''
b.add(1784575,1,r'''In triangle $PQR$, $PQ=PR$, and $X$ is a point on side $PR$ such that $QR^2=PR\cdot XR$. Prove that $QX=QR$.''',
r'''From $QR^2=PR\cdot XR$ we get
\[
\dfrac{QR}{PR}=\dfrac{XR}{QR}.
\]
Triangles $RQX$ and $RPQ$ share the angle at $R$ (the angle $QRX$ is the angle $PRQ$, because $X$ lies on $RP$), and the sides enclosing that angle are proportional: $\dfrac{RX}{RQ}=\dfrac{RQ}{RP}$. Hence, by SAS similarity, $\triangle RXQ\sim\triangle RQP$, with $R\to R$, $X\to Q$, $Q\to P$.
'''+asy(fig,'4.5cm')+r'''
Corresponding angles give $\angle RXQ=\angle RQP$. Since $PQ=PR$, the base angles of triangle $PQR$ are equal: $\angle RQP=\angle PRQ$. Therefore
\[
\angle QXR=\angle RQP=\angle PRQ=\angle QRX ,
\]
so triangle $QXR$ has equal angles at $X$ and $R$, and is isosceles with $QX=QR$. $\blacksquare$''',
'Similarity|Isosceles triangles|Triangles',3,
note='The figure uses PQ = PR = sqrt(40) and QR = 4, so XR = 16/sqrt(40), i.e. X is 0.4 of the way from R to P; QX = QR = 4 was checked with coordinates.')

# ---------------- 1784545 PQ parallel BC
fig=r'''pair B=(0,0),C=(6,0),A=(2,4.5);
pair P=A+(B-A)/3,Q=A+(C-A)/3;
draw(A--B--C--cycle,linewidth(0.9));
draw(P--Q,linewidth(0.9));
dot(P);dot(Q);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$P$",P,W);label("$Q$",Q,E);
label("$1.5$",(A+P)/2,W);label("$3$",(P+B)/2,W);
label("$1.3$",(A+Q)/2,NE);label("$x$",(Q+C)/2,NE);'''
b.add(1784545,1,r'''In triangle $ABC$, points $P$ and $Q$ lie on sides $AB$ and $AC$ with $PQ\parallel BC$. If $AP=1.5$ cm, $PB=3$ cm and $AQ=1.3$ cm, find $QC$.''',
r'''Since $PQ\parallel BC$, triangles $APQ$ and $ABC$ are similar (corresponding angles at $P,B$ and at $Q,C$ are equal), so $\dfrac{AP}{AB}=\dfrac{AQ}{AC}$, or equivalently (basic proportionality theorem) $\dfrac{AP}{PB}=\dfrac{AQ}{QC}$.
'''+asy(fig,'4.5cm')+r'''
With $QC=x$:
\[
\dfrac{1.5}{3}=\dfrac{1.3}{x}\ \Longrightarrow\ x=\dfrac{3\cdot1.3}{1.5}=2.6 .
\]
So $QC=\boxed{2.6\text{ cm}}$.''',
'Similarity|Parallel lines|Triangles|Ratios, proportions, and variation',2)

# ---------------- 1776535 factorise marathon P1, P2
b.add(1776535,1,r'''Factorise $x^2+2xy+y^2$.''',
r'''This is a perfect square trinomial: $(x+y)^2=x^2+2xy+y^2$. Hence
\[
x^2+2xy+y^2=\boxed{(x+y)^2}.
\]''',
'Factoring|Algebraic expressions and identities',1)
b.add(1776535,2,r'''A rectangle has area $x^2-y^2$, where $x>y>0$. Express possible side lengths of the rectangle in terms of $x$ and $y$ by factorising the area.''',
r'''By the difference of squares,
\[
x^2-y^2=(x+y)(x-y).
\]
Both factors are positive because $x>y>0$, so the rectangle can have sides $\boxed{x+y\text{ and }x-y}$; indeed $(x+y)(x-y)=x^2-y^2$.''',
'Difference of squares|Factoring',1,
note='The post says "the 2 sides of the square"; it means the rectangle. The condition x > y > 0 is added so that the side lengths are positive.')

# ---------------- 1784532 folded square
fig=r'''real s=5;
draw((0,0)--(s,0)--(s,s)--(0,s)--cycle,linewidth(0.9));
for(int k=1;k<5;++k) draw((k,0)--(k,s),dashed);
label("$s$",(s/2,0),S);label("$s$",(0,s/2),W);
pair o=(7,0);
filldraw(shift(o)*((0,0)--(1,0)--(1,s)--(0,s)--cycle),paleblue,linewidth(0.9));
label("$\dfrac{s}{5}$",o+(0.5,0),S);label("$s$",o+(1,s/2),E);
label("square",(s/2,s),N);label("folded",o+(0.5,s),N);'''
b.add(1784532,1,r'''A square sheet of paper is folded along four broken lines, parallel to one side, that divide it into $5$ equal strips, so that the strips lie exactly on top of one another. The rectangle that results from the folding has perimeter $180$ cm. What is the area of the original square?''',
r'''Let the side of the square be $s$ cm. The broken lines cut it into five strips of size $s\times\dfrac s5$, and after folding only one strip is visible:
'''+asy(fig,'5cm')+r'''
The rectangle has perimeter
\[
2\left(s+\dfrac s5\right)=\dfrac{12s}{5}=180\ \Longrightarrow\ s=75 .
\]
So the square has area $75^2=\boxed{5625\text{ cm}^2}$. (No trial and error is needed: write the perimeter in terms of $s$ and solve the linear equation.)''',
'Paper folding|Squares|Rectangles|Lengths, perimeter, and area|Linear equations',2,
note='The figure of the original problem is missing; the text determines it (the broken lines split the square into 5 equal strips, which are folded onto one another).')

# ---------------- 1784164 parallelogram, 2014 MATHCOUNTS State Sprint 25
fig=r'''void para(real a,real x,pair o,string nm){
 pair A=o,B=o+(a,0),C=o+(a+x,18),D=o+(x,18);
 draw(A--B--C--D--cycle,linewidth(0.9));
 draw(A--C,blue);draw(B--D,blue);
 draw(o+(0,18)--D,dashed);draw(A--o+(0,18),dashed);
 draw((o+(0,18))--(o+(2.2,18))--(o+(2.2,15.8))--(o+(0,15.8)));
 label("$18$",o+(0,9),W);
 label("$"+string(a)+"$",(A+B)/2,S);
 label("$A$",A,SW);label("$B$",B,S);label("$C$",C,NE);label("$D$",D,N);
 label("$AC=82$",o+(86,11),E);label("$BD=30$",o+(86,5),E);
 label(nm,o+(-9,9),W);
}
para(28,52,(0,0),"(i)");
para(52,28,(0,-36),"(ii)");'''
b.add(1784164,1,r'''The diagonals of a parallelogram have lengths $82$ cm and $30$ cm. One altitude of the parallelogram is $18$ cm long. What is the smallest possible area of the parallelogram, in square centimetres?''',
r'''Let the altitude $18$ be drawn to the side $AB$ of length $a$, and place $A=(0,0)$, $B=(a,0)$, $D=(x,18)$, $C=(a+x,18)$ (we may take $a+x>0$ by reflecting the figure if necessary). The diagonals are $AC$ and $BD$:
\[
AC^2=(a+x)^2+18^2,\qquad BD^2=(x-a)^2+18^2 .
\]
The diagonal ending on the far side at horizontal distance $a+x$ is the longer one, so $(a+x)^2+324=82^2=6724$ and $(x-a)^2+324=30^2=900$. Hence $a+x=80$ and $x-a=\pm24$, giving
\[
a=\dfrac{80-24}{2}=28\qquad\text{or}\qquad a=\dfrac{80+24}{2}=52 .
\]
'''+asy(fig,'10cm')+r'''
Both cases give genuine parallelograms: (i) $a=28$, $x=52$ and (ii) $a=52$, $x=28$. The area is base times height, $18a$, which is $504$ or $936$. The smallest possible area is $\boxed{504}$ square centimetres.''',
'Parallelograms|Diagonals|Coordinate geometry|Pythagorean theorem|Lengths, perimeter, and area',4,
source=src('MATHCOUNTS',2014,'State',25,rnd='Sprint'),
note='Both configurations were checked with coordinates (diagonals 82 and 30, altitude 18 to the side of length 28 or 52).')

# ---------------- 1784280 alternating sums
b.add(1784280,1,r'''Find the value of $-1+2-3+4-5+6-\cdots-23+24$.''',
r'''Group the terms in consecutive pairs:
\[
(-1+2)+(-3+4)+\cdots+(-23+24).
\]
There are $\dfrac{24}{2}=12$ pairs, each equal to $1$, so the sum is $\boxed{12}$.''',
'Pairing and grouping|Summation',1)
b.add(1784280,2,r'''Find the value of
\[
3\cdot(1+3+5-7+9+11+13-15+\cdots+89+91+93-95+97+99+101-103),
\]
where the odd numbers from $1$ to $103$ appear in order and every fourth one is subtracted.''',
r'''The odd numbers $1,3,\dots,103$ are $52$ numbers, which split into $13$ blocks of four consecutive odd numbers. The block starting at $8k+1$ ($k=0,1,\dots,12$) contributes
\[
(8k+1)+(8k+3)+(8k+5)-(8k+7)=16k+2 .
\]
(Check: $1+3+5-7=2$ and $97+99+101-103=194=16\cdot12+2$.) The sum inside the brackets is
\[
\sum_{k=0}^{12}(16k+2)=16\cdot\dfrac{12\cdot13}{2}+2\cdot13=1248+26=1274,
\]
and the requested value is $3\cdot1274=\boxed{3822}$.''',
'Pairing and grouping|Arithmetic sequences|Summation',3,source=src('Math Is Cool',2018,None,None),
note='Math Is Cool 2018 (as the post says). The pattern (every fourth odd number subtracted) is stated explicitly.')

# ---------------- 1784100 Heronian triangle, longest side 17
fig=r'''pair B=(0,0),C=(17,0),A=(154/17,72/17),H=(154/17,0);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--H,dashed);
draw((H.x,0)--(H.x+0.6,0)--(H.x+0.6,0.6)--(H.x,0.6));
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$H$",H,S);
label("$10$",(A+B)/2,NW);label("$9$",(A+C)/2,NE);label("$17$",(5,0),S);'''
b.add(1784100,1,r'''A Heronian triangle is a triangle with three integer side lengths and integer area. What is the least possible area of a Heronian triangle whose longest side has length $17$?''',
r'''Let the other two sides be $x\le y\le17$ and put $u=x+y$, $d=y-x\ge0$. The triangle inequality gives $u\ge18$, and $y\le17$ gives $u+d\le34$. Heron's formula $16A^2=(x+y+17)(x+y-17)(17+x-y)(17-x+y)$ becomes
\[
16A^2=(u^2-289)(289-d^2).
\]
If $u$ were even, $d$ would be even too, and the right side would be odd; so $u$ and $d$ are odd, $u\ge19$, $d\le34-u$.

\textbf{$u=19$.} Then $u^2-289=72$ and $A^2=\dfrac{9(289-d^2)}{2}$, so $\dfrac{289-d^2}{2}$ must be a perfect square. For $d=1,3,5,\dots,15$ this number is $144,140,132,120,104,84,60,32$; only $d=1$ works, giving $A^2=9\cdot144$, $A=36$, with sides $x=9$, $y=10$.

\textbf{$u=21$.} Then $u^2-289=152$ and $A^2=\dfrac{19(289-d^2)}{2}$, so $19$ must divide $\dfrac{289-d^2}{2}$ for some odd $d\le13$; the values $144,140,132,120,104,84,60$ are not multiples of $19$. No triangle.

\textbf{$u\ge23$.} Then $d\le11$, so $289-d^2\ge168$, and $u^2-289\ge240$; hence $A^2\ge\dfrac{240\cdot168}{16}=2520>36^2$.

So the least possible area is $\boxed{36}$, attained by the triangle with sides $9,10,17$: $s=18$ and $A=\sqrt{18\cdot9\cdot8\cdot1}=\sqrt{1296}=36$.
'''+asy(fig,'6cm')+r'''
Geometrically, the altitude $AH$ to the side $17$ has length $\dfrac{2\cdot36}{17}=\dfrac{72}{17}$, and $BH=\dfrac{154}{17}$, $HC=\dfrac{135}{17}$; the triangle is very flat, which is why its area is small.''',
'Heron\'s formula|Triangles|Triangle inequality|Casework|Perfect squares',4,
note='Checked by brute force over all integer sides x <= y <= 17: the least area is 36 (9, 10, 17), as the posted answer says.')

# ---------------- 1783820 Harry vs Voldemort
b.add(1783820,1,r'''Harry chooses two distinct integers $a,b$ and Voldemort chooses two distinct integers $c,d$, all from $\{1,2,\dots,9\}$, so that the four numbers $a,b,c,d$ are all different; every such choice is equally likely. If some two of the four numbers have a sum that is a perfect square, Voldemort spares Harry. Find the probability that Voldemort spares Harry.''',
r'''The set $\{a,b,c,d\}$ is a uniformly random $4$-element subset of $\{1,\dots,9\}$; there are $\dbinom94=126$ of them. Count the subsets in which \emph{no} two elements sum to a square. The possible square sums of two different numbers from $1$ to $9$ are $4,9,16$, coming from the pairs
\[
\{1,3\};\quad \{1,8\},\{2,7\},\{3,6\},\{4,5\};\quad \{7,9\}.
\]
Join two numbers when they form one of these pairs. The numbers split into three chains, $8-1-3-6$, $2-7-9$ and $4-5$, and we need $4$ numbers with no two joined. Counting sets of non-adjacent numbers by size:
\begin{itemize}
\item chain $8-1-3-6$: $1$ empty set, $4$ singletons, $3$ pairs ($\{8,3\},\{8,6\},\{1,6\}$), no triples;
\item chain $2-7-9$: $1$, $3$ singletons, $1$ pair ($\{2,9\}$);
\item chain $4-5$: $1$, $2$ singletons.
\end{itemize}
The number of good $4$-sets is the coefficient of $t^4$ in $(1+4t+3t^2)(1+3t+t^2)(1+2t)$. The first two factors multiply to $1+7t+16t^2+13t^3+3t^4$, so the coefficient is $3+2\cdot13=29$.

Hence Harry is put to death with probability $\dfrac{29}{126}$, and he is spared with probability
\[
1-\dfrac{29}{126}=\boxed{\dfrac{97}{126}}.
\]''',
'Probability|Complementary probability|Perfect squares|Casework|Combinations',4,
note='The condition "at least 2 items p, q of the set sum to a perfect square" is read as: some two different numbers of the four have a square sum. The integers are 1 to 9 (the interval 0 < x < 10). Checked by enumerating all 126 sets.')

# ---------------- 1783710 maximum of -a + sqrt(4-a^2)
b.add(1783710,1,r'''Find the greatest possible value of $-a+\sqrt{4-a^2}$, where $a$ is a real number with $-2\le a\le2$.''',
r'''By the Cauchy-Schwarz inequality (or the inequality $u+v\le\sqrt{2(u^2+v^2)}$),
\[
(-a)\cdot1+\sqrt{4-a^2}\cdot1\le\sqrt{1^2+1^2}\cdot\sqrt{(-a)^2+\left(\sqrt{4-a^2}\right)^2}=\sqrt2\cdot\sqrt{4}=2\sqrt2 .
\]
Equality holds when $-a=\sqrt{4-a^2}$, i.e.\ $a\le0$ and $a^2=2$, so $a=-\sqrt2$; then the value is $\sqrt2+\sqrt2=2\sqrt2$. The greatest value is $\boxed{2\sqrt2}$.

(AM-GM gives lower bounds for sums of positive terms; here we need an upper bound for a sum, which comes from comparing the sum with the sum of squares $a^2+(4-a^2)=4$. Equivalently, with $a=2\cos t$, $0\le t\le\pi$, the expression is $2\sin t-2\cos t=2\sqrt2\sin(t-45^\circ)\le2\sqrt2$.)''',
'Cauchy-Schwarz inequality|Maxima and minima|Radicals',3,
note='The domain -2 <= a <= 2 (where the square root is defined) is stated. The post asks why AM-GM does not apply; the solution explains this and uses Cauchy-Schwarz.')

# ---------------- 1783346 trapezoid 3,4,8,3
fig=r'''pair D=(0,0),C=(8,0),A=(1.8,2.4),B=(4.8,2.4),T=(3,0),H=(4.8,0);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(B--T,dashed);draw(B--H,dashed);
pair u1=unit(T-B),u2=unit(C-B);
draw((B+0.3*u1)--(B+0.3*(u1+u2))--(B+0.3*u2));
draw((H+(0.25,0))--(H+(0.25,0.25))--(H+(0,0.25)));
label("$A$",A,NW);label("$B$",B,N);label("$C$",C,SE);label("$D$",D,SW);label("$T$",T,S);label("$H$",H,S);
label("$3$",(A+B)/2,N);label("$3$",(A+D)/2,NW);label("$4$",(B+C)/2,NE);
label("$3$",(D+T)/2,S);label("$5$",(T+C)/2+(0.5,0),S);label("$3$",(B+T)/2+(-0.3,0.15),W);label("$h$",(B+H)/2,E);'''
b.add(1783346,1,r'''In trapezoid $ABCD$, $AB$ is parallel to $CD$, $AB=3$, $BC=4$, $CD=8$ and $DA=3$. Find the area of the trapezoid.''',
r'''Through $B$ draw the line parallel to $AD$, meeting $DC$ at $T$. Then $ABTD$ is a parallelogram, so $DT=AB=3$, $BT=AD=3$ and $TC=8-3=5$.
'''+asy(fig,'7cm')+r'''
Triangle $TBC$ has sides $3,4,5$, so it is right-angled at $B$. Its altitude from $B$ is the height $h$ of the trapezoid:
\[
h=\dfrac{TB\cdot BC}{TC}=\dfrac{3\cdot4}{5}=\dfrac{12}{5}.
\]
The area of the trapezoid is
\[
\dfrac{AB+CD}{2}\cdot h=\dfrac{3+8}{2}\cdot\dfrac{12}{5}=\boxed{\dfrac{66}{5}}.
\]
(The other reading, $BC\parallel DA$, is impossible: then the same construction would give a triangle with sides $3$, $8$ and $4-3=1$, which violates the triangle inequality.)''',
'Trapezoids|Right triangles|Pythagorean theorem|Parallelograms|Lengths, perimeter, and area',3,
note='The post says "AB is parallel to BC", a typo. AB parallel to CD is the only possible reading (BC parallel to DA would need a triangle with sides 1, 3, 8); this is explained in the solution. Coordinates D(0,0), C(8,0), A(1.8,2.4), B(4.8,2.4) confirm all four sides and the area 13.2.')

# ---------------- 1783613 isosceles trapezoid EF
fig=r'''pair D=(0,0),C=(4,0),A=(0.5,3),B=(3.5,3);
real t=15/31;
pair F=A+t*(D-A),Ep=B+t*(C-B),K=(1,0),G=A+t*(K-A);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(F--Ep,linewidth(0.9));
draw(A--K,dashed);
dot(F);dot(Ep);dot(G);dot(K);
label("$A$",A,NW);label("$B$",B,NE);label("$C$",C,SE);label("$D$",D,SW);
label("$F$",F,W);label("$E$",Ep,E);label("$G$",G,NE);label("$K$",K,S);
label("$3$",(A+B)/2,N);label("$1$",(D+K)/2,S);label("$3$",(K+C)/2,S);'''
b.add(1783613,1,r'''In isosceles trapezoid $ABCD$, $AB$ is parallel to $CD$, with $AB=3$ and $CD=4$. Segment $EF$ is drawn parallel to $CD$ with $E$ on $BC$ and $F$ on $AD$. If $AF:FD=15:16$, what is the length of $EF$?''',
r'''Draw through $A$ the line parallel to $BC$; it meets $FE$ at $G$ and $DC$ at $K$.
'''+asy(fig,'5cm')+r'''
$ABEG$ and $ABCK$ are parallelograms, so $GE=KC=AB=3$ and $DK=4-3=1$. Since $FG\parallel DK$, triangles $AFG$ and $ADK$ are similar with ratio $\dfrac{AF}{AD}=\dfrac{15}{31}$, so $FG=\dfrac{15}{31}\cdot1=\dfrac{15}{31}$. Therefore
\[
EF=FG+GE=\dfrac{15}{31}+3=\boxed{\dfrac{108}{31}}.
\]
(The trapezoid need not be isosceles for this argument; the height does not matter either.)''',
'Trapezoids|Similarity|Parallel lines|Ratios, proportions, and variation',3,
note='Checked with coordinates (height 3, and other heights). The figure uses height 3; the height is not given and does not affect the answer.')

# ---------------- 1783549 27 dice
fig=r'''pair v=(0.45,0.32);
pen[] col={palegreen,paleblue,pink};
int ext(int i){return (i==0||i==2)?1:0;}
for(int i=0;i<3;++i) for(int j=0;j<3;++j){
 filldraw((i,j)--(i+1,j)--(i+1,j+1)--(i,j+1)--cycle,col[ext(i)+ext(j)]);
 filldraw(((i,3)+j*v)--((i+1,3)+j*v)--((i+1,3)+(j+1)*v)--((i,3)+(j+1)*v)--cycle,col[ext(i)+ext(j)]);
 filldraw(((3,i)+j*v)--((3,i)+(j+1)*v)--((3,i+1)+(j+1)*v)--((3,i+1)+j*v)--cycle,col[ext(i)+ext(j)]);
}
draw((0,0)--(3,0)--(3,3)--(0,3)--cycle,linewidth(0.9));
draw((0,3)--(0,3)+3v--(3,3)+3v--(3,0)+3v--(3,0),linewidth(0.9));draw((3,3)--(3,3)+3v,linewidth(0.9));
filldraw(box((0,-1.0),(0.4,-0.6)),pink);label("$3$ faces",(0.5,-0.8),E);
filldraw(box((0,-1.8),(0.4,-1.4)),paleblue);label("$2$ faces",(0.5,-1.6),E);
filldraw(box((0,-2.6),(0.4,-2.2)),palegreen);label("$1$ face",(0.5,-2.4),E);'''
b.add(1783549,1,r'''A $3\times3\times3$ cube is formed by gluing together $27$ standard dice. What is the smallest possible sum of all the numbers showing on the surface of the large cube? (On a standard die the numbers on opposite faces add up to $7$.)''',
r'''Classify the $26$ dice that are visible by how many of their faces lie on the surface:
\begin{itemize}
\item the $8$ corner dice show $3$ faces, which meet at a vertex of the die and are pairwise adjacent;
\item the $12$ edge dice (middle of each edge) show $2$ adjacent faces;
\item the $6$ face-centre dice show $1$ face;
\end{itemize}
and the centre die is hidden.
'''+asy(fig,'4.5cm')+r'''
Three faces of a die meeting at a vertex contain no pair of opposite faces, so they show three different numbers, with sum at least $1+2+3=6$; and $1,2,3$ can indeed meet at a vertex, since no two of them are opposite ($1+6=2+5=3+4=7$). Two adjacent faces show different numbers with sum at least $1+2=3$, which is attainable. A single face shows at least $1$. Each die can be turned independently, so all these minima are achieved together, and the smallest total is
\[
8\cdot6+12\cdot3+6\cdot1=48+36+6=\boxed{90}.
\]''',
'Cubes and rectangular prisms|Bounding and extremal cases|Systematic counting',3)

# ---------------- 1783551 polynomial crossing the axis 10 times
b.add(1783551,1,r'''The graph of a polynomial function crosses the $x$-axis at exactly $10$ points. What are the minimum and the maximum possible degree of the polynomial? Which degrees are possible?''',
r'''Let $p$ be the polynomial. At each crossing point $p$ has a real root, so $p$ has at least $10$ distinct real roots and $\deg p\ge10$. The degree $10$ occurs, for example, for
\[
p(x)=(x-1)(x-2)\cdots(x-10),
\]
whose graph crosses the axis at $1,2,\dots,10$.

There is \emph{no maximum}: for every $k\ge0$, the polynomial $(x-1)(x-2)\cdots(x-10)\,(x^2+1)^k$ has degree $10+2k$ and the same sign as $(x-1)\cdots(x-10)$ everywhere, so its graph crosses the axis exactly at the same $10$ points.

On the other hand the degree must be \emph{even}. The graph crosses the axis exactly where $p$ changes sign, so between $x\to-\infty$ and $x\to+\infty$ the sign of $p$ changes exactly $10$ times, an even number. Hence $p(x)$ has the same sign for very large negative and very large positive $x$. For odd degree the leading term $cx^n$ has opposite signs at the two ends, so the degree cannot be odd.

Answer: the minimum degree is $\boxed{10}$, there is no maximum, and the possible degrees are exactly the even numbers $10,12,14,\dots$.''',
'Polynomials|Polynomial roots|Parity',4,
note='The post asks for a maximum degree; there is none. The record adds the observation that the degree must be even.')

# ---------------- 1783256 even three-digit numbers
b.add(1783256,1,r'''How many positive even three-digit numbers have the property that the sum of the hundreds digit and the tens digit equals the units digit?''',
r'''Let the number have digits $h,t,u$ with $h\ge1$ and $h+t=u$. The units digit $u$ is even, and $u=h+t\ge1$, so $u\in\{2,4,6,8\}$. For a fixed $u$, the hundreds digit can be any of $h=1,2,\dots,u$, and then $t=u-h$ is a digit from $0$ to $u-1$. So there are $u$ numbers for each $u$, and the total is
\[
2+4+6+8=\boxed{20}.
\]''',
'Digit problems|Systematic counting|Casework',2,source=src('MATHCOUNTS',None,None,None),
note='The post names MATHCOUNTS without year or round. Checked by brute force.')

# ---------------- 1783520 2021^n divides 2018!
b.add(1783520,1,r'''Determine the largest positive integer $n$ for which $2018!$ is divisible by $2021^n$.''',
r'''Factor $2021=43\cdot47$, with $43$ and $47$ prime. By Legendre's formula the exponents of these primes in $2018!$ are
\[
v_{43}(2018!)=\left\lfloor\dfrac{2018}{43}\right\rfloor+\left\lfloor\dfrac{2018}{43^2}\right\rfloor=46+1=47,\qquad
v_{47}(2018!)=\left\lfloor\dfrac{2018}{47}\right\rfloor=42,
\]
since $43^2=1849\le2018<47^2=2209$. As $2021^n=43^n47^n$, we need $n\le47$ and $n\le42$. The largest $n$ is $\boxed{42}$.''',
'Factorials|Prime factorisation|Divisibility|Floor and ceiling functions',3)

# ---------------- 1772864 two Korean problems
b.add(1772864,1,r'''Factorise $a^3(b-c)^3+b^3(c-a)^3+c^3(a-b)^3$.''',
r'''Put $x=a(b-c)$, $y=b(c-a)$, $z=c(a-b)$. Then
\[
x+y+z=ab-ac+bc-ab+ca-bc=0 .
\]
Using the identity $x^3+y^3+z^3-3xyz=(x+y+z)(x^2+y^2+z^2-xy-yz-zx)$, we get $x^3+y^3+z^3=3xyz$ whenever $x+y+z=0$. Hence
\[
a^3(b-c)^3+b^3(c-a)^3+c^3(a-b)^3=\boxed{3abc(a-b)(b-c)(c-a)}.
\]
(Check with $a=1,b=2,c=3$: the left side is $-1+8\cdot8-27=36$ and the right side is $3\cdot6\cdot(-1)(-1)\cdot2=36$.)''',
'Factoring|Algebraic expressions and identities|Sum and difference of cubes|Substitution',4)
fig=r'''pair B=(0,0),C=(5,0),A=(1.6,3);
draw(A--B--C--cycle,linewidth(0.9));
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);
label("$a$",(B+C)/2,S);label("$b$",(A+C)/2,NE);label("$c$",(A+B)/2,NW);'''
b.add(1772864,2,r'''A triangle has side lengths $a$, $b$, $c$. Let
\[
p=a^4+b^4+c^4-2\left(a^2b^2+b^2c^2+c^2a^2\right).
\]
Determine whether $p$ is positive or negative, and explain why.''',
r'''Complete a square:
\[
p=\left(a^2+b^2-c^2\right)^2-4a^2b^2 ,
\]
since $(a^2+b^2-c^2)^2=a^4+b^4+c^4+2a^2b^2-2a^2c^2-2b^2c^2$. By the difference of squares, twice,
\[
p=\left(a^2+b^2-c^2-2ab\right)\left(a^2+b^2-c^2+2ab\right)=\bigl((a-b)^2-c^2\bigr)\bigl((a+b)^2-c^2\bigr)
\]
\[
=(a-b-c)(a-b+c)(a+b-c)(a+b+c).
\]
'''+asy(fig,'4cm')+r'''
By the triangle inequality $a<b+c$, $b<a+c$ and $c<a+b$, so $a-b-c<0$ while $a-b+c>0$, $a+b-c>0$ and $a+b+c>0$. Hence $\boxed{p<0}$ for every triangle.

(In fact $p=-16K^2$, where $K$ is the area of the triangle, by Heron's formula.)''',
'Factoring|Difference of squares|Triangle inequality|Heron\'s formula|Inequalities',4)

# ---------------- 1783316 ax+by=1 has infinitely many solutions
b.add(1783316,1,r'''Let $a$ and $b$ be nonzero integers with $\gcd(a,b)=1$. Can the equation $ax+by=1$ have more than one solution in integers $x,y$? Describe all its integer solutions.''',
r'''Yes; it has infinitely many. By Bezout's identity there is at least one solution $(x_0,y_0)$. For every integer $t$,
\[
a(x_0+bt)+b(y_0-at)=ax_0+by_0+abt-abt=1,
\]
so $(x_0+bt,\ y_0-at)$ is a solution, and different $t$ give different solutions because $b\ne0$.

These are all the solutions. If $ax+by=1$, subtracting $ax_0+by_0=1$ gives $a(x-x_0)=-b(y-y_0)$. So $b$ divides $a(x-x_0)$, and since $\gcd(a,b)=1$, $b\mid x-x_0$; write $x-x_0=bt$. Then $abt=-b(y-y_0)$, so $y-y_0=-at$.

Answer: $\boxed{\text{yes: the solutions are }x=x_0+bt,\ y=y_0-at\ (t\in\mathbb Z)}$, infinitely many. For example $3x+5y=1$ has the solutions $(2,-1),(7,-4),(-3,2),\dots$.''',
'Linear Diophantine equations|HCF and LCM|Divisibility',3,
note='The post asks only whether there can be more than one solution; the record also asks for all solutions. Nonzero a, b are assumed.')

# ---------------- 1783275 p divides C(p,k)
b.add(1783275,1,r'''Let $p$ be a prime and $k$ an integer with $0<k<p$. Prove that $p$ divides $\dbinom pk=\dfrac{p!}{k!\,(p-k)!}$. Does the statement remain true if $p$ is replaced by a composite number?''',
r'''$\dbinom pk$ is an integer, and
\[
p!=\dbinom pk\cdot k!\,(p-k)! .
\]
The prime $p$ divides the left side. On the right, $k!$ and $(p-k)!$ are products of positive integers smaller than $p$ (because $1\le k\le p-1$ and $1\le p-k\le p-1$), and a prime dividing a product divides one of the factors, so $p\nmid k!\,(p-k)!$. Hence $p\mid\dbinom pk$. $\blacksquare$

For composite numbers the statement is false: for $n=4$ and $k=2$, $\dbinom42=6$ is not divisible by $4$. (The proof breaks down because $4$ divides $2!\cdot2!=4$.) So the answer to the second question is $\boxed{\text{no}}$.''',
'Combinatorial identities and binomial coefficients|Prime numbers|Divisibility|Factorials|Counterexamples',3,
note='The post writes p!/(n!(p-k)!); n! is a typo for k!. The question about composite p is answered with a counterexample.')

# ---------------- 1780436 triangular tray and samosas
fig=r'''pair A=(0,0),B=(10,0),C=(5,5*sqrt(3));
fill((0,0)--(1,0)--(0.5,sqrt(3)/2)--cycle,lightred);
for(int k=1;k<10;++k){
 draw(A+k/10*(C-A)--B+k/10*(C-B),gray);
}
for(int k=1;k<10;++k){draw(A+k/10*(B-A)--A+k/10*(B-A)+(10-k)/10*(C-A),gray);draw(B+k/10*(A-B)--B+k/10*(A-B)+(10-k)/10*(C-B),gray);}
draw(A--B--C--cycle,linewidth(0.9));
label("$50$",(5,0),S);label("$5$",(0.5,0),S);'''
b.add(1780436,1,r'''A tray is shaped like an equilateral triangle with side $50$ units. A samosa is shaped like an equilateral triangle with side $5$ units. What is the least number of samosas needed to cover the tray completely?''',
r'''The ratio of side lengths is $\dfrac{50}{5}=10$, so the area of the tray is $10^2=100$ times the area of one samosa. The samosas must cover the whole area of the tray, so at least $100$ are needed.

$100$ samosas suffice: dividing each side of the tray into $10$ equal parts and drawing the lines parallel to the sides through the division points cuts the tray into $1+3+5+\cdots+19=10^2=100$ equilateral triangles of side $5$ (the row $k$ from the top contains $2k-1$ triangles).
'''+asy(fig,'5.5cm')+r'''
So the least number is $\boxed{100}$, as the poster thought.''',
'Equilateral triangles|Colourings, tilings, and coverings|Scaling of length, area, and volume|Lengths, perimeter, and area',2,
note='The post asks for the "maximum number of Somucha we will need to fully cover the tray"; this is read as the least number that covers it. The poster\'s answer 100 is correct.')

# ---------------- 1783141 nth term of 1, 16, 56, 121
b.add(1783141,1,r'''The sequence $1,16,56,121,\dots$ has constant second differences. Find a formula for its $n$th term.''',
r'''The first differences are $15,40,65,\dots$ and the second differences are all $25$. A sequence with constant second difference $D$ is given by a quadratic $a_n=An^2+Bn+C$ with $2A=D$, because
\[
a_{n+1}-a_n=A(2n+1)+B,\qquad (a_{n+2}-a_{n+1})-(a_{n+1}-a_n)=2A .
\]
So $A=\dfrac{25}{2}$. The first difference $a_2-a_1=3A+B=15$ gives $B=15-\dfrac{75}{2}=-\dfrac{45}{2}$, and $a_1=A+B+C=1$ gives $C=1-\dfrac{25}{2}+\dfrac{45}{2}=11$. Hence
\[
a_n=\boxed{\dfrac{25n^2-45n+22}{2}}.
\]
Check: $a_1=1$, $a_2=\dfrac{100-90+22}{2}=16$, $a_3=\dfrac{225-135+22}{2}=56$, $a_4=\dfrac{400-180+22}{2}=121$, and the next term is $a_5=211$.''',
'Sequences and series|Pattern recognition|Systems of linear equations',3,
note='The post gives four terms and asks for a method; the record states that the second differences are constant (otherwise four terms do not determine the sequence).')

# ---------------- 1783108 Ellie's tests
b.add(1783108,1,r'''In the second-to-last test of the year Ellie scored $98$, and her average score increased by $1$. In the last test she scored $70$, and her average score decreased by $2$. How many tests did she take during the year?''',
r'''Before the second-to-last test, let Ellie have taken $n$ tests with average $m$, so her total was $nm$.

After scoring $98$: $\dfrac{nm+98}{n+1}=m+1$, so $nm+98=nm+n+m+1$, i.e.\ $n+m=97$.

After scoring $70$ the average drops by $2$ from $m+1$ to $m-1$: $\dfrac{nm+168}{n+2}=m-1$, so $nm+168=nm+2m-n-2$, i.e.\ $2m-n=170$.

Adding the two equations gives $3m=267$, so $m=89$ and $n=8$. She took $n+2=\boxed{10}$ tests. (Check: $8\cdot89=712$; $\dfrac{810}{9}=90$; $\dfrac{880}{10}=88=90-2$.)''',
'Averages and weighted averages|Systems of linear equations',3)

# ---------------- 1726380 chocolate bars, trisected corner
fig=r'''real w=2*sqrt(3);
pair A=(0,0),B=(6,0),C=(6,w),D=(0,w),P=(2,w);
fill(A--B--C--cycle,paleyellow);fill(A--C--P--cycle,palecyan);fill(A--P--D--cycle,pink);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--C,linewidth(0.8));draw(A--P,linewidth(0.8));
draw(arc(A,0.9,0,30));draw(arc(A,1.1,30,60));draw(arc(A,0.9,60,90));
label("$30^\circ$",A+1.45*dir(15),fontsize(8pt));label("$30^\circ$",A+1.6*dir(45),fontsize(8pt));label("$30^\circ$",A+1.45*dir(75),fontsize(8pt));
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);label("$P$",P,N);
label("$6$",(A+B)/2,S);label("$2\sqrt3$",(A+D)/2,W);label("$2$",(D+P)/2,N);label("$4$",(P+C)/2,N);
label("$M$",(4,1.1));label("$R$",(3.1,2.6));label("$K$",(0.55,2.75));'''
b.add(1726380,1,r'''Kyle has three identical chocolate bars, each a rectangular block of length $6$ and height (thickness) $1$; its width is not given. He gives one bar to each of his friends Meit and RJ and keeps one himself. Meit makes two straight vertical cuts from one corner of the top face of his bar that trisect the right angle at that corner, and one of the cuts runs along a diagonal of the top face (so the bar breaks into $3$ pieces). Meit gives the smallest piece to Kyle, keeps the biggest piece and gives the remaining piece to RJ. Kyle and RJ still have their own full bars. Let $K$, $R$ and $M$ be the total volumes of chocolate that Kyle, RJ and Meit now have. Find $K\cdot(R-M)$, assuming that the length $6$ is the longer side of the top face.''',
r'''Let the top face be the rectangle $ABCD$ with $AB=6$, cut from the corner $A$. The two cuts make angles of $30^\circ$ and $60^\circ$ with $AB$. A diagonal $AC$ makes an angle less than $45^\circ$ with the longer side $AB$, so the diagonal is the $30^\circ$ cut and the width is $BC=6\tan30^\circ=2\sqrt3$. The $60^\circ$ cut meets $DC$ at $P$ with $DP=AD\tan30^\circ=2\sqrt3\cdot\dfrac{1}{\sqrt3}=2$, so $PC=4$.
'''+asy(fig,'6.5cm')+r'''
With thickness $1$, the volumes of the pieces equal the areas of the triangles:
\[
[ABC]=\dfrac12\cdot6\cdot2\sqrt3=6\sqrt3,\qquad [ACP]=\dfrac12\cdot4\cdot2\sqrt3=4\sqrt3,\qquad [APD]=\dfrac12\cdot2\cdot2\sqrt3=2\sqrt3 .
\]
A full bar has volume $6\cdot2\sqrt3=12\sqrt3$. Kyle gets the smallest piece and RJ the middle one, and each also has a full bar; Meit keeps only the biggest piece:
\[
K=12\sqrt3+2\sqrt3=14\sqrt3,\qquad R=12\sqrt3+4\sqrt3=16\sqrt3,\qquad M=6\sqrt3 .
\]
Hence $K(R-M)=14\sqrt3\cdot10\sqrt3=\boxed{420}$.''',
'Rectangles|Special right triangles|Area decomposition|Volume|Lengths, perimeter, and area',4,
note='Local competition problem, rewritten for clarity. "Length 6" is read as the longer side of the top face (otherwise the width would be 6 sqrt 3 and the answer 3780); the cuts are read as vertical cuts through the whole thickness. "Kyle and RJ still have 1 full chocolate bar" is used: each of them has a full bar besides the piece.')

b.save()
