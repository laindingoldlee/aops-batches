from qb import *
b=Bank('p235_03')

# ---------------- 1707222 MATHCOUNTS problems 1-4
b.add(1707222,1,r'''What is the arithmetic mean of all $3$-digit numbers whose digits are distinct and nonzero?''',
r'''The set of such numbers is unchanged when every digit $d$ is replaced by $10-d$ (this keeps digits distinct and nonzero), and the map sends $\overline{abc}$ to $999+111-\overline{abc}=1110-\overline{abc}$. So the numbers pair up with sum $1110$ (a number paired with itself would need every digit equal to $5$, impossible with distinct digits), and the mean is $\boxed{555}$.''',
'Symmetry|Pairing and grouping|Averages and weighted averages',3,
note='The poster asks for a non-brute-force method. Repeat of an earlier record (aliased).')

figpq=r'''pair P=(-12.5,0),Q=(-3.5,12),R=(12.5,0),S=(3.5,-12),M=(0,0);
draw(P--Q--R--S--cycle,linewidth(0.9));
draw(P--R,blue+dashed);draw(Q--S,blue+dashed);
draw((-3.5,-12)--(-3.5,12),gray+dotted);draw((-3.5,-12)--S,gray+dotted);
dot(M);
label("$P$",P,W);label("$Q$",Q,N);label("$R$",R,E);label("$S$",S,S);label("$M$",M,NE);
label("$15$",(P+Q)/2,NW);label("$20$",(Q+R)/2,NE);label("$24$",(-3.5,-4),W,gray);label("$7$",(0,-12),S,gray);'''
b.add(1707222,2,r'''Rectangle $PQRS$ is drawn on a coordinate plane. The $y$-coordinate of $Q$ is $24$ units greater than the $y$-coordinate of $S$, the $x$-coordinate of $R$ is $25$ units greater than the $x$-coordinate of $P$, and the $y$-coordinate of $P$ is equal to the $y$-coordinate of $R$. What is the perimeter of rectangle $PQRS$?''',
r'''In rectangle $PQRS$ the diagonals are $PR$ and $QS$. Since $P$ and $R$ have the same $y$-coordinate, $PR$ is horizontal, and its length is $25$. The diagonals of a rectangle are equal and bisect each other at the centre $M$, so $QS=25$ too. The vertical component of $QS$ is $24$, so its horizontal component is $\sqrt{25^2-24^2}=7$.
'''+asy(figpq,'6.5cm')+r'''
Put $M$ at the origin. Then $P=(-12.5,0)$, $R=(12.5,0)$, and $Q=(\pm3.5,12)$, $S=(\mp3.5,-12)$. With $Q=(-3.5,12)$:
\[
PQ=\sqrt{9^2+12^2}=15,\qquad QR=\sqrt{16^2+12^2}=20,
\]
and $\overrightarrow{PQ}\cdot\overrightarrow{QR}=9\cdot16-12\cdot12=0$ confirms the right angle. (The other choice $Q=(3.5,12)$ just swaps the side lengths $15$ and $20$.) The perimeter is $2(15+20)=\boxed{70}$.''',
'Rectangles|Coordinate geometry|Distance formula|Pythagorean theorem',4,
note='Repeat of an earlier record (aliased).')

b.add(1707222,3,r'''Seven points are equally spaced around a unit circle. How many non-congruent convex pentagons can be drawn using five of the points as vertices?''',
r'''Any five of the points form a convex pentagon (they lie on a circle), and the pentagon is determined by the two points left out. Label the points $0,1,\dots,6$ around the circle. Measure the sides of a pentagon by the number of steps between consecutive vertices; a side of $k$ steps is a chord of length $2\sin\dfrac{k\pi}{7}$, and congruent pentagons have the same cyclic sequence of sides up to rotation and reflection.

Rotating, we may leave out $0$ and $k$ with $k\in\{1,2,3\}$ (leaving out $0$ and $7-k$ is the mirror image).
\begin{itemize}
\item $k=1$ (omit $0,1$): sides $1,1,1,1,3$.
\item $k=2$ (omit $0,2$): vertices $1,3,4,5,6$, sides $2,1,1,1,2$: the two long sides are adjacent (meeting at vertex $1$).
\item $k=3$ (omit $0,3$): vertices $1,2,4,5,6$, sides $1,2,1,1,2$: the two long sides are not adjacent.
\end{itemize}
The first pentagon has a side of $3$ steps and the others do not; the last two have the same side lengths, but in a different cyclic order, so they are not congruent. Hence there are $\boxed{3}$ non-congruent pentagons.''',
'Symmetry|Combinations|Casework',3)

