from qb import *
b=Bank('p223_02')

# ---------------- 1777627 5a+3b+4c-abc=19
b.add(1777627,1,r'''Find all triples $(a,b,c)$ of positive integers such that
\[
5a+3b+4c-abc=19 .
\]''',
r'''\textbf{A factorisation.} Multiply the equation $abc-5a-3b=4c-19$ by $c$ and add $15$:
\[
(ac-3)(bc-5)=abc^2-5ac-3bc+15=c(4c-19)+15=(c-1)(4c-15).
\]
\textbf{$c=1$.} Then $(a-3)(b-5)=0$: every triple $(3,b,1)$ and every triple $(a,5,1)$ works (check: $15+3b+4-3b=19$ and $5a+15+4-5a=19$).

\textbf{$c=2$.} $(2a-3)(2b-5)=-7$ with both factors odd and $2a-3\ge-1$, $2b-5\ge-3$: the factorisations $(-1)(7)$ and $(7)(-1)$ give $(a,b)=(1,6)$ and $(5,2)$; the others give $b$ or $a$ not positive.

\textbf{$c=3$.} $3(a-1)(3b-5)=-6$, i.e.\ $(a-1)(3b-5)=-2$. Here $a-1\ge0$, and $a-1=0$ is impossible, so $a-1\in\{1,2\}$: $a-1=1$ gives $3b-5=-2$, so $(a,b)=(2,1)$; $a-1=2$ gives $3b-5=-1$, which has no integer solution.

\textbf{$c\ge4$.} Now the right side $(c-1)(4c-15)$ is positive. If $a\ge2$ and $b\ge2$, both factors on the left are positive and
\[
(ac-3)(bc-5)\ge(2c-3)(2c-5)=4c^2-16c+15>4c^2-19c+15=(c-1)(4c-15),
\]
a contradiction. So $a=1$ or $b=1$.
\begin{itemize}
\item $a=1$: $(c-3)(bc-5)=(c-1)(4c-15)=(c-3)(4c-7)-6$, so $c-3\mid6$ and $c\in\{4,5,6,9\}$. Then $bc-5=(4c-7)-\dfrac{6}{c-3}$ equals $3,10,15,28$, giving $b=2$ for $c=4$, $b=3$ for $c=5$, and no integer $b$ for $c=6$ or $c=9$.
\item $b=1$: $(ac-3)(c-5)=(c-1)(4c-15)=(c-5)(4c+1)+20$, so $c\ne5$ and $c-5\mid20$, giving $c\in\{4,6,7,9,10,15,25\}$. Then $ac-3=4c+1+\dfrac{20}{c-5}$ equals $-3,45,39,42,45,63,102$, giving $a=0$ (not allowed) for $c=4$, $a=8$ for $c=6$, $a=6$ for $c=7$, $a=5$ for $c=9$, and no integer $a$ for $c=10,15,25$.
\end{itemize}
\textbf{Answer.} The solutions are the two infinite families
\[
\boxed{(3,b,1)\ (b\ge1)\quad\text{and}\quad(a,5,1)\ (a\ge1)}
\]
together with the eight triples
\[
\boxed{(1,6,2),\ (5,2,2),\ (2,1,3),\ (1,2,4),\ (1,3,5),\ (8,1,6),\ (6,1,7),\ (5,1,9)}.
\]''',
'Diophantine equations|Factoring|Divisibility|Casework',5,
note='The post asks for all integer solutions. Over the integers there are many more families (for instance a = 0 with 3b + 4c = 19), so the record restricts to positive integers. Solution list confirmed by a computer search over 1 <= a, b, c <= 60.')

# ---------------- 1777493 change for $20
b.add(1777493,1,r'''In how many ways can change for a $\$20$ bill be made using $\$1$, $\$5$ and $\$10$ bills (not every type has to be used)?''',
r'''Let $x$, $y$, $z$ be the numbers of $\$1$, $\$5$ and $\$10$ bills, so $x+5y+10z=20$ with $x,y,z\ge0$. Once $y$ and $z$ are chosen with $5y+10z\le20$, $x$ is determined.
\begin{itemize}
\item $z=0$: $5y\le20$, so $y=0,1,2,3,4$: $5$ ways.
\item $z=1$: $5y\le10$, so $y=0,1,2$: $3$ ways.
\item $z=2$: $y=0$: $1$ way.
\end{itemize}
Total: $\boxed{9}$ ways.''',
'Money and currency|Linear Diophantine equations|Systematic counting',2,
note='"And/or" read as allowing any combination of the three bill types. The second problem of the post is only in an attachment and is dropped.')

