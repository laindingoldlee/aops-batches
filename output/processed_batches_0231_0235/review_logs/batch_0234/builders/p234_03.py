from qb import *
b=Bank('p234_03')
RA=r'''void ra(pair P,pair U,pair V,real s){draw(P+s*unit(U-P)--P+s*unit(U-P)+s*unit(V-P)--P+s*unit(V-P),linewidth(0.5));}
'''

# ---------------- 1713423 a^5 natural
b.add(1713423,1,r'''A student claims: ``If $a^5$ is a natural number, then $a$ is also a natural number.''
\begin{enumerate}
\item[(a)] Show that the claim is false for real numbers $a$.
\item[(b)] Prove that the claim is true if $a$ is a rational number.
\end{enumerate}''',
r'''\textbf{(a)} Take $a=\sqrt[5]{2}$. Then $a^5=2$ is a natural number, but $1<a<2$ (since $1^5<2<2^5$), so $a$ is not a natural number. The claim is false.

\textbf{(b)} Let $a$ be rational with $a^5=n$, a natural number. Since $n>0$, also $a>0$. Write $a=\dfrac pq$ in lowest terms with $p,q$ positive integers and $\gcd(p,q)=1$. Then
\[
p^5=nq^5 .
\]
Suppose $q>1$ and let $r$ be a prime factor of $q$. Then $r\mid nq^5=p^5$, and since $r$ is prime, $r\mid p$. So $r$ divides both $p$ and $q$, contradicting $\gcd(p,q)=1$. Hence $q=1$ and $a=p$ is a natural number. $\blacksquare$''',
'Counterexamples|Radicals|Prime factorisation|Proof by contradiction',3,
note='The post asks to prove the claim as stated, which is false for real a (counterexample 2^(1/5)); the record asks for the counterexample and proves the corrected claim for rational a.')

# ---------------- 1712750 2^200 mod 13
b.add(1712750,1,r'''Find the remainder when $2^{200}$ is divided by $13$.''',
r'''Since $13$ is prime and does not divide $2$, Fermat's little theorem gives $2^{12}\equiv1\pmod{13}$. (Directly: $2^6=64=5\cdot13-1\equiv-1$, so $2^{12}\equiv1$.) As $200=12\cdot16+8$,
\[
2^{200}=\left(2^{12}\right)^{16}\cdot2^8\equiv2^8=256=19\cdot13+9\equiv9\pmod{13}.
\]
The remainder is $\boxed{9}$.''',
'Modular exponentiation|Remainders and congruences|Fermat\'s little theorem',3,
note='Near miss (different exponent) with aops-topic-2796272-q10 (2^2000 mod 13).')

# ---------------- 1713347 RMO mock: AP = BQ = CR
fig=r'''pair A=(1.2,4),B=(0,0),C=(5,0);
pair A1=(A.x,0);
pair H=extension(A,A1,B,B+rotate(90)*(C-A));
real r=4.6;
pair D=(B+C)/2,Ee=(C+A)/2,F=(A+B)/2;
pair hit(pair X,pair Y){pair u=unit(Y-X);pair w=Y-H;real bb=dot(w,u);real cc=dot(w,w)-r*r;real t=-bb+sqrt(bb*bb-cc);return Y+t*u;}
pair P=hit(Ee,F),Q=hit(F,D),R=hit(D,Ee);
pair K=extension(A,A1,Ee,F);
draw(circle(H,r),gray+linewidth(0.8));
draw(Ee--P,gray);draw(F--Q,gray);draw(D--R,gray);
draw(A--A1,dashed);
draw(A--B--C--cycle,linewidth(0.9));
draw(A--P,red+linewidth(0.9));draw(B--Q,red+linewidth(0.9));draw(C--R,red+linewidth(0.9));
dot(H);dot(D);dot(Ee);dot(F);dot(P,red);dot(Q,red);dot(R,red);dot(K);dot(A1);
label("$A$",A,dir(60));label("$B$",B,dir(200));label("$C$",C,dir(-20));
label("$H$",H,W);label("$D$",D,dir(-110));label("$E$",Ee,dir(40));label("$F$",F,dir(120));
label("$P$",P,W);label("$Q$",Q,SE);label("$R$",R,N);
label("$K$",K,dir(60));label("$A_1$",A1,dir(135));'''
b.add(1713347,1,r'''Let $ABC$ be an acute triangle with orthocentre $H$, and let $D$, $E$, $F$ be the midpoints of $BC$, $CA$, $AB$, respectively. A circle centred at $H$ is drawn so large that triangle $ABC$ lies in its interior. The line $EF$ meets the circle at $P$, the line $FD$ meets it at $Q$, and the line $DE$ meets it at $R$ (for each line, either of the two intersection points may be taken). Prove that $AP=BQ=CR$.''',
r'''Let $r$ be the radius of the circle and let $AA_1$, $BB_1$, $CC_1$ be the altitudes. As the triangle is acute, $H$ lies inside it, on each altitude between the vertex and the foot.
'''+asy(fig,'6.5cm')+r'''
\textbf{A formula for $AP$.} $EF$ is a midline, so $EF\parallel BC$, and therefore the altitude $AA_1$ is perpendicular to $EF$. Let $K=AA_1\cap EF$. The dilation with centre $A$ and ratio $\dfrac12$ maps $B,C$ to $F,E$ and hence $A_1$ to $K$, so $K$ is the midpoint of $AA_1$. Write $h=AA_1$ and $t=AH$, with $0<t<h$.

The points $A$, $H$, $K$ lie on a line perpendicular to line $EF$ at $K$, and $P$ lies on line $EF$. By Pythagoras in the right triangles $AKP$ and $HKP$,
\[
AP^2=AK^2+KP^2,\qquad r^2=HP^2=HK^2+KP^2 .
\]
Subtracting, and using $AK=\dfrac h2$, $HK=\left|t-\dfrac h2\right|$,
\[
AP^2=r^2+AK^2-HK^2=r^2+\dfrac{h^2}{4}-\left(t-\dfrac h2\right)^2=r^2+t(h-t)=r^2+AH\cdot HA_1 .
\]
This holds for either intersection point $P$. In the same way
\[
BQ^2=r^2+BH\cdot HB_1,\qquad CR^2=r^2+CH\cdot HC_1 .
\]

\textbf{The three products are equal.} Since $\angle AA_1B=\angle AB_1B=90^\circ$, the points $A_1$ and $B_1$ lie on the circle with diameter $AB$. The chords $AA_1$ and $BB_1$ of that circle meet at $H$, so by the power of the point $H$,
\[
AH\cdot HA_1=BH\cdot HB_1 ,
\]
and likewise $BH\cdot HB_1=CH\cdot HC_1$ (circle with diameter $BC$). Hence $AP^2=BQ^2=CR^2$, so $AP=BQ=CR$. $\blacksquare$''',
'Triangles|Altitudes|Midpoints|Power of a point|Pythagorean theorem|Circles',6,
note='RMO mock test problem. The statement is tidied ("DE intersects" read like the other two as "the line DE meets the circle"); the proof shows that AP = BQ = CR whichever intersection point is chosen on each line. Checked numerically for random acute triangles and radii.')

