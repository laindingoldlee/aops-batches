from qb import *
b=Bank('p225_03')

# ---------------- 1764035 MATHCOUNTS 2010 Nat Sprint 26
b.add(1764035,1,r'''Four standard six-sided dice are rolled. If the product of their values turns out to be an even number, what is the probability that their sum is odd? Express your answer as a common fraction.''',
r'''Only the parity of each die matters, and each die is odd or even with probability $\dfrac12$ independently, so the $16$ parity patterns are equally likely.

The product is odd only when all four dice are odd ($1$ pattern), so it is even in $15$ patterns. The sum is odd when the number of odd dice is odd, i.e.\ $1$ or $3$ odd dice: $\dbinom41+\dbinom43=8$ patterns, all of which have at least one even die, so an even product. Hence
\[
P(\text{sum odd}\mid\text{product even})=\boxed{\dfrac{8}{15}}.
\]''',
'Conditional probability|Parity|Dice probability|Probability with dice',3,source=src('MATHCOUNTS',2010,'National',26,rnd='Sprint'))

# ---------------- 1763996 Kangaroo squirrels
b.add(1763996,1,r'''Four squirrels ate $1999$ nuts altogether, and each ate at least $100$ nuts. The first squirrel ate more nuts than any other squirrel. The second and third squirrels together ate $1265$ nuts. How many nuts did the first squirrel eat?''',
r'''The first and fourth squirrels together ate $1999-1265=734$ nuts, and the fourth ate at least $100$, so the first ate at most $634$.

One of the second and third ate at least half of $1265$, i.e.\ at least $633$ (as $1265$ is odd). The first ate more than that, so at least $634$.

Hence the first squirrel ate $\boxed{634}$ nuts (with $633$ and $632$ for the second and third in some order, and $100$ for the fourth).''',
'Bounding and extremal cases|Logical deduction|Inequalities',3,source=src('Math Kangaroo',1999,'Level 5-6',23))

# ---------------- 1763749 donuts
b.add(1763749,1,r'''Bill is sent to a donut shop to buy exactly six donuts. The shop has four kinds of donuts, and Bill must get at least one of each kind. How many combinations will satisfy the order? Also explain why the count $4\cdot3\cdot2\cdot1\cdot4\cdot4$ (``one of each kind in some order, then any two'') is wrong.''',
r'''Donuts of the same kind are identical, so a combination is determined by how many of each kind Bill buys. Taking one of each kind first, he must choose the remaining $2$ donuts from $4$ kinds with repetition: either $2$ of the same kind ($4$ ways) or $2$ different kinds ($\dbinom42=6$ ways). So there are $4+6=\boxed{10}$ combinations. (By stars and bars: $\dbinom{2+3}{3}=10$.)

The product $4\cdot3\cdot2\cdot1\cdot4\cdot4=384$ counts ordered sequences, not combinations. The factor $4!$ orders the four required donuts, which does not change the purchase; the two extra donuts are also counted in both orders; and the same purchase is counted many times over depending on which donut of a doubled kind is called the ``required'' one.''',
'Stars and bars|Distributions and integer solutions|Combinations',2,source=src('MATHCOUNTS',None,'State',2,rnd='Target'),
note='MATHCOUNTS State Target #2 (year not given). The record also asks for the error in the poster\'s product.')

# ---------------- 1763617 guessing game
b.add(1763617,1,r'''Kevin picks a positive integer less than $1000$. Alex tries to find it by asking questions that Kevin answers with yes or no; each question must be either ``Is the number at most $a$?'' or ``Is the number at least $a$?'', where Alex chooses $a$ each time. What is the minimum number of questions that guarantees Alex can determine Kevin's number?''',
r'''\textbf{Lower bound.} There are $999$ possible numbers. After $k$ yes/no questions there are at most $2^k$ different answer patterns, and Alex can only be sure of the number if different numbers give different patterns. Since $2^9=512<999$, nine questions are not enough.

\textbf{Ten questions suffice.} At every stage the numbers still possible form a block of consecutive integers (each answer cuts the block at $a$). Asking ``Is the number at most $a$?'' with $a$ in the middle of the block leaves at most half of it, rounded up. Starting from $999\le1024=2^{10}$ numbers, after ten questions at most $1$ number remains.

So the minimum is $\boxed{10}$.''',
'Powers of two|Bounding and extremal cases|Games and strategies',3)

# ---------------- 1763563 binary operations
b.add(1763563,1,r'''The binary operation $\heartsuit$ is defined on the real numbers by $a\heartsuit b=ab^2$. Define $a\diamondsuit b=a\left((b^2+3)\heartsuit(3b^2+4)\right)$. For what nonnegative value of $x$ is the function $\dfrac{2018\diamondsuit x}{x^2+3}$ minimized?

$\textbf{(A)}\ -\dfrac{4}{3}\qquad\textbf{(B)}\ -\dfrac{2\sqrt3}{3}\qquad\textbf{(C)}\ 0\qquad\textbf{(D)}\ \dfrac{2\sqrt3}{3}\qquad\textbf{(E)}\ \text{this function cannot be minimized}$''',
r'''By the definitions, $(x^2+3)\heartsuit(3x^2+4)=(x^2+3)(3x^2+4)^2$, so
\[
\dfrac{2018\diamondsuit x}{x^2+3}=\dfrac{2018(x^2+3)(3x^2+4)^2}{x^2+3}=2018(3x^2+4)^2 .
\]
For $x\ge0$, $3x^2+4$ is smallest (and positive) at $x=0$, so the function is minimized at $x=0$, with value $2018\cdot16$. The answer is $\boxed{\textbf{(C)}\ 0}$.''',
'Custom operations|Maxima and minima|Functions',2)

# ---------------- 1763615 |x-10|+|y-5|<=100
fig=r'''import graph;
pair Cc=(10,5);
pair P1=(110,5),P2=(10,105),P3=(-90,5),P4=(10,-95);
fill(P1--P2--P3--P4--cycle,paleblue);draw(P1--P2--P3--P4--cycle,blue+linewidth(0.9));
draw((-110,0)--(130,0),Arrow);draw((0,-110)--(0,125),Arrow);
label("$x$",(130,0),S);label("$y$",(0,125),W);
draw(P3--P1,dashed);draw(P4--P2,dashed);dot(Cc);
label("$(10,5)$",Cc,dir(-45));
label("$(110,5)$",P1,dir(20));label("$(10,105)$",P2,E);label("$(-90,5)$",P3,dir(160));label("$(10,-95)$",P4,E);'''
b.add(1763615,1,r'''What is the area of the region of points $(x,y)$ in the coordinate plane with $|x-10|+|y-5|\le100$?''',
r'''Put $u=x-10$, $v=y-5$; this translation does not change areas, and the region becomes $|u|+|v|\le100$. In each quadrant this is a right triangle with legs $100$, for instance $u,v\ge0$, $u+v\le100$. So the region is a square (a ``diamond'') centred at $(10,5)$ with vertices $(110,5)$, $(10,105)$, $(-90,5)$, $(10,-95)$.
'''+asy(fig,'6cm')+r'''
Its diagonals have length $200$, so its area is $\dfrac12\cdot200\cdot200=\boxed{20000}$.''',
'Absolute value|Coordinate geometry|Squares|Lengths, perimeter, and area|Translations',2)

