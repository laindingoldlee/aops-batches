from qb import *
b=Bank('p233_03')

RA=r'''void ra(pair P,pair Q,pair R,real s){pair u=unit(Q-P),v=unit(R-P);draw(P+s*u--P+s*u+s*v--P+s*v,linewidth(0.5));}
'''

# ---------------- 1716595 man and tree shadows
fig=RA+r'''pair T=(0,0),Tt=(0,9),M=(6,0),Mt=(6,1.5),X=(7.2,0);
draw((-0.8,0)--(8.2,0),linewidth(0.6));
draw(T--Tt,linewidth(1.6));draw(M--Mt,linewidth(1.4));
draw(Tt--X,dashed);
ra(T,X,Tt,0.35);ra(M,X,Mt,0.25);
label("$9$",(0,4.5),W);label("$1.5$",(6,0.75),W);
label("$6$",(3,0),S);label("$1.2$",(6.6,0),S);
label("$X$",X,SE);'''
b.add(1716595,1,r'''A man $1.5$ metres tall stands $6$ metres from a tree, on the side away from the sun, so that the tip of his shadow coincides with the tip of the tree's shadow. His shadow is $1.2$ metres long. What is the height of the tree?''',
r'''The sun's rays are parallel, so the ray over the top of the man also passes over the top of the tree and both shadows end at the same point $X$. The man and the tree are both vertical, so the right triangles formed by the man and his shadow and by the tree and its shadow are similar (they share the angle at $X$). The tree's shadow is $6+1.2=7.2$ metres long, so
\[
\dfrac{h}{7.2}=\dfrac{1.5}{1.2}\quad\Longrightarrow\quad h=7.2\cdot1.25=\boxed{9\text{ metres}}.
\]
'''+asy(fig,'6cm'),
'Similarity|Right triangles|Ratios, proportions, and variation',2,
note='The post does not say where the shadows end; the standard reading (the man stands between the tree and the common tip of the two shadows) is stated in the question.')

# ---------------- 1717421 compare
b.add(1717421,1,r'''Compare the numbers $A=5+2\sqrt5$ and $B=\sqrt{45+20\sqrt5}$.''',
r'''Both numbers are positive, so compare their squares:
\[
A^2=25+20\sqrt5+4\cdot5=45+20\sqrt5=B^2 .
\]
Hence $\boxed{A=B}$.''',
'Radicals|Algebraic expressions and identities',2,source=src('Junior Regional Olympiad FBH',2014,'Grade 8',1))

# ---------------- 1717426 two odd two even digits
b.add(1717426,1,r'''How many $4$-digit numbers have exactly two odd digits and two even digits?''',
r'''The thousands digit has $5$ odd choices ($1,3,5,7,9$) and $4$ even choices ($2,4,6,8$); each other digit has $5$ odd and $5$ even choices.
\begin{itemize}
\item Thousands digit odd: one more of the other three digits is odd ($3$ ways to choose which), so $5\cdot3\cdot5^3=1875$.
\item Thousands digit even: two of the other three digits are odd ($3$ ways), so $4\cdot3\cdot5^3=1500$.
\end{itemize}
Total $1875+1500=\boxed{3375}$.''',
'Casework|Multiplication principle|Parity|Digit problems',2,source=src('Junior Regional Olympiad FBH',2014,'Grade 8',5))

# ---------------- 1717419 5-digit numbers divisible by 5
b.add(1717419,1,r'''Five-digit numbers with all digits different are written using the digits $0,1,3,4,7,9$. How many of them are divisible by $5$?''',
r'''A number divisible by $5$ ends in $0$ or $5$; there is no $5$ among the digits, so the last digit is $0$. The first four digits are then an ordered choice of $4$ of the remaining $5$ digits $1,3,4,7,9$ (none of which is $0$, so the leading digit is fine): $5\cdot4\cdot3\cdot2=\boxed{120}$.''',
'Divisibility rules|Permutations',2,source=src('Junior Regional Olympiad FBH',2014,'Grade 7',5))

