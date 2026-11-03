import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(1)
# 1752850 cat sat csgo
vals=set()
for c,a,t in itertools.product(range(1,6),repeat=3):
    if c*a*t!=5: continue
    for s in range(1,76):
        if s*a*t!=75: continue
        for g in range(1,46):
            for o in range(1,46):
                if c*s*g*o==45: vals.add(c*a*t*s+g*o)
assert vals=={78}
# 1752843 soap
C=lambda b: 2*b if b<=3 else (2*(b-1) if b<=7 else 12)
assert all(C(b)==2*(b-b//4) for b in range(9)) and C(4)==6
# 1751545
sol=[(x,y) for y in range(1,2013) for x in range(1,2013) if x*y+2*y*y+3*x==2012*y]
assert sol==[(1003,3)]
# 1752607 (alias) mean 433
nums=[100*h+10*t+u for h in (1,2,9) for t in (0,1,2,9) for u in (0,1,2,9)]
assert F(sum(nums),len(nums))==433
# 1738877 Lagrange interpolation cycles
for n in range(1,7):
    a=random.sample(range(-50,50),n)
    def f(x):
        return sum(F(a[(i+1)%n])*math.prod(F(x-a[j],a[i]-a[j]) for j in range(n) if j!=i) for i in range(n))
    assert all(f(a[k])==a[(k+1)%n] for k in range(n))
# 1745114
assert 45376%4==0 and 76%4==0 and all(N%4==(N%100)%4 for N in range(1,100000,7))
# 1752482
good=sum(1 for s in itertools.product('HT',repeat=5) if 'HH' not in ''.join(s)); assert good==13
# 1751255 dice L+G and area
tot=sum(min(r)+max(r) for r in itertools.product(range(1,7),repeat=3)); assert F(tot,216)==7
assert F(72)*F(1,3)*F(1,2)==12
# 1752245 alias
v=(math.sqrt(2)-1)**(1-math.sqrt(3))/(math.sqrt(2)+1)**(1+math.sqrt(3)); assert abs(v-(3-2*math.sqrt(2)))<1e-12
# 1752100
for a in range(-50,50):
    for bb in range(1,20):
        q=(a-2*bb)//bb; r=a-q*bb; assert 2*bb<=r<3*bb
        assert sum(1 for qq in range(-200,200) if 2*bb<=a-qq*bb<3*bb)==1
assert all(math.isqrt(3*a*a-1)**2!=3*a*a-1 for a in range(1,10000))
assert all(pow(a,3,7) in (0,1,6) for a in range(-100,100))
# 1751902
f=lambda x:3*x-1; g=lambda x:-10-F(x+3,3)
assert f(-3)==-10 and f(3)==8 and g(-3)==-10 and g(12)==-15
# 1751778
N=2003**4-1997**4; assert N==192000432000 and sum(map(int,str(N)))==21
# 1751211 reflections
def refl(P,A,B):
    d=(B[0]-A[0],B[1]-A[1]); v=(P[0]-A[0],P[1]-A[1]); t=F(v[0]*d[0]+v[1]*d[1],d[0]**2+d[1]**2)
    return (2*(A[0]+t*d[0])-P[0],2*(A[1]+t*d[1])-P[1])
A=(2,7);B=(-2,0);Cc=(3,-1)
A1=refl(A,B,Cc);B1=refl(B,A1,Cc);A2=refl(A1,B1,Cc)
assert A1==(-1,-8) and B1==(F(32,5),F(-24,5)) and A2==(F(52,5),F(11,5))
assert F(A2[1]-7,1)/(A2[0]-2)==F(-4,7)
assert (2+2)**2+7**2==65 and 1+64==65
# 1751518
assert min(max(x,y) for x in range(1,20) for y in range(1,20) if x+y>=9)==5
# 1751489
x=1.7; assert abs(math.sqrt(4*x*x+x*x)-math.sqrt(9*x*x-4*x*x))<1e-12
# 1750915
L=[F('632.14'),F('632.15'),F('632.12'),F('632.14'),F('632.13'),F('632.16')]; assert sum(L)/6==F('632.14')
# 1750909 10 intersection points of the figure
def circ(c): return lambda p:(p[0]-c)**2+p[1]**2-1
el=lambda p:(p[0]/2.2)**2+(p[1]/0.5)**2-1
pts=[]
for c in (-0.6,0.6):
    th=np.linspace(0,2*np.pi,400001)
    X=c+np.cos(th);Y=np.sin(th);v=(X/2.2)**2+(Y/0.5)**2-1
    idx=np.where(np.sign(v[:-1])!=np.sign(v[1:]))[0]
    assert len(idx)==4
    pts+= [(round(X[i],4),round(Y[i],4)) for i in idx]
pts+=[(0,0.8),(0,-0.8)]
assert len(set(pts))==10
# 1750969
assert math.comb(8,2)*math.factorial(5)==3360
assert F(1,2)*2*F(7,2)+F(1,2)*F(7,4)==F(35,8)
xr=1.0; s1=2*xr/math.sqrt(3); s2=xr*math.sqrt(2/3)
assert abs((s2*math.sqrt(2)/2)**2+s2**2-xr**2)<1e-12 and abs(s1**3/s2**3-2*math.sqrt(2))<1e-12
# 1684977
assert [n for n in range(0,200) if math.comb(n,6)==math.comb(n,3)]==[0,1,2,9]
# 1751050
P=[(5,4),(8,-3),(1,-6),(-2,1)]
d=[(P[(i+1)%4][0]-P[i][0],P[(i+1)%4][1]-P[i][1]) for i in range(4)]
assert all(u[0]**2+u[1]**2==58 for u in d) and all(d[i][0]*d[(i+1)%4][0]+d[i][1]*d[(i+1)%4][1]==0 for i in range(4))
# 1750857
for _ in range(20000):
    x=-random.random(); y=random.random()
    if x>-1 and 0<y<1: assert x*x+y*y+x*y<1
# 1750568
assert math.hypot(12,9)==15 and F(4,16)*12==3
best=min(a+b+c+d for a in range(1,200) for b in range(a+1,200) for c in [2*b-a] for d in [c*c//b] if c>b and c*c%b==0 and d>c and F(c,b)==F(5,4)); assert best==73
dd=F(5*3825,6); assert dd==F(6375,2) and dd/450-dd/510==F(5,6)
