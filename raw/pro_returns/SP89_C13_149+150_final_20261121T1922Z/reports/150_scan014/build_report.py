from pathlib import Path
import json

ROOT = Path('/workspace/scratch/8759b8008681')
PAGE = '150_scan014'
OUT = ROOT / 'work/reports' / PAGE
C = (ROOT / 'packets' / PAGE / 'C.tex').read_text()
H = (ROOT / 'packets' / PAGE / 'H.tex').read_text()
D = (OUT / 'draft.tex').read_text()
DC = '\n'.join(x for x in D.splitlines() if not x.lstrip().startswith('%'))
BOX = json.loads((OUT / 'crop_boxes.json').read_text())

def between(text, start, end, occurrence=0):
    at = -1
    for _ in range(occurrence + 1):
        at = text.index(start, at + 1)
    return text[at:text.index(end, at) + len(end)]

changes = []
def change(id, crop, place, c, h, final, evidence, confidence='high', kind='misread word',
           against_c=False, against_h=True, marked_in_h=False, consequential=False,
           error_category='2'):
    assert c in C, (id, 'C', c)
    assert h in H, (id, 'H', h)
    assert final in D, (id, 'final', final)
    changes.append(dict(id=id, place=place, c=c, h=h, final=final, evidence=evidence,
                        crop=f'crops/{PAGE}_{crop}.png', box=BOX[crop], confidence=confidence,
                        kind=kind, against_c=against_c, against_h=against_h,
                        marked_in_h=marked_in_h, consequential=consequential,
                        error_category=error_category))

change('P01a','P01','Author number at the upper left',r'\mspage{2}',
       '« 2) »',r'\mspage{2)}',
       'A compact hooked 2 is followed by a separate long closing parenthesis sweeping down and left. The lower sweep belongs to that parenthesis, not an underline. H quotes the number in an editorial note; only the written number is transcribed.',
       kind='omission',against_c=True,against_h=False,error_category='3')
change('P02a','P02','Opening L2: T in de T dans X',r'de $\bar T$ dans $X$',
       r'de $T$ dans $X$',r'de $T$ dans $X$',
       'The letter has one detached horizontal roof and one upright. There is no second horizontal stroke above a completed T. The adjacent dotted T forms have exactly this roof plus a separate dot, providing the local comparison.',
       kind='misread symbol or index',against_c=True,against_h=False,error_category='1')
change('P02b','P02','Opening reference number',r'i.e. (7)',r'i.e. (8)',r'i.e. (7)',
       'The digit has an angled upper entry and one long descending stroke, with no pair of closed loops. The parentheses and reference position are distinct from the nearby insertion leader.',
       kind='misread symbol or index',error_category='1')
change('P02c','P02','Parenthesis: X=T',r'X=\bar T',r'X=T',r'X=T',
       'The T in X=T has a single roof joined to its upright. The later overtraced group is to its right, not an extra overbar.',
       kind='misread symbol or index',against_c=True,against_h=False,error_category='1')
change('P02d','P02','Crossed group immediately after X=T',
       r'X=\bar T\deleted{\unsure{_\lambda}}',r'X=T',
       r'X=T\deleted{\unsure{_\lambda}}',
       'There is a separate crossed/retraced narrow body between T and the comma: an upper crossing, a looped descending body and a lower return. Lambda and its lowered attachment remain doubtful; H omits this ink. The plain-T correction in the contextual snippet is separately logged as P02c.',
       confidence='low',kind='omission',consequential=True,error_category='3')
change('P02e','P02','Short word after the parenthetical comma',r'avec',
       r'\uncertain{\ill{}}',r'\unsure{pour|avec}',
       'The first body has a closed upper loop and a long descending stroke, more p-like than a. The middle is compressed and retraced and the ending rises briefly; pour is preferred with avec retained as an alternative. Neither the grammar nor the non-emptiness statement settles the letters.',
       confidence='low',against_c=True,marked_in_h=True,error_category='2')
point = between(D,r'\figure{\begin{tikzpicture}',r'\end{tikzpicture}}')
change('P02f','P02','Isolated ink point below faux and right of the parenthesis',
       r'(prendre $X=\bar T\deleted{\unsure{_\lambda}}$, avec $\dot T\neq0$).',
       r'(prendre $X=T$, \uncertain{\ill{}}, $\dot T\neq0$).',point,
       'A separate small filled vertical oval lies below faux, well to the right of the parenthetical line. Its dark ink is unambiguous, but its linguistic status is not. It is reproduced as an isolated graphic, without attaching it as a sentence stop. The witness snippets are the neighboring parenthesis, not assertions that either witness denies the point.',
       kind='drawing or diagram',against_c=True,against_h=True,error_category='4')
change('P03a','P03','Cancelled opening before the definition',r'\deleted{On dira}',
       r'\struck{Disons}',r'\deleted{\unsure{On dira}}',
       'The old group begins with a large oval O-like loop and a low joined n-like body; a later ascender and dot support di-. The long cancellation obscures the ending, so the full On dira reading remains doubtful. There is no secure capital D followed by the sequence isons.',
       confidence='low',against_c=False,error_category='2')
change('P03b','P03','Raised replacement above the cancelled opening',
       r'\inserted{\illegible{1}}',r'\add{\emph{Évitons}}',
       r'\inserted{\unsure{É|E}}',
       'Only an isolated capital E-like group is written directly above the cancellation: an oblique upright, two short rightward limbs, and a separate upper stroke that may be its accent or its upper bar. No following vitons sequence is present there. The slanted writing to its lower left belongs to the marginal structure line, not this insertion. The preferred accented capital is retained with E as an alternative; it is not expanded into a word.',
       confidence='medium',kind='readable ink left as \\ill{}',against_c=True,against_h=True,
       consequential=True,error_category='5')
change('P04a','P04','First overwritten variable after partie fermée',
       r'fermée $\unsure{Y|Z}$',r'fermée \struck{$Z$} $Y$',
       r'fermée $\deleted{Z}Y$',
       'Thin upper and lower horizontal limbs and an oblique join form an earlier Z. A much heavier fork with a long descending stem forms Y over it. The live Y agrees with the clean forked Y in the following map. The older Z is retained before Y as overwritten ink, resolving C’s letter choice and preserving H’s two layers.',
       kind='deletion state (struck given live or live given struck)',against_c=True,
       against_h=False,error_category='7')
change('P04b','P04','Quoted and underlined term partie bord',
       r"``\uline{partie bord}''",r'« \emph{partie bordante} »',
       r"``\uline{partie bord}''",
       'The final d rises in a tall loop and immediately gives way to two closing upper ticks. There are no ante letters. The opening mark is also a paired upper-tick mark, not a pair of angle brackets; one underline runs beneath the two words.',
       error_category='2')
change('P05a','P05','Hyphen after voisinage',r'\uline{voisinage} ',
       r'\emph{voisinage} ',r'\uline{voisinage}-',
       'A short independent horizontal stroke sits on the text baseline after the underlined voisinage and before the overwritten/raised replacement area. It is separated from the lower underline and from the cancellation strokes.',
       kind='omission',against_c=True,against_h=True,error_category='3')
