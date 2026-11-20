from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-07',10,106);ch=r.change
r.edit(r'\scanpage{106}',r'\scanpage{106}'+'\n'+r'\mspage{105}')
r.edit('% archive sheet number: 105','')
r.edit('admet',r'a\unsure{\rlap{m}d|d}\rlap{d}met')
r.edit(r'\uline{pré-structure de Hodge}',r'\uline{pré-str\rlap{c}u\rlap{u}cture de Hodge}')
r.edit(r'\unsure{\otimes|\Omega}',r'\otimes')
r.edit('conjugaison','conjuguaison')
r.edit('un groupe de Galois $G$,',r'un groupe de \unsure{$\mathbb{G}$|G}alois $G$,')
r.edit(r'\unsure{\doteqdot|\div|=}',r'\unsure{\doteqdot|=}')
r.edit(r'\inserted{schéma en}',r'''\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]
\node[anchor=base west] at (0,.4) {schéma en};
\draw (-.15,.6) .. controls (-.3,.1) and (.2,0) .. (1,0) -- (2.5,.05) .. controls (3.1,.05) and (3.5,-.1) .. (3.6,-.6) .. controls (3.8,.05) and (4.1,.05) .. (4.7,.1) -- (5.8,.3) .. controls (6.2,.4) and (6.2,.5) .. (6.1,.65);
\end{tikzpicture}}''')
r.edit(r'\inserted{(pro-unipotent)}',r'''\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]
\node[anchor=base west] at (0,.4) {(pro-unipotent)};
\draw (-.4,-.8) .. controls (-.55,.1) and (-.2,.1) .. (.7,.1) -- (7,.12) .. controls (8,.1) and (8.2,.35) .. (8,.7);
\end{tikzpicture}}''')
r.edit(r'\inserted{$V$}',r'''\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]
\node[anchor=base west] at (0,.5) {$V$};
\draw (.1,-.65) .. controls (0,-.35) and (.6,.05) .. (1.2,.7) -- (1.6,1.3);
\end{tikzpicture}}''')
r.edit(r'\inserted{$F$}',r'''\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]
\node[anchor=base west] at (0,.4) {$F$};
\draw (.7,.5) .. controls (1.05,-.2) and (.2,-.35) .. (-.4,-.9);
\end{tikzpicture}}''')
r.edit(r'\inserted{$\otimes$-}',r'''\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]
\node[anchor=base west] at (0,.4) {$\otimes$-};
\draw (-.25,-.7) .. controls (0,-.25) and (.6,-.15) .. (1.25,-.1) .. controls (1.65,0) and (1.6,.35) .. (1.5,.6);
\end{tikzpicture}}''')
r.edit(r'\inserted{qui commutent}',r'''\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]
\node[anchor=base west] at (0,.5) {qui commutent};
\draw (-.15,.65) .. controls (-.45,.35) and (-.4,-.05) .. (.2,-.1) -- (6,-.05) .. controls (6.5,-.05) and (6.7,-.3) .. (6.7,-.65) -- (7.4,.55);
\end{tikzpicture}}''')
r.edit(r'\inserted{pré-}',r'''\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]
\node[anchor=base west] at (0,.4) {pré-};
\draw (.6,-.55) .. controls (.8,-.25) and (1.1,-.15) .. (1.4,-.05);
\end{tikzpicture}}''')
r.edit('(nécessairement central,',r'\margin{\tikz[baseline=0pt,x=1em,y=1em]{\draw (0,0) .. controls (.1,.05) and (.17,.15) .. (.22,.3);}}(nécessairement central,')
ch('admet overtyping','admet','admet',r'a\unsure{\rlap{m}d|d}\rlap{d}met','The m cell also carries a tall hooked d shaft. The preceding d has additional low right-hand stems suggestive of m, but those merge more strongly and stay qualified. Both impressions are represented without chronology.','admet; admetclose','omission','medium',True,True)
ch('un e cancellation',r'un\deleted{e}','un',r'un\deleted{e}','A separate e cell after un is crossed with x strokes.','une','omission','high',False,True)
ch('cancelled sous',r'\deleted{sous}','omitted',r'\deleted{sous}','The four letters s o u s remain visible beneath four typed cancellation crosses before sur.','sous','omission','high',False,True)
ch('groupes ending','groupes','groupe','groupes','After the complete e a separate clipped cell retains an upper curve and lower left trace of s at the scan edge.','groupeedge','misread word','medium',False,True)
for place,cr,shows in [('schéma en guide','schema','The long open lower enclosure curls at both ends and descends to a point after le.'),('pro-unipotent guide','pro','A shallow lower line curls upward on the right and descends on the left before H.'),('inserted V guide','Vinsert','A long rising diagonal starts in the gap after vectoriel, to the right of the raised typed V.'),('inserted F guide','Fadd','A curved freehand guide descends from the right of the raised F to the gap before the period after oubli.'),('tensor-prefix guide','tensorinsert','A curved line turns upward on the right of the raised tensor-prefix and descends left toward the start of sous-catégorie.'),('commuting insertion guide','commutent; commutentrot','The lower open loop runs under qui commutent and ends in a descending then rising pointer after homomorphismes.'),('pré- guide','pre','A short rising curved guide lies below the raised pré-, in the gap before structure.')]:
 ch(place,'omitted','omitted','guide drawn',shows,cr,'drawing or diagram','high',True,True)
