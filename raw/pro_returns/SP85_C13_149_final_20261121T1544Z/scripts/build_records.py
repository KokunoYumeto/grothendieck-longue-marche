"""Rebuild the requested records from main-reader-approved per-page JSON.

This script handles bookkeeping only. It does not recognize image text or
make reading decisions. The original scans/witnesses remain outside output.
"""
from pathlib import Path
import csv, json, collections, re, hashlib, datetime, sys

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'SP85_C13_149'

def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def table_cell(x):
    return str(x).replace('|','&#124;').replace('\n','<br>')

def md_table(headers, rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(table_cell(v) for v in row)+' |\n' for row in rows)

def write_delim(path, fields, rows, delimiter='\t'):
    with path.open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore')
        wr.writeheader();wr.writerows(rows)

def main():
    records=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('149_scan*.json'))]
    changes=[];collation=[];decisions=[];inventory=[];doubts=[];notes=[];hands=[];notation=[];abbreviations=[];events=[]
    counts=[];witness_conf=[];consequential=[];error_counts=collections.Counter();against_c_categories=collections.Counter()
    for p in records:
        n=p['scan'];page=p['page'];rows=p.get('rows',[])
        cc=sum(bool(r.get('against_C')) for r in rows);hc=sum(bool(r.get('against_H')) for r in rows)
        conf=collections.Counter(r['confidence'] for r in rows)
        counts.append([f'{n:03}',len(rows),cc,hc,conf['high'],conf['medium'],conf['low']])
        witness_conf.append([f'{n:03}']+[sum(bool(r.get(flag)) and r['confidence']==level for r in rows) for flag in ['against_C','against_H'] for level in ['high','medium','low']])
        content=[]
        for k,r in enumerate(rows,1):
            r_id=f'{n:03}-{k:03}';evidence=r['scan_shows']
            if r.get('crop'):
                evidence+=f"; `{r['crop']}`; original-pixel box {tuple(r.get('box',[]))}"
            content.append([r_id,r['place'],r['C'],r['H'],r['final'],evidence,r['confidence']])
            if r.get('against_H'):
                collation.append(dict(folder='149',their_page=n-1,our_scan=n,line=r['place'],their_reading=r['H'],codex_reading=r['C'],final_reading=r['final'],scan_shows=evidence,kind=r['kind'],marked_in_H='yes' if r.get('marked_in_H') else 'no',confidence=r['confidence']))
            if r.get('consequential'):
                consequential.append(f"- Scan {n}, {r['place']}: {r['C']} / {r['H']} → {r['final']}. {r['scan_shows']}")
            cat=r.get('error_category','Other');error_counts[cat]+=1
            if r.get('against_C'):against_c_categories[cat]+=1
        changes.append(f'## Scan {n:03}\n\n'+md_table(['ID','Place','Witness C','Witness H','Final reading','What the scan shows','Confidence'],content))
        unresolved=p.get('doubts',[])
        changes.append('\nStill unresolved: '+('; '.join(f"{d['place']}: `{d['reading']}` ({d['confidence']})" for d in unresolved) if unresolved else 'none recorded.')+'\n')
        if p.get('second_changes'):
            changes.append('\n### Changes after the independent second reading\n\n'+md_table(['Box / place','First reading','Independent reading','Final reading','Decision from the crop'],[[x['box'],x['first'],x['second'],x['final'],x['ink']+'; `'+x['crop']+'`'] for x in p['second_changes']]))
        for d in p.get('decisions',[]):
            decisions.append({'id':d['id'],'cote':'149','scan':n,'decision':d['decision'],'reading':d['reading'],'what the ink shows':d['ink'],'crop':d.get('crop','page')+(f"; {tuple(d['box'])}" if d.get('crop')!='page' and d.get('box') else ''),'confidence':d['confidence']})
        for e in p.get('inventory',[]):inventory.append(dict(scan=n,**e))
        for d in unresolved:doubts.append([f'{n:03}',d['place'],d['reading'],d.get('alternatives',''),d['confidence'],d.get('reason','')])
        notes.append(f"## Scan {n:03}\n\n{p.get('notes','')}\n")
        for h in p.get('hand_log',[]):hands.append([f'{n:03}',h['habit'],h['places'],h['scope'],h['witness_errors']])
        for x in p.get('notation',[]):notation.append([x['form'],x['meaning'],f"Scan {n}: {x['evidence']}"])
        for x in p.get('abbreviations',[]):abbreviations.append([x['form'],x['expansion'],str(n)])
        for e in p.get('check_events',[]):
            who=e.get('who','GPT-6 Astra Pro; inherited reasoning setting; SP85_C13_149')
            if 'inherited' not in who and e.get('reasoning'):who+='; reasoning '+e['reasoning']
            if 'SP85_C13_149' not in who:who+='; '+e.get('run','SP85_C13_149')
            outcome=e['outcome']
            if e.get('argument') and e['argument'] not in outcome:outcome+=' Argument: '+e['argument']
            if e.get('refined_statement_id'):outcome+=' Refined statement ID: '+e['refined_statement_id']+'.'
            events.append({'statement id':e['statement_id'],'date':e.get('date',datetime.date.today().isoformat()),'who (model, effort, run)':who,'type':e['type'],'outcome':outcome})
        boxes=p.get('audit_boxes',[])
        # First readings are frozen before the blind reader is assigned.
        bpath=ROOT/'second'/f'{page}_boxes.tsv';fpath=ROOT/'second'/f'{page}_first.tsv'
        if not bpath.exists():
            write_delim(bpath,['box','kind','x0','y0','x1','y1'],[dict(box=b['box'],kind=b['kind'],**dict(zip(['x0','y0','x1','y1'],b['coords']))) for b in boxes])
        if not fpath.exists():write_delim(fpath,['box','reading'],[dict(box=b['box'],reading=b['reading'].replace('\n',' ')) for b in boxes])
    sums=['All']+[sum(x[i] for x in counts) for i in range(1,7)]
    head='# Changes — SP85_C13_149\n\nCounts are material places, not raw token edits. A place can differ from both witnesses. Changes of macro syntax alone and newly added doubt alone are excluded. Resolving an existing doubt is recorded with its image evidence.\n\n'
    head+=md_table(['Scan','Places','Against C','Against H','High','Medium','Low'],counts+[sums])
    head+='\n### Confidence by witness\n\n'+md_table(['Scan','C: high','C: medium','C: low','H: high','H: medium','H: low'],witness_conf+[['All']+[sum(x[i] for x in witness_conf) for i in range(1,7)]])
    head+='\n## Consequential corrections\n\n'+('\n'.join(consequential) if consequential else 'No consequential correction has yet been recorded.')+'\n\n'
    (ROOT/f'{PREFIX}_changes.md').write_text(head+'\n'.join(changes))
    write_delim(ROOT/f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    source_marks=list(csv.DictReader((ROOT.parent/'source/SP85_C13_149_texts/MARKS.tsv').open(),delimiter='\t'))
    rank={r['id']:i for i,r in enumerate(source_marks)}
    decisions.sort(key=lambda r:rank[r['id']])
    write_delim(ROOT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decisions)
    write_delim(ROOT/f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
    # Group literally identical forms without erasing evidence of varying spellings.
    ng=collections.OrderedDict()
    for form,meaning,evidence in notation:
        key=(form,meaning);ng.setdefault(key,[]).append(evidence)
    nt=md_table(['Written form / transcription','Meaning or convention','Observed places'],[[k[0],k[1],'; '.join(v)] for k,v in ng.items()])
    (ROOT/'notation.md').write_text('# Current notation table\n\n'+nt)
    ag=collections.OrderedDict()
    for form,expansion,scan in abbreviations:ag.setdefault((form,expansion),[]).append(scan)
    limits=(ROOT/'records/legibility.txt').read_text() if (ROOT/'records/legibility.txt').exists() else 'The reading is in progress. Dense crossings-out, faint pencil, and oblique marginalia receive the lowest confidence. Each uncertain reading remains marked locally; agreement between the two AI witnesses was not treated as visual evidence.'
    (ROOT/f'{PREFIX}_doubts.md').write_text('# Doubts and notation — SP85_C13_149\n\n## Notation table\n\n'+nt+'\n## Remaining doubts\n\n'+md_table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'\n## Abbreviations (expansions only here)\n\n'+md_table(['Written form','Proposed expansion','Scans'],[[k[0],k[1],', '.join(v)] for k,v in ag.items()])+'\n## Legibility and witness comparison\n\n'+limits+'\n')
    (ROOT/f'{PREFIX}_notes.md').write_text('# Reading notes — SP85_C13_149\n\nThese notes describe only the supplied leaves. A summary of an assertion does not certify its truth. Explicit mathematical checks, when performed, are separately identified in CHECK_EVENTS.tsv; transcription and image comparison are not counted as proof checks.\n\nPaper features and show-through are excluded. The supplied instructions identify the paper watermark as “EXTRA STRONG”; that identification is recorded here once, not transcribed as handwriting or as a doubt mark.\n\n'+'\n'.join(notes))
    write_delim(ROOT/'CHECK_EVENTS.tsv',['statement id','date','who (model, effort, run)','type','outcome'],events)
    (ROOT/f'{PREFIX}_hand_log.md').write_text('# Hand log — SP85_C13_149\n\nHabits below were observed on the named leaves. They are not universal substitution rules; uncertain glyphs remain uncertain.\n\n'+md_table(['Scan','Habit','Places','Scope of confirmation','Witness errors'],hands))
    cats=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertions put in the wrong place','Struck text','Abbreviations expanded, spelling modernised','Text that is not on the page','Other']
    observations=(ROOT/'records/sheet_observations.md').read_text() if (ROOT/'records/sheet_observations.md').exists() else 'See the hand log for page-specific recurring forms. Independent second-reading differences are retained in `second/` and adjudicated in the changes log. Macro-only differences and editorial H notes are excluded.'
    (ROOT/f'{PREFIX}_sheet_feedback.md').write_text('# Error-sheet feedback — SP85_C13_149\n\nOne primary error-sheet kind is assigned to each material logged place, to avoid counting the same physical place repeatedly. These are observed correction counts, not error-rate estimates for all tokens. H-only disagreements are included in all-places counts.\n\n'+md_table(['Error-sheet kind','All logged places','Places changing C'],[[c,error_counts[c],against_c_categories[c]] for c in cats])+'\n## Recurrence and additional observations\n\n'+observations+'\n')
    combined='\\cotefile{149}\n'+''.join((ROOT/'pages'/f"{p['page']}.tex").read_text().rstrip()+'\n\n' for p in records)
    (ROOT/f'{PREFIX}_transcription.tex').write_text(combined)
    summary={'pages':len(records),'rows':len([r for p in records for r in p.get('rows',[])]),'against_C':sums[2],'against_H':sums[3],'decisions':len(decisions),'inventory_elements':len(inventory),'doubts':len(doubts),'audit_boxes':sum(len(p.get('audit_boxes',[])) for p in records),'events':len(events)}
    (ROOT/'records/counts.json').write_text(json.dumps(summary,indent=2))
    state_path=ROOT/'records/next_steps.json'
    state=json.loads(state_path.read_text()) if state_path.exists() else {}
    assignments_path=ROOT/'records/assignments.json'
    assignments=json.loads(assignments_path.read_text()) if assignments_path.exists() else {'first':{},'second':{}}
    order=state.get('page_order',[28,29,30,31,33,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,53])
    done=[p['scan'] for p in records]
    unassigned=[n for n in order if f'149_scan{n:03}' not in assignments.get('first',{})]
    state.update(next_unassigned=unassigned[0] if unassigned else None,first_phase_pending=[n for n in order if f'149_scan{n:03}' in assignments.get('first',{}) and n not in done],main_visual_review_complete=done,second_phase_started=bool(assignments.get('second')),updated_utc=utc())
    state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2))
    print(json.dumps(summary))

if __name__=='__main__':main()
