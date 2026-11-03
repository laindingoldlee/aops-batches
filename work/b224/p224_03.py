from qb import *
b=Bank('p224_03')

# ---------------- 1768394 Chinese remainder theorem
b.add(1768394,1,r'''\begin{enumerate}
\item[(a)] Let $m$ and $n$ be coprime positive integers. Prove the Chinese remainder theorem for two moduli: for any integers $a$ and $b$ there is an integer $x$ with $x\equiv a\pmod m$ and $x\equiv b\pmod n$, and any two such integers differ by a multiple of $mn$.
\item[(b)] Find the smallest positive integer that leaves remainder $2$ when divided by $3$, remainder $3$ when divided by $5$, and remainder $2$ when divided by $7$.
\end{enumerate}''',
r'''\textbf{(a) Existence.} Consider the $n$ numbers $a,\ a+m,\ a+2m,\ \dots,\ a+(n-1)m$, all $\equiv a\pmod m$. No two of them are congruent modulo $n$: if $a+sm\equiv a+tm\pmod n$ with $0\le s<t\le n-1$, then $n\mid(t-s)m$, and since $\gcd(m,n)=1$, $n\mid t-s$, impossible as $0<t-s<n$. So these $n$ numbers leave the $n$ different remainders $0,1,\dots,n-1$ modulo $n$, and one of them is $\equiv b\pmod n$.

\textbf{Uniqueness.} If $x$ and $y$ both work, then $m\mid x-y$ and $n\mid x-y$; since $m,n$ are coprime, $mn\mid x-y$. $\blacksquare$

\textbf{(b)} Applying (a) twice: the numbers $\equiv3\pmod5$ are $3,8,13,18,23,\dots$, and the first that is $\equiv2\pmod3$ is $8$; so $x\equiv8\pmod{15}$. The numbers $8,23,38,\dots$ are $\equiv1,2,\dots\pmod7$: $8\equiv1$ and $23\equiv2$. So $x\equiv23\pmod{105}$, and the smallest positive solution is $\boxed{23}$. Check: $23=7\cdot3+2=4\cdot5+3=3\cdot7+2$.''',
'Chinese remainder theorem|Remainders and congruences|Divisibility',3,
note='The post asks what the Chinese remainder theorem is; the record asks for a proof of the two-modulus statement and the classical example of Sunzi (answer 23).')

# ---------------- 1768345 sum of n with 3^20 < n^2 < 53^3
b.add(1768345,1,r'''What is the sum of the integer values of $n$ such that $3^{20}<n^2<53^3$?''',
r'''Compare the bounds: $3^{20}=\left(3^{10}\right)^2=59049^2=3486784401$, while $53^3=148877$. So $3^{20}>53^3$, no integer $n$ satisfies $3^{20}<n^2<53^3$, and the sum of the (non-existent) values is the empty sum, $\boxed{0}$.

(The answer $0$ is robust: whatever the bounds, the condition depends only on $n^2$, so the integers satisfying it come in pairs $n,-n$ and always add up to $0$.)''',
'Exponents|Inequalities|Symmetry|Pairing and grouping',2,
note='As posted the lower bound 3^20 exceeds the upper bound 53^3, so no n qualifies; the record keeps the problem and notes that the sum is 0 for any bounds of this kind, by the pairing n, -n.')

# ---------------- 1752262 marathon P3 (P1 and P2 need missing images)
b.add(1752262,3,r'''In a room, $\dfrac25$ of the people are wearing gloves, and $\dfrac34$ of the people are wearing hats. What is the minimum number of people in the room wearing both a hat and a glove?

$\textbf{(A)}\ 3\qquad\textbf{(B)}\ 5\qquad\textbf{(C)}\ 8\qquad\textbf{(D)}\ 15\qquad\textbf{(E)}\ 20$''',
r'''Let there be $N$ people; $N$ must be a multiple of $5$ and of $4$, so of $20$. If $x$ people wear both, then by inclusion-exclusion the number wearing a hat or a glove is $\dfrac25N+\dfrac34N-x\le N$, so
\[
x\ge\dfrac25N+\dfrac34N-N=\dfrac{3}{20}N\ge\dfrac{3}{20}\cdot20=3 .
\]
With $N=20$: $8$ wear gloves and $15$ wear hats; if all $20-15=5$ people without hats wear gloves, exactly $8-5=3$ wear both. The minimum is $\boxed{\textbf{(A)}\ 3}$.''',
'Sets and inclusion–exclusion|Fractions|Bounding and extremal cases',3,source=src('AMC 8'),
note='Third problem of a "get close to 1000" game thread; P1 (gasoline price graph) and P2 (octagon of unit squares) depend on missing images and are dropped. The thread names AMC 8 as the source without a year.')

# ---------------- 1767081 Andy and Beth
b.add(1767081,1,r'''Andy and Beth play a game. Andy thinks of two numbers $a$ and $b$ and tells Beth the ordered pair $(a,b)$. Beth must find a different ordered pair of numbers $(c,d)$ such that $a+b=c+d$, $ab=cd$ and $a\ne d$. Beth wins if she completes this task; otherwise Andy wins. Prove that Andy always wins.''',
r'''Suppose $(c,d)$ satisfies $c+d=a+b$ and $cd=ab$. Then for every $t$,
\[
(t-c)(t-d)=t^2-(c+d)t+cd=t^2-(a+b)t+ab=(t-a)(t-b).
\]
Putting $t=c$ gives $(c-a)(c-b)=0$, so $c=a$ or $c=b$.
\begin{itemize}
\item If $c=a$, then $d=(a+b)-c=b$, so $(c,d)=(a,b)$ is not a different pair.
\item If $c=b$, then $d=(a+b)-c=a$, which violates $a\ne d$.
\end{itemize}
So no admissible pair $(c,d)$ exists, whatever $(a,b)$ Andy chooses, and Andy always wins. $\blacksquare$''',
'Vieta\'s formulas|Quadratic equations|Proof by cases',2)

