import math, itertools, random
from fractions import Fraction as F
import numpy as np
import sympy as sp
random.seed(3)
r2,r3,r6=math.sqrt(2),math.sqrt(3),math.sqrt(6)
# 1734443 q01
a,b=12,8; assert b*b+a*a/4==100 and a*a+b*b/4==160 and a*a+b*b==208 and abs(math.sqrt(208)-4*math.sqrt(13))<1e-12
# q02
xs=[x for x in range(2,200) if sorted([5*x,4*x+13,x-1])[0]**2+sorted([5*x,4*x+13,x-1])[1]**2==sorted([5*x,4*x+13,x-1])[2]**2]
assert xs==[12] and 1+2==3
# q03
A=(4,3); assert 4**2+3**2==25 and 12**2+3**2==153
vals={math.hypot(4-t,3) for t in np.linspace(0,16,160001)}
ints=[k for k in range(1,20) if min(vals)<=k<=max(vals)]; assert ints==list(range(3,13)) and sum(ints)==75
# q04
B=np.array([0,0]);A=np.array([r6,0]);C=np.array([0,r2]);D=np.array([r2,r2+r6])
assert abs(np.linalg.norm(A-C)-2*r2)<1e-12 and abs(np.dot(D-C,A-C))<1e-12 and abs(np.linalg.norm(D-C)-2*r2)<1e-12
assert abs(D[1]-(r6+r2))<1e-12 and abs(4*math.sin(math.radians(75))-(r6+r2))<1e-12
# q05
assert abs(math.sqrt(26**2-8**2)-6*math.sqrt(17))<1e-12 and abs(math.sqrt(26**2-18**2)-4*math.sqrt(22))<1e-12
O=np.array([0,0]);Ac=np.array([26,0]);n1=np.array([-8/26,math.sqrt(612)/26]);n2=np.array([18/26,-math.sqrt(352)/26])
T1,T2=O+5*n1,Ac+13*n1; assert abs(np.dot(T2-T1,n1))<1e-12
U1,U2=O+5*n2,Ac-13*n2; assert abs(np.dot(U2-U1,n2))<1e-12
# q06
assert 80**2+18**2==82**2 and F(6400,82)-41==F(1519,41)
# q07
assert 49+64-2*7*8*F(1,2)==57
# q08
SA=12*5*0.5*10*(5/math.tan(math.radians(36)))
assert abs(SA-300*math.sqrt(25+10*math.sqrt(5)))<1e-9 and abs(math.tan(math.radians(36))-math.sqrt(5-2*math.sqrt(5)))<1e-12
# q09
assert 441+100-505==36 and 18**2+6**2==360
# q10
s=3*r2; assert abs(s*math.sqrt(2/3)-2*r3)<1e-12 and abs(s**3/(6*r2)-9)<1e-9
# q11
assert abs(8*0.5*math.sin(math.pi/4)-2*r2)<1e-12 and abs(6*0.5*math.sin(math.pi/3)-1.5*r3)<1e-12 and abs(2*r2-1.5*r3-0.230)<1e-3
# q12: overlap of folded rectangle (polygon intersection by sampling)
Bp=np.array([16,0])-2*((3*16-0)/25)*np.array([3,-4]); assert np.allclose(Bp,[4.48,15.36])
t=sp.symbols('t'); assert sp.solve((16-t)**2+144-t**2,t)==[sp.Rational(25,2)] and F(1,2)*F(25,2)*12==75
cnt=0;N=200000
for _ in range(N):
    x,y=random.uniform(0,16),random.uniform(0,12)
    if 3*x-4*y<0:  # upper triangle; reflected point inside lower triangle region of the flap?
        # point is covered by the flap if its reflection lies in the lower triangle (y<3x/4 inside rectangle)
        q=np.array([x,y])-2*((3*x-4*y)/25)*np.array([3,-4])
        if 0<=q[0]<=16 and 0<=q[1]<=12: cnt+=1
assert abs(cnt/N*192-75)<1.5
# q13
tot=math.comb(7,3)*math.comb(14,3)*math.comb(13,3)*math.comb(9,2); assert tot==131171040 and tot%100==40
# q14 (Pappus) numeric check by integration for R=3,r=1
R_,r_=3,1; V=sum(2*math.pi*(R_+r_*math.cos(th))*r_*r_*math.sin(th)**2 for th in np.linspace(0,2*math.pi,20001)[:-1])*(2*math.pi/20000)
assert abs(V-2*math.pi**2*R_*r_**2)<1e-6
# q15
assert abs(math.hypot(10,15)-5*math.sqrt(13))<1e-12
best=min(math.hypot(x,5)+math.hypot(10-x,10) for x in np.linspace(0,10,100001)); assert abs(best-5*math.sqrt(13))<1e-6
# q16
assert 21**2+32**2-26**2==789 and 297+144==441 and 532+144==676 and 532+492==1024 and 297+492==789
# 1729571
assert sum(range(376,425,2))==10000 and len(range(376,425,2))==25
# 1734824
assert abs(sum(0.5**k for k in range(1,60))-1)<1e-12
# 1735477
assert [n for n in range(1,30) if n>5 and n%2==0 and n<=8]==[6,8]
# 1735595
assert abs(math.hypot(8,22)-2*math.sqrt(137))<1e-12
best=min(math.hypot(t+1,t-4)+math.hypot(12-t,21-t) for t in np.linspace(-5,20,250001)); assert abs(best-2*math.sqrt(137))<1e-6
assert len(set(itertools.permutations('TINCAN')))==360 and 360*5==1800
k=sp.symbols('k'); ks=sp.solve(9-8*k**2,k); assert sum(ks)==0
assert F(1,72)+F(1,120)==F(1,45)
# 1732120
for a_ in [0,1,2,-1.5,3.7]:
    assert abs(math.sqrt(1+a_**2+math.sqrt(1+a_**2+a_**4))-(math.sqrt(2*a_*a_+2*a_+2)+math.sqrt(2*a_*a_-2*a_+2))/2)<1e-12