change('P05b','P05','Cancelled underlined word below cylindrique',
       r'\deleted{\uline{collier}}',r'\struck{\emph{collant}}',
       r'\deleted{\uline{collier}}',
       'Beneath the strike are the initial c/o bowls, two successive tall l loops, a separate i dot, and a short e/r ending. That sequence supports collier, not collant. Its lower horizontal stroke is an underline separate from the strike through the word.',
       error_category='2')
change('P05c','P05','Overworked initial group of raised cylindrique',
       r'\inserted{\uline{cylindrique}}',
       r'\struck{\ill{}} \struck{\emph{collant}} \add{\emph{cylindrique}}',
       r'\inserted{\uline{\unsure{c}ylindrique}}',
       'A black zigzag occupies the initial c position immediately before clear ylindrique. It is not possible to separate a further earlier word from the overwork of that initial group. The reading records a doubtful initial c and the visible replacement word, rather than H’s additional independent cancelled word. The state of the underlying strokes remains open; this does not assert that every dark stroke is part of a clean c.',
       confidence='medium',kind='deletion state (struck given live or live given struck)',
       against_c=False,against_h=True,marked_in_h=True,error_category='7')
change('P05d','P05','Second overwritten variable after cylindrique de',
       r'de $\unsure{Y|Z}$ dans $X$',r'de $Y$ dans $X$',
       r'de $\deleted{Z}Y$ dans $X$',
       'As in the first occurrence, thin horizontal Z limbs remain visible under a heavier forked Y with a descending stem. This is not merely a single ambiguous letter: both layers remain on the page. H preserves only the live Y here.',
       kind='deletion state (struck given live or live given struck)',against_c=True,
       against_h=True,error_category='7')
change('P06a','P06','First occurrence of cônique',r'conique $\bar T$ tel que',
       r'conique $T$ tel que',r'cônique $T$ tel que',
       'A separate small curved circumflex-like stroke sits over the o, with the body of conique on the baseline below it. The same extra accent is repeated in the later example. The source spelling cônique is retained.',
       kind='abbreviation expanded or spelling modernised',against_c=True,against_h=True,error_category='8')
change('P06b','P06','T following the first cônique',r'\bar T$ tel que',r'T$ tel que',
       r'T$ tel que',
       'A single roof and a single descending upright form the T; no second overbar is present. The dotted T at the start of the next line shows the extra dot separately.',
       kind='misread symbol or index',against_c=True,against_h=False,error_category='1')
change('P06c','P06','First homéom abbreviation and following dash',
       r'homéom. --- ou',r'homéomorphisme -- ou',r'homéom --- ou',
       'After the accented é and short o/m ending there is blank space, then an independent long dash before ou. There is no intervening stop and no following orphisme letters. The marginal homéom. has a separate clear dot and supplies a useful contrast.',
       kind='abbreviation expanded or spelling modernised',against_c=True,against_h=True,error_category='8')
change('P07a','P07','Cancelled phrase before live s’il existe',
       r"\deleted{i.e. tel que l'on}",r"\struck{s'il tel que l'on}",
       r"\deleted{\unsure{i.e.} tel que l'on}",
       'The cancellation extends from the initial small abbreviation through tel que l’on. The first cluster has a short dotted upright and a low e-like body, unlike the larger live s’il immediately after the strike; its punctuation is partially masked, so i.e. remains doubtful. Tall t/l stems, the q descender and the l apostrophe group remain readable in the remainder.',
       confidence='medium',against_c=False,against_h=True,error_category='2')
change('P07b','P07','Small cancelled group before the second voisinage T',
       r'\deleted{\unsure{de}}',r'voisinage $T$ de $Y$',
       r'\deleted{\unsure{de}}',
       'A small crossed looped body stands between voisinage and T. Its upper loop and lower return allow de, but the strike prevents recovery of both letters with certainty. H leaves this group out.',
       confidence='low',kind='omission',error_category='3')
change('P07c','P07','T after the small cancelled group',
       r'voisinage $\deleted{\unsure{de}}\bar T$ de $Y$',
       r'voisinage $T$ de $Y$',r'voisinage $\deleted{\unsure{de}}T$ de $Y$',
       'The T has one detached roof and one upright. The cancelled group at its left is separate; there is no independent bar over T. This row concerns T only; the contextual deleted group is logged in P07b.',
       kind='misread symbol or index',against_c=True,against_h=False,error_category='1')
change('P07d','P07','Second homéom abbreviation before (9)',
       r'et un homéom.',r'et un homéomorphisme',r'et un homéom',
       'The word ends with the low undulating m and a short downward return. No isolated punctuation follows it, and no orphisme sequence is written before the displayed equality.',
       kind='abbreviation expanded or spelling modernised',against_c=True,against_h=True,error_category='8')
change('P08a','P08','Complete equality (9)',r'(9)\qquad\bar T\simeq Y\times I',
       r'(9)\qquad T\simeq Y\times\mathbf{I}',
       r'(9)\qquad T\simeq Y\times\mathbf{I}',
       'The T has its sole horizontal topstroke. The interval I has a heavily filled upright and broad upper and lower serif bars, unlike the thin index-set I later on the page. The relation is a wave above a horizontal stroke; (9) stands at the left.',
       kind='misread symbol or index',against_c=True,against_h=False,error_category='1')
cdiag = between(C,r'(10)\qquad',r'\end{tikzcd}')
hdiag = between(H,r'\begin{tikzcd}',r'(10)')
ddiag = between(D,r'(10)\qquad',r'\end{tikzcd}')
change('P09a','P09','Complete triangular diagram (10)',cdiag,hdiag,ddiag,
       'There are three objects, two arrow shafts, two right/down-right heads and one hooked tail. Y maps horizontally with a hook to plain T and diagonally to Y times the heavy serif I. The diagonal label is y mapsto (y,0), with its own mapsto bar and zero. Between T and the product is a curved upright beside a straight upright, with no arrowhead and no third connecting shaft. It is set as vertical wr plus vert; C’s horizontal simeq and H’s added downward arrow do not preserve that orientation/stroke count. The number (10) is at the left of the diagram, not below it.',
       kind='drawing or diagram',against_c=True,against_h=True,consequential=True,error_category='4')
change('P10a','P10','First words of the diagonal margin note',
       r'définir la \unsure{structure}',r'\uncertain{définir} le \uncertain{voisinage}',
       r'définir la structure',
       'In the clockwise-rotated saved crop the first words read définir la: the final a is a small closed bowl after l. The next word has an initial looped s, a tall t, compressed ru/c, another tall crossed t and the final ure sequence. These strokes give structure, resolving C’s doubt. They are on the marginal line and must not be borrowed to extend the isolated main-text É/E.',
       kind='misread word',against_c=True,against_h=True,
       marked_in_h=True,error_category='2')
change('P10b','P10','Continuation of diagonal margin prose',
       'de voisinage cylindrique\ncomme un homéom.',
       r'\ill{} \uncertain{de frontière} \ldots\ ',
       'de voisinage cylindrique\ncomme un homéom.',
       'The margin has a clear v/o/i sequence and g descender in voisinage, then the c/y/l/i/n/d/r/i/q/u/e pattern of cylindrique. The next line has the two low m humps of comme followed by un. The short homéom ends in a distinct separate dot. Neither frontière nor an ellipsis is written at those positions.',
       kind='readable ink left as \\ill{}',marked_in_h=True,error_category='5')
