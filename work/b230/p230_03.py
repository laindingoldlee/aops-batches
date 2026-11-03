from qb import *
b=Bank('p230_03')

# ---------------- 1734443 sixteen geometry problems from a local contest
fig=r'''pair C=(0,0),B=(12,0),A=(0,8),M=(6,0),K=(0,4);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--M,blue+dashed);draw(B--K,blue+dashed);
draw((0,0.7)--(0.7,0.7)--(0.7,0));
draw((3,-0.25)--(3,0.25));draw((9,-0.25)--(9,0.25));
draw((-0.25,2)--(0.25,2));draw((-0.25,6)--(0.25,6));
label("$A$",A,N);label("$B$",B,E);label("$C$",C,SW);label("$M$",M,S);label("$K$",K,W);
label("$10$",(3.9,4.6),blue);label("$4\sqrt{10}$",(7.6,0.55),blue+fontsize(9pt));'''
b.add(1734443,1,r'''The medians to the legs of a right triangle have lengths $10$ and $4\sqrt{10}$. Find the length of the hypotenuse.''',
r'''Let the right angle be at $C$, with legs $CB=a$ and $CA=b$, and let $M$ and $K$ be the midpoints of $CB$ and $CA$:
'''+asy(fig,'6.5cm')+r'''
By Pythagoras in the right triangles $ACM$ and $BCK$,
\[
AM^2=b^2+\dfrac{a^2}{4}=100,\qquad BK^2=a^2+\dfrac{b^2}{4}=160 .
\]
Adding, $\dfrac54(a^2+b^2)=260$, so $AB^2=a^2+b^2=208$ and $AB=\sqrt{208}=\boxed{4\sqrt{13}}$. (The legs are $a=12$ and $b=8$.)''',
'Right triangles|Pythagorean theorem|Medians and centroids|Midpoints',3,
note='First of sixteen problems from a local contest (q01-q16 in the order of the post).')
fig=r'''pair C=(0,0),B=(60,0),A=(0,11);
draw(A--B--C--cycle,linewidth(0.9));draw((0,2.2)--(2.2,2.2)--(2.2,0));
label("$5x=60$",(30,0),S);label("$x-1=11$",(0,5.5),W);label("$4x+13=61$",(30,5.5),NE);'''
b.add(1734443,2,r'''The sides of a right triangle measure $5x$, $4x+13$ and $x-1$. If $x$ is an integer, find the sum of the digits of $x$.''',
r'''We need $x>1$. The hypotenuse is the longest side, and $x-1<5x$ and $x-1<4x+13$, so it is $5x$ or $4x+13$.

If the hypotenuse is $5x$: $25x^2=(4x+13)^2+(x-1)^2$ gives $8x^2-102x-170=0$, i.e.\ $4x^2-51x-85=0$, whose discriminant $51^2+4\cdot4\cdot85=3961$ is not a perfect square ($62^2<3961<63^2$), so there is no integer root.

If the hypotenuse is $4x+13$: $(4x+13)^2=25x^2+(x-1)^2$ gives $10x^2-106x-168=0$, i.e.\ $5x^2-53x-84=0=(x-12)(5x+7)$. So $x=12$, and the sides are $60$, $61$, $11$; indeed $11^2+60^2=121+3600=3721=61^2$:
'''+asy(fig,'7cm')+r'''
The sum of the digits of $x=12$ is $\boxed{3}$.''',
'Right triangles|Pythagorean theorem|Quadratic equations|Pythagorean triples',3)
fig=r'''pair B=(0,0),C=(16,0),A=(4,3),H=(4,0),D=(11,0);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--H,dashed);draw(A--D,blue);
draw((4,0)--(4.5,0)--(4.5,0.5)--(4,0.5));
dot(D,blue);
label("$A$",A,N);label("$B$",B,W);label("$C$",C,E);label("$H$",H,S);label("$D$",D,S,blue);
label("$5$",(A+B)/2,NW);label("$\sqrt{153}$",(A+C)/2,NE);label("$3$",(4,1.5),W);'''
b.add(1734443,3,r'''In triangle $ABC$, $AB=5$, $BC=16$, $AC=\sqrt{153}$, and $D$ is a point on segment $BC$. Compute the sum of all possible integer values of $AD$.''',
r'''By the law of cosines, $\cos B=\dfrac{25+256-153}{2\cdot5\cdot16}=\dfrac{128}{160}=\dfrac45$, so the foot $H$ of the altitude from $A$ satisfies $BH=4$, and $AH=3$; then $HC=12$ and indeed $AC^2=3^2+12^2=153$:
'''+asy(fig,'6cm')+r'''
As $D$ moves along $BC$, $AD=\sqrt{9+HD^2}$ takes every value from its minimum $AH=3$ (at $D=H$) up to its maximum $AC=\sqrt{153}\approx12.37$ (at $D=C$), continuously. So the possible integer values are $3,4,\dots,12$, with sum $\dfrac{(3+12)\cdot10}{2}=\boxed{75}$.''',
'Triangles|Pythagorean theorem|Law of cosines|Altitudes|Bounding and extremal cases',3,
note='"Sum of all possible integral values" is read as the sum of the distinct integer lengths AD can take.')
fig=r'''pair B=(0,0),A=(sqrt(6),0),C=(0,sqrt(2)),D=(sqrt(2),sqrt(2)+sqrt(6)),H=(sqrt(2),0);
draw(A--B--C--cycle,linewidth(0.9));draw(A--C--D--cycle,linewidth(0.9));
draw(D--H,blue+dashed);
draw((0,0.2)--(0.2,0.2)--(0.2,0));draw(H+(0,0.2)--H+(-0.2,0.2)--H+(-0.2,0));
pair u=unit(A-C),w=unit(D-C);draw(C+0.2*u--C+0.2*u+0.2*w--C+0.2*w);
label("$A$",A,SE);label("$B$",B,SW);label("$C$",C,W);label("$D$",D,N);label("$H$",H,S);
label("$\sqrt{2}$",(B+C)/2,W);
draw(arc(A,0.45,degrees(C-A),180));label("$30^\circ$",A+0.75*dir(165),fontsize(7pt));
draw(arc(A,0.7,degrees(D-A),degrees(C-A)));label("$45^\circ$",A+1.0*dir(127.5),fontsize(7pt));'''
b.add(1734443,4,r'''Right triangle $ABC$ has hypotenuse $AC$, $\angle CAB=30^\circ$ and $BC=\sqrt2$. Right triangle $ACD$ has hypotenuse $AD$ and $\angle DAC=45^\circ$. The interiors of triangles $ABC$ and $ACD$ do not overlap. Find the length of the perpendicular from $D$ to line $AB$.''',
r'''In triangle $ABC$ (right angle at $B$), $AC=\dfrac{BC}{\sin30^\circ}=2\sqrt2$. Triangle $ACD$ has its right angle at $C$ and $\angle DAC=45^\circ$, so it is isosceles with $CD=AC=2\sqrt2$ and $AD=AC\sqrt2=4$. Since the triangles lie on opposite sides of $AC$, $\angle DAB=\angle DAC+\angle CAB=75^\circ$:
'''+asy(fig,'5cm')+r'''
The perpendicular from $D$ to line $AB$ has length
\[
DH=AD\sin75^\circ=4\cdot\dfrac{\sqrt6+\sqrt2}{4}=\boxed{\sqrt6+\sqrt2}.
\]
(Coordinates confirm it: with $B=(0,0)$, $A=(\sqrt6,0)$, $C=(0,\sqrt2)$ one finds $D=(\sqrt2,\sqrt2+\sqrt6)$.)''',
'Special right triangles|Right triangles|Trigonometry|Angle chasing',3)
fig=r'''pair O=(0,0),A=(26,0); real r=5,R=13;
pair n1=(-8/26,sqrt(612)/26), n2=(18/26,-sqrt(352)/26);
pair T1=O+r*n1,T2=A+R*n1,U1=O+r*n2,U2=A-R*n2;
draw(circle(O,r),linewidth(0.8));draw(circle(A,R),linewidth(0.8));
draw(O--A,dashed);
draw(T1--T2,blue+linewidth(0.9));draw(U1--U2,red+linewidth(0.9));
draw(O--T1,gray(0.5));draw(A--T2,gray(0.5));draw(O--U1,gray(0.5));draw(A--U2,gray(0.5));
dot(O);dot(A);
label("$O$",O,W);label("$A$",A,E);label("$26$",(19,0),S);
label("$6\sqrt{17}$",(T1+T2)/2,dir(100),blue);label("$4\sqrt{22}$",(6.6,-3.2),red);'''
b.add(1734443,5,r'''A circle with centre $O$ has radius $5$, and a circle with centre $A$ has radius $13$, with $OA=26$. Find the sum of the lengths of one common external tangent segment and one common internal tangent segment of the two circles (each segment running between its two points of tangency).''',
r'''For a common tangent segment $T_1T_2$, the radii $OT_1$ and $AT_2$ are both perpendicular to it:
'''+asy(fig,'7cm')+r'''
For an external tangent the radii point to the same side, and sliding $T_1T_2$ along the radii gives a right triangle with hypotenuse $OA=26$, one leg $13-5=8$ and the other leg equal to the tangent length:
\[
\sqrt{26^2-8^2}=\sqrt{612}=6\sqrt{17}.
\]
For an internal tangent the radii point to opposite sides, and the leg is $13+5=18$:
\[
\sqrt{26^2-18^2}=\sqrt{352}=4\sqrt{22}.
\]
The sum is $\boxed{6\sqrt{17}+4\sqrt{22}}$.''',
'Tangents|Circles|Pythagorean theorem|Right triangles',3,
note='"The lengths of one common external and one common internal tangent" is read as the lengths of the tangent segments between the points of tangency.')
fig=r'''pair A=(0,0),C=(82,0),X=(41,0),B=(6400/82,1440/82),D=(6400/82,0);
draw(circle(X,41),gray(0.6));
draw(A--B--C--cycle,linewidth(0.9));draw(B--D,blue+dashed);
draw(D+(0,1.8)--D+(-1.8,1.8)--D+(-1.8,0),blue);
dot(X);
label("$A$",A,W);label("$B$",B,N);label("$C$",C,E);label("$X$",X,S);label("$D$",D,S);
label("$80$",(A+B)/2,N);label("$18$",(B+C)/2,dir(10));'''
b.add(1734443,6,r'''Triangle $ABC$ is inscribed in a circle with centre $X$, where $\angle ABC=90^\circ$, $BC=18$ and $AB=80$. The altitude from $B$ meets $AC$ at $D$. What is the distance between $X$ and $D$?''',
r'''Since $\angle ABC=90^\circ$, $AC$ is a diameter and $X$ is its midpoint. Here $AC=\sqrt{80^2+18^2}=\sqrt{6724}=82$, so $AX=41$:
'''+asy(fig,'6.5cm')+r'''
In a right triangle the altitude to the hypotenuse gives $AB^2=AD\cdot AC$ (similar triangles $ABD$ and $ACB$), so $AD=\dfrac{6400}{82}=\dfrac{3200}{41}$. Then
\[
XD=AD-AX=\dfrac{3200}{41}-41=\dfrac{3200-1681}{41}=\boxed{\dfrac{1519}{41}}.
\]''',
'Right triangles|Circumcircles and circumcentres|Similarity|Altitudes',3)
fig=r'''pair B=(0,0),C=(8,0),A=7*dir(60);
draw(A--B--C--cycle,linewidth(0.9));
draw(arc(B,1,0,60));label("$60^\circ$",B+1.6*dir(30),fontsize(9pt));
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$7$",(A+B)/2,NW);label("$8$",(B+C)/2,S);label("$\sqrt{57}$",(A+C)/2,NE);'''
b.add(1734443,7,r'''In triangle $ABC$, $AB=7$, $BC=8$ and $\angle ABC=60^\circ$. What is the length of $AC$?''',
r'''By the law of cosines,
\[
AC^2=7^2+8^2-2\cdot7\cdot8\cos60^\circ=49+64-56=57,
\]
so $AC=\boxed{\sqrt{57}}$.
'''+asy(fig,'4.5cm'),
'Law of cosines|Triangles',2)
fig=r'''real s=10; real ap=(s/2)/Tan(36); pair O=(0,0);
pair[] P; for(int i=0;i<5;++i) P.push((s/(2*Sin(36)))*dir(270-36+72*i));
draw(P[0]--P[1]--P[2]--P[3]--P[4]--cycle,linewidth(0.9));
pair M=(P[0]+P[1])/2;
draw(O--M,blue+dashed);draw(O--P[0],gray(0.5));draw(O--P[1],gray(0.5));
dot(O);label("$O$",O,N);
label("$10$",M,S);label("$a$",(O+M)/2,E,blue);
label("$36^\circ$",O+2.4*dir(252),fontsize(8pt));draw(arc(O,1.4,234,270));'''
b.add(1734443,8,r'''Find the total surface area of a regular dodecahedron with edge length $10$.''',
r'''A regular dodecahedron has $12$ faces, each a regular pentagon with side $10$. Split a face into $5$ isosceles triangles from its centre $O$; each has apex angle $72^\circ$, base $10$ and height equal to the apothem $a$:
'''+asy(fig,'4.5cm')+r'''
Since half of the apex angle is $36^\circ$, $a=\dfrac{5}{\tan36^\circ}$, and the face area is $5\cdot\dfrac12\cdot10\cdot a=\dfrac{125}{\tan36^\circ}$. Using $\tan36^\circ=\sqrt{5-2\sqrt5}$, this equals $25\sqrt{25+10\sqrt5}$, since $\dfrac{125}{\sqrt{5-2\sqrt5}}=\dfrac{125\sqrt{5+2\sqrt5}}{\sqrt{25-20}}=25\sqrt5\sqrt{5+2\sqrt5}$. So the surface area is
\[
12\cdot25\sqrt{25+10\sqrt5}=\boxed{300\sqrt{25+10\sqrt5}}\approx2064.7 .
\]''',
'Polyhedra|Regular polygons|Surface area|Trigonometry',4)
fig=r'''pair P=(3,4),C=(21,10); real r=6; pair Q=C+r*unit(P-C);
draw(circle(C,r),linewidth(0.9));
draw(C--Q,dashed);draw(P--Q,blue+linewidth(1));
dot(P);dot(C);dot(Q,blue);
label("$P(3,4)$",P,W);label("$C$",C,E);label("$Q$",Q,dir(250));label("$6$",(C+Q)/2,N);'''
b.add(1734443,9,r'''What is the shortest distance from the point $(3,4)$ to the circle $x^2+y^2-42x-20y=-505$?''',
r'''Completing the squares, $(x-21)^2+(y-10)^2=441+100-505=36$: a circle with centre $C=(21,10)$ and radius $6$. The point $P=(3,4)$ is at distance $\sqrt{18^2+6^2}=\sqrt{360}=6\sqrt{10}>6$ from $C$, so it is outside, and the nearest point $Q$ of the circle lies on segment $PC$:
'''+asy(fig,'6cm')+r'''
The shortest distance is $PC-6=\boxed{6\sqrt{10}-6}\approx12.97$.''',
'Circles|Distance formula|Completing the square|Coordinate geometry',3)
fig=r'''real s=3*sqrt(2),h=2*sqrt(3);
pair pr(real x,real y,real z){return (x+0.6*y,0.3*y+z);}
pair P1=pr(0,0,0),P2=pr(s,0,0),P3=pr(s/2,s*sqrt(3)/2,0),G=pr(s/2,s*sqrt(3)/6,h),O=pr(s/2,s*sqrt(3)/6,0);
draw(P1--P3,dashed);draw(P1--P2--P3,linewidth(0.9));draw(P1--G--P2,linewidth(0.9));draw(P3--G,linewidth(0.9));
draw(G--O,blue+dashed);dot(O,blue);
label("$h$",(G+O)/2,E,blue);label("$s$",(P1+P2)/2,S);'''
b.add(1734443,10,r'''What is the volume of a regular tetrahedron with height $2\sqrt3$?''',
r'''Let the edge be $s$. The foot of the height is the centre of the base triangle, at distance $\dfrac{s}{\sqrt3}$ from each base vertex, so by Pythagoras the height is
\[
h=\sqrt{s^2-\dfrac{s^2}{3}}=s\sqrt{\dfrac23}.
\]
'''+asy(fig,'4.5cm')+r'''
With $h=2\sqrt3$ we get $s=2\sqrt3\cdot\sqrt{\dfrac32}=3\sqrt2$. The volume is
\[
V=\dfrac13\cdot\dfrac{\sqrt3}{4}s^2\cdot h=\dfrac13\cdot\dfrac{\sqrt3}{4}\cdot18\cdot2\sqrt3=\boxed{9}.
\]''',
'Pyramids|Volume|Equilateral triangles|Pythagorean theorem',3,
note='"A tetrahedron with height 2 sqrt 3" is read as a regular tetrahedron (otherwise the volume is not determined).')
fig=r'''pair O1=(0,0),O2=(2.6,0);
draw(circle(O1,1),gray(0.6));draw(circle(O2,1),gray(0.6));
pair[] H; for(int i=0;i<6;++i) H.push(O1+dir(60*i));
draw(H[0]--H[1]--H[2]--H[3]--H[4]--H[5]--cycle,linewidth(0.9));
pair[] G; for(int i=0;i<8;++i) G.push(O2+dir(45*i));
draw(G[0]--G[1]--G[2]--G[3]--G[4]--G[5]--G[6]--G[7]--cycle,linewidth(0.9));
draw(O1--H[0],blue);draw(O1--H[1],blue);draw(O2--G[0],blue);draw(O2--G[1],blue);
label("$1$",O1+0.5*dir(-14),S,blue);label("$1$",O2+0.5*dir(-14),S,blue);
label("$60^\circ$",O1+0.33*dir(30),dir(30),fontsize(7pt));label("$45^\circ$",O2+0.35*dir(22.5),dir(22.5),fontsize(7pt));'''
b.add(1734443,11,r'''What is the difference between the areas of a regular octagon and a regular hexagon, both inscribed in a circle of radius $1$?''',
r'''Split each polygon into isosceles triangles with two sides $1$ (radii) and apex angle $\dfrac{360^\circ}{n}$; each has area $\dfrac12\sin\dfrac{360^\circ}{n}$:
'''+asy(fig,'6cm')+r'''
\[
\text{hexagon: }6\cdot\dfrac12\sin60^\circ=\dfrac{3\sqrt3}{2},\qquad \text{octagon: }8\cdot\dfrac12\sin45^\circ=2\sqrt2 .
\]
The difference is $\boxed{2\sqrt2-\dfrac{3\sqrt3}{2}}\approx0.230$ (the octagon is larger).''',
'Regular polygons|Circles|Trigonometry|Area decomposition',3)
fig=r'''pair A=(0,0),B=(16,0),C=(16,12),D=(0,12),B2=(4.48,15.36),Q=(3.5,12);
fill(A--C--Q--cycle,rgb(0.82,0.9,1));
draw(A--B--C--D--cycle,linewidth(0.9));draw(A--C,linewidth(0.9));
draw(A--B2--C,red+dashed);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,E);label("$D$",D,W);label("$B'$",B2,N,red);label("$Q$",Q,dir(125));
label("$16$",(A+B)/2,S);label("$12$",(B+C)/2,E);'''
b.add(1734443,12,r'''A $12$ by $16$ rectangular piece of paper is folded along a diagonal. What is the area of the region where the two layers overlap?''',
r'''Let the rectangle be $ABCD$ with $AB=16$, $BC=12$, folded along $AC$, so that $B$ goes to $B'$. The overlap is the triangle $ACQ$, where $Q$ is the point where $AB'$ crosses side $DC$:
'''+asy(fig,'5.5cm')+r'''
Folding gives $\angle B'AC=\angle BAC$, and $\angle BAC=\angle ACD$ (alternate angles, $AB\parallel DC$). So $\angle QAC=\angle QCA$ and $QA=QC$. Let $QC=t$; then $DQ=16-t$, and in the right triangle $ADQ$:
\[
(16-t)^2+12^2=t^2\ \Longrightarrow\ 400=32t\ \Longrightarrow\ t=12.5 .
\]
Triangle $ACQ$ has base $QC=12.5$ on line $DC$ and height $AD=12$, so the overlap area is $\dfrac12\cdot12.5\cdot12=\boxed{75}$.''',
'Paper folding|Rectangles|Isosceles triangles|Pythagorean theorem|Reflections',3)
b.add(1734443,13,r'''Starting at $(0,0)$, you travel to $(3,4)$, then to $(14,7)$, then to $(24,10)$, then to $(26,17)$, moving only up or to the right one unit at a time. What are the last two digits of the total number of possible paths for the entire trip?''',
r'''Each leg is independent. A leg that goes $p$ units right and $q$ units up has $\binom{p+q}{p}$ paths. The legs are $(3,4)$, $(11,3)$, $(10,3)$, $(2,7)$, so the number of paths is
\[
\binom73\binom{14}{3}\binom{13}3\binom92=35\cdot364\cdot286\cdot36 .
\]
Modulo $100$: $35\cdot364\equiv35\cdot64=2240\equiv40$, then $40\cdot286\equiv40\cdot86=3440\equiv40$, then $40\cdot36=1440\equiv40$. The last two digits are $\boxed{40}$ (the total is $131171040$).''',
'Lattice paths|Combinations|Multiplication principle|Remainders and congruences',3)
fig=r'''real R=3,r=1;
draw((0,-1.8)--(0,1.8),dashed);label("axis",(0,1.8),N,fontsize(8pt));
draw(circle((R,0),r),blue+linewidth(0.9));draw(circle((-R,0),r),blue+linewidth(0.9));
draw((0,-1.35)--(R,-1.35),Arrows(TeXHead));draw((R,-0.15)--(R,-1.5),gray(0.5));label("$R$",(R/2,-1.35),S);
draw((R,0)--(R,0)+r*dir(-60));label("$r$",(R,0)+0.5*r*dir(-60),E);
dot((R,0));
draw(ellipse((0,0),R,0.45),gray(0.5)+dashed);'''
b.add(1734443,14,r'''A torus is formed by revolving a circle of radius $r$ about a line in its plane at distance $R>r$ from its centre. Using Pappus's centroid theorems (the surface area of a surface of revolution equals the length of the generating curve times the distance travelled by its centroid, and the volume of a solid of revolution equals the area of the generating region times the distance travelled by its centroid), find the surface area and the volume of the torus.''',
r'''The generating circle has centroid at its centre, which travels around a circle of radius $R$, a distance $2\pi R$:
'''+asy(fig,'5.5cm')+r'''
\textbf{Surface area.} The circle has length $2\pi r$, so $S=2\pi r\cdot2\pi R=\boxed{4\pi^2Rr}$.

\textbf{Volume.} The disc has area $\pi r^2$, so $V=\pi r^2\cdot2\pi R=\boxed{2\pi^2Rr^2}$.

(For example $R=3$, $r=1$ gives $S=12\pi^2$ and $V=6\pi^2$.)''',
'Solid geometry|Surface area|Volume|Circles',3,
note='"How do you find the surface area and volume of a torus" is turned into a question with the generating radii R and r; the solution uses Pappus\'s theorems, which are stated in the question.')
fig=r'''pair Nn=(0,5),Dj=(10,10),D2=(10,-10),X=(10/3,0);
draw((-1.5,0)--(12,0),blue+linewidth(1.2));label("river",(12,0),E,blue);
draw(Nn--X--Dj,linewidth(0.9));draw(X--D2,dashed);draw(Dj--D2,dotted);
dot(Nn);dot(Dj);dot(D2);dot(X);
label("$N$",Nn,W);label("$D$",Dj,E);label("$D'$",D2,E);label("$X$",X,dir(250));'''
b.add(1734443,15,r'''A ninja is standing $5$ miles north of a perfectly straight east-west river. He wants to get to a dojo $10$ miles east and $5$ miles north of his current location, but first he wants to stop at the river for a drink. What is the shortest distance he can travel?''',
r'''Put the river on the $x$-axis, the ninja at $N=(0,5)$ and the dojo at $D=(10,10)$. Reflect the dojo in the river to $D'=(10,-10)$. For any point $X$ on the river, $XD=XD'$, so the route length is $NX+XD'\ge ND'$, with equality when $X$ is on segment $ND'$:
'''+asy(fig,'5cm')+r'''
The shortest distance is $ND'=\sqrt{10^2+15^2}=\sqrt{325}=\boxed{5\sqrt{13}}\approx18.0$ miles (stopping at the point $\dfrac{10}{3}$ miles east of the start).''',
'Reflections|Distance formula|Coordinate geometry|Bounding and extremal cases',3)
fig=r'''real b=12,p=sqrt(297),q=sqrt(532),d=sqrt(492);
pair A=(-p,0),B=(0,b),C=(q,0),D=(0,-d),O=(0,0);
draw(A--B--C--D--cycle,linewidth(0.9));draw(A--C,dashed);draw(B--D,dashed);
draw((0,1.3)--(1.3,1.3)--(1.3,0));
label("$A$",A,W);label("$B$",B,N);label("$C$",C,E);label("$D$",D,S);label("$O$",O,dir(225));
label("$21$",(A+B)/2,NW);label("$26$",(B+C)/2,NE);label("$32$",(C+D)/2,SE);label("$\sqrt{789}$",(A+D)/2,SW);'''
b.add(1734443,16,r'''A convex quadrilateral $ABCD$ has perpendicular diagonals $AC$ and $BD$, and $AB=21$, $BC=26$, $CD=32$. What is the length of side $AD$?''',
r'''Let the diagonals meet at $O$, and let $OA=p$, $OB=b$, $OC=q$, $OD=d$. The four triangles around $O$ are right-angled, so
\[
AB^2=p^2+b^2,\quad BC^2=q^2+b^2,\quad CD^2=q^2+d^2,\quad DA^2=p^2+d^2 .
\]
'''+asy(fig,'5.5cm')+r'''
Hence $AB^2+CD^2=p^2+b^2+q^2+d^2=BC^2+DA^2$, and
\[
AD^2=21^2+32^2-26^2=441+1024-676=789,\qquad AD=\boxed{\sqrt{789}}.
\]
(The figure uses $b=12$, $p=\sqrt{297}$, $q=\sqrt{532}$, $d=\sqrt{492}$, which fit the data.)''',
'Quadrilaterals and polygons|Diagonals|Perpendicular lines|Pythagorean theorem',3)

