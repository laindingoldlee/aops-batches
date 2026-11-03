from qb import *
b=Bank('p226_01')

# ---------------- 1762570 square, bisector of angle APB
fig=r'''pair A=(0,0),B=(1,0),C=(1,1),D=(0,1);
real t=0.3; pair P=(t,1);
real pa=abs(P-A), pb=abs(P-B); pair Q=(pa/(pa+pb),0);
pair Q0=(sqrt(2)-1,0), Q1=(2-sqrt(2),0);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(P--A,linewidth(0.7));draw(P--B,linewidth(0.7));
draw(P--Q,blue+linewidth(0.8));
draw(Q0--Q1,red+linewidth(2.2));
real a1=degrees(A-P),a2=degrees(Q-P),a3=degrees(B-P);
draw(arc(P,0.14,a1,a2),linewidth(0.5));draw(arc(P,0.14,a2,a3),linewidth(0.5));
draw((P+0.11*dir((a1+a2)/2))--(P+0.17*dir((a1+a2)/2)),linewidth(0.5));
draw((P+0.11*dir((a2+a3)/2))--(P+0.17*dir((a2+a3)/2)),linewidth(0.5));
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);
label("$P$",P,N);label("$Q$",Q,NE);
label("$Q_0$",Q0,S,red);label("$Q_1$",Q1,S,red);'''
b.add(1762570,1,r'''Let $ABCD$ be a square of side length $1$, and let $P$ be a variable point on side $\overline{CD}$. Let $Q$ be the point where the bisector of $\angle APB$ meets $\overline{AB}$. As $P$ moves along $\overline{CD}$, the set of possible locations of $Q$ is a line segment. Find the length of this segment.''',
r'''Place $A=(0,0)$, $B=(1,0)$, $C=(1,1)$, $D=(0,1)$ and $P=(t,1)$ with $0\le t\le1$. By the angle bisector theorem in triangle $APB$,
\[
\dfrac{AQ}{QB}=\dfrac{PA}{PB},\qquad\text{so}\qquad AQ=\dfrac{PA}{PA+PB}=\dfrac{1}{1+\dfrac{PB}{PA}},
\]
where $PA=\sqrt{t^2+1}$ and $PB=\sqrt{(1-t)^2+1}$.
'''+asy(fig,'5.5cm')+r'''
As $t$ increases from $0$ to $1$, $PA$ increases and $PB$ decreases, so $\dfrac{PB}{PA}$ decreases and $AQ$ increases strictly and continuously. Hence $Q$ sweeps out the segment from $Q_0$ (for $P=D$) to $Q_1$ (for $P=C$), shown in red:
\[
AQ_0=\dfrac{1}{1+\sqrt2}=\sqrt2-1,\qquad AQ_1=\dfrac{\sqrt2}{\sqrt2+1}=2-\sqrt2 .
\]
The length of the segment is $(2-\sqrt2)-(\sqrt2-1)=\boxed{3-2\sqrt2}$.''',
'Squares|Angle bisectors|Angle bisector theorem|Loci and geometric constraints',4,
source=src('CMIMC',2018,None,None),
note='Title: "CMIMC 2018, DJ\'s Homemade Problem Collection"; the problem number is not given.')

# ---------------- 1762490 pizza and pepperoni
fig1=r'''real s=sin(pi/8); real r=s/(1+s);
draw(circle((0,0),1),linewidth(0.9));
for(int i=0;i<8;++i) draw((0,0)--dir(45*i),linewidth(0.6));
for(int i=0;i<8;++i) filldraw(circle((1-r)*dir(22.5+45*i),r),rgb(0.95,0.55,0.5),black+linewidth(0.5));'''
fig2=r'''real s=sin(pi/8); real r=s/(1+s);
pair O=(0,0), X=dir(0), Y=dir(45);
pair K=(1-r)*dir(22.5);
pair T=(K.x,0);
draw(O--X,linewidth(0.8));draw(O--Y,linewidth(0.8));draw(arc(O,1,0,45),linewidth(0.8));
filldraw(circle(K,r),rgb(0.95,0.55,0.5),black+linewidth(0.6));
draw(O--K,dashed);draw(K--(1)*dir(22.5),dashed);
draw(K--T,blue+linewidth(0.7));
draw((T+(-0.035,0))--(T+(-0.035,0.035))--(T+(0,0.035)),linewidth(0.4));
dot(O);dot(K);
label("$O$",O,W);label("$K$",K,NW);label("$T$",T,S);
label("$r$",(K+T)/2,E,blue);
label("$R-r$",(O+K)/2,N+0.6*W);
draw(arc(O,0.22,0,22.5),linewidth(0.5));
label("$22.5^\circ$",0.36*dir(11),E,fontsize(8pt));'''
b.add(1762490,1,r'''A circular cheese pizza is cut into $8$ congruent $45^\circ$ sectors. On each slice the largest possible circle of pepperoni is placed so that the whole pepperoni circle lies on that slice. What fraction of the pizza is covered by pepperoni?''',
r'''Let the pizza have radius $R$ and centre $O$. The largest circle inside a $45^\circ$ sector is tangent to both straight edges and to the arc, so its centre $K$ lies on the bisector of the sector, at distance $R-r$ from $O$, where $r$ is its radius.
'''+asy(fig1,'4.5cm')+asy(fig2,'6cm')+r'''
If $T$ is the point of tangency with one straight edge, then $KT\perp OT$ and $\angle KOT=22.5^\circ$, so
\[
r=KT=(R-r)\sin22.5^\circ\quad\Longrightarrow\quad \dfrac rR=\dfrac{s}{1+s},\qquad s=\sin22.5^\circ=\dfrac{\sqrt{2-\sqrt2}}{2}.
\]
The eight pepperoni circles cover $8\pi r^2$ out of $\pi R^2$, so the fraction covered is
\[
8\left(\dfrac{s}{1+s}\right)^2=\dfrac{8(2-\sqrt2)}{\left(2+\sqrt{2-\sqrt2}\right)^2}\approx\boxed{0.613}.
\]
(Here $s^2=\dfrac{2-\sqrt2}{4}$ and $1+s=\dfrac{2+\sqrt{2-\sqrt2}}{2}$.)''',
'Circles|Tangents|Trigonometry|Lengths, perimeter, and area',4,
note='Exact answer 8(2 - sqrt 2)/(2 + sqrt(2 - sqrt 2))^2, about 0.6128; checked numerically.')