b.add(1707222,4,r'''The coefficients $c$ and $d$ of $x^3-19x^2+cx+d=0$ are chosen so that the roots of the equation are positive integers that form a geometric sequence. What is the value of $c+d$?''',
r'''Let the roots be $u,v,w$ in geometric progression, so $v^2=uw$. The ratio $\dfrac vu$ is rational; write it as $\dfrac pq$ in lowest terms. Then $q^2\mid u$, so the roots are $tq^2,\ tpq,\ tp^2$ for a positive integer $t$, and by Vieta $t(p^2+pq+q^2)=19$. As $19$ is prime and $p^2+pq+q^2\ge3$, $t=1$ and $p^2+pq+q^2=19$, giving $\{p,q\}=\{2,3\}$. So the roots are $4,6,9$ (ratio $\dfrac32$, which explains why no integer ratio works). Then
\[
c=4\cdot6+6\cdot9+4\cdot9=114,\qquad d=-4\cdot6\cdot9=-216,
\]
and $c+d=\boxed{-102}$.''',
'Polynomial roots|Vieta\'s formulas|Geometric sequences',4,
note='The poster tried integer ratios only; the ratio is 3/2. Repeat of an earlier record (aliased).')

# ---------------- 1707437 sum over 3-smooth numbers
b.add(1707437,1,r'''Evaluate
\[
\dfrac11+\dfrac12+\dfrac13+\dfrac14+\dfrac16+\dfrac18+\dfrac19+\dfrac1{12}+\cdots,
\]
where the denominators are all the positive integers of the form $2^a3^b$ with $a,b\ge0$ (each taken once).''',
r'''Multiply the two geometric series
\[
\left(1+\dfrac12+\dfrac14+\cdots\right)\left(1+\dfrac13+\dfrac19+\cdots\right)=\sum_{a,b\ge0}\dfrac1{2^a3^b}.
\]
By unique prime factorisation each number $2^a3^b$ arises from exactly one pair $(a,b)$, so the right side is exactly the given sum (all terms are positive, so the order of summation does not matter). Hence the sum is
\[
\dfrac{1}{1-\dfrac12}\cdot\dfrac{1}{1-\dfrac13}=2\cdot\dfrac32=\boxed{3}.
\]''',
'Geometric sequences|Prime factorisation|Sequences and series',3)

# ---------------- 1311798 harmonic series (alias)
b.add(1311798,1,r'''Show that the infinite sum $1+\dfrac12+\dfrac13+\dfrac14+\dfrac15+\cdots$ has no finite value.''',
r'''Group the terms in blocks ending at powers of $2$:
\[
1+\dfrac12+\left(\dfrac13+\dfrac14\right)+\left(\dfrac15+\cdots+\dfrac18\right)+\cdots+\left(\dfrac1{2^{k-1}+1}+\cdots+\dfrac1{2^k}\right).
\]
Each bracket has $2^{k-1}$ terms, each at least $\dfrac1{2^k}$, so each bracket is at least $\dfrac12$. Hence the partial sum up to $\dfrac1{2^k}$ is at least $1+\dfrac k2$, which exceeds any bound as $k$ grows. The partial sums increase without bound, so the series \textbf{diverges}: it has no finite sum.''',
'Sequences and series|Summation|Bounding and extremal cases',3,
note='"Compute the infinite sum" of the harmonic series; the answer is that it diverges. Repeat of an earlier record (aliased).')

# ---------------- 1706861 4-digit number
b.add(1706861,1,r'''I am a $4$-digit number strictly between $5000$ and $6000$. My ones digit is half of my tens digit, and my hundreds digit is $3$ times my tens digit. Which number am I?''',
r'''The thousands digit is $5$ (the number $5000$ itself is excluded). Let the tens digit be $t$. The ones digit $\dfrac t2$ must be a whole number, so $t$ is even, and the hundreds digit $3t$ must be at most $9$, so $t\le3$. Hence $t=0$ or $t=2$. The choice $t=0$ gives $5000$, which is not strictly between $5000$ and $6000$. So $t=2$, the hundreds digit is $6$ and the ones digit is $1$: the number is $\boxed{5621}$.''',
'Place value|Digit problems',1,
note='"Between 5000 and 6000" read as strictly between, which rules out 5000 (digits 0, 0, 0 also fit the conditions).')

