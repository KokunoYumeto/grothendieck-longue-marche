from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B12-01',12,85,'cancelled_draft');H='[No H text supplied.]'
def ch(place,C,final,shows,crop,kind='other',confidence='high',against_C=False,consequential=False):
 r.change(place,C,H,final,shows,crop,kind,confidence,against_C,False,False,consequential)
r.edit(r'\inserted{\handwritten{4}}',r'\raisebox{2ex}{\inserted{\handwritten{4}}}')
noeth=r'n\unsure{\rlap{e}o|o}et\rlap{é}h\rlap{h}érien'
r.edit(r'\unsure{noethérien}',noeth)
j=r'''\mbox{\begin{tikzpicture}[baseline=(left.base)]
\node[inner sep=0] (left) {puissances};
\node[anchor=base west,inner sep=0,xshift=.25cm] at (left.base east) {de son};
\node[anchor=south west,inner sep=0,xshift=-.05cm,yshift=.08cm] at (left.north east) {\inserted{$\text{\rlap{J}\raisebox{.3ex}{\kern.08em J}}_i$}};
\end{tikzpicture}}'''
r.edit(r'puissances \inserted{$\mathbb{J}_i$} de son',j)
r.edit(r'\unsure{Z_{i\,S}|Z_{A\,S}}',r' Z_{i\,S}')
cf=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {dominante.};
\node[anchor=south west,inner sep=0,yshift=.12cm] at (base.north west) {\inserted{cf définition 5}};
\end{tikzpicture}}'''
r.edit(r'dominante\inserted{cf définition 5}.',cf)
r.edit(r'S_{\unsure{o|0}}',r'S_o')
r.edit('cf SGAD IX 4.2.','cf SGAD IX. 4.2.')
ch('heading, added 4',r'\inserted{\handwritten{4}}',r'\raisebox{2ex}{\inserted{\handwritten{4}}}','The small handwritten 4 has a closed triangular upper part and a longer right stem, and stands above the gap between Remarques and a). Its raised level is restored.','heading4','insertion or placement','high',True)
ch('remark a, first noetherian adjective',r'\unsure{noethérien}',noeth,'After noet, each of the two adjacent altered cells contains the tall left h ascender/serif and an e middle bar/bowl with an acute above. The first o also contains two dark mid-height bar fragments compatible with an overlapping e; that component remains qualified. The plain later noethérien supplies separate h and é controls, without deciding any reading by grammar. No typing chronology is asserted.','noeth;noethfine;noethmiddle;ofirst;hcontrol','misread word','medium',True)
ch('remark a, inserted J_i',r'\inserted{$\mathbb{J}_i$}',j,'The inserted J has two vertically displaced top bars and two lower hooks, with the upper impression slightly rightward. These are represented as overlapping J impressions, not silently assigned to a blackboard-bold alphabet. The i has a separate dot/stem/foot below and to the right; the addition is above the gap between puissances and de son, with i near the d.','Jinsert;insertplace;Jfine','misread symbol or index','high',True,True)
ch('remark b, base-change Z index',r'\unsure{Z_{i\,S}|Z_{A\,S}}',r'Z_{i\,S}','A dot-like top impression, left-projecting serif, vertical stem, and broad foot remain visible. The apparent left leg of an A is the continuous diagonal cancellation stroke; the typed index matches the separate i control. C macro/table doubt is resolved from the surviving parts of i.','baseformula;baseZ;baseifine;uicontrol;Ziprimewide','misread symbol or index','high',True,True)
ch('remark b, added reference',r'dominante\inserted{cf définition 5}.',cf,'cf définition 5 is typed on a separate raised line above dominante., starting at the same left edge and extending beyond the word. No leader occurs. Both its text and the baseline word/period are preserved in their relative positions.','cfdef5;cfplace','insertion or placement','high',True)
ch('Definition 5, opening family delimiter',r'\unsure{(Z_i)|\{Z_i)}',r'\unsure{(Z_i)|\{Z_i)}','The main tall curved stroke is compatible with an opening parenthesis, but an extra upper horizontal stroke, a left fragment, and a lower right loop overlap it. Their origin cannot be separated securely. Z, its dotted i, and the closing parenthesis are clear. C macro/table uncertainty is retained.','Zibrackets;parenthesisfine','other','low')
ch('Lemma 6, first S subscript',r'S_{\unsure{o|0}}',r'S_o','The circle is the height and round proportion of the lowercase o in soit, and is shorter than the distinct tall oval zero in the two preceding J_i=0 formulas. The second lowered o has the same round form. C macro/table doubt is resolved to the visible lowercase o.','SSo;Socontrol;uiSo;zeroone;zero2read','misread symbol or index','high',True,True)
ch('final reference','cf SGAD IX 4.2.','cf SGAD IX. 4.2.','A separate dark baseline stop stands after the X, before the gap preceding 4. The further stops between 4 and 2 and after 2 remain present.','SGAD;IX42;IXdot','omission','high',True)
for place,reading,shows,crop in [
 ('remark a, indexed family',r'(J_i)_{i\quad I}','The outer index has a dotted i and a capital I separated by blank space, with no membership sign. The inner J has its own lowered i.','Jiindex'),
 ('remark a, final two formulas',r'\quad J_i=0\ \ldots\ \quad J_i=0 !','Both blank slots before J_i are unfilled. The second formula has no B and ends with a separate exclamation mark; no intersection or product symbol is supplied.','Ji0one;Ji0two;zeroone;zero2read'),
 ('local cancellation after fractions','Le fait','The L upright/foot, e curve, f crossbar, a bowl, i and t remain readable under the x row, which extends past the last letter.','Lefait'),
 ('local cancellation after On peut','se ram','The s/e curves, r shoulder, a bowl and m stems remain beneath the typed crosses. Only the visible fragment is retained.','seram;seramfine'),
 ('Definition 5, canceled relativement','relativement','The whole word remains discernible beneath the row of x crosses; its local cancellation is retained in addition to the global page cancellation.','relcancel'),
 ('Definition 5, long canceled parenthesis',r"(ou que la famille des sous-préschémas $Z_i$, s'il s'agit de tels, est sch dense dans $X$ rel à $S$)",'The complete two-line parenthesis is readable under repeated x strokes. The index i descends below its cancel row, and a comma tail survives beneath the last cross after Z_i. Both surrounding parentheses, apostrophes, accent on préschémas and grave on à are retained.','longdel1;longdel2;longdel3;longdel4;longdel5;longdel6;Zicommaread'),
 ('Definition 5, canceled restart','(resp ou que la famille','The opening parenthesis, r/e/s/p, o/u and que la famille remain under crosses. No closing parenthesis is visible for this restart.','respcancel;quelafam'),
 ('Definition 5, before family delimiter','des','The d ascender/bowl, e middle bar and s lower curve remain under the three crossing cancel cells.','descancel'),
 ('Definition 5, base-change expression',r"S'\quad S;\ u_{i\,S'}\colon Z_{i\,S'}\quad X_{S'}",'Each prime is a single short raised stroke after S, and each i has a dot and foot at the index level. The spaces between S-prime/S and Z/X have no arrow.','SprimeS;uiprime;Ziprime;Xprime;Ziprimewide'),
 ('Definition 5, ellipsis',r'X \ldots,','Three separate baseline dots follow X, followed by a comma with a descending tail.','Xellipsis'),
 ('Lemma 6, capitals','Idéal Nilpotent','The initial I has top and bottom bars; N has two uprights and a diagonal. Both capitals are retained.','idealnil'),
 ('Lemma 6, unusual verb','resper','Six visible letters r-e-s-p-e-r precede avec; no expansion or repair is made.','resper;resperfull'),
 ('Lemma 6, quoted phrase',r"``rel à $S$''",'The opening and closing quotation marks each have two separate high strokes. The abbreviated rel and grave-accented à remain unexpanded.','relquote')]:ch(place,reading,reading,shows,crop)
r.doubt('remark a, first o in noetherian adjective',r'\rlap{e}o','o with internal residual ink','medium','Two dark fragments at middle-bar height suggest an e/o overlap; unlike the neighboring h/é overprints, this component is not fully separable.')
r.doubt('Definition 5, opening family delimiter','(Z_i)',r'\{Z_i) or parenthesis with another overprinted glyph','low','Extra top horizontal and lower loop remain fused with the tall curved delimiter; no underlying letter is confidently assigned.')
r.notation('typewriter overlapping letters',r'\rlap{é}h; \rlap{h}é','12:085 first noetherian adjective; both ascenders, accents and e bowls survive; first e/o overlap remains qualified.')
r.notation('overprinted inserted J',r'\text{\rlap{J}\raisebox{.3ex}{\kern.08em J}}_i','12:085 remark a, above puissances/de son: two displaced J impressions; no intended alphabet inferred.')
r.notation('base-change i and prime',r'Z_{i\,S}; u_{i\,S\prime}; Z_{i\,S\prime}; X_{S\prime}','12:085 dotted i with foot; primes are single high short strokes. Diagonal cancellation is separate from the i of Z_iS.')
r.notation('lowercase o versus zero',r'S_o; u_{i\,S_o}; J_i=0','12:085 lemma circles have lowercase o height/proportion; zeros in remark a are taller ovals.')
r.notation('unfilled formula slots',r'(J_i)_{i\quad I};\ \quad J_i=0;\ Z_i\quad X;\ S\quad\operatorname{Spec}(k)','12:085 visible blanks preserved; no membership, intersection, product, or arrow supplied.')
for a,e in [('sch.','schématiquement'),('sch','schématiquement'),('rel à','relativement à'),('resp','respectivement'),('cf','confer / see'),('SGAD','not expanded securely from this page'),('NB','nota bene')]:r.r.setdefault('abbreviations',[]).append(dict(abbreviation=a,expansion=e,attestations='12:085'))
r.r['inventory_overrides']={'085-04':dict(first_words_or_objects='two vertically displaced J impressions with subscript i',position='above gap between puissances and de son'),'085-07':dict(position='raised line directly above dominante., left aligned')}
extras=[('adjacent h/é overprints, first e/o overlap qualified','text','remark a first noetherian adjective','typewriter'),('overprinted opening family delimiter, unresolved','text','Definition 5 before Z_i','typewriter'),('archive folio 84 retained as comment','margin note','bottom left','another unnamed hand')]
for i,(s,k,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='12:085',sheet_kind='cancelled_draft',hand=h,element=f'085-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=sum([json.loads(Path(f).read_text()) for f in ['work/crops12_085.json','work/fine12_085.json','work/last12_085.json']],[])
r.r['inspection_note']='Root alone viewed whole085 and both actual supplied halves before witnesses, then full C, H absence, all four C macro/table doubts, four retained slips and all16 C inventory elements. All82 crop recipes were viewed. The first combined display of respcancel/quelafam was truncated and was not counted; each was successfully viewed separately. Two fine crops (zerotwo, Zicancelcomma) missed their intended loci and were not used for those decisions; zero2read and Zicommaread supply the correct loci. Both actual halves were reread line by line after initial and fine crops, followed by four adaptive controls. All three broad diagonal cancellations, local x deletions, three raised additions, and all mathematics-critical glyphs were inspected; there is no slanted verbal margin note. Archive84 remains a comment. Overprints are represented without assigning chronology. Context remains sealed. This is first-pass collation, not the ordered audit or a mathematical check.'
r.save('work/record12_085.json')