# ---------------- 1777483 2014 Chapter Sprint 22 (canonical)
b.add(1777483,1,r'''The length of the diagonal of rectangle $ABCD$ is half the rectangle's perimeter less four-fifths the length of the shorter side. Find the ratio of the length of the shorter side to the length of the longer side of the rectangle. Express your answer as a common fraction.''',
r'''Let the longer side be $l$ and the shorter side $w$. Half the perimeter is $l+w$; subtracting four-fifths of the shorter side leaves $l+\dfrac w5$. By the Pythagorean theorem,
\[
l^2+w^2=\left(l+\dfrac w5\right)^2=l^2+\dfrac{2lw}{5}+\dfrac{w^2}{25},
\]
so $\dfrac{24}{25}w^2=\dfrac25lw$ and $\dfrac wl=\dfrac{10}{24}=\boxed{\dfrac{5}{12}}$. (Check: a $5$ by $12$ rectangle has diagonal $13$, and $\dfrac{34}{2}-\dfrac45\cdot5=17-4=13$.)
'''+asy(r'''pair A=(0,0),B=(12,0),C=(12,5),D=(0,5);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--C,blue+linewidth(0.8));
real s=0.6; draw(B+(-s,0)--B+(-s,s)--B+(0,s));
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,NE);label("$D$",D,NW);
label("$l$",(A+B)/2,S);label("$w$",(B+C)/2,E);label("$l+\dfrac{w}{5}$",(A+C)/2+(0.6,0),dir(-60),blue);''','6cm')+r'''
The figure shows the rectangle drawn with the answer's proportions, $l=12$ and $w=5$.''',
'Rectangles|Pythagorean theorem|Ratios, proportions, and variation',2,source=src('MATHCOUNTS',2014,'Chapter',22,rnd='Sprint'),
note='"Less four-fifths" means minus four-fifths.')

# ---------------- 1773488 1234*** square
b.add(1773488,1,r'''A seven-digit number $1234\ast\ast\ast$, where each $\ast$ is a missing digit, is a perfect square. Find its square root.''',
r'''The number lies between $1\,234\,000$ and $1\,234\,999$. Since $1110^2=1\,232\,100$ is too small and $1112^2=1\,236\,544$ is too large, the square root, an integer between $1110$ and $1112$, must be $1111$. Indeed $1111^2=1\,234\,321$ has the required form. The square root is $\boxed{1111}$.''',
'Perfect squares|Estimation|Digit problems',2)

# ---------------- 1777171 play roles
b.add(1777171,1,r'''A play has two male roles, two female roles and two roles that can be either gender. Only a man can be assigned to a male role, and only a woman can be assigned to a female role. If five men and six women audition, in how many ways can the six roles be assigned? Explain why the answer is not $\dbinom52\dbinom62\dbinom72$.''',
r'''The roles are different from each other (each is a particular character), so the order of assignment matters within each type.
\begin{itemize}
\item The two male roles: $5\cdot4=20$ ways.
\item The two female roles: $6\cdot5=30$ ways.
\item The two either-gender roles go to two of the remaining $3+4=7$ people: $7\cdot6=42$ ways.
\end{itemize}
The total is $20\cdot30\cdot42=\boxed{25200}$.

The product $\dbinom52\dbinom62\dbinom72=10\cdot15\cdot21=3150$ only chooses \emph{which} people fill each type of role; it treats the two male roles as interchangeable, and likewise the female and the either-gender roles. Each of the three choices must be multiplied by $2$ for the two ways to hand the two chosen people their two different roles: $3150\cdot2^3=25200$.''',
'Permutations|Multiplication principle|Arrangements with restrictions',3,source=src('MATHCOUNTS',2005,'Chapter',29),
note='The post cites "Chapter Problem 29, 2005" (round not given) and asks why C(5,2)C(6,2)C(7,2) is wrong; both parts are in the record.')

# ---------------- 1777424 cube colouring
b.add(1777424,1,r'''Six different colours are available. In how many ways can the faces of a cube be painted, using one or more of the colours, so that each face is a single colour and any two faces sharing an edge have different colours? Two colourings are considered the same if one can be rotated into the other. In particular, explain why exactly $30$ colourings use all six colours.''',
r'''Faces sharing an edge differ, so faces of the same colour must be opposite. The three faces at a corner are pairwise adjacent, so at least $3$ colours are used. Count by the number $k$ of colours used.

\textbf{$k=6$.} All faces differ. Rotate so that one particular colour, say red, is on top (this uses the freedom of rotation once). The bottom can be any of the other $5$ colours. The remaining $4$ colours go around the sides; turning the cube about the vertical axis lets us put a chosen one of them in front, and the other $3$ can be arranged in the remaining positions in $3!=6$ ways, all different. So there are $5\cdot6=30$ colourings. Equivalently: $6!=720$ ways to colour labelled faces, and each colouring with six different colours is counted once for each of the $24$ rotations of the cube, giving $\dfrac{720}{24}=30$. (This is the $\dfrac{6!}{4!}$ in the book's solution: $4!=24$ is the number of rotations.)

\textbf{$k=5$.} Exactly one pair of opposite faces shares a colour. Choose the $5$ colours ($6$ ways) and the colour of that pair ($5$ ways); put the pair on top and bottom. The other $4$ colours go around a ring of $4$ side faces, and the symmetries of the cube keeping the top-bottom pair in place act on the ring as the $8$ symmetries of a square, so there are $\dfrac{4!}{8}=3$ arrangements. Total $6\cdot5\cdot3=90$.

\textbf{$k=4$.} Two opposite pairs share colours, and the third pair has two different colours. Choose the $4$ colours ($15$ ways) and the two colours used on pairs ($\dbinom42=6$ ways); all such colourings are rotations of one another (a half-turn swaps the two single faces). Total $15\cdot6=90$.

\textbf{$k=3$.} Each opposite pair has one colour: choose the $3$ colours ($\dbinom63=20$ ways); the arrangement is unique up to rotation. Total $20$.

Altogether $30+90+90+20=\boxed{230}$.''',
'Colourings, tilings, and coverings|Casework|Symmetry|Circular arrangements',5,
note='Rotations are taken as equivalent (as in the book solution the poster quotes, which divides by 4! = 24). The total 230 was confirmed by enumerating all 4080 proper colourings of a labelled cube and grouping them into rotation classes.')

