from qb import *
b=Bank('p228_03')

# ---------------- 1748824 prime conjecture
b.add(1748824,1,r'''A student conjectures: ``If $n$ is a prime number whose last digit is not $1$, $4$, $5$ or $9$, then $n^2+4$ is also prime.''
\begin{enumerate}
\item[(a)] Explain why, for a prime $n$ ending in $1$ or $9$, the number $n^2+4$ is never prime.
\item[(b)] Disprove the conjecture. What is the smallest odd prime for which it fails?
\end{enumerate}''',
r'''\textbf{(a)} If $n$ ends in $1$ or $9$, then $n^2$ ends in $1$, so $n^2+4$ ends in $5$. It is a multiple of $5$ greater than $5$, hence not prime.

\textbf{(b)} The conjecture already fails for $n=2$: $2^2+4=8$ is not prime. Among odd primes, the ones allowed by the conjecture end in $3$ or $7$:
\[
3^2+4=13,\quad 7^2+4=53,\quad 13^2+4=173,\quad 17^2+4=293
\]
are prime, but
\[
23^2+4=533=13\cdot41
\]
is not. So the conjecture is false, and the smallest odd counterexample is $\boxed{n=23}$. (The next ones are $43$, $53$ and $83$; for instance $43^2+4=1853=17\cdot109$.)''',
'Prime numbers|Counterexamples|Units digits and last digits',2,
note='The post states the conjecture as an observation and asks others to test it; the record asks for the reason behind the excluded digits and a counterexample (the claim is false: 2 and 23 fail). The remarks about units digits of consecutive primes are not used.')

# ---------------- 1717495 simplify
b.add(1717495,1,r'''Simplify each expression.
\begin{enumerate}
\item[(a)] $-2x+5+10x-9$
\item[(b)] $3(x+7)+2(-x+4)+5x$
\end{enumerate}''',
r'''\textbf{(a)} Collect like terms: $(-2x+10x)+(5-9)=\boxed{8x-4}$.

\textbf{(b)} Distribute first: $3x+21-2x+8+5x$. Then collect like terms: $(3x-2x+5x)+(21+8)=\boxed{6x+29}$.''',
'Algebraic manipulation|Algebraic expressions and identities',1,
note='The post says "simplify the following equations"; they are expressions.')

# ---------------- 1748217 chords; walking polygons
fig=r'''real r=sqrt(481)/4;pair O=(0,0);
pair A1=(-5,2.25),A2=(5,2.25),B1=(-4,-3.75),B2=(4,-3.75);
draw(circle(O,r),linewidth(0.8));
draw(A1--A2,linewidth(0.9));draw(B1--B2,linewidth(0.9));
draw((0,2.25)--(0,-3.75),dashed);
draw(O--A2,blue);draw(O--B2,blue);dot(O);
draw((0,2.25)--(0.3,2.25)--(0.3,1.95)--(0,1.95),linewidth(0.5));
draw((0,-3.75)--(0.3,-3.75)--(0.3,-3.45)--(0,-3.45),linewidth(0.5));
label("$O$",O,W);
label("$5$",(-2.5,2.25),N);label("$4$",(-2,-3.75),S);
label("$d$",(0,1.1),W);label("$6-d$",(0,-1.9),W);
label("$r$",(A2+O)/2+(0,0.1),N,blue);label("$r$",(B2+O)/2+(0.25,0),E,blue);'''
b.add(1748217,1,r'''A circle has two parallel chords of lengths $10$ and $8$ that are $6$ units apart. Find the radius of the circle.''',
r'''Let $r$ be the radius and let the chords of lengths $10$ and $8$ be at distances $d$ and $e$ from the centre $O$. The perpendicular from $O$ to a chord bisects it, so
\[
r^2=5^2+d^2=4^2+e^2,\qquad\text{hence}\qquad e^2-d^2=9 .
\]
\textbf{Same side of the centre.} Then $e-d=6$, so $e+d=\dfrac96=1.5<6$, which would make $d$ negative. Impossible.

\textbf{Opposite sides.} Then $d+e=6$ and $e-d=\dfrac96=1.5$, so $d=2.25$ and $e=3.75$.
'''+asy(fig,'5.5cm')+r'''
Hence $r^2=25+2.25^2=25+\dfrac{81}{16}=\dfrac{481}{16}$ (check: $16+3.75^2=16+\dfrac{225}{16}=\dfrac{481}{16}$), and
\[
r=\boxed{\dfrac{\sqrt{481}}{4}}\approx5.48 .
\]''',
'Arcs and chords|Circles|Pythagorean theorem|Casework',3,
note='The post also asks for a diagram; the solution sketch shows the only possible configuration (the chords on opposite sides of the centre).')
fig=r'''pair K=(0,0);path kev=K;pair p=K;real h=90;
for(int i=0;i<20;++i){p+=8*dir(h);kev=kev--p;h+=18;}
pair q=K;path al=K;real g=-90;
for(int i=0;i<24;++i){q+=6*dir(g);al=al--q;g+=15;}
draw(kev,blue+linewidth(0.9));draw(al,red+linewidth(0.9));
draw(K--(0,8),blue+linewidth(1.2),EndArrow(6));draw(K--(0,-6),red+linewidth(1.2),EndArrow(6));
dot(K);label("start",K,2*W);
label("Kevin",(-25.6,9),blue);label("$20$ sides of $8$ m",(-25.6,5),blue);
label("Allen",(22.9,2),red);label("$24$ sides of $6$ m",(22.9,-2),red);'''
b.add(1748217,2,r'''Kevin and Allen start at the same place and walk at the same constant speed. Kevin walks $8$ m north, turns $18^\circ$ counterclockwise, walks another $8$ m, turns $18^\circ$ counterclockwise again, and so on. At the same time Allen walks $6$ m south, turns $15^\circ$ counterclockwise, walks another $6$ m, and so on. How far must Kevin walk before he meets Allen again?''',
r'''Turning through the same angle after each equal step traces a regular polygon whose exterior angle is the turning angle. Kevin traces a regular polygon with $\dfrac{360}{18}=20$ sides of $8$ m (perimeter $160$ m) and Allen one with $\dfrac{360}{15}=24$ sides of $6$ m (perimeter $144$ m); each returns to the start exactly when he has walked a multiple of his perimeter.
'''+asy(fig,'8cm')+r'''
\textbf{They can meet only at the start.} Kevin's first step points north and he always turns left, so his convex polygon lies in the half-plane to the left of his first step, i.e.\ west of the north-south line through the start. Allen's first step points south and he turns left, so his polygon lies to the east of that line. The two polygons have only the starting point in common (the parts of them on the north-south line are Kevin's first side, going north, and Allen's first side, going south).

Since they walk at the same speed, they have always walked the same distance $D$. They are together at the start exactly when $D$ is a common multiple of $160$ and $144$. The least positive one is
\[
\operatorname{lcm}(160,144)=\operatorname{lcm}(2^5\cdot5,\ 2^4\cdot3^2)=2^5\cdot3^2\cdot5=1440 .
\]
So Kevin must walk $\boxed{1440}$ m (that is, $9$ laps for Kevin and $10$ for Allen).''',
'Regular polygons|HCF and LCM|Angle sums',4,
note='"Before turning again" read as: they keep repeating the walk-and-turn pattern. They start together and walk simultaneously at the same speed; the solution shows they can meet only at the start.')