# ---------------- 1763579 isosceles not equilateral, sides <= 10
b.add(1763579,1,r'''The number of isosceles but not equilateral triangles with integer sides, no side exceeding $10$, is

(1) $65$\qquad (2) $75$\qquad (3) $81$\qquad (4) $90$''',
r'''Such a triangle has two equal sides $a$ and a different third side $b$, with $1\le a,b\le10$ and $b\ne a$; the triangle inequality requires only $b<2a$ (the other inequality $a<a+b$ is automatic). For each $a$ count the $b$:
\begin{itemize}
\item $a=1$: $b<2$, $b\ne1$: none;
\item $a=2,3,4,5$: $b=1,\dots,2a-1$ except $a$: $2,4,6,8$ choices;
\item $a=6,\dots,10$: $b=1,\dots,10$ except $a$: $9$ choices each.
\end{itemize}
Different pairs $(a,b)$ give different triangles. The total is $2+4+6+8+5\cdot9=\boxed{65}$, choice (1).''',
'Isosceles triangles|Triangle inequality|Casework|Systematic counting',3)

# ---------------- 1763629 X+Y+Z=10 with lower bounds
b.add(1763629,1,r'''Integers $X$, $Y$, $Z$ satisfy $X+Y+Z=10$ with $X\ge0$, $Y\ge-1$ and $Z\ge-1$. How many solutions $(X,Y,Z)$ are there?''',
r'''Shift the variables so that all lower bounds are $0$: with $Y'=Y+1\ge0$ and $Z'=Z+1\ge0$ the equation becomes $X+Y'+Z'=12$ in nonnegative integers. By stars and bars ($12$ stars and $2$ bars) the number of solutions is
\[
\dbinom{14}{2}=\boxed{91}.
\]''',
'Stars and bars|Distributions and integer solutions|Substitution',2,
note='The poster asks for a method other than listing; the shift-and-stars-and-bars method is given.')

# ---------------- 1763630 die then coins, even heads
b.add(1763630,1,r'''Bill rolls a fair standard six-sided die once and gets $n$. Then he flips $n$ fair coins. What is the probability that an even number of them land heads? (Zero heads counts as even.)''',
r'''Fix $n\ge1$. Whatever the first $n-1$ coins show, exactly one of the two outcomes of the last coin makes the total number of heads even. So for each $n\in\{1,\dots,6\}$ the probability of an even number of heads is exactly $\dfrac12$, and therefore the overall probability is $\boxed{\dfrac12}$.''',
'Probability|Parity|Conditional probability',2)

# ---------------- 1763616 divisors of 10^99
b.add(1763616,1,r'''How many positive factors does the least positive integer with $100$ digits have?''',
r'''The least $100$-digit positive integer is $10^{99}=2^{99}\cdot5^{99}$. Its number of positive factors is $(99+1)(99+1)=\boxed{10000}$.''',
'Divisor counting|Prime factorisation|Place value',2)

# ---------------- 1763566 coin game; Heron rational
b.add(1763566,1,r'''Albert, Bertha and Carlos play rounds of a game with a fair coin. In a round the players flip in a fixed order, cycling through the three players, and the round stops as soon as someone flips heads; that player wins the round. In the first round the order is Albert, Bertha, Carlos. In each later round, the winner of the previous round goes last and the other two keep their relative order. (For example, if Albert wins the first round, the second round goes Bertha, Carlos, Albert; if Bertha then wins, the third round goes Carlos, Albert, Bertha.)
\begin{enumerate}
\item[(a)] Find the probability that Albert wins the third round.
\item[(b)] Let $p_n$ be the probability that Albert wins round $n$. Prove that $\left|p_{2018}-\dfrac13\right|<10^{-300}$.
\end{enumerate}''',
r'''\textbf{One round.} The players in first, second and third place win with probabilities
\[
\dfrac12\left(1+\dfrac18+\dfrac1{64}+\cdots\right)=\dfrac47,\qquad\dfrac27,\qquad\dfrac17 .
\]
\textbf{Albert's place.} Let $a_n,b_n,c_n$ be the probabilities that Albert is first, second, third in round $n$. If Albert wins he is third next time. If he is first and loses, he stays first; if he is second, he becomes first when the first player wins and stays second when the third wins; if he is third and loses, he becomes second. So
\[
a_{n+1}=\dfrac37a_n+\dfrac47b_n,\qquad b_{n+1}=\dfrac17b_n+\dfrac67c_n,\qquad c_{n+1}=\dfrac47a_n+\dfrac27b_n+\dfrac17c_n ,
\]
and $p_n=\dfrac47a_n+\dfrac27b_n+\dfrac17c_n=c_{n+1}$ (Albert is last in round $n+1$ exactly when he won round $n$).

(a) Start: $(a_1,b_1,c_1)=(1,0,0)$. Then $(a_2,b_2,c_2)=\left(\dfrac37,0,\dfrac47\right)$ and $(a_3,b_3,c_3)=\left(\dfrac{9}{49},\dfrac{24}{49},\dfrac{16}{49}\right)$, so
\[
p_3=\dfrac47\cdot\dfrac9{49}+\dfrac27\cdot\dfrac{24}{49}+\dfrac17\cdot\dfrac{16}{49}=\dfrac{36+48+16}{343}=\boxed{\dfrac{100}{343}}.
\]
(b) Using $a_n=1-b_n-c_n$, put $\beta_n=b_n-\dfrac13$ and $\gamma_n=c_n-\dfrac13$. The equations become
\[
\beta_{n+1}=\dfrac17\beta_n+\dfrac67\gamma_n,\qquad \gamma_{n+1}=-\dfrac27\beta_n-\dfrac37\gamma_n .
\]
Eliminating $\beta$ gives $\gamma_{n+2}=-\dfrac27\gamma_{n+1}-\dfrac{9}{49}\gamma_n$. Hence $q_n=p_n-\dfrac13=\gamma_{n+1}$ satisfies
\[
q_{n+2}=-\dfrac27q_{n+1}-\dfrac9{49}q_n,\qquad q_1=\dfrac47-\dfrac13=\dfrac5{21},\quad q_2=\dfrac{16}{49}-\dfrac13=-\dfrac1{147}.
\]
Let $M_n=\max(|q_n|,|q_{n+1}|)$. Then $|q_{n+2}|\le\left(\dfrac27+\dfrac9{49}\right)M_n=\dfrac{23}{49}M_n$, so $M_{n+1}\le M_n$ and $M_{n+2}\le\dfrac{23}{49}M_n$. Therefore
\[
\left|p_{2018}-\dfrac13\right|=|q_{2018}|\le M_{2017}\le\left(\dfrac{23}{49}\right)^{1008}M_1<\left(\dfrac{23}{49}\right)^{1008}<10^{-300},
\]
since $M_1=\dfrac5{21}<1$ and $\left(\dfrac{23}{49}\right)^{3}=\dfrac{12167}{117649}<\dfrac1{9.6}$, so $\left(\dfrac{23}{49}\right)^{1008}<9.6^{-336}<10^{-300}$. $\blacksquare$''',
'Probability|Recurrence relations|Recursive probability|Geometric sequences|Bounding and extremal cases',6,
note='The post asks for the probability that Albert wins round 2018. The exact value is a fraction with denominator 7^2018 and no useful closed form (it is 1/3 + s/(3*7^2018) with s from a linear recurrence), so the record asks for the third round (100/343) and to prove that the 2018th-round probability is within 10^-300 of 1/3. Both checked by exact computation.')

