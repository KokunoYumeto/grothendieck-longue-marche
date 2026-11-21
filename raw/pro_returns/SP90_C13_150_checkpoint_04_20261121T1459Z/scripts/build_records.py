"""Rebuild cumulative edition records from editor-approved page metadata.

This script does not read handwriting or settle a textual difference. All
readings and evidence originate in the visual readers' and editor's records.
"""
from pathlib import Path
import csv, json, collections, re, difflib, argparse

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'source'
PREFIX = 'SP90_C13_150'

def table(headers, rows):
    def cell(value):
        return str(value).replace('|', '\\|').replace('\n', '<br>')
    return '\n'.join(['| ' + ' | '.join(headers) + ' |',
                       '| ' + ' | '.join(['---']*len(headers)) + ' |'] +
                      ['| ' + ' | '.join(cell(x) for x in row) + ' |' for row in rows]) + '\n'

def tsv(path, headers, rows, delimiter='\t'):
    with path.open('w', encoding='utf-8', newline='') as f:
        w=csv.DictWriter(f, fieldnames=headers, delimiter=delimiter, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)

def source_marks():
    with (SOURCE/'SP90_C13_150_texts/MARKS.tsv').open() as f:
        return list(csv.DictReader(f, delimiter='\t'))

def match_marks(d, originals):
    found=[]; missing=[]; used=set()
    explicit={x['id']:x for x in d.get('decisions',[]) if 'id' in x}
    for original in originals:
        m=explicit.get(original['id'])
        if m is None:
            candidates=[(i,x) for i,x in enumerate(d.get('marks',[]))
                        if i not in used and x.get('mark','').strip()==original['the mark as written'].strip()]
            if candidates:
                i,m=max(candidates,key=lambda p:difflib.SequenceMatcher(None,p[1].get('context',''),original['the LaTeX around it']).ratio())
                used.add(i)
        if m is None:
            missing.append(original); continue
        crop=m.get('crop','page')
        if crop!='page' and m.get('box'):
            crop+=' '+str(tuple(m['box']))
        found.append({'id':original['id'],'cote':original['cote'],'scan':original['scan'],
                      'decision':m['decision'],'reading':m['reading'],
                      'what the ink shows':m.get('evidence',m.get('what the ink shows','')),
                      'crop':crop,'confidence':m['confidence']})
    return found,missing