# ---------------- 1717412 trapezoid perpendicular diagonals
fig=RA+r'''transform t=rotate(degrees((4,3)));
pair O=t*(0,0),A=t*(-4,0),C=t*(2,0),B=t*(0,-3),D=t*(0,1.5);
pair K=C+(B-D);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--C,linewidth(0.7));draw(B--D,linewidth(0.7));
draw(B--K,dashed);draw(C--K,dashed+blue);
ra(O,C,D,0.22);ra(C,A,K,0.22);
dot(O);dot(K);
label("$A$",A,SW);label("$B$",B,S);label("$C$",C,NE);label("$D$",D,NW);label("$O$",O,dir(-10)*1.6);label("$K$",K,SE);
label("$a$",(A+B)/2,S);label("$c$",(D+C)/2,N);label("$c$",(B+K)/2,S);'''
b.add(1717412,1,r'''Let $ABCD$ be a trapezoid with bases $AB$ and $CD$ ($AB\parallel CD$, $AB\ne CD$), and let $AB=a$, $BC=b$, $CD=c$, $DA=d$, $AC=m$ and $BD=n$. Suppose that $m^2+n^2=(a+c)^2$.
\begin{enumerate}
\item[(a)] Prove that the lines $AC$ and $BD$ are perpendicular.
\item[(b)] Prove that $ac<bd$.
\end{enumerate}''',
r'''\textbf{(a)} Through $C$ draw the line parallel to $BD$; it meets line $AB$ at $K$. Since $DC\parallel BK$ and $CK\parallel DB$, the quadrilateral $DBKC$ is a parallelogram, so $BK=DC=c$ and $CK=DB=n$. Because $\overrightarrow{AB}$ and $\overrightarrow{DC}$ point the same way, $K$ lies on ray $AB$ beyond $B$ and $AK=a+c$.
'''+asy(fig,'6.5cm')+r'''
In triangle $ACK$,
\[
AC^2+CK^2=m^2+n^2=(a+c)^2=AK^2,
\]
so by the converse of Pythagoras' theorem $\angle ACK=90^\circ$. As $CK\parallel BD$, also $AC\perp BD$. $\blacksquare$

\textbf{(b)} Let the diagonals meet at $O$. Since $AB\parallel CD$, triangles $OAB$ and $OCD$ are similar with ratio $a:c$, so there are $s,t>0$ with
\[
OA=at,\quad OC=ct,\quad OB=as,\quad OD=cs .
\]
By (a) the angles at $O$ are right angles. Pythagoras' theorem in the four right triangles around $O$ gives
\[
a^2=a^2(t^2+s^2),\qquad b^2=a^2s^2+c^2t^2,\qquad d^2=a^2t^2+c^2s^2 ,
\]
so $t^2+s^2=1$. Then
\[
b^2d^2-a^2c^2=(a^2s^2+c^2t^2)(a^2t^2+c^2s^2)-a^2c^2(s^2+t^2)^2=s^2t^2\left(a^4+c^4-2a^2c^2\right)=s^2t^2(a^2-c^2)^2 .
\]
Since $a\ne c$ (the bases of a trapezoid that is not a parallelogram are unequal), this is positive, so $b^2d^2>a^2c^2$ and $bd>ac$. $\blacksquare$''',
'Trapezoids|Pythagorean theorem|Parallelograms|Similarity|Diagonals|Perpendicular lines',5,source=src('Junior Regional Olympiad FBH',2014,'Grade 7',3),
note='The assumption AB != CD is stated (for a rhombus, a = c and ac = bd). The identity in (b) was checked symbolically and the claims numerically.')

# ---------------- 1717410 wheat moisture
b.add(1717410,1,r'''Raw wheat contains $70\%$ moisture and dry wheat contains $10\%$ moisture. A miller buys $3$ tons of raw wheat at $0.4$ dollars per kilogram and dries it. At what price per kilogram must he sell the dry wheat to make an $80\%$ profit?''',
r'''The $3000$ kg of raw wheat contains $30\%$ dry matter, i.e.\ $900$ kg. In the dry wheat this dry matter is $90\%$ of the mass, so the dry wheat weighs $\dfrac{900}{0.9}=1000$ kg.

The miller paid $3000\cdot0.4=1200$ dollars. An $80\%$ profit means a revenue of $1.8\cdot1200=2160$ dollars, so the price must be $\dfrac{2160}{1000}=\boxed{2.16\text{ dollars per kilogram}}$.''',
'Percentages|Mixture problems|Money and currency',3,source=src('Junior Regional Olympiad FBH',2014,'Grade 7',2))

# ---------------- 1717408 ratios
b.add(1717408,1,r'''If $a:b=4:3$ and $b:c=2:5$, find the value of $(3a-2b):(b+2c)$.''',
r'''Make the two ratios agree in $b$: $a:b=8:6$ and $b:c=6:15$, so $a:b:c=8:6:15$. Put $a=8k$, $b=6k$, $c=15k$ ($k\ne0$). Then
\[
(3a-2b):(b+2c)=(24k-12k):(6k+30k)=12:36=\boxed{1:3}.
\]''',
'Ratios, proportions, and variation',2,source=src('Junior Regional Olympiad FBH',2014,'Grade 7',1))

# ---------------- 1717403 absent students
b.add(1717403,1,r'''In a class, the number of absent students is $\dfrac16$ of the number of students present. When the teacher sends one of the present students out to bring chalk, the number of absent students becomes $\dfrac15$ of the number of students present. How many students are in the class?''',
r'''Let $p$ students be present at first; then $\dfrac p6$ are absent. After one student leaves, $p-1$ are present and $\dfrac p6+1$ are absent, so
\[
\dfrac p6+1=\dfrac{p-1}{5}\ \Longrightarrow\ 5p+30=6p-6\ \Longrightarrow\ p=36 .
\]
So $36$ were present and $6$ absent: the class has $\boxed{42}$ students. Check: $7$ absent and $35$ present after the errand, and $7=\dfrac{35}{5}$.''',
'Fractions|Linear equations',2,source=src('Junior Regional Olympiad FBH',2014,'Grade 6',2))

