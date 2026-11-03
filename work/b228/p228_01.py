from qb import *
b=Bank('p228_01')

# ---------------- 1752850 c a t s g o
b.add(1752850,1,r'''The positive integers $c,a,t,s,g,o$ satisfy
\[
cat=5,\qquad sat=75,\qquad csgo=45,
\]
where juxtaposition means multiplication (so $cat=c\cdot a\cdot t$). Find the maximum possible value of $cats+go$.''',
r'''Since $c\cdot a\cdot t=5$ is prime, exactly one of $c,a,t$ equals $5$ and the other two equal $1$.

If $c=5$, then $a=t=1$, so $s=75$ and $csgo=5\cdot75\cdot go=375\,go\ge375>45$, impossible.

Hence $c=1$ and $at=5$. Then $s\cdot at=75$ gives $s=15$, and $csgo=15\,go=45$ gives $go=3$. In every solution
\[
cats+go=(cat)\cdot s+go=5\cdot15+3=78 .
\]
(For example $c=1$, $a=5$, $t=1$, $s=15$, $g=3$, $o=1$.) The value is forced, so the maximum is $\boxed{78}$.''',
'Factors and multiples|Prime factorisation|Logical deduction',2,
note='The post writes the products with *; the record writes them as juxtaposition. The value 78 is the same for every solution, so "maximum" is kept. Checked by brute force.')

# ---------------- 1752843 soap piecewise
b.add(1752843,1,r'''A store is having a sale on soap: for every three bars of soap purchased, one more bar is given free. Each bar costs $\$2$, and there is a limit of eight bars per customer (free bars included). A customer takes home $b$ bars and pays as little as possible.
\begin{enumerate}
\item Write a piecewise-defined function $C(b)$ for the total cost in dollars.
\item State the domain of $C$ in the context of the problem.
\end{enumerate}''',
r'''In a group of four bars, three are paid for and the fourth is free. So among $b$ bars the number of free bars is the number of complete groups of four, and the customer pays for the rest.
\begin{itemize}
\item $0\le b\le3$: no free bar, so $C=2b$.
\item $b=4$: three bars are paid for, so $C=6$.
\item $5\le b\le7$: one bar is free, so $C=2(b-1)$.
\item $b=8$: two bars are free, so $C=2\cdot6=12$.
\end{itemize}
Hence
\[
C(b)=\begin{cases}2b, & b=0,1,2,3,\\ 2(b-1), & b=4,5,6,7,\\ 12, & b=8.\end{cases}
\]
(The middle line gives $C(4)=6$, as required.) Equivalently $C(b)=2\left(b-\left\lfloor\dfrac b4\right\rfloor\right)$.

The domain is the set of whole numbers of bars allowed: $\boxed{\{0,1,2,3,4,5,6,7,8\}}$ (or $\{1,\dots,8\}$ if a customer must buy something). It is not an interval, since a fraction of a bar cannot be bought.''',
'Piecewise functions|Functions|Money and currency|Floor and ceiling functions',2,
note='The post asks how the problem is done; the record states that the customer pays the least possible (free bars are counted among the b bars).')

# ---------------- 1751545 x+2y+3x/y=2012
b.add(1751545,1,r'''Find all pairs of positive integers $(x,y)$ such that
\[
x+2y+\dfrac{3x}{y}=2012 .
\]''',
r'''Multiply by $y$: $xy+2y^2+3x=2012y$, so $x(y+3)=y(2012-2y)$ and
\[
x=\dfrac{y(2012-2y)}{y+3}.
\]
For $x>0$ we need $y<1006$. Put $u=y+3$, so $4\le u\le1008$. Then $y(2012-2y)=(u-3)(2018-2u)\equiv(-3)\cdot2018=-6054\pmod u$, so $u$ must divide
\[
6054=2\cdot3\cdot1009 ,
\]
with $1009$ prime. The divisors of $6054$ are $1,2,3,6,1009,2018,3027,6054$, and the only one in $[4,1008]$ is $u=6$. Thus $y=3$ and
\[
x=\dfrac{3\cdot2006}{6}=1003 .
\]
Check: $1003+6+\dfrac{3\cdot1003}{3}=1003+6+1003=2012$. The only solution is $\boxed{(x,y)=(1003,3)}$.''',
'Diophantine equations|Divisibility|Prime factorisation',4,
note='"Natural numbers" read as positive integers (y = 0 is impossible; if x = 0 were allowed, (0, 1006) would also work). Checked by brute force.')

# ---------------- 1752607 mean, digits {2,0,1,9} (alias)
b.add(1752607,1,r'''What is the mean of all three-digit positive integers whose digits are all in the set $\{2,0,1,9\}$? (Digits may repeat.)''',
r'''The hundreds digit is $1$, $2$ or $9$, and the tens and units digits are any of $0,1,2,9$, independently, so each position is uniform over its allowed digits. The mean is
\[
100\cdot\dfrac{1+2+9}{3}+10\cdot\dfrac{12}{4}+\dfrac{12}{4}=400+30+3=\boxed{433}.
\]''',
'Mean|Place value|Digit problems',3,source=src('MATHCOUNTS',None,'Handbook',108,rnd='Warm-Up 8'),
note='MATHCOUNTS Handbook Warm-Up 8 #108. Repeat of an earlier record (aliased).')

