from qb import *
b=Bank('p235_01')

# ---------------- 1710811 a=2c, bd=c
b.add(1710811,1,r'''Suppose $a=2c$, $bd=c$, $b\ne0$ and $d=16$. Express $a$ in terms of $b$. Can the value of $a$ be determined from these conditions alone?''',
r'''From $bd=c$ and $d=16$ we get $c=16b$, so
\[
a=2c=2\cdot16b=\boxed{32b}.
\]
The value of $a$ is \emph{not} determined: $b$ can be any nonzero number. For example $b=1$ gives $c=16$, $a=32$, while $b=2$ gives $c=32$, $a=64$; both satisfy all the conditions. A numerical value of $a$ needs one more piece of information, such as the value of $b$ or $c$.''',
'Substitution|Linear equations|Algebraic expressions and identities',1,
note='As posted ("what is the value of a?") the conditions do not determine a; the record asks for a in terms of b (a = 32b) and whether a is determined.')

# ---------------- 1711180 48k^2+1 square
b.add(1711180,1,r'''Find all positive integers $k$ such that $48k^2+1$ is a perfect square.''',
r'''We need positive integers $m,k$ with $m^2-48k^2=1$. The smallest solution with $k>0$ is $(m,k)=(7,1)$, since $48+1=49$.

\textbf{Going down.} Let $(m,k)$ be a solution with $k\ge1$ and $m>0$, and put
\[
m'=7m-48k,\qquad k'=7k-m .
\]
A direct expansion gives $m'^2-48k'^2=(49-48)(m^2-48k^2)=1$ (the cross terms $\mp672mk$ cancel), so $(m',k')$ is again a solution. Since $m^2=48k^2+1>48k^2$, we have $m>\sqrt{48}\,k>6.9k$, so $k'<0.1k<k$. Also $m^2=48k^2+1\le49k^2$ (as $k\ge1$), so $m\le7k$ and $k'\ge0$, with $k'=0$ only when $k=1$. Finally $m'>0$, because $49m^2=49\cdot48k^2+49>48^2k^2$ gives $7m>48k$. So from any solution with $k\ge1$ we reach a solution with smaller nonnegative $k'$, and repeating this we arrive at $k=0$, $m=1$.

\textbf{Going up.} The step is reversed by $m=7m'+48k'$, $k=m'+7k'$. Starting from $(1,0)$ and applying the reverse step repeatedly, we therefore obtain \emph{every} solution:
\[
(1,0)\to(7,1)\to(97,14)\to(1351,195)\to(18817,2716)\to\cdots
\]
In terms of $k$ alone: the reverse step gives $m_{n+1}=7m_n+48k_n$ and $k_{n+1}=m_n+7k_n$, so $m_n=k_{n+1}-7k_n$ and
\[
k_{n+2}=m_{n+1}+7k_{n+1}=7(k_{n+1}-7k_n)+48k_n+7k_{n+1}=14k_{n+1}-k_n ,
\]
with $k_0=0$, $k_1=1$ (equivalently $m_n+k_n\sqrt{48}=(7+\sqrt{48})^n$).

So the positive integers $k$ are exactly
\[
\boxed{k=1,\ 14,\ 195,\ 2716,\ 37829,\ \dots},\qquad k_{n+1}=14k_n-k_{n-1},
\]
for instance $48\cdot14^2+1=9409=97^2$ and $48\cdot195^2+1=1825201=1351^2$.''',
'Diophantine equations|Perfect squares|Recurrence relations',5,
note='Pell equation m^2 - 48k^2 = 1; infinitely many k, described by the recurrence. Checked by brute force up to k = 10^5.')

# ---------------- 1711161 rainy vacation
b.add(1711161,1,r'''It rained on exactly $10$ days during Tricia's vacation. On each rainy day it rained either in the morning or in the afternoon, but not both. There were exactly $13$ mornings when it did not rain and exactly $17$ afternoons when it did not rain. How many days did Tricia's vacation last?''',
r'''Let the vacation last $D$ days, with rain on $x$ mornings and $y$ afternoons. Each rainy day has exactly one rainy half, so $x+y=10$. The dry mornings and dry afternoons give
\[
D-x=13,\qquad D-y=17 .
\]
Adding, $2D-(x+y)=30$, so $2D=40$ and $D=\boxed{20}$. (Then $x=7$ and $y=3$: $7+3=10$.)''',
'Systems of linear equations|Logical deduction',2)

# ---------------- 1710748 Tony and Maria
b.add(1710748,1,r'''Tony and Maria are training for a race by running all the way up and down a $700$ m long ski slope. They each run up the slope at different constant speeds. Coming down the slope, each runs at double his or her uphill speed. Maria reaches the top first, and immediately starts running back down, meeting Tony $70$ m from the top. When Maria reaches the bottom, how far behind is Tony?''',
r'''Let Maria's uphill speed be $u$ and Tony's be $v$ (so their downhill speeds are $2u$ and $2v$).

When they meet, Maria has run $700$ m up and $70$ m down, taking $\dfrac{700}{u}+\dfrac{70}{2u}=\dfrac{735}{u}$, while Tony has run $630$ m up, taking $\dfrac{630}{v}$. These times are equal, so $\dfrac vu=\dfrac{630}{735}=\dfrac67$.

After the meeting, Maria runs the remaining $630$ m down in $\dfrac{630}{2u}=\dfrac{315}{u}$. In that time Tony first finishes the last $70$ m uphill, taking $\dfrac{70}{v}=\dfrac{70\cdot7}{6u}=\dfrac{245}{3u}$, and then runs downhill at $2v=\dfrac{12u}{7}$ for the remaining time
\[
\dfrac{315}{u}-\dfrac{245}{3u}=\dfrac{700}{3u},
\]
covering $\dfrac{700}{3u}\cdot\dfrac{12u}{7}=400$ m. So Tony is $400$ m down from the top, that is $700-400=\boxed{300\text{ m}}$ from the bottom, when Maria finishes.''',
'Distance, rate, and time|Ratios, proportions, and variation',4,
note='The poster correctly reads the meeting as Maria 770 m, Tony 630 m; the record completes the computation (300 m).')

