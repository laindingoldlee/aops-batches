from qb import *
b=Bank('p225_02')

# ---------------- 1764320 4-digit odd digit sum
b.add(1764320,1,r'''How many positive four-digit integers have an odd sum of digits?''',
r'''There are $9000$ four-digit integers, $1000$ to $9999$. Pair each one ending in $0,2,4,6,8$ with the number obtained by increasing its last digit by $1$ (ending in $1,3,5,7,9$); this pairs all $9000$ numbers, and in each pair the digit sums differ by $1$, so exactly one of the pair has an odd digit sum. Hence there are $\dfrac{9000}{2}=\boxed{4500}$ such integers.''',
'Parity|Pairing and grouping|Digit problems',2)

# ---------------- 1764322 median triangle of 17-25-26
fig=r'''pair B=(0,0),C=(26,0),A=(340/52,408/26);
pair D=(B+C)/2,G=(A+B+C)/3,H=2*D-G;
draw(A--B--C--cycle,linewidth(0.9));
draw(A--D,gray);draw(B--(A+C)/2,gray);draw(C--(A+B)/2,gray);
draw(G--H,blue+linewidth(0.8));draw(B--H,blue+dashed);draw(C--H,dashed+gray);
draw(B--G,blue+linewidth(0.8));
dot(G);dot(D);dot(H);
label("$A$",A,N);label("$B$",B,W);label("$C$",C,E);
label("$G$",G,dir(150));label("$D$",D,dir(-60));label("$H$",H,S);
label("$17$",(A+B)/2,NW);label("$25$",(A+C)/2,NE);'''
b.add(1764322,1,r'''In triangle $ABC$, $AB=17$, $AC=25$ and $BC=26$. What is the area of the triangle whose side lengths are equal to the lengths of the three medians of triangle $ABC$?''',
r'''\textbf{Area of $ABC$.} By Heron's formula with $s=\dfrac{17+25+26}{2}=34$,
\[
[ABC]=\sqrt{34\cdot17\cdot9\cdot8}=\sqrt{41616}=204 .
\]

\textbf{The median triangle has $\dfrac34$ of this area.} Let $G$ be the centroid and $D$ the midpoint of $BC$, and extend $GD$ beyond $D$ to $H$ with $DH=GD$.
'''+asy(fig,'7cm')+r'''
Since the diagonals $BC$ and $GH$ of $BGCH$ bisect each other, $BGCH$ is a parallelogram, so $BH=GC$. The centroid divides each median in the ratio $2:1$, so
\[
BG=\dfrac23m_b,\qquad GH=2GD=\dfrac23m_a,\qquad BH=GC=\dfrac23m_c ,
\]
where $m_a,m_b,m_c$ are the medians from $A,B,C$. So triangle $BGH$ is similar to the median triangle with ratio $\dfrac23$. Its area is $[BGH]=2[BGD]=[BGC]=\dfrac13[ABC]$ (the median $BD$ of triangle $BGH$ halves it, and $D$ is the midpoint of $BC$). Hence the median triangle has area
\[
\left(\dfrac32\right)^2\cdot\dfrac13[ABC]=\dfrac34\cdot204=\boxed{153}.
\]''',
"Medians and centroids|Heron's formula|Parallelograms|Similarity|Area ratios",4)

# ---------------- 1765275 isosceles trapezoid AOPS
fig=r'''pair Sx=(0,0),P=(36,0),A=(5,12),O=(31,12),M=(18,12);
draw(Sx--P--O--A--cycle,linewidth(0.9));
draw(Sx--M,blue+dashed);draw(P--M,blue+dashed);
draw(A--(5,0),dotted);
draw(arc(Sx,3.2,0,degrees(M-Sx)),red);draw(arc(Sx,3.8,degrees(M-Sx),degrees(A-Sx)),red);
draw(arc(P,3.2,degrees(M-P),180),red);draw(arc(P,3.8,degrees(O-P),degrees(M-P)),red);
dot(M);
label("$A$",A,NW);label("$O$",O,NE);label("$P$",P,SE);label("$S$",Sx,SW);label("$M$",M,N);
label("$13$",(A+M)/2,N);label("$13$",(M+O)/2,N);label("$12$",(5,6),E);
label("$36$",(18,0),S);label("$13$",(Sx+A)/2,W);'''
b.add(1765275,1,r'''$AOPS$ is an isosceles trapezoid with $AO\parallel PS$, $AO=26$ and $SP=36$. The bisectors of $\angle ASP$ and $\angle OPS$ meet at a point on $AO$. Compute the area of $AOPS$.''',
r'''Let the bisector of $\angle ASP$ meet line $AO$ at $M$. Because $AO\parallel SP$, the alternate angles give $\angle AMS=\angle MSP=\angle ASM$, so triangle $ASM$ is isosceles with $AM=AS$. By the symmetry of the isosceles trapezoid, the bisector from $P$ meets $AO$ at the mirror image of $M$, and the two bisectors meet on $AO$ only if $M$ is on the axis of symmetry, i.e.\ $M$ is the midpoint of $AO$.
'''+asy(fig,'7cm')+r'''
So the legs are $AS=OP=AM=13$. The bases differ by $10$, so each leg projects $5$ onto $SP$, and the height is $\sqrt{13^2-5^2}=12$. The area is
\[
\dfrac{26+36}{2}\cdot12=\boxed{372}.
\]''',
'Trapezoids|Angle bisectors|Isosceles triangles|Parallel lines|Pythagorean theorem|Lengths, perimeter, and area',3)

