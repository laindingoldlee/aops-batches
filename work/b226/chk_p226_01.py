import math, itertools
from fractions import Fraction as F
import numpy as np
# 1762570 bisector locus
def aq(t):
    pa=math.hypot(t,1); pb=math.hypot(1-t,1); return pa/(pa+pb)
vals=[aq(t) for t in np.linspace(0,1,1001)]
assert all(x<y for x,y in zip(vals,vals[1:]))
assert abs(vals[-1]-vals[0]-(3-2*math.sqrt(2)))<1e-12
# 1762490 pizza
s=math.sin(math.pi/8); r=s/(1+s)
assert abs(r-(1-r)*s)<1e-12
assert abs(8*r*r-8*(2-math.sqrt(2))/(2+math.sqrt(2-math.sqrt(2)))**2)<1e-12 and round(8*r*r,3)==0.613
# 1762377
assert 43**2+11**2+7**2==2019 and pow(2019,2019,4)==3 and 2019==3*673
# 1762370 smallest number
from functools import lru_cache
digs=[1,0,2,2,3,4,5,6,7,8]+[9]*220
assert sum(digs)==2018 and len(digs)==230 and digs.count(0)==1 and all(d in digs for d in range(1,10))
assert 36+9*(228-8)<2018 and 36+9*(229-8)>=2018
# all multisets of 221 extra nonzero digits with shortfall 7: smallest sorted tuple
best=None
def parts(n,maxd):
    if n==0: yield []; return
    for d in range(min(n,maxd),0,-1):
        for p in parts(n-d,d): yield [d]+p
for p in parts(7,8):
    extra=[9-x for x in p]
    if len(extra)>221: continue
    ms=sorted(list(range(1,9))+extra+[9]*(221-len(extra)))
    num=[ms[0],0]+ms[1:]
    if best is None or num<best: best=num
assert best==digs
# 1762318
b,c=3,2; a=math.sqrt(19); x=b+c
assert abs((x+a)*(x-a)-b*c)<1e-12 and abs((b*b+c*c-a*a)/(2*b*c)+0.5)<1e-12
# 1762308
sol=[(x,y) for x in range(100) for y in range(100) if 100*y+x-5==2*(100*x+y)]
assert sol==[(31,63)]
# 1762175
x=F(-5,2); assert 2*x-3==4*x+2 and x*x-6==F(1,4)
# 1762096
assert 3+13==16
A=(12,5); assert A[0]**2+A[1]**2==169 and (16-12)**2+25==41 and F(16*5,2)==40
# 1762194
L=[1,2,9,31,255,480,4,15,63,127]
for T,rep in [(243,(127,63,31,9,9,4)),(248,(127,63,31,9,9,9)),(371,(255,63,31,9,9,4))]:
    assert sum(rep)==T and all(v in L for v in rep)
    sols=[cc for cc in itertools.combinations_with_replacement(sorted(L),6) if sum(cc)==T]
    assert sols==[tuple(sorted(rep))]
    assert not any(sum(cc)==T for k in range(1,6) for cc in itertools.combinations_with_replacement(L,k))
