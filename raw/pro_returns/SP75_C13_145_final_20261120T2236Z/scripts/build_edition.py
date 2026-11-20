"""Assemble deliverables only from reports explicitly adjudicated by the main reader."""
from pathlib import Path
import csv, json, re, collections

ED = Path(__file__).resolve().parents[1]
ROOT = ED.parent
PREFIX = 'SP75_C13_145'

def table(headers, rows):
    def cell(x):
        return str(x).replace('|','&#124;').replace('\n','<br>')
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(cell(x) for x in row)+' |' for row in rows])+'\n'

def write_csv(path, headers, rows, delim='\t'):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=headers,delimiter=delim,extrasaction='ignore'); w.writeheader(); w.writerows(rows)

def locus_evidence(c):
    crop=c.get('crop','')
    box=c.get('box',[])
    return c.get('ink','')+(f' [{crop}; original pixels {tuple(box)}]' if crop else '')

def is_substantive(c):
    return c['c_changed'] or c['h_changed']

def locus_label(c):
    label=c['id']+' / '+c['place']
    return label if is_substantive(c) else label+' [noncounted observation]'

reports=[json.loads(p.read_text()) for p in sorted((ED/'reader_reports').glob('*_reviewed.json'))]
reports.sort(key=lambda r:r['scan'])
allchanges=[(r['scan'],c) for r in reports for c in r['changes']]
substantivechanges=[(scan,c) for scan,c in allchanges if is_substantive(c)]
counts=[]
for r in reports:
    counted=[c for c in r['changes'] if is_substantive(c)]
    cc=collections.Counter(c['confidence'] for c in counted)
    counts.append([f"{r['scan']:03d}",len(counted),sum(bool(c['c_changed']) for c in counted),sum(bool(c['h_changed']) for c in counted),cc['high'],cc['medium'],cc['low']])
