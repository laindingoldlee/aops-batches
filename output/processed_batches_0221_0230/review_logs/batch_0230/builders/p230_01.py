from qb import *
b=Bank('p230_01')

# ---------------- 1739467 remove K from 1..n
b.add(1739467,1,r'''The numbers $1,2,3,\dots,n$ are written on a board. After one number $K$ is erased, the arithmetic mean of the remaining $n-1$ numbers is $46\dfrac{20}{23}$. Find $K$.''',
r'''The mean $46\dfrac{20}{23}=\dfrac{1078}{23}$ has denominator $23$, and the sum of the remaining numbers, $(n-1)\cdot\dfrac{1078}{23}$, is an integer. Since $\gcd(1078,23)=1$, $23$ divides $n-1$.

Erasing one number changes the mean only a little. If the largest number $n$ is erased the mean is $\dfrac{1+2+\dots+(n-1)}{n-1}=\dfrac n2$, and if $1$ is erased it is $\dfrac{n+2}{2}$. So
\[
\dfrac n2\le\dfrac{1078}{23}\le\dfrac{n+2}{2}\quad\Longrightarrow\quad 91<n<94,
\]
so $n=92$ or $93$, and $n-1$ divisible by $23$ forces $n=93$. Then the remaining sum is $92\cdot\dfrac{1078}{23}=4\cdot1078=4312$, while $1+2+\dots+93=\dfrac{93\cdot94}{2}=4371$. Hence
\[
K=4371-4312=\boxed{59}.
\]''',
'Averages and weighted averages|Arithmetic sequences|Summation|Bounding and extremal cases',3,
note='"46 (whole) 20/23" is read as the mixed number 46 20/23.')

# ---------------- 1740263 product and quotient of fractions
b.add(1740263,1,r'''The product of two positive fractions is $\dfrac{14}{15}$, and dividing one of them by the other gives $\dfrac{35}{24}$. What is the greater of the two fractions?''',
r'''Let the fractions be $x$ and $y$ with $xy=\dfrac{14}{15}$ and $\dfrac xy=\dfrac{35}{24}$. Multiplying the two equations,
\[
x^2=\dfrac{14}{15}\cdot\dfrac{35}{24}=\dfrac{490}{360}=\dfrac{49}{36},
\]
so $x=\dfrac76$ (as $x>0$), and $y=\dfrac{14}{15}\div\dfrac76=\dfrac{14}{15}\cdot\dfrac67=\dfrac45$. Since $\dfrac xy>1$, $x$ is the greater one: the answer is $\boxed{\dfrac76}$. Check: $\dfrac76\cdot\dfrac45=\dfrac{28}{30}=\dfrac{14}{15}$ and $\dfrac76\div\dfrac45=\dfrac{35}{24}$.''',
'Fractions|Equations and systems of equations',2,
note='"Positive" is added: without it the pair -7/6, -4/5 also works and then -4/5 is the greater fraction.')

