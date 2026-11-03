from qb import *
b=Bank('p228_02')

# ---------------- 1746517 pairwise sums squares
b.add(1746517,1,r'''\begin{enumerate}
\item[(a)] Find a set of four distinct integers such that the sum of any two of them is a perfect square.
\item[(b)] Find a set of four distinct positive integers such that the sum of any two of them is a perfect square, or prove that no such set exists.
\item[(c)] Find a set of five distinct integers such that the sum of any two of them is a perfect square, or prove that no such set exists.
\end{enumerate}''',
r'''\textbf{A method for four numbers.} Suppose $a<b<c<d$ and the six pairwise sums are squares. The three ways of splitting $\{a,b,c,d\}$ into two pairs give the same total:
\[
(a+b)+(c+d)=(a+c)+(b+d)=(a+d)+(b+c)=N .
\]
So $N$ must be a sum of two squares in three ways. Conversely, suppose $N=p^2+u^2=q^2+t^2=r^2+s^2$. Put
\[
a=\dfrac{p^2+q^2-s^2}{2},\quad b=p^2-a,\quad c=q^2-a,\quad d=r^2-a .
\]
Then $a+b=p^2$, $a+c=q^2$, $a+d=r^2$, $b+c=p^2+q^2-2a=s^2$, $b+d=p^2+r^2-2a=r^2+s^2-q^2=t^2$ and $c+d=q^2+r^2-2a=r^2+s^2-p^2=u^2$. All six sums are squares, as long as $a$ is an integer and the four numbers are distinct.

\textbf{(a)} Take $N=325=1^2+18^2=6^2+17^2=10^2+15^2$ and $(p,q,r,s)=(1,6,10,15)$ (so $t=17$, $u=18$). Then $a=\dfrac{1+36-225}{2}=-94$, and we get the set
\[
\boxed{\{-94,\ 95,\ 130,\ 194\}}:
\]
the sums are $1,36,100,225,289,324$, i.e.\ $1^2,6^2,10^2,15^2,17^2,18^2$.

\textbf{(b)} Such a set exists. Take $N=16900=50^2+120^2=66^2+112^2=104^2+78^2$ with $(p,q,r,s)=(50,66,104,78)$ (so $t=112$, $u=120$): $a=\dfrac{2500+4356-6084}{2}=386$, giving
\[
\boxed{\{386,\ 2114,\ 3970,\ 10430\}}.
\]
The sums are $2500=50^2$, $4356=66^2$, $10816=104^2$, $6084=78^2$, $12544=112^2$, $14400=120^2$.

\textbf{(c)} Such a set also exists, even with positive integers:
\[
\boxed{\{7442,\ 28658,\ 148583,\ 177458,\ 763442\}}.
\]
Its ten pairwise sums are
\[
\begin{aligned}
&7442+28658=190^2, && 7442+148583=395^2, && 7442+177458=430^2, && 7442+763442=878^2,\\
&28658+148583=421^2, && 28658+177458=454^2, && 28658+763442=890^2, &&\\
&148583+177458=571^2, && 148583+763442=955^2, && 177458+763442=970^2 . &&
\end{aligned}
\]
(Any four of these five numbers also answer (b), but the example above is much smaller.)''',
'Perfect squares|Construction|Diophantine equations|Systems of linear equations',6,
note='The poster had not solved (b) and (c). Both sets exist; the four-number examples come from the three-way sum-of-two-squares construction in the solution, and the five-number set is a known example. All pairwise sums were verified by computer.')

# ---------------- 1749804 nested roots
b.add(1749804,1,r'''A student claims that $\sqrt[3]{x}=\sqrt{\sqrt{x}}$ and $\sqrt[4]{x}=\sqrt{\sqrt{\sqrt{x}}}$ for every $x\ge0$, ``and so on''. Show that the first claim is false by giving a counterexample, determine for which $x\ge0$ it does hold, and give the correct value of a square root taken $k$ times in succession.''',
r'''For $x\ge0$, $\sqrt{x}=x^{\dfrac12}$, so taking the square root twice gives $\left(x^{\dfrac12}\right)^{\dfrac12}=x^{\dfrac14}=\sqrt[4]{x}$, and taking it $k$ times gives
\[
\underbrace{\sqrt{\sqrt{\cdots\sqrt{x}}}}_{k\text{ roots}}=x^{\dfrac{1}{2^k}}=\sqrt[2^k]{x}.
\]
So $\sqrt{\sqrt{x}}$ is the fourth root, not the cube root, and $\sqrt{\sqrt{\sqrt{x}}}$ is the eighth root. Counterexample: for $x=64$, $\sqrt[3]{64}=4$ but $\sqrt{\sqrt{64}}=\sqrt8=2\sqrt2\ne4$.

The equation $x^{\dfrac13}=x^{\dfrac14}$ holds for $x=0$ and $x=1$. For $x>0$, $x\ne1$, it would give $x^{\dfrac13-\dfrac14}=x^{\dfrac{1}{12}}=1$, so $x=1$, a contradiction. Hence $\boxed{\sqrt[3]{x}=\sqrt{\sqrt x}\text{ only for }x=0\text{ and }x=1}$, and $k$ successive square roots give the $2^k$-th root.''',
'Radicals|Exponents|Counterexamples',2,
note='The post asks whether the cube root equals the double square root, the fourth root the triple square root, and so on; the record asks for a counterexample and the correct rule (the double square root is the fourth root).')

