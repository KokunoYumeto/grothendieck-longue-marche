#!/usr/bin/env python3
"""Materialize the root's explicit scan-027 adjudications; no automatic reading."""
from pathlib import Path
from copy import deepcopy
import json

ROOT=Path(__file__).resolve().parents[1]
raw={w:json.loads((ROOT/f'readers/scan027/{w}/review.json').read_text()) for w in 'ABC'}
idx={w:{int(x['id'].split('-')[-1]):x for x in raw[w]['loci']} for w in 'ABC'}
amap={1:1,2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:9,10:10,11:11,12:12,13:13,14:14,15:15,16:17,17:16,18:18,19:19,20:20,21:21,22:22,23:23,24:24,25:25,26:26,27:27,28:28,29:29,30:30,31:45,32:31,33:32,34:33,35:34,36:35,37:36,38:37,39:38,40:39,41:40,42:41,43:42}
cmap={1:1,2:1,3:2,4:3,5:5,6:6,7:4,8:7,9:9,10:10,11:11,12:12,13:13,14:14,15:15,16:17,17:16,18:18,19:19,20:20,21:21,22:22,23:23,24:24,25:25,26:26,27:28,28:27,29:28,30:28,31:30,32:28,33:8,34:8,35:31,36:32,37:33,38:34,39:35,40:36,41:37,42:38,43:39}
cropmap={1:'A/01_heading.png',2:'A/01_heading.png',3:'A/02_initial_soient.png; B/02_opening.png',4:'A/02_initial_soient.png',5:'main/01_product_direct.png',6:'B/03_rank_and_soit.png',7:'main/04_second_ens.png',8:'B/03_rank_and_soit.png',9:'A/05_on_a_un_isom.png',10:'A/05_on_a_un_isom.png',11:'main/02_boxed_formula.png',12:'B/05_comme.png',13:'A/06_un_quotient.png',14:'A/06_un_quotient.png',15:'A/07_nb.png',16:'A/07_nb.png',17:'A/07_nb.png',18:'A/08_enumeration.png',19:'A/09_inserted_j_et_forall_b.png',20:'A/09_inserted_j_et_forall_b.png',21:'A/09_inserted_j_et_forall_b.png',22:'A/09_inserted_j_et_forall_b.png',23:'A/09_inserted_j_et_forall_b.png',24:'A/10_basis_overwrite.png',25:'A/10_basis_overwrite.png',26:'A/11_basis_left.png',27:'A/11_basis_left.png',28:'A/11_basis_left.png',29:'A/11_basis_left.png; A/12_basis_right.png',30:'A/12_basis_right.png',31:'A/12_basis_right.png',32:'A/12_basis_right.png',33:'main/05_first_Gl.png',34:'main/06_second_Gl.png',35:'A/13_sum_parenthesis.png',36:'A/14_inserted_conclusion.png',37:'A/14_inserted_conclusion.png',38:'main/03_On_change.png',39:'A/15_cancelled_power.png',40:'A/16_final_lines.png',41:'A/16_final_lines.png',42:'A/16_final_lines.png',43:'A/16_final_lines.png'}
loci=[]
for n in range(1,44):
    x=deepcopy(idx['B'][n]);x['id']=f'S027-{n:02}'
    x['readers']={'A':idx['A'][amap[n]]['reading'],'B':idx['B'][n]['reading'],'C':idx['C'][cmap[n]]['reading']}
    x['crop']='scan027/'+cropmap[n]
    x['decision']='Main-reader crop inspection supports the stated reading; source-coordinate manifests are retained.'
    x.pop('box',None)
    loci.append(x)
