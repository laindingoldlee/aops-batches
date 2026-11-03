from qb import *
b=Bank('p222_02')

# ---------------- 1782319 BdMO 2014 Dhaka 4 (no solutions)
b.add(1782319,1,r'''Prove that there are no positive integers $p$ and $q$ such that
\[
\dfrac{p^6+2p^4+p^2}{p^9-8p^3}-\dfrac{1}{4q}=\dfrac{5}{6q}.
\]''',
r'''We need $p^9-8p^3\ne0$, i.e.\ $p^6\ne8$, which holds for all positive integers. Simplify both sides. The left fraction is
\[
\dfrac{p^2(p^2+1)^2}{p^3(p^6-8)}=\dfrac{(p^2+1)^2}{p(p^6-8)},
\]
and $\dfrac{5}{6q}+\dfrac{1}{4q}=\dfrac{10+3}{12q}=\dfrac{13}{12q}$. So the equation is
\[
12q\,(p^2+1)^2=13p\,(p^6-8).
\]
For $p=1$ the right side is negative, so $p\ge2$. Now look at the factor $p^2+1$:
\begin{itemize}
\item $\gcd(p^2+1,p)=1$;
\item $p^2\equiv-1\pmod{p^2+1}$ gives $p^6\equiv-1$, so $p^6-8\equiv-9\pmod{p^2+1}$ and $\gcd(p^2+1,p^6-8)$ divides $9$; but $p^2+1\equiv1$ or $2\pmod3$ is never divisible by $3$, so $\gcd(p^2+1,p^6-8)=1$.
\end{itemize}
Hence $(p^2+1)^2$ is coprime to $p(p^6-8)$, and since it divides $13p(p^6-8)$, it divides $13$. But $(p^2+1)^2\ge25>13$ for $p\ge2$. This contradiction shows that there are \boxed{\text{no positive integers }p,q} satisfying the equation. $\blacksquare$''',
'Rational equations|Divisibility|Remainders and congruences|Factoring|Diophantine equations',5,
source=src('Bangladesh Mathematical Olympiad',2014,'Dhaka Regional',4),
note='The post (BdMO 2014 Dhaka regional, problem 4) asks for the minimum of p*q, but as typed the equation has no solutions in positive integers (proved here; also checked by search for p < 3000). The original wording could not be recovered, so the record asks for the proof that there are no solutions.')

# ---------------- 1782694 BdMO 2014 Dhaka 3, square in triangle (two cases)
fig=r'''pair B=(0,0),C=(6,0),A=(2.5,2);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--(-0.8,2),dotted);draw((-0.6,0)--(-0.6,2),Arrows(4));
pair D=(1.875,1.5),Ep=(3.375,1.5),F=(3.375,0),G=(1.875,0);
draw(D--Ep--F--G--cycle,blue+linewidth(0.9));
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);
label("$D$",D,NW);label("$E$",Ep,NE);label("$F$",F,S);label("$G$",G,S);
label("$2$",(-0.6,1),W);label("$6$",(4.7,0),S);label("(i)",(3,-1.1));'''
fig2=r'''pair B=(0,0),C=(6,0),A=(2.5,2);
pair D=(3.75,3),Ep=(0.75,3),F=(0.75,0),G=(3.75,0);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--D,dashed);draw(A--Ep,dashed);
draw(D--Ep--F--G--cycle,blue+linewidth(0.9));
label("$A$",A,S);label("$B$",B,SW);label("$C$",C,SE);
label("$D$",D,NE);label("$E$",Ep,NW);label("$F$",F,S);label("$G$",G,S);
label("$3$",(D+Ep)/2,N);label("$6$",(4.9,0),S);label("(ii)",(3,-1.1));'''
b.add(1782694,1,r'''$ABC$ is a triangle in which the altitude from $A$ to $BC$ has length $2$ and $BC=6$. $DEFG$ is a square with $D$ on line $AB$ and $E$ on line $AC$ (on the sides or their extensions), and $F$, $G$ on line $BC$. Find all possible values of the perimeter of $DEFG$.''',
r'''Let the square have side $s$. Since $F$ and $G$ lie on $BC$, the side $DE$ is parallel to $BC$ at distance $s$ from it. Triangle $ADE$ is then similar to triangle $ABC$ (with $D\in AB$, $E\in AC$), and the ratio of similarity is the ratio of the distances from $A$ to the lines $DE$ and $BC$. So
\[
\dfrac{DE}{BC}=\dfrac{|2-s|}{2}\quad\text{if $DE$ is on the same side of $BC$ as $A$,}\qquad
\dfrac{DE}{BC}=\dfrac{2+s}{2}\quad\text{otherwise.}
\]
With $DE=s$ and $BC=6$:
\begin{itemize}
\item $DE$ between $BC$ and $A$ ($s<2$): $s=3(2-s)$, so $s=\dfrac32$; this is the square inscribed in the triangle, figure (i).
\item $DE$ beyond $A$ ($s>2$): $s=3(s-2)$, so $s=3$; here $D$ and $E$ lie on the extensions of $AB$ and $AC$ beyond $A$, figure (ii).
\item $DE$ on the other side of $BC$: $s=3(2+s)$ has no positive solution.
\end{itemize}
'''+asy(fig,'5.5cm')+asy(fig2,'5.5cm')+r'''
So the perimeter of $DEFG$ is $4\cdot\dfrac32=\boxed{6}$ for the square inside the triangle, and $4\cdot3=\boxed{12}$ for the square on the extensions beyond $A$. (The computation does not depend on the shape of the triangle; in figure (ii) the square overlaps the triangle, and $A$ lies inside it.)''',
'Squares|Similarity|Triangles|Altitudes|Lengths, perimeter, and area',4,
source=src('Bangladesh Mathematical Olympiad',2014,'Dhaka Regional',3),
note='BdMO 2014 Dhaka regional, problem 3. Because the post allows D, E on the extensions of AB, AC, there are two squares (side 3/2 and side 3); the record asks for all values (perimeters 6 and 12). Both configurations were checked with coordinates.')

