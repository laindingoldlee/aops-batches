from qb import *
b=Bank('p233_01')

RA=r'''void ra(pair P,pair Q,pair R,real s){pair u=unit(Q-P),v=unit(R-P);draw(P+s*u--P+s*u+s*v--P+s*v,linewidth(0.5));}
'''

# ---------------- 1722465 math dinner
b.add(1722465,1,r'''At a math dinner there are $15$ possible dishes: $5$ vegetable dishes, $4$ protein dishes, $3$ snacks (one of which is Mentos), $2$ drinks (one of which is Coke) and $1$ ice cream. A meal consists of $4$, $5$ or $6$ different dishes. Each meal must contain at least one vegetable dish and at most two protein dishes, and it may not contain both Coke and Mentos. How many possible meals are there?''',
r'''Call the $6$ snacks, drinks and ice cream ``other'' dishes. For a meal of $k$ dishes, first count the meals with at most two proteins, then remove those with no vegetable, then remove those containing both Coke and Mentos.

\textbf{At most two proteins, at least one vegetable.} With $p\le2$ proteins and the remaining $k-p$ dishes chosen from the $11$ non-protein dishes, there are $\sum_{p=0}^{2}\binom4p\binom{11}{k-p}$ meals; those with no vegetable choose the $k-p$ dishes from the $6$ other dishes only, $\sum_{p=0}^{2}\binom4p\binom{6}{k-p}$. This gives
\[
k=4:\ 1320-185=1135,\qquad k=5:\ 2772-186=2586,\qquad k=6:\ 4290-115=4175 .
\]
For example, for $k=4$: $\binom{11}{4}+4\binom{11}{3}+6\binom{11}{2}=330+660+330=1320$ and $\binom64+4\binom63+6\binom62=15+80+90=185$.

\textbf{Meals with both Coke and Mentos.} Such a meal consists of Coke, Mentos and $k-2$ further dishes chosen from the $13$ remaining dishes ($5$ vegetables, $4$ proteins, $4$ others), still with at least one vegetable and at most two proteins. The same count with $11$ replaced by $9$ and $6$ replaced by $4$ gives
\[
k=4:\ 78-28=50,\qquad k=5:\ 282-52=230,\qquad k=6:\ 678-53=625 .
\]

\textbf{Total.}
\[
(1135-50)+(2586-230)+(4175-625)=1085+2356+3550=\boxed{6991}.
\]''',
'Combinations|Complementary counting|Casework|Counting principles',4,
note='Posted as an unsolved AMC 8 prep problem with no answer. The 15 dishes are read as 5 + 4 + 3 + 2 + 1 (the ice cream is one dish); Coke is one of the drinks and Mentos one of the snacks. Answer checked by brute force over all subsets.')

# ---------------- 1710142 (sqrt2+sqrta)/(sqrt3+sqrtb) rational
b.add(1710142,1,r'''Find all positive integers $a$ and $b$ such that the number
\[
p=\dfrac{\sqrt2+\sqrt a}{\sqrt3+\sqrt b}
\]
is rational.''',
r'''Suppose $p$ is rational; clearly $p>0$. Then $\sqrt2-p\sqrt3=p\sqrt b-\sqrt a$. Squaring both sides,
\[
2+3p^2-2p\sqrt6=p^2b+a-2p\sqrt{ab},
\]
so $2p\left(\sqrt6-\sqrt{ab}\right)=2+3p^2-p^2b-a$ is rational, and therefore $r=\sqrt6-\sqrt{ab}$ is rational.

\textbf{$ab=6$.} From $\sqrt{ab}=\sqrt6-r$, squaring gives $ab=6-2r\sqrt6+r^2$. If $r\ne0$ this would make $\sqrt6$ rational, which it is not. So $r=0$, i.e.\ $ab=6$, and then also $2+3p^2=p^2b+a$.

\textbf{Check the four cases.}
\begin{itemize}
\item $(a,b)=(1,6)$: $p=\dfrac{\sqrt2+1}{\sqrt3+\sqrt6}=\dfrac{\sqrt2+1}{\sqrt3\,(1+\sqrt2)}=\dfrac{1}{\sqrt3}$, irrational.
\item $(a,b)=(2,3)$: $p=\dfrac{2\sqrt2}{2\sqrt3}=\sqrt{\dfrac23}$, irrational.
\item $(a,b)=(3,2)$: $p=\dfrac{\sqrt2+\sqrt3}{\sqrt3+\sqrt2}=1$, rational.
\item $(a,b)=(6,1)$: $p=\dfrac{\sqrt2+\sqrt6}{\sqrt3+1}=\dfrac{\sqrt2\,(1+\sqrt3)}{\sqrt3+1}=\sqrt2$, irrational.
\end{itemize}
Hence the only solution is $\boxed{a=3,\ b=2}$ (with $p=1$).''',
'Radicals|Proof by contradiction|Casework',4,source=src('Junior Regional Olympiad FBH',2017,'Grade 7',5),
note='The necessary condition ab = 6 is not sufficient; each of the four cases is checked.')

# ---------------- 1710127 remainders 11 and 3
b.add(1710127,1,r'''When $19250$ is divided by a certain positive integer, the remainder is $11$. When $20302$ is divided by the same integer, the remainder is $3$. Find this integer.''',
r'''Let the divisor be $d$. Then $d$ divides $19250-11=19239$ and $20302-3=20299$, and $d>11$ (a remainder is smaller than the divisor). The common divisors of $19239$ and $20299$ divide their difference $1060=2^2\cdot5\cdot53$. Since $19239$ is odd and does not end in $0$ or $5$, the common divisors can only be $1$ and $53$; indeed $19239=53\cdot363$ and $20299=53\cdot383$. So $d=\boxed{53}$. Check: $19250=53\cdot363+11$ and $20302=53\cdot383+3$.''',
'Remainders and congruences|HCF and LCM|Divisibility',2,source=src('Junior Regional Olympiad FBH',2017,'Grade 6',4))