# ---------------- 1729571 2016 AMC 8 #19 (alias)
b.add(1729571,1,r'''The sum of $25$ consecutive even integers is $10{,}000$. What is the largest of these $25$ consecutive integers?
\[
\textbf{(A)}\ 360\qquad\textbf{(B)}\ 388\qquad\textbf{(C)}\ 412\qquad\textbf{(D)}\ 416\qquad\textbf{(E)}\ 424
\]''',
r'''The middle (13th) number is the mean, $\dfrac{10000}{25}=400$. The largest is $12$ steps of $2$ above it: $400+24=\boxed{424}$, answer $\textbf{(E)}$.''',
'Arithmetic sequences|Averages and weighted averages',2,source=src('AMC 8',2016,None,19),
note='Repeat of an earlier record (aliased).')

# ---------------- 1734824 series manipulations
b.add(1734824,1,r'''For $S=\dfrac12+\dfrac14+\dfrac18+\cdots$ one argues: $2S=1+\dfrac12+\dfrac14+\cdots=1+S$, so $S=1$. For $T=1-1+1-1+\cdots$ the same kind of argument, $T=1-(1-1+1-\cdots)=1-T$, gives $T=\dfrac12$. Explain why the first argument is valid and the second is not.''',
r'''An infinite series means the limit of its partial sums, when that limit exists.

\textbf{First series.} The partial sums are $S_n=\dfrac12+\cdots+\dfrac1{2^n}=1-\dfrac1{2^n}$, which tend to $1$, so the series converges and $S$ is a genuine number. For convergent series, multiplying termwise by a constant and adding or subtracting termwise are allowed, because they are just limits of the same operations on partial sums: $2S_n=1+S_{n-1}$ for every $n$, and letting $n\to\infty$ gives $2S=1+S$. So $S=1$ is correct (and agrees with $S_n\to1$).

\textbf{Second series.} The partial sums are $T_n=1,0,1,0,\dots$, which do not approach any limit, so $T$ is not a number at all; the series diverges. The step $T=1-T$ treats $T$ as a number and rearranges it, which is meaningless. Assuming that a divergent series has a value leads to contradictions: grouping as $(1-1)+(1-1)+\cdots$ would give $T=0$, while $1+(-1+1)+(-1+1)+\cdots$ would give $T=1$.

So the manipulation is justified for convergent series (where linearity of limits applies), not for divergent ones. (The value $\dfrac12$ does have a meaning in more general summation methods, such as the average of the partial sums, but not as an ordinary sum.)''',
'Geometric sequences|Sequences and series|Counterexamples',3,
note='The post asks whether the difference is convergence; turned into an explanation question.')