fig=r'''import graph;
pair P1=(1,1),P2=(6,2),P3=(2.5,5);
draw((-0.5,0)--(7.5,0),Arrow);draw((0,-0.5)--(0,6),Arrow);
label("$x$",(7.5,0),S);label("$y$",(0,6),W);
draw(P1--P2--P3--cycle,linewidth(0.9));dot(P1);dot(P2);dot(P3);
label("$(a,b)$",P1,SW);label("$(c,d)$",P2,E);label("$(e,f)$",P3,N);'''
b.add(1763566,2,r'''Let
\[
g=\dfrac{\sqrt{(b-d)^2+(a-c)^2}+\sqrt{(b-f)^2+(a-e)^2}+\sqrt{(d-f)^2+(c-e)^2}}{2},
\]
where $a,b,c,d,e,f$ are rational numbers. Show that
\[
\sqrt{g\left(g-\sqrt{(b-d)^2+(a-c)^2}\right)\left(g-\sqrt{(b-f)^2+(a-e)^2}\right)\left(g-\sqrt{(d-f)^2+(c-e)^2}\right)}
\]
is always rational.''',
r'''The three square roots are the distances between the points $P=(a,b)$, $Q=(c,d)$, $R=(e,f)$, and $g$ is half their sum.
'''+asy(fig,'5cm')+r'''
If $P,Q,R$ form a triangle, $g$ is its semiperimeter and the expression is, by Heron's formula, its area $K$. By the shoelace formula
\[
K=\dfrac12\left|a(d-f)+c(f-b)+e(b-d)\right| ,
\]
which is rational since $a,\dots,f$ are.

If the points are collinear (or two coincide), the largest distance is the sum of the other two, so $g$ equals the largest distance and one factor is $0$; the expression is $0$, again rational (and the shoelace value is also $0$). In every case the expression is rational. $\blacksquare$''',
"Heron's formula|Shoelace formula|Distance formula|Coordinate geometry|Radicals",4,
note='Posed as in the post; the solution recognises Heron\'s formula for the triangle with the three given points as vertices.')

# ---------------- 1763571 units digit; system
b.add(1763571,1,r'''Find the units digit of $\displaystyle\sum_{k=5}^{2018}\left(1+3\cdot2^{2k-5}\right)$.''',
r'''The exponent $2k-5$ is odd. The units digit of $2^m$ for odd $m$ is $2$ if $m\equiv1\pmod4$ and $8$ if $m\equiv3\pmod4$; as $k$ increases by $1$, $2k-5$ increases by $2$, so these alternate, starting with $2^5$ (units digit $2$) at $k=5$. The terms $1+3\cdot2^{2k-5}$ therefore have units digits $1+6=7$ and $1+24\to5$ alternately. There are $2018-5+1=2014$ terms, i.e.\ $1007$ pairs, each contributing $7+5=12$. The units digit of the sum is that of $1007\cdot12=12084$, namely $\boxed{4}$.''',
'Units digits and last digits|Powers of two|Summation|Remainders and congruences',3)
b.add(1763571,2,r'''Positive integers $a$, $b$, $c$ satisfy
\[
a^2+b+c=112,\qquad a+b^2+c=130,\qquad a+b+c^2=460 .
\]
Find $a+b+c$.''',
r'''Subtracting the first equation from the second,
\[
(b^2-b)-(a^2-a)=18\ \Longrightarrow\ (b-a)(a+b-1)=18 .
\]
Here $a+b-1\ge1$, so $b-a\ge1$, and $b-a$ and $a+b-1$ have opposite parity (their sum $2b-1$ is odd). The factorisations $18=1\cdot18=2\cdot9$ give $(a,b)=(9,10)$ or $(4,6)$; the factorisations $3\cdot6$, $6\cdot3$, $9\cdot2$, $18\cdot1$ give $(2,5)$ or no positive solution. The first equation then gives $c=112-a^2-b$: $c=21$, $90$ or $103$ respectively. Only the first satisfies the third equation: $9+10+21^2=460$, and also $9+100+21=130$. So $(a,b,c)=(9,10,21)$ and $a+b+c=\boxed{40}$.''',
'Equations and systems of equations|Factoring|Diophantine equations',4,
note='"Find the sum of the values of a, b and c" is ambiguous for real solutions (the system has several); the record takes positive integers, for which the solution (9, 10, 21) is unique.')

# ---------------- 1763561 circles in perpendicular planes; bananas
fig=r'''pair O1=(0,2.6);
real c=Cos(30),sn=Sin(30);
pair O2=O1+(-c,sn),T1=O1+2*(-c,sn),O3=O1+(0,3),T2=O1+(0,2);
pair H=O1+(2.6/sn)*(c,-sn);
draw((-3.6,0)--(5.2,0),linewidth(0.8));label("$\ell$",(5.2,0),E);
draw(circle(O1,2),linewidth(0.9));draw(circle(O2,1),blue);draw(circle(O3,1),red);
draw(T1--H,dashed);draw(O1--T2,dashed);
draw(O2--O3,heavygreen+linewidth(1));
draw(arc(H,0.7,150,180));label("$30^\circ$",H+1.1*dir(165));
dot(O1);dot(O2);dot(O3);dot(T1);dot(T2);
label("$O_1$",O1,dir(-30));label("$O_2$",O2,dir(-60));label("$O_3$",O3,E);label("$T_1$",T1,W);label("$T_2$",T2,dir(-30));
label("$\sqrt7$",(O2+O3)/2,NW,heavygreen);'''
b.add(1763561,1,r'''Planes $\mathbf{P}_1$ and $\mathbf{P}_2$ are perpendicular and meet along the line $\ell$. Circle $\omega_1$ with radius $2$ and centre $O_1$ lies in $\mathbf{P}_1$. Unit circle $\omega_2$, centred at $O_2\in\mathbf{P}_1$, is internally tangent to $\omega_1$ at $T_1$, where the ray $\overrightarrow{T_1O_1}$ meets $\ell$ at an acute angle of $30^\circ$. Unit circle $\omega_3$, centred at $O_3\in\mathbf{P}_1$, is externally tangent to $\omega_1$ at $T_2$, where the ray $\overrightarrow{T_2O_1}$ is perpendicular to $\ell$. The minimum possible length of $\overline{O_2O_3}$ is $\sqrt m$ for a positive integer $m$. Compute $m$.''',
r'''Everything happens in the plane $\mathbf{P}_1$, which contains $\ell$; the plane $\mathbf{P}_2$ plays no role. Tangency puts the centres on the radii: $O_2$ is the midpoint of $O_1T_1$, so $O_1O_2=1$ in the direction of $T_1$, and $O_3$ lies beyond $T_2$ on ray $O_1T_2$ with $O_1O_3=3$.

The direction $\overrightarrow{T_1O_1}$ makes $30^\circ$ with $\ell$, so the direction $\overrightarrow{O_1O_2}$ also makes $30^\circ$ with $\ell$ (it is the opposite direction), and $\overrightarrow{O_1O_3}$ is perpendicular to $\ell$. Hence the angle $\theta=\angle O_2O_1O_3$ is $90^\circ-30^\circ=60^\circ$ or $90^\circ+30^\circ=120^\circ$, depending on which side of $\ell$ the point $O_3$ is taken. By the law of cosines,
\[
O_2O_3^2=1^2+3^2-2\cdot1\cdot3\cos\theta=10-6\cos\theta ,
\]
which is $7$ for $\theta=60^\circ$ and $13$ for $\theta=120^\circ$. The configuration with $\theta=60^\circ$ is shown:
'''+asy(fig,'6cm')+r'''
The minimum is $\sqrt7$, so $m=\boxed{7}$.''',
'Tangent circles|Circles|Law of cosines|Angles and lines',3,
note='The three-dimensional setting is irrelevant (all centres and the line l lie in plane P1); the record keeps the wording.')
b.add(1763561,2,r'''I want to eat $100$ bananas, and my brother Walt is willing to help. I eat $3$ bananas per minute and Walt eats $5$ bananas per minute. I start alone and eat for $15$ minutes; then Walt joins me and we eat together until all $100$ bananas are gone. How many bananas does Walt eat?''',
r'''In the first $15$ minutes I eat $45$ bananas, leaving $55$. Together we eat $8$ bananas per minute, so the rest takes $\dfrac{55}{8}$ minutes, during which Walt eats
\[
5\cdot\dfrac{55}{8}=\boxed{\dfrac{275}{8}}=34\dfrac38
\]
bananas (bananas are treated as divisible; I eat the other $\dfrac{165}{8}$ in that time).''',
'Work and rates|Rates|Fractions',2,
note='The answer is not a whole number; bananas are treated as divisible, as the rates imply.')

