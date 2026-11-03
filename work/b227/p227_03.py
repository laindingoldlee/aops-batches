from qb import *
b=Bank('p227_03')

# ---------------- 1754152 two primes same tens digit
b.add(1754152,1,r'''Let $S=\overline{ab}+\overline{ac}$, where $\overline{ab}$ and $\overline{ac}$ are distinct two-digit prime numbers (with the same tens digit $a$) such that $10\mid\overline{ab}^{\,2}+\overline{ac}^{\,2}$. Determine the minimum and the maximum value of $S$.''',
r'''A two-digit prime ends in $1,3,7$ or $9$, and the squares of these digits end in $1,9,9,1$. The sum of the squares ends in $0$ only if one of them ends in $1$ and the other in $9$, that is, one of $b,c$ is in $\{1,9\}$ and the other in $\{3,7\}$. Also $\overline{ab}+\overline{ac}=20a+b+c$.

\textbf{Minimum.} With $a=1$ the primes are $11,13,17,19$, and $11+13=24$ is admissible ($121+169=290$). Any admissible pair with $a=1$ has $b+c\ge1+3$, so $S\ge24$; with $a\ge2$, $S\ge40$. The minimum is $\boxed{24}$.

\textbf{Maximum.} With $a=9$ the only two-digit prime is $97$, so no pair exists. With $a=8$ the primes are $83,89$, and $83^2+89^2=6889+7921=14810$ is divisible by $10$. So the maximum is $83+89=\boxed{172}$ (any pair with $a\le7$ has $S\le2\cdot79<172$).''',
'Prime numbers|Units digits and last digits|Digits and bases|Casework',3,
note='The notation means two two-digit numbers with the same tens digit a. Checked by listing all admissible pairs.')

# ---------------- 1754045 24 | a(a^2+23)
b.add(1754045,1,r'''Prove that if $a$ is an integer not divisible by $2$ or $3$, then $24\mid a\left(a^2+23\right)$.''',
r'''Since $a^2+23=(a^2-1)+24$, it suffices to show $24\mid a^2-1=(a-1)(a+1)$.

$a$ is odd, so $a-1$ and $a+1$ are consecutive even numbers; one of them is divisible by $4$, so $8\mid(a-1)(a+1)$. Among the three consecutive integers $a-1,a,a+1$ one is divisible by $3$, and it is not $a$; so $3\mid(a-1)(a+1)$. As $\gcd(3,8)=1$, $24\mid a^2-1$, hence $24\mid a^2+23$ and $24\mid a(a^2+23)$. $\blacksquare$''',
'Divisibility|Remainders and congruences|Difference of squares|Parity',3)

# ---------------- 1753689 x^4+16=10x^2
b.add(1753689,1,r'''If $p$ and $q$ are distinct roots of the equation $x^4+16=10x^2$ and $pq>0$, what is the value of the product $pq$?''',
r'''Write $x^4-10x^2+16=0$ as $(x^2-2)(x^2-8)=0$, so the roots are $\pm\sqrt2$ and $\pm2\sqrt2$. Two distinct roots with positive product have the same sign and different absolute values (a root and itself is excluded): $\left\{\sqrt2,2\sqrt2\right\}$ or $\left\{-\sqrt2,-2\sqrt2\right\}$. In both cases $pq=\sqrt2\cdot2\sqrt2=\boxed{4}$.''',
'Polynomial roots|Quadratic equations|Factoring|Substitution',2)

