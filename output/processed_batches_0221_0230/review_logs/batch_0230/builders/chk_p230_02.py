import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(2)
# 1734807 coupon collector: exact and simulation
E4=4*sum(F(1,k) for k in range(1,5)); assert E4==F(25,3)
tot=0
for _ in range(40000):
    seen=set();c=0
    while len(seen)<4: seen.add(random.randrange(4)); c+=1
    tot+=c
assert abs(tot/40000-25/3)<0.08
# 1736828 and 1737548: notched square region
sq=[np.array(c,float) for c in [[(0,0),(1,0),(1,1),(0,1)],[(4,0),(5,0),(5,1),(4,1)],[(4,4),(5,4),(5,5),(4,5)],[(0,4),(1,4),(1,5),(0,5)]]]
def overlap(P,Q):
    for poly in (P,Q):
        for i in range(len(poly)):
            e=poly[(i+1)%len(poly)]-poly[i]; ax=np.array([-e[1],e[0]])
            a=P@ax; b=Q@ax
            if a.max()<=b.min()+1e-9 or b.max()<=a.min()+1e-9: return False
    return True
def ok(T): return T.min()>=-1e-9 and T.max()<=5+1e-9 and not any(overlap(T,s) for s in sq)
def reg(cx,cy,th,s,n):
    r=s/(2*math.sin(math.pi/n)); return np.array([[cx+r*math.cos(th+2*math.pi*k/n),cy+r*math.sin(th+2*math.pi*k/n)] for k in range(n)])
a=(5-math.sqrt(5))/2
assert ok(np.array([(a,0),(5,a),(5-a,5),(0,5-a)])) and abs(a*a+(5-a)**2-15)<1e-12
assert ok(np.array([(2.5,0),(2.5+4/math.sqrt(3),4),(2.5-4/math.sqrt(3),4)]))
for n,smax in [(4,math.sqrt(15)),(3,8/math.sqrt(3))]:
    for _ in range(30000):
        T=reg(random.uniform(1,4),random.uniform(1,4),random.uniform(0,2*math.pi),smax+0.02,n)
        assert not ok(T)
# local search near the optimum does not beat the bound
for n,smax in [(4,math.sqrt(15)),(3,8/math.sqrt(3))]:
    best=0
    for _ in range(4):
        cx,cy,th=2.5,2.5,random.uniform(0,2*math.pi); s=0.5
        for it in range(500):
            c2=(cx+random.gauss(0,0.1),cy+random.gauss(0,0.1),th+random.gauss(0,0.1))
            lo,hi=0,7
            for _ in range(18):
                m=(lo+hi)/2
                if ok(reg(*c2,m,n)): lo=m
                else: hi=m
            if lo>s: cx,cy,th,s=*c2,lo
        best=max(best,s)
    assert best<smax+1e-3 and best>smax-0.08,(n,best,smax)
# 1733948
assert abs((19/20)**9/20-0.0315)<1e-3
# 1737138
d=40; assert F(d,20)+F(2*d,40)==4 and 3*d==120
# 1736178
from fractions import Fraction as Fr
def clip(poly,a,b,c):  # keep a x + b y <= c
    out=[]
    for i in range(len(poly)):
        P,Q=poly[i],poly[(i+1)%len(poly)]
        fp=a*P[0]+b*P[1]-c; fq=a*Q[0]+b*Q[1]-c
        if fp<=0: out.append(P)
        if fp*fq<0:
            t=fp/(fp-fq); out.append((P[0]+t*(Q[0]-P[0]),P[1]+t*(Q[1]-P[1])))
    return out
def area(p): return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[(i+1)%len(p)][0]*p[i][1] for i in range(len(p))))/2
T1=[(Fr(-4),Fr(2)),(Fr(1),Fr(2)),(Fr(-1),Fr(5))]; T2=[(-x,y) for x,y in T1][::-1]
p=T1
for i in range(3):
    P,Q=T2[i],T2[(i+1)%3]; a_,b_=Q[1]-P[1],P[0]-Q[0]; c_=a_*P[0]+b_*P[1]
    R=T2[(i+2)%3]
    if a_*R[0]+b_*R[1]>c_: a_,b_,c_=-a_,-b_,-c_
    p=clip(p,a_,b_,c_)
