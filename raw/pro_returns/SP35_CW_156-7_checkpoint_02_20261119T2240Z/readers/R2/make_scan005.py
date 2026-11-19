from pathlib import Path
from datetime import datetime, timezone
import json

out = Path(__file__).parent
manifest = json.loads((out / 'scan005_crops.json').read_text())
byname = {Path(x['file']).stem.removeprefix('scan005_'): x for x in manifest}
D = []

def row(n, place, C, H, reading, dc, dh, kind, evidence, crop=None,
        confidence='high', marked=False, cd='not applicable', math=None):
    item = byname.get(crop)
    D.append(dict(id=f'R2-005-{n:02d}', place=place, C=C, H=H, reading=reading,
        diff_C=dc, diff_H=dh, kind=kind, marked_in_H=marked,
        confidence=confidence, evidence=evidence,
        crop=item['file'] if item else None,
        crop_coordinates=item['box'] if item else None,
        C_doubt_status=cd, math_consequence=math))

row(1, 'manuscript number', r'\deleted{\unsure{3}}4', 'overwritten digit described in an editorial note',
    r'\deleted{\unsure{3}}4', False, True, 'omission',
    'Current 4 is dark and secure; two rounded older lobes survive beneath it, consistent with 3 but not independently clean.',
    'page_no', 'low', True, 'retained')
row(2, 'first circled label', r'\unsure{e}', '(e), with circle described in note',
    r'circled \unsure{e}', False, True, 'drawing or diagram',
    'The small enclosure is circular. The internal loop is crossed by the stroke of the circle; e remains tentative.',
    'e', 'low', False, 'retained')
row(3, 'M alphabet, first and subsequent instances', r'\unsure{M|\mathcal M}', r'\mathcal M',
    r'\unsure{M|\mathcal M}', False, True, 'misread symbol or index',
    'Two high pointed stems and a curved entry stroke give an ordinary handwritten M; script versus plain cannot be securely distinguished. The ambiguity is marked at its first occurrence.',
    'top_alphabets', 'medium', False, 'retained')
row(4, 'quotation marks before figures', r'\unsure{``}', '«', r'\unsure{``}',
    False, True, 'other',
    'The area above and before the f is occupied by the overwritten page number and a small separate dot. No secure angled guillemet or complete opening pair is visible. Closing paired strokes after élémentaires are secure.',
    'opening_quote', 'low', False, 'retained')
row(5, 'figure-set alphabet throughout', r'\unsure{\mathscr F|\mathcal F}', r'\mathfrak F',
    r'\unsure{\mathscr F|\mathcal F}', False, True, 'misread symbol or index',
    'The F has a swept upper arm with a loop/turn at its junction and a separate middle cross-stroke. There are no broken Gothic strokes. Script versus calligraphic remains open.',
    'top_alphabets', 'medium', False, 'retained')
row(6, 'subset expression in item e', r'figures $\subset\mathscr F$ élémentaires',
    r'figures élémentaires ou multistrates $\subset\mathfrak F$',
    r'figures $\subset\mathscr F$ élémentaires', False, True, 'insertion or placement',
    'The small subset curve and F stand directly to the right of figures on the first line; élémentaires and multistrates are on the following lines.',
    'top_alphabets')
row(7, 'top-left definition', 'déployement', 'déploiement', 'déployement', False, True,
    'abbreviation expanded or spelling modernised',
    'A long descending y follows the deploy sequence; no separate short i replaces it. The spelling déployement is literal.')
row(8, 'top-left underlining', 'strates; déployement; strates; incident underlined',
    'only déploiement and incident emphasized', 'strates; déployement; strates; incident underlined',
    False, True, 'other', 'Separate horizontal rules run under both occurrences of strates and under déployement; incident also has its own rule.')
row(9, 'top-left and item-f connection strokes', 'TikZ bracket and long connector',
    'drawings only described in editorial notes', 'TikZ bracket and long connector, preserved in TeX',
    False, True, 'drawing or diagram',
    'The left annotation has a bent ruled enclosure with upper and lower connections. A separate long bent connector joins the revised lieux entry to the right-hand definition.')
row(10, 'upper right after par', r'\deleted{\unsure{\mathscr F}}', 'omitted',
    r'\deleted{\unsure{\mathscr F}}', False, True, 'omission',
    'Below par, a small crossed letter retains a vertical stem, upper arm and middle loop. F is plausible but is obscured by the strike.',
    'right_deleted', 'low', False, 'retained')
