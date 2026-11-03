from qb import *
b=Bank('en03')

# ---------------- 1790978 9-gon three consecutive
b.add(1790978,1,r'''Each of the integers $1,2,3,\dots,9$ is assigned to a vertex of a regular $9$-sided polygon, every vertex receiving a different integer, so that the sum of the integers assigned to any three consecutive vertices does not exceed some positive integer $n$. What is the least possible value of $n$ for which such an assignment exists?''',
r'''Let the numbers around the polygon be $a_1,\dots,a_9$ (indices modulo $9$), and let $T_i=a_i+a_{i+1}+a_{i+2}$.

\textbf{Lower bound.} Each number appears in exactly three of the nine sums, so $T_1+\cdots+T_9=3(1+2+\cdots+9)=135$, and the average sum is $15$. Hence $n\ge15$. If $n=15$, then all nine sums equal $15$; from $T_i=T_{i+1}$ we get $a_i=a_{i+3}$, so $a_1=a_4$, contradicting distinctness. Therefore $n\ge16$.

\textbf{Construction.} Place the numbers around the polygon in the order
\[
1,\ 5,\ 8,\ 2,\ 6,\ 7,\ 3,\ 4,\ 9 .
\]
The sums of three consecutive numbers (cyclically) are $14,15,16,15,16,14,16,14,15$, all at most $16$.

So the least possible value is $\boxed{16}$.''',
'Bounding and extremal cases|Construction|Double counting|Proof by contradiction',4,
note='Checked by exhaustive search over all arrangements.')

# ---------------- 1790901 Martin weight
b.add(1790901,1,r'''Since 1970, when Martin graduated from high school, he has gained $2$ pounds every year. In 2000 he was $40\%$ heavier than in 1970. What percent of his 2015 weight was his 2000 weight?''',
r'''Let his 1970 weight be $w$ pounds. By 2000 he had gained $30\cdot2=60$ pounds, so $w+60=1.4w$, giving $w=150$. His weight was $210$ pounds in 2000 and $210+15\cdot2=240$ pounds in 2015. The ratio is $\dfrac{210}{240}=\dfrac78$, so his 2000 weight was $\boxed{87.5\%}$ of his 2015 weight.''',
'Percentages|Linear equations',2)

# ---------------- 1790697 knights and thieves
b.add(1790697,1,r'''On an island there are two types of people: knights, who always tell the truth, and thieves, who always lie. A line of $2015$ islanders is formed; everyone knows who is of which type. Each of them says: ``The number of thieves in front of me is greater than the number of knights behind me.'' How many thieves are in the line?''',
r'''Number the people $1,2,\dots,2015$ from the front. For person $i$ let $T_i$ be the number of thieves among persons $1,\dots,i-1$ and $K_i$ the number of knights among persons $i+1,\dots,2015$, and put $f(i)=T_i-K_i$. Person $i$'s statement is $f(i)>0$, so person $i$ is a knight exactly when $f(i)>0$.

\textbf{The thieves come first.} Going from $i$ to $i+1$, $T$ increases by $1$ if person $i$ is a thief, and $K$ decreases by $1$ if person $i+1$ is a knight; so $f(i+1)\ge f(i)$. As $f$ never decreases, the set of $i$ with $f(i)>0$ is a final block of the line. Hence the line consists of $t$ thieves followed by $2015-t$ knights, for some $t$.

\textbf{Find $t$.} For a thief in position $i\le t$, the statement $i-1>2015-t$ must be false, i.e.\ $i-1\le2015-t$; the strongest case $i=t$ gives $t-1\le2015-t$, so $t\le1008$. For a knight in position $i>t$, the statement $t>2015-i$ must be true; the strongest case $i=t+1$ gives $t>2014-t$, so $t\ge1008$. (If $t=2015$ the last thief's statement $2014>0$ would be true, so there is at least one knight; if $t=0$ the first knight's statement $0>2014$ would be false.) Hence $t=1008$, and conversely the line of $1008$ thieves followed by $1007$ knights satisfies all the conditions. There are $\boxed{1008}$ thieves.''',
'Truth-tellers and liars|Logical deduction|Invariants and monovariants',5,
note='The posted answer choices (0, 1, 2014, 1002, 1003) do not contain the correct answer; the record is free-response with answer 1008 (checked by exhaustive search for lines of up to 13 people, where the answer is always the ceiling of n/2).')

