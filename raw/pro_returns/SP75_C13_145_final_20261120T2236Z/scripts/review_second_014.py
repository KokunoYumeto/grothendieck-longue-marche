from adjudication_io import E,read_rows,write_adjudication
import json
r=json.loads((E/'reader_reports/145_scan014_reviewed.json').read_text())
f={x['box']:x['reading'] for x in read_rows(E/'second/145_scan014_first.tsv')}
b={x['box']:[int(x[k]) for k in ['x0','y0','x1','y1']] for x in read_rows(E/'second/145_scan014_boxes.tsv')}
oldidx=r'\unsure{\varepsilon_\infty|\varepsilon_1}'
newidx=r'\unsure{\varepsilon_\infty|\varepsilon_0|\varepsilon_1}'
oldpow=r'\deleted{\unsure{2}}';newpow=r'\deleted{\unsure{2|3}}'
chain=r'''\[
\begin{array}{r@{}c@{}l}
\deleted{\rho={}}&\deleted{\sigma_0\sigma_1}&\deleted{{}=\sigma_1\sigma_\infty=\sigma_\infty\sigma_0}\\
&\Vert&\\
&\makebox[0pt][c]{$\deleted{\varepsilon_0\varepsilon_1^3\unsure{\varepsilon_\infty|\varepsilon_0|\varepsilon_1}}$}&
\end{array}
\]'''
c={
'B04':{'use_first':True,'adjudication':'Do not promote the isolated low spot after sigma1 to punctuation.','ink':'The small black point is below the writing line, between the subscript1 and the equality. It has no established punctuation position or multiplication function there. The three sigma definitions, all indices and square exponents are otherwise clear. The isolated spot is recorded here but not transcribed as a doubtful added period.'},
'B07':{'final':chain,'changed':True,'adjudication':'Align the live vertical connector and cancelled continuation under the first sigma product; add0 to the unresolved last index.','ink':'The two short parallel vertical strokes stand beneath sigma0sigma1, untouched by the cancellation, and the crossed epsilon product sits directly below them. The first transcription separated this into an independently centered display, losing the precise attachment. The final lower trace of the last epsilon is broad and filled: a compressed infinity or0 is possible, with the earlier1 retained as a less secure alternative. No subscript is supplied from the expected product.'},
'B08':{'use_first':True,'adjudication':'Math delimiter serialization only.','ink':'The live replacement is above the cancelled chain. Its sigma0sigma1, equality, l1 with separate raised minus and1, and rho are all distinct. The second reading agrees on every symbol and insertion state.'},
'B09':{'final':f['B09'].replace(oldpow,newpow),'changed':True,'adjudication':'Broaden the cancelled exponent to2/3; retain the surrounding factors and grouping.','ink':'The small exponent has a dark oblique crossing and surviving upper and lower bends. These allow3 as well as2. The epsilon bases and their lower1/0/infinity indices remain readable; the following epsilon1-squared and epsilon-infinity-squared lie above the grouping line labelled epsilon0-to-minus2. The broader formula need not be made wholly doubtful merely because this one old exponent is obscured.'},
'B10':{'use_first':True,'adjudication':'Retain the colon attached to the last row.','ink':'Two separate dark points stand at the right of the third cyclic expression, at that row’s height. Both readings transcribe a colon, but placing it outside the entire aligned environment would move it toward the block’s middle. All powers and indices were checked and agree.'},
'B11':{'use_first':True,'adjudication':'Retain the negative marginal statement and its left separator.','ink':'The first line ends with a low n/e course. The second begins s/e/m followed by the two tall b/l courses and the final e/n/t, then a separate p with descender and low a/s. In conséquences there is one clear q head with a long descender and the u/e/n/c/e/s continuation. There are not the additional j/g descenders of conjugaison or the d ascender of déduisent. The third line reads des autres. The continuous vertical rule remains visible at left. This supports ne semblent pas conséquences, independently of whether that assertion is mathematically correct.'},
'B12':{'final':f['B12'].replace('Multipliant','multipliant').replace(r'\deleted{dans}',r'\deleted{\unsure{dans|donc}}'),'changed':True,'adjudication':'Use the visible lowercase initial and retain uncertainty in the locally struck word.','ink':'The opening m consists of two low arches on the baseline; the later l/t ascenders rise well above it, so an editorial capital is not retained. The cancelled word has a readable d and terminal hooked trace, but the long strike obscures the middle; dans is preferred with donc possible. The live inverse-order wording, rho cubed, equality and1 are clear.'},
'B14':{'use_first':True,'adjudication':'Retain the uncertain abbreviated élément(s) proposal.','ink':'After d-apostrophe there is a small e-like opening and immediately a tall l, followed by compressed low courses and a raised terminal hook/sweep. The tall stroke comes too early to support a confident autres sequence a/u/t/r/e/s. The abbreviated élém with an uncertain raised ending is retained; neither the plural ending nor an expanded word is supplied.'}}
for x in r['changes']:
 if x['id']=='s014-08':x.update(final=x['final'].replace(oldidx,newidx),ink=c['B07']['ink'],crop='crops/second_145_scan014_B07.png',box=b['B07'])
 if x['id']=='s014-09':x.update(final=chain,ink=c['B07']['ink'],crop='crops/second_145_scan014_B07.png',box=b['B07'],error_category=[3,6,7])
 if x['id'] in ['s014-11','s014-12']:x.update(final=x['final'].replace(oldpow,newpow),ink=c['B09']['ink'],crop='crops/second_145_scan014_B09.png',box=b['B09'])
