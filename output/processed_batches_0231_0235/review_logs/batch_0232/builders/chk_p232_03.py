import math, itertools, random
from fractions import Fraction as F
from math import comb, sqrt
from collections import Counter
random.seed(3)
def shoelace(P):
    return abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[(i+1)%len(P)][0]*P[i][1] for i in range(len(P))))/2
# 1723400 hexagon area formula
for _ in range(300):
    A=(random.uniform(-3,3),random.uniform(-3,3));B=(random.uniform(-3,3),random.uniform(-3,3));C=(random.uniform(-3,3),random.uniform(-3,3))
    T=shoelace([A,B,C])
    if T<0.3: continue
    x=random.uniform(0.1,4)
    u=lambda P,Q:((P[0]-Q[0])/math.dist(P,Q),(P[1]-Q[1])/math.dist(P,Q))
    pt=lambda P,Q:(P[0]+x*u(P,Q)[0],P[1]+x*u(P,Q)[1])
    A1,A2,B1,B2,C1,C2=pt(A,B),pt(A,C),pt(B,A),pt(B,C),pt(C,B),pt(C,A)
    a=math.dist(B,C);b=math.dist(C,A);c=math.dist(A,B)
    H=shoelace([A1,A2,B2,B1,C2,C1])
    assert abs(H/T-(1+2*x*(1/a+1/b+1/c)+2*x*x*(a+b+c)/(a*b*c)))<1e-8
# equilateral side 1, x=1 -> 13
assert 1+2*3+2*3==13
# 1724670
from itertools import combinations
nums=list(range(21,50))
def pf(n):
    s=set();d=2
    while d*d<=n:
        while n%d==0: s.add(d);n//=d
        d+=1
    if n>1: s.add(n)
    return s