if counts: counts.append(['Total']+[sum(row[i] for row in counts) for i in range(1,7)])
changes=['# Consolidated reading: changes against witnesses C and H\n',
'Counts refer to distinct documented substantive loci, not tokens. A locus may differ from both witnesses. Pure macro substitutions and editorial witness headings are excluded. Rows with neither witness-change flag set remain fully published below as noncounted observations, but are excluded from locus, witness, confidence and feedback-category totals. Certainty-only observations remain in the doubt apparatus and may also be retained as explicitly noncounted rows.\n',
table(['Scan','Substantive loci','Against C','Against H','High','Medium','Low'],counts),
'## Consequential corrections\n']
consequential=[f"- Scan {scan:03d}, {c['place']} ({c['id']}): {c['math_consequence']}" for scan,c in substantivechanges if c.get('math_consequence')]
changes+=['\n'.join(consequential) if consequential else 'No consequential correction recorded in the pages finalized so far.']
collation=[]; decisions=[]; inventory=[]; doubts=[]; notes=[]; events=[]; hand=[]; notations=[]; abbrev=[]
feedback=collections.Counter(); examples=collections.defaultdict(list)
for r in reports:
    scan=r['scan']; stem=f'145_scan{scan:03d}'
    changes.append(f'\n## Scan {scan:03d}\n')
    changes.append(table(['ID / place','C','H','Final','What the scan shows','Confidence'],[
      [locus_label(c),c['C'],c['H'],c['final'],locus_evidence(c),c['confidence']] for c in r['changes']]))
    changes.append('### Remaining unresolved places\n')
    changes.append('\n'.join('- '+d['place']+': '+d['reading']+' — '+d.get('reason','') for d in r['doubts']) or 'None recorded.')
    if r.get('unlisted_decisions'):
        changes.append('### Decisions on C doubts absent from MARKS.tsv\n')
        changes.append(table(['Local ID','Decision','Reading','Ink evidence','Crop / pixels','Confidence'], [[d['id'],d['decision'],d['reading'],d['ink'],str(d.get('crop',''))+' '+str(d.get('box',[])),d['confidence']] for d in r['unlisted_decisions']]))
    if r.get('audit'):
        a=r['audit']
        changes.append('### Independent image-only second reading\n')
        changes.append(f"{a['boxes_read']} boxes read; {len(a['differences'])} boxes differed token by token; {sum(bool(x['changed']) for x in a['differences'])} adjudicated boxes changed the first consolidated reading. First and independent readings are preserved verbatim in second/.\n")
        changes.append(table(['Box','First consolidated reading','Independent reading','Adjudicated reading','Changed','Decision and ink evidence','Crop / original pixels'],[[x['box'],x['first'],x['second'],x['final'],'yes' if x['changed'] else 'no',x['adjudication']+' — '+x['ink'],x['crop']+' '+str(x['coords'])] for x in a['differences']]))
    for c in r['changes']:
        if c['h_changed']:
            # Scope matters: a doubt elsewhere in a quoted full formula does
            # not mark the particular differing sign. The main reader reviews
            # flags against H's explicit macros and editorial uncertainty notes.
            hmarked=c.get('marked_in_H','no')
            collation.append(dict(folder='145',their_page=str(scan-1),our_scan=str(scan),line=c['place'],their_reading=c['H'],codex_reading=c['C'],final_reading=c['final'],scan_shows=locus_evidence(c),kind={'deletion state':'deletion state (struck given live or live given struck)'}.get(c['kind'],c['kind']),marked_in_H=hmarked,confidence=c['confidence']))
        if is_substantive(c):
            categories=c.get('error_category',[])
            if isinstance(categories,int): categories=[categories]
            for cat in set(categories):
                feedback[int(cat)]+=1; examples[int(cat)].append(c['id'])
    for d in r['decisions']:
        decisions.append({'id':d['id'],'cote':'145','scan':str(scan),'decision':d['decision'],'reading':d['reading'],'what the ink shows':d['ink'],'crop':f"{d.get('crop','')} scan {scan:03d} {tuple(d.get('box',[]))}" if d.get('crop') else 'page','confidence':d['confidence']})
    for row in r['inventory']:
        row=dict(row);row['scan']=str(scan);inventory.append(row)
    for d in r['doubts']: doubts.append([f'{scan:03d}',d['place'],d['reading'],d.get('alternatives',''),d['confidence'],d.get('reason','')])
    notes.append(f'\n## Scan {scan:03d}\n\n'+ ('\n\n'.join(r['notes']) if isinstance(r['notes'],list) else r['notes']))
    for e in r.get('check_events',[]):
        events.append({'statement id':e['statement_id'],'date':e.get('date','2026-11-20'),'who (model, effort, run)':e.get('who','GPT-6 Astra Pro; inherited effort not exposed; cote 145 second pass, '+r.get('reader','reader')),'type':e['type'],'outcome':e['outcome']})
    for h in r.get('hand',[]): hand.append((scan,h))
    for n in r.get('notation',[]): notations.append((scan,n))
    for a in r.get('abbreviations',[]): abbrev.append((scan,a))
    # Freeze the initial box readings at first page completion. Later audit edits do not overwrite them.
    boxespath=ED/'second'/(stem+'_boxes.tsv'); firstpath=ED/'second'/(stem+'_first.tsv')
    if not boxespath.exists():
        write_csv(boxespath,['box','kind','x0','y0','x1','y1'],[dict(box=b['box'],kind=b['kind'],**dict(zip(['x0','y0','x1','y1'],b['coords']))) for b in r['second_boxes']])
        write_csv(firstpath,['box','reading'],[{'box':b['box'],'reading':b['reading']} for b in r['second_boxes']])

