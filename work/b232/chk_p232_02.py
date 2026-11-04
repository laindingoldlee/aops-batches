import math, itertools, random
from fractions import Fraction as F
from math import comb, sqrt
random.seed(2)
# 1722695
assert pow(5,400,19)==17
# 1726398
assert 2**2==(-2)**2 and all(abs(math.sqrt(x*x)-x)<1e-12 for x in [0,0.5,3])
# 11090
def ways(n,lo):
    return [(a,b) for a in range(lo,int(n**.5)+1) for b in range(a+1,int(n**.5)+1) if a*a+b*b==n]
assert next(n for n in range(1,200) if len(ways(n,1))>=2)==65
assert next(n for n in range(1,200) if len(ways(n,0))>=2)==25
# 1726419
assert pow(11,12,13)==1
# 1726387
for x in [10,100]: assert abs(x**math.log10(x)-x**3/100)<1e-6*x**3
xs=[10**(k/1000) for k in range(-3000,4000)]
roots=[x for x in xs if abs(math.log10(x)**2-3*math.log10(x)+2)<1e-9]
assert all(abs(r-10)<1e-6 or abs(r-100)<1e-4 for r in roots)
# 1726281 q01-q04
assert 2*(13+17)==60
a=( -2*sqrt(78)+sqrt(4*78-84))/(-6); c=sqrt(78)-2*a
assert a>0 and c>0 and abs(2*a*a+c*c-64)<1e-9 and abs(2*(a*a+2*a*c)-14)<1e-9 and 64+14==78
s_=16; r=5*s_/8; O=(s_-r,s_/2)
assert r==10 and abs(math.dist(O,(0,0))-r)<1e-12 and abs(math.dist(O,(0,s_))-r)<1e-12 and abs((s_-O[0])-r)<1e-12
h=sqrt(6**2-2**2); assert abs(h-4*sqrt(2))<1e-12 and 4+8==6+6
# 1725452
a=10; assert abs(sqrt(3)/4*a*a-25*sqrt(3))<1e-9
s=20*sqrt(3)-30; x=(a-s)/2
assert abs(s-x*sqrt(3))<1e-12 and abs(s*s-(2100-1200*sqrt(3)))<1e-9
# 1723237
D=(-5,-3);Fp=(5,4);v=(D[0]-Fp[0],D[1]-Fp[1]);D2=(Fp[0]-v[1],Fp[1]+v[0])
assert D2==(12,-6)
R=(-5,3);R1=(R[1]+2,R[0]-2);assert R1==(5,-7)
mid=((R[0]+R1[0])/2,(R[1]+R1[1])/2);assert mid[1]==mid[0]-2 and (R1[0]-R[0])+(R1[1]-R[1])==0
R2=(R1[1],-R1[0]);assert R2==(-7,-5) and (R2[0]-R[0])**2+(R2[1]-R[1])**2==68==4*17
assert round(100/24,1)==4.2
m=set()
for cc in itertools.product([-1,0,1],repeat=4):
    v_=sum(p*q for p,q in zip(cc,[1,3,8,26]))
    if v_>0: m.add(v_)
assert min(set(range(1,100))-m)==13
# 1725457: brute force over complex common roots with a real
for k in range(2015):
    z=complex(math.cos(2*math.pi*k/2015),math.sin(2*math.pi*k/2015))
    av=-(z**3+1)/z
    if abs(av.imag)<1e-9:
        assert k==0 and abs(av.real+2)<1e-9
assert 1-2+1==0
# 1724568
assert F(54,10)*F(1,3)+F(46,10)*F(1,2)==F(41,10) and F(41,10)/F(5,6)==F(492,100)
# 1725609
n=next(n for n in range(1,10**6) if math.isqrt(sum(range(n,n+888)))**2==sum(range(n,n+888)))
assert n==56 and sum(range(56,56+888))==666**2
# 1724520
sol=[(b,c) for b in range(9,200) for c in range(9,200) if 8*b+5==5*c+8]
assert min(sol)[0]==11 and (11,17) in sol
# 1725821
N=200000;hit=0
for _ in range(N):
    x=random.uniform(0,10);y=random.uniform(0,10)
    if x+y>5 and abs(x-y)<5: hit+=1
assert abs(hit/N-5/8)<0.005
# 1725653
best=0
for T in itertools.chain.from_iterable(itertools.combinations(range(1,21),k) for k in range(10,15)):
    if sum(T)==90: best=max(best,len(T))
assert best==12 and F(2)**(2*12-20)==16
assert sum(F(n,2) for n in range(1,21) if n not in (1,2,3,4,5,6,7,8,9,10,15,20))+sum(2*n for n in (1,2,3,4,5,6,7,8,9,10,15,20))==240
# 1725566
P=lambda n: comb(n+5,5)
assert sum(P(n) for n in range(3,71))+28==comb(76,6)
def pf(n):
    f=[];d=2
    while d*d<=n:
        while n%d==0: f.append(d);n//=d
        d+=1
    if n>1: f.append(n)
    return f
