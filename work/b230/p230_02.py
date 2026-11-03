from qb import *
b=Bank('p230_02')

# ---------------- 1734807 coupon collector, 4 minigames
b.add(1734807,1,r'''A trial version of a game offers four different minigames. Each time the game is installed it chooses one of the four minigames at random (each with probability $\dfrac14$, independently of earlier installs), and only that minigame can be played. A player keeps uninstalling and reinstalling the game until every minigame has been offered at least once.
\begin{enumerate}
\item[(a)] What is the expected number of installs, counting the first one?
\item[(b)] Find a formula for the expected number of installs if there are $n$ minigames.
\end{enumerate}''',
r'''\textbf{(b) first.} Suppose $k$ different minigames have been seen so far ($0\le k<n$). Each new install shows a new minigame with probability $p_k=\dfrac{n-k}{n}$, so the number of installs until the next new one is geometric with mean $\dfrac1{p_k}=\dfrac{n}{n-k}$. Adding the expected waiting times for $k=0,1,\dots,n-1$ (linearity of expectation),
\[
E_n=\dfrac nn+\dfrac n{n-1}+\cdots+\dfrac n1=n\left(1+\dfrac12+\dfrac13+\cdots+\dfrac1n\right).
\]

\textbf{(a)} For $n=4$:
\[
E_4=4\left(1+\dfrac12+\dfrac13+\dfrac14\right)=4\cdot\dfrac{25}{12}=\boxed{\dfrac{25}{3}}\approx8.33
\]
installs. (Not counting the first install, the expected number of reinstalls is $\dfrac{25}3-1=\dfrac{22}3$.)''',
'Expected value|Geometric distribution|Probability',4,
note='The coupon-collector problem; the picture in the post is decorative. "Average number of uninstalls/installs" is read as the expected number of installs including the first (the number of reinstalls, 22/3, is also given). The bonus question is part (b).')

# ---------------- 1736828 2015 AMC 8 #25 largest square
L=r'''real a=(5-sqrt(5))/2;
fill(box((0,0),(1,1)),gray(0.65));fill(box((4,0),(5,1)),gray(0.65));fill(box((4,4),(5,5)),gray(0.65));fill(box((0,4),(1,5)),gray(0.65));
draw((1,0)--(4,0)--(4,1)--(5,1)--(5,4)--(4,4)--(4,5)--(1,5)--(1,4)--(0,4)--(0,1)--(1,1)--cycle,linewidth(0.9));
draw(box((0,0),(5,5)),dashed+gray(0.5));'''
fig=L+r'''
filldraw((a,0)--(5,a)--(5-a,5)--(0,5-a)--cycle,rgb(0.82,0.9,1),blue+linewidth(0.8));
dot((4,1));dot((4,4));dot((1,4));dot((1,1));
label("$a$",(a/2,0),S);label("$5-a$",((5+a)/2,0),S);
label("$P$",(4.5,0.5));'''
b.add(1736828,1,r'''One-inch squares are cut from the corners of a $5$-inch square. What is the area, in square inches, of the largest square that can be fitted into the remaining space?
\[
\textbf{(A)}\ 9\qquad\textbf{(B)}\ 12\dfrac12\qquad\textbf{(C)}\ 15\qquad\textbf{(D)}\ 15\dfrac12\qquad\textbf{(E)}\ 17
\]''',
r'''Put the $5$-inch square at $0\le x,y\le5$. An upright square must fit inside the cross-shaped region, so it has side at most $3$ (area $9$). A tilted square does better: place it with one vertex on each side of the $5$-inch square, at $(a,0)$, $(5,a)$, $(5-a,5)$, $(0,5-a)$. Its side is the hypotenuse of a right triangle with legs $a$ and $5-a$, so its area is
\[
a^2+(5-a)^2 ,
\]
which grows as $a$ moves away from $\dfrac52$. The limit is reached when each side passes through the inner corner of a cut-out square, such as $P=(4,1)$:
'''+asy(fig,'5cm')+r'''
The side from $(a,0)$ to $(5,a)$ passes through $(4,1)$ when the slopes agree: $\dfrac{1}{4-a}=\dfrac{a}{5-a}$, i.e.\ $a^2-5a+5=0$, so $a=\dfrac{5-\sqrt5}{2}$ (the root between $1$ and $4$). Then
\[
a^2+(5-a)^2=\left(\dfrac{5-\sqrt5}{2}\right)^2+\left(\dfrac{5+\sqrt5}{2}\right)^2=\dfrac{(30-10\sqrt5)+(30+10\sqrt5)}{4}=15 .
\]
So the largest square has area $\boxed{15}$, answer $\textbf{(C)}$.

(A $3\times5$ rectangle also has area $15$ and fits, but it is not a square, so it does not answer the question; the agreement of the areas is a coincidence.)''',
'Squares|Right triangles|Pythagorean theorem|Lengths, perimeter, and area|Bounding and extremal cases',5,source=src('AMC 8',2015,None,25),
note='The figure was attached; the text determines it. The poster found 15 with a 3 by 5 rectangle; the solution explains why that is not the answer to the question although the number agrees. The maximality of the tilted square (official answer C) was confirmed by a numerical search over squares in all positions and orientations. Near-miss of aops-topic-2501508-q01, which gives this tilted square in a figure and asks for its area.')

# ---------------- 1737548 largest equilateral triangle in the notched square
fig=L+r'''
pair U=(2.5,0),V=(2.5+4/sqrt(3),4),Wv=(2.5-4/sqrt(3),4);
filldraw(U--V--Wv--cycle,rgb(0.82,0.9,1),blue+linewidth(0.8));
draw((2.5,0)--(2.5,4),dashed+blue);
label("$4$",(2.5,2.6),E,blue);'''
b.add(1737548,1,r'''One-inch squares are cut from the corners of a $5$-inch square. What is the area, in square inches, of the largest equilateral triangle that can be fitted into the remaining space?''',
r'''Put the $5$-inch square at $0\le x,y\le5$; the remaining region $R$ consists of the points of the square that are not in a corner, i.e.\ not with ($x<1$ or $x>4$) and ($y<1$ or $y>4$).

\textbf{An upper bound.} Let $T$ be an equilateral triangle in $R$ with altitude $h$. The width of an equilateral triangle in any direction is at least its altitude, so the horizontal extent and the vertical extent of $T$ are both at least $h$. Suppose $h>4$. Since $T$ lies in $0\le x\le5$ and its horizontal extent exceeds $4$, its leftmost point has $x<1$ and its rightmost point has $x>4$; similarly its lowest point has $y<1$ and its highest point has $y>4$. These four extreme points can be taken to be vertices of $T$. A triangle has only three vertices, so one vertex plays two of the four roles; it cannot be both leftmost and rightmost, or both lowest and highest, so it is, say, leftmost and lowest, with $x<1$ and $y<1$. That vertex lies in a cut-out corner, a contradiction. Hence $h\le4$.

\textbf{The bound is attained.} Take the triangle with one vertex at $(2.5,0)$ and the opposite side on the line $y=4$, so its altitude is $4$:
'''+asy(fig,'5cm')+r'''
Its side is $\dfrac{2h}{\sqrt3}=\dfrac{8}{\sqrt3}$, so the top vertices are $\left(2.5\pm\dfrac4{\sqrt3},4\right)\approx(0.19,4)$ and $(4.81,4)$, which lie in $R$. The slanted sides stay clear of the lower cut-outs: on the right side, at height $y=1$ the point is at $x=2.5+\dfrac{1}{\sqrt3}\approx3.08<4$. So the triangle fits, and the largest area is
\[
\dfrac{\sqrt3}{4}\left(\dfrac{8}{\sqrt3}\right)^2=\boxed{\dfrac{16\sqrt3}{3}}\approx9.24\text{ square inches}.
\]''',
'Equilateral triangles|Lengths, perimeter, and area|Bounding and extremal cases|Pigeonhole principle',6,
note='A variant (posted as "Nostalgia") of 2015 AMC 8 #25 with an equilateral triangle instead of a square; no answer was posted. The answer 16 sqrt 3 / 3 was confirmed by a numerical search over all positions and orientations.')

