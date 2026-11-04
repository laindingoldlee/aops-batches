from qb import *
import itertools, math
b=Bank('p234_01')
FBH=lambda y,g,q: src('Junior Regional Olympiad FBH',y,'Grade %d'%g,q)

# ---------------- 1716692 marathon P1: 10 dollars to 4 children
b.add(1716692,1,r'''In how many ways can $10$ identical one-dollar bills be given out to $4$ different children if each child must receive at least one bill (and bills cannot be split)?''',
r'''Give each child one bill first. The remaining $6$ identical bills are then distributed freely among the $4$ children, which is the number of nonnegative integer solutions of $x_1+x_2+x_3+x_4=6$. By stars and bars this is
\[
\dbinom{6+3}{3}=\dbinom{9}{3}=\boxed{84}.
\]
(Equivalently, choose $3$ of the $9$ gaps between $10$ bills in a row to place dividers.)''',
'Distributions and integer solutions|Stars and bars|Combinations',2,
note='P1 of a general maths marathon; the marathon rules are not part of the record.')

# ---------------- 1716751 n^0 "method"
b.add(1716751,1,r'''A student wants to find $n$ from the equation $5\cdot6=n$. The student argues: ``Whatever we do to one side we may do to the other, so raise both sides to the power $0$. This gives $(5\cdot6)^0=n^0$, that is, $1=1$, which is true for every $n$. Hence $n$ can be any number.'' But clearly $n=30$ only. Explain exactly where the argument goes wrong.''',
r'''Doing the same thing to both sides of a true equation produces a true equation: if $5\cdot6=n$, then certainly $(5\cdot6)^0=n^0$. This step is an implication in one direction only,
\[
5\cdot6=n\ \Longrightarrow\ 1=1 ,
\]
and it can be reversed only when the operation applied is one-to-one, so that equal outputs come from equal inputs (for example adding $3$, multiplying by a nonzero number, or taking a cube).

The map $t\mapsto t^0$ sends every nonzero number to $1$, so it is not one-to-one; it throws away all information about $t$. From $n^0=1$ we learn only that $n\ne0$ (as $0^0$ is usually left undefined), not that $n=30$. The final statement ``$1=1$ for every $n$'' says nothing about which $n$ satisfy the \emph{original} equation; the set of solutions of the new equation is larger than that of the old one.

Concretely, $n=7$ satisfies $1=1$ but not $5\cdot6=n$. The only solution of the original equation is $n=\boxed{30}$. (The same mistake appears when both sides are squared: $x=3$ leads to $x^2=9$, which also has the extra solution $x=-3$.)''',
'Exponents|Logical deduction|Counterexamples',2,
note='The post asks whether some law prohibits raising both sides to the power 0; posed as "find the error". 0^0 is treated as undefined.')

# ---------------- 1715695 three MATHCOUNTS questions
b.add(1715695,1,r'''An algebra course can be scheduled in three ways during the five-day school week:
\begin{itemize}
\item it meets every one of the five days from 10:00 to 11:00 am;
\item it meets from 10:00 to 11:15 am on four of the five days;
\item it meets from 10:00 to 11:40 am on three of the five days.
\end{itemize}
In how many different ways could the course be scheduled?''',
r'''The three options are mutually exclusive, so we add the counts.
\begin{itemize}
\item Five days of one hour: all five days are used, $\dbinom55=1$ way.
\item Four days of $75$ minutes: choose the four days, $\dbinom54=5$ ways.
\item Three days of $100$ minutes: choose the three days, $\dbinom53=10$ ways.
\end{itemize}
(Each option gives $300$ minutes per week.) The total is $1+5+10=\boxed{16}$.''',
'Combinations|Addition principle',2,
note='Problem 1 of the post. The garbled "each of the four days" is read as "on four of the five days".')
b.add(1715695,2,r'''What is the sum of all positive integers $n$ such that $n+\dfrac{18}{n}$ is an integer?''',
r'''Since $n$ is an integer, $n+\dfrac{18}{n}$ is an integer exactly when $\dfrac{18}{n}$ is an integer, that is, when $n$ is a positive divisor of $18$. These are $1,2,3,6,9,18$, with sum
\[
1+2+3+6+9+18=\boxed{39}.
\]
(If the expression is read as $\dfrac{n+18}{n}=1+\dfrac{18}{n}$, the condition is the same and the answer is again $39$.)''',
'Factors and multiples|Divisibility',2,
note='The post writes n+18/n; both readings n + 18/n and (n+18)/n give the same answer 39.')
fig=r'''pair P(real x,real y,real z){return (x+0.42*z,y+0.32*z);}
pen blk=linewidth(0.9);
draw(P(0,0,10)--P(10,0,10),dashed+gray);draw(P(0,0,10)--P(0,10,10),dashed+gray);draw(P(0,0,10)--P(0,0,0),dashed+gray);
// block of eight 4-cubes, front, top and right faces
fill(P(0,0,0)--P(8,0,0)--P(8,8,0)--P(0,8,0)--cycle,rgb(0.80,0.88,1));
fill(P(0,8,0)--P(8,8,0)--P(8,8,8)--P(0,8,8)--cycle,rgb(0.70,0.80,0.98));
fill(P(8,0,0)--P(8,0,8)--P(8,8,8)--P(8,8,0)--cycle,rgb(0.62,0.74,0.95));
pen bl=blue+linewidth(0.7);
draw(P(0,0,0)--P(8,0,0)--P(8,8,0)--P(0,8,0)--cycle,bl);
draw(P(0,8,0)--P(0,8,8)--P(8,8,8)--P(8,0,8)--P(8,0,0),bl);draw(P(8,8,0)--P(8,8,8),bl);
draw(P(4,0,0)--P(4,8,0)--P(4,8,8),bl);draw(P(0,4,0)--P(8,4,0)--P(8,4,8),bl);
draw(P(0,8,4)--P(8,8,4)--P(8,0,4),bl);
// box 10 x 10 x 10
draw(P(0,0,0)--P(10,0,0)--P(10,10,0)--P(0,10,0)--cycle,blk);
draw(P(0,10,0)--P(0,10,10)--P(10,10,10)--P(10,0,10)--P(10,0,0),blk);draw(P(10,10,0)--P(10,10,10),blk);
label("$10$",P(5,10,10),N);label("$10$",P(0,5,0),W);label("$10$",P(10,0,5),SE);
label("$4$",P(2,0,0),S);label("$4$",P(6,0,0),S);'''
b.add(1715695,3,r'''What percent of the volume of a $10\times10\times10$ box can be filled with solid $4\times4\times4$ cubes (placed inside the box without overlapping, with faces parallel to the faces of the box)? Express your answer as a decimal to the nearest tenth.''',
r'''\textbf{At most $8$ cubes fit.} A cube placed in the box occupies $[a,a+4]\times[b,b+4]\times[c,c+4]$ with $0\le a,b,c\le6$. The open interval $(a,a+4)$ contains $3.5$ when $a<3.5$ and contains $6.5$ when $a>2.5$, so it always contains $3.5$ or $6.5$. Hence the interior of every cube contains one of the $8$ points whose coordinates are all $3.5$ or $6.5$. Non-overlapping cubes have disjoint interiors, so each of these points lies inside at most one cube, and there are at most $8$ cubes.

\textbf{Eight cubes fit}, in a $2\times2\times2$ block filling an $8\times8\times8$ corner of the box:
'''+asy(fig,'5.5cm')+r'''
They occupy $8\cdot64=512$ of the $1000$ cubic units, so the fraction filled is $\dfrac{512}{1000}=\boxed{51.2\%}$.''',
'Volume|Cubes and rectangular prisms|Percentages',2,
note='Problem 3 of the post. The cubes are taken to be placed with faces parallel to the faces of the box, as intended; the solution proves that at most 8 fit.')

