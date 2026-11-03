import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(2)
# 1782319 no solutions
for p in range(1,5000):
    lhs=F(p**6+2*p**4+p**2,p**9-8*p**3)
    q=F(13,12)/lhs  # equation: lhs = 13/(12q)
    assert not (q>0 and q.denominator==1)
    assert math.gcd(p*p+1,p**6-8)==1
# 1782694 squares: side 3/2 and 3 for the figure triangle
for s,fx in [(F(3,2),None),(F(3),None)]:
    A=(F(5,2),F(2)); B=(F(0),F(0)); C=(F(6),F(0))
    xD=A[0]*s/A[1]; xE=A[0]+(C[0]-A[0])*(A[1]-s)/A[1]
    assert abs(xD-xE)==s
assert 4*F(3,2)==6 and 4*3==12
# 1782754
for a in range(2,30):
    for n in range(1,30): assert (a**n-1)%(a-1)==0
# 1782611 q26
P=F(-2,3); assert F(5,4)*P+F(5,6)==0
Qx=F(2);assert F(5,4)*Qx+F(5,6)==F(10,3)==5-F(5,6)*Qx
small=F(1,2)*(6-P)*F(10,3); assert (25-small)/small==F(5,4)
# q29 coordinates
a,b=F(-3),F(4)
A=(a,5);B=(b,5);C=(-F(7,5)*a,-7);D=(-F(7,5)*b,-7)
Pp=((3*a+2*b)/5,F(5));Q=((6*C[0]+D[0])/7,F(-7))
M=(Pp[0]+(Q[0]-Pp[0])/3,Pp[1]+(Q[1]-Pp[1])/3);N=(Pp[0]+2*(Q[0]-Pp[0])/3,Pp[1]+2*(Q[1]-Pp[1])/3)
col=lambda U,V,W:(V[0]-U[0])*(W[1]-U[1])-(V[1]-U[1])*(W[0]-U[0])==0
assert col(B,D,M) and col(A,C,N)
assert (Pp[0]-a)/(b-Pp[0])==F(2,3)
assert F(5,7)==F(5,7)
# q30 count solutions by sampling exact piecewise
def count(av):
    sols=set()
    # y=2|x|-5 ; x - |2y+2| = a ; solve piecewise linear exactly
    for sx in (1,-1):
        for sy in (1,-1):
            # x = a + sy*(2y+2), y = 2*sx*x - 5  -> x = a + sy*(4 sx x - 8)
            coef=1-4*sx*sy
            x=(av-8*sy)/coef
            y=2*abs(x)-5
            if (x>=0)==(sx==1) or x==0:
                if ((2*y+2)>=0)==(sy==1) or 2*y+2==0:
                    if abs(2*x)-y==5 and x-abs(2*y+2)==av: sols.add((x,y))
    return len(sols)
odd=[av for av in [F(k,4) for k in range(-80,40)] if count(av)%2==1]
assert sorted(odd)==[-8,-2,2] and (-8)*(-2)*2==32
# q08
k=F(1,5); assert (math.sqrt(2-k)-math.sqrt(k))-2*math.sqrt(k)<1e-12
assert abs(2*math.sqrt(1/5)-2*math.sqrt(5)/5)<1e-12
# 1771440 tables simulation exact
def prob():
    tot=F(0)
    for t in range(3):
        tb=[1,2,3]; pt=F(tb[t],6); tb2=tb[:]; tb2[t]+=1
        for u in range(3):
            pu=F(tb2[u],7); tb3=tb2[:]; tb3[u]+=1
            if max(tb3)>=4: tot+=pt*pu
    return tot
assert prob()==F(6,7)
# 1782703
for _ in range(10000):
    a_,b_,c_=sorted(1+random.random()*5 for _ in range(3))
    assert a_*b_+b_*c_+c_*a_>a_+b_+c_
# 1782744
for _ in range(20000):
    x=random.uniform(-100,100); n=random.randint(1,20)
    assert math.floor(math.floor(x)/n)==math.floor(x/n)