r['changes'].append({'id':'s014-18','place':'initial letter of paragraph beginning multipliant','C':'Multipliant','H':r'\uncertain{Multipliant}','final':'multipliant','ink':c['B12']['ink'],'confidence':'high','kind':'abbreviation expanded or spelling modernised','c_changed':True,'h_changed':True,'marked_in_H':'yes','crop':'crops/second_145_scan014_B12.png','box':b['B12'],'error_category':[2,8],'math_consequence':''})
for x in r['doubts']:
 if x['reading']==oldidx:x.update(reading=newidx,alternatives=[r'\varepsilon_\infty',r'\varepsilon_0',r'\varepsilon_1'],reason=c['B07']['ink'])
 if x['reading']==oldpow:x.update(reading=newpow,alternatives=['2','3'],reason=c['B09']['ink'])
r['doubts'].append({'place':'cancelled word after multipliant','reading':r'\deleted{\unsure{dans|donc}}','alternatives':['dans','donc'],'confidence':'low','reason':c['B12']['ink']})
for x in r['inventory']:
 x['first_words_or_objects']=x['first_words_or_objects'].replace(oldidx,newidx).replace(oldpow,newpow).replace('Multipliant','multipliant')
r['notes'].append('The blind audit retains the negative marginal sentence after checking its ascenders and descenders against the incompatible positive paraphrase. It refines the layout by attaching the uncancelled vertical connector and cancelled epsilon continuation specifically under sigma0sigma1. It also records lowercase multipliant, broadens the old exponent2/3 and the terminal cancelled epsilon index, and qualifies the struck dans/donc. The isolated low point between sigma1 and its equality is not established as punctuation. None of these paleographic decisions alters the conditional algebra checks recorded above.')
r['hand'].append('Blind audit: the low two-arch m in multipliant must not be capitalized automatically at a paragraph opening. The marginal negative ne and pas are separate readable words; a single long q descender in conséquences must not be expanded into the different descender sequence of conjugaison. The vertical equality below a cancelled chain attaches to its first product, not to the whole line’s center.')
edits=[{'old':f['B07'],'new':chain},{'old':oldpow,'new':newpow},{'old':r'Multipliant \deleted{dans}','new':r'multipliant \deleted{\unsure{dans|donc}}'}]
write_adjudication(14,'/root/reader_b',c,edits,report_replace={k:r[k] for k in ['changes','doubts','inventory','notes','hand']})
