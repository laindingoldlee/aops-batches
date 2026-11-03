from qb import *
b=Bank('p223_01')

# ---------------- 1779396 product of logs
b.add(1779396,1,r'''Evaluate $(\log_2 9)(\log_3 7)(\log_7 8)$.''',
r'''Write every logarithm in terms of natural logarithms (change of base):
\[
(\log_2 9)(\log_3 7)(\log_7 8)=\dfrac{\ln 9}{\ln 2}\cdot\dfrac{\ln 7}{\ln 3}\cdot\dfrac{\ln 8}{\ln 7}
=\dfrac{2\ln 3}{\ln 2}\cdot\dfrac{\ln 7}{\ln 3}\cdot\dfrac{3\ln 2}{\ln 7}=2\cdot3=\boxed{6}.
\]''',
'Logarithms',2,
note='KPMT problem; the post writes Log_2 9 etc. without LaTeX.')

# ---------------- 1780033 2014 Chapter Sprint: rectangle (alias, in-batch) and triangles
b.add(1780033,1,r'''The length of the diagonal of rectangle $ABCD$ equals half the rectangle's perimeter less four-fifths of the length of the shorter side. What is the ratio of the length of the shorter side of the rectangle to the length of its longer side? Express your answer as a common fraction.''',
r'''Let the longer side be $l$ and the shorter side $w$. Half the perimeter is $l+w$, and ``less four-fifths of the shorter side'' means subtract $\dfrac45w$. So the diagonal is $l+w-\dfrac45w=l+\dfrac w5$, and by the Pythagorean theorem
\[
l^2+w^2=\left(l+\dfrac w5\right)^2=l^2+\dfrac{2lw}{5}+\dfrac{w^2}{25}.
\]
Hence $\dfrac{24}{25}w^2=\dfrac25lw$, so $\dfrac wl=\dfrac25\cdot\dfrac{25}{24}=\boxed{\dfrac{5}{12}}$. (Check: a $5$ by $12$ rectangle has diagonal $13=12+1$.)''',
'Rectangles|Pythagorean theorem|Ratios, proportions, and variation',2,source=src('MATHCOUNTS',2014,'Chapter',22,rnd='Sprint'),
note='2014 MATHCOUNTS Chapter Sprint #22; the same problem is posted in topic 1777483 of this batch (aliased to it).')
b.add(1780033,2,r'''How many different combinations of three numbers can be selected from the set $\{1,2,3,4,5,6,7,8\}$ so that the three numbers could be the side lengths of a triangle?''',
r'''Choose three different numbers $a<b<c$. They are the sides of a (non-degenerate) triangle exactly when $a+b>c$; the other two triangle inequalities hold automatically. Count by the largest number $c$, listing pairs $a<b<c$ with $a+b>c$:
\begin{itemize}
\item $c=4$: $(2,3)$; $1$ set.
\item $c=5$: $(2,4),(3,4)$; $2$ sets.
\item $c=6$: $(2,5),(3,4),(3,5),(4,5)$; $4$ sets.
\item $c=7$: $(2,6),(3,5),(3,6),(4,5),(4,6),(5,6)$; $6$ sets.
\item $c=8$: $(2,7),(3,6),(3,7),(4,5),(4,6),(4,7),(5,6),(5,7),(6,7)$; $9$ sets.
\end{itemize}
($c\le3$ gives nothing, since $1+2=3$.) The total is $1+2+4+6+9=\boxed{22}$.''',
'Triangle inequality|Systematic counting|Casework',3,source=src('MATHCOUNTS',2014,'Chapter',26,rnd='Sprint'),
note='Second problem of the post (2014 Chapter Sprint #26, as identified in the earlier record); repeat of an earlier record (aliased). "Combinations of three numbers" read as three different numbers from the set; degenerate triangles are excluded. Count checked by computer.')

# ---------------- 1779918 words with A and B
b.add(1779918,1,r'''Find the number of five-letter words that use letters from the set $\{A,B,C\}$ and contain at least one $A$ and at least one $B$.''',
r'''There are $3^5=243$ words in all. By inclusion--exclusion, remove the $2^5=32$ words with no $A$ and the $2^5=32$ words with no $B$, and add back the $1$ word ($CCCCC$) with neither:
\[
243-32-32+1=\boxed{180}.
\]''',
'Sets and inclusion–exclusion|Complementary counting|Multiplication principle',2)