# ---------------- 1782754 (a-1) | a^n - 1
b.add(1782754,1,r'''Let $a>1$ and $n\ge1$ be integers. Prove that $a-1$ divides $a^n-1$.''',
r'''\textbf{Factorisation.} For every $n\ge1$,
\[
a^n-1=(a-1)\left(a^{n-1}+a^{n-2}+\cdots+a+1\right),
\]
as one checks by expanding: the product is $(a^n+a^{n-1}+\cdots+a)-(a^{n-1}+\cdots+a+1)=a^n-1$. The second factor is an integer, so $(a-1)\mid a^n-1$.

\textbf{Congruences (alternative).} Since $a\equiv1\pmod{a-1}$, we get $a^n\equiv1^n=1\pmod{a-1}$, i.e.\ $a-1\mid a^n-1$. $\blacksquare$''',
'Divisibility|Factoring|Remainders and congruences|Geometric sequences',2)

# ---------------- 1782611 2017 MATHCOUNTS State: Sprint 26, 29, 30, Target 8
fig=r'''pair A=(-4,0),B=(6,0),C=(0,5),P=(-2/3,0),Q=(2,10/3);
fill(P--B--Q--cycle,palecyan);
draw((-5,0)--(7,0),gray,Arrow);draw((0,0)--(0,6),gray,Arrow);
draw(A--B--C--cycle,linewidth(0.9));
draw(P--Q,blue+linewidth(0.9));
dot(A);dot(B);dot(C);dot(P);dot(Q);
label("$(-4,0)$",A,S);label("$(6,0)$",B,S);label("$(0,5)$",C,NE);
label("$-\dfrac23$",P,S);label("$Q$",Q,NE);label("$x$",(7,0),E);label("$y$",(0,6),N);'''
b.add(1782611,26,r'''A triangle in the coordinate plane has vertices $(-4,0)$, $(6,0)$ and $(0,5)$. The line $y=\dfrac54x+c$, where $c$ is a positive number, divides the triangle into a trapezoid and a smaller triangle whose areas, respectively, are in the ratio $5:4$. What is the value of $c$? Express your answer as a common fraction.''',
r'''The side from $(-4,0)$ to $(0,5)$ has slope $\dfrac54$, so the line $y=\dfrac54x+c$ is parallel to it. For $c>0$ it cuts off a small triangle at the vertex $(6,0)$, similar to the whole triangle, and the rest is a trapezoid.
'''+asy(fig,'6.5cm')+r'''
The small triangle has $\dfrac{4}{5+4}=\dfrac49$ of the area of the whole triangle, so its linear ratio of similarity is $\sqrt{\dfrac49}=\dfrac23$. Its side on the $x$-axis is $\dfrac23\cdot10=\dfrac{20}{3}$, so the line meets the $x$-axis at $x=6-\dfrac{20}{3}=-\dfrac23$. Then $0=\dfrac54\cdot\left(-\dfrac23\right)+c$, so
\[
c=\boxed{\dfrac56}.
\]
(Check: the line meets the side $y=5-\dfrac56x$ at $Q=\left(2,\dfrac{10}{3}\right)$; the small triangle has area $\dfrac12\cdot\dfrac{20}{3}\cdot\dfrac{10}{3}=\dfrac{100}{9}$ and the whole triangle $25$, and $25-\dfrac{100}{9}=\dfrac{125}{9}$, ratio $125:100=5:4$.)''',
'Coordinate geometry|Similarity|Area ratios|Slope|Triangles',3,
source=src('MATHCOUNTS',2017,'State',26,rnd='Sprint'))
fig=r'''pair X=(0,0),A=(-3,5),B=(4,5),C=(4.2,-7),D=(-5.6,-7);
pair P=(-0.2,5),Q=(2.8,-7),M=(0.8,1),Nn=(1.8,-3);
draw((-5,5)--(6,5),linewidth(0.9));draw((-7,-7)--(6,-7),linewidth(0.9));
draw(A--C,linewidth(0.8));draw(B--D,linewidth(0.8));
draw(P--Q,blue+linewidth(0.9));
dot(X);dot(P);dot(Q);dot(M);dot(Nn);
label("$A$",A,N);label("$B$",B,N);label("$C$",C,S);label("$D$",D,S);label("$X$",X,W);
label("$P$",P,N);label("$Q$",Q,S);label("$M$",M,E);label("$N$",Nn,E);
pair u=unit(Q-P),nrm=rotate(90)*u;
for(pair m: new pair[]{(P+M)/2,(M+Nn)/2,(Nn+Q)/2}) draw((m-0.3*nrm)--(m+0.3*nrm),blue);'''
b.add(1782611,29,r'''Lines $AB$ and $DC$ are parallel, and the transversals $AC$ and $BD$ intersect at a point $X$ between the two lines so that $\dfrac{AX}{CX}=\dfrac57$. Points $P$ and $Q$ lie on segments $AB$ and $DC$, respectively. Segment $PQ$ intersects the transversals $BD$ and $AC$ at points $M$ and $N$, respectively, so that $PM=MN=NQ$. What is the ratio $\dfrac{AP}{BP}$? Express your answer as a common fraction.''',
r'''Put $X$ at the origin with the lines $AB$ and $DC$ horizontal: $AB$ is the line $y=5$ and $DC$ the line $y=-7$ (distances in the ratio $AX:XC=5:7$). The dilation about $X$ with factor $-\dfrac75$ maps $A$ to $C$ and $B$ to $D$, so write $A=(a,5)$, $B=(b,5)$, $C=\left(-\dfrac{7a}{5},-7\right)$, $D=\left(-\dfrac{7b}{5},-7\right)$.

The points of $PQ$ that divide it into three equal parts lie at heights $5-\dfrac{12}{3}=1$ and $5-\dfrac{24}{3}=-3$. The point of $BD$ at height $1$ is $M=\left(\dfrac b5,1\right)$ and the point of $AC$ at height $-3$ is $N=\left(-\dfrac{3a}{5},-3\right)$. Let $P=(p,5)$ and let $d$ be the horizontal step from $P$ to $M$ (equal to the step from $M$ to $N$):
\[
p+d=\dfrac b5,\qquad p+2d=-\dfrac{3a}{5}\quad\Longrightarrow\quad d=-\dfrac{3a+b}{5},\quad p=\dfrac{3a+2b}{5}.
\]
'''+asy(fig,'6cm')+r'''
So $P=\dfrac{3A+2B}{5}$, which divides $AB$ with $AP=\dfrac25AB$ and $BP=\dfrac35AB$. Hence $\dfrac{AP}{BP}=\boxed{\dfrac23}$. (Then $Q=\dfrac{6C+D}{7}$ lies on segment $DC$, so the configuration exists; in the figure $a=-3$, $b=4$.)''',
'Parallel lines|Similarity|Coordinate geometry|Dilations and homothety|Ratios, proportions, and variation',5,
source=src('MATHCOUNTS',2017,'State',29,rnd='Sprint'),
note='The post writes "AX CX = 5 7"; read as AX/CX = 5/7.')
b.add(1782611,30,r'''Suppose that $a$ is a number such that the system of equations
\[
|2x|-y=5,\qquad x-|2y+2|=a
\]
has an odd number of distinct solutions. What is the product of all possible values of $a$?''',
r'''From the first equation $y=2|x|-5$, so $2y+2=4|x|-8$ and the second equation becomes
\[
g(x):=x-\bigl|4|x|-8\bigr|=a .
\]
Each solution $x$ gives exactly one solution $(x,y)$ of the system, so we count solutions of $g(x)=a$. The function $g$ is piecewise linear:
\[
g(x)=\begin{cases}5x+8,&x\le-2,\\-3x-8,&-2\le x\le0,\\5x-8,&0\le x\le2,\\-3x+8,&x\ge2,\end{cases}
\qquad g(-2)=-2,\ g(0)=-8,\ g(2)=2 .
\]
So $g$ rises to $-2$, falls to $-8$, rises to $2$ and then falls again. Counting intersections with the horizontal line at height $a$:
\begin{itemize}
\item $a>2$: $0$ solutions; $a=2$: $1$ solution ($x=2$);
\item $-2<a<2$: $2$ solutions (one in $(0,2)$, one in $(2,\infty)$);
\item $a=-2$: $3$ solutions ($x=-2$ and one on each side of $2$);
\item $-8<a<-2$: $4$ solutions; $a=-8$: $3$ solutions ($x=0$, one with $x<-2$, one with $x>2$);
\item $a<-8$: $2$ solutions.
\end{itemize}
The number of solutions is odd exactly for $a\in\{2,-2,-8\}$, and the product is $2\cdot(-2)\cdot(-8)=\boxed{32}$.''',
'Absolute value|Systems of linear equations|Piecewise functions|Casework',5,
source=src('MATHCOUNTS',2017,'State',30,rnd='Sprint'))
fig=r'''import graph;
real f(real x){return abs(x)<=1 ? x^2 : 2-x^2;}
real k=1/5;
draw((-2,0)--(2,0),gray,Arrow);draw((0,-1.4)--(0,1.6),gray,Arrow);
draw(graph(f,-1.8,1.8,n=721),linewidth(0.9));
draw((-1,1)--(1,1),dashed+gray);
draw((-1.9,k)--(1.9,k),blue);
pair A=(-sqrt(9/5),k),B=(-sqrt(1/5),k),C=(sqrt(1/5),k),D=(sqrt(9/5),k);
dot(A);dot(B);dot(C);dot(D);
label("$A$",A,NW);label("$B$",B,NE);label("$C$",C,NW);label("$D$",D,NE);
label("$y=1$",(1,1),E,gray);label("$x$",(2,0),E);label("$y$",(0,1.6),N);'''
b.add(1782611,8,r'''An M-shaped curve is created by graphing the parabola $y=x^2$ in the coordinate plane and then reflecting the part of the parabola that is above the line $y=1$ across the line $y=1$. There is a horizontal line that intersects the M-shaped curve at four points $A$, $B$, $C$ and $D$ so that $AB=BC=CD$. What is the distance $AB$? Express your answer as a common fraction in simplest radical form.''',
r'''The M-shaped curve is $y=x^2$ for $|x|\le1$ and $y=2-x^2$ for $|x|\ge1$ (reflecting $y$ across $y=1$ replaces $y$ by $2-y$). A horizontal line $y=k$ with $0<k<1$ meets it at four points: $x=\pm\sqrt k$ on the inner part and $x=\pm\sqrt{2-k}$ on the reflected parts.
'''+asy(fig,'6cm')+r'''
In order, $A=-\sqrt{2-k}$, $B=-\sqrt k$, $C=\sqrt k$, $D=\sqrt{2-k}$ (as $x$-coordinates). $BC=2\sqrt k$ and $AB=\sqrt{2-k}-\sqrt k$. The condition $AB=BC$ gives
\[
\sqrt{2-k}=3\sqrt k\ \Longrightarrow\ 2-k=9k\ \Longrightarrow\ k=\dfrac15 .
\]
Then $AB=2\sqrt{\dfrac15}=\dfrac{2}{\sqrt5}=\boxed{\dfrac{2\sqrt5}{5}}$.''',
'Parabolas|Reflections|Coordinate geometry|Radicals',4,
source=src('MATHCOUNTS',2017,'State',8,rnd='Target'),
note='Part number 08 is Target problem 8; parts 26, 29, 30 are Sprint problems. The line y = 1 itself meets the curve in only two points, so k < 1.')