# ---------------- 1710800 2^n+1, 3^n-1 (alias)
b.add(1710800,1,r'''Find the smallest positive integer $n$ such that $2^n+1$ is divisible by $11$ and $3^n-1$ is divisible by $13$.''',
r'''Modulo $11$, the powers of $2$ are $2,4,8,5,10,9,7,3,6,1$ for $n=1,\dots,10$, so $2^n\equiv-1\pmod{11}$ exactly when $n\equiv5\pmod{10}$. Modulo $13$, $3^3=27\equiv1$, and $3,3^2$ are not $1$, so $3^n\equiv1\pmod{13}$ exactly when $3\mid n$. The smallest $n$ with $n\equiv5\pmod{10}$ and $3\mid n$ is $\boxed{15}$.''',
'Remainders and congruences|Multiplicative order|Chinese remainder theorem',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1710801 base -3 (alias)
b.add(1710801,1,r'''Express $224$ in base $-3$, using only the digits $0,1,2$.''',
r'''Divide repeatedly by $-3$, always taking a remainder in $\{0,1,2\}$:
\[
224=(-3)(-74)+2,\quad -74=(-3)(25)+1,\quad 25=(-3)(-8)+1,\quad -8=(-3)(3)+1,
\]
\[
3=(-3)(-1)+0,\quad -1=(-3)(1)+2,\quad 1=(-3)(0)+1 .
\]
Reading the remainders from the last to the first, $224=\boxed{1201112_{-3}}$. Check: $729-2\cdot243+0-27+9-3+2=224$.''',
'Digits and bases',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1710592 2018 National Sprint 12 cookies
b.add(1710592,1,r'''Rudy has a basket of perfectly cylindrical cookies of varying sizes. He has seven cookies of radius $3$ inches, eight cookies of radius $2$ inches and seven cookies of radius $1$ inch. All cookies are $0.25$ inches thick. Rudy splits the cookies into $3$ groups such that each group's cookies have the same total volume. If all the cookies remain whole, what is the fewest possible number of cookies in any group?''',
r'''All cookies have the same thickness, so volumes are proportional to $r^2$: the cookies have ``weights'' $9$ (seven of them), $4$ (eight) and $1$ (seven). The total weight is $63+32+7=102$, so each group has weight $34$.

\textbf{No group has $5$ or fewer cookies.} Suppose a group has $a$ big, $b$ medium and $c$ small cookies, with $a+b+c\le5$ and $9a+4b+c=34$. Since $36>34$, $a\le3$. If $a\le2$, then $9a+4b+c\le9a+4(5-a)=5a+20\le30<34$. If $a=3$, the other at most two cookies must weigh $7$, but two cookies from $\{4,1\}$ weigh $2$, $5$ or $8$, and one weighs $1$ or $4$. So every group has at least $6$ cookies.

\textbf{Six is possible.} For example
\[
\{9,9,4,4,4,4\},\qquad \{9,9,9,4,1,1,1\},\qquad \{9,9,4,4,4,1,1,1,1\}
\]
uses seven $9$'s, eight $4$'s and seven $1$'s, and each group weighs $34$. The fewest possible number of cookies in a group is $\boxed{6}$.''',
'Ratios, proportions, and variation|Bounding and extremal cases|Construction',4,source=src('MATHCOUNTS',2018,'National',12,rnd='Sprint'),
note='The poster found a split with a 6-cookie group and asks why 5 is impossible; the record proves the bound. The poster\'s first group (9,9,9,4,1,1,1,1) weighs 35, not 34; the record uses a corrected split (6, 7 and 9 cookies). Official answer 6.')

# ---------------- 1710182 FBH 2017 G8 P4
b.add(1710182,1,r'''Let $n$ and $k$ be positive integers, and consider the four statements
\begin{enumerate}
\item[(i)] $n+1$ is divisible by $k$;
\item[(ii)] $n=2k+5$;
\item[(iii)] $n+k$ is divisible by $3$;
\item[(iv)] $n+7k$ is prime.
\end{enumerate}
Determine all pairs $(n,k)$ for which exactly three of the four statements are true and one is false.''',
r'''\textbf{(ii) and (iii) cannot both be true.} If $n=2k+5$, then $n+k=3k+5\equiv2\pmod3$, so (iii) fails. Hence the false statement is (ii) or (iii).

\textbf{Case 1: (ii) false; (i), (iii), (iv) true.} Then $n+7k=(n+k)+6k$ is divisible by $3$ and at least $1+7=8$, so it is not prime, contradicting (iv). No solutions.

\textbf{Case 2: (iii) false; (i), (ii), (iv) true.} Now $n=2k+5$ and $k\mid n+1=2k+6$, so $k\mid6$, i.e.\ $k\in\{1,2,3,6\}$. Then $n+7k=9k+5$ equals $14,\ 23,\ 32,\ 59$ respectively, which is prime only for $k=2$ and $k=6$. For these, (iii) is indeed false by the first remark.

So $\boxed{(n,k)=(9,2)\text{ or }(17,6)}$. Check: $k=2$: $2\mid10$, $9=2\cdot2+5$, $9+14=23$ prime, $11$ not divisible by $3$; $k=6$: $6\mid18$, $17=12+5$, $17+42=59$ prime, $23$ not divisible by $3$.''',
'Divisibility|Prime numbers|Logical deduction|Casework',4,source=src('Junior Regional Olympiad FBH',2017,'Grade 8',4),
note='Checked by brute force over n, k < 2000.')

# ---------------- 1709573 FBH 2018 G7 P4 four circles
figq=r'''pair O=(0,0),O1=(-1,0),O2=(1,0),P=(0,4/3);
draw(circle(O,2),linewidth(0.8));draw(circle(O1,1),linewidth(0.8));draw(circle(O2,1),linewidth(0.8));
draw(circle(P,2/3),linewidth(0.8));
draw(O--(0,-2));draw(O2--(2,0));
dot(O);dot(O2);
label("$2$",(0,-1.25),E);label("$1$",(1.5,0),N);
label("?",P);'''
figa=r'''pair O=(0,0),O1=(-1,0),O2=(1,0),P=(0,4/3),T=(0,2);
draw(circle(O,2),linewidth(0.8));draw(circle(O1,1),linewidth(0.8));draw(circle(O2,1),linewidth(0.8));
draw(circle(P,2/3),linewidth(0.8));
draw(O--O2,blue+linewidth(0.8));draw(O2--P,blue+linewidth(0.8));draw(O--P,blue+linewidth(0.8));draw(P--T,dashed);
draw((0.15,0)--(0.15,0.15)--(0,0.15));
dot(O);dot(O1);dot(O2);dot(P);dot(T);
label("$O$",O,SE);label("$O_1$",O1,S);label("$O_2$",O2,S);label("$P$",P,W);label("$T$",T,N);'''
figa2=r'''pair O=(0,0),O2=(3,0),P=(0,4);
draw(O--O2--P--cycle,blue+linewidth(0.9));
draw((0.3,0)--(0.3,0.3)--(0,0.3));
dot(O);dot(O2);dot(P);
label("$O$",O,SW);label("$O_2$",O2,SE);label("$P$",P,N);
label("$1$",(1.5,0),S);label("$2-r$",(0,2),W);label("$1+r$",(1.5,2),NE);'''
b.add(1709573,1,r'''Four circles lie in a plane and each of them touches the other three, as shown. The biggest circle has radius $2$ and each of the two medium circles has radius $1$. Find the radius of the fourth circle.
'''+asy(figq,'5cm'),
r'''Let $O$ be the centre of the big circle. Each medium circle has diameter $2$, which is the radius of the big circle, and touches it from inside; the two medium circles touch each other. So their centres $O_1$, $O_2$ lie on a diameter of the big circle at distance $1$ from $O$, and they touch each other at $O$. The fourth circle (radius $r$, centre $P$) lies in the space above (or, symmetrically, below) them. By symmetry $P$ lies on the perpendicular to $O_1O_2$ at $O$.
'''+asy(figa,'6cm')+r'''
The fourth circle touches the big circle internally at the point $T$ of the line $OP$, so $OP=2-r$. It touches the circle with centre $O_2$ externally, so $O_2P=1+r$. In the right triangle $OO_2P$ (right angle at $O$; drawn separately below, to scale),
'''+asy(figa2,'3cm')+r'''
\[
1^2+(2-r)^2=(1+r)^2\ \Longrightarrow\ 1+4-4r+r^2=1+2r+r^2\ \Longrightarrow\ 6r=4 .
\]
So the fourth circle has radius $\boxed{\dfrac23}$.''',
'Circles|Tangent circles|Pythagorean theorem',3,source=src('Junior Regional Olympiad FBH',2018,'Grade 7',4),
note='The figure was an image in the post; the text determines it (two radius-1 circles inside the radius-2 circle, touching at its centre). The question figure is redrawn from the text.')

# ---------------- 1710480 World Cup matches
b.add(1710480,1,r'''In a football World Cup, $32$ teams are split into $8$ groups of $4$. In the group stage, each team plays every other team in its group exactly once. The top $2$ teams of each group ($16$ teams) go on to a knockout stage: a round of $16$, quarter-finals, semi-finals, a match for third place between the two losing semi-finalists, and the final. How many matches are played in the whole tournament?''',
r'''Each group of $4$ plays $\dbinom42=6$ matches, so the group stage has $8\cdot6=48$ matches.

In the knockout stage every match except the third-place match eliminates one team. Going from $16$ teams to $1$ champion eliminates $15$ teams, so there are $15$ such matches ($8+4+2+1$), plus the third-place match: $16$ matches.

In total $48+16=\boxed{64}$ matches are played.''',
'Combinations|Counting principles|Addition principle',2)

# ---------------- 1709513 AP challenge, problems 5-13
b.add(1709513,5,r'''The sum of the first three terms of an arithmetic progression is $189$, and the sum of the next three terms is $369$. What is the $10$th term?''',
r'''Let the terms be $a_1,a_2,\dots$ with common difference $d$. The sum of three consecutive terms is three times the middle one, so $3a_2=189$ and $3a_5=369$, giving $a_2=63$ and $a_5=123$. Then $3d=60$, $d=20$, and $a_{10}=a_5+5d=123+100=\boxed{223}$.''',
'Arithmetic sequences',2)
b.add(1709513,6,r'''The $15$th term of an arithmetic progression is $-235$, and the $41$st term minus the $30$th term is $-198$. What is the first term?''',
r'''With common difference $d$, $a_{41}-a_{30}=11d=-198$, so $d=-18$. Then $a_1=a_{15}-14d=-235+252=\boxed{17}$.''',
'Arithmetic sequences',2)
b.add(1709513,7,r'''Which term of the arithmetic progression $144,136,128,\dots$ is the first negative term?''',
r'''The $n$th term is $144-8(n-1)=152-8n$. It is negative when $8n>152$, i.e.\ $n>19$. (The $19$th term is $0$, which is not negative.) So the first negative term is the $\boxed{20\text{th}}$ term, equal to $-8$.''',
'Arithmetic sequences|Inequalities',1)
b.add(1709513,8,r'''Find the arithmetic mean of $14$ and $9$, that is, the number $m$ such that $14,m,9$ form an arithmetic progression.''',
r'''$m=\dfrac{14+9}{2}=\boxed{\dfrac{23}{2}}$. Indeed $14-\dfrac{23}{2}=\dfrac{23}{2}-9=\dfrac52$.''',
'Arithmetic sequences|Averages and weighted averages',1)
b.add(1709513,9,r'''The sums of the first $n$, $2n$ and $3n$ terms of an arithmetic progression are $S_1$, $S_2$ and $S_3$ respectively. Prove that $S_3=3(S_2-S_1)$.''',
r'''Let the first term be $a$ and the common difference $d$. The sum of the first $m$ terms is $\dfrac m2\bigl(2a+(m-1)d\bigr)$, so
\[
S_1=\dfrac n2\bigl(2a+(n-1)d\bigr),\qquad S_2=n\bigl(2a+(2n-1)d\bigr),\qquad S_3=\dfrac{3n}{2}\bigl(2a+(3n-1)d\bigr).
\]
Then
\[
S_2-S_1=\dfrac n2\Bigl(4a+(4n-2)d-2a-(n-1)d\Bigr)=\dfrac n2\bigl(2a+(3n-1)d\bigr),
\]
and $3(S_2-S_1)=\dfrac{3n}{2}\bigl(2a+(3n-1)d\bigr)=S_3$. $\blacksquare$

(Equivalently: $S_2-S_1$ is the sum of the terms $n+1,\dots,2n$; the three blocks of $n$ terms have sums in arithmetic progression with difference $n^2d$, and the middle block sum $S_2-S_1$ is their average, so the three blocks together give $3(S_2-S_1)$.)''',
'Arithmetic sequences|Summation',3,
note='The post writes "S3 = S(S2-S1)"; the intended (and true) identity is S3 = 3(S2 - S1).')
b.add(1709513,10,r'''Consider the increasing sequence of all three-digit numbers that leave remainder $1$ when divided by $5$. How many terms does it have, and what are its middle terms?''',
r'''The terms are $101,106,111,\dots,996$, an arithmetic progression with difference $5$, so there are $\dfrac{996-101}{5}+1=180$ terms. Since $180$ is even, there are two middle terms, the $90$th and the $91$st:
\[
101+89\cdot5=546,\qquad 101+90\cdot5=551 .
\]
So there are $\boxed{180}$ terms and the middle terms are $\boxed{546\text{ and }551}$ (their average, $548.5$, is the median of the sequence).''',
'Arithmetic sequences|Remainders and congruences',2,
note='The post asks for "the middle term"; the sequence has 180 terms, so the record asks for both middle terms (546 and 551).')
b.add(1709513,11,r'''In an arithmetic progression, the $22$nd term is $\dfrac1{19}$ and the $19$th term is $\dfrac1{22}$. What is the $418$th term?''',
r'''With common difference $d$,
\[
3d=a_{22}-a_{19}=\dfrac1{19}-\dfrac1{22}=\dfrac{3}{418},
\]
so $d=\dfrac1{418}$. Then $a_1=a_{19}-18d=\dfrac{19}{418}-\dfrac{18}{418}=\dfrac1{418}$, and in general $a_n=\dfrac{n}{418}$. Hence $a_{418}=\boxed{1}$.''',
'Arithmetic sequences|Fractions',2)
b.add(1709513,12,r'''The numbers $4a-1$, $5a+2$ and $8a-1$ are consecutive terms of an arithmetic progression. Find the second number.''',
r'''The middle term is the average of its neighbours: $2(5a+2)=(4a-1)+(8a-1)$, so $10a+4=12a-2$ and $a=3$. The numbers are $11,17,23$, and the second number is $\boxed{17}$.''',
'Arithmetic sequences|Linear equations',1)
b.add(1709513,13,r'''The sum of the first $7$ terms of an arithmetic progression is $-42$ and the sum of its first $21$ terms is $-714$. What is the sum of the first $50$ terms?''',
r'''With first term $a$ and difference $d$, $S_7=7(a+3d)=-42$ and $S_{21}=21(a+10d)=-714$, so $a+3d=-6$ and $a+10d=-34$. Hence $7d=-28$, $d=-4$, $a=6$, and
\[
S_{50}=\dfrac{50}{2}\bigl(2\cdot6+49\cdot(-4)\bigr)=25(12-196)=\boxed{-4600}.
\]''',
'Arithmetic sequences|Systems of linear equations|Summation',2)

# ---------------- 1710170 FBH 2017 G8 P1
b.add(1710170,1,r'''Let $f(x)=3x-2$, and let $m$ be a real parameter.
\begin{enumerate}
\item[(a)] Find the function $g$ such that $f\bigl(2x-g(x)\bigr)=-3(1+2m)x+34$ for all real $x$.
\item[(b)] Solve the equation $g(x)=4(m-1)x-4(m+1)$ in $x$, discussing all values of $m$.
\end{enumerate}''',
r'''\textbf{(a)} $f\bigl(2x-g(x)\bigr)=3\bigl(2x-g(x)\bigr)-2=6x-3g(x)-2$. Setting this equal to $-3(1+2m)x+34$:
\[
3g(x)=6x+3x+6mx-36\quad\Longrightarrow\quad \boxed{g(x)=(2m+3)x-12}.
\]

\textbf{(b)} The equation becomes $(2m+3)x-12=4(m-1)x-4m-4$, i.e.
\[
(2m+3-4m+4)x=12-4m-4\quad\Longrightarrow\quad (7-2m)x=8-4m .
\]
\begin{itemize}
\item If $m\ne\dfrac72$: exactly one solution, $\boxed{x=\dfrac{8-4m}{7-2m}}$.
\item If $m=\dfrac72$: the equation reads $0\cdot x=-6$, which has \textbf{no solution}.
\end{itemize}''',
'Functions|Linear equations|Substitution',3,source=src('Junior Regional Olympiad FBH',2017,'Grade 8',1))

# ---------------- 1710139 FBH 2017 G7 P3
b.add(1710139,1,r'''Ten different positive integers are written on a blackboard, and their sum is $62$. Prove that the product of these numbers is divisible by $60$.''',
r'''\textbf{Step 1: the numbers $1,2,3$ are on the board.} Suppose some $x\le10$ is missing. Then the ten numbers are distinct positive integers different from $x$, so their sum is at least the sum of the ten smallest such integers, which is $(1+2+\cdots+11)-x=66-x$. Hence $66-x\le62$, so $x\ge4$. Thus $1,2,3$ are all present, and the product is divisible by $2\cdot3=6$.

\textbf{Step 2: a further factor $2$.} If $4$ is present, the product is divisible by $2\cdot4=8$, hence by $4$. If $4$ is missing, Step 1 with $x=4$ gives sum $\ge62$, with equality only for the ten numbers $1,2,3,5,6,\dots,11$; these include $2$ and $6$, so again $4$ divides the product.

\textbf{Step 3: a factor $5$.} If neither $5$ nor $10$ is present, the sum is at least the sum of the ten smallest positive integers other than $5$ and $10$, namely $(1+2+\cdots+12)-5-10=63>62$, a contradiction. So $5$ or $10$ is on the board, and $5$ divides the product.

Since $3$, $4$ and $5$ divide the product and are pairwise coprime, $60$ divides the product. $\blacksquare$''',
'Divisibility|Bounding and extremal cases|Proof by cases',4,source=src('Junior Regional Olympiad FBH',2017,'Grade 7',3),
note='Checked by enumerating all sets of ten distinct positive integers with sum 62.')

# ---------------- 1710185 FBH 2017 G8 P5
figk=r'''pair A=(0,0),B=(10,0),C=(7,5);
real a=length(C-B);
pair K=((10-a)/2,0),L=((10+a)/2,0),M=(A+C)/2,Nn=(A+B)/2;
draw(circle(Nn,a/2),gray+dashed);
draw(A--B--C--cycle,linewidth(0.9));
draw(K--M--L,blue+linewidth(0.8));draw(Nn--M,red+dashed);
pair u=unit(K-M),v=unit(L-M);real q=0.45;
draw(M+q*u--M+q*(u+v)--M+q*v);
dot(A);dot(B);dot(C);dot(K);dot(L);dot(M);dot(Nn);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,N);label("$K$",K,SW);label("$L$",L,SE);label("$M$",M,NW);label("$N$",Nn,S);'''
b.add(1710185,1,r'''Points $K$ and $L$ lie on side $AB$ of triangle $ABC$ such that $KL=BC$ and $AK=LB$. Let $M$ be the midpoint of $AC$. Prove that $\angle KML=90^\circ$.''',
r'''Let $N$ be the midpoint of $AB$.

\textbf{$N$ is also the midpoint of $KL$.} Since $AK=LB$, the points $K$ and $L$ are symmetric about the midpoint of $AB$ (going from $A$ by $AK$ and from $B$ by the same length $LB$), so $NK=NL=\dfrac{KL}{2}=\dfrac{BC}{2}$.

\textbf{$NM=\dfrac{BC}{2}$.} $M$ and $N$ are the midpoints of $AC$ and $AB$, so $MN$ is a midline of triangle $ABC$ and $MN=\dfrac{BC}{2}$.
'''+asy(figk,'7cm')+r'''
Hence $NK=NL=NM$: the point $M$ lies on the circle with diameter $KL$ (centre $N$, dashed). Since $M$ is not on line $AB$, it is different from $K$ and $L$, and by Thales' theorem (an angle inscribed in a semicircle) $\angle KML=90^\circ$. $\blacksquare$

(Directly: in triangle $KML$ the median $MN$ equals half of $KL$, so the triangles $KNM$ and $LNM$ are isosceles and $\angle KML=\angle NKM+\angle NLM$; as these three angles sum to $180^\circ$, $\angle KML=90^\circ$.)''',
'Triangles|Midpoints|Circles|Inscribed angles',4,source=src('Junior Regional Olympiad FBH',2017,'Grade 8',5),
note='Checked numerically for random triangles.')

# ---------------- 1710178 FBH 2017 G8 P3
b.add(1710178,1,r'''Find all real numbers $x$ such that
\[
\sqrt{\dfrac{x-7}{2015}}+\sqrt{\dfrac{x-6}{2016}}+\sqrt{\dfrac{x-5}{2017}}=\sqrt{\dfrac{x-2015}{7}}+\sqrt{\dfrac{x-2016}{6}}+\sqrt{\dfrac{x-2017}{5}} .
\]''',
r'''The right side requires $x\ge2017$. Put $t=x-2022$, so $t\ge-5$. Since $x-7=2015+t$, $x-2015=7+t$, and so on, the equation reads
\[
\sqrt{1+\dfrac{t}{2015}}+\sqrt{1+\dfrac{t}{2016}}+\sqrt{1+\dfrac{t}{2017}}=\sqrt{1+\dfrac t7}+\sqrt{1+\dfrac t6}+\sqrt{1+\dfrac t5}.
\]
\begin{itemize}
\item If $t>0$, then $\dfrac t7>\dfrac t{2015}$, $\dfrac t6>\dfrac t{2016}$, $\dfrac t5>\dfrac t{2017}$, so each term on the right is larger than the corresponding term on the left: no solution.
\item If $-5\le t<0$, all three inequalities reverse, and the left side is larger: no solution.
\item If $t=0$, both sides equal $3$.
\end{itemize}
So the only solution is $\boxed{x=2022}$.''',
'Radical equations|Inequalities|Substitution',4,source=src('Junior Regional Olympiad FBH',2017,'Grade 8',3))

# ---------------- 1710138 FBH 2017 G7 P2
figq2=r'''real s=sqrt(3);
pair A=(0,0),B=(6,0),C=(5,s),D=(2,2s),P=(3,3s);
draw(D--P--C,dashed+gray);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--C,blue);draw(B--D,blue);
pair u=unit(A-D),v=unit(C-D);real q=0.35;
draw(D+q*u--D+q*(u+v)--D+q*v);
draw(arc(A,0.8,0,60));draw(arc(B,0.8,120,180));
label("$60^\circ$",A+1.4*dir(40));label("$60^\circ$",B+1.5*dir(160));
dot(P);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,E);label("$D$",D,W);label("$P$",P,N);
label("$6$",(3,0),S);label("$4$",(1,s),NW);label("$2$",(5.5,s/2),E);label("$2$",(2.5,2.5s),W);label("$4$",(4,2s),E);'''
b.add(1710138,1,r'''In quadrilateral $ABCD$, $AB=6$, $AD=4$, $\angle DAB=\angle ABC=60^\circ$ and $\angle ADC=90^\circ$. Find the lengths of the diagonals and the area of the quadrilateral.''',
r'''Extend $AD$ and $BC$ to meet at $P$. Triangle $ABP$ has two $60^\circ$ angles, so it is equilateral with side $6$, and its area is $\dfrac{\sqrt3}{4}\cdot36=9\sqrt3$.

$D$ lies on $AP$ with $DP=6-4=2$. Since $\angle ADC=90^\circ$, also $\angle PDC=90^\circ$, so triangle $PDC$ is a $30^\circ$-$60^\circ$-$90^\circ$ triangle with the $60^\circ$ angle at $P$: $PC=2PD=4$ and $DC=2\sqrt3$. Hence $C$ lies on segment $PB$ with $BC=6-4=2$.
'''+asy(figq2,'6cm')+r'''
\textbf{Diagonals.} In the right triangle $ADC$, $AC^2=AD^2+DC^2=16+12=28$. In triangle $ABD$, by the law of cosines, $BD^2=36+16-2\cdot6\cdot4\cdot\dfrac12=28$. So
\[
AC=BD=\boxed{2\sqrt7}.
\]

\textbf{Area.} $[ABCD]=[ABP]-[PDC]=9\sqrt3-\dfrac12\cdot2\cdot2\sqrt3=\boxed{7\sqrt3}$.''',
'Quadrilaterals and polygons|Equilateral triangles|Special right triangles|Law of cosines|Pythagorean theorem|Lengths, perimeter, and area|Area decomposition',4,source=src('Junior Regional Olympiad FBH',2017,'Grade 7',2),
note='Checked with coordinates A(0,0), B(6,0), C(5,sqrt3), D(2,2sqrt3) and the shoelace formula.')

# ---------------- 1710140 FBH 2017 G7 P4 climbers
b.add(1710140,1,r'''A group of $27$ climbers shared $13$ loaves of bread among themselves. Every man got $2$ loaves, every woman half a loaf, and every child a third of a loaf. There was at least one man, at least one woman and at least one child. How many men, women and children were there? Find all possibilities.''',
r'''Let there be $m$ men, $w$ women and $c$ children. Then
\[
m+w+c=27,\qquad 2m+\dfrac w2+\dfrac c3=13 .
\]
Multiply the second equation by $6$: $12m+3w+2c=78$. Subtract twice the first: $10m+w=24$. So $m\le2$, and $m\ge1$ by assumption:
\begin{itemize}
\item $m=1$: $w=14$, $c=27-15=12$. Check: $2+7+4=13$.
\item $m=2$: $w=4$, $c=27-6=21$. Check: $4+2+7=13$.
\end{itemize}
So there are \textbf{two} possibilities: $\boxed{1\text{ man},\ 14\text{ women},\ 12\text{ children}}$ or $\boxed{2\text{ men},\ 4\text{ women},\ 21\text{ children}}$. (Without the assumption that there is at least one man, $0$ men, $24$ women and $3$ children would also work.)''',
'Linear Diophantine equations|Systems of linear equations|Fractions',3,source=src('Junior Regional Olympiad FBH',2017,'Grade 7',4),
note='The post asks for "how many men, women and children"; the data allow two answers with at least one of each (and a third with no men). The record states the at-least-one assumption and asks for all possibilities.')

# ---------------- 1710133 FBH 2017 G6 P5 father's life
b.add(1710133,1,r'''A father's childhood lasted one sixth of his life. After a further one eighth of his life he married and immediately left for the army. After another one twelfth of his life he returned from the army, and $5$ years later his son was born. The son lived half as many years as his father lived, and died $4$ years before his father. How many years did the father live, and how old was he when his son was born?''',
r'''Let the father live $L$ years. His life splits into childhood, the time until marriage, the army, the $5$ years until the son's birth, the son's life, and the final $4$ years:
\[
\dfrac L6+\dfrac L8+\dfrac L{12}+5+\dfrac L2+4=L .
\]
Since $\dfrac16+\dfrac18+\dfrac1{12}+\dfrac12=\dfrac{4+3+2+12}{24}=\dfrac78$, we get $\dfrac L8=9$, so $L=\boxed{72}$ years. When the son was born the father was
\[
12+9+6+5=\boxed{32}\text{ years old}.
\]
Check: the son lived $36$ years and died when the father was $68=72-4$.''',
'Linear equations|Fractions|Age problems',2,source=src('Junior Regional Olympiad FBH',2017,'Grade 6',5))

# ---------------- 1710124 FBH 2017 G6 P2 cisterns
b.add(1710124,1,r'''Three cisterns hold $780$ litres of milk in total. If we pour off a quarter of the milk from the first cistern, a fifth from the second cistern and $\dfrac37$ from the third cistern, the same amount of milk remains in each cistern. How much milk is in each cistern?''',
r'''Let the amount remaining in each cistern be $t$. Then the first cistern held $\dfrac34$ of its milk equal to $t$, so it held $\dfrac{4t}3$; similarly the second held $\dfrac{5t}{4}$ (since $\dfrac45$ of it is $t$) and the third $\dfrac{7t}{4}$ (since $\dfrac47$ of it is $t$). Then
\[
\dfrac{4t}3+\dfrac{5t}4+\dfrac{7t}4=\dfrac{16t+15t+21t}{12}=\dfrac{13t}{3}=780,
\]
so $t=180$. The cisterns hold $\boxed{240,\ 225\text{ and }315}$ litres. Check: $180=\dfrac34\cdot240=\dfrac45\cdot225=\dfrac47\cdot315$, and $240+225+315=780$.''',
'Fractions|Linear equations|Ratios, proportions, and variation',2,source=src('Junior Regional Olympiad FBH',2017,'Grade 6',2))

# ---------------- 1710125 FBH 2017 G6 P3 altitudes
figh=r'''pair A=(0,0),B=(6,0);
pair C=extension(A,A+dir(80),B,B+dir(134));
pair D=A+dot(C-B,A-B)/dot(C-B,C-B)*(C-B);
pair Dd=B+dot(A-B,C-B)/dot(C-B,C-B)*(C-B);
pair Ee=A+dot(B-A,C-A)/dot(C-A,C-A)*(C-A);
pair H=extension(A,Dd,B,Ee);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--Dd,blue);draw(B--Ee,blue);
real q=0.3;
pair u=unit(A-Dd),v=unit(C-Dd);draw(Dd+q*u--Dd+q*(u+v)--Dd+q*v);
u=unit(B-Ee);v=unit(C-Ee);draw(Ee+q*u--Ee+q*(u+v)--Ee+q*v);
draw(arc(H,0.55,degrees(Dd-H),degrees(Ee-H)),red);
label("$126^\circ$",H+0.95*dir(75),red);
draw(arc(A,0.65,0,80));label("$80^\circ$",A+1.15*dir(18));
dot(H);dot(Dd);dot(Ee);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,N);label("$H$",H,N);label("$D$",Dd,NE);label("$E$",Ee,NW);'''
b.add(1710125,1,r'''In an acute triangle $ABC$, $\angle BAC=80^\circ$. The altitudes from $A$ and from $B$ meet at $H$, and $\angle AHB=126^\circ$. Which side of the triangle is the shortest and which is the longest?''',
r'''Let $D$ and $E$ be the feet of the altitudes from $A$ and $B$, on $BC$ and $CA$. In quadrilateral $CEHD$ the angles at $D$ and $E$ are right angles, so $\angle DHE=360^\circ-90^\circ-90^\circ-\angle C=180^\circ-\angle C$. The angles $\angle AHB$ and $\angle DHE$ are vertical angles (the figure marks $\angle DHE$), so
\[
126^\circ=\angle AHB=180^\circ-\angle C\quad\Longrightarrow\quad \angle C=54^\circ,
\]
and $\angle B=180^\circ-80^\circ-54^\circ=46^\circ$.
'''+asy(figh,'7cm')+r'''
In a triangle the longer side is opposite the larger angle. The angles are $\angle A=80^\circ>\angle C=54^\circ>\angle B=46^\circ$, so the \textbf{longest side is $BC$} (opposite $A$) and the \textbf{shortest side is $CA$} (opposite $B$): $\boxed{CA<AB<BC}$.''',
'Triangles|Altitudes|Angle chasing|Angle sums',3,source=src('Junior Regional Olympiad FBH',2017,'Grade 6',3),
note='"Altitudes h_a and h_b" read as the altitudes from A and B. The figure is drawn with the actual angles 80, 46, 54 degrees.')

# ---------------- 1710135 FBH 2017 G7 P1 percent
b.add(1710135,1,r'''The price of a book was increased by $20\%$ and then decreased by $10\%$. By what percentage should the current price now be decreased to obtain a price equal to $54\%$ of the original price?''',
r'''If the original price is $P$, the current price is $1.2\cdot0.9\,P=1.08P$. We want a final price of $0.54P=\dfrac12\cdot1.08P$, so the current price must be halved: the decrease is $\boxed{50\%}$.''',
'Percentages',2,source=src('Junior Regional Olympiad FBH',2017,'Grade 7',1))

# ---------------- 1710118 FBH 2017 G6 P1 cards
b.add(1710118,1,r'''Cards numbered $1$ to $100$ are laid out in order. First Faris takes every card whose number is a multiple of $7$, and after that every remaining card whose number contains the digit $7$. Then, from the remaining cards, Lamija takes every card whose number is divisible by $5$, and after that every remaining card whose number contains the digit $5$.
\begin{enumerate}
\item[(a)] Who gets more cards, and by how many?
\item[(b)] Answer the same question if instead Lamija goes first with her ``$5$ rule'' and Faris then applies his ``$7$ rule'' to the remaining cards.
\end{enumerate}''',
r'''\textbf{Useful lists.} Multiples of $7$: $7,14,\dots,98$ ($14$ numbers). Numbers containing $7$: $7,17,\dots,97$ and $70,\dots,79$, that is $10+10-1=19$ numbers, of which $7,70,77$ are multiples of $7$; the other $16$ are $17,27,37,47,57,67,71,72,73,74,75,76,78,79,87,97$. Multiples of $5$: $20$ numbers. Numbers containing $5$ but not divisible by $5$: $51,52,53,54,56,57,58,59$ ($8$ numbers).

\textbf{(a)} Faris takes $14+16=30$ cards. Of the $20$ multiples of $5$, Faris already has $35,70$ (multiples of $7$) and $75$ (contains $7$), so Lamija takes $17$. Of $51,52,53,54,56,57,58,59$, Faris has $56$ and $57$, so Lamija takes $6$ more: $23$ cards in all. \textbf{Faris has $\boxed{7}$ more cards} ($30$ against $23$).

\textbf{(b)} Lamija takes all $20+8=28$ of her cards. Of the multiples of $7$, she already has $35,56,70$, so Faris takes $11$; of the other $16$ numbers containing $7$, she has $57$ and $75$, so Faris takes $14$: $25$ cards in all. \textbf{Lamija has $\boxed{3}$ more cards} ($28$ against $25$).''',
'Systematic counting|Factors and multiples|Casework',3,source=src('Junior Regional Olympiad FBH',2017,'Grade 6',1),
note='"Every 7th card" read as the cards whose numbers are multiples of 7. Checked by direct simulation.')

# ---------------- 1709775 squares
figsq=r'''draw((0,0)--(10,0)--(10,10)--(0,10)--cycle,linewidth(0.8));
draw((13,0)--(37,0)--(37,24)--(13,24)--cycle,linewidth(0.8));
draw((40,0)--(66,0)--(66,26)--(40,26)--cycle,blue+linewidth(0.8));
label("$10$",(5,0),S);label("$24$",(25,0),S);label("$26$",(53,0),S);
label("$100$",(5,5));label("$576$",(25,12));label("$676$",(53,13),blue);'''
b.add(1709775,1,r'''The perimeters of two squares are $40$ metres and $96$ metres. Find the perimeter of a third square whose area equals the sum of the areas of the first two squares.''',
r'''The sides of the first two squares are $\dfrac{40}{4}=10$ m and $\dfrac{96}{4}=24$ m, so their areas are $100\text{ m}^2$ and $576\text{ m}^2$. The third square has area $100+576=676\text{ m}^2$, so its side is $\sqrt{676}=26$ m.
'''+asy(figsq,'8cm')+r'''
Its perimeter is $4\cdot26=\boxed{104\text{ m}}$. (Note that $10^2+24^2=26^2$: the three sides form a right triangle.)''',
'Squares|Lengths, perimeter, and area|Perfect squares',1)

# ---------------- 1709576 FBH 2018 G8 P1 time
b.add(1709576,1,r'''Asked ``What time is it?'', a father told his son: ``A quarter of the time that has passed since midnight, plus half of the time that remains until the next midnight, gives the exact time.'' What time was it?''',
r'''Let $t$ hours have passed since midnight, so $24-t$ hours remain. The condition is
\[
\dfrac t4+\dfrac{24-t}{2}=t\quad\Longrightarrow\quad t+48-2t=4t\quad\Longrightarrow\quad t=\dfrac{48}{5}=9.6 .
\]
So $9.6$ hours, i.e.\ $9$ hours $36$ minutes, have passed: the time is $\boxed{9{:}36}$ (a.m.). Check: $\dfrac{9.6}{4}+\dfrac{14.4}{2}=2.4+7.2=9.6$.''',
'Linear equations|Fractions|Calendar and clock problems',2,source=src('Junior Regional Olympiad FBH',2018,'Grade 8',1),
note='Times are measured over a 24-hour day from midnight, the standard reading of this classic.')

b.save()