# ---------------- 1777119 abundant factorial
b.add(1777119,1,r'''An abundant number is a positive integer whose proper factors (all positive divisors except the number itself) add up to more than the number. In the sequence $1!,2!,3!,\dots$, which term is the first abundant number?''',
r'''Check the terms in order.
\begin{itemize}
\item $1!=1$: no proper factors except none; the sum is $0$.
\item $2!=2$: proper factors sum to $1$.
\item $3!=6$: $1+2+3=6$, equal to $6$ ($6$ is perfect, not abundant).
\item $4!=24$: $1+2+3+4+6+8+12=36>24$.
\end{itemize}
So the first abundant term is $4!=24$, the $\boxed{4\text{th}}$ term.''',
'Factorials|Sum of divisors|Factors and multiples',2)

# ---------------- 1777120 earrings (alias)
b.add(1777120,1,r'''Susan has $5$ pairs of differently coloured hoop earrings jumbled together in a drawer. If she chooses two earrings at random without looking, what is the probability that she picks a matching pair?''',
r'''Whatever the first earring is, $1$ of the remaining $9$ earrings matches it. The probability is $\boxed{\dfrac19}$. (Equivalently, $5$ of the $\dbinom{10}{2}=45$ pairs of earrings match: $\dfrac{5}{45}=\dfrac19$.)''',
'Probability|Sampling without replacement',1,
note='Repeat of an earlier record (aliased).')

# ---------------- 1777122 plates around a table
b.add(1777122,1,r'''Mrs. Arthur is putting two red plates and four blue plates around a circular table at six equally spaced seats. In how many ways can she arrange the red and blue plates, if two arrangements that differ by a rotation of the table are considered the same?''',
r'''An arrangement is determined, up to rotation, by how far apart the two red plates are around the table: they can be adjacent ($1$ seat apart), have one seat between them ($2$ apart), or be opposite ($3$ apart). Distances $4$ and $5$ are the same as $2$ and $1$ measured the other way. These three arrangements cannot be rotated into each other, so there are $\boxed{3}$ arrangements.

(If the seats are distinguishable, i.e.\ rotations count as different, the answer would be $\dbinom62=15$; check: the three classes contain $6$, $6$ and $3$ seatings, and $6+6+3=15$.)''',
'Circular arrangements|Casework|Symmetry',2,
note='The post does not say whether rotations count as different; the record takes rotations as the same and gives the other reading (15) as a remark.')

# ---------------- 1775465 product 9 sum 12
b.add(1775465,1,r'''The product of two numbers is $9$ and their sum is $12$. Express their positive difference in simplest radical form.''',
r'''Let the numbers be $x$ and $y$. Then
\[
(x-y)^2=(x+y)^2-4xy=144-36=108,
\]
so the positive difference is $\sqrt{108}=\boxed{6\sqrt3}$. (The numbers are $6\pm3\sqrt3$.)''',
'Algebraic expressions and identities|Radicals|Quadratic equations',2)