# ---------------- 1716645 truncated octahedron
V=sorted({tuple(a*s for a,s in zip(p,sg)) for p in itertools.permutations([0,1,2]) for sg in itertools.product([1,-1],repeat=3)})
def sub(a,c): return [x-y for x,y in zip(a,c)]
def dotp(a,c): return sum(x*y for x,y in zip(a,c))
def cross(a,c): return [a[1]*c[2]-a[2]*c[1],a[2]*c[0]-a[0]*c[2],a[0]*c[1]-a[1]*c[0]]
def unit(a): l=math.sqrt(dotp(a,a)); return [x/l for x in a]
view=unit([1.2,-0.9,1.0]); up=[0,0,1]
ex=unit(cross(up,view)); ey=cross(view,ex)
ex=[-x for x in ex]
proj=lambda p:(dotp(p,ex),dotp(p,ey))
faces=[]
for i in range(3):
    for s in (2,-2):
        n=[0,0,0];n[i]=s/2;faces.append(('sq',n,[v for v in V if v[i]==s]))
for sg in itertools.product([1,-1],repeat=3):
    faces.append(('hx',list(sg),[v for v in V if dotp(v,sg)==3]))
lines=[]
for kind,n,vs in faces:
    if dotp(n,view)<=0: continue
    c=[sum(v[k] for v in vs)/len(vs) for k in range(3)]
    u1=unit(sub(vs[0],c)); u2=cross(unit(n),u1)
    vs=sorted(vs,key=lambda v: math.atan2(dotp(sub(v,c),u2),dotp(sub(v,c),u1)))
    pts='--'.join('(%.4f,%.4f)'%proj(v) for v in vs)+'--cycle'
    col='rgb(0.80,0.88,1)' if kind=='sq' else 'rgb(1,0.93,0.75)'
    lines.append('filldraw(%s,%s,linewidth(0.8));'%(pts,col))
# a corner where two hexagons and a square meet: the vertex (2,0,1)
lines.append('dot((%.4f,%.4f),red+3.5bp);'%proj((2,0,1)))
fig='\n'.join(lines)
b.add(1716645,1,r'''A truncated octahedron is a solid with $14$ faces: $6$ congruent squares and $8$ congruent regular hexagons. At each corner (vertex) exactly $2$ hexagons and $1$ square meet. How many corners does the solid have?''',
r'''Count pairs (face, corner of that face) in two ways. The faces have
\[
6\cdot4+8\cdot6=24+48=72
\]
corners in total, counted face by face. Each corner of the solid belongs to exactly $3$ faces ($2$ hexagons and $1$ square), so it has been counted $3$ times. Hence the solid has $\dfrac{72}{3}=\boxed{24}$ corners.

Check: the faces have $\dfrac{6\cdot4+8\cdot6}{2}=36$ edges (each edge lies on two faces), and Euler's formula $V-E+F=24-36+14=2$ holds. The sketch shows the solid with the squares in blue and the hexagons in yellow; the red corner is where one square and two hexagons meet.
'''+asy(fig,'5cm'),
'Polyhedra|Double counting|Euler\'s polyhedron formula',2,
note='Counted by double counting; the vertex count 24 is confirmed from the coordinates (all permutations of (0, +-1, +-2)).')

