from adjudication_io import E,read_rows,write_adjudication
import json
r=json.loads((E/'reader_reports/145_scan019_reviewed.json').read_text())
f={x['box']:x['reading'] for x in read_rows(E/'second/145_scan019_first.tsv')}
b={x['box']:[int(x[k]) for k in ['x0','y0','x1','y1']] for x in read_rows(E/'second/145_scan019_boxes.tsv')}
n=dict(f)
n['B01']=f['B01'].replace(r'\sigma_0l_{\unsure{1}}',r'\sigma_0l_{\unsure{1|0}}').replace(r'l_{\unsure{1}}^{\deleted{\unsure{-1}}}\sigma_1l_\infty',r'l_{\unsure{1|\infty}}^{\deleted{\unsure{-1}}}\sigma_{\unsure{1|\infty}}l_{\unsure{\infty|0}}').replace(r'l_{\unsure{0}}',r'l_{\unsure{0|\infty}}')
n['B03']=f['B03'].replace(r'l_{\unsure{1}}',r'l_{\unsure{1|0}}')
oldphrase=r'\deleted{\unsure{il faudrait}}';newphrase=r'\deleted{\unsure{il faudrait|il faut donc les}}'
oldword=r'\deleted{\unsure{ici}}';newword=r'\deleted{\unsure{ici|laisser}}'
n['B04']=f['B04'].replace(oldphrase,newphrase).replace(oldword,newword)
product=r'\unsure{produits|produit|quotient}'
n['B07']=f['B07'].replace('produits',product).replace('par des expressions en les $l_i$.','par des expressions')+'\nen les $l_i$.'
def bracket(term,label):
 return r'\underset{'+label+r'}{\begin{tikzpicture}[baseline=(term.base)]\node[inner sep=1pt] (term) {$'+term+r'$};\draw ([yshift=-1pt]term.south west) -- ++(0,-3pt) -| ([yshift=-1pt]term.south east);\end{tikzpicture}}'
