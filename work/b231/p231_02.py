from qb import *
b=Bank('p231_02')
MTE=lambda k: src('MTE',2018,'Middle School',k,rnd='Theme')

# ---------------- 1731770 subsets mod 10; three random reals
b.add(1731770,1,r'''The positive integers $1$ through $49$ are divided into $k$ disjoint subsets so that no two integers whose sum is divisible by $10$ are in the same subset. For example, $13$ and $37$ cannot be in the same subset. What is the smallest possible value of $k$?''',
r'''\textbf{At least $5$.} The five numbers $5,15,25,35,45$ have pairwise sums $\equiv10\equiv0\pmod{10}$, so they must lie in five different subsets. Hence $k\ge5$.

\textbf{$5$ suffice.} Two numbers have a sum divisible by $10$ exactly when their residues modulo $10$ are $r$ and $10-r$ (or both are $0$, or both are $5$). Use the subsets
\begin{itemize}
\item $\{5,10\}\cup\{n: n\equiv1,2,3,4\pmod{10}\}$,
\item $\{15,20\}\cup\{n: n\equiv6,7,8,9\pmod{10}\}$,
\item $\{25,30\}$, $\{35,40\}$, $\{45\}$.
\end{itemize}
In the first subset the residues are $5,0,1,2,3,4$; no two of them add to $0$ or $10$ (two different residues from $1$--$4$ add to at most $7$, and $5+r$, $0+r$ are not multiples of $10$ for $r=1,\dots,4$). The second subset is similar with residues $5,0,6,7,8,9$ (sums of two different residues from $6$--$9$ lie between $13$ and $17$). The last three subsets contain one number $\equiv5$ and at most one number $\equiv0$. So the smallest $k$ is $\boxed{5}$.''',
'Pigeonhole principle|Remainders and congruences|Construction',3,
note='Checked by verifying the construction.')
b.add(1731770,2,r'''Three real numbers are chosen independently and uniformly at random between $0$ and $1$. What is the probability that their sum is at most $1$?''',
r'''The triples with $x,y,z\ge0$ and $x+y+z\le1$ form a tetrahedron with three perpendicular edges of length $1$ inside the unit cube, of volume $\dfrac13\cdot\dfrac12\cdot1=\dfrac16$. The probability is $\boxed{\dfrac16}$.''',
'Geometric probability|Probability',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1732639 consecutive product identity
b.add(1732639,1,r'''Take two different natural numbers $m$ and $n$. Multiply each by the next two natural numbers, getting $n(n+1)(n+2)$ and $m(m+1)(m+2)$. Subtract the smaller product from the larger and divide by the positive difference of $m$ and $n$. Finally add the product $mn$. Prove that the result is a product of two consecutive integers.''',
r'''We may assume $n>m$ (the rule is symmetric). Then
\[
n(n+1)(n+2)-m(m+1)(m+2)=\left(n^3-m^3\right)+3\left(n^2-m^2\right)+2(n-m)=(n-m)\left(n^2+nm+m^2+3n+3m+2\right),
\]
so dividing by $n-m$ gives $n^2+nm+m^2+3(n+m)+2$. Adding $mn$ and writing $s=m+n$,
\[
n^2+2mn+m^2+3(m+n)+2=s^2+3s+2=(s+1)(s+2).
\]
So the result is $\boxed{(m+n+1)(m+n+2)}$, a product of two consecutive integers. $\blacksquare$ (For example $m=1$, $n=3$: $\dfrac{60-6}{2}+3=30=5\cdot6$.)''',
'Factoring|Sum and difference of cubes|Algebraic expressions and identities',3,
note='The post\'s wording "difference by the positive difference" is read as dividing by it.')

# ---------------- 1732287 eight houses
b.add(1732287,1,r'''Each of eight houses on a street is painted red, blue or green. Each house is painted only one colour and each colour is used on at least one house. No two colours are used on the same number of houses. In how many ways could the eight houses be painted?''',
r'''The numbers of houses of the three colours are three different positive integers with sum $8$: as a set, $\{1,2,5\}$ or $\{1,3,4\}$.

For $\{1,2,5\}$: assign the three counts to the three colours in $3!=6$ ways, and then choose which houses get which colour in $\dfrac{8!}{1!\,2!\,5!}=168$ ways. For $\{1,3,4\}$: $6\cdot\dfrac{8!}{1!\,3!\,4!}=6\cdot280$ ways. Total:
\[
6(168+280)=\boxed{2688}.
\]''',
'Multiset permutations|Partitions and compositions|Casework|Multiplication principle',3,
note='Checked by enumerating all 3^8 colourings.')

# ---------------- 1147571 stars and bars
b.add(1147571,1,r'''How many ordered quadruples $(a,b,c,d)$ of positive integers satisfy $a+b+c+d=17$?''',
r'''Write $17$ as a row of $17$ ones; a solution corresponds to choosing $3$ of the $16$ gaps between consecutive ones as cut points. Hence the number of solutions is
\[
\binom{16}{3}=\boxed{560}.
\]
(The value $\binom{19}{3}=969$ counts nonnegative solutions of $a+b+c+d=16$, not positive solutions of $a+b+c+d=17$.)''',
'Stars and bars|Distributions and integer solutions',2,
source=src('Math League',None,None,None),
note='The post says "ordered pairs" for a quadruple, and the poster\'s answer 969 = C(19,3) is wrong (later acknowledged); the correct count is 560.')

# ---------------- 1732169 primes 6n+-1 (alias)
b.add(1732169,1,r'''Prove that every prime other than $2$ and $3$ can be written in the form $6n+1$ or $6n-1$, where $n$ is a positive integer.''',
r'''Every integer is $6n+r$ with $r\in\{-1,0,1,2,3,4\}$. If $r=0,2,4$ the number is even, and if $r=3$ it is divisible by $3$; a prime $p>3$ is neither, so $p=6n\pm1$, and $n\ge1$ since $p\ge5$. $\blacksquare$''',
'Prime numbers|Remainders and congruences',2,
note='Repeat of an earlier record (aliased).')

# ---------------- 1731721 MATHCOUNTS magnets
b.add(1731721,1,r'''On the refrigerator, MATHCOUNTS is spelled out with $10$ magnets, one letter per magnet. Two vowels and three consonants fall off and are put away in a bag. If the T's are indistinguishable, how many distinct possible collections of letters could be put in the bag?''',
r'''``Indistinguishable'' means that the two T's are identical, so collections that differ only in which T was taken are the same collection; we count collections by which letters they contain, not by which magnets.

The vowels are A, O, U (all different): $\binom32=3$ choices of two.

The consonants are M, T, H, C, N, T, S: six different letters, with T appearing twice. Choose three by the number of T's:
\begin{itemize}
\item no T: $\binom53=10$ (from M, H, C, N, S);
\item one T: $\binom52=10$;
\item two T's: $\binom51=5$.
\end{itemize}
That gives $25$ consonant collections. In total there are $3\cdot25=\boxed{75}$ collections.''',
'Combinations|Casework|Multiplication principle',3,
source=src('MATHCOUNTS',2006,'National',21,rnd='Sprint'))

# ---------------- 1731866 3(n-5) vs 3n-5
b.add(1731866,1,r'''A student says that $3(n-5)$ is equal to $3n-5$. Show that this is wrong, and explain the error.''',
r'''By the distributive law, $3(n-5)=3n-3\cdot5=3n-15$. So
\[
3(n-5)-(3n-5)=(3n-15)-(3n-5)=-10\ne0
\]
for every $n$; for example at $n=6$, $3(6-5)=3$ while $3\cdot6-5=13$. The two expressions are never equal. The error is multiplying only the first term $n$ by $3$: the factor $3$ must multiply both terms inside the brackets, so $3(n-5)=\boxed{3n-15}$, not $3n-5$.''',
'Algebraic expressions and identities|Linear equations',1)

# ---------------- 1731843 three warm-up problems
b.add(1731843,1,r'''A deck of $14$ cards numbered $1$ through $14$ is dealt to Ken and Gunther so that each gets $7$ cards. Each player's score is the sum of his card values, and the player with the lower score wins. How many different winning scores are possible?''',
r'''The two scores add to $1+2+\cdots+14=105$, an odd number, so there are no ties, and the winner's score $s$ satisfies $s<105-s$, i.e.\ $s\le52$. The smallest possible score is $1+2+\cdots+7=28$.

Every score from $28$ to $52$ occurs. Start from $\{1,\dots,7\}$ (sum $28$) and repeatedly increase the sum by $1$: in a $7$-card hand that is not $\{8,\dots,14\}$, some card $c$ has $c+1\le14$ not in the hand (take the largest card $c$ such that $c+1$ is missing); replacing $c$ by $c+1$ raises the sum by exactly $1$. So all sums from $28$ up to $77$ occur, in particular $28,\dots,52$. The number of winning scores is $52-28+1=\boxed{25}$.''',
'Summation|Bounding and extremal cases|Construction',3,
source=src('MATHCOUNTS',None,'Handbook',None,rnd='Warm-Up'),
note='Repeat of an earlier record from the previous run (aliased). Checked by enumerating all 7-card hands.')
b.add(1731843,2,r'''All test scores are integers from $0$ to $100$, inclusive. What is the least possible median of five test scores that add to $204$?''',
r'''Order the scores $a\le b\le c\le d\le e$; the median is $c$. Since $d,e\le100$, $a+b+c\ge204-200=4$, and since $a,b\le c$, $3c\ge4$, so $c\ge2$. The scores $0,2,2,100,100$ (sum $204$) have median $2$. The answer is $\boxed{2}$.''',
'Median|Bounding and extremal cases',2,
source=src('MATHCOUNTS',None,'Handbook',None,rnd='Warm-Up'))
b.add(1731843,3,r'''Don's signature coffee blend is $60\%$ dark roast and $40\%$ light roast. He has $10$ kg of blend A, which is $80\%$ dark roast and $20\%$ light roast, and $10$ kg of blend B, which is $20\%$ dark roast and $80\%$ light roast. How many kilograms of blend A will Don need to use to make $10$ kg of his signature blend? Express your answer as a mixed number.''',
r'''Use $x$ kg of A and $10-x$ kg of B. The dark roast must total $60\%$ of $10$ kg:
\[
0.8x+0.2(10-x)=6\ \Longrightarrow\ 0.6x=4\ \Longrightarrow\ x=\dfrac{20}{3}.
\]
He needs $\boxed{6\dfrac23}$ kg of blend A (and $3\dfrac13$ kg of blend B; both are available).''',
'Mixture problems|Percentages|Linear equations',2,
source=src('MATHCOUNTS',None,'Handbook',None,rnd='Warm-Up'))

# ---------------- 1731473 divisorous (alias)
b.add(1731473,1,r'''Call a positive integer $N$ divisorous if the ones digits of the positive divisors of $N$ include all of the base ten digits from $0$ to $9$. What is the least positive integer that is divisorous?''',
r'''$N$ needs a divisor ending in $0$, so $10\mid N$; a divisor ending in $9$ and one ending in $7$ are needed too. Checking multiples of $10$ shows the least is $\boxed{270}$, with divisors $1,2,3,5,6,9,10,15,18,27,30,45,54,90,135,270$.''',
'Factors and multiples|Units digits and last digits|Divisibility',3,
source=src('MathWorks',2016,None,None),
note='Repeat of an earlier record (aliased).')

# ---------------- 336615 AMC 8 2006 #22
b.add(336615,1,r'''Three different one-digit positive integers are placed in the three cells of the bottom row of a triangular array of cells (three cells in the bottom row, two in the middle row, one at the top). Numbers in adjacent cells are added and the sum is placed in the cell above them. In the second row the same process gives the number in the top cell. What is the difference between the largest and smallest numbers possible in the top cell?

$\textbf{(A)}\ 16\qquad\textbf{(B)}\ 24\qquad\textbf{(C)}\ 25\qquad\textbf{(D)}\ 26\qquad\textbf{(E)}\ 35$''',
r'''If the bottom row is $a,b,c$, the middle row is $a+b$, $b+c$ and the top cell holds $a+2b+c$. The middle number counts twice.

Largest: put $9$ in the middle and $8,7$ at the ends: $8+18+7=33$. Smallest: put $1$ in the middle and $2,3$ at the ends: $2+2+3=7$. (These are optimal: $a+2b+c=(a+b+c)+b$ is largest when $\{a,b,c\}=\{7,8,9\}$ with $b=9$ and smallest when $\{a,b,c\}=\{1,2,3\}$ with $b=1$.) The difference is $33-7=26$, answer $\boxed{\textbf{(D)}\ 26}$.''',
'Bounding and extremal cases|Whole-number operations',2,
source=src('AMC 8',2006,None,22),
note='The figure (a three-row triangular array of cells) is described in words.')

# ---------------- 1731478 2^2000 mod 13 (alias)
b.add(1731478,1,r'''Find the remainder when $2^{2000}$ is divided by $13$.''',
r'''By Fermat's little theorem $2^{12}\equiv1\pmod{13}$. Since $2000=12\cdot166+8$, $2^{2000}\equiv2^8=256\equiv\boxed{9}\pmod{13}$.''',
'Fermat\'s little theorem|Modular exponentiation|Remainders and congruences',2,
note='Repeat of an earlier record (aliased). The poster\'s observed period 12 is Fermat\'s little theorem.')

# ---------------- 1731491 11^2014 mod 1000 (alias)
b.add(1731491,1,r'''What is the remainder when $11^{2014}$ is divided by $1000$? (A student expanded $(10+1)^{2014}$ as $10^{2014}+10^{2013}+\cdots+10+1$ and got $111$; find the error.)''',
r'''The binomial theorem gives $(10+1)^{2014}=\sum_k\binom{2014}{k}10^k$; the student dropped the coefficients. Modulo $1000$ only $k\le2$ matter: $1+2014\cdot10+\binom{2014}{2}\cdot100\equiv1+140+100=\boxed{241}$, since $\binom{2014}{2}=2027091$ is odd.''',
'Binomial theorem|Modular exponentiation|Remainders and congruences',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1731288 flavours
b.add(1731288,1,r'''An ice-cream shop has $5$ flavours, and a customer chooses $2$ scoops; the two scoops may be the same flavour, and the order of the scoops does not matter. How many different choices are there? Explain why $5^2$ is not the answer, and say what $5^2$ counts.''',
r'''Count by whether the flavours are equal: two different flavours in $\binom52=10$ ways, or the same flavour twice in $5$ ways. Total $\boxed{15}$. This agrees with the formula for combinations with repetition, $\binom{5+2-1}{2}=\binom62=15$.

$5^2=25$ counts \emph{ordered} pairs (first scoop, second scoop). In that count each choice of two different flavours appears twice (as $(x,y)$ and $(y,x)$) and each double flavour once: $25=2\cdot10+5$. Since order does not matter here, $25$ overcounts; and $25$ cannot simply be halved because the $5$ doubles are not counted twice. (If the two flavours must be different, the answer is $10$.)''',
'Combinations|Stars and bars|Counting principles',2,
note='The post asks whether 5^2 works for "combinations of 2 flavours from 5"; the record fixes the reading (repetition allowed, order irrelevant: 15) and explains 25 and 10.')

# ---------------- 1657695 2018 MS MTE Theme Round (15 problems)
b.add(1657695,1,r'''If $r$ and $s$ are the roots of $x^2+6x+8$, find $\dfrac4r+\dfrac4s$.''',
r'''By Vieta's formulas $r+s=-6$ and $rs=8$, so
\[
\dfrac4r+\dfrac4s=\dfrac{4(r+s)}{rs}=\dfrac{-24}{8}=\boxed{-3}.
\]
(Directly: the roots are $-2$ and $-4$, and $-2-1=-3$.)''',
'Vieta\'s formulas|Quadratic equations',1,source=MTE(1))
b.add(1657695,2,r'''Given that $\dfrac{3-2x}{4x^2+8x+3}=\dfrac{2}{2x+1}-\dfrac{3}{2x+3}$, evaluate
\[
\sum_{k=1}^{3}\dfrac{3-2k}{4k^2+8k+3}.
\]''',
r'''Using the given decomposition,
\[
\sum_{k=1}^{3}\left(\dfrac{2}{2k+1}-\dfrac{3}{2k+3}\right)=\left(\dfrac23-\dfrac35\right)+\left(\dfrac25-\dfrac37\right)+\left(\dfrac27-\dfrac39\right)=\dfrac23-\dfrac15-\dfrac17-\dfrac13 .
\]
This is $\dfrac13-\dfrac{12}{35}=\dfrac{35-36}{105}=\boxed{-\dfrac{1}{105}}$. (Check: $\dfrac1{15}-\dfrac1{35}-\dfrac{3}{63}=\dfrac{7-3-5}{105}$.)''',
'Partial fractions|Telescoping sums|Summation',2,source=MTE(2))
b.add(1657695,3,r'''Jill has two geometric sequences, each consisting of $3$ consecutive terms. The first sequence is $\left(1,\ x-1,\ x^3-12x^2+42x-31\right)$ and the second is $\left(1,\ x-2,\ x^3-11x^2+32x-28\right)$. What is the value of $x$?''',
r'''Three terms $1,q,t$ form a geometric sequence exactly when $t=q^2$. So
\[
x^3-12x^2+42x-31=(x-1)^2\iff x^3-13x^2+44x-32=0,
\]
\[
x^3-11x^2+32x-28=(x-2)^2\iff x^3-12x^2+36x-32=0 .
\]
Subtracting the first from the second gives $x^2-8x=0$, so $x=0$ or $x=8$. $x=0$ fails the first equation ($-32\ne0$), while $x=8$ satisfies both ($512-832+352-32=0$ and $512-768+288-32=0$). So $x=\boxed{8}$; the sequences are $(1,7,49)$ and $(1,6,36)$.''',
'Geometric sequences|Polynomials|Equations and systems of equations',3,source=MTE(3))
b.add(1657695,4,r'''Find the sum of the coefficients of the polynomial
\[
\dfrac{264x^3+792x^2+528x}{\left(\dfrac{4!\cdot6!}{720}\right)}.
\]''',
r'''Since $6!=720$, the denominator is $4!=24$, and the polynomial is $11x^3+33x^2+22x$. The sum of its coefficients is its value at $x=1$: $11+33+22=\boxed{66}$.''',
'Polynomials|Factorials',1,source=MTE(4))
b.add(1657695,5,r'''The polynomial $f(x)=4x^3-48x^2+189x-243$ satisfies $f(3)=0$ and has a double root. What is the sum of the distinct roots of $f$?''',
r'''Divide by $x-3$:
\[
f(x)=(x-3)\left(4x^2-36x+81\right)=(x-3)(2x-9)^2 .
\]
So the roots are $3$ and the double root $\dfrac92$, and the sum of the distinct roots is $3+\dfrac92=\boxed{\dfrac{15}{2}}$.''',
'Polynomial roots|Factoring|Remainder theorem and factor theorem',2,source=MTE(5),
note='The original says f has an inverse g with g(0) = 3. But f(x) = (x - 3)(2x - 9)^2 has f\'(x) = (2x - 9)(6x - 21), so f is not one-to-one and has no inverse; the condition is replaced by its intended content f(3) = 0.')
f6=r'''pair P1=(1,2),P2=(18,3),P3=(6,5);
draw((-0.5,0)--(19.5,0),Arrow(6));draw((0,-0.5)--(0,6.5),Arrow(6));
label("$x$",(19.5,0),SE);label("$y$",(0,6.5),NW);
draw(P1--P2--P3--cycle,linewidth(0.9));
dot(P1);dot(P2);dot(P3);
label("$(1,2)$",P1,SE);label("$(18,3)$",P2,SE);label("$(6,5)$",P3,N);'''
b.add(1657695,6,r'''A triangle in the Cartesian plane has vertices $(x,2)$, $(18,3x)$ and $(6,5x)$. Let $p(x)$ be the polynomial with $p(0)<0$ such that $\left|p(x)\right|$ is the area of the triangle for all real numbers $x$. What is the sum of the coefficients of $p(x)$?''',
r'''By the shoelace formula the area is
\[
\dfrac12\left|x(3x-5x)+18(5x-2)+6(2-3x)\right|=\dfrac12\left|-2x^2+72x-24\right|=\left|-x^2+36x-12\right| .
\]
The polynomials whose absolute value equals this for all $x$ are $\pm\left(-x^2+36x-12\right)$; the one with $p(0)<0$ is $p(x)=-x^2+36x-12$. The sum of its coefficients is $p(1)=-1+36-12=\boxed{23}$. For $x=1$ the triangle is the one shown, with area $23$.
'''+asy(f6,'7cm'),
'Shoelace formula|Coordinate geometry|Polynomials',3,source=MTE(6),
note='As posted, p is determined only up to sign (sum of coefficients 23 or -23); the condition p(0) < 0 is added to fix the intended answer 23.')
b.add(1657695,7,r'''Three integers are chosen independently and uniformly at random from the interval $[-1,1]$ (that is, each is $-1$, $0$ or $1$). What is the probability that these three integers are the roots of a polynomial $x^3+ax^2+bx+c$ with $a,c\in[0,1]$?''',
r'''Numbers $r,s,t$ are the roots (with multiplicity) of the monic cubic $(x-r)(x-s)(x-t)=x^3+ax^2+bx+c$ with $a=-(r+s+t)$, $b=rs+st+tr$, $c=-rst$; $b$ is unrestricted. So we need
\[
r+s+t\in\{-1,0\}\quad\text{and}\quad rst\in\{-1,0\}.
\]
If none of the numbers is $0$, they are $\pm1$; then $rst=-1$ needs one or three $-1$'s, with sums $1$ or $-3$, which fail. So at least one number is $0$ (and then $rst=0$), and we need the sum to be $-1$ or $0$. Count ordered triples:
\begin{itemize}
\item sum $0$: $(0,0,0)$, and the arrangements of $\{0,1,-1\}$: $1+6=7$;
\item sum $-1$: arrangements of $\{0,0,-1\}$: $3$.
\end{itemize}
That is $10$ of the $27$ equally likely triples, so the probability is $\boxed{\dfrac{10}{27}}$.''',
'Vieta\'s formulas|Probability|Polynomial roots|Casework',3,source=MTE(7),
note='"Three integers chosen from [-1,1]" read as three independent uniform choices from {-1,0,1} (27 ordered outcomes). Checked by enumeration.')
b.add(1657695,8,r'''The polynomial $P(x)=x^3+2x^2+4x+8$ has roots $a$, $b$ and $c$. Find $\dfrac1a+\dfrac1b+\dfrac1c$.''',
r'''By Vieta's formulas $ab+bc+ca=4$ and $abc=-8$. So
\[
\dfrac1a+\dfrac1b+\dfrac1c=\dfrac{ab+bc+ca}{abc}=\dfrac{4}{-8}=\boxed{-\dfrac12}.
\]''',
'Vieta\'s formulas|Polynomial roots',2,source=MTE(8))
b.add(1657695,9,r'''If eighteen times $x$ minus $1$ is equal to the square of $x$, what is the units digit of $x^{2048}+x^{-2048}$?''',
r'''From $x^2=18x-1$ we get $x\ne0$ and $x+\dfrac1x=18$. Let $s_n=x^n+x^{-n}$. Then $s_{2n}=s_n^2-2$, and every $s_{2^k}$ is an integer: $s_1=18$, $s_2=18^2-2=322$, and each later term is the square of the previous one minus $2$. If $s_n$ ends in $2$, then $s_n^2$ ends in $4$ and $s_{2n}$ ends in $2$. Since $s_2$ ends in $2$, so do $s_4,s_8,\dots,s_{2048}$ ($2048=2^{11}$). The units digit is $\boxed{2}$.''',
'Recurrence relations|Units digits and last digits|Algebraic expressions and identities',3,source=MTE(9))
f10=r'''real x=13,y=16;
filldraw((0,0)--(2,0)--(2,2)--(0,2)--cycle,lightgray,gray);
filldraw((x-2,0)--(x,0)--(x,2)--(x-2,2)--cycle,lightgray,gray);
filldraw((0,y-2)--(2,y-2)--(2,y)--(0,y)--cycle,lightgray,gray);
filldraw((x-2,y-2)--(x,y-2)--(x,y)--(x-2,y)--cycle,lightgray,gray);
draw((0,0)--(x,0)--(x,y)--(0,y)--cycle,linewidth(0.9));
draw((2,2)--(x-2,2)--(x-2,y-2)--(2,y-2)--cycle,dashed);
label("$x$",(x/2,0),S);label("$y$",(x,y/2),E);
label("$2$",(1,2),N);label("$2$",(2,1),E);
label("$x-4$",(x/2,2),N);label("$y-4$",(2,y/2),E);'''
b.add(1657695,10,r'''Joe has a paper rectangle with side lengths $x$ and $y$, where $x$ and $y$ are integers greater than $4$. He cuts out a $2\times2$ square from each corner, then folds the sides upward to make an open box. Finally, he closes the top with another rectangle. If the volume of the new shape is $216$ cubic units, how many ordered pairs $(x,y)$ are possible?''',
r'''After the corners are cut out, the base is $(x-4)\times(y-4)$ and the folded sides have height $2$ (dashed lines are the folds).
'''+asy(f10,'5cm')+r'''
So the volume is $2(x-4)(y-4)=216$, i.e.\ $(x-4)(y-4)=108$. With $u=x-4$ and $v=y-4$ positive integers, the ordered pairs correspond to the ordered factorisations $uv=108=2^2\cdot3^3$, one for each divisor $u$ of $108$. The number of divisors is $(2+1)(3+1)=12$, so there are $\boxed{12}$ ordered pairs.''',
'Volume|Cubes and rectangular prisms|Divisor counting',3,source=MTE(10),
note='Integer side lengths are assumed (otherwise there are infinitely many pairs); the volume is that of the closed box, base (x-4)(y-4) and height 2.')
b.add(1657695,11,r'''Let $p$, $q$ and $r$ be the roots of $x^3+20x^2+18x-2018$.
\begin{enumerate}
\item[(a)] Compute $\dfrac{pqr}{2(pq+qr+rp)}$, which would be the ratio of the volume to the surface area of a rectangular prism with edge lengths $p,q,r$.
\item[(b)] Show that, in fact, no rectangular prism has edge lengths $p$, $q$, $r$.
\end{enumerate}''',
r'''\textbf{(a)} By Vieta's formulas, $p+q+r=-20$, $pq+qr+rp=18$ and $pqr=2018$. So
\[
\dfrac{pqr}{2(pq+qr+rp)}=\dfrac{2018}{36}=\boxed{\dfrac{1009}{18}}.
\]

\textbf{(b)} Edge lengths must be positive real numbers, but $p+q+r=-20<0$, so the roots are not all positive reals. (In fact the cubic has exactly one positive root: for $x>0$ it is increasing; the other two roots are negative or non-real.) So the prism cannot exist, and the value in (a) is only a formal ratio.''',
'Vieta\'s formulas|Polynomial roots',2,source=MTE(11),
note='Ill-posed as stated: the roots have sum -20, so they cannot all be side lengths (the problem title itself asks "is this prism even possible?"). The record asks for the formal value 1009/18 and for the proof that the prism does not exist.')
f12=r'''real a=4,bb=2,c=5;
real cx=(bb*bb+c*c-a*a)/(2*c);
pair A=(0,0),B=(c,0),C=(cx,sqrt(bb*bb-cx*cx));
draw(A--B--C--cycle,linewidth(0.9));
label("$5$",(A+B)/2,S);label("$2$",(A+C)/2,W);label("$4$",(B+C)/2,NE);'''
b.add(1657695,12,r'''Let $a,b,c$ be the integer side lengths of a scalene triangle, where $a,b,c$ are not three consecutive integers and $c$ is the largest side. Given that $x=a+b-2c$ is a root of the polynomial $f(x)=x^2+k$, where $k$ is a constant, what is the largest possible value of $k$?''',
r'''Since $x$ is a root of $x^2+k$, $k=-x^2=-(a+b-2c)^2$, so we want $|a+b-2c|=(c-a)+(c-b)$ as small as possible. As the triangle is scalene with $c$ largest, $c-a$ and $c-b$ are different positive integers, so their sum is at least $1+2=3$, and the sum $3$ means the sides are $c-2,c-1,c$: consecutive, which is excluded. The sum cannot be $3$ otherwise, so it is at least $4$, attained by $\{c-a,c-b\}=\{1,3\}$, e.g.\ sides $2,4,5$ (a valid triangle as $2+4>5$).
'''+asy(f12,'4.5cm')+r'''
Then $x=-4$ and the largest $k$ is $-16$. The answer is $\boxed{-16}$.''',
'Triangle inequality|Triangles|Bounding and extremal cases|Quadratic equations',3,source=MTE(12))
b.add(1657695,13,r'''Let $P(x)=(x-3)(x-9)$, and let $G_n(x)$ denote $P$ applied $n$ times: $G_1(x)=P(x)$, $G_2(x)=P(P(x))$, $G_3(x)=P(P(P(x)))$, and so forth. What is the sum of the roots of $G_{10}(x)$, counted with multiplicity?''',
r'''$G_n$ has degree $2^n$. Its roots are the solutions of $P(x)=y$ as $y$ runs over the $2^{n-1}$ roots of $G_{n-1}$ (with multiplicity), because $G_n(x)=G_{n-1}(P(x))$. For each such $y$, the equation $x^2-12x+27-y=0$ has two roots with sum $12$. So the sum of the roots of $G_n$ is $12\cdot2^{n-1}$, and for $n=10$ it is $12\cdot512=\boxed{6144}$.''',
'Vieta\'s formulas|Polynomial roots|Functions',3,source=MTE(13),
note='The notation "G(1) = P(x), G(2) = P(P(x)), ..." is written as G_n(x); roots are counted with multiplicity.')
b.add(1657695,14,r'''Let $f(x)=2x^5+x^4-26x^3-13x^2+72x+36$, and define $g(x)=f(x+4)$. Find the sum of the roots of $g(x)=0$.''',
r'''If $f$ has roots $r_1,\dots,r_5$, then $g(x)=f(x+4)=0$ exactly when $x+4=r_i$, so $g$ has roots $r_i-4$. By Vieta's formulas $\sum r_i=-\dfrac12$, so the sum of the roots of $g$ is $-\dfrac12-5\cdot4=\boxed{-\dfrac{41}{2}}$. (In fact $f(x)=(2x+1)(x^2-4)(x^2-9)$ with roots $-\dfrac12,\pm2,\pm3$.)''',
'Vieta\'s formulas|Polynomial roots',2,source=MTE(14))
b.add(1657695,15,r'''If $r,s,t$ are the roots of $2x^3+10x+8$, determine $r^2+rs+rt+s^2+st+t^2$.''',
r'''By Vieta's formulas, $r+s+t=0$ and $rs+st+tr=\dfrac{10}{2}=5$. Then
\[
r^2+s^2+t^2+rs+st+tr=(r+s+t)^2-(rs+st+tr)=0-5=\boxed{-5}.
\]''',
'Vieta\'s formulas|Algebraic expressions and identities',2,source=MTE(15))

# ---------------- 1731212 sqrt10 x + sqrt6 y
b.add(1731212,1,r'''Rational numbers $x$ and $y$ satisfy $\sqrt{10}\,x+\sqrt6\,y=\sqrt{4-\sqrt{15}}$. Find $x+y+xy$.''',
r'''Denest the right side: $\left(\sqrt{10}-\sqrt6\right)^2=16-2\sqrt{60}=16-4\sqrt{15}=4\left(4-\sqrt{15}\right)$, and $\sqrt{10}>\sqrt6$, so
\[
\sqrt{4-\sqrt{15}}=\dfrac{\sqrt{10}-\sqrt6}{2}.
\]
Hence $\left(x-\dfrac12\right)\sqrt{10}=-\left(y+\dfrac12\right)\sqrt6$. If $y\ne-\dfrac12$, dividing gives $\dfrac{\sqrt{10}}{\sqrt6}=-\dfrac{y+\dfrac12}{x-\dfrac12}$, a rational number; but $\dfrac{\sqrt{10}}{\sqrt6}=\dfrac{\sqrt{15}}{3}$ is irrational. So $y=-\dfrac12$, and then $\left(x-\dfrac12\right)\sqrt{10}=0$ gives $x=\dfrac12$. Therefore
\[
x+y+xy=0-\dfrac14=\boxed{-\dfrac14}.
\]''',
'Radicals|Algebraic manipulation',4,
note='The post does not say that x and y are rational; without that, x + y + xy is not determined, so the condition is added (intended reading).')

# ---------------- 1730716 sqrt(x + sqrt2011/2) - sqrt(x - sqrt2011/2)
b.add(1730716,1,r'''Let $x$ be an integer such that
\[
\sqrt{x+\dfrac12\sqrt{2011}}-\sqrt{x-\dfrac12\sqrt{2011}}
\]
is an integer. Find $x$.''',
r'''Let the expression be $y$; it is a positive integer (the first root is larger, and the expression is defined only for $x\ge\dfrac12\sqrt{2011}>0$). Squaring,
\[
y^2=2x-2\sqrt{x^2-\dfrac{2011}{4}}=2x-\sqrt{4x^2-2011}.
\]
So $\sqrt{4x^2-2011}=2x-y^2$ is an integer, i.e.\ $4x^2-2011=m^2$ for a nonnegative integer $m$. Then $(2x-m)(2x+m)=2011$, and $2011$ is prime, so $2x+m=2011$ and $2x-m=1$, giving $x=503$, $m=1005$. Then $y^2=1006-1005=1$, so $y=1$, an integer. Hence $x=\boxed{503}$.''',
'Radicals|Difference of squares|Diophantine equations|Prime numbers',4,
note='Repeat of an earlier record (aliased). From "a 2011 test" (contest not named). Checked numerically.')

# ---------------- 1111533 nested fraction
b.add(1111533,1,r'''Simplify
\[
1-\dfrac{1}{1-\dfrac{1}{1-\dfrac{1}{x-1}}}
\]
and state for which real $x$ the expression is defined.''',
r'''Work from the inside out. For $x\ne1$,
\[
1-\dfrac1{x-1}=\dfrac{x-2}{x-1},
\]
which must be nonzero, so $x\ne2$. Then
\[
\dfrac{1}{\dfrac{x-2}{x-1}}=\dfrac{x-1}{x-2},\qquad 1-\dfrac{x-1}{x-2}=\dfrac{-1}{x-2}\ (\ne0),
\]
\[
\dfrac{1}{\dfrac{-1}{x-2}}=-(x-2)=2-x,\qquad 1-(2-x)=x-1 .
\]
So the expression equals $\boxed{x-1}$, defined for all real $x$ except $x=1$ and $x=2$.''',
'Fractions|Rational equations|Algebraic manipulation',2,
note='The post says "solve for x" but gives no equation, and its LaTeX has a \\frac with a missing argument; read as the continued fraction 1 - 1/(1 - 1/(1 - 1/(x-1))) to be simplified. Checked symbolically.')

# ---------------- 1730856 divisibility by 11 (alias)
b.add(1730856,1,r'''Prove the divisibility rule for $11$: a positive integer is divisible by $11$ if and only if the alternating sum of its digits (units digit minus tens digit plus hundreds digit, and so on) is divisible by $11$.''',
r'''If $N=\sum_k d_k10^k$, then since $10\equiv-1\pmod{11}$, $N\equiv\sum_k d_k(-1)^k\pmod{11}$. So $11\mid N$ exactly when $11$ divides the alternating digit sum. $\blacksquare$''',
'Divisibility rules|Remainders and congruences|Digits and bases',2,
note='Repeat of an earlier record (aliased).')

# ---------------- 1730732 SAY x 3 = BABY
b.add(1730732,1,r'''In the multiplication $\overline{SAY}\times3=\overline{BABY}$, different letters represent different digits (and the leading digits $S$ and $B$ are not $0$). What three-digit number does $\overline{SAY}$ represent?''',
r'''\textbf{Setting up.} $\overline{SAY}\times3<1000\cdot3=3000$, so $B\le2$. Also $3Y$ ends in $Y$, so $2Y\equiv0\pmod{10}$ and $Y\in\{0,5\}$.

Writing the equation as
\[
300S+30A+3Y=1000B+100A+10B+Y,
\]
we get $300S=1010B+70A-2Y$. \textbf{$B=2$ is impossible.} For $B=2$: $300S=2020+70A-2Y$. With $Y=0$ the right side $2020+70A$ is a multiple of $300$ for no digit $A$ ($2020+70A\equiv20+70A\pmod{100}$, which needs $70A\equiv80\pmod{100}$, i.e.\ $7A\equiv8\pmod{10}$, $A=4$, giving $2300$, not a multiple of $300$). With $Y=5$: $2010+70A\equiv10+70A\pmod{100}$ needs $7A\equiv9\pmod{10}$, $A=7$, giving $2500$, not a multiple of $300$. So $B=1$.

\textbf{$B=1$.} Now $300S=1010+70A-2Y$. With $Y=5$: $1000+70A\equiv70A\pmod{100}$ needs $A=0$, giving $1000$, not a multiple of $300$. With $Y=0$: $1010+70A\equiv10+70A\pmod{100}$ needs $7A\equiv9\pmod{10}$, $A=7$, giving $1500=300\cdot5$, so $S=5$.

So $S=5$, $A=7$, $Y=0$, $B=1$, all different, and $\overline{SAY}=\boxed{570}$: indeed $570\times3=1710$.''',
'Cryptarithms|Digit problems|Remainders and congruences',3,
note='Checked by trying all digit assignments; the solution is unique.')

b.save()
