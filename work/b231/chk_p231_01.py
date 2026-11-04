import math, itertools, random, sys
sys.set_int_max_str_digits(100000)
from fractions import Fraction as F
from sympy import totient, isprime
random.seed(1)
# 1733681
for n in range(1,200): assert sum(k*k for k in range(1,n+1))==n*(n+1)*(2*n+1)//6
# 1734046 towers mod 10 via generalised Euler theorem
def big(n,h,lim):
    v=1
    for _ in range(h):
        if v>64: return True
        v=n**v
        if v>=lim: return True
    return v>=lim
def tmod(n,h,m):
    if m==1: return 0
    if h==0: return 1%m
    if h==1: return n%m
    ph=int(totient(m)); e=tmod(n,h-1,ph)
    if big(n,h-1,ph): e+=ph
    return pow(n,e,m)
assert tmod(3,3,10)==pow(3,27,10) and tmod(2,2,10)==4 and tmod(4,4,1000)==pow(4,4**256,1000)
d=[tmod(n,n,10) for n in range(1,2019)]
assert d[:20]==[1,4,7,6,5,6,3,6,9,0,1,6,3,6,5,6,7,6,9,0] and sum(d)==9887 and sum(d)%10==7
# 1734624
assert math.hypot(15,8)==17 and 23-17==6 and 17*14//2==119
# 1734398 Heron degenerate
for a,b in [(3,4),(2,5)]:
    c=a+b; s=F(a+b+c,2); assert s*(s-a)*(s-b)*(s-c)==0
# 1734291
assert min(a+b for a in range(1,100) for b in range(1,100) if 45*a==54*b)==11
# 1444972
assert min(n for n in range(2011,10**6,10000) if n%7==0)==32011
# 1733869 cube segments
V=list(itertools.product((0,1),repeat=3))
def inter(p,q,r,s):
    import numpy as np
    p,q,r,s=map(np.array,(p,q,r,s))
    M=np.array([q-p,r-s]).T
    for i,j in [(0,1),(0,2),(1,2)]:
        A=M[[i,j]]
        if abs(np.linalg.det(A))>1e-9:
            t=np.linalg.solve(A,(r-p)[[i,j]])
            return 0<=t[0]<=1 and 0<=t[1]<=1 and np.allclose(p+t[0]*(q-p),r+t[1]*(s-r))
    return False
cnt=tot=0
for A,B,C,D in itertools.permutations(V,4):
    tot+=1; cnt+=inter(A,B,C,D)
assert F(cnt,tot)==F(2,35)
# 1734077 triangle count (enumeration)
sq=[(0,0),(1,0),(-1,0),(0,1),(0,-1)]
segs=set()
for (x,y) in sq:
    P=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
    c=(F(2*x+1,2),F(2*y+1,2))
    for i in range(4): segs.add(frozenset([tuple(map(F,P[i])),tuple(map(F,P[(i+1)%4]))]))
    for p in P: segs.add(frozenset([tuple(map(F,p)),c]))
pts=set(itertools.chain.from_iterable(segs))
col=lambda a,b,c:(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])==0
def conn(a,b):
    on=sorted(p for p in pts if col(a,b,p) and min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and min(a[1],b[1])<=p[1]<=max(a[1],b[1]))
    return all(frozenset([on[i],on[i+1]]) in segs for i in range(len(on)-1))
assert sum(1 for a,b,c in itertools.combinations(sorted(pts),3) if not col(a,b,c) and conn(a,b) and conn(b,c) and conn(a,c))==56
# 1734047
assert all((int('42'*k)+e)%p for k in range(1,30) for e in (1,-1) for p in (2,3,5,7))
assert (int('42'*5)-1)%11==0 and int('42'*5)-1==11*385674931
# 1734032
assert pow(7,2018,10)==9 and pow(7,2019,10)==3
# 1607327
assert math.comb(26,6)==230230
# 1733566
for n in range(1,1001):
    p=F(1)
    for k in range(n-1): p*=F(999-k,1000-k)
    assert p==F(1001-n,1000) and p*F(1,1001-n)==F(1,1000)
# 1076780
for x in [F(-2),F(-1,3)]: pass
y=lambda x:(x*x-2*x-3)/(2*x*x+2*x+1)
assert y(F(-2))==1 and y(F(-1,3))==-4
assert all(-4-1e-12<=y(t/100)<=1+1e-12 for t in range(-100000,100000))
# 1701662
assert F(sum(1 for s in itertools.product((10,15,50),repeat=10) if sum(s)%3==0),3**10)==F(1,3)
# 1711870
import sympy as sp
x=sp.symbols('x')
assert sp.simplify((5*x**3-3*x**2+2*x-1)/(x**4+x**2)-(2/x-1/x**2+(3*x-2)/(x**2+1)))==0
# 1731581
ok=lambda n:any(n-8*a-12*b>=0 and (n-8*a-12*b)%15==0 for a in range(n//8+1) for b in range(n//12+1))
assert not ok(49) and all(ok(n) for n in range(50,200))
# 1731674
assert len({3*a+5*b for a in range(21) for b in range(21)}-{0})==152
# 1732087 circles: a=6,c=5,b=7
a,c,b=6,5,7
d=math.sqrt(c*c-a*a/4)
for sgn,r2 in [(-1,18),(1,130)]:
    r=math.sqrt(b*b+c*c+sgn*b*math.sqrt(4*c*c-a*a)); assert abs(r*r-r2)<1e-9
    O1=(-d,0); O2=(-d+b,0) if sgn<0 else (-d-b,0)
    assert abs(math.dist(O2,(0,3))-r)<1e-9 and abs(math.dist(O1,(0,3))-c)<1e-9
# 1732087 hexagon closes
import cmath
z=sum(L*cmath.exp(1j*math.radians(60*k)) for k,L in enumerate([4,2,7,1,5,4])); assert abs(z)<1e-9
# 1732678
m=len(str(16**2011)); n=len(str(625**2011)); assert m+n==8045
# 1543814
for _ in range(20000):
    u=[random.random() for _ in range(3)]; s=sum(u); a,b,c=[3*t/s for t in u]
    assert 9/(a*b*c)>=2*(a/b+b/c+c/a)+3-1e-9
# 1732887
p=lambda n,k: n**3+1+k*(n-1)*(n-2)*(n-3)
k=F(-94,55); assert [p(1,k),p(2,k),p(3,k),p(12,k)]==[2,9,28,37] and p(12,0)==1729
# 1627894
assert abs((math.sqrt(5)-1)/2+1-2/(math.sqrt(5)-1))<1e-12
# 526580
def ways(t): return sum(1 for s in range(t//2+1) for f in range(t//3+1) for u in range(t//6+1) for v in range(t//7+1) if 2*s+3*f+6*u+7*v==t)
assert ways(21)==18 and ways(17)==10
# 1732939
N=1.0
for _ in range(200): N=math.sqrt(7*math.sqrt(3*N))
assert abs(N**3-147)<1e-9
# 1732841
for r in [(-3+math.sqrt(37))/2,(-3-math.sqrt(37))/2]: assert abs(r*(r+1)*(r+2)*(r+3)-63)<1e-9
assert len([t for t in sp.Poly(x*(x+1)*(x+2)*(x+3)-63).nroots() if abs(sp.im(t))<1e-12])==2
# 1732752
assert len({min(tuple(c[i:]+c[:i]) for i in range(7)) for c in itertools.product((0,1),repeat=7)})==20
# 1732647
for N in range(10,100000):
    assert (N%17==0)==((N//10-5*(N%10))%17==0)
    assert (N%19==0)==((N//10+2*(N%10))%19==0)
print('ok')