row(11, 'second circled label', r'\unsure{f}', '(f), circle described', r'circled \unsure{f}',
    False, True, 'drawing or diagram',
    'The inner ascender and cross-stroke overlap the left outline of the enclosure; f remains possible rather than certain.',
    'f_lieux', 'low', False, 'retained')
row(12, 'L alphabet', r'\unsure{L|\mathcal L}', r'\mathcal L', r'\unsure{L|\mathcal L}',
    False, True, 'misread symbol or index',
    'A looped entry at the bottom of a long rising stem ends in a long rightward foot. This does not uniquely fix the mathematical alphabet.',
    'f_lieux', 'medium', False, 'retained')
row(13, 'erased word beneath lieux', r'\deleted{\unsure{éléments}}',
    'word is mentioned only as underlined and struck in note', r'\deleted{\unsure{éléments}}',
    False, True, 'omission',
    'The line of cancellation leaves an ascender and separated lower traces. Éléments is plausible, but its individual letters are largely covered.',
    'f_lieux', 'low', True, 'retained')
row(14, 'inserted lieux and underline', r'\inserted{``lieux\'\'}', '« emphasized lieux »',
    'inserted double-quoted, underlined lieux', True, True, 'insertion or placement',
    'Lieux is above the cancelled baseline word. A separate short horizontal rule below the crossing is aligned with the width of lieux; I attach the emphasis to the live inserted word. Its scope is medium confidence. The quotation strokes are paired raised marks, not guillemets.',
    'f_lieux', 'medium')
row(15, 'erased second word under item f', r'\deleted{\unsure{minimaux}}', 'omitted',
    r'\deleted{\unsure{minimaux}}', False, True, 'omission',
    'The second heavy crossing retains initial m-like humps, a dotted short stem and low terminal strokes. Minimaux remains the best tentative reading.',
    'f_lieux', 'low', True, 'retained')
row(16, 'definition of lieux', 'connected insertion, éléments minimaux de ... pour ≪',
    'ordinary prose after a colon', 'connected insertion, éléments minimaux de ... pour ≪',
    False, True, 'insertion or placement',
    'The definition is set in the right column and joined by a drawn line; there is no literal colon before éléments minimaux. The deleted earlier words remain separately present.')
row(17, 'punctuation in top table and margin', 'no terminal punctuation after several displayed lines',
    'semicolon after right definition and first stratum criterion; periods after lieux definition and tilde-F display',
    'no such supplied semicolons or periods', False, True, 'text not on the page',
    'The visible line endings at F, script F and ≪ stop without the semicolon or period introduced by H. Line separation supplies the organization.')
row(18, 'sine qua non quotation marks', 'paired high marks', 'guillemets', 'paired high marks',
    False, True, 'other', 'Both sides of sine qua non use two short raised strokes rather than angular brackets.')
row(19, 'axiom introduction', 'inserted At 1 - At 3; baseline ne concernent que',
    'inserted concernent; (At 1 – At 3); struck illegible group',
    'inserted At 1 - At 3; baseline ne concernent que', False, True, 'insertion or placement',
    'At 1 - At 3 is written in the upper interline. Ne concernent que is a continuous live baseline sequence. No parentheses surround the interlinear axiom range.')
row(20, 'first cancelled group before les relations', r'\deleted{\unsure{At 1}}',
    'At 4 described as crossed in note', r'\deleted{\unsure{At 1|At 4}}',
    True, True, 'misread symbol or index',
    'The left group contains A/t-like strokes and a final tall digit under multiple diagonals. The final straight stem favours 1, but the low crossing allows 4, so I expand the alternatives.',
    'intro_deleted', 'low', False, 'changed')
row(21, 'second cancelled group before les relations', r'\deleted{\unsure{et|4}}',
    'omitted', r'\deleted{\unsure{4|et}}', True, True, 'omission',
    'The lower surviving form has an oblique left arm meeting a right stem and a transverse bar, making 4 the first reading. The upper crossed traces still allow a word-like et.',
    'intro_deleted', 'low', False, 'changed')
row(22, 'At 1 margin opening', 'Axiomes', 'Axiome', 'Axiomes', False, True, 'misread word',
    'The rotated first heading ends in a short extra descending hook after the e, absent from the neighbouring singular Axiome des strates.',
    'At1_margin', 'medium')