# ---------------- 1771440 dining hall tables
b.add(1771440,1,r'''A dorm dining hall has three tables. Currently, one student is seated at one table, two are seated at another and three are seated at the remaining table. Each student who enters the dining hall picks a table to join with probability proportional to the number of students already seated at the table. Terri enters the dining hall and sits at a table. Ursula then enters the dining hall and sits at a table. What is the probability that there is now a table at which at least four students are seated? Express your answer as a common fraction.''',
r'''Call the tables $T_1,T_2,T_3$ with $1,2,3$ students. Terri joins them with probabilities $\dfrac16,\dfrac26,\dfrac36$.
\begin{itemize}
\item Terri joins $T_3$ (probability $\dfrac12$): $T_3$ already has $4$ students.
\item Terri joins $T_2$ (probability $\dfrac13$): the tables have $1,3,3$ students out of $7$, and we need Ursula to join one of the tables with $3$: probability $\dfrac67$.
\item Terri joins $T_1$ (probability $\dfrac16$): the tables have $2,2,3$, and Ursula must join the table with $3$: probability $\dfrac37$.
\end{itemize}
The total probability is
\[
\dfrac12+\dfrac13\cdot\dfrac67+\dfrac16\cdot\dfrac37=\dfrac{7}{14}+\dfrac{4}{14}+\dfrac{1}{14}=\boxed{\dfrac67}.
\]
(Complementary check: no table reaches $4$ only if Terri sits at $T_2$ and Ursula at $T_1$, or Terri at $T_1$ and Ursula at $T_1$ or $T_2$: $\dfrac13\cdot\dfrac17+\dfrac16\cdot\dfrac47=\dfrac{1}{21}+\dfrac{2}{21}=\dfrac17$.)''',
'Probability|Conditional probability|Casework|Complementary probability',3,
source=src('MATHCOUNTS',2018,'School',None,rnd='Team'))

