"""Prepare source-based heading witnesses; close only after final visual review.

prepare reads source/TeX metadata, never a PDF. queue --final is run only after
the full build is declared stable. record accepts actual human observations and
rejects evidence whose PDF or image hashes changed.
"""
from pathlib import Path
import argparse,csv,hashlib,json,re
import editorial,verify_sources

ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/'work/data'
BUILD=ROOT/'work/build'
EVIDENCE=ROOT/'work/visual_repair_proofs/heading_final'
INVENTORY=DATA/'heading_witness_inventory.json'
REPORT=DATA/'heading_closure_final.json'
READERS={
 'LM_FR_diplomatique':('fr',0),
 'LM_FR_corrige_apparat':('fr',1),
 'LM_FR_texte_de_lecture':('fr',2),
 'LM_EN_corrected_apparatus':('en',1),
 'LM_EN_reading':('en',2)}
NOTES=[
 ('m582','LM_P050','140-2',492,0,[234,235],230),
 ('m599','LM_P051','140-2',508,0,[239,240],230),
 ('m725','LM_P066','140-3',73,0,[305,306],190),
 ('m1108','LM_C3-416-434','140-3',416,1,[513,514],230),
 ('m1576','LM_C4-115-133','140-4',132,0,[793,794],590)]

def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha_file(p):return sha_bytes(p.read_bytes())
def sha_text(s):return sha_bytes(s.encode())
def relative(p):return p.relative_to(ROOT).as_posix()
def read_json(p):return json.loads(p.read_text())
def write_json(p,obj):
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def raw_path(package,language):
 return ROOT/('sources/fr/texts/'+package+'.tex' if language=='fr' else 'sources/en/packages/'+package+'_en.tex')
def source_margins(package,language,scan):
 p=raw_path(package,language);s=p.read_text()
 return p,s,[m for m in editorial.spans(s,{'margin'}) if editorial.at_scan(s,m['start'])==scan]
def meta_candidates(marks,package,scan):
 return [m for m in marks if m['kind']=='margin' and m['package']==package and int(m['scan'])==scan]

def prepare():
 marks={lang:read_json(BUILD/(lang+'_source_marks.json')) for lang in ('fr','en')}
 witnesses=[]
 for ref,package,cote,scan,ordinal,oldpages,depth in NOTES:
  p,raw,ms=source_margins(package,'fr',scan);m=ms[ordinal]
  candidates=meta_candidates(marks['fr'],package,scan)
  target=candidates[ordinal]
  assert target['argument'].startswith((r'\diagram{',r'\figure{')),(ref,target['argument'][:60])
  witnesses.append(dict(id='note-'+ref,kind='marginal-note',readers=['LM_FR_diplomatique'],
    package=package,cote=cote,scan=scan,source_margin_ordinal=ordinal+1,
    source_path=relative(p),source_file_sha256=sha_file(p),
    source_line=raw.count('\n',0,m['start'])+1,
    raw_argument_sha256=sha_text(m['argument']),
    master_argument_sha256=sha_text(target['argument']),
    prior_source_id=target['id'],prior_note_ref=ref,prior_pages=oldpages,
    body_kind='diagram' if target['argument'].startswith(r'\diagram') else 'sketch',
    native_depth_pt=depth))
 for language in ('fr','en'):
  package='LM_C3-530-548';scan=548;cote='140-3'
  token='préliminaires' if language=='fr' else 'Preliminary'
  p,raw,ms=source_margins(package,language,scan)
  m=next(x for x in ms if token in x['argument'])
  target=next(x for x in meta_candidates(marks[language],package,scan) if token in x['argument'])
  witnesses.append(dict(id='section-V-'+language,kind='section-start',
    readers=[b for b,(lang,_) in READERS.items() if lang==language],
    package=package,cote=cote,scan=scan,source_path=relative(p),
    source_file_sha256=sha_file(p),source_line=raw.count('\n',0,m['start'])+1,
    raw_argument_sha256=sha_text(m['argument']),
    master_argument_sha256=sha_text(target['argument']),prior_source_id=target['id'],
    preliminary_token=token,intro_token='Soit donc' if language=='fr' else 'So let',
    native_depth_pt=250))
 write_json(INVENTORY,dict(schema='heading-witness-inventory-v1',
   status='PENDING_FINAL_BUILD',scope='Five diplomatic marginal-note starts and section V/preliminary-data start in five primary readers.',
   source_mark_snapshots={lang:sha_file(BUILD/(lang+'_source_marks.json')) for lang in ('fr','en')},
   expected_final_witnesses=10,witnesses=witnesses))
 if not REPORT.exists():
  write_json(REPORT,dict(schema='heading-closure-v1',status='PENDING_FINAL_BUILD',
    expected_witnesses=10,readers=[],witnesses=[],pass_count=0))
 print('Prepared five marginal-note witnesses and five primary-reader section witnesses; no PDF was inspected.')