assert area(p)==Fr(3,2)
assert F(math.comb(8,4),256)==F(35,128)
ms=[m for n in range(3,400) for m in range(3,400) if F(360,n)-F(360,m)==45]; assert max(ms)==56
sol=[(a_,b_) for a_ in range(-20,20) for b_ in range(-20,20) if sorted([a_+1,2*a_-5,3*a_-10,b_+8,2*b_+5,3*b_+10])==[1,2,3,4,5,6]]
assert sol==[(4,-2)]
# 1736995
assert [x for x in range(-100,101) if (2*x+10)**2==4*(x-5)**2]==[0]
# 1736372
import sympy as sp
x=sp.symbols('x'); assert sp.expand((x-2)*(x-3)*(x+8))==x**3+3*x**2-34*x+48
# 1729625
assert F(20,1)/F(11,2)==F(40,11) and round(260+40/11)==264  # 264 min after noon = 16:24
assert [t for t in range(261,1440) if (11*t)%720 in (20,700)][0]==460  # 19:40 exact alternative
assert pow(2,2041,100)==52
assert sum(1 for s in itertools.product('BO',repeat=10) if 'OOO' not in ''.join(s))==504 and F(504,1024)==F(63,128)
# 1735431
assert sum(1 for a_ in range(1,10) for b_ in range(1,10) if 10-a_-b_>=1)==36
# 1736376
y=sp.symbols('y'); assert sp.expand((y-1)**3-8*(y-1)-12)==y**3-3*y**2-5*y-5
# 447574
assert 30*20/2==40*15/2==300 and 15**2+20**2==25**2
# 1736176
def cnt(n,s,strict):
    if strict:
        if s<=0 or n<=0: return 0
        t=1 if n==s else 0
        for a_ in range(1,s):
            if (n-a_)%3==0 and (n-a_)//3>0: t+=cnt((n-a_)//3,s-a_,True)
        return t
    if n==0: return 1 if s==0 else 0
    return sum(cnt((n-a_)//3,s-a_,False) for a_ in range(0,min(s,n)+1) if (n-a_)%3==0 and not (a_==0 and n==0))
assert cnt(2018,18,True)==11 and cnt(2018,18,False)==50
for co in [(2,3,1,2,3,7),(2,3,1,2,6,3,1),(2,3,1,5,2,4,1),(2,3,1,8,1,1,2),(2,3,4,1,3,4,1),(2,3,4,4,2,1,2),(2,6,3,1,3,1,2),(5,2,1,2,3,4,1),(5,2,1,5,2,1,2),(5,2,4,1,3,1,2),(8,1,1,2,3,1,2)]:
    assert sum(co)==18 and sum(c*3**i for i,c in enumerate(co))==2018
# 1501275
assert F(4,5)**2==F(16,25)
# 1731630
def tiles(w,h):
    c=0
    for i in range(w):
        for j in range(h):
            # does segment (0,0)-(w,h) pass through interior of [i,i+1]x[j,j+1]? check y-range of line over x in (i,i+1)
            y0=F(h*i,w); y1=F(h*(i+1),w)
            if max(y0,F(j))<min(y1,F(j+1)): c+=1
    return c
assert tiles(72,24)==72 and tiles(6,2)==6
assert [n for n in range(3,30) if 6*(n-2)**2==486]==[11] and 11**3==1331
assert sum('5' in str(i) for i in range(1,601))==195
e,a_=1,2; u,o,i_=6,4,3
assert i_+a_+e==6 and u+a_+e==9 and e+a_+o==7 and u+e==7 and 2*e+a_+o==8 and 2*o+a_+e==11 and len({a_,e,i_,o,u})==5
# 1735430
best=max(w[3]-w[0] for w in itertools.product(range(1,50),repeat=4) if list(w)==sorted(w) and sum(w)==48 and w[1]+w[2]==22)
assert best==24
assert F(1,80)+F(1,200)+F(1,400)==F(1,50)
# 1735512
# 82: Monte Carlo over random line directions through A=(0,0); circle B centre (2sqrt2,0) radius 2
hits=0
for _ in range(100000):
    t=random.uniform(0,math.pi); dist=abs(-math.sin(t)*2*math.sqrt(2)); hits+=dist<=2
assert abs(hits/100000-0.5)<0.01
cards=[2,3,5,6,7,10]; assert F(sum(1 for c in itertools.combinations(cards,2) if c[0]*c[1]%10==0),15)==F(7,15)
L=sorted(n for n in range(1000,2000) if sum(map(int,str(n)))==24); assert len(L)==15 and L[7]==1878
assert F(10,9)/(F(1,7)-F(1,9))==35
# 1736373
assert abs(25*math.pi-78.54)<0.005
# 1736642
for k in [3,4,5,10]:
    r=np.roots([1,0,-k,1]); assert np.allclose(r.imag,0) and abs(sum(r.real**3)+3)<1e-9
# 1736382
assert 100000/1.1>90909.09 and 100000/0.9<111111.12 and abs(100000-111000)<=0.1*111000 and not abs(111000-100000)<=10000
# 1735893
X,Y=sp.symbols('X Y'); assert sp.expand(13*(X**2+Y**2)-(3*X-2*Y-6)**2)==4*X**2+12*X*Y+9*Y**2+36*X-24*Y-36
p=3/math.sqrt(13); n_=np.array([3,-2])/math.sqrt(13); t_=np.array([2,3])/math.sqrt(13); V=np.array([9/13,-6/13])
for v in np.linspace(-4,4,9):
    P=V-(v*v/(4*p))*n_+v*t_; assert abs(np.linalg.norm(P)-abs(3*P[0]-2*P[1]-6)/math.sqrt(13))<1e-9
# 1736317
assert (90*20-90*5)/10-90==45
# 1735148
ab=[(a_,b_) for a_ in range(7,200) for b_ in range(a_,200) if a_*b_==6*(a_+b_)]
cd=[(c,d) for c in range(5,200) for d in range(c,200) if c*d==4*(c+d)]
m=[(p_,q_) for p_ in ab for q_ in cd if F(3*sum(p_),2*sum(q_))==F(3,2)]
assert m==[((10,15),(5,20))] and 10+15+5+20==50
# 1736204
assert math.factorial(98)+math.factorial(99)+math.factorial(100)==math.factorial(98)*10000
# 1501286
phi=math.acos(-math.sqrt(3)/8)
rts=sorted(4/math.sqrt(3)*math.cos((phi+2*math.pi*k)/3) for k in range(3))
assert np.allclose(sorted(np.roots([3,0,-12,2]).real),rts)
for r in rts: assert abs(3*r**3-12*r+2)<1e-9
# 1729507
d=sp.symbols('d'); assert sp.factor(d**3-174*d-308)==(d-14)*(d**2+14*d+22)
assert abs(math.asin(1/7)+math.asin(1/2)+math.asin(11/14)-math.pi/2)<1e-12
h=F(120,17); assert 8**2+15**2==17**2 and F(23,2)*h==F(1380,17) and math.gcd(1380,17)==1 and 1380-17==1363
pp=F(64,17); assert pp**2+h**2==64 and (17-pp)**2+h**2==225
r0=22*math.sqrt(3); assert abs((2*11/r0)/(1-121/r0**2)-24/r0)<1e-12 and abs(2*math.sqrt(3)*r0-132)<1e-9
s=132; base=math.sqrt(3)/4*s*s; Vv=base*24/3; sl=math.sqrt(24**2+r0**2); S_=base+3*0.5*s*sl; assert abs(3*Vv/S_-11)<1e-9
# 1736016
assert sum(1 for p_ in itertools.product(range(10),repeat=4) if p_[:3]!=(9,1,1))==9990
# 1735385
assert (-4)**2-(-3)**2==7 and (-4)*(-3)==12 and 256+81==337
print('chk_p230_02 ok')
