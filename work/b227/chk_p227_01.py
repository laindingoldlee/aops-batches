import math, itertools, random
from fractions import Fraction as F
from collections import Counter
import numpy as np
random.seed(1)
# 1758922 UKMT
L=sorted(''.join(p) for p in itertools.permutations('UKMIC')); assert L[0]=='CIKMU' and L.index('UKIMC')+1==112
# 1758855 / 1758503 hypotenuse
hyp=set(c for a in range(1,300) for b in range(a,300) for c in [math.isqrt(a*a+b*b)] if c*c==a*a+b*b)
assert all(c in hyp for c in (39,40,41)) and 42 not in hyp
assert 15**2+36**2==39**2 and 24**2+32**2==40**2 and 9**2+40**2==41**2
# 1758744
g=lambda x:x**3-2*x**2-16*x+32
assert g(2)==0 and g(-2)==48 and g(-8)==-480 and g(16)==3360
assert all(g(x)==(x-2)*(x-4)*(x+4) for x in range(-10,10))
# 1758734
for x in np.linspace(-20,20,4001):
    assert (-2*abs(x-4)+8<=-4+1e-12)==(x<=-2+1e-9 or x>=10-1e-9)
# 1758642 totient
def phi(n): return sum(1 for k in range(1,n+1) if math.gcd(k,n)==1)
ph=[0]+[phi(n) for n in range(1,402)]
for n in range(2,400): assert n*ph[n]+(n+1)*ph[n+1]<=2*n*n
for n in range(2,40): assert phi(n*n)==n*ph[n]
# 1758750
assert 17*67==1139 and 17+67==84
# 1758747
assert 9*2+4==22
# 1755354
assert sum(pow(2,-k,13) for k in range(1,7))%13==2
# 1758380
assert abs(2.02-2*0.01-2)<1e-12
# 1758669 Descartes
p=np.poly1d([27,51,-300,1,-49,-52,178,-37]); rr=sorted(x.real for x in p.r if abs(x.imag)<1e-9)
assert sum(1 for x in rr if x>0)==3 and sum(1 for x in rr if x<0)==2
assert p(-5)<0 and p(-1)==107 and p(0)==-37 and p(0.5)>0 and p(1)==-181 and p(3)>0
c=[27,51,-300,1,-49,-52,178,-37]; ch=lambda c: sum(1 for a,b in zip(c,c[1:]) if a*b<0)
assert ch(c)==5 and ch([a*(-1)**(7-i) for i,a in enumerate(c)])==2
# 1757851 phone (alias)
for _ in range(50):
    s=''.join(random.choice('0123456789') for _ in range(6))
    assert len({s[:i]+d+s[i:] for i in range(7) for d in '0123456789'})==64
# 1758503 q02
ds=set(a*a-b*b for a in range(1,2100) for b in range(1,a))
assert sum(1 for n in range(1,2011) if n not in ds)==505
# 1758419
assert abs(-2+math.sqrt(3)+0.3)<0.05 and abs(-2-math.sqrt(3)+3.7)<0.05
assert all(6*x*x+5*x-6==(3*x-2)*(2*x+3) for x in range(-5,6))
# 1747860 penalty box: exact Markov computation
from functools import lru_cache
p1=F(1,6)
@lru_cache(None)
def P(rem,turn):
    # rem: tuple of remaining players in order of play starting with 'turn' index into rem; returns prob Piper(0) last
    if len(rem)==1: return F(1) if rem[0]==0 else F(0)
    # cycle until someone escapes: player i (position k from turn) escapes first
    n=len(rem); q=1-p1; tot=F(0)
    for k in range(n):
        pr=q**k*p1/(1-q**n); idx=(turn+k)%n; new=rem[:idx]+rem[idx+1:]
        tot+=pr*P(new, idx%len(new))
    return tot
assert P((0,1,2),0)==F(305,1001)
# 1758425
assert (1j)*(6j)*(4+6j)==-24-36j
# 1758208
assert math.log2(16)==4 and 3<math.log2(10)<4
# 1757353
a=[8,13,18,23,28]; assert sum(a)==90 and sum(x*x for x in a)==5*374
base=[5,5,8,8,8,9,10,11,11,33]; sols=[]
for n in range(1,500):
    s=sorted(base+[n]); cc=Counter(s); mx=max(cc.values()); md=[k for k in cc if cc[k]==mx]
    if len(md)==1 and F(sum(s),11)+s[5]+md[0]==s[-1]-s[0]: sols.append(n)
assert sols==[13,35]
r=[4,6,9]; assert sum(r)==19 and 6*6==4*9 and r[0]*r[1]+r[0]*r[2]+r[1]*r[2]==114 and -r[0]*r[1]*r[2]==-216
gp=[(u,v,w) for u in range(1,20) for v in range(u,20) for w in range(v,20) if u+v+w==19 and v*v==u*w]; assert gp==[(4,6,9)]
# 1757894
S=sum(F(1,k**3+k+1) for k in range(2,2019)); assert S<F(1,6) and F(1,11)+F(1,31)+F(1,24)==F(1349,8184)<F(1,6)
# 1758037
assert {x*x-y*y for x,y in [(9,1),(1,9)]}=={80,-80}
# 1757623
assert [n for n in range(1,201) if sum(int(d)**2 for d in str(n))==n]==[1]
# 1757647
assert all(9*x*x-6*x+1>=0 for x in np.linspace(-5,5,1001))
assert all(((x*x-4*x-45)<=0)==(-5<=x<=9) for x in range(-30,30))
# 1757367
sol=set()
for a_ in range(1,300):
    for b_ in range(a_,300):
        if a_*b_==6*(a_+b_):
            for c_ in range(1,300):
                for d_ in range(c_,300):
                    if c_*d_==4*(c_+d_) and F(a_*b_,c_*d_)==F(3,2): sol.add(a_+b_+c_+d_)
assert sol=={50}
pts=np.random.default_rng(2).uniform(0,10,(400000,2)); assert abs(np.mean(abs(pts[:,0]-pts[:,1])<3)-0.51)<0.005
# 1754235
assert 19997**2-19994**2==119973
# knights: simulate backwards
people=[]  # people remaining after day d, built backwards
types={}
rem=[]
for d in range(2019,0,-1):
    k=sum(rem); n=len(rem)-k
    t=1 if k==n else 0; types[d]=t; rem.append(t)
assert sum(1-t for t in types.values())==1009
assert sum(1 for c in itertools.combinations(range(7),3) if all(b-a>=2 for a,b in zip(c,c[1:])))==10
best=min(x+y for x in range(60) for y in range(30) if 19*x+41*y==1000); assert best==26
assert F(1,2)/(F(1,2)+F(1,5)+F(1,8))*132000==80000
