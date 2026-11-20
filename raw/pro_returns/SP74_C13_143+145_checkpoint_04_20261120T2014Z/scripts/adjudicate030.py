from pathlib import Path
import json
R=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
p=R/'reviews/143_scan030_readerB.json';d=json.loads(p.read_text())
t=R/'reviews/143_scan030_readerB.tex';s=t.read_text();assert len(d['changes'])==66
mapping={0:('isomorphism',[275,45,695,155]),2:('profini_guide',[235,145,1650,360]),3:('profini_guide',[235,145,1650,360]),6:('tag4',[225,510,335,600]),43:('claim_reference',[960,1040,1640,1330]),44:('caracterisation',[320,1330,1570,1580]),45:('caracterisation',[320,1330,1570,1580])}
for i,(n,b) in mapping.items():d['changes'][i].update(crop=f'crops/143_scan030_main_{n}.png',box=b)
d['changes'][1].update(supplemental_crop='crops/143_scan030_main_profini_guide.png',supplemental_box=[235,145,1650,360])
d['changes'][43]['ink']+=' The existing reader crop ends at aimerait; the main crop begins with the immediately following que, with no intervening word.'
old=r'\unsure{\tikz[baseline=-.5ex]{\node[rotate=90,inner sep=0pt] {$\simeq$};}|\wr}'
wave=r'\tikz[baseline=-.5ex]{\node[rotate=90,inner sep=0pt] {$\approx$};}'
assert old in s;s=s.replace(old,wave)
d['changes'][11].update(final=wave,H=r'\wr [and the note reports a question mark]',confidence='medium',consequential=False,ink='Two separate wavy vertical strokes are visible, without a detached question-mark dot. The rotated approximate-sign shape reproduces both strokes and their orientation, consistently with the independently inspected scan026 example. The mathematical intention of the symbol is not separately asserted.')
d['excluded_duplicate_rows']=[dict(d['changes'][12],exclusion_reason='The alleged question mark and the paired-wave shape are one physical locus, recorded together in the preceding row.')]
d['remaining_doubts']=[r for r in d['remaining_doubts'] if r['place']!='Diagram left vertical-map label']
for n in d['notation']:
    if n['form'].startswith(r'\tikz'):n.update(form=wave,meaning='Physical paired-wave shape beside the vertical map',evidence='Two curved vertical strokes are represented by a rotated approximate sign, as on scan026; no detached author question-mark dot is visible. The encoding records shape without proving a particular mathematical interpretation.')
old=r'\mathcal T_{g,\nu}^{\wedge}\to$'+'\n'+r'\unsure{est invariant|injective}'
new=r'\mathcal T_{g,\nu}^{\wedge}\unsure{\to|\text{est}}$'+'\n'+r'\unsure{invariant|injective}'
assert old in s;s=s.replace(old,new)
d['changes'][24]['final']=r'\mathcal T_{g,\nu}^{\wedge}'
d['changes'][25].update(final=r'\unsure{\to|\text{est}}',confidence='low',ink='The short horizontal graph after T ends in a raised pointed or folded terminal. It may be a headed shaft or the author’s severely reduced est. There is no independent est before the lower predicate, so no second copy is supplied.')
d['changes'][26].update(final=r'\unsure{invariant|injective} dans',ink='The lower line has an invariant-like run followed by the clearly separate dans; its initial letters overlap the margin. The injective alternative remains local. No independent est is visible before this word; the upper graph after T separately carries arrow/est alternatives.')
for r in d['remaining_doubts']:
    if r['place']=='Invariance predicate':r.update(reading=r'\unsure{invariant|injective}',alternatives='invariant / injective',reason='The lower word is crowded, with invariant preferred; no separate est is copied into it. The upper short graph has its own arrow/est doubt. Existing invariance crop.')
