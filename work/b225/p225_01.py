from qb import *
b=Bank('p225_01')

# ---------------- 1763997 Kangaroo "yield" = product of digits
b.add(1763997,1,r'''The ``yield'' of $36$ equals $18$, the ``yield'' of $325$ equals $30$, the ``yield'' of $45$ equals $20$, and the ``yield'' of $30$ equals $0$. Following the same rule, what is the ``yield'' of $531$?''',
r'''The examples fit the rule ``multiply the digits'':
\[
3\cdot6=18,\qquad 3\cdot2\cdot5=30,\qquad 4\cdot5=20,\qquad 3\cdot0=0 .
\]
The last example is a useful check: a yield of $0$ from $30$ rules out rules such as adding the digits. So the yield of $531$ is $5\cdot3\cdot1=\boxed{15}$.''',
'Pattern recognition|Digits and bases|Whole-number operations',1,source=src('Math Kangaroo',1999,'Level 5-6',26),
note='The rule (product of the digits) is inferred from the four examples, as intended.')

# ---------------- 1766350 1, 5, 21, 85
b.add(1766350,1,r'''The sequence $1,5,21,85,\dots$ has differences $4,16,64,\dots$ between consecutive terms, the successive powers of $4$. Find a formula for its $n$th term $a_n$, and use it to find $a_{8}$.''',
r'''By the description, $a_1=1$ and $a_{k+1}-a_k=4^k$. Adding the differences,
\[
a_n=1+4+4^2+\cdots+4^{n-1}=\dfrac{4^n-1}{4-1}=\dfrac{4^n-1}{3},
\]
by the formula for a geometric series. Check: $\dfrac{4-1}{3}=1$, $\dfrac{16-1}{3}=5$, $\dfrac{64-1}{3}=21$, $\dfrac{256-1}{3}=85$. Hence $a_n=\boxed{\dfrac{4^n-1}{3}}$ and $a_8=\dfrac{65536-1}{3}=\boxed{21845}$.''',
'Geometric sequences|Sequences and series|Summation|Pattern recognition',2,
note='The post asks whether there is an equation for 1, 5, 21, 85, ...; the record asks for the general term and a sample value.')

# ---------------- 1766101 perfect square factors of 18000
b.add(1766101,1,r'''How many positive factors of $18000$ are perfect squares? List them.''',
r'''Factor: $18000=2^4\cdot3^2\cdot5^3$. A factor $2^a3^b5^c$ is a perfect square exactly when $a,b,c$ are all even, so $a\in\{0,2,4\}$, $b\in\{0,2\}$ and $c\in\{0,2\}$. That gives $3\cdot2\cdot2=\boxed{12}$ square factors:
\[
1,\ 4,\ 16,\ 9,\ 36,\ 144,\ 25,\ 100,\ 400,\ 225,\ 900,\ 3600 .
\]''',
'Perfect squares|Prime factorisation|Divisor counting|Factors and multiples',2,
note='"Perfect factors" read as perfect square factors. The poster listed exactly these 12 and asked which were missing; none are.')

# ---------------- 1766239 |5-12i|
b.add(1766239,1,r'''Find the absolute value $|5-12i|$ of the complex number $5-12i$. A student writes $5-12i=5-12\sqrt{-1}=5+\sqrt{12}\approx8.46$. What is wrong with this?''',
r'''The absolute value of $a+bi$ is its distance from $0$ in the complex plane, $|a+bi|=\sqrt{a^2+b^2}$. So
\[
|5-12i|=\sqrt{5^2+(-12)^2}=\sqrt{169}=\boxed{13}.
\]
The student's steps are wrong in two ways. First, $12\sqrt{-1}=12i$ is not a real number, and $-12i$ cannot be rewritten as $+\sqrt{12}$ (that step treats $\sqrt{-1}$ as $-1$ and also replaces $12$ by $\sqrt{12}$). Second, $5-12i$ itself is not a real number at all, so its absolute value is not found by simplifying it to a real number; it is the length $\sqrt{a^2+b^2}$.''',
'Complex numbers|Pythagorean triples|Radicals',1,
note='The post shows the wrong working (answer about 8.6); the record asks for |5 - 12i| = 13 and for the error.')