def body_and_margin_refs(path,form):
 s=path.read_text();m=re.search(r'^% COMMON MASTER BODY SHA256 ([0-9a-f]{64})\n',s,re.M)
 assert m,'Missing common-body header'
 body=s[m.end():s.rfind(r'\end{document}')]
 assert sha_text(body)==m[1],'Common-body hash mismatch'
 old=verify_sources.LINK_KINDS.copy()
 try:
  verify_sources.LINK_KINDS['margin']='margin'
  found,problems=verify_sources.expected_mark_ids(body,form)
 finally:verify_sources.LINK_KINDS=old
 assert not problems,problems
 margins=[key for key,kind in found.items() if kind=='margin']
 return m[1],{key:'m'+str(i+1) for i,key in enumerate(margins)}

def pages_for_scan(path,cote,scan):
 with path.open() as f:rows=list(csv.DictReader(f,delimiter='\t'))
 match=next(r for r in rows if r['cote']==cote and int(r['scan'])==scan)
 return [int(x) for x in match['physical_pages'].split(',') if x]

def note_location(pdf,ref,pages):
 import fitz
 candidates=sorted({q for p in pages for q in (p-1,p,p+1,p+2) if 1<=q<=len(pdf)})
 for number in candidates:
  page=pdf[number-1];refs=[fitz.Rect(w[:4]) for w in page.get_text('words') if w[4]==ref]
  for heading in page.search_for('Note marginale.'):
   close=[r for r in refs if -.5<=r.x0-heading.x1<=60 and abs(r.y0-heading.y0)<16]
   if close:return number,heading,{'note_ref_bbox':list(close[0])}
 return None,None,{}

def section_location(pdf,spec,pages):
 import fitz
 candidates=sorted({q for p in pages for q in (p-1,p,p+1) if 1<=q<=len(pdf)})
 for number in candidates:
  page=pdf[number-1];intro=page.search_for(spec['intro_token']);prelim=page.search_for(spec['preliminary_token'])
  roman=[fitz.Rect(s['bbox']) for b in page.get_text('dict')['blocks'] if 'lines' in b
    for l in b['lines'] for s in l['spans'] if s['text'].strip()=='V']
  for v in roman:
   below=[r for r in intro if 0<r.y0-v.y0<180]
   nearby=[r for r in prelim if abs(r.y0-v.y0)<180]
   if below and nearby:return number,v,{'intro_bbox':list(below[0]),'preliminary_bbox':list(nearby[0])}
 return None,None,{}

def render_evidence(pdf,reader,spec,number,heading,pdf_sha256):
 import fitz
 page=pdf[number-1];d=EVIDENCE/pdf_sha256[:16]/reader;d.mkdir(parents=True,exist_ok=True)
 stem=spec['id']+'_p'+str(number).zfill(4);items=[]
 full=d/(stem+'_full.png')
 page.get_pixmap(matrix=fitz.Matrix(900/page.rect.width,900/page.rect.width),alpha=False).save(full)
 items.append(dict(image=relative(full),sha256=sha_file(full),basis='full page at900px'))
 crop=d/(stem+'_native.png')
 clip=fitz.Rect(35,max(35,heading.y0-24),page.rect.width-25,
   min(page.rect.height-35,heading.y0+spec['native_depth_pt']))
 page.get_pixmap(matrix=fitz.Matrix(3,3),clip=clip,alpha=False).save(crop)
 items.append(dict(image=relative(crop),sha256=sha_file(crop),basis='native3x heading and opening body crop',clip=list(clip)))
 return items

