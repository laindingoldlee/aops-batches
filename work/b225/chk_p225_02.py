import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(2)
cr=lambda u,v:u[0]*v[1]-u[1]*v[0]
# 1764320
assert sum(1 for n in range(1000,10000) if sum(map(int,str(n)))%2)==4500
# 1764322 median triangle
B=np.array([0.,0]);C=np.array([26.,0]);A=np.array([340/52,408/26])
assert abs(np.linalg.norm(A-B)-17)<1e-9 and abs(np.linalg.norm(A-C)-25)<1e-9
area=lambda a,b,c: math.sqrt(max(0,(a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c)))/4
assert abs(area(17,25,26)-204)<1e-9
ma=np.linalg.norm(A-(B+C)/2);mb=np.linalg.norm(B-(A+C)/2);mc=np.linalg.norm(C-(A+B)/2)
assert abs(area(ma,mb,mc)-153)<1e-6
# 1765275 trapezoid
Sx=np.array([0.,0]);P=np.array([36.,0]);Ap=np.array([5.,12]);O=np.array([31.,12]);M=np.array([18.,12])
ang=lambda U,V,W: math.degrees(math.acos(np.dot(U-V,W-V)/np.linalg.norm(U-V)/np.linalg.norm(W-V)))
assert abs(ang(Ap,Sx,M)-ang(M,Sx,P))<1e-9 and abs(ang(O,P,M)-ang(M,P,Sx))<1e-9
assert abs(np.linalg.norm(Ap-Sx)-13)<1e-12 and (26+36)//2*12==372
# 1765191 alternating harmonic partial sums -> ln2
s=sum((-1)**(n+1)/n for n in range(1,200001)); assert abs(s-math.log(2))<1e-5
# 1765183
s_=4*math.pi**(1/3); r=math.sqrt(3)*s_**2/(8*math.pi)
assert abs(math.sqrt(3)/4*s_**2-2*math.pi*r)<1e-9 and abs(math.pi*r*r-3*s_)<1e-9
assert abs(math.sqrt(3)/4*s_**2-4*math.sqrt(3)*math.pi**(2/3))<1e-9
# 1764326 enumerate colour orders
def gen(y,b,g):
    if y==b==g==0: yield ''; return
    if y:
        for t in gen(y-1,b,g): yield 'Y'+t
    if b:
        for t in gen(y,b-1,g): yield 'B'+t
    if g:
        for t in gen(y,b,g-1): yield 'G'+t
tot=c=0
for t in gen(3,4,6):
    tot+=1; c+= t.rfind('B')<t.rfind('G') and t.rfind('B')<t.rfind('Y')
assert F(c,tot)==F(153,455)
# 1764048 parts (sympy)
import sympy as sp
x,y,a,bb,n=sp.symbols('x y a b n')
assert (x**2+4*x-12).subs(x,2)==0
assert sp.expand((2*x+4)*(3*x-5))==6*x**2+2*x-20
assert sp.expand((x+1)*(x+2)*(x-3)*(x-4)+6-(x**2-2*x-5)*(x**2-2*x-6))==0
st=lambda p,q:p*q-p+q
assert sp.expand(st(x+y,x-y)-1-(x+y+1)*(x-y-1))==0
assert F(9,4)**2-F(9,4)-4*F(-3,8)**2-2*F(-3,8)==3 and F(9,4)-2*F(-3,8)==3 and F(9,4)+2*F(-3,8)==F(3,2)
assert sp.expand((x-2)*(x*y+5)-(x**2*y+5*x-2*x*y-10))==0
assert sp.expand((x-2)*(x-3)*(x+3)-(x**3-2*x**2-9*x+18))==0
assert math.prod(1-F(1,k*k) for k in range(2,11))==F(11,20)
assert sp.expand((a-bb+6)*(a+bb-6)-(a**2-bb**2+12*bb-36))==0
assert sp.expand((n**2+3*n+1)**2-(n**4+6*n**3+11*n**2+6*n+1))==0
r=(81**(1/3)+9**(1/3)+1)/8; assert abs(8*r**3-3*r*r-3*r-1)<1e-9
def dc(m): return sp.divisor_count(m)
ok=[k for k in range(1,3000) if dc(110*k**3)==110]
assert ok and all(dc(81*k**4)==325 for k in ok)
# 1765109 triangles in grid triangle: brute force over triples of lines
lines=[('v',i) for i in range(10)]+[('h',j) for j in range(10)]+[('d',10)]
def inter(l1,l2):
    (t1,c1),(t2,c2)=l1,l2
    if t1==t2: return None
    d={l1[0]:l1[1],l2[0]:l2[1]}
    if 'v' in d and 'h' in d: return (d['v'],d['h'])
    if 'v' in d: return (d['v'],10-d['v'])
    return (10-d['h'],d['h'])