# ---------------- 1763568 cube ending in ddd; power of 2
b.add(1763568,1,r'''Let $N$ be the smallest positive perfect cube whose decimal representation ends in at least three identical nonzero digits. Compute the remainder when $N$ is divided by $1000$.''',
r'''Let $N=n^3$ end in $ddd$ with $1\le d\le9$, i.e.\ $n^3\equiv111d\pmod{1000}$.

\textbf{Even $d$.} Then $n$ is even, so $8\mid n^3$ and $8\mid111d$; as $111$ is odd, $8\mid d$, so $d=8$. Write $n=2m$: $8m^3\equiv888\pmod{1000}$ means $m^3\equiv111\pmod{125}$.

\textbf{$d=5$.} Then $5\mid n$, so $125\mid n^3$, but $555\not\equiv0\pmod{125}$. Impossible.

\textbf{$d=1,3,7,9$.} Then $n$ is odd and prime to $5$. Building up $n$ digit by digit from the last digit of a cube (the last digit of $n^3$ determines the last digit of $n$, then the tens digit of $n^3$ determines the tens digit of $n$, and so on), the solutions are
\[
n\equiv471,\ 477,\ 753,\ 999\pmod{1000}\quad\text{for }d=1,3,7,9,
\]
e.g.\ $471^3=104487111$; so every such $n$ is at least $471$.

\textbf{$d=8$.} The same digit-by-digit process gives $n\equiv192\pmod{250}$: the cube ends in $8$ only if $n$ ends in $2$; $(10a+2)^3\equiv8+120a\pmod{100}$ ends in $88$ only if $2a\equiv8\pmod{10}$, i.e.\ $n\equiv42$ or $92\pmod{100}$; checking the hundreds digit, $42^3=74088$, $92^3=778688$, $142^3=2863288$, $192^3=7077888$, and $192$ is the first that works.

So the smallest $n$ is $192$, $N=192^3=7077888$, and the remainder is $\boxed{888}$.''',
'Perfect cubes|Remainders and congruences|Units digits and last digits|Casework',5,
note='Checked by direct search: 192 is the least n whose cube ends in three equal nonzero digits.')
b.add(1763568,2,r'''Suppose $2^k$ is the largest power of $2$ that divides
\[
\dfrac{1!\cdot2!\cdot3!\cdots100!}{(1!)^2\cdot(3!)^2\cdot(5!)^2\cdots(99!)^2}.
\]
Compute the remainder when $k$ is divided by $1000$.''',
r'''Group the factorials in consecutive pairs $(2j-1)!\,(2j)!$ for $j=1,\dots,50$, and use one factor $\left((2j-1)!\right)^2$ of the denominator for each pair:
\[
\dfrac{(2j-1)!\,(2j)!}{\left((2j-1)!\right)^2}=\dfrac{(2j)!}{(2j-1)!}=2j .
\]
So the quotient is $\displaystyle\prod_{j=1}^{50}2j=2^{50}\cdot50!$. By Legendre's formula the exponent of $2$ in $50!$ is $25+12+6+3+1=47$, so $k=50+47=97$ and the remainder is $\boxed{97}$.''',
'Factorials|Prime factorisation|Floor and ceiling functions|Powers of two',3)

# ---------------- 1765675 Heronian, longest side 17 (alias)
b.add(1765675,1,r'''A Heronian triangle is a triangle with integer side lengths and integer area. What is the smallest possible area of a Heronian triangle with longest side $17$?''',
r'''Let the other sides be $a\le b\le17$ with $a+b>17$. Heron's formula gives $16K^2=(a+b+17)(a+b-17)(17-a+b)(17+a-b)$, and checking the finitely many pairs shows that $K$ is an integer only for $(a,b)=(8,15),(9,10),(10,17),(16,17),(17,17)$ and a few others, the least area being that of the $9$-$10$-$17$ triangle: $s=18$, $K=\sqrt{18\cdot9\cdot8\cdot1}=36$. The answer is $\boxed{36}$.''',
"Heron's formula|Triangles|Casework",4,
note='Repeat of an earlier record (aliased).')

