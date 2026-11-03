from qb import *
b=Bank('p227_01')

# ---------------- 1758922 UKMT IMC 2005 Q23
b.add(1758922,1,r'''There are $120$ different ways of arranging the letters U, K, M, I and C. All of these arrangements are listed in dictionary order, starting with CIKMU. Which position in the list does UKIMC occupy?

\textbf{(A)} $110$th \qquad \textbf{(B)} $112$th \qquad \textbf{(C)} $114$th \qquad \textbf{(D)} $116$th \qquad \textbf{(E)} $118$th''',
r'''In alphabetical order the letters are C, I, K, M, U. Count the arrangements that come before UKIMC.
\begin{itemize}
\item Arrangements beginning with C, I, K or M: $4\cdot4!=96$.
\item Arrangements beginning with U and then C or I: $2\cdot3!=12$.
\item Arrangements beginning UK and then C: $2!=2$ (UKCIM, UKCMI).
\item Arrangements beginning UKI that come before UKIMC: only UKICM, so $1$.
\end{itemize}
So $96+12+2+1=111$ arrangements come before UKIMC, and it is in position $\boxed{112}$, answer \textbf{(B)}.''',
'Permutations|Systematic counting',2,source=src('UKMT IMC',2005,None,23))

# ---------------- 1758855 hypotenuse > 38
b.add(1758855,1,r'''What is the smallest integer greater than $38$ that cannot be the length of the hypotenuse of a right triangle with integer side lengths?''',
r'''Check $39,40,41,\dots$ in turn.
\begin{itemize}
\item $39=3\cdot13$: scale the $5$--$12$--$13$ triangle by $3$: $15^2+36^2=39^2$.
\item $40=8\cdot5$: scale the $3$--$4$--$5$ triangle by $8$: $24^2+32^2=40^2$.
\item $41$: $9^2+40^2=81+1600=1681=41^2$.
\item $42$: suppose $a^2+b^2=42^2$ with positive integers $a,b$. Squares are $\equiv0$ or $1\pmod3$, and $a^2+b^2\equiv0\pmod3$ forces $3\mid a$ and $3\mid b$. Squares modulo $7$ are $0,1,2,4$, and the only way two of them add to $0\pmod7$ is $0+0$, so $7\mid a$ and $7\mid b$. Hence $a=21a'$, $b=21b'$ with $a'^2+b'^2=4$, which has no solution in positive integers ($4=0+4$ only). So $42$ is not a hypotenuse.
\end{itemize}
The answer is $\boxed{42}$.''',
'Pythagorean triples|Remainders and congruences|Quadratic residues',4,source=src('MATHCOUNTS',2014,'National',None),
note='MATHCOUNTS 2014 National (problem number not given). The impossibility of 42 is proved with residues modulo 3 and 7; all values checked by brute force.')

# ---------------- 1758744 factor of cubic
b.add(1758744,1,r'''Which of the following linear factors is a factor of the polynomial $g(x)=x^3-2x^2-16x+32$?

\textbf{(A)} $x-2$ \qquad \textbf{(B)} $x+2$ \qquad \textbf{(C)} $x+8$ \qquad \textbf{(D)} $x-16$''',
r'''Group the terms:
\[
g(x)=x^2(x-2)-16(x-2)=(x-2)(x^2-16)=(x-2)(x-4)(x+4).
\]
So $x-2$ is a factor, answer \textbf{(A)}. (Check with the factor theorem: $g(2)=8-8-32+32=0$, while $g(-2)=48$, $g(-8)=-480$ and $g(16)=3360$ are not zero.)''',
'Polynomials|Factoring|Remainder theorem and factor theorem',2,
note='The post prints g(x) = x^3 = 2x^2 - 16x + 32; the "=" is read as "-" (the only reading for which one of the choices is a factor).')

# ---------------- 1758734 absolute value inequality
b.add(1758734,1,r'''Solve the inequality $-2|x-4|+8\le-4$.''',
r'''Subtract $8$ and divide by $-2$, reversing the inequality:
\[
-2|x-4|\le-12\quad\Longleftrightarrow\quad|x-4|\ge6 .
\]
The distance from $x$ to $4$ is at least $6$, so $x-4\ge6$ or $x-4\le-6$. The solution is $\boxed{x\le-2\ \text{or}\ x\ge10}$, that is, $(-\infty,-2]\cup[10,\infty)$.''',
'Absolute value|Inequalities',2)

