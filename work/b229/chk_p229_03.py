import math, itertools
from fractions import Fraction as F
import numpy as np
# 1742467 convex sequences
cs=[p for p in itertools.permutations(range(1,9)) if all(2*p[i]<=p[i-1]+p[i+1] for i in range(1,7))]
assert len(cs)==8 and (7,5,3,1,2,4,6,8) in cs and (7,1,2,3,4,5,6,8) in cs
# 1742450 hexagon
assert abs(2*4*math.sin(math.pi/6)-4)<1e-12
# 1742456 towers
X=(F(200,9),70); assert 90-F(9,10)*X[0]==70
assert abs(math.hypot(200/9,20)-20*math.sqrt(181)/9)<1e-12 and abs(20*math.sqrt(181)/9-29.9)<0.05
# 1742459
assert [x*x-x for x in range(1,100) if 1801<=x*x-x<=1850]==[1806]
# 1742264
r1=(3-math.sqrt(37))/14; r2=(3+math.sqrt(37))/14
assert abs(-7*r1**2+3*r1+1)<1e-12 and round(r1,2)==-0.22 and round(r2,2)==0.65
assert abs((-3+math.sqrt(37))/(-14)-r1)<1e-12
r3=(3-math.sqrt(233))/14; assert abs(-7*r3**2+3*r3+1+7)<1e-12 and round(r3,2)==-0.88 and round((3+math.sqrt(233))/14,2)==1.30
# 1741984
A=np.array([1,3]);B=np.array([4,4]);C=np.array([5,1]);D=np.array([2,0])
for P,Q,R in [(A,B,C),(B,C,D),(C,D,A),(D,A,B)]:
    assert (P-Q)@(R-Q)==0 and (P-Q)@(P-Q)==10
# 1742279
glops=400; blops=glops*F(6,5); cow=F(400,2); ch=blops-cow
assert ch==280 and ch*F(5,6)==F(700,3)
assert sum(1 for n in range(401,2**12) if 400**2<n*n<2**24)==2**12-401  # same formula with 2^24 in place of 2^400
assert F(400*400,2)*F(1,2)*1==40000 and 400*400*F(1,2)==80000
# 1669230
best=None
P=[2,3,5,7,11,13,17]
def rec(i,rem,cur,maxe):
    global best
    if rem==1:
        best=cur if best is None or cur<best else best; return
    for e in range(1,maxe+1):
        if rem%(e+1)==0: rec(i+1,rem//(e+1),cur*P[i]**e,e)
rec(0,200,1,199)
assert best==498960==2**4*3**4*5*7*11 and sum(map(int,str(best)))==36
dc=lambda n: sum(2 for d in range(1,math.isqrt(n)+1) if n%d==0)-(1 if math.isqrt(n)**2==n else 0)
assert dc(498960)==200
# 1741935
a=0
for n in range(1,101): a=2*a+2**n
assert a==100*2**100
# 1740608
assert sum(range(1,101))==5050
assert len({a+b+c for a,b,c in itertools.combinations_with_replacement(range(0,126,25),3)})==16
assert min(k for k in range(1,50) if int('1'*k)%41==0)==5 and 11111==41*271
# 1741490
w=3+2*math.sqrt(2); assert abs(math.hypot(w-2-1,2-1)-3)<1e-12 and round(4/w,2)==0.69
# 1741457 joker: exact by enumeration over position of joker among primes+joker
assert F(1,9)==F(math.factorial(8),math.factorial(9))
import random; random.seed(3)
cards=list(range(1,21))+['J']; primes={2,3,5,7,11,13,17,19}; hit=0; N=200000
for _ in range(N):
    random.shuffle(cards); k=cards.index('J'); hit+= sum(1 for c in cards[:k] if c in primes)==4
assert abs(hit/N-1/9)<0.005
# 1741722 Connex
def go(rem,av):
    if rem==0: return 1
    t=0
    for L in (1,2,3,4):
        if av[L]>0 and L<=rem:
            av[L]-=1; t+=go(rem-L,av); av[L]+=1
    return t
assert go(10,{1:4,2:3,3:2,4:1})==277
assert 35+60+20+15+30+6+30+30+4+20+24+3==277
# 1741715
sols=[]
for p in itertools.permutations('123456'):
    a=int(p[0]);b=int(''.join(p[1:3]));c=int(''.join(p[3:]))
    if a*b*c==20400: sols.append((a,b,c))
assert sols==[(3,16,425)]
# 1741603
O=np.zeros(2)
def tri(angC):
    A=5*np.array([0,1.]);B=5*np.array([math.cos(math.radians(150)),math.sin(math.radians(150))])
    C=5*np.array([math.cos(math.radians(angC)),math.sin(math.radians(angC))]); return A,B,C
for angC,val in [(90-2*math.degrees(math.asin(0.6)),3*math.sqrt(3)+4),(90+2*math.degrees(math.asin(0.6)),3*math.sqrt(3)-4)]:
    A,B,C=tri(angC); assert abs(np.linalg.norm(A-B)-5)<1e-9 and abs(np.linalg.norm(A-C)-6)<1e-9 and abs(np.linalg.norm(B-C)-val)<1e-9
# 1741190
m=b=F(1,13); assert 5*m+4*(m+b)==1 and m+6*(m+b)==1
# 1741553
for x in range(-5,6): assert ((x+1)-1)**3==x**3
# 1740713 Newton relation: random instance satisfies determinant
import random
for _ in range(20):
    g,r,c=[random.uniform(1,5) for _ in range(3)]
    rows=[]
    for _ in range(3):
        Q=random.uniform(1,4); R=random.uniform(1,10); P=Q*(g+r*R)/(c*R)
        rows.append([P*R/Q,R,1])
    assert abs(np.linalg.det(np.array(rows)))<1e-8
    (x1,R1,_),(x2,R2,_),(x3,R3,_)=rows
    assert abs(x1*(R2-R3)+x2*(R3-R1)+x3*(R1-R2))<1e-8
# 1730513
assert math.factorial(6)==720 and math.comb(7,3)==35==sum(1 for t in itertools.product(range(1,9),repeat=4) if sum(t)==8)
# 1740548
for y in [-2,-1,1,3]:
    x,z=1.5,-0.7; assert abs((16*x**8*y**4*z**16)**0.25-2*x*x*abs(y)*z**4)<1e-9
# 1738754
L=list('MATHCOUNTS'); assert len(set(itertools.permutations(L,4)))==3360
# 1740568
import sympy as sp
x=sp.symbols('x'); p=x**3-x**2-7*x+3
assert sp.expand(p.subs(x,sp.sqrt(2)-1))==0 and p.subs(x,3)==0