# ---------------- 1568921 AM-GM by a picture
fig=r'''real a=3,b=1.4,s=a+b;
pen f=rgb(0.82,0.9,1);
filldraw((0,0)--(a,0)--(a,b)--(0,b)--cycle,f,linewidth(0.8));
filldraw((a,0)--(s,0)--(s,a)--(a,a)--cycle,f,linewidth(0.8));
filldraw((b,a)--(s,a)--(s,s)--(b,s)--cycle,f,linewidth(0.8));
filldraw((0,b)--(b,b)--(b,s)--(0,s)--cycle,f,linewidth(0.8));
draw((0,0)--(s,0)--(s,s)--(0,s)--cycle,linewidth(1));
label("$a$",(a/2,0),S);label("$b$",(a+b/2,0),S);
label("$b$",(0,b/2),W);label("$a$",(0,b+a/2),W);
label("$ab$",(a/2,b/2));label("$ab$",(a+b/2,a/2));label("$ab$",(b+a/2,a+b/2));label("$ab$",(b/2,b+a/2));
label("$(a-b)^2$",((a+b)/2,(a+b)/2),fontsize(9pt));'''
b.add(1568921,1,r'''Prove, using a picture instead of algebraic computation, that for all positive real numbers $a$ and $b$,
\[
\dfrac{a+b}{2}\ge\sqrt{ab},
\]
with equality only when $a=b$.''',
r'''Suppose $a\ge b$ (otherwise swap them). Draw a square of side $a+b$ and place four $a\times b$ rectangles inside it in a pinwheel, each rectangle starting at a corner of the square and running along one side:
'''+asy(fig,'4.6cm')+r'''
The four rectangles do not overlap, and they leave a small square hole in the middle of side $a-b$. So the big square, of area $(a+b)^2$, contains four rectangles of total area $4ab$:
\[
(a+b)^2\ge 4ab .
\]
The hole is empty exactly when $a=b$, so equality holds only then. Taking square roots of both (positive) sides gives $a+b\ge2\sqrt{ab}$, which is the claim $\dfrac{a+b}{2}\ge\sqrt{ab}$. $\blacksquare$''',
'AM-GM inequality|Inequalities|Area decomposition|Squares',3,
note='The post asks for a proof of AM-GM "with just words and reasoning"; the record asks for the classical picture proof of the two-variable case.')

# ---------------- 1738949 3x^10/y^10 = 1991
b.add(1738949,1,r'''Prove that the equation
\[
\dfrac{3x^{10}}{y^{10}}=1991
\]
has no solutions in integers $x,y$ (with $y\ne0$).''',
r'''Suppose integers $x$ and $y\ne0$ satisfy $3x^{10}=1991\,y^{10}$. Then $x\ne0$ too. Look at the exponent of the prime $3$ in both sides. Write $3^p\parallel x$ and $3^q\parallel y$ (the exact powers of $3$ dividing $x$ and $y$). Since $1991=11\cdot181$ is not divisible by $3$, the exponent of $3$ is $10p+1$ on the left and $10q$ on the right. But $10p+1\equiv1\pmod{10}$ and $10q\equiv0\pmod{10}$, so they cannot be equal, contradicting unique prime factorisation. Hence there are no integer solutions. $\blacksquare$''',
'Diophantine equations|Prime factorisation|Exponents|Proof by contradiction',3)

# ---------------- 1739977 nested radical
b.add(1739977,1,r'''Find all positive integers $n\le40$ for which
\[
\sqrt{n+\sqrt{n+\sqrt{n+\cdots}}}
\]
(infinitely many nested square roots) is an integer.''',
r'''The nested radical is the limit $L$ of $a_1=\sqrt n$, $a_{k+1}=\sqrt{n+a_k}$. This sequence is increasing (by induction, $a_{k+1}>a_k$ because $a_2>a_1$ and $t\mapsto\sqrt{n+t}$ is increasing) and bounded above by the positive root of $t^2=n+t$, so it converges, and its limit satisfies
\[
L=\sqrt{n+L}\quad\Longrightarrow\quad L^2-L=n,\qquad L=\dfrac{1+\sqrt{1+4n}}{2}.
\]
So $L$ is an integer $m$ exactly when $n=m(m-1)$. Since $n\ge1$ we need $m\ge2$, and $m(m-1)\le40$ gives $m\le6$. Hence
\[
n\in\{\boxed{2,\ 6,\ 12,\ 20,\ 30}\},
\]
with values $L=2,3,4,5,6$ respectively.''',
'Radicals|Sequences and series|Quadratic equations',3,
note='The garbled "sqrt of n + sqrt n....(whole root)" is read as the infinite nested radical sqrt(n + sqrt(n + ...)).')

