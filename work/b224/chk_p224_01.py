import math, itertools, random
from fractions import Fraction as F
from math import comb, perm, factorial
import numpy as np
random.seed(1)
# 1772698 P1-P9
P=list(itertools.permutations(range(6)))
assert sum(abs(p.index(0)-p.index(1))==1 for p in P)==240
assert sum(abs(p.index(0)-p.index(2))!=1 for p in P)==480
assert sum(abs(p.index(0)-p.index(1))<=3 for p in P)==576
assert F(sum(p.index(0)<p.index(1)<p.index(2) for p in P),720)==F(1,6)
assert 500-99>=1 and 500+99<=1000 and (99%2==1)
# P6: guard knows -> 999/1000; random -> 1/2
assert F(999,1000)==1-F(1,1000) and F(1,1000)/(F(1,1000)+F(999,1000)*F(1,999))==F(1,2)
Q=list(itertools.permutations(range(9)))
g7=sum(1 for q in Q if list(q[0::2])==sorted(q[0::2]) and list(q[1::2])==sorted(q[1::2]))
assert F(g7,len(Q))==F(1,2880)
g8=sum(1 for q in Q if list(q[:5])==sorted(q[:5]) and list(q[4:])==sorted(q[4:],reverse=True))
assert F(g8,len(Q))==F(1,5184)
assert F(6*perm(22,5),perm(26,9))==F(1,59800)
# 1772054
pts=[(i,j) for i in range(3) for j in range(3)];c=0
for a,b,cc in itertools.combinations(pts,3):
    if (b[0]-a[0])*(cc[1]-a[1])-(b[1]-a[1])*(cc[0]-a[0])==0: continue
    if 2 in [(p[0]-q[0])**2+(p[1]-q[1])**2 for p,q in [(a,b),(b,cc),(a,cc)]]: c+=1
assert c==44
# 1772017 keystrokes
reps=[(int(''.join(t)),L) for L in range(1,5) for t in itertools.product('12',repeat=L)]
dp=[10**9]*2020; dp[0]=-1
for n in range(1,2020):
    for v,L in reps:
        if v<=n: dp[n]=min(dp[n],dp[n-v]+L+1)
assert dp[27]==8 and dp[2019]==23
assert 1222+222+222+221+121+11==2019
# 1771914 hexagon
s3=math.sqrt(3); V=[(0,1),(0,3),(s3,4),(2*s3,3),(2*s3,1),(s3,0)]
for i in range(6): assert abs(math.dist(V[i],V[(i+1)%6])-2)<1e-12
cx=sum(p[0] for p in V)/6; cy=sum(p[1] for p in V)/6
assert abs(cx-s3)<1e-12 and abs(cy-2)<1e-12 and abs(cy/cx-2*s3/3)<1e-12
# 1772385
best=-1e9
for y in np.linspace(0,5.99999,20001):
    best=max(best,5*y-(12-3*y)/2)
assert best<33 and 2*(-2.5)+3*5.9>12 and abs(5*5.9+2.5-32)<1e-12
# 1772376
vals={a+2*b+6*c+24*d for a in range(2) for b in range(3) for c in range(4) for d in range(5)}
assert vals==set(range(120))
# 1770315
assert {(n*n+2*n)%10 for n in range(-200,200) if (n*n+2*n)%4==0}=={0,4,8}
# 1772315
assert [F(80,2**x) for x in range(1,6)]==[40,20,10,5,F(5,2)]
# 1772119 mangoes
p=9; assert F(144,F(144,p)+2)==p-1 and 144//p==16
# 1771773 George
import sympy as sp
pp=sp.symbols('p0:6')
eq=[sp.Eq(pp[0],0),sp.Eq(pp[5],1)]+[sp.Eq(pp[n],sp.Rational(1,n+1)*pp[n+1]+sp.Rational(n,n+1)*pp[n-1]) for n in range(1,5)]
assert sp.solve(eq,pp)[pp[2]]==sp.Rational(1,17)
# 1772123 factorial base
def fb(n):
    d=[];i=2
    while n: d.append(n%i); n//=i; i+=1
    return d
