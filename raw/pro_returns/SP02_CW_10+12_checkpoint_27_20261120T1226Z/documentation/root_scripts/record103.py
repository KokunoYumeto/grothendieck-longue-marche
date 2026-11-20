from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-07',10,103);ch=r.change
r.edit('\\scanpage{103}','\\scanpage{103}\n\\mspage{102}')
r.edit('% archive sheet number: 102','')
r.edit('homomorphisme naturel\n',r'homomorphisme naturel\quad\handwritten{\tikz[baseline=0pt,x=1em,y=1em]{\draw (0,0)--(.12,.12);}}'+'\n')
r.edit("commutant l'un à l'autre\n",r"commutant l'un à l'autre\hspace{1em}\handwritten{\tikz[baseline=0pt,x=1em,y=1em]{\draw (.06,-.15)--(.1,-.32);\fill (0,-.4) circle (.045);}}"+'\n')
r.edit(r'pour $\underline{C}$ la catégorie',r'pour $\underline{C}$ la c\rlap{t}a\rlap{a}t\rlap{g}égorie')
r.edit(r'sur $k$, avec $k$ de',r'sur $k$, a\unsure{\rlap{n}v|\rlap{m}v|v}ec $k$ de')
r.edit(r'\uline{foncteur de De Rham} qui',r'\uline{foncteur de De Rham}\rlap{\handwritten{\tikz[baseline=0pt,x=1em,y=1em]{\draw (0,-.7)--(.3,-.55);}}} qui')
r.edit(r'bigradué\handwritten{\unsure{é,|en,}}',r'bigradué\rlap{\handwritten{\tikz[baseline=0pt,x=1em,y=1em]{\draw (0,-.65)--(.2,-.5);}}}\handwritten{\unsure{é,|en,|ée,}}')
r.edit(r'\handwritten{(}la filtration',r'\rlap{x}\handwritten{(}la filtration')
r.edit(r'Hodge\handwritten{)}.',r'Hodge\rlap{x}\handwritten{)}.')
old=r'\inserted{\handwritten{où on \unsure{gradue} le $2^{\mathrm{ème}}$ membre \uline{par $p$}}}'
new=r'''\inserted{\begin{tikzpicture}[baseline=-.3ex,x=1cm,y=1cm]
\node[anchor=base west] at (0,.3) {\handwritten{où on gradue le $2^{\unsure{\mathrm{em}|\mathrm{ème}}}$ membre \uline{par $p$}}};
\draw (.25,.7) .. controls (-.45,.5) and (-.5,.02) .. (0,-.05) -- (1.6,-.05) .. controls (1.9,.05) and (1.95,-.1) .. (2,-.2) .. controls (2.1,-.05) and (2.2,-.05) .. (2.4,-.05) -- (6.8,-.2) .. controls (7.6,-.25) and (7.85,.1) .. (7.65,.5) .. controls (7.5,.7) and (7.2,.7) .. (7.05,.65);
\draw (2,-.2) .. controls (2.1,-.4) and (1.95,-.65) .. (2,-.9);
\end{tikzpicture}}'''
r.edit(old,new)
r.edit('% The inserted handwritten note is circled, with a pointer immediately after V.','')
r.edit("munie d'un foncteur fibre $F$, on peut",r"\handwritten{\tikz[baseline=0pt,x=1em,y=1em]{\draw (0,.8)--(.15,1.02);}}munie d'un foncteur fibre $F$, on peut")
r.edit('les filtra%','les filtra-')
ch('Hodge phrase emphasis','underline including comma','emphasis with comma outside','underline including comma','A continuous hand rule runs beneath foncteur de Hodge and extends past its comma.','hodge','other','high',False,True)
ch('coproduct sign','handwritten coprod','coprod without hand distinction','handwritten coprod','Two upright pen strokes meet or approach a long low rule; the sign differs visibly from the adjacent typed H.','formula','other','high',False,True)
ch('Hodge Omega','handwritten underlined Omega','underlined Omega without hand distinction','handwritten underlined Omega','The curved omega and separate underline are freehand; superscript p and X/k are typed.','formula','other','high',False,True)
ch('after Hodge formula','no point','point','no supplied point','The closing parenthesis is visible at the right edge; no separate point is visible before the next line Donc.','formula','text not on the page','high',False,True)
ch('after naturel','omitted','omitted','short oblique mark','A small detached grey oblique stroke follows naturel after a blank; no punctuation function is imposed.','naturel','drawing or diagram','medium',True,True)
for i in [1,2]:ch('map arrow '+str(i),'handwritten longrightarrow','longrightarrow without hand distinction','handwritten longrightarrow','Uneven pen shaft and diagonal head contrast with the typed group letters.','map1' if i==1 else 'maps2','other','high',False,True)
ch('below end of commuting sentence','omitted','omitted','isolated small upper/lower marks','An upright grey trace and a darker lower wedge occur beneath the right end of the sentence, away from the equation.','point; middle','drawing or diagram','medium',True,True)
for i in [1,2,3]:ch('lambda '+str(i),'handwritten lambda','lambda without hand distinction','handwritten lambda','The two slanted pen arms are distinct from the typed parentheses and indices.','weight','other','high',False,True)
ch('catégorie in2 opening','catégorie','catégorie',r'c\rlap{t}a\rlap{a}t\rlap{g}égorie','The a cell carries an extra tall t/crossbar, the t cell a low a bowl, and the accented e cell a descending g loop. Overlap is retained without assigning impression order.','category','omission','medium',True,True)
ch('avec in2 opening','avec','avec',r'a\unsure{\rlap{n}v|\rlap{m}v|v}ec','The v has its central pointed valley but also an upright and arch-like trace; n is the first underlying-letter candidate, m remains possible.','avec','omission','low',True,True)
ch('De Rham emphasis','underline','emphasis','underline','The long pen rule is visible beneath the name and extends to the right edge.','DR','other','high',False,True)
ch('after De Rham','no comma','comma','no supplied comma','The right edge contains the end of the name and its rule, but no visible comma.','DR','text not on the page','medium',False,True)
ch('right-margin short stroke below De Rham','omitted','omitted','short slanting stroke','A detached thin rising stroke lies below the underline near the right edge.','rightmarks','drawing or diagram','medium',True,True)
ch('hypercohomology Omega','handwritten unruled Omega','underlined Omega','handwritten unruled Omega','Only the two terminal feet of the omega occur; no separate line lies beneath it.','hyper','misread symbol or index','high',False,True,False,True)
ch('typed bigradué and hand continuation',r'bigradué plus handwritten unsure é,/en,','bigradué,',r'bigradué plus handwritten unsure é,/en,/ée,','The typed final accented e is visible at the right edge. The next line begins with an accented loop, another compressed loop-like continuation and comma-shaped tail; this separate addition is not absorbed into the typed word.','bigradue; handend; handendrot','omission','low',True,True)
ch('right-edge tick below bigradué','omitted','omitted','short slanting stroke','A second short oblique trace is visible beneath the clipped typed ending.','bigradue; rightmarks','drawing or diagram','medium',True,True)
ch('opening parenthesis','handwritten opening parenthesis','omitted','typed x with handwritten opening parenthesis superposed','The pen curve crosses a typed x-shaped body with serif-like ends. Both impressions remain.','parenopen','omission','medium',True,True)
ch('closing parenthesis','handwritten closing parenthesis','omitted','typed x with handwritten closing parenthesis superposed','The freehand curve crosses the typed x after Hodge; the printed full stop follows.','parenclose','omission','high',True,True)
ch('isomorphism sign','handwritten simeq','simeq without hand distinction','handwritten simeq','The upper wave and lower horizontal line are drawn in pen; the curved line below belongs to the note enclosure.','Gr','other','high',False,True)
ch('insertion verb',r'\unsure{gradue}','gradue','gradue','Enlargement and rotation show descending g, angled r, compressed a, tall d, u and final e; no distinct rival word is visible.','notestart; noterot','misread word','medium',True,False)
ch('ordinal in insertion',r'2^{ème}','2ème',r'2 with qualified raised em/ème','The raised writing has an e loop and m humps. No accent or separate final e can be distinguished; the terminal flourish leaves the longer reading as an alternative.','notemid','abbreviation expanded or spelling modernised','medium',True,True)
ch('insertion emphasis','par p underlined','par p plain','par p underlined','The low rule runs beneath the final phrase and through the descender region of p.','noteend','other','high',False,True)
ch('insertion placement','inserted after motif V','marginal note before the parenthetic clause','insertion connected after motif V','The long enclosure dips into a pointer immediately after the typed V, before its closing parenthesis.','note; HV','insertion or placement','high',False,True)
ch('insertion enclosure','comment only','omitted','open curved enclosure and pointer drawn','The low curved enclosure has short returning ends and a downward pointer; it is not merely an editorial description.','note; noteend; HV','drawing or diagram','high',True,True)
ch('given agreement','étant donné une catégorie','étant donné une catégorie','étant donné une catégorie','The last typed letter is accented e, followed by a blank and une; no further e is present.','givenC','other','high',False,False)
ch('last category letter','plain C','underlined C','plain C','The final C has a single body and blank space below it, unlike the separately underlined C in2.','givenC; sec2','misread symbol or index','high',False,True,False,True)
ch('left tick above munie','omitted','omitted','small slanting stroke','A short pencil stroke sits above and to the left of the last line.','lefttick; general','drawing or diagram','medium',True,True)
ch('page-ending division','filtra with comment join','filtra discretionary hyphen','filtra-','The final horizontal hyphen is visible at the right edge and is retained as a physical page-ending division.','finalhyphen','omission','high',True,False)
ch('folio','comment only','administrative page marker102','mspage102','The lower-left pencil figures read102.','folio','insertion or placement','high',True,True)
r.doubt('avec','n/v superposition','m/v superposition; v with unidentified extra trace','low','The v body is clear; the extra arch is not secure enough for an unqualified earlier letter.')
r.doubt('after typed bigradué','handwritten é,','en,; ée,','low','Separate handwritten line beginning retained after the already visible typed ending; rotated20 degrees for inspection.')
r.doubt('insertion ordinal','2 with raised em','2 with raised eme orème','medium','Final flourish could conceal another small letter; no accent is distinctly visible.')
r.notation('Omega','first occurrence underlined, second unruled; both handwritten','10/103, Hodge and hypercohomology formulas')
r.notation('category C','underlined in2; plain in final paragraph','10/103')
r.notation('group G and cohomology H','single typed letters; separate G underline where visible','10/103')
r.notation('parentheses around filtration clause','typed x-shaped impressions under handwritten curved parentheses','10/103')
r.r['abbreviations']=[dict(abbreviation='i.e.',expansion='id est',attestations='10/103'),dict(abbreviation='car.',expansion='caractéristique',attestations='10/103'),dict(abbreviation='2em (em raised)',expansion='deuxième',attestations='10/103, insertion'),dict(abbreviation='Gr',expansion='gradué associé',attestations='10/103'),dict(abbreviation='DR',expansion='De Rham',attestations='10/103'),dict(abbreviation='Hdg',expansion='Hodge',attestations='10/103')]
r.r['inventory_overrides']={'grading insertion':{'first_words_or_objects':'où on gradue le 2 with raised em membre par p; open enclosure and pointer'},'grading handwriting':{'first_words_or_objects':'où on gradue (resolved); raised em retained'},'opening parenthesis':{'first_words_or_objects':'typed x with handwritten opening parenthesis'},'closing parenthesis':{'first_words_or_objects':'typed x with handwritten closing parenthesis'},'bigradue ending':{'first_words_or_objects':'qualified handwritten é, / en, / ée,'}}
extras=[('naturel','after naturel','short oblique mark','drawing','unnamed hand'),('point','below commuting sentence end','upper upright and lower wedge','drawing','unnamed hand'),('category','2 opening','t/a a/t g/é overlapping impressions','text','typewriter'),('avec','2 opening','qualified n/v or m/v composite','text','typewriter'),('right1','right edge below De Rham','short rising stroke','drawing','unnamed hand'),('right2','right edge below bigradué','short rising stroke','drawing','unnamed hand'),('noteframe','above motif V','open curved enclosure and downward pointer','drawing','his hand'),('ordinal','insertion','2 with raised em','text','his hand'),('noteunderline','insertion ending','par p underline','text','his hand'),('lefttick','above final line left','short oblique stroke','drawing','unnamed hand'),('hyphen','end of page','filtra-','text','typewriter'),('folio','lower left','102','margin note','unnamed hand')]
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:103',sheet_kind='typescript',hand=hand,element='103-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops103.json').read_text())
r.r['inspection_note']='Whole then both halves viewed before C/H, C doubts and C inventory. All35 crops displayed, including note rotated3 degrees and small handwritten ending rotated20 degrees. All agreed prose and mathematical letters, indices, stars, arrows, coproduct, Omegas, lambdas, equality/isomorphism and punctuation inspected. C gradue doubt resolved from letter forms; the ending after bigradué remains qualified. The actual handwritten note has an open enclosure with a pointer after V. No OCR, parallel transcription, compilation, context access or mathematical correction. The final plain C, donné and absent point after the Hodge formula are retained from visible ink. Separate right-edge strokes are drawn without interpreting their function.'
r.save('work/record103.json')