def main():
    data=[json.loads(p.read_text()) for p in sorted((ROOT/'editor').glob('150_scan*.json'))]
    changes=[]; collation=[]; inventory=[]; decisions=[]; missing=[]; counts=[]; consequences=[]
    notation=[]; abbreviations=[]; doubts=[]; hands=[]; notes=[]; events=[]; error_counts=collections.Counter()
    marks=source_marks()
    for d in data:
        scan=d['scan']; page=f'150_scan{scan:03}'
        cc=collections.Counter()
        for i,c in enumerate(d.get('changes',[]),1):
            if not (c.get('change_C') or c.get('change_H')): continue
            cc['C']+=bool(c.get('change_C'));cc['H']+=bool(c.get('change_H'));cc[c['confidence']]+=1
            c=dict(c,scan=scan,change_id=f'{page}.c{i:02}')
            changes.append(c); error_counts[c.get('error_kind','other')]+=1
            if c.get('consequential'): consequences.append((scan,c['place'],c['consequential']))
            if c.get('change_H'):
                collation.append({'folder':'150','their_page':scan-1,'our_scan':scan,'line':c['place'],
                    'their_reading':c['H'],'codex_reading':c['C'],'final_reading':c['final'],
                    'scan_shows':evidence(c),'kind':c['kind'],
                    'marked_in_H':'yes' if c.get('marked_in_H') else 'no','confidence':c['confidence']})
        counts.append((scan,cc['C'],cc['H'],cc['high'],cc['medium'],cc['low']))
        for x in d.get('inventory',[]): inventory.append(dict(x,scan=scan))
        matched,unmatched=match_marks(d,[m for m in marks if int(m['scan'])==scan]);decisions+=matched;missing+=unmatched
        for k,target in [('notation',notation),('abbreviations',abbreviations),('doubts',doubts),('hand_log',hands)]:
            for x in d.get(k,[]): target.append(dict(x,scan=scan))
        notes.append((scan,d.get('notes',[])))
        for x in d.get('check_events',[]):
            events.append({'statement id':x['statement_id'],'date':d.get('reviewed_at',''),
                           'who (model, effort, run)':x.get('who','GPT-6 Astra Pro; inherited effort; SP90_C13_150'),
                           'type':x['type'],'outcome':x['outcome']})
        boxes=[]; first=[]
        for b in d.get('second_boxes',[]):
            x0,y0,x1,y1=b['coords'];boxes.append({'box':b['box'],'kind':b['kind'],'x0':x0,'y0':y0,'x1':x1,'y1':y1})
            first.append({'box':b['box'],'reading':b['reading']})
        # The first readings are frozen before independent second readers receive boxes.
        if not (ROOT/'reference/first_readings_frozen.json').exists() and not (ROOT/'second'/f'{page}_second.tsv').exists():
            tsv(ROOT/'second'/f'{page}_boxes.tsv',['box','kind','x0','y0','x1','y1'],boxes)
            tsv(ROOT/'second'/f'{page}_first.tsv',['box','reading'],first)

    total=tuple(['All']+[sum(x[i] for x in counts) for i in range(1,6)])
    text='# Changes and visual adjudications\n\n'
    text+='Each row is one recorded place, not a token count. C/H columns count substantive or diplomatic differences from each witness; a row can count against both. Resolution of a source doubt is included when recorded as a reading decision. New uncertainty alone is listed in the doubts file. Macro-only differences and H editorial annotations are excluded. Pixel boxes refer to the supplied original scans.\n\n'
    text+=table(['Scan','Against C','Against H','High','Medium','Low'],counts+[total])
    text+='\n## Consequential corrections\n\n'
    text+='\n'.join(f'- Scan {s}, {p}: {c}' for s,p,c in consequences) or 'None recorded.'
    text+='\n'
    for d in data:
        scan=d['scan']; text+=f'\n## Scan {scan:03}\n\n'
        rows=[(c['place'],code(c['C']),code(c['H']),code(c['final']),evidence(c),c['confidence']) for c in changes if c['scan']==scan]
        text+=table(['Place','Witness C','Witness H','Consolidated reading','What the scan shows','Confidence'],rows)
        audit=d.get('audit_changes',[])
        if audit:
            text+='\n### Changes after the independent image reading\n\n'
            text+='These entries preserve the independently written readings and the editor\'s decision. They do not add duplicate witness-change counts to the table above.\n\n'
            text+=table(['Box / place','First reading','Independent second reading','Final reading','Visual adjudication','Confidence'],
                        [(x.get('audit_box',x.get('place','')),code(x['first']),code(x['second']),code(x['final']),evidence(x),x['confidence']) for x in audit])
        text+='\n### Unresolved places\n\n'
        ds=d.get('doubts',[])
        text+=('\n'.join(f"- {x['place']}: {code(x['reading'])}; alternatives: {x.get('alternatives','')}; confidence {x['confidence']}." for x in ds) if ds else 'No unresolved reading recorded.')+'\n'
    (ROOT/f'{PREFIX}_changes.md').write_text(text)
    tsv(ROOT/f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    tsv(ROOT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decisions)
    tsv(ROOT/f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
    nt='# Notation table\n\n'+table(['Scan','Written form','Meaning or form of the strokes','Places'],[(x['scan'],code(x['form']),x['meaning_or_shape'],x.get('places','')) for x in notation])
    (ROOT/'reference/notation.md').write_text(nt)
    dt=nt+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence'],[(x['scan'],x['place'],code(x['reading']),code(x.get('alternatives','')),x['confidence']) for x in doubts])
    dt+='\n## Abbreviations\n\nExpansions in this table are editorial suggestions and are not supplied in the transcription.\n\n'+table(['Scan','Written form','Suggested expansion'],[(x['scan'],code(x['form']),x['expansion']) for x in abbreviations])
    dt+='\n## Legibility and witness comparison\n\n'
    dt+=(ROOT/'reference/legibility_note.txt').read_text() if (ROOT/'reference/legibility_note.txt').exists() else 'Assessment remains provisional until all pages and independent second readings have been completed.\n'
    (ROOT/f'{PREFIX}_doubts.md').write_text(dt)
    ht='# Hand log\n\n'+table(['Scan','Habit','Places','Consistency on examined occurrences','Witness errors'],[(x['scan'],x['habit'],x.get('places',''),x.get('consistent',''),x.get('witness_errors','')) for x in hands])
    (ROOT/f'{PREFIX}_hand_log.md').write_text(ht)
    no='# Reading notes\n\nThese notes report the manuscript and record local mathematical checks used in reading. A reported assertion is not thereby verified. No external sources were consulted. Scan numbers identify the attached primary sources.\n'
    for s,items in notes:
        no+=f'\n## Scan {s:03}\n\n'+'\n\n'.join(items)+'\n'
    (ROOT/f'{PREFIX}_notes.md').write_text(no)
    tsv(ROOT/'CHECK_EVENTS.tsv',['statement id','date','who (model, effort, run)','type','outcome'],events)
    kinds=['symbols and indices','words','omissions','drawings and diagrams','readable ink left as illegible','insertion placement','struck text','abbreviation/spelling','text not on page','other']
    feedback='# Error-sheet feedback\n\nCounts are recorded places assigned a principal category, not inferred rates or counts of characters. A place with several defects is counted once under its principal category.\n\n'+table(['Error-sheet category','Places'],[(k,error_counts[k]) for k in kinds])
    feedback+='\n## Recurring features and additional observations\n\nSee the hand log for page-specific forms and witness errors. '+((ROOT/'reference/feedback_extra.txt').read_text() if (ROOT/'reference/feedback_extra.txt').exists() else 'Final assessment pending the complete second reading.')+'\n'
    (ROOT/f'{PREFIX}_sheet_feedback.md').write_text(feedback)
    pages=sorted((ROOT/'pages').glob('150_scan*.tex'))
    (ROOT/f'{PREFIX}_transcription.tex').write_text('\\cotefile{150}\n\n'+'\n\n'.join(p.read_text().rstrip() for p in pages)+'\n')
    report={'pages':len(data),'change_rows':len(changes),'C':total[1],'H':total[2],'decisions':len(decisions),'missing_marks':missing,'inventory_elements':len(inventory),'second_boxes':sum(len(x.get('second_boxes',[])) for x in data)}
    print(json.dumps(report,ensure_ascii=False,indent=2))

def code(s):
    return '`'+str(s).replace('`','\\`')+'`'

def evidence(c):
    result=c.get('evidence','')
    if c.get('crop'):
        result+=' Crop: '+c['crop']
        if c.get('box'): result+='; original pixels '+str(tuple(c['box']))
        result+='.'
    if c.get('second_adjudication'): result+=' Second reading: '+c['second_adjudication']
    return result

if __name__=='__main__': main()