# ---------------- 1161680 division by a quadratic
b.add(1161680,1,r'''Synthetic division works for divisors of the form $x-c$. Use it twice to divide $P(x)=x^4-3x^3+2x^2+5x-1$ by $x^2-x-2$, finding the quotient and the remainder.''',
r'''Factor the divisor: $x^2-x-2=(x-2)(x+1)$.

\textbf{Divide by $x-2$.} Synthetic division with $2$ on the coefficients $1,-3,2,5,-1$ gives $1,\,-1,\,0,\,5$ and remainder $9$:
\[
P(x)=(x-2)(x^3-x^2+5)+9 .
\]
\textbf{Divide the quotient by $x+1$.} Synthetic division with $-1$ on $1,-1,0,5$ gives $1,\,-2,\,2$ and remainder $3$:
\[
x^3-x^2+5=(x+1)(x^2-2x+2)+3 .
\]
\textbf{Combine.}
\[
P(x)=(x-2)\bigl[(x+1)(x^2-2x+2)+3\bigr]+9=(x^2-x-2)(x^2-2x+2)+3(x-2)+9 .
\]
So the quotient is $\boxed{x^2-2x+2}$ and the remainder is $\boxed{3x+3}$.

Check with the roots of the divisor: $P(2)=16-24+8+10-1=9=3\cdot2+3$ and $P(-1)=1+3+2-5-1=0=3(-1)+3$. In general, dividing by $(x-a)(x-b)$ this way gives quotient $Q_2$ and remainder $r_2(x-a)+r_1$, where $r_1$, $r_2$ are the two synthetic-division remainders.''',
'Polynomials|Remainder theorem and factor theorem|Factoring',3,
note='The post asks how synthetic division works for a divisor such as x^2 - x - 2 without giving a dividend; the polynomial x^4 - 3x^3 + 2x^2 + 5x - 1 was chosen for the record to illustrate the method.')

# ---------------- 1776896 0.999...=1
b.add(1776896,1,r'''A student argues: let $x=0.\overline{9}=0.999\ldots$; then $10x=9.999\ldots$, so $10x-x=9$, $9x=9$ and $x=1$. Is $0.\overline{9}=1$ true? Explain what the argument assumes, and give a proof.''',
r'''Yes, $0.\overline9=1$. The argument is correct once we know what an infinite decimal means: $0.999\ldots$ is the limit of the partial sums $0.9,\ 0.99,\ 0.999,\dots$, that is, the sum of the infinite geometric series
\[
x=\dfrac{9}{10}+\dfrac{9}{100}+\dfrac{9}{1000}+\cdots .
\]
The steps ``$10x=9.999\ldots$'' and ``$10x-x=9$'' multiply a convergent series by $10$ term by term and subtract two convergent series term by term; both are valid for convergent series, but they assume that $x$ exists as a number, which is exactly what the geometric series provides.

\textbf{Proof.} The $n$-th partial sum is $s_n=1-\dfrac1{10^n}$, since $1-s_n=0.00\ldots01$ with $n$ decimal places. As $n\to\infty$, $\dfrac1{10^n}\to0$, so $x=\lim s_n=1$. (By the geometric series formula, $x=\dfrac{\dfrac{9}{10}}{1-\dfrac1{10}}=1$.)

Another way to see it: if $0.\overline9<1$, the number $d=1-0.\overline9$ would be positive; but $d\le1-s_n=\dfrac1{10^n}$ for every $n$, which is impossible for a positive $d$ once $10^n>\dfrac1d$. So $\boxed{0.\overline{9}=1}$.''',
'Repeating decimals|Geometric sequences|Proof by contradiction',2,
note='The post asks whether the 10x - x argument works; the record asks for a proof and a comment on the argument. Repeat of an earlier record (aliased).')

# ---------------- 1776603 a^3-6b^2
b.add(1776603,1,r'''If $a$ and $b$ are the two roots of $x^2+x-5=0$, find $a^3-6b^2$.''',
r'''Since $a$ and $b$ are roots, $a^2=5-a$ and $b^2=5-b$. Then
\[
a^3=a\cdot a^2=5a-a^2=5a-(5-a)=6a-5,
\]
and
\[
a^3-6b^2=6a-5-6(5-b)=6(a+b)-35 .
\]
By Vieta's formulas $a+b=-1$, so $a^3-6b^2=-6-35=\boxed{-41}$. (The value is the same whichever root is called $a$.)''',
'Polynomial roots|Vieta\'s formulas|Algebraic manipulation',3)

