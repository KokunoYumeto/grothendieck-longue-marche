from pathlib import Path
import json
import math

ROOT = Path('/workspace/scratch/8759b8008681')
OUT = ROOT / 'work/reports/150_scan018'
PAGE = '150_scan018'
BOXES = json.loads((OUT / 'crop_boxes.json').read_text())

draft = r'''\scanpage{18}
\mspage{4)}
On dit qu'une partie-bord \inserted{$B$ de $X$} est \uline{compatible} avec
une famille de parties $X_i$ de $X$, s'il
existe un voisinage cylindrique qui est
compatible \inserted{(au sens cylindrique\unsure{)}} avec chacun des $X_i$.
% P03: the possible closing arc meets the descending y of the main-line cylindrique.
\margin{utiliser plutôt la terminologie de \uline{transversalité}}

Revenons : $Y\subset X$ et un voisinage
cônique \inserted{\uuline{strict}} $T$ de $Y$. On dit que $T$ est
\inserted{\uline{strictement}} compatible avec une famille de $X_i\subset X$
si \inserted{elle est compatible avec chaque $X_i$
$(X_i\cap T=\mathbf I.X_i\cap\dot T-)$, et si}
$\dot T$ est un sous-espace bord de
$X^*=X\setminus\mathring T$, compatible avec la famille des
$X_i^*=X^*\cap X_i$. Donc cela implique que
$X_i\cap\dot T$ est un sous-espace bord (non seule-
ment de $X_i\cap T$, mais aussi) de $X_i^*$.
% P08: seule-/ment is the manuscript's physical word division.
\margin{\deleted{\unsure{appeler transversalité ?}}}
% P09: the crossed question-mark area also has an extra dot-like residue.
\margin{\unsure{On dira} que $X_i$ est
\deleted{\uline{\unsure{strictement}}}\uline{transversal}
\deleted{compatible \unsure{avec $T$|avec $\bar T$}}
\deleted{si $X_i\cap Y=0.\unsure{\dot X_i|X_i}$}
\unsure{dire|désir} : \unsure{transversalité}
\deleted{stricte} \unsure{transversalité} :
\[
-\quad 0.\dot X_i=X_i\cap Y
\]
i.e. $X_i=\overline{X_i\setminus X_i\cap Y}$}
% P10: the large cross/return after the marginal final Y is main-text X_i;
% the lower descending line is main-text ment. They are not repeated in this margin.

\textcircled{4}. \deleted{Soit} Un voisinage cônique (absolu)
$T\deleted{\unsure{_\varepsilon}}$ de
$Y$ est dit \uline{équisingulier} si $\dot T\overset{-}{\unsure{\relbar\joinrel\relbar|\longrightarrow}}Y$ est une
% P12: the upper short dash is independently present; its role is not established.
fibration loc. triviale. Il est dit \uline{equisingulier}
\uline{pour une famille} \uline{de} $T_i\subset T$, si \uline{de plus}
les $Y_i$ sont coniques, et $\dot T_i\longrightarrow Y$ sont des
fibrations localement triviales --- et \unsure{même}
% P15: the initial letters are overworked; no independent whole-word cancellation is secure.
\margin{17}
'''
(OUT / 'draft.tex').write_text(draft)

changes = []
def change(id, place, p, c, h, final, evidence, *, confidence='high', kind='misread word', against_c=False, against_h=True, marked_in_h=False, consequential=False, error_category=2):
    changes.append(dict(id=id, place=place, c=c, h=h, final=final, evidence=evidence,
                        crop=f'crops/{PAGE}_{p}.png', box=BOXES[p], confidence=confidence,
                        kind=kind, against_c=against_c, against_h=against_h,
                        marked_in_h=marked_in_h, consequential=consequential,
                        error_category=error_category))

change('P01_a', 'Upper-left author number', 'P01', r'\mspage{4}', '« 4) »', r'\mspage{4)}',
       'The angular 4 is followed by a long independent closing curve. C drops this written closing parenthesis; H explicitly records it.',
       kind='other', against_c=True, against_h=False, error_category=10)
change('P02_a', 'Opening compound', 'P02', 'partie-bord', 'partie bordante', 'partie-bord',
       'An independent short hyphen joins partie to bord. The second member has b, a low o/r run and a final d ascender; there is no following ante sequence.')
change('P02_b', 'Insertion and verb immediately after partie-bord', 'P02',
       r'\inserted{$B$ de $X$} est', r'\add{$B$ de $X$} \struck{est} est', r'\inserted{$B$ de $X$} est',
       'B de X is above the line. Its curved attachment passes above the one visible est; no separate crossed est or second verb body is present.',
       kind='text not on the page', error_category=9)
change('P03_a', 'Parenthetical insertion after compatible', 'P03',
       r'compatible \inserted{(au sens cylindrique)} avec',
       r'cylindrique \add{(ou \uncertain{semi-cylindrique})} qui est compatible avec',
       r'compatible \inserted{(au sens cylindrique\unsure{)}} avec',
       'The insertion has au (closed a body, then u), separate sens, and the long y descender and ending of cylindrique. Its lower curved line returns to the gap after compatible, before avec. The opening parenthesis is independent; the short possible closing arc meets the main-line y descender and remains locally doubtful. This added punctuation doubt alone is not a departure from C.',
       confidence='medium', kind='insertion or placement', marked_in_h=True, error_category=6)
change('P03_b', 'End of opening paragraph', 'P03', 'chacun', 'chacune', 'chacun',
       'After the final n shoulder the pen leaves the word for des; there is no separate e loop or extra low body.')
change('P04_a', 'Upper transverse marginal note', 'P04',
       r'\margin{utiliser plutôt la terminologie de \uline{transversalité}.}',
       r'\marginal{\uncertain{utiliser} \uncertain{plutôt} \uncertain{la} terminologie \uncertain{« transversale »}}',
       r'\margin{utiliser plutôt la terminologie de \uline{transversalité}}',
       'The three slanted lines yield utiliser plutôt la / terminologie de / transversalité. The last word continues through a tall t and terminal accented e rather than ending in le; no quote marks are present. One separate line lies below that word. No independent terminal full stop is recoverable after it, so C’s stop is not supplied.',
       confidence='medium', against_c=True, marked_in_h=True)
change('P05_a', 'After Revenons; M0342', 'P05', r'\unsure{à|:}', ':', ':',
       'Two detached, vertically arranged dark points are visible. There is no a body or separate grave accent. This resolves C’s doubt to its alternative, colon.',
       kind='other', against_c=True, against_h=False, error_category=10)
change('P05_b', 'First conic-neighbourhood adjective', 'P05', 'conique', 'conique', 'cônique',
       'A separate shallow arch/near-horizontal accent lies over the o. Its shallow form does not justify erasing the independently visible accent.',
       kind='abbreviation expanded or spelling modernised', against_c=True, error_category=8)
change('P05_c', 'Inserted strict', 'P05', r'\inserted{\uuline{strict}}', r'\add{strict}', r'\inserted{\uuline{strict}}',
       'There are two short, parallel underline strokes under strict, and a third, differently curved attachment leader into the line before T. The two underlines are not that leader.',
       kind='other', error_category=10)
