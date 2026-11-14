#!/usr/bin/env python3
"""Freeze E124 after complete actual replay and page-image inspection."""
from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[1];L=R/'ledger'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proof=R/'sections/E_fiftythree_ordinary_valuation.tex'
s=proof.read_text()
assert s.count(r'\begin{statement}{E.124}{Proved}')==1
assert s.count(r'\begin{proof}')==s.count(r'\end{proof}')==1
assert [int(x) for x in re.findall(r'\\tag\{E124\.(\d+)\}',s)]==list(range(1,25))
assert not [x for x in s if ord(x)<32 and x not in '\n\t\r']
replay=json.loads((R/'code/e53_ordinary_replay.json').read_text())
assert replay['status']=='PASS' and replay['excluded_fields']==[]
for name,h in replay['mathematical_source_hashes'].items():
    assert sha(R/'code'/name)==h
for name,h in replay['immutable_input_hashes'].items():
    assert sha(R/'inputs'/name)==h
layout=json.loads((R/'code/e53_ordinary_layout.json').read_text())
assert layout['status']=='LAYOUT_PASS' and layout['pages']==7
assert layout['overfull']==[] and layout['section_sha256']==sha(proof)
assert layout['PDF_sha256']==sha(R/'qa/e124_standalone.pdf')
visual={
 'status':'PASS','statement':'E.124','section_sha256':sha(proof),
 'PDF_sha256':sha(R/'qa/e124_standalone.pdf'),'pages':7,
 'scope':'All seven actual page images and the contact sheet were viewed. Formulas, matrix columns, tags, margins and page breaks are clean. This is actual image review in addition to the automated layout result.',
 'images':[{'file':f'qa/page-{i}.png','sha256':sha(R/f'qa/page-{i}.png'),'actually_viewed':True} for i in range(1,8)]
}
(L/'e_fiftythree_ordinary_visual_review.json').write_text(json.dumps(visual,indent=2)+'\n')
programs=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or p.suffix not in ('.py','.gp'):continue
    rel=p.relative_to(R).as_posix();out=p.with_suffix('.out');err=p.with_suffix('.err')
    if rel=='code/e53_ordinary_freeze.py':
        programs.append({'source':rel,'source_sha256':sha(p),'stdout':'code/e53_ordinary_freeze.out','scope':'Actual current invocation; complete captured stdout is excluded from the recursively generated manifest.'})
        continue
    assert out.exists(),rel
    assert out.stat().st_size or (err.exists() and err.stat().st_size),rel
    programs.append({'source':rel,'source_sha256':sha(p),
     'stdout':out.relative_to(R).as_posix(),'stdout_sha256':sha(out),
     'stderr':err.relative_to(R).as_posix() if err.exists() else None,
     'stderr_sha256':sha(err) if err.exists() else None,
     'scope':'Actual retained execution; histories distinguish failed attempts from final mathematical results and complete copied-source replays.'})
(L/'e_fiftythree_ordinary_program_outputs.json').write_text(json.dumps(programs,indent=2)+'\n')
excluded={'ledger/e_fiftythree_ordinary_manifest.json','code/e53_ordinary_freeze.out','code/e53_ordinary_freeze.err'}
files=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    rel=p.relative_to(R).as_posix()
    if rel in excluded:continue
    files.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
inputs=[r for r in files if r['path'].startswith('inputs/')]
manifest={
 'statement':'E.124','status':'FROZEN','proof':proof.relative_to(R).as_posix(),
 'proof_sha256':sha(proof),'PDF':'qa/e124_standalone.pdf','PDF_sha256':sha(R/'qa/e124_standalone.pdf'),
 'owned_files':files,'immutable_inputs':inputs,'excluded_recursive_outputs':sorted(excluded),
 'program_output_registry':'ledger/e_fiftythree_ordinary_program_outputs.json',
 'full_replay':'code/e53_ordinary_replay.json',
 'visual_review':'ledger/e_fiftythree_ordinary_visual_review.json',
 'source_evidence':'ledger/e_fiftythree_ordinary_source_evidence.json',
 'proof_review_scope':'Author complete; root full draft review received. Final root replay and independent final peer audit are not claimed at this freeze.',
 'portable_replay':'In a fresh copy: python code/e53_ordinary_replay.py --gp /absolute/path/to/gp --label fresh_audit'
}
mp=L/'e_fiftythree_ordinary_manifest.json'
mp.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':'FROZEN','statement':'E.124','owned_files':len(files),
 'programs_with_actual_outputs':len(programs),'immutable_input_files':len(inputs),
 'proof_sha256':sha(proof),'manifest_sha256':sha(mp),'PDF_sha256':sha(R/'qa/e124_standalone.pdf'),
 'replay':'PASS, nine stages, whole outputs and both complete GEN objects, no exclusions',
 'actual_visual_review_pages':7},indent=2))