# ---------------- 1715055 twice as far from 10 as from 1
b.add(1715055,1,r'''What positive number is twice as far from $10$ as it is from $1$?''',
r'''We need $|x-10|=2|x-1|$ with $x>0$.
\begin{itemize}
\item If $x\ge10$: $x-10=2x-2$ gives $x=-8$, not in this range.
\item If $1\le x<10$: $10-x=2x-2$ gives $x=4$, which is in the range.
\item If $x<1$: $10-x=2-2x$ gives $x=-8$, which is not positive.
\end{itemize}
So the only positive number is $\boxed{4}$: it is $6$ from $10$ and $3$ from $1$. (The other solution, $-8$, is $18$ from $10$ and $9$ from $1$.)''',
'Absolute value|Linear equations',2)

# ---------------- 1715902 FBH 2015 G6 P4
b.add(1715902,1,r'''The fraction $\dfrac{\overline{28a3}}{7276}$ has a four-digit numerator whose hundreds digit is the unknown digit $a$. Find the digit $a$ and the whole number $x$ such that subtracting $x$ from the numerator and adding $x$ to the denominator gives a fraction equal to $\dfrac27$.''',
r'''The numerator is $N=2803+10a$. We need
\[
\dfrac{N-x}{7276+x}=\dfrac27\iff 7N-7x=14552+2x\iff 9x=7N-14552=19621+70a-14552=5069+70a .
\]
So $5069+70a$ must be divisible by $9$. Since $5069\equiv5+0+6+9=20\equiv2\pmod 9$ and $70\equiv7\pmod9$, we need $2+7a\equiv0$, i.e.\ $7a\equiv7\pmod9$, so $a\equiv1\pmod9$. As $a$ is a digit with $28a3$ a four-digit number, $a=1$ (the value $a=10$ is not a digit). Then $9x=5139$ and $x=571$.

Check: $\dfrac{2813-571}{7276+571}=\dfrac{2242}{7847}$ and $7\cdot2242=15694=2\cdot7847$. So $\boxed{a=1,\ x=571}$.''',
'Fractions|Divisibility rules|Linear equations|Digits and bases',3,source=FBH(2015,6,4),
note='The number to be subtracted and added is taken to be a whole number (otherwise every digit a works with a fractional x); this is what makes a unique.')

# ---------------- 1715910 FBH 2015 G7 P4 watermelons
b.add(1715910,1,r'''A seller has watermelons, melons and young corn cobs, $239$ pieces in total, with at least one of each kind. One buyer bought $\dfrac23$ of all the watermelons, $\dfrac35$ of all the melons and $\dfrac57$ of all the corn cobs. A second buyer bought $\dfrac1{13}$ of all the watermelons, $\dfrac14$ of all the melons and $\dfrac15$ of all the corn cobs. How many watermelons, melons and corn cobs did the seller have at the beginning, and how many pieces in total did the second buyer buy?''',
r'''Let the seller have $w$ watermelons, $m$ melons and $c$ corn cobs. The buyers' fractions must give whole numbers, so $w$ is divisible by $3$ and by $13$, $m$ by $5$ and by $4$, and $c$ by $7$ and by $5$:
\[
w=39i,\qquad m=20j,\qquad c=35k,\qquad i,j,k\ge1,\qquad 39i+20j+35k=239 .
\]
Reducing modulo $5$: $39i\equiv239$, i.e.\ $4i\equiv4\pmod5$, so $i\equiv1\pmod5$. Since $39\cdot6>239$, $i=1$ and $w=39$. Then $20j+35k=200$, i.e.\ $4j+7k=40$. So $4\mid7k$, $k$ is a multiple of $4$, and $k\ge1$ with $35k\le200$ forces $k=4$; then $4j=12$, $j=3$.

Hence the seller had $\boxed{39\text{ watermelons},\ 60\text{ melons and }140\text{ corn cobs}}$. The second buyer bought
\[
\dfrac{39}{13}+\dfrac{60}{4}+\dfrac{140}{5}=3+15+28=\boxed{46}\text{ pieces.}
\]
(The first buyer bought $26+36+100=162$ pieces, so together they bought $208\le239$, as they must.)''',
'Fractions|HCF and LCM|Linear Diophantine equations|Remainders and congruences',3,source=FBH(2015,7,4),
note='"At least one of each kind" is stated explicitly: without it, w=39, m=200, c=0 would also fit. Checked by exhaustive search.')

# ---------------- 1715897 FBH 2015 G6 P2 fruit exchange
b.add(1715897,1,r'''At a school fruit exchange the rates are: $11$ strawberries for $14$ raspberries, $22$ cherries for $21$ raspberries, $10$ cherries for $3$ bananas, and $5$ pears for $2$ bananas. How many pears does Amila have to give to get $7$ strawberries?''',
r'''Convert step by step, using the rates as proportions.
\[
7\text{ strawberries}=7\cdot\dfrac{14}{11}=\dfrac{98}{11}\text{ raspberries}=\dfrac{98}{11}\cdot\dfrac{22}{21}=\dfrac{28}{3}\text{ cherries},
\]
\[
\dfrac{28}{3}\text{ cherries}=\dfrac{28}{3}\cdot\dfrac{3}{10}=\dfrac{14}{5}\text{ bananas}=\dfrac{14}{5}\cdot\dfrac{5}{2}=7\text{ pears}.
\]
Amila has to give $\boxed{7}$ pears.''',
'Ratios, proportions, and variation|Fractions',2,source=FBH(2015,6,2))