# ---------------- 1692181 blue cards
b.add(1692181,1,r'''A bag contains two cards. The first card is blue on one side and white on the other. The second card is blue on both sides. You reach into the bag and slide out a random card, with a random side facing up, and see that the face showing is blue. What is the probability that you have pulled out the blue/blue card?''',
r'''There are four equally likely (card, face up) outcomes. Exactly three of them show a blue face: the blue side of the first card, and either side of the second card. Two of these three belong to the blue/blue card. Given that a blue face shows, the probability is
\[
\dfrac{\dfrac12}{\dfrac34}=\boxed{\dfrac23}.
\]
(The tempting answer $\dfrac12$ wrongly treats ``the card is blue/blue'' and ``the card is blue/white'' as equally likely after seeing blue; but the blue/blue card is twice as likely to show blue.)''',
'Conditional probability|Probability',3,
note='From the course The Power of Mathematical Visualization. The random choice of the face shown is stated explicitly.')

# ---------------- 1706924 guessing words
b.add(1706924,1,r'''A word bank contains three words, and each of the three words is the answer to exactly one of three questions. Without studying, you guess, using each word exactly once (all assignments equally likely). What is the probability that you get all three questions right?''',
r'''There are $3!=6$ ways to assign the three words to the three questions, all equally likely, and exactly one of them is correct. The probability is $\boxed{\dfrac16}$.''',
'Probability|Permutations',1)

# ---------------- 1706395 Ioana
b.add(1706395,1,r'''Ioana picks two different numbers $a$ and $b$ from the set $\{1,2,3,\dots,26\}$. The product $ab$ is equal to the sum of the remaining $24$ numbers. What is the value of $|a-b|$?''',
r'''The sum of $1,\dots,26$ is $\dfrac{26\cdot27}{2}=351$, so $ab=351-a-b$, that is,
\[
ab+a+b+1=352\quad\Longrightarrow\quad (a+1)(b+1)=352=2^5\cdot11 .
\]
Both factors are between $2$ and $27$. The factor divisible by $11$ is $11$ or $22$ (not $33$ or more); $11$ would need the cofactor $32>27$, so the factors are $22$ and $16$. Hence $\{a,b\}=\{21,15\}$ and $|a-b|=\boxed{6}$. Check: $15\cdot21=315=351-36$.''',
'Factoring|Diophantine equations|Summation',3)

# ---------------- 1705401 digits 1 to 70
b.add(1705401,1,r'''A data set consists of the $131$ digits used to write all the natural numbers from $1$ to $70$ inclusive. What is the arithmetic mean of the data set? Express your answer as a decimal to the nearest tenth.''',
r'''Count the digit sum. From $1$ to $9$: $45$. From $10$ to $69$: the tens digits $1,\dots,6$ each appear $10$ times, giving $10\cdot21=210$, and the units digits run through $0,\dots,9$ six times, giving $6\cdot45=270$. The number $70$ adds $7$. The total is $45+210+270+7=532$ (and the number of digits is $9+2\cdot61=131$). The mean is
\[
\dfrac{532}{131}\approx4.061,
\]
which is $\boxed{4.1}$ to the nearest tenth.''',
'Mean|Digits and bases|Systematic counting',3)

# ---------------- 1706122 ski slope grade
figg=r'''pair A=(0,4),B=(4,0),Cc=(0,0);
draw(A--B,linewidth(1.1));draw(A--Cc--B,gray+dashed);draw(A--(0,4.3),gray+dashed);
draw((0.35,0)--(0.35,0.35)--(0,0.35));
draw(arc(A,0.9,-90,-45),blue);
label("$45^\circ$",A+1.5*dir(-67.5),blue);
label("$d$",(0,2),W);label("$d$",(2,0),S);
label("vertical",(0,4.3),N);label("slope",(2.4,2.2),NE);'''
b.add(1706122,1,r'''The grade of a ski slope is the ratio of the vertical drop to the horizontal distance. What is the measure of the angle between the ski slope and the vertical, for a ski slope whose grade is $100\%$?''',
r'''A grade of $100\%$ means the vertical drop equals the horizontal distance, say both equal $d$. The slope is then the hypotenuse of a right isosceles triangle with legs $d$ (vertical) and $d$ (horizontal).
'''+asy(figg,'4.5cm')+r'''
The two acute angles of a right isosceles triangle are equal, so each is $45^\circ$. The angle between the slope and the vertical leg is therefore $\boxed{45^\circ}$ (and so is the angle with the horizontal).''',
'Right triangles|Isosceles triangles|Percentages|Ratios, proportions, and variation',2,
note='Asked on a state-round test according to the poster (contest not named).')

