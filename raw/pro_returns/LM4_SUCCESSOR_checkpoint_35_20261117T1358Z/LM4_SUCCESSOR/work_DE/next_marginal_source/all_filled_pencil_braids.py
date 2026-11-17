"""The remaining25 filled critical lassos in the same twenty-strand marking.

This imports the exact Sturm/interval engine used for the six previously
certified loops. Discriminant circles are half twists and are not asserted
pure. No source-kernel normality is inferred from this output.
"""
from pathlib import Path
from fractions import Fraction as F
import itertools,json,time
import sympy as S
from quadratic_pencil_braid import Segment,u,frac,complex_sqrt,red,invert,I,Q
HERE=Path(__file__).resolve().parent

def rnd(x):
 return Q(round(frac(x)*10**30),10**30)
def rounded(z):return rnd(S.re(S.expand(z)))+I*rnd(S.im(S.expand(z)))
def norm2(z):return S.expand(S.re(z)**2+S.im(z)**2)
def make_centers():
 rows=[{'name':'special0','center':S.Integer(0),'type':'retained_double','expected_exponent':2}]
 for k,q in enumerate(u[1:],1):
  C=S.expand(q*(q-1));R,J=complex_sqrt(frac(S.re(C)),frac(S.im(C)))
  sq=Q(R[0].numerator,R[0].denominator)+I*Q(J[0].numerator,J[0].denominator)
  for sign in (1,-1):
   c=rounded(2*(1-q)+sign*2*sq)
   rows.append({'name':f'discriminant_{k}_{"plus" if sign==1 else "minus"}',
                'center':c,'type':'retained_half_twist','q_index':k,'expected_exponent':1})
  for side,c in [('constant',2-q),('moving',1+1/(1-q))]:
   rows.append({'name':f'zero_double_{k}_{side}','center':rounded(S.expand_complex(c)),
                'type':'U_retained_double','u_index':k,'expected_exponent':2})
 for k,v in enumerate(u[1:],1):
  for l,w in enumerate(u[1:],1):
   if k==l or k+l==5:continue
   c=rounded(S.expand_complex(1+(v-1)/(w-1)))
   rows.append({'name':f'other_triple_{k}_{l}','center':c,'type':'U_U_retained_triple',
                'u_indices':[k,l],'expected_exponent':6})
 assert len(rows)==25
 known=[S.Integer(1),S.Integer(2)]+[1-v for v in u[1:]]
 centers=known+[r['center'] for r in rows]
 for a,b in itertools.combinations(centers,2):assert norm2(a-b)>Q(1,10000)
 return rows

def run():
 rows=make_centers();base=I/100;h=Q(1,1000);out=[];cache={};started=time.monotonic()
 center_data=[]
 for row in rows:
  c=row['center'];center_data.append({k:v for k,v in row.items() if k!='center'}|{'center':[str(S.re(c)),str(S.im(c))]})
 (HERE/'remaining_pencil_centers.json').write_text(json.dumps({'coefficient_center_error_upper_bound':'1/10^25',
   'minimum_distinct_center_distance_lower_bound':'1/100','loops':center_data},indent=2)+'\n')
 for row in rows:
  name=row['name'];c=row['center'];corners=[c+h+h*I,c-h+h*I,c-h-h*I,c+h-h*I,c+h+h*I]
  path=[base]+corners;forward=[];records=[]
  for a,b in zip(path,path[1:]):
   key=(a,b)
   if key not in cache:
    rec=Segment(a,b,parameter_bound=10).compute();cache[key]=rec
    print('segment',len(cache),'crossings',rec['crossing_count'],'elapsed',round(time.monotonic()-started,2),flush=True)
   rec=cache[key];records.append(rec);forward+=rec['word']
  word=red(forward+invert(records[0]['word']))
  assert sum(1 if x>0 else -1 for x in word)==row['expected_exponent'],('unexpected exponent',name)
  perm=list(range(20))
  for x in word:perm[abs(x)-1],perm[abs(x)]=perm[abs(x)],perm[abs(x)-1]
  moved=[i for i in range(20) if perm[i]!=i]
  assert len(moved)==(2 if row['type']=='retained_half_twist' else 0),(name,perm)
  rec={k:v for k,v in row.items() if k!='center'}|{'center':[str(S.re(c)),str(S.im(c))],
       'word':word,'permutation':perm,'forward_segments':records}
  out.append(rec)
  (HERE/'remaining_pencil_braids.partial.json').write_text(json.dumps({'loops':out},separators=(',',':'))+'\n')
  print('loop',name,'length',len(word),'exponent',row['expected_exponent'],'elapsed',round(time.monotonic()-started,2),flush=True)
 result={'description':__doc__,'base':['0','1/100'],'rotation':['1','371/1000'],
   'initial_order':Segment(base,base+Q(1,10**7)).order(F(0)),'loops':out,'segment_count':len(cache),
   'parameter_L1_bound':'10','point_modulus_bound':'50','actual_coefficient_homotopy_motion_upper_bound':'1/10^22',
   'actual_segment_pair_separation_lower_bound':'1/10^14'}
 (HERE/'remaining_pencil_braids.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
 (HERE/'remaining_pencil_words.json').write_text(json.dumps({k:v for k,v in result.items() if k!='loops'}|
   {'loops':[{k:v for k,v in r.items() if k!='forward_segments'} for r in out]},indent=2)+'\n')
 print('PASS: remaining25 actual critical lassos, with8 half twists and17 pure local braids.',flush=True)

if __name__=='__main__':run()