# ---------------- 1762377 2019^2019 as a sum of squares
b.add(1762377,1,r'''Write $2019^{2019}$ as a sum of squares of positive integers using as few squares as possible, and prove that fewer squares are impossible.''',
r'''\textbf{One or two squares are impossible.} Since $2019=3\cdot673$ is not a perfect square and the exponent $2019$ is odd, the prime $3$ occurs in $2019^{2019}$ to the odd power $2019$, so $2019^{2019}$ is not a perfect square. Also $2019\equiv3\pmod4$, so $2019^{2019}\equiv3^{2019}\equiv(-1)^{2019}\equiv3\pmod4$. Every square is $\equiv0$ or $1\pmod4$, so a sum of two squares is $\equiv0,1$ or $2\pmod4$, never $3$. Hence $2019^{2019}$ is not a sum of two squares.

\textbf{Three squares suffice.} We have $2019=1849+121+49=43^2+11^2+7^2$. Multiplying by $2019^{2018}=\left(2019^{1009}\right)^2$,
\[
2019^{2019}=\left(43\cdot2019^{1009}\right)^2+\left(11\cdot2019^{1009}\right)^2+\left(7\cdot2019^{1009}\right)^2 .
\]
So the least number of squares is $\boxed{3}$, with the representation above.''',
'Perfect squares|Remainders and congruences|Exponents|Construction',4,
note='The post only says "write 2019^2019 as the sum of squares"; posed as finding a representation with the fewest squares (three) and proving two are impossible.')

# ---------------- 1762370 lowest number with digit sum 2018
b.add(1762370,1,r'''Find the smallest positive integer whose digit sum is $2018$, which contains the digit $0$ exactly once, and which contains each of the digits $1,2,\dots,9$ at least once.''',
r'''\textbf{Number of digits.} Let the number have $m$ nonzero digits (and one $0$). They include $1,2,\dots,8$ (sum $36$) and $m-8$ further digits, each at most $9$, so $36+9(m-8)\ge2018$, i.e.\ $9(m-8)\ge1982$, giving $m\ge229$. A number with fewer digits is smaller, so we look for the smallest number with $229$ nonzero digits and one zero, i.e.\ $230$ digits, if one exists.

\textbf{Which digits.} With $229$ nonzero digits, the total shortfall from all nines is $9\cdot229-2018=43$. The obligatory digits $1,\dots,8$ account for a shortfall of $8+7+\cdots+1=36$, so the $221$ other nonzero digits have total shortfall $7$ (a digit $d$ has shortfall $9-d$).

\textbf{Smallest arrangement.} The first digit cannot be $0$, so it is at least $1$; we can make it $1$. The second digit can be $0$. A second $1$ would have shortfall $8>7$, so there is exactly one $1$ and the third digit is at least $2$; it can be $2$. The fourth digit can be $2$ only if one of the other digits is a $2$, whose shortfall $7$ uses up the whole allowance; this forces the digits to be $0,1,2,2,3,4,5,6,7,8$ and $220$ nines. Any other choice makes the fourth digit at least $3$ and the number larger. With this multiset the smallest arrangement puts $1$ first, then $0$, then the rest in increasing order:
\[
\boxed{10223456789\cdots9}\quad(\text{the digits }1,0,2,2,3,4,5,6,7,8\text{ followed by }220\text{ nines}).
\]
Check: $1+0+2+2+3+4+5+6+7+8=38$ and $38+220\cdot9=2018$; it has $230$ digits.''',
'Digits and bases|Bounding and extremal cases|Digit problems',4,
note='"The other digits of the decimal system are contained at least once" read as each of 1-9 appearing at least once; checked by computer that no 229-digit number works and that the multiset is forced.')

# ---------------- 1762318 (x+a)(x-a)=y
fig=r'''pair B=(0,0),C=(sqrt(19),0);
real c=2,bb=3; real ang=acos((19+4-9)/(2*sqrt(19)*2));
pair A=c*dir(degrees(ang));
draw(A--B--C--cycle,linewidth(0.9));
draw(arc(A,0.35,degrees(B-A),degrees(C-A)),linewidth(0.6));
label("$120^\circ$",A+0.65*dir((degrees(B-A)+degrees(C-A))/2));
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);
label("$c$",(A+B)/2,NW);label("$b$",(A+C)/2,NE);label("$a$",(B+C)/2,S);'''
b.add(1762318,1,r'''In a triangle with side lengths $a,b,c$, let $b+c=x$ and $bc=y$. If $(x+a)(x-a)=y$, then the triangle is necessarily
\[
\textbf{(A)}\ \text{equilateral}\qquad\textbf{(B)}\ \text{right-angled}\qquad\textbf{(C)}\ \text{acute-angled}\qquad\textbf{(D)}\ \text{obtuse-angled}
\]''',
r'''The condition is $x^2-a^2=y$, that is, $(b+c)^2-a^2=bc$, or
\[
b^2+c^2-a^2=-bc .
\]
By the law of cosines, $b^2+c^2-a^2=2bc\cos A$, so $\cos A=-\dfrac12$ and $A=120^\circ$. The triangle is necessarily obtuse-angled: $\boxed{\textbf{(D)}}$.
'''+asy(fig,'5.5cm')+r'''
For example, $b=3$, $c=2$, $a=\sqrt{19}$ satisfies the condition: $x=5$ and $25-19=6=bc$.''',
'Law of cosines|Triangles|Trigonometry',2)

# ---------------- 1762308 cashier
b.add(1762308,1,r'''An absent-minded cashier switched the dollars and the cents when he cashed a cheque for Mr.\ Truck, giving him dollars instead of cents and cents instead of dollars. On his way home Mr.\ Truck dropped a $5$-cent coin, and then he found that he had exactly twice the amount of the original cheque. What was the amount of the cheque?''',
r'''Let the cheque be $x$ dollars and $y$ cents, with $0\le x,y\le99$ integers; in cents it is $100x+y$. He received $100y+x$ cents, and after losing $5$ cents,
\[
100y+x-5=2(100x+y)\quad\Longleftrightarrow\quad 98y=199x+5 .
\]
Modulo $98$: $199\equiv3$, so $3x+5\equiv0$, i.e.\ $3x\equiv93\pmod{98}$ and $x\equiv31\pmod{98}$ (as $\gcd(3,98)=1$). With $0\le x\le99$ this gives $x=31$, and then $y=\dfrac{199\cdot31+5}{98}=\dfrac{6174}{98}=63$. The cheque was for $\boxed{\$31.63}$. Check: he received $\$63.31$, and $\$63.31-\$0.05=\$63.26=2\cdot\$31.63$.''',
'Linear Diophantine equations|Remainders and congruences|Money and currency',4)

# ---------------- 1762175 reading the question
b.add(1762175,1,r'''If $2x-3=4x+2$, find $x^2-6$.''',
r'''From $2x-3=4x+2$ we get $-5=2x$, so $x=-\dfrac52$. Then $x^2-6=\dfrac{25}{4}-6=\boxed{\dfrac14}$. (The question asks for $x^2-6$, not for $x$.)''',
'Linear equations',1,
note='From an advice post about reading questions carefully; the example in it is used.')

