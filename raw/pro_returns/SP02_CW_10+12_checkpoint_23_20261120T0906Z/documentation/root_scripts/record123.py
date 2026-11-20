from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-09',10,123);ch=r.change
r.edit(r'\scanpage{123}',r'\scanpage{123}'+'\n'+r'\mspage{122}')
r.edit('% archive sheet number: 122','')
r.edit(r"d'une $\otimes$",r"d'une $\unsure{\otimes|\Omega}$")
r.edit('impliquant',r'\rlap{c}impliquant')
r.edit('pompatible',r'\rlap{p}compatible')
extra_a=r'\begin{tikzpicture}[x=1em,y=1em,baseline=0pt]\draw (.28,.72) .. controls (.26,.58) and (.30,.48) .. (.34,.32);\draw (.56,.34) .. controls (.66,.48) and (.81,.43) .. (.75,.30) .. controls (.71,.21) and (.66,.17) .. (.65,.11);\end{tikzpicture}'
r.edit(r'\unsure{algèbres|Àlgèbres}',r'\unsure{\rlap{'+extra_a+r'}a|a|À}lgèbres')
r.edit(r'\deleted{\unsure{$C\to D$ est}}',r'\deleted{$C\unsure{\to}D$ est}')
r.edit('(et $c$ choisi',r'(et $\unsure{\mathbb{c}|c}$ choisi')
gtensor=r'\handwritten{\begin{tikzpicture}[x=.4cm,y=.4cm,baseline=-.2ex]\draw (0,-.35) .. controls (.10,-.05) and (.20,.20) .. (.38,.42);\end{tikzpicture}}'
r.edit(r'\inserted{\handwritten{$\otimes$}}',r'\inserted{\handwritten{$\otimes$}'+gtensor+'}')
r.edit(r'\unsure{La|Ea}',r'\rlap{C}La')
r.edit(r'\unsure{N.e.|i.e.}',r'\unsure{\rlap{N}i|N}.e.')
r.edit(r'\unsure{làisomorphisme|laisomorphisme}',r"l\rlap{'}aisomorphisme")
r.edit(r'\unsure{muttiplication|multiplication}',r'mu\rlap{l}t\rlap{l}tiplication')
r.edit(r'\deleted{\unsure{respecte}}',r'\deleted{respecte}')
gU=r'\handwritten{\begin{tikzpicture}[x=.45cm,y=.45cm,baseline=-.2ex]\draw (0,-.35) .. controls (-.06,.05) and (.18,.13) .. (.40,.15)--(2.0,.15) .. controls (2.22,.16) and (2.40,.20) .. (2.41,.42);\end{tikzpicture}}'
r.edit(r'\inserted{i.e. de $U$}',r'\inserted{i.e. de $U$'+gU+'}')
r.edit('récupérer le ',r'récupérer l\rlap{e}a ')
r.edit(r'\deleted{\unsure{foncteur au|foncteur}} graduation',r'\deleted{foncteur \unsure{au|du}} \rlap{f}graduation')
r.edit('à vérifier,',r'à $\mathbb{v}$érifier,')
r.edit(r'\unsure{quelc.|quelq.}','quelc.')
r.edit(r'\unsure{graduation}',r'\unsure{gr.duation|graduation}')
r.edit(r'\unsure{arbitrairement}',r'arbit\rlap{r}ai\rlap{r}eement')
r.edit(r'\handwritten{\unsure{soit}}',r'\rlap{es}\handwritten{\unsure{soi}}t')
r.edit(r'\handwritten{9/}',r'\handwritten{9\unsure{/|)}}')
r.edit(r'\deleted{\unsure{b)}}',r'\deleted{b)}')
gfix=r'\handwritten{\begin{tikzpicture}[x=.45cm,y=.45cm,baseline=-.2ex]\draw (0,-.35) .. controls (-.06,.04) and (.17,.12) .. (.44,.14)--(4.5,.12) .. controls (4.8,.14) and (5.0,.20) .. (5.03,.40);\end{tikzpicture}}'
r.edit(r"\inserted{(b) -l'unité - étant \handwritten{\unsure{fixée}}}",r"\inserted{(b) -l'unité - étant \rlap{fix}\handwritten{\unsure{fix}}"+gfix+'}')
r.edit(r'$g\handwritten{\in}U$',r'$\unsure{\mathbb{g}|g}\handwritten{\in}U$')
ghom=r'\handwritten{\begin{tikzpicture}[x=.45cm,y=.45cm,baseline=-.2ex]\draw (0,.28) .. controls (.05,.04) and (.20,.0) .. (.44,.0)--(4.7,.0) .. controls (4.95,.02) and (5.13,.10) .. (5.14,.28);\draw[->] (2.9,0)--(2.95,-.60);\end{tikzpicture}}'
r.edit(r"d'augmentation 1\inserted{\handwritten{(i.e. les hom unitaires $\unsure{g|q}:A\to k$)}}",r"d'augmentation 1,\inserted{\handwritten{(i.e. les hom unitaires $\unsure{g|q}:A\to k$)}"+ghom+'}')
r.edit('condition exprime',r'condition expri\unsure{$\mathbb{m}$|m}e')
r.edit(r'\deleted{\unsure{foncte|foncteur}}',r'\deleted{foncte}')
r.edit(r'\deleted{\unsure{t}}',r'\deleted{t}')
r.edit(r'\deleted{\unsure{(donner exemple}}',r'\deleted{(donner exemple}')
ch('typed tensor glyphs','otimes throughout','otimes throughout',r'first \unsure{\otimes|\Omega}; seven later typed instances use otimes','Eight typed forms have the arch, crossed interior and low feet; the separately inserted handwritten circled cross is clearer and not conflated with them.','tensor1; Delta; xy; MkN; NkM; tensor2; Deltag','misread symbol or index','medium',True,True,False,True)
ch('C after structure','plain C','underlined C','plain C','The C has a single open body without a detached lower line.','C1','misread symbol or index','high',False,True,False,True)
ch('impliquant opening','impliquant','impliquant',r'\rlap{c}impliquant','A c-shaped open curve lies around the dotted i and its upright; both bodies occupy the first cell.','impliquant; impliquant-over','misread word','medium',True,True)
ch('first C to D','plain C and D','underlined C and D','plain C and D','Both typed capitals lack separate underlines; the intervening hand arrow points right.','CD1','misread symbol or index','high',False,True,False,True)
ch('pompatible initial','pompatible','compatible',r'\rlap{p}compatible','The p descender and outer bowl remain together with an inner right-open c curve. Neither single-letter witness reading represents the overlap.','pompatible; pompatible-over','misread word','medium',True,True)
ch('algèbres initial',r'\unsure{algèbres|Àlgèbres}','algèbres','qualified a with extra strokes drawn; a and À alternatives','The ordinary a is visible with a thin rising stroke above it and a small curve to its right. The extra ink does not securely identify another letter or accent; its shape is retained.','algebres; algebres-over','drawing or diagram','low',True,True)
ch('canceled C to D est',r'whole \unsure{$C\to D$ est}',r'\ill{}',r'$C\unsure{\to}D$ est, canceled','The C, D and est can be followed through the crosses; the central connecting mark remains too covered to identify securely.','cancelCD','readable ink left as \\ill{}','medium',True,True,True,True)
ch('C after sur','plain C','underlined C','plain C','No separate line lies beneath the typed C.','C2','misread symbol or index','high',False,True,False,True)
ch('symmétrie','symmétrie','symétrie','symmétrie','Two adjacent m cells precede the accented e.','symmetrie','abbreviation expanded or spelling modernised')
ch('second C to D','plain C and D','underlined C and D','plain C and D','The ordinary capitals have no underline; a handwritten right arrow lies between them.','CD2','misread symbol or index','high',False,True,False,True)
ch('c chosen above','plain c','plain c',r'\unsure{\mathbb{c}|c}','A light displaced upper terminal and lower ending lie to the right of the dark c body, suggesting a second strike; the weaker outline leaves an ordinary c possible.','c2; c2-over','misread symbol or index','medium',True,True,False,True)
ch('hand tensor insertion guide','omitted','omitted','curved rising guide drawn locally','A short curved hand stroke rises between structure and précédente to the inserted circled cross.','tensorinsert','drawing or diagram','high',True,True)
ch('diagonal formula placement','inline','display','inline','The formula follows satisfaisant on the same typewritten line; its punctuation is the sentence period.','Delta','insertion or placement')
ch('La first cell',r'\unsure{La|Ea}','La',r'\rlap{C}La','An outer C curve and an inner L upright and foot occupy the same cell, followed by a.','La','misread word','medium',True,True)
ch('long cancellation opening','revient à canceled','revient à live','revient à canceled','Cancellation strokes begin at revient and continue through the following long clause.','cancelboundary','deletion state')
ch('canceled N.e. first cell',r'\unsure{N.e.|i.e.}','i.e.',r'\unsure{\rlap{N}i|N}.e.','The N diagonals remain with a possible central i upright/dot; the cancellation prevents a secure separation of the two. The two points and e are visible.','Ne; Ne-over','misread word','low',True,True)
ch('first homogeneous module index',r'{}_iM=M',r'\pi_iM=M',r'{}_iM=M','The low i immediately precedes M; no pi body occupies the blank above or before it.','iM','misread symbol or index','high',False,True,False,True)
ch('second homogeneous module index',r'{}_jN=N',r'\pi_jN=N',r'{}_jN=N','A low j precedes N without a visible pi.','Nj','misread symbol or index','high',False,True,False,True)
ch('canceled isomorphism word',r'\unsure{làisomorphisme|laisomorphisme}',"l'isomorphisme",r"l\rlap{'}aisomorphisme",'A separate a body occupies the cell under an apostrophe-shaped upper stroke; it is not a grave-accented a alone and is not absent.','laiso','misread word','medium',True,True)
ch('between tensor expressions','blank',r'\mapsto','blank','The area between y and the parenthesized minus one has no shaft or arrowhead, despite visible neighboring cancellation strokes.','xy','text not on the page','high',False,True,False,True)
ch('degree phrase quotation marks','double quotes','guillemets','double quotes','Paired upper strokes enclose the typed phrase; no angular guillemets are drawn.','Ucanceled; Ucancelend','other')
ch('canceled U formula',r'U^i\unsure{=\pi_j|=\sum_j}',r'\ill{}',r'U^i\unsure{=\pi_j|=\sum_j} retained','U and its high i are readable, as is the low terminal j. The middle group is obscured by crossings, so the two C alternatives remain unresolved.','Ucanceled','readable ink left as \\ill{}','low',False,True,True,True)
ch('first anticommutative emphasis','only anti underlined','whole word italic','only anti underlined','A separate line ends under anti, before commutative.','anti1','other')
ch('multiplication middle cells',r'\unsure{muttiplication|multiplication}','multiplication',r'mu\rlap{l}t\rlap{l}tiplication','The third and fourth cells each show a tall l stem/top serif and a t crossbar in the same cell. Both physical overlaps are retained.','multiplication; multiplication-over','misread word','medium',True,True)
ch('canceled respecte',r'\unsure{respecte}',r'\ill{}','respecte, canceled','The r, e, s, p descender, e, c opening, t ascender and final e survive beneath the crosses.','respecte','readable ink left as \\ill{}','high',True,True,True)
ch('second anticommutative emphasis','underlined','italic','underlined','The separate underline extends across the end of one line and the continuation on the next; the line-end hyphen is joined.','anti2; anticomm2','other')
ch('i.e. de U position','after graduation de A','margin after preceding sentence','after graduation de A','The insertion guide begins immediately after A in the graduation clause and passes below the added words.','Uinsert','insertion or placement','high',False,True,False,True)
ch('i.e. de U guide','omitted','omitted','local curved guide drawn','A line dips after A, runs beneath the insertion, and curls upward at its right.','Uinsert','drawing or diagram','high',True,True)
ch('article before canceled foncteur','le','la',r'l\rlap{e}a','The final cell contains an e bar and curved body together with the a bowl and right foot.','le','misread word','medium',True,True)
ch('canceled foncteur phrase',r'\unsure{foncteur au|foncteur}',r'\ill{}',r'foncteur \unsure{au|du}, canceled','Foncteur is legible under the row of crosses, and two further cells are present. The first has an a-like bowl but its upper part is obscured; au is favored over du without omitting the group.','foncteureau; cancel-du','readable ink left as \\ill{}','medium',True,True,True)
ch('graduation opening after cancellation','graduation','graduation',r'\rlap{f}graduation','A tall f ascender and crossbar overlie the g bowl and descender, outside the canceled phrase.','foncteureau; foncteureau-end','misread word','high',True,True)
ch('margin vérifier v','vérifier','vérifier',r'$\mathbb{v}$érifier','Two displaced V-shaped strokes are visible in the typed initial v, beyond a merely dark single body. The line-end hyphen is joined.','marginall; marginupright','misread word','medium',True,True)
ch('margin comma','comma after vérifier','no comma','comma','A low hooked point follows vérifier before the handwritten parenthesis.','marginall; marginupright','other')
ch('margin groupe',r'\unsure{groupe}',r'\ill{}',r'\unsure{groupe} retained','After gr the connected low undulations and a descender support groupe, but the letter joins remain blurred even upright.','marginhand','readable ink left as \\ill{}','low',False,True,True)
ch('margin de or des',r'\unsure{de|des}',r'\ill{}',r'\unsure{de|des} retained','The looped d and low ending are visible, but the number of terminal strokes is uncertain.','marginhand','readable ink left as \\ill{}','low',False,True,True)
ch('margin classes',r'classes',r'\ill{}','classes','The c, tall l, a and paired s bodies are readable after rotation.','marginhand','readable ink left as \\ill{}','medium',False,True,True)
ch('margin quelc.',r'\unsure{quelc.|quelq.}',r'\ill{}','quelc.','The final letter is a right-open c with no descending stroke, followed by a point.','marginhand','readable ink left as \\ill{}','medium',True,True,True)
ch('margin graduation',r'\unsure{graduation}',r'\ill{}',r'\unsure{gr.duation|graduation}','A distinct small blob follows gr before the d-like ascender. It may be an abbreviation point; the tightly joined continuation leaves the full spelling possible.','marginhand; margin-gr','readable ink left as \\ill{}','low',True,True,True)
ch('canceled n\'est',"n'est",r'\ill{}',"n'est, canceled",'The n arches, apostrophe, e curve, s and t remain distinct below the crosses.','nest','readable ink left as \\ill{}','high',False,True,True)
ch('arbitrairement overlapped cells',r'\unsure{arbitrairement}','arbitrairement',r'arbit\rlap{r}ai\rlap{r}eement','The baseline has thirteen occupied cells: after arbit, r and a overlap; after the following i, r and e overlap, followed by ement. The final e is dark but has no separately recoverable t.','arbitrairement; arbitraire-middle; arbitraire-end','misread word','medium',True,True)
ch('nécessaires final s','s canceled','s omitted','s canceled','A final s body remains under a hand slash following nécessaire.','necessaires','omission')
ch('soit or est correction',r'handwritten \unsure{soit}','soit canceled',r'\rlap{es}\handwritten{\unsure{soi}}t','Typed e and s survive underneath thin hand strokes read as soi; the rightmost t is typed. There is no separate cancellation of a complete handwritten soit.','soit','insertion or placement','medium',True,True,False,True)
ch('paragraph 9 punctuation','9/','9)',r'hand 9\unsure{/|)}','The lower sign is a long slanted stroke with a slight curve. Slash is favored but a parenthesis cannot be excluded.','nine','misread symbol or index','medium',True,True)
ch('canceled b)',r'\unsure{b)}','à','b), canceled','The b ascender and lower bowl and following right parenthesis remain under the cancellation.','bdelete','misread word','high',True,True)
ch('unit insertion placement','inserted after jeu','marginal after comma','inserted after jeu','The hand guide rises from the point after jeu, before the typewritten comma.','bfixe','insertion or placement')
ch('unit insertion hyphens','short hyphens','em dashes','short hyphens','Short typewriter horizontal marks flank l\'unité; no long dash is present.','bfixe','other')
ch('clipped fixée group',r'handwritten \unsure{fixée}',r'\ill{}',r'typed fix overlapped by hand \unsure{fix}; continuation clipped','The typed f, i and x are visible underneath a thin handwritten group at the right boundary. No complete ée or closing parenthesis is available inside this image.','bfixe; fixe','readable ink left as \\ill{}','low',True,True,True)
ch('unit insertion guide','omitted','omitted','local curved guide drawn','A long curve dips after jeu and passes below the added phrase, rising at the right edge.','bfixe','drawing or diagram','high',True,True)
ch('oubli quotation marks','double quotes','guillemets','double quotes','Two upper strokes at each side enclose oubli, without angular guillemets.','oubli','other')
ch('g in g in U','plain g','plain g',r'\unsure{\mathbb{g}|g}','A small additional middle loop and displaced upper ear suggest a second g strike; the merged bodies prevent certainty. The g letters in the diagonal formula have ordinary single bodies.','gU; g-over; Deltag','misread symbol or index','medium',True,True,False,True)
ch('augmentation punctuation','no comma','period','comma','A low comma follows the numeral 1 before the obscured opening parenthesis.','NBopen','other','high',True,True)
ch('homomorphisms insertion opening','i.e. les','et les','i.e. les','Two separate abbreviation points surround the e after i; this is not et.','homall; hom1','misread word')
ch('hom abbreviation point','hom','hom.','hom','No separate point follows the m before unitaires.','hom1; hom2','abbreviation expanded or spelling modernised')
ch('hand homomorphism name',r'\unsure{g|q}','g',r'\unsure{g|q} retained','The descender hooks left, favoring g, but the small upper body does not securely exclude q. The colon, A, right arrow and k are clear.','hom2','misread symbol or index','medium',False,True,False,True)
ch('homomorphisms insertion guide','omitted','omitted','curved guide and downward arrow drawn','A curved bracket beneath the inserted phrase has a downward arrow to the point after augmentation 1.','homall; NBopen','drawing or diagram','high',True,True)
ch('NB opening parenthesis',r'\unsure{(}','(',r'\unsure{(} retained','The insertion arrow and crossing strokes overlap the expected opening mark, preventing a firm identification.','NBopen','misread symbol or index','low',False,True)
ch('exprime m','exprime','exprime',r'expri\unsure{$\mathbb{m}$|m}e','The m has lighter displaced vertical and arch traces beside the dark body, compatible with a second strike; their weak joins leave a single m possible.','NBcondition; exprime-m','misread word','low',True,True)
ch('un e spacing','un e','une','un e','An empty typewriter interval separates n and e.','un_e','other')
ch('canceled foncte',r'\unsure{foncte|foncteur}',r'\ill{}','foncte, canceled','Six cells f o n c t e are visible beneath crosses; no following u or r is present before schéma.','foncte','readable ink left as \\ill{}','high',True,True,True)
ch('réconstituer accent','réconstitu...','reconstituer','réconstitu...','A separate acute accent is visible over the initial e.','reconstituer','abbreviation expanded or spelling modernised')
ch('extra t in réconstituer',r'\deleted{\unsure{t}}','omitted','t, canceled','A distinct t body between u and e is crossed by the hand cancellation.','reconstituer','deletion state','high',True,True)
ch('final canceled phrase',r'\unsure{(donner exemple}','Donner exemple','(donner exemple, canceled','The opening curved parenthesis, lower-case d ascender and the letters of both words remain readable through the cancellation; no closing parenthesis is visible.','lastcancel','misread word','high',True,True)
ch('pencil folio','comment only','page 122','mspage 122','Three pencil digits read 122 at the lower left.','folio','omission','high',True,False)
for line,reading,alts,conf,comment in [
 ('first typed tensor',r'\otimes',r'\Omega','medium','Eight typed instances; later forms use the first candidate. Hand inserted tensor is distinct.'),
 ('algèbres initial','a plus drawn extra strokes','a; À','low','Extra ink retained as a graphic without inventing another letter.'),
 ('canceled C to D',r'\to','','low','Only the central connector remains uncertain.'),
 ('c choisi',r'\mathbb{c}','c','medium','Light offset terminal and lower curve.'),
 ('N.e. first cell',r'\rlap{N}i','N','low','Overlapping middle upright and cancellation.'),
 ('canceled U expression',r'=\pi_j',r'=\sum_j','low','Middle group obscured; i and j themselves readable.'),
 ('canceled foncteur ending','au','du','medium','Both cells present, first upper body obscured.'),
 ('margin groupe','groupe','','low','Joined low letters remain unclear.'),
 ('margin de','de','des','low','Terminal stroke count uncertain.'),
 ('margin graduation','gr.duation','graduation','low','Blob after gr may be abbreviation point.'),
 ('correction over est','soi','','medium','Hand strokes overlap the still visible typed es; terminal t is typed.'),
 ('paragraph 9','/',')','medium','Slanted lower stroke has some curvature.'),
 ('unit insertion edge','hand fix over typed fix','','low','Visible fragment only; continuation beyond the right edge cannot be transcribed.'),
 ('g in U',r'\mathbb{g}','g','medium','Additional loop/ear may show repeated type.'),
 ('homomorphism name','g','q','medium','Left-hooked descender favors g.'),
 ('NB opening','(','','low','Arrow/crossing overlaps the punctuation.'),
 ('exprime m',r'\mathbb{m}','m','low','Weak displaced stem and arch traces.')]:r.doubt(line,reading,alts,conf,comment)