# ---------------- 1735477 sparrows and feeders
b.add(1735477,1,r'''Some sparrows are flying in a garden where $5$ feeders hang. If one sparrow sits on each feeder, some sparrows are still left flying. If instead all the sparrows sit down, two on each occupied feeder, then at least one feeder is empty. How many sparrows can there be?''',
r'''Let there be $n$ sparrows. The first condition says $n>5$. In the second arrangement $n$ is even (two on each occupied feeder) and at most $4$ feeders are occupied, so $n\le8$. The even numbers with $5<n\le8$ are $6$ and $8$, and both work: $6$ sparrows leave $1$ flying, or fill $3$ feeders leaving $2$ empty; $8$ sparrows leave $3$ flying, or fill $4$ feeders leaving $1$ empty. So there are $\boxed{6\text{ or }8}$ sparrows.''',
'Inequalities|Logical deduction|Parity',2,
note='The vague second condition ("when two sparrows are on each feeder, some of the feeders will be empty") is made precise: all sparrows sit, two on each occupied feeder, and at least one feeder is empty. (If one sparrow could be left over, 7 would also be possible.)')

# ---------------- 1735595 four tournament problems
fig=r'''pair P=(-1,4),Q=(12,21),P2=(4,-1),X=(48/7,48/7);
draw((-2.5,0)--(13,0),gray(0.5),Arrow(TeXHead));draw((0,-2.5)--(0,22),gray(0.5),Arrow(TeXHead));
label("$x$",(13,0),S,gray(0.3));label("$y$",(0,22),W,gray(0.3));
draw((-2,-2)--(13,13),blue+linewidth(0.9));label("$y=x$",(13,13),E,blue);
draw(P--X--Q,linewidth(0.9));draw(X--P2,dashed);draw(P--P2,dotted);
dot(P);dot(Q);dot(P2);dot(X);
label("$(-1,4)$",P,W);label("$(12,21)$",Q,E);label("$(4,-1)$",P2,E);label("$X$",X,E);'''
b.add(1735595,1,r'''Bill and Ted are at the point $(-1,4)$ of the coordinate plane. They want to get to a potato at $(12,21)$, but first they need water from a river along the line $y=x$. What is the length of the shortest route that goes first to the river and then to the potato?''',
r'''Both points lie above the line $y=x$. Reflect the start $(-1,4)$ in the line $y=x$ to get $(4,-1)$. For any point $X$ on the line, the distance from $(-1,4)$ to $X$ equals the distance from $(4,-1)$ to $X$, so the route length is at least the straight distance from $(4,-1)$ to $(12,21)$, with equality when $X$ lies on that segment:
'''+asy(fig,'5cm')+r'''
The shortest route has length $\sqrt{(12-4)^2+(21+1)^2}=\sqrt{64+484}=\sqrt{548}=\boxed{2\sqrt{137}}\approx23.4$.''',
'Reflections|Distance formula|Coordinate geometry',3,
note='First of four problems in the post (q01-q04 in order).')
b.add(1735595,2,r'''The six letters of ``TIN CAN'' (T, I, N, C, A, N) are arranged in a row and a single space is placed in one of the five gaps between consecutive letters, so that two groups of letters are formed. For example, ``NIT NAC'' is one arrangement, ``NAC NIT'' is a different one, and ``NITNAC'' (no space) does not count. How many arrangements are possible?''',
r'''The letters can be ordered in $\dfrac{6!}{2!}=360$ ways (the two N's are identical), and the space can go in any of the $5$ gaps. Different choices give different strings, so there are $360\cdot5=\boxed{1800}$ arrangements.''',
'Multiset permutations|Multiplication principle',2,
note='"Two distinct groups of letters" is read as: one space splits the six letters into two nonempty groups of any sizes. (If both groups must have three letters, the count is 360.)')
b.add(1735595,3,r'''What is the sum of the values of $k$ for which $f(x)=kx^2+3x+2k$ has exactly one distinct zero?''',
r'''If $k=0$, then $f(x)=3x$ has the single zero $x=0$, so $k=0$ counts. If $k\ne0$, $f$ is quadratic and has exactly one distinct zero when its discriminant vanishes: $9-8k^2=0$, so $k=\pm\dfrac{3}{2\sqrt2}=\pm\dfrac{3\sqrt2}{4}$. The values are $0$ and $\pm\dfrac{3\sqrt2}4$, and their sum is $\boxed{0}$.''',
'Quadratic equations|Polynomial roots',2)
b.add(1735595,4,r'''A yacht hits an iceberg that breaks two holes in the hull. Water rushes through one hole at a rate that would sink the yacht in $72$ minutes, and through the other at a rate that would sink it in $2$ hours. How many minutes would it take for the yacht to sink with water rushing through both holes?''',
r'''In one minute the holes let in $\dfrac1{72}$ and $\dfrac1{120}$ of the water needed to sink the yacht, together
\[
\dfrac1{72}+\dfrac1{120}=\dfrac{5+3}{360}=\dfrac1{45}.
\]
So the yacht sinks in $\boxed{45}$ minutes. (The sailing speed and the time of day in the original story are irrelevant.)''',
'Work and rates|Fractions',2)

