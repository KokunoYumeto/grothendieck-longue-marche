"""Assemble only main-reader-approved page records; no source recognition."""
from pathlib import Path
import csv, json, collections, re, datetime

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'SP116_CW_75'
KINDS = ['misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other']
COLLATION = ['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']
INVENTORY = ['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']

def md(x):
    if x is None: return ''
    if not isinstance(x, str): x=json.dumps(x,ensure_ascii=False)
    return x.replace('|','&#124;').replace('\n','<br>')

def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |'] + ['| '+' | '.join(md(v) for v in row)+' |' for row in rows])+'\n'

def write_csv(path, fields, rows, delimiter):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore');w.writeheader();w.writerows(rows)

def evidence(c):
    s=c.get('evidence','')
    crop=c.get('crop','')
    if crop:
        crop=str(crop).replace(str(ROOT)+'/','')
        s+=f" Crop: {crop}; original box {c.get('box',[])}."
    return s

def assemble():
    records=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('scan[0-9][0-9][0-9].json'))]
    changes=[];coll=[];inv=[];doubts=[];notes=[];hands=[];notation=[];checks=[];counts=[];math=[];feedback=collections.defaultdict(list)
    for r in records:
        n=int(r['scan']);folder='J75-01' if n<=9 else 'J75-02'
        cr=r.get('changes',[])
        conf=collections.Counter(c.get('confidence','medium') for c in cr)
        counts.append([n,len(cr),sum(bool(c.get('against_c')) for c in cr),sum(bool(c.get('against_h')) for c in cr),conf['high'],conf['medium'],conf['low']])
        changes.append(f'## Scan {n:03d}\n\n'+table(['ID / place','Witness C','Witness H','Consolidated reading','What the image shows','Confidence'],[[str(c.get('id',''))+' / '+c.get('place',''),c.get('c',''),c.get('h',''),c.get('final',''),evidence(c),c.get('confidence','')] for c in cr]))
        unresolved=r.get('doubts',[])
        changes.append('Remaining doubts: '+ ('; '.join(str(d.get('place',''))+': '+str(d.get('reading','')) for d in unresolved) if unresolved else 'none.')+'\n')
        if r.get('root_review'):changes.append('Main-reader review: '+md(r['root_review'])+'\n')
        for c in cr:
            if c.get('against_h') and n!=2:
                coll.append(dict(folder=folder,their_page=n-1,our_scan=n,line=c.get('place',''),their_reading=c.get('h',''),codex_reading=c.get('c',''),final_reading=c.get('final',''),scan_shows=evidence(c),kind=c.get('kind','other'),marked_in_H='yes' if c.get('marked_in_H') else 'no',confidence=c.get('confidence','')))
            feedback[c.get('kind','other')].append(f"{n:03d}:{c.get('id',c.get('place',''))}")
            if c.get('math_note'):math.append(f"- Scan {n:03d}, {c.get('place','')}: {c['math_note']}")
        for i in r.get('inventory',[]): inv.append(dict(i,scan=n))
        for d in unresolved: doubts.append([n,d.get('place',''),d.get('reading',''),d.get('alternatives',''),d.get('confidence','')])
        notes.append(f'## Scan {n:03d}\n\n'+'\n\n'.join(str(x) for x in r.get('notes',[]))+'\n')
        if r.get('check_events'):
            for e in r['check_events']:
                checks.append(dict(statement_id=e.get('statement_id',f'S75-{n:03d}'),date=e.get('date',r.get('review_date','2026-11-20')),who=e.get('who','GPT-6 Astra Pro; reasoning effort inherited/not separately recorded; SP116_CW_75'),type=e['type'],outcome=e['outcome']))
        if r.get('hand_habits'):hands.append(f'## Scan {n:03d}\n\n'+'\n'.join('- '+str(x) for x in r['hand_habits'])+'\n')
        for t in r.get('notation',[]):notation.append([n,t])
    sums=['Total']+[sum(row[k] for row in counts) for k in range(1,7)]
    intro=f'# {PREFIX}: reading decisions\n\nCounts are by documented place, not by token. A place may differ from both witnesses. Decisions resolving C doubts and confirming or overturning witness S are recorded alongside text changes. Mere macro syntax is excluded. Scan 002 has no H transcription and contributes no H collation rows.\n\n'
    intro+=table(['Scan','Rows','Against C','Against H','High','Medium','Low'],counts+[sums])+'\n'
    intro+='## Consequential readings and mathematical slips\n\n'+ ('\n'.join(math) if math else 'No consequential decision recorded yet.')+'\n\n'
    (ROOT/f'{PREFIX}_changes.md').write_text(intro+'\n'.join(changes))
    write_csv(ROOT/f'{PREFIX}_collation.tsv',COLLATION,coll,'\t')
    write_csv(ROOT/f'{PREFIX}_inventory.csv',INVENTORY,inv,',')
    write_csv(ROOT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks,'\t')
    (ROOT/f'{PREFIX}_notes.md').write_text('# Reading notes\n\nThese notes describe only the supplied pages. Image verification of a reading is not a mathematical proof check. Mathematical check events, when performed, are separately recorded in CHECK_EVENTS.tsv.\n\n'+'\n'.join(notes))
    (ROOT/f'{PREFIX}_hand_log.md').write_text('# Observed handwriting and notation\n\nHabits below are local observations, not automatic substitutions on other pages.\n\n'+'\n'.join(hands)+('\n'+(ROOT/'records/hand_cross_page.md').read_text() if (ROOT/'records/hand_cross_page.md').exists() else ''))
    abbreviations=(ROOT/'records/abbreviations.md').read_text() if (ROOT/'records/abbreviations.md').exists() else 'Entries pending final cross-page review.'
    legibility=(ROOT/'records/legibility.md').read_text() if (ROOT/'records/legibility.md').exists() else 'The remaining doubts are retained in the page files; final cross-page assessment pending.'
    (ROOT/f'{PREFIX}_doubts.md').write_text('# Notation and doubts\n\n'+(ROOT/'notation.md').read_text()+'\n\n## Page-grounded observations\n\n'+table(['Scan','Observation'],notation)+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence'],doubts)+'\n## Abbreviations (expansions only here)\n\n'+abbreviations+'\n\n## Legibility and witness comparison\n\n'+legibility+'\n')
    feedback_rows=[[k,len(feedback[k]),'; '.join(feedback[k])] for k in KINDS]
    (ROOT/f'{PREFIX}_sheet_feedback.md').write_text('# Error-sheet feedback\n\nThe counts below concern documented decision places, including retained uncertainty where noted; they are not an error rate for all tokens. A place is counted under its principal kind.\n\n'+table(['Kind','Places','IDs'],feedback_rows)+'\nDetailed recurring handwriting issues are in the hand log.\n'+('\n'+(ROOT/'records/specific_feedback.md').read_text() if (ROOT/'records/specific_feedback.md').exists() else ''))
    files=sorted((ROOT/'pages').glob('*.tex'))
    (ROOT/f'{PREFIX}_transcription.tex').write_text('\n\n'.join(f.read_text().rstrip() for f in files)+'\n')
    summary=dict(pages=len(files),decision_rows=sum(len(r.get('changes',[])) for r in records),against_c=sum(bool(c.get('against_c')) for r in records for c in r.get('changes',[])),against_h=len(coll),doubts=len(doubts),inventory_rows=len(inv))
    (ROOT/'records/summary.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary))

if __name__=='__main__':assemble()