# ---------------- 1753987 cone cut into equal volumes
h=10/2**(1/3)
fig=r'''real H=10,R=5,h=%.5f; real yc=H-h, rc=R*h/H;
pair V=(0,H);
draw(shift(0,0)*xscale(R)*yscale(R*0.25)*arc((0,0),1,180,360),linewidth(0.9));
draw(shift(0,0)*xscale(R)*yscale(R*0.25)*arc((0,0),1,0,180),dashed);
draw(shift(0,yc)*xscale(rc)*yscale(rc*0.25)*unitcircle,blue+linewidth(0.8));
draw((-R,0)--V--(R,0),linewidth(0.9));
draw(V--(0,0),dashed);
dot(V);
label("$V$",V,N);
draw((R+1.2,0)--(R+1.2,H),Arrows(5));label("$10$",(R+1.2,H/2),E);
draw((-R-1.2,yc)--(-R-1.2,H),blue,Arrows(5));label("$h$",(-R-1.2,(yc+H)/2),W,blue);
draw((0,0)--(R,0),dashed);
draw((0,-1.9)--(R,-1.9),Arrows(5));label("$5$",(R/2,-1.9),S);
draw((0,-0.1)--(0,-2.1),dotted);draw((R,-0.1)--(R,-2.1),dotted);
draw((-R-1.4,yc)--(-rc,yc),dotted);draw((-R-1.4,H)--(-0.3,H),dotted);'''%h
b.add(1753987,1,r'''A cone has base radius $5$ and height $10$. A plane parallel to the base cuts the cone into two pieces of equal volume. What is the height of the piece that is a cone?''',
r'''The small piece is a cone similar to the whole cone, with the same apex $V$; let its height be $h$.
'''+asy(fig,'5cm')+r'''
The ratio of similarity is $\dfrac h{10}$, so the volume ratio is $\left(\dfrac h{10}\right)^3$. Equal pieces mean the small cone has half the volume:
\[
\left(\dfrac h{10}\right)^3=\dfrac12\quad\Longrightarrow\quad h=\dfrac{10}{\sqrt[3]2}=\boxed{5\sqrt[3]4}\approx7.94 .
\]
(The radius $5$ is not needed.)''',
'Cones|Volume|Scaling of length, area, and volume|Similarity|Solid geometry',3,
note='Checked: (5*4^(1/3)/10)^3 = 1/2.')

# ---------------- 1751624 equilateral with D
fig=r'''real s=6;
pair A=(0,0),B=(s,0),C=s*dir(60);
real t=s*Sin(20)/Sin(150); pair D=t*dir(10);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--D--B,linewidth(0.8));draw(C--D,red+linewidth(0.8));
dot(D);
draw(arc(A,1.6,0,10),linewidth(0.6));label("$10^\circ$",A+2.35*dir(5),fontsize(8pt));
draw(arc(B,1.3,160,180),linewidth(0.6));label("$20^\circ$",B+2.05*dir(170),fontsize(8pt));
real ca=degrees(A-C),cd=degrees(D-C);
draw(arc(C,1.3,ca,cd),red+linewidth(0.6));label("$x$",C+1.75*dir((ca+cd)/2),red);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,N);label("$D$",D,dir(45));'''
b.add(1751624,1,r'''Let $\triangle ABC$ be an equilateral triangle. Point $D$ is inside $\triangle ABC$ such that $\angle DBA=20^\circ$ and $\angle DAB=10^\circ$. Find $\angle ACD$.''',
r'''Let the side be $1$ and $x=\angle ACD$.
'''+asy(fig,'6cm')+r'''
In triangle $ABD$, $\angle ADB=150^\circ$, so by the law of sines $AD=\dfrac{\sin20^\circ}{\sin150^\circ}=2\sin20^\circ$. In triangle $ACD$, $\angle CAD=60^\circ-10^\circ=50^\circ$ and $\angle ADC=180^\circ-50^\circ-x=130^\circ-x$, so the law of sines gives
\[
\dfrac{AD}{\sin x}=\dfrac{AC}{\sin(130^\circ-x)}\quad\Longrightarrow\quad 2\sin20^\circ\sin(130^\circ-x)=\sin x .
\]
Expand $\sin(130^\circ-x)=\sin50^\circ\cos x+\cos50^\circ\sin x$ and divide by $\cos x$:
\[
\tan x=\dfrac{2\sin20^\circ\sin50^\circ}{1-2\sin20^\circ\cos50^\circ}.
\]
By the product-to-sum formulas, $2\sin20^\circ\sin50^\circ=\cos30^\circ-\cos70^\circ=\dfrac{\sqrt3}{2}-\sin20^\circ$ and $2\sin20^\circ\cos50^\circ=\sin70^\circ-\sin30^\circ=\cos20^\circ-\dfrac12$. Hence
\[
\tan\angle ACD=\dfrac{\sqrt3-2\sin20^\circ}{3-2\cos20^\circ},\qquad \angle ACD=\boxed{\arctan\dfrac{\sqrt3-2\sin20^\circ}{3-2\cos20^\circ}\approx43.08^\circ}.
\]
(Since $0<x<60^\circ$ and the tangent is increasing there, this determines $x$.) The angle is not a whole number of degrees: $\tan43^\circ\approx0.9325$ and $\tan44^\circ\approx0.9657$, while the value above is about $0.9352$; this is why a pure angle chase does not succeed.''',
'Equilateral triangles|Law of sines|Trigonometric identities|Trigonometry|Triangles',5,
note='Self-made problem whose poster could not solve it; the answer is not a whole number of degrees (about 43.08), so it is given in closed form. Checked with coordinates and with trigonometric Ceva.')

