"""Apply the explicitly adjudicated scan 082 readings and apparatus."""
from pathlib import Path
import json,subprocess,sys
R=Path(__file__).resolve().parents[1]
r=json.loads((R/'adjudicated/147_scan082.json').read_text());changes={x['id']:x for x in r['changes']}
edits=[]
def rep(old,new,count=1):edits.append(dict(old=old,new=new,count=count))
rep("\\Pi M^*_{G,\\deleted{\\unsure{G'}},G''}","\\Pi M^*_{G,\\deleted{\\unsure{G',}}G''}",2)
rep("\\varphi_{G,G''}\"'","\\varphi_{G,\\unsure{G''}}\"'")
rep("\\Pi M_{G\\deleted{,\\unsure{G'}}} \\& \\text{(103)}","\\Pi M_{G,\\deleted{\\unsure{G'}}} \\& \\text{(103)}")
rep('\\deleted{et on a remplacé','\\deleted{et \\unsure{on a} remplacé')
rep('\\inserted{\\deleted{a défini}}','\\inserted{\\deleted{\\unsure{a défini}}}')
rep("\\deleted{,\\unsure{G''|G'}}","\\deleted{\\unsure{,G''|,G'}}")
rep("\\Pi M_{G\\deleted{,\\unsure{G'}}}","\\Pi M_{G\\deleted{\\unsure{,G'}}}",3)
rep("\\gamma_{G,\\deleted{\\unsure{G'}},G''}","\\gamma_{G,\\deleted{\\unsure{G',}}G''}")
rep("\\varphi_{G,G''\\deleted{,\\unsure{G'}}}","\\varphi_{G,G''\\deleted{\\unsure{,G'}}}")
rep("$\\mathbb Z^{C\\amalg C'}$ tordu.","$\\mathbb Z^{C\\amalg C'}$ tordu\\unsure{.}")
rep('on retire de (105) le diagramme','on retire de (105) \\uline{le} diagramme')
updates=[]
def upd(i,final,ink,box,confidence=None,against_C=None):
 c=changes[f'082-RC-{i:02d}']; fields=dict(final=final,ink=c['ink']+' Blind adjudication: '+ink,crop=f'crops/blind/147_scan082/082-B{box:02d}.png')
 coords={1:[302,8,1673,464],4:[315,848,1657,968],5:[318,976,980,1093],7:[315,1420,1680,1733],8:[315,1735,1680,1980],9:[309,1981,1471,2337]}
 # Use the committed coordinate row, never a guessed extent.
 import csv
 rows=list(csv.DictReader((R/'second/147_scan082_boxes.tsv').open(),delimiter='\t'))
 b=next(x for x in rows if x['box']==f'082-B{box:02d}');fields['box']=[int(b[k]) for k in ['x0','y0','x1','y1']]
 if confidence is not None:fields['confidence']=confidence
 if against_C is not None:fields['against_C']=against_C
 updates.append(dict(id=c['id'],expect={'final':c['final']},fields=fields))
