from qb import *
b=Bank('p227_02')

# ---------------- 1755393 work
b.add(1755393,1,r'''$A$ and $B$ working together can complete a piece of work in $30$ days. After they have both worked for $18$ days, $A$ leaves and $B$ finishes the work alone in $20$ more days. Find the time in which each of them can do the work alone.''',
r'''Together they do $\dfrac1{30}$ of the work per day, so in $18$ days they do $\dfrac{18}{30}=\dfrac35$ of it. The remaining $\dfrac25$ takes $B$ alone $20$ days, so $B$ does $\dfrac{2}{5\cdot20}=\dfrac1{50}$ of the work per day. Then $A$ does $\dfrac1{30}-\dfrac1{50}=\dfrac{5-3}{150}=\dfrac1{75}$ per day. Alone, $\boxed{A\text{ needs }75\text{ days and }B\text{ needs }50\text{ days}}$.''',
'Work and rates|Fractions',2)

# ---------------- 1756280 interval difference
b.add(1756280,1,r'''Write the set difference $(-3,5]\setminus(-\infty,2]$ in interval notation.''',
r'''The set difference consists of the numbers in $(-3,5]$, i.e.\ with $-3<x\le5$, that are not in $(-\infty,2]$, i.e.\ with $x>2$. Both conditions together give $2<x\le5$, so the answer is $\boxed{(2,5]}$. The endpoint $2$ is excluded because it belongs to $(-\infty,2]$, and $5$ is included because it belongs to $(-3,5]$.''',
'Inequalities',1,
note='The post writes the difference with a minus sign, "(-3,5] - (-oo,2]"; it is read as the set difference.')

# ---------------- 1754490 probability of a single point
b.add(1754490,1,r'''A real number $X$ is chosen uniformly at random from the interval $[0,69]$. Show that the probability that $X$ equals exactly $1$ is $0$, and explain why this does not contradict the fact that $X=1$ is possible.''',
r'''For a uniform choice on $[0,69]$, the probability that $X$ lies in a subinterval is its length divided by $69$. For every $\varepsilon$ with $0<\varepsilon<1$, the event $X=1$ is contained in the event $1-\varepsilon\le X\le1+\varepsilon$, so
\[
0\le P(X=1)\le\dfrac{2\varepsilon}{69}.
\]
Since this holds for every positive $\varepsilon$, however small, $P(X=1)=\boxed{0}$.

There is no contradiction: probability $0$ does not mean impossible. For a continuous choice every single value has probability $0$ (otherwise, if each of infinitely many points had the same positive probability, the total would exceed $1$); probabilities only become positive for sets of positive length. The expression ``$\dfrac1\infty$'' is not a number; the precise statement is the limit argument above.''',
'Geometric probability|Probability',2,
note='Conceptual post turned into a short exercise with a proof.')

# ---------------- 1756743 perpendicular bisector
fig=r'''import graph;
xaxis(Label("$x$",position=EndPoint,align=E),-4,10,Arrow(6));
yaxis(Label("$y$",position=EndPoint,align=N),-1,7,Arrow(6));
pair P=(-2,4),Q=(8,4),M=(3,4);
draw(P--Q,linewidth(0.9));
draw((3,-1)--(3,7),blue+linewidth(0.8));
draw((3,4)--(3.4,4)--(3.4,4.4)--(3,4.4));
dot(P);dot(Q);dot(M);
label("$(-2,4)$",P,N);label("$(8,4)$",Q,N);label("$M(3,4)$",M+(0.3,-0.1),SE);
label("$x=3$",(3,6.3),E,blue);
draw((0.5,3.85)--(0.5,4.15));draw((5.5,3.85)--(5.5,4.15));'''
b.add(1756743,1,r'''Which of the following is an equation of the perpendicular bisector of the segment whose endpoints are $(-2,4)$ and $(8,4)$?

\textbf{(A)} $x=3$ \qquad \textbf{(B)} $y=3$ \qquad \textbf{(C)} $x=5$ \qquad \textbf{(D)} $y=5$''',
r'''The midpoint of the segment is $\left(\dfrac{-2+8}{2},\dfrac{4+4}{2}\right)=(3,4)$. Both endpoints have $y=4$, so the segment is horizontal, and the line perpendicular to it is vertical. The vertical line through $(3,4)$ is $x=3$.
'''+asy(fig,'6cm')+r'''
The answer is \textbf{(A)} $x=3$. (Every point $(3,y)$ is at distance $\sqrt{25+(y-4)^2}$ from both endpoints, as a perpendicular bisector must be.)''',
'Perpendicular bisectors|Coordinate geometry|Midpoints',1)

