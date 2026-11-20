from pathlib import Path
import json
out=Path('/workspace/scratch/94548b74fbe0/out/readers/012/B')
r=json.loads((out/'report.json').read_text())
r['end_utc']='2026-11-20 13:13:48 UTC'
r['workflow']['structural_checks']=json.loads((out/'scripts/structural_checks.json').read_text())
r['notes'].append({'topic':'Final synchronization','text':'reading.tex, report.json and reading.md were checked together after the final additions. Original lexical labels, all three source C doubt mappings, cancellation qualifications, all 22 added physical trace entries, 68 contour mappings, crop references and the archive comment agree. End of independent review: 2026-11-20 13:13:48 UTC.'})
(out/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=out/'reading.md';s=p.read_text()
s=s.replace('Structural source checks will be recorded after the final synchronized read.','Structural source checks passed after the final synchronized read: braces and environments balance; only supplied or standard TikZ/LaTeX commands occur; all 68 original C contours remain byte-for-byte; all eight lexical labels and their qualifications match report.json; all three C source rows and their nine local subloci are mapped; all 55 inventory entries and ten crop references resolve. No compiler or renderer was used.\n\nUTC end of independent review: 2026-11-20 13:13:48 UTC.')
p.write_text(s)
print('Final report and audit synchronized; end UTC recorded.')