change('P05_d', 'First T after inserted strict', 'P05', r'$\bar T$ de $Y$', r'$T$ de $Y$', r'$T$ de $Y$',
       'This T has one long roof and a looped/retraced upright below it. The higher bent line belongs to the insertion leader; there is no second horizontal bar over T.',
       kind='misread symbol or index', against_c=True, against_h=False, consequential=True, error_category=1)
change('P05_e', 'T after On dit que', 'P05', r'On dit que $\bar T$ est', r'On dit que $T$ est', r'On dit que $T$ est',
       'The second T has a heavily filled stem and one thick cap only. The dark stem is retracing, not a separate bar or a secure cancellation.',
       kind='misread symbol or index', against_c=True, against_h=False, consequential=True, error_category=1)
change('P06_a', 'Emphasis scope at strictement compatible', 'P06',
       r'\inserted{\uline{strictement}} compatible', r'\add{\emph{strictement}} \emph{compatible}',
       r'\inserted{\uline{strictement}} compatible',
       'strictement has one underline (completed by P17). The longer bent line turns into its attachment before compatible; no independent underline lies beneath compatible.',
       kind='other', error_category=10)
change('P06_b', 'Opening of the long insertion', 'P06',
       r'si \inserted{elle est compatible avec chaque $X_i$', r"\add{s'il est compatible avec chaque $X_i$",
       r'si \inserted{elle est compatible avec chaque $X_i$',
       'The main line already has si. The raised opening has the e body and two tall l stems of elle, followed by est. It is not the compact s-apostrophe-il reported by H.',
       kind='misread word', consequential=True)
change('P06_c', 'Interval symbol inside inserted formula', 'P06', r'I.', r'\mathbf{I}.', r'\mathbf I.',
       'The I has a very heavily filled vertical body and conspicuous top and bottom serifs, unlike the thin T stems nearby. The following multiplication point is independent.',
       kind='misread symbol or index', against_c=True, against_h=False, error_category=1)
change('P06_d', 'End of inserted formula', 'P06', r'\dot T-', r'\dot T\ldots', r'\dot T-',
       'Immediately after dotted T there is one short horizontal dash before the closing parenthesis, not a run of dots. The literal terminal dash is retained without an operand being supplied.',
       kind='misread symbol or index', consequential=True, error_category=1)
change('P06_e', 'Raised et si attachment', 'P06', r', et si}', r'$)}, et si', r', et si}',
       'et si is written in the raised insertion zone under its opening and attaches back to the main dotted T. It is included in the insertion, not placed as an independently surviving baseline clause.',
       kind='insertion or placement', error_category=6)
change('P06_f', 'First sous-espace bord', 'P06', 'un sous-espace bord de', 'un sous-espace bordant de', 'un sous-espace bord de',
       'The tall initial b, flattened o/r and final d are followed directly by de. No a-n-t continuation is visible.')
change('P07_a', 'Inference after the two X-star formulas', 'P07', 'Donc cela', r'\emph{Dans} \uncertain{ce cas}', 'Donc cela',
       'The first word begins with a tall rounded D followed by the low onc run; the second has the tall l and final a of cela. There is no second word cas and no independent underline.',
       marked_in_h=True)
change('P08_a', 'Second sous-espace bord', 'P08', 'un sous-espace bord (non seulement', 'un sous-espace bordant (non seulement', 'un sous-espace bord (non seule-',
       'bord again ends at the d ascender, before the open parenthesis. It has no ante/ant continuation. The line-end word division is separately recorded in P08_b.')
change('P08_b', 'Physical line division in seulement', 'P08', 'non seulement', 'non seulement', 'non seule-\nment',
       'A short horizontal hyphen follows seule at the end of the first line; ment begins the next line. The draft retains this written line division, without treating it as a different lexical word.',
       kind='omission', against_c=True, error_category=3)
change('P09_a', 'Small crossed transverse note', 'P09', r'\deleted{\unsure{appeler transversalité ?}}', r'\struck{\ill{}}', r'\deleted{\unsure{appeler transversalité ?}}',
       'Broad crossing strokes clearly cancel the small note. The two descending p-like stems, a high l loop, and parts of the following transvers- run support the retained candidates, but not every letter survives. The terminal question-mark-like stroke has an extra dot-like residue. C’s under-strike doubt is retained.',
       confidence='low', kind=r'readable ink left as \ill{}', marked_in_h=True, error_category=5)
change('P10_a', 'Opening words of the large margin', 'P10', 'On dira que', '[not transcribed]', r'\unsure{On dira} que',
       'The opening has compressed linked rounded and tall strokes before the clearer que. On dira remains the preferred candidate with a local doubt; it is not expanded. H omits these words. Added doubt alone is not counted against C.',
       confidence='low', kind='omission', error_category=3)
change('P10_b', 'Initial marginal Xi and est', 'P10', '$X_i$ est', '$X_i^{*}$', '$X_i$ est',
       'The X has a low i beside it, followed by the small est group. No independent superscript star belongs to this slanted marginal X; neighbouring upright main-text strokes are excluded.',
       confidence='medium', kind='misread symbol or index', consequential=True, error_category=1)
change('P10_c', 'Cancelled underlined modifier in the large margin', 'P10', r'\deleted{\uline{\unsure{strictement}}}', '[not transcribed]', r'\deleted{\uline{\unsure{strictement}}}',
       'A short word beneath the opening is crossed through its bodies and has a separate lower underline. Tall t strokes and the compressed central run support strictement, but crossing strokes prevent all-letter resolution.',
       confidence='low', kind='omission', error_category=3)
change('P10_d', 'Live transversal in the large margin', 'P10', r'\uline{transversal}', r'\uncertain{transversal}', r'\uline{transversal}',
       'The live word has a distinct line beneath it, ending before the following crossed phrase. The terminal tall l is visible; no final té is added here. The source underline is absent from H’s encoding.',
       confidence='medium', kind='other', marked_in_h=True, error_category=10)
change('P10_e', 'Cancelled compatible-with-T phrase', 'P10', r'\deleted{compatible \unsure{avec $\bar T$}}', '[not transcribed]', r'\deleted{compatible \unsure{avec $T$|avec $\bar T$}}',
       'A long strike crosses compatible and the following crowded group. The latter remains doubtful; a plain T is preferred because no independent second cap can be isolated, while C’s barred-T candidate is retained as an alternative. No cancellation is inferred from blackness alone.',
       confidence='low', kind='omission', against_c=True, consequential=True, error_category=3)
change('P10_f', 'First cancelled marginal equality', 'P10',
       r'\deleted{si $X_i\cap Y=0.\unsure{X_i}$}', r'$\dot X_i\cap Y=0.\dot X_i$',
       r'\deleted{si $X_i\cap Y=0.\unsure{\dot X_i|X_i}$}',
       'A continuous strike traverses si and the entire equality. The left X has no independent dot. A distinct dark point is visible above the right X, but its relation to surrounding overlaid strokes remains uncertain, so dotted X_i is preferred with plain X_i retained. The zero, multiplication point, intersection and Y remain visible.',
       confidence='medium', kind='deletion state (struck given live or live given struck)', against_c=True, consequential=True, error_category=7)