q={n:loci[n-1] for n in range(1,44)}
q[5]['evidence']='Reader B settled the curved upper stroke above a separate short horizontal rule from half a. The main reader subsequently inspected the cited tight crop and confirmed those two strokes and the simeq reading.'
q[1].update(reading="d'associativité",confidence='high',evidence='The tall final t is followed by the accented, hooked terminal e; there is no further letter after that e. The hook belongs to the e body. Reader A retained the plural alternative; the main crop supports the singular.',decision='Resolve the C heading doubt, agreeing with B and C on the final e.')
q[2]['readers']={w:r'\uline{Formules d’associativité…}' for w in 'ABC'}
q[3].update(reading=r'\unsure{Soit|Soient}',diff_C=True,confidence='low',evidence='The compressed body consists of joined loops between a tall initial and one terminal upstroke. Soit is the leading visual reading; Soient remains possible. The low joining stroke follows the letters without an independent cancellation bar.',decision='Retain both live readings, with Soit first as in reader C; A and B lead with Soient.')
q[8].update(location='definition of d_i, rank letters',C=r'\operatorname{rg}',H=r'\dim',reading=r'\operatorname{rg}',evidence='The leading short r is followed by a bowl and long descending g. Retracing supplies no separately recoverable earlier string.',readers={w:r'\operatorname{rg}' for w in 'ABC'})
q[9].update(C=r'\unsure{a un}',H='a un',reading=r'\unsure{a un}',diff_C=False,diff_H=True,confidence='low',unresolved=True,evidence='The low bowl and joined humps support a un, but a descending return crowds their boundary. The main crop does not separate those strokes sufficiently to remove the doubt.',decision='Retain the uncertainty with A and C; B removes it.')
q[23].update(reading=r'B_{\unsure{\alpha|i}}',diff_C=True,evidence='The low glyph has a loop and a rising right limb; no detached dot is evident. The main crop favours alpha while retaining i. The later B_i is independently dotted.',decision='Adopt reader C’s candidate order alpha|i; A and B retain i|alpha.')
q[25].update(evidence='Two principal dark horizontal groups occur between the clear commas, joined by a faint trace. There is no third dark group. The rendering retains the two principal marks and records the connecting trace here.',decision='Adopt the two-mark reading of all three readers; the faint connection remains documented.')
q[28].update(reading=r'e_{i_2,\unsure{2|1}}',confidence='low',unresolved=True,evidence='The index has a peaked upper hook, descending right segment and turned lower foot. These favour 2 in the main crop, while retracing still allows 1.',decision='Retain 2|1 as in C; A leads with 1 and B resolves the index to 2.')
q[31].update(confidence='low',readers={'A':r'e_{i_n,1}','B':r'e_{i_n,\unsure{t|1}}','C':r'e_{i_n,1}'},evidence='The low glyph has an upright and a short bar at mid-height, supporting t; its retraced outline also permits 1. The main crop preserves this local ambiguity.',decision='Adopt B’s t|1 doubt after direct root inspection; the expected basis pattern is not used to replace it.')
q[36].update(C=r'\inserted{donc définit \unsure{=|même} él. de $\omega_E$}',H=r'\uncertain{donc définit le même} él. de $\omega_E$',reading=r'\inserted{donc définit $=$ él. de $\omega_E$}',evidence='Two separated parallel horizontal bars directly follow définit. The following él. and omega_E are separate. The insertion leader attaches the phrase after the dimension parenthesis.',decision='All readers and the main crop read the visible equals sign; punctuation is recorded in the next locus.')
q[37].update(C=r'$\omega_E$. Si on',H=r'$\omega_E$ ; si on',reading=r'$\omega_E$. Si on',H_marked=False,evidence='A detached terminal point follows omega_E in the insertion. The next baseline S is a tall capital, and the guide enters immediately before Si. This locus records the point and capitalization without duplicating the preceding word/sign decision.',readers={w:r'$\omega_E$. Si on' for w in 'ABC'})
q[41]['readers']={w:r'par une $\sigma^+$' for w in 'ABC'}
q[42]['evidence']='The final det has no detached accent above the e. The crop includes the complete lower sheet edge.'
q[33]['evidence']='The first Gl argument has two separate left uprights in R, visible in the root crop. The d_i is heavily retraced, with no independently recoverable underlying letter.'
q[34]['evidence']='The second Gl argument independently has two separate left uprights in R. Its d, closing parenthesis and raised plus remain clear.'

def extra(location,C,H,reading,evidence,crop,readers,diff_C=False,diff_H=False,kind='other',confidence='high'):
    x={'id':f'S027-{len(loci)+1:02}','location':location,'C':C,'H':H,'reading':reading,'diff_C':diff_C,'diff_H':diff_H,'kind':kind,'H_marked':False,'confidence':confidence,'evidence':evidence,'crop':'scan027/'+crop,'readers':readers,'unresolved':False,'decision':'Explicit root adjudication on the cited existing crop.'}
    loci.append(x)

extra('definition of d_i, real-number subscript',r'\mathbb R',r'\mathbf R',r'\mathbb R','Two distinct left uprights are visible in the rank subscript. This alphabet decision is separate from the rg letters.','B/03_rank_and_soit.png',{w:r'\mathbb R' for w in 'ABC'},diff_H=True,kind='misread symbol or index')
extra('long basis row, first terminal d subscript; prior C query','d_1','d_1','d_1','One low digit follows d; the nested i of the final term is absent here. The written d_1 is retained.','A/11_basis_left.png',{w:'d_1' for w in 'ABC'})
extra('long basis row, second terminal d subscript; prior C query','d_2','d_2','d_2','One low digit follows d in the second endpoint. The root retains d_2 without adding an i.','A/12_basis_right.png',{w:'d_2' for w in 'ABC'})
extra('enumerations and final block index; prior C query',r'i_{n^-}; j_{n^+}; i_n; d_{i_n}',r'i_{n^-}; j_{n^+}; i_n; d_{i_n}',r'i_{n^-}; j_{n^+}; i_n; d_{i_n}','The short signs are visible above n in the two enumerations. The final displayed block has unqualified i_n and the terminal d has nested i_n. The last block’s other doubtful index is recorded separately.','A/08_enumeration.png; A/09_inserted_j_et_forall_b.png; A/12_basis_right.png',{w:r'i_{n^-}; j_{n^+}; i_n; d_{i_n}' for w in 'ABC'})
extra('NB diagram, physical placement of target label','numérot(I−) on the source baseline','numérot(I−) on the source baseline','numérot(I−) below the horizontal arrow','The horizontal arrow has épi above it; the target expression is written below that arrow, beginning under its rightward span. The consolidated tikz-cd uses a lower row for that label and retains the horizontal arrow.','A/07_nb.png',{w:'target on the source baseline in the returned diagram' for w in 'ABC'},diff_C=True,diff_H=True,kind='drawing or diagram')