# ---------------- 1738877 Casio-able
b.add(1738877,1,r'''Call a function $f$ \emph{calculator-made} if $f(x)$ can be written as an expression in $x$ and real constants using only addition, subtraction, multiplication, division, powers and roots, logarithms, factorials, and the trigonometric functions and their inverses.

Let $n\ge1$ and let $a_1,a_2,\dots,a_n$ be distinct real numbers; put $a_{n+1}=a_1$. Prove that there is a calculator-made function $f$ with $f(a_i)=a_{i+1}$ for every $i=1,2,\dots,n$.''',
r'''We only need addition, subtraction, multiplication and division with constants. For $n=1$ take $f(x)=a_1$ (a constant is allowed). For $n\ge2$ use Lagrange interpolation: for each $i$ let
\[
L_i(x)=\prod_{j\ne i}\dfrac{x-a_j}{a_i-a_j}.
\]
The denominators are nonzero because the $a_j$ are distinct. If $x=a_k$ with $k\ne i$, the factor with $j=k$ is $0$, so $L_i(a_k)=0$; and $L_i(a_i)=\prod_{j\ne i}1=1$. Now define
\[
f(x)=\sum_{i=1}^{n}a_{i+1}L_i(x).
\]
For each $k$, all terms vanish at $x=a_k$ except the $k$-th, so $f(a_k)=a_{k+1}\cdot1=a_{k+1}$. This $f$ is a polynomial written with $+,-,\times,\div$ and the constants $a_i$, so it is calculator-made. Hence $\boxed{\text{such an }f\text{ always exists}}$.

For example, for $n=2$ the function $f(x)=a_1+a_2-x$ swaps $a_1$ and $a_2$. $\blacksquare$''',
'Polynomials|Functions|Construction',3,
note='The post asks whether such a "Casio-able" function exists; it is posed as a proof. Lagrange interpolation needs only the four basic operations.')

# ---------------- 1745114 divisibility by 4
b.add(1745114,1,r'''Explain why
\[
45376=453\cdot100+76\equiv453\cdot0+4\cdot19\equiv0\pmod4,
\]
and use the same idea to prove that a positive integer is divisible by $4$ if and only if the number formed by its last two digits is divisible by $4$.''',
r'''Any positive integer $N$ can be written as $N=100q+r$, where $q$ is the number formed by all digits except the last two and $r$ is the number formed by the last two digits ($0\le r\le99$). For $45376$, $q=453$ and $r=76$.

Since $100=4\cdot25$, we have $100\equiv0\pmod4$, so $100q\equiv0\cdot q=0\pmod4$. Hence
\[
N=100q+r\equiv r\pmod4 .
\]
So $N$ and $r$ leave the same remainder on division by $4$; in particular $4\mid N$ if and only if $4\mid r$. For $45376$: $76=4\cdot19\equiv0\pmod4$, so $45376\equiv0\pmod4$, which is exactly the displayed chain ($453\cdot100\equiv453\cdot0$ and $76=4\cdot19$). Indeed $45376=4\cdot11344$. $\blacksquare$''',
'Divisibility rules|Remainders and congruences|Place value',2,
note='The poster does not understand the chain of congruences; the record asks for the explanation and the general rule.')

# ---------------- 1752482 five flips no HH
b.add(1752482,1,r'''A fair coin is flipped five times. What is the probability that it never lands heads up twice in a row? Express your answer as a common fraction.''',
r'''Let $a_n$ be the number of sequences of $n$ flips with no two consecutive heads. Such a sequence either ends in T (preceded by any good sequence of length $n-1$) or ends in TH (preceded by any good sequence of length $n-2$), so $a_n=a_{n-1}+a_{n-2}$, with $a_1=2$ (H, T) and $a_2=3$ (HT, TH, TT). Then
\[
a_3=5,\quad a_4=8,\quad a_5=13 .
\]
Out of $2^5=32$ equally likely sequences, $13$ are good, so the probability is $\boxed{\dfrac{13}{32}}$.''',
'Probability|Recursive counting|Fibonacci sequence',3,source=src('MATHCOUNTS',None,'Handbook',104,rnd='Warm-Up 8'),
note='MATHCOUNTS Handbook Warm-Up 8 #104 ("fie flips" read as five flips). Checked by enumeration.')

