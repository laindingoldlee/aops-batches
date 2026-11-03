from qb import *
b=Bank('p229_03')

# ---------------- 1742467 convex sequences
b.add(1742467,1,r'''A convex sequence is a sequence of integers in which each term other than the first and the last is no greater than the arithmetic mean of the terms immediately before and after it. For example, $4,1,2,3$ is convex because $1\le\dfrac{4+2}{2}$ and $2\le\dfrac{1+3}{2}$. How many convex sequences use each number of the set $\{1,2,3,4,5,6,7,8\}$ exactly once?''',
r'''The condition $p_i\le\dfrac{p_{i-1}+p_{i+1}}{2}$ says $p_i-p_{i-1}\le p_{i+1}-p_i$: the successive differences never decrease. As the terms are distinct, no difference is $0$, so the sequence decreases down to its smallest term $1$ and then increases. Reading outward from $1$ on either side, the terms increase and the gaps between neighbours never decrease. The two sides are otherwise independent (at $1$ the condition holds automatically, a negative difference being followed by a positive one).

The number $2$ is next to $1$ (it is the nearest term on its side). By reversing the sequence we may assume $2$ is to the right of $1$, and we double at the end. Let the right side start $1,2,\dots,k$ with gaps $1$ and let $k$ be maximal ($2\le k\le8$).
\begin{itemize}
\item $k=8$: the sequence $1,2,\dots,8$.
\item $k=7$: then $8$ is on the left: $8,1,2,\dots,7$.
\item $k\le6$: then $k+1$ is the first term on the left, with gap $k$ from $1$, so every later left gap is at least $k$; and every further right gap is at least $2$.
 \begin{itemize}
 \item If $k\ge3$: the number $k+2\le8$ cannot be on the left (the next left term is at least $2k+1>k+2$), so it is on the right with gap $2$. If $k\le5$, then $k+3\le8$ fits neither on the right (gap $1<2$) nor on the left (it is less than $2k+1$). So $k=6$, giving $7,1,2,3,4,5,6,8$.
 \item If $k=2$: the left side starts $1,3$ with gaps at least $2$, the right side $1,2$ continues with gaps at least $2$. Then $4$ must go right, so $5$ must go left, so $6$ goes right, $7$ left, $8$ right, every gap being $2$: the sequence $7,5,3,1,2,4,6,8$.
 \end{itemize}
\end{itemize}
That is $4$ sequences with $2$ to the right of $1$, and $4$ mirror images, $\boxed{8}$ in all.''',
'Arrangements with restrictions|Casework|Inequalities',5,source=src('MATHCOUNTS',2015,'State',8,rnd='Team'),
note='Answer 8 confirmed by brute force over all 8! permutations.')

# ---------------- 1742450 hexagon in circle
fig=r'''pair O=(0,0);pair[] V;for(int i=0;i<6;++i)V[i]=4*dir(60*i);
draw(circle(O,4),linewidth(0.8));draw(V[0]--V[1]--V[2]--V[3]--V[4]--V[5]--cycle,linewidth(0.9));
draw(O--V[0],dashed);draw(O--V[1],dashed);
dot(O);label("$O$",O,SW);
label("$4$",(V[0]+V[1])/2+0.55*dir(210));label("$4$",(O+V[0])/2,S);label("$4$",(O+V[1])/2,dir(150));'''
b.add(1742450,1,r'''A regular hexagon with side length $4$ cm is inscribed in a circle. Find the radius of the circle.''',
r'''Join the centre $O$ to two adjacent vertices. The central angle is $\dfrac{360^\circ}{6}=60^\circ$, and the two radii are equal, so the triangle is isosceles with apex angle $60^\circ$, hence equilateral.
'''+asy(fig,'4.5cm')+r'''
So the radius equals the side: $\boxed{4\text{ cm}}$.''',
'Regular polygons|Circles|Equilateral triangles',1)

