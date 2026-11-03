import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(2)
# 1792312
assert pow(2,178,1000)==544 and pow(2,78,125)==44
# 1791613 Monte Carlo
h=0
for _ in range(100000):
    a=sorted(random.random() for _ in range(4)); g=[a[1]-a[0],a[2]-a[1],a[3]-a[2],1-a[3]+a[0]]
    h+=max(g)<0.5
assert abs(h/100000-0.5)<0.01
# 1791940
pats=set(itertools.permutations('EEESSSSXX'))
good=[p for p in pats if all(p[i]!=p[i+1] for i in range(8))]
assert len(good)==79 and 79*6*24*2==22752
tot=0
for w in set(itertools.permutations('EEEXX')):
    k=sum(w[i]==w[i+1] for i in range(4)); tot+=math.comb(6-k,4-k) if k<=4 else 0
assert tot==79
# 1792157
x=sum(1/(2*k+1)**3 for k in range(200000)); n=sum(1/k**3 for k in range(1,400000))
assert abs(n-8*x/7)<1e-9
# 1791558
O=(F(12),F(41,3)); r2=lambda P:(P[0]-O[0])**2+(P[1]-O[1])**2
assert r2((0,6))==r2((8,0))==r2((16,0))==F(1825,9)
# 1791573
x,y,z=F(16,3),F(16,5),F(-16)
assert x*y==2*(x+y) and y*z==4*(y+z) and x*z==8*(x+z)
# 1791997: shadow via projection vs law of sines
for _ in range(200):
    a,bt=random.uniform(5,85),random.uniform(5,85); L=random.uniform(1,5)
    T=np.array([L*math.cos(math.radians(a)),L*math.sin(math.radians(a))])
    Qx=T[0]+T[1]/math.tan(math.radians(bt))
    assert abs(Qx-L*math.sin(math.radians(a+bt))/math.sin(math.radians(bt)))<1e-9
assert abs(4*math.sin(math.radians(120))/math.sin(math.radians(60))-4)<1e-12
assert math.sin(math.radians(140))<math.sin(math.radians(80))
# 1791167
assert (pow(9,2018)+pow(9,2019))%1000==210 and pow(9,2018,100)==21
cnt=0
for m in range(1<<12):
    if sum(7**i for i in range(12) if m>>i&1)%8==0: cnt+=1
assert F(cnt,4096)==F(231,1024) and 231+10==241
assert sum(1 for c in itertools.combinations(range(1,13),4) if all(c[i+1]-c[i]>=2 for i in range(3)))==126
g=0
for p in itertools.permutations(range(6)):
    if (p[0]+p[1]+p[2])%(p[3]+p[4]+p[5])==0: g+=1
assert F(g,720)==F(3,20)
names='ABCDE'  # E = AIME, D = Bob
arr=set()
for p in itertools.permutations(names):
    i=p.index('A'); q=p[i:]+p[:i]
    if abs(q.index('D')-q.index('E')) not in (1,4): arr.add(q)
assert len(arr)==12
k=2*math.sqrt(3)-3
assert abs(4*math.pi*3*k*k/(1+3*k*k)-9*math.pi*(4-math.sqrt(3))/13)<1e-12 and round(9*math.pi*(4-math.sqrt(3))/13,3)==4.933
# check tangency: three circles radius kR at distance R-kR, mutually tangent
R=2; r=k*R; assert abs(2*(R-r)*math.sin(math.radians(60))-2*r)<1e-12
# 1790899
assert F(100,40)*60==150 and F(100,48)==F(5,6)*F(100,40)
# 1791941
assert F(54,60)-F(60,75)==F(1,10)
assert [x for x in range(-100,100) if 4*(x-4)**2+2<=2*x+6]==[3,4,5,6]
# 1791855, 1791115
assert 10+8+F(6,2)-F(2,2)==20 and 50*(4-2)*1==100
# 1791322
p=F(4,5); q=1-p; assert 10*p**3*q**2==32*5*p*q**4
# 1787964
for n in range(1,12):
    sq=sum(1 for k in range(1,n+1) for i in range(n-k+1) for j in range(n-k+1))
    rc=sum(1 for a in range(n+1) for b_ in range(a+1,n+1) for c in range(n+1) for d in range(c+1,n+1))
    assert sq==n*(n+1)*(2*n+1)//6 and rc==math.comb(n+1,2)**2
assert 8*9*17//6==204 and 36**2==1296
# 1791264
rolls=list(itertools.product(range(1,7),repeat=3))
assert sum(sum(r)<8 for r in rolls)==35==math.comb(7,3) and sum(sum(r)<=8 for r in rolls)==56==math.comb(8,3)
# 1791227
assert F(sum(a!=b for a in range(1,7) for b in range(1,7)),36)==F(5,6)
# 1788394
assert 8**2+4**2==80
# 1499461
def ok(N): return all(pow(n,N,N)==n%N for n in range(1,N+1))
pr=[p for p in range(2,60) if all(p%d for d in range(2,int(p**.5)+1))]
best=min(p+q for p in pr for q in pr if ok(3*p*q))
assert best==28 and ok(561)
