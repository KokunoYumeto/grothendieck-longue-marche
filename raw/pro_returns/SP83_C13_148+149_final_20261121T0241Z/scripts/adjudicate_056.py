from pathlib import Path
import csv,json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan056'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B02':'The old item has a crossbar and right upright, favouring 4, with a separate small raised circular mark before the old closing parenthesis. Four framing sides remain. Hatching prevents complete exclusion of the former A reading; 4-degree is now the leading doubtful reading. The cleaner parenthesized B is raised above it.',
'B03':'The long old word has the two f strokes, medial l/b-like ascenders and a low -issement ending, favouring affaiblissement rather than the shorter affinement/effilement. The following small et/ou stays uncertain under the strike. The old de is crossed separately; the raised sur has its own short underline.',
'B04':'The raised first line retains several groups ending in a separate de, favouring en termes de over one word autrement. The main d-un ending does not securely separate a final e. The middle raised phrase has an initial un, a y-like descender and crossed t in systeme, then a d ascender and low double-n run before de: un systeme donne de is preferred provisionally to composante connexe de. The contour phrase remains readable beneath the strike. Within the cancelled lower formula the old Sigma-like group is independently hatched; the first A subscript is overworked and admits zero/star. All remaining formula alternatives are retained rather than replaced by an illegible-word count.',
'B05':'The whole lower formula was viewed independently in this box. The old Sigma-like glyph before A is separately hatched within the general paragraph cancellation. The first A subscript is a small overworked closed/angular form, allowing zero or star. The open relation and the second index remain uncertain; the R-not-phi condition and the wavy mark over the following Sigma are retained.',
'B06':'The left d loop and low e/s run lie under a long cancellation. A separate small oval with a right downstroke survives near the far end of that same strike, provisionally a; it is not merely the return of the strike. This additional cancelled character is restored without asserting a certain reading.',
'B07':'The raised parenthesis and the main A-plus/ens/des/aretes line agree. The small preposition before Gamma has a low final joined form which can be u or e, so du remains first with de explicit as an alternative. The three dark strokes after Gamma have the b bowl, dotted i and descending p plus point of bip. The inequality has a clear greater-than and zero.',
'B09':'The separate raised qualification was also viewed here. Its initial du/de ending remains uncertain. Bip. has a bowl/stem, dotted short upright and final descender; the rest is telles que r(a)>0. The entire qualification is an insertion, not just the abbreviation.',
'B10':'The opening double ticks, effectively-marked words, closing ticks and following comma are visible. The long strike starts across et B and continues through l-ens des, whose lower joins remain recoverable. It does not cancel the quoted phrase. The punctuation and first deletion boundary are retained.',
'B11':'Above the Sigma body inside pi-zero there is a small curved extra stroke distinct from the main top bar; tilde-Sigma is now preferred, with plain Sigma retained because the return nearly joins the bar. The empty-set glyph has an oval and long descending stem and is kept as phi under the local notation convention. The other C, cap, R, inequality, B-plus and ens signs agree.',
'B12':'The low run after connexes ends in a pronounced downward hook. It can represent final s or the exit of e, so des/de remains unresolved. Both plus superscripts, the set-difference slash, R and the intersection sign are distinct; no parentheses are supplied.',
'B13':'The box clips upper parts of the final long word, but the surviving sur-marq-uage run agrees with the first reading and with its full first-pass crop. The interval abbreviation and point are visible. No underline is present. The blind uncertainty caused by the clipped boundary does not establish another word.',
'B15':'The underline lies below arete. The curved insertion leader leads to the parenthesized ouverte and the cancelled qui. The horizontal strike crosses the latter part of ouverte and all of qui, while the beginning of the parenthesis lies below it; complete withdrawal of ouverte is therefore still an uncertain alternative. The comma after Sigma is already present in the consolidated page, outside the original target reading of this box.',
'B17':'The old word has l, apostrophe, a low o, a p descender and a short final e-like group before live il y. There is no separate -ration continuation. The first abbreviated l-ope reading is retained as doubtful under the strike, not expanded to operation.',
'B18':'The punctuation after arbitraires is a long horizontal dash, not a small comma. The following word has the accented initial e and the low -anmoins ending of neanmoins, without the c/ss/r sequence required for necessaires. No comma follows that word.',
'B19':'The small soit and tuple occupy the interline directly below objet/de-category; no leader connects them to the later pres. They are anchored after objet in the linear transcription, with their actual below-line position recorded. The R has a dark upper return and a detached right speck; R_1 remains first, with hat/prime alternatives explicitly doubtful. The category alphabet is kept consistently with the surrounding pages. The last word has a tall b loop and i dot followed by en, supporting bien, and the main unique-isomorphism wording is continuous.',
'B20':'The tuple was viewed separately. X, Sigma, commas and subscript 1 are clear. The R upper loop is thick and angular, with an extra detached mark on its right, so plain R, hat-R and prime-R cannot all be distinguished securely. The entire small phrase remains an insertion.',
'B21':'After d-un the short word has a small e-like entry, low n run and hooked final s, rather than the longer sous sequence. The following marque has its q descender and accented ending. The prime after the first R, open inclusion and subscript 1 on the second R are visible despite clipped upper strokes.',
'B22':'The upper cancelled and lower underlined words have the accented e/t sequence of aretes, rather than autres. Under the strike after cercles a separate q-like descender favours the old marques; the long f descenders belong to the raised effectivement line, not a certain old efficaces. The small raised corr./comp group is crossed by the descender from the adjacent marques, so its ending is now doubtful. The final q-like descender and low ue-like continuation after Sigma remain visible and are retained as doubtful que.',
'B23':'The NB line has plural elles, followed by a compressed low opening, a tall t-like stroke, and an extended fine broken run ending in low joined strokes. Those surviving strokes do not justify shortening the entire first doubtful phrase to a certain sont or ne sont pas. The first alternatives remain unresolved. Eff. is visibly abbreviated with two f strokes and a point. The lower line has et then a short s/o/n/t-like run; the existing et sont, des intervalles and ouverts are retained. Both the canonical crop and a same-crop strip of the NB line were viewed.',
'B24':'Both digits have upper bars, descending left strokes and open lower bowls: 55. The mspage rather than margin wrapper changes no reading.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
repls={
'B02':[(r'\unsure{A)|4)}',r'\unsure{$4^\circ$)|A)}')],
'B04':[("d'une \\inserted",r"\unsure{d'une|d'un} \inserted"),(r'\unsure{composante connexe de}',r'\unsure{un système donné de|composante connexe de}'),(r'\unsure{\widetilde\Sigma_*}\;A_0^+',r'\deleted{\unsure{\widetilde\Sigma_*|\Sigma_*}}\;\unsure{A_0^+|A_*^+}')],
'B05':[(r'\unsure{\widetilde\Sigma_*}\;A_0^+',r'\deleted{\unsure{\widetilde\Sigma_*|\Sigma_*}}\;\unsure{A_0^+|A_*^+}')],
'B06':[(r'\deleted{\unsure{des}}',r'\deleted{\unsure{des} \unsure{a}}')],
'B07':[(r'\inserted{du $\Gamma$',r'\inserted{\unsure{du|de} $\Gamma$')],
'B09':[(r'\inserted{du $\Gamma$',r'\inserted{\unsure{du|de} $\Gamma$')],
'B11':[(r'\pi_0(\Sigma)',r'\pi_0(\unsure{\widetilde\Sigma|\Sigma})')],
'B19':[(r'R_1)',r'\unsure{R_1|\widehat R_1|R^{\prime}_1})')],
'B20':[(r'R_1)',r'\unsure{R_1|\widehat R_1|R^{\prime}_1})')],
'B22':[(r'\inserted{corr.}',r'\inserted{\unsure{corr.|comp.}}')]}
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,rs in repls.items():
 v=C[b]['first']
 for a,z in rs:
  assert a in v,(b,a);v=v.replace(a,z)
  if a in s:s=s.replace(a,z)
  else:assert z in s,(b,a)
 D[b].update(choice='reading',reading=v)
