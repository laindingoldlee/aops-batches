import math, itertools, random
from fractions import Fraction as F
import sympy as sp
# 1777627
sols=sorted((a,b,c) for a in range(1,61) for b in range(1,61) for c in range(1,61) if 5*a+3*b+4*c-a*b*c==19)
spor=[s for s in sols if not (s[2]==1 and (s[0]==3 or s[1]==5))]
assert sorted(spor)==sorted([(1,6,2),(5,2,2),(2,1,3),(1,2,4),(1,3,5),(8,1,6),(6,1,7),(5,1,9)])
assert all(s[2]==1 and (s[0]==3 or s[1]==5) for s in sols if s not in spor)
for a in range(-5,6):
    for b in range(-5,6):
        for c in range(-5,6): assert (a*c-3)*(b*c-5)-(c-1)*(4*c-15)==c*(a*b*c-5*a-3*b-4*c+19)
# 1777493
assert sum(1 for y in range(5) for z in range(3) if 5*y+10*z<=20)==9
# 1777483
assert 5**2+12**2==13**2 and 13==17-4
# 1773488
assert [k for k in range(1000,1200) if str(k*k).startswith('1234') and len(str(k*k))==7]==[1111]
# 1777171
men=range(5); women=range(5,11)
cnt=0
for m in itertools.permutations(men,2):
    for w in itertools.permutations(women,2):
        rest=[p for p in range(11) if p not in m and p not in w]
        cnt+=len(list(itertools.permutations(rest,2)))
assert cnt==25200 and 10*15*21*8==25200
# 1777424 cube colourings
opp={0:1,1:0,2:3,3:2,4:5,5:4}
adj=[(i,j) for i in range(6) for j in range(i+1,6) if opp[i]!=j]
def comp(p,q): return tuple(p[q[i]] for i in range(6))
gens=[(2,3,1,0,4,5),(0,1,5,4,2,3),(4,5,2,3,1,0)]
G={tuple(range(6))}; fr=[tuple(range(6))]
while fr:
    g=fr.pop()
    for h in gens:
        k=comp(g,h)
        if k not in G: G.add(k); fr.append(k)
assert len(G)==24
# check they are rotations: preserve opposite pairs and orientation (determinant via face normals)
nrm={0:(0,0,1),1:(0,0,-1),2:(0,1,0),3:(0,-1,0),4:(-1,0,0),5:(1,0,0)}
for g in G:
    M=[nrm[g[f]] for f in (5,2,0)]
    det=M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    assert all(opp[g[i]]==g[opp[i]] for i in range(6)) and det==1
cols=[c for c in itertools.product(range(6),repeat=6) if all(c[i]!=c[j] for i,j in adj)]
seen=set(); orb={}
for c in cols:
    if c in seen: continue
    k=len(set(c)); orb[k]=orb.get(k,0)+1
    for g in G: seen.add(tuple(c[g[i]] for i in range(6)))
assert orb=={6:30,5:90,4:90,3:20} and sum(orb.values())==230
# 1777119
def sp_(n): return sum(d for d in range(1,n) if n%d==0)
assert [sp_(math.factorial(k))>math.factorial(k) for k in range(1,5)]==[False,False,False,True]
# 1777120
assert F(5,math.comb(10,2))==F(1,9)
# 1777122
seen=set(); cl=0
for c in itertools.combinations(range(6),2):
    s=frozenset(c)
    if s in seen: continue
    cl+=1
    for r in range(6): seen.add(frozenset((x+r)%6 for x in c))
assert cl==3
# 1775465
x=6+3*math.sqrt(3); y=6-3*math.sqrt(3); assert abs(x*y-9)<1e-12 and abs(x+y-12)<1e-12 and abs(x-y-6*math.sqrt(3))<1e-12
# 1161680
X=sp.symbols('x'); P=X**4-3*X**3+2*X**2+5*X-1
q,r=sp.div(P,X**2-X-2); assert sp.expand(q-(X**2-2*X+2))==0 and sp.expand(r-(3*X+3))==0
assert sp.div(P,X-2)==(X**3-X**2+5,9) and sp.div(X**3-X**2+5,X+1)==(X**2-2*X+2,3)
# 1776896
assert all(1-sum(F(9,10**k) for k in range(1,n+1))==F(1,10**n) for n in range(1,20))
# 1776603
for a,b in [((-1+math.sqrt(21))/2,(-1-math.sqrt(21))/2),((-1-math.sqrt(21))/2,(-1+math.sqrt(21))/2)]:
    assert abs(a**3-6*b**2+41)<1e-9
