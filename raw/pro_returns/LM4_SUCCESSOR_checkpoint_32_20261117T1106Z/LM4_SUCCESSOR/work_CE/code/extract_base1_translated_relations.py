"""The exact first retained-base translates of the special node and pair4."""
from pathlib import Path
import sys,json,hashlib
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2];CE=ROOT/'work_CE';DE=ROOT/'work_DE/next_marginal_source'
sys.path.insert(0,str(DE));p=DE/'reduce_other_triples_hnn.py'
ns={'__file__':str(p)};exec(compile(p.read_text().split('rows=[]',1)[0],str(p),'exec'),ns)
art,mul,iv,sub,britton,new=(ns[k] for k in ('art','mul','iv','sub','britton','new'))
P=DE/'ratio_pencil_braids.json';D=json.loads(P.read_text());row=next(r for r in D['loops'] if r['name']=='base1');A=art(row['word'])
Ainv=art(iv(row['word']))
for i in range(1,21):assert sub(A[i],Ainv)==(i,)==sub(Ainv[i],A)
c=sub(mul(A[10],A[11]),new);b=sub(A[11],new)
j=0
while len(b)-2*j>1 and b[j]==-b[-j-1]:j+=1
h=b[:j];assert b[j:len(b)-j]==(11,) and all(abs(x)!=11 for x in h)
d=mul(iv(h),c,h);node=mul(d,(11,),iv(d),(-11,));node_reduced,node_steps=britton(node)
q=mul(iv(h),sub(A[9],new),h);p4=mul(iv(h),sub(A[15],new),h)
p4red,p4steps=britton(p4)
L=(10,12,13,14,15,16,17,18,19,20)
expected=mul((11,),iv(h),(-11,),L,(-11,10),iv(L),(11,),h)
assert d==expected
out={'scope':'Exact full-presentation consequences obtained by translating already imposed relations by retained base1; no subgroup-normality conclusion.',
 'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'base1_word':row['word'],
 'base1_b_transporter_h':h,'base1_c_normalized_d':d,'right_cluster_word_L':L,
 'translated_node_commutator':node,'translated_node_partial_HNN_result':node_reduced,'translated_node_steps':node_steps,
 'translated_pair4_P':p4,'translated_pair4_P_partial_HNN_result':p4red,'translated_pair4_P_steps':p4steps,
 'translated_pair4_Q':q}
(CE/'base1_translated_relations.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact inverse Artin action and literal special-basis conversion.')
print('h=',h)
print('d=b*h^-1*b^-1*L*b^-1*c*L^-1*b*h, L=',L)
print('The translated special-node relation is [d,b]=1.')
print('Node partial-HNN result length',len(node_reduced),'b letters',sum(abs(x)==11 for x in node_reduced))
print('Normalized translated pair4 Q=',q)
print('Normalized translated pair4 P has length',len(p4red),'and b letters',sum(abs(x)==11 for x in p4red))
print('LIMIT: the translated P is not reduced into H by the current rank17 edge rules; pair normalization cannot yet be asserted on two H words.')
