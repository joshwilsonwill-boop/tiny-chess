import json,os
from urllib.request import urlopen
U=os.environ["MAKEFUN_ENV_URL"]
def h(p,b):
 try:
  with urlopen(U+p,json.dumps(b).encode()) as s:return json.load(s)
 except Exception:return None
V=[0,100,320,330,500,900,0]
W=[4,2,3,5,6,3,2,4]
S="SSSSX]]?XNISSSSgXX]l]]gq{{{{SSSS"
A=[0]+[[ord(S[(i>>4)*4+min(i&7,7-(i&7))])-83 for i in range(128)]]+[[0]*128]*5
Q=[i for i in range(128) if not i&136]
O=[31,33,14,18,-31,-33,-14,-18]
J=[15,17,-15,-17]
R=[1,-1,16,-16]
I=R+J
M={0:13,7:14,4:12,112:7,119:11,116:3}
B=[0]*128;T=0;C=15;E=-1;K=[4,116];N=[0];D=80000
class Z(Exception):pass
def q(s):return (ord(s[1])-49)*16+ord(s[0])-97
def n(x):return chr(97+(x&7))+str((x>>4)+1)
def u(m):
 f=m&127;t=(m>>7)&127;pr=m>>14
 return n(f)+n(t)+("nbrq"[pr-2] if pr else "")
def o(s):
 f=q(s[:2]);t=q(s[2:4]);pr="nbrq".index(s[4])+2 if len(s)==5 else 0
 return f|t<<7|pr<<14
def v(m):
 global T,C,E
 f=m&127;t=(m>>7)&127;pr=m>>14
 p=B[f];c=B[t]
 B[t]=p;B[f]=0
 if pr:B[t]=pr|(p&8)
 if (p&7)==6:
  K[T]=t
  if abs(t-f)==2:
   a=t+1 if t>f else t-2;b=t-1 if t>f else t+1;B[b]=B[a];B[a]=0
 elif (p&7)==1 and t==E and (t&7)!=(f&7):
  w=t-16+32*T;c=B[w];B[w]=0
 u=(m,c,C,E)
 C&=M.get(f,15)&M.get(t,15)
 E=(f+t)//2 if (p&7)==1 and abs(t-f)==32 else -1
 T^=1
 return u
def x(u):
 global T,C,E
 m,c,C,E=u
 f=m&127;t=(m>>7)&127;pr=m>>14
 p=B[t]
 T^=1
 e=(p&7)==1 and t==E and (t&7)!=(f&7)
 if (p&7)==6:
  K[T]=f
  if abs(t-f)==2:a=t+1 if t>f else t-2;b=t-1 if t>f else t+1;B[a]=B[b];B[b]=0
 B[t]=0 if e else c
 if e:B[t-16+32*T]=c
 B[f]=1|(p&8) if pr else p
def at(s,by):
 for L,pc in (((-15,-17) if by==0 else (15,17),1),(O,2),(I,6)):
  for o in L:
   if not (s+o)&136 and B[s+o]==pc+8*by:return 1
 for L,ty in ((J,3),(R,4)):
  for o in L:
   r=s+o
   while not r&136 and not B[r]:r+=o
   if not r&136 and (B[r]>>3)==by and (B[r]&7) in (5,ty):return 1
 return 0
DIRS=[0,0,O,J,R,I,I]
def pm(L,q,r):
 for pr in (5,4,3,2):L.append((10000+V[pr],q|r<<7|pr<<14))
def g(c):
 ms=[];d=16 if T==0 else -16;pr=(6 if T==0 else 1);st=(1 if T==0 else 6)
 for sq in Q:
  p=B[sq]
  if not p or (p>>3)!=T:continue
  t=p&7
  if t==1:
   P=(sq>>4)==pr
   for o in (d,d-1,d+1):
    r=sq+o
    if r&136:continue
    v=B[r];mv=sq|r<<7
    if o==d:
     if v:continue
     if P:pm(ms,sq,r)
     elif not c:
      ms.append((0,mv))
      if (sq>>4)==st and not B[sq+2*d]:ms.append((0,sq|(sq+2*d)<<7))
    elif v and (v>>3)!=T:
     if P:pm(ms,sq,r)
     else:ms.append((10000+V[v&7],mv))
    elif r==E and (r&7)!=(sq&7):ms.append((10000,mv))
  else:
   for o in DIRS[t]:
    r=sq+o
    while not r&136:
     v=B[r]
     if v:
      if (v>>3)!=T:ms.append((10000+V[v&7],sq|r<<7))
      break
     if not c:ms.append((0,sq|r<<7))
     if t in (2,6):break
     r+=o
   if t==6:
    for k,bit,far in ((1,1<<2*T,0),(-1,2<<2*T,1)):
     if C&bit and not any(B[sq+i*k] for i in (1,2,3)[:2+far]) and not any(at(sq+i*k,T^1) for i in (0,1,2)):ms.append((0,sq|(sq+2*k)<<7))
 ms.sort(reverse=True)
 return ms
def f(a,b,d):
 N[0]+=1
 if N[0]>D:raise Z
 ik=at(K[T],T^1)
 n=0
 if d<=0 and not ik:
  s=0
  for sq in Q:
   p=B[sq]
   if p:
    t=p&7
    s+=V[t]+A[t][sq] if p<8 else -(V[t]+A[t][sq^112])
  s=s if T==0 else -s
  if s>=b:return b
  if s>a:a=s
 for sc,m in g(0 if d>0 or ik else 1):
  u=v(m)
  if at(K[T^1],T):x(u);continue
  s=-f(-b,-a,d-1)
  x(u)
  n+=1
  if s>a:a=s
  if a>=b:break
 if not n and (d>0 or ik):return -30000 if ik else 0
 return a
def r():
 N[0]=0
 leg=[]
 for sc,m in g(0):
  u=v(m)
  if at(K[T^1],T):x(u);continue
  leg.append(m);x(u)
 if not leg:return None
 best=leg[0]
 for d in range(1,13):
  try:
   a=-30000
   for m in leg:
    u=v(m)
    s=-f(-30000,-a,d-1)
    x(u)
    if s>a:a=s;best=m
   leg.remove(best);leg.insert(0,best)
  except Z:break
 return best
def m():
 global T,C,E
 while True:
  z=h("/game",{})
  if z is None:continue
  if z["status"]=="done":break
  B[:]=[0]*128
  for i in range(8):B[i]=W[i];B[112+i]=W[i]+8;B[16+i]=1;B[96+i]=9
  T=0;C=15;E=-1;K[:]=[4,116]
  for w in z["moves"]:v(o(w))
  if z["status"]=="your_move":
   h("/move",{"game":z["game"],"move":u(r())})
m()