# ---------------- 1765191 alternating harmonic paradox
b.add(1765191,1,r'''Consider the series $1-\dfrac12+\dfrac13-\dfrac14+\dfrac15-\cdots$.

Argument 1: grouping it as $\left(1-\dfrac12\right)+\left(\dfrac13-\dfrac14\right)+\cdots$, every bracket is positive, so the sum is positive.

Argument 2: every positive integer is uniquely $p\cdot2^k$ with $p$ odd and $k\ge0$. Collecting, for each odd $p$, the terms with denominators $p,2p,4p,\dots$ gives $\dfrac1p\left(1-\dfrac12-\dfrac14-\cdots\right)=0$, so the sum is $0$.

Which argument is wrong, and why?''',
r'''\textbf{Argument 1 is right.} The partial sums $S_n$ converge: the even partial sums $S_{2m}=\sum_{j=1}^m\left(\dfrac1{2j-1}-\dfrac1{2j}\right)$ increase, the odd ones $S_{2m+1}=1-\sum_{j=1}^m\left(\dfrac1{2j}-\dfrac1{2j+1}\right)$ decrease, and they differ by $\dfrac1{2m+1}\to0$. So the series has a sum $S$, and $S\ge S_2=\dfrac12>0$. (In fact $S=\ln2\approx0.693$.)

\textbf{Argument 2 is wrong.} Each group really does sum to $0$, but collecting the terms by odd part $p$ rearranges the series: for $p=1$ it uses the terms $-\dfrac12,-\dfrac14,-\dfrac18,\dots$, which lie infinitely far along the series, before any term with $p=3$. Rearranging and regrouping terms is allowed for a series whose terms are all of one sign, or more generally for an \emph{absolutely} convergent series. Here
\[
\sum\left|\pm\dfrac1n\right|=1+\dfrac12+\dfrac13+\cdots
\]
is the harmonic series, which diverges: the positive terms $1+\dfrac13+\dfrac15+\cdots$ and the negative terms $\dfrac12+\dfrac14+\cdots$ each add up to $+\infty$. For such a (conditionally convergent) series the value depends on the order of the terms, so ``$0+0+0+\cdots$'' says nothing about the original sum. $\boxed{\text{Argument 2 is invalid; the sum is positive (it equals }\ln 2)}$.''',
'Sequences and series|Summation|Counterexamples|Calculus',5,
note='The post asks how both "arguments" can hold; the record asks which one is wrong and why. The value ln 2 is quoted, not needed.')

# ---------------- 1765183 equilateral triangle and circle
fig=r'''real s=4*(pi^(1/3)); real r=sqrt(3)*s^2/(8*pi);
pair P=(0,0),Q=(s,0),R=(s/2,s*sqrt(3)/2);
draw(P--Q--R--cycle,linewidth(0.9));
pair M=(s+1.2+r,r);
draw(circle(M,r),linewidth(0.9));dot(M);draw(M--M+r*dir(30),dashed);
label("$P$",P,SW);label("$Q$",Q,SE);label("$R$",R,N);
label("$s$",(P+Q)/2,S);label("$M$",M,S);label("$r$",M+r/2*dir(30),N);'''
b.add(1765183,1,r'''The numerical value of the area of equilateral triangle $PQR$ equals the numerical value of the circumference of circle $M$, and the numerical value of the area of circle $M$ equals the numerical value of the perimeter of triangle $PQR$. Find the area $[PQR]$.''',
r'''Let the triangle have side $s$ and the circle radius $r$.
'''+asy(fig,'6cm')+r'''
The conditions are
\[
\dfrac{\sqrt3}{4}s^2=2\pi r,\qquad \pi r^2=3s .
\]
From the first, $r=\dfrac{\sqrt3\,s^2}{8\pi}$. Substituting in the second,
\[
\pi\cdot\dfrac{3s^4}{64\pi^2}=3s\ \Longrightarrow\ s^3=64\pi\ \Longrightarrow\ s=4\sqrt[3]{\pi}.
\]
Then
\[
[PQR]=\dfrac{\sqrt3}{4}s^2=\dfrac{\sqrt3}{4}\cdot16\sqrt[3]{\pi^2}=\boxed{4\sqrt3\,\sqrt[3]{\pi^2}}\approx14.86 .
\]
(Check: $r=\dfrac{\sqrt3\cdot16\sqrt[3]{\pi^2}}{8\pi}=\dfrac{2\sqrt3}{\sqrt[3]{\pi}}$, and $\pi r^2=\dfrac{12\pi}{\sqrt[3]{\pi^2}}=12\sqrt[3]{\pi}=3s$.)''',
'Equilateral triangles|Circles|Lengths, perimeter, and area|Equations and systems of equations|Radicals',3)