# The insertion is below objet, rather than attached to the later pres/dash.
ins=r'\inserted{soit $(X,\Sigma,\unsure{R_1|\widehat R_1|R^{\prime}_1})$}'
assert s.count(ins)==1
s=s.replace('un objet de','un objet '+ins+' de').replace('près '+ins+' ---','près ---')
v=D['B19']['reading'];v=v.replace('un objet de','un objet '+ins+' de').replace('près '+ins+' ---','près ---');D['B19']['reading']=v
pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
def update(n,b,**kw):
 x=next(x for x in r['changes'] if x['id']==f'{p}-{n:02d}')
 x.update(evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b],**kw)
update(1,'B02',final=D['B02']['reading'],diff_h=True)
update(5,'B04',final=r"\deleted{\unsure{d'une|d'un} \inserted{\unsure{un système donné de|composante connexe de}}}",kind='misread word',error_kind='Struck text')
formula=r'$\deleted{\unsure{\widetilde\Sigma_*|\Sigma_*}}\;\unsure{A_0^+|A_*^+}\unsure{\subset|\in}\unsure{A_0|A_*}$'
update(10,'B05',final=formula)
update(12,'B06',final=r'\deleted{\unsure{des} \unsure{a}}',diff_c=True)
update(16,'B09',final=D['B09']['reading'],confidence='medium')
update(29,'B19',final=r'un objet '+ins+r' de $S\mathcal TD^+$, défini à isom unique près --- muni bien entendu',diff_c=True,confidence='medium')
update(32,'B22',final=r'\inserted{\unsure{corr.|comp.}}',confidence='low')
r['changes'].append(dict(id=p+'-37',place='Live component formula inside pi-zero',c=r'\pi_0(\Sigma)',h=r'\pi_0(\Sigma)',final=r'\pi_0(\unsure{\widetilde\Sigma|\Sigma})',diff_c=True,diff_h=True,kind='misread symbol or index',error_kind='Symbols and indices',evidence=E['B11'],crop=f'crops/{p}_second_B11.png',box=boxes['B11'],confidence='medium',marked_in_h=False,consequential=True))
for x in r['doubts']:
 if x['place']=='Boxed old item under (B)':x.update(reading=r'\unsure{$4^\circ$)|A)}',alternatives='4 with raised degree and closing parenthesis; A)',reason=E['B02'])
 if x['place']=='Raised phrase within cancelled opening':x.update(reading=r'\inserted{\unsure{un système donné de|composante connexe de}}',alternatives='un système donné de; composante connexe de',reason=E['B04'])
 if x['place']=='Overwritten symbol after Soit':x.update(reading=r'$\deleted{\unsure{\widetilde\Sigma_*|\Sigma_*}}$',reason=E['B05'])
 if x['place']=='Entire cancelled A formula':x.update(reading=formula,alternatives='First and second indices zero/star; subset/membership; old Sigma tilde/plain',reason=E['B05'])
 if x['place']=='Short cancelled word before Soit A+':x.update(reading=r'\deleted{\unsure{des} \unsure{a}}',alternatives='des; additional tentative a under same strike',reason=E['B06'])