# ---------------- 1775616 semicircle probability
fig=r'''real R=4; pair O=(0,0);
draw(arc(O,R,0,180),linewidth(0.9)); draw((-R,0)--(R,0),linewidth(0.6));
pair A=R*dir(25),B=R*dir(75);
draw(O--A--B--cycle,linewidth(0.9));
pair Fp=O+dot(B-O,unit(A-O))*unit(A-O);
draw(B--Fp,dashed+blue);
pair u=unit(A-O),v=unit(B-Fp);
draw(Fp-0.3*u--Fp-0.3*u+0.3*v--Fp+0.3*v,blue);
draw(arc(O,0.9,25,75),linewidth(0.6)); label("$\theta$",O+1.3*dir(50));
dot(O); label("$O$",O,S); label("$A$",A,dir(25)); label("$B$",B,dir(75));
label("$4$",(O+A)/2,dir(-65)); label("$h$",(B+Fp)/2,dir(25),blue);'''
b.add(1775616,1,r'''A semicircle with radius $4$ has centre $O$, and $A$ and $B$ are distinct points on its curved part. Suppose that at least one angle of $\triangle OAB$ has an integer measure in degrees, and that, up to congruence, each triangle $OAB$ satisfying this is equally likely. What is the probability that the area of $\triangle OAB$ is at most $4$?''',
r'''Let $\theta=\angle AOB$, with $0^\circ<\theta\le180^\circ$; since $A$ and $B$ lie on the arc of a semicircle, $\theta<180^\circ$ unless $A$, $B$ are the ends of the diameter, where the triangle is degenerate, so $0^\circ<\theta<180^\circ$. Triangle $OAB$ is isosceles with $OA=OB=4$ and base angles $\dfrac{180^\circ-\theta}{2}$; it is determined up to congruence by $\theta$.

\textbf{Which triangles qualify.} If a base angle is an integer $k$, then $\theta=180^\circ-2k$ is an integer. So ``at least one angle is an integer'' means exactly that $\theta$ is an integer, $\theta\in\{1,2,\dots,179\}$: $179$ equally likely triangles.
'''+asy(fig,'6cm')+r'''
\textbf{Area.} The height from $B$ to $OA$ is $h=4\sin\theta$, so $[OAB]=\dfrac12\cdot4\cdot4\sin\theta=8\sin\theta$. Then $[OAB]\le4$ iff $\sin\theta\le\dfrac12$ iff $\theta\le30^\circ$ or $\theta\ge150^\circ$. That gives $30+30=60$ values.

The probability is $\boxed{\dfrac{60}{179}}$.''',
'Probability|Circles|Isosceles triangles|Lengths, perimeter, and area|Trigonometry',4,
note='As posted, the probability is not defined (the condition "at least one angle has integer measure" has probability zero for random points). The record makes the intended reading explicit: the triangles allowed, one for each integer value of angle AOB from 1 to 179 degrees, are equally likely. Degenerate triangles are excluded.')

# ---------------- 1776391 three problems
b.add(1776391,1,r'''Real numbers $a$ and $b$ satisfy $a^2b^2+a^2+b^2+10ab+16=0$. Find $a^2+b^2$.''',
r'''Split $10ab=8ab+2ab$ and complete two squares:
\[
a^2b^2+a^2+b^2+10ab+16=(a^2b^2+8ab+16)+(a^2+2ab+b^2)=(ab+4)^2+(a+b)^2 .
\]
For real numbers this sum of squares is $0$ only if $ab=-4$ and $a+b=0$ (e.g.\ $a=2$, $b=-2$). Then
\[
a^2+b^2=(a+b)^2-2ab=0+8=\boxed{8}.
\]''',
'Completing the square|Algebraic expressions and identities',3,
note='The post does not say a and b are real; this is needed and is added.')
b.add(1776391,2,r'''Simplify $|x+3|-|4-x|$ for all real $x$ (write it without absolute value signs on each interval).''',
r'''The expressions inside change sign at $x=-3$ and $x=4$.
\begin{itemize}
\item $x<-3$: $|x+3|=-(x+3)$ and $|4-x|=4-x$, so the value is $-x-3-4+x=-7$.
\item $-3\le x\le4$: $|x+3|=x+3$ and $|4-x|=4-x$, so the value is $2x-1$.
\item $x>4$: $|x+3|=x+3$ and $|4-x|=x-4$, so the value is $7$.
\end{itemize}
\[
\boxed{|x+3|-|4-x|=\begin{cases}-7,&x<-3,\\ 2x-1,&-3\le x\le4,\\ 7,&x>4.\end{cases}}
\]''',
'Absolute value|Piecewise functions',2)
b.add(1776391,3,r'''Simplify $|x+1|-|2x-3|+|x+2|$ for all real $x$.''',
r'''The breakpoints are $x=-2$, $x=-1$ and $x=\dfrac32$.
\begin{itemize}
\item $x<-2$: $-(x+1)+(2x-3)-(x+2)=-6$.
\item $-2\le x<-1$: $-(x+1)+(2x-3)+(x+2)=2x-2$.
\item $-1\le x<\dfrac32$: $(x+1)+(2x-3)+(x+2)=4x$.
\item $x\ge\dfrac32$: $(x+1)-(2x-3)+(x+2)=6$.
\end{itemize}
\[
\boxed{|x+1|-|2x-3|+|x+2|=\begin{cases}-6,&x<-2,\\ 2x-2,&-2\le x<-1,\\ 4x,&-1\le x<\dfrac32,\\ 6,&x\ge\dfrac32.\end{cases}}
\]
(The pieces agree at the breakpoints: $-6$ at $x=-2$, $-4$ at $x=-1$, $6$ at $x=\dfrac32$.)''',
'Absolute value|Piecewise functions',2)

