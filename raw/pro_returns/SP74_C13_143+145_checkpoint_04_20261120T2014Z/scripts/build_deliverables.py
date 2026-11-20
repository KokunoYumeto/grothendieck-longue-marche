#!/usr/bin/env python3
"""Assemble reader/adjudicator records. No OCR or textual reading inference."""
from pathlib import Path
import csv, json, collections

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
PREFIX = 'SP74_C13_143+145'

def load_records():
    order = json.loads((ROOT/'page_order.json').read_text())
    return [json.loads((ROOT/'reviews'/f"{p['key']}_accepted.json").read_text()) for p in order if (ROOT/'reviews'/f"{p['key']}_accepted.json").exists()]

def write_table(name, fields, rows, delimiter='\t'):
    with (ROOT/name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter=delimiter, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)

def esc(s):
    return str(s if s is not None else '').replace('|','&#124;').replace('\n','<br>')

def mdtable(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(esc(c) for c in row)+' |' for row in rows])+'\n'

def evidence(c):
    s=c.get('ink','')
    cr=c.get('crop','page'); box=c.get('box')
    return s + ('; '+cr+(' '+str(tuple(box)) if box else '') if cr else '')

def inventory_in_source_order(items):
    """Keep original source order, placing subsequently drawn details by their parent."""
    ordered=sorted(items,key=lambda x:int(x['element'][1:]))
    ids={x['element'] for x in ordered}; children=collections.defaultdict(list); roots=[]
    for item in ordered:
        parent=item.get('parent_element',item.get('associated_existing_element'))
        if parent:
            assert parent in ids and parent!=item['element'], (parent,item['element'])
            children[parent].append(item)
        else: roots.append(item)
    result=[];seen=set()
    def add(item):
        assert item['element'] not in seen
        seen.add(item['element']);result.append(item)
        for child in children[item['element']]:add(child)
    for item in roots:add(item)
    assert len(result)==len(items), 'Inventory parent cycle'
    return result

