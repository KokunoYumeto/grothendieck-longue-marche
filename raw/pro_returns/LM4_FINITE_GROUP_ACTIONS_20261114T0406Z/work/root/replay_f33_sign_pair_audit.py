#!/usr/bin/env python3
"""Execute the frozen independent F33 literal-word audit in an isolated mirror."""
from pathlib import Path
from hashlib import sha256
import json,subprocess,sys,datetime

ROOT=Path(__file__).resolve().parents[2]
original=ROOT/'work/part_a/code'
source=original/'affine_nonproduct_sign_pair_independent_audit.py'
author_output=source.with_name('affine_nonproduct_sign_pair_independent_audit_output.json')
author_stdout=source.with_name('affine_nonproduct_sign_pair_independent_audit_stdout.txt')
def binding(p):
    raw=p.read_bytes();return {'path':str(p.relative_to(ROOT)),'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
assert binding(source)['sha256']=='ce73e213189a8c63ca72d2c43c71d3caaac6cd7061736d598050bb1076cead0b'
assert binding(author_output)['sha256']=='07b92a66895988a539ba886a260883325f6fd1862b3ed499c22ac2a2d552c3bf'
data=json.loads(author_output.read_text())
folder=ROOT/'work/root/f33_independent_replay'
assert not folder.exists();folder.mkdir()
copies=[]
for row in data['input_bindings']:
    src=original/row['path'];dst=folder/row['path'];raw=src.read_bytes()
    assert len(raw)==row['bytes'] and sha256(raw).hexdigest()==row['sha256']
    dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(raw)
    assert dst.read_bytes()==raw
    copies.append({'original':binding(src),'copy':binding(dst),'whole_bytes_identical':True})
copied=folder/source.name;copied.write_bytes(source.read_bytes())
proc=subprocess.run([sys.executable,str(copied)],cwd=folder,capture_output=True)
stdout,stderr=folder/'stdout.txt',folder/'stderr.txt'
stdout.write_bytes(proc.stdout);stderr.write_bytes(proc.stderr)
assert proc.returncode==0 and not proc.stderr
output=folder/author_output.name
assert output.read_bytes()==author_output.read_bytes()
assert stdout.read_bytes()==author_stdout.read_bytes()
result=json.loads(output.read_text())
assert result['check_count']==252309 and result['literal_sources']==19 and result['original_source_rows']==64
assert [x['certified_rank'] for x in result['charts']]==[13]*4
record={'status':'PASS_UNCHANGED_ISOLATED_ROOT_F33_LITERAL_WORD_REPLAY',
 'executed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,
 'command':[sys.executable,str(copied)],'cwd':str(folder),
 'checker_original':binding(source),'checker_copy':binding(copied),'input_copies':copies,
 'author_output':binding(author_output),'output':binding(output),
 'author_stdout':binding(author_stdout),'stdout':binding(stdout),'stderr':binding(stderr),
 'raw_output_whole_bytes_identical':True,'raw_stdout_whole_bytes_identical':True,
 'output_transport_both_directions':'Identity on the complete mathematical output bytes; stdout identity is separately checked.',
 'checks':252309,'literal_negative_sources':19,'original_source_rows':64,'chart_ranks':[13]*4,
 'scope':'All nineteen actual negative braid words, decorations, eleven old actions, 64 actual seed/conjugate rows and the complete four-chart paired rank certificate. The standalone proof supplies the exact paired field and principal-line maps; the many-factor consequence is separate.'}
target=folder/'comparison.json';target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'checks':record['checks'],'comparison':binding(target)},indent=2))