ch('definition heading emphasis','underlined','italic','underlined','One continuous separate rule extends beneath pré-structure de Hodge.','heading','other','high',False,True)
ch('definition heading overlapping letters','structure','structure',r'str\rlap{c}u\rlap{u}cture','The first of the two adjacent cells contains the curved c body together with the low u bowl and right stem; the next contains the open c curve plus the right u stem. The following t is separate.','headingstr','omission','medium',True,True)
for place,cr in [('dimension field','Qdim'),('first tensor base','firstformula'),('condition a quoted field','conditionquote'),('homogeneous subspace field','conditionA'),('tensor category field','middle'),('F C tensor base','FC'),('defined over field','Qdef'),('centrality component field','centralQ'),('final component field','lastQ')]:
 ch(place,'plain underlined Q','underlined blackboard Q','plain underlined Q','A single typed oval with a short lower tail stands above a detached underline; no second displaced letter body is visible.','%s'%cr,'misread symbol or index','high',False,True,False,True)
ch('first tensor sign doubt',r'\unsure{\otimes|\Omega}',r'\otimes',r'\otimes','The oval is crossed by two diagonal strokes, matching the separately enlarged prefix and later tensor sign; there are no separated bottom feet of Omega.','tensor1; tensor2; tensorinsert','misread symbol or index','medium',True,False,False,True)
ch('first bigrading placement','inline','display','inline','The formula follows the preceding comma on the same typed line; the next prose line begins telle que.','firstformula','insertion or placement','high',False,True)
ch('first coproduct handwriting','handwritten coprod and p,q','no hand distinction','handwritten coprod and p,q','The tall irregular U-like product arms and small p,q below are freehand; the V and its typed superscripts lie to the right.','coprod1','other','high',False,True)
ch('condition a quotation marks','double quotes','guillemets','double quotes','Two small raised vertical impressions occur at each end of définie sur Q, without angled guillemets.','conditionquote','misread symbol or index','high',False,True)
ch('i.e. emphasis','underlined','plain','underlined','The continuous rule lies directly beneath i.e. and above the V of the following line.','conditionA; Vbar','other','high',False,True)
ch('second coproduct handwriting','handwritten coprod','no hand distinction','handwritten coprod with typed p+q=n','The irregular vertical arms and bottom crossbar contrast with the regularly spaced typed index below.','coprod2','other','high',False,True)
ch('sous espace','sous espace','sous-espace','sous espace','A blank separates sous from espace; no horizontal hyphen occupies it.','conditionA','abbreviation expanded or spelling modernised','high',False,True)
ch('conjugate V bar scope','bar over V only','bar over V and p,q','bar over V only','The short pale bar is immediately above V and stops before the raised p,q. The much longer dark line higher up belongs to the previous line under i.e.','Vbar','misread symbol or index','high',False,True,False,True)
ch('conjugation mapping handwriting','handwritten mapsto and x bar','no hand distinction','handwritten mapsto and x bar','An irregular rightward shaft with a distinct initial upright and the short freehand bar over x are separate from the typed x bodies.','conjmap','other','high',False,True)
ch('conjugaison spelling','conjugaison','conjuguaison','conjuguaison','After the descending g there is a distinct u cell before a: the full typed sequence is c o n j u g u a i s o n.','conjword','misread word','high',True,False)
ch('NB opening doubt',r'\unsure{(}','(',r'\unsure{(} retained','Multiple curved overlapping traces precede N; their original character cannot be separated reliably. The opening curve remains qualified.','NB','other','low',False,True)
ch('NB abbreviation','NB','N.B.','NB','N and B are adjacent plain capitals without following points.','NB','abbreviation expanded or spelling modernised','high',False,True)
ch('oubli quotation marks','double quotes','guillemets','double quotes','Two high short vertical marks occur on each side of oubli.','Fadd','misread symbol or index','high',False,True)
ch('first Galois capital','G','G',r'\unsure{$\mathbb{G}$|G}','An extra curved impression with a right-hand bar sits above and merges into the lower G. A repeated G is possible, but the upper body is insufficiently separate for certainty; the later Galois has a single ordinary capital.','Galois; Galoisclose; Galois2','misread symbol or index','low',True,True)
ch('tout cancellation',r'\deleted{tout}','omitted',r'\deleted{tout}','Four typed letters remain beneath x marks between et and plus.','tout','omission','high',False,True)
ch('oubli cancellation',r'\deleted{oubli}','omitted',r'\deleted{oubli}','The o u b l i sequence is crossed out before the next line F C(V).','oubli','omission','high',False,True)
ch('ellipsis length','four points','three-point ellipsis','four points','Four equally spaced baseline dots occur before the closing parenthesis.','dots','misread symbol or index','high',False,True)
for place,cr,shows in [('base-change arrow','hominline','The long irregular horizontal stroke and right head connect the two typed groups.'),('pair arrow','pair','An uneven freehand shaft and rightward point lie between the typed groups.'),('diagonal mapping symbols','ic','The initial lambda, mapping shaft and its initial bar, and both argument lambdas are handwritten among typed i symbols and parentheses.'),('rational arrow','rational','The long freehand shaft and rightward head are distinct from typed i, G and m.')]:
 ch(place,'handwritten','no hand distinction','handwritten',shows,cr,'other','high',False,True)