# ---------------- 1750183 radical equation
b.add(1750183,1,r'''Solve for real $x$:
\[
\dfrac{1+x^2}{1+\sqrt{1+x^2}}+\dfrac{1-x^2}{1-\sqrt{1-x^2}}=1 .
\]''',
r'''We need $|x|\le1$, and $x\ne0$ (otherwise the second denominator is $0$). Put $a=\sqrt{1+x^2}$ and $b=\sqrt{1-x^2}$, so $a^2-1=x^2=1-b^2$. Then
\[
\dfrac{a^2}{1+a}=\dfrac{a^2(a-1)}{a^2-1}=\dfrac{a^2(a-1)}{x^2},\qquad
\dfrac{b^2}{1-b}=\dfrac{b^2(1+b)}{1-b^2}=\dfrac{b^2(1+b)}{x^2}.
\]
Multiplying the equation by $x^2$ gives $a^3-a^2+b^3+b^2=x^2$. Since $a^2-b^2=2x^2$, this is
\[
a^3+b^3=3x^2 .
\]
Write $t=x^2\in(0,1]$: $(1+t)^{\dfrac32}+(1-t)^{\dfrac32}=3t$. Both sides are positive, so squaring is reversible:
\[
(1+t)^3+(1-t)^3+2(1-t^2)^{\dfrac32}=9t^2\iff 2+6t^2+2(1-t^2)^{\dfrac32}=9t^2 .
\]
Now let $w=\sqrt{1-t^2}\in[0,1)$, so $t^2=1-w^2$:
\[
2+6(1-w^2)+2w^3=9(1-w^2)\iff 2w^3+3w^2-1=0\iff(w+1)^2(2w-1)=0 .
\]
Since $w\ge0$, $w=\dfrac12$, so $t^2=\dfrac34$ and $t=x^2=\dfrac{\sqrt3}{2}$. Every step was reversible, so
\[
\boxed{x=\pm\sqrt{\dfrac{\sqrt3}{2}}=\pm\dfrac{\sqrt[4]{12}}{2}\approx\pm0.9306}.
\]''',
'Radical equations|Substitution|Factoring|Polynomial roots',5,
note='Solution x^2 = sqrt(3)/2 checked numerically in the original equation (no other root in [-1, 1]).')

# ---------------- 1750115 units digit 13^2003
b.add(1750115,1,r'''What is the units digit of $13^{2003}$? Use modular arithmetic rather than listing a pattern of units digits.''',
r'''The units digit is the remainder modulo $10$. Since $13\equiv3\pmod{10}$,
\[
13^{2003}\equiv3^{2003}\pmod{10}.
\]
Now $3^4=81\equiv1\pmod{10}$, and $2003=4\cdot500+3$, so
\[
3^{2003}=\left(3^4\right)^{500}\cdot3^3\equiv1^{500}\cdot27\equiv7\pmod{10}.
\]
The units digit is $\boxed{7}$.''',
'Units digits and last digits|Modular exponentiation|Remainders and congruences',2,
note='The poster says the problem is on the 2003 AMC 10A; this was not confirmed, so no source is recorded.')

