from pathlib import Path
import json,re
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
R={rn:json.loads((root/'readers'/rn/'scan002.json').read_text()) for rn in ['R1','R2','R3']}
def clean(x):
 if isinstance(x,str):return re.sub(r'\\\\(?=[A-Za-z])',lambda m:'\\',x)
 if isinstance(x,list):return [clean(v) for v in x]
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items()}
 return x
R=clean(R)
rows=[]
map1={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,16:15,17:16,18:17,19:17,20:18,21:19}
map3={1:1,2:2,3:3,4:7,5:6,6:8,7:9,8:10,9:11,10:12,11:13,12:14,13:15,14:16,15:17,16:18,17:19,18:20,19:21,20:22,21:23}
for n,d0 in enumerate(R['R2']['differences'][:21],1):
 d=d0.copy();d['id']=f'002-{n:02d}';d['final']=d.pop('reading');d['readers']={'R2':d['final']}
 for rn,mp in [('R1',map1),('R3',map3)]:
  d['readers'][rn]=R[rn]['differences'][mp[n]-1]['reading'] if n in mp else d['final']
 rows.append(d)
# Explicit adjudications at every inter-reader difference.
rows[0]['evidence']+=' M retains GF|CF: the number of letters is settled; the open first capital does not securely distinguish G from C.'
rows[1]['crop']='crops/main/002_title.png'
rows[2]['readers']['R3']='Cf surtout p. 23 50-58, 59; arrowed oval 110-113'
rows[2]['evidence']+=' R1’s proposed separator after 23 is the upper return/arrowhead of the oval below; M does not read a separate dash or comma between 23 and 50.'
rows[6]['crop']='crops/main/002_des_proprietes.png'
rows[8]['crop']='crops/main/002_proprement.png'
rows[9]['evidence']+=' R1 and R3 read des here; M selects R2’s de from the short connector, in contrast to the additional hump in the first des.'
rows[12]['evidence']+=' R1 retains a doubt on autour; M resolves it from the looped a, low u, tall t, following rounded strokes and r, without supplying H’s additional word.'
rows[14]['crop']='crops/main/002_sine.png';rows[14]['marked_in_H']=True
rows[16]['crop']='crops/main/002_sens.png'
rows[17]['evidence']+=' R1 leaves joueront as an alternative. M selects pourront: the descender joins an o-like bowl, whereas a distinct j followed by o-u-e is not present. The missing infinitive remains missing.'
rows[18]['readers']={rn:r'\unsure{doute}' for rn in R}
rows[19]['evidence']+=' R3 retains the grave as an alternative; M resolves the right-rising mark as acute, retaining piéces.'
# Log each literal quotation locus separately; equivalent emphasis macros alone are not counted.
quoted=[('algèbre des figures','crops/main/002_quotes_opening.png'),('atelier','crops/main/002_quotes_opening.png'),('algébriques','crops/main/002_quotes_algebriques.png'),('propriété combinatoires fines','readers/R2/crops/scan002_propriete.png; readers/R2/crops/scan002_fines.png'),('sine qua non','crops/main/002_sine.png'),('facultatifs','crops/main/002_quotes_facultatifs.png')]
for k,(q,crop) in enumerate(quoted,22):
 rows.append({'id':f'002-{k:02d}','place':'quotation pair around '+q,'C':"``…''",'H':'« … »','final':"``…''",'readers':{rn:"``…''" for rn in R},'diff_C':False,'diff_H':True,'kind':'other','marked_in_H':False,'confidence':'high','evidence':'Two short raised opening strokes and two raised closing strokes, not angular guillemets. Lexical differences within the phrase are logged separately.','crop':crop})
# Preserve the complete R2 reading after adjudication.
text=(root/'readers/R2/scan002.tex').read_text()
(root/'pages/H156-01_156-7_scan002.tex').write_text(text)
audit=[]
for item in R['R2']['C_doubt_audit']:
 s=item['C_reading'];place=item.get('place','');status=item['status']
 if s=='Chp|Chap':final=r'\unsure{GF|CF}';status='changed; first-capital doubt retained'
 elif s=='doute':final=r'\unsure{doute}';status='retained'
 else:
  final={'23|213':'23','--':'--','dominant|donnant':'dominant','densité':'densité','propriété|propriétés':'propriété','autour':'autour','simplexe|simplexes':'simplexe','joueront|pourront':'pourront','sans':'sans','piéces|pièces':'piéces','les|la|le':'le'}.get(s,s)
  status='resolved'
 audit.append({'place':place,'C':s,'status':status,'final':final,'evidence':item.get('crop','')+'; see corresponding adjudication row.'})