# ---------------- 1721702 max product with given sum
b.add(1721702,1,r'''Let $x>0$. We write $x$ as a sum of any number of positive real numbers and multiply those numbers together.
\begin{enumerate}
\item[(a)] Show that if exactly $k$ numbers are used, the largest possible product is $\left(\dfrac xk\right)^k$.
\item[(b)] Show that the largest possible product overall is $\left(\dfrac xk\right)^k$ for $k=\left\lfloor \dfrac xe\right\rfloor$ or $k=\left\lceil\dfrac xe\right\rceil$ (whichever gives the larger value, with $k\ge1$).
\item[(c)] Find the largest possible product when $x=10$.
\end{enumerate}''',
r'''\textbf{(a)} If $a_1+\dots+a_k=x$ with all $a_i>0$, then by AM-GM
\[
a_1a_2\cdots a_k\le\left(\dfrac{a_1+\dots+a_k}{k}\right)^k=\left(\dfrac xk\right)^k ,
\]
with equality when all $a_i=\dfrac xk$. So the maximum with $k$ terms is $\left(\dfrac xk\right)^k$.

\textbf{(b)} It remains to choose the number of terms $k$. Consider $h(t)=\ln\left(\dfrac xt\right)^t=t\ln x-t\ln t$ for real $t>0$. Then $h'(t)=\ln x-\ln t-1$, which is positive for $t<\dfrac xe$ and negative for $t>\dfrac xe$. So $h$ increases up to $t=\dfrac xe$ and decreases afterwards, and among the integers $k\ge1$ the maximum of $\left(\dfrac xk\right)^k$ is attained at the integer just below or just above $\dfrac xe$.

\textbf{(c)} For $x=10$, $\dfrac{10}{e}\approx3.68$. Compare $k=3$ and $k=4$:
\[
\left(\dfrac{10}{3}\right)^3=\dfrac{1000}{27}\approx37.04,\qquad\left(\dfrac{10}{4}\right)^4=\dfrac{625}{16}=39.0625 .
\]
So the largest product is $\boxed{\dfrac{625}{16}}$, from $10=2.5+2.5+2.5+2.5$.''',
'AM-GM inequality|Maxima and minima|Calculus|Exponents',4,
note='The post asks in general for the maximum product of positive reals with sum x; the record states the general answer as parts (a) and (b) and adds the concrete case x = 10 so that there is a definite answer. Values checked numerically.')

# ---------------- 1722254 MMC quadratic
b.add(1722254,1,r'''Consider the quadratic equation $x^2+bx+c=0$, where $b+c=298$. Its two roots $u$ and $v$ are integers with $u<v$, so that $x^2+bx+c=(x-u)(x-v)$. Find the smallest possible value of $v-u$.''',
r'''By Vieta's formulas, $b=-(u+v)$ and $c=uv$. The condition $b+c=298$ becomes
\[
uv-u-v=298\iff(u-1)(v-1)=299=13\cdot23 .
\]
With $u<v$ we have $u-1<v-1$, so $(u-1,v-1)$ is one of $(1,299)$, $(13,23)$, $(-299,-1)$, $(-23,-13)$, giving $v-u=298,10,298,10$. The smallest value is $\boxed{10}$, for example $u=14$, $v=24$: $x^2-38x+336=0$ with $-38+336=298$.''',
"Vieta's formulas|Quadratic equations|Factoring|Diophantine equations",3,source=src('MMC',2015,None,12),
note='Repeat of an earlier record (aliased). The posted statement "(u - v)(u + v) = x2 + bx + c" is a garbling of (x - u)(x - v) = x^2 + bx + c, where u < v are the integer roots; the record states it that way.')

# ---------------- 1720977 jars
b.add(1720977,1,r'''Jar A contains $50$ balls, $15$ green and $35$ red. Jar B also contains $50$ balls, $20$ green and $30$ red. Three balls are chosen at random from jar A and placed in jar B. Jar B is then shaken to mix the balls, and a ball is chosen at random from jar B. What is the probability that it is red?

A student splits into the cases ``$0,1,2,3$ red balls moved'' and uses probabilities such as $\dfrac{65}{100}\cdot\dfrac{30}{103}$. Explain why this does not work.''',
r'''Let $K$ be the number of red balls moved from A to B. Afterwards jar B has $53$ balls, of which $30+K$ are red, so
\[
P(\text{red})=\sum_k P(K=k)\cdot\dfrac{30+k}{53}=\dfrac{30+E[K]}{53}.
\]
Each of the three balls moved is red with probability $\dfrac{35}{50}$, so by linearity of expectation $E[K]=3\cdot\dfrac{35}{50}=2.1$. Hence
\[
P(\text{red})=\dfrac{32.1}{53}=\boxed{\dfrac{321}{530}}.
\]
(Directly: $P(K=k)=\dbinom{35}{k}\dbinom{15}{3-k}\Big/\dbinom{50}{3}$, which is $\dfrac{455}{19600},\dfrac{3675}{19600},\dfrac{8925}{19600},\dfrac{6545}{19600}$ for $k=0,1,2,3$, and $\sum P(K=k)\cdot\dfrac{30+k}{53}=\dfrac{321}{530}$.)

\textbf{The student's errors.} Jar A has $50$ balls, not $100$, and after the transfer jar B has $53$ balls, not $103$; moreover the probability of moving exactly $k$ red balls must count the choices of which of the three balls are red (the hypergeometric probabilities above), not just a product of single draws.''',
'Probability|Conditional probability|Expected value|Sampling without replacement',4,
note='Repeat of an earlier record (aliased); this record also asks for the error in the attempt. The posted attempt (denominators 100 and 103, missing case counts) is wrong; the key answer 321/530 is correct and is derived. Checked with exact fractions.')