# ---------------- 1767962 nested radical equation
b.add(1767962,1,r'''How many real values of $x$ satisfy the equation
\[
\sqrt{3+\sqrt{3+\sqrt{3+x}}}=x\ ?
\]''',
r'''Let $g(t)=\sqrt{3+t}$ for $t\ge-3$; the equation is $g(g(g(x)))=x$. The left side is a square root, so $x\ge0$, and $g$ is strictly increasing.

If $g(x)>x$, then applying the increasing function $g$ gives $g(g(x))>g(x)>x$ and then $g(g(g(x)))>g(g(x))>x$, a contradiction. Likewise $g(x)<x$ leads to $g(g(g(x)))<x$. Hence every solution satisfies $g(x)=x$, i.e.\ $\sqrt{3+x}=x$, so $x^2-x-3=0$ with $x\ge0$, giving $x=\dfrac{1+\sqrt{13}}{2}$. Conversely this value satisfies $g(x)=x$ and hence the equation.

There is exactly $\boxed{1}$ real solution, $x=\dfrac{1+\sqrt{13}}{2}\approx2.30$.''',
'Radical equations|Functions|Quadratic equations|Proof by contradiction',4)

# ---------------- 1767197 reciprocals
b.add(1767197,1,r'''Find $x$ if $1$ minus the reciprocal of $1-x$ equals the reciprocal of $1-x$.''',
r'''The equation is $1-\dfrac{1}{1-x}=\dfrac{1}{1-x}$ with $x\ne1$. Then $1=\dfrac{2}{1-x}$, so $1-x=2$ and $x=\boxed{-1}$. Check: $\dfrac{1}{1-(-1)}=\dfrac12$ and $1-\dfrac12=\dfrac12$.''',
'Rational equations|Linear equations',1)

# ---------------- 1768268 median of a set with unknown s
b.add(1768268,1,r'''Let $Q=\{1.7,\ 1.1,\ 1.4,\ 2.1,\ 2.3,\ s\}$, where $s$ is a real number. What is the absolute difference between the greatest and least possible values of the median of $Q$? Express your answer as a decimal to the nearest hundredth.''',
r'''In increasing order the known values are $1.1,\ 1.4,\ 1.7,\ 2.1,\ 2.3$. With six numbers, the median is the average of the $3$rd and $4$th smallest.
\begin{itemize}
\item If $s\le1.4$, the $3$rd and $4$th values are $1.4$ and $1.7$: median $1.55$.
\item If $1.4\le s\le2.1$, they are $1.7$ and $s$, so the median is $\dfrac{1.7+s}{2}$, which lies between $1.55$ and $1.9$.
\item If $s\ge2.1$, they are $1.7$ and $2.1$: median $1.9$.
\end{itemize}
In every case the median is between $1.55$ and $1.9$, and both values occur. The difference is $1.9-1.55=\boxed{0.35}$.''',
'Median|Casework',2)