change('P10c','P10','Marginal compatible avec after the product formula',
       r'compatible avec',r'$E\simeq Y\times[0,1]$ \ldots\ $y\mapsto(y,0)$',
       r'compatible avec',
       'The next marginal line begins co/m, has a p descender and tall t/b/l members, and ends in the small avec group. Those letters are present before the two-row map, where H supplies only an editorial ellipsis.',
       kind='omission',error_category='3')
cmargin_diagram = between(C,r'\begin{tikzcd}',r'\end{tikzcd}',1)
dmargin_diagram = between(D,r'\begin{tikzcd}[column sep=small',r'\end{tikzcd}')
change('P10d','P10','Complete two-row marginal map and literal target',
       cmargin_diagram,r'$y\mapsto(y,0)$',dmargin_diagram,
       'The first row is Y, a horizontal connector, then an opening square bracket immediately followed by 0, comma, 1 and a closing bracket. No Y or multiplication cross intervenes before the bracket. The upper connector ends in a small rise/thickening without a secure two-sided head, so an unheaded stroke is preferred with arrow as alternative. The lower row is y mapsto (y,0), with a short transverse tail bar and an upturned terminal head. The target choice [0,1] is resolved on the ink; the resulting type mismatch is retained.',
       confidence='medium',kind='drawing or diagram',against_c=True,against_h=True,
       consequential=True,error_category='4')
change('P11a','P11','Example: T est un voisinage',r'Par exemple, si $\bar T$',
       r'Par exemple, si $T$',r'Par exemple, si $T$',
       'The example’s T has one roof joined to its descending upright. There is no second horizontal accent; the dotted T on the following line has a separate dot over the same basic shape.',
       kind='misread symbol or index',against_c=True,against_h=False,error_category='1')
change('P11b','P11','Second occurrence of cônique',
       r'\deleted{tubulaire} conique',r'\struck{tubulaire} conique',
       r'\deleted{tubulaire} cônique',
       'A distinct short curved accent lies over the o of the final word, repeating the first cônique. It is separated from the c/o baseline bodies and from the strike through tubulaire.',
       kind='abbreviation expanded or spelling modernised',against_c=True,against_h=True,error_category='8')
change('P11c','P11','Cancelled word after de in the example',
       r'\deleted{\unsure{tout}}',r'de \struck{\ill{}} $Y$',
       r'\deleted{\unsure{tout}}',
       'A tall crossed t is visible at the beginning, followed by a low rounded body under a thick horizontal strike. Tout remains a plausible complete reading but the middle and ending are not all separable; the doubt is retained rather than declaring the word fully recovered.',
       confidence='low',kind='readable ink left as \\ill{}',marked_in_h=True,error_category='5')
change('P11d','P11','Example endpoint: sous-espace bord.',r'sous-espace bord.',
       r'sous-espace bordant de $T$,',r'sous-espace bord.',
       'The word ends in a tall d and a separate full stop. There are no ant letters or de T after it. The next physical line starts the doubtful donc and a new dotted T-lambda statement.',
       error_category='2')
change('P12a','P12','Start of the next statement after bord.',
       r'\unsure{donc} $\dot T_\lambda$ est',r'et un sous-espace',
       r'\unsure{donc} $\dot T_\lambda$ est',
       'A looped d-like initial and a compressed low ending precede a separately written dotted T with lowered lambda and the letters est. Donc remains doubtful because the nc ending is compressed. The dot over T is separate and dark. H’s et un wording omits this repeated subject and verb.',
       confidence='medium',kind='omission',error_category='3')
change('P12b','P12','Second sous-espace bord term',
       r'bord de $\bar T_\lambda$',r'bordant de $T_\lambda$',
       r'bord de $T_\lambda$',
       'The final d closes the short bord body; no ant sequence intervenes before de. The neighboring T correction is separately described in P12c.',
       error_category='2')
change('P12c','P12','T-lambda at the end of that statement',
       r'\bar T_\lambda',r'T_\lambda',r'T_\lambda',
       'The final T has its roof and descending stem with lambda below-right, but no dot and no second topstroke. This contrasts with the separately dotted T-lambda at the line’s beginning.',
       kind='misread symbol or index',against_c=True,against_h=False,error_category='1')
change('P13a','P13','Cancelled operator before the strip examples',
       r'\deleted{\unsure{\mathrm{Ep}}}',r'\struck{$E$}',
       r'\deleted{\unsure{\mathrm{Ep}}}',
       'The crossed group has an E-like box of horizontal strokes and a separate descending looped body to its right, compatible with p. The heavy crossing prevents an assured whole reading or a decision about an earlier accent; Ep remains doubtful. H’s E omits the descending right-hand body.',
       confidence='medium',kind='misread symbol or index',error_category='1')
change('P13b','P13','Plural bords before the strip operator',r'bords de',r'bordants de',
       r'bords de',
       'After the tall d, the short s ends the word before de. There are no a/n/t bodies between d and s. This agrees with the short bord terms used elsewhere on the sheet.',
       error_category='2')
change('P13c','P13','Live strip operator with E-bar, p, epsilon and (T)',
       r'\mathrm{Ep}_\varepsilon^{(T)}',r'E_\varepsilon(T)',
       r'\bar{\mathrm{E}}\mathrm{p}_\varepsilon(T)',
       'Here, unlike T, the E has an independent horizontal bar above its own upper arm. To the right is a small p with a clear long descender, followed by a lowered epsilon. The parenthesized T ends on the E baseline; its upper roof is high because of the taller capital and parentheses, not because the whole (T) is an exponent. The overbar covers E only.',
       kind='misread symbol or index',against_c=True,against_h=True,
       consequential=True,error_category='1')
change('P14a','P14','Final sous-espace bord term',r'est un sous-espace bord ssi',
       r'est un sous-espace bordant ssi',r'est un sous-espace bord ssi',
       'The d’s tall return is followed directly by the compressed three-letter ssi group. No ant is written before that abbreviation.',
       error_category='2')
change('P14b','P14','Whole final union formula: uncertain lower index-set letter',
       r'Y=\bigcup_{i\in I}Y_i',r'Y=\bigcup_{i\in I}Y_i',
       r'Y=\bigcup_{i\in\unsure{J|I}}Y_i',
       'The lower index after the membership sign has a top stroke and a descending body that returns markedly to the left, producing a J-like shape; the earlier family index uses a more upright serif I. J is the preferred literal shape with I retained as alternative. The shared intended indexing in the mathematical statement is not used to regularize the ink.',
       confidence='medium',kind='misread symbol or index',against_c=True,against_h=True,
       consequential=True,error_category='1')
change('P14c','P14','Page-edge ending after le sont',r'le sont.',r'le sont.',r'le sont',
       'The compressed terminal word reaches the right paper edge. Its final upright is crowded by that edge, but no independent full stop is visible after it. The text is not extended into the black border or supplied with a stop.',
       confidence='medium',kind='other',against_c=True,against_h=True,error_category='10')