# ---------------- 1721820 modular arithmetic bonanza
b.add(1721820,1,r'''What is the units digit of
\[
1^{2^3}+2^{3^4}+3^{4^5}+\dots+2018^{2019^{2020}}\,?
\]
(Here $a^{b^c}$ means $a^{(b^c)}$.)''',
r'''The $k$-th term is $k^{e_k}$ with $e_k=(k+1)^{k+2}$. The units digit of $k^e$ ($e\ge1$) depends only on the units digit of $k$ and on $e$ modulo $4$ (the units digits of powers repeat with period dividing $4$).
\begin{itemize}
\item \textbf{$k$ odd.} Then $k+1$ is even and $k+2\ge3$, so $8\mid e_k$ and $e_k\equiv0\pmod4$. The units digit of $k^{e_k}$ is that of $k^4$: $1,1,5,1,1$ for $k$ ending in $1,3,5,7,9$.
\item \textbf{$k$ even.} Then $k+1$ is odd and $k+2$ is even, so $e_k$ is an odd square and $e_k\equiv1\pmod4$. The units digit of $k^{e_k}$ is that of $k$ itself: $2,4,6,8,0$.
\end{itemize}
So every block of ten consecutive values of $k$ contributes units digits with sum $1+1+5+1+1+2+4+6+8+0=29$. The terms $k=1,\dots,2010$ form $201$ blocks, and $k=2011,\dots,2018$ contribute $1+1+5+1+2+4+6+8=28$. The units digit of the sum is that of $201\cdot29+28=5857$, namely $\boxed{7}$.''',
'Units digits and last digits|Modular exponentiation|Remainders and congruences|Parity',5,
note='Modular Arithmetic Bonanza, round 1, problem 1. Checked by computing every term modulo 10.')
b.add(1721820,2,r'''The number $N$ is formed by writing the integers from $1$ to $2018$ from left to right, with a zero inserted between consecutive integers:
\[
N=102030405060708090100110\cdots020160201702018 .
\]
What is the remainder when $N$ is divided by $36$?''',
r'''Since $36=4\cdot9$, find $N$ modulo $4$ and modulo $9$.

\textbf{Modulo 4.} A number is congruent modulo $4$ to its last two digits, here $18$, so $N\equiv2\pmod4$.

\textbf{Modulo 9.} A number is congruent modulo $9$ to its digit sum. The inserted zeros do not change the digit sum, so the digit sum of $N$ is the total digit sum of $1,2,\dots,2018$, which is congruent modulo $9$ to
\[
1+2+\dots+2018=\dfrac{2018\cdot2019}{2}=1009\cdot2019 .
\]
Here $1009\equiv1$ and $2019\equiv3\pmod9$, so $N\equiv3\pmod9$.

\textbf{Combine.} Among $3,12,21,30$ (the numbers below $36$ that are $\equiv3\pmod9$), only $30$ is $\equiv2\pmod4$. The remainder is $\boxed{30}$.''',
'Remainders and congruences|Divisibility rules|Chinese remainder theorem|Digits and bases',4,
note='Bonanza round 1, problem 2. Checked by computing N mod 36 exactly.')
b.add(1721820,3,r'''What is the sum of the two rightmost digits in the decimal representation of $2018^{2019^{2020}}+2021^{2022^{2023}}$?''',
r'''Work modulo $100$.

\textbf{First term.} Modulo $4$: $2018$ is even and the exponent is at least $2$, so $2018^{2019^{2020}}\equiv0\pmod4$. Modulo $25$: $2018\equiv18$ and $\gcd(18,25)=1$, so by Euler's theorem exponents can be reduced modulo $\varphi(25)=20$. Since $2019\equiv-1\pmod{20}$ and $2020$ is even, $2019^{2020}\equiv1\pmod{20}$, and the term is $\equiv18^1=18\pmod{25}$. The number below $100$ that is $\equiv0\pmod4$ and $\equiv18\pmod{25}$ is $68$.

\textbf{Second term.} $2021\equiv21\pmod{100}$, and by the binomial theorem $21^n=(1+20)^n\equiv1+20n\pmod{100}$, because every later term contains $20^2=400$. So only $n$ modulo $5$ matters, where $n=2022^{2023}\equiv2^{2023}\pmod5$. The powers of $2$ modulo $5$ repeat as $2,4,3,1$, and $2023\equiv3\pmod4$, so $n\equiv3\pmod5$ and the term is $\equiv1+60=61\pmod{100}$.

\textbf{Sum.} $68+61=129\equiv29\pmod{100}$. The two rightmost digits are $2$ and $9$, with sum $\boxed{11}$.''',
"Modular exponentiation|Euler's theorem and totient|Chinese remainder theorem|Units digits and last digits|Binomial theorem",5,
note='Bonanza round 1, problem 3. Checked with Python modular exponentiation.')
b.add(1721820,4,r'''Two students take a $25$-question test on which each correct answer scores $1$ point and every other answer scores $0$, so each score is an integer from $0$ to $25$. The first student scores strictly higher than the second. The sum of their scores leaves remainder $0$ when divided by $9$, and the product of their scores leaves remainder $4$ when divided by $7$. How many ordered pairs of scores (first, second) are possible?''',
r'''Let the scores be $a>b\ge0$ with $a\le25$. Then $a+b=s\in\{9,18,27,36,45\}$ (as $1\le a+b\le49$). Writing $b=s-a$, the condition is $a(s-a)\equiv4\pmod7$, i.e.\ $a^2-sa+4\equiv0\pmod7$. Recall that the squares modulo $7$ are $0,1,2,4$.
\begin{itemize}
\item $s=9\equiv2$: $a^2-2a+4\equiv0$, i.e.\ $(a-1)^2\equiv4$, so $a\equiv3$ or $a\equiv6\pmod 7$, and then $b\equiv6$ or $3$. Among $(9,0),(8,1),(7,2),(6,3),(5,4)$ only $(6,3)$ works.
\item $s=18\equiv4$: $(a-2)^2\equiv0$, so $a\equiv b\equiv2\pmod7$. With $10\le a\le18$: $a=16$, $b=2$.
\item $s=27\equiv6$: $(a-3)^2\equiv5$, impossible since $5$ is not a square modulo $7$.
\item $s=36\equiv1$: multiplying by $4$, $(2a-1)^2\equiv1-16\equiv6$, impossible.
\item $s=45\equiv3$: $(2a-3)^2\equiv9-16\equiv0$, so $a\equiv5\pmod7$; but $a+b=45$ with $b<a\le25$ forces $a\in\{23,24,25\}$, none of which is $\equiv5\pmod7$.
\end{itemize}
So the possible pairs are $(6,3)$ and $(16,2)$: there are $\boxed{2}$.''',
'Remainders and congruences|Quadratic residues|Casework',4,
note='Bonanza round 1, problem 4 (Mock AMC 8 scores), restated without the story; the scoring "all standard rules apply" is read as 25 questions, 1 point each, as in the AMC 8, so scores are 0-25. Checked by brute force.')