# ---------------- 1756668 jellybeans
b.add(1756668,1,r'''Three friends share a full bag of jellybeans. Mike took $\dfrac13$ of the jellybeans in the full bag, Zac took $\dfrac12$ of the jellybeans in the full bag and Kary took what was left. Mike ate $\dfrac12$ of his jellybeans, Zac ate $\dfrac13$ of his jellybeans and Kary ate all of hers. If Mike and Zac now have a total of $45$ jellybeans together, how many jellybeans did Kary eat?''',
r'''Let the bag hold $N$ jellybeans. Mike has $\dfrac12\cdot\dfrac N3=\dfrac N6$ left and Zac has $\dfrac23\cdot\dfrac N2=\dfrac N3$ left, together $\dfrac N2=45$, so $N=90$. Kary took $N-\dfrac N3-\dfrac N2=\dfrac N6=15$ jellybeans and ate them all: $\boxed{15}$.''',
'Fractions|Linear equations',2)

# ---------------- 1756531 product of divisors
b.add(1756531,1,r'''Let $n$ be a positive integer with $d(n)$ positive divisors. Prove that the product of all positive divisors of $n$ equals $n^{\dfrac{d(n)}{2}}$. Deduce the prime factorisation of this product when $n=p_1^{a_1}p_2^{a_2}\cdots p_k^{a_k}$, and use it to find the product of the divisors of $72$.''',
r'''Let $P$ be the product of the divisors. The map $t\mapsto\dfrac nt$ is a bijection of the set of divisors onto itself, so
\[
P=\prod_{t\mid n}t=\prod_{t\mid n}\dfrac nt ,\qquad\text{hence}\qquad P^2=\prod_{t\mid n}\left(t\cdot\dfrac nt\right)=n^{d(n)} .
\]
Since $P>0$, $P=n^{\dfrac{d(n)}{2}}$. $\blacksquare$ (When $n$ is a perfect square, $d(n)$ is odd and $n^{\dfrac{d(n)}2}$ is the integer $\sqrt n^{\,d(n)}$.)

With $n=p_1^{a_1}\cdots p_k^{a_k}$ we have $d(n)=(a_1+1)\cdots(a_k+1)$, so
\[
P=p_1^{\dfrac{a_1d(n)}{2}}p_2^{\dfrac{a_2d(n)}{2}}\cdots p_k^{\dfrac{a_kd(n)}{2}} ,
\]
and every exponent $\dfrac{a_id(n)}2$ is an integer (if all $a_j$ are even, $d(n)$ is odd but then $a_i$ is even).

For $72=2^3\cdot3^2$: $d(72)=4\cdot3=12$, so the product of its divisors is $72^6=\boxed{2^{18}\cdot3^{12}}$.''',
'Divisor counting|Prime factorisation|Factors and multiples|Pairing and grouping',3,
note='The post asks whether there is a formula; the record asks for a proof of n^(d(n)/2) and an example (72), checked by computation.')

# ---------------- 1756275 slope between two points
fig=r'''import graph;
fill((1,1)--(0,2)--(0,3)--cycle,paleblue);
xaxis(Label("$x$",position=EndPoint,align=E),-0.6,2.4,Arrow(6));
yaxis(Label("$y$",position=EndPoint,align=N),-0.4,3.8,Arrow(6));
pair P=(1,1),A=(0,2),B=(0,3);
draw((1.6,-0.2)--(0,3),dashed);draw((1.8,0.2)--(0,2),dashed);
draw((1.7,-0.05)--(0,2.5),red+linewidth(0.8));
dot(P);dot(A);dot(B);
label("$(1,1)$",P,E);label("$(0,2)$",A,W);label("$(0,3)$",B,W);'''
b.add(1756275,1,r'''A line contains the point $(1,1)$ and passes between the points $(0,2)$ and $(0,3)$, that is, it meets the $y$-axis strictly between them. What are the possible values of its slope?''',
r'''A line through $(1,1)$ with slope $m$ is $y=1+m(x-1)$; it meets the $y$-axis at $y=1-m$. The condition is $2<1-m<3$, that is, $\boxed{-2<m<-1}$. The boundary slopes are those of the lines through $(1,1)$ and $(0,2)$ (slope $-1$) and through $(1,1)$ and $(0,3)$ (slope $-2$).
'''+asy(fig,'6cm')+r'''
In the figure the dashed lines are the two boundary lines (slopes $-1$ and $-2$, not included), and the red line, with slope $-\dfrac32$, is one admissible line.''',
'Slope|Coordinate geometry|Inequalities',2,
note='The answer choices are not in the post, so the record asks for all possible slopes.')

