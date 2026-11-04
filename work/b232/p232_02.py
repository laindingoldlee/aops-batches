from qb import *
b=Bank('p232_02')

# ---------------- 1722695 5^400 mod 19
b.add(1722695,1,r'''Find the remainder when $5^{400}$ is divided by $19$.''',
r'''Since $19$ is prime and does not divide $5$, Fermat's little theorem gives $5^{18}\equiv1\pmod{19}$. As $400=18\cdot22+4$,
\[
5^{400}=\left(5^{18}\right)^{22}\cdot5^4\equiv5^4=625\pmod{19}.
\]
Finally $625=19\cdot32+17$, so the remainder is $\boxed{17}$.''',
'Modular exponentiation|Fermat\'s little theorem|Remainders and congruences',2)

# ---------------- 1726398 inverse of x^2
b.add(1726398,1,r'''Does the function $f(x)=x^2$, defined for all real numbers $x$, have an inverse function? If not, restrict its domain to $x\ge0$ and find the inverse of the restricted function.''',
r'''A function has an inverse function only if it is one-to-one (no two inputs give the same output). Here $f(2)=f(-2)=4$, so an inverse would have to send $4$ to both $2$ and $-2$, which a function cannot do. So $f(x)=x^2$ on all real numbers has \textbf{no} inverse function. (Graphically, the horizontal line $y=4$ meets the parabola twice.)

On the restricted domain $x\ge0$, the function is increasing, hence one-to-one, with range $y\ge0$. Solving $y=x^2$ with $x\ge0$ gives $x=\sqrt y$. So the inverse is $\boxed{f^{-1}(x)=\sqrt{x}\ \text{ for } x\ge0}$.''',
'Inverse functions|Functions',1,
note='The post asks only whether x^2 has an inverse; the record adds the restriction to x >= 0.')

# ---------------- 11090 two squares in two ways
b.add(11090,1,r'''\begin{enumerate}
\item[(a)] What is the smallest positive integer that can be written as the sum of two different \emph{positive} perfect squares in two different ways?
\item[(b)] What is the answer if $0=0^2$ is also allowed as one of the perfect squares?
\end{enumerate}''',
r'''\textbf{(a)} List the sums $a^2+b^2$ with $1\le a<b$ in increasing order:
\[
5,10,13,17,20,25,26,29,34,37,40,41,45,50,52,53,58,61,65,65,\dots
\]
(for $b\le7$, together with $64+1=65$ for $b=8$). The values below $65$ are all different, and $65=1^2+8^2=4^2+7^2$. So the answer is $\boxed{65}$.

\textbf{(b)} Allowing $0$ adds the sums $0^2+b^2=b^2$ for $b\ge1$, that is $1,4,9,16,25,\dots$. Now $25=0^2+5^2=3^2+4^2$. No smaller number works: the numbers below $25$ from part (a) are $5,10,13,17,20$, each in one way, and the new values $1,4,9,16$ are not among them. So the answer is $\boxed{25}$.

Since $0=0^2$ is a perfect square, $25$ is correct unless the problem says the squares are positive; the answer $65$ given with the original problem means that positive squares were intended.''',
'Perfect squares|Systematic counting',2,
note='The poster answered 25 (0 + 25 = 9 + 16) while the given answer was 65 and asked whether 0 counts as a perfect square. The record asks both versions: 65 for positive squares, 25 with 0 allowed.')

# ---------------- 1726419 11^12 mod 13 (alias)
b.add(1726419,1,r'''What is the remainder when $11^{12}$ is divided by $13$?''',
r'''Since $13$ is prime and $13\nmid11$, Fermat's little theorem gives $11^{12}\equiv1\pmod{13}$. The remainder is $\boxed{1}$.''',
'Fermat\'s little theorem|Remainders and congruences',2,
note='Repeat of an earlier record (aliased).')

# ---------------- 1726387 x^{log x} = x^3/100
b.add(1726387,1,r'''Find all real $x$ such that
\[
x^{\log x}=\dfrac{x^3}{100},
\]
where $\log$ denotes the base-$10$ logarithm.''',
r'''We need $x>0$. Both sides are positive, so take base-$10$ logarithms and put $t=\log x$:
\[
\log x\cdot\log x=3\log x-2\quad\Longrightarrow\quad t^2-3t+2=0\quad\Longrightarrow\quad(t-1)(t-2)=0 .
\]
So $t=1$ or $t=2$, i.e.\ $x=10$ or $x=100$. Check: $10^{1}=10=\dfrac{1000}{100}$ and $100^{2}=10^4=\dfrac{10^6}{100}$. The solutions are $\boxed{x=10\text{ and }x=100}$.''',
'Logarithms|Exponents|Quadratic equations|Substitution',3)