change('P10_g', 'Marginal dire and colon', 'P10', r'\unsure{dire|désir} :', r'\uncertain{dire}', r'\unsure{dire|désir} :',
       'After the tall initial d and compressed middle letters, two detached colon points are visible. The word itself remains dire|désir; only the written colon, absent in H, is added to its representation.',
       confidence='medium', kind='omission', marked_in_h=True, error_category=3)
change('P10_h', 'First doubtful transversalité after dire', 'P10', r'\unsure{transversalité}', r'\uncertain{transversaux}', r'\unsure{transversalité}',
       'The extended candidate ends with a tall t-like stroke and a small terminal body, not a clearly formed aux cluster. Internal strokes are crowded by returns from above, so C’s candidate remains doubtful rather than resolved.',
       confidence='low', marked_in_h=True)
change('P10_i', 'Cancelled stricte in lower margin', 'P10', r'\deleted{stricte}', r'\uncertain{strict}', r'\deleted{stricte}',
       'The word is traversed by a strike, with an additional low ending after the final t consistent with e. It is not retained as an unstruck strict.',
       confidence='medium', kind='deletion state (struck given live or live given struck)', marked_in_h=True, error_category=7)
change('P10_j', 'Second doubtful transversalité and colon', 'P10', r'\unsure{transversalité} :', '[not transcribed]', r'\unsure{transversalité} :',
       'A second long live word and its terminal colon occur after the cancelled stricte. The tall initial t and later t-like upright support transversalité, but the flattened interior remains uncertain. It is not the earlier word duplicated editorially.',
       confidence='low', kind='omission', error_category=3)
change('P10_k', 'Short dash before the live zero-image equality', 'P10', r'0.\dot X_i=X_i\cap Y', r'$0.\dot X_i=X_i\cap Y$', r'-\quad 0.\dot X_i=X_i\cap Y',
       'A short dark horizontal dash precedes the live equality at original approximately (51,1472). It is in the transverse margin, not an upright-text overlap. Its punctuation/minus role is not forced; the stroke is retained.',
       kind='omission', against_c=True, error_category=3)
change('P10_l', 'Final marginal closure formula', 'P10', r'$X_i=\overline{X_i\setminus X_i\cap Y}$', r'$\dot X_i=X_i\setminus X_i\cap Y$', r'$X_i=\overline{X_i\setminus X_i\cap Y}$',
       r'The initial X_i has no independent dot. A continuous line lies above the full right-hand X_i\setminus X_i\cap Y expression, at the height of an overbar, not below as an underline. The nearby large cross and descending line map to upright main-text X_i and ment and are excluded.',
       kind='misread symbol or index', consequential=True, error_category=1)
change('P11_a', 'Second conic-neighbourhood adjective', 'P11', 'conique (absolu)', 'conique (absolu)', 'cônique (absolu)',
       'A short detached shallow accent is visible above the o. The overworked initial c remains live; no separate cancellation crossing the entire word is established.',
       kind='abbreviation expanded or spelling modernised', against_c=True, error_category=8)
change('P11_b', 'T in the absolute-neighbourhood definition', 'P11', r'$\bar T\deleted{\unsure{_\varepsilon}}$', r'$T$', r'$T\deleted{\unsure{_\varepsilon}}$',
       'One cap and one retraced vertical define T. The lower horizontal strike belongs to the small subscript group, not an extra upper bar. The subscript is separately retained as cancelled and doubtful.',
       kind='misread symbol or index', against_c=True, against_h=False, consequential=True, error_category=1)
change('P11_c', 'Cancelled subscript after the same T', 'P11', r'\deleted{\unsure{_\varepsilon}}', '[not transcribed]', r'\deleted{\unsure{_\varepsilon}}',
       'A small lower curl immediately after T is crossed by a horizontal stroke extending to the right. Its epsilon-like body is not fully separated from that stroke, so the subscript candidate remains doubtful rather than being omitted or resolved.',
       confidence='low', kind='omission', error_category=3)
change('P12_a', 'Whole first dotted-T relation; M0346', 'P12',
       r'$\dot T\unsure{-|\longrightarrow}Y$', r'$\dot T\to Y$',
       r'$\dot T\overset{-}{\unsure{\relbar\joinrel\relbar|\longrightarrow}}Y$',
       'The whole formula has dotted T, a long lower shaft with a slight upward bend but no separately visible arrowhead, Y, and a separate short upper dash. The extra upper dash must survive. The lower shaft’s status remains undecided; the upper dash is not silently interpreted as an equality or a conventional arrow label.',
       confidence='medium', kind='misread symbol or index', against_c=True, consequential=True, error_category=1)
change('P13_a', 'Second equisingulier', 'P13', 'équisingulier', 'équisingulier', 'equisingulier',
       'Unlike the first occurrence in P12, this initial e has no independent accent stroke above it. The small dark initial body belongs to the letter itself. The source’s unaccented second spelling is retained.',
       confidence='medium', kind='abbreviation expanded or spelling modernised', against_c=True, error_category=8)
change('P13_b', 'Family formula and underline scope', 'P13',
       r'\uline{équisingulier'+ '\n' + r'pour une famille de} $\bar T_i\subset\bar T$',
       r'\emph{équisingulier pour une famille de $T_i\subset T$}',
       r'\uline{equisingulier}'+ '\n' + r'\uline{pour une famille} \uline{de} $T_i\subset T$',
       r'Both T letters have one roof; their forked/retraced bodies do not supply another bar. Underlines lie under the adjective, then pour une famille, then separately de. No independent underline extends beneath the formula T_i\subset T, contrary to H’s full emphasis span. The accent issue is recorded separately in P13_a.',
       kind='misread symbol or index', against_c=True, consequential=True, error_category=1)
change('P13_c', 'Emphasis at de plus', 'P13', r'\uline{de plus}', r'de \emph{plus}', r'\uline{de plus}',
       'The low underline begins under the tail of de and continues under plus. It does not include si. The de is part of the underlined group.',
       confidence='medium', kind='other', error_category=10)
change('P14_a', 'Literal subject of sont coniques', 'P14', r'les $Y_i$ sont coniques', r'les $T_i$ sont coniques', r'les $Y_i$ sont coniques',
       'The initial variable has an open fork and descending stem, with no horizontal T roof. It is Y_i, unlike the separately roofed dotted T_i later on this line. The literal source variable is retained.',
       kind='misread symbol or index', consequential=True, error_category=1)
change('P15_a', 'Final word; M0347', 'P15', r'\unsure{même}', r'\uncertain{\ill{}}', r'\unsure{même}',
       'The detached circumflex, later low m/e run and the overworked opening support même. The initial group has horizontal retracing/crossing, so the whole word remains locally doubtful; a whole-word cancellation is not established. No terminal stop is supplied.',
       confidence='medium', kind=r'readable ink left as \ill{}', marked_in_h=True, error_category=5)
