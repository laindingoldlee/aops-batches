import math, itertools
from fractions import Fraction as F
import numpy as np
# 1744764 mass points: FG:GB = 24:49
A=np.array([0.,0.]);B=np.array([8.,0.]);C=np.array([2.5,5.5])
D=A+3/8*(B-A);E=C+8/11*(B-C)
def inter(P,Q,R,S):
    M=np.array([Q-P,R-S]).T; t=np.linalg.solve(M,R-P); return P+t[0]*(Q-P)
G=inter(A,E,C,D);Fp=inter(B,G,A,C)
assert abs(np.linalg.norm(Fp-G)/np.linalg.norm(G-B)-24/49)<1e-12
# 1743694
assert sum(1 for d in range(1,2007) if 2006%d==0)==8
# 1744693: any consistent prices give 8.00
for s in [1,1.5,2,2.3]:
    for c in [0.5,1,2]:
        b=(16.90-4*s-c)/10
        if abs(3*s+c+7*b-12.60)<1e-9: assert abs(2*s+2*c+2*b-8)<1e-9
lam,mu=-4,6; assert (4*lam+3*mu,lam+mu,10*lam+7*mu)==(2,2,2) and abs(lam*16.90+mu*12.60-8)<1e-9
# 1744133
for t in np.linspace(0,6.28,50):
    P=8*np.array([math.cos(t),math.sin(t)]); assert abs(math.hypot(P[0],P[1])-8)<1e-12
# 1743778: overlap area by grid integration
def inside(p,T):
    (x1,y1),(x2,y2),(x3,y3)=T
    def s(a,b,c): return (a[0]-c[0])*(b[1]-c[1])-(b[0]-c[0])*(a[1]-c[1])
    d1,d2,d3=s(p,T[0],T[1]),s(p,T[1],T[2]),s(p,T[2],T[0])
    return not ((min(d1,d2,d3)<0) and (max(d1,d2,d3)>0))
