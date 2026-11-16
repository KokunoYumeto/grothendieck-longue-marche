"""Common source-based local markings for every w-pencil lasso.

Exact local type, transport and literal source-word membership are separate checks.
"""
from pathlib import Path
import json
from weighted_stallings import multiply as mul,inverse as inv,substitute as sub,WeightedFold
P=Path(__file__).resolve().parent
b=json.loads((P/'w_pencil_braids.json').read_text());d=json.loads((P/'w_pencil_fiber_data.json').read_text())
n=13;s0=b['source_position']+1
rem0=[i for i in range(1,n+1) if i!=s0];ren0={j:i+1 for i,j in enumerate(rem0)}
def artin(word):
 a={i:(i,) for i in range(1,n+1)}
 for x in word:
  k=abs(x);v,w=a[k],a[k+1]
  a[k],a[k+1]=(mul(v,w,inv(v)),v) if x>0 else (w,mul(inv(w),v,w))
 return a

def transport(word,s1):
 a=artin(word);v=a[s1];h=[]
 while len(v)>1:assert v[0]==-v[-1];h.append(v[0]);v=v[1:-1]
 assert v==(s0,)
 def fill(w):return mul(tuple(ren0[abs(x)]*(1 if x>0 else -1) for x in w if abs(x)!=s0))
 q=fill(h);rem1=[j for j in range(1,n+1) if j!=s1]
 T={i+1:mul(inv(q),fill(a[j]),q) for i,j in enumerate(rem1)}
 f=WeightedFold(list(T.values()));Ti={j:f.rewrite((j,)) for j in range(1,13)}
 assert all(w is not None for w in Ti.values())
 for j in range(1,13):assert sub(T[j],Ti)==(j,) and sub(Ti[j],T)==(j,)
 return T,Ti

def blocks(row):
 name=row['name']
 if name=='base_zero':return [[0,1,2,3,4,5,6,12]],[0,6]
 if name.startswith('base_positive_'):
  k=int(name.rsplit('_',1)[1]);cl=[1+k,6,7+(2*k)%5]
  if k==0:cl.append(12)
  return [cl]+[[1+j,7+(k+j)%5] for j in range(5) if j!=k],([7,12] if k==0 else [])
 if name.startswith('filled_negative_'):
  k=int(name.rsplit('_',1)[1]);return [[6,7+(2*k)%5]],[]
 if name=='source_zero_v':return [[0,12]],[]
 if name.startswith('source_constant_'):return [[1+int(name.rsplit('_',1)[1]),12]],[]
 if name.startswith('source_product_'):return [[7+int(name.split('_')[2]),12]],[]
 raise AssertionError(name)

source={int(k):tuple(w) for k,w in d['source_fiber_words'].items()}
source_order=sorted(source);source_list=[source[i] for i in source_order]
fsource=WeightedFold(source_list,allow_relations=True)
result=[]
for index,row in enumerate(b['loops']):
 local_order=row['forward_segments'][1]['initial_order'];sl=local_order.index(12)+1
 prefix=tuple(b['common_trunk']['word'])+tuple(row['forward_segments'][0]['word'])
 local=mul(*(r['word'] for r in row['forward_segments'][1:]));cs,nested=blocks(row)
 expected=[]
 for cl in cs:
  positions=sorted(local_order.index(j) for j in cl)
  assert positions==list(range(positions[0],positions[-1]+1)),(row['name'],'noninterval',cl,positions)
  expected+=list(range(positions[0]+1,positions[-1]+1))*len(cl)
 if nested:
  pos=sorted(local_order.index(j) for j in nested);assert pos[1]==pos[0]+1
  expected += [pos[0]+1]*2
 assert artin(local)==artin(expected),(row['name'],'local type')
 T,Ti=transport(prefix,sl)
 local_fiber_labels=[j for j in local_order if j!=12]
 transported={label:T[i+1] for i,label in enumerate(local_fiber_labels)}
 source_exp={label:fsource.rewrite(w) for label,w in transported.items()}
 for label,w in source_exp.items():
  if w is not None:assert sub(w,{i+1:v for i,v in enumerate(source_list)})==transported[label]
 rr={'index':index,'name':row['name'],'local_order':local_order,'source_local_position':sl,'local_braid':local,'standard_local_braid':expected,'blocks':cs,'nested_pair':nested,'local_to_initial_fiber':T,'initial_to_local_fiber':Ti,'transported_peripheral_words_by_label':transported,'expressions_in_13_source_fiber_words':source_exp}
 result.append(rr)
 print(row['name'],'local form and both12-basis transports PASS; source-word meridians',[j for j,w in source_exp.items() if w is not None],flush=True)
# The source-modified w1 marking: all3 cluster meridians are kept separate.
w1=result[1];cluster=[1,6,7];outer=[j for j in range(12) if j not in cluster]
combined=source_list+[w1['transported_peripheral_words_by_label'][j] for j in cluster]
f=WeightedFold(combined,allow_relations=True);back={i:f.rewrite((i,)) for i in range(1,13)}
print('w1 actual cluster plus13 source words generates full F12:',all(w is not None for w in back.values()),flush=True)
out={'description':__doc__,'source_word_order':source_order,'all_local_markings':result,'w1_cluster_labels':cluster,'w1_exterior_labels':outer,'w1_exterior_source_membership':{j:w1['expressions_in_13_source_fiber_words'][j] for j in outer},'w1_cluster_plus_source_inverse_words':back,'scope':'Each listed source-word expression is literal. A failed rewrite means only failure in this finite fiber subgroup, not nonmembership in the full source image. No entire-kernel normalizer is inferred from local pair relations.'}
(P/'w_local_markings.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all24 actual common local markings',flush=True)