# ---------------- 1717404 bisector of right angle
fig=RA+r'''pair A=(0,0),B=(10,0),C=(3.6,4.8),H=(3.6,0),M=(5,0),L=(30/7,0);
draw(A--B--C--cycle,linewidth(0.9));
draw(C--H,linewidth(0.7));draw(C--M,linewidth(0.7)+blue);draw(C--L,linewidth(0.7)+red);
ra(H,B,C,0.3);ra(C,A,B,0.35);
draw(arc(C,2.8,degrees(H-C),degrees(L-C)),linewidth(0.5));
draw(arc(C,2.8,degrees(L-C),degrees(M-C)),linewidth(0.5));
draw(C+2.65*dir((degrees(H-C)+degrees(L-C))/2)--C+2.95*dir((degrees(H-C)+degrees(L-C))/2),linewidth(0.5));
draw(C+2.65*dir((degrees(L-C)+degrees(M-C))/2)--C+2.95*dir((degrees(L-C)+degrees(M-C))/2),linewidth(0.5));
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,N);
label("$H$",H,S);label("$L$",L,S);label("$M$",M,S);'''
b.add(1717404,1,r'''Let $ABC$ be a right triangle with the right angle at $C$. Prove that the bisector of the right angle also bisects the angle between the median and the altitude drawn from $C$ to the hypotenuse.''',
r'''Let $CH$ be the altitude, $CM$ the median and $CL$ the bisector, with $H,M,L$ on $AB$. If $CA=CB$ the three lines coincide and there is nothing to prove, so assume $CA<CB$; then $\angle B<45^\circ<\angle A$.

\textbf{$\angle ACH=\angle B$.} In the right triangle $ACH$, $\angle ACH=90^\circ-\angle A=\angle B$.

\textbf{$\angle MCB=\angle B$.} The midpoint $M$ of the hypotenuse is the centre of the circumcircle, so $MC=MB$ and triangle $MBC$ is isosceles: $\angle MCB=\angle MBC=\angle B$.

Since $\angle ACH=\angle B<45^\circ=\angle ACL$ and $\angle MCB=\angle B<45^\circ=\angle LCB$, the rays from $C$ come in the order $CA,CH,CL,CM,CB$, and
\[
\angle HCL=\angle ACL-\angle ACH=45^\circ-\angle B=\angle LCB-\angle MCB=\angle LCM .
\]
So $CL$ bisects angle $HCM$. $\blacksquare$
'''+asy(fig,'6.5cm')+r'''
In the figure $CA=6$, $CB=8$, $AB=10$: the altitude $CH$ (black), the bisector $CL$ (red) and the median $CM$ (blue), with the equal angles $HCL$ and $LCM$ marked.''',
'Right triangles|Angle bisectors|Medians and centroids|Altitudes|Angle chasing',3,source=src('Junior Regional Olympiad FBH',2014,'Grade 6',3))

# ---------------- 1717359 KEP round eight
fig=r'''pair A=(0,1),B=(-5.5,0),C=(5.5,0),Ep=(-0.5,0),D=(0.5,0);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--Ep,linewidth(0.7));draw(A--D,linewidth(0.7));
draw((0,0)--A,dotted);
label("$A$",A,N);label("$B$",B,W);label("$C$",C,E);label("$E$",Ep,dir(-110));label("$D$",D,dir(-70));
label("$5$",(-3,0),S);label("$1$",(0,-0.25),S);label("$5$",(3,0),S);'''
b.add(1717359,1,r'''In isosceles triangle $ABC$ with $AB=AC$, points $E$ and $D$ lie on side $BC$, in the order $B,E,D,C$, such that $AE$ and $AD$ trisect $\angle BAC$. If $CD=5$ and $DE=1$, find $AC$.''',
r'''The reflection in the axis of symmetry of the triangle (the altitude from $A$) swaps $B$ and $C$ and swaps the two trisectors, so it swaps $D$ and $E$. Hence $BE=CD=5$, $BC=11$ and $AE=AD$.

In triangle $AEC$, the segment $AD$ bisects $\angle EAC$ (it splits it into two of the three equal parts of $\angle A$). By the angle bisector theorem,
\[
\dfrac{AE}{AC}=\dfrac{ED}{DC}=\dfrac15,\qquad\text{so } AC=5\,AE .
\]
Let $h$ be the height from $A$; its foot is the midpoint of $BC$ and $ED$, which is at distance $\dfrac12$ from $E$ and $\dfrac{11}2$ from $C$. So
\[
AE^2=h^2+\dfrac14,\qquad AC^2=h^2+\dfrac{121}4,\qquad AC^2-AE^2=30 .
\]
With $AC^2=25AE^2$ this gives $24AE^2=30$, $AE^2=\dfrac54$, and
\[
AC^2=\dfrac{125}{4},\qquad AC=\boxed{\dfrac{5\sqrt5}{2}}.
\]
(Then $h=1$; the triangle is very flat, with $\angle A\approx159.6^\circ$.)
'''+asy(fig,'9cm'),
'Angle bisector theorem|Isosceles triangles|Pythagorean theorem|Symmetry',4,
note='Repeat of the b232 draft 1724486-q03 (same KEP problem, same repair; aliased). KEP round 8, problem 1. The posted data are inconsistent: CD = 5 and DE = 1 already force AE = sqrt(5)/2, so the given AE = 9 is impossible, and the points F, G (trisectors of angle C) play no role. The record drops AE = 9 and F, G, states the order B, E, D, C, and asks for AC. Checked with coordinates (h = 1).')

b.add(1717359,2,r'''The minimum value of $y=\sqrt{2x^2-3}+\sqrt{3x+5}$ (over all real $x$ for which it is defined) can be written as $\sqrt{a-\dfrac{b\sqrt c}{d}}$, where $a,b,c,d$ are positive integers, $c$ is squarefree and $\dfrac bd$ is in lowest terms. Find $a+b+c+d$.''',
r'''The expression is defined when $2x^2\ge3$ and $3x\ge-5$, i.e.\ on $\left[-\dfrac53,-\dfrac{\sqrt6}{2}\right]\cup\left[\dfrac{\sqrt6}2,\infty\right)$. Let $x_0=-\dfrac{\sqrt6}2$; then $y(x_0)=\sqrt{3x_0+5}=\sqrt{5-\dfrac{3\sqrt6}{2}}\approx1.151$.

\textbf{Right part.} For $x\ge\dfrac{\sqrt6}2$ both square roots increase, so $y\ge y\left(\dfrac{\sqrt6}2\right)=\sqrt{5+\dfrac{3\sqrt6}2}>y(x_0)$.

\textbf{Left part.} Let $x=x_0-t$ with $0\le t\le\dfrac53-\dfrac{\sqrt6}2<0.45$, and $k=3x_0+5=5-\dfrac{3\sqrt6}2>0$. Then
\[
\sqrt{k}-\sqrt{3x+5}=\dfrac{3t}{\sqrt k+\sqrt{3x+5}}\le\dfrac{3t}{\sqrt k},
\qquad 2x^2-3=2(x^2-x_0^2)=2t(|x|+|x_0|)\ge4|x_0|\,t=2\sqrt6\,t .
\]
So $y(x)\ge y(x_0)$ holds if $\sqrt{2\sqrt6\,t}\ge\dfrac{3t}{\sqrt k}$, i.e.\ if $2\sqrt6\,k\ge9t$. Here $2\sqrt6\,k=10\sqrt6-18>6.4$ while $9t<4.1$. Hence the minimum is attained at $x_0$:
\[
y_{\min}=\sqrt{5-\dfrac{3\sqrt6}{2}},
\]
so $(a,b,c,d)=(5,3,6,2)$ and $a+b+c+d=\boxed{16}$.''',
'Maxima and minima|Radicals|Inequalities|Bounding and extremal cases',5,
note='Repeat of the b232 draft 1723304-q01 (aliased). KEP round 8, problem 2. "a, b, c, d integers in simplest form" made precise (c squarefree, b/d in lowest terms). The minimum lies at the endpoint x = -sqrt(6)/2 of the left part of the domain; checked numerically.')

