#!/usr/bin/env python3
"""Record the ninth hourly review against the exact checked manuscript."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re,shutil
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'notes/pdf_qa/manifest.json').read_text())
assert all(row.get('visually_inspected') for row in manifest['pages'])
sha=hashlib.sha256((ROOT/'GT_TOWER_CHECK_paper.pdf').read_bytes()).hexdigest()
assert sha==manifest['pdf_sha256']
rows=list(csv.DictReader((ROOT/'GT_TOWER_CHECK_results.csv').open()))
counts={s:sum(row['status']==s for row in rows) for s in ('Proved','Known','Open')}
assert len(rows)==173 and counts=={'Proved':158,'Known':2,'Open':13}
assert not re.search(r'Overfull|undefined|multiply defined',(ROOT/'GT_TOWER_CHECK_paper.log').read_text())
record=(f"Checkpoint09 has {manifest['pdf_pages']} pages, zero overfull boxes and no unresolved references or citations. "
        f"All {len(manifest['pages'])} selected full-page PNGs were opened and visually inspected. "
        "The observed crowded SVM.6 display was repaired without changing its two-line height; exact bibliography locations received ordinary spacing. "
        "The repaired render changed only pages171,370,371; each was reopened and inspected. The other82 selected images were byte-identical, verified by SHA256. "
        "The final inspected pages have no clipping, overlap, damaged glyphs or unreadable displays. "
        f"The PDF SHA256 is {sha}. Exact source/build hashes, before-repair files and all page observations are retained.")
review=('The ninth-hour review records explicit finite recognition of the ordinary translation normalizer, '
        'fusion of competing translation complements for every multiplier, and full elliptic-involution centralizer recognition '
        'on the nine-, ten-, eleven- and twelve-point configurations. The exact common binary, ternary and modulus-six source '
        'kernels are proved, with the actual eight insertion maps and literal Chinese remainder comparison. '
        'The entire mixed-mod6 identity fibre is excluded at parity one, while genuine harmonic survivors prove the limits '
        'of the preceding odd refinements. An additional pure positive involution-fusion proof has passed two independent '
        'audits in the retained working sources. The direct branch-cover comparison and full canonical-cover census of '
        'nonidentity records have both made concrete new progress. These results advance the main A.4 question, so research '
        'continues after checkpoint09. The next hourly checkpoint and progress review are due at approximately09:45UTC.')
pending_path=ROOT/'notes/ninth_pending_status.json'
pending=(json.loads(pending_path.read_text())['text'] if pending_path.exists() else
         'The working sources retain the reviewed A.4.56 finite involution fusion, the collar/diagonal braid comparison, '
         'the developing direct nine-point branch-output realization, and the selected nonidentity full central-cover computation. '
         'These continuing fragments are not silently counted as integrated statements of the checked372-page manuscript.')
path=ROOT/'GT_TOWER_CHECK_report.md'
backup=ROOT/'notes/ninth_hour_report_before_finalization.md'
assert not backup.exists(), 'One-shot finalization already performed.'
shutil.copy2(path,backup)
text=path.read_text()
text=text.replace('Current state after checkpoint08','Current state at checkpoint09')
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| A.4 |'):
        lines[i]='| A.4 | A.4, A.4.1--A.4.52; A.4.54; retained working A.4.53, A.4.55--A.4.56 | Open; explicit translation fusion and ordinary centralizer recognition are proved; the exact common mod6 source has parity0 in its identity fibre but a genuine parity1 pentagon survivor in a nonidentity fibre; direct branch-output retention and the remaining finite branch-kernel comparison advance the separating-level census |'
text='\n'.join(lines)+'\n'
start=text.index('Ninth-hour working manuscript, 17 November 2026.')
end=text.index('\n\n',start)
text=text[:start]+(
    'Ninth-hour checkpoint, 17 November 2026. Research began at approximately23:45UTC on16November. '
    'Checkpoints01--08 remain unchanged. Eight further audited results have been integrated. '
    'The checked manuscript has372pages and173numbered statements:158Proved,2Known,13Open. '
    'The completed three-pass LuaLaTeX build and85actual full-page inspections are recorded below. '
    'The next hourly checkpoint and progress review are due at approximately09:45UTC.')+text[end:]
text=text.replace('Checkpoints01--07 are retained unchanged.','Checkpoints01--08 are retained unchanged.')
start=text.index('The current ledger has165 numbered statements')
end=text.index('The prior checkpoint manuscripts',start)
text=text[:start]+('The current ledger has173 numbered statements:158Proved,2Known and13Open. '
    'All eight newly integrated proofs and their finite certificates have passed root review and independent audit or replay. '
    +record+' ')+text[end:]
needle='The next hourly review is due at approximately08:45UTC.'
assert text.count(needle)==1
text=text.replace(needle,review)
needle='## Sources, reproducibility and retained files'
assert text.count(needle)==1
text=text.replace(needle,'## Continuing work retained at the ninth-hour freeze\n\n'+pending+'\n\n'+needle)
path.write_text(text)
with (ROOT/'notes/typesetting_audit.md').open('a') as stream:
    stream.write('\n\n## Checkpoint09\n\n'
      'The initial ninth-hour build had one5.168pt overfull SVM display and one unresolved Fresse citation. '
      'Both were repaired in authoritative sources, with the failed build and bibliography gate retained. '
      'The next full build had zero overfull boxes; full-page inspection identified a crowded SVM.6 rank row and bibliography spacing. '
      'The final same-height spacing repair retained all mathematical content. '+record+
      '\n\nInspector counts: '+str(manifest['inspector_counts'])+'.\n')
with (ROOT/'notes/research_log.md').open('a') as stream:
    stream.write('\n\n## Ninth-hour progress review\n\n'+review+'\n\n'+record+'\n\n'+pending+'\n')
provenance=ROOT/'notes/checkpoint_provenance'
(provenance/'checkpoint_09_prearchive.json').write_text(json.dumps({
    'utc':datetime.now(timezone.utc).isoformat(),'checkpoint':9,'statement_count':len(rows),
    'statuses':counts,'pdf_sha256':sha,'pdf_pages':manifest['pdf_pages'],
    'visually_inspected_pages':len(manifest['pages']),'inspector_counts':manifest['inspector_counts'],
    'overfull_boxes':0,'unresolved_references':0,
    'progress_review':'Continue: main finite branch recognition and genuine common-source frame census are advancing.',
    'pending_source_fragments':pending},indent=2)+'\n')
print(record)
print('Recorded the ninth hourly decision to continue and the173-statement ledger.')
