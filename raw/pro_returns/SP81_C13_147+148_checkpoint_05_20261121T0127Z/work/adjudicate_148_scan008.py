from pathlib import Path
import csv,json
r=Path('edition');page='148_scan008'
comp=json.loads((r/'second'/f'{page}_comparison.json').read_text())
d={x['box']:x for x in comp['differences']}
p=r/'work'/f'{page}_final.json';report=json.loads(p.read_text());assert not report.get('audit')
f=d['B11']['second'].replace('x=0.0024cm,y=-0.0024cm','x=0.0011cm,y=-0.0011cm').replace('\\end{tikzpicture}',r'\node[anchor=west] at (2420,900) {\unsure{}};'+'\n'+r'\end{tikzpicture}')
pt=r/'pages'/f'{page}.tex';t=pt.read_text();assert d['B11']['first'] in t;t=t.replace(d['B11']['first'],f);pt.write_text(t)
evidence='The crop exposes a narrow upper-left loop, long vertical, large open left loop, two separated middle curves, a low sweep broken before its rising right end, the small detached upper-right stroke, one detached short dark left stroke, and the separate dotted lower flourish with a further gap near the right end. The second drawing preserves these gaps. The two paler spots near the left mark and below the inner oval remain unassigned. The complete letter sequence remains unresolved; the in-place doubt is retained. Coordinate scale is editorial.'
for x in report['changes']:
 if x['id']==page+'-04':x.update(final=f,evidence=evidence,crop=page+'_second_B11.png',box=[910,1940,1110,2056])
report['notes']+=' Blind audit: the three decorative rows retain their independently counted 12, 52 and 11 dashes. The signature drawing now preserves the small gaps in the low sweep and lower flourish; uncertain pale traces are unassigned and M0088 remains undecided.'
p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
choices=[]
for box in d:
 choices.append(dict(box=box,choice='literal' if box=='B11' else 'first',**({'final':f} if box=='B11' else {}),changed=box=='B11',confidence='medium' if box=='B11' else 'high',evidence=evidence if box=='B11' else {'B01':'The enlarged crop has DU LANGUEDOC and twelve distinct keyed dashes. Both readings record these same characters; the first two-baseline layout is retained.','B04':'The full capitals are unchanged and fifty-two separate keyed dashes occupy the following baseline. Both readings give the same count; first layout retained.','B05':'The crop has AUTOMATIQUE and eleven separate keyed dashes. Both readings record the same characters and gaps; first layout retained.'}[box]))
(r/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_c',choices=choices),ensure_ascii=False,indent=2)+'\n')
