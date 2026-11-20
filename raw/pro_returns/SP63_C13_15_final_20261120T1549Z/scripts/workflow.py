"""Mechanical record assembly only; all readings and evidence are supplied by the reader."""
from pathlib import Path
import csv, json, re
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT.parent/'source'/'SP63_C13_15_texts'
PREFIX='SP63_C13_15'
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def write_table(path,fields,rows,delimiter='\t'):
 with path.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter);w.writeheader();w.writerows(rows)
def esc(x): return str(x).replace('|','&#124;').replace('\n',' ')
def mdtable(fields,rows):
 return '| '+' | '.join(fields)+' |\n|'+ '|'.join(['---']*len(fields))+'|\n'+''.join('| '+' | '.join(esc(x) for x in r)+' |\n' for r in rows)
def row(place,c,h,final,ink,kind='other',confidence='high',C=False,H=False,marked='no',consequential=False):
 return dict(place=place,c=c,h=h,final=final,ink=ink,kind=kind,confidence=confidence,C=C,H=H,marked=marked,consequential=consequential)
def decision(id,decision,reading,ink,crop='page',confidence='high'):
 return dict(id=id,decision=decision,reading=reading,**{'what the ink shows':ink},crop=crop,confidence=confidence)
def record(scan,text,rows,decisions,inventory,notes,doubts=(),notation=(),hand=(),abbreviations=(),events=(),sheet='text',extra=''):
 data=dict(scan=scan,rows=rows,decisions=decisions,inventory=inventory,notes=notes,doubts=doubts,notation=notation,hand=hand,abbreviations=abbreviations,events=events,sheet=sheet,extra=extra)
 (ROOT/'pages'/f'15_scan{scan}.tex').write_text(text.rstrip()+'\n',encoding='utf-8')
 (ROOT/'records'/f'{scan}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 assemble()
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03d} done {utc()} cote 15\n')
def assemble():
 data=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('*.json'))]
 totals={k:0 for k in ['C','H','high','medium','low']};counts=[];cons=[];body=[];coll=[];decs=[];inv=[];notes=[];doubts=[];notation=[];hands=[];abbr=[];events=[]
 for d in data:
  s=d['scan'];rs=d['rows'];count={k:sum(bool(r[k]) for r in rs) for k in ['C','H']}
  count.update({k:sum(r['confidence']==k for r in rs) for k in ['high','medium','low']})
  for k in totals:totals[k]+=count[k]
  counts.append([s]+list(count.values()))
  body.append(f'## Scan {s} (H page {s-1})\n\n'+mdtable(['Place','C','H','Final','Scan evidence / crop','Confidence'],[[r[k] for k in ['place','c','h','final','ink','confidence']] for r in rs]))
  body.append('\nRemaining uncertainties: '+('; '.join(x[1]+': '+x[2] for x in d['doubts']) or 'None.')+'\n\n'+d.get('extra','')+'\n')
  for r in rs:
   if r['consequential']:cons.append(f'- Scan {s}, {r["place"]}: {r["final"]}. {r["ink"]}')
   if r['H']:coll.append(dict(folder='15',their_page=str(s-1),our_scan=str(s),line=r['place'],their_reading=r['h'],codex_reading=r['c'],final_reading=r['final'],scan_shows=r['ink'],kind=r['kind'],marked_in_H=r['marked'],confidence=r['confidence']))
  for x in d['decisions']:decs.append(dict(id=x['id'],cote='15',scan=str(s),**{k:v for k,v in x.items() if k!='id'}))
  for n,x in enumerate(d['inventory'],1):
   kind,position,words,*hand=x
   inv.append(dict(scan=s,sheet_kind=d['sheet'],hand=hand[0] if hand else 'his hand',element=f'{s}.{n:02}',kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))
  notes.append(f'## Scan {s}\n\n'+d['notes']+'\n')
  doubts.extend(d['doubts']);notation.extend(d['notation']);hands.extend([f'- Scan {s}: {x}' for x in d['hand']]);abbr.extend(d['abbreviations'])
  for x in d['events']:events.append(dict(statement_id=x[0],date=utc().split()[0],who='GPT-6 Astra Pro; effort not exposed; SP63_C13_15 second pass, run 1',type=x[1],outcome=x[2]))
 (ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join((ROOT/'pages'/f'15_scan{d["scan"]}.tex').read_text() for d in data),encoding='utf-8')
 counts.append(['TOTAL']+list(totals.values()))
 intro='# Changes and collation\n\nCounts are places, not changed characters. A place can differ from both witnesses. Confidence counts cover unique substantive rows. Certainty-only resolutions appear in decisions.tsv and the doubts file. Macro-only differences and H editorial notes are excluded. H is absent on scans 157, 160, 162, 164 and 172.\n\n'+mdtable(['Scan','Against C','Against H','High','Medium','Low'],counts)+'\n## Consequential corrections\n\n'+('\n'.join(cons) or 'None recorded yet.')+'\n\n'
 witness_confidence=[]
 for d in data:
  witness_confidence.append([d['scan']]+[sum(r[w] and r['confidence']==level for r in d['rows']) for w in ['C','H'] for level in ['high','medium','low']])
 witness_confidence.append(['TOTAL']+[sum(row[i] for row in witness_confidence) for i in range(1,7)])
 intro=intro.replace('\n## Consequential corrections\n', '\n### Confidence by witness\n\n'+mdtable(['Scan','C high','C medium','C low','H high','H medium','H low'],witness_confidence)+'\n## Consequential corrections\n')
 (ROOT/f'{PREFIX}_changes.md').write_text(intro+'\n'.join(body),encoding='utf-8')
 write_table(ROOT/f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
 write_table(ROOT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decs)
 write_table(ROOT/f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,',')
 (ROOT/f'{PREFIX}_notes.md').write_text('# Reading notes\n\nStatements below are reports of what each sheet says. Transcription and comparison alone are not proof checks. Only actual mathematical checks or background uses are entered in CHECK_EVENTS.tsv. No external text was consulted.\n\n'+'\n'.join(notes),encoding='utf-8')
 write_table(ROOT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
 certainty='\n'.join(f'- {x["id"]} (scan {x["scan"]}): {x["decision"]}; `{x["reading"]}`. {x["what the ink shows"]}' for x in decs)
 (ROOT/f'{PREFIX}_doubts.md').write_text('# Notation and doubts\n\n## Notation table\n\n'+mdtable(['Usage','Written form / transcription','Pages','Evidence'],notation)+'\n## Remaining doubts\n\n'+mdtable(['Scan','Place','Reading','Alternatives / limitation','Confidence'],doubts)+'\n## Mark decisions, including certainty-only resolutions\n\n'+certainty+'\n\n## Abbreviations (expansions only here)\n\n'+mdtable(['Written abbreviation','Suggested expansion'],sorted(set(tuple(x) for x in abbr)))+'\n\n## Legibility and witness comparison\n\n'+((ROOT/'assessment.txt').read_text() if (ROOT/'assessment.txt').exists() else 'Assessment in progress; see the per-page evidence.')+'\n',encoding='utf-8')
 hand_review=(ROOT/'hand_review.txt').read_text() if (ROOT/'hand_review.txt').exists() else ''
 (ROOT/f'{PREFIX}_hand_log.md').write_text('# Hand log\n\nAll observations are limited to the occurrences cited; page-specific exceptions are retained. For a local observation, application to every other occurrence is not established. The final review table gives the explicitly checked extent of recurring habits.\n\n'+'\n'.join(hands)+'\n\n'+hand_review,encoding='utf-8')
 kinds={}
 for d in data:
  for r in d['rows']:kinds[r['kind']]=kinds.get(r['kind'],0)+1
 feedback=(ROOT/'feedback_final.txt').read_text() if (ROOT/'feedback_final.txt').exists() else '# Error-sheet feedback\n\nSubstantive differing places by collation kind; certainty-only decisions are tabulated separately in decisions.tsv.\n\n'+mdtable(['Kind','Places'],sorted(kinds.items()))+'\nThe evidence for each place is in the changes log. Final synthesis follows completion of the second reading.\n'
 (ROOT/f'{PREFIX}_sheet_feedback.md').write_text(feedback,encoding='utf-8')
if __name__=='__main__':assemble()