change('P16_a', 'Thin lower-left foliation', 'P16', r'\margin{17}', '[not transcribed]', r'\margin{17}',
       'The thin oblique-to-vertical first digit and the separate arched 7 with its crossbar read 17. This is recorded separately from the author’s heavy 4) and circled 4; attribution of the thin foliation is indeterminate.',
       kind='omission', error_category=3)

decisions = []
def decision(id, p, choice, reading, evidence, confidence):
    decisions.append(dict(id=id,cote='150',scan='18',decision=choice,reading=reading,
                          evidence=evidence,crop=f'crops/{PAGE}_{p}.png',box=BOXES[p],confidence=confidence))
decision('M0342','P05','alternative',':','Two vertically separated points; no a body or grave stroke.','high')
decision('M0343','P10','undecided',r'\unsure{dire|désir}',
         'Tall initial d and compressed middle/end strokes favour dire, but their separation does not securely exclude désir; colon is independent.','medium')
decision('M0344','P10','undecided',r'\unsure{transversalité}',
         'First long candidate after dire has tall t-like strokes and a terminal small body; the central run is crossed/overlapped by returns from above.','low')
decision('M0345','P10','undecided',r'\unsure{transversalité}',
         'Second long live candidate after cancelled stricte is a separate occurrence; t-like initial and later upright are visible, but flattened middle letters are not all separable.','low')
decision('M0346','P12','undecided',r'\dot T\overset{-}{\unsure{\relbar\joinrel\relbar|\longrightarrow}}Y',
         'Long lower unheaded/bent shaft plus an independent short upper dash. Both strokes are retained; no secure arrowhead settles the lower shaft.','medium')
decision('M0347','P15','undecided',r'\unsure{même}',
         'Circumflex and later m/e run support même, but the initial group remains overworked and its local crossing state is not separable.','medium')

inventory = []
def inv(kind, position, text, hand='his hand'):
    inventory.append(dict(scan=PAGE,sheet_kind='text',hand=hand,element=f'E{len(inventory)+1:02d}',
                          kind=kind,position=position,first_words_or_objects=text,transcribed='yes'))
inv('text','upper-left corner', '4) author number')
inv('text','upper main block', "On dit qu’une partie-bord ... chacun des X_i.")
inv('insertion','above first line after partie-bord', 'B de X')
inv('insertion','above/below the end of the opening block, after compatible', '(au sens cylindrique; closing arc doubtful)')
inv('margin note','upper left, slanted', 'utiliser plutôt la terminologie de transversalité')
inv('text','central main block', 'Revenons : Y⊂X ... de X_i^*.')
inv('insertion','above first central T', 'strict, double underlined')
inv('insertion','above central compatible', 'strictement, single underline and distinct leader')
inv('insertion','above si dotted-T est...', 'elle est compatible ... (X_i∩T=I.X_i∩dotT-), et si')
inv('margin note','left, small crossed transverse group', 'appeler transversalité ?; locally doubtful')
inv('deletion','same small transverse group', 'whole small note crossed')
inv('margin note','left, larger transverse group', r'On dira que X_i est ... i.e. X_i=overline(X_i\X_i∩Y)')
inv('deletion','large margin, under its opening', 'underlined strictement, locally doubtful')
inv('deletion','large margin after live underlined transversal', 'compatible avec T; latter group locally doubtful')
inv('deletion','large margin, first si equality', 'si X_i∩Y=0.(dot X_i|X_i)')
inv('deletion','large margin between two transversalité candidates', 'stricte')
inv('display','large margin, next-to-last formula line', '- 0.dot X_i=X_i∩Y')
inv('display','large margin, final formula line', r'i.e. X_i=overline(X_i\X_i∩Y)')
inv('text','lower definition heading', 'circled 4 with separate point')
inv('deletion','after circled 4', 'Soit')
inv('text','lower main block', 'Un voisinage cônique (absolu) T ... et même')
inv('deletion','subscript immediately after the lower T', 'epsilon-like cancelled subscript')
inv('text','first equisingular relation in lower block', 'dot T, short upper dash over long lower unheaded shaft, Y')
inv('text','end of final main line', 'même, with overworked initial letters; state uncertain')
inv('margin note','bottom left', 'thin 17', 'attribution indeterminate')

audit_boxes = []
def audit(box, kinds, reading, scope=None):
    d=dict(box=f'B{len(audit_boxes)+1:02d}',kind='; '.join(kinds),xyxy=box,reading=reading)
    if scope: d['scope']=scope
    audit_boxes.append(d)

audit(BOXES['P01'],['handwritten number'],r'\mspage{4)}')
audit(BOXES['P02'],['insertion','C/H different words'],
      r"On dit qu'une partie-bord \inserted{$B$ de $X$} est \uline{compatible} avec",
      'Target the upper main sentence and its raised B de X insertion; the following family line is separately covered.')
audit([280,145,1625,253],['handwritten number'],r"une famille de parties $X_i$ de $X$, s'il",
      'Target the family line, including its subscript i, not the slanted marginal note.')
audit(BOXES['P03'],['insertion','C/H different words','handwritten number','less than high confidence departure'],
      r'existe un voisinage cylindrique qui est compatible \inserted{(au sens cylindrique\unsure{)}} avec chacun des $X_i$.',
      'Main two-line continuation plus its inserted parenthetical; exclude the transverse note at left.')
audit(BOXES['P04'],['margin note','C/H different words','less than high confidence departure'],
      r'\margin{utiliser plutôt la terminologie de \uline{transversalité}}',
      'Only the three slanted marginal lines; clockwise rotation 40 degrees. Exclude upright main-text fragments at the lower/right edge.')
audit(BOXES['P05'],['insertion','C/H different words','doubtful formula'],
      r'Revenons : $Y\subset X$ et un voisinage cônique \inserted{\uuline{strict}} $T$ de $Y$. On dit que $T$ est',
      'The two main lines and raised strict; both T caps and the colon are included.')
audit([195,635,700,810],['insertion','C/H different words'],
      r'\inserted{\uline{strictement}} compatible',
      'Target the entire raised modifier, its underline/leader, and the baseline word to which it attaches; exclude the preceding conic-neighbourhood line.')
audit([680,710,1667,815],['handwritten number'],r'avec une famille de $X_i\subset X$',
      'Target the main-line family phrase and the entire X_i⊂X formula; exclude the smaller inserted row below.')
audit(BOXES['P06'],['insertion','doubtful formula','handwritten number','C/H different words'],
      r'si \inserted{elle est compatible avec chaque $X_i$ $(X_i\cap T=\mathbf I.X_i\cap\dot T-)$, et si} $\dot T$ est un sous-espace bord de',
      'Target the original si and the lower main dotted-T clause together with the entire intervening raised insertion; exclude the preceding main family line and strictement already targeted separately.')
audit(BOXES['P07'],['handwritten number','C/H different words'],
      r'$X^*=X\setminus\mathring T$, compatible avec la famille des $X_i^*=X^*\cap X_i$. Donc cela implique que',
      'Two upright main lines, including all stars, indices and hollow circle; exclude transverse marginal overlap at left.')