row(23, 'At 1 margin underline', 'sommes majorées de figures underlined', 'no emphasis marked',
    'sommes majorées de figures underlined', False, True, 'other',
    'One rule follows sommes majorées de and a second rule follows figures on the line below.', 'At1_margin')
row(24, 'At 2 margin prose', 'équivaut à : Si; d’inclusion de figures',
    'équivalent à : si; d’inclusion des figures; Critère included in emphasis',
    'équivaut à : Si; Critère followed by underlined d’inclusion de figures par strates',
    False, True, 'misread word',
    'The rotated note ends équivaut with a tall t, begins Si with a capital rising S, and has de without a terminal s. The rule begins under d’inclusion rather than under Critère.',
    'At2_margin')
row(25, 'At 2 margin initial pair', r'F,\unsure{C|G}', 'F,G', r'F,\unsure{C|G}',
    False, True, 'misread symbol or index',
    'The second initial capital is a faint open curve with a short lower horizontal touch, less developed than the unmistakable G in the following inequality. C remains first but G is not excluded.',
    'At2_margin', 'medium', False, 'retained',
    'The margin begins with a C/G doubt but the displayed criterion then uses G; the mismatch is not repaired.')
row(26, 'At 2 before est', r'\deleted{\unsure{d}}', 'omitted', r'\deleted{\unsure{d}}',
    False, True, 'omission',
    'An extra upright loop crosses the opening e of est. A cancelled d fits the loop, but the overlap prevents certainty.',
    'At2', 'low', False, 'retained')
row(27, 'Scholie axiom references', 'At in At 1 and At 2 underlined', 'not emphasized',
    'At in At 1 and At 2 underlined', False, True, 'other',
    'Short horizontal rules sit beneath each At, stopping before the numeral.')
row(28, 'Scholie correspondence mark', 'bilaterally ticked stroke | mapsto', r'\mapsto',
    'horizontal stroke with a vertical tick at each end, drawn in TikZ', True, True, 'misread symbol or index',
    'The right endpoint is one short transverse downstroke, not an arrowhead. Both ends have the same perpendicular-tick form.',
    'map_F', 'high', False, 'resolved', 'The ink is reproduced without replacing it by an expected function arrow.')
row(29, 'Scholie letter in F(M)', r'\unsure{\mathscr F|\mathscr P}', r'\mathfrak F',
    r'\mathscr F', True, True, 'misread symbol or index',
    'The middle crossbar below the looped upper arm is independent and clear. It is an F, not P. Script F is retained even though a powerset notation might be expected.',
    'F_of_M', 'high', False, 'resolved', 'No substitution of P(M) is made.')
row(30, 'abbreviation punctuation in Scholie and primed clauses', 'ens; un ens; l’ens',
    'ens.; un ens.; l’ens.', 'ens; un ens; l’ens', False, True, 'other',
    'There is no independent point after these three short ens groups. By contrast ens. in the upper definitions visibly includes its point.')
row(31, 'Scholie order parenthesis', 'pour ≤', 'par ≤', 'pour ≤', False, True, 'misread word',
    'The word has two low rounded middle turns between p and r, giving pour; it is not the shorter par.')
row(32, 'first Phi in clause a', r'\unsure{\Phi|\varphi}', r'\Phi', r'\unsure{\Phi|\varphi}',
    False, True, 'misread symbol or index',
    'A central vertical crosses an oval, with a descending lower stem. The upper extension merges with the oval, leaving capital Phi versus cursive varphi open. Later instances have a turned foot.',
    'Phi_a', 'medium', False, 'retained')
row(33, 'clause a final adjective', 'fermés', r'\uncertain{fermées}', 'fermés',
    False, True, 'misread word',
    'The ending has one accented e followed directly by the s turn, without an additional e.', None, 'high', True)
row(34, 'clause b opening', 'Si', 'si', 'Si', False, True, 'other',
    'The initial S rises to capital height before the separate i.')
row(35, 'short cancellation below c', r'\deleted{\unsure{(et}}',
    'unread word between parentheses described in note', r'\deleted{\unsure{(et}}',
    False, True, 'omission',
    'The left parenthesis is distinct. The following crossed group has a central rising stem compatible with t, while e is mostly obscured. I retain the cancellation grouping; the strike itself begins to the right of the parenthesis.',
    'c_deleted', 'low', True, 'retained')