# ---------------- 1762096 3-13-16 triangle
fig=r'''pair B=(0,0),C=(16,0),A=(12,5),H=(12,0);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--H,dashed+blue);
draw((H+(-0.5,0))--(H+(-0.5,0.5))--(H+(0,0.5)),linewidth(0.4));
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$H$",H,S);
label("$13$",(A+B)/2,NW);label("$\sqrt{41}$",(A+C)/2,NE);label("$16$",(B+C)/2,S);
label("$h$",(A+H)/2,W,blue);'''
b.add(1762096,1,r'''\begin{enumerate}
\item[(a)] Explain why there is no triangle with side lengths $3$, $13$ and $16$.
\item[(b)] The triangle with side lengths $\sqrt{41}$, $13$ and $16$ has area $40$. Find the length of the altitude to its longest side.
\end{enumerate}''',
r'''(a) Since $3+13=16$, the triangle inequality fails (the "triangle" would be a flat segment of area $0$), so no triangle has these side lengths, and certainly none of area $40$.

(b) The longest side is $16$ (as $\sqrt{41}<7<13$). If $h$ is the altitude to it, then $\dfrac12\cdot16\cdot h=40$, so $h=\boxed{5}$.
'''+asy(fig,'7cm')+r'''
Check: put $B=(0,0)$, $C=(16,0)$, $A=(12,5)$. Then $AB=\sqrt{144+25}=13$, $AC=\sqrt{16+25}=\sqrt{41}$, and the area is $\dfrac12\cdot16\cdot5=40$.''',
'Triangles|Triangle inequality|Altitudes|Lengths, perimeter, and area',1,
note='The posted data (a 3-13-16 triangle of area 40, Montgomery County Middle School Math League) are impossible, since 3 + 13 = 16. The intended answer only uses the longest side 16 and the area 40 (height 5); the record asks why 3-13-16 fails and uses the genuine triangle sqrt(41)-13-16 of area 40.')

# ---------------- 1762194 make 243 with six numbers
b.add(1762194,1,r'''Using only addition, write each of the numbers $243$, $248$ and $371$ as a sum of exactly six numbers taken from the list
\[
1,\ 2,\ 4,\ 9,\ 15,\ 31,\ 63,\ 127,\ 255,\ 480,
\]
where a number may be used more than once.''',
r'''Take the largest useful numbers first and fill in the rest.

$243$: using $127$ leaves $116$; using $63$ leaves $53$; using $31$ leaves $22$, which must be made from three numbers: $22=9+9+4$. So
\[
243=127+63+31+9+9+4 .
\]
$248$: as before, $248-127-63-31=27=9+9+9$, so
\[
248=127+63+31+9+9+9 .
\]
$371$: using $255$ leaves $116$, which is made exactly as above: $116=63+31+9+9+4$. So
\[
371=255+63+31+9+9+4 .
\]
Each sum uses exactly six numbers from the list. (A complete search shows that each of these representations is the only one with six numbers, and that none of the three numbers can be made with fewer than six.)''',
'Whole-number operations|Systematic counting|Construction',2,
note='The poster asks whether 243 (and also 248 and 371) can be made by adding six numbers from 1, 2, 9, 31, 255, 480, 4, 15, 63, 127 with repetition; all three are possible (verified by exhaustive search).')

# ---------------- 1761304 line through origin halves triangle
fig=r'''pair O=(0,0),A=(0,8),B=(2,0),C=(8,0);
real m=(-5+sqrt(41))/2;
pair P=(8/(4+m),8*m/(4+m)), Q=(8/(1+m),8*m/(1+m));
fill(A--P--Q--cycle,rgb(0.8,0.88,1));
draw((-0.5,0)--(10,0),Arrow(4));draw((0,-0.5)--(0,9),Arrow(4));
draw(A--B--C--cycle,linewidth(0.9));
draw(O--(9.2,9.2*m),red+linewidth(0.8));
dot(P);dot(Q);
label("$A(0,8)$",A,W);label("$B(2,0)$",B,S);label("$C(8,0)$",C,S);label("$O$",O,SW);
label("$P$",P,W);label("$Q$",Q,N);label("$y=mx$",(9.2,9.2*m),E,red);
label("$x$",(10,0),S);label("$y$",(0,9),W);'''
b.add(1761304,1,r'''Triangle $ABC$ has vertices $A(0,8)$, $B(2,0)$ and $C(8,0)$. A line through the origin cuts the area of triangle $ABC$ in half. Find the sum of the slope and the $y$-intercept of this line.''',
r'''The area of the triangle is $\dfrac12\cdot6\cdot8=24$. The line through the origin has $y$-intercept $0$; write it as $y=mx$ with $m>0$ (for $m\le0$ the line has $y\le0$ whenever $x\ge0$, so it misses the interior of the triangle, and the line $x=0$ touches it only at $A$). It crosses $AB$ (the line $4x+y=8$) at $P$ and $AC$ (the line $x+y=8$) at $Q$, cutting off triangle $APQ$.
'''+asy(fig,'6cm')+r'''
Points of $AB$ are $A+t(B-A)=(2t,8-8t)$ and points of $AC$ are $A+u(C-A)=(8u,8-8u)$. Solving with $y=mx$ gives
\[
t=\dfrac{4}{4+m}\ \ \Bigl(P=\Bigl(\dfrac{8}{4+m},\dfrac{8m}{4+m}\Bigr)\Bigr),\qquad u=\dfrac{1}{1+m}\ \ \Bigl(Q=\Bigl(\dfrac{8}{1+m},\dfrac{8m}{1+m}\Bigr)\Bigr).
\]
Triangle $APQ$ shares the angle at $A$ with triangle $ABC$, so $[APQ]=tu\,[ABC]$. We need $tu=\dfrac12$:
\[
\dfrac{4}{(4+m)(1+m)}=\dfrac12\iff m^2+5m+4=8\iff m^2+5m-4=0,
\]
so $m=\dfrac{-5+\sqrt{41}}{2}\approx0.70$ (the other root is negative). Then $t\approx0.85$ and $u\approx0.59$ lie in $(0,1)$, as required. The slope plus the $y$-intercept is
\[
\dfrac{-5+\sqrt{41}}{2}+0=\boxed{\dfrac{\sqrt{41}-5}{2}}.
\]''',
'Coordinate geometry|Slope|Area ratios|Triangles|Quadratic equations',4)

