import math, itertools, random
from fractions import Fraction as F
import numpy as np
# 1785447
assert abs(0.8**4.5-512*math.sqrt(5)/3125)<1e-12 and abs(1-0.8**4.5-0.6336)<1e-3
# 1786990 alias: coordinates
O=np.zeros(3);P=np.array([0,0,1.]);A=np.array([1,1,0.]);B=np.array([-1,1,0.]);C=np.array([-1,-1,0.]);D=np.array([1,-1,0.])
Bp=B+(P-B)/4;Dp=D+(P-D)/5
n=np.cross(Bp-A,Dp-A)
t=np.dot(n,A-C)/np.dot(n,P-C);Cp=C+t*(P-C)
assert abs(np.linalg.norm(Cp-C)/np.linalg.norm(P-C)-7/19)<1e-12
# 1787427
assert 76-2*9==58 and 76+9==85
# 1787424
assert ((4+10)/2)**2==49
# 1787422
sc=[random.randint(0,100) for _ in range(20)]; y=7
assert abs(np.mean([s+y for s in sc])-(np.mean(sc)+y))<1e-9
# 1787280
assert F(sum(1 for a in range(1,7) for c in range(1,7) if a+c==9),36)==F(1,9)
# 1787277 alias
T=[(l,m) for l in range(5) for m in range(5)]
g=sum(all(any(i!=j and (t[i][0]==t[j][0] or t[i][1]==t[j][1]) for j in range(3)) for i in range(3)) for t in itertools.combinations(T,3))
assert g==500 and F(g,2300)==F(5,23)
# 1787262
assert 4==-3*(-2)+(-2) and 2==-3*5+17
# 1787120
A=np.array([-2,0.]);Pp=np.array([0,1.5]);d=(Pp-A)/np.linalg.norm(Pp-A)
tt=-2*np.dot(A,d); Cc=A+tt*d
assert abs(tt-3.2)<1e-12 and np.allclose(Cc,[14/25,48/25]) and abs(np.linalg.norm(Cc)-2)<1e-12
# 1786975
K=[n for n in range(1,1000) if n%4 and n%7]; assert K[78]==122
# 1785652
assert 70*40==80*35
# 1786099
assert (9*6)%25==4 and pow(9,-1,25)==14
# 1786616: brute force circular seatings of k labelled people in n seats up to rotation
def circ(k,n):
    seen=set()
    for perm in itertools.permutations(range(n),k):
        arr=[-1]*n
        for p,s in enumerate(perm): arr[s]=p
        seen.add(min(tuple(arr[(i+r)%n] for i in range(n)) for r in range(n)))
    return len(seen)
assert circ(5,6)==120
for n in range(1,7):
    for k in range(1,n+1): assert circ(k,n)==math.factorial(n-1)//math.factorial(n-k)
# 1765739
rng=random.Random(5)
for _ in range(20000):
    a,b,c=[rng.uniform(0.01,10) for _ in range(3)]
    assert a**3+b**3+c**3>=a*a*b+b*b*c+c*c*a-1e-9
# 1785946
t=math.sqrt(2)/2; assert abs(1-t-(1-t)**2/2-0.25)<1e-12 and abs((1-t)*math.sqrt(2)-(math.sqrt(2)-1))<1e-12
# 1786360
a=[2];
for n in range(1,200): a.append(a[-1]+n+2)
assert a[:6]==[2,5,9,14,20,27]
s=sum(F(a[n])/F(11)**n for n in range(200)); assert abs(float(s)-2.541)<1e-12
assert F(21,10)*F(121,100)==F(2541,1000)
# 1606524
x=F(40,3)
for _ in range(60): x=40/(3+x)
assert abs(float(x)-5)<1e-9 and F(245,267)<1
# 1786041
def der(n): return sum(1 for p in itertools.permutations(range(n)) if all(p[i]!=i for i in range(n)))
Dn=[None]+[der(n) for n in range(1,9)]
assert Dn[1:6]==[0,1,2,9,44]
for n in range(1,7): assert Dn[n+2]==(n+1)*(Dn[n+1]+Dn[n])
assert 2*Dn[4]+5*Dn[3]!=Dn[5]
# 1785634
assert F(F(1,2),F(1,3))-F(2,3)==F(5,6)
assert str(555555555555*2).count('0')==1
assert math.factorial(11)//10==3991680 and str(3991680).count('1')==1
ds=[18+8-2*math.sqrt(2),18-8+2*math.sqrt(2),12,24,18,18]; assert abs(sum(ds)/6-18)<1e-12 and min(ds)>0
s_=4*math.sqrt(2);P=np.array([1,1])/math.sqrt(2)
V=[np.array(v) for v in [(0,0),(0,s_),(s_,s_),(s_,0)]]
assert np.allclose([np.linalg.norm(P-v) for v in V],[1,5,7,5]) and abs(s_**2-32)<1e-12
# 1786654 alias
u=np.random.default_rng(7).uniform(0,1,(300000,3)); assert abs(np.mean(u.sum(1)<1)-1/6)<0.003
# 1786839 alias
tens=set()
for a,b_,c in itertools.product(range(1,10),repeat=3):
    if ((10*a+7)*(10*b_+7)*(10*c+7)//10)%10==5: tens.add(((10*a+7)+(10*b_+7)+(10*c+7))//10%10)
assert tens=={1}
# 1786656 alias
g=sum(1 for t in itertools.product(range(1,7),repeat=3) if any(t[i]+t[j]==6 for i,j in [(0,1),(0,2),(1,2)]))
assert F(g,216)==F(19,54)
# 1654926 alias
def las(s):
    out='';i=0
    while i<len(s):
        j=i
        while j<len(s) and s[j]==s[i]: j+=1
        out+=str(j-i)+s[i];i=j
    return out
assert las('1211')=='111221' and las('111221')=='312211'