# ---------------- 1742456 towers, bridge and rope
fig=r'''pair A=(0,0),B=(100,0),P=(0,90),Q=(100,150),X=(200/9,70);
draw((-22,0)--(115,0),linewidth(0.6));
draw(A--P,linewidth(2));draw(B--Q,linewidth(2));
draw((0,70)--(100,70),brown+linewidth(1.2));
draw(P--B,blue);
dot(X);dot(P);
label("$P$",P,W);label("$A$",A,S);label("$B$",B,S);label("$Q$",Q,E);label("$X$",X,dir(60));
draw((-16,0)--(-16,90),Arrows(4));label("$90$",(-16,45),W);label("$150$",(100,75),E);label("$100$",(50,0),S);label("bridge",(70,70),N,brown);
label("$20$",(0,80),W);label("$70$",(0,35),W);'''
b.add(1742456,1,r'''Two towers of heights $90$ m and $150$ m stand $100$ m apart on level ground. A straight horizontal bridge connects the towers at a height of $70$ m. A rope is stretched from the top of the shorter tower to the foot of the taller tower. Find the distance from the top of the shorter tower to the point where the rope crosses the bridge.''',
r'''Use coordinates with the shorter tower $AP$ on the $y$-axis ($A=(0,0)$, $P=(0,90)$) and the foot of the taller tower at $B=(100,0)$. The bridge is the segment $y=70$, $0\le x\le100$.
'''+asy(fig,'6cm')+r'''
The rope $PB$ is $y=90-\dfrac{9}{10}x$. It reaches height $70$ when $\dfrac9{10}x=20$, i.e.\ at $X=\left(\dfrac{200}{9},70\right)$. (By similar triangles: the rope drops $20$ of its total $90$, so $X$ is $\dfrac{20}{90}$ of the way from $P$ to $B$.) Hence
\[
PX=\dfrac29\,PB=\dfrac29\sqrt{100^2+90^2}=\dfrac29\cdot10\sqrt{181}=\boxed{\dfrac{20\sqrt{181}}{9}}\approx29.9\text{ m}.
\]
The height of the taller tower is not needed.''',
'Similarity|Pythagorean theorem|Coordinate geometry',3,
note='"70 m from the foot of both towers a bridge constructed" is read as a horizontal bridge at height 70 m.')

# ---------------- 1742459 born in year x^2 - x
b.add(1742459,1,r'''A man born in the first half of the nineteenth century (1801-1850) was $x$ years old in the year $x^2$. In which year was he born?''',
r'''He was born in the year $x^2-x$. We need $1801\le x^2-x\le1850$ (and he must be alive in year $x^2$). Now $42^2-42=1722$, $43^2-43=1806$ and $44^2-44=1892$, and $x^2-x$ increases with $x$, so $x=43$: he was born in $\boxed{1806}$ and was $43$ in $1849=43^2$.''',
'Perfect squares|Age problems',2)

# ---------------- 1742264 quadratic roots
b.add(1742264,1,r'''Let $y=-7x^2+3x+1$. In the quadratic formula $x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$, call $x_+$ the value with the $+$ sign and $x_-$ the value with the $-$ sign.
\begin{enumerate}
\item[(a)] Find $x_+$ and $x_-$ for the equation $-7x^2+3x+1=0$, to the nearest hundredth.
\item[(b)] Find $x_+$ for the points of the graph whose $y$-coordinate is $-7$, to the nearest hundredth.
\end{enumerate}
A student answered $x_+\approx0.65$, $x_-\approx-0.22$ and, for (b), $1.3$; explain the error.''',
r'''\textbf{(a)} Here $a=-7$, $b=3$, $c=1$, $b^2-4ac=9+28=37$, and $2a=-14$:
\[
x_+=\dfrac{-3+\sqrt{37}}{-14}=\dfrac{3-\sqrt{37}}{14}\approx\boxed{-0.22},\qquad x_-=\dfrac{-3-\sqrt{37}}{-14}=\dfrac{3+\sqrt{37}}{14}\approx\boxed{0.65}.
\]
\textbf{(b)} $-7x^2+3x+1=-7$ means $-7x^2+3x+8=0$, so $b^2-4ac=9+224=233$ and
\[
x_+=\dfrac{-3+\sqrt{233}}{-14}=\dfrac{3-\sqrt{233}}{14}\approx\boxed{-0.88}
\]
(the other root is $x_-\approx1.30$).

The student's numbers are the correct roots but with the labels swapped: because $a$ is negative, the denominator $2a=-14$ is negative, so the $+$ sign gives the \emph{smaller} root.''',
'Quadratic equations',2,
note='The poster suspects the answer key is wrong; it is not: the poster swapped x+ and x- (with a = -7 the + sign gives the smaller root).')

