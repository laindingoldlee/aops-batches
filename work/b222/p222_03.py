from qb import *
b=Bank('p222_03')

# ---------------- 1781845 Math is Cool, sum of base-n numerals
b.add(1781845,1,r'''In base ten, find the sum of the first fifteen terms of the sequence
\[
10_2,\ 21_3,\ 32_4,\ 43_5,\ 54_6,\ 65_7,\ 76_8,\ 87_9,\ 98_{10},\ \dots
\]
(the $k$th term is written in base $k+1$ with digits $k$ and $k-1$).''',
r'''The term in base $n$ has digits $n-1$ and $n-2$, so its value is
\[
(n-1)\cdot n+(n-2)=n^2-2 .
\]
The first fifteen terms use the bases $n=2,3,\dots,16$. Using $\sum_{n=1}^{16}n^2=\dfrac{16\cdot17\cdot33}{6}=1496$,
\[
\sum_{n=2}^{16}(n^2-2)=(1496-1)-2\cdot15=1495-30=\boxed{1465}.
\]''',
'Digits and bases|Summation|Pattern recognition',3,source=src('Math Is Cool',None,'Masters',None),
note='Math is Cool Masters (year not given). The rule for the terms (digits k and k-1 in base k+1) is stated; for bases above 10 the digits are digit symbols, as usual.')

# ---------------- 1781688 |-2n-18| >= |n^2+2n+2|
b.add(1781688,1,r'''Solve the inequality $|-2n-18|\ge|n^2+2n+2|$ for real $n$.''',
r'''Since $n^2+2n+2=(n+1)^2+1>0$, the right side is $n^2+2n+2$, and the left side is $|2n+18|$. So we need $|2n+18|\ge n^2+2n+2$, i.e.
\[
2n+18\ge n^2+2n+2\qquad\text{or}\qquad -(2n+18)\ge n^2+2n+2 .
\]
The first gives $n^2\le16$, i.e.\ $-4\le n\le4$. The second gives $n^2+4n+20\le0$, i.e.\ $(n+2)^2+16\le0$, which is impossible. Hence the solution set is
\[
\boxed{-4\le n\le4}.
\]''',
'Absolute value|Inequalities|Quadratic equations|Completing the square',3,
note='n is taken to be real (the post does not say); for integers the solutions are -4, -3, ..., 4.')

# ---------------- 1781399 2014 Chapter Target 7, cube with 2 faces of each colour
b.add(1781399,1,r'''How many distinct unit cubes are there with two faces painted red, two faces painted green and two faces painted blue? Two cubes are considered the same if one can be rotated to look like the other.''',
r'''Classify the cubes by how many colours occupy a pair of opposite faces.

\textbf{All three colours on opposite pairs.} Each pair of opposite faces has one colour; by a rotation we may put red on top and bottom, green in front and back, blue left and right. There is $1$ such cube.

\textbf{Exactly one colour on an opposite pair.} (If two colours occupy opposite pairs, so does the third, so ``exactly two'' is impossible.) Say this colour is on top and bottom; the four side faces carry the other two colours, with neither on opposite faces, so around the side the colours read $XXYY$; all such cubes are rotations of each other. The opposite colour can be chosen in $3$ ways, giving $3$ cubes.

\textbf{No colour on an opposite pair.} Each of the three pairs of opposite faces then carries two different colours, and each colour is used twice; so the three opposite pairs are coloured $\{R,G\}$, $\{G,B\}$ and $\{B,R\}$. Rotate so that red is on top and green on the bottom. The side faces form two opposite pairs coloured $\{G,B\}$ and $\{B,R\}$; rotating about the vertical axis we may assume the front-back pair is $\{G,B\}$. Choosing which of front and back is green and which of left and right is red gives $4$ arrangements, and the half-turn about the vertical axis swaps front with back and left with right at the same time, identifying them in pairs. This leaves $2$ cubes, which are mirror images of each other and are not related by a rotation.

The total is $1+3+2=\boxed{6}$.''',
'Colourings, tilings, and coverings|Casework|Symmetry',4,
source=src('MATHCOUNTS',2014,'Chapter',7,rnd='Target'),
note='Checked by computer: the 90 colourings fall into 6 orbits under the 24 rotations of the cube.')

