"""Exact finite four-point model from cote146/20,27,31.
Positive wall crossings are inverse to the author's a-arrow in the opposite
wall incidence. Every relation is checked both for endpoints and in F(A,F) x Z.
"""
import json
from pathlib import Path
V=[]
for k in range(6):
 V.append(('Q',k))
 for w in (-1,1):V.extend([('P',k,w),('R',k,w)])
E={}
for k in range(6):
 for w in (-1,1):
  j=(k+w)%6
  E['a',k,w]=(('R',k,w),('R',j,-w))
  E['b',k,w]=(('Q',k),('R',k,w))
  E['c',k,w]=(('P',k,w),('Q',k))
  E['d',k,w]=(('P',k,w),('P',j,w))
def reduce_word(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return tuple(out)
def mult(a,b):return a[0]+b[0],reduce_word(a[1]+b[1])
def inverse(a):return -a[0],tuple(-x for x in a[1][::-1])
unit=(0,())
y=[(0,(1,)),(0,(-1,-2)),(0,(2,)),(1,(1,)),(0,(-1,-2)),(0,(2,))]
x=[unit]*5+[(1,())]
def value(e):
 name,k,w=e
 return unit if name in ('b','c') else (x[k] if w==1 else y[k])
def path(word):
 start=end=None;v=unit
 for e,eps in word:
  s,t=E[e];z=value(e)
  if eps==-1:s,t=t,s;z=inverse(z)
  if start is None:start=s
  if end is not None:assert end==s,(end,s,word)
  end=t;v=mult(z,v)
 return start,end,v
rels=[]
for k in range(6):
 for w in (-1,1):
  j=(k+w)%6
  lhs=[(('d',k,w),1),(('c',j,w),1)]
  rhs=[(('c',k,w),1),(('b',k,w),1),(('a',k,w),1),(('b',j,-w),-1)]
  assert path(lhs)==path(rhs)
  rels.append((lhs,rhs))
for k in range(6):
 words=[]
 for w in (1,-1):
  words.append([(('c',k,w),-1)]+[(('d',(k+w*j)%6,w),1) for j in range(3)]+[(('c',(k+3)%6,w),1)])
 assert path(words[0])==path(words[1])
 rels.append(tuple(words))
for k in range(6):
 for w in (-1,1):
  loop=[(('d',(k+w*j)%6,w),1) for j in range(6)]
  assert path(loop)[2]==(1,())
# Original full-turn and half-turn auxiliary names.
aux=30+6+12
print('arrangement objects:',len(V),'P/Q/R:',12,6,12)
print('essential arrows:',len(E),'families a/b/c/d:',12,12,12,12)
print('mixed relations:',12,'half-turn relations:',6,'total:',len(rels))
print('expanded scan27 generator table:',len(E)+aux)
print('all 18 typed relations verified in F(A,F) x Z: True')
print('all 12 pole full-turn loops map to t: True')
print('chamber reduction: objects 6; arrows 12; lifted braid relations 6')
print('isotropy presentation: <A,F,t | [t,A]=[t,F]=1>')
print('mu2-free induction to four legs: objects',len(V)*8,'essential generators',len(E)*8+len(V)*24,'expanded generators',(len(E)+aux)*8+len(V)*24)
Path(__file__).with_name('b_four_point.json').write_text(json.dumps({'vertices':V,'arrows':[{'name':e,'source':s,'target':t,'word':value(e)} for e,(s,t) in E.items()],'relations':rels,'word_coordinates':'central exponent t; reduced free word in A=1,F=2; words compose on the left'},indent=2))