# ---------------- 1751255 two problems
b.add(1751255,1,r'''Three fair six-sided dice are rolled. Let $G$ be the greatest and $L$ the least of the three numbers rolled. Find the expected value of $L+G$.''',
r'''Replace each roll $x$ by $7-x$. This is a bijection of the outcomes that keeps every outcome equally likely, and it turns the least roll $L$ into $7-G'$, where $G'$ is the greatest of the new rolls. Hence $L$ has the same distribution as $7-G$, so $E[L]=7-E[G]$ and
\[
E[L+G]=E[L]+E[G]=\boxed{7}.
\]
(Directly: $P(G\le k)=\left(\dfrac k6\right)^3$ gives $E[G]=\dfrac{1}{216}\sum_{k=1}^{6}k\left(k^3-(k-1)^3\right)=\dfrac{1071}{216}$, and $E[L]=7-\dfrac{1071}{216}=\dfrac{441}{216}$; the sum is $\dfrac{1512}{216}=7$.)''',
'Expected value|Dice probability|Symmetry',3,
note='Checked by enumerating all 216 outcomes.')
fig=r'''pair A=(1.6,5),B=(0,0),C=(7,0);
pair Ep=A+(B-A)/3,F=(A+C)/2;
fill(A--Ep--F--cycle,palegray);
draw(A--B--C--cycle,linewidth(0.9));
draw(Ep--F,linewidth(0.8));
dot(Ep);dot(F);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);
label("$E$",Ep,W);label("$F$",F,NE);
label("$1$",(A+Ep)/2,W);label("$2$",(Ep+B)/2,W);
label("$1$",(A+F)/2,NE);label("$1$",(F+C)/2,NE);'''
b.add(1751255,2,r'''The area of triangle $ABC$ is $72$. Points $E$ and $F$ lie on sides $AB$ and $AC$, respectively, such that $AE:EB=1:2$ and $AF:FC=1:1$. Find the area of triangle $AEF$.''',
r'''Triangles $AEF$ and $ABC$ share the angle at $A$, so their areas are in the ratio of the products of the sides enclosing that angle:
\[
\dfrac{[AEF]}{[ABC]}=\dfrac{\dfrac12\,AE\cdot AF\sin A}{\dfrac12\,AB\cdot AC\sin A}=\dfrac{AE}{AB}\cdot\dfrac{AF}{AC}=\dfrac13\cdot\dfrac12=\dfrac16 .
\]
(Without trigonometry: $[AEC]=\dfrac13[ABC]$ because the two triangles have the same height from $C$ and bases $AE=\dfrac13AB$; and $[AEF]=\dfrac12[AEC]$ because $F$ is the midpoint of $AC$.)
'''+asy(fig,'6cm')+r'''
Hence $[AEF]=\dfrac{72}{6}=\boxed{12}$.''',
'Area ratios|Triangles|Lengths, perimeter, and area',2)

# ---------------- 1752245 Mandelbrot (alias)
b.add(1752245,1,r'''Simplify
\[
\dfrac{(\sqrt{2}-1)^{1-\sqrt{3}}}{(\sqrt{2}+1)^{1+\sqrt{3}}},
\]
writing your answer as $a-b\sqrt{c}$, where $a$, $b$, $c$ are positive integers.''',
r'''Since $(\sqrt2-1)(\sqrt2+1)=1$, $\sqrt2+1=(\sqrt2-1)^{-1}$, so the expression is
\[
(\sqrt2-1)^{1-\sqrt3}(\sqrt2-1)^{1+\sqrt3}=(\sqrt2-1)^2=\boxed{3-2\sqrt2}.
\]''',
'Exponents|Radicals|Algebraic manipulation',3,source=src('Mandelbrot'),
note='Mandelbrot problem. Repeat of an earlier record (aliased).')

# ---------------- 1752100 Burton
b.add(1752100,1,r'''Prove that if $a$ and $b$ are integers with $b>0$, then there exist unique integers $q$ and $r$ such that
\[
a=qb+r\qquad\text{and}\qquad 2b\le r<3b .
\]''',
r'''\textbf{Existence.} By the division algorithm there are integers $q'$ and $r'$ with $a=q'b+r'$ and $0\le r'<b$. Put $q=q'-2$ and $r=r'+2b$. Then
\[
qb+r=(q'-2)b+r'+2b=q'b+r'=a,
\]
and $2b\le r'+2b<3b$.

\textbf{Uniqueness.} Suppose $a=q_1b+r_1=q_2b+r_2$ with $2b\le r_1,r_2<3b$. Then $r_1-r_2=(q_2-q_1)b$ is a multiple of $b$, and $-b<r_1-r_2<b$. The only multiple of $b$ strictly between $-b$ and $b$ is $0$, so $r_1=r_2$, and then $(q_2-q_1)b=0$ with $b>0$ gives $q_1=q_2$. $\blacksquare$''',
'Remainders and congruences|Divisibility',2,
note='Burton, Elementary Number Theory, exercise; problem 1 of the post.')
b.add(1752100,2,r'''Prove that $3a^2-1$ is never a perfect square, for any integer $a$.''',
r'''Every integer $m$ is congruent to $0$, $1$ or $2$ modulo $3$, so $m^2\equiv0$, $1$ or $4\equiv1\pmod3$: a perfect square leaves remainder $0$ or $1$ on division by $3$. But
\[
3a^2-1\equiv-1\equiv2\pmod3 .
\]
Hence $3a^2-1$ is never a perfect square. $\blacksquare$''',
'Perfect squares|Remainders and congruences|Quadratic residues',2)
b.add(1752100,3,r'''Show that the cube of any integer is of the form $7k$ or $7k\pm1$ for some integer $k$.''',
r'''Every integer $a$ is congruent to one of $0,\pm1,\pm2,\pm3$ modulo $7$, and $(-a)^3=-a^3$, so it suffices to compute
\[
0^3=0,\qquad 1^3=1,\qquad 2^3=8=7+1,\qquad 3^3=27=28-1 .
\]
Thus $a^3\equiv0,\pm1\pmod7$ for $a\equiv0,\pm1,\pm2,\pm3$ respectively (with $(\pm2)^3\equiv\pm1$ and $(\pm3)^3\equiv\mp1$). So $a^3=7k$ or $a^3=7k\pm1$ for some integer $k$. $\blacksquare$''',
'Perfect cubes|Remainders and congruences',2)

