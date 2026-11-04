import math, itertools, random
from fractions import Fraction as F
random.seed(1)
# 1739467
sols=[(n,K) for n in range(2,400) for K in range(1,n+1) if F(n*(n+1)//2-K,n-1)==F(46*23+20,23)]
assert sols==[(93,59)]
# 1740263
x,y=F(7,6),F(4,5); assert x*y==F(14,15) and x/y==F(35,24) and x>y
# 1568921
for a,b in [(3,1.4),(2,2),(5,0.1)]: assert (a+b)**2>=4*a*b-1e-12
# 1738949: no solution with small values (exponent argument), spot-check
assert 1991%3!=0 and 1991==11*181
# 1739977
assert [n for n in range(1,41) if math.isqrt(1+4*n)**2==1+4*n]==[2,6,12,20,30]
v=0
for _ in range(200): v=math.sqrt(30+v)
assert abs(v-6)<1e-12
# 1739930
best=max(int(''.join(p)) for p in itertools.permutations('0123456789') if p[0]!='0' and int(p[-2]+p[-1])%4==0)
assert best==9876543120 and best%12==0
# 1736311: brute force small n
def val(ops):
    terms=[];cur=F(2);sign=1;tot=F(0)
    for o in ops:
        if o=='*': cur*=2
        elif o=='/': cur/=2
        else: tot+=sign*cur; cur=F(2); sign=1 if o=='+' else -1
    return tot+sign*cur
for n in range(1,8):
    s=sum(val(o) for o in itertools.product('+-*/',repeat=n-1))
    assert s==F(2,3)*(4**n-F(5,2)**(n-1)),n
n=2018; assert F(2,3)*(F(4)**n-F(5,2)**(n-1))==F(2**6053-5**2017,3*2**2016)
# 1739351
def nx(x): return x//3 if x%3==0 else x-1
s=[]
for a in range(100,1000):
    x=a
    for _ in range(5): x=nx(x)
    if x==1: s.append(a)
assert s==[108,162,243] and sum(s)==513
# 1739592: smoothing spot check
for _ in range(1000):
    xs=[random.uniform(0.1,10) for _ in range(random.randint(2,7))]
    A=sum(xs)/len(xs); assert math.prod(xs)<=A**len(xs)+1e-9
# 1739370: cyclic orders of 4 blocks up to rotation / rotation+reflection
def canon(p,refl):
    rots=[p[i:]+p[:i] for i in range(4)]
    if refl: rots+=[r[::-1] for r in rots]
    return min(rots)
P=list(itertools.permutations('RBGW'))
assert len({canon(p,False) for p in P})==6 and len({canon(p,True) for p in P})==3
# 1737760
assert pow(1999,2000,5)==1
# 1738860
w,h=F(6),F(4); s_=F(4,7); P_=(w-s_*w/2,h/3+2*s_*h/3); t=P_[0]/w; assert P_[1]==t*h and t==F(5,7) and t/(1-t)==F(5,2)
# 1737110
c=[(a,b) for a in range(1,13) for b in range(a+1,13) if a**3+b**3==1729]; assert c==[(1,12),(9,10)] and 1+12+9+10==32
# 1737382
assert 2**2+44==48
assert sum(5*x+7 for x in range(128))==41536
# 1738601
S=[1,2,3,11,12,13,21,22,23]; assert len({sum(c) for c in itertools.combinations(S,3)})==29
# 1550572
assert [n for n in range(1000,2001) if n%15==0 and n%20==0 and n%25==0]==[1200,1500,1800]
# 1730993
E=sum(k*F(5,6)**(k-1)*F(1,6) for k in range(1,400)); assert abs(float(E)-6)<1e-9
# 1738261
t=[1,2,3]
while len(t)<11: t.append(t[-1]+t[-2]+t[-3])
assert t[10]==423
# 415026
assert F(sum(1 for a in range(1,7) for b in range(1,7) if a*b>10),36)==F(17,36)
# 1737416
cA=F(13**2+14**2-15**2,2*13*14); assert cA==F(5,13)
assert 1-2*cA**2==F(119,169) and 119**2+120**2==169**2 and math.gcd(119,120)==1 and 119+120+169==408
B=(0,0);C=(15,0);A=(8.4,11.2);X=(7.5,3.125)
for P in (A,B,C): assert abs(math.dist(P,X)-8.125)<1e-12
ang=math.degrees(math.acos(((B[0]-X[0])*(C[0]-X[0])+(B[1]-X[1])*(C[1]-X[1]))/8.125**2))
assert abs(math.cos(math.radians(180-ang))-119/169)<1e-12
# 1737879
assert math.gcd(1,1)==1 and math.gcd(1,0)==1
print('chk_p230_01 ok')