change('P15a','P15','Thin lower-left foliation',r'\margin{13}',
       r'\note{« une partie finie » : lire \uncertain{une famille finie}.}',r'\margin{13}',
       'The lower left has a thin hooked 1 followed by a two-lobed 3, distinct in instrument/weight from the main manuscript. H has no folio reading at this position; its final note about partie/famille is editorial and is not transcribed.',
       kind='omission',error_category='3')

decisions = []
def decision(id, crop, result, reading, evidence, confidence='high'):
    assert reading in D, (id, reading)
    decisions.append(dict(id=id,cote='150',scan='14',decision=result,reading=reading,
                          evidence=evidence,crop=f'crops/{PAGE}_{crop}.png',box=BOX[crop],
                          confidence=confidence))
decision('M0324','P03','other',r'\inserted{\unsure{É|E}}',
         'An isolated raised capital with oblique upright and short right limbs is recoverable; the detached upper stroke may be an accent or the upper arm. No following letters support Évitons. Adjacent slanted letters belong to the marginal structure line.','medium')
decision('M0325','P03','undecided',r'\unsure{enfin de}',
         'The live compressed group beside dire is crossed/approached by slanted marginal strokes. A tall f-like member and low terminal line support the inherited enfin de reading, but the exact division and the small de are not separable enough to remove doubt.','low')
decision('M0326','P04','other',r'fermée $\deleted{Z}Y$',
         'Thin upper/lower Z limbs remain beneath a heavier Y fork and stem. Both layers are preserved, so the result is not merely choosing Y and discarding the old Z.')
decision('M0327','P05','other',r'de $\deleted{Z}Y$ dans $X$',
         'The second glyph repeats the thin Z under heavier Y layering, with lower horizontal residue distinct from the live descending Y stem.')
decision('M0328','P10','first',r'définir la structure',
         'The rotated crop separates the marginal line: initial s loop, tall t, low ru/c, second crossed t and ure ending support structure. The preceding short article ends in a closed a bowl.')
decision('M0329','P10','first',r'Y&\unsure{-|\longrightarrow}&[0,1]',
         'The opening square bracket immediately follows the upper connector; 0, comma, 1 and the closing bracket follow. No preceding Y-times group is present. This resolves the target only; the connector head remains uncertain.')
decision('M0330','P12','undecided',r'\unsure{donc}',
         'A d-like loop and upright are clear; the compressed ending can be read nc, but no fully separated terminal sequence warrants removing the doubt.','medium')

inventory=[]
def inv(kind, position, content, hand='his hand', transcribed='yes'):
    inventory.append(dict(scan=PAGE,sheet_kind='text',hand=hand,element=f'E{len(inventory)+1:02d}',
                          kind=kind,position=position,first_words_or_objects=content,
                          transcribed=transcribed))
inv('margin note','upper left; P01','2)')
inv('text','upper three lines; P02','Mais on ne peut pas dire … frontière … (7) … X=T')
inv('insertion','above que in the first line; P02','en général; curved leader attaches before que')
inv('deletion','after X=T in the parenthesis; P02','crossed doubtful lowered lambda/group')
inv('drawing','isolated at approximately (1110,261), below faux and right of parenthesis; P02','one small filled vertical oval; linguistic status unclear')
inv('text','definition paragraph; P03–P07','[cancelled opening] [raised É/E] enfin de dire … partie bord … cônique')
inv('deletion','above the definition opening; P03','On dira, ending obscured')
inv('insertion','directly above the cancelled opening; P03','isolated É/E, not expanded')
inv('deletion','first variable after partie fermée; P04','earlier Z overwritten by live Y')
inv('deletion','under the raised cylindrique; P05','underlined collier, struck through')
inv('insertion','above collier; P05','underlined cylindrique, initial group overworked')
inv('deletion','second variable after cylindrique de; P05','earlier Z overwritten by live Y')
inv('deletion','before first cônique; P06','tubulaire')
inv('deletion','between au même and live s’il existe; P07','doubtful i.e. tel que l’on')
inv('deletion','immediately before second voisinage T; P07','small crossed doubtful de')
inv('display','middle of page; P08','(9) T ≃ Y × bold serif I')
inv('text','between (9) and (10), read on the upper/lower halves','rendant commutatif le diagramme')
inv('diagram','middle; P09','(10): three objects, two directed arrows, one hook, one vertical two-stroke identification')
inv('margin note','diagonal left margin; P10, original box [20,380,372,1245]','définir la structure … homéom. E≃Y×[0,1] compatible avec')
inv('diagram','lower part of diagonal marginal note; P10','Y — [0,1], uncertain upper head; y mapsto (y,0)')
inv('text','lower example and closing paragraph; P11–P14','Par exemple … cônique … sous-espace bord … partie finie … ssi')
inv('deletion','first example line; P11','tubulaire')
inv('insertion','above de in the example; full half and P11','(absolu), with separate curved attachment leader')
inv('deletion','after de and before Y in the example; P11','doubtful tout')
inv('deletion','before first dotted-T strip expression; P13','doubtful Ep with descending right-hand body')
inv('deletion','before live Si X; P13','Dans')
inv('margin note','lower left; P15','13','thin pencil/other or undetermined hand')

audits=[]
def audit(kind, box, reading):
    assert reading in DC or reading in D, ('audit reading',reading)
    audits.append(dict(box=f'B{len(audits)+1:02d}',kind=kind,xyxy=box,reading=reading))
audit('handwritten number',[25,18,120,85],r'\mspage{2)}')
audit('insertion',[915,25,1190,125],r'\inserted{en général}')
audit('handwritten number; C/H different words',[250,125,1640,220],
      r'de $T$ dans $X$, i.e. (7) devient faux si $\lambda=1$')
audit('struck passage; doubtful formula; handwritten number; C/H different words; less than high confidence departure',
      [250,205,1005,300],r'(prendre $X=T\deleted{\unsure{_\lambda}}$, \unsure{pour|avec} $\dot T\neq0$).')
audit('less than high confidence departure',[1094,238,1133,284],point)
audit('struck passage; insertion; C/H different words; less than high confidence departure',
      [330,305,855,455],r"\deleted{\unsure{On dira}} \inserted{\unsure{É|E}} \unsure{enfin de} dire qu'une")
audit('struck passage; doubtful formula',[870,343,1572,435],r"partie fermée $\deleted{Z}Y$ d'un")
audit('C/H different words',[248,425,1590,516],
      r"espace topologique $X$ est une ``\uline{partie bord}''")
audit('struck passage; insertion; doubtful formula; C/H different words; less than high confidence departure',
      [230,503,1654,619],
      "s'il existe un \\uline{voisinage}-\\deleted{\\uline{collier}}\n"+
      r'\inserted{\uline{\unsure{c}ylindrique}} de $\deleted{Z}Y$ dans $X$,')
audit('struck passage; C/H different words',[242,632,1656,716],
      r'i.e. un voisinage \deleted{tubulaire} cônique $T$ tel que')
audit('C/H different words',[242,718,1656,812],
      r'$\dot T\longrightarrow Y$ soit un homéom --- ou ce qui revient')
