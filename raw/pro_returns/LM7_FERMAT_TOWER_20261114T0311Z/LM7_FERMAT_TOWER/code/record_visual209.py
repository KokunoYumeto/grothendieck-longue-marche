"""Record the visual inspection actually completed on checkpoint209."""
from pathlib import Path
import hashlib,json,datetime,shutil
B=Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
V=json.loads("{\"contacts\":[\"qa/contact_385_400.jpg\",\"qa/contact_401_416.jpg\",\"qa/contact_417_432.jpg\",\"qa/contact_433_448.jpg\",\"qa/contact_449_464.jpg\",\"qa/contact_465_480.jpg\",\"qa/contact_481_496.jpg\",\"qa/contact_497_512.jpg\",\"qa/contact_513_528.jpg\",\"qa/contact_529_544.jpg\",\"qa/contact_545_560.jpg\",\"qa/contact_561_576.jpg\",\"qa/contact_577_592.jpg\",\"qa/contact_593_608.jpg\",\"qa/contact_609_613.jpg\"],\"observations\":[\"Pages385–416: all visible text blocks, equations and tables fit the page; no clipping, overlap or unexpected blank page observed at contact resolution.\",\"Pages417–448: formulas, headings and class-group tables remain within margins; no clipping, overlap or blank page observed at contact resolution.\",\"Pages449–480: all equations and dense matrix/table layouts fit their blocks; no overlap or clipping observed at contact resolution.\",\"Pages481–512: the equation and table blocks remain aligned and contained; no page-layout defect observed at contact resolution.\",\"Pages513–544: dense Smith matrices, tables and equations remain within margins with no overlap observed at contact resolution.\",\"Pages545–576: all current theorem headings and displays fit; no overlap or clipping at contact resolution. New material begins later and receives separate detailed review.\",\"Pages577–608: proof displays and bibliography columns fit the pages; no clipping, overlap or empty pages observed at contact resolution.\",\"Pages609–613: bibliography entries fit their columns; page613 is a normal short final page. Detail587: statement and complete coefficient formulas fit cleanly.\",\"Details588–593: E108 displays, character table, proof paragraphs and page continuations are fully legible; no clipping, overlap or detached equation numbers observed.\",\"Details594–597: E109 coefficient maps, Johnson projector and cycle comparison formulas are fully visible and aligned; no layout defects observed.\",\"Details598–605: E110 norm identities, aligned coordinate maps, character matrix and all proof continuations fit; corrected displays E110.1/E110.2/E110.10 are fully visible. No clipping or overlap observed.\",\"Detail606: reference entries and wrapped source-reading notes are fully visible; no bibliography layout defects observed.\"],\"details\":[\"qa/detail209_page_587.jpg\",\"qa/detail209_page_588.jpg\",\"qa/detail209_page_589.jpg\",\"qa/detail209_page_590.jpg\",\"qa/detail209_page_591.jpg\",\"qa/detail209_page_592.jpg\",\"qa/detail209_page_593.jpg\",\"qa/detail209_page_594.jpg\",\"qa/detail209_page_595.jpg\",\"qa/detail209_page_596.jpg\",\"qa/detail209_page_597.jpg\",\"qa/detail209_page_598.jpg\",\"qa/detail209_page_599.jpg\",\"qa/detail209_page_600.jpg\",\"qa/detail209_page_601.jpg\",\"qa/detail209_page_602.jpg\",\"qa/detail209_page_603.jpg\",\"qa/detail209_page_604.jpg\",\"qa/detail209_page_605.jpg\",\"qa/detail209_page_606.jpg\"]}")
pdf=B/'LM7_FERMAT_TOWER_paper.pdf'
expected='0197634cad8fd1609f08450038762904db6f219357cfefa9fdafc0a28bfb1c29'
assert sha(pdf)==expected
assert len(V['contacts'])==15 and len(V['details'])==20
A=json.loads((B/'qa/visual209_a.json').read_text())
D=json.loads((B/'qa/visual209_d.json').read_text())
assert A['pdf']['sha256']==D['pdf_sha256']==expected
seen=set()
for x in A['reviewed_files']:
 assert x['actually_viewed'] and sha(B/x['file'])==x['sha256']
 seen.update(range(x['pages'][0],x['pages'][1]+1))