# ---------------- 1753684 incircle angle; seating
aa=34
fig=r'''real b=(180-%d)/2;
pair B=(-2,0),C=(2,0),A=(0,2*Tan(b));
real r=2*Tan(b/2); pair P=(0,r);
draw(circle(P,r),blue+linewidth(0.7));
draw(A--B--C--cycle,linewidth(0.9));
draw(P--A,dashed);draw(P--C,dashed);
dot(P);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$P$",P,W);
draw(arc(A,2.4,degrees(B-A),degrees(C-A)),linewidth(0.6));label("$34^\circ$",A+2.95*dir(-98.5),fontsize(8pt));
'''%aa
b.add(1753684,1,r'''A circle with centre $P$ is inscribed in isosceles triangle $ABC$ with apex angle $A$ measuring $34^\circ$. What is the degree measure of angle $APC$? Express your answer as a decimal to the nearest tenth.''',
r'''The base angles are $\angle B=\angle C=\dfrac{180^\circ-34^\circ}{2}=73^\circ$. The centre $P$ of the inscribed circle is the incentre, where the angle bisectors meet, so $\angle PAC=17^\circ$ and $\angle PCA=36.5^\circ$.
'''+asy(fig,'6cm')+r'''
In triangle $APC$,
\[
\angle APC=180^\circ-17^\circ-36.5^\circ=\boxed{126.5^\circ}
\]
(in general $\angle APC=90^\circ+\dfrac12\angle B$).''',
'Incircles and incentres|Isosceles triangles|Angle bisectors|Angle sums',2,source=src('MATHCOUNTS Handbook',None,None,None))
b.add(1753684,2,r'''Mr.\ and Mrs.\ Shell have three children. In how many different ways can the five people be seated in a row of five chairs if Mr.\ and Mrs.\ Shell must sit next to each other?''',
r'''Glue the parents into one block. The block and the three children are $4$ units, which can be arranged in $4!=24$ ways, and the parents can be ordered within the block in $2$ ways. The answer is $24\cdot2=\boxed{48}$.''',
'Arrangements with restrictions|Permutations',2,
note='Seating is taken to be in a row of five chairs.')

# ---------------- 1753584 circular segment
fig=r'''pair O=(0,0),A=6*dir(30),B=6*dir(150);
fill(arc(O,6,30,150)--cycle,paleblue);
draw(circle(O,6),linewidth(0.8));
draw(O--A,linewidth(0.8));draw(O--B,linewidth(0.8));draw(A--B,linewidth(0.8));
draw(arc(O,1,30,150),linewidth(0.6));label("$120^\circ$",O+1.75*dir(118),fontsize(8pt));
pair M=(A+B)/2;draw(O--M,dashed);
draw(M--M+(0.4,0)--M+(0.4,-0.4)--M+(0,-0.4));
dot(O);label("$O$",O,S);label("$A$",A,E);label("$B$",B,W);label("$M$",M,dir(60),fontsize(8pt));
label("$6$",(O+A)/2,SE);'''
b.add(1753584,1,r'''A circle has radius $6$ cm. Two radii $OA$ and $OB$ form a central angle of $120^\circ$, so the minor arc $AB$ measures $120^\circ$. The sector $AOB$ is cut by the chord $AB$ into the triangle $AOB$ and the region between the chord and the minor arc, which is shaded. Find the area of the shaded region.''',
r'''Let $M$ be the midpoint of $AB$.
'''+asy(fig,'5cm')+r'''
The sector has area $\dfrac{120}{360}\cdot\pi\cdot6^2=12\pi$. In the isosceles triangle $AOB$, the altitude $OM$ bisects the $120^\circ$ angle, so triangle $OMA$ is a $30^\circ$--$60^\circ$--$90^\circ$ triangle with $OM=3$ and $AM=3\sqrt3$. So $AB=6\sqrt3$ and the triangle has area $\dfrac12\cdot6\sqrt3\cdot3=9\sqrt3$. (Equivalently, $\dfrac12\cdot6\cdot6\sin120^\circ=9\sqrt3$.) The shaded region has area
\[
\boxed{12\pi-9\sqrt3}\approx22.11\text{ cm}^2 .
\]''',
'Arcs and chords|Circles|Lengths, perimeter, and area|Special right triangles|Area decomposition',3,
note='The figure is missing; from the description ("a shaded sector and a triangle inscribed in that sector") the shaded region is read as the sector minus the triangle formed by the two radii and the chord, i.e. the circular segment.')

