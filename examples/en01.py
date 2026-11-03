from qb import *
b=Bank('en01')

# ---------------- 1792761 Frobenius 11, 13 (alias)
b.add(1792761,1,r'''The country of Kurtlandia has a coin worth $11$ cents and a coin worth $13$ cents. What is the largest number of cents that cannot be made using these coins?''',
r'''Since $13\equiv2\pmod{11}$, the amounts $13b$ for $b=0,1,\dots,10$ cover all eleven remainders modulo $11$, and any amount with $b\ge11$ coins of $13$ can be rewritten with $b-11$ coins of $13$ and $13$ more coins of $11$. So in the remainder class of $13b$ ($0\le b\le10$) the amounts that can be made are exactly $13b,13b+11,13b+22,\dots$. The largest starting value is $130$, and $130-11=119$ cannot be made, while every larger amount can. The answer is $\boxed{119}=11\cdot13-11-13$.''',
'Linear Diophantine equations|Remainders and congruences|Money and currency',3,
note='Math Is Cool problem; repeat of an earlier record (aliased).')

# ---------------- 1793819 floor(nx)=n floor(x)
b.add(1793819,1,r'''Let $x$ be a real number such that $\lfloor nx\rfloor=n\lfloor x\rfloor$ for every positive integer $n$. Prove that $x$ is an integer.''',
r'''Write $x=k+f$ with $k=\lfloor x\rfloor$ an integer and $0\le f<1$. For every positive integer $n$, $nx=nk+nf$ with $nk$ an integer, so
\[
\lfloor nx\rfloor=nk+\lfloor nf\rfloor .
\]
The hypothesis $\lfloor nx\rfloor=nk$ therefore says $\lfloor nf\rfloor=0$, that is, $nf<1$, for every positive integer $n$.

Suppose $f>0$. Choose a positive integer $n\ge\dfrac1f$; then $nf\ge1$, a contradiction. Hence $f=0$ and $x=k$ is an integer. $\blacksquare$

(Conversely, every integer $x$ satisfies $\lfloor nx\rfloor=nx=n\lfloor x\rfloor$. For a non-integer such as $x=\dfrac12$ the condition already fails at $n=2$: $\lfloor1\rfloor=1\ne2\lfloor\dfrac12\rfloor=0$.)''',
'Floor and ceiling functions|Proof by contradiction',2,
note='The post states the claim "if [nx]=n[x] for any natural n then x is a whole number" with [ ] read as the floor function; it is posed as a proof.')

# ---------------- 1793329 dance club
b.add(1793329,1,r'''A dance club has $19$ members, some young men and some girls (at least one of each). At every dance exactly one young man and one girl are on the dance floor, and the other $17$ members wait in a single queue. Before each new dance, the first person in the queue replaces the dancer of the same gender on the floor, and the replaced dancer goes to the back of the queue. Prove that, sooner or later, every young man dances with every girl.''',
r'''Let there be $m$ young men and $g$ girls, with $m+g=19$ and $m,g\ge1$.

\textbf{The men rotate.} List the men in a cyclic order: the man dancing at the start, followed by the men of the queue in queue order; call them $M_0,M_1,\dots,M_{m-1}$. Call a change a \emph{man-step} if the first person in the queue is a man. At a man-step the first man of the queue goes onto the floor and the dancing man goes to the back of the queue, i.e.\ behind all the other men; a girl-step does not change the order of the men. So the list of men (dancer first, then queue order) is rotated by one place at each man-step, and after $a$ man-steps the dancing man is $M_{a \bmod m}$. In the same way, with the girls listed as $G_0,\dots,G_{g-1}$, after $b$ girl-steps the dancing girl is $G_{b\bmod g}$.

\textbf{The gender pattern repeats every $17$ changes.} At each change the person removed from the front of the queue is replaced at the back by a person of the same gender. Hence the pattern of genders along the queue is just shifted cyclically, and the gender of the person at the front at the $s$-th change is the gender of the person in position $s$ (counted cyclically modulo $17$) of the initial queue. The initial queue contains $m-1$ men and $g-1$ girls, so every block of $17$ consecutive changes contains exactly $m-1$ man-steps and $g-1$ girl-steps.

\textbf{Conclusion.} After $17k$ changes there have been $k(m-1)$ man-steps and $k(g-1)$ girl-steps, so the couple on the floor is
\[
M_{k(m-1)\bmod m}=M_{-k\bmod m}\quad\text{and}\quad G_{k(g-1)\bmod g}=G_{-k\bmod g}.
\]
Since $19$ is prime and $1\le m\le18$, $\gcd(m,g)=\gcd(m,19-m)=\gcd(m,19)=1$. Given any man $M_i$ and girl $G_j$, the Chinese remainder theorem gives a $k\ge0$ with $k\equiv-i\pmod m$ and $k\equiv-j\pmod g$; after $17k$ changes $M_i$ dances with $G_j$. Therefore every young man dances with every girl (in fact infinitely often, since $k$ can be increased by multiples of $mg$). $\blacksquare$''',
'Process simulation|Invariants and monovariants|Chinese remainder theorem|Remainders and congruences',5,source=src('Bulgaria National Olympiad',None,'Grade 7',None,rnd='2'),
note='Bulgarian NMO, 2nd round, Grade 7 (year not given). The translation "prove that ever again" is read as "sooner or later"; the assumption that there is at least one young man and one girl is stated. The claim was checked by simulation for every split m+g=19 and random queues.')