# ---------------- 1755042 MATHCOUNTS handbook warm-up 9
b.add(1755042,114,r'''The pentagonal numbers $1,5,12,22,35,\dots$ count the dots in nested regular pentagon patterns: the $n$th pentagonal number is obtained from the $(n-1)$th by adding $3n-2$ dots. What is the $20$th pentagonal number?''',
r'''The $n$th pentagonal number is
\[
P_n=\sum_{k=1}^{n}(3k-2)=3\cdot\dfrac{n(n+1)}{2}-2n=\dfrac{n(3n-1)}{2}.
\]
Check: $P_1=1$, $P_2=5$, $P_3=12$, $P_4=22$, $P_5=35$. Hence $P_{20}=\dfrac{20\cdot59}{2}=\boxed{590}$.''',
'Arithmetic sequences|Summation|Pattern recognition',2,source=src('MATHCOUNTS Handbook',None,None,114,rnd='Warm-Up 9'),
note='The picture of the first five pentagonal numbers is missing; the standard values 1, 5, 12, 22, 35 and the growth rule are stated in the question.')
b.add(1755042,115,r'''What is the arithmetic mean of all $3$-digit numbers whose digits are distinct and nonzero?''',
r'''There are $9\cdot8\cdot7=504$ such numbers. The map replacing each digit $a$ by $10-a$ is a bijection of this set onto itself (digits stay distinct and nonzero), and it sends $\overline{abc}$ to $1110-\overline{abc}$. So the numbers pair up with sum $1110$ (or are fixed, when equal to $555$, which is not in the set), and the mean is $\dfrac{1110}{2}=\boxed{555}$.''',
'Averages and weighted averages|Symmetry|Digit problems|Pairing and grouping',3,source=src('MATHCOUNTS Handbook',None,None,115,rnd='Warm-Up 9'))
b.add(1755042,118,r'''Alvin plays mini-golf with four friends, and each of the five players gets a positive integer score. The median and the unique mode of their five scores are both $10$, and the range of their scores is $16$. If the mean of all their scores is $15$, what is the sum of all possible values of the lowest score?''',
r'''Order the scores $a\le b\le10\le d\le e$ (median $10$). Then $e=a+16$ and the total is $75$, so $a+b+10+d+a+16=75$, i.e.\ $2a+b+d=49$.

\textbf{If $b<10$}, then $10$ must appear at least twice, so $d=10$; then $2a+b=39$ with $a\le b\le9$, but $2a+b\le27$. Impossible.

\textbf{So $b=10$}, and $d=39-2a$. Now $d\le e=a+16$ gives $a\ge\dfrac{23}{3}$, so $a\ge8$, and $a\le b=10$.
\begin{itemize}
\item $a=8$: scores $8,10,10,23,24$.
\item $a=9$: scores $9,10,10,21,25$.
\item $a=10$: scores $10,10,10,19,26$.
\end{itemize}
In each case $10$ is the unique mode, the median is $10$, the range is $16$ and the mean is $15$. The possible lowest scores are $8,9,10$, with sum $\boxed{27}$.''',
'Median|Mode|Range|Mean|Casework',4,source=src('MATHCOUNTS Handbook',None,None,118,rnd='Warm-Up 9'),
note='Scores are taken to be positive integers (mini-golf scores). Checked by brute force.')
b.add(1755042,119,r'''Cayley has a fair six-sided die whose faces are numbered $-2,-1,0,0,1,2$. She rolls the die three times. What is the probability that the sum of the three numbers she rolls is $0$? Express your answer as a common fraction.''',
r'''There are $6^3=216$ equally likely outcomes (the two $0$ faces are different faces). Group the outcomes with sum $0$ by the multiset of values rolled:
\begin{itemize}
\item $\{0,0,0\}$: each roll is one of the $2$ zero faces: $2^3=8$ outcomes.
\item $\{-2,0,2\}$: $3!=6$ orders, times $2$ choices of zero face: $12$.
\item $\{-1,0,1\}$: likewise $12$.
\item $\{-2,1,1\}$: $3$ orders (position of the $-2$): $3$.
\item $\{2,-1,-1\}$: $3$.
\end{itemize}
In total $8+12+12+3+3=38$, so the probability is $\dfrac{38}{216}=\boxed{\dfrac{19}{108}}$.

The poster's list has $22$ outcomes, giving $\dfrac{22}{216}=\dfrac{11}{108}$. It misses $(0,0,0)$, which accounts for $8$ outcomes because each roll can show either zero face, and outside the case ``first roll $0$'' it counts each triple containing one $0$ (such as $(-2,0,2)$ or $(1,-1,0)$) once instead of twice, which is $8$ more outcomes: $22+8+8=38$.''',
'Dice probability|Probability|Casework|Systematic counting',3,source=src('MATHCOUNTS Handbook',None,None,119,rnd='Warm-Up 9'),
note='The poster got 11/108; the solution explains the missing outcomes. Checked by enumeration.')