# ---------------- 1766133 geometric series, 24 terms
b.add(1766133,1,r'''Consider the geometric series $5832+1944+648+\cdots$. Find the exact sum of its first $24$ terms. An answer key gives $8747$ and a student gives $8748$; is either correct?''',
r'''The ratio is $r=\dfrac{1944}{5832}=\dfrac13$ and the first term is $5832=2^3\cdot3^6$. The sum of the first $24$ terms is
\[
S_{24}=\dfrac{5832\left(1-\left(\dfrac13\right)^{24}\right)}{1-\dfrac13}=8748\left(1-\dfrac{1}{3^{24}}\right)=8748-\dfrac{8748}{3^{24}}=8748-\dfrac{4}{3^{17}},
\]
since $8748=4\cdot3^7$. So $S_{24}=\boxed{8748-\dfrac{4}{3^{17}}}$. Neither given answer is exact: the sum is slightly \emph{less} than $8748$ (by about $3.1\times10^{-8}$), so $8748$ is its value rounded to the nearest integer (it is the sum of the whole infinite series), and $8747$ is wrong.''',
'Geometric sequences|Summation|Exponents',2,
note='Answer key 8747 and poster 8748 are both inexact; the exact sum 8748 - 4/3^17 is given.')

# ---------------- 1765448 2019^{2x}=y^2+2018
b.add(1765448,1,r'''Do there exist positive integers $x$ and $y$ such that $2019^{2x}=y^2+2018$?''',
r'''Suppose so. Then
\[
2018=2019^{2x}-y^2=\left(2019^x-y\right)\left(2019^x+y\right).
\]
The two factors differ by $2y$, an even number, so they have the same parity. If both are odd, their product is odd; if both are even, their product is divisible by $4$. But $2018=2\cdot1009$ is even and not divisible by $4$. This is a contradiction, so $\boxed{\text{no such positive integers exist}}$.

(Equivalently: $2019^{2x}$ is an odd square, so $2019^{2x}\equiv1\pmod 4$, while $y^2+2018\equiv2$ or $3\pmod 4$.)''',
'Diophantine equations|Difference of squares|Parity|Remainders and congruences',3)

# ---------------- 1765863 min (x+1)(x+2)(x+3)(x+4)
b.add(1765863,1,r'''Find the least possible value of $(x+1)(x+2)(x+3)(x+4)$ over all real numbers $x$.''',
r'''Pair the outer and inner factors:
\[
(x+1)(x+4)\cdot(x+2)(x+3)=(x^2+5x+4)(x^2+5x+6).
\]
With $t=x^2+5x+5$ this is $(t-1)(t+1)=t^2-1\ge-1$. Equality needs $t=0$, i.e.\ $x^2+5x+5=0$, which has the real roots $x=\dfrac{-5\pm\sqrt5}{2}$. So the least value is $\boxed{-1}$.

(The value $-\dfrac{15}{16}$ is what one gets at $x=-\dfrac52$, the midpoint of $-1,-2,-3,-4$; that is a local maximum, not the minimum.)''',
'Substitution|Maxima and minima|Completing the square|Polynomials',3,
note='The poster got -15/16 (the value at x = -5/2); the correct minimum is -1.')

# ---------------- 1765846 5^x+5^{2-x}=26
b.add(1765846,1,r'''Solve $5^x+5^{2-x}=26$ for real $x$.''',
r'''Put $u=5^x>0$. Then $5^{2-x}=\dfrac{25}{u}$, and the equation becomes
\[
u+\dfrac{25}{u}=26\ \Longleftrightarrow\ u^2-26u+25=0\ \Longleftrightarrow\ (u-1)(u-25)=0 .
\]
So $5^x=1$ or $5^x=25$, giving $\boxed{x=0\text{ or }x=2}$. Both check: $1+25=26$ and $25+1=26$.''',
'Exponents|Substitution|Quadratic equations',2,
note='The post writes "5exp(x) + 5exp(2-x) = 26", read as 5^x + 5^(2-x) = 26. (Read literally as 5e^x + 5e^(2-x) = 26 it has no real solution, since 5e^x + 5e^(2-x) >= 10e > 26.)')