# ---------------- 1713302 Pythagorean triple divisible by 3
b.add(1713302,1,r'''Prove that in every Pythagorean triple (positive integers $a,b,c$ with $a^2+b^2=c^2$) at least one of the three numbers is divisible by $3$.''',
r'''Every integer is $\equiv0,1$ or $2\pmod3$, so every square is $\equiv0$ or $1\pmod3$ (as $1^2\equiv2^2\equiv1$), and a square is $\equiv0$ exactly when the number is divisible by $3$.

Suppose neither $a$ nor $b$ is divisible by $3$. Then $a^2\equiv b^2\equiv1$, so $c^2=a^2+b^2\equiv2\pmod3$, which is impossible for a square. Hence $3\mid a$ or $3\mid b$. $\blacksquare$

(In fact one of the legs is always divisible by $3$; for example $(3,4,5)$, $(5,12,13)$, $(8,15,17)$.)''',
'Pythagorean triples|Remainders and congruences|Perfect squares|Proof by contradiction',2)

# ---------------- 1713055 triangle A=60, C=45, AB=12
fig=RA+r'''real s=sqrt(3);
pair A=(0,0),C=(6+6*s,0),B=(6,6*s),Hh=(6,0);
draw(A--B--C--cycle,linewidth(0.9));
draw(B--Hh,dashed);
ra(Hh,B,C,0.6);
draw(arc(A,1.3,0,60));draw(arc(C,1.6,135,180));
label("$60^\circ$",A+2.5*dir(30));label("$45^\circ$",C+2.5*dir(157.5));
label("$A$",A,SW);label("$B$",B,N);label("$C$",C,SE);label("$H$",Hh,S);
label("$12$",(A+B)/2,NW);label("$6\sqrt6$",(B+C)/2,NE);
label("$6$",(A+Hh)/2,S);label("$6\sqrt3$",(Hh+C)/2,S);label("$6\sqrt3$",(B+Hh)/2+(0,-1.2),W);'''
b.add(1713055,1,r'''In triangle $ABC$, $\angle A=60^\circ$, $\angle C=45^\circ$ and $AB=12$. Find the perimeter of the triangle.''',
r'''Drop the altitude $BH$ to $AC$. Since $\angle A$ and $\angle C$ are acute, $H$ lies between $A$ and $C$.
'''+asy(fig,'6cm')+r'''
\begin{itemize}
\item Triangle $ABH$ is a $30^\circ$-$60^\circ$-$90^\circ$ triangle with hypotenuse $AB=12$: $AH=6$ and $BH=6\sqrt3$.
\item Triangle $BHC$ is a $45^\circ$-$45^\circ$-$90^\circ$ triangle with leg $BH=6\sqrt3$: $HC=6\sqrt3$ and $BC=6\sqrt3\cdot\sqrt2=6\sqrt6$.
\end{itemize}
So $AC=6+6\sqrt3$, $BC=6\sqrt6$, and the perimeter is
\[
12+(6+6\sqrt3)+6\sqrt6=\boxed{18+6\sqrt3+6\sqrt6}\approx43.09 .
\]''',
'Triangles|Special right triangles|Altitudes|Lengths, perimeter, and area',3)