# ---------------- 1753554 nickels and quarters
b.add(1753554,1,r'''Mariana has only nickels and quarters in her piggy bank. Their combined value is $\$9.15$ and their combined weight is $1$ pound. Ninety nickels weigh one pound and eighty quarters weigh one pound. How many nickels does Mariana have in her piggy bank?''',
r'''Let there be $n$ nickels and $q$ quarters. Then
\[
5n+25q=915,\qquad \dfrac n{90}+\dfrac q{80}=1 .
\]
The first equation gives $n=183-5q$; the second gives $8n+9q=720$. Substituting, $1464-40q+9q=720$, so $31q=744$, $q=24$ and $n=183-120=63$. Check: $63\cdot5+24\cdot25=315+600=915$ cents and $\dfrac{63}{90}+\dfrac{24}{80}=0.7+0.3=1$. Mariana has $\boxed{63}$ nickels.''',
'Systems of linear equations|Money and currency',2)

# ---------------- 1753532 triangles in hexagon
fig=r'''pair[] P; for(int i=0;i<6;++i) P[i]=dir(60*i);
picture hexp(int k){picture pic; pair[] Q;
 for(int i=0;i<6;++i) Q[i]=P[i];
 filldraw(pic,(k==0?Q[0]--Q[2]--Q[4]--cycle:(k==1?Q[0]--Q[1]--Q[2]--cycle:Q[0]--Q[1]--Q[3]--cycle)),paleblue,blue+linewidth(0.8));
 draw(pic,Q[0]--Q[1]--Q[2]--Q[3]--Q[4]--Q[5]--cycle,linewidth(0.8));
 for(int i=0;i<6;++i) dot(pic,Q[i]);
 return pic;}
add(shift(0,0)*hexp(0));add(shift(2.6,0)*hexp(1));add(shift(5.2,0)*hexp(2));
label("equilateral",(0,-1.3));label("isosceles $120^\circ$",(2.6,-1.3));label("$30^\circ$-$60^\circ$-$90^\circ$",(5.2,-1.3));'''
b.add(1753532,1,r'''Triangles are formed by joining three of the six vertices of a regular hexagon.
\begin{enumerate}
\item[(a)] How many different triangles can be formed?
\item[(b)] How many of them are pairwise non-congruent, that is, how many different shapes occur?
\end{enumerate}''',
r'''\textbf{(a)} No three vertices of a regular hexagon are collinear, and a triangle is determined by its three vertices, so there are $\dbinom63=\boxed{20}$ triangles.

\textbf{(b)} Classify the $20$ triangles by the arcs between their vertices around the hexagon (the three gaps, measured in hexagon steps, add up to $6$): the gap patterns are $\{2,2,2\}$, $\{1,1,4\}$ and $\{1,2,3\}$.
'''+asy(fig,'9cm')+r'''
\begin{itemize}
\item $\{2,2,2\}$: alternate vertices, an equilateral triangle with side $\sqrt3$ (for unit side): $2$ triangles.
\item $\{1,1,4\}$: three consecutive vertices, an isosceles triangle with sides $1,1,\sqrt3$ and a $120^\circ$ angle: $6$ triangles.
\item $\{1,2,3\}$: two opposite vertices and one more, a $30^\circ$--$60^\circ$--$90^\circ$ triangle with sides $1,\sqrt3,2$: $12$ triangles.
\end{itemize}
Check: $2+6+12=20$. Triangles in the same class are congruent (a rotation or reflection of the hexagon maps one to another), and the three classes have different side lengths. So there are $\boxed{3}$ non-congruent triangles (not $4$).''',
'Regular polygons|Combinations|Congruence|Casework|Special right triangles',3,
note='The post asks whether "different" means 20 or "non-congruent" (suggesting 4); the record asks both, and the non-congruent count is 3, not 4.')

