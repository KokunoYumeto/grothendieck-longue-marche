#!/usr/bin/env python3
"""Finalize the eighth-hour report after the exact PDF and all page inspections."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'notes/pdf_qa/manifest.json').read_text())
assert all(row.get('visually_inspected') for row in manifest['pages'])
sha=hashlib.sha256((ROOT/'GT_TOWER_CHECK_paper.pdf').read_bytes()).hexdigest()
assert sha==manifest['pdf_sha256']
rows=list(csv.DictReader((ROOT/'GT_TOWER_CHECK_results.csv').open()))
counts={s:sum(row['status']==s for row in rows) for s in ('Proved','Known','Open')}
assert len(rows)==165 and counts=={'Proved':150,'Known':2,'Open':13}
log=(ROOT/'GT_TOWER_CHECK_paper.log').read_text()
assert not re.search(r'Overfull|undefined|multiply defined',log)
record=(f"Checkpoint08 has {manifest['pdf_pages']} pages, zero overfull boxes and no unresolved references or citations. "
        f"All {len(manifest['pages'])} selected full-page PNGs were opened and visually inspected. "
        "No clipping, overlap, damaged glyphs or unreadable displays were found. "
        f"The PDF SHA256 is {sha}. "
        "The exact source/build hashes, page observations and PNG hashes are retained in the build and visual-audit manifests.")
path=ROOT/'GT_TOWER_CHECK_report.md';text=path.read_text()
start=text.index('Eighth-hour working revision, 17 November 2026.')
end=text.index('\n\n',start)
text=text[:start]+(
    'Eighth-hour checkpoint, 17 November 2026. Research began at approximately23:45UTC on16November. '
    'Checkpoints01--07 remain unchanged. Nine further independently audited results have been integrated, '
    'with a clean three-pass LuaLaTeX build and completed full-page visual inspection. '
    'The ledger has165 statements:150Proved,2Known and13Open. '
    'The next checkpoint and hourly progress review are due at approximately08:45UTC.')+text[end:]
text=text.replace('Current state during eighth-hour work','Current state at checkpoint08')
start=text.index('The current ledger has165 numbered statements')
end=text.index('The prior checkpoint manuscripts',start)
text=text[:start]+(
    'The current ledger has165 numbered statements:150Proved,2Known and13Open. '
    'All nine newly integrated proofs and their finite certificates have passed root review and independent audit or replay. '
    +record+' ')+text[end:]
review=('The eighth-hour review records a complete ordinary-centralizer image census, an explicit finite coefficient compiler, '
        'and the actual finite genus-one and universal-curve actions. Two genuine-survivor theorems eliminate whole proposed '
        'relative nilpotent target families. The exact C3^4 discrepancy and full CM fibre product identify the remaining finite '
        'recognition obstruction. A marked C3*C3 covering source and a split five-point retraction provide two new concrete '
        'routes into that obstruction. The next work is the relative configuration-cover recognition and the complete genuine '
        'frame gate on the retained alternating-prime source. These advance the main A.4 question, so research continues after '
        'checkpoint08. The next hourly review is due at approximately08:45UTC.')
assert text.count('The next hourly review is due at approximately07:45UTC.')==1
text=text.replace('The next hourly review is due at approximately07:45UTC.',review)
pending=('The post-freeze working files retain the actual common ternary source calculation (rank97), its two-dimensional '
         'kernel to the vertex-module image, and the exact remaining harmonic-frame gate. They also retain the normalized '
         'torus-configuration fixed-locus proof and the developing relative cohomology/Smith refinement. These are continuing '
         'research records; none is silently treated as the completed ambient finite-normalizer recognition or full shadow census. '
         'The fresh primary Smith-theory location was opened by both the investigator and root. All current source fragments, '
         'programs and actual outputs are included, with earlier passages preserved by the checkpoint retention procedure.')
needle='## Sources, reproducibility and retained files'
assert needle in text
text=text.replace(needle,'## Pending work retained at the eighth-hour freeze\n\n'+pending+'\n\n'+needle)
path.write_text(text)
with (ROOT/'notes/typesetting_audit.md').open('a') as stream:
    stream.write('\n\n## Checkpoint08\n\n'
      'The first eighth-hour build stopped at an Improper prevdepth error caused by paragraph commands inside a proof; '
      'all three such headers in the harmonic fragment were repaired and the actual failed log was retained. '
      'Subsequent eighth-hour full builds reported zero overfull boxes, including zero greater than2pt. '
      'The new proof headers use explicit paragraph spacing. The finite CM marking was corrected by the actual free-group '
      'swap before the final freeze. '+record+'\n\nInspector counts: '+str(manifest['inspector_counts'])+'.\n')
with (ROOT/'notes/research_log.md').open('a') as stream:
    stream.write('\n\n## Eighth-hour progress review\n\n'+review+'\n\n'+record+'\n\n'+pending+'\n')
provenance=ROOT/'notes/checkpoint_provenance';provenance.mkdir(exist_ok=True)
(provenance/'checkpoint_08_prearchive.json').write_text(json.dumps({
    'utc':datetime.now(timezone.utc).isoformat(),'checkpoint':8,'statement_count':len(rows),
    'statuses':counts,'pdf_sha256':sha,'pdf_pages':manifest['pdf_pages'],
    'visually_inspected_pages':len(manifest['pages']),'inspector_counts':manifest['inspector_counts'],
    'overfull_boxes':0,'unresolved_references':0,
    'progress_review':'Continue: main finite recognition and genuine frame census are advancing.',
    'pending_source_fragments':pending},indent=2)+'\n')
print(record)
print('Recorded the hourly decision to continue and the165-statement ledger.')
