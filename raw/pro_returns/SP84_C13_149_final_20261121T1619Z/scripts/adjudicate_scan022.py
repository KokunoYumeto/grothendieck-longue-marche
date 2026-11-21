"""Single-use root adjudication after personal inspection of every differing box."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1];ch={}
first={x['box']:x['reading'] for x in csv.DictReader((R/'second/149_scan022_first.tsv').open(),delimiter='\t')}
def c(k,e,final=None,crop=None):
 ch[k]={'personally_inspected':True,'selection':'first' if final is None else 'custom','evidence':e,'changed':'no' if final is None else 'yes'}
 if final is not None:ch[k]['final']=final
 if crop:ch[k]['crop']=crop
c('b02','Both signs have long legs and roofs, unlike the short pi forms in the final paragraph. Q has an independent inner stroke. The connector starts freely, without a perpendicular bar; its right end has only a short down-hook, not a separable two-arm head. Retain the complete-formula shaft/arrow uncertainty.')
c('b03','The noun has c, a, crossed tall t, the dotted i and a separate terminal down-curve consistent with plural s. Retain catégories and both des. The initial stroke of the short form has an upright and short oblique foot, but no securely separate cross-stroke, permitting t.f. or v.f.; do not repair the awkward syntax.',r'des catégories des \unsure{t.f.|v.f.} de')
parenthesis=r"(bien que pr la \unsure{démon.|démonstr.} \unsure{faut|faite|facile} une \unsure{voie} arithmétique pure)"
upper=r"\margin{En fait, ce théorème n'est pas spécial à $\mathbb Q$ --- il marcherait sur un corps de base quelconque --- et en fait la dém. montre bien que c'est en fait un énoncé de nature géométrique non arithmétique "+parenthesis+'}'
c('b04','The same box was viewed unrotated and at -45 and -60 degrees. After quelconque there is a short dash, then an e and crossed t, and the low en run; the next line begins with the long f-descender and dotted i of fait, followed by la. There is no car or separate zero. The central abbreviated word is dém. In the parenthesis the initial tall b with belly, dotted i and en, followed by q-descender and ue, read bien que, not j\'énonce. The next short p-descender/r pair is pr, without ou or a separate rendre. The following abbreviation and f-initial word remain compressed. The next line has a low u/n/e run followed by a separate v/o/i/e-like run, retained tentatively as voie. The final arithmétique has a q-descender and -tique ending; pure has p/ure and no tall t. The note has both parentheses and no terminal stop. Rotation changes the alignment of this same source extent, not its content.',upper,'crops/149_scan022_second_b04_rot-60_fullview.png')
c('b06','The end of hom is followed by blank paper before de, with no separate point. The raised sur Pi_Q has a leader to the interval before isomorphes; Q has the inner stroke. Retain the stop-free short form and placement.')
triangle=first['b07'].replace(r'\Pi_{\mathbb Q} \&',r'\Pi_{\mathbb Q}, \&')
assert triangle!=first['b07']
c('b07','All three nodes have capital Pi roofs and long legs. The top source alone has K-prime; both horizontal arrows have two-arm heads. The p-prime diagonal has only a heavy return at its end, while the p diagonal has a V-shaped head. A separate descending comma appears below and to the right of the bottom Q. Add that comma; retain the objects, diagonal states and centered bottom node.',triangle)
c('b08','The article has a tall l loop, detached apostrophe and complete low e loop. Under the strike, the i dot, s, o and m survive, without an independent stop. The raised replacement begins with open c and a, has two angular r joins and an e with detached accent. It is carré, not comm followed by a raised t.')
c('b09','Below the strike are initial co, two short r joins, a following low run, a central p-descender, and later a tall d loop with an a/n run and final t hook. These support correspondant. Commutatif lacks the central descender, while compatible places it earlier and does not account for the later d.')
c('b10','Both horizontal links have a wavy upper stroke and a straight lower bar, with blunt ends and no two-arm head. The upper p(alpha) label is separate. The left vertical has a head and the right only an end hook. The top-right argument is plain eta, without bar or prime; the other three have both. Retain the complete square without imposing agreement among its arguments.')
c('b12','The q-descender and i-like dot survive, but the crossing leaves qui ne versus qu\'on unresolved, and also the middle of peut. The separate lower baseline de K-prime and comma remain visible in the box context and the lower half; their omission from the second target reading is not absence from the leaf.')
ins=first['b13'].replace('$f,g$',r"$\unsure{f|f'},g$").replace(r'\unsure{\bar K_\varepsilon|\bar K}',r'\unsure{\bar K_\varepsilon|\bar K_f|\bar K}')
c('b13','The initial donnant, clipped by this second box, is present in first crop c13 and the lower half. Beside f is a raised tick as well as the lower separator; it may be a prime. The first K has a bar and a small lower-right curled stroke allowing epsilon, f, or a return without subscript. The second K still has an uncertain tilde. At the end a looped d and low e give de, and the following angular letter has capital-K height locally. Retain de K and broaden only the two undecided decorations.',ins)
c('b14','The live que precedes the beginning of the cancellation. The strike crosses les deux hom d\'exten, whose t is tall, but no separate point follows hom. The right-edge continuation is visible in first crop c14 and the lower half; no second que or extra word is supplied.')
cancel=r'\deleted{bien que\unsure{,|.}}'
longins=r"\inserted{l'on peut trouver un isomorphisme entre celles-ci (permettant donc d'identifier $\mathcal E_{\bar K/K}$ et $\mathcal E_{\widetilde K/K}$),} "+cancel+r'\inserted{de telle façon que les deux hom}'
c('b15','The full lower half and first crop c15 supplement the clipped right edge of this box: the first line ends celles-ci, not elles. The next line has the looped d and onc of donc, then d\'identifier. Between the two two-lobed open E forms is et, not à; both denominator letters have the angular construction and local height of capital K. The separate cancellation bien que lies between this parenthetical line and the following de telle façon line. Preserve that physical/textual order by splitting the long insertion around the cancellation; the lower added line still continues the replacement. The final hom has no separate stop.',longins)
mid=r"\margin{induisant ``l'identité'' sur les clôtures alg. \unsure{\deleted{$\overline{\mathbb Q}$}|$\overline{\mathbb Q}$} et $\widetilde{\mathbb Q}$ de $\mathbb Q$ dans $\bar K$ et $\widetilde K$, identifiées à celle dans $\bar K'$}"
c('b16','The opening i, flattened n, looped d and u/i/s/a/n/t form induisant; the low n stroke is not a hyphen. The quotation marks are paired ticks. After alg. the first crossed cluster has an oval Q and overhead stroke; the lower diagonal crossings do not securely settle whether the symbol was cancelled. It is followed by a distinct et and a second Q with a wavy tilde, then de Q dans. This is not a cancelled two-letter et/de followed by a lone barred Q. The next line has barred K, et, tilde K and comma. At the bottom the accented à and singular c/e/two l/e run give à celle, not entre elles; the final bar stops over K before the prime. Preserve the uncertainty of cancellation on the first Q only.',mid,'crops/149_scan022_second_b16_rot-30_fullview.png')
display=r"$f^*,g^*:\mathcal E_{\bar K'/K'}\substack{\longrightarrow\\\unsure{-|\longrightarrow}}\mathcal E_{\bar K/K}$"
c('b17','Both E forms have two open lobes, unlike a closed G body. The source numerator bar ends over K before its prime; both source-index K letters are primed. The upper arrow has a separable head. The lower shaft has only a short down-return, without its upper branch: localize the existing doubt to that lower head, retaining the full formula and the certain upper arrow.',display)
c('b18','Sont has the short s/o/n run and tall crossed t; there is no internal i/e. The next word has an e loop, g-descender and a/u/x, followed by a separate comma. No independent accent stroke over the e is secure amid the nearby leader, so retain an accented/unaccented alternative for that word.',r'sont \unsure{égaux|egaux},')
crossed=r"\deleted{Il \unsure{s'agit|faut} en \unsure{conclure|conclusion}} \inserted{\deleted{\unsure{C'est} \unsure{sans} doute plus}}"
c('b19','The lower and raised cancelled runs remain distinct. In the lower run a long descender and compressed joins permit s\'agit or faut under the strike; after en, the low c/o/n/c/l/u/r/e-like ending favors conclure, but the overlap does not eliminate conclusion. The raised C\'est/sans/doute/plus line is present even though omitted in the independent target reading. Doute and plus are clear; the earlier two words remain tentative. Retain both cancelled layers and broaden the two lower alternatives.',crossed)
c('b20','A marginal leader obscures the beginning, but the tall closed b loop, separate i dot and low en account for bien. Clair and alors do not account for that loop and dot. Retain tentative Ou bien without resolving its crossed opening.')
c('b21','The Q has a straight overhead stroke with an initial hook, not a wave, and its separate inner stroke. Fixée has the long f-descender and accent; independent commas follow fixée and the final Q. Retain the first reading.')
bottom=r"\margin{On doit se ramener au cas $k=k'$ --- c'est immédiat en \deleted{\unsure{faisant le chgt de base|faire d'extension}}\inserted{\unsure{pr une|prenant|par une}} extension finie de $\mathbb Q$}"
c('b23','The same source box was read at -35 and -50 degrees. The d-loop, dotted i and short t run support doit, followed by se. Ramener has no secure extra accent. The two k forms are smaller than the nearby barred capital K and the second has a looped return; retain k=k-prime. The short en has no s/a sequence supporting sans. Below it the cancellation preserves f/a/i and later tall strokes, but the joins and spacing do not settle the full phrase: retain the first abbreviated reading and the independent shorter faire d\'extension as alternatives. The replacement has a p-descender, short r-like stroke and a separated low u/n/e-like run; pr une is favored, while prenant and par une remain possible. The following extension, singular finie and unbarred Q are clear; no stop follows Q.',bottom,'crops/149_scan022_second_b23_rot-50_fullview.png')
c('b24','The thin marginal number has the curved top, oblique and long foot of2 followed by a narrow1. The location and pen weight distinguish it from an author heading. The numerical reading agrees; retain the margin wrapper.')
c('b25','Under the continuous horizontal strike, the initial tall b with low belly, independent i dot and low e/n run is followed by a separate q-descender and u/e. This reads bien que rather than disons. The small final mark is distinct, but its point versus comma shape is not secure. The lower half shows this cancellation before de telle façon, not after the completed long replacement.',cancel)
(R/'documentation/149_scan022_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan022.tex';s=p.read_text()
for k in ['b03','b04','b07','b13','b16','b17','b18','b23']:
 old=first[k]
 if k=='b17':old=old.strip('$');new=ch[k]['final'].strip('$')
 else:new=ch[k]['final']
 assert old in s,(k,old);s=s.replace(old,new)
old=first['b15'].replace(' '+r'\deleted{\unsure{disons}}','')+'\n'+r'\deleted{\unsure{disons}}'
assert old in s;s=s.replace(old,longins)
old=r"\deleted{Il \unsure{s'agit} en \unsure{conclusion}}";new=r"\deleted{Il \unsure{s'agit|faut} en \unsure{conclure|conclusion}}"
assert old in s;s=s.replace(old,new);p.write_text(s)
p=R/'reviews/149_scan022.json';r=json.loads(p.read_text());boxes={x['box']:x for x in r['audit_boxes']}
def update(cid,k,final=None,**kw):
 x=next(z for z in r['changes'] if z['id']==cid);b=boxes[k]
 x.update(final=ch[k].get('final',first[k]) if final is None else final,evidence=ch[k]['evidence'],crop=ch[k].get('crop',f'crops/149_scan022_second_{k}.png'),box=[b[t] for t in ['x0','y0','x1','y1']],**kw)
update('c03','b03',confidence='medium')
update('c06','b04',r'--- et en fait la dém.',place='Upper margin after quelconque',against_C=True,confidence='high',kind='misread word',error_category='Words')
update('c07','b04',r"fait la dém. montre bien que c'est en fait un énoncé de nature géométrique non arithmétique",against_C=True,confidence='high')
update('c08','b04',parenthesis,against_C=True,confidence='low')
update('c12','b07',confidence='high')
update('c17','b13',confidence='medium')
x=next(z for z in r['changes'] if z['id']=='c18');x['final']=x['final'].replace('$f,g$',r"$\unsure{f|f'},g$").replace(r'\unsure{\bar K_\varepsilon|\bar K}',r'\unsure{\bar K_\varepsilon|\bar K_f|\bar K}')
update('c21','b15',confidence='high',against_C=True)
update('c24','b25',place='Cancelled words before de telle façon',confidence='medium',against_C=True)
update('c27','b16',mid,confidence='medium',against_C=True)
update('c30','b17',display.strip('$'),confidence='medium')
update('c31','b18',confidence='medium')
update('c32','b19',confidence='low')
update('c38','b23',r"\deleted{\unsure{faisant le chgt de base|faire d'extension}}",confidence='low')
update('c39','b23',r'\inserted{\unsure{pr une|prenant|par une}} extension finie de $\mathbb Q$',against_C=True,confidence='low')
mark_updates={'M1026':('other','fait la','b04','high'),'M1027':('other','bien que','b04','high'),'M1028':('other','pr','b04','high'),'M1029':('other',r'une \unsure{voie}','b04','low'),'M1034':('undecided',r'\unsure{\bar K_\varepsilon|\bar K_f|\bar K}','b13','medium'),'M1037':('undecided',r'\unsure{pr une|prenant|par une}','b23','low')}
for x in r['decisions']:
 if x['id'] in mark_updates:
  dec,reading,k,conf=mark_updates[x['id']];b=boxes[k]
  x.update(decision=dec,reading=reading,evidence=ch[k]['evidence']+(' The parenthetical passage has been resegmented as a whole; the former marked rendre has no separate corresponding word.' if x['id']=='M1028' else ''),crop=ch[k].get('crop',f'crops/149_scan022_second_{k}.png'),box=[b[t] for t in ['x0','y0','x1','y1']],confidence=conf)
remove={'Upper margin before démon.','Upper margin after pour','Upper margin after facile','Cancelled word below the long replacement','Middle marginal cancellation','Extension-group display, parallel shafts','Lower run of the final cancellation','End of the lower cancelled run','Bottom marginal cancellation','Bottom marginal replacement'}
r['doubts']=[x for x in r['doubts'] if x['place'] not in remove]
for x in r['doubts']:
 if x['place']=='First field in the lower insertion':x.update(reading=r'\bar K_\varepsilon',alternatives=[r'\bar K_f',r'\bar K'],reason=ch['b13']['evidence'])
def doubt(place,reading,alts,k,confidence='low'):
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence=confidence,reason=ch[k]['evidence']))
doubt('Theorem, abbreviated field category','t.f.',['v.f.'],'b03','medium')
doubt('Upper margin, parenthetical abbreviation','démon.',['démonstr.'],'b04')
doubt('Upper margin, following f-initial word','faut',['faite','facile'],'b04')
doubt('Upper margin, after une','voie',[],'b04')
doubt('First lower insertion, map letter','f',["f'"],'b13','medium')
doubt('Cancelled bien que, final punctuation',',',['.'],'b25')
doubt('Middle margin, first barred Q cancellation',r'\deleted{$\overline{\mathbb Q}$}',[r'$\overline{\mathbb Q}$'],'b16')
doubt('Extension display, lower shaft head','-',[r'\longrightarrow'],'b17','medium')
doubt('After extension display, accent','égaux',['egaux'],'b18','medium')
doubt('Lower cancelled run, after Il',"s'agit",['faut'],'b19')
doubt('Lower cancelled run, after en','conclure',['conclusion'],'b19')
doubt('Bottom marginal cancellation','faisant le chgt de base',["faire d'extension"],'b23')
doubt('Bottom marginal replacement','pr une',['prenant','par une'],'b23')
for x in r['inventory']:
 e=x['element']
 if e=='e14':x['first_words_or_objects']=r"donnant via $\unsure{f|f'},g$ deux clôtures alg."
 if e=='e16':x['position']='replacement split around cancelled bien que; ending before the display'
 if e=='e17':x.update(position='between the parenthetical insertion and de telle façon',first_words_or_objects=cancel)
 if e=='e19':x.update(kind='text',position='first barred Q inside middle note; cancellation uncertain',first_words_or_objects=r'\unsure{\deleted{$\overline{\mathbb Q}$}|$\overline{\mathbb Q}$}')
 if e=='e20':x['first_words_or_objects']=display
 if e=='e21':x['first_words_or_objects']=ch['b18']['final']
 if e=='e22':x['first_words_or_objects']=r"Il \unsure{s'agit|faut} en \unsure{conclure|conclusion}"
 if e=='e27':x['first_words_or_objects']=r"\unsure{faisant le chgt de base|faire d'extension}"
 if e=='e28':x['first_words_or_objects']=r'\unsure{pr une|prenant|par une}'
byid={x['id']:x for x in r['changes']}
for x in r['diff_coverage']:
 if x.get('change_id') in byid:x['reason']=byid[x['change_id']]['evidence']
r['notes'][0]='The page states Théorème2: faithfulness of the displayed association from fields of finite type over Q to profinite groupoids over Pi_Q. The literal noun is catégories; the following short form retains t.f./v.f. uncertainty. Neither des nor the awkward syntax is repaired. This is transcription, not verification of the theorem.'
r['notes'][1]='The upper marginal note says the theorem works over an arbitrary base and calls its nature geometric rather than arithmetic. The independent audit overturns the earlier characteristic-zero reading: after quelconque the ink is a dash and et en, followed by fait la dém. on the next line; no zero is written there. The parenthesis begins bien que pr la. Its compressed abbreviation, f-initial word and voie remain uncertain. The final arithmétique pure is clear; these are reading judgments, not a check of the assertion.'
r['notes'][4]='The lower paragraph uses chosen algebraic closures and an isomorphism between them. The first inserted map letter may have a prime; the first decorated K has an epsilon/f-like lower-right curl or no subscript. In the middle margin, barred Q and tilde Q are both present; cancellation of the first is uncertain. The note retains singular à celle and barred K-prime. The cancellation bien que stands between the parenthetical replacement and its continuation de telle façon.'
r['notes'][5]='Four locally matching open two-lobed extension letters are retained as calligraphic E; the independent G alternative is excluded by their open forms. The upper display arrow is headed; only the lower shaft has a head/shaft doubt. The bar on the source K stops before its prime. No proof check is claimed.'
r['notes'][6]='After sont égaux/egaux, the lower cancelled run retains s\'agit/faut and conclure/conclusion. The raised cancelled replacement C\'est sans doute plus is separately preserved, with doubt on its earlier two words. The two layers and strike are clear, but exact pen chronology and all internal letters are not.'
r['notes'][7]='The final main paragraph uses outer profinite groups pi_K and Gamma operators. The bottom note retains On doit se ramener au cas k=k-prime. Its crossed phrase remains uncertain between the abbreviated first reading and the independent shorter alternative. The replacement is pr une/prenant/par une; extension finie and unbarred Q are clear. No abbreviation is expanded by fiat.'
r['notes'].append('Independent audit: all21 differing boxes were personally inspected, with the lower half and existing first crops supplying clipped continuation. Changes include the upper marginal assertion, a comma at the triangle bottom, the middle marginal closure symbols, cancelled bien que and its placement, and localized uncertainty. The two frozen readings and every token difference are retained separately. No OCR, external research or TeX compilation was used.')
r['hand'].append({'habit':'Strongly oblique compressed prose can merge word boundaries when viewed without alignment.','pages':[22],'consistency':'The upper note was checked in two upright views of the same extent; this is a local observation, not a universal letter substitution.','misread':'C and the first pass read de car0 where the ink has a dash and et en; both also missegmented the parenthetical beginning. The independent reading recovered bien que.'})
r['notation'].append({'written':r'\overline{\mathbb Q},\widetilde{\mathbb Q}','rendering':r'\overline{\mathbb Q},\widetilde{\mathbb Q}','meaning':'Two closures named in the middle marginal note.','evidence':'The first has a straight bar and uncertain cancellation, the second a wavy tilde; both have independent Q inner strokes.'})
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
