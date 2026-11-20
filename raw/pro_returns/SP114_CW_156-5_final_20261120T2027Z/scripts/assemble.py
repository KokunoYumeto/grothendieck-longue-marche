"""Assemble deliverables from main-reader adjudicated page records.
No OCR, image recognition, or mathematical text normalization is performed.
"""
from pathlib import Path
import csv, json, collections, re
ROOT=Path(__file__).resolve().parents[1]
ID='SP114_CW_156-5'
SCANS=range(26,34)

def text_value(x):
    if isinstance(x,str): return x
    if isinstance(x,list): return '; '.join(text_value(v) for v in x)
    if isinstance(x,dict): return '; '.join(f'{k}: {text_value(v)}' for k,v in x.items())
    return str(x)

def cell(x):
    return text_value(x).replace('|','\\|').replace('\n','<br>')

def witness_value(x):
    # Explicit nulls in this edition's C/H slots denote omitted source spans.
    # Do not apply this convention to missing readings or other metadata.
    return '(omitted)' if x is None else x

def evidence(r):
    e=r.get('evidence',r.get('scan_shows',''))
    if r.get('crop'):
        e += f" Crop: `{r['crop']}`; original-image box {r.get('box',[])}."
    if r.get('main_decision'): e+=' Main adjudication: '+text_value(r['main_decision'])
    if r.get('second_evidence'): e+=' Second reading: '+text_value(r['second_evidence'])
    return e

def getrecords():
    records=[]
    for n in SCANS:
        p=ROOT/'review'/f'scan{n:03}_adjudicated.json'
        if p.exists(): records.append(json.loads(p.read_text()))
    return records

