"""Exact integer 2x2 calculations for local assertions on scan 123/016.
No image recognition or external mathematics library is involved.
"""
from pathlib import Path
import json
OUT=Path(__file__).resolve().parents[1]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
def neg(a):return [[-x for x in row] for row in a]
def scale(c,a):return [[c*x for x in row] for row in a]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def bracket(a,b):return add(mul(a,b),neg(mul(b,a)))
e=[[0,1],[0,0]];h=[[1,0],[0,-1]];f=[[0,0],[1,0]];zero=[[0,0],[0,0]];identity=[[1,0],[0,1]]
assert bracket(h,e)==scale(2,e)
assert bracket(h,f)==scale(-2,f)
assert bracket(e,f)==h
assert bracket(e,h)==scale(-2,e)
assert bracket(e,bracket(e,f))==scale(-2,e)
assert mul(e,e)==zero
exp_e=add(identity,e)
assert add(exp_e,neg(identity))==e
out={
 'arithmetic':'exact integers; conclusions interpreted over characteristic-zero fields',
 'matrices':{'e':e,'x=h':h,'f':f,'identity':identity},
 'brackets':{'[h,e]':bracket(h,e),'[h,f]':bracket(h,f),'[e,f]':bracket(e,f),'[e,h]':bracket(e,h),'ad(e)^2(f)':bracket(e,bracket(e,f))},
 'weight_spaces':'For ad(h), g(2)=span(e), g(0)=span(h), g(-2)=span(f); other nonzero weights are absent.',
 'b_minus_two_counterexample':'The identity Sl(2)->Sl(2) satisfies d) and gives x=h,e=e. Yet ad(e)(h)=-2e is nonzero in g(2), not in g(-2). Thus the written map in b) has the wrong target and the displayed equivalence fails literally.',
 'a_check':'For k=1 the source and target are zero; for k=2 the map f -> -2e is invertible; for k>=3 both spaces are zero. Thus a) holds in the same example.',
 'zero_exponential':{'e=0':zero,'exp(0)':identity,'claim_e_zero_iff_u_not_identity':'false; exp(0)=identity'},
 'nilpotent_example':{'e_squared':mul(e,e),'exp(e)=I+e':exp_e,'log(I+e)=e':add(exp_e,neg(identity))},
 'cancelled_bprime_conditional':'If the canceled variant reads bijectif with target g(2), use G=Sl(2)xSl(2), x=(h,0), e=(e,0). The nonzero element (0,h) has weight 0 and lies in ker ad(e), while ad(e)(h,0)=(-2e,0) spans g(2). Thus surjectivity holds but bijectivity need not. This does not assert why the author canceled the line.'
}
p=OUT/'math_checks/123_016_sl2_certificate.json';p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'certificate':str(p),'integer_bracket_assertions':'passed','claims_literally_refuted':['b) with target -2','e=0 i.e. u!=1']}))
