"""Record the root agent's completed checkpoint-214 visual inspection.
This program hashes the images identified by the prior manual inspection; it
does not infer a visual review from a successful render.
"""
from pathlib import Path
import hashlib, json
BASE=Path(__file__).resolve().parents[2]
PDF=BASE/'LM7_FERMAT_TOWER_paper.pdf'
EXPECTED='dffcac360a8d8f7c54645f21a20533ec8f7f5e104f5dcc27e56974f303374d77'
assert hashlib.sha256(PDF.read_bytes()).hexdigest()==EXPECTED
observed=json.loads("{\"contacts_seen\":[1,17,33,49,65,81,97,113,129,145,161,177,193,209,225,241,257,273,289,305,321,337,353,369,385,401,417,433,449,465,481,497,513,529,545,561,577,593,609,625,641],\"details_seen\":[209,210,211,212,213,214,215,216,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643],\"prose_spacing_followup\":{\"statement\":\"E.111\",\"pages\":[615,617,618],\"examples\":[\"scans172\",\"folios733v\",\"Sections2--4\",\"Proposition3.1\",\"Hilbert90\"]}}")
qa=json.loads((BASE/'qa/pdf_qa.json').read_text())
assert qa['sha256']==EXPECTED and qa['pages']==643
assert observed['contacts_seen']==list(range(1,644,16))
assert observed['details_seen']==list(range(209,217))+list(range(613,644))
paths=[BASE/p for p in qa['contact_sheets']]
paths += [BASE/'qa'/f'detail214_page_{n:03d}.jpg' for n in observed['details_seen']]
record={'pdf_sha256':EXPECTED,'pages':643,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode), root','contact_sheets_actually_viewed':41,'detail_images_actually_viewed':39,'observations':observed,'layout_findings':'No clipping, overlapping text, missing block, unexpected blank page, or obscured display was observed. Matrices, equation numbers, inverse maps and reference entries fit their margins. Prose citation spacing needs the recorded later editorial correction.','images':[{'path':str(p.relative_to(BASE)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]}
(BASE/'qa/visual214_root.json').write_text(json.dumps(record,indent=2)+'\n')
review="""# Checkpoint214 visual review

PDF SHA256: `dffcac360a8d8f7c54645f21a20533ec8f7f5e104f5dcc27e56974f303374d77`.

The 643-page PDF completed three LuaLaTeX passes and BibTeX. The build certificate records no undefined reference or citation, missing character, or overfull box. All 643 pages rendered; the structural check found all 214 statement headings, no empty page, and no word outside its safety border.

Root actually viewed all 41 current contact sheets, covering pages 1–643, and all 39 current detail images, covering pages 209–216 and 613–643. Exact image hashes and the manually supplied inspection scope are in visual214_root.json. The details include all of D.60, E.111–E.114, and the bibliography. No clipping, overlap, missing text block, unexpected blank page, or obscured equation was observed. The large matrices, equation numbers, coefficient maps and inverse formulas fit their margins.

The inspection found missing prose spaces in some theorem and manuscript citations in E.111, E.112, E.114 and bibliography notes. These are recorded for the next editorial build; no claim of flawless copy editing is made. The exact mathematical statements, coefficient formulas and certificate outputs were reviewed separately. The previous 209 review and images are preserved under qa/history/checkpoint209_before214/.
"""
(BASE/'qa/visual_review.md').write_text(review)
print(json.dumps({'pdf_sha256':EXPECTED,'contact_sheets_actually_viewed':41,'detail_images_actually_viewed':39,'record_sha256':hashlib.sha256((BASE/'qa/visual214_root.json').read_bytes()).hexdigest()},indent=2))

