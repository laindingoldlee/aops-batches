from qb import *
b=Bank('p232_03')

# ---------------- 1723400 hexagon around a triangle
fig=r'''pair A=(0,0),B=(5,0),C=(1.6,3.4);real x=1.2;
pair A1=A+x*unit(A-B),A2=A+x*unit(A-C),B1=B+x*unit(B-A),B2=B+x*unit(B-C),C1=C+x*unit(C-B),C2=C+x*unit(C-A);
fill(A--A1--A2--cycle,palegreen);fill(B--B2--B1--cycle,palegreen);fill(C--C2--C1--cycle,palegreen);
fill(A--A2--B2--B--cycle,paleblue);fill(B--B1--C2--C--cycle,paleblue);fill(C--C1--A1--A--cycle,paleblue);
draw(A1--A2--B2--B1--C2--C1--cycle,linewidth(0.9));
draw(A--B--C--cycle,linewidth(1.1));
draw(A1--B1,dashed);draw(B2--C1,dashed);draw(A2--C2,dashed);
label("$A$",A,dir(80));label("$B$",B,dir(140));label("$C$",C,S);
label("$A_1$",A1,W);label("$A_2$",A2,SW);label("$B_1$",B1,E);label("$B_2$",B2,SE);label("$C_1$",C1,N);label("$C_2$",C2,NE);
label("$x$",(A+A1)/2,N);label("$x$",(B+B1)/2,N);label("$x$",(C+C2)/2,NW);
label("$T$",(A+B+C)/3);'''
b.add(1723400,1,r'''Triangle $ABC$ has side lengths $a=BC$, $b=CA$, $c=AB$ and area $T$, and let $x>0$. On each of the three lines $AB$, $BC$, $CA$, mark the two points that lie outside the side, at distance $x$ beyond each of its endpoints: on line $AB$ the points $A_1$ (beyond $A$) and $B_1$ (beyond $B$), on line $BC$ the points $B_2$ (beyond $B$) and $C_1$ (beyond $C$), and on line $CA$ the points $C_2$ (beyond $C$) and $A_2$ (beyond $A$). Find the area of the hexagon $A_1A_2B_2B_1C_2C_1$ in terms of $T$, $a$, $b$, $c$ and $x$.''',
r'''Cut the hexagon into the triangle, three corner triangles at the vertices (green) and three quadrilaterals along the sides (blue).
'''+asy(fig,'6.5cm')+r'''
\textbf{Corner triangles.} At $A$, triangle $AA_1A_2$ has $AA_1=AA_2=x$ and angle $\angle A_1AA_2=\angle BAC$ (vertical angles), so its area is $\dfrac12x^2\sin A$. Similarly at $B$ and $C$.

\textbf{Side quadrilaterals.} The points $A_2$ and $B_2$ lie on the rays $CA$ and $CB$ beyond $A$ and $B$, with $CA_2=b+x$ and $CB_2=a+x$. So the quadrilateral $ABB_2A_2$ is triangle $CA_2B_2$ minus triangle $CAB$, with area
\[
\dfrac12(a+x)(b+x)\sin C-\dfrac12ab\sin C=\dfrac12\left(x(a+b)+x^2\right)\sin C .
\]
Similarly for the other two sides.

\textbf{Total.} Adding everything, the hexagon has area
\[
H=T+\sum_{\text{vertices}}\left(x^2+\dfrac{x(\text{sum of the two sides at the vertex})}{2}\right)\sin(\text{angle}) .
\]
Using $\sin C=\dfrac{2T}{ab}$, $\sin A=\dfrac{2T}{bc}$, $\sin B=\dfrac{2T}{ca}$:
\[
\sum x^2\sin C=2Tx^2\left(\dfrac1{ab}+\dfrac1{bc}+\dfrac1{ca}\right)=\dfrac{2Tx^2(a+b+c)}{abc},\qquad
\sum\dfrac{x(a+b)}{2}\sin C=Tx\sum\left(\dfrac1a+\dfrac1b\right)=2Tx\left(\dfrac1a+\dfrac1b+\dfrac1c\right).
\]
Therefore
\[
\boxed{\ \dfrac{H}{T}=1+2x\left(\dfrac1a+\dfrac1b+\dfrac1c\right)+\dfrac{2x^2(a+b+c)}{abc}\ } .
\]
For example, for an equilateral triangle with side $1$ and $x=1$, the hexagon has $13$ times the area of the triangle.''',
'Area decomposition|Triangles|Lengths, perimeter, and area|Trigonometry',5,
note='The post asks for "the correlation between the areas" with every point at the same distance x from the vertex; the record asks for the hexagon area in terms of the triangle\'s sides, area and x, with the hexagon named explicitly. Checked with the shoelace formula on random triangles.')

# ---------------- 1724670 MathWorks 2011 #3
b.add(1724670,1,r'''Julio's teacher asks the class to write down a list of positive integers between $20$ and $50$ such that no two numbers on the list have a prime factor in common. How many numbers are in the largest possible list meeting this requirement?''',
r'''\textbf{Upper bound.} Give each number on the list its smallest prime factor. These primes are all different, since two numbers sharing it would have a common prime factor. Every number $n$ with $20<n<50$ has smallest prime factor $p$ with $p^2\le n$ or $p=n$ (if $n$ is composite, $p\le\sqrt{n}<\sqrt{50}$, so $p\in\{2,3,5,7\}$). So the smallest prime factors come from $\{2,3,5,7\}\cup\{23,29,31,37,41,43,47\}$, which has $4+7=11$ elements; the primes $11,13,17,19$ cannot occur. So the list has at most $11$ numbers.

\textbf{Construction.} The list $25,27,32,49,23,29,31,37,41,43,47$ works: $32=2^5$, $27=3^3$, $25=5^2$, $49=7^2$ and the seven primes pairwise share no prime factor.

The answer is $\boxed{11}$.''',
'Prime numbers|Prime factorisation|Bounding and extremal cases|Construction',3,source=src('MathWorks Math Contest',2011,None,3),
note='"Between 20 and 50" gives the same answer whether or not 20 and 50 are allowed.')