# ---------------- 1763513 x^3-2x-2 one real root
b.add(1763513,1,r'''Prove that $f(x)=x^3-2x-2$ has exactly one real zero. (A student applies Descartes' rule of signs: $f(x)$ has one sign change, so one positive zero; $f(-x)=-x^3+2x-2$ has two sign changes, ``so two negative zeros''. What is wrong?)''',
r'''\textbf{No negative zeros.} For $x<0$ write $f(x)=x(x^2-2)-2$.
\begin{itemize}
\item If $x\le-\sqrt2$, then $x<0$ and $x^2-2\ge0$, so $x(x^2-2)\le0$ and $f(x)\le-2<0$.
\item If $-\sqrt2<x<0$, then $g(x)=x(x^2-2)=x^3-2x$ has $g'(x)=3x^2-2$, so on this interval $g$ is largest at $x=-\sqrt{\dfrac23}$, where $g=-\sqrt{\dfrac23}\left(\dfrac23-2\right)=\dfrac43\sqrt{\dfrac23}<\dfrac43<2$. So $f(x)<0$.
\end{itemize}
Also $f(0)=-2\ne0$.

\textbf{Exactly one positive zero.} $f(1)=-3<0<f(2)=2$, so there is a zero between $1$ and $2$. For $x\ge\sqrt{\dfrac23}$, $f'(x)=3x^2-2\ge0$, so $f$ is increasing there, and for $0<x<\sqrt{\dfrac23}$ we have $f(x)=x^3-2x-2<x^3-2<0$. So there is only one positive zero. Hence $f$ has $\boxed{\text{exactly one real zero}}$ (about $1.769$). $\blacksquare$

The student misreads Descartes' rule: the number of negative zeros equals the number of sign changes of $f(-x)$ \emph{or is less than it by an even number}. Two sign changes allow $2$ or $0$ negative zeros, and the argument above shows it is $0$.''',
'Polynomial roots|Polynomials|Calculus|Inequalities',4,
note='The post asks why Descartes\' rule seems to predict two negative zeros; the record asks for a proof of exactly one real zero and the error.')

# ---------------- 1763250 units digits fun (6 parts)
UT=r'''Let $u(n)$ be the units digit of a positive integer $n$, and let $t(n)$ be its tens digit if $n\ge10$ and $0$ otherwise.'''
A2=r'''u\left(2019^{u(u(2019)^{u(2019^{2019 u(2019)})}) \times u(u(2019^{2018})^{2019})}\right)'''
A3=r'''t\left(2019^{u(t(2019^{2019}) \times 2019^{t(u(2019^{2018})})}\right)'''
A4=r'''u\left(2019^{2019^{'''+A3+r'''}}+'''+A2+r'''\right)'''
b.add(1763250,1,r'''Find the units digit of $1^2+2^3+3^4+4^5+\cdots+2019^{2020}$.''',
r'''The units digit of $n^{m}$ ($m\ge1$) depends only on the units digit of $n$ and on $m$ modulo $4$. For the term $n^{n+1}$ both are determined by $n$ modulo $20$, so the units digits of the terms repeat with period $20$. For $n=1,\dots,20$ they are
\[
1,8,1,4,5,6,1,8,1,0,\ 1,2,9,4,5,6,9,2,1,0,
\]
with sum $74$. The terms $n=1$ to $2000$ form $100$ periods, contributing $7400$, which ends in $0$; the terms $n=2001$ to $2019$ repeat the first $19$ entries, whose sum is $74$. So the units digit of the sum is $\boxed{4}$.''',
'Units digits and last digits|Remainders and congruences|Pattern recognition|Summation',4)
b.add(1763250,2,UT+r''' What is $\displaystyle '''+A2+r'''$?''',
r'''Work from the inside out, using that $9^{\text{odd}}$ ends in $9$ and $9^{\text{even}}$ ends in $1$; $2019$ ends in $9$, so $u(2019)=9$.
\begin{itemize}
\item $2019\,u(2019)=18171$ is odd, so $u\left(2019^{18171}\right)=9$, and $u\left(9^9\right)=9$.
\item $u\left(2019^{2018}\right)=1$, so $u\left(1^{2019}\right)=1$.
\end{itemize}
The exponent is $9\times1=9$, and $u\left(2019^9\right)=\boxed{9}$.''',
'Units digits and last digits|Exponents|Parity',2)
b.add(1763250,3,UT+r''' What is $\displaystyle '''+A3+r'''$?''',
r'''We need $2019^{m}$ modulo $100$, i.e.\ $19^m\bmod100$. Now $19^2=361\equiv61$, $19^4\equiv61^2\equiv21$, $19^5\equiv21\cdot19=399\equiv99\equiv-1$, so $19^{10}\equiv1\pmod{100}$.
\begin{itemize}
\item $2019^{2019}\equiv19^{9}\equiv19^{-1}\equiv79\pmod{100}$ (as $19\cdot79=1501$). So $t\left(2019^{2019}\right)=7$ and $u(7)=7$.
\item $u\left(2019^{2018}\right)=1$, $t(1)=0$, and $2019^0=1$.
\end{itemize}
The exponent is $7\times1=7$, and $2019^7\equiv19^7\equiv19^5\cdot19^2\equiv-61\equiv39\pmod{100}$. The tens digit is $\boxed{3}$.''',
'Units digits and last digits|Modular exponentiation|Remainders and congruences',3)
b.add(1763250,4,UT+r''' What is $\displaystyle '''+A4+r'''$?''',
r'''The exponent tower uses
\[
'''+A3+r'''=3
\]
(since $t(2019^{2019})=7$ because $2019^{2019}\equiv79\pmod{100}$, $t(u(2019^{2018}))=t(1)=0$, and $2019^7\equiv39\pmod{100}$), and
\[
'''+A2+r'''=9
\]
(the exponent is $u(9^9)\cdot u(1^{2019})=9\cdot1$, and $2019^9$ ends in $9$). So the expression is $u\left(2019^{2019^3}+9\right)$. The exponent $2019^3$ is odd, so $2019^{2019^3}$ ends in $9$, and $9+9=18$. The answer is $\boxed{8}$.''',
'Units digits and last digits|Modular exponentiation|Parity',3)
b.add(1763250,5,r'''Let $u(n)$ be the units digit of a positive integer $n$. Define a sequence by $k_1=2019$ and $k_i=u\left(2019^{k_{i-1}}\right)$ for $i>1$. What is $u\left(2019^{k_1+k_2+\cdots+k_{2019}}\right)$?''',
r'''A power of $2019$ ends in $9$ if the exponent is odd and in $1$ if it is even. Since $k_1=2019$ is odd, $k_2=9$; then $k_3=u(2019^9)=9$, and so on: $k_i=9$ for all $i\ge2$. The exponent is
\[
2019+2018\cdot9=20181,
\]
which is odd, so $u\left(2019^{20181}\right)=\boxed{9}$.''',
'Units digits and last digits|Recurrence relations|Parity',2)
b.add(1763250,6,UT+r''' Let
\[
X='''+A3+r''',\qquad Y='''+A2+r''',
\]
\[
Z='''+A4+r'''.
\]
What is $u\left(X^{Y^{Z}}\right)$?''',
r'''From the computations of these numbers: $X=3$ (because $2019^{2019}\equiv79\pmod{100}$ makes the exponent $u(7)\cdot2019^{t(1)}=7$, and $2019^7\equiv39\pmod{100}$); $Y=9$ (the exponent is $u(9^9)\cdot u(1^{2019})=9$, and $2019^9$ ends in $9$); and $Z=u\left(2019^{2019^3}+9\right)=u(9+9)=8$.

So we need the units digit of $3^{9^8}$. Powers of $3$ end in $3,9,7,1$ with period $4$, and $9^8\equiv1^8=1\pmod4$. Hence $u\left(3^{9^8}\right)=u(3^1)=\boxed{3}$.''',
'Units digits and last digits|Modular exponentiation|Remainders and congruences',3)

