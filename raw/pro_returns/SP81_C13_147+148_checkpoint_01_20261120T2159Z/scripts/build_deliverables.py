"""Assemble only root-approved page evidence. No OCR, LaTeX compilation, or source normalization."""
from pathlib import Path
import json,csv,collections,re
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
BASE='SP81_C13_147+148'
SOURCE=ROOT.parent/'source'

def cell(x):
 return str(x).replace('|','\\|').replace('\n','<br>')
def table(headers, rows):
 return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(cell(v) for v in row)+' |' for row in rows])+'\n'
def write_tsv(name,fields,rows,delimiter='\t'):
 with (ROOT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore');w.writeheader();w.writerows(rows)
def main():
 manifest=json.loads((ROOT/'work/manifest.json').read_text())
 reports=[]
 for m in manifest:
  p=ROOT/'work'/f"{m['page']}_final.json"
  if p.exists():
   r=json.loads(p.read_text());assert r.get('root_approved'),m['page'];reports.append(r)
 changes=[(r,c) for r in reports for c in r['changes']]
 cnt=lambda r,k:sum(bool(c.get(k)) for c in r['changes'])
 total_c=sum(cnt(r,'differs_C') for r in reports);total_h=sum(cnt(r,'differs_H') for r in reports)
 lines=[f'# {BASE}: changes against the two draft witnesses','',f'Root-adjudicated pages: {len(reports)}/24. Rows identify physical reading loci; one locus can differ from both witnesses. Macro syntax alone and editorial witness page markers are excluded. Confidence counts count rows once.','',table(['Page','Against C','Against H','High','Medium','Low'],[[r['page'],cnt(r,'differs_C'),cnt(r,'differs_H')]+[sum(c['confidence']==conf for c in r['changes']) for conf in ['high','medium','low']] for r in reports]+[['TOTAL',total_c,total_h]+[sum(c['confidence']==conf for _,c in changes) for conf in ['high','medium','low']]]),'## Consequential corrections','']
 cons=[f"- **{r['page']} · {c['place']}** ({c['id']}): `{c['final']}`. {c.get('consequence',c['evidence'])}" for r,c in changes if c.get('consequential')]
 lines+=cons or ['No consequential correction recorded in the approved pages so far.']
 for r in reports:
  lines += ['',f"## {r['page']}",'',table(['ID / place','Witness C','Witness H','Final reading','What the scan shows / evidence','Confidence'],[[c['id']+' / '+c['place'],c['C'],c.get('H','[no witness H]'),c['final'],c['evidence']+(f" Crop: `crops/{c['crop']}`; original box {c.get('box')}." if c.get('crop') else ''),c['confidence']] for c in r['changes']]),'### Remaining doubts','']
  lines += [table(['Place','Reading','Alternatives','Confidence','Reason'],[[d.get('place',''),d.get('reading',''),d.get('alternatives',''),d.get('confidence',''),d.get('reason','')] for d in r.get('doubts',[])])] if r.get('doubts') else ['No unresolved reading recorded on this page.']
  if r.get('audit_changes'):
   audit_boxes={b['box']:[b[k] for k in ['x0','y0','x1','y1']] for b in r['second_boxes']}
   lines+=['','### Blind second-reading adjudications','',table(['Box / place','First reading','Blind reading','Final reading','Crop and visible evidence','Confidence'],[[x.get('box',''),x.get('first',''),x.get('second',''),x.get('final',''),x.get('evidence','')+f" Crop: `crops/{x.get('crop','')}`; original box {audit_boxes.get(x.get('box',''))}.",x.get('confidence','')] for x in r['audit_changes']])]
 (ROOT/f'{BASE}_changes.md').write_text('\n'.join(lines)+'\n')
 col=[]
 for r,c in changes:
  if c.get('differs_H'):
   cote,scan=r['page'].split('_scan')
   # The supplied prompt explicitly maps H page n to our scan n + 1.
   col.append(dict(folder=cote,their_page=int(scan)-1,our_scan=int(scan),line=c['place'],their_reading=c.get('H',''),codex_reading=c['C'],final_reading=c['final'],scan_shows=c['evidence']+(f"; crops/{c['crop']} {c.get('box')}" if c.get('crop') else ''),kind=c['kind'],marked_in_H='yes' if c.get('marked_in_H') else 'no',confidence=c['confidence']))
 write_tsv(f'{BASE}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],col)
 all_marks=list(csv.DictReader((SOURCE/'SP81_C13_147+148_texts/MARKS.tsv').open(),delimiter='\t',quoting=csv.QUOTE_NONE))
 dec={d['id']:(r,d) for r in reports for d in r['decisions']}
 dr=[]
 for m in all_marks:
  if m['id'] in dec:
   r,d=dec[m['id']]
   dr.append({'id':m['id'],'cote':m['cote'],'scan':m['scan'],'decision':d['decision'],'reading':d['reading'],'what the ink shows':d['evidence'],'crop':d['crop'],'confidence':d['confidence']})
 write_tsv('decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],dr)
 inv=[]
 for r in reports:
  for x in r['inventory']:inv.append({'scan':r['page'],**x})
 write_tsv(f'{BASE}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,',')
 notes=['# Notes while reading','', 'These notes report the manuscript and the actual checks recorded below. A transcription or report of a mathematical claim does not certify that claim. References identify the supplied scan and source locus. No material outside these pages was researched.','']
 for r in reports:notes += [f"## {r['page']}",'',r['notes'],'']
 (ROOT/f'{BASE}_notes.md').write_text('\n'.join(notes))
 events=[]
 for r in reports:
  for e in r.get('check_events',[]):
   events.append({'statement_id':e['statement_id'],'date':e.get('date',r.get('approved_at','')),'who':e.get('who',r.get('reader','')+'; inherited ChatGPT model; effort not exposed; SP81_C13_147+148 run'),'type':e['type'],'outcome':e['outcome']})
 write_tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
 notations=[[n.get('form',''),n.get('meaning',''),r['page']+'; '+n.get('evidence',''),n.get('scope','')] for r in reports for n in r.get('notation',[])]
 ntext=table(['Written form','Meaning / use on these pages','Evidence','Scope checked'],notations)
 (ROOT/'notation.md').write_text('# Working notation table\n\n'+ntext)
 doubts=['# Notation and remaining doubts','', '## Notation table','', ntext,'## Remaining doubts','',table(['Page','Place','Reading','Alternatives','Confidence','Reason'],[[r['page'],d.get('place',''),d.get('reading',''),d.get('alternatives',''),d.get('confidence',''),d.get('reason','')] for r in reports for d in r.get('doubts',[])]),'## Abbreviations','', 'Expansions below are editorial reading aids only. The transcription preserves the written abbreviated forms.','',table(['Form','Suggested expansion','Pages'],[[a.get('form',''),a.get('expansion',''),r['page']] for r in reports for a in r.get('abbreviations',[])]),'## Legibility and witness comparison','']
 for r in reports:
  if r.get('legibility'):doubts += [f"- **{r['page']}:** {r['legibility']}"]
 if not any(r.get('legibility') for r in reports):doubts += ['The retained doubts identify the passages whose strokes do not support a unique reading. The page-specific evidence records where either draft was retained or changed.']
 (ROOT/f'{BASE}_doubts.md').write_text('\n'.join(doubts)+'\n')
 hand=['# Hand log','', 'Each entry is limited to the occurrences actually inspected; repeated notation is checked on the ink, not propagated mechanically.','',table(['Habit / form','Pages and places','Scope of observation','Witness misreadings'],[[h.get('habit',''),r['page']+'; '+h.get('places',''),h.get('scope',''),h.get('witness_errors','')] for r in reports for h in r.get('hand',[])])]
 (ROOT/f'{BASE}_hand_log.md').write_text('\n'.join(hand)+'\n')
 kinds=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertions put in the wrong place','Struck text','Abbreviations expanded, spelling modernised','Text that is not on the page','Other']
 feedback=['# Error-sheet feedback','', 'Counts below are recorded changed loci, classified once by their primary error-sheet kind. They count differences against either draft, including preserved source features that one draft omitted; they are not a statistical estimate of every token on these pages. Confidence-only additions are recorded in the doubts table.','',table(['Error-sheet kind','Recorded loci','Places'],[[kind,sum(c.get('error_sheet_kind','Other')==kind for _,c in changes),'; '.join(c['id'] for _,c in changes if c.get('error_sheet_kind','Other')==kind)] for kind in kinds]),'## Further recurring observations','']
 for r in reports:
  for h in r.get('hand',[]):feedback += [f"- {r['page']}, {h.get('places','')}: {h.get('habit','')} ({h.get('scope','')})."]
 (ROOT/f'{BASE}_sheet_feedback.md').write_text('\n'.join(feedback)+'\n')
 trans=[]
 for r in reports:
  trans.append((ROOT/'pages'/f"{r['page']}.tex").read_text().rstrip()+'\n')
 (ROOT/f'{BASE}_transcription.tex').write_text('\n'.join(trans))
 print(json.dumps({'approved_pages':len(reports),'changes_C':total_c,'changes_H':total_h,'change_loci':len(changes),'mark_decisions':len(dr),'inventory_elements':len(inv),'check_events':len(events)}))
if __name__=='__main__':main()