d['remaining_doubts'].append(dict(place='Graph after completed T in invariance line',reading=r'\unsure{\to|\text{est}}',alternatives='rightward arrow / severely reduced est',confidence='low',reason='The raised folded terminal can be a small arrowhead or the end of the reduced word. No independent est is present before the lower predicate.',crop='crops/143_scan030_readerB_invariance.png',box=[333,747,1493,1047]))
d['notes'][1]['text']=d['notes'][1]['text'].replace('The paired vertical left-map label, its cancelled right label, the last vertical tip and the clipped continuation after Out remain local doubts.','The paired vertical label is rendered as the two wavy strokes actually visible, consistent with scan026; its mathematical intention is not separately settled. Its cancelled right label, the last vertical tip and the clipped continuation after Out remain local doubts.')
d['notes'][2]['text']='The crowded line below the diagram appears to begin admettons. The short graph after completed T is retained as arrow / severely reduced est, and the lower word as invariant / injective. Neither reader can locate an independent second est before that lower word. The operator argument contains the author’s literal question mark. This local treatment preserves the unclear wording without supplying grammatical completion.'
for e in d['check_events']:
    if e['statement_id']=='143_scan030-N3':e['outcome']='Recorded the local arrow/est and invariant/injective doubts; the absence of an independent lower est was checked with the first reader, without using mathematical expectation to supply a word.'
for i in d['inventory']:
    if i['element']=='E09':i['first_words_or_objects']='admettons que ... arrow/est ... invariant/injective dans ...'
    if i['element']=='E26':i.update(hand='unnamed pencil hand',kind='margin note')

guide=r'''\begin{tikzpicture}[baseline=(base.base)]
\node[anchor=base west,inner sep=0] (base) at (0,0) {suites exactes};
\node[anchor=base west,inner sep=0] at (.02,.58) {\inserted{hom de}};
\draw[line width=.3pt] (-.20,-.08) .. controls (-.12,.27) and (.02,.32) .. (.30,.32) .. controls (.82,.26) and (1.27,.38) .. (1.75,.49);
\end{tikzpicture}'''
assert r'\inserted{hom de} suites exactes' in s;s=s.replace(r'\inserted{hom de} suites exactes',guide)
cancel=r'\deleted{\unsure{(cas} \illegible{1} \unsure{abélien} $*$ \unsure{est} \illegible{1}}'
frame=r'''\figure{\begin{tikzpicture}
\node[anchor=north west,align=left,text width=3.4cm,font=\footnotesize,inner sep=0] at (0,.85) {'''+cancel+r'''};
\draw[line width=.35pt] (-.13,-.75)--(-.13,.98)--(3.45,.91)--(3.48,-.68)--cycle;
\draw[line width=.45pt] (-.08,.70)--(.22,-.79)--(.47,.86)--(.72,-.78)--(.97,.91)--(1.20,-.73)--(1.43,.90)--(1.68,-.69)--(1.91,.91)--(2.15,-.70)--(2.39,.88)--(2.62,-.70)--(2.88,.85)--(3.16,-.63)--(3.42,.83);
\draw[line width=.3pt] (.06,-.69)--(.82,.98) (1.01,-.79)--(1.76,.92) (2.12,-.74)--(2.85,.91) (-.10,.16)--(3.37,.19);
\end{tikzpicture}}'''
assert cancel in s;s=s.replace(cancel,frame)
del d['changes'][12]
d['changes'].append(dict(place='Opening hom de insertion, curved attachment',C='[inserted hom de; no drawn guide]',H='[no guide]',final=r'\draw[line width=.3pt] (-.20,-.08)',against_C=True,against_H=True,kind='drawing or diagram',ink='A fine guide descends immediately before suites, bends right and passes below the added hom de. It has no arrowhead. The baseline and raised text are placed with this visible curve.',confidence='high',crop='crops/143_scan030_main_profini_guide.png',box=[235,145,1650,360],marked_in_H=False,consequential=False))
d['changes'].append(dict(place='Exception margin, cancellation frame and zigzag strokes',C='[deleted text without the frame or repeated zigzag]',H='un bloc ... encadré, est raturé en zigzag',final=r'\draw[line width=.35pt] (-.13,-.75)',against_C=True,against_H=True,kind='drawing or diagram',ink='The crossed block has an enclosing roughly rectangular frame, repeated tall up/down strokes and oblique overstrikes. The surviving textual fragments remain uncertain within a TikZ approximation of that physical cancellation; inseparable overtracing is not assigned extra letters.',confidence='medium',crop='crops/143_scan030_readerB_margin_exception.png',box=[13,1168,511,1850],marked_in_H=True,consequential=False))
for target,place,obj in [('E02','before suites and beneath the raised hom de','curved insertion guide without arrowhead'),('E22','around and across the canceled marginal block','rough rectangular frame and repeated zigzag/oblique cancellation strokes')]:
    i=next(i for i,r in enumerate(d['inventory']) if r['element']==target)
    d['inventory'].insert(i+1,dict(sheet_kind='text',hand='his hand',element=target+'a',kind='drawing',position=place,first_words_or_objects=obj,transcribed='yes'))