# ---------------- 1732120 denesting
b.add(1732120,1,r'''Simplify $\sqrt{1+a^2+\sqrt{1+a^2+a^4}}$ for real $a$.''',
r'''First, $1+a^2+a^4=(a^2+1)^2-a^2=(a^2+a+1)(a^2-a+1)$, and both factors are positive. Look for $u,v\ge0$ with $(\sqrt u+\sqrt v)^2=u+v+2\sqrt{uv}$ equal to the expression under the outer root, i.e.
\[
u+v=1+a^2,\qquad 4uv=1+a^2+a^4 .
\]
Since $(a^2+a+1)+(a^2-a+1)=2(1+a^2)$, the choice $u=\dfrac{a^2+a+1}{2}$, $v=\dfrac{a^2-a+1}{2}$ works: $u+v=1+a^2$ and $4uv=(a^2+a+1)(a^2-a+1)=1+a^2+a^4$. Therefore
\[
\sqrt{1+a^2+\sqrt{1+a^2+a^4}}=\sqrt{\dfrac{a^2+a+1}{2}}+\sqrt{\dfrac{a^2-a+1}{2}}=\boxed{\dfrac{\sqrt{2a^2+2a+2}+\sqrt{2a^2-2a+2}}{2}}.
\]
(Check at $a=0$: both sides equal $\sqrt2$; at $a=1$: $\sqrt{2+\sqrt3}=\dfrac{\sqrt6+\sqrt2}{2}$.)''',
'Radicals|Factoring|Algebraic expressions and identities',4)

