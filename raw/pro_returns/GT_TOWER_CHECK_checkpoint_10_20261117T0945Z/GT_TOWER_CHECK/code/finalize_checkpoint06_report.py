#!/usr/bin/env python3
"""Record the completed sixth-hour build and actual visual inspection."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT/'notes/pdf_qa/manifest.json').read_text())
assert all(row.get('visually_inspected') for row in manifest['pages'])
sha = hashlib.sha256((ROOT/'GT_TOWER_CHECK_paper.pdf').read_bytes()).hexdigest()
assert sha == manifest['pdf_sha256']
rows = list(csv.DictReader((ROOT/'GT_TOWER_CHECK_results.csv').open()))
counts = {s:sum(r['status']==s for r in rows) for s in ('Proved','Known','Open')}
assert len(rows)==141 and counts=={'Proved':126,'Known':2,'Open':13}
log = (ROOT/'GT_TOWER_CHECK_paper.log').read_text()
assert not re.search(r'Overfull|undefined|multiply defined',log)
record = (f"Checkpoint06 has {manifest['pdf_pages']} pages, zero overfull boxes and no unresolved references or citations. "
          f"All {len(manifest['pages'])} selected full-page PNGs were opened and visually inspected. "
          "No clipping, overlap, damaged glyphs or unreadable displays were found. "
          f"The PDF SHA256 is {sha}. "
          "The exact source/build hashes, individual page observations and PNG hashes are retained in the build and visual-audit manifests.")
path=ROOT/'GT_TOWER_CHECK_report.md'
text=path.read_text()
old=('Sixth-hour working revision, 17 November 2026. Research began at approximately23:45UTC on16November. '
     'Checkpoint05 was saved after its ZIP completed at04:45:40UTC and remains unchanged. '
     'The current source includes the audited post-checkpoint normalizer and descent results. '
     'The next checkpoint and hourly progress review are due at approximately05:45UTC; '
     'the current newly integrated source is not represented as a visually checked PDF until its build and inspection have completed.')
new=('Sixth-hour checkpoint, 17 November 2026. Research began at approximately23:45UTC on16November. '
     'Checkpoint05 remains unchanged. The audited sixth-hour proofs have a clean three-pass LuaLaTeX build '
     'and completed full-page visual inspection. The source ledger has141 statements:126Proved,2Known and13Open. '
     'The next checkpoint and hourly progress review are due at approximately06:45UTC.')
assert old in text
text=text.replace(old,new)
start=text.index('The current source ledger has141 numbered statements:126Proved')
end=text.index('The prior checkpoint manuscripts',start)
text=text[:start]+('The current ledger has141 numbered statements:126Proved,2Known and13Open. '
                  'All new integrated finite computations and proofs named above have been independently reviewed or rerun. '
                  +record+' ')+text[end:]
text=text.replace('The next hourly review is due at approximately05:45UTC.',
                  'The sixth-hour review records substantial advances in the main A.4 finite comparison: the exact joint normalizer, finite fusion, actual local braid target and central-recovery map are now proved. The entire reduced descent obstruction has also vanished, and the exact infinite quadratic quotient is proved. New ten-point fusion and peripheral computations and a further centralizer witness remain under audit. These advance the main question and specified open items, so research continues after checkpoint06. The next hourly review is due at approximately06:45UTC.')
text=text.replace('finite fusion and the direct braid bridge are proved; the common pentagon level',
                  'finite fusion, the direct braid bridge and its exact216-element central-recovery target are proved; the common pentagon level')
path.write_text(text)
with (ROOT/'notes/typesetting_audit.md').open('a') as f:
    f.write('\n\n## Checkpoint06\n\n'+record+'\n\nInspector counts: '+str(manifest['inspector_counts'])+'.\n')
with (ROOT/'notes/research_log.md').open('a') as f:
    f.write('\n\n## Sixth-hour progress review\n\nThe main finite A.4 task advanced through exact joint normalizers, pure corrections, finite fusion and an actual432-to216 central-recovery map. The common finite pentagon implication remains unproved. B.2 now has a fully vanishing central obstruction, surjective descent and the exact infinite quadratic quotient. Pending ten-point binary fusion, class-three comparison and further signed centralizer work are moving these same open items. Research continues under the user\'s hourly stopping rule. '+record+'\n')
print(record)
print('Recorded the hourly decision to continue and the141-statement ledger.')