# ---------------- 1754151 improper/proper divisors of 2^n
b.add(1754151,1,r'''The improper divisors of a positive integer $m>1$ are $1$ and $m$; its other positive divisors are called proper. For a natural number $n\ge2$, let $S_i$ be the sum of the improper divisors and $S_p$ the sum of the proper divisors of $2^n$. Prove that $3\mid S_i$ if and only if $3\mid S_p$.''',
r'''The divisors of $2^n$ are $1,2,4,\dots,2^n$. So
\[
S_i=1+2^n,\qquad S_p=2+4+\cdots+2^{n-1}=2^n-2=2\left(2^{n-1}-1\right).
\]
Since $2\equiv-1\pmod3$, we have $2^m\equiv(-1)^m\pmod 3$.

\begin{itemize}
\item $3\mid S_i\iff(-1)^n\equiv-1\pmod3\iff n$ is odd.
\item $3\mid S_p\iff3\mid2^{n-1}-1$ (as $\gcd(2,3)=1$) $\iff(-1)^{n-1}\equiv1\pmod3\iff n-1$ is even $\iff n$ is odd.
\end{itemize}
Both conditions are equivalent to ``$n$ is odd'', so $3\mid S_i\iff3\mid S_p$. $\blacksquare$''',
'Sum of divisors|Powers of two|Remainders and congruences|Parity',2,
note='The definitions are made explicit: the improper divisors of m are 1 and m, the proper divisors are the others (the usual convention in the source country).')

# ---------------- 1765446 2018abc divisible by 321
b.add(1765446,1,r'''Determine all seven-digit natural numbers of the form $\overline{2018abc}$ that are divisible by $321$.''',
r'''Write $\overline{2018abc}=2018000+\overline{abc}$ with $0\le\overline{abc}\le999$. Since $321\cdot6286=2017806$, we have $2018000=2017806+194\equiv194\pmod{321}$. So we need
\[
\overline{abc}\equiv-194\equiv127\pmod{321},
\]
i.e.\ $\overline{abc}\in\{127,448,769\}$ (the next one, $1090$, is too big). The numbers are $\boxed{2018127,\ 2018448,\ 2018769}$, which are $321\cdot6287$, $321\cdot6288$ and $321\cdot6289$.''',
'Divisibility|Remainders and congruences|Place value',2)

# ---------------- 1765724 Fibonacci triangle
fig=r'''pair A=(0,0),B=(8,0);
draw(A--B,linewidth(1));
draw(arc(A,3,0,75),blue+dashed);draw(arc(B,5,105,180),red+dashed);
draw(A--3*dir(55),blue);draw(B--B+5*dir(150),red);
dot(A);dot(B);dot((3,0));
label("$F_j$",1.5*dir(55),NW,blue);label("$F_k$",B+2.5*dir(150),NE,red);
label("$F_{k+1}=F_j+F_k$",(4,0),S);'''
b.add(1765724,1,r'''Three distinct numbers are chosen from the Fibonacci sequence $1,1,2,3,5,8,13,\dots$ (they need not be consecutive terms). Prove that they can never be the side lengths of a triangle.''',
r'''Let the Fibonacci numbers be $F_1=F_2=1$, $F_{m+1}=F_m+F_{m-1}$. The sequence is non-decreasing, and strictly increasing from $F_2$ on. Let the three distinct values be $a<b<c$. Write $b=F_k$ and $c=F_l$, choosing the indices so that $k\ge2$; since $c>b$ we have $l\ge k+1$. As $a<b=F_k$ and $a$ is a Fibonacci number, $a\le F_{k-1}$ (with $k\ge 3$, because $a<b$ forces $b\ge2$). Hence
\[
a+b\le F_{k-1}+F_k=F_{k+1}\le F_l=c .
\]
A triangle needs the sum of the two shorter sides to be \emph{greater} than the longest side, so $a,b,c$ are never the sides of a triangle: at best $a+b=c$ and the ``triangle'' is flat.
'''+asy(fig,'6cm')+r'''
The sketch shows the extreme case $a=F_j$, $b=F_k$ with $j=k-1$ and $c=F_{k+1}$ (here $3,5,8$): the two shorter segments, swung from the ends of the longest one, can meet only on it, so they do not form a triangle. $\blacksquare$''',
'Fibonacci sequence|Triangle inequality|Inequalities',3)