# ---------------- 1748211 lattice points hyperbola
b.add(1748211,1,r'''How many lattice points lie on the hyperbola $x^2-y^2=2000^2$?''',
r'''Write $(x-y)(x+y)=2000^2=2^8\cdot5^6$. The factors $x-y$ and $x+y$ have the same parity (their sum is $2x$); their product is even, so both are even. Put $x-y=2m$ and $x+y=2n$; then
\[
mn=2^6\cdot5^6=10^6,
\]
and conversely every pair of integers $(m,n)$ with $mn=10^6$ gives the lattice point $(x,y)=(m+n,\,n-m)$, different pairs giving different points. The number $10^6$ has $(6+1)(6+1)=49$ positive divisors, and $m$ may be any positive or negative divisor (then $n=\dfrac{10^6}{m}$), so there are $2\cdot49=\boxed{98}$ lattice points.''',
'Lattice points|Hyperbolas|Divisor counting|Difference of squares|Parity',4,
note='The poster got 32 and a friend 98; 98 is correct. Checked by brute force.')

# ---------------- 1750121 6^1999 mod 37
b.add(1750121,1,r'''What is the remainder when $6^{1999}$ is divided by $37$?''',
r'''Since $6^2=36\equiv-1\pmod{37}$, we get $6^4\equiv1\pmod{37}$. As $1999=4\cdot499+3$,
\[
6^{1999}=\left(6^4\right)^{499}\cdot6^3\equiv216=5\cdot37+31\equiv31\pmod{37}.
\]
The remainder is $\boxed{31}$.''',
'Modular exponentiation|Remainders and congruences',2)

# ---------------- 1750117 gcd(a,a+n)
b.add(1750117,1,r'''Prove that for a positive integer $n$ and any integer $a$, $\gcd(a,a+n)$ divides $n$. Deduce that $\gcd(a,a+1)=1$.''',
r'''Let $d=\gcd(a,a+n)$. Then $d\mid a$ and $d\mid a+n$, so $d$ divides their difference $(a+n)-a=n$. For $n=1$ this says $d\mid1$, and since $d$ is positive, $\gcd(a,a+1)=1$. $\blacksquare$''',
'HCF and LCM|Divisibility',1,
note='Burton, Elementary Number Theory, exercise.')

# ---------------- 1750107 three proofs
b.add(1750107,1,r'''Prove that the sum of the squares of two odd integers cannot be a perfect square.''',
r'''An odd integer is $2k+1$, and $(2k+1)^2=4k(k+1)+1\equiv1\pmod4$. So the sum of two odd squares is $\equiv2\pmod4$. But every perfect square is $\equiv0$ or $1\pmod4$ (even squares are multiples of $4$, odd squares are $\equiv1$). Hence the sum is not a perfect square. $\blacksquare$''',
'Perfect squares|Remainders and congruences|Parity',2,
note='Burton, Elementary Number Theory, exercise; problem 1 of the post.')
b.add(1750107,2,r'''Prove that the product of four consecutive integers is $1$ less than a perfect square.''',
r'''$n(n+1)(n+2)(n+3)=(n^2+3n)(n^2+3n+2)=(n^2+3n+1)^2-1$. $\blacksquare$''',
'Algebraic expressions and identities|Perfect squares',2,
note='Repeat of an earlier record (aliased).')
b.add(1750107,3,r'''Prove that the difference of two consecutive cubes is never divisible by $2$.''',
r'''For any integer $n$,
\[
(n+1)^3-n^3=3n^2+3n+1=3n(n+1)+1 .
\]
One of $n$ and $n+1$ is even, so $3n(n+1)$ is even and the difference is odd. Hence it is never divisible by $2$. $\blacksquare$''',
'Perfect cubes|Parity|Algebraic expressions and identities',1)

# ---------------- 1749896 continued fraction (alias); nested radical dropped
b.add(1749896,1,r'''Evaluate the infinite continued fraction
\[
\dfrac{1}{2+\dfrac{3}{4+\dfrac{5}{6+\cdots}}}.
\]''',
r'''Numerically the truncations converge to $0.379731954\ldots$; in closed form the value is $\dfrac{\sqrt{2e}}{\sqrt\pi\,\operatorname{erfi}\left(\dfrac{1}{\sqrt2}\right)}-1$ (see the earlier record).''',
'Continued fractions|Sequences and series',6,
note='Problem 1 of the post. Repeat of an earlier record (aliased). Problem 2 (the nested radical sqrt(1+sqrt(2+sqrt(3+...)))) has no known closed form and is dropped.')

