import math, itertools, random
from fractions import Fraction as F
from functools import lru_cache
import sympy as sp
random.seed(3)
# 1730463
assert F(math.comb(5,2),math.comb(10,2))==F(2,9)
# 1730652
D=(0,0); h=2.0
def inter(P,Q,R,S):
    import numpy as np
    A=np.array([[Q[0]-P[0],R[0]-S[0]],[Q[1]-P[1],R[1]-S[1]]]); t=np.linalg.solve(A,[R[0]-P[0],R[1]-P[1]]); return t
tX=inter((0,h),(1,0),(0,0),(3,h))[1]; tY=inter((0,h),(2,0),(0,0),(3,h))[1]
assert abs(tY-tX-0.15)<1e-12
# 1730101
x,y=sp.symbols('x y')
assert sp.expand(2*((x-1)**2+(y-1)**2)-(x+y)**2)==x**2-2*x*y+y**2-4*x-4*y+4
u,v,w,p,q=sp.symbols('u v w p q')
expr=sp.expand((x-p)**2+(y-q)**2-(u*x+v*y+w)**2)
A=expr.coeff(x,2); B=expr.coeff(x,1).coeff(y,1); C=expr.coeff(y,2)
assert sp.simplify((B**2-4*A*C).subs(v**2,1-u**2))==0
# 1730306
@lru_cache(None)
def vals(n):
    if n==1: return frozenset([1])
    return frozenset(a-b for k in range(1,n) for a in vals(k) for b in vals(n-k))
for n in range(2,13): assert vals(n)==frozenset(range(-(n-2),n-1,2))
# 1268207
st=[0]*101
for k in range(1,101):
    for j in range(k,101,k): st[j]^=1
assert [i for i in range(1,101) if st[i]]==[i*i for i in range(1,11)]
# 1729694
assert max(n for n in range(100,1000) if n%2==1 and n%3==1 and n%4==1)==997
ok=lambda n:any((n-7*a)%11==0 for a in range(n//7+1))
assert not ok(59) and all(ok(n) for n in range(60,300))
# 1730054
found=max(a for a in range(60,80) for b in range(50,70) for c in range(b,70) for d in range(c,70) for e in range(d,70)
          if a+b+c+d+e==300 and (a-60)**2+(b-60)**2+(c-60)**2+(d-60)**2+(e-60)**2==20)
assert found==64
# real-valued bound: max deviation d with sum dev^2=20 is 4
assert abs(math.sqrt(20*4/5)-4)<1e-12
# 1729919
from decimal import Decimal,getcontext
getcontext().prec=50
fr=Decimal(123456789).sqrt()%1
assert min(range(1,1000),key=lambda n:abs(Decimal(1)/n-fr))==9 and Decimal('0.111056')<fr<Decimal('0.111062')
# 1729780
assert sum(1 for n in range(1,100) if math.floor(F(n,7)+F(1,2))==math.ceil(F(n,7)))==56
# 1729473
assert [n for n in range(100,1000) if n%7==0 and n%17==2]==[189,308,427,546,665,784,903]
# 1729478
assert all(F(1,4)<F(k,24)<F(1,2) for k in range(7,12))
# 1729495
assert math.perm(10,7)==604800 and math.comb(10,7)==120
# 1728894
P=(-4,0);Q=(6,0); nn=(1/5,math.sqrt(24)/5)
L=(P[0]+6*nn[0],P[1]+6*nn[1]); M=(Q[0]+4*nn[0],Q[1]+4*nn[1])
d=(M[0]-L[0],M[1]-L[1])
assert abs(d[0]*nn[0]+d[1]*nn[1])<1e-12 and abs(math.hypot(*d)-4*math.sqrt(6))<1e-12
assert abs(math.dist(P,Q)-10)<1e-12 and abs(math.dist(P,(-10,0))-6)<1e-12 and abs(math.dist(Q,(10,0))-4)<1e-12
# 1726523
assert pow(2016,pow(2015,2014,10),11)==1 and pow(3,5,11)==1
# 1726545 simulate
tot=0;T=100000
for _ in range(T):
    a,b=0,1;t=0
    while True:
        t+=1; a=random.choice([v for v in range(4) if v!=a]); b=random.choice([v for v in range(4) if v!=b])
        if a==b: break
    tot+=t
assert abs(tot/T-4.5)<0.06
# 1729010
assert sum(map(int,str(10**1000-7982)))==8975
# 1728999
assert [Y for Y in range(2018,3000) if 12*(Y-2018)<=Y<=12*(Y-2018)+11]==[2201]
# 1726530
seen=F(30*5,1)+F(25,2); assert seen/(45*60)==F(13,216) and 1-F(13,216)*F(1,2)*F(9,10)==F(467,480)
# 1728477
for _ in range(2000):
    n=random.randint(2,12); Sv=random.uniform(0.1,10); a=[random.uniform(0,Sv) for _ in range(n)]
    assert min(abs(a[i]-a[j]) for i in range(n) for j in range(i)) <= Sv/(n-1)+1e-12
# 1727878
import numpy as np
for _ in range(50):
    A,B,C=[np.array([random.uniform(-5,5),random.uniform(-5,5)]) for _ in range(3)]
    E=(3*B+A)/4; Dd=(4*C+B)/5; Fp=(E+5*Dd)/6
    M=np.array([Fp-B,A-C]).T; t=np.linalg.solve(M,A-B); G=B+t[0]*(Fp-B)
    assert abs(np.linalg.norm(Fp-B)/np.linalg.norm(G-Fp)-17/7)<1e-7
    assert abs(np.linalg.norm(G-A)/np.linalg.norm(C-G)-16)<1e-6
# 1728427
a,b=sp.symbols('a b'); om=(-1+sp.sqrt(3)*sp.I)/2
assert sp.expand((a-om*b)*(a-sp.conjugate(om)*b))==a**2+a*b+b**2
# 1727717
s_=[sp.symbols(c) for c in 'aops']
sol=sp.solve([s_[0]+s_[1]+s_[2]-3,s_[0]+s_[1]+s_[3]+15,s_[0]+s_[2]+s_[3]-1,s_[1]+s_[2]+s_[3]-17],s_)
assert sol[s_[0]]*sol[s_[1]]*sol[s_[2]]*sol[s_[3]]==255
assert F(15*10*5,math.comb(100,3))==F(5,1078)
assert math.comb(16,3)-14==546
V=list(itertools.product((0,1),repeat=3))
def rots():
    R=set()
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1,-1),repeat=3):
            M=np.zeros((3,3),int)
            for i,pi in enumerate(perm): M[i,pi]=sg[i]
            if round(np.linalg.det(M))==1: R.add(tuple(M.flatten()))
    return [np.array(r).reshape(3,3) for r in R]
Rs=rots(); assert len(Rs)==24
def act(Mx,v):
    c=np.array(v)*2-1; c2=Mx@c; return tuple(((c2+1)//2).tolist())
orbits=set()
for pl in itertools.permutations(V,4):
    orbits.add(min(tuple(act(Mx,v) for v in pl) for Mx in Rs))
assert len(orbits)==70
N=200000; c=0
for _ in range(N):
    t=[random.uniform(0,120) for _ in range(3)]
    if any(abs(t[i]-t[j])<30 for i in range(3) for j in range(i)): c+=1
assert abs(c/N-7/8)<0.005
# 1728425
for k in range(1,201):
    v=F(k**7,7)+F(k**5,5)+F(2*k**3,3)-F(k,105); assert v.denominator==1 and v>0
print('ok')