# ---------------- 1779794 three algebra problems
b.add(1779794,1,r'''The numbers $a$ and $b$ are rational, and one of the roots of $9x^2+ax-b=0$ is $\dfrac{-2-\sqrt6}{3}$. Solve the equation $bx^2-ax+16=0$.''',
r'''Since the coefficients are rational and $\dfrac{-2-\sqrt6}{3}$ is irrational, the other root is its conjugate $\dfrac{-2+\sqrt6}{3}$. (Indeed, if $r=\dfrac{-2-\sqrt6}{3}$, then $(3r+2)^2=6$, i.e.\ $9r^2+12r-2=0$; subtracting $9r^2+ar-b=0$ gives $(12-a)r=2-b$, and since $r$ is irrational, $a=12$ and $b=2$.) By Vieta's formulas the sum of the roots is $-\dfrac43=-\dfrac a9$ and the product is $\dfrac{4-6}{9}=-\dfrac29=-\dfrac b9$, so $a=12$ and $b=2$.

The second equation is $2x^2-12x+16=0$, i.e.\ $x^2-6x+8=(x-2)(x-4)=0$. So $x=\boxed{2\text{ or }4}$.''',
'Quadratic equations|Vieta\'s formulas|Radicals',3,
note='The post does not say that a and b are rational (needed for the conjugate root); this is added. "Find x" read as solving the second equation (both roots given).')
b.add(1779794,2,r'''For a positive integer $x$, let $\langle x\rangle$ denote the number of primes less than or equal to $x$. Find the sum of all positive integers $x$ such that
\[
\left(\langle x\rangle+1\right)^2-2\left(\langle x\rangle+4\right)-9=0 .
\]''',
r'''Let $p=\langle x\rangle$. The equation is $p^2+2p+1-2p-8-9=0$, i.e.\ $p^2=16$, so $p=4$ (a count is nonnegative). The primes up to $x$ are $2,3,5,7$ exactly when $7\le x<11$, i.e.\ $x\in\{7,8,9,10\}$. The sum is $7+8+9+10=\boxed{34}$.''',
'Prime numbers|Quadratic equations',2,
note='The post says <x> "represents the prime numbers less than or equal to x"; read as the number of such primes.')
b.add(1779794,3,r'''A bowl contains $100$ g of salt water with a salt concentration of $20\%$. We take out $x$ g of the mixture and then add $x$ g of water. Then we again take out $x$ g of the (well-mixed) salt water and add $x$ g of water. Now the concentration is $5\%$. Find $x$.''',
r'''Each step keeps the total mass $100$ g and removes the fraction $\dfrac{x}{100}$ of the salt present, so it multiplies the concentration by $1-\dfrac{x}{100}$. After two steps
\[
20\left(1-\dfrac{x}{100}\right)^2=5\ \Longrightarrow\ \left(1-\dfrac{x}{100}\right)^2=\dfrac14\ \Longrightarrow\ 1-\dfrac{x}{100}=\dfrac12
\]
(the value must lie between $0$ and $1$). Hence $x=\boxed{50}$. Check: $20$ g of salt becomes $10$ g, then $5$ g, in $100$ g of water: $5\%$.''',
'Mixture problems|Percentages|Quadratic equations',3)

# ---------------- 1779655 base conversion
b.add(1779655,1,r'''Convert $213_6$ (the number written $213$ in base $6$) to base $4$.''',
r'''First convert to base $10$: $213_6=2\cdot6^2+1\cdot6+3=72+6+3=81$. Then write $81$ in base $4$ using the powers $1,4,16,64$: $81=1\cdot64+17=1\cdot64+1\cdot16+1=1\cdot64+1\cdot16+0\cdot4+1$. So $213_6=\boxed{1101_4}$.

(Repeated division gives the same digits: $81=4\cdot20+1$, $20=4\cdot5+0$, $5=4\cdot1+1$, $1=4\cdot0+1$; reading the remainders upwards gives $1101$.)''',
'Digits and bases',1,
note='The post asks how to convert between bases, with the example 213 in base 6 to base 4; that example is the question.')

# ---------------- 1779563 2019-gon
fig=r'''int n=12; real R=1; real r=R*cos(pi/n);
pair O=(0,0);
pair[] P; for(int k=0;k<n;++k) P.push(R*dir(90+360*k/n));
path g=P[0]; for(int k=1;k<n;++k) g=g--P[k]; g=g--cycle;
draw(g,linewidth(0.9));
draw(circle(O,r),dashed+gray);
pair Mid=(P[6]+P[7])/2;
draw(O--Mid,blue+linewidth(0.7)); draw(O--P[7],dashed);
dot(O); label("$O$",O,N);
label("$r$",(O+Mid)/2,dir(degrees(Mid-O)-90),blue);
label("$R$",(O+P[7])/2,dir(degrees(P[7]-O)+90));
pair u=unit(P[7]-P[6]); pair v=(-u.y,u.x);
draw(Mid+0.05*u--Mid+0.05*u+0.05*v--Mid+0.05*v);'''
b.add(1779563,1,r'''A regular $2019$-gon has perimeter $2\pi$. Find its area, rounded to the nearest integer.''',
r'''Let $n=2019$, let $R$ be the circumradius and $r$ the inradius (apothem) of the polygon. The figure shows a regular $12$-gon with the same notation; $O$ is the centre and the dashed circle is the incircle.
'''+asy(fig,'5cm')+r'''
Cutting the polygon into $n$ triangles with apex $O$, each with base a side and height $r$, gives
\[
\text{Area}=\dfrac12\cdot(\text{perimeter})\cdot r=\dfrac12\cdot2\pi\cdot r=\pi r .
\]
\textbf{Upper bound.} The polygon contains its incircle, and its perimeter is longer than the circumference of that circle, so $2\pi>2\pi r$, i.e.\ $r<1$.

\textbf{Lower bound.} The polygon is inscribed in its circumcircle, so its perimeter is shorter than that circumference: $2\pi<2\pi R$, i.e.\ $R>1$. Also $r=R\cos\dfrac{\pi}{n}$ and $\dfrac\pi n<0.01$, so $r>\cos0.01>1-\dfrac{0.01^2}{2}>0.99$.

Hence $3.11<0.99\pi<\text{Area}<\pi<3.15$, and the area to the nearest integer is $\boxed{3}$. (Exactly, the area is $\dfrac{\pi^2}{n}\cot\dfrac{\pi}{n}\approx3.14159$, extremely close to the area $\pi$ of a circle of perimeter $2\pi$.)''',
'Regular polygons|Lengths, perimeter, and area|Circles|Estimation',3,
note='The post does not say "regular"; a 2019-gon of perimeter 2pi can have any area in (0, pi), so the polygon is taken to be regular. The figure illustrates the notation with a 12-gon.')