# ---------------- 1781263 pattern 153, 165033, 166500333
b.add(1781263,1,r'''Observe that
\[
1^3+5^3+3^3=153,\qquad 16^3+50^3+33^3=165033,\qquad 166^3+500^3+333^3=166500333 .
\]
State the general pattern and prove it.''',
r'''\textbf{The pattern.} For $k=0,1,2,\dots$ let
\[
a=1\underbrace{6\cdots6}_{k},\qquad b=5\underbrace{0\cdots0}_{k},\qquad c=\underbrace{3\cdots3}_{k+1}.
\]
Then $a^3+b^3+c^3$ is the number obtained by writing $a$, $b$, $c$ one after another; for $k=3$, for instance, $1666^3+5000^3+3333^3=166650003333$.

\textbf{Proof.} Let $x=10^{k+1}$. Then
\[
a=\dfrac{x-4}{6},\qquad b=\dfrac x2,\qquad c=\dfrac{x-1}{3}
\]
(for example $\dfrac{1000-4}{6}=166$, $\dfrac{1000}{2}=500$, $\dfrac{999}{3}=333$). Since $b$ and $c$ both have exactly $k+1$ digits, writing $a,b,c$ one after another gives the number $ax^2+bx+c$. Now
\[
216\left(a^3+b^3+c^3\right)=(x-4)^3+27x^3+8(x-1)^3=36x^3-36x^2+72x-72,
\]
so $a^3+b^3+c^3=\dfrac{x^3-x^2+2x-2}{6}$. On the other hand
\[
ax^2+bx+c=\dfrac{(x-4)x^2}{6}+\dfrac{x^2}{2}+\dfrac{x-1}{3}=\dfrac{x^3-4x^2+3x^2+2x-2}{6}=\dfrac{x^3-x^2+2x-2}{6}.
\]
The two expressions are equal, which proves the pattern for every $k\ge0$. $\blacksquare$''',
'Algebraic expressions and identities|Place value|Pattern recognition|Digit problems',5,
note='The post asks what the pattern is; the record states it and asks for a proof (checked for k = 0 to 30).')

# ---------------- 1780934 board of directors, 6 enemies each
b.add(1780934,1,r'''A company's board of directors has $20$ members. Each member has exactly $6$ enemies on the board, and all other members are his or her friends (friendship and enmity are mutual). In how many ways can a $3$-member subcommittee be formed whose members are either all mutual friends or all mutual enemies?''',
r'''There are $\dbinom{20}{3}=1140$ subcommittees. Call one \emph{mixed} if it contains both a friendly pair and a hostile pair. In a mixed triple, exactly two of its three members have one friend and one enemy among the other two (if the pairs are, say, friend, friend, enemy, the two members on the hostile pair are these two).

Count pairs (member $v$, mixed triple containing $v$ in which $v$ has one friend and one enemy). Each member has $6$ enemies and $13$ friends, so $v$ can be completed to such a triple in $6\cdot13=78$ ways. Summing over the $20$ members gives $20\cdot78=1560$, and each mixed triple is counted exactly twice, so there are $\dfrac{1560}{2}=780$ mixed triples.

The remaining triples are all friends or all enemies:
\[
1140-780=\boxed{360}.
\]''',
'Graph theory|Double counting|Complementary counting|Combinations',5,
note='Answer 360 as in the post.')

# ---------------- 1635242 Q1, Q2
b.add(1635242,1,r'''What is the least positive integer $n$ such that $28n$ is divisible by $365$?''',
r'''Factor: $28=2^2\cdot7$ and $365=5\cdot73$. These have no common prime factor, so $\gcd(28,365)=1$, and $365\mid28n$ forces $365\mid n$. The least positive $n$ is $\boxed{365}$.''',
'Divisibility|Prime factorisation|HCF and LCM',2,
note='The post writes "28(n)"; read as 28 times n.')
b.add(1635242,2,r'''A certain type of fabric is woven from threads spaced so that there are $120$ threads per inch in each of two perpendicular directions. How many square inches of fabric can be woven with $20$ yards of thread?''',
r'''A $1$-inch by $1$-inch square of fabric contains $120$ threads of length $1$ inch running one way and $120$ running the other way, so it uses $240$ inches of thread. The thread available is $20$ yards $=20\cdot36=720$ inches, enough for
\[
\dfrac{720}{240}=\boxed{3}
\]
square inches of fabric.''',
'Unit conversion|Rates|Ratios, proportions, and variation',3)