# ---------------- 1726281 four geometry problems
fig1=r'''pair T(real a){return dir(a);}
real[] t={95,200,265,330};
pair V(real a,real c){return dir((a+c)/2)/Cos((c-a)/2);}
pair L=V(t[0],t[1]),M=V(t[1],t[2]),Nn=V(t[2],t[3]),O=V(t[3],t[0]+360);
draw(unitcircle,gray);dot((0,0));label("$P$",(0,0),NE);
draw(L--M--Nn--O--cycle,linewidth(0.9));
for(int i=0;i<4;++i) dot(T(t[i]),blue);
label("$L$",L,dir(L));label("$M$",M,dir(M));label("$N$",Nn,dir(Nn));label("$O$",O,dir(O));
void tl(pair X,real a,string s){pair P=T(a);label(s,(X+P)/2,unit(X+P),blue+fontsize(9pt));}
tl(L,t[0],"$\ell$");tl(L,t[1],"$\ell$");
tl(M,t[1],"$m$");tl(M,t[2],"$m$");
tl(Nn,t[2],"$n$");tl(Nn,t[3],"$n$");
tl(O,t[3],"$o$");tl(O,t[0],"$o$");'''
b.add(1726281,1,r'''Quadrilateral $LMNO$ is circumscribed about circle $P$ (each side is tangent to the circle). Given that $MN=13$ and $OL=17$, find the perimeter of the quadrilateral.''',
r'''The two tangent segments from a point outside a circle to the circle are equal. Let the tangent lengths from $L,M,N,O$ be $\ell,m,n,o$.
'''+asy(fig1,'5cm')+r'''
Each side is the sum of the tangent lengths at its ends:
\[
LM=\ell+m,\quad MN=m+n,\quad NO=n+o,\quad OL=o+\ell .
\]
Hence $LM+NO=\ell+m+n+o=MN+OL=13+17=30$, and the perimeter is $30+30=\boxed{60}$.''',
'Tangents|Circles|Quadrilaterals and polygons|Lengths, perimeter, and area',2,
note='Problem 1 of four geometry questions in the post. The figure is not to scale.')
fig2=r'''real a=4.2,bb=2.4,c=2.0;pair d=(0.9,0.6);
pair O0=(0,0),X=(a,0),Y=(a,c),Z=(0,c);
draw(O0--X--Y--Z--cycle,linewidth(0.9));
draw(X--X+d--Y+d--Y,linewidth(0.9));draw(Y+d--Z+d--Z,linewidth(0.9));
draw(O0--O0+d,dashed);draw(O0+d--X+d,dashed);draw(O0+d--Z+d,dashed);
draw(O0--Y+d,red+linewidth(0.9));
label("$\ell$",(O0+X)/2,S);label("$h$",(X+Y)/2+(0.05,-0.15),E);label("$w$",X+d/2,SE);
label("$8$",(O0+Y+d)/2,NW,red);'''
b.add(1726281,2,r'''A rectangular box has total surface area $14$, and its longest interior diagonal has length $8$. Find the square of the sum of its length, width and height.''',
r'''Let the dimensions be $\ell,w,h$. The surface area gives $2(\ell w+wh+h\ell)=14$, and the space diagonal gives $\ell^2+w^2+h^2=8^2=64$ (Pythagoras twice: the diagonal of the base is $\sqrt{\ell^2+w^2}$, and the space diagonal is the hypotenuse of a right triangle with legs this base diagonal and $h$).
'''+asy(fig2,'5cm')+r'''
Therefore
\[
(\ell+w+h)^2=\ell^2+w^2+h^2+2(\ell w+wh+h\ell)=64+14=\boxed{78}.
\]
(Such a box exists, for example with $\ell=w\approx0.427$ and $h\approx7.977$; the figure is not to scale.)''',
'Cubes and rectangular prisms|Surface area|Pythagorean theorem|Algebraic expressions and identities',3,
note='Problem 2 of the post; the existence of such a box was checked numerically.')
fig3=r'''pair Z=(0,0),Ep=(16,0),Nn=(16,16),G=(0,16),M=(16,8),O=(6,8),H=(0,8);
draw(Z--Ep--Nn--G--cycle,linewidth(0.9));
draw(circle(O,10),blue+linewidth(0.8));
dot(O);dot(M);
draw(O--M,dashed);draw(O--Z,red+dashed);draw(O--H,dashed);
draw((0,8)--(0.9,8)--(0.9,8.9)--(0,8.9),linewidth(0.5));
draw((16,8)--(15.1,8)--(15.1,8.9)--(16,8.9),linewidth(0.5));
label("$Z$",Z,SW);label("$E$",Ep,SE);label("$N$",Nn,NE);label("$G$",G,NW);
label("$M$",M,E);label("$O$",O,N);label("$H$",H,W);
label("$r$",(O+M)/2,N);label("$r$",(O+Z)/2,SE,red);
label("$s-r$",(O+H)/2,S);label("$\dfrac s2$",(Z+H)/2,W);'''
b.add(1726281,3,r'''In square $ZENG$ (vertices in this order), $M$ is the midpoint of side $EN$. A circle $\omega$ passes through $Z$ and $G$ and is tangent to side $EN$ at $M$. If the radius of $\omega$ is $10$, what is the area of $ZENG$?''',
r'''Let the side be $s$ and the radius $r$. The centre $O$ lies on the perpendicular to $EN$ at $M$ (the radius to a point of tangency is perpendicular to the tangent), so $O$ is on the horizontal line through $M$ at distance $r$ from $EN$. This line also passes through the midpoint $H$ of $ZG$, and $OH=s-r$.
'''+asy(fig3,'5.5cm')+r'''
In right triangle $OHZ$, $OZ=r$, $OH=s-r$ and $HZ=\dfrac s2$, so
\[
r^2=(s-r)^2+\dfrac{s^2}{4}\quad\Longrightarrow\quad 0=s^2-2sr+\dfrac{s^2}4\quad\Longrightarrow\quad r=\dfrac{5s}{8}.
\]
With $r=10$ we get $s=16$, and the area is $16^2=\boxed{256}$.''',
'Squares|Circles|Tangents|Pythagorean theorem',4,
note='Problem 3 of the post says "circle w is constructed such that w is tangent to Z, and G", which is garbled; the record reads it as the standard problem: w passes through Z and G and is tangent to EN at its midpoint M (the only role M can play).')
fig4=r'''real h=4*sqrt(2),r=2*sqrt(2);
pair A=(-4,0),B=(4,0),C=(2,h),D=(-2,h),Q=(2,0),O=(0,r);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(circle(O,r),blue+linewidth(0.8));
draw(C--Q,dashed);draw(Q--Q+(-0.35,0)--Q+(-0.35,0.35)--Q+(0,0.35),linewidth(0.5));
label("$4$",(D+C)/2,N);draw((-4,-1.2)--(4,-1.2),Arrows(4));label("$8$",(0,-1.2),S);label("$6$",(B+C)/2,E);
label("$2$",(Q+B)/2,S);label("$4\sqrt2$",(C+Q)/2+(0,-0.6),W);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);'''
b.add(1726281,4,r'''A circle is inscribed in an isosceles trapezoid whose bases have lengths $4$ and $8$. What is the diameter of the circle?''',
r'''A quadrilateral with an inscribed circle has equal sums of opposite sides (equal tangent segments). So the two legs together equal $4+8=12$, and each leg is $6$.

Drop a perpendicular from an end of the short base to the long base. It cuts off a segment of length $\dfrac{8-4}{2}=2$, so the height is $\sqrt{6^2-2^2}=\sqrt{32}=4\sqrt2$.
'''+asy(fig4,'5cm')+r'''
The circle touches both bases, which are parallel, so its diameter equals the distance between them, the height. The diameter is $\boxed{4\sqrt2}$.''',
'Trapezoids|Incircles and incentres|Tangents|Pythagorean theorem|Isosceles triangles',3,
note='Problem 4 of the post.')

# ---------------- 1725452 square in equilateral triangle
fig=r'''real a=10,s=20*sqrt(3)-30;
pair A=(0,0),B=(a,0),C=(a/2,a*sqrt(3)/2);
pair P=((a-s)/2,0),Q=((a+s)/2,0),R=((a+s)/2,s),T=((a-s)/2,s);
draw(A--B--C--cycle,linewidth(0.9));
fill(P--Q--R--T--cycle,lightgray);draw(P--Q--R--T--cycle,blue+linewidth(0.9));
label("$s$",(Q+R)/2,W);label("$s$",(T+R)/2,S);
label("$x$",(A+P)/2,S);label("$x$",(Q+B)/2,S);
draw(arc(B,0.9,120,180));label("$60^\circ$",B+1.6*dir(150),fontsize(8pt));
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,N);
label("$P$",P,S);label("$Q$",Q,S);label("$R$",R,NE);label("$T$",T,NW);'''
b.add(1725452,1,r'''An equilateral triangle has area $25\sqrt3\text{ cm}^2$. A square is inscribed in the triangle with one side on a side of the triangle and the other two vertices on the other two sides. Find the area of the square.''',
r'''From $\dfrac{\sqrt3}{4}a^2=25\sqrt3$ the side of the triangle is $a=10$.

Let the square $PQRT$ have side $s$, with $P,Q$ on $AB$, $R$ on $BC$ and $T$ on $AC$. By symmetry $AP=QB=x$ with $2x+s=10$. In the right triangle $QBR$, the angle at $B$ is $60^\circ$ and $QR=s$, so $s=x\tan60^\circ=x\sqrt3$.
'''+asy(fig,'5.5cm')+r'''
Then $2x+x\sqrt3=10$, so $x=\dfrac{10}{2+\sqrt3}=10(2-\sqrt3)$ and
\[
s=10\sqrt3(2-\sqrt3)=20\sqrt3-30\approx4.64 .
\]
The area is
\[
s^2=(20\sqrt3-30)^2=1200-1200\sqrt3+900=\boxed{2100-1200\sqrt3}\ \text{cm}^2\approx21.5\text{ cm}^2 .
\]''',
'Equilateral triangles|Squares|Special right triangles|Lengths, perimeter, and area|Radicals',3,
note='The post asks for the maximum area of a square inscribed in the triangle. The record asks for the square with a side on a side of the triangle, which is the configuration meant (it is the largest square that fits, a known fact not proved here).')

