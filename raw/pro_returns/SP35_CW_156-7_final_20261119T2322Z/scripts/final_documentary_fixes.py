"""Final source-only and documentary corrections from independent audits."""
from pathlib import Path
from datetime import datetime,timezone
import json,re,hashlib
root=Path(__file__).resolve().parents[1]
changes=[]
for n in range(2,10):
 p=root/'records'/f'scan{n:03d}.json'
 r=json.loads(p.read_text())
 if n==4:
  for a in r['abbreviations']:
   if a['form']=='def':
    a.update(form='déf / def',meaning='définition',location='004, first equivalence label retains the accent doubt déf|def; second label is unaccented def')
  for a in [dict(form='NB / NB.',meaning='nota bene',location='004 margins; 008–009 NB paragraphs'),dict(form='Sup / sup',meaning='supremum',location='004 supremum margin; 005 At1/At2; 008–009 intersection formulas'),dict(form='Cor / Cor.',meaning='corollaire',location='008–009 corollary headings and references')]:
   if not any(x['form']==a['form'] for x in r['abbreviations']):r['abbreviations'].append(a)
  changes.append('004 abbreviation wording distinguishes the first accent doubt from the resolved second label; NB, Sup/sup and Cor added.')
 if n==5:
  d=next(d for d in r['decisions'] if d['id']=='005-22')
  d['math_consequence']='The initial pair retains C|G, with C preferred; if C is the written letter, it differs from G in the following equivalence. The ink uncertainty is preserved.'
  changes.append('005-22 consequential summary no longer asserts C or a definite mismatch beyond the retained doubt.')
 # The audit is authoritative. Avoid carrying an earlier reader's resolved/
 # retained flag after main adjudication changed that decision.
 for d in r['decisions']:
  if 'C_doubt_status' in d:
   matching=[a for a in r['C_doubt_audit'] if d['id'] in a.get('evidence','') or a.get('decision_id')==d['id']]
   if matching:
    d['C_doubt_status']='; '.join(dict.fromkeys(a['status'] for a in matching))
  # Crop coordinates are retained in each actual crop manifest. Copied reader
  # coordinates may refer to a different crop selected by the main reader.
  for key in ['crop_coordinates','crop_rotation_degrees']:d.pop(key,None)
 p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
changes.append('Decision-level doubt flags synchronized to main C-doubt audits; crop coordinates remain in original crop manifests rather than copied main rows.')

p=root/'pages/H156-01_156-7_scan008.tex';s=p.read_text();before=hashlib.sha256(s.encode()).hexdigest()
old=r'\tikz[baseline=(b.base),every node/.style={inner sep=0pt}]'
if old in s and r'\mbox{'+old not in s:
 start=s.index(old);bs=s.index('{',start+len(old));depth=0;end=None
 for i in range(bs,len(s)):
  if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
  elif s[i]=='}' and (i==0 or s[i-1]!='\\'):
   depth-=1
   if depth==0:end=i+1;break
 assert end
 s=s[:start]+r'\mbox{'+s[start:end]+'}'+s[end:]
 p.write_text(s)
changes.append('008 cf Cor inline TikZ boxed with standard mbox to protect its spaced options from ulem word scanning; no ink reading changed.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report=dict(date=now,changes=changes,source_protection=dict(file=str(p.relative_to(root)),before_sha256=before,after_sha256=hashlib.sha256(s.encode()).hexdigest()),scope='Source inspection and documentary consistency only; no compilation, rendering, OCR or new manuscript reading.')
(root/'records/final_documentary_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with (root/'progress.log').open('a') as f:f.write('final documentary/source corrections '+now+'; see records/final_documentary_audit.json; no manuscript readings altered on002–008\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