# ---------------- 1733948 chest probability
b.add(1733948,1,r'''Each chest in a game independently contains a special item with probability $\dfrac1{20}$. A player has opened nine chests and has not yet found the item. What is the probability that the tenth chest contains it?''',
r'''The chests are independent, so what happened in the first nine chests does not affect the tenth. The probability is $\boxed{\dfrac1{20}}$.

(This is different from the probability, computed before any chest is opened, that the item is found \emph{for the first time} at the tenth chest, which is $\left(\dfrac{19}{20}\right)^9\cdot\dfrac1{20}\approx0.0315$.)''',
'Independent events|Conditional probability|Probability',1,
note='The post asks for the probability on the tenth chest "consider that I have not gotten the item before"; read as the conditional probability (1/20). The unconditional first-success probability is also given.')

# ---------------- 1737138 2012 Chapter Sprint 25 (alias)
b.add(1737138,1,r'''A car traveled a certain distance at $20$ miles per hour. The car then traveled twice the original distance at $40$ miles per hour. If the entire trip lasted four hours, what was the total number of miles driven?''',
r'''Let the first distance be $d$ miles. The times are $\dfrac d{20}$ and $\dfrac{2d}{40}=\dfrac d{20}$ hours, so $\dfrac d{10}=4$ and $d=40$. The total distance is $3d=\boxed{120}$ miles.''',
'Distance, rate, and time|Linear equations',2,source=src('MATHCOUNTS',2012,'Chapter',25,rnd='Sprint'),
note='Repeat of an earlier record (aliased).')

# ---------------- 1737089 0^0
b.add(1737089,1,r'''Explain why $0^0$ is often left undefined: show that
\[
\lim_{x\to0^+}x^0=1\qquad\text{but}\qquad\lim_{y\to0^+}0^y=0,
\]
and conclude that no value assigned to $0^0$ makes the function $f(x,y)=x^y$ (defined for $x\ge0$, $y>0$ and for $x>0$, $y=0$) continuous at $(0,0)$. Why do algebra and combinatorics nevertheless use the convention $0^0=1$?''',
r'''For every $x>0$ we have $x^0=1$, so $\lim_{x\to0^+}x^0=1$. For every $y>0$ we have $0^y=0$, so $\lim_{y\to0^+}0^y=0$.

If $f$ were continuous at $(0,0)$ with some value $f(0,0)=c$, then $f$ would tend to $c$ along every path into $(0,0)$. Along the path $(x,0)$, $x\to0^+$, the values are all $1$, forcing $c=1$; along the path $(0,y)$, $y\to0^+$, the values are all $0$, forcing $c=0$. This is impossible, so no choice of $0^0$ makes $x^y$ continuous at $(0,0)$; this is why $0^0$ is called an indeterminate form in analysis. (Other paths give other limits too: along $y=\dfrac{1}{\ln\dfrac1x}$ the value $x^y=e^{-1}$ is constant.)

In algebra and combinatorics, however, $a^0$ means the empty product, which is $1$ for every $a$, and with $0^0=1$ formulas such as $(1+x)^n=\sum_k\binom nk x^k$ at $x=0$, $\sum_k a_kx^k$ at $x=0$, and ``the number of functions from an $m$-set to an $n$-set is $n^m$'' (one function from the empty set) hold without exceptions. So $0^0=1$ is the useful convention there, while in limits $0^0$ has no single value.''',
'Exponents|Calculus|Counterexamples',3,
note='The post asks why 0^0 is not 1 and for a proof that it is undefined; turned into an explanation of the two competing limits and the convention.')

# ---------------- 1736178 four MATHCOUNTS problems
fig=r'''pair A=(-4,2),B=(1,2),C=(-1,5),A2=(4,2),B2=(-1,2),C2=(1,5);
fill(B2--B--(0,3.5)--cycle,gray(0.7));
draw((-5,0)--(5,0),Arrow(TeXHead));draw((0,-0.6)--(0,6),Arrow(TeXHead));
label("$x$",(5,0),S);label("$y$",(0,6),W);
draw(A--B--C--cycle,blue+linewidth(0.9));draw(A2--B2--C2--cycle,red+linewidth(0.9)+dashed);
label("$A$",A,W);label("$B$",B,dir(-60));label("$C$",C,N);
label("$A'$",A2,E);label("$B'$",B2,dir(240));label("$C'$",C2,N);
dot((0,3.5));'''
b.add(1736178,1,r'''Points $A$, $B$ and $C$ have coordinates $(-4,2)$, $(1,2)$ and $(-1,5)$, respectively. If triangle $ABC$ is reflected across the $y$-axis, what is the area of the region that is the intersection of triangle $ABC$ and its reflection? Express your answer as a decimal to the nearest tenth.''',
r'''The reflection is $A'=(4,2)$, $B'=(-1,2)$, $C'=(1,5)$. Both triangles have their bases on the line $y=2$, and the intersection is bounded below by $y=2$ and above by the sides $BC$ and $B'C'$:
'''+asy(fig,'6.5cm')+r'''
Line $BC$ through $(1,2)$ and $(-1,5)$ is $y=2-\dfrac32(x-1)$, and line $B'C'$ is its mirror image $y=2+\dfrac32(x+1)$. They meet on the $y$-axis at $(0,3.5)$. The other sides do not cut into this region (for example $AC$ is $y=x+6$, far above it). So the intersection is the triangle with vertices $(-1,2)$, $(1,2)$, $(0,3.5)$, with base $2$ and height $1.5$, and its area is $\dfrac12\cdot2\cdot1.5=\boxed{1.5}$.''',
'Coordinate geometry|Reflections|Triangles|Lengths, perimeter, and area',3,
note='One of four problems in the post (q01-q04 in order).')
b.add(1736178,2,r'''If Desi flips a fair coin eight times, what is the probability that he gets the same number of heads and tails? Express your answer as a common fraction.''',
r'''He needs exactly $4$ heads in $8$ flips. There are $\binom84=70$ such sequences out of $2^8=256$, so the probability is $\dfrac{70}{256}=\boxed{\dfrac{35}{128}}$.''',
'Binomial probability|Combinations|Probability',2)
fig=r'''pair[] Q={(0,0),(2,0),(2,2),(0,2)};
draw(Q[0]--Q[1]--Q[2]--Q[3]--cycle,linewidth(0.9));draw(Q[1]--(3.1,0),dashed);
draw(arc(Q[1],0.45,0,90));label("$90^\circ$",Q[1]+0.8*dir(45),fontsize(8pt));
pair c=(5.6,1); real R=1.08; pair[] G; for(int i=0;i<8;++i) G.push(c+R*dir(-112.5+45*i));
draw(G[0]--G[1]--G[2]--G[3]--G[4]--G[5]--G[6]--G[7]--cycle,linewidth(0.9));
pair e=G[1]+0.95*unit(G[1]-G[0]); draw(G[1]--e,dashed);
draw(arc(G[1],0.45,degrees(G[1]-G[0]),degrees(G[2]-G[1])));label("$45^\circ$",G[1]+0.85*dir((degrees(G[1]-G[0])+degrees(G[2]-G[1]))/2),fontsize(8pt));'''
b.add(1736178,3,r'''For positive integers $n$ and $m$, each exterior angle of a regular $n$-sided polygon is $45$ degrees larger than each exterior angle of a regular $m$-sided polygon. One example is $n=4$ and $m=8$, because the exterior angles of a square and a regular octagon are $90^\circ$ and $45^\circ$. What is the greatest possible value of $m$?''',
r'''The exterior angle of a regular $k$-gon is $\dfrac{360^\circ}{k}$, so
\[
\dfrac{360}{n}-\dfrac{360}{m}=45\iff\dfrac8n-\dfrac8m=1\iff 8m-8n=mn\iff(8-n)(m+8)=64 .
\]
Since $m+8>8$, the factor $8-n$ is a positive divisor of $64$ less than $8$, i.e.\ $1$, $2$ or $4$, and $n\ge3$ allows all three: $n=7,m=56$; $n=6,m=24$; $n=4,m=8$. The greatest value is $m=\boxed{56}$. (Check: $\dfrac{360}{7}-\dfrac{360}{56}=\dfrac{2880-360}{56}=45$.) The exterior angle is the turn between one side and the extension of the previous side; for the example in the statement:
'''+asy(fig,'5cm'),
'Regular polygons|Angle sums|Diophantine equations|Factoring',3)
b.add(1736178,4,r'''On a standard die each face shows a different number from $1$ through $6$. Jake has a die whose six faces show the expressions
\[
a+1,\quad 2a-5,\quad 3a-10,\quad b+8,\quad 2b+5,\quad 3b+10,
\]
in no particular order, and their values are the six numbers $1$ through $6$. If $a$ and $b$ are integers, what is the value of the product $ab$?''',
r'''Every value lies between $1$ and $6$. From $a+1\le6$ we get $a\le5$, and from $3a-10\ge1$ we get $a\ge\dfrac{11}3$, so $a=4$ or $5$. For $a=5$ the values $a+1=6$, $2a-5=5$, $3a-10=5$ repeat, so $a=4$, giving the values $5,3,2$.

From $b+8\le6$ we get $b\le-2$, and from $3b+10\ge1$ we get $b\ge-3$. For $b=-3$, $2b+5=-1$ is too small, so $b=-2$, giving $6,1,4$. Together the six values are $5,3,2,6,1,4$, all different, as required. Hence $ab=4\cdot(-2)=\boxed{-8}$.''',
'Linear equations|Inequalities|Casework',3)