# ---------------- 1764326 balls, blue finishes first
b.add(1764326,1,r'''Kevin randomly puts $3$ yellow balls, $4$ blue balls and $6$ green balls into $13$ boxes numbered $1$ to $13$, one ball per box. Bob takes out the balls from box $1$, then box $2$, and so on. What is the probability that all the blue balls have been drawn before all the green balls have been drawn and before all the yellow balls have been drawn (that is, blue is the first colour to be used up)?

$\textbf{(A) }\dfrac{4}{13}\qquad\textbf{(B) }\dfrac{153}{455}\qquad\textbf{(C) }\dfrac{48}{143}\qquad\textbf{(D) }\dfrac13\qquad\textbf{(E) }\dfrac{30}{91}$''',
r'''All orders of the $13$ balls are equally likely. Blue is used up first exactly when the last blue ball comes before the last green ball and before the last yellow ball. Look at the order from the end.

\textbf{The very last ball} is green with probability $\dfrac{6}{13}$, yellow with probability $\dfrac{3}{13}$, and blue with probability $\dfrac4{13}$ (then blue is used up last, a failure).

\textbf{If the last ball is green}, green is used up last, and we need blue to be used up before yellow: among the $7$ blue and yellow balls, the last one must be yellow. By symmetry this has probability $\dfrac37$.

\textbf{If the last ball is yellow}, we need the last of the $10$ blue and green balls to be green: probability $\dfrac{6}{10}$.

Hence the probability is
\[
\dfrac{6}{13}\cdot\dfrac37+\dfrac{3}{13}\cdot\dfrac{6}{10}=\dfrac{18}{91}+\dfrac{9}{65}=\dfrac{90+63}{455}=\boxed{\textbf{(B) }\dfrac{153}{455}}.
\]''',
'Probability|Conditional probability|Symmetry|Sampling without replacement',4,
note='The wording "before all of the green or yellow balls are drawn" is read as: blue is the first colour to be used up (the only reading matching an answer choice). Checked by enumerating all 60060 colour orders.')

# ---------------- 1764048 factorization match P1-P13
T=1764048
b.add(T,1,r'''The polynomial $x^2+4x+k$ is divisible by $x-2$. Find the constant $k$.''',
r'''By the factor theorem, $x-2$ divides the polynomial exactly when its value at $x=2$ is $0$: $4+8+k=0$, so $k=\boxed{-12}$. (Indeed $x^2+4x-12=(x-2)(x+6)$.)''',
'Remainder theorem and factor theorem|Polynomials',1)
b.add(T,2,r'''The polynomial $6x^2+Ax-20$ factors as $(2x+4)(Bx-5)$. Find $A+B$.''',
r'''Expanding, $(2x+4)(Bx-5)=2Bx^2+(4B-10)x-20$. Comparing $x^2$ coefficients, $2B=6$, so $B=3$; then $A=4\cdot3-10=2$. So $A+B=\boxed{5}$.''',
'Polynomials|Factoring|Algebraic expressions and identities',1)
b.add(T,3,r'''Factor $(x+1)(x+2)(x-3)(x-4)+6$.''',
r'''Pair the factors so that the products share the terms $x^2-2x$:
\[
(x+1)(x-3)=x^2-2x-3,\qquad (x+2)(x-4)=x^2-2x-8 .
\]
With $t=x^2-2x$ the expression is $(t-3)(t-8)+6=t^2-11t+30=(t-5)(t-6)$. Hence
\[
(x+1)(x+2)(x-3)(x-4)+6=\boxed{(x^2-2x-5)(x^2-2x-6)}.
\]
(Neither quadratic factors over the integers: their discriminants are $24$ and $28$.)''',
'Factoring|Substitution|Polynomials',3)
b.add(T,4,r'''For real numbers $a$ and $b$, define $a*b=ab-a+b$. Factor $(x+y)*(x-y)-1$.''',
r'''By the definition with $a=x+y$, $b=x-y$:
\[
(x+y)*(x-y)-1=(x+y)(x-y)-(x+y)+(x-y)-1=x^2-y^2-2y-1=x^2-(y+1)^2 .
\]
This is a difference of squares, so the expression equals $\boxed{(x+y+1)(x-y-1)}$.''',
'Custom operations|Difference of squares|Factoring',2)
b.add(T,5,r'''Real numbers $a$ and $b$ satisfy $a^2-a-4b^2-2b=3$ and $a-2b=3$. Find $a+2b$.''',
r'''Group the first equation:
\[
a^2-4b^2-(a+2b)=(a+2b)(a-2b)-(a+2b)=(a+2b)(a-2b-1)=3 .
\]
With $a-2b=3$ this is $2(a+2b)=3$, so $a+2b=\boxed{\dfrac32}$. (Then $a=\dfrac94$, $b=-\dfrac38$, which satisfy both equations.)''',
'Factoring|Difference of squares|Equations and systems of equations',2)
b.add(T,6,r'''A rectangle has area $x^2y+5x-2xy-10$ and length $x-2$. Find its perimeter in terms of $x$ and $y$.''',
r'''Factor by grouping: $x^2y-2xy+5x-10=xy(x-2)+5(x-2)=(x-2)(xy+5)$. So the width is $xy+5$, and the perimeter is
\[
2\bigl((x-2)+(xy+5)\bigr)=\boxed{2xy+2x+6}.
\]''',
'Factoring|Algebraic expressions and identities',2)
b.add(T,7,r'''The polynomial $x^3-2x^2-9x+18$ factors as a product of three linear factors, each with leading coefficient $1$. Find the sum of the three factors.''',
r'''Group the terms: $x^2(x-2)-9(x-2)=(x-2)(x^2-9)=(x-2)(x-3)(x+3)$. The sum of the factors is $(x-2)+(x-3)+(x+3)=\boxed{3x-2}$.''',
'Factoring|Difference of squares|Polynomials',2)
b.add(T,8,r'''Compute $\left(1-\dfrac1{2^2}\right)\left(1-\dfrac1{3^2}\right)\left(1-\dfrac1{4^2}\right)\cdots\left(1-\dfrac1{10^2}\right)$.''',
r'''Each factor is $1-\dfrac1{k^2}=\dfrac{k-1}{k}\cdot\dfrac{k+1}{k}$, and the product telescopes: $\dfrac12\cdot\dfrac{11}{10}=\boxed{\dfrac{11}{20}}$.''',
'Telescoping sums|Difference of squares|Fractions',2,
note='The last factor is printed as (1/10^2) in the post; it is read as (1 - 1/10^2). Repeat of an earlier record (aliased).')
b.add(T,9,r'''Factor $a^2-b^2+12b-36$.''',
r'''The last three terms are $-(b^2-12b+36)=-(b-6)^2$, so the expression is a difference of squares:
\[
a^2-(b-6)^2=\boxed{(a-b+6)(a+b-6)}.
\]''',
'Difference of squares|Factoring|Completing the square',2)
b.add(T,10,r'''Factor $n^4+6n^3+11n^2+6n+1$.''',
r'''Try the square of $n^2+3n+c$: $(n^2+3n+c)^2=n^4+6n^3+(9+2c)n^2+6cn+c^2$. Matching $6cn$ and $c^2$ gives $c=1$, and then $9+2c=11$ as needed. So
\[
n^4+6n^3+11n^2+6n+1=\boxed{(n^2+3n+1)^2}.
\]
(Equivalently, it is $n(n+1)(n+2)(n+3)+1$.)''',
'Factoring|Perfect squares|Polynomials',3)
b.add(T,11,r'''Which is a possible value of $x$ if $x^2-12x+36=0$?

(a) $6$\qquad(b) $2$\qquad(c) $-6$\qquad(d) There is not enough information.''',
r'''The left side is a perfect square: $x^2-12x+36=(x-6)^2$. It is $0$ only for $x=6$. The answer is $\boxed{\text{(a) } 6}$.''',
'Quadratic equations|Factoring',1)
b.add(T,12,r'''The real root of the equation $8x^3-3x^2-3x-1=0$ can be written in the form $\dfrac{\sqrt[3]{a}+\sqrt[3]{b}+1}{c}$, where $a$, $b$ and $c$ are positive integers. Find $a+b+c$.''',
r'''Rewrite the equation as $9x^3=x^3+3x^2+3x+1=(x+1)^3$. Taking real cube roots, $\sqrt[3]{9}\,x=x+1$, so
\[
x=\dfrac{1}{\sqrt[3]{9}-1}=\dfrac{\sqrt[3]{81}+\sqrt[3]{9}+1}{9-1}=\dfrac{\sqrt[3]{81}+\sqrt[3]{9}+1}{8},
\]
using $(u-1)(u^2+u+1)=u^3-1$ with $u=\sqrt[3]9$. (The other two cube roots of $9$ are not real, so this is the only real root.) Hence $a+b+c=81+9+8=\boxed{98}$.''',
'Polynomial roots|Sum and difference of cubes|Rationalising denominators|Radicals',5,source=src('AIME',2013,'I',5),
note='2013 AIME I Problem 5.')
b.add(T,13,r'''For some positive integer $n$, the number $110n^3$ has $110$ positive integer divisors, including $1$ and the number $110n^3$. How many positive integer divisors does the number $81n^4$ have?''',
r'''$110n^3$ has $110=2\cdot5\cdot11$ divisors. Since $110n^3=2\cdot5\cdot11\cdot n^3$, its divisor count is a product of factors $(e+1)$ with each $e\equiv1\pmod 3$ for the primes $2,5,11$ (if they appear in $n$) and $e\equiv0\pmod3$ for the others. The only possibility is $110n^3=p^{1}\cdot q^{4}\cdot r^{10}$ with $\{p,q,r\}=\{2,5,11\}$, so $n=q\,r^3$ with $q,r$ among $2,5,11$ (not $3$). Then $81n^4=3^4q^4r^{12}$ has $5\cdot5\cdot13=\boxed{325}$ divisors.''',
'Divisor counting|Prime factorisation',4,source=src('AMC 10',2018,'A',14),
note='Repeat of an earlier record (aliased).')