# ---------------- 1705963 quadratic form maximum
b.add(1705963,1,r'''Let $a,b,c$ be positive integers such that
\[
25a^2+29b^2+37c^2+12ab+48ac+10bc=28812 .
\]
Find the maximum value of $a+b+c$.''',
r'''The left side is a sum of three squares:
\[
25a^2+29b^2+37c^2+12ab+48ac+10bc=(3a+2b)^2+(5b+c)^2+(4a+6c)^2 ,
\]
as expanding the right side shows ($9a^2+12ab+4b^2$, $25b^2+10bc+c^2$, $16a^2+48ac+36c^2$). Put $X=3a+2b$, $Y=5b+c$, $Z=4a+6c$; then $X+Y+Z=7a+7b+7c$, so
\[
a+b+c=\dfrac{X+Y+Z}{7}.
\]
By the Cauchy-Schwarz (or QM-AM) inequality,
\[
(X+Y+Z)^2\le3(X^2+Y^2+Z^2)=3\cdot28812=86436=294^2,
\]
so $X+Y+Z\le294$ and $a+b+c\le42$. Equality needs $X=Y=Z=98$:
\[
3a+2b=98,\qquad 5b+c=98,\qquad 4a+6c=98 .
\]
This system has the solution $a=20$, $b=19$, $c=3$ (check: $60+38=95+3=80+18=98$), which consists of positive integers. Hence the maximum of $a+b+c$ is $\boxed{42}$.''',
'Cauchy-Schwarz inequality|Algebraic expressions and identities|Maxima and minima',6,
note='Brute force over all positive integer solutions confirms that (20, 19, 3) is the only one, so the maximum is 42.')

# ---------------- 1705567 sum 2n/4^n
b.add(1705567,1,r'''Evaluate the infinite sum
\[
\dfrac24+\dfrac4{16}+\dfrac6{64}+\dfrac8{256}+\cdots+\dfrac{2n}{4^n}+\cdots .
\]''',
r'''Let $T=\displaystyle\sum_{n\ge1}\dfrac{n}{4^n}$; the required sum is $2T$. (The series converges, e.g.\ because $\dfrac{n}{4^n}\le\dfrac1{2^n}$.) Then
\[
T-\dfrac T4=\sum_{n\ge1}\dfrac{n}{4^n}-\sum_{n\ge1}\dfrac{n-1}{4^n}=\sum_{n\ge1}\dfrac1{4^n}=\dfrac{\dfrac14}{1-\dfrac14}=\dfrac13 ,
\]
so $\dfrac34T=\dfrac13$ and $T=\dfrac49$. The sum is $2T=\boxed{\dfrac89}$.''',
'Sequences and series|Geometric sequences|Summation',3)

# ---------------- 1705590 equal numbers of coins
b.add(1705590,1,r'''A collection of coins has equally many quarters, dimes and nickels, and no other coins. Its total value is $x$ cents.
\begin{enumerate}
\item[(a)] How many coins are there, in terms of $x$?
\item[(b)] For which values of $x$ is this possible?
\item[(c)] How many coins are there if the total value is $\$6.00$?
\end{enumerate}''',
r'''Group the coins into sets of one quarter, one dime and one nickel. Each set is worth $25+10+5=40$ cents and contains $3$ coins.

\textbf{(a)} There are $\dfrac x{40}$ sets, so $\boxed{\dfrac{3x}{40}}$ coins.

\textbf{(b)} The number of sets must be a positive integer, so $x$ must be a positive multiple of $40$.

\textbf{(c)} $x=600$ gives $15$ sets: $15$ of each coin, $\boxed{45}$ coins.''',
'Money and currency|Linear equations',1,
note='The post asks how to solve "equal numbers of quarters, nickels and dimes add up to x" problems in general; the record asks for the general answer and a sample total ($6.00) chosen for the record.')