# ---------------- 1782703 a+b+c = ab+bc+ca with 1<a<b<c
b.add(1782703,1,r'''Find all real numbers $a,b,c$ with $1<a<b<c$ such that $a+b+c=ab+bc+ca$, or show that there are none.''',
r'''There are none. Since all three numbers exceed $1$,
\[
ab>a\cdot1=a,\qquad bc>b\cdot1=b,\qquad ca>c\cdot1=c .
\]
Adding, $ab+bc+ca>a+b+c$, so the equation can never hold. Hence $\boxed{\text{there is no solution}}$. (In fact only $a,b,c>1$ is needed, not the ordering.) $\blacksquare$''',
'Inequalities|Proof by contradiction',2,
note='The post says "solve if possible"; it is impossible for any reals greater than 1, which the record proves.')

# ---------------- 1782744 floor(floor(x)/n) = floor(x/n)
b.add(1782744,1,r'''Let $x$ be a real number and $n$ a positive integer. Prove that
\[
\left\lfloor\dfrac{\lfloor x\rfloor}{n}\right\rfloor=\left\lfloor\dfrac{x}{n}\right\rfloor .
\]''',
r'''Let $m=\left\lfloor\dfrac xn\right\rfloor$, an integer with $m\le\dfrac xn<m+1$, i.e.\ $mn\le x<(m+1)n$.

Since $mn$ is an integer and $mn\le x$, we have $mn\le\lfloor x\rfloor$ (the floor is the largest integer not exceeding $x$). Also $\lfloor x\rfloor\le x<(m+1)n$. Hence
\[
mn\le\lfloor x\rfloor<(m+1)n\quad\Longrightarrow\quad m\le\dfrac{\lfloor x\rfloor}{n}<m+1,
\]
so $\left\lfloor\dfrac{\lfloor x\rfloor}{n}\right\rfloor=m=\left\lfloor\dfrac xn\right\rfloor$. $\blacksquare$''',
'Floor and ceiling functions|Inequalities',3,
note='The square brackets of the post are the floor function.')

# ---------------- 1782697 BdMO 2014 Dhaka 6, repaired data
fig=r'''real a=13,b=9,c=11;
pair B=(0,0),C=(a,0);
real xa=(a^2+c^2-b^2)/(2a);pair A=(xa,sqrt(c^2-xa^2));
real s=(a+b+c)/2;real K=2*sqrt(s*(s-a)*(s-b)*(s-c));
pair Oa=(b*B+c*C)/(b+c),Ob=(c*C+a*A)/(a+c),Oc=(b*B+a*A)/(a+b);
draw(circle(Oa,K/(b+c)),blue);draw(circle(Ob,K/(a+c)),heavygreen);draw(circle(Oc,K/(a+b)),red);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--Oa,dashed);
pair T1=B+dot(Oa-B,unit(A-B))*unit(A-B),T2=C+dot(Oa-C,unit(A-C))*unit(A-C);
draw(Oa--T1,blue+dashed);draw(Oa--T2,blue+dashed);
dot(Oa);dot(Ob);dot(Oc);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);
label("$O_1$",Oa,S);label("$O_2$",Ob,NE);label("$O_3$",Oc,NW);'''
b.add(1782697,1,r'''In an acute triangle $ABC$, a circle of radius $66$ has its diameter on side $BC$ and touches sides $AB$ and $AC$. Similarly, a circle of radius $55$ has its diameter on side $CA$ and touches $AB$ and $BC$, and a circle of radius $60$ has its diameter on side $AB$ and touches $BC$ and $CA$. What is the radius of the incircle of triangle $ABC$?''',
r'''Let $a=BC$, $b=CA$, $c=AB$, let $K$ be twice the area of $ABC$, and let $O_1$ be the centre of the first circle, on $BC$. Since the circle touches $AB$ and $AC$, its radius $66$ is the distance from $O_1$ to both lines. Splitting the triangle along $AO_1$,
\[
K=2[ABO_1]+2[AO_1C]=66\,c+66\,b,\qquad\text{so}\qquad b+c=\dfrac{K}{66}.
\]
'''+asy(fig,'6.5cm')+r'''
In the same way $c+a=\dfrac{K}{55}$ and $a+b=\dfrac{K}{60}$. Adding,
\[
2(a+b+c)=K\left(\dfrac1{66}+\dfrac1{55}+\dfrac1{60}\right)=K\cdot\dfrac{10+12+11}{660}=\dfrac{K}{20}.
\]
The inradius $r$ satisfies $K=r(a+b+c)$, so
\[
r=\dfrac{K}{a+b+c}=\boxed{40}.
\]
(Such a triangle exists: the three equations give $a:b:c=13:9:11$, an acute triangle, and each circle's diameter lies inside its side.)

\emph{Remark on the original data.} With radii $18$ on $BC$, $6$ on $CA$ and $9$ on $AB$, the same equations give $b+c=\dfrac K{18}$, $c+a=\dfrac K6$, $a+b=\dfrac K9$ and $a+b+c=\dfrac K6$, hence $b=0$: no such triangle exists (the formula would give $r=6$).''',
'Incircles and incentres|Tangents|Circles|Area decomposition|Triangles',5,
source=src('Bangladesh Mathematical Olympiad',2014,'Dhaka Regional',6),
note='BdMO 2014 Dhaka regional, problem 6. The posted radii 18 (on BC), 6 (on AC) and 9 (on AB) are impossible: they force CA = 0 (shown in the solution; the intended answer was presumably r = 6). The radii were changed to 66, 55, 60, which give a genuine acute triangle with sides in the ratio 13:9:11 and inradius 40 (checked with coordinates, including that each diameter lies within its side).')

