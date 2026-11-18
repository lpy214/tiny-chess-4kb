import json,os
from urllib.request import*
U=os.environ["MAKEFUN_ENV_URL"]
V=[0,100,320,330,500,900,0]
T=["KKKKKKKKUUUUUUUUMMOQQOMMLLMPPMLLKKKOOKKKLJIKKIJLLMMGGMMLKKKKKKKK","ACEEEECACGKKKKGCEKMNNMKEELNOONLEEKNOONKEELMNNMLECGKLLKGCACEEEECA","GIIIIIIGIKKKKKKIIKLMMLKIILLMMLLIIKMMMMKIIMMMMMMIILKKKKLIGIIIIIIG","KKKKKKKKLMMMMMMLJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJKKKLLKKK","GIIJJIIGIKKKKKKIIKLLLLKIJKLLLLKJKKLLLLKJILLLLLKIIKLKKKKIGIIJJIIG","ECCAACCEECCAACCEECCAACCEECCAACCEGEECCEEGIGGGGGGIOOKKKKOOOQMKKMQO"]
KN=[-33,-31,-18,-14,14,18,31,33]
DG=[-17,-15,15,17]
OG=[-16,-1,1,16]
KG=DG+OG
N=[0,25000];K={}
X=StopIteration
def F(f):
 p=f.split();b=[0]*128;r=q=0
 for c in p[0]:
  if c=='/':r+=1;q=0
  elif c.isdigit():q+=int(c)
  else:i="PNBRQKpnbrqk".find(c);b[r*16+q]=((i<6)*2-1)*(i%6+1);q+=1
 e=-1 if p[3]=='-' else (8-int(p[3][1]))*16+ord(p[3][0])-97
 return b,1 if p[1]=='w' else-1,p[2],e
def A(b,q,y):
 for o in(15*y,17*y):
  x=q+o
  if not x&136 and b[x]==y:return 1
 for o,pc in((KN,2),(KG,6)):
  for d in o:
   x=q+d
   if not x&136 and b[x]==pc*y:return 1
 for o,ps in ((DG,(3,5)),(OG,(4,5))):
  for d in o:
   x=q+d
   while not x&136:
    if b[x]:
     if b[x] in (ps[0]*y,ps[1]*y):return 1
     break
    x+=d
 return 0
def M(b,s,c,e,v):
 q,t,pr=v;w=list(b);p=w[q];w[q]=0;d=-16*s
 if abs(p)==1 and t==e and not w[t]:w[t-d]=0
 w[t]=pr*s if pr else p
 if abs(p)==6 and abs(t-q)==2:
  if t>q:w[q+1]=w[q+3];w[q+3]=0
  else:w[q-1]=w[q-4];w[q-4]=0
 n=c
 if abs(p)==6:n=n.replace('K','').replace('Q','') if s==1 else n.replace('k','').replace('q','')
 for z,cs in zip((119,112,7,0),'KQkq'):
  if q==z or t==z:n=n.replace(cs,'')
 return w,-s,n,q+d if abs(p)==1 and abs(t-q)==32 else -1
def G(b,s,c,e):
 m=[]
 for q,p in enumerate(b):
  if p*s<=0:continue
  a=abs(p)
  if a==1:
   d=-16*s;t=q+d
   if not t&136 and not b[t]:
    if (t>>4) in (0,7):m.append((q,t,5))
    else:
     m.append((q,t,0))
     if (q>>4)==6-5*(s<0) and not b[q+2*d]:m.append((q,q+2*d,0))
   for o in (d-1,d+1):
    t=q+o
    if t&136:continue
    if b[t]*s<0 or t==e:m.append((q,t,5 if (t>>4) in (0,7) else 0))
  elif a==2 or a==6:
   for o in KN if a==2 else KG:
    t=q+o
    if not t&136 and b[t]*s<=0:m.append((q,t,0))
  else:
   for o in DG if a==3 else OG if a==4 else DG+OG:
    t=q+o
    while not t&136:
     if not b[t]:m.append((q,t,0))
     elif b[t]*s<0:m.append((q,t,0));break
     else:break
     t+=o
 for k0,kr,ks,cs in ((116,119,1,'K'),(116,112,-1,'Q'),(4,7,1,'k'),(4,0,-1,'q')):
  if cs in c and b[k0]==6*s and b[kr]==4*s and not b[k0+ks] and not b[k0+2*ks] and (ks==1 or not b[k0+3*ks]) and not A(b,k0,-s) and not A(b,k0+ks,-s) and not A(b,k0+2*ks,-s):m.append((k0,k0+2*ks,0))
 o=[]
 for v in m:
  w,ns,nc,ne=M(b,s,c,e,v)
  if not A(w,w.index(6*s),-s):o.append(v)
 return o
def E(b):
 v=0
 for q,p in enumerate(b):
  if p:
   a=abs(p);i=((q>>4) if p>0 else 7-(q>>4))*8+(q&7)
   v+=(V[a]+(ord(T[a-1][i])-75)*5)*(p/abs(p))
 return v
def S(b,s,c,e,d,a,be,pl):
 N[0]+=1
 if N[0]>N[1]:raise X
 if d==0 and not A(b,b.index(6*s),-s):
  st=E(b)*s
  if st>=be:return be
  if st>a:a=st
  if pl>6:return a
  v=[x for x in G(b,s,c,e) if b[x[1]] or x[1]==e]
 else:
  v=G(b,s,c,e)
  if not v:
   return -99999+pl if A(b,b.index(6*s),-s) else 0
 v.sort(key=lambda x:(x!=K.get(pl),-abs(b[x[1]])))
 for x in v:
  w,ns,nc,ne=M(b,s,c,e,x)
  sc=-S(w,ns,nc,ne,d-1 if d else 0,-be,-a,pl+1)
  if sc>a:a=sc
  if a>=be:K[pl]=x;break
 return a
def C(fen,l):
 b,s,c,e=F(fen);best=l[0];N[0]=0
 for d in range(1,6):
  try:
   l.sort(key=best.__ne__)
   cur=l[0];cs=-10**9
   for u in l:
    fr=(8-int(u[1]))*16+ord(u[0])-97;to=(8-int(u[3]))*16+ord(u[2])-97
    pr=(5,2,3,4)["qnbr".find(u[4])] if len(u)==5 else 0
    w,ns,nc,ne=M(b,s,c,e,(fr,to,pr))
    sc=-S(w,ns,nc,ne,d-1,-10**9,-cs,1)
    if sc>cs:cs=sc;cur=u
   best=cur
  except X:break
 return best
def P(p,y):
 with urlopen(U+p,json.dumps(y).encode()) as x:return json.load(x)
while True:
 g=P("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  g=P("/move",{"game":g["game"],"move":C(g["fen"],g["legal_moves"])})