# ---------------- 1711204 zeros of (zeros of 420!)!
b.add(1711204,1,r'''Let $z$ be the number of zeros at the end of $420!$. How many zeros are at the end of $z!$?''',
r'''The number of trailing zeros of $n!$ equals the exponent of $5$ in $n!$ (there are always more factors $2$), which by Legendre's formula is $\left\lfloor\dfrac n5\right\rfloor+\left\lfloor\dfrac n{25}\right\rfloor+\left\lfloor\dfrac n{125}\right\rfloor+\cdots$.

For $420!$: $z=84+16+3=103$.

For $103!$: $20+4=\boxed{24}$.''',
'Trailing zeros|Factorials|Floor and ceiling functions',2,
note='Near miss with aops-topic-1872176-q01 (zeros at the end of 420! only).')

# ---------------- 1698023 hexagon in circle
fig=r'''pair O=(0,0);
pair[] V;for(int i=0;i<6;++i) V.push(6*dir(60*i));
draw(circle(O,6),blue+linewidth(0.9));
draw(V[0]--V[1]--V[2]--V[3]--V[4]--V[5]--cycle,linewidth(0.9));
for(int i=0;i<6;++i) draw(O--V[i],dashed+gray);
dot(O);
label("$O$",O+(0,-1.4));
label("$6$",(V[0]+V[1])/2,dir(210));
label("$6$",(O+V[0])/2,S);'''
b.add(1698023,1,r'''A regular hexagon with area $54\sqrt3$ square inches is inscribed in a circle. What is the circumference of the circle? Express your answer in terms of $\pi$.''',
r'''The segments from the centre $O$ to the six vertices cut the hexagon into six equilateral triangles whose side $s$ equals the side of the hexagon and also the radius of the circle.
'''+asy(fig,'4.5cm')+r'''
Each triangle has area $\dfrac{\sqrt3}{4}s^2$, so
\[
6\cdot\dfrac{\sqrt3}{4}s^2=\dfrac{3\sqrt3}{2}s^2=54\sqrt3\quad\Longrightarrow\quad s^2=36,\quad s=6 .
\]
The radius is $6$ inches, so the circumference is $2\pi\cdot6=\boxed{12\pi}$ inches.''',
'Regular polygons|Circles|Equilateral triangles|Lengths, perimeter, and area',2,source=src('MATHCOUNTS',2013,'School',30,rnd='Sprint'))

# ---------------- 1712659 outfits
b.add(1712659,1,r'''A boy has $3$ pairs of trousers, $2$ jackets and $5$ shirts. How many different outfits consisting of one pair of trousers, one jacket and one shirt can he put together?''',
r'''By the multiplication principle there are $3\cdot2\cdot5=\boxed{30}$ outfits.''',
'Multiplication principle',1)

# ---------------- 1712621 triangle KLM
fig=RA+r'''real s=sqrt(3);
pair L=(0,0),M=(20*s,0),Hh=(30-10*s,0),K=(30-10*s,30-10*s);
draw(K--L--M--cycle,linewidth(0.9));
draw(K--Hh,dashed);
ra(Hh,K,M,1.4);
draw(arc(L,3.5,0,45));draw(arc(M,4.5,150,180));
label("$45^\circ$",L+5.2*dir(22.5));label("$30^\circ$",M+6.6*dir(165));draw(arc(K,2.2,degrees(L-K),degrees(M-K)+360));label("$105^\circ$",K+4.8*dir(312));
label("$K$",K,N);label("$L$",L,SW);label("$M$",M,SE);label("$H$",Hh,S);
label("$20\sqrt3$",(L+M)/2+(0,-3),S);
label("$h$",(K+Hh)/2,W);'''
b.add(1712621,1,r'''In triangle $KLM$, $LM=20\sqrt3$, $\angle K=105^\circ$ and $\angle M=30^\circ$. Find $KL$ and $KM$.''',
r'''The third angle is $\angle L=180^\circ-105^\circ-30^\circ=45^\circ$. Drop the altitude $KH=h$ to $LM$; since $\angle L$ and $\angle M$ are acute, $H$ lies between $L$ and $M$.
'''+asy(fig,'6.5cm')+r'''
\begin{itemize}
\item In the $45^\circ$-$45^\circ$-$90^\circ$ triangle $KHL$: $LH=h$ and $KL=h\sqrt2$.
\item In the $30^\circ$-$60^\circ$-$90^\circ$ triangle $KHM$: $HM=h\sqrt3$ and $KM=2h$.
\end{itemize}
So $LM=h+h\sqrt3=20\sqrt3$, giving
\[
h=\dfrac{20\sqrt3}{1+\sqrt3}=\dfrac{20\sqrt3(\sqrt3-1)}{2}=30-10\sqrt3 .
\]
Therefore
\[
\boxed{KL=h\sqrt2=30\sqrt2-10\sqrt6\approx17.93},\qquad \boxed{KM=2h=60-20\sqrt3\approx25.36}.
\]
(Check with the law of sines: $\dfrac{KL}{\sin30^\circ}=\dfrac{KM}{\sin45^\circ}=\dfrac{LM}{\sin105^\circ}\approx35.86$.)''',
'Triangles|Special right triangles|Altitudes|Rationalising denominators',3)