# ---------------- 1765713 coins heads 30 cents
b.add(1765713,1,r'''Yu has $12$ coins: $5$ pennies, $4$ nickels and $3$ dimes. He tosses them all in the air. What is the probability that the total value of the coins that land heads up is exactly $30$ cents? Also explain why the following argument is wrong: ``The numbers of heads among the pennies, nickels and dimes can be $0$--$5$, $0$--$4$ and $0$--$3$, giving $6\cdot5\cdot4=120$ cases; exactly $5$ of them give $30$ cents, so the probability is $\dfrac{5}{120}=\dfrac1{24}$.''\ ''',
r'''Let $p,n,d$ be the numbers of pennies, nickels and dimes showing heads, so $p+5n+10d=30$. Then $5\mid p$, so $p=0$ or $5$:
\begin{itemize}
\item $p=0$: $n+2d=6$, so $(n,d)=(0,3),(2,2),(4,1)$;
\item $p=5$: $n+2d=5$, so $(n,d)=(1,2),(3,1)$ ($n=5$ is impossible).
\end{itemize}
The $12$ distinguishable coins give $2^{12}=4096$ equally likely outcomes, and a case $(p,n,d)$ occurs in $\dbinom5p\dbinom4n\dbinom3d$ of them:
\[
1\cdot1\cdot1+1\cdot6\cdot3+1\cdot1\cdot3+1\cdot4\cdot3+1\cdot4\cdot3=1+18+3+12+12=46 .
\]
The probability is $\dfrac{46}{4096}=\boxed{\dfrac{23}{2048}}$.

The faulty argument counts the five cases correctly but treats the $120$ triples $(p,n,d)$ as equally likely. They are not: for example $p=0$ happens in only $1$ of the $32$ ways the pennies can land, while $p=2$ happens in $\dbinom52=10$ ways. Each triple must be weighted by its number of outcomes, as above.''',
'Probability|Combinations|Casework|Money and currency',3,source=src('MATHCOUNTS',2017,'Chapter',None,rnd='Sprint'),
note='MATHCOUNTS 2017 Chapter Sprint (question number not given). The record also asks why the poster\'s count 5/120 is wrong (cases not equally likely).')

# ---------------- 1765813 n^2+5n+1 not divisible by 49
b.add(1765813,1,r'''Prove that $n^2+5n+1$ is never divisible by $49$ for any integer $n$.''',
r'''Multiply by $4$ and complete the square:
\[
4\left(n^2+5n+1\right)=(2n+5)^2-21 .
\]
Suppose $49\mid n^2+5n+1$. Then $49\mid(2n+5)^2-21$, so in particular $7\mid(2n+5)^2-21$ and hence $7\mid(2n+5)^2$. As $7$ is prime, $7\mid2n+5$, so $49\mid(2n+5)^2$. Then $49\mid(2n+5)^2-\left((2n+5)^2-21\right)=21$, which is false. Hence $49\nmid n^2+5n+1$ for every integer $n$. $\blacksquare$''',
'Divisibility|Completing the square|Prime numbers|Proof by contradiction',3,
note='The post says "prove that n^2 + 5n + 1 is divisible by 49", which is false (e.g. n = 1 gives 7); the intended statement is that it is never divisible by 49 (7 does divide it when n = 1 mod 7). Checked for all residues mod 49.')

# ---------------- 1765742 names J _ _ _ _ L
b.add(1765742,1,r'''Mr.\ Jamal will give his son a six-letter name that starts with J and ends with L. Each of the four middle letters is one of the letters A through M (inclusive), and letters may repeat. How many names are possible?''',
r'''The first and last letters are fixed. The letters A through M are $13$ letters, and each of the $4$ middle positions can be any of them independently. By the multiplication principle there are $13^4=\boxed{28561}$ names.

(If the four middle letters had to be different, the count would be $13\cdot12\cdot11\cdot10=17160$.)''',
'Multiplication principle|Counting principles',1,
note='The post does not say whether letters may repeat; repetition is allowed in the record (the distinct-letter count is mentioned in the solution). "Between A and M" is read inclusively (13 letters).')

# ---------------- 1765746 102_x = 73_{x+1}
b.add(1765746,1,r'''A number is written $102$ in base $x$ and $73$ in base $x+1$. Find $x$ and the number (in base ten).''',
r'''Expanding the place values,
\[
1\cdot x^2+0\cdot x+2=7(x+1)+3\ \Longrightarrow\ x^2-7x-8=0\ \Longrightarrow\ (x-8)(x+1)=0 .
\]
A base is a positive integer, and the digit $7$ requires $x+1\ge8$; so $x=\boxed{8}$. The number is $64+2=\boxed{66}$; check: $73_9=63+3=66$.''',
'Digits and bases|Quadratic equations',2,
note='The post asks whether 1x^2 + 0x + 2 = 7(x+1) + 3 is the right equation (it is); the record asks for the base and the number.')