# ---------------- 1665584 odd coefficients, no rational root (alias)
b.add(1665584,1,r'''Show that if $a$, $b$ and $c$ are odd integers, the equation $ax^2+bx+c=0$ has no rational root.''',
r'''Suppose $x=\dfrac pq$ in lowest terms is a root; then $ap^2+bpq+cq^2=0$. Not both $p,q$ are even. If both are odd, all three terms are odd and their sum is odd; if exactly one is even, exactly one term is odd. Either way the sum is odd, not $0$. $\blacksquare$''',
'Parity|Polynomial roots|Proof by contradiction',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1767629 3^(3^(3^3)) mod 1000
b.add(1767629,1,r'''Find the remainder when $3^{3^{3^{3}}}$ is divided by $1000$.''',
r'''The tower means $3^{\left(3^{27}\right)}$. Compute powers of $3$ modulo $1000$:
\[
3^{10}=59049\equiv49,\quad 3^{20}\equiv49^2=2401\equiv401,\quad 3^{40}\equiv401^2\equiv801,\quad 3^{80}\equiv801^2\equiv601 .
\]
Then $3^{100}=3^{80}\cdot3^{20}\equiv601\cdot401=241001\equiv1\pmod{1000}$, so only the exponent $3^{27}$ modulo $100$ matters. Since $3^{20}\equiv401\equiv1\pmod{100}$,
\[
3^{27}\equiv3^{7}=2187\equiv87\pmod{100}.
\]
Hence $3^{3^{27}}\equiv3^{87}=3^{80}\cdot3^{7}\equiv601\cdot2187\equiv601\cdot187=112387\equiv\boxed{387}\pmod{1000}$.''',
'Modular exponentiation|Remainders and congruences|Euler\'s theorem and totient|Exponents',4,
note='The tower is read from the top down, 3^(3^(3^3)) = 3^(3^27).')

# ---------------- 1768109 orthodiagonal right trapezoid
fig=r'''real a=9,bb=4,h=6;
pair A=(0,0),B=(a,0),D=(0,h),C=(bb,h);
pair X=extension(A,C,B,D);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--C,blue);draw(B--D,blue);
draw((0.4,0)--(0.4,0.4)--(0,0.4));draw((0,h-0.4)--(0.4,h-0.4)--(0.4,h));
pair u=unit(C-X),v=unit(B-X);draw(X+0.4*u--X+0.4*u+0.4*v--X+0.4*v,blue);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);
label("$a$",(A+B)/2,S);label("$b$",(D+C)/2,N);label("$h$",(A+D)/2,W);'''
b.add(1768109,1,r'''In a right trapezoid $ABCD$, the bases are $AB=a$ and $DC=b$, and the leg $AD$ is perpendicular to both bases. The diagonals $AC$ and $BD$ are perpendicular. Prove that the altitude $AD$ equals $\sqrt{ab}$.''',
r'''Put $A=(0,0)$, $B=(a,0)$, $D=(0,h)$ and $C=(b,h)$, where $h=AD$.
'''+asy(fig,'5.5cm')+r'''
Then $\overrightarrow{AC}=(b,h)$ and $\overrightarrow{BD}=(-a,h)$, and the diagonals are perpendicular exactly when
\[
\overrightarrow{AC}\cdot\overrightarrow{BD}=-ab+h^2=0 ,
\]
that is, $h=\sqrt{ab}$. $\blacksquare$

With similar triangles instead: $\angle ABD=90^\circ-\angle BAC$ (the diagonals meet at a right angle) and $\angle DAC=90^\circ-\angle BAC$ (since $\angle DAB=90^\circ$), so the right triangles $DAB$ and $CDA$ are similar, and $\dfrac{AD}{AB}=\dfrac{DC}{DA}$, i.e.\ $h^2=ab$. (The figure uses $a=9$, $b=4$, $h=6$.)''',
'Trapezoids|Perpendicular lines|Similarity|Coordinate geometry|Diagonals',3,
note='The post asks for the formula and a proof; the record states the configuration (right angle at A and D) and proves h = sqrt(ab).')

# ---------------- 1767722 2015 MATHCOUNTS School Sprint 30 (26 needs the figure)
fig=r'''pair A=(0,0),B=(6,0),C=(0,8),D=(8,14),Ee=(14,6);
draw(A--B--C--cycle,linewidth(0.9));draw(B--C--D--Ee--cycle,linewidth(0.9));
draw(A--D,blue);draw(A--Ee,blue);draw(D--Ee,blue+linewidth(0.9));
draw((0.6,0)--(0.6,0.6)--(0,0.6));
label("$A$",A,SW);label("$B$",B,S);label("$C$",C,W);label("$D$",D,N);label("$E$",Ee,E);
label("$6$",(A+B)/2,S);label("$8$",(A+C)/2,W);label("$10$",C+0.3*(B-C),SW);'''
b.add(1767722,30,r'''Right triangle $ABC$ has legs $AB=6$ cm and $AC=8$ cm. Square $BCDE$ is drawn outside the triangle along the hypotenuse. What is the area of triangle $ADE$, in square centimetres?''',
r'''Place $A=(0,0)$, $B=(6,0)$, $C=(0,8)$. Then $\overrightarrow{BC}=(-6,8)$, and the perpendicular vector of the same length pointing away from $A$ is $(8,6)$. So the square has vertices $D=C+(8,6)=(8,14)$ and $E=B+(8,6)=(14,6)$.
'''+asy(fig,'5.5cm')+r'''
The area of triangle $ADE$ is
\[
\dfrac12\left|x_Dy_E-x_Ey_D\right|=\dfrac12\left|8\cdot6-14\cdot14\right|=\dfrac12\cdot148=\boxed{74}.
\]
Without coordinates: the distance from $A$ to line $DE$ equals the distance from $A$ to line $BC$ (the altitude $\dfrac{6\cdot8}{10}=4.8$) plus the side $10$ of the square, so $[ADE]=\dfrac12\cdot10\cdot14.8=74$.''',
'Squares|Right triangles|Lengths, perimeter, and area|Coordinate geometry|Pythagorean theorem',3,source=src('MATHCOUNTS',2015,'School',30,rnd='Sprint'),
note='Problem 26 of the same post (congruent right triangles and three squares "in the figure") depends on a missing figure and is dropped.')

# ---------------- 1766250 chocolate bars (inconsistent data repaired)
b.add(1766250,1,r'''Shi Ting's mother gives her $8$ chocolate bars on each day she practises the piano for $30$ minutes or more, and $5$ chocolate bars on each day she practises for less than $30$ minutes (she ``falls short of the $30$-minute mark''). She practises on $18$ days.
\begin{enumerate}
\item[(a)] Show that she cannot have earned a total of $53$ chocolate bars.
\item[(b)] Which totals are possible?
\item[(c)] If she earned $117$ chocolate bars, on how many days did she fall short of the $30$-minute mark?
\end{enumerate}''',
r'''Let $x$ be the number of days with at least $30$ minutes, so she fell short on $18-x$ days, with $0\le x\le18$. Her total is
\[
8x+5(18-x)=90+3x .
\]
\textbf{(a)} The total is at least $90$ (she gets at least $5$ bars on each of the $18$ days), so $53$ is impossible.

\textbf{(b)} The possible totals are $90+3x$ for $x=0,1,\dots,18$: the numbers $90,93,96,\dots,144$, i.e.\ the multiples of $3$ from $90$ to $144$.

\textbf{(c)} $90+3x=117$ gives $x=9$, so she fell short on $18-9=\boxed{9}$ days.''',
'Linear equations|Systems of linear equations|Inequalities',2,
note='The posted data are inconsistent: 18 days earn at least 5 x 18 = 90 bars, so 53 is impossible (8x + 5(18 - x) = 53 gives x = -37/3). The record asks to show this, lists the possible totals, and replaces the total by 117 (answer 9 days). "Fall short of the 30-minute mark" is explained as practising less than 30 minutes.')

# ---------------- 1767658 mathematics and history
b.add(1767658,1,r'''In a class, every student reads mathematics or history (or both). One quarter of the students who read mathematics also read history, and one third of the students who read history also read mathematics. What fraction of the class reads history?''',
r'''Let $x$ students read both subjects. Then $x$ is a quarter of the mathematics readers and a third of the history readers, so $4x$ read mathematics and $3x$ read history. By inclusion-exclusion the class has $4x+3x-x=6x$ students. The fraction reading history is $\dfrac{3x}{6x}=\boxed{\dfrac12}$.''',
'Sets and inclusion–exclusion|Venn diagrams|Fractions',2)

# ---------------- 1767474 finite arithmetico-geometric sum
b.add(1767474,1,r'''Find the value of
\[
\dfrac12+\dfrac{3}{2^2}+\dfrac{5}{2^3}+\dfrac{7}{2^4}+\cdots+\dfrac{45}{2^{23}} .
\]''',
r'''Let $S=\displaystyle\sum_{k=1}^{23}\dfrac{2k-1}{2^k}$. Then $\dfrac S2=\displaystyle\sum_{k=1}^{23}\dfrac{2k-1}{2^{k+1}}=\sum_{k=2}^{24}\dfrac{2k-3}{2^{k}}$, and subtracting,
\[
S-\dfrac S2=\dfrac12+\sum_{k=2}^{23}\dfrac{2}{2^k}-\dfrac{45}{2^{24}}=\dfrac12+\left(1-\dfrac{1}{2^{22}}\right)-\dfrac{45}{2^{24}} .
\]
So $\dfrac S2=\dfrac32-\dfrac{4}{2^{24}}-\dfrac{45}{2^{24}}=\dfrac32-\dfrac{49}{2^{24}}$ and
\[
S=3-\dfrac{49}{2^{23}}=\boxed{\dfrac{25165775}{8388608}}\approx2.99999416 .
\]''',
'Sequences and series|Geometric sequences|Telescoping sums|Summation',4,
note='The post is titled "inequalities" but asks for the value of the finite sum. Checked with exact fractions.')

# ---------------- 1766947 five congruent parts but not congruent
fig=r'''pair P(real a,real b,real c){ real x=(b^2+a^2-c^2)/(2*a); return (x,sqrt(b^2-x^2)); }
pair A1=(0,0),B1=(8,0),C1=P(8,6,4.5);
draw(A1--B1--C1--cycle,linewidth(0.9));
label("$8$",(A1+B1)/2,S);label("$6$",(A1+C1)/2,NW);label("$\dfrac92$",(B1+C1)/2,NE);
pair sh=(10.5,0);
pair A2=sh,B2=sh+(32/3,0),C2=sh+P(32/3,8,6);
draw(A2--B2--C2--cycle,linewidth(0.9));
label("$\dfrac{32}{3}$",(A2+B2)/2,S);label("$8$",(A2+C2)/2,NW);label("$6$",(B2+C2)/2,NE);'''
b.add(1766947,1,r'''Two triangles have five pairs of congruent parts (among their three sides and three angles) but are not congruent. Each triangle has a side of length $6$ and a side of length $8$. What is the length of the third side of each triangle?''',
r'''\textbf{The five parts are three angles and two sides.} If all three pairs of sides were congruent, the triangles would be congruent (SSS). So at most two pairs of sides are congruent, and the five pairs are two sides and all three angles. Hence the triangles are similar with some ratio $k\ne1$, say $k>1$: if the first triangle has sides $x\le y\le z$, the second has sides $kx\le ky\le kz$.

\textbf{Which sides are shared.} The side $kz$ is longer than every side of the first triangle, and $x$ is shorter than every side of the second. So the two common lengths are among $y,z$ and among $kx,ky$; since $kx<ky$, we need $y=kx$ and $z=ky$ (and $y<z$). The sides are therefore
\[
x,\ kx,\ k^2x\qquad\text{and}\qquad kx,\ k^2x,\ k^3x .
\]
\textbf{Use $6$ and $8$.} Both triangles contain $6$ and $8$. The first triangle's side $x$ is not in the second, and the second's side $k^3x$ is not in the first, so $\{kx,k^2x\}=\{6,8\}$: $kx=6$, $k^2x=8$, $k=\dfrac43$, $x=\dfrac92$ and $k^3x=\dfrac{32}{3}$.
'''+asy(fig,'8cm')+r'''
The triangles have sides $\dfrac92,6,8$ and $6,8,\dfrac{32}{3}$; both satisfy the triangle inequality ($\dfrac92+6>8$ and $6+8>\dfrac{32}{3}$), and their angles agree because the side ratios are $\dfrac43$. The third sides are $\boxed{\dfrac92\text{ and }\dfrac{32}{3}}$.''',
'Similarity|Congruence|Triangles|Geometric sequences|Triangle inequality',5,
note='The post omits "Two triangles have ... but are not congruent" as a statement of the problem; the record states it. The angle equalities were checked with the law of cosines.')

# ---------------- 1767337 four bugs on a square
fig=r'''pair A=(0,0),B=(4,0),C=(4,4),D=(0,4),O=(2,2);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--O,dashed);draw(B--O,dashed);draw(C--O,dashed);draw(D--O,dashed);
draw(A--(A+(1.6,0)),red+linewidth(1.1),Arrow(TeXHead));
draw(B--(B+(0,1.6)),red+linewidth(1.1),Arrow(TeXHead));
draw(C--(C+(-1.6,0)),red+linewidth(1.1),Arrow(TeXHead));
draw(D--(D+(0,-1.6)),red+linewidth(1.1),Arrow(TeXHead));
draw(arc(A,0.9,0,45));label("$45^\circ$",A+1.35*dir(22.5),fontsize(8pt));
dot(A);dot(B);dot(C);dot(D);dot(O);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);label("$O$",O,E);'''
b.add(1767337,1,r'''Four bugs sit at the vertices of a unit square. At the same moment each bug begins to crawl directly towards its counterclockwise neighbour, always heading straight at it, at a constant speed of $1$ unit per minute. How long does it take for the bugs to meet?

Also explain the following ``radial'' argument: each bug's velocity makes a $45^\circ$ angle with the line to the centre, so it approaches the centre at speed $\dfrac{1}{\sqrt2}$, and it starts at distance $\dfrac{1}{\sqrt2}$ from the centre.''',
r'''Label the bugs $A,B,C,D$ counterclockwise, so $A$ chases $B$, $B$ chases $C$, and so on.

\textbf{The bugs always form a square.} The situation is unchanged by a quarter turn about the centre $O$ that takes each bug to the next, so at every moment the four bugs are the vertices of a square centred at $O$ (shrinking and rotating).
'''+asy(fig,'4.5cm')+r'''
\textbf{Rate at which a side shrinks.} Bug $A$ moves straight towards $B$ at speed $1$. Bug $B$ moves towards $C$, which is perpendicular to $AB$ because the bugs form a square; so $B$'s motion does not change the distance $AB$ to first order. Hence the side length $AB$ decreases at the constant rate of $1$ unit per minute, from $1$ to $0$: the bugs meet after $\boxed{1\text{ minute}}$ (at the centre, after each has crawled $1$ unit along a spiral).

\textbf{The radial argument.} Each bug moves along a side of the current square, which makes a $45^\circ$ angle with the half-diagonal to the centre (shown for $A$). So the component of its velocity towards $O$ is $1\cdot\cos45^\circ=\dfrac{1}{\sqrt2}$ at every moment, and its distance to $O$ starts at half the diagonal, $\dfrac{\sqrt2}{2}=\dfrac{1}{\sqrt2}$. The distance to the centre therefore decreases at the constant rate $\dfrac1{\sqrt2}$, reaching $0$ after $\dfrac{1}{\sqrt2}\div\dfrac{1}{\sqrt2}=1$ minute. The line from a vertex to the centre in the posted solution represents this radial distance, not the actual spiral path; the sideways component of the velocity only rotates the square.''',
'Relative speed|Distance, rate, and time|Symmetry|Squares',4,
note='The post asks why the given solution works; the record asks for the time and for the explanation of the radial argument.')

# ---------------- 1766580 lattice points in a lattice triangle (Pick)
fig=r'''for(int i=0;i<=6;++i) for(int j=0;j<=4;++j) dot((i,j),gray(0.6)+linewidth(1.5));
pair A=(0,0),B=(6,0),C=(2,4);
draw(A--B--C--cycle,blue+linewidth(0.9));
pair[] I={(2,1),(3,1),(4,1),(5,1),(2,2),(3,2),(2,3)};
for(pair p:I) dot(p,red+linewidth(4));
pair[] Bd={(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(1,2),(2,4),(3,3),(4,2),(5,1)};
for(pair p:Bd) dot(p,blue+linewidth(4));
label("$(0,0)$",A,SW);label("$(6,0)$",B,SE);label("$(2,4)$",C,N);'''
b.add(1766580,1,r'''A triangle in the coordinate plane has its vertices at the lattice points $(x_1,y_1)$, $(x_2,y_2)$, $(x_3,y_3)$. Give formulas for the number $B$ of lattice points on its boundary and the number $I$ of lattice points strictly inside it. Use them to count the lattice points inside and on the triangle with vertices $(0,0)$, $(6,0)$ and $(2,4)$.''',
r'''\textbf{Boundary.} On the segment from $(x_1,y_1)$ to $(x_2,y_2)$, the lattice points are $(x_1,y_1)+\dfrac{t}{g}(x_2-x_1,\,y_2-y_1)$ for $t=0,1,\dots,g$, where $g=\gcd(|x_2-x_1|,|y_2-y_1|)$. Counting each vertex once,
\[
B=\gcd(|x_2-x_1|,|y_2-y_1|)+\gcd(|x_3-x_2|,|y_3-y_2|)+\gcd(|x_1-x_3|,|y_1-y_3|).
\]
\textbf{Interior.} The area is given by the shoelace formula,
\[
A=\dfrac12\left|x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)\right| ,
\]
and Pick's theorem $A=I+\dfrac B2-1$ for lattice polygons gives
\[
I=A-\dfrac B2+1,\qquad I+B=A+\dfrac B2+1 .
\]
\textbf{Example.} For $(0,0),(6,0),(2,4)$: $B=\gcd(6,0)+\gcd(4,4)+\gcd(2,4)=6+4+2=12$ and $A=\dfrac12\cdot6\cdot4=12$, so $I=12-6+1=\boxed{7}$ interior points and $\boxed{19}$ points inside or on the triangle.
'''+asy(fig,'5.5cm')+r'''
The figure shows the $12$ boundary points (blue) and the $7$ interior points (red).''',
'Pick\'s theorem|Lattice points|Shoelace formula|Coordinate geometry|HCF and LCM',3,
note='The post asks for the forgotten formula; the record gives the boundary count, the shoelace area and Pick\'s theorem, and adds a worked example (checked by brute force).')

# ---------------- 1767062 bread and bologna (alias)
b.add(1767062,1,r'''Mike and Joey bought identical loaves of bread and identical packages of bologna. Mike made sandwiches with $5$ slices of bologna each and had $4$ slices of bread left when he ran out of meat. Joey made sandwiches with $4$ slices of bologna each and had $4$ slices of meat left when he ran out of bread. Each sandwich uses $2$ slices of bread, and each boy used one loaf and one package. How many slices of bread were in each loaf?''',
r'''With $L$ slices of bread and $M$ of bologna: Mike made $s$ sandwiches with $M=5s$, $L=2s+4$; Joey made $j$ with $L=2j$, $M=4j+4$. Then $j=s+2$, $5s=4s+12$, $s=12$ and $L=\boxed{28}$.''',
'Systems of linear equations|Linear equations',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1767069 pyramid volume from slant height
fig=r'''pair d=(0.5,0.32);
real s=2*sqrt(7);
pair p0=(0,0),p1=(s,0),p2=p1+s*d,p3=s*d,O=(p0+p2)/2,M=(p1+p2)/2,apex=O+(0,sqrt(29));
draw(p0--p1--p2,linewidth(0.9));draw(p2--p3--p0,dashed);
draw(apex--p0,linewidth(0.9));draw(apex--p1,linewidth(0.9));draw(apex--p2,linewidth(0.9));draw(apex--p3,dashed);
draw(apex--O,dashed);draw(O--M,dashed);draw(apex--M,red+linewidth(0.9));
dot(O);dot(M,red);
label("$V$",apex,N);label("$O$",O,dir(200));label("$M$",M,SE,red);
label("$6$",apex+0.55*(M-apex),E,red);label("$h$",apex+0.5*(O-apex),W);
label("$\sqrt7$",O+0.25*(M-O),S,fontsize(9pt));'''
b.add(1767069,1,r'''A pyramid has a square base of area $28$ square feet. The slant height of the pyramid (the height of each triangular face, from the apex to the midpoint of a base edge) is $6$ feet. Find the volume of the pyramid.''',
r'''The base has side $\sqrt{28}=2\sqrt7$. Let $V$ be the apex, $O$ the centre of the base and $M$ the midpoint of a base edge (the figure uses the right-hand edge); then $OM=\sqrt7$ (half the side), $VM=6$ is the slant height, and $VO=h$ is the height, with a right angle at $O$.
'''+asy(fig,'5cm')+r'''
By the Pythagorean theorem, $h=\sqrt{6^2-(\sqrt7)^2}=\sqrt{29}$. The volume is
\[
\dfrac13\cdot28\cdot\sqrt{29}=\boxed{\dfrac{28\sqrt{29}}{3}}\ \text{cubic feet}\approx50.3 .
\]
The poster's value $\dfrac{28\sqrt{22}}{3}$ comes from treating $6$ as a lateral edge $VA$ (from the apex to a vertex): half the diagonal of the base is $\sqrt{14}$ and $\sqrt{36-14}=\sqrt{22}$. Slant height, however, means the height of a face.''',
'Pyramids|Volume|Pythagorean theorem|Squares',2,
note='The answer choices are not given in the post; the poster\'s 28 sqrt(22)/3 uses 6 as a lateral edge. The record defines slant height explicitly (face height), answer 28 sqrt(29)/3.')

# ---------------- 1766655 great rhombicuboctahedron; painted cube (alias)
fig=r'''pair V=(0,0);
path poly(pair P,real a,int n){ path p=P; pair Q=P; real t=a; for(int k=0;k<n-1;++k){ Q=Q+dir(t); p=p--Q; t+=360/n; } return p--cycle; }
filldraw(poly(V,0,4),rgb(0.85,0.92,1),linewidth(0.9));
filldraw(poly(V,90,6),rgb(1,0.93,0.8),linewidth(0.9));
filldraw(poly(V,210,8),rgb(0.88,0.97,0.85),linewidth(0.9));
dot(V);
pair ctr(real a,int n){ real al=180-360/n; return V+1/(2*Sin(180/n))*dir(a+al/2); }
label("square",ctr(0,4),fontsize(8pt));label("hexagon",ctr(90,6),fontsize(8pt));label("octagon",ctr(210,8),fontsize(8pt));'''
b.add(1766655,1,r'''The great rhombicuboctahedron is a convex polyhedron with $26$ faces: $12$ square faces, $6$ regular octagonal faces and $8$ regular hexagonal faces. At each vertex, one square, one hexagon and one octagon meet. How many of the segments joining two vertices of the polyhedron lie in its interior (apart from their endpoints)?''',
r'''\textbf{Vertices and edges.} Each vertex lies on exactly one octagon, so there are $6\cdot8=48$ vertices. Three faces, hence three edges, meet at each vertex, so there are $\dfrac{48\cdot3}{2}=72$ edges. (Check with Euler's formula: $48-72+26=2$.)
'''+asy(fig,'4.5cm')+r'''
\textbf{Segments.} The $48$ vertices determine $\dbinom{48}{2}=1128$ segments. Since the polyhedron is convex, a segment lies on the surface if its endpoints lie on a common face, and otherwise it passes through the interior. Two vertices on a common face are joined by an edge or by a diagonal of that face, and two vertices not joined by an edge share at most one face, so nothing is counted twice. The face diagonals number
\[
12\cdot2+8\cdot\dfrac{6\cdot3}{2}+6\cdot\dfrac{8\cdot5}{2}=24+72+120=216 .
\]
So the number of interior segments is $1128-72-216=\boxed{840}$.''',
'Polyhedra|Combinations|Complementary counting|Diagonals|Euler\'s polyhedron formula',5,source=src('AIME',1988,None,10),
note='AIME 1988 Problem 10 (official answer 840). The sketch shows the three faces meeting at a vertex, laid flat.')
b.add(1766655,2,r'''A $3\times3\times3$ wooden cube is painted on all six faces and then cut into $27$ unit cubes. One unit cube is chosen at random and rolled, so that each of its faces is equally likely to end up on the bottom. What is the probability that exactly one of the $5$ visible faces is painted?''',
r'''The unit cubes have $0,1,2,3$ painted faces in numbers $1,6,12,8$. A cube with one painted face works when that face is visible ($\dfrac56$); a cube with two works when one of them is at the bottom ($\dfrac26$). So the probability is $\dfrac{6}{27}\cdot\dfrac56+\dfrac{12}{27}\cdot\dfrac26=\boxed{\dfrac13}$.''',
'Cubes and rectangular prisms|Probability|Conditional probability|Counting principles',3,
note='MATHCOUNTS problem; repeat of an earlier record (aliased).')

# ---------------- 1755096 blueberries expression
b.add(1755096,1,r'''Sarah picks $b$ blueberries. Michael picks $3$ more than half as many as Sarah, and David picks $5$ more than Michael. Kaycee picks $10$ less than $3$ times as many as David, and Hannah picks twice as many as Kaycee. Find an expression in terms of $b$ for the number of blueberries Hannah picked.''',
r'''Build the expressions one person at a time:
\[
\text{Michael: }\dfrac b2+3,\qquad\text{David: }\dfrac b2+8,\qquad\text{Kaycee: }3\left(\dfrac b2+8\right)-10=\dfrac{3b}{2}+14,
\]
\[
\text{Hannah: }2\left(\dfrac{3b}{2}+14\right)=\boxed{3b+28}.
\]
Check with $b=10$: Michael $8$, David $13$, Kaycee $29$, Hannah $58=3\cdot10+28$. The poster's $3b-4$ has the right coefficient but a wrong constant (for example, from $3\cdot\dfrac b2+8$ instead of $3\left(\dfrac b2+8\right)$, which gives $2\left(\dfrac{3b}{2}-2\right)=3b-4$).''',
'Algebraic expressions and identities|Linear equations',1,
note='The poster\'s answer 3b - 4 is wrong; the correct expression is 3b + 28.')

# ---------------- 1766801 trapezoid ratio
fig=r'''real k=2.25, c=3, a=sqrt(k)*c;
pair D=(0,0),C=(c,0),A=(-0.8,2.6),B=A+(a,0);
pair O=extension(A,C,B,D);
draw(A--B--C--D--cycle,linewidth(0.9));draw(A--C,blue);draw(B--D,blue);
dot(O);
label("$A$",A,NW);label("$B$",B,NE);label("$C$",C,SE);label("$D$",D,SW);label("$O$",O,dir(-90)*1.2);'''
b.add(1766801,1,r'''In trapezoid $ABCD$ with $AB\parallel CD$, the diagonals meet at $O$, and the area of triangle $AOB$ is $k$ times the area of triangle $COD$. Assuming $AC\ne BD$, find
\[
\dfrac{AD^2-BC^2}{AC^2-BD^2}
\]
in terms of $k$.''',
r'''Triangles $AOB$ and $COD$ are similar (alternate angles at the parallel sides), with ratio $\dfrac{AB}{CD}$, so $\dfrac{AB^2}{CD^2}=k$ and $AB=\sqrt k\,CD$.
'''+asy(fig,'5.5cm')+r'''
Use coordinates $D=(0,0)$, $C=(c,0)$, $A=(p,h)$, $B=(p+a,h)$ with $a=AB=\sqrt k\,c$. Then
\[
AD^2-BC^2=p^2-(p+a-c)^2=(c-a)(2p+a-c),
\]
\[
AC^2-BD^2=(p-c)^2-(p+a)^2=-(a+c)(2p+a-c).
\]
The assumption $AC\ne BD$ means $2p+a-c\ne0$, so
\[
\dfrac{AD^2-BC^2}{AC^2-BD^2}=\dfrac{a-c}{a+c}=\boxed{\dfrac{\sqrt k-1}{\sqrt k+1}} .
\]
(The figure uses $k=\dfrac94$, so the ratio is $\dfrac15$.)''',
'Trapezoids|Similarity|Area ratios|Coordinate geometry|Diagonals',4,
note='The condition AC not equal to BD (the trapezoid is not isosceles) is added; for an isosceles trapezoid the ratio is 0/0. Checked numerically for random trapezoids.')

# ---------------- 1766257 Euler's formula; inradius
fig=r'''pair d=(0.5,0.35);
pair p0=(0,0),p1=(2,0),p2=(2,2),p3=(0,2);
draw(p0--p1--p2--p3--cycle,linewidth(0.9));
draw(p1--p1+2*d--p2+2*d--p2,linewidth(0.9));draw(p3--p3+2*d--p2+2*d,linewidth(0.9));
draw(p0--p0+2*d,dashed);draw(p0+2*d--p1+2*d,dashed);draw(p0+2*d--p3+2*d,dashed);
dot(p0);dot(p1);dot(p2);dot(p3);dot(p1+2*d);dot(p2+2*d);dot(p3+2*d);dot(p0+2*d);
label("$V-E+F=8-12+6=2$",(1.5,-0.45),S);'''
b.add(1766257,1,r'''A convex polyhedron has $56$ faces and $114$ edges. How many vertices must it have?''',
r'''Euler's formula for a convex polyhedron states $V-E+F=2$, as in the cube below.
'''+asy(fig,'3.8cm')+r'''
Here $V-114+56=2$, so $V=\boxed{60}$.''',
'Euler\'s polyhedron formula|Polyhedra',1,
note='"Polyhedron" is taken to be convex (or at least a simple polyhedron), as Euler\'s formula needs.')
fig=r'''pair B=(0,0),C=(12,0),A=(11/3,2*sqrt(26)/3);
real a=12,bb=9,c=5;
pair I=(a*A+bb*B+c*C)/(a+bb+c);
real r=4*sqrt(26)/13;
draw(A--B--C--cycle,linewidth(0.9));
draw(circle(I,r),blue);
pair F=(I.x,0);
draw(I--F,red);dot(I);dot(F,red);
draw(F+(0.3,0)--F+(0.3,0.3)--F+(0,0.3),red);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$I$",I,NE);
label("$r$",(I+F)/2,W,red);
label("$12$",(B+C)/2+(2.5,0),S);label("$5$",(A+B)/2,NW);label("$9$",(A+C)/2,NE);'''
b.add(1766257,2,r'''Find the radius of the circle inscribed in a triangle with side lengths $5$ inches, $9$ inches and $12$ inches. Round your answer to the nearest hundredth of an inch.''',
r'''The semiperimeter is $s=\dfrac{5+9+12}{2}=13$. By Heron's formula the area is
\[
K=\sqrt{13(13-5)(13-9)(13-12)}=\sqrt{13\cdot8\cdot4\cdot1}=\sqrt{416}=4\sqrt{26}.
\]
The area also equals $rs$ (split the triangle into three triangles with apex at the incentre $I$ and height $r$).
'''+asy(fig,'6.5cm')+r'''
So
\[
r=\dfrac Ks=\dfrac{4\sqrt{26}}{13}\approx\boxed{1.57}\text{ inches}.
\]''',
'Incircles and incentres|Heron\'s formula|Lengths, perimeter, and area|Triangles',3)

# ---------------- 1766918 MATH in one pile
b.add(1766918,1,r'''The $26$ letters of the alphabet are written on tiles and randomly separated into two piles of $13$ tiles each. What is the probability that the letters M, A, T and H all end up in the same pile?''',
r'''Look at the pile containing M. Its other $12$ tiles are a random $12$-element subset of the other $25$ letters. The probability that A, T and H are all among them is
\[
\dfrac{12}{25}\cdot\dfrac{11}{24}\cdot\dfrac{10}{23}=\dfrac{1320}{13800}=\boxed{\dfrac{11}{115}} .
\]
(Equivalently, $\dfrac{2\dbinom{22}{9}}{\dbinom{26}{13}}=\dfrac{994840}{10400600}=\dfrac{11}{115}$.)''',
'Probability|Combinations|Sampling without replacement',3,
note='"The word MATH can be found in one of the two piles" is read as all four letters lying in the same pile.')

# ---------------- 1766302 x^2+x+1=y, y^2+y+1=x
b.add(1766302,1,r'''Complex numbers $x$ and $y$ satisfy $x^2+x+1=y$ and $y^2+y+1=x$. Find the maximum possible value of $|xy|$.''',
r'''Subtract the equations: $x^2-y^2+x-y=y-x$, so $(x-y)(x+y+2)=0$.

\textbf{Case $x=y$.} Then $x^2+x+1=x$, so $x^2=-1$, $x=y=\pm i$ and $|xy|=|x^2|=1$.

\textbf{Case $x+y=-2$.} Adding the equations gives $x^2+y^2+2=0$, so $(x+y)^2-2xy=-2$, i.e.\ $4-2xy=-2$ and $xy=3$. Such numbers exist: $x,y$ are the roots of $t^2+2t+3=0$, namely $-1\pm i\sqrt2$, and indeed $x^2=-2x-3$ gives $x^2+x+1=-x-2=y$ (and symmetrically). Here $|xy|=3$.

The maximum is $\boxed{3}$.''',
'Complex numbers|Equations and systems of equations|Vieta\'s formulas|Factoring',4)

# ---------------- 1766872 product of consecutive odd numbers
b.add(1766872,1,r'''The number $\underbrace{11\ldots1}_{2002\text{ digits}}\underbrace{55\ldots5}_{2002\text{ digits}}$ is the product of two consecutive odd numbers. Find the sum of these two odd numbers.''',
r'''Let $t=10^{2002}$. The number is
\[
N=\dfrac{t-1}{9}\cdot t+5\cdot\dfrac{t-1}{9}=\dfrac{(t-1)(t+5)}{9}=\dfrac{t^2+4t-5}{9}=\left(\dfrac{t+2}{3}\right)^2-1 .
\]
Here $\dfrac{t+2}{3}=\underbrace{33\ldots3}_{2001}4$ is an even integer, so
\[
N=\left(\dfrac{t+2}{3}-1\right)\left(\dfrac{t+2}{3}+1\right)=\underbrace{33\ldots3}_{2002}\cdot\underbrace{33\ldots3}_{2001}5 ,
\]
a product of two consecutive odd numbers. Their sum is
\[
\dfrac{2(t+2)}{3}=\dfrac{2\cdot10^{2002}+4}{3}=\boxed{\underbrace{66\ldots6}_{2001}8} .
\]
(The same pattern holds for every length: $15=3\cdot5$, $1155=33\cdot35$, $111555=333\cdot335$.)''',
'Digits and bases|Difference of squares|Algebraic expressions and identities|Pattern recognition',4,
note='Checked exactly with integer arithmetic for the 2002-digit case.')

# ---------------- 1766818 AD^2 = AM * AC
fig=r'''pair A=(0,0),C=(7,0),D=(2.2,3.4);
real t=abs(D-A)^2/abs(C-A);
pair M=(t,0);
draw(A--C--D--cycle,linewidth(0.9));draw(D--M,blue+linewidth(0.9));
draw(arc(D,0.7,degrees(A-D),degrees(M-D)),blue);
draw(arc(C,1.1,180,degrees(D-C)),blue);
label("$A$",A,SW);label("$C$",C,SE);label("$D$",D,N);label("$M$",M,S);
real ma=(degrees(A-D)+degrees(M-D))/2;
label("$\theta$",D+1.05*dir(ma),blue);
label("$\theta$",C+1.45*dir((180+degrees(D-C))/2),blue);'''
b.add(1766818,1,r'''In triangle $ADC$, point $M$ lies on side $AC$ and segment $DM$ is drawn so that $\angle ADM=\angle ACD$. Prove that $AD^2=AM\cdot AC$.''',
r'''Let $\theta=\angle ADM=\angle ACD$.
'''+asy(fig,'5.5cm')+r'''
Triangles $ADM$ and $ACD$ share the angle at $A$ (since $M$ lies on $AC$, $\angle DAM=\angle DAC$), and $\angle ADM=\angle ACD$. By AA, triangle $ADM$ is similar to triangle $ACD$, with $A\to A$, $D\to C$, $M\to D$. Corresponding sides are proportional:
\[
\dfrac{AD}{AC}=\dfrac{AM}{AD},
\]
so $AD^2=AM\cdot AC$. $\blacksquare$''',
'Similarity|Triangles|Angle chasing',2,
note='AoPS Introduction to Geometry exercise; "segment DM is drawn" is read as M on side AC.')

# ---------------- 1766234 1/16 in base 5
b.add(1766234,1,r'''When the fraction $\dfrac{1}{16}$ is written in base $5$, the result is the repeating expansion $0.\overline{abcd}_5$, where $a,b,c,d$ are base-$5$ digits. Find $a+b+c+d$.''',
r'''A purely periodic base-$5$ expansion with period $4$ satisfies $0.\overline{abcd}_5=\dfrac{(abcd)_5}{5^4-1}=\dfrac{(abcd)_5}{624}$. Since $624=16\cdot39$,
\[
\dfrac1{16}=\dfrac{39}{624},
\]
so $(abcd)_5=39=0\cdot125+1\cdot25+2\cdot5+4$, i.e.\ $abcd=0124$. Hence $\dfrac1{16}=0.\overline{0124}_5$ and $a+b+c+d=0+1+2+4=\boxed{7}$.''',
'Digits and bases|Repeating decimals|Fractions',3)

# ---------------- 1766118 number of subsets
b.add(1766118,1,r'''How many subsets does the set $\{a,b,c,d,e,f,g,h\}$ have? How many of them are proper subsets?''',
r'''To form a subset, decide for each of the $8$ elements whether it is in or out: $2^8=\boxed{256}$ subsets, counting the empty set and the whole set.

A proper subset is any subset other than the set itself, so there are $256-1=\boxed{255}$ proper subsets. (If both the empty set and the whole set are excluded, there are $254$; a key giving one of these numbers is counting a different kind of subset, but the number of subsets is $256$.)''',
'Counting principles|Multiplication principle|Combinations',1,
note='The poster\'s 2^8 = 256 is correct for "subsets"; the record also asks for proper subsets (255), the likely source of the confusion.')

# ---------------- 1764346 x|y, x+1|y+1, x+2|y+2
b.add(1764346,1,r'''Let $x$ and $y$ be distinct positive integers such that $x\mid y$, $x+1\mid y+1$ and $x+2\mid y+2$. Given that one of $x$, $x+1$, $x+2$ is divisible by $7$, what is the sum of the digits of the smallest possible value of $y$?''',
r'''The three conditions say that $y-x$ is divisible by $x$, by $x+1$ and by $x+2$, i.e.\ by $L=\operatorname{lcm}(x,x+1,x+2)$. Since $y\ne x$, $y=x+mL$ for a nonzero integer $m$; as $L\ge x+2>x$, a negative $m$ would make $y$ negative, so the smallest $y$ for a given $x$ is $y=x+L$.

One of $x,x+1,x+2$ is divisible by $7$ exactly when $x\equiv5,6,0\pmod7$. Since $x+1$ is coprime to $x$ and $x+2$, and $\gcd(x,x+2)\le2$, we have $L\ge\dfrac{x(x+1)(x+2)}{2}$, which grows quickly. So compare the smallest candidates:
\[
x=5:\ 5+\operatorname{lcm}(5,6,7)=215,\qquad x=6:\ 6+\operatorname{lcm}(6,7,8)=174,\qquad x=7:\ 7+\operatorname{lcm}(7,8,9)=511,
\]
and for $x\ge12$, $y>L\ge\dfrac{12\cdot13\cdot14}{2}=1092$. So the smallest value is $y=174$ (with $x=6$: $6\mid174$, $7\mid175$, $8\mid176$), and its digit sum is $1+7+4=\boxed{12}$.''',
'Divisibility|HCF and LCM|Remainders and congruences|Bounding and extremal cases',4,
note='The post writes "x/y, x+1/y+1, x+2/y+2" with the note "x/y means x divides y"; the record writes the divisibilities explicitly. Checked by brute force.')

b.save()