# ---------------- 1715918 FBH 2015 G8 P5 Schur
b.add(1715918,1,r'''The set $X=\{1,2,\dots,9\}$ is split into two disjoint sets. Prove that at least one of the two sets contains three distinct elements such that one of them is the sum of the other two.''',
r'''Colour the elements of one set red and of the other blue, and suppose, for a contradiction, that there are no distinct $x<y$ of the same colour with $x+y$ also of that colour (call such $x,y,x+y$ a \emph{monochromatic sum}). Swapping the colours if necessary, $1$ is red.

\textbf{Case 1: $2$ is red.} Then $3=1+2$ is blue.
\begin{itemize}
\item If $4$ is red, then $5=1+4$ and $6=2+4$ are blue; then $8=3+5$ and $9=3+6$ are red, and $1+8=9$ is a red monochromatic sum. Contradiction.
\item If $4$ is blue, then $7=3+4$ is red, so $8=1+7$ and $9=2+7$ are blue. Now $5$ cannot be blue ($4+5=9$) and cannot be red ($2+5=7$). Contradiction.
\end{itemize}

\textbf{Case 2: $2$ is blue.}
\begin{itemize}
\item If $3$ is red, then $4=1+3$ is blue, so $6=2+4$ is red; then $7=1+6$ and $9=3+6$ are blue, and $2+7=9$ is a blue monochromatic sum. Contradiction.
\item If $3$ is blue, then $5=2+3$ is red, so $4$ is blue (as $1+4=5$) and $6$ is blue (as $1+5=6$). Then $2+4=6$ is a blue monochromatic sum. Contradiction.
\end{itemize}
Every case leads to a contradiction, so one of the two sets contains distinct $x,y$ and $x+y$. $\blacksquare$

(The number $9$ cannot be lowered: $\{1,2,4,8\}$ and $\{3,5,6,7\}$ split $\{1,\dots,8\}$ with no such triple.)''',
'Proof by cases|Proof by contradiction|Colourings, tilings, and coverings',4,source=FBH(2015,8,5),
note='"Three elements" is read as three distinct elements x, y, x+y. Checked by testing all 512 splittings; the remark that 8 does not suffice is also checked.')

# ---------------- 1715894 FBH 2015 G6 P1
b.add(1715894,1,r'''Find two angles whose sum is $180^\circ$ and whose difference is $1'$ (one minute of arc).''',
r'''Let the angles be $\alpha>\beta$ with $\alpha+\beta=180^\circ$ and $\alpha-\beta=1'$. Adding and halving,
\[
\alpha=\dfrac{180^\circ+1'}{2}=90^\circ+30''=90^\circ0'30'',\qquad \beta=180^\circ-\alpha=89^\circ59'30'' ,
\]
since $1'=60''$ and half of it is $30''$. So the angles are $\boxed{90^\circ0'30''\text{ and }89^\circ59'30''}$. Check: $90^\circ0'30''-89^\circ59'30''=1'$.''',
'Unit conversion|Systems of linear equations',2,source=FBH(2015,6,1))

# ---------------- 1715905 FBH 2015 G7 P1 trucks
b.add(1715905,1,r'''Each of the six trucks of a construction company drove for $8$ hours, and together they used $720$ litres of fuel. How many litres would $9$ such trucks use if each of them drives for $6$ hours?''',
r'''The six trucks drove $6\cdot8=48$ truck-hours, so one truck uses $\dfrac{720}{48}=15$ litres per hour. Nine trucks driving $6$ hours each make $54$ truck-hours and use $54\cdot15=\boxed{810}$ litres.''',
'Ratios, proportions, and variation|Work and rates',2,source=FBH(2015,7,1),
note='"Oil" in the translation is fuel; fuel use is assumed proportional to driving time.')

# ---------------- 1715914 FBH 2015 G8 P2
b.add(1715914,1,r'''Let $a,b,c$ be pairwise distinct numbers. Show that the value of
\[
A=\dfrac{(b-c)^2}{(a-b)(a-c)}+\dfrac{(c-a)^2}{(b-c)(b-a)}+\dfrac{(a-b)^2}{(c-a)(c-b)}
\]
does not depend on $a$, $b$ and $c$, and find it.''',
r'''Put $x=a-b$, $y=b-c$, $z=c-a$; these are nonzero and $x+y+z=0$. Then $a-c=-z$, $b-a=-x$, $c-b=-y$, so
\[
A=\dfrac{y^2}{x(-z)}+\dfrac{z^2}{y(-x)}+\dfrac{x^2}{z(-y)}=-\dfrac{x^3+y^3+z^3}{xyz}.
\]
By the identity
\[
x^3+y^3+z^3-3xyz=(x+y+z)(x^2+y^2+z^2-xy-yz-zx)
\]
and $x+y+z=0$ we get $x^3+y^3+z^3=3xyz$. Hence
\[
A=-\dfrac{3xyz}{xyz}=\boxed{-3}
\]
for all pairwise distinct $a,b,c$. (For example $a=0$, $b=1$, $c=2$ gives $\dfrac12-4+\dfrac12=-3$.)''',
'Algebraic expressions and identities|Substitution|Factoring',4,source=FBH(2015,8,2),
note='The condition that a, b, c are pairwise distinct (needed for A to be defined) is stated; the constant value -3 is asked for. Verified symbolically.')