# ---------------- 1724416 sixty-degree angles in convex polygon
fig=r'''pair A=(0,0),B=(3,0),C=B+3*dir(60),D=3*dir(60);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--(-1.4,0),dashed);draw(C--C+1.4*dir(60),dashed);
draw(arc(A,0.55,0,60));label("$60^\circ$",A+1.0*dir(30),fontsize(8pt));
draw(arc(C,0.55,180,240));label("$60^\circ$",C+1.0*dir(210),fontsize(8pt));
draw(arc(A,0.45,60,180),blue,Arrow(4));label("$120^\circ$",A+0.95*dir(120),blue+fontsize(8pt));
draw(arc(C,0.45,-120,60),blue,Arrow(4));label("$120^\circ$",C+0.95*dir(-30),blue+fontsize(8pt));
label("$A$",A,S);label("$B$",B,SE);label("$C$",C,N);label("$D$",D,NW);'''
b.add(1724416,1,r'''Prove that a convex polygon with $n\ge4$ sides has at most two interior angles equal to $60^\circ$.''',
r'''Walking around a convex polygon, we turn at each vertex through the exterior angle $180^\circ-(\text{interior angle})$, which is positive because each interior angle is less than $180^\circ$. After one full trip we have turned through exactly $360^\circ$, so the exterior angles add up to $360^\circ$.

An interior angle of $60^\circ$ has exterior angle $120^\circ$. If three interior angles were $60^\circ$, their exterior angles alone would add up to $3\cdot120^\circ=360^\circ$, leaving $0^\circ$ for the other $n-3\ge1$ exterior angles, each of which is positive. This is impossible, so there are at most two angles of $60^\circ$. $\blacksquare$
'''+asy(fig,'5cm')+r'''
Two is possible for every $n\ge4$: the rhombus $ABCD$ above with angles $60^\circ,120^\circ,60^\circ,120^\circ$ has two (its exterior angles at $A$ and $C$ are $120^\circ$ each, leaving $120^\circ$ for $B$ and $D$), and for larger $n$ one can cut the corners at $B$ and $D$ slightly. (For a triangle, $n=3$, all three angles can be $60^\circ$, and the statement needs convexity: it is about convex polygons.)''',
'Angle sums|Quadrilaterals and polygons|Proof by contradiction',3,
note='The poster asks why a polygon with n > 3 sides has at most two 60 degree angles; the claim is stated for convex polygons, where it holds.')

# ---------------- 1724261 x^4+2^{4n+2} prime
b.add(1724261,1,r'''Find all positive integers $x$ and nonnegative integers $n$ such that $p=x^4+2^{4n+2}$ is a prime number.''',
r'''Put $y=2^n$. Then $2^{4n+2}=4y^4$, and by the Sophie Germain identity
\[
p=x^4+4y^4=\left(x^2+2y^2\right)^2-(2xy)^2=\left(x^2+2xy+2y^2\right)\left(x^2-2xy+2y^2\right).
\]
The second factor is $(x-y)^2+y^2\ge1$, and the first is larger than the second. For $p$ to be prime the smaller factor must be $1$: $(x-y)^2+y^2=1$ with $y\ge1$ forces $y=1$ and $x=y=1$. So $n=0$, $x=1$, and indeed $p=1+4=5$ is prime.

The only solution is $\boxed{x=1,\ n=0}$, giving $p=5$. (If $n$ must be a positive integer, there are no solutions.)''',
'Prime numbers|Factoring|Difference of squares|Algebraic expressions and identities',4,
note='"Natural numbers" is ambiguous about 0; the only solution has n = 0, so the record allows n >= 0 and notes that there is none with n >= 1. Near-miss of aops-topic-1972985-q01 (n^4 + 4 prime).')

# ---------------- 1724256 x^2+1 | x^2+x+2
b.add(1724256,1,r'''Find all integers $x$ such that $x^2+1$ divides $x^2+x+2$.''',
r'''Since $x^2+1$ divides itself, it divides $(x^2+x+2)-(x^2+1)=x+1$.
\begin{itemize}
\item If $x+1=0$, i.e.\ $x=-1$: $x^2+1=2$ divides $x^2+x+2=2$. \checkmark
\item If $x+1\ne0$, then $x^2+1\le|x+1|\le|x|+1$, so $x^2\le|x|$, which forces $x\in\{0,1\}$ (or $x=-1$, already done). For $x=0$: $1\mid2$ \checkmark; for $x=1$: $2\mid4$ \checkmark.
\end{itemize}
The solutions are $\boxed{x=-1,\ 0,\ 1}$.''',
'Divisibility|Bounding and extremal cases|Polynomials',3,
note='The notation (x^2+x+2) \\vdots (x^2+1) means "is divisible by".')

