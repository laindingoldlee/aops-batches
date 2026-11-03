import math, itertools, random
from fractions import Fraction as F
random.seed(1)
# 1779396
assert abs(math.log(9,2)*math.log(7,3)*math.log(8,7)-6)<1e-12
# 1780033 rectangle and triangles
assert F(5,12)==F(10,24) and 13==12+F(5,5)*1 and 5**2+12**2==13**2 and 12+5-F(4,5)*5==13
assert sum(1 for a,b,c in itertools.combinations(range(1,9),3) if a+b>c)==22
# 1779918
assert sum(1 for w in itertools.product('ABC',repeat=5) if 'A' in w and 'B' in w)==180
# 1779794
r=(-2-math.sqrt(6))/3; assert abs(9*r*r+12*r-2)<1e-12
assert all(abs(2*x*x-12*x+16)<1e-12 for x in (2,4))
def pi_(x): return sum(1 for p in range(2,x+1) if all(p%d for d in range(2,p)))
assert sum(x for x in range(1,200) if (pi_(x)+1)**2-2*(pi_(x)+4)-9==0)==34
assert 20*(1-F(50,100))**2==5
# 1779655
assert int('213',6)==81 and int('1101',4)==81
# 1779563
n=2019; A=math.pi**2/n/math.tan(math.pi/n); assert round(A)==3 and 0.99*math.pi<A<math.pi
# 1779468
H=lambda k: sum(F(1,j) for j in range(1,k+1))
assert [H(k) for k in range(1,5)]==[1,F(3,2),F(11,6),F(25,12)] and H(5)==2+F(17,60) and H(6)==2+F(9,20)
best=max(F(a,b)-c*d for a,b,c,d in itertools.permutations(range(-5,5),4) if b!=0); assert best==24
m=100; day=1
while m>0:
    day+=1; k=day//2
    m+= k if day%2==0 else -(k+1)
assert day==201
assert F(25,36)*(-1)+F(10,36)*2+F(1,36)*5==0
# 1779434
assert F(sum(1 for t in itertools.product(range(1,7),repeat=3) if (lambda s: s[2]-s[1]==s[1]-s[0])(sorted(t))),216)==F(7,36)
# 1779285 configuration: angle BOC=76 gives angle ABO=24, OBC=OCD=52, AB||CD
d=lambda a: (math.cos(math.radians(a)),math.sin(math.radians(a)))
def ang(P,Q,R):
    u=(P[0]-Q[0],P[1]-Q[1]); v=(R[0]-Q[0],R[1]-Q[1])
    return math.degrees(math.acos((u[0]*v[0]+u[1]*v[1])/math.hypot(*u)/math.hypot(*v)))
O=(0,0);A_=d(260);B_=d(128);C_=d(52);D_=d(-24)
assert abs(ang(A_,B_,O)-24)<1e-9 and abs(ang(O,B_,C_)-52)<1e-9 and abs(ang(O,C_,D_)-52)<1e-9 and abs(ang(B_,O,C_)-76)<1e-9
u=(B_[0]-A_[0],B_[1]-A_[1]); v=(C_[0]-D_[0],C_[1]-D_[1]); assert abs(u[0]*v[1]-u[1]*v[0])<1e-12
# 1778686
x=(5+math.sqrt(21))/2; assert abs(x**4+x**-4-527)<1e-6
# 1779038
arm=[n for n in range(100,1000) if sum(int(c)**3 for c in str(n))==n]; assert arm==[153,370,371,407] and sum(arm)==1301
# 1778933
w=[1,1,2]
for i in range(3,7): w.append(w[-1]+w[-2]+w[-3])
assert w[6]==24
# 1779041
for _ in range(20000):
    v=[random.gauss(0,1) for _ in range(3)]; s=math.sqrt(sum(t*t for t in v)); a,b,c=[t/s for t in v]
    q=a*b+b*c+c*a; assert -0.5-1e-12<=q<=1+1e-12
best=max(2*abs(1+2*math.sin(t)) for t in [k*0.001 for k in range(6284)]); assert abs(best-6)<1e-6
# 1779111
assert math.comb(9,2)==36 and math.comb(6,2)==15
assert sum(1 for a in range(8) for b in range(a,8) for c in range(b,8) if a+b+c==7)==8
# 1778662
def mc(n): return min(q+d+k+(n-25*q-10*d-5*k) for q in range(n//25+1) for d in range((n-25*q)//10+1) for k in range((n-25*q-10*d)//5+1))
assert all(mc(n)<=7 for n in range(1,69)) and mc(69)==8
assert all(mc(n)==n//25+(n%25)//10+(n%25%10)//5+n%5 for n in range(1,200))
# 1778586
x,y=1.2,1.6; w_=x+math.sqrt(9-y*y); h=y+math.sqrt(100-(w_-x)**2)
assert abs(math.hypot(x,y)-2)<1e-12 and abs(math.hypot(w_-x,y)-3)<1e-12 and abs(math.hypot(w_-x,h-y)-10)<1e-12
assert abs(math.hypot(x,h-y)-math.sqrt(95))<1e-9
assert abs(sum((math.pi-2)*0.5**k for k in range(200))-(2*math.pi-4))<1e-12
assert max(F(a,10*b+a)+F(b,10*a+b) for a in range(2,17) for b in range(2,17))==F(37,81)
# 1778486
assert abs((36/math.sqrt(2))**2/36**2-0.5)<1e-12 and abs(36/math.sqrt(2)-18*math.sqrt(2))<1e-12
# 1773289
assert 99**100>100**99 and all((1+F(1,n))**n<3 for n in range(1,60))
# 1774814
def df(k):
    r=1
    while k>1: r*=k; k-=2
    return r
def formula(m): return sum((-1)**k*math.comb(m,k)*df(2*m-2*k-1) for k in range(m+1))
def matchings(people):
    if not people: yield []; return
    a=people[0]
    for i in range(1,len(people)):
        for rest in matchings(people[1:i]+people[i+1:]): yield [(a,people[i])]+rest
for m in range(1,6):
    old={(2*i,2*i+1) for i in range(m)}
    assert sum(1 for M in matchings(list(range(2*m))) if not (set(M)&old))==formula(m)
assert formula(12)==187778717632
# 1777751
def P(x,y,z): return x/(x+y*z)+y/(y+x*z)+math.sqrt(x*y*z)/(z+x*y)
mx=1+3*math.sqrt(3)/4; xs=2*math.sqrt(3)-3; zs=7-4*math.sqrt(3)
assert abs(2*xs+zs-1)<1e-12 and abs(P(xs,xs,zs)-mx)<1e-12
N=300
for i in range(1,N):
    for j in range(1,N-i):
        x=i/N;y=j/N;z=1-x-y
        assert P(x,y,z)<=mx+1e-12
# 1777839
def ok(a2):
    a,b=999,a2
    for n in range(2,2006): a,b=b,abs(b-a)
    return b==1
assert sum(1 for a2 in range(999) if ok(a2))==324
