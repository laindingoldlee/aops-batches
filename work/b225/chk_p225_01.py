import math, itertools
from fractions import Fraction as F
# 1763997 product of digits
pd=lambda n: math.prod(int(c) for c in str(n))
assert [pd(36),pd(325),pd(45),pd(30)]==[18,30,20,0] and pd(531)==15
# 1766350
a=[1]
for k in range(1,10): a.append(a[-1]+4**k)
assert all(a[n-1]==(4**n-1)//3 for n in range(1,11)) and a[7]==21845
# 1766101
sq=[d for d in range(1,18001) if 18000%d==0 and math.isqrt(d)**2==d]
assert len(sq)==12 and set(sq)=={1,4,16,25,9,36,225,100,400,144,900,3600}
# 1766239
assert abs(complex(5,-12))==13
# 1763568 q01
n=1
while not (n**3%10!=0 and len(set(str(n**3)[-3:]))==1 and n**3>=100): n+=1
assert n==192 and n**3%1000==888 and 471**3%1000==111
assert [min(m for m in range(1,1001) if m**3%1000==111*d) for d in (1,3,7,9)]==[471,477,753,999]
# q02
num=math.prod(math.factorial(i) for i in range(1,101)); den=math.prod(math.factorial(i)**2 for i in range(1,100,2))
q=num//den; assert num%den==0 and q==2**50*math.factorial(50)
k=0
while q%2==0: q//=2; k+=1
assert k==97
# 1765675 heronian
best=min((math.isqrt((a+b+17)*(a+b-17)*(17-a+b)*(17+a-b))//4,a,b) for a in range(1,18) for b in range(a,18) if a+b>17 and (lambda s:math.isqrt(s)**2==s and math.isqrt(s)%4==0)((a+b+17)*(a+b-17)*(17-a+b)*(17+a-b)))
assert best==(36,9,10)
# 1766133
S=sum(F(5832)*F(1,3)**k for k in range(24)); assert S==8748-F(4,3**17)
# 1765448: no solutions small, and parity argument 2018 % 4 == 2
assert 2018%4==2
for x in range(1,4):
    v=2019**(2*x)-2018; assert math.isqrt(v)**2!=v
# 1765863
import numpy as np
xs=np.linspace(-6,1,700001); f=(xs+1)*(xs+2)*(xs+3)*(xs+4)
assert abs(f.min()+1)<1e-9
r=(-5+5**0.5)/2; assert abs((r+1)*(r+2)*(r+3)*(r+4)+1)<1e-12
# 1765846
assert 5**0+5**2==26 and 5**2+5**0==26 and 10*math.e>26
# 1754151
for n in range(2,60):
    Si=1+2**n; Sp=sum(2**j for j in range(1,n)); assert (Si%3==0)==(Sp%3==0)==(n%2==1)
# 1765446
assert [2018000+a for a in range(1000) if (2018000+a)%321==0]==[2018127,2018448,2018769]
# 1765724 Fibonacci: no triple of distinct values forms a triangle
fib=[1,1]
while len(fib)<40: fib.append(fib[-1]+fib[-2])
vals=sorted(set(fib))
for a,b,c in itertools.combinations(vals,3): assert a+b<=c
# 1765713
tot=sum(math.comb(5,p)*math.comb(4,n)*math.comb(3,d) for p in range(6) for n in range(5) for d in range(4) if p+5*n+10*d==30)
assert F(tot,2**12)==F(23,2048) and tot==46
# 1765813
assert all((n*n+5*n+1)%49 for n in range(49))
# 1765742
assert 13**4==28561 and 13*12*11*10==17160
# 1765746
assert 8**2+2==7*9+3==66
# 1765635
L=[2,3,5,8,13]; assert sum(1 for a,b,c in itertools.combinations(L,3) if a+b>c)==0
# 1763348
I=[1,1j,-1,-1j]
assert I[17%4]==1j and I[69%4]==1j and I[1972%4]==1
# 1765571
combos=[(q,d,n) for q in range(2) for d in range(5) for n in range(10) if 25*q+10*d+5*n==45]
assert len(combos)==8 and sum(1 for c in combos if c[1]>=3)==2
# 1765455
for k in range(0,200):
    s=sum(range(25*k+1,25*k+25)); assert s%100==0 and (s//100)%10%2==1
# 1765502 sign pyramid
cnt=0
for row in itertools.product([1,-1],repeat=4):
    r=list(row)
    while len(r)>1: r=[r[i]*r[i+1] for i in range(len(r)-1)]
    cnt+=r[0]==1
assert cnt==8
# 1764786
can=lambda n:any((n-7*a)%3==0 for a in range(n//7+1))
assert not can(11) and all(can(n) for n in range(12,200))
# 1764009
cr=lambda u,v:u[0]*v[1]-u[1]*v[0]
D=np.array([0,0]);G=np.array([4,3]);A=np.array([0,4]);nv=np.array([-3,4])/5
E=D+3.2*nv;Fp=G+3.2*nv
assert abs(cr(Fp-E,A-E))<1e-12 and 0<np.dot(A-E,Fp-E)<np.dot(Fp-E,Fp-E)
assert abs(abs(cr(G-D,A-D))/5-3.2)<1e-12
# 1764818
assert 3000*3001//2*5==22507500
# 1765152
best=0
for x in np.linspace(0.05,3.95,400):
    for y in np.linspace(0.05,5.9,400):
        z=12-3*x-2*y
        if z>0: best=max(best,x**3*y*y*z)
assert best<=64+1e-9 and best>63.5 and 8*4*2==64