# ---------------- 1722305 quadrilateral areas
fig=r'''pair X=(0,0),A=(-2,0),C=(3.75,0),B=4*dir(250),D=(4/3)*dir(70);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--C,linewidth(0.6));draw(B--D,linewidth(0.6));
label("$A$",A,W);label("$B$",B,S);label("$C$",C,E);label("$D$",D,N);label("$X$",X,dir(-40));
label("$8$",(A+B+X)/3);label("$15$",(B+C+X)/3);label("$5$",(C+D+X)/3+(0.15,0));label("$x$",(D+A+X)/3+(-0.1,0.02));
dot(X);'''
b.add(1722305,1,r'''In quadrilateral $ABCD$ the diagonals meet at $X$. Given that $[AXB]=8$, $[BXC]=15$ and $[CXD]=5$, find $[DXA]$. (Here $[PQR]$ denotes the area of triangle $PQR$.)''',
r'''Let $x=[DXA]$. Triangles $AXB$ and $CXB$ have bases $XA$ and $XC$ on line $AC$ and the same apex $B$, so they have the same height and
\[
\dfrac{[AXB]}{[CXB]}=\dfrac{XA}{XC}.
\]
In the same way, triangles $AXD$ and $CXD$ share the apex $D$, so $\dfrac{[AXD]}{[CXD]}=\dfrac{XA}{XC}$. Therefore
\[
\dfrac{x}{5}=\dfrac{8}{15}\quad\Longrightarrow\quad x=\boxed{\dfrac83}.
\]
Equivalently, $[AXB]\cdot[CXD]=[BXC]\cdot[DXA]$.
'''+asy(fig,'5.5cm')+r'''
The figure is drawn to scale with $XA:XC=2:3.75$ and $XB:XD=4:\dfrac43$, which gives the four areas in the ratio $8:15:5:\dfrac83$.''',
'Area ratios|Quadrilaterals and polygons|Diagonals|Triangles',3)

# ---------------- 1709579 integer fraction
b.add(1709579,1,r'''Find all integers $m$ such that $\dfrac{2m^2+7m-9}{m^2+m+1}$ is an integer.''',
r'''Note $m^2+m+1>0$ for every integer $m$. Division gives
\[
\dfrac{2m^2+7m-9}{m^2+m+1}=2+\dfrac{5m-11}{m^2+m+1},
\]
so we need $m^2+m+1\mid 5m-11$. Since $5m-11\ne0$ for integers $m$, this requires $m^2+m+1\le|5m-11|$.
\begin{itemize}
\item $m^2+m+1-(5m-11)=m^2-4m+12=(m-2)^2+8>0$, so $m^2+m+1>5m-11$ always; hence we need $5m-11<0$ and $m^2+m+1\le11-5m$, i.e.\ $m^2+6m-10\le0$, i.e.\ $-3-\sqrt{19}\le m\le-3+\sqrt{19}$. So $-7\le m\le1$.
\end{itemize}
Checking these nine values of $\dfrac{5m-11}{m^2+m+1}$:
\[
m=-7:\ \dfrac{-46}{43},\ \ m=-6:\ \dfrac{-41}{31},\ \ m=-5:\ \dfrac{-36}{21},\ \ m=-4:\ \dfrac{-31}{13},\ \ m=-3:\ \dfrac{-26}{7},
\]
\[
m=-2:\ \dfrac{-21}{3}=-7,\ \ m=-1:\ \dfrac{-16}{1},\ \ m=0:\ \dfrac{-11}{1},\ \ m=1:\ \dfrac{-6}{3}=-2 .
\]
So $m\in\boxed{\{-2,-1,0,1\}}$, giving the values $-5,-14,-9,0$.''',
'Divisibility|Polynomials|Bounding and extremal cases|Inequalities',3,source=src('Junior Regional Olympiad FBH',2018,'Grade 8',2),
note='Checked by search over |m| <= 1000.')

# ---------------- 1709572 compare roots
b.add(1709572,1,r'''Let $a$, $b$ and $m$ be positive real numbers with $a>b$. Which of the numbers $A=\sqrt{a+m}-\sqrt a$ and $B=\sqrt{b+m}-\sqrt b$ is bigger?''',
r'''Multiply and divide by the conjugates:
\[
A=\dfrac{(a+m)-a}{\sqrt{a+m}+\sqrt a}=\dfrac{m}{\sqrt{a+m}+\sqrt a},\qquad B=\dfrac{m}{\sqrt{b+m}+\sqrt b}.
\]
Since $a>b$, we have $\sqrt{a+m}>\sqrt{b+m}$ and $\sqrt a>\sqrt b$, so the denominator of $A$ is larger, while the numerators are equal and positive. Hence $\boxed{B>A}$.''',
'Radicals|Rationalising denominators|Inequalities',2,source=src('Junior Regional Olympiad FBH',2018,'Grade 7',3))

# ---------------- 1709564 altitude half of side
fig=RA+r'''pair A=(0,0),B=(4,0),C=(2,2),H=(2,0);
draw(A--B--C--cycle,linewidth(0.9));draw(C--H,linewidth(0.7));
ra(H,B,C,0.25);
draw(arc(A,0.7,0,45),linewidth(0.6));label("$45^\circ$",A+1.05*dir(22.5));
draw((1,-0.1)--(1,0.1));draw((3,-0.1)--(3,0.1));draw((1.9,1)--(2.1,1));
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,N);label("$H$",H,S);'''
b.add(1709564,1,r'''In triangle $ABC$, the altitude $CH$ (with $H$ on side $AB$) is equal to half of side $AB$. If $\angle BAC=45^\circ$, find $\angle ABC$.''',
r'''In the right triangle $AHC$ the angle at $A$ is $45^\circ$, so it is isosceles: $AH=CH$. Since $CH=\dfrac12AB$, also $AH=\dfrac12AB$, so $H$ is the midpoint of $AB$ and $HB=\dfrac12AB=CH$.
'''+asy(fig,'5cm')+r'''
Then the right triangle $BHC$ is also isosceles ($HB=HC$), so $\angle HBC=45^\circ$. Hence $\angle ABC=\boxed{45^\circ}$ (and $\angle ACB=90^\circ$). The figure marks $AH=HB=HC$.''',
'Right triangles|Isosceles triangles|Altitudes|Angle chasing',2,source=src('Junior Regional Olympiad FBH',2018,'Grade 6',5))