# ---------------- 1722309 quadrilateral with cevians to midpoints
fig=r'''pair A=(0,0),B=(4,0),D=(1.4,3),C=B+D;
pair K=(C+D)/2,L=(D+A)/2,M=(A+B)/2,Nn=(B+C)/2;
pair P1=extension(A,K,B,L),P2=extension(B,L,C,M),P3=extension(C,M,D,Nn),P4=extension(D,Nn,A,K);
fill(P1--P2--P3--P4--cycle,lightgray);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--K,blue);draw(B--L,blue);draw(C--M,blue);draw(D--Nn,blue);
dot(K);dot(L);dot(M);dot(Nn);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);
label("$K$",K,N);label("$L$",L,W);label("$M$",M,S);label("$N$",Nn,E);'''
b.add(1722309,1,r'''In a quadrilateral $ABCD$, the segments $AK$, $BL$, $CM$, $DN$ are drawn, where $K,L,M,N$ are the midpoints of $CD$, $DA$, $AB$, $BC$ respectively. These four segments bound a smaller quadrilateral inside $ABCD$.
\begin{enumerate}
\item[(a)] Prove that if $ABCD$ is a parallelogram, the area of the small quadrilateral is $\dfrac15$ of the area of $ABCD$.
\item[(b)] Show that the ratio is not $\dfrac15$ for every quadrilateral, by computing it for $A=(0,0)$, $B=(2,0)$, $C=(2,2)$, $D=(0,4)$.
\end{enumerate}''',
r'''\textbf{(a)} An affine map (such as $(x,y)\mapsto(px+qy+e,\ rx+sy+f)$ with $ps-qr\ne0$) sends lines to lines, midpoints to midpoints and intersection points to intersection points, and multiplies all areas by the same factor $|ps-qr|$, so it preserves ratios of areas. Every parallelogram is the image of the unit square under such a map, so it is enough to treat $A=(0,0)$, $B=(1,0)$, $C=(1,1)$, $D=(0,1)$.
'''+asy(fig,'5.5cm')+r'''
Then $K=\left(\dfrac12,1\right)$, $L=\left(0,\dfrac12\right)$, $M=\left(\dfrac12,0\right)$, $N=\left(1,\dfrac12\right)$. Line $AK$ is $y=2x$ and line $BL$ is $y=\dfrac{1-x}{2}$; they meet at $\left(\dfrac15,\dfrac25\right)$. The figure is unchanged by a quarter turn about the centre $\left(\dfrac12,\dfrac12\right)$ (which maps $A\to B\to C\to D\to A$ and $K\to L\to M\to N\to K$), so the four corners of the small quadrilateral are the images of this point:
\[
\left(\dfrac15,\dfrac25\right),\ \left(\dfrac35,\dfrac15\right),\ \left(\dfrac45,\dfrac35\right),\ \left(\dfrac25,\dfrac45\right).
\]
It is a square with side $\sqrt{\left(\dfrac25\right)^2+\left(\dfrac15\right)^2}=\dfrac{1}{\sqrt5}$, so its area is $\dfrac15$ of the unit square. Hence the ratio is $\dfrac15$ for every parallelogram. $\blacksquare$

\textbf{(b)} Here $K=(1,3)$, $L=(0,2)$, $M=(1,0)$, $N=(2,1)$, and $ABCD$ (a right trapezoid) has area $\dfrac{(4+2)\cdot2}{2}=6$. Intersecting consecutive segments gives the corners
\[
AK\cap BL=\left(\dfrac12,\dfrac32\right),\quad BL\cap CM=\left(\dfrac43,\dfrac23\right),\quad CM\cap DN=\left(\dfrac{12}{7},\dfrac{10}{7}\right),\quad DN\cap AK=\left(\dfrac89,\dfrac83\right).
\]
By the shoelace formula the small quadrilateral has area $\dfrac{151}{126}$, so the ratio is
\[
\dfrac{151}{126\cdot6}=\boxed{\dfrac{151}{756}}\ne\dfrac15=\dfrac{151.2}{756} .
\]
So the claim ``always $\dfrac15$'' is false for general quadrilaterals; it holds for parallelograms.''',
'Parallelograms|Area ratios|Midpoints|Coordinate geometry|Shoelace formula|Counterexamples|Geometric transformations',5,
note='The post asks to prove that the ratio is always 1/5 for any quadrilateral; this is false (for the trapezoid in part (b) it is 151/756). The record proves it for parallelograms, where it is true, and asks for the counterexample. The segments are taken as A to the midpoint of CD, B to DA, C to AB, D to BC (each vertex to a non-adjacent side, no two sharing an endpoint).')

# ---------------- 1721154 D&D ability scores
b.add(1721154,1,r'''To generate an ability score in Dungeons and Dragons, one rolls four fair six-sided dice, removes one die showing the lowest value, and adds the three that remain.
\begin{enumerate}
\item What is the most likely score?
\item What is the least likely score?
\item What is the probability of a score of $15$ or higher?
\item What is the probability of a score of $5$ or lower?
\item Six scores are generated independently. What is the probability that they are, in some order, $9$, $13$, $13$, $15$, $15$, $18$?
\end{enumerate}''',
r'''There are $6^4=1296$ equally likely rolls. For a score $s$, let $N(s)$ be the number of rolls giving $s$. Counting by the smallest die $m$: the other three dice are all at least $m$ and the score is their sum. Carrying out this count for each $s$ (for example, $s=3$ needs all four dice equal to $1$, and $s=18$ needs at least three sixes) gives
\[
\begin{array}{c|cccccccccccccccc}
s&3&4&5&6&7&8&9&10&11&12&13&14&15&16&17&18\\ \hline
N(s)&1&4&10&21&38&62&91&122&148&167&172&160&131&94&54&21
\end{array}
\]
(the counts add up to $1296$). Two entries can be checked by hand: $N(3)=1$ (all ones), and $N(18)=\dbinom43\cdot5+1=21$ (exactly three sixes with the fourth die $1$ to $5$, or four sixes).
\begin{enumerate}
\item The most likely score is $\boxed{13}$ ($172$ rolls).
\item The least likely score is $\boxed{3}$ ($1$ roll).
\item $P(s\ge15)=\dfrac{131+94+54+21}{1296}=\dfrac{300}{1296}=\boxed{\dfrac{25}{108}}$.
\item $P(s\le5)=\dfrac{1+4+10}{1296}=\dfrac{15}{1296}=\boxed{\dfrac{5}{432}}$.
\item The six scores can be arranged in $\dfrac{6!}{1!\,2!\,2!\,1!}=180$ orders, so the probability is
\[
180\cdot\dfrac{91\cdot172^2\cdot131^2\cdot21}{1296^6}=\boxed{\dfrac{101062244465}{2742118830047232}}\approx3.69\times10^{-5}.
\]
\end{enumerate}
For example, $N(4)=4$: the dice must be three $1$s and one $2$ (the score drops one $1$ and keeps $1+1+2$), in $4$ orders.''',
'Probability|Dice probability|Casework|Multiset permutations|Independent events',4,
note='Five questions about one setup, kept as one record. "Removes the one with the lowest value" means one die of the lowest value. All probabilities computed exactly by enumerating the 1296 rolls.')

# ---------------- 1724087 bogus solution x^2-8x-9=0
b.add(1724087,1,r'''A student solves $x^2-8x-9=0$ as follows:
\[
x=\dfrac{8+\sqrt{8^2-4\cdot1\cdot(-9)}}{2}=\dfrac{8+\sqrt{100}}{2}=\dfrac{18}{2}=9 .
\]
What is wrong with this solution? Give the correct set of solutions.''',
r'''The quadratic formula has a $\pm$ sign: $x=\dfrac{8\pm\sqrt{100}}{2}=\dfrac{8\pm10}{2}$. The student used only the $+$ sign and lost the root $\dfrac{8-10}{2}=-1$. Indeed $x^2-8x-9=(x-9)(x+1)$. The solutions are $\boxed{x=9\text{ and }x=-1}$.''',
'Quadratic equations|Factoring',1,
note='First problem of a "bogus solutions" marathon; the record asks for the error.')