# ---------------- 1724280 divisibility of polynomials
b.add(1724280,1,r'''Let $P(x)=x^3+ax+b$ and $Q(x)=x^2-3x+2$. Find $a$ and $b$ such that $P(x)$ is divisible by $Q(x)$.''',
r'''Since $Q(x)=(x-1)(x-2)$, $Q$ divides $P$ exactly when $P(1)=0$ and $P(2)=0$ (factor theorem):
\[
1+a+b=0,\qquad 8+2a+b=0 .
\]
Subtracting gives $7+a=0$, so $\boxed{a=-7,\ b=6}$. Indeed $x^3-7x+6=(x-1)(x-2)(x+3)$.''',
'Remainder theorem and factor theorem|Polynomials|Systems of linear equations',2,
note='The notation P(x) ⋮ Q(x) ("P is divisible by Q") is written out in words.')

# ---------------- 1735442 page digits
b.add(1735442,1,r'''Printing the page numbers of a $12$-page book uses $15$ digits ($1,2,\dots,9,10,11,12$). How many digits are used to print the page numbers of a book with $200$ pages?''',
r'''Pages $1$-$9$ use $9$ digits, pages $10$-$99$ use $90\cdot2=180$ digits, and pages $100$-$200$ use $101\cdot3=303$ digits. The total is $9+180+303=\boxed{492}$.''',
'Digits and bases|Fencepost counting|Whole-number operations',1)

