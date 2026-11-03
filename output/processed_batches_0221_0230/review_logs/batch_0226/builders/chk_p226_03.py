import math, itertools, datetime
from fractions import Fraction as F
# 1760410
best=None
for x3 in range(0,21):
    for x2 in range(0,101):
        x1=100-x2-x3
        if x1<0 or x1+2*x2+3*x3!=136: continue
        best=x2+x3 if best is None else min(best,x2+x3)
assert best==18 and 18+38+42+2==100
# 1759490
assert all(any(n==3*x+5*y for x in range(n) for y in range(n)) for n in range(8,300)) and not any(7==3*x+5*y for x in range(3) for y in range(2))
# 1760131
for n in range(1,40):
    assert sum(k**3 for k in range(1,n+1))==math.comb(n+1,2)**2
    U=range(1,n+2)
    if n<9:
        subs=list(itertools.combinations(U,2))
        for d in range(2,n+2):
            assert sum(1 for S in subs for T in subs if max(S+T)==d)==(d-1)**3
assert math.comb(2,2)**2!=1+8
# 1759713
assert math.gcd(2563,4147)==11 and 2563==11*233 and 4147==11*13*29
assert sum(math.comb(a+b,a) for a in range(6) for b in range(9) if 5*a+3*b==25)==22
for d in (5,-5):
    xs=[18+k*d for k in range(-2,3)]; assert F(sum(xs),5)==18 and F(sum(v*v for v in xs),5)==374 and max(xs)==28
assert F(1000*2000,400)==5000 and math.isqrt(26**2-10**2)==24
# 1759128
r,h=4,2
seg=r*r*math.acos((r-h)/r)-(r-h)*math.sqrt(2*r*h-h*h)
assert abs(seg-(16*math.pi/3-4*math.sqrt(3)))<1e-12 and abs(16*seg-157.2)<0.1
# numeric integration of segment
N=200000; dx=2*r/N
area=sum(max(0,min(-r+h,math.sqrt(r*r-x*x))-(-math.sqrt(r*r-x*x))) *dx for x in [(-r+(i+0.5)*dx) for i in range(N)] if True)
assert abs(area-seg)<1e-3
for k in (0.3,0.6,0.9):
    x=3/k; AC=math.sqrt(x*x-9); assert abs(AC-3*math.sqrt(1-k*k)/k)<1e-12
assert F(540*180)==97200 and abs(540*180/math.pi-30940)<1
assert len([t for t in itertools.product(range(7),repeat=4) if sum(t)==6])==84
# avg speed always < 2x
for v in [1,10,1000,1e9]: assert 2*1*v/(1+v)<2
# 1759881
import math as m
recipes=m.ceil(216/15); assert recipes==15 and recipes*2/6==5
# 1759676
import cmath
A=4+0j; C=4*cmath.exp(1j*2*math.pi/3); D=-4+0j; K=(C+D)/2
assert abs(abs(A-K)-2*math.sqrt(13))<1e-12
a,b_,c=13,7,4
a,b_,c=a-b_-c,2*b_,2*c; assert (a,b_,c)==(2,14,8)
a,b_,c=2*a,b_-a-c,2*c; assert (a,b_,c)==(4,4,16)
a,b_,c=2*a,2*b_,c-a-b_; assert (a,b_,c)==(8,8,8)
# 1705149
assert sum(1 for d in range(1,401) if 400%d==0)==15
# 1758550
x=(1+math.sqrt(5))/2; assert abs(x**3-x**2-x)<1e-12
# 1758680
good=lambda s: all(s%p for p in (3,5,7))
circ=[1,7,4,9,2,6,5,8,3]; assert all(good(circ[i]+circ[(i+1)%9]) for i in range(9))
sols=set()
for p in itertools.permutations(range(2,10)):
    c=(1,)+p
    if all(good(c[i]+c[(i+1)%9]) for i in range(9)): sols.add(c)
assert len(sols)==2  # the circle and its reflection, with 1 fixed in first place
# 1759512
a_,b2=1,1;S=0
for n in range(1,400): S+=F(a_,2**n); a_,b2=b2,a_+b2
assert abs(float(S)-2)<1e-10
fib=[1,1]
for _ in range(60): fib.append(fib[-1]+fib[-2])
assert all(fib[n-1]<=(5/3)**n for n in range(1,60))
# 1759213
for x in [F(2),F(-3),F(1,2)]:
    assert x/(1-x**3)-x/(1+x+x*x)==x*x/(1-x**3)
# 1759331
P=(F(-29,7),F(26,7)); assert P[1]==2*P[0]+12
assert (P[0]+6)**2+P[1]**2==P[0]**2+(P[1]-4)**2==F(845,49)
# 1759297
import numpy as np
xs=np.linspace(0.01,10,1000001); vals=8*xs**3+36*xs+54/xs+27/xs**3
assert abs(vals.min()-48*math.sqrt(6))<1e-6
# 1759282
assert sum(1 for n in range(1,2001) if sum(1 for d in range(1,math.isqrt(n)+1) if n%d==0)*2-(math.isqrt(n)**2==n) & 1)==44
# 1759220
best=min(np.hypot(t-1,2)+np.hypot(t-3,4) for t in np.linspace(0,4,400001))
assert abs(best-2*math.sqrt(10))<1e-6
assert abs(min(np.linspace(0,4,400001),key=lambda t: np.hypot(t-1,2)+np.hypot(t-3,4))-5/3)<1e-4
# 1759193
best=0
for y in range(1900,2101):
    d=datetime.date(y,1,1);fr=[]
    while d.year==y:
        if d.weekday()==4: fr.append(d.day)
        d+=datetime.timedelta(1)
    best=max(best,max(sum(fr[i:i+7]) for i in range(len(fr)-6)))
assert best==142 and 17+24+31+7+14+21+28==142
# 1759180
cnt=[]
for order in itertools.permutations(['D','S','P']):
    pos={d:i for i,d in enumerate(order)}
    for gr in itertools.permutations([6,7,8]):
        g=dict(zip(order,gr))
        for le in itertools.permutations(['r','g','b']):
            l=dict(zip(order,le))
            if pos['D']!=pos['S']+1 or pos['P']==0: continue
            if any(l[d]=='r' and g[d]!=7 for d in order): continue
            if l['S']=='g': continue
            if g['D']==6 and l['P']!='b': continue
            if g[order[0]]!=8: continue
            green=[d for d in order if l[d]=='g'][0]
            cnt.append(g[order[1]]*g['P']*g[green])
assert cnt==[252]
# 1758725
assert sum(1 for t in itertools.product(range(4),repeat=4) if sum(t)==6)==44
assert min(n for n in range(1,100) if n%6==0 and n%7==3)==24
c=0
for f in itertools.product(range(4),repeat=4):
    if any(f[i]==i for i in range(4)): continue
    if any(f[f[i]]==i for i in range(4)): c+=1
assert F(c,81)==F(17,27) and 17+27==44
assert math.lcm(44,24)==264 and sum(1 for d in range(1,265) if 264%d==0)==16
assert math.lcm(44,16,24)==528
dc=lambda n: sum(1 for d in range(1,n+1) if n%d==0)
mx=max(dc(n) for n in range(1,1000)); assert mx==32 and [n for n in range(1,1000) if dc(n)==32]==[840]
assert dc(720)==30 and dc(960)==28 and dc(630)==24
# 1759073
L=1.0; v=12; T=60
t_back=0.4*L/v; assert abs(t_back*T - 0)>=0  # train distance to entrance D: D/T = 0.4L/v
D=T*0.4*L/v; assert abs((D+L)/T-(0.6*L)/v)<1e-12
