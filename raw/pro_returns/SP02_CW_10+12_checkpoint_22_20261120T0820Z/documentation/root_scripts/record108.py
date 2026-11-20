from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-07',10,108);ch=r.change
r.edit(r'\scanpage{108}',r'\scanpage{108}'+'\n'+r'\mspage{107}')
r.edit('% archive sheet number: 107','')
r.edit('indication sérieuse','indicationsérieuse')
r.edit(r'\deleted{désigné}',r'\deleted{de degré}')
r.edit('Frobenius',r'\rlap{f}Frobenius')
r.edit(r'H^*(X_o',r'H^{\handwritten{*}}(X_o')
r.edit(r'\inserted{$\unsure{\otimes|\Omega}$-}',r'''\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]
\node[anchor=base west] at (0,.45) {$\unsure{\otimes|\Omega}$-};
\draw (-.35,.2) .. controls (.1,.15) and (.8,-.05) .. (1.25,-.5) .. controls (1.8,.2) and (2.2,.65) .. (2.5,1.15);
\end{tikzpicture}}''')
r.edit(r'\inserted{$\underline{C}$}',r'''\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]
\node[anchor=base west] at (0,.5) {$\underline{C}$};
\draw (-.35,.2) .. controls (0,.35) and (.25,-.2) .. (.45,-.8) .. controls (.75,-.2) and (1.1,.4) .. (1.7,1.2);
\end{tikzpicture}}''')
r.edit(r'\inserted{lisse}',r'''\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]
\node[anchor=base west] at (0,.5) {lisse};
\draw (.1,-.7) .. controls (.2,-.25) and (.5,.1) .. (1,.15) .. controls (2.3,.25) and (3.3,.25) .. (3.5,.5) -- (3.55,.9);
\end{tikzpicture}}''')
r.edit('variété projective réelle',r'variété project\rlap{\raisebox{1.1ex}{\tikz[x=1em,y=1em]{\draw (0,0)--(0,.12) (0,.2)--(.01,.33) (.01,.43)--(.02,.49);}}}ive réelle')
r.edit("à l'automorphisme du foncteur",r"\margin{\tikz[x=1em,y=1em]{\draw (0,0) .. controls (.08,.02) and (.15,.13) .. (.2,.25);}}à l'automorphisme du foncteur")
ch('varéiét spelling','varéiét',r'\uncertain{varéiét}','varéiét','The typed order is v a r é i é t, with two distinct rising accents. No character is obscured at enlargement.','vareiet','other','high',False,True,True)
ch('NB','NB','N.B.','NB','The two capital bodies are adjacent, with no periods after either letter.','NB','abbreviation expanded or spelling modernised','high',False,True)
ch('espèrer','espèrer','espérer','espèrer','The accent above the first e after p falls from upper left to lower right; its small rising terminal does not turn it into an acute accent.','esperer','abbreviation expanded or spelling modernised','high',False,True)
ch('doncune spacing','doncune','donc une','doncune','The n and c are close/partly overlapping, and c is followed directly by the u character cell, without an intervening blank cell.','doncune','other','high',False,True)
ch('equivalence arrow','handwritten right arrow','right arrow without hand distinction','handwritten right arrow','An irregular thick shaft and a freehand right head lie after the separately underlined C.','arrow','other','high',False,True)
ch('indication spacing','indication sérieuse','indication sérieuse','indicationsérieuse','The final n is immediately followed by s at the ordinary character-cell spacing. By contrast a full blank separates sérieuse and dans.','indication; toprest; serieusedans','other','high',True,True)
ch('pré deletion',r'\deleted{pré} structures','pré-structures',r'\deleted{pré} structures','All three letters p r é carry cancelling x strokes. A blank, without a hyphen, precedes structures.','pre','deletion state','high',False,True,False,True)
ch('En fait cancellation',r'\deleted{En fait,}','omitted',r'\deleted{En fait,}','E n, the blank cell, f a i t and the comma are crossed with typed x marks; the comma descends below the last x.','enfait','omission','high',False,True)
ch('tensor-prefix insertion and doubt',r'\inserted{$\unsure{\otimes|\Omega}$-}',r'\supplied{$\otimes$-}',r'\inserted{$\unsure{\otimes|\Omega}$-}','A raised rounded sign has an interior cross but an interrupted lower oval with foot-like ends. The ink supports tensor first, but Omega remains a graphic alternative; a hyphen is visibly typed after it.','tensorinsert; tensor2; tensor3','insertion or placement','medium',False,True,False,True)
for place,cr,shows in [('tensor-prefix guide','tensorinsert','A shallow left curve descends to a point before catégorie and rises diagonally to the right.'),('C-insertion guide','Cinsert','A small left curl descends below the line and rises diagonally just before de.'),('lisse insertion guide','lisse','The curved guide descends on the left before complexe and runs below lisse to a short upward hook on the right.')]:
 ch(place,'omitted','omitted','guide drawn',shows,cr,'drawing or diagram','high',True,True)
