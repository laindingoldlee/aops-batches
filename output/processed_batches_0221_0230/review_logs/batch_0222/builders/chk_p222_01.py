import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(1)
# 1784477 temperature
assert 20+F(140,100)*215==321
# 1784575 QX = QR in the figure configuration and random isosceles triangles
for h in [2,3,6,10]:
    Q=np.array([-1.,0]);R=np.array([1.,0]);P=np.array([0.,h])
    PR=np.linalg.norm(P-R);QR=2.0;XR=QR**2/PR
    X=R+(P-R)*XR/PR
    assert abs(np.linalg.norm(Q-X)-QR)<1e-9
# 1784545
assert F(3)*F(13,10)/F(3,2)==F(26,10)
# 1776535
import sympy as sp
x,y=sp.symbols('x y')
assert sp.expand((x+y)**2-(x**2+2*x*y+y**2))==0 and sp.expand((x+y)*(x-y)-(x**2-y**2))==0
# 1784532
s=F(180)*5/12; assert s==75 and 2*(s+s/5)==180 and s*s==5625
# 1784164 parallelogram cases
for a,xx in [(28,52),(52,28)]:
    assert (a+xx)**2+18**2==82**2 and (xx-a)**2+18**2==30**2
assert min(18*28,18*52)==504
# 1784280
assert sum((-1)**k*k for k in range(1,25))==12
odd=list(range(1,104,2)); assert len(odd)==52
assert 3*sum(-v if i%4==3 else v for i,v in enumerate(odd))==3822
# 1784100 Heronian minimum
best=None
for a in range(1,18):
    for b2 in range(a,18):
        if a+b2<=17: continue
        v=(a+b2+17)*(a+b2-17)*(17+a-b2)*(17-a+b2)
        r=math.isqrt(v)
        if r*r==v and r%4==0:
            A=r//4
            best=A if best is None else min(best,A)
assert best==36
# 1783820 Harry
good=0;tot=0
for S4 in itertools.combinations(range(1,10),4):
    tot+=1
    if any(math.isqrt(p+q)**2==p+q for p,q in itertools.combinations(S4,2)): good+=1
assert tot==126 and F(good,tot)==F(97,126)
# 1783710
v=max(-a+math.sqrt(4-a*a) for a in np.linspace(-2,2,400001))
assert abs(v-2*math.sqrt(2))<1e-8
# 1783346 trapezoid coordinates
D=(0,0);C=(8,0);A=(F(9,5),F(12,5));B=(F(24,5),F(12,5))
d2=lambda P,Q:(P[0]-Q[0])**2+(P[1]-Q[1])**2
assert d2(A,B)==9 and d2(B,C)==16 and d2(C,D)==64 and d2(D,A)==9
assert (3+8)*F(12,5)/2==F(66,5)
# 1783613
for h in [1,3,7]:
    Ap=np.array([0.5,h]);Dp=np.array([0.,0]);Bp=np.array([3.5,h]);Cp=np.array([4.,0])
    t=15/31;Fp=Ap+t*(Dp-Ap);Ep=Bp+t*(Cp-Bp)
    assert abs(Fp[1]-Ep[1])<1e-12 and abs((Ep[0]-Fp[0])-108/31)<1e-12
# 1783549 dice: brute force minimum per die type over all 24 orientations of a standard die
# faces: opposite pairs (1,6),(2,5),(3,4); a vertex is a choice of one face from each pair
assert min(a+b+c for a in (1,6) for b in (2,5) for c in (3,4))==6
adj=[(p,q) for p in range(1,7) for q in range(1,7) if p!=q and p+q!=7]
assert min(p+q for p,q in adj)==3
assert 8*6+12*3+6*1==90
# 1783551: example polynomials degrees 10+2k have exactly 10 sign changes
xs=np.linspace(0.5,10.5,200001)+1.234e-6
for k in range(3):
    vals=np.prod([xs-i for i in range(1,11)],axis=0)*(xs**2+1)**k
    assert np.sum(np.sign(vals[1:])!=np.sign(vals[:-1]))==10
# 1783256
assert sum(1 for n in range(100,1000) if n%2==0 and n//100+(n//10)%10==n%10)==20
# 1783520
def v(p,n):
    e=0
    while n: n//=p; e+=n
    return e
f=math.factorial(2018); n=0
while f%2021**(n+1)==0: n+=1
assert n==42==min(v(43,2018),v(47,2018))
# 1772864
a,b,c=sp.symbols('a b c')
assert sp.expand(a**3*(b-c)**3+b**3*(c-a)**3+c**3*(a-b)**3-3*a*b*c*(a-b)*(b-c)*(c-a))==0
p=a**4+b**4+c**4-2*(a*a*b*b+b*b*c*c+c*c*a*a)
assert sp.expand(p-(a-b-c)*(a-b+c)*(a+b-c)*(a+b+c))==0
for _ in range(1000):
    A_,B_,C_=sorted(random.uniform(0.1,10) for _ in range(3))
    if A_+B_>C_: assert float(p.subs({a:A_,b:B_,c:C_}))<0
# 1783316
sols=[(x_,y_) for x_ in range(-30,31) for y_ in range(-30,31) if 3*x_+5*y_==1]
assert all((x_-2)%5==0 and (y_+1)==-3*((x_-2)//5) for x_,y_ in sols) and len(sols)>5
# 1783275
for pr in [2,3,5,7,11,13,17,19,23]:
    assert all(math.comb(pr,k)%pr==0 for k in range(1,pr))
assert math.comb(4,2)%4!=0
# 1780436
assert sum(2*k-1 for k in range(1,11))==100==(50//5)**2
# 1783141
an=lambda n:F(25*n*n-45*n+22,2)
assert [an(n) for n in range(1,6)]==[1,16,56,121,211]
# 1783108
nn,m=8,89
assert F(nn*m+98,nn+1)==m+1 and F(nn*m+168,nn+2)==m+1-2 and nn+2==10
# 1726380
w=6*math.tan(math.pi/6); assert abs(w-2*math.sqrt(3))<1e-12
xp=w/math.tan(math.pi/3); assert abs(xp-2)<1e-12
small,mid,big=0.5*xp*w,0.5*(6-xp)*w,0.5*6*w
full=6*w
K=full+small;R=full+mid;M=big
assert abs(K*(R-M)-420)<1e-9
print('chk_p222_01 ok')