# ---------------- 1763183 system of powers and logs
b.add(1763183,1,r'''Solve the following system in positive real numbers $x,y$ with $y\ne1$:
\[
y^{y^3}=x^{x^y},\qquad y^{y^y}=y^{\dfrac{x^{y+1}}{2}},\qquad y^{\log_y\left(\left(y^y\right)^{\log_y x}\right)}=\dfrac{\sqrt[y^{-1}]{x^2}}{2}.
\]''',
r'''\textbf{Third equation.} The left side is $\left(y^y\right)^{\log_yx}=\left(y^{\log_yx}\right)^y=x^y$. The $y^{-1}$-th root of $x^2$ is $\left(x^2\right)^{y}=x^{2y}$. So $x^y=\dfrac{x^{2y}}{2}$, and as $x^y>0$, $x^y=2$.

\textbf{Second equation.} Since $y>0$, $y\ne1$, the map $t\mapsto y^t$ is one-to-one, so $y^y=\dfrac{x^{y+1}}{2}=\dfrac{x\cdot x^y}{2}=x$.

\textbf{First equation.} $x^{x^y}=x^2=\left(y^y\right)^2=y^{2y}$, so $y^{y^3}=y^{2y}$ and $y^3=2y$, i.e.\ $y^2=2$, $y=\sqrt2$. Then $x=y^y=\sqrt2^{\sqrt2}$.

\textbf{Check.} $x^y=\left(\sqrt2^{\sqrt2}\right)^{\sqrt2}=\sqrt2^{\,2}=2$; the second equation holds as $y^y=x$; and the first holds as $y^{y^3}=y^{2\sqrt2}=y^{2y}=x^2=x^{x^y}$. The solution is
\[
\boxed{x=\sqrt2^{\sqrt2},\quad y=\sqrt2}.
\]''',
'Exponents|Logarithms|Equations and systems of equations|Substitution',4,
note='The conditions x, y > 0 and y not equal to 1 (needed for log base y) are stated explicitly.')

# ---------------- 1762366 Handbook 148, 149
fig=r'''import graph;
pair W=(2,1),X=(6,3),Y=(4,7),Z=(0,5),M=(3,4);
draw((-0.8,0)--(7.2,0),Arrow);draw((0,-0.5)--(0,8),Arrow);
label("$x$",(7.2,0),S);label("$y$",(0,8),W);
draw(W--X--Y--Z--cycle,linewidth(0.9));draw(W--Y,dashed);draw(X--Z,dashed);
dot(W);dot(X);dot(Y);dot(Z);dot(M);
label("$W(2,1)$",W,S);label("$X(6,3)$",X,E);label("$Y(4,7)$",Y,N);label("$Z(0,5)$",Z,W);label("$(3,4)$",M,dir(-20));'''
b.add(1762366,148,r'''Square $WXYZ$ has vertices $W(2,1)$, $X(a,b)$, $Y(4,7)$ and $Z(c,d)$, in this order. What is the value of $|ab-cd|$?''',
r'''In the order $W,X,Y,Z$, the vertices $W$ and $Y$ are opposite, so $WY$ is a diagonal. (They need not be adjacent, which is why ``$W$ and $Y$ do not form a side'' is no obstacle.) The centre is the midpoint $M=(3,4)$, and $\overrightarrow{MW}=(-1,-3)$. The other two vertices are obtained by rotating this vector through $\pm90^\circ$: $(3,-1)$ and $(-3,1)$. So $X$ and $Z$ are $(6,3)$ and $(0,5)$ in some order.
'''+asy(fig,'5cm')+r'''
Either way $|ab-cd|=|6\cdot3-0\cdot5|=\boxed{18}$.''',
'Squares|Coordinate geometry|Rotations|Midpoints',3,source=src('MATHCOUNTS Handbook',None,None,148),
note='The poster thought the vertices could not form a square (W and Y are opposite vertices, not adjacent) and got 10; the answer is 18.')
b.add(1762366,149,r'''Ten guppies in Vida's tank are $5,5,8,8,8,9,10,11,11$ and $33$ weeks old. A guppy of age $n$ weeks is added to her tank. The sum of the mean, the median and the unique mode of the eleven guppies' ages equals their range. What is the sum of all possible integer values of $n$?''',
r'''The ten ages have sum $108$. After adding $n$:
\begin{itemize}
\item \textbf{Mode.} $8$ appears $3$ times; if $n=5$ or $n=11$ there would be a tie, so the mode is not unique. Otherwise the unique mode is $8$.
\item \textbf{Median} (the $6$th of $11$): $8$ if $n\le8$ and $9$ if $n\ge9$.
\item \textbf{Range:} $33-n$ if $n<5$, $28$ if $5\le n\le33$, and $n-5$ if $n>33$.
\end{itemize}
Now solve $\dfrac{108+n}{11}+\text{median}+8=\text{range}$ in each case:
\begin{itemize}
\item $n<5$: $\dfrac{108+n}{11}+16=33-n$ gives $12n=79$, not an integer.
\item $5\le n\le8$ ($n\ne5$): $\dfrac{108+n}{11}+16=28$ gives $n=24$, outside the range.
\item $9\le n\le33$ ($n\ne11$): $\dfrac{108+n}{11}+17=28$ gives $n=13$. Valid.
\item $n>33$: $\dfrac{108+n}{11}+17=n-5$ gives $10n=350$, $n=35$. Valid.
\end{itemize}
Check: for $n=13$, mean $11$, median $9$, mode $8$, sum $28$ = range $28$; for $n=35$, mean $13$, median $9$, mode $8$, sum $30$ = range $30$. The sum of the possible values is $13+35=\boxed{48}$.''',
'Mean|Median|Mode|Range|Casework',4,source=src('MATHCOUNTS Handbook',None,None,149),
note='The poster found only n = 24 (which fails, since n = 24 gives median 9); the values are 13 and 35.')