def build():
    records=load_records(); changes=[]; counts=[]; collation=[]; decisions=[]; inventory=[]; doubts=[]; cert=[]; notes=[]; events=[]; habits=[]; abbr=[]
    for r in records:
        key=r['key']; cote,nn=key.split('_scan'); scan=int(nn)
        ch=r.get('changes',[])
        count=collections.Counter(c.get('confidence','medium') for c in ch)
        counts.append([key,sum(c.get('against_C',False) for c in ch),sum(c.get('against_H',False) for c in ch),count['high'],count['medium'],count['low']])
        changes.append('\n## '+key+'\n\n'+mdtable(['Place','Witness C','Witness H','Final reading','What the scan shows; evidence','Confidence'],[[c['place'],c.get('C',''),c.get('H',''),c['final'],evidence(c),c['confidence']] for c in ch]))
        if not ch: changes.append('No material differences from the available witnesses.\n')
        rem=r.get('remaining_doubts',[])
        changes.append('\nRemaining unresolved places: '+('; '.join(d['place']+': '+d['reading'] for d in rem) if rem else 'none')+'.\n')
        for c in ch:
            if c.get('against_H') and key!='143_scan034':
                collation.append(dict(folder=cote,their_page=scan-1,our_scan=scan,line=c['place'],their_reading=c.get('H',''),codex_reading=c.get('C',''),final_reading=c['final'],scan_shows=evidence(c),kind=c.get('kind','other'),marked_in_H='yes' if c.get('marked_in_H',False) else 'no',confidence=c['confidence']))
        for d in r.get('decisions',[]):
            decisions.append(dict(id=d['id'],cote=cote,scan=scan,decision=d['decision'],reading=d['reading'],**{'what the ink shows':d['ink']},crop=d.get('crop','page')+(' '+str(tuple(d['box'])) if d.get('box') else ''),confidence=d['confidence']))
        for i in inventory_in_source_order(r.get('inventory',[])): inventory.append(dict(scan=key,**i))
        for d in rem: doubts.append([key,d['place'],d['reading'],d.get('alternatives',''),d['confidence'],d.get('reason','')])
        for d in r.get('certainty_resolutions',[]): cert.append([key,d['place'],d['C'],d['final'],d['ink']])
        for a in r.get('abbreviations',[]): abbr.append([a['form'],a['expansion'],key])
        source_notes=[n for n in r.get('notes',[]) if n['id'].startswith(key+'-N')]
        source_notes.sort(key=lambda n:int(n['id'].split('-N')[-1]))
        later_notes=[n for n in r.get('notes',[]) if not n['id'].startswith(key+'-N')]
        notes.append('\n## '+key+'\n\n'+'\n\n'.join('**'+n['id']+'.** '+n['text'] for n in source_notes+later_notes)+'\n')
        for e in r.get('check_events',[]):
            events.append(dict(statement_id=e['statement_id'],date=e.get('date',r.get('accepted_at','').split(' ')[0]),who=e.get('who','GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; reader '+r['reader']),type=e['type'],outcome=e['outcome']))
        for h in r.get('hand_log',[]): habits.append([h['habit'],key+': '+h['places'],h['scope'],h['misreadings']])
    total=['TOTAL']+[sum(row[i] for row in counts) for i in range(1,6)]
    consequential=[f"- {r['key']}, {c['place']}: {c.get('C','')} / {c.get('H','')} → {c['final']}. {c['ink']}" for r in records for c in r.get('changes',[]) if c.get('consequential')]
    header='# Changes and collation decisions\n\nCounts are distinct material loci against each witness; a locus can count against both. Certainty-only and macro-only differences are excluded. Confidence counts count each logged locus once. For explicit unresolved alternatives, witness counts compare the preferred first reading; they do not assert that the alternative is certainly wrong.\n\n'+mdtable(['Page','Against C','Against H','High','Medium','Low'],counts+[total])+'\n## Consequential corrections\n\n'+('\n'.join(consequential) if consequential else 'None recorded yet.')+'\n'
    (ROOT/f'{PREFIX}_changes.md').write_text(header+''.join(changes))
    write_table(f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    source_marks=BASE/'source'/f'{PREFIX}_texts'/'MARKS.tsv'
    rank={row['id']:i for i,row in enumerate(csv.DictReader(source_marks.open(),delimiter='\t'))}
    decisions.sort(key=lambda d:rank[d['id']])
    write_table('decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decisions)
    write_table(f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
    notation=(ROOT/'notation.md').read_text()
    legibility=(ROOT/'legibility_note.md').read_text() if (ROOT/'legibility_note.md').exists() else 'Assessment remains in progress; see the page-specific uncertainty records.'
    (ROOT/f'{PREFIX}_doubts.md').write_text('# Notation, doubts and abbreviations\n\n'+notation+'\n## Remaining doubts\n\n'+mdtable(['Page','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'\n## Certainty-only resolutions\n\n'+mdtable(['Page','Place','Witness C','Final','Ink evidence'],cert)+'\n## Abbreviations (expansions only here)\n\n'+mdtable(['Written form','Proposed expansion','Page'],abbr)+'\n## Legibility and witnesses\n\n'+legibility+'\n')
    (ROOT/f'{PREFIX}_notes.md').write_text('# Notes while reading\n\nThese notes report the supplied manuscript pages. A source claim is not certified by transcription. Actual mathematical checks, where performed, are separately classified in CHECK_EVENTS.tsv. No external research was used.\n'+''.join(notes))
    write_table('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
    (ROOT/f'{PREFIX}_hand_log.md').write_text('# Hand log\n\nObserved habits are scoped to the occurrences actually inspected; they do not license silent normalization.\n\n'+mdtable(['Habit or notation','Pages and places','Scope','Witness misreadings'],habits))
    kinds=['misread symbol or index','misread word','omission','drawing or diagram','readable ink left as \\ill{}','insertion or placement','deletion state','abbreviation expanded or spelling modernised','text not on the page','other']
    kc=collections.Counter(c.get('kind','other') for r in records for c in r.get('changes',[]))
    feedback='# Error-sheet feedback\n\nCounts below describe material decision loci recorded in this run, against either witness. They are not token frequencies or estimates of unobserved errors. One locus has one primary kind. Certainty-only resolutions are reported separately in the doubts file.\n\n'+mdtable(['Error-sheet kind','Recorded loci'],[[k,kc[k]] for k in kinds])
    feedback+='\n## Recurring features and limits\n\nSee the hand log for scoped handwriting observations and the changes log for every locus. Additional recurring patterns will be recorded below after the cross-page comparison.\n'
    if (ROOT/'feedback_extra.md').exists(): feedback+='\n'+(ROOT/'feedback_extra.md').read_text()
    (ROOT/f'{PREFIX}_sheet_feedback.md').write_text(feedback)
    fragments=[]
    current_cote=None
    for r in records:
        cote=r['key'].split('_scan')[0]
        if cote != current_cote:
            fragments.append('\\cotefile{'+cote+'}')
            current_cote=cote
        fragments.append((ROOT/'pages'/f"{r['key']}.tex").read_text().rstrip())
    combined='\n\n'.join(fragments)+'\n'
    (ROOT/f'{PREFIX}_transcription.tex').write_text(combined)
    return {'pages':len(records),'changes':sum(len(r.get('changes',[])) for r in records),'collation':len(collation),'decisions':len(decisions),'inventory':len(inventory),'remaining_doubts':len(doubts)}

if __name__=='__main__': print(json.dumps(build(),ensure_ascii=False))