# ---------------- 1709557 last digit powers of 18
b.add(1709557,1,r'''Determine the last digit of $18^1+18^2+\dots+18^{19}+18^{20}$.''',
r'''The last digit of $18^n$ is the last digit of $8^n$, and these repeat with period $4$: $8,4,2,6,8,4,2,6,\dots$. Each block of four consecutive powers contributes last digits with sum $8+4+2+6=20$, which ends in $0$. The twenty powers form $5$ such blocks, so the sum ends in $\boxed{0}$.''',
'Units digits and last digits|Pattern recognition|Exponents',2,source=src('Junior Regional Olympiad FBH',2018,'Grade 6',4))

# ---------------- 1720902 words from ABC
b.add(1720902,1,r'''How many $5$-letter words (arbitrary strings of letters) can be formed using only the letters $A$, $B$ and $C$?''',
r'''Each of the $5$ positions can be filled with any of the $3$ letters independently, so there are $3^5=\boxed{243}$ words.''',
'Multiplication principle|Counting principles',1,
note='"Words" means arbitrary strings; letters may repeat.')

# ---------------- 1721937 tangential right trapezoid
fig=RA+r'''pair A=(0,9),B=(0,0),C=(45,0),D=(5,9),I=(4.5,4.5);
pair T=I+4.5*unit(rotate(90)*(C-D));
draw(A--B--C--D--cycle,linewidth(0.9));
draw(circle(I,4.5),blue+linewidth(0.6));
ra(A,B,D,1.2);ra(B,C,A,1.2);
dot(I);label("$I$",I,S);
label("$A$",A,NW);label("$B$",B,SW);label("$C$",C,SE);label("$D$",D,NE);
label("$9$",(A+B)/2,W);label("$5$",(A+D)/2,N);'''
b.add(1721937,1,r'''In quadrilateral $ABCD$, $\angle A=90^\circ$ and $\angle B=90^\circ$, and the four angle bisectors meet at one point. If $AB=9$ and $AD=5$, what is the length of $BC$?''',
r'''If the four angle bisectors meet at a point $I$, then $I$ is equidistant from all four sides (each bisector is the locus of points equidistant from the two sides of its angle), so the circle with centre $I$ and that radius is tangent to all four sides: $ABCD$ has an incircle. For a quadrilateral with an incircle, the two pairs of opposite sides have equal sums (the tangent lengths from each vertex are equal), so
\[
AB+CD=AD+BC .
\]
Since $\angle A=\angle B=90^\circ$, the sides $AD$ and $BC$ are both perpendicular to $AB$, so $ABCD$ is a right trapezoid with parallel sides $AD$ and $BC$. Let $BC=x$; then $CD=5+x-9=x-4$. Dropping the perpendicular from $D$ to $BC$ gives a right triangle with legs $AB=9$ and $x-5$ and hypotenuse $CD$:
\[
(x-4)^2=81+(x-5)^2\ \Longrightarrow\ -8x+16=81-10x+25\ \Longrightarrow\ x=45 .
\]
So $BC=\boxed{45}$ and $CD=41$ (check: $9^2+40^2=41^2$, and $9+41=5+45$).
'''+asy(fig,'10cm')+r'''
The figure is to scale: the incircle has radius $\dfrac92$ (half the distance $AB$ between the parallel sides) and touches all four sides.''',
'Incircles and incentres|Trapezoids|Angle bisectors|Pythagorean theorem|Tangents',4,
note='Checked numerically: the circle of radius 4.5 centred at (4.5, 4.5) is tangent to CD in the right trapezoid with AB = 9, AD = 5, BC = 45.')

# ---------------- 1721792 rational inequality
b.add(1721792,1,r'''Solve the inequality $\dfrac{2}{x+1}>-1$.

A student adds $1$ to both sides and simplifies to $\dfrac{x+3}{x+1}>0$, and then is stuck. Finish the solution.''',
r'''The student's steps are correct:
\[
\dfrac{2}{x+1}+1>0\iff\dfrac{2+(x+1)}{x+1}>0\iff\dfrac{x+3}{x+1}>0 .
\]
(One must not multiply by $x+1$ directly, because its sign is unknown.) A quotient is positive exactly when numerator and denominator have the same sign.
\begin{itemize}
\item Both positive: $x>-3$ and $x>-1$, i.e.\ $x>-1$.
\item Both negative: $x<-3$ and $x<-1$, i.e.\ $x<-3$.
\end{itemize}
At $x=-3$ the quotient is $0$ (not $>0$), and $x=-1$ is excluded. The solution set is
\[
\boxed{x<-3\ \text{ or }\ x>-1},
\]
i.e.\ $(-\infty,-3)\cup(-1,\infty)$; on a number line, two open rays with open endpoints at $-3$ and $-1$. Check: $x=0$ gives $2>-1$; $x=-2$ gives $-2>-1$, false; $x=-4$ gives $-\dfrac23>-1$, true.''',
'Inequalities|Rational equations|Casework',2,
note='The post asks to "solve and graph"; the graph is described as a number line.')

# ---------------- 1719666 scalene triangles longest side 11
fig=r'''pair A=(0,0),B=(11,0),C=(3.4,5.2);
draw(A--B--C--cycle,linewidth(0.9));
label("$11$",(A+B)/2,S);label("$a$",(A+C)/2,NW);label("$b$",(B+C)/2,NE);'''
b.add(1719666,1,r'''Find the number of non-congruent scalene triangles whose sides all have integer lengths and whose longest side has length $11$.''',
r'''Let the sides be $a<b<11$ (scalene, and $11$ is the longest). The triangle inequality reduces to $a+b>11$ (the other two inequalities hold automatically since $11$ is the longest side).
'''+asy(fig,'4.5cm')+r'''
For each $b$, $a$ runs over $12-b\le a\le b-1$:
\[
b=10:\ a=2,\dots,9\ (8);\quad b=9:\ 3,\dots,8\ (6);\quad b=8:\ 4,\dots,7\ (4);\quad b=7:\ 5,6\ (2);\quad b\le6:\ \text{none}.
\]
Total $8+6+4+2=\boxed{20}$.''',
'Triangle inequality|Systematic counting|Triangles',3)

