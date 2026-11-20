from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-08',10,122);ch=r.change
r.edit(r'\scanpage{122}',r'\scanpage{122}'+'\n'+r'\mspage{121}')
r.edit('% archive sheet number: 121','')
r.edit(r'\unsure{!|/|.}',r'\unsure{!|/}')
r.edit(r'Gardons $\otimes$',r'Gardons $\unsure{\otimes|\Omega}$')
r.edit(r'\deleted{ou $\handwritten{\unsure{\phi|\psi}}$}',r'\deleted{en \rlap{\unsure{l}}$\handwritten{\unsure{\phi|\psi}}$e}')
r.edit(r'\deleted{\unsure{tri}}',r'\deleted{tui}')
gnouveau=r'\handwritten{\begin{tikzpicture}[x=.45cm,y=.45cm,baseline=-.2ex]\draw (0,-.32) .. controls (.05,-.04) and (.16,.06) .. (.38,.08)--(1.8,.06) .. controls (2.02,.08) and (2.14,.22) .. (2.16,.45);\end{tikzpicture}}'
r.edit(r'\inserted{\handwritten{nouveau}}',r'\inserted{\handwritten{nouveau}'+gnouveau+'}')
r.edit(r'choix de $\handwritten{\mu}$',r'choix de $\handwritten{\unsure{\mu|\psi}}$')
r.edit(r'\unsure{par}',r'pa\unsure{r}')
r.edit(r'c\deleted{\unsure{a}}oup',r'c\deleted{a}oup')
r.edit(r'il y a\deleted{\unsure{x}}',r'il y a\deleted{\unsure{u|n}}')
r.edit('à} savoir',r'à} \unsure{\rlap{a}s|$\mathbb{s}$}\unsure{\rlap{s}a|$\mathbb{a}$}voir')
r.edit(r'l\deleted{\unsure{es}}',r'l\deleted{es}')
gv=r'\handwritten{\begin{tikzpicture}[x=.5cm,y=.5cm,baseline=-.2ex]\draw (0,-.45) .. controls (-.05,.05) and (.2,.18) .. (.48,.2)--(2.6,.03) .. controls (2.9,.06) and (3.08,.2) .. (3.05,.45);\end{tikzpicture}}'
r.edit(r'\inserted{de $V^o$ dans $C$}',r'\inserted{de $V^o$ dans $C$'+gv+'}')
r.edit(r'Koko\deleted{\unsure{f}}!',r'Koko\rlap{\raisebox{.65ex}{\deleted{\unsure{f}}}}\handwritten{!}')
sep=r'\makebox[0pt][c]{\handwritten{\begin{tikzpicture}[x=.32cm,y=.32cm,baseline=0pt]\draw (0,-.65) .. controls (-.06,.1) and (.03,.4) .. (0,.7);\end{tikzpicture}}}'
r.edit(r'$C$comme',r'$C$'+sep+'comme')
r.edit("% Thin separation stroke between C and comme in the preceding paragraph.\n"+r'\figure{\begin{tikzpicture}[baseline]\draw (0,-.55) .. controls (-.06,.1) and (.03,.4) .. (0,.7);\end{tikzpicture}}','')
r.edit(r"n'y\deleted{\unsure{a}}",r"n'y\deleted{a}")
r.edit(r'en\deleted{\unsure{s}}',r'en\deleted{s}')
r.edit(r'dim\unsure{e|m}nsion',r'di\rlap{e}m\rlap{m}ension')
r.edit(r'avec $\otimes$ \unsure{co.|cr.}',r'avec $\unsure{\ominus|\otimes}$ cr.')
r.edit(r'$G=G_m\unsure{8|\beta|B}$)',r'$G=G_m$')
r.edit(r'avec $\unsure{\psi|\mu}$ de Koko',r'avec $\psi$ \unsure{de} Koko')
r.edit(r'\unsure{gr.duation|graduation}','gr.duation')
r.edit('Pour pallier','8) Pour pallier')
r.edit(r"\unsure{lorsqu'on s'en va dans}","lorsqu'on s'en va dans")
r.edit(r'\unsure{catégori|catégorie}','catégorie')
r.edit(r'd\deleted{\unsure{e}}',r'd\deleted{e}')
r.edit('foncteurs compatibles avec a)b)c)',r'foncteurs compatib\rlap{e}l\rlap{s}es avec a)b)c)')
ggrad=r'\handwritten{\begin{tikzpicture}[x=.48cm,y=.48cm,baseline=-.2ex]\draw (0,-.45) .. controls (-.08,.05) and (.16,.16) .. (.45,.17)--(2.7,.15) .. controls (2.93,.15) and (3.08,.19) .. (3.05,.4);\end{tikzpicture}}'
r.edit(r'\inserted{de modules \unsure{grad|gradués}}',r'\inserted{de modules \unsure{grad|gradués}'+ggrad+'}')
r.edit(r'$\mathbb{C}$ comme',r'$\unsure{\rlap{\(X\)}C|\mathbb{C}}$ comme')
r.edit(r'ce sont \handwritten{l}es',r'ce sont \rlap{d}\handwritten{l}es')
arr=r'\begin{tikzpicture}[x=.6cm,y=.6cm,baseline=-.1ex]\fill (-.12,0) circle (.025);\draw (0,0)--(.85,0);\draw (0,0) .. controls (.3,-.22) and (.62,-.16) .. (.65,.12);\draw (.61,.2)--(.88,0)--(.57,-.23);\end{tikzpicture}'
r.edit(r'C\handwritten{\to}\mathrm{Gradf}',r'C\handwritten{'+arr+r'}\mathrm{Gradf}')
rel=r'\begin{tikzpicture}[x=1em,y=1em,baseline=-.1ex]\draw[line width=.6pt] (0,.32)--(.8,.32);\draw[line width=.8pt] (0,.08)--(.8,.08);\draw[line width=1.2pt] (.33,.08)--(.34,-.08);\draw[line width=.8pt] (.54,.08)--(.55,-.06);\end{tikzpicture}'
r.edit(r'\unsure{=|\equiv}',r'\unsure{'+rel+r'|=|\equiv}')
r.edit(r'\deleted{$\unsure{\handwritten{\pi}_i=0_i|\handwritten{\pi}_i\pi_i=0}$}',r'\deleted{$\unsure{\handwritten{\pi}}_i^2=0,\unsure{\handwritten{\pi}_i|i}$}')
ch('opening category C','plain C','underlined C','plain C','One ordinary C body appears without a detached lower line.','C1','misread symbol or index','high',False,True,False,True)
ch('final punctuation after second G_m',r'\unsure{!|/|.}','period',r'\unsure{!|/}','A long slanted stroke with a lower dark blob and separate upper trace excludes a plain period; exclamation versus slash-like mark remains qualified.','G2bang; G2punct-close','misread symbol or index','medium',True,True)
ch('typed tensor form','otimes','otimes',r'first \unsure{\otimes|\Omega}; five later typed signs take first candidate','The six typed instances have an arch, internal crossed strokes and feet. The handwritten marginal circle is treated separately.','tensor1; toprow; cinsertion-full; cancel-colon; marginall; tensorlast','misread symbol or index','medium',True,True,False,True)
ch('unit 1','underlined 1','plain 1','underlined 1','A separate short horizontal line is visible beneath the numeral.','unit','misread symbol or index','high',False,True,False,True)
ch('large commutor after changeons',r'\unsure{\psi|\mu}','psi',r'\unsure{\psi|\mu} retained','The large fork has two outer rising arms and a central descender. Psi is favored, but the joined strokes leave mu possible. The same large marginal form later uses psi.','change','misread symbol or index','medium',False,True,False,True)
ch('deleted words after changeons','ou plus hand phi/psi','en lui','en, then qualified typed l overlapped by hand phi/psi, followed by e','The first letter has an e bar/curve, followed by an n arch. In the next group the last typed cell is e; a tall type remnant and baseline foot lie under the hand looped letter. No separate ui sequence is visible.','change; change-en; change-phi','misread word','medium',True,True)
ch('canceled hand sign',r'\unsure{\phi|\psi}','omitted',r'\unsure{\phi|\psi} retained over typed l?','The loop and long through-stroke survive the blue cancellation, but its crossing obscures the join.','change-phi','omission','medium',False,True,False,True)
ch('deleted group before utilisant',r'\unsure{tri}','omitted','tui, canceled','The t ascender/crossbar, middle u bottom bowl and two uprights, and dotted i are visible beneath the crosses.','tri; tri-close','misread word','medium',True,True)
ch('nouveau insertion guide','omitted','omitted','local curved guide drawn','A curved line begins between Ce and choix, runs below nouveau and turns upward at the right.','nouveau','drawing or diagram','high',True,True)
ch('smaller commutor after choix',r'\mu','psi',r'\unsure{\mu|\psi}','This smaller hand form has low joined legs and a long diagonal; it is qualified separately from the earlier large fork. The later smaller form after choisir takes mu.','mu2; mu3','misread symbol or index','medium',True,True,False,True)
ch('questions status','baseline type','added questions','baseline type','The word occupies ordinary typewriter cells on the line and has no insertion guide.','questions','insertion or placement')
ch('comma after canceled nulle','comma canceled','comma live','comma canceled','The row of cancellation crosses extends through the comma after nulle.','cancelcar','deletion state')
ch('category V','plain V','underlined V','plain V','The typed V has no separate underline.','V','misread symbol or index','high',False,True,False,True)
ch('right-edge par',r'\unsure{par}',r'pa supplied r le',r'pa\unsure{r}','The p and a are complete; only left portions of the final r survive at the clipped edge. The supplied le has no visible ink.','par; toprow','misread word','medium',True,True,True)
ch('commutativité line break','commutativité','commutati supplied vité','commutativité','The ending vité is fully present at the beginning of the next line; it is not missing or supplied text.','commuti; commutivite','insertion or placement','high',False,True,True)
ch('coup canceled a',r'c deleted unsure a oup','coup','c deleted a oup','The a upper/lower bowls and foot remain visible below the x cancellation.','coup','deletion state','high',True,True)
ch('extra canceled letter after il y a',r'\unsure{x}','omitted',r'\unsure{u|n}, canceled','The X is the cancellation; an underlying pair of uprights and a low bowl favor u, while the obscured upper join leaves n possible.','ax; ax-close','misread word','low',True,True)
ch('right-edge à',r'\unsure{à}','added à',r'\unsure{à} retained','Only a clipped lower-left trace remains after the comma; it is aligned with the type rather than a separate insertion.','uneedge','insertion or placement','low',False,True,False)
ch('savoir first two cells','savoir','savoir','qualified overlapping a/s and s/a; repeated s/a alternatives retained','Both cells have additional inner outlines. The first can be read as a under s and the second as s under a; tightly repeated same letters remain possible. The alternatives are not resolved from the expected word.','savoir; savoir-sa; savoir-sample','misread word','low',True,True)
ch('lespace canceled es',r'\unsure{es}, canceled','omitted','es, canceled','The e bar and curve and s upper/lower curves remain visible under the crosses.','lespace; savoir-sample','deletion state','high',True,True)
ch('espace final canceled s','canceled s','omitted','canceled s','A separate final s cell is crossed after the live espace.','lespace','omission')
ch('V superscript after cohomological expression',r'V^{\unsure{o|0}}','underlined V circle',r'V^{\unsure{o|0}} retained','V has no underline; the small closed oval does not securely distinguish letter o from numeral 0. The inserted V later uses first-candidate o.','coh; Vo; cinsertion-full','misread symbol or index','medium',False,True,False,True)
ch('punctuation after V superscript','comma','semicolon','comma','There is a single comma body and no separate upper point.','commaVo','misread symbol or index')
ch('insertion de V^o dans C','plain V and C','underlined V and C','plain V and C','The long line below the inserted phrase is its connecting guide, not individual category underlines.','cinsertion-full','misread symbol or index','high',False,True,False,True)
ch('guide for de V^o dans C','omitted','omitted','local guide drawn','A line rises from after the tensor sign, runs beneath the inserted phrase and curls up at its right end.','cinsertion-full','drawing or diagram','high',True,True)
ch('à condition emphasis','underlined','plain','underlined','A separate horizontal line runs beneath both words.','condition','other')
ch('C after choisir','plain C','underlined C','plain C','The C body has no lower line.','C2','misread symbol or index','high',False,True,False,True)
ch('Koko ending',r'deleted unsure f then !','period','raised canceled f? overlapped by lower hand !','The canceled typed cluster sits above the baseline, and a thin hand stroke descends from it to the lower dark point. Its f reading remains uncertain; the physical overlap is retained.','kokof; koko-close','insertion or placement','low',True,True)
ch('lorsque on','lorsque on',"lorsqu'on",'lorsque on','The final e of lorsque and a separate following on are both present.','Aprouver','abbreviation expanded or spelling modernised')
ch('C before comme','plain C with separate figure later','underlined C and space','plain C with thin separator drawn inline','A thin vertical hand stroke stands between C and comme, extending above and below the line. It is neither a C underline nor a separate later figure.','Ccomme','drawing or diagram','high',True,True)
ch('canceled a after n\'y',r'\unsure{a}, canceled','omitted','a, canceled','The typed a bowls and right foot survive the cancellation.','ny','deletion state','high',True,True)
ch('C after fibre sur','plain C','underlined C','plain C','No detached bar lies below the ordinary C.','Cfiber','misread symbol or index','high',False,True,False,True)
ch('canceled s after en',r'\unsure{s}, canceled','omitted','s, canceled','Both curved portions of s remain around the crossing strokes.','ens','deletion state','high',True,True)
ch('dimension middle cells',r'dim\unsure{e|m}nsion','dimension',r'di\rlap{e}m\rlap{m}ension','The first cell combines m uprights with an e bowl/bar; the next combines an e with m uprights. These are two physical overlaps, not a choice of only one letter in the second cell.','dimension; dimension-close','misread word','high',True,True)
ch('Cf abbreviation','Cf','Cf.','Cf','No point follows the f before exemple; the surrounding oval and connection are visible.','Cf-upright','abbreviation expanded or spelling modernised')
ch('Cf balloon and note callout','drawing','omitted','drawing retained','The upper oval, descending connecting line and long angular callout enclose and connect the slanted marginal texts.','Cfdraw; marginall; margin-upright','drawing or diagram')
ch('margin foncteurs and extended text','substantially readable','ill after tous les; remainder ill','readable text retained with localized doubts','Upright rotation reveals foncteurs qui sont compatibles, the unitary phrase, torseurs, the underlined clause and the final note. H illegibility is not adopted for these readable groups.','margin-upright; margin-detail','readable ink left as \\ill{}','high',False,True,True)
ch('hand operator in margin','otimes','ill',r'\unsure{\ominus|\otimes}','The small oval encloses a short horizontal stroke; no clear crossing diagonal is visible. Ominus is the ink-led first candidate.','marginall; margin-detail','misread symbol or index','medium',True,True,True,True)
ch('margin abbreviation',r'\unsure{co.|cr.}','ill','cr.','After c there is an angular r-like upstroke and a point, without an o oval.','margin-detail','abbreviation expanded or spelling modernised','medium',True,True,True)
ch('margin opening parenthesis',r'\unsure{(}','ill',r'\unsure{(} retained','A small curved/slanted stroke precedes ils but its punctuation role remains uncertain; no matching final parenthesis is invented.','margin-upright; margin-detail','misread symbol or index','low',False,True,True)
ch('G=G_m marginal ending',r'G=G_m unsure 8/beta/B then )','ill','G=G_m only','The adjacent 8 and closing parenthesis are upright typewriter enumeration, spatially outside the hand formula. They begin the next main paragraph.','enumeration; marginall; margin-detail','text not on the page','high',True,True,True,True)
ch('margin commutor doubt',r'\unsure{\psi|\mu}','ill','psi, first-candidate recurrence','The large fork matches the previously qualified changeons sign; it is not requalified at its later occurrence.','margin-detail; change','misread symbol or index','medium',True,True,True,True)
ch('margin before Koko','de','ill',r'\unsure{de}','The short strokes are partly merged with the underline and adjacent commutor, leaving de plausible but not fully secure.','marginall; margin-detail','misread word','low',True,True,True)
ch('gr.duation abbreviation',r'\unsure{gr.duation|graduation}','ill','gr.duation','A distinct point follows gr before the joined duation strokes; no a is silently supplied there.','margin-upright; margin-detail; margin-bottom','abbreviation expanded or spelling modernised','medium',True,True,True)
ch('paragraph number','omitted','8)','8)','The two upright typed characters stand immediately before Pour; the callout edge passes through the 8 without canceling the number.','enumeration; marginall','omission','high',True,False)
ch('long canceled phrase opening',r"\unsure{lorsqu'on s'en va dans}","lorsqu'on s'en va dans","lorsqu'on s'en va dans",'The ascenders, descender, apostrophes and low letter bodies remain readable beneath the row of crosses.','cancel1; cancel1a; cancel1b','misread word','high',True,False)
ch('first canceled catégorie',r'\unsure{catégori|catégorie}','catégorie','catégorie','The accent and final e curve/bar are visible under the cancellation; the ending is not clipped.','cancel2','misread word','high',True,False)
ch('colon in canceled phrase','none','colon after tensor','none','The crossed cells after the operator do not expose two independent colon points. No such punctuation is supplied; fully covered earlier punctuation cannot be excluded.','cancel-colon','text not on the page','medium',False,True)
ch('canceled e after d',r'\unsure{e}','omitted','e, canceled','The lower rounded body and middle bar remain visible under the X.','dele','deletion state','high',True,True)
ch('compatibles corrected cells','compatibles','compatibles',r'compatib\rlap{e}l\rlap{s}es','One cell combines the tall l with an e bowl and bar; the next combines e and an s-like lower curve. Both overlapping bodies are preserved without assigning revision chronology.','compatibles; compatible-le','misread word','medium',True,True)
ch('de modules insertion placement','before C','after C','before C','The vertical start of the guide falls between catégorie and C, then runs below the added words.','insert','insertion or placement')
ch('clipped inserted grad',r'\unsure{grad|gradués}','gradués',r'\unsure{grad|gradués} retained','Only grad is visible before the right crop edge; the continuation cannot be read from this scan.','insert','misread word','medium',False,True)
ch('de modules guide','omitted','omitted','local guide drawn','The thin line rises at the insertion point before C and runs below the inserted phrase, turning up at the clipped right edge.','insert','drawing or diagram','high',True,True)
ch('C with crossing typed body',r'\mathbb{C}','underlined C',r'\unsure{\rlap{\(X\)}C|\mathbb{C}}','The outer C is crossed by diagonal serif-bearing strokes. A typed X overlap is favored; a repeated C is not secure, and there is no separate underline.','Cdouble; C-over','misread symbol or index','low',True,True,False,True)
ch('des corrected to les','hand l plus es','des','typed d overlapped by handwritten l, followed by es','The blue looped l lies over a typed d whose oval, tall stem and baseline foot remain visible. Both layers are retained.','les','insertion or placement','high',True,True)
ch('quotation marks and emphasis','hand double quotes and underline','angle quotes, plain text','hand double quotes and underline','Two upper strokes occur at each end; a separate line underlies the phrase.','quotes; tordus','other')
ch('C after si','plain C','underlined C','plain C','No lower bar is visible.','Csi','misread symbol or index','high',False,True,False,True)
ch('C before Gradf arrow','plain C','underlined C','plain C','The typed C has no separate underline.','CGradf','misread symbol or index','high',False,True,False,True)
ch('hand arrow shape','right arrow','right arrow','right arrow with curved lower return and left point drawn','A small detached point precedes the arrow, whose shaft has an under-loop/return and triangular right head. The full visible shape is retained.','Gradf; CGradf','drawing or diagram','high',True,True)
ch('relation before D',r'\unsure{=|\equiv}','equals','qualified graphic of two bars with two short lower traces; equals/equiv alternatives','There are two long horizontal bars and two short downward bodies attached below the lower bar; no complete third bar is visible.','relation','drawing or diagram','medium',True,True,False,True)
ch('D body',r'\mathbb{D}','underlined D',r'\mathbb{D}','Two displaced left vertical bodies and doubled curved portions show repeated type; no underline is present.','DX','misread symbol or index','high',False,True,False,True)
ch('D exponent',r'\unsure{\mathbb{X}|X}',r'\mathbb{Z}',r'\unsure{\mathbb{X}|X} retained','Crossing diagonal strokes meet between upper and lower serifs, supporting X rather than Z. Whether the dark central body reflects a second X remains uncertain.','DX','misread symbol or index','medium',False,True,False,True)
ch('où accent','où','ou','où','A distinct grave accent lies above the u.','ou','abbreviation expanded or spelling modernised')
ch('canceled bottom formula',r'\unsure{\pi_i=0_i|\pi_i\pi_i=0}','omitted',r'\unsure{\handwritten{\pi}}_i^2=0,\unsure{\handwritten{\pi}_i|i}, all canceled','A raised typed 2, lower i, equality, oval 0, comma and final lower i are visible beneath crosses and a wavy hand strike. The hand pi bodies remain uncertain; no mathematically expected formula is substituted.','cancelbottom; final-cancel-top; final-cancel-bottom; final-cancel-wide','misread symbol or index','low',True,True,False,True)
ch('H editorial explanatory notes','absent','Koko explanation and claim that slanted note remainder is unreadable','excluded from transcription','These are H editorial notes; no corresponding prose occurs on the sheet. The manuscript words and marginal drawing are transcribed separately from their interpretation.','kokof; marginall','text not on the page','high',False,True)
ch('folio','comment 121','administrative page121','mspage121','Three pencil figures at lower left read121.','folio','insertion or placement','high',True,True)
for args in [
 ('punctuation after second G_m','!', '/','medium','Long slanted stroke with lower blob; plain period excluded.'),
 ('first typed tensor',r'\otimes',r'\Omega','medium','Crossed arch with lower feet; later typed instances take first candidate.'),
 ('large hand commutor',r'\psi',r'\mu','medium','Large forked form; later marginal recurrence uses psi.'),
 ('typed remnant in deleted en group','l','','low','Tall type remnant lies under handwritten sign; final e is clear.'),
 ('deleted hand sign',r'\phi',r'\psi','low','Loop/through-stroke is crossed by cancellation.'),
 ('smaller hand commutor',r'\mu',r'\psi','medium','Low joined legs differ from large fork; later smaller recurrence uses mu.'),
 ('par final r','r','','medium','Right edge clips most of the final character; le is not supplied.'),
 ('canceled letter after il y a','u','n','low','Low bowl favors u but the upper join is crossed.'),
 ('clipped à','à','','low','Only a lower-left fragment survives beyond the comma.'),
 ('savoir first cell','overlapping a and s','repeated s','low','Additional curved/vertical bodies cannot be assigned securely.'),
 ('savoir second cell','overlapping s and a','repeated a','low','Additional inner body remains unresolved.'),
 ('V exponent','o','0','medium','Small closed oval; later occurrence uses o.'),
 ('raised canceled Koko ending','f','','low','Dense raised crossed cluster overlaps lower exclamation.'),
 ('marginal hand operator',r'\ominus',r'\otimes','medium','The oval contains a horizontal stroke without a secure cross.'),
 ('margin opening parenthesis','(','unidentified small curved stroke','low','No matching final parenthesis is reconstructed.'),
 ('margin word before Koko','de','','low','Short strokes merge with underline and neighboring letter.'),
 ('clipped inserted modules word','grad','gradués','medium','Only grad is visible before the edge.'),
 ('crossed C body','C overlapped by X','repeated C','low','Diagonal serif-bearing strokes are visible inside the C.'),
 ('relation before D','two bars and short lower traces drawn','=','medium','Short lower marks do not form a complete third bar; equiv also retained inline.'),
 ('D exponent',r'\mathbb{X}','X','medium','X rather than Z is supported; repetition is not settled.'),
 ('first sign in canceled bottom formula',r'\pi','','low','Crosses and long hand stroke obscure the horizontal top.'),
 ('last sign in canceled bottom formula',r'\pi_i','i','low','The lower i is clear; preceding hand traces may belong to pi or the wavy cancellation.')]:r.doubt(*args)