# ---------------- 1724204 Schur-type colouring
b.add(1724204,1,r'''The positive integers $1,2,3,\dots$ are written down in order and each is coloured with one of $k$ colours. The rule is that there must be no three \emph{distinct} numbers $a<b<c$ of the same colour with $a+b=c$. Prove that for every $k$ there is a number $N$ such that it is impossible to colour all of $1,2,\dots,N$ by the rule; that is, no matter how many colours are allowed, one is always forced to stop.''',
r'''Fix a colouring of $1,2,\dots,N$ with $k$ colours, where $N=(k+1)^{L}$ and $L=3k+2$. We find distinct $a<b<c\le N$ of the same colour with $a+b=c$.

\textbf{Colouring pairs.} For integers $1\le u<v\le N+1$ give the pair $\{u,v\}$ the colour of the number $v-u\in\{1,\dots,N\}$.

\textbf{A sequence with a simple pattern.} Start with $V_0=\{1,2,\dots,N+1\}$. Let $v_1$ be the smallest element of $V_0$. The other elements $v$ of $V_0$ are split into $k$ classes by the colour of $\{v_1,v\}$; let $V_1$ be a largest class, so $|V_1|\ge\dfrac{|V_0|-1}{k}$. Repeat: $v_2$ is the smallest element of $V_1$, $V_2$ is a largest class of $V_1\setminus\{v_2\}$ by the colour of $\{v_2,v\}$, and so on. If $|V_{i-1}|\ge(k+1)^{L-i+1}$ then
\[
|V_i|\ge\dfrac{(k+1)^{L-i+1}-1}{k}\ge(k+1)^{L-i},
\]
since $(k+1)^{j+1}-1-k(k+1)^j=(k+1)^j-1\ge0$. As $|V_0|>(k+1)^L$, every $V_i$ with $i\le L-1$ is nonempty, and we obtain $v_1<v_2<\cdots<v_L$ with the property: \emph{the colour of $\{v_i,v_j\}$ for $i<j$ depends only on $i$}; call it $c_i$.

\textbf{Four indices of one colour.} Among $c_1,\dots,c_{L-1}$ (that is, $3k+1$ values in $k$ colours) some colour occurs at least $4$ times, by the pigeonhole principle: at indices $i_1<i_2<i_3<i_4$. Put $w=v_{i_1}$, $x=v_{i_2}$, $y=v_{i_3}$, $z=v_{i_4}$. Every pair among $w,x,y,z$ has this common colour, because the colour of a pair is $c$ of its smaller index.

\textbf{The triple.} The numbers $x-w$, $y-x$, $y-w$ all have this colour and $(x-w)+(y-x)=y-w$. If $x-w\ne y-x$, they are three distinct numbers, as required. If $x-w=y-x$, use $w,x,z$ instead: $(x-w)+(z-x)=z-w$, and $z-x>y-x=x-w$, so $x-w<z-x<z-w$ are distinct and all have the common colour.

In both cases the rule is broken, so no $k$-colouring of $1,\dots,N$ obeys it. $\blacksquare$

(The poster's colouring of $1,\dots,23$ with three colours shows that for $k=3$ one can go at least to $23$; the exact largest values for $3,4,5$ colours are known only through computer searches and are not asked for here.)''',
'Pigeonhole principle|Graph theory|Colourings, tilings, and coverings|Bounding and extremal cases',6,
note='The post asks for the largest N for 3 (and 4, 5) colours, with a conjectured 23 for 3 colours, and whether the numbers can go on for ever with enough colours. The exact maxima (the weak Schur numbers) are only known by computer search and are dropped. The record proves part (b): the process always stops (a weak form of Schur\'s theorem, via a Ramsey-type argument). The poster\'s colouring allows a + a = 2a in one colour, so a and b are taken distinct.')

# ---------------- 1723431 Fibonacci over powers of 10 (alias)
b.add(1723431,1,r'''Let $F_n$ be the Fibonacci numbers with $F_1=F_2=1$. Find $\displaystyle\sum_{n=1}^{\infty}\dfrac{F_n}{10^n}$.''',
r'''With $S=\sum F_nx^n$ and $x=\dfrac1{10}$, $S-xS-x^2S=x$, so $S=\dfrac{x}{1-x-x^2}=\boxed{\dfrac{10}{89}}$.''',
'Fibonacci sequence|Generating functions|Geometric sequences',4,
note='Repeat of an earlier record (aliased).')

# ---------------- 1723619 geometric sequence 2x, x+4, 2x-7
b.add(1723619,1,r'''The first three terms of a geometric sequence are $2x$, $x+4$ and $2x-7$. Find the sum of all possible values of $x$. Express your answer as a common fraction.''',
r'''Three nonzero numbers are consecutive terms of a geometric sequence exactly when the middle one squared equals the product of the other two:
\[
(x+4)^2=2x(2x-7)\ \Longrightarrow\ x^2+8x+16=4x^2-14x\ \Longrightarrow\ 3x^2-22x-16=0\ \Longrightarrow\ (x-8)(3x+2)=0 .
\]
So $x=8$ (terms $16,12,9$, ratio $\dfrac34$) or $x=-\dfrac23$ (terms $-\dfrac43,\dfrac{10}{3},-\dfrac{25}{3}$, ratio $-\dfrac52$). Both give nonzero terms, so both are valid, and the sum is $8-\dfrac23=\boxed{\dfrac{22}{3}}$.''',
'Geometric sequences|Quadratic equations|Vieta\'s formulas',2)

