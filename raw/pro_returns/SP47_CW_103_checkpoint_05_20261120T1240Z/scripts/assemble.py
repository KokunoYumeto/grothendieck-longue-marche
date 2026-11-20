"""Rebuild current deliverables from the main reader's per-page decisions.

No OCR, automatic reading, or textual 'correction' is performed here.
"""
from pathlib import Path
from collections import Counter
import csv, json, argparse, hashlib, re
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
PREFIX='SP47_CW_103'
FIELDS=['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']
INV=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
def stamp():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def md(s):return str(s).replace('|','&#124;').replace('\n','<br>')
def code(s):return '<code>'+md(s).replace('<','&lt;').replace('>','&gt;')+'</code>'
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join('---' for _ in headers)+' |']+['| '+' | '.join(md(v) for v in row)+' |' for row in rows])+'\n'
def rebuild():
    ds=[json.loads(p.read_text()) for p in sorted((ROOT/'decisions').glob('scan*.json'))]
    if not ds:return
    pages=[];coll=[];inventory=[];counts=[];comparison_counts=[];total_cc=Counter();total_hc=Counter();conseq=[];notes=[];doubts=[];abbrev={};events=[];notation=[]
    changes=['# SP47_CW_103 — changes and adjudications\n\n',
      'The scans are the authority. A locus is counted once against each witness whose reading or uncertainty marking differs, regardless of how many glyphs it contains. Counts include resolved, added or reordered doubt marks; they are not estimates of witness error rates. Macro-only differences are excluded. Unchanged C doubts are recorded but are not counted against C. Confidence describes the final reading. Each reader\'s full independent return is preserved in `readers/`; the main decisions and crop references are preserved in `decisions/`.\n']
    bodies=[]
    for d in ds:
        n=d['scan']; cs=d['changes'];page=ROOT/'pages'/d['filename'];pages.append(page.read_text().rstrip())
        ac=sum(bool(x['against_c']) for x in cs); ah=sum(bool(x['against_h']) for x in cs)
        conf=Counter(x['confidence'] for x in cs if x['against_c'] or x['against_h'])
        cc=Counter(x['confidence'] for x in cs if x['against_c']);hc=Counter(x['confidence'] for x in cs if x['against_h']);total_cc.update(cc);total_hc.update(hc)
        counts.append([f'{n:03}',ac,ah,conf['high'],conf['medium'],conf['low'],len(d.get('unresolved',[]))])
        comparison_counts.append([f'{n:03}',ac,' / '.join(str(cc[k]) for k in ['high','medium','low']),ah,' / '.join(str(hc[k]) for k in ['high','medium','low']),len(d.get('unresolved',[]))])
        for c in cs:
            if c.get('consequential'):conseq.append(f'- Scan {n:03}, {c["place"]}: {c["consequential"]}')
            if c['against_h']:coll.append([d['folder'],n-1,n,c['place'],c['h'],c['c'],c['final'],c['scan_shows'],c['kind'],c.get('marked_in_H','no'),c['confidence']])
        bodies.append(f'## Scan {n:03}\n\n')
        rows=[]
        for c in cs:
            ev=c['scan_shows']
            if c.get('crops'):ev+=' Crop(s): '+', '.join('`'+p+'`' for p in c['crops'])+'.'
            rr=c.get('readers',{})
            if rr:ev+=' Readers: '+'; '.join(f'{k}: {code(v)}' for k,v in rr.items())+'.'
            rows.append([c['place'],code(c['c']),code(c['h']),code(c['final']),ev,c['confidence']])
        bodies.append(table(['Place','Witness C','Witness H','Consolidated reading','Scan evidence and adjudication','Confidence'],rows))
        bodies.append('\n### Remaining unresolved places\n\n')
        if d.get('unresolved'):
            bodies.append(table(['Place','Reading','Alternatives','Confidence','Evidence'],[[u['place'],code(u['reading']),code(u.get('alternatives','')),u['confidence'],u.get('evidence','')] for u in d['unresolved']]))
        else:bodies.append('None.\n')
        for i in d['inventory']:inventory.append({**i,'scan':n})
        notes.append(f'## Scan {n:03}\n\n'+'\n\n'.join(d['notes'])+'\n')
        for u in d.get('unresolved',[]):doubts.append([f'{n:03}',u['place'],code(u['reading']),code(u.get('alternatives','')),u['confidence'],u.get('evidence','')])
        for a in d.get('abbreviations',[]):abbrev.setdefault(a['form'],{'expansion':a['expansion'],'scans':[]})['scans'].append(n)
        for no in d.get('notation',[]):notation.append([f'{n:03}: '+no['place'],no['sign'],no['ink'],code(no['latex'])])
        events.extend(d.get('check_events',[]))
    totals=['All']+[sum(r[i] for r in counts) for i in range(1,7)]
    comparison_counts.append(['All',totals[1],' / '.join(str(total_cc[k]) for k in ['high','medium','low']),totals[2],' / '.join(str(total_hc[k]) for k in ['high','medium','low']),totals[6]])
    changes+=['## Counts\n\n',table(['Scan','Changes vs C','C high / medium / low','Changes vs H','H high / medium / low','Unresolved loci'],comparison_counts),f'\nAcross both witnesses, distinct changed loci by final confidence: {totals[3]} high, {totals[4]} medium, {totals[5]} low. An unresolved locus may contain several in-place doubt macros.\n\n## Consequential corrections\n\n','\n'.join(conseq)+'\n' if conseq else 'None established so far.\n','\n']
    (ROOT/f'{PREFIX}_changes.md').write_text(''.join(changes+bodies))
    (ROOT/f'{PREFIX}_transcription.tex').write_text('\n\n'.join(pages)+'\n')
    with (ROOT/f'{PREFIX}_collation.tsv').open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(FIELDS);w.writerows(coll)
    with (ROOT/f'{PREFIX}_inventory.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=INV,extrasaction='ignore');w.writeheader();w.writerows(inventory)
    (ROOT/f'{PREFIX}_notes.md').write_text('# Notes while reading\n\nThese notes describe only the supplied pages. Statements attributed to the text are reports of what it says, not endorsements or proof certificates. Mathematical checks actually performed are recorded in `CHECK_EVENTS.tsv`. No external sources were researched.\n\n'+'\n'.join(notes))
    notation_text='# Shared notation table\n\nEntries are ink-derived readings; repeated signs were reconsidered on each new page.\n\n'+table(['Scan/place','Sign or abbreviation','Ink / alternatives','LaTeX reading'],notation)
    (ROOT/'notation.md').write_text(notation_text)
    legibility=(ROOT/'records/legibility.md').read_text() if (ROOT/'records/legibility.md').exists() else 'Work in progress. Remaining doubts are listed above; no blanket claim of full certainty is made.'
    (ROOT/f'{PREFIX}_doubts.md').write_text(notation_text+'\n# Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Evidence'],doubts)+'\n# Abbreviations\n\nExpansions in this table are interpretive aids only; abbreviations are retained in the transcription.\n\n'+table(['Form','Probable expansion','Scans'],[[code(k),v['expansion'],', '.join(map(str,v['scans']))] for k,v in sorted(abbrev.items())])+'\n# Legibility and witness comparison\n\n'+legibility+'\n')
    with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
        for e in events:w.writerow([e[k] for k in ['statement_id','date','who','type','outcome']])
    (ROOT/'records/counts.json').write_text(json.dumps({'pages':len(ds),'counts':counts,'total':totals,'collation_rows':len(coll),'inventory_rows':len(inventory),'check_events':len(events)},indent=2))
    print(json.dumps({'decided_pages':len(ds),'changes_vs_C':totals[1],'changes_vs_H':totals[2],'collation_rows':len(coll),'inventory_rows':len(inventory)}))
if __name__=='__main__':rebuild()
