from qb import *
b=Bank('p223_03')

# ---------------- 1775470 average speed
b.add(1775470,1,r'''Abi walks halfway to school at $2$ mph and runs the rest of the way at $7$ mph. What is her average speed for the whole trip?''',
r'''Let the distance to school be $2d$ miles. The walking half takes $\dfrac d2$ hours and the running half takes $\dfrac d7$ hours, so the total time is $d\left(\dfrac12+\dfrac17\right)=\dfrac{9d}{14}$ hours. The average speed is total distance over total time:
\[
\dfrac{2d}{\dfrac{9d}{14}}=\dfrac{28}{9}=\boxed{3\dfrac19\text{ mph}}.
\]
(This is the harmonic mean of $2$ and $7$, not their ordinary average $4.5$, because she spends more time at the slower speed.)''',
'Distance, rate, and time|Harmonic mean|Averages and weighted averages',2,
note='"Halfway" read as half the distance.')

# ---------------- 1772259 five problems
b.add(1772259,1,r'''How many pairs of integers $(m,n)$ satisfy $mn+n+10=(m-1)^2$?''',
r'''Rewrite the equation as $n(m+1)=m^2-2m-9$. If $m=-1$, the left side is $0$ and the right side is $1+2-9=-6$, so there is no solution. Otherwise
\[
n=\dfrac{m^2-2m-9}{m+1}=m-3-\dfrac{6}{m+1},
\]
since $(m+1)(m-3)=m^2-2m-3$. So $n$ is an integer exactly when $m+1$ divides $6$, i.e.\ $m+1\in\{\pm1,\pm2,\pm3,\pm6\}$, and each such $m$ gives one $n$. There are $\boxed{8}$ pairs: $(0,-9)$, $(-2,1)$, $(1,-5)$, $(-3,-3)$, $(2,-3)$, $(-4,-5)$, $(5,1)$, $(-7,-9)$.''',
'Diophantine equations|Divisibility|Polynomials',3)
b.add(1772259,2,r'''In how many ways can $10$ identical blue balls and $5$ identical red balls be put into $3$ distinct boxes if each box must contain more blue balls than red balls?''',
r'''Let box $i$ contain $r_i$ red and $b_i$ blue balls, with $b_i\ge r_i+1$. Write $b_i=r_i+1+e_i$ with $e_i\ge0$. Then
\[
10=\sum b_i=\sum r_i+3+\sum e_i=5+3+\sum e_i ,
\]
so $e_1+e_2+e_3=2$. Conversely, any choice of $(r_1,r_2,r_3)$ with sum $5$ and $(e_1,e_2,e_3)$ with sum $2$ (all nonnegative) gives a valid placement, and different choices give different placements. By stars and bars there are $\dbinom{7}{2}=21$ choices of the $r_i$ and $\dbinom{4}{2}=6$ choices of the $e_i$. The answer is $21\cdot6=\boxed{126}$.''',
'Stars and bars|Distributions and integer solutions|Bijections',4,
note='Checked by direct enumeration.')
fig3=r'''real t=8/sqrt(15);
pair B=(0,0),C=(4*t,0),A=(11*t/8,3);
pair ft(pair P,pair Q,pair R){return Q+dot(P-Q,unit(R-Q))*unit(R-Q);}
pair Ha=ft(A,B,C),Hb=ft(B,A,C),Hc=ft(C,A,B);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--Hb,dotted); draw(A--Hc,dotted);
draw(A--Ha,blue+dashed); draw(B--Hb,blue+dashed); draw(C--Hc,blue+dashed);
real s=0.25;
void ra(pair F,pair P,pair Q){pair u=unit(P-F),v=unit(Q-F); draw(F+s*u--F+s*u+s*v--F+s*v,blue);}
ra(Ha,C,A); ra(Hb,B,C); ra(Hc,C,B);
label("$A$",A+(0,0.45));label("$B$",B,SW);label("$C$",C,SE);
label("$3$",(A+Ha)/2,W,blue);label("$4$",(B+Hb)/2,dir(150),blue);label("$6$",(C+Hc)/2,dir(45),blue);
label("$4t$",(B+C)/2,S);label("$3t$",(A+C)/2,dir(-119));label("$2t$",(A+B)/2,dir(-43));'''
b.add(1772259,3,r'''Find the perimeter of a triangle whose altitudes have lengths $3$, $4$ and $6$.''',
r'''Let the area be $K$ and let $a$, $b$, $c$ be the sides on which the altitudes $3$, $4$, $6$ stand. Then $a=\dfrac{2K}{3}$, $b=\dfrac{2K}{4}$, $c=\dfrac{2K}{6}$, so $a:b:c=4:3:2$; write $a=4t$, $b=3t$, $c=2t$. (Such a triangle exists, since $2+3>4$.)

By Heron's formula with $s=\dfrac{9t}{2}$,
\[
K=\sqrt{\dfrac{9t}{2}\cdot\dfrac{t}{2}\cdot\dfrac{3t}{2}\cdot\dfrac{5t}{2}}=\dfrac{t^2\sqrt{135}}{4}=\dfrac{3\sqrt{15}}{4}t^2 .
\]
Also $K=\dfrac12\cdot a\cdot3=6t$. Hence $\dfrac{3\sqrt{15}}{4}t^2=6t$, so $t=\dfrac{8}{\sqrt{15}}$, and the perimeter is
\[
9t=\dfrac{72}{\sqrt{15}}=\boxed{\dfrac{24\sqrt{15}}{5}}.
\]
'''+asy(fig3,'7cm')+r'''
The triangle is obtuse at $A$ (since $16>9+4$), so the altitudes from $B$ and $C$ meet the extensions of $CA$ and $BA$ beyond $A$, as drawn.''',
'Altitudes|Heron\'s formula|Ratios, proportions, and variation|Lengths, perimeter, and area|Triangles',4,
note='Figure drawn to scale with t = 8/sqrt(15); the three altitude lengths were checked numerically.')
fig4=r'''pair A=(0,1),B=(1,1),C=(1,0),D=(0,0);
pair Ep=(1,1/sqrt(3)); real x=sqrt(3)/(sqrt(3)+1); pair F=(x,x/sqrt(3));
draw(A--B--C--D--cycle,linewidth(0.9));
draw(D--Ep,linewidth(0.8)); draw(B--F,linewidth(0.8)); draw(A--F,red+linewidth(0.8));
draw(B--D,dashed+gray); draw(F--C,dashed+gray);
void tk(pair P,pair Q,int n){pair m=(P+Q)/2,u=unit(Q-P),v=(-u.y,u.x); for(int i=0;i<n;++i){pair c=m+(i-(n-1)/2)*0.03*u; draw(c-0.035*v--c+0.035*v,linewidth(0.7));}}
tk(D,F,1); tk(B,F,1); tk(F,Ep,2); tk(B,Ep,2);
draw(arc(F,0.07,degrees(A-F),degrees(D-F)),red); label("$75^\circ$",F+0.135*dir(182),red);
draw(arc(D,0.3,degrees(Ep-D),45),blue); label("$15^\circ$",D+0.4*dir(37.5),blue);
label("$A$",A,NW);label("$B$",B,NE);label("$C$",C,SE);label("$D$",D,SW);label("$E$",Ep,E);label("$F$",F,dir(-80));'''
b.add(1772259,4,r'''Let $ABCD$ be a square. Let $E$ be a point on side $BC$ and $F$ a point on segment $DE$ such that $DF=BF$ and $EF=BE$. Find $\angle DFA$.''',
r'''Let $\angle FDB=y$. Since $DF=BF$, triangle $BDF$ is isosceles and $\angle FBD=y$, so its exterior angle at $F$ is $\angle BFE=2y$. Since $EF=BE$, triangle $BEF$ is isosceles with $\angle EBF=\angle EFB=2y$. Now $\angle DBC=45^\circ$ (diagonal of a square) and $\angle DBC=\angle DBF+\angle FBE=y+2y$, so $y=15^\circ$.

$F$ is equidistant from $B$ and $D$, so it lies on the perpendicular bisector of $BD$, which is the other diagonal $AC$. Therefore $\angle DAF=\angle DAC=45^\circ$. Also $\angle ADF=\angle ADB+\angle BDF=45^\circ+15^\circ=60^\circ$. In triangle $ADF$,
\[
\angle DFA=180^\circ-45^\circ-60^\circ=\boxed{75^\circ}.
\]
'''+asy(fig4,'7cm')+r'''
(The figure is to scale: $\angle EDC=30^\circ$, so $CE=\dfrac{1}{\sqrt3}$ for a unit square.)''',
'Squares|Isosceles triangles|Angle chasing|Perpendicular bisectors',4,
note='Answer checked with coordinates.')
b.add(1772259,5,r'''Find the last three digits of the base-$4$ representation of $10\cdot3195\cdot4949$.''',
r'''The last three base-$4$ digits are the base-$4$ digits of the remainder modulo $4^3=64$. Now $10\equiv10$, $3195=49\cdot64+59\equiv59\equiv-5$ and $4949=77\cdot64+21\equiv21\pmod{64}$. So
\[
10\cdot3195\cdot4949\equiv10\cdot(-5)\cdot21=-1050\equiv-1050+17\cdot64=38\pmod{64}.
\]
Since $38=2\cdot16+1\cdot4+2$, the last three digits are $\boxed{212}$.''',
'Digits and bases|Remainders and congruences',3)