br1=(r'\underbrace{\sigma_0l_1^2\sigma_0^{-1}}_{l_\infty^2}',bracket(r'\sigma_0l_1^2\sigma_0^{-1}',r'l_\infty^2'))
br2=(r'\underbrace{\sigma_0\sigma_1}_{\rho l_0}',bracket(r'\sigma_0\sigma_1',r'\rho l_0'))
n['B08']=f['B08'].replace(*br1).replace(*br2)
lastword=(r'\unsure{définition}',r'\unsure{définition|définit}')
n['B11']=f['B11'].replace('des gén.','des gén').replace(*lastword)
c={
'B01':{'final':n['B01'],'changed':True,'adjudication':'Retain the five cancelled inverse-looking exponents; qualify five overwritten live indices.','ink':'The first row’s last index has a dark upright over a closed lower trace, admitting1/0. In the second row the first l index and the sigma index each have a vertical foot over pale linked loops, admitting1/infinity; its last l index has two low joined loops but a retraced enclosing oval, admitting infinity/0. The third row’s last index has a dark closed body with doubled interior, admitting0/infinity. All five high inverse-looking groups have independent crossing strokes and remain cancelled tentative -1. The cyclic pattern is not used to determine any index.'},
'B02':{'use_first':True,'adjudication':'Retain the margin’s general covariance formula and three-case expansion.','ink':'The underline below NB, detached dot over the small rho in the general right-member index, separate i dot, and all three inverse exponents are visible. The abbreviation has only its medial point. The independent reading’s choice of a separate display for the header does not change these inscriptions.'},
'B03':{'final':n['B03'],'changed':True,'adjudication':'Broaden the overwritten post-brace index to1/0.','ink':'The last index before the first equality is heavily blackened: a vertical/foot-like component favours1, but an enclosed low curved remainder permits0. The central annotation has a true cusp-shaped underbrace, and the two attached calculation rows, inverse exponents and lowercase ok are clear.'},
'B04':{'final':n['B04'],'changed':True,'adjudication':'Retain the parentheses, Les, de tantôt, exclamation mark and live replacement; broaden two cancelled phrases.','ink':'The separate curved stroke left of NB and the large closing parenthesis on the next baseline are visible. Les has a tall opening L. The extra original-image crop of the earlier-reference words shows de, then two tall t-like strokes separated by a long low course, a detached mark over the small rounded o and a final tall t, supporting de tantôt rather than du début. The punctuation after it has an upper stroke and low point. Above the cancelled baseline, qu’il faudra is live and lacks a final t. The crossed baseline admits both il faudrait and il faut donc les: the far-right tall/low group is not securely assignable through the strike. The next crossed word has a tall loop, detached dot and a low connected course, leaving ici/laisser unresolved. Donc noter and the primed epsilon followed by three marks remain live.'},
'B06':{'use_first':True,'adjudication':'Retain the three rows and individually represented unfinished placeholders.','ink':'The left brace spans all three rows. The square exponents and indices are visible. Between rho and its first placeholder there is a crossed looped factor compatible with l-infinity but not resolved. Two points are visible inside the crowded parentheses, with an obscured additional mark still possible; the next placeholder has two points and the third a point plus short horizontal dash. The two later placeholders are not three-dot ellipses.'},
'B07':{'final':n['B07'],'changed':True,'adjudication':'Qualify produits/produit/quotient and place the crossed trial between the two prose baselines it separates.','ink':'Comme is a dark compact insertion. The next word begins with a low loop and descender compatible with p or q; its middle tall stroke supports the d of produit but does not completely exclude a compressed t sequence. The short continuation after the final tall t may be s or merely its exit. The singular/plural and quotient alternatives remain open. The struck short formula is physically below expressions and above en les l_i.; its sigma has a distinct low1. The prose continuation is therefore placed after that deleted display.'},
'B08':{'final':n['B08'],'changed':True,'adjudication':'Retain the readable current factors and replace the two cusp-shaped braces with flat brackets.','ink':'Both sigma indices show a dark current upright1 and foot over pale loops. The live rho and following l0 are distinguishable from underlying strokes; the low loops do not establish new rho subscripts. The two annotation rules have nearly flat courses and short rising ends, without the central cusp of the earlier square-calculation brace. Their labels l-infinity squared and rho l0 are below the appropriate factors. Two small literal TikZ brackets preserve those shapes using the supplied preamble, without adding a new macro.'},
'B09':{'use_first':True,'adjudication':'Retain the current factors; do not assign separate letters to earlier underlying traces.','ink':'Row2’s live index after rho has a dark straight1 and firm foot; row3’s corresponding current index has two joined low loops, supporting infinity. The raised2 in row3 is small but retains its curved head and lower foot. Extra pale circles near rho and a lower slashed trace under the last infinity are materially present, but do not isolate a separate earlier numeral or factor. That earlier-layer uncertainty is already documented. The extra crossed epsilon-like glyph in row1 remains qualified.'},
'B11':{'final':n['B11'],'changed':True,'adjudication':'Remove the supplied stop after final gén and retain two alternatives for the compressed last word.','ink':'The abbreviated gén ends in a connected terminal turn followed by blank paper before the epsilon list; no separate point is present. Avec relations de is visible. The last word has a tall f, a detached i dot and a compressed terminal course, compatible with définition or abbreviated définit, but its final letters are not individually separable. No terminal punctuation is supplied.'}}
for x in r['changes']:
 if x['id']=='s019-01':
  x['final']=n['B01'];x['ink']=c['B01']['ink'];x['crop']='crops/second_145_scan019_B01.png';x['box']=b['B01']
 if x['id']=='s019-08':x.update(final=x['final'].replace(oldphrase,newphrase),ink=c['B04']['ink'],confidence='low',crop='crops/second_145_scan019_B04.png',box=b['B04'])
 if x['id']=='s019-09':x.update(final=x['final'].replace(oldword,newword),ink=c['B04']['ink'],confidence='low',crop='crops/second_145_scan019_B04.png',box=b['B04'])
 if x['id']=='s019-13':x.update(final=r'\inserted{comme} '+product,ink=c['B07']['ink'],confidence='medium',crop='crops/second_145_scan019_B07.png',box=b['B07'])
 if x['id']=='s019-14':x.update(final=n['B07'],ink=c['B07']['ink'],c_changed=True,error_category=[1,3,6],crop='crops/second_145_scan019_B07.png',box=b['B07'])
 if x['id']=='s019-17':x['final']=x['final'].replace(*lastword)
r['changes'].extend([
 {'id':'s019-19','place':'long product calculation, two annotation brackets','C':br1[0]+' '+br2[0],'H':r'\underbrace{\sigma_0\,l_1^2\,\sigma_0^{-1}}_{l_\infty^2}\,\underbrace{\sigma_0\sigma_1}_{\rho\,l_0}','final':br1[1]+' '+br2[1],'ink':c['B08']['ink'],'confidence':'high','kind':'diagram or graphic sign','c_changed':True,'h_changed':True,'marked_in_H':'no','crop':'crops/second_145_scan019_B08.png','box':b['B08'],'error_category':[4,6],'math_consequence':'The labels retain their exact factor attachments; only the shape of the written annotation rules is changed.'},
 {'id':'s019-20','place':'final prose, abbreviation before epsilon list','C':'des gén.','H':'des gén.','final':'des gén','ink':c['B11']['ink'],'confidence':'high','kind':'text not on the page','c_changed':True,'h_changed':True,'marked_in_H':'no','crop':'crops/second_145_scan019_B11.png','box':b['B11'],'error_category':[8,9,10],'math_consequence':''}])
doubt_updates={
 '(8), row 1 final l subscript':(r'\unsure{1|0}',['1','0'],'B01'),
 '(8), row 2 first l subscript':(r'\unsure{1|\infty}',['1',r'\infty'],'B01'),
 '(8), row 3 final l subscript':(r'\unsure{0|\infty}',['0',r'\infty'],'B01'),
 'square verification, l immediately after underbrace':(r'\unsure{1|0}',['1','0'],'B03'),
 'NB paragraph, cancelled baseline phrase':(newphrase,['il faudrait','il faut donc les'],'B04'),
 'NB paragraph, cancelled lower-line word':(newword,['ici','laisser'],'B04'),
 'final word':(lastword[1],['définition','définit'],'B11')}