# ---------------- 1790898 printing presses
b.add(1790898,1,r'''Two printing presses working together can complete a job in $2.5$ hours. Working alone, press A can do the job in $10$ hours. How many hours will press B take to do the job by itself?''',
r'''Together the presses do $\dfrac{1}{2.5}=\dfrac25$ of the job per hour, and press A does $\dfrac1{10}$ per hour. So press B does $\dfrac25-\dfrac1{10}=\dfrac3{10}$ of the job per hour and needs $\boxed{\dfrac{10}{3}}$ hours, that is, $3$ hours $20$ minutes.''',
'Work and rates|Fractions',2)

# ---------------- 1790151 triangle of medians (alias)
b.add(1790151,1,r'''Triangle $A$ has medians of lengths $k$, $l$ and $m$, and triangle $B$ has sides of lengths $k$, $l$ and $m$. Find $\dfrac{[B]}{[A]}$, where $[\ ]$ denotes area.''',
r'''With the centroid of $A$ at the origin and vertex vectors $a,b,c$ ($a+b+c=0$), the medians are $-\dfrac32a,-\dfrac32b,-\dfrac32c$, which close up to a triangle similar (ratio $\dfrac32$) to the triangle with sides $|a|,|b|,|c|$ of area $\dfrac13[A]$. So $[B]=\dfrac94\cdot\dfrac13[A]$ and the ratio is $\boxed{\dfrac34}$.''',
'Medians and centroids|Area ratios|Vectors',4,
note='Repeat of an earlier record (aliased).')

# ---------------- 1790666 Venn circles (alias)
b.add(1790666,1,r'''Can a Venn diagram for four sets (showing all $16$ combinations of inside and outside) be drawn with four circles? Prove your answer.''',
r'''No. Adding circles one at a time, the $k$-th circle meets the earlier ones in at most $2(k-1)$ points and so adds at most $2(k-1)$ regions; $n$ circles make at most $n^2-n+2$ regions, which is $14<16$ for $n=4$.''',
'Counting regions|Venn diagrams|Mathematical induction',4,
note='Repeat of an earlier record (aliased). The four-colour theorem asked about in the post is not related.')

# ---------------- 1790652 Ms Kitts
b.add(1790652,1,r'''Ms.\ Kitts works at a music store. Last week she sold $6$ more than $3$ times the number of CDs that she sold this week. She sold a total of $110$ CDs over the two weeks. Write a system of equations for $l$, the number of CDs she sold last week, and $t$, the number she sold this week, and solve it.''',
r'''``$6$ more than $3$ times this week's number'' is $3t+6$, so
\[
l=3t+6,\qquad l+t=110 .
\]
Substituting, $3t+6+t=110$, so $4t=104$, $t=26$ and $l=84$. She sold $\boxed{84\text{ CDs last week and }26\text{ this week}}$.''',
'Systems of linear equations|Linear equations',1,
note='The poster wrote l = 3c + 6 with an undefined c; the variable for this week is t. The record also asks for the solution.')

# ---------------- 1786655 Varun (alias)
b.add(1786655,1,r'''One evening, Varun finishes reading a novel and immediately begins reading its sequel. Each novel has pages numbered consecutively starting with page $1$, and each has fewer than $1000$ pages. If Varun reads a total of $42$ pages in one sitting and the sum of the page numbers he reads in that sitting is $2018$, what is the number of the last page of the first novel?''',
r'''If he reads the last $p$ pages $N-p+1,\dots,N$ of the first novel and pages $1,\dots,42-p$ of the sequel, the condition simplifies to $p(N-42)=1115=5\cdot223$. With $1\le p\le41$ and $N<1000$, $p=5$ and $N=\boxed{265}$.''',
'Arithmetic sequences|Summation|Diophantine equations|Factoring',4,source=src('MATHCOUNTS',2018,'State',8,rnd='Target'),
note='Repeat of an earlier record (aliased).')

