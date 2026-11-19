from pathlib import Path
import json,re
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
def clean(x):
 if isinstance(x,str):return re.sub(r'\\\\(?=[A-Za-z])',lambda m:'\\',x)
 if isinstance(x,list):return [clean(v) for v in x]
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items()}
 return x
R=clean({rn:json.loads((root/'readers'/rn/'scan003.json').read_text()) for rn in ['R1','R2','R3']})
T={rn:(root/'readers'/rn/'scan003.tex').read_text() for rn in R}
def argument(s,macro):
 start=s.index(macro+'{')+len(macro)+1;depth=1
 for i in range(start,len(s)):
  if s[i]=='{' and s[i-1]!='\\':depth+=1
  elif s[i]=='}' and s[i-1]!='\\':
   depth-=1
   if depth==0:return s[start:i]
 raise ValueError(macro)
final=T['R3'].replace(r'\unsure{géométrique} à ce',r'\unsure{géométrique} \unsure{à} \unsure{ce}')
(root/'pages/H156-01_156-7_scan003.tex').write_text(final)
m1={1:1,2:2,4:3,5:4,6:5,7:6,8:7,9:8,10:9,11:10,12:11,13:12,14:13,15:14,16:15,17:16,18:17,19:18,20:19}
m3={1:1,2:4,3:5,4:6,5:7,6:8,7:9,8:10,9:11,10:12,11:13,12:14,13:15,14:16,15:17,16:18,17:19,18:20,19:21,20:22}
rows=[]
for n,d0 in enumerate(R['R2']['differences'][:20],1):
 d=d0.copy();d['id']=f'003-{n:02d}';d['final']=d.pop('reading');d['readers']={'R2':d['final']}
 for rn,mp in [('R1',m1),('R3',m3)]:
  v=R[rn]['differences'][mp[n]-1]['reading'] if n in mp else d['final']
  d['readers'][rn]=d['C'] if v=='same as C' else v
 rows.append(d)
rows[0]['crop']='readers/R1/crops/scan003_contexte.jpg'
rows[1].update({'C':r"(voire, la notion de ``lieu ponctuel'' ou ``point'', dont il n'a pas encore été question\ldots)",'H':r'(voire, \ill{} la notion de « lieu ponctuel » — ou « point » \ill{} — qui \ill{} par avoir été \ill{}…)','final':r"(voire, la notion de ``lieu ponctuel'' ou ``point'', dont il n'a pas encore été question\ldots)",'crop':'readers/R3/crops/003_body_parenthesis.png'})
rows[1]['readers']={rn:rows[1]['final'] for rn in R}
rows[2]['crop']='crops/main/003_simplicite.png'
rows[3]['crop']='readers/R1/crops/scan003_margin.jpg'
rows[4]['crop']='readers/R1/crops/scan003_lieux.jpg'
rows[5]['crop']='readers/R1/crops/scan003_etant.jpg';rows[5]['confidence']='medium';rows[5]['evidence']+=' R1 retains the doubt; M selects the visible initial e/t and terminal n/t, as R2 and R3 do.'
rows[6]['final']=r'figure \inserted{$F$}';rows[6]['crop']='readers/R1/crops/scan003_insertions.jpg'
rows[7]['final']=r"\inserted{(par l'ens de ses ``strates'')}";rows[7]['crop']='readers/R1/crops/scan003_insertions.jpg'
rows[8]['crop']='crops/main/003_comme_partie.png'
rows[9]['final']=r"de l'ens";rows[9]['crop']='readers/R3/crops/003_ens_M.png'
rows[10]['crop']='readers/R3/crops/003_ens_M.png'
rows[11]['final']=r'\inserted{(ordonné par $\leq$)} after M';rows[11]['crop']='readers/R1/crops/scan003_insertions.jpg'
rows[12]['final']="l'écrivons";rows[12]['crop']='readers/R1/crops/scan003_lecrivons.jpg'
rows[13]['final']=r'\mathrm{Mulomb}(F)';rows[13]['crop']='readers/R3/crops/003_operators.png'
rows[14]['crop']='crops/main/003_est.png'
rows[15]['final']=r'\mathrm{Mulomb}(F)';rows[15]['crop']='crops/main/003_mulomb2.png'
rows[16]['crop']='crops/main/003_permet.png'
rows[17]['crop']='readers/R1/crops/scan003_reconstituer.jpg'
rows[18]['crop']='readers/R1/crops/scan003_deleted.jpg'
rows[19].update({'final':"son ``support'' seulement",'diff_C':False,'diff_H':True,'crop':'crops/main/003_support_opening.png; readers/R2/crops/scan003_support_quotes.png','confidence':'medium','evidence':'The added upper-extent crop shows a small joined pair above the beginning of support; the second pair lies after support. R2’s crop clipped the upper tips of the opening pair and led to an opening quote before seulement. M retains C/R1/R3’s quotation around support.'})
# One full marginal locus, with each individual C doubt separately audited below.
csource=(root.parent/'source/SP35_CW_156-7_witnesses/codex/H156-01/pages/H156-01_156-7_scan003.tex').read_text()
rows.append({'id':'003-21','place':'entire slanted marginal note, overlapping body text','C':argument(csource,r'\margin'),'H':r"L'autre raison \ill{} « \ill{} » \ill{} simplicité \ill{} figures \ill{} multistrates",'final':argument(final,r'\margin'),'readers':{rn:argument(T[rn],r'\margin') for rn in R},'diff_C':True,'diff_H':True,'kind':r'readable ink left as \ill{}','marked_in_H':True,'confidence':'low','evidence':'Following the rotated marginal baseline recovers application f, région, image inverse, figure, the parenthetical qualification and the reciprocal-image clause with abbreviated multistr. H’s simplicité belongs to the intersecting main text. Donner and tend are distinguishable; quand/on and the crossed words géométrique, à, ce, mot/terme, sera, pas and encore remain locally uncertain. R1/R2/R3’s different doubt dispositions are preserved in the adjacent readings and individual audits. The crossing through sera is an actual cancellation; the oblique crossings elsewhere are the two text directions, not deletions.','crop':'readers/R1/crops/scan003_margin.jpg','math_consequence':'The long marginal comparison of inverse images of figures and multistrates is recovered from H’s fragments, but its intersected words remain doubtful; no mathematical truth is inferred from the reconstruction.'})
# Quotation-locus rows not already fully represented by another row.
for n,q in enumerate(['contrée','figure élémentaire','multistrate','lieu','grande multiombre','grande ombre'],22):
 rows.append({'id':f'003-{n:02d}','place':'quotation pair around '+q,'C':"``…''",'H':'« … »','final':"``…''",'readers':{rn:"``…''" for rn in R},'diff_C':False,'diff_H':True,'kind':'other','marked_in_H':False,'confidence':'high','evidence':'Paired raised quotation strokes occur at this expression in the supplied halves. This systematic punctuation difference is listed at its own locus; the full parenthetical, insertion and marginal-note rows cover their internal quotation pairs.','crop':None})