# ---------------- 1747922 stars and bars and queues
b.add(1747922,1,r'''\begin{enumerate}
\item[(a)] How many solutions in nonnegative integers does $a+b+c+d+e=7$ have?
\item[(b)] Seven different people line up at five different machines (some queues may be empty; the order of the people within each queue matters). In how many ways can this happen?
\end{enumerate}''',
r'''\textbf{(a)} By stars and bars, a solution is an arrangement of $7$ stars and $4$ bars in a row, so there are $\dbinom{11}{4}=\boxed{330}$ solutions.

\textbf{(b)} A line-up is described by the queue sizes $(a,b,c,d,e)$, a solution of part (a), together with an ordering of the $7$ people (read the first queue front to back, then the second, and so on). Different pairs give different line-ups, so the count is
\[
\dbinom{11}{4}\cdot7!=330\cdot5040=\boxed{1663200}.
\]
Equivalently, arrange the $7$ people and $4$ identical dividers in a row: $\dfrac{11!}{4!}=1663200$.

So the number of solutions in (a) is not the number of ways in (b): part (b) is $7!$ times larger, because the people are distinct and their order in a queue matters. (The coefficient $\dbinom{11}{5}$ in the first expression of the post is a slip for $\dbinom{11}{4}$.)''',
'Stars and bars|Distributions and integer solutions|Permutations',3,
note='The post asks whether the number of solutions equals the number of ways for 7 people to line up at 5 machines, and offers C(11,5)*7! and C(11,4); the record asks for both counts (330 and 1663200). The poster\'s C(11,5) is corrected to C(11,4).')

# ---------------- 1746735 mn+1 multiple of 24
b.add(1746735,1,r'''If $m$ and $n$ are integers and $mn+1$ is a multiple of $24$, prove that $m+n$ is also a multiple of $24$.''',
r'''Since $24=3\cdot8$ with $\gcd(3,8)=1$, it suffices to show $3\mid m+n$ and $8\mid m+n$.

\textbf{Modulo 3.} $mn\equiv-1\pmod3$, so $3\nmid m$, i.e.\ $m\equiv\pm1\pmod3$ and $m^2\equiv1\pmod3$. Then
\[
m(m+n)=m^2+mn\equiv1-1=0\pmod3,
\]
and since $3\nmid m$, $3\mid m+n$.

\textbf{Modulo 8.} $mn\equiv-1\pmod8$, so $m$ is odd, and every odd square is $\equiv1\pmod8$ (as $(2k+1)^2=4k(k+1)+1$ with $k(k+1)$ even). Then
\[
m(m+n)=m^2+mn\equiv1-1=0\pmod8,
\]
and since $m$ is odd, $8\mid m+n$.

Hence $24\mid m+n$. $\blacksquare$''',
'Remainders and congruences|Divisibility|Quadratic residues',4)

# ---------------- 1748168 3x3 system
b.add(1748168,1,r'''Solve the system by substitution:
\[
-x-y-3z=-9,\qquad z=-3x-1,\qquad x=5y-z+23 .
\]''',
r'''Substitute $z=-3x-1$ into the other two equations.

First equation: $-x-y-3(-3x-1)=-9$, i.e.\ $8x-y+3=-9$, so $y=8x+12$.

Third equation: $x=5y+3x+1+23$, i.e.\ $-2x=5y+24$. Substituting $y=8x+12$: $-2x=40x+60+24$, so $-42x=84$ and $x=-2$.

Then $y=8(-2)+12=-4$ and $z=-3(-2)-1=5$. The solution is $\boxed{(x,y,z)=(-2,-4,5)}$.

Check: $2+4-15=-9$; $-3(-2)-1=5$; $5(-4)-5+23=-2$.''',
'Systems of linear equations|Substitution',2)

# ---------------- 1747797 max of product
b.add(1747797,1,r'''Consider $P=(x-y+1)(y-z+2)(z-x+3)$ for real numbers $x,y,z$.
\begin{enumerate}
\item[(a)] Show that $P$ has no maximum value over all real $x,y,z$.
\item[(b)] Find the maximum value of $P$ when all three factors are positive.
\end{enumerate}''',
r'''Put $a=x-y+1$, $b=y-z+2$, $c=z-x+3$. Then $a+b+c=6$ for every $x,y,z$. Conversely any $a,b$ can occur (take $z=0$, $y=b-2$, $x=a+b-3$), with $c=6-a-b$.

\textbf{(a)} Take $a=b=-t$ with $t>0$, so $c=6+2t$ and $P=t^2(6+2t)$, which exceeds every bound as $t$ grows. So $P$ has no maximum.

\textbf{(b)} For positive $a,b,c$ with $a+b+c=6$, AM-GM gives
\[
abc\le\left(\dfrac{a+b+c}{3}\right)^3=2^3=8,
\]
with equality for $a=b=c=2$, e.g.\ $(x,y,z)=(1,0,0)$: $(1+1)(0+2)(-1+3)=8$. The maximum is $\boxed{8}$.''',
'AM-GM inequality|Maxima and minima|Substitution',4,
note='As posted ("maximum possible value", no conditions) the problem has no answer: the product is unbounded above. The record adds part (a) and states the condition that the factors are positive, under which the intended answer 8 holds.')