T1=[(-4,2),(1,2),(-1,5)];T2=[(4,2),(-1,2),(1,5)]
n=400; h=1/n*5; cnt=0
xs=np.linspace(-4,4,801); ys=np.linspace(2,5,301)
dx=xs[1]-xs[0]; dy=ys[1]-ys[0]
cnt=sum(1 for x in xs for y in ys if inside((x,y),T1) and inside((x,y),T2))
assert abs(cnt*dx*dy-1.5)<0.05
# 1743701
sols=[(I,T,E,S) for T in range(1,50) for I in range(1,2007) if 2006%(I*T*T)==0 for E in range(1,2007) if (2006//(I*T*T))%E==0 for S in [2006//(I*T*T*E)] if len({I,T,E,S})==4 and I*T*E*S*T==2006]
assert {I+T+E+S+T+2006 for I,T,E,S in sols}=={2086}
# 1743705 couples
men=['H','P','L','R']; women=['E','J','M','A']
ans=set()
for w in itertools.permutations(women):
    wife=dict(zip(men,w)); hus={v:k for k,v in wife.items()}
    dancers_m=[m for m in men if m not in ('R','P')]; dancers_w=[x for x in women if x not in ('A','M')]
    for pw in itertools.permutations(dancers_w):
        part=dict(zip(dancers_m,pw))
        if wife['H'] not in pw: continue
        if part['H']==wife['H']: continue
        if hus['E'] not in part or part[hus['E']]!=wife['H']: continue
        if hus['A']=='P': continue
        ans.add(wife['R'])
assert ans=={'A'}
# 1743710, 1743711
assert pow(2,2006,7)==4
L=list(range(110,127)); assert sum(L)==2006 and L[-2]==125
# 1741712
assert [(x,(541-9*x)//17) for x in range(1,61) if (541-9*x)%17==0 and 541-9*x>0]==[(11,26),(28,17),(45,8)]
# 1742347 necklace: Burnside value + method check by brute force on a small case
def burn(cs):
    n=sum(cs); tot=0
    def multi(c):
        r=math.factorial(sum(c))
        for k in c: r//=math.factorial(k)
        return r
    for r in range(n):
        L=n//math.gcd(r,n)
        if all(c%L==0 for c in cs): tot+=multi([c//L for c in cs])
    # reflections
    if n%2==1:
        odd=[i for i,c in enumerate(cs) if c%2]
        if len(odd)==1:
            c2=list(cs); c2[odd[0]]-=1; tot+=n*multi([c//2 for c in c2])
    else:
        if all(c%2==0 for c in cs): tot+=(n//2)*multi([c//2 for c in cs])
        odd=[i for i,c in enumerate(cs) if c%2]
        if len(odd)==2:
            c2=list(cs); c2[odd[0]]-=1; c2[odd[1]]-=1; tot+=(n//2)*2*multi([c//2 for c in c2])
        if len(odd)==0:
            # both axis beads same colour or two different even colours... general: sum over pairs
            s=0
            for i in range(len(cs)):
                for j in range(len(cs)):
                    c2=list(cs); c2[i]-=1; c2[j]-=1
                    if min(c2)>=0 and all(c%2==0 for c in c2): s+=multi([c//2 for c in c2])
            tot+=(n//2)*s
    assert tot%(2*n)==0
    return tot//(2*n)
def brute(cs):
    beads=''.join(ch*c for ch,c in zip('abcde',cs)); n=len(beads); seen=set()
    for p in set(itertools.permutations(beads)):
        s=''.join(p); vs=[]
        for r in range(n):
            t=s[r:]+s[:r]; vs+= [t,t[::-1]]
        seen.add(min(vs))
    return len(seen)
for cs in [[3,1,2,2],[3,3,2],[1,3,2,2],[2,2,2,2]]:
    assert burn(cs)==brute(cs),cs
assert burn([3,5,2,2,4])==9460080
# 1743083
oc=list(itertools.combinations(range(8),4))
assert F(sum(1 for s in oc if not any((v+1)%8 in s for v in s)),len(oc))==F(1,35)
assert [k for k in range(20) if 257<=4**k<=262145]==[5,6,7,8,9]
# cube half: count lattice points above plane through E(0,0,1),J(1,0,.5),C(1,1,0),I(0,1,.5) with A origin, B=(1,0,0), D=(0,1,0)
Ep=np.array([0,0,1.]);J=np.array([1,0,.5]);Cc=np.array([1,1,0.]);I=np.array([0,1,.5])
nrm=np.cross(J-Ep,Cc-Ep); assert abs(nrm@(I-Ep))<1e-12
g=np.linspace(0.0025,0.9975,200); X,Y,Z=np.meshgrid(g,g,g)
side=(X-Ep[0])*nrm[0]+(Y-Ep[1])*nrm[1]+(Z-Ep[2])*nrm[2]
G_=np.array([1,1,1.]); sg=np.sign((G_-Ep)@nrm)
assert abs(np.mean(np.sign(side)==sg)-0.5)<1e-2, np.mean(np.sign(side)==sg)
s2=F(108); Fp=(F(2,3),F(2,3))
assert F(5,12)*s2==45 and F(1,6)*s2==18
assert [n for n in range(100,1000) if n%5==2 and n%7==5 and n%11==7]==[117,502,887]
# 1743378 AIME
import sympy as sp
x=sp.symbols('x'); f=12-2*(x-1)*(x-5)*(x-6)
assert all(abs(f.subs(x,v))==12 for v in [1,2,3,5,6,7]) and f.subs(x,0)==72 and sp.expand(f+12+2*(x-2)*(x-3)*(x-7))==0
# 1742862
assert sum(1 for a in range(1,31) for b in range(a,31) for c in [30-a-b] if c>=b and a+b>c)==19
# 1742840: brute force colourings
cnt=set()
for col in itertools.product(range(4),repeat=9):
    if col[0]!=0: continue  # pencil 0 is blue (colour 0); others arbitrary
    if any(len(set(g))==4 for g in itertools.combinations(col,4)): continue
    from collections import Counter
    if max(Counter(col).values())>3: continue
    cnt.add(col.count(0))
assert cnt=={3}
# 1729666
p=F(2,3);q=F(1,3)
P1=sum(math.comb(4+k,k)*p**5*q**k for k in range(5)); P2=sum(math.comb(9,j)*p**j*q**(9-j) for j in range(5,10))
assert P1==P2==F(16832,19683)
# 1742842
assert [n for n in range(16,200) if (16-4)%n==(7-12)%n]==[17]
# 1742992
assert max(w*(42-2*w) for w in np.linspace(0,21,2101))==220.5
w=(21-math.sqrt(41))/2; assert abs(w*(42-2*w)-200)<1e-9 and round(w,1)==7.3
# 1743013
t=2; T=(1.5,2); U=(6,2); assert F(1,2)*F(9,2)*6==F(27,2)
# 1742873
assert 98+62+78==238
# 1742771
assert sum(1 for r in range(8) for s in itertools.combinations(range(1,8),r) if sum(s)==14)==8
# 1742540
u=np.array([3,4])/5;v=np.array([5,12])/13;wv=u+v; assert abs(wv[1]/wv[0]-7/4)<1e-12
def tang(m1,m2): return abs((m1-m2)/(1+m1*m2))
assert tang(F(7,4),F(4,3))==tang(F(7,4),F(12,5))==F(1,8)
v2=sum(100//2**i for i in range(1,8)); assert v2==97 and v2//3==32
assert sum((6-k)**3 for k in range(1,5))==224
assert sum(1 for n in range(50,100) if math.factorial(n)%(n*n)==0)==40
assert sorted(a+b for a,b in itertools.combinations([12,15,29,32],2))==[27,41,44,44,47,61]