# ---------------- 1755147 absolute values
b.add(1755147,1,r'''If $\dfrac{|a+3|}{2}=1$ and $2|b+1|=6$, then $|a+b|$ could equal any of the following EXCEPT

\textbf{(A)} $1$ \qquad \textbf{(B)} $3$ \qquad \textbf{(C)} $5$ \qquad \textbf{(D)} $7$''',
r'''From $|a+3|=2$, $a=-1$ or $a=-5$. From $|b+1|=3$, $b=2$ or $b=-4$. The four sums $a+b$ are $1,-5,-3,-9$, so $|a+b|\in\{1,5,3,9\}$. The value $7$ is impossible: the answer is \textbf{(D)}.''',
'Absolute value|Casework',2)

# ---------------- 1755144 greenhouse
b.add(1755144,1,r'''In a greenhouse the Fahrenheit temperature $F$ is controlled so that it does not differ from $79$ degrees by more than $7$ degrees. Which of the following best expresses the possible range of the temperature?

\textbf{(A)} $|F-79|\le7$ \qquad \textbf{(B)} $|F-79|>7$ \qquad \textbf{(C)} $|F-7|\le79$ \qquad \textbf{(D)} $|F-7|>79$''',
r'''The difference between $F$ and $79$ is $|F-79|$, and ``not more than $7$'' means $\le7$. So the answer is \textbf{(A)} $|F-79|\le7$, i.e.\ $72\le F\le86$.''',
'Absolute value|Inequalities',1)