# ---------------- 1763339 number of terms
b.add(1763339,1,r'''How many terms are there in the expansion of $(a+b+c+d+e)^{19}$ after like terms are combined? Give also the number of terms of $(x_1+x_2+\cdots+x_n)^r$ in general.''',
r'''Every term is a monomial $a^{i}b^{j}c^{k}d^{l}e^{m}$ with nonnegative integer exponents and $i+j+k+l+m=19$, and each such monomial appears with a positive coefficient (a multinomial coefficient), so no terms cancel. By stars and bars the number of such exponent choices is
\[
\dbinom{19+4}{4}=\dbinom{23}{4}=\boxed{8855}.
\]
In general $(x_1+\cdots+x_n)^r$ has $\dbinom{r+n-1}{n-1}$ terms.''',
'Stars and bars|Distributions and integer solutions|Binomial theorem|Combinations',3)

# ---------------- 1762984 trains 9 and 16 hours
b.add(1762984,1,r'''Train $X$ starts from $A$ towards $B$, and at the same time train $Y$ starts from $B$ towards $A$, each at constant speed. After they meet, train $X$ reaches $B$ in $9$ hours and train $Y$ reaches $A$ in $16$ hours. Find the ratio of their speeds.''',
r'''Let the speeds be $x$ and $y$, and let them meet after $t$ hours at point $M$. Then $AM=xt$ and $MB=yt$. After meeting, $X$ covers $MB$ in $9$ hours and $Y$ covers $AM$ in $16$ hours:
\[
yt=9x,\qquad xt=16y .
\]
Dividing, $\dfrac{y}{x}=\dfrac{9x}{16y}$, so $\dfrac{x^2}{y^2}=\dfrac{16}{9}$ and $x:y=\boxed{4:3}$. (Then $t=12$ hours.)''',
'Distance, rate, and time|Ratios, proportions, and variation|Relative speed',3)

# ---------------- 1763216 prealgebra marathon P1
b.add(1763216,1,r'''Compute $972-72\cdot97$.''',
r'''Multiplication comes first: $72\cdot97=72\cdot100-72\cdot3=7200-216=6984$. Then $972-6984=\boxed{-6012}$.''',
'Order of operations|Whole-number operations',1)

# ---------------- 1762187 CMIMC angle BPC - BAC
fig=r'''pair B=(0,0),C=(7,0);
real Bb=70,Cg=50;
pair A=extension(B,B+dir(Bb),C,C+dir(180-Cg));
pair P=extension(B,B+dir(Bb-20),C,C+dir(180-Cg+15));
draw(A--B--C--cycle,linewidth(0.9));
draw(B--P--C,blue+linewidth(0.8));
draw(arc(B,1.2,Bb-20,Bb),red);label("$20^\circ$",B+1.75*dir(Bb-10),red);
draw(arc(C,1.6,180-Cg,180-Cg+15),red);label("$15^\circ$",C+2.2*dir(180-Cg+7.5),red);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$P$",P,S);'''
b.add(1762187,1,r'''Let $ABC$ be a triangle. Point $P$ lies in the interior of $ABC$ such that $\angle ABP=20^\circ$ and $\angle ACP=15^\circ$. Compute $\angle BPC-\angle BAC$.''',
r'''In triangle $BPC$, $\angle BPC=180^\circ-\angle PBC-\angle PCB$. Since $P$ is inside the triangle,
\[
\angle PBC=\angle ABC-20^\circ,\qquad \angle PCB=\angle ACB-15^\circ .
\]
'''+asy(fig,'6cm')+r'''
Hence
\[
\angle BPC=180^\circ-\angle ABC-\angle ACB+35^\circ=\angle BAC+35^\circ,
\]
using the angle sum of triangle $ABC$. So $\angle BPC-\angle BAC=\boxed{35^\circ}$, whatever the shape of the triangle.''',
'Angle chasing|Angle sums|Triangles',2,source=src('CMIMC',2018,None,None),
note='The post has angle ABP = 2 degrees, a typo for the contest\'s 20 degrees (answer 35); with 2 degrees the same argument gives 17.')

# ---------------- 1763003 guns and train
b.add(1763003,1,r'''Guns are fired from a city at intervals of $4$ minutes. A man travelling towards the city by train hears two successive shots $3$ minutes $50$ seconds apart. If the speed of sound is $1265$ ft/s, find the speed of the train.''',
r'''Between hearing the two shots the man travels for $230$ seconds at speed $v$, towards the city. The second shot is fired $240$ seconds after the first. The sound of the first shot reached him at distance $d$ from the city; the second reaches him at distance $d-230v$, so it takes $\dfrac{d-230v}{1265}$ seconds to arrive, compared with $\dfrac{d}{1265}$ for the first. Hence
\[
240+\dfrac{d-230v}{1265}=\dfrac{d}{1265}+230\ \Longrightarrow\ 230v=10\cdot1265\ \Longrightarrow\ v=55 .
\]
In words: in $230$ seconds the train covers the distance that sound covers in $10$ seconds. The speed is $\boxed{55\text{ ft/s}}$, which is $37.5$ miles per hour.''',
'Distance, rate, and time|Relative speed|Unit conversion',3)

