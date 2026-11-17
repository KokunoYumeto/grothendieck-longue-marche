"""Bind actual final32 visual observations and final engine output; no rendering."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import hashlib,json,re,shutil
root=Path(__file__).resolve().parents[1]
read=lambda rel:json.loads((root/rel).read_text())
sha=lambda rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()
m=read('records/checkpoint32_metrics.json')
render=read('records/pdf_qa/checkpoint32_final/render_manifest.json')
assert sha('LM4_SUCCESSOR_paper.pdf')==m['pdf_sha256']==render['pdf_sha256']
receipts=['work_A/review_checkpoint32_pages154_160.json','work_CE/checkpoint32_final_visual_receipt_161_165.json','work_DE/checkpoint32_visual_review_pages512_521.json']
individual=set([1,4,600,611])
for rel in receipts:
    r=read(rel);assert r['pdf_sha256']==m['pdf_sha256']
    for row in r['pages']:
        assert row.get('result',row.get('status'))=='PASS' and not row['issues']
        assert any(row.get(key) is True for key in ('individually_displayed_and_visually_viewed','actually_viewed_full_individual_image','individually_viewed_full_image'))
        assert sha(row['path'])==row['sha256'] and (root/row['path']).stat().st_size==row['bytes']
        individual.add(row['page'])
assert set(render['required_new_mathematical_pages'])<=individual
assert len(render['required_new_mathematical_pages'])==22
passes=max((root/'records/build_passes').iterdir(),key=lambda p:p.name)
stdout=max(passes.glob('build*.log'),key=lambda p:p.stat().st_mtime_ns)
audits=[]
for path in [root/'LM4_SUCCESSOR_paper.log',stdout]:
    text=path.read_text()
    warnings=[line for line in text.splitlines() if re.search(r'\bwarning\b',line,re.I) and not line.startswith(('Package:','File:'))]
    issues=[line for line in text.splitlines() if re.search(r'overfull|undefined|missing character|^!|fatal error|rerun to get',line,re.I)]
    notices=re.findall(r'^.*Underfull.*$',text,re.M)
    assert not warnings and not issues
    audits.append({'path':str(path.relative_to(root)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'warnings':warnings,'issues':issues,'underfull_notices':notices})
assert Counter(audits[0]['underfull_notices'])==Counter(audits[1]['underfull_notices'])
prior=read('records/checkpoint31_visual_review.json')['final_log_and_stdout_audits'][0]['underfull_notices']
assert Counter(prior)==Counter(audits[0]['underfull_notices'])
assert len(prior)==19
root_receipt={'reviewer':'root','pdf_sha256':m['pdf_sha256'],'individual_pages':[1,4,600,611],
 'individual_pngs':{f'records/pdf_qa/checkpoint32_final/page-{n:03d}.png':sha(f'records/pdf_qa/checkpoint32_final/page-{n:03d}.png') for n in [1,4,600,611]},
 'contacts':{f'records/pdf_qa/checkpoint32_final/contact-{n:02d}.png':sha(f'records/pdf_qa/checkpoint32_final/contact-{n:02d}.png') for n in range(1,6)},
 'each_contact_opened_as_actual_image':True,'observations':'All five full contact images, covering all45 rendered pages, inspected. Individual title/abstract page1, contents page4, new bibliography entry page600 and final reference-continuation page611 inspected at full resolution. No clipping, overlap or missing glyphs; the final page is a normal three-line bibliography-note continuation. All22 new mathematical pages have separately read individual peer receipts.','issues':[]}
p=root/'records/checkpoint32_root_visual_observations.json';assert not p.exists();p.write_text(json.dumps(root_receipt,indent=2)+'\n')
record={'recorded_at':datetime.now(timezone.utc).isoformat(),'visual_review':'PASS','pdf_sha256':m['pdf_sha256'],'rendered_pages':render['rendered_pages'],'required_math_pages':render['required_new_mathematical_pages'],'individually_inspected_pages':sorted(individual),'individual_page_review_receipts':{p:sha(p) for p in receipts+['records/checkpoint32_root_visual_observations.json']},'contact_sheets_inspected':5,'each_contact_sheet_opened_separately':True,'truncated_outputs_counted':False,'final_log_and_stdout_case_insensitive':'PASS','final_log_and_stdout_audits':audits,'underfull_scope':'The19 final underfull notices agree exactly as a multiset with the actual checkpoint31 final-log notices, including badness values and source line ranges. The final engine log and stabilized stdout agree exactly. No new underfull paragraph was introduced; visual review of every new mathematical page and all45 rendered pages found no layout defects.','recovery_scope':'Fresh611-page reconstruction; no reuse of the lost615-page PDF visual approval.'}
p=root/'records/checkpoint32_visual_review.json';assert not p.exists();p.write_text(json.dumps(record,indent=2)+'\n')
p=root/'records/checkpoint32_typesetting.txt';assert not p.exists();p.write_text('Visual review: PASS\nActual PDF SHA256:'+m['pdf_sha256']+'\n611pages;22new mathematical pages individually inspected;26individual pages overall;45rendered pages on5separately viewed contacts. Clean final log and stabilized stdout; exactly19unchanged prior underfull notices. This is fresh QA of the reconstructed PDF.\n')
p=root/'records/checkpoint32_root_formal_reviews.json'
backup=root/'records/environment_recovery32/checkpoint32_root_formal_reviews.before_final_delimiter_receipt.json'
assert not backup.exists();shutil.copy2(p,backup)
formal=json.loads(p.read_text())
rel='work_A/review_A101_final_delimiters_recovery32.md'
formal['independent_reviews'][rel]=sha(rel)
formal['final_delimiter_review']='Complete six-delimiter diff and all14-source lexical scan independently reviewed; source9224b80c has no mathematical change.'
p.write_text(json.dumps(formal,indent=2)+'\n')
print(json.dumps({'status':'PASS','pdf_sha256':m['pdf_sha256'],'pages':m['pages'],'required_new_math_pages':22,'individual_pages':len(individual),'contacts':5,'underfull_notices':19},indent=2),flush=True)