r.notation('typed tensor sign','six typed crossed arches; first otimes/Omega qualified, later first-candidate tokens','10/122','unresolved')
r.notation('large and small hand commutors','large psi/mu first qualified, smaller mu/psi separately qualified; later matching forms take respective first candidates','10/122','unresolved')
r.notation('hand marginal operator','oval with horizontal interior stroke, qualified ominus/tensor','10/122','unresolved')
r.notation('V exponent','first o/0 qualified; second o by first-candidate rule','10/122','unresolved')
r.notation('repeated type and crossing bodies','D doubled; exponent X possibly doubled; C contains crossing typed body and remains qualified','10/122','partly unresolved')
r.notation('physical letter overlaps','dimension e/m then m/e; compatibles e/l then s/e; hand l over typed d; savoir a/s and s/a qualified','10/122','partly unresolved')
r.notation('canceled formula','raised 2 and comma restored; pi bodies remain qualified; no mathematical normalization','10/122','partly unresolved')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10/122') for a,b in [('car.','caractéristique'),('Cf','confer'),('cr.','unresolved abbreviation'),('comp.','compatibles'),('gr.duation','graduation'),('mod','modulo'),('i.e.','id est'),('Gradf','modules gradués de type fini (contextual label)')]]
r.r['inventory_overrides']={
 '002':{'first_words_or_objects':'qualified hand ! or slash; plain period excluded'},
 '006':{'first_words_or_objects':'en, then typed l? overlapped by hand phi/psi, followed by e; canceled'},
 '007':{'first_words_or_objects':'qualified phi/psi overlapping typed l? in canceled group'},
 '008':{'first_words_or_objects':'tui, canceled; u bowl read'},
 '009':{'first_words_or_objects':'hand nouveau with local curved insertion guide'},
 '011':{'first_words_or_objects':'smaller hand mu/psi, first qualified occurrence'},
 '013':{'first_words_or_objects':'a, canceled after c of coup'},
 '014':{'first_words_or_objects':'qualified u/n under x cancellation'},
 '015':{'first_words_or_objects':'es, canceled between l and apostrophe'},
 '019':{'first_words_or_objects':'de V^o dans C, plain categories, with curved insertion guide'},
 '021':{'first_words_or_objects':'raised canceled f? overlapping lower exclamation'},
 '023':{'first_words_or_objects':'a, canceled after n\'y'},
 '024':{'first_words_or_objects':'s, canceled after en'},
 '025':{'position':'inline between C and comme','first_words_or_objects':'thin vertical handwritten separation stroke'},
 '030':{'first_words_or_objects':'déterminer tous les foncteurs ... qualified ominus/tensor cr. unitaire; G=G_m without spurious 8); underlined clause with psi and de?'},
 '031':{'first_words_or_objects':'seul la gr.duation mod 2 intervient ici !'},
 '032':{'first_words_or_objects':'8) Pour pallier; long cancellation; inserted de modules grad?; overlapped C/X; corrected les'},
 '033':{'first_words_or_objects':"lorsqu'on s'en va dans une catégorie avec tensor la catégorie des; canceled, no independently visible colon"},
 '034':{'first_words_or_objects':'e, canceled in d\'étudier'},
 '035':{'first_words_or_objects':'de modules grad/gradues, inserted before C with local guide'},
 '036':{'first_words_or_objects':'hand l overlapping typed d in des'},
 '039':{'kind':'drawing','first_words_or_objects':'right arrow with lower curved return and small left point'},
 '043':{'first_words_or_objects':'qualified pi_i raised2 equals0 comma qualified pi_i/i; all canceled'},
 '044':{'first_words_or_objects':'first qualified hand pi under cancellation'},
 '045':{'first_words_or_objects':'possible second hand pi before clear trailing i; qualified against i alone'}}