best=0
# greedy check of the construction and bound by smallest prime factor argument
L=[25,27,32,49,23,29,31,37,41,43,47]
assert all(not (pf(a)&pf(b)) for a,b in combinations(L,2))
sp={min(pf(n)) for n in range(20,51)}
assert len(sp)==11
# 1724416: exterior angles; three 60s in convex n-gon impossible (sum check)
for n in range(4,20): assert 3*120+ (n-3)*0 >= 360
# 1724261
sols=[(x,n) for x in range(1,200) for n in range(0,8) if all((x**4+2**(4*n+2))%d for d in range(2,int((x**4+2**(4*n+2))**.5)+1))]
assert sols==[(1,0)]
# 1724256
assert [x for x in range(-1000,1001) if (x*x+x+2)%(x*x+1)==0]==[-1,0,1]
# 1722309
def inter(p1,p2,p3,p4):
    (x1,y1),(x2,y2),(x3,y3),(x4,y4)=p1,p2,p3,p4
    den=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    t=((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/den
    return (x1+t*(x2-x1),y1+t*(y2-y1))
mid=lambda p,q:((p[0]+q[0])/2,(p[1]+q[1])/2)
def ratio(Q):
    A,B,C,D=[(F(x),F(y)) for x,y in Q]
    a=(A,mid(C,D)); b=(B,mid(D,A)); c=(C,mid(A,B)); d=(D,mid(B,C))
    P=[inter(*a,*b),inter(*b,*c),inter(*c,*d),inter(*d,*a)]
    return P,shoelace(P)/shoelace([A,B,C,D])
P,r=ratio([(0,0),(2,0),(2,2),(0,4)])
assert P==[(F(1,2),F(3,2)),(F(4,3),F(2,3)),(F(12,7),F(10,7)),(F(8,9),F(8,3))] and shoelace(P)==F(151,126) and r==F(151,756)
for _ in range(50):
    A=(random.randint(-9,9),random.randint(-9,9));u=(random.randint(1,9),random.randint(-3,3));v=(random.randint(-3,3),random.randint(1,9))
    if u[0]*v[1]-u[1]*v[0]==0: continue
    Q=[A,(A[0]+u[0],A[1]+u[1]),(A[0]+u[0]+v[0],A[1]+u[1]+v[1]),(A[0]+v[0],A[1]+v[1])]
    assert ratio(Q)[1]==F(1,5)
assert ratio([(0,0),(1,0),(1,1),(0,1)])[0]==[(F(1,5),F(2,5)),(F(3,5),F(1,5)),(F(4,5),F(3,5)),(F(2,5),F(4,5))]
# 1721154
c=Counter()
for r_ in itertools.product(range(1,7),repeat=4): c[sum(r_)-min(r_)]+=1
assert [c[s] for s in range(3,19)]==[1,4,10,21,38,62,91,122,148,167,172,160,131,94,54,21]
assert max(c,key=c.get)==13 and min(c,key=c.get)==3
assert F(sum(c[s] for s in range(15,19)),1296)==F(25,108) and F(sum(c[s] for s in range(3,6)),1296)==F(5,432)
p={s:F(c[s],1296) for s in c}
assert 180*p[9]*p[13]**2*p[15]**2*p[18]==F(101062244465,2742118830047232)
assert c[18]==comb(4,3)*5+1
# 1724087
assert 81-72-9==0 and 1+8-9==0
# 1724204: verify the construction argument numerically for k=1,2 on small cases, and the poster's colouring
col='RRGRGGGRBBRBBBBBBBGBGRG'
assert len(col)==23
for a in range(1,24):
    for b in range(a+1,24):
        if a+b<=23: assert not (col[a-1]==col[b-1]==col[a+b-1])
# weak Schur: every 2-colouring of 1..9 has a monochromatic a<b, a+b=c (WS(2)=8)
def ok(cs):
    n=len(cs)
    return all(not(cs[a-1]==cs[b-1]==cs[a+b-1]) for a in range(1,n+1) for b in range(a+1,n+1) if a+b<=n)
assert any(ok(cs) for cs in itertools.product(range(2),repeat=8)) and not any(ok(cs) for cs in itertools.product(range(2),repeat=9))
assert all((k+1)**(j+1)-1-k*(k+1)**j>=0 for k in range(1,6) for j in range(0,10))
# 1723431
s=F(0);fa,fb=1,1
for n in range(1,80):
    s+=F(fa,10**n);fa,fb=fb,fa+fb
assert abs(float(s)-10/89)<1e-15
# 1723619
for x in [F(8),F(-2,3)]:
    assert (x+4)**2==2*x*(2*x-7) and 2*x!=0 and x+4!=0
assert F(8)+F(-2,3)==F(22,3)
# 1723583: x^2+y^2=0 unique; homogeneous system with m<n has nonzero solution (random check via numpy rank)
import numpy as np
for _ in range(100):
    m=random.randint(1,4);n=m+random.randint(1,3)
    M=np.random.randint(-5,6,size=(m,n))
    assert np.linalg.matrix_rank(M)<n
# 1723636
assert sum(1 for n in range(24,126) if sum(map(int,str(n)))%7==0)==14
# 1723548
ang=lambda n:F(180*(n-2),n)
assert ang(5)*2+ang(12)==366 and ang(5)*2+ang(10)==360
# 1717425
pr=[q for q in range(2,3000) if all(q%d for d in range(2,int(q**.5)+1))]
assert [(p_,q) for p_ in pr for q in pr if (2*p_-q)**2==17*p_-10*q]==[(3,5),(7,7),(7,11)]
# 1722827
cnt=0;tot=0
for a in range(6):
    for b_ in range(6-a):
        c_=5-a-b_; co=math.factorial(5)//(math.factorial(a)*math.factorial(b_)*math.factorial(c_))*2**b_*(-3)**c_
        tot+=1
        if co>0 and math.isqrt(co)**2==co: cnt+=1
assert tot==21 and cnt==1
# 1723123
assert [2*n*n-3*n+6 for n in range(1,7)]==[5,8,15,26,41,60]
# 1723135
assert sum(n for n in range(1000,10000) if str(n)==str(n)[::-1])==495000
# 1722852
pts=[(x,y) for x in range(6) for y in range(6)]
good=sum(1 for p_,q in combinations(pts,2) if (p_[0]-q[0])**2+(p_[1]-q[1])**2 in (1,2))
assert F(good,comb(36,2))==F(11,63)
pts7=[(x,y) for x in range(7) for y in range(7)]
assert F(sum(1 for p_,q in combinations(pts7,2) if (p_[0]-q[0])**2+(p_[1]-q[1])**2 in (1,2)),comb(49,2))==F(13,98)
# 1721400
fac=[math.factorial(d) for d in range(10)]
assert sum(fac[int(d)] for d in '40585')==40585
assert all(362880*d<10**(d-1) for d in range(8,40))
assert [n for n in range(1,2540161) if sum(fac[int(d)] for d in str(n))==n]==[1,2,145,40585]
# 1723186
assert math.factorial(8)//(2**4*math.factorial(4))==105==7*5*3
# 1722616
for x in [1,-3]: assert x*x+2*x-3==0
assert sqrt(2*1+7)==1+2 and sqrt(2*(-3)+7)!=-3+2
# 1722825
def has_y(x):
    # search t=|y| >=0
    k=2*abs(x)-1
    if abs(k)<1e-15: return False
    t=(3-x*x)/k
    return t>=0
for x in np.linspace(-3,3,6001):
    expect=(0.5<abs(x)<=sqrt(3)+1e-12)
    if abs(abs(x)-0.5)<1e-9: expect=False
    assert has_y(x)==expect or abs(abs(x)-sqrt(3))<1e-3
# 1722491
def bounded(k):
    x=0.0
    for _ in range(2000):
        x=x*x+k
        if abs(x)>10: return False
    return True
for k in np.linspace(-2.5,0.6,621):
    if abs(k+2)<1e-9 or abs(k-0.25)<1e-9: continue
    if k<-2.01 or k>0.26: assert not bounded(k)
    if -1.99<k<0.24: assert bounded(k)
assert bounded(-2) and bounded(0.25)
# 1722841
poly=[1]
for j in range(1,7):
    r=j*j
    new=[0]*(len(poly)+1)
    for i,cf in enumerate(poly):
        new[i]+=cf; new[i+1]-=r*cf
    poly=new
assert [cf%13 for cf in poly]==[1,0,0,0,0,0,12]
# 1721070
lst=[5,9,2,3,7,8,6,5,6,4,1,7,9,8]
best=max(sum(1 for v in lst if m<=v<=m+2) for m in range(1,8) if m in lst and m+2 in lst)
assert len(lst)-best==8
assert (2+F(3,4)+F(5,6))/(F(6,4)+F(3,2))==F(43,36)