# ---------------- 1749330 five primes AP
b.add(1749330,1,r'''An arithmetic progression is formed by five prime numbers. What is the least possible sum of those five numbers?''',
r'''Let the primes be $a,a+d,\dots,a+4d$ with $d>0$.

If $a=2$, the other four terms are $2+kd$; they cannot all be odd primes unless $d$ is odd, but then $2+2d$ is even and greater than $2$. So $a$ is odd, and then $d$ must be even (otherwise $a+d$ is even).

If $3\nmid d$, then $a,a+d,a+2d$ have different remainders modulo $3$, so one of them is divisible by $3$ and must equal $3$; it must be $a=3$ (it is the smallest). But then $a+d$ and $a+2d$ have the two nonzero remainders, while $a+3d\equiv0\pmod3$ and $a+3d>3$, a contradiction. Hence $6\mid d$.

With $a\ge5$ (since $a=3$ would make $3+d$ divisible by $3$) and $d\ge6$, the sum is $5a+10d\ge25+60=85$. Equality holds for $5,11,17,23,29$, which are all prime. The least sum is $\boxed{85}$.''',
'Prime numbers|Arithmetic sequences|Remainders and congruences|Bounding and extremal cases',4,source=src('MATHCOUNTS',2014,'School',24,rnd='Sprint'),
note='2014 MATHCOUNTS School Sprint #24, as titled. The poster\'s answer 85 is correct. Checked by search.')

# ---------------- 1749903 Pascal (alias)
b.add(1749903,1,r'''Prove Pascal's identity: for integers $1\le k\le n$,
\[
\dbinom{n}{k}=\dbinom{n-1}{k-1}+\dbinom{n-1}{k}.
\]''',
r'''Count the $k$-element subsets of $\{1,2,\dots,n\}$. Those containing $n$ correspond to the $(k-1)$-element subsets of $\{1,\dots,n-1\}$, and those not containing $n$ are the $k$-element subsets of $\{1,\dots,n-1\}$. Adding gives the identity. $\blacksquare$''',
'Combinatorial identities and binomial coefficients|Pascal\'s triangle|Double counting',2,
note='"Prove Pascal\'s triangle" read as proving the rule that generates it (Pascal\'s identity). Repeat of an earlier record (aliased).')

# ---------------- 1748599 four handbook problems
b.add(1748599,1,r'''Blake has a repertoire of $15$ songs, of which $5$ are acoustic. In his concert he plans to perform $10$ distinct songs, of which $4$ will be acoustic. He wants to perform the $4$ acoustic songs consecutively in the second half of the concert, but does not want to end the concert with an acoustic song. How many different sequences of songs can Blake perform?''',
r'''The concert has positions $1$ to $10$; the second half is positions $6$ to $10$. Four consecutive positions inside $6$--$10$ are $6$--$9$ or $7$--$10$, and the second would end the concert with an acoustic song. So the acoustic songs occupy positions $6$--$9$.
\begin{itemize}
\item Acoustic songs in positions $6$--$9$: choose and order $4$ of the $5$ acoustic songs, $5\cdot4\cdot3\cdot2=120$ ways.
\item The other $6$ positions ($1$--$5$ and $10$): choose and order $6$ of the $10$ non-acoustic songs, $10\cdot9\cdot8\cdot7\cdot6\cdot5=151200$ ways.
\end{itemize}
The number of sequences is $120\cdot151200=\boxed{18144000}$.''',
'Permutations|Arrangements with restrictions|Multiplication principle',3,source=src('MATHCOUNTS',None,'Handbook',None))
b.add(1748599,2,r'''The Bobcats had a win-loss record of $41$--$23$ before their star player, Melissa, got injured. Melissa did not play in any more games, and the Bobcats finished the season with an overall win-loss record of $54$--$34$. What is the absolute difference, in percentage points, between the Bobcats' winning percentages with and without Melissa? Express your answer to the nearest whole number.''',
r'''With Melissa the record was $41$--$23$: $\dfrac{41}{64}=64.0625\%$. Without her the team went $(54-41)$--$(34-23)=13$--$11$: $\dfrac{13}{24}\approx54.1667\%$. The difference is about $9.896$ percentage points, so the answer is $\boxed{10}$.''',
'Percentages|Fractions',2,source=src('MATHCOUNTS',None,'Handbook',None))
b.add(1748599,3,r'''On a test, Walter scored $86$, Bev scored $72$, Claire scored $61$ and Rachel scored $93$. Tyler did not remember his score, but he knew that it was both the mean and the median of all five students' scores. What was Tyler's score?''',
r'''If Tyler scored $T$, the mean is $\dfrac{86+72+61+93+T}{5}=\dfrac{312+T}{5}$. Setting it equal to $T$ gives $312+T=5T$, so $T=78$. Then the scores in order are $61,72,78,86,93$, whose median is indeed $78$. Tyler scored $\boxed{78}$.''',
'Mean|Median|Linear equations',2,source=src('MATHCOUNTS',None,'Handbook',None))
b.add(1748599,4,r'''At Randolf's furniture store, a standard breakfast table costs $\$1000$. Karthik wants to buy the luxury version, which costs $35\%$ more than the standard one, and he has a coupon for a $15\%$ discount on his purchase. After a $6\%$ sales tax is applied to the discounted price, how much will Karthik pay for the luxury table?''',
r'''The luxury table costs $1000\cdot1.35=\$1350$. After the discount it costs $1350\cdot0.85=\$1147.50$, and with tax $1147.50\cdot1.06=\boxed{\$1216.35}$.''',
'Percentages|Money and currency|Decimals',1,source=src('MATHCOUNTS',None,'Handbook',None))