# ---------------- 1765494 interval notation
b.add(1765494,1,r'''Write the set of all real numbers $x$ with $-1\le x\le1$ and $x\ne0$ in interval notation.''',
r'''The set consists of the numbers from $-1$ up to (but not including) $0$, together with those after $0$ up to and including $1$. Square brackets include an endpoint and round brackets exclude it, so the set is
\[
\boxed{[-1,0)\cup(0,1]}.
\]''',
'Inequalities',1)

# ---------------- 1765635 triangles from 2,3,5,8,13
fig=r'''pair A=(0,0),B=(13,0);
draw(A--B,linewidth(1));
draw(arc(A,5,0,80),blue+dashed);draw(arc(B,8,100,180),red+dashed);
draw(A--5*dir(60),blue);draw(B--B+8*dir(150),red);
dot(A);dot(B);
label("$5$",2.5*dir(60),NW,blue);label("$8$",B+4*dir(150),NE,red);
label("$13$",(6.5,0),S);'''
b.add(1765635,1,r'''Given five segments of lengths $2$, $3$, $5$, $8$ and $13$, how many distinct triangles can be formed using three of the segments as the sides?''',
r'''Three segments $a<b<c$ form a triangle exactly when $a+b>c$ (the triangle inequality for the longest side). Each length here is the sum of the two before it, so for any choice $a<b<c$ from the list,
\[
a+b\le(\text{the length just before }b)+b=(\text{the length just after }b)\le c .
\]
For example $5+8=13$, $3+5=8$, $3+8<13$. So no choice works:
'''+asy(fig,'6cm')+r'''
the segments of lengths $5$ and $8$ swung from the ends of the segment of length $13$ can only meet on it. The number of triangles is $\boxed{0}$.''',
'Triangle inequality|Fibonacci sequence|Combinations',2)

# ---------------- 1763348 powers of i
b.add(1763348,1,r'''Compute $i^{17}$, $i^{69}$ and $i^{1972}$, where $i^2=-1$.''',
r'''The powers of $i$ repeat with period $4$: $i^1=i$, $i^2=-1$, $i^3=-i$, $i^4=1$, so $i^n$ depends only on the remainder of $n$ when divided by $4$. Since $17=4\cdot4+1$, $69=4\cdot17+1$ and $1972=4\cdot493$,
\[
i^{17}=\boxed{i},\qquad i^{69}=\boxed{i},\qquad i^{1972}=\boxed{1}.
\]''',
'Complex numbers|Exponents|Remainders and congruences',1,source=src('AoPS Volume 1',None,None,'2-1'),
note='The poster\'s answers i, i, 1 are correct.')

# ---------------- 1765571 cups with 45 cents
b.add(1765571,1,r'''Max has $8$ identical cups. Each cup contains a different combination of nickels, dimes and quarters totaling $45$ cents, and together the cups show every such combination. Max randomly selects a cup. What is the probability that it contains at least $3$ dimes?''',
r'''List the combinations with $q$ quarters, $d$ dimes and $n$ nickels, $25q+10d+5n=45$:
\begin{itemize}
\item $q=0$: $2d+n=9$, so $d=0,1,2,3,4$ with $n=9,7,5,3,1$ ($5$ combinations);
\item $q=1$: $2d+n=4$, so $d=0,1,2$ with $n=4,2,0$ ($3$ combinations).
\end{itemize}
That is $8$ combinations, one per cup. Those with at least $3$ dimes are $(q,d,n)=(0,3,3)$ and $(0,4,1)$, so the probability is $\dfrac28=\boxed{\dfrac14}$.''',
'Probability|Systematic counting|Money and currency',2,source=src('MATHCOUNTS Handbook',None,None,None),
note='Made explicit that the 8 cups hold all 8 possible combinations (a coin type may be absent).')

# ---------------- 1765455 24 consecutive numbers
b.add(1765455,1,r'''The sum of $24$ consecutive positive integers, none of which is divisible by $25$, is computed.
\begin{enumerate}
\item[(a)] Find the last two digits of the sum.
\item[(b)] Can the hundreds digit of the sum be even?
\end{enumerate}''',
r'''Among any $25$ consecutive integers one is a multiple of $25$, and $24$ consecutive integers avoiding multiples of $25$ must fill exactly the gap between two consecutive multiples. So the numbers are $25k+1,25k+2,\dots,25k+24$ for some integer $k\ge0$, and the sum is
\[
24\cdot25k+(1+2+\cdots+24)=600k+300=100(6k+3).
\]
(a) The sum is a multiple of $100$, so its last two digits are $\boxed{00}$.

(b) The hundreds digit is the last digit of $6k+3$, which is odd. So $\boxed{\text{no}}$, the hundreds digit is always odd (it is $3,9,5,1$ or $7$).''',
'Divisibility|Arithmetic sequences|Units digits and last digits|Parity',3)