# ---------------- 1721676 compositions and domains
b.add(1721676,1,r'''Let $f(x)=1-x$ and $g(x)=\dfrac1x$, each with its natural domain. Find $f(f(x))$ and $g(g(x))$ together with their domains. Are $f\circ f$ and $g\circ g$ the same function?''',
r'''$f$ is defined for all real $x$, and $f(f(x))=1-(1-x)=x$ for every real $x$.

$g$ is defined for $x\ne0$, and $g(x)=\dfrac1x$ is never $0$, so $g(g(x))=\dfrac{1}{1/x}$ is defined exactly for $x\ne0$, where it equals $x$.

So both compositions are given by the rule $x\mapsto x$, but $f\circ f$ has domain all real numbers while $g\circ g$ has domain $\{x:x\ne0\}$. Since a function includes its domain, $\boxed{\text{they are not the same function}}$: they agree wherever both are defined, but $f(f(0))=0$ while $g(g(0))$ is undefined.''',
'Functions|Inverse functions',2,
note='The post asks whether f(f(x)) and g(g(x)) are the same function given the domain restriction; made into a question with the answer.')

# ---------------- 1721671 AIME 1995 #5
b.add(1721671,1,r'''For certain real values of $a,b,c$ and $d$, the equation $x^4+ax^3+bx^2+cx+d=0$ has four non-real roots. The product of two of these roots is $13+i$ and the sum of the other two roots is $3+4i$, where $i=\sqrt{-1}$. Find $b$. In your solution, explain why the product of the other two roots must be exactly $13-i$.''',
r'''Because the coefficients are real, the non-real roots come in complex-conjugate pairs: the conjugate of every root is also a root (with the same multiplicity).

Let $z,w$ be the two roots with $zw=13+i$. They are not conjugates of each other, since $z\bar z=|z|^2$ is real and $13+i$ is not. So the conjugates $\bar z$ and $\bar w$ are the other two roots. This is why their product is exactly $\bar z\,\bar w=\overline{zw}=13-i$ (not some multiple of it): the other two roots are \emph{the conjugates of} $z$ and $w$. Likewise $\bar z+\bar w=3+4i$, so $z+w=3-4i$.

By Vieta's formulas, $b$ is the sum of the products of the roots taken two at a time:
\[
b=zw+\bar z\bar w+(z+w)(\bar z+\bar w)=(13+i)+(13-i)+(3-4i)(3+4i)=26+25=\boxed{51}.
\]''',
"Vieta's formulas|Complex numbers|Polynomial roots|Polynomials",5,source=src('AIME',1995,None,5),
note='The poster asks why the product of the other two roots is 13 - i and not a multiple of it; the record asks for that explanation too. Official answer 51.')

# ---------------- 1721580 multiples of 2,3,5
b.add(1721580,1,r'''Alexio has $100$ cards numbered $1$ to $100$ and chooses one at random.
\begin{enumerate}
\item[(a)] What is the probability that the number on the card is a multiple of $2$, $3$ or $5$ (at least one of them)?
\item[(b)] What is the probability that it is a multiple of all three of $2$, $3$ and $5$?
\end{enumerate}''',
r'''\textbf{(a)} By inclusion--exclusion, the number of multiples of $2$, $3$ or $5$ up to $100$ is
\[
50+33+20-16-10-6+3=74
\]
(multiples of $2,3,5$; minus multiples of $6,10,15$; plus multiples of $30$). The probability is $\dfrac{74}{100}=\boxed{\dfrac{37}{50}}$.

\textbf{(b)} A multiple of all three is a multiple of $30$: $30,60,90$. The probability is $\boxed{\dfrac{3}{100}}$.''',
'Probability|Sets and inclusion–exclusion|Factors and multiples|HCF and LCM',2,
note='"A multiple of 2,3,5" is ambiguous; the record asks for both readings (at least one; all three).')

# ---------------- 1721577 induction harmonic
b.add(1721577,1,r'''Prove by induction that for every positive integer $n$,
\[
\dfrac n2\le\dfrac12+\dfrac13+\dfrac14+\dots+\dfrac{1}{2^n}.
\]''',
r'''Let $S_n=\dfrac12+\dfrac13+\dots+\dfrac1{2^n}$ (the sum of $\dfrac1k$ for $2\le k\le2^n$).

\textbf{Base case.} $S_1=\dfrac12\ge\dfrac12$.

\textbf{Inductive step.} Suppose $S_n\ge\dfrac n2$. Then
\[
S_{n+1}=S_n+\left(\dfrac1{2^n+1}+\dfrac1{2^n+2}+\dots+\dfrac1{2^{n+1}}\right).
\]
The bracket has $2^{n+1}-2^n=2^n$ terms, each at least $\dfrac1{2^{n+1}}$, so it is at least $2^n\cdot\dfrac1{2^{n+1}}=\dfrac12$. Hence $S_{n+1}\ge\dfrac n2+\dfrac12=\dfrac{n+1}2$.

By induction the inequality holds for all $n\ge1$. $\blacksquare$''',
'Mathematical induction|Inequalities|Summation',3,
note='Checked numerically for n <= 15.')

# ---------------- 1721429 (n+2)^(n+1) >= 2(n+1)^(n+1)
b.add(1721429,1,r'''Prove that $(n+2)^{n+1}\ge2\,(n+1)^{n+1}$ for every natural number $n$.''',
r'''Dividing by $(n+1)^{n+1}>0$, the claim is
\[
\left(1+\dfrac1{n+1}\right)^{n+1}\ge2 .
\]
By the binomial theorem, with $m=n+1$,
\[
\left(1+\dfrac1m\right)^m=1+\binom m1\dfrac1m+\binom m2\dfrac1{m^2}+\dots\ge1+m\cdot\dfrac1m=2,
\]
since all the remaining terms are non-negative. Hence $(n+2)^{n+1}\ge2(n+1)^{n+1}$. $\blacksquare$

Equality holds only when there are no further terms, i.e.\ $m=1$ ($n=0$, if $0$ is counted as natural: $2^1=2\cdot1^1$); for $n\ge1$ the inequality is strict.''',
'Binomial theorem|Inequalities|Exponents',3,
note='Checked for n <= 50.')

