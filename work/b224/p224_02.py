from qb import *
b=Bank('p224_02')

# ---------------- 1770935 quartic with rational roots
b.add(1770935,1,r'''Find all solutions of $2x^4-15x^3+41x^2-48x+20=0$, listed from least to greatest.''',
r'''The coefficients add up to $2-15+41-48+20=0$, so $x=1$ is a root. Also $2\cdot16-15\cdot8+41\cdot4-48\cdot2+20=32-120+164-96+20=0$, so $x=2$ is a root. Dividing by $(x-1)(x-2)=x^2-3x+2$,
\[
2x^4-15x^3+41x^2-48x+20=(x^2-3x+2)(2x^2-9x+10)=(x-1)(x-2)(x-2)(2x-5).
\]
So the solutions are $\boxed{x=1,\ 2,\ \dfrac52}$, where $x=2$ is a double root. All roots are real and rational.''',
'Polynomials|Polynomial roots|Factoring',2,
note='The post asks for the "solutions to the polynomial"; read as the roots of the equation = 0.')

# ---------------- 1770709 two multiples of 5
b.add(1770709,1,r'''Two different integers are chosen at random from $1$ to $20$. What is the probability that both are multiples of $5$?''',
r'''There are $\dbinom{20}{2}=190$ equally likely pairs. The multiples of $5$ are $5,10,15,20$, which form $\dbinom42=6$ pairs. The probability is
\[
\dfrac{6}{190}=\boxed{\dfrac{3}{95}} .
\]
(Counting ordered choices gives the same answer: $\dfrac{4\cdot3}{20\cdot19}=\dfrac{12}{380}=\dfrac{3}{95}$.) Neither of the poster's candidates $\dfrac{6}{95}$ and $\dfrac{12}{95}$ is correct; both come from mixing an ordered count with an unordered one.''',
'Probability|Combinations|Sampling without replacement',2,
note='The garbled question ("get 2 numbers in which multiples of 5") is read as both chosen numbers being multiples of 5, the reading consistent with the poster\'s candidates; the correct answer 3/95 is neither of them.')

# ---------------- 1770602 Pythagorean triple with leg 2017
b.add(1770602,1,r'''The three side lengths of a right triangle are integers, and one of the legs has length $2017$ (a prime number). Find the length of the other leg.''',
r'''Let the other leg be $b$ and the hypotenuse $c$. Then
\[
2017^2=c^2-b^2=(c-b)(c+b),
\]
with $0<c-b<c+b$. Since $2017$ is prime, the factorisations of $2017^2$ are $1\cdot2017^2$ and $2017\cdot2017$, and the second would give $c-b=c+b$, i.e.\ $b=0$. So $c-b=1$ and $c+b=2017^2=4068289$, giving
\[
b=\dfrac{4068289-1}{2}=\boxed{2034144},\qquad c=2034145 .
\]
No guessing is needed: for any odd prime $p$ the only triple with leg $p$ is $p,\ \dfrac{p^2-1}{2},\ \dfrac{p^2+1}{2}$.''',
'Pythagorean triples|Difference of squares|Prime numbers|Diophantine equations',3)