# ---------------- 1739930 largest multiple of 12 with all ten digits
b.add(1739930,1,r'''What is the largest multiple of $12$ that can be written using each of the digits $0,1,2,3,4,5,6,7,8,9$ exactly once?''',
r'''A number is a multiple of $12$ exactly when it is divisible by $3$ and by $4$. The digit sum is $0+1+\dots+9=45$, so every such ten-digit number is divisible by $3$. We need its last two digits to form a multiple of $4$.

To make the number as large as possible, keep the leading digits as large as possible. With the first eight digits $98765432$ the last two digits are $1,0$ in some order, and neither $10$ nor $01$ is a multiple of $4$. With the first seven digits $9876543$ the last three digits are $2,1,0$ in some order; the largest arrangement whose last two digits form a multiple of $4$ is $120$ ($20$ is divisible by $4$, while $210$ and $201$ end in $10$ and $01$). So the answer is
\[
\boxed{9876543120}.
\]''',
'Divisibility rules|Digits and bases|Factors and multiples',2)

# ---------------- 1736311 sum over all operator choices
b.add(1736311,1,r'''Consider the expression
\[
2\ \square\ 2\ \square\ 2\ \square\ \cdots\ \square\ 2
\]
with $2018$ twos and $2017$ blanks. Each blank is filled with one of $+$, $-$, $\times$, $\div$, giving $4^{2017}$ expressions, and each expression is evaluated with the usual order of operations. Find the sum of all $4^{2017}$ results.''',
r'''Let there be $n$ twos in general (here $n=2018$). Each expression is a sum of signed \emph{terms}, the blocks of twos joined by $\times$ and $\div$:
\[
\text{value}=T_1\pm T_2\pm\cdots\pm T_r ,
\]
where $T_1$ is the first block and the sign of every later term is the $+$ or $-$ in front of it.

\textbf{Later terms cancel.} Fix an expression and a term $T_i$ with $i\ge2$. Changing the sign in front of $T_i$ (from $+$ to $-$ or back) gives another expression with exactly the same terms. These two expressions contribute $+T_i$ and $-T_i$, so over all expressions the contributions of all terms other than the first cancel. Hence the total is the sum, over all expressions, of the first term $T_1$.

\textbf{The first term.} Suppose the first block has $k$ twos. Its $k-1$ operations are $\times$ or $\div$, and each $\times2$ multiplies by $2$ while each $\div2$ multiplies by $\dfrac12$, so summing over the $2^{k-1}$ choices,
\[
\sum T_1=2\left(2+\dfrac12\right)^{k-1}=2\left(\dfrac52\right)^{k-1}.
\]
If $k<n$, the next operation is $+$ or $-$ ($2$ choices) and the remaining $n-1-k$ operations are free ($4^{n-1-k}$ choices). If $k=n$ the whole expression is one block. So the total is
\[
\sum_{k=1}^{n-1}2\left(\dfrac52\right)^{k-1}\cdot2\cdot4^{n-1-k}+2\left(\dfrac52\right)^{n-1}
=4^{n-1}\sum_{j=0}^{n-2}\left(\dfrac58\right)^{j}+2\left(\dfrac52\right)^{n-1}.
\]
The geometric sum is $\dfrac{1-\left(\dfrac58\right)^{n-1}}{\dfrac38}$, so the total is
\[
\dfrac83\cdot4^{n-1}-\dfrac83\left(\dfrac52\right)^{n-1}+2\left(\dfrac52\right)^{n-1}=\dfrac23\left(4^{n}-\left(\dfrac52\right)^{n-1}\right).
\]
(For example $n=2$: $4+0+4+1=9=\dfrac23\left(16-\dfrac52\right)$.) For $n=2018$ the sum of all results is
\[
\boxed{\dfrac23\left(4^{2018}-\left(\dfrac52\right)^{2017}\right)=\dfrac{2^{6053}-5^{2017}}{3\cdot2^{2016}}}.
\]''',
'Summation|Geometric sequences|Pairing and grouping|Symmetry|Order of operations',6,
note='The formula was checked by brute force over all operator choices for 1 to 7 twos with exact fractions.')