# ---------------- 1711916 five MATHCOUNTS-style problems
fig=r'''pair A=(0,0),B=(10,0),C=(3.6,4.8),C2=(3.6,-4.8),O=(3.6,0);
path el=shift(O)*scale(1.3,4.8)*unitcircle;
draw(subpath(el,1,3),dashed+gray);
draw(subpath(el,3,5),linewidth(0.8));
draw(A--C--B--C2--cycle,linewidth(0.9));
draw(A--B,dashed);
draw(O--C,blue+dashed);
dot(O);
label("$A$",A,W);label("$B$",B,E);label("$C$",C,N);
label("$6$",(A+C)/2,NW);label("$8$",(C+B)/2,NE);
label("$r$",(4.05,2.4),blue);
draw((0,-5.8)--(3.6,-5.8),Arrows(4));draw((3.6,-5.8)--(10,-5.8),Arrows(4));
draw((0,-5.5)--(0,-6.1));draw((3.6,-5.5)--(3.6,-6.1));draw((10,-5.5)--(10,-6.1));
label("$3.6$",(1.8,-5.8),S);label("$6.4$",(6.8,-5.8),S);'''
b.add(1711916,1,r'''A right triangle with sides $6$, $8$ and $10$ units is rotated about its side of length $10$. What is the volume of the resulting solid? Express your answer as a decimal to the nearest tenth.''',
r'''Let the triangle be $ABC$ with hypotenuse $AB=10$, $AC=6$, $BC=8$. Rotating about $AB$, the vertex $C$ traces a circle whose radius is the altitude from $C$ to $AB$:
\[
r=\dfrac{AC\cdot BC}{AB}=\dfrac{6\cdot8}{10}=4.8 .
\]
The foot of this altitude splits $AB$ into $\dfrac{6^2}{10}=3.6$ and $\dfrac{8^2}{10}=6.4$. The solid consists of two cones with common base radius $4.8$ and heights $3.6$ and $6.4$:
'''+asy(fig,'5.5cm')+r'''
\[
V=\dfrac13\pi(4.8)^2(3.6+6.4)=\dfrac13\pi\cdot23.04\cdot10=76.8\pi\approx\boxed{241.3}\text{ cubic units}.
\]''',
'Cones|Volume|Right triangles|Solid geometry',3,
note='Problem 1 of the post (a set of practice problems).')
b.add(1711916,2,r'''An eight-digit number $N$ has one digit $2$, three digits $3$, two digits $4$ and two digits $5$. If $N$ is a power of $2$, what is $N$?''',
r'''Eight-digit powers of $2$ lie between $10^7$ and $10^8$: since $2^{23}=8388608$ has seven digits and $2^{27}=134217728$ has nine, the candidates are $2^{24},2^{25},2^{26}$.

The digit sum of $N$ is $2+3\cdot3+2\cdot4+2\cdot5=29$, so $N\equiv29\equiv2\pmod9$. Powers of $2$ modulo $9$ repeat with period $6$: $2^6\equiv1$, so $2^{24}\equiv1$, $2^{25}\equiv2$, $2^{26}\equiv4\pmod9$. Only $2^{25}$ fits, and indeed
\[
N=2^{25}=\boxed{33554432},
\]
which has one $2$, three $3$'s, two $4$'s and two $5$'s.''',
'Powers of two|Digits and bases|Remainders and congruences',3,
note='Problem 2 of the post.')
b.add(1711916,3,r'''Ty flips a fair coin $20$ times. What is the probability that it lands heads up and tails up an equal number of times? Express your answer as a decimal to the nearest thousandth.''',
r'''Equal numbers means exactly $10$ heads. The probability is
\[
\dfrac{\dbinom{20}{10}}{2^{20}}=\dfrac{184756}{1048576}\approx0.17620,
\]
which rounds to $\boxed{0.176}$.''',
'Binomial probability|Probability|Combinations',2,
note='Problem 3 of the post.')
b.add(1711916,4,r'''The number $2019$ can be written as a sum of consecutive integers (positive, zero or negative) in increasing order in several ways, for example $1009+1010=2019$ and $(-2018)+(-2017)+\cdots+2018+2019=2019$. Including these two examples, in how many ways can $2019$ be written as the sum of at least two consecutive integers in increasing order?''',
r'''A run of $k\ge1$ consecutive integers starting at $a$ has sum $\dfrac{k(2a+k-1)}{2}$. So we need
\[
k(2a+k-1)=4038=2\cdot3\cdot673 .
\]
The two factors $k$ and $2a+k-1$ differ by the odd number $2a-1$, so they have opposite parity; conversely, every factorisation $4038=k\cdot m$ with $k\ge1$ and $k,m$ of opposite parity gives an integer $a=\dfrac{m-k+1}{2}$. Since $4038=2\cdot2019$ with $2019$ odd, every divisor $k$ of $4038$ works: an odd $k$ has even partner and vice versa. The divisors of $4038$ are
\[
1,2,3,6,673,1346,2019,4038 ,
\]
eight in all. The divisor $k=1$ is the one-term ``sum'' $2019$, which is not allowed. Hence there are $\boxed{7}$ ways ($k=2,3,6,673,1346,2019,4038$; for example $k=4038$ gives $-2018+\cdots+2019$ and $k=3$ gives $672+673+674$).''',
'Factors and multiples|Divisor counting|Arithmetic sequences|Parity',4,
note='Problem 4 of the post. Checked by enumerating all runs.')
fig=r'''real R=sqrt(66.25);
pair O=(0,0);
draw(circle(O,R),linewidth(0.9));
real[] y={-1.5,-3.5,-5.5};
pen cp=blue+linewidth(1);
for(int i=0;i<3;++i){real hx=sqrt(R^2-y[i]^2);draw((-hx,y[i])--(hx,y[i]),cp);}
draw(O--(0,-5.5),dashed);
draw(O--(8,-1.5),dashed+gray);draw(O--(-6,-5.5),dashed+gray);
dot(O);label("$O$",O,N);
label("$16$",(8,-1.5),E,blue);label("$k$",(sqrt(R^2-12.25),-3.5),E,blue);label("$12$",(6,-5.5),E,blue);
label("$d$",(0,-0.75),E);label("$2$",(0,-2.5),W);label("$2$",(0,-4.5),W);
label("$r$",(4,-0.75),N,gray);label("$r$",(-3,-2.75),NW,gray);'''
b.add(1711916,5,r'''Three parallel chords of a circle have lengths $12$, $k$ and $16$, and all three lie on the same side of the centre. The chord of length $k$ lies between the other two and is $2$ units from each of them. Find $k$ in simplest radical form.''',
r'''A longer chord is closer to the centre, so the chord of length $16$ is nearest the centre. Let it be at distance $d$ from the centre $O$; then the chord of length $k$ is at distance $d+2$ and the chord of length $12$ at distance $d+4$. With radius $r$, the half-chords give
\[
r^2=8^2+d^2=6^2+(d+4)^2 .
\]
So $64+d^2=36+d^2+8d+16$, hence $8d=12$, $d=\dfrac32$ and $r^2=64+\dfrac94=\dfrac{265}{4}$.
'''+asy(fig,'5cm')+r'''
For the middle chord, at distance $d+2=\dfrac72$,
\[
\left(\dfrac k2\right)^2=r^2-\left(\dfrac72\right)^2=\dfrac{265-49}{4}=54,\qquad \dfrac k2=3\sqrt6,
\]
so $k=\boxed{6\sqrt6}\approx14.7$.''',
'Circles|Arcs and chords|Pythagorean theorem',3,
note='Problem 5 of the post. The picture was not provided; the post describes it (all three chords on the same side of the centre, the chord of length k in the middle).')