# ---------------- 1770185 five spheres in a square pyramid
fig=r'''real r=1, d=r*sqrt(2);
pair L=(-d,r),R=(d,r),T=(0,r+d),O=(0,r);
draw((-2.7,0)--(3.0,0),linewidth(0.8));
draw(circle(L,r),linewidth(0.9));draw(circle(R,r),linewidth(0.9));draw(circle(T,r),linewidth(0.9));
draw(L--T--R,blue+dashed);draw(L--R,dashed);draw(O--T,red);
dot(L);dot(R);dot(T);dot(O);
draw((2.8,0)--(2.8,r+d+r),Arrows(TeXHead));label("$h$",(2.8,(r+d+r)/2),E);
draw((0,r+d+r)--(2.9,r+d+r),dotted);
pair sh=(6.6,0.2); real g=1.7;
pair l=sh+g*(-d,0),rr=sh+g*(d,0),t=sh+g*(0,d),o=sh;
draw(l--t--rr,blue+dashed);draw(l--rr,dashed);draw(o--t,red);
draw(o+(0.2,0)--o+(0.2,0.2)--o+(0,0.2),red);
dot(l);dot(rr);dot(t);dot(o);
label("$2r$",(l+t)/2,NW,blue);label("$2r$",(rr+t)/2,NE,blue);
label("$r\sqrt2$",(l+o)/2,S);label("$r\sqrt2$",(o+rr)/2,S);
label("$r\sqrt2$",o+0.35*(t-o),E,red);'''
b.add(1770185,1,r'''Five congruent spheres of radius $r$ form a square pyramid resting on a horizontal table: the four base spheres lie on the table with their centres at the corners of a square, each tangent to its two neighbours, and the fifth sphere sits on top, tangent to all four base spheres. Find the height of the top of the pyramid (the highest point of the top sphere) above the table, in terms of $r$.''',
r'''The centres of the base spheres are at height $r$ and form a square of side $2r$ (neighbouring spheres are tangent). Its centre $O$ is at distance $\dfrac{2r\sqrt2}{2}=r\sqrt2$ from each corner. The centre of the top sphere lies above $O$ at distance $2r$ from each base centre. The figure shows the vertical cross-section through two opposite base spheres (left) and the triangle formed by their centres and the top centre (right).
'''+asy(fig,'8cm')+r'''
By the Pythagorean theorem, the top centre is $\sqrt{(2r)^2-(r\sqrt2)^2}=r\sqrt2$ above the plane of the base centres. So the highest point of the top sphere is at height
\[
h=r+r\sqrt2+r=\boxed{(2+\sqrt2)\,r}.
\]
(The pyramid formed by the five centres has height $r\sqrt2$.)''',
'Spheres|Solid geometry|Pythagorean theorem|Squares',3,
note='"The height of the pyramid" is ambiguous; the record asks for the height of the top above the table, (2 + sqrt 2) r, and also gives the height r sqrt 2 of the pyramid of centres.')

# ---------------- 1770260 AP^2 = BP^2 + CP^2 implies angle BPC = 150
fig=r'''real s3=sqrt(3);
pair B=(0,0),C=(4,0),A=(2,2*s3);
pair P=(2,-2*s3)+4*dir(80);
pair Pp=rotate(60,B)*P;
draw(A--B--C--cycle,linewidth(0.9));
draw(P--A);draw(P--B);draw(P--C);
draw(B--Pp,blue+dashed);draw(P--Pp,blue+dashed);draw(A--Pp,blue+dashed);
pair u=unit(A-Pp),v=unit(P-Pp);
draw(Pp+0.25*u--Pp+0.25*u+0.25*v--Pp+0.25*v,blue);
dot(P);dot(Pp,blue);
label("$A$",A,N);label("$B$",B,SW);label("$C$",C,SE);
label("$P$",P,dir(25));label("$P'$",Pp,W,blue);'''
b.add(1770260,1,r'''Let $P$ be a point inside an equilateral triangle $ABC$ such that $AP^2=BP^2+CP^2$. Prove that $\angle BPC=150^\circ$.''',
r'''Rotate triangle $BPC$ about $B$ through $60^\circ$, in the direction that takes $C$ to $A$ (possible because $BC=BA$ and $\angle CBA=60^\circ$). Let $P$ go to $P'$.
'''+asy(fig,'5.5cm')+r'''
Then $BP'=BP$ and $\angle PBP'=60^\circ$, so triangle $BPP'$ is equilateral: $PP'=BP$ and $\angle BP'P=60^\circ$. Also $AP'=CP$ and $\angle BP'A=\angle BPC$, since the rotation carries triangle $BPC$ onto triangle $BP'A$.

In triangle $AP'P$,
\[
AP'^2+PP'^2=CP^2+BP^2=AP^2 ,
\]
so by the converse of the Pythagorean theorem $\angle AP'P=90^\circ$. The point $P$ lies inside the triangle and $P'$ outside it beyond side $AB$, so the ray $P'B$ lies on the far side of $P'P$ from $A$ and
\[
\angle BPC=\angle BP'A=\angle BP'P+\angle PP'A=60^\circ+90^\circ=150^\circ .\qquad\blacksquare
\]''',
'Equilateral triangles|Rotations|Pythagorean theorem|Congruence|Angle chasing',5)