# ---------------- 1749760 three dice
b.add(1749760,1,r'''What is the expected value of the sum of the numbers rolled on three fair six-sided dice?''',
r'''One die has expected value $\dfrac{1+2+\cdots+6}{6}=\dfrac{21}{6}=3.5$. By linearity of expectation the sum of three dice has expected value $3\cdot3.5=\boxed{10.5}$.''',
'Expected value|Dice probability',1,
note='The poster recalls it from a 2014 mathleague.org Sprint test; the source is not recorded since the wording is from memory.')

# ---------------- 1749553 gifts (alias)
b.add(1749553,1,r'''In how many ways can six different gifts be given to five different children so that each child receives at least one gift and each gift is given to exactly one child?''',
r'''Exactly one child gets two gifts. Choose the pair of gifts that go together, $\dbinom62=15$ ways; then hand out the five ``bundles'' to the five children, $5!=120$ ways. Total $15\cdot120=\boxed{1800}$.''',
'Distributions and integer solutions|Combinations|Permutations',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1749495 space diagonal
fig=r'''real a=4,c=2.4,bb=2.2;pair v=bb*(0.55,0.4);
pair P0=(0,0),P1=(a,0),P2=(a,c),P3=(0,c);
pair Q0=P0+v,Q1=P1+v,Q2=P2+v,Q3=P3+v;
draw(P0--P1--P2--P3--cycle,linewidth(0.9));
draw(P1--Q1--Q2--Q3--P3,linewidth(0.9));draw(P2--Q2,linewidth(0.9));
draw(P0--Q0,dashed);draw(Q0--Q1,dashed);draw(Q0--Q3,dashed);
draw(P0--Q1,blue+dashed+linewidth(0.8));
draw(P0--Q2,red+linewidth(1.1));
dot(P0);dot(Q2);
label("$P$",P0,SW);label("$Q$",Q2,NE);
label("$a$",(P0+P1)/2,S);label("$b$",(P1+Q1)/2,SE);label("$c$",(Q1+Q2)/2,E);
label("$e$",P0+0.6*(Q1-P0),S,blue);'''
b.add(1749495,1,r'''A rectangular box (rectangular prism) has edge lengths $a$, $b$ and $c$. Find the distance between two vertices that are farthest apart (the length of a space diagonal). What is it for a cube of edge $a$?''',
r'''Let $P$ be a corner of the box and $Q$ the opposite corner. Walk from $P$ along the bottom face to the corner below $Q$: this is a diagonal of an $a\times b$ rectangle, of length $e=\sqrt{a^2+b^2}$ by the Pythagorean theorem. That diagonal is perpendicular to the vertical edge of length $c$ that ends at $Q$, so by the Pythagorean theorem again
\[
PQ=\sqrt{e^2+c^2}=\boxed{\sqrt{a^2+b^2+c^2}}.
\]
'''+asy(fig,'6cm')+r'''
No two vertices are farther apart: two vertices differ in $0$, $1$, $2$ or $3$ of the coordinates (in a coordinate system along the edges), giving distances $0$, an edge, a face diagonal or the space diagonal, and the space diagonal is the largest. For a cube of edge $a$ the space diagonal is $\sqrt{3a^2}=a\sqrt3$.''',
'Cubes and rectangular prisms|Pythagorean theorem|Solid geometry',2)

# ---------------- 1749683 two modular problems
b.add(1749683,1,r'''Using modular arithmetic (not a pattern of remainders), find the remainder when $5^{2012}$ is divided by $7$.''',
r'''Since $7$ is prime and $7\nmid5$, Fermat's little theorem gives $5^6\equiv1\pmod7$. (Directly: $5^2=25\equiv4$, $5^3\equiv20\equiv6\equiv-1$, so $5^6\equiv1$.) As $2012=6\cdot335+2$,
\[
5^{2012}=\left(5^6\right)^{335}\cdot5^2\equiv25\equiv4\pmod7 .
\]
The remainder is $\boxed{4}$.''',
'Modular exponentiation|Fermat\'s little theorem|Remainders and congruences',2)
b.add(1749683,2,r'''Using modular arithmetic, find the units digit of $13^{2012}$.''',
r'''$13^{2012}\equiv3^{2012}=\left(3^4\right)^{503}=81^{503}\equiv1\pmod{10}$, so the units digit is $\boxed{1}$.''',
'Units digits and last digits|Modular exponentiation',2,
note='Repeat of an earlier record (aliased).')

# ---------------- 1749222 digits 2 and 5
b.add(1749222,1,r'''How many three-digit positive integers have all of their digits equal to $2$ or $5$?''',
r'''Each of the three digits can be chosen independently as $2$ or $5$ (neither is $0$, so the hundreds digit causes no problem). By the multiplication principle there are $2\cdot2\cdot2=\boxed{8}$ such integers: $222,225,252,255,522,525,552,555$.''',
'Multiplication principle|Digit problems',1)

# ---------------- 1749682 texts
b.add(1749682,1,r'''Max's cell phone plan charges $\$0.13$ for each text message sent or received. Max was charged $\$7.41$ in a month in which he sent $15$ more texts than he received. How many texts did Max send?''',
r'''Max sent or received $\dfrac{7.41}{0.13}=57$ texts in all. If he sent $s$ and received $r$, then $s+r=57$ and $s-r=15$, so $2s=72$ and $s=\boxed{36}$ (he received $21$).''',
'Systems of linear equations|Money and currency|Decimals',1)

# ---------------- 1749365 cats and dogs
b.add(1749365,1,r'''An animal shelter spends $\$2.35$ per day to care for each cat and $\$5.50$ per day to care for each dog. If $\$89.50$ is spent in one day caring for a total of $22$ cats and dogs, how much was spent that day caring for all of the cats?''',
r'''Let there be $c$ cats and $22-c$ dogs. Then
\[
2.35c+5.50(22-c)=89.50\ \Longrightarrow\ 121-3.15c=89.50\ \Longrightarrow\ c=10 .
\]
So there are $10$ cats and $12$ dogs (check: $23.50+66=89.50$), and the cats cost $10\cdot2.35=\boxed{\$23.50}$.''',
'Linear equations|Money and currency|Decimals',2,
note='"Per day" is read as the cost of one day; the total 89.50 is for that day.')

# ---------------- 1749458 increasing/decreasing numbers
b.add(1749458,1,r'''For an integer $n\ge2$, find formulas for
\begin{enumerate}
\item[(a)] the number of $n$-digit positive integers whose digits are strictly increasing from left to right;
\item[(b)] the number of $n$-digit positive integers whose digits are strictly decreasing from left to right.
\end{enumerate}''',
r'''\textbf{(a)} The digit $0$ cannot appear: it would have to be the leading digit. Any set of $n$ distinct digits from $\{1,\dots,9\}$ can be written in increasing order in exactly one way, and this gives a valid $n$-digit number. So the count is $\boxed{\dbinom9n}$ (which is $0$ for $n\ge10$).

\textbf{(b)} Any set of $n$ distinct digits from $\{0,1,\dots,9\}$ written in decreasing order gives exactly one number; since $n\ge2$, the largest digit, which comes first, is not $0$. So the count is $\boxed{\dbinom{10}{n}}$ (for example $\dbinom{10}{2}=45$ two-digit numbers such as $10$ and $98$). (For $n=1$ the convention matters: the nine one-digit numbers $1$--$9$, not $\dbinom{10}1=10$.)''',
'Combinations|Digit problems|Bijections',3,
note='The post asks for formulas; the record states them for n >= 2 (a one-digit number counts as both, and 0 is excluded for n = 1).')

# ---------------- 1749150 16 a^2 64
b.add(1749150,1,r'''If $16\cdot a^2\cdot64=(4\cdot b)^2$, where $a$ and $b$ are positive integers, then $b$ is how many times as large as $a$?''',
r'''The left side is $1024a^2=(32a)^2$ and the right side is $(4b)^2$. Since $a,b>0$, $32a=4b$, so $b=8a$: $b$ is $\boxed{8}$ times as large as $a$.''',
'Exponents|Algebraic manipulation',1,
note='The x signs in the post are multiplication signs. "How many times greater" is read as "how many times as large".')

# ---------------- 1749331 strips
fig=r'''real r3=sqrt(3);pair u=dir(30);
pair O=(0,0),B=(4,0),C=(4+2r3,2),D=(2r3,2);
fill(O--B--C--D--cycle,lightgray);
draw((-3,0)--(12,0),linewidth(0.9));draw((-3,2)--(12,2),linewidth(0.9));
draw(O-3.4*u--O+6*u,linewidth(0.9));draw(B-6.4*u--B+6*u,linewidth(0.9));
draw(O--B--C--D--cycle,red+linewidth(0.9));
draw(arc(O,1.1,0,30),linewidth(0.6));label("$30^\circ$",2.15*dir(14));
pair n=(sin(pi/6),-cos(pi/6));pair p=O-2.6*u;
draw(p--p+2n,Arrows(4));label("$2$",p+n,-1.5*u);
draw((-2,0)--(-2,2),Arrows(4));label("$2$",(-2,1),W);
label("$4$",(2,0),S);label("$4$",(O+D)/2,dir(120));
label("$A$",O,dir(250));label("$B$",B,dir(-60));label("$C$",C,dir(60));label("$D$",D,dir(110));'''
b.add(1749331,1,r'''Two long strips of paper are each $2$ inches wide, and they overlap so that the angle between the strips is $30^\circ$. What is the number of square inches in the area of the parallelogram formed by the overlap?''',
r'''Let the overlap be $ABCD$, with $AB$ along an edge of the first strip and $AD$ along an edge of the second. The distance between the parallel sides $AB$ and $DC$ is the width $2$ of the first strip, and the angle at $A$ is $30^\circ$. Side $AD$ crosses the first strip, so its length satisfies $AD\sin30^\circ=2$, giving $AD=4$. In the same way, $AB$ crosses the second strip: $AB\sin30^\circ=2$ and $AB=4$. (So the overlap is a rhombus.)
'''+asy(fig,'7cm')+r'''
The area is base times height: $AB\cdot2=4\cdot2=\boxed{8}$ square inches.''',
'Parallelograms|Rhombi|Lengths, perimeter, and area|Special right triangles',3,source=src('MATHCOUNTS',2014,'School',26,rnd='Sprint'),
note='2014 MATHCOUNTS School Sprint #26, as titled.')

# ---------------- 1749345 11-3x
b.add(1749345,1,r'''If $11-3x$ is $4$ less than $13$, what is the value of $6x$?''',
r'''$11-3x=13-4=9$, so $3x=2$ and $6x=\boxed{4}$.''',
'Linear equations',1)

# ---------------- 1748689 trapezoid
fig=r'''pair D=(0,0),C=(8,0),A=(1.5,4),B=(5,4);
real t=0.55;pair Ep=t*A;
real s=(1-t)*8/(t*(B.x-A.x)+(1-t)*8);pair P=C+s*(B-C);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(Ep--B,blue+linewidth(0.9));draw(D--P,blue+linewidth(0.9));
draw(Ep--C,red+dashed+linewidth(0.9));draw(A--P,red+dashed+linewidth(0.9));
dot(Ep);dot(P);
label("$A$",A,NW);label("$B$",B,NE);label("$C$",C,SE);label("$D$",D,SW);
label("$E$",Ep,W);label("$P$",P,E);'''
b.add(1748689,1,r'''In trapezoid $ABCD$ with $AB\parallel DC$, point $E$ lies on side $AD$ and point $P$ lies on side $BC$ such that $EB\parallel DP$. Prove that $EC\parallel AP$.''',
r'''Use coordinates with $DC$ on the $x$-axis: $D=(0,0)$, $C=(c,0)$, $A=(a,h)$, $B=(b,h)$ with $c>0$ and $h>0$. Write $E=tA=(ta,th)$ and $P=C+s(B-C)=\bigl(c+s(b-c),\,sh\bigr)$ with $0<t,s<1$.

Two vectors $(p_1,p_2)$ and $(q_1,q_2)$ are parallel exactly when $p_1q_2-p_2q_1=0$.

\textbf{The hypothesis.} $\vec{EB}=\bigl(b-ta,\,(1-t)h\bigr)$ and $\vec{DP}=\bigl(c+s(b-c),\,sh\bigr)$, so $EB\parallel DP$ means
\[
(b-ta)sh-(1-t)h\bigl(c+s(b-c)\bigr)=0 .
\]
Dividing by $h$ and expanding, $sb-sta-(1-t)c-(1-t)sb+(1-t)sc=0$, i.e.
\[
st(b-a)+(1-t)(s-1)c=0. \tag{1}
\]

\textbf{The claim.} $\vec{EC}=(c-ta,\,-th)$ and $\vec{AP}=\bigl(c+s(b-c)-a,\,(s-1)h\bigr)$, so $EC\parallel AP$ means
\[
(c-ta)(s-1)h+th\bigl(c+s(b-c)-a\bigr)=0 .
\]
Dividing by $h$ and expanding: $cs-c-tas+ta+tc+tsb-tsc-ta=st(b-a)+c(s-1)-tc(s-1)$, which equals
\[
st(b-a)+(1-t)(s-1)c .
\]
This is exactly the left side of (1), which is $0$. Hence $EC\parallel AP$. $\blacksquare$
'''+asy(fig,'6.5cm')+r'''
In the figure the given parallel segments $EB$ and $DP$ are solid blue, and the segments $EC$ and $AP$, proved parallel, are dashed red.''',
'Trapezoids|Parallel lines|Coordinate bashing|Coordinate geometry',4,
note='E in (AD), P in (BC) read as points on the open sides. The coordinate proof covers every trapezoid (including parallelograms, where AD and BC do not meet); checked numerically for random trapezoids.')

# ---------------- 1749316 x/8+y/5
b.add(1749316,1,r'''Positive integers $x$ and $y$ satisfy $\dfrac x8+\dfrac y5=\dfrac{31}{40}$. What is the value of $x+y$?''',
r'''Multiplying by $40$ gives $5x+8y=31$. Since $x\ge1$, $8y\le26$, so $y\in\{1,2,3\}$: $y=1$ gives $5x=23$, $y=3$ gives $5x=7$ (no integer $x$), and $y=2$ gives $x=3$. The only solution is $(x,y)=(3,2)$, so $x+y=\boxed{5}$.''',
'Linear Diophantine equations|Fractions',2)

# ---------------- 1749176 handbook warm-up 7
b.add(1749176,92,r'''A deck of $14$ cards numbered $1$ through $14$ is dealt to Ken and Gunther so that each gets $7$ cards. Each player's score is the sum of his card values, and the player with the lower score wins. How many different winning scores are possible?''',
r'''The two scores add up to $1+2+\cdots+14=105$, which is odd, so there is never a tie, and the winning score $w$ satisfies $w<105-w$, i.e.\ $w\le52$. The smallest possible score is $1+2+\cdots+7=28$.

Every integer from $28$ to $52$ is a possible score: start from $\{1,\dots,7\}$ (sum $28$) and repeatedly replace some card $k$ by $k+1$ when $k+1$ is not yet in the hand; each step raises the sum by $1$, and this can be continued until the hand is $\{8,\dots,14\}$ (sum $77$). So the winning scores are exactly $28,29,\dots,52$, and there are $52-28+1=\boxed{25}$ of them.''',
'Bounding and extremal cases|Summation|Construction',3,source=src('MATHCOUNTS',None,'Handbook',92,rnd='Warm-Up 7'),
note='MATHCOUNTS Handbook Warm-Up 7 #92; the posted answer 25 is correct. Checked by enumerating all 3432 hands.')
b.add(1749176,97,r'''Freddie Frog traveled $29$ yards in $261$ jumps, at a constant distance per jump. After hurting a toe, her distance per jump decreased by $1$ inch. How many more than $261$ jumps will it take her to travel another $29$ yards with the hurt toe?''',
r'''$29$ yards is $29\cdot36=1044$ inches, so each jump was $\dfrac{1044}{261}=4$ inches. With the hurt toe each jump is $3$ inches, so $29$ yards takes $\dfrac{1044}{3}=348$ jumps, which is $348-261=\boxed{87}$ more.''',
'Unit conversion|Rates',2,source=src('MATHCOUNTS',None,'Handbook',97,rnd='Warm-Up 7'),
note='MATHCOUNTS Handbook Warm-Up 7 #97; the posted answer 87 is correct.')
b.add(1749176,99,r'''How many ways are there to put twelve identical donuts into three differently coloured boxes if each box must contain at least two donuts?''',
r'''Put two donuts in each box first. The remaining $6$ donuts can be distributed freely: the number of solutions of $x_1+x_2+x_3=6$ in nonnegative integers is, by stars and bars, $\dbinom{6+2}{2}=\boxed{28}$.''',
'Stars and bars|Distributions and integer solutions',2,source=src('MATHCOUNTS',None,'Handbook',99,rnd='Warm-Up 7'),
note='MATHCOUNTS Handbook Warm-Up 7 #99; the posted answer 28 is correct.')

b.save()