# ---------------- 1751902 perpendicular lines
fig=r'''import graph;
real f(real x){return 3x-1;} real g(real x){return -10-(x+3)/3;}
pair P=(-3,-10),Q=(3,8),R=(12,-15);
draw((-8,0)--(15,0),gray,Arrow(5));draw((0,-18)--(0,11),gray,Arrow(5));
label("$x$",(15,0),NE,gray);label("$y$",(0,11),NE,gray);
draw((-5,f(-5))--(3.6,f(3.6)),blue+linewidth(0.9));
draw((-7.5,g(-7.5))--(14,g(14)),red+linewidth(0.9));
pair u=unit((1,3)),v=unit((3,-1));real m=1.1;
draw(P+m*u--P+m*u+m*v--P+m*v,linewidth(0.6));
dot(P);dot(Q);dot(R);
label("$(-3,-10)$",P,2*dir(205));label("$(3,8)$",Q,E);label("$(12,-15)$",R,SW);
label("$f$",(3.6,f(3.6)),N,blue);label("$g$",(14,g(14)),NE,red);'''
b.add(1751902,1,r'''The graph of a linear function $f$ is perpendicular to the graph of a linear function $g$. The graphs intersect at $(-3,-10)$, and $f(3)=8$. Find $g(12)$.''',
r'''The graph of $f$ passes through $(-3,-10)$ and $(3,8)$, so its slope is $\dfrac{8-(-10)}{3-(-3)}=\dfrac{18}{6}=3$. Perpendicular lines (neither vertical) have slopes with product $-1$, so the graph of $g$ has slope $-\dfrac13$ and passes through $(-3,-10)$:
\[
g(x)=-10-\dfrac13(x+3).
\]
'''+asy(fig,'6.5cm')+r'''
Hence $g(12)=-10-\dfrac{15}{3}=\boxed{-15}$.''',
'Slope|Perpendicular lines|Linear equations|Functions|Coordinate geometry',2)

# ---------------- 1751778 2003^4-1997^4
b.add(1751778,1,r'''Without a calculator, find the sum of the digits of the number $2003^4-1997^4$.''',
r'''Let $a=2003$ and $b=1997$, so $a+b=4000$ and $a-b=6$. Then
\[
a^4-b^4=(a^2-b^2)(a^2+b^2)=(a-b)(a+b)(a^2+b^2)=24000\,(a^2+b^2).
\]
With $a=2000+3$ and $b=2000-3$, $a^2+b^2=2\left(2000^2+3^2\right)=2\cdot4000009=8000018$. Therefore
\[
2003^4-1997^4=24000\cdot8000018=192000432000 .
\]
The sum of its digits is $1+9+2+4+3+2=\boxed{21}$.''',
'Difference of squares|Algebraic expressions and identities|Digits and bases',3,source=src('Mandelbrot'),
note='Mandelbrot problem. The post\'s hint ("rewrite the numbers as a power of 2") is not used; the numbers are written as 2000 plus or minus 3. Checked by direct computation.')