# ---------------- 1715917 FBH 2015 G8 P4
b.add(1715917,1,r'''Let $n$ be a positive integer, $a=2^n\cdot7^{n+1}+11$ and $b=2^{n+1}\cdot7^n+3$.
\begin{enumerate}
\item[(a)] Prove that the fraction $\dfrac ab$ is in lowest terms.
\item[(b)] Prove that $a+b-7$ is not a perfect square for any positive integer $n$.
\end{enumerate}''',
r'''Write $t=14^n=2^n7^n$. Then $a=7t+11$ and $b=2t+3$.

\textbf{(a)} We have
\[
2a-7b=(14t+22)-(14t+21)=1 .
\]
Any common divisor of $a$ and $b$ divides $2a-7b=1$, so $\gcd(a,b)=1$ and $\dfrac ab$ is in lowest terms.

\textbf{(b)} Here $a+b-7=9t+7=9\cdot14^n+7$.
\begin{itemize}
\item For $n=1$: $9\cdot14+7=133$, which lies strictly between $11^2=121$ and $12^2=144$.
\item For $n\ge2$: $14^n$ is divisible by $7^2=49$, so $9\cdot14^n+7\equiv7\pmod{49}$. The number is divisible by $7$ but not by $49$. A perfect square divisible by the prime $7$ is divisible by $49$, so it is not a square.
\end{itemize}
Hence $a+b-7$ is never a perfect square. $\blacksquare$''',
'HCF and LCM|Divisibility|Perfect squares|Remainders and congruences',3,source=FBH(2015,8,4),
note='Both parts kept in one record. Checked numerically for n up to 60.')

# ---------------- 1715915 FBH 2015 G8 P3
fig=r'''pair A=(1.5,4),B=(0,0),C=(6,0),D=(B+C)/2;
pair Ep=B+0.5*(A-B);
pair F=extension(D,D+rotate(90)*(Ep-D),A,C);
pair Ep2=2*D-Ep;
void ra(pair P,pair U,pair V,real s){draw(P+s*unit(U-P)--P+s*unit(U-P)+s*unit(V-P)--P+s*unit(V-P),linewidth(0.5));}
draw(A--B--C--cycle,linewidth(0.9));
draw(Ep--D--F,linewidth(0.8));draw(Ep--F,linewidth(0.8));
draw(D--Ep2,blue+dashed);draw(C--Ep2,blue+dashed);draw(F--Ep2,blue+dashed);
ra(D,Ep,F,0.3);
dot(D);dot(Ep);dot(F);dot(Ep2,blue);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,E);label("$D$",D,dir(-100));
label("$E$",Ep,W);label("$F$",F,NE);label("$E'$",Ep2,SE,blue);'''
b.add(1715915,1,r'''Let $D$ be the midpoint of side $BC$ of triangle $ABC$. Points $E$ and $F$ lie on sides $AB$ and $AC$ respectively (not at the vertices), such that $\angle EDF=90^\circ$. Prove that $BE+CF>EF$.''',
r'''Let $E'$ be the reflection of $E$ in $D$, so that $D$ is the midpoint of $EE'$.
'''+asy(fig,'6cm')+r'''
\textbf{$CE'=BE$.} The segments $BC$ and $EE'$ bisect each other at $D$, so $EBE'C$ is a parallelogram (or, directly, triangles $DBE$ and $DCE'$ are congruent by SAS with the vertical angles at $D$). Hence $CE'=BE$.

\textbf{$FE'=FE$.} Since $\angle EDF=90^\circ$ and $D$ is the midpoint of $EE'$, the line $DF$ is the perpendicular bisector of $EE'$, so $FE'=FE$.

\textbf{Triangle inequality.} In triangle $FCE'$,
\[
CF+CE'\ge FE',\qquad\text{that is,}\qquad CF+BE\ge EF ,
\]
with equality only if $C$ lies on segment $FE'$. That would put $E'$ on line $AC$. But $CE'\parallel BE$, i.e.\ $CE'$ is parallel to $AB$, and the line through $C$ parallel to $AB$ meets line $AC$ only at $C$; so $E'=C$ and $E=B$, which is excluded. Therefore $BE+CF>EF$. $\blacksquare$''',
'Triangles|Triangle inequality|Reflections|Midpoints|Perpendicular bisectors|Parallelograms',4,source=FBH(2015,8,3),
note='E and F are taken strictly inside the sides (if E = B the inequality becomes an equality). Checked numerically on random configurations.')

# ---------------- 1715908 FBH 2015 G7 P3
fig=r'''real r=sqrt(58)/2;
pair B=(-r,0),D=(r,0),A=(0,r);
real x=10/r; pair C=(x,-sqrt(r^2-x^2));
void ra(pair P,pair U,pair V,real s){draw(P+s*unit(U-P)--P+s*unit(U-P)+s*unit(V-P)--P+s*unit(V-P),linewidth(0.5));}
draw(A--B--C--D--cycle,linewidth(0.9));
draw(B--D,dashed+gray);
ra(A,B,D,0.45);ra(C,B,D,0.45);
// equal-length ticks on AB and AD
pair m1=(A+B)/2,m2=(A+D)/2;
draw(m1+0.22*unit(rotate(90)*(B-A))--m1-0.22*unit(rotate(90)*(B-A)));
draw(m2+0.22*unit(rotate(90)*(D-A))--m2-0.22*unit(rotate(90)*(D-A)));
label("$A$",A,N);label("$B$",B,W);label("$C$",C,S);label("$D$",D,E);
label("$a$",m1+0.6*unit(rotate(-90)*(B-A)));label("$a$",m2+0.6*unit(rotate(90)*(D-A)));
label("$x$",(B+C)/2,SW);label("$y$",(C+D)/2,SE);'''
b.add(1715908,1,r'''In quadrilateral $ABCD$ the angles at $A$ and $C$ are right angles, $AB=AD$, and $BC+CD=10$. Find the area of $ABCD$.''',
r'''Let $AB=AD=a$, $BC=x$, $CD=y$, so $x+y=10$. The diagonal $BD$ is the hypotenuse of both right triangles $BAD$ and $BCD$:
'''+asy(fig,'5.5cm')+r'''
\[
BD^2=a^2+a^2=2a^2\qquad\text{and}\qquad BD^2=x^2+y^2 .
\]
The area is the sum of the areas of the two right triangles:
\[
[ABCD]=\dfrac{a^2}{2}+\dfrac{xy}{2}=\dfrac{2a^2+2xy}{4}=\dfrac{x^2+y^2+2xy}{4}=\dfrac{(x+y)^2}{4}=\dfrac{100}{4}=\boxed{25}.
\]
(The answer does not depend on how the sum $10$ is split between $x$ and $y$; the figure shows $x=7$, $y=3$.)''',
'Quadrilaterals and polygons|Right triangles|Pythagorean theorem|Lengths, perimeter, and area|Isosceles triangles',4,source=FBH(2015,7,3),
note='"Two opposite angles are right; two sides which form a right angle are equal" is read as: the angles at A and C are right, the sides AB = AD at the right angle A are equal, and BC + CD = 10. Checked numerically for several splits.')

