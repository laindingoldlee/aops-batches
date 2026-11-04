from qb import *
b=Bank('p231_03')

# ---------------- 1730463 cows
b.add(1730463,1,r'''I have $10$ cows: $3$ are red, $2$ are yellow and $5$ are green. If I choose $2$ of the cows at random, what is the probability that both are green?''',
r'''All $\binom{10}{2}=45$ pairs are equally likely, and $\binom52=10$ of them consist of two green cows. The probability is $\dfrac{10}{45}=\boxed{\dfrac29}$. (Equivalently $\dfrac5{10}\cdot\dfrac49$.)''',
'Probability|Combinations|Sampling without replacement',1,
note='Problem 1 of a cow-problem marathon (only P1 is in the post).')

# ---------------- 1730652 rectangle XY/BD (alias)
b.add(1730652,1,r'''In rectangle $ABCD$, points $E$ and $F$ lie on $DC$ so that $DF=FE=EC$. Segments $AF$ and $AE$ meet diagonal $BD$ at $X$ and $Y$. Find $\dfrac{XY}{BD}$.''',
r'''Triangles $XDF\sim XBA$ with ratio $DF:AB=1:3$ give $DX=\dfrac14DB$; triangles $YDE\sim YBA$ with ratio $2:3$ give $DY=\dfrac25DB$. So $\dfrac{XY}{BD}=\dfrac25-\dfrac14=\boxed{\dfrac{3}{20}}$.''',
'Rectangles|Similarity',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1730101 tilted parabola
fig=r'''import graph;
real f=sqrt(2)/2;
pair V=(0.5,0.5),u=dir(45),w=dir(135);
pair g(real t){return V+(t^2/(4*f))*u+t*w;}
draw((-3.2,0)--(4.2,0),Arrow(6));draw((0,-3.2)--(0,4.2),Arrow(6));
label("$x$",(4.2,0),SE);label("$y$",(0,4.2),NW);
draw((-2.8,2.8)--(2.8,-2.8),dashed+blue);
draw(graph(g,-3.1,3.1),linewidth(0.9)+red);
pair F=(1,1);dot(F);label("$F(1,1)$",F,SE);
label("$x+y=0$",(2.3,-2.3),NE,blue);'''
b.add(1730101,1,r'''A parabola is the set of points equidistant from a fixed point (the focus) and a fixed line (the directrix) not through the focus. Its axis need not be vertical or horizontal.
\begin{enumerate}
\item[(a)] Find an equation of the parabola with focus $F=(1,1)$ and directrix $x+y=0$.
\item[(b)] Prove that every parabola has an equation of the form $Ax^2+Bxy+Cy^2+Dx+Ey+G=0$ with $A,B,C$ not all zero and $B^2=4AC$.
\end{enumerate}''',
r'''\textbf{(a)} The distance from $(x,y)$ to the line $x+y=0$ is $\dfrac{|x+y|}{\sqrt2}$. Equating squared distances,
\[
(x-1)^2+(y-1)^2=\dfrac{(x+y)^2}{2}\iff2x^2-4x+2+2y^2-4y+2=x^2+2xy+y^2,
\]
so the parabola is $\boxed{x^2-2xy+y^2-4x-4y+4=0}$. Its axis is the line $y=x$ and its vertex is $\left(\dfrac12,\dfrac12\right)$, halfway between $F$ and the foot $(0,0)$ of the perpendicular from $F$ to the directrix.
'''+asy(fig,'6cm')+r'''
\textbf{(b)} Write the directrix as $ux+vy+w=0$ with $u^2+v^2=1$ (divide any equation of the line by $\sqrt{u^2+v^2}$), and let the focus be $(p,q)$. The distance from $(x,y)$ to the line is $|ux+vy+w|$, so the parabola is
\[
(x-p)^2+(y-q)^2=(ux+vy+w)^2 .
\]
Its quadratic part is
\[
x^2+y^2-(ux+vy)^2=\left(1-u^2\right)x^2-2uv\,xy+\left(1-v^2\right)y^2=v^2x^2-2uv\,xy+u^2y^2=(vx-uy)^2 .
\]
So $A=v^2$, $B=-2uv$, $C=u^2$ (not all zero since $u^2+v^2=1$), and $B^2-4AC=4u^2v^2-4u^2v^2=0$. $\blacksquare$

In (a), $A=1$, $B=-2$, $C=1$ and indeed $B^2=4AC$. The equation of a given parabola is unique only up to multiplying it by a nonzero constant; a tilted parabola has an $xy$ term, and rotating the axes by the angle of its axis removes that term and gives the familiar form $Y=kX^2$.''',
'Parabolas|Conic sections|Coordinate geometry|Distance formula',4,
note='The post asks in general what the equation of a tilted parabola is and whether there are several; turned into a concrete example and a proof that every parabola is a conic with B^2 = 4AC.')

# ---------------- 1730306 brackets in 1-1-...-1
b.add(1730306,1,r'''How many different values can be obtained by placing brackets in the expression
\[
1-1-1-\cdots-1\qquad(2000\text{ ones})?
\]
$\textbf{(A)}\ 2000\qquad\textbf{(B)}\ 1999\qquad\textbf{(C)}\ 2001\qquad\textbf{(D)}\ 4000\qquad\textbf{(E)}\ 4001$''',
r'''Write the expression as $a_1-a_2-\cdots-a_n$ with $n=2000$ (all $a_i=1$). After brackets are placed and removed, the value is $\sum\varepsilon_ia_i$ with signs $\varepsilon_i=\pm1$.

\textbf{$\varepsilon_1=+1$ and $\varepsilon_2=-1$ always.} A bracketed expression of at least two terms has the form $L-R$, where $L$ contains $a_1,\dots,a_k$ and $R$ contains $a_{k+1},\dots,a_n$. By induction on the length, the first term of any bracketed expression has sign $+$. If $k=1$, then $a_2$ is the first term of $R$, has sign $+$ in $R$ and so $-$ overall; if $k\ge2$, then by induction $a_2$ has sign $-$ in $L$, which enters with $+$.

\textbf{Every sign pattern for $a_3,\dots,a_n$ occurs.} Split $a_2,\dots,a_n$ into consecutive blocks, starting a new block at $a_2$ and at every $a_i$ ($i\ge3$) that should get a minus sign, and write
\[
a_1-(a_2-a_{i_1}-\cdots)-(a_j-\cdots)-\cdots .
\]
Inside a block $(a_j-a_{j+1}-\cdots-a_l)$ the first term gets $-$ overall and the others $+$. So exactly the block starts get $-$.

Therefore the possible values are $1-1+\sum_{i=3}^{2000}\varepsilon_i$ with arbitrary $\varepsilon_i=\pm1$: a sum of $1998$ terms $\pm1$, which takes exactly the values $-1998,-1996,\dots,1996,1998$. That is $1999$ values, answer $\boxed{\textbf{(B)}\ 1999}$.''',
'Mathematical induction|Construction|Parity|Algebraic expressions and identities',4,
note='Checked by enumerating all bracketings for up to 12 ones (n ones give n - 1 values).')

# ---------------- 1268207 lockers (alias)
b.add(1268207,1,r'''There are $100$ lockers, all closed, and $100$ keys. The first key opens every locker; the second key changes the state of every second locker (opening it if closed, closing it if open); the third key changes the state of every third locker; and so on. Which lockers are open after all the keys have been used?''',
r'''Locker $k$ is changed once for each divisor of $k$, and is open at the end exactly when $k$ has an odd number of divisors, i.e.\ when $k$ is a perfect square. The open lockers are $\boxed{1,4,9,16,25,36,49,64,81,100}$.''',
'Divisor counting|Perfect squares',2,
note='Repeat of an earlier record (aliased). P1 of a logic marathon.')

# ---------------- 1729694 remainders 1; Frobenius 7, 11
b.add(1729694,1,r'''Adam chooses a three-digit number. It leaves a remainder of $1$ when divided by $2$, a remainder of $1$ when divided by $3$, and a remainder of $1$ when divided by $4$. What is the largest possible value of Adam's number?''',
r'''$N-1$ is divisible by $2$, $3$ and $4$, hence by $\operatorname{lcm}(2,3,4)=12$. So $N=12k+1$. The largest three-digit such number: $999=12\cdot83+3$, so $12\cdot83+1=\boxed{997}$.''',
'HCF and LCM|Remainders and congruences',2)
b.add(1729694,2,r'''Using only $7$s and $11$s (any number of each), what is the greatest whole number that cannot be written as a sum?''',
r'''By the Chicken McNugget theorem the answer is $7\cdot11-7-11=\boxed{59}$.''',
'Linear Diophantine equations|Remainders and congruences',3,
note='Repeat of an earlier record (aliased). The poster thought the answer would be infinite.')

# ---------------- 1730054 standard deviation
b.add(1730054,1,r'''Students recorded the temperature on each of the five weekdays. The (population) standard deviation of the five temperatures was $2$ degrees and their mean was $60$ degrees. What is the maximum temperature they could have recorded during the week? Explain why the answer is not $62$ degrees.''',
r'''Let the deviations from the mean be $d_1,\dots,d_5$. Then $\sum d_i=0$ and the variance is $\dfrac15\sum d_i^2=2^2=4$, so $\sum d_i^2=20$.

Suppose $d_1=d$ is the largest. The other four deviations sum to $-d$, and their squares sum to at least $4\left(\dfrac{d}{4}\right)^2=\dfrac{d^2}{4}$ (by QM-AM, with equality when they are equal). So
\[
20=\sum d_i^2\ge d^2+\dfrac{d^2}{4}=\dfrac{5d^2}{4},\qquad d^2\le16,\qquad d\le4 .
\]
The value $d=4$ occurs for the temperatures $64,59,59,59,59$: mean $60$ and $\dfrac{16+4\cdot1}{5}=4$. So the maximum is $\boxed{64}$ degrees.

$62$ is wrong because the standard deviation is not the largest possible distance from the mean: it is the root-mean-square of all five deviations. One large deviation can be balanced by four small ones: in the extreme case $64,59,59,59,59$ one value is $4$ degrees above the mean while the standard deviation is still exactly $2$.''',
'Mean|Inequalities|Bounding and extremal cases',4,
note='Population standard deviation is used (with the sample standard deviation, sum of squared deviations 16, the maximum would be 60 + 8/sqrt5, about 63.58). The answer 64 matches the post\'s key.')

# ---------------- 1729919 fractional part sqrt(123456789)
b.add(1729919,1,r'''Find the positive integer $n$ such that $\dfrac1n$ is closest to $\left\{\sqrt{123456789}\right\}$, where $\{x\}$ denotes the fractional part $x-\lfloor x\rfloor$.''',
r'''Note $11111^2=123454321$ and $123456789-123454321=2468$. Write $\sqrt{123456789}=11111+\delta$ with $0<\delta<1$ (as $11112^2=123476544$ is larger). Then
\[
22222\delta+\delta^2=2468,\qquad\delta=\dfrac{2468}{22222+\delta},
\]
so $\dfrac{2468}{22223}<\delta<\dfrac{2468}{22222}$, i.e.\ $0.111056<\delta<0.111062$. Hence $\{\sqrt{123456789}\}=\delta$ is within $0.00006$ of $\dfrac19=0.11111\ldots$, while the neighbouring values $\dfrac18=0.125$ and $\dfrac1{10}=0.1$ are more than $0.01$ away (and other $\dfrac1n$ are farther still). So $n=\boxed{9}$.''',
'Radicals|Floor and ceiling functions|Estimation|Decimals',3,
note='Checked with 50-digit arithmetic: the fractional part is 0.1110605555...')

# ---------------- 1729780 nearest integer = ceiling
b.add(1729780,1,r'''For a real number $x$ let $[x]$ denote the integer nearest to $x$ (for example $[5]=5$, $[5.3]=5$, $[6.7]=7$), and let $\lceil x\rceil$ denote the least integer greater than or equal to $x$. How many positive integers $n<100$ satisfy $\left[\dfrac n7\right]=\left\lceil\dfrac n7\right\rceil$?''',
r'''Write $n=7q+r$ with $0\le r\le6$. If $r=0$, both sides equal $q$. If $r\ge1$, then $\left\lceil\dfrac n7\right\rceil=q+1$, while $\left[\dfrac n7\right]=q+1$ exactly when $\dfrac r7>\dfrac12$, i.e.\ $r\in\{4,5,6\}$ (no tie occurs since $\dfrac r7\ne\dfrac12$). So we count $1\le n\le99$ with $n\equiv0,4,5,6\pmod7$:
\begin{itemize}
\item $r=0$: $7,14,\dots,98$: $14$ numbers;
\item $r=4$: $4,11,\dots,95$: $14$; $r=5$: $5,\dots,96$: $14$; $r=6$: $6,\dots,97$: $14$.
\end{itemize}
The answer is $14\cdot4=\boxed{56}$.''',
'Floor and ceiling functions|Remainders and congruences|Systematic counting',2,
note='"n in N" read as positive integers (with n = 0 included the count would be 57). The post calls [x] the "closest positive integer"; read as the nearest integer.')

# ---------------- 1729473 three-digit, 7 | n, n = 2 mod 17
b.add(1729473,1,r'''How many three-digit numbers are divisible by $7$ and leave a remainder of $2$ when divided by $17$?''',
r'''Write $n=17k+2$. Then $7\mid n$ means $17k+2\equiv3k+2\equiv0\pmod7$, i.e.\ $3k\equiv5\pmod7$; multiplying by $5$ (as $3\cdot5\equiv1$) gives $k\equiv25\equiv4\pmod7$. So $k=4$ gives $n=70$, and all solutions are $n\equiv70\pmod{119}$ ($119=7\cdot17$). The three-digit ones are
\[
189,\ 308,\ 427,\ 546,\ 665,\ 784,\ 903,
\]
since $70+8\cdot119=1022$ is too large. There are $\boxed{7}$.''',
'Chinese remainder theorem|Remainders and congruences|Divisibility',3)

# ---------------- 1729478 rationals between 1/4 and 1/2
b.add(1729478,1,r'''Find five rational numbers between $\dfrac14$ and $\dfrac12$ by multiplying the numerator and the denominator of each fraction by a suitable number (not by taking averages).''',
r'''Use the common denominator $24$: multiply numerator and denominator of $\dfrac14$ by $6$ and of $\dfrac12$ by $12$:
\[
\dfrac14=\dfrac6{24},\qquad\dfrac12=\dfrac{12}{24}.
\]
The fractions with numerators $7,8,9,10,11$ lie strictly between them:
\[
\boxed{\dfrac7{24},\ \dfrac8{24}=\dfrac13,\ \dfrac9{24}=\dfrac38,\ \dfrac{10}{24}=\dfrac5{12},\ \dfrac{11}{24}}.
\]
(Any denominator giving at least five integers strictly between the numerators works, e.g.\ $\dfrac{3}{12}$ and $\dfrac{6}{12}$ give only two, so a larger multiplier such as $6$ is needed.)''',
'Fractions',1)

# ---------------- 1729495 arrangements of 7 digits
b.add(1729495,1,r'''Seven different digits are chosen from $0,1,2,\dots,9$.
\begin{enumerate}
\item[(a)] How many ordered arrangements (rows of seven different digits) are possible?
\item[(b)] How many different groups of seven digits (order not mattering) are possible?
\end{enumerate}''',
r'''\textbf{(a)} The first digit can be chosen in $10$ ways, the second in $9$, and so on down to $4$ for the seventh:
\[
10\cdot9\cdot8\cdot7\cdot6\cdot5\cdot4=\dfrac{10!}{3!}=\boxed{604800}.
\]
\textbf{(b)} Each group of seven digits is arranged in $7!=5040$ orders, so the number of groups is $\dfrac{604800}{5040}=\binom{10}{7}=\boxed{120}$.''',
'Permutations|Combinations',1,
note='"Arrange the numbers 0-9 in groups of seven" is ambiguous; the record asks for both ordered arrangements and unordered groups (digits not repeated).')

# ---------------- 1728894 semicircles tangent line LM
qf=r'''pair O=(0,0),P=(-4,0),Q=(6,0);
pair nn=(1,sqrt(24))/5;
pair L=P+6*nn,M=Q+4*nn;
draw(arc(O,10,0,180),linewidth(0.9));draw(arc(P,6,0,180),linewidth(0.8));draw(arc(Q,4,0,180),linewidth(0.8));
draw((-10,0)--(10,0),linewidth(0.9));
draw(L+0.25*(L-M)--M+0.4*(M-L),linewidth(0.8));
dot(P);dot(Q);dot(L);dot(M);
label("$P$",P,S);label("$Q$",Q,S);label("$L$",L,N);label("$M$",M,NE);'''
sf=r'''pair O=(0,0),P=(-4,0),Q=(6,0);
pair nn=(1,sqrt(24))/5;
pair L=P+6*nn,M=Q+4*nn,H=P+4*nn;
draw(arc(O,10,0,180),gray);draw(arc(P,6,0,180),linewidth(0.8));draw(arc(Q,4,0,180),linewidth(0.8));
draw((-10,0)--(10,0),linewidth(0.9));
draw(L--M,linewidth(0.9));
draw(P--L,blue);draw(Q--M,blue);draw(H--Q,dashed+red);
draw(M+0.5*unit(L-M)--M+0.5*unit(L-M)+0.5*unit(P-L)--M+0.5*unit(P-L));
draw(L+0.5*unit(M-L)--L+0.5*unit(M-L)+0.5*unit(P-L)--L+0.5*unit(P-L));
dot(P);dot(Q);dot(L);dot(M);dot(H);
label("$P$",P,S);label("$Q$",Q,S);label("$L$",L,N);label("$M$",M,NE);label("$H$",H,W);
label("$4$",(Q+M)/2,E,blue);label("$4$",(P+H)/2,W,blue);label("$2$",(H+L)/2,W,blue);
label("$10$",(-1.6,0),S);'''
b.add(1728894,1,r'''Two semicircles with centres $P$ and $Q$ and radii $6$ and $4$ stand on the diameter of a large semicircle. They are tangent to each other and to the large semicircle. A line is tangent to semicircle $P$ at $L$ and to semicircle $Q$ at $M$, as shown.
'''+asy(qf,'6.5cm')+r'''
Find $LM$.''',
r'''The two small semicircles touch each other, so $PQ=6+4=10$ (and they fit exactly in a large semicircle of radius $10$). The radii $PL$ and $QM$ are perpendicular to the tangent line $LM$, so they are parallel. Let $H$ be the point on $PL$ with $PH=QM=4$; then $HLMQ$ is a rectangle, so $HQ=LM$, $HL=6-4=2$, and triangle $PHQ$ has a right angle at $H$.
'''+asy(sf,'6.5cm')+r'''
By the Pythagorean theorem,
\[
LM=HQ=\sqrt{PQ^2-PH^2}=\sqrt{10^2-2^2}=\sqrt{96}=\boxed{4\sqrt6}.
\]''',
'Tangents|Tangent circles|Circles|Pythagorean theorem|Rectangles',3,
note='The poster could not draw the figure; it is rebuilt from the text, with L and M read as the points of tangency (the usual reading; the large semicircle then has radius 10 and is not needed for LM).')

# ---------------- 1726523 2016^(2015^2014) mod 11
b.add(1726523,1,r'''Find the remainder when $2016^{2015^{2014}}$ is divided by $11$, where $a^{b^c}$ means $a^{\left(b^c\right)}$.''',
r'''Since $2016=11\cdot183+3$, we need $3^{2015^{2014}}\bmod11$. Now $3^5=243=22\cdot11+1\equiv1\pmod{11}$, so powers of $3$ modulo $11$ repeat with period $5$. The exponent $2015^{2014}$ is a multiple of $5$ (as $5\mid2015$), so
\[
2016^{2015^{2014}}\equiv3^{5m}=\left(3^5\right)^m\equiv1\pmod{11}.
\]
The remainder is $\boxed{1}$.''',
'Modular exponentiation|Multiplicative order|Remainders and congruences',3)

# ---------------- 1726545 tetrahedron spider (alias)
b.add(1726545,1,r'''I stand at one vertex of a regular tetrahedron and a spider stands at another. Every minute we both move simultaneously, each to one of the other three vertices chosen uniformly at random and independently. We meet when we arrive at the same vertex. What is the expected number of minutes until we meet?''',
r'''From any two different vertices, we meet at the next step with probability $\dfrac29$ (we must both go to one of the two other vertices, the same one). So the waiting time is geometric with mean $\boxed{\dfrac92}$ minutes.''',
'Expected value|Random walks|Geometric distribution',4,
note='Repeat of an earlier record (aliased).')

# ---------------- 1729010 digit sum
b.add(1729010,1,r'''Find the sum of the digits of $10^{1000}-7982$.''',
r'''Since $10^{1000}-7982=\left(10^{1000}-10^4\right)+\left(10^4-7982\right)$, and $10^{1000}-10^4$ is the number formed by $996$ nines followed by four zeros, while $10^4-7982=2018$, the number is $996$ nines followed by the digits $2,0,1,8$. Its digit sum is
\[
996\cdot9+2+0+1+8=8964+11=\boxed{8975}.
\]''',
'Digits and bases|Place value|Exponents',2)

# ---------------- 1635216 Pythagorean theorem (alias)
b.add(1635216,1,r'''Prove the Pythagorean theorem: a right triangle with legs $a,b$ and hypotenuse $c$ satisfies $a^2+b^2=c^2$.''',
r'''Place four copies of the triangle in a square of side $a+b$, leaving a central square of side $c$. Comparing areas, $(a+b)^2=4\cdot\dfrac{ab}{2}+c^2$, so $a^2+b^2=c^2$. $\blacksquare$''',
'Right triangles|Pythagorean theorem|Area decomposition',2,
note='Repeat of an earlier record (aliased). The post asks for the hardest and easiest proofs.')

# ---------------- 1728999 year = months worked
b.add(1728999,1,r'''Bob starts a business at the beginning of $2018$. In what year will the year number equal the number of months he has worked? (For example, at the beginning of $2020$ he has worked $24$ months.)''',
r'''At the beginning of year $Y$ he has worked $12(Y-2018)$ months, and during year $Y$ the number of completed months runs through $12(Y-2018),\dots,12(Y-2018)+11$. We need
\[
12(Y-2018)\le Y\le12(Y-2018)+11 .
\]
The left inequality gives $11Y\le24216$, $Y\le2201.4\ldots$; the right gives $11Y\ge24205$, $Y\ge2200.4\ldots$. So $Y=\boxed{2201}$. Indeed at the beginning of $2201$ he has worked $12\cdot183=2196$ months, and after $5$ more months (at the beginning of June $2201$) the count is $2201$.''',
'Linear equations|Inequalities|Date and time',3,
note='The equation 12(Y - 2018) = Y has no integer solution; read as the year during which the count of completed months equals the year number (start at the beginning of 2018).')

# ---------------- 1726530 death eater (alias)
b.add(1726530,1,r'''A death eater arrives on Cherrison Street at a uniformly random time between 5:45 PM and 6:30 PM and stays exactly $5$ minutes. I pass through the street at a single, uniformly random instant between 6:00 PM and 7:00 PM, independently. If he sees me, he devours my soul with probability $50\%$, and if my soul is devoured I die with probability $90\%$. What is the probability that I survive?''',
r'''With times in minutes after 6:00, $P(\text{seen})=\dfrac{30\cdot5+\dfrac12\cdot5\cdot5}{45\cdot60}=\dfrac{13}{216}$, so $P(\text{die})=\dfrac{13}{216}\cdot\dfrac12\cdot\dfrac{9}{10}=\dfrac{13}{480}$ and $P(\text{survive})=\boxed{\dfrac{467}{480}}$.''',
'Geometric probability|Independent events|Complementary probability',4,
note='Repeat of an earlier record (aliased).')

# ---------------- 1728477 pigeonhole on an interval
b.add(1728477,1,r'''Let $n\ge2$ and let $a_1,a_2,\dots,a_n$ be real numbers with $0\le a_k\le S$ for every $k$. Prove that there exist indices $i\ne j$ with
\[
|a_i-a_j|\le\dfrac{S}{n-1}.
\]''',
r'''Relabel the numbers in increasing order: $b_1\le b_2\le\cdots\le b_n$. The $n-1$ gaps $b_{k+1}-b_k\ge0$ add up to
\[
(b_2-b_1)+(b_3-b_2)+\cdots+(b_n-b_{n-1})=b_n-b_1\le S-0=S .
\]
If every gap were greater than $\dfrac{S}{n-1}$, their sum would exceed $S$. So some gap satisfies $b_{k+1}-b_k\le\dfrac{S}{n-1}$, and the two numbers $b_k$, $b_{k+1}$ come from different indices $i\ne j$. $\blacksquare$ (The bound is sharp: $a_k=\dfrac{(k-1)S}{n-1}$ has all gaps equal to $\dfrac{S}{n-1}$.)''',
'Pigeonhole principle|Inequalities|Extremal principle',3,
note='The post (in mixed language: "prove existe i,j") is read with i different from j and n at least 2.')

# ---------------- 1727878 BF:FG
fig=r'''pair B=(0,0),A=(1.8,7),C=(7,0);
pair Ep=(3*B+A)/4,D=(4*C+B)/5,F=(Ep+5*D)/6,G=extension(B,F,A,C);
draw(A--B--C--cycle,linewidth(0.9));
draw(Ep--D,linewidth(0.8));draw(B--G,blue+linewidth(0.8));
dot(Ep);dot(D);dot(F);dot(G);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);
label("$E$",Ep,W);label("$D$",D,S);label("$F$",F,dir(80));label("$G$",G,NE);'''
b.add(1727878,1,r'''In triangle $ABC$, point $E$ lies on $AB$ with $AE:EB=3:1$, point $D$ lies on $BC$ with $BD:DC=4:1$, and point $F$ lies on $ED$ with $EF:FD=5:1$. Line $BF$ meets $AC$ at $G$. Find $BF:FG$.''',
r'''Use vectors with origin $B$, writing $\vec A$ and $\vec C$ for the position vectors of $A$ and $C$. Then
\[
\vec E=\dfrac14\vec A,\qquad\vec D=\dfrac45\vec C,\qquad\vec F=\dfrac16\vec E+\dfrac56\vec D=\dfrac1{24}\vec A+\dfrac23\vec C .
\]
'''+asy(fig,'6.5cm')+r'''
A point $t\vec F$ on line $BF$ lies on line $AC$ exactly when its coefficients of $\vec A$ and $\vec C$ add up to $1$:
\[
t\left(\dfrac1{24}+\dfrac{16}{24}\right)=1\iff t=\dfrac{24}{17}.
\]
So $\vec G=\dfrac{24}{17}\vec F=\dfrac1{17}\vec A+\dfrac{16}{17}\vec C$ (so $AG:GC=16:1$), and $BG=\dfrac{24}{17}BF$. Hence $FG=\dfrac7{17}BF$ and
\[
BF:FG=\boxed{17:7}.
\]
The problem is consistent. The poster's mass points ($A=1$, $B=3$, $C=12$) balance $E$ and $D$, and they locate the point where $ED$ meets the cevian from $B$ to the point $G_0$ with $AG_0:G_0C=12:1$, giving $15:4$ on $ED$. That point is not $F$ (since $15:4\ne5:1$), so $G\ne G_0$ and those masses do not apply to line $BG$.''',
'Triangles|Vectors|Mass points|Ratios, proportions, and variation',4,
note='The poster asks whether the question is wrong because mass points give EF:FD = 15:4; it is not (G is defined by F, not by concurrent cevians). Answer 17:7 checked with coordinates.')

# ---------------- 1728427 a^2+ab+b^2
b.add(1728427,1,r'''Can $a^2+ab+b^2$ be factored into two linear factors with real coefficients? Prove your answer, and factor it over the complex numbers.''',
r'''\textbf{No real factorisation.} Suppose $a^2+ab+b^2=(pa+qb)(ra+sb)$ with real $p,q,r,s$. Comparing the coefficients of $a^2$, $pr=1$, so $p\ne0$. Put $a=-\dfrac qp$, $b=1$: the right side is $0$, so $t=-\dfrac qp$ is a real root of $t^2+t+1=0$. But $t^2+t+1=\left(t+\dfrac12\right)^2+\dfrac34>0$ for all real $t$. Contradiction. (Equivalently, $a^2+ab+b^2=\left(a+\dfrac b2\right)^2+\dfrac34b^2$ is zero only for $a=b=0$, while a product of two real linear forms vanishes on a whole line.)

\textbf{Over the complex numbers.} The roots of $t^2+t+1=0$ are $\omega=\dfrac{-1+i\sqrt3}{2}$ and $\bar\omega=\dfrac{-1-i\sqrt3}{2}$, with $\omega+\bar\omega=-1$ and $\omega\bar\omega=1$. Hence
\[
\boxed{a^2+ab+b^2=(a-\omega b)(a-\bar\omega b)=\left(a+\dfrac{1-i\sqrt3}{2}b\right)\left(a+\dfrac{1+i\sqrt3}{2}b\right)},
\]
since the product is $a^2-(\omega+\bar\omega)ab+\omega\bar\omega b^2$. Useful related forms over the reals are $a^2+ab+b^2=(a+b)^2-ab$ and $a^3-b^3=(a-b)\left(a^2+ab+b^2\right)$.''',
'Factoring|Complex numbers|Quadratic equations|Sum and difference of cubes',3,
note='The post asks how to factorise a^2 + b^2 + ab; it does not factor over the reals, so the record asks to prove this and to factor over C.')

# ---------------- 1727717 AoPS edition problems
b.add(1727717,1,r'''Find the number of permutations of the letters of the word AOPS.''',
r'''The four letters are different, so there are $4!=\boxed{24}$ permutations.''',
'Permutations',1,
note='Repeat of an earlier record (aliased).')
b.add(1727717,2,r'''If $a+o+p=3$, $a+o+s=-15$, $a+p+s=1$ and $o+p+s=17$, what is the product $aops$?''',
r'''Adding all four equations, each variable appears three times: $3(a+o+p+s)=6$, so $a+o+p+s=2$. Subtracting each equation from this:
\[
s=2-3=-1,\quad p=2-(-15)=17,\quad o=2-1=1,\quad a=2-17=-15 .
\]
So $aops=(-15)\cdot1\cdot17\cdot(-1)=\boxed{255}$.''',
'Systems of linear equations|Symmetry',2)
b.add(1727717,3,r'''Richard has $100$ posts on a forum website: $15$ on Middle School Math, $10$ on High School Math, $5$ on Contests and Programs, $35$ on Fun Factory and $35$ on Accumulation Playoffs. Only the posts in the first three forums count as ``official''. Three different posts are selected at random. What is the probability that the three posts are in three different forums and are all official?''',
r'''All $\binom{100}{3}=161700$ sets of three posts are equally likely. Three official posts in three different forums must be one from each of the three official forums: $15\cdot10\cdot5=750$ sets. The probability is
\[
\dfrac{750}{161700}=\boxed{\dfrac{5}{1078}}.
\]''',
'Probability|Combinations|Sampling without replacement',2)
b.add(1727717,4,r'''A default avatar uses $3$ distinct colours chosen from $16$ colours, and red and blue cannot both be used. Avatars with the same set of colours count as the same, whatever their arrangement. How many default avatars are possible?''',
r'''There are $\binom{16}{3}=560$ sets of three colours, of which $\binom{14}{1}=14$ contain both red and blue. So there are $560-14=\boxed{546}$ avatars.''',
'Combinations|Complementary counting',2)
b.add(1727717,5,r'''The letters A, O, P and S are placed on four different vertices of a cube. How many different arrangements are possible if arrangements that differ by a rotation of the cube are considered the same?''',
r'''There are $8\cdot7\cdot6\cdot5=1680$ placements. The cube has $24$ rotations. A rotation other than the identity fixes at most $2$ vertices (a rotation about an axis through two opposite vertices fixes those two; the other rotations fix none), so it cannot fix a placement, which needs four vertices to stay in place. Hence each placement has exactly $24$ different images, the placements fall into classes of $24$, and the number of different arrangements is $\dfrac{1680}{24}=\boxed{70}$.''',
'Symmetry|Permutations|Burnside\'s lemma',4,
note='Checked by computing orbits under the 24 rotations.')
b.add(1727717,6,r'''Three people log in to a website at independent, uniformly random times between 9 pm and 11 pm. Each stays online for exactly $30$ minutes and then logs out. Find the probability that at least two of the three people are online at the same time.''',
r'''Measure times in minutes after 9 pm, so the log-in times are uniform on $[0,120]$. Two people are online together exactly when their log-in times differ by less than $30$. We find the probability that no two overlap.

Order the log-in times $y_1\le y_2\le y_3$ (each ordering of the people is equally likely and the ordered triple is uniform on $\{0\le y_1\le y_2\le y_3\le120\}$, of volume $\dfrac{120^3}{6}$). No overlap means $y_2\ge y_1+30$ and $y_3\ge y_2+30$. With $z_1=y_1$, $z_2=y_2-30$, $z_3=y_3-60$ this becomes $0\le z_1\le z_2\le z_3\le60$, a region of volume $\dfrac{60^3}{6}$ (the substitution is a translation, so volume is preserved). Hence
\[
P(\text{no overlap})=\dfrac{60^3}{120^3}=\dfrac18,\qquad P(\text{some two overlap})=\boxed{\dfrac78}.
\]''',
'Geometric probability|Complementary probability|Probability',4,
note='Checked by Monte Carlo simulation.')

# ---------------- 1728425 k^7/7 + k^5/5 + 2k^3/3 - k/105
b.add(1728425,1,r'''Prove that
\[
\dfrac{k^7}{7}+\dfrac{k^5}{5}+\dfrac{2k^3}{3}-\dfrac{k}{105}
\]
is a positive integer for every positive integer $k$.''',
r'''Since $\dfrac17+\dfrac15+\dfrac23=\dfrac{15+21+70}{105}=\dfrac{106}{105}$, we can rewrite the expression as
\[
\dfrac{k^7-k}{7}+\dfrac{k^5-k}{5}+\dfrac{2\left(k^3-k\right)}{3}+k\left(\dfrac{106}{105}-\dfrac1{105}\right)=\dfrac{k^7-k}{7}+\dfrac{k^5-k}{5}+\dfrac{2\left(k^3-k\right)}{3}+k .
\]
By Fermat's little theorem, $p\mid k^p-k$ for every prime $p$ and integer $k$; so $7\mid k^7-k$, $5\mid k^5-k$ and $3\mid k^3-k$. Each term is an integer, hence so is the sum. It is positive because $15k^7\ge15k>k$ gives $\dfrac{k^7}{7}>\dfrac{k}{105}$, and the other two terms are positive. $\blacksquare$

(Instead of Fermat's theorem one can use $k^3-k=(k-1)k(k+1)$, a product of three consecutive integers, and similar factorisations for $5$ and $7$; or induction on $k$, since the difference between the values at $k+1$ and $k$ is an integer polynomial in $k$.)''',
'Fermat\'s little theorem|Divisibility|Remainders and congruences',4,
note='The post titled "Induction" asks how to prove it; the record gives the Fermat argument and mentions induction. Checked for k up to 200.')

b.save()