# ---------------- 1762011 four quarter circles in a unit square
figq=r'''pair A=(0,0),B=(1,0),C=(1,1),D=(0,1);
real h=sqrt(3)/2;
pair P1=(0.5,1-h),P2=(h,0.5),P3=(0.5,h),P4=(1-h,0.5);
path reg=arc(D,1,-60,-30)--arc(A,1,30,60)--arc(B,1,120,150)--arc(C,1,210,240)--cycle;
fill(reg,rgb(0.8,0.88,1));
draw(arc(A,1,0,90),linewidth(0.6));draw(arc(B,1,90,180),linewidth(0.6));
draw(arc(C,1,180,270),linewidth(0.6));draw(arc(D,1,270,360),linewidth(0.6));
draw(A--B--C--D--cycle,linewidth(0.9));
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);'''
figs=figq+r'''
draw(P1--P2--P3--P4--cycle,dashed);
dot(P1);dot(P2);dot(P3);dot(P4);
label("$P_1$",P1,S,fontsize(8pt));label("$P_2$",P2,E,fontsize(8pt));label("$P_3$",P3,N,fontsize(8pt));label("$P_4$",P4,W,fontsize(8pt));
draw(D--P1,gray+dotted);draw(D--P2,gray+dotted);'''
b.add(1762011,1,r'''Square $ABCD$ has side length $1$. Four quarter circles of radius $1$ are drawn inside the square, centred at $A$, $B$, $C$ and $D$. What is the area of the region that lies inside all four quarter circles (shaded)?
'''+asy(figq,'4.5cm'),
r'''Put $A=(0,0)$, $B=(1,0)$, $C=(1,1)$, $D=(0,1)$ and $h=\dfrac{\sqrt3}{2}$. The region is bounded by four arcs whose endpoints are
\[
P_1=\left(\tfrac12,1-h\right),\quad P_2=\left(h,\tfrac12\right),\quad P_3=\left(\tfrac12,h\right),\quad P_4=\left(1-h,\tfrac12\right);
\]
for instance $P_1$ is on the circles centred at $C$ and $D$ (it forms an equilateral triangle with $C$ and $D$), and $P_2$ is on the circles centred at $A$ and $D$. The arc $P_1P_2$ is part of the circle centred at $D$, and similarly for the other three arcs.
'''+asy(figs,'6cm')+r'''
\textbf{The square $P_1P_2P_3P_4$.} Its side is $P_1P_2=\sqrt2\left(h-\tfrac12\right)=\dfrac{\sqrt3-1}{\sqrt2}$, so its area is $\dfrac{(\sqrt3-1)^2}{2}=2-\sqrt3$.

\textbf{The four segments.} Seen from $D$, the directions to $P_1$ and $P_2$ make angles of $60^\circ$ and $30^\circ$ with side $DC$, so the arc $P_1P_2$ subtends $30^\circ=\dfrac{\pi}{6}$ at $D$. The circular segment between chord $P_1P_2$ and the arc has area
\[
\dfrac12\cdot1^2\left(\dfrac\pi6-\sin\dfrac\pi6\right)=\dfrac{\pi}{12}-\dfrac14 .
\]
\textbf{Total.} The area is
\[
2-\sqrt3+4\left(\dfrac\pi{12}-\dfrac14\right)=\boxed{1+\dfrac{\pi}{3}-\sqrt3}\approx0.315 .
\]''',
'Circles|Arcs and chords|Squares|Area decomposition|Lengths, perimeter, and area',5,
note='The figure was an image; the text ("area of the intersection of the four quarter circles" in a unit square) determines the standard configuration (quarter circles of radius 1 centred at the corners), which is stated and redrawn.')

# ---------------- 1761970 mulch
b.add(1761970,1,r'''Gale buys $12$ bags of mulch. Each bag contains $2$ cubic feet of mulch. What fraction of a cubic yard is the total amount of mulch? Express your answer as a common fraction.''',
r'''The total is $12\cdot2=24$ cubic feet. One cubic yard is $3\cdot3\cdot3=27$ cubic feet, so the mulch is $\dfrac{24}{27}=\boxed{\dfrac89}$ of a cubic yard. (Using $3$ instead of $27$ cubic feet per cubic yard is the usual mistake.)''',
'Unit conversion|Fractions',2)

# ---------------- 1761985 circumference 18 pi
fig=r'''draw(circle((0,0),1),linewidth(0.9));
dot((0,0));draw((0,0)--dir(25),linewidth(0.7));
label("$O$",(0,0),SW);label("$9$",0.5*dir(25),NW);'''
b.add(1761985,1,r'''The circumference of a circle is $18\pi$. What is the area of the circle? Express your answer in terms of $\pi$.''',
r'''From $2\pi r=18\pi$ the radius is $r=9$.
'''+asy(fig,'3cm')+r'''
The area is $\pi r^2=\boxed{81\pi}$.''',
'Circles|Lengths, perimeter, and area',1,
note='P1 of a MATHCOUNTS geometry marathon; only P1 is in the post.')

# ---------------- 1761309 17m+3n=1
b.add(1761309,1,r'''Find all pairs of integers $(m,n)$ with $17m+3n=1$, and show how the solution $m=-1$, $n=6$ can be found.''',
r'''\textbf{One solution by the Euclidean algorithm.} $17=5\cdot3+2$ and $3=1\cdot2+1$. Working backwards,
\[
1=3-2=3-(17-5\cdot3)=6\cdot3-1\cdot17,
\]
so $m=-1$, $n=6$ works. (Equivalently: $17m+3n=1$ forces $17m\equiv1\pmod3$, i.e.\ $2m\equiv1$, so $m\equiv2\equiv-1\pmod3$; the choice $m=-1$ gives $3n=18$, $n=6$.)

\textbf{All solutions.} If $17m+3n=1=17(-1)+3\cdot6$, then $17(m+1)=3(6-n)$. Since $\gcd(17,3)=1$, $3\mid m+1$; write $m+1=3k$, and then $6-n=17k$. Conversely every such pair works. So the solutions are
\[
\boxed{(m,n)=(-1+3k,\ 6-17k),\ k\in\mathbb Z}.
\]''',
'Linear Diophantine equations|Remainders and congruences',2,
note='The post (titled IMC 2004 Q21) asks only why m = -1, n = 6 solves 17m + 3n = 1; the contest problem itself is not stated, so the record asks for all integer solutions and the method.')

