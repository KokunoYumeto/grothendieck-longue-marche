"""Read the actual common-marking transporters for the four missing-b triples."""
from pathlib import Path
import json,itertools
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'ratio_pencil_braids.json').read_text())
order=D['initial_order'];initial={label:i+1 for i,label in enumerate(order)}
def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def mul(*ws):return red(itertools.chain.from_iterable(ws))
def sub(w,A):return mul(*(A[x] if x>0 else inv(A[-x]) for x in w))
def artin(w):
 A={i:(i,) for i in range(1,21)}
 for x in w:
  i=abs(x);a,b=A[i],A[i+1]
  A[i],A[i+1]=(mul(a,b,inv(a)),a) if x>0 else (b,mul(inv(b),a,b))
 return A
def cyclic(w):
 k=0
 while len(w)-2*k>1 and w[k]==-w[-1-k]:k+=1
 return w[:k],w[k:len(w)-k] if k else w

a=initial[0];b=initial[3];assert b==a+1
rewrite={i:(i,) for i in range(1,21)};rewrite[a]=(a,-b)
inverse_rewrite={i:(i,) for i in range(1,21)};inverse_rewrite[a]=(a,b)
for i in range(1,21):assert sub(rewrite[i],inverse_rewrite)==(i,)==sub(inverse_rewrite[i],rewrite)
U=sorted(initial[j] for j in range(4,12))
fillH={i:() if i in U else (i,) for i in range(1,21)}
print('Original a,b basis indices:',a,b)
print('Special-fiber basis replaces a by a*b; missing generator index:',b)
print('Eight U basis indices:',U)
out=[]
for row in D['loops']:
 if not row['name'].startswith('b_triple_'):continue
 k=int(row['name'].rsplit('_',1)[1]);partner=5-k
 labels=[3,4+2*(k-1),5+2*(partner-1)]
 W=row['forward_segments'][0]['word'];A=artin(W);Ai=artin(inv(W))
 for i in range(1,21):assert sub(A[i],Ai)==(i,)==sub(Ai[i],A)
 endpoint=row['forward_segments'][0]['final_order']
 positions=[endpoint.index(label)+1 for label in labels]
 assert sorted(positions)==list(range(min(positions),max(positions)+1))
 local=mul(*(r['word'] for r in row['forward_segments'][1:]))
 l=min(positions);standard=(l,l+1,l,l,l+1,l)
 assert artin(local)==artin(standard),'local circle is not the positive full twist on its actual three strands'
 meridians=[A[i] for i in positions]
 for label,w in zip(labels,meridians):assert cyclic(w)[1]==(initial[label],)
 h,core=cyclic(meridians[0]);hn=sub(h,rewrite)
 while hn and abs(hn[-1])==b:hn=hn[:-1]
 newwords=[sub(w,rewrite) for w in meridians]
 inH=[all(abs(x)!=b for x in w) for w in newwords]
 UinK=[inH[j] and not sub(newwords[j],fillH) for j in (1,2)]
 rec={'name':row['name'],'whisker_braid':W,'local_positions':positions,'local_labels':labels,
      'meridians_original_basis':meridians,'meridians_special_basis':newwords,
      'b_conjugator_special_basis_mod_right_b':hn,
      'b_transporter_in_H':all(abs(x)!=b for x in hn),'U_meridians_in_H_kernel':UinK}
 out.append(rec)
 print(row['name'],'b transporter in H:',rec['b_transporter_in_H'],'U pair in H-kernel:',UinK,
       'b-conjugator length:',len(hn),flush=True)
(HERE/'pencil_triple_transports.json').write_text(json.dumps({'a':a,'b':b,'U':U,
 'original_initial_order':order,'old_to_special_basis':rewrite,'special_to_old_basis':inverse_rewrite,
 'triples':out,'scope':'Exact common based transports. Membership is tested in the generic free group, before global van Kampen relations.'},indent=2)+'\n')
print('PASS: all inverse Artin actions, local full-twist identities, and literal free-factor membership tests.')