# ---------------- 1712099 N^2-71 divisible by 7N+55
b.add(1712099,1,r'''Find all integers $N$ such that $N^2-71$ is divisible by $7N+55$.''',
r'''Let $d=7N+55$ (note $d\ne0$, as $7\nmid55$). If $d\mid N^2-71$, then $d\mid49(N^2-71)$. Since
\[
49(N^2-71)=49N^2-3479=(7N+55)(7N-55)-454 ,
\]
it follows that $d\mid454=2\cdot227$. So $7N+55\in\{\pm1,\pm2,\pm227,\pm454\}$, i.e.\ $7N\in\{-54,-56,-53,-57,172,-282,399,-509\}$. Only $-56$ and $399$ are multiples of $7$, giving $N=-8$ and $N=57$.

Check: for $N=-8$, $7N+55=-1$ divides everything ($N^2-71=-7$). For $N=57$, $7N+55=454$ and $N^2-71=3178=7\cdot454$.

The answers are $\boxed{N=-8\ \text{and}\ N=57}$.''',
'Divisibility|Diophantine equations|Factors and multiples',4,
note='Source given only as "BC Exam"; not recorded as a contest source. Checked by search over |N| <= 10^5.')

# ---------------- 1712340 product of ten integers
b.add(1712340,1,r'''Ten different integers from $1$ to $20$ inclusive have product $7.783776\cdot10^{10}$. What is their sum?''',
r'''The product is $P=77837760000=2^9\cdot3^5\cdot5^4\cdot7\cdot11\cdot13$ (divide out $10^4$ to get $7783776=2^5\cdot3^5\cdot7\cdot11\cdot13$).
\begin{itemize}
\item $17,19\nmid P$, so $17$ and $19$ are not used. The only multiples of $11$ and $13$ up to $20$ are $11$ and $13$, so both are used.
\item The multiples of $5$ are $5,10,15,20$, each contributing exactly one factor $5$; to reach $5^4$ all four are used.
\item The multiples of $7$ are $7$ and $14$; exactly one of them is used.
\end{itemize}
Now $5\cdot10\cdot15\cdot20=2^3\cdot3\cdot5^4$, so the remaining three numbers, chosen from $\{1,2,3,4,6,8,9,12,16,18\}$, must have product $2^6\cdot3^4$ (if $7$ is used) or $2^5\cdot3^4$ (if $14$ is used). Each of these numbers contains at most $3^2$, so the exponent $4$ of $3$ arises either as $2+2+0$ or as $2+1+1$.
\begin{itemize}
\item $2+1+1$: one of $9,18$ and two of $3,6,12$. The power of $2$ in such a product is at most $2^{1+1+2}=2^4$, too small.
\item $2+2+0$: the numbers $9$ and $18$ (product $2\cdot3^4$) and a power of $2$, which must be $2^5=32$ (too big) or $2^4=16$ (with $14$).
\end{itemize}
Hence the numbers are
\[
5,9,10,11,13,14,15,16,18,20 ,
\]
and their sum is $\boxed{131}$.''',
'Prime factorisation|Factors and multiples|Casework',4,
note='The ten integers are taken to be distinct. The factorisation and the uniqueness of the set were checked by searching all 10-element subsets of {1,...,20}.')