upd(1,"\\Pi M^*_{G,\\deleted{\\unsure{G',}}G''}",'The apparent comma after the old index is covered with that index; no separate live comma is visible before the final G double-prime.',1,'medium',True)
upd(8,"\\Pi M_{G,\\deleted{\\unsure{G'}}}",'The comma after the live first G is distinctly left of the first hatching stroke and remains live. The old G-prime remains doubtful.',1,'high',True)
upd(16,'\\inserted{\\deleted{\\unsure{a défini}}}','The raised location and subsequent strike are secure, but the strike hides small letter bodies in défini. The spelling is now locally doubtful.',4)
upd(18,"\\Pi M^*_{G,G''\\deleted{\\unsure{,G''|,G'}}}",'The comma-like low hook is also crossed and is included within the doubt. The blind beta-with-subscript proposal is not secured.',5)
for i,b in [(22,7),(24,8),(29,9)]:upd(i,"\\Pi M_{G\\deleted{\\unsure{,G'}}}",'The old index remains doubtful; its preceding comma cannot be isolated from the hatching and is included within that doubt.',b)
upd(26,"\\Pi M^*_{G,\\deleted{\\unsure{G',}}G''}",'The terminal lower return after the cancelled middle index belongs to the cancelled group. No separate live comma stands before the last G double-prime.',9,'medium',True)
upd(27,"\\gamma_{G,\\deleted{\\unsure{G',}}G''}",'The lower return immediately after the hatched middle index is covered as part of that old group; no independent live comma follows it.',9,'medium',True)
upd(28,"\\varphi_{G,G''\\deleted{\\unsure{,G'}}}",'The preceding comma is caught in the cancellation and cannot be certified separately; the old index remains doubtful.',9)
new=dict(id='082-B01',place='Introduction of (107), underline beneath le',C='le diagramme',H='le diagramme',final='\\uline{le} diagramme',ink='A separate low horizontal stroke runs beneath the tall-loop l and low e, ending after e. No second comma follows the closing parenthesis of (105).',crop='crops/blind/147_scan082/082-B08.png',box=[315,1735,1680,1980],confidence='high',kind='other',against_C=True,against_H=True,consequential=False,category='omissions',marked_in_H=False)
doubts=[dict(place='(105), far-left curved phi label final index',reading="\\varphi_{G,\\unsure{G''}}",alternatives=['G-prime or partly obscured final primes'],confidence='low',reason='The label meets the curved shaft; the terminal letter/primes cannot all be isolated.'),dict(place='First prose paragraph, cancelled on a after et',reading='\\unsure{on a}',alternatives=['pour (blind proposal)'],confidence='low',reason='The e and tall t of et are exposed; the small following bodies are crossed and not all recoverable.'),dict(place='Raised and subsequently cancelled a défini',reading='\\unsure{a défini}',alternatives=[],confidence='low',reason='The horizontal strike traverses the small letters; the tall ascenders alone do not certify the whole phrase.'),dict(place='End of extension paragraph, after tordu',reading='\\unsure{.}',alternatives=['no punctuation; projection of scan edge'],confidence='low',reason='A dark point at the expected terminal position is contiguous with the black edge; the supplementary right-edge crop does not separate them.')]
payload=dict(scan=82,page_replacements=edits,changes_updates=updates,changes_add=[new],doubts_add=doubts,notes_add=['Blind audit: punctuation is treated separately from cancelled letters. The comma after the lower-left live G in (105) remains live; apparent trailing commas of hatched middle groups in (105)/(107) belong within the cancellations. The crossed letters themselves remain doubtful. A visible underline beneath le before diagramme is restored. A point at the right scan edge after tordu is locally uncertain.','Blind comparison does not support replacing en tant qu\'ext. by double ext., or connexe by comme. These decisions are letter-based; the expected extension argument was not used to supply absent words.'])
subprocess.run([sys.executable,str(R/'scripts/apply_audit_edits.py')],input=json.dumps(payload),text=True,check=True)
p=R/'adjudicated/147_scan082.json';r=json.loads(p.read_text())
for d in r['doubts']:
 if d['place']=='First prose cancelled word':d['alternatives'].append('employé (blind proposal; central letters obscured)')
 if d['place'] in ["(105) top-left middle index","(107) upper-left middle index","(107) gamma middle index"]:
  d['reading']="\\unsure{G',}";d['alternatives'].append('beta with subscript G (blind proposal, not established)')
 if d['place'] in ["prose after en tant qu'ext., Pi M_G cancelled index","prose after extension de, Pi M_G cancelled index","(107) phi final index","(107) lower-object final index"]:
  d['reading']="\\unsure{,G'}";d['reason']+=' The comma-like stroke is included in the same local doubt.';d['alternatives'].append('beta with a subscript (blind proposal, not established)')
 if d['place']=='(106), cancelled third index':d['reading']="\\unsure{,G''|,G'}";d['alternatives'].append('beta with subscript G-double-prime (blind proposal, not established)')
for a in r['inventory']:
 if a['element'] in ['082-I15','082-I15D']:a['first_words_or_objects']='a défini, doubtful; inserted above tire de (105), then struck'
 if a['element']=='082-I13':a['first_words_or_objects']='et, doubtful on a, remplacé la notation ... pour Pi M ...'
 if a['element']=='082-I22':a['first_words_or_objects']='De façon plus précise, on retire de (105) \\uline{le} diagramme'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
