import math, itertools, random
from fractions import Fraction as F
import sympy as sp
random.seed(5)
C=math.comb
# 1713423
assert abs((2**(1/5))**5-2)<1e-12 and 1<2**(1/5)<2
for p in range(1,40):
    for q in range(2,40):
        if math.gcd(p,q)==1: assert (F(p,q)**5).denominator!=1
# 1712750
assert pow(2,200,13)==9
# 1713347: AP^2 = r^2 + AH*HA1, equal for all three, numerically
def foot(P,X,Y):
    d=(Y[0]-X[0],Y[1]-X[1]); t=((P[0]-X[0])*d[0]+(P[1]-X[1])*d[1])/(d[0]**2+d[1]**2); return (X[0]+t*d[0],X[1]+t*d[1])
def orth(A,B,Cc):
    import numpy as np
    M=np.array([[Cc[0]-B[0],Cc[1]-B[1]],[Cc[0]-A[0],Cc[1]-A[1]]]); rhs=np.array([A[0]*(Cc[0]-B[0])+A[1]*(Cc[1]-B[1]),B[0]*(Cc[0]-A[0])+B[1]*(Cc[1]-A[1])])
    return tuple(np.linalg.solve(M,rhs))
def hits(X,Y,H,r):
    u=(Y[0]-X[0],Y[1]-X[1]); L=math.hypot(*u); u=(u[0]/L,u[1]/L); w=(Y[0]-H[0],Y[1]-H[1])
    b=w[0]*u[0]+w[1]*u[1]; c=w[0]**2+w[1]**2-r*r; s=math.sqrt(b*b-c)
    return [(Y[0]+t*u[0],Y[1]+t*u[1]) for t in (-b+s,-b-s)]
cnt=0
while cnt<500:
    A,B,Cc=[(random.uniform(-5,5),random.uniform(-5,5)) for _ in range(3)]
    def ang(P,Q,R):
        v=(Q[0]-P[0],Q[1]-P[1]);w=(R[0]-P[0],R[1]-P[1]);return v[0]*w[0]+v[1]*w[1]
    if min(ang(A,B,Cc),ang(B,A,Cc),ang(Cc,A,B))<=0.5: continue
    H=orth(A,B,Cc); r=max(math.dist(H,P) for P in (A,B,Cc))+random.uniform(0.1,3)
    D=((B[0]+Cc[0])/2,(B[1]+Cc[1])/2);E=((Cc[0]+A[0])/2,(Cc[1]+A[1])/2);Fm=((A[0]+B[0])/2,(A[1]+B[1])/2)
    vals=[math.dist(A,P) for P in hits(E,Fm,H,r)]+[math.dist(B,Q) for Q in hits(Fm,D,H,r)]+[math.dist(Cc,R) for R in hits(D,E,H,r)]
    A1=foot(A,B,Cc)
    assert max(vals)-min(vals)<1e-7 and abs(vals[0]**2-(r*r+math.dist(A,H)*math.dist(H,A1)))<1e-7
    cnt+=1
# 1713302
for m in range(2,60):
    for n in range(1,m):
        a,b,c=m*m-n*n,2*m*n,m*m+n*n
        assert a%3==0 or b%3==0
# 1713055
s3,s2,s6=math.sqrt(3),math.sqrt(2),math.sqrt(6)
AC=12*math.sin(math.radians(75))/math.sin(math.radians(45)); BC=12*math.sin(math.radians(60))/math.sin(math.radians(45))
assert math.isclose(AC,6+6*s3) and math.isclose(BC,6*s6) and math.isclose(12+AC+BC,18+6*s3+6*s6)
# 1711204
def z(n):
    t=0;p=5
    while p<=n: t+=n//p;p*=5
    return t
assert z(420)==103 and z(103)==24
# 1698023
assert F(54)/F(3,2)==36
# 1712659
assert 3*2*5==30
# 1712621
D_=20*s3/math.sin(math.radians(105))
assert math.isclose(D_*0.5,30*s2-10*s6) and math.isclose(D_*math.sin(math.radians(45)),60-20*s3)
# 1711916 q01
assert math.isclose(math.pi*4.8**2*10/3,76.8*math.pi) and round(76.8*math.pi,1)==241.3
# 1711916 q02
c8=[k for k in range(60) if 10**7<=2**k<10**8]
assert c8==[24,25,26] and [k for k in c8 if sorted(str(2**k))==sorted('23334455')]==[25]
# 1711916 q03
assert round(C(20,10)/2**20,3)==0.176
# 1711916 q04
ways=0
for k in range(2,4039):
    num=4038-k*(k-1)
    if num%(2*k)==0: ways+=1
assert ways==7
# 1711916 q05
d=F(3,2); r2=64+d*d
assert r2==36+(d+4)**2 and r2-(d+2)**2==54 and math.isclose(2*math.sqrt(54),6*s6)
# 1712099
sols=[N for N in range(-100000,100001) if (N*N-71)%(7*N+55)==0]
assert sols==[-8,57]
# 1712340
P=77837760000
assert sp.factorint(P)=={2:9,3:5,5:4,7:1,11:1,13:1}
S10=[s for s in itertools.combinations(range(1,21),10) if math.prod(s)==P]
assert S10==[(5,9,10,11,13,14,15,16,18,20)] and sum(S10[0])==131
# 1690790
assert pow(120,300,1000)==0
# 1711274
assert all((n**4-n**3+n*n-n)%2==0 for n in range(-200,200))
# 1711594
assert sum(1 for n in range(7001,9000) if int(str(n)[0])==sum(map(int,str(n)[1:])))==81
# 1711919
A=(6,8);B=(0,0);Cc=(21,0)
G=(F(27,3),F(8,3)); assert G==(9,F(8,3))
a,b,c=21,17,10; assert math.dist(B,Cc)==21 and math.dist(Cc,A)==17 and math.dist(A,B)==10
I=((a*6+c*21)/48,(a*8)/48); assert I==(7,3.5)
H=(6,F(45,4)); assert 6*(H[0]-21)+8*H[1]==0 and 15*H[0]-8*H[1]==0
# 1712197
for e in range(1,41):
    for f in range(1,41):
        for g in range(1,41):
            cond=((g*g-f*f)-e*e)%((e+f+g)**2)==0
            assert cond==(e*e+f*f==g*g)
# 1648327
assert math.sqrt(1/1)==1
# 1712010
xx,yy=sp.symbols('x y')
assert sp.expand(4*(xx-2)**2+9*(yy+3)**2-36-(4*xx**2+9*yy**2-16*xx+54*yy+61))==0
# 1711366
assert F(1,34)*60==F(30,17)
# 1711063
n=sp.symbols('n')
assert sp.expand((n-1)*(n-2)*(n+2)*(n+3)-(n**4+2*n**3-7*n**2-8*n+12))==0
assert sum(F(k**4+2*k**3-7*k*k-8*k+12,4*C(k-1,2)) for k in range(3,11))==344
# 1711299
assert not any(sp.isprime(p) and sp.isprime(p+7) for p in range(1,10000))
# 1710875
xx,yy=sp.symbols('x y')
assert sp.expand((xx-yy)*(xx*xx+xx*yy+yy*yy))==xx**3-yy**3 and sp.expand((xx+yy)*(xx*xx-xx*yy+yy*yy))==xx**3+yy**3
print('chk_p234_03 ok')
