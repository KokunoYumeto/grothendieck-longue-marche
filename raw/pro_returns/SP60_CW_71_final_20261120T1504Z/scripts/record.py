"""Bookkeeping for the single-reader SP60_CW_71 collation. No OCR or TeX compilation."""
from pathlib import Path
import csv
from datetime import datetime, timezone
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
PREFIX='SP60_CW_71'
HEADERS={
 'decisions.tsv':['scan','id','place','C','H','final','scan_shows','confidence','against_C','against_H','kind','marked_in_H','record_type','consequential'],
 'doubt_records.tsv':['scan','place','reading','alternatives','confidence','status','reason'],
 'notation.tsv':['notation','form_and_use','places','ambiguity_consistency'],
 'hand.tsv':['habit','places','scope','witness_errors'],
 PREFIX+'_inventory.csv':['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],
 'CHECK_EVENTS.tsv':['statement_id','date','who','type','outcome'],
 PREFIX+'_collation.tsv':['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']}

def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def append(name,vals):
 p=ROOT/name; exists=p.exists() and p.stat().st_size
 with p.open('a',encoding='utf-8',newline='') as f:
  w=csv.writer(f,delimiter=',' if name.endswith('.csv') else '\t')
  if not exists:w.writerow(HEADERS[name])
  w.writerow(vals)
def rows(name):
 p=ROOT/name
 if not p.exists():return []
 with p.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter=',' if name.endswith('.csv') else '\t'))
def md(s):return str(s).replace('|','&#124;').replace('\n','<br>')
def table(headers,data):
 return '| '+' | '.join(headers)+' |\n|'+'|'.join(['---']*len(headers))+'|\n'+''.join('| '+' | '.join(md(x) for x in row)+' |\n' for row in data)
def change(scan,id,place,C,H,final,shows,confidence='high',c=False,h=False,kind='other',marked='no',record_type='change',consequential=''):
 append('decisions.tsv',[scan,id,place,C,H,final,shows,confidence,'yes' if c else 'no','yes' if h else 'no',kind,marked,record_type,consequential])
 if h:
  if scan not in (38,47,48):raise ValueError('H has no source text on this page')
  append(PREFIX+'_collation.tsv',['J71-05' if scan<=42 else 'J71-06',scan-1,scan,place,H,C,final,shows,kind,marked,confidence])
def doubt(scan,place,reading,alts='',confidence='medium',status='remaining',reason=''):
 append('doubt_records.tsv',[scan,place,reading,alts,confidence,status,reason])
def notation(n,f,p,a=''):append('notation.tsv',[n,f,p,a])
def hand(h,p,s,e):append('hand.tsv',[h,p,s,e])
def inv(scan,els,sheet='text'):
 for i,(kind,pos,words) in enumerate(els,1):append(PREFIX+'_inventory.csv',[scan,sheet,'another unnamed hand (main memoir; identity unverified)',f'{scan:03}-{i:02}',kind,pos,words,'yes'])
def note(scan,text):
 p=ROOT/(PREFIX+'_notes.md')
 if not p.exists():p.write_text('# SP60_CW_71 — Notes while reading\n\nOnly the supplied pages are used. Descriptions of claims are not proof certifications. Check events below distinguish the work actually performed.\n',encoding='utf-8')
 with p.open('a',encoding='utf-8') as f:f.write(f'\n## Scan {scan}\n\n{text}\n')
def event(id,typ,outcome):append('CHECK_EVENTS.tsv',[id,utc(),'ChatGPT GPT-6 Astra Pro; effort not exposed; SP60_CW_71 second pass',typ,outcome])
def done(scan):
 with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write(f'scan {scan:03} done {utc()}\n')
 render()
def assemble():
 ps=sorted((ROOT/'pages').glob('*.tex'))
 (ROOT/(PREFIX+'_transcription.tex')).write_text('\\cotefile{71}\n'+''.join(p.read_text(encoding='utf-8').rstrip()+'\n\n' for p in ps),encoding='utf-8')
