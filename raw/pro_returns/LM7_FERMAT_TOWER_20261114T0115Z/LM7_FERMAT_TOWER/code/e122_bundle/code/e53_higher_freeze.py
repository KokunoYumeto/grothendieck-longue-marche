"""Freeze every E122 source, actual output, data object and retained failure."""
from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[1]
manifest=R/'ledger/e_fiftythree_higher_manifest.json'
excluded={manifest,R/'code/e53_higher_freeze.out',R/'code/e53_higher_freeze.err'}
files=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or p in excluded or '__pycache__' in p.parts:continue
    files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
proof=R/'sections/E_fiftythree_higher_action.tex';text=proof.read_text()
assert text.count('\\begin{statement}')==text.count('\\end{statement}')==1
assert len(re.findall(r'(?m)^\s*\\\[\s*$',text))==len(re.findall(r'(?m)^\s*\\\]\s*$',text))
assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',text)
layout=json.loads((R/'code/e53_higher_layout.json').read_text())
assert layout['status']=='LAYOUT_PASS' and layout['section_sha256']==hashlib.sha256(proof.read_bytes()).hexdigest()
assert json.loads((R/'code/e53_higher_replay.json').read_text())['status']=='PASS'
pairs={}
for p in sorted(R.rglob('*')):
    if p.suffix not in ['.py','.gp'] or not p.is_file():continue
    if p==Path(__file__).resolve():continue
    out=p.with_suffix('.out');err=p.with_suffix('.err')
    assert out.exists() or err.exists(),str(p)
    assert (out.exists() and out.stat().st_size) or (err.exists() and err.stat().st_size),str(p)
    pairs[str(p.relative_to(R))]={'stdout':str(out.relative_to(R)) if out.exists() else None,
                                'stderr':str(err.relative_to(R)) if err.exists() else None,
                                'stdout_bytes':out.stat().st_size if out.exists() else None,
                                'stderr_bytes':err.stat().st_size if err.exists() else None}
d={'statement':'E.122','status':'FROZEN','owned_file_count':len(files),'files':files,
   'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
   'program_output_pairs':pairs,
   'self_output':'The actual code/e53_higher_freeze.out and .err are retained after execution and excluded from this manifest to avoid self-reference. No snapshot of their in-progress empty streams is created.',
   'scope':'All mathematical data and source, including discovery/failure records, are retained. Final theorem replay uses only the five owned mathematical sources and literal inputs in the dependency ledger.',
   'author_replay':'Complete byte/GEN identity, zero exclusions.',
   'visual_scope':'All eight final page images were actually opened and reviewed; no overfull boxes.'}
t=json.dumps(d,indent=2)+'\n';manifest.write_text(t)
print(json.dumps({'status':'PASS','manifest':str(manifest.relative_to(R)),
                  'manifest_sha256':hashlib.sha256(t.encode()).hexdigest(),
                  'owned_file_count':len(files),'proof_sha256':d['proof_sha256'],
                  'programs_with_actual_output':len(pairs)+1},indent=2))