# ---------------- 1751211 reflected triangle
fig=r'''pair A=(2,7),B=(-2,0),C=(3,-1),A1=(-1,-8),B1=(6.4,-4.8),A2=(10.4,2.2);
draw(A--B--C--cycle,linewidth(0.9));
draw(A1--B--C--cycle,gray+dashed);
draw(A1--B1--C--cycle,gray+dashed);
draw(A2--B1--C--cycle,gray+dashed);
draw(A--A2,red+linewidth(0.9));
dot(A);dot(B);dot(C);dot(A1);dot(B1);dot(A2);
label("$A(2,7)$",A,N);label("$B(-2,0)$",B,W);label("$C$",C,2*dir(205));
label("$A'$",A1,SW);label("$B'$",B1,SE);label("$A''$",A2,E);'''
b.add(1751211,1,r'''Triangle $ABC$ is isosceles with $A=(2,7)$, $B=(-2,0)$ and $C=(3,-1)$. Triangle $ABC$ is reflected over $BC$ to form triangle $A'BC$. Triangle $A'BC$ is reflected over $A'C$ to form triangle $A'B'C$. Triangle $A'B'C$ is reflected over $B'C$ to form triangle $A''B'C$. What is the slope of line $AA''$?''',
r'''Here $AB=AC=\sqrt{65}$. All three reflections are in lines through $C$, so we work with vectors from $C$: $\vec{CA}=(-1,8)$, $\vec{CB}=(-5,1)$.

To reflect a vector $\mathbf v$ in the line through $C$ with direction $\mathbf d$, use $\mathbf v\mapsto 2\dfrac{\mathbf v\cdot\mathbf d}{\mathbf d\cdot\mathbf d}\,\mathbf d-\mathbf v$.

\textbf{Over $BC$} ($\mathbf d=(-5,1)$): $\mathbf v=(-1,8)$, $\mathbf v\cdot\mathbf d=13$, $\mathbf d\cdot\mathbf d=26$, so $\vec{CA'}=(-5,1)-(-1,8)=(-4,-7)$ and $A'=(-1,-8)$.

\textbf{Over $A'C$} ($\mathbf d=(-4,-7)$): $\mathbf v=\vec{CB}=(-5,1)$, $\mathbf v\cdot\mathbf d=13$, $\mathbf d\cdot\mathbf d=65$, so $\vec{CB'}=\dfrac25(-4,-7)-(-5,1)=\left(\dfrac{17}{5},-\dfrac{19}{5}\right)$ and $B'=\left(\dfrac{32}{5},-\dfrac{24}{5}\right)$.

\textbf{Over $B'C$} ($\mathbf d=(17,-19)$): $\mathbf v=\vec{CA'}=(-4,-7)$, $\mathbf v\cdot\mathbf d=65$, $\mathbf d\cdot\mathbf d=650$, so $\vec{CA''}=\dfrac15(17,-19)-(-4,-7)=\left(\dfrac{37}{5},\dfrac{16}{5}\right)$ and $A''=\left(\dfrac{52}{5},\dfrac{11}{5}\right)$.
'''+asy(fig,'7cm')+r'''
The slope of $AA''$ is
\[
\dfrac{\dfrac{11}{5}-7}{\dfrac{52}{5}-2}=\dfrac{-\dfrac{24}{5}}{\dfrac{42}{5}}=\boxed{-\dfrac47}.
\]
(Check: $CA''=\sqrt{\dfrac{37^2+16^2}{25}}=\sqrt{65}=CA$, as it must be.)''',
'Reflections|Coordinate geometry|Slope|Isosceles triangles',4,
note='Coordinates of every image checked with exact arithmetic.')

# ---------------- 1751518 max(x,y)
b.add(1751518,1,r'''Positive integers $x$ and $y$ satisfy $x+y\ge9$, and $M=\max(x,y)$. Find the largest integer $k$ such that $M\ge k$ for all such $x$ and $y$.''',
r'''Since $M\ge x$ and $M\ge y$, we get $2M\ge x+y\ge9$, so $M\ge\dfrac92$, and as $M$ is an integer, $M\ge5$. The pair $(x,y)=(4,5)$ has $x+y=9$ and $M=5$, so no larger bound holds. The answer is $\boxed{5}$.''',
'Inequalities|Bounding and extremal cases',2,
note='The post asks "find M >= ?"; read as the best (largest) lower bound for M.')

# ---------------- 1751489 altitude AN
fig=r'''real x=1;pair N0=(0,0),C=(x,0),B=(-sqrt(5)*x,0),A=(0,2x);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--N0,linewidth(0.8));
draw((0,0.16)--(0.16,0.16)--(0.16,0),linewidth(0.6));
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$N$",N0,S);
label("$x$",(N0+C)/2,S);label("$2x$",(A+N0)/2,W);
label("$3x$",(A+B)/2,NW);label("$\sqrt{5}\,x$",(B+N0)/2,S);label("$\sqrt{5}\,x$",(A+C)/2,NE);'''
b.add(1751489,1,r'''Segment $AN$ is an altitude of triangle $ABC$ (so $N$ lies on line $BC$ and $AN\perp BC$). If $AB=3\cdot NC$ and $AN=2\cdot NC$, prove that $AC=BN$.''',
r'''Let $NC=x$. Then $AN=2x$ and $AB=3x$. Both triangles $ANC$ and $ANB$ have a right angle at $N$, so by the Pythagorean theorem
\[
AC=\sqrt{AN^2+NC^2}=\sqrt{4x^2+x^2}=\sqrt5\,x,
\qquad
BN=\sqrt{AB^2-AN^2}=\sqrt{9x^2-4x^2}=\sqrt5\,x .
\]
'''+asy(fig,'6cm')+r'''
Hence $AC=BN$. $\blacksquare$ (The argument does not depend on whether $N$ lies between $B$ and $C$.)''',
'Right triangles|Pythagorean theorem|Altitudes',2)

# ---------------- 1750915 mean of decimals
b.add(1750915,1,r'''What is the mean of the six numbers $632.14$, $632.15$, $632.12$, $632.14$, $632.13$, $632.16$? Find it quickly, without adding the numbers in full.''',
r'''Guess $632.14$ and add up the deviations from it, in hundredths:
\[
0+1-2+0-1+2=0 .
\]
The deviations sum to $0$, so their mean is $0$ and the mean of the numbers is the guess itself, $\boxed{632.14}$. (Subtracting a common amount from every number subtracts it from the mean, so only the small deviations need to be averaged.)''',
'Mean|Decimals|Estimation',1,
note='"632..13" read as 632.13. The poster\'s method (average the decimal parts) is correct; the record shows the even quicker deviation method.')