fs=sorted(set(pf(comb(76,6))))
assert fs[-3:]==[37,71,73] and sum(fs[-3:])==181
# brute force P_n for small n
for n in range(1,6):
    assert sum(1 for t in itertools.product(range(1,7),repeat=n) if all(t[i]>=t[i+1] for i in range(n-1)))==P(n)
# 1725606
assert sum(pow(2013,k,7) for k in range(2014))%7==1
w='BLUEMOUNTAINS'; vowels=[ch for ch in w if ch in 'AEIOU']
assert sorted(vowels)==list('AEIOUU') and len(w)==13
assert F(1,math.factorial(6)//2)==F(1,360)
# 1725534: glide reflection check
A=(0,0);B=(4,3);C=(4,0);Dd=(5,0);E=(F(9,5),F(-12,5))
assert (E[0]**2+E[1]**2)==9 and (E[0]-5)**2+E[1]**2==16
def refl(p):
    d=(3*p[0]+p[1]-F(15,2))/10
    return (p[0]-2*d*3,p[1]-2*d*1)
def glide(p):
    q=refl(p); return (q[0]+F(1,2),q[1]-F(3,2))
assert glide(A)==Dd and glide(B)==A and glide(C)==E
area_small=F(1,2)*F(5,2)*F(3,2); assert area_small/(6-area_small)==F(5,11)
# 1724620 pentagon circle
r=(18-9*sqrt(2))/4; c=3-r
assert abs((2*c-1.5)/sqrt(2)-r)<1e-12 and c>r
# grid check: max inscribed radius by sampling centres
best=0
for i in range(301):
    for j in range(301):
        x=3*i/300;y=3*j/300
        if x+y<1.5: continue
        d=min(x,y,3-x,3-y,(x+y-1.5)/sqrt(2))
        # distance to corner region boundary: also need distance to points Y,I edges; the pentagon is convex
        best=max(best,d)
assert abs(best-r)<0.01
# 1725436
assert 9*5==45
# 1725061
L=[n for n in range(1000,2000) if sum(map(int,str(n)))==24]
assert len(L)==15 and sorted(L)[7]==1878
# 1723304
import numpy as np
xs=np.concatenate([np.linspace(-5/3,-sqrt(1.5),400001),np.linspace(sqrt(1.5),20,400001)])
ys=np.sqrt(np.maximum(2*xs**2-3,0))+np.sqrt(np.maximum(3*xs+5,0))
assert abs(ys.min()-sqrt(5-3*sqrt(6)/2))<1e-9 and 5+3+6+2==16
# 1725176
f=lambda a: a*2**a
assert f(1)<3<f(1.5)
lo,hi=1,1.5
for _ in range(60):
    mm=(lo+hi)/2
    if f(mm)<3: lo=mm
    else: hi=mm
assert abs(lo-1.256)<0.001
# 1724972
ab=F(864*27,80); assert ab==F(1458,5) and ab>F(1089,4)
best=min((a*a+(33-a)**2-225)/(2*a*(33-a)) for a in np.linspace(9.01,23.99,100001))
assert abs(best-71/121)<1e-6 and 13/27<best
# 1724982
assert abs(sqrt(3)/2-(0.5/(1/sqrt(3))))<1e-12 and abs((1/math.tan(math.pi/3)+1/math.sin(math.pi/3))-sqrt(3))<1e-12
for _ in range(200):
    P_=[(random.random(),random.random()) for _ in range(3)]
    a=math.dist(P_[1],P_[2]);b=math.dist(P_[0],P_[2]);c=math.dist(P_[0],P_[1])
    s=(a+b+c)/2;T=sqrt(max(s*(s-a)*(s-b)*(s-c),0))
    if T<1e-3: continue
    rr=T/s;Cang=math.acos((a*a+b*b-c*c)/(2*a*b))
    assert abs((s-c)/rr-(1/math.tan(Cang)+1/math.sin(Cang)))<1e-6*max(1,(s-c)/rr)
# 1724486 q01
for k in [0,1,-3.5]:
    for x in [10.0,100.0,1000.0]:
        assert abs((2*x*x+6*x+k)/(x+4)-(2*x-2))<20/x
assert math.gcd(math.gcd(2,6),math.gcd(1,4))==1 and 2+6+1+4==13
# 1724486 q03
A=(0,1);B=(-5.5,0);C=(5.5,0);E=(-0.5,0);D=(0.5,0)
ang=lambda P,Q,R: math.acos(((P[0]-Q[0])*(R[0]-Q[0])+(P[1]-Q[1])*(R[1]-Q[1]))/(math.dist(P,Q)*math.dist(R,Q)))
t1,t2,t3=ang(B,A,E),ang(E,A,D),ang(D,A,C)
assert abs(t1-t2)<1e-12 and abs(t2-t3)<1e-12
assert abs(math.dist(A,C)-5*sqrt(5)/2)<1e-12 and abs(math.dist(A,E)-sqrt(5)/2)<1e-12
