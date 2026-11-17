"""Record only root's actually displayed final-edition images and retraction."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
def bind(rel):
    raw=(ROOT/rel).read_bytes()
    return {'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

pdf=bind('LM4_SUCCESSOR_paper.pdf')
assert pdf['sha256']=='c5be64cdf00bf3a384a3328de004453b3e3496f969822af26fbf6df88af0c8a2'
manifest=bind('records/pdf_qa/checkpoint37_final/render_manifest.json')
assert manifest['sha256']=='b23de512e2e8959efe471bfa993cdb1efdefdccebb6b7e8f34a0bbcf1c89c0f1'
observations={
    1:'Full individual image displayed. Title, GPT-6 Astra/OpenAI credit, date, explicit INCOMPLETE status and the first abstract page are legible and within margins.',
    2:'Full individual image displayed. Dense abstract continuation, superscripts and mathematical symbols are legible; no clipping or overlap.',
    3:'Full individual image displayed. Abstract continuation has consistent text margins and clear mathematical notation, with the footer unobstructed.',
    4:'Full individual image displayed. The final dense abstract continuation and all long prose lines are visible without collision or truncation.',
    5:'Full individual image displayed. Abstract conclusion and contents page are clear; the wrapped Part C entry, leaders and right-aligned page numbers do not overlap.',
    6:'Full individual image displayed. Scope conventions, Part A heading, normalization display and A.1 text/citations are legible; no margin overflow or clipped symbols.',
    7:'Full individual image displayed. Existing A.2/A.3 displays, inverse-limit notation, proof ending and headings have clear spacing and readable subscripts.',
    234:'Full individual image displayed. The line following A.127.27 visibly includes Bu in L D W Bu Fb inverse. Boxed C3 parameter and equivalences are legible. The alleged omission was a false alert, independently checked against complete PDF text and source in chunk d0e5bc.',
    246:'Full individual image displayed. Repaired canonical U/V/T/beta display occupies three centered rows entirely inside the text area. Provenance paths, Part B transition and B.1 opening are legible without overlap.',
    708:'Full individual image displayed. References heading, hanging paragraphs, source-scope notes and first bibliography entries are legible and remain inside the margins.',
    719:'Full individual image displayed. Final bibliography entries and the explicit scope/failed-screenshot note are completely visible; no clipping or overlap.'
}
pages=[]
for n,observation in observations.items():
    row=bind(f'records/pdf_qa/checkpoint37_final/page-{n:03d}.png')
    row.update(page=n,actually_viewed_individually=True,result='PASS',issues=[],observation=observation)
    if n==6:
        row['nonblocking_notes']=['An existing prose/citation boundary has tight spacing; the citation and sentence are fully legible. No mathematical or layout repair is required.']
    pages.append(row)
contacts=[]
for n in range(1,7):
    row=bind(f'records/pdf_qa/checkpoint37_final/contact-{n:02d}.png')
    row.update(result='PASS',issues=[],actually_viewed_separately=True,
               observation='This contact sheet was opened as its own actual image output; every page is within its frame with no visible clipping, overlapping text or displaced equation labels.')
    contacts.append(row)
record={'reviewer':'/root','recorded_at':datetime.now(timezone.utc).isoformat(),
        'pdf_sha256':pdf['sha256'],'render_manifest_sha256':manifest['sha256'],
        'truncated_outputs_counted':False,'pages':pages,'contacts':contacts,
        'scope':'Eleven final pages actually viewed as individual image blocks; all six contact sheets separately displayed. Earlier truncated image outputs were not counted. The actual final PDF/render did not change after the retracted Bu alert.'}
with (ROOT/'records/checkpoint37_root_visual_observations.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
retraction={'recorded_at':datetime.now(timezone.utc).isoformat(),
    'result':'FALSE_ALERT_RETRACTED_NO_SOURCE_PDF_OR_RENDER_CHANGE',
    'root_exact_source_and_complete_page_text_read_chunk':'d0e5bc',
    'root_page234_individually_viewed':True,
    'source':bind('sections/a_elliptic_brunnian_cyclic_involution.tex'),
    'pdf':pdf,'render_manifest':manifest,
    'agent_retraction':bind('work_DE/checkpoint37_A127_Bu_alert_retraction.json'),
    'extra_preservation_record':bind('records/checkpoint37_before_A127_Bu_correction_observed.json'),
    'extra_preservation_actual_exit_code':0,'extra_preservation_tool_chunk':'a77829',
    'explanation':'The preservation directory and its earlier reason were written while a missing-factor alert was pending. Exact source and PDF reinspection disproved that alert. All copied bytes remain retained, but there is no correction, no new edition, and no extra build/render. The running size estimate still measures the unchanged final PDF.'}
with (ROOT/'records/checkpoint37_root_A127_Bu_alert_retraction.json').open('x') as stream:
    json.dump(retraction,stream,indent=2);stream.write('\n')
print(json.dumps({'result':'ACTUAL_ROOT_IMAGES_RECORDED','individual_pages':list(observations),'contacts':len(contacts),'pdf_sha256':pdf['sha256']}))
