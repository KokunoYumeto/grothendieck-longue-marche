"""Mechanical recording helpers for the primary reader's image-based second audit.
No image recognition or reading decisions are performed by this module.
"""
from record import *

def rewrite_tsv(name, rows, fields=None):
 p=ROOT/name
 if fields is None:
  with p.open(newline='') as f:fields=next(csv.reader(f,delimiter='\t'))
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)

def replace_text(key, pairs):
 p=ROOT/'pages'/(key+'.tex');s=p.read_text()
 for old,new in pairs:
  if old not in s:raise ValueError(('absent audit replacement',key,old))
  s=s.replace(old,new)
 p.write_text(s)

def add_changes(key, rows):
 fs=['page','place','C','H','final','scan_shows','confidence','kind','diff_C','diff_H','marked_H','consequential','crop']
 append('CHANGE_LEDGER.tsv',fs,[dict(zip(fs,[key]+list(x))) for x in rows])

def revise_change(key,place,**updates):
 rows=readtsv('CHANGE_LEDGER.tsv');found=[r for r in rows if r['page']==key and r['place']==place]
 if len(found)!=1:raise ValueError(('change row not unique',key,place,len(found)))
 found[0].update(updates);rewrite_tsv('CHANGE_LEDGER.tsv',rows)

def revise_decision(mid,**updates):
 rows=readtsv('decisions.tsv');found=[r for r in rows if r['id']==mid]
 if len(found)!=1:raise ValueError(('decision not unique',mid))
 found[0].update(updates);rewrite_tsv('decisions.tsv',rows)

def add_certainty(key, rows):
 fs=['page','place','C','final','ink','crop','confidence']
 append('CERTAINTY.tsv',fs,[dict(zip(fs,[key]+list(x))) for x in rows])

def add_doubts(key, rows):
 fs=['page','place','reading','alternatives','confidence']
 append('DOUBTS.tsv',fs,[dict(zip(fs,[key]+list(x))) for x in rows])

def remove_doubt(key,place):
 rows=readtsv('DOUBTS.tsv');keep=[r for r in rows if not (r['page']==key and r['place']==place)]
 if len(keep)==len(rows):raise ValueError(('doubt absent',key,place))
 rewrite_tsv('DOUBTS.tsv',keep)

def add_inventory(key,kind,position,words,after,hand='his hand'):
 p=ROOT/(PREFIX+'_inventory.csv')
 with p.open(newline='') as f:
  reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
 matches=[i for i,r in enumerate(rows) if r['scan']==key and r['element']==after]
 if len(matches)!=1:raise ValueError(('inventory anchor',key,after))
 i=matches[0];r=dict(rows[i]);r.update(kind=kind,position=position,first_words_or_objects=words,hand=hand)
 rows.insert(i+1,r);n=0
 for r in rows:
  if r['scan']==key:n+=1;r['element']=f'E{n:02}'
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def finish(key, note='All lines and page elements reread against the image; no additional textual change.', habits='',notation=(),abbreviations=()):
 cote,scan=key.split('_scan')
 if re.search(rf'^scan {scan} audited .* cote {cote}$',(ROOT/'progress.log').read_text(),re.M):raise RuntimeError('Already audited '+key)
 addtext('AUDIT_LOG.md',key,note)
 if habits:addtext(PREFIX+'_hand_log.md',key+' — second audit',habits)
 append('NOTATION.tsv',['page','sign_or_form','reading_and_manuscript_form'],[{'page':key,'sign_or_form':x[0],'reading_and_manuscript_form':x[1]} for x in notation])
 append('ABBREVIATIONS.tsv',['page','form','expansion'],[{'page':key,'form':x[0],'expansion':x[1]} for x in abbreviations])
 regenerate()
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan} audited {now()} cote {cote}\n')