# ---------------- 1715903 FBH 2015 G6 P5
b.add(1715903,1,r'''In how many ways can you pay exactly $\$2015$ using bills of $\$1$, $\$10$, $\$100$ and $\$200$ (any number of each kind, including none)?''',
r'''Let the payment use $p$ bills of $\$200$ and $q$ bills of $\$100$, and put $m=2p+q$, so these bills make $100m$ dollars with $0\le m\le20$. For a given $m$ there are $\left\lfloor\dfrac m2\right\rfloor+1$ pairs $(p,q)$ (namely $p=0,1,\dots,\lfloor\dfrac m2\rfloor$).

The remaining $R=2015-100m$ dollars are paid with tens and ones; the number of tens can be any of $0,1,\dots,\left\lfloor\dfrac R{10}\right\rfloor=201-10m$, and the ones make up the rest, so there are $202-10m$ ways. Hence the total is
\[
\sum_{m=0}^{20}\left(\left\lfloor\dfrac m2\right\rfloor+1\right)(202-10m).
\]
Grouping $m=2k$ and $m=2k+1$ (both with $\lfloor\dfrac m2\rfloor+1=k+1$) for $k=0,\dots,9$, plus $m=20$:
\[
\sum_{k=0}^{9}(k+1)\bigl[(202-20k)+(192-20k)\bigr]+11\cdot2=\sum_{k=0}^{9}(k+1)(394-40k)+22 .
\]
With $j=k+1$ running from $1$ to $10$, $(k+1)(394-40k)=j(434-40j)=434j-40j^2$, so the sum is
\[
434\cdot55-40\cdot385+22=23870-15400+22=\boxed{8492}.
\]''',
'Money and currency|Systematic counting|Linear Diophantine equations|Summation',4,source=FBH(2015,6,5),
note='Count checked by direct enumeration.')

# ---------------- 1715912 FBH 2015 G8 P1 ages
b.add(1715912,1,r'''A father is $42$ years old and his son is $14$. In how many years will the father be twice as old as his son?''',
r'''In $x$ years the father will be $42+x$ and the son $14+x$. We need $42+x=2(14+x)=28+2x$, so $x=\boxed{14}$. Then the father is $56$ and the son $28$.''',
'Age problems|Linear equations',1,source=FBH(2015,8,1))

# ---------------- 1715911 FBH 2015 G7 P5
b.add(1715911,1,r'''There are $2015$ numbers written on a board. If every number is replaced by the sum of the other $2014$ numbers, the board shows the same $2015$ numbers as before (possibly in a different order). Prove that the product of the $2015$ numbers is $0$.''',
r'''Let the numbers be $a_1,\dots,a_{2015}$ and $S=a_1+\dots+a_{2015}$. The new numbers are $S-a_1,\dots,S-a_{2015}$, and they form the same collection (with multiplicities) as the old ones.

\textbf{The sum is $0$.} The two collections have the same sum:
\[
\sum_{i}(S-a_i)=2015S-S=2014S=S ,
\]
so $2013S=0$ and $S=0$.

\textbf{The collection is symmetric.} With $S=0$ the new numbers are $-a_1,\dots,-a_{2015}$. So the collection is unchanged when every number is replaced by its negative: for every $x\ne0$ the number $x$ occurs exactly as often as $-x$.

\textbf{A zero exists.} Pair each occurrence of a nonzero $x>0$ with an occurrence of $-x$. This pairs up all the nonzero numbers, so their count is even. Since $2015$ is odd, at least one of the numbers is $0$, and the product of all the numbers is $0$. $\blacksquare$''',
'Pairing and grouping|Parity|Summation',4,source=FBH(2015,7,5),
note='"We get the same 2015 numbers" is read as the same multiset of numbers.')

# ---------------- 1715907 FBH 2015 G7 P2 shirt
b.add(1715907,1,r'''A seller reduced the price of a shirt by $20\%$ and then raised the new price by $10\%$. Should he now reduce or raise the price, and by what percent of the current price, so that the final price is $10\%$ lower than the original price?''',
r'''Let the original price be $P$. After the two changes the price is
\[
P\cdot0.8\cdot1.1=0.88P .
\]
The target is $0.9P$, which is higher, so the seller must \emph{raise} the price, by
\[
\dfrac{0.9P-0.88P}{0.88P}=\dfrac{0.02}{0.88}=\dfrac{1}{44}=\dfrac{100}{44}\%=\boxed{2\dfrac{3}{11}\%}\approx2.27\% .
\]''',
'Percentages',2,source=FBH(2015,7,2))