# ---------------- 1754998 sum of n uniforms
b.add(1754998,1,r'''Let $n\ge1$ be an integer. Numbers $x_1,x_2,\dots,x_n$ are chosen independently and uniformly at random from the interval $[0,1]$. Prove that the probability that $x_1+x_2+\cdots+x_n<1$ is $\dfrac{1}{n!}$.''',
r'''The point $(x_1,\dots,x_n)$ is uniform in the unit cube $[0,1]^n$, of volume $1$, so the probability is the volume of
\[
T=\{x_i\ge0,\ x_1+\cdots+x_n<1\}.
\]
Consider the partial sums $s_k=x_1+\cdots+x_k$. The map $(x_1,\dots,x_n)\mapsto(s_1,\dots,s_n)$ is linear with a triangular matrix having $1$s on the diagonal, so it preserves volume, and it maps $T$ bijectively onto
\[
T'=\{0\le s_1\le s_2\le\cdots\le s_n<1\}
\]
(the inverse is $x_1=s_1$, $x_k=s_k-s_{k-1}$).

Now the cube $[0,1)^n$ is the union of the $n!$ regions $\{s_{\sigma(1)}\le s_{\sigma(2)}\le\cdots\le s_{\sigma(n)}\}$, one for each permutation $\sigma$ of the coordinates; two of them overlap only where two coordinates are equal, a set of volume $0$. Permuting coordinates preserves volume, so all $n!$ regions have the same volume, which is therefore $\dfrac1{n!}$. One of them is $T'$, so
\[
P(x_1+\cdots+x_n<1)=\operatorname{vol}(T)=\operatorname{vol}(T')=\boxed{\dfrac1{n!}} .\qquad\blacksquare
\]
(For $n=2$ this is the triangle below the line $x_1+x_2=1$, of area $\dfrac12$; for $n=3$ the corner tetrahedron, of volume $\dfrac16$. The other suggestion, $\dfrac1{n(n-1)}$, agrees with $\dfrac1{n!}$ only for $n=2,3$; for $n=4$ it gives $\dfrac1{12}\ne\dfrac1{24}$.)''',
'Geometric probability|Probability|Symmetry|Bijections',6,
note='The post asks which of 1/(n(n-1)) and 1/n! is right, for n > 3; the record proves 1/n! for all n. Checked by Monte Carlo for n = 2..6.')

# ---------------- 1754943 exponent identity
b.add(1754943,1,r'''Show that $4^{2^{n}}+2^{2^{n}}=16^{2^{n-1}}+4^{2^{n-1}}$ for every positive integer $n$.''',
r'''Use $2^n=2\cdot2^{n-1}$ and $(a^b)^c=a^{bc}$:
\[
16^{2^{n-1}}=\left(4^2\right)^{2^{n-1}}=4^{2\cdot2^{n-1}}=4^{2^n},\qquad 4^{2^{n-1}}=\left(2^2\right)^{2^{n-1}}=2^{2\cdot2^{n-1}}=2^{2^n}.
\]
Adding the two equalities gives the identity. $\blacksquare$''',
'Exponents',1)

# ---------------- 1754904 house numbers
b.add(1754904,23,r'''A street has $20$ houses on each side, for a total of $40$ houses. The addresses on the south side of the street form an arithmetic sequence, as do the addresses on the north side. On the south side the addresses are $4,10,16,\dots$, and on the north side they are $3,9,15,\dots$. A sign painter paints house numbers on a house for $\$1$ per digit. If he paints the appropriate house number once on each of these $40$ houses, how much does he earn?''',
r'''\textbf{South side:} $4,10,\dots,4+6\cdot19=118$. One-digit: $4$ ($1$ number). Two-digit: $10,16,\dots,94$, that is $\dfrac{94-10}{6}+1=15$ numbers. Three-digit: $100,106,112,118$ ($4$ numbers). Digits: $1+30+12=43$.

\textbf{North side:} $3,9,\dots,3+6\cdot19=117$. One-digit: $3,9$ ($2$). Two-digit: $15,21,\dots,99$, that is $\dfrac{99-15}{6}+1=15$. Three-digit: $105,111,117$ ($3$). Digits: $2+30+9=41$.

He paints $43+41=84$ digits and earns $\boxed{\$84}$.''',
'Arithmetic sequences|Digit problems|Systematic counting',2,source=src('MATHCOUNTS',2005,'School',23,rnd='Sprint'))

# ---------------- 1753724 2005^2007^2009 mod 7
b.add(1753724,1,r'''Find the remainder when $2005^{2007^{2009}}$ is divided by $7$.''',
r'''The tower is read as $2005^{\left(2007^{2009}\right)}$. Since $2005=7\cdot286+3$, we need $3^{2007^{2009}}\bmod7$. The powers of $3$ modulo $7$ are $3,2,6,4,5,1$, repeating with period $6$ (as Fermat's little theorem predicts, $3^6\equiv1$). So we need the exponent modulo $6$.

$2007\equiv3\pmod6$, and $3^k\equiv3\pmod6$ for every $k\ge1$ (it is odd and divisible by $3$). Hence $2007^{2009}\equiv3\pmod6$ and
\[
2005^{2007^{2009}}\equiv3^3=27\equiv\boxed{6}\pmod7 .
\]''',
"Modular exponentiation|Remainders and congruences|Fermat's little theorem",3,
note='The tower 2005^2007^2009 is read top-down, as usual. Checked with modular exponentiation.')