# ---------------- 1769463 9 red and 3 blue balloons in a circle
b.add(1769463,1,r'''Nine red and three blue balloons are to be placed in a circle. Find the number of distinct circular arrangements of the balloons, if two arrangements are considered the same when one can be obtained from the other by a rotation or a reflection.''',
r'''Going round the circle, the three blue balloons split the nine red ones into three gaps of sizes $a,b,c\ge0$ with $a+b+c=9$. An arrangement is determined by the cyclic sequence of gaps, and rotations and reflections of the circle permute the three gaps cyclically or reverse their order. For three gaps these operations produce every ordering of $(a,b,c)$, so an arrangement corresponds exactly to an unordered triple $\{a,b,c\}$, that is, a partition of $9$ into at most $3$ parts:
\[
900,\ 810,\ 720,\ 711,\ 630,\ 621,\ 540,\ 531,\ 522,\ 441,\ 432,\ 333
\]
(written as $abc$ with $a\ge b\ge c$). There are $\boxed{12}$ arrangements.

Check with Burnside's lemma: the $24$ symmetries fix $\dbinom{12}{3}=220$ (identity), $4$ each (the two rotations by a third of a turn), $10$ each (the six reflections through two balloons: one fixed position blue and one symmetric pair blue) and $0$ for the rest, giving $\dfrac{220+8+60}{24}=12$.''',
'Circular arrangements|Burnside\'s lemma|Partitions and compositions|Symmetry',4)

# ---------------- 1770219 cone from a quarter circle
fig=r'''real r=2.4;
pair O=(0,0),K=(r,0),J=(0,r);
draw(O--K,linewidth(0.9));draw(O--J,linewidth(0.9));draw(arc(O,r,0,90),linewidth(0.9));
draw((0.3,0)--(0.3,0.3)--(0,0.3));
label("$O$",O,SW);label("$K$",K,SE);label("$J$",J,NW);label("$r$",(r/2,0),S);label("$r$",(0,r/2),W);
draw((r+0.4,r/2)--(r+1.4,r/2),Arrow(TeXHead));
real a=r/4, h=sqrt(r^2-a^2);
pair V=(r+2.4+a,r+0.1), c=(r+2.4+a,r+0.1-h);
draw(ellipse(c,a,0.12),linewidth(0.9));
draw(V--(c+(a,0)),linewidth(0.9));draw(V--(c-(a,0)),linewidth(0.9));
draw(V--c,dashed);draw(c--c+(a,0),dashed);
label("$O$",V,N);label("$r$",(V+c+(a,0))/2,E);label("$h$",(V+c)/2,W);label("$\dfrac{r}{4}$",c+(a/2,-0.12),S);'''
b.add(1770219,1,r'''A sector of a circle with central angle $90^\circ$ and radius $r$ has radii $OK$ and $OJ$, where $K$ and $J$ are points on the circle. The sector is cut out and curved so that $OK$ and $OJ$ coincide, forming the lateral surface of a cone. Find the volume of the cone in terms of $r$.''',
r'''The radius $r$ of the sector becomes the slant height of the cone, and the arc $KJ$ becomes the circumference of the base. The arc has length $\dfrac14\cdot2\pi r=\dfrac{\pi r}{2}$, so the base radius $a$ satisfies $2\pi a=\dfrac{\pi r}{2}$, i.e.\ $a=\dfrac r4$.
'''+asy(fig,'7cm')+r'''
The height is $h=\sqrt{r^2-\dfrac{r^2}{16}}=\dfrac{r\sqrt{15}}{4}$, so the volume is
\[
V=\dfrac13\pi a^2h=\dfrac13\pi\cdot\dfrac{r^2}{16}\cdot\dfrac{r\sqrt{15}}{4}=\boxed{\dfrac{\sqrt{15}\,\pi r^3}{192}} .
\]''',
'Cones|Volume|Nets|Pythagorean theorem|Arcs and chords',3,
note='The word "Construct" is kept as a description; the task is to find the volume.')