# ---------------- 1791587 AM-GM minimum
b.add(1791587,1,r'''Let $x$ and $y$ be positive real numbers such that $x+2y=8$. Determine the minimum value of
\[
x+y+\dfrac{3}{x}+\dfrac{9}{2y}.
\]''',
r'''Split the expression so that each piece can be bounded by AM-GM:
\[
x+y+\dfrac3x+\dfrac{9}{2y}=\left(\dfrac{3x}{4}+\dfrac3x\right)+\left(\dfrac y2+\dfrac{9}{2y}\right)+\dfrac{x+2y}{4}.
\]
By AM-GM, $\dfrac{3x}{4}+\dfrac3x\ge2\sqrt{\dfrac94}=3$ with equality when $x^2=4$, and $\dfrac y2+\dfrac{9}{2y}\ge2\sqrt{\dfrac94}=3$ with equality when $y^2=9$. The last term is $\dfrac84=2$. Hence the expression is at least $3+3+2=8$.

Equality needs $x=2$ and $y=3$, and indeed $2+2\cdot3=8$; then the value is $2+3+\dfrac32+\dfrac32=8$. The minimum is $\boxed{8}$.''',
'AM-GM inequality|Maxima and minima|Inequalities',4)

# ---------------- 1793269 gcd (alias)
b.add(1793269,1,r'''Prove that $\gcd\bigl(n!+1,\ (n+1)!+1\bigr)=1$ for every positive integer $n$.''',
r'''Let $d$ be the gcd. Since $(n+1)!+1-(n+1)(n!+1)=-n$, $d$ divides $n$. A prime $p$ dividing $d$ would divide $n$, so $p\le n$ and $p\mid n!$; with $p\mid n!+1$ this gives $p\mid1$, impossible. So $d=1$. $\blacksquare$''',
'HCF and LCM|Factorials|Divisibility|Prime numbers',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1793574 ages and mixture
b.add(1793574,1,r'''Anita is $4\dfrac12$ years older than Basilio. Three times Anita's age added to six times Basilio's age is $36$. Find the age of each person.

A student sets up the system $y=4.5x$, $3x+6y=36$. Explain what is wrong with it.''',
r'''Let Anita be $a$ years old and Basilio $b$ years old. ``$4\dfrac12$ years older'' means $a=b+4.5$ (add $4.5$), not $a=4.5b$ ($4.5$ \emph{times} as old). The second condition is $3a+6b=36$. Substituting,
\[
3(b+4.5)+6b=36\ \Longrightarrow\ 9b+13.5=36\ \Longrightarrow\ 9b=22.5\ \Longrightarrow\ b=2.5,
\]
and $a=7$. So Anita is $\boxed{7}$ years old and Basilio is $\boxed{2\dfrac12}$ years old. Check: $3\cdot7+6\cdot2.5=21+15=36$.

The student's system has two errors: $y=4.5x$ says one age is $4.5$ times the other, and in $3x+6y=36$ the variables are swapped relative to the first equation if $y$ is Anita's age ($3$ must multiply Anita's age).''',
'Systems of linear equations|Age problems|Linear equations',1,
note='The post asks whether y = 4.5x and 3x + 6y = 36 are the right equations; the record asks for the ages and for the error (4.5 years older means add 4.5).')
b.add(1793574,2,r'''A chemistry lab needs to make $100$ gallons of an $18\%$ acid solution by mixing a $12\%$ acid solution with a $20\%$ acid solution. How many gallons of each solution are needed?''',
r'''Let $x$ gallons of the $12\%$ solution and $y$ gallons of the $20\%$ solution be used. The volumes and the amounts of acid must add up:
\[
x+y=100,\qquad 0.12x+0.20y=0.18\cdot100=18 .
\]
(The acid equation multiplies each volume by its percentage; writing just $0.12+0.20=100$ leaves out the volumes.) From the first equation $y=100-x$, so $0.12x+20-0.20x=18$, giving $0.08x=2$ and $x=25$. So $\boxed{25\text{ gallons of the }12\%\text{ solution and }75\text{ gallons of the }20\%\text{ solution}}$. Check: $3+15=18$ gallons of acid.''',
'Mixture problems|Systems of linear equations|Percentages',2,
note='The poster asks how to write the equations (suggesting 0.12 + 0.20 = 100); the solution explains the acid-amount equation.')

# ---------------- 1793467 sum and difference
b.add(1793467,1,r'''Find two numbers whose sum is $12$ and whose difference is $4$.''',
r'''The difference of two numbers is the larger minus the smaller. Let the larger number be $x$; then the smaller is $x-4$, and
\[
x+(x-4)=12\ \Longrightarrow\ 2x=16\ \Longrightarrow\ x=8 .
\]
The numbers are $\boxed{8\text{ and }4}$. (Check: $8+4=12$, $8-4=4$.)''',
'Systems of linear equations|Linear equations',1,
note='The poster asks what "difference" means and whether x + x - 4 = 12 is right; it is, with x the larger number.')
b.add(1793467,2,r'''The difference of two numbers is $3$ and their sum is $13$. Find the numbers.''',
r'''Let the larger number be $x$ and the smaller $y$. Then $x-y=3$ and $x+y=13$. Adding the equations gives $2x=16$, so $x=8$, and then $y=5$. The numbers are $\boxed{8\text{ and }5}$. (Equivalently $x+(x-3)=13$.)''',
'Systems of linear equations|Linear equations',1)

# ---------------- 1793187 square, angle FAE
fig=r'''pair A=(0,0),B=(7,0),C=(7,7),D=(0,7),Ep=(7,2.8),F=(3,7),G=(7,-3);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--Ep,linewidth(0.8));draw(A--F,linewidth(0.8));draw(Ep--F,linewidth(0.8));
draw(B--G,dashed);draw(A--G,dashed);
draw(arc(A,1.6,degrees(Ep-A),degrees(F-A)),linewidth(0.6));
label("$45^\circ$",A+2.45*dir((degrees(Ep-A)+degrees(F-A))/2));
label("$A$",A,SW);label("$B$",B,dir(-20));label("$C$",C,NE);label("$D$",D,NW);
label("$E$",Ep,E);label("$F$",F,N);label("$G$",G,SE);
label("$x$",(D+F)/2,N);label("$y$",(B+Ep)/2,E);label("$x$",(B+G)/2,E);'''
b.add(1793187,1,r'''In square $ABCD$, point $E$ lies on side $BC$ and point $F$ lies on side $CD$ such that $DF+BE=FE$. Find $\angle FAE$.''',
r'''Let $DF=x$ and $BE=y$, so $EF=x+y$. Rotate triangle $ADF$ about $A$ through $90^\circ$ so that $D$ goes to $B$; let $F$ go to $G$. Since $\angle ABG=\angle ADF=90^\circ$ and $\angle ABE=90^\circ$, the point $G$ lies on line $CB$ extended beyond $B$, with $BG=DF=x$ and $AG=AF$.
'''+asy(fig,'6cm')+r'''
Now $GE=GB+BE=x+y=FE$, $AG=AF$, and $AE$ is common, so triangles $AGE$ and $AFE$ are congruent (SSS). Hence $\angle GAE=\angle FAE$. But
\[
\angle GAE=\angle GAB+\angle BAE=\angle FAD+\angle BAE=90^\circ-\angle FAE ,
\]
because $\angle FAD+\angle FAE+\angle EAB=\angle DAB=90^\circ$. So $\angle FAE=90^\circ-\angle FAE$, and $\angle FAE=\boxed{45^\circ}$.''',
'Squares|Congruence|Rotations|Angle chasing',4,
note='The figure uses the true configuration BE = 2.8, DF = 3 on a square of side 7 (then EF = 5.8); the angle was checked numerically for several positions of E.')

# ---------------- 1793143 y^2=x^3+7
b.add(1793143,1,r'''Prove that the equation $y^2=x^3+7$ has no solutions in integers $x,y$.''',
r'''\textbf{$x$ is odd.} If $x$ is even, then $x^3\equiv0\pmod8$ and $y^2\equiv7\pmod8$. But squares are $\equiv0,1$ or $4\pmod8$. So $x$ is odd. Also $x^3=y^2-7\ge-7$, so $x\ge-1$.

\textbf{Factor.} Add $1$ to both sides:
\[
y^2+1=x^3+8=(x+2)(x^2-2x+4),\qquad x^2-2x+4=(x-1)^2+3 .
\]
Since $x$ is odd, $x-1$ is even, so $(x-1)^2\equiv0\pmod4$ and $x^2-2x+4\equiv3\pmod4$. This number is positive, and a positive integer that is $3\pmod4$ cannot be a product of primes that are all $1\pmod4$ (and it is odd), so it has a prime factor $p\equiv3\pmod4$. Then $p\mid y^2+1$.

\textbf{Contradiction.} From $y^2\equiv-1\pmod p$ we get $p\nmid y$, and since $\dfrac{p-1}{2}$ is odd,
\[
y^{p-1}=\left(y^2\right)^{\dfrac{p-1}{2}}\equiv(-1)^{\dfrac{p-1}{2}}=-1\pmod p .
\]
But Fermat's little theorem gives $y^{p-1}\equiv1\pmod p$, so $p\mid2$, impossible for an odd prime. Hence $\boxed{y^2=x^3+7\text{ has no integer solutions}}$. $\blacksquare$''',
'Diophantine equations|Remainders and congruences|Quadratic residues|Fermat\'s little theorem|Sum and difference of cubes|Parity',6,
note='"Solve in Z" made into a proof that there are no solutions (Lebesgue-type argument). Checked by search for |x| <= 10^5.')

# ---------------- 1793132 primes p(p+1)+q(q+1)=r(r+1) (alias)
b.add(1793132,1,r'''Find all primes $p,q,r$ such that $p(p+1)+q(q+1)=r(r+1)$.''',
r'''We have $p(p+1)=(r-q)(r+q+1)$ with $r>p$, $r>q$. If $p\mid r-q$, the right side exceeds $p(p+1)$; so $p\mid r+q+1$. Write $r+q+1=kp$, so $p+1=k(r-q)$; casework on $k$ (with $p\ge q$) leaves only $k=3$, $p=q=2$, $r=3$. The only solution is $\boxed{(p,q,r)=(2,2,3)}$.''',
'Prime numbers|Diophantine equations|Factoring|Divisibility',5,
note='Repeat of an earlier record (aliased).')

# ---------------- 1792786 centroid, collinear L M N
fig=r'''pair A=(1.2,5),B=(0,0),C=(6,0);
pair G=(A+B+C)/3,X=2G-A;
pair L=extension(X,X+(A-C),B,C);
pair M=extension(X,X+(B-A),C,A);
pair Nn=extension(X,X+(C-B),A,B);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--X,linewidth(0.6));
draw(X--L,blue);draw(X--M,blue);draw(X--Nn,blue);
draw(B--Nn,dashed+gray);
draw(M--Nn,red+dashed+linewidth(0.8));
dot(G);dot(X);dot(L,red);dot(M,red);dot(Nn,red);
label("$A$",A,N);label("$B$",B,NE);label("$C$",C,E);
label("$G$",G,W);label("$X$",X,SE);
label("$L$",L,NW);label("$M$",M,NE);label("$N$",Nn,SW);'''
b.add(1792786,1,r'''Let $G$ be the centroid of triangle $ABC$. Extend $AG$ beyond $G$ to $X$ so that $AG=GX$. The lines through $X$ parallel to $CA$, $AB$, $BC$ meet the lines $BC$, $CA$, $AB$ at $L$, $M$, $N$, respectively. Prove that $L$, $M$, $N$ are collinear.''',
r'''\textbf{Reduce to one triangle.} An affine map (a map $P\mapsto TP+v$ with $T$ an invertible linear map) sends lines to lines, parallel lines to parallel lines, and midpoints to midpoints, so it sends the centroid to the centroid and preserves ratios along a line. It therefore carries the whole configuration ($G$, $X$ with $AG=GX$, the three parallels, and $L,M,N$) for one triangle onto the configuration for its image, and it preserves collinearity. Since any triangle can be mapped to any other by an affine map, it is enough to prove the statement for
\[
A=(0,0),\quad B=(3,0),\quad C=(0,3).
\]

\textbf{Compute.} Then $G=(1,1)$ and $X=2G-A=(2,2)$.
\begin{itemize}
\item $CA$ is the line $x=0$, so the parallel through $X$ is $x=2$; it meets $BC$ ($x+y=3$) at $L=(2,1)$.
\item $AB$ is the line $y=0$, so the parallel through $X$ is $y=2$; it meets $CA$ ($x=0$) at $M=(0,2)$.
\item $BC$ has direction $(1,-1)$, so the parallel through $X$ is $x+y=4$; it meets $AB$ ($y=0$) at $N=(4,0)$.
\end{itemize}
All three points satisfy $x+2y=4$: $2+2=4$, $0+4=4$, $4+0=4$. Hence $L$, $M$, $N$ are collinear. $\blacksquare$

The figure shows a general triangle: $L$ lies on side $BC$, $M$ on side $CA$, and $N$ on line $AB$ extended beyond $B$.
'''+asy(fig,'7cm'),
'Medians and centroids|Parallel lines|Coordinate geometry|Geometric transformations|Triangles',5,
note='The post says "AG is produced to X"; read as extending AG beyond G. Proof by an affine reduction to a right isosceles triangle; collinearity also checked numerically for random triangles.')

# ---------------- 1792646 last digit 3^1118
b.add(1792646,1,r'''What is the last digit of $3^{1118}$?''',
r'''The last digits of $3^1,3^2,3^3,3^4,3^5,\dots$ are $3,9,7,1,3,\dots$: each last digit is determined by the previous one (multiply by $3$ and keep the units digit), so the pattern repeats with period $4$. Since $1118=4\cdot279+2$, the last digit of $3^{1118}$ is the same as that of $3^2$, namely $\boxed{9}$.''',
'Units digits and last digits|Remainders and congruences|Pattern recognition',2)

# ---------------- 1780334 two primes sum 69
b.add(1780334,1,r'''The sum of two prime numbers is $69$. What is the difference of these two numbers?''',
r'''The sum $69$ is odd. If both primes were odd, their sum would be even, so one of them is the only even prime, $2$. The other is $69-2=67$, which is prime. The difference is $67-2=\boxed{65}$.''',
'Prime numbers|Parity',2)

# ---------------- 1792647 zeros in 123...2019
b.add(1792647,1,r'''The integers from $1$ to $2019$ are written one after another to form the long number $123456789101112\cdots20182019$. How many digits $0$ does it contain?''',
r'''Count the zeros by blocks.
\begin{itemize}
\item $1$--$9$: none.
\item $10$--$99$: only the units digit can be $0$: $10,20,\dots,90$, so $9$ zeros.
\item $100$--$999$: in each hundred $h00$--$h99$ the tens digit is $0$ for $10$ numbers and the units digit is $0$ for $10$ numbers, so $20$ zeros per hundred and $9\cdot20=180$ zeros.
\item $1000$--$1999$: the last three digits run through all strings $000$--$999$, in which each of the three positions is $0$ exactly $100$ times: $300$ zeros.
\item $2000$--$2019$: $2000$ has $3$ zeros, $2001$--$2009$ have $2$ each ($18$), $2010$ has $2$, and $2011$--$2019$ have $1$ each ($9$): $32$ zeros.
\end{itemize}
Total: $9+180+300+32=\boxed{521}$.''',
'Digit problems|Systematic counting|Place value',3,
note='Part 1 of the post. Parts 2 and 3 ("1234...N" and "from N to M") ask for general formulas with no specific numbers and are dropped. Count checked by direct computation.')

# ---------------- 1792730 cyclic quadrilaterals
fig=r'''pair A=dir(140),D=dir(62),B=dir(212),C=dir(328);
pair Ep=B+0.24*(C-B);
pair cc(pair P,pair Q,pair R){pair a=Q-P,c=R-P; real d=2*(a.x*c.y-a.y*c.x);
  return P+((c.y*dot(a,a)-a.y*dot(c,c))/d,(a.x*dot(c,c)-c.x*dot(a,a))/d);}
pair O2=cc(A,D,Ep); real r2=abs(A-O2);
pair u=unit(C-B); real t=-2*dot(Ep-O2,u); pair F=Ep+t*u;
draw(unitcircle,gray+linewidth(0.6));
draw(circle(O2,r2),dashed+blue);
draw(A--B--C--D--cycle,linewidth(0.9));
draw(A--Ep,linewidth(0.6));draw(A--F,linewidth(0.6));draw(D--Ep,linewidth(0.6));draw(D--F,linewidth(0.6));
draw(A--C,red+linewidth(0.6));draw(D--B,red+linewidth(0.6));
dot(Ep);dot(F);
label("$A$",A,NW);label("$B$",B,SW);label("$C$",C,SE);label("$D$",D,NE);
label("$E$",Ep,SW);label("$F$",F,SE);'''
b.add(1792730,1,r'''$ABCD$ is a convex quadrilateral, and $E$ and $F$ are points on side $BC$ with $E$ closer to $B$ than $F$. Suppose $\angle FDC=\angle EAB$ and $\angle EAF=\angle EDF$. Prove that $\angle CAF=\angle BDE$.''',
r'''\textbf{Step 1: $A,E,F,D$ are concyclic.} The points $A$ and $D$ lie on the same side of line $BC$ (the quadrilateral is convex), and they see the segment $EF$ under the equal angles $\angle EAF=\angle EDF$. Hence $A$, $D$, $E$, $F$ lie on a circle, in the cyclic order $A,D,F,E$.

\textbf{Step 2: $ABCD$ is cyclic.} Let $\alpha=\angle EAB=\angle FDC$. In the cyclic quadrilateral $AEFD$ an exterior angle equals the opposite interior angle, so $\angle AEB=\angle ADF$ and $\angle DFC=\angle DAE$. In triangle $ABE$,
\[
\angle ABC=\angle ABE=180^\circ-\alpha-\angle AEB=180^\circ-\alpha-\angle ADF ,
\]
while $\angle ADC=\angle ADF+\angle FDC=\angle ADF+\alpha$. So $\angle ABC+\angle ADC=180^\circ$, and $ABCD$ is cyclic.
'''+asy(fig,'7cm')+r'''
\textbf{Step 3: the angles.} Seen from $A$, the rays $AB,AE,AF,AC,AD$ come in this order, so $\angle CAF=\angle FAD-\angle CAD$. In circle $AEFD$, the angles $\angle FAD$ and $\angle FED$ stand on the chord $FD$ from the same side, so $\angle FAD=\angle FED$. Since $F$ lies on ray $EC$, $\angle FED$ is the exterior angle at $E$ of triangle $BED$, hence $\angle FED=\angle EBD+\angle BDE=\angle CBD+\angle BDE$. In circle $ABCD$, $\angle CAD=\angle CBD$. Therefore
\[
\angle CAF=\angle FAD-\angle CAD=\bigl(\angle CBD+\angle BDE\bigr)-\angle CBD=\angle BDE . \qquad\blacksquare
\]''',
'Cyclic quadrilaterals|Inscribed angles|Angle chasing|Circles',5,
note='Problem P2 of a locked Euclidean geometry marathon, reposted. Proof written by the authors; the figure is built from a cyclic ABCD and the circle through A, D, E, and the angle equalities were checked numerically.')

# ---------------- 1792720 twin primes mod 9
b.add(1792720,1,r'''Show that if $p>3$ and $q=p+2$ are both prime (twin primes), then $pq\equiv-1\pmod9$.''',
r'''Since $p>3$ is prime, $p$ is odd and not divisible by $3$. If $p\equiv1\pmod3$, then $q=p+2\equiv0\pmod3$ and $q>3$, so $q$ would not be prime. Hence $p\equiv2\pmod3$, and with $p$ odd, $p\equiv5\pmod6$. Write $p=6k-1$; then $q=6k+1$ and
\[
pq=(6k-1)(6k+1)=36k^2-1\equiv-1\pmod9 ,
\]
since $9\mid36k^2$. (In fact $pq\equiv-1\pmod{36}$.) $\blacksquare$''',
'Prime numbers|Remainders and congruences|Difference of squares',2)

# ---------------- 1792707 rotation
fig=r'''pair A=(0,0),B=5*dir(0),C=3.2*dir(35),Bp=5*dir(70),Cp=3.2*dir(105);
pair M=(B+Bp)/2,K=(C+Cp)/2;
draw(A--B--C--cycle,linewidth(0.9));
draw(A--Bp--Cp--cycle,linewidth(0.9)+deepgreen);
draw(B--Bp,dashed);draw(C--Cp,dashed);
draw(C--M,red+linewidth(0.7));
dot(M);dot(K);
label("$A$",A,SW);label("$B$",B,SE);label("$C$",C,S);
label("$B'$",Bp,NE);label("$C'$",Cp,NW);label("$M$",M,NE);label("$K$",K,2*dir(205));'''
b.add(1792707,1,r'''A triangle $ABC$ is rotated in its own plane about the vertex $A$ to a position $AB'C'$. If line $AC$ bisects segment $BB'$, prove that line $AB'$ bisects segment $CC'$.''',
r'''Let the rotation be through the angle $\theta$ with $0<\theta<360^\circ$ (for $\theta=0$ there is nothing to prove). If $\theta=180^\circ$, then $A$ is the midpoint of both $BB'$ and $CC'$, and every line through $A$ bisects both; so assume $\theta\ne180^\circ$.

Since $AB=AB'$, triangle $ABB'$ is isosceles, and the line through $A$ and the midpoint $M$ of $BB'$ is the bisector of angle $BAB'$: it is the line through $A$ in the direction of $AB$ turned through $\dfrac{\theta}{2}$. As line $AC$ passes through $A$ and $M$, the direction of $AC$ is that of $AB$ turned through $\dfrac\theta2$ (as lines, i.e.\ up to $180^\circ$).

Likewise $AC=AC'$, so the line through $A$ and the midpoint $K$ of $CC'$ is the line through $A$ in the direction of $AC$ turned through $\dfrac\theta2$. Turning $AB$ first through $\dfrac\theta2$ and then through another $\dfrac\theta2$ turns it through $\theta$, which gives the direction of $AB'$. Hence line $AK$ is line $AB'$, i.e.\ $AB'$ passes through the midpoint of $CC'$. $\blacksquare$
'''+asy(fig,'6cm')+r'''
In the figure $\theta=70^\circ$: line $AC$ (extended in red) makes $35^\circ$ with $AB$ and passes through the midpoint $M$ of $BB'$, and $AB'$ makes $35^\circ$ with $AC$ and passes through the midpoint $K$ of $CC'$.''',
'Rotations|Isosceles triangles|Angle bisectors|Midpoints',3,
note='Problem P1 of a Euclidean geometry marathon thread (only P1 is in the post).')

# ---------------- 1792695 Ted and Sally
b.add(1792695,1,r'''Ted and Sally play a game on a square $ABCD$. At the same moment, each of them draws a segment across the square that is perpendicular to one pair of opposite sides and joins those two sides. Each player independently chooses the direction (parallel to $AB$ or parallel to $BC$) with probability $\dfrac12$ each, and the position of the segment uniformly at random. If the two segments intersect, Ted wins; otherwise Sally wins. What is the probability that Ted wins?''',
r'''If the two segments have different directions, one runs all the way across the square from left to right and the other from top to bottom, so they cross. If they have the same direction, they are parallel and (with probability $1$) at different positions, so they do not meet. Hence Ted wins exactly when the directions differ, which happens with probability
\[
\dfrac12\cdot\dfrac12+\dfrac12\cdot\dfrac12=\boxed{\dfrac12}.
\]''',
'Probability|Independent events',1,
note='The random model is made explicit (direction 1/2 each, uniform position); "without laying one line over the other" is the probability-0 event of coinciding segments. The bonus question (both lines from the same side, not necessarily perpendicular) gives no distribution for the lines and is dropped.')

# ---------------- 1771789 twins (alias)
b.add(1771789,1,r'''Three pairs of identical twins randomly seat themselves at a round table containing six seats. What is the probability that no person is seated directly across from his or her identical twin? Express your answer as a common fraction.''',
r'''Let $E_i$ be the event that pair $i$ sits opposite. $P(E_i)=\dfrac15$, $P(E_iE_j)=\dfrac15\cdot\dfrac13=\dfrac1{15}$, and $P(E_1E_2E_3)=\dfrac1{15}$ (two opposite pairs force the third). By inclusion-exclusion the probability is $1-\left(\dfrac35-\dfrac3{15}+\dfrac1{15}\right)=\boxed{\dfrac{8}{15}}$.''',
'Probability|Sets and inclusion–exclusion|Circular arrangements',4,
note='Mock MATHCOUNTS State Sprint #18; repeat of an earlier record (aliased).')

# ---------------- 1792514 0=3
b.add(1792514,1,r'''A student argues as follows. ``Let $x$ satisfy $x^2+x+1=0$. Multiplying by $x$ gives $x^3+x^2+x=0$. From the first equation $x^2+x=-1$, so $x^3-1=0$ and $x=1$. Substituting into the first equation, $1+1+1=0$, i.e.\ $3=0$.'' Find the error, and find all complex solutions of $x^2+x+1=0$.''',
r'''Every step from $x^2+x+1=0$ to $x^3-1=0$ is a correct \emph{consequence}: indeed $x^3-1=(x-1)(x^2+x+1)$, so any root of $x^2+x+1$ is a root of $x^3-1$. But the implication does not reverse. The equation $x^3=1$ has three roots, $x=1$ and the two non-real cube roots of unity, and the step ``$x^3-1=0$, so $x=1$'' silently picks the one root that does \emph{not} satisfy the original equation: $x=1$ comes from the factor $x-1$, which was in effect introduced by the manipulation. (Over the real numbers the original equation has no solution at all, since its discriminant is $1-4<0$, so there is no real $x$ to begin with.)

The solutions of $x^2+x+1=0$ are, by the quadratic formula,
\[
x=\boxed{\dfrac{-1\pm i\sqrt3}{2}},
\]
the two cube roots of unity other than $1$. They do satisfy $x^3=1$, and they are exactly the roots of $x^3-1=0$ with $x\ne1$.''',
'Quadratic equations|Complex numbers|Roots of unity|Factoring',3,
note='The post shows the 0 = 3 "paradox" and asks where the extra root comes from; the record asks for the error and the true solutions.')

b.save()