# ---------------- 1776515 remainders 32 and 58
b.add(1776515,1,r'''A positive integer less than $3000$ leaves remainder $30$ when divided by $32$ and remainder $44$ when divided by $58$. Find all such integers.''',
r'''Write $N=32k+30$. We need $32k+30\equiv44\pmod{58}$, i.e.\ $32k\equiv14\pmod{58}$. Everything is even, so divide by $2$: $16k\equiv7\pmod{29}$. Since $16\cdot20=320=11\cdot29+1$, the inverse of $16$ modulo $29$ is $20$, and $k\equiv140\equiv24\pmod{29}$. So $N=32(24+29j)+30=798+928j$, where $928=\operatorname{lcm}(32,58)$.

Below $3000$ this gives $\boxed{798,\ 1726,\ 2654}$. (Check: $798=24\cdot32+30=13\cdot58+44$.)''',
'Chinese remainder theorem|Remainders and congruences|HCF and LCM',3,
note='The post asks "What number am I?", but three numbers below 3000 satisfy the conditions; the record asks for all of them (the least is 798).')

# ---------------- 1329488 telescoping product
b.add(1329488,1,r'''Evaluate $\left(1+\dfrac12\right)\left(1+\dfrac13\right)\left(1+\dfrac14\right)\cdots\left(1+\dfrac1{499}\right)$.''',
r'''Each factor is $1+\dfrac1k=\dfrac{k+1}{k}$, so the product telescopes:
\[
\dfrac32\cdot\dfrac43\cdot\dfrac54\cdots\dfrac{500}{499}=\dfrac{500}{2}=\boxed{250}.
\]''',
'Fractions|Telescoping sums',2)

# ---------------- 1776390 Gaussian binomial coefficients
b.add(1776390,1,r'''Let $n$ be a positive integer and $a$ a number with $a^j\ne1$ for $j=1,\dots,n$. Let
\[
f(x)=(1+ax)\left(1+a^2x\right)\cdots\left(1+a^nx\right)=1+A_1x+A_2x^2+\cdots+A_nx^n .
\]
\begin{enumerate}
\item Prove that $(1+ax)f(ax)=\left(1+a^{n+1}x\right)f(x)$.
\item Find $A_i$ in terms of $a$, $n$ and $i$.
\end{enumerate}''',
r'''\textbf{1.} Replacing $x$ by $ax$ multiplies each $a^kx$ by $a$: $f(ax)=\left(1+a^2x\right)\left(1+a^3x\right)\cdots\left(1+a^{n+1}x\right)$. Hence
\[
(1+ax)f(ax)=(1+ax)\left(1+a^2x\right)\cdots\left(1+a^nx\right)\left(1+a^{n+1}x\right)=\left(1+a^{n+1}x\right)f(x).
\]
\textbf{2.} Put $A_0=1$. The coefficient of $x^i$ ($1\le i\le n$) on the left is $a^iA_i+a\cdot a^{i-1}A_{i-1}=a^iA_i+a^iA_{i-1}$, and on the right it is $A_i+a^{n+1}A_{i-1}$. So
\[
(a^i-1)A_i=\left(a^{n+1}-a^i\right)A_{i-1},\qquad A_i=a^i\cdot\dfrac{a^{n-i+1}-1}{a^i-1}\,A_{i-1},
\]
which is allowed since $a^i\ne1$. Multiplying these relations for $1,2,\dots,i$ and using $1+2+\cdots+i=\dfrac{i(i+1)}{2}$,
\[
\boxed{A_i=a^{\dfrac{i(i+1)}{2}}\prod_{j=1}^{i}\dfrac{a^{n-j+1}-1}{a^{j}-1}=a^{\dfrac{i(i+1)}{2}}\cdot\dfrac{(a^n-1)(a^{n-1}-1)\cdots(a^{n-i+1}-1)}{(a-1)(a^2-1)\cdots(a^i-1)}}.
\]
For example, $A_1=a\cdot\dfrac{a^n-1}{a-1}=a+a^2+\cdots+a^n$, as it should be, and $A_n=a^{\dfrac{n(n+1)}{2}}=a\cdot a^2\cdots a^n$.''',
'Polynomials|Recurrence relations|Algebraic manipulation',5,
note='The post states part 1 (with its solution) and asks for A_i; the record asks for both. The condition a^j != 1 is added so the division is valid. The formula was checked symbolically for n <= 6.')