# ---------------- 1750843 four problems
b.add(1750843,1,r'''Let $f(x)=x^n+2x^{n-1}+3x^{n-2}+\cdots+nx+(n+1)$. For how many of the first $100$ positive integers $n$ does the equation $f(x)=0$ have a real solution?''',
r'''\textbf{A closed form.} Let $F(x)=(x-1)^2f(x)$. Since $f(x)=\sum_{k=0}^{n}(k+1)x^{n-k}$, multiplying by $x-1$ gives $(x-1)f(x)=x^{n+1}+x^n+\cdots+x-(n+1)$ (the coefficients $k+1$ and $k$ telescope), and multiplying once more by $x-1$ gives
\[
F(x)=x^{n+2}-(n+2)x+(n+1).
\]

\textbf{$n$ odd.} Then $f$ has odd degree, so $f(x)\to-\infty$ as $x\to-\infty$ and $f(x)\to+\infty$ as $x\to+\infty$, and it has a real root by the intermediate value theorem.

\textbf{$n$ even.} Then $F'(x)=(n+2)\left(x^{n+1}-1\right)$ with $n+1$ odd, so $F'<0$ for $x<1$ and $F'>0$ for $x>1$. Hence $F$ has its minimum at $x=1$, where $F(1)=0$, and $F(x)>0$ for $x\ne1$. Therefore $f(x)=\dfrac{F(x)}{(x-1)^2}>0$ for $x\ne1$, and $f(1)=1+2+\cdots+(n+1)>0$. So $f$ has no real root.

Exactly the odd $n$ work, and there are $\boxed{50}$ of them among $1,\dots,100$.''',
'Polynomials|Polynomial roots|Telescoping sums|Calculus|Parity',5,
note='The identity (x-1)^2 f(x) = x^(n+2) - (n+2)x + (n+1) was checked symbolically for n <= 30.')
b.add(1750843,2,r'''A quartic function $f(x)=ax^4+bx^3+cx^2+dx+e$ has its minimum value at the point $(1,2)$. If $e-a=6$, what is the value of $b-d$?''',
r'''Since the minimum is at $x=1$ with value $2$, we have $f(1)=2$ and $f'(1)=0$:
\[
a+b+c+d+e=2,\qquad 4a+3b+2c+d=0 .
\]
With $e=a+6$ the first equation becomes $2a+b+c+d=-4$, i.e.\ $4a+2b+2c+2d=-8$. Subtracting this from the second equation gives
\[
b-d=0-(-8)=\boxed{8}.
\]
Such quartics exist: for example $f(x)=(x-1)^2\left(x^2+5\right)+2=x^4-2x^3+6x^2-10x+7$ has minimum $2$ at $x=1$, $e-a=7-1=6$ and $b-d=-2+10=8$.''',
'Polynomials|Calculus|Maxima and minima|Systems of linear equations',4)
b.add(1750843,3,r'''Find all asymptotes of the graph of $y=\dfrac{(x-1)(x-2)(x-3)}{x}$.''',
r'''Expanding and dividing,
\[
\dfrac{(x-1)(x-2)(x-3)}{x}=\dfrac{x^3-6x^2+11x-6}{x}=x^2-6x+11-\dfrac6x .
\]
\begin{itemize}
\item As $x\to0$ the numerator tends to $-6\ne0$, so $\boxed{x=0}$ is a vertical asymptote ($y\to+\infty$ as $x\to0^-$ and $y\to-\infty$ as $x\to0^+$).
\item The degree of the numerator exceeds that of the denominator by $2$, so there is no horizontal or slant asymptote: $y\to+\infty$ as $x\to\pm\infty$.
\end{itemize}
So the only asymptote (straight line) is $x=0$. For large $|x|$ the graph approaches the parabola $y=x^2-6x+11$, since the difference $-\dfrac6x$ tends to $0$; this is a curved asymptote.''',
'Rational equations|Functions|Polynomials',3,
note='"Asymptotes" read as straight-line asymptotes; the parabolic asymptote is mentioned.')
b.add(1750843,4,r'''What is the value of $\dfrac11+\dfrac13+\dfrac16+\dfrac1{10}+\cdots+\dfrac1{210}$, where the denominators are the triangular numbers $1,3,6,10,\dots,210$?''',
r'''The denominators are $T_k=\dfrac{k(k+1)}2$ for $k=1,\dots,20$ ($T_{20}=210$). Since
\[
\dfrac1{T_k}=\dfrac{2}{k(k+1)}=2\left(\dfrac1k-\dfrac1{k+1}\right),
\]
the sum telescopes:
\[
\sum_{k=1}^{20}\dfrac1{T_k}=2\left(1-\dfrac1{21}\right)=\boxed{\dfrac{40}{21}} .
\]''',
'Telescoping sums|Triangular numbers|Partial fractions|Summation',3)