# ---------------- 1761719 lattice points on a segment
fig=r'''for(int i=3;i<=15;++i) draw((i,-2)--(i,7),gray(0.8)+linewidth(0.3));
for(int j=-2;j<=7;++j) draw((3,j)--(15,j),gray(0.8)+linewidth(0.3));
pair A=(3,-2),B=(15,7);
draw(A--B,linewidth(0.9));
for(int k=0;k<=3;++k) dot(A+k*(4,3),red);
label("$A(3,-2)$",A,SE);label("$B(15,7)$",B,NW);
label("$(7,1)$",A+(4,3),SE,fontsize(8pt));label("$(11,4)$",A+(8,6),SE,fontsize(8pt));'''
b.add(1761719,1,r'''Let $A(x_1,y_1)$ and $B(x_2,y_2)$ be distinct lattice points (points with integer coordinates).
\begin{enumerate}
\item[(a)] Prove that the number of lattice points on segment $AB$, including $A$ and $B$, is $\gcd\left(|x_2-x_1|,|y_2-y_1|\right)+1$ (where $\gcd(0,k)=k$).
\item[(b)] How many lattice points lie on the segment from $(3,-2)$ to $(15,7)$, including the endpoints?
\end{enumerate}''',
r'''(a) Let $a=x_2-x_1$, $b=y_2-y_1$ (not both $0$) and $g=\gcd(|a|,|b|)\ge1$. The points of the segment are $X(t)=(x_1+ta,\ y_1+tb)$ for $0\le t\le1$, and $X(t)$ is a lattice point exactly when $ta$ and $tb$ are both integers.

If $t=\dfrac kg$ with $k$ an integer, then $ta=k\cdot\dfrac ag$ and $tb=k\cdot\dfrac bg$ are integers. Conversely, by B\'ezout there are integers $\alpha,\beta$ with $\alpha a+\beta b=g$; if $ta$ and $tb$ are integers, then $tg=\alpha(ta)+\beta(tb)$ is an integer, so $t=\dfrac kg$ for some integer $k$. Hence the lattice points correspond to $t=0,\dfrac1g,\dfrac2g,\dots,1$, and there are exactly $g+1$ of them.

(b) Here $a=12$, $b=9$ and $g=\gcd(12,9)=3$, so there are $\boxed{4}$ lattice points: $(3,-2)$, $(7,1)$, $(11,4)$, $(15,7)$, spaced by $\left(\dfrac{12}{3},\dfrac93\right)=(4,3)$.
'''+asy(fig,'6.5cm'),
'Lattice points|Coordinate geometry|HCF and LCM|Linear Diophantine equations',3,
note='The post asks for the formula for the number of lattice points on the segment between two points (assumed to be lattice points) and an explanation; the record asks for a proof and adds a numerical example.')

# ---------------- 1761969 mode median mean
b.add(1761969,1,r'''Find the mode, the median and the mean of the data set $5,8,1,5,10,5$.''',
r'''In order the data are $1,5,5,5,8,10$. The mode is $5$ (it occurs three times). With six values the median is the mean of the third and fourth, $\dfrac{5+5}{2}=5$. The mean is $\dfrac{1+5+5+5+8+10}{6}=\dfrac{34}{6}=\dfrac{17}{3}$. So the mode is $\boxed{5}$, the median is $\boxed{5}$ and the mean is $\boxed{\dfrac{17}{3}}$.''',
'Mean|Median|Mode',1,
note='P1 of a math marathon; only P1 is in the post.')

# ---------------- 1761513 x^y = y^(x-y)
b.add(1761513,1,r'''Find all pairs of positive integers $(x,y)$ such that $x^y=y^{x-y}$.''',
r'''\textbf{$x\le y$.} If $x<y$, then $y^{x-y}<1\le x^y$, impossible. If $x=y$, then $x^x=1$, so $x=y=1$, which works.

\textbf{$x>y$.} If $y=1$, then $x=1$, a contradiction; so $y\ge2$. Since $x>y$, $y^{x-y}=x^y>y^y$, so $x-y>y$. Put $r=\dfrac{x-y}{y}>1$. For each prime $p$, comparing exponents gives $y\,v_p(x)=(x-y)\,v_p(y)$, i.e.\ $v_p(x)=r\,v_p(y)$; hence $x=y^r$. But $x=y(1+r)$, so
\[
y^{r-1}=r+1 .
\]
Write $r=\dfrac pq$ in lowest terms. Raising to the power $q$: $y^{p-q}=\left(\dfrac{p+q}{q}\right)^q$. The left side is an integer, while $\gcd(p+q,q)=\gcd(p,q)=1$, so the right side is an integer only if $q=1$. Thus $r$ is an integer, $r\ge2$, and $y^{r-1}=r+1$ with $y\ge2$.
\begin{itemize}
\item $r=2$: $y=3$, $x=y(1+r)=9$. Check: $9^3=729=3^6$.
\item $r=3$: $y^2=4$, $y=2$, $x=8$. Check: $8^2=64=2^6$.
\item $r\ge4$: $y^{r-1}\ge2^{r-1}>r+1$ (true for $r=4$ since $8>5$, and the left side doubles while the right side grows by $1$), no solution.
\end{itemize}
The solutions are $\boxed{(x,y)=(1,1),\ (8,2),\ (9,3)}$.''',
'Diophantine equations|Exponents|Prime factorisation|Bounding and extremal cases',6,
note='Checked by brute force for x, y < 200.')

# ---------------- 1761577 disjoint subsets
b.add(1761577,1,r'''For a finite set $Z$, let $|Z|$ denote the number of elements of $Z$. How many ordered pairs $(A,B)$ of disjoint subsets of $\{1,2,3,4,5,6,7,8\}$ satisfy
\[
|A|+|B|\in A\qquad\text{and}\qquad|A|-|B|\in B\ ?
\]''',
r'''Let $a=|A|$ and $b=|B|$. Since $a-b\in B$, $B$ is nonempty and $a-b\ge1$; so $b\ge1$, $a\ge b+1$, and $a+b\le8$ because $A$ and $B$ are disjoint. The two numbers $a+b\in A$ and $a-b\in B$ are distinct. Choose the other $a-1$ elements of $A$ from the remaining $6$ numbers, then the other $b-1$ elements of $B$ from the remaining $7-a$: there are $\dbinom{6}{a-1}\dbinom{7-a}{b-1}$ pairs.
\begin{itemize}
\item $b=1$, $2\le a\le7$: $\sum_{a=2}^{7}\dbinom6{a-1}=6+15+20+15+6+1=63$.
\item $b=2$, $3\le a\le6$: $15\cdot4+20\cdot3+15\cdot2+6\cdot1=156$.
\item $b=3$, $4\le a\le5$: $20\cdot\dbinom32+15\cdot\dbinom22=60+15=75$.
\item $b\ge4$ would need $a\ge5$ and $a+b\ge9$: impossible.
\end{itemize}
The total is $63+156+75=\boxed{294}$.''',
'Sets and inclusion–exclusion|Combinations|Casework',4,
note='The post\'s "x in Z means that the element a can be found" is a typo. Pairs (A, B) are counted as ordered; verified by brute force over all 3^8 assignments.')

