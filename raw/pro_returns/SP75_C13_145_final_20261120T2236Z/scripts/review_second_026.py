from adjudication_io import E,read_rows,write_adjudication
import json
r=json.loads((E/'reader_reports/145_scan026_reviewed.json').read_text())
f={x['box']:x['reading'] for x in read_rows(E/'second/145_scan026_first.tsv')}
b={x['box']:[int(x[k]) for k in ['x0','y0','x1','y1']] for x in read_rows(E/'second/145_scan026_boxes.tsv')}
n=dict(f)
oa=r'(\alpha_i)_{i\in\{0,1,\infty\}}';na=r'(\unsure{\alpha^i|\alpha_i|\alpha\prime})_{i\in\{0,1,\infty\}}'
ow=r'\unsure{de|dans}';nw=r'\unsure{de|des|dans}'
ot=r'\deleted{\unsure{(l_i^{\alpha_i}g^{-1})}}';nt=r'\deleted{\unsure{(l_i^{\alpha_i}g^{-1})|(l_i^{\alpha_i}g)}}'
og=r'\unsure{\sim|\deleted{\sim}}';ng=r'\unsure{\sim|\deleted{\sim}|\infty}'
ol=r'\deleted{\unsure{leurs}}';nl=r'\deleted{\unsure{leurs|par la|de la}}'
of=r'\gamma_{i+1}(\bar u)';nf=r'\gamma_{i+1}\unsure{(}\bar u)'
oi=r'\unsure{i.e.}';ni=r'\unsure{i.e.|ici}'
ou=r'\unsure{si} $\tilde u$ est défini par';nu=r'\unsure{si} $\unsure{\hat u|\tilde u}$ est défini par'
pairs=[(oa,na),(ow,nw),(ot,nt),(og,ng),(ol,nl),(of,nf),(oi,ni),(ou,nu)]
for bid in ['B01','B02','B03','B04','B06']:
 for old,new in pairs:n[bid]=n[bid].replace(old,new)
