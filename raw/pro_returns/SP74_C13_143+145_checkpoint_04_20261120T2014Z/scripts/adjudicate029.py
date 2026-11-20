from pathlib import Path
import json

R=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
p=R/'reviews/143_scan029_readerA.json';d=json.loads(p.read_text())
t=R/'reviews/143_scan029_readerA.tex';s=t.read_text()
assert len(d['changes'])==65
mapping={0:('title',[175,40,1495,175]),1:('des_entiers',[660,205,1040,285]),3:('surQ_guide',[1090,245,1450,365]),4:('relatives_guide',[450,355,735,470]),5:('munies_uple',[690,465,1640,550]),7:('munies_uple',[690,465,1640,550]),8:('sections',[280,540,1640,670]),9:('sections',[280,540,1640,670]),27:('exponent_statement',[275,1435,1660,1790]),28:('exponent_statement',[275,1435,1660,1790]),29:('exponent_statement',[275,1435,1660,1790]),30:('exponent_statement',[275,1435,1660,1790]),31:('exponent_statement',[275,1435,1660,1790]),39:('notons',[375,1815,1035,1920]),48:('compatibles',[650,2050,1215,2145]),62:('final_words',[365,2260,1660,2355]),63:('final_words',[365,2260,1660,2355]),64:('number28',[20,2280,100,2360])}
for i,(n,b) in mapping.items():d['changes'][i].update(crop=f'crops/143_scan029_main_{n}.png',box=b)
d['changes'][0].update(against_C=True,kind='drawing or diagram')
d['changes'][0]['ink']+=' The two separate physical underline rules are retained, rather than joining them across the title gap.'
s=s.replace(r'\unsure{notion proche = schémable}',r'notion proche = \unsure{schémable}')
d['changes'][11].update(final=r'notion proche = \unsure{schémable}',ink='The main crop of the left end separately resolves notion proche; the reader crop then shows the equals sign and a compressed schémable-like group whose interior remains insecure. The two crops cover different portions of the phrase.',supplemental_crop='crops/143_scan029_main_notion_proche.png',supplemental_box=[275,900,670,1005])
for r in d['decisions']:
    if r['id']=='M0716':r.update(reading=r'notion proche = \unsure{schémable}',ink='The left words notion proche are resolved by the main crop of the previously uncropped left end; the equals sign is clear in the reader crop, while the interior of schémable remains compressed.',supplemental_crop='crops/143_scan029_main_notion_proche.png',supplemental_box=[275,900,670,1005])
for r in d['remaining_doubts']:
    if r['place']=="Exception paragraph's final phrase":r.update(place="Exception paragraph's final word",reading=r'\unsure{schémable}',alternatives='schémable; uncertain interior letters',reason='The main crop resolves the separate left words notion proche. Only the central letters of the final long word remain insecure in the existing reader crop.')
d['certainty_resolutions'].append(dict(place='Exception phrase, resolved left part',C=r'\unsure{notion proche = schémable}',final=r'notion proche = \unsure{schémable}',ink='Separate left-end crop resolves notion proche; only the compressed final word remains unsure.'))
genus=d['changes'][22].copy();genus['exclusion_reason']='Only the order of existing alternatives and their preference changed; this is not a material text change.'
d.setdefault('excluded_certainty_only_changes',[]).append(genus)
d['certainty_resolutions'].append(dict(place='Genus preference only',C=r'\unsure{0|g}',final=r'\unsure{g|0}',ink=genus['ink']))
for i in [41,55]:
    d['changes'][i]['against_C']=False
    d['changes'][i]['ink']+=' Reordering the already present C alternatives is a certainty decision only; the material H difference also includes the basepoint placement.'
    d['certainty_resolutions'].append(dict(place=d['changes'][i]['place']+' (preference only)',C=r'\unsure{\xi|j}',final=r'\unsure{j|\xi}',ink='The alternatives remain the same; the hooked unlooped stem receives first preference without resolving the letter.'))