# ---------------- 1690790 last 3 digits of 1^300...5^300
b.add(1690790,1,r'''What are the last three digits of $1^{300}\cdot2^{300}\cdot3^{300}\cdot4^{300}\cdot5^{300}$?''',
r'''The product is $(1\cdot2\cdot3\cdot4\cdot5)^{300}=120^{300}$. Since $120$ is divisible by $10$, $120^{300}$ is divisible by $10^{300}$, in particular by $1000$. The last three digits are $\boxed{000}$.''',
'Units digits and last digits|Exponents|Factorials',1,
note='Near miss with aops-topic-1787633-q01 (last two nonzero digits of 1^100 2^200 3^300 4^400 5^500).')

# ---------------- 1711274 n^4-n^3+n^2-n even
b.add(1711274,1,r'''Show that $n^4-n^3+n^2-n$ is divisible by $2$ for every integer $n$.''',
r'''Factor by grouping:
\[
n^4-n^3+n^2-n=n^3(n-1)+n(n-1)=n(n-1)(n^2+1).
\]
Among the consecutive integers $n-1$ and $n$, one is even, so the product $n(n-1)$, and hence the whole expression, is divisible by $2$. $\blacksquare$''',
'Parity|Factoring|Divisibility',1)

# ---------------- 1711594 7000-9000 digit sums
b.add(1711594,1,r'''How many four-digit integers between $7000$ and $9000$ have the property that the thousands digit equals the sum of the other three digits?''',
r'''The thousands digit is $7$ or $8$ ($9000$ does not have the property).
\begin{itemize}
\item Thousands digit $7$: the other digits $a,b,c\ge0$ satisfy $a+b+c=7$; each is automatically at most $9$. Stars and bars gives $\dbinom{9}{2}=36$.
\item Thousands digit $8$: $a+b+c=8$, giving $\dbinom{10}{2}=45$.
\end{itemize}
The total is $36+45=\boxed{81}$.''',
'Stars and bars|Digit problems|Distributions and integer solutions',3)

# ---------------- 1711919 centroid, incentre, orthocentre
fig=r'''pair B=(0,0),C=(21,0),A=(6,8);
pair G=(A+B+C)/3,I=(7,3.5),H=(6,11.25);
pair fb=A+dot(B-A,unit(C-A))*unit(C-A),fc=A+dot(C-A,unit(B-A))*unit(B-A);
draw(A--fb,dotted+gray);draw(A--fc,dotted+gray);
draw(circle(I,3.5),heavygreen);
draw(A--(B+C)/2,blue+dashed);draw(B--(C+A)/2,blue+dashed);draw(C--(A+B)/2,blue+dashed);
draw(A--(6,0),red+dashed);draw(A--H,red+dashed);draw(B--H,red+dashed);draw(C--H,red+dashed);
draw(A--B--C--cycle,linewidth(0.9));
dot(G,blue);dot(I,heavygreen);dot(H,red);
label("$A$",A,1.6*W);label("$B$",B,SW);label("$C$",C,SE);
label("$G$",G,dir(65),blue);label("$I$",I,N,heavygreen);label("$H$",H,N,red);'''
b.add(1711919,1,r'''Explain the difference between the centroid, the incentre and the orthocentre of a triangle by stating how each is defined. Then find all three for the triangle with vertices $A(6,8)$, $B(0,0)$ and $C(21,0)$.''',
r'''\textbf{Definitions.}
\begin{itemize}
\item The \emph{centroid} $G$ is the common point of the three medians (segments from a vertex to the midpoint of the opposite side). It divides each median in the ratio $2:1$ from the vertex, and its coordinates are the averages of the vertices' coordinates.
\item The \emph{incentre} $I$ is the common point of the three angle bisectors. It is equidistant from the three sides and is the centre of the inscribed circle. With side lengths $a=BC$, $b=CA$, $c=AB$, it is $I=\dfrac{aA+bB+cC}{a+b+c}$.
\item The \emph{orthocentre} $H$ is the common point of the three altitudes (lines through a vertex perpendicular to the opposite side). It lies inside an acute triangle, at the right-angle vertex of a right triangle, and outside an obtuse triangle.
\end{itemize}
The centroid and incentre are always inside the triangle; the three points coincide only for an equilateral triangle.

\textbf{The example.} Here $a=BC=21$, $b=CA=\sqrt{15^2+8^2}=17$, $c=AB=\sqrt{6^2+8^2}=10$.
\begin{itemize}
\item $G=\left(\dfrac{6+0+21}{3},\dfrac{8+0+0}{3}\right)=\boxed{\left(9,\dfrac83\right)}$.
\item $I=\dfrac{21(6,8)+17(0,0)+10(21,0)}{48}=\left(\dfrac{336}{48},\dfrac{168}{48}\right)=\boxed{\left(7,\dfrac72\right)}$. Check: the area is $\dfrac12\cdot21\cdot8=84$ and the semiperimeter $24$, so the inradius is $\dfrac{84}{24}=\dfrac72$, the height of $I$ above $BC$.
\item The altitude from $A$ is the line $x=6$. The altitude from $C$ is perpendicular to $AB$, whose direction is $(6,8)$: it is $6(x-21)+8y=0$. At $x=6$: $8y=90$, $y=\dfrac{45}{4}$. So $H=\boxed{\left(6,\dfrac{45}{4}\right)}$; it lies outside the triangle because the angle at $A$ is obtuse ($AB^2+AC^2=389<441=BC^2$). (The altitude from $B$, perpendicular to $AC$, is $15x-8y=0$, which also passes through $H$.)
\end{itemize}
In the sketch, the medians are blue, the altitudes red (with the sides $AB$, $AC$ extended, dotted, to the feet of the altitudes from $C$ and $B$), and the incircle green.
'''+asy(fig,'7cm'),
'Medians and centroids|Incircles and incentres|Altitudes|Angle bisectors|Coordinate geometry',3,
note='The post asks what the difference between centroids, incenters and orthocenters is; turned into definitions plus a computation for a specific obtuse triangle.')

