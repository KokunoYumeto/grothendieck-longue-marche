from pathlib import Path
import json,csv,re
R=Path('/workspace/scratch/d12e26a9cd50/SP93_C13_151_work');p=R/'reports/151_scan017.json';d=json.loads(p.read_text());tp=R/'reports/151_scan017.tex';t=tp.read_text()
f={r['box']:r['first'] for r in csv.DictReader((R/'second/151_scan017_comparison.tsv').open(),delimiter='\t')}
b={r['box']:[int(r[k]) for k in ('x0','y0','x1','y1')] for r in csv.DictReader((R/'second/151_scan017_boxes.tsv').open(),delimiter='\t')}
D=r'{\unsure{\delta|\partial}}';G=lambda s:r'\unsure{\mathcal G_{'+s+r'}|\mathfrak S_{'+s+'}}'
def node(x,y,s):return r'\node[anchor=west,inner sep=0pt] at ('+str(x)+','+str(y)+') {$'+s+'$};\n'
def fig(s):return '\\figure{\\begin{tikzpicture}[x=.72cm,y=.72cm]\n'+s+'\\end{tikzpicture}}'
upper=fig(node(.75,3.2,'K_n'+D+r'_n=\mathrm{id}_{\mathbb E_n}')+node(.75,2.1,D+r'_n\sigma=i_n(\sigma)'+D+'_n')+node(.75,1.1,r'\sigma K_n=K_n i^{\prime}_n(\sigma)')+node(.75,.2,r'K_n\sigma_{n+1}=K_n')+node(7,2.1,r'\text{si }\sigma\in'+G('n'))+node(7,1.1,r'\text{si }\sigma\in'+G('n-1'))+node(11.3,2.1,r'\text{pour }n\geq2')+node(11.3,1.1,r'\text{pour }n\geq2')+r'''\draw (.4,3.65)..controls(.22,3.15)and(.6,2.5)..(.15,2.0)..controls(.6,1.8)and(.15,.2)..(.5,-.2);
\draw (0,-.4)--(-.08,3.9)--(5.8,4.1)--(5.9,3.1);
\draw (6.12,3.03)--(10.9,3.15)--(11.08,.45)--(.05,-.48)--(0,3.9);
''')
start=t.index('\\[\n\\boxed{\\left\\{');end=t.index('\\]\n',start)+3;t=t[:start]+upper+'\n'+t[end:]
dual=fig(node(-1,1.55,'(*)')+node(.4,3.2,D+r'_n^*K_n^*=\mathrm{id}_{E_n^*}')+node(.4,2.15,r'\sigma'+D+r'_n^*='+D+r'_n^*i_n(\sigma)')+node(.4,1.1,r'K_n^*\sigma=i^{\prime}_n(\sigma)K_n^*')+node(.4,.1,r'\sigma_{n+1}K_n^*=K_n^*')+node(7.7,2.15,r'(\sigma\in'+G('n')+')')+node(7.7,1.1,r'\text{(id)}')+r'''\draw (0,-.28)--(-.08,3.75);
\draw (.04,3.77)--(7.25,4.0)--(7.4,3.85);
\draw (7.55,3.78)--(7.6,.1)--(.12,-.45);
''')
start=t.index('\\[\n(*)');end=t.index('\\]\n',start)+3;t=t[:start]+dual+'\n'+t[end:]
bar=r'\begin{tikzpicture}[baseline=(e.base)]\node[inner sep=0pt] (e) at (0,0) {$E_n^*$};\draw (-.36,-.3)--(-.36,-.43)..controls(-.12,-.39)and(.12,-.48)..(.32,-.4);\node[anchor=north,inner sep=0pt] at (0,-.55) {$'+G('n')+r'\text{-ens.}$};\end{tikzpicture}'
old=r'\underbrace{E_n^*}_{\unsure{\mathcal G_n|\mathfrak S_n}\text{-ens.}}';assert old in t;t=t.replace(old,r'\text{'+bar+'}')
label=r'\inserted{(\alpha^*_{\deleted{\unsure{p+q}}p+q,p},\beta^*_{\deleted{\unsure{p+q}}p+q,q})}'
pair=fig(node(-1,.1,'(**)')+node(.4,.75,'E_{p+q}^*')+node(4.8,.75,'E_p^*\times E_q^*')+node(9,.9,r'\text{surjectif pour}')+node(9,.1,r'p,q\geq1')+node(1.6,2.1,label)+r'''\draw[->] (2.15,.72)--(4.5,.72);
\draw (1.4,1.88)..controls(1.9,1.65)and(2.7,1.35)..(3.0,1.12)..controls(3.0,1.45)and(3.3,1.33)..(3.55,1.4);
\draw (4.2,1.55)..controls(5.5,1.55)and(6.2,1.62)..(6.3,1.85)--(6.3,2.5);
\draw (0,1.25)--(.05,-.38);
\draw (.1,1.65)--(12.3,1.8);
\draw (12.48,1.7)--(12.48,.0);
\draw (.12,-.5)--(12.35,-.25);
''')
start=t.index('\\[\n(**)');end=t.index('\\]\n',start)+3;t=t[:start]+pair+'\n'+t[end:]
oldbottom=r'\boxed{'+D+r"'_m=\rho_{m+1}"+D+'_m}'
bottom=r'\begin{tikzpicture}[baseline=(e.base)]\node[inner sep=0pt] (e) at (0,0) {$'+D+r"'_m=\rho_{m+1}"+D+r'_m$};\draw (-1.8,.45)--(-1.72,-.4);\end{tikzpicture}'
assert oldbottom in t;t=t.replace(oldbottom,r'\text{'+bottom+'}')
# The low point after the last condition remains a point; no syntactic closure is supplied.
revised={'B004':upper,'B008':dual,'B009':f['B009'].replace(old,r'\text{'+bar+'}'),'B010':pair,'B011':pair,'B017':f['B017'].replace(oldbottom,r'\text{'+bottom+'}')}
def update(cid,box,final,evidence):
 c=next(c for c in d['changes'] if c['id']==cid);c.update(final=final,evidence=evidence,crop=f'crops/151_scan017_second_{box}.png',box=b[box],differs_C=True)
