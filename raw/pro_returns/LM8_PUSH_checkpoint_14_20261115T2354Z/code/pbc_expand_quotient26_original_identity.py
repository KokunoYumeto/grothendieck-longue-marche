#!/usr/bin/env python3
"""Make the G26 mod9 witness a literal integer combination of original rows.

Every coordinate/modulus leaf is REMOVED before forming the displayed sum.
The remaining coordinate-divisible residual is eliminated by explicit Bezout
multiples of genuine original power-consistency rows.  The final ledger has
only the target, genuine frame commutators, and original identity rows.
"""
from pathlib import Path
from collections import defaultdict
import ast,gzip,hashlib,json,math,subprocess,time
from pbc_source_coordinate_bounds import coordinate_bounds,extended_gcd
CODE=Path(__file__).resolve().parent;WORK=CODE.parents[1]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
compact=lambda v:json.dumps(v,separators=(',',':'))
source=CODE/'pbc_quotient26_original_source.json'
trace=CODE/'pbc_quotient26_primary9_trace.jsonl.gz'
verified=CODE/'pbc_quotient26_primary9_verified.json'
s=json.loads(source.read_text());v=json.loads(verified.read_text())
assert v['source_sha256']==sha(source) and v['trace_sha256']==sha(trace)
assert v['target_coefficient']==1 and v['integer_residual_divisible_by9']
co=dict(v['nonzero_leaf_coefficients']);M=9;n=26;width=351;start=time.time()
original_bounds,proofs=coordinate_bounds(s);bounds=[math.gcd(x,M) for x in original_bounds]
target=None;extra_rows={};identity_rows={};extra_coeff=defaultdict(int);identity_coeff=defaultdict(int)
removed=[]
for line in gzip.open(trace,'rt'):
    r=json.loads(line)
    if r[0]!='leaf' or r[1] not in co:continue
    c=co[r[1]];kind=r[2]
    if kind in ('coordinate','modulus'):
        removed.append([r[1],c,kind]);continue
    if kind=='target':assert target is None and c==1;target=r[4]
    elif kind=='extra':
        i=r[3][0];assert i>=74
        assert i not in extra_rows or extra_rows[i]==r[4]
        extra_rows[i]=r[4];extra_coeff[i]+=c
    else:
        assert kind=='identity';meta=tuple(r[3])
        assert meta not in identity_rows or identity_rows[meta]==r[4]
        identity_rows[meta]=r[4];identity_coeff[meta]+=c
assert target is not None
def add(total,coefficient,row):
    for i,a in zip(row[::2],row[1::2]):total[i]+=coefficient*a
literal=defaultdict(int);add(literal,1,target)
for i,c in extra_coeff.items():add(literal,c,extra_rows[i])
for meta,c in identity_coeff.items():add(literal,c,identity_rows[meta])
assert all(a%bounds[i-1]==0 for i,a in literal.items())
eliminations=[]
for i,a in sorted(literal.items()):
    if not a or bounds[i-1]==M:continue
    proof=proofs[i];d=proof['bound'];g,x,y=extended_gcd(d,M)
    assert g==bounds[i-1] and x*d+y*M==g
    multiplier=-(a//g)*x
    for r in proof['rows']:
        meta=tuple(r['meta']);row=[i,r['value']]
        assert meta not in identity_rows or identity_rows[meta]==row
        identity_rows[meta]=row;identity_coeff[meta]+=multiplier*r['coefficient']
    eliminations.append(dict(index=i,original_residual=a,original_bound=d,
        reduced_bound=g,bezout=[x,y],added_original_d_row_coefficient=multiplier))
final=defaultdict(int);add(final,1,target)
for i,c in extra_coeff.items():add(final,c,extra_rows[i])
for meta,c in identity_coeff.items():add(final,c,identity_rows[meta])
assert all(a%M==0 for a in final.values())
assert all(c%3==0 for c in extra_coeff.values())
ledger=[dict(meta=list(meta),coefficient=c,vector=identity_rows[meta])
        for meta,c in sorted(identity_coeff.items()) if c]
frames=[dict(original_extra_index=i,coefficient=c,vector=extra_rows[i])
        for i,c in sorted(extra_coeff.items()) if c]
# Independently recompute the literal final sum solely from the exported rows.
check=[0]*width
for row,c in [(target,1)]+[(r['vector'],r['coefficient']) for r in frames+ledger]:
    for i,a in zip(row[::2],row[1::2]):check[i-1]+=c*a
assert check==[final[i] for i in range(1,width+1)] and all(a%9==0 for a in check)
leaves=[['leaf',1,'target',[],target]]
for r in frames:leaves.append(['leaf',len(leaves)+1,'extra',[r['original_extra_index']],r['vector']])
for r in ledger:leaves.append(['leaf',len(leaves)+1,'identity',r['meta'],r['vector']])
old=CODE/'pbc_replay_source_rows.py';body=None
for node in ast.parse(old.read_text()).body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='body' for t in node.targets):body=ast.literal_eval(node.value)
assert isinstance(body,str)
con=[[] for _ in range(n)]
for i,j,w in s['conjugates']:assert len(con[i-1])==j-1;con[i-1].append(w)
data=dict(orders=s['relative_orders'],powers=s['powers'],conjugates=con,
          s=s['s'],r=s['r'],bs=s['left_s_frame'],br=s['left_r_frame'],
          cs=s['s_centralizers'],cr=s['r_centralizers'],s_image=s['s_image'],r_image=s['r_image'])
gap=CODE/'pbc_quotient26_literal_original_replay.g';out=gap.with_suffix('.out')
gap.write_text('LoadPackage("polycyclic");;\n'+body+'\nPBC_data:=rec('
               +','.join(k+':='+compact(x) for k,x in data.items())+');;\n'
               +'PBC_leaves:='+compact(leaves)+';;\nAssert(0,PBC_Replay(PBC_data,PBC_leaves));\nQUIT;\n')
cmd=[str(WORK/'gap-runtime/gap-4.16.1/gap'),'-q','-m','128m','-o','1g',str(gap)]
with out.open('w') as f:proc=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT)
assert proc.returncode==0 and f'original_source_identity_replay_verified {len(leaves)} leaves' in out.read_text()
assert 'mismatched_leaf' not in out.read_text() and 'Error,' not in out.read_text()
result=dict(status='PASS: literal integer combination of original rows, with independent GAP replay',
    source_sha256=sha(source),trace_sha256=sha(trace),earlier_expansion_sha256=sha(verified),
    generator_sha256=sha(__file__),modulus=9,target=dict(coefficient=1,vector=target),
    genuine_frame_rows=frames,original_identity_rows=ledger,
    removed_coordinate_and_modulus_leaves=removed,original_row_eliminations=eliminations,
    exact_integer_residual=check,exact_integer_residual_divided_by9=[a//9 for a in check],
    coordinate_or_modulus_rows_in_final_witness=False,
    original_rows_replayed=len(leaves),all_frame_coefficients_zero_mod3=True,
    forbidden_power_and_s_corrections_absent=True,
    gap_command=cmd,gap_program_sha256=sha(gap),gap_output_sha256=sha(out),
    seconds=time.time()-start,
    scope='Original three-primary target vanishes by the approved H2 comparison and annihilator9. The independent two-primary target remains Open.')
dest=CODE/'pbc_quotient26_literal_original_identity.json';dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('status','modulus','original_rows_replayed',
    'coordinate_or_modulus_rows_in_final_witness','all_frame_coefficients_zero_mod3','scope','seconds')},indent=2))