# ---------------- 1765502 AMC 8 2018 #19 sign pyramid
b.add(1765502,1,r'''In a sign pyramid a cell gets a ``$+$'' if the two cells below it have the same sign, and it gets a ``$-$'' if the two cells below it have different signs. A sign pyramid with four levels has $4$ cells in the bottom row, then $3$, $2$ and $1$. How many possible ways are there to fill the four cells in the bottom row to produce a ``$+$'' at the top of the pyramid?

$\textbf{(A) } 2 \qquad \textbf{(B) } 4 \qquad \textbf{(C) } 8 \qquad \textbf{(D) } 12 \qquad \textbf{(E) } 16$

Also explain what the operation ``$a$ XOR $b$'' (exclusive or) is and why it describes this rule.''',
r'''Write $1$ for ``$+$'' and $0$ for ``$-$''. Two cells with values $x,y$ produce $1$ above them exactly when $x=y$. It is easier to work with $0$ for ``$+$'' and $1$ for ``$-$'' instead: then the cell above $x,y$ is $1$ exactly when $x\ne y$. This is the operation $x$ XOR $y$ (``exclusive or'': true when exactly one of $x,y$ is $1$), and it equals $x+y$ reduced modulo $2$:
\[
0+0\equiv0,\quad0+1\equiv1,\quad1+0\equiv1,\quad1+1\equiv0\pmod2 .
\]
With bottom row $a,b,c,d$ (in this coding) the rows above are $a+b,\ b+c,\ c+d$, then $a+2b+c,\ b+2c+d$, then $a+3b+3c+d\equiv a+b+c+d\pmod 2$. The top is ``$+$'', i.e.\ $0$, exactly when $a+b+c+d$ is even: an even number of ``$-$'' signs in the bottom row. For any choice of $a,b,c$ there is exactly one $d$ that makes the sum even, so there are $2^3=8$ ways. The answer is $\boxed{\textbf{(C) } 8}$.''',
'Parity|Remainders and congruences|Pascal\'s triangle|Counting principles',3,source=src('AMC 8',2018,None,19),
note='The pyramid figure is described in words. The poster asked what XOR means; the solution explains it. The coding 0 = "+", 1 = "-" is used so that the rule is exactly XOR.')

# ---------------- 1764786 7 and 3 points
b.add(1764786,1,r'''In a game there are two ways of scoring: method $A$ gives $7$ points and method $B$ gives $3$ points. What is the largest total score that cannot be obtained?''',
r'''A score is obtainable if it equals $7a+3b$ with $a,b\ge0$ integers.

\textbf{$11$ is not obtainable.} With $a=0$ we would need $3\mid11$; with $a=1$, $3b=4$; and $a\ge2$ gives more than $11$.

\textbf{Every score from $12$ on is obtainable.} We have $12=3\cdot4$, $13=7+3\cdot2$ and $14=7\cdot2$. Any larger score is one of these three plus a multiple of $3$, so it is obtained by adding method-$B$ scores.

So the largest impossible score is $\boxed{11}$ (in agreement with the Chicken McNugget formula $7\cdot3-7-3=11$ for coprime $7$ and $3$).''',
'Linear Diophantine equations|Bounding and extremal cases',2)