# ---------------- 1770209 similar pyramids
fig=r'''pair d=(0.55,0.35);
void pyr(pair o,real s,string lab){
  pair p0=o,p1=o+(s,0),p2=o+(s,0)+s*d,p3=o+s*d,apex=o+(s/2,0)+s*d/2+(0,1.3*s);
  draw(p0--p1--p2,linewidth(0.9));draw(p2--p3--p0,dashed);
  draw(apex--p0,linewidth(0.9));draw(apex--p1,linewidth(0.9));draw(apex--p2,linewidth(0.9));draw(apex--p3,dashed);
  label(lab,o+(s/2,0),S);
}
real k=sqrt(10/17);
pyr((0,0),2*k,"$A=10,\ V=\,?$");
pyr((2.6,0),2,"$A=17,\ V=13$");'''
b.add(1770209,1,r'''Two similar pyramids have surface areas $10$ and $17$. If the larger pyramid has a volume of $13$, find the volume of the smaller pyramid.''',
r'''If the smaller pyramid is the larger one scaled by a factor $k$, then areas scale by $k^2$ and volumes by $k^3$.
'''+asy(fig,'6cm')+r'''
Here $k^2=\dfrac{10}{17}$, so $k=\sqrt{\dfrac{10}{17}}$ and
\[
V=13k^3=13\cdot\dfrac{10}{17}\sqrt{\dfrac{10}{17}}=\dfrac{130\sqrt{10}}{17\sqrt{17}}=\boxed{\dfrac{130\sqrt{170}}{289}}\approx5.86 .
\]''',
'Scaling of length, area, and volume|Pyramids|Volume|Surface area|Similarity',2)

# ---------------- 1770041 Ansel's boat (alias)
b.add(1770041,1,r'''Ansel left the dock in his motorboat, travelled $10$ miles downstream, and then returned to the dock along the same route, travelling against the current. His speed relative to the water was $20$ miles per hour on both legs. If the round trip took $64$ minutes, what is the speed of the river's current?''',
r'''With current $c$, $\dfrac{10}{20+c}+\dfrac{10}{20-c}=\dfrac{16}{15}$, so $\dfrac{400}{400-c^2}=\dfrac{16}{15}$, $c^2=25$ and the current is $\boxed{5}$ miles per hour.''',
'Distance, rate, and time|Rational equations|Relative speed',3,
note='MATHCOUNTS Handbook 2017-18; repeat of an earlier record (aliased).')

# ---------------- 1769320 k^2+37k+299 a perfect square
b.add(1769320,1,r'''Positive integers $p$ and $k$ satisfy $p=k^2+37k+299$, and $p$ is a perfect square. What is the value of $\sqrt p+k$?''',
r'''Let $p=m^2$ with $m>0$. Multiply by $4$ and complete the square:
\[
4m^2=4k^2+148k+1196=(2k+37)^2-173 ,
\]
so $(2k+37-2m)(2k+37+2m)=173$. Both factors are integers and the second is positive, so the first is too; since $173$ is prime, $2k+37-2m=1$ and $2k+37+2m=173$. Then $4m=172$, $m=43$, and $2k+37=87$, $k=25$. Check: $625+925+299=1849=43^2$. Hence $\sqrt p+k=43+25=\boxed{68}$.''',
'Perfect squares|Completing the square|Difference of squares|Diophantine equations|Prime numbers',4)