# ---------------- 1723237 MATHCOUNTS handbook stretch #1-#4
fig=r'''import graph;
pair D=(-5,-3),Fp=(5,4),D2=(12,-6);
draw((-7,0)--(14,0),gray,Arrow(5));draw((0,-8)--(0,7),gray,Arrow(5));
draw(Fp--D,blue+dashed);draw(Fp--D2,red+dashed);
pair u=unit(D-Fp),v=unit(D2-Fp);
draw(Fp+0.8*u--Fp+0.8*u+0.8*v--Fp+0.8*v,linewidth(0.5));
draw(arc(Fp,3.2,degrees(D-Fp),degrees(D2-Fp)+360),Arrow(5));
dot(D);dot(Fp);dot(D2);
label("$D(-5,-3)$",D,W);label("$F(5,4)$",Fp,N);label("$D'(12,-6)$",D2,E);
label("$x$",(14,0),S);label("$y$",(0,7),W);'''
b.add(1723237,1,r'''What are the coordinates of the image of the point $D(-5,-3)$ when it is rotated $90^\circ$ counterclockwise about the point $F(5,4)$? (Rotating about $F$ means that $F$ stays fixed and every point turns around $F$, keeping its distance from $F$.)''',
r'''A rotation about $F$ turns the vector from $F$ to the point. Here $\overrightarrow{FD}=(-5-5,\,-3-4)=(-10,-7)$. A $90^\circ$ counterclockwise rotation sends a vector $(p,q)$ to $(-q,p)$, so the new vector is $(7,-10)$, and the image is
\[
D'=F+(7,-10)=(5+7,\,4-10)=\boxed{(12,-6)} .
\]
'''+asy(fig,'7.5cm')+r'''
Check: $FD'=\sqrt{49+100}=\sqrt{149}=FD$, and $\overrightarrow{FD}\cdot\overrightarrow{FD'}=-70+70=0$, so the angle $DFD'$ is a right angle; going from $FD$ to $FD'$ is counterclockwise, as the arrow shows.''',
'Rotations|Coordinate geometry|Geometric transformations',2,source=src('MATHCOUNTS Handbook',2019,None,1,rnd='Transformations and Measurement Stretch'),
note='The poster also asks what rotating "about the point F" means; the question now explains it.')
fig=r'''pair R=(-5,3),R1=(5,-7),R2=(-7,-5),O=(0,0);
draw((-9,0)--(8,0),gray,Arrow(5));draw((0,-9)--(0,6),gray,Arrow(5));
draw((-4,-6)--(7,5),linewidth(0.8));label("$y=x-2$",(7,5),E);
draw(R--R1,dashed);draw(O--R1,dotted+linewidth(0.8));draw(O--R2,dotted+linewidth(0.8));
draw(R--R2,red+linewidth(0.9));
dot(R);dot(R1);dot(R2);dot(O);
label("$R(-5,3)$",R,W);label("$R'(5,-7)$",R1,E);label("$R''(-7,-5)$",R2,W);label("$O$",O,NE);
label("$2\sqrt{17}$",(R+R2)/2,W,red);'''
b.add(1723237,2,r'''The point $R(-5,3)$ is reflected across the line $y=x-2$, and then its image $R'$ is rotated $90^\circ$ clockwise about the origin to give $R''$. What is the distance from $R$ to $R''$? Express your answer in simplest radical form.''',
r'''\textbf{Reflection.} The reflection of $(p,q)$ across $y=x-2$ is $(q+2,\,p-2)$: the midpoint $\left(\dfrac{p+q+2}{2},\dfrac{p+q-2}{2}\right)$ lies on the line, and the segment joining the point to its image has direction $(q+2-p,\,p-2-q)$, which is perpendicular to the line's direction $(1,1)$. So $R'=(3+2,\,-5-2)=(5,-7)$.

\textbf{Rotation.} A $90^\circ$ clockwise rotation about the origin sends $(p,q)$ to $(q,-p)$, so $R''=(-7,-5)$.
'''+asy(fig,'7cm')+r'''
\textbf{Distance.} $RR''=\sqrt{(-7+5)^2+(-5-3)^2}=\sqrt{4+64}=\sqrt{68}=\boxed{2\sqrt{17}}$.''',
'Reflections|Rotations|Coordinate geometry|Distance formula',3,source=src('MATHCOUNTS Handbook',2019,None,2,rnd='Transformations and Measurement Stretch'))
b.add(1723237,3,r'''If the reading of a measuring stick can be off by at most $1$ cm, what is the maximum percent error when a length of $24$ cm is measured? Express your answer to the nearest tenth.''',
r'''The percent error is $\dfrac{\text{error}}{\text{true value}}\times100\%$. The largest possible error is $1$ cm on a length of $24$ cm, so the maximum percent error is
\[
\dfrac{1}{24}\times100\%=4.1\overline{6}\,\%\approx\boxed{4.2\%}.
\]''',
'Percentages|Fractions',1,source=src('MATHCOUNTS Handbook',2019,None,3,rnd='Transformations and Measurement Stretch'))
b.add(1723237,4,r'''Vijay gives Sanjay a set of four weights of $1$, $3$, $8$ and $26$ grams. Sanjay may place weights on either pan of a balance. What is the smallest positive integer number of grams that he cannot measure with this set?''',
r'''An object of $w$ grams can be measured when $w$ is a signed sum $\pm1\pm3\pm8\pm26$ in which each weight may also be left out (weights on the object's pan count negatively).

\textbf{$1$ to $12$ can be measured:}
\[
1,\ 2=3-1,\ 3,\ 4=3+1,\ 5=8-3,\ 6=8+1-3,\ 7=8-1,\ 8,\ 9=8+1,\ 10=8+3-1,\ 11=8+3,\ 12=8+3+1 .
\]
\textbf{$13$ cannot.} Without the $26$-gram weight the largest amount is $1+3+8=12$. If the $26$-gram weight is used on the pan opposite the object, the object weighs at least $26-(1+3+8)=14$ grams. If it is on the object's pan, the other pan must hold more than $26$ grams, but the other weights total only $12$. So $13$ is impossible, and the answer is $\boxed{13}$.''',
'Systematic counting|Logical deduction|Bounding and extremal cases',3,source=src('MATHCOUNTS Handbook',2019,None,4,rnd='Transformations and Measurement Stretch'))

# ---------------- 1725457 common root
b.add(1725457,1,r'''Find all real numbers $a$ for which the equations $x^3+ax+1=0$ and $x^{2018}+ax+1=0$ have a common root (real or complex).''',
r'''Let $r$ be a common root. Subtracting the equations gives $r^{2018}=r^3$, so $r^3\left(r^{2015}-1\right)=0$. Now $r=0$ is not a root (it gives $1=0$), so $r^{2015}=1$ and in particular $|r|=1$; write $r=\cos\theta+i\sin\theta$.

From the first equation $a=-\dfrac{r^3+1}{r}=-\left(r^2+\dfrac1r\right)=-\left(r^2+\bar r\right)$. Its imaginary part is $-(\sin2\theta-\sin\theta)=-\sin\theta(2\cos\theta-1)$, so $a$ real forces $\sin\theta=0$ or $\cos\theta=\dfrac12$, i.e.\ $r=\pm1$ or $r=\cos60^\circ\pm i\sin60^\circ$.
\begin{itemize}
\item $r=-1$: $(-1)^{2015}=-1\ne1$.
\item $r=\cos60^\circ\pm i\sin60^\circ$: $r^{2015}=1$ would need $6\mid2015$, false.
\item $r=1$: then $1+a+1=0$, so $a=-2$, and indeed $x=1$ is a root of both $x^3-2x+1$ and $x^{2018}-2x+1$.
\end{itemize}
So the only value is $\boxed{a=-2}$ (with common root $x=1$).''',
'Polynomial roots|Roots of unity|Complex numbers',5,
note='The post does not say whether the common root may be complex; the record allows complex roots with a real, and the answer a = -2 is the same as for a real common root.')

