import math, itertools, random
from fractions import Fraction as F
from math import comb
random.seed(1)
# 419795 2003 AMC 8 #17
kids={'Benjamin':('Blue','Black'),'Jim':('Brown','Blond'),'Nadeen':('Brown','Black'),'Austin':('Blue','Blond'),'Tevyn':('Blue','Black'),'Sue':('Blue','Blond')}
ok=lambda g: all(kids[a][0]==kids[b][0] or kids[a][1]==kids[b][1] for a,b in itertools.combinations(g,2))
others=[k for k in kids if k!='Jim']
good=[p for p in itertools.combinations(others,2) if ok(('Jim',)+p) and ok(tuple(k for k in others if k not in p))]
assert good==[('Austin','Sue')]
# 1728070 DE || BC
B=(0,0);C=(4,0);A=(2,2*math.tan(math.radians(70)))
def ext(P,d,Q,R):
    # intersection of P+t d with line QR
    ex,ey=R[0]-Q[0],R[1]-Q[1]
    den=d[0]*ey-d[1]*ex; t=((Q[0]-P[0])*ey-(Q[1]-P[1])*ex)/den
    return (P[0]+t*d[0],P[1]+t*d[1])
Ep=ext(C,(math.cos(math.radians(145)),math.sin(math.radians(145))),B,A)
for yD in [Ep[1]]:
    s=yD/A[1]; D=(C[0]+s*(A[0]-C[0]),yD)
assert abs(math.dist(C,D)-math.dist(D,Ep))<1e-9
# 1726572 lattice triangles 5x5
P=[(x,y) for x in range(5) for y in range(5)]
col=lambda a,b,c:(b[0]-a[0])*(c[1]-a[1])==(b[1]-a[1])*(c[0]-a[0])
assert sum(1 for t in itertools.combinations(P,3) if not col(*t))==2148
# 1727888
assert sum(1 for a in range(11) for b in range(11) if (2**a*5**b)%2000==0)==56
# 1727994
assert abs(sum(1/(2*k+1)**2 for k in range(10**6))-math.pi**2/8)<1e-6
# 1727959 grid
g=[[8,None,None,14],[None,None,3,None],[None,12,13,None],[10,11,6,4]]
cells=[(i,j) for i in range(4) for j in range(4) if g[i][j] is None]
sols=[]
for p in itertools.permutations([1,2,5,7,9,15,16]):
    h=[r[:] for r in g]
    for (i,j),v in zip(cells,p): h[i][j]=v
    s=[sum(r) for r in h]+[sum(h[i][j] for i in range(4)) for j in range(4)]+[sum(h[i][i] for i in range(4)),sum(h[i][3-i] for i in range(4))]
    if sorted(s)==list(range(30,40)): sols.append(h)
assert sorted(sols)==sorted([[[8,1,15,14],[7,9,3,16],[5,12,13,2],[10,11,6,4]],[[8,1,15,14],[16,9,3,7],[2,12,13,5],[10,11,6,4]]])
# 1101383
assert (-3)**2+10*(-3)+21==0 and 49-70+21==0
# 1726492
p=F(4,13);q=1-p
assert 15*p**4*q**2==F(1,3)*20*p**3*q**3 and q==F(9,13)
# 1723444 clock
h=7*30+23*F(1,2); m=23*6
assert h-m==F(167,2) and 360-(h-m)==F(553,2)
# 1727520
cnt=sum(1 for d in range(2) for e in range(2) for a in range(3,21) for b_ in range(3,21) if 20-d-e-a-b_>=3)
assert cnt==265
# 1727026
assert len(str(5**2018))==1411 and str(5**2018)[0]=='3'
assert sum(1 for n in range(1,2019) if str(5**n)[0]=='1')==607
# 1721571
pts=[(x,y) for x in range(-2,3) for y in range(-2,3) if x*x+y*y<8]
assert len(pts)==21
tri=sum(1 for t in itertools.combinations(pts,3) if not col(*t))
assert F(tri,comb(21,3))==F(124,133)
# 1727049
N=200000;hit=0
for _ in range(N):
    x=sorted(random.uniform(0,9) for _ in range(5))
    if all(x[i+1]-x[i]>1 for i in range(4)): hit+=1
