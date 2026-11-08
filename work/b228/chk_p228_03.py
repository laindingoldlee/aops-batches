import math, itertools, random
from fractions import Fraction as F
random.seed(3)
ip=lambda n: n>1 and all(n%d for d in range(2,math.isqrt(n)+1))
# 1748824
assert not ip(2*2+4)
odd=[p for p in range(3,100) if ip(p) and p%10 in (3,7) and not ip(p*p+4)]
assert odd[:3]==[23,43,53] and 533==13*41 and 1853==17*109
assert all((p*p+4)%5==0 for p in range(1,1000) if p%10 in (1,9))
# 1717495
for x in range(-10,10):
    assert -2*x+5+10*x-9==8*x-4 and 3*(x+7)+2*(-x+4)+5*x==6*x+29
# 1748217 chords
r2=F(481,16); assert 25+F(9,4)**2==r2 and 16+F(15,4)**2==r2 and F(9,4)+F(15,4)==6
# 1748217 walking polygons
assert 360//18*8==160 and 360//15*6==144 and math.lcm(160,144)==1440
def poly(step,h0,turn,n):
    p=complex(0,0);pts=[p];h=h0
    for i in range(n):
        p+=step*complex(math.cos(math.radians(h)),math.sin(math.radians(h)));pts.append(p);h+=turn
    return pts
K=poly(8,90,18,20);Al=poly(6,-90,15,24)
assert abs(K[-1])<1e-9 and abs(Al[-1])<1e-9
assert all(z.real<=1e-9 for z in K) and all(z.real>=-1e-9 for z in Al)
# 1747922
assert math.comb(11,4)==330 and 330*math.factorial(7)==1663200==math.factorial(11)//math.factorial(4)
# brute force small case: 3 people, 2 machines -> C(4,1)*3! = 24
cnt=0
for perm in itertools.permutations(range(3)):
    for cut in range(4): cnt+=1
assert cnt==24==math.comb(4,1)*6
# 1746735
assert all((m+n)%24==0 for m in range(-200,200) for n in range(-200,200) if (m*n+1)%24==0)
# 1748168
x,y,z=-2,-4,5; assert -x-y-3*z==-9 and z==-3*x-1 and x==5*y-z+23
# 1747797
assert (1-0+1)*(0-0+2)*(0-1+3)==8
for _ in range(20000):
    a,b=random.uniform(0,6),random.uniform(0,6); c=6-a-b
    if c>0: assert a*b*c<=8+1e-9
t=100; assert t*t*(6+2*t)>10**6
# 1746979
for _ in range(200):
    a=random.choice([q for q in range(-9,10) if q]); b,c=random.sample(range(-9,10),2); d,e=random.randint(-9,9),random.randint(-9,9)
    X=F(b*e-c*d,a*(b-c)); Y=F(d-e,b-c); assert a*X+b*Y==d and a*X+c*Y==e