# ---------------- 1753558 cannon ball in cube
fig=r'''real s=4;
draw(box((0,0),(s,s)),linewidth(0.9));
draw(circle((s/2,s/2),s/2),blue+linewidth(0.8));
pair O=(s/2,s/2);dot(O);
draw(O--(s,s/2),dashed);
label("$r$",(3*s/4,s/2),N);
draw((0,-0.35)--(s,-0.35),Arrows(5));label("$s=2r$",(s/2,-0.35),S);
label("$O$",O,W);'''
b.add(1753558,1,r'''A spherical cannon ball with a volume of $18$ decilitres is dropped into a cubic box completely filled with water. The ball touches all six faces of the box. How much water, in millilitres, is left in the box when the cannon ball is removed?''',
r'''Since the ball touches all six faces, it is inscribed in the cube: if the ball has radius $r$, the cube has edge $s=2r$. The figure shows the cross-section through the centre $O$ parallel to a face.
'''+asy(fig,'4cm')+r'''
The ball's volume is $\dfrac43\pi r^3=\dfrac{\pi}{6}s^3=18\text{ dL}=1800$ mL, so the cube holds $s^3=\dfrac{6\cdot1800}{\pi}=\dfrac{10800}{\pi}$ mL. When the ball goes in, $1800$ mL of water overflows; when it is taken out, the water left is
\[
\dfrac{10800}{\pi}-1800\approx\boxed{1638\text{ mL}}
\]
(exactly $1800\left(\dfrac6\pi-1\right)\approx1637.7$ mL).''',
'Spheres|Cubes and rectangular prisms|Volume|Unit conversion|Solid geometry',3,
note='The water that overflows when the ball is dropped in is assumed lost, so the box keeps the cube volume minus the ball volume.')

# ---------------- 1753565 divisibility proofs
b.add(1753565,1,r'''Prove that $3\mid a\left(2a^2+7\right)$ for every integer $a$.''',
r'''Modulo $3$, $7\equiv1$ and $2\equiv-1$, so $a(2a^2+7)\equiv a(1-a^2)=-(a-1)a(a+1)\pmod3$. The product of three consecutive integers $a-1,a,a+1$ is divisible by $3$. Hence $3\mid a(2a^2+7)$. $\blacksquare$''',
'Divisibility|Remainders and congruences',2)
b.add(1753565,2,r'''Prove that if $a$ is odd, then $32\mid\left(a^2+3\right)\left(a^2+7\right)$.''',
r'''For odd $a=2k+1$, $a^2=4k(k+1)+1\equiv1\pmod8$, because $k(k+1)$ is even. Hence $a^2+3\equiv4\pmod8$, so $4\mid a^2+3$, and $a^2+7\equiv0\pmod8$. Therefore $4\cdot8=32$ divides the product. $\blacksquare$''',
'Divisibility|Remainders and congruences|Perfect squares|Parity',3)
b.add(1753565,3,r'''Prove that if $a$ and $b$ are both odd integers, then $16\mid a^4+b^4-2$.''',
r'''For odd $a$, $a^4-1=(a-1)(a+1)(a^2+1)$. Here $a-1$ and $a+1$ are consecutive even numbers, so one of them is divisible by $4$ and their product by $8$; and $a^2+1$ is even. Hence $16\mid a^4-1$, i.e.\ $a^4\equiv1\pmod{16}$. Likewise $b^4\equiv1\pmod{16}$, so $a^4+b^4-2\equiv0\pmod{16}$. $\blacksquare$''',
'Divisibility|Remainders and congruences|Factoring|Parity',3)