for x in r['doubts']:
 if x['place'] in doubt_updates:
  val,alts,bid=doubt_updates[x['place']];x.update(reading=val,alternatives=alts,reason=c[bid]['ink'])
for place,reading,alts,bid in [
 ('(8), row2 sigma subscript',r'\unsure{1|\infty}',['1',r'\infty'],'B01'),
 ('(8), row2 final l subscript',r'\unsure{\infty|0}',[r'\infty','0'],'B01'),
 ('instruction after comme',product,['produits','produit','quotient'],'B07')]:
 r['doubts'].append({'place':place,'reading':reading,'alternatives':alts,'confidence':'medium' if bid=='B07' else 'low','reason':c[bid]['ink']})
for x in r['decisions']:
 if x['id']=='M0833':x.update(reading=r'\unsure{1|0}',ink=c['B03']['ink'],crop='crops/second_145_scan019_B03.png',box=b['B03'])
 if x['id']=='M0838':x.update(reading=lastword[1],ink=c['B11']['ink'],crop='crops/second_145_scan019_B11.png',box=b['B11'])
for x in r['unlisted_decisions']:
 if x['id'] in ['U019-06','U019-07']:x.update(reading=newphrase if x['id']=='U019-06' else newword,ink=c['B04']['ink'],crop='crops/second_145_scan019_B04.png',box=b['B04'])
for x in r['inventory']:
 for bid in ['B01','B03','B04','B07','B08','B11']:
  x['first_words_or_objects']=x['first_words_or_objects'].replace(f[bid],n[bid])
 x['first_words_or_objects']=x['first_words_or_objects'].replace(oldphrase,newphrase).replace(oldword,newword)
 if x['element']=='I08':x['first_words_or_objects']=x['first_words_or_objects'].replace('produits',product);x['position']='instruction in three prose baselines, interrupted between expressions and en les by crossed trial I09'
 if x['element']=='I10':x['position']='long product calculation and its two flat bracket labels'
for x in r['diff_coverage']:
 if x['row']==28:x['explanation']='The raised qu’il faudra is live. The crossed baseline admits il faudrait / il faut donc les; the q descender of the insertion crosses it and is not assigned to the deleted phrase.'
 if x['row']==29:x['explanation']='The raised qu’il faudra is live. The next cancelled word remains ici / laisser, while donc noter and the primed epsilon remain outside the cancellation.'
 if x['row']==40:x['explanation']='Comme is inserted; the following word is now qualified produits / produit / quotient because its low opening loop and terminal turn do not securely establish the lexical sequence or plural.'
 if x['row'] in [41,42,43,44]:x['explanation']+=' The cancelled trial is physically between expressions and the continued en les l_i, which is now preserved in transcription placement.'
for x in r['abbreviations']:
 if x['form']=='gén.':x['place']='generators-and-relations introduction; final des gén lacks a stop'
r['abbreviations'].append({'form':'gén','expansion':'générateurs','place':'final des gén before epsilon list, no terminal stop'})
r['notes']=[x.replace('Three overwritten live subscripts have new local uncertainty','Five overwritten live subscripts have local uncertainty').replace('The earlier phrase il faudrait and word ici remain crossed and uncertain','The earlier phrase il faudrait / il faut donc les and word ici / laisser remain crossed and uncertain').replace('as products of rho by expressions in the l_i','using the uncertain word produits / produit / quotient before de rho par des expressions en les l_i').replace('with labels l-infinity squared and rho l0 beneath two braces','with labels l-infinity squared and rho l0 beneath two flat brackets').replace('followed by tentative définition','followed by tentative définition / définit').replace('No date is visible; all inscriptions appear to be in his hand.','No date is visible; the mathematical and prose inscriptions appear to be in his hand, while the isolated pagination hand remains indeterminate.') for x in r['notes']]
r['notes'].append('Blind audit: five overwritten indices in (8) and the post-brace index in the square calculation retain explicit alternatives. The free-word checks use the preferred cyclic indices as a stated conditional interpretation; they cannot select those readings from the ink. The readable current l factors in the later product formulas remain distinct from uncertain earlier-layer remnants. The cancelled trial is placed between expressions and en les l_i, matching its physical interline position. The two later annotation rules are flat brackets; the earlier square calculation retains its cusp-shaped brace. Final gén has no full stop, and the last word remains définition / définit. No new mathematical check event is claimed.')
r['hand'].append('Blind audit: overwritten lower indices can preserve both a dark current numeral and pale earlier loops. These layers must be separated case by case. A true cusp-shaped underbrace in the square computation contrasts with two flat brackets in the product computation. Terminal turns of abbreviated words do not establish a separate punctuation point.')
write_adjudication(19,'/root/reader_a',c,[{'old':f[bid],'new':n[bid]} for bid in ['B01','B03','B04','B07','B08','B11']],report_replace={k:r[k] for k in ['changes','doubts','decisions','unlisted_decisions','inventory','diff_coverage','abbreviations','notes','hand']})
