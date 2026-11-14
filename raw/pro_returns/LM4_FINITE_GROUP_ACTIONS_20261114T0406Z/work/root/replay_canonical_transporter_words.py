#!/usr/bin/env python3
"""Unchanged isolated replay of the original canonical-transporter word checks."""
from pathlib import Path
from hashlib import sha256
import datetime,json,subprocess,sys

ROOT=Path(__file__).resolve().parents[2]
def binding(p):
    raw=p.read_bytes();return {'path':str(p.relative_to(ROOT)),'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
source=ROOT/'work/part_d_attack/code/actual_canonical_transporter_words.py'
author=source.with_name('actual_canonical_transporter_words_output.json')
author_stdout=source.with_name('actual_canonical_transporter_words_stdout.txt')
assert binding(source)['sha256']=='ee354569eedce861e104647f9a190af227ff3e28a133d417b853b2f6bdaf4c33'
assert binding(author)['sha256']==binding(author_stdout)['sha256']=='65806b2bd6cf34312ced05a162472182e3f44bdf3012ab062076925b7fc010a9'
folder=ROOT/'work/root/canonical_transporter_independent_replay'
assert not folder.exists();folder.mkdir()
copied=folder/source.name;copied.write_bytes(source.read_bytes())
proc=subprocess.run([sys.executable,str(copied)],cwd=folder,capture_output=True)
stdout,stderr=folder/'stdout.txt',folder/'stderr.txt'
stdout.write_bytes(proc.stdout);stderr.write_bytes(proc.stderr)
assert proc.returncode==0 and not proc.stderr
output=folder/author.name
assert output.read_bytes()==stdout.read_bytes()==author.read_bytes()==author_stdout.read_bytes()
d=json.loads(output.read_text())
assert d['status']=='PASS' and d['named_check_count']==20 and len(d['checks'])==20
assert all(x['status']=='PASS' for x in d['checks'])
assert d['universal_odd_exponent_cases']==17 and len(d['integral_branch_cases'])==19
assert [x['k'] for x in d['integral_branch_cases']]==list(range(-9,10))
record={'status':'PASS_UNCHANGED_ISOLATED_ROOT_CANONICAL_TRANSPORTER_REPLAY',
 'executed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,
 'command':[sys.executable,str(copied)],'cwd':str(folder),
 'bindings':[binding(p) for p in [source,copied,author,author_stdout,output,stdout,stderr]],
 'checker_whole_bytes_identical':copied.read_bytes()==source.read_bytes(),
 'all_four_output_and_stdout_whole_bytes_identical':True,
 'output_transport_both_directions':'Identity on the complete byte string.',
 'named_checks':20,'universal_odd_exponent_cases':17,'standard_integral_branch_cases':19,
 'scope':'Universal formal word identities and the original full standard input h=f=1. Formal symbols do not assign new nonstandard h values; the mathematical proof uses the retained original full centralizers and section classes.'}
target=folder/'comparison.json';target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'checks':20,'comparison':binding(target)},indent=2))