audit('struck passage; C/H different words; less than high confidence departure',[244,806,1620,910],
      r"au même, \deleted{\unsure{i.e.} tel que l'on} s'il existe un")
audit('struck passage; doubtful formula; C/H different words',[244,914,1620,992],
      r'voisinage $\deleted{\unsure{de}}T$ de $Y$ dans $X$ et un homéom')
audit('handwritten number',[235,1005,923,1127],r'(9)\qquad T\simeq Y\times\mathbf{I}')
audit('handwritten number; doubtful formula',[237,1245,880,1479],ddiag)
margin = between(DC,r'\margin{définir',r'\]}}')
audit('margin note; doubtful formula; handwritten number; C/H different words; less than high confidence departure',
      [20,380,372,1245],margin)
audit('struck passage; insertion; C/H different words; less than high confidence departure',
      [130,1533,1682,1743],
      'Par exemple, si $T$ est un voisinage \\deleted{tubulaire} cônique\n'+
      r'\inserted{(absolu)} de \deleted{\unsure{tout}} $Y$, alors $\dot T$ est un sous-espace bord.')
audit('doubtful formula; C/H different words; less than high confidence departure',[232,1752,1625,1833],
      r'\unsure{donc} $\dot T_\lambda$ est un sous-espace bord de $T_\lambda$ ;')
strip = between(DC,r'$\deleted{\unsure{\mathrm{Ep}}}',r'Si $X$ est un espace')
audit('struck passage; doubtful formula; handwritten number; C/H different words; less than high confidence departure',
      [235,1844,1682,2068],strip)
audit('C/H different words',[244,2056,1684,2165],
      r'\uline{compact}, et $(Y_i)_{i\in I}$ une partie finie de')
audit('doubtful formula; C/H different words; less than high confidence departure',[244,2165,1684,2352],
      'parties fermées disjointes de $X$, alors\n'+
      r'$Y=\bigcup_{i\in\unsure{J|I}}Y_i$ est un sous-espace bord ssi les $Y_i$ le sont')
audit('margin note; handwritten number',[19,2301,75,2357],r'\margin{13}')

doubts=[]
def doubt(place,reading,alternatives,confidence,reason):
    doubts.append(dict(place=place,reading=reading,alternatives=alternatives,
                       confidence=confidence,reason=reason))
doubt('P02 crossed group after X=T',r'\deleted{\unsure{_\lambda}}',
      'lambda with uncertain lowered attachment; no second recoverable token offered','low',
      'Upper crossing and lower loop are dark and retraced; both the letter and its exact height remain uncertain. The empty space is not substituted for present ink.')
doubt('P02 word after comma',r'\unsure{pour|avec}','pour | avec','low',
      'A p-like initial descender is more visible than a clean a; the compressed middle and final rise do not establish a complete word.')
doubt('P02 isolated filled point',point,'linguistic or nonlinguistic isolated mark; no stop attached','medium',
      'The oval itself is clear, but its separation from the parenthesis and position below faux do not establish punctuation attachment.')
doubt('P03 old opening',r'\deleted{\unsure{On dira}}','On dira; ending not fully recoverable','low',
      'Initial O/n and later d/i are supportable, but the cancellation obscures the old ending. H’s Disons does not match the visible initial loop/body.')
doubt('P03 isolated raised capital',r'\inserted{\unsure{É|E}}','É | E','medium',
      'The upper separate stroke could be an accent or the upper arm of an abbreviated capital. No continuation warrants Évitons.')
doubt('P03 following live group',r'\unsure{enfin de}','enfin de; exact division unresolved','low',
      'The compressed live letters abut/cross slanted marginal strokes; the f-like tall member is visible but the little de is not fully separable.')
doubt('P05 initial cylindrique overwork',r'\inserted{\uline{\unsure{c}ylindrique}}',
      'initial c overwork; underlying earlier mark not independently recoverable','medium',
      'Clear ylindrique follows a zigzag mass in the initial position. There may be underlying revision strokes, but a separate whole cancelled word cannot be established.')
doubt('P07 cancelled first abbreviation',r"\deleted{\unsure{i.e.} tel que l'on}",
      'i.e.; punctuation beneath strike unresolved','medium',
      'A short dotted upright and low loop favor i.e.; the strike masks the exact points and prevents certainty.')
doubt('P07 crossed group before T',r'\deleted{\unsure{de}}','de; no secure alternative','low',
      'Two loop/return portions are partly hidden by crossing strokes.')
doubt('P10 upper marginal connector',r'\unsure{-|\longrightarrow}',
      'unheaded horizontal stroke | arrow','medium',
      'The terminal rise/thickening lacks a secure separate head; the lower mapsto head is more explicit. The target [0,1] itself is clear.')
doubt('P11 cancelled word after de',r'\deleted{\unsure{tout}}','tout; inner letters obscured','low',
      'The initial t is visible but the heavy strike obscures the middle and ending.')
doubt('P12 first word',r'\unsure{donc}','donc; terminal nc compressed','medium',
      'The d is secure but the remaining low strokes are not individually separated.')
doubt('P13 cancelled operator',r'\deleted{\unsure{\mathrm{Ep}}}',
      'Ep; exact earlier accent and letters remain partly obscured','medium',
      'E-like horizontal members and a separate descending right body support Ep, but are heavily crossed.')
doubt('P13 first radial factor',r'(1-\unsure{\varepsilon|\delta})\dot T',
      'epsilon | delta in the first factor','medium',
      'The first Greek letter has looped, overworked upper and lower portions; the later epsilon is clearer. Similarity of the two formulas does not remove the local ambiguity. No independent cancellation is asserted.')
doubt('P14 lower union index',r'Y=\bigcup_{i\in\unsure{J|I}}Y_i','J | I','medium',
      'The lower index-set letter has a pronounced leftward lower return, unlike the upright earlier I. Mathematical consistency favors the same set but cannot settle the literal shape.')
doubt('P14 page-edge ending',r'le sont','le sont; terminal t crowded by paper edge','medium',
      'The compressed final upright reaches the edge. No following stop is recoverable and none is supplied.')