s=s.replace(r'aux $x_i$.',r'aux $x_i$\unsure{--|.}')
d['changes'][31].update(place='Exposant sentence, terminal mark and absent parenthesis',final=r'aux $x_i$\unsure{--|.}',against_C=True,kind='punctuation',confidence='medium',ink='A detached short horizontal terminal stroke follows x_i. It may be a dash or an elongated period; no series of dots or closing parenthesis is visible. The local ambiguity is retained.')
d['remaining_doubts'].append(dict(place='Exposant sentence terminal mark',reading=r'\unsure{--|.}',alternatives='dash or elongated period',confidence='medium',reason='The detached short horizontal stroke is longer than the nearby round points but could be a dragged terminal period.',crop='crops/143_scan029_main_exponent_statement.png',box=[275,1435,1660,1790]))
s=s.replace(r'\unsure{\mathfrak S_\nu}',r'\mathfrak S_\nu')
d['changes'][36].update(final=r'de $\mathfrak S_\nu$ sur le $\pi_1$',confidence='medium',ink='The large outer loop and inner return match both separately inspected S_nu graphs on scan028. The low nu and the following sur le are visible. The repeated graphic pattern and its local permutation role together support S_nu; mathematical expectation alone is not the basis.')
d['remaining_doubts']=[r for r in d['remaining_doubts'] if r['place']!="Diagonal margin's large indexed group graph"]
d['certainty_resolutions']=[r for r in d['certainty_resolutions'] if r['place']!='Diagonal S-like graph: confidence lowered']
for r in d['notation']:
    if r['form']==r'\unsure{\mathfrak S_\nu}':r.update(form=r'\mathfrak S_\nu',meaning='Indexed permutation-group graph in the diagonal query',evidence='Outer spiral and inner return agree with both S_nu occurrences on scan028; low nu is distinct. Root resolves the local alphabet doubt at medium confidence by this cross-page graphic comparison and the common role.')
d['notes'][0]['text']=d['notes'][0]['text'].replace("The phrase 'notion proche = schémable' remains a reading doubt.","In 'notion proche = schémable', only schémable remains a reading doubt after the main reader resolves the left words.")
d['notes'][2]['text']=d['notes'][2]['text'].replace('a large unresolved S-like indexed graph','a large S_nu graph resolved by comparison with both occurrences on scan028')

def guide(insert,base,offset,width):
    return '\\begin{tikzpicture}[baseline=(base.base)]\n'+f'\\node[anchor=base west,inner sep=0] (base) at (0,0) {{{base}}};\n'+f'\\node[anchor=base west,inner sep=0] at ({offset},.56) {{{insert}}};\n'+f'\\draw[line width=.3pt] (-.12,-.12) .. controls (-.28,.15) and (-.18,.29) .. (.06,.29) -- ({width},.34) .. controls ({width+.15},.34) and ({width+.18},.42) .. ({width+.12},.53);\n'+'\\end{tikzpicture}'
guides=[
 (r'\inserted{sur $\mathbf Q$} pour',r'\inserted{sur $\mathbf Q$}','pour',-.05,1.55,'sur Q before pour','crops/143_scan029_main_surQ_guide.png',[1090,245,1450,365]),
 (r'\inserted{relatives} lisses',r'\inserted{relatives}','lisses',-.05,1.7,'relatives before lisses','crops/143_scan029_main_relatives_guide.png',[450,355,735,470]),
 (r'\inserted{(sur $\overline{\mathbf Q}$)} de genre',r'\inserted{(sur $\overline{\mathbf Q}$)}','de genre',-.05,2.25,'sur barred Q before de genre','crops/143_scan029_A_explanation.png',[310,1170,1630,1515]),
 (r"\inserted{$\in M_{g,\nu}(\overline{\mathbf Q})$}. \deleted{On} L'exposant",r'\inserted{$\in M_{g,\nu}(\overline{\mathbf Q})$}',r". \deleted{On} L'exposant",-.45,2.6,'membership after xi, before On and L’exposant','crops/143_scan029_A_explanation.png',[310,1170,1630,1515])]
