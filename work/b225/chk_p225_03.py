import math, itertools
from fractions import Fraction as F
import numpy as np
# 1764035
pr=list(itertools.product(range(1,7),repeat=4))
ev=[t for t in pr if math.prod(t)%2==0]
assert F(sum(1 for t in ev if sum(t)%2),len(ev))==F(8,15)
# 1763996
sols=[(a,b,c,d) for b in range(100,1166) for a in range(100,1700) for c in [1265-b] for d in [734-a] if c>=100 and d>=100 and a>max(b,c,d)]
assert {s[0] for s in sols}=={634}
# 1763749
assert sum(1 for t in itertools.product(range(1,7),repeat=4) if sum(t)==6)==10
# 1763617
assert 2**9<999<=2**10
# 1763563
f=lambda x:2018*(x*x+3)*(3*x*x+4)**2/(x*x+3)
xs=np.linspace(0,5,5001); assert xs[np.argmin(f(xs))]==0
# 1763615 area by lattice count approx and exact
assert 200*200//2==20000
# 1763579
assert sum(1 for a in range(1,11) for b in range(1,11) if b!=a and b<2*a)==65
# 1763629
assert sum(1 for X in range(0,13) for Y in range(-1,13) if 10-X-Y>=-1)==91
# 1763630
p=F(0)
for n in range(1,7): p+=F(1,6)*F(sum(math.comb(n,k) for k in range(0,n+1,2)),2**n)
assert p==F(1,2)
# 1763616
assert (99+1)**2==10000 and len(str(10**99))==100
# 1763566 q01 exact chain
probs=[F(4,7),F(2,7),F(1,7)]
dist={('A','B','C'):F(1)}; win=[]
for r in range(1,2019):
    nd={}; w=F(0)
    for o,pp in dist.items():
        for i in range(3):
            q=pp*probs[i]
            if o[i]=='A': w+=q
            no=tuple([z for z in o if z!=o[i]]+[o[i]]); nd[no]=nd.get(no,0)+q
    dist=nd; win.append(w)
assert win[2]==F(100,343) and win[0]==F(4,7) and win[1]==F(16,49)
qq=[w-F(1,3) for w in win]
assert all(qq[k+2]==-F(2,7)*qq[k+1]-F(9,49)*qq[k] for k in range(50))
d=abs(qq[2017]); assert d<F(1,10**300)
assert F(23,49)**3<F(10,96)
# q02 Heron rational = shoelace
import random; random.seed(3)
for _ in range(200):
    a,b,c,dd,e,f_=[F(random.randint(-30,30),random.randint(1,9)) for _ in range(6)]
    K=abs(a*(dd-f_)+c*(f_-b)+e*(b-dd))/2
    s1=math.dist((a,b),(c,dd));s2=math.dist((a,b),(e,f_));s3=math.dist((c,dd),(e,f_));g=(s1+s2+s3)/2
    assert abs(math.sqrt(max(0,g*(g-s1)*(g-s2)*(g-s3)))-float(K))<1e-6*(1+float(K))