# ---------------- 1724568 average speed
b.add(1724568,1,r'''Bob runs for $20$ minutes at $5.4$ miles per hour and then for $30$ minutes at $4.6$ miles per hour. What is Bob's average speed for the $50$ minutes he ran? Is it $5$ miles per hour?''',
r'''Average speed is total distance divided by total time. In $20$ minutes $=\dfrac13$ hour Bob runs $5.4\cdot\dfrac13=1.8$ miles, and in $30$ minutes $=\dfrac12$ hour he runs $4.6\cdot\dfrac12=2.3$ miles. The total is $4.1$ miles in $\dfrac56$ hour, so the average speed is
\[
\dfrac{4.1}{\dfrac56}=\dfrac{24.6}{5}=\boxed{4.92\text{ miles per hour}} .
\]
It is not $5$ miles per hour: $5$ is the plain average of $5.4$ and $4.6$, which would be correct only if Bob ran for equal times at the two speeds. He spends more time at the slower speed, so the time-weighted average $\dfrac{20\cdot5.4+30\cdot4.6}{50}=4.92$ is lower.''',
'Distance, rate, and time|Averages and weighted averages',2,
note='The poster suspected 5 mph was wrong; the correct average is 4.92 mph.')

# ---------------- 1725609 888 consecutive integers
b.add(1725609,1,r'''The sum of $888$ consecutive positive integers $n+(n+1)+\cdots+(n+887)$ is a perfect square. Find the smallest possible value of $n$.''',
r'''The sum is $888n+(0+1+\cdots+887)=888n+\dfrac{887\cdot888}{2}=444(2n+887)$. Since $444=2^2\cdot3\cdot37$, the sum is a perfect square exactly when $111(2n+887)$ is a perfect square. As $111=3\cdot37$ is squarefree, this happens exactly when $2n+887=111k^2$ for a positive integer $k$, and then $k$ must be odd (the left side is odd).

We need $2n+887\ge2\cdot1+887=889$, so $111k^2\ge889$, $k^2\ge9$ (since $111\cdot1<889$), and the smallest odd $k$ is $3$: $2n+887=999$ gives $n=\boxed{56}$. Check: the sum is $444\cdot999=443556=666^2$.''',
'Perfect squares|Prime factorisation|Arithmetic sequences|Summation',4)

# ---------------- 1724520 85_b = 58_c
b.add(1724520,1,r'''If $85_b=58_c$ for positive integer bases $b$ and $c$, what is the smallest possible value of $b$?''',
r'''The digit $8$ must be smaller than each base, so $b\ge9$ and $c\ge9$. The equation says $8b+5=5c+8$, i.e.\ $8b-3=5c$. So $8b\equiv3\pmod5$, i.e.\ $3b\equiv3$, i.e.\ $b\equiv1\pmod5$. The smallest $b\ge9$ with $b\equiv1\pmod5$ is $b=11$, and then $5c=85$, $c=17\ge9$. Check: $85_{11}=93=58_{17}$. The answer is $\boxed{11}$.''',
'Digits and bases|Linear Diophantine equations|Remainders and congruences',3)

# ---------------- 1725821 triangle with random sides
fig=r'''real k=0.45;
pair O=(0,0);
path sq=(0,0)--(10,0)--(10,10)--(0,10)--cycle;
fill(scale(k)*((5,0)--(10,5)--(10,10)--(5,10)--(0,5)--cycle),lightgray);
draw(scale(k)*sq,linewidth(0.9));
draw(scale(k)*((5,0)--(10,5)),red+dashed);draw(scale(k)*((0,5)--(5,10)),red+dashed);draw(scale(k)*((5,0)--(0,5)),blue+dashed);
label("$x$",k*(7.5,0),S);label("$y$",k*(0,7.5),W);label("$0$",O,SW);
label("$5$",k*(5,0),S);label("$10$",k*(10,0),S);label("$5$",k*(0,5),W);label("$10$",k*(0,10),W);
label("$x+y=5$",k*(2.0,1.0),fontsize(8pt));label("$y-x=5$",k*(2.4,9.0),fontsize(8pt));label("$x-y=5$",k*(7.6,1.0),fontsize(8pt));'''
b.add(1725821,1,r'''One side of a triangle is $5$ cm long. Two real numbers are chosen independently and uniformly at random between $0$ and $10$. What is the probability that they can be the lengths, in cm, of the other two sides of the triangle?''',
r'''Let the numbers be $x$ and $y$, a uniform point of the square $0<x,y<10$ of area $100$. Sides $5,x,y$ form a triangle exactly when
\[
x+y>5,\qquad x+5>y,\qquad y+5>x ,
\]
that is, $x+y>5$ and $|x-y|<5$. The favourable region is the shaded hexagon.
'''+asy(fig,'5cm')+r'''
The strip $|x-y|<5$ is the square minus two corner triangles with legs $5$, so it has area $100-2\cdot\dfrac{25}{2}=75$. From it remove the triangle $x+y\le5$ (legs $5$, area $\dfrac{25}{2}$), which lies inside the strip. The favourable area is $75-12.5=62.5$, and the probability is $\dfrac{62.5}{100}=\boxed{\dfrac58}$.''',
'Geometric probability|Triangle inequality|Probability',3)

# ---------------- 1725653 2018 MATHCOUNTS National Target #2
b.add(1725653,1,r'''A list contains $20$ numbers. For each positive integer $n$ from $1$ to $20$, the $n$th number in the list is either $\dfrac12n$ or $2n$. If the mean of the numbers in the list is exactly $12$, and the product of the numbers is $P$, what is the greatest possible value of $\dfrac{P}{20!}$?''',
r'''Let $T$ be the set of $n$ for which the $n$th number is $2n$; for the others it is $\dfrac n2$. The sum must be $20\cdot12=240$:
\[
\sum_{n\in T}2n+\sum_{n\notin T}\dfrac n2=\dfrac12\cdot210+\dfrac32\sum_{n\in T}n=240\quad\Longrightarrow\quad\sum_{n\in T}n=90 .
\]
The product is $P=20!\cdot2^{|T|}\cdot\left(\dfrac12\right)^{20-|T|}$, so $\dfrac{P}{20!}=2^{2|T|-20}$, which is largest when $T$ has as many elements as possible.

Since $1+2+\cdots+13=91>90$, any $13$ distinct numbers from $1$ to $20$ add up to more than $90$, so $|T|\le12$. Twelve is possible: $T=\{1,2,\dots,10,15,20\}$ has sum $55+35=90$. So the greatest value is $2^{24-20}=\boxed{16}$.''',
'Averages and weighted averages|Bounding and extremal cases|Exponents|Summation',4,source=src('MATHCOUNTS',2018,'National',2,rnd='Target'),
note='The poster asks for a more elegant solution than replacing terms by trial; the record bounds the number of doubled terms directly. Answer 16 as given.')