cnt=0;iso=0
for L1,L2,L3 in itertools.combinations(lines,3):
    p=[inter(L1,L2),inter(L2,L3),inter(L1,L3)]
    if None in p or len(set(p))<3: continue
    if any(q[0]<0 or q[1]<0 or q[0]+q[1]>10 for q in p): continue
    cnt+=1
    ds=sorted(math.dist(p[i],p[j]) for i,j in [(0,1),(1,2),(0,2)])
    iso+= abs(ds[0]-ds[1])<1e-9 or abs(ds[1]-ds[2])<1e-9
assert cnt==iso==55
# 1764520
assert 33+11+3+1==48
v3=0;m=math.factorial(100)
while m%3==0: m//=3; v3+=1
assert v3==48
# 1764199
m=math.factorial(100);k=0
while m%8==0: m//=8;k+=1
assert k==32
# 1764218
assert math.perm(5,2)==20
# 1764798
assert 10*23-45>=180>10*22-45 and sum([23,22,21,20,19,18,17,16,15,9])==180
# 1763286 hexagon leash: integrate geodesic-distance region on a fine grid (vectorised, exact visibility via half-planes)
s=120.;Lh=600.
V=[np.array([s*math.cos(math.radians(-90+60*k)),s*math.sin(math.radians(-90+60*k))]) for k in range(6)]
phi=math.acos(math.sqrt(3)/6)
exact=381600*math.pi-129600*math.atan(math.sqrt(11))+10800*math.sqrt(11)-3600*math.sqrt(3)
assert abs(math.atan(math.sqrt(11))-(math.pi/2-math.asin(math.sqrt(3)/6)))<1e-12
# half-plane formula: half = 120000pi + 38400pi + clipped sector at V2 (numerical polar integration)
th=np.linspace(0,math.pi/3,2000001); R=360.;h=60*math.sqrt(3)
rr=np.minimum(R,h/np.maximum(np.sin(th),1e-300))
clip=np.trapezoid(0.5*rr**2,th)
assert abs(2*(120000*math.pi+38400*math.pi+clip)-exact)<1e-3
# Monte Carlo with geodesic distance
def inside(P):
    return all(cr(V[(k+1)%6]-V[k],P-V[k])>0 for k in range(6))
def seg_ok(Q,P):
    for t in np.linspace(0.002,0.998,120):
        if inside(Q+(P-Q)*t): return False
    return True
bd=[min(k,6-k)*s for k in range(6)]
rng=np.random.default_rng(5);N=40000;hit=0;Rb=800
for P in rng.uniform(-Rb,Rb,(N,2)):
    if inside(P): continue
    d=min(bd[k]+np.linalg.norm(P-V[k]) for k in range(6) if seg_ok(V[k],P))
    hit+=d<=Lh
est=hit/N*(2*Rb)**2
assert abs(est-exact)<0.02*exact
# 1764207
yv=F(5,8); assert F(1,4)+(1-yv)**2==yv**2 and (1+yv)/2*F(1,2)==F(13,32)
# 1763710
for a,b_,c in itertools.product(range(1,10),repeat=3):
    S=sum(10*p+q for p in (a,b_,c) for q in (a,b_,c)); assert S==33*(a+b_+c)
sol=sorted(100*a+10*b_+c for a,b_,c in itertools.product(range(1,10),repeat=3) if 33*(a+b_+c)==165)
assert sol==[113,122,131,212,221,311]
# 1764107
good=[(a,b_) for a in range(1,40) for b_ in range(1,40) if sorted(pow(a,k,b_) for k in range(1,b_+1))==list(range(b_))]
assert all(b_==1 for a,b_ in good) and len(good)==39
# 1760189
assert sum(1 for t in itertools.product(range(1,23),repeat=3) if 22-sum(t)>=1)==1330
cnt=lambda nn,k,lo: sum(1 for t in itertools.product(range(lo,nn+1),repeat=k) if sum(t)==nn)
assert [cnt(3,2,0),cnt(4,2,0),cnt(5,2,0),cnt(3,3,0),cnt(4,3,0),cnt(5,3,0),cnt(7,4,0)]==[4,5,6,10,15,21,120]
assert [cnt(3,2,1),cnt(4,2,1),cnt(5,2,1),cnt(3,3,1),cnt(4,3,1),cnt(5,3,1),cnt(7,4,1)]==[2,3,4,1,3,6,20]
assert sum(1 for t in itertools.product(range(10),repeat=6) if sum(t)<10)==5005
# 1763215 trapezoid for several x
for xx in [0.5,2,4,7]:
    D=np.array([0,0]);A=np.array([1,math.sqrt(3)]);Bq=np.array([1+xx,math.sqrt(3)]);Cq=np.array([2+xx,0])
    assert abs(np.linalg.norm(A-D)-2)<1e-12 and abs(np.linalg.norm(Bq-Cq)-2)<1e-12