# ---------------- 1734263 Heron-type formulas for quadrilaterals
fig=r'''draw(box((0,0),(1,1)),linewidth(0.9));
pair A=(1.6,0),B=(2.6,0),C=B+dir(60),D=A+dir(60);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(arc(A,0.22,0,60));label("$60^\circ$",A+0.42*dir(30),fontsize(7pt));
label("$1$",(0.5,0),S);label("$1$",(1,0.5),E);label("$1$",(0.5,1),N);label("$1$",(0,0.5),W);
label("$1$",(A+B)/2,S);label("$1$",(B+C)/2,E);label("$1$",(C+D)/2,N);label("$1$",(D+A)/2,W);'''
fig2=r'''real R=32.5; pair V2=(-R,0),V4=(R,0),V1=V2+25*dir(degrees(acos(5/13))),V3=V2+39*dir(-degrees(acos(3/5)));
draw(circle((0,0),R),gray(0.6));
draw(V1--V2--V3--V4--cycle,linewidth(0.9));draw(V2--V4,dashed);
pair u=unit(V2-V1),w=unit(V4-V1);draw(V1+2.5*u--V1+2.5*u+2.5*w--V1+2.5*w);
pair u2=unit(V2-V3),w2=unit(V4-V3);draw(V3+2.5*u2--V3+2.5*u2+2.5*w2--V3+2.5*w2);
label("$V_1$",V1,N);label("$V_2$",V2,W);label("$V_3$",V3,S);label("$V_4$",V4,E);
label("$25$",(V1+V2)/2,unit(-(V1+V2)));label("$39$",(V2+V3)/2,unit(-(V2+V3)));label("$52$",(V3+V4)/2,unit(-(V3+V4)));label("$60$",(V4+V1)/2,unit(-(V4+V1)));
label("$65$",(12,0),N);'''
b.add(1734263,1,r'''Heron's formula gives the area of a triangle from its three side lengths.
\begin{enumerate}
\item[(a)] Show that no formula can give the area of every quadrilateral from its four side lengths alone.
\item[(b)] For cyclic quadrilaterals there is such a formula, Brahmagupta's formula $K=\sqrt{(s-a)(s-b)(s-c)(s-d)}$, where $s$ is the semiperimeter. A cyclic quadrilateral has sides $25$, $39$, $52$, $60$ in this order. Find its area, both by Brahmagupta's formula and by splitting it into two triangles.
\end{enumerate}''',
r'''\textbf{(a)} A unit square and a rhombus with side $1$ and an angle of $60^\circ$ have the same four side lengths:
'''+asy(fig,'5cm')+r'''
but their areas are $1$ and $1\cdot1\cdot\sin60^\circ=\dfrac{\sqrt3}{2}$. So the side lengths do not determine the area of a quadrilateral, and no formula in the side lengths alone can work. (A quadrilateral with given sides can flex, unlike a triangle.)

\textbf{(b)} Here $s=\dfrac{25+39+52+60}{2}=88$, so
\[
K=\sqrt{63\cdot49\cdot36\cdot28}=\sqrt{(7\cdot9)\cdot7^2\cdot6^2\cdot(4\cdot7)}=7^2\cdot6\cdot3\cdot2=\boxed{1764}.
\]
Check by splitting: $25^2+60^2=65^2$ and $39^2+52^2=65^2$. Let the vertices be $V_1,\dots,V_4$ with $V_1V_2=25$, $V_2V_3=39$, $V_3V_4=52$, $V_4V_1=60$. The triangles $V_4V_1V_2$ and $V_2V_3V_4$ with the common side $V_2V_4=65$ are right triangles, so both right angles are inscribed in the circle with diameter $V_2V_4$, which is therefore the circumcircle:
'''+asy(fig2,'5cm')+r'''
The area is $\dfrac12\cdot25\cdot60+\dfrac12\cdot39\cdot52=750+1014=1764$, as before.''',
'Brahmagupta\'s formula|Cyclic quadrilaterals|Heron\'s formula|Rhombi|Counterexamples|Right triangles',4,
note='The post asks whether Heron\'s formula applies to other shapes; turned into a counterexample for general quadrilaterals and an application of Brahmagupta\'s formula for cyclic ones.')

# ---------------- 1735427 palindromes with digit sum 9
b.add(1735427,1,r'''How many $3$-digit palindromes have digit sum $9$?''',
r'''A $3$-digit palindrome is $\overline{aba}$ with $1\le a\le9$ and $0\le b\le9$, and its digit sum is $2a+b=9$. Then $b=9-2a\ge0$ forces $a\le4$, and every $a=1,2,3,4$ works: $171$, $252$, $333$, $414$. The answer is $\boxed{4}$.''',
'Palindromes|Digits and bases|Systematic counting',1)

# ---------------- 1735205 2018 National Team #9
b.add(1735205,1,r'''Claudia and Mary Ann each choose a set of ten consecutive positive integers. They each compute the greatest common factor of each pair of distinct numbers in their set, so that each has a list of $45$ numbers. If $C$ is the sum of Claudia's $45$ greatest common factors, and $M$ is the sum of Mary Ann's $45$ greatest common factors, what is the greatest possible value of $C-M$?''',
r'''Use the identity $m=\sum_{d\mid m}\varphi(d)$ ($\varphi$ is Euler's totient). For a set of ten consecutive integers,
\[
\sum_{\text{pairs}}\gcd(x,y)=\sum_{\text{pairs}}\ \sum_{d\mid x,\ d\mid y}\varphi(d)=\sum_{d\ge1}\varphi(d)\binom{c_d}{2},
\]
where $c_d$ is the number of multiples of $d$ in the set. For $d\ge10$ there is at most one multiple, so only $d\le9$ count, and $c_d$ is $\left\lfloor\dfrac{10}{d}\right\rfloor$ or $\left\lceil\dfrac{10}{d}\right\rceil$:
\[
\begin{array}{c|ccccccccc}
d&1&2&3&4&5&6&7&8&9\\\hline
\varphi(d)&1&1&2&2&4&2&6&4&6\\
c_d&10&5&3\text{ or }4&2\text{ or }3&2&1\text{ or }2&1\text{ or }2&1\text{ or }2&1\text{ or }2\\
\varphi(d)\binom{c_d}2&45&10&6\text{ or }12&2\text{ or }6&4&0\text{ or }2&0\text{ or }6&0\text{ or }4&0\text{ or }6
\end{array}
\]
So every sum lies between $45+10+6+2+4=67$ and $45+10+12+6+4+2+6+4+6=95$.

Both extremes occur. The set $504,505,\dots,513$ starts with a multiple of $9$, $8$ and $7$ ($504=7\cdot8\cdot9$), so it contains $4$ multiples of $3$, $3$ of $4$ ($504,508,512$), $2$ of $6$ ($504,510$), $2$ of $7$, $2$ of $8$ and $2$ of $9$: its sum is $95$. The set $2,3,\dots,11$ contains $3$ multiples of $3$, $2$ of $4$, and only one multiple each of $6,7,8,9$: its sum is $67$. Hence the greatest possible value of $C-M$ is $95-67=\boxed{28}$.''',
'HCF and LCM|Euler\'s theorem and totient|Double counting|Bounding and extremal cases',6,source=src('MATHCOUNTS',2018,'National',9,rnd='Team'),
note='The posted answer 28 is confirmed; the poster\'s idea (sets with many or few primes) does not decide the sums. Checked by computing the sum for every starting value modulo 2520.')