ch('sign after i1i2',r'\unsure{\doteqdot|\div|=}',':',r'\unsure{\doteqdot|=}','Two horizontal bars are visible, with an upper rounded trace and lower dark oval. Two bars exclude division and a plain colon; the additional traces may be dots or residual overprint, so dotted and ordinary equality remain alternatives.','eqsign; ic','misread symbol or index','low',True,True,False,True)
ch('defined over Q quotation marks','double quotes','guillemets','double quotes','The opening and closing marks are each two raised vertical strokes.','definedquote','misread symbol or index','high',False,True)
ch('pré- insertion status','inserted','editorially supplied','inserted','The typed p r é and hyphen are visibly raised above the line before structure, with a physical guide beneath.','pre','insertion or placement','high',False,True)
ch('final de','de','des','de','A d with tall hooked stem and a single e are followed by a blank before V; there is no third s cell.','de; bottom','misread word','high',False,True)
ch('left margin trace','omitted','omitted','short curved trace drawn','A small rising two-part ink stroke lies left of the centrality paragraph.','tick','drawing or diagram','medium',True,True)
ch('folio','comment only','administrative page105','mspage105','The lower-left handwritten figures read105.','folio','insertion or placement','high',True,True)
r.doubt('first line admet',r'\rlap{m}d','d','low','Additional low stems in the first overlapped cell do not fully separate from d; the next d/m cell is clearer.')
r.doubt('before NB','(','','low','Overlapping curves do not establish the original struck or overtyped character.')
r.doubt('first Galois capital',r'\mathbb{G}','G','low','Possible self-overstrike; the displaced upper body remains incomplete.')
r.doubt('diagonal-map separator',r'\doteqdot','=','low','Two bars are clear, but the upper and lower traces may belong to a prior impression instead of intentional dots.')
r.notation('rational Q','single typewriter Q with separate underline at all nine occurrences','10/106')
r.notation('tensor product','crossed oval resolved as otimes; three separately inspected instances','10/106 first tensor, prefix and F C formula')
r.notation('conjugate V','short handwritten bar covers V only, not the superscript p,q','10/106 condition b')
r.notation('typed Galois capital','qualified possible repeated G / single G at first occurrence; second occurrence ordinary G','10/106','unresolved')
r.notation('diagonal-map separator','doteqdot / =; two bars with unresolved upper and lower traces','10/106','unresolved')
r.notation('typewriter overlapping cells','admet has d/m overlap and qualified m/d; structure has c/u and u/c overlaps','10/106')
r.r['abbreviations']=[dict(abbreviation='i.e.',expansion='id est',attestations='10/106'),dict(abbreviation='NB',expansion='nota bene',attestations='10/106')]
r.r['inventory_overrides']={'continuation':{'first_words_or_objects':'i.e. que la filtration; overlapping admet'},'definition underline':{'first_words_or_objects':'pré-str c/u u/c ucture de Hodge; physical overlap'},'definition paragraph':{'first_words_or_objects':'3) Appelons; first tensor sign resolved, conjuguaison, first Galois capital qualified'},'diagonal map':{'first_words_or_objects':'i_C=i_1i_2, qualified doteqdot / =, lambda mapsto'}}
extras=[('admet','first line','d/m and qualified m/d overlaps','text','typewriter'),('str','heading','c/u and u/c overlaps','text','typewriter'),('Galois','middle','qualified repeated G / G','text','typewriter')]
for ident,pos,txt in [('schema','above groupes','lower enclosure and central pointer'),('pro','before H','lower guide with left descending end'),('V','after vectoriel','rising diagonal guide'),('F','after oubli','curved insertion guide'),('tensor','before sous-catégorie','curved insertion guide'),('commutent','after homomorphismes','lower loop and pointed end'),('pre','before final structure','short curved guide')]:extras.append((ident+'guide',pos,txt,'drawing','unnamed hand'))
extras += [('tick','left of centrality paragraph','short rising curved trace','drawing','unnamed hand'),('folio','lower left','105','margin note','unnamed hand')]
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:106',sheet_kind='typescript',hand=hand,element='106-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops106.json').read_text())
r.r['inspection_note']='Whole image and both halves viewed before C/H, three C doubt loci and inventory. All55 crop recipes displayed successfully, including a rotated commuting insertion. Nine initially truncated bottom outputs were repeated and inspected successfully. Additional enlargements distinguished physical letter overlaps, checked the ordinary category spellings and second Galois, and separated the short V bar from the long previous-line underline. Every agreed prose line, index, alphabet, arrow, equality, quotation, deletion and insertion was checked in ink. First tensor doubt resolved from crossed strokes; the NB opening stays qualified; the equality alternatives narrowed by its two bars. Additional first-cell admet and first Galois uncertainties remain explicit. All nine Q bodies individually checked. Seven insertion guides, a margin trace and folio added to inventory and text. No OCR, parallel transcription, compilation, context access or mathematical correction.'
r.save('work/record106.json')