# ---------------- 1779468 four challenge questions
b.add(1779468,1,r'''The sequence $1,\ 1\dfrac12,\ 1\dfrac56,\ 2\dfrac1{12},\ \dots$ is formed by adding $\dfrac12$, then $\dfrac13$, then $\dfrac14$, and so on. Find the next two terms.''',
r'''The terms are the partial sums $1$, $1+\dfrac12$, $1+\dfrac12+\dfrac13$, $1+\dfrac12+\dfrac13+\dfrac14$: indeed $1+\dfrac12=1\dfrac12$, $1\dfrac12+\dfrac13=1\dfrac56$ and $1\dfrac56+\dfrac14=\dfrac{25}{12}=2\dfrac1{12}$. The next two terms are
\[
2\dfrac1{12}+\dfrac15=\dfrac{125+12}{60}=\dfrac{137}{60}=2\dfrac{17}{60}\qquad\text{and}\qquad\dfrac{137}{60}+\dfrac16=\dfrac{147}{60}=\dfrac{49}{20}=2\dfrac{9}{20}.
\]
So the next two terms are $\boxed{2\dfrac{17}{60}\text{ and }2\dfrac{9}{20}}$.''',
'Sequences and series|Fractions|Pattern recognition',2,
note='The post only asks for the next two numbers of 1, 1 1/2, 1 5/6, 2 1/12; the rule (harmonic partial sums, which these four terms fit) is stated in the question so that the answer is determined.')
b.add(1779468,2,r'''If $a$, $b$, $c$ and $d$ are four distinct integers between $-5.5$ and $4.5$, what is the greatest possible value of $\dfrac ab-cd$?''',
r'''The integers available are $-5,-4,\dots,4$, and $b\ne0$.

\textbf{Bounds.} Always $\dfrac ab\le|a|\le5$, and $\dfrac ab=5$ only for $a=-5,\ b=-1$. Also $cd\ge-20$, with $cd=-20$ only for $\{c,d\}=\{-5,4\}$.
\begin{itemize}
\item If $-5\in\{c,d\}$, then $a\ne-5$, so $\dfrac ab\le4$ (as $|a|\le4$), and $-cd\le20$: the value is at most $24$.
\item If $-5\notin\{c,d\}$, then $c,d\in\{-4,\dots,4\}$ are distinct, so $cd\ge-16$ (the most negative product is $-4\cdot4$), and $\dfrac ab\le5$: the value is at most $21$.
\end{itemize}
The value $24$ is attained by $a=-4$, $b=-1$, $c=4$, $d=-5$: $\dfrac{-4}{-1}-(4)(-5)=4+20=24$. The greatest value is $\boxed{24}$.''',
'Bounding and extremal cases|Casework|Fractions',3,
note='Answer confirmed by checking all choices of four distinct integers.')
b.add(1779468,3,r'''On day $1$ you have $100$ dollars. On day $2$ you earn $1$ dollar, on day $3$ you lose $2$ dollars, on day $4$ you earn $2$ dollars, on day $5$ you lose $3$ dollars, on day $6$ you earn $3$ dollars, and so on (on day $2k$ you earn $k$ dollars and on day $2k+1$ you lose $k+1$ dollars). On which day do you first run out of money?''',
r'''Look at the money at the end of each odd day $2k+1$ ($k\ge1$). Days $2k$ and $2k+1$ together change the money by $k-(k+1)=-1$. So at the end of day $2k+1$ you have $100-k$ dollars, and at the end of day $2k+2$ you have $100-k+(k+1)=101$ dollars. Thus the amount is never below $100-k$ before the end of day $2k+1$, and it first reaches $0$ when $100-k=0$, i.e.\ $k=100$, at the end of day $2\cdot100+1=\boxed{201}$.

(Just before, at the end of day $200$, you have $101$ dollars and on day $201$ you lose $101$.)''',
'Sequences and series|Pattern recognition|Money and currency',2,
note='The phrase "the number of days it takes" is read as the day on which the money first reaches 0. Checked by simulation.')
b.add(1779468,4,r'''You pick a number from $1$ to $6$ and then roll two fair six-sided dice. If your number does not show on either die, you lose $1$ dollar; if it shows on exactly one die, you win $2$ dollars; if it shows on both dice, you win $5$ dollars. Find your expected winnings per game. Is the game favourable, unfavourable or fair?''',
r'''For a fixed number, each die shows it with probability $\dfrac16$, independently. So
\[
P(\text{none})=\dfrac{25}{36},\qquad P(\text{exactly one})=2\cdot\dfrac16\cdot\dfrac56=\dfrac{10}{36},\qquad P(\text{both})=\dfrac1{36}.
\]
The expected winnings are
\[
\dfrac{25}{36}(-1)+\dfrac{10}{36}(2)+\dfrac1{36}(5)=\dfrac{-25+20+5}{36}=\boxed{0}.
\]
The game is \textbf{fair}: on average you neither win nor lose, so there is no advantage in playing (or in refusing).''',
'Expected value|Dice probability|Independent events',2,
note='"Should you play the game?" made precise as computing the expected value.')

# ---------------- 1779434 dice arithmetic sequence (alias)
b.add(1779434,1,r'''Three standard six-sided dice are rolled. What is the probability that the three numbers showing can be arranged to form an arithmetic sequence? (For example, $(1,3,2)$ counts, since $1,2,3$ is an arithmetic sequence; a constant sequence such as $4,4,4$ also counts.)''',
r'''Count ordered outcomes. Constant sequences: $6$ outcomes. Common difference $1$: the sets $\{1,2,3\},\{2,3,4\},\{3,4,5\},\{4,5,6\}$; difference $2$: $\{1,3,5\},\{2,4,6\}$. Each of these $6$ sets of three different numbers appears in $3!=6$ orders, giving $36$ outcomes. The probability is $\dfrac{6+36}{216}=\boxed{\dfrac{7}{36}}$.''',
'Probability|Arithmetic sequences|Dice probability|Systematic counting',2,
note='Repeat of an earlier record (aliased). Constant sequences counted as arithmetic.')