audit(BOXES['P08'],['handwritten number','C/H different words'],
      '$X_i\\cap\\dot T$ est un sous-espace bord (non seule-\nment de $X_i\\cap T$, mais aussi) de $X_i^*$.',
      'Two upright main lines, including the written line-end hyphen and ment continuation. Their strokes also intrude into the rotated large-margin frame.')
audit(BOXES['P09'],['margin note','struck passage','C/H different words','less than high confidence departure'],
      r'\margin{\deleted{\unsure{appeler transversalité ?}}}',
      'Only the small upper crossed note after clockwise rotation45; exclude the beginning of the larger marginal note below.')

def inverse_rotated_rectangle(rect):
    # P10: native crop464×730, Pillow expanded clockwise45 to846×846, then scaled to2600×2600.
    points=[]
    for x in (rect[0],rect[2]):
        for y in (rect[1],rect[3]):
            dx=x*846/2600-423
            dy=y*846/2600-423
            points.append((248+(dx+dy)/math.sqrt(2),1220+(-dx+dy)/math.sqrt(2)))
    return [max(16,math.floor(min(x for x,y in points))),max(855,math.floor(min(y for x,y in points))),
            min(480,math.ceil(max(x for x,y in points))),min(1585,math.ceil(max(y for x,y in points)))]

audit(inverse_rotated_rectangle([1000,545,1940,830]),
      ['margin note','handwritten number','C/H different words','less than high confidence departure'],
      r'\unsure{On dira} que $X_i$ est',
      'First line of the large transverse note, clockwise45. Do not read the small cancelled note above, nor the upright-body fragments at right.')
audit(inverse_rotated_rectangle([800,705,1290,930]),
      ['margin note','struck passage','C/H different words','less than high confidence departure'],
      r'\deleted{\uline{\unsure{strictement}}}',
      'Short crossed-and-underlined marginal word below the opening, left of the next live underlined word after clockwise45.')
audit(inverse_rotated_rectangle([1300,765,2580,1045]),
      ['margin note','struck passage','C/H different words','less than high confidence departure','doubtful formula'],
      r'\uline{transversal} \deleted{compatible \unsure{avec $T$|avec $\bar T$}}',
      'Live underlined marginal word followed by the crossed phrase on the same transverse row. Exclude the upright main-text X-star crossing below/right.')
audit(inverse_rotated_rectangle([685,935,1785,1160]),
      ['margin note','struck passage','doubtful formula','handwritten number','C/H different words','less than high confidence departure'],
      r'\deleted{si $X_i\cap Y=0.\unsure{\dot X_i|X_i}$}',
      'The first crossed marginal equality only; retain its initial si and both sides. Exclude the independent lower live equality and upright main text.')
audit(inverse_rotated_rectangle([440,1040,1840,1235]),
      ['margin note','C/H different words','less than high confidence departure'],
      r'\unsure{dire|désir} : \unsure{transversalité}',
      'The transverse row immediately below the crossed equality, with its initial colon. Overlapping long descenders from above are not new words.')
audit(inverse_rotated_rectangle([430,1195,2090,1415]),
      ['margin note','struck passage','C/H different words','less than high confidence departure'],
      r'\deleted{stricte} \unsure{transversalité} :',
      'Next transverse row, beginning with the crossed word and ending at the colon. Exclude upright-body fragments to the right.')
audit(inverse_rotated_rectangle([295,1305,1355,1515]),
      ['margin note','doubtful formula','handwritten number','C/H different words'],
      r'-\quad 0.\dot X_i=X_i\cap Y',
      'The live zero-image equality with its separate leading dash; include the dot over the first X, but no dot over the right X.')
audit(inverse_rotated_rectangle([120,1485,1160,1755]),
      ['margin note','doubtful formula','handwritten number','C/H different words'],
      r'i.e. $X_i=\overline{X_i\setminus X_i\cap Y}$',
      'Last transverse formula and its preceding abbreviation. Exclude the adjacent large rotated cross/return, which is upright main-text X_i, and the lower long line, which is upright ment.')
audit(BOXES['P11'],['handwritten number','struck passage','doubtful formula','C/H different words','less than high confidence departure'],
      r'\textcircled{4}. \deleted{Soit} Un voisinage cônique (absolu) $T\deleted{\unsure{_\varepsilon}}$ de',
      'Entire lower heading line including circled number, separate point, cancelled word, accent and crossed subscript.')
audit(BOXES['P12'],['doubtful formula','C/H different words','less than high confidence departure'],
      r'$Y$ est dit \uline{équisingulier} si $\dot T\overset{-}{\unsure{\relbar\joinrel\relbar|\longrightarrow}}Y$ est une',
      'Entire first equisingular line; preserve the independently visible short upper dash and the long lower relation shaft.')
audit([290,1810,1645,1915],['C/H different words','less than high confidence departure'],
      r'fibration loc. triviale. Il est dit \uline{equisingulier}',
      'Upper line of P13, including both abbreviation/sentence stops and the unaccented second adjective.')
audit([290,1910,1645,2045],['doubtful formula','handwritten number','C/H different words','less than high confidence departure'],
      r'\uline{pour une famille} \uline{de} $T_i\subset T$, si \uline{de plus}',
      'Lower line of P13, distinguishing the separate underline under de, the un-underlined formula, and de plus.')
audit(BOXES['P14'],['handwritten number','C/H different words'],
      r'les $Y_i$ sont coniques, et $\dot T_i\longrightarrow Y$ sont des',
      'Whole line: literal Y_i at left, unaccented coniques, and a definite headed arrow in the later dotted-T_i formula.')
audit(BOXES['P15'],['C/H different words','less than high confidence departure'],
      r'fibrations localement triviales --- et \unsure{même}',
      'Final source line including one written horizontal dash, the overworked last word and absence of terminal punctuation.')
audit(BOXES['P16'],['handwritten number','margin note','C/H different words'],r'\margin{17}',
      'Thin lower-left foliation alone; hand attribution is indeterminate.')