ch('possessive overwritten letter',r's\deleted{\unsure{e}}a','sa',r's\deleted{\unsure{e}}a','A faint curved body with a possible mid-bar remains beneath the live a. Its merging strokes do not settle the former e; C doubt is retained.','possession','omission','low',False,True)
ch('possessive final s',r'\deleted{s}','omitted',r'\deleted{s}','The separate final cell carries x strokes over a residual curved s, after the corrected a.','possession','omission','medium',False,True)
ch('structure final s',r'structure\deleted{s}','structure',r'structure\deleted{s}','A distinct final s cell remains visible under a full x after the e.','structure','omission','high',False,True)
ch('cancelled second structure',r'i_1\deleted{,\unsure{i_2}}','i_1',r'i_1\deleted{,\unsure{i_2}}','After i1 there is a descending comma, an upper dotted stem and a lower character almost covered by two x impressions. The proposed i2 is retained with doubt rather than inferred from the last line.','i2','omission','low',False,True,False,True)
ch('cancelled que',r'\deleted{que}','omitted',r'\deleted{que}','The q descender, u bowl and e bar survive beneath three cancelling x impressions.','que','omission','high',False,True)
ch('cancelled (plus',r'\deleted{(plus}','omitted',r'\deleted{(plus}','The opening curved parenthesis and p l u s bodies are separately discernible beneath cancellation.','plus','omission','high',False,True)
for place,cr,final in [('complexe quotation','complexe',"``complexe''"),('real Hodge quotation','realquote',"``structure de Hodge réelle''"),('Frobenius quotation','Frobquote',"double quotes around élément de Frobenius à l'infini")]:
 ch(place,'double quotes','guillemets',final,'Each endpoint has a pair of high short vertical marks, with no angled guillemet strokes.',cr,'misread symbol or index','high',False,True)
for place,cr in [('real-model index','Xreal'),('Betti source index','bettimap'),('Betti argument index','bettimap'),('last X index','lastX')]:
 ch(place,'X_o','X_0','X_o','The lowered character is the short round lowercase o; it is visibly smaller than a full-height numeral zero.','%s'%cr,'misread symbol or index','high',False,True,False,True)
ch('X_o.On spacing',r'X_o$.On',r'X_0$. On',r'X_o$.On','The point is directly followed by the capital O at the next normal character position, without an empty typed cell.','Xreal','other','high',False,True)
ch('projective upper trace','omitted','omitted','short broken vertical trace drawn','Three short separated vertical ink segments rise above the dot of i in the second projective. No additional letter is inferred.','projectiveMark','drawing or diagram','medium',True,True)
ch('infinity index','handwritten infinity','infinity without hand distinction','handwritten infinity','The two adjoining irregular loops are written below and to the right of the typed f.','fi','other','high',False,True)
for place,cr in [('G field','GQ'),('Betti coefficient field','bettimap')]:
 ch(place,'plain underlined Q','underlined blackboard Q','plain underlined Q','There is one faint typed oval with a descending tail and a distinct dark underline; no displaced second Q body is present.',cr,'misread symbol or index','high',False,True,False,True)