# ---------------- 1721378 magic triangle
QF=r'''pair[] P={(0,0),(6,0),(3,5.196)};
pair[] Q={P[0]+(P[1]-P[0])/3,P[0]+2*(P[1]-P[0])/3,P[1]+(P[2]-P[1])/3,P[1]+2*(P[2]-P[1])/3,P[2]+(P[0]-P[2])/3,P[2]+2*(P[0]-P[2])/3};
draw(P[0]--P[1]--P[2]--cycle,gray+linewidth(0.6));
for(int i=0;i<3;++i) filldraw(circle(P[i],0.55),white,linewidth(0.8));
for(int i=0;i<6;++i) filldraw(circle(Q[i],0.55),white,linewidth(0.8));'''
SF=r'''void tri(pair o,int[] c,int[] s){
pair[] P={o,o+(6,0),o+(3,5.196)};
pair[] Q={P[0]+(P[1]-P[0])/3,P[0]+2*(P[1]-P[0])/3,P[1]+(P[2]-P[1])/3,P[1]+2*(P[2]-P[1])/3,P[2]+(P[0]-P[2])/3,P[2]+2*(P[0]-P[2])/3};
draw(P[0]--P[1]--P[2]--cycle,gray+linewidth(0.6));
for(int i=0;i<3;++i){filldraw(circle(P[i],0.55),white,linewidth(0.8));label("$"+string(c[i])+"$",P[i]);}
for(int i=0;i<6;++i){filldraw(circle(Q[i],0.55),white,linewidth(0.8));label("$"+string(s[i])+"$",Q[i]);}
}
tri((0,0),new int[]{1,2,3},new int[]{5,9,4,8,6,7});
tri((9,0),new int[]{7,8,9},new int[]{2,6,1,5,3,4});
label("sum $17$",(3,-1.3));label("sum $23$",(12,-1.3));'''
b.add(1721378,1,r'''The digits $1,2,3,\dots,9$ are placed, one per circle, in the nine circles of the triangle below (four circles on each side, the corner circles belonging to two sides), so that the sums of the four numbers on the three sides are all equal.
'''+asy(QF,'3.5cm')+r'''
What is the positive difference between the greatest and the least possible common sum?''',
r'''Let the common side sum be $T$ and let $c$ be the sum of the three corner numbers. Adding the three side sums counts every number once and the corners twice:
\[
3T=(1+2+\dots+9)+c=45+c .
\]
The corners are three different digits, so $1+2+3=6\le c\le7+8+9=24$, and therefore $17\le T\le23$.

Both extremes occur:
'''+asy(SF,'8cm')+r'''
with corners $1,2,3$ and sides $1+5+9+2=2+4+8+3=3+6+7+1=17$, and with corners $7,8,9$ and sides $7+2+6+8=8+1+5+9=9+3+4+7=23$. The difference is $23-17=\boxed{6}$.''',
'Double counting|Bounding and extremal cases|Construction',3,
note='The figure (four circles per side of a triangle) is described in the text and redrawn. The possible sums 17, 19, 20, 21, 23 were found by brute force; only the extremes matter.')

# ---------------- 1720979 sum divisible by 3
b.add(1720979,1,r'''Three different integers are selected at random from the integers $1$ to $12$ inclusive. What is the probability that their sum is divisible by $3$?''',
r'''The twelve integers fall into three residue classes modulo $3$, with $4$ numbers in each. The sum of three numbers is divisible by $3$ exactly when their residues are all equal or all different:
\begin{itemize}
\item all in the same class: $3\binom43=12$ choices;
\item one from each class: $4^3=64$ choices.
\end{itemize}
There are $\binom{12}3=220$ choices in all, so the probability is $\dfrac{76}{220}=\boxed{\dfrac{19}{55}}$.''',
'Probability|Remainders and congruences|Combinations|Casework',3,note='Repeat of an earlier record (aliased).')

# ---------------- 1721021 system of inequalities
b.add(1721021,1,r'''Solve the system of inequalities without graphing:
\[
6+6.2x\ge12-1.8x,\qquad 2-x\ge3.5-2x .
\]''',
r'''First inequality: $6.2x+1.8x\ge12-6$, i.e.\ $8x\ge6$, so $x\ge\dfrac34$.

Second inequality: $-x+2x\ge3.5-2$, i.e.\ $x\ge1.5$.

Both must hold, so the solution is $\boxed{x\ge\dfrac32}$.''',
'Inequalities|Linear equations',1)

# ---------------- 1720900 ABC words no letter more than thrice
b.add(1720900,1,r'''How many $5$-letter words (arbitrary strings) can be formed using only the letters $A$, $B$, $C$, if no letter is used more than three times?''',
r'''There are $3^5=243$ words in all. Subtract those in which some letter appears $4$ or $5$ times (only one letter can do so):
\begin{itemize}
\item one letter $5$ times: $3$ words;
\item one letter exactly $4$ times: choose the letter ($3$), the position of the other letter ($5$) and that letter ($2$): $30$ words.
\end{itemize}
So there are $243-3-30=\boxed{210}$ words.''',
'Complementary counting|Multiplication principle|Arrangements with restrictions',2)

# ---------------- 1720901 row sums of Pascal
b.add(1720901,1,r'''Prove that the sum of the entries in row $n$ of Pascal's triangle is $2^n$, i.e.
\[
\binom n0+\binom n1+\dots+\binom nn=2^n .
\]''',
r'''\textbf{Counting proof.} Count the subsets of an $n$-element set in two ways. On the one hand, each of the $n$ elements is either in the subset or not, so there are $2^n$ subsets. On the other hand, there are $\binom nk$ subsets with exactly $k$ elements, for $k=0,1,\dots,n$. Hence $\sum_{k=0}^n\binom nk=2^n$.

\textbf{Inductive proof using Pascal's rule.} Row $0$ is $1=2^0$. Each entry of row $n+1$ is the sum of the two entries above it, $\binom{n+1}{k}=\binom nk+\binom n{k-1}$, so every entry of row $n$ is used exactly twice when forming row $n+1$. Hence the sum of row $n+1$ is twice the sum of row $n$, and by induction the sum of row $n$ is $2^n$. $\blacksquare$

(Equivalently, put $x=y=1$ in the binomial theorem $(x+y)^n=\sum\binom nkx^ky^{n-k}$.)''',
"Pascal's triangle|Combinatorial identities and binomial coefficients|Double counting|Binomial theorem",2,
note='Contained in an earlier record (aliased). The post asks to prove that every row sum is a power of 2; proved that the sum of row n is 2^n.')