# ---------------- 1763222 AMC 10A 2011 #25
b.add(1763222,1,r'''Let $R$ be a square region and $n\ge4$ an integer. A point $X$ in the interior of $R$ is called $n$-ray partitional if there are $n$ rays emanating from $X$ that divide $R$ into $n$ triangles of equal area. How many points are $100$-ray partitional but not $60$-ray partitional?

$\textbf{(A)}\ 1500\qquad\textbf{(B)}\ 1560\qquad\textbf{(C)}\ 2320\qquad\textbf{(D)}\ 2480\qquad\textbf{(E)}\ 2500$''',
r'''Let $R$ be the unit square $[0,1]^2$ and $X=(x,y)$ an interior point.

\textbf{The rays must go to the four corners.} Each of the $n$ regions is a triangle with a vertex at $X$; a region containing a corner of the square in the interior of its boundary arc would not be a triangle. So four of the rays go to the corners, and they split $R$ into four triangles on the sides with areas $\dfrac x2,\dfrac{1-x}{2},\dfrac y2,\dfrac{1-y}{2}$ (base $1$, height the distance from $X$ to that side).

\textbf{Counting.} The remaining rays split each of these four triangles into triangles with a common height, so each triangle on a side is cut into some number $m_i\ge1$ of pieces of area $\dfrac1n$. Hence $\dfrac x2=\dfrac{m_1}{n}$ and $\dfrac{1-x}{2}=\dfrac{m_2}{n}$, so $x=\dfrac{2m_1}{n}$, and similarly for $y$. Conversely, if $x$ and $y$ are multiples of $\dfrac2n$ strictly between $0$ and $1$, dividing each side into equal parts gives $n$ triangles of area $\dfrac1n$ (then $m_1+m_2+m_3+m_4=\dfrac n2+\dfrac n2=n$).

So the $100$-ray partitional points are those with $x,y\in\left\{\dfrac1{50},\dots,\dfrac{49}{50}\right\}$: $49^2=2401$ points. The $60$-ray partitional points have coordinates that are multiples of $\dfrac1{30}$. A number that is a multiple of both $\dfrac1{50}$ and $\dfrac1{30}$ is a multiple of $\dfrac1{10}$ (if $\dfrac p{50}=\dfrac q{30}$ then $3p=5q$, so $5\mid p$), and there are $9^2=81$ points with both coordinates in $\left\{\dfrac1{10},\dots,\dfrac9{10}\right\}$. The answer is $2401-81=\boxed{\textbf{(C)}\ 2320}$.''',
'Squares|Area decomposition|Lengths, perimeter, and area|HCF and LCM|Coordinate geometry',6,source=src('AMC 10',2011,'A',25))

# ---------------- 1763217 same trapezoid (alias)
b.add(1763217,1,r'''In an isosceles trapezoid $ABCD$ with $AB\parallel DC$ and $AB<DC$, an altitude is dropped from $A$ to the point $E$ on the longer base $DC$. The legs are $2$ cm long, $DE=1$ cm, and $BE$ is drawn. A student argues that the shorter base must be $2$ cm because the figure splits into three equilateral triangles. Show that the shorter base is not determined, and find the error.''',
r'''For any $x>0$ the points $D=(0,0)$, $E=(1,0)$, $A=(1,\sqrt3)$, $B=(1+x,\sqrt3)$, $C=(2+x,0)$ give such a trapezoid with $AB=x$, so the shorter base can be any positive length. The student assumes, without reason, that $BE$ bisects an angle and that triangle $EBC$ is equilateral; this holds only when $x=2$.''',
'Trapezoids|Isosceles triangles|Counterexamples|Coordinate geometry',2,
note='Same problem as topic 1763215 in this batch (aliased).')

# ---------------- 1762944 tangents, angle 120
fig=r'''real r=8*sqrt(3);
pair O=(0,0),B=(-16,0),A=r*dir(120),C=r*dir(240);
draw(circle(O,r),linewidth(0.9));
draw(A--B--C,linewidth(0.9));
draw(O--A,dashed);draw(O--C,dashed);draw(O--B,dashed);
pair u=unit(B-A),w=unit(O-A);draw(A+1.4*u--A+1.4*u+1.4*w--A+1.4*w);
pair u2=unit(B-C),w2=unit(O-C);draw(C+1.4*u2--C+1.4*u2+1.4*w2--C+1.4*w2);
draw(arc(B,2.2,-60,60));label("$120^\circ$",B+(3.6,0));
dot(O);
label("$O$",O,E);label("$A$",A,N);label("$C$",C,S);label("$B$",B,W);
label("$8$",(A+B)/2,NW);label("$r$",(O+A)/2,NE);'''
b.add(1762944,1,r'''$\overline{AB}$ and $\overline{BC}$ are tangent to circle $O$ at $A$ and $C$, respectively. The measure of $\angle ABC$ is $120^\circ$ and $AB=8$. What is the area of the circle?''',
r'''A radius to a point of tangency is perpendicular to the tangent, so $OA\perp AB$ and $OC\perp CB$. Triangles $OAB$ and $OCB$ are congruent (hypotenuse $OB$ common, $OA=OC$), so $OB$ bisects $\angle ABC$ and $\angle ABO=60^\circ$.
'''+asy(fig,'5.5cm')+r'''
In the right triangle $OAB$, $r=OA=AB\tan60^\circ=8\sqrt3$. The area of the circle is $\pi r^2=\boxed{192\pi}$.''',
'Tangents|Circles|Special right triangles|Lengths, perimeter, and area',2)

# ---------------- 1762933 10-digit first+last=10
b.add(1762933,1,r'''How many $10$-digit positive integers have first and last digits adding up to $10$? (The first digit is not $0$.)''',
r'''The first digit $f$ is $1,\dots,9$, and then the last digit must be $10-f$, which is a digit from $9$ down to $1$; so there are $9$ choices for the pair. The $8$ middle digits are arbitrary: $10^8$ choices. The total is $9\cdot10^8=\boxed{900000000}$.''',
'Multiplication principle|Digit problems',1)

# ---------------- 1762832 perpendicular hands in 24 hours
b.add(1762832,1,r'''How many times in a $24$-hour day (from midnight to the next midnight) are the minute hand and the hour hand of a clock perpendicular? (A student gets $48$, reasoning ``twice every hour''. Explain why this is wrong.)''',
r'''The minute hand turns $360^\circ$ per hour and the hour hand $30^\circ$ per hour, so the angle from the hour hand to the minute hand increases steadily at $330^\circ$ per hour. In $24$ hours it increases by $24\cdot330^\circ=7920^\circ=22\cdot360^\circ$. In each full turn of this relative angle the hands are perpendicular exactly twice (relative angle $90^\circ$ and $270^\circ$). At midnight the relative angle is $0^\circ$, so none of these moments falls at the endpoints, and the count is $22\cdot2=\boxed{44}$.

``Twice every hour'' fails because the hour hand also moves: the minute hand gains a full lap on the hour hand only $22$ times a day, not $24$. For instance, between $2{:}00$ and $4{:}00$ the hands are perpendicular only three times (about $2{:}27$, $3{:}00$ and $3{:}33$), since the moment near $3{:}00$ is shared.''',
'Clock problems|Calendar and clock problems|Rates|Relative speed',3,
note='The poster got 48 and the key 44; the record asks for the count and for the error.')