# ---------------- 1782692 BdMO 2014 Dhaka 5
b.add(1782692,1,r'''A sequence satisfies $a_1=2015$ and
\[
\dfrac{a_1+a_2+\cdots+a_n}{a_n}=n^2\quad\text{for every } n>1 .
\]
Find $a_{2014}$.''',
r'''Let $S_n=a_1+\cdots+a_n$, so $S_n=n^2a_n$ for $n\ge2$; this also holds for $n=1$. Then for $n\ge2$
\[
a_n=S_n-S_{n-1}=n^2a_n-(n-1)^2a_{n-1}\ \Longrightarrow\ (n^2-1)a_n=(n-1)^2a_{n-1}\ \Longrightarrow\ a_n=\dfrac{n-1}{n+1}\,a_{n-1}.
\]
Multiplying these relations for $n=2,\dots,N$ telescopes:
\[
a_N=a_1\cdot\dfrac13\cdot\dfrac24\cdot\dfrac35\cdots\dfrac{N-1}{N+1}=a_1\cdot\dfrac{1\cdot2}{N(N+1)}=\dfrac{2a_1}{N(N+1)}.
\]
Hence $a_{2014}=\dfrac{2\cdot2015}{2014\cdot2015}=\boxed{\dfrac{1}{1007}}$.''',
'Recurrence relations|Sequences and series|Telescoping sums',4,
source=src('Bangladesh Mathematical Olympiad',2014,'Dhaka Regional',5))

# ---------------- 1782691 ace/bdf = m/n, m+n > 100
b.add(1782691,1,r'''Positive integers $a,b,c,d,e,f$ satisfy $a+b=c+d=e+f=101$, and positive integers $m,n$ satisfy $\dfrac{ace}{bdf}=\dfrac mn$. Prove that $m+n>100$.''',
r'''From $\dfrac{ace}{bdf}=\dfrac mn$ we get $n\cdot ace=m\cdot bdf$. Work modulo the prime $101$. Since $b=101-a$, $d=101-c$, $f=101-e$,
\[
bdf\equiv(-a)(-c)(-e)=-ace\pmod{101}.
\]
So $n\cdot ace\equiv-m\cdot ace$, i.e.
\[
ace\,(m+n)\equiv0\pmod{101}.
\]
Each of $a,c,e$ lies between $1$ and $100$, so none is divisible by the prime $101$, and neither is their product. Hence $101\mid m+n$, and as $m+n>0$, $m+n\ge101>100$. $\blacksquare$

(The fraction $\dfrac mn$ need not be in lowest terms for this argument.)''',
'Remainders and congruences|Prime numbers|Divisibility',4)

# ---------------- 1782537 right triangle with leg 11
fig=r'''pair C=(0,0),B=(60,0),A=(0,11);
draw(A--B--C--cycle,linewidth(0.9));
draw((0,2)--(2,2)--(2,0));
label("$A$",A,N);label("$B$",B,E);label("$C$",C,SW);
label("$11$",(A+C)/2,W);label("$60$",(B+C)/2,S);label("$61$",(A+B)/2,NE);'''
b.add(1782537,1,r'''The side lengths of a right triangle are positive integers, and one of its legs has length $11$. Find the perimeter of the triangle.''',
r'''Let the other leg be $b$ and the hypotenuse $c$. Then $c^2-b^2=11^2=121$, so
\[
(c-b)(c+b)=121 .
\]
Here $0<c-b<c+b$, and since $121=11^2$ with $11$ prime, the only factorisation with the smaller factor first is $1\cdot121$. Thus $c-b=1$, $c+b=121$, giving $c=61$, $b=60$.
'''+asy(fig,'7cm')+r'''
The triangle is $11,60,61$ and its perimeter is $11+60+61=\boxed{132}$.''',
'Right triangles|Pythagorean theorem|Pythagorean triples|Difference of squares|Diophantine equations',3)

# ---------------- 1782307 BdMO 2014 Dhaka 2, f(f(x)) = x^2+2
b.add(1782307,1,r'''The function $f$ takes positive integers to positive integers, is strictly increasing (if $a>b$ then $f(a)>f(b)$), and satisfies $f(f(x))=x^2+2$ for every positive integer $x$. Find $f(6)$.''',
r'''Let $f(1)=k$. Then $f(k)=f(f(1))=3$.
\begin{itemize}
\item $k=1$ is impossible: then $f(1)=1$ and $f(f(1))=1\ne3$.
\item $k\ge3$ is impossible: a strictly increasing function on the positive integers satisfies $f(m)>f(1)$ for $m>1$, so $f(k)>f(1)=k\ge3$, contradicting $f(k)=3$.
\end{itemize}
Hence $f(1)=2$, and then
\[
f(2)=f(f(1))=1^2+2=3,\quad f(3)=f(f(2))=2^2+2=6,\quad f(6)=f(f(3))=3^2+2=11 .
\]
So $f(6)=\boxed{11}$.''',
'Functional equations|Functions|Logical deduction',4,
source=src('Bangladesh Mathematical Olympiad',2014,'Dhaka Regional',2))