# ---------------- 1750909 circles and ellipse
fig=r'''path c1=circle((-0.6,0),1),c2=circle((0.6,0),1);
path el=scale(2.2,0.5)*unitcircle;
draw(c1,blue+linewidth(0.8));draw(c2,heavygreen+linewidth(0.8));draw(el,red+linewidth(0.8));
pair[] P=intersectionpoints(c1,c2);
pair[] Q=intersectionpoints(c1,el);
pair[] R=intersectionpoints(c2,el);
for(pair z:P) dot(z);for(pair z:Q) dot(z);for(pair z:R) dot(z);
label("$C_1$",(-0.6,0)+dir(135),NW,blue);label("$C_2$",(0.6,0)+dir(45),NE,heavygreen);label("$\mathcal{E}$",(2.2,0),E,red);'''
b.add(1750909,1,r'''Two distinct circles and an ellipse are drawn in the plane. What is the maximum possible number of points at which at least two of the three curves intersect?''',
r'''\textbf{Upper bound.} Two distinct circles meet in at most $2$ points. A circle and an ellipse meet in at most $4$ points: two distinct conics meet in at most $4$ points (after a rotation the circle is $x^2+y^2+Dx+Ey+F=0$; eliminating one variable between the two equations leaves an equation of degree at most $4$). So there are at most
\[
2+4+4=10
\]
intersection points.

\textbf{The bound is attained.} The question asks for the maximum over all possible drawings, so it is enough to exhibit one configuration. Take circles of radius $1$ centred at $(\pm0.6,0)$ and the ellipse $\dfrac{x^2}{2.2^2}+\dfrac{y^2}{0.5^2}=1$. The circles meet at $(0,\pm0.8)$; the long flat ellipse passes through each circle, crossing it twice above the $x$-axis and twice below, and none of these crossings is at $(0,\pm0.8)$ or common to both circles.
'''+asy(fig,'7cm')+r'''
The figure shows the $2+4+4$ distinct points, so the maximum is $\boxed{10}$. The poster's count of $6$ assumes that each pair of curves meets in only $2$ points, which is true for two circles but not for a circle and an ellipse.''',
'Circles|Ellipses|Conic sections|Counting intersections',3,
note='The post reads "two distinct circles and ellipses"; read as two circles and one ellipse ("two of the three curves"). The poster objects that 10 needs a special layout; the record explains that a maximum is over all layouts. The 10 intersection points of the figure were computed numerically and checked to be distinct.')

# ---------------- 1750969 three mock problems
b.add(1750969,1,r'''In a class, $8$ students do an activity: $6$ of them sit in a circle and the other $2$ act out a story in the middle of the circle. In how many ways can this be done, if two seatings are considered the same when one is a rotation of the other?''',
r'''Choose the two actors: $\dbinom82=28$ ways (they play the same role, so their order does not matter). Arrange the remaining $6$ students around the circle up to rotation: $\dfrac{6!}{6}=5!=120$ ways. The total is $28\cdot120=\boxed{3360}$.''',
'Circular arrangements|Combinations|Multiplication principle',2,
note='The two actors are taken as an unordered pair (the post gives them no distinct roles).')
b.add(1750969,2,r'''Amy rolls a standard six-sided die and tosses a fair coin at the same time. If the coin shows heads, she multiplies the number on the die by $2$; otherwise she divides it by $2$. What is the expected value of the resulting number? Express your answer as a decimal rounded to the nearest thousandth.''',
r'''The die and the coin are independent and the die has mean $3.5$. By linearity,
\[
E=\dfrac12\cdot2\cdot3.5+\dfrac12\cdot\dfrac{3.5}{2}=3.5+0.875=\boxed{4.375}.
\]''',
'Expected value|Dice probability|Independent events',2)
fig=r'''real x=1.6,s1=2x/sqrt(3),s2=x*sqrt(2/3);
picture p1,p2;
draw(p1,circle((0,0),x),linewidth(0.8));
draw(p1,box((-s1*sqrt(2)/2,-s1/2),(s1*sqrt(2)/2,s1/2)),blue+linewidth(0.9));
draw(p1,(0,0)--(s1*sqrt(2)/2,s1/2),dashed);dot(p1,(0,0));
label(p1,"$x$",(s1*sqrt(2)/4,s1/4),NW);
label(p1,"$s$",(-s1*sqrt(2)/2,0),E,blue);label(p1,"$s\sqrt{2}$",(0,-s1/2),N,blue);
label(p1,"sphere",(0,-x),S);
draw(p2,arc((0,0),x,0,180)--cycle,linewidth(0.8));
draw(p2,box((-s2*sqrt(2)/2,0),(s2*sqrt(2)/2,s2)),blue+linewidth(0.9));
draw(p2,(0,0)--(s2*sqrt(2)/2,s2),dashed);dot(p2,(0,0));
label(p2,"$x$",(s2*sqrt(2)/4,s2/2),2*NW);
label(p2,"$s$",(-s2*sqrt(2)/2,s2/2),E,blue);label(p2,"$s\sqrt{2}$",(0,0),S,blue);
label(p2,"hemisphere",(0,-0.55),S);
add(p1);add(shift(4.2,0)*p2);'''
b.add(1750969,3,r'''Find the ratio of the volume of the largest cube that can be inscribed in a sphere of radius $x$ to the volume of the largest cube that can be inscribed in a hemisphere of radius $x$. Express your answer in simplest radical form.''',
r'''\textbf{Sphere.} The largest cube has all eight vertices on the sphere, so its space diagonal is a diameter: $s\sqrt3=2x$, $s=\dfrac{2x}{\sqrt3}$, and the volume is $V_1=\dfrac{8x^3}{3\sqrt3}$.

\textbf{Hemisphere.} The largest cube stands on the flat face with its base centred at the centre $O$ of the hemisphere, and its four top vertices on the curved surface. A top vertex is at horizontal distance $\dfrac{s\sqrt2}{2}$ (half the base diagonal) and height $s$ from $O$, so
\[
\left(\dfrac{s\sqrt2}{2}\right)^2+s^2=x^2\ \Longrightarrow\ \dfrac32s^2=x^2\ \Longrightarrow\ s=x\sqrt{\dfrac23},
\]
and $V_2=s^3=\dfrac{2\sqrt2\,x^3}{3\sqrt3}$.

The sketches show the cross-sections through a diagonal plane of each cube (side $s$, face diagonal $s\sqrt2$):
'''+asy(fig,'8cm')+r'''
The ratio is
\[
\dfrac{V_1}{V_2}=\dfrac{8}{2\sqrt2}=\boxed{2\sqrt2}.
\]''',
'Spheres|Cubes and rectangular prisms|Volume|Pythagorean theorem',4,
note='Standard reading: the largest cube in a hemisphere rests on the flat face. Values checked numerically.')