N=sum(n for n in range(1,721) if 0 in fb(n)); assert N==205311 and N%720==111
# 1772214
assert abs(1.1*1.1-1.21)<1e-12 and F(11,9)-1==F(2,9)
# 1771928 tokens
a=sp.symbols('a0:5'); bb=sp.symbols('b0:5'); eqs=[sp.Eq(a[0],1),sp.Eq(bb[0],1),sp.Eq(a[4],0),sp.Eq(bb[4],0)]
for k in range(1,4):
    eqs+=[sp.Eq(a[k],(bb[k]+bb[k-1])/2),sp.Eq(bb[k],(a[k]+a[k+1])/2)]
assert sp.solve(eqs,list(a)+list(bb))[a[2]]==sp.Rational(4,7)
# 1772188
assert len(set(itertools.permutations('ELECTRICITY',5)))==8220==2520+4800+900
# 1772117
V_=60; R=F(2*V_,3)-(F(V_,3)-1); assert R==21 and R-(R/3-1)==15
# 1772122
from functools import lru_cache
@lru_cache(None)
def f(n,k):
    if k==0: return int(n==1)
    return sum(f(n//d,k-1) for d in range(1,27) if n%d==0)
assert f(32032,6)==11880 and 32032==2**5*7*11*13
# 1771925 Xavier
terms=[1]; prods={1}
while True:
    n=1
    while n in prods: n+=1
    terms.append(n); prods|={q*n for q in prods if q*n<=5000}
    if n>1000: break
comp=[t for t in terms if t>1 and any(t%d==0 for d in range(2,int(t**.5)+1))]
assert len(comp)==15 and terms[-1]==1009
# 1772052
x=math.sqrt(2)
for _ in range(100): x=math.sqrt(2-x)
assert abs(x-1)<1e-12
# 1771980
for nums in itertools.combinations(range(1,40),4):
    assert any((u*u-v*v)%5==0 or (u*u+v*v)%5==0 for u,v in itertools.combinations(nums,2))
# 1771791 frustum: min over tangent+arc vs straight
assert abs(math.dist((3,0),(6*math.cos(2*math.pi/3),6*math.sin(2*math.pi/3)))-math.sqrt(63))<1e-12
# numeric shortest path in annulus 3<=r<=6, angle 120 deg: discretised polar paths r(t)
best=1e9
for rmin_t in np.linspace(0.0,1.0,201):
    pass
# path: from B (r=6, phi=0) straight to tangent point then arc: compare with paths via any point on inner circle
def plen(phi):  # straight from B to inner point at angle phi (must not cross inner disc), then arc to A at 120deg
    P=np.array([3*math.cos(phi),3*math.sin(phi)]); Bp=np.array([6.0,0.0])
    d=P-Bp; t=-(Bp@d)/(d@d)
    if 0<t<1 and np.linalg.norm(Bp+t*d)<3-1e-9: return 1e9
    return np.linalg.norm(d)+3*(2*math.pi/3-phi)
best=min(plen(ph) for ph in np.linspace(0,2*math.pi/3,20001))
assert abs(best-(3*math.sqrt(3)+math.pi))<1e-6
assert 9*math.sqrt(3)/math.sqrt(63)<3
# 1771889
assert factorial(52)//factorial(13)**4==53644737765488792839237440000==comb(52,13)*comb(39,13)*comb(26,13)
# 1771651
assert round(3*math.sin(math.radians(40)),1)==1.9
for xx in [-3,0,2.5,7]: assert abs(abs((xx-2)-1)-1-(abs(xx-3)-1))<1e-12
# 1771487
X,Y=sp.symbols('X Y'); assert sp.Poly(sp.expand((2*X**2+8*Y**7)**5)).eval({X:1,Y:1})==100000
# 1771314: 7-colouring labels of hex lattice: neighbours all distinct
for (da,db) in [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)]: pass
diffs={(da+3*db)%7 for (da,db) in [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)]}
assert diffs=={1,2,3,4,5,6} and (7+0)%7==0 and (-3+3*1)%7==0
# 1771480
assert sum(1 for t in itertools.product(range(5),repeat=6) if (t[0]-t[3])**2+(t[1]-t[4])**2+(t[2]-t[5])**2==1)==600
# 1771161
P_=1
for n in range(10,100):
    if n%2 and n%5: P_=P_*n%100
assert P_==9 and pow(11,9,100)==91
# 1770283
assert 12**2+81==(27-12)**2
# 1771063
xs=sp.symbols('xs'); assert sp.expand((3*xs-2)*(xs+3)*(xs**2-4*xs+5)-(3*xs**4-5*xs**3-19*xs**2+59*xs-30))==0