doubts = [
 dict(place='P03 closing parenthesis',reading=r'\unsure{)}',alternatives='Closing parenthesis, or an arc partly/wholly continuous with the main-line y descender.',confidence='medium',reason='The opening parenthesis is independent; the short possible closing stroke meets the y, and its lower extent cannot be separated.'),
 dict(place='P04 terminal punctuation',reading=r'\uline{transversalité}',alternatives='No separately established terminal stop; C supplies a full stop.',confidence='medium',reason='No isolated point after the terminal word was identifiable apart from its accent/word strokes; the draft does not invent an uncertain point.'),
 dict(place='P09 cancelled note',reading=r'\deleted{\unsure{appeler transversalité ?}}',alternatives='The preferred word candidates remain under-strike doubts; the terminal question-mark area also contains an extra dot-like residue.',confidence='low',reason='Crossing strokes obscure internal letters and the exact punctuation state; not every letter is plain.'),
 dict(place='P10 opening',reading=r'\unsure{On dira}',alternatives='Preferred compressed On dira; no supplied expansion.',confidence='low',reason='Initial rounded and tall linked strokes overlap and cannot all be separated, although the following que/X_i/est is clearer.'),
 dict(place='P10 cancelled modifier',reading=r'\deleted{\uline{\unsure{strictement}}}',alternatives='strictement preferred, still cancelled and underlined.',confidence='low',reason='Tall t strokes survive but the lower strike covers the compressed middle letters.'),
 dict(place='P10 cancelled following group',reading=r'\deleted{compatible \unsure{avec $T$|avec $\bar T$}}',alternatives='avec plain T preferred; C’s barred-T candidate retained.',confidence='low',reason='The crossed lower group is crowded; no independently identifiable second T cap settles the bar question.'),
 dict(place='P10 right-hand X in cancelled equality',reading=r'0.\unsure{\dot X_i|X_i}',alternatives=r'0.\dot X_i preferred; 0.X_i retained.',confidence='medium',reason='A separate dark point is present above the right X, but nearby transverse returns make its exact attachment less secure. There is no secure dot over the left X.'),
 dict(place='P10 dire; M0343',reading=r'\unsure{dire|désir}',alternatives='dire | désir',confidence='medium',reason='The initial d and following compressed letters favour dire, without eliminating the alternative.'),
 dict(place='P10 first transversalité; M0344',reading=r'\unsure{transversalité}',alternatives='Preferred first transversalité; interior remains unresolved.',confidence='low',reason='Long return strokes from above overlap its initial/central bodies.'),
 dict(place='P10 second transversalité; M0345',reading=r'\unsure{transversalité}',alternatives='Preferred second transversalité; no alternative word is supplied.',confidence='low',reason='Tall t-like uprights survive, but the flattened central sequence is not letterwise certain.'),
 dict(place='P10 leading dash',reading=r'-\quad 0.\dot X_i=X_i\cap Y',alternatives='Leading punctuation dash or minus-like stroke; its semantic role is not established.',confidence='medium',reason='The horizontal stroke is physically separate and genuinely marginal; neither witness records it.'),
 dict(place='P11 cancelled subscript',reading=r'\deleted{\unsure{_\varepsilon}}',alternatives='Epsilon-like subscript; retained as cancelled but not resolved.',confidence='low',reason='The small lower curl is crossed by the horizontal stroke and is not fully separable from it.'),
 dict(place='P12 relation; M0346',reading=r'\dot T\overset{-}{\unsure{\relbar\joinrel\relbar|\longrightarrow}}Y',alternatives='Long headless lower shaft preferred; lower arrow remains possible. Independent upper dash retained with unspecified role.',confidence='medium',reason='The lower shaft bends upward at the right but has no independent two-stroke arrowhead. The short upper dash cannot be discarded or assigned a role by mathematics.'),
 dict(place='P13 second initial e',reading='equisingulier',alternatives='Unaccented second spelling preferred; no independent acute is visible.',confidence='medium',reason='The dark initial body does not separate into an accent and letter as the first occurrence does.'),
 dict(place='P15 final word; M0347',reading=r'\unsure{même}',alternatives='même preferred; possible local overstrike/cancellation of initial strokes remains unassigned.',confidence='medium',reason='A circumflex and later m/e run are present, but the initial strokes are overworked. No secure full-word strike or terminal punctuation is visible.')
]

notes = [
 dict(id='N01',text='This undated handwritten leaf bears a heavy upper 4), a lower circled 4 with a separate point, and thin lower-left foliation 17. The body defines compatibility of a partie-bord with a family through a cylindrical neighbourhood, then strict compatibility of a conic neighbourhood using the complementary X* and its induced family. It begins definitions of equisingularity via locally trivial fibrations. These are source-content descriptions, not proof claims. The final sentence stops after the locally doubtful même and is not completed.'),
 dict(id='N02',text='Insertion and cancellation scope were read separately from word identity. B de X has one curved attachment and is followed by one live est; H’s extra struck est is not independently on the page. The au sens cylindrique insertion attaches after compatible, and its doubtful closing arc meets the main-line y. strict has two underlines; strictement has one underline plus a distinct attachment leader, fully captured in completing crop P17. The long elle ... et si insertion includes its final et si. The main line physically divides seule-/ment. The upper marginal note has no secure terminal stop; no quote marks were supplied.'),
 dict(id='N03',text=r'The inserted formula is preserved literally as X_i\cap T=\mathbf I.X_i\cap\dot T-, including its heavy serif interval symbol, multiplication point, lack of supplied grouping parentheses, and final dash. No operand, union term or missing sign is completed. Main T forms have one roof, not an added bar. This paragraph is a transcription/formula-scope observation, not a verification of the displayed condition.'),
 dict(id='N04',text=r'The lower definition literally says les Y_i sont coniques after introducing a family T_i\subset T. The forked Y has no T roof; H’s T_i is not adopted. The first équisingulier has an independent acute, whereas the second equisingulier has none identifiable. First relation: dotted T, a short upper dash, a longer lower unheaded/bent shaft, and Y; its role remains doubtful. The later dotted-T_i-to-Y relation has a definite two-sided arrowhead. The two relations are not silently made identical.'),
 dict(id='N05',text='The large transverse margin is not a container for overlapping upright body text. P10 was made from original [16,855,480,1585], rotated clockwise45 (expanded846×846), then scaled to2600×2600. Inverse mapping sends the large cross/return after the final marginal Y to approximately original x273–402,y1296–1309, centred at (325,1309): the main-line X_i already transcribed in P08. The lower long downward stroke maps from about (293,1431) to (406,1421): the main-line ment continuation. A rotated cross near the earlier cancelled equality maps to (338,1015), also upright-body X-star ink. These are excluded from the margin. In contrast, the short dash before its live zero-image equality maps to (51,1472) and is genuinely marginal. The final marginal formula has an overbar above its right side, not a source underline.'),
 dict(id='N06',text=r'Targeted conditional check of the marginal i.e.: interpret dot X_i as X_i\cap dot T, the zero action as the retraction to Y, and the final overbar as closure in X of X_i\setminus(X_i\cap Y). For a closed conic-compatible X_i, equality 0.dot X_i=X_i\cap Y implies the density formula: for each y in the intersection choose a boundary point b with 0.b=y; the positive points t.b approach y as t tends to zero and remain outside Y. Points already outside Y need no approximation. Closedness then gives X_i=cl_X(X_i\setminus Y). Conversely, density gives only density of the zero-image in X_i\cap Y under the conic-ray interpretation: a continuous zero retraction sends approximating positive rays to 0.dot X_i. Continuity does not make that image closed or surjective. This is a limited proof check of the two conditions, not a proof of all source definitions.'),
 dict(id='N07',text=r'The converse in the marginal i.e. is refuted by the following explicit example, proposed by root and independently checked here. Put A=(0,1], Y=[0,1], f:A\to Y the inclusion, and let X be the quotient of Y disjoint-union (A×[0,2]) identifying (a,0) with f(a). Let T be Y together with the images of A×[0,1], dot T=A×{1}, use the usual scalar action on heights in T, and take X_i=X (closed). Y and T are closed; T contains the open neighbourhood consisting of Y and heights<1. Its exterior X* is A×[1,2], so dot T has the explicit product collar there. Compatibility with X_i=X is automatic. If a stronger strictness formulation requires shrinking by a homeomorphism, the increasing piecewise-linear height map h_lambda(t)=lambda*t on [0,1] and h_lambda(t)=lambda+(2-lambda)*(t-1) on [1,2] fixes0,2 and sends1 to lambda; it descends to the quotient fixing Y and sends T to lambda T. The positive part X\setminus Y is dense: every neighbourhood of y in Y has an open Y portion meeting A; if a is in that intersection, openness in the cylinder gives points (a,t) with t>0 in the neighbourhood. Thus X_i=cl_X(X_i\setminus Y)=X. However 0.dot X_i=f(A)=(0,1] is a proper subset of X_i\cap Y=[0,1]. Therefore the displayed density condition does not in general imply the zero-image equality, even with the explicit strict ambient collar. No source formula has been corrected.'),
 dict(id='N08',text=r'The counterexample in N07 addresses the marginal i.e. between zero-image equality and density. The main inserted expression has the literal unfinished-looking ending X_i\cap T=I.X_i\cap dot T-. If that separate expression is completed/interpreted as the exact stronger hypothesis X_i\cap T=I·(X_i\cap dot T), then, under the usual conic-ray interpretation, intersecting with Y already imposes X_i\cap Y=0.dot X_i. N07 does not satisfy that extra equality, and is not claimed to refute a definition that includes it. The unclear terminal dash and the missing grouping are preserved rather than resolved by this diagnostic.')
]