# 1775616
assert sum(1 for t in range(1,180) if 8*math.sin(math.radians(t))<=4+1e-12)==60
# 1776391
for a in [x/10 for x in range(-50,51)]:
    for b in [x/10 for x in range(-50,51)]:
        if abs(a*a*b*b+a*a+b*b+10*a*b+16)<1e-9: assert abs(a*a+b*b-8)<1e-9
f2=lambda x: -7 if x<-3 else (2*x-1 if x<=4 else 7)
f3=lambda x: -6 if x<-2 else (2*x-2 if x<-1 else (4*x if x<1.5 else 6))
for k in range(-1000,1001):
    x=k/100
    assert abs(abs(x+3)-abs(4-x)-f2(x))<1e-9 and abs(abs(x+1)-abs(2*x-3)+abs(x+2)-f3(x))<1e-9
# 1776515
assert [N for N in range(1,3000) if N%32==30 and N%58==44]==[798,1726,2654]
# 1329488
p=F(1)
for k in range(2,500): p*=1+F(1,k)
assert p==250
# 1776390
a,xx=sp.symbols('a x')
for n in range(1,7):
    f=sp.prod([1+a**k*xx for k in range(1,n+1)])
    assert sp.expand((1+a*xx)*f.subs(xx,a*xx)-(1+a**(n+1)*xx)*f)==0
    coeffs=sp.Poly(sp.expand(f),xx).all_coeffs()[::-1]
    for i in range(1,n+1):
        Ai=a**(i*(i+1)//2)*sp.prod([(a**(n-j+1)-1)/(a**j-1) for j in range(1,i+1)])
        assert sp.simplify(coeffs[i]-Ai)==0
# 1776426
assert 3**2+1**2==10 and 3**2+(1-3)**2==13 and (5-3)**2+1==5 and 3*3+5*1<15
# 1776440
xs=sp.Poly(X**5+X**2+1).nroots(n=30)
pr=1
for r_ in xs: pr*=(r_**2-2)
assert abs(complex(pr)-(-23))<1e-12
# 1776388
assert 4*10==2**2+6**2 and (2*3-0*1)==6 and 2*1+0*(-3)==2
for _ in range(2000):
    t=random.uniform(0,2*math.pi); a_,b_=2*math.cos(t),2*math.sin(t)
    s=random.choice([1,-1]); phi=math.acos(2/(2*math.sqrt(10)))*s
    c_,d_=math.sqrt(10)*math.cos(t+phi),math.sqrt(10)*math.sin(t+phi)
    assert abs(a_*c_+b_*d_-2)<1e-9 and abs(abs(a_*d_-b_*c_)-6)<1e-9
# 1774223 circumcentre equidistant
A_=(1,3.2);B_=(0,0);C_=(5,0)
ox=2.5; oy=(A_[0]**2+A_[1]**2-2*ox*A_[0])/(2*A_[1])
assert abs(math.hypot(ox-A_[0],oy-A_[1])-math.hypot(ox,oy))<1e-12 and abs(math.hypot(ox-5,oy)-math.hypot(ox,oy))<1e-12
# 1775548
sq=lambda v: v>=0 and math.isqrt(v)**2==v
assert sorted(n for n in range(-2000,2001) if n*n!=1 and (n**4-1441)%(n*n-1)==0 and sq((n**4-1441)//(n*n-1)))==[-9,9]
assert [n for n in range(2,38) if 1440%(n*n-1)==0]==[2,3,4,5,7,9,11,17,19]
# 1774742
assert [2*n-2+(1//n) for n in range(1,7)]==[1,2,4,6,8,10]