# ---------------- 1753098 lines through cube centres
b.add(1753098,244,r'''When $64$ unit cubes are glued together to form a $4\times4\times4$ cube, there are $76$ distinct lines that pass through the centres of exactly four unit cubes. If $1000$ unit cubes are glued together to form a $10\times10\times10$ cube, how many distinct lines pass through the centres of ten unit cubes?''',
r'''Give the unit cubes of an $n\times n\times n$ cube the coordinates $(x,y,z)$ with $x,y,z\in\{1,\dots,n\}$. A line through $n$ centres must run straight across the cube, so it contains the points $P+tv$, $t=0,\dots,n-1$, with $v$ a nonzero vector with entries in $\{-1,0,1\}$, and in each coordinate where $v$ is $\pm1$ the line goes from $1$ to $n$ (or $n$ to $1$), while the other coordinates are constant.

Now surround the cube by one more layer, forming an $(n+2)^3$ cube with coordinates $0,\dots,n+1$. Extend each line one step at both ends: it then ends in two cells of the outer layer. Conversely, a cell $(x,y,z)$ of the outer layer determines exactly one such line: in each coordinate, the value $0$ forces the step $+1$, the value $n+1$ forces $-1$, and a value in $1,\dots,n$ forces $0$; moving from the cell in that direction passes through exactly $n$ interior centres and then leaves at another outer cell. So the lines correspond to pairs of outer-layer cells, and
\[
\#\text{lines}=\dfrac{(n+2)^3-n^3}{2}.
\]
For $n=4$ this is $\dfrac{216-64}{2}=76$, as stated. For $n=10$ it is $\dfrac{1728-1000}{2}=\boxed{364}$.''',
'Bijections|Counting principles|Pattern recognition',5,source=src('MATHCOUNTS Handbook',None,None,244,rnd='Workout 8'),
note='The formula was checked by brute force for n = 1..6 (all lines through exactly n centres).')

# ---------------- 1753197 last digit of odd non-multiples of 5
b.add(1753197,1,r'''From the product $1\cdot2\cdot3\cdots2018$, all even numbers and all numbers whose units digit is $5$ are removed. What is the last digit of the product of the remaining numbers?''',
r'''The remaining numbers are those ending in $1,3,7$ or $9$. Only units digits matter. In each block of ten, $10k+1,\dots,10k+9$ for $k=0,1,\dots,200$ (that is, up to $2009$), the remaining numbers end in $1,3,7,9$, whose product $189$ ends in $9$. The leftover numbers $2011,2013,2017$ give $1\cdot3\cdot7=21$, ending in $1$. So the last digit is that of $9^{201}\cdot1$. Since $9^2=81$ ends in $1$, $9^{201}=9\cdot\left(9^2\right)^{100}$ ends in $9$. The answer is $\boxed{9}$.''',
'Units digits and last digits|Remainders and congruences|Pattern recognition',3)

# ---------------- 1753183 digits of 2^2018 5^1918
b.add(1753183,1,r'''How many digits does $C=2^{2018}\cdot5^{1918}$ have?''',
r'''$C=2^{100}\cdot\left(2^{1918}5^{1918}\right)=2^{100}\cdot10^{1918}$, so the number of digits of $C$ is $1918$ plus the number of digits of $2^{100}$. Now $2^{100}=1024^{10}$, and
\[
10^{30}<1024^{10}=10^{30}\cdot1.024^{10}<10^{30}\cdot1.03^{10}<10^{30}\cdot\left(1.03^{2}\right)^{5}<10^{30}\cdot1.07^5<10^{31},
\]
because $1.07^5<1.5$. So $2^{100}$ has $31$ digits (indeed $2^{100}=1267650600228229401496703205376$), and $C$ has $31+1918=\boxed{1949}$ digits.''',
'Exponents|Digits and bases|Estimation',3)

# ---------------- 1753196 five-digit numbers with even nonzero digit product
b.add(1753196,1,r'''How many five-digit positive integers have a product of digits that is even and nonzero?''',
r'''The product is nonzero exactly when no digit is $0$: then each of the five digits is one of $1,\dots,9$, giving $9^5=59049$ numbers. Among these the product is odd exactly when all digits are odd ($1,3,5,7,9$): $5^5=3125$ numbers. By complementary counting the answer is $59049-3125=\boxed{55924}$.''',
'Complementary counting|Multiplication principle|Parity|Digit problems',2,
note='"the product numbers a even nonzero number" is read as "the product of the digits is an even nonzero number".')