# 1761304
m=(-5+math.sqrt(41))/2
Pp=np.array([8/(4+m),8*m/(4+m)]); Q=np.array([8/(1+m),8*m/(1+m)]); Aa=np.array([0,8])
area=lambda P,Q,R: abs((Q[0]-P[0])*(R[1]-P[1])-(R[0]-P[0])*(Q[1]-P[1]))/2
assert abs(area(Aa,Pp,Q)-12)<1e-9 and abs(4*Pp[0]+Pp[1]-8)<1e-9 and abs(Q[0]+Q[1]-8)<1e-9
# 1762011
h=math.sqrt(3)/2
assert abs((2-math.sqrt(3))+4*(math.pi/12-0.25)-(1+math.pi/3-math.sqrt(3)))<1e-12
n=1500; g=(np.arange(n)+0.5)/n; X,Y=np.meshgrid(g,g)
inside=(X**2+Y**2<=1)&((X-1)**2+Y**2<=1)&((X-1)**2+(Y-1)**2<=1)&(X**2+(Y-1)**2<=1)
assert abs(inside.mean()-(1+math.pi/3-math.sqrt(3)))<1e-3
# 1761970
assert F(24,27)==F(8,9)
# 1761985
assert 9**2==81
# 1761309
sols=[(m_,n_) for m_ in range(-30,31) for n_ in range(-200,201) if 17*m_+3*n_==1]
assert all((m_+1)%3==0 and n_==6-17*((m_+1)//3) for m_,n_ in sols) and (-1,6) in sols and len(sols)==len([k for k in range(-30,31) if -30<=-1+3*k<=30 and -200<=6-17*k<=200])
# 1761719
def cnt(x1,y1,x2,y2):
    c=0
    for i in range(min(x1,x2),max(x1,x2)+1):
        for j in range(min(y1,y2),max(y1,y2)+1):
            if (i-x1)*(y2-y1)==(j-y1)*(x2-x1): c+=1
    return c
import random
random.seed(3)
for _ in range(300):
    p=[random.randint(-9,9) for _ in range(4)]
    if p[:2]==p[2:]: continue
    assert cnt(*p)==math.gcd(abs(p[2]-p[0]),abs(p[3]-p[1]))+1
assert cnt(3,-2,15,7)==4
# 1761969
d=[5,8,1,5,10,5]; assert F(sum(d),6)==F(17,3) and sorted(d)[2:4]==[5,5]
# 1761513
assert [(x,y) for x in range(1,200) for y in range(1,200) if x**y==y**(x-y)]==[(1,1),(8,2),(9,3)]
# 1761577
cnt2=0
for mask in itertools.product(range(3),repeat=8):
    A_={i+1 for i in range(8) if mask[i]==1}; B_={i+1 for i in range(8) if mask[i]==2}
    if len(A_)+len(B_) in A_ and len(A_)-len(B_) in B_: cnt2+=1
assert cnt2==294==63+156+75
# 1761688
def interior(n):
    return sum(1 for x in range(2,9) for y in range(2,n) if (y-1)*8<(x-1)*(n-1))
assert interior(162)==560 and interior(161)!=560 and interior(163)!=560
# 1761611
assert F(400-200,300)==F(2,3)
# 1760257
xs=np.roots([1,18,20]); assert all(abs(v*v+18*v+30-2*math.sqrt(v*v+18*v+45))<1e-9 for v in xs) and abs(np.prod(xs)-20)<1e-9
assert F(1,12)-F(1,24)-F(1,40)==F(1,60)
sols=[(x,y) for x in range(-50,51) for y in range(-200,201) if y*y+3*x*x*y*y==30*x*x+517]
assert sols and all(3*x*x*y*y==588 for x,y in sols)
# 1761574
assert sum(math.comb(i,3) for i in range(3,16))<2019<=sum(math.comb(i,3) for i in range(3,17))
s=set(itertools.permutations([7,7,8,8,8,9,9])); assert sum(all(a!=b for a,b in zip(p,p[1:])) for p in s)==38
assert math.gcd(2017,2019)==1 and math.gcd(2017,2018)==1 and math.gcd(2018,2019)==1
people=['Je','Jo','Sa','Js','Mr','Mrs','An'];c=0
for seats in itertools.permutations(range(10),7):
    dd=dict(zip(people,seats)); dist=lambda a,b: min((a-b)%10,(b-a)%10)
    if dist(dd['Je'],dd['Jo'])<3 or dist(dd['Sa'],dd['Js'])!=1: continue
    if not ((dd['Mrs']-dd['Mr'])%10 < (dd['An']-dd['Mr'])%10): continue
    c+=1
assert c==36000 and c//10==3600
N=0
for p in set(itertools.permutations('201820182019')):
    if p[0]=='0' or any(int(a)%2 and int(b)%2 for a,b in zip(p,p[1:])): continue
    N+=1
assert N==223440 and N//2==111720
assert sum(1 for t in itertools.product(range(0,26,1),repeat=4) if sum(t)<=25 and all(v%2 for v in t) and 25-sum(t)>0 and (25-sum(t))%2)==1001
# 1754925
f=lambda x: x**3+35*x**2-50*x+24
assert all(f(F(s_*dv))!=0 for dv in [1,2,3,4,6,8,12,24] for s_ in (1,-1))
assert f(-1)==108 and f(-24)==7560 and f(-36.4)<0<f(-36.3)
xs=np.linspace(-5,5,11); assert all(abs((x+2)*(x-3)*(x+5)*(x+6)-(x**4+10*x**3+13*x**2-96*x-180))<1e-6 for x in xs)
# 1761505
assert pow(2019,2019,10)==9 and 2019*2020//2==2039190 and math.comb(2019,2)==2037171
# 1761528 incentre equidistant (numeric)
A=np.array([0.9,3.2]);B=np.array([0,0]);C=np.array([5,0])
a=np.linalg.norm(B-C);bb=np.linalg.norm(A-C);cc=np.linalg.norm(A-B);I=(a*A+bb*B+cc*C)/(a+bb+cc)
dl=lambda P,U,V: abs((V-U)[0]*(P-U)[1]-(V-U)[1]*(P-U)[0])/np.linalg.norm(V-U)
assert abs(dl(I,A,B)-dl(I,B,C))<1e-12 and abs(dl(I,B,C)-dl(I,C,A))<1e-12
# 1761521
assert [n for n in range(1,3000) if pow(10,n,(n+1)*(n*n+1))==0]==[3,7]
