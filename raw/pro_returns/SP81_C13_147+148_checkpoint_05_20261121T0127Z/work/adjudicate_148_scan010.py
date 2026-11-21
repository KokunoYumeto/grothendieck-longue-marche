from pathlib import Path
import json
r=Path('edition');page='148_scan010';p=r/'work'/f'{page}_final.json';q=json.loads(p.read_text());assert not q.get('audit');d={x['box']:x for x in json.loads((r/'second'/f'{page}_comparison.json').read_text())['differences']}
a='  .. controls (45.5,109) and (47,121) .. (51,128);'
b='  .. controls (45.5,109) and (46.5,114) .. (46.8,117.7);\n'+r'\draw[line width=0.45pt] (47.7,120) .. controls (48.2,123) and (49.6,126) .. (51,128);'
f=d['B05']['first'].replace(a,b);assert f!=d['B05']['first']
pt=r/'pages'/f'{page}.tex';t=pt.read_text();assert d['B05']['first'] in t;pt.write_text(t.replace(d['B05']['first'],f))
e={
'B01':'Both readings give DU LANGUEDOC and thirteen individual circumflex marks on the following baseline. The crop exposes the same count and keyed shapes; first layout retained.',
'B02':'Both readings give the same quoted capitals, option, and sixty equals signs in the separate row. The enlarged crop shows all characters; spacing commands do not alter the reading.',
'B03':'The r-shaped left stem, shoulder and foot remain visible beside the p; an additional taller oblique/top-serif stroke and separate lower right upright share that cell. The second graphical trace confirms the composite but does not identify its earlier component or typing order. The first readable r and its locally uncertain deleted-unreadable/additional-stroke state are retained, with the separately visible acute over e.',
'B04':'The a-shaped lower loop and right stem remain readable after atl; an additional elevated diagonal/serif shares the cell. Its prior-letter state remains unresolved. The first transcription retains the visible a and the local state doubt. The underline has a full gap beneath n, so its two separate runs are retained from the first reading.',
'B05':'Both drawings expose the long vertical, open upper loop, narrow left appendages, large left curve, central oval, low connector, right loop and terminal, three detached right marks and lower horizontal flourish. A small pale gap interrupts the vertical near its foot, now preserved in the first contour. The complete alphabetic sequence remains unresolved; the unsure wrapper is retained.'}
for c in q['changes']:
 if c['id']==page+'-04':c.update(final=f,evidence=e['B05'],crop=page+'_second_B05.png',box=[942,1878,1129,2015])
for x in q['decisions']:
 if x['id']=='M0097':x.update(reading=f,evidence=e['B05'],crop=page+'_second_B05.png [942,1878,1129,2015]')
for x in q['doubts']:
 if x['place']=='L38, handwritten signature':x.update(reading=f,reason=e['B05'])
q['notes']+=' Blind audit confirms the composite r and a cells without determining the prior glyphs or typing order. The first local uncertainty states and the underline gap beneath n remain. A small gap at the signature stem foot is added to its contour; no alphabetic completion is supplied.'
p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
choices=[dict(box=k,choice='literal' if k=='B05' else 'first',**({'final':f} if k=='B05' else {}),changed=k=='B05',evidence=e[k],confidence='high' if k in ['B01','B02'] else 'medium') for k in d]
(r/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_c',choices=choices),ensure_ascii=False,indent=2)+'\n')