# ---------------- 1776426 2006 State Sprint 29
fig=r'''pair A=(0,0),B=(0,3),C=(5,0),P=(3,1);
draw((-0.6,0)--(5.8,0),gray,Arrow(5)); draw((0,-0.6)--(0,3.8),gray,Arrow(5));
label("$x$",(5.8,0),E,gray); label("$y$",(0,3.8),N,gray);
draw(A--B--C--cycle,linewidth(0.9));
draw(P--A,blue+dashed); draw(P--B,blue+dashed); draw(P--C,red+dashed);
dot(P); dot(A); dot(B); dot(C);
label("$A$",A,SW); label("$B(0,3)$",B,W); label("$C(5,0)$",C,S); label("$P$",P,dir(-90));
label("$\sqrt{10}$",(1.6,0.92),blue); label("$\sqrt{13}$",(1.3,1.7),blue); label("$\sqrt{5}$",(3.9,0.22),red);'''
b.add(1776426,1,r'''Triangle $ABC$ has vertices $A(0,0)$, $B(0,3)$ and $C(5,0)$. A point $P$ inside the triangle is $\sqrt{10}$ units from $A$ and $\sqrt{13}$ units from $B$. How many units is $P$ from $C$? Express your answer in simplest radical form.''',
r'''Let $P=(x,y)$. The distance conditions are
\[
x^2+y^2=10,\qquad x^2+(y-3)^2=13 .
\]
Subtracting, $-6y+9=3$, so $y=1$ and $x^2=9$. As $P$ is inside the triangle, $x>0$, so $P=(3,1)$ (indeed $3\cdot3+5\cdot1<15$, so $P$ is below line $BC$).
'''+asy(fig,'8cm')+r'''
Then $PC=\sqrt{(5-3)^2+(0-1)^2}=\boxed{\sqrt5}$.''',
'Coordinate geometry|Distance formula|Equations and systems of equations',2,source=src('MATHCOUNTS',2006,'State',29,rnd='Sprint'))

# ---------------- 1776440 USAMTS product
b.add(1776440,1,r'''Let $p(x)=x^5+x^2+1$ have roots $r_1,r_2,r_3,r_4,r_5$, and let $q(x)=x^2-2$. Determine the product $q(r_1)q(r_2)q(r_3)q(r_4)q(r_5)$.''',
r'''Since $p$ is monic of degree $5$, $p(t)=\prod_{i=1}^{5}(t-r_i)$, so $\prod_{i=1}^5(r_i-t)=(-1)^5p(t)=-p(t)$. Now $q(r_i)=(r_i-\sqrt2)(r_i+\sqrt2)$, so
\[
\prod_{i=1}^5q(r_i)=\prod_{i=1}^5(r_i-\sqrt2)\cdot\prod_{i=1}^5\bigl(r_i-(-\sqrt2)\bigr)=\bigl(-p(\sqrt2)\bigr)\bigl(-p(-\sqrt2)\bigr)=p(\sqrt2)\,p(-\sqrt2).
\]
With $(\sqrt2)^5=4\sqrt2$: $p(\sqrt2)=4\sqrt2+2+1=3+4\sqrt2$ and $p(-\sqrt2)=3-4\sqrt2$. The product is $9-32=\boxed{-23}$.''',
'Polynomial roots|Polynomials|Difference of squares',4,source=src('USAMTS',None,None,None),
note='The post calls this a past USAMTS problem (year and number not given). Checked numerically with the roots of p.')

# ---------------- 1776388 ad-bc
b.add(1776388,1,r'''Real numbers $a,b,c,d$ satisfy $a^2+b^2=4$, $c^2+d^2=10$ and $ac+bd=2$. Find all possible values of $ad-bc$.''',
r'''Use the identity (Lagrange's or Brahmagupta--Fibonacci identity)
\[
(a^2+b^2)(c^2+d^2)=(ac+bd)^2+(ad-bc)^2 ,
\]
which follows by expanding both sides. It gives $40=4+(ad-bc)^2$, so $(ad-bc)^2=36$ and $ad-bc=\pm6$.

Both signs occur: $a=2$, $b=0$, $c=1$, $d=3$ gives $a^2+b^2=4$, $c^2+d^2=10$, $ac+bd=2$ and $ad-bc=6$; changing $d$ to $-3$ keeps the three conditions and gives $ad-bc=-6$. So $ad-bc=\boxed{\pm6}$.''',
'Algebraic expressions and identities|Equations and systems of equations',3,
note='The post asks for "ad - bc" as if it were unique; both values 6 and -6 occur, and the record asks for all possible values.')