# ---------------- 1765109 isosceles triangles in grid triangle
qf=r'''pair C=(0,0),A=(0,10),B=(10,0);
for(int i=1;i<10;++i){draw((i,0)--(i,10-i),gray);draw((0,i)--(10-i,i),gray);}
draw(A--B--C--cycle,linewidth(0.9));
label("$A$",A,N);label("$B$",B,E);label("$C$",C,SW);
label("$10$",(0,5),W);label("$10$",(5,0),S);'''
sf=r'''pair C=(0,0),A=(0,10),B=(10,0);
for(int i=1;i<10;++i){draw((i,0)--(i,10-i),gray);draw((0,i)--(10-i,i),gray);}
fill((3,2)--(8,2)--(3,7)--cycle,paleblue);
draw((3,2)--(8,2)--(3,7)--cycle,blue+linewidth(1));
draw(A--B--C--cycle,linewidth(0.9));
dot((3,2),blue);
label("$A$",A,N);label("$B$",B,E);label("$C$",C,SW);
label("$(i,j)$",(3,2),SW,blue);'''
b.add(1765109,1,r'''In isosceles right triangle $ABC$ with right angle at $C$, $AC=BC=10$ units. Inside the triangle, horizontal segments (parallel to $BC$) are drawn $1$ unit apart, and vertical segments (parallel to $AC$) are drawn $1$ unit apart, each running from a leg to the hypotenuse $AB$, as shown. Including triangle $ABC$, how many triangles in this figure are isosceles?
'''+asy(qf,'5cm'),
r'''Put $C$ at the origin with $B=(10,0)$ and $A=(0,10)$. The figure consists of the horizontal lines $y=j$ and the vertical lines $x=i$ ($0\le i,j\le9$, including the legs) together with the hypotenuse $x+y=10$. A triangle needs three sides on three pairwise non-parallel lines, so it uses one horizontal line, one vertical line and the hypotenuse.
'''+asy(sf,'5cm')+r'''
The lines $x=i$ and $y=j$ meet at $(i,j)$, which lies inside the figure (or on a leg) exactly when $i+j\le9$; the triangle is then the one with vertices $(i,j)$, $(10-j,j)$ and $(i,10-i)$, whose legs both have length $10-i-j$. So every triangle in the figure is an isosceles right triangle, and they correspond to the pairs of integers $i,j\ge0$ with $i+j\le9$. Their number is
\[
10+9+8+\cdots+1=\boxed{55}.
\]''',
'Counting shapes in figures|Isosceles triangles|Right triangles|Triangular numbers',3,
note='The figure was not included; it is rebuilt from the description (horizontal and vertical segments 1 unit apart across the triangle, ending on the hypotenuse).')