# ---------------- 1736995 two short exercises
b.add(1736995,1,r'''For what value of $x$ is the square of the binomial $2x+10$ four times as large as the square of the binomial $x-5$?''',
r'''We need $(2x+10)^2=4(x-5)^2=\bigl(2(x-5)\bigr)^2$, so $2x+10=\pm(2x-10)$. The plus sign gives $10=-10$, impossible. The minus sign gives $2x+10=-2x+10$, so $x=\boxed{0}$. Check: $(10)^2=100=4\cdot(-5)^2$.''',
'Quadratic equations|Difference of squares|Algebraic expressions and identities',2,
note='"Four times greater" is read as "four times as large".')
b.add(1736995,2,r'''Write $27a^3$ as the cube of a monomial.''',
r'''Since $27=3^3$, $27a^3=3^3a^3=\boxed{(3a)^3}$.''',
'Exponents|Perfect cubes',1)

# ---------------- 1736372 cubic with roots 2,3,-8
b.add(1736372,1,r'''Find the monic cubic equation $x^3+px^2+qx+r=0$ whose roots are $2$, $3$ and $-8$.''',
r'''The equation is $(x-2)(x-3)(x+8)=0$. Expanding, $(x-2)(x-3)=x^2-5x+6$ and
\[
(x^2-5x+6)(x+8)=x^3+8x^2-5x^2-40x+6x+48=x^3+3x^2-34x+48 .
\]
So the equation is $\boxed{x^3+3x^2-34x+48=0}$. (Check with Vieta: $2+3-8=-3=-p$, $2\cdot3+2(-8)+3(-8)=-34=q$, $2\cdot3\cdot(-8)=-48=-r$.)''',
'Polynomials|Polynomial roots|Vieta\'s formulas',1,
note='The post gives the template ___x^3 + ___x^2 - ___x + ___ = 0; the blanks are 1, 3, 34, 48.')

# ---------------- 1729625 Halloween contest
b.add(1729625,1,r'''Bob leaves to go trick-or-treating at 4:20 pm and looks at his analog watch. To the nearest minute, what is the next time at which the angle between the minute hand and the hour hand is the same as when he started? Express your answer in 24-hour time.''',
r'''At 4:20 the hour hand is at $4\cdot30^\circ+20\cdot\dfrac12^\circ=130^\circ$ (measured clockwise from 12) and the minute hand at $120^\circ$, so the angle is $10^\circ$ with the minute hand behind.

The minute hand gains $6-\dfrac12=\dfrac{11}{2}$ degrees per minute on the hour hand. The angle is next $10^\circ$ when the minute hand is $10^\circ$ \emph{ahead}, i.e.\ after it has gained $20^\circ$, which takes $20\div\dfrac{11}{2}=\dfrac{40}{11}\approx3.64$ minutes. That is about 4:23.6 pm, so to the nearest minute the answer is $\boxed{16{:}24}$.''',
'Clock problems|Relative speed|Calendar and clock problems',3,
note='The phrase "he checks his watch every minute" is ignored, as "to the nearest minute" asks for the rounded time of the exact coincidence (16:23.6, i.e. 16:24). If instead the angle had to be exactly 10 degrees at a whole minute, the next such time would be 19:40.')
b.add(1729625,2,r'''What is the tens digit of $2^{2041}$?''',
r'''We need $2^{2041}\bmod100$. Since $2^{10}=1024\equiv24$ and $2^{20}\equiv24^2=576\equiv76\pmod{100}$, and $76^2=5776\equiv76$, every power $2^{20k}$ with $k\ge1$ is $\equiv76\pmod{100}$. Hence
\[
2^{2041}=2^{20\cdot102}\cdot2\equiv76\cdot2=152\equiv52\pmod{100},
\]
so the last two digits are $52$ and the tens digit is $\boxed{5}$.''',
'Units digits and last digits|Modular exponentiation|Remainders and congruences',3)
b.add(1729625,3,r'''Chester picks $10$ candies one after another; each candy is black or orange with probability $\dfrac12$ each, independently. He gets upset if he ever picks $3$ or more orange candies in a row. What is the probability that he does not get upset after picking all $10$ candies?''',
r'''Let $a_n$ be the number of black/orange sequences of length $n$ with no three consecutive oranges. Sort them by how they end: in B, in BO, or in BOO (or the whole sequence is O or OO for small $n$). This gives $a_n=a_{n-1}+a_{n-2}+a_{n-3}$ for $n\ge4$, with $a_1=2$, $a_2=4$, $a_3=7$. Then
\[
a_4=13,\ a_5=24,\ a_6=44,\ a_7=81,\ a_8=149,\ a_9=274,\ a_{10}=504 .
\]
All $2^{10}=1024$ sequences are equally likely, so the probability is $\dfrac{504}{1024}=\boxed{\dfrac{63}{128}}$.''',
'Recursive counting|Probability|Recurrence relations',4)

# ---------------- 1735431 x+y+z=10
b.add(1735431,1,r'''How many ordered triples $(x,y,z)$ of positive integers satisfy $x+y+z=10$?''',
r'''Think of $10$ stars in a row; choosing two of the $9$ gaps between them to place bars splits the stars into three nonempty groups of sizes $x,y,z$, and every solution arises exactly once. So there are $\binom92=\boxed{36}$ triples.''',
'Stars and bars|Distributions and integer solutions|Diophantine equations',2,
note='"Positive" is read as positive integers.')

# ---------------- 1736376 shift root of cubic
b.add(1736376,1,r'''Let $\alpha$ be a root of $x^3-8x-12$. Find a cubic polynomial which has $\alpha+1$ as a root.''',
r'''Let $y=\alpha+1$, so $\alpha=y-1$ and $(y-1)^3-8(y-1)-12=0$. Expanding,
\[
y^3-3y^2+3y-1-8y+8-12=y^3-3y^2-5y-5=0 .
\]
So $\alpha+1$ is a root of $\boxed{x^3-3x^2-5x-5}$ (and in fact the three roots of this polynomial are the three roots of $x^3-8x-12$ each increased by $1$).''',
'Polynomials|Polynomial roots|Substitution',2)