row(36, 'union index in c', r'\Phi\unsure{\in|+}\widetilde{\mathscr F}',
    r'\Phi\in\widetilde{\mathfrak F}', r'\Phi\unsure{\in|+}\widetilde{\mathscr F}',
    False, True, 'misread symbol or index',
    'The compressed mark after Phi has intersecting horizontal and near-vertical strokes. The curved part expected for membership is not separable enough to exclude a plus.',
    'c_index', 'low', False, 'retained', 'An expected membership index does not settle the compressed sign.')
row(37, 'sloping margin beside c', r'\widetilde F≠∅ automatique si M≠∅ et dans tous les cas, \unsure{équivaut} à ∅∈\widetilde F',
    r'\widetilde F≠∅ [ill.] [ill.] et donc ∅∈\widetilde F',
    r'\widetilde F≠∅ automatique si M≠∅ et dans tous les cas, équivaut à ∅∈\widetilde F',
    True, True, r'readable ink left as \ill{}',
    'Rotation exposes the complete note. Automatique has a tall t and descending q; the next line reads et dans tous les cas. The last word has the long q descender and terminal t of équivaut. Donc is not present.',
    'c_margin', 'medium', True, 'resolved',
    'The note asserts equivalence, not only the implication H gives with donc.')
row(38, 'transition after c', r'\unsure{un|une}', 'un', 'un', True, False, 'misread word',
    'The article has only two connected low humps before the blank separating ens; no final extra e loop appears.',
    'un_ens', 'medium', False, 'resolved')
row(39, 'b′ quantifier, superscript and membership variable', r'x; ^x; x\in\Phi',
    r'X; ^X; X\in\Phi', r'x; ^x; x\in\Phi', False, True, 'misread symbol or index',
    'All three x marks are short lowercase crosses. The named principal element at the end is a visibly larger uppercase X with a tilde.',
    'bprime')
row(40, 'b′ first character within braces', r'\deleted{\unsure{F}}\Phi', 'Phi only',
    r'\deleted{\unsure{F}}\Phi', False, True, 'omission',
    'A crossed vertical and horizontal arm remain beneath and just before the live looped Phi. F is plausible but fused with the replacement.',
    'bprime', 'low', False, 'retained')
row(41, 'b′ family after membership', r'\unsure{\overline{\mathscr F}|\widetilde{\mathscr F}}',
    r'\widetilde{\mathfrak F}', r'\overline{\mathscr F}', True, True, 'misread symbol or index',
    'The mark is a single straight rising bar. The adjacent superscripted family at the left has an unmistakable curved wave, making the difference visible within the same crop.',
    'bprime', 'high', False, 'resolved', 'The bar is retained even if the family was meant to be the earlier tilde family.')
row(42, 'b′ after élément', r'\deleted{\unsure{F}}', 'omitted', r'\deleted{F}',
    True, True, 'omission',
    'The vertical stem and two rightward arms of F are clear beneath separate diagonal cancellation strokes.',
    'element_F', 'high', False, 'resolved')
row(43, 'second primed label', r'\unsure{a|c}′', 'd′', 'a′', True, True,
    'misread symbol or index',
    'The letter has a closed low bowl plus a short right-hand stem, with no tall d ascender. The bowl is closed, ruling against c.',
    'aprime', 'high', False, 'resolved')
row(44, 'crossed group before Dans', r'\deleted{\unsure{\forall|F}}',
    'crossed ∀ only described in note', r'\deleted{\unsure{\forall|F}}',
    False, True, 'omission',
    'Several diagonals overlap a vertical and a short side arm. An inverted A-like form is possible, but F also fits surviving arms.',
    'aprime', 'low', False, 'retained')
row(45, 'a′ before famille', r'\unsure{toute|toutes}', 'toute', 'toute',
    True, False, 'misread word',
    'After the second tall t, one terminal loop turns down and stops. No separate s follows that e-shaped loop.',
    'toute', 'medium', False, 'resolved')
row(46, 'left of primed conditions', 'upward curved arrow', 'brace described in note',
    'upward curved arrow reproduced in tikz-cd', False, True, 'drawing or diagram',
    'The line curves from the lower primed condition upward, ending in a pointed arrowhead beside b′. It does not have the opposed hooks and central point of a brace.')