# ---------------- 1746979 system one solution
b.add(1746979,1,r'''Let $a,b,c,d,e$ be constants, with $b\ne c$ and $a\ne0$, in the system
\[
ax+by=d,\qquad ax+cy=e .
\]
A student thinks the system might have no solution. Prove that it always has exactly one solution $(x,y)$, and find it.''',
r'''Subtracting the second equation from the first eliminates $x$:
\[
(b-c)y=d-e\quad\Longrightarrow\quad y=\dfrac{d-e}{b-c},
\]
which is allowed because $b\ne c$. Then the first equation gives $ax=d-by$, and since $a\ne0$,
\[
x=\dfrac{d-by}{a}=\dfrac{d(b-c)-b(d-e)}{a(b-c)}=\dfrac{be-cd}{a(b-c)} .
\]
So any solution must be this pair, and substituting back shows that it satisfies both equations (the first by the choice of $x$, the second because the difference of the equations holds). Hence there is exactly one solution,
\[
\boxed{(x,y)=\left(\dfrac{be-cd}{a(b-c)},\ \dfrac{d-e}{b-c}\right)}.
\]
A system of two linear equations has no solution only when the two lines are parallel and distinct; here the lines have slopes $-\dfrac ab\ne-\dfrac ac$ (or one of them is vertical and the other is not), so they always meet in one point.''',
'Systems of linear equations|Linear equations',2,source=src('Introduction to Algebra',None,None,'5.3.4'),
note='AoPS Introduction to Algebra problem 5.3.4. The solutions manual is right (exactly one solution); the poster\'s worry that there may be none is answered.')

# ---------------- 1747574 triangular 9n+1
b.add(1747574,1,r'''Let $n$ be a triangular number.
\begin{enumerate}
\item[(a)] Prove that $9n+1$ is a triangular number.
\item[(b)] Show that $25n+1$ and $49n+1$ need not be triangular, and find constants $p$ and $q$ such that $25n+p$ and $49n+q$ are always triangular.
\end{enumerate}''',
r'''Write $n=T_k=\dfrac{k(k+1)}{2}$ with $k\ge0$ an integer.

\textbf{(a)}
\[
9n+1=\dfrac{9k^2+9k+2}{2}=\dfrac{(3k+1)(3k+2)}{2}=T_{3k+1}. \qquad\blacksquare
\]

\textbf{(b)} For $n=1$: $25n+1=26$ and $49n+1=50$, and neither is triangular (the triangular numbers near them are $21,28$ and $45,55$). So the claim fails for $25$ and $49$.

The same computation works with a different constant. For any integer $m\ge0$,
\[
T_{(2m+1)k+m}=\dfrac{\bigl((2m+1)k+m\bigr)\bigl((2m+1)k+m+1\bigr)}{2}=(2m+1)^2\,\dfrac{k(k+1)}{2}+\dfrac{m(m+1)}{2},
\]
because expanding the numerator gives $(2m+1)^2k^2+(2m+1)k(2m+1)+m(m+1)$. Hence $(2m+1)^2n+T_m$ is always triangular. With $m=1,2,3$ this gives
\[
9n+1,\qquad \boxed{25n+3},\qquad \boxed{49n+6},
\]
so $p=3$ and $q=6$ (for example $n=1$: $28=T_7$ and $55=T_{10}$).''',
'Triangular numbers|Algebraic expressions and identities|Counterexamples',4,
note='The posted claim is false for 25n + 1 and 49n + 1 (n = 1 gives 26 and 50). The record proves the 9n + 1 case and asks for the correct constants 25n + 3 and 49n + 6 (general (2m+1)^2 n + T_m). Checked for the first 2000 triangular numbers.')

# ---------------- 1747745 phi iteration
b.add(1747745,1,r'''For a positive integer $m$, let $\phi(m)$ be the number of integers $k$ with $1\le k\le m$ and $\gcd(k,m)=1$. For every integer $n\ge10$ the following is done: $\phi$ is applied to $n$ repeatedly until a one-digit number is obtained, and that one-digit number is put into a set $S$ (which starts empty). How many elements does $S$ have at the end?''',
r'''\textbf{Which digits can occur.} The process starts at $n\ge10$ and stops at the first value below $10$, so the number put into $S$ is $\phi(m)$ for some $m\ge10$. For $m\ge3$, $\phi(m)$ is even: if $m$ has an odd prime factor $p$ with $p^a\parallel m$, then $\phi(m)$ is divisible by $\phi(p^a)=p^{a-1}(p-1)$, which is even; otherwise $m=2^a$ with $a\ge2$ and $\phi(m)=2^{a-1}$ is even. Also $\phi(m)\ge1$. So the digit is $2$, $4$, $6$ or $8$.

\textbf{The digit $2$ never occurs.} If $\phi(m)=2$ and a prime $p$ divides $m$, then $p-1$ divides $\phi(m)=2$, so $p\in\{2,3\}$. Writing $m=2^a3^b$: $\phi(m)=2$ forces $m\in\{3,4,6\}$ (for example $a\ge3$ gives $4\mid\phi(m)$, and $b\ge2$ gives $3\mid\phi(m)$). All of these are below $10$, so $\phi(m)=2$ never happens with $m\ge10$.

\textbf{The digits $4$, $6$, $8$ occur.} $\phi(10)=4$, $\phi(14)=6$, $\phi(15)=8$.

Hence $S=\{4,6,8\}$ and $|S|=\boxed{3}$.''',
'Euler\'s theorem and totient|Parity|Proof by cases',5,
note='The post defines phi(n) as the count of positive integers less than n coprime to n (the same for n >= 2) and says "for all positive integers n". Read as starting from every n >= 10, so that at least one application is needed; if one-digit n were included unchanged, S would trivially be {1,...,9}. Checked by computer for n < 10^5.')