# ---------------- 447574 two isosceles triangles
fig=r'''pair P=(0,0),Q=(30,0),R=(15,20);pair P2=(38,0),Q2=(78,0),R2=(58,15);
draw(P--Q--R--cycle,linewidth(0.9));draw(P2--Q2--R2--cycle,linewidth(0.9));
draw(R--(15,0),dashed);draw(R2--(58,0),dashed);
draw((15,0)--(16.4,0)--(16.4,1.4)--(15,1.4));draw((58,0)--(59.4,0)--(59.4,1.4)--(58,1.4));
label("$25$",(P+R)/2,NW);label("$25$",(Q+R)/2,NE);label("$15$",(7.5,0),S);label("$15$",(22.5,0),S);
label("$20$",(15,10),W);
label("$25$",(P2+R2)/2,NW);label("$25$",(Q2+R2)/2,NE);label("$20$",(48,0),S);label("$20$",(68,0),S);
label("$15$",(58,7.5),W);'''
b.add(447574,1,r'''Let $A$ be the area of the triangle with sides of length $25$, $25$ and $30$. Let $B$ be the area of the triangle with sides of length $25$, $25$ and $40$. What is the relationship between $A$ and $B$?
\[
\textbf{(A)}\ A=\dfrac9{16}B\qquad\textbf{(B)}\ A=\dfrac34B\qquad\textbf{(C)}\ A=B\qquad\textbf{(D)}\ A=\dfrac43B\qquad\textbf{(E)}\ A=\dfrac{16}9B
\]''',
r'''In an isosceles triangle the altitude to the base bisects the base. Both triangles split into two right triangles with hypotenuse $25$:
'''+asy(fig,'7.5cm')+r'''
In the first, the half-base is $15$ and the altitude is $\sqrt{25^2-15^2}=20$; in the second, the half-base is $20$ and the altitude is $\sqrt{25^2-20^2}=15$. Both are made of two $15$-$20$-$25$ right triangles, so
\[
A=\dfrac12\cdot30\cdot20=300=\dfrac12\cdot40\cdot15=B ,
\]
and the answer is $\boxed{\textbf{(C)}\ A=B}$.''',
'Isosceles triangles|Right triangles|Pythagorean theorem|Lengths, perimeter, and area',2)

# ---------------- 1736176 polynomials with f(1)=18, f(3)=2018
b.add(1736176,1,r'''How many polynomials $f(x)$ are there such that all of the coefficients of $f(x)$ are positive integers (that is, $f(x)=a_dx^d+\cdots+a_1x+a_0$ with every $a_i$ a positive integer), $f(1)=18$ and $f(3)=2018$?''',
r'''Write $f(x)=a_0+x\,g(x)$, where $g$ is again a polynomial with positive integer coefficients (or $g=0$ if $f$ is constant). Then $a_0\equiv f(3)\pmod3$, $g(1)=f(1)-a_0$ and $g(3)=\dfrac{f(3)-a_0}{3}$. So the coefficients are peeled off one at a time: at a state $(N,s)=(h(3),h(1))$ the constant term $a$ satisfies $1\le a\le s$ and $a\equiv N\pmod3$, and the next state is $\left(\dfrac{N-a}{3},\,s-a\right)$; the process ends when $N=s$ and the remaining polynomial is the constant $s$. A state can only lead to a solution if $N\ge s$, and $N\equiv s\pmod2$ (every power of $3$ is odd).

Starting from $(2018,18)$, with $2018\equiv2\pmod3$, the first coefficient is $a_0\in\{2,5,8\}$ with next states $(672,16)$, $(671,13)$, $(670,10)$ (the choices $a_0=11,14,17$ lead to states such as $(669,7)$ whose branches die out after a step or two). Carrying the search through, the complete list of coefficient sequences $(a_0,a_1,\dots,a_d)$ is
\[
\begin{array}{lll}
(2,3,1,2,3,7) & (2,3,1,2,6,3,1) & (2,3,1,5,2,4,1)\\
(2,3,1,8,1,1,2) & (2,3,4,1,3,4,1) & (2,3,4,4,2,1,2)\\
(2,6,3,1,3,1,2) & (5,2,1,2,3,4,1) & (5,2,1,5,2,1,2)\\
(5,2,4,1,3,1,2) & (8,1,1,2,3,1,2) &
\end{array}
\]
For example the first is $f(x)=7x^5+3x^4+2x^3+x^2+3x+2$, with $f(1)=18$ and $f(3)=1701+243+54+9+9+2=2018$. Hence there are $\boxed{11}$ such polynomials.''',
'Polynomials|Digits and bases|Remainders and congruences|Systematic counting',5,
note='Read literally: every coefficient a_0, ..., a_d (up to the degree) is a positive integer. Under the other reading (nonnegative coefficients, i.e. only the nonzero coefficients must be positive) the count is 50. Both counts were checked by exhaustive search.')

# ---------------- 1501275 prealgebra marathon problem 1
b.add(1501275,1,r'''What is $\left(\dfrac45\right)^2$?''',
r'''Square the numerator and the denominator: $\left(\dfrac45\right)^2=\dfrac{4^2}{5^2}=\boxed{\dfrac{16}{25}}$.''',
'Fractions|Exponents',1,
note='Problem 1 of a prealgebra marathon thread.')

# ---------------- 1731630 four MATHCOUNTS problems
fig=r'''for(int i=0;i<=6;++i) draw((i,0)--(i,2),gray(0.6));
for(int j=0;j<=2;++j) draw((0,j)--(6,j),gray(0.6));
pen f=rgb(0.82,0.9,1);
fill(box((0,0),(1,1)),f);fill(box((1,0),(2,1)),f);fill(box((2,0),(3,1)),f);
fill(box((3,1),(4,2)),f);fill(box((4,1),(5,2)),f);fill(box((5,1),(6,2)),f);
for(int i=0;i<=6;++i) draw((i,0)--(i,2),gray(0.6));
for(int j=0;j<=2;++j) draw((0,j)--(6,j),gray(0.6));
draw(box((0,0),(6,2)),linewidth(0.9));
draw((0,0)--(6,2),red+linewidth(0.9));dot((3,1),red);'''
b.add(1731630,1,r'''A $24$-foot by $72$-foot rectangular dance floor is completely tiled with one-foot by one-foot square tiles. Two opposite corners of the dance floor are connected by a diagonal. This diagonal passes through the interior of exactly how many tiles?''',
r'''Go along the diagonal from one corner to the other. It starts in one tile, and it enters a new tile each time it crosses a vertical grid line ($71$ interior lines) or a horizontal grid line ($23$ interior lines), except that when it passes exactly through a lattice point it crosses both lines at once and enters only one new tile.

The diagonal from $(0,0)$ to $(72,24)$ passes through the lattice points $(3k,k)$; the interior ones are $k=1,\dots,23$, that is $\gcd(72,24)-1=23$ points. So the number of tiles is
\[
1+71+23-23=72=72+24-\gcd(72,24),
\]
answer $\boxed{72}$. (Equivalently, the floor splits into $24$ copies of a $3\times1$ block, and the diagonal crosses $3$ tiles in each. The picture shows the same pattern for a $6\times2$ floor: $6+2-2=6$ tiles.)
'''+asy(fig,'6cm'),
'HCF and LCM|Counting principles|Lattice points|Rectangles',3,
note='One of four problems in the post (q01-q04 in order). The figure illustrates the count on a scaled-down 6 by 2 floor.')
fig=r'''int n=4; pair d=(0.45,0.32);
pen f=rgb(0.82,0.9,1);
fill(box((1,1),(n-1,n-1)),f);
fill(((n,1)+d)--((n,1)+(n-1)*d)--((n,n-1)+(n-1)*d)--((n,n-1)+d)--cycle,f);
fill(((1,n)+d)--((n-1,n)+d)--((n-1,n)+(n-1)*d)--((1,n)+(n-1)*d)--cycle,f);
for(int i=0;i<=n;++i){draw((i,0)--(i,n),gray(0.5));draw((0,i)--(n,i),gray(0.5));
 draw((i,n)--(i,n)+n*d,gray(0.5));draw((0,n)+i*d--(n,n)+i*d,gray(0.5));
 draw((n,i)--(n,i)+n*d,gray(0.5));draw((n,0)+i*d--(n,n)+i*d,gray(0.5));}
draw(box((0,0),(n,n)),linewidth(0.9));
draw((0,n)--(0,n)+n*d--(n,n)+n*d--(n,0)+n*d--(n,0),linewidth(0.9));draw((n,n)--(n,n)+n*d,linewidth(0.9));'''
b.add(1731630,2,r'''A large cube is built from unit cubes and then dipped in paint. Afterwards it is taken apart into the original unit cubes, and $486$ of them have exactly one face painted. How many unit cubes were used to build the large cube?''',
r'''Let the large cube be $n\times n\times n$. A unit cube has exactly one painted face when it lies on a face of the large cube but not on an edge, so each face contributes the $(n-2)^2$ cubes of its interior (shaded below for $n=4$):
'''+asy(fig,'4cm')+r'''
Hence $6(n-2)^2=486$, so $(n-2)^2=81$, $n-2=9$ and $n=11$. The number of unit cubes is $11^3=\boxed{1331}$.''',
'Cubes and rectangular prisms|Perfect squares|Perfect cubes',2)
b.add(1731630,3,r'''How many of the natural numbers from $1$ to $600$, inclusive, contain the digit $5$ at least once?''',
r'''Count the complement. Write the numbers $0$ to $599$ with three digits (leading zeros allowed). Those with no digit $5$ have hundreds digit in $\{0,1,2,3,4\}$ ($5$ choices) and tens and units digits from the nine digits other than $5$: $5\cdot9\cdot9=405$ numbers, including $000$. So $404$ of the numbers $1$ to $599$ have no $5$, and so does $600$: $405$ numbers from $1$ to $600$ have no $5$. The answer is $600-405=\boxed{195}$.''',
'Complementary counting|Digits and bases|Multiplication principle',2,
note='The poster counted by the three-place method and asks for a quicker way; the solution uses complementary counting.')
b.add(1731630,4,r'''At the Word Store each vowel sells for a different price, but all consonants are free. The word ``Triangle'' sells for $\$6$, ``square'' for $\$9$, ``pentagon'' for $\$7$, ``cube'' for $\$7$ and ``Tetrahedron'' for $\$8$. What is the dollar cost of the word ``Octahedron''?''',
r'''Let the vowels cost $a,e,i,o,u$. Reading off the vowels of each word:
\[
\text{Triangle: } i+a+e=6,\quad \text{square: } u+a+e=9,\quad \text{pentagon: } e+a+o=7,
\]
\[
\text{cube: } u+e=7,\quad \text{Tetrahedron: } 2e+a+o=8 .
\]
Subtracting pentagon from Tetrahedron gives $e=1$. Then cube gives $u=6$, square gives $a=2$, pentagon gives $o=4$ and Triangle gives $i=3$ (all different, as required). ``Octahedron'' has the vowels O, a, e, o, so it costs $2o+a+e=8+2+1=\boxed{11}$ dollars.''',
'Systems of linear equations|Linear equations',2)