# ---------------- 1769062 prism and pyramid
fig=r'''pair d=(0.45,0.3);
real a=8,bb=12,h=16, s=0.25;
pair p0=(0,0),p1=(bb*s,0),p2=p1+a*s*d,p3=a*s*d,up=(0,h*s);
draw(p0--p1--p2,linewidth(0.9));draw(p2--p3--p0,dashed);
draw(p0+up--p1+up--p2+up--p3+up--cycle,linewidth(0.9));
draw(p0--p0+up,linewidth(0.9));draw(p1--p1+up,linewidth(0.9));draw(p2--p2+up,linewidth(0.9));draw(p3--p3+up,dashed);
label("$y=12$",(p0+p1)/2,S);label("$x=8$",(p1+p2)/2,SE);label("$2x=16$",p0+up/2,W);'''
b.add(1769062,1,r'''A rectangular prism has a base with a perimeter of $40$ inches. Its height is twice the shorter side of the base. If the volume is $1536$ cubic inches, what is the length of the longer side of the base?''',
r'''Let the base be $x$ by $y$ with $x\le y$. Then $x+y=20$, the height is $2x$, and
\[
x\cdot y\cdot2x=1536\ \Longrightarrow\ x^2(20-x)=768\ \Longrightarrow\ x^3-20x^2+768=0 .
\]
Trying divisors of $768$, $x=8$ works: $512-1280+768=0$. Then $x^3-20x^2+768=(x-8)(x^2-12x-96)$, and the quadratic has roots $6\pm2\sqrt{33}$. The negative root is impossible, and $x=6+2\sqrt{33}\approx17.5$ would give $y=20-x\approx2.5<x$, contradicting $x\le y$. So $x=8$, $y=12$, the height is $16$, and the longer side of the base is $\boxed{12}$ inches.
'''+asy(fig,'4.5cm')+r'''
Check: $2(8+12)=40$ and $8\cdot12\cdot16=1536$.''',
'Cubes and rectangular prisms|Volume|Polynomials|Polynomial roots',3,
note='The volume unit "in^2" in the post is corrected to cubic inches.')
fig=r'''pair d=(0.45,0.3);
real L=14,Wd=12,H=17,s=0.22;
pair p0=(0,0),p1=(L*s,0),p2=p1+Wd*s*d,p3=Wd*s*d,ctr=(p0+p2)/2,apex=ctr+(0,H*s);
draw(p0--p1--p2,linewidth(0.9));draw(p2--p3--p0,dashed);
draw(apex--p0,linewidth(0.9));draw(apex--p1,linewidth(0.9));draw(apex--p2,linewidth(0.9));draw(apex--p3,dashed);
draw(apex--ctr,dashed);dot(ctr);
label("$x=14$",(p0+p1)/2,S);label("$x-2=12$",(p1+p2)/2,SE);real xr=p0.x-0.35; draw((xr,ctr.y)--(xr,apex.y),Arrows(TeXHead)); draw(apex--(xr-0.1,apex.y),dotted); draw(ctr--(xr-0.1,ctr.y),dotted); label("$x+3=17$",(xr,(ctr.y+apex.y)/2),W);'''
b.add(1769062,2,r'''A right rectangular pyramid has a base of length $x$ inches and width $2$ inches less than the length, and its height is $3$ inches more than the length. If the volume is $952$ cubic inches, what is the width of the pyramid, in inches?''',
r'''The volume is $\dfrac13\cdot x(x-2)\cdot(x+3)=952$, so
\[
x(x-2)(x+3)=2856\ \Longleftrightarrow\ x^3+x^2-6x-2856=0 .
\]
Since $14\cdot12\cdot17=2856$, $x=14$ is a root, and $x^3+x^2-6x-2856=(x-14)(x^2+15x+204)$. The quadratic has discriminant $225-816<0$, so $x=14$ is the only real solution.
'''+asy(fig,'7cm')+r'''
The width is $14-2=\boxed{12}$ inches.''',
'Pyramids|Volume|Polynomials|Polynomial roots',3)

# ---------------- 1769946 MIC 2018 4th #11
b.add(1769946,1,r'''Kylo Ren, Captain Phasma and three identical First Order Stormtroopers line up. If Kylo Ren insists on being first, how many different ways can the five of them line up?''',
r'''Kylo Ren takes the first place. The remaining four places hold Captain Phasma and three identical Stormtroopers, so an arrangement is determined by Phasma's place: $4$ choices. The answer is $\boxed{4}$ (equivalently $\dfrac{4!}{3!}=4$).''',
'Multiset permutations|Arrangements with restrictions',1,source=src('Math Is Cool',2018,'4th Grade',11))