# ---------------- 1758642 totient inequality
b.add(1758642,1,r'''Show that for every integer $n>1$,
\[
\varphi\left(n^2\right)+\varphi\left((n+1)^2\right)\le2n^2,
\]
where $\varphi$ is Euler's totient function.''',
r'''For every positive integer $m$, $\varphi(m^2)=m\varphi(m)$: if $m=\prod p_i^{a_i}$ then $\varphi(m^2)=\prod p_i^{2a_i-1}(p_i-1)=m\prod p_i^{a_i-1}(p_i-1)=m\varphi(m)$. Also $\varphi(m)\le m-1$ for $m\ge2$, and $\varphi(m)\le\dfrac m2$ for even $m$ (the even numbers up to $m$ are not coprime to $m$).

Exactly one of $n,n+1$ is even.

\textbf{$n$ even.} Then $n\varphi(n)\le\dfrac{n^2}{2}$ and $(n+1)\varphi(n+1)\le(n+1)n$, so the sum is at most
\[
\dfrac{n^2}{2}+n^2+n=2n^2-\dfrac{n(n-2)}{2}\le2n^2 .
\]

\textbf{$n$ odd.} Then $n\varphi(n)\le n(n-1)$ and $(n+1)\varphi(n+1)\le\dfrac{(n+1)^2}{2}$, so the sum is at most
\[
n^2-n+\dfrac{n^2+2n+1}{2}=2n^2-\dfrac{n^2-1}{2}\le2n^2 .
\]
In both cases the inequality holds. $\blacksquare$''',
"Euler's theorem and totient|Inequalities|Parity|Proof by cases",4,
note='Checked numerically for 2 <= n <= 2000.')

# ---------------- 1758750 primes product 1139
b.add(1758750,1,r'''Two prime numbers have a product of $1139$. What is the sum of these two numbers?''',
r'''Since $33^2=1089<1139<34^2$, the smaller prime is at most $33$. Trying primes: $1139$ is odd, its digit sum $14$ is not a multiple of $3$, it does not end in $0$ or $5$, and $1139=7\cdot162+5=11\cdot103+6=13\cdot87+8$, but $1139=17\cdot67$. Both $17$ and $67$ are prime, so the sum is $17+67=\boxed{84}$.''',
'Prime factorisation|Prime numbers',2)

# ---------------- 1758747 vertex form
b.add(1758747,1,r'''What is the $x$-coordinate of the vertex of the quadratic function $f(x)=3(x-2)^2+6$?''',
r'''In the vertex form $f(x)=a(x-h)^2+k$ the vertex is $(h,k)$. Here $(x-2)^2\ge0$ with equality only at $x=2$, so the minimum value $6$ is reached at $x=2$; the vertex is $(2,6)$ and its $x$-coordinate is $\boxed{2}$.''',
'Quadratic equations|Functions',1)
b.add(1758747,2,r'''A quadratic function has its vertex at $(3,4)$ and its $y$-intercept is $22$. Which of the following is the equation of the function?

\textbf{(A)} $y=(x-3)^2+4$ \qquad \textbf{(B)} $y=2(x-3)^2+4$ \qquad \textbf{(C)} $y=\dfrac12(x+3)^2+4$ \qquad \textbf{(D)} $y=4(x+3)^2+4$''',
r'''With vertex $(3,4)$ the function is $y=a(x-3)^2+4$ (this rules out (C) and (D), whose vertices are at $x=-3$). At $x=0$: $9a+4=22$, so $a=2$. The answer is \textbf{(B)} $y=2(x-3)^2+4$.''',
'Quadratic equations|Functions',2)

# ---------------- 1755354 sum of inverses mod 13
b.add(1755354,1,r'''Find the value of $2^{-1}+2^{-2}+2^{-3}+2^{-4}+2^{-5}+2^{-6}\pmod{13}$, where $2^{-k}$ denotes the inverse of $2^k$ modulo $13$.''',
r'''Since $2^6=64=5\cdot13-1\equiv-1\pmod{13}$, we have $2^{-6}\equiv(-1)^{-1}=-1$. Put everything over $2^6$:
\[
2^{-1}+2^{-2}+\cdots+2^{-6}=2^{-6}\left(2^5+2^4+2^3+2^2+2+1\right)=2^{-6}\cdot63\equiv-63\pmod{13}.
\]
As $63=4\cdot13+11$, this is $-11\equiv\boxed{2}\pmod{13}$.

Check term by term: $2^{-1}\equiv7$ (since $2\cdot7=14$), and multiplying by $7$ each time gives $2^{-2}\equiv10$, $2^{-3}\equiv5$, $2^{-4}\equiv9$, $2^{-5}\equiv11$, $2^{-6}\equiv12$; their sum is $54\equiv2$.''',
'Remainders and congruences|Geometric sequences|Modular exponentiation',3,
note='The post asks for a quick method; the solution factors out 2^{-6} and uses 2^6 = -1 (mod 13).')