# 1724280
x=sp.symbols('x'); assert sp.expand((x-1)*(x-2)*(x+3))==x**3-7*x+6
# 1735442
assert sum(len(str(i)) for i in range(1,201))==492 and sum(len(str(i)) for i in range(1,13))==15
# 1734263
assert 63*49*36*28==1764**2 and 25**2+60**2==65**2 and 39**2+52**2==65**2 and 750+1014==1764
V2=np.array([-32.5,0]);V4=np.array([32.5,0]);V1=V2+25*np.array([5/13,12/13]);V3=V2+39*np.array([3/5,-4/5])
for P in (V1,V3): assert abs(np.linalg.norm(P)-32.5)<1e-9
assert abs(np.linalg.norm(V3-V4)-52)<1e-9 and abs(np.linalg.norm(V1-V4)-60)<1e-9
# 1735427
assert len([n for n in range(100,1000) if str(n)==str(n)[::-1] and sum(map(int,str(n)))==9])==4
# 1735205
def sg(n): return sum(math.gcd(n+i,n+j) for i in range(10) for j in range(i+1,10))
v=[sg(n) for n in range(1,2521)]; assert max(v)==95 and min(v)==67 and sg(504)==95 and sg(2)==67
# 1732115 exact integration
Bv,Mv,Lv=sp.symbols('B M L',real=True)
inner=sp.integrate(1,(Mv,sp.Max(Bv,15),sp.Min(Bv+Lv,75)))
# direct: P(0<M-B<L) for fixed L by integrating over B in [0,60]: M in (max(B,15), B+L) when B+L>15
PL=sp.Piecewise((0,True))
def prob(L):
    tot=0
    # piecewise in B: for B<=15-L nothing; 15-L<B<15: length B+L-15; 15<=B<=60: length L (B+L<=75 since B<=60, L<=15)
    tot=sp.integrate(Bv+L-15,(Bv,15-L,15))+sp.integrate(L,(Bv,15,60))
    return tot/3600
PLs=sp.simplify(prob(Lv)); assert sp.simplify(PLs-(45*Lv+Lv**2/2)/3600)==0
P=sp.integrate(PLs,(Lv,5,15))/10; assert P==sp.Rational(121,864) and P/2==sp.Rational(121,1728)
c=0;N=200000
for _ in range(N):
    b_=random.uniform(0,60); m_=random.uniform(15,75); l_=random.uniform(5,15)
    c+=(b_<m_<b_+l_)
assert abs(c/N-121/864)<0.004
# 1735058
assert 70*300/60==350
# 1734599
assert F(3*6,8)==F(9,4)
u=np.array([math.cos(math.radians(115)),math.sin(math.radians(115))]);Cc=8*u;Ee=-(9/4)*u
kk=(Cc[0]**2+Cc[1]**2-3*Cc[0]-18)/(2*Cc[1]);P=np.array([1.5,kk]);R=np.linalg.norm(np.array([-3,0])-P)
for Q in (np.array([6,0]),Cc,Ee): assert abs(np.linalg.norm(Q-P)-R)<1e-9
# 1734465
for a_,b_,c_ in [(1,-4,0),(-3,4,16)]:
    assert sp.expand((x-2)*(x-a_-1)*(x-a_+1))==sp.expand(x**3+b_*x**2-b_*x-c_)
# 1734740
best=0
g=np.linspace(-1,1,21)
for x1,y1,x2,y2 in itertools.product(g,g,g,g):
    if (x1,y1)!=(x2,y2): best=max(best,(x1-x2)**2+(y1-y2)**2+(y1+y2)**2)
assert abs(best-8)<1e-9 and math.floor(math.sqrt(8))==2
# 1734735
assert max(((l*g_+l+g_)//(l*l+g_*g_)) for a_ in range(1,101) for b_ in range(1,101) if a_!=b_ for g_ in [math.gcd(a_,b_)] for l in [a_*b_//g_])==1
# 1734605
dirs=[0,75,120,195,240,315];V=[np.array([0.,0.])]
for d_ in dirs: V.append(V[-1]+2*np.array([math.cos(math.radians(d_)),math.sin(math.radians(d_))]))
assert np.allclose(V[6],V[0]); V=V[:6]
ar=abs(sum(V[i][0]*V[(i+1)%6][1]-V[(i+1)%6][0]*V[i][1] for i in range(6)))/2
assert abs(ar-(2*r3+3*r2+r6))<1e-9
def ang(P,Q,Rr):
    u1=P-Q;u2=Rr-Q; return math.degrees(math.acos(np.dot(u1,u2)/np.linalg.norm(u1)/np.linalg.norm(u2)))
angs=[ang(V[i-1],V[i],V[(i+1)%6]) for i in range(6)]; assert np.allclose(angs,[135,105,135,105,135,105])
# 1734670
assert sum(range(1,26))==325 and pow(325,2018,10)==5
print('chk_p230_03 ok')