notes=[
 dict(id='N01',text='The sheet is manuscript text in his hand, with author number 2), a diagonal left-margin note, two mathematical diagram blocks, numerous revisions, and thin lower-left foliation 13 in another or undetermined hand. The entire original and both supplied native halves were read once; all fifteen saved crops were inspected once. P10 is rotated 45 degrees clockwise for reading, while every recorded coordinate remains in the original 1685 by 2363 image. The main text has nineteen physical prose lines, one equality display and one triangular diagram block (line_count 21 by this convention); the diagonal margin is inventoried separately. H’s foliation discussion, note about its added vertical arrow and proposed famille correction are editorial, not manuscript text.'),
 dict(id='N02',text='Targeted boundary check. The source says “Mais on ne peut pas dire … en général que dot T soit la frontière de T dans X” and gives X=T with dot T not equal to the written 0. For any space X, the topological boundary of X inside itself is closure_X(X) minus interior_X(X), hence empty. Taking a nonempty Y and X=T=Y×[0,1], with the distinguished outer section dot T=Y×{1}, gives a nonempty dot T and empty ambient frontier. Thus the displayed counterexample mechanism is valid. This checks that mechanism only: reference (7) is read from its ink and the unavailable earlier statement numbered (7) is not reconstructed. The source’s un-crossed oval 0 is retained, not silently changed to phi or an empty-set glyph.'),
 dict(id='N03',text='Independent local re-proof of the collar/mapping-cylinder equivalence, conditional on cônique having its usual mapping-cylinder meaning here. Let f:B→Y be a homeomorphism and let C(f) be the quotient of Y disjoint union (B×[0,1]) by (b,0) identified with f(b). The map sending the base y to (y,0) and the class of (b,r) to (f(b),r) is well-defined and continuous by the quotient property. Its inverse sends (y,r) to the class of (f^{-1}(y),r); this is continuous and agrees with the base identification at r=0. The two maps compose to the identities, so C(f)≃Y×[0,1] and the base inclusion becomes y↦(y,0), precisely the commutativity of diagram (10). Conversely a product collar transports the identity-map cone structure on Y×[0,1]. This proof uses an explicitly stated interpretation of the cone construction; the assigned leaf does not define all of its earlier notation. No extra bar on T is justified by this interpretation.'),
 dict(id='N04',text='Targeted check of the absolute-cone and strip examples. Under the standard radial convention, away from the cone vertex the absolute cone on B has the product coordinates B×(0,1]. For any 0<a<1, the strip B×[a,1] is a collar neighborhood of the outer section B×{1}; the coordinate u=(1-r)/(1-a) sends that section to u=0 and gives B×[0,1]. For a positive radius lambda, the same construction on [a lambda,lambda] collars the section B×{lambda} inside the truncated cone T_lambda. This requires lambda>0; the source’s line does not state its range anew, and no assertion about the vertex radius zero is inferred. For a product strip B×[a,b] with a<b, each endpoint section has a collar obtained by a sufficiently short endpoint subinterval. Their union has a collar by choosing two disjoint endpoint subintervals and taking the disjoint union of those product collars. Therefore the three listed boundary choices are valid if the live barred-E-p operator denotes that radial strip and 0<epsilon<1. The operator is not defined on this leaf, so that identification and parameter range remain explicit hypotheses, not purported recovered definitions. The first epsilon/delta reading remains unresolved despite the expected strip formula.'),
 dict(id='N05',text='Independent re-proof of the closing finite-union statement under the compact-Hausdorff convention, and assuming the uncertain lower J/I denotes the same finite index set as the preceding family. Let Y_i be finitely many pairwise disjoint closed subsets of compact Hausdorff X, and write Y for their union. Each Y_i is clopen in Y. If h:Y×[0,1]→T is a collar with h(y,0)=y and T a neighborhood of Y, then h(Y_i×[0,1]) is a neighborhood of Y_i: its product component is open in T, and intersecting it with an ambient open neighborhood of Y contained in T gives an ambient open neighborhood of Y_i. The restricted h is its collar. Conversely choose pairwise disjoint ambient open neighborhoods U_i of the Y_i, using normality for a finite family. For a collar h_i:Y_i×[0,1]→T_i, the preimage of U_i∩T_i is open and contains the compact zero section Y_i×{0}. A finite subcover by product neighborhoods provides delta_i>0 such that h_i(Y_i×[0,delta_i]) lies in U_i. Each shortened strip is still a neighborhood of Y_i: the smaller relatively open product Y_i×[0,delta_i) intersects an ambient neighborhood contained in T_i. Rescaling each shortened interval and taking the finite disjoint union gives a bijective collar Y×[0,1]→the union of those strips. Continuity follows from the finite clopen decomposition of Y, and its inverse follows either piecewise from the disjoint U_i or from compactness of the domain and Hausdorffness of X. This proves both directions under the stated separation and indexing hypotheses. The source’s “une partie finie” is retained; it can mean a finite collection here and is not changed to H’s proposed famille.'),
 dict(id='N06',text='Counterexample to the weaker quasi-compact variant of N05, without a Hausdorff convention or an additional requirement that each collar neighborhood be closed in X. Form X from two copies of [0,1] by identifying equal t>0 and keeping their origins o_1,o_2 distinct. It is quasi-compact as a quotient of a finite disjoint union of compact intervals. Each {o_i} is closed. The subset U_i={o_i} union (0,1] is open in X and is homeomorphic to [0,1], so it is a product collar of its origin. The pair Y={o_1,o_2} is closed and discrete as a subspace. It has no collar: if Y×[0,1] embedded as a neighborhood T with the prescribed zero section, its two clopen product components, intersected with an ambient open neighborhood of Y contained in T, would give disjoint ambient open neighborhoods of the two origins. Every neighborhood of either origin contains a positive initial interval, so any two such neighborhoods intersect. This is a contradiction. The example refutes only that weakened interpretation of compact; it does not refute the manuscript statement under the customary compact-Hausdorff convention. If another page imposes closed collar neighborhoods or a separated-space convention, this particular example does not satisfy those strengthened hypotheses. No other page was consulted.'),
 dict(id='N07',text='Targeted typing diagnostic for the diagonal marginal map. The upper target is literally [0,1], while the lower rule is y↦(y,0). For a general topological space Y, the pair (y,0) is an element of Y×[0,1], not of [0,1]. Thus the written two-row map has a type mismatch unless an unstated special identification is imposed. The natural repaired target would be Y×[0,1], consistent with the preceding product isomorphism, but that repair is not put into the transcription. The upper connector itself has no secure head, so its direction is also left doubtful.'),
 dict(id='N08',text='The final lower index is J-shaped and is retained as J|I doubt beside the earlier clear I. If it is literally J and differs from I, the collection being unioned is not specified by the preceding clause, so N05 is a proof only for the intended same-index formulation, not a validation of an undefined J. Ink alone does not decide whether this is an authorial slip, a compressed I, or an unprovided convention. The operator bar(E)p_epsilon(T) has a true additional overbar above E only, a separate p and baseline (T); its interpretation is not used to remove the source’s separate first epsilon/delta ambiguity.'),
 dict(id='N09',text='Revision and punctuation diagnostics. The isolated raised É/E is not expanded to Évitons, and the slanted word structure is transcribed only in the margin where it is written. The two Y variables visibly overwrite earlier Z forms; both layers are preserved. The heavy initial cylindrique group does not yield an independently readable additional cancelled word. Both main homéom forms have no stop, but the marginal homéom. has a real dot. The source writes cônique twice. The isolated filled oval below faux is preserved as a graphic with no assigned punctuation attachment. The final le sont reaches the paper edge without a recoverable following full stop. A curved insertion leader at (absolu) and one at en général are attachment strokes, not extra parentheses/underlines. These are source-state decisions, not mathematical emendations.'),
]