# ---------------- 1761688 2012 MATHCOUNTS National Target 6
fig=r'''pair P=(1,1),Q=(9,1),R=(9,13);
draw(P--Q--R--cycle,linewidth(0.9));
draw((Q+(-0.5,0))--(Q+(-0.5,0.5))--(Q+(0,0.5)),linewidth(0.4));
label("$(1,1)$",P,SW);label("$(9,1)$",Q,SE);label("$(9,n)$",R,NE);
label("$8$",(P+Q)/2,S);label("$n-1$",(Q+R)/2,E);'''
b.add(1761688,1,r'''A lattice point is a point $(x,y)$ with both $x$ and $y$ integers. A triangle has vertices $(1,1)$, $(9,1)$ and $(9,n)$. For what integer $n>1$ are there exactly $560$ lattice points strictly inside the triangle?''',
r'''Let $m=n-1>0$. The triangle is right-angled at $(9,1)$ with legs $8$ and $m$, so its area is $4m$. (The sketch is not to scale.)
'''+asy(fig,'3.6cm')+r'''
Lattice points on the boundary: the horizontal leg contributes $8$ steps, the vertical leg $m$ steps, and by the gcd rule the hypotenuse from $(1,1)$ to $(9,n)$ contains $\gcd(8,m)$ steps; so the boundary has $B=8+m+g$ points, where $g=\gcd(8,m)$. By Pick's theorem $A=I+\dfrac B2-1$, so
\[
560=I=4m-\dfrac{8+m+g}{2}+1\iff 7m-g=1126 .
\]
Here $g\in\{1,2,4,8\}$, so $7m\in\{1127,1128,1130,1134\}$; only $1127=7\cdot161$ is divisible by $7$, giving $m=161$, and indeed $\gcd(8,161)=1=g$. Hence $n=\boxed{162}$.''',
'Lattice points|Pick\'s theorem|Coordinate geometry|Right triangles',4,
source=src('MATHCOUNTS',2012,'National',6,rnd='Target'),
note='The post says n > 0; n > 1 is needed for a triangle. Answer matches the official 162; checked by counting interior points directly.')

# ---------------- 1761611 echo
b.add(1761611,1,r'''You stand $100$ meters from a concrete wall, and your friend Billy stands $200$ meters farther from the wall, on the same side and on the same line perpendicular to the wall. You give a loud yell. Billy hears both the original sound and its echo from the wall. Taking the speed of sound to be $300$ meters per second, how many seconds pass between Billy hearing the original yell and hearing the echo? Give your answer as a decimal rounded to the nearest hundredth.''',
r'''The direct sound travels $200$ m from you to Billy. The echo travels $100$ m from you to the wall and then $300$ m from the wall back to Billy, $400$ m in all. The extra distance is $200$ m, so the time difference is $\dfrac{200}{300}=\dfrac23\approx\boxed{0.67}$ seconds.''',
'Distance, rate, and time',2,
note='Science Bowl question; that you, Billy and the wall are on one line perpendicular to the wall is made explicit.')

# ---------------- 1760257 AIME marathon
b.add(1760257,1,r'''What is the product of the real roots of the equation $x^2+18x+30=2\sqrt{x^2+18x+45}$?''',
r'''Let $y=\sqrt{x^2+18x+45}\ge0$. The equation becomes $y^2-15=2y$, i.e.\ $(y-5)(y+3)=0$, so $y=5$. Then $x^2+18x+45=25$, i.e.\ $x^2+18x+20=0$, whose discriminant $324-80>0$ gives two real roots, both satisfying the original equation. Their product is $\boxed{20}$.''',
'Quadratic equations|Radical equations|Substitution|Vieta\'s formulas',3,
source=src('AIME',1983,None,3))
b.add(1760257,2,r'''Let $x$, $y$ and $z$ all exceed $1$, and let $w$ be a positive number such that $\log_xw=24$, $\log_yw=40$ and $\log_{xyz}w=12$. Find $\log_zw$.''',
r'''Take reciprocals: $\log_wx=\dfrac1{24}$, $\log_wy=\dfrac1{40}$ and $\log_w(xyz)=\dfrac1{12}$. Since $\log_w(xyz)=\log_wx+\log_wy+\log_wz$,
\[
\log_wz=\dfrac1{12}-\dfrac1{24}-\dfrac1{40}=\dfrac{10-5-3}{120}=\dfrac1{60},
\]
so $\log_zw=\boxed{60}$.''',
'Logarithms',3,source=src('AIME',1983,None,1))
b.add(1760257,3,r'''Find $3x^2y^2$ if $x$ and $y$ are integers such that $y^2+3x^2y^2=30x^2+517$.''',
r'''Rearrange: $3x^2y^2+y^2-30x^2-10=507$, which factors as
\[
(3x^2+1)(y^2-10)=507=3\cdot13^2 .
\]
So $3x^2+1$ is a positive divisor of $507$: one of $1,3,13,39,169,507$. It is $\equiv1\pmod3$, leaving $1,13,169$. $3x^2+1=1$ gives $x=0$ and $y^2=517$, not a square; $3x^2+1=169$ gives $x^2=56$, not a square; $3x^2+1=13$ gives $x^2=4$ and then $y^2-10=39$, $y^2=49$. Hence $3x^2y^2=3\cdot4\cdot49=\boxed{588}$.''',
'Diophantine equations|Factoring|Divisibility',4,source=src('AIME',1987,None,5))