# ---------------- 1735430 Handbook Warm-Up 4 #6, #7
b.add(1735430,1,r'''Preston has four potatoes, each of which weighs a whole number of ounces. The median weight of his potatoes is $11$ ounces, and the mean weight is $12$ ounces. What is the greatest possible difference between the weights of the heaviest and the lightest potato?''',
r'''Let the weights be $w_1\le w_2\le w_3\le w_4$. The mean gives $w_1+w_2+w_3+w_4=48$ and the median gives $w_2+w_3=22$, so $w_1+w_4=26$ and
\[
w_4-w_1=26-2w_1 .
\]
This is largest when $w_1$ is as small as possible, $w_1=1$, giving $w_4=25$; the weights $1,11,11,25$ are valid. The greatest difference is $\boxed{24}$ ounces.''',
'Median|Mean|Bounding and extremal cases',2,source=src('MATHCOUNTS Handbook',2019,None,6,rnd='Warm-Up 4'))
b.add(1735430,2,r'''Photographers often choose a shutter speed, in seconds, equal to the reciprocal of the effective focal length of the lens in millimeters. Jackie shoots at a focal length of $80$ mm, Clarise at $200$ mm and Sage at $400$ mm, and they all apply this reciprocal rule. What focal length corresponds to the sum of their shutter speeds?''',
r'''The shutter speeds are $\dfrac1{80}$, $\dfrac1{200}$ and $\dfrac1{400}$ seconds, and
\[
\dfrac1{80}+\dfrac1{200}+\dfrac1{400}=\dfrac{5+2+1}{400}=\dfrac{8}{400}=\dfrac1{50}.
\]
A shutter speed of $\dfrac1{50}$ second corresponds to a focal length of $\boxed{50}$ mm.''',
'Fractions|Ratios, proportions, and variation',1,source=src('MATHCOUNTS Handbook',2019,None,7,rnd='Warm-Up 4'))

# ---------------- 1735512 Handbook Warm-Up 6 #82, 83, 85, 89
fig=r'''real s=2; pair A=(0,0),B=(s*sqrt(2),0),Ep=(s/sqrt(2),s/sqrt(2)),F=(s/sqrt(2),-s/sqrt(2));
fill(A--(4.4,4.4)--(4.4,-4.4)--cycle,rgb(1,0.92,0.85));fill(A--(-1.2,1.2)--(-1.2,-1.2)--cycle,rgb(1,0.92,0.85));
draw(circle(A,s),linewidth(0.8));draw(circle(B,s),linewidth(0.8));
draw(A--Ep--B--F--cycle,blue);
draw((-1.2,-1.2)--(4.4,4.4),red+linewidth(0.8));draw((-1.2,1.2)--(4.4,-4.4),red+linewidth(0.8));
draw(A--B,dashed);
draw(Ep+0.3*dir(-45)--Ep+0.3*dir(-45)+0.3*dir(-135)--Ep+0.3*dir(-135));
dot(A);dot(B);
label("$A$",A+(-0.5,0));label("$B$",B,E);label("$E$",Ep,N);label("$F$",F,S);
'''
b.add(1735512,82,r'''Circles $A$ and $B$ (centred at points $A$ and $B$) intersect, and points $E$ and $F$ lie on circle $B$ so that quadrilateral $AEBF$ is a square. What is the probability that a randomly chosen line through point $A$ intersects both circles? Express your answer as a common fraction.''',
r'''Every line through $A$ meets circle $A$, since $A$ is its centre. So we need the probability that the line meets circle $B$.

Let the square have side $s$. Then circle $B$ has radius $BE=s$, and $AB=s\sqrt2$ is a diagonal of the square. Since $\angle AEB=90^\circ$, the line $AE$ is perpendicular to the radius $BE$, so it is tangent to circle $B$; likewise $AF$. These tangents make angles of $45^\circ$ with $AB$ (the diagonal of a square bisects its angle):
'''+asy(fig,'6cm')+r'''
A line through $A$ meets circle $B$ exactly when its angle with line $AB$ is at most $45^\circ$ (the shaded double wedge bounded by the two tangent lines). A random line through $A$ has its direction uniformly distributed over $180^\circ$, and $90^\circ$ of these directions work, so the probability is $\dfrac{90}{180}=\boxed{\dfrac12}$.''',
'Geometric probability|Tangents|Circles|Squares',4,source=src('MATHCOUNTS Handbook',2019,None,82,rnd='Warm-Up 6'),
note='The figure was attached; the text determines the answer. "A randomly chosen line through A" is read as a uniformly random direction. The figure draws circle A with radius AE (its radius does not matter).')
b.add(1735512,83,r'''Lauren randomly picks two cards, without replacement, from six cards numbered $2,3,5,6,7$ and $10$. What is the probability that the product of the two numbers on the selected cards is a multiple of $10$? Express your answer as a common fraction.''',
r'''There are $\binom62=15$ equally likely pairs. The product is a multiple of $10$ when the pair contains $10$ ($5$ pairs), or contains $5$ and an even number other than $10$, i.e.\ $\{5,2\}$ or $\{5,6\}$ ($2$ pairs). So the probability is $\dfrac{7}{15}$: $\boxed{\dfrac7{15}}$.''',
'Probability|Sampling without replacement|Divisibility',2,source=src('MATHCOUNTS Handbook',2019,None,83,rnd='Warm-Up 6'))
b.add(1735512,85,r'''Consider the set of all four-digit positive integers less than $2000$ whose digits have a sum of $24$. What is the median of this set of integers?''',
r'''Such a number is $\overline{1abc}$ with $a+b+c=23$ and digits at most $9$. The multisets of digits are $\{9,9,5\}$ ($3$ orders), $\{9,8,6\}$ ($6$), $\{9,7,7\}$ ($3$) and $\{8,8,7\}$ ($3$), so there are $15$ numbers. In increasing order:
\[
1599,1689,1698,1779,1788,1797,1869,\mathbf{1878},1887,1896,1959,1968,1977,1986,1995 .
\]
The median is the $8$th: $\boxed{1878}$.''',
'Median|Digits and bases|Systematic counting',2,source=src('MATHCOUNTS Handbook',2019,None,85,rnd='Warm-Up 6'))
b.add(1735512,89,r'''Gavin goes for a run at a constant pace of $9$ minutes per mile. Ten minutes later, Lars goes for a run along the same route at a constant pace of $7$ minutes per mile. How many minutes does it take Lars to reach Gavin?''',
r'''When Lars starts, Gavin is $\dfrac{10}{9}$ mile ahead. Their speeds are $\dfrac19$ and $\dfrac17$ mile per minute, so Lars closes the gap at $\dfrac17-\dfrac19=\dfrac2{63}$ mile per minute. He reaches Gavin after
\[
\dfrac{10}{9}\div\dfrac{2}{63}=\dfrac{10}{9}\cdot\dfrac{63}{2}=\boxed{35}\text{ minutes}.
\]
(Check: Lars runs $5$ miles in $35$ minutes, and Gavin runs $5$ miles in $45=10+35$ minutes.)''',
'Relative speed|Distance, rate, and time',2,source=src('MATHCOUNTS Handbook',2019,None,89,rnd='Warm-Up 6'))