# ---------------- 1781234 water tanks, 7/3 corrected to 7/8
b.add(1781234,1,r'''Two water tanks are being filled. Each one starts with $100$ litres of water. The first tank fills at the rate of $15$ litres per minute and the second at the rate of $20$ litres per minute. After how many minutes will the first tank contain $\dfrac78$ as much water as the second tank?

(a) $5$ minutes \quad (b) $6$ minutes \quad (c) $7$ minutes \quad (d) $8$ minutes''',
r'''After $t$ minutes the tanks contain $100+15t$ and $100+20t$ litres. We need
\[
100+15t=\dfrac78(100+20t)\ \Longrightarrow\ 800+120t=700+140t\ \Longrightarrow\ 20t=100\ \Longrightarrow\ t=5 .
\]
Check: after $5$ minutes the tanks hold $175$ and $200$ litres, and $\dfrac{175}{200}=\dfrac78$. The answer is \textbf{(a)} $\boxed{5\text{ minutes}}$.

(As posted, with $\dfrac73$ instead of $\dfrac78$, the equation $300+45t=700+140t$ gives $t=-\dfrac{80}{19}<0$: the first tank always holds less water than the second, so it can never hold $\dfrac73$ times as much.)''',
'Rates|Linear equations|Fractions',2,
note='The posted ratio 7/3 is impossible (the first tank always holds less than the second); with 7/8 the answer is choice (a), 5 minutes, so 7/3 is taken as a typo for 7/8. The record uses 7/8 and explains the change.')

# ---------------- 1568275 three workers
b.add(1568275,1,r'''Three workers have to do a certain job. The first worker can finish the job alone in $8$ hours, and each of the other two can finish it alone in $4$ hours. How long will it take the three workers to finish the job working together?''',
r'''In one hour the workers do $\dfrac18$, $\dfrac14$ and $\dfrac14$ of the job, together
\[
\dfrac18+\dfrac14+\dfrac14=\dfrac58
\]
of the job. So the whole job takes $1\div\dfrac58=\dfrac85$ hours, that is $\boxed{\dfrac85\text{ hours}=1\text{ hour }36\text{ minutes}}$.''',
'Work and rates|Fractions',2)

# ---------------- 1782298 BdMO 2014 Dhaka 1, digits 8
b.add(1782298,1,r'''How many times does the digit $8$ appear in the product $999999999\times123456789$?''',
r'''Since $999999999=10^9-1$,
\[
999999999\times123456789=123456789\cdot10^9-123456789=123456788\,876543211 .
\]
(Subtracting $123456789$ from $123456789000000000$: the last nine digits become $10^9-123456789=876543211$ and the first nine digits decrease by $1$, from $123456789$ to $123456788$.) The digits are $1,2,3,4,5,6,7,8,8,8,7,6,5,4,3,2,1,1$, so the digit $8$ appears $\boxed{3}$ times.''',
'Place value|Whole-number operations|Digits and bases',2,
source=src('Bangladesh Mathematical Olympiad',2014,'Dhaka Regional',1))

# ---------------- 1781571 rearranging 2335142
b.add(1781571,1,r'''\begin{enumerate}
\item[(a)] How many distinct $7$-digit numbers can be made by rearranging the digits of $2335142$?
\item[(b)] How many distinct $5$-digit numbers can be made using five of these seven digits (each digit used at most as often as it occurs in $2335142$)?
\end{enumerate}''',
r'''The digits are $1,2,2,3,3,4,5$: the digits $2$ and $3$ occur twice and $1,4,5$ once. There is no $0$, so every arrangement is a genuine number.

(a) The number of arrangements of a multiset is $\dfrac{7!}{2!\,2!}=\dfrac{5040}{4}=\boxed{1260}$.

(b) Classify the five chosen digits by how many repeated pairs they contain.
\begin{itemize}
\item Five different digits: they must be $1,2,3,4,5$, giving $5!=120$ numbers.
\item Exactly one pair ($22$ or $33$) and three other different digits chosen from the remaining four values: $2\cdot\dbinom43=8$ choices of digits, each with $\dfrac{5!}{2!}=60$ arrangements, giving $480$.
\item Both pairs $22$, $33$ and one of $1,4,5$: $3$ choices, each with $\dfrac{5!}{2!\,2!}=30$ arrangements, giving $90$.
\end{itemize}
The total is $120+480+90=\boxed{690}$.''',
'Multiset permutations|Casework|Digit problems',3,
note='Part (b) is the post\'s "challenge" (5-digit numbers from the same 7 digits). Both counts were checked by brute force.')

# ---------------- 1782185 1/x+1/y=1/7 and 1/m+1/n=2/15
b.add(1782185,1,r'''Find the sum of the $y$-coordinates of all integer solutions $(x,y)$ of
\[
\dfrac1x+\dfrac1y=\dfrac17 .
\]''',
r'''Multiplying by $7xy$ (with $x,y\ne0$) gives $7y+7x=xy$, i.e.\ $xy-7x-7y=0$, and adding $49$:
\[
(x-7)(y-7)=49 .
\]
(Note the sign: the constant on the right is $+49$, not $-49$.) The integer factorisations of $49$ are $1\cdot49$, $7\cdot7$, $49\cdot1$, $(-1)(-49)$, $(-7)(-7)$, $(-49)(-1)$, giving
\[
(x,y)=(8,56),\ (14,14),\ (56,8),\ (6,-42),\ (0,0),\ (-42,6).
\]
The pair $(0,0)$ must be discarded, since $\dfrac10$ is undefined. The remaining $y$-values are $56,14,8,-42,6$, with sum $\boxed{42}$.''',
'Diophantine equations|Factoring|Rational equations',3,
note='The poster obtains 42 but writes (x-7)(y-7) = -49 and includes y = 0; the solution corrects the sign and excludes (0,0) (which contributes 0, so the sum is unchanged).')
b.add(1782185,2,r'''Positive integers $m$ and $n$ satisfy $m>n$, $m$ is not a multiple of $n$, and
\[
\dfrac1m+\dfrac1n=\dfrac2{15}.
\]
Find $m+n$.''',
r'''Clearing denominators, $15n+15m=2mn$. Multiply by $2$ and add $225$ to factor:
\[
4mn-30m-30n+225=225\ \Longrightarrow\ (2m-15)(2n-15)=225 .
\]
(Working with $7.5$ as in $(m-7.5)(n-7.5)=56.25$ is the same equation divided by $4$; doubling avoids fractions.) Both factors are odd. They cannot both be negative: then $|2n-15|\le13$ and $|2m-15|\le13$, and the product would be at most $169<225$. So both are positive, with $2n-15<2m-15$:
\[
2n-15\in\{1,3,5,9\},\qquad (n,m)=(8,120),\ (9,45),\ (10,30),\ (12,20).
\]
In the first three pairs $m$ is a multiple of $n$ ($120=15\cdot8$, $45=5\cdot9$, $30=3\cdot10$); only $(m,n)=(20,12)$ remains. So $m+n=\boxed{32}$.''',
'Diophantine equations|Factoring|Factors and multiples',4,
note='The post stops at (m-7.5)(n-7.5) = 56.25; the solution doubles to integer factors.')