# ---------------- 1790194 sum n/2^n (alias)
b.add(1790194,1,r'''Evaluate $\displaystyle\sum_{n=1}^{\infty}\dfrac{n}{2^n}$.''',
r'''The partial sums are $S_N=2-\dfrac{N+2}{2^N}$ (subtract $\dfrac12S_N$ from $S_N$), so the sum is $\boxed{2}$.''',
'Sequences and series|Summation',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1790252 multinomial coefficient
b.add(1790252,1,r'''When $(x+2y-z)^8$ is expanded and like terms are combined, what is the coefficient of $x^3y^2z^3$?''',
r'''By the multinomial theorem, the term with $x^3$, $(2y)^2$ and $(-z)^3$ arises in $\dbinom{8}{3,2,3}=\dfrac{8!}{3!\,2!\,3!}=560$ ways (choose which $3$ of the $8$ factors give $x$, then which $2$ of the remaining $5$ give $2y$). Its coefficient is
\[
560\cdot1^3\cdot2^2\cdot(-1)^3=\boxed{-2240}.
\]''',
'Binomial theorem|Combinations|Multiset permutations',3,
note='The "theorem" the poster could not remember is the multinomial theorem.')

# ---------------- 1789225 CHAI
b.add(1789225,1,r'''In the list of numbers $1,2,\dots,9999$, the digits $0$ through $9$ are replaced with the letters A through J, respectively. For example, the number $501$ is replaced by the string ``FAB'' and $8243$ is replaced by the string ``ICED''. The resulting list of $9999$ strings is sorted alphabetically (as in a dictionary, so a string comes before every longer string that begins with it). How many strings appear before ``CHAI'' in this list?''',
r'''``CHAI'' is the number $2708$. A string comes before ``CHAI'' exactly when it is a proper prefix of ``CHAI'' or, at the first position where they differ, it has an earlier letter. No string starts with A (no leading zeros).
\begin{itemize}
\item First letter B (numbers whose first digit is $1$): $1$, $10$--$19$, $100$--$199$, $1000$--$1999$, i.e.\ $1+10+100+1000=1111$ strings.
\item The prefix ``C'' itself (the number $2$): $1$.
\item First letters C then A--G (numbers starting $20,\dots,26$): for each such two-digit start there are $1+10+100=111$ strings, so $7\cdot111=777$.
\item The prefix ``CH'' ($27$): $1$. The prefix ``CHA'' ($270$): $1$.
\item ``CHA'' followed by A--H ($2700$--$2707$): $8$.
\end{itemize}
Every other string either begins with a later letter or comes after ``CHAI''. The total is $1111+1+777+1+1+8=\boxed{1899}$.''',
'Systematic counting|Digits and bases|Casework',4,source=src('MATHCOUNTS',2016,'State',29,rnd='Sprint'),
note='Dictionary order is stated explicitly. Answer checked by sorting the 9999 strings.')

# ---------------- 1788973 median length; hexagon
fig1=r'''pair B=(0,0),C=(10,0),A=(0.6,sqrt(80.64)),D=(5,0);
draw(A--B--C--cycle,linewidth(0.9));draw(A--D,blue+linewidth(0.8));
dot(D);
draw((1.15,-0.25)--(1.35,0.25));draw((8.65,-0.25)--(8.85,0.25));
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$D$",D,S);
label("$9$",(A+B)/2,W);label("$13$",(A+C)/2+0.3*dir(45),NE);label("$5$",(2.5,0),S);label("$5$",(7.5,0),S);label("$10$",(A+D)/2,E,blue);'''
b.add(1788973,1,r'''Triangle $ABC$ has side lengths $AB=9$, $BC=10$ and $CA=13$, and $D$ is the midpoint of side $BC$. What is the length of segment $AD$?''',
r'''Put $B=(0,0)$, $C=(10,0)$ and $A=(u,v)$ with $v>0$. Then $u^2+v^2=81$ and $(u-10)^2+v^2=169$. Subtracting, $-20u+100=88$, so $u=\dfrac35$ and $v^2=81-\dfrac{9}{25}=\dfrac{2016}{25}$. With $D=(5,0)$,
\[
AD^2=\left(5-\dfrac35\right)^2+v^2=\dfrac{484}{25}+\dfrac{2016}{25}=\dfrac{2500}{25}=100,
\]
so $AD=\boxed{10}$.
'''+asy(fig1,'6cm')+r'''
(Equivalently, by Apollonius's theorem $AB^2+AC^2=2AD^2+2BD^2$: $81+169=2AD^2+50$, so $AD^2=100$.)''',
'Medians and centroids|Triangles|Coordinate geometry|Distance formula|Midpoints',3,
note='The post gives only "side lengths 9, 10 and 13" without saying which side is BC. The record takes BC = 10 (with AB = 9, CA = 13), the assignment that gives the intended integer answer 10; for BC = 9 or 13 the median would be sqrt(457)/2 or sqrt(193)/2.')
fig2=r'''real ap=7; real R=2*ap/sqrt(3);
pair[] V; for(int i=0;i<6;++i) V.push(R*dir(30+60*i));
draw(V[0]--V[1]--V[2]--V[3]--V[4]--V[5]--cycle,linewidth(0.9));
pair P=(3,-1/sqrt(3));
real[] d={4,6,9,10,8,5};
for(int k=0;k<6;++k){
  pair n=dir(60*k), F=P+d[k]*n;
  draw(P--F,dashed+blue);
  pair t=dir(60*k+90);
  draw(F-0.45*n--F-0.45*n+0.45*t--F+0.45*t);
  label("$"+string(d[k])+"$",P+0.55*d[k]*n,t,blue);
}
dot(P);label("$P$",P,2.4*S);'''
b.add(1788973,2,r'''The lengths of the perpendiculars drawn to the sides of a regular hexagon from a point inside it are $4$, $5$, $6$, $8$, $9$ and $10$ centimetres. What is the length of a side of the hexagon, in centimetres? Express your answer in simplest radical form.''',
r'''Let the side be $s$ and let $P$ be the point. Joining $P$ to the six vertices cuts the hexagon into six triangles, each with a side of the hexagon as base and the corresponding perpendicular as height. So
\[
[\text{hexagon}]=\dfrac12s\,(4+5+6+8+9+10)=21s .
\]
On the other hand a regular hexagon is made of six equilateral triangles of side $s$, so its area is $6\cdot\dfrac{\sqrt3}{4}s^2=\dfrac{3\sqrt3}{2}s^2$. Hence $\dfrac{3\sqrt3}{2}s^2=21s$ and
\[
s=\dfrac{42}{3\sqrt3}=\dfrac{14}{\sqrt3}=\boxed{\dfrac{14\sqrt3}{3}}.
\]
(The data are consistent: the distance between opposite sides is $2\cdot7=14$, and the distances pair up as $4+10=5+9=6+8=14$. The figure shows such a point.)
'''+asy(fig2,'6cm'),
'Regular polygons|Area decomposition|Lengths, perimeter, and area|Equilateral triangles|Radicals',3)

# ---------------- 1760605 criminal organization
b.add(1760605,1,r'''The $20$ members of a criminal organization are given the different numbers $1,2,\dots,20$. Five of them, chosen at random, announce their numbers, and the organization's penalty score is the sum of the five numbers announced. What is the expected value of the penalty score?''',
r'''Let $X_1,\dots,X_5$ be the five numbers announced. Each $X_i$ is equally likely to be any of $1,\dots,20$, so $E[X_i]=\dfrac{1+20}{2}=10.5$. By linearity of expectation (which holds even though the $X_i$ are dependent),
\[
E[X_1+\cdots+X_5]=5\cdot10.5=\boxed{52.5}.
\]''',
'Expected value|Sampling without replacement|Mean',2,
note='From a user\'s personal problem set. "Best possible estimate for the penalty score" is read as the expected value.')

# ---------------- 1789216 base 5 and base 8
b.add(1789216,1,r'''How many positive integers have the same number of digits when written in base $5$ and in base $8$?''',
r'''A positive integer $m$ has $d$ digits in base $5$ exactly when $5^{d-1}\le m<5^d$, and $d$ digits in base $8$ exactly when $8^{d-1}\le m<8^d$. Both hold exactly when $8^{d-1}\le m<5^d$ (as $5^{d-1}\le8^{d-1}$ and $5^d\le8^d$).
\begin{itemize}
\item $d=1$: $1\le m<5$: $4$ numbers.
\item $d=2$: $8\le m<25$: $17$ numbers.
\item $d=3$: $64\le m<125$: $61$ numbers.
\item $d=4$: $512\le m<625$: $113$ numbers.
\item $d=5$: $4096>3125$, so none; and for $d\ge5$, $\dfrac{8^{d-1}}{5^d}=\dfrac18\left(\dfrac85\right)^d\ge\dfrac18\left(\dfrac85\right)^5>1$, so there are none for larger $d$ either.
\end{itemize}
The total is $4+17+61+113=\boxed{195}$.''',
'Digits and bases|Exponents|Casework',3,
note='Checked by direct computation.')

# ---------------- 1789696 circles in a 45 degree angle
fig=r'''real s=sin(pi/8); pair u=dir(22.5);
draw((0,0)--(20,0),linewidth(0.8));draw((0,0)--(13.5,13.5),linewidth(0.8));
draw((0,0)--19.5*u,dashed+gray);
real d=2.5;
for(int n=0;n<3;++n){real r=d*s; draw(circle(d*u,r),blue); dot(d*u,blue);
  if(n>0) label("$w_"+string(n)+"$",d*u+0.55*r*dir(112.5),blue); else label("$w_0$",(d*u.x,0),S,blue);
  d=d*(1+s)/(1-s);}
label("$O$",(0,0),SW);label("$y=x$",(13.5,13.5),NW);label("$x$-axis",(20,0),SE);'''
b.add(1789696,1,r'''In the $xy$-plane, circles $w_0,w_1,w_2,\dots$ all lie inside the angle between the positive $x$-axis and the ray $y=x$, $x>0$, and each is tangent to both the $x$-axis and the line $y=x$. Each circle $w_n$ is externally tangent to $w_{n+1}$, and $w_{n+1}$ is farther from the origin $O$ than $w_n$.
\begin{enumerate}
\item[(a)] Prove that the centres of all the circles lie on the line through $O$ and the centre of $w_0$. (Is induction needed?)
\item[(b)] Find the ratio $\dfrac{r_{n+1}}{r_n}$ of the radii of consecutive circles.
\end{enumerate}''',
r'''(a) The centre of a circle tangent to two lines is at distance equal to the radius from each line, so it is equidistant from both lines. Inside the angle, the points equidistant from the two sides are exactly the points of the angle bisector, the ray from $O$ at angle $22.5^\circ$ to the $x$-axis. So every centre lies on this one ray, which in particular passes through $O$ and the centre of $w_0$. No induction is needed: each circle's centre is on the bisector for the same reason, independently of its neighbours.
'''+asy(fig,'7cm')+r'''
(b) Let $s=\sin22.5^\circ$. If the centre of $w_n$ is at distance $d_n$ from $O$, then its distance to the $x$-axis is $d_n\sin22.5^\circ$, so $r_n=s\,d_n$. The centres lie on one ray and the circles are externally tangent, so $d_{n+1}-d_n=r_n+r_{n+1}$, i.e.
\[
\dfrac{r_{n+1}}{s}-\dfrac{r_n}{s}=r_n+r_{n+1}\quad\Longrightarrow\quad r_{n+1}(1-s)=r_n(1+s).
\]
Hence
\[
\dfrac{r_{n+1}}{r_n}=\boxed{\dfrac{1+\sin22.5^\circ}{1-\sin22.5^\circ}=\dfrac{2+\sqrt{2-\sqrt2}}{2-\sqrt{2-\sqrt2}}}\approx2.240,
\]
using $\sin22.5^\circ=\dfrac{\sqrt{2-\sqrt2}}{2}$. The radii form a geometric sequence (and the configuration is a sequence of dilations centred at $O$).''',
'Tangent circles|Angle bisectors|Geometric sequences|Dilations and homothety|Trigonometry|Circles',4,
note='The post asks whether "the centres are collinear" is a valid induction problem. The record makes the configuration precise (all circles inside the 45-degree angle, chained outward), notes that induction is unnecessary, and adds part (b) on the ratio of radii.')

# ---------------- 1788599 (x+p)(x+q)<0
b.add(1788599,1,r'''For which real numbers $p$ and $q$ does the inequality $(x+p)(x+q)<0$ have at least one real solution $x$?''',
r'''If $p=q$, the left side is $(x+p)^2\ge0$ for every real $x$, so there is no solution.

If $p\ne q$, take $x=-\dfrac{p+q}{2}$, the midpoint of $-p$ and $-q$. Then
\[
(x+p)(x+q)=\dfrac{p-q}{2}\cdot\dfrac{q-p}{2}=-\dfrac{(p-q)^2}{4}<0 .
\]
(In fact the solution set is the open interval between $-p$ and $-q$, where the two factors have opposite signs.) So the solution set is nonempty exactly when $\boxed{p\ne q}$.''',
'Inequalities|Quadratic equations|Factoring',2)

# ---------------- 1731835 basketball
b.add(1731835,1,r'''In basketball, players score $2$ points for each field goal, $3$ points for each three-point shot, and $1$ point for each free throw made. Write an expression for the total score of a team that makes $g$ field goals, $t$ three-point shots and $f$ free throws. Find the total score of a team that makes $23$ field goals, $6$ three-pointers and $11$ free throws.''',
r'''Each field goal is worth $2$, each three-pointer $3$ and each free throw $1$, so the total score is $\boxed{2g+3t+f}$. For $g=23$, $t=6$, $f=11$:
\[
2\cdot23+3\cdot6+11=46+18+11=\boxed{75}.
\]''',
'Algebraic expressions and identities|Whole-number operations',1,
note='The poster\'s answer (2g + 3t + f, total 75) is correct.')

# ---------------- 1789625 boxes in boxes
fig=r'''pair ob=(0.7,0.4);
pair P(real x,real y,real z){return (x,z)+y*ob;}
void box(real a,real b2,real c,real x0,real y0,real z0,pen p,pen hid){
  pair A=P(x0,y0,z0),B=P(x0+a,y0,z0),C=P(x0+a,y0+b2,z0),D=P(x0,y0+b2,z0);
  pair A2=P(x0,y0,z0+c),B2=P(x0+a,y0,z0+c),C2=P(x0+a,y0+b2,z0+c),D2=P(x0,y0+b2,z0+c);
  draw(A--B--B2--A2--cycle,p);draw(B--C--C2--B2,p);draw(A2--D2--C2,p);
  draw(A--D--C,hid);draw(D--D2,hid);
}
box(3,3,3,0,0,0,black+linewidth(0.9),gray+dashed+linewidth(0.4));
box(2,2,2,0,0,0,blue+linewidth(0.8),blue+dashed+linewidth(0.5));
dot(P(1.5,1.5,1.5),red);label("$Z$",P(1.5,1.5,1.5),dir(-40),red);
label("$3$",P(1.5,0,0),S);label("$2$",P(0.8,0,2),S,blue);'''
b.add(1789625,1,r'''Small boxes of size $x\times y\times z$ are to be packed, without overlapping and with edges parallel to the edges of the large box, into an $a\times b\times c$ box. By volume, at most $\left\lfloor\dfrac{abc}{xyz}\right\rfloor$ small boxes can fit.
\begin{enumerate}
\item[(a)] Show that this bound is not always achieved, even when every dimension of the small box is less than every dimension of the large box.
\item[(b)] Show that the bound is achieved when $x\mid a$, $y\mid b$ and $z\mid c$.
\end{enumerate}''',
r'''(a) Take $2\times2\times2$ cubes in a $3\times3\times3$ box. The volume bound is $\left\lfloor\dfrac{27}{8}\right\rfloor=3$, but only one cube fits. Place the box as $[0,3]^3$. A cube with edges parallel to the box is $[u,u+2]\times[v,v+2]\times[w,w+2]$ with $0\le u,v,w\le1$. Since $u<1.5<u+2$ (and similarly for $v$, $w$), the centre $Z=(1.5,1.5,1.5)$ of the box lies in the \emph{interior} of every such cube. So any two cubes would overlap, and at most $\boxed{1}$ cube fits, not $3$.
'''+asy(fig,'5cm')+r'''
(b) If $a=px$, $b=qy$, $c=rz$ for positive integers $p,q,r$, cut the large box into a $p\times q\times r$ array of $x\times y\times z$ boxes. That is $pqr=\dfrac{abc}{xyz}$ small boxes, which meets the bound. The divisibility condition only needs to hold for some orientation of the small box: for example, $2\times1\times1$ boxes fill a $3\times2\times1$ box once they are turned so that their edge of length $2$ runs along the edge of length $2$.''',
'Cubes and rectangular prisms|Volume|Counterexamples|Floor and ceiling functions',3,
note='The post asks whether floor(abc/xyz) boxes always fit and under what conditions. The record asks for a counterexample (with axis-parallel packing, to keep the proof elementary) and a sufficient condition.')

# ---------------- 1789074 mean of three-digit numbers
b.add(1789074,1,r'''What is the mean of all three-digit numbers that can be formed using three different digits chosen from $2,3,5$ and $7$?''',
r'''There are $4\cdot3\cdot2=24$ such numbers. By symmetry, each of the four digits appears in each position (hundreds, tens, units) in exactly $\dfrac{24}{4}=6$ of them. So the average digit in each position is $\dfrac{2+3+5+7}{4}=\dfrac{17}{4}$, and the mean of the numbers is
\[
111\cdot\dfrac{17}{4}=\dfrac{1887}{4}=\boxed{471.75}.
\]
(Equivalently, the sum of all $24$ numbers is $6\cdot17\cdot111=11322$, and $\dfrac{11322}{24}=471.75$.)''',
'Mean|Symmetry|Permutations|Place value',2)

# ---------------- 1789107 B^2+AB+1 | A^2+AB+1
b.add(1789107,1,r'''Let $A$ and $B$ be positive integers such that $B^2+AB+1$ divides $A^2+AB+1$. Prove that $A=B$.''',
r'''Let $d=B^2+AB+1$. Since $d$ divides both $A^2+AB+1$ and itself, it divides their difference:
\[
d\mid(A^2+AB+1)-(B^2+AB+1)=A^2-B^2=(A-B)(A+B).
\]
Now $d=B(A+B)+1$, so any common divisor of $d$ and $A+B$ divides $1$; that is, $\gcd(d,A+B)=1$. Hence $d\mid A-B$.

But $|A-B|<\max(A,B)\le AB+1<d$ when $A\ne B$ (because $A,B\ge1$, so $A\le AB$ and $B\le AB$). A multiple of $d$ with absolute value less than $d$ must be $0$, so $A-B=0$, i.e.\ $A=B$. $\blacksquare$''',
'Divisibility|HCF and LCM|Difference of squares|Bounding and extremal cases',4,
note='Checked by search over 1 <= A, B <= 300.')

# ---------------- 1789385 digits of 2^30
b.add(1789385,1,r'''How many digits are in the integer $2^{30}$?''',
r'''Since $2^{10}=1024$, we have $2^{30}=1024^3$. Now $1000^3=10^9\le1024^3<1100^3=1.331\times10^9<10^{10}$, so $2^{30}$ lies between $10^9$ and $10^{10}$ and has $\boxed{10}$ digits. (Indeed $2^{30}=1073741824$.)''',
'Exponents|Estimation|Powers of two',2,source=src('MATHCOUNTS',2014,'State',None,rnd='Sprint'))

# ---------------- 1789434 floor
b.add(1789434,1,r'''Evaluate
\[
\left\lfloor\dfrac{2012^3}{2008\cdot2010}-\dfrac{2008^3}{2010\cdot2012}\right\rfloor .
\]''',
r'''Let $n=2010$. Over the common denominator $(n-2)n(n+2)$,
\[
\dfrac{(n+2)^3}{(n-2)n}-\dfrac{(n-2)^3}{n(n+2)}=\dfrac{(n+2)^4-(n-2)^4}{n(n-2)(n+2)} .
\]
By the binomial theorem the odd powers of $2$ survive: $(n+2)^4-(n-2)^4=2\left(4\cdot2n^3+4\cdot8n\right)=16n^3+64n$. So the expression equals
\[
\dfrac{16n(n^2+4)}{n(n^2-4)}=\dfrac{16(n^2+4)}{n^2-4}=16+\dfrac{128}{n^2-4}.
\]
Since $0<\dfrac{128}{2010^2-4}<1$, the floor is $\boxed{16}$.''',
'Floor and ceiling functions|Substitution|Algebraic manipulation|Binomial theorem',4)

# ---------------- 1789337 compare fractions
b.add(1789337,1,r'''Which is larger:
\[
\dfrac{2018^{2018}+1}{2019^{2019}+1}\qquad\text{or}\qquad\dfrac{2017^{2017}+1}{2018^{2018}+1}\ ?
\]''',
r'''Let $a=2017^{2017}$, $b=2018^{2018}$, $c=2019^{2019}$. All are positive, so comparing $\dfrac{b+1}{c+1}$ with $\dfrac{a+1}{b+1}$ is the same as comparing $(b+1)^2$ with $(a+1)(c+1)$, i.e.\ $b^2+2b$ with $ac+a+c$.

\textbf{Claim: $ac>b^2$.} With $m=2018$,
\[
\dfrac{ac}{b^2}=\dfrac{(m-1)^{m-1}(m+1)^{m+1}}{m^{2m}}=\left(\dfrac{(m-1)(m+1)}{m^2}\right)^{m-1}\left(\dfrac{m+1}{m}\right)^{2}=\left(1-\dfrac1{m^2}\right)^{m-1}\left(1+\dfrac1m\right)^2 .
\]
By Bernoulli's inequality $\left(1-\dfrac1{m^2}\right)^{m-1}\ge1-\dfrac{m-1}{m^2}=\dfrac{m^2-m+1}{m^2}$, so
\[
\dfrac{ac}{b^2}\ge\dfrac{(m^2-m+1)(m+1)^2}{m^4}=\dfrac{m^4+m^3+m+1}{m^4}>1 .
\]

\textbf{Conclusion.} By AM-GM, $a+c\ge2\sqrt{ac}>2b$. Adding this to $ac>b^2$ gives $ac+a+c>b^2+2b$, so $(a+1)(c+1)>(b+1)^2$ and
\[
\dfrac{2018^{2018}+1}{2019^{2019}+1}<\dfrac{2017^{2017}+1}{2018^{2018}+1}.
\]
The second fraction, $\boxed{\dfrac{2017^{2017}+1}{2018^{2018}+1}}$, is larger.''',
'Inequalities|AM-GM inequality|Exponents|Bounding and extremal cases',5,
note='Proof written by the authors; the inequality was checked exactly with integer arithmetic and for analogous triples (n-1)^(n-1), n^n, (n+1)^(n+1) with small n.')

# ---------------- 1789389 multiple of 500
b.add(1789389,1,r'''What is the least positive integer $n$ such that the sum of all positive integers from $1$ to $n$ is a multiple of $500$?''',
r'''We need $500\mid\dfrac{n(n+1)}{2}$, i.e.\ $1000=8\cdot125\mid n(n+1)$. Since $n$ and $n+1$ are coprime, $125$ divides one of them and $8$ divides one of them. So $n\equiv0$ or $-1\pmod{125}$ and $n\equiv0$ or $-1\pmod8$. By the Chinese remainder theorem the four cases give, modulo $1000$:
\begin{itemize}
\item $n\equiv0\pmod{125}$, $n\equiv0\pmod 8$: $n\equiv0$, least $1000$;
\item $n\equiv-1\pmod{125}$, $n\equiv-1\pmod8$: $n\equiv999$;
\item $n\equiv0\pmod{125}$, $n\equiv-1\pmod8$: among $125,250,375$, the number $375=8\cdot46+7$ works;
\item $n\equiv-1\pmod{125}$, $n\equiv0\pmod8$: among $124,249,374,499,624$, the first multiple of $8$ is $624$.
\end{itemize}
The least is $n=\boxed{375}$. Check: $\dfrac{375\cdot376}{2}=70500=500\cdot141$.''',
'Triangular numbers|Chinese remainder theorem|Divisibility|Remainders and congruences',4)

b.save()