check_events = [
 dict(statement_id='150_scan018.N05',type='used and rechecked in this run',outcome='Computed the inverse of the actual saved P10 rotation/scale and compared mapped loci with already-inspected upright text. Resolved source-scope overlap; this is an image-coordinate/source comparison, not a theorem proof.'),
 dict(statement_id='150_scan018.N06',type='targeted proof check',outcome='Checked the ray-limit implication for closed conic-compatible X_i and the limited continuous-retraction density conclusion. The stated conic interpretation and closedness hypotheses are explicit.'),
 dict(statement_id='150_scan018.N07',type='refuted, with refined id',outcome='The density⇒zero-image-equality converse of the marginal i.e. fails in the height-[0,2] mapping-cylinder example. Checked density, proper zero image, closed X_i, ambient collar and the descended piecewise-linear shrinking homeomorphism. Scope is refined by N08; no claim is made against an additional exact orbit-generation hypothesis.')
]

notation = [
 dict(form=r'T,\dot T,\mathring T',meaning='Conic neighbourhood, its dotted boundary, and the circled interior expression used in X*.',evidence='P05 two plain T roofs; P06/P08/P12/P14 filled boundary dots; P07 hollow circle. A single T cap is not an extra overbar.'),
 dict(form=r'\mathbf I',meaning='Heavy serif interval/action symbol in the inserted cone formula; its interval value is not newly written here.',evidence='P06 shows filled stem plus heavy top and bottom serifs.'),
 dict(form=r'X^*=X\setminus\mathring T; X_i^*=X^*\cap X_i',meaning='Complementary ambient piece and induced pieces.',evidence='P07 whole formulas, with all stars and subscripts retained.'),
 dict(form=r'0.\dot X_i; \overline{X_i\setminus X_i\cap Y}',meaning='Zero-action image and a marginal closure expression, under the conditional interpretation discussed in N06–N08.',evidence='P10 independent zero/multiplication point/boundary dot and overbar spanning the right side; source grouping not supplied.'),
 dict(form=r'\dot T\overset{-}{\unsure{\relbar\joinrel\relbar|\longrightarrow}}Y',meaning='Unresolved two-level relation glyph; not equated editorially with the later headed map.',evidence='P12 has separate upper short dash and long lower shaft; P14 provides a definite headed-arrow comparison.')
]

abbreviations = [
 dict(form='loc.',expansion='localement'),
 dict(form='i.e.',expansion='id est')
]

hand = [
 dict(habit='A heavily retraced or forked T body still has only one long cap; a separate upper bar must be independently present.',places='P05, P06, P11, P13, P14',consistency='All live T forms on this leaf have one cap. The crossed marginal T candidate remains locally doubtful rather than globally regularised.',witness_errors='C adds bars over the live neighbourhood and family Ts; H correctly has plain T there.'),
 dict(habit='Shallow, nearly horizontal accents are still independent accent strokes.',places='P05 cônique; P11 cônique; contrast P12 first équisingulier and P13 second equisingulier',consistency='The two conic-neighbourhood accents are present; the later plural coniques is unaccented. The second equisingulier has no independent acute.',witness_errors='Both witnesses flatten the two cônique spellings to conique and supply the second equisingulier acute.'),
 dict(habit='Bent attachment leaders can run near letters or underlines without cancelling or emphasising the adjacent main word.',places='P02 B de X; P03 parenthetical; P05 strict; P06/P17 strictement and the longer insertion',consistency='Each attachment was traced separately. The parenthetical closing arc remains doubtful where it meets y.',witness_errors='H duplicates est under a supposed strike, moves/misreads the parenthetical, and extends emphasis to compatible.'),
 dict(habit='A Y is an open fork without a roof; the same fork under a horizontal cap belongs to a T form.',places='P13 T_i⊂T; P14 Y_i and dotted T_i',consistency='The contrast is visible on adjacent lines, without using grammatical expectation.',witness_errors='H changes literal Y_i to T_i in les Y_i sont coniques.'),
 dict(habit='A relation may be a long unheaded shaft with a separate upper dash; not every horizontal relation has a completed arrowhead.',places='P12 versus P14',consistency='First relation retains two visible levels and uncertainty; later relation has a clear two-sided tip.',witness_errors='C omits the upper dash; H reduces the first relation to a conventional arrow.'),
 dict(habit='Slanted margin formulas can touch upright body letters which become large crosses or descending strokes after rotation.',places='P10 overlap with P07/P08 body text',consistency='Inverse-coordinate mapping confirms three such intrusions and separates the truly marginal leading dash.',witness_errors='H’s marginal fragments misassign a star/dot and treat the final overbar as an underline; no overlapping main-text ink is duplicated in the draft.')
]