# ---------------- 1761574 New Year's Problems II
b.add(1761574,1,r'''Find the least positive integer $n\ge3$ such that $\displaystyle\sum_{i=3}^{n}\dbinom{i}{3}\ge2019$.''',
r'''By the hockey-stick identity, $\displaystyle\sum_{i=3}^{n}\dbinom i3=\dbinom{n+1}{4}$. We have $\dbinom{16}{4}=1820<2019$ and $\dbinom{17}{4}=2380\ge2019$, so $n+1=17$ and $n=\boxed{16}$.''',
'Combinatorial identities and binomial coefficients|Pascal\'s triangle|Summation',3,
note='The post writes the summand as C(n,3), which does not depend on i; corrected to C(i,3), the evident intent. (With the literal C(n,3), the sum is (n-2)C(n,3) and the answer would be 12.)')
b.add(1761574,2,r'''Compute the number of ways to order the seven integers $2017, 2017, 2018, 2018, 2018, 2019, 2019$ in a row so that every two adjacent integers are relatively prime. Integers with the same value are indistinguishable.''',
r'''Distinct values among these are relatively prime: consecutive integers always are, and $\gcd(2017,2019)$ divides $2$ while both are odd. Equal values are not. So we count the arrangements of $a,a,b,b,b,c,c$ (with $a=2017$, $b=2018$, $c=2019$) with no two equal letters adjacent.

First arrange $a,a,c,c$ in a row ($6$ ways), then put the three $b$'s into the $5$ gaps (ends included), at most one per gap so that no two $b$'s touch; every gap between two equal letters must receive a $b$.
\begin{itemize}
\item $acac$, $caca$: no forced gap; $\dbinom53=10$ ways each.
\item $acca$, $caac$: the middle gap is forced; $\dbinom42=6$ ways each.
\item $aacc$, $ccaa$: two forced gaps; $\dbinom31=3$ ways each.
\end{itemize}
Total: $20+12+6=\boxed{38}$.''',
'Arrangements with restrictions|Multiset permutations|Casework|HCF and LCM',4)
b.add(1761574,3,r'''Four children (Jessica, John, and the twins Sam and Joseph) and three adults (Mr.\ Smith, Mrs.\ Smith and Grandmother Annie) sit around a round table with ten equally spaced chairs, one person per chair. Jessica must sit at least three chairs away from John: for example J1, empty, empty, J2 is acceptable, but J1, empty, J2 is not. The twins must sit in adjacent chairs. Going clockwise around the table, the three adults must appear in the order Mr.\ Smith, Mrs.\ Smith, Grandmother Annie (not necessarily next to each other). Arrangements that are rotations of each other are considered the same. How many seating arrangements are there?''',
r'''First count arrangements on ten labelled chairs, then divide by $10$: since all people are distinct, no rotation other than the identity fixes an arrangement, so each class of rotations has exactly $10$ members.

\textbf{Twins:} $10$ pairs of adjacent chairs and $2$ orders: $20$ ways. By symmetry, say they occupy chairs $0$ and $1$.

\textbf{Jessica and John} use two of the chairs $2,3,\dots,9$, which form a row (chairs $9$ and $2$ are separated by the twins' chairs). Pairs at distance $1$: $(2,3),\dots,(8,9)$, $7$ pairs; at distance $2$: $(2,4),\dots,(7,9)$, $6$ pairs (chairs $9$ and $1$, or $0$ and $2$, would involve a twin). So $\dbinom82-13=15$ unordered pairs are allowed, and $30$ ordered placements.

\textbf{Adults:} choose $3$ of the remaining $6$ chairs, $\dbinom63=20$ ways; of the $6$ ways to seat the adults in them, exactly $3$ give the clockwise order Mr.\ Smith, Mrs.\ Smith, Annie (one cyclic order out of two). So $60$ ways.

With labelled chairs: $20\cdot30\cdot60=36000$. Up to rotation: $\dfrac{36000}{10}=\boxed{3600}$.''',
'Circular arrangements|Arrangements with restrictions|Multiplication principle|Symmetry',5,
note='"Sit together" read as adjacent chairs and "at least three chairs away" as the example says (circular distance at least 3); the adults\' clockwise order is a cyclic order, not adjacency. Verified by brute force over all seatings.')
b.add(1761574,4,r'''Let $N$ be the number of ways to rearrange the twelve digits of $201820182019$ to form a twelve-digit positive integer (no leading zero) in which no two odd digits are adjacent. Digits of the same value are indistinguishable. Find $\dfrac N2$.''',
r'''The digits are $0,0,0,2,2,2,8,8$ (eight even digits) and $1,1,1,9$ (four odd digits).

\textbf{Ignoring the leading-zero rule.} Arrange the even digits: $\dfrac{8!}{3!\,3!\,2!}=560$ ways. The odd digits go into $4$ of the $9$ gaps around them, at most one per gap: $\dbinom94=126$ ways, and they can be ordered in $\dfrac{4!}{3!}=4$ ways. Total $560\cdot126\cdot4=282240$.

\textbf{Leading zero.} The number starts with $0$ exactly when the first even digit is $0$ and no odd digit is placed before it. Arrange the remaining even digits $0,0,2,2,2,8,8$: $\dfrac{7!}{2!\,3!\,2!}=210$ ways; choose $4$ of the other $8$ gaps: $\dbinom84=70$; order the odd digits: $4$. That is $58800$.

So $N=282240-58800=223440$ and $\dfrac N2=\boxed{111720}$.''',
'Arrangements with restrictions|Multiset permutations|Complementary counting|Digit problems',4,
note='Verified by brute force over all distinct rearrangements.')
b.add(1761574,5,r'''Let $N$ be the number of ways to distribute $25$ indistinguishable gifts to $5$ distinguishable children so that each child receives an odd number of gifts. Find $9N-8$.''',
r'''Write the $i$-th child's number of gifts as $2y_i+1$ with $y_i\ge0$. Then $\sum(2y_i+1)=25$ gives $y_1+\cdots+y_5=10$, which by stars and bars has $\dbinom{14}{4}=1001$ solutions. So $N=1001$ and $9N-8=\boxed{9001}$.''',
'Stars and bars|Distributions and integer solutions|Parity',3)

# ---------------- 1754925 factoring and expanding
b.add(1754925,1,r'''\begin{enumerate}
\item[(a)] Show that the polynomial $x^3+35x^2-50x+24$ has no rational roots, and deduce that it cannot be factored into polynomials of lower degree with integer coefficients.
\item[(b)] Expand $(x+2)(x-3)(x+5)(x+6)$.
\end{enumerate}''',
r'''(a) Let $f(x)=x^3+35x^2-50x+24$. By the rational root theorem a rational root must be an integer dividing $24$: $\pm1,\pm2,\pm3,\pm4,\pm6,\pm8,\pm12,\pm24$.

For $x>0$: $35x^2-50x+24=35\left(x-\dfrac57\right)^2+\dfrac{43}{7}>0$ and $x^3>0$, so $f(x)>0$.

For $-35<x<0$: $x^2(x+35)>0$ and $-50x+24>0$, so $f(x)=x^2(x+35)-50x+24>0$. All the negative candidates $-1,-2,-3,-4,-6,-8,-12,-24$ lie in this range. (For instance $f(-1)=108$ and $f(-24)=7560$.)

So $f$ has no rational root. A factorization of a cubic over the integers into lower-degree factors would include a linear factor $px+q$ and hence the rational root $-\dfrac qp$; therefore $f$ cannot be factored over the integers. (Its real root, near $x\approx-36.4$, is irrational.)

(b) Multiply in pairs: $(x+2)(x+5)=x^2+7x+10$ and $(x-3)(x+6)=x^2+3x-18$. Then
\[
(x^2+7x+10)(x^2+3x-18)=x^4+3x^3-18x^2+7x^3+21x^2-126x+10x^2+30x-180,
\]
so the product is $\boxed{x^4+10x^3+13x^2-96x-180}$.''',
'Polynomials|Polynomial roots|Factoring|Algebraic expressions and identities',3,
note='The post asks in general how to factor cubics, giving x^3 + 35x^2 - 50x + 24 as an example, and how to expand (x+2)(x-3)(x+5)(x+6) fast. The example cubic has no rational roots, so the record asks to show it does not factor over the integers, and to expand the product.')

