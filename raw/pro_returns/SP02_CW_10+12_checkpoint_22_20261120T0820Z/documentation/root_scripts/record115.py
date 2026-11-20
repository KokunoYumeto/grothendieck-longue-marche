from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-08',10,115);ch=r.change
r.edit(r'\scanpage{115}',r'\scanpage{115}'+'\n'+r'\mspage{114}')
r.edit('% archive sheet number: 114','')
r.edit(r'opérations $\otimes$',r'opérations $\unsure{\otimes|\Omega}$')
r.edit(r'Relations entre $\otimes$-catégories',r'Relations entre $\otimes$\deleted{-}catégories')
r.edit(r'\deleted{\unsure{Group}}',r'\deleted{Group}')
r.edit('mixtes',r'm$\mathbb{i}$\rlap{c}xtes')
r.edit(r'\uline{Exemples nombreux et divers.}',r'\rlap{\raisebox{-1.2ex}{\tikz[x=1em,y=1em]{\draw (3,0)--(4.4,.8);}}}\uline{Exemples nombreux et divers.}')
r.edit('(2.8,1.15);','(2.8,1.15) .. controls (2.95,1.2) and (3,1.05) .. (2.95,.95);')
r.edit('termes de gerbes.',r'termes de \rlap{G}gerbes.')
r.edit(r'\unsure{8hapitre|Chapitre}',r'\unsure{\rlap{C}8|8|C}hapitre')
r.edit('Structures de Hodge',r'Structures de Ho\rlap{t}dge')
r.edit('cas non commutatif',r'cas \unsure{n-|non} commutatif')
r.edit(r'sur variantes pour catégories \uline{triangulées}',r'sur \unsure{variantes|variante|variant} pour catégories triangulées')
r.edit(r'\unsure{gr.poïdes|g.poïdes}',r'g.poïdes')
r.edit(r'$\otimes$ ----}',r'''$\otimes$ ----}

\margin{\handwritten{\figure{\begin{tikzpicture}[x=1em,y=1em]
\draw (0,2.2) .. controls (.05,1.8) and (-.05,1.3) .. (.3,1.05) .. controls (.6,.9) and (.9,.85) .. (1,.95);
\draw (.85,0) .. controls (.95,-.2) and (1.03,-.3) .. (1.18,-.4);
\end{tikzpicture}}}}''')
ch('first typed tensor sign','otimes','otimes',r'\unsure{\otimes|\Omega}','A crossed interior lies inside the rounded upper arch, whose lower ends have prominent feet and do not establish a fully closed separate oval. The same graphic form occurs at the four later typed tensor prefixes, each enlarged.','tensor1; tensor2; tensor5; tensor6; tensor7','misread symbol or index','medium',True,True,False,True)
ch('Appendix terminal points','five points','ellipsis','five points','Five separately spaced small pen points follow bigèbres.','appendix; appendixword','misread symbol or index','high',False,True)
ch('chapter2 hyphen','live hyphen','live hyphen',r'\deleted{-}','The short horizontal hyphen is crossed by the two oblique strokes of a typed x, unlike the uncrossed hyphens in later headings.','tensor2','deletion state','high',True,True)
ch('chapter2 cancelled word',r'\unsure{Group}','Groupe','Group','The five cells preserve G r o u p under the x strokes, ending at the p descender; the next cell is blank before Dualité.','Group','misread word','medium',True,True)
ch('mixtes repeated i','mixtes','mixtes',r'm$\mathbb{i}$\rlap{c}xtes','Two offset vertical i stems and displaced dots are visible before the next cell; the self-overstrike is recorded by the prescribed blackboard convention.','mixtes; mixtesi','misread symbol or index','medium',True,True)
ch('mixtes c/x overlap','x only','x only',r'\rlap{c}x','An open curved c body remains between the crossed x strokes in the same typed cell. The overlap notation does not assign chronology.','mixtes','misread symbol or index','high',True,True)
ch('connexions points','four points','ellipsis','four points','Four round typed points stand before the closing parenthesis.','dots','misread symbol or index','high',False,True)
ch('chapter2 parenthesis placement','separate indented line','same paragraph','separate indented line','The parenthesis starts on its own line far to the right under the end of the chapter2 text.','typedtop','insertion or placement','high',False,True)
ch('chapter3 underlines','two underlines','omitted','two underlines','Two long pencil curves run separately beneath the two phrases.','underlines','omission','high',False,True)
ch('chapter3 extra slant','omitted','omitted','short rising slant drawn','A separate diagonal pencil stroke rises beneath Exemples, above the long lower line.','underlines','drawing or diagram','medium',True,True)
ch('left pencil drawing','four-path drawing','omitted','four-path drawing with curled lower endpoint','The paired upper diagonals, long bent descent, separate small inner curve and separate lower rising curve are all visible. The right end of the lowest curve hooks slightly down.','margin','drawing or diagram','high',True,True)
ch('gerbes capital/lowercase overlap','gerbes','gerbes',r'\rlap{G}gerbes','The first cell combines a capital G bowl and inner horizontal bar with the lowered loop of g.','gerbes','misread symbol or index','high',True,True)
ch('chapter8 initial doubt',r'\unsure{8hapitre|Chapitre}','Chapitre',r'\unsure{\rlap{C}8|8|C}hapitre','Two closed lobes match the following numeral8; heavy upper-right and lower-right ends also resemble the C in the other headings. The possible overlap remains qualified.','chapter8; chapter8compare','misread symbol or index','medium',True,True)
ch('chapter8 Hodge overlap','Hodge','Hodge',r'Ho\rlap{t}dge','The d bowl and stem share a cell with an additional tall t stem, lateral top bar and curved lower foot.','Hodge; Hodged','misread symbol or index','medium',True,True)
ch('first handwritten note doubt',r'\unsure{Armature}','structure',r'\unsure{Armature} retained','The high triangular initial with crossbar, following r-shaped turn, low joined middle and tall t favour the tentative C reading, but the compressed middle does not settle the whole word. H structure is not supported by a distinct initial str sequence.','note1; armature','misread word','low',False,True)
ch('non abbreviation','non','non',r'\unsure{n-|non}','After cas, a short rising-and-falling letter is followed by a separate low horizontal dash; three distinct letters n o n cannot be resolved.','non','abbreviation expanded or spelling modernised','medium',True,True)
ch('noncommutative quotation','double quotes','guillemets','double quotes','The opening is two short nearly vertical strokes; the closing pair is likewise raised, without angular guillemet forms.','note1; non','misread symbol or index','high',False,True)
ch('second handwritten note opening','Un autre sur','Un autre, une','Un autre sur','There is no comma after autre. The next joined word has a low initial curve, u-like trough and final r-shaped exit; no initial u/n/e sequence is present.','note2; note2words','misread word','high',False,True)
ch('variantes ending','variantes','variante',r'\unsure{variantes|variante|variant}','The stem reads variant, but the compressed descending terminal stroke does not resolve a separate e and s at full enlargement. The prior plural reading remains tentative.','note2; variantes','misread word','low',True,True)
ch('triangulées supposed underline',r'\uline{triangulées}','triangulées','triangulées','The long lower stroke is continuous with the g descender, looping left and ending under the earlier letters; there is no independent underline.','triangle; note2','other','high',True,False)
ch('g.poïdes abbreviation doubt',r'\unsure{gr.poïdes|g.poïdes}','gpoïdes','g.poïdes','The g is followed by its exit stroke and a distinct point before p; no independent r body is resolved.','gpoides','abbreviation expanded or spelling modernised','medium',True,True)
ch('final loi ending','deux loi','deux lois','deux loi','The final dotted i turns down and ends; the following blank separates it from the circled plus. There is no final s.','note5; loi; twosigns','abbreviation expanded or spelling modernised','high',False,True)
ch('bottom handwriting placement','three lower paragraphs','marginal notes','three lower paragraphs','The three additions occupy successive broad lines below chapter9, in the central text area, with the last addition continuing over three lines.','note1; note2; note3; note4; note5','insertion or placement','high',False,True)
ch('lower right traces','omitted','omitted','two curved traces drawn','In the blank lower-right area there is a long descending curve turning right, and a detached short oblique curve lower down.','bottomtrace','drawing or diagram','medium',True,True)
ch('folio','comment only','administrative page114','mspage114','The lower-left handwritten figures read114.','folio','insertion or placement','high',True,True)
r.doubt('first typed tensor prefix',r'\otimes',r'\Omega','medium','Crossed arch with foot-like lower ends; all five typed occurrences enlarged.')
r.doubt('chapter8 initial',r'\rlap{C}8','8; C','medium','Two lobes plus heavy right ends leave an overlap possible.')
r.doubt('first handwritten note','Armature','','low','Initial A-like form is clear, but joined middle remains compressed.')
r.doubt('first handwritten note after cas','n-','non','medium','Letter-like start followed by detached horizontal dash.')
r.doubt('second handwritten note','variantes','variante; variant','low','Terminal es cannot be separated from the t exit stroke.')
r.notation('typed tensor prefix','crossed arch with feet; tensor / Omega first, first candidate later','10/115','unresolved')
r.notation('typed overlaps','self-overstrike i as mathbb; c/x, G/g and t/d as physical overlaps without chronological assertion','10/115')
r.notation('handwritten operations','circled cross twice; circled plus in final line','10/115')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10/115') for a,b in [('resp.','respectivement'),('gén.','généralement / général'),('g.poïdes','groupoïdes'),('n-','non (tentative)')]]
r.r['inventory_remove_elements']=['018']
r.r['inventory_overrides']={'005':{'first_words_or_objects':'Group (resolved under cancellation)'},'006':{'first_words_or_objects':'structures mixtes with repeated i and c/x overlap; four points'},'014':{'first_words_or_objects':'qualified C/8 overlap in chapter heading; t/d overlap in Hodge'},'017':{'first_words_or_objects':'Un autre sur variantes (ending qualified); g descender, no underline'}}
extras=[('hyphen','chapter2 tensor prefix','crossed hyphen','deletion','typewriter'),('slant','beneath Exemples','separate rising pencil stroke','drawing','unnamed hand'),('mixtes','parenthesis under chapter2','repeated i and c/x overlap','text','typewriter'),('gerbes','chapter5 final word','G/g overlap','text','typewriter'),('Hodge','chapter8','t/d overlap','text','typewriter'),('bottomtrace','lower right blank','two separated curved traces','drawing','unnamed hand'),('folio','lower left','114','margin note','unnamed hand')]
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:115',sheet_kind='typescript',hand=hand,element='115-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops115.json').read_text())
r.r['inspection_note']='Whole and both halves read before witnesses, four C doubts and inventory. All40 crop recipes viewed; the initially truncated loi/twosigns/bottomtrace/folio batch was repeated successfully. Every agreed typed heading and all handwritten additions read against ink. The three additions were rotated upright. Typed tensor prefixes were reconsidered at higher zoom and given the same qualified first-occurrence treatment as the neighbouring crossed arches; handwritten circled operations remain unqualified. C Group and g.poïdes doubts resolved; initial C/8 and Armature doubts retained/refined; compressed non and variantes newly qualified. C inventory018 is removed because the alleged underline is the continuous g descender, not an independent element. H final editorial heading belongs to the next sheet and is not assigned here. No OCR, parallel transcription, context, compilation or mathematical correction.'
r.save('work/record115.json')