# 1763571
assert sum(1+3*2**(2*k-5) for k in range(5,2019))%10==4
sols=[(a,b,c) for a in range(1,11) for b in range(1,12) for c in range(1,22) if a*a+b+c==112 and a+b*b+c==130 and a+b+c*c==460]
assert sols==[(9,10,21)]
# 1763561
c30=math.cos(math.pi/6); s30=0.5
O2=np.array([-c30,s30]); O3=np.array([0,3.0]); O3b=np.array([0,-3.0])
assert abs(np.dot(O2-O3,O2-O3)-7)<1e-12 and abs(np.dot(O2-O3b,O2-O3b)-13)<1e-12
assert 45+F(55,8)*8==100 and 5*F(55,8)==F(275,8)
# 1763513
import numpy.polynomial.polynomial as P
r=np.roots([1,0,-2,-2]); assert sum(1 for z in r if abs(z.imag)<1e-9)==1
assert 4/3*math.sqrt(2/3)<2
# 1763250
u=lambda n:n%10; t=lambda n:(n//10)%10
assert sum(pow(n,n+1,10) for n in range(1,2020))%10==4
A2=u(pow(2019,u(u(2019)**u(pow(2019,2019*u(2019),10)))*u(pow(2019,2018,10)**2019),10)); assert A2==9
E3=u(t(pow(2019,2019,100)))*2019**t(u(pow(2019,2018,10))); A3=t(pow(2019,E3,100)); assert A3==3 and E3==7
assert pow(2019,2019,100)==79
A4=u(pow(2019,2019**A3,10)+A2); assert A4==8
k=[2019]
for i in range(2018): k.append(u(pow(2019,k[-1],10)))
assert u(pow(2019,sum(k),10))==9 and sum(k)==20181
assert u(pow(A3,A2**A4,10))==3
# 1763183
y=math.sqrt(2); x=y**y
assert abs(y**(y**3)-x**(x**y))<1e-9 and abs(y**(y**y)-y**(x**(y+1)/2))<1e-9
lhs=y**(math.log((y**y)**(math.log(x)/math.log(y)))/math.log(y)); rhs=(x**2)**y/2
assert abs(lhs-rhs)<1e-9
# 1762366
W=np.array([2,1]);X=np.array([6,3]);Y=np.array([4,7]);Z=np.array([0,5])
sides=[np.linalg.norm(Q-R) for Q,R in [(W,X),(X,Y),(Y,Z),(Z,W)]]
assert max(sides)-min(sides)<1e-12 and np.dot(X-W,Z-W)==0 and abs(6*3-0*5)==18
ages=[5,5,8,8,8,9,10,11,11,33]; good=[]
for nn in range(0,300):
    Lr=sorted(ages+[nn]); cnts={v:Lr.count(v) for v in Lr}; mx=max(cnts.values()); md=[v for v in cnts if cnts[v]==mx]
    if len(md)==1 and F(sum(Lr),11)+Lr[5]+md[0]==Lr[-1]-Lr[0]: good.append(nn)
assert good==[13,35]
# 1763339
assert sum(1 for tt in itertools.product(range(20),repeat=4) if sum(tt)<=19)==math.comb(23,4)==8855
# 1762984
vx,vy=4,3; tm=12; assert vy*tm==9*vx and vx*tm==16*vy
# 1763216
assert 972-72*97==-6012
# 1762187
for (Bb,Cg) in [(70,50),(80,40),(45,60)]:
    Aa=180-Bb-Cg; BPC=180-(Bb-20)-(Cg-15); assert BPC-Aa==35
# 1763003
v=F(1265*10,230); assert v==55 and v*3600/5280==F(75,2)
# 1763222 brute force small analogue: n-ray partitional grid count formula check
def pts(n): return {(F(i,n//2),F(j,n//2)) for i in range(1,n//2) for j in range(1,n//2)}
assert len(pts(100)-pts(60))==2320
# 1762944
assert abs(8*math.tan(math.pi/3)-8*math.sqrt(3))<1e-12 and (8*math.sqrt(3))**2-192<1e-9
# 1762933
assert sum(1 for f_ in range(1,10) for l in range(10) if f_+l==10)*10**8==900000000
# 1762832 perpendicular in 24h (count crossings of relative angle 90/270)
c=0
for kk in range(0,100):
    for tgt in (90,270):
        tm=(tgt+360*kk)/330
        if 0<tm<24: c+=1
assert c==44
# 1757873
assert sum(1 for m in range(1,1000) if '1' in str(m))==271
x=math.radians(180/7); A=np.array([0,0]);Bv=3*np.array([math.cos(-math.pi/2-x/2),math.sin(-math.pi/2-x/2)]);Cv=3*np.array([math.cos(-math.pi/2+x/2),math.sin(-math.pi/2+x/2)])
tt=np.linalg.norm(Bv-Cv); D=tt*Cv/3; E=2*tt*math.cos(x)*Bv/3
for L in [np.linalg.norm(D-A),np.linalg.norm(E-D),np.linalg.norm(Cv-E)]: assert abs(L-tt)<1e-9
assert sum(m for m in range(100,1000) if int(str(m)[1:]+str(m)[0])-m==108 and int(str(m)[-1]+str(m)[:-1])-m==189)==3192
Sd=''.join(str(i) for i in range(1,101)); keep=len(Sd)-100
best=''; pos=0
for i in range(keep):
    win_=Sd[pos:len(Sd)-(keep-i)+1]; ch=max(win_); pos=pos+win_.index(ch)+1; best+=ch
assert len(Sd)==192 and best=='9999978'+''.join(str(i) for i in range(59,101))
# clock 3,4: count via exact event times
cnt=0
for kk in range(-2,20):
    for dval in range(1,8):
        cth=(25-dval*dval)/24; base=math.degrees(math.acos(cth))
        for ang in ({base,360-base} if 0<base<180 else {base%360}):
            tm=(ang+360*kk-(-30))/330   # relative angle minute-hour at 1:00 is -30
            if 0<tm<12: cnt+=1
assert cnt==132
# 1762815
def sqc(n): return sum((n-k+1)*(3-k+1) for k in range(1,4))
assert all(sqc(n)==6*n-4 for n in range(3,30))
# 1762708
assert sum(1 for m in range(1,100) if 2**8+1<=m**3<=2**18+1)==58
