from pathlib import Path
import json,csv,datetime
R=Path(__file__).resolve().parents[1]; d=json.loads((R/'review/scan002_review.json').read_text()); t=(R/'review/scan002_proposed.tex').read_text()
t=t.replace(r'\deleted{\illegible{1}}50',r'\unsure{50}').replace(r'\margin{\unsure{--}}','').replace(r'des\unsure{.} figures','des figures')
changes=[]
for c in d['changes']:
    c['crop']=c.get('crop','').removeprefix('out/')
    c['reader_kind']=c['kind']
    if c['id'] in ['scan002-06','scan002-14']:continue
    if c['id']=='scan002-11':
        c.update(final='[no textual marginal dash]',against_C=True,against_H=False,confidence='high',kind='text not on the page',scan_shows='The crop shows an isolated, very faint broken stroke outside the text, with no attachment or lexical function. It is markedly paler than the writing. Under the prompt’s rule for incidental marks it is excluded, rather than promoted to a doubtful textual dash.')
    elif c['reader_kind']=='annotation_geometry':c['kind']='drawing or diagram'
    elif c['reader_kind'] in ['quotation_glyphs','capitalization','punctuation_and_capitalization','resolve_C_doubt']:c['kind']='other'
    elif c['reader_kind']=='accent_and_resolve_C_doubt':c['kind']='other'
    elif c['id']=='scan002-04':c['kind']=r'readable ink left as \ill{}'
    elif c['id']=='scan002-22':c['kind']='text not on the page'
    else:c['kind']='misread word'
    c['consequential']=c['id'] in ['scan002-16','scan002-21']
    changes.append(c)
changes.append(dict(id='scan002-17',place='Supralinear word before géométriques',C=r'\inserted{\uline{proprement}}',H=r'\emph{proprement} (not marked as inserted)',final=r'\inserted{\uline{proprement}}',scan_shows='The complete word is above the baseline of géométriques; a single underline lies beneath it and crosses no letters. The attachment is before géométriques. H preserves the word and underline but does not encode its inserted state.',confidence='high',kind='insertion or placement',crop='crops/scan002_proprement.png',box=[196,934,694,1074],against_C=False,against_H=True,marked_in_H=False,consequential=False))
d['changes']=sorted(changes,key=lambda x:x['id'])
d['doubts']=[x for x in d['doubts'] if x['place'] not in ['Left margin beside body line 2','Body line 5, after des']]
for x in d['doubts']:
    x['reason']=x['reason'].replace('out/crops/','crops/')
    if 'underwriting' in x['place']:
        x.update(reading=r'\unsure{50}',alternatives=['50 with retracing','50 over an unrecoverable earlier entry'],reason='50 is readable. Additional overlapping strokes cannot be separated into an earlier numeral, and an actual cancellation cannot be distinguished from retracing. The in-place doubt flags this source-state issue; no invented deleted word or numeral is supplied. Crop crops/scan002_references.png [1367,111,1664,337].')
newinv=[]
for e in d['inventory']:
    if e['element']=='Isolated margin stroke':continue
    if e['element'] in ['Corner classification','Reference note']:e['kind']='margin note'
    elif e['element']=='Supralinear insertion':e['kind']='insertion'
    else:e['kind']='text'
    newinv.append(e)
d['inventory']=newinv
# Graphic elements are separately inventoried, as required.
d['inventory']+= [dict(element='Reference oval and leader',kind='drawing',position='Upper-right note, x 1367–1664 y 111–337',first_words_or_objects='110-113, enclosed by oval; arrow toward interval after 23'),dict(element='Corner border',kind='drawing',position='Upper-right classification',first_words_or_objects='Left vertical and lower horizontal rule')]
d['root_adjudication']={'reader':'GPT-6 Astra Pro root; effort not exposed','viewed':'whole page once, both halves once, all 22 reader crops','decisions':['Accepted the independently supported words and retained GF/CF, simplexe(s), and facultatif(s) doubts.','Rejected the proposed point after des: no punctuation function is supported here; both witnesses omit it.','Removed C’s doubtful isolated pale margin stroke under the rule for incidental marks.','Declined to invent cancelled text beneath 50; recorded the uncertain overtracing state with an in-place doubt.','Added H’s missing insertion state for proprement.']}
# First readings use transcription notation rather than the reader’s descriptive glosses.
bs=d['second_boxes'];drop={'scan002_first_des','scan002_reference_overwriting','scan002_reference_arrow'}
fix={
'scan002_date':r'\uline{23 juin}',
'scan002_corner':r'\unsure{GF|CF} VII',
'scan002_references':r'Cf surtout p. 23 \unsure{50}-58, 59; 110-113',
'scan002_atelier':r"``\uline{atelier}''",
'scan002_dash':'',
'scan002_point_after_des':'des',
'scan002_proprement':r'\inserted{\uline{proprement}} géométriques',
'scan002_propriete':r'``propriété',
'scan002_fines':r"fines'',",
'scan002_autour':'autour',
'scan002_facultatif':r"``\unsure{facultatif|facultatifs}''",
}
new=[]
for b in bs:
    if b['box'] in drop:continue
    old=b['box'];b['reading']=fix.get(old,b['reading']);b['source_box_id']=old;b['box']=f'B{len(new)+1:03d}'
    if old in ['scan002_dash','scan002_point_after_des']:b['kind']='incidental_mark_status'
    new.append(b)
d['second_boxes']=new
(R/'review/scan002_final.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(R/'pages/H156-01_156-7_scan002.tex').write_text(t)
base=R/'second/H156-01_156-7_scan002'
for suffix,cols in [('_boxes.tsv',['box','kind','x0','y0','x1','y1']),('_first.tsv',['box','reading'])]:
    with Path(str(base)+suffix).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(new)
with (R/'review/root_visual_log.tsv').open('a') as f:
    for n in ['atelier_quotes','algébriques_quotes']:f.write('2\tcrops/scan002_'+n+'.png\t'+datetime.datetime.now(datetime.timezone.utc).isoformat()+'\troot direct crop inspection\n')
print('Finalized initial reading of scan002:',len(d['changes']),'records;',len(d['doubts']),'doubts;',len(new),'blind boxes.')
