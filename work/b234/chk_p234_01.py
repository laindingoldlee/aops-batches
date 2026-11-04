import math, itertools, random
from fractions import Fraction as F
import sympy as sp
random.seed(7)
C=math.comb
# 1716692
assert sum(1 for a in itertools.product(range(1,11),repeat=4) if sum(a)==10)==84==C(9,3)
# 1716751
assert 5*6==30
# 1715695 q01
assert C(5,5)+C(5,4)+C(5,3)==16 and 5*60==4*75==3*100
# 1715695 q02
assert sum(n for n in range(1,1000) if (n*n+18)%n==0)==39 and sum(n for n in range(1,1000) if (n+18)%n==0)==39
# 1715695 q03: axis-parallel 4-cubes in 10-box, grid of points {3.5,6.5}^3 hit by every placement
for a in [x/10 for x in range(0,61)]:
    assert a<3.5<a+4 or a<6.5<a+4
assert F(8*64,1000)==F(512,1000)
# 1716645 truncated octahedron
V={tuple(a*s for a,s in zip(p,sg)) for p in itertools.permutations([0,1,2]) for sg in itertools.product([1,-1],repeat=3)}
E=[(u,v) for u,v in itertools.combinations(V,2) if sum((a-b)**2 for a,b in zip(u,v))==2]
assert len(V)==24 and len(E)==36 and (6*4+8*6)//3==24 and 24-36+14==2
# 1715055
sols=[F(x,10) for x in range(-200,200) if abs(F(x,10)-10)==2*abs(F(x,10)-1)]
assert sols==[-8,4]
# 1715902
res=[(a,x) for a in range(10) for x in range(0,3000) if F(2803+10*a-x,7276+x)==F(2,7)]
assert res==[(1,571)]
# 1715910
res=[(w,m,c) for w in range(39,240,39) for m in range(20,240,20) for c in range(35,240,35) if w+m+c==239]
assert res==[(39,60,140)] and 39//13+60//4+140//5==46
# 1715897
assert F(7*14,11)*F(22,21)*F(3,10)*F(5,2)==7
# 1715918
T=[(x,y,x+y) for x in range(1,10) for y in range(x+1,10) if x+y<=9]
good=0
for bits in itertools.product([0,1],repeat=9):
    col=dict(zip(range(1,10),bits))
    if all(not(col[a]==col[b]==col[c]) for a,b,c in T): good+=1
assert good==0
A8={1,2,4,8};B8={3,5,6,7}
for S_ in (A8,B8):
    assert not any(x in S_ and y in S_ and x+y in S_ for x in range(1,9) for y in range(x+1,9))
# 1715894
a=90*3600+30; bb=89*3600+59*60+30
assert a+bb==180*3600 and a-bb==60
# 1715905
assert 720*F(9*6,6*8)==810
# 1715914
a_,b_,c_=sp.symbols('a b c')
Aexpr=(b_-c_)**2/((a_-b_)*(a_-c_))+(c_-a_)**2/((b_-c_)*(b_-a_))+(a_-b_)**2/((c_-a_)*(c_-b_))
assert sp.simplify(Aexpr+3)==0
# 1715917
for n in range(1,61):
    A_=2**n*7**(n+1)+11; B_=2**(n+1)*7**n+3
    assert math.gcd(A_,B_)==1 and 2*A_-7*B_==1
    s=A_+B_-7; assert math.isqrt(s)**2!=s and s==9*14**n+7
# 1715915: BE+CF>EF numerically
for _ in range(3000):
    Ax,Ay=random.uniform(-3,3),random.uniform(0.5,4); B=(0,0);Cc=(random.uniform(1,5),0)
    D=(Cc[0]/2,0); t=random.uniform(0.02,0.98); Ep=(t*Ax,t*Ay)
    v=(Ep[0]-D[0],Ep[1]-D[1]); w=(-v[1],v[0])
    # intersect D+s*w with line A->C
    import numpy as np
    M=np.array([[w[0],-(Cc[0]-Ax)],[w[1],-(Cc[1]-Ay)]]); rhs=np.array([Ax-D[0],Ay-D[1]])
    if abs(np.linalg.det(M))<1e-9: continue
    s,u=np.linalg.solve(M,rhs)
    if not (0.01<u<0.99): continue
    Fp=(Ax+u*(Cc[0]-Ax),Ay+u*(Cc[1]-Ay))
    d=lambda P,Q: math.dist(P,Q)
    assert d(B,Ep)+d(Cc,Fp)>d(Ep,Fp)
# 1715908
for x in [7,5,9,2.5]:
    y=10-x; a2=(x*x+y*y)/2
    assert abs(a2/2+x*y/2-25)<1e-12
# 1715903
cnt=sum((2015-200*p-100*q)//10+1 for p in range(11) for q in range(21) if 200*p+100*q<=2015)
brute=sum(1 for p in range(11) for q in range(21) for t in range(202) if 200*p+100*q+10*t<=2015)
assert cnt==brute==8492==434*55-40*385+22
# 1715912
assert 42+14==2*(14+14)
# 1715911: symmetric multisets of odd size contain 0 (small check)
for vals in itertools.product(range(-2,3),repeat=5):
    S_=sum(vals)
    if sorted(S_-v for v in vals)==sorted(vals): assert 0 in vals
# 1715907
assert F(8,10)*F(11,10)*(1+F(1,44))==F(9,10) and F(100,44)==2+F(3,11)
# 1715031: every 3x3 bipartite 2-regular graph has a perfect matching
for perm in itertools.permutations(range(3)):
    knows={(i,j) for i in range(3) for j in range(3) if j!=perm[i]}
    assert all(((i,(perm[(i+1)%3])) in knows) for i in range(3))
# 1715644
assert abs(math.pi**7-3020.29)<0.01 and abs(1000*math.pi/math.pi**7-1)<0.05 and 0.986<math.pi**2/10<0.988
# 1715047
pr=sp.primerange(2,10**6)
for p in pr:
    r=p%30; assert r==1 or sp.isprime(r)
# 1715602
assert sum(F(1,4*x*x-1) for x in range(1,85))==F(84,169)
# 1713845
assert (2**2)==4 and 6*15==90 and F(90,90)==1 and 90+1==91
# 1715429
assert math.isclose(math.sqrt(100-9+1),2*math.sqrt(23))
# 1715432 (iii) by positions; (i),(ii) by gender patterns
pat=[p for p in itertools.combinations(range(12),5)]
assert sum(1 for p in pat if p[-1]-p[0]==4)*math.factorial(5)*math.factorial(7)==4838400==math.factorial(8)*120
assert sum(1 for p in pat if all(b-a>1 for a,b in zip(p,p[1:])))*math.factorial(5)*math.factorial(7)==33868800
cnt=0
for pa in range(12):
    for pb in range(12):
        if abs(pa-pb)==4: cnt+=1
assert cnt*60*math.factorial(7)==4838400
print('chk_p234_01 ok')