# ---------------- 1725566 dice sum
b.add(1725566,1,r'''$n$ standard dice, labelled $d_1,d_2,\dots,d_n$, are rolled. For a positive integer $n$, let $P_n$ be the number of outcomes in which, for all integers $i$ with $1\le i\le n-1$, the number rolled on $d_i$ is greater than or equal to the number rolled on $d_{i+1}$. Let $k=\displaystyle\sum_{n=3}^{70}P_n$. Compute the sum of the three largest prime factors of $k+28$.

$\textbf{(A) }181\qquad\textbf{(B) }199\qquad\textbf{(C) }213\qquad\textbf{(D) }239\qquad\textbf{(E) }247$''',
r'''A non-increasing sequence of $n$ values from $\{1,\dots,6\}$ is determined by how many times each value occurs, so $P_n$ is the number of solutions of $c_1+\cdots+c_6=n$ in nonnegative integers: $P_n=\dbinom{n+5}{5}$ (stars and bars). This also holds for $n=0$ with $P_0=1$.

By the hockey-stick identity,
\[
\sum_{n=0}^{70}\dbinom{n+5}{5}=\dbinom{76}{6}.
\]
The terms $n=0,1,2$ are $1+6+21=28$, so $k=\dbinom{76}{6}-28$ and
\[
k+28=\dbinom{76}{6}=\dfrac{76\cdot75\cdot74\cdot73\cdot72\cdot71}{720}=2\cdot3\cdot5^2\cdot19\cdot37\cdot71\cdot73 .
\]
The three largest prime factors are $73,71,37$, with sum $\boxed{\textbf{(A) }181}$.''',
'Stars and bars|Combinatorial identities and binomial coefficients|Prime factorisation|Summation',4,
note='The post writes the sum as sum_{i=3}^{70} P_n; the index typo is corrected to n. Answer (A) 181 checked by computer.')

# ---------------- 1725606 Texas A&M problems
b.add(1725606,1,r'''Let $S=2013^0+2013^1+2013^2+\cdots+2013^{2013}$. Find the remainder when $S$ is divided by $7$.''',
r'''Since $2013=7\cdot287+4$, we have $2013\equiv4\pmod7$, and $4^3=64\equiv1\pmod7$. So the powers $2013^k$ are $\equiv1,4,2,1,4,2,\dots$, repeating every $3$ terms, and each block of three consecutive terms is $\equiv1+4+2=7\equiv0$.

$S$ has $2014$ terms ($k=0,\dots,2013$): the first $2013=3\cdot671$ terms form $671$ complete blocks with sum $\equiv0$, and the last term is $2013^{2013}\equiv4^{2013}=\left(4^3\right)^{671}\equiv1$. The remainder is $\boxed{1}$.''',
'Remainders and congruences|Modular exponentiation|Geometric sequences',3,source=src('Texas A&M Math Contest',None,None,1),
note='Problem 1 of the post; the exponents, lost in copying ("(2013)0+ (2013)1+..."), are restored.')
b.add(1725606,2,r'''In a random arrangement of the letters of BLUEMOUNTAINS, what is the probability that the vowels are in alphabetical order within the arrangement? Express your answer as a fraction in lowest terms.''',
r'''BLUEMOUNTAINS has $13$ letters, of which the vowels are U, E, O, U, A, I: six vowels with U repeated. In a random arrangement, the set of positions occupied by vowels and the order in which the vowels appear in those positions are independent, and every distinguishable order of the vowels A, E, I, O, U, U is equally likely. There are $\dfrac{6!}{2!}=360$ such orders, and exactly one of them, A, E, I, O, U, U, is alphabetical. The probability is $\boxed{\dfrac{1}{360}}$.''',
'Probability|Multiset permutations|Symmetry',3,source=src('Texas A&M Math Contest',None,None,2),
note='Problem 2 of the post. Y is not in the word, so there is no question about whether it is a vowel.')

# ---------------- 1725534 2018 MATHCOUNTS National Sprint #30
figq=r'''pair A=(0,0),D=(5,0),C=(4,0),B=(4,3),Ep=(9/5,-12/5);
draw(A--B--C--cycle,linewidth(0.9));draw(D--A--Ep--cycle,linewidth(0.9));
draw(C--C+(-0.3,0)--C+(-0.3,0.3)--C+(0,0.3),linewidth(0.5));
pair u=unit(A-Ep),v=unit(D-Ep);draw(Ep+0.3*u--Ep+0.3*u+0.3*v--Ep+0.3*v,linewidth(0.5));
label("$A$",A,W);label("$B$",B,N);label("$C$",C,SE);label("$D$",D,E);label("$E$",Ep,S);
label("$5$",(A+B)/2,NW);label("$3$",(B+C)/2,E);label("$4$",(A+C)/2,N);
label("$3$",(A+Ep)/2,SW);label("$4$",(D+Ep)/2,SE);'''
figs=r'''pair A=(0,0),D=(5,0),C=(4,0),B=(4,3),Ep=(9/5,-12/5);
pair M1=(2.5,0),M2=(2,1.5),M3=(2.9,-1.2);
fill(A--M1--M2--cycle,lightgray);
draw(A--B--C--cycle,linewidth(0.9));draw(D--A--Ep--cycle,linewidth(0.9));
draw(C--Ep,gray+dashed);
pair dirm=unit(M2-M1);
draw((M1-1.9*dirm)--(M1+2.6*dirm),red+linewidth(0.9));
dot(M1,red);dot(M2,red);dot(M3,red);
label("$A$",A,W);label("$B$",B,N);label("$C$",C,NE);label("$D$",D,E);label("$E$",Ep,S);
label("$P$",M1,NE);label("$M$",M2,W);label("$K$",M3,W);label("$m$",M1+2.6*dirm,E,red);'''
b.add(1725534,1,r'''Triangles $ABC$ and $DAE$ have $AB=DA=5$, $AC=DE=4$ and $BC=AE=3$. Point $C$ lies on segment $AD$, and $B$ and $E$ are on opposite sides of line $AD$, as shown.
'''+asy(figq,'5cm')+r'''
It is possible to move triangle $ABC$ onto triangle $DAE$ (with $A\to D$, $B\to A$, $C\to E$) by reflecting triangle $ABC$ across a line $m$ and then translating the image in a direction parallel to $m$. Line $m$ divides triangle $ABC$ into two regions. What is the ratio of the area of the smaller region to the area of the larger region? Express your answer as a common fraction.''',
r'''Both triangles are $3$-$4$-$5$ right triangles, with right angles at $C$ and $E$. Put $A=(0,0)$, $D=(5,0)$, $C=(4,0)$, $B=(4,3)$. Then $E$ satisfies $AE=3$, $DE=4$ and lies below $AD$: $E=\left(\dfrac95,-\dfrac{12}5\right)$.

\textbf{The axis.} A reflection in $m$ followed by a translation along $m$ (a glide reflection) moves every point $X$ to a point $X'$ such that the midpoint of $XX'$ lies on $m$: the reflection moves $X$ perpendicular to $m$ and the translation moves it along $m$, so the midpoint is the foot on $m$ shifted by half the translation. Hence $m$ passes through the midpoints of $AD$, $BA$ and $CE$:
\[
P=\left(\dfrac52,0\right),\qquad M=\left(2,\dfrac32\right),\qquad K=\left(\dfrac{29}{10},-\dfrac{6}{5}\right),
\]
which indeed are collinear, on the line $y=-3x+\dfrac{15}{2}$.
'''+asy(figs,'5.5cm')+r'''
\textbf{The regions.} Line $m$ meets $AC$ at $P$ and $AB$ at its midpoint $M$. The piece of triangle $ABC$ next to $A$ is triangle $APM$, with base $AP=\dfrac52$ on the $x$-axis and height $\dfrac32$, so its area is $\dfrac12\cdot\dfrac52\cdot\dfrac32=\dfrac{15}{8}$. Triangle $ABC$ has area $6$, so the other region has area $6-\dfrac{15}8=\dfrac{33}{8}$. The ratio is
\[
\dfrac{\dfrac{15}{8}}{\dfrac{33}{8}}=\boxed{\dfrac{5}{11}} .
\]
(Indeed, reflecting in $m$ sends $A,B,C$ to $\left(\dfrac92,\dfrac32\right)$, $\left(-\dfrac12,\dfrac32\right)$, $\left(\dfrac{13}{10},-\dfrac{9}{10}\right)$, and the translation by $\left(\dfrac12,-\dfrac32\right)$, which is parallel to $m$, then gives $D,A,E$.)''',
'Reflections|Translations|Geometric transformations|Area ratios|Coordinate geometry|Right triangles',5,source=src('MATHCOUNTS',2018,'National',30,rnd='Sprint'),
note='The figure was attached; the text determines it once E is on the side of AD opposite B (on the same side the map would preserve orientation and could not be a glide reflection). The answer 5/11 matches the given answer. Repeat of an earlier record (aliased).')

