import math, itertools, random
from fractions import Fraction as F
random.seed(2)
sq=lambda n: n>=0 and math.isqrt(n)**2==n
# 1746517
for S in ([-94,95,130,194],[386,2114,3970,10430],[7442,28658,148583,177458,763442]):
    assert len(set(S))==len(S) and all(sq(x+y) for x,y in itertools.combinations(S,2))
assert 1+18**2==6**2+17**2==10**2+15**2==325 and 50**2+120**2==66**2+112**2==104**2+78**2==16900
assert (1+36-225)//2==-94 and (2500+4356-6084)//2==386
# 1749804
assert 64**(1/3)-4<1e-9 and abs(math.sqrt(math.sqrt(64))-2*math.sqrt(2))<1e-12
# 1750183
f=lambda x:(1+x*x)/(1+math.sqrt(1+x*x))+(1-x*x)/(1-math.sqrt(1-x*x))-1
x0=(3/4)**0.25; assert abs(f(x0))<1e-12 and abs(f(-x0))<1e-12 and abs(x0-12**0.25/2)<1e-12
xs=[i/100000 for i in range(1,100001)]
ch=[x for a,x in zip(xs,xs[1:]) if (f(a)>0)!=(f(x)>0)]
assert len(ch)==1 and abs(ch[0]-x0)<1e-4
# 1750115
assert pow(13,2003,10)==7
# 1748211
cnt=0
for m in range(1,10**6+1):
    if 10**6%m==0: cnt+=2
assert cnt==98
pts=set()
N=2000**2
for d in range(1,N+1):
    if N%d==0:
        e=N//d
        if (d+e)%2==0:
            for s in (1,-1):
                pts.add((s*(d+e)//2,s*(e-d)//2))
assert len(pts)==98 and all(x*x-y*y==N for x,y in pts)
# 1750121
assert pow(6,1999,37)==31
# 1750117
assert all(n%math.gcd(a,a+n)==0 for a in range(-60,60) for n in range(1,40))
# 1750107
assert all(not sq(a*a+b*b) for a in range(1,200,2) for b in range(1,200,2))
assert all(n*(n+1)*(n+2)*(n+3)+1==(n*n+3*n+1)**2 for n in range(-50,50))
assert all(((n+1)**3-n**3)%2==1 for n in range(-100,100))
# 1749896 (alias) value
v=2*400.0
for k in range(399,0,-1): v=2*k+(2*k+1)/v
assert abs(1/v-0.3797319547)<1e-9
# 1749330
P=[p for p in range(2,400) if all(p%d for d in range(2,int(p**.5)+1))];PS=set(P)
best=min(5*a+10*d for a in P for d in range(1,100) if all(a+k*d in PS for k in range(5)))
assert best==85 and all(x in PS for x in (5,11,17,23,29))
# 1749903 (alias)
assert all(math.comb(n,k)==math.comb(n-1,k-1)+math.comb(n-1,k) for n in range(1,30) for k in range(1,n+1))
# 1748599
assert math.perm(5,4)*math.perm(10,6)==18144000
cnt=0
for pos in range(0,7):   # block start (0-indexed) of 4 consecutive acoustic songs
    if pos>=5 and pos+3<=8: cnt+=1
assert cnt==1
assert round((F(41,64)-F(13,24))*100)==10 and (54-41,34-23)==(13,11)
T=78; assert F(312+T,5)==T and sorted([86,72,61,93,T])[2]==T
assert F(1000)*F(135,100)*F(85,100)*F(106,100)==F(121635,100)
# 1749760
assert F(sum(sum(r) for r in itertools.product(range(1,7),repeat=3)),216)==F(21,2)
# 1749553 (alias)
assert sum(1 for f in itertools.product(range(5),repeat=6) if len(set(f))==5)==1800
# 1749495
a,b,c=3.,4.,12.; assert math.dist((0,0,0),(a,b,c))==13
# 1749683
assert pow(5,2012,7)==4 and pow(13,2012,10)==1
# 1749222
assert sum(1 for n in range(100,1000) if set(str(n))<={'2','5'})==8
# 1749682
assert round(7.41/0.13)==57 and 36+21==57 and 36-21==15
# 1749365
assert F(235,100)*10+F(55,10)*12==F(895,10) and F(235,100)*10==F(235,10)
# 1749458
for n in range(2,8):
    inc=sum(1 for m in range(10**(n-1),10**n) if all(x<y for x,y in zip(str(m),str(m)[1:])))
    dec=sum(1 for m in range(10**(n-1),10**n) if all(x>y for x,y in zip(str(m),str(m)[1:])))
    assert inc==math.comb(9,n) and dec==math.comb(10,n)
# 1749150
assert all(16*a*a*64==(4*8*a)**2 for a in range(1,50))
# 1749331
r3=math.sqrt(3); assert abs(math.hypot(2*r3,2)-4)<1e-12 and 4*2==8
# 1749345
x=F(2,3); assert 11-3*x==13-4 and 6*x==4
# 1748689 trapezoid: random checks of EB||DP => EC||AP
for _ in range(500):
    a,b=random.uniform(-3,3),random.uniform(1,6); c=random.uniform(1,8); h=random.uniform(1,5)
    A=(a,h);B=(b,h);Cq=(c,0);D=(0,0)
    t=random.uniform(0.05,0.95)
    den=t*(b-a)+(1-t)*c
    if abs(den)<1e-6: continue
    s=(1-t)*c/den
    if not 0<s<1: continue
    E=(t*a,t*h);P=(c+s*(b-c),s*h)
    cr=lambda u,v:u[0]*v[1]-u[1]*v[0]
    assert abs(cr((B[0]-E[0],B[1]-E[1]),(P[0]-D[0],P[1]-D[1])))<1e-9
    assert abs(cr((Cq[0]-E[0],Cq[1]-E[1]),(P[0]-A[0],P[1]-A[1])))<1e-9
# 1749316
assert [(x,y) for x in range(1,10) for y in range(1,10) if F(x,8)+F(y,5)==F(31,40)]==[(3,2)]
# 1749176
sc=set()
for h in itertools.combinations(range(1,15),7):
    s=sum(h); sc.add(min(s,105-s))
assert sc==set(range(28,53)) and len(sc)==25
assert 29*36/261==4 and 29*36/3-261==87
assert sum(1 for x in range(13) for y in range(13) if x>=2 and y>=2 and 12-x-y>=2)==28