# ---------------- 1739351 divide by 3 or subtract 1
b.add(1739351,1,r'''A sequence of positive integers is generated as follows: if the current term is divisible by $3$, the next term is the current term divided by $3$; otherwise the next term is the current term minus $1$. If the first term is a three-digit number and the sixth term is $1$, what is the sum of all possible first terms?''',
r'''Work backwards. A term $x$ can be preceded by $3x$ (always, since $3x$ is divisible by $3$), or by $x+1$, but only when $x+1$ is \emph{not} divisible by $3$.

\begin{itemize}
\item Term 6: $1$.
\item Term 5: $3$ or $2$.
\item Term 4: from $3$: $9$ or $4$; from $2$: $6$ (not $3$, which is divisible by $3$). So $9,4,6$.
\item Term 3: $27,10$; $12,5$; $18,7$.
\item Term 2: $81,28$; $30,11$; $36,13$; $15$ (not $6$); $54,19$; $21,8$.
\item Term 1: each term-2 value $x$ gives $3x$ and possibly $x+1$. The values $x+1$ are all at most $82$, and $3x$ is a three-digit number only for $x=81,36,54$, giving $243,108,162$.
\end{itemize}
Check: $243\to81\to27\to9\to3\to1$, $108\to36\to12\to4\to3\to1$, $162\to54\to18\to6\to2\to1$. The sum is $243+108+162=\boxed{513}$.''',
'Working backwards|Recurrence relations|Divisibility',3)

# ---------------- 1739592 AM-GM for n numbers, elementary proof
b.add(1739592,1,r'''Let $x_1,x_2,\dots,x_n$ be positive real numbers with arithmetic mean $A=\dfrac{x_1+x_2+\cdots+x_n}{n}$. Prove, without calculus, that
\[
x_1x_2\cdots x_n\le A^n ,
\]
with equality only when all the numbers are equal.''',
r'''If all the numbers equal $A$, the product is $A^n$. Otherwise some number is larger than $A$ and some number is smaller than $A$ (they cannot all be on the same side, since their average is $A$); say $x_i>A>x_j$.

\textbf{Smoothing step.} Replace $x_i$ by $A$ and $x_j$ by $x_i+x_j-A$. The new numbers are still positive ($x_i+x_j-A>x_j>0$), their sum and therefore their mean $A$ are unchanged, and the product of the two changed numbers increases:
\[
A(x_i+x_j-A)-x_ix_j=(x_i-A)(A-x_j)>0 .
\]
The other numbers are untouched, so the whole product strictly increases. Moreover, the number of entries equal to $A$ goes up by at least one.

\textbf{Repeat.} After at most $n-1$ smoothing steps every entry equals $A$ (once $n-1$ entries equal $A$, the last one does too, because the sum is $nA$). The product has strictly increased at every step and ends at $A^n$. Hence, if the numbers were not all equal, the original product was strictly less than $A^n$. Together with the equality case this proves $x_1x_2\cdots x_n\le A^n$, with equality only when all $x_k$ are equal. $\blacksquare$

(Taking $n$-th roots gives the familiar form $\dfrac{x_1+\cdots+x_n}{n}\ge\sqrt[n]{x_1x_2\cdots x_n}$.)''',
'AM-GM inequality|Inequalities|Invariants and monovariants',4,
note='The post asks for a proof of AM-GM using only middle-school mathematics; the record gives the smoothing proof for n numbers.')