update('C017-13','B004',upper,'The upper frame has a stepped, interrupted top course and a retraced left edge; the two pour n>=2 conditions lie beyond its right border. Both final digits have a curled upper stroke and a broad horizontal foot, matching 2. The grouping brace remains inside. A full rectangle enclosing the conditions changes the written scope.')
update('C017-18','B008',dual,'The four identities are inside an outline with separated top corners and a lower-left gap. The sigma-membership condition and (id) lie outside the right boundary. The subscript E of id has one main vertical, unlike the unmistakably doubled E in the neighboring finite-set diagrams; it remains plain E.')
update('C017-20','B009',revised['B009'],'The annotation beneath E_n^* is attached by a low flat stroke with an upturned left end and rounded right return, without a central brace cusp. The following de has no separate terminal s. Satisfaisant aux relations is retained, with its tall t/f forms and final sequence; the isolated group glyph remains G/S doubtful.')
update('C017-22','B010',pair,'The alpha/beta pair is above the enclosing line, with a short curved two-arm leader reaching down toward the map. A separate lower-right returning stroke is preserved. The old p+q-like subscripts remain doubtful under overwriting; the surviving p+q,p and p+q,q are live. They are not replaced by a generic unreadable math symbol.')
update('C017-23','B011',pair,'The map frame consists of separate top, left, right and lower courses, with gaps at the corners; the pair label stands above it. The short curved leader approaches the map from above and is not an underbrace below the map. The comparison in p,q>=1 has both the upper angled stroke and the lower bar.')
d['changes'].append(dict(id='C017-A01',place='bottom factorization, left boundary',C=oldbottom,H=r"\partial'_m=\rho_m\partial_m",final=bottom,evidence='Only a separate upright stroke stands immediately left of the bottom factorization. No upper, right or lower enclosure is visible around it; the lower edge is the scan boundary. The complete box in C is therefore removed and the visible left stroke is drawn. H omits this stroke.',confidence='high',kind='drawing or diagram',crop='crops/151_scan017_second_B017.png',box=b['B017'],differs_C=True,differs_H=True,consequential='',marked_in_H='no'))
for x in d['inventory']:
 if 'underbrace' in x.get('first_words_or_objects',''):x['first_words_or_objects']=x['first_words_or_objects'].replace('underbrace','flat underbar')