# ---------------- 1723583 linear systems
b.add(1723583,1,r'''A student claims: ``To solve a system of equations in $n$ variables uniquely, you need at least $n$ equations.''
\begin{enumerate}
\item[(a)] Show that the claim is false for general (nonlinear) equations by giving a single equation in two real variables with exactly one solution.
\item[(b)] Prove that the claim is true for \emph{linear} equations: if a system of $m$ linear equations in $n$ real variables has $m<n$, then it has either no solution or infinitely many.
\end{enumerate}''',
r'''\textbf{(a)} The equation $x^2+y^2=0$ has exactly one real solution, $(x,y)=(0,0)$, since a sum of squares is zero only when both squares are zero.

\textbf{(b)} First a lemma.

\emph{Lemma.} A \emph{homogeneous} linear system (all right-hand sides $0$) with fewer equations than variables has a solution other than all zeros.

\emph{Proof by induction on the number $m$ of equations.} If $m=0$, take any nonzero values. Suppose $m\ge1$ and the lemma holds for $m-1$ equations. If no equation involves some variable $x_j$ with a nonzero coefficient, set $x_j=1$ and all other variables $0$. Otherwise pick an equation with a nonzero coefficient of some variable, solve it for that variable, and substitute into the other $m-1$ equations. This gives a homogeneous system of $m-1$ equations in the remaining $n-1$ variables, and $m-1<n-1$. By the induction hypothesis it has a solution that is not all zeros; computing the eliminated variable from the chosen equation gives a nonzero solution of the original system. $\square$

Now let the system with $m<n$ have a solution $p=(p_1,\dots,p_n)$. Its homogeneous version (same left sides, right sides $0$) has a nonzero solution $q$ by the lemma. For every real $t$, $p+tq$ is again a solution, because each linear left side changes by $t$ times its value at $q$, which is $0$. Since $q\ne0$, these are infinitely many different solutions. So the system has no solution or infinitely many, never exactly one. $\blacksquare$''',
'Systems of linear equations|Mathematical induction|Counterexamples|Proof by cases',5,
note='Question 1 of the post. Questions 2-4 (an "optimal algorithm", graphing 4-variable systems, dimensions of the universe) are not definite maths questions and are dropped. Question 1 is split: false for nonlinear equations, true for linear systems (with proof).')

# ---------------- 1723636 digit sums multiple of 7 (alias)
b.add(1723636,1,r'''For how many of the integers from $24$ to $125$ inclusive is the sum of the digits a multiple of $7$?''',
r'''Two-digit numbers need digit sum $7$ or $14$: $25,34,43,52,61,70$ and $59,68,77,86,95$ ($11$). From $100$ to $125$: $106,115,124$ ($3$). Total $\boxed{14}$.''',
'Digits and bases|Systematic counting',2,
note='Repeat of an earlier record (aliased).')

# ---------------- 1723548 tiling with pentagons and decagon
fig=r'''pair V=(0,0);
path poly(pair P,real d,int n){pair[] q;q.push(P);real t=d;pair X=P;for(int i=1;i<n;++i){X=X+dir(t);q.push(X);t+=360/n;}path g=q[0];for(int i=1;i<n;++i) g=g--q[i];return g--cycle;}
path p1=poly(V,0,5),p2=poly(V,108,5),d1=poly(V,216,10);
fill(p1,palegreen);fill(p2,palegreen);fill(d1,paleblue);
draw(p1,linewidth(0.9));draw(p2,linewidth(0.9));draw(d1,linewidth(0.9));
dot(V);label("$V$",V,dir(25),fontsize(9pt));
draw(arc(V,0.35,0,108));draw(arc(V,0.28,108,216));draw(arc(V,0.35,216,360));
label("$108^\circ$",0.62*dir(54),fontsize(7pt));label("$108^\circ$",0.6*dir(162),fontsize(7pt));label("$144^\circ$",0.62*dir(288),fontsize(7pt));
label("pentagon",(0.55,1.05),fontsize(8pt));label("pentagon",(-1.15,0.45),fontsize(8pt));label("decagon",(0.2,-1.7),fontsize(8pt));'''
b.add(1723548,1,r'''Regular polygons with $5$, $5$ and $12$ sides do not fit around a point, but two regular pentagons and a regular decagon do.
\begin{enumerate}
\item[(a)] Check both statements.
\item[(b)] Prove that there is no edge-to-edge tiling of the plane by regular polygons in which every vertex is surrounded by two regular pentagons and one regular decagon.
\end{enumerate}''',
r'''\textbf{(a)} A regular $n$-gon has interior angles $\dfrac{(n-2)180^\circ}{n}$: $108^\circ$ for $n=5$, $144^\circ$ for $n=10$ and $150^\circ$ for $n=12$. Since $108^\circ+108^\circ+150^\circ=366^\circ\ne360^\circ$, two pentagons and a dodecagon do not fit around a point, while $108^\circ+108^\circ+144^\circ=360^\circ$, so two pentagons and a decagon do.
'''+asy(fig,'5cm')+r'''
\textbf{(b)} Suppose such a tiling exists, and look at one pentagon $P$. At each vertex $V$ of $P$ there are exactly three tiles: $P$, one other pentagon and one decagon. The two edges of $P$ at $V$ separate $P$ from its two neighbours at $V$; each of these edges is shared with one of the other two tiles at $V$ (the tiling is edge-to-edge). So at every vertex of $P$, the two edges of $P$ meeting there are shared with tiles of \emph{different} kinds: one with a pentagon and one with the decagon.

Going around $P$, the kinds of the neighbours across its edges $e_1,e_2,e_3,e_4,e_5$ must therefore alternate: pentagon, decagon, pentagon, decagon, \dots\ But there are $5$ edges, an odd number, so $e_5$ and $e_1$, which meet at a vertex of $P$, would have neighbours of the same kind. This contradiction shows that no such tiling exists. $\blacksquare$

(The same argument shows that a vertex type $a.b.c$ with $a$ odd can occur everywhere in a tiling only if $b=c$; vertex types that fit around one point need not extend to a tiling.)''',
'Regular polygons|Colourings, tilings, and coverings|Angle sums|Parity|Proof by contradiction',5,
note='The post says 5, 5 and 12 meet at a vertex; they do not (108 + 108 + 150 = 366). The intended configuration is two pentagons and a decagon (5.5.10), which fits around a point but cannot tile the plane; the record corrects the polygon and asks for the proof. The general question "a way to tell if a vertex type tiles" is answered only by the parity remark.')