# ---------------- 1769951 MIC 2018 4th #26 palindrome dates
b.add(1769951,1,r'''When the month, day and two-digit year are written in the form m/d/yy (without extra zeros), some dates form palindromes, which read the same forwards and backwards when the slashes are ignored; for example, 8/14/18 gives $81418$. What is the total number of palindrome dates that occur in $2018$ (including the example)?''',
r'''The digit string is $m$, then $d$, then $18$. For a palindrome it must begin with $81$. So the month starts with the digit $8$, and the only such month is $8$ (August; months $10$ to $12$ start with $1$). The string is then $8\,d\,18$, which must read $81\ldots18$.
\begin{itemize}
\item If $d$ has one digit, the string $8d18$ is a palindrome only for $d=1$: the date 8/1/18.
\item If $d$ has two digits $d_1d_2$, the string $8d_1d_218$ is a palindrome exactly when $d_1=1$, with $d_2$ free in the middle: the days $10$ to $19$, all valid in August.
\end{itemize}
The total is $1+10=\boxed{11}$.''',
'Palindromes|Calendar and clock problems|Casework',2,source=src('Math Is Cool',2018,'4th Grade',26))

# ---------------- 1769749 symmetric polynomial value
b.add(1769749,1,r'''Numbers $a,b,c$ satisfy $a+b+c=6$, $a^2+b^2+c^2=26$ and $a^3+b^3+c^3=84$. Find the value of
\[
P=\left(a^2+ab+b^2\right)\left(b^2+bc+c^2\right)\left(c^2+ca+a^2\right).
\]''',
r'''Let $e_1=a+b+c=6$, $e_2=ab+bc+ca$ and $e_3=abc$. From $a^2+b^2+c^2=e_1^2-2e_2$ we get $26=36-2e_2$, so $e_2=5$. From $a^3+b^3+c^3=e_1^3-3e_1e_2+3e_3$ we get $84=216-90+3e_3$, so $e_3=-14$. Hence $a,b,c$ are the roots of
\[
q(t)=t^3-6t^2+5t+14 .
\]
Now
\[
a^2+ab+b^2=(a+b)^2-ab=(a+b)(a+b+c)-\bigl(ab+c(a+b)\bigr)=e_1(a+b)-e_2=6(6-c)-5=31-6c ,
\]
and similarly for the other two factors. So
\[
P=(31-6a)(31-6b)(31-6c)=6^3\,q\!\left(\dfrac{31}{6}\right)=31^3-6\cdot6\cdot31^2+5\cdot36\cdot31+14\cdot216 .
\]
This equals $29791-34596+5580+3024=\boxed{3799}$.

(The cubic $q$ has only one real root, so $a,b,c$ cannot all be real; the value of $P$ does not depend on this.)''',
'Vieta\'s formulas|Newton\'s sums|Algebraic expressions and identities|Polynomials',5,
note='The post calls a, b, c real numbers, but no real numbers satisfy the three conditions (t^3 - 6t^2 + 5t + 14 has one real root); the word "real" is dropped. The value P = 3799 was checked numerically with the complex roots.')

# ---------------- 1769594 radical equation (repaired)
b.add(1769594,1,r'''Positive real numbers $x$ and $y$ satisfy
\[
3y+\sqrt[3]{4x^2}=2\sqrt[6]{108x^2y^3}.
\]
What is the value of $\dfrac{x^2}{y^3}$?''',
r'''Let $u=3y>0$ and $v=\sqrt[3]{4x^2}>0$. Then
\[
(uv)^3=27y^3\cdot4x^2=108x^2y^3,\qquad\text{so}\qquad\sqrt[6]{108x^2y^3}=\sqrt{uv}.
\]
The equation says $u+v=2\sqrt{uv}$, i.e.\ $\left(\sqrt u-\sqrt v\right)^2=0$ (equality in AM-GM). So $u=v$: $3y=\sqrt[3]{4x^2}$, hence $27y^3=4x^2$ and
\[
\dfrac{x^2}{y^3}=\boxed{\dfrac{27}{4}} .
\]
(For example $y=1$, $x=\dfrac{3\sqrt3}{2}$ works.)

Without the factor $2$, as in the original post, the equation $u+v=\sqrt{uv}$ has no solution with $u,v>0$, because $\sqrt{uv}\le\dfrac{u+v}{2}<u+v$; this is why the factor $2$ must have been intended.''',
'Radicals|AM-GM inequality|Exponents|Substitution',4,
note='As posted, 3y + cbrt(4x^2) = sixth-root(108x^2y^3) has no solution with x^2/y^3 defined (by AM-GM the left side exceeds the right unless x = y = 0). The record restores the factor 2 on the right, which makes it the standard AM-GM equality problem, answer 27/4, and explains why the original fails.')

