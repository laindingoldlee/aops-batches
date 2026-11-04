import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(3)
# 1716595
assert F(15,10)*F(72,10)/F(12,10)==9
# 1717421
assert math.isclose(5+2*math.sqrt(5),math.sqrt(45+20*math.sqrt(5)))
# 1717426
assert sum(1 for n in range(1000,10000) if sum(int(c)%2 for c in str(n))==2)==3375
# 1717419
assert sum(1 for p in itertools.permutations('013479',5) if p[0]!='0' and int(''.join(p))%5==0)==120
# 1717412
import sympy as sp
a,c,s,t=sp.symbols('a c s t',positive=True)
expr=sp.expand((a**2*s**2+c**2*t**2)*(a**2*t**2+c**2*s**2)-a**2*c**2*(s**2+t**2)**2-s**2*t**2*(a**2-c**2)**2)
assert expr==0
for _ in range(200):
    p,r=random.uniform(1,5),random.uniform(1,5); k=random.uniform(0.2,0.9)
    A=np.array([-p,0.]);C=np.array([k*p,0.]);B=np.array([0.,-r]);D=np.array([0.,k*r])
    aa=np.linalg.norm(B-A);bb=np.linalg.norm(C-B);cc=np.linalg.norm(D-C);dd=np.linalg.norm(A-D)
    m=np.linalg.norm(C-A);n=np.linalg.norm(D-B)
    assert math.isclose(m*m+n*n,(aa+cc)**2) and aa*cc<bb*dd
# 1717410
assert F(3000*3,10)/F(9,10)==1000 and F(18,10)*3000*F(4,10)/1000==F(216,100)
# 1717408
a_,b_,c_=8,6,15; assert F(a_,b_)==F(4,3) and F(b_,c_)==F(2,5) and F(3*a_-2*b_,b_+2*c_)==F(1,3)
# 1717403
assert F(6,36)==F(1,6) and F(7,35)==F(1,5) and 36+6==42
# 1717404
for _ in range(100):
    x=random.uniform(0.5,5); y=random.uniform(0.5,5)
    C0=np.array([0.,0.]);A=np.array([x,0.]);B=np.array([0.,y])
    M=(A+B)/2; u=B-A; H=A+np.dot(C0-A,u)/np.dot(u,u)*u
    Lp=(np.linalg.norm(B)*A+np.linalg.norm(A)*B)/(np.linalg.norm(A)+np.linalg.norm(B))
    ang=lambda P,Q: math.degrees(math.acos(np.dot(P,Q)/np.linalg.norm(P)/np.linalg.norm(Q)))
    assert math.isclose(ang(H,Lp),ang(Lp,M),abs_tol=1e-7)
# 1717359 q01
B=np.array([-5.5,0]);Cc=np.array([5.5,0]);A=np.array([0,1.]);E=np.array([-0.5,0]);D=np.array([0.5,0])
ang=lambda P,Q,R: math.degrees(math.acos(np.dot(P-Q,R-Q)/np.linalg.norm(P-Q)/np.linalg.norm(R-Q)))
assert math.isclose(ang(B,A,E),ang(E,A,D)) and math.isclose(ang(E,A,D),ang(D,A,Cc))
assert math.isclose(np.linalg.norm(Cc-A),5*math.sqrt(5)/2)
# 1717359 q02
g=lambda x: math.sqrt(2*x*x-3)+math.sqrt(3*x+5)
x0=-math.sqrt(6)/2
xs=list(np.linspace(-5/3,x0-1e-12,20001))+list(np.linspace(-x0+1e-12,50,20001))
assert min(g(x) for x in xs)>=math.sqrt(5-3*math.sqrt(6)/2)-1e-9 and 5+3+6+2==16
# 1717359 q03
def period(p):
    k=1
    while pow(10,k,p)!=1: k+=1
    return k
assert [p for p in range(3,10000) if all(p%d for d in range(2,int(p**.5)+1)) and p!=5 and period(p)==4]==[101]
# 1717359 q04
for K in [0.5,1,3,7.25]:
    for x in [10.0,100.0,1000.0]:
        f=(2*x*x+6*x+K)/(x+4); assert abs(f-(2*x-2))<(K+8)/(x+4)+1e-9