# ---------------- 1741984 square from a diagonal
fig=r'''pair A=(1,3),C=(5,1),B=(4,4),D=(2,0),M=(3,2);
draw((-0.5,0)--(6,0),gray,Arrow(5));draw((0,-0.5)--(0,5),gray,Arrow(5));
draw(A--B--C--D--cycle,linewidth(0.9));draw(A--C,dashed);draw(B--D,dashed);
dot(A);dot(B);dot(C);dot(D);dot(M);
label("$A(1,3)$",A,W);label("$B(4,4)$",B,N);label("$C(5,1)$",C,E);label("$D(2,0)$",D,dir(-60));label("$M$",M,dir(15));'''
b.add(1741984,1,r'''$ABCD$ is a square with $A=(1,3)$ and $C=(5,1)$. Find the coordinates of $B$ and $D$.''',
r'''$A$ and $C$ are opposite vertices, so the diagonals meet at the midpoint $M=(3,2)$ of $AC$. The other diagonal $BD$ has the same length, is perpendicular to $AC$, and is bisected by $M$. Since $\overrightarrow{MC}=(2,-1)$, rotating it by $90^\circ$ gives $(1,2)$, so $B$ and $D$ are $M\pm(1,2)$:
\[
\boxed{(4,4)\text{ and }(2,0)}.
\]
'''+asy(fig,'4.5cm')+r'''
Going around $A,B,C,D$ in order, either $B=(4,4)$, $D=(2,0)$ or the reverse. (Check: all four sides have length $\sqrt{10}$ and $\overrightarrow{AB}\cdot\overrightarrow{BC}=(3,1)\cdot(1,-3)=0$.)''',
'Squares|Coordinate geometry|Rotations',2,
note='The post gives only "ab = bc = cd" with a(1,3), c(5,1); equal sides alone do not determine B and D, so ABCD is taken to be a square (the evident intent).')

# ---------------- 1742279 400th post
b.add(1742279,1,r'''In the Martian currency system, $5$ glops are worth $6$ blops, and $10$ blops are worth $20$ slops. Rachel has $400$ glops. She buys a cow costing $400$ slops and pays with all of her money. How much change does she receive, in blops? Also express it in glops.''',
r'''$400$ glops $=400\cdot\dfrac65=480$ blops, and $1$ blop $=2$ slops, so the cow costs $200$ blops. The change is $480-200=\boxed{280\text{ blops}}$, which is $280\cdot\dfrac56=233\dfrac13$ glops.''',
'Unit conversion|Ratios, proportions, and variation',2,
note='The post asks for the answer "with glops and blops"; since the change is not a whole number of glops, the record asks for it in blops and in glops.')
b.add(1742279,2,r'''How many perfect squares lie strictly between $400^2$ and $2^{400}$?''',
r'''$2^{400}=(2^{200})^2$. The squares strictly between $400^2$ and $(2^{200})^2$ are $n^2$ for $401\le n\le2^{200}-1$, so there are $2^{200}-1-400=\boxed{2^{200}-401}$ of them.''',
'Perfect squares|Exponents',2,
note='"Between" read as strictly between.')
b.add(1742279,3,r'''Exploding $200$ lb of TNT produces an explosion of $400$ kabloowies, and the strength of an explosion is proportional to the amount of TNT. A sheet of paper can withstand $0.5$ kabloowies, a sheet of metal is $400$ times as strong as a sheet of paper, and a wall is equivalent to $400$ sheets of metal. How much TNT is needed to produce an explosion as strong as the wall can withstand?''',
r'''The wall withstands $400\cdot400\cdot0.5=80000$ kabloowies. Each pound of TNT gives $2$ kabloowies, so $\dfrac{80000}{2}=\boxed{40000\text{ lb}}$ of TNT are needed.''',
'Ratios, proportions, and variation',1,
note='Proportionality of explosion strength to the amount of TNT is stated explicitly; the post leaves it implicit.')