r.notation('typed tensor operator',r'first \unsure{\otimes|\Omega}; later \otimes','10:123 eight typed operators; one clear hand insertion','qualified by form')
r.notation('same-letter typed overstrike',r'\mathbb{v}; qualified \mathbb{c}, \mathbb{g}, \mathbb{m}','10:123 margin vérifier; c choisi; g in U; exprime','clear v; remaining forms qualified')
r.notation('physical different-letter overlap',r'\rlap{old}new without chronology','10:123 c/i, p/c, C/L, apostrophe/a, l/t twice, e/a, f/g, r/a and r/e; typed es under hand soi; typed fix under hand fix','physical overlap; not revision chronology')
r.notation('homogeneous module notation',r'{}_iM and {}_jN','10:123 canceled clause; no pi visible')
r.notation('graded quotient formula',r'U_\alpha^i=\widehat{\sum}\pi_{i+j}U_\alpha\pi_i','10:123 final subscript visibly i; not normalized')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10:123') for a,b in [('i.e.','id est'),('hom','homomorphismes'),('NB','nota bene'),('quelc.','quelconques, probable'),('gr.duation','graduation, qualified')]]
r.r['crops']=json.loads(Path('work/crops123.json').read_text())
r.r['inventory_overrides']={
 '123-E013':dict(first_words_or_objects=r'$C\unsure{\to}D$ est'),
 '123-E016':dict(first_words_or_objects=r'hand inserted tensor with curved guide'),
 '123-E023':dict(first_words_or_objects=r'revient à dire que si M ... N/i.e. ... {}_iM ... {}_jN ... l apostrophe/a isomorphisme ... U'),
 '123-E030':dict(first_words_or_objects='respecte'),
 '123-E031':dict(first_words_or_objects='i.e. de U and local guide after graduation de A'),
 '123-E032':dict(first_words_or_objects=r'foncteur \unsure{au|du}'),
 '123-E033':dict(first_words_or_objects=r'à mathbb v érifier, (groupe? de/des classes quelc. pour gr.duation/graduation ?)'),
 '123-E034':dict(first_words_or_objects=r'(groupe? de/des classes quelc. pour gr.duation/graduation ?)'),
 '123-E042':dict(first_words_or_objects=r'hand soi? overlapped with typed es; typed terminal t'),
 '123-E043':dict(hand='typewriter',first_words_or_objects='Quelles que soient les structures a) canceled b) c) ...'),
 '123-E044':dict(first_words_or_objects=r'9\unsure{/|)}'),
 '123-E045':dict(first_words_or_objects='b)'),
 '123-E046':dict(first_words_or_objects="(b) -l'unité - étant; typed fix with hand fix? overlapped and clipped continuation; guide"),
 '123-E047':dict(first_words_or_objects='fix? over typed fix; clipped continuation'),
 '123-E051':dict(first_words_or_objects='(i.e. les hom unitaires g/q:A to k), curved guide with downward arrow'),
 '123-E053':dict(first_words_or_objects='foncte'),
 '123-E054':dict(first_words_or_objects='t'),
 '123-E055':dict(first_words_or_objects='(donner exemple')}