# ---------------- 1739370 necklace with colour blocks
b.add(1739370,1,r'''Three red beads, five blue beads, four green beads and three white beads are put on a necklace so that all beads of the same colour are next to each other. Beads of the same colour are identical, and two necklaces are the same if one can be turned into the other by rotating it or flipping it over. How many different necklaces are there?

A student says the answer is $6$, the circular arrangements of $4$ objects; another says $24$, because rotations should not be counted. Who, if anyone, is right?''',
r'''Since each colour forms one block, a necklace is determined by the cyclic order of the four blocks R, B, G, W around the circle. Up to rotation, the number of cyclic orders of $4$ distinct blocks is $\dfrac{4!}{4}=3!=6$: fix R and order the other three after it.

A necklace can also be flipped over, which reverses the cyclic order. For four distinct blocks a cyclic order is never the same as its reverse (for example R,B,G,W reversed is R,W,G,B), so the $6$ cyclic orders fall into $3$ mirror pairs:
\[
\{\text{RBGW},\text{RWGB}\},\quad\{\text{RBWG},\text{RGWB}\},\quad\{\text{RGBW},\text{RWBG}\}.
\]
So there are $\boxed{3}$ different necklaces.

The student's $6$ is the right count if the necklace may be rotated but not flipped (for instance, if it has a clasp on one side). The answer $24=4!$ counts the orders of four blocks in a row, which is not a count of necklaces at all: a circle has no first position, so rotations of the same arrangement must be identified.''',
'Circular arrangements|Permutations|Symmetry',2,
note='The teacher\'s answer 24 is not correct. "Necklace" is read with rotations and reflections identified (answer 3); the solution also explains that 6 counts rotations only.')

# ---------------- 1737760 1999^2000 mod 5 (alias)
b.add(1737760,1,r'''When $1999^{2000}$ is divided by $5$, what is the remainder?''',
r'''Since $1999\equiv-1\pmod 5$, we get $1999^{2000}\equiv(-1)^{2000}=1\pmod5$. The remainder is $\boxed{1}$.''',
'Remainders and congruences|Modular exponentiation',1,
note='Repeat of an earlier record (aliased).')

# ---------------- 1738860 rectangle AP:PC
fig=r'''pair A=(0,0),B=(6,0),C=(6,4),D=(0,4),Ep=(6,4/3),F=(3,4),P=(30/7,20/7),G=(7.5,0);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--C,linewidth(0.8));draw(F--Ep,linewidth(0.8));
draw(B--G,dashed);draw(Ep--G,dashed);
draw((1.5,3.85)--(1.5,4.15));draw((4.5,3.85)--(4.5,4.15));
dot(P);
label("$A$",A,SW);label("$B$",B,S);label("$C$",C,NE);label("$D$",D,NW);
label("$E$",Ep,dir(20));label("$F$",F,N);label("$P$",P+(0,0.12),dir(88));label("$G$",G,S);'''
b.add(1738860,1,r'''In rectangle $ABCD$, points $E$ and $F$ lie on sides $BC$ and $CD$, respectively. Point $F$ is the midpoint of $CD$, and $BE=\dfrac13BC$. Segments $AC$ and $FE$ intersect at point $P$. What is the ratio of $AP$ to $PC$? Express your answer as a common fraction.''',
r'''Extend $FE$ beyond $E$ to meet line $AB$ (extended beyond $B$) at $G$.
'''+asy(fig,'6cm')+r'''
Let $AB=w$ and $BC=h$. Then $BE=\dfrac h3$ and $EC=\dfrac{2h}{3}$, and $FC=\dfrac w2$. Triangles $EBG$ and $ECF$ are similar (vertical angles at $E$ and right angles at $B$ and $C$), so
\[
\dfrac{BG}{CF}=\dfrac{BE}{EC}=\dfrac12,\qquad BG=\dfrac w4,\qquad AG=w+\dfrac w4=\dfrac{5w}{4}.
\]
Now $AG\parallel CF$, so triangles $APG$ and $CPF$ are similar (alternate angles), and
\[
\dfrac{AP}{PC}=\dfrac{AG}{CF}=\dfrac{5w}{4}\cdot\dfrac{2}{w}=\boxed{\dfrac52}.
\]
(Check with coordinates $A=(0,0)$, $C=(w,h)$, $E=\left(w,\dfrac h3\right)$, $F=\left(\dfrac w2,h\right)$: the lines meet at $P=\dfrac57\,C$.)''',
'Rectangles|Similarity|Midpoints|Parallel lines',3,
note='The figure was attached; the text determines it. The poster asks for a method without coordinates, so the solution uses similar triangles. The figure uses a 6 by 4 rectangle.')

