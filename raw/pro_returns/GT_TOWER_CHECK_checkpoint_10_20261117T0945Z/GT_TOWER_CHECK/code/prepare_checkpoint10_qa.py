#!/usr/bin/env python3
"""Render tenth-hour proof pages and assign actual full-page visual inspection."""
from pathlib import Path
import hashlib,json,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'GT_TOWER_CHECK_paper.pdf';OUT=ROOT/'notes/pdf_qa'
OUT.mkdir(exist_ok=True)
doc=fitz.open(PDF);reasons={}
def take(page,reason):
    if 1<=page<=len(doc):reasons.setdefault(page,[]).append(reason)
new_markers=['IFM.','FBO.','DDP.','CMC.','ICF.','CF4.','QCS.',
             'CONE.','OBT.','BCV.','FCP.','ICS.','BTR.','PPO.']
for number,page in enumerate(doc,1):
    value=' '.join(page.get_text().split())
    for marker in ['A.L6','A.C11','A.J2','B5.5','B.M','B.N','MC.','FCE.','FCM.','SVM.6']:
        if marker in value:take(number,'Earlier repaired display: '+marker)
    for marker in new_markers:
        if marker in value:
            take(number,'Tenth-hour proof and display: '+marker)
            take(number+1,'Continuation of tenth-hour proof: '+marker)
    for result in (53,55,56,57,58,59,60):
        if f'A.4.{result} (Proved)' in value:
            take(number,'Tenth-hour statement A.4.'+str(result))
    for marker in ['B.5 (Proved)','C.2.2 (Proved)','C.1.13 (Proved)','C.1.15 (Proved)']:
        if marker in value:
            take(number,'Earlier repaired source region: '+marker)
            take(number+1,'Continuation of earlier repair: '+marker)
    if 'with exactly the eight roots' in value:take(number,'Earlier repaired root list')
for k in range(17):take(1+round(k*(len(doc)-1)/16),'Spread sample')
for number in range(max(1,len(doc)-3),len(doc)+1):take(number,'Bibliography sample')
for number in sorted(reasons):
    subprocess.run(['pdftoppm','-f',str(number),'-l',str(number),'-singlefile',
      '-r','105','-png',str(PDF),str(OUT/f'page_{number:03d}')],
      check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    print(number,', '.join(reasons[number]),flush=True)
record={'pdf_sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),
 'pdf_pages':len(doc),'render_dpi':105,
 'pages':[{'page':n,'reasons':reasons[n],'file':f'page_{n:03d}.png'} for n in sorted(reasons)],
 'visual_inspection':'Pending; rendering alone is not a visual check.'}
(OUT/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
people=('root','tower','centralizer','ghost');assignments={who:[] for who in people}
for i,row in enumerate(record['pages']):assignments[people[i%4]].append(row['page'])
(OUT/'checkpoint10_assignments.json').write_text(json.dumps({
 'pdf_sha256':record['pdf_sha256'],'assignments':assignments,
 'instructions':'Open every assigned full-page PNG and inspect it visually. Record concrete observations and its SHA256; rendering alone is not inspection.'},indent=2)+'\n')
print('Rendered',len(reasons),'pages; actual full-page inspection remains required.')
print(json.dumps(assignments,indent=2))
