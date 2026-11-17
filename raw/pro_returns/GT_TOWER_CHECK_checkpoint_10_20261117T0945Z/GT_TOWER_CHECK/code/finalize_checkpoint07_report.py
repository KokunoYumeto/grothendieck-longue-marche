#!/usr/bin/env python3
"""Record the completed seventh-hour build and every actual page inspection."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'notes/pdf_qa/manifest.json').read_text())
assert all(row.get('visually_inspected') for row in manifest['pages'])
sha=hashlib.sha256((ROOT/'GT_TOWER_CHECK_paper.pdf').read_bytes()).hexdigest()
assert sha==manifest['pdf_sha256']
rows=list(csv.DictReader((ROOT/'GT_TOWER_CHECK_results.csv').open()))
counts={s:sum(r['status']==s for r in rows) for s in ('Proved','Known','Open')}
assert len(rows)==156 and counts=={'Proved':141,'Known':2,'Open':13}
log=(ROOT/'GT_TOWER_CHECK_paper.log').read_text()
assert not re.search(r'Overfull|undefined|multiply defined',log)
record=(f"Checkpoint07 has {manifest['pdf_pages']} pages, zero overfull boxes and no unresolved references or citations. "
        f"All {len(manifest['pages'])} selected full-page PNGs were opened and visually inspected. "
        "No clipping, overlap, damaged glyphs or unreadable displays were found. "
        f"The PDF SHA256 is {sha}. "
        "The exact source/build hashes, individual page observations and PNG hashes are retained in the build and visual-audit manifests.")
path=ROOT/'GT_TOWER_CHECK_report.md'
text=path.read_text()
assert 'Seventh-hour working revision' in text
start=text.index('Seventh-hour working revision')
end=text.index('\n\n',start)
text=text[:start]+(
    'Seventh-hour checkpoint, 17 November 2026. Research began at approximately23:45UTC on16November. '
    'Checkpoints01--06 remain unchanged. The audited seventh-hour proofs have a clean three-pass LuaLaTeX build '
    'and completed full-page visual inspection. The source ledger has156 statements:141Proved,2Known and13Open. '
    'The next checkpoint and hourly progress review are due at approximately07:45UTC.')+text[end:]
text=text.replace('Current state during seventh-hour work','Current state at checkpoint07')
start=text.index('The current source ledger has156 numbered statements')
end=text.index('The prior checkpoint manuscripts',start)
text=text[:start]+(
    'The current ledger has156 numbered statements:141Proved,2Known and13Open. '
    'All new integrated finite computations and proofs named above have been independently reviewed or rerun. '
    +record+' ')+text[end:]
review=('The seventh-hour review records new explicit finite ten-point quotient, centralizer, fusion and geometric-word constructions, '
        'together with a specified characteristic five-point action. The final finite frame comparison and complete shadow census remain active. '
        'The full quadratic-character module now has countably many independent prime-indexed descent generators and an exact infinite-dimensional quotient by descent. '
        'An actual ordinary-centralizer image computation and the finite E44-to-local-frame comparison are continuing in separately retained working fragments. '
        'These advance the main finite question and specified open items, so research continues after checkpoint07. '
        'The next hourly review is due at approximately07:45UTC.')
assert text.count('The next hourly review is due at approximately06:45UTC.')==1
text=text.replace('The next hourly review is due at approximately06:45UTC.',review)
pending=('The separately retained A.4.38 working fragment and its executed quartet-motion/ordinary-image programs were produced after the integrated proof freeze. '
         'They are preserved with their actual outputs and independent audit notes; the root review and manuscript integration are pending. '
         'The auxiliary PC52 cohomology run was terminated as superseded by the integral perfect-factor proof; no cohomology result is claimed for it, and its source and output remain retained.')
text=text.replace('## Sources, reproducibility and retained files',
                  '## Pending work retained at the source freeze\n\n'+pending+'\n\n## Sources, reproducibility and retained files')
path.write_text(text)
with (ROOT/'notes/typesetting_audit.md').open('a') as f:
    f.write('\n\n## Checkpoint07\n\n'
            'The seventh-hour first complete build had two overflows greater than2pt, of10.81139pt and129.59485pt, '
            'and one smaller1.3854pt paragraph overflow. The source display, breakable filenames and paragraph map were repaired. '
            'A later newly integrated proof had a missing math delimiter; that failed build and every subsequent build log are retained. '
            'The final three-pass build has zero overfull boxes. '+record+'\n\nInspector counts: '+str(manifest['inspector_counts'])+'.\n')
with (ROOT/'notes/research_log.md').open('a') as f:
    f.write('\n\n## Seventh-hour progress review\n\n'+review+'\n\n'+record+'\n')
provenance=ROOT/'notes/checkpoint_provenance'
provenance.mkdir(exist_ok=True)
(provenance/'checkpoint_07_prearchive.json').write_text(json.dumps({
    'utc':datetime.now(timezone.utc).isoformat(),'checkpoint':7,'statement_count':len(rows),
    'statuses':counts,'pdf_sha256':sha,'pdf_pages':manifest['pdf_pages'],
    'visually_inspected_pages':len(manifest['pages']),'inspector_counts':manifest['inspector_counts'],
    'overfull_boxes':0,'unresolved_references':0,'progress_review':'Continue: main finite comparison and explicit character module are advancing.',
    'pending_source_fragments':pending},indent=2)+'\n')
print(record)
print('Recorded the hourly decision to continue and the156-statement ledger.')
