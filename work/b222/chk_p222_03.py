import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(3)
def tobase(n,b):
    d=[]
    while n: d.append(n%b); n//=b
    return d[::-1]
# 1781845
terms=[]
for n in range(2,17):
    v=(n-1)*n+(n-2); assert tobase(v,n)==[n-1,n-2]; terms.append(v)
assert sum(terms)==1465
# 1781688
for x in np.linspace(-20,20,40001):
    ok=abs(-2*x-18)>=abs(x*x+2*x+2)-1e-12
    assert ok==(-4-1e-9<=x<=4+1e-9)
# 1781399 and 1777432: cube rotations
faces=['U','D','F','B','L','R']
def rot(perm_cycles):
    p={f:f for f in faces}
    for cyc in perm_cycles:
        for i in range(len(cyc)): p[cyc[i]]=cyc[(i+1)%len(cyc)]
    return p
gens=[rot([('F','R','B','L')]),rot([('U','F','D','B')])]
group=[{f:f for f in faces}]
changed=True
while changed:
    changed=False
    for g in list(group):
        for h in gens:
            c={f:h[g[f]] for f in faces}
            if c not in group: group.append(c); changed=True
assert len(group)==24
def orbits(cols):
    seen=set();cnt=0
    for c in cols:
        key=tuple(c[f] for f in faces)
        if key in seen: continue
        cnt+=1
        for g in group:
            seen.add(tuple(c[g_inv] for g_inv in [next(x for x in faces if g[x]==f) for f in faces]))
    return cnt
cols=[dict(zip(faces,p)) for p in set(itertools.permutations('RRGGBB'))]
assert orbits(cols)==6
opp={'U':'D','D':'U','F':'B','B':'F','L':'R','R':'L'}
proper=[]
for p in itertools.product(range(6),repeat=6):
    c=dict(zip(faces,p))
    if all(c[f]!=c[g] for f in faces for g in faces if f!=g and opp[f]!=g): proper.append(c)
assert orbits(proper)==230
assert orbits([c for c in proper if len(set(c.values()))==6])==30
# 1781263
for k in range(0,31):
    x=10**(k+1); a=(x-4)//6; b=x//2; c=(x-1)//3
    assert a**3+b**3+c**3==int(str(a)+str(b)+str(c))
    assert str(a)=='1'+'6'*k and str(b)=='5'+'0'*k and str(c)=='3'*(k+1)
# 1780934: random 6-regular enemy graphs on 20 vertices
import networkx as nx
for seed in range(5):
    Gr=nx.random_regular_graph(6,20,seed=seed)
    cnt=0
    for t in itertools.combinations(range(20),3):
        e=sum(Gr.has_edge(u,v) for u,v in itertools.combinations(t,2))
        if e in (0,3): cnt+=1
    assert cnt==360
# 1635242
assert min(n for n in range(1,10000) if 28*n%365==0)==365
assert F(20*36,2*120)==3
# 1682685
assert 2*(-3)-3==4*(-3)+3
# 1638802: brute force minimum over attribute assignments
best=None
for N in range(9,13):
    # each student: subset of {T,S,R}, nonempty
    types=[t for t in itertools.product((0,1),repeat=3) if any(t)]
    for combo in itertools.combinations_with_replacement(types,N):
        T=sum(t[0] for t in combo);S_=sum(t[1] for t in combo);R=sum(t[2] for t in combo)
        sn=sum(1 for t in combo if t[1] and not t[0]);rn=sum(1 for t in combo if t[2] and not t[0])
        if (T,S_,R,sn,rn)==(9,5,4,1,1): best=N;break
    if best: break
assert best==10
# 1780409
assert min(a*b*c for a,b,c in itertools.combinations([1,2,0,-3,-2],3))==-6
# 1777350
cnt=0
for mask in range(1<<12):
    vals=[1]*5+[5]*4+[10]*3
    if sum(v for i,v in enumerate(vals) if mask>>i&1)==30: cnt+=1
assert F(cnt,4096)==F(23,2048)
# 1780414
for p in range(1,30):
    n=3*p+1; t=0
    while n>0: n-=min(3,n); t+=1
    assert t==p+1
# 1779767 Monte Carlo
X=np.random.default_rng(0).uniform(0,12,(400000,3))
d=np.abs(X[:,[0,0,1]]-X[:,[1,2,2]])
p=np.mean((d<3).any(axis=1)); assert abs(p-7/8)<0.003
# 1780335
assert ''.join(str(i) for i in range(1,101)).count('1')==21
# 1780203
def v(pr,n):
    e=0
    while n: n//=pr; e+=n
    return e
assert v(2,12)+v(3,18)==18
Y=np.random.default_rng(1).uniform(0,100,(400000,3)).sum(axis=1)
assert abs(np.mean((Y>=100)&(Y<=200))-2/3)<0.003
r1=-3+3*math.sqrt(5)/5;r2=-3-3*math.sqrt(5)/5
for r in (r1,r2): assert abs(abs(r*r+5*r+6)/r**2-1/6)<1e-12
xs=np.linspace(-20,20,400001); xs=xs[xs!=0]
g=np.abs(xs**2+5*xs+6)/xs**2-1/6
assert np.sum(np.sign(g[1:])!=np.sign(g[:-1]))==2 and abs(r1+r2+6)<1e-12
k=2/math.sqrt(21)
assert abs(24*k*k/(24-6*k*k)-0.2)<1e-12 and abs(4-4*k-(4-8*math.sqrt(21)/21))<1e-12
# 1779907
assert sum(1 for n in range(100,1000) if str(n)[0]!=str(n)[1] and str(n)[1]!=str(n)[2])==729
# 1779636
import datetime
assert (datetime.date(2014,6,21)-datetime.date(2014,4,18)).days==64 and datetime.date(2014,4,18).weekday()==4
print('chk_p222_03 ok')
