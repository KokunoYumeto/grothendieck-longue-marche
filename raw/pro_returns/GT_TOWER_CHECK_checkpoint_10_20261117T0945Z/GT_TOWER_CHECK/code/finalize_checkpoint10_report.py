#!/usr/bin/env python3
"""Record the tenth hourly review for the exact fully inspected manuscript."""
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
assert len(rows)==180 and counts=={'Proved':165,'Known':2,'Open':13}
log=(ROOT/'GT_TOWER_CHECK_paper.log').read_text()
assert not re.search(r'Overfull|undefined|multiply defined',log)
record=(f"Checkpoint 10 has {manifest['pdf_pages']} pages, zero overfull boxes and no unresolved references or citations. "
 f"All {len(manifest['pages'])} selected full-page PNGs were opened and visually inspected. "
 "The first tenth-hour build exposed one 74.68729pt overflow at CMC.1; its authoritative source was split into two gathered lines. "
 "The failed source and build logs remain retained. A later wording repair made the assertion 2*kappa_s=0 explicit; "
 "the sole changed full-page image, page 222, was reopened and inspected. The other 100 selected PNGs were byte-identical, checked by SHA256. "
 "The final three-pass build has no overflow. "
 f"The PDF SHA256 is {sha}. Exact source/build hashes, page observations and image hashes are retained.")
review=("The tenth-hour review records a completed explicit finite exclusion theorem on the main A.4 task. "
 "A.4.57 specifies one characteristic five-point level and proves that every genuine gentle pentagon shadow there has Delta zero, "
 "for every multiplier. Its proof includes the actual branch-kernel comparison, both ordinary normalizer corrections, "
 "the one-conjugator CM square, the finite point-pushing linearization and the exact coupled cubic-centralizer residues. "
 "The full genuine-source enumeration at that level remains unexecuted. A.4.55 and A.4.59 prove actual parity-one survivors "
 "of the complete smaller mod6 and mod12 tests, with full canonical-cover lifts. A.4.60 determines the integral target and "
 "common source at every coefficient, providing exact transition maps for the next census. The later working proof A.4.61 "
 "now constructs one genuine parity-one survivor through the entire relative-abelian tower simultaneously; its complete "
 "integral affine, canonical-kernel and Hensel argument has passed independent semantic audit and a fresh five-program replay. "
 "It is retained as a working proof for subsequent integration and is not counted among the 180 statements in this checked PDF. "
 "The first binary class-two target and its literal eight-map common source have also been computed, with an exact "
 "comparison to the modular class-two source. These results address the remaining main A.4 computation directly. Research therefore continues "
 "after checkpoint 10. The next hourly checkpoint and progress review are due at approximately 10:45 UTC.")
pending_path=ROOT/'notes/tenth_pending_status.json'
pending=(json.loads(pending_path.read_text())['text'] if pending_path.exists() else
 "The retained working sources contain the exact uniform binary canonical modules and transition maps, the integral affine "
 "lifting system, and the diagnostic factorization of the compact ordered-pole target through Gamma12. The honest affine "
 "tangent map into the full canonical transition kernel and a nonabelian five-point refinement remain under active calculation. "
 "These continuing inputs are retained separately and are not silently counted as additional numbered results of this checked manuscript.")
path=ROOT/'GT_TOWER_CHECK_report.md';backup=ROOT/'notes/tenth_hour_report_before_finalization.md'
assert not backup.exists(),'One-shot finalization already performed.'
shutil.copy2(path,backup)
text=path.read_text().replace('Current state during tenth-hour work','Current state at checkpoint 10')
start=text.index('Tenth-hour working manuscript, 17 November 2026.');end=text.index('\n\n',start)
text=text[:start]+(
 "Tenth-hour checkpoint, 17 November 2026. Research began at approximately 23:45 UTC on 16 November. "
 "Checkpoints 01--09 remain unchanged. Seven further audited results are integrated. "
 f"The checked manuscript has {manifest['pdf_pages']} pages and 180 numbered statements: 165 Proved, 2 Known and 13 Open. "
 f"Its completed three-pass LuaLaTeX build and {len(manifest['pages'])} actual full-page inspections are recorded below. "
 "The next hourly checkpoint and progress review are due at approximately 10:45 UTC.")+text[end:]
start=text.index('The current working ledger has 180 numbered statements:')
end=text.index('The prior checkpoint manuscripts',start)
text=text[:start]+(
 "The current ledger has 180 numbered statements: 165 Proved, 2 Known and 13 Open. "
 "All seven newly integrated numbered results and their finite certificates have passed root review and independent audit or replay. "
 +record+' ')+text[end:]
heading='## Sources, reproducibility and retained files'
assert text.count(heading)==1
text=text.replace(heading,'## Tenth-hour progress review\n\n'+review+
 '\n\n## Continuing work retained at the tenth-hour freeze\n\n'+pending+'\n\n'+heading)
path.write_text(text)
with (ROOT/'notes/typesetting_audit.md').open('a') as stream:
    stream.write('\n\n## Checkpoint 10\n\n'+record+
      '\n\nInspector counts: '+str(manifest['inspector_counts'])+'.\n')
with (ROOT/'notes/research_log.md').open('a') as stream:
    stream.write('\n\n## Tenth-hour progress review\n\n'+review+'\n\n'+record+'\n\n'+pending+'\n')
provenance=ROOT/'notes/checkpoint_provenance';provenance.mkdir(exist_ok=True)
(provenance/'checkpoint_10_prearchive.json').write_text(json.dumps({
 'utc':datetime.now(timezone.utc).isoformat(),'checkpoint':10,'statement_count':len(rows),
 'statuses':counts,'pdf_sha256':sha,'pdf_pages':manifest['pdf_pages'],
 'visually_inspected_pages':len(manifest['pages']),'inspector_counts':manifest['inspector_counts'],
 'overfull_boxes':0,'unresolved_references':0,
 'progress_review':'Continue: explicit finite exclusion is proved; a simultaneous all-coefficient genuine survivor and the exact next binary nonabelian source advance the main A.4 computation.',
 'pending_source_fragments':pending},indent=2)+'\n')
print(record)
print('Recorded the tenth-hour decision to continue and the 180-statement ledger.')