# ---------------- 1720835 MATHCOUNTS handbook translation
fig=r'''import graph;
pair A=(0,0),B=(-3,4),C=(-6,0);
draw((-7,0)--(1.2,0),Arrow(TeXHead));draw((0,-1)--(0,5.2),Arrow(TeXHead));
for(int i=-6;i<=0;++i) draw((i,-0.08)--(i,0.08),linewidth(0.4));
for(int j=1;j<=4;++j) draw((-0.08,j)--(0.08,j),linewidth(0.4));
draw(A--B--C--cycle,linewidth(0.9));
draw(B--(-3,0),dashed);
dot(A);dot(B);dot(C);
label("$A(0,0)$",A,SE);label("$B(-3,4)$",B,N);label("$C(-6,0)$",C,dir(-110)*1.3);
label("$5$",(A+B)/2,NE);label("$5$",(B+C)/2,NW);label("$6$",(-4.5,0),S);
label("$x$",(1.2,0),N);label("$y$",(0,5.2),N);'''
b.add(1720835,1,r'''A segment has endpoints $A(0,0)$ and $B(-3,4)$. Point $C$ is the image of point $B$ translated down $4$ units and left $3$ units. What is the perimeter of $\triangle ABC$?''',
r'''Translating $B(-3,4)$ left $3$ units and down $4$ units gives $C(-3-3,\,4-4)=(-6,0)$. (Not $(0,-6)$: ``left'' changes the $x$-coordinate and ``down'' changes the $y$-coordinate.)
'''+asy(fig,'6cm')+r'''
The side lengths are
\[
AB=\sqrt{3^2+4^2}=5,\qquad BC=\sqrt{3^2+4^2}=5,\qquad AC=6,
\]
since $C$ lies on the $x$-axis $6$ units from $A$. The perimeter is $5+5+6=\boxed{16}$.''',
'Translations|Distance formula|Coordinate geometry|Lengths, perimeter, and area',2,source=src('MATHCOUNTS Handbook',2019,None,2,rnd='Transformations Stretch'),
note='The poster found C = (0, -6), which is wrong; C = (-6, 0). Answer 16 as given.')

# ---------------- 1720781 R(4,4)=18
b.add(1720781,1,r'''Mark $n$ points around a circle. For every pair of points, draw the segment joining them in red or in blue. Find the smallest $n$ such that, however the colours are chosen, there are always $4$ of the points all six of whose connecting segments have the same colour.''',
r'''The position of the points plays no role: we have a red/blue colouring of the edges of the complete graph $K_n$ and want a monochromatic $K_4$. The answer is $\boxed{18}$.

\textbf{Lemma 1.} Among $6$ points there is always a monochromatic triangle. A point $v$ has $5$ edges, so at least $3$ of the same colour, say red to $x,y,z$. If one of $xy,yz,zx$ is red it forms a red triangle with $v$; otherwise $xyz$ is a blue triangle.

\textbf{Lemma 2.} Among $9$ points there is a red triangle or a blue $K_4$. If some point $v$ has $4$ red edges, to $a,b,c,d$: a red edge among them gives a red triangle with $v$, and otherwise $abcd$ is a blue $K_4$. If some point has $6$ blue edges, by Lemma 1 its $6$ blue neighbours contain a red triangle or a blue triangle, and a blue triangle together with $v$ is a blue $K_4$. Otherwise every point has at most $3$ red and at most $5$ blue edges, so exactly $3$ red edges, as $3+5=8$. Then the number of red edges would be $\dfrac{9\cdot3}{2}$, not an integer, a contradiction. By symmetry, among $9$ points there is also always a blue triangle or a red $K_4$.

\textbf{$n=18$ suffices.} A point $v$ has $17$ edges, so at least $9$ of one colour, say red. By Lemma 2, these $9$ red neighbours contain a red triangle, which together with $v$ forms a red $K_4$, or a blue $K_4$. (If the $9$ edges are blue, use the form of Lemma 2 with the colours swapped.) Either way there is a monochromatic $K_4$.

\textbf{$n=17$ is not enough.} Number the points $0,1,\dots,16$ and colour the edge $\{x,y\}$ red if $x-y$ is a nonzero square modulo $17$, i.e.\ $x-y\equiv\pm1,\pm2,\pm4,\pm8\pmod{17}$, and blue otherwise. (Since $-1\equiv4^2$ is a square, this does not depend on the order of $x,y$.) The squares form the set $Q=\{1,2,4,8,9,13,15,16\}$.
\begin{itemize}
\item The maps $x\mapsto x+t$ and $x\mapsto qx$ with $q\in Q$ preserve the colouring (a product of squares is a square). Given a red $K_4$ $\{a,b,c,d\}$, subtract $a$ and then multiply by the inverse of $b-a$ (a square, since the inverse of a square is a square): we get a red $K_4$ containing $0$ and $1$.
\item Its other two points must be red neighbours of both $0$ and $1$, i.e.\ $x\in Q$ with $x-1\in Q$: only $x=2,9,16$. But $9-2=7$, $16-2=14$, $16-9=7$ are not in $Q$, so no two of $2,9,16$ are joined in red. Hence there is no red $K_4$.
\item Multiplying by $3$ (not a square modulo $17$) swaps the two colours, since $3$ times a square is a non-square and $3$ times a non-square is a square. So a blue $K_4$ would be mapped to a red $K_4$; there is none.
\end{itemize}
So $17$ points can be coloured with no monochromatic $K_4$, and the smallest $n$ is $18$.''',
'Graph theory|Graph colouring|Pigeonhole principle|Construction|Quadratic residues',7,
note='This is the Ramsey number R(4,4) = 18. The poster knew the triangle case (6) and a bound of at least 13. The colouring of 17 points (Paley graph) was also checked by computer to have no monochromatic K4.')

b.save()