dispositions = {
 1:'Archive scan marker/editorial H header are metadata, not a source-word disagreement. Author number covered by P01_a.',
 2:'P01_a preserves the written closing curve in 4); H’s explanatory prose is editorial.',
 3:'P02_a: partie-bord with a written hyphen, not partie bordante.',
 4:'P02_b: one live est; insertion leader does not supply an extra cancelled verb.',
 5:'P03_a: actual insertion au sens cylindrique attaches after compatible, not H’s ou semi-cylindrique after the earlier cylindrique.',
 6:'P03_a: actual words and attachment retained; closing arc locally unsure.',
 7:'P03_b: chacun, no final e.',
 8:'P04_a: complete upper marginal wording, underline and absence of source quotation marks; H note is editorial.',
 9:'P05_a and M0342 resolve to colon; independent accent in cônique separately covered by P05_b.',
 10:'P06_b: original si plus inserted elle est, not s’il.',
 11:'H’s backslash-comma is TeX spacing, not a written comma; no macro-only change row. Bold serif I and multiplication point covered by P06_c.',
 12:'P06_d: a written terminal dash, not H ellipsis. Entire formula is audited.',
 13:'P06_f: first bord, not bordant.',
 14:'H overset-circle versus C mathring is the same hollow-circle source mark; macro-only, no change row. P07 whole formula audited.',
 15:'P07_a: Donc cela, with no supplied ce cas or underline.',
 16:'P08_a: second bord, not bordant. Physical seule-/ment is separately preserved by P08_b.',
 17:'P09_a preserves the cancelled small note with its under-strike doubt; P10_a preserves the larger note’s compressed opening with local doubt.',
 18:'P10_b–P10_c: X_i est and cancelled underlined strictement; no marginal superscript star.',
 19:'P10_e–P10_f: crossed compatible/avec-T group and complete first si equality, with local dot and letter doubts.',
 20:'P10_h: transversalité candidate retained rather than H transversaux; no unsourced additional transversaux inserted.',
 21:'P10_g–P10_j: dire|désir, both separate transversalité candidates, colon punctuation, and cancelled stricte retained with their local states.',
 22:'Display wrappers are macro layout, not manuscript brackets; no change row. P10_k preserves a genuinely written leading dash and the whole formula.',
 23:'H’s long note is editorial. Actual closure formula covered by P10_l; lower heading is read independently in P11. No editorial prose is transcribed.',
 24:'Circled 4 and its separate point are preserved; H explains its circle editorially. Source circle representation is macro-only; audit B21 covers the ink.',
 25:'P11_c: cancelled epsilon-like subscript retained with doubt; P11_b separately removes a nonexistent live T overbar.',
 26:'P12_a and M0346: separate upper dash retained over the doubtful lower unheaded shaft; no forced conventional arrow.',
 27:'P14_a: literal Y_i, not T_i.',
 28:'One written horizontal dash; C three-hyphen versus H two-hyphen TeX conventions are typography-only, not a stroke-count difference. No change row.',
 29:'P15_a and M0347 retain a locally doubtful même rather than H illegible; P16_a records thin17 with H [not transcribed]. H’s end-of-leaf prose is editorial.'
}

deletion_insertion_review = [
 dict(text=r'\inserted{$B$ de $X$}',scope_attachment='After partie-bord, before the one live est.',evidence='P02 raised text and curved leader; no separate struck est.'),
 dict(text=r'\inserted{(au sens cylindrique\unsure{)}}',scope_attachment='After compatible, before avec chacun; opening parenthesis certain, closing arc local doubt.',evidence='P03 bent lower attachment and overlap of possible closing arc with main-line y.'),
 dict(text=r'\inserted{\uuline{strict}}',scope_attachment='Before first live T in the central paragraph.',evidence='P05 two underline strokes independent of its bent attachment leader.'),
 dict(text=r'\inserted{\uline{strictement}}',scope_attachment='Before main compatible, not an underline of compatible.',evidence='P06 and one completing P17: full word, one underline, distinct long leader.'),
 dict(text=r'\inserted{elle est compatible avec chaque $X_i$ $(X_i\cap T=\mathbf I.X_i\cap\dot T-)$, et si}',scope_attachment='After original si and before original dotted-T est; et si belongs to the insertion.',evidence='P06 two raised text rows, complete formula punctuation and return to the baseline dotted T.'),
 dict(text=r'\deleted{\unsure{appeler transversalité ?}}',scope_attachment='Entire small transverse note cancelled; not the large note’s opening.',evidence='P09 broad crossing strokes; words and extra dot-like terminal residue remain locally uncertain.'),
 dict(text=r'\deleted{\uline{\unsure{strictement}}}',scope_attachment='Cancelled underlined word in the large margin before live underlined transversal.',evidence='P10 lower underline distinct from crossing stroke; internal letters obscured.'),
 dict(text=r'\deleted{compatible \unsure{avec $T$|avec $\bar T$}}',scope_attachment='Whole following phrase crossed; the live transversal stays outside the deletion.',evidence='P10 strike through word bodies; final crowded group remains unresolved.'),
 dict(text=r'\deleted{si $X_i\cap Y=0.\unsure{\dot X_i|X_i}$}',scope_attachment='si and the entire first marginal equality cancelled; next live equality is separate.',evidence='P10 continuous strike crossing both sides, with separate candidate point above right X.'),
 dict(text=r'\deleted{stricte}',scope_attachment='Only stricte cancelled between the two live doubtful transversalité occurrences.',evidence='P10 short strike traverses that word; no forced cancellation of the following long word.'),
 dict(text=r'\deleted{Soit}',scope_attachment='Between circled4 plus point and live Un.',evidence='P11 horizontal cancellation through the readable four-letter word.'),
 dict(text=r'\deleted{\unsure{_\varepsilon}}',scope_attachment='Small lower group immediately after the lower T; T itself remains live.',evidence='P11 epsilon-like curl under the horizontal strike; no second upper T bar.'),
 dict(text=r'\unsure{même}',scope_attachment='Final live-preferred word; possible local crossing of its initial letters is not promoted to whole-word deletion.',evidence='P15 heavy initial retracing, independent circumflex and later m/e run; no secure strike across the entire word.'),
 dict(text='P10 source-scope exclusions',scope_attachment='Upright main-text X_i, X-star and ment overlaps are transcribed once in the main body, not added to the margin.',evidence='Recorded rotation inverse places them at the main-text loci; N05 contains coordinates.')
]

logical_lines = [line for line in draft.splitlines() if line.strip() and not line.lstrip().startswith('%')]
report = dict(page=PAGE,reader='reader_a',line_count=len(logical_lines),
              line_count_basis='Nonempty logical draft rows, excluding TeX comment-only rows; not a claim about physical manuscript line count.',
              inspection=dict(original_size=[1682,2359],whole_original_views=1,native_half_views=[1,1],
                              half2_y_offset=1062,saved_crops=17,inspected_crops=list(BOXES),
                              completion_crop='P17 only, for upper portions of strictement clipped by P06; all announced earlier frames unchanged.',
                              image_scope='Assigned page150_scan018 only; all agreed words, numbers, insertions, cancellations and marginal ink read. No OCR, recognition, research or TeX compilation.',
                              delivery_note='An earlier P04 delivery was truncated before the image was received; only the successful visual inspection is counted.'),
              changes=changes,decisions=decisions,inventory=inventory,audit_boxes=audit_boxes,doubts=doubts,
              notes=notes,check_events=check_events,notation=notation,abbreviations=abbreviations,hand=hand,
              diff_coverage=[dict(row=i,disposition=dispositions[i]) for i in range(1,30)],
              deletion_insertion_review=deletion_insertion_review)
(OUT / 'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:len(report[k]) for k in ['changes','decisions','inventory','audit_boxes','doubts','notes','check_events','diff_coverage']},ensure_ascii=False))
print('line_count',report['line_count'])