# ---------------- 1764520 Legendre's formula (alias)
b.add(1764520,1,r'''Let $p$ be a prime and $n$ a positive integer.
\begin{enumerate}
\item[(a)] Prove Legendre's formula: the exponent of $p$ in the prime factorisation of $n!$ is
\[
\left\lfloor\dfrac{n}{p}\right\rfloor+\left\lfloor\dfrac{n}{p^2}\right\rfloor+\left\lfloor\dfrac{n}{p^3}\right\rfloor+\cdots .
\]
\item[(b)] Use it to find the exponent of $3$ in $100!$.
\end{enumerate}''',
r'''(a) The exponent of $p$ in $n!$ is the sum over $m=1,\dots,n$ of the exponent $e(m)$ of $p$ in $m$, and $e(m)$ is the number of $j\ge1$ with $p^j\mid m$. Counting by $j$ instead, the total is $\sum_{j\ge1}\#\{m\le n:p^j\mid m\}=\sum_{j\ge1}\left\lfloor\dfrac{n}{p^j}\right\rfloor$. $\blacksquare$

(b) $33+11+3+1=\boxed{48}$.''',
'Factorials|Floor and ceiling functions|Prime factorisation|Double counting',3,
note='Conceptual post ("can someone explain Legendre\'s formula?"); repeat of an earlier record (aliased).')

# ---------------- 1764199 power of 8 in 100!
b.add(1764199,1,r'''What is the largest power of $8$ that divides $100!$?''',
r'''By Legendre's formula, the exponent of $2$ in $100!$ is
\[
\left\lfloor\dfrac{100}{2}\right\rfloor+\left\lfloor\dfrac{100}{4}\right\rfloor+\left\lfloor\dfrac{100}{8}\right\rfloor+\left\lfloor\dfrac{100}{16}\right\rfloor+\left\lfloor\dfrac{100}{32}\right\rfloor+\left\lfloor\dfrac{100}{64}\right\rfloor=50+25+12+6+3+1=97 .
\]
Since $8^k=2^{3k}$ divides $100!$ exactly when $3k\le97$, the largest $k$ is $32$. The answer is $\boxed{8^{32}}$.''',
'Factorials|Prime factorisation|Floor and ceiling functions|Powers of two',2,
note='Posted as a MATHCOUNTS National Sprint question (year not given).')

# ---------------- 1764218 5P2
b.add(1764218,1,r'''Compute ${}_5P_2$, the number of permutations of $2$ objects chosen from $5$. Does order matter in a permutation?''',
r'''${}_5P_2$ counts ordered selections of $2$ of the $5$ objects: $5$ choices for the first and $4$ for the second, so
\[
{}_5P_2=\dfrac{5!}{(5-2)!}=5\cdot4=\boxed{20}.
\]
Yes, order matters: choosing $A$ then $B$ is a different permutation from $B$ then $A$. If order did not matter we would count combinations, $\dbinom52=\dfrac{20}{2!}=10$.''',
'Permutations|Combinations|Multiplication principle',1)

# ---------------- 1764798 Kangaroo grandchildren
b.add(1764798,1,r'''Granny has $10$ grandchildren, all of different ages (each age a whole number of years). Alice is the eldest. The sum of the ages of all the grandchildren is $180$. At least how old is Alice?''',
r'''Let Alice be $a$ years old. The other nine ages are different whole numbers less than $a$, so they are at most $a-1,a-2,\dots,a-9$. Hence
\[
180\le a+(a-1)+\cdots+(a-9)=10a-45,
\]
so $10a\ge225$ and $a\ge23$ (as $a$ is a whole number).

Age $23$ is possible: $23+22+\cdots+14=185$, and lowering the youngest age from $14$ to $9$ gives the different ages $23,22,21,20,19,18,17,16,15,9$ with sum $180$. So Alice is at least $\boxed{23}$ years old.''',
'Bounding and extremal cases|Arithmetic sequences|Inequalities',3,source=src('Math Kangaroo',2014,'Level 5-6',27),
note='Ages are taken to be whole numbers (otherwise the minimum 22.5 is not attained).')