b.add(1717359,3,r'''Find the sum of all prime numbers $p$ such that the decimal expansion of $\dfrac1p$ has a repetend (period) of length exactly $4$.''',
r'''If $\dfrac1p$ has period exactly $4$, then $p$ divides $10^4-1=9999$ (multiply by $10^4$ and subtract), but $p$ does not divide $10^k-1$ for $k=1,2,3$ (otherwise the period would be shorter), and $p\ne2,5$. Now $9999=3^2\cdot11\cdot101$.
\begin{itemize}
\item $p=3$: $\dfrac13=0.\overline{3}$, period $1$ ($3\mid9$).
\item $p=11$: $\dfrac1{11}=0.\overline{09}$, period $2$ ($11\mid99$).
\item $p=101$: $101\nmid9,99,999$, and $\dfrac1{101}=0.\overline{0099}$, period $4$.
\end{itemize}
So the only such prime is $101$, and the sum is $\boxed{101}$.''',
'Repeating decimals|Multiplicative order|Prime factorisation|Divisibility',4,
note='KEP round 8, problem 3; answer 101 as in the posted solution.')

b.add(1717359,4,r'''A function whose graph has exactly two asymptotes, $x=-4$ and $y=2x-2$, is written as
\[
f(x)=\dfrac{ax^2+bx+\dfrac cf}{dx+e},
\]
where $a,b,c,d,e,f$ are positive integers and $a,b,d,e$ have no common factor greater than $1$. (Different $c$ and $f$ give different functions with the same asymptotes.) Find $a+b+d+e$.''',
r'''The vertical asymptote is where $dx+e=0$, so $-\dfrac ed=-4$ and $e=4d$. Write $K=\dfrac cf$. Dividing,
\[
f(x)=\dfrac{ax^2+bx+K}{d(x+4)}=\dfrac ad\,x+\dfrac{b-4a}{d}+\dfrac{16a-4b+K}{d(x+4)} .
\]
The slant asymptote is $y=\dfrac ad x+\dfrac{b-4a}d$, so $\dfrac ad=2$ and $\dfrac{b-4a}{d}=-2$, giving $a=2d$ and $b=6d$. Thus $(a,b,d,e)=d\,(2,6,1,4)$, and since they have no common factor, $d=1$:
\[
f(x)=\dfrac{2x^2+6x+K}{x+4}=2x-2+\dfrac{K+8}{x+4}.
\]
For every positive $K$ the remainder $K+8$ is nonzero, so both asymptotes really occur, which is why $c$ and $f$ can vary. The answer is $2+6+1+4=\boxed{13}$.''',
'Functions|Polynomials',3,
note='Repeat of the b232 draft 1724486-q01 (same repair; aliased). KEP round 8, problem 4. As posted, a, b, d, e are only determined up to a common factor (any multiple of (2, 6, 1, 4) works); the record adds that they have no common factor greater than 1.')