# ---------------- 1669230 200 divisors
b.add(1669230,1,r'''Find the sum of the digits of the smallest positive integer that has exactly $200$ positive divisors.''',
r'''If $n=p_1^{e_1}p_2^{e_2}\cdots$, then $n$ has $(e_1+1)(e_2+1)\cdots$ divisors. For the smallest $n$ with a given list of exponents, the largest exponents go on the smallest primes. So we must write $200=2^3\cdot5^2$ as a product of factors $f_1\ge f_2\ge\dots\ge2$ and minimise $2^{f_1-1}3^{f_2-1}5^{f_3-1}\cdots$. Since $200$ has five prime factors, at most five factors appear. The main candidates are
\[
\begin{array}{ll}
5\cdot5\cdot2\cdot2\cdot2: & 2^4\cdot3^4\cdot5\cdot7\cdot11=498960\\
5\cdot5\cdot4\cdot2: & 2^4\cdot3^4\cdot5^3\cdot7=1134000\\
10\cdot5\cdot2\cdot2: & 2^9\cdot3^4\cdot5\cdot7=1451520\\
10\cdot5\cdot4: & 2^9\cdot3^4\cdot5^3=5184000\\
8\cdot5\cdot5: & 2^7\cdot3^4\cdot5^4=6480000
\end{array}
\]
and every other factorisation ($10\cdot10\cdot2$, $20\cdot5\cdot2$, $25\cdot2\cdot2\cdot2$, $\dots$, $200$) gives a number larger than $5\times10^7$. (Merging two factors $f,g$ into $fg$ always replaces $p^{g-1}$ by a factor at least $2^{f(g-1)}$, which here is much larger.) So the smallest number is $498960=2^4\cdot3^4\cdot5\cdot7\cdot11$, and its digit sum is $4+9+8+9+6+0=\boxed{36}$.''',
'Divisor counting|Prime factorisation|Digit problems',5,
note='All 16 factorisations of 200 were checked by computer; 498960 is the least.')

# ---------------- 1741935 a_n = 2a_{n-1}+2^n
b.add(1741935,1,r'''Let $a_0,a_1,a_2,\dots$ be the sequence with $a_0=0$ and $a_n=2a_{n-1}+2^n$ for $n\ge1$. Find $a_{100}$ exactly.''',
r'''Divide by $2^n$: with $b_n=\dfrac{a_n}{2^n}$ the recurrence becomes $b_n=b_{n-1}+1$, and $b_0=0$, so $b_n=n$. Hence $a_n=n\cdot2^n$ and
\[
a_{100}=\boxed{100\cdot2^{100}}=25\cdot2^{102}\approx1.27\times10^{32}.
\]''',
'Recurrence relations|Exponents',3,
note='The poll choices of the post are not given; the record asks for the exact value.')

# ---------------- 1740608 Math Arcade
b.add(1740608,1,r'''What is the sum of the first $100$ positive integers?''',
r'''Pair $1$ with $100$, $2$ with $99$, and so on: $50$ pairs each summing to $101$, so the sum is $50\cdot101=\boxed{5050}$.''',
'Arithmetic sequences|Summation|Pairing and grouping',1)
b.add(1740608,2,r'''In an archery game each dart scores one of $0,25,50,75,100,125$. How many different total scores are possible with $3$ darts?''',
r'''Every score is $25$ times one of $0,1,\dots,5$, so a total is $25s$ with $s$ a sum of three numbers from $\{0,\dots,5\}$. Such sums take every value from $0$ to $15$ (for instance $s=3q+r$ with $0\le r<3$ is achieved by $r$ darts of $q+1$ and $3-r$ darts of $q$, and $s=15$ by three $5$'s). So there are $\boxed{16}$ possible totals, $0,25,\dots,375$.''',
'Systematic counting|Addition principle',2,
note='"How many results are possible" is read as the number of distinct total scores (the number of unordered score combinations would be 56).')
b.add(1740608,3,r'''What is the least multiple of $41$ whose digits are all $1$ (such as $111$)?''',
r'''The number with $k$ ones is $R_k=\dfrac{10^k-1}{9}$, and $41\mid R_k$ exactly when $41\mid10^k-1$ (as $\gcd(41,9)=1$). Modulo $41$: $10^2\equiv18$, $10^3\equiv180\equiv16$, $10^4\equiv160\equiv37$, $10^5\equiv370\equiv1$. So the least $k$ is $5$ (the order of $10$ is $5$), and the answer is $\boxed{11111}=41\cdot271$.''',
'Multiplicative order|Remainders and congruences|Digit problems',3)

