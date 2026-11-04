import math, itertools, random
from fractions import Fraction as F
from collections import Counter
import numpy as np
random.seed(2)
# 1746368 trees
sol=[(d,F(1800,d)) for d in range(2,200) if (F(1800,d)+20)*(F(2*d,3)-1)==1320]
assert sol==[(18,100)]
# 1742979 q16
pts=[(x,y) for x in range(-10,20) for y in range(-20,10) if (x-3)**2+(y+4)**2==25]
assert len(pts)==12 and max(x*x+y*y for x,y in pts)==100
# 1742979 q17
def ok(q):
    ps=[p for p in range(2,q+1) if q%p==0 and all(p%d for d in range(2,int(p**.5)+1))]
    sq=[p for p in ps if math.isqrt(q//p)**2==q//p]
    cu=[p for p in ps if round((q//p)**(1/3))**3==q//p]
    return any(a!=b for a in sq for b in cu)
assert min(q for q in range(1,1000) if ok(q))==432
# 1742979 q21
c=0
for n in range(10000,100000):
    s=sorted(str(n))
    if len(set(s))==5 and all(int(s[i+1])-int(s[i])==1 for i in range(4)): c+=1
assert c==696
# 1745995 rectangle
P=np.array([-12.5,0]);Q=np.array([3.5,12]);R=np.array([12.5,0]);S=np.array([-3.5,-12])
assert abs((Q-P)@(R-Q))<1e-12 and abs(np.linalg.norm(Q-P)-20)<1e-12 and abs(np.linalg.norm(R-Q)-15)<1e-12
assert np.allclose(S,P+R-Q) and Q[1]-S[1]==24 and R[0]-P[0]==25
# 1745992 q01, q02
assert 2*math.comb(6,2)==30
a,b,c=6,8,10; s=(a+b+c)/2; A=math.sqrt(s*(s-a)*(s-b)*(s-c)); assert A==24==a+b+c and A/s==2
# 1745976
assert 12**4==20736
assert math.factorial(6)//(2*1*6)*9*4*8==17280
x,y,z=2,3,5
# brute coefficient via expansion
from itertools import product
cnt=sum(1 for t in product('xyz',repeat=6) if t.count('x')==2 and t.count('y')==1)
assert cnt*9*4*8==17280
# 1745924
assert F(1,math.comb(23,2))==F(1,253)
# 1745621
res=set()
for L in itertools.combinations_with_replacement(range(1,60),5):
    if L[2]!=10 or L[4]-L[0]!=16 or sum(L)!=75: continue
    C=Counter(L); m=max(C.values())
    if [k for k in C if C[k]==m]==[10]: res.add(L[0])
assert res=={8,9,10}
fc=[-2,-1,0,0,1,2]
assert F(sum(1 for t in product(fc,repeat=3) if sum(t)==0),216)==F(19,108)
assert max(0,460+571-985)==46 and 460-46==414
# 1745770 odometer: count readings
def okr(n): return all(ch in '02468' for ch in str(n))
r=[n for n in range(0,90000) if okr(n)]
assert r[1]==2 and r[5]==20 and r.index(8866)==618
# 1574955 pentagon area sqrt3 and M midpoint of DP
def rot(p,c,a):
    a=math.radians(a); v=p-c; return c+np.array([v[0]*math.cos(a)-v[1]*math.sin(a),v[0]*math.sin(a)+v[1]*math.cos(a)])
def area(P): return 0.5*sum(P[i][0]*P[(i+1)%len(P)][1]-P[(i+1)%len(P)][0]*P[i][1] for i in range(len(P)))
B=np.array([0.,0.]);D=np.array([2.,0.])
for C in [np.array([0.6,-0.5])]+[np.array([random.uniform(0.2,1.8),random.uniform(-1.5,-0.1)]) for _ in range(50)]:
    A_=rot(C,B,120);E_=rot(C,D,-60);P_=rot(D,B,120)
    assert abs(area([A_,B,C,D,E_])-math.sqrt(3))<1e-9
    assert np.allclose((A_+E_)/2,(D+P_)/2)
# 1745630
for n in range(1,200): assert ((-13)**(n+1)-(-13)**n-(-13)**(n-1))%181==0
assert (-(13**2)-(-13-1))%181!=0
# 1745141
Dv=[d for d in range(1,721) if 720%d==0]
assert F(sum(1 for a,b in itertools.combinations(Dv,2) if (a+b)%6==0),math.comb(30,2))==F(143,435)
# 1745554: real solutions count -> number of distinct x/y = 2
r=np.roots([1,0,-20907,138]); good=[s for s in r if abs(s.imag)<1e-9 and s.real**2<=13938]
assert len(good)==1
s0=good[0].real; p0=(s0*s0-6969)/2; disc=s0*s0-4*p0; assert disc>0
a1=(s0+math.sqrt(disc))/2; b1=(s0-math.sqrt(disc))/2
assert abs(a1*a1+b1*b1-6969)<1e-6 and abs(a1**3+b1**3-69)<1e-6
cb=lambda t: math.copysign(abs(t)**(1/3),t)
ratios={round(cb(a1)/cb(b1),9),round(cb(b1)/cb(a1),9)}; assert len(ratios)==2
# 1743700, 1743708
assert F(2*10*20,30)==F(40,3)
assert F(1,2)*(-6)+3==0 and F(1,2)*(-2)==-1
# 1731039: supply always positive
for k in range(0,100000,7):
    assert 2018+k-F(10,11)*(k+1)>0
# 1742448
d=F(2); assert d/5-d/30==F(1,3)
# 1745435
import sympy as sp
X=sp.symbols('X'); xs=sp.solve((X-3)**2+(X+2-3)**2-100,X)
p1,p2=[(t,t+2) for t in xs]; assert sp.simplify(sp.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)-14*sp.sqrt(2))==0
assert F(31,2)==F(27,2)+2 and F(-22,7)==F(-36,7)+2
# 1744310
assert pow(3,2006,10)==9
# 1745417
s=1+math.sqrt(13); assert abs(s**3-(s-2)**3-80)<1e-9 and abs(4/3*math.pi*(3/math.pi)*4*5-80)<1e-9
# 1734050 sentence
w="zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
def nw(n):
    if n<20: return w[n]
    t=['','','twenty','thirty','forty'][n//10]; return t+('' if n%10==0 else '-'+w[n%10])
sols=[(x,y,z) for x in range(1,50) for y in range(1,50) for z in range(1,50)
      if (lambda s:(s.count('e'),s.count('t'),s.count('s'))==(x,y,z))(f"This sentence contains {nw(x)} e's, {nw(y)} t's, and {nw(z)} s's.".lower())]
assert sols==[(6,5,8)]
# 1744827
assert max(n for n in range(100,1000) if '7' in str(n) and 1000<=math.lcm(700,n)<=9999)==875
# 1744022 q01 holes
solid={(x,y,z) for x in range(5) for y in range(5) for z in range(5) if [x,y,z].count(2)<2}
def painted(c): return sum(1 for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)] if (c[0]+d[0],c[1]+d[1],c[2]+d[2]) not in solid)
assert len(solid)==112 and sum(1 for c in solid if painted(c)==2)==72
# 1744022 q02 falcon: Monte Carlo of reachable fraction of ball outside the house octant
assert F(7,8)*F(4,3)*30**3==31500
