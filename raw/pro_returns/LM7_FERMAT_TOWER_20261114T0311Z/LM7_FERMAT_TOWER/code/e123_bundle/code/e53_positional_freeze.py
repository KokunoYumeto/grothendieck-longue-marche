#!/usr/bin/env python3
"""Freeze E123 after exact replay, source-scope and actual image review."""
from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[1]
L=R/'ledger'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proof=R/'sections/E_fiftythree_positional_stable.tex'
text=proof.read_text()
assert text.count('\\begin{statement}{E.123}{Proved}')==1
assert text.count('\\begin{proof}')==text.count('\\end{proof}')==1
assert [int(x) for x in re.findall(r'\\tag\{E123\.(\d+)\}',text)]==list(range(1,27))
assert not [c for c in text if ord(c)<32 and c not in '\n\t\r']
replay=json.loads((R/'code/e53_positional_replay.json').read_text())
assert replay['status']=='PASS' and replay['excluded_fields']==[]
for name,h in replay['source_hashes'].items():assert sha(R/'code'/name)==h
visual=json.loads((L/'e_fiftythree_positional_visual_review.json').read_text())
assert visual['status']=='PASS' and visual['section_sha256']==sha(proof)
assert visual['PDF_sha256']==sha(R/'qa/e123_standalone.pdf')
for p in visual['images']:
    assert p['actually_viewed'] and sha(R/p['file'])==p['sha256']

programs=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or p.suffix not in ('.py','.gp'):continue
    rel=p.relative_to(R).as_posix()
    out=p.with_suffix('.out');err=p.with_suffix('.err')
    if rel=='code/e53_positional_freeze.py':
        programs.append({'source':rel,'source_sha256':sha(p),'stdout':'code/e53_positional_freeze.out',
            'scope':'This actual invocation; stdout is captured after manifest generation and excluded from the recursive manifest.'})
        continue
    assert out.exists(),rel
    assert out.stat().st_size or (err.exists() and err.stat().st_size),rel
    programs.append({'source':rel,'source_sha256':sha(p),'stdout':out.relative_to(R).as_posix(),
        'stdout_sha256':sha(out),'stderr':err.relative_to(R).as_posix() if err.exists() else None,
        'stderr_sha256':sha(err) if err.exists() else None,
        'scope':'Actual retained execution; the computation-status and amendment records distinguish successful, failed, stopped and replayed runs.'})
(L/'e_fiftythree_positional_program_outputs.json').write_text(json.dumps(programs,indent=2)+'\n')

excluded={'ledger/e_fiftythree_positional_manifest.json','code/e53_positional_freeze.out','code/e53_positional_freeze.err'}
files=[]
for p in sorted(R.rglob('*')):
    if p.is_file():
        rel=p.relative_to(R).as_posix()
        if rel in excluded or '__pycache__' in p.parts:continue
        files.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
inputs=[r for r in files if r['path'].startswith('inputs/')]
manifest={'statement':'E.123','status':'FROZEN','proof':proof.relative_to(R).as_posix(),
 'proof_sha256':sha(proof),'PDF':'qa/e123_standalone.pdf','PDF_sha256':sha(R/'qa/e123_standalone.pdf'),
 'owned_files':files,'immutable_inputs':inputs,'excluded_recursive_outputs':sorted(excluded),
 'program_output_registry':'ledger/e_fiftythree_positional_program_outputs.json',
 'full_replay':'code/e53_positional_replay.json','visual_review':'ledger/e_fiftythree_positional_visual_review.json',
 'proof_review_scope':'Author complete; root draft review received. Final root and independent peer review are not claimed at this freeze.',
 'portable_replay':'In a fresh copy: python code/e53_positional_replay.py --gp /absolute/path/to/gp --label fresh_audit'}
mp=L/'e_fiftythree_positional_manifest.json'
mp.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':'FROZEN','statement':'E.123','owned_files':len(files),
 'programs_with_actual_outputs':len(programs),'immutable_input_files':len(inputs),
 'proof_sha256':sha(proof),'manifest_sha256':sha(mp),'PDF_sha256':sha(R/'qa/e123_standalone.pdf'),
 'full_replay_status':'PASS','actual_visual_review_pages':8},indent=2))
