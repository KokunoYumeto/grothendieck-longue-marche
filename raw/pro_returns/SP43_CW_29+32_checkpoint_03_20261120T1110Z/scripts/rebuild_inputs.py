"""Reconstruct only disposable page input bundles after a checkpoint restore.

The original user archive must already have been unpacked once into source/.
This never resets notation, progress, check events, checkpoints, or decisions.
"""
from pathlib import Path
import csv,json,re,shutil,subprocess
O=Path(__file__).resolve().parents[1];R=O.parent
S=R/'source/SP43_CW_29+32_witnesses';W=R/'work';W.mkdir(exist_ok=True)
rows=list(csv.DictReader((S/'page_map.tsv').open(),delimiter='\t'))
(W/'page_map.json').write_text(json.dumps(rows,indent=2)+'\n')
if not (O/'PREAMBLE.tex').exists():shutil.copyfile(S/'codex/C29-04/PREAMBLE.tex',O/'PREAMBLE.tex')
for row in rows:
    stem=Path(row['codex_file']).stem;d=W/stem;d.mkdir(exist_ok=True)
    if not (d/'C.tex').exists():shutil.copyfile(S/row['codex_file'],d/'C.tex')
    if not (d/'H.tex').exists():
        h=(S/row['hua_file']).read_text();m=re.search(r'\\page\{'+row['their_page']+r'\}',h)
        block='% Witness H has no transcription of this scan.\n'
        if row['hua_has']=='text' and m:
            end=re.search(r'\\page\{\d+\}',h[m.end():])
            block=h[m.end():m.end()+end.start() if end else len(h)]
        (d/'H.tex').write_text(block)
    meta=dict(row,stem=stem,**{role:str(R/'source/SP43_CW_29+32_scans'/f'{stem}{suffix}.jpg') for role,suffix in [('whole',''),('half_a','_a'),('half_b','_b')]})
    (d/'meta.json').write_text(json.dumps(meta,indent=2)+'\n')
    if not (d/'C_prior_questions.md').exists():subprocess.run(['python',str(O/'scripts/refresh_prior_questions.py'),stem],check=True)
    snap=O/'notation_snapshots'/f'{stem}.md'
    if snap.exists() and not (d/'notation_snapshot.md').exists():shutil.copyfile(snap,d/'notation_snapshot.md')
print('Rebuilt input bundles without changing any deliverable or decision.')