events=[
 dict(statement_id=f'{PAGE}.N02',type='targeted proof check',outcome='Verified the X=T boundary counterexample mechanism; did not reconstruct unavailable formula (7).'),
 dict(statement_id=f'{PAGE}.N03',type='independent re-proof',outcome='Constructed mutually inverse continuous maps for the mapping cylinder of a homeomorphism and the product collar; converse by transport of structure, under the stated interpretation of cônique.'),
 dict(statement_id=f'{PAGE}.N04',type='targeted proof check',outcome='Constructed endpoint collar coordinates and disjoint endpoint substrips; checked only positive radii/nondegenerate strips and explicitly conditional interpretation of the undefined strip operator.'),
 dict(statement_id=f'{PAGE}.N05',type='independent re-proof',outcome='Proved the finite disjoint closed-union collar equivalence in compact Hausdorff X with a common finite index set; used normality and compactness/tube shrinking explicitly.'),
 dict(statement_id=f'{PAGE}.N06',type='refuted, with refined id',outcome='Refuted N05.Q, the weakened quasi-compact/non-Hausdorff version with collars merely neighborhoods, by the compact interval with two origins. This does not refute N05.H, the compact-Hausdorff same-index version proved in N05, nor a separately imposed closed-collar formulation.'),
 dict(statement_id=f'{PAGE}.N07',type='targeted proof check',outcome='Checked the types: y↦(y,0) naturally lands in Y×[0,1], while the manuscript target is [0,1]. Retained the written target and the connector uncertainty.'),
 dict(statement_id=f'{PAGE}.N08',type='targeted proof check',outcome='Separated the literal unresolved J/I index from the same-index hypothesis needed for the finite-union proof; no formula was silently regularized.'),
]

notation=[
 dict(form=r'T;\ \dot T;\ T_\lambda;\ \dot T_\lambda',meaning='Cone/collar object and its distinguished dotted/radial sections, retaining only the marks actually written; earlier construction is not defined anew on this leaf.',evidence='P02, P06–P09 and P11–P13: every plain T has one roof and upright; dotted forms add a distinct dot. No independent overbar occurs on these T forms.'),
 dict(form=r'\mathbf{I}',meaning='The interval factor in equality (9) and diagram (10).',evidence='P08/P09: thick filled upright with broad upper and lower serif bars; visually heavier than the thin index-set I of the final family.'),
 dict(form=r'\bar{\mathrm{E}}\mathrm{p}_\varepsilon(T)',meaning='Written operator attached to the listed boundary pieces; not defined on the assigned leaf. The strip interpretation in N04 is conditional.',evidence='P13: independent overbar above the E’s own upper arm, separate descending p, lowered epsilon, and (T) ending on the operator baseline.'),
 dict(form=r'\wr\!\vert',meaning='Vertical identification between T and Y×bold I, with no directed shaft.',evidence='P09: one curved upright beside one straight upright; neither has an arrowhead. This agrees with the supplied convention while being confirmed locally.'),
 dict(form=r'\deleted{Z}Y',meaning='Earlier Z overwritten by live Y in the two definition positions.',evidence='P04/P05: thin horizontal Z limbs remain below the heavier forked Y body.'),
 dict(form=r'\unsure{-|\longrightarrow}',meaning='Marginal upper connector, with an unheaded shaft preferred and an arrow not excluded.',evidence='P10: continuous horizontal stroke has a small terminal rise but no secure separate head.'),
 dict(form=r'\unsure{J|I}',meaning='Unresolved index-set letter below the final union, kept distinct from the earlier clear family index I.',evidence='P14: top stroke, descending body and pronounced left return give J-like shape; the earlier I is more upright.'),
]
abbreviations=[
 dict(form='i.e.',expansion='id est; c’est-à-dire'),
 dict(form='homéom',expansion='homéomorphisme'),
 dict(form='homéom.',expansion='homéomorphisme'),
 dict(form='ssi',expansion='si et seulement si'),
]
hand=[
 dict(habit='A T roof can be long and detached from its upright without being an added overbar.',places='150_scan014 P02, P06–P09, P11–P13',consistency='Holds for every plain T read on this leaf; the dotted forms supply repeated comparison with an actual added dot.',witness_errors='C puts a bar on all eight plain-T occurrences; H’s plain T agrees with the ink. The separate E overbar in P13 prevents generalizing this finding to all horizontal accents.'),
 dict(habit='The interval I in displays is deliberately thick with broad serif caps, whereas a family-index I is thin.',places='150_scan014 P08/P09 versus P14',consistency='Both display occurrences agree; the lower union index remains J/I ambiguous.',witness_errors='C’s plain display I loses the visible weight. H keeps bold I in the two displays. Both witnesses normalize the doubtful lower union index to I.'),
 dict(habit='Repeated cônique has a separate curved circumflex-like accent over o.',places='150_scan014 P06 and P11',consistency='The extra accent appears in both occurrences.',witness_errors='Both witnesses give conique without the written accent.'),
 dict(habit='The defined border term is short bord, with a tall looped d and no -ant extension.',places='150_scan014 P04, P11, P12, P13 and P14',consistency='All five term occurrences use bord/bords on this leaf.',witness_errors='H repeatedly expands it to bordant/bordants and adds de T in the first example; C retains the shorter source term.'),
 dict(habit='Abbreviation stops are locally variable and must be read separately.',places='150_scan014 P06/P07 versus P10',consistency='Both main homéom forms lack a stop; the marginal homéom. has an isolated dot.',witness_errors='C supplies stops in the two main occurrences; H expands those occurrences to homéomorphisme.'),
 dict(habit='Slanted marginal writing can overlap the apparent opening of a main-line revision.',places='150_scan014 P03/P10',consistency='The main raised capital is isolated; the slanted structure belongs to the marginal line.',witness_errors='H’s Évitons appears to join ink from different physical lines; the main insertion is only É/E.'),
 dict(habit='Overwriting Z by Y leaves both horizontal Z limbs under the darker forked Y.',places='150_scan014 P04/P05',consistency='Both definition variables show the same two-layer structure.',witness_errors='C treats each as a one-letter Y/Z choice; H retains the earlier Z only in the first occurrence.'),
]

