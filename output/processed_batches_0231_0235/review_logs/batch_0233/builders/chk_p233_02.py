import math, itertools, random
from fractions import Fraction as F
from math import comb as C
random.seed(2)
# 1720756 q02 (Monte Carlo + exact)
assert F(9,2)/25==F(18,100)
n=200000; hit=0
for _ in range(n):
    x=random.uniform(0,5); y=random.uniform(1,6)
    hit+= x*x+y*y < (x-4)**2+(y-4)**2
assert abs(hit/n-0.18)<0.005
# 1720756 q01 dropped: y-intercepts irrational ratio
L=5+math.hypot(11,4)
def root(f,a,b):
    for _ in range(200):
        m=(a+b)/2
        if f(a)*f(m)<=0: b=m
        else: a=m
    return (a+b)/2
f=lambda y: abs(y)+math.hypot(8,y-8)-L
r=root(f,-50,0)/root(f,0,50)
assert all(abs(r-F(p,q))>1e-6 for q in range(1,60) for p in range(-60,1))
# 1719974
for x in [i/50 for i in range(-200,800)]:
    assert (abs(x-5)>3 and (x-5)**2<25)==(0<x<2 or 8<x<10)
# 1719786
def mincoins(n):
    best=99
    for q in range(n//25+1):
        for d in range((n-25*q)//10+1):
            for k in range((n-25*q-10*d)//5+1):
                best=min(best,q+d+k+(n-25*q-10*d-5*k))
    return best
assert all(mincoins(n)<=7 for n in range(1,69)) and mincoins(69)==8
# 1719663
s=''.join(str(i) for i in range(1,30001)); assert sum(1 for i in range(len(s)) if s.startswith('2013',i))==25
# 1640117
assert sum(1 for n in range(100,1000) if n%2==0 and len(set(str(n)))==3)==328
assert sum(1 for t in itertools.product('0123456',repeat=3) if t[0]!='0' and int(t[2])%2==0)==168
assert sum(1 for t in itertools.permutations('0123456',3) if t[0]!='0' and int(t[2])%2==0)==105
# 1603119
assert len(set(itertools.permutations('BANANA')))==60
# 1707844 (combinatorial model: points = pairs of diagonals)
diags=list(range(5)); pairs=list(itertools.combinations(diags,2))
cnt=sum(1 for c in itertools.combinations(pairs,5) if all(sum(1 for p in c if d in p)==2 for d in diags))
assert cnt==12
# geometric check that two diagonals always meet at a vertex or inside
V=[(math.cos(math.radians(90+72*i)),math.sin(math.radians(90+72*i))) for i in range(5)]
D=[(i,(i+2)%5) for i in range(5)]
for a,b in itertools.combinations(D,2):
    assert len(set(a)&set(b))==1 or len(set(a)&set(b))==0
assert sum(1 for a,b in itertools.combinations(D,2) if set(a)&set(b))==5
# 1601848
assert sum(math.factorial(k) for k in range(1,67))%100==13
# 1630167
assert sum(1 for p in itertools.permutations('0123456') if p[0]!='0')==4320
# 1719597
assert F(sum(1 for n in range(1000,10000) if math.prod(map(int,str(n)))%2==0),9000)==F(67,72)
# 1719574
pts=[(x,y) for x in range(-5,6) for y in range(-5,6) if x*x+y*y==25]; assert len(pts)==12
d2=[(p[0]-q[0])**2+(p[1]-q[1])**2 for p in pts for q in pts if p!=q]
irr=[d for d in d2 if math.isqrt(d)**2!=d]
assert max(irr)==98 and min(irr)==2 and math.isclose(math.sqrt(98/2),7)
# 1719242 numeric: angle between l and rotated l is a
for _ in range(100):
    a=random.uniform(1,179); th=math.radians(random.uniform(0,180))
    d=(math.cos(th),math.sin(th)); r=math.radians(a); d2_=(math.cos(th+r),math.sin(th+r))
    ang=math.degrees(math.acos(abs(d[0]*d2_[0]+d[1]*d2_[1])))
    assert math.isclose(ang,min(a,180-a),abs_tol=1e-7)
# 1719384
def phi(n): return sum(1 for k in range(1,n+1) if math.gcd(k,n)==1)
assert [x for x in range(1,2000) if phi(x)==24 and set(p for p in range(2,x+1) if x%p==0 and all(p%q for q in range(2,p)))=={3,5}]==[45]
# 1719274
assert sum(F(1,n*(n+1)*(n+2)) for n in range(1,99))==F(4949,19800)
# 1718720
assert sum(1 for p in set(itertools.permutations('MAXIMUM')) if 'MM' not in ''.join(p))==240
# 1718086
assert 88*30-1000==1640 and math.isclose(60*5280/3600,88)
# 1711163
s7=set(itertools.permutations('ELEMENT')); assert F(sum(1 for p in s7 if 'EEE' in ''.join(p)),len(s7))==F(1,7)
# 1717423
for _ in range(100):
    x=random.uniform(0.2,5); y=random.uniform(0.2,5); z=1/(x*y)
    assert math.isclose(1/(1+x+x*y)+1/(1+y+y*z)+1/(1+z+z*x),1)
# 1717407 exhaustive over colourings of K6
E6=list(itertools.combinations(range(6),2))
for m in range(1<<15):
    col={e:(m>>i)&1 for i,e in enumerate(E6)}
    assert any(col[(a,b)]==col[(a,c)]==col[(b,c)] for a,b,c in itertools.combinations(range(6),3))
# 1717974
for _ in range(200):
    a=random.randint(1,10**6); b=random.randint(1,a)
    x,y=a,b
    while y: x,y=y,x%y
    assert x==math.gcd(a,b)
# 1717400
assert [n for n in range(3004,4000,10) if str(n)[0]=='3' and n%9==0]==[3024,3114,3204,3294,3384,3474,3564,3654,3744,3834,3924]
# 1717405
Pr=[p for p in range(2,500) if all(p%d for d in range(2,p))]
assert [(p,q) for p in Pr for q in Pr if 3*p*p*q+2*p*q*q==483]==[(3,7)]
# 1717720
pr={2,3,5,7,11,13,17}
assert F(sum(1 for t in itertools.product(range(1,7),repeat=3) if sum(t) in pr or sum(t)%2==0),216)==F(181,216)
assert sum(1 for t in itertools.product(range(1,7),repeat=3) if sum(t)==9)==25 and sum(1 for t in itertools.product(range(1,7),repeat=3) if sum(t)==15)==10
# 1717424
A=(0,0);B=(0,2);Cc=(2*math.sqrt(3),0);K=(2/math.sqrt(3),0)
BK=math.dist(B,K);KC=math.dist(K,Cc);AK=math.dist(A,K)
assert math.isclose(BK,KC) and math.isclose(KC,2*AK)
ang=lambda P,Q,R: math.degrees(math.acos(((P[0]-Q[0])*(R[0]-Q[0])+(P[1]-Q[1])*(R[1]-Q[1]))/math.dist(P,Q)/math.dist(R,Q)))
assert math.isclose(ang(A,B,K),ang(K,B,Cc)) and math.isclose(ang(A,B,Cc),60) and math.isclose(ang(B,Cc,A),30)
print('ok')
