from qb import *
b=Bank('p232_01')

# ---------------- 419795 2003 AMC 8 #17 (alias)
b.add(419795,1,r'''The six children listed below are from two families of three siblings each. Each child has blue or brown eyes and black or blond hair. Children from the same family have at least one of these characteristics in common. Which two children are Jim's siblings?
\[
\begin{array}{c|c|c}\text{Child}&\text{Eye Color}&\text{Hair Color}\\ \hline \text{Benjamin}&\text{Blue}&\text{Black}\\ \text{Jim}&\text{Brown}&\text{Blond}\\ \text{Nadeen}&\text{Brown}&\text{Black}\\ \text{Austin}&\text{Blue}&\text{Blond}\\ \text{Tevyn}&\text{Blue}&\text{Black}\\ \text{Sue}&\text{Blue}&\text{Blond}\end{array}
\]
$\textbf{(A)}\ \text{Nadeen and Austin}\qquad\textbf{(B)}\ \text{Benjamin and Sue}\qquad\textbf{(C)}\ \text{Benjamin and Austin}\qquad\textbf{(D)}\ \text{Nadeen and Tevyn}\qquad\textbf{(E)}\ \text{Austin and Sue}$''',
r'''Jim's siblings must share brown eyes or blond hair with him, so Benjamin and Tevyn (blue, black) are not his siblings. Of Nadeen, Austin and Sue, Nadeen shares nothing with Austin or with Sue, so Jim's siblings are Austin and Sue: $\boxed{\textbf{(E)}}$.''',
'Logical deduction',2,source=src('AMC 8',2003,None,17),
note='Repeat of an earlier record (aliased).')

# ---------------- 1728070 DE parallel BC
fig=r'''pair B=(0,0),C=(4,0),A=(2,2*Tan(70));
pair Ep=extension(C,C+dir(145),B,A);
pair D=extension(Ep,Ep+(1,0),A,C);
draw(A--B--C--cycle,linewidth(0.9));
draw(C--Ep,linewidth(0.8));draw(Ep--D,blue+linewidth(0.9));
draw(arc(C,0.8,145,180),linewidth(0.6));draw(arc(C,0.95,110,145),linewidth(0.6));
draw(arc(Ep,0.9,-35,0),linewidth(0.6));
label("$35^\circ$",C+1.3*dir(164),fontsize(8pt));
label("$35^\circ$",C+1.55*dir(128),fontsize(8pt));
label("$35^\circ$",Ep+1.5*dir(-17.5),fontsize(8pt));
draw(arc(B,0.6,0,70),linewidth(0.6));label("$70^\circ$",B+1.05*dir(35),fontsize(8pt));
path tk(pair P,pair Q){pair M=(P+Q)/2,u=unit(Q-P)*0.18,v=rotate(90)*u;return (M-v)--(M+v);}
draw(tk(C,D));draw(tk(Ep,D));
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$E$",Ep,W);label("$D$",D,E);'''
b.add(1728070,1,r'''In triangle $ABC$, $AB=AC$ and $\angle ABC=70^\circ$. Point $D$ lies on side $AC$ and point $E$ lies on side $AB$ so that $\angle ECB=35^\circ$ and $CD=DE$. Prove that $DE\parallel BC$.''',
r'''Since $AB=AC$, the base angles are equal: $\angle ACB=\angle ABC=70^\circ$.
'''+asy(fig,'5cm')+r'''
As $E$ lies on side $AB$, the ray $CE$ lies inside $\angle ACB$, so
\[
\angle DCE=\angle ACE=\angle ACB-\angle ECB=70^\circ-35^\circ=35^\circ .
\]
Triangle $CDE$ is isosceles with $CD=DE$, so its base angles at $C$ and $E$ are equal: $\angle DEC=\angle DCE=35^\circ$.

Hence $\angle DEC=\angle ECB=35^\circ$. These are alternate angles formed by the transversal $EC$ with the lines $DE$ and $BC$ ($D$ and $B$ lie on opposite sides of line $CE$). Equal alternate angles give $DE\parallel BC$. $\blacksquare$

(So $CE$ bisects $\angle ACB$, and the result is the general fact that the bisector from $C$ makes $CD=DE$ exactly when $DE\parallel BC$.)''',
'Isosceles triangles|Parallel lines|Angle chasing|Angle bisectors',2,
note='The post gives only "AC = AB, CD = DE, angle ABC = 70, angle ECB = 35, prove DE || BC" (RSM homework, no figure). The positions of D and E are not stated; the record takes D on side AC and E on side AB, the reading in which the data make sense (then CE bisects angle C).')

# ---------------- 1726572 lattice triangles (alias)
b.add(1726572,1,r'''How many triangles have all three vertices among the $25$ points of a $5\times5$ square array of lattice points?''',
r'''There are $\dbinom{25}{3}=2300$ triples. Collinear triples: rows and columns $10\cdot\dbinom53=100$; diagonals of slope $\pm1$: $2\left(\dbinom53+2\dbinom43+2\dbinom33\right)=2(10+8+2)=40$; slopes $\pm2$, $\pm\dfrac12$: $4\cdot3=12$. Total $152$, so there are $2300-152=\boxed{2148}$ triangles.''',
'Combinations|Complementary counting|Counting shapes in figures',4,
note='"Lattice points from a 5x5 grid" read as a 5 by 5 array of points. Repeat of an earlier record (aliased).')