# ---------------- 1779285 Intro Geometry 3.20
figq=r'''pair O=(0,0);
pair A=dir(260),B=dir(128),C=dir(52),D=dir(-24);
draw(unitcircle,linewidth(0.7));
draw(A--B--C--D,linewidth(0.9));
draw(B--O--C,linewidth(0.7));
dot(O);dot(A);dot(B);dot(C);dot(D);
label("$O$",O,S);label("$A$",A,dir(260));label("$B$",B,dir(128));label("$C$",C,dir(52));label("$D$",D,dir(-24));
draw(arc(B,0.45,-76,-52),linewidth(0.6));
label("$24^\circ$",B+0.74*dir(-64));'''
figs=r'''pair O=(0,0);
pair A=dir(260),B=dir(128),C=dir(52),D=dir(-24);
draw(unitcircle,linewidth(0.7));
draw(A--B--C--D,linewidth(0.9));
draw(B--O--C,linewidth(0.7));
dot(O);dot(A);dot(B);dot(C);dot(D);
label("$O$",O,S);label("$A$",A,dir(260));label("$B$",B,dir(128));label("$C$",C,dir(52));label("$D$",D,dir(-24));
draw(arc(B,0.45,-76,-52),linewidth(0.6));
label("$24^\circ$",B+0.74*dir(-64));
draw(arc(B,0.3,-52,0),blue+linewidth(0.6)); label("$x$",B+0.4*dir(-26),blue);
draw(arc(C,0.3,180,232),blue+linewidth(0.6)); label("$x$",C+0.4*dir(206),blue);
draw(arc(C,0.22,232,284),blue+linewidth(0.6)); label("$x$",C+0.32*dir(258),blue);'''
b.add(1779285,1,r'''In the diagram, $O$ is the centre of the circle and $A$, $B$, $C$, $D$ lie on the circle. Chords $AB$ and $CD$ are parallel, $\angle ABO=24^\circ$, and $\angle OBC=\angle OCD$. Find $\angle BOC$.
'''+asy(figq,'6cm'),
r'''Let $\angle OBC=\angle OCD=x$. Since $OB=OC$ (radii), triangle $OBC$ is isosceles and $\angle OCB=\angle OBC=x$.
'''+asy(figs,'6.5cm')+r'''
As in the figure, $O$ lies inside the angles $ABC$ and $BCD$, so
\[
\angle ABC=\angle ABO+\angle OBC=24^\circ+x,\qquad \angle BCD=\angle BCO+\angle OCD=2x .
\]
Because $AB\parallel CD$ and $A$, $D$ are on the same side of the transversal $BC$, these co-interior angles add up to $180^\circ$:
\[
24^\circ+x+2x=180^\circ\ \Longrightarrow\ x=52^\circ .
\]
Finally, in triangle $OBC$, $\angle BOC=180^\circ-2x=180^\circ-104^\circ=\boxed{76^\circ}$.''',
'Circles|Parallel lines|Isosceles triangles|Angle chasing',3,
note='AoPS Introduction to Geometry problem 3.20; the book figure is missing from the post. It was rebuilt from the text: O inside angles ABC and BCD, A and D on the same side of BC (the only configuration consistent with the data, drawn to scale from the answer).')

# ---------------- 1778686 x+1/x=5
b.add(1778686,1,r'''If $x+\dfrac1x=5$, find $x^4+\dfrac1{x^4}$.''',
r'''Square twice. From $\left(x+\dfrac1x\right)^2=x^2+2+\dfrac1{x^2}$,
\[
x^2+\dfrac1{x^2}=5^2-2=23 ,
\]
and from $\left(x^2+\dfrac1{x^2}\right)^2=x^4+2+\dfrac1{x^4}$,
\[
x^4+\dfrac1{x^4}=23^2-2=\boxed{527}.
\]
In general, if $s_k=x^k+\dfrac1{x^k}$, then $s_{2k}=s_k^2-2$ and $s_{k+1}=s_1s_k-s_{k-1}$ (from multiplying $s_1$ by $s_k$), so any $s_k$ follows quickly from $s_1$.''',
'Algebraic expressions and identities|Exponents|Recurrence relations',2,
note='KPMT problem from the title; the post asks for a quick general method, given at the end of the solution.')

# ---------------- 1779038 Armstrong numbers
b.add(1779038,1,r'''There are four three-digit numbers that are equal to the sum of the cubes of their digits. Find them and their sum.''',
r'''Write the number as $100a+10b+c$ with digits $a\ge1$, $b$, $c$. The condition is
\[
100a+10b+c=a^3+b^3+c^3\iff a(100-a^2)+b(10-b^2)=c^3-c=(c-1)c(c+1).
\]
Put $f(a)=a(100-a^2)$, $g(b)=b(10-b^2)$ and $h(c)=c^3-c$. For $a=1,\dots,9$, $f(a)=99,192,273,336,375,384,357,288,171$; for $b=0,\dots,9$, $g(b)=0,9,12,3,-24,-75,-156,-273,-432,-639$; and for $c=0,\dots,9$, $h(c)=0,0,6,24,60,120,210,336,504,720$. We need $f(a)+g(b)=h(c)$. Listing $f(a)+g(b)$ for $b=0,\dots,9$:
\begin{itemize}
\item $a=1$: $99,108,111,102,75,\mathbf{24},-57,-174,-333,-540$; $24=h(3)$ gives $\mathbf{153}$.
\item $a=2$: $192,201,204,195,168,117,36,-81,-240,-447$: none.
\item $a=3$: $273,282,285,276,249,198,117,\mathbf{0},-159,-366$; $0=h(0)=h(1)$ gives $\mathbf{370}$ and $\mathbf{371}$.
\item $a=4$: $\mathbf{336},345,348,339,312,261,180,63,-96,-303$; $336=h(7)$ gives $\mathbf{407}$.
\item $a=5$: $375,384,387,378,351,300,219,102,-57,-264$: none.
\item $a=6$: $384,393,396,387,360,309,228,111,-48,-255$: none.
\item $a=7$: $357,366,369,360,333,282,201,84,-75,-282$: none.
\item $a=8$: $288,297,300,291,264,213,132,15,-144,-351$: none.
\item $a=9$: $171,180,183,174,147,96,15,-102,-261,-468$: none.
\end{itemize}
The numbers are $153,370,371,407$, and their sum is $\boxed{1301}$.''',
'Digit problems|Perfect cubes|Casework',3,
note='Narcissistic (Armstrong) numbers; the case check was confirmed by computer.')