for place,reading,alt,conf,b in [
 ('Cancelled d-un ending',r"\unsure{d'une|d'un}",'d’une; d’un','low','B04'),
 ('Raised preposition before Gamma',r'\unsure{du|de}','du; de','medium','B09'),
 ('Live component Sigma accent',r'\unsure{\widetilde\Sigma|\Sigma}','tilde-Sigma; plain Sigma','medium','B11'),
 ('Inserted tuple R decoration',r'\unsure{R_1|\widehat R_1|R^{\prime}_1}','R_1; hat-R_1; prime-R_1','medium','B20'),
 ('Small raised marginal abbreviation',r'\unsure{corr.|comp.}','corr.; comp.','low','B22')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alt,confidence=conf,reason=E[b]))
for x in r['inventory']:
 if x['element']=='E02':x['first_words_or_objects']=r'\unsure{$4^\circ$)|A)}'
 if x['element']=='E09':x['first_words_or_objects']='un système donné de / composante connexe de'
 if x['element']=='E10':x['first_words_or_objects']='des; additional tentative a'
 if x['element']=='E13':x['first_words_or_objects']='du/de Γ bip. telles que r(a)>0'
 if x['element']=='E29':x.update(position='Small interlinear phrase directly below objet/de-category',first_words_or_objects=ins)
 if x['element']=='E35':x['first_words_or_objects']='corr. / comp.'
i=next(i for i,x in enumerate(r['inventory']) if x['element']=='E09')+1
r['inventory'].insert(i,dict(element='E38',sheet_kind='text',hand='his hand',kind='deletion',position='Independently hatched symbol within generally cancelled lower formula',first_words_or_objects=r'\widetilde\Sigma_* / \Sigma_*',transcribed='yes'))
for x in r['notation']:
 if x['sign'].startswith('A_0^+'):
  x.update(sign=r'A_{0/*}^+\;\subset/\in\;A_0/A_*',meaning_or_form='Both low indices are overworked and admit zero/star; the relation is open c-shaped but may have a concealed middle stroke.',witness_errors='The blind audit leaves both indices uncertain and distinguishes the independently cancelled preceding Sigma-like symbol.')
r['notation'].append(dict(sign=r'\widetilde\Sigma / \Sigma',meaning_or_form='An additional curved stroke above Sigma inside the live pi-zero formula favours a tilde, but it nearly joins the top bar.',places='Live component formula in B11; compare the clear tilde in the cancelled opening.',universality='Local uncertainty retained; no blanket tilde is added to other Sigma symbols.',witness_errors='Both witnesses omit the possible live tilde.'))
r['notes'].append(dict(id=p+'-N-audit',text='The blind second TSV was frozen before comparison. Every unequal box was viewed. The old item now favours 4 with a raised degree. The cancelled middle insertion now provisionally reads un système donné de; the old Sigma has a separate cancellation and both A indices remain uncertain. A further tentative cancelled a is restored. The live pi-zero formula now retains tilde/plain Sigma uncertainty. The object tuple is recorded directly below objet, with its R decoration uncertain. No mathematical expectation was used to repair the ungrammatical live operation description or to settle the compressed NB phrase.'))
extra=[f'crops/{p}_second_detail_nbline.png',f'crops/{p}_second_detail_nbline2.png']
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json','additional_existing_crops_viewed':extra}
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