# ---------------- 1736373 cone volume
fig=r'''real r=5,h=3,k=1.25;
draw(arc((0,0),r,k,180,360),linewidth(0.9));
draw(reverse(arc((0,0),r,k,0,180)),dashed+linewidth(0.6));
path el(real r,real k,real a,real b){guide g; for(int i=0;i<=60;++i){real t=a+(b-a)*i/60; g=g--(r*Cos(t),k*Sin(t));} return g;}
draw(el(r,k,180,360),linewidth(0.9));draw(el(r,k,0,180),dashed+linewidth(0.6));
draw((-r,0)--(0,h)--(r,0),linewidth(0.9));
draw((0,0)--(0,h),dashed);draw((0,0)--(r,0),dashed);
draw((0,0.35)--(0.35,0.35)--(0.35,0));
dot((0,0));
label("$3$",(0,2.15),W);label("$5$",(r/2,0),N);'''
fig=fig.replace(r'''draw(arc((0,0),r,k,180,360),linewidth(0.9));
draw(reverse(arc((0,0),r,k,0,180)),dashed+linewidth(0.6));
''','')
b.add(1736373,1,r'''What is the volume of a cone with height $3$ cm and base radius $5$ cm? Round your answer to the nearest hundredth.''',
r'''The volume of a cone is one third of base area times height:
'''+asy(fig,'5cm')+r'''
\[
V=\dfrac13\pi r^2h=\dfrac13\pi\cdot5^2\cdot3=25\pi\approx\boxed{78.54}\text{ cm}^3 .
\]''',
'Cones|Volume',1,
note='Problem P1 of a geometry thread; the poster\'s answer "about 78.5" is given to the nearest hundredth as requested (78.54).')

# ---------------- 1736642 (a^3+1)/a equal
b.add(1736642,1,r'''Let $a$, $b$, $c$ be three distinct real numbers such that
\[
\dfrac{a^3+1}{a}=\dfrac{b^3+1}{b}=\dfrac{c^3+1}{c}.
\]
Find $a^3+b^3+c^3$.''',
r'''Let $k$ be the common value. Then each of $a,b,c$ satisfies $\dfrac{x^3+1}{x}=k$, i.e.\ $x^3-kx+1=0$. This cubic has at most three roots, and $a,b,c$ are three distinct roots, so they are exactly its roots, and by Vieta's formulas
\[
a+b+c=0,\qquad abc=-1 .
\]
Using $a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)=0$, we get $a^3+b^3+c^3=3abc=\boxed{-3}$.

(Such numbers exist: for example $k=3$ gives $x^3-3x+1=0$, whose left side takes the values $-1,3,1,-1,3$ at $x=-2,-1,0,1,2$, so it has three distinct real roots, one in each of $(-2,-1)$, $(0,1)$ and $(1,2)$.)''',
'Vieta\'s formulas|Polynomial roots|Algebraic expressions and identities|Sum and difference of cubes',4,
note='"Distinct" is added: without it a = b = c gives infinitely many values of a^3+b^3+c^3, so "the sum of all possible values" makes no sense. With it the value is unique (-3).')

# ---------------- 1736382 within 10%
b.add(1736382,1,r'''The actual attendance at a game in Atlanta is $100{,}000$, and Anita made an estimate $E$ of it. Find all values of $E$ for which each statement is true:
\begin{enumerate}
\item[(i)] the actual attendance is within $10\%$ of Anita's estimate;
\item[(ii)] Anita's estimate is within $10\%$ of the actual attendance.
\end{enumerate}''',
r'''``$X$ is within $10\%$ of $Y$'' means $|X-Y|\le0.1\,Y$: the percentage is taken of the second quantity.

\textbf{(ii)} $|E-100000|\le0.1\cdot100000=10000$, so $\boxed{90000\le E\le110000}$.

\textbf{(i)} $|100000-E|\le0.1E$, i.e.\ $0.9E\le100000\le1.1E$, so
\[
\boxed{\dfrac{100000}{1.1}\le E\le\dfrac{100000}{0.9}},\quad\text{i.e.}\quad 90909.\overline{09}\le E\le111111.\overline{1}.
\]
The two conditions differ because the $10\%$ is measured from different bases: for example an estimate of $111000$ satisfies (i) (it is $11000\le11100$ away) but not (ii).''',
'Percentages|Inequalities|Absolute value',2,
note='The post asks for the difference between the two statements and how to set up the equations with attendance 100000; turned into finding the range of estimates in each case.')

# ---------------- 1735893 parabola: equidistant from line and origin
fig=r'''real p=3/sqrt(13); pair nn=(3,-2)/sqrt(13), t=(2,3)/sqrt(13), V=(9/13,-6/13);
guide g; for(int i=0;i<=80;++i){real v=-4.6+9.2*i/80; g=g..(V-(v^2/(4p))*nn+v*t);}
draw((-6.5,0)--(4.5,0),gray(0.5),Arrow(TeXHead));draw((0,-4.5)--(0,6),gray(0.5),Arrow(TeXHead));
label("$x$",(4.5,0),S,gray(0.3));label("$y$",(0,6),W,gray(0.3));
draw((-0.6,-3.9)--(3.6,2.4),red+linewidth(0.9));
label("$3x-2y-6=0$",(3.6,2.4),E,red);
draw(g,blue+linewidth(0.9));
real v0=-3; pair P=V-(v0^2/(4p))*nn+v0*t; pair Fp=P-((3*P.x-2*P.y-6)/13)*(3,-2);
draw(P--(0,0),dashed);draw(P--Fp,dashed);
pair u=unit(P-Fp),w=unit((2,3));
draw(Fp+0.25*u--Fp+0.25*u+0.25*w--Fp+0.25*w);
dot((0,0));dot(P);
label("$O$",(0,0),dir(135));label("$P$",P,dir(235));'''
b.add(1735893,1,r'''Find an equation for the set of points that are equidistant from the line $3x-2y-6=0$ and the origin.''',
r'''A point $P=(x,y)$ is at distance $\sqrt{x^2+y^2}$ from the origin $O$ and at distance $\dfrac{|3x-2y-6|}{\sqrt{3^2+2^2}}=\dfrac{|3x-2y-6|}{\sqrt{13}}$ from the line. Setting these equal and squaring (both sides are nonnegative),
\[
13(x^2+y^2)=(3x-2y-6)^2=9x^2+4y^2+36-12xy-36x+24y ,
\]
which simplifies to
\[
\boxed{4x^2+12xy+9y^2+36x-24y-36=0}.
\]
This is the parabola with focus $O$ and directrix $3x-2y-6=0$ (note $4x^2+12xy+9y^2=(2x+3y)^2$, a perfect square, as for every parabola):
'''+asy(fig,'6cm'),
'Parabolas|Distance formula|Loci and geometric constraints|Coordinate geometry',4)

# ---------------- 1736317 men and work
b.add(1736317,1,r'''Ninety men can complete a piece of work in $20$ days. After the $90$ men have worked for $5$ days, it is decided that the rest of the work must be finished in $10$ more days. How many more men must be employed?''',
r'''The whole job is $90\cdot20=1800$ man-days. After $5$ days, $90\cdot5=450$ man-days are done and $1350$ remain. To do them in $10$ days requires $\dfrac{1350}{10}=135$ men, that is $135-90=\boxed{45}$ more men.''',
'Work and rates|Ratios, proportions, and variation',2,
note='The garbled sentence is read as: 90 men can finish the work in 20 days; after 5 days the remainder must be finished in 10 days.')

