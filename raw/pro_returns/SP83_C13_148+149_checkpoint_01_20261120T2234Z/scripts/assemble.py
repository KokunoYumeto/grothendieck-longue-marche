"""Assemble the reviewed collation records. No OCR and no TeX compilation."""
from pathlib import Path
import csv, json, re, sys, hashlib
from collections import Counter
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'result'
ID='SP83_C13_148+149'
ORDER=(OUT/'page_order.txt').read_text().splitlines()
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def md(s):return str(s).replace('|','&#124;').replace('\n','<br>')
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']+['| '+' | '.join(md(v) for v in row)+' |' for row in rows])+'\n'
def tsv(path,fields,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
def evidence(c):
    s=c.get('evidence','')
    if c.get('crop') and c['crop']!='page':s+='; '+c['crop']+' '+str(tuple(c.get('box',[])))
    return s
def records():
    return [json.loads((OUT/'records'/f'{p}.json').read_text()) for p in ORDER if (OUT/'records'/f'{p}.json').exists()]
def assemble():
    rs=records();page_rows=[];confidence_rows=[];total=Counter();coll=[];dec=[];inv=[];events=[];conseq=[];cats=Counter()
    change_sections=[];doubt_rows=[];note_sections=[];habits=[];abbrevs=[]
    for r in rs:
        p=r['page'];cote,scan=p.split('_scan');cnt=Counter()
        cs=[c for c in r.get('changes',[]) if c.get('diff_c') or c.get('diff_h')]
        for c in cs:
            cnt['C']+=bool(c.get('diff_c'));cnt['H']+=bool(c.get('diff_h'));cnt[c['confidence']]+=1
            for witness,field in [('C','diff_c'),('H','diff_h')]:
                if c.get(field):cnt[witness+'_'+c['confidence']]+=1
            cats[c.get('error_kind','Other')]+=1
            if c.get('consequential'):conseq.append(f"- **{p}, {c['place']}**: {c['c']} / {c['h']} → {c['final']}. {c.get('consequence',c.get('evidence',''))}")
            if c.get('diff_h'):
                coll.append(dict(folder=cote,their_page=int(scan)-1,our_scan=int(scan),line=c['place'],their_reading=c['h'],codex_reading=c['c'],final_reading=c['final'],scan_shows=evidence(c),kind=c.get('kind','other'),marked_in_H='yes' if c.get('marked_in_h') else 'no',confidence=c['confidence']))
        total.update(cnt);page_rows.append([p,len(cs),cnt['C'],cnt['H'],cnt['high'],cnt['medium'],cnt['low']])
        confidence_rows.append([p]+[cnt[w+'_'+level] for w in ['C','H'] for level in ['high','medium','low']])
        section=f"## {p}\n\n"+table(['Place','Witness C','Witness H','Final reading','What the scan shows; crop and original pixel box','Confidence'],[[c['place'],c['c'],c['h'],c['final'],evidence(c),c['confidence']] for c in cs])
        if not cs:section+='No material differences from either witness.\n'
        for a in r.get('audit_changes',[]):
            section+=f"\n### Independent second reading: {a['box']}\n\n"+table(['First reading','Independent reading','Final decision','Evidence'],[[a['first'],a['second'],a['final'],a['evidence']]])
        if r.get('implicit_decisions'):
            section+='\n### Other reading decisions, including C doubts outside MARKS.tsv\n\n'+table(['Local id','Decision','Reading','What the ink shows','Confidence'],[[d.get('id',''),d['decision'],d['reading'],evidence(d),d['confidence']] for d in r['implicit_decisions']])
        section+='\n### Still unresolved\n\n'
        ds=r.get('doubts',[])
        section+=('\n'.join(f"- {d['place']}: `{d['reading']}` — {d.get('reason','')}" for d in ds) if ds else 'None.')+'\n'
        change_sections.append(section)
        for d in r.get('decisions',[]):
            crop=d.get('crop','page')
            if crop!='page':crop+=' '+str(tuple(d.get('box',[])))
            dec.append({'id':d['id'],'cote':cote,'scan':int(scan),'decision':d['decision'],'reading':d['reading'],'what the ink shows':d['evidence'],'crop':crop,'confidence':d['confidence']})
        for i in r.get('inventory',[]): inv.append(dict(i,scan=p))
        for d in ds:doubt_rows.append([p,d['place'],d['reading'],d.get('alternatives',''),d['confidence'],d.get('reason','')])
        note_sections.append(f"## {p}\n\n"+'\n\n'.join(f"**{n['id']}**. {n['text']}" if isinstance(n,dict) else str(n) for n in r.get('notes',[])))
        for e in r.get('check_events',[]):events.append(dict(e,date=e.get('date',r.get('reviewed_at','').split(' ')[0]),who=e.get('who',f"GPT-6 Astra Pro; inherited effort; {r.get('reader','first reader')} / main reader; run 2026-11-20")))
        for n in r.get('notation',[]):habits.append([n.get('sign',''),n.get('meaning_or_form',''),p+': '+n.get('places',''),n.get('universality',''),n.get('witness_errors','')])
        abbrevs.extend(r.get('abbreviations',[]))
    totalrow=['TOTAL',sum(x[1] for x in page_rows),total['C'],total['H'],total['high'],total['medium'],total['low']]
    header=f'# Consolidated changes: {ID}\n\n{len(rs)} of {len(ORDER)} pages reviewed by the main reader. Counts are places, not character edits. One place may differ from both witnesses. Pure macro syntax, editorial headings and certainty-only changes are excluded. The supplied word-diff list is a location aid, not the counting unit.\n\n'
    header+=table(['Page','Places','Against C','Against H','High','Medium','Low'],page_rows+[totalrow])
    header+='\n### Confidence by witness\n\n'+table(['Page','C high','C medium','C low','H high','H medium','H low'],confidence_rows+[['TOTAL']+[total[w+'_'+level] for w in ['C','H'] for level in ['high','medium','low']]])
    header+='\n## Consequential corrections\n\n'+('\n'.join(conseq) if conseq else 'No consequential correction recorded so far.')+'\n\n'
    (OUT/f'{ID}_changes.md').write_text(header+'\n'.join(change_sections))
    tsv(OUT/f'{ID}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
    original=list(csv.DictReader((ROOT/'source/SP83_C13_148+149_texts/MARKS.tsv').open(),delimiter='\t'))
    mark_order={r['id']:i for i,r in enumerate(original)}
    dec.sort(key=lambda d:mark_order[d['id']])
    tsv(OUT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],dec)
    with (OUT/f'{ID}_inventory.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],extrasaction='ignore');w.writeheader();w.writerows(inv)
    tsv(OUT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
    nt=table(['Sign / form','Meaning or visible form','Pages and places','Scope observed','Witness errors'],habits)
    (OUT/'notation_working.md').write_text('# Working notation table\n\n'+nt)
    (OUT/f'{ID}_hand_log.md').write_text('# Hand and notation log\n\nEntries record observations on the supplied pages. A stated habit is not permission to regularise a clear contrary form.\n\n'+nt)
    seen=set();ars=[]
    for a in abbrevs:
        k=(a['form'],a['expansion'])
        if k not in seen:seen.add(k);ars.append(list(k))
    legibility=(OUT/'legibility_note.md').read_text() if (OUT/'legibility_note.md').exists() else 'Review in progress. Remaining doubts are retained explicitly; no human verification is claimed.'
    (OUT/f'{ID}_doubts.md').write_text('# Notation table\n\n'+nt+'\n# Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubt_rows)+'\n# Abbreviations\n\nExpansions here are explanatory only and are not substituted in the transcription.\n\n'+table(['Written form','Proposed expansion'],ars)+'\n# Legibility and witnesses\n\n'+legibility+'\n')
    (OUT/f'{ID}_notes.md').write_text('# Notes while reading\n\nThese notes describe the supplied leaves only. Reports of the author’s claims are not independent proofs. CHECK_EVENTS.tsv distinguishes actual checking from statements carried as background. No external sources were consulted.\n\n'+'\n\n'.join(note_sections)+'\n')
    kinds=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertions put in the wrong place','Struck text','Abbreviations expanded, spelling modernised','Text that is not on the page','Other']
    feedback='# Error-sheet feedback\n\nCounts below classify material discrepancy places by their primary error-sheet kind; a place can affect both witnesses but is counted once. They are observed discrepancies, not a statistical estimate of all errors in the manuscript or other runs. Certainty-only decisions are excluded.\n\n'
    feedback+=table(['Error-sheet category','Places'],[[k,cats[k]] for k in kinds]+[[k,v] for k,v in cats.items() if k not in kinds])
    feedback+='\n## Recurring features and errors\n\nSee the hand log for page-grounded recurring shapes and the exact witnesses affected.\n'
    for r in rs:
        for f in r.get('sheet_feedback',[]):feedback+=f"\n- {r['page']}: {f}\n"
    (OUT/f'{ID}_sheet_feedback.md').write_text(feedback)
    combined=[];previous=None
    for p in ORDER:
        fp=OUT/'pages'/f'{p}.tex'
        if not fp.exists():continue
        cote=p.split('_')[0]
        if cote!=previous:combined.append('\\cotefile{'+cote+'}\n');previous=cote
        combined.append('% '+p+'\n'+fp.read_text().rstrip()+'\n')
    (OUT/f'{ID}_transcription.tex').write_text('\n'.join(combined))
    print(json.dumps({'pages':len(rs),'changes':totalrow[1],'against_C':total['C'],'against_H':total['H'],'decisions':len(dec),'inventory_elements':len(inv),'doubts':len(doubt_rows)},ensure_ascii=False))

def accept(page):
    p=ROOT/'proposed'/f'{page}.json';r=json.loads(p.read_text());r['reviewed_at']=now()
    if not r.get('main_reader_reviewed'):raise ValueError('Main reader must mark review complete explicitly before accepting')
    (OUT/'pages'/f'{page}.tex').write_text((ROOT/'proposed'/f'{page}.tex').read_text())
    (OUT/'records'/f'{page}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    boxes=r.get('second_boxes',[])
    tsv(OUT/'second'/f'{page}_boxes.tsv',['box','kind','x0','y0','x1','y1'],boxes)
    tsv(OUT/'second'/f'{page}_first.tsv',['box','reading'],boxes)
    assemble()
    with (OUT/'progress.log').open('a') as f:f.write(f"scan {int(page.split('_scan')[1]):03} done {now()} cote {page.split('_')[0]}: {r['lines_read']} lines read, {len(list((OUT/'crops').glob(page+'_*.png')))} places cropped, {sum(bool(c.get('diff_c') or c.get('diff_h')) for c in r.get('changes',[]))} rows; first reader {r.get('reader','unknown')}\n")

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='accept':accept(sys.argv[2])
    else:assemble()