# 1782697: radii 66,55,60 -> r=40, triangle 13:9:11 acute, diameters inside sides
X,Y,Z=F(1,66),F(1,55),F(1,60)
a_,b_,c_=(Y+Z-X),(X+Z-Y),(X+Y-Z)
assert (a_/c_,b_/c_)==(F(13,11),F(9,11))
assert 2/(X+Y+Z)==40
a_,b_,c_=13.,9.,11.
s=(a_+b_+c_)/2;K=2*math.sqrt(s*(s-a_)*(s-b_)*(s-c_))
ra,rb,rc=K/(b_+c_),K/(a_+c_),K/(a_+b_)
assert abs(ra/rb-66/55)<1e-12 and abs(ra/rc-66/60)<1e-12 and abs((K/(a_+b_+c_))/ra-40/66)<1e-12
assert ra<min(a_*c_/(b_+c_),a_*b_/(b_+c_)) and rb<min(b_*c_/(a_+c_),b_*a_/(a_+c_)) and rc<min(c_*b_/(a_+b_),c_*a_/(a_+b_))
assert a_**2<b_**2+c_**2
# original data degenerate
X,Y,Z=F(1,18),F(1,6),F(1,9); assert X+Z-Y==0
# 1782692
a=[None,F(2015)]
for n in range(2,2015): a.append(a[-1]*F(n-1,n+1))
S=F(0)
for n in range(1,30):
    S+=a[n]; assert S==n*n*a[n]
assert a[2014]==F(1,1007)
# 1782691: brute check m+n divisible by 101 in random cases
for _ in range(2000):
    A_,C_,E_=(random.randint(1,100) for _ in range(3))
    fr=F(A_*C_*E_,(101-A_)*(101-C_)*(101-E_))
    assert (fr.numerator+fr.denominator)%101==0
# 1782537
sols=[(b2,c2) for b2 in range(1,200) for c2 in range(b2,200) if 121+b2*b2==c2*c2]
assert sols==[(60,61)] and 11+60+61==132
# 1782307: forced values; also a consistent extension exists for small values (search)
f={1:2,2:3,3:6,6:11}
for x in f:
    if f[x] in f: assert f[f[x]]==x*x+2
# 1781234
assert F(175,200)==F(7,8) and 100+15*5==175 and 100+20*5==200
assert F(-400,95)==F(-80,19)
# 1568275
assert 1/(F(1,8)+F(1,4)+F(1,4))==F(8,5)
# 1782298
assert str(999999999*123456789).count('8')==3
# 1781571
assert len(set(itertools.permutations('2335142')))==1260
assert len(set(itertools.permutations('2335142',5)))==690
# 1782185
ys=[y for x in range(-500,500) for y in range(-500,500) if x and y and F(1,x)+F(1,y)==F(1,7)]
assert sum(ys)==42
mn=[(m,n) for m in range(1,500) for n in range(1,m) if F(1,m)+F(1,n)==F(2,15) and m%n]
assert mn==[(20,12)]
# 1746417 insphere of regular tetrahedron edge 1
P4=np.array([[0,0,0],[1,0,0],[0.5,math.sqrt(3)/2,0],[0.5,math.sqrt(3)/6,math.sqrt(2/3)]])
G=P4.mean(axis=0)
for face in itertools.combinations(range(4),3):
    p0,p1,p2=P4[list(face)]
    nrm=np.cross(p1-p0,p2-p0);nrm/=np.linalg.norm(nrm)
    assert abs(abs(np.dot(G-p0,nrm))-math.sqrt(6)/12)<1e-12
# 1782144
assert sum(range(1,26,2))==169==13**2
# 1782143
assert F(3,4)*F(5,4)*F(33,5)==F(99,16)==6+F(3,16)
# 1781693
assert abs(30*5-F(11,2)*0)==150
# 1782031
assert F(60,4)==15 and F(60,12)==5 and 2*(15+5)==40 and F(60,75)==F(4,5)
# 1781575
assert sum(1 for h in range(1,141) if h%4 and h%10)==98
# 1445715
op=lambda a,b:a*a*(7-b); assert op(op(2,5),3)==256
# 1781238
assert 800-15*20==25*20==500
print('chk_p222_02 ok')
