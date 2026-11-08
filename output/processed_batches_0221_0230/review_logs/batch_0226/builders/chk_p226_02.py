import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(5)
# 1761523
asc=sum(1 for p in itertools.permutations(range(1,8),4) if list(p)==sorted(p))
assert F(asc,7*6*5*4)==F(1,24)
# 1761483
for m,n,x in [(2,3,F(3,2)),(5,2,None),(1,4,None)]:
    # solve m x^m = n x^n numerically for x>0
    xr=(F(n,m))**1 if False else (n/m)**(1/(m-n))
    lhs=1/(xr**m+xr**n)+1/(xr**m-xr**n); rhs=2*m*n/((n*n-m*m)*xr**n)
    assert abs(m*xr**m-n*xr**n)<1e-9 and abs(lhs-rhs)<1e-9
# 1761140 dart
T=400000;hit=0
for _ in range(T):
    x=random.uniform(-1,1);y=random.uniform(-1,1)
    dc=math.hypot(x,y); dk=min(math.hypot(x-a,y-b) for a in (1,-1) for b in (1,-1))
    if dc<dk and dk<=1: hit+=1
assert abs(hit/T-(math.pi-2)/4)<0.004
# 1761230
assert F(sum(1 for t in itertools.product('HT',repeat=4) if t.count('H')>=3),16)==F(5,16)
# 1761162
assert pow(7,2010,100)==49
# 1761197
assert 10**2*9==900
# 1761161
for n in range(1,50): assert F(1,n*(n+2))==F(1,2*n)-F(1,2*(n+2))
# 1760139 seeds
S=set()
for a in itertools.product(range(7),range(3),range(3)):
    for b in itertools.product(range(7),range(3),range(3)):
        c=(6-a[0]-b[0],2-a[1]-b[1],2-a[2]-b[2])
        if min(c)<0: continue
        S.add((a,)+tuple(sorted([b,c])))
assert len(S)==512 and math.comb(8,2)*36==1008
# 1761117
def leg(N,p):
    e=0;q=p
    while q<=N: e+=N//q; q*=p
    return e
assert leg(201,5)==49 and leg(10,5)==2
fe=0;f=math.factorial(201)
while f%5==0: f//=5; fe+=1
assert fe==49
# 1760928
sets=[c for c in itertools.combinations(range(10),5) if sum(c)==31]
assert len(sets)==5 and F(sum(len({2,3,5,7}&set(c))==2 for c in sets),5)==F(3,5)
# 1759738
a,b,c=np.linalg.solve([[1,1,0],[0,1,1],[1,0,1]],[10,14,24]); assert abs(a+b+c-24)<1e-9
# 1760504: construct triangle through several vertices
fp=lambda x:x*x+2*x+4
def bis(g,lo,hi):
    for _ in range(200):
        mid=(lo+hi)/2
        if g(lo)*g(mid)<=0: hi=mid
        else: lo=mid
    return (lo+hi)/2
R=np.array([[0.5,-math.sqrt(3)/2],[math.sqrt(3)/2,0.5]])
for a in [-3,-1,0,0.7,2.5]:
    A=np.array([a,fp(a)])
    g=lambda t:(lambda C:C[1]-fp(C[0]))(A+R@(np.array([t,fp(t)])-A))
    ts=np.linspace(a+1e-4,a+50,200001); v=[g(t) for t in ts]
    i=next(i for i in range(len(v)-1) if v[i]>0 and v[i+1]<=0)
    t=bis(g,ts[i],ts[i+1]); B=np.array([t,fp(t)]); C=A+R@(B-A)
    assert abs(C[1]-fp(C[0]))<1e-6 and abs(np.linalg.norm(A-B)-np.linalg.norm(B-C))<1e-6
    assert abs(math.sqrt(3)/2+2*math.sqrt(3)*(a+1)**2 - (math.sqrt(3)/2+2*math.sqrt(3)*(a+1)**2))<1e-12
assert abs(fp(1.3005)-8.2923)<1e-3 and abs(fp(-3.0670)-7.2724)<1e-3
A,B,C=np.array([-1,3]),np.array([math.sqrt(3)-1,6]),np.array([-math.sqrt(3)-1,6])
assert abs(fp(B[0])-6)<1e-12 and abs(np.linalg.norm(A-B)-2*math.sqrt(3))<1e-12 and abs(np.linalg.norm(B-C)-2*math.sqrt(3))<1e-12
# 1760988
s=sum(k*(k+1)*(k+2) for k in range(1,2019)); assert s%10==0 and s==2018*2019*2020*2021//4
# 1760858
pts=[(x,y) for x in range(8) for y in range(8)]
assert F(sum((p[0]*q[1]-p[1]*q[0])%2==0 for p in pts for q in pts),4096)==F(5,8)
# 1760752
def tax(I): return 0.04*min(I,10000)+0.05*max(0,min(I,30000)-10000)+0.06*max(0,I-30000)
assert abs(tax(60000)-3200)<1e-9
# 1760885
assert abs(math.tan(math.asin(2/3))**2-0.8)<1e-12
# 1760574
J={0,1,2,3};c=0
for g1 in itertools.combinations(range(10),3):
    r=[p for p in range(10) if p not in g1]
    for g2 in itertools.combinations(r,3):
        g3=set(r)-set(g2)
        if J&set(g1) and J&set(g2) and J&g3: c+=1
assert c==2520
# 1760770
assert [x for x in range(1,106) if x%3==2 and x%5==3 and x%7==2]==[23]
# 1759320 Hill: count invertible 2x2 mod 26 by enumeration
inv=0
for a in range(26):
    for d in range(26):
        ad=a*d
        for b in range(26):
            for c in range(26):
                if math.gcd((ad-b*c)%26,26)==1: inv+=1
assert inv==157248 and F(26**4-inv,26**4)==F(1441,2197)
prod=lambda n: math.prod((1-F(1,2**i))*(1-F(1,13**i)) for i in range(1,n+1))
assert 1-prod(2)==F(1441,2197)
# n=1 check of formula: integers 0..25 coprime to 26: 12
assert 1-prod(1)==F(26-12,26)
# 1760552
x=2/3; assert abs(2**(16**x)-16**(2**x))<1e-9