# ---------------- 1777432 cube colourings, adjacent faces different
b.add(1777432,1,r'''Six different colours are available. In how many distinguishable ways can the faces of a cube be painted, each face with one colour (not all colours need be used), so that any two faces sharing an edge have different colours? Two colourings are the same if one can be rotated into the other. In particular, explain why exactly $30$ of these colourings use all six colours.''',
r'''Faces sharing an edge must differ, so two faces can have the same colour only if they are opposite. Classify by the number of colours used.

\textbf{Six colours.} All faces differ. There are $6!=720$ ways to colour the fixed faces, and the cube has $24$ rotations; a rotation other than the identity moves some face to a different position, so it cannot fix a colouring with six different colours. Hence the $720$ colourings fall into classes of exactly $24$, giving $\dfrac{720}{24}=30$. (This is why the solution writes $\dfrac{6!}{4!}$: here $4!=24$ happens to equal the number of rotations.)

\textbf{Five colours.} Exactly one pair of opposite faces has the same colour. Choose the $5$ colours ($6$ ways) and the colour of the pair ($5$ ways); put that pair on top and bottom. The remaining $4$ colours go around the side: there are $4!=24$ arrangements, and the $8$ rotations preserving the top-bottom pair (turns about the vertical axis, and half-turns that swap top and bottom) act freely, giving $3$. Total $6\cdot5\cdot3=90$.

\textbf{Four colours.} Exactly two pairs of opposite faces are monochromatic. Choose the $4$ colours ($15$ ways) and the two colours of the monochromatic pairs ($6$ ways); the remaining two colours go on the last opposite pair. All such colourings are rotations of each other, giving $15\cdot6=90$.

\textbf{Three colours.} All three opposite pairs are monochromatic: $\dbinom63=20$ ways.

Fewer than three colours is impossible, since the three faces at a vertex are pairwise adjacent. The total is $30+90+90+20=\boxed{230}$.''',
'Colourings, tilings, and coverings|Casework|Symmetry|Combinations',5,
note='The post asks only why 6!/4! appears for six colours; the record asks for the whole count (230) and for that explanation. The count was checked by computer (orbits of proper colourings under the 24 rotations).')

# ---------------- 1682685 linear equation
b.add(1682685,1,r'''Subtracting three from two times a number gives three more than four times that number. What is the number?''',
r'''Let the number be $x$. Then $2x-3=4x+3$, so $-2x=6$ and $x=\boxed{-3}$. (Check: $2(-3)-3=-9$ and $4(-3)+3=-9$.)''',
'Linear equations',1)

# ---------------- 1638802 students talking, standing, reading
b.add(1638802,1,r'''In a classroom, $9$ students are talking, $5$ are standing and $4$ are reading (a student may do more than one of these things, for example stand while reading or talking). Exactly one student is standing and not talking, and exactly one student is reading and not talking. Every student is talking, standing or reading. What is the smallest possible number of students in the room?''',
r'''Every student who is not talking is standing or reading. The non-talking students who stand: exactly one; the non-talking students who read: exactly one. So there is at least one and at most two non-talking students, and exactly one if the same student both stands and reads without talking. Hence the number of students is at least $9+1=10$.

$10$ is possible: let student $S$ stand and read without talking, and let the $9$ talking students include $4$ who stand and $3$ who read. Then $9$ students talk, $1+4=5$ stand and $1+3=4$ read, as required. The smallest possible number is $\boxed{10}$. (If the two non-talking students had to be different, the answer would be $11$.)''',
'Venn diagrams|Sets and inclusion–exclusion|Logical deduction|Bounding and extremal cases',3,
note='The post does not say whether a student can do two things at once or whether every student does one of the three things; the record states these assumptions (overlaps allowed; everyone talks, stands or reads). Then the answer is 10; the solution notes that 11 results if the two non-talking students must differ.')

