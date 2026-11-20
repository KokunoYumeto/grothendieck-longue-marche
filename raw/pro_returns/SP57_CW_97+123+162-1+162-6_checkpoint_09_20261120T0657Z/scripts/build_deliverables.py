from pathlib import Path
import csv, json, hashlib, collections, re

OUT=Path(__file__).resolve().parents[1]
NAME='SP57_CW_97+123+162-1+162-6'
order=json.loads((OUT/'page_order.json').read_text())
assembly_path=OUT/'assembly_rules.json'
assembly=json.loads(assembly_path.read_text()) if assembly_path.exists() else {}
records=[]
for m in order:
    p=OUT/'decisions'/(m['stem']+'.json')
    if p.exists(): records.append(json.loads(p.read_text()))

def cell(s):
    if isinstance(s,(dict,list)): s=json.dumps(s,ensure_ascii=False)
    return str(s or '').replace('|','&#124;').replace('\n','<br>')
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n|'+'|'.join(['---']*len(headers))+'|\n'+''.join('| '+' | '.join(cell(s) for s in row)+' |\n' for row in rows)

counts=[]; consequential=[]
for r in records:
    ds=r.get('differences',[])
    cc=sum(bool(d.get('c_changed')) for d in ds); hh=sum(bool(d.get('h_changed')) for d in ds)
    confidence=collections.Counter(d['confidence'] for d in ds if d.get('c_changed') or d.get('h_changed'))
    counts.append([r['cote']+'/'+str(r['scan']).zfill(3),cc,hh,confidence['high'],confidence['medium'],confidence['low']])
    consequential += [f"- {r['cote']}/{str(r['scan']).zfill(3)}: {s}" for s in r.get('consequential',[])]
tot=[sum(x[j] for x in counts) for j in range(1,6)]
change='# Changes and decisions\n\nCounts are loci, not words or error-rate estimates. Changes include resolved or revised doubt markings; pure macro translations are excluded. A locus may differ from both witnesses. Confidence columns count distinct loci. Retained C doubts are separately documented even where the reading is unchanged.\n\n'
change+=table(['Cote/scan','Against C','Against H','High','Medium','Low'],counts+[['TOTAL']+tot])
change+='\n## Consequential reading corrections\n\n'+ ('\n'.join(consequential) if consequential else 'None recorded so far.')+'\n'
coll=[];inv=[];doubts=[];abbreviations=[];notes='# Notes while reading\n\nEvidence is the supplied scan at each cited cote/scan and the recorded crop. No external sources were researched. These are notes on the pages; a reported statement is not thereby verified. Actual check events are in CHECK_EVENTS.tsv.\n'
for r in records:
    ref=r['cote']+'/'+str(r['scan']).zfill(3)
    change+='\n## '+ref+'\n\n'
    ds=r.get('differences',[])
    change+=table(['Place','C','H','Final','Three readers (R1; R2; R3)','What the scan shows / crop','Confidence'],[[d['place'],d.get('C',''),d.get('H',''),d.get('final',d.get('reading','')),d.get('readers',''),d.get('evidence','')+(' [crop: '+d['crop']+']' if d.get('crop') else ''),d['confidence']] for d in ds]) if ds else 'No substantive witness differences.\n'
    reviews=r.get('c_doubts',[])
    if reviews:
        change+='\n### C doubt review\n\n'+table(['Place','C reading','Final decision','Evidence / crop'],[[d.get('place',''),d.get('C',''),d.get('decision',''),d.get('evidence','')+(' [crop: '+d['crop']+']' if d.get('crop') else '')] for d in reviews])
    if r.get('s_decisions'):
        change+='\n### Witness S\n\n'+'\n'.join(r['s_decisions'])+'\n'
    change+='\n### Still unresolved\n\n'
    rem=r.get('remaining_doubts',[])
    change+=table(['Place','Reading','Alternatives','Confidence'],[[d.get('place',''),d.get('reading',''),d.get('alternatives',''),d.get('confidence','low')] for d in rem]) if rem else 'None.\n'
    for d in ds:
        if d.get('h_changed'):
            coll.append([r['folder'],r['their_page'],r['scan'],d['place'],d.get('H',''),d.get('C',''),d.get('final',d.get('reading','')),d.get('evidence','')+(' Crop: '+d['crop'] if d.get('crop') else ''),d.get('kind','other'),d.get('marked_in_H','no'),d['confidence']])
    for d in r.get('inventory',[]):
        inv.append([ref]+[d.get(k,'') for k in ['sheet_kind','hand','element','kind','position','first_words_or_objects']]+['yes'])
    for d in rem: doubts.append([ref,d.get('place',''),d.get('reading',''),d.get('alternatives',''),d.get('confidence','low')])
    for a in r.get('abbreviations',[]):
        if isinstance(a,str): abbreviations.append([ref,a,''])
        else: abbreviations.append([ref,a.get('form',a.get('abbreviation','')),a.get('expansion',a.get('meaning',''))])
    notes+='\n## '+ref+'\n\n'+r.get('notes','No mathematical assertion; documentary content recorded in the inventory.')+'\n'
(OUT/f'{NAME}_changes.md').write_text(change)
with (OUT/f'{NAME}_collation.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']);w.writerows(coll)
with (OUT/f'{NAME}_inventory.csv').open('w') as f:
    w=csv.writer(f);w.writerow(['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']);w.writerows(inv)
(OUT/f'{NAME}_notes.md').write_text(notes)
text=(OUT/'briefs/notation.md').read_text()+'\n## Remaining doubts\n\n'+table(['Cote/scan','Place','Reading','Alternatives','Confidence'],doubts)+'\n## Abbreviations (expansions are editorial, not part of the transcription)\n\n'+table(['Cote/scan','Written form','Suggested expansion'],abbreviations)
leg=OUT/'decisions/legibility.md'
if leg.exists(): text+='\n'+leg.read_text()
(OUT/f'{NAME}_doubts.md').write_text(text)
parts=[];last=None
for index,m in enumerate(order):
    p=OUT/'pages'/(m['stem']+'.tex')
    if p.exists():
        if m['cote']!=last: parts.append('\\cotefile{'+m['cote']+'}\n');last=m['cote']
        fragment=re.sub(r'\\cotefile\{[^}]+\}\s*','',p.read_text())
        content_lines=[line for line in fragment.splitlines() if line.strip() and not line.lstrip().startswith('%')]
        following=order[index+1] if index+1<len(order) else None
        continues=(content_lines and content_lines[-1].rstrip().endswith('%') and following
                   and following['cote']==m['cote'] and int(following['our_scan'])==int(m['our_scan'])+1)
        # A terminal % preserves a word divided across consecutive source sheets
        # (e.g. 123/002 ele- and 123/003 ment); do not create a new paragraph there.
        same_paragraph=assembly.get(m['stem'],{}).get('join_to_next')=='same_paragraph'
        parts.append(fragment.rstrip()+('\n' if continues or same_paragraph else '\n\n'))
(OUT/f'{NAME}_transcription.tex').write_text(''.join(parts))
print(json.dumps(dict(pages=len(records),changes_C=tot[0],changes_H=tot[1],confidence=tot[2:],collation_rows=len(coll),inventory_rows=len(inv),remaining_doubts=len(doubts))))
