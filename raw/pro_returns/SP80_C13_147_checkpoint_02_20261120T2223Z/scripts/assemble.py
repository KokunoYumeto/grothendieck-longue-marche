"""Regenerate deliverables solely from the root's reviewed per-page records."""
from pathlib import Path
import csv, json, collections, re, sys
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
SCANS=list(range(108,118))+list(range(119,132))
KINDS=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertions put in the wrong place','Struck text','Abbreviations expanded, spelling modernised','Text that is not on the page','Other']

def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def cell(value):
    if value is None:return ''
    return str(value).replace('|',r'\|').replace('\n','<br>')
def code(value):return '`'+str(value).replace('`','&#96;')+'`'
def table(cols,rows):
    return '| '+' | '.join(cols)+' |\n| '+' | '.join(['---']*len(cols))+' |\n'+''.join('| '+' | '.join(map(cell,r))+' |\n' for r in rows)+'\n'
def tsv(path,cols,rows,delimiter='\t'):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=cols,delimiter=delimiter,extrasaction='ignore');w.writeheader();w.writerows(rows)
def cropshow(r):
    if not r.get('crop'):return 'page/half view'
    return r['crop']+' '+str(tuple(r.get('box',[])))

def assemble():
    data=[]
    for s in SCANS:
        p=ROOT/'review'/f'147_scan{s}_reviewed.json'
        if p.exists():data.append(json.loads(p.read_text()))
    allrows=[(d['scan'],r) for d in data for r in d['rows']]
    counts=[]
    for d in data:
        c=collections.Counter(r['confidence'] for r in d['rows'])
        counts.append([d['scan'],sum(bool(r.get('against_C')) for r in d['rows']),sum(bool(r.get('against_H')) for r in d['rows']),len(d['rows']),c['high'],c['medium'],c['low']])
    if counts:counts.append(['Total']+[sum(r[i] for r in counts) for i in range(1,7)])
    md='# Consolidated transcription: changes against witnesses C and H\n\n'
    md+='Counts are substantive locations, not tokens. One location can differ from both witnesses. Macro-only variation and certainty-only changes are excluded; doubt decisions are listed separately. Distinct changes within a crowded passage are separated when they can be located independently.\n\n'
    md+=table(['Scan','Against C','Against H','Locations','High','Medium','Low'],counts)
    md+='## Consequential corrections\n\n'
    consequential=[f"- Scan {s}, {r['place']}: {code(r['final'])}. {r.get('consequence',r['scan_shows'])}" for s,r in allrows if r.get('math_consequential')]
    md+='\n'.join(consequential)+'\n\n' if consequential else 'No mathematical correction has yet been accepted.\n\n'
    coll=[]; inv=[]; dec=[]; doubts=[]; abbr=[]; events=[]
    notes='# Notes while reading\n\nThese notes describe the supplied manuscript pages. No external sources were consulted. A report of a manuscript assertion is not a proof check; the accompanying CHECK_EVENTS.tsv distinguishes actual checks from background carried during transcription. Scan 118 is absent from the supplied set.\n\n'
    hand='# Hand and notation log\n\nObservations are local to the supplied scans. A recurring convention is applied only after checking the corresponding ink; clearly written authorial slips remain in the text.\n\n'
    for d in data:
        s=d['scan']; md+=f'## Scan {s}\n\n'
        rows=[]
        for r in d['rows']:
            rows.append([r['place'],code(r['C']),code(r['H']),code(r['final']),r['scan_shows']+'; '+cropshow(r),r['confidence']])
            if r.get('against_H'):
                coll.append(dict(folder='147',their_page=str(s-1),our_scan=str(s),line=r['place'],their_reading=r['H'],codex_reading=r['C'],final_reading=r['final'],scan_shows=r['scan_shows']+'; '+cropshow(r),kind=r['kind'],marked_in_H='yes' if r.get('marked_in_H') else 'no',confidence=r['confidence']))
        md+=table(['Place','C','H','Consolidated','What the scan shows','Confidence'],rows)
        md+='### Unresolved places\n\n'+('\n'.join('- '+x for x in d.get('unresolved',[])) or 'None.')+'\n\n'
        if d.get('audit_changes'):
            md+='### Changes after independent image-only rereading\n\n'
            md+=table(['Box/place','First reading','Blind second reading','Adjudication','Evidence'],[[r.get('box',''),code(r.get('first','')),code(r.get('second','')),code(r.get('final','')),r.get('evidence','')] for r in d['audit_changes']])
        for r in d.get('decisions',[]):
            dec.append(dict(id=r['id'],cote='147',scan=str(s),decision=r['decision'],reading=r['reading'],**{'what the ink shows':r['ink']},crop=cropshow(r) if r.get('crop') else 'page',confidence=r['confidence']))
        for r in d['inventory']:inv.append(dict(scan=str(s),**r))
        for r in d.get('doubts',[]):doubts.append([s,r['place'],code(r['reading']),code(r.get('alternatives','')),r['confidence']])
        for r in d.get('abbreviations',[]):abbr.append([r['form'],r['expansion'],str(s)])
        notes+=f'## Scan {s}\n\n'
        for i,n in enumerate(d.get('notes',[]),1):notes+=f'**N{s}-{i:02d}.** {n}\n\n'
        for e in d.get('check_events',[]):
            events.append(dict(statement_id=e['statement_id'],date=e.get('date',d.get('reviewed_at','').split(' ')[0]),who=e.get('who','GPT-6 Astra Pro; effort not separately exposed; SP80_C13_147 second-pass run'),type=e['type'],outcome=e['outcome']))
        if d.get('hand_log'):
            hand+=f'## Scan {s}\n\n'+table(['Habit','Places','Observed scope','Witness readings affected'],[[x['habit'],x['places'],x['scope'],x['misreadings']] for x in d['hand_log']])
    (ROOT/'SP80_C13_147_changes.md').write_text(md)
    tsv(ROOT/'SP80_C13_147_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
    order={r['id']:i for i,r in enumerate(csv.DictReader((BASE/'source/SP80_C13_147_texts/MARKS.tsv').open(),delimiter='\t'))}
    dec.sort(key=lambda r:order[r['id']])
    tsv(ROOT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],dec)
    tsv(ROOT/'SP80_C13_147_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,',')
    (ROOT/'SP80_C13_147_notes.md').write_text(notes)
    (ROOT/'SP80_C13_147_hand_log.md').write_text(hand)
    tsv(ROOT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
    uniqueabbr=collections.OrderedDict()
    for form,meaning,s in abbr:
        key=(form,meaning);uniqueabbr.setdefault(key,[]).append(s)
    doubtful='# Remaining doubts and notation\n\n'+(ROOT/'notation.md').read_text()+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence'],doubts)
    doubtful+='## Abbreviations encountered\n\nExpansions are editorial suggestions confined to this list. The transcription retains the manuscript forms.\n\n'+table(['Form','Suggested expansion','Scans'],[[code(k[0]),k[1],', '.join(v)] for k,v in uniqueabbr.items()])
    legibility=ROOT/'review/legibility.md'
    doubtful+='## Legibility and relative performance of the witnesses\n\n'+(legibility.read_text() if legibility.exists() else 'Final assessment will follow completion of the independent rereading.\n')
    (ROOT/'SP80_C13_147_doubts.md').write_text(doubtful)
    cats=collections.Counter(r.get('error_category','Other') for s,r in allrows)
    feedback='# Feedback on the recurring-error sheet\n\nCounts are locations in the consolidated change log. Each location is assigned one primary error category; they do not estimate error rates for the manuscript or for either witness. Certainty-only decisions and syntax-only differences are excluded.\n\n'
    feedback+=table(['Error-sheet category','Locations'],[[k,cats[k]] for k in KINDS])
    feedback+='## Observations beyond or more specific than the sheet\n\n'
    extra=ROOT/'review/feedback.md'
    feedback+=extra.read_text() if extra.exists() else 'See the hand log for specific recurring forms; final cross-page assessment is in progress.\n'
    (ROOT/'SP80_C13_147_sheet_feedback.md').write_text(feedback)
    pages=[ROOT/'pages'/f'147_scan{d["scan"]}.tex' for d in data]
    (ROOT/'SP80_C13_147_transcription.tex').write_text('\\cotefile{147}\n\n'+'\n\n'.join(p.read_text().rstrip() for p in pages)+'\n')
    print(json.dumps({'reviewed_scans':[d['scan'] for d in data],'locations':len(allrows),'C_changes':sum(bool(r.get('against_C')) for _,r in allrows),'H_changes':len(coll),'decisions':len(dec),'inventory_elements':len(inv),'remaining_doubts':len(doubts)}))

if __name__=='__main__':assemble()