# ---------------- 1724620 square ZENG pentagon; LMNO and prism repeats
fig=r'''real r=(18-9*sqrt(2))/4,c=3-r;
pair Z=(0,0),Ep=(3,0),Nn=(3,3),G=(0,3),Y=(1.5,0),I=(0,1.5),O=(c,c),T=(0.75,0.75);
fill(Z--Y--I--cycle,mediumgray+opacity(0.4));
draw(G--I--Y--Ep--Nn--cycle,linewidth(0.9));draw(I--Z--Y,dashed);
draw(circle(O,r),blue+linewidth(0.8));dot(O);
draw(O--(3,c),dashed);draw(O--(c,3),dashed);draw(O--T,red+dashed);
label("$Z$",Z,SW);label("$E$",Ep,SE);label("$N$",Nn,NE);label("$G$",G,NW);label("$Y$",Y,S);label("$I$",I,W);label("$O$",O,NW);label("$T$",T,SW);
label("$r$",(O+(3,c))/2,N);label("$r$",(O+(c,3))/2,W);label("$r$",(O+T)/2,SE,red);'''
b.add(1724620,1,r'''Square $ZENG$ has perimeter $12$. Points $Y$ and $I$ are the midpoints of sides $ZE$ and $ZG$, respectively. Find the radius of the largest circle that can be drawn inside pentagon $GIYEN$.''',
r'''Place $Z=(0,0)$, $E=(3,0)$, $N=(3,3)$, $G=(0,3)$, so $Y=\left(\dfrac32,0\right)$, $I=\left(0,\dfrac32\right)$, and the pentagon is the square with the corner triangle $ZYI$ cut off by the line $x+y=\dfrac32$.

The inscribed circle of the square (centre $\left(\dfrac32,\dfrac32\right)$, radius $\dfrac32$) does not fit: its centre is only $\dfrac{3-\dfrac32}{\sqrt2}=\dfrac{3\sqrt2}{4}<\dfrac32$ from the cut. A largest circle must touch the cut $YI$ and the two far sides $EN$ ($x=3$) and $NG$ ($y=3$); by symmetry its centre is $O=(c,c)$ with radius $r=3-c$, and its distance to the line $x+y=\dfrac32$ is
\[
\dfrac{2c-\dfrac32}{\sqrt2}=r=3-c\quad\Longrightarrow\quad 2(3-r)-\dfrac32=\sqrt2\,r\quad\Longrightarrow\quad r=\dfrac{\dfrac92}{2+\sqrt2}=\dfrac{9(2-\sqrt2)}{4}.
\]
'''+asy(fig,'5cm')+r'''
This circle lies in the pentagon: its centre is $c=3-r\approx1.68$ from the sides $ZE$ and $ZG$, more than $r\approx1.32$, and it touches $YI$ at $T=\left(\dfrac34,\dfrac34\right)$, which lies between $Y$ and $I$. No larger circle fits: a circle inside the pentagon lies in the half-planes $x\le3$, $y\le3$, $x+y\ge\dfrac32$, which form a right isosceles triangle with legs $\dfrac92$ whose incircle is exactly this circle. The radius is $\boxed{\dfrac{18-9\sqrt2}{4}}$.''',
'Squares|Incircles and incentres|Tangents|Coordinate geometry|Midpoints',5,
note='First problem of the post (marked solved, no answer given). The question "how do you find the circumradius of a cyclic hexagon" has no data and is dropped. The two "other questions" (LMNO and the box) repeat problems 1 and 2 of topic 1726281 in this batch and are aliased to them (q03, q04).')
b.add(1724620,3,r'''Quadrilateral $LMNO$ is circumscribed about circle $P$. Given that $MN=13$ and $OL=17$, find the perimeter of the quadrilateral.''',
r'''Equal tangent segments give $LM+NO=MN+OL=30$, so the perimeter is $\boxed{60}$.''',
'Tangents|Quadrilaterals and polygons',2,note='Repeat of 1726281-q01 in this batch (aliased).')
b.add(1724620,4,r'''A rectangular box has total surface area $14$, and its longest interior diagonal has length $8$. Find the square of the sum of its length, width and height.''',
r'''$(\ell+w+h)^2=(\ell^2+w^2+h^2)+2(\ell w+wh+h\ell)=64+14=\boxed{78}$.''',
'Algebraic expressions and identities',3,note='Repeat of 1726281-q02 in this batch (aliased).')

# ---------------- 1725436 counting paths P1
b.add(1725436,1,r'''There are $9$ paths from $A$ to $C$ and $5$ paths from $C$ to $D$. How many ways are there to get from $A$ to $D$ by way of $C$?''',
r'''Each route from $A$ to $D$ through $C$ consists of a path from $A$ to $C$ ($9$ choices) followed by a path from $C$ to $D$ ($5$ choices), and every pair of choices gives a different route. By the multiplication principle there are $9\cdot5=\boxed{45}$ ways.''',
'Multiplication principle|Counting principles',1,
note='Problem 1 of a counting thread; "by way of C" is made explicit (no other paths from A to D are described).')

# ---------------- 1725061 median of numbers with digit sum 24
b.add(1725061,1,r'''Consider the set of all four-digit positive integers less than $2000$ whose digits have a sum of $24$. What is the median of this set of integers?''',
r'''Such a number is $\overline{1abc}$ with $a+b+c=23$ and each digit at most $9$. Then each digit is at least $23-18=5$. Listing by the hundreds digit $a$:
\begin{itemize}
\item $a=5$: $b=c=9$: $1599$.
\item $a=6$: $b+c=17$: $1689,1698$.
\item $a=7$: $b+c=16$: $1779,1788,1797$.
\item $a=8$: $b+c=15$: $1869,1878,1887,1896$.
\item $a=9$: $b+c=14$: $1959,1968,1977,1986,1995$.
\end{itemize}
There are $15$ numbers, already in increasing order, so the median is the $8$th: $\boxed{1878}$.''',
'Median|Digits and bases|Systematic counting',2,
note='Repeat of an earlier record (aliased).')