# ---------------- 1780409 smallest product
b.add(1780409,1,r'''What is the smallest product that can be obtained by multiplying three different numbers from the set $\{1,2,0,-3,-2\}$?''',
r'''A product of three different numbers from the set is negative only if exactly one factor is negative (there are only two negative numbers, and a factor $0$ gives $0$). With one negative factor, the product is as small as possible when the negative factor has the largest size and the two positive factors are as large as possible: the set has only the positives $1$ and $2$. So the smallest product is
\[
(-3)\cdot2\cdot1=\boxed{-6}.
\]
(The other candidate with one negative factor is $(-2)\cdot2\cdot1=-4$; products with two negative factors are positive.)''',
'Whole-number operations|Bounding and extremal cases|Casework',1,
note='The poster\'s answer -6 is correct.')

# ---------------- 1777350 2017 Chapter Sprint 29, coins
b.add(1777350,1,r'''Yu has $12$ coins: $5$ pennies, $4$ nickels and $3$ dimes. He tosses them all in the air. What is the probability that the total value of the coins that land heads up is exactly $30$ cents? Express your answer as a common fraction.''',
r'''Each of the $2^{12}=4096$ outcomes (which coins show heads) is equally likely. Let $p$, $n$, $d$ be the numbers of pennies, nickels and dimes showing heads; we need $p+5n+10d=30$. Since $p\le5$ and $p$ must be a multiple of $5$, $p=0$ or $p=5$.
\begin{itemize}
\item $p=0$: $5n+10d=30$, i.e.\ $n+2d=6$: $(n,d)=(0,3),(2,2),(4,1)$, giving $\dbinom40\dbinom33+\dbinom42\dbinom32+\dbinom44\dbinom31=1+18+3=22$ outcomes.
\item $p=5$: $n+2d=5$: $(n,d)=(1,2),(3,1)$ ($n=5$ is impossible), giving $\dbinom41\dbinom32+\dbinom43\dbinom31=12+12=24$ outcomes.
\end{itemize}
In total $22+24=46$ outcomes, and the probability is $\dfrac{46}{4096}=\boxed{\dfrac{23}{2048}}$.''',
'Probability|Casework|Combinations|Money and currency',4,
source=src('MATHCOUNTS',2017,'Chapter',29,rnd='Sprint'))

# ---------------- 1780414 magic box
b.add(1780414,1,r'''A magic box contains $n=3p+1$ balls, where $p$ is a positive integer. Each time we take $1$ ball out of the box, $2$ more balls vanish from the box (if fewer than $2$ balls remain, all of them vanish). How many times can we take a ball out of the box? Express the answer in terms of $p$.''',
r'''Each removal of a ball (with the two vanishing balls) lowers the number of balls by $3$, as long as at least $3$ balls are present. After $p$ removals, $3p+1-3p=1$ ball is left. We can take this ball out too (nothing remains to vanish), and then the box is empty. So we can take a ball out $\boxed{p+1}$ times.

(If one insisted that a ball may be taken only when two other balls can vanish, the last ball could not be taken and the answer would be $p$; in no reading is it $p-1$.)''',
'Process simulation|Remainders and congruences',2,
note='The post asks whether the answer is p-1. The rule for the last ball is made explicit; under it the answer is p+1 (p if the last single ball may not be taken). p-1 is not correct under either reading.')

# ---------------- 1779767 Alice, Blice, Clice
b.add(1779767,1,r'''Alice, Blice and Clice each arrive at a park at a time chosen uniformly at random between 6 AM and 6 PM, independently. Each of them stays for exactly $3$ hours and then leaves. What is the probability that at least two of them meet each other?''',
r'''Measure time in hours from 6 AM, so the arrival times $x,y,z$ are independent and uniform on $[0,12]$. Two people meet exactly when their arrival times differ by less than $3$ (they may stay after 6 PM; meeting at a single instant has probability $0$).

Use the complement: nobody meets when all pairwise differences are at least $3$. For the ordering $x<y<z$ this means $y\ge x+3$ and $z\ge y+3$. Substituting $y'=y-3$, $z'=z-6$ turns this region into $0\le x\le y'\le z'\le6$, which has volume $\dfrac{6^3}{3!}=36$. There are $3!=6$ orderings, so the region where nobody meets has volume $6\cdot36=216$, out of $12^3=1728$. Hence
\[
P(\text{at least two meet})=1-\dfrac{216}{1728}=1-\dfrac18=\boxed{\dfrac78},
\]
confirming the poster's answer.''',
'Geometric probability|Complementary probability|Probability',5,
note='The poster\'s answer 7/8 is correct. The record assumes independent arrivals and that a person may stay after 6 PM (as the post implies). Checked by Monte Carlo simulation.')