# 1747574
T=[k*(k+1)//2 for k in range(3000)];TS=set(T)
tri=lambda m: math.isqrt(8*m+1)**2==8*m+1
assert all(tri(9*n+1) and tri(25*n+3) and tri(49*n+6) for n in T[:2000])
assert not tri(26) and not tri(50)
# 1747745
def phi(m): return sum(1 for k in range(1,m+1) if math.gcd(k,m)==1)
N=3000
ph=[0]+[0]*N
for m in range(1,N+1): ph[m]=m
for p in range(2,N+1):
    if ph[p]==p:
        for q in range(p,N+1,p): ph[q]-=ph[q]//p
assert all(ph[m]==phi(m) for m in range(1,200))
S=set()
for n in range(10,N+1):
    v=n
    while v>=10: v=ph[v]
    S.add(v)
assert S=={4,6,8}
assert [m for m in range(1,N+1) if ph[m]==2]==[3,4,6]
# 1747765
assert all(sum(range(1,n+1))==n*(n+1)//2 for n in range(1,100))
# 1747731 q01 (DP count)
ways=[0]*150; ways[0]=1
for n in range(1,7):
    new=[0]*150
    for s in range(150):
        if ways[s]:
            for a in range(n+1,150-s): new[s+a]+=ways[s]
    ways=new
assert sum(ways[:150])==math.comb(128,6)==5423611200
# 1747731 q02 exact and simulation
vol=5*75+(F(75,2)*5+5*25-F(125,6))
assert vol==F(2000,3) and vol/9000==F(2,27)
random.seed(5);n=400000;hit=0
for _ in range(n):
    A=random.uniform(0,30);B=random.uniform(10,40);C=random.uniform(20,30)
    if max(A,B,C)-min(A,B,C)<=5: hit+=1
assert abs(hit/n-2/27)<0.003
# 1747731 q03
for n in range(1,20):
    xs=[n+0.001*k for k in range(1,40000)]
    xm=min(xs,key=lambda x:x*x/(x-n)); assert abs(xm-2*n)<0.002
assert 2*5050==10100
# 1747731 q04 Euler line
for _ in range(100):
    P=[(random.uniform(-5,5),random.uniform(-5,5)) for _ in range(3)]
    (ax,ay),(bx,by),(cx,cy)=P
    d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    if abs(d)<1e-3: continue
    ux=((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)*(ay-by))/d
    uy=((ax*ax+ay*ay)*(cx-bx)+(bx*bx+by*by)*(ax-cx)+(cx*cx+cy*cy)*(bx-ax))/d
    hx,hy=ax+bx+cx-2*ux,ay+by+cy-2*uy
    assert abs((hx-ax)*(bx-cx)+(hy-ay)*(by-cy))<1e-6
    gx,gy=(ax+bx+cx)/3,(ay+by+cy)/3
    assert abs(math.hypot(hx-ux,hy-uy)-3*math.hypot(gx-ux,gy-uy))<1e-6
# 1747684
assert max(y*(72-2*y) for y in range(0,37))==648
# 1747571
assert all((n in TS)==(math.isqrt(8*n+1)**2==8*n+1) for n in range(0,20000))
# 1746837 (proof; SAS check of side lengths)
d1,d2,th=5.,3.,math.radians(70)
AB=math.sqrt((d1/2)**2+(d2/2)**2-2*(d1/2)*(d2/2)*math.cos(math.pi-th)); assert AB>0
# 1747120
assert (-2)*3==-6 and (-2)*(-3)==6
# 1747361 (alias)
assert [(p,q) for p in range(3,20) for q in range(3,20) if (p-2)*(q-2)<4]==[(3,3),(3,4),(3,5),(4,3),(5,3)]
# 1741498 (alias)
assert F(2,5)==F(1,5)+F(1,5)
# 1747050
sums={sum(c) for k in range(1,5) for c in itertools.combinations([25,10,5,1],k)}; assert len(sums)==15
# 1706241
x=2+math.sqrt(3); assert abs(x+1/x-4)<1e-12 and abs(x**5+x**-5-724)<1e-6
# 1738203
assert math.comb(9,4)*F(1,5)**4*F(4,5)**5==F(129024,1953125)
assert len(range(1,37,4))==9
pr=1-F(28,31)**9; assert abs(float(pr)-0.600)<0.001
random.seed(7);n=100000;h=0
for _ in range(n):
    p=list(range(32));random.shuffle(p)
    if p.index(0)//4==p.index(1)//4: h+=1
assert abs(h/n-3/31)<0.004
# 1742452
assert F(1,7)*F(5,6)+F(6,7)*F(1,6)==F(11,42)
# 1746955
for _ in range(20000):
    a,b,c=[abs(random.gauss(0,1))+1e-9 for _ in range(3)]
    r=math.sqrt(a*a+b*b+c*c);a,b,c=a/r,b/r,c/r
    xs=[1-a*b,1-b*c,1-c*a]
    assert sum(math.sqrt(v) for v in xs)>=math.sqrt(6)-1e-12
    p=a*b+b*c+c*a;q=(a*b)**2+(b*c)**2+(c*a)**2
    assert q<=1/3+1e-12 and p<=1+1e-12
    assert sum(math.sqrt(v) for v in xs)**2*sum(v*v for v in xs)>=sum(xs)**3-1e-9
for p in [i/1000 for i in range(1001)]:
    assert abs((3-p)**3-20+12*p-(1-p)**2*(7-p))<1e-9
# 1746950
s=1320/3**0.25; assert abs(math.sqrt(3)/4*s*s-435600)<1e-6 and round(s)==1003 and 1320**2==1742400
# 1742477
assert sum(1 for a in range(1,6) for b in range(1,6) if (a+b)%3==0)==9
# 1746203
assert all(a*a%8==1 for a in range(-99,100,2))
assert all(pow(a,3,7) in (0,1,6) for a in range(-50,50))
assert all(pow(a,4,5) in (0,1) for a in range(-50,50))
assert all(a*a%24==1 for a in range(-200,200) if a%2 and a%3)
# 1746596
assert all((n+1)*(n+2)-n*(n+3)==2 for n in range(-50,50))
# 1745510
assert sum(1 for s in itertools.product(range(10),repeat=5) if all(x!=y for x,y in zip(s,s[1:])))==65610