# ---------------- 1723304 minimum of sqrt(2x^2-3)+sqrt(3x+5)
b.add(1723304,1,r'''The minimum value of $y=\sqrt{2x^2-3}+\sqrt{3x+5}$ (over all real $x$ for which it is defined) can be written as $\sqrt{a-\dfrac{b\sqrt c}{d}}$, where $a,b,c,d$ are positive integers, $c$ is not divisible by the square of a prime, and $\dfrac bd$ is in lowest terms. Find $a+b+c+d$.''',
r'''\textbf{Domain.} We need $2x^2\ge3$ and $3x+5\ge0$, i.e.\ $x\ge-\dfrac53$ and $|x|\ge\sqrt{\dfrac32}$. So $x\ge\sqrt{\dfrac32}$ or $-\dfrac53\le x\le-\sqrt{\dfrac32}$.

\textbf{Right part.} For $x\ge\sqrt{\dfrac32}>1$, $y\ge\sqrt{3x+5}>\sqrt8>2$.

\textbf{Left part.} Put $u=-x$, so $\sqrt{\dfrac32}\le u\le\dfrac53$ and $y=\sqrt{2u^2-3}+\sqrt{5-3u}$ with both radicands nonnegative. Squaring,
\[
y^2=(2u^2-3)+(5-3u)+2\sqrt{(2u^2-3)(5-3u)}\ \ge\ 2u^2-3u+2 ,
\]
with equality when $2u^2=3$. The quadratic $g(u)=2u^2-3u+2$ is increasing for $u\ge\dfrac34$, so for $u\ge u_0=\sqrt{\dfrac32}$,
\[
y^2\ge g(u_0)=3-3u_0+2=5-3\sqrt{\dfrac32}=5-\dfrac{3\sqrt6}{2},
\]
with equality at $u=u_0$, i.e.\ $x=-\sqrt{\dfrac32}$, where $y=\sqrt{5-\dfrac{3\sqrt6}{2}}\approx1.151<2$.

So the minimum is $\sqrt{5-\dfrac{3\sqrt6}{2}}$, giving $a=5$, $b=3$, $c=6$, $d=2$ and $a+b+c+d=\boxed{16}$.''',
'Radicals|Maxima and minima|Inequalities|Quadratic equations',5,
note='"a, b, c, d are integers and the expression is in simplest form" is made precise. The minimum was confirmed numerically.')

# ---------------- 1725176 a*2^a=3
b.add(1725176,1,r'''Show that the equation $a\cdot2^a=3$ has exactly one real solution, and that this solution lies between $1$ and $\dfrac32$.''',
r'''Let $f(a)=a\cdot2^a$.
\begin{itemize}
\item If $a\le0$, then $f(a)\le0<3$, so there are no solutions with $a\le0$.
\item For $a>0$, both $a$ and $2^a$ are positive and increasing, so their product $f$ is increasing on $(0,\infty)$; hence $f(a)=3$ has at most one positive solution.
\end{itemize}
Also $f(1)=2<3$ and $f\left(\dfrac32\right)=\dfrac32\cdot2\sqrt2=3\sqrt2>3$. Since $f$ is continuous, the intermediate value theorem gives a solution between $1$ and $\dfrac32$, and it is the only real solution. $\blacksquare$

(The solution, $a\approx1.256$, cannot be written with elementary functions; it equals $\dfrac{W(3\ln2)}{\ln2}$, where $W$ is the Lambert $W$ function, and can be computed to any accuracy by bisection.)''',
'Exponents|Functions|Inequalities|Bounding and extremal cases',2,
note='The post asks how to "find" a with a 2^a = 3, which has no elementary closed form. The record asks to show there is exactly one solution and to locate it; the numerical value 1.256 is given.')

# ---------------- 1724972 impossible triangle
fig=r'''real c=15;pair A=(-7.5,0),B=(7.5,0);
real sa=16.5,sb=sqrt(16.5^2-7.5^2);
draw(xscale(sa)*yscale(sb)*unitcircle,gray+dashed);
pair Ct=(0,sb);
real a=18,bb=15;
real x=A.x+(bb^2-a^2+c^2)/(2*c);pair C=(x,sqrt(bb^2-(x-A.x)^2));
draw(A--B--C--cycle,linewidth(0.9));
draw(A--Ct--B,blue+dashed);
dot(Ct,blue);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,N);label("$C_0$",Ct,N,blue);
label("$c=15$",(A+B)/2,S);label("$b$",(A+C)/2,W);label("$a$",(B+C)/2,SW);
label("$a+b=33$",(13,-13.5),E,gray);'''
b.add(1724972,1,r'''A problem states: ``In triangle $ABC$, $AB=15$, the semiperimeter is $24$, and $\cos C=\dfrac{13}{27}$. Find the circumradius of triangle $ABC$.'' Prove that no triangle satisfies these conditions.''',
r'''Let $a=BC$, $b=CA$, $c=AB=15$. The semiperimeter is $24$, so $a+b=48-15=33$. By the law of cosines,
\[
c^2=a^2+b^2-2ab\cos C=(a+b)^2-2ab(1+\cos C),
\]
so $225=1089-2ab\cdot\dfrac{40}{27}$, which gives $ab=\dfrac{864\cdot27}{80}=\dfrac{1458}{5}=291.6$.

But for positive $a,b$ with $a+b=33$, AM-GM gives $ab\le\left(\dfrac{a+b}{2}\right)^2=\dfrac{1089}{4}=272.25<291.6$. This is a contradiction, so no such triangle exists. $\blacksquare$
'''+asy(fig,'6cm')+r'''
Equivalently, $\cos C=\dfrac{(a+b)^2-2ab-c^2}{2ab}=\dfrac{432}{ab}-1\ge\dfrac{432}{272.25}-1=\dfrac{71}{121}\approx0.587$, while $\dfrac{13}{27}\approx0.481$. Geometrically, $C$ lies on the ellipse with foci $A,B$ on which $a+b=33$ (dashed), and the angle $C$ is largest at the top point $C_0$, where $a=b=16.5$ and $\cos C=\dfrac{71}{121}$; the required angle is larger than that. (The formula $R=\dfrac{c}{2\sin C}=\dfrac{405}{8\sqrt{35}}$ would give a value, but it describes no triangle with semiperimeter $24$.)''',
'Law of cosines|Triangles|AM-GM inequality|Trigonometry|Ellipses',4,
note='The posted data are inconsistent: with a + b = 33 and c = 15, cos C is at least 71/121 = 0.587, so cos C = 13/27 is impossible. The record asks for a proof that no such triangle exists instead of the circumradius.')