for x in D['images']:
 assert x['actually_viewed'] and sha(Path(x['path']))==x['sha256']
 if 'contact_' in x['path']: seen.update(x['pages'])
images=[]
for name in V['contacts']+V['details']:
 p=B/name
 if 'contact_' in name:
  a,z=map(int,p.stem.split('_')[-2:]); pages=list(range(a,z+1)); seen.update(pages)
 else: pages=[int(p.stem.split('_')[-1])]
 images.append(dict(file=name,sha256=sha(p),pages=pages,actually_viewed=True))
assert seen==set(range(1,614))
record=dict(reviewer='/root',checkpoint=209,pdf_sha256=expected,pages=613,
 reviewed_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 scope='15 contact sheets, pages385–613, and all20 110-dpi detail images587–606 actually viewed.',
 images=images,observations=V['observations'],status='PASS',
 copyediting_note='Some source-adjacent prose spaces remain absent in E108–E110; this review asserts layout and visibility, not flawless copy editing.')
(B/'qa/visual209_root.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
review=f"""# Checkpoint209 visual review

PDF SHA256: `{expected}`.

The 613-page PDF completed three LuaLaTeX passes and BibTeX. The build certificate records no undefined references or citations, missing characters, or overfull boxes. All613 pages rendered. The automated check found all209 statement headings, no empty page, and no word outside its safety border.

All39 current contact sheets were actually viewed: a_structure reviewed pages1–192, d_galois pages193–384, and root pages385–613. Exact image hashes and scoped observations are in visual209_a.json, visual209_d.json and visual209_root.json. These contact-resolution inspections found no clipping, overlap, unexpected blank page or missing text block.

All25 current detail images at110 dpi were also actually viewed: d_galois inspected pages204–208 and root pages587–606. D.59's corrected lower-bound integer is fully visible. E108's coefficient formulas, E109's actual affine and Johnson comparisons, and E110's norm-coordinate maps are fully visible and fit their margins. The three repaired displays E110.1, E110.2 and E110.10 were reviewed in this rendered form.

A few missing prose spaces in source-adjacent phrases in E108–E110 are recorded for the next editorial pass. No claim of flawless copy editing is made. The retained first-build failure and its exact layout-only correction are code/checkpoint209_first_build/ and ledger/checkpoint209_layout_amendment.json. The earlier205 review was preserved under qa/history/checkpoint205_before209/. Visual review supplements the separate mathematical proof reads, source checks, fresh executions and peer audits.
"""
for a,b in [('All613','All 613'),('all209','all 209'),('All39','All 39'),('All25','All 25'),('at110','at 110'),('pages1','pages 1'),('pages193','pages 193'),('pages385','pages 385'),('pages204','pages 204'),('pages587','pages 587'),('earlier205','earlier 205')]:review=review.replace(a,b)
(B/'qa/visual_review.md').write_text(review)
src=B.parent
route=B/'code/source_routes209';route.mkdir(exist_ok=True)
copied=[]
for ext in ('.py','.out','.json'):
 p=src/('root_coleman_exact_public_pdf'+ext)
 assert p.is_file()
 q=route/p.name;shutil.copy2(p,q)
 copied.append(dict(file=str(q.relative_to(B)),sha256=sha(q)))
log=B/'ledger/d_original_source_recheck.md'
note="""\n## Checkpoint209: exact public Coleman PDF route\n\nThe exact PDF URL advertised by OpenAlex was requested once by ordinary HTTPS GET. The server returned HTTP200 with text/html (1153 bytes), SHA256 2b17e72e81f1232efb2b42f0f91ca2d5feeb8214478556b00b41263c57d9485f. No PDF was obtained or read through this route. The owned program, actual output and JSON record are preserved in code/source_routes209/. No authentication, altered challenge headers, challenge handling or access-control bypass was used. Coleman1989 remains unverified at the original-source level.\n"""
if note not in log.read_text(): log.write_text(log.read_text()+note)
print(json.dumps(dict(status='PASS',pdf_sha256=expected,all_contact_pages=613,root_contact_images=15,root_detail_images=20,total_current_details=25,visual_record_sha256=sha(B/'qa/visual209_root.json'),source_route_records=copied),indent=2))