# ---------------- 1761505 2019 problems
b.add(1761505,1,r'''What is the last digit of $2019^{2019}$?''',
r'''The last digit of $2019^k$ is that of $9^k$, which is $9$ for odd $k$ and $1$ for even $k$ (since $9^2=81$). As $2019$ is odd, the last digit is $\boxed{9}$.''',
'Units digits and last digits|Exponents',1)
b.add(1761505,2,r'''What is the sum of the first $2019$ positive integers?''',
r'''$1+2+\cdots+2019=\dfrac{2019\cdot2020}{2}=2019\cdot1010=\boxed{2039190}$.''',
'Arithmetic sequences|Summation',1)
b.add(1761505,3,r'''There are $2019$ people in a club, and every two of them shake hands exactly once. How many handshakes are there in total?''',
r'''Each handshake corresponds to a pair of people, so there are $\dbinom{2019}{2}=\dfrac{2019\cdot2018}{2}=2019\cdot1009=\boxed{2037171}$ handshakes.''',
'Combinations',1,
note='"Each person shakes hands with another person exactly once" read as every pair shaking hands once.')

# ---------------- 1761528 angle bisectors concurrent
fig=r'''pair A=(0.9,3.2),B=(0,0),C=(5,0);
real a=abs(B-C),bb=abs(A-C),c=abs(A-B);
pair I=(a*A+bb*B+c*C)/(a+bb+c);
pair F1=A+dot(I-A,unit(B-A))*unit(B-A), F2=B+dot(I-B,unit(C-B))*unit(C-B), F3=A+dot(I-A,unit(C-A))*unit(C-A);
pair XA=extension(A,I,B,C), XB=extension(B,I,A,C);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--XA,blue);draw(B--XB,blue);draw(C--extension(C,I,A,B),blue);
draw(I--F1,dashed);draw(I--F2,dashed);draw(I--F3,dashed);
dot(I);dot(F1);dot(F2);dot(F3);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);
label("$I$",I,2*dir(80));
label("$D$",F1,W);label("$E$",F2,S);label("$F$",F3,NE);'''
b.add(1761528,1,r'''Prove that the three angle bisectors of a triangle $ABC$ are concurrent.''',
r'''\textbf{Key fact.} A point inside an angle lies on its bisector if and only if it is equidistant from the two sides of the angle. Indeed, if $P$ is inside $\angle XOY$ with feet of perpendiculars $P_1$ on $OX$ and $P_2$ on $OY$, the right triangles $OPP_1$ and $OPP_2$ share the hypotenuse $OP$; they are congruent (AAS) when $\angle POP_1=\angle POP_2$, giving $PP_1=PP_2$, and congruent (HL) when $PP_1=PP_2$, giving equal angles.

\textbf{Proof.} The bisectors of the angles at $A$ and $B$ run into the interior of the triangle and meet at a point $I$ inside it (the bisector from $A$ meets side $BC$, and the bisector from $B$ crosses the segment from $A$ to that point). Let $D$, $E$, $F$ be the feet of the perpendiculars from $I$ to $AB$, $BC$, $CA$.
'''+asy(fig,'6cm')+r'''
Since $I$ is on the bisector of $\angle A$, $ID=IF$; since $I$ is on the bisector of $\angle B$, $ID=IE$. Hence $IE=IF$: the point $I$, which is inside $\angle C$, is equidistant from its sides $CB$ and $CA$, so it lies on the bisector of $\angle C$. Therefore all three angle bisectors pass through $I$. $\blacksquare$

(The common point $I$ is the incentre: the circle with centre $I$ and radius $ID=IE=IF$ touches all three sides.)''',
'Angle bisectors|Triangles|Congruence|Incircles and incentres',3)

# ---------------- 1761521 (n+1)(n^2+1) | 10^n
b.add(1761521,1,r'''Find all positive integers $n$ such that $n^3+n^2+n+1$ divides $10^n$.''',
r'''Factor: $n^3+n^2+n+1=(n+1)(n^2+1)$. Both factors divide $10^n$, so each is of the form $2^i5^j$. Note $n^2+1$ is never divisible by $4$.

\textbf{If $5\mid n+1$,} then $n\equiv-1\pmod5$ and $n^2+1\equiv2\pmod5$, so $n^2+1$ is a power of $2$ not divisible by $4$: $n^2+1\le2$, $n=1$, but $5\nmid2$. So $n+1$ is a power of $2$.

\textbf{$n$ even} would make $n+1$ an odd power of $2$, i.e.\ $n+1=1$; impossible. So $n$ is odd, $n+1=2^a$ with $a\ge1$, and $n^2+1\equiv2\pmod4$ gives $n^2+1=2\cdot5^d$. With $n=2^a-1$:
\[
2^{2a}-2^{a+1}+2=2\cdot5^d\iff 2^{2a-1}-2^a+1=5^d .
\]
\begin{itemize}
\item $a=1$: $n=1$, and $4\nmid10$. No.
\item $a=2$: $n=3$, $5^d=5$; indeed $4\cdot10=40\mid1000$. Yes.
\item $a\ge3$: the left side is $\equiv1\pmod8$, so $5^d\equiv1\pmod8$ and $d=2e$ is even, $e\ge1$. Then $25^e-1=2^a\left(2^{a-1}-1\right)$, so $2^a$ is the exact power of $2$ in $25^e-1$. Writing $e=2^sk$ with $k$ odd, $25^e-1=(25^{k}-1)(25^k+1)(25^{2k}+1)\cdots(25^{2^{s-1}k}+1)$, where $25^k-1=24(25^{k-1}+\cdots+1)$ contains exactly $2^3$ (the sum has $k$ odd terms) and each other factor is $\equiv2\pmod4$. Hence $a=3+s$ and $2^a=8\cdot2^s\le8e$. Then $25^e-1<2^{2a}\le64e^2$, which holds for $e=1$ ($24<64$) but fails for $e\ge2$ ($25^e$ grows much faster: $624>256$, and so on). So $e=1$, $d=2$, $a=3$, $n=7$: $2^5-2^3+1=25$ and $8\cdot50=400\mid10^7$. Yes.
\end{itemize}
The answers are $\boxed{n=3\text{ and }n=7}$.''',
'Divisibility|Prime factorisation|Factoring|Powers of two|Bounding and extremal cases',6,
note='Checked by computer for n < 3000 (only 3 and 7).')

b.save()
