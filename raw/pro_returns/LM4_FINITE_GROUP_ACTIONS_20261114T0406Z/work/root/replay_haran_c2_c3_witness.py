#!/usr/bin/env python3
"""Unchanged isolated root replay of the frozen Haran finite witness."""
from pathlib import Path
from hashlib import sha256
import datetime,json,subprocess,sys

ROOT=Path(__file__).resolve().parents[2]
def binding(p):
    raw=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
source=ROOT/'work/part_d_attack/code/haran_c2_c3_marked_subgroup_witness.py'
author=source.with_name('haran_c2_c3_marked_subgroup_witness_output.json')
author_stdout=source.with_name('haran_c2_c3_marked_subgroup_witness_stdout.txt')
assert binding(source)['sha256']=='5b84d0a79f60e5533aa8673906da23f4e03aaf3e4877d788323b8f6b5a2779c6'
assert binding(author)['sha256']==binding(author_stdout)['sha256']=='612e55e5d4ed6e37bc97e18b5dbe530b81a7cd5a14d34c66d08830bc6c46a57f'
folder=ROOT/'work/root/haran_c2_c3_independent_replay'
assert not folder.exists()
folder.mkdir()
copied=folder/source.name
copied.write_bytes(source.read_bytes())
proc=subprocess.run([sys.executable,str(copied)],cwd=folder,capture_output=True)
stdout,stderr=folder/'stdout.txt',folder/'stderr.txt'
stdout.write_bytes(proc.stdout);stderr.write_bytes(proc.stderr)
assert proc.returncode==0 and not proc.stderr
output=folder/author.name
assert copied.read_bytes()==source.read_bytes()
assert output.read_bytes()==stdout.read_bytes()==author.read_bytes()==author_stdout.read_bytes()
d=json.loads(output.read_text())
assert d['status']=='PASS' and d['named_check_count']==11 and len(d['checks'])==11
assert all(x['status']=='PASS' for x in d['checks'])
assert d['S3_conjugator_pair_cases']==36 and d['proper_image_order']==6
assert d['proper_image_fixed_point']==3 and d['J_star_inversion_defect_image']==[3,4,1,2]
result={'status':'PASS_UNCHANGED_ISOLATED_ROOT_REPLAY','executed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'command':[sys.executable,str(copied)],'cwd':str(folder),'exit_code':0,
 'bindings':[binding(p) for p in [source,copied,author,author_stdout,output,stdout,stderr]],
 'source_copy_whole_bytes_identical':True,'all_four_output_and_stdout_whole_bytes_identical':True,
 'forward_output_transport':'Identity on the complete byte string.','inverse_output_transport':'Identity on the complete byte string.',
 'named_checks':11,'S3_conjugator_pairs':36,'proper_S4_image_order':6,'proper_image_fixed_point':3,
 'literal_J_star_defect':[3,4,1,2],
 'scope':'Actual S4/S3 generator words and full finite enumeration. No computation of a minimal closed subgroup or of nonstandard original h,j,kappa is asserted.'}
target=folder/'comparison.json'
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks':11,'pairs':36,'comparison':binding(target)},indent=2))