# ---------------- 1705202 locus
figl=r'''import graph;
real f(real x){return 1/x;}
draw((-3.2,0)--(3.4,0),Arrow);draw((0,-3.2)--(0,3.4),Arrow);
draw(graph(f,0.36,3),blue+linewidth(0.9));draw(graph(f,-3,-0.36),blue+linewidth(0.9));
real g(real x){return -1/x;}
draw(graph(g,0.36,3),red+linewidth(0.9));draw(graph(g,-3,-0.36),red+linewidth(0.9));
label("$x$",(3.4,0),E);label("$y$",(0,3.4),N);
label("$xy=k$",(1.9,1.9),blue);label("$xy=-k$",(1.9,-1.9),red);
label("$xy=k$",(-1.9,-1.9),blue);label("$xy=-k$",(-1.9,1.9),red);'''
b.add(1705202,1,r'''A point moves in the coordinate plane so that the product of the squares of its distances from the two coordinate axes is a positive constant $c$. What is its locus?''',
r'''The distance from $(x,y)$ to the $x$-axis is $|y|$ and to the $y$-axis is $|x|$. The condition is
\[
x^2y^2=c\quad\Longleftrightarrow\quad |xy|=\sqrt c\quad\Longleftrightarrow\quad xy=k\ \text{ or }\ xy=-k,\qquad k=\sqrt c>0 .
\]
So the locus is the union of the two rectangular hyperbolas $xy=\sqrt c$ (branches in the first and third quadrants) and $xy=-\sqrt c$ (branches in the second and fourth quadrants), both having the coordinate axes as asymptotes.
'''+asy(figl,'5cm')+r'''
The answer: $\boxed{\text{the pair of hyperbolas }xy=\pm\sqrt c}$ (four branches, one in each quadrant). The points on the axes are excluded automatically, since there $xy=0$.''',
'Loci and geometric constraints|Hyperbolas|Coordinate geometry',2,
note='The figure is drawn for k = 1.')

# ---------------- 1704547 cubic inequality (alias)
b.add(1704547,1,r'''Solve the inequality $(2x-1)(x+1)(x+7)>0$.''',
r'''The factors vanish at $x=-7$, $x=-1$ and $x=\dfrac12$, which split the real line into four intervals. On each interval every factor keeps its sign, so a sign chart gives:
\[
\begin{array}{c|cccc}
 & x<-7 & -7<x<-1 & -1<x<\dfrac12 & x>\dfrac12\\ \hline
2x-1 & - & - & - & +\\
x+1 & - & - & + & +\\
x+7 & - & + & + & +\\ \hline
\text{product} & - & + & - & +
\end{array}
\]
The product is positive exactly for $\boxed{-7<x<-1\ \text{ or }\ x>\dfrac12}$ (the endpoints give $0$ and are excluded).''',
'Inequalities|Polynomials',2,
note='The poster asks how a sign chart works. Repeat of an earlier record (aliased).')