# ---------------- 1747765 zeta(-1)
b.add(1747765,1,r'''The Riemann zeta function is defined for real $s>1$ by $\zeta(s)=\sum_{k=1}^{\infty}\dfrac{1}{k^s}$. Someone argues:
\[
\zeta(-1)=\dfrac{1}{1^{-1}}+\dfrac{1}{2^{-1}}+\dfrac{1}{3^{-1}}+\cdots=1+2+3+\cdots=\sum_{k=1}^{\infty}k .
\]
What is wrong with this argument?''',
r'''The series $\sum\dfrac{1}{k^s}$ converges only for $s>1$, so the formula defines $\zeta(s)$ only there. For $s=-1$ the series is $1+2+3+\cdots$, whose partial sums are
\[
1+2+\cdots+N=\dfrac{N(N+1)}{2},
\]
which grow without bound. So $\sum_{k\ge1}k$ diverges: it is not a number, and it cannot equal $\zeta(-1)$ or anything else.

The first equality in the argument substitutes $s=-1$ into a formula that is not valid at $s=-1$. The value $\zeta(-1)$ is defined in a different way (by extending $\zeta$ from $s>1$ to other $s$, a process called analytic continuation), and with that definition $\zeta(-1)=-\dfrac{1}{12}$; but this does not mean that $1+2+3+\cdots$ converges to $-\dfrac{1}{12}$. $\boxed{\text{The series formula for }\zeta(s)\text{ does not hold at }s=-1\text{; the series diverges.}}$''',
'Sequences and series|Summation|Arithmetic sequences',3,
note='The post presents the "identity" zeta(-1) = 1 + 2 + 3 + ...; the record asks for the error. The value -1/12 is quoted as a known fact, not proved.')

# ---------------- 1747731 discarded mock
b.add(1747731,1,r'''How many ordered $6$-tuples of positive integers $(a_1,a_2,a_3,a_4,a_5,a_6)$ satisfy $a_n>n$ for every $n$ and $a_1+a_2+a_3+a_4+a_5+a_6<150$?''',
r'''Put $b_n=a_n-(n+1)$, so the conditions $a_n\ge n+1$ become $b_n\ge0$. Since $\sum_{n=1}^{6}(n+1)=27$, the condition $\sum a_n<150$, i.e.\ $\sum a_n\le149$, becomes
\[
b_1+b_2+\cdots+b_6\le122 .
\]
Add a slack variable $b_7=122-\sum_{n\le6}b_n\ge0$; the tuples correspond to the solutions of $b_1+\cdots+b_7=122$ in nonnegative integers, and by stars and bars there are
\[
\dbinom{122+6}{6}=\dbinom{128}{6}=\boxed{5423611200}.
\]''',
'Stars and bars|Distributions and integer solutions|Bijections',4,
note='Problem 1 of the discarded mock questions; "sets" read as ordered 6-tuples. Count checked by a dynamic-programming computation.')
b.add(1747731,2,r'''Three friends go to a concert. Ann arrives at a time chosen uniformly at random between 8:00 and 8:30, Ben between 8:10 and 8:40, and Cal between 8:20 and 8:30, independently. Each stays for exactly $5$ minutes and then leaves. What is the probability that all three of them see each other?''',
r'''Measure times in minutes after 8:00: $A\in[0,30]$, $B\in[10,40]$, $C\in[20,30]$, uniform and independent. Each pair sees each other exactly when their arrival times differ by at most $5$; then the three time intervals overlap pairwise and so have a common point. So we need
\[
\max(A,B,C)-\min(A,B,C)\le5 .
\]
The sample space has volume $30\cdot30\cdot10=9000$. Fix $C=k\in[20,30]$ and write $u=A-k$, $v=B-k$. We need $u,v\in[-5,5]$ and $|u-v|\le5$; the constraint $A\le30$ gives $u\le m$ with $m=\min(5,30-k)$, while $A\ge0$, $B\ge10$ and $B\le40$ are automatic.

For $0\le m\le5$ the area of $\{-5\le u\le m,\ -5\le v\le5,\ |u-v|\le5\}$ is
\[
\int_{-5}^{0}(u+10)\,du+\int_0^{m}(10-u)\,du=\dfrac{75}{2}+10m-\dfrac{m^2}{2}.
\]
For $20\le k\le25$, $m=5$ and the area is $75$; for $25\le k\le30$, $m=30-k$. The favourable volume is
\[
5\cdot75+\int_0^5\left(\dfrac{75}{2}+10m-\dfrac{m^2}{2}\right)dm=375+\dfrac{375}{2}+125-\dfrac{125}{6}=\dfrac{2000}{3}.
\]
The probability is $\dfrac{2000}{3\cdot9000}=\boxed{\dfrac{2}{27}}$.''',
'Geometric probability|Probability|Calculus',5,
note='Problem 2 of the discarded mock questions; the usernames are replaced by names. Arrival times are taken uniform and independent, and "all of them see each other" as every pair being at the concert together at some moment (equivalent to all three at once). Checked by exact integration and simulation.')
b.add(1747731,3,r'''For each positive integer $n$, let $a_n$ be the value of $x$ that minimizes
\[
f(x)=\dfrac{x^2}{x-n}
\]
on the interval $x>n$. Evaluate $a_1+a_2+\cdots+a_{100}$.''',
r'''Put $t=x-n>0$. Then
\[
f(x)=\dfrac{(t+n)^2}{t}=t+2n+\dfrac{n^2}{t}\ge2n+2\sqrt{t\cdot\dfrac{n^2}{t}}=4n
\]
by AM-GM, with equality exactly when $t=\dfrac{n^2}{t}$, i.e.\ $t=n$. So the minimum is attained only at $x=2n$, and $a_n=2n$. Hence
\[
a_1+\cdots+a_{100}=2(1+2+\cdots+100)=2\cdot5050=\boxed{10100}.
\]''',
'AM-GM inequality|Maxima and minima|Arithmetic sequences',3,
note='Problem 3 of the discarded mock questions.')
fig=r'''pair A=(1,3.6),B=(0,0),C=(6,0);
real d=2*(A.x*(B.y-C.y)+B.x*(C.y-A.y)+C.x*(A.y-B.y));
pair O=((dot(A,A)*(B.y-C.y)+dot(B,B)*(C.y-A.y)+dot(C,C)*(A.y-B.y))/d,(dot(A,A)*(C.x-B.x)+dot(B,B)*(A.x-C.x)+dot(C,C)*(B.x-A.x))/d);
pair G=(A+B+C)/3,H=A+B+C-2*O;
draw(A--B--C--cycle,linewidth(0.9));
draw(circle(O,abs(A-O)),gray);
draw(H+0.35*(H-O)--O+0.7*(O-H),red+dashed);
dot(O);dot(G);dot(H);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);
label("$O$",O,N);label("$G$",G,S);label("$H$",H,N);'''
b.add(1747731,4,r'''Triangle $ABC$ has circumcentre $O$, orthocentre $H$ and centroid $G$. The distance between $O$ and $G$ is $\dfrac{x^2-16}{x^2-9}$. Find the distance between $O$ and $H$ in terms of $x$.''',
r'''\textbf{Euler line.} Place the origin at $O$ and let $\mathbf a,\mathbf b,\mathbf c$ be the position vectors of $A,B,C$; then $|\mathbf a|=|\mathbf b|=|\mathbf c|=R$, the circumradius. Let $\mathbf h=\mathbf a+\mathbf b+\mathbf c$. Then
\[
(\mathbf h-\mathbf a)\cdot(\mathbf b-\mathbf c)=(\mathbf b+\mathbf c)\cdot(\mathbf b-\mathbf c)=|\mathbf b|^2-|\mathbf c|^2=0,
\]
so the point $\mathbf h$ lies on the altitude from $A$; in the same way it lies on the altitudes from $B$ and $C$, so it is the orthocentre $H$. The centroid is $G=\dfrac{\mathbf a+\mathbf b+\mathbf c}{3}=\dfrac{\mathbf h}{3}$. Hence $O$, $G$, $H$ are collinear and
\[
OH=3\,OG .
\]
'''+asy(fig,'5.5cm')+r'''
Therefore
\[
OH=\boxed{\dfrac{3(x^2-16)}{x^2-9}}.
\]
(For this to be a distance, $x$ must satisfy $|x|\ge4$ or $|x|<3$.)''',
'Circumcircles and circumcentres|Medians and centroids|Altitudes|Vectors',4,
note='Problem 4 of the discarded mock questions; the points m, l, c of the post are renamed O, H, G.')

