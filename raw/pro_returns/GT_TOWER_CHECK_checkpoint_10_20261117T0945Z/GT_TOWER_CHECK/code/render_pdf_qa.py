#!/usr/bin/env python3
"""Render the repaired display pages and a spread sample using Poppler."""
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
    text=' '.join(page.get_text().split())
    for marker in ['A.L6','A.C11','A.J2','B5.5','B.M','B.N','MC.','FCE.','FCM.']:
        if marker in text:take(index,'Repaired display or its immediate proof: '+marker)
    for marker in ['B.5 (Proved)','C.2.2 (Proved)','C.1.13 (Proved)','C.1.15 (Proved)']:
        if marker in text:
            take(index,'Repaired source region: '+marker)
            take(index+1,'Continuation of repaired source region: '+marker)
    if 'with exactly the eight roots' in text:
        take(index,'Repaired long root list')
    if 'C.1.19 (Proved)' in text:
        take(index,'New exact 24-element section fibre')
    for ident in ([f'A.4.{i}' for i in range(38,46)] + ['B.2.31']):
        marker=ident+' (Proved)'
        if marker in text:
            for offset in range(4):
                take(index+offset,'Eighth-hour new proof region: '+ident)
    for marker in ['OCM.','FEC.','FGA.','OGS.','FCD.','CDF.','RPO.','COB.','MFP.','TMR.',
                   'B.AD','A.T9']:
        if marker in text:
            take(index,'Eighth-hour display verification: '+marker)
            if marker!='A.T9':
                take(index+1,'Continuation of eighth-hour display proof: '+marker)
for k in range(11):take(1+round(k*(len(doc)-1)/10),'Spread sample')
for page in sorted(reasons):
    target=OUT/f'page_{page:03d}'
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile',
                    '-r','105','-png',str(PDF),str(target)],check=True,
                   stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    print(page,', '.join(reasons[page]),flush=True)
record={'pdf_sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),
        'pdf_pages':len(doc),'render_dpi':105,
        'pages':[{'page':p,'reasons':reasons[p],
                  'file':f'page_{p:03d}.png'} for p in sorted(reasons)],
        'visual_inspection':'Pending; rendering alone is not a visual check.'}
(OUT/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print('Rendered',len(reasons),'pages. Visual inspection remains explicit.')