# ---------------- 1717425 primes (2p-q)^2=17p-10q
b.add(1717425,1,r'''Find all prime numbers $p$ and $q$ such that
\[
(2p-q)^2=17p-10q .
\]''',
r'''\textbf{Case $p=q$.} Then $p^2=7p$, so $p=q=7$.

\textbf{Case $p\ne q$.} Reducing modulo $p$: $q^2\equiv-10q$, so $p\mid q(q+10)$, and since $p\nmid q$, $p\mid q+10$. Write $q+10=kp$ with $k\ge1$. Also the left side is positive (it is a nonzero square, as $2p=q$ is impossible for odd $q$, and $q=2$, $p=1$ is not allowed), so $17p>10q$, i.e.\ $q<1.7p$. Then $kp-10<1.7p$, so $(k-1.7)p<10$.
\begin{itemize}
\item $k=1$: $q=p-10$. Modulo $q$ the equation gives $q\mid p(4p-17)$, so $q\mid4p-17=4q+23$, hence $q=23$ and $p=33$, not prime.
\item $k=2$: $q=2p-10$, and the equation becomes $100=17p-20p+100$, so $p=0$: impossible.
\item $k=3$: $1.3p<10$ gives $p\le7$, and $q=3p-10$: $p=5$ gives $q=5=p$ (excluded here), $p=7$ gives $q=11$; check: $(14-11)^2=9=119-110$. \checkmark ($p=2,3$ give $q\le0$.)
\item $k=4$: $2.3p<10$ gives $p\in\{2,3\}$, $q=4p-10\in\{-2,2\}$; $(p,q)=(3,2)$: $16\ne31$.
\item $k=5$: $3.3p<10$ gives $p\in\{2,3\}$, $q=5p-10\in\{0,5\}$; $(p,q)=(3,5)$: $(6-5)^2=1=51-50$. \checkmark
\item $k\ge6$: $4.3p<10$ gives $p=2$, and $q=2k-10$ is even, so $q=2=p$, excluded.
\end{itemize}
The solutions are $\boxed{(p,q)=(3,5),\ (7,7),\ (7,11)}$.''',
'Prime numbers|Diophantine equations|Divisibility|Casework|Bounding and extremal cases',5,source=src('Junior Regional Olympiad FBH',2014,'Grade 8',4),
note='Federation of Bosnia and Herzegovina Junior Regional Olympiad 2014, Grade 8, Problem 4. Checked by search over primes below 2000.')

# ---------------- 1722827 perfect-square coefficients of (x+2y-3)^5
b.add(1722827,1,r'''When $(x+2y-3)^5$ is expanded and like terms are collected, how many of the terms have a coefficient that is a perfect square?''',
r'''By the multinomial theorem, for $a+b+c=5$ the term containing $x^ay^b$ is
\[
\dfrac{5!}{a!\,b!\,c!}\,2^b(-3)^c\,x^ay^b ,
\]
and there are $\dbinom{7}{2}=21$ terms, one for each $(a,b,c)$. A coefficient with $c$ odd is negative, hence not a square. For $c\in\{0,2,4\}$ write $M=\dfrac{5!}{a!b!c!}\in\{1,5,10,20,30\}$ for the multinomial coefficient; the coefficient is $M\cdot2^b\cdot3^c$, and $3^c$ is a square, so we need $M\cdot2^b$ to be a square.
\begin{itemize}
\item $c=0$: $(a,b)=(5,0),(4,1),(3,2),(2,3),(1,4),(0,5)$ give $1,\ 5\cdot2,\ 10\cdot4,\ 10\cdot8,\ 5\cdot16,\ 32$, i.e.\ $1,10,40,80,80,32$: only $1$ is a square.
\item $c=2$: $(a,b)=(3,0),(2,1),(1,2),(0,3)$ give $M2^b=10,\ 30\cdot2,\ 30\cdot4,\ 10\cdot8$: none is a square ($10,60,120,80$).
\item $c=4$: $(a,b)=(1,0),(0,1)$ give $5,\ 5\cdot2$: not squares.
\end{itemize}
So exactly $\boxed{1}$ term, $x^5$ (coefficient $1$), has a perfect-square coefficient.''',
'Binomial theorem|Perfect squares|Casework|Combinatorial identities and binomial coefficients',3,
note='The answer 1 (only x^5) was checked by expanding the polynomial.')

# ---------------- 1723123 general term of 5,8,15,26,...
b.add(1723123,1,r'''Find a formula for the $n$th term of the sequence $5,8,15,26,41,60,\dots$, given that the second differences are constant.''',
r'''The first differences are $3,7,11,15,19$ and the second differences are all $4$. A sequence with constant second difference $4$ is a quadratic $a_n=An^2+Bn+C$ with $2A=4$, so $A=2$. (In general, for $a_n=An^2+Bn+C$ the first differences are $a_{n+1}-a_n=2An+A+B$ and the second differences are $2A$.) Now
\[
a_1=2+B+C=5,\qquad a_2=8+2B+C=8\quad\Longrightarrow\quad B=-3,\ C=6 .
\]
So $\boxed{a_n=2n^2-3n+6}$. Check: $a_3=18-9+6=15$, $a_4=32-12+6=26$, $a_5=50-15+6=41$, $a_6=72-18+6=60$.

The general method: if the $k$th differences of a sequence are constant, its terms are given by a polynomial of degree $k$ in $n$, whose coefficients can be found from the first $k+1$ terms. (No exponents are involved.)''',
'Sequences and series|Polynomials|Systems of linear equations|Pattern recognition',2,
note='The poster asks for the general term and a general method; the sequence is read as continuing with constant second difference 4.')

# ---------------- 1723135 sum of 4-digit palindromes (alias)
b.add(1723135,1,r'''Find the sum of all four-digit palindromes.''',
r'''A four-digit palindrome is $\overline{abba}=1001a+110b$ with $1\le a\le9$, $0\le b\le9$. The sum is $1001\cdot45\cdot10+110\cdot45\cdot9=450450+44550=\boxed{495000}$.''',
'Palindromes|Digits and bases|Summation',2,
note='Repeat of an earlier record (aliased).')

# ---------------- 1722852 6x6 grid distances
b.add(1722852,1,r'''Two different points are chosen at random from the $36$ points of a $6\times6$ square array of lattice points (adjacent points $1$ unit apart). What is the probability that the distance between them is either $1$ or $\sqrt2$?''',
r'''There are $\dbinom{36}{2}=630$ equally likely pairs.

Pairs at distance $1$ are horizontally or vertically adjacent: each of the $6$ rows has $5$ adjacent pairs, and so does each column, giving $2\cdot6\cdot5=60$.

Pairs at distance $\sqrt2$ are opposite corners of a unit square: there are $5\cdot5=25$ unit squares, each with $2$ diagonals, giving $50$.

The probability is $\dfrac{60+50}{630}=\dfrac{110}{630}=\boxed{\dfrac{11}{63}}$.''',
'Probability|Counting shapes in figures|Combinations',2,
note='"A 6x6 grid" is read as a 6 by 6 array of points (if it meant 6 by 6 unit squares, i.e. 7 by 7 points, the answer would be 156/1176 = 13/98).')