# ---------------- 1737110 taxicab number
b.add(1737110,1,r'''Ramanujan knew that there are four different positive integers $A,B,C,D$ with
\[
A^3+B^3=1729\quad\text{and}\quad C^3+D^3=1729 .
\]
Find $A+B+C+D$.''',
r'''The cubes below $1729$ are $1,8,27,64,125,216,343,512,729,1000,1331,1728$. Checking which pairs add up to $1729$: $1729-1728=1=1^3$ and $1729-1000=729=9^3$, and no other difference $1729-k^3$ (for $k=10,11,12$ or $k\le9$) is a cube apart from these. So
\[
1729=1^3+12^3=9^3+10^3,
\]
and $A+B+C+D=1+12+9+10=\boxed{32}$.''',
'Perfect cubes|Diophantine equations|Systematic counting',2)

# ---------------- 1737382 random marathon P2, P3
b.add(1737382,2,r'''At how many points does the parabola $y=x^2+8x+7$ intersect the line $y=6x+18$?''',
r'''At an intersection point $x^2+8x+7=6x+18$, that is $x^2+2x-11=0$. The discriminant is $2^2+4\cdot11=48>0$, so there are two real solutions $x=-1\pm2\sqrt3$, each giving one point. The answer is $\boxed{2}$.''',
'Quadratic equations|Equations and systems of equations',2,
note='Problem P2 of a marathon post; "a parabola with formula x^2+8x+7" is read as y = x^2+8x+7.')
b.add(1737382,3,r'''A linear function $f$ satisfies $f(0)=7$ and $f(2)=17$. Find
\[
f(0)+f(1)+f(2)+\cdots+f(127).
\]''',
r'''A linear function has the form $f(x)=mx+c$. From $f(0)=7$ we get $c=7$, and $f(2)=2m+7=17$ gives $m=5$. So $f(x)=5x+7$, and
\[
\sum_{x=0}^{127}(5x+7)=5\cdot\dfrac{127\cdot128}{2}+7\cdot128=40640+896=\boxed{41536}.
\]''',
'Functions|Arithmetic sequences|Summation',2,
note='Problem P3 of the marathon. As posted, f is not determined by f(0) and f(2); the word "linear" is added, which is clearly intended.')

# ---------------- 1738601 sums of three numbers
b.add(1738601,1,r'''Three friends each select a different number from the set $\{1,2,3,11,12,13,21,22,23\}$ and add the three numbers together. If they repeat this for all possible choices, how many different sums can they get?''',
r'''Write each number as $10a+b$ with tens digit $a\in\{0,1,2\}$ and units digit $b\in\{1,2,3\}$; the nine numbers are all nine pairs $(a,b)$. For three different numbers let $T$ be the sum of the tens digits and $U$ the sum of the units digits. The sum is $10T+U$ with $3\le U\le9$, so different pairs $(T,U)$ give different sums, and we count the achievable pairs.

\begin{itemize}
\item $T=0$: all three numbers are $1,2,3$, so $U=6$: $1$ sum. Similarly $T=6$ ($21,22,23$): $1$ sum.
\item $T=1$: two numbers with $a=0$ (different units digits, $b_1+b_2\in\{3,4,5\}$) and one with $a=1$ ($b_3\in\{1,2,3\}$), so $U$ takes every value from $4$ to $8$: $5$ sums. By symmetry $T=5$ also gives $5$ sums.
\item $T=2$: tens digits $0,0,2$ or $0,1,1$; in both cases $U$ is a sum of two different units digits and one more, again every value $4,\dots,8$, and $U=3$ or $9$ would need three equal units digits, i.e.\ tens digits $0,1,2$. So $5$ sums; likewise $T=4$.
\item $T=3$: tens digits $0,1,2$ allow any three units digits, so $U=3,\dots,9$: $7$ sums (tens digits $1,1,1$ give only $U=6$ again).
\end{itemize}
In total $1+5+5+7+5+5+1=\boxed{29}$ different sums.''',
'Casework|Systematic counting|Place value',3,
note='"Select a number and remove it" is read as three different numbers. Checked by listing all 84 triples.')