# ---------------- 1769528 101 divides 1+11+...+R_n
b.add(1769528,1,r'''Let $a_n=1+11+111+\cdots+\underbrace{11\ldots1}_{n}$. Determine the smallest $n\ge1000$ for which $101\mid a_n$.''',
r'''Since $\underbrace{11\ldots1}_{k}=\dfrac{10^k-1}{9}$,
\[
a_n=\sum_{k=1}^{n}\dfrac{10^k-1}{9}=\dfrac{1}{9}\left(\dfrac{10^{n+1}-10}{9}-n\right)=\dfrac{10^{n+1}-10-9n}{81}.
\]
As $\gcd(81,101)=1$, we need $10^{n+1}\equiv10+9n\pmod{101}$. Now $10^2=100\equiv-1$, so $10^4\equiv1$ and $10^{n+1}$ depends only on $n\bmod4$. Using $9^{-1}\equiv45\pmod{101}$ (since $9\cdot45=405=4\cdot101+1$):
\begin{itemize}
\item $n\equiv3\pmod4$: $1\equiv10+9n$, so $9n\equiv-9$ and $n\equiv-1\equiv100\pmod{101}$;
\item $n\equiv0\pmod4$: $10\equiv10+9n$, so $n\equiv0\pmod{101}$;
\item $n\equiv1\pmod4$: $-1\equiv10+9n$, so $n\equiv-11\cdot45\equiv10\pmod{101}$;
\item $n\equiv2\pmod4$: $-10\equiv10+9n$, so $n\equiv-20\cdot45\equiv9\pmod{101}$.
\end{itemize}
Combining each case by the Chinese remainder theorem modulo $404$ gives $n\equiv403,\ 0,\ 313,\ 110\pmod{404}$. The values from $1000$ upwards are $808+313=1121$, $808+403=1211$, $1212$, \dots{} (and $808+110=918<1000$). The smallest is $n=\boxed{1121}$.''',
'Remainders and congruences|Modular exponentiation|Chinese remainder theorem|Geometric sequences|Summation',5,
note='Checked by computing a_n mod 101 directly for n up to 1300.')

# ---------------- 1760794 sqrt(5-2x) > x-1
b.add(1760794,1,r'''Solve the inequality $\sqrt{5-2x}>x-1$.

A student argues: ``If $x-1<0$, the inequality holds whenever $5-2x\ge0$, which gives $x<1$. If $x-1\ge0$, both sides may be squared: $5-2x>x^2-2x+1$, so $-2<x<2$. Combining everything, the answer is $-2<x<2$.'' The answer key says $x<2$. Which is right, and what is wrong with the student's conclusion?''',
r'''The square root requires $5-2x\ge0$, i.e.\ $x\le\dfrac52$.

\textbf{Case $x<1$.} The right side is negative and the left side is nonnegative, so every $x<1$ is a solution (all such $x$ satisfy $x\le\dfrac52$).

\textbf{Case $1\le x\le\dfrac52$.} Both sides are nonnegative, so the inequality is equivalent to $5-2x>(x-1)^2=x^2-2x+1$, i.e.\ $x^2<4$, i.e.\ $-2<x<2$. Together with $1\le x\le\dfrac52$ this gives $1\le x<2$.

The solution set is the \emph{union} of the two cases: $x<1$ or $1\le x<2$, that is, $\boxed{x<2}$. The answer key is right.

The student's case work is correct, but at the end the condition $-2<x<2$ from the second case was intersected with everything (including the first case's $x<1$) instead of being combined only with $1\le x\le\dfrac52$ and then joined to the first case. For example $x=-5$ is a solution, since $\sqrt{15}>-6$, but it is excluded by $-2<x<2$.''',
'Inequalities|Radicals|Proof by cases',2,
note='The record asks for the solution and for the error in the poster\'s argument (it intersects the two cases instead of taking their union).')

