import math, itertools, random
from fractions import Fraction as F
import numpy as np
# 1707222 q01
L=[n for n in range(100,1000) if '0' not in str(n) and len(set(str(n)))==3]
assert F(sum(L),len(L))==555
# q02
P,Q,R,S=map(np.array,[(-12.5,0),(-3.5,12),(12.5,0),(3.5,-12)])
assert abs((Q-P)@(R-Q))<1e-12 and abs((R-Q)@(S-R))<1e-12 and Q[1]-S[1]==24 and R[0]-P[0]==25
assert abs(2*(np.linalg.norm(Q-P)+np.linalg.norm(R-Q))-70)<1e-12
# q03
def key(omit):
    pts=[i for i in range(7) if i not in omit]
    steps=[(pts[(i+1)%5]-pts[i])%7 for i in range(5)]
    forms=[]
    for s in (steps,steps[::-1]):
        for k in range(5): forms.append(tuple(s[k:]+s[:k]))
    return min(forms)
assert len({key(o) for o in itertools.combinations(range(7),2)})==3
# q04
sol=[(u,v,w) for u in range(1,20) for v in range(u,20) for w in range(v,20) if u+v+w==19 and v*v==u*w]
assert sol==[(4,6,9)] and (4*6+6*9+4*9)+(-4*6*9)==-102
# 1707437
s=sum(F(1,2**a*3**b) for a in range(60) for b in range(40)); assert abs(float(s)-3)<1e-10
# 1311798
assert all(sum(F(1,n) for n in range(1,2**k+1))>=1+F(k,2) for k in range(0,11))
# 1706861
assert [n for n in range(5001,6000) if (n//10%10)%2==0 and n%10*2==n//10%10 and n//100%10==3*(n//10%10)]==[5621]
# 1692181
faces=[('BW','B'),('BW','W'),('BB','B'),('BB','B')]
blue=[f for f in faces if f[1]=='B']; assert F(sum(1 for f in blue if f[0]=='BB'),len(blue))==F(2,3)
# 1706924
assert F(sum(1 for p in itertools.permutations(range(3)) if p==(0,1,2)),6)==F(1,6)
# 1706395
sol=[(a,b) for a in range(1,27) for b in range(a+1,27) if a*b==351-a-b]
assert sol==[(15,21)]
# 1705401
digs=''.join(str(n) for n in range(1,71)); assert len(digs)==131 and sum(map(int,digs))==532
assert round(532/131,1)==4.1
# 1705963
sol=[(a,b,c) for a in range(1,40) for b in range(1,40) for c in range(1,40) if 25*a*a+29*b*b+37*c*c+12*a*b+48*a*c+10*b*c==28812]
assert sol==[(20,19,3)]
for a,b,c in [(1,2,3),(5,-1,7)]:
    assert 25*a*a+29*b*b+37*c*c+12*a*b+48*a*c+10*b*c==(3*a+2*b)**2+(5*b+c)**2+(4*a+6*c)**2
assert 3*28812==294**2
# 1705567
assert abs(sum(2*n/4**n for n in range(1,200))-8/9)<1e-14
# 1705590
assert 600//40*3==45
# 1704691
assert (17*60+15)-(8*60)==555
assert sum(1 for s in itertools.product('HT',repeat=5) if 'HH' not in ''.join(s))==13
nums=[n for n in range(100,1000) if set(str(n))<=set('2019')]
d=[n for n in nums if len(set(str(n)))==3]
assert F(sum(nums),len(nums))==433 and F(sum(d),len(d))==F(1288,3) and len(d)==18
# 1704482
Z=lambda n: sum(n//5**k for k in range(1,6))
v=[n for n in range(1,1000) if Z(n)==100]; assert v==[405,406,407,408,409] and v[0]+v[-1]==814
assert all(math.factorial(n)%10**100==0 and math.factorial(n)%10**101 for n in v)
# 252019
assert 2000*2000**20==2000**21
# 1704105
k,c,a=3,2,1.5; d=math.hypot(k,c)
vals=[(k+a*math.cos(t))**2+(c+a*math.sin(t))**2 for t in np.linspace(0,2*math.pi,200001)]
assert abs(max(vals)-(d+a)**2)<1e-6 and abs(min(vals)-(d-a)**2)<1e-6
k,c,a=0.3,0.2,2; d=math.hypot(k,c)
vals=[(k+a*math.cos(t))**2+(c+a*math.sin(t))**2 for t in np.linspace(0,2*math.pi,200001)]
assert abs(min(vals)-(d-a)**2)<1e-6
# 1704033
cnt=sum(1 for l in range(6) for j in range(4) for ch in range(13) if 12-l-j-ch>=0)
assert cnt==216 and math.comb(15,3)-(math.comb(9,3)+math.comb(11,3)-math.comb(5,3))==216
# 1703725
assert pow(657,315,1314)==657
print('ok3')
# 1704547
import numpy as np
for x in np.linspace(-20,20,40001):
    v=(2*x-1)*(x+1)*(x+7)
    if min(abs(x+7),abs(x+1),abs(x-0.5))>1e-9: assert (v>0)==((-7<x<-1) or x>0.5)
print('ok3b')