# Main image inspection corroborates all such pairs in whole/halves; no duplicate crops of settled punctuation.
retained={'quand|quant','on','géométrique','à','ce','mot|terme','sera','pas','encore','M|mathcal M'}
replacements={'contexte|contextes':'contexte','donner':'donner','tend':'tend','étant':'étant','ens|ensemble':'ens','ens':'ens','ordonné':'ordonné','par|pour':'par','l’écrivons|l’écrirons':"l'écrivons",'il|le':r'\deleted{\unsure{le|il}}','M|mathcal M':r'\unsure{M|\mathcal M}'}
audit=[];unresolved=[]
for a in R['R2']['C_doubt_audit']:
 k=a['C_reading'];v=replacements.get(k,r'\unsure{'+k+'}')
 status='retained' if k in retained else ('changed primary; retained' if k=='il|le' else 'resolved')
 audit.append({'place':a['place'],'C':k,'status':status,'final':v,'evidence':('readers/R1/crops/scan003_margin.jpg' if 'margin' in a['place'] else a['crop'])+'; main decision follows the preserved intersecting ink.'})
 if k in retained or k=='il|le':
  alternatives=k.split('|')[1:] if '|' in k else []
  unresolved.append({'place':a['place']+': '+k,'reading':v,'alternatives':' / '.join(alternatives),'confidence':'low' if 'margin' in a['place'] or k=='il|le' else 'medium','reason':'Intersecting strokes/cancellation obscure the word.' if 'margin' in a['place'] or k=='il|le' else 'The capital’s handwritten form does not securely determine the typographic alphabet.'})