# ---------------- 1778933 stairs 1,2,3
b.add(1778933,1,r'''David climbs a staircase of $6$ steps, taking $1$, $2$ or $3$ steps at a time. In how many ways can he get to the top?''',
r'''Let $w_n$ be the number of ways to climb $n$ steps. The last move is $1$, $2$ or $3$ steps, so $w_n=w_{n-1}+w_{n-2}+w_{n-3}$ with $w_0=1$, $w_1=1$, $w_2=2$. Then
\[
w_3=4,\quad w_4=7,\quad w_5=13,\quad w_6=24 .
\]
He can get upstairs in $\boxed{24}$ ways.''',
'Recursive counting|Recurrence relations|Partitions and compositions',2,
note='Repeat of an earlier record (aliased).')

# ---------------- 1779041 two problems
b.add(1779041,1,r'''Let real numbers $a,b,c$ satisfy $a^2+b^2+c^2=1$. Let $M$ and $m$ be the maximum and minimum values of $ab+bc+ca$. Find $M-m$.''',
r'''\textbf{Maximum.} $a^2+b^2+c^2-(ab+bc+ca)=\dfrac12\left[(a-b)^2+(b-c)^2+(c-a)^2\right]\ge0$, so $ab+bc+ca\le1$, with equality at $a=b=c=\dfrac1{\sqrt3}$. So $M=1$.

\textbf{Minimum.} $(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)=1+2(ab+bc+ca)\ge0$, so $ab+bc+ca\ge-\dfrac12$, with equality when $a+b+c=0$, e.g.\ $a=\dfrac1{\sqrt2}$, $b=-\dfrac1{\sqrt2}$, $c=0$. So $m=-\dfrac12$.

Hence $M-m=\boxed{\dfrac32}$.''',
'Inequalities|Maxima and minima|Algebraic expressions and identities',3)
b.add(1779041,2,r'''A complex number $z$ satisfies $|z-i|=2$. Find the maximum value of $|z-\overline{z}|$.''',
r'''Write $z=x+yi$. Then $z-\overline z=2yi$, so $|z-\overline z|=2|y|$. The condition says $z$ lies on the circle with centre $i$ and radius $2$, so $y$ ranges over $[1-2,\,1+2]=[-1,3]$. Hence $|y|\le3$, with $|y|=3$ at $z=3i$, and the maximum is $\boxed{6}$.''',
'Complex numbers|Maxima and minima',2,
note='The post writes "I z-i I" and "z with a bar on top"; read as |z - i| = 2 and the conjugate.')

# ---------------- 1779111 stars and bars
b.add(1779111,1,r'''A student writes that the number of ways to put $n$ indistinguishable objects into $k$ indistinguishable boxes is $\dbinom{n+k-1}{k}$, and asks whether this requires every box to get at least one object. Correct the statement, and illustrate with $n=7$ objects and $k=3$ boxes: find the number of ways when
\begin{enumerate}
\item the boxes are distinguishable and boxes may be empty;
\item the boxes are distinguishable and every box gets at least one object;
\item the boxes are indistinguishable and boxes may be empty.
\end{enumerate}''',
r'''Stars and bars counts placements of $n$ identical objects into $k$ \emph{distinguishable} boxes. A placement is a row of $n$ stars and $k-1$ bars (the bars separate the boxes), so there are $\dbinom{n+k-1}{k-1}$ of them, and \emph{empty boxes are allowed} (two adjacent bars). If every box must get at least one object, first put one object in each box and distribute the remaining $n-k$ freely: $\dbinom{n-1}{k-1}$ ways. For indistinguishable boxes there is no such binomial formula: one counts partitions of $n$ into at most $k$ parts.

For $n=7$, $k=3$:
\begin{enumerate}
\item $\dbinom{9}{2}=\boxed{36}$;
\item $\dbinom{6}{2}=\boxed{15}$;
\item the partitions of $7$ into at most $3$ parts: $7,\ 6+1,\ 5+2,\ 4+3,\ 5+1+1,\ 4+2+1,\ 3+3+1,\ 3+2+2$, so $\boxed{8}$.
\end{enumerate}''',
'Stars and bars|Distributions and integer solutions|Partitions and compositions',2,
note='Conceptual question turned into a correction of the formula (the bottom number is k - 1, the boxes must be distinguishable, and empty boxes are allowed) with a worked example n = 7, k = 3 chosen for the record.')