# ---------------- 1754485 comboity
b.add(1754485,1,r'''The \emph{comboity} of a word is the number of letters it shares with the word COMBO, counted with multiplicity but never more often than they occur in COMBO: it is the sum, over the letters C, O, M, B, of the smaller of the number of times the letter occurs in the word and the number of times it occurs in COMBO (once for C, M, B and twice for O). For example, BOW has comboity $2$, BOOK has comboity $3$ and BOOOK also has comboity $3$. A $4$-letter word is any string of $4$ letters from the $26$-letter alphabet, repetitions allowed. What is the expected comboity of a $4$-letter word chosen uniformly at random?''',
r'''Let $X_L$ be the number of times the letter $L$ occurs in the word. The comboity is
\[
\min(X_C,1)+\min(X_M,1)+\min(X_B,1)+\min(X_O,2),
\]
and by linearity of expectation we can take the expected value of each term separately. Each position is a given letter with probability $\dfrac1{26}$, independently.
\begin{itemize}
\item For $L=C,M,B$: $E[\min(X_L,1)]=P(X_L\ge1)=1-\left(\dfrac{25}{26}\right)^4$.
\item For $O$: $E[\min(X_O,2)]=P(X_O\ge1)+P(X_O\ge2)$, where $P(X_O\ge2)=1-\left(\dfrac{25}{26}\right)^4-4\cdot\dfrac1{26}\left(\dfrac{25}{26}\right)^3$.
\end{itemize}
Adding,
\[
E=5-\dfrac{5\cdot25^4+4\cdot25^3}{26^4}=5-\dfrac{25^3\cdot129}{26^4}=\dfrac{2284880-2015625}{456976}=\boxed{\dfrac{269255}{456976}}\approx0.589 .
\]''',
'Expected value|Probability|Complementary probability|Binomial probability',4,
note='The post defines comboity only by two examples; the record states the definition (multiplicity capped by the counts in COMBO) explicitly, and "any permutation of x letters counts as an x-letter word" is read as all 26^4 strings. Answer checked by enumerating all 26^4 words.')

# ---------------- 1754002 insphere volume formula
fig=r'''triple[] T={(0,0,0),(6,0,0),(3,3*sqrt(3),0),(3,sqrt(3),2*sqrt(6))};
pair P(triple t){return (t.x+0.45*t.y,t.z+t.y);}
pair A=P(T[0]),B=P(T[1]),C=P(T[2]),D=P(T[3]);
pair G=P((3,sqrt(3),0)),O=P((3,sqrt(3),sqrt(6)/2));
draw(A--B--C--D--cycle,linewidth(0.9));draw(B--D,linewidth(0.9));
draw(A--C,dashed);
draw(O--A,blue+dashed);draw(O--B,blue+dashed);draw(O--C,blue+dashed);
draw(O--G,red+linewidth(0.9));
dot(O);dot(G);
label("$O$",O,E);label("$r$",(O+G)/2,W,red);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,E);label("$D$",D,N);'''
b.add(1754002,1,r'''A polyhedron has an inscribed sphere of radius $r$, that is, a sphere tangent to every face. Let $V$ be the volume of the polyhedron and $S$ its total surface area.
\begin{enumerate}
\item[(a)] Prove that $V=\dfrac13rS$ (the analogue of the plane formula area $=$ inradius $\times$ semiperimeter).
\item[(b)] Use (a) to find the radius of the sphere inscribed in a regular tetrahedron of edge $6$.
\end{enumerate}''',
r'''\textbf{(a)} Let $O$ be the centre of the inscribed sphere. Join $O$ to every vertex; this cuts the polyhedron into pyramids, one for each face, with apex $O$ and that face as base. Since the sphere is tangent to the face, the perpendicular from $O$ to the plane of the face has length $r$, so every pyramid has height $r$. In the figure (a tetrahedron) the pyramid $OABC$ is drawn, with its height $r$ in red.
'''+asy(fig,'5.5cm')+r'''
If the faces have areas $S_1,\dots,S_k$, then
\[
V=\sum_{i=1}^{k}\dfrac13S_ir=\dfrac13r\left(S_1+\cdots+S_k\right)=\dfrac13rS .\qquad\blacksquare
\]

\textbf{(b)} A regular tetrahedron of edge $a=6$ has four equilateral faces, so $S=4\cdot\dfrac{\sqrt3}{4}a^2=36\sqrt3$. Its height is $a\sqrt{\dfrac23}=2\sqrt6$ (the centroid of a face is at distance $\dfrac{a}{\sqrt3}=2\sqrt3$ from each vertex, and $36-12=24$), so $V=\dfrac13\cdot9\sqrt3\cdot2\sqrt6=18\sqrt2$. Then
\[
r=\dfrac{3V}{S}=\dfrac{54\sqrt2}{36\sqrt3}=\boxed{\dfrac{\sqrt6}{2}} .
\]''',
'Polyhedra|Pyramids|Volume|Surface area|Solid geometry|Area decomposition',4,
note='The post asks whether a 3D analogue of area = inradius x semiperimeter exists; the record proves V = rS/3 and adds an application (regular tetrahedron of edge 6), checked numerically.')