c={
'B01':{'final':n['B01'],'changed':True,'adjudication':'Qualify the small mark beside the opening alpha, preserving its visibly raised placement as the first reading.','ink':'The small upright lies high at the right of alpha, nearer its upper level than the low outer i in the family index. Its dot and stem are not independently clean, so raised i, lower i and a prime remain possible. The first displayed alternative preserves the observed raised position. The outer index still has a distinct i, membership sign,0,1,infinity and braces; the rest reads en associant à ... le système.'},
'B02':{'final':n['B02'],'changed':True,'adjudication':'Retain the tuple point and two separate cancelled trials; broaden the old word and the second trial’s inverse alternative.','ink':'The tuple’s subscript consists of one detached dark point; no separate short i stem follows it. The first old formula has its own enclosing curves and dense diagonal hatching. The second has a clear g-like descender but the high mark beside it merges with cancellation and the closing curve; it may include an inverse or no inverse, so neither is certified. The first cancelled word starts with a d loop and low e-like trace, but its final dark turn also permits des as well as the retained dans alternative. The live p=1 and final gl_i to alpha_i are unchanged.'},
'B03':{'final':n['B03'],'changed':True,'adjudication':'Retain the operations sentence and overwritten old symbol; allow an infinity-shaped reading of each extra upper mark.','ink':'The word sur before the parenthesis is crossed independently; its s/u/r bodies remain visible. The later sur has the small initial return and joined u/r course and is live. The old body before tilded u has stacked rounded turns and remains u/epsilon uncertain. Above each double hat the dark extra mark has a shallow joined two-loop appearance: a wave, an overstruck wave, or infinity remain possible. The two hats and separate raised exclamation in each group are distinct and retained.'},
'B04':{'final':n['B04'],'changed':True,'adjudication':'Retain live par and conjugaison; broaden the obscured old short phrase and preserve de rho, On trouve and the cancellation after que.','ink':'The live p/a/r group is just above the heavy crossing line, whose contact with its low stroke does not cancel the whole word. The older material below is crossed; tall and low remnants permit leurs, par la or de la, without a fully legible sequence. Conjugaison has the long descending middle stroke and joined ending and is separate from the oblique marginal words. After en particulier, de and the descending rho with a stop are present; On has the open capital O and n before the tall t of trouve. The later long cancellation crosses the doubtful descended p and the readable parenthesis bien sûr.'},
'B05':{'use_first':True,'adjudication':'Retain les, double quotation marks and the complete covariants phrase.','ink':'The initial word has a high l and low joined es despite the adjacent oblique note. Gamma_i is separate, sont has its short s and high terminal t, and covariants has the c/o/v course and final t/s. Two short high ticks open the quotation and a compressed pair closes it; there are no guillemets. Rho has the looped head and long lower stem.'},
'B06':{'final':n['B06'],'changed':True,'adjudication':'Retain the plus index and barred right u; qualify the opening before it and the accent on the cancelled u below.','ink':'The index visibly has a vertical stroke crossing the short horizontal between i and1. The mark over the right u is a short level bar, unlike the wave over the left u. The curved stroke at the right argument’s left edge is partly joined to the u entry and is not securely a separate opening parenthesis, so that one character is qualified. On the cancelled line the accent above u has an angular peak with two sloping arms, favoring a hat, but the dense crossing and short span leave tilde as an alternative. The first short crossed cluster can be i.e. or ici; the separate later si remains qualified.'},
'B07':{'use_first':True,'adjudication':'Retain the marginal text and distinguish it from crossing main-line words and formulas.','ink':'In the margin’s direction the first line reads Il y a lieu, then d’introduire un and groupe S-hatted-E extension. The first Z has its own detached hat; the second does not. Déduite begins with two tall d strokes, and canonique has its q descender. A separate Gamma with cap and long leg followed by par occurs before the next-line Z; it is not absent. The next long introduire course and live des relèvements are followed by sigma_i,rho and the longer par/des/éléments/de sequence ending at S-hatted-E. Main-line conjugaison and de rho cross that region in a different direction; their strokes do not produce a second marginal int(l_i),rho formula. The small old word remains cancelled and doubtful; four separate continuation points end the note.'}}
for x in r['changes']:
 for old,new in pairs:x['final']=x['final'].replace(old,new)
 if x['id'] in ['s026-01','s026-04']:
  x.update(ink=c['B02']['ink'],crop='crops/second_145_scan026_B02.png',box=b['B02'])
 if x['id'] in ['s026-08','s026-12']:
  x.update(ink=c['B03']['ink'],crop='crops/second_145_scan026_B03.png',box=b['B03'])
 if x['id']=='s026-13':x.update(ink=c['B04']['ink'],confidence='low',crop='crops/second_145_scan026_B04.png',box=b['B04'])
 if x['id']=='s026-18':x.update(ink=c['B06']['ink'],crop='crops/second_145_scan026_B06.png',box=b['B06'])
 if x['id']=='s026-19':x['ink']=x['ink'].replace('The following tilde-u, est, défini and par remain readable.','The following u has a hat/tilde qualification after the blind audit; est, défini and par remain readable.')
r['changes'].extend([
 {'id':'s026-32','place':'Opening alpha family, small mark beside alpha','C':r'\alpha_i','H':r'\alpha_i','final':r'\unsure{\alpha^i|\alpha_i|\alpha\prime}','ink':c['B01']['ink'],'confidence':'medium','kind':'misread symbol or index','c_changed':True,'h_changed':True,'marked_in_H':'no','crop':'crops/second_145_scan026_B01.png','box':b['B01'],'error_category':[1],'math_consequence':'The local small mark is preserved at its apparent height; the outer family index remains i in{0,1,infinity}.'},
 {'id':'s026-33','place':'Last cancelled line, accent on u','C':r'\tilde u','H':r'\tilde u','final':r'\unsure{\hat u|\tilde u}','ink':c['B06']['ink'],'confidence':'medium','kind':'misread symbol or index','c_changed':True,'h_changed':True,'marked_in_H':'no','crop':'crops/second_145_scan026_B06.png','box':b['B06'],'error_category':[1,7],'math_consequence':''}])
for x in r['unlisted_decisions']:
 for old,new in pairs:x['reading']=x['reading'].replace(old,new)
 if x['id']=='U026-02':x.update(ink=c['B02']['ink'],crop='crops/second_145_scan026_B02.png',box=b['B02'])
 if x['id']=='U026-04':x.update(ink=c['B04']['ink'],crop='crops/second_145_scan026_B04.png',box=b['B04'])
