#!/usr/bin/env python3
"""Independent exact expansion and original GAP replay of the G26 mod9 proof.

No searched Hermite basis is loaded.  The entire small arithmetic DAG is
expanded into original leaves, all diagonal eliminations use explicit Bezout
combinations of original power identities, and every used source leaf is
recomputed with GAP's original collector.  This certifies only the
three-primary component; C31 still needs its two-primary component.
"""
from pathlib import Path
from collections import defaultdict
import ast, gzip, hashlib, json, math, subprocess, time
from pbc_source_coordinate_bounds import coordinate_bounds, extended_gcd

CODE=Path(__file__).resolve().parent
WORK=CODE.parents[1]
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
compact=lambda x:json.dumps(x,separators=(',',':'))
source=CODE/'pbc_quotient26_original_source.json'
trace=CODE/'pbc_quotient26_primary9_trace.jsonl.gz'
original=CODE/'pbc_iterated_shortcut_v2_original_source.json'
homology=CODE/'pbc_three_h2_layer_bound.json'
s=json.loads(source.read_text());o=json.loads(original.read_text())
h=json.loads(homology.read_text());start=time.time()
assert h['status']=='PASS' and h['full_three_primary_annihilator']==9
assert h['original_source_sha256']==sha(original)==s['quotient_of_sha256']
assert s['homology_comparison_certificate_sha256']==sha(homology)
assert len(s['relative_orders'])==26
def trunc(w): return [a for i,e in zip(w[::2],w[1::2]) if i<=26 for a in(i,e)]
assert s['relative_orders']==o['relative_orders'][:26]
assert s['powers']==[trunc(w) for w in o['powers'][:26]]
assert s['conjugates']==[[i,j,trunc(w)] for i,j,w in o['conjugates'] if i<=26]
for k in ('s','r','f','left_s_frame','left_r_frame','s_image','r_image'):
    assert s[k]==trunc(o[k])
for k in ('s_centralizers','r_centralizers'):
    assert s[k]==[trunc(w) for w in o[k]]
M=9;n=26;width=n*(n+1)//2;sc=len(s['s_centralizers'])
old_bounds,bound_proofs=coordinate_bounds(s)
coordinates=[math.gcd(d,M) for d in old_bounds]
nodes=[None];source_header=None;success=None
for line in gzip.open(trace,'rt'):
    assert line.endswith('\n')
    r=json.loads(line);kind=r[0]
    if kind=='source':
        assert source_header is None and len(nodes)==1
        assert r==['source',sha(source),n,width,M,coordinates]
        source_header=r;continue
    if kind=='success':
        assert success is None and source_header is not None
        success=r;continue
    assert success is None and source_header is not None
    assert kind in ('leaf','sub','neg','mul') and r[1]==len(nodes)
    if kind=='leaf':
        v=r[4];assert len(v)%2==0 and v[::2]==sorted(set(v[::2]))
        assert all(1<=i<=width for i in v[::2])
        assert all(isinstance(c,int) and c for c in v[1::2])
        if r[2]=='modulus': assert v==[r[3][0],M]
        elif r[2]=='coordinate':
            i=r[3][0];assert i in bound_proofs and v==[i,coordinates[i-1]]
        elif r[2]=='extra': assert sc+3<=r[3][0]<=sc+11
        else: assert r[2] in ('target','identity')
    elif kind=='sub': assert 1<=r[2]<r[1] and 1<=r[4]<r[1] and isinstance(r[3],int)
    elif kind=='neg': assert 1<=r[2]<r[1]
    else: assert 1<=r[3]<r[1] and math.gcd(r[2],M)==1
    nodes.append(r)
assert success is not None and 1<=success[1]<len(nodes)
c=[0]*len(nodes);c[success[1]]=1;used=[]
for i in range(len(nodes)-1,0,-1):
    a=c[i]
    if not a:continue
    r=nodes[i]
    if r[0]=='leaf':used.append((i,a))
    elif r[0]=='sub':c[r[2]]=(c[r[2]]+a)%M;c[r[4]]=(c[r[4]]-a*r[3])%M
    elif r[0]=='neg':c[r[2]]=(c[r[2]]-a)%M
    else:c[r[3]]=(c[r[3]]+a*r[2])%M
used.sort();total=defaultdict(int);target_coefficient=0;extras=defaultdict(int)
leaves=[];used_bounds=set();identity_count=0
for i,a in used:
    r=nodes[i]
    for k,v in zip(r[4][::2],r[4][1::2]):total[k]+=a*v
    if r[2]=='target':target_coefficient+=a;leaves.append(r)
    elif r[2]=='extra':extras[r[3][0]]+=a;leaves.append(r)
    elif r[2]=='identity':leaves.append(r);identity_count+=1
    elif r[2]=='coordinate':used_bounds.add(r[3][0])
    else:assert r[2]=='modulus'
