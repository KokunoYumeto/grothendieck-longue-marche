"""Record the root assistant's actual visual inspection of build 229.

The list was supplied after the images were opened and inspected. This
program checks the identity of that evidence; it does not perform visual QA.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

BASE=Path(__file__).resolve().parents[1];QA=BASE/'qa'
EXPECTED='f6307cb0c8d6ad23873f51fe60ce306d9c73f0bc89ae30702fa6c4e0dd5b10af'
PAGES=[1,2,42,46,47,51,55,56,250,251,252,253,254,255,256,257,
       269,273,274,275,276,277,278,724,725,726,727,728,729,730,
       731,732,733,734,735,736,737,738,740,748]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    qa=json.loads((QA/'pdf_qa.json').read_text())
    detail=json.loads((QA/'detail229_manifest.json').read_text())
    assert sha(BASE/'LM7_FERMAT_TOWER_paper.pdf')==qa['sha256']==EXPECTED
    assert qa['pages']==748 and len(qa['contact_sheets'])==47
    assert detail['pdf_sha256']==EXPECTED
    assert [x['page'] for x in detail['images']]==PAGES
    contacts=[{'path':p,'sha256':sha(BASE/p)} for p in qa['contact_sheets']]
    for x in detail['images']:
        assert sha(BASE/x['path'])==x['sha256']
    result={'status':'PASS','pdf_sha256':EXPECTED,'pdf_pages':748,
            'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode), root assistant',
            'basis':'Actual image-tool inspection of every listed image',
            'contact_sheets':contacts,'detail_images':detail['images'],
            'all_pages_inspected_in_contact_sheets':True,
            'observed_layout_defects':[],
            'truncated_prior_return_used_as_evidence':False,
            'truncated_return_resolution':'The earlier return for pages 449-512 was truncated and excluded. All four contact sheets for those pages were reopened and inspected before this record.',
            'mathematical_proof_review_claimed_here':False,
            'recorded_utc':datetime.now(timezone.utc).isoformat()}
    (QA/'visual229_root.json').write_text(json.dumps(result,indent=2)+'\n')
    review=f'''# Actual visual review of the assembled 229-statement paper

PDF SHA256: `{EXPECTED}`. Pages: 748.

All 47 contact sheets, covering pages 1-748, were opened and inspected by the root assistant. All 40 detail images listed in visual229_root.json were separately inspected at 110 dpi: pages 1-2, 42, 46-47, 51, 55-56, 250-257, 269, 273-278, 724-738, 740 and 748. These include the entire newly integrated D66, E123 and E124 proofs and their boundaries, the amended D13, D19 and E23 paragraphs, the title and notation table, section transitions, and the final bibliography page.

No clipping, overlap, broken table, unintended blank page, missing glyph or displaced equation label was observed. Equations, matrices, arrows, source filenames and page numbers remained legible in the detail images. The structural renderer separately checked all 229 statement headings and every page boundary. Mathematical proof reviews and exact arithmetic replays are recorded separately.

The earlier image-tool return for pages 449-512 was truncated. Its four contact sheets were excluded from the inspection record until they were reopened and actually inspected. No truncated return was counted as visual evidence. Prior visual reviews and frozen author proofs remain in the archive history.
'''
    (QA/'visual_review.md').write_text(review)
    print(json.dumps({'status':'PASS','pdf_sha256':EXPECTED,
                      'contacts_inspected':47,'details_inspected':40,
                      'visual_record_sha256':sha(QA/'visual229_root.json')},indent=2))

if __name__=='__main__':main()
