import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(1)
# 1792761
can=lambda n: any((n-13*b)%11==0 for b in range(n//13+1))
assert not can(119) and all(can(n) for n in range(120,1200))
# 1793819: non-integers fail for some n
for _ in range(2000):
    x=F(random.randint(-500,500),random.randint(2,60))
    if x.denominator==1: continue
    assert any(math.floor(n*x)!=n*math.floor(x) for n in range(1,61))
# 1793329 dance simulation
for m in range(1,19):
    g=19-m
    for trial in range(5):
        people=[('M',i) for i in range(m)]+[('G',j) for j in range(g)]
        random.shuffle(people)
        man=next(p for p in people if p[0]=='M'); girl=next(p for p in people if p[0]=='G')
        q=[p for p in people if p not in (man,girl)]
        seen={(man[1],girl[1])}
        for s in range(17*m*g+5):
            h=q.pop(0)
            if h[0]=='M': q.append(man); man=h
            else: q.append(girl); girl=h
            seen.add((man[1],girl[1]))
        assert len(seen)==m*g
# 1791587
best=min(x+(8-x)/2+3/x+9/(8-x) for x in np.linspace(0.001,7.999,200001))
assert abs(best-8)<1e-6 and 2+3+F(3,2)+F(9,6)==8
# 1793269
for n in range(1,60): assert math.gcd(math.factorial(n)+1,math.factorial(n+1)+1)==1
# 1793574
assert 3*7+6*F(5,2)==36 and 7-F(5,2)==F(9,2)
assert 25+75==100 and F(12,100)*25+F(20,100)*75==18
# 1793467
assert 8+4==12 and 8-4==4 and 8+5==13 and 8-5==3
# 1793187: angle FAE = 45 for several positions
for y in [0.1,0.3,0.4,0.7,0.9]:
    x=(1-y)/(1+y); E=np.array([1,y]); Fp=np.array([x,1])
    assert abs(np.linalg.norm(E-Fp)-(x+y))<1e-12
    ang=math.degrees(math.acos(E@Fp/np.linalg.norm(E)/np.linalg.norm(Fp))); assert abs(ang-45)<1e-9
assert abs(math.hypot(4,4.2)-5.8)<1e-12  # figure: side 7, BE=2.8, DF=3
# 1793143
for x in range(-1,100001):
    v=x**3+7; r=math.isqrt(v); assert r*r!=v
# 1793132
P=[p for p in range(2,400) if all(p%d for d in range(2,int(p**.5)+1))]
S=set(P)
sol=[(p,q) for p in P for q in P if any(r*(r+1)==p*(p+1)+q*(q+1) for r in [int((math.isqrt(4*(p*p+p+q*q+q)+1)-1)//2)] if r in S)]
assert sol==[(2,2)]
# 1792786 random triangles
def ext(P,d,Q1,Q2):
    M=np.array([d,Q1-Q2]).T; t=np.linalg.solve(M,Q1-P); return P+t[0]*d
for _ in range(200):
    A,B,C=[np.array([random.uniform(-5,5),random.uniform(-5,5)]) for _ in range(3)]
    G=(A+B+C)/3; X=2*G-A
    L=ext(X,A-C,B,C); M_=ext(X,B-A,C,A); N_=ext(X,C-B,A,B)
    cr=(M_-L)[0]*(N_-L)[1]-(M_-L)[1]*(N_-L)[0]
    assert abs(cr)<1e-6*(1+np.linalg.norm(M_-L)*np.linalg.norm(N_-L))
for P_ in [(2,1),(0,2),(4,0)]: assert P_[0]+2*P_[1]==4
# 1792646
assert pow(3,1118,10)==9
# 1780334
assert 2+67==69 and 67-2==65
# 1792647
assert ''.join(map(str,range(1,2020))).count('0')==521==9+180+300+32
# 1792730 numeric (figure configuration)
d=lambda a: np.array([math.cos(math.radians(a)),math.sin(math.radians(a))])
A,D,B,C=d(140),d(62),d(212),d(328); E=B+0.24*(C-B)
def cc(P,Q,R):
    a=Q-P;c=R-P;dd=2*(a[0]*c[1]-a[1]*c[0])
    return P+np.array([(c[1]*(a@a)-a[1]*(c@c))/dd,(a[0]*(c@c)-c[0]*(a@a))/dd])
O2=cc(A,D,E);u=(C-B)/np.linalg.norm(C-B);Fq=E-2*((E-O2)@u)*u
ang=lambda P,Q,R: math.degrees(math.acos((P-Q)@(R-Q)/np.linalg.norm(P-Q)/np.linalg.norm(R-Q)))
assert 0<(Fq-B)@u<(C-B)@u and (E-B)@u<(Fq-B)@u
assert abs(ang(Fq,D,C)-ang(E,A,B))<1e-9 and abs(ang(E,A,Fq)-ang(E,D,Fq))<1e-9 and abs(ang(C,A,Fq)-ang(B,D,E))<1e-9
# 1792720
for p in range(5,20000):
    if all(p%d for d in range(2,int(p**.5)+1)) and all((p+2)%d for d in range(2,int((p+2)**.5)+1)):
        assert (p*(p+2))%9==8
# 1792707 numeric
for _ in range(100):
    th=random.uniform(0.1,6.2);
    if abs(th-math.pi)<0.05: continue
    R=lambda v: np.array([math.cos(th)*v[0]-math.sin(th)*v[1],math.sin(th)*v[0]+math.cos(th)*v[1]])
    B=np.array([random.uniform(1,5),0.0]); c=random.uniform(1,5); C=c*np.array([math.cos(th/2),math.sin(th/2)])
    M_=(B+R(B))/2; assert abs(C[0]*M_[1]-C[1]*M_[0])<1e-9
    K=(C+R(C))/2; Bp=R(B); assert abs(Bp[0]*K[1]-Bp[1]*K[0])<1e-9
# 1792695 Monte Carlo
h=0
for _ in range(100000):
    d1,d2=random.random()<.5,random.random()<.5; h+=(d1!=d2)
assert abs(h/100000-0.5)<0.01
# 1771789
c=sum(1 for p in itertools.permutations([0,0,1,1,2,2]) if all(p[i]!=p[i+3] for i in range(3)))
assert F(c,720)==F(8,15)
# 1792514
w=(-1+1j*math.sqrt(3))/2
assert abs(w*w+w+1)<1e-12 and abs(w**3-1)<1e-12