alternatives={3:('Soit','Soient'),9:('a un','joined strokes unresolved'),13:('un','word and intention of crossing unresolved'),23:(r'\alpha','i'),26:('2',','),28:('2','1'),31:('t','1'),35:(')','crossed curved glyph unresolved'),39:(r'(-1)^{i_\alpha i_{\alpha+1}}',r'(-1)^{i_\alpha+i_{\alpha+1}}')}
doubts=[{'location':q[n]['location'],'reading':a,'alternatives':b,'confidence':q[n]['confidence'],'reason':q[n]['evidence']} for n,(a,b) in alternatives.items()]
notes=(ROOT/'decisions/scan027_notes.md').read_text().replace('the first index of the second block,','the first index of the second block, the t|1 character in the final block,')
checks=[{'statement_id':f'N027.{n}','date':'2026-11-20','who':'GPT-6 Astra Pro; effort not exposed; root/scan027','type':kind,'outcome':outcome} for n,kind,outcome in [
 (1,'carried as background without fault found','Source statements reported; no independent proof of the complete orientation formula or coherence.'),
 (3,'targeted proof check','Explicit adjacent-block permutation: rs inversions; determinant (-1)^(rs); odd-odd exchange -1, even-even exchange +1; products give the page’s local sign statements. The cancelled exponent is not inferred.'),
 (4,'targeted proof check','Restriction r of total orders has the explicit section s that places the I− sequence before the supplied I+ sequence; r composed with s is the identity entrywise.')]]
abbr={'ens':'ensemble','dim':'dimension','rg':'rang','isom':'isomorphisme','mb':'membre','NB':'nota bene','num.':'numérotation','numérot':'numérotations','épi':'épimorphisme','él.':'élément','dét':'déterminant','det':'déterminant','sgn':'signature'}
rec={'scan':27,'loci':loci,'inventory':raw['C']['inventory'],'doubts':doubts,'notes':notes,'check_events':checks,'abbreviations':[{'abbr':a,'expansion':e,'scans':[27]} for a,e in abbr.items()], 'consequential':[
 'The rank operator reads rg; H prints dim. All three real-number letters have doubled left uprights.',
 'The inserted conclusion reads “donc définit = él. de ω_E.”; its two-rule sign is preserved.',
 'The extra hook after the first basis index remains 2/comma, the second-block index remains 2|1, and the final-block character is newly marked t|1. No j-indexed terms are supplied.',
 'The first B subscript remains α|i. The deleted determinant power is partially readable but its exponent alternatives remain open.',
 'The marginal rightward arrow retains its épi label and the target expression’s lower physical position.'
]}
(ROOT/'decisions/scan027.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')

page=(ROOT/'readers/scan027/B/page.tex').read_text()
page=page.replace(r'\unsure{Soient|Soit}',r'\unsure{Soit|Soient}',1)
page=page.replace('On a un isom canonique',r'On \unsure{a un} isom canonique')
page=page.replace(r'B_{\unsure{i|\alpha}}',r'B_{\unsure{\alpha|i}}',1)
page=page.replace(r'e_{i_2,2}',r'e_{i_2,\unsure{2|1}}',1)
page=page.replace(r'\begin{tikzcd}[ampersand replacement=\&,column sep=small]',r'\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=-.3em]',1)
page=page.replace(r'\operatorname{numérot}(I)\arrow[r,"\text{épi}"] \& \operatorname{numérot}(I^{-})',r'\operatorname{numérot}(I)\arrow[r,"\text{épi}"] \& \phantom{\operatorname{numérot}(I^{-})} \\'+'\n'+r'\& \operatorname{numérot}(I^{-})',1)
(ROOT/'pages/J75-04_75_scan027.tex').write_text(page)
print(json.dumps({'loci':len(loci),'doubts':len(doubts),'inventory':len(rec['inventory'])}))