# ---------------- 1778662 2018 School Sprint 25 coins
b.add(1778662,1,r'''In cents, what is the least total amount that cannot be obtained by using a combination of fewer than eight coins from a collection of pennies, nickels, dimes and quarters?''',
r'''\textbf{Fewest coins for an amount.} Take a collection with the fewest coins for an amount $n$. It has at most $4$ pennies (five pennies could be replaced by one nickel), at most $1$ nickel (two nickels by a dime), at most $2$ dimes (three dimes by a quarter and a nickel), and not both $2$ dimes and a nickel (these make a quarter). So the coins other than quarters are worth at most $20+4=24$ cents, which forces the number of quarters to be $q=\left\lfloor\dfrac n{25}\right\rfloor$ and the rest to be worth $r=n-25q\le24$. The rest is then made greedily, with
\[
c(r)=\left\lfloor\dfrac r{10}\right\rfloor+\left\lfloor\dfrac{r\bmod10}{5}\right\rfloor+(r\bmod5)
\]
coins, and the fewest coins for $n$ is $q+c(r)$. For $0\le r\le18$ we have $c(r)\le5$ (the largest values are $c(9)=c(14)=c(18)=5$), while $c(19)=1+1+4=6$.

\textbf{The least amount.} An amount below $69$ has $q\le1$, giving at most $1+6=7$ coins, or $q=2$ and $r\le18$, giving at most $2+5=7$ coins. The amount $69=2\cdot25+19$ needs $2+6=8$ coins. So the least amount that cannot be made with fewer than eight coins is $\boxed{69}$ cents.''',
'Money and currency|Casework|Bounding and extremal cases',3,source=src('MATHCOUNTS',2018,'School',25,rnd='Sprint'),
note='"Last year\'s school sprint #25" (post from January 2019): 2018 MATHCOUNTS School Sprint #25. The minimum-coin counts were checked by computer for all amounts up to 200.')

# ---------------- 1778586 three problems
fig1=r'''real x=1.2,y=1.6,w=x+sqrt(9-y^2),h=y+sqrt(100-(w-x)^2);
pair A=(0,0),B=(w,0),C=(w,h),D=(0,h),P=(x,y);
draw(A--B--C--D--cycle,linewidth(0.9));
draw((x,0)--(x,h),dashed+gray); draw((0,y)--(w,y),dashed+gray);
draw(P--A,blue);draw(P--B,blue);draw(P--C,blue);draw(P--D,red);
dot(P);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);label("$P$",P+0.5*dir(140));
label("$2$",(P+A)/2,dir(140),blue);label("$3$",(P+B)/2,dir(80),blue);label("$10$",P+0.62*(C-P),dir(-5),blue);
label("$p$",(0,y/2),W);label("$t$",(0,(y+h)/2),W);label("$r$",(x/2,0),S);label("$s$",((x+w)/2,0),S);'''
fig2=r'''real r=1;
for(int k=0;k<5;++k){
  fill(circle((0,0),r),lightgray);
  path sq=r*dir(45)--r*dir(135)--r*dir(225)--r*dir(315)--cycle;
  fill(sq,white);
  draw(circle((0,0),r),linewidth(0.7)); draw(sq,linewidth(0.7));
  r=r/sqrt(2);
}
draw((0,0)--dir(160),blue+linewidth(0.6)); label("$1$",0.88*dir(160)+0.13*dir(70),blue);'''
b.add(1778586,1,r'''A point $P$ lies inside rectangle $ABCD$ with $PA=2$, $PB=3$ and $PC=10$. Find $PD$.''',
r'''Draw the lines through $P$ parallel to the sides (dashed). Let $r$ and $s$ be the distances from $P$ to $AD$ and to $BC$, and $p$ and $t$ the distances from $P$ to $AB$ and to $CD$; in the figure they appear as the pieces of the sides $AB$ and $AD$.'''+asy(fig1,'0,7cm')+r'''
By the Pythagorean theorem in the four right triangles with hypotenuses $PA,PB,PC,PD$:
\[
PA^2=r^2+p^2,\quad PB^2=s^2+p^2,\quad PC^2=s^2+t^2,\quad PD^2=r^2+t^2 .
\]
Hence $PA^2+PC^2=r^2+s^2+p^2+t^2=PB^2+PD^2$ (the British flag theorem), so
\[
PD^2=PA^2+PC^2-PB^2=4+100-9=95,\qquad PD=\boxed{\sqrt{95}}.
\]
The figure is drawn to scale (one such rectangle; the answer does not depend on which).''',
'Rectangles|Pythagorean theorem|Right triangles',3,
note='The figure uses P = (1.2, 1.6) in a rectangle about 3.74 by 11.27, which realises PA = 2, PB = 3, PC = 10.')
b.add(1778586,2,r'''A square is inscribed in a circle of radius $1$, and the region inside the circle but outside the square is shaded. Then a circle is inscribed in the square, a square is inscribed in this new circle, and the region between the new circle and the new square is shaded. This process is repeated infinitely many times. What is the total area of the shaded region?''',
r'''A square inscribed in a circle of radius $r$ has diagonal $2r$, so its area is $\dfrac{(2r)^2}{2}=2r^2$, and its inscribed circle has radius equal to half the side, $\dfrac{r}{\sqrt2}$.
'''+asy(fig2,'5cm')+r'''
So the shaded region at a stage with circle radius $r$ has area $\pi r^2-2r^2=(\pi-2)r^2$, and the next circle has radius $\dfrac r{\sqrt2}$, i.e.\ $r^2$ is halved at each stage. Starting from $r=1$, the total is the geometric series
\[
(\pi-2)\left(1+\dfrac12+\dfrac14+\cdots\right)=(\pi-2)\cdot2=\boxed{2\pi-4}.
\]''',
'Circles|Squares|Geometric sequences|Lengths, perimeter, and area',3,
note='The figure shows the first five stages.')
b.add(1778586,3,r'''Let $a$ and $b$ be integers with $2\le a\le16$ and $2\le b\le16$. What is the maximum possible value of $\dfrac{a}{10b+a}+\dfrac{b}{10a+b}$?''',
r'''The expression is symmetric, so assume $a\ge b$ and put $t=\dfrac ab\ge1$:
\[
f(t)=\dfrac{t}{10+t}+\dfrac{1}{10t+1}.
\]
Then
\[
f'(t)=\dfrac{10}{(10+t)^2}-\dfrac{10}{(10t+1)^2},
\]
which is positive for $t>1$ because $10t+1>10+t$ there. So $f$ increases with $t$, and the maximum comes from the largest ratio $t=\dfrac{16}{2}=8$, i.e.\ $a=16$, $b=2$ (or the reverse):
\[
\dfrac{16}{36}+\dfrac{2}{162}=\dfrac49+\dfrac1{81}=\boxed{\dfrac{37}{81}}.
\]''',
'Maxima and minima|Fractions|Calculus',4,
note='Checked over all 225 pairs (a, b).')

