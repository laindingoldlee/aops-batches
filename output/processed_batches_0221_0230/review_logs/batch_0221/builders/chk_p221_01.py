import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(1)
# 1789388 five positive integers: brute force on small analogue (sum odd S, three of them even sum)
for _ in range(20000):
    a,b,c=[random.randint(1,600) for _ in range(3)]
    if a+b+c!=1000: c=1000-a-b
    if c<1: continue
    d=random.randint(1,1008); e=1009-d
    assert (a*b*c*d*e)%4==0
# 1789275
B=np.array([0,0]);C=np.array([6,0]);A=np.array([3,3*math.sqrt(3)]);O=(A+B+C)/3
assert all(abs(np.linalg.norm(O-P)-2*math.sqrt(3))<1e-12 for P in (A,B,C))
# 1683277
assert math.comb(4,2)==6
# 1789230 clock: disk rotation 3*theta
assert 360/3==120 and 120/30==4
# 1789026
assert 25%25==0 and (2*2+5)%25!=0
assert 104%8==0 and (3*1+2*0+4)%8!=0
for N in range(10,100000): assert (N%4==0)==((2*((N//10)%10)+N%10)%4==0)
for N in range(1,1000): assert (N%2==0)==((N%10)%2==0) and (N%5==0)==((N%10)%5==0)
# 1789002
S=sum(int('3'*k) for k in range(1,50)); assert sum(map(int,str(S)))==174 and S==(10**50-451)//27
assert str(S)=='37'+'037'*14+'03687'
# 1789143
assert math.perm(30,8)==235989936000
# 1789170
for n in range(12):
    for r in range(n+1): assert len(list(itertools.combinations(range(n),r)))==math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
# 1789162
assert 10+8*7-6/2==63
# 1789101 balanced ternary and uniqueness of 4-weight sets with max 40
def meas(ws):
    s=set()
    for cs in itertools.product((-1,0,1),repeat=len(ws)):
        v=sum(c*w for c,w in zip(cs,ws))
        if v>0: s.add(v)
    return s
assert set(range(1,41))<=meas([1,3,9,27])
for ws in itertools.combinations(range(1,41),3): assert not set(range(1,41))<=meas(ws)
good=[ws for ws in itertools.combinations_with_replacement(range(1,41),4) if sum(ws)>=40 and set(range(1,41))<=meas(ws)]
assert all(max(w)==27 for w in good) and good==[(1,3,9,27)]
# 1788776
for _ in range(100):
    a,b=random.randint(-50,50),random.randint(-50,50)
    assert a*a-b*b==(a-b)*(a+b) and a**3-b**3==(a-b)*(a*a+a*b+b*b) and a**3+b**3==(a+b)*(a*a-a*b+b*b)
# 1788416
assert pow(11,12,13)==1
# 1788191 numeric integration
xs=np.linspace(0,5,2001); ys=np.linspace(0,3,1201)
X,Y=np.meshgrid((xs[:-1]+xs[1:])/2,(ys[:-1]+ys[1:])/2); R=X**2+Y**2
p=np.mean((R>=4)&(R<=15)); ex=math.sqrt(6)/10+0.5*math.atan(math.sqrt(6)/2)-math.pi/15
assert abs(p-ex)<1e-3 and abs(ex-0.4785)<1e-3
# 1788440 Connex
lim={4:1,3:2,2:3,1:4}
def go(rem,used):
    if rem==0: return 1
    s=0
    for q in (1,2,3,4):
        if q<=rem and used.get(q,0)<lim[q]:
            u=dict(used);u[q]=u.get(q,0)+1;s+=go(rem-q,u)
    return s
assert go(10,{})==277
assert 35+60+20+15+30+6+30+30+4+20+24+3==277
# 1787416
sols=[]
for ad in range(1,13):
    dc=math.sqrt(169-ad*ad)
    if abs(ad*dc-60)<1e-9: sols.append((ad,dc))
assert sols==[(5,12.0),(12,5.0)]
assert 0.5*14*12==84 and 9**2+12**2==225
A=np.array([9,12]);B=np.array([0,0]);C=np.array([14,0])
for P,Q,Rr in [(A,B,C),(B,C,A),(C,A,B)]: assert np.dot(Q-P,Rr-P)>0
assert 15**2+13**2<(10*math.sqrt(2)+12)**2
# 1788621
def nd(m,b):
    k=0
    while m: m//=b;k+=1
    return k
assert sum(1 for m in range(1,100000) if nd(m,5)==nd(m,8))==195
# 1788511
def pd(n): return [d for d in range(2,n) if n%d==0]
assert [n for n in range(2,20000) if pd(n) and max(pd(n))==45*min(pd(n))]==[180,405]
# 1788057
assert sum(1 for n in range(1,100) if n*(n+1)*(n+2)*(n+3)<100000)==16
# 1787875
assert 1-F(415,450)**2==F(1211,8100)
N=400000; x=np.random.default_rng(2).uniform(0,450,N); y=np.random.default_rng(3).uniform(0,450,N)
ov=np.maximum(0,np.minimum(x,y)+45-np.maximum(x,y)); assert abs(np.mean(ov>=10)-1211/8100)<0.004
# 1788156
M=[[25,7,10],[-1,14,29],[18,21,3]]
L=[sum(r) for r in M]+[sum(M[i][j] for i in range(3)) for j in range(3)]+[M[0][0]+M[1][1]+M[2][2],M[0][2]+M[1][1]+M[2][0]]
assert set(L)=={42}
# 1786814
P=np.polymul([1,-4,-32],[1,-14,62]); assert list(P)==[1,-18,86,200,-1984]
# 1787435 alias
assert abs(math.pi/6+math.sqrt(3)/4-0.5-0.4566)<1e-4
# 1787556
assert 3*F(-1,3)+9*F(1,3)==2 and 3*F(2,3)+9*0==2 and (0-F(1,3))/(F(2,3)+F(1,3))==F(-1,3)
# 1787527
def p(n): return 1-F(n+1,2**n)
assert p(4)<F(4,5)<=p(5) and p(5)==F(13,16)
# 1787633
v=1**100*2**200*3**300*4**400*5**500
while v%10==0: v//=10
assert v%100==76