# ---------------- 1747684 fence
fig=r'''pair P=(0,0),Q=(36,0),R=(36,18),T=(0,18);
fill((-4,18)--(40,18)--(40,22)--(-4,22)--cycle,palegray);
label("house",(18,20));
draw(T--P--Q--R,linewidth(1.1));
label("$x$",(P+Q)/2,S);label("$y$",(P+T)/2,W);label("$y$",(Q+R)/2,E);
label("garden",(18,9));'''
b.add(1747684,1,r'''Anand bought a $72$-foot wire fence for his rectangular garden and wants to enclose the largest possible area. One side of the garden is along his house, so he only needs to fence the other three sides. In square feet, what is the largest area he can enclose?''',
r'''Let the side parallel to the house be $x$ and the two sides perpendicular to it be $y$, so $x+2y=72$.
'''+asy(fig,'5.5cm')+r'''
The area is
\[
xy=(72-2y)y=-2(y^2-36y)=648-2(y-18)^2,
\]
which is largest when $y=18$, giving $x=36$ and area $\boxed{648}$ square feet.''',
'Rectangles|Lengths, perimeter, and area|Maxima and minima|Completing the square',3)

# ---------------- 1747571 8n+1
b.add(1747571,1,r'''Prove that a nonnegative integer $n$ is a triangular number if and only if $8n+1$ is a perfect square.''',
r'''If $n=\dfrac{k(k+1)}{2}$ for an integer $k\ge0$, then $8n+1=4k^2+4k+1=(2k+1)^2$.

Conversely, suppose $8n+1=m^2$ with $m\ge0$. Then $m^2$ is odd, so $m$ is odd, $m=2k+1$ with $k\ge0$. Hence $8n=(2k+1)^2-1=4k(k+1)$ and $n=\dfrac{k(k+1)}{2}$, a triangular number. $\blacksquare$''',
'Triangular numbers|Perfect squares|Parity',2)

# ---------------- 1747361 Platonic solids (alias)
b.add(1747361,1,r'''Prove that there are exactly five Platonic solids (convex polyhedra whose faces are congruent regular polygons, with the same number of faces at every vertex).''',
r'''If each face is a regular $p$-gon and $q$ faces meet at each vertex, the face angles at a vertex add up to less than $360^\circ$: $q\cdot\dfrac{180(p-2)}{p}<360$, i.e.\ $(p-2)(q-2)<4$. With $p,q\ge3$ this leaves $(p,q)=(3,3),(3,4),(3,5),(4,3),(5,3)$, realised by the tetrahedron, octahedron, icosahedron, cube and dodecahedron. $\blacksquare$''',
'Polyhedra|Regular polygons|Angle sums',4,
note='The poster asks for a non-paper-folding proof. Repeat of an earlier record (aliased).')