# ---------------- 1732115 Bob and Fortnite
b.add(1732115,1,r'''Bob comes home from school at a random time between 3:00 and 4:00 pm, and his mom comes home from work at a random time between 3:15 and 4:15 pm (both uniformly distributed, independently). If no one else is in the house when Bob gets home, he starts a game that lasts a random time between $5$ and $15$ minutes (uniformly distributed, independent of the arrival times). If Bob's mom comes home while Bob is playing, there is a $50\%$ chance that she makes him stop, in which case he will rage. What is the probability that Bob will rage?''',
r'''Measure times in minutes after 3:00: Bob arrives at $B$ uniform on $[0,60]$, his mom at $M$ uniform on $[15,75]$, and the game lasts $L$ uniform on $[5,15]$. Bob plays only if his mom is not yet home, and she interrupts him when $B<M<B+L$; then he rages with probability $\dfrac12$.

Write $M=15+V$ with $V$ uniform on $[0,60]$. Then $M-B=15+(V-B)$, and $D=V-B$ has the triangular density $\dfrac{60-|x|}{3600}$ on $[-60,60]$. The condition $0<M-B<L$ means $-15<D<L-15$, an interval inside $[-15,0]$, where the density is $\dfrac{60+x}{3600}$. Substituting $y=x+15$, for a fixed $L$:
\[
P(0<M-B<L)=\int_0^L\dfrac{45+y}{3600}\,dy=\dfrac{45L+L^2/2}{3600}.
\]
Averaging over $L$: $E[L]=10$ and $E[L^2]=\dfrac{15^3-5^3}{3\cdot10}=\dfrac{325}3$, so
\[
P(\text{interrupted})=\dfrac{45\cdot10+\dfrac12\cdot\dfrac{325}{3}}{3600}=\dfrac{3025/6}{3600}=\dfrac{121}{864}.
\]
The probability that Bob rages is $\dfrac12\cdot\dfrac{121}{864}=\boxed{\dfrac{121}{1728}}\approx0.070$.''',
'Geometric probability|Probability|Independent events|Calculus',6,
note='All three random times are taken as uniform and independent, as the post implies. Checked by exact integration and by simulation.')

# ---------------- 1735058 fly between trains
b.add(1735058,1,r'''Two trains are $300$ miles apart and moving toward each other, one at $20$ mph and the other at $40$ mph. A fly that flies at $70$ mph starts at the front of one train and flies back and forth between the two trains until they meet. How far does the fly travel?''',
r'''The trains approach each other at $20+40=60$ mph, so they meet after $\dfrac{300}{60}=5$ hours. The fly flies at $70$ mph the whole time, so it travels $70\cdot5=\boxed{350}$ miles. (There is no need to add up the infinitely many back-and-forth trips.)''',
'Relative speed|Distance, rate, and time',2)

# ---------------- 1722397 x^3 odd
b.add(1722397,1,r'''Prove that $f(x)=x^3$ is an odd function.''',
r'''A function is odd when $f(-x)=-f(x)$ for every $x$ in its domain (here all real numbers). For every real $x$,
\[
f(-x)=(-x)^3=(-x)(-x)(-x)=-x^3=-f(x),
\]
so $f$ is odd. $\blacksquare$ (Its graph is symmetric about the origin.)''',
'Functions|Symmetry',1)

# ---------------- 1734599 intersecting chords
fig=r'''pair A=(0,0),B=(-3,0),D=(6,0); pair u=dir(115); pair C=8*u,Ep=-(9/4)*u;
real k=(C.x^2+C.y^2-3*C.x-18)/(2*C.y); pair P=(1.5,k);
draw(circle(P,abs(B-P)),linewidth(0.9));
draw(B--D,linewidth(0.9));draw(C--Ep,linewidth(0.9));
dot(A);dot(P);
label("$A$",A,dir(55));label("$B$",B,W);label("$D$",D,E);label("$C$",C,N);label("$E$",Ep,S);label("$P$",P,E);
label("$3$",(A+B)/2,S);label("$6$",(A+D)/2,S);label("$8$",(A+C)/2,W);'''
b.add(1734599,1,r'''In circle $P$, chords $BD$ and $CE$ intersect at $A$, as shown, with $AB=3$ units, $AC=8$ units and $AD=6$ units. What is the value of $AE$? Express your answer as a mixed number.
'''+asy(fig,'4.5cm'),
r'''By the intersecting chords theorem (power of the point $A$), the products of the pieces of the two chords are equal:
\[
AB\cdot AD=AC\cdot AE\quad\Longrightarrow\quad3\cdot6=8\cdot AE\quad\Longrightarrow\quad AE=\dfrac{18}{8}=\boxed{2\dfrac14}\text{ units}.
\]
'''+asy(fig.replace(r'label("$8$",(A+C)/2,W);',r'label("$8$",(A+C)/2,W);label("$2\dfrac14$",(A+Ep)/2,E,blue+fontsize(8pt));draw(A--Ep,blue+linewidth(1));'),'4.5cm')+r'''
(The triangles $ABC$ and $AED$ are similar, since $\angle BAC=\angle EAD$ (vertical angles) and $\angle ABC=\angle AED$ (both inscribed in arc $CD$), which is why the products agree.)''',
'Power of a point|Arcs and chords|Circles|Similarity',2,source=src('MATHCOUNTS Handbook',2019,None,6,rnd='Warm-Up 3'),
note='The figure was attached. The chords are stated as BD and CE, the pairing consistent with the requested mixed-number answer (pairing B with C would give the integer 4). Figure redrawn to scale with AE = 9/4.')

# ---------------- 1734465 roots 2, a+1, a-1
b.add(1734465,1,r'''The numbers $2$, $a+1$ and $a-1$ are the roots of the equation $x^3+bx^2-bx-c=0$. Find all possible values of $b$.''',
r'''By Vieta's formulas,
\[
2+(a+1)+(a-1)=-b,\qquad 2(a+1)+2(a-1)+(a+1)(a-1)=-b,\qquad 2(a+1)(a-1)=c .
\]
The first two give $2a+2=a^2+4a-1$, i.e.\ $a^2+2a-3=(a-1)(a+3)=0$.

\begin{itemize}
\item $a=1$: the roots are $2,2,0$, $b=-4$, $c=0$, and indeed $x(x-2)^2=x^3-4x^2+4x$.
\item $a=-3$: the roots are $2,-2,-4$, $b=4$, $c=16$, and indeed $(x-2)(x+2)(x+4)=x^3+4x^2-4x-16$.
\end{itemize}
So $\boxed{b=4\text{ or }b=-4}$. (If the three roots must be distinct, only $b=4$ remains.)''',
'Vieta\'s formulas|Polynomial roots|Quadratic equations',3,
note='The post asks for b; both values b = 4 and b = -4 satisfy the conditions as stated (b = -4 gives a double root 2), so both are given.')