# ---------------- 1741490 circles in a rectangle
qfig=r'''real r=1,w=3+2*sqrt(2),h=4;
draw((0,0)--(w,0)--(w,h)--(0,h)--cycle,linewidth(0.9));
draw(circle((1,1),1));draw(circle((1,3),1));draw(circle((w-2,2),2));
draw((0,-0.45)--(w,-0.45),Arrows(4));label("$w$",(w/2,-0.45),S);
draw((w+0.45,0)--(w+0.45,h),Arrows(4));label("$h$",(w+0.45,h/2),E);'''
sfig=r'''real w=3+2*sqrt(2),h=4;pair P1=(1,1),P2=(1,3),Q=(w-2,2);
draw((0,0)--(w,0)--(w,h)--(0,h)--cycle,linewidth(0.9));
draw(circle(P1,1));draw(circle(P2,1));draw(circle(Q,2));
draw(P1--Q,blue);draw(P1--(Q.x,P1.y),dashed);draw(Q--(Q.x,P1.y),dashed);
draw(Q--(Q.x,4),dotted);draw(P1--(0,1),dotted);
dot(P1);dot(P2);dot(Q);
label("$r$",(0.5,1),N);label("$2r$",(Q.x,3),E);
label("$3r$",(P1+Q)/2,dir(110),blue);label("$r$",(Q.x,1.5),E);label("$d$",((1+Q.x)/2,1),S);'''
b.add(1741490,1,r'''Three circles are inscribed in a rectangle of width $w$ and height $h$, as shown. Two of the circles are congruent; one is tangent to the left and top sides, the other to the left and bottom sides, and they are tangent to each other. The third circle is larger and is tangent to the top, bottom and right sides of the rectangle and to both smaller circles. What is the ratio of $h$ to $w$? Express your answer as a decimal to the nearest hundredth.
'''+asy(qfig,'5cm'),
r'''Let the small radius be $r$. The two small circles are stacked along the left side, so $h=4r$, and the large circle touches the top and bottom, so its radius is $2r$. Put the lower small centre at $(r,r)$ and the large centre at $(x,2r)$.
'''+asy(sfig,'5.5cm')+r'''
Tangency of the circles gives a centre distance of $r+2r=3r$, with vertical difference $r$, so the horizontal difference is $d=\sqrt{9r^2-r^2}=2\sqrt2\,r$. Hence $w=r+2\sqrt2\,r+2r=(3+2\sqrt2)r$ and
\[
\dfrac hw=\dfrac{4}{3+2\sqrt2}=4(3-2\sqrt2)=12-8\sqrt2\approx\boxed{0.69}.
\]''',
'Tangent circles|Rectangles|Pythagorean theorem',4,
note='The figure is missing; the text alone allows the small circles to be stacked along a short or a long side. The configuration matching the poster\'s answer 0.69 (small circles along the left side, h < w) is stated and drawn; the other placement would give 1/0.69, about 1.46.')

# ---------------- 1741457 joker
b.add(1741457,1,r'''In a card game, Noah draws cards at random, without replacement, from a deck of $21$ cards: $20$ cards numbered $1$ through $20$ and a joker. Noah keeps all of the cards he draws before he draws the joker. What is the probability that the cards Noah keeps include exactly $4$ prime-numbered cards? Express your answer as a common fraction.''',
r'''The primes up to $20$ are $2,3,5,7,11,13,17,19$: eight cards. Only the relative order of these eight cards and the joker matters, and all $9!$ relative orders are equally likely. The number of prime cards kept is the number of them that precede the joker, and the joker's position among the nine cards is uniform on $1,\dots,9$. So the number of primes kept is equally likely to be any of $0,1,\dots,8$, and the probability that it is $4$ is $\boxed{\dfrac19}$.''',
'Probability|Symmetry',4)

# ---------------- 1741722 Connex
b.add(1741722,1,r'''Connex contains one $4$-unit piece, two $3$-unit pieces, three $2$-unit pieces and four $1$-unit pieces; pieces of the same length are identical. How many different $10$-unit lengths can be formed by placing pieces end to end, if the order of the pieces matters?''',
r'''Choose how many pieces of each length are used, $(n_4,n_3,n_2,n_1)$ with $n_4\le1$, $n_3\le2$, $n_2\le3$, $n_1\le4$ and $4n_4+3n_3+2n_2+n_1=10$; then arrange them in $\dfrac{(n_4+n_3+n_2+n_1)!}{n_4!\,n_3!\,n_2!\,n_1!}$ orders.
\[
\begin{array}{cccc|c}
n_4&n_3&n_2&n_1&\text{orders}\\\hline
0&0&3&4&35\\
0&1&2&3&60\\
0&1&3&1&20\\
0&2&0&4&15\\
0&2&1&2&30\\
0&2&2&0&6\\
1&0&1&4&30\\
1&0&2&2&30\\
1&0&3&0&4\\
1&1&0&3&20\\
1&1&1&1&24\\
1&2&0&0&3
\end{array}
\]
(For $n_4=0$: $3n_3+2n_2+n_1=10$ with $n_1\le4$ forces $3n_3+2n_2\ge6$; for $n_4=1$: $3n_3+2n_2+n_1=6$. These are all the cases.) The total is
\[
35+60+20+15+30+6+30+30+4+20+24+3=\boxed{277}.
\]''',
'Multiset permutations|Partitions and compositions|Casework',5,source=src('MATHCOUNTS',2013,'State',28,rnd='Sprint'),
note='The poster asks for a faster method than the official one; the count by piece multiset is given.')