# ---------------- 1775342 Kangaroo king and messengers
b.add(1775342,1,r'''A king and his messengers are walking at $5$ km/h from the king's castle to his summer palace. At a certain moment the king sends one messenger back to the castle; one hour later he sends another messenger back. The messengers walk at $10$ km/h. How many minutes pass between the arrivals of the two messengers at the castle?''',
r'''Suppose the first messenger leaves when the king is $d$ km from the castle. He reaches the castle $\dfrac{d}{10}$ hours later.

In the next hour the king and the second messenger walk $5$ km further, so the second messenger leaves $1$ hour later from $d+5$ km away and needs $\dfrac{d+5}{10}=\dfrac d{10}+\dfrac12$ hours. Measured from the first departure, he arrives after $1+\dfrac{d}{10}+\dfrac12$ hours.

The difference is $1\dfrac12$ hours $=\boxed{90}$ minutes.''',
'Distance, rate, and time|Rates',2,source=src('Math Kangaroo',None,None,None),
note='Corrected answer: the post gives the answer as 120, but the stated data give 90 minutes (the poster\'s own answer): the second messenger starts 1 hour later and has 5 km more to walk at 10 km/h.')

# ---------------- 1593299 totient of 30
b.add(1593299,1,r'''How many positive integers less than or equal to $30$ are relatively prime to $30$?''',
r'''Since $30=2\cdot3\cdot5$, a number is relatively prime to $30$ exactly when it is divisible by none of $2$, $3$, $5$. By inclusion--exclusion, the numbers from $1$ to $30$ divisible by at least one of them number
\[
15+10+6-5-3-2+1=22 ,
\]
so $30-22=\boxed{8}$ are relatively prime to $30$: $1,7,11,13,17,19,23,29$. (Equivalently, $\varphi(30)=30\cdot\dfrac12\cdot\dfrac23\cdot\dfrac45=8$.)''',
'Euler\'s theorem and totient|Sets and inclusion–exclusion|Prime factorisation',2,
note='Repeat of an earlier record (aliased).')