fig=r'''pair A=(0,3),B=(0,0),C=(4,0),Ep=(1.5,0),D=(12/25,66/25),F=(0.4,2.2),O=(2.75,2);
draw(circle(O,sqrt(89)/4),blue+linewidth(0.6));
draw(A--B--C--cycle,linewidth(0.9));
draw(A--Ep,linewidth(0.7));draw(B--D,linewidth(0.7));
draw(O--A,dashed);draw(O--B,dashed);
draw(B--(0.18,0)--(0.18,0.18)--(0,0.18),linewidth(0.5));
dot(O);dot(F);dot(D);dot(Ep);
label("$A$",A,NW);label("$B$",B,SW);label("$C$",C,SE);label("$E$",Ep,S);
label("$D$",D,dir(-68)*1.6);label("$F$",F,W);label("$O$",O,E);'''
b.add(1717359,5,r'''Triangle $ABC$ has $AB=3$, $BC=4$ and $AC=5$. Point $E$ is on segment $BC$ such that $AE$ bisects $\angle BAC$. Point $D$ lies on segment $AC$, and $F$ is the intersection of segments $BD$ and $AE$. The points $C$, $D$, $F$, $E$ lie on a circle with centre $O$. The value of $OA+OB$ can be written as $\dfrac{\sqrt a+\sqrt b}{c}$, where $a$ and $b$ are positive integers relatively prime to the positive integer $c$. Find $a+b+c$.''',
r'''Since $3^2+4^2=5^2$, the angle at $B$ is right. Put $B=(0,0)$, $C=(4,0)$, $A=(0,3)$, and let $\alpha=\angle BAC$, $\gamma=\angle BCA$, so $\tan\gamma=\dfrac34$ and $\tan\alpha=\dfrac43$. By the angle bisector theorem $\dfrac{BE}{EC}=\dfrac{AB}{AC}=\dfrac35$, so $BE=\dfrac32$ and $E=\left(\dfrac32,0\right)$.

\textbf{Locating $D$.} In the cyclic quadrilateral $CDFE$ the exterior angle at $D$ equals the interior angle at $E$: $\angle ADB=\angle ADF=\angle FEC=\angle AEC$. From triangles $ABD$ and $AEC$,
\[
180^\circ-\alpha-\angle ABD=180^\circ-\dfrac\alpha2-\gamma\quad\Longrightarrow\quad\angle ABD=\gamma-\dfrac\alpha2 .
\]
Here $\tan\dfrac\alpha2=\dfrac{\sin\alpha}{1+\cos\alpha}=\dfrac{\ \dfrac45\ }{\ \dfrac85\ }=\dfrac12$, so
\[
\tan\angle ABD=\dfrac{\dfrac34-\dfrac12}{1+\dfrac38}=\dfrac2{11}.
\]
Since $\angle ABD$ is measured from $BA$ (the $y$-axis), line $BD$ is $x=\dfrac{2}{11}y$. It meets $AC$: $\dfrac x4+\dfrac y3=1$ at $D=\left(\dfrac{12}{25},\dfrac{66}{25}\right)$, and $AE$: $2x+y=3$ at $F=\left(\dfrac25,\dfrac{11}5\right)$.

\textbf{The centre.} $O$ lies on the perpendicular bisector $x=\dfrac{11}4$ of $CE$; write $O=\left(\dfrac{11}4,k\right)$. From $OC^2=OD^2$:
\[
\dfrac{25}{16}+k^2=\left(\dfrac{227}{100}\right)^2+\left(k-\dfrac{66}{25}\right)^2\ \Longrightarrow\ \dfrac{132}{25}k=\dfrac{105600}{10000}\ \Longrightarrow\ k=2 .
\]
So $O=\left(\dfrac{11}4,2\right)$ and the radius is $\sqrt{\dfrac{25}{16}+4}=\dfrac{\sqrt{89}}4$. (Check: $OF^2=\left(\dfrac{47}{20}\right)^2+\left(\dfrac15\right)^2=\dfrac{2225}{400}=\dfrac{89}{16}$, so $F$ is on the circle too.)
'''+asy(fig,'6cm')+r'''
Finally
\[
OA=\sqrt{\dfrac{121}{16}+1}=\dfrac{\sqrt{137}}4,\qquad OB=\sqrt{\dfrac{121}{16}+4}=\dfrac{\sqrt{185}}4,
\]
so $OA+OB=\dfrac{\sqrt{137}+\sqrt{185}}{4}$, and $a+b+c=137+185+4=\boxed{326}$.''',
'Cyclic quadrilaterals|Angle bisector theorem|Coordinate geometry|Right triangles|Trigonometry|Circumcircles and circumcentres',6,
note='KEP round 8, problem 5 (proposed by kvedula2004); no solution was posted. The position of D was found from the cyclic condition and confirmed numerically (unique D on AC).')

# ---------------- 1710109 KEP round seven
b.add(1710109,1,r'''Let $F_n$ be the $n$-th Fibonacci number ($F_1=F_2=1$, $F_{n+1}=F_n+F_{n-1}$). What is the greatest possible value of $\gcd(F_n,F_{n+1})$?''',
r'''Any common divisor of $F_n$ and $F_{n+1}$ divides $F_{n+1}-F_n=F_{n-1}$, and conversely, so $\gcd(F_n,F_{n+1})=\gcd(F_{n-1},F_n)$ for $n\ge2$. Repeating this down to $\gcd(F_1,F_2)=\gcd(1,1)=1$ shows that $\gcd(F_n,F_{n+1})=1$ for all $n$. The greatest possible value is $\boxed{1}$.''',
'Fibonacci sequence|HCF and LCM|Recurrence relations',2,
note='KEP round 7, problem 1.')
b.add(1710109,2,r'''The graph of $3xy=x^2+2y$ has two asymptotes. If they are written as $x=ay+b$ and $x=cy+d$, what is $a+b+c+d$?''',
r'''Solving for $y$: $y(3x-2)=x^2$, so $y=\dfrac{x^2}{3x-2}$. Long division gives
\[
y=\dfrac13x+\dfrac29+\dfrac{4}{9(3x-2)} .
\]
So there is a vertical asymptote $x=\dfrac23$, i.e.\ $x=0\cdot y+\dfrac23$, and a slant asymptote $y=\dfrac13x+\dfrac29$, i.e.\ $x=3y-\dfrac23$. Hence
\[
a+b+c+d=0+\dfrac23+3-\dfrac23=\boxed{3}.
\]''',
'Functions|Polynomials',3,
note='KEP round 7, problem 2; answer 3 as posted.')