# ---------------- 1684977 C(n,6)=C(n,3)
b.add(1684977,1,r'''The number of ways of selecting $6$ objects from $n$ distinct objects is the same as the number of ways of selecting $3$ objects from $n$ distinct objects. An answer key says $n=9$ is the only solution, but a student claims that $n=0,1,2$ also work. Find all nonnegative integers $n$ with $\dbinom n6=\dbinom n3$, and decide who is right.''',
r'''\textbf{Small $n$.} For $n\le2$ there is no way to choose $3$ (or $6$) objects, so $\dbinom n3=\dbinom n6=0$ and the equation holds. For $n=3,4,5$, $\dbinom n3\ge1$ but $\dbinom n6=0$, so it fails.

\textbf{$n\ge6$.} Both sides are positive and
\[
\dfrac{\dbinom n6}{\dbinom n3}=\dfrac{\dfrac{n!}{6!\,(n-6)!}}{\dfrac{n!}{3!\,(n-3)!}}=\dfrac{(n-3)(n-4)(n-5)}{6\cdot5\cdot4}.
\]
So we need $(n-3)(n-4)(n-5)=120=6\cdot5\cdot4$. The left side is strictly increasing for $n\ge6$, so there is exactly one solution, $n-3=6$, i.e.\ $n=9$. (This is also $\dbinom n3=\dbinom n{n-3}$ with $n-3=6$.)

So the full solution set is $\boxed{n\in\{0,1,2,9\}}$. The student is right as a matter of mathematics: for $n=0,1,2$ both counts are $0$. The answer key is right only if the problem intends that selections are possible (that is, $n\ge6$, or the common number of ways is positive), which is presumably what was meant.''',
'Combinations|Combinatorial identities and binomial coefficients|Polynomials',3,
note='The poster\'s answer n = 0, 1, 2, 9 is correct over the nonnegative integers; the key\'s n = 9 is the unique solution with a positive number of ways. The record asks for all n and explains both. Checked by direct computation for n up to 200.')

# ---------------- 1751050 square vertices
fig=r'''pair A=(5,4),C=(1,-6),B=(8,-3),D=(-2,1),M=(3,-1);
draw((-4,0)--(10,0),gray,Arrow(5));draw((0,-8)--(0,6),gray,Arrow(5));
label("$x$",(10,0),NE,gray);label("$y$",(0,6),NE,gray);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--C,dashed);draw(B--D,dashed);
dot(A);dot(B);dot(C);dot(D);dot(M);
label("$(5,4)$",A,NE);label("$(8,-3)$",B,E);label("$(1,-6)$",C,SE);label("$(-2,1)$",D,W);
label("$M$",M,3*dir(298));'''
b.add(1751050,1,r'''Two opposite vertices of a square are $(5,4)$ and $(1,-6)$. Find the coordinates of the other two vertices.''',
r'''The diagonals of a square bisect each other, are equal, and are perpendicular. The centre is the midpoint of the given diagonal,
\[
M=\left(\dfrac{5+1}{2},\dfrac{4+(-6)}{2}\right)=(3,-1),
\]
and the vector from $M$ to $(5,4)$ is $(2,5)$. The other half-diagonals are this vector turned through $\pm90^\circ$, namely $(5,-2)$ and $(-5,2)$. Hence the other two vertices are
\[
M\pm(5,-2)=\boxed{(8,-3)\ \text{and}\ (-2,1)}.
\]
'''+asy(fig,'6cm')+r'''
Check: the four sides all have length $\sqrt{3^2+7^2}=\sqrt{58}$, e.g.\ from $(5,4)$ to $(8,-3)$ the vector is $(3,-7)$ and from $(8,-3)$ to $(1,-6)$ it is $(-7,-3)$, which is perpendicular to it.''',
'Squares|Coordinate geometry|Rotations|Midpoints',3)