def render():
 ds=rows('decisions.tsv'); change_rows=[r for r in ds if r['against_C']=='yes' or r['against_H']=='yes']
 scans=sorted(set(int(r['scan']) for r in rows(PREFIX+'_inventory.csv')))
 lines=['# SP60_CW_71 — Changes and crop decisions\n\nCounts are distinct recorded places, not changed characters. A place differing from both witnesses counts once in the confidence columns and once against each witness. Changes of certainty alone are listed in the doubts file and excluded from these counts. Macro-only changes are excluded. **H has source text on scans 38, 47 and 48, principally marginal annotations and short source locators. Its editorial `\\note` synopses are not source text. Untranscribed body blocks on those three pages are recorded as coverage omissions, not as attempted readings that H got wrong.** H has no source-text collation rows for scans 39–46. See the sheet-feedback file for the separate coverage and recovery counts. The `kind` field is a primary classification of a place; C and H can differ for different reasons at that same place. Pixel boxes refer to the supplied whole-page JPG; decisions settled by the supplied halves or second-reading whole image needed no crop.\n\n## Counts\n\n']
 counts=[]
 for s in scans:
  rs=[r for r in change_rows if int(r['scan'])==s];co=Counter(r['confidence'] for r in rs)
  counts.append([s,sum(r['against_C']=='yes' for r in rs),sum(r['against_H']=='yes' for r in rs),len(rs),co['high'],co['medium'],co['low']])
 if counts:counts.append(['Total']+[sum(r[i] for r in counts) for i in range(1,7)])
 lines.append(table(['Scan','Against C','Against H','Distinct places','High','Medium','Low'],counts))
 lines.append('\n### Confidence by witness\n\n')
 wc=[]
 for s in scans:
  rs=[r for r in change_rows if int(r['scan'])==s]
  cc=Counter(r['confidence'] for r in rs if r['against_C']=='yes')
  hc=Counter(r['confidence'] for r in rs if r['against_H']=='yes')
  wc.append([s,cc['high'],cc['medium'],cc['low'],hc['high'],hc['medium'],hc['low']])
 if wc:wc.append(['Total']+[sum(r[i] for r in wc) for i in range(1,7)])
 lines.append(table(['Scan','C high','C medium','C low','H high','H medium','H low'],wc))
 lines.append('\n## Consequential corrections\n\n')
 cs=[r for r in change_rows if r['consequential']]
 lines.extend(f"- Scan {r['scan']}, {r['id']}: {r['consequential']}\n" for r in cs)
 if not cs:lines.append('No mathematical reading correction recorded so far. Authorial slips retained are discussed in the notes.\n')
 for s in scans:
  lines.append(f'\n## Scan {s}\n\n')
  rs=[r for r in change_rows if int(r['scan'])==s]
  if rs:lines.append(table(['ID / place','Witness C','Witness H','Final reading','What the scan shows','Confidence'],[[r['id']+' — '+r['place'],r['C'],r['H'],r['final'],r['scan_shows'],r['confidence']] for r in rs]))
  else:lines.append('No substantive difference from the applicable witness text.\n')
  extra=[r for r in ds if int(r['scan'])==s and r not in change_rows]
  if extra:
   lines.append('\n### Crop decisions retaining a reading\n\n')
   lines.append(table(['ID / place','C / H','Decision','Ink and crop','Confidence'],[[r['id']+' — '+r['place'],r['C']+' / '+r['H'],r['final'],r['scan_shows'],r['confidence']] for r in extra]))
  dr=[r for r in rows('doubt_records.tsv') if int(r['scan'])==s and r['status']=='remaining']
  lines.append('\n### Remaining doubts\n\n')
  lines.append('; '.join(r['place']+': '+r['reading']+(' / '+r['alternatives'] if r['alternatives'] else '') for r in dr)+'.\n' if dr else 'None recorded.\n')
 (ROOT/(PREFIX+'_changes.md')).write_text(''.join(lines),encoding='utf-8')
 ns=rows('notation.tsv');dr=rows('doubt_records.tsv')
 st='# SP60_CW_71 — Doubts and notation\n\n## Notation table\n\n'+table(['Notation','Form and use','Scans / places','Ambiguity / consistency'],[[r[x] for x in HEADERS['notation.tsv']] for r in ns])
 for status,title in [('remaining','Remaining doubts'),('resolved','Certainty decisions'),('retained','Doubts retained after checking')]:
  st+='\n## '+title+'\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],[[r[x] for x in ['scan','place','reading','alternatives','confidence','reason']] for r in dr if r['status']==status])
 for fn in ['abbreviations.md','legibility.md']:
  p=ROOT/fn
  if p.exists():st+='\n'+p.read_text(encoding='utf-8')
 (ROOT/(PREFIX+'_doubts.md')).write_text(st,encoding='utf-8')
 hs=rows('hand.tsv')
 (ROOT/(PREFIX+'_hand_log.md')).write_text('# SP60_CW_71 — Hand log\n\nHabits observed in the supplied scans; scope is explicit and no claim is made about other manuscripts. The main memoir and marginal annotation layers are distinguished by observed appearance, without identifying either writer. H describes the memoir as another hand; that editorial attribution is not an independently established identity. The doubtful signature on scan 48 does not settle it. Inventory hand descriptions therefore use unnamed hands and specify the layer; they do not assert that every intervention belongs to a separate person. Pencil sketches on scan 46 remain unattributed.\n\n'+table(['Habit','Places','Does it hold throughout?','Witness readings affected'],[[r[x] for x in HEADERS['hand.tsv']] for r in hs]),encoding='utf-8')
 if not (ROOT/(PREFIX+'_collation.tsv')).exists():
  with (ROOT/(PREFIX+'_collation.tsv')).open('w',encoding='utf-8',newline='') as f:csv.writer(f,delimiter='\t').writerow(HEADERS[PREFIX+'_collation.tsv'])
 assemble()

if __name__=='__main__':render()