# ---------------- 1763286 human on leash around hexagonal barn
fig=r'''real s=1.2, L=6, R=L-2s;
pair[] V; for(int k=0;k<6;++k) V[k]=s*dir(-90+60*k);
path hex=V[0]--V[1]--V[2]--V[3]--V[4]--V[5]--cycle;
real ph=degrees(acos(sqrt(3)/6));
filldraw(arc(V[0],L,150,390)--V[0]--cycle,palegray,gray);
filldraw(V[1]--arc(V[1],L-s,30,90)--cycle,paleblue,gray);
filldraw(V[5]--arc(V[5],L-s,90,150)--cycle,paleblue,gray);
filldraw(V[2]--arc(V[2],R,90,180-ph)--V[3]--cycle,palegreen,gray);
filldraw(V[4]--V[3]--arc(V[4],R,ph,90)--cycle,palegreen,gray);
pair X=V[2]+R*dir(180-ph);
filldraw(hex,white,black+linewidth(1));
draw(V[0]--(0,-L-s),dashed);draw(V[3]--X,dashed);
dot(V[0]);dot(X);
label("$V_0$",V[0],N);label("$V_1$",V[1],dir(150));label("$V_5$",V[5],dir(30));
label("$V_2$",V[2],dir(210));label("$V_4$",V[4],dir(-30));label("$V_3$",V[3],S);label("$X$",X,N);
label("$600$",V[0]+3.2*dir(-60),dir(30));
label("$480$",V[1]+2.6*dir(45),dir(-45));label("$360$",V[2]+2.2*dir(80),E);'''
b.add(1763286,1,r'''A goat keeps a pet human on a leash. One end of the leash is tied to the human and the other end to one vertex of the goat's barn, which is a regular hexagon of side length $120$. The leash has length $600$, it cannot pass through the barn, and the human must stay outside the barn. What is the area of the region the human can reach?''',
r'''Label the vertices $V_0,\dots,V_5$ in order, with the leash tied at $V_0$; $V_3$ is the opposite vertex. A point $P$ outside the barn is reachable when the shortest path from $V_0$ to $P$ that goes around the barn has length at most $600$. Such a path runs along the boundary, clockwise or counterclockwise, to some vertex $V_k$ and then straight to $P$.

\textbf{Halving the region.} The region is symmetric about the line $V_0V_3$ (dashed). For a point $P$ on the side of $V_1,V_2$, going round that way is never longer, so the half of the region on this side consists of
\begin{itemize}
\item half of the sector at $V_0$: the leash sweeps the exterior angle $240^\circ$ with radius $600$, and half of it is $\dfrac13\pi\cdot600^2=120000\pi$;
\item the sector at $V_1$: the leash has $480$ left and sweeps the exterior angle $60^\circ$: $\dfrac16\pi\cdot480^2=38400\pi$;
\item the part, on this side of the line $V_0V_3$, of the sector at $V_2$ with radius $360$ and angle $60^\circ$, bounded by the line $V_1V_2$ extended and the side $V_2V_3$ extended (green). Beyond the line $V_0V_3$ the other direction round takes over. A path wrapping round $V_3$ is never needed: going the other way round, via $V_4$, is at least as short there.
\end{itemize}
'''+asy(fig,'8cm')+r'''
\textbf{The clipped sector.} Put $V_3$ at the origin with the line $V_3V_0$ as the vertical axis. Then $V_2$ is at horizontal distance $120\cos30^\circ=60\sqrt3$ from the axis, and the sector at $V_2$ consists of the directions from straight up (along $V_1V_2$ extended) to the direction of $V_2V_3$, which makes $30^\circ$ with the horizontal. Measure the angle $\theta$ from the upward vertical towards $V_3$, so $\theta$ runs from $0$ to $60^\circ$. In direction $\theta$ the axis is at distance $\dfrac{60\sqrt3}{\sin\theta}$ from $V_2$, and the arc of radius $360$ meets the axis at $X$, where $\sin\theta_X=\dfrac{60\sqrt3}{360}=\dfrac{\sqrt3}{6}$. The part of the sector on our side is the sector minus the piece beyond the axis:
\[
21600\pi-\int_{\theta_X}^{\pi/3}\dfrac12\left(360^2-\dfrac{10800}{\sin^2\theta}\right)d\theta
=21600\pi-64800\left(\dfrac\pi3-\theta_X\right)+5400\left(\cot\theta_X-\cot\dfrac\pi3\right).
\]
Here $\cot\theta_X=\sqrt{11}$, $\cot\dfrac\pi3=\dfrac{1}{\sqrt3}$, and $\dfrac\pi3-\theta_X=\arctan\sqrt{11}-\dfrac\pi6$ (because $\dfrac\pi2-\theta_X$ is the angle whose tangent is $\sqrt{11}$).

\textbf{Total.} The whole area is twice the half:
\[
2\left[120000\pi+38400\pi+21600\pi-64800\left(\arctan\sqrt{11}-\dfrac\pi6\right)+5400\sqrt{11}-1800\sqrt3\right],
\]
that is,
\[
\boxed{381600\pi-129600\arctan\sqrt{11}+10800\sqrt{11}-3600\sqrt3}\approx1.0628\times10^{6}.
\]
(Adding the full sectors $240000\pi+2\cdot38400\pi+2\cdot21600\pi=360000\pi\approx1.131\times10^6$ would count the overlap of the two sectors behind $V_3$ twice.)''',
'Regular polygons|Circles|Arcs and chords|Lengths, perimeter, and area|Area decomposition|Symmetry|Calculus',7,
note='No answer was posted. The overlap of the regions behind the far vertex makes the exact answer involve arctan(sqrt 11); the result was checked by a Monte Carlo computation of the set of points whose shortest path around the hexagon to the tie point is at most 600 (agreement to 0.1%, within the sampling error) and by numerical integration of the clipped sector.')