assert target_coefficient==1
assert all(v%coordinates[i-1]==0 for i,v in total.items())
used_bounds.update(i for i,v in total.items() if v and coordinates[i-1]<M)
corrected=dict(total);diagonal=[];next_id=-1
for i in sorted(used_bounds):
    proof=bound_proofs[i];d=proof['bound'];g,a,b=extended_gcd(d,M)
    assert g==coordinates[i-1] and a*d+b*M==g
    assert sum(r['coefficient']*r['value'] for r in proof['rows'])==d
    multiplier=(total[i]//g)*a
    corrected[i]=total[i]-multiplier*d
    assert corrected[i]%M==0
    diagonal.append(dict(index=i,original_bound=d,reduced_bound=g,
                         bezout=[a,b],source_multiplier=multiplier,original_rows=proof['rows']))
    for r in proof['rows']:
        leaves.append(['leaf',next_id,'identity',r['meta'],[i,r['value']]])
        next_id-=1
assert all(v%M==0 for v in corrected.values())
returned=success[2]
assert len(returned)==82 and all(v==0 for v in returned)
assert extras[1]==extras[2]==0
assert all(v%3==0 for i,v in extras.items())
assert all(i>=sc+3 for i,v in extras.items() if v)

# The independent GAP collector is copied by AST extraction from the retained
# original-source replay routine, not from the search or its processed rows.
replay_source=CODE/'pbc_replay_source_rows.py';body=None
for node in ast.parse(replay_source.read_text()).body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='body' for t in node.targets):
        assert body is None;body=ast.literal_eval(node.value)
assert isinstance(body,str) and 'PBC_Replay:=function' in body
con=[[] for _ in range(n)]
for i,j,w in s['conjugates']:
    assert len(con[i-1])==j-1;con[i-1].append(w)
data=dict(orders=s['relative_orders'],powers=s['powers'],conjugates=con,
          s=s['s'],r=s['r'],bs=s['left_s_frame'],br=s['left_r_frame'],
          cs=s['s_centralizers'],cr=s['r_centralizers'],
          s_image=s['s_image'],r_image=s['r_image'])
gap=CODE/'pbc_quotient26_primary9_original_replay.g'
gap.write_text('LoadPackage("polycyclic");;\n'+body+'\nPBC_data:=rec('
               +','.join(k+':='+compact(v) for k,v in data.items())+');;\n'
               +'PBC_leaves:='+compact(leaves)+';;\n'
               +'Assert(0,PBC_Replay(PBC_data,PBC_leaves));\nQUIT;\n')
output=CODE/'pbc_quotient26_primary9_original_replay.out'
gap_exe=WORK/'gap-runtime/gap-4.16.1/gap'
command=[str(gap_exe),'-q','-m','128m','-o','1g',str(gap)]
with output.open('w') as out:proc=subprocess.run(command,stdout=out,stderr=subprocess.STDOUT)
assert proc.returncode==0
text=output.read_text()
assert f'original_source_identity_replay_verified {len(leaves)} leaves' in text
assert 'mismatched_leaf' not in text and 'Error,' not in text
report=dict(status='PASS: exact DAG expansion and every used ORIGINAL source leaf replayed',
            source_sha256=sha(source),original_source_sha256=sha(original),
            homology_certificate_sha256=sha(homology),trace_sha256=sha(trace),
            verifier_sha256=sha(__file__),primary_modulus=M,dag_nodes=len(nodes)-1,
            source_header=source_header,nonzero_leaf_coefficients=used,
            used_identity_leaves=identity_count,all_original_leaves_replayed=len(leaves),
            exact_integer_diagonal_eliminations=diagonal,
            integer_residual_divisible_by9=True,
            integer_residual_over9=[[i,v//M] for i,v in sorted(corrected.items()) if v],
            target_coefficient=target_coefficient,
            used_extra_coefficients=[[i,v] for i,v in sorted(extras.items()) if v],
            all_genuine_r_frame_coefficients_zero_mod3=True,
            forbidden_power_and_s_frame_coefficients_zero=True,
            actual_target_has_free_abelianization_zero='The three defining differences telescope exactly in the free-source abelianization.',
            conclusion='The original target has zero three-primary component, by the actual H2(G176,Z3) -> H2(G26,Z3) isomorphism and the exponent9 bound.',
            scope='Only the three-primary component. C31 remains Open until the independent two-primary component is proved.',
            gap_command=command,gap_source_sha256=sha(gap),gap_output_sha256=sha(output),
            original_replay_routine_sha256=sha(replay_source),seconds=time.time()-start)
dest=CODE/'pbc_quotient26_primary9_verified.json'
dest.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('status','primary_modulus','dag_nodes','used_identity_leaves',
      'all_original_leaves_replayed','target_coefficient','conclusion','scope','seconds')},indent=2))