# ---------------- 1741715 MATHCOUNTS 2017 National Team 3
b.add(1741715,1,r'''Madison writes a one-digit positive integer, a two-digit positive integer and a three-digit positive integer using the digits $1$ through $6$, each exactly once. The product of the three integers is $20400$. What is the sum of the three integers?''',
r'''$20400=2^4\cdot3\cdot5^2\cdot17$. The digit $5$ is used once, so at most one of the numbers is divisible by $5$ (a number divisible by $5$ with no digit $0$ ends in $5$). Hence one number is divisible by $25$; with no $0$, $7$ available, it ends in $25$.
\begin{itemize}
\item If it is the two-digit $25$: the other two multiply to $816=2^4\cdot3\cdot17$, using digits $1,3,4,6$. The one-digit number is $1,3,4$ or $6$, leaving $816,272,204,136$ for the three-digit number, none of which uses the remaining digits.
\item If it is a three-digit $\underline{a}25$ with $a\in\{1,3,4,6\}$: $125$ and $625$ are powers of $5$ (too many factors of $5$) and $325=25\cdot13$ does not divide $20400$, so it is $425=25\cdot17$. The others multiply to $48$ using digits $1,3,6$: $3\cdot16=48$ works ($1\cdot36$ and $6\cdot13$ do not).
\end{itemize}
So the numbers are $3,16,425$, and their sum is $\boxed{444}$.''',
'Prime factorisation|Digit problems|Casework',4,source=src('MATHCOUNTS',2017,'National',3,rnd='Team'))

# ---------------- 1741603 third side
fig1=r'''pair O=(0,0);pair A=5*dir(90),B=5*dir(150),C=5*dir(90-2*aSin(0.6));
draw(circle(O,5),gray);draw(A--B--C--cycle,linewidth(0.9));
dot(O);label("$O$",O,S);
label("$A$",A,N);label("$B$",B,W);label("$C$",C,E);
label("$5$",(A+B)/2,dir(120));label("$6$",(A+C)/2,dir(50));'''
fig2=r'''pair O=(0,0);pair A=5*dir(90),B=5*dir(150),C=5*dir(90+2*aSin(0.6));
draw(circle(O,5),gray);draw(A--B--C--cycle,linewidth(0.9));
dot(O);label("$O$",O,S);
label("$A$",A,N);label("$B$",B,NW);label("$C$",C,W);
label("$5$",(A+B)/2,dir(120));label("$6$",(A+C)/2,dir(-30));'''
b.add(1741603,1,r'''A triangle inscribed in a circle of radius $5$ has two sides of lengths $5$ and $6$. Find all possible lengths of the third side.''',
r'''Let $AB=5$ and $AC=6$, with circumradius $R=5$. By the extended law of sines, $\sin C=\dfrac{AB}{2R}=\dfrac12$ and $\sin B=\dfrac{AC}{2R}=\dfrac35$. So $C=30^\circ$ or $150^\circ$, and $\cos B=\pm\dfrac45$.

Since $C$ is opposite the shorter side $AB<AC$, $C<B$, so $C=30^\circ$ ($C=150^\circ$ would leave $B<30^\circ$). Two cases remain, $B$ acute or obtuse, and both occur:
\begin{center}
'''+asy(fig1,'4.2cm')+r'''\qquad
'''+asy(fig2,'4.2cm')+r'''
\end{center}
The third side is $BC=2R\sin A=10\sin(B+C)=10(\sin B\cos C+\cos B\sin C)=10\left(\dfrac35\cdot\dfrac{\sqrt3}{2}\pm\dfrac45\cdot\dfrac12\right)$:
\begin{itemize}
\item $B$ acute (left): $BC=3\sqrt3+4\approx9.20$;
\item $B$ obtuse (right): $BC=3\sqrt3-4\approx1.20$.
\end{itemize}
So the third side is $\boxed{3\sqrt3+4\text{ or }3\sqrt3-4}$.''',
'Law of sines|Circumcircles and circumcentres|Trigonometry|Triangles',5,
note='The post expects one answer; there are two triangles, and both lengths are given.')