assert 2+6+1+4==13
# 1717359 q05
A=np.array([0,3.]);B=np.array([0,0.]);Cc=np.array([4,0.]);E=np.array([1.5,0]);D=np.array([12/25,66/25]);Fp=np.array([0.4,2.2]);O=np.array([2.75,2])
assert abs(D[0]/4+D[1]/3-1)<1e-12 and abs(2*Fp[0]+Fp[1]-3)<1e-12 and abs(Fp[0]-2/11*Fp[1])<1e-12 and abs(D[0]-2/11*D[1])<1e-12
r=np.linalg.norm(O-Cc)
for P in (D,E,Fp): assert math.isclose(np.linalg.norm(O-P),r)
assert math.isclose(np.linalg.norm(O-A)+np.linalg.norm(O-B),(math.sqrt(137)+math.sqrt(185))/4) and 137+185+4==326
assert math.isclose(ang(B,A,E),ang(E,A,Cc))
# 1710109 q01
fib=[1,1]
for _ in range(80): fib.append(fib[-1]+fib[-2])
assert all(math.gcd(fib[i],fib[i+1])==1 for i in range(80))
# 1710109 q02
for x in [10.,100.,1000.]:
    y=x*x/(3*x-2); assert abs(y-(x/3+2/9))<1/x
assert 0+F(2,3)+3-F(2,3)==3
# 1710109 q03 numeric Ceva for several BC
for x in [3.5,7,10,14.5]:
    Aa=np.array([0.,0.]);Bb=np.array([9.,0.]);cx=(36-x*x+81)/18;Cv=np.array([cx,math.sqrt(36-cx*cx)])
    Dm=(Bb+Cv)/2;Ff=Aa+(6/(6+x))*(Bb-Aa)
    def ext(P,Q,R,S):
        M=np.array([Q-P,R-S]).T; tt=np.linalg.solve(M,R-P); return P+tt[0]*(Q-P)
    P_=ext(Aa,Dm,Cv,Ff); Ee=ext(Bb,P_,Aa,Cv)
    assert math.isclose(np.linalg.norm(Ee-Aa),36/(x+6))
assert F(12,7)+4==F(40,7) and 40+7==47
# 1710109 q05
def phi(n):
    r=n;m=n;p=2
    while p*p<=m:
        if m%p==0:
            while m%p==0: m//=p
            r-=r//p
        p+=1
    if m>1: r-=r//m
    return r
L=[n for n in range(1,1000) if phi(phi(n))==20]; assert L==[67,69,92,134,138] and 134+138==272
assert [m for m in range(1,500) if phi(m)==20]==[25,33,44,50,66]
# 1717292
assert sum(1 for a in range(101) for b in range(a+1) for c in range(101) if abs(a-b)==c and abs(b-c)==a)==201
# 1715899
for _ in range(100):
    A,B,Cc=[np.array([random.uniform(-5,5),random.uniform(-5,5)]) for _ in range(3)]
    D=(B+Cc)/2; Sm=(A+D)/2
    M=np.array([Sm-Cc,A-B]).T; tt=np.linalg.solve(M,A-Cc); E=Cc+tt[0]*(Sm-Cc)
    assert math.isclose(np.linalg.norm(B-E),2*np.linalg.norm(A-E),rel_tol=1e-7)
# 1715029
assert F(5553,5557)>F(6664,6669)
# 1715574
def nd(n): return sum(1 for d in range(1,n+1) if n%d==0)
assert all(nd(n)!=14 or n==192 for n in range(12,20000,12)) and nd(192)==14
# 1716607
assert 5+1==6 and (1-(-1))/(0-(-2))==1
# 1716924
best=0
N=300
for i in range(N+1):
    for j in range(N+1-i):
        a=i/N;b=j/N;c=1-a-b
        best=max(best,a*b+b*c+c*a-3*a*b*c)
assert abs(best-0.25)<1e-9
# 1716960
for _ in range(50):
    B=np.array([0.,0.]);Cc=np.array([3.,0.]);A=np.array([random.uniform(-2,4),random.uniform(0.5,4)])
    D=np.array([1.,0.]);E=(A+Cc)/2
    M=np.array([D-A,B-E]).T; tt=np.linalg.solve(M,B-A); Fp=A+tt[0]*(D-A)
    area=lambda *P: abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[(i+1)%len(P)][0]*P[i][1] for i in range(len(P))))/2
    assert math.isclose(area(B,D,Fp)*5,area(Fp,D,Cc,E))
# 1715535
x=(3*math.sqrt(5)-3)/2
assert math.isclose(x*x,3*(3-x)) and math.isclose(3*x+x*x,9) and math.isclose(math.sqrt(3*x),3*math.sqrt((math.sqrt(5)-1)/2))
assert not math.isclose(x*(3-x),2)
print('ok')
