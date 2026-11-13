#!/usr/bin/env python3
"""Freeze the actual revision512 heading observations and their evidence bytes.

The explicit page lists below select already-written actual review statements;
they do not turn machine candidates into visual findings.
"""
from pathlib import Path
import collections
import csv
import hashlib
import json
import re
import shutil
import unicodedata
import fitz

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'work/data/generated_heading_known_witnesses.json'
INPUTS=ROOT/'work/data/generated_heading_revision512_inputs'
IMAGES=ROOT/'work/visual_repair_proofs/generated_heading_known_before'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p):return p.resolve().relative_to(ROOT).as_posix()
def read(p):return json.loads((ROOT/p).read_text())

def main():
    INPUTS.mkdir(parents=True,exist_ok=True);IMAGES.mkdir(parents=True,exist_ok=True)
    inputs={};rows=[];docs={};pdf_hashes={}
    def snapshot(path):
        p=ROOT/path;target=INPUTS/(sha(p)[:12]+'_'+p.name)
        if not target.exists():shutil.copy2(p,target)
        inputs[path]={'path':rel(target),'sha256':sha(target),'original_path':path}
        return json.loads(target.read_text())
    def document(book):
        if book not in docs:
            p=ROOT/'work/build'/(book+'.pdf');pdf_hashes[book]=sha(p);docs[book]=fitz.open(p)
        return docs[book]
    def add(record,kind,origin):
        row=dict(record);book=Path(row.get('reader',row.get('book',''))).stem
        pages=row.get('pages',[]);assert book and pages
        doc=document(book);assert row.get('pdf_sha256',pdf_hashes[book])==pdf_hashes[book]
        page=int(pages[0]);next_text=unicodedata.normalize('NFKC',doc[page].get_text()) if page<len(doc) else ''
        anchors=re.findall(r'140-[1-4]-s\d{3,4}-[DI]\d{3}',next_text)
        cote=row.get('cote');scan=row.get('scan')
        if not cote or scan is None:
            assert anchors,(book,page)
            m=re.match(r'(140-[1-4])-s(\d+)-',anchors[0]);cote=m[1];scan=int(m[2])
        scan=int(scan);prefix=f'{cote}-s{scan:03d}-'
        anchor=next((a for a in anchors if a.startswith(prefix)),None)
        if kind!='scan_range':assert anchor,(book,page,cote,scan)
        source_images=[]
        for image in row.get('images',[]):
            p=ROOT/image['path'];digest=sha(p);assert digest==image['sha256'],p
            target=IMAGES/(digest+'.png')
            if not target.exists():shutil.copy2(p,target)
            source_images.append({'path':rel(target),'sha256':digest,'original_path':image['path']})
        assert source_images,(book,page)
        rows.append({'id':f'GHKNOWN-{book}-{cote}-s{scan:03d}-{kind}','reader':book,'heading_kind':kind,
                     'cote':cote,'scan':scan,'package':row.get('package'),'before_pdf_sha256':pdf_hashes[book],
                     'before_pages':pages,'before_observation':row['observation'],'before_reviewer':row.get('reviewer',''),
                     'before_images':source_images,'first_entry_anchor':anchor,'observation_source':inputs[origin],
                     'evidence_note':'Frozen supporting evidence; actual inspection scope is exactly that stated in the attributed before_observation, including any explicit distinction between viewed full pages and preserved native crops.'})
    for path,kind in [('work/data/apparatus_heading_orphans_revision512.json','apparatus'),
                      ('work/data/range_heading_orphans_revision512.json','scan_range'),
                      ('work/data/retained_heading_typeset_release512_witnesses.json','retained_doubts')]:
        for row in snapshot(path):
            k=kind
            if ('RULE' in row.get('id','') or 'rule-only' in row.get('observation','')) and kind!='scan_range':k+='_rule_only'
            add(row,k,path)
    notes_specs=[('LM_FR_texte_de_lecture','work/verification/LM_FR_texte_de_lecture/notes_revision512_glossary.json','assistant/glossary',
                  [44,97,106,122,123,180,311,427,430,497,506,559,566],{430,506}),
                 ('LM_EN_reading','work/data/en_read_release512_root_observations.json','root',
                  [131,228,240,244,245,270,314,430,605,634],{131,228,430,605}),
                 ('LM_FR_texte_de_lecture','work/data/fr_read_release512_root_observations.json','root',[632],set())]
    for book,path,reviewer,pages,rule_pages in notes_specs:
        notes=snapshot(path);document(book)
        for page in pages:
            observed=[n for n in (page,page+1) if str(n) in notes]
            assert observed,(book,page)
            observation=' | '.join('Physical'+str(n)+': '+notes[str(n)] for n in observed)
            images=[]
            for n in observed:
                p=ROOT/'work/verification'/book/f'page_{n:04d}.png'
                assert p.exists(),p
                images.append({'path':rel(p),'sha256':sha(p)})
            add({'reader':book,'pdf_sha256':pdf_hashes[book],'pages':[page,page+1],
                 'reviewer':reviewer,'observation':observation,'images':images},
                'retained_doubts_rule_only' if page in rule_pages else 'retained_doubts',path)
    index=list(csv.DictReader((ROOT/'sources/fr/records/CURRENT_TEXT_INDEX.tsv').open(),delimiter='\t'))
    for row in rows:
        candidates=[]
        for p in index:
            a,b=map(int,p['scans'].split('-'))
            if p['cote']==row['cote'] and a<=row['scan']<=b:candidates.append(p)
        assert len(candidates)==1,row['id']
        info=candidates[0];row['package']=info['package'];row['scan_range']=info['scans']
        language='en' if '_EN_' in row['reader'] else 'fr'
        src=ROOT/'sources'/('en/packages' if language=='en' else 'fr/texts')/(info['package']+('_en' if language=='en' else '')+'.tex')
        text=src.read_text();match=re.search(r'\\scanpage\{'+str(row['scan'])+r'\}',text);assert match
        following=re.search(r'\\scanpage\{\d+\}',text[match.end():]);end=match.end()+following.start() if following else len(text)
        row['source']={'path':rel(src),'sha256':sha(src),'scan_marker_line':text[:match.start()].count('\n')+1,
                       'scan_fragment_sha256':hashlib.sha256(text[match.start():end].encode()).hexdigest()}
    unique={}
    for row in rows:
        assert row['id'] not in unique,row['id'];unique[row['id']]=row
    for book,doc in docs.items():
        doc.close();assert sha(ROOT/'work/build'/(book+'.pdf'))==pdf_hashes[book]
    result={'schema':'generated-heading-known-witnesses-v1','status':'FROZEN_ACTUAL_BEFORE_WITNESSES',
            'count':len(rows),'witnesses':rows,'inputs':list(inputs.values()),'before_pdf_hashes':pdf_hashes,
            'counts_by_reader':dict(collections.Counter(r['reader'] for r in rows)),
            'scope':'Actually reported revision512 generated heading, separator-rule and range-heading detachments only. Exact source identifiers and evidence bytes are preserved before rebuild; no machine candidate is automatically classified as defective.',
            'observations_generated_by_script':False}
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'output':rel(OUT),'count':len(rows),'by_reader':result['counts_by_reader']},ensure_ascii=False))

if __name__=='__main__':main()