# ---------------- 1735148 two right triangles (Warm-Up 14 #162)
fig=r'''pair O1=(0,0),X1=(10,0),Y1=(0,15);pair O2=(16,0),X2=(36,0),Y2=(16,5);
draw(O1--X1--Y1--cycle,linewidth(0.9));draw(O2--X2--Y2--cycle,linewidth(0.9));
draw((0,0.9)--(0.9,0.9)--(0.9,0));draw((16,0.9)--(16.9,0.9)--(16.9,0));
label("$a=10$",(5,0),S);label("$b=15$",(0,7.5),W);
label("$d=20$",(26,0),S);label("$c=5$",(16,2.5),W);'''
b.add(1735148,1,r'''The larger of two right triangles has area numerically equal to $3$ times the sum of its integer leg lengths $a$ and $b$. The other right triangle has area numerically equal to $2$ times the sum of its integer leg lengths $c$ and $d$. If the areas of the triangles are in the ratio $3:2$, what is the value of $a+b+c+d$?''',
r'''The conditions are $\dfrac{ab}{2}=3(a+b)$ and $\dfrac{cd}2=2(c+d)$. The areas are $3(a+b)$ and $2(c+d)$, and their ratio is $3:2$ exactly when $a+b=c+d$.

From $ab=6a+6b$ we get $(a-6)(b-6)=36$, and from $cd=4c+4d$ we get $(c-4)(d-4)=16$ (the factors must be positive, since a negative factor would make a leg nonpositive). Listing with $a\le b$ and $c\le d$:
\[
(a,b)\in\{(7,42),(8,24),(9,18),(10,15),(12,12)\},\quad a+b\in\{49,32,27,25,24\},
\]
\[
(c,d)\in\{(5,20),(6,12),(8,8)\},\quad c+d\in\{25,18,16\}.
\]
The only common sum is $25$, from legs $10,15$ and $5,20$:
'''+asy(fig,'6.5cm')+r'''
Indeed the areas are $75=3\cdot25$ and $50=2\cdot25$, in ratio $3:2$. Hence $a+b+c+d=25+25=\boxed{50}$.''',
'Right triangles|Diophantine equations|Factoring|Lengths, perimeter, and area',4,source=src('MATHCOUNTS Handbook',None,None,162,rnd='Warm-Up 14'))

# ---------------- 1736204 98!+99!+100!
b.add(1736204,1,r'''A solution factors $98!+99!+100!$ as $98!\cdot10000$. A student thinks it should be $98!\cdot9999$. Which is correct? Show the factorisation.''',
r'''Since $99!=99\cdot98!$ and $100!=100\cdot99\cdot98!=9900\cdot98!$,
\[
98!+99!+100!=98!\,(1+99+9900)=98!\cdot10000 .
\]
So $\boxed{98!\cdot10000}$ is correct. The student probably forgot the term $1$ that remains when $98!$ is factored out of $98!$ itself ($99+9900=9999$).''',
'Factorials|Factoring',1,
note='The post questions a step in an AMC solution; the record asks for the factorisation and the error.')

# ---------------- 1501286 3x^3-12x+2=0
b.add(1501286,1,r'''Solve $3x^3-12x+2=0$ exactly.''',
r'''Try $x=\dfrac{4}{\sqrt3}\cos\theta$, chosen so that the identity $4\cos^3\theta-3\cos\theta=\cos3\theta$ appears:
\[
3x^3-12x+2=3\cdot\dfrac{64}{3\sqrt3}\cos^3\theta-\dfrac{48}{\sqrt3}\cos\theta+2=\dfrac{16}{\sqrt3}\left(4\cos^3\theta-3\cos\theta\right)+2=\dfrac{16}{\sqrt3}\cos3\theta+2 .
\]
So the equation becomes $\cos3\theta=-\dfrac{2\sqrt3}{16}=-\dfrac{\sqrt3}{8}$. Let $\varphi=\arccos\left(-\dfrac{\sqrt3}8\right)$. Then $3\theta=\varphi+2\pi k$, and the three roots are
\[
\boxed{x_k=\dfrac{4\sqrt3}{3}\cos\left(\dfrac{\varphi+2\pi k}{3}\right),\quad k=0,1,2,\qquad \varphi=\arccos\left(-\dfrac{\sqrt3}{8}\right)},
\]
approximately $x\approx1.917$, $0.168$ and $-2.085$. These are three distinct real numbers, so they are all the roots. (There is no rational root: by the rational root test the candidates $\pm1,\pm2,\pm\dfrac13,\pm\dfrac23$ all fail. Cardano's formula would express the roots through cube roots of complex numbers, since the discriminant is positive; the trigonometric form avoids this.)''',
'Polynomial roots|Polynomials|Substitution',5,
note='The post asks for an exact solution with an insightful approach; the trigonometric substitution is used. The roots were checked numerically.')