# ---------------- 1605801 2018 School Sprint 22 median
b.add(1605801,1,r'''Let $Q=\{1.7,\ 1.1,\ 1.4,\ 2.1,\ 2.3,\ s\}$. What is the absolute difference between the greatest and least possible values of the median of $Q$? Express your answer as a decimal to the nearest hundredth.''',
r'''In order, the five known values are $1.1,1.4,1.7,2.1,2.3$. With six values, the median is the average of the third and fourth smallest.
\begin{itemize}
\item If $s\le1.4$, the third and fourth are $1.4$ and $1.7$: median $1.55$.
\item If $1.4\le s\le2.1$, they are $s$ and $1.7$ in some order: median $\dfrac{s+1.7}{2}$, between $1.55$ and $1.9$.
\item If $s\ge2.1$, they are $1.7$ and $2.1$: median $1.9$.
\end{itemize}
So the median ranges from $1.55$ to $1.9$, and the difference is $1.9-1.55=\boxed{0.35}$.''',
'Median|Casework',2,source=src('MATHCOUNTS',2018,'School',22,rnd='Sprint'),
note='Q is treated as a list of six values (s may equal one of the others).')

# ---------------- 1774417 apples
b.add(1774417,1,r'''There were $2000$ kg of apples in three baskets in total. After $\dfrac16$ of the apples in the first basket, $\dfrac3{13}$ of those in the second basket and $\dfrac13$ of those in the third basket were sold, the same mass of apples remained in each basket. How many kilograms of apples were in each basket at first?''',
r'''Let $r$ kg remain in each basket. The first basket kept $\dfrac56$ of its apples, the second $\dfrac{10}{13}$ and the third $\dfrac23$, so they held $\dfrac65r$, $\dfrac{13}{10}r$ and $\dfrac32r$ kg. Then
\[
\left(\dfrac65+\dfrac{13}{10}+\dfrac32\right)r=4r=2000,\qquad r=500 .
\]
The baskets held $\boxed{600,\ 650\text{ and }750\text{ kg}}$. (Check: $500=\dfrac56\cdot600=\dfrac{10}{13}\cdot650=\dfrac23\cdot750$.)''',
'Fractions|Linear equations|Ratios, proportions, and variation',2)