# ---------------- 1752547 BD/DA
def fig95(t,lab):
    return r'''pair A=(0,4*sqrt(3)),B=(-4,0),C=(4,0);
real t=%s;
pair D=A+t*(B-A),Ep=C+t*(A-C);
pair F=extension(B,Ep,C,D);
fill(B--C--F--cycle,paleblue);
draw(A--B--C--cycle,linewidth(0.9));
draw(B--Ep,linewidth(0.8));draw(C--D,linewidth(0.8));
dot(D);dot(Ep);dot(F);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$D$",D,W);label("$E$",Ep,E);label("$F$",F,N);
label("%s",(0,-1.5));'''%(t,lab)
b.add(1752547,1,r'''Let $ABC$ be an equilateral triangle, and let $D$ and $E$ be points on sides $AB$ and $AC$ respectively such that $AD=CE$. Let segments $BE$ and $CD$ meet at $F$. If $[ABC]=7$ and $[BCF]=2$, find all possible values of $\dfrac{BD}{DA}$.''',
r'''Take side length $1$ and let $AD=CE=t$ with $0<t<1$. Use barycentric (area) coordinates with respect to $ABC$: $D=(1-t)A+tB$ and $E=tA+(1-t)C$.

A point $X$ of line $CD$ has the form $X\propto(1-t)A+tB+\lambda C$, and a point of line $BE$ has the form $X\propto tA+\mu B+(1-t)C$. For $F$ the ratios of the coefficients agree:
\[
\dfrac{1-t}{t}=\dfrac{t}{\mu}\ \text{ and }\ \dfrac{1-t}{\lambda}=\dfrac{t}{1-t},\qquad\text{so}\qquad F\propto\bigl(t(1-t),\ t^2,\ (1-t)^2\bigr).
\]
The $A$-coordinate of $F$ is $\dfrac{[FBC]}{[ABC]}$, so
\[
\dfrac{[BCF]}{[ABC]}=\dfrac{t(1-t)}{t(1-t)+t^2+(1-t)^2}=\dfrac{t-t^2}{1-t+t^2}=\dfrac27 .
\]
This gives $7t-7t^2=2-2t+2t^2$, i.e.\ $9t^2-9t+2=0$, so $(3t-1)(3t-2)=0$ and $t=\dfrac13$ or $t=\dfrac23$. Both give points on the sides, and both configurations are shown ($[BCF]$ shaded).
'''+asy(fig95(1/3,r"$AD=\dfrac13AB$"),'4.5cm')+asy(fig95(2/3,r"$AD=\dfrac23AB$"),'4.5cm')+r'''
Since $\dfrac{BD}{DA}=\dfrac{1-t}{t}$, the possible values are $\boxed{2\text{ and }\dfrac12}$.''',
'Equilateral triangles|Area ratios|Triangles|Coordinate bashing',5,
note='The post asks for BD/DA as if unique; both t = 1/3 and t = 2/3 satisfy the conditions, so both values 2 and 1/2 are given. Checked with coordinates.')

# ---------------- 1753103 two probability problems
b.add(1753103,1,r'''A two-digit positive integer is selected at random. What is the probability that its units digit is a multiple of its tens digit? Express your answer as a common fraction.''',
r'''There are $90$ two-digit numbers. For tens digit $t$, the units digit $u\in\{0,\dots,9\}$ must be a multiple of $t$; note that $0$ is a multiple of every $t$. The counts are
\[
t=1:10,\quad t=2:5,\quad t=3:4,\quad t=4:3,\quad t=5,6,7,8,9:\ 2\text{ each},
\]
for a total of $10+5+4+3+10=32$. The probability is $\dfrac{32}{90}=\boxed{\dfrac{16}{45}}$.

(The answer $\dfrac{23}{90}$ comes from forgetting that a units digit $0$ is a multiple of the tens digit: the $9$ numbers $10,20,\dots,90$ are missing, and $23+9=32$.)''',
'Probability|Factors and multiples|Digit problems|Casework',2,
note='The poster got 23/90; the solution identifies the omitted case (units digit 0).')
b.add(1753103,2,r'''Tamyra is making $4$ cookies and has exactly $4$ chocolate chips. She puts each chip into one of the $4$ cookies, chosen at random, independently and with equal probabilities. What is the probability that no cookie gets more than $2$ chips? Express your answer as a common fraction.''',
r'''There are $4^4=256$ equally likely assignments of the chips. Count the complement, where some cookie gets at least $3$ chips (only one cookie can):
\begin{itemize}
\item exactly $3$ chips in one cookie: $4$ choices of cookie, $\dbinom43=4$ choices of chips, and $3$ cookies for the last chip: $48$;
\item all $4$ chips in one cookie: $4$.
\end{itemize}
So $52$ assignments are bad, and the probability is $\dfrac{256-52}{256}=\dfrac{204}{256}=\boxed{\dfrac{51}{64}}$.''',
'Probability|Complementary probability|Sampling with replacement|Casework',3,
note='"Distributes the chips randomly" is read as each chip independently going into a uniformly random cookie (if instead the 35 distributions of identical chips were equally likely, the answer would be 19/35). Checked by enumeration.')