# ---------------- 1764207 square ADEF
fig=r'''pair D=(0,0),C=(1,0),B=(1,1),A=(0,1),Ep=(0.5,0),F=(0.5,0.625);
fill(A--D--Ep--F--cycle,paleblue);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(Ep--F,linewidth(0.8));draw(A--F--B,linewidth(0.8));
draw(Ep+(0.05,0)--Ep+(0.05,0.05)--Ep+(0,0.05));
label("$A$",A,NW);label("$B$",B,NE);label("$C$",C,SE);label("$D$",D,SW);
label("$E$",Ep,S);label("$F$",F,dir(-20));
label("$y$",(Ep+F)/2,W);label("$y$",(A+F)/2,SW);label("$1-y$",(0.5,0.81),E);
label("$\dfrac12$",(0.25,0),S);'''
b.add(1764207,1,r'''Square $ABCD$ has side length $1$. Point $E$ lies on $\overline{CD}$ and point $F$ lies inside the square so that $\overline{EF}\perp\overline{DC}$ and $AF=BF=EF$. Find the area of quadrilateral $ADEF$.''',
r'''Put $D=(0,0)$, $C=(1,0)$, $B=(1,1)$, $A=(0,1)$. Since $AF=BF$, the point $F$ is on the perpendicular bisector $x=\dfrac12$ of $AB$; as $EF\perp DC$, also $E=\left(\dfrac12,0\right)$. Let $F=\left(\dfrac12,y\right)$, so $EF=y$.
'''+asy(fig,'5cm')+r'''
Then $AF=EF$ gives
\[
\left(\dfrac12\right)^2+(1-y)^2=y^2\ \Longrightarrow\ \dfrac14+1-2y=0\ \Longrightarrow\ y=\dfrac58 .
\]
$ADEF$ is a right trapezoid with parallel sides $AD=1$ and $EF=\dfrac58$ and width $DE=\dfrac12$, so its area is
\[
\dfrac12\left(1+\dfrac58\right)\cdot\dfrac12=\boxed{\dfrac{13}{32}}.
\]''',
'Squares|Trapezoids|Perpendicular bisectors|Pythagorean theorem|Coordinate geometry|Lengths, perimeter, and area',3)

# ---------------- 1763710 digits a,b,c, sum of two-digit numbers
b.add(1763710,1,r'''Let $a,b,c$ be nonzero digits (not necessarily different). Let $S$ be the sum of the nine two-digit numbers $\overline{xy}$ obtained by choosing the tens digit $x$ and the units digit $y$ each from $a,b,c$ (all $3\cdot3$ choices, so $\overline{aa},\overline{ab},\overline{ac},\overline{ba},\dots,\overline{cc}$, counted with repetition).
\begin{enumerate}
\item[(a)] Find $S$ divided by $3$ in terms of $a,b,c$.
\item[(b)] Find all three-digit numbers $\overline{abc}$ for which $S=165$.
\end{enumerate}''',
r'''(a) Each of $a,b,c$ is the tens digit of $3$ of the nine numbers and the units digit of $3$ of them, so
\[
S=10\cdot3(a+b+c)+3(a+b+c)=33(a+b+c),\qquad \dfrac S3=\boxed{11(a+b+c)}.
\]
(b) $S=165$ means $a+b+c=5$ with nonzero digits. The multisets of digits are $\{1,1,3\}$ and $\{1,2,2\}$, giving
\[
\boxed{113,\ 131,\ 311,\ 122,\ 212,\ 221}.
\]''',
'Place value|Digit problems|Systematic counting',2,
note='The post says "non-negative digits" and "including numbers with same digits". A zero digit would give "numbers" with a leading zero, and repeated digits would make "all two-digit numbers" ambiguous, so the record takes nonzero digits and the nine ordered choices counted with repetition (the reading that gives a quotient S/3 for every a, b, c).')

# ---------------- 1764107 a, a^2, ..., a^b complete residue system mod b
b.add(1764107,1,r'''Find all pairs of positive integers $(a,b)$ such that $a^1,a^2,\dots,a^b$ form a complete residue system modulo $b$ (that is, they leave the remainders $0,1,\dots,b-1$ in some order).''',
r'''For $b=1$ every $a$ works, since every integer is $\equiv0\pmod1$.

Let $b\ge2$. One of the powers must be $\equiv0\pmod b$ and another must be $\equiv1\pmod b$. If $a^k\equiv1\pmod b$ then $\gcd(a,b)=1$, so $\gcd(a^j,b)=1$ for every $j$, and no power of $a$ is divisible by $b\ge2$. This contradiction shows that no pair with $b\ge2$ works.

So the pairs are exactly $\boxed{(a,1)\text{ for every positive integer }a}$.''',
'Remainders and congruences|HCF and LCM|Proof by contradiction',3,
note='The post asks "what relationship does a have to b if a^1, ..., a^b is a complete residue system modulo b"; the record asks for all such pairs (only the trivial modulus b = 1).')