# ---------------- 1704691 MATHCOUNTS handbook warm-up P1-P3
b.add(1704691,1,r'''Coordinated Universal Time (UTC) is $5$ hours later than Eastern Standard Time (EST). If Nico and Jon start playing a tennis match in London at $8{:}00$ a.m.\ UTC and finish at $12{:}15$ p.m.\ EST, for how many minutes did they play?''',
r'''Convert the finishing time to UTC: $12{:}15$ p.m.\ EST is $5$ hours later in UTC, i.e.\ $5{:}15$ p.m.\ UTC. From $8{:}00$ a.m.\ to $5{:}15$ p.m.\ is $9$ hours $15$ minutes, that is $\boxed{555}$ minutes.

(Equivalently, the start, $8{:}00$ a.m.\ UTC, is $3{:}00$ a.m.\ EST. The answer $1395$ minutes comes from converting in the wrong direction, i.e.\ taking the start as $1{:}00$ p.m.\ EST on the previous day.)''',
'Date and time|Unit conversion',2,source=src('MATHCOUNTS',None,'Handbook',None),
note='The poster got 1395 and doubted the handbook answer 555; 555 is correct (the poster converted in the wrong direction).')
b.add(1704691,2,r'''A fair coin is flipped five times. What is the probability that it never lands heads up twice in a row? Express your answer as a common fraction.''',
r'''Let $a_n$ be the number of length-$n$ strings of H and T with no two consecutive H. A valid string ends in T (preceded by any valid string of length $n-1$) or in TH (preceded by any valid string of length $n-2$), so $a_n=a_{n-1}+a_{n-2}$ with $a_1=2$, $a_2=3$. Then $a_3=5$, $a_4=8$, $a_5=13$, and the probability is $\boxed{\dfrac{13}{32}}$.''',
'Probability|Recursive counting|Fibonacci sequence',3,source=src('MATHCOUNTS',None,'Handbook',None),
note='The poster got 17/32; the handbook answer 13/32 is correct. Repeat of an earlier record (aliased).')
b.add(1704691,3,r'''What is the mean of all three-digit positive integers whose digits are in the set $\{2,0,1,9\}$ (digits may be repeated)? What is the mean if the three digits must be distinct?''',
r'''\textbf{Digits may repeat.} The hundreds digit is $1$, $2$ or $9$ (each equally often), with mean $4$; the tens and units digits each run through $0,1,2,9$ equally often, with mean $3$. So the mean is $400+30+3=\boxed{433}$ ($48$ numbers).

\textbf{Distinct digits.} There are $3\cdot3\cdot2=18$ numbers. Each nonzero digit $d$ is the hundreds digit of $6$ of them, so the hundreds digits sum to $6\cdot12\cdot100=7200$. For the tens place: $0$ appears $6$ times (with the hundreds digit any of $3$ and the units digit any of the remaining $2$), and each nonzero digit appears $4$ times, giving $4\cdot12\cdot10=480$; similarly the units digits sum to $48$. The mean is $\dfrac{7200+480+48}{18}=\dfrac{7728}{18}=\boxed{\dfrac{1288}{3}=429\dfrac13}$.''',
'Mean|Digits and bases|Systematic counting',3,source=src('MATHCOUNTS',None,'Handbook',None),
note='The handbook answer 433 assumes digits may repeat; the poster\'s 429 1/3 is the mean for distinct digits. Repeat of an earlier record that asks both readings (aliased).')

# ---------------- 1704482 100 trailing zeros
b.add(1704482,1,r'''The number $n!$ ends in exactly $100$ zeros. What is the sum of the least and the greatest possible values of $n$?''',
r'''The number of trailing zeros of $n!$ is
\[
Z(n)=\left\lfloor\dfrac n5\right\rfloor+\left\lfloor\dfrac n{25}\right\rfloor+\left\lfloor\dfrac n{125}\right\rfloor+\cdots,
\]
the exponent of $5$ in $n!$ (there are always more factors $2$). $Z$ is nondecreasing and changes only at multiples of $5$. Now $Z(400)=80+16+3=99$ and $Z(405)=81+16+3=100$, while $Z(410)=82+16+3=101$. So $Z(n)=100$ exactly for $n=405,406,407,408,409$, and the answer is $405+409=\boxed{814}$.''',
'Trailing zeros|Factorials|Floor and ceiling functions',3)

# ---------------- 252019 2000(2000^2000)
b.add(252019,1,r'''$2000\left(2000^{2000}\right)=$

$\textbf{(A)}\ 2000^{2001}\qquad\textbf{(B)}\ 4000^{2000}\qquad\textbf{(C)}\ 2000^{4000}\qquad\textbf{(D)}\ 4{,}000{,}000^{2000}\qquad\textbf{(E)}\ 2000^{4{,}000{,}000}$''',
r'''Multiplying powers of the same base adds the exponents: $2000\cdot2000^{2000}=2000^1\cdot2000^{2000}=2000^{2001}$, choice $\boxed{\textbf{(A)}}$.

The others are different: $4000^{2000}=2^{2000}\cdot2000^{2000}$, $4{,}000{,}000^{2000}=2000^{4000}$, and $2000^{4{,}000{,}000}$ are all far larger.''',
'Exponents',1)

