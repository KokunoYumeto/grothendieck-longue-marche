"""Scan all actual final-build logs, preserving transient-pass evidence."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse, hashlib, json, re

root=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
parser=argparse.ArgumentParser()
parser.add_argument('--passes',required=True)
parser.add_argument('--driver-prefix',default='records/checkpoint37_build_driver')
args=parser.parse_args()
passes=root/args.passes
assert passes.is_dir() and passes.parent==root/'records/build_passes'
m=json.loads((root/'records/checkpoint37_metrics.json').read_text())
render=json.loads((root/'records/pdf_qa/checkpoint37_final/render_manifest.json').read_text())
assert sha(root/'LM4_SUCCESSOR_paper.pdf')==m['pdf_sha256']==render['pdf_sha256']
assert m['pages']==render['page_count']
assert not m['overfull'] and not m['warnings'] and not m['errors']
files=sorted(passes.glob('build*.log'))
assert all((passes/('build_'+str(i)+'.log')).is_file() for i in range(4))
audits=[]
for path in [root/'LM4_SUCCESSOR_paper.log',*files]:
    content=path.read_text()
    warnings=[line for line in content.splitlines() if re.search(r'\bwarning\b',line,re.I)
              and not line.startswith(('Package:','File:'))]
    issues=[line for line in content.splitlines()
            if re.search(r'overfull|undefined|missing character|^!|fatal error|rerun to get',line,re.I)]
    audits.append(dict(path=str(path.relative_to(root)),bytes=path.stat().st_size,sha256=sha(path),
      warnings=warnings,issues=issues,underfull_notices=re.findall(r'^.*Underfull.*$',content,re.M),
      overfull=re.findall(r'^.*Overfull.*$',content,re.M),complete_file_scanned=True))
stabilized=sorted(passes.glob('build_stabilize_*.log'),key=lambda p:int(p.stem.rsplit('_',1)[1]))
last=stabilized[-1] if stabilized else passes/'build_3.log'
final=[audits[0],next(a for a in audits if a['path']==str(last.relative_to(root))) ]
assert all(not a['warnings'] and not a['issues'] for a in final)
assert Counter(final[0]['underfull_notices'])==Counter(final[1]['underfull_notices'])
baseline_path=root/'records/pdf_qa/checkpoint37_before_integration/LM4_SUCCESSOR_paper.log'
baseline=baseline_path.read_text()
old_underfull=re.findall(r'^.*Underfull.*$',baseline,re.M)
old_overfull=re.findall(r'^.*Overfull.*$',baseline,re.M)
out_path=root/(args.driver_prefix+'.out');err_path=root/(args.driver_prefix+'.err')
assert out_path.is_file() and err_path.is_file() and not err_path.read_bytes()
assert 'Build passes: no overflow greater than2pt and no undefined references.' in out_path.read_text()
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),result='PASS_FINAL_LOGS',
  final_pdf_sha256=m['pdf_sha256'],final_build_directory=str(passes.relative_to(root)),
  final_log_and_stdout_audits=final,all_final_build_pass_audits=audits,
  previous_overfull_count=len(old_overfull),previous_overfull_notices=old_overfull,
  final_overfull_count=len(final[0]['overfull']),final_underfull_count=len(final[0]['underfull_notices']),
  underfull_identical_to_checkpoint36=Counter(old_underfull)==Counter(final[0]['underfull_notices']),
  added_underfull_notices=list((Counter(final[0]['underfull_notices'])-Counter(old_underfull)).elements()),
  removed_underfull_notices=list((Counter(old_underfull)-Counter(final[0]['underfull_notices'])).elements()),
  baseline_log=dict(path=str(baseline_path.relative_to(root)),sha256=sha(baseline_path)),
  driver_files=[dict(path=str(p.relative_to(root)),bytes=p.stat().st_size,sha256=sha(p)) for p in (out_path,err_path)],
  scope='Every byte of the final engine log and all actual stdout files from this build directory was scanned case-insensitively. Final engine and last completed stdout are clean. Transient preceding-pass issues remain recorded. Actual image inspection is separate. Tool exit observation is separate.')
with (root/'records/checkpoint37_final_pdf_audit.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print(json.dumps({k:record[k] for k in ['result','final_pdf_sha256','final_build_directory','previous_overfull_count','final_overfull_count','final_underfull_count','underfull_identical_to_checkpoint36','added_underfull_notices','removed_underfull_notices']},indent=2))