del d['changes'][22]
for old,ins,base,off,w,place,crop,box in guides:
    assert old in s,old
    s=s.replace(old,guide(ins,base,off,w),1)
    d['changes'].append(dict(place='Curved insertion guide: '+place,C='[insertion text; no drawn guide]',H='[no drawn guide]',final=guide(ins,base,off,w),against_C=True,against_H=True,kind='drawing or diagram',ink='A separate fine curved stroke descends beside the insertion point, bends under the raised addition and turns upward at the other end. It has no arrowhead. Its relation to the written baseline and addition is reproduced.',confidence='high',crop=crop,box=box,marked_in_H=False,consequential=False))
for target,place in [('E05','under sur Q, attachment immediately before pour'),('E06','under relatives, attachment immediately before lisses'),('E14','under (sur barred Q), attachment immediately before de genre'),('E15','under the membership insertion, after xi and before the canceled On')]:
    ix=next(i for i,r in enumerate(d['inventory']) if r['element']==target)
    d['inventory'].insert(ix+1,dict(sheet_kind='text',hand='his hand',element=target+'a',kind='drawing',position=place,first_words_or_objects='thin curved insertion guide without arrowhead',transcribed='yes'))
for i,r in enumerate(d['inventory'],1):r['element']=f'E{i:02}'
d['notes'].append(dict(id='143_scan029-N6',text='Limited integer check of the listed exceptions: with nonnegative integers g and nu, the inequality 2g-2+nu <= 0 gives nu <= 2 when g=0, nu=0 when g=1, and no solutions when g>=2. Thus its solution list is exactly the two groups of exceptions written here. This checks only that numerical list, not the assertions about an algebraic etendue, automorphisms or monodromy. It supplies no missing ink and does not resolve the separate g/0 genus reading.'))
d['check_events'].append(dict(statement_id='143_scan029-N6',who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; main reader',type='targeted proof check',outcome='Split the nonnegative integer inequality into g=0, g=1 and g>=2; the displayed exceptional list is exactly the resulting solution set. No geometric claim was proved.'))
d['notes'].append(dict(id='143_scan029-N7',text='Main adjudication preserves all four single continuation strokes and their individual comma patterns, the shortened brace, the canceled item above its equals sign, literal source grammar, and four visible insertion guides. Inner Pi/pi remains locally uncertain at all three occurrences; the two later basepoints remain j/xi. The terminal stroke after x_i is locally dash/period. The S_nu graph is resolved only after comparison with the two prior-page examples. Changes in preference among already listed alternatives are excluded from material C-change counts.'))
d['unresolved_for_main']=[dict(place=r['place'],reading=r['reading'],crop=r.get('crop'),box=r.get('box'),question=r['reason']) for r in d['remaining_doubts']]
d['main_adjudication']=dict(original_seen=True,existing_crops_seen=10,main_crops_seen=12,decision='All reported differences and open marks inspected. Four insertion guides added; terminal dash/period localized; notion proche resolved; S_nu resolved by cross-page comparison; certainty-only preference changes excluded.')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2));t.write_text(s)
(R/'reviews/143_scan029_main.md').write_text('''# Main-reader adjudication — 143_scan029

The original, all ten reader crops, and twelve main-reader crops were inspected. Every material difference and open locus has a crop or a documented original-page check; the left-end notion proche crop supplements a different portion from the reader's associated-clause crop. Munies is underlined; no ordonné or terminal fibre period is supplied. Both title underline rules and all four curved insertion guides are retained. The insertion membership expression belongs after xi, before the canceled On.

The first puncture list has commas on both sides of its single continuation stroke. The tuple and the next two lists have only the left comma. All three inner Pi/pi graphs remain uncertain independently. The second and third basepoint graphs remain j/xi; their reordered alternatives are not material C corrections. The changed preference g/0 is also excluded from material counts. Notion proche is resolved, while schémable remains unsure. S_nu agrees graphically with both prior-page examples and is accepted at medium confidence. The ending after x_i is retained as dash/period uncertainty.

The short brace starts inside the operator and ends at the opening set brace; its canceled annotation lies above equals. It is not extended to a conventional whole expression. Stricts alone has the underline; orientés and locale/lacets remain unresolved. The low versus full-height indices, separate bars, analytic superscripts and circles are retained as physically written. N6 records only a finite integer-case proof for the exception list, with no asserted proof of the geometric claims.
''')
