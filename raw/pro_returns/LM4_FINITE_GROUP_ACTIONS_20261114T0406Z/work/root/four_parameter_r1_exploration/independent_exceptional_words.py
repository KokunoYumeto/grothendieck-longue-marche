#!/usr/bin/env python3
"""Literal three-word verification of the exceptional nonsplitting certificate.

No four-parameter producer or algebra package is imported. The already
reviewed independent Laurent arithmetic evaluates the actual F23 words.
"""
from pathlib import Path
import hashlib,json,runpy
ROOT=Path(__file__).resolve().parents[3]
folder=Path(__file__).resolve().parent
arithmetic=ROOT/'work/part_a/code/affine_product_one_three_parameter_independent_audit.py'
ns=runpy.run_path(str(arithmetic))
g=ns['literal_braid'].__globals__
# Here the three formal axes mean original s,t,u, with original r=1.
g['CHARACTERS']=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(0,0,0),(0,0,0),(-1,-1,-1)]
parse=ns['parse'];MM=ns['matrix_mul'];MS=ns['matrix_sub'];SM=ns['scalar_mul'];I=ns['identity'];PM=ns['parse_matrix']
def specialize(poly):
 out={}
 for (a,b,d),coef in poly.items():
  exp=(0,0,b-a);value=coef*(-1 if d%2 else 1)
  out=ns['add'](out,{exp:value})
 return out
words=ROOT/'work/part_a/code/full_cross_source_stage/marginal_braids.json'
word_data=json.loads(words.read_text());records={x['index']:x for x in word_data['records']}
certificate=folder/'forced_lifts_output.json';cert=json.loads(certificate.read_text())
basis=PM(cert['basis']);inverse=PM(cert['inverse_basis'])
checks=[]
def check(name,value):
 assert value,name
 checks.append(name)
check('both_actual_basis_composites',MM(basis,inverse)==I(6) and MM(inverse,basis)==I(6))
section=I(6)+[[{} for _ in range(6)]];SJ=MM(section,basis)
delta=PM([['0'],['1/t-1'],['t-1'],['-2'],['0'],['0'],['-2']])
labels={1:'old_1_0',2:'old_1_1',7:'old_-1_1'};matrices={}
for index,label in labels.items():
 record=records[index];check('source_label_'+str(index),record['label']==label)
 _,A=ns['literal_braid'](record['negative_braid'])
 A=[[specialize(x) for x in row] for row in A]
 check('literal_principal_fixed_'+str(index),MM(A,delta)==delta)
 T=PM(cert['source_matrices'][str(index)]);matrices[index]=T
 lhs=MM(A,SJ);rhs=MM(SJ,T)
 check('cleared_actual_principal_quotient_'+str(index),SM(parse('-2'),MS(lhs,rhs))==MM(delta,[lhs[6]]))
vb=PM(cert['forced_boundary_lift']);vx=PM(cert['forced_X1_lift']);res=PM([['3*t-1'],['-2'],['0'],['0'],['0'],['0']])
check('boundary_forced_source_7',MM(matrices[7],vb)==SM(parse('1/t'),vb))
check('X1_forced_source_2',MM(matrices[2],vx)==SM(parse('1/t'),vx))
check('boundary_source_1_residual',MS(MM(matrices[1],vb),vb)==res)
check('X1_source_1_residual',MS(MM(matrices[1],vx),vx)==res)
for i,diagonal in [(2,['t','1/t','-t','-t']),(7,['1/t','t','-t','-t'])]:
 T=matrices[i]
 check('scalar_core_'+str(i),[row[:2] for row in T[:2]]==SM(parse('t'),I(2)))
 check('diagonal_quotient_'+str(i),all(not T[j][k] for j in range(2,6) for k in range(6) if j!=k))
 check('exact_quotient_values_'+str(i),[T[j][j] for j in range(2,6)]==[parse(x) for x in diagonal])
def bind(p):return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
out={'status':'PASS_LITERAL_EXCEPTIONAL_NONSPLITTING_CERTIFICATE','checks':checks,'check_count':len(checks),
 'literal_word_internal_checks':dict(g['CHECKS']),'source_indices_and_labels':labels,
 'coefficient_map':'Original r=1,s=t^-1,u=-1; a formal original (s,t,u) exponent (a,b,d) maps to (-1)^d*t^(b-a).',
 'principal_quotient_identity':'-2*(A*S*J-S*J*T)=delta*(row7(A*S*J)); -2 is invertible in the stated odd-characteristic stratum.',
 'residual':['3*t-1','-2','0','0','0','0'],
 'inputs':[bind(arithmetic),bind(words),bind(certificate)],
 'independence':'No producer or algebra package imports; actual three F23 braid words are evaluated over integer Laurent coefficients before exact specialization.',
 'scope':'The three source matrices and the forced-lift residual are proved integral identities. In characteristic odd and t outside Fp, the displayed source equations exclude both boundary and X1 eigenline lifts in this exceptional stratum. The full four-parameter theorem remains separately under review.'}
(folder/'independent_exceptional_words_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'checks':len(checks),'residual':['3*t-1','-2']},indent=2))