def queue(final):
 if not final:raise SystemExit('queue requires --final after the complete build is declared stable.')
 import fitz
 inventory=read_json(INVENTORY);out=dict(schema='heading-closure-v1',
   status='PENDING_VISUAL',expected_witnesses=10,readers=[],witnesses=[],pass_count=0,
   method='Resolve the exact margin argument in current source-mark metadata; select the current diplomatic/form branches to derive note references; locate headings in source-scan page ranges; require actual final-PDF image review.')
 for lang in ('fr','en'):
  assert inventory.get('source_mark_snapshots',{}).get(lang)==sha_file(BUILD/(lang+'_source_marks.json')), 'Source assembly changed: rerun prepare before queue --final.'
 marks={lang:read_json(BUILD/(lang+'_source_marks.json')) for lang in ('fr','en')}
 for reader,(lang,form) in READERS.items():
  path=BUILD/(reader+'.pdf');tex=path.with_suffix('.tex');scanmap=path.with_suffix('.lm-scans.tsv')
  initial=sha_file(path);pdf=fitz.open(path)
  body_sha,refs=body_and_margin_refs(tex,form)
  out['readers'].append(dict(file=path.name,sha256=initial,pages=len(pdf),tex_sha256=sha_file(tex),
    actual_body_sha256=body_sha,source_marks_sha256=sha_file(BUILD/(lang+'_source_marks.json')),
    scan_map_sha256=sha_file(scanmap)))
  for spec in inventory['witnesses']:
   if reader not in spec['readers']:continue
   candidates=[m for m in meta_candidates(marks[lang],spec['package'],spec['scan'])
     if sha_text(m['argument'])==spec['master_argument_sha256']]
   assert candidates,('Source margin identity missing',reader,spec['id'])
   target=next((m for m in candidates if m['id'] in refs),candidates[0])
   pages=pages_for_scan(scanmap,spec['cote'],spec['scan'])
   row={k:v for k,v in spec.items() if k!='readers'}
   row.update(key=reader+'|'+spec['id'],reader=reader,pdf_sha256=initial,
     source_id=target['id'],source_scan_pages=pages,status='PENDING_VISUAL')
   if spec['kind']=='marginal-note':
    assert target['id'] in refs
    row['note_ref']=refs[target['id']]
    number,heading,extra=note_location(pdf,row['note_ref'],pages)
   else:number,heading,extra=section_location(pdf,spec,pages)
   row.update(extra)
   if number is None:row.update(status='LOOKUP_FAILED',evidence=[])
   else:
    row.update(heading_page=number,heading_bbox=list(heading),
      evidence=render_evidence(pdf,reader,spec,number,heading,initial))
    if spec['kind']=='marginal-note':
     graphics=[x['rect'] for x in pdf[number-1].get_drawings()
       if x['rect'].y0>heading.y1+1 and x['rect'].y0<heading.y1+160
       and (x['rect'].width>.3 or x['rect'].height>.3)]
     row['same_page_graphic_candidate']=bool(graphics)
     row['first_graphic_bbox']=list(min(graphics,key=lambda r:r.y0)) if graphics else None
   out['witnesses'].append(row)
  assert sha_file(path)==initial,('PDF changed during queue',reader)
  pdf.close()
 assert len(out['witnesses'])==out['expected_witnesses']
 for r in out['readers']:assert sha_file(BUILD/r['file'])==r['sha256'],'PDF changed after rendering'
 if REPORT.exists():
  previous=read_json(REPORT)
  fingerprint=sha_text(json.dumps(previous.get('readers',[]),sort_keys=True))[:16]
  write_json(DATA/'heading_closure_history'/(fingerprint+'.json'),previous)
 write_json(REPORT,out)
 print('Queued',len(out['witnesses']),'hash-bound final witnesses; all remain unreviewed.')
 for r in out['witnesses']:print(r['key'],r.get('heading_page'),r['status'])

def record(path):
 report=read_json(REPORT);notes=read_json(path);rows={r['key']:r for r in report['witnesses']}
 assert set(notes)<=set(rows),'Unknown witness observation'
 for r in report['readers']:assert sha_file(BUILD/r['file'])==r['sha256'],'Final PDF hash changed'
 for key,value in notes.items():
  r=rows[key];assert r['status']!='LOOKUP_FAILED'
  for e in r['evidence']:assert sha_file(ROOT/e['image'])==e['sha256'],'Evidence image hash changed'
  value={'status':'PASS','observation':value} if isinstance(value,str) else value
  assert value['status'] in ('PASS','ISSUE') and len(value['observation'])>20
  r.update(status=value['status'],observation=value['observation'],reviewer='editorial',
    review_basis='Actual final-PDF full-page and native heading/body images')
 report['pass_count']=sum(r['status']=='PASS' for r in rows.values())
 report['status']='PASS' if report['pass_count']==report['expected_witnesses'] else ('ISSUES' if any(r['status']=='ISSUE' for r in rows.values()) else 'PENDING_VISUAL')
 write_json(REPORT,report);print(report['status'],report['pass_count'],'/',report['expected_witnesses'])

def main():
 p=argparse.ArgumentParser();sub=p.add_subparsers(dest='command',required=True)
 sub.add_parser('prepare');q=sub.add_parser('queue');q.add_argument('--final',action='store_true')
 r=sub.add_parser('record');r.add_argument('--observations',type=Path,required=True)
 args=p.parse_args()
 if args.command=='prepare':prepare()
 elif args.command=='queue':queue(args.final)
 else:record(args.observations)
if __name__=='__main__':main()
