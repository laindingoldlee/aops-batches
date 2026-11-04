import math, itertools, random
from fractions import Fraction as F
import sympy as sp
random.seed(11)
C=math.comb
# 1715264 q01
assert (2+F(6,10)*5, 3+F(6,10)*(-10))==(5,-3)
# 1715264 q02
cubes=[n**3 for n in range(1,30)]
ps={a-b for a in cubes for b in cubes if 0<a-b<200 and sp.isprime(a-b)}
assert sorted(ps)==[7,19,37,61,127]
# 1715264 q03
a,b_,c,d=sp.symbols('a b c d')
assert len(sp.Poly(sp.expand((a+b_+c+d)**6),a,b_,c,d).terms())==84
# 1715061
s3=sp.sqrt(3)
B=sp.Matrix([0,0]);Cc=sp.Matrix([7,0]);D=Cc+3*sp.Matrix([-sp.Rational(1,2),s3/2]);A=3*s3*sp.Matrix([s3/2,sp.Rational(1,2)])
M=(B+Cc)/2;N=(A+D)/2;E=(A+B)/2;Fp=(Cc+D)/2
assert sp.simplify(A[1]-D[1])==0 and sp.simplify((M-N).norm()-3)==0 and sp.simplify((E-Fp).norm()-4)==0
# angles 30 at B, 60 at C
assert sp.simplify(A[1]/A[0]-1/s3)==0
# 1714787
assert 55*56==3080 and (-56)*(-55)==3080
# 1715130 / 1713859
a_=[None,-1]
for n in range(2,2019): a_.append(a_[-1]+n)
assert a_[2:5]==[1,4,8] and a_[2018]-a_[1]==2037170
# 1715046
w=sp.sqrt(1+sp.sqrt(-3+2*s3))-sp.sqrt(1-sp.sqrt(-3+2*s3))
assert abs(sp.N(w-(s3-1),50))<1e-40
# 1715043
assert F(100,F(112,100))==F(2500,28) and F(2500,28)==89+F(2,7)
# 1715049
for _ in range(2000):
    p,q=random.uniform(1,9),random.uniform(1,9)
    Cq=(0,0);Aq=(0,p);Bq=(q,0);Dq=(q/2,p/2)
    e=random.uniform(0.01,0.99)*p; Eq=(0,e)
    v=(Eq[0]-Dq[0],Eq[1]-Dq[1]); wv=(v[1],-v[0])
    if abs(wv[1])<1e-9: continue
    s=-Dq[1]/wv[1]; Fq=(Dq[0]+s*wv[0],0)
    if not 0<=Fq[0]<=q: continue
    assert math.isclose(math.dist(Eq,Fq)**2, (p-e)**2+(q-Fq[0])**2, rel_tol=1e-9)
# 1715033
x=F(105)/(F(5,4)+1+F(3,2)); assert x==28
assert F(105)/(F(5,4)+F(3,2)-1)==60
# 1715057
for _ in range(1000):
    c_=random.uniform(-5,5);b2=c_+random.uniform(0.01,5);a2=b2+random.uniform(0.01,5)
    assert 1/(a2-b2)+1/(b2-c_)>2/(a2-c_)
# 1715070
assert [n for n in range(1,100) if n*(n+1)**2//2==605 and n*(n+1)**2%2==0]==[10]
assert sum(k*k for k in range(1,11))==385 and sum(k*(k+1)//2 for k in range(1,11))==220
# 1715059
def dp(n): return math.prod(int(t) for t in str(n))
assert [n for n in range(8,10**5,8) if sum(map(int,str(n)))==7 and dp(n)==6]==[16,1312,3112]
# 1715027
assert [(a3,b3) for a3 in range(1,10) for b3 in range(10) if int(f'{a3}783{b3}')%56==0]==[(2,2),(9,2)]
# 1715038
sols=[k for k in range(1,51) for S_ in itertools.combinations(range(1,51),k) if False]
ok=[]
for m in range(0,51):
    if (101+m)%4: continue
    T=(101+m)//4
    if m*(m+1)//2<=T<=sum(range(51-m,51)) and m>0: ok.append(m)
assert ok==[3] and sum(4*k-1 for k in (1,2,23))==101 and 5050-101==4949
# 1714156
assert sum(range(2,101,2))==2550
# 1714863
assert len(set(itertools.permutations('ANGELA')))==360
# 1714665
assert math.factorial(8)//4==10080
# 1570243
for n in range(2,41):
    L=C(n,2); assert C(L,2)-n*C(n-1,2)==3*C(n,4)==n*(n-1)*(n-2)*(n-3)//8
for n in [4,5,6]:
    pts=[(random.random(),random.random()) for _ in range(n)]
    lines=list(itertools.combinations(range(n),2))
    def inter(l1,l2):
        (x1,y1),(x2,y2)=pts[l1[0]],pts[l1[1]];(x3,y3),(x4,y4)=pts[l2[0]],pts[l2[1]]
        den=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        t=((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/den
        return (round(x1+t*(x2-x1),9),round(y1+t*(y2-y1),9))
    P=set(inter(l1,l2) for l1,l2 in itertools.combinations(lines,2) if not set(l1)&set(l2))
    assert len(P)==3*C(n,4)
# 1711485
assert abs(18+12*math.pi-55.699)<0.01
# 1714155
assert 10-3==F(14,2) and 14==10+4
# 1713999
A9=sp.Matrix([0,0]);Dd=sp.Matrix([5,0]);C9=sp.Matrix([4,0]);B9=sp.Matrix([4,3]);E9=sp.Matrix([sp.Rational(9,5),-sp.Rational(12,5)])
assert (E9).norm()==3 and (E9-Dd).norm()==4
area_small=sp.Rational(1,2)*abs(2*0-sp.Rational(3,2)*sp.Rational(5,2))
assert area_small/(6-area_small)==sp.Rational(5,11)
# 1712630
q=2*sp.sqrt(3306)/5
A0=sp.Matrix([0,0]);C0=sp.Matrix([10,0]);B0=sp.Matrix([sp.Rational(1,5),q])
assert sp.simplify(B0.dot(B0))==529 and sp.simplify((B0-C0).dot(B0-C0))==625
D0=(B0+C0)/2;E0=sp.Matrix([B0[0],0]);F0=sp.Rational(2,7)*B0
assert sp.simplify((F0-A0).norm()/(B0-F0).norm()-sp.Rational(2,5))==0
ar=sp.Abs((D0-E0)[0]*(F0-E0)[1]-(D0-E0)[1]*(F0-E0)[0])/2
assert sp.simplify(ar-103*sp.sqrt(3306)/350)==0
r=sp.sqrt(1653)
for ch in [3125*r/8057,25*r/49,343*r/625,7*sp.sqrt(551)/5,2147*sp.sqrt(3306)/3500]:
    assert abs(float(ch-ar))>0.5
# 1712753
A1=sp.Matrix([4,sp.sqrt(105)]);K=sp.Matrix([4,sp.sqrt(105)/4])
assert sp.simplify((A1-K).norm()/K.norm())==3
# 1714043
assert 32-2==30
# 1713813
assert all(x*x+1>=1 for x in [-3,-0.5,0,0.5,2])
print('chk_p234_02 ok')