def assemble():
    records=getrecords()
    rows=[(r['scan'],x) for r in records for x in r.get('changes',[])]
    substantive=[(s,r) for s,r in rows if not r.get('certainty_only',False) and (r.get('against_C') or r.get('against_H'))]
    intro=[f'# Consolidated changes — {ID}','',
      'Source authority: the supplied scan images. C and H are draft witnesses; their agreement is not treated as evidence. Each locus is counted once in the total and may count against both witnesses. Macro-only differences and certainty-only resolutions are excluded from substantive-change totals; crop-supported certainty decisions are recorded separately. Pixel boxes refer to the original whole-page JPG; coordinates use the top-left origin.','',
      '| Scan | Substantive loci | Against C | Against H | High | Medium | Low | Certainty decisions |',
      '| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
    totals=[0]*7
    for rec in records:
        rr=[x for s,x in substantive if s==rec['scan']]
        vals=[len(rr),sum(bool(x.get('against_C')) for x in rr),sum(bool(x.get('against_H')) for x in rr)]+[sum(x.get('confidence')==c for x in rr) for c in ['high','medium','low']]+[sum(x.get('certainty_only',False) for x in rec.get('changes',[]))]
        totals=[a+b for a,b in zip(totals,vals)]
        intro.append('| '+str(rec['scan'])+' | '+' | '.join(map(str,vals))+' |')
    intro+=['| **Total** | '+' | '.join(f'**{v}**' for v in totals)+' |','','## Consequential corrections and retained slips','']
    for s,r in substantive:
        if r.get('consequential'):
            intro.append(f"- Scan {s}, {r.get('id','')}, {r['place']}: {r['final']} — {r.get('consequence',r['evidence'])}")
    for rec in records:
        intro+=['',f"## Scan {rec['scan']} (manuscript {rec['scan']-1})",'',
           '| ID / place | Witness C | Witness H | Consolidated reading | Ink evidence | Confidence |',
           '| --- | --- | --- | --- | --- | --- |']
        for r in rec.get('changes',[]):
            if r.get('certainty_only',False): continue
            if not (r.get('against_C') or r.get('against_H')): continue
            intro.append('| '+' | '.join(cell(x) for x in [r.get('id','')+' — '+r['place'],witness_value(r['C']),witness_value(r['H']),r['final'],evidence(r),r['confidence']])+' |')
        decisions=[r for r in rec.get('changes',[]) if r.get('certainty_only',False)]
        if decisions:
            intro+=['','### Crop-supported certainty decisions','',
              '| ID / place | C doubt | Reading retained or resolved | Ink evidence | Confidence |',
              '| --- | --- | --- | --- | --- |']
            for r in decisions:
                intro.append('| '+' | '.join(cell(x) for x in [r.get('id','')+' — '+r['place'],witness_value(r['C']),r['final'],evidence(r),r['confidence']])+' |')
        intro+=['','### Unresolved places','']
        if not rec.get('unresolved'): intro.append('None recorded after adjudication.')
        for r in rec.get('unresolved',[]): intro.append('- '+text_value(r))
        if rec.get('audit_changes'):
            intro+=['','### Adjudication of independent second-reading differences','',
               '| Box / place | First reading | Independent second reading | Final decision and crop evidence | Confidence |',
               '| --- | --- | --- | --- | --- |']
            for r in rec['audit_changes']:
                intro.append('| '+' | '.join(cell(r.get(k,'')) for k in ['box','first','second','decision','confidence'])+' |')
        if rec.get('S_decisions'):
            intro+=['','### Witness S','']
            intro += ['- '+text_value(x) for x in rec['S_decisions']]
    (ROOT/f'{ID}_changes.md').write_text('\n'.join(intro)+'\n')
    fields=['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']
    with (ROOT/f'{ID}_collation.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader()
        for scan,r in substantive:
            if r.get('against_H'):
                w.writerow(dict(folder='J156-5-04',their_page=scan-1,our_scan=scan,line=r['place'],their_reading=witness_value(r['H']),codex_reading=witness_value(r['C']),final_reading=r['final'],scan_shows=evidence(r).replace('\n',' '),kind=r['kind'],marked_in_H='yes' if r.get('H_marked') else 'no',confidence=r['confidence']))
    invfields=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
    with (ROOT/f'{ID}_inventory.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=invfields);w.writeheader()
        for rec in records:
            for r in rec.get('inventory',[]):
                w.writerow(dict(scan=rec['scan'],sheet_kind=r.get('sheet_kind','text'),hand=r.get('hand',"Alexander Grothendieck's hand"),element=r['element'],kind=r['kind'],position=r['position'],first_words_or_objects=r['first_words_or_objects'],transcribed='yes'))
    notation=(ROOT/'notation_working.md').read_text() if (ROOT/'notation_working.md').exists() else ''
    doubts=[notation,'','## Remaining doubts','',
      '| Scan | Place | Reading | Alternatives | Confidence | Reason |','| --- | --- | --- | --- | --- | --- |']
    for rec in records:
        for r in rec.get('unresolved',[]):
            doubts.append('| '+' | '.join(cell(x) for x in [rec['scan'],r.get('place',''),r.get('reading',''),r.get('alternatives',''),r.get('confidence',''),r.get('reason','')])+' |')
    doubts+=['','## Abbreviations (expansions are editorial and do not enter the transcription)','']
    for rec in records:
        if rec.get('abbreviations'):
            doubts.append(f"### Scan {rec['scan']}\n")
            for x in rec['abbreviations']: doubts.append('- '+text_value(x))
            doubts.append('')
    leg=ROOT/'review/legibility.md'
    if leg.exists(): doubts+=['## Legibility and witness comparison','',leg.read_text()]
    (ROOT/f'{ID}_doubts.md').write_text('\n'.join(doubts)+'\n')
    notes=[f'# Reading notes — {ID}','',
      'These notes concern scans 26–33 only. Descriptions of what the manuscript states do not certify its claims. Actual mathematical checks and use of supplied background are distinguished in CHECK_EVENTS.tsv. The transcription retains visible slips; proposed mathematical repairs appear only here.','']
    for rec in records:
        notes += [f"## Scan {rec['scan']} — manuscript page {rec['scan']-1}",'']
        n=rec.get('notes',[])
        if isinstance(n,str): notes.append(n)
        elif isinstance(n,dict):
            for k,v in n.items(): notes.append(f'**{k}.** '+text_value(v)+'\n')
        else:
            for x in n: notes.append('- '+text_value(x))
        notes.append('')
    notes+=['## Source attribution','',
      'Grothendieck, A. (1986). *[Chapitre] V. Algèbre des figures: Notes manuscrites (14/06/1986)* [Unpublished manuscript, cote 156-5, archive scans 26–33; handwritten pages 25–32]. Université de Montpellier, fonds Grothendieck. Source images supplied with this task. The archival catalogue date is not a date written on these eight sheets.','',
      'Hua, M., & Commutator project. (2026). *Grothendieck project: Cote 156-5, batch 02, pages 25–32* [AI transcription, commit aef7db2]. Supplied witness H.','',
      'Witness C: supplied Codex session J156-5-04, pages 026–033, GPT-6 Astra, 13–15 November 2026. Witness S: supplied horizontal sweep 3, 156-5_CORRECTIONS.tsv, row SA21-K5-02 (19 November 2026); its metadata explicitly identifies the scan reading as undecided. No external sources were consulted.']
    (ROOT/f'{ID}_notes.md').write_text('\n'.join(notes)+'\n')
    pages=[ROOT/'pages'/f'J156-5-04_156-5_scan{n:03}.tex' for n in SCANS]
    existing=[p for p in pages if p.exists()]
    (ROOT/f'{ID}_transcription.tex').write_text('\n\n'.join(p.read_text().rstrip() for p in existing)+'\n')
    print(json.dumps({'adjudicated_scans':[r['scan'] for r in records],'totals':dict(zip(['loci','against_C','against_H','high','medium','low','certainty'],totals))},ensure_ascii=False))

if __name__=='__main__': assemble()