# ---------------- 1764009 square, rectangle, EAF line
qf=r'''pair D=(0,0),C=(4,0),B=(4,4),A=(0,4),G=(4,3);
pair n=(-3,4)/5; pair Ep=D+3.2*n, F=G+3.2*n;
draw(A--B--C--D--cycle,linewidth(0.9));
draw(D--Ep--F--G--cycle,linewidth(0.9));
dot(A);
label("$A$",A,dir(160));label("$B$",B,NE);label("$C$",C,SE);label("$D$",D,SW);
label("$E$",Ep,W);label("$F$",F,N);label("$G$",G,E);
label("$4$",(D+C)/2,S);label("$3$",(C+G)/2,E);'''
sf=r'''pair D=(0,0),C=(4,0),B=(4,4),A=(0,4),G=(4,3);
pair n=(-3,4)/5; pair Ep=D+3.2*n, F=G+3.2*n;
fill(A--D--G--cycle,lightgray);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(D--Ep--F--G--cycle,linewidth(0.9));
draw(A--G,dashed);
dot(A);
label("$A$",A,dir(160));label("$B$",B,NE);label("$C$",C,SE);label("$D$",D,SW);
label("$E$",Ep,W);label("$F$",F,N);label("$G$",G,E);
label("$4$",(D+C)/2,S);label("$3$",(C+G)/2,E);label("$5$",(D+G)/2+(0.15,-0.3));'''
b.add(1764009,1,r'''In the diagram, $ABCD$ is a square of side $4$ cm, $DEFG$ is a rectangle, $G$ lies on side $BC$, and $E$, $A$, $F$ lie on a straight line with $A$ between $E$ and $F$. Given that $CG=3$ cm and $DG=5$ cm, find the length of $DE$ in cm.
'''+asy(qf,'5cm'),
r'''Look at triangle $ADG$ (shaded).
'''+asy(sf,'5cm')+r'''
\textbf{As part of the square.} Take $AD$ as the base. The vertex $G$ lies on side $BC$, which is $4$ cm from $AD$, so the height is $4$ cm and
\[
[ADG]=\dfrac12\cdot4\cdot4=8\text{ cm}^2,
\]
which is half of the square.

\textbf{As part of the rectangle.} Now take $DG$ as the base. The vertex $A$ lies on the opposite side $EF$ of the rectangle, so the height of the triangle is the width $DE$ of the rectangle. Hence $[ADG]=\dfrac12\cdot DG\cdot DE$ is half of the rectangle, and the rectangle has area $2\cdot8=16$ cm$^2$.

Therefore $DG\cdot DE=16$, and $DE=\dfrac{16}{5}=\boxed{3.2}$ cm. (The data agree: $3^2+4^2=5^2$, so triangle $DCG$ is right-angled at $C$, as it must be with $G$ on $BC$.)''',
'Rectangles|Squares|Area decomposition|Lengths, perimeter, and area|Pythagorean theorem',3,
note='The figure was missing; it is rebuilt from the text and the usual version of this problem (CG = 3, DG = 5, CD = 4 force angle DCG = 90 degrees, so G is on line BC; A lying between E and F then puts G on segment BC; the answer 16/5 is the same in either position). The poster asked for an explanation suitable for a 4th grader; the solution uses only areas of a triangle, square and rectangle.')

# ---------------- 1764818 sum of logs
b.add(1764818,1,r'''How many integers $x$ satisfy
\[
\log x+\log x^2+\log x^3+\cdots+\log x^{2999}+\log x^{3000}\le22507500,
\]
where $\log$ is the base-$10$ logarithm?''',
r'''The logarithms are defined only for $x>0$, and then $\log x^k=k\log x$. So the left side is
\[
(1+2+\cdots+3000)\log x=\dfrac{3000\cdot3001}{2}\log x=4501500\log x .
\]
Since $4501500\cdot5=22507500$, the inequality is $\log x\le5$, i.e.\ $0<x\le10^5$. The integers $x=1,2,\dots,100000$ work, so there are $\boxed{100000}$ of them.''',
'Logarithms|Summation|Arithmetic sequences|Inequalities',2,
note='The base-10 logarithm is assumed (the usual meaning of log in this setting); x must be positive for log x to be defined.')

# ---------------- 1765152 max x^3y^2z
b.add(1765152,1,r'''Find the maximum value of $x^3y^2z$ over positive real numbers $x,y,z$ with $3x+2y+z=12$.''',
r'''Write $12$ as the sum of six positive terms, $x+x+x+y+y+z$, and apply AM-GM:
\[
2=\dfrac{x+x+x+y+y+z}{6}\ge\sqrt[6]{x^3y^2z},
\]
so $x^3y^2z\le2^6=64$. Equality holds when $x=y=z$, that is $x=y=z=2$, which satisfies $3\cdot2+2\cdot2+2=12$ and gives $8\cdot4\cdot2=64$. The maximum is $\boxed{64}$.''',
'AM-GM inequality|Maxima and minima|Inequalities',3,
note='The post asks for the minimum, which does not exist (with no sign conditions the product is unbounded below, and for positive variables it can be made arbitrarily close to 0). The intended question, the maximum for positive x, y, z, is used.')

b.save()