d['notes'].append('Independent audit: both upper range digits remain 2, not the second reader’s proposed 3. Stepped/gapped frames and their exterior conditions, the flat group-action underbar, and the leader of the inserted alpha/beta pair are now reproduced explicitly with text nodes. The bottom factorization has only a left boundary stroke, not a complete box. Delta/partial and the ornate group letter remain unresolved across the page; no algebraic expectation settled them. The bottom case value 1 retains its visible angled cap, upright and foot at the scan edge. The written rho_(m+1) versus rho_m mismatch remains.')
e={
'B001':'The circled 1, blackboard E objects, opposed arrows and n>=1 agree. The inclusion glyph has a curved upper-left entry and closed lower loop, which does not settle delta versus partial; the first local doubt is retained.',
'B002':'The retraction has a tall upright with two angular arms, matching the capital K elsewhere on this page. The hooked forward inclusion, leftward retraction, right grouping bracket and both words agree. The inclusion glyph remains delta/partial doubtful.',
'B003':'The group glyph has a broad outer loop and an inner S-like curve; it does not establish fraktur S alone. The G/S doubt remains, with opère sur, the blackboard E, i_n and hooked inclusion.',
'B004':'Both final range digits have the same rounded upper turn and broad horizontal foot: 2 is retained in both rows. The frame steps down after the first equation and stops before the two pour conditions; its separated top course and left retrace are drawn. The brace and all four formulas remain.',
'B005':'The projector has a long upright and an angular upper bowl, matching p more closely than the looped rho below. The cramped ending after project- still does not settle projection/projecteur. The opening parenthesis has no closing mate at the edge. The definition accent and formula agree.',
'B006':'The tiny text under the defining equals is still compressed and remains unsure déf. The two i factors and group chain agree. The transposition has a square left delimiter and round right delimiter; it is not regularized. Both upper range digits visible again are 2.',
'B007':'The two opposed arrows and their d_n=K_n^* and p_n labels agree. Both E objects are doubled; the inclusion-star sign remains delta/partial doubtful.',
'B008':'The id subscript has a single E upright and detached upper return, not the clear double stroke of blackboard E nearby. The parenthetic id has a dotted i and tall looped d. Both conditions sit outside the right frame edge; gaps at the upper corners and lower left are reproduced.',
'B009':'The following preposition has a tall d and one joined low e without a separate s. The participle and aux relations remain legible. The group annotation is attached to E_n^* by a flat underbar with no central cusp, replacing the first mathematical underbrace.',
'B010':'The older indices remain visible only as crossed p/q-like strokes, so their explicit uncertainty is retained. The live replacement p+q,p and p+q,q remain. The descending two-arm leader and separate return below the label are now drawn; this is an insertion connector, not an underbrace.',
'B011':'The finite-set dual map and surjectif pour p,q>=1 agree. The comparison contains a lower bar. The outer strokes have open corners, and the inserted pair is placed above the top course with its leader toward the arrow; the label is not omitted merely because this overlapping crop clips its top.',
'B012':'The long stroke below défini par is the top edge of the formula frame, not an additional lexical underline. The alpha comparison n>p>=1, objects and stars agree. The second chain index stays n-2/n-1 doubtful; the short course before the dots remains visible and is retained.',
'B013':'The first comparison contains both an upper angle and a separate lower stroke, supporting >=. All primed stars and chain objects agree. The long stroke by défini par forms the frame top, rather than a separate word underline. The intervening dots are not a solid arrow.',
'B014':'The formula, inverse exponent, and line-broken circulaire agree. The compressed following word shows accented low entry, a tall stem and short joined ending; élément. remains only a doubtful abbreviation. The proposed full standard is not established. The extra detail crop was also viewed.',
'B015':'The alpha map has a clear complete right head; the beta map ends in a short thick rising terminal without a separate lower wing. The first headless hooked beta course is retained instead of adding a full head. The affine formula, colon and lack of final punctuation agree.',
'B016':'The live source and target indices are m and m+1 below crossed older strokes, which remain explicitly doubtful. The pointwise formula has a narrow single hump n, distinct from the wider m in the adjacent factorization; it remains n. The first map index is less distinct and stays m/n doubtful. Pale 16 is separate.',
'B017':'Only the left upright boundary is visible beside the factorization, so a complete box is removed. Rho_(m+1) in that factorization differs visibly from rho_m in the prose and cases and is preserved. The second case value has a cap, upright and foot consistent with 1 despite the touching edge. The extra detail crop was viewed; the written points are retained.'}
m={k:dict(changed=k in revised,evidence=v) for k,v in e.items()}
for k,v in revised.items():m[k]['final']=v
(R/'reviews/151_scan017_manual.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');tp.write_text(t)
