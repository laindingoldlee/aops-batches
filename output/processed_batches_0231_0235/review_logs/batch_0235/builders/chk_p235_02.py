import math, itertools, random
from fractions import Fraction as F
import numpy as np
random.seed(2)
# 1709625
s=F(2,5); assert (s/2)**2+(1+s)**2==2 and s*s/4==F(1,25)
# 1709552
P=100; assert F(P,2)+F(P,4)+F(P,5)+5==P and F(P,4)==F(P-F(P,4),3) and F(P,5)==F(P-F(P,5),4)
# 1709584
for _ in range(2000):
    a,b,c=sorted([random.uniform(0.1,10) for _ in range(3)],reverse=True)
    assert a/b+b/c+c/a<=b/a+c/b+a/c+1e-12
    D=a*a*b+b*b*c+c*c*a-a*a*c-a*b*b-b*c*c; assert abs(D-(a-b)*(b-c)*(a-c))<1e-9
# 1708983
d2=F(2*540,45); assert d2==24
side=math.hypot(22.5,12); assert abs(side-25.5)<1e-12
assert abs(22.5*12/25.5-180/17)<1e-12
# 1709567
assert abs(2*2018-0.95*1.4*2018-1352.06)<1e-9
# 1709580
assert [n for n in range(1000,10000) if 4*n+30==int(str(n)[::-1])]==[2018]
# 1709569
nz=[(a,b,c) for a in range(1,10) for b in range(1,10) for c in range(1,10) if 20*a+11*b+2*c==293]
assert nz==[(9,9,7)] and 97+97+99==293
assert max(20*a+11*b+2*c for a,b,c in itertools.permutations(range(1,10),3))==282
# 1709312
assert F(600,F(19,2))==F(1200,19)
assert 2*60*F(200,3)/(60+F(200,3))==F(1200,19)
# 1705943
assert 4**6+8**3-32**2==7*2**9==3584
# 106088
assert F(4,5)**2*50==32
# 1702869
sol=[n for n in range(100,1000) if n%10 and 4*n%3==0 and 4*n//3==int(str(n)[-1]+str(n)[:-1])]
assert sol==[162,243,324,405,486,567,648,729]
# 1708628
A,B,C,D=map(np.array,[(0.,0.),(8.,0.),(8.,6.),(0.,6.)])
E=np.array([1.75,0.]);Fp=np.array([6.25,6.])
assert abs(np.linalg.norm(E-B)-np.linalg.norm(E-D))<1e-12 and abs(np.linalg.norm(Fp-B)-np.linalg.norm(Fp-D))<1e-12
assert abs(np.linalg.norm(E-Fp)-7.5)<1e-12
# 1708605
cnt=0
for pos in itertools.combinations(range(16),6):
    for ob in itertools.combinations(range(6),3):
        t=['M']*16
        for k,p in enumerate(pos): t[p]='O' if k in ob else 'B'
        t=''.join(t)
        if 'OB' not in t and 'BO' not in t: cnt+=1
assert cnt==40370
assert sum(math.comb(2,i-1)*math.comb(2,j-1)*math.comb(11,i)*math.comb(11-i,j) for i in range(1,4) for j in range(1,4))==40370
# 1708235 small-scale brute check of the bound idea and the construction
X=[1,122,222,223,224,225,226,227,229]
sums=[a+b for a,b in itertools.combinations(X,2)]
assert min(sums)==123 and max(sums)==456 and sum(X)==1699 and len(set(X))==9
# 1708041
N=3**19+2**19; D=3**15+2**15; assert N//D==80 and 81*D-N==65*2**15
# 1708333 q03
m=F(885730,59049)
for _ in range(10): m=3*m-30
assert 3*m==30 and 3*m-30==0
# 1708321
assert sum(1 for a in range(1,1004) for b in [2008-2*a] if b>0 and 2*a>b)==501
# 1294839
assert all(sum(3**i for i in range(n+1))==(3**(n+1)-1)//2 for n in range(20))
# 1707812
assert [n for n in range(8,1000) if all((n-7)%d==0 for d in (4,5,6))][0]==67
# 1706974
assert [b for b in range(20) if (9-(b+4))%20==0]==[5] and [b for b in range(3) if (1-(b+2))%3==0]==[2]
# 1707260
from functools import lru_cache
@lru_cache(None)
def p(n,r,mn=1):
    if r==0: return 1 if n==0 else 0
    return sum(p(n-x,r-1,x) for x in range(mn,n//r+1)) if n>=r*mn else 0
for N in range(1,61):
    assert p(N,2)==N//2
    assert p(N,3)==round(N*N/12) and abs(N*N/12-round(N*N/12))<0.5
    for r in range(2,N): assert p(N,r)==p(N-1,r-1)+p(N-r,r)
assert p(12,3)==12 and p(20,3)==33 and p(5,2)==2
# 1707676 q01
h=math.sqrt(216); A=np.array([3,h]);D=np.array([0.,0.]);B=np.array([15,h]);C=np.array([18.,0.])
E=D+(2.5/15)*(A-D);Fp=C+(2.5/15)*(B-C)
assert abs(np.linalg.norm(A-D)-15)<1e-12 and abs(np.linalg.norm(E-Fp)-17)<1e-12 and abs(E[1]-Fp[1])<1e-12
# q04
l=math.hypot(48,10); assert abs(l-2*math.sqrt(601))<1e-12
tot=2*36*math.pi+2*math.pi*(6+16)*l; assert abs(tot-(72+88*math.sqrt(601))*math.pi)<1e-9
# q05
V=[np.array([2*math.cos(math.radians(90+72*i)),2*math.sin(math.radians(90+72*i))]) for i in range(5)]
sc=2/np.linalg.norm(V[0]-V[1]); assert abs(sc*np.linalg.norm(V[0]-V[2])-(1+math.sqrt(5)))<1e-12
# 1706187
assert sum((-1)**(k%2)*k*k for k in range(1,51))==1275
# 1707744
assert sum(1 for a in range(6) for b in range(6) if 0<=12-a-b<=5)==10
# 1707054
assert sum(1 for c in itertools.combinations_with_replacement(range(6),4))==126
# 1704985
tot=lambda n: 3*n*(n+1)//2+(n+1)*(n+2)//2
assert tot(2)==15 and tot(8)==153 and all(tot(n)==(2*n+1)*(n+1) for n in range(1,20))
print('ok2')