# ---------------- 1715031 FBH 2016 G6 P3
b.add(1715031,1,r'''There are three boys and three girls. Every boy knows exactly two of the girls, and every girl knows exactly two of the boys. Prove that they can be split into three boy-girl pairs such that in every pair the two people know each other.''',
r'''Each boy does \emph{not} know exactly one girl, and each girl does not know exactly one boy. So ``does not know'' pairs each boy with exactly one girl and each girl with exactly one boy: it is a one-to-one correspondence. Name the boys $B_1,B_2,B_3$ and let $G_i$ be the girl whom $B_i$ does not know; then $G_1,G_2,G_3$ are the three girls, each appearing once, and $B_i$ knows every girl except $G_i$.

Now form the pairs
\[
(B_1,G_2),\qquad(B_2,G_3),\qquad(B_3,G_1).
\]
Every boy and every girl appears exactly once, and in each pair $(B_i,G_j)$ we have $j\ne i$, so $B_i$ knows $G_j$. This is the required pairing. $\blacksquare$

(In fact the ``knows'' relation is a $6$-cycle $B_1G_2B_3G_1B_2G_3B_1$, which has two such pairings.)''',
'Graph theory|Logical deduction|Construction',3,source=FBH(2016,6,3),
note='Knowing is assumed mutual (if a boy knows a girl, she knows him).')

# ---------------- 1715644 pi^7 estimate
b.add(1715644,1,r'''Without a calculator or paper, estimate $\pi^7$ to within $5\%$ of its true value. Justify that your estimate is accurate enough.''',
r'''Use $\pi^2\approx9.87$ (from $\pi\approx3.1416$), which is close to $10$:
\[
\pi^7=\pi\cdot\left(\pi^2\right)^3\approx\pi\cdot10^3=1000\pi\approx3142 .
\]
\textbf{How good is this?} $\pi^7=1000\pi\left(\dfrac{\pi^2}{10}\right)^3$ and $0.986<\dfrac{\pi^2}{10}<0.988$, so $\left(\dfrac{\pi^2}{10}\right)^3$ lies between $0.986^3>1-3(0.014)=0.958$ and $0.988^3<1$. Hence $1000\pi$ overestimates $\pi^7$ by less than about $4.4\%$, which is within $5\%$. A better estimate uses $0.987^3\approx1-0.039=0.961$:
\[
\pi^7\approx3142\cdot0.961\approx\boxed{3020}.
\]
(The true value is $\pi^7=3020.29\ldots$; the quick estimate $1000\pi\approx3142$ is $4.0\%$ too large.)

Another mental route: $\pi=3(1.0472)$, so $\pi^7=2187\cdot1.0472^7$ and $1.0472^7\approx1+7(0.0472)+21(0.0472)^2+35(0.0472)^3\approx1.381$, giving about $3020$.''',
'Estimation|Exponents|Binomial theorem',3,
note='Number-sense question: the post asks how to approximate pi^7 within 5% mentally; the record asks for such an estimate with justification. Any value between about 2870 and 3170 is acceptable.')

# ---------------- 1715047 FBH 2016 G7 P3
b.add(1715047,1,r'''Prove that when a prime number is divided by $30$, the remainder is never a composite number.''',
r'''Let $p$ be a prime and $p=30q+r$ with $0\le r\le29$. Suppose $r$ is composite. A composite number $r\le29$ has a prime factor $s$ with $s^2\le r<49$, so $s\in\{2,3,5\}$; in particular $s\mid30$. Then $s$ divides $30q+r=p$. Since $p$ is prime, $p=s\le5$. But a prime $p\le5<30$ leaves remainder $r=p$ on division by $30$, and $p$ is prime, not composite. This contradiction shows that $r$ is not composite: the remainder is $1$ or a prime (for example $31\to1$, $37\to7$, $59\to29$). $\blacksquare$''',
'Prime numbers|Remainders and congruences|Divisibility|Proof by contradiction',3,source=FBH(2016,7,3),
note='Checked for all primes below 10^6.')

# ---------------- 1715602 telescoping
b.add(1715602,1,r'''If $f(x)=4x^2-1$, what is the value of
\[
\dfrac1{f(1)}+\dfrac1{f(2)}+\dfrac1{f(3)}+\cdots+\dfrac1{f(84)}\,?
\]''',
r'''Since $4x^2-1=(2x-1)(2x+1)$,
\[
\dfrac1{f(x)}=\dfrac{1}{(2x-1)(2x+1)}=\dfrac12\left(\dfrac1{2x-1}-\dfrac1{2x+1}\right).
\]
The sum telescopes:
\[
\sum_{x=1}^{84}\dfrac1{f(x)}=\dfrac12\left(\dfrac11-\dfrac13+\dfrac13-\dfrac15+\cdots+\dfrac1{167}-\dfrac1{169}\right)=\dfrac12\left(1-\dfrac1{169}\right)=\boxed{\dfrac{84}{169}}.
\]''',
'Telescoping sums|Partial fractions|Summation|Difference of squares',3)