for x in r['doubts']:
 for old,new in pairs:x['reading']=x['reading'].replace(old,new)
 if x['place']=='parameter line, initial cancelled word':x.update(alternatives=['de','des','dans'],reason=c['B02']['ink'])
 if x['place']=='parameter line, second cancelled trial':x.update(alternatives=[r'(l_i^{\alpha_i}g^{-1})',r'(l_i^{\alpha_i}g)'],reason=c['B02']['ink'])
 if 'upper group adornment' in x['place']:x.update(alternatives=['wave','cancelled wave','infinity-shaped mark'],reason=c['B03']['ink'])
 if x['place']=='main prose, cancelled word after par':x.update(alternatives=['leurs','par la','de la'],reason=c['B04']['ink'])
 if x['place']=='last cancelled line, first cluster':x.update(alternatives=['i.e.','ici','obscured initial cluster'],reason=c['B06']['ink'])
r['doubts'].extend([
 {'place':'Opening family, small alpha mark','reading':r'\unsure{\alpha^i|\alpha_i|\alpha\prime}','alternatives':[r'\alpha^i',r'\alpha_i',r'\alpha\prime'],'confidence':'medium','reason':c['B01']['ink']},
 {'place':'Covariance formula, opening before barred u','reading':r'\unsure{(}','alternatives':['opening parenthesis','curved entry stroke of u without separate parenthesis'],'confidence':'medium','reason':c['B06']['ink']},
 {'place':'Last cancelled line, u accent','reading':r'\unsure{\hat u|\tilde u}','alternatives':[r'\hat u',r'\tilde u'],'confidence':'medium','reason':c['B06']['ink']}])
for x in r['inventory']:
 for old,new in pairs:x['first_words_or_objects']=x['first_words_or_objects'].replace(old,new)
for x in r['notation']:
 for old,new in pairs:x['form']=x['form'].replace(old,new)
 if x['form']=='(g_\\cdot)':x['qualification']='The tuple point is distinct from the outer family i; the small mark immediately beside the opening alpha remains raised-i/lower-i/prime uncertain.'
r['notation'].append({'form':r'\unsure{\alpha^i|\alpha_i|\alpha\prime};\unsure{\hat u|\tilde u}','places':['opening alpha family','u in final cancelled line'],'observation':'The first small mark lies high; the cancelled u accent has an angular peak. Both remain qualified after the independent reading.','qualification':'No uniform index placement or accent is imposed from the mathematical role.'})
r['notes'][0]+=' The small mark beside the opening alpha lies high and is now qualified as raised i/lower i/prime. The second cancelled trial also allows no surviving inverse after g.'
r['notes'][1]+=' The weak opening parenthesis before the barred right u is qualified separately, without changing the bar or the plus index.'
r['notes'][2]+=' Each extra trace also admits an infinity-shaped reading; this does not assign it a mathematical meaning.'
r['notes'][3]=r['notes'][3].replace('Before tilde-u','Before the hat/tilde-qualified u').replace('doubtful i.e., suggested by H','doubtful i.e./ici, with i.e. originally suggested by H')
r['notes'][5]=r['notes'][5].replace('old leurs;','old leurs/par la/de la;')
r['notes'].append('The blind audit preserves all marginal words after separating their direction from crossing main-line strokes; it supplies no extra marginal formula. It broadens pale and cancelled letterforms rather than choosing them from the kernel or covariance computations. The bar on the live right u remains resolved on ink; the different accent on the cancelled u below remains hat/tilde uncertain. The mathematical check events are unchanged.')
r['hand'].append({'habit':'A small raised mark may be an index or prime; an angular accent under cancellation need not match a nearby live tilde.','places':['opening alpha family','u in last cancelled line'],'universal_on_page':False,'witness_effect':'Both witnesses give a lower alpha index and a tilde in the cancelled line; the second reading prompts explicit local alternatives.'})
edits=[{'old':old,'new':new,'count':2 if old==og else 1} for old,new in pairs]
write_adjudication(26,'/root/reader_c',c,edits,report_replace={k:r[k] for k in ['changes','unlisted_decisions','doubts','inventory','notation','notes','hand']})
