import math, itertools, random
from fractions import Fraction as F
from math import comb, gcd
import numpy as np
random.seed(3)
# 1768394
assert min(x for x in range(1,200) if x%3==2 and x%5==3 and x%7==2)==23
# 1768345
assert 3**20>53**3 and [n for n in range(-400,400) if 3**20<n*n<53**3]==[]
assert sum(n for n in range(-400,400) if 3<n*n<53**3)==0
# 1752262 P3
assert min(N*2//5+N*3//4-N for N in range(20,401,20))==3
# 1767081: random check that only swaps work
for _ in range(200):
    a,b=random.randint(-9,9),random.randint(-9,9)
    for c in range(-20,21):
        d=a+b-c
        if c*d==a*b: assert (c,d) in [(a,b),(b,a)]
# 1767962
g=lambda t: math.sqrt(3+t)
xs=np.linspace(0,10,200001); f=np.sqrt(3+np.sqrt(3+np.sqrt(3+xs)))-xs
assert sum(1 for i in range(len(xs)-1) if f[i]*f[i+1]<0 or f[i]==0)==1
r=(1+math.sqrt(13))/2; assert abs(g(g(g(r)))-r)<1e-12
# 1767197
x=-1; assert F(1)-F(1,1-x)==F(1,1-x)
# 1768268
med=lambda s: (sorted([1.7,1.1,1.4,2.1,2.3,s])[2]+sorted([1.7,1.1,1.4,2.1,2.3,s])[3])/2
ms=[med(s) for s in np.linspace(-5,5,10001)]
assert abs(max(ms)-min(ms)-0.35)<1e-9
# 1665584
for a in range(-15,16,2):
    for b in range(-15,16,2):
        for c in range(-15,16,2):
            for p in range(-30,31):
                for q in range(1,31):
                    assert a*p*p+b*p*q+c*q*q!=0
# 1767629
assert pow(3,3**27,1000)==387==pow(3,87,1000) and pow(3,27,100)==87 and pow(3,100,1000)==1
# 1768109
for a,b in [(9,4),(5,2),(7,3)]:
    h=math.sqrt(a*b); assert abs(-a*b+h*h)<1e-9
# 1767722
A=(0,0);D=(8,14);E=(14,6); assert abs(D[0]*E[1]-E[0]*D[1])/2==74
assert math.dist((6,0),(0,8))==10 and math.dist((0,8),D)==10 and math.dist(D,E)==10 and math.dist(E,(6,0))==10
# 1766250
assert sorted({8*x+5*(18-x) for x in range(19)})==list(range(90,145,3)) and 53 not in {8*x+5*(18-x) for x in range(19)}
assert [18-x for x in range(19) if 8*x+5*(18-x)==117]==[9]
# 1767658
assert F(3,6)==F(1,2) and 4+3-1==6
# 1767474
S=sum(F(2*k-1,2**k) for k in range(1,24)); assert S==F(25165775,8388608)==3-F(49,2**23)
# 1766947
T1=[F(9,2),F(6),F(8)]; T2=[F(6),F(8),F(32,3)]
assert all(T2[i]/T1[i]==F(4,3) for i in range(3))
def cosang(a,b,c): return (b*b+c*c-a*a)/(2*b*c)
assert sorted(cosang(*T1[i:]+T1[:i]) for i in range(3))==sorted(cosang(*T2[i:]+T2[:i]) for i in range(3))
assert T1[0]+T1[1]>T1[2] and T2[0]+T2[1]>T2[2]
# 1767337 simulate
P=np.array([[0,0],[1,0],[1,1],[0,1]],float); t=0; dt=1e-5
while np.linalg.norm(P[1]-P[0])>1e-3:
    V=np.roll(P,-1,axis=0)-P; V/=np.linalg.norm(V,axis=1)[:,None]; P=P+dt*V; t+=dt
assert abs(t-1)<2e-3
# 1766580 Pick example
pts=[(i,j) for i in range(7) for j in range(5)]
def inside(p):
    (x1,y1),(x2,y2),(x3,y3)=(0,0),(6,0),(2,4); x,y=p
    d1=(x2-x1)*(y-y1)-(y2-y1)*(x-x1); d2=(x3-x2)*(y-y2)-(y3-y2)*(x-x2); d3=(x1-x3)*(y-y3)-(y1-y3)*(x-x3)
    return (d1>0 and d2>0 and d3>0), (d1>=0 and d2>=0 and d3>=0)
I=sum(inside(p)[0] for p in pts); T=sum(inside(p)[1] for p in pts)
assert I==7 and T==19 and gcd(6,0)+gcd(4,4)+gcd(2,4)==12
# 1767062
assert 28==2*12+4 and 60==5*12 and 28==2*14 and 60==4*14+4
# 1767069
assert abs(28*math.sqrt(36-7)/3-28*math.sqrt(29)/3)<1e-12 and abs(math.sqrt(36-14)-math.sqrt(22))<1e-12
# 1766655
V=6*8; E=V*3//2; assert V-E+26==2 and comb(48,2)-E-(12*2+8*9+6*20)==840
assert F(6,27)*F(5,6)+F(12,27)*F(2,6)==F(1,3)
# 1755096
for bv in [10,20,7]:
    m=F(bv,2)+3; d=m+5; k=3*d-10; assert 2*k==3*bv+28
# 1766801
for _ in range(200):
    c=random.uniform(1,5); kk=random.uniform(0.2,5); a=math.sqrt(kk)*c; p=random.uniform(-3,3); h=random.uniform(0.5,4)
    D=np.array([0,0]);C=np.array([c,0]);A=np.array([p,h]);B=np.array([p+a,h])
    num=np.sum((A-D)**2)-np.sum((B-C)**2); den=np.sum((A-C)**2)-np.sum((B-D)**2)
    if abs(den)<1e-6: continue
    # area ratio check
    O=A+(C-A)*(a/(a+c))
    ar=lambda P,Q,R: abs((Q-P)[0]*(R-P)[1]-(Q-P)[1]*(R-P)[0])/2
    assert abs(ar(A,O,B)/ar(C,O,D)-kk)<1e-9
    assert abs(num/den-(math.sqrt(kk)-1)/(math.sqrt(kk)+1))<1e-9
# 1766257
assert 2-56+114==60
s=13; K=math.sqrt(s*8*4*1); assert abs(K-4*math.sqrt(26))<1e-12 and round(K/s,2)==1.57
# 1766918
assert F(2*comb(22,9),comb(26,13))==F(11,115)==F(12*11*10,25*24*23)
# 1766302
import cmath
best=0
for (x_,y_) in [(1j,1j),(-1j,-1j),(-1+1j*math.sqrt(2),-1-1j*math.sqrt(2)),(-1-1j*math.sqrt(2),-1+1j*math.sqrt(2))]:
    assert abs(x_*x_+x_+1-y_)<1e-12 and abs(y_*y_+y_+1-x_)<1e-12; best=max(best,abs(x_*y_))
assert abs(best-3)<1e-12
# all solutions: resultant gives quartic in x
import sympy as sp
X=sp.symbols('X'); polyx=sp.expand((X**2+X+1)**2+(X**2+X+1)+1-X)
assert max(abs(complex(r)*(complex(r)**2+complex(r)+1)) for r in sp.Poly(polyx).nroots())<3+1e-9
# 1766872
t=10**2002; N=int('1'*2002+'5'*2002); m=(t+2)//3
assert (m-1)*(m+1)==N and (m-1)%2==1 and str(2*m)=='6'*2001+'8'
# 1766818
for _ in range(100):
    A=np.array([0.,0]); C=np.array([random.uniform(4,9),0]); D=np.array([random.uniform(0.5,3),random.uniform(1,4)])
    tt=np.sum(D**2)/C[0]; M=np.array([tt,0])
    if not 0<tt<C[0]: continue
    def angle(P,Q,R):
        u=P-Q;v=R-Q; return math.acos(u@v/np.linalg.norm(u)/np.linalg.norm(v))
    assert abs(angle(A,D,M)-angle(A,C,D))<1e-9
# 1766234
x=F(1,16); dg=[]
for _ in range(8): x*=5; dg.append(int(x)); x-=int(x)
assert dg==[0,1,2,4,0,1,2,4] and sum(dg[:4])==7
# 1766118
assert 2**8==256
# 1764346
ys=[(x+0,y) for x in range(1,60) for y in range(1,3000) if y!=x and y%x==0 and (y+1)%(x+1)==0 and (y+2)%(x+2)==0 and any(v%7==0 for v in (x,x+1,x+2))]
ymin=min(y for x,y in ys); assert ymin==174 and sum(map(int,str(ymin)))==12