# ---------------- 1550572 multiples of 15, 20, 25
b.add(1550572,1,r'''How many numbers from $1000$ to $2000$ have all three of the numbers $15$, $20$ and $25$ as factors?''',
r'''A number has $15=3\cdot5$, $20=2^2\cdot5$ and $25=5^2$ as factors exactly when it is a multiple of
\[
\operatorname{lcm}(15,20,25)=2^2\cdot3\cdot5^2=300 .
\]
The multiples of $300$ from $1000$ to $2000$ are $1200,1500,1800$, so the answer is $\boxed{3}$.''',
'HCF and LCM|Factors and multiples',1,
note='P1 of an AMC 8 marathon thread (the contest year is not given).')

# ---------------- 1730993 expected throws until a 6
b.add(1730993,1,r'''On average, how many times must a fair die be thrown until a $6$ appears for the first time?''',
r'''Let $E$ be the expected number of throws. The first throw is a $6$ with probability $\dfrac16$, and then one throw was needed. With probability $\dfrac56$ it is not a $6$; then one throw has been used and the situation starts afresh, so on average $E$ more throws are needed. Hence
\[
E=1+\dfrac56E\quad\Longrightarrow\quad\dfrac16E=1\quad\Longrightarrow\quad E=\boxed{6}.
\]
(Directly: $E=\sum_{k\ge1}k\left(\dfrac56\right)^{k-1}\dfrac16=\dfrac16\cdot\dfrac{1}{\left(1-\dfrac56\right)^2}=6$.)''',
'Expected value|Geometric distribution|Dice probability|Recursive probability',3,
note='From Fifty Challenging Problems in Probability (Mosteller); the poster asks for an explanation of the book solution.')

# ---------------- 1738261 tribonacci 1,2,3
b.add(1738261,1,r'''The first three terms of a sequence are $1$, $2$ and $3$. Each later term is the sum of the three terms before it. What is the $11$th term of the sequence?''',
r'''Let $t_n$ be the $n$-th term, so $t_n=t_{n-1}+t_{n-2}+t_{n-3}$ for $n\ge4$. A small time-saver: $t_{n}=2t_{n-1}-t_{n-4}$, since $t_{n-1}=t_{n-2}+t_{n-3}+t_{n-4}$. Either way,
\[
1,\ 2,\ 3,\ 6,\ 11,\ 20,\ 37,\ 68,\ 125,\ 230,\ 423,
\]
so the $11$th term is $\boxed{423}$. (For example $t_{11}=2\cdot230-37=423$.)''',
'Recurrence relations|Sequences and series',2,
note='The poster got 423 by adding; the solution confirms it and gives the shortcut t_n = 2t_(n-1) - t_(n-4).')

# ---------------- 415026 1992 AJHSME 23
b.add(415026,1,r'''If two dice are tossed, the probability that the product of the numbers showing on the tops of the dice is greater than $10$ is
\[
\textbf{(A)}\ \dfrac37\qquad\textbf{(B)}\ \dfrac{17}{36}\qquad\textbf{(C)}\ \dfrac12\qquad\textbf{(D)}\ \dfrac58\qquad\textbf{(E)}\ \dfrac{11}{12}
\]''',
r'''There are $36$ equally likely ordered outcomes. Count the products greater than $10$ by the first die:
\begin{itemize}
\item first die $1$: none; first die $2$: second die $6$ ($1$ outcome);
\item first die $3$: $4,5,6$ ($3$); first die $4$: $3,4,5,6$ ($4$);
\item first die $5$: $3,4,5,6$ ($4$); first die $6$: $2,3,4,5,6$ ($5$).
\end{itemize}
That is $1+3+4+4+5=17$ outcomes, so the probability is $\dfrac{17}{36}$, answer $\boxed{\textbf{(B)}}$.''',
'Dice probability|Probability|Systematic counting',2,source=src('AJHSME',1992,None,23))