# ---------------- 1704105 extreme x^2+y^2 on a circle
figc=r'''pair O=(0,0),C=(3,2);real a=1.5;
pair u=unit(C);pair Pn=C-a*u,Pf=C+a*u;
draw((-0.5,0)--(5.2,0),gray,Arrow);draw((0,-0.5)--(0,4.3),gray,Arrow);
draw(circle(C,a),linewidth(0.9));
draw(O--Pf,blue+dashed);
pair X=C+a*dir(110);draw(O--X,red);draw(C--X,red+dashed);
dot(O);dot(C);dot(Pn);dot(Pf);dot(X);
label("$O$",O,SW);label("$C(k,c)$",C,SE);label("$P_1$",Pn+0.42*dir(255));label("$P_2$",Pf,NE);label("$X$",X,N);
label("$a$",(C+X)/2,E,red);'''
b.add(1704105,1,r'''Let $k$ and $c$ be real numbers and $a>0$. Over all points $(x,y)$ with $(x-k)^2+(y-c)^2=a^2$, find the greatest and the least values of $x^2+y^2$ (without ``bashing'').''',
r'''The point $X=(x,y)$ lies on the circle with centre $C=(k,c)$ and radius $a$, and $x^2+y^2=OX^2$, where $O$ is the origin. Let $d=OC=\sqrt{k^2+c^2}$.
'''+asy(figc,'5.5cm')+r'''
By the triangle inequality in triangle $OCX$ (or along a line),
\[
|d-a|=|OC-CX|\le OX\le OC+CX=d+a .
\]
Both bounds are attained on the line $OC$: the point $P_2$ of the circle beyond $C$ (on ray $OC$) has $OP_2=d+a$, and the point $P_1$ on the line $OC$ nearest $O$ has $OP_1=|d-a|$. (If $C=O$, every point has $OX=a$ and both bounds equal $a$.) Hence
\[
\max(x^2+y^2)=\boxed{\left(\sqrt{k^2+c^2}+a\right)^2},\qquad \min(x^2+y^2)=\boxed{\left(\sqrt{k^2+c^2}-a\right)^2}.
\]
For example, on $(x-3)^2+(y-4)^2=4$ the values of $x^2+y^2$ range from $(5-2)^2=9$ to $(5+2)^2=49$.''',
'Circles|Distance formula|Coordinate geometry|Triangle inequality|Maxima and minima',3,
note='The post asks for a fast general method; the record states the general problem and proves the formulas geometrically.')

# ---------------- 1704033 donuts
b.add(1704033,1,r'''You buy a dozen donuts at a shop with $4$ flavours: chocolate, lemon, jelly and glazed. There are unlimited glazed and chocolate donuts, but only $5$ lemon and $3$ jelly donuts left. How many different combinations of $12$ donuts can you get? (Donuts of the same flavour are identical.) A student computed $\dbinom{15}{3}-\left(\dbinom93+\dbinom{11}3-\dbinom53\right)$ and got $346$. Is this right?''',
r'''Let $c,\ell,j,g\ge0$ be the numbers of each flavour, with $c+\ell+j+g=12$, $\ell\le5$, $j\le3$. Without restrictions there are $\dbinom{15}{3}=455$ solutions (stars and bars).
\begin{itemize}
\item $\ell\ge6$: put $\ell=6+\ell'$; then the sum of the four variables is $6$: $\dbinom93=84$.
\item $j\ge4$: the sum becomes $8$: $\dbinom{11}{3}=165$.
\item both: the sum becomes $2$: $\dbinom53=10$.
\end{itemize}
By inclusion-exclusion the number of allowed combinations is
\[
455-(84+165-10)=455-239=\boxed{216}.
\]
The student's method and formula are correct, but the arithmetic is not: the expression equals $216$, not $346$.''',
'Stars and bars|Sets and inclusion–exclusion|Distributions and integer solutions',3,
note='The poster\'s expression is right but evaluates to 216, not the posted 346. Checked by brute force.')

# ---------------- 1703725 657^315 mod 1314
b.add(1703725,1,r'''Find the remainder when $657^{315}$ is divided by $1314$.''',
r'''Note that $1314=2\cdot657$. Let $N=657^{315}$. Then $N$ is divisible by $657$, and $N$ is odd (a power of an odd number). The multiples of $657$ that are odd are exactly the numbers $\equiv657\pmod{1314}$, because the multiples of $657$ alternate between $\equiv0$ and $\equiv657\pmod{1314}$ according to whether the cofactor is even or odd. Here $N=657\cdot657^{314}$ with an odd cofactor, so the remainder is $\boxed{657}$.''',
'Remainders and congruences|Modular exponentiation|Parity',3)

b.save()