# ---------------- 1757873 five problems
T=1757873
b.add(T,1,r'''Determine the number of positive integers less than $1000$ that contain at least one digit $1$ in their decimal representation.''',
r'''Count the complement. Write each of $0,1,\dots,999$ with three digits (leading zeros allowed). The strings with no digit $1$ have $9$ choices per digit: $9^3=729$, one of which is $000$. So $728$ positive integers below $1000$ contain no $1$, and $999-728=\boxed{271}$ contain at least one.''',
'Complementary counting|Digit problems|Multiplication principle',2)
fig=r'''real x=180/7;
pair A=(0,0),B=3*dir(-90-x/2),C=3*dir(-90+x/2);
real t=abs(B-C);
pair D=t*dir(-90+x/2),Ep=2*t*Cos(x)*dir(-90-x/2);
draw(A--B--C--cycle,linewidth(0.9));
draw(D--Ep--C,blue+linewidth(0.8));
void tk(pair P,pair Q){pair m=(P+Q)/2,v=0.12*unit(rotate(90)*(Q-P));draw(m-v--m+v,linewidth(0.7));}
tk(A,D);tk(D,Ep);tk(Ep,C);tk(C,B);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$D$",D,E);label("$E$",Ep,W);'''
b.add(T,2,r'''In triangle $ABC$, $AB=AC$. Points $D$ and $E$ lie on $\overline{AC}$ and $\overline{AB}$ respectively, such that $AD=DE=EC=CB$. Find $\angle BAC$.''',
r'''Let $\angle BAC=x$.
'''+asy(fig,'3.2cm')+r'''
\begin{itemize}
\item $AD=DE$: in triangle $ADE$, $\angle DEA=\angle DAE=x$, so the exterior angle $\angle EDC=2x$.
\item $DE=EC$: in triangle $DEC$, $\angle ECD=\angle EDC=2x$.
\item In triangle $AEC$, the exterior angle at $E$ is $\angle CEB=\angle EAC+\angle ECA=x+2x=3x$.
\item $EC=CB$: in triangle $ECB$, $\angle CBE=\angle CEB=3x$.
\end{itemize}
Since $AB=AC$, also $\angle ACB=\angle ABC=3x$. The angle sum of triangle $ABC$ gives $x+3x+3x=180^\circ$, so $\angle BAC=\boxed{\left(\dfrac{180}{7}\right)^\circ}\approx25.7^\circ$.''',
'Isosceles triangles|Angle chasing|Angle sums',4,
note='The post\'s text is garbled ("AD=DE=?EC=DC?"); it is read as the standard problem AD = DE = EC = CB. (Read literally with EC = DC, the condition AB = AC is never used and the answer would be 30 degrees.)')
b.add(T,3,r'''The value of a three-digit number increases by $108$ when its first digit is moved to the end, and increases by $189$ when its last digit is moved to the front. Determine the sum of all such three-digit numbers.''',
r'''Let the number be $\overline{abc}$ with $a\ne0$. The conditions are
\[
\overline{bca}-\overline{abc}=90b+9c-99a=108,\qquad \overline{cab}-\overline{abc}=99c-90a-9b=189,
\]
i.e.\ $10b+c-11a=12$ and $11c-10a-b=21$. From the first, $c=11a+12-10b$; substituting into the second, $111a-111b+132=21$, so $b=a+1$, and then $c=a+2$. With $1\le a$ and $a+2\le9$ the numbers are $123,234,\dots,789$, and their sum is
\[
\dfrac{7(123+789)}{2}=\boxed{3192}.
\]''',
'Place value|Linear equations|Digit problems|Arithmetic sequences',3)
b.add(T,4,r'''The number $123456789101112\cdots99100$ is formed by writing the integers from $1$ to $100$ in order. Determine the largest number that can be obtained by deleting $100$ of its digits (the remaining digits keep their order).''',
r'''The number has $9+2\cdot90+3=192$ digits, so $92$ remain. Compare numbers with the same number of digits from the left: we should make the first digit as large as possible, then the second, and so on, while keeping enough digits after each chosen one.

\begin{itemize}
\item The first $9$ appears after $8$ digits: delete $1,\dots,8$ ($8$ deletions).
\item The next $9$ is the last digit of $19$, after the $19$ digits $1,0,1,1,\dots,1,8,1$: delete them ($27$ deletions in all). Similarly take the $9$ of $29$, $39$ and $49$ ($46$, $65$, $84$ deletions).
\item Now $16$ deletions remain, and the digits continue $5,0,5,1,5,2,\dots,5,7,5,8,5,9,6,0,\dots$. The next $9$ (in $59$) would need $19$ deletions, too many. Among the next $17$ digits the largest is the $7$ of $57$, reached by deleting $15$ digits ($99$ in all).
\item With $1$ deletion left the digits continue $5,8,5,9,\dots$: delete the $5$ and keep the $8$ of $58$.
\end{itemize}
No deletions remain, so the rest, $5960616263\cdots99100$, is kept. The largest number is
\[
\boxed{9999978596061\cdots9899100},
\]
i.e.\ $9999978$ followed by the digits of $59,60,61,\dots,99,100$ (a $92$-digit number).''',
'Bounding and extremal cases|Place value|Digit problems',5)
fig=r'''pair O=(0,0);
draw(circle(O,4.6),linewidth(0.9));
for(int k=0;k<12;++k) draw(4.3*dir(90-30*k)--4.6*dir(90-30*k));
pair H=3*dir(70),M=4*dir(-10);
draw(O--H,linewidth(1.6));draw(O--M,linewidth(1));
draw(H--M,red+dashed);
draw(arc(O,0.9,-10,70));label("$\theta$",1.3*dir(30));
dot(O);
label("$3$",H/2,W);label("$4$",M/2,S);label("$d$",(H+M)/2,NE,red);'''
b.add(T,5,r'''A clock has an hour hand of length $3$ and a minute hand of length $4$. From $1{:}00$ am to $1{:}00$ pm of the same day, how many times is the distance between the tips of the two hands an integer?''',
r'''Let $\theta$ be the angle between the hands. By the law of cosines the distance between the tips is
\[
d=\sqrt{3^2+4^2-2\cdot3\cdot4\cos\theta}=\sqrt{25-24\cos\theta}.
\]
'''+asy(fig,'4.5cm')+r'''
As the angle from the hour hand to the minute hand goes once round, from $0^\circ$ to $360^\circ$, $d$ increases from $1$ to $7$ (at $180^\circ$) and decreases back to $1$. So in each full turn the integer values $2,3,4,5,6$ occur twice each and $1$ and $7$ once each: $12$ times.

The minute hand gains $330^\circ$ per hour on the hour hand, so in the $12$ hours it gains $12\cdot330^\circ=11\cdot360^\circ$: eleven full turns of the relative angle. At $1{:}00$ (start and end) the angle is $30^\circ$ and $d^2=25-12\sqrt3$ is not an integer, so no occurrence is double-counted at the endpoints. The answer is $11\cdot12=\boxed{132}$.''',
'Clock problems|Law of cosines|Rates|Calendar and clock problems',4)

# ---------------- 1762815 squares in n x 3
b.add(1762815,1,r'''How many squares (of all sizes, with sides along the grid lines) are there in an $n\times3$ array of unit squares ($n$ rows and $3$ columns), where $n>4$?''',
r'''A $k\times k$ square fits in $(n-k+1)(3-k+1)$ positions, and $k\le3$:
\[
\underbrace{3n}_{1\times1}+\underbrace{2(n-1)}_{2\times2}+\underbrace{(n-2)}_{3\times3}=\boxed{6n-4}.
\]
(The formula holds for every $n\ge3$; for example a $3\times3$ grid has $14$ squares.)''',
'Counting shapes in figures|Systematic counting',2)

# ---------------- 1762708 AMC 8 2018 #25 (alias)
b.add(1762708,1,r'''How many perfect cubes lie between $2^8+1$ and $2^{18}+1$, inclusive?

$\textbf{(A) }4\qquad\textbf{(B) }9\qquad\textbf{(C) }10\qquad\textbf{(D) }57\qquad\textbf{(E) }58$''',
r'''The range is $257\le n^3\le262145$. Since $6^3=216<257\le343=7^3$ and $64^3=2^{18}=262144\le262145<65^3$, the cubes are $7^3,\dots,64^3$: $\boxed{\textbf{(E) }58}$ of them.''',
'Perfect cubes|Exponents|Powers of two',2,source=src('AMC 8',2018,None,25),
note='Repeat of an earlier record (aliased).')

b.save()