# ---------------- 1727888 factors of 10^10 that are multiples of 2000
b.add(1727888,1,r'''How many of the positive factors of $10^{10}$ are multiples of $2000$?''',
r'''We have $10^{10}=2^{10}\cdot5^{10}$ and $2000=2^4\cdot5^3$. A factor of $10^{10}$ has the form $2^a5^b$ with $0\le a,b\le10$, and it is a multiple of $2^4\cdot5^3$ exactly when $a\ge4$ and $b\ge3$. There are $7$ choices for $a$ ($4,\dots,10$) and $8$ choices for $b$ ($3,\dots,10$), so the answer is $7\cdot8=\boxed{56}$.

(Equivalently, these factors are $2000m$ with $m$ a factor of $\dfrac{10^{10}}{2000}=2^6\cdot5^7$, which has $7\cdot8=56$ factors.)''',
'Divisor counting|Prime factorisation|Factors and multiples',2)

# ---------------- 1727994 sum of odd reciprocal squares (alias)
b.add(1727994,1,r'''It is known that $\dfrac{1}{1^2}+\dfrac{1}{2^2}+\dfrac{1}{3^2}+\cdots=\dfrac{\pi^2}{6}$. Given this fact, determine the exact value of
\[
\dfrac{1}{1^2}+\dfrac{1}{3^2}+\dfrac{1}{5^2}+\cdots .
\]''',
r'''The even terms are $\dfrac{1}{(2k)^2}=\dfrac14\cdot\dfrac1{k^2}$, so they add up to $\dfrac14\cdot\dfrac{\pi^2}{6}=\dfrac{\pi^2}{24}$. The odd terms therefore add up to $\dfrac{\pi^2}{6}-\dfrac{\pi^2}{24}=\boxed{\dfrac{\pi^2}{8}}$. (All terms are positive, so the series may be split this way.)''',
'Sequences and series|Summation',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1727959 4x4 grid with consecutive line sums
b.add(1727959,1,r'''Each of the numbers $1,2,\dots,16$ is to be written exactly once in the cells of a $4\times4$ grid. Some cells are already filled in, as shown:
\[
\begin{array}{|c|c|c|c|}
\hline 8 & & & 14\\
\hline & & 3 & \\
\hline & 12 & 13 & \\
\hline 10 & 11 & 6 & 4\\
\hline
\end{array}
\]
The grid must be completed so that the ten sums of the four rows, the four columns and the two diagonals are ten consecutive integers (in some order). Find all ways to complete the grid, and explain why there are no others.''',
r'''Name the empty cells as follows:
\[
\begin{array}{|c|c|c|c|}
\hline 8 & p & q & 14\\
\hline r & s & 3 & t\\
\hline u & 12 & 13 & v\\
\hline 10 & 11 & 6 & 4\\
\hline
\end{array}
\]
The numbers already used are $3,4,6,8,10,11,12,13,14$, so $p,q,r,s,t,u,v$ are $1,2,5,7,9,15,16$ in some order.

\textbf{The ten sums are $30,31,\dots,39$.} Let the sums be $m,m+1,\dots,m+9$; they add up to $10m+45$. The four row sums add up to $1+2+\cdots+16=136$, and so do the four column sums. The diagonal from top-left is $8+s+13+4=25+s$ and the other diagonal is $14+3+12+10=39$. Hence
\[
10m+45=136+136+(25+s)+39\quad\Longrightarrow\quad 10m=291+s .
\]
So $s\equiv9\pmod{10}$, and since $s$ is one of $1,2,5,7,9,15,16$, we get $s=9$ and $m=30$. The sums are $30,\dots,39$; already the bottom row is $31$, the diagonals are $34$ and $39$.

\textbf{The top row.} Column $2$ is $p+9+12+11=32+p\le39$, so $p\le7$; column $3$ is $q+3+13+6=22+q\ge30$, so $q\ge8$, i.e.\ $q\in\{15,16\}$. Row $1$ is $22+p+q\le39$, so $p+q\le17$, leaving $(p,q)=(1,15)$, $(2,15)$ or $(1,16)$. The last two make row $1$ equal to $39$, which is already the sum of a diagonal. So $p=1$, $q=15$, and row $1$, column $2$, column $3$ are $38,33,37$.

\textbf{The rest.} The sums used so far are $31,33,34,37,38,39$, so rows $2,3$ and columns $1,4$ have the sums $30,32,35,36$ in some order, and $r,t,u,v$ are $2,5,7,16$. Row $3$ is $25+u+v$, and the only pair from $\{2,5,7,16\}$ giving a sum in $\{30,32,35,36\}$ is $\{u,v\}=\{2,5\}$ (sum $32$). Then $\{r,t\}=\{7,16\}$ and row $2$ is $12+7+16=35$. Columns $1$ and $4$ must be $30$ and $36$: column $1$ is $18+r+u$.
\begin{itemize}
\item $r=7$: column $1$ is $25+u\in\{30,36\}$, so $u=5$, $v=2$, $t=16$; column $4$ is $18+16+2=36$. \checkmark
\item $r=16$: column $1$ is $34+u\in\{30,36\}$, so $u=2$, $v=5$, $t=7$; column $4$ is $18+7+5=30$. \checkmark
\end{itemize}
So there are exactly $\boxed{2}$ completions:
\[
\begin{array}{|c|c|c|c|}
\hline 8 & 1 & 15 & 14\\
\hline 7 & 9 & 3 & 16\\
\hline 5 & 12 & 13 & 2\\
\hline 10 & 11 & 6 & 4\\
\hline
\end{array}
\qquad\qquad
\begin{array}{|c|c|c|c|}
\hline 8 & 1 & 15 & 14\\
\hline 16 & 9 & 3 & 7\\
\hline 2 & 12 & 13 & 5\\
\hline 10 & 11 & 6 & 4\\
\hline
\end{array}
\]
with row sums $38,35,32,31$ in both, column sums $30,33,37,36$ and $36,33,37,30$, and diagonals $34$ and $39$.''',
'Magic squares|Logical deduction|Casework',4,
note='"Each cell is completed with an integer in [1,16]" is read as using each of 1 to 16 exactly once (needed for the totals; the given entries are distinct). Both completions were confirmed by trying all 5040 fillings.')

# ---------------- 1101383 average of roots
b.add(1101383,1,r'''What is the average of the values of $x$ that satisfy the equation $x^2+10x+21=0$?''',
r'''The equation factors as $(x+3)(x+7)=0$, so $x=-3$ or $x=-7$, and the average is $\dfrac{-3+(-7)}{2}=\boxed{-5}$. (By Vieta's formulas the sum of the roots is $-10$, so the average is $-5$ without solving.)''',
'Quadratic equations|Vieta\'s formulas',1,
note='From a mock MATHCOUNTS Sprint round (problem 7).')

# ---------------- 1726492 unfair coin
b.add(1726492,1,r'''An unfair coin is tossed $6$ times. The probability that it lands heads exactly $4$ times is $\dfrac13$ of the probability that it lands heads and tails the same number of times. What is the probability that it lands tails on a single toss?''',
r'''Let one toss give heads with probability $p$ and tails with probability $q=1-p$, where $0<p<1$. Then
\[
P(4\text{ heads})=\dbinom64p^4q^2=15p^4q^2,\qquad P(3\text{ heads})=\dbinom63p^3q^3=20p^3q^3 .
\]
The condition $15p^4q^2=\dfrac13\cdot20p^3q^3$ becomes, after dividing by $5p^3q^2>0$,
\[
3p=\dfrac43q\quad\Longrightarrow\quad 9p=4q=4(1-p)\quad\Longrightarrow\quad p=\dfrac4{13}.
\]
So the probability of tails is $q=\boxed{\dfrac{9}{13}}$.''',
'Binomial probability|Probability|Linear equations',3,
note='The post asks for the answer "in simplest radical form", but the condition leads to a linear equation and the answer 9/13 is rational; the record drops the radical-form request.')

# ---------------- 1723444 clock 7:23
b.add(1723444,1,r'''What are the angles formed by the hands of a clock at $7{:}23$?''',
r'''Measure positions clockwise from $12$. The minute hand moves $6^\circ$ per minute, so at $23$ minutes past it is at $23\cdot6^\circ=138^\circ$. The hour hand moves $30^\circ$ per hour and $\dfrac12^\circ$ per minute, so it is at $7\cdot30^\circ+23\cdot\dfrac12^\circ=210^\circ+11.5^\circ=221.5^\circ$.

The hands are $221.5^\circ-138^\circ=83.5^\circ$ apart. So the hands form an angle of $\boxed{83.5^\circ}$ and, on the other side, a reflex angle of $360^\circ-83.5^\circ=\boxed{276.5^\circ}$.''',
'Clock problems|Rates',2,
note='Problem 1 of a "clock marathon" thread; the other problems were never posted in the opening post.')

# ---------------- 1727520 candy canes
b.add(1727520,1,r'''Santa distributes $20$ identical candy canes to five children: Aidan, Bill, Cecilia, Donald and Emma. Donald and Emma each receive at most $1$ candy cane (possibly $0$), and Aidan, Bill and Cecilia each receive at least $3$ candy canes. All $20$ candy canes are given out. In how many ways can Santa distribute them?''',
r'''Let Donald and Emma receive $d,e\in\{0,1\}$, so Aidan, Bill and Cecilia share $20-d-e$ canes, each getting at least $3$. Give each of them $3$ first; the remaining $11-d-e$ canes are distributed freely among the three, in $\dbinom{(11-d-e)+2}{2}$ ways (stars and bars).
\begin{itemize}
\item $d+e=0$ ($1$ way): $\dbinom{13}{2}=78$.
\item $d+e=1$ ($2$ ways): $\dbinom{12}{2}=66$ each.
\item $d+e=2$ ($1$ way): $\dbinom{11}{2}=55$.
\end{itemize}
The total is $78+2\cdot66+55=\boxed{265}$.''',
'Stars and bars|Distributions and integer solutions|Casework',3)

# ---------------- 1727026 5^n with leading digit 1
b.add(1727026,1,r'''The number $5^{2018}$ has $1411$ digits and its leading digit is $3$. How many of the numbers $5^n$, for positive integers $n\le2018$, have leading digit $1$?''',
r'''Compare $5^{n+1}=5\cdot5^n$ with $5^n$. Write $5^n=m\cdot10^k$ with $1\le m<10$ (so $5^n$ has $k+1$ digits and its leading digit is $\lfloor m\rfloor$).
\begin{itemize}
\item If the leading digit is $1$, then $1\le m<2$ and $5\le5m<10$: $5^{n+1}$ has the \emph{same} number of digits.
\item If the leading digit is at least $2$, then $10\le5m<50$: $5^{n+1}$ has exactly \emph{one more} digit.
\end{itemize}
Going from $5^0=1$ ($1$ digit) to $5^{2018}$ ($1411$ digits) takes $2018$ steps, and the number of digits grows by $1410$. So exactly $1410$ of the steps $n=0,1,\dots,2017$ add a digit, and the other $2018-1410=608$ start from a power with leading digit $1$. One of these is $5^0=1$, so among $n=1,\dots,2017$ there are $607$ powers with leading digit $1$. Finally $5^{2018}$ has leading digit $3$. The answer is $\boxed{607}$.''',
'Digits and bases|Exponents|Logical deduction',5,
note='Problem 1 of the post. The digit count and leading digit of 5^2018 (1411 digits, leading digit 3) are supplied in the question, as the count cannot be found by hand otherwise; both and the answer 607 were checked exactly. Problems 2 and 3 (a general formula for 1^k + ... + n^k, for integer and for rational k) ask for formulas with no definite answer and are dropped.')

# ---------------- 1721571 lattice points in circle (alias)
b.add(1721571,1,r'''Three distinct lattice points are chosen at random in the interior of the circle $x^2+y^2=8$. What is the probability that they form a triangle?''',
r'''The interior lattice points are those with $|x|,|y|\le2$ except $(\pm2,\pm2)$: $21$ points and $\dbinom{21}{3}=1330$ triples. There are $90$ collinear triples ($32$ horizontal, $32$ vertical, $22$ of slope $\pm1$, $4$ of slope $\pm2$ or $\pm\dfrac12$), so the probability is $\dfrac{1240}{1330}=\boxed{\dfrac{124}{133}}$.''',
'Probability|Complementary counting|Lattice points|Combinations',4,
note='Repeat of an earlier record (aliased).')

# ---------------- 1727049 five numbers in [0,9]
b.add(1727049,1,r'''Five real numbers $a,b,c,d,e$ are chosen independently and uniformly at random from the interval $[0,9]$. What is the probability that no two of them are within $1$ of each other?''',
r'''The sample space is the cube $[0,9]^5$ of volume $9^5$. By symmetry, every ordering of the five numbers is equally likely (ties have probability $0$), so we may count the volume of the region where $x_1<x_2<\cdots<x_5$ (the sorted values) and multiply by $5!$.

In sorted order the condition is $x_{i+1}-x_i>1$ for $i=1,\dots,4$. Put $y_i=x_i-(i-1)$. Then $0\le y_1<y_2<\cdots<y_5\le9-4=5$, and conversely every such $y$ gives a valid $x$. The map is a translation in each coordinate, so it preserves volume. The volume of $\{0\le y_1<\cdots<y_5\le5\}$ is $\dfrac{5^5}{5!}$, so the favourable volume is $5!\cdot\dfrac{5^5}{5!}=5^5$.

The probability is $\dfrac{5^5}{9^5}=\boxed{\dfrac{3125}{59049}}$.''',
'Geometric probability|Probability|Bijections',5,
note='"Within one of each other" read as a distance less than 1 (the boundary has probability 0). Checked by simulation.')

# ---------------- 1726537 candies and bags (alias)
b.add(1726537,1,r'''A positive integer $N$ is the smallest that leaves remainder $6$ when divided by $11$, remainder $95$ when divided by $100$, and remainder $99$ when divided by $101$. Bags hold exactly $11$, $100$ or $101$ candies. If $N$ candies are packed into full bags, what is the least number of bags needed?''',
r'''$N\equiv-5\pmod{1100}$ and $N\equiv-2\pmod{101}$ give $N=70395$. At least $\left\lceil\dfrac{70395}{101}\right\rceil=697$ bags are needed, and $695\cdot101+2\cdot100=70395$ uses $697$. Answer $\boxed{697}$.''',
'Chinese remainder theorem|Remainders and congruences|Linear Diophantine equations',5,
note='Halloween story problem; packing read as filling every bag. Repeat of an earlier record (aliased).')

# ---------------- 1726968 self-inverse linear functions
b.add(1726968,1,r'''A function $f$ is its own inverse if $f(f(x))=x$ for every $x$ in its domain.
\begin{enumerate}
\item[(a)] Show that a function can be its own inverse by checking that $f(x)=\dfrac{1}{x}$ (for $x\ne0$) and $g(x)=5-x$ are.
\item[(b)] Find all real numbers $a$ and $b$ for which the linear function $h(x)=ax+b$ (defined for all real $x$) is its own inverse.
\end{enumerate}''',
r'''\textbf{(a)} For $x\ne0$, $f(f(x))=\dfrac{1}{\dfrac1x}=x$. For every real $x$, $g(g(x))=5-(5-x)=x$. So both are their own inverses. (Their graphs are symmetric about the line $y=x$, as the graph of every self-inverse function must be.)

\textbf{(b)} For all $x$,
\[
h(h(x))=a(ax+b)+b=a^2x+(ab+b).
\]
This equals $x$ for every $x$ exactly when the coefficients agree: $a^2=1$ and $b(a+1)=0$.
\begin{itemize}
\item $a=1$: then $2b=0$, so $b=0$ and $h(x)=x$.
\item $a=-1$: the second condition holds for every $b$, giving $h(x)=b-x$.
\end{itemize}
So $h$ is its own inverse exactly when $\boxed{a=1,\ b=0\ \text{ or }\ a=-1,\ b\text{ any real number}}$.''',
'Inverse functions|Functions|Functional equations',2,
note='The post only asks "Can a function be its own inverse?"; the record makes it a question with examples and a classification of self-inverse linear functions.')

# ---------------- 1727169 sums of two squares
b.add(1727169,1,r'''How many of the first $100$ positive integers can be written as $a^2+b^2$ with $a$ and $b$ nonnegative integers?''',
r'''The squares up to $100$ are $0,1,4,9,16,25,36,49,64,81,100$. Listing the sums $a^2+b^2\le100$ with $0\le a\le b$ by the larger square $b^2$:
\begin{itemize}
\item $b\le3$: $1,2,4,5,8,9,10,13,18$;
\item $b=4$: $16,17,20,25,32$;
\item $b=5$: $25,26,29,34,41,50$;
\item $b=6$: $36,37,40,45,52,61,72$;
\item $b=7$: $49,50,53,58,65,74,85,98$;
\item $b=8$: $64,65,68,73,80,89,100$;
\item $b=9$: $81,82,85,90,97$;
\item $b=10$: $100$.
\end{itemize}
Removing repeats ($25$, $50$, $65$, $85$, $100$ each appear twice), the distinct values are
\[
1,2,4,5,8,9,10,13,16,17,18,20,25,26,29,32,34,36,37,40,41,45,49,50,52,53,58,61,64,65,68,72,73,74,80,81,82,85,89,90,97,98,100,
\]
which is $\boxed{43}$ numbers.

(This agrees with the two-square theorem: $n$ is a sum of two squares exactly when every prime $p\equiv3\pmod4$ divides $n$ to an even power. If $0$ is not allowed, so that both squares are positive, the answer is $35$: the eight perfect squares $1,4,9,16,36,49,64,81$ that are not also sums of two positive squares drop out.)''',
'Perfect squares|Systematic counting',3,
note='"Sum of two squares" read with 0 allowed (squares of nonnegative integers), which is the usual convention; the solution also gives 35 for two positive squares. Both counts checked by computer.')

# ---------------- 1727051 USAMO 1972 (alias)
b.add(1727051,1,r'''Prove that for all positive integers $a,b,c$,
\[
\dfrac{\gcd(a,b,c)^2}{\gcd(a,b)\gcd(b,c)\gcd(c,a)}=\dfrac{\operatorname{lcm}(a,b,c)^2}{\operatorname{lcm}(a,b)\operatorname{lcm}(b,c)\operatorname{lcm}(c,a)} .
\]''',
r'''Compare the exponent of each prime $p$. If its exponents in $a,b,c$ are $\alpha\le\beta\le\gamma$ (after relabelling; both sides are symmetric), the left side has exponent $2\alpha-(\alpha+\beta+\alpha)=-\beta$ and the right side $2\gamma-(\beta+\gamma+\gamma)=-\beta$. All exponents agree, so the two sides are equal. $\blacksquare$''',
'HCF and LCM|Prime factorisation',3,source=src('USAMO',1972,None,1),
note='USAMO 1972 Problem 1. Repeat of an earlier record (aliased).')

# ---------------- 1726538 2015 AMC 8 #15 (alias)
b.add(1726538,1,r'''At Euler Middle School, $198$ students voted on two issues in a school referendum with the following results: $149$ voted in favor of the first issue and $119$ voted in favor of the second issue. If there were exactly $29$ students who voted against both issues, how many students voted in favor of both issues?

$\textbf{(A) }49\qquad\textbf{(B) }70\qquad\textbf{(C) }79\qquad\textbf{(D) }99\qquad\textbf{(E) }149$''',
r'''$198-29=169$ students voted for at least one issue. By inclusion-exclusion $149+119-x=169$, so $x=\boxed{\textbf{(D) }99}$.''',
'Sets and inclusion–exclusion|Venn diagrams',2,source=src('AMC 8',2015,None,15),
note='Repeat of an earlier record (aliased).')

# ---------------- 1726318 odd factors and consecutive sums
b.add(1726318,1,r'''Let $N$ be a positive integer with exactly $n$ positive odd divisors. Prove that $N$ can be written as a sum of two or more consecutive positive integers in exactly $n-1$ ways.''',
r'''\textbf{Sums of consecutive integers.} A sum of $k\ge1$ consecutive positive integers starting at $a\ge1$ is
\[
a+(a+1)+\cdots+(a+k-1)=\dfrac{k(2a+k-1)}{2}.
\]
So such a sum equals $N$ exactly when $2N=k\,m$ with $m=2a+k-1$. Here $m-k=2a-1$ is odd and positive, so $k$ and $m$ have \emph{opposite parity} and $m>k$. Conversely, if $2N=km$ with $k<m$ of opposite parity, then $a=\dfrac{m-k+1}{2}$ is a positive integer, and the $k$ integers from $a$ to $a+k-1$ add up to $N$. So the representations of $N$ as a sum of $k\ge1$ consecutive positive integers correspond exactly to the factorisations $2N=km$ with $k<m$ and $k,m$ of opposite parity.

\textbf{Counting the factorisations.} In such a factorisation exactly one of $k,m$ is odd, and it divides $N$ (since the odd factor $d$ of $2N=dd'$ is coprime to $2$). Conversely, every odd divisor $d$ of $N$ gives the factorisation $2N=d\cdot\dfrac{2N}{d}$ into an odd and an even number, which are different; putting the smaller one first gives a pair $k<m$. Different odd divisors give different pairs (the odd member of the pair is $d$). Hence the number of representations with $k\ge1$ terms equals the number $n$ of odd divisors of $N$.

\textbf{Removing the trivial sum.} Exactly one of these representations has $k=1$ term, namely $N$ itself (it comes from $d=1$ if $N$ is even, and from $d=N$ if $N$ is odd). So $N$ has exactly $n-1$ representations as a sum of \emph{two or more} consecutive positive integers. $\blacksquare$

For example, $15$ has odd divisors $1,3,5,15$, and indeed $15=7+8=4+5+6=1+2+3+4+5$ in $3$ ways; a power of $2$ has $n=1$ and no such representation.''',
'Factors and multiples|Divisor counting|Bijections|Parity|Arithmetic sequences',5,
note='Checked for every N up to 3000 by direct enumeration.')

# ---------------- 1726274 locus on variable parabola
fig=r'''import graph;
real k=4;
pair Fa=(1,0),Fb=(3,0);
draw((-0.6,0)--(5.2,0),gray,Arrow(5));draw((0,-5.2)--(0,5.2),gray,Arrow(5));
real a1=1,a3=3;
path p1=graph(new real(real y){return y^2/(4*a1);},-3.6,3.6,operator ..);
path p3=graph(new real(real y){return y^2/(4*a3);},-4.8,4.8,operator ..);
p1=reflect((0,0),(1,1))*p1;p3=reflect((0,0),(1,1))*p3;
draw(p1,linewidth(0.8));draw(p3,linewidth(0.8));
draw(shift(2,0)*xscale(2)*yscale(4)*unitcircle,red+dashed+linewidth(0.9));
pair P1=(3,2*sqrt(3)),P3=(1,2*sqrt(3));
dot(Fa);dot(Fb);dot(P1,red);dot(P3,red);
draw(Fa--P1,blue);draw(Fb--P3,blue);
label("$k$",Fa+0.3*(P1-Fa),W,blue);label("$k$",Fb+0.3*(P3-Fb),E,blue);
label("$x$",(5.2,0),S);label("$y$",(0,5.2),W);
label("$a=1$",(3.24,-3.6),E);label("$a=3$",(1.92,-4.8),E);
label("$O$",(0,0),SW);'''
b.add(1726274,1,r'''Let $k>0$ be fixed. For each value of the parameter $a>0$, consider the parabola $y^2=4ax$ with focus $(a,0)$. On each such parabola take the points whose distance from the focus equals $k$. Find the equation of the locus of these points as $a$ varies.''',
r'''For a point $(x,y)$ on $y^2=4ax$, the distance to the focus $(a,0)$ equals the distance to the directrix $x=-a$, which is $x+a$ (as $x\ge0$). So the condition is $x+a=k$, i.e.\ $a=k-x$, which requires $0\le x<k$ (as $a>0$).

Eliminate the parameter: $y^2=4ax=4(k-x)x$, that is,
\[
\boxed{y^2=4kx-4x^2}\qquad\text{or}\qquad \dfrac{\left(x-\dfrac k2\right)^2}{\left(\dfrac k2\right)^2}+\dfrac{y^2}{k^2}=1 .
\]
'''+asy(fig,'6.5cm')+r'''
This is the ellipse with centre $\left(\dfrac k2,0\right)$ and semi-axes $\dfrac k2$ (horizontal) and $k$ (vertical). Conversely, every point of this ellipse with $0\le x<k$ lies on the parabola with $a=k-x>0$ at distance $k$ from its focus; for instance the origin is the vertex of the parabola with $a=k$. Only the point $(k,0)$ is missed, since it would need $a=0$. So the locus is the ellipse $y^2=4kx-4x^2$ with the single point $(k,0)$ removed. The figure shows $k=4$: on $y^2=4x$ ($a=1$) and $y^2=12x$ ($a=3$) the points at distance $4$ from the focus lie on the dashed ellipse.''',
'Parabolas|Ellipses|Loci and geometric constraints|Conic sections',4,
note='The post is garbled ("the locus of a point on the variable parabola y^2 = 4ax whose distance from the focus is always equal to k ... a is parameter"); the record states the intended question. The answer y^2 = 4k x - 4x^2 (an ellipse) was checked numerically.')

# ---------------- 1726527 Halloween logic
b.add(1726527,1,r'''The following statements are all true.
\begin{itemize}
\item If I don't invite my best friend, I invite my sister to collect candy with me.
\item If I go trick-or-treating, I always get the most candy.
\item If I reveal that I am wearing a funny costume, my sister chooses not to collect candy with me.
\item If I invite my best friend, I never get the most candy.
\item If my best friend dares me to wear a serious costume, I will wear my funny costume.
\item If I go to a haunted house, my friend gets scared.
\item If my friend gets scared, he will dare me to wear a serious costume.
\end{itemize}
Suppose I go trick-or-treating. Which of the following must then be true?

(a) I go to a haunted house.\quad (b) My friend dares me to wear a funny costume.\quad (c) I invite my best friend.\quad (d) I don't get the most candy.\quad (e) I don't go to a haunted house.''',
r'''Suppose I go trick-or-treating. Then:
\begin{itemize}
\item I get the most candy (statement 2), so (d) is \emph{false}.
\item Since inviting my best friend would mean not getting the most candy (statement 4), I do not invite my best friend: (c) is \emph{false}.
\item Not inviting my best friend means I invite my sister (statement 1). If I revealed a funny costume she would not come (statement 3), so I do not reveal that I am wearing a funny costume.
\end{itemize}
Nothing else follows. Whether I go to a haunted house is not determined: if I do, my friend gets scared, dares me to wear a serious costume, and I wear my funny costume. That is consistent with everything above, because \emph{wearing} the funny costume is not the same as \emph{revealing} it. If I don't go to the haunted house, all the statements also hold. So neither (a) nor (e) must be true. Finally, no statement ever produces a dare to wear a funny costume, so (b) need not be true.

Hence $\boxed{\text{none of (a)--(e) must be true}}$; in fact (c) and (d) are certainly false. Going trick-or-treating is consistent with all the statements: I invite my sister and not my best friend, get the most candy, and keep my costume a secret.''',
'Logical deduction',3,
note='Halloween logic puzzle; the post gives no answer. Checked by enumerating all truth assignments of the nine atomic statements.')

# ---------------- 1726526 Fibonacci units digits period 60
b.add(1726526,1,r'''Let $F_1=F_2=1$ and $F_{n+2}=F_{n+1}+F_n$. Prove that the units digits of the Fibonacci numbers repeat with period $60$, and that $60$ is the smallest period.''',
r'''\textbf{Pairs determine the future.} The residue of $F_{n+2}$ modulo any $m$ is determined by the residues of $F_n$ and $F_{n+1}$. So if $(F_{p},F_{p+1})\equiv(F_0,F_1)=(0,1)\pmod m$ (with $F_0=0$), then $F_{n+p}\equiv F_n\pmod m$ for all $n\ge0$. Conversely, if $p$ is a period modulo $m$ (that is, $F_{n+p}\equiv F_n$ for all $n\ge1$), then running the recurrence backwards ($F_n=F_{n+2}-F_{n+1}$) also gives $F_p\equiv F_0$, so $(F_p,F_{p+1})\equiv(0,1)$. The periods are therefore exactly the $p\ge1$ with $(F_p,F_{p+1})\equiv(0,1)$, and they are the multiples of the smallest one (if $p$ is the smallest period and $q$ is a period, then $q\bmod p$ is $0$ or a smaller period).

\textbf{Modulo $2$.} The sequence is $1,1,0,1,1,0,\dots$: the smallest period is $3$.

\textbf{Modulo $5$.} The sequence $F_1,\dots,F_{21}$ is
\[
1,1,2,3,0,3,3,1,4,0,4,4,3,2,0,2,2,4,1,0,1 .
\]
The pairs $(F_p,F_{p+1})$ with $F_p\equiv0$ are $(0,3),(0,4),(0,2),(0,1)$ for $p=5,10,15,20$, so the first time $(0,1)$ returns is $p=20$: the smallest period is $20$.

\textbf{Modulo $10$.} A number's residue modulo $10$ is determined by its residues modulo $2$ and $5$. So $p$ is a period modulo $10$ exactly when it is a period modulo $2$ and modulo $5$, i.e.\ when $3\mid p$ and $20\mid p$, i.e.\ when $60\mid p$. Hence the units digits repeat with period $60$, and no smaller period works. $\blacksquare$''',
'Fibonacci sequence|Remainders and congruences|Units digits and last digits|Chinese remainder theorem',5,
note='The post asks for a proof of the observed period 60 (the problem that led to it was redacted). The minimal periods 3, 20 and 60 were checked by computer.')

# ---------------- 1726675 tetrahedron edges
fig=r'''pair A=(0,0),B=(3.2,-0.6),C=(4.2,0.9),D=(2.0,3.3);
draw(A--B--C,linewidth(0.9));draw(A--C,dashed);
draw(D--A,linewidth(0.9));draw(D--B,linewidth(0.9));draw(D--C,linewidth(0.9));
dot(A);dot(B);dot(C);dot(D);
label("$A$",A,W);label("$B$",B,S);label("$C$",C,E);label("$D$",D,N);'''
b.add(1726675,1,r'''How many edges does a regular tetrahedron have? Explain why.''',
r'''A tetrahedron has $4$ vertices, $A,B,C,D$, and every two vertices are joined by an edge (each face is a triangle, and any two vertices lie on a common face).
'''+asy(fig,'4cm')+r'''
So the edges correspond to the pairs of vertices: $AB,AC,AD,BC,BD,CD$, which is $\dbinom42=6$ edges. Alternatively, it has $4$ triangular faces with $3$ edges each, and each edge is shared by exactly $2$ faces, giving $\dfrac{4\cdot3}{2}=6$. As a check, Euler's formula $V-E+F=4-6+4=2$ holds. The answer is $\boxed{6}$.''',
'Polyhedra|Double counting|Euler\'s polyhedron formula',1,
note='The poster asks why a regular tetrahedron has six edges.')

# ---------------- 1726581 1 = -1 with functions
b.add(1726581,1,r'''Suppose a function $f$ satisfies $f(x)=n-f(x-n)$ for every real $x$ and every integer $n$, and $f(0)=1$. Here is a ``proof'' that $1=-1$:
\[
f(0)=n-f(0-n)\ \Rightarrow\ 1=n-f(-n)\ \Rightarrow\ f(-n)=n-1\ \Rightarrow\ f(-0)=0-1\ \Rightarrow\ 1=-1 .
\]
What is wrong?''',
r'''Every step of the argument is a correct deduction from the hypotheses: putting $x=0$ gives $1=n-f(-n)$, so $f(-n)=n-1$ for every integer $n$, and $n=0$ gives $f(0)=-1$. The conclusion $1=-1$ is false, so the \emph{hypotheses} are false: no function satisfies both conditions.

Indeed, $n=0$ in the defining equation already gives $f(x)=0-f(x)$, so $f(x)=0$ for every $x$; this contradicts $f(0)=1$. (Even the condition $f(x)=n-f(x-n)$ alone forces $f\equiv0$, and then $n=1$ gives $0=1-0$, so it has no solutions at all.)

So the error is in the setup, not in the algebra: the ``definition'' of $f$ does not define any function, and from contradictory premises any statement, such as $1=-1$, can be derived. $\boxed{\text{No such function exists.}}$''',
'Functional equations|Functions|Proof by contradiction',2,
note='The post asks what is wrong with the "proof"; its hint suggests a hidden division by zero, but there is none. The real flaw is that the hypotheses are inconsistent (n = 0 gives f = 0).')

# ---------------- 1726370 MATHCOUNTS School #24 and #27
b.add(1726370,24,r'''If $a$ and $b$ are integers such that $a^2-b^2=100$, what is the greatest possible value of $a$?''',
r'''Factor: $(a-b)(a+b)=100$. The factors $a-b$ and $a+b$ have the same parity (their sum $2a$ is even), and they cannot both be odd since $100$ is even, so both are even. To make $a=\dfrac{(a-b)+(a+b)}{2}$ as large as possible, take the factor pair with the largest sum: the even pairs with product $100$ are $2\cdot50$ and $10\cdot10$ (and their negatives, which give negative $a$). The pair $a-b=2$, $a+b=50$ gives $a=26$, $b=24$, and indeed $26^2-24^2=676-576=100$. The greatest value is $\boxed{26}$.''',
'Difference of squares|Diophantine equations|Parity',3,source=src('MATHCOUNTS',None,'School',24))
b.add(1726370,27,r'''Seven jars hold a total of $250$ candies. They are lined up from left to right from fullest to emptiest, and no two jars hold the same number of candies. The leftmost jar has $72$ candies and the rightmost jar has $13$. What is the positive difference between the greatest and the least number of candies that could be in the second jar from the left?''',
r'''The middle five jars hold $165$ candies. The second jar holds at most $71$ (achievable, e.g.\ $71,40,20,18,16$) and at least $35$ (since $165\le5j_2-10$; achieved by $35,34,33,32,31$). The difference is $\boxed{36}$.''',
'Bounding and extremal cases|Inequalities',3,source=src('MATHCOUNTS',None,'School',27),
note='Repeat of an earlier record (aliased).')

# ---------------- 1725794 geometric probability in rectangle
fig=r'''pair B=(0,0),C=(6,0),D=(6,3),A=(0,3),Q=(6,1.5);
fill(B--C--Q--cycle,lightgray);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(B--Q,red+dashed+linewidth(0.8));
label("$A$",A,NW);label("$B$",B,SW);label("$C$",C,SE);label("$D$",D,NE);
label("$\dfrac12$",(C+Q)/2,E);label("$y=\dfrac{x}{4}$",(3.0,1.5),red);
label("$1$",(A+B)/2,W);label("$2$",(B+C)/2,S);'''
b.add(1725794,1,r'''In rectangle $ABCD$, $AB=1$ and $BC=2$. A point $X$ is chosen at random inside the rectangle. What is the probability that the area of triangle $ABX$ is more than twice the area of triangle $BCX$?''',
r'''Place $B=(0,0)$, $C=(2,0)$, $D=(2,1)$, $A=(0,1)$, and let $X=(x,y)$ with $0<x<2$, $0<y<1$. Triangle $ABX$ has base $AB=1$ on the line $x=0$ and height $x$, so its area is $\dfrac x2$. Triangle $BCX$ has base $BC=2$ on the line $y=0$ and height $y$, so its area is $y$.

The condition $\dfrac x2>2y$ means $y<\dfrac x4$: the point lies below the line through $B$ with slope $\dfrac14$, which meets side $CD$ at $\left(2,\dfrac12\right)$.
'''+asy(fig,'5.5cm')+r'''
The favourable region is the shaded triangle with legs $2$ and $\dfrac12$, of area $\dfrac12\cdot2\cdot\dfrac12=\dfrac12$. The rectangle has area $2$, so the probability is $\dfrac{\dfrac12}{2}=\boxed{\dfrac14}$.''',
'Geometric probability|Rectangles|Lengths, perimeter, and area|Coordinate geometry',3)

b.save()
