import math, itertools, random
from fractions import Fraction as F
random.seed(3)
# 1790978
best=min(max(a[i]+a[(i+1)%9]+a[(i+2)%9] for i in range(9)) for p in itertools.permutations(range(2,10)) for a in [(1,)+p])
a=[1,5,8,2,6,7,3,4,9]; sums=[a[i]+a[(i+1)%9]+a[(i+2)%9] for i in range(9)]
assert best==16 and max(sums)==16 and sums==[14,15,16,15,16,14,16,14,15]
# 1790901
w=150; assert w+60==F(14,10)*w and F(210,240)==F(7,8)
# 1790697 brute force small n, and formula
def solve(n):
    out=[]
    for t in itertools.product([0,1],repeat=n):
        if all((sum(t[:i])>sum(1-x for x in t[i+1:]))==(t[i]==0) for i in range(n)): out.append(sum(t))
    return out
for n in range(1,14): assert solve(n)==[(n+1)//2]
n=2015
def okt(t):
    for i in range(n):  # 0-indexed position i; thieves are 0..t-1
        thieves_front=min(i,t); knights_behind=n-max(i+1,t)
        if (thieves_front>knights_behind)!=(i>=t): return False
    return True
assert [t for t in range(n+1) if okt(t)]==[1008]
# 1790898
assert F(2,5)-F(1,10)==F(3,10)
# 1790151 numeric
for _ in range(50):
    P=[complex(random.uniform(-5,5),random.uniform(-5,5)) for _ in range(3)]
    area=lambda u,v,w: abs(((v-u).conjugate()*(w-u)).imag)/2
    A_,B_,C_=P; med=[abs((B_+C_)/2-A_),abs((A_+C_)/2-B_),abs((A_+B_)/2-C_)]
    s=sum(med)/2; hb=math.sqrt(max(0,s*(s-med[0])*(s-med[1])*(s-med[2])))
    assert abs(hb/area(*P)-0.75)<1e-9
# 1790652
assert 3*26+6==84 and 84+26==110
# 1786655
sol=[(N,p) for N in range(1,1000) for p in range(1,42) if N-p+1>=1 and p*(2*N-p+1)//2+(42-p)*(43-p)//2==2018 and (p*(2*N-p+1))%2==0]
assert sol==[(265,5)]
# 1790194
assert abs(sum(n/2**n for n in range(1,200))-2)<1e-12
# 1790252
import sympy as sp
x,y,z=sp.symbols('x y z'); assert sp.Poly(sp.expand((x+2*y-z)**8),x,y,z).coeff_monomial(x**3*y**2*z**3)==-2240
# 1789225
tos=lambda n: ''.join(chr(65+int(d)) for d in str(n))
L=sorted(tos(n) for n in range(1,10000)); assert L.index('CHAI')==1899==1111+1+777+1+1+8
# 1788973
u=F(3,5); v2=81-u*u; assert (u-10)**2+v2==169 and (5-u)**2+v2==100
P=(3,-1/math.sqrt(3)); d=[4,6,9,10,8,5]
for k in range(6):
    n_=(math.cos(math.radians(60*k)),math.sin(math.radians(60*k)))
    assert abs(7-(P[0]*n_[0]+P[1]*n_[1])-d[k])<1e-12
s_=F(42)/ (3) ; assert abs(42/(3*math.sqrt(3))-14*math.sqrt(3)/3)<1e-12
# hexagon area check: (3 sqrt3/2) s^2 == 21 s
s=14/math.sqrt(3); assert abs(1.5*math.sqrt(3)*s*s-21*s)<1e-9
# 1760605
tot=sum(sum(c) for c in itertools.combinations(range(1,21),5)); assert F(tot,math.comb(20,5))==F(105,2)
# 1789216
def nd(m,b):
    c=0
    while m: m//=b; c+=1
    return c
assert sum(1 for m in range(1,10**6) if nd(m,5)==nd(m,8))==195
# 1789696
s=math.sin(math.pi/8); assert abs(s-math.sqrt(2-math.sqrt(2))/2)<1e-15
r=(1+s)/(1-s); assert abs(r-2.240)<0.001
d0=1.0; d1=d0*r; assert abs((d1-d0)-(s*d0+s*d1))<1e-12
# 1788599
for _ in range(200):
    p,q=random.uniform(-5,5),random.uniform(-5,5); xm=-(p+q)/2; assert (xm+p)*(xm+q)<0
# 1731835
assert 2*23+3*6+11==75
# 1789625: brute force axis-parallel 2-cubes in 3-cube with positions on a fine grid
pos=[i/4 for i in range(5)]
cubes=list(itertools.product(pos,repeat=3))
ov=lambda c1,c2: all(abs(c1[i]-c2[i])<2 for i in range(3))
assert all(ov(c1,c2) for c1 in cubes for c2 in cubes)
# 1789074
nums=[100*a+10*b+c for a,b,c in itertools.permutations([2,3,5,7],3)]
assert len(nums)==24 and F(sum(nums),24)==F(1887,4)
# 1789107
for A in range(1,301):
    for B in range(1,301):
        if (A*A+A*B+1)%(B*B+A*B+1)==0: assert A==B
# 1789385
assert len(str(2**30))==10
# 1789434
assert math.floor(F(2012**3,2008*2010)-F(2008**3,2010*2012))==16
# 1789337
a,b,c=2017**2017,2018**2018,2019**2019
assert (b+1)**2<(a+1)*(c+1) and a*c>b*b
for m in range(2,60):
    a,b,c=(m-1)**(m-1),m**m,(m+1)**(m+1); assert a*c>b*b
# 1789389
assert min(n for n in range(1,2000) if (n*(n+1)//2)%500==0)==375