extras=[('guide-nouveau','between Ce and choix','local curved guide for nouveau','drawing','his hand'),('savoir-over','first two cells of savoir','qualified overlapping a/s and s/a, with repeated-letter alternatives','text','typewriter'),('guide-V','after tensor sign','local guide for de V^o dans C','drawing','his hand'),('Koko-bang','below raised canceled group after Koko','lower hand exclamation overlapping raised canceled f?','insertion','his hand'),('dimension-over','middle two cells of dimension','e/m and m/e overlaps','text','typewriter'),('number8','before Pour','8)','text','typewriter'),('compatible-over','last internal cells of compatibles','e/l and s/e overlaps','text','typewriter'),('guide-grad','before C after catégorie','local guide for de modules grad','drawing','his hand'),('C-over','before comme ci-dessus','qualified crossing C/X body versus repeated C','text','typewriter'),('d-under-l','under handwritten l in les','typed d body retained under l','text','typewriter'),('relation-traces','before D exponent X','two bars with short downward traces, qualified','drawing','typewriter'),('folio','lower left','121','margin note','unnamed hand')]
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:122',sheet_kind='typescript',hand=hand,element='122-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops122.json').read_text())
r.r['inspection_note']='Root viewed whole122 then both halves, C/H, all26 C uncertainty fields and45 C inventory items. All87 crops were actually viewed, including upright rotations of both slanted marginal notes. An initially truncated enumeration/cancel1/cancel1a/cancel1b output was repeated successfully. The change-en crop clips n; complete change and change-phi crops were reread. The margin-bottom crop clips the gr.duation continuation, supplied by the complete upright/detail crops. All agreed words, signs, indices, deletions, marginal marks and insertion guides were checked against ink. No OCR, parallel transcription, context, compilation or mathematical checking. No123 image opened before finalization.'
r.save('work/record122.json')
