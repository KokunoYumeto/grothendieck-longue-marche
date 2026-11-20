from pathlib import Path
import json
O=Path(__file__).resolve().parents[1];p='H162-01_162-1_scan004'
r=json.loads((O/'work'/f'{p}_report.json').read_text());s=(O/'work'/f'{p}_draft.tex').read_text()
s=s.replace(r'\unsure{Rapport|R. Wood} Bourbaki','Rapport Bourbaki')
for c in r['changes']:
 # These corrections affect the recorded bibliographic wording, not mathematics.
 c['consequential']=False
 if c['id']=='r12':
  c['final']='Rapport';c['confidence']='high';c['scan_shows']='The root reads R-a-pp-o-r-t: the small a is compressed, the two low p descenders make the apparent W, and the final tall stroke is t. The same configuration in the Rapport entry on 162-1/003 supports the page-local reading. There is no independent dot or word space that would divide R. Wood. C is retained.'
for b in r['boxes']:
 if b['box']=='b12':b['reading']='Rapport Bourbaki calcul différentiel'
r['doubts']=[d for d in r['doubts'] if not(d['line']=='L10' and d['reading']=='Rapport')]
for i in r['inventory']:
 i['sheet_kind']='list';i['first_words_or_objects']=i['first_words_or_objects'].replace('Rapport/R. Wood','Rapport')
r['reading_notes']=[n.replace('a Rapport/R. Wood Bourbaki entry','a Rapport Bourbaki entry') for n in r['reading_notes']]
r['notes'].append('Root adjudication: the whole page and all 32 saved crops were inspected. Rapport is read without the first-reader alternative after the two low p descenders and final t were compared with the same word on the preceding list sheet. Other retained uncertainties remain explicit. No mathematical check was inferred from a bibliographic label.')
r['hand_log'].append('Root comparison 162-1/003–004: the compressed a and two low p descenders of Rapport recur in both Bourbaki entries. The visible final t and absence of an independent full W support Rapport at both sites. This is a two-occurrence observation, not a universal hand rule; H reads R. Wood at both.')
(O/'work'/f'{p}_decided.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));(O/'pages'/f'{p}.tex').write_text(s)
pth=O/'work/abbreviations.md';a=pth.read_text().replace('| Ch. / Coh. | cohomologie, proposed; exact letters to be adjudicated in place |','| Ch. | cohomologie, proposed; the written Ch. is retained |');pth.write_text(a)
