import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(1)
# 1710811
for bb in [1,2,F(1,3),-5]:
    c=bb*16; a=2*c; assert a==32*bb
# 1711180
ks=[k for k in range(1,100001) if math.isqrt(48*k*k+1)**2==48*k*k+1]
assert ks==[1,14,195,2716,37829]
seq=[0,1]
for _ in range(5): seq.append(14*seq[-1]-seq[-2])
assert seq[1:6]==ks and 48*195**2+1==1351**2 and 48*14**2+1==97**2
# 1711161
sol=[(D,x) for D in range(1,100) for x in range(0,11) if D-x==13 and D-(10-x)==17]
assert sol==[(20,7)]
# 1710748
u=F(1); v=F(6,7)*u
assert 700/u+70/(2*u)==630/v
t=630/(2*u); rest=t-70/v; assert rest==F(700,3)/u and 700-rest*2*v==300
# 1710800
assert [n for n in range(1,100) if (2**n+1)%11==0 and (3**n-1)%13==0][0]==15
# 1710801
assert 729-2*243+0-27+9-3+2==224 and sum(d*(-3)**i for i,d in enumerate([2,1,1,1,0,2,1]))==224
# 1710592
assert 7*9+8*4+7==102
for a in range(8):
    for b in range(9):
        for c in range(8):
            if 9*a+4*b+c==34: assert a+b+c>=6
groups=[[9,9,4,4,4,4],[9,9,9,4,1,1,1],[9,9,4,4,4,1,1,1,1]]
assert all(sum(g)==34 for g in groups)
allc=sum(groups,[]); assert allc.count(9)==7 and allc.count(4)==8 and allc.count(1)==7
# 1710182
def st(n,k): return [(n+1)%k==0, n==2*k+5, (n+k)%3==0, all((n+7*k)%p for p in range(2,int((n+7*k)**.5)+1)) and n+7*k>1]
assert [(n,k) for n in range(1,2000) for k in range(1,2000) if sum(st(n,k))==3 and k<=n+1]==[(9,2),(17,6)]
# 1709573
r=F(2,3); assert 1+(2-r)**2==(1+r)**2
# 1710480
assert 8*math.comb(4,2)+8+4+2+1+1==64
# 1709513
a1=63-20; assert 3*a1+3*20==189 and 3*a1+12*20==369 and a1+9*20==223
assert 17+14*(-18)==-235 and 11*(-18)==-198
assert 152-8*19==0 and 152-8*20==-8
assert F(14+9,2)==F(23,2)
for _ in range(50):
    a=random.randint(-20,20); d=random.randint(-9,9); n=random.randint(1,30)
    S=lambda m: sum(a+i*d for i in range(m))
    assert S(3*n)==3*(S(2*n)-S(n))
L=[x for x in range(100,1000) if x%5==1]; assert len(L)==180 and L[89]==546 and L[90]==551
d=F(1,418); a=F(1,22)-18*d; assert a+21*d==F(1,19) and a+417*d==1
assert 2*(5*3+2)==(4*3-1)+(8*3-1) and 5*3+2==17
S=lambda m: F(m,2)*(2*6+(m-1)*(-4)); assert S(7)==-42 and S(21)==-714 and S(50)==-4600
# 1710170
for m in [-2,0,1,F(5,2),4]:
    g=lambda x: (2*m+3)*x-12
    for x in [-3,0,2,7]: assert 3*(2*x-g(x))-2==-3*(1+2*m)*x+34
    x=F(8-4*m,7-2*m); assert g(x)==4*(m-1)*x-4*(m+1)
m=F(7,2); assert all((2*m+3)*x-12!=4*(m-1)*x-4*(m+1) for x in range(-50,50))
# 1710139: all sets of 10 distinct positive integers with sum 62
cnt=0
def gen(start,k,s):
    if k==0:
        if s==0: yield ()
        return
    for x in range(start,s+1):
        if x*k+k*(k-1)//2>s: break
        for rest in gen(x+1,k-1,s-x): yield (x,)+rest
for t in gen(1,10,62):
    cnt+=1; assert math.prod(t)%60==0
assert cnt>0
# 1710185
for _ in range(200):
    A=np.array([0.,0.]);B=np.array([random.uniform(4,10),0.]);C=np.array([random.uniform(-3,12),random.uniform(1,8)])
    a=np.linalg.norm(C-B)
    if a>=B[0]: continue
    K=np.array([(B[0]-a)/2,0]);Lp=np.array([(B[0]+a)/2,0]);M=(A+C)/2
    assert abs((K-M)@(Lp-M))<1e-9
# 1710178
f=lambda x: math.sqrt((x-7)/2015)+math.sqrt((x-6)/2016)+math.sqrt((x-5)/2017)-math.sqrt((x-2015)/7)-math.sqrt((x-2016)/6)-math.sqrt((x-2017)/5)
assert abs(f(2022))<1e-12
for x in np.linspace(2017,3000,5001):
    if abs(x-2022)>1e-6: assert abs(f(x))>1e-9
# 1710138
s3=math.sqrt(3)
A,B,C,D=map(np.array,[(0,0),(6,0),(5,s3),(2,2*s3)])
ang=lambda P,Q,R: math.degrees(math.acos((P-Q)@(R-Q)/np.linalg.norm(P-Q)/np.linalg.norm(R-Q)))
assert abs(ang(D,A,B)-60)<1e-9 and abs(ang(A,B,C)-60)<1e-9 and abs(ang(A,D,C)-90)<1e-9
assert abs(np.linalg.norm(D-A)-4)<1e-12 and abs(np.linalg.norm(C-B)-2)<1e-12
assert abs(np.linalg.norm(C-A)-2*math.sqrt(7))<1e-12 and abs(np.linalg.norm(D-B)-2*math.sqrt(7))<1e-12
P=[A,B,C,D]; area=abs(sum(P[i][0]*P[(i+1)%4][1]-P[(i+1)%4][0]*P[i][1] for i in range(4)))/2
assert abs(area-7*s3)<1e-12
# 1710140
sol=[(m,w,27-m-w) for m in range(28) for w in range(28-m) if 12*m+3*w+2*(27-m-w)==78]
assert sol==[(0,24,3),(1,14,12),(2,4,21)]
# 1710133
L=72; assert F(L,6)+F(L,8)+F(L,12)+5+F(L,2)+4==L and 12+9+6+5==32 and 32+36==68
# 1710124
assert F(3,4)*240==F(4,5)*225==F(4,7)*315==180 and 240+225+315==780
# 1710125
C=180-126; B=180-80-C; assert (C,B)==(54,46)
# 1710135
assert F(12,10)*F(9,10)*F(1,2)==F(54,100)
# 1710118
cards=set(range(1,101))
Fa={c for c in cards if c%7==0}; Fa|={c for c in cards-Fa if '7' in str(c)}
rem=cards-Fa; La={c for c in rem if c%5==0}; La|={c for c in rem-La if '5' in str(c)}
assert (len(Fa),len(La))==(30,23)
L2={c for c in cards if c%5==0}; L2|={c for c in cards-L2 if '5' in str(c)}
rem=cards-L2; F2={c for c in rem if c%7==0}; F2|={c for c in rem-F2 if '7' in str(c)}
assert (len(L2),len(F2))==(28,25)
# 1709775
assert math.isqrt(100+576)==26 and 26*26==676 and 4*26==104
# 1709576
t=F(48,5); assert t/4+(24-t)/2==t and t*60==576
print('ok1')