# ---------------- 1760189 stars and bars P1-P3
b.add(1760189,1,r'''How many solutions does $x_1+x_2+x_3+x_4=22$ have in positive integers?''',
r'''Think of $22$ stars in a row; a solution corresponds to placing $3$ bars in the $21$ gaps between stars (at most one bar per gap), cutting the row into $4$ nonempty groups. So the number of solutions is
\[
\dbinom{21}{3}=\boxed{1330}.
\]''',
'Stars and bars|Distributions and integer solutions|Combinations',2,
note='x_i in N is read as positive integers. (For nonnegative integers the count would be C(25,3) = 2300.)')
b.add(1760189,2,r'''Some identical Rubik's cubes are to be given to friends (a friend may get none).
\begin{enumerate}
\item In how many ways can you give: (A) $3$ cubes to $2$ people; (B) $4$ cubes to $2$ people; (C) $5$ cubes to $2$ people; (D) $3$ cubes to $3$ people; (E) $4$ cubes to $3$ people; (F) $5$ cubes to $3$ people?
\item Find, with an explanation, the number of ways to give $7$ cubes to $4$ people.
\item How do the answers to parts 1 and 2 change if each person must get at least one cube?
\end{enumerate}''',
r'''Line up the $n$ cubes and insert $k-1$ dividers among them to split the row among $k$ people in order. Any arrangement of $n$ cubes and $k-1$ dividers in a row gives one distribution, so the number of distributions is the number of ways to choose the divider positions among $n+k-1$ places:
\[
\dbinom{n+k-1}{k-1}.
\]
1. (A) $\dbinom41=4$; (B) $\dbinom51=5$; (C) $\dbinom61=6$; (D) $\dbinom52=10$; (E) $\dbinom62=15$; (F) $\dbinom72=21$.

2. $\dbinom{10}{3}=\boxed{120}$ (the pattern above: $n+1$ ways for $2$ people, the triangular numbers $\dbinom{n+2}{2}$ for $3$ people).

3. If everyone gets at least one cube, first give each person one cube and distribute the remaining $n-k$ freely: $\dbinom{n-1}{k-1}$ ways. The answers become (A) $2$, (B) $3$, (C) $4$, (D) $1$, (E) $3$, (F) $6$, and $7$ cubes to $4$ people: $\dbinom63=\boxed{20}$.''',
'Stars and bars|Distributions and integer solutions|Combinations|Pattern recognition',2)
b.add(1760189,3,r'''How many solutions in nonnegative integers does the inequality $x_1+x_2+\cdots+x_6<10$ have?''',
r'''The inequality means $x_1+\cdots+x_6\le9$. Add a slack variable $x_7=9-(x_1+\cdots+x_6)\ge0$; the solutions correspond exactly to the nonnegative solutions of $x_1+\cdots+x_7=9$. By stars and bars there are
\[
\dbinom{9+6}{6}=\dbinom{15}{6}=\boxed{5005}.
\]''',
'Stars and bars|Distributions and integer solutions|Inequalities',3)

# ---------------- 1763215 isosceles trapezoid: shorter base not determined
fig1=r'''pair D=(0,0),Ep=(1,0),A=(1,sqrt(3)),B=(3,sqrt(3)),C=(4,0);
draw(D--C--B--A--cycle,linewidth(0.9));
draw(A--Ep,dashed);draw(B--Ep,blue);
draw(Ep+(0,0.15)--Ep+(0.15,0.15)--Ep+(0.15,0));
label("$D$",D,SW);label("$E$",Ep,S);label("$C$",C,SE);label("$A$",A,N);label("$B$",B,N);
label("$1$",(D+Ep)/2,S);label("$2$",(D+A)/2,W);label("$2$",(C+B)/2,E);label("$AB=2$",(A+B)/2,N);'''
fig2=r'''pair D=(0,0),Ep=(1,0),A=(1,sqrt(3)),B=(5,sqrt(3)),C=(6,0);
draw(D--C--B--A--cycle,linewidth(0.9));
draw(A--Ep,dashed);draw(B--Ep,blue);
draw(Ep+(0,0.15)--Ep+(0.15,0.15)--Ep+(0.15,0));
label("$D$",D,SW);label("$E$",Ep,S);label("$C$",C,SE);label("$A$",A,N);label("$B$",B,N);
label("$1$",(D+Ep)/2,S);label("$2$",(D+A)/2,W);label("$2$",(C+B)/2,E);label("$AB=4$",(A+B)/2,N);'''
b.add(1763215,1,r'''In an isosceles trapezoid $ABCD$ with $AB\parallel DC$ and $AB<DC$, an altitude is dropped from $A$ to the point $E$ on the longer base $DC$. The legs $AD$ and $BC$ are $2$ cm long and $DE=1$ cm, and segment $BE$ is drawn. Show that the length of the shorter base $AB$ is not determined by this information. (A student argues that $AB$ must be $2$ cm, because ``$BE$ is an altitude, so triangle $EAB$ has a right angle at $A$, and the figure splits into three equilateral triangles''. Find the error.)''',
r'''Let $AB=x$ for any $x>0$, and put $D=(0,0)$, $E=(1,0)$, $A=(1,\sqrt3)$, $B=(1+x,\sqrt3)$, $C=(2+x,0)$. Then $AD=\sqrt{1+3}=2$, $BC=2$, $AE\perp DC$ with $DE=1$, $AB\parallel DC$ and $AB=x<DC=x+2$. So every $x>0$ gives a trapezoid with all the stated properties; drawing $BE$ adds no condition. Two of them:
'''+asy(fig1,'4.5cm')+asy(fig2,'5.5cm')+r'''
Hence $\boxed{\text{the shorter base can be any positive length}}$; only the relation $DC=AB+2$ is forced.

The student's error is the unjustified assumption that the figure has three equilateral triangles. $\angle EAB=90^\circ$ is true for every $x$ (because $AE\perp DC\parallel AB$), but nothing says that $BE$ bisects an angle or that $\triangle EBC$ is equilateral; that holds only in the special case $x=2$ (left), where $BE=2$. In the right figure, $x=4$, triangle $EBC$ is not equilateral.''',
'Trapezoids|Isosceles triangles|Special right triangles|Counterexamples|Coordinate geometry',2,
note='The poster (and the duplicate topic 1763217) argue whether the shorter base is 2 or undetermined; the record asks to show it is undetermined and to find the error in the "three equilateral triangles" argument.')

b.save()