# ---------------- 1746837 parallelogram construction
fig=r'''pair O=(0,0);real th=55;real p=3,q=2;
pair A=-p*dir(0),C=p*dir(0),B=-q*dir(th),D=q*dir(th);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--C,blue+linewidth(0.8));draw(B--D,blue+linewidth(0.8));
draw(arc(O,0.5,0,th),linewidth(0.6));label("$\theta$",0.8*dir(th/2));
dot(O);
label("$A$",A,W);label("$B$",B,SW);label("$C$",C,E);label("$D$",D,NE);label("$O$",O,dir(-60));
label("$\dfrac{d_1}{2}$",(A+O)/2,N,blue);label("$\dfrac{d_1}{2}$",(C+O)/2+(0.4,0),N,blue);
label("$\dfrac{d_2}{2}$",(B+O)/2,dir(th+90),blue);label("$\dfrac{d_2}{2}$",0.4*D,dir(th+90),blue);'''
b.add(1746837,1,r'''True or false: a parallelogram is determined uniquely (up to congruence) if the lengths of both diagonals and the angle between them are given. Give reasons, including a construction.''',
r'''\textbf{True}, for diagonal lengths $d_1,d_2>0$ and an angle $\theta$ with $0^\circ<\theta<180^\circ$.

\textbf{Construction.} Draw a segment $AC$ of length $d_1$ with midpoint $O$. Draw the line through $O$ making the angle $\theta$ with $AC$, and on it mark $B$ and $D$ on opposite sides of $O$ with $OB=OD=\dfrac{d_2}{2}$. The diagonals of the quadrilateral $ABCD$ bisect each other, so $ABCD$ is a parallelogram (triangles $OAB$ and $OCD$ are congruent by SAS, so $\angle OAB=\angle OCD$ and $AB\parallel CD$; similarly $AD\parallel BC$). It has the required diagonals and angle.
'''+asy(fig,'7.5cm')+r'''
\textbf{Uniqueness.} In any parallelogram $ABCD$ with these data, the diagonals bisect each other at a point $O$, so $OA=OC=\dfrac{d_1}{2}$ and $OB=OD=\dfrac{d_2}{2}$, and the angles at $O$ are $\theta$ and $180^\circ-\theta$. By SAS the four triangles $OAB$, $OBC$, $OCD$, $ODA$ are determined (two of them have angle $\theta$ at $O$, two have $180^\circ-\theta$), so all the sides and angles of the parallelogram are determined. Two such parallelograms can be moved onto each other by placing their diagonals on top of each other, so they are congruent. $\boxed{\text{True}}$''',
'Parallelograms|Diagonals|Congruence',3)

# ---------------- 1747120 negative products
b.add(1747120,1,r'''Using only the distributive law, the fact that $0\cdot a=a\cdot0=0$, and the meaning of $-a$ as the number with $a+(-a)=0$, prove that $(-2)\cdot3=-6$ and $(-2)\cdot(-3)=6$.''',
r'''\textbf{$(-2)\cdot3=-6$.} By the distributive law,
\[
0=0\cdot3=\bigl(2+(-2)\bigr)\cdot3=2\cdot3+(-2)\cdot3=6+(-2)\cdot3 .
\]
So $(-2)\cdot3$ is the number which added to $6$ gives $0$, i.e.\ $(-2)\cdot3=-6$.

\textbf{$(-2)\cdot(-3)=6$.} Again,
\[
0=(-2)\cdot0=(-2)\cdot\bigl(3+(-3)\bigr)=(-2)\cdot3+(-2)\cdot(-3)=-6+(-2)\cdot(-3).
\]
So $(-2)\cdot(-3)$ is the number which added to $-6$ gives $0$, i.e.\ $(-2)\cdot(-3)=6$. $\blacksquare$

(In words: if $(-2)\cdot(-3)$ were anything other than $6$, the distributive law, which the post's example $2(3+4)=2\cdot3+2\cdot4$ illustrates, would fail for $(-2)\bigl(3+(-3)\bigr)$.)''',
'Algebraic manipulation|Whole-number operations',2,
note='The post asks for a visual demonstration of (-2)(3) = -6 and (-2)(-3) = 6; the record asks for the proof from the distributive law.')

# ---------------- 1741498 fruit chew (alias)
b.add(1741498,1,r'''A box contains $4$ chocolates and $1$ fruit chew. Clark and Chloe take turns drawing a treat out of the box at random, without replacement, and whoever draws the fruit chew wins. Clark draws first. What is the probability that Chloe wins? Express your answer as a common fraction.''',
r'''The fruit chew is equally likely to be in any of the five draw positions; Chloe makes draws $2$ and $4$, so she wins with probability $\boxed{\dfrac25}$.''',
'Probability|Sampling without replacement|Symmetry',2,
note='The poster got 1/5; the answer 2/5 is correct. Repeat of an earlier record (aliased).')

# ---------------- 1747050 Dak coins
b.add(1747050,1,r'''Dak has a quarter, a dime, a nickel and a penny. How many different amounts can be obtained by using one or more of the coins in Dak's collection?''',
r'''The subsets of $\{25,10,5\}$ have the sums $0,5,10,15,25,30,35,40$, all different multiples of $5$. Adding the penny or not turns each into two amounts, $s$ and $s+1$; since all the $s$ are multiples of $5$, the $16$ amounts
\[
0,1,5,6,10,11,15,16,25,26,30,31,35,36,40,41
\]
are all different. Excluding $0$ (no coins), there are $\boxed{15}$ amounts. In other words, every one of the $2^4-1=15$ nonempty sets of coins gives a different total.''',
'Money and currency|Systematic counting|Counting principles',2,source=src('MATHCOUNTS',2018,'Chapter',None,rnd='Sprint'),
note='2018 MATHCOUNTS Chapter Sprint, as titled (problem number not given).')

# ---------------- 1706241 x+1/x=4
b.add(1706241,1,r'''If $x+\dfrac1x=4$, find $x^5+\dfrac{1}{x^5}$.''',
r'''Let $s_k=x^k+\dfrac{1}{x^k}$, so $s_1=4$. Then
\[
s_2=s_1^2-2=14,\qquad s_3=s_1^3-3s_1=64-12=52,
\]
and since $s_2s_3=\left(x^2+\dfrac{1}{x^2}\right)\left(x^3+\dfrac{1}{x^3}\right)=s_5+s_1$,
\[
s_5=s_2s_3-s_1=14\cdot52-4=\boxed{724}.
\]''',
'Algebraic expressions and identities|Recurrence relations',3,
note='The post asks for "(x^5)/1+x^5", read as x^5 + 1/x^5 (the reading in which the question is determined by the condition and fits x + 1/x). Checked numerically with x = 2 + sqrt 3.')