# ---------------- 1741190 building a house
b.add(1741190,1,r'''I work alone on building a house for $5$ months; then my brother joins me and we finish it together in the next $4$ months. If instead my brother had joined me after $1$ month, we would have finished in $7$ months altogether. How long would each of us take to build the house alone?''',
r'''Let me build $m$ and my brother $b$ of the house per month. Then
\[
5m+4(m+b)=1\quad\text{and}\quad m+6(m+b)=1,
\]
i.e.\ $9m+4b=1$ and $7m+6b=1$. Multiplying the first by $3$ and the second by $2$ and subtracting: $13m=1$, so $m=\dfrac1{13}$, and then $4b=1-\dfrac9{13}=\dfrac4{13}$, $b=\dfrac1{13}$. Each of us would take $\boxed{13\text{ months}}$ alone.''',
'Work and rates|Systems of linear equations',3,
note='"We could have finished it in 7 months" is read as 7 months in total (1 month alone and 6 together).')

# ---------------- 1741553 f(x+1)=x^3
b.add(1741553,1,r'''If $f(x+1)=x^3$ for all real $x$, find $f(x)$.''',
r'''Put $t=x+1$, so $x=t-1$ and $f(t)=(t-1)^3$ for every real $t$. Hence $f(x)=\boxed{(x-1)^3}=x^3-3x^2+3x-1$.''',
'Functions|Substitution',1)

# ---------------- 1740713 Newton's cows
b.add(1740713,1,r'''$P$ cows graze $Q$ fields bare in $R$ days, $P'$ cows graze $Q'$ fields bare in $R'$ days, and $P''$ cows graze $Q''$ fields bare in $R''$ days. All fields start with the same amount of grass, the grass in each field grows at the same constant daily rate, and all cows eat the same amount per day. Find the relation between $P,Q,R,P',Q',R',P'',Q'',R''$.''',
r'''Let each field start with $g$ units of grass and grow $r$ units per day, and let each cow eat $c$ units per day. In the first situation the cows eat everything there is over the $R$ days:
\[
PRc=Q(g+rR),\qquad\text{i.e.}\qquad \dfrac{PR}{Q}=\dfrac gc+\dfrac rc\,R .
\]
Similarly $\dfrac{P'R'}{Q'}=\dfrac gc+\dfrac rc\,R'$ and $\dfrac{P''R''}{Q''}=\dfrac gc+\dfrac rc\,R''$. So the three points $\left(R,\dfrac{PR}{Q}\right)$, $\left(R',\dfrac{P'R'}{Q'}\right)$, $\left(R'',\dfrac{P''R''}{Q''}\right)$ lie on one line, which is exactly the condition
\[
\begin{vmatrix}\dfrac{PR}{Q}&R&1\\[2mm]\dfrac{P'R'}{Q'}&R'&1\\[2mm]\dfrac{P''R''}{Q''}&R''&1\end{vmatrix}=0,
\quad\text{i.e.}\quad
\boxed{\dfrac{PR}{Q}(R'-R'')+\dfrac{P'R'}{Q'}(R''-R)+\dfrac{P''R''}{Q''}(R-R')=0.}
\]
(Conversely, when this holds and the $R$'s are not all equal, suitable $\dfrac gc$ and $\dfrac rc$ exist.) This is Newton's relation from the \emph{Arithmetica Universalis}.''',
'Work and rates|Systems of linear equations|Matrices and determinants',4,
note='Historical problem (Newton); the relation is derived and checked numerically.')

# ---------------- 1730513 circle and donuts
b.add(1730513,1,r'''In how many ways can $7$ people sit around a circular table, if rotations of an arrangement are considered the same?''',
r'''Fix one person's seat to remove the rotations; the other $6$ people can then be arranged in $6!=\boxed{720}$ ways.''',
'Circular arrangements|Permutations',1)
b.add(1730513,2,r'''A shop sells $4$ kinds of donuts (with plenty of each kind). In how many ways can I choose $8$ donuts if I must take at least one of each kind? (Donuts of the same kind are identical.)''',
r'''Take one donut of each kind first; then choose the remaining $4$ donuts freely from $4$ kinds. By stars and bars this can be done in $\dbinom{4+3}{3}=\dbinom73=\boxed{35}$ ways.''',
'Stars and bars|Distributions and integer solutions',2,
note='"I find 8 donuts ... at least 1 of each 4 kinds" read as choosing 8 donuts from 4 kinds with at least one of each.')

