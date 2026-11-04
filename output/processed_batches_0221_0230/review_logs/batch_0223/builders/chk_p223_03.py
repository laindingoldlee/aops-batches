import math, itertools, random
from fractions import Fraction as F
import sympy as sp
random.seed(3)
# 1775470
assert F(2,1)/(F(1,2)+F(1,7))==F(28,9)
# 1772259
s1=[(m,n) for m in range(-200,200) for n in range(-2000,2000) if m*n+n+10==(m-1)**2]
assert len(s1)==8 and set(s1)=={(0,-9),(-2,1),(1,-5),(-3,-3),(2,-3),(-4,-5),(5,1),(-7,-9)}
cnt=0
for b1 in range(11):
  for b2 in range(11-b1):
    b3=10-b1-b2
    for r1 in range(6):
      for r2 in range(6-r1):
        r3=5-r1-r2
        if b1>r1 and b2>r2 and b3>r3: cnt+=1
assert cnt==126==math.comb(7,2)*math.comb(4,2)
t=8/math.sqrt(15); a,b,c=4*t,3*t,2*t; s=(a+b+c)/2; K=math.sqrt(s*(s-a)*(s-b)*(s-c))
assert abs(2*K/a-3)<1e-12 and abs(2*K/b-4)<1e-12 and abs(2*K/c-6)<1e-12 and abs(a+b+c-24*math.sqrt(15)/5)<1e-12
# 1772259 q04
A=(0,1);B=(1,1);C=(1,0);D=(0,0); E=(1,1/math.sqrt(3)); x=math.sqrt(3)/(math.sqrt(3)+1); Fp=(x,x/math.sqrt(3))
dist=lambda P,Q: math.hypot(P[0]-Q[0],P[1]-Q[1])
assert abs(dist(D,Fp)-dist(B,Fp))<1e-12 and abs(dist(E,Fp)-dist(B,E))<1e-12
assert abs(dist(D,Fp)+dist(Fp,E)-dist(D,E))<1e-12
u=(D[0]-Fp[0],D[1]-Fp[1]); v=(A[0]-Fp[0],A[1]-Fp[1])
assert abs(math.degrees(math.acos((u[0]*v[0]+u[1]*v[1])/math.hypot(*u)/math.hypot(*v)))-75)<1e-9
v_=10*3195*4949; assert sp.ntheory.digits(v_,4)[-3:]==[2,1,2]
# 1775342
d=7.0; assert abs((1+(d+5)/10)-(d/10)-1.5)<1e-12
# 1593299
assert sum(1 for k in range(1,31) if math.gcd(k,30)==1)==8
# 1605801
med=lambda L: (sorted(L)[2]+sorted(L)[3])/2
vals=[med([1.7,1.1,1.4,2.1,2.3,s/100]) for s in range(0,400)]
assert abs(max(vals)-min(vals)-0.35)<1e-9
# 1774417
assert 600+650+750==2000 and F(5,6)*600==F(10,13)*650==F(2,3)*750==500
# 1774061
N=200000; hits=sum(1 for _ in range(N) if (lambda x,y,z: x+y<=1 and y+z<=1 and x+z<=1)(random.random(),random.random(),random.random()))
assert abs(hits/N-0.25)<0.005
X=sp.symbols('x'); assert sp.integrate((1-X)**2,(X,0,1))-sp.integrate((1-2*X)**2/2,(X,0,sp.Rational(1,2)))==sp.Rational(1,4)
sols=[]
for road in range(1,6):
    st=[road==1,road!=3,road==5,road!=1,road==2,road==4]
    if sum(st)==1: sols.append((st.index(True)+1,road))
assert sols==[(4,3)]
U={}
for i in range(1,7):
  for j in range(1,7): U[i+j]=U.get(i+j,0)+F(i*j,441)
assert sum(U[u]*F(1,36) for u in U for i in range(1,7) for j in range(1,7) if u>i+j)==F(365,567)
assert sp.expand((X-2)*(X-4)*(X-6)*(X-8)*(X-10)).subs(X,1)==-945
assert sum(1 for n in range(1,101) if math.isqrt(1+4*n)**2==1+4*n)==9
# 1771790
assert sum({p*q for p in range(-15,16) for q in range(-15,16) if p!=q})==-1175
# 1771792
ds=lambda n: sum(map(int,str(n)))
cool=[n for n in range(100,1000) if ds(n)==ds(11*n)]
assert sum(cool)==36621 and len(cool)==54
assert set(cool)=={n for n in range(100,1000) if ds(n)==18}-{909}|{999}
assert sum((a+1)*(F(189,2)*a+99) for a in range(1,10))==36531
# 1774078
for n in range(2,300):
    f=sp.factorint(math.factorial(n)); assert math.gcd(*f.values())==1 if len(f)>1 else min(f.values())==1
# 1773801
assert [(a,b,c,d) for a in range(1,4) for b in range(1,130) for c in range(b,130) for d in range(c,130) if b**3+c**3+d**3-5==2019**a]==[(1,8,8,10)]
assert {(x**3+y**3+z**3)%9 for x in range(9) for y in range(9) for z in range(9)}=={0,1,2,3,6,7,8}
# 1773745
P=(F(12,7),F(30,7)); Q=(F(9,4),0)
for (x,y) in (P,Q): assert 8*x+y==18 and x+y+(60-5*x-12*y)/13==6
assert 5*P[0]+12*P[1]==60 and (P[0]+Q[0])/2==F(111,56) and math.gcd(111,56)==1
for _ in range(1000):
    lam=random.random(); x=float(P[0])+lam*float(Q[0]-P[0]); y=float(P[1])+lam*float(Q[1]-P[1])
    assert abs(x+y+(60-5*x-12*y)/13-6)<1e-9
# 1773840
assert [int(str(2**k)[::-1]) for k in range(4,11)]==[61,23,46,821,652,215,4201]
# 1773603
assert math.factorial(8)//(6*6*2)==560
# 1772890
assert sum(F(1,k*k) for k in range(1,101))>F(14,10) and 1+F(1,2)-F(1,101)>F(149,100)
# 1773142
m,n,a=sp.symbols('m n a',positive=True)
for av in range(1,5):
    e=m**(2*av+1)-2*n**(3*av-1)-m*n+2*m**(2*av)*n**(3*av-2)
    assert sp.expand(e-(m**(2*av)-n)*(m+2*n**(3*av-2)))==0