# ---------------- 1778486 parallel line halves area
fig=r'''pair B=(0,0),C=(36,0),A=(12,24);
real k=1/sqrt(2);
pair D=A+k*(B-A),Ep=A+k*(C-A);
fill(A--D--Ep--cycle,paleblue);
draw(A--B--C--cycle,linewidth(0.9));
draw(D--Ep,red+linewidth(0.9));
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$D$",D,W);label("$E$",Ep,E);
label("$36$",(B+C)/2,S);label("$x$",(D+Ep)/2,N,red);'''
b.add(1778486,1,r'''One side of a triangle has length $36$. A line parallel to that side divides the triangle into two parts of equal area. Find the length of the segment of this line that lies inside the triangle.''',
r'''Let the triangle be $ABC$ with $BC=36$, and let the line meet $AB$ at $D$ and $AC$ at $E$, with $DE\parallel BC$ and $DE=x$.
'''+asy(fig,'6cm')+r'''
Since $DE\parallel BC$, triangle $ADE$ is similar to triangle $ABC$ with ratio $\dfrac{x}{36}$, so its area is $\left(\dfrac x{36}\right)^2$ times the area of $ABC$. The two parts have equal area, so triangle $ADE$ has half the area of $ABC$:
\[
\left(\dfrac{x}{36}\right)^2=\dfrac12\ \Longrightarrow\ x=\dfrac{36}{\sqrt2}=\boxed{18\sqrt2}.
\]''',
'Similarity|Area ratios|Parallel lines|Triangles',2)

# ---------------- 1773289 99^100 vs 100^99
b.add(1773289,1,r'''Determine which is greater: $99^{100}$ or $100^{99}$.''',
r'''Compare the quotient
\[
\dfrac{99^{100}}{100^{99}}=99\cdot\left(\dfrac{99}{100}\right)^{99}=\dfrac{99}{\left(1+\dfrac1{99}\right)^{99}} .
\]
\textbf{Claim:} $\left(1+\dfrac1n\right)^n<3$ for every positive integer $n$. By the binomial theorem,
\[
\left(1+\dfrac1n\right)^n=\sum_{k=0}^{n}\dbinom nk\dfrac1{n^k},\qquad \dbinom nk\dfrac1{n^k}=\dfrac{1}{k!}\cdot\dfrac{n}{n}\cdot\dfrac{n-1}{n}\cdots\dfrac{n-k+1}{n}\le\dfrac1{k!}\le\dfrac{1}{2^{k-1}}\ (k\ge1).
\]
So the sum is at most $1+1+\dfrac12+\dfrac14+\cdots<3$.

Hence the quotient exceeds $\dfrac{99}{3}=33>1$, and $\boxed{99^{100}}$ is the greater number.''',
'Exponents|Binomial theorem|Inequalities|Bounding and extremal cases',4)

# ---------------- 1774814 re-pairing 24 students
b.add(1774814,1,r'''A teacher pairs her $24$ students into $12$ pairs. Next week she pairs them into $12$ pairs again so that every student gets a different partner from this week. In how many ways can next week's pairing be made?''',
r'''The number of ways to split $2m$ people into $m$ unordered pairs is $(2m-1)!!=(2m-1)(2m-3)\cdots3\cdot1$: the first person in a fixed order has $2m-1$ choices of partner, then the first unpaired person has $2m-3$ choices, and so on.

Let $A_i$ ($i=1,\dots,12$) be the set of pairings of the $24$ students that contain this week's $i$-th pair. A pairing containing $k$ prescribed pairs is a pairing of the other $24-2k$ students, so $|A_{i_1}\cap\dots\cap A_{i_k}|=(23-2k)!!$. By inclusion--exclusion, the number of pairings avoiding all twelve old pairs is
\[
\sum_{k=0}^{12}(-1)^k\dbinom{12}{k}(23-2k)!!=\boxed{187\,778\,717\,632},
\]
where $(-1)!!=1$. (For instance, with $4$ students the formula gives $3-2+1=2$, and with $6$ students $15-9+3-1=8$, as direct listing confirms.)''',
'Sets and inclusion–exclusion|Derangements|Combinations',5,
note='"How many ways is this possible" read as the number of new pairings of the 24 students in which nobody keeps this week\'s partner. Formula checked against brute force for up to 10 students; the value was computed exactly.')