# ---------------- 1769328 p(p-2)+4k(k-p+1)=3
b.add(1769328,1,r'''Real numbers $p$ and $k$ satisfy $p(p-2)+4k(k-p+1)=3$. What is the sum of the greatest and least possible values of $p-2k$?''',
r'''Expand: $p^2-2p+4k^2-4kp+4k=3$. The terms regroup as
\[
(p-2k)^2-2(p-2k)=3 .
\]
With $t=p-2k$, $t^2-2t-3=0$, so $(t-3)(t+1)=0$ and $t=3$ or $t=-1$. Both occur: $(p,k)=(3,0)$ gives $3\cdot1+0=3$, and $(p,k)=(-1,0)$ gives $(-1)(-3)+0=3$. The sum of the greatest and least values is $3+(-1)=\boxed{2}$.''',
'Substitution|Quadratic equations|Completing the square',3,
note='p and k are taken to be real numbers.')

# ---------------- 1769179 10x^2+5y^2+2xy-14x=-5
b.add(1769179,1,r'''Real numbers $x$ and $y$ satisfy $10x^2+5y^2+2xy-14x=-5$. What is the value of $x+y$?''',
r'''View the equation as a quadratic in $y$: $5y^2+2x\,y+(10x^2-14x+5)=0$. For a real $y$ the discriminant must be nonnegative:
\[
4x^2-20(10x^2-14x+5)=-196x^2+280x-100=-4(7x-5)^2\ge0 .
\]
So $7x-5=0$, $x=\dfrac57$, and then the double root is $y=-\dfrac{2x}{10}=-\dfrac{x}{5}=-\dfrac17$. Hence $x+y=\dfrac57-\dfrac17=\boxed{\dfrac47}$.

(Equivalently, $5\cdot\bigl(10x^2+5y^2+2xy-14x+5\bigr)=(5y+x)^2+(7x-5)^2$, which is zero only when $7x=5$ and $5y=-x$.)''',
'Quadratic equations|Completing the square|Inequalities',4,
note='x and y are taken to be real (otherwise x + y is not determined).')

# ---------------- 1768864 angle RQZ (alias)
b.add(1768864,1,r'''Point $Z$ is on side $\overline{PR}$ of triangle $PQR$ such that $\angle PZQ=\angle PQZ$, and $\angle PQR-\angle PRQ=42^\circ$. Find $\angle RQZ$.''',
r'''Let $\alpha=\angle PQZ=\angle PZQ$ and $x=\angle RQZ$. The exterior angle $\angle PZQ$ of triangle $QZR$ gives $\alpha=x+\angle PRQ$. Then $42^\circ=(\alpha+x)-(\alpha-x)=2x$, so $\angle RQZ=\boxed{21^\circ}$.''',
'Angle chasing|Isosceles triangles|Triangles',3,
note='AoPS Introduction to Geometry problem; repeat of an earlier record (aliased).')

# ---------------- 1768599 a^(b^c) divisible by 4
b.add(1768599,1,r'''Three distinct integers $a,b,c$ are chosen in order at random from the set $\{1,2,3,4,5,6\}$. What is the probability that $a^{b^c}$ is divisible by $4$?''',
r'''There are $6\cdot5\cdot4=120$ equally likely ordered choices. The exponent $b^c$ is a positive integer, equal to $1$ only when $b=1$.
\begin{itemize}
\item $a$ odd: $a^{b^c}$ is odd. No good choices.
\item $a=4$: $4^{b^c}$ is divisible by $4$ for every exponent: all $5\cdot4=20$ choices of $(b,c)$.
\item $a=2$ or $a=6$: $a^{b^c}$ has exactly $b^c$ factors of $2$, so it is divisible by $4$ exactly when $b^c\ge2$, i.e.\ $b\ne1$. Out of the $20$ choices of $(b,c)$, those with $b=1$ number $4$, leaving $16$ for each of these values of $a$.
\end{itemize}
The probability is $\dfrac{20+16+16}{120}=\dfrac{52}{120}=\boxed{\dfrac{13}{30}}$.''',
'Probability|Exponents|Divisibility|Casework',3,
note='The tower is read as a^(b^c), and the ordered triple (a, b, c) is uniformly random. Checked by enumeration.')

b.save()