# ---------------- 1758431 transformations (q02 dropped)
b.add(1758431,1,r'''Match each equation with the description of how its graph is obtained from the graph of the parent function $y=x^2$.
\begin{itemize}
\item[x.] $y=(x-8)^2$
\item[y.] $y=\dfrac18x^2$
\item[z.] $y=x^2+8$
\end{itemize}
\begin{itemize}
\item[1.] Vertical translation
\item[2.] Horizontal translation
\item[3.] Vertical compression
\end{itemize}''',
r'''\begin{itemize}
\item[x.] $y=(x-8)^2$ takes at $x$ the value that $y=x^2$ takes at $x-8$, so the graph of $y=x^2$ is moved $8$ units to the right: \textbf{2}, horizontal translation.
\item[y.] $y=\dfrac18x^2$ multiplies every $y$-value of the parent graph by $\dfrac18$, squashing it towards the $x$-axis: \textbf{3}, vertical compression.
\item[z.] $y=x^2+8$ adds $8$ to every $y$-value, moving the graph up $8$ units: \textbf{1}, vertical translation.
\end{itemize}
So $\boxed{\text{x--2, y--3, z--1}}$. Quick rule: a change inside the square (to $x$) moves the graph sideways; a change outside it (to the output) acts vertically, adding shifts and multiplying by a factor between $0$ and $1$ compresses.''',
'Functions|Quadratic equations',1,
note='The post lists "y. y = x^2" (the parent function itself) to be matched with "vertical compression", which is impossible; the coefficient was evidently lost, and y = (1/8)x^2 is used. Part 2 of the post (the 68% rule for a normal distribution) is a recalled fact outside the vocabulary and is dropped.')

# ---------------- 1758380 chocolate standard deviation
b.add(1758380,1,r'''A machine in a chocolate factory squirts out drops of molten chocolate. When the machine is set to $x$, the drops have mean mass $x$ grams with a standard deviation of $0.01$ grams. Nearly all chocolate chips produced have a mass within $2$ standard deviations of the mean. To make (nearly) no chocolate chips of mass less than $2$ grams, what is the lowest setting $x$ that should be used?''',
r'''Nearly all chips have mass between $x-2(0.01)$ and $x+2(0.01)$ grams. For (nearly) none to be below $2$ grams, the lower end must be at least $2$:
\[
x-0.02\ge2\quad\Longleftrightarrow\quad x\ge2.02 .
\]
The lowest setting is $x=\boxed{2.02}$ grams.''',
'Inequalities|Data and graph interpretation',1)

# ---------------- 1758669 Descartes
b.add(1758669,1,r'''Use Descartes' rule of signs to determine the possible numbers of positive real roots and of negative real roots of
\[
27x^7+51x^6-300x^5+x^4-49x^3-52x^2+178x-37=0 .
\]''',
r'''Let $p(x)$ be the polynomial. Descartes' rule says the number of positive roots (with multiplicity) equals the number of sign changes in the coefficient sequence, or is less than it by an even number; negative roots are counted the same way using $p(-x)$.

\textbf{Positive roots.} The signs of the coefficients of $p(x)$ are
\[
+\,+\,-\,+\,-\,-\,+\,- ,
\]
with sign changes $+\to-$, $-\to+$, $+\to-$, $-\to+$, $+\to-$: five changes. So $p$ has $5$, $3$ or $1$ positive roots.

\textbf{Negative roots.} $p(-x)=-27x^7+51x^6+300x^5+x^4+49x^3-52x^2-178x-37$, with signs
\[
-\,+\,+\,+\,+\,-\,-\,- ,
\]
which has two sign changes. So $p$ has $2$ or $0$ negative roots.

Answer: $\boxed{5,\ 3\text{ or }1\text{ positive roots, and }2\text{ or }0\text{ negative roots}}$.

(Evaluating, $p(-5)<0$, $p(-1)=107>0$ and $p(0)=-37<0$, so there are in fact exactly $2$ negative roots; and $p(0)<0$, $p\!\left(\dfrac12\right)>0$, $p(1)=-181<0$, $p(3)>0$ give at least $3$ positive roots. Numerically the real roots are about $-4.42$, $-0.91$, $0.23$, $0.71$ and $2.55$.)''',
'Polynomials|Polynomial roots',2,
note='"Determine the number" is read as the standard Descartes exercise (possible numbers); the actual numbers (3 positive, 2 negative, found numerically) are given as a remark.')