# ---------------- 1737416 13-14-15 circumcentre
fig=r'''pair B=(0,0),C=(15,0),A=(8.4,11.2),X=(7.5,3.125);
draw(circle(X,8.125),gray(0.55));
draw(A--B--C--cycle,linewidth(0.9));
draw(B--X--C,blue+linewidth(0.8));
dot(X);
draw(arc(X,1.0,degrees(B-X),degrees(C-X)),blue);
label("$2\angle A$",X+2.15*dir(270),blue);
label("$A$",A,N);label("$B$",B,W);label("$C$",C,E);label("$X$",X,N);
label("$14$",(A+B)/2,NW);label("$13$",(A+C)/2,NE);label("$15$",(B+C)/2,S);'''
b.add(1737416,1,r'''In triangle $ABC$, $AB=14$, $BC=15$ and $AC=13$. Let $X$ be the circumcentre of the triangle. The supplement of $\angle BXC$ is one of the angles of a right triangle with integer side lengths. Find the smallest possible perimeter of this right triangle.''',
r'''By the law of cosines,
\[
\cos A=\dfrac{AB^2+AC^2-BC^2}{2\cdot AB\cdot AC}=\dfrac{196+169-225}{364}=\dfrac{5}{13},\qquad \sin A=\dfrac{12}{13}.
\]
Angle $A$ is acute, so the circumcentre $X$ lies on the same side of $BC$ as $A$, and the central angle is $\angle BXC=2\angle A$:
'''+asy(fig,'6cm')+r'''
Let $\theta=180^\circ-2A$ be its supplement. Then
\[
\cos\theta=-\cos2A=1-2\cos^2A=\dfrac{119}{169},\qquad \sin\theta=\sin2A=2\cdot\dfrac{12}{13}\cdot\dfrac5{13}=\dfrac{120}{169}.
\]
In a right triangle with an acute angle $\theta$, the adjacent leg, opposite leg and hypotenuse are in the ratio $\cos\theta:\sin\theta:1=119:120:169$. Since $\gcd(119,120)=1$, the integer triangles with this angle are the multiples $119k,120k,169k$, and the smallest perimeter is
\[
119+120+169=\boxed{408}.
\]''',
'Circumcircles and circumcentres|Inscribed angles|Law of cosines|Trigonometric identities|Pythagorean triples|Right triangles',5,
note='Solution figure drawn to scale from B=(0,0), C=(15,0), A=(8.4,11.2), circumcentre (7.5,3.125), R=65/8.')

# ---------------- 1737879 gcd with 1 and 0
b.add(1737879,1,r'''Two integers are relatively prime when their greatest common divisor is $1$.
\begin{enumerate}
\item[(a)] Is $1$ relatively prime to $1$?
\item[(b)] Is $1$ relatively prime to $0$?
\end{enumerate}''',
r'''\textbf{(a)} The only positive divisor of $1$ is $1$, so the common positive divisors of $1$ and $1$ are just $1$, and $\gcd(1,1)=1$. So $\boxed{\text{yes}}$, $1$ is relatively prime to $1$.

\textbf{(b)} Every integer divides $0$ (because $0=d\cdot0$), so the common positive divisors of $1$ and $0$ are the positive divisors of $1$, namely just $1$. Thus $\gcd(1,0)=1$ and $\boxed{\text{yes}}$, $1$ and $0$ are relatively prime. (More generally $\gcd(n,0)=|n|$, so $n$ is relatively prime to $0$ only for $n=\pm1$; and $1$ is relatively prime to every integer.)''',
'HCF and LCM|Factors and multiples',1)

b.save()
