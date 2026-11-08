import math, itertools, random
from fractions import Fraction as F
import sympy as sp
random.seed(2)
# 1731770 q01: construction valid and k>=5
S=[{5,10}|{n for n in range(1,50) if n%10 in (1,2,3,4)},{15,20}|{n for n in range(1,50) if n%10 in (6,7,8,9)},{25,30},{35,40},{45}]
assert set().union(*S)==set(range(1,50)) and sum(map(len,S))==49
assert all((a+b)%10 for s in S for a,b in itertools.combinations(s,2))
assert all((a+b)%10==0 for a,b in itertools.combinations([5,15,25,35,45],2))
# q02
N=200000; assert abs(sum(random.random()+random.random()+random.random()<=1 for _ in range(N))/N-1/6)<0.01
# 1732639
for m in range(1,40):
    for n in range(m+1,40):
        v=(n*(n+1)*(n+2)-m*(m+1)*(m+2))//(n-m)+m*n
        assert (n*(n+1)*(n+2)-m*(m+1)*(m+2))%(n-m)==0 and v==(m+n+1)*(m+n+2)
# 1732287
cnt=0
for col in itertools.product(range(3),repeat=8):
    k=[col.count(i) for i in range(3)]
    if min(k)>0 and len(set(k))==3: cnt+=1
assert cnt==2688
# 1147571
assert sum(1 for a in range(1,17) for b in range(1,17) for c in range(1,17) if 17-a-b-c>=1)==560==math.comb(16,3)
# 1732169
assert all(p%6 in (1,5) for p in sp.primerange(5,10**5))
# 1731721
vow='AOU'; con='MTHCNTS'
assert len({(tuple(sorted(v)),tuple(sorted(c))) for v in itertools.combinations(vow,2) for c in itertools.combinations(con,3)})==75
# 1731866
n=sp.symbols('n'); assert sp.expand(3*(n-5)-(3*n-5))==-10
# 1731843
assert len({sum(c) for c in itertools.combinations(range(1,15),7) if 2*sum(c)<105})==25
best=min(c for a in range(0,101) for b in range(a,101) for c in range(b,101) for d in range(c,101) if 0<=204-a-b-c-d<=100 and 204-a-b-c-d>=d)
assert best==2
x=F(20,3); assert F(8,10)*x+F(2,10)*(10-x)==6
# 1731473
n=1
while {d%10 for d in sp.divisors(n)}!=set(range(10)): n+=1
assert n==270
# 336615
assert max(a+2*b+c for a,b,c in itertools.permutations(range(1,10),3))-min(a+2*b+c for a,b,c in itertools.permutations(range(1,10),3))==26
# 1731478, 1731491
assert pow(2,2000,13)==9 and pow(11,2014,1000)==241 and math.comb(2014,2)==2027091
# 1731288
assert len(set(itertools.combinations_with_replacement(range(5),2)))==15
# MTE
x=sp.symbols('x')
r=sp.solve(x**2+6*x+8,x); assert sum(F(4,int(t)) for t in r)==-3
assert sum(F(3-2*k,4*k*k+8*k+3) for k in range(1,4))==F(-1,105)
assert all(sp.simplify((3-2*x)/(4*x**2+8*x+3)-(2/(2*x+1)-3/(2*x+3)))==0 for _ in [0])
sol=[t for t in range(-50,51) if (t-1)**2==t**3-12*t**2+42*t-31 and (t-2)**2==t**3-11*t**2+32*t-28]
assert sol==[8]
assert sp.Poly(sp.expand((264*x**3+792*x**2+528*x)/(math.factorial(4)*math.factorial(6)//720)),x).coeffs()==[11,33,22]
f=4*x**3-48*x**2+189*x-243
assert sp.factor(f)==(x-3)*(2*x-9)**2 and sp.Rational(3)+sp.Rational(9,2)==sp.Rational(15,2)
assert sp.solve(sp.diff(f,x),x)==[sp.Rational(7,2),sp.Rational(9,2)]
xx=sp.symbols('xx')
area2=xx*(3*xx-5*xx)+18*(5*xx-2)+6*(2-3*xx)
assert sp.expand(area2/2)==-xx**2+36*xx-12 and (-1+36-12)==23
c=0
for t in itertools.product([-1,0,1],repeat=3):
    if 0<=-sum(t)<=1 and 0<=-t[0]*t[1]*t[2]<=1: c+=1
assert F(c,27)==F(10,27)
P=x**3+2*x**2+4*x+8
rt=sp.Poly(P).nroots(); assert abs(sum(1/z for z in rt)+0.5)<1e-9
y=(18+math.sqrt(320))/2; assert abs(y*y-18*y+1)<1e-9
s=18
for _ in range(11): s=s*s-2
assert s%10==2
assert len(sp.divisors(108))==12 and all(2*(u)*(108//u)==216 for u in sp.divisors(108))
rt=sp.Poly(x**3+20*x**2+18*x-2018).nroots()
assert sum(1 for z in rt if abs(sp.im(z))<1e-9 and sp.re(z)>0)==1 and F(2018,36)==F(1009,18)
best=None
for cc in range(3,60):
    for a in range(1,cc):
        for b in range(a+1,cc):
            if a+b>cc and not (b==a+1 and cc==b+1):
                k=-(a+b-2*cc)**2
                best=k if best is None or k>best else best
assert best==-16
# sum of roots of P^n: coefficient check for small n
def iterate(n):
    g=x
    for _ in range(n): g=sp.expand((g-3)*(g-9))
    return g
for n in range(1,5):
    pl=sp.Poly(iterate(n),x); cs=pl.all_coeffs(); assert -cs[1]/cs[0]==12*2**(n-1)
assert 12*2**9==6144
f14=2*x**5+x**4-26*x**3-13*x**2+72*x+36
assert sp.factor(f14)==(2*x+1)*(x-2)*(x+2)*(x-3)*(x+3)
g=sp.Poly(sp.expand(f14.subs(x,x+4)),x).all_coeffs(); assert sp.Rational(-g[1],g[0])==sp.Rational(-41,2)
rt=sp.Poly(2*x**3+10*x+8).nroots(); r_,s_,t_=rt
assert abs(complex(r_**2+r_*s_+r_*t_+s_**2+s_*t_+t_**2)+5)<1e-9
# 1731212
assert abs(math.sqrt(10)*0.5-math.sqrt(6)*0.5-math.sqrt(4-math.sqrt(15)))<1e-12 and F(1,2)-F(1,2)-F(1,4)==F(-1,4)
# 1730716
for X in range(23,5000):
    v=math.sqrt(X+math.sqrt(2011)/2)-math.sqrt(X-math.sqrt(2011)/2)
    if abs(v-round(v))<1e-9: assert X==503
assert abs(math.sqrt(503+math.sqrt(2011)/2)-math.sqrt(503-math.sqrt(2011)/2)-1)<1e-9
# 1111533
e=1-1/(1-1/(1-1/(x-1)))
assert sp.simplify(e-(x-1))==0
# 1730856
for N in range(1,100000):
    d=[int(c) for c in str(N)[::-1]]
    assert (N%11==0)==((sum(d[0::2])-sum(d[1::2]))%11==0)
# 1730732
sols=[(S_,A,Y,B) for S_,A,Y,B in itertools.product(range(10),repeat=4) if len({S_,A,Y,B})==4 and S_>0 and B>0 and (100*S_+10*A+Y)*3==1010*B+100*A+Y]
assert sols==[(5,7,0,1)]
print('ok')