# ---------------- 1729507 three problems
R7=r'''real R=7; real al=2*aSin(1/7), be=60, ga=2*aSin(11/14);
real[] arcs={al,al,be,be,ga,ga};
pair[] P; real t=100; for(int i=0;i<6;++i){P.push(R*dir(t)); t-=arcs[i];}
draw(circle((0,0),R),gray(0.6));
draw(P[0]--P[1]--P[2]--P[3]--P[4]--P[5]--cycle,linewidth(0.9));
string[] lab={"$2$","$2$","$7$","$7$","$11$","$11$"};
for(int i=0;i<6;++i){pair m=(P[i]+P[(i+1)%6])/2; label(lab[i],(R+0.75)*unit(m));}
dot((0,0));label("$O$",(0,0),S);'''
R8=r'''real R=7; real x=aSin(1/7), y=30, z=aSin(11/14);
pair P0=R*dir(180),P1=R*dir(180-2*x),P2=R*dir(180-2*x-2*y),P3=R*dir(0);
draw(arc((0,0),R,0,180),gray(0.6));
draw(P0--P1--P2--P3--cycle,linewidth(0.9));
draw(P0--P2,dashed);draw(P1--P3,dashed);
label("$2$",(P0+P1)/2,W);label("$7$",(R+0.75)*unit((P1+P2)/2));label("$11$",(R+0.75)*unit((P2+P3)/2));
label("$d=2R$",(0,0),S);
label("$P_0$",P0,SW);label("$P_1$",P1,NW);label("$P_2$",P2,N);label("$P_3$",P3,E);'''
b.add(1729507,1,r'''A cyclic hexagon has side lengths $2$, $2$, $7$, $7$, $11$ and $11$, in that order. Find its circumradius.''',
r'''Let the circumradius be $R$ and the centre $O$.
'''+asy(R7,'5cm')+r'''
A chord of length $\ell$ cuts off an arc whose central angle depends only on $\ell$ and $R$. So reordering the sides around the circle keeps the same circle: the hexagon with sides $2,7,11,2,7,11$ in this order also has circumradius $R$. In that hexagon the arcs of the sides $2,7,11$ make up half of the circle, so the vertices $P_0$ and $P_3$ at the ends of the path $2,7,11$ are diametrically opposite. Thus $P_0P_1P_2P_3$ is a cyclic quadrilateral with sides $a=2$, $b=7$, $c=11$ and the diameter $d=P_0P_3=2R$:
'''+asy(R8,'5cm')+r'''
The angles at $P_1$ and $P_2$ are inscribed in a semicircle, so they are right angles, and the diagonals are $P_0P_2=\sqrt{d^2-c^2}$ and $P_1P_3=\sqrt{d^2-a^2}$. Ptolemy's theorem gives $P_0P_2\cdot P_1P_3=ac+bd$, so
\[
(d^2-a^2)(d^2-c^2)=(ac+bd)^2\ \Longrightarrow\ d^4-(a^2+c^2)d^2=2abcd+b^2d^2\ \Longrightarrow\ d^3-(a^2+b^2+c^2)d-2abc=0 .
\]
With $a=2,b=7,c=11$: $d^3-174d-308=0$, which factors as $(d-14)(d^2+14d+22)=0$. The quadratic factor has only negative roots, so $d=14$ and the circumradius is $R=\boxed{7}$.

(Check: the half-angles $\arcsin\dfrac17$, $\arcsin\dfrac12=30^\circ$ and $\arcsin\dfrac{11}{14}$ add up to $90^\circ$, since $\cos\left(\arcsin\dfrac17+30^\circ\right)=\dfrac{4\sqrt3}{7}\cdot\dfrac{\sqrt3}2-\dfrac17\cdot\dfrac12=\dfrac{11}{14}$.)''',
'Circles|Arcs and chords|Cyclic quadrilaterals|Ptolemy\'s theorem|Inscribed angles|Polynomial roots',6,
note='First of three problems in the post (q01-q03 in order). Figures drawn to scale with R = 7.')
fig=r'''real h=120/17,p=64/17; pair A=(0,0),B=(20,0),D=(p,h),C=(p+3,h),Ep=(3,0);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(C--Ep,dashed+blue);
pair u=unit(Ep-C),w=unit(B-C);draw(C+0.7*u--C+0.7*u+0.7*w--C+0.7*w,blue);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,N);label("$D$",D,N);label("$E$",Ep,S);
label("$8$",(A+D)/2,W);label("$15$",(B+C)/2,NE);label("$3$",(C+D)/2,N);
label("$3$",(A+Ep)/2,S);label("$17$",(Ep+B)/2,S);'''
b.add(1729507,2,r'''A trapezoid has the property that the sum of each pair of opposite sides is $23$. The lengths of the legs differ by $7$, and the lengths of the bases differ by $17$. The area of the trapezoid can be written as a reduced fraction $\dfrac xy$ with $x>y$. Find $x-y$.''',
r'''The bases add up to $23$ and differ by $17$, so they are $20$ and $3$; the legs add up to $23$ and differ by $7$, so they are $15$ and $8$. Let $ABCD$ have bases $AB=20$, $DC=3$ and legs $AD=8$, $BC=15$. Through $C$ draw $CE\parallel DA$ with $E$ on $AB$. Then $AECD$ is a parallelogram, $AE=3$, $CE=8$ and $EB=17$:
'''+asy(fig,'6.5cm')+r'''
Triangle $ECB$ has sides $8,15,17$, and $8^2+15^2=17^2$, so it has a right angle at $C$. Its height to $EB$, which is the height of the trapezoid, is
\[
h=\dfrac{8\cdot15}{17}=\dfrac{120}{17}.
\]
The area is $\dfrac{20+3}{2}\cdot\dfrac{120}{17}=\dfrac{1380}{17}$, a reduced fraction, so $x-y=1380-17=\boxed{1363}$.''',
'Trapezoids|Right triangles|Pythagorean theorem|Parallelograms|Lengths, perimeter, and area',4)
fig=r'''real r0=22*sqrt(3),h=24,r=11; pair O=(0,0),M=(r0,0),D=(0,h),I=(0,r);
pair T=D+dot(I-D,unit(M-D))*unit(M-D);
draw(O--M--D--cycle,linewidth(0.9));
draw(arc(I,r,-90,90),blue);
draw(I--T,blue+dashed);
draw(O+(1.4,0)--O+(1.4,1.4)--O+(0,1.4));
dot(I);
label("$D$",D,N);label("$O$",O,SW);label("$M$",M,SE);label("$I$",I,W);label("$T$",T,NE);
label("$11$",(I+T)/2,dir(-45),blue);
draw((-5,0)--(-5,h),Arrows(TeXHead));label("$24$",(-5,h/2),W);
label("$r_0$",(r0/2,0),S);'''
b.add(1729507,3,r'''In tetrahedron $ABCD$, $AB=BC=CA$ and $DA=DB=DC$. The altitude of $ABCD$ from $D$ is $24$, and the radius of the inscribed sphere of $ABCD$ is $11$. Find $AB$.''',
r'''By symmetry the foot of the altitude from $D$ is the centre $O$ of the equilateral triangle $ABC$, and the centre $I$ of the inscribed sphere lies on $DO$ with $IO=11$. Let $M$ be the midpoint of $BC$ and $r_0=OM$ the inradius of triangle $ABC$. The plane $DOM$ is perpendicular to the face $DBC$ (it contains $DM$ and is perpendicular to $BC$), so in this plane the inscribed sphere appears as a circle of radius $11$ tangent to $OM$ at $O$ and to $DM$ at a point $T$ (drawn to scale):
'''+asy(fig,'6cm')+r'''
Let $\varphi=\angle DMO$. Since $I$ is equidistant from the lines $MO$ and $MD$, $MI$ bisects $\varphi$, so
\[
\tan\dfrac\varphi2=\dfrac{11}{r_0},\qquad \tan\varphi=\dfrac{24}{r_0}.
\]
By the double-angle formula, $\dfrac{22}{r_0}\div\left(1-\dfrac{121}{r_0^2}\right)=\dfrac{24}{r_0}$, so $22=24\left(1-\dfrac{121}{r_0^2}\right)$, which gives $\dfrac{121}{r_0^2}=\dfrac1{12}$ and $r_0^2=1452$, $r_0=22\sqrt3$. The inradius of an equilateral triangle with side $s$ is $\dfrac{s}{2\sqrt3}$, so
\[
AB=2\sqrt3\,r_0=2\sqrt3\cdot22\sqrt3=\boxed{132}.
\]
(Check with $r=\dfrac{3V}{\text{surface area}}$: the slant height is $DM=\sqrt{24^2+1452}=\sqrt{2028}=26\sqrt3$, the surface area is $\dfrac{\sqrt3}4\cdot132^2+3\cdot\dfrac12\cdot132\cdot26\sqrt3=4356\sqrt3+5148\sqrt3=9504\sqrt3$, and $V=\dfrac13\cdot4356\sqrt3\cdot24=34848\sqrt3$, so $r=\dfrac{3\cdot34848}{9504}=11$.)''',
'Pyramids|Spheres|Equilateral triangles|Angle bisectors|Trigonometric identities|Volume|Surface area',5,
note='The solution sketch is the cross-section through D, the base centre O and the midpoint M of BC, drawn to scale.')

# ---------------- 1736016 2016 AMC 8 #17 ATM password
b.add(1736016,1,r'''An ATM password at Fred's Bank is composed of four digits from $0$ to $9$, with repeated digits allowable. If no password may begin with the sequence $9,1,1$, then how many passwords are possible?
\[
\textbf{(A)}\ 30\qquad\textbf{(B)}\ 7290\qquad\textbf{(C)}\ 9000\qquad\textbf{(D)}\ 9990\qquad\textbf{(E)}\ 9999
\]
A student answers $9^3\cdot10=7290$, reasoning that the first three digits each have $9$ choices. Explain the error.''',
r'''Without the restriction there are $10^4=10000$ passwords. The forbidden ones are $911d$ for the $10$ choices of the last digit $d$. So there are $10000-10=\boxed{9990}$ passwords, answer $\textbf{(D)}$.

The student's count forbids $9$ as the first digit, $1$ as the second digit and $1$ as the third digit \emph{separately}, which excludes far too much: for example $9234$ or $1155$ do not begin with $9,1,1$ and are allowed. Only the single combination $9,1,1$ in the first three places is forbidden.''',
'Complementary counting|Multiplication principle|Counting principles',2,source=src('AMC 8',2016,None,17))

# ---------------- 1735385 x^4+y^4
b.add(1735385,1,r'''If $x^2-y^2=7$, $x=\dfrac{12}{y}$ and $y<0$, what is the value of $x^4+y^4$?''',
r'''From $x=\dfrac{12}{y}$ we get $xy=12$. Then
\[
x^4+y^4=(x^2-y^2)^2+2x^2y^2=7^2+2\cdot12^2=49+288=\boxed{337}.
\]
(The values are $x=-4$, $y=-3$: indeed $16-9=7$ and $(-4)(-3)=12$, and $256+81=337$. The condition $y<0$ only selects this solution among $(\pm4,\pm3)$ and does not affect the answer.)''',
'Algebraic expressions and identities|Equations and systems of equations',2,source=src('MATHCOUNTS Handbook',2019,None,6,rnd='Warm-Up 6'))

b.save()