# ---------------- 1738203 probability problems
b.add(1738203,1,r'''Calvin takes a $25$-question multiple-choice test on which each question has five possible answers and each correct answer scores $1$ point. He answers the first $16$ questions correctly, then guesses randomly on the last $9$. What is the probability that Calvin scores exactly $20$? Express your answer as a common fraction.''',
r'''He needs exactly $4$ correct guesses out of $9$, each correct with probability $\dfrac15$ independently. By the binomial formula,
\[
\dbinom94\left(\dfrac15\right)^4\left(\dfrac45\right)^5=\dfrac{126\cdot4^5}{5^9}=\boxed{\dfrac{129024}{1953125}}\approx0.066 .
\]''',
'Binomial probability|Probability|Independent events',3,
note='One point per correct answer and no penalty for wrong answers are assumed.')
b.add(1738203,2,r'''April's science class has $32$ students, including April and her best friend Brooke. The teacher arranges the students randomly into $8$ tables of $4$, every arrangement being equally likely.
\begin{enumerate}
\item[(a)] What is the probability that April and Brooke are at the same table?
\item[(b)] The teacher makes a new independent random arrangement every four weeks. The school year has $36$ weeks and the first arrangement is made on the first day of school. What is the probability that April and Brooke sit at the same table at least once during the year?
\end{enumerate}''',
r'''\textbf{(a)} Wherever April sits, the other $3$ seats at her table are equally likely to be any $3$ of the $31$ other seats, so Brooke is at April's table with probability $\boxed{\dfrac{3}{31}}$.

\textbf{(b)} Arrangements are made at the start of weeks $1,5,9,\dots,33$, which is $9$ arrangements. Each time, the probability that they are \emph{not} together is $\dfrac{28}{31}$, independently. So
\[
P(\text{together at least once})=\boxed{1-\left(\dfrac{28}{31}\right)^9}\approx0.600 .
\]''',
'Complementary probability|Independent events|Probability',3,
note='Problems 2a and 2b of the post, kept together as one record (q02). The 36-week year with a new arrangement every 4 weeks starting on day one gives 9 arrangements.')

# ---------------- 1742452 selection
b.add(1742452,1,r'''A husband and wife apply for two vacancies for the same post. The probability that the husband is selected is $\dfrac17$ and the probability that the wife is selected is $\dfrac16$, independently. What is the probability that exactly one of them is selected?''',
r'''Exactly one is selected if the husband is selected and the wife is not, or the other way round:
\[
\dfrac17\cdot\dfrac56+\dfrac67\cdot\dfrac16=\dfrac{5}{42}+\dfrac{6}{42}=\boxed{\dfrac{11}{42}}.
\]''',
'Independent events|Probability',2,
note='Independence of the two selections is stated (the post assumes it implicitly). The names P and Q are replaced by husband and wife.')

# ---------------- 1746955 sqrt inequality
b.add(1746955,1,r'''Let $a,b,c>0$ with $a^2+b^2+c^2=1$. Prove that
\[
\sqrt{1-ab}+\sqrt{1-bc}+\sqrt{1-ca}\ge\sqrt6 .
\]''',
r'''Let $x_1=1-ab$, $x_2=1-bc$, $x_3=1-ca$ (all positive, as $ab\le\dfrac{a^2+b^2}{2}<1$), and write $\sum$ for sums over $i=1,2,3$.

\textbf{Step 1: $\left(\sum\sqrt{x_i}\right)^2\sum x_i^2\ge\left(\sum x_i\right)^3$.} By Cauchy-Schwarz,
\[
\left(\sum x_i\right)^2=\left(\sum x_i^{\dfrac14}\cdot x_i^{\dfrac34}\right)^2\le\sum\sqrt{x_i}\cdot\sum x_i^{\dfrac32},
\qquad
\sum x_i^{\dfrac32}=\sum\sqrt{x_i}\cdot x_i\le\sqrt{\sum x_i}\sqrt{\sum x_i^2}.
\]
Combining, $\left(\sum x_i\right)^2\le\sum\sqrt{x_i}\cdot\sqrt{\sum x_i}\sqrt{\sum x_i^2}$; dividing by $\sqrt{\sum x_i}$ and squaring gives the claim.

\textbf{Step 2: the sums.} Let $p=ab+bc+ca$ and $q=a^2b^2+b^2c^2+c^2a^2$. Then $\sum x_i=3-p$ and $\sum x_i^2=3-2p+q$. Moreover $0<p\le a^2+b^2+c^2=1$, and
\[
1=(a^2+b^2+c^2)^2=(a^4+b^4+c^4)+2q\ge q+2q=3q,
\]
so $q\le\dfrac13$ (using $a^4+b^4+c^4\ge a^2b^2+b^2c^2+c^2a^2$).

\textbf{Step 3: a one-variable inequality.} By Steps 1 and 2,
\[
\left(\sum\sqrt{x_i}\right)^2\ge\dfrac{(3-p)^3}{3-2p+q}\ge\dfrac{(3-p)^3}{\dfrac{10}{3}-2p}.
\]
It remains to show $(3-p)^3\ge6\left(\dfrac{10}{3}-2p\right)=20-12p$ for $0<p\le1$. Let $g(p)=(3-p)^3-20+12p$. Then $g(1)=8-20+12=0$ and
\[
g(p)=-p^3+9p^2-15p+7=(1-p)^2(7-p)\ge0 .
\]
Hence $\left(\sum\sqrt{x_i}\right)^2\ge6$, which is the inequality. Equality holds for $a=b=c=\dfrac{1}{\sqrt3}$, when each term is $\sqrt{\dfrac23}$. $\blacksquare$''',
'Cauchy-Schwarz inequality|Inequalities|Algebraic manipulation',6,
note='Proof by a Holder-type bound obtained from two applications of Cauchy-Schwarz. The inequality and every step were checked numerically on random points of the sphere.')