fig=r'''pair A=(0,0),B=(9,0),C=(17/18,sqrt(36-(17/18)^2));
pair D=(B+C)/2,F=(3.375,0);
pair P=extension(A,D,C,F),Ep=extension(B,P,A,C);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--D,linewidth(0.7));draw(C--F,linewidth(0.7));draw(B--Ep,linewidth(0.7)+blue);
dot(P);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,N);label("$D$",D,NE);label("$F$",F,S);label("$E$",Ep,W);label("$P$",P,dir(245)*1.5);'''
b.add(1710109,3,r'''In $\triangle ABC$, $AB=9$ and $AC=6$. $D$ is the midpoint of $BC$, and $F$ is the point on $AB$ such that $CF$ bisects $\angle C$. The segments $AD$ and $CF$ meet at $P$, and line $BP$ meets $AC$ at $E$. As $BC$ varies over all values for which the triangle exists, $AE$ takes values in an interval. The sum of the greatest lower bound and the least upper bound of the possible values of $AE$ can be written as $\dfrac mn$ in lowest terms. Find $m+n$.''',
r'''Let $BC=x$. By the angle bisector theorem $\dfrac{AF}{FB}=\dfrac{CA}{CB}=\dfrac6x$, and $\dfrac{BD}{DC}=1$. By Ceva's theorem for the concurrent cevians $AD$, $BE$, $CF$,
\[
\dfrac{AF}{FB}\cdot\dfrac{BD}{DC}\cdot\dfrac{CE}{EA}=1\ \Longrightarrow\ \dfrac{CE}{EA}=\dfrac x6\ \Longrightarrow\ AE=\dfrac{6\cdot6}{6+x}=\dfrac{36}{x+6}.
\]
'''+asy(fig,'6cm')+r'''
The triangle exists exactly for $3<x<15$, and $\dfrac{36}{x+6}$ decreases from $\dfrac{36}{9}=4$ to $\dfrac{36}{21}=\dfrac{12}{7}$. So $AE$ takes all values in the open interval $\left(\dfrac{12}7,4\right)$; these endpoints are not attained (they correspond to degenerate triangles) but are the greatest lower bound and least upper bound. Their sum is $\dfrac{12}{7}+4=\dfrac{40}{7}$, and $m+n=\boxed{47}$.''',
"Ceva's theorem|Angle bisector theorem|Triangle inequality|Triangles|Bounding and extremal cases",4,
note='KEP round 7, problem 3. As posted it asks for the "minimum and maximum possible values" of AE, but the bounds 12/7 and 4 are attained only by degenerate triangles (the posted solution uses 3 <= BC <= 15); the record asks for the greatest lower bound and least upper bound. Answer 47 as posted.')

b.add(1710109,5,r'''Find the sum of all three-digit positive integers $N$ such that $\varphi(\varphi(N))=20$, where $\varphi$ is Euler's totient function.''',
r'''Recall that $\varphi\left(p_1^{k_1}\cdots p_r^{k_r}\right)=\prod p_i^{k_i-1}(p_i-1)$, that $\varphi(n)$ is even for $n\ge3$, and that if a prime $p$ divides $n$ then $p-1\mid\varphi(n)$.

\textbf{Step 1: $\varphi(M)=20$.} The primes dividing $M$ satisfy $p-1\mid20$, so $p\in\{2,3,5,11\}$; since $3,11\nmid20$, the primes $3$ and $11$ appear at most to the first power, and $5$ at most squared.
\begin{itemize}
\item If $11\mid M$: $\varphi(11)=10$, and the rest $M'$ needs $\varphi(M')=2$, so $M'\in\{3,4,6\}$: $M=33,44,66$.
\item If $11\nmid M$ and $25\mid M$: $\varphi(25)=20$ and $M'\in\{1,2\}$: $M=25,50$.
\item Otherwise $\varphi(M)$ is $2^i$ or $4\cdot2^i$ (from $2$, $3$, $5$ to the first power), never $20$.
\end{itemize}
So $M\in\{25,33,44,50,66\}$, and $M=\varphi(N)$ must be even (or $1$): $M\in\{44,50,66\}$.

\textbf{Step 2: $\varphi(N)=44$.} Possible primes: $p-1\mid44$ gives $p\in\{2,3,5,23\}$. The factor $11$ can only come from $23-1=22$, so $23\,\|\,N$ and the rest $N'$ has $\varphi(N')=2$: $N=69,92,138$.

\textbf{$\varphi(N)=50$.} Possible primes: $p\in\{2,3,11\}$, and the factor $25$ cannot arise ($5\nmid N$, and $11$ appears at most once, giving one factor $5$). No solutions.

\textbf{$\varphi(N)=66$.} Possible primes: $p\in\{2,3,7,23,67\}$. The factor $11$ comes from $23$ (leaving $\varphi(N')=3$, impossible) or from $67$ (leaving $\varphi(N')=1$, $N'\in\{1,2\}$): $N=67,134$.

All solutions are $67,69,92,134,138$; the three-digit ones are $134$ and $138$, with sum $\boxed{272}$.''',
"Euler's theorem and totient|Prime factorisation|Casework",5,
note='KEP round 7, problem 5; answer 272 as posted. Checked by computing phi(phi(N)) for all N < 1000.')

# ---------------- 1717292 Math Madness triples
b.add(1717292,1,r'''Let $a$, $b$, $c$ be chosen from $\{0,1,2,\dots,100\}$, not necessarily distinct, with $a\ge b$. How many ordered triples $(a,b,c)$ satisfy both $|a-b|=c$ and $|b-c|=a$?''',
r'''Since $a\ge b$, the first condition gives $c=a-b$. Then $b-c=2b-a$, and the second condition is $|2b-a|=a$, so $2b-a=a$ or $2b-a=-a$, i.e.\ $b=a$ or $b=0$.
\begin{itemize}
\item $b=a$: then $c=0$, giving the triples $(a,a,0)$ for $a=0,\dots,100$: $101$ triples.
\item $b=0$: then $c=a$, giving $(a,0,a)$ for $a=0,\dots,100$: $101$ triples.
\end{itemize}
The triple $(0,0,0)$ is counted twice, so there are $101+101-1=\boxed{201}$ triples.''',
'Absolute value|Casework|Systems of linear equations',3,
note='Checked by brute force.')