row(47, 'Relation heading', 'Relation without underline', 'Relation emphasized',
    'Relation without underline', False, True, 'other',
    'The blank space immediately beneath the word contains no underline; this differs from Scholie above.')
row(48, 'definition label above equivalence', r'\unsure{défn|defn}', 'déf', 'defn',
    True, True, 'abbreviation expanded or spelling modernised',
    'The small label includes a final low n-like shoulder following the tall f. No distinct accent is present over the e. The n is part of the same small annotation, not a separately raised exponent.',
    'defn', 'medium', False, 'resolved')
row(49, 'join in compatibility definition', 'F∨C', 'F∨G', 'F∨C', False, True,
    'misread symbol or index',
    'The second letter is an open rounded C without the short internal return of nearby G in the braced pair {F,G}.',
    None, 'medium', False, 'not applicable',
    'The literal join operand disagrees with the G in both the relation and the braced pair. It is preserved.')
row(50, 'punctuation around definition and final brace',
    'existe i.e.; figures compatibles without following period; réflexive symétrique without comma',
    'existe, i.e.; figures compatibles.; réflexive, symétrique',
    'existe i.e.; figures compatibles without following period; réflexive symétrique without comma',
    False, True, 'text not on the page',
    'No independent punctuation mark appears at these three positions; the thin strokes below figures compatibles are underlines.')
row(51, 'cancelled word before se reconstitue', r'\deleted{\unsure{est}}', r'\struck{\ill{}}',
    r'\deleted{\unsure{est}}', False, True, r'readable ink left as \ill{}',
    'Below the diagonal crossings is a short e/s-like run ending at a vertical and cross-stroke. Est is plausible but remains doubtful.',
    'est', 'low', True, 'retained')
row(52, 'interlinear axiom qualification', 'avec At 1, At 2, At 3',
    'avec (At 1, At 2, At 3)', 'inserted avec At 1, At 2, At 3, attached after the order pair',
    False, True, 'insertion or placement',
    'The interlinear phrase begins avec and lists the three At references separated by commas; there are no enclosing parentheses. It is attached to (script F,≤) before se reconstitue.')
row(53, 'first glyph in final brace', r'\unsure{X|\forall}', 'X', 'X', True, False,
    'misread symbol or index',
    'Two oblique strokes cross at their middle. There is no horizontal bar joining the upper arms as required by an inverted A.',
    'bottom_X', 'high', False, 'resolved')
row(54, 'first line of final brace', 'X [compatibility] réflexive symétrique',
    'X [compatibility] X, réflexive symétrique', 'X [compatibility] réflexive symétrique',
    False, True, 'text not on the page',
    'After the crossed-angle sign, the line proceeds directly to the r of réflexive. No second X occupies the gap.',
    'bottom_X', 'high', False, 'not applicable',
    'The elliptical or malformed line is copied; the mathematically expected second X is not supplied.')

# All thirty individual C doubt occurrences, in source order.
A = [
 ('3','overwritten manuscript number','retained',1),
 ('e','first circled label','retained',2),
 ('M|mathcal M','first definition','retained',3),
 ('opening double quote','before figures','retained',4),
 ('mathscr F|mathcal F','first figure-set glyph','retained',5),
 ('deleted mathscr F','upper right after par','retained',10),
 ('f','second circled label','retained',11),
 ('L|mathcal L','second definition','retained',12),
 ('deleted éléments','under lieux','retained',13),
 ('deleted minimaux','below lieux','retained',15),
 ('deleted At 1','introduction','changed: At 1|At 4',20),
 ('deleted et|4','introduction','changed primary: 4|et',21),
 ('C|G','At 2 margin','retained',25),
 ('deleted d','before est in At 2','retained',26),
 ('bilaterally ticked mark|mapsto','Scholie','resolved: bilaterally ticked mark',28),
 ('mathscr F|mathscr P','Scholie F(M)','resolved: mathscr F',29),
 ('Phi|varphi','clause a','retained',32),
 ('deleted (et','clause c','retained',35),
 ('in|+','clause c union index','retained',36),
 ('équivaut','clause c margin','resolved: équivaut',37),
 ('un|une','transition after c','resolved: un',38),
 ('deleted F','b′ first object in braces','retained',40),
 ('bar-F|tilde-F','b′ family inside braces','resolved: overbar',41),
 ('deleted F','after élément','resolved: F',42),
 ('a|c','second primed label','resolved: a',43),
 ('deleted forall|F','before Dans','retained',44),
 ('toute|toutes','before famille','resolved: toute',45),
 ('défn|defn','definition label','resolved: defn',48),
 ('deleted est','before se reconstitue','retained',51),
 ('X|forall','final brace first glyph','resolved: X',53),
]
index = {int(x['id'].rsplit('-',1)[1]): x for x in D}
audit = [dict(C_reading=a, place=b, status=c, evidence=index[d]['evidence'],
              crop=index[d]['crop'], crop_coordinates=index[d]['crop_coordinates'],
              difference_id=index[d]['id']) for a,b,c,d in A]

end = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
data = dict(
 reader='R2', scan=5, start_utc='2026-11-19 21:30:37 UTC', end_utc=end,
 model='GPT-6 Astra Pro; inherited effort setting not exposed; R2',
 images_viewed=['H156-01_156-7_scan005.jpg','H156-01_156-7_scan005_a.jpg','H156-01_156-7_scan005_b.jpg']+[x['file'] for x in manifest],
 display_note='The initial batch of eleven crop displays was unavailable to the model because the tool output was truncated. The existing crop files were then displayed in small batches. No crop was regenerated or taken a second time.',
 coverage=[
  'overwritten manuscript number 4; first circled entry and all top definition words, quotes, underlines, subset placement and mathematical alphabets',
  'complete upper-left strates / déployement / incidence note, its formulas and enclosing bent line',
  'upper-right irreducibility definition, induced ≤M and ≪M, and small cancelled F',
  'second circled entry, L subset M, two deleted words, inserted lieux, underline and long connector to revised definition',
  'Axiomes heading and sine qua non introduction, interlinear At1–At3 and two crossed starts before les relations',
  'At1 and its full slanted margin, Sup subscript I and arbitrary-I qualification',
  'At2 and its small deletion, full Sup formula, tilde-F set, complete rotated inclusion criterion',
  'Scholie with underlined At references, bilateral correspondence mark, script F(M), pour≤ and all clause a/b/c words and symbols',
  'cancelled nonemptiness formula, short cancellation, tiny union index, final nonemptiness condition and full slanted marginal gloss',
  'transition and both primed conditions: lower-case x, superscript x, overwritten F/Phi, straight bar, second erased F, a′ label, cancelled forall/F, uppercase tilde X, upward curved arrow',
  'Relation heading, crossed-angle compatibility glyph, complete equivalence label and literal F∨C, braced pair and underlined figures compatibles',
  'final reconstruction paragraph, t.f., cancelled est, inserted axiom list and all variables and primes in the two-line final brace'],
 notation=[
  dict(form='figure set', reading='mathscr F|mathcal F; Gothic excluded', evidence='swept upper arm and middle cross-stroke'),
  dict(form='M and L', reading='M|mathcal M; L|mathcal L', evidence='cursive entry strokes leave alphabet unresolved; first occurrence marked'),
  dict(form='correspondence', reading='horizontal stroke ticked at both ends', evidence='no pointed arrowhead'),
  dict(form='Scholie ambient family', reading='mathscr F(M)', evidence='clear middle F bar; not P'),
  dict(form='family in b′ braces', reading='overline mathscr F', evidence='straight diagonal overbar contrasting with neighbouring wave'),
  dict(form='b′ variable', reading='lowercase x in quantifier, exponent and membership; uppercase tilde X in naming', evidence='relative heights visible'),
  dict(form='compatibility', reading='six-ended crossed-angle sign', evidence='custom TikZ copied at every occurrence'),
  dict(form='definition abbreviation', reading='defn', evidence='no accent and a low terminal n, not a separately raised exponent'),
  dict(form='quotes and abbreviations', reading='paired raised marks; déployement; ens. in top definitions, ens/l’ens without point lower down; At; t.f.; i.e.', evidence='literal visible forms retained')],
 math_notes=[
  dict(type='summary, not proof check', text='Defines multistrates as strictly irreducible objects of the inclusion poset, strata of a figure, its stratum set, and lieux via minimality for the second relation. At1 gives nonemptiness and bounded suprema, and At2 expresses a figure as the supremum of its strata.'),
  dict(type='targeted proof check', statement_id='R2-005-M1', text='The displayed At2 margin criterion with F and G follows from At2: if F≤G, every X≤F is also a stratum of G, so choose Y=X. Conversely, if every stratum X of F lies below a stratum Y of G, each X≤G; taking the supremum of all such X gives F≤G. This validates the displayed F/G criterion conditionally on At2; it does not decide the initial C|G glyph.'),
  dict(type='targeted proof check', statement_id='R2-005-M2', text='Under clause b, a nonempty family contains the empty set: take one member Phi and use the empty closed subset of Phi. The converse is immediate. Under the union=M clause, M nonempty forces the family nonempty. These are the two implications stated in the c margin. The proof is about the clauses as read, not evidence for their individual glyphs.'),
  dict(type='reading anomalies retained', text='The literal script F(M), the overbar inside b′, the C in F∨C, and the missing second X in the first compatibility line are preserved. Each was compared with nearby forms rather than repaired to an expected notation.'),
  dict(type='unproved author assertion', text='The complete Scholie equivalence and the reconstruction of a finite-type figure poset from its multistrata, order and compatibility relation were read but not independently proved; At3 is not on this page.')],
 author_qualifications=['strictement irréductibles','Sup majorés (I quelconque)','Dans le cas où les figures sont de t.f.','avec At 1, At 2, At 3'],
 author_explicit_verification_requests=[],
 unresolved=[dict(place=x['place'], reading=x['reading'], confidence=x['confidence']) for x in D if x['C_doubt_status'] in ('retained','changed')]+[
  dict(place='inserted lieux underline scope', reading='underline attached to live lieux; could be inherited from the erased predecessor', confidence='medium')],
 differences=D, C_doubt_audit=audit, new_omissions_from_both=[],
 crop_manifest='readers/R2/scan005_crops.json',
 check_events=[
  dict(statement_id='R2-005-M1', date=end, who='GPT-6 Astra Pro; inherited effort setting not exposed; R2', type='targeted proof check', outcome='Displayed F/G inclusion criterion proved from At2, in both directions; unresolved C|G opening retained.'),
  dict(statement_id='R2-005-M2', date=end, who='GPT-6 Astra Pro; inherited effort setting not exposed; R2', type='targeted proof check', outcome='Margin nonemptiness equivalence proved using downward closure under closed subsets; automatic nonemptiness for M≠∅ proved from union=M.')])

