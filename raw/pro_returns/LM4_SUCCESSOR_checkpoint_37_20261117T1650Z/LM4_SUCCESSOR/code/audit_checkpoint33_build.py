"""Read all current build logs, compare final notices, and bind the existing bibliography."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import hashlib,json,re,shutil
root=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
metrics=json.loads((root/'records/checkpoint33_metrics.json').read_text())
assert sha(root/'LM4_SUCCESSOR_paper.pdf')==metrics['pdf_sha256']
passes=root/'records/build_passes/20261117T112757717519Z'
assert passes.is_dir()
audits=[]
for path in [root/'LM4_SUCCESSOR_paper.log',*sorted(passes.glob('build*.log'))]:
    content=path.read_text()
    warnings=[line for line in content.splitlines() if re.search(r'\bwarning\b',line,re.I) and not line.startswith(('Package:','File:'))]
    issues=[line for line in content.splitlines() if re.search(r'overfull|undefined|missing character|^!|fatal error|rerun to get',line,re.I)]
    notices=re.findall(r'^.*Underfull.*$',content,re.M)
    overfull=re.findall(r'^.*Overfull.*$',content,re.M)
    audits.append(dict(path=str(path.relative_to(root)),sha256=sha(path),warnings=warnings,issues=issues,underfull_notices=notices,overfull=overfull))
final=[audits[0],next(a for a in audits if a['path'].endswith('/build_stabilize_0.log'))]
assert all(not a['warnings'] and not a['issues'] for a in final)
assert Counter(final[0]['underfull_notices'])==Counter(final[1]['underfull_notices'])
prior=json.loads((root/'records/checkpoint32_visual_review.json').read_text())['final_log_and_stdout_audits'][0]
assert Counter(prior['underfull_notices'])==Counter(final[0]['underfull_notices'])
assert len(final[0]['underfull_notices'])==19
assert all(not a['overfull'] for a in audits)
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),result='PASS',pdf_sha256=metrics['pdf_sha256'],
    all_current_build_log_audits=audits,final_log_and_stdout_audits=final,
    previous_overfull_count=0,first_current_pass_overfull_count=0,final_overfull_count=0,
    unchanged_underfull_count=19,
    scope='Every current build log read in full; intermediate reference-stabilization diagnostics retained. Final engine log and final stdout contain no warnings, overflow, missing glyph, undefined reference, or error. All19 underfull notices agree exactly with checkpoint32.')
target=root/'records/checkpoint33_build_audit.json'
assert not target.exists();target.write_text(json.dumps(record,indent=2)+'\n')
formal_path=root/'records/checkpoint33_root_formal_reviews.json'
backup=root/'records/pdf_qa/checkpoint33_before_integration/checkpoint33_root_formal_reviews_before_bibliography.json'
assert not backup.exists();shutil.copy2(formal_path,backup)
formal=json.loads(formal_path.read_text())
bib=root/'LM4_SUCCESSOR_references.bib'
assert bib.read_bytes()==(root/'records/pdf_qa/checkpoint33_before_integration/LM4_SUCCESSOR_references.bib').read_bytes()
formal['bibliography']=dict(path='LM4_SUCCESSOR_references.bib',sha256=sha(bib),entries=115,
    scope='Byte-identical consolidated bibliography before and after33; no new external reference was added by the seven statements.')
formal_path.write_text(json.dumps(formal,indent=2)+'\n')
print(json.dumps(dict(result='PASS',all_logs=len(audits),final_overfull=0,final_warning=0,final_error=0,unchanged_underfull=19,bibliography='unchanged115'),indent=2))