inv=[('text','top centre','1'),('margin note','upper-right ruled corner',r'\unsure{GF|CF} VII'),('text','heading','Analysis Situs (troisième mouture)'),('margin note','upper right, slanted','Cf surtout p. 23 50-58, 59; 110-113'),('drawing','around the final marginal range','arrowed oval around 110-113; ruled chapter corner'),('text','below heading, left','23 juin (underlined)'),('text','paragraph 1','Je récapitule les données et axiomes'),('margin note','left of paragraph 1','short grey dash'),('insertion','above géométriques','proprement (underlined)'),('text','paragraph 2','Parmi les axiomes, je distingue')]
record={'scan':2,'decided_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':rows,'C_doubt_audit':audit,'unresolved':[{'place':'upper-right inscription','reading':r'\unsure{GF|CF} VII','alternatives':'CF for GF','confidence':'medium','reason':'Two capitals are clear; the open first capital has no decisive inner bar.'},{'place':'paragraph 2, before un rôle','reading':r'\unsure{doute}','alternatives':'none separately legible','confidence':'medium','reason':'The d and final knot are visible; the medial strokes are compressed.'}], 'inventory':[{'kind':k,'position':p,'first_words_or_objects':f} for k,p,f in inv], 'notation':[{'sign':'Quotation marks','latex':"``…''",'evidence':'Scan 002, six quoted expressions: paired short raised strokes.','status':'settled'},{'sign':'Axiom labels','latex':'At~1; At~7','evidence':'Scan 002, paragraph 2: baseline At followed by a numeral.','status':'settled'},{'sign':'Chapter initials','latex':r'\unsure{GF|CF} VII','evidence':'Scan 002, upper-right ruled corner: two large capitals, not a four-letter abbreviation.','status':'first capital uncertain'},{'sign':'Underlining and interlinear insertion','latex':r'\uline{…}; \inserted{\uline{proprement}}','evidence':'Scan 002: date, atelier and proprement each carry a single underline; proprement is above the line.','status':'settled'}], 'abbreviations':[{'form':'Cf','meaning':'confer / compare','location':'002, upper-right reference'},{'form':'p.','meaning':'page(s)','location':'002, upper-right reference'},{'form':'At','meaning':'axiome d’atelier (provisional expansion)','location':'002, paragraph 2'},{'form':'GF','meaning':'Unexpanded here; the first capital remains uncertain.','location':'002, chapter inscription'}], 'notes':[
'**Statement 002-N1.** The opening sheet recapitulates the data and axioms of an “algèbre des figures” or atelier, restricting the present discussion to the algebraic formalism. It explicitly sets aside topological properties including **densité**, connexity and acyclicity, geometrical properties, and fine combinatorial properties surrounding the simplex notion (Grothendieck, 1986, scan 2, paragraph 1). This is a record of the page’s scope, not a theorem check.',
'**Statement 002-N2.** At 1–At 7 are singled out as “sine qua non”; the other axioms are described as more or less “facultatifs” at the algebraic level. His qualifications are “qui me paraissent les plus essentielles” and “Ils pourront sans [doute] un rôle crucial”. The compressed word doute remains marked in the transcription. The line does not supply an infinitive after pourront, and no avoir or jouer is inserted (scan 2, paragraph 2).',
'**Reading decisions.** H’s dimension is contradicted by the short densité with its crossed t; H’s finies has an extra i unsupported by the ink. The phrase le sens géométrico-topologique is retained against H’s la seule géométrie topologique. These are visual readings, not mathematical deductions. The feminine essentielles, singular propriété after les, and acute piéces are preserved as written. The second algèbre phrase reads de figures; the first reads des figures.',
'**Title and date.** Analysis Situs (troisième mouture), underlined 23 juin, manuscript page 1, and upper-right GF|CF VII. The slanted reference gives p. 23 50-58, 59 and an arrowed oval around 110-113. No year or total page count is written on this sheet. No explicit à vérifier, sauf erreur or proof obligation occurs here.'
], 'check_events':[{'statement_id':'002-N1','date':datetime.now(timezone.utc).date().isoformat(),'who':'M; GPT-6 Astra Pro; effort not exposed; SP35 run','type':'carried as background without fault found','outcome':'Source-grounded account of the page’s declared scope; checked visually against both halves and the densité/fines crops. No mathematical proof attempted.'},{'statement_id':'002-N2','date':datetime.now(timezone.utc).date().isoformat(),'who':'M; GPT-6 Astra Pro; effort not exposed; SP35 run','type':'carried as background without fault found','outcome':'Author’s distinction and qualifications are recorded as assertions; no claim of necessity/sufficiency proved. Missing infinitive preserved.'}], 'main_images_viewed':['whole','half a','half b']+[str(p.relative_to(root)) for p in sorted((root/'crops/main').glob('002_*.png'))]+[str(p.relative_to(root)) for p in sorted((root/'readers/R2/crops').glob('scan002_*.png'))]}
(root/'records/scan002.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
