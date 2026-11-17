from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, re
ROOT=Path(__file__).resolve().parents[1]
expected=list(range(46,79))+list(range(80,88))+[89]
log=(ROOT/'progress.log').read_text()
assert not re.search(r'^transcription frozen ',log,re.M),'Already frozen'
assert not re.search(r'^context opened ',log,re.M),'Context was already opened'
pages=sorted((ROOT/'pages').glob('*.tex'))
assert [int(re.search(r'scan(\d+)',p.name)[1]) for p in pages]==expected
combined=ROOT/'MPL_138_046-089_transcription.tex'
s=combined.read_text()
assert s=='\n'.join(p.read_text() for p in pages)
assert s.startswith('\\cotefile{138}\n\\scanpage{46}')
assert s.count('\\cotefile{')==1
assert [int(n) for n in re.findall(r'\\scanpage\{(\d+)\}',s)]==expected
assert sorted(int(n) for n in re.findall(r'^138 scan (\d+) done ',log,re.M))==expected
assert sorted(int(n) for n in re.findall(r'^scan (\d+) audited ',log,re.M))==expected
with (ROOT/'MPL_138_046-089_inventory.csv').open() as f:
    rd=csv.DictReader(f); rows=list(rd)
    assert rd.fieldnames==['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
assert all(x['transcribed']=='yes' for x in rows)
assert sorted(set(int(x['scan']) for x in rows))==expected
assert all(x['kind'] in ['text','display','diagram','drawing','margin note','insertion','deletion'] for x in rows)
assert all(x['sheet_kind'] in ['text','reused_typed','cancelled_draft','cover'] for x in rows)
sha=[]
for p in pages+[combined]:sha.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(ROOT).as_posix())
(ROOT/'SHA256SUMS').write_text('\n'.join(sha)+'\n')
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:
    f.write('Pre-freeze validation: 42 saved pages; 42 second visual audits; 646 inventory rows all yes; 26 TikZ-CD environments and 3 array tables.\n')
    f.write('Raw combined fragment compiled successfully with pdfLaTeX; no syntax, missing-glyph, overfull or underfull warnings. Temporary validation harness only; 44 rendered sheets are not manuscript pagination.\n')
    f.write('Rendered checks inspected for scans 047, 053, 062, 064, 078, 089; the nested barycentric drawing on 078 accounts for its extra inventory drawing row.\n')
    f.write('Encoding-only fixes before freeze: explicit TikZ-CD ampersand replacement; text-mode words in the 047 array; paragraph boundary before the 062 minipages.\n')
    for h in sha:f.write('SHA-256 '+h+'\n')
    f.write('transcription frozen '+stamp+'\n')
(ROOT/'validation_report.md').write_text(f'''# Pre-freeze validation

Completed {stamp}.

- 42 page files, exactly scans 046–078, 080–087 and 089.
- 42 per-page completion records and 42 separate visual audit records.
- 646 inventory rows; all marked `yes`; all required columns and allowed categories checked.
- One combined fragment, exactly the ordered concatenation of the page files, beginning with `\\cotefile{{138}}` and `\\scanpage{{46}}`.
- 26 TikZ-CD environments and 3 array tables within diagram macros.
- 349 explicit uncertainty macros and 3 physically unreadable word spans, estimated at 6 words in total.
- Successful pdfLaTeX compilation of the raw fragment using the disposable harness in `scripts/check_tex.py`; no syntax, missing-glyph, overfull or underfull warnings in the final log.
- Rendered checks inspected on 047, 053, 062, 064, 078 and 089. The drawing and its inner barycentric triangle on 078 share one TikZ figure and have separate inventory rows.
- The temporary harness uses colours for page-state macros and is not the diplomatic deliverable or a facsimile. Its 44 physical sheets do not assert manuscript pagination.
- SHA-256 hashes for all 42 page files and the combined fragment are recorded in `SHA256SUMS` and `progress.log` before any contextual source was opened.

No OCR or sub-agent transcription was used. Source images and the context archive are excluded from the deliverable archive.
''')
print('transcription frozen',stamp,';',len(sha),'hashes')
