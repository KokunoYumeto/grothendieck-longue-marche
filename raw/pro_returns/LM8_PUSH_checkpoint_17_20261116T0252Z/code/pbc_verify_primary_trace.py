# PRIMARY COMPONENT ONLY: this modulus does not kill the other torsion component.
# Every reduced coordinate bound uses an explicit original-row/constant-modulus
# Bezout identity. Both components and source-row replay remain mandatory.
#!/usr/bin/env python3
"""Expand a bounded-modulus DAG independently in external memory.

No Hermite basis is read. Every arithmetic node is checked and expanded into
the ORIGINAL source leaves. Proper coordinate eliminations are rederived
from original power identities. Replaying every used source leaf is a
separate mandatory gate. An annihilator input invokes the separately proved
integral Hopf-torsion comparison, never a finite-cover approximation.
"""
from collections import defaultdict
from pathlib import Path
from pbc_source_coordinate_bounds import coordinate_bounds,extended_gcd
import argparse,gzip,hashlib,json,math,mmap,struct,sys,tempfile,time
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ap=argparse.ArgumentParser()
ap.add_argument('source',type=Path);ap.add_argument('trace',type=Path)
ap.add_argument('--s-count',type=int,required=True)
ap.add_argument('--annihilator',type=Path,required=True)
ap.add_argument('--prime',type=int,choices=[2,3],required=True)
ap.add_argument('--out',type=Path,required=True)
args=ap.parse_args();started=time.time()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
raw=json.loads(args.source.read_text());source_hash=sha(args.source)
assert args.s_count==len(raw['s_centralizers'])
N=math.prod(raw['relative_orders']);M=N;annihilator=None
if args.annihilator:
 a=json.loads(args.annihilator.read_text())
 provenance=args.annihilator.with_name(args.annihilator.stem+'_provenance.json')
 pr=json.loads(provenance.read_text());assert pr['original_source_sha256']==source_hash
 assert a['group_order']==N and a['derived_orders'][0]==N and a['derived_orders'][-1]==1
 assert [math.lcm(*v) for v in a['abelian_invariants']]==a['factor_exponents']
 assert [a['derived_orders'][i]//a['derived_orders'][i+1] for i in range(len(a['derived_orders'])-1)]==[math.prod(v) for v in a['abelian_invariants']]
 M=math.prod(v*v for v in a['factor_exponents']);assert M==a['bound'] and N%M==0
 annihilator={'path':str(args.annihilator),'sha256':sha(args.annihilator),
  'provenance_sha256':sha(provenance),'factor_exponents':a['factor_exponents'],
  'comparison':'notes/pbc_C31_small_annihilator.md',
  'arithmetic_scope':'The actual derived series and its abelian factors were computed in the separately executed original-group GAP certificate.'}
global_annihilator=M
M=1;remaining=global_annihilator
while remaining%args.prime==0:M*=args.prime;remaining//=args.prime
assert M>1 and global_annihilator%M==0
annihilator['global_homology_annihilator']=global_annihilator
annihilator['primary_modulus']=M;annihilator['prime']=args.prime
assert 1<M<2**64 and sys.byteorder=='little'
original_coordinates,bound_proofs=coordinate_bounds(raw)
coordinates=[math.gcd(d,M) for d in original_coordinates]
assert all(d>0 and M%d==0 for d in coordinates)
n=len(raw['relative_orders']);width=n*(n+1)//2
coefficient_type='I' if M<2**32 else 'Q'
coefficient_bytes=4 if M<2**32 else 8
record=struct.Struct('<B3xIQQQ' if M<2**32 else '<B7xQQQQ')
trace_hash=sha(args.trace);trace_open=gzip.open if args.trace.suffix=='.gz' else open
parent=Path(__file__).resolve().parents[2]/'pbc_proof_workspace';parent.mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(prefix='smallmod_dag_',dir=parent) as tmp:
 tmp=Path(tmp);nodefile=tmp/'nodes.bin';leaffile=tmp/'leaves.jsonl';count=0;source=success=None
 with nodefile.open('wb') as nodes,leaffile.open('wb') as leaves,trace_open(args.trace,'rb') as inp:
  nodes.write(bytes(record.size))
  for line_number,line in enumerate(inp,1):
   assert line.endswith(b'\n');row=json.loads(line);kind=row[0]
   if kind=='source':
    assert source is None and count==0
    assert row==['source',source_hash,n,width,M,coordinates];source=row;continue
   if kind=='success':
    assert success is None and source is not None;success=row;continue
   assert source is not None and success is None
   assert kind in ('leaf','sub','neg','mul') and row[1]==count+1
   count+=1
   if kind=='leaf':
    vector=row[4];assert len(vector)%2==0
    assert vector[::2]==sorted(set(vector[::2]))
    assert all(1<=i<=width for i in vector[::2])
    assert all(isinstance(c,int) and c for c in vector[1::2])
    if row[2]=='modulus':assert len(row[3])==1 and vector==[row[3][0],M]
    elif row[2]=='coordinate':
     assert len(row[3])==1 and row[3][0] in bound_proofs
     assert vector==[row[3][0],coordinates[row[3][0]-1]]
    elif row[2]=='extra':
     idx=row[3][0];assert idx>=3,'Power-word correction forbidden'
     assert (idx<=args.s_count+2)==(args.prime==2),'Wrong-primary frame correction forbidden' 
    else:assert row[2] in ('target','identity')
    offset=leaves.tell();leaves.write(line);nodes.write(record.pack(0,0,0,0,offset))
   elif kind=='sub':
    assert 1<=row[2]<count and 1<=row[4]<count and isinstance(row[3],int)
    nodes.write(record.pack(1,row[3]%M,row[2],row[4],0))
   elif kind=='neg':
    assert 1<=row[2]<count;nodes.write(record.pack(2,0,row[2],0,0))
   else:
    assert 1<=row[3]<count and math.gcd(row[2],M)==1
    nodes.write(record.pack(3,row[2]%M,row[3],0,0))
   if count%2000000==0:print(json.dumps({'phase':'parse','nodes':count,'seconds':time.time()-started}),flush=True)
 assert source is not None and success is not None and 1<=success[1]<=count
 coefficients=tmp/'coefficients.bin'
 with coefficients.open('w+b') as cf,nodefile.open('rb') as nf:
  cf.truncate(coefficient_bytes*(count+1))
  with mmap.mmap(cf.fileno(),0) as cm,mmap.mmap(nf.fileno(),0,access=mmap.ACCESS_READ) as nm:
   c=memoryview(cm).cast(coefficient_type);c[success[1]]=1;used=[]
   for node_id in range(count,0,-1):
    coefficient=c[node_id]
    if not coefficient:continue
    c[node_id]=0;kind,q,a,b,offset=record.unpack_from(nm,node_id*record.size)
    if kind==1:c[a]=(c[a]+coefficient)%M;c[b]=(c[b]-coefficient*q)%M
    elif kind==2:c[a]=(c[a]-coefficient)%M
    elif kind==3:c[a]=(c[a]+coefficient*q)%M
    else:assert kind==0;used.append((node_id,coefficient,offset))
   assert c[0]==0;c.release()
 total=defaultdict(int);target_coefficient=0;extra_coefficients=defaultdict(int)
 identities=[];source_leaves=[];modulus_leaves=0;used_bounds=set()
 with leaffile.open('rb') as leaves:
  for node_id,coefficient,offset in sorted(used):
   leaves.seek(offset);row=json.loads(leaves.readline());assert row[0]=='leaf' and row[1]==node_id
   for index,value in zip(row[4][::2],row[4][1::2]):total[index]+=coefficient*value
   if row[2]=='target':target_coefficient+=coefficient;source_leaves.append(node_id)
   elif row[2]=='extra':extra_coefficients[row[3][0]]+=coefficient;source_leaves.append(node_id)
   elif row[2]=='identity':identities.append([node_id,coefficient,row[3]]);source_leaves.append(node_id)
   elif row[2]=='coordinate':used_bounds.add(row[3][0])
   else:assert row[2]=='modulus';modulus_leaves+=1
 assert target_coefficient==1
 assert all(value%coordinates[i-1]==0 for i,value in total.items())
 for i,value in total.items():
  if value and coordinates[i-1]<M:used_bounds.add(i)
 proofs={}
 for i in sorted(used_bounds):
  original=bound_proofs[i];d=original['bound'];g,a,b=extended_gcd(d,M)
  assert g==coordinates[i-1] and a*d+b*M==g
  proofs[i]=dict(original,reduced_bound=g,bezout_source_coefficient=a,bezout_modulus_coefficient=b)
 eliminations=[[i,(total[i]//coordinates[i-1])*proofs[i]['bezout_source_coefficient']] for i in sorted(used_bounds) if total[i]]
 corrected=dict(total)
 for i,multiple in eliminations:
  correction=multiple*sum(r['coefficient']*r['value'] for r in proofs[i]['rows'])
  assert (total[i]-correction)%M==0;corrected[i]-=correction
 assert all(value%M==0 for value in corrected.values())
 returned=success[2];assert returned[:2]==[0,0]
 assert all(v==0 for i,v in enumerate(returned,1) if i>=3 and ((i<=args.s_count+2)!=(args.prime==2)))
 assert extra_coefficients[1]==extra_coefficients[2]==0
 for i,value in enumerate(returned,1):
  c=extra_coefficients[i]
  if i<=2:assert c==value==0
  else:assert (c-value)%(2 if i<=args.s_count+2 else 3)==0
 cert={'verified_original_modular_identity':True,'original_integer_residual_divisible_by_modulus':True,
  'source_header':source,'modulus':M,'group_order':N,'annihilator_certificate':annihilator,
  'primary_component_only':True,'prime':args.prime,'global_homology_annihilator':global_annihilator,'other_primary_component_still_required':True,
  'source_sha256':source_hash,'trace_sha256':trace_hash,'trace_is_gzip':args.trace.suffix=='.gz',
  'dag_nodes':count,'nonzero_leaf_coefficients':[[i,c] for i,c,o in sorted(used)],
  'used_original_source_leaf_ids':source_leaves,'used_source_identities':identities,
  'used_modulus_leaves':modulus_leaves,'target_coefficient':target_coefficient,
  'forbidden_power_word_coefficients':[0,0],
  'extra_coefficients_mod_N':[extra_coefficients[i]%M for i in range(1,len(returned)+1)],
  'extra_coefficients_modulus':M,'returned_boundary_coefficients':returned,
  'integer_modulus_quotient':[[i,v//M] for i,v in sorted(corrected.items()) if v],
  'coordinate_bound_proofs':proofs,'coordinate_eliminations':eliminations,
  'coordinate_moduli':coordinates,'original_coordinate_power_relations_checked':True,
  'label_reduction_verified':True,'source_identity_replay_still_required':True,
  'hopf_torsion_faithfulness_comparison':'notes/pbc_C31_primary_split_gate.md; no integral conclusion from one component',
  'external_memory_scratch':'Only temporary indexed copies of the retained exact DAG; no new source relations or numerical approximations.',
  'verifier_source_sha256':sha(Path(__file__)),'seconds':time.time()-started}
 args.out.write_text(json.dumps(cert,indent=2)+'\n')
 print(json.dumps({k:cert[k] for k in ['verified_original_modular_identity','modulus','group_order','dag_nodes','target_coefficient','forbidden_power_word_coefficients','source_identity_replay_still_required','seconds']},indent=2),flush=True)
 print('used_original_source_leaves',len(source_leaves),'used_source_identities',len(identities),flush=True)