# ---------------- 1774657 0/0
b.add(1774657,1,r'''Some websites say $\dfrac00=0$ and some say $\dfrac00=1$. Explain why no value can be assigned to $\dfrac00$ in a way that keeps the usual rules of arithmetic.''',
r'''Division is defined by multiplication: for $b\ne0$, $\dfrac ab$ is the unique number $q$ with $q\cdot b=a$.

\textbf{No unique candidate.} For $\dfrac00$ we would need $q\cdot0=0$, which is true for \emph{every} number $q$. So the definition does not single out any value ($0$, $1$ and $5$ are all ``solutions''). (For $\dfrac a0$ with $a\ne0$ there is no candidate at all, since $q\cdot0=0\ne a$.)

\textbf{Any choice leads to a contradiction.} Suppose $\dfrac00=c$ for some number $c$, and that the rule $\dfrac{ka}{b}=k\cdot\dfrac ab$ still holds. Then for every number $k$,
\[
c=\dfrac{0}{0}=\dfrac{k\cdot0}{0}=k\cdot\dfrac00=kc .
\]
Taking $k=2$ gives $c=2c$, so $c=0$. But the rule $\dfrac{a}{a}=1$ would give $c=1$. Both cannot hold, so no value of $\dfrac00$ is consistent with the usual rules; $\boxed{\dfrac00\text{ is undefined}}$. (In calculus, an expression of the form $\dfrac00$ in a limit can approach any value, which is why it is called an indeterminate form.)''',
'Proof by contradiction|Logical deduction',1,
note='Conceptual question ("what is 0/0?") turned into an explanation/proof that 0/0 is undefined. Repeat of an earlier record (aliased).')

# ---------------- 1774061 five mock problems
b.add(1774061,1,r'''Real numbers $x$, $y$, $z$ are chosen independently and uniformly at random from the interval $[0,1]$. What is the probability that all of $x+y$, $y+z$ and $z+x$ lie in the interval $[0,1]$?''',
r'''The probability is the volume of the region of the unit cube where $x+y\le1$, $y+z\le1$, $z+x\le1$. Fix $x$; then $y,z\in[0,1-x]$ and $y+z\le1$.
\begin{itemize}
\item If $x\ge\dfrac12$, then $y+z\le2(1-x)\le1$ automatically, and the cross-section has area $(1-x)^2$.
\item If $x<\dfrac12$, the square $[0,1-x]^2$ loses the corner triangle where $y+z>1$, which has legs $2(1-x)-1=1-2x$; the area is $(1-x)^2-\dfrac{(1-2x)^2}{2}$.
\end{itemize}
Integrating,
\[
\int_0^1(1-x)^2\,dx-\int_0^{\dfrac12}\dfrac{(1-2x)^2}{2}\,dx=\dfrac13-\dfrac1{12}=\boxed{\dfrac14}.
\]''',
'Geometric probability|Calculus|Inequalities',4,
note='Checked by exact integration and by simulation.')
b.add(1774061,2,r'''On the island of Iguanas, every iguana either always tells the truth or always lies. You are lost and want to find which one of $5$ roads leads to the airport (exactly one does). You ask six iguanas:
\begin{itemize}
\item Iguana 1: ``Road 1 leads to the airport.''
\item Iguana 2: ``Road 3 does not lead to the airport.''
\item Iguana 3: ``Road 5 leads to the airport.''
\item Iguana 4: ``Road 1 does not lead to the airport.''
\item Iguana 5: ``Road 2 leads to the airport.''
\item Iguana 6: ``Road 4 leads to the airport.''
\end{itemize}
You later learn that exactly one of the six iguanas tells the truth. What is the sum of the number of the truthful iguana and the number of the road that leads to the airport?''',
r'''Iguanas 1 and 4 make opposite statements, so exactly one of them tells the truth. Since there is only one truthful iguana, iguanas 2, 3, 5 and 6 all lie. Iguana 2 lying means road $3$ leads to the airport (and indeed iguanas 3, 5, 6 then lie, as roads $5$, $2$, $4$ do not). Then road $1$ does not, so iguana 4 is the truthful one. The sum is $4+3=\boxed{7}$.''',
'Truth-tellers and liars|Logical deduction',2)
b.add(1774061,3,r'''An unfair die with faces numbered $1$ to $6$ has the property that the probability of rolling each number is proportional to that number. You roll this unfair die twice and a fair die twice. What is the probability that the sum of the two rolls of the unfair die is greater than the sum of the two rolls of the fair die?''',
r'''The unfair die shows $k$ with probability $\dfrac{k}{21}$. For the unfair sum $U$, $P(U=s)=\dfrac1{441}\sum_{i+j=s}ij$, which gives, for $s=2,\dots,12$, the numerators
\[
1,\ 4,\ 10,\ 20,\ 35,\ 56,\ 70,\ 76,\ 73,\ 60,\ 36\qquad(\text{out of }441).
\]
Hence the numbers of ways (out of $441$) to get $U>v$ for $v=2,\dots,11$ are
\[
440,\ 436,\ 426,\ 406,\ 371,\ 315,\ 245,\ 169,\ 96,\ 36 .
\]
For the fair sum $V$, $P(V=v)=\dfrac{6-|v-7|}{36}$, i.e.\ numerators $1,2,3,4,5,6,5,4,3,2,1$ for $v=2,\dots,12$ (and $U>12$ is impossible). So
\[
P(U>V)=\dfrac{1\cdot440+2\cdot436+3\cdot426+4\cdot406+5\cdot371+6\cdot315+5\cdot245+4\cdot169+3\cdot96+2\cdot36}{441\cdot36}=\dfrac{10220}{15876}=\boxed{\dfrac{365}{567}}.
\]''',
'Probability|Dice probability|Independent events|Systematic counting',4,
note='Exact value checked by computer.')
b.add(1774061,4,r'''Let $P(x)=(x-2)(x-4)(x-6)(x-8)(x-10)$. What is the sum of all the coefficients in the expansion of $P(x)$?''',
r'''The sum of the coefficients of a polynomial is its value at $x=1$:
\[
P(1)=(-1)(-3)(-5)(-7)(-9)=-945 .
\]
The sum is $\boxed{-945}$.''',
'Polynomials',1)
b.add(1774061,5,r'''For how many positive integers $n\le100$ is $\sqrt{n+\sqrt{n+\sqrt{n+\cdots}}}$ rational?''',
r'''The nested radical is the limit $L$ of $a_1=\sqrt n$, $a_{k+1}=\sqrt{n+a_k}$; this sequence increases and is bounded by the positive root of $L^2=L+n$, so it converges to that root:
\[
L=\dfrac{1+\sqrt{1+4n}}{2}.
\]
$L$ is rational exactly when $1+4n$ is a perfect square. Since $1+4n$ is odd, write $1+4n=(2k+1)^2$; then $n=k(k+1)$ with $k\ge1$. The values $n=k(k+1)\le100$ are $2,6,12,20,30,42,56,72,90$ ($k=1,\dots,9$; $10\cdot11=110>100$). The answer is $\boxed{9}$.''',
'Radicals|Perfect squares|Quadratic equations|Sequences and series',3)