coverage_text={
 1:'Macro/editorial-only: scanpage14 is an editorial locator; H’s upper note is not source prose. Written author number is P01a.',
 2:'P01a preserves the source closing parenthesis of 2); H’s remainder is editorial inference, excluded.',
 3:'P02b: literal reference (7), not H (8).',
 4:'P02d: present crossed group after T retained with lambda/attachment doubt.',
 5:'P02e: short word retained as pour|avec doubt; H leaves it unread.',
 6:'P03a/P03b and M0325: old opening doubtful On dira; isolated raised É/E, no expansion to Évitons; following enfin de unresolved.',
 7:'P04a: earlier Z remains under the live Y.',
 8:'P04a/M0326: the two layers replace C’s one-letter choice.',
 9:'P04b: paired upper quotation ticks, not angle quotes.',
 10:'P04b: literal underlined partie bord with no ante.',
 11:'P05b/P05c: cancelled collier, not collant; raised cylindrique initial overwork kept uncertain.',
 12:'P05d/M0327: second Z overwritten by Y, both layers retained.',
 13:'P06c: homéom without stop followed by long dash; no expansion.',
 14:'P07a: cancelled initial i.e. remains uncertain, preferred over H s’il; cancellation covers whole old phrase.',
 15:'P07b: small cancelled de-like group retained.',
 16:'P07d: second homéom without stop, no expansion.',
 17:'P09a: number (10) at left of complete diagram; display wrapper itself is macro-only.',
 18:'P09a: vertical curved-plus-straight sign, no horizontal simeq.',
 19:'P09a: no downward arrow shaft/head; phantom only positions the typeset vertical sign.',
 20:'P09a: left number placement; H’s explanatory note about its added arrow is editorial.',
 21:'P10a/M0328: définir la structure resolved from the diagonal line.',
 22:'P10b: voisinage cylindrique comme un homéom., not frontière/ellipsis.',
 23:'P10c: compatible avec is written before the two-row marginal map.',
 24:'P10d/M0329: full two-row marginal map; literal upper target [0,1], upper head uncertain.',
 25:'P10d: diagram closing syntax is macro-only; H’s note calling the margin illegible is editorial.',
 26:'P11c: doubtful tout retained under the strike, rather than absent/unread content.',
 27:'P11d/P12a: bord. with no de T, followed by a new line beginning doubtful donc.',
 28:'P12a: dotted T_lambda and est explicitly written; H omits them.',
 29:'P12b: bord, without ant.',
 30:'P13a: crossed Ep-like group includes a descending right-hand body; retained doubt.',
 31:'P13b: bords, without ant.',
 32:'P13c: live operator has E-bar and separate p.',
 33:'P13c: (T) is at operator baseline, not an exponent.',
 34:'P14a: final bord, without ant.',
 35:'P15a: thin folio13 preserved. H’s partie→famille suggestion is editorial; literal partie finie retained.',
}
diff_lines=(ROOT/'packets'/PAGE/'differences.tsv').read_text().splitlines()
assert len(diff_lines)-1 == len(coverage_text) == 35
diff_coverage=[dict(row=n,disposition=coverage_text[n]) for n in range(1,36)]

revisions=[
 dict(text=r'\inserted{en général}',scope_attachment='Raised phrase attaches after dire and before que in the first sentence.',evidence='P02: curved leader rises from before que toward the raised phrase; it is not an underline or added parenthesis.'),
 dict(text=r'\deleted{\unsure{_\lambda}}',scope_attachment='Small old group after the T in X=T, before the comma; lambda and its lowered position remain doubtful.',evidence='P02: separate upper crossing and descending loop/return, not part of T’s roof.'),
 dict(text=r'\deleted{\unsure{On dira}}',scope_attachment='Cancellation covers the entire old opening, ending before the following live compressed group.',evidence='P03: long stroke crosses O/n-like opening and later d/i; old ending obscured.'),
 dict(text=r'\inserted{\unsure{É|E}}',scope_attachment='Isolated capital directly above the cancelled opening; no inferred continuation.',evidence='P03 and separation provided by P10: raised E-like body belongs to main line; slanted structure belongs to margin.'),
 dict(text=r'fermée $\deleted{Z}Y$',scope_attachment='Earlier Z directly overwritten by Y after fermée.',evidence='P04: thin Z horizontals beneath heavy forked Y; old layer preserved before live layer.'),
 dict(text=r'\deleted{\uline{collier}}',scope_attachment='Whole underlined old word beneath the replacement cylindrique.',evidence='P05: strike crosses c/o, twin l loops and i/e/r ending; lower underline is separate.'),
 dict(text=r'\inserted{\uline{\unsure{c}ylindrique}}',scope_attachment='Raised underlined replacement attaches to voisinage-, replacing the old collier.',evidence='P05: word lies immediately above collier; black initial overwork is not resolved into another independent cancelled word.'),
 dict(text=r'de $\deleted{Z}Y$ dans $X$',scope_attachment='Second earlier Z overwritten by Y, after cylindrique de.',evidence='P05: the same two-layer horizontal Z/heavy Y structure as P04.'),
 dict(text=r'\deleted{tubulaire}',scope_attachment='First whole tubulaire cancelled before the live cônique T.',evidence='P06: line crosses the word from initial t to the final low ending; the following cônique is outside the strike.'),
 dict(text=r"\deleted{\unsure{i.e.} tel que l'on}",scope_attachment='Entire old phrase from the uncertain abbreviation through l’on, before live s’il existe.',evidence='P07: continuous cancellation crosses all of these words and stops before the new s’il.'),
 dict(text=r'\deleted{\unsure{de}}',scope_attachment='Small cancelled group between voisinage and T, independent of both.',evidence='P07: overcrossed looped group sits in the gap; reading de remains doubtful.'),
 dict(text=r'\deleted{tubulaire}',scope_attachment='Second whole tubulaire in the example, before live cônique.',evidence='P11: horizontal strike traverses its tall initial/middle stems and low ending but not cônique.'),
 dict(text=r'\inserted{(absolu)}',scope_attachment='Raised parenthesized word attaches before de in the example.',evidence='Full lower half and P11: literal round parentheses surround absolu; the lower curved leader bends toward de and is not another parenthesis or underline. The crop includes the latter part; the blind box extends left to cover the whole insertion.'),
 dict(text=r'\deleted{\unsure{tout}}',scope_attachment='Cancelled word after de and before Y in the example.',evidence='P11: visible initial t and low body under a heavy stroke, stopping before Y; doubt retained.'),
 dict(text=r'\deleted{\unsure{\mathrm{Ep}}}',scope_attachment='Cancelled group immediately before the first dotted T in the strip list.',evidence='P13: crossed E-like strokes and right descending loop; no deletion of the following dotted T or radial factors is inferred.'),
 dict(text=r'\deleted{Dans}',scope_attachment='Whole old Dans cancelled before live Si X.',evidence='P13: a long stroke crosses the large D loop and following low a/n/s body; Si X lies to its right outside the strike.'),
]

report=dict(page=PAGE,reader='reader_c',line_count=21,changes=changes,decisions=decisions,
            inventory=inventory,audit_boxes=audits,doubts=doubts,notes=notes,check_events=events,
            notation=notation,abbreviations=abbreviations,hand=hand,diff_coverage=diff_coverage,
            deletion_insertion_review=revisions)

mark_ids=[x.split('\t')[0] for x in (ROOT/'packets'/PAGE/'marks.tsv').read_text().splitlines()[1:]]
assert [x['id'] for x in decisions] == mark_ids
assert len({x['id'] for x in changes}) == len(changes)
assert set(report)=={'page','reader','line_count','changes','decisions','inventory','audit_boxes','doubts',
                     'notes','check_events','notation','abbreviations','hand','diff_coverage',
                     'deletion_insertion_review'}
assert len(BOX)==15
for item in changes+decisions:
    assert (ROOT/'work'/item['crop']).is_file()
for item in audits:
    x0,y0,x1,y1=item['xyxy']
    assert 0<=x0<x1<=1685 and 0<=y0<y1<=2363
assert D.count('{')==D.count('}'), 'unbalanced braces'
assert D.count(r'\begin{tikzcd}')==D.count(r'\end{tikzcd}')==2
assert D.count(r'\begin{tikzpicture}')==D.count(r'\end{tikzpicture}')==1
assert r'\bar T' not in D
assert r'\illegible' not in D
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':PAGE,'changes':len(changes),'marks':len(decisions),
                  'audit_boxes':len(audits),'inventory':len(inventory),'crops':len(BOX),
                  'diff_rows':len(diff_coverage),'doubts':len(doubts)},ensure_ascii=False))