# ---------------- 1746950 equilateral acres
fig=r'''real s=4;pair A=(0,0),B=(s,0),C=(s/2,s*sqrt(3)/2),M=(s/2,0);
draw(A--B--C--cycle,linewidth(0.9));
draw(C--M,dashed);draw(M+(0,0.2)--M+(0.2,0.2)--M+(0.2,0),linewidth(0.5));
label("$s$",(A+C)/2,NW);label("$s$",(B+C)/2,NE);label("$s$",(s/4,0),S);
label("$\dfrac{\sqrt{3}}{2}s$",(C+M)/2,W);
label("area $435600$ ft$^2$",(s/2,-0.75));'''
b.add(1746950,1,r'''A field in the shape of an equilateral triangle covers an area of $10$ acres. Calculate the length of a side of the field in feet, to the nearest foot. ($1$ acre $=43560$ square feet; a calculator may be used.)''',
r'''The area is $10\cdot43560=435600$ square feet. An equilateral triangle of side $s$ has height $\dfrac{\sqrt3}{2}s$, so its area is $\dfrac{\sqrt3}{4}s^2$.
'''+asy(fig,'4.5cm')+r'''
Hence
\[
\dfrac{\sqrt3}{4}s^2=435600\ \Longrightarrow\ s^2=\dfrac{1742400}{\sqrt3}=\dfrac{1320^2}{\sqrt3}\ \Longrightarrow\ s=\dfrac{1320}{\sqrt[4]{3}}\approx\boxed{1003\text{ feet}}.
\]''',
'Equilateral triangles|Lengths, perimeter, and area|Unit conversion',2,
note='The acre conversion (43560 square feet) is stated in the question; the post assumes it.')

# ---------------- 1742477 5-sided dice
b.add(1742477,1,r'''Two fair $5$-sided dice, each numbered $1$ to $5$, are tossed. What is the probability that the sum of the numbers that come up is divisible by $3$?''',
r'''The sum is between $2$ and $10$, so it must be $3$, $6$ or $9$. Sum $3$: $(1,2),(2,1)$. Sum $6$: $(1,5),(2,4),(3,3),(4,2),(5,1)$. Sum $9$: $(4,5),(5,4)$. That is $9$ of the $25$ equally likely outcomes, so the probability is $\boxed{\dfrac{9}{25}}$.''',
'Dice probability|Probability|Systematic counting',2)

# ---------------- 1746203 Burton congruences
b.add(1746203,1,r'''Prove that if $a$ is an odd integer, then $a^2\equiv1\pmod8$.''',
r'''Write $a=2k+1$. Then $a^2=4k^2+4k+1=4k(k+1)+1$. One of $k$ and $k+1$ is even, so $8\mid4k(k+1)$ and $a^2\equiv1\pmod8$. $\blacksquare$''',
'Remainders and congruences|Parity|Perfect squares',2,
note='Burton, Elementary Number Theory, exercise; problem 1 of the post.')
b.add(1746203,2,r'''Prove that for every integer $a$, $a^3\equiv0$, $1$ or $6\pmod7$.''',
r'''Modulo $7$, $a\equiv0,\pm1,\pm2,\pm3$, and $(-a)^3=-a^3$. Since $0^3=0$, $1^3=1$, $2^3=8\equiv1$ and $3^3=27\equiv6\equiv-1\pmod7$, every cube is $\equiv0$ or $\pm1$, i.e.\ $a^3\equiv0,1$ or $6\pmod7$. $\blacksquare$''',
'Remainders and congruences|Perfect cubes',2)
b.add(1746203,3,r'''Prove that for every integer $a$, $a^4\equiv0$ or $1\pmod5$.''',
r'''If $5\mid a$, then $a^4\equiv0$. Otherwise $a\equiv\pm1$ or $\pm2\pmod5$, so $a^2\equiv1$ or $4\equiv-1$, and $a^4=(a^2)^2\equiv1\pmod5$. (This is also Fermat's little theorem for $p=5$.) $\blacksquare$''',
'Remainders and congruences|Fermat\'s little theorem',2)
b.add(1746203,4,r'''Prove that if the integer $a$ is divisible by neither $2$ nor $3$, then $a^2\equiv1\pmod{24}$.''',
r'''Since $a$ is odd, $a^2\equiv1\pmod8$ (write $a=2k+1$; then $a^2-1=4k(k+1)$ and $k(k+1)$ is even). Since $3\nmid a$, $a\equiv\pm1\pmod3$ and $a^2\equiv1\pmod3$. So $8\mid a^2-1$ and $3\mid a^2-1$, and as $\gcd(3,8)=1$, $24\mid a^2-1$. $\blacksquare$''',
'Remainders and congruences|Divisibility|Parity',2)

# ---------------- 1746596 consecutive
b.add(1746596,1,r'''If $a,b,c,d$ are consecutive integers (in increasing order), prove that $bc-ad=2$.''',
r'''Write $a=n$, $b=n+1$, $c=n+2$, $d=n+3$. Then
\[
bc-ad=(n+1)(n+2)-n(n+3)=(n^2+3n+2)-(n^2+3n)=2 .
\]
So $bc-ad$ is always $\boxed{2}$. $\blacksquare$''',
'Algebraic expressions and identities|Algebraic manipulation',1,
note='The post asks why bc - ad is always 2; "consecutive" is taken in increasing order (in decreasing order the same identity holds by symmetry).')

# ---------------- 1745510 passcodes
b.add(1745510,1,r'''How many $5$-character passcodes are there if each character is a digit from $0$ to $9$ and no two consecutive characters are equal?''',
r'''The first character can be any of $10$ digits; each later character can be any digit except the one just before it, so $9$ choices each. The number of passcodes is $10\cdot9^4=\boxed{65610}$.''',
'Multiplication principle|Arrangements with restrictions',2)

b.save()
