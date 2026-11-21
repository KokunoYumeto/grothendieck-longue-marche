from pathlib import Path
import json,csv,collections,shutil,datetime
W=Path(__file__).resolve().parents[1]
P='SP89_C13_149+150'
ORDER=(W/'scripts/page_order.txt').read_text().splitlines()
def now():return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def write_tsv(path,fields,rows,delimiter='\t'):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore');w.writeheader();w.writerows(rows)
def esc(s):return str(s).replace('|','&#124;').replace('\n','<br>')
def table(headers,rows):return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(esc(c) for c in row)+' |\n' for row in rows)+'\n'
def code(s):return '`'+str(s).replace('`','&#96;')+'`'
def reports():
 r=[]
 for p in ORDER:
  f=W/'reports'/p/'report.json'
  if f.exists():
   x=json.loads(f.read_text())
   if x.get('main_reviewed'):r.append(x)
 return r
def aggregate():
 rs=reports();changes=[];coll=[];dec=[];inv=[];events=[];notes=[];hand=[];doubts=[];abbr=[];cons=[];counts=[]
 notation={}
 # Editorial grouping of equivalent table entries only; this never edits a
 # transcription or replaces a locally different glyph in the source.
 grouping_path=W/'reports/notation_groups.json'
 groups=json.loads(grouping_path.read_text()).get('groups',[]) if grouping_path.exists() else []
 aliases={alias:g for g in groups for alias in g.get('aliases',[g['form']])}
 for r in rs:
  for n in r.get('notation',[]):
   group=aliases.get(n['form'])
   form=group['form'] if group else n['form']
   entry=notation.setdefault(form,dict(meanings=[],evidence=[]))
   meaning=(group['meaning'] if group else n['meaning']).rstrip('.')
   if meaning not in entry['meanings']:entry['meanings'].append(meaning)
   entry['evidence'].append(r['page']+': '+n['evidence'])
 notation_text='# Notation table — current\n\nThe entries below are established or explicitly unresolved readings from the accepted pages. Local changes of notation and clear authorial slips are preserved; a resemblance of letter shapes does not by itself justify making different symbols identical.\n\n'
 notation_text+=table(['Written form','Use on these pages','Attestations and stroke evidence'],[[code(form),'; '.join(v['meanings']),'<br>'.join(v['evidence'])] for form,v in notation.items()])
 (W/'notation.md').write_text(notation_text)
 for r in rs:
  p=r['page'];cote,scan=p.split('_scan');ch=r['changes']
  co=collections.Counter(x['confidence'] for x in ch)
  counts.append([p,len(ch),sum(bool(x['against_c']) for x in ch),sum(bool(x['against_h']) for x in ch),co['high'],co['medium'],co['low']])
  s='## '+p+'\n\n'+table(['Place','Witness C','Witness H','Final reading','What the scan shows; crop and original pixel box','Confidence'],[[x['place'],code(x['c']),code(x['h']),code(x['final']),x['evidence']+' '+(f"[{x.get('crop','page')}; {','.join(map(str,x.get('box',[])))}]"),x['confidence']] for x in ch])
  s+='### Unresolved places\n\n'
  s+=table(['Place','Reading','Alternatives','Reason','Confidence'],[[x['place'],code(x['reading']),code(x.get('alternatives','')),x.get('reason',''),x['confidence']] for x in r['doubts']]) if r['doubts'] else 'None remaining in this page.\n\n'
  if r.get('audit_changes'):
   s+='### Changes after the independent image-only reading\n\n'
   s+=table(['Box / place','First reading','Independent second reading','Final reading','Main-reader crop adjudication'],[[x['place'],code(x['first']),code(x['second']),code(x['final']),x['evidence']+' ['+x['crop']+']'] for x in r['audit_changes']])
  changes.append(s)
  for x in ch:
   if x.get('consequential'):cons.append(f"- {p}, {x['place']}: {code(x['c'])} / {code(x['h'])} → {code(x['final'])}. {x['evidence']}\n")
   if x['against_h']:
    coll.append(dict(folder=cote,their_page=str(int(scan)-1),our_scan=str(int(scan)),line=x['place'],their_reading=x['h'],codex_reading=x['c'],final_reading=x['final'],scan_shows=x['evidence']+' '+x.get('crop','page')+' '+str(x.get('box',[])),kind=x['kind'],marked_in_H='yes' if x['marked_in_h'] else 'no',confidence=x['confidence']))
  for d in r['decisions']:
   d=dict(d);d['what the ink shows']=d.pop('evidence');d['crop']=d.get('crop','page')+(' '+str(d.get('box',[])) if d.get('crop')!='page' else '');dec.append(d)
  inv.extend(r['inventory'])
  for e in r['check_events']:events.append(dict(statement_id=e['statement_id'],date=e.get('date',datetime.datetime.now(datetime.timezone.utc).date().isoformat()),who=e.get('who',r.get('reader','reader')+'; GPT-6 Astra Pro; inherited effort; SP89 second pass'),type=e['type'],outcome=e['outcome']))
  notes.append('## '+p+'\n\n'+''.join('### '+n['id']+'\n\n'+n['text']+'\n\n' for n in r['notes']))
  for h in r['hand']:hand.append([p,h['habit'],h['places'],h['consistency'],h['witness_errors']])
  for d in r['doubts']:doubts.append([p,d['place'],code(d['reading']),code(d.get('alternatives','')),d['confidence'],d.get('reason','')])
  for a in r['abbreviations']:abbr.append([p,code(a['form']),a['expansion']])
 total=["TOTAL"]+[sum(row[i] for row in counts) for i in range(1,7)]
 intro='# Changes against witnesses C and H\n\nRows identify local readings or source states, not differences in TeX macro syntax. A resolved C doubt is a recorded certainty decision even when its preferred letters remain unchanged. Counts are local decisions, not token counts. Original image coordinates are (x0,y0,x1,y1).\n\n'
 (W/f'{P}_changes.md').write_text(intro+table(['Page','Rows','Against C','Against H','High','Medium','Low'],counts+[total])+'## Consequential corrections\n\n'+(''.join(cons) or 'None recorded yet.\n')+'\n'+''.join(changes))
 write_tsv(W/f'{P}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
 original=W.parent/'source/SP89_C13_149+150_texts/MARKS.tsv'
 with original.open() as f:markorder={d['id']:i for i,d in enumerate(csv.DictReader(f,delimiter='\t'))}
 dec.sort(key=lambda d:markorder[d['id']])
 write_tsv(W/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],dec)
 write_tsv(W/f'{P}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,',')
 write_tsv(W/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
 (W/f'{P}_notes.md').write_text('# Notes while reading\n\nThese notes report the source and record local mathematical diagnostics. The transcription preserves clear authorial slips. Reporting a statement is not a proof check; actual checks, uses and background dependencies are distinguished in CHECK_EVENTS.tsv. No external sources were researched.\n\n'+''.join(notes))
 (W/f'{P}_hand_log.md').write_text('# Hand log\n\nThe supplied earlier logs were consulted for cote-specific leads, but every habit below is grounded in the current scans; no prior reading is authority.\n\n'+table(['Page','Habit','Places','Extent of consistency','Witness errors'],hand))
 (W/f'{P}_doubts.md').write_text((W/'notation.md').read_text()+'\n# Remaining doubts\n\n'+table(['Page','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'# Abbreviations\n\nExpansions are explanatory only and are never substituted in the transcription.\n\n'+table(['Page','Written form','Probable expansion'],abbr)+'# Legibility and comparative reliability\n\n'+((W/'reports/legibility.txt').read_text() if (W/'reports/legibility.txt').exists() else 'Assessment is in progress. No unreviewed page is represented as complete.\n'))
 text=[];last_cote=None
 for r in rs:
  f=W/'pages'/f"{r['page']}.tex"
  if f.exists():
   cote=r['page'].split('_')[0]
   if cote!=last_cote:text.append('\\cotefile{'+cote+'}\n');last_cote=cote
   text.append(f.read_text().rstrip()+'\n')
 (W/f'{P}_transcription.tex').write_text('\n'.join(text))
 cats=['1 Symbols and indices','2 Words','3 Omissions','4 Drawings and diagrams','5 Readable ink left as illegible','6 Insertions put in wrong place','7 Struck text','8 Abbreviations expanded or spelling modernised','9 Text not on page','10 Other']
 counter=collections.Counter()
 places=collections.defaultdict(list)
 for r in rs:
  for x in r['changes']:
   cat=str(x.get('error_category','10 Other'));num=cat.split()[0]
   category=next((c for c in cats if c.split()[0]==num),'10 Other')
   counter[category]+=1;places[category].append(r['page']+': '+x['id']+' ('+x['place']+')')
 feedback='# Feedback on the error sheet\n\nCounts concern recorded local decisions against one or both witnesses; a place is classified by its primary issue so totals do not double count. Certainty resolutions are included in the relevant class. These counts do not estimate an error rate for the manuscript.\n\n'+table(['Kind','Places','Locations'],[[c,counter[c],'; '.join(places[c])] for c in cats])
 extra=W/'reports/feedback_extra.md'
 feedback+='## Additional recurrent issues\n\n'+(extra.read_text() if extra.exists() else 'To be assessed after all pages and independent rereadings are complete.\n')
 (W/f'{P}_sheet_feedback.md').write_text(feedback)
 print('Aggregated',len(rs),'pages;',sum(len(r['changes']) for r in rs),'changes;',len(dec),'mark decisions;',len(inv),'inventory elements')
if __name__=='__main__':aggregate()