# ---------------- 1715899 BE=2AE
fig=r'''pair A=(1,4),B=(0,0),C=(6,0);
pair D=(B+C)/2,Sm=(A+D)/2;
pair Ep=extension(C,Sm,A,B);
pair M=extension(D,D+(Ep-C),A,B);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--D,linewidth(0.7));draw(C--Ep,linewidth(0.7));
draw(D--M,dashed+blue);
dot(Sm);dot(M);dot(Ep);dot(D);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$D$",D,S);
label("$S$",Sm,dir(45));label("$E$",Ep,W);label("$M$",M,W);'''
b.add(1715899,1,r'''Let $AD$ be a median of triangle $ABC$ and let $S$ be the midpoint of $AD$. The line $CS$ meets $AB$ at $E$. Prove that $BE=2AE$.''',
r'''Through $D$ draw the line parallel to $CE$; it meets $AB$ at $M$.
'''+asy(fig,'5.5cm')+r'''
\begin{itemize}
\item In triangle $BCE$, $D$ is the midpoint of $BC$ and $DM\parallel CE$, so by the midpoint theorem $M$ is the midpoint of $BE$: $BM=ME$.
\item In triangle $ADM$, $S$ is the midpoint of $AD$ and $SE\parallel DM$ (as $E$ lies on line $CS$), so $E$ is the midpoint of $AM$: $AE=EM$.
\end{itemize}
Hence $BE=BM+ME=2EM=2AE$. $\blacksquare$''',
'Midpoints|Parallel lines|Medians and centroids|Triangles',3,source=src('Junior Regional Olympiad FBH',2015,'Grade 6',3),
note='Checked with coordinates for random triangles.')

# ---------------- 1715029 compare fractions
b.add(1715029,1,r'''Which fraction is bigger: $\dfrac{5553}{5557}$ or $\dfrac{6664}{6669}$?''',
r'''Write each as $1$ minus a small fraction:
\[
\dfrac{5553}{5557}=1-\dfrac{4}{5557},\qquad\dfrac{6664}{6669}=1-\dfrac{5}{6669}.
\]
Compare $\dfrac4{5557}$ and $\dfrac5{6669}$ by cross-multiplying: $4\cdot6669=26676<27785=5\cdot5557$, so $\dfrac{4}{5557}<\dfrac{5}{6669}$. Subtracting the smaller amount from $1$ leaves more, so $\boxed{\dfrac{5553}{5557}}$ is bigger.''',
'Fractions|Inequalities',2,source=src('Junior Regional Olympiad FBH',2016,'Grade 6',2))

# ---------------- 1715574 N multiple of 12 with 14 divisors
b.add(1715574,1,r'''$N$ is a multiple of $12$ and has exactly $14$ positive divisors. Find $N$.''',
r'''If $N=p_1^{e_1}\cdots p_r^{e_r}$, it has $(e_1+1)\cdots(e_r+1)$ divisors. Since $14=14\cdot1=7\cdot2$, either $N=p^{13}$ or $N=p^6q$ with distinct primes $p,q$. As $12=2^2\cdot3\mid N$, $N$ has the two prime factors $2$ and $3$ with $2^2\mid N$, so $N=p^6q$ with $\{p,q\}=\{2,3\}$ and the exponent of $2$ at least $2$: $p=2$, $q=3$. Hence $N=2^6\cdot3=\boxed{192}$. Check: $(6+1)(1+1)=14$ and $192=12\cdot16$.''',
'Divisor counting|Prime factorisation|Factors and multiples',3,
note='The posted problem asks to compute N; it is unique. Checked by search.')

# ---------------- 1716607 point on line AB
fig=r'''import graph;
pair A=(0,1),B=(-2,-1),P=(5,6);
draw((-3.2,0)--(6,0),Arrow(TeXHead));draw((0,-2)--(0,7),Arrow(TeXHead));
draw((-3,-2)--(5.6,6.6),blue+linewidth(0.8));
draw(P--(5,0),dotted);
dot(A);dot(B);dot(P);
label("$A$",A,NW);label("$B$",B,NW);label("$E$",P,E);
label("$y=x+1$",(3.2,2.0),blue);
label("$x$",(6,0),N);label("$y$",(0,7),E);label("$5$",(5,0),S);'''
b.add(1716607,1,r'''The point $E(5,h)$ lies on the line through $A(0,1)$ and $B(-2,-1)$. What is the value of $h$?''',
r'''The slope of $AB$ is $\dfrac{1-(-1)}{0-(-2)}=1$, and the line passes through $(0,1)$, so its equation is $y=x+1$. For $x=5$, $h=5+1=\boxed{6}$.
'''+asy(fig,'5cm'),
'Slope|Coordinate geometry|Linear equations',1,
note='The opening word "Iftar" in the post is a typo and is dropped.')

# ---------------- 1716924 inequality
b.add(1716924,1,r'''Let $a,b,c$ be non-negative real numbers with $a+b+c=1$. Find the maximum value of $s=ab+bc+ca-3abc$.''',
r'''Let $c$ be the smallest of the three numbers, so $c\le\dfrac13$. Using $a+b=1-c$,
\[
s=ab(1-3c)+c(a+b)=ab(1-3c)+c(1-c).
\]
Since $1-3c\ge0$ and $ab\le\left(\dfrac{a+b}{2}\right)^2=\dfrac{(1-c)^2}{4}$ (AM-GM),
\[
s\le\dfrac{(1-c)^2(1-3c)}{4}+c(1-c)=\dfrac{1-c}{4}\bigl((1-c)(1-3c)+4c\bigr)=\dfrac{(1-c)(1+3c^2)}{4}.
\]
Finally $(1-c)(1+3c^2)=1-c(1-3c+3c^2)\le1$, because $1-3c+3c^2>0$ for all real $c$ (its discriminant $9-12$ is negative). Hence $s\le\dfrac14$, with equality when $c=0$ and $a=b=\dfrac12$: $s=\dfrac14$. The maximum is $\boxed{\dfrac14}$.''',
'AM-GM inequality|Inequalities|Maxima and minima',5,
note='Checked numerically on a fine grid of the simplex (for comparison, a = b = c = 1/3 gives only 2/9).')