inv=[('text','top centre','2'),('text','opening continuation','contexte d’un atelier définissant une contrée'),('text','main paragraph, upper part','Le travail précédent a permis de dégager'),('margin note','left, sloping across body','L’autre raison, c’est que'),('deletion','within sloping note',r'\unsure{sera}'),('text','main paragraph, middle','où il est agréable de pouvoir manipuler'),('insertion','above figure est','F'),('insertion','above comme, attached after interprétée','(par l’ens de ses strates)'),('insertion','above M with bracket pointer','(ordonné par ≤)'),('text','main paragraph, lower part','Quand elle est interprétée comme une figure'),('insertion','above figure dans M','ensembliste'),('deletion','penultimate line, after F',r'\unsure{le|il}')]
now=datetime.now(timezone.utc)
rec={'scan':3,'decided_utc':now.strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':rows,'C_doubt_audit':audit,'unresolved':unresolved,'inventory':[{'kind':k,'position':p,'first_words_or_objects':v} for k,p,v in inv],'notation':[{'sign':'Figure and its stratum set','latex':r'F; \widetilde F','evidence':'003, middle: angular capital F and a separate wave above it in the set notation.','status':'settled'},{'sign':'Set of multistrates','latex':r'\unsure{M|\mathcal M}; M','evidence':'003, after ens: two tall bowed stems with flared foot; plain M preferred, calligraphic remains possible. First occurrence marked; subsequent M follows the first candidate.','status':'recurring alphabet doubt'},{'sign':'Large multiombre and support','latex':r'\mathrm{Mulomb}(F); \mathrm{Omb}(F)','evidence':'003, lower paragraph: Mulomb occurs twice without an intervening t; Omb begins with capital O.','status':'settled'},{'sign':'Order relation','latex':r'\leq','evidence':'003, inserted ordonné par: one angle with a short lower horizontal stroke.','status':'settled'}],'abbreviations':[{'form':'ens','meaning':'ensemble','location':'003, two body/insertion occurrences without full stops'},{'form':'multistr.','meaning':'multistrate','location':'003, slanted note'},{'form':'Mulomb','meaning':'multiombre (large initial denotes grande multiombre here)','location':'003, lower paragraph'},{'form':'Omb','meaning':'ombre (grande ombre here)','location':'003, lower paragraph'}],'notes':[
'**Statement 003-N1.** The page presents figure as the basic notion, treating multistrates and lieux as particular figures. It distinguishes a figure F, its set of strata F̃, its grande multiombre Mulomb(F), and the support Omb(F); it states that the latter practically never reconstructs the figure, only its “support” (Grothendieck, 1986, scan 3, main paragraph). This is recorded as the author’s explanation, with no independent reconstruction theorem checked.',
'**Statement 003-N2.** The oblique note supplies another reason, discussing an “application f” between “régions” and comparing inverse images of figures with reciprocal images of multistrates. The crossed words, including the negative clause, are retained with local doubts; no general inverse-image theorem is inferred. The earlier word sera is cancelled. H’s marginal fragments include simplicité from the body text rather than the oblique baseline.',
'**Reading decisions.** The brace from (ordonné par ≤) points to M, not to partie; its masculine ordonné is retained. F is an interlinear insertion. The operator has no t: Mulomb, at both occurrences. The verbs are est and permet, not H’s participles. Réconstituer has an acute accent. At the foot, an upper-extent crop reveals the opening quotation pair over support, explaining why a crop cut slightly lower could suggest a quote before seulement instead. The cancelled token after F is retained as le|il.',
'**Qualifications and dating.** “me semble bien”, “pratiquement jamais” and “moralement” qualify the exposition. There is no explicit proof-check request, no new title or date, and no total page count. Manuscript page 2 is visible.'
],'check_events':[{'statement_id':'003-N1','date':now.date().isoformat(),'who':'M; GPT-6 Astra Pro; effort not exposed; SP35 run','type':'carried as background without fault found','outcome':'Page’s conceptual distinctions used to locate notation, then verified visually. No injectivity or reconstruction claim proved.'},{'statement_id':'003-N2','date':now.date().isoformat(),'who':'M; GPT-6 Astra Pro; effort not exposed; SP35 run','type':'carried as background without fault found','outcome':'Marginal assertion transcribed with unresolved crossed words; not promoted to a checked mathematical statement.'}],'main_images_viewed':['whole','half a','half b','readers/R1/crops/scan003_margin.jpg','readers/R1/crops/scan003_contexte.jpg','readers/R1/crops/scan003_lieux.jpg','readers/R1/crops/scan003_etant.jpg','readers/R1/crops/scan003_insertions.jpg','readers/R1/crops/scan003_lecrivons.jpg','readers/R1/crops/scan003_reconstituer.jpg','readers/R1/crops/scan003_deleted.jpg','readers/R3/crops/003_body_parenthesis.png','readers/R3/crops/003_operators.png','readers/R3/crops/003_ens_M.png','readers/R2/crops/scan003_support_quotes.png']+[str(p.relative_to(root)) for p in (root/'crops/main').glob('003_*.png')]}
(root/'records/scan003.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