# ---------------- 1774463 negative factorial
b.add(1774463,1,r'''The factorial satisfies $0!=1$ and $n!=n\cdot(n-1)!$ for every positive integer $n$. Show that there is no way to define $(-1)!,(-2)!,\dots$ as numbers so that the rule $n!=n\cdot(n-1)!$ also holds for $n=0,-1,-2,\dots$.''',
r'''Suppose numbers $(-1)!,(-2)!,\dots$ were defined with $n!=n\cdot(n-1)!$ for all integers $n\le0$ as well. Taking $n=0$:
\[
1=0!=0\cdot(-1)!=0 ,
\]
a contradiction. So already $(-1)!$ cannot be defined, and the factorials of negative integers do not exist under this rule; $\boxed{(-5)!\text{ is undefined}}$. (Indeed, if $(-5)!$ existed, the rule would give $(-4)!=-4\cdot(-5)!$, then $(-3)!$, $(-2)!$ and $(-1)!$, contradicting the above.) $\blacksquare$

(The Gamma function extends the factorial to most real numbers, with $\Gamma(x+1)=x!$ for nonnegative integers $x$, but it has poles exactly at $0,-1,-2,\dots$, which matches this argument: $(-n)!$ is undefined for every positive integer $n$.)''',
'Factorials|Proof by contradiction',1,
note='Conceptual question ("does (-5)! exist?") turned into a proof that negative-integer factorials cannot be defined consistently with n! = n(n-1)!.')