# ---------------- 1750857 inequality
b.add(1750857,1,r'''Let $x$ and $y$ be real numbers with $-1<x<0$ and $0<y<1$. Prove that
\[
x^2+y^2+xy<1 .
\]''',
r'''Put $u=-x$, so $0<u<1$ and $0<y<1$, and the expression is $u^2+y^2-uy$. By symmetry we may assume $u\ge y$. Then
\[
u^2+y^2-uy=u^2-y(u-y)\le u^2<1,
\]
since $y>0$ and $u-y\ge0$. Hence $x^2+y^2+xy<1$. $\blacksquare$''',
'Inequalities|Algebraic manipulation',3,
note='Translated from French ("soient x et y deux reels ... montrer que").')

# ---------------- 1750568 three problems
fig=r'''pair A=(0,0),B=(12,0),C=(12,12),D=(0,12),P=(-4,0),Q=(0,3);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(P--A,linewidth(0.9));draw(P--C,red+linewidth(0.9));
dot(P);dot(Q);
label("$A$",A,S);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);
label("$P$",P,SW);label("$Q$",Q,dir(140));
label("$4$",(P+A)/2,S);label("$12$",(A+B)/2,S);label("$12$",(B+C)/2,E);
label("$3$",(0,1.5),E);label("$9$",(0,7.5),E);'''
b.add(1750568,1,r'''Square $ABCD$ has side length $12$. Point $P$ lies on line $AB$, outside the square, with $PA=4$. Segment $PC$ intersects side $AD$ at $Q$. What is the length of $CQ$?''',
r'''For $PC$ to cross side $AD$, $P$ must lie on line $AB$ beyond $A$. Use coordinates $A=(0,0)$, $B=(12,0)$, $C=(12,12)$, $D=(0,12)$, $P=(-4,0)$.
'''+asy(fig,'6cm')+r'''
Triangles $PAQ$ and $PBC$ are similar (both have a right angle, at $A$ and at $B$, and they share the angle at $P$), so
\[
\dfrac{AQ}{BC}=\dfrac{PA}{PB}=\dfrac{4}{16}\ \Longrightarrow\ AQ=3,\qquad DQ=9 .
\]
Then in right triangle $CDQ$, $CQ=\sqrt{CD^2+DQ^2}=\sqrt{144+81}=\boxed{15}$.''',
'Squares|Similarity|Pythagorean theorem|Right triangles',2,
note='P is taken on line AB beyond A, the only position for which PC meets side AD.')
b.add(1750568,2,r'''Four positive integers are arranged from smallest to largest. The smallest three form an arithmetic sequence, and the largest three form a geometric sequence. When the second largest integer is divided by the second smallest integer, the result is $\dfrac54$. What is the smallest possible sum of the four integers?''',
r'''Write the numbers $a<b<c<d$. From $\dfrac cb=\dfrac54$, $b=4k$ and $c=5k$; then $a=2b-c=3k$ and $d=\dfrac{c^2}{b}=\dfrac{25k}{4}$, which is an integer exactly when $4\mid k$. The sum $\dfrac{73k}{4}$ is least for $k=4$: $12,16,20,25$, with sum $\boxed{73}$.''',
'Arithmetic sequences|Geometric sequences|Divisibility',3,
note='Repeat of an earlier record (aliased).')
b.add(1750568,3,r'''When a jet flies between city A and city B at $510$ mph, it arrives $16$ minutes ahead of schedule. When it flies at $450$ mph, it arrives $34$ minutes behind schedule. What is the distance between city A and city B? Express your answer as a decimal to the nearest tenth.''',
r'''Let the distance be $d$ miles and the scheduled flight time $T$ hours. Then
\[
\dfrac{d}{510}=T-\dfrac{16}{60},\qquad \dfrac{d}{450}=T+\dfrac{34}{60}.
\]
Subtracting, the two flight times differ by $\dfrac{50}{60}=\dfrac56$ hour:
\[
\dfrac d{450}-\dfrac d{510}=\dfrac56\ \Longrightarrow\ d\cdot\dfrac{510-450}{450\cdot510}=\dfrac56\ \Longrightarrow\ \dfrac{d}{3825}=\dfrac56,
\]
so $d=\dfrac{5\cdot3825}{6}=\boxed{3187.5}$ miles. (Check: $\dfrac{3187.5}{510}=6.25$ hours and $\dfrac{3187.5}{450}=7.08\overline{3}$ hours differ by $50$ minutes; the schedule is $6$ hours $31$ minutes.) The poster's $399.3$ is not correct.''',
'Distance, rate, and time|Linear equations|Unit conversion',3,
note='The poster\'s answer 399.3 is wrong; the distance is 3187.5 miles. Checked with exact fractions.')

b.save()
