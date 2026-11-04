import math, itertools, random, cmath
from fractions import Fraction as F
from collections import Counter
import numpy as np
import sympy as sp
# 1754152
pr=[p for p in range(10,100) if all(p%d for d in range(2,10) if d<p)]
S=[x+y for x in pr for y in pr if x<y and x//10==y//10 and (x*x+y*y)%10==0]; assert min(S)==24 and max(S)==172
# 1754045
assert all(a*(a*a+23)%24==0 for a in range(-500,500) if a%2 and a%3)
# 1753689
xs=[math.sqrt(2),-math.sqrt(2),2*math.sqrt(2),-2*math.sqrt(2)]
assert all(abs(x**4+16-10*x*x)<1e-9 for x in xs)
pq={round(p*q,9) for p,q in itertools.combinations(xs,2) if p*q>0}; assert pq=={4.0}
# 1753987
h=5*4**(1/3); assert abs((h/10)**3-0.5)<1e-12 and abs(h-7.937)<1e-3
# 1751624
d=lambda a: cmath.exp(1j*math.radians(a))
t=np.linalg.solve(np.array([[d(10).real,-d(160).real],[d(10).imag,-d(160).imag]]),np.array([1,0]))
D=t[0]*d(10); A=0;B=1;C=d(60)
ang=lambda P,Q,R: math.degrees(abs(cmath.phase((P-Q)/(R-Q))))
x=ang(A,C,D); assert abs(ang(D,B,A)-20)<1e-9 and abs(ang(D,A,B)-10)<1e-9
s20,c20=math.sin(math.radians(20)),math.cos(math.radians(20))
assert abs(math.tan(math.radians(x))-(math.sqrt(3)-2*s20)/(3-2*c20))<1e-12 and abs(x-43.08)<0.01
assert abs(abs(D)-2*s20)<1e-12   # AD = 2 sin 20
# D inside triangle
assert 0<D.imag and (D-B).imag/(1) >0
# 1753684
b_=73; assert (180-34)/2==73 and 180-17-36.5==126.5
P=(0,2*math.tan(math.radians(b_/2))); Ap=(0,2*math.tan(math.radians(b_))); Cp=(2,0)
v1=np.subtract(Ap,P);v2=np.subtract(Cp,P); assert abs(math.degrees(math.acos(v1@v2/np.linalg.norm(v1)/np.linalg.norm(v2)))-126.5)<1e-9
assert sum(1 for p in itertools.permutations('MFabc') if abs(p.index('M')-p.index('F'))==1)==48
# 1753584
assert abs(F(120,360)*36-12)<1e-12 and abs(0.5*36*math.sin(math.radians(120))-9*math.sqrt(3))<1e-12
# 1753554
assert 5*63+25*24==915 and F(63,90)+F(24,80)==1
# 1753532
V=[cmath.exp(1j*math.pi*k/3) for k in range(6)]
shapes=Counter(tuple(sorted(round(abs(V[a]-V[b]),6) for a,b in itertools.combinations(c,2))) for c in itertools.combinations(range(6),3))
assert sum(shapes.values())==20 and len(shapes)==3 and sorted(shapes.values())==[2,6,12]
# 1750843 q01
x_=sp.symbols('x')
for n in range(1,31):
    f=sum((k+1)*x_**(n-k) for k in range(n+1))
    assert sp.expand((x_-1)**2*f-(x_**(n+2)-(n+2)*x_+(n+1)))==0
    nreal=len([r for r in sp.Poly(f,x_).nroots() if abs(sp.im(r))<1e-9])
    assert (nreal>0)==(n%2==1)
# q02
fq=x_**4-2*x_**3+6*x_**2-10*x_+7
assert sp.expand((x_-1)**2*(x_**2+5)+2-fq)==0 and fq.subs(x_,1)==2 and sp.diff(fq,x_).subs(x_,1)==0
assert 7-1==6 and -2-(-10)==8
# q03
assert sp.simplify((x_-1)*(x_-2)*(x_-3)/x_-(x_**2-6*x_+11-6/x_))==0
# q04
assert sum(F(2,k*(k+1)) for k in range(1,21))==F(40,21) and 20*21//2==210
# 1753098 lines through n centres
def lines(n):
    pts=set(itertools.product(range(n),repeat=3)); cnt=0
    dirs=[v for v in itertools.product((-1,0,1),repeat=3) if v!=(0,0,0)]
    for p in pts:
        for v in dirs:
            prev=tuple(p[i]-v[i] for i in range(3))
            if prev in pts: continue
            L=[tuple(p[i]+k*v[i] for i in range(3)) for k in range(n)]
            nxt=tuple(p[i]+n*v[i] for i in range(3))
            if all(q in pts for q in L) and nxt not in pts: cnt+=1
    return cnt//2
for n in range(1,7): assert lines(n)==((n+2)**3-n**3)//2
assert lines(4)==76 and ((12)**3-1000)//2==364
# 1753197
pr_=1
for k in range(1,2019):
    if k%2 and k%10!=5: pr_=pr_*k%10
assert pr_==9
# 1753183
assert len(str(2**2018*5**1918))==1949 and len(str(2**100))==31 and 1.07**5<1.5
# 1753196
assert sum(1 for n in range(10000,100000) if (lambda p:p and p%2==0)(math.prod(int(c) for c in str(n))))==55924
# 1752547
def bc(t):
    w=(t*(1-t),t*t,(1-t)**2); s=sum(w); return [u/s for u in w]
for t in (F(1,3),F(2,3)): assert bc(t)[0]==F(2,7)
# coordinate check
A=np.array([0,4*math.sqrt(3)]);B=np.array([-4,0.]);C=np.array([4,0.])
def ext(P1,P2,P3,P4):
    M=np.array([P2-P1,P3-P4]).T; s=np.linalg.solve(M,P3-P1); return P1+s[0]*(P2-P1)
ar=lambda P,Q,R: abs((Q-P)[0]*(R-P)[1]-(Q-P)[1]*(R-P)[0])/2
for t,rat in ((1/3,2),(2/3,0.5)):
    D=A+t*(B-A);Ep=C+t*(A-C);Fp=ext(B,Ep,C,D); assert abs(ar(B,C,Fp)/ar(A,B,C)-2/7)<1e-12 and abs((1-t)/t-rat)<1e-12
# 1753103
assert sum(1 for t in range(1,10) for u in range(10) if u%t==0)==32
assert F(sum(1 for c in itertools.product(range(4),repeat=4) if max(Counter(c).values())<=2),256)==F(51,64)
comps=[c for c in itertools.product(range(5),repeat=4) if sum(c)==4]; assert len(comps)==35 and F(sum(1 for c in comps if max(c)<=2),35)==F(19,35)
# 1753130
assert F(3,2)**2==F(9,4)
# 1752932
fx=lambda x:-4*(x+2)**2-5; assert fx(-4)==-21 and fx(-2)==-5
# 1752848
N=next(n for n in range(1,10000) if n%5==4 and n%6==5 and n%7==6 and n%8==7); assert N==839
# 1752498
assert 2**18+1==5*13*37*109==65*4033==545*481 and all(sp.isprime(p) for p in (5,13,37,109))