# ---------------- 1771790 sum of distinct products (alias)
b.add(1771790,1,r'''Joanna selects two different numbers from the set $\{-15,-14,-13,\ldots,14,15\}$ and multiplies them to obtain their product $p$. What is the sum of all possible products $p$ that Joanna could obtain? (Each possible value is counted once.)''',
r'''Let $V$ be the set of possible products. If $p=ab>0$ with $a\ne b$, then $-p=(-a)b$ with $-a\ne b$ (they have opposite signs), so $-p\in V$. If $p=ab<0$ with $a\ne b$, then $-p=(-a)b\in V$ unless $-a=b$, i.e.\ $p=-b^2$. So the positive and negative values cancel in pairs except for the values $-k^2$ ($1\le k\le15$) for which $k^2$ is not a product of two different numbers from the set. Now $4=1\cdot4$, $9=1\cdot9$, $16=2\cdot8$, $36=3\cdot12$ are such products, but $1,25,49,64,81,100,121,144,169,196,225$ are not (their only factorisations with factors at most $15$ in absolute value use equal factors). The sum is
\[
-(1+25+49+64+81+100+121+144+169+196+225)=\boxed{-1175}.
\]''',
'Systematic counting|Pairing and grouping|Perfect squares',4,source=src('Mock MATHCOUNTS',None,'State',19,rnd='Sprint'),
note='Repeat of an earlier record (aliased).')

# ---------------- 1771792 cool numbers
b.add(1771792,1,r'''A positive integer $n$ is \emph{cool} if the sum of the digits of $n$ equals the sum of the digits of $11n$. What is the sum of all cool three-digit integers?''',
r'''Let $s(m)$ denote the digit sum. Since $11n=10n+n$, and in a column addition each carry lowers the digit sum by $9$ (a column total $t\ge10$ writes $t-10$ and carries $1$),
\[
s(11n)=s(10n)+s(n)-9C=2s(n)-9C,
\]
where $C$ is the number of carries when adding $n$ and $10n$. So $n$ is cool iff $s(n)=9C$.

For $n=\overline{abc}$ the column sums are $c$ (units, no carry), $b+c$ (tens), $a+b+c_1$ (hundreds) and $a+c_2$ (thousands), where $c_1,c_2$ are the carries out of the tens and hundreds columns; at most $3$ carries occur, so $s(n)\in\{9,18,27\}$.
\begin{itemize}
\item $s(n)=9$ needs $C=1$. But then $b+c\le9$ and $a+b\le9$, so there is no carry at all. No cool numbers.
\item $s(n)=27$: $n=999$, and $9990+999=10989$ has digit sum $27$. Cool.
\item $s(n)=18$ needs $C=2$. If $b+c\ge10$, then $c_1=1$ and $a+b+1=19-c\ge10$, so $c_2=1$, and $a+c_2\ge10$ would need $a=9$, i.e.\ $b+c=9$, which is impossible; so exactly $2$ carries. If $b+c\le9$, then $a=18-b-c\ge9$, so $a=9$ and $b+c=9$; the hundreds column $9+b$ carries iff $b\ge1$, and then the thousands column $9+1$ carries too. So all numbers with digit sum $18$ are cool except $909$ (no carries).
\end{itemize}
\textbf{Sum.} For leading digit $a$, the pairs $(b,c)$ with $b+c=18-a$ number $a+1$, and on average $b=c=\dfrac{18-a}{2}$. So the numbers with digit sum $18$ add up to
\[
\sum_{a=1}^{9}(a+1)\left(100a+11\cdot\dfrac{18-a}{2}\right)=\sum_{a=1}^{9}(a+1)\left(94.5a+99\right)=36531 .
\]
The cool numbers sum to $36531-909+999=\boxed{36621}$ (there are $54$ of them).''',
'Digit problems|Digits and bases|Casework|Summation',5,source=src('Mock MATHCOUNTS',None,'State',30,rnd='Sprint'),
note='From the poster\'s own mock MATHCOUNTS State Sprint (#30). Confirmed by checking all three-digit numbers.')

# ---------------- 1774078 n! not a perfect power
b.add(1774078,1,r'''Prove that for every integer $n>1$, the number $n!$ is not a perfect power (it is not $m^k$ for any integers $m$ and $k\ge2$).''',
r'''We use Bertrand's postulate: for every integer $n\ge2$ there is a prime $p$ with $\dfrac n2<p\le n$ (for $n=2,3$ take $p=2,3$).

Such a prime divides $n!$, because $p\le n$. It divides $n!$ only once: the multiples of $p$ in $1,2,\dots,n$ are $p,2p,\dots$, and $2p>n$, so $p$ is the only one, and $p^2\nmid p$. Hence the exponent of $p$ in the prime factorisation of $n!$ is exactly $1$.

In a perfect power $m^k$ with $k\ge2$, every prime exponent is a multiple of $k$, so it is $0$ or at least $2$. Therefore $n!$ is not a perfect power. $\blacksquare$''',
'Factorials|Prime factorisation|Perfect powers|Prime numbers',4,
note='The proof quotes Bertrand\'s postulate (Chebyshev\'s theorem), which the record names explicitly.')