# ---------------- 1780335 digit 1 from 1 to 100
b.add(1780335,1,r'''If we write the numbers from $1$ to $100$ one after another, how many times is the digit $1$ written?''',
r'''Count by position. Units digit $1$: $1,11,21,\dots,91$, which is $10$ numbers. Tens digit $1$: $10,11,\dots,19$, another $10$ (the number $11$ is counted once in each list, correctly, since it contains two $1$s). Hundreds digit $1$: only $100$. In total $10+10+1=\boxed{21}$.''',
'Place value|Systematic counting|Digit problems',1)

# ---------------- 1780203 four discarded mock MATHCOUNTS problems
b.add(1780203,1,r'''Randell writes down the largest integer $m$ such that $2^m$ divides $12!$ and the largest integer $n$ such that $3^n$ divides $18!$. Find the sum of the two numbers Randell writes.''',
r'''By Legendre's formula,
\[
m=\left\lfloor\dfrac{12}{2}\right\rfloor+\left\lfloor\dfrac{12}{4}\right\rfloor+\left\lfloor\dfrac{12}{8}\right\rfloor=6+3+1=10,\qquad
n=\left\lfloor\dfrac{18}{3}\right\rfloor+\left\lfloor\dfrac{18}{9}\right\rfloor=6+2=8 .
\]
The sum is $10+8=\boxed{18}$.''',
'Factorials|Prime factorisation|Floor and ceiling functions',2,
note='The post writes "2m divides 12!" and "3n divides 18!", which are lost exponents (as written, m would be 12!/2); read as 2^m and 3^n.')
b.add(1780203,2,r'''Three real numbers $a,b,c$ are selected randomly and independently from the interval $[0,100]$. Find the probability that $100\le a+b+c\le200$.''',
r'''Scale by $100$: $x,y,z$ are uniform on $[0,1]$ and we need $1\le x+y+z\le2$. The point $(x,y,z)$ is uniform in the unit cube. The region $x+y+z<1$ is the corner tetrahedron with volume $\dfrac16$, and by the symmetry $(x,y,z)\mapsto(1-x,1-y,1-z)$ the region $x+y+z>2$ also has volume $\dfrac16$. The probability is
\[
1-\dfrac16-\dfrac16=\boxed{\dfrac23}.
\]''',
'Geometric probability|Complementary probability|Symmetry',4)
b.add(1780203,3,r'''Find the sum of all real solutions of
\[
\dfrac{|x^2+5x+6|}{x^2}=\dfrac16 .
\]''',
r'''The equation says $6\,|x^2+5x+6|=x^2$ with $x\ne0$. Note $x^2+5x+6=(x+2)(x+3)$.

\textbf{Case $(x+2)(x+3)\ge0$} ($x\le-3$ or $x\ge-2$): $6x^2+30x+36=x^2$, i.e.\ $5x^2+30x+36=0$, with roots $x=-3\pm\dfrac{3\sqrt5}{5}$. Since $\dfrac{3\sqrt5}{5}\approx1.34$, the roots are about $-1.66\ge-2$ and $-4.34\le-3$: both satisfy the case condition.

\textbf{Case $-3<x<-2$:} $-6x^2-30x-36=x^2$, i.e.\ $7x^2+30x+36=0$, with discriminant $900-1008<0$: no roots.

The solutions are $-3\pm\dfrac{3\sqrt5}{5}$, and their sum is $\boxed{-6}$.''',
'Absolute value|Quadratic equations|Rational equations|Casework',3)
fig=r'''real k=2/sqrt(21),h=4;
pair V=(0,h);
real yc=h*(1-k);
real t0=degrees(asin(0.15));
draw(scale(3,0.6)*arc((0,0),1,t0,180-t0),dashed);draw(scale(3,0.6)*arc((0,0),1,180-t0,360+t0),linewidth(0.9));
draw(shift(0,yc)*scale(3k,0.6k)*arc((0,0),1,t0,180-t0),dashed);
draw(shift(0,yc)*scale(3k,0.6k)*arc((0,0),1,180-t0,360+t0),blue+linewidth(0.9));
draw((-3*Cos(t0),0.6*Sin(t0))--V--(3*Cos(t0),0.6*Sin(t0)),linewidth(0.9));
draw((0,0)--(3,0),dashed);draw((0,0)--V,dashed);
dot((0,0));dot((0,yc));
label("$3$",(1.5,-0.2),fontsize(8pt));label("$5$",(2.3,1.0),E);
draw((3.8,0)--(3.8,yc),Arrows(4));draw((3.1,0)--(4,0),dotted);draw((3k+0.2,yc)--(4,yc),dotted);
label("$d$",(3.8,yc/2),E);label("$V$",V,N);'''
b.add(1780203,4,r'''A cone has base radius $3$ and slant height $5$. A plane parallel to the base cuts the cone into a smaller cone and a frustum whose total surface areas are in the ratio $1:5$. Find the distance from the plane to the base.''',
r'''The cone has height $\sqrt{5^2-3^2}=4$. Its lateral area is $\pi\cdot3\cdot5=15\pi$ and its base area is $9\pi$. Let the small cone (with the same apex $V$) be similar to the whole cone with ratio $k$, $0<k<1$.
'''+asy(fig,'5cm')+r'''
The small cone has radius $3k$ and slant height $5k$, so its total surface area is $15\pi k^2+9\pi k^2=24\pi k^2$. The frustum has lateral area $15\pi-15\pi k^2$, bottom $9\pi$ and top $9\pi k^2$, in total $24\pi-6\pi k^2$. The condition is
\[
\dfrac{24k^2}{24-6k^2}=\dfrac15\ \Longrightarrow\ 120k^2=24-6k^2\ \Longrightarrow\ k^2=\dfrac{4}{21},\quad k=\dfrac{2}{\sqrt{21}} .
\]
(The reverse ratio $5:1$ would need $k^2=\dfrac{20}{9}>1$, which is impossible, so the configuration is unique.) The plane is at height $4k$ below the apex, so its distance to the base is
\[
d=4-4k=4-\dfrac{8}{\sqrt{21}}=\boxed{4-\dfrac{8\sqrt{21}}{21}}\approx2.25 .
\]''',
'Cones|Surface area|Scaling of length, area, and volume|Similarity',4,
note='The post asks for "the smallest distance from the plane to the base"; the distance is unique (the reverse ratio is impossible), as the solution shows. Total surface areas (including the bases) are used.')