# ---------------- 1721400 factorions
b.add(1721400,1,r'''The number $145$ equals the sum of the factorials of its digits: $145=1!+4!+5!$.
\begin{enumerate}
\item[(a)] Verify that $40585$ has the same property.
\item[(b)] Prove that every positive integer with this property has at most $7$ digits.
\end{enumerate}''',
r'''\textbf{(a)} $4!+0!+5!+8!+5!=24+1+120+40320+120=40585$. \checkmark

\textbf{(b)} Suppose $N$ has $d$ digits. Each digit's factorial is at most $9!=362880$, so the sum of the digit factorials is at most $362880d$, while $N\ge10^{d-1}$. For $d=8$: $8\cdot362880=2903040<10^7$. For larger $d$ the gap only widens: going from $d$ to $d+1$ multiplies $10^{d-1}$ by $10$ but increases $362880d$ by a factor $\dfrac{d+1}{d}\le\dfrac98$. So for every $d\ge8$, $362880d<10^{d-1}\le N$, and $N$ cannot equal its digit-factorial sum. Hence such numbers have at most $7$ digits. $\blacksquare$

(In fact one can sharpen this: a $7$-digit $N$ is at most $7\cdot9!=2540160$. A finite check, best done by computer, shows that the only such numbers are $1,2,145$ and $40585$.)''',
'Factorials|Digits and bases|Bounding and extremal cases',3,
note='The post asks whether there are numbers other than 1, 2 and 145 equal to the sum of the factorials of their digits. The complete list (1, 2, 145, 40585) needs a computer search; the record asks to verify 40585 and to prove the digit bound that makes the search finite.')

# ---------------- 1723186 WWPMT 2017 #11
b.add(1723186,1,r'''In a frisbee tournament there are $8$ teams. In the first round there are $4$ games, each between two teams, and each team plays exactly once. In how many ways can the tournament director set up the first round, if only the pairings of the teams matter?

$\textbf{(A) }60\qquad\textbf{(B) }105\qquad\textbf{(C) }210\qquad\textbf{(D) }455\qquad\textbf{(E) }2520$''',
r'''Take the team with the smallest label: its opponent can be chosen in $7$ ways. Among the remaining $6$ teams, the smallest-labelled one has $5$ possible opponents, then $3$, then $1$. So there are $7\cdot5\cdot3\cdot1=105$ pairings. (Equivalently, $\dfrac{8!}{2^4\cdot4!}=\dfrac{40320}{384}=105$: order all teams, pair them off consecutively, and divide by the orders within each pair and the order of the pairs.) The answer is $\boxed{\textbf{(B) }105}$.''',
'Combinations|Multiplication principle|Partitions and compositions',2,source=src('WWPMT',2017,None,11))

# ---------------- 1722616 squaring both sides
b.add(1722616,1,r'''\begin{enumerate}
\item[(a)] Solve $\sqrt{2x+7}=x+2$ over the real numbers. Squaring both sides gives a quadratic with two roots; show that only one of them solves the original equation, and explain why.
\item[(b)] Explain why cubing both sides of an equation never introduces such extra solutions.
\end{enumerate}''',
r'''\textbf{(a)} Squaring gives $2x+7=x^2+4x+4$, i.e.\ $x^2+2x-3=0$, so $(x+3)(x-1)=0$ and $x=1$ or $x=-3$.
\begin{itemize}
\item $x=1$: $\sqrt9=3=1+2$. \checkmark
\item $x=-3$: $\sqrt1=1$ but $x+2=-1$, so it fails.
\end{itemize}
So the only solution is $\boxed{x=1}$. Squaring is a valid step in one direction: if $A=B$ then $A^2=B^2$. But the converse fails: $A^2=B^2$ means $A=B$ \emph{or} $A=-B$. The value $x=-3$ solves $\sqrt{2x+7}=-(x+2)$, not the original equation. That is why every root of the squared equation must be checked (or the condition $x+2\ge0$ imposed).

\textbf{(b)} The function $t\mapsto t^3$ is strictly increasing on the real numbers, hence one-to-one: $A^3=B^3$ implies $A=B$ (indeed $A^3-B^3=(A-B)\left(A^2+AB+B^2\right)$, and the second factor is positive unless $A=B=0$). So for real numbers, cubing both sides gives an \emph{equivalent} equation, and no extraneous solutions appear. The same holds for taking cube roots.''',
'Radical equations|Quadratic equations|Sum and difference of cubes',2,
note='The post asks whether squaring both sides is "valid" and about cubing; the record makes this a worked question. Near-miss of aops-topic-3361787-q01 (sqrt(x+2) = x), with a different equation and the cubing part.')

# ---------------- 1722825 domain
b.add(1722825,1,r'''Find all real numbers $x$ for which there is a real number $y$ satisfying
\[
|x^2|+2|xy|-3=|y| .
\]''',
r'''Write $t=|y|\ge0$. The equation is $x^2+2|x|t-3=t$, i.e.
\[
t\,(2|x|-1)=3-x^2 .
\]
\begin{itemize}
\item If $|x|=\dfrac12$: the left side is $0$ but $3-\dfrac14\ne0$. No solution.
\item If $|x|<\dfrac12$: $2|x|-1<0$ while $3-x^2>0$, so $t<0$. No solution.
\item If $|x|>\dfrac12$: $t=\dfrac{3-x^2}{2|x|-1}$, which is $\ge0$ exactly when $x^2\le3$. Then $y=\pm t$ works.
\end{itemize}
So the set of such $x$ (the ``domain'' of the relation) is $\boxed{-\sqrt3\le x<-\dfrac12\ \text{ or }\ \dfrac12<x\le\sqrt3}$.''',
'Absolute value|Inequalities|Functions|Proof by cases',3,
note='"Domain of the equation" is read as the set of x for which some real y satisfies it.')

