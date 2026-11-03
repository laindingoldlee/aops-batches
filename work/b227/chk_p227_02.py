import math, itertools, random
from fractions import Fraction as F
from collections import Counter
import numpy as np
rng=np.random.default_rng(3)
# 1755393
assert F(1,30)-F(1,50)==F(1,75) and 18*F(1,30)+20*F(1,50)==1
# 1756280
xs=np.linspace(-5,7,1201); assert all(((-3<x<=5) and not x<=2)==(2<x<=5) for x in xs)
# 1754490 (proof only)
# 1756743
assert ((-2+8)/2,(4+4)/2)==(3,4)
for y in range(-5,6): assert math.isclose(math.dist((3,y),(-2,4)),math.dist((3,y),(8,4)))
# 1756668
N=90; assert F(N,6)+F(N,3)==45 and N-F(N,3)-F(N,2)==15
# 1756531 (alias)
def divs(n): return [d for d in range(1,n+1) if n%d==0]
for n in range(1,300):
    P=math.prod(divs(n)); assert P*P==n**len(divs(n))
assert math.prod(divs(72))==2**18*3**12==72**6
# 1756275
for m in np.linspace(-3,0,301):
    b=1-m; assert (2<b<3)==(-2<m<-1)
# 1755042 q114
Pn=lambda n:n*(3*n-1)//2; assert [Pn(n) for n in range(1,6)]==[1,5,12,22,35] and Pn(20)==590
assert all(Pn(n)-Pn(n-1)==3*n-2 for n in range(2,30))
# q115
L=[100*a+10*b+c for a,b,c in itertools.permutations(range(1,10),3)]; assert len(L)==504 and F(sum(L),len(L))==555
# q118
vals=set()
for sc in itertools.combinations_with_replacement(range(1,80),5):
    if sum(sc)!=75 or sc[2]!=10 or sc[4]-sc[0]!=16: continue
    c=Counter(sc); mx=max(c.values()); md=[k for k in c if c[k]==mx]
    if md==[10]: vals.add(sc[0])
assert vals=={8,9,10}
# q119
f=[-2,-1,0,0,1,2]; assert F(sum(1 for t in itertools.product(f,repeat=3) if sum(t)==0),216)==F(19,108)
# 1755147
assert {abs(a+b) for a in (-1,-5) for b in (2,-4)}=={1,3,5,9}
assert all(abs(a+3)==2 for a in (-1,-5)) and all(abs(b+1)==3 for b in (2,-4))
# 1755144
assert all((abs(Fh-79)<=7)==(72<=Fh<=86) for Fh in range(50,110))
# 1754998 Monte Carlo
for n in range(2,7):
    x=rng.uniform(0,1,(600000,n)); est=np.mean(x.sum(1)<1); assert abs(est-1/math.factorial(n))<0.004
# 1754943
for n in range(1,5): assert 4**(2**n)+2**(2**n)==16**(2**(n-1))+4**(2**(n-1))
# 1754904
south=[4+6*k for k in range(20)]; north=[3+6*k for k in range(20)]
assert south[-1]==118 and north[-1]==117 and sum(len(str(x)) for x in south+north)==84
assert sum(len(str(x)) for x in south)==43
# 1753724
assert pow(2005,pow(2007,2009),7)==6
assert pow(2007,2009,6)==3
# 1753558
s3=6*1800/math.pi; assert abs(s3-1800-1637.7)<0.05 and abs(math.pi/6*s3-1800)<1e-9
# 1753565
assert all(a*(2*a*a+7)%3==0 for a in range(-300,300))
assert all((a*a+3)*(a*a+7)%32==0 for a in range(-301,301,2))
assert all((a**4+b**4-2)%16==0 for a in range(-51,51,2) for b in range(-51,51,2))
# 1754485 comboity: exact enumeration
cap={'C':1,'O':2,'M':1,'B':1}
import string
tot=0
for w in itertools.product(range(26),repeat=4):
    c=Counter(w); tot+=min(c[2],1)+min(c[12],1)+min(c[1],1)+min(c[14],2)   # C=2,M=12,B=1,O=14
assert F(tot,26**4)==F(269255,456976)
assert F(5)-F(5*25**4+4*25**3,26**4)==F(269255,456976)
def com(word):
    c=Counter(word.upper()); return sum(min(c[k],v) for k,v in cap.items())
assert com('bow')==2 and com('book')==3 and com('boook')==3
# 1754002 regular tetrahedron edge 6
A=np.array([0,0,0.]);B=np.array([6,0,0.]);C=np.array([3,3*math.sqrt(3),0]);D=np.array([3,math.sqrt(3),math.sqrt(24)])
V=abs(np.dot(B-A,np.cross(C-A,D-A)))/6; assert abs(V-18*math.sqrt(2))<1e-9
O=(A+B+C+D)/4; assert abs(O[2]-math.sqrt(6)/2)<1e-12   # distance to base face z=0
Sarea=4*math.sqrt(3)/4*36; assert abs(3*V/Sarea-math.sqrt(6)/2)<1e-12
# 1754302
assert [d for d in range(1,37) if 36%d==0 and math.isqrt(d)**2==d]==[1,4,9,36]
# 1754336
r=2/math.sqrt(5); assert abs(4*0.5*math.sqrt(5)*r-4)<1e-12 and round(4-math.pi*r*r,1)==1.5
# distance from O to line through (2,0),(0,1)
assert abs(abs(2*1-0)/math.hypot(1,2)-r)<1e-12