# ---------------- 1724982 (s-c)/r = cot C + csc C
fig=r'''pair A=(0,0),B=(7,0),C=(2.4,6.2);
real a=abs(B-C),bb=abs(C-A),c=abs(A-B);
pair I=(a*A+bb*B+c*C)/(a+bb+c);
real r=I.y;
pair Pa=C+dot(I-C,unit(A-C))*unit(A-C),Pb=C+dot(I-C,unit(B-C))*unit(B-C);
draw(A--B--C--cycle,linewidth(0.9));
draw(circle(I,r),blue);dot(I);
draw(C--I,dashed);draw(I--Pa,red);draw(I--Pb,red);
void ra(pair P,pair Q,pair R){pair u=unit(Q-P)*0.25,v=unit(R-P)*0.25;draw(P+u--P+u+v--P+v,linewidth(0.5));}
ra(Pa,I,C);ra(Pb,I,C);
draw(arc(C,1.0,degrees(Pa-C),degrees(I-C)),linewidth(0.6));
label("$\dfrac C2$",C+1.6*dir((degrees(Pa-C)+degrees(I-C))/2),fontsize(8pt));
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,N);label("$I$",I,S);
label("$r$",(I+Pa)/2,N,red);label("$r$",(I+Pb)/2,S,red);
label("$s-c$",(C+Pa)/2,W);label("$s-c$",(C+Pb)/2,NE);'''
b.add(1724982,1,r'''In triangle $ABC$ let $a,b,c$ be the sides opposite $A,B,C$, let $s$ be the semiperimeter, $r$ the inradius and $R$ the circumradius.
\begin{enumerate}
\item[(a)] Show that the identity $\dfrac{s-c}{R}=\cot C+\csc C$ is false in general.
\item[(b)] Prove that $\dfrac{s-c}{r}=\cot C+\csc C$ for every triangle.
\end{enumerate}''',
r'''\textbf{(a)} Take an equilateral triangle with side $1$: $s-c=\dfrac12$ and $R=\dfrac{1}{\sqrt3}$, so $\dfrac{s-c}{R}=\dfrac{\sqrt3}{2}$, while $\cot60^\circ+\csc60^\circ=\dfrac1{\sqrt3}+\dfrac2{\sqrt3}=\sqrt3$. So the identity with $R$ fails.

\textbf{(b)} Let the incircle, with centre $I$, touch $CA$ and $CB$ at $P$ and $Q$. Tangent segments from a point are equal; writing $x,y,z$ for the tangent lengths from $A,B,C$, we have $y+z=a$, $z+x=b$, $x+y=c$, so $z=\dfrac{a+b-c}{2}=s-c$. Thus $CP=CQ=s-c$.
'''+asy(fig,'6.5cm')+r'''
The incentre lies on the bisector of angle $C$, so in the right triangle $CPI$ (right angle at $P$, since a radius is perpendicular to the tangent) we have $\angle PCI=\dfrac C2$ and
\[
\dfrac{s-c}{r}=\dfrac{CP}{IP}=\cot\dfrac C2 .
\]
Finally, using $\cos C=2\cos^2\dfrac C2-1$ and $\sin C=2\sin\dfrac C2\cos\dfrac C2$,
\[
\cot C+\csc C=\dfrac{1+\cos C}{\sin C}=\dfrac{2\cos^2\dfrac C2}{2\sin\dfrac C2\cos\dfrac C2}=\cot\dfrac C2 .
\]
Hence $\dfrac{s-c}{r}=\cot C+\csc C$. $\blacksquare$''',
'Incircles and incentres|Tangents|Trigonometric identities|Angle bisectors|Counterexamples|Trigonometry',4,
note='The post asks to prove (s - c)/R = cot c + csc c with R the circumradius; this is false (equilateral counterexample). With R replaced by the inradius r the identity is true, which was surely intended; the record asks for both. Checked numerically on random triangles.')

# ---------------- 1724486 three problems
b.add(1724486,1,r'''A rational function has the form
\[
f(x)=\dfrac{ax^2+bx+k}{dx+e},
\]
where $a,b,d,e$ are positive integers with greatest common divisor $1$ and $k$ is a real number. The only asymptotes of its graph are the lines $x=-4$ and $y=2x-2$. Find $a+b+d+e$.''',
r'''A vertical asymptote at $x=-4$ requires the denominator to vanish there, so $dx+e=d(x+4)$, i.e.\ $e=4d$. Long division gives
\[
\dfrac{ax^2+bx+k}{d(x+4)}=\dfrac ad x+\dfrac{b-4a}{d}+\dfrac{k-4b+16a}{d(x+4)} .
\]
The slant asymptote is $y=\dfrac adx+\dfrac{b-4a}{d}$, so $\dfrac ad=2$ and $\dfrac{b-4a}{d}=-2$, i.e.\ $a=2d$ and $b=4a-2d=6d$. Then $(a,b,d,e)=(2d,6d,d,4d)$, and the gcd condition forces $d=1$: $a=2$, $b=6$, $d=1$, $e=4$. (For $x=-4$ to be a genuine asymptote the remainder must be nonzero, $k\ne-8$; any such $k$ works.) Hence $a+b+d+e=\boxed{13}$.''',
'Polynomials|Functions|Algebraic manipulation',4,
note='Problem 1 of the post ("c and f can be varied but don\'t change the asymptotes") is restated: the constant term is written k and the coefficients a, b, d, e are required to have gcd 1, which makes the answer 13 unique.')
b.add(1724486,2,r'''The minimum value of $y=\sqrt{2x^2-3}+\sqrt{3x+5}$ can be written as $\sqrt{a-\dfrac{b\sqrt c}{d}}$ with $a,b,c,d$ positive integers in simplest form. Find $a+b+c+d$.''',
r'''The minimum is attained at $x=-\sqrt{\dfrac32}$ and equals $\sqrt{5-\dfrac{3\sqrt6}{2}}$, so the answer is $\boxed{16}$.''',
'Radicals|Maxima and minima',5,note='Repeat of 1723304-q01 in this batch (aliased).')
fig=r'''real sc=1;
pair B=(-5.5,0),C=(5.5,0),A=(0,1),Ep=(-0.5,0),D=(0.5,0);
draw(A--B--C--cycle,linewidth(0.9));draw(A--Ep,linewidth(0.8));draw(A--D,linewidth(0.8));
dot(Ep);dot(D);
label("$A$",A,N);label("$B$",B,W);label("$C$",C,E);label("$E$",Ep,SW);label("$D$",D,SE);
label("$5$",(D+C)/2,S);label("$5$",(B+Ep)/2,S);label("$1$",(Ep+D)/2,2*S);'''
b.add(1724486,3,r'''In isosceles triangle $ABC$, $AB=AC$. Points $D$ and $E$ lie on side $BC$ so that $AD$ and $AE$ trisect $\angle BAC$, with $D$ closer to $C$. If $CD=5$ and $DE=1$, find $AC$.''',
r'''\textbf{Symmetry.} The reflection in the altitude from $A$ swaps $B$ and $C$ and maps the two trisectors of $\angle A$ to each other, so it swaps $D$ and $E$. Hence $BE=CD=5$ and $AE=AD$; call this length $x$. The points lie in the order $B,E,D,C$ with $EC=6$.

\textbf{Triangle $AEC$.} Since $\angle EAD=\angle DAC$, segment $AD$ bisects $\angle EAC$. By the angle bisector theorem,
\[
\dfrac{ED}{DC}=\dfrac{AE}{AC}\quad\Longrightarrow\quad AC=5x .
\]
By Stewart's theorem for the cevian $AD$ in triangle $AEC$ (with $ED=1$, $DC=5$, $EC=6$):
\[
AE^2\cdot DC+AC^2\cdot ED=EC\left(AD^2+ED\cdot DC\right)\ \Longrightarrow\ 5x^2+25x^2=6(x^2+5)\ \Longrightarrow\ x^2=\dfrac54 .
\]
So $x=\dfrac{\sqrt5}{2}$ and $AC=5x=\boxed{\dfrac{5\sqrt5}{2}}$.
'''+asy(fig,'8cm')+r'''
The triangle is very flat (drawn to scale): with $BC=11$ and $AC=\dfrac{5\sqrt5}2$, the height is $\sqrt{\dfrac{125}{4}-\dfrac{121}{4}}=1$, and the three angles at $A$ are each about $53.1^\circ$.''',
'Isosceles triangles|Angle bisector theorem|Stewart\'s theorem|Symmetry',5,
note='Problem 3 of the post also gives AE = 9, which contradicts CD = 5 and DE = 1: the angle bisector theorem in triangle AEC would give AC = 45 > AE + EC = 15. In fact CD and DE alone force AE = sqrt(5)/2. The record drops AE = 9 and asks for AC = 5 sqrt(5)/2.')

b.save()