# ---------------- 1734740 AMC 8 prep problem 5
fig=r'''draw(box((-1,-1),(1,1)),linewidth(0.9));
draw((-1.6,0)--(1.6,0),gray(0.6),Arrow(TeXHead));draw((0,-1.6)--(0,1.7),gray(0.6),Arrow(TeXHead));
pair P1=(-1,1),P2=(1,1);
draw(P1--P2,blue+linewidth(1));dot(P1,blue);dot(P2,blue);
label("$P_1$",P1,NW);label("$P_2$",P2,NE);label("$a=2$",(0,1),N,blue);
label("$(1,-1)$",(1,-1),SE,fontsize(8pt));label("$(-1,-1)$",(-1,-1),SW,fontsize(8pt));'''
b.add(1734740,1,r'''Two distinct points $P_1$ and $P_2$ lie in the square with vertices $(1,1)$, $(1,-1)$, $(-1,-1)$, $(-1,1)$ (boundary included). Let $a$ be the length of $\overline{P_1P_2}$ and $b$ the sum of the $y$-coordinates of the two points. Two new distinct points $P_3$ and $P_4$ are plotted so that the difference of their $y$-coordinates is $a$ and the difference of their $x$-coordinates is $b$. What is the greatest integer less than or equal to the maximum possible length of $\overline{P_3P_4}$?''',
r'''Let $P_1=(x_1,y_1)$ and $P_2=(x_2,y_2)$. Then
\[
P_3P_4^2=a^2+b^2=(x_1-x_2)^2+(y_1-y_2)^2+(y_1+y_2)^2=(x_1-x_2)^2+2(y_1^2+y_2^2).
\]
In the square $|x_i|,|y_i|\le1$, so $(x_1-x_2)^2\le4$ and $2(y_1^2+y_2^2)\le4$, hence $P_3P_4\le\sqrt8=2\sqrt2$. Equality holds for $P_1=(-1,1)$ and $P_2=(1,1)$ (then $a=2$, $b=2$):
'''+asy(fig,'4cm')+r'''
The maximum length is $2\sqrt2\approx2.83$, and the greatest integer not exceeding it is $\boxed{2}$. (If the points had to be strictly inside the square, the length could get arbitrarily close to $2\sqrt2$ without reaching it, and the answer would still be $2$.)''',
'Distance formula|Coordinate geometry|Squares|Bounding and extremal cases|Floor and ceiling functions',3,
note='"Entirely contained within the square" is read as boundary included; the answer is the same for the interior.')

# ---------------- 1734735 AMC 8 prep problem 4
b.add(1734735,1,r'''Let $\ell$ be the least common multiple of two distinct integers between $1$ and $100$ (inclusive), and let $g$ be their greatest common divisor. What is the maximum possible value of $\left\lfloor\dfrac{\ell g+\ell+g}{\ell^2+g^2}\right\rfloor$?''',
r'''Since $g$ divides $\ell$ and the integers are distinct, $\ell=kg$ with $k\ge2$. Then
\[
\ell^2+g^2-(\ell g+\ell+g)=g^2(k^2+1)-g^2k-g(k+1)=g\bigl(g(k^2-k+1)-(k+1)\bigr).
\]
For $k\ge2$ and $g\ge1$, $g(k^2-k+1)-(k+1)\ge k^2-2k=k(k-2)\ge0$. So the fraction is at most $1$, and its floor is at most $1$. The value $1$ is attained by the numbers $1$ and $2$: $\ell=2$, $g=1$, $\dfrac{2+2+1}{4+1}=1$. The maximum is $\boxed{1}$.''',
'HCF and LCM|Inequalities|Floor and ceiling functions|Bounding and extremal cases',3)

# ---------------- 1734605 equilateral hexagon
fig=r'''real[] dirs={0,75,120,195,240,315};
pair[] V={(0,0)}; for(int i=0;i<5;++i) V.push(V[i]+2*dir(dirs[i]));
draw(V[0]--V[1]--V[2]--V[3]--V[4]--V[5]--cycle,linewidth(0.9));
draw(V[0]--V[2]--V[4]--cycle,blue+dashed);
string[] nm={"$A$","$B$","$C$","$D$","$E$","$F$"};
pair c=(V[0]+V[2]+V[4])/3;
for(int i=0;i<6;++i) label(nm[i],V[i],unit(V[i]-c));
for(int i=0;i<6;++i){pair m=(V[i]+V[(i+1)%6])/2; label("$2$",m,unit(m-c),fontsize(8pt));}
label("$105^\circ$",V[1]+0.55*unit(c-V[1]),fontsize(7pt));'''
b.add(1734605,1,r'''Equilateral hexagon $ABCDEF$ has side length $2$. Angles $A$, $C$ and $E$ are $135^\circ$, and angles $B$, $D$ and $F$ are $105^\circ$. What is the area of hexagon $ABCDEF$?''',
r'''Triangles $ABC$, $CDE$, $EFA$ are congruent (SAS: two sides $2$ with an included angle of $105^\circ$), so $AC=CE=EA$ and triangle $ACE$ is equilateral:
'''+asy(fig,'5cm')+r'''
(The angles fit: each base angle of triangle $ABC$ is $\dfrac{180^\circ-105^\circ}{2}=37.5^\circ$, and $135^\circ-2\cdot37.5^\circ=60^\circ$ is left at $A$, $C$, $E$ for the equilateral triangle.)

By the law of cosines, $AC^2=2^2+2^2-2\cdot2\cdot2\cos105^\circ=8+8\sin15^\circ=8+2(\sqrt6-\sqrt2)$, using $\cos105^\circ=-\sin15^\circ=-\dfrac{\sqrt6-\sqrt2}{4}$. The area is
\[
[ACE]+3[ABC]=\dfrac{\sqrt3}{4}AC^2+3\cdot\dfrac12\cdot2\cdot2\sin105^\circ .
\]
Here $\dfrac{\sqrt3}{4}\left(8+2\sqrt6-2\sqrt2\right)=2\sqrt3+\dfrac{3\sqrt2-\sqrt6}{2}$, and with $\sin105^\circ=\dfrac{\sqrt6+\sqrt2}{4}$, $6\sin105^\circ=\dfrac{3\sqrt6+3\sqrt2}{2}$. Adding,
\[
\text{area}=2\sqrt3+\dfrac{6\sqrt2+2\sqrt6}{2}=\boxed{2\sqrt3+3\sqrt2+\sqrt6}\approx10.16 .
\]''',
'Quadrilaterals and polygons|Equilateral triangles|Law of cosines|Area decomposition|Trigonometric identities|Isosceles triangles',4,
note='The hexagon is determined by the data (its sides turn by 75 and 45 degrees alternately and close up). The area was checked with the shoelace formula.')

# ---------------- 1734670 AMC 8 prep problem 3
b.add(1734670,1,r'''A polynomial $f(x)$ of degree $25$ has $f(0)=0$, and for each integer $k$ with $1\le k\le25$ the coefficient of $x^k$ in $f(x)$ is $k$. When $[f(x)]^{2018}$ is expanded and like terms are combined, what is the units digit of the sum of the coefficients of the resulting polynomial?''',
r'''The sum of the coefficients of a polynomial $p$ is $p(1)$. Here $f(1)=1+2+\dots+25=\dfrac{25\cdot26}{2}=325$, so the required sum is $325^{2018}$. Every power of a number ending in $5$ ends in $5$, so the units digit is $\boxed{5}$.''',
'Polynomials|Units digits and last digits|Exponents',2)

b.save()
