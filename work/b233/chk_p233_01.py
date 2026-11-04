import sys; sys.set_int_max_str_digits(100000)
import math, itertools, random
from fractions import Fraction as F
from math import comb as C
random.seed(1)
# 1722465 dinner
dishes=['V']*5+['P']*4+['S']*3+['D']*2+['I']; coke,mentos=12,9
cnt=0
for k in (4,5,6):
    for c in itertools.combinations(range(15),k):
        t=[dishes[i] for i in c]
        if t.count('V')>=1 and t.count('P')<=2 and not(coke in c and mentos in c): cnt+=1
assert cnt==6991
assert sum(C(4,p)*C(11,4-p) for p in range(3))==1320 and sum(C(4,p)*C(6,4-p) for p in range(3))==185
# 1710142: rational p only for (3,2): check ab=6 cases and random search over small a,b numerically
import sympy as sp
sols=[]
for a in range(1,60):
    for b_ in range(1,60):
        p=sp.nsimplify((sp.sqrt(2)+sp.sqrt(a))/(sp.sqrt(3)+sp.sqrt(b_)))
        if sp.simplify((sp.sqrt(2)+sp.sqrt(a))/(sp.sqrt(3)+sp.sqrt(b_))).is_rational: sols.append((a,b_))
assert sols==[(3,2)]
# 1710127
assert [d for d in range(12,20300) if 19250%d==11 and 20302%d==3]==[53]
# 1721702
assert max((F(10,k))**k for k in range(1,11))==F(625,16)
# 1722254
best=min(v-u for u in range(-400,400) for v in range(u+1,400) if -(u+v)+u*v==298); assert best==10
# 1720977
from fractions import Fraction
P=sum(Fraction(C(35,k)*C(15,3-k),C(50,3))*Fraction(30+k,53) for k in range(4)); assert P==Fraction(321,530)
# 1721820 q01 units digit (exact exponents mod 4 via pow with big exponent mod 4, check vs cycle)
s=0
for k in range(1,2019):
    e=pow(k+1,k+2)  # exact
    s+=pow(k,e,10)
assert s%10==7
# q02
N=int(''.join(str(i)+'0' for i in range(1,2018))+'2018'); assert N%36==30
# q03
e1=2019**2020; e2=2022**2023
v=(pow(2018,e1,100)+pow(2021,e2,100))%100; assert v==29 and 2+9==11
# q04
assert len([(a,b_) for a in range(26) for b_ in range(a) if (a+b_)%9==0 and (a*b_)%7==4])==2
# 1722305
assert F(8*5,15)==F(8,3)
# 1709579
assert [m for m in range(-1000,1001) if (2*m*m+7*m-9)%(m*m+m+1)==0]==[-2,-1,0,1]
# 1709572
for _ in range(1000):
    a=random.uniform(0.1,50); b_=random.uniform(0,a-0.01) if a>0.02 else 0; m=random.uniform(0.01,30)
    assert math.sqrt(a+m)-math.sqrt(a) < math.sqrt(b_+m)-math.sqrt(b_)
# 1709564: A=(0,0),B=(4,0),C=(2,2): CH=2=AB/2, angle A=45, angle B=45
assert math.isclose(math.degrees(math.atan2(2,2)),45)
# 1709557
assert sum(pow(18,k) for k in range(1,21))%10==0
# 1720902
assert len(list(itertools.product('ABC',repeat=5)))==243
# 1721937: incircle check
I=(4.5,4.5); Dp=(5,9); Cp=(45,0)
dx,dy=Cp[0]-Dp[0],Cp[1]-Dp[1]
dist=abs(dx*(Dp[1]-I[1])-dy*(Dp[0]-I[0]))/math.hypot(dx,dy); assert math.isclose(dist,4.5)
assert 9+41==5+45 and 9**2+40**2==41**2
# 1721792
for x in [i/7 for i in range(-100,100)]:
    if x==-1: continue
    assert (2/(x+1)>-1)==(x<-3 or x>-1)
# 1719666
assert sum(1 for a in range(1,11) for b_ in range(a+1,11) if a+b_>11)==20
# 1721671 b=51: build polynomial
z=complex(3,1)  # choose z,w with zw=13+i and conj sum 3+4i -> z+w=3-4i
import cmath
# solve t^2-(3-4i)t+(13+i)=0
d=cmath.sqrt((3-4j)**2-4*(13+1j)); z=((3-4j)+d)/2; w=((3-4j)-d)/2
roots=[z,w,z.conjugate(),w.conjugate()]
b2=sum(roots[i]*roots[j] for i in range(4) for j in range(i+1,4))
assert abs(b2-51)<1e-9 and all(abs(r.imag)>1e-9 for r in roots)
# 1721580
assert sum(1 for n in range(1,101) if n%2==0 or n%3==0 or n%5==0)==74 and sum(1 for n in range(1,101) if n%30==0)==3
# 1721577
for n in range(1,16): assert sum(F(1,k) for k in range(2,2**n+1))>=F(n,2)
# 1721429
for n in range(0,51): assert (n+2)**(n+1)>=2*(n+1)**(n+1)
# 1721378
S=set()
for p in itertools.permutations(range(1,10)):
    s1=p[0]+p[3]+p[4]+p[1]; s2=p[1]+p[5]+p[6]+p[2]; s3=p[2]+p[7]+p[8]+p[0]
    if s1==s2==s3: S.add(s1)
assert min(S)==17 and max(S)==23
assert 1+5+9+2==2+4+8+3==3+6+7+1==17 and 7+2+6+8==8+1+5+9==9+3+4+7==23
# 1720979
assert F(sum(1 for c in itertools.combinations(range(1,13),3) if sum(c)%3==0),220)==F(19,55)
# 1721021
for x in [i/100 for i in range(-500,500)]:
    assert ((6+6.2*x>=12-1.8*x-1e-12) and (2-x>=3.5-2*x-1e-12))==(x>=1.5-1e-12)
# 1720900
assert sum(1 for w in itertools.product('ABC',repeat=5) if max(w.count(c) for c in 'ABC')<=3)==210
# 1720901
for n in range(30): assert sum(C(n,k) for k in range(n+1))==2**n
# 1720835
Cc=(-6,0); assert math.hypot(3,4)+math.hypot(-3,4)+6==16
# 1720781 Paley 17 no mono K4; and random colourings of 18 always have one (sample)
Q={(x*x)%17 for x in range(1,17)}; assert Q=={1,2,4,8,9,13,15,16}
red=lambda x,y: (x-y)%17 in Q
for c in itertools.combinations(range(17),4):
    pr=list(itertools.combinations(c,2))
    assert not all(red(*e) for e in pr) and not all(not red(*e) for e in pr)
assert [x for x in Q if (x-1)%17 in Q]==sorted([2,9,16]) or sorted(x for x in Q if (x-1)%17 in Q)==[2,9,16]
# R(3,4)<=9 sanity: R(3,3)=6 exhaustive on 5 points pentagon colouring exists
for _ in range(200):
    col={e:random.random()<0.5 for e in itertools.combinations(range(18),2)}
    assert any(len({col[e] for e in itertools.combinations(c,2)})==1 for c in itertools.combinations(range(18),4))
print('ok')