# ---------------- 1757851 phone number (alias)
b.add(1757851,1,r'''Yesterday I wrote down my friend John's telephone number. The number on my note has $6$ digits, but John said that his number has seven digits. I do not know which digit I forgot to write down or where it was. How many different telephone numbers do I have to try in order to be sure that I use the correct one? (A telephone number may start with any digit, including $0$.)''',
r'''The candidates are the strings obtained by inserting one digit into one of the $7$ gaps of the noted $6$-digit string. Inserting a digit $d$ just before an equal digit gives the same string as inserting it just after that digit, so every candidate arises from a unique insertion in which $d$ differs from the digit immediately after it, or $d$ is placed at the end. That gives $6\cdot9+10=\boxed{64}$ different numbers.''',
'Counting principles|Systematic counting',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1758503 hypotenuse (alias) and difference of squares
b.add(1758503,1,r'''What is the smallest integer greater than $38$ that cannot be the length of the hypotenuse of a right triangle with integer side lengths?''',
r'''$39^2=15^2+36^2$, $40^2=24^2+32^2$, $41^2=9^2+40^2$, but $42^2=a^2+b^2$ would force $21\mid a,b$ (squares modulo $3$ and $7$), leaving $a'^2+b'^2=4$, impossible in positive integers. The answer is $\boxed{42}$.''',
'Pythagorean triples|Right triangles|Pythagorean theorem',4,source=src('MATHCOUNTS',2014,'National',None),
note='Same problem as topic 1758855 of this batch (aliased).')
b.add(1758503,2,r'''How many positive integers less than $2011$ cannot be expressed as the difference of the squares of two positive integers?''',
r'''Suppose $n=a^2-b^2=(a-b)(a+b)$ with positive integers $a>b$. The factors $a-b$ and $a+b$ have the same parity (their sum is $2a$).

\textbf{Numbers $\equiv2\pmod4$ never work.} If both factors are odd, $n$ is odd; if both are even, $4\mid n$.

\textbf{Odd $n\ge3$ work:} $n=2k+1=(k+1)^2-k^2$ with $k\ge1$.

\textbf{Multiples of $4$ from $8$ on work:} $n=4k=(k+1)^2-(k-1)^2$ with $k\ge2$, so $k-1\ge1$.

\textbf{$1$ and $4$ do not work.} $1=(a-b)(a+b)$ forces $a+b=1$, impossible for positive $a,b$. For $4$ the factors have the same parity, so they are $2$ and $2$, giving $b=0$.

The numbers below $2011$ that are $\equiv2\pmod4$ are $2,6,\dots,2010$: there are $\dfrac{2010-2}{4}+1=503$ of them. Adding $1$ and $4$, the answer is $503+2=\boxed{505}$.''',
'Difference of squares|Factoring|Parity|Remainders and congruences',4,source=src('MATHCOUNTS',2011,'National',None),
note='MATHCOUNTS 2011 National (problem number not given). The requirement that both integers be positive excludes 1 and 4; count checked by brute force.')

# ---------------- 1758419 quadratics
b.add(1758419,1,r'''Find all $x$-intercepts of the quadratic function $f(x)=-x^2-4x-1$, rounded to the nearest tenth.''',
r'''Set $f(x)=0$: $x^2+4x+1=0$. Completing the square, $(x+2)^2=3$, so $x=-2\pm\sqrt3$. With $\sqrt3\approx1.732$, the intercepts are $x\approx\boxed{-0.3\text{ and }-3.7}$.''',
'Quadratic equations|Completing the square',2)
b.add(1758419,2,r'''When the trinomial $6x^2+5x-6$ is factored, which of the following is one of the factors?

\textbf{(A)} $6x-1$ \qquad \textbf{(B)} $x-6$ \qquad \textbf{(C)} $3x-2$ \qquad \textbf{(D)} $2x-3$''',
r'''We need two numbers with product $6\cdot(-6)=-36$ and sum $5$: they are $9$ and $-4$. Then
\[
6x^2+5x-6=6x^2+9x-4x-6=3x(2x+3)-2(2x+3)=(3x-2)(2x+3).
\]
The answer is \textbf{(C)} $3x-2$.''',
'Factoring|Quadratic equations',2)

# ---------------- 1747860 penalty box
b.add(1747860,1,r'''In a hockey-themed board game, players start in the penalty box, and a player escapes from the penalty box by rolling the same number on both of two standard six-sided dice. Piper, Quincy and Riley take turns, in that order, each rolling the pair of dice on her turn; a player who has escaped no longer rolls. What is the probability that Piper is the last of the three to escape? Express your answer as a common fraction.''',
r'''On each roll a player escapes with probability $p=\dfrac16$ and stays with probability $q=\dfrac56$.

\textbf{Who escapes first.} Rounds of three rolls (Piper, Quincy, Riley) repeat until someone escapes. Summing over the number of failed rounds, the first escape is by Quincy with probability $\dfrac{qp}{1-q^3}$ and by Riley with probability $\dfrac{q^2p}{1-q^3}$ (Piper must not escape first).

\textbf{The race between the other two.} Once one player has escaped, the remaining two alternate. The player who rolls first escapes first with probability
\[
p+q^2p+q^4p+\cdots=\dfrac{p}{1-q^2}=\dfrac{1}{1+q}=\dfrac{6}{11},
\]
and the other with probability $\dfrac5{11}$.
\begin{itemize}
\item If Quincy escapes first, Riley rolls next, then Piper. Riley must beat Piper: probability $\dfrac6{11}$.
\item If Riley escapes first, Piper rolls next, then Quincy. Quincy must beat Piper: probability $\dfrac5{11}$.
\end{itemize}
Therefore, with $1-q^3=\dfrac{91}{216}$, $qp=\dfrac{30}{216}$ and $q^2p=\dfrac{25}{216}$,
\[
P=\dfrac{\dfrac{30}{216}\cdot\dfrac6{11}+\dfrac{25}{216}\cdot\dfrac5{11}}{\dfrac{91}{216}}=\dfrac{180+125}{11\cdot91}=\boxed{\dfrac{305}{1001}} .
\]
(The poster's $\dfrac6{11}$ is the probability that the first of two alternating players wins the race; it is only one ingredient. The rule of the turn order after an escape matters: the next roller is the next remaining player in the original order.)''',
'Probability|Geometric sequences|Independent events|Recursive probability|Casework',5,source=src('MATHCOUNTS',2017,'National',None),
note='MATHCOUNTS 2017 National (problem number not given). The statement makes explicit that escaped players stop rolling and the others keep the original order. The answer 305/1001 was checked exactly with a Markov-chain computation and by simulation.')

# ---------------- 1758425 complex product
b.add(1758425,1,r'''Multiply the complex numbers $(i)(6i)(4+6i)$ and give the answer in the form $a+bi$. A student expands to $24i^2+36i^3$, then ``divides by $i^2$'' and gets $24+36i$. What is wrong?''',
r'''First $(i)(6i)=6i^2=-6$, so
\[
(i)(6i)(4+6i)=-6(4+6i)=\boxed{-24-36i}.
\]
Equivalently, $24i^2+36i^3=24(-1)+36(-i)=-24-36i$, using $i^2=-1$ and $i^3=i^2\cdot i=-i$.

The student's error is ``dividing by $i^2$'': that changes the value (it divides the number by $-1$, flipping its sign). To simplify one must replace $i^2$ by $-1$, not remove it.''',
'Complex numbers',1)

# ---------------- 1758208 logarithms
b.add(1758208,1,r'''\begin{enumerate}
\item[(a)] Solve $\log_2 x=4$.
\item[(b)] Solve $2^x=10$, and explain why logarithms are needed to write the answer exactly.
\end{enumerate}''',
r'''\textbf{(a)} By definition, $\log_2x=4$ means $2^4=x$, so $x=\boxed{16}$.

\textbf{(b)} Since $2^3=8<10<16=2^4$ and $2^x$ is increasing, the solution lies strictly between $3$ and $4$, so it is not an integer; in fact it is not even rational: $2^{\dfrac mn}=10$ with positive integers $m,n$ would give $2^m=10^n$, impossible because $10^n$ has the factor $5$. The logarithm is exactly the name for this exponent: $x=\boxed{\log_2 10}\approx3.32$. Logarithms let us solve equations in which the unknown is an exponent, just as square roots let us solve $x^2=10$.''',
'Logarithms|Exponents',1,
note='The post shows log_2(x) = 4 gives x = 16 and asks why logarithms are needed; part (b) (2^x = 10) is added to answer that question.')

# ---------------- 1757353 sequences and statistics
b.add(1757353,1,r'''Five numbers form an arithmetic sequence with a mean of $18$. If the mean of the squares of the five numbers is $374$, what is the greatest of the five original numbers?''',
r'''The mean of an arithmetic sequence of five terms is its middle term, so the numbers are $18-2d,18-d,18,18+d,18+2d$. The cross terms cancel when squaring and adding:
\[
\dfrac{(18-2d)^2+(18-d)^2+18^2+(18+d)^2+(18+2d)^2}{5}=18^2+\dfrac{(4+1+0+1+4)d^2}{5}=324+2d^2 .
\]
So $324+2d^2=374$, $d^2=25$, $|d|=5$. The numbers are $8,13,18,23,28$, and the greatest is $\boxed{28}$.''',
'Arithmetic sequences|Mean|Algebraic manipulation',3)
b.add(1757353,2,r'''The ten guppies in Vida's tank are $5,5,8,8,8,9,10,11,11$ and $33$ weeks old. A guppy of age $n$ weeks, where $n$ is a positive integer, is added to her tank. The sum of the mean, the median and the unique mode of the eleven guppies' ages equals their range. What is the sum of all possible values of $n$?''',
r'''The ten ages add up to $108$, so the new mean is $\dfrac{108+n}{11}$. The mode must be unique. Among the ten ages $8$ appears three times and every other age at most twice; adding $n=5$ or $n=11$ would create a second age appearing three times, so $n\ne5,11$, and then the unique mode is $8$. The median is the $6$th of the eleven ages: it is $8$ if $n\le8$ and $9$ if $n\ge9$. The range is $33-n$ if $n<5$, $28$ if $5\le n\le33$, and $n-5$ if $n>33$.
\begin{itemize}
\item $n<5$: $\dfrac{108+n}{11}+16=33-n$ gives $12n=79$; no integer.
\item $5\le n\le8$: $\dfrac{108+n}{11}+16=28$ gives $n=24$; not in range.
\item $9\le n\le33$: $\dfrac{108+n}{11}+17=28$ gives $n=13$. Check: mean $11$, median $9$, mode $8$, sum $28$, range $28$.
\item $n>33$: $\dfrac{108+n}{11}+17=n-5$ gives $10n=350$, $n=35$. Check: mean $13$, median $9$, mode $8$, sum $30=35-5$.
\end{itemize}
The possible values are $13$ and $35$, with sum $\boxed{48}$.''',
'Mean|Median|Mode|Range|Casework',4,
note='The age n is taken to be a positive integer, as "integer values of n" in the post requires; answer checked by brute force.')
b.add(1757353,3,r'''The coefficients $c$ and $d$ of $x^3-19x^2+cx+d=0$ are chosen so that the roots of the equation are positive integers that form a geometric sequence. What is the value of $c+d$?''',
r'''Let the roots, in increasing order, be $u\le v\le w$ with $v^2=uw$; by Vieta, $u+v+w=19$. Write the common ratio in lowest terms as $\dfrac pq$ with $p\ge q\ge1$. Since $w=u\dfrac{p^2}{q^2}$ is an integer and $\gcd(p,q)=1$, $q^2\mid u$; put $u=kq^2$, so the roots are $kq^2,kpq,kp^2$ and
\[
k\left(p^2+pq+q^2\right)=19 .
\]
As $19$ is prime and $p^2+pq+q^2\ge3$, we get $k=1$ and $p^2+pq+q^2=19$. Trying $q=1$: $p^2+p+1=19$ has no integer root. $q=2$: $p^2+2p+4=19$ gives $p=3$. ($q\ge3$ gives at least $27$.) So the roots are $4,6,9$. By Vieta,
\[
c=4\cdot6+4\cdot9+6\cdot9=114,\qquad d=-4\cdot6\cdot9=-216,
\]
and $c+d=\boxed{-102}$.''',
"Vieta's formulas|Geometric sequences|Polynomial roots|Diophantine equations",4)

# ---------------- 1757894 compare with 1/6
b.add(1757894,1,r'''Compare
\[
\dfrac{1}{2^3+3}+\dfrac{1}{3^3+4}+\dfrac{1}{4^3+5}+\cdots+\dfrac{1}{2018^3+2019}
\]
with $\dfrac16$.''',
r'''The general term is $\dfrac1{k^3+k+1}$ for $k=2,3,\dots,2018$. For $k\ge2$, $k^3+k+1>k^3-k=(k-1)k(k+1)$, and
\[
\dfrac{1}{(k-1)k(k+1)}=\dfrac12\left(\dfrac1{(k-1)k}-\dfrac1{k(k+1)}\right).
\]
Keep the first two terms exactly and bound the rest by the telescoping sum:
\[
\sum_{k=4}^{2018}\dfrac{1}{k^3+k+1}<\dfrac12\sum_{k=4}^{2018}\left(\dfrac1{(k-1)k}-\dfrac1{k(k+1)}\right)=\dfrac12\left(\dfrac1{12}-\dfrac1{2018\cdot2019}\right)<\dfrac1{24}.
\]
Hence the whole sum is less than
\[
\dfrac1{11}+\dfrac1{31}+\dfrac1{24}=\dfrac{744+264+341}{8184}=\dfrac{1349}{8184}<\dfrac{1364}{8184}=\dfrac16 .
\]
So the sum is $\boxed{\text{less than }\dfrac16}$ (numerically it is about $0.1614$).

(Bounding from the second term on, $\dfrac1{11}+\dfrac1{12}=\dfrac{23}{132}>\dfrac16$, is too weak; that is why two terms are kept exactly.)''',
'Telescoping sums|Inequalities|Summation|Bounding and extremal cases',5,
note='Sum read as the terms 1/(k^3 + k + 1) for k = 2, ..., 2018, which fits the three printed terms. Checked numerically.')

# ---------------- 1758037 xy=9, x+y=10
b.add(1758037,1,r'''Real numbers $x$ and $y$ satisfy $xy=9$ and $x+y=10$. Find all possible values of $x^2-y^2$.''',
r'''We have $(x-y)^2=(x+y)^2-4xy=100-36=64$, so $x-y=\pm8$. Then
\[
x^2-y^2=(x+y)(x-y)=10\cdot(\pm8)=\boxed{\pm80}.
\]
Indeed $(x,y)=(9,1)$ gives $80$ and $(x,y)=(1,9)$ gives $-80$.''',
'Difference of squares|Equations and systems of equations|Algebraic expressions and identities',2,
note='The post asks for "x^2 - y^2" without saying which variable is larger, so both values are given.')

# ---------------- 1757623 sum of squares of digits
b.add(1757623,1,r'''How many of the integers $1,2,\dots,200$ are equal to the sum of the squares of their digits?''',
r'''\textbf{One digit.} $n=n^2$ gives $n=1$.

\textbf{Two digits.} $10a+b=a^2+b^2$ with $1\le a\le9$, $0\le b\le9$ means $a(10-a)=b(b-1)$. The left side is one of $9,16,21,24,25$; the right side is one of $0,2,6,12,20,30,42,56,72$. They never agree, so there is no solution.

\textbf{Three digits.} For $100\le n\le199$, $n=100+10b+c$ while the digit-square sum is $1+b^2+c^2$; equality means $b(b-10)+c(c-1)=99$. But $b(b-10)\le0$ and $c(c-1)\le72$, so the left side is at most $72$. Also $200$ has digit-square sum $4$.

So only $n=1$ works: the answer is $\boxed{1}$.''',
'Digit problems|Digits and bases|Casework',3,
note='Checked by direct computation over 1-200.')

# ---------------- 1757647 quadratic inequalities
b.add(1757647,1,r'''Solve the inequality $-6x<-1-9x^2$.''',
r'''Rearranging, $9x^2-6x+1<0$, that is, $(3x-1)^2<0$. A square of a real number is never negative, so $\boxed{\text{there is no real solution}}$. (With $\le$ instead of $<$, the only solution would be $x=\dfrac13$.)''',
'Inequalities|Quadratic equations|Factoring',2)
b.add(1757647,2,r'''Solve the inequality $x^2-4x-45\le0$.''',
r'''Factor: $x^2-4x-45=(x-9)(x+5)$. The product is $0$ at $x=-5$ and $x=9$; it is negative when the factors have opposite signs, i.e.\ for $-5<x<9$, and positive for $x<-5$ or $x>9$. Including the zeros (because of $\le$), the solution is $\boxed{-5\le x\le9}$, i.e.\ $[-5,9]$.''',
'Inequalities|Quadratic equations|Factoring',2)

# ---------------- 1757367 right triangles and probability
fig=r'''draw((0,0)--(15,0)--(0,10)--cycle,linewidth(0.9));
draw((0,0)--(0.8,0)--(0.8,0.8)--(0,0.8));
label("$15$",(7.5,0),S);label("$10$",(0,5),W);label("area $75$",(7.5,-3.2));
draw(shift(19,0)*((0,0)--(5,0)--(0,20)--cycle),linewidth(0.9));
draw(shift(19,0)*((0,0)--(0.8,0)--(0.8,0.8)--(0,0.8)));
label("$5$",(21.5,0),S);label("$20$",(19,10),W);label("area $50$",(21.5,-3.2));'''
b.add(1757367,1,r'''The larger of two right triangles has area numerically equal to $3$ times the sum of its integer leg lengths $a$ and $b$. The other right triangle has area numerically equal to $2$ times the sum of its integer leg lengths $c$ and $d$. If the areas of the triangles are in the ratio $3:2$, what is the value of $a+b+c+d$?''',
r'''The conditions are $\dfrac{ab}{2}=3(a+b)$ and $\dfrac{cd}{2}=2(c+d)$. The ratio of areas is $\dfrac{3(a+b)}{2(c+d)}=\dfrac32$, so $a+b=c+d$.

From $ab=6a+6b$ we get $(a-6)(b-6)=36$, and from $cd=4c+4d$ we get $(c-4)(d-4)=16$ (both factors positive, since $a,b>6$ and $c,d>4$ follow from the equations with positive legs). With $a-6=u$, $b-6=\dfrac{36}u$, the possible sums $a+b=12+u+\dfrac{36}u$ are $49,32,27,25,24$ (for $u=1,2,3,4,6$). With $c-4=v$, the sums $c+d=8+v+\dfrac{16}v$ are $25,18,16$ (for $v=1,2,4$). The only common value is $25$: legs $10,15$ (area $75=3\cdot25$) and $5,20$ (area $50=2\cdot25$), ratio $75:50=3:2$.
'''+asy(fig,'7cm')+r'''
Hence $a+b+c+d=\boxed{50}$.''',
'Right triangles|Diophantine equations|Factoring|Lengths, perimeter, and area',4,
note='Checked by brute force over legs up to 200.')
fig=r'''fill((3,0)--(10,7)--(10,10)--(7,10)--(0,3)--(0,0)--cycle,paleblue);
draw((0,0)--(10,0)--(10,10)--(0,10)--cycle,linewidth(0.8));
draw((10,0)--(12,0),Arrow(6));draw((0,10)--(0,12),Arrow(6));
draw((3,0)--(10,7),dashed);draw((0,3)--(7,10),dashed);
label("$x$",(12,0),E);label("$y$",(0,12),N);label("$0$",(0,0),SW);
label("$3$",(3,0),S);label("$10$",(10,0),S);label("$3$",(0,3),W);label("$10$",(0,10),W);
label(rotate(45)*"$|x-y|<3$",(5,5));
label("$\dfrac{49}{2}$",(23/3,7/3));label("$\dfrac{49}{2}$",(7/3,23/3));'''
b.add(1757367,2,r'''Two real numbers from $0$ to $10$, inclusive, are chosen independently and uniformly at random. What is the probability that the absolute difference between the two numbers is less than $3$? Express your answer as a common fraction.''',
r'''Represent the pair $(x,y)$ as a point of the square $[0,10]\times[0,10]$, of area $100$. The condition $|x-y|<3$ describes the band between the lines $y=x-3$ and $y=x+3$.
'''+asy(fig,'5cm')+r'''
The two corners outside the band are right isosceles triangles with legs $7$, each of area $\dfrac{49}2$ (as marked), so together $49$. The probability is
\[
\dfrac{100-49}{100}=\boxed{\dfrac{51}{100}} .
\]''',
'Geometric probability|Probability|Lengths, perimeter, and area',3)

# ---------------- 1754235 five problems
b.add(1754235,1,r'''If $19997^2-N=19994^2$, find $N$.''',
r'''$N=19997^2-19994^2=(19997-19994)(19997+19994)=3\cdot39991=\boxed{119973}$.''',
'Difference of squares',1)
b.add(1754235,2,r'''There were $2019$ inhabitants on an island, each a knight, who always tells the truth, or a knave, who always lies. Every day one inhabitant declared, ``When I depart the island, there will be an equal number of knights and knaves left,'' and then immediately left the island. After $2019$ days there were no inhabitants left on the island. How many knaves were there on the island initially?''',
r'''Work backwards from the last day. Number the days $1,\dots,2019$; after the speaker of day $d$ leaves, $2019-d$ people remain.

On day $2019$ the speaker leaves nobody: $0$ knights and $0$ knaves, so the statement is true and the speaker is a knight.

\textbf{Claim.} After the speaker of day $d$ leaves, if $2019-d$ is even the remaining people are half knights and half knaves; and the speaker of day $d$ is a knight if $2019-d$ is even, a knave if it is odd.

Prove it backwards on $d$. If $2019-d$ is odd, an equal split of the $2019-d$ remaining people is impossible, so the statement is false and the speaker is a knave. If $2019-d$ is even, the people remaining are the speakers of days $d+1,\dots,2019$; by the claim for those later days they are, from day $2019$ backwards, knight, knave, knight, knave, \dots, ending with a knave on day $d+1$, so there are equally many of each. The statement is true and the speaker of day $d$ is a knight.

Hence the speakers on the odd days $1,3,\dots,2019$ are knights ($1010$ of them) and those on the even days $2,4,\dots,2018$ are knaves. The number of knaves is $\boxed{1009}$.''',
'Truth-tellers and liars|Working backwards|Parity|Logical deduction',3)
fig=r'''for(int i=0;i<7;++i) draw(box((i,0),(i+1,1)),linewidth(0.8));
fill(box((0,0),(1,1)),gray(0.6));fill(box((3,0),(4,1)),gray(0.6));fill(box((5,0),(6,1)),gray(0.6));
for(int i=0;i<7;++i) draw(box((i,0),(i+1,1)),linewidth(0.8));'''
b.add(1754235,3,r'''A strip consists of $7$ squares in a row. In how many different ways can you colour three of the squares (all in the same colour) so that no two neighbouring squares are coloured?''',
r'''One admissible colouring is shown.
'''+asy(fig,'5cm')+r'''
Remove one uncoloured square from each of the $2$ gaps that must separate the $3$ coloured squares. This gives a bijection between admissible colourings of the $7$-strip and arbitrary choices of $3$ squares in a $5$-strip (put the separating squares back to recover the colouring). Hence the number of ways is $\dbinom53=\boxed{10}$.

Directly: if the coloured squares are in positions $a<b<c$ with $b\ge a+2$ and $c\ge b+2$, then $a<b-1<c-2$ are any three distinct positions among $1,\dots,5$.''',
'Combinations|Bijections|Arrangements with restrictions',3,
note='The strip is described in the post (7 squares in a row); its picture is not needed.')
b.add(1754235,4,r'''Dorie spent exactly $\$10.00$, with no change, buying $19$-cent stamps and $41$-cent stamps. What is the smallest total number of stamps she could have purchased?''',
r'''Let her buy $x$ stamps at $19$ cents and $y$ at $41$ cents: $19x+41y=1000$ with $x,y\ge0$. Modulo $19$: $41\equiv3$ and $1000=19\cdot52+12\equiv12$, so $3y\equiv12$, i.e.\ $y\equiv4\pmod{19}$. Since $41y\le1000$ gives $y\le24$, $y=4$ or $y=23$:
\begin{itemize}
\item $y=4$: $19x=836$, $x=44$, total $48$;
\item $y=23$: $19x=1000-943=57$, $x=3$, total $26$.
\end{itemize}
The smallest total is $\boxed{26}$.''',
'Linear Diophantine equations|Remainders and congruences|Money and currency',3)
b.add(1754235,5,r'''Alex, Ben and Ciano agreed to build a Thingamajig and sell it for $\$132{,}000$. Working individually, it would have taken them $2$, $5$ and $8$ days respectively. They worked together as a team, each working at his own constant rate, and now they divide the $\$132{,}000$ in proportion to each person's contribution to the work. How much money should Alex get?''',
r'''Per day Alex does $\dfrac12$ of the job, Ben $\dfrac15$ and Ciano $\dfrac18$. Working together for the same time, their contributions are in the ratio
\[
\dfrac12:\dfrac15:\dfrac18=20:8:5 .
\]
Alex's share is $\dfrac{20}{33}$ of the money: $\dfrac{20}{33}\cdot132000=\boxed{\$80{,}000}$. (Ben gets $\$32{,}000$ and Ciano $\$20{,}000$.)''',
'Work and rates|Ratios, proportions, and variation|Fractions',2)

b.save()
