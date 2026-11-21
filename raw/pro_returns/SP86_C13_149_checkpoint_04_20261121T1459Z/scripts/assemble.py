from pathlib import Path
import csv,json,re,hashlib
from datetime import datetime,timezone

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
PREFIX='SP86_C13_149'

def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def cell(x): return str(x).replace('|','&#124;').replace('\n','<br>').replace('\r','')
def table(headers,rows):
 return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(cell(v) for v in row)+' |\n' for row in rows)
def write_tsv(path,fields,rows):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
def load_reports():
 return [json.loads(p.read_text()) for p in sorted((BASE/'reviews').glob('149_scan*.json'))]

def build():
 reports=load_reports()
 editorial_path=BASE/'final_editorial.json'
 editorial=json.loads(editorial_path.read_text()) if editorial_path.exists() else {}
 changes=[];coll=[];decs=[];inv=[];doubts=[];abbr=[];notations=[];hands=[];checks=[];notes=[];counts=[];conseq=[]
 for r in reports:
  page=r['page'];scan=r['scan'];rows=r['changes']
  counts.append([f'{scan:03d}',sum(bool(x.get('against_C')) for x in rows),sum(bool(x.get('against_H')) for x in rows),*[sum(x['confidence']==c for x in rows) for c in ['high','medium','low']],len(rows)])
  changes.append(f'## Scan {scan:03d}\n\n'+table(['Place','Witness C','Witness H','Consolidated reading','What the scan shows; crop and original pixels','Confidence'],[[x['place'],x['C'],x['H'],x['final'],x['evidence']+(' — `'+x.get('crop','')+'` '+str(tuple(x['box'])) if x.get('crop') else ''),x['confidence']] for x in rows]))
  changes.append('\nRemaining unresolved places: '+('; '.join(f"{x['place']}: `{x['reading']}` ({x.get('reason','')})" for x in r['doubts']) or 'None recorded.')+'\n')
  observations=r.get('nonmaterial_observations',[])
  if observations:
   changes.append('\n### Uncounted observations\n\nThese preserve uncertainty or document the rendering of the same written form; they are excluded from the material-change totals.\n\n'+table(['Place','Witness C','Witness H','Reading / observation','Evidence'],[[x.get('place',x.get('id','')),x.get('C',''),x.get('H',''),x.get('final',x.get('reading','')),x.get('evidence',x.get('reason',''))+(' — `'+x['crop']+'` '+str(tuple(x.get('box',[]))) if x.get('crop') else '')] for x in observations]))
  audit_changed=[x for x in r.get('audit_adjudications',[]) if x.get('changed')]
  if audit_changed:
   changes.append('\n### Changes made after the independent image-only reading\n\n'+table(['Box / place','First reading','Independent reading','Final reading','Crop adjudication'],[[x['box']+(' — '+x['place'] if x.get('place') else ''),x['first'],x['second'],x['final'],x['evidence']+' — `'+x['crop']+'` '+str(tuple(x['coords']))] for x in audit_changed]))
  for x in rows:
   if x.get('against_H'):
    coll.append({'folder':'149','their_page':scan-1,'our_scan':scan,'line':x['place'],'their_reading':x['H'],'codex_reading':x['C'],'final_reading':x['final'],'scan_shows':x['evidence']+(' | '+x['crop']+' '+str(tuple(x['box'])) if x.get('crop') else ''),'kind':x['kind'],'marked_in_H':'yes' if x.get('marked_in_H') else 'no','confidence':x['confidence']})
   if x.get('consequential'):conseq.append(f"- Scan {scan:03d}, {x['place']}: `{x['final']}`. {x.get('consequence',x['evidence'])}")
  for x in r['decisions']:
   decs.append({'id':x['id'],'cote':'149','scan':scan,'decision':x['decision'],'reading':x['reading'],'what the ink shows':x['evidence'],'crop':x['crop'],'confidence':x['confidence']})
  for x in r['inventory']:inv.append({'scan':scan,**x})
  for x in r['doubts']:doubts.append([f'{scan:03d}',x['place'],x['reading'],x['alternatives'],x['confidence'],x.get('reason','')])
  for x in r['abbreviations']:abbr.append([x['written'],x['expansion'],f"{scan:03d}: {x['places']}"])
  for x in r['notation']:notations.append([x['form'],x['meaning'],f"{scan:03d}: {x['places']}"])
  for x in r['hand']:hands.append([x['form'],x['observation'],f"{scan:03d}: {x['places']}",x['scope'],x['witness_errors']])
  for x in r['check_events']:checks.append({'statement id':x['statement_id'],'date':x.get('date',r.get('accepted_utc',utc())),'who':x.get('who',f"GPT-6 Astra Pro; {r['reader']}; effort not exposed; SP86_C13_149"),'type':x['type'],'outcome':x['outcome']})
  notes.append(f'## Scan {scan:03d}\n\n'+'\n\n'.join(r['notes'])+'\n')
  boxes=[{'box':x['box'],'kind':x['kind'],**dict(zip(['x0','y0','x1','y1'],x['coords']))} for x in r['audit_boxes']]
  first=[{'box':x['box'],'reading':x['reading']} for x in r['audit_boxes']]
  # Blind-reading inputs are frozen when the audit begins; no rewrite then.
  if not (BASE/'second'/'input_manifest.json').exists() and not (BASE/'second'/f'{page}_second.tsv').exists():
   write_tsv(BASE/'second'/f'{page}_boxes.tsv',['box','kind','x0','y0','x1','y1'],boxes)
   write_tsv(BASE/'second'/f'{page}_first.tsv',['box','reading'],first)
 totals=['Total']+[sum(int(r[i]) for r in counts) for i in range(1,7)]
 audited=sum(bool(r.get('audit',{}).get('completed_utc')) for r in reports)
 head=f'# {PREFIX}: changes against both witnesses\n\nMaterial readings and source-state differences only; macro equivalences and editorial page markers are excluded. A resolved C doubt is counted as a reading decision; adding, narrowing or broadening an unresolved doubt alone is excluded. Counts refer to places, so one row may differ from both witnesses. {len(reports)} of 23 supplied scans have received the main reader’s review; {audited} have also completed the independent image-only reading and crop adjudication.\n\n'
 head+=table(['Scan','Against C','Against H','High','Medium','Low','Rows'],counts+[totals])
 head+='\n## Consequential corrections\n\n'+('\n'.join(conseq) or 'None recorded yet.')+'\n\n'
 (BASE/f'{PREFIX}_changes.md').write_text(head+'\n'.join(changes))
 write_tsv(BASE/f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
 order={line.split('\t')[0]:i for i,line in enumerate((ROOT/'source/SP86_C13_149_texts/MARKS.tsv').read_text().splitlines()[1:])}
 decs.sort(key=lambda d:order.get(d['id'],99999));write_tsv(BASE/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decs)
 with (BASE/f'{PREFIX}_inventory.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],extrasaction='ignore');w.writeheader();w.writerows(inv)
 nd='# Notation table\n\n'+editorial.get('notation_review','')+('\n\n' if editorial.get('notation_review') else '')+table(['Written form / LaTeX','Meaning or transcription observation','Confirmed places'],notations)
 (BASE/'notation.md').write_text(nd)
 (BASE/f'{PREFIX}_doubts.md').write_text(nd+'\n# Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'\n# Abbreviations\n\nExpansions are editorial aids confined to this list.\n\n'+table(['Written form','Proposed expansion','Places'],abbr)+'\n# Legibility and witness comparison\n\n'+editorial.get('legibility','The reading is in progress. Detailed local uncertainty is retained above; no global accuracy claim is made.\n'))
 (BASE/f'{PREFIX}_hand_log.md').write_text('# Hand log for the supplied cote 149 pages\n\nObservations are limited to the explicitly listed occurrences. Earlier hand logs served only as prompts for local inspection.\n\n'+table(['Form','Observed strokes or habit','Places','Scope','Witness reading affected'],hands)+editorial.get('hand_review',''))
 (BASE/f'{PREFIX}_notes.md').write_text('# Notes while reading\n\nThese notes describe the source pages and identify the mathematical checks actually performed. The author’s conjectures and qualifications remain attributed to the manuscript. Nothing beyond the supplied pages was researched.\n\n'+'\n'.join(notes)+editorial.get('notes_appendix',''))
 write_tsv(BASE/'CHECK_EVENTS.tsv',['statement id','date','who','type','outcome'],checks)
 kinds=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertions put in the wrong place','Struck text','Abbreviations expanded, spelling modernised','Text that is not on the page','Other']
 allrows=[(r['scan'],x) for r in reports for x in r['changes']]
 feedback=[]
 for k in kinds:
  found=[(s,x) for s,x in allrows if x.get('error_category')==k]
  feedback.append([k,len(found),'; '.join(f"{s:03d}:{x['id']}" for s,x in found)])
 (BASE/f'{PREFIX}_sheet_feedback.md').write_text('# Feedback on the recurring-error sheet\n\nCounts are consolidated material decision places assigned one primary category; they are not estimates of the frequency of errors in all handwriting. A place may affect either or both witnesses.\n\n'+table(['Error-sheet category','Places','References'],feedback)+'\n## Recurring observations\n\n'+editorial.get('sheet_feedback','See the hand log for each locally established habit and its exact scope. No unsupported cross-cote rule is inferred.\n'))
 combined='\\cotefile{149}\n\n'+'\n\n'.join((BASE/'pages'/f"{r['page']}.tex").read_text().rstrip() for r in reports)+'\n'
 (BASE/f'{PREFIX}_transcription.tex').write_text(combined)
 return {'pages':len(reports),'rows':len(allrows),'C':sum(bool(x.get('against_C')) for s,x in allrows),'H':len(coll),'decisions':len(decs),'doubts':len(doubts)}

if __name__=='__main__': print(json.dumps(build(),ensure_ascii=False))