# ---------------- 1746417 insphere of regular tetrahedron edge 1
fig=r'''real h=sqrt(2/3);
pair A=(0,0),M=(sqrt(3)/2,0),D=(sqrt(3)/3,h),G=(sqrt(3)/3,0);
real r=h/4;pair I=(sqrt(3)/3,r);
draw(A--M--D--cycle,linewidth(0.9));
draw(D--G,dashed);
draw(circle(I,r),blue);
pair T=M+dot(I-M,unit(D-M))*unit(D-M);
draw(I--T,blue+dashed);dot(I);dot(G);dot(T);
draw((G+(0.03,0))--(G+(0.03,0.03))--(G+(0,0.03)));
label("$A$",A,SW);label("$M$",M,SE);label("$D$",D,N);label("$G$",G,S);label("$I$",I,W);label("$r$",(I+T)/2,NE);'''
b.add(1746417,1,r'''What is the radius of the largest sphere that fits inside a regular tetrahedron with edge length $1$?''',
r'''The largest sphere is the inscribed sphere, tangent to all four faces; its centre $I$ is the centre of the tetrahedron. Joining $I$ to the four vertices splits the tetrahedron into four pyramids, each with a face as base and height $r$. So
\[
V=\dfrac13\,r\cdot(\text{total surface area}).
\]
For edge $1$: each face has area $\dfrac{\sqrt3}{4}$, so the surface area is $\sqrt3$. The height of the tetrahedron is $DG$, where $G$ is the centroid of the base $ABC$ and $AG=\dfrac23\cdot\dfrac{\sqrt3}{2}=\dfrac{\sqrt3}{3}$, so $DG=\sqrt{1-\dfrac13}=\sqrt{\dfrac23}=\dfrac{\sqrt6}{3}$. The volume is $V=\dfrac13\cdot\dfrac{\sqrt3}{4}\cdot\dfrac{\sqrt6}{3}=\dfrac{\sqrt2}{12}$. Hence
\[
r=\dfrac{3V}{\sqrt3}=\dfrac{\sqrt2}{4\sqrt3}=\boxed{\dfrac{\sqrt6}{12}}.
\]
The figure shows the cross-section through the apex $D$, the vertex $A$ and the midpoint $M$ of $BC$; the sphere meets it in a circle tangent to $AM$ (in the base) and to $DM$ (in the face $DBC$, which is perpendicular to this plane).
'''+asy(fig,'5cm')+r'''
Equivalently, $r=\dfrac14DG$: the centre divides each height in the ratio $3:1$.''',
'Pyramids|Spheres|Volume|Surface area|Solid geometry',4,
note='"Regular triangular pyramid with base length 1" does not fix the height; it is read as a regular tetrahedron with edge 1 (the usual intended meaning). The radius was checked with coordinates (distance from the centroid to each face).')

# ---------------- 1782144 Gina's tiles
b.add(1782144,1,r'''Gina lays square tiles on a floor. She begins with $1$ tile in a corner of the room. She adds $3$ tiles to form a $2\times2$ square of tiles, then $5$ tiles to form a $3\times3$ square, and so on, until the whole floor is covered. The last time, she adds $25$ tiles. What is the size of the floor, in tiles?''',
r'''Going from an $(n-1)\times(n-1)$ square to an $n\times n$ square adds $n^2-(n-1)^2=2n-1$ tiles. The last step adds $25=2n-1$ tiles, so $n=13$. The floor is a $\boxed{13\times13}$ square of tiles, using $169$ tiles in all. (Check: $1+3+5+\cdots+25=13^2=169$.)''',
'Perfect squares|Pattern recognition|Sequences and series',1)

# ---------------- 1782143 flagpoles
b.add(1782143,1,r'''Flagpole $A$ is $6\dfrac35$ metres high. Flagpole $C$ is $\dfrac14$ higher than flagpole $A$ (that is, its height exceeds the height of $A$ by a quarter of the height of $A$), and flagpole $B$ is $\dfrac34$ the height of flagpole $C$. What is the height of flagpole $B$?''',
r'''Flagpole $A$ is $6\dfrac35=\dfrac{33}{5}$ m high. Flagpole $C$ is $1+\dfrac14=\dfrac54$ times as high:
\[
C=\dfrac54\cdot\dfrac{33}{5}=\dfrac{33}{4}\text{ m}.
\]
Then $B=\dfrac34\cdot\dfrac{33}{4}=\dfrac{99}{16}$ m, i.e.\ $\boxed{6\dfrac{3}{16}\text{ metres}}$.''',
'Fractions|Ratios, proportions, and variation',2,
note='"1/4 higher than flagpole A" is read as a quarter of A\'s height higher (the reading is stated in the question); the alternative "1/4 metre higher" would give B = 5.1375 m.')