# ---------------- 1712197 ordered triples
b.add(1712197,1,r'''How many ordered triples of positive integers $(e,f,g)$ satisfy
\[
(ge-fe)\left(\dfrac ge+\dfrac fe\right)\equiv e^2\pmod{(e+f+g)^2}\ ?
\]
Prove your answer.''',
r'''First simplify the left side: $(ge-fe)\left(\dfrac ge+\dfrac fe\right)=e(g-f)\cdot\dfrac{g+f}{e}=g^2-f^2$, an integer. So the condition says
\[
(e+f+g)^2\ \Big|\ g^2-f^2-e^2 .
\]
Let $M=(e+f+g)^2$. Then $0<g^2<M$ and $0<e^2+f^2<M$, so $g^2-(e^2+f^2)$ is the difference of two numbers in the interval $(0,M)$ and has absolute value less than $M$. The only multiple of $M$ in that range is $0$. Hence the condition holds exactly when
\[
e^2+f^2=g^2 ,
\]
i.e.\ when $(e,f,g)$ is a Pythagorean triple with hypotenuse $g$. There are infinitely many such triples, for example $(3k,4k,5k)$ for every positive integer $k$. So there are $\boxed{\text{infinitely many}}$ ordered triples.''',
'Pythagorean triples|Remainders and congruences|Bounding and extremal cases',4,
note='Checked by search for e, f, g <= 60: the solutions are exactly the triples with e^2 + f^2 = g^2.')

# ---------------- 1648327 nested radical
b.add(1648327,1,r'''Assume the infinite expression
\[
x=\sqrt{\dfrac{\sqrt{\dfrac{\sqrt{\dfrac{\sqrt{\cdots}}{\sqrt{\cdots}}}}{\sqrt{\dfrac{\sqrt{\cdots}}{\sqrt{\cdots}}}}}}{\sqrt{\dfrac{\sqrt{\dfrac{\sqrt{\cdots}}{\sqrt{\cdots}}}}{\sqrt{\dfrac{\sqrt{\cdots}}{\sqrt{\cdots}}}}}}}
\]
has a positive real value $x$, where every numerator and every denominator under a fraction bar is again a copy of the whole expression. Find $x$.''',
r'''The expression is $\sqrt{\dfrac{Y}{Z}}$, where the numerator $Y$ and the denominator $Z$ are copies of the whole expression, so $Y=Z=x$. Hence
\[
x=\sqrt{\dfrac xx}=\sqrt1=\boxed{1}.
\]
(The value is forced once a positive value is assumed; and $x=1$ is consistent, since every finite truncation in which the innermost entries are replaced by $1$ also equals $1$.)''',
'Radicals|Substitution',1,
note='Joke-style self-similar expression; the reading that each numerator and denominator is a copy of the whole expression, with a positive value, is stated.')

# ---------------- 1712010 shifting an ellipse
fig=r'''import graph;
draw((-4.2,0)--(6,0),gray,Arrow(5));draw((0,-5.8)--(0,2.8),gray,Arrow(5));
label("$x$",(6,0),N,gray);label("$y$",(0,2.8),E,gray);
for(int i=-3;i<=5;++i) if(i!=0) {draw((i,-0.1)--(i,0.1),gray);}
for(int j=-5;j<=2;++j) if(j!=0) {draw((-0.1,j)--(0.1,j),gray);}
draw(scale(3,2)*unitcircle,dashed+gray);
pair c=(2,-3);
draw(shift(c)*scale(3,2)*unitcircle,blue+linewidth(1));
draw((0,0)--c,red,Arrow(6));
dot(c,blue);
draw(c--c+(3,0),dashed);draw(c--c+(0,2),dashed);
label("$3$",c+(1.5,0),N);label("$2$",c+(0,1),E);
label("$(2,-3)$",c,S,blue);
label("$O$",(0,0),dir(135));'''
b.add(1712010,1,r'''For positive constants $a,b,c$, the graph of $ax^2+by^2=c$ is an ellipse centred at the origin.
\begin{enumerate}
\item[(a)] How should the equation be changed to move the ellipse, without changing its shape, so that its centre is the point $(h,k)$?
\item[(b)] Find the centre and the lengths of the semi-axes of the ellipse $4x^2+9y^2-16x+54y+61=0$.
\end{enumerate}''',
r'''\textbf{(a)} Translating a graph by $h$ to the right and $k$ upward replaces $x$ by $x-h$ and $y$ by $y-k$: a point $(x,y)$ lies on the moved curve exactly when $(x-h,y-k)$ lies on the original one. So the new equation is
\[
\boxed{a(x-h)^2+b(y-k)^2=c}.
\]

\textbf{(b)} Complete the squares:
\[
4(x^2-4x)+9(y^2+6y)=-61\ \Longrightarrow\ 4(x-2)^2-16+9(y+3)^2-81=-61\ \Longrightarrow\ 4(x-2)^2+9(y+3)^2=36 ,
\]
that is,
\[
\dfrac{(x-2)^2}{9}+\dfrac{(y+3)^2}{4}=1 .
\]
This is the ellipse $4x^2+9y^2=36$ (dashed in the sketch) moved $2$ units right and $3$ units down. Its centre is $\boxed{(2,-3)}$, with horizontal semi-axis $\boxed{3}$ and vertical semi-axis $\boxed{2}$.
'''+asy(fig,'5.5cm'),
'Ellipses|Conic sections|Translations|Completing the square|Coordinate geometry',3,
note='The post asks how to shift the centre of an ellipse ax^2+by^2=c; part (b) was added as a concrete exercise.')

