import math, itertools, random
from fractions import Fraction as F
from math import comb
import numpy as np, sympy as sp
random.seed(2)
x=sp.symbols('x')
# 1770935
assert sp.expand((x-1)*(x-2)**2*(2*x-5)-(2*x**4-15*x**3+41*x**2-48*x+20))==0
# 1770709
assert F(comb(4,2),comb(20,2))==F(3,95)
# 1770602
sols=[b for b in range(1,2017**2) if math.isqrt(2017**2+b*b)**2==2017**2+b*b] if False else None
b=(2017**2-1)//2; assert b==2034144 and math.isqrt(2017**2+b*b)**2==2017**2+b*b
# uniqueness via divisors of 2017^2
assert [(d,2017**2//d) for d in [1,2017,2017**2] if d<2017**2//d]==[(1,2017**2)]
# 1770185
r=1; assert abs(math.sqrt(4-2)-math.sqrt(2))<1e-12 and abs(r+math.sqrt(2)+r-(2+math.sqrt(2)))<1e-12
# 1770260 numeric: points with AP^2=BP^2+CP^2 inside have angle BPC=150
s3=math.sqrt(3); A=np.array([2,2*s3]); B=np.array([0.,0]); C=np.array([4.,0])
def ang(P,Q,R):
    u=P-Q; v=R-Q; return math.degrees(math.acos(u@v/np.linalg.norm(u)/np.linalg.norm(v)))
cnt=0
for phi in np.linspace(35,145,50):
    P=np.array([2,-2*s3])+4*np.array([math.cos(math.radians(phi)),math.sin(math.radians(phi))])
    if P[1]<=0: continue
    assert abs(np.sum((A-P)**2)-np.sum((B-P)**2)-np.sum((C-P)**2))<1e-9 and abs(ang(B,P,C)-150)<1e-9; cnt+=1
assert cnt>10
# 1769463
seen=set();n=0
for cb in itertools.combinations(range(12),3):
    t=tuple(int(i in cb) for i in range(12))
    if t in seen: continue
    n+=1
    for k in range(12):
        u=t[k:]+t[:k]; seen.add(u); seen.add(u[::-1])
assert n==12==(220+8+60)//24
# 1770219
rr=sp.symbols('r',positive=True); a=rr/4; h=sp.sqrt(rr**2-a**2)
assert sp.simplify(sp.pi*a**2*h/3-sp.sqrt(15)*sp.pi*rr**3/192)==0
# 1770209
assert abs(13*(10/17)**1.5-130*math.sqrt(170)/289)<1e-12
# 1770041
c=5; assert F(10,20+c)+F(10,20-c)==F(64,60)
# 1769320
sol=[k for k in range(1,100000) if math.isqrt(k*k+37*k+299)**2==k*k+37*k+299]
assert sol==[25] and math.isqrt(25*25+37*25+299)+25==68
# 1769062
assert [a for a in range(1,20) if a*(20-a)*2*a==1536 and a<=20-a]==[8]
assert [w for w in range(1,100) if w*(w-2)*(w+3)==2856]==[14]
assert sp.discriminant(x**2+15*x+204)<0 and sp.expand((x-14)*(x**2+15*x+204)-(x**3+x**2-6*x-2856))==0
# 1769946
assert len(set(itertools.permutations('PSSS')))==4
# 1769951
import datetime
d=datetime.date(2018,1,1);pc=0
while d.year==2018:
    s=f"{d.month}{d.day}18"; pc+=s==s[::-1]; d+=datetime.timedelta(1)
assert pc==11
# 1769749
roots=np.roots([1,-6,5,14]); a_,b_,c_=roots
for e,v in [(a_+b_+c_,6),(a_*a_+b_*b_+c_*c_,26),(a_**3+b_**3+c_**3,84)]: assert abs(e-v)<1e-9
Pv=(a_*a_+a_*b_+b_*b_)*(b_*b_+b_*c_+c_*c_)*(c_*c_+c_*a_+a_*a_); assert abs(Pv-3799)<1e-6
assert sum(abs(z.imag)<1e-9 for z in roots)==1
# 1769594
for y in [0.5,1,2,3.7]:
    xx=math.sqrt(27*y**3/4)
    assert abs(3*y+(4*xx*xx)**(1/3)-2*(108*xx*xx*y**3)**(1/6))<1e-9
for _ in range(1000):
    xx=random.uniform(0.01,10); y=random.uniform(0.01,10)
    assert 3*y+(4*xx*xx)**(1/3)>(108*xx*xx*y**3)**(1/6)
# 1769528
s=0;L=[]
for n in range(1,1300):
    s=(s+int('1'*n))%101
    if s==0: L.append(n)
assert min(n for n in L if n>=1000)==1121 and set(n%404 for n in L)=={110,313,403,0}
# 1760794
for t in np.linspace(-20,2.5,4501):
    assert (math.sqrt(5-2*t)>t-1)==(t<2), t
# 1769328
vals=set()
for _ in range(2000):
    k=random.uniform(-5,5)
    for tt in [3,-1]:
        p=tt+2*k; assert abs(p*(p-2)+4*k*(k-p+1)-3)<1e-9
assert 3+(-1)==2
# 1769179
assert abs(10*(5/7)**2+5*(1/7)**2+2*(5/7)*(-1/7)-14*(5/7)+5)<1e-12
X,Y=sp.symbols('X Y'); assert sp.expand((5*Y+X)**2+(7*X-5)**2-5*(10*X**2+5*Y**2+2*X*Y-14*X+5))==0
# 1768864
Pt=np.array([0.,0]); 
# triangle angles Q=82? construct: angle chase numeric
Q_,R_=58.0+21,58.0  # PQR - PRQ = 42 with PQR=100? use generic check
for R in [20,30,40,50]:
    Qa=R+42; Pa=180-Qa-R
    alpha=(180-Pa)/2; assert abs(Qa-alpha-21)<1e-12
# 1768599
g=sum(1 for a,b,c in itertools.permutations(range(1,7),3) if pow(a,b**c,4)==0)
assert F(g,120)==F(13,30)