# ---------------- 1781693 clock at 5:00
b.add(1781693,1,r'''What is the smaller angle between the hour hand and the minute hand of an analogue clock at $5{:}00$? Give a method that works for any time $h{:}m$.''',
r'''The $12$ hour marks are $\dfrac{360^\circ}{12}=30^\circ$ apart. At $5{:}00$ the minute hand points at $12$ and the hour hand at $5$, five marks away, so the angle is $5\cdot30^\circ=\boxed{150^\circ}$ (the other angle is $210^\circ$, which is larger).

In general, at $h{:}m$ the minute hand is $6m$ degrees past $12$ (it moves $360^\circ$ in $60$ minutes) and the hour hand is $30h+\dfrac m2$ degrees past $12$ (it moves $30^\circ$ per hour, i.e.\ $\dfrac12^\circ$ per minute). The angle between them is $\left|30h-\dfrac{11m}{2}\right|$, replaced by $360^\circ$ minus this value if it exceeds $180^\circ$. For $5{:}00$: $|150-0|=150^\circ$.''',
'Clock problems|Rates',1)

# ---------------- 1782031 MATHCOUNTS National 2015 Countdown, ribbons
fig=r'''pair u=(3/5,4/5);
fill((-6,0)--(26,0)--(26,4)--(-6,4)--cycle,paleyellow);
fill((-2.25,-3)--(12.75,-3)--(12.75,-3)+10.5/0.8*u--(-2.25,-3)+10.5/0.8*u--cycle,palecyan);
fill((0,0)--(15,0)--(18,4)--(3,4)--cycle,mediumgray);
draw((-6,0)--(26,0));draw((-6,4)--(26,4));
draw((-2.25,-3)--(-2.25,-3)+10.5/0.8*u);draw((12.75,-3)--(12.75,-3)+10.5/0.8*u);
draw((0,0)--(15,0)--(18,4)--(3,4)--cycle,linewidth(1));
label("$15$",(7.5,0),S);label("$5$",(16.5,2),E);
label("width $4$",(-3,2));label("width $12$",(-2.25,-3)+10.5/0.8*u+(6,0.6),N);'''
b.add(1782031,1,r'''Two ribbons, of widths $4$ mm and $12$ mm, are laid on top of each other, crossing to form a parallelogram (their overlap). What is the perimeter of the parallelogram, in millimetres, if its area is $60\text{ mm}^2$?''',
r'''Each pair of opposite sides of the parallelogram lies along the two edges of one ribbon, so the distance between those sides is that ribbon's width.

Take as base a side lying along an edge of the $4$ mm ribbon; the corresponding height is $4$, so this side has length $\dfrac{60}{4}=15$. Take as base a side along an edge of the $12$ mm ribbon; the height is $12$, so this side has length $\dfrac{60}{12}=5$.
'''+asy(fig,'7cm')+r'''
The perimeter is $2(15+5)=\boxed{40}$ mm. (The ribbons cross at an angle $\theta$ with $\sin\theta=\dfrac{60}{15\cdot5}=\dfrac45$, which is possible; the figure is drawn with this angle.)''',
'Parallelograms|Lengths, perimeter, and area',3,
source=src('MATHCOUNTS',2015,'National',None,rnd='Countdown'),
note='The figure is in a missing attachment, but the text determines the configuration (the overlap of two straight ribbons).')

# ---------------- 1781575 Protik's village
b.add(1781575,1,r'''There are $140$ houses in Protik's village, numbered $1,2,3,\dots,140$. On the first day Protik took chocolates at the houses whose numbers are divisible by $4$. The next day he ate noodles at the houses whose numbers are divisible by $10$. Then he went to all the houses he had not yet visited and had ice cream. At how many houses did he have ice cream?''',
r'''Count the houses he visited on the first two days, by inclusion-exclusion. Multiples of $4$: $\left\lfloor\dfrac{140}{4}\right\rfloor=35$. Multiples of $10$: $14$. Multiples of both, i.e.\ of $\operatorname{lcm}(4,10)=20$: $7$. So he visited $35+14-7=42$ houses on the first two days, and he had ice cream at
\[
140-42=\boxed{98}
\]
houses. ($42$ is the number of houses he had \emph{already} visited.)''',
'Sets and inclusion–exclusion|Complementary counting|HCF and LCM|Factors and multiples',2,
note='The post asks "isn\'t the answer 42?"; 42 houses were visited on the first two days, and the answer is 140 - 42 = 98.')

# ---------------- 1781696 pigeonhole, hairs
b.add(1781696,1,r'''In Noakhali, every person has at least $1$ and at most $2018$ hairs. What is the minimum number of people that must live there so that we can be certain that at least two of them have the same number of hairs?''',
r'''There are $2018$ possible numbers of hairs ($1,2,\dots,2018$). With $2018$ people it is possible that all the numbers are different (one person with each number), so $2018$ people are not enough. With $2019$ people, by the pigeonhole principle two of them must have the same number of hairs. The minimum is $\boxed{2019}$.''',
'Pigeonhole principle',1,
note='The poster\'s answer 2019 is correct.')

# ---------------- 1445715 custom operation
b.add(1445715,1,r'''If $a\#b=a^2(7-b)$, what is the value of $(2\#5)\#3$?''',
r'''The symbol $\#$ is an operation defined by the formula. First $2\#5=2^2(7-5)=4\cdot2=8$. Then
\[
(2\#5)\#3=8\#3=8^2(7-3)=64\cdot4=\boxed{256}.
\]''',
'Custom operations|Order of operations',1,source=src('MATHCOUNTS',2017,'School',23,rnd='Sprint'),
note='The post writes "a (squared)(7-b)"; read as a^2(7-b).')

# ---------------- 1781238 two tanks
b.add(1781238,1,r'''Elmer and Elvin are emptying a full $800$-gallon tank while they fill an empty $1000$-gallon tank. They empty the first tank at the rate of $15$ gallons per minute and fill the second at the rate of $25$ gallons per minute. After how many minutes will both tanks contain the same number of gallons?''',
r'''After $t$ minutes the first tank holds $800-15t$ gallons and the second $25t$ gallons. Setting them equal,
\[
800-15t=25t\ \Longrightarrow\ 40t=800\ \Longrightarrow\ t=20 .
\]
After $\boxed{20}$ minutes both tanks hold $500$ gallons. (The difference $800$ shrinks by $15+25=40$ gallons every minute, so it vanishes after $\dfrac{800}{40}=20$ minutes.)''',
'Rates|Linear equations',1,
note='The starting states (first tank full, second empty) are stated explicitly.')

b.save()