# ---------------- 1773801 AwesomeMath 2019^a
b.add(1773801,1,r'''Find all positive integers $a,b,c,d$ such that
\[
2019^a=b^3+c^3+d^3-5 .
\]''',
r'''\textbf{Modulo $9$.} Cubes are $\equiv0,1,8\pmod9$, so a sum of three cubes is $\equiv0,\pm1,\pm2,\pm3\pmod9$; it is never $\equiv\pm4\pmod9$. Since $2019\equiv3\pmod9$, for $a\ge2$ we get $2019^a\equiv0$ and $b^3+c^3+d^3=2019^a+5\equiv5\equiv-4\pmod9$, impossible. So $a=1$ and
\[
b^3+c^3+d^3=2024 .
\]
\textbf{Solve.} By symmetry take $b\le c\le d$. Then $3d^3\ge2024$ gives $d\ge9$, and $d^3<2024$ gives $d\le12$.
\begin{itemize}
\item $d=12$: $b^3+c^3=296$; with $c\le6$, $296-c^3\in\{295,288,269,232,171,80\}$, none a cube.
\item $d=11$: $b^3+c^3=693$ needs $c^3\ge347$, so $c\ge8$, and $c^3\le693$, so $c=8$: $693-512=181$, not a cube.
\item $d=10$: $b^3+c^3=1024$ with $c\ge8$: $c=8$ gives $b^3=512$, $b=8$; $c=9$ gives $295$ and $c=10$ gives $24$, not cubes.
\item $d=9$: $b^3+c^3=1295$ with $c\le9$ needs $c=9$: $1295-729=566$, not a cube.
\end{itemize}
So the solutions are $\boxed{a=1\text{ and }(b,c,d)\text{ a permutation of }(8,8,10)}$: indeed $512+512+1000-5=2019$.''',
'Diophantine equations|Remainders and congruences|Perfect cubes|Casework',5,source=src('AwesomeMath Admission Test',None,None,3,paper='A'),
note='AwesomeMath admission Test A, question 3 (year not stated; the post says the test was due a few days earlier). Confirmed by a computer search with a <= 3 and b, c, d < 200.')

# ---------------- 1773745 locus in 5-12-13 triangle
fig=r'''pair C=(0,0),A=(0,5),B=(12,0);
pair P=(12/7,30/7),Q=(9/4,0),X=(15/7,18-8*15/7);
draw(A--B--C--cycle,linewidth(0.9));
draw(P--Q,red+linewidth(1.1));
dot(P,red);dot(Q,red);dot(X);
draw(X--(0,X.y),dashed+blue);
real s=0.35; draw(C+(s,0)--C+(s,s)--C+(0,s));
label("$A$",A,NW);label("$B$",B,SE);label("$C$",C,SW);
label("$P$",P,NE,red);label("$Q$",Q,S,red);label("$X$",X,E);
label("$5$",(A+C)/2,W);label("$12$",(B+C)/2+(1.5,0),S);label("$13$",(A+B)/2,NE);
label("$x$",(X.x/2,X.y),N,blue);'''
b.add(1773745,1,r'''In $\triangle ABC$, $AB=13$, $BC=12$ and $AC=5$. Consider all points inside or on the triangle for which the sum of the distances to the three sides of $\triangle ABC$ is $6$. They form a segment; the average distance from a point of this segment to side $AC$ (averaged uniformly along the segment) can be written as $\dfrac mn$ in lowest terms. Find $m+n$.''',
r'''Since $5^2+12^2=13^2$, the angle at $C$ is right. Put $C=(0,0)$, $A=(0,5)$, $B=(12,0)$. For a point $X=(x,y)$ in the triangle, the distances to $AC$ and $BC$ are $x$ and $y$, and the distance to $AB$ (the line $5x+12y=60$) is $\dfrac{60-5x-12y}{13}$. The condition is
\[
x+y+\dfrac{60-5x-12y}{13}=6\iff 8x+y=18 .
\]
This line meets $BC$ ($y=0$) at $Q=\left(\dfrac94,0\right)$ and $AB$ at $P=\left(\dfrac{12}7,\dfrac{30}7\right)$ (from $5x+12(18-8x)=60$, $x=\dfrac{156}{91}=\dfrac{12}{7}$), and the points of the triangle on it form the segment $PQ$.
'''+asy(fig,'7cm')+r'''
The distance to $AC$ is $x$, which varies linearly along $PQ$, so its average is the value at the midpoint:
\[
\dfrac12\left(\dfrac{12}7+\dfrac94\right)=\dfrac{48+63}{56}=\dfrac{111}{56}.
\]
Since $\gcd(111,56)=1$, $m+n=\boxed{167}$.''',
'Coordinate geometry|Right triangles|Loci and geometric constraints|Averages and weighted averages',4,
note='"All points are plotted" is read as all points inside or on the triangle (for points outside, the distances to the sides are not well defined in the intended way), and the average is taken uniformly along the resulting segment.')