(out/'scan005.json').write_text(json.dumps(data, ensure_ascii=False, indent=2))
(out/'scan005.md').write_text('''# R2 — independent reading, scan 005

Whole page and both supplied halves were inspected once, followed by 24 distinct targeted crops. All 30 C doubts have an individual decision with stroke evidence. The initial overlarge display batch was truncated before the images were available in context; its existing crops were displayed again in small batches, without making any new version of those crops.

The Scholie correspondence is a horizontal line with transverse ticks at both ends, not an arrowhead. Its following set-letter is visibly script F in F(M). In b′ the family within braces has a straight overbar, the three variable occurrences are lowercase x, and the named principal member is uppercase tilde X. The second primed label is a′. The F cancelled after élément is legible. The definition annotation reads defn without a separable accent or raised terminal exponent.

The lower definition literally has F∨C, while its relation and braced pair use G. The first line of the last brace begins X, then the compatibility sign, then réflexive symétrique; it has no second X. These irregularities are retained.

The principal low-confidence groups are the overwritten earlier page number 3; circled e and f; opening quotation before figures; the three upper cancelled forms (script F, éléments, minimaux); cancelled At 1|At 4 and 4|et in the introduction; the tiny deleted d; Phi|varphi; cancelled (et; the union index in|+; the first erased F in b′; cancelled forall|F before Dans; and cancelled est. M/L and script/calligraphic F remain alphabet doubts. I attach the short underline beneath the lieux replacement to live lieux at medium confidence, with the scope recorded explicitly for adjudication.

The full left margins are transcribed. Their distinctive readings are Axiomes des sommes majorées de figures, Axiome des strates équivaut à, d’inclusion de figures par strates, and the complete nonemptiness note with équivaut à. Déployement retains y. No new content omitted by both witnesses was identified.

Two narrow mathematical checks were actually made and are recorded separately: the displayed inclusion criterion follows from At2, and the nonemptiness claims in the c margin follow from the stated closed-subset and covering clauses. The complete Scholie and final reconstruction statement were not proved.
''')
print(len(D), 'difference rows;', len(A), 'C doubts;', len(manifest), 'crops')