# ---------------- 1753130 dynamic pressure
b.add(1753130,1,r'''The dynamic pressure $q$ generated by a fluid moving with velocity $v$ is $q=\dfrac12nv^2$, where $n$ is the constant density of the fluid. An engineer uses the formula to find the dynamic pressure of a fluid moving with velocity $v$ and of the same fluid moving with velocity $1.5v$. What is the ratio of the dynamic pressure of the faster fluid to that of the slower fluid?''',
r'''The pressure is proportional to $v^2$ (with $n$ unchanged), so the ratio is
\[
\dfrac{\dfrac12n(1.5v)^2}{\dfrac12nv^2}=1.5^2=\boxed{\dfrac94}=2.25 .
\]''',
'Ratios, proportions, and variation|Exponents',1)

# ---------------- 1752932 restricted quadratic
b.add(1752932,1,r'''The function $f$ is a quadratic function whose domain is restricted to one side of its axis of symmetry (including the vertex), so that $f$ has an inverse. The vertex of its graph is $(-2,-5)$, and $f^{-1}(-21)=-4$. Find $f(x)$, including its domain.''',
r'''With vertex $(-2,-5)$, $f(x)=a(x+2)^2-5$. The condition $f^{-1}(-21)=-4$ means $f(-4)=-21$: $4a-5=-21$, so $a=-4$. Since $-4$ is in the domain and $-4<-2$, the domain is the left half, $x\le-2$. Hence
\[
\boxed{f(x)=-4(x+2)^2-5\ \text{ for }x\le-2}.
\]
On this domain $f$ is increasing, so it is one-to-one, as needed for $f^{-1}$.''',
'Inverse functions|Quadratic equations|Functions',3)

# ---------------- 1752848 remainders
b.add(1752848,1,r'''What is the smallest positive integer that leaves a remainder of $4$ when divided by $5$, a remainder of $5$ when divided by $6$, a remainder of $6$ when divided by $7$, and a remainder of $7$ when divided by $8$?''',
r'''Each condition says $N\equiv-1$ modulo the divisor, so $N+1$ is divisible by $5,6,7$ and $8$, hence by $\operatorname{lcm}(5,6,7,8)=840$. The smallest positive $N$ is $840-1=\boxed{839}$.''',
'Remainders and congruences|HCF and LCM|Chinese remainder theorem',2)

# ---------------- 1752498 2^18+1
b.add(1752498,1,r'''Find the prime factorisation of $2^{18}+1$.''',
r'''Since $2^{18}=\left(2^6\right)^3=64^3$, the sum of cubes factorisation gives
\[
2^{18}+1=64^3+1=(64+1)\left(64^2-64+1\right)=65\cdot4033 .
\]
Here $65=5\cdot13$, and $4033=37\cdot109$ (for example from the Sophie Germain identity $1+4b^4=(1+2b+2b^2)(1-2b+2b^2)$ with $b=16$: $2^{18}+1=1+4\cdot16^4=545\cdot481=(5\cdot109)(13\cdot37)$). The numbers $5,13,37,109$ are prime ($109$ is not divisible by $2,3,5,7$, and $11^2>109$). Hence
\[
2^{18}+1=262145=\boxed{5\cdot13\cdot37\cdot109}.
\]''',
'Prime factorisation|Sum and difference of cubes|Factoring',3)

b.save()
