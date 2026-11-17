#!/usr/bin/env python3
"""Select and render the ninth-hour proof pages; inspection remains separate."""
from pathlib import Path
import hashlib,json,re,subprocess
import fitz

ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'GT_TOWER_CHECK_paper.pdf'
OUT=ROOT/'notes/pdf_qa'
OUT.mkdir(exist_ok=True)
doc=fitz.open(PDF)
reasons={}
def take(page,reason):
    if 1<=page<=len(doc):reasons.setdefault(page,[]).append(reason)
for index,page in enumerate(doc,1):
    value=' '.join(page.get_text().split())
    for marker in ['A.L6','A.C11','A.J2','B5.5','B.M','B.N','MC.','FCE.','FCM.']:
        if marker in value:take(index,'Earlier repaired display: '+marker)
    for marker in ['NCF.','ECR.','SVM.','HTS.','CFF.','HOR.','MIF.','CFK.','ICR.']:
        if marker in value:
            take(index,'Ninth-hour proof and display: '+marker)
            take(index+1,'Continuation of ninth-hour proof: '+marker)
    for number in list(range(46,53))+[54]:
        if f'A.4.{number} (Proved)' in value:
            take(index,'Ninth-hour statement A.4.'+str(number))
    for marker in ['B.5 (Proved)','C.2.2 (Proved)','C.1.13 (Proved)','C.1.15 (Proved)']:
        if marker in value:
            take(index,'Earlier repaired source region: '+marker)
            take(index+1,'Continuation of earlier repair: '+marker)
    if 'with exactly the eight roots' in value:take(index,'Earlier repaired root list')
for k in range(13):take(1+round(k*(len(doc)-1)/12),'Spread sample')
for page in range(max(1,len(doc)-3),len(doc)+1):take(page,'Bibliography spacing repair')
for page in sorted(reasons):
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile',
                    '-r','105','-png',str(PDF),str(OUT/f'page_{page:03d}')],
                   check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    print(page,', '.join(reasons[page]),flush=True)
record={'pdf_sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),
        'pdf_pages':len(doc),'render_dpi':105,
        'pages':[{'page':p,'reasons':reasons[p],'file':f'page_{p:03d}.png'} for p in sorted(reasons)],
        'visual_inspection':'Pending; rendering alone is not a visual check.'}
(OUT/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
people=('root','tower','centralizer','ghost')
assignments={who:[] for who in people}
for i,row in enumerate(record['pages']):assignments[people[i%4]].append(row['page'])
(OUT/'checkpoint09_assignments.json').write_text(json.dumps({
    'pdf_sha256':record['pdf_sha256'],'assignments':assignments,
    'instructions':'Open every listed full-page PNG and inspect it visually. Record actual observations and each PNG SHA256. Rendering alone is not inspection.'},indent=2)+'\n')
print('Rendered',len(reasons),'pages. Actual visual inspection remains required.')
print(json.dumps(assignments,indent=2))