# ---------------- 1779907 three-digit numbers with no two consecutive equal digits
b.add(1779907,1,r'''Find the number of three-digit numbers (integers from $100$ to $999$) in which no two consecutive digits are equal.''',
r'''Choose the digits from left to right. The hundreds digit can be any of $1,\dots,9$: $9$ choices. The tens digit can be any of the $10$ digits except the hundreds digit: $9$ choices. The units digit can be anything except the tens digit: $9$ choices. By the multiplication principle there are $9\cdot9\cdot9=\boxed{729}$ such numbers.''',
'Multiplication principle|Digit problems',2,
note='From Combinatorics: A Problem Oriented Approach by D. A. Marcus (as the post says; not a contest).')

# ---------------- 1779636 days until June 21
b.add(1779636,1,r'''In 2014, the longest day of the year for a Seattle resident was June 21st. If today is Friday, April 18th, 2014, how many days are there until the longest day of the year?''',
r'''From April 18 to April 30 there are $30-18=12$ days, May has $31$ days, and from May 31 to June 21 there are $21$ more days. In total
\[
12+31+21=\boxed{64}
\]
days. (Check with the weekday: $64=9\cdot7+1$, so June 21 is one weekday after Friday, a Saturday, which is correct for 2014.)''',
'Date and time|Calendar and clock problems',1)

b.save()