for ident,kind,pos,words,hand in [
 ('123-E056','drawing','after structure','short curved guide to inserted tensor','unnamed hand'),
 ('123-E057','drawing','after graduation de A','curved guide for i.e. de U','unnamed hand'),
 ('123-E058','drawing','after en jeu','long guide for unit insertion','unnamed hand'),
 ('123-E059','drawing','above augmentation 1','curved guide and downward insertion arrow','unnamed hand'),
 ('123-E060','text','lower left folio','122','unnamed hand'),
 ('123-E061','drawing','algèbres first cell','extra strokes over and right of a','unnamed hand')]:
 r.r['inventory_extra'].append(dict(scan='10:123',sheet_kind='typescript',hand=hand,element=ident,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
r.r['inspection_note']='Root inspected whole scan, then both halves (repeated individually after truncated output), before witness comparison; all 82 crop recipes were rendered and visually read. Truncated piU/Amap2/nest/arbitrairement and final g/c/exprime/wide-foncteur batches were repeated individually. foncteureau-end proved to target the following f/g overlap; exprime-over targeted the ending, so cancel-du and exprime-m were added and read. Slanted margin read upright at -8 degrees. All agreed words, formula indices/signs, handwritten additions and deletion boundaries checked; all 22 C uncertainty loci reviewed. No OCR, context access, mathematical-check event, or parallel transcription.'
r.save('work/record123.json')