ch('cancelled wording before order',r'\deleted{désigné}',r'\struck{de degré}',r'\deleted{de degré}','The first two letters are d e, followed by a blank covered with x, then d e g r é. The second d ascender and the g descender exclude désigné.','designe','misread word','high',True,False,False,True)
ch('Frobenius initial overlap','Frobenius','Frobenius',r'\rlap{f}Frobenius','The capital top bar is above a separate bowed lower-case f head; the stem and lower serif overlap. Both letter forms are retained without asserting their order.','Frobenius; Frobquote','omission','medium',True,True)
ch('Betti arrow','handwritten mapsto','mapsto without hand distinction','handwritten mapsto','The uneven shaft, right head and broken initial upright are freehand between the typed X_o and H.','bettimap','other','high',False,True)
ch('cohomology star hand','plain star','plain star','handwritten/retraced star','The long lower-left and short lower-right rays have thick uneven pen contours extending from a lighter central cluster; they are retained as a handwritten star.','star','other','medium',True,True)
ch('conjugation arrow','handwritten mapsto','mapsto without hand distinction','handwritten mapsto','The irregular shaft and curved head have a separate initial upright between the typed x bodies.','conjmap','other','high',False,True)
ch('conjugation bar','handwritten x bar','bar without hand distinction','handwritten x bar','The short uneven horizontal pen rule lies over the final x alone.','conjmap','other','high',False,True)
ch('left margin trace','omitted','omitted','short curved trace drawn','A small ascending freehand stroke lies just left of the Betti-functor line.','tick','drawing or diagram','medium',True,True)
ch('folio','comment only','administrative page107','mspage107','The pale lower-left handwritten figures read107.','folio','insertion or placement','high',True,True)
r.doubt('inserted tensor prefix',r'\otimes',r'\Omega','medium','Interior diagonals support tensor; the interrupted lower oval and separated feet leave the graphic alternative open. Later matching signs use the first candidate.')
r.doubt('possessive under a','e','','low','The faint former curved body and possible crossbar merge with the live a and cancellation.')
r.doubt('deleted second structure',r'i_2','','low','The dotted upper stem is visible, but the lower index is largely hidden by cancelling x impressions.')
r.notation('tensor category sign','crossed rounded sign with interrupted lower oval; tensor / Omega retained at first occurrence, tensor thereafter','10/108 three occurrences','unresolved')
r.notation('rational Q','single plain typed Q and separate underline at both occurrences','10/108')
r.notation('base model subscript','short round lowercase o, not full-height zero, in all four X_o instances','10/108')
r.notation('Frobenius initial','overlapping lower-case f and capital F represented together','10/108')
r.r['abbreviations']=[dict(abbreviation='NB',expansion='nota bene',attestations='10/108')]
r.r['inventory_overrides']={'désigné cancellation':{'first_words_or_objects':'de degré (cancelled)'},'possessive overwritten letter':{'first_words_or_objects':'qualified e beneath a'},'second structure':{'first_words_or_objects':'comma and qualified i_2, cancelled'},'tensor prefix':{'first_words_or_objects':'qualified tensor / Omega prefix and hyphen'}}
extras=[('tensor-guide','before catégorie','descending then rising insertion guide','drawing','unnamed hand'),('C-guide','before de pré-structures','V-like curved insertion guide','drawing','unnamed hand'),('lisse-guide','before complexe','curved lower guide and upturned right end','drawing','unnamed hand'),('projective-trace','above second projective i','broken short vertical trace','drawing','unnamed hand'),('F-overlap','Frobenius initial','overlapping f and F','text','typewriter'),('star','above H','handwritten/retraced asterisk','insertion','unnamed hand'),('tick','left of Betti line','short ascending curved stroke','drawing','unnamed hand'),('folio','lower left','107','margin note','unnamed hand')]
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:108',sheet_kind='typescript',hand=hand,element='108-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops108.json').read_text())
r.r['inspection_note']='Whole page then both halves viewed before C/H and C doubts/inventory. All40 crops successfully displayed and inspected; six crops in the initially truncated batch were repeated before decisions. Every agreed line, alphabet, subscript, quotation, deletion, insertion and mathematical sign read in ink. All three C doubts retained with explicit graphic reasons; cancelled de degré corrects C to H. Missing word spacing, f/F overlap, star hand, three guides, two small traces and folio checked and recorded. The space before dans was separately enlarged and retained. No OCR, parallel transcription, compilation, context access or mathematical correction.'
r.save('work/record108.json')