# ---------------- 1773840 reversed powers of two
b.add(1773840,1,r'''What is the next term of the sequence $61,\ 23,\ 46,\ 821,\ 652,\ 215,\ \dots$? (Hint: $2,4,8,16,32,\dots$.)''',
r'''Reverse the digits of each term: $16,32,64,128,256,512$. These are the powers of two $2^4,\dots,2^9$. The next power is $2^{10}=1024$, and reversing its digits gives $\boxed{4201}$.''',
'Powers of two|Pattern recognition|Digits and bases',2,
note='The hint "wu2481632" (from the post\'s author name) points to the powers of two; it is replaced by the hint 2, 4, 8, 16, 32.')

# ---------------- 1772547 domain
b.add(1772547,1,r'''For which real values of $m$ is $\sqrt{-m}+\sqrt{10-m}$ a real number?''',
r'''Both square roots must be of nonnegative numbers: $-m\ge0$ and $10-m\ge0$, i.e.\ $m\le0$ and $m\le10$. Both hold exactly when $\boxed{m\le0}$.''',
'Radicals|Inequalities',1)

# ---------------- 1773603 AIME clay targets
b.add(1773603,1,r'''In a shooting match, eight clay targets are arranged in two hanging columns of three targets each and one column of two targets. A marksman is to break all the targets according to the following rules: (1) the marksman first chooses a column from which a target is to be broken; (2) the marksman must then break the lowest remaining target in the chosen column. If the rules are followed, in how many different orders can the eight targets be broken?''',
r'''Within each column the order is forced (bottom to top), so an order of breaking is determined by the sequence of column choices: a word with three $A$'s, three $B$'s and two $C$'s, and every such word is possible. The number of words is
\[
\dfrac{8!}{3!\,3!\,2!}=\dfrac{40320}{72}=\boxed{560}.
\]''',
'Multiset permutations|Bijections',3,source=src('AIME',1990,None,8),
note='1990 AIME Problem 8.')

# ---------------- 1772890 sum of 1/k^2
b.add(1772890,1,r'''Prove that
\[
\dfrac1{1^2}+\dfrac1{2^2}+\dfrac1{3^2}+\cdots+\dfrac1{100^2}>1.4 .
\]''',
r'''For $k\ge2$, $k^2<k(k+1)$, so $\dfrac1{k^2}>\dfrac1{k(k+1)}=\dfrac1k-\dfrac1{k+1}$. Therefore
\[
\sum_{k=1}^{100}\dfrac1{k^2}>1+\sum_{k=2}^{100}\left(\dfrac1k-\dfrac1{k+1}\right)=1+\dfrac12-\dfrac1{101}>1+0.5-0.01=1.49>1.4 .
\]
$\blacksquare$ (The sum is about $1.635$.)''',
'Telescoping sums|Inequalities|Bounding and extremal cases',3,
note='The post writes "1,4" (decimal comma) for 1.4.')

# ---------------- 1773142 factor
b.add(1773142,1,r'''Factor $m^{2a+1}-2n^{3a-1}-mn+2m^{2a}n^{3a-2}$, where $a\ge1$ is an integer.''',
r'''Group the terms with $m^{2a}$ and those without:
\[
m^{2a+1}+2m^{2a}n^{3a-2}-mn-2n^{3a-1}=m^{2a}\left(m+2n^{3a-2}\right)-n\left(m+2n^{3a-2}\right),
\]
because $n\cdot2n^{3a-2}=2n^{3a-1}$. Hence
\[
m^{2a+1}-2n^{3a-1}-mn+2m^{2a}n^{3a-2}=\boxed{\left(m^{2a}-n\right)\left(m+2n^{3a-2}\right)}.
\]''',
'Factoring|Exponents|Algebraic expressions and identities',3,
note='The post asks to "simplify" m^(2a+1) - 2n^(3a-1) - mn + 2m^(2n)n^(3a), which does not factor; the last term is read as a typo for 2m^(2a)n^(3a-2), which makes the expression factor by grouping (the intended exercise). Checked symbolically.')

b.save()