# ---------------- 1777751 max of P
b.add(1777751,1,r'''Let $x,y,z$ be positive numbers with $x+y+z=1$. Find the maximum value of
\[
P=\dfrac{x}{x+yz}+\dfrac{y}{y+zx}+\dfrac{\sqrt{xyz}}{z+xy}.
\]''',
r'''\textbf{Substitution.} Put $a=\sqrt{\dfrac{yz}{x}}$, $b=\sqrt{\dfrac{zx}{y}}$, $c=\sqrt{\dfrac{xy}{z}}$. Then $bc=x$, $ca=y$, $ab=z$, so $ab+bc+ca=1$, and conversely positive $a,b,c$ with $ab+bc+ca=1$ give positive $x,y,z$ with sum $1$. Dividing numerator and denominator by $x$, $y$, $z$ respectively,
\[
P=\dfrac1{1+a^2}+\dfrac1{1+b^2}+\dfrac{c}{1+c^2}.
\]
\textbf{Angles.} Write $a=\tan\dfrac A2$, $b=\tan\dfrac B2$ with $A,B\in(0,\pi)$. Since $c=\dfrac{1-ab}{a+b}>0$ we have $ab<1$, so $\dfrac{A+B}{2}<\dfrac\pi2$, and $c=\cot\dfrac{A+B}{2}=\tan\dfrac C2$ with $C=\pi-A-B>0$. Using $\dfrac1{1+\tan^2u}=\cos^2u=\dfrac{1+\cos2u}{2}$ and $\dfrac{\tan u}{1+\tan^2u}=\sin u\cos u=\dfrac{\sin 2u}{2}$,
\[
P=1+\dfrac{\cos A+\cos B}{2}+\dfrac{\sin C}{2}.
\]
\textbf{Bound.} $\cos A+\cos B=2\cos\dfrac{A+B}{2}\cos\dfrac{A-B}{2}\le2\sin\dfrac C2$, with equality when $A=B$. With $t=\dfrac C2\in\left(0,\dfrac\pi2\right)$,
\[
P\le1+\sin t+\sin t\cos t=1+g(t),\qquad g(t)=\sin t\,(1+\cos t).
\]
Now $g'(t)=\cos t+\cos^2t-\sin^2t=(2\cos t-1)(\cos t+1)$, which is positive for $t<\dfrac\pi3$ and negative after, so $g(t)\le g\left(\dfrac\pi3\right)=\dfrac{\sqrt3}{2}\cdot\dfrac32=\dfrac{3\sqrt3}{4}$.

\textbf{Equality} needs $C=\dfrac{2\pi}{3}$, $A=B=\dfrac\pi6$: $a=b=\tan15^\circ=2-\sqrt3$, $c=\tan60^\circ=\sqrt3$, i.e.\ $x=y=bc=2\sqrt3-3$ and $z=ab=7-4\sqrt3$ (indeed $x+y+z=1$). Hence the maximum is
\[
\boxed{1+\dfrac{3\sqrt3}{4}}.
\]''',
'Substitution|Maxima and minima|Inequalities|Calculus',6,
note='Checked numerically by a fine grid search over the simplex and by evaluating P at the equality point.')

# ---------------- 1777839 AMC sequence 999
b.add(1777839,1,r'''A sequence $a_1,a_2,\dots$ of non-negative integers is defined by the rule $a_{n+2}=|a_{n+1}-a_n|$ for $n\ge1$. If $a_1=999$, $a_2<999$ and $a_{2006}=1$, how many different values of $a_2$ are possible?

$\textbf{(A)}\ 165\qquad\textbf{(B)}\ 324\qquad\textbf{(C)}\ 495\qquad\textbf{(D)}\ 499\qquad\textbf{(E)}\ 660$''',
r'''\textbf{The gcd is invariant.} $\gcd(a_{n+1},a_{n+2})=\gcd(a_{n+1},|a_{n+1}-a_n|)=\gcd(a_n,a_{n+1})$. So $\gcd(999,a_2)$ divides every term, including $a_{2006}=1$: we need $\gcd(999,a_2)=1$ (in particular $a_2\ge1$).

\textbf{Parity.} If $a_2$ is even, the parities are odd, even, odd, odd, even, odd, odd, even, $\dots$ (period $3$), and $a_n$ is even exactly when $n\equiv2\pmod3$. Since $2006\equiv2\pmod3$, $a_{2006}$ would be even. So $a_2$ must be odd. Then the parities are odd, odd, even, odd, odd, even, $\dots$, and $a_n$ is even exactly when $n\equiv0\pmod3$; $a_{2006}$ is odd.

\textbf{These conditions suffice.} Suppose $a_2$ is odd and $\gcd(999,a_2)=1$, and let $M_n=\max(a_n,a_{n+1})$. While $M_n>1$, two consecutive terms are positive and coprime, hence different, so the next term is positive too; and if $a_n,a_{n+1},a_{n+2}>0$ then $a_{n+2}<M_n$ and $a_{n+3}<\max(a_{n+1},a_{n+2})\le M_n$, so $M_{n+2}\le M_n-1$. Starting from $M_1=999$, we get $M_n=1$ for some $n\le1+2\cdot998=1997$. From then on the terms are $0$s and $1$s following $|a_{n+1}-a_n|$, i.e.\ the pattern $1,1,0$ repeats, so every term after that point is $0$ or $1$. As $a_{2006}$ is odd, $a_{2006}=1$.

\textbf{Count.} $999=3^3\cdot37$, so $\varphi(999)=999\cdot\dfrac23\cdot\dfrac{36}{37}=648$ numbers in $[1,998]$ are coprime to $999$. The map $k\mapsto999-k$ pairs them and changes parity, so exactly half are odd. The number of possible $a_2$ is $\boxed{324}$, answer $\textbf{(B)}$.''',
'Recurrence relations|Invariants and monovariants|Parity|Euler\'s theorem and totient',6,
note='This is 2006 AMC 12B #25 (the post does not name the source). Count confirmed by simulating every a_2 < 999.')

b.save()