# ---------------- 1722491 bounded orbits of x^2+k
b.add(1722491,1,r'''For a real number $k$, define $x_0=0$ and $x_{n+1}=x_n^2+k$ for $n\ge0$. Find all real $k$ for which the sequence $(x_n)$ is bounded (does not diverge to infinity). Write the answer in interval notation.''',
r'''\textbf{$k>\dfrac14$: unbounded.} Then $x_{n+1}-x_n=x_n^2-x_n+k=\left(x_n-\dfrac12\right)^2+k-\dfrac14\ge k-\dfrac14>0$, so the sequence increases by at least the fixed amount $k-\dfrac14$ each step and tends to infinity.

\textbf{$0\le k\le\dfrac14$: bounded.} If $0\le x_n\le\dfrac12$, then $0\le x_{n+1}=x_n^2+k\le\dfrac14+\dfrac14=\dfrac12$. Since $x_0=0$, induction gives $0\le x_n\le\dfrac12$ for all $n$.

\textbf{$-2\le k<0$: bounded.} Let $c=-k\in(0,2]$. If $|x_n|\le c$, then $x_{n+1}=x_n^2-c$ satisfies $-c\le x_{n+1}\le c^2-c\le c$, the last step because $c\le2$. Since $x_0=0$, induction gives $|x_n|\le c$ for all $n$.

\textbf{$k<-2$: unbounded.} Let $c=-k>2$. Then $x_1=-c$ and $x_2=c^2-c=c(c-1)>c$. If $x_n>c$, then
\[
x_{n+1}-x_n=x_n^2-x_n-c>x_n^2-2x_n=x_n(x_n-2)>c(c-2)>0 ,
\]
so from $n=2$ on the sequence increases by more than the fixed amount $c(c-2)$ each step and tends to infinity.

Hence the sequence is bounded exactly for $\boxed{k\in\left[-2,\dfrac14\right]}$.

(For some $k$ in this interval the sequence is bounded but does not converge; for example $k=-1$ gives $0,-1,0,-1,\dots$. ``Does not diverge'' is read here as ``stays bounded''.)''',
'Recurrence relations|Sequences and series|Inequalities|Mathematical induction|Proof by cases',6,
note='"Does not diverge" is read as "stays bounded" (the real slice of the Mandelbrot set); with "converges" the answer would be different (k = -1 gives an oscillating bounded sequence). Checked numerically for many k.')

# ---------------- 1722841 product of (x - j^2) mod 13
b.add(1722841,1,r'''Prove that, as polynomials with coefficients taken modulo $13$,
\[
(x-1^2)(x-2^2)(x-3^2)(x-4^2)(x-5^2)(x-6^2)\equiv x^6-1\pmod{13},
\]
that is, the two sides have coefficients that agree modulo $13$.''',
r'''\textbf{The six squares are distinct roots of $x^6-1$.} Modulo $13$ the squares are $1,4,9,16\equiv3,25\equiv12,36\equiv10$: six different residues $r_1,\dots,r_6$. Each is $r=j^2$ with $13\nmid j$, so by Fermat's little theorem $r^6=j^{12}\equiv1$. Thus every $r_i$ is a root of $x^6-1$ modulo $13$.

\textbf{Comparing the polynomials.} Let $P(x)=\prod_{i=1}^{6}(x-r_i)$ and $D(x)=P(x)-(x^6-1)$. Both are monic of degree $6$, so $D$ has degree at most $5$, and $D(r_i)\equiv0-0=0$ for the six distinct residues $r_i$. Over the integers modulo the prime $13$, a nonzero polynomial of degree at most $5$ has at most $5$ roots (if $D(r)\equiv0$, then $D(x)\equiv(x-r)E(x)$, and since $13$ is prime a product is $0$ only if a factor is, so roots of $D$ other than $r$ are roots of $E$; induct on the degree). Hence all coefficients of $D$ are divisible by $13$, which is the claim. $\blacksquare$

(The residues $1,3,4,9,10,12$ are the quadratic residues modulo $13$, and the identity is a case of Euler's criterion.)''',
'Quadratic residues|Polynomials|Polynomial roots|Fermat\'s little theorem|Remainders and congruences',5,
note='Checked by expanding the product and reducing the coefficients modulo 13.')

# ---------------- 1721070 MATHCOUNTS warm-up #75 and #79
b.add(1721070,75,r'''Jalacia erases some integers from the list
\[
5,\ 9,\ 2,\ 3,\ 7,\ 8,\ 6,\ 5,\ 6,\ 4,\ 1,\ 7,\ 9,\ 8 .
\]
When she is done, the range of the remaining list is $2$. What is the least possible number of integers that Jalacia could have erased?''',
r'''If the remaining list has range $2$, its values lie in some window $\{m,m+1,m+2\}$ (with both $m$ and $m+2$ present). To erase as few numbers as possible, keep every number in the best window. The list has $14$ numbers, with counts: $1,2,3,4$ once each and $5,6,7,8,9$ twice each. The windows hold
\[
\{1,2,3\}:3,\ \{2,3,4\}:3,\ \{3,4,5\}:4,\ \{4,5,6\}:5,\ \{5,6,7\}:6,\ \{6,7,8\}:6,\ \{7,8,9\}:6 .
\]
At most $6$ numbers can remain, for example $5,7,6,5,6,7$ (range $7-5=2$). So at least $14-6=\boxed{8}$ numbers must be erased.''',
'Range|Bounding and extremal cases',2,
note='Two problems (75 and 79) from a MATHCOUNTS warm-up, kept with their numbers.')
b.add(1721070,79,r'''If $a=2+\dfrac34+\dfrac56$ and $b=\dfrac64+\dfrac32$, what is the value of $\dfrac ab$? Express your answer as a common fraction.''',
r'''With denominator $12$: $a=\dfrac{24}{12}+\dfrac{9}{12}+\dfrac{10}{12}=\dfrac{43}{12}$, and $b=\dfrac32+\dfrac32=3$. So $\dfrac ab=\dfrac{43}{12\cdot3}=\boxed{\dfrac{43}{36}}$.''',
'Fractions|Order of operations',1,
note='The post writes a = 2+3/4+(5/6) and b = 6/4+(3/2); the slashes are read as fractions.')

b.save()