# ---------------- 1754302 perfect square factors of 36
b.add(1754302,1,r'''How many perfect squares are factors of $36$? A student lists $0,1,4,9,36$ and answers $5$. Is the student right?''',
r'''$0$ is a perfect square ($0=0^2$), but it is not a factor of $36$: a factor $t$ of $36$ must satisfy $36=t\cdot k$ for some integer $k$, and $0\cdot k=0\ne36$. The positive square factors of $36=2^2\cdot3^2$ are $2^{2i}3^{2j}$ with $i,j\in\{0,1\}$, namely $1,4,9,36$. So the answer is $\boxed{4}$, and the student is wrong only in counting $0$.''',
'Perfect squares|Factors and multiples|Prime factorisation',1,
note='The post asks whether 0 counts; the record asks the count for 36 (the post says "it wasn\'t 36 but you get the point").')

# ---------------- 1754336 rhombus incircle
fig=r'''pair A=(-2,0),B=(0,-1),C=(2,0),D=(0,1),O=(0,0);
real r=2/sqrt(5);
pair T=O+r*dir(degrees(D-C)+90+180);
pair u=unit(D-C); pair T2=C+dot(O-C,u)*u;
fill(A--B--C--D--cycle,paleblue);
filldraw(circle(O,r),white,blue+linewidth(0.8));
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--C,dashed);draw(B--D,dashed);
draw(O--T2,red+linewidth(0.8));
pair v=unit(O-T2);
draw(T2+0.12*u--T2+0.12*u+0.12*v--T2+0.12*v);
dot(O);
label("$A$",A,W);label("$B$",B,S);label("$C$",C,E);label("$D$",D,N);label("$O$",O,SW);
label("$r$",(O+T2)/2,dir(-27),red);
label("$2$",(-1,0),S);label("$1$",(0,-0.5),E);'''
b.add(1754336,5,r'''A circle is inscribed in a rhombus whose diagonals are $2$ feet and $4$ feet long. What is the area, in square feet, of the region of the rhombus that is outside the circular region? Express your answer as a decimal to the nearest tenth.

A student argues: the rhombus has area $4$, which equals the total area of $4$ congruent right triangles with height $r$ and base $2\sqrt5$, so $4=4\cdot\dfrac12\cdot r\cdot2\sqrt5$, $r^2=\dfrac15$, and the answer is $4-\dfrac\pi5\approx3.4$. Find the error.''',
r'''The diagonals of a rhombus bisect each other at right angles, so with centre $O$ the half-diagonals are $1$ and $2$, and each side is $\sqrt{1^2+2^2}=\sqrt5$. The area is $\dfrac{2\cdot4}{2}=4$. The inscribed circle has centre $O$ and touches each side, so its radius $r$ is the height from $O$ in each of the four right triangles $OAB,OBC,OCD,ODA$ with hypotenuse $\sqrt5$.
'''+asy(fig,'6cm')+r'''
Hence
\[
4=4\cdot\dfrac12\cdot\sqrt5\cdot r\quad\Longrightarrow\quad r=\dfrac{2}{\sqrt5},\qquad r^2=\dfrac45 .
\]
The area outside the circle is
\[
4-\dfrac{4\pi}{5}\approx4-2.513=1.487\approx\boxed{1.5}\text{ square feet}.
\]
The student's error is the base of the triangles: each right triangle $OAB$ has hypotenuse $AB=\sqrt5$, not $2\sqrt5$ (the half-diagonals are $1$ and $2$, not $2$ and $4$).''',
'Rhombi|Circles|Incircles and incentres|Lengths, perimeter, and area|Pythagorean theorem|Tangents',3,source=src('MATHCOUNTS',2010,'National',5,rnd='Target'),
note='The post gives the official answer 1.5 and asks why 3.4 is wrong; the record adds the error-finding part.')

b.save()