(ED/(PREFIX+'_changes.md')).write_text('\n'.join(changes)+'\n')
write_csv(ED/(PREFIX+'_collation.tsv'),['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
source_marks=list(csv.DictReader((ROOT/'source/SP75_C13_145_texts/MARKS.tsv').open(),delimiter='\t'))
mark_order={r['id']:i for i,r in enumerate(source_marks)}
decisions.sort(key=lambda d:mark_order[d['id']])
write_csv(ED/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decisions)
write_csv(ED/(PREFIX+'_inventory.csv'),['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
write_csv(ED/'CHECK_EVENTS.tsv',['statement id','date','who (model, effort, run)','type','outcome'],events)
(ED/(PREFIX+'_notes.md')).write_text('# Notes while reading\n\nThe following are accounts of the manuscript and local reading decisions, not an independent proof of all its mathematical claims. No sources beyond the supplied pages and witnesses were researched. Actual verification events, where any occurred, are distinguished in CHECK_EVENTS.tsv.\n\nPrimary source: Grothendieck, A. (n.d.). *Printemps 81 (vieille rédaction)[149]: Notes manuscrites* [Manuscript, cote 145]. Montpellier archive. The title and archival identification are those supplied with the task; each heading gives the scan locator. Witnesses C and H are the supplied derivative readings, not independent evidence for an inscription.\n'+'\n'.join(notes)+'\n')
def describe(x):
    return x if isinstance(x,str) else '; '.join(f'{k}: {v}' for k,v in x.items())
working=(ED/'notation.md').read_text()
doubt_text=[working,'\n## Page-grounded notation observations\n',table(['Scan','Observation'],[[f'{s:03d}',describe(n)] for s,n in notations]),'\n## Remaining doubts\n',table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts),'\n## Abbreviations (expansions only here)\n',table(['Scan','Written form','Proposed expansion','Place'],[[f'{s:03d}',a.get('form',''),a.get('expansion',''),a.get('place','')] for s,a in abbrev]),'\n## Legibility and witness comparison\n']
legibility=ED/'legibility_note.txt'
doubt_text.append(legibility.read_text() if legibility.exists() else 'Assessment in progress; unresolved readings are preserved explicitly above. Both witnesses are treated as fallible readings of the same image.')
(ED/(PREFIX+'_doubts.md')).write_text('\n'.join(doubt_text)+'\n')
(ED/(PREFIX+'_hand_log.md')).write_text('# Hand log — cote 145\n\nObservations are scoped to the pages specified. A recurrent shape is not authority to overwrite a visibly different letter.\n\n'+table(['Scan','Observed habit, scope and witness consequences'],[[f'{s:03d}',describe(h)] for s,h in hand]))
categories={1:'Symbols and indices',2:'Words',3:'Omissions',4:'Drawings and diagrams',5:'Readable ink left as illegible',6:'Insertions put in the wrong place',7:'Struck text',8:'Abbreviations expanded / spelling modernised',9:'Text not on the page',10:'Other'}
(ED/(PREFIX+'_sheet_feedback.md')).write_text('# Feedback on the error sheet\n\nCounts below count documented substantive loci of the indicated kind in this run, regardless of which witness was corrected. Categories can overlap; they are not token error rates or a census of all occurrences. Macro-only differences, explicitly noncounted observations and unverified historical rates are excluded.\n\n'+table(['Kind','Loci','Locus IDs'],[[f'{i}. {categories[i]}',feedback[i],', '.join(examples[i])] for i in range(1,11)])+'\n## Additional recurring observations\n\n'+((ED/'feedback_observations.md').read_text() if (ED/'feedback_observations.md').exists() else 'See the hand log for page-scoped observations. No additional class is asserted unless supported by repeated observed loci.\n'))
texts=[]
for r in reports:
    p=ED/'pages'/f"145_scan{r['scan']:03d}.tex"
    if p.exists(): texts.append(p.read_text().rstrip())
(ED/(PREFIX+'_transcription.tex')).write_text('\\cotefile{145}\n\n'+'\n\n'.join(texts)+'\n' if texts else '')
print(json.dumps({'reviewed_pages':len(reports),'change_loci':len(substantivechanges),'noncounted_observations':len(allchanges)-len(substantivechanges),'published_reading_records':len(allchanges),'collation_rows':len(collation),'decisions':len(decisions),'inventory':len(inventory),'doubts':len(doubts)}))