for i,r in enumerate(d['inventory'],1):r['element']=f'E{i:02}'
d['notes'].append(dict(id='143_scan030-N9',text='Limited group-theoretic check relevant to the normalizer revision: for any subgroup T of a group A, each t in T normalizes T, so T is contained in N_A(T); by the defining equality nTn^{-1}=T for n in N_A(T), T is normal there, and N_A(T)/T is a group. By contrast A/T needs normality of T in A. This checks the elementary role of a normalizer in the marginal revision; it proves neither the source’s proposed identification with Gamma nor normality in the full exterior-automorphism group. It does not settle the written arrow/est or invariant/injective ambiguity.'))
d['check_events'].append(dict(statement_id='143_scan030-N9',who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; main reader',type='targeted proof check',outcome='Used the defining conjugation equality for N_A(T) and inclusion T subset N_A(T) to verify only the existence of its quotient by T; no geometric or profinite characterization was proved.'))
d['main_adjudication']=dict(original_seen=True,existing_crops_seen=13,main_crops_seen=6,decision='Every disagreement and original mark checked. Two vertical waves rendered consistently, duplicate report row merged, upper arrow/est separated from lower predicate, and visible insertion/cancellation strokes added. Source mismatched formula references and delimiters preserved.')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2));t.write_text(s)
(R/'reviews/143_scan030_main.md').write_text('''# Main-reader adjudication — 143_scan030

The original, all thirteen reader crops and six main-reader crops were inspected. The five broad text crops check the opening underline and continuation, the hom de guide, the main reference and characterization, and the example; the sixth checks the left diagram tag (4). All differing and unresolved loci are tied to these or the reader's saved crops. The supplementary lower opening line is used for passant au profini and suites exactes rather than pretending that the first-line reader crop contains them.

The two separate vertical wavy strokes are encoded as a rotated approximate shape, consistently with scan026. No question-mark dot is invented; two report rows describing this single locus are merged. All completion wedges remain at the upper right, and the new low X basepoint omitted by both witnesses remains xi/j. The rightmost Out is secure but its clipped T is not. The final vertical head remains unclear. The three puncture lists keep their actual connected strokes and their differing commas; the lower diagram has no separate closing curly brace and the final example has only one closing round parenthesis.

The line below the diagram has no independent lower est. Reader B confirms this; the upper graph is retained as arrow/est, and the lower word as invariant/injective. The framed locale and its separate divider are retained. The hom de insertion guide and the roughly rectangular zigzag cancellation are reproduced in TikZ. Celà retains its visible short accent stroke at medium confidence. The completed inner argument alone has the partial underbrace, with its left end near the low 1/opening parenthesis. The source references (1) and (5) are left unchanged although the diagram is (4). N9 records a limited normalizer-quotient proof, not a proof of the proposed arithmetic characterization.
''')