# ---------------- 1713845 variation
b.add(1713845,1,r'''$x$ varies directly with $z^2$. When $z$ doubles, by what factor does $x$ change? Does $x$ increase or decrease?''',
r'''Direct variation means $x=kz^2$ for a constant $k$. Replacing $z$ by $2z$ gives
\[
k(2z)^2=4kz^2=4x .
\]
So $x$ is multiplied by $\boxed{4}$: it \emph{increases} (for $k\ne0$), it does not decrease. (Saying that $x$ ``decreases by a factor of $4$'' would be wrong; it is the quantity $\dfrac{1}{x}$ that is divided by $4$.)''',
'Ratios, proportions, and variation',1,
note='The original asks "by what factor does x decrease?" (the poster says "decrease" is not a typo, i.e. a trick question); the record asks for the factor and the direction.')
b.add(1713845,2,r'''The kinetic energy $K$ of a body of mass $m$ moving with speed $v$ is $K=\dfrac{mv^2}{2}$. Describe this relation in words as a variation, and state what happens to $K$ when (a) $v$ is doubled with $m$ fixed, (b) $m$ is doubled with $v$ fixed.''',
r'''$K$ varies jointly as the mass $m$ and the square of the speed $v$, with constant of variation $\dfrac12$: $K$ is directly proportional to $m$ when $v$ is fixed, and directly proportional to $v^2$ when $m$ is fixed.

(a) Doubling $v$ multiplies $v^2$ by $4$, so $K$ is multiplied by $\boxed{4}$.

(b) Doubling $m$ multiplies $K$ by $\boxed{2}$.''',
'Ratios, proportions, and variation',1,
note='The post asks to "describe this relation in words"; two concrete follow-up questions were added so the record has checkable answers.')
b.add(1713845,3,r'''The variable $y$ varies directly with $x$, and $z$ varies inversely with $y$. When $x=3$, we have $y=18$ and $z=5$. What is $y+z$ when $x=15$?''',
r'''Write $y=kx$ and $z=\dfrac{c}{y}$. From $x=3$, $y=18$: $k=6$. From $y=18$, $z=5$: $c=90$. When $x=15$: $y=6\cdot15=90$ and $z=\dfrac{90}{90}=1$, so $y+z=\boxed{91}$.''',
'Ratios, proportions, and variation',2,
note='From a MathCounts team selection test (as stated in the post).')

# ---------------- 1715429 prism distance
fig=r'''pair d=(3.6,1.4); // drawn depth for the height 1 (not to scale)
real h=sqrt(91);
pair B1=(-3,0),B2=(3,0),T=(0,h),M=(0,0);
pair B1b=B1+d,B2b=B2+d,Tb=T+d,Mb=M+d;
draw(B1b--B2b,dashed+gray);draw(B1b--B1,dashed+gray);draw(B1b--Tb,dashed+gray);
draw(B1--B2--T--cycle,linewidth(0.9));
draw(T--Tb--B2b--B2,linewidth(0.9));
draw(T--M,blue+dashed);draw(M--Mb,blue+dashed);
draw(T--Mb,red+linewidth(0.9));
void ra(pair P,pair U,pair V,real s){draw(P+s*unit(U-P)--P+s*unit(U-P)+s*unit(V-P)--P+s*unit(V-P),linewidth(0.5));}
ra(M,T,B2,0.4);
dot(T);dot(Mb,red);
label("$T$",T,N);label("$M$",M,S);label("$M'$",Mb,NE);
label("$3$",(B1+M)/2,S);label("$3$",(M+B2)/2,S);
label("$10$",(B1+T)/2,W);
label("$1$",(B2+B2b)/2,SE);
label("$\sqrt{91}$",(-1.1,2.1),blue);'''
b.add(1715429,1,r'''A triangular prism has height $1$, and its two bases are isosceles triangles with side lengths $10,10,6$. Let $T$ be the apex (the vertex between the two sides of length $10$) of one base, and let $M'$ be the midpoint of the side of length $6$ of the \emph{other} base. Find the distance $TM'$.''',
r'''Let $M$ be the midpoint of the side of length $6$ in the base containing $T$; then $M'$ is the image of $M$ in the other base, and $MM'=1$ is a lateral edge direction perpendicular to the base.

In the isosceles base, the median $TM$ to the side of length $6$ is also an altitude, so
\[
TM=\sqrt{10^2-3^2}=\sqrt{91}.
\]
Since $MM'$ is perpendicular to the plane of the base, it is perpendicular to $TM$, and triangle $TMM'$ has a right angle at $M$:
\[
TM'=\sqrt{TM^2+MM'^2}=\sqrt{91+1}=\sqrt{92}=\boxed{2\sqrt{23}}.
\]
The sketch is not to scale (the height $1$ is drawn larger so the back face is visible).
'''+asy(fig,'5cm'),
'Solid geometry|Pythagorean theorem|Isosceles triangles|Right triangles',3,
note='The post asks for the distance from "the upper tip of the prism" to the point dividing "the lower back edge" (of length 6) into two equal parts; read as the apex of one base and the midpoint of the side of length 6 of the other base, with the prism a right prism of height 1.')

# ---------------- 1715432 12 students in a row
b.add(1715432,1,r'''There are $12$ students at a party, $5$ of whom are girls and $7$ boys. In how many ways can the $12$ students be arranged in a row if
\begin{enumerate}
\item[(i)] the $5$ girls must be together;
\item[(ii)] no two girls are adjacent;
\item[(iii)] between two particular boys $A$ and $B$ there are no boys but exactly $3$ girls?
\end{enumerate}''',
r'''\textbf{(i)} Glue the girls into one block. The block and the $7$ boys can be arranged in $8!$ ways, and the girls inside the block in $5!$ ways:
\[
8!\cdot5!=40320\cdot120=\boxed{4838400}.
\]

\textbf{(ii)} Arrange the $7$ boys in $7!$ ways. They create $8$ gaps (including both ends); the girls go into $5$ different gaps, in order, in $8\cdot7\cdot6\cdot5\cdot4=6720$ ways:
\[
7!\cdot6720=5040\cdot6720=\boxed{33868800}.
\]

\textbf{(iii)} The block is $A$, three girls, $B$ (or $B$, three girls, $A$): $2$ orders of $A,B$, and $5\cdot4\cdot3=60$ ordered choices of the three girls. Treat the block of $5$ people as one unit; with the remaining $7$ students ($5$ boys and $2$ girls) there are $8$ units, arranged in $8!$ ways:
\[
2\cdot60\cdot8!=120\cdot40320=\boxed{4838400}.
\]''',
'Permutations|Arrangements with restrictions|Multiplication principle',3,
note='All three counts checked by direct computation over gender patterns and position pairs.')

b.save()