# ---------------- 1711366 Frank and Usain
b.add(1711366,1,r'''Frank and Usain start together at the same point of a circular track one mile long and run in opposite directions, Frank at $12$ miles per hour and Usain at $22$ miles per hour. After how long do they first meet?''',
r'''Running in opposite directions, they approach each other along the track at the combined speed $12+22=34$ miles per hour, and they meet for the first time when together they have covered the full lap of $1$ mile. This takes
\[
\dfrac{1}{34}\text{ hour}=\dfrac{60}{34}\text{ min}=\boxed{\dfrac{30}{17}\text{ minutes}}\approx1\text{ min }46\text{ s}.
\]
(The same time results if they start at the two ends of a straight one-mile course and run towards each other.)''',
'Relative speed|Distance, rate, and time',2,
note='The post only says "a mile race ... in opposite directions"; read as a one-mile circular track with a common start (equivalently, the two ends of a one-mile course running towards each other).')

# ---------------- 1711063 easy summation
b.add(1711063,1,r'''What is the value of
\[
\sum_{n=3}^{10}\dfrac{n^4+2n^3-7n^2-8n+12}{4\dbinom{n-1}{2}}\ ?
\]''',
r'''The numerator vanishes at $n=1,2,-2,-3$, and indeed
\[
n^4+2n^3-7n^2-8n+12=(n-1)(n-2)(n+2)(n+3)
\]
(multiply $(n^2-3n+2)(n^2+5n+6)$ to check). The denominator is $4\cdot\dfrac{(n-1)(n-2)}{2}=2(n-1)(n-2)$. So for $n\ge3$ each term is
\[
\dfrac{(n+2)(n+3)}{2}=\dbinom{n+3}{2}.
\]
By the hockey-stick identity,
\[
\sum_{n=3}^{10}\dbinom{n+3}{2}=\sum_{m=6}^{13}\dbinom m2=\dbinom{14}{3}-\dbinom{6}{3}=364-20=\boxed{344}.
\]''',
'Factoring|Polynomials|Combinatorial identities and binomial coefficients|Summation',4)

# ---------------- 1711299 primes differing by 7
b.add(1711299,1,r'''Prove that there is no pair of prime numbers whose difference is $7$.''',
r'''Suppose $p$ and $q$ are primes with $p-q=7$. Since $7$ is odd, $p$ and $q$ have different parity, so one of them is even. The only even prime is $2$, and as $p>q$, we get $q=2$ and $p=9$. But $9=3\cdot3$ is not prime. Hence no two primes differ by $7$. $\blacksquare$''',
'Prime numbers|Parity|Proof by contradiction',2)

# ---------------- 1710875 sum and difference of cubes
b.add(1710875,1,r'''Show how one can discover the factorisations
\[
x^3-y^3=(x-y)(x^2+xy+y^2)\qquad\text{and}\qquad x^3+y^3=(x+y)(x^2-xy+y^2)
\]
without knowing them in advance.''',
r'''\textbf{Finding a factor.} Regard $x^3-y^3$ as a polynomial in $x$ (with $y$ a constant). It vanishes at $x=y$, so by the factor theorem $x-y$ is a factor. Likewise $x^3+y^3$ vanishes at $x=-y$, so $x+y$ is a factor.

\textbf{Finding the other factor.} The quotient has degree $2$ in $x$ and is homogeneous of degree $2$, so it is $x^2+pxy+y^2$ (comparing the $x^3$ and $y^3$ coefficients). Expanding,
\[
(x-y)(x^2+pxy+y^2)=x^3+(p-1)x^2y+(1-p)xy^2-y^3 ,
\]
which equals $x^3-y^3$ exactly when $p=1$. Hence
\[
x^3-y^3=(x-y)(x^2+xy+y^2).
\]
(This is also the finite geometric series idea: $(x-y)(x^2+xy+y^2)=x^3+x^2y+xy^2-x^2y-xy^2-y^3$ telescopes.)

\textbf{The sum.} Replace $y$ by $-y$ in the identity just proved:
\[
x^3+y^3=x^3-(-y)^3=(x+y)\bigl(x^2-xy+y^2\bigr). \qquad\blacksquare
\]''',
'Sum and difference of cubes|Factoring|Remainder theorem and factor theorem|Polynomials',2,
note='The post lists the second formula as x^3 + y^3 = (x - y)(x^2 + xy + y^2), a typo for x^3 - y^3; the record states both formulas correctly.')

b.save()