assert abs(hit/N-3125/59049)<0.003
# 1726537
n=next(n for n in range(1,10**6) if n%11==6 and n%100==95 and n%101==99)
assert n==70395
best=min(a+b_+c for c in range(n//101+1) for b_ in range(0,(n-101*c)//100+1) for a in [(n-101*c-100*b_)//11] if (n-101*c-100*b_)%11==0)
assert best==697
# 1726968
for a,b_ in [(1,0),(-1,3),(-1,-2.5)]:
    for x in [-3,0,1.7]: assert abs(a*(a*x+b_)+b_-x)<1e-12
# 1727169
sq=[i*i for i in range(11)]
assert len({a+b_ for a in sq for b_ in sq if 1<=a+b_<=100})==43
assert len({a+b_ for a in sq[1:] for b_ in sq[1:] if a+b_<=100})==35
# 1727051
for a,b_,c in itertools.product(range(1,25),repeat=3):
    g3=math.gcd(a,b_,c); l3=math.lcm(a,b_,c)
    assert F(g3**2,math.gcd(a,b_)*math.gcd(b_,c)*math.gcd(c,a))==F(l3**2,math.lcm(a,b_)*math.lcm(b_,c)*math.lcm(c,a))
# 1726538
assert 149+119-(198-29)==99
# 1726318
def reps(N):
    c=0
    for k in range(2,N+1):
        num=N-k*(k-1)//2
        if num<=0: break
        if num%k==0: c+=1
    return c
for N in range(1,3001):
    od=sum(1 for d in range(1,N+1,2) if N%d==0)
    assert reps(N)==od-1
# 1726274 locus
for a in [0.3,1,2.5,3.9]:
    k=4; x=k-a; y=math.sqrt(4*a*x)
    assert abs(math.dist((x,y),(a,0))-k)<1e-12 and abs(y*y-(4*k*x-4*x*x))<1e-9
# 1726527 logic: enumerate
names=['go','bf','sis','most','reveal','dare','funny','haunt','scared']
imp=lambda p,q: (not p) or q
models=[]
for v in itertools.product([0,1],repeat=9):
    d=dict(zip(names,v))
    if imp(not d['bf'],d['sis']) and imp(d['go'],d['most']) and imp(d['reveal'],not d['sis']) and imp(d['bf'],not d['most']) and imp(d['dare'],d['funny']) and imp(d['haunt'],d['scared']) and imp(d['scared'],d['dare']) and d['go']:
        models.append(d)
assert any(m['haunt'] for m in models) and any(not m['haunt'] for m in models)
assert all(not m['bf'] and m['most'] for m in models)
# 1726526 Pisano periods
def per(m):
    a,b_=0,1
    for p in range(1,1000):
        a,b_=b_,(a+b_)%m
        if (a,b_)==(0,1): return p
assert per(2)==3 and per(5)==20 and per(10)==60
# 1726675
assert comb(4,2)==6==4*3//2 and 4-6+4==2
# 1726581: f(x)=-f(x) when n=0 forces 0
# 1726370 q24
assert max(a for a in range(0,200) for b_ in range(0,200) if a*a-b_*b_==100)==26
# 1726370 q27
vals=[]
for j2 in range(14,72):
    for rest in itertools.combinations(range(14,j2),4):
        if j2+sum(rest)==165: vals.append(j2); break
assert max(vals)-min(vals)==36
# 1725794
N=200000;hit=0
for _ in range(N):
    x=random.uniform(0,2);y=random.uniform(0,1)
    if x/2>2*y: hit+=1
assert abs(hit/N-0.25)<0.005