# ---------------- 1716960 AHSME 1980 #21
fig=r'''pair B=(0,0),C=(6,0),A=4*dir(72);
pair D=(2,0),Ep=(A+C)/2,F=extension(A,D,B,Ep);
fill(B--D--F--cycle,palegray);fill(F--D--C--Ep--cycle,paleblue);
draw(A--B--C--cycle,linewidth(0.9));draw(A--D,linewidth(0.7));draw(B--Ep,linewidth(0.7));
draw(arc(B,0.6,0,72),linewidth(0.5));label("$72^\circ$",B+1.15*dir(55));
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$D$",D,S);label("$E$",Ep,NE);label("$F$",F,dir(150)*1.3);
label("$1$",(1,0),dir(-90)*1.6);label("$2$",(4,0),dir(-90)*1.6);'''
b.add(1716960,1,r'''In triangle $ABC$, $\angle CBA=72^\circ$, $E$ is the midpoint of side $AC$, and $D$ is a point on side $BC$ such that $2BD=DC$. The segments $AD$ and $BE$ intersect at $F$. Find the ratio of the area of triangle $BDF$ to the area of quadrilateral $FDCE$.''',
r'''The angle $72^\circ$ is not needed. Let the area of $ABC$ be $1$.

\textbf{Locating $F$.} Assign masses $A:1$, $C:1$ (so $E$, the midpoint of $AC$, has mass $2$) and $B:2$ (so that $2\cdot BD=1\cdot DC$, and $D$ has mass $3$). The balance point $F$ of the system lies on $BE$ and on $AD$, with
\[
\dfrac{BF}{FE}=\dfrac{2}{2}=1,\qquad\dfrac{AF}{FD}=\dfrac{3}{1}.
\]
\textbf{Areas.} $[ABD]=\dfrac{BD}{BC}[ABC]=\dfrac13$ and $[BDF]=\dfrac{FD}{AD}[ABD]=\dfrac14\cdot\dfrac13=\dfrac1{12}$. Also $[BEC]=\dfrac12$ because $E$ is the midpoint of $AC$, and the quadrilateral is
\[
[FDCE]=[BEC]-[BDF]=\dfrac12-\dfrac1{12}=\dfrac5{12}.
\]
'''+asy(fig,'6cm')+r'''
Hence $[BDF]:[FDCE]=\dfrac1{12}:\dfrac5{12}=\boxed{1:5}$.''',
'Mass points|Area ratios|Triangles|Midpoints',4,source=src('AHSME',1980,None,21),
note='Official answer 1/5. The answer choices are not in the post, so the record is free-response. Checked with coordinates.')

# ---------------- 1715535 right triangle AD=BC
fig=RA+r'''real x=(3*sqrt(5)-3)/2; real h=sqrt(x*(3-x));
pair A=(0,0),B=(3,0),D=(x,0),C=(x,h);
draw(A--B--C--cycle,linewidth(0.9));draw(C--D,linewidth(0.7));
ra(D,B,C,0.12);ra(C,A,B,0.14);
pair m1=(A+D)/2,m2=(B+C)/2,n2=unit(rotate(90)*(C-B));
draw(m1+(0,-0.07)--m1+(0,0.07));draw(m2-0.07*n2--m2+0.07*n2);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,N);label("$D$",D,S);
label("$3$",(1.5,-0.12),S);'''
b.add(1715535,1,r'''In right triangle $ABC$ with the right angle at $C$, $CD$ is the altitude to the hypotenuse, and $AD=BC$. If $AB=3$ cm, find $AC$.''',
r'''Let $AD=BC=x$. In a right triangle each leg is the geometric mean of the hypotenuse and its projection on the hypotenuse (triangles $CBD$ and $ABC$ are similar, as are $ACD$ and $ABC$):
\[
BC^2=BD\cdot AB,\qquad AC^2=AD\cdot AB .
\]
'''+asy(fig,'6cm')+r'''
With $BD=3-x$ the first relation gives $x^2=3(3-x)$, i.e.\ $x^2+3x-9=0$, so $x=\dfrac{3\sqrt5-3}{2}$ (the positive root). Then
\[
AC^2=3x=\dfrac{9\left(\sqrt5-1\right)}{2},\qquad AC=\boxed{3\sqrt{\dfrac{\sqrt5-1}{2}}}\ \text{cm}\approx2.36\text{ cm}.
\]
Check: $AC^2+BC^2=3x+x^2=3x+(9-3x)=9=AB^2$.

(The post also gives $CD=\sqrt2$, but this contradicts the other data: from $AD=BC$ and $AB=3$ we get $CD^2=AD\cdot DB=x(3-x)=9\sqrt5-18\approx2.12$, not $2$. With $CD=\sqrt2$ and $AB=3$ instead, $\{AD,DB\}=\{1,2\}$ and $BC=\sqrt6$ or $\sqrt3$, never equal to $AD$.)''',
'Right triangles|Similarity|Altitudes|Quadratic equations|Pythagorean theorem',4,
note='The posted data (AB = 3, CD = sqrt 2, AD = BC) are inconsistent, as shown in the solution; the record keeps AD = BC and AB = 3 and drops CD = sqrt 2. The right angle is taken at C (CD is the altitude to the hypotenuse).')

b.save()