# ---------------- 1740624 2x+3y unbounded
b.add(1740624,1,r'''Is the problem ``Find the maximum value of $f(x,y)=2x+3y$'' (over all real $x,y$) a valid problem? Prove your answer.''',
r'''No: $f$ has no maximum value. Take $x=t$, $y=0$: then $f(t,0)=2t$, which exceeds any proposed maximum value $M$ once $t>\dfrac M2$. So $f$ is unbounded above and has no maximum. $\blacksquare$

Such a problem only makes sense with constraints on $x$ and $y$ (for example $x,y\ge0$ and $x+y\le4$, where the maximum $12$ is attained at $(0,4)$, a vertex of the allowed region).''',
'Maxima and minima|Functions',1,
note='The post asks whether the problem is valid; the record asks for a proof that it has no maximum.')

# ---------------- 1740548 fourth root
b.add(1740548,1,r'''Simplify $\sqrt[4]{16x^8y^4z^{16}}$ for real numbers $x,y,z$. Is the answer $2x^2yz^4$ the same as $x^2yz^4\sqrt[4]{16}$?''',
r'''For real $u$, $\sqrt[4]{u^4}=|u|$. Here
\[
\sqrt[4]{16x^8y^4z^{16}}=\sqrt[4]{2^4\,(x^2)^4\,y^4\,(z^4)^4}=2x^2|y|z^4,
\]
since $x^2$ and $z^4$ are already nonnegative. So the answer is $\boxed{2x^2|y|z^4}$, which equals $2x^2yz^4$ when $y\ge0$ (as the textbook presumably assumes).

The two forms in the question are the same: $\sqrt[4]{16}=2$, so $x^2yz^4\sqrt[4]{16}=2x^2yz^4$. There is no error in the solutions manual (apart from the absolute value needed when $y$ may be negative).''',
'Radicals|Exponents|Absolute value',2,
note='The poster thinks the manual\'s 2x^2yz^4 is wrong; it is the same as x^2yz^4 times the fourth root of 16. The absolute value on y is added for real y.')

# ---------------- 1738754 MATHCOUNTS letters (alias)
b.add(1738754,1,r'''How many different four-letter arrangements can be formed using four of the ten letters of MATHCOUNTS (each letter used at most as often as it occurs)?''',
r'''MATHCOUNTS has eight distinct letters other than T, and two T's. With no T: $8\cdot7\cdot6\cdot5=1680$; with one T: $4\cdot8\cdot7\cdot6=1344$; with two T's: $\dbinom42\cdot8\cdot7=336$. The total is $\boxed{3360}$.''',
'Multiset permutations|Casework',3,
note='Repeat of an earlier record (aliased).')

# ---------------- 1740467 interval notation
b.add(1740467,1,r'''Write the set of all real numbers other than $-8$ and $-2$ in interval notation.''',
r'''Remove the two points from the real line, leaving three open intervals:
\[
\boxed{(-\infty,-8)\cup(-8,-2)\cup(-2,\infty)}.
\]''',
'Inequalities',1)

# ---------------- 1740568 monic cubic
b.add(1740568,1,r'''Construct a monic cubic polynomial with integer coefficients that has $3$ and $\sqrt2-1$ as roots. Is it unique?''',
r'''If $p$ has rational coefficients and $p(\sqrt2-1)=0$, write $p(x)=(x^2+2x-1)q(x)+(ux+v)$ with $q,u,v$ rational ($x^2+2x-1$ is the polynomial with roots $-1\pm\sqrt2$). Then $u(\sqrt2-1)+v=0$, and since $\sqrt2$ is irrational, $u=v=0$. So $x^2+2x-1$ divides $p$, and $-1-\sqrt2$ is also a root.

A monic cubic with roots $3$, $-1+\sqrt2$, $-1-\sqrt2$ is therefore
\[
(x-3)(x^2+2x-1)=\boxed{x^3-x^2-7x+3},
\]
and it is the only one: a monic cubic is determined by its three roots, and we have shown that all three are forced.''',
'Polynomials|Polynomial roots|Radicals',3)

b.save()
