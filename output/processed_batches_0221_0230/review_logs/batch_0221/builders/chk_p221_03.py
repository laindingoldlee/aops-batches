import math, itertools, random
from fractions import Fraction as F
import numpy as np
# 1786013
for _ in range(200):
    a,b,x=[random.randint(-30,30) for _ in range(3)]
    assert 4*a*a-12*a*b+9*b*b-x*x==(2*a-3*b-x)*(2*a-3*b+x)
# 1785283
assert F(4*729,1)/(F(4,3)*729)==3
# 1785779 alias
assert 300/25-300/30==2
# 1780989 P1 regular hexagon
V=[(math.cos(math.pi/3*i),math.sin(math.pi/3*i)) for i in range(6)]
def iso(t):
    d=sorted(round(math.dist(V[i],V[j]),9) for i,j in itertools.combinations(t,2))
    return d[0]==d[1] or d[1]==d[2]
assert F(sum(iso(t) for t in itertools.combinations(range(6),3)),20)==F(2,5)
# 1780989 P2
assert [b for b in range(102) if 0.575<=b*(b-1)/10100<0.585]==[77] and not any(b*(b-1)==5858 for b in range(102))
# 1785255 seven clues
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
def ok(n):
    s=str(n)
    if not (n%3==0 and isprime(n//3)): return False
    if sum(map(int,str(2*n)))!=12: return False
    if not 50<n<500: return False
    rest=int(s[1:]) if len(s)>1 else 0
    if rest==0 or F(int(s[0]),rest)!=F(10,sum(map(int,s))): return False
    if any(c in '2357' for c in s): return False
    if int(s[0])+int(s[1])!=15: return False
    if [d for d in range(2,10) if n%d==0]!=[3]: return False
    return True
assert [n for n in range(1,1000) if ok(n)]==[69]
# 1785658
assert 360/12==30
assert {14-19,14+19}=={-5,33}
assert F(2,3)*F(-3,2)==-1 and 2*4-3*5==-7
Q=np.linalg.solve([[3,2],[2,-3]],[7,-7]); assert np.allclose(Q,[7/13,35/13])
# 1785804
assert abs(math.pi*3.5**2*5.6/(4/3*math.pi*0.7**3)-150)<1e-9
# 1785113
xs=[x for x in range(100,1000) if (x//10)%10==4 and F(242,x)==F(22,(x//100)*10+x%10)]
assert xs==[143,242,341,440] and max(xs)==440
assert F(154,253)==F(14,23)
# 1785758 brute force: minimal k for each n, and minimal n overall
def best_k(n):
    s=0;k=-1
    while s<2019:
        k+=1;s+=(n+k)%5
    return k if s==2019 else None
res={n:best_k(n) for n in range(1,30)}
good=[n for n in res if res[n] is not None]
assert min(good)==2 and res[2]==1007 and min(res[n] for n in good)==1007
# 1695399 aliases
assert math.comb(21,2)+10==220
def paths():
    c=0
    for p in set(itertools.permutations('xxyyzz')):
        x=[0,0,0];okp=True
        for m in p:
            x['xyz'.index(m)]+=1
            if x==[1,1,1]: okp=False
        c+=okp
    return c
assert paths()==54
def interior(n):
    return sum(1 for x in range(1,10) for y in range(1,n+1) if 1<x<9 and y>1 and (y-1)*8<(n-1)*(x-1))
assert interior(162)==560
# 1785284
assert 60/3-60/4==5
# 1785275 numeric
O=np.zeros(2);P=np.array([3.2,0]);r=1.5;ang=math.acos(r/3.2)
A=r*np.array([math.cos(ang),math.sin(ang)]);B=r*np.array([math.cos(ang),-math.sin(ang)])
assert abs(np.dot(A-O,P-A))<1e-12 and abs(np.linalg.norm(P-A)-np.linalg.norm(P-B))<1e-12
assert abs(np.dot(A-B,P-O))<1e-12 and abs(((A+B)/2)[1])<1e-12
# 1785367
N=next(n for n in range(2005,10000) if math.isqrt((n+5)**2-n*n)**2==(n+5)**2-n*n); assert N==2100
assert 5*(33**2-1)//2==2720
# 1782142
assert 40*1.5**3==135
# 1784530
rows={'A':1,'B':3,'C':2,'D':11,'E':13}
assert [k for k,v in rows.items() if (86-v)%7==0 and 86>=v]==['C']
# 1781243
d=F(42)
for _ in range(3): d=d*F(2,3)
assert d==F(112,9)
d5=42*F(2,3)**5; assert 42-d5==F(2954,81)
assert sum(42*F(1,3)*F(2,3)**k for k in range(5))==F(2954,81) and 42*F(1,3)*F(2,3)**4==F(224,81)
# 1785265
assert abs(math.tan(math.radians(60))-math.sqrt(3))<1e-12 and abs(math.tan(0))<1e-12
# 1784529
assert sum(3**k for k in range(8))==3280
# 1784580
assert 49+(15-6)**2==9+(15-4)**2==130
# 1784598
assert (300-102)%4!=0 and 298 in range(102,400,4) and 302 in range(102,400,4)
# 1781932 alias
assert [n for n in range(1,2000) if sorted(str(n*n)+str(n**3))==list('0123456789')]==[69]
# 1784461 alias
x=2/3; assert abs(16**x-4*2**x)<1e-12