# ---------------- 1774223 every triangle is cyclic
fig=r'''pair A=(1,3.2),B=(0,0),C=(5,0);
pair cc(pair P,pair Q,pair R){pair a=Q-P,c=R-P; real d=2*(a.x*c.y-a.y*c.x);
  return P+((c.y*dot(a,a)-a.y*dot(c,c))/d,(a.x*dot(c,c)-c.x*dot(a,a))/d);}
pair O=cc(A,B,C); real R=abs(A-O);
pair M=(A+B)/2,K=(B+C)/2;
draw(circle(O,R),blue+linewidth(0.7));
draw(A--B--C--cycle,linewidth(0.9));
pair u1=unit(rotate(90)*(B-A)); draw(M-0.9*u1--O+0.9*unit(O-M),dashed);
draw(K+(0,-0.9)--O+(0,0.9),dashed);
draw(O--A,gray);draw(O--B,gray);draw(O--C,gray);
real s=0.22; pair e1=unit(A-B),e2=unit(O-M);
draw(M+s*e1--M+s*e1+s*e2--M+s*e2);
draw(K+(s,0)--K+(s,s)--K+(0,s));
dot(O);dot(M);dot(K);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);label("$O$",O+0.32*dir(40));
label("$M$",M+0.4*dir(117.6));label("$K$",K,dir(-45));'''
b.add(1774223,1,r'''Prove that every triangle is cyclic: for any triangle $ABC$ there is a circle passing through $A$, $B$ and $C$.''',
r'''Let $M$ and $K$ be the midpoints of $AB$ and $BC$, and draw the perpendicular bisectors of $AB$ and $BC$ (the lines through $M$ and $K$ perpendicular to these sides).
'''+asy(fig,'6cm')+r'''
\textbf{The bisectors meet.} If they were parallel, then $AB$ and $BC$, being perpendicular to parallel lines, would be parallel; as they share the point $B$, the points $A$, $B$, $C$ would be collinear, which is not a triangle. So the two perpendicular bisectors meet at a point $O$.

\textbf{$O$ is equidistant from the vertices.} A point is on the perpendicular bisector of a segment exactly when it is equally far from the two endpoints (the right triangles $OMA$ and $OMB$ are congruent by SAS). So $OA=OB$ because $O$ is on the bisector of $AB$, and $OB=OC$ because $O$ is on the bisector of $BC$.

Hence $OA=OB=OC$, and the circle with centre $O$ and radius $OA$ passes through $A$, $B$ and $C$. Every triangle is cyclic. $\blacksquare$ (Moreover $OA=OC$ shows that $O$ also lies on the perpendicular bisector of $CA$, and the circle is unique, since its centre must lie on all three bisectors.)''',
'Circumcircles and circumcentres|Perpendicular bisectors|Triangles|Congruence',2,
note='The post asks to prove "all triangles are cyclic", i.e. that every triangle has a circumcircle. The argument does not depend on whether the triangle is acute or obtuse, so one figure is drawn.')

# ---------------- 1775548 (n^4-1441)/(n^2-1) square
b.add(1775548,1,r'''Find all integers $n$ for which $\dfrac{n^4-1441}{n^2-1}$ is a perfect square (the square of an integer).''',
r'''We need $n\ne\pm1$. Divide:
\[
\dfrac{n^4-1441}{n^2-1}=\dfrac{(n^4-1)-1440}{n^2-1}=n^2+1-\dfrac{1440}{n^2-1}.
\]
For this to be an integer, $n^2-1$ must divide $1440$. For $n=0$ the value is $1441$, not a square ($37^2=1369$, $38^2=1444$). For $|n|\ge2$, the divisors of $1440=2^5\cdot3^2\cdot5$ of the form $n^2-1$ are $3,8,15,24,48,80,120,288,360$ (for $|n|=2,3,4,5,7,9,11,17,19$; for $|n|\le37$ one checks the other values of $n^2-1$, and for $|n|\ge38$, $n^2-1>1440$). The corresponding values of $n^2+1-\dfrac{1440}{n^2-1}$ are
\[
5-480,\ 10-180,\ 17-96,\ 26-60,\ 50-30,\ 82-18,\ 122-12,\ 290-5,\ 362-4,
\]
that is, $-475,-170,-79,-34,20,64,110,285,358$. The only perfect square is $64=8^2$, at $|n|=9$.

So $n=\boxed{\pm9}$. (Check: $\dfrac{9^4-1441}{80}=\dfrac{5120}{80}=64$.)''',
'Perfect squares|Divisibility|Polynomials',4,
note='Negative values are not squares, so they are excluded. Confirmed by a computer search over |n| <= 2000.')

# ---------------- 1774742 sequence formula
b.add(1774742,1,r'''The sequence $1,2,4,6,8,10,\dots$ starts with $1$ and then continues with the even numbers $2,4,6,\dots$. Find a formula for its $n$-th term, and give a single expression valid for all $n\ge1$.''',
r'''From the second term on, the terms go up by $2$, and the $n$-th term is $2(n-1)$ for $n\ge2$: $a_2=2$, $a_3=4$, and so on. The first term breaks this pattern ($2(1-1)=0$, but $a_1=1$). So
\[
a_n=\begin{cases}1,&n=1,\\ 2n-2,&n\ge2.\end{cases}
\]
A single expression is $a_n=2n-2+\left\lfloor\dfrac1n\right\rfloor$, because $\left\lfloor\dfrac1n\right\rfloor$ is $1$ for $n=1$ and $0$ for $n\ge2$. Another is $a_n=2n-2+0^{\,n-1}$ with the convention $0^0=1$. So $\boxed{a_n=2n-2+\left\lfloor\dfrac1n\right\rfloor}$.''',
'Arithmetic sequences|Floor and ceiling functions|Piecewise functions',2,
note='The post gives only six terms; the record states the intended rule (1, then the even numbers) so that the formula is determined.')

b.save()
