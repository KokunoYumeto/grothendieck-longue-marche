import json
from pathlib import Path

ROOT = Path('/workspace/scratch/d7279cb02214/SP92_C13_150+151_work')
PAGE = '150_scan088'
packet = json.loads(Path('/workspace/scratch/d7279cb02214/reading_packets/150_scan088/packet.json').read_text())
crop_rows = json.loads((ROOT/'records'/f'{PAGE}_cropmap.json').read_text())
crop_map = {r[0]: r for r in crop_rows}
changes = []

def change(cid, place, C, H, final, evidence, crop, confidence, kind, error_kind,
           against_C=False, against_H=False, consequential=False, marked_in_H=False,
           change_type=None):
    row = dict(id=cid, place=place, C=C, H=H, final=final, evidence=evidence,
               crop=f'crops/{PAGE}_{crop}.png', box=crop_map[crop][1],
               confidence=confidence, kind=kind, error_kind=str(error_kind),
               against_C=against_C, against_H=against_H, consequential=consequential,
               marked_in_H=marked_in_H)
    if change_type:
        row['change_type'] = change_type
    changes.append(row)

change('C01', 'Formula (80), first index in the parenthesized flag',
       r'j_{\unsure{1}}', r'j_1', r'j_1',
       'The index has a thick capped upright stem, with no separate lower loop. The adjacent j has its own long left-returning descender. The tight crop and the full formula support 1, resolving M0705 on C\'s first reading.',
       'formula80_left_indices', 'high', 'misread symbol or index', 1,
       against_C=True, change_type='doubt resolution')
change('C02', 'Formula (80), right-hand condition belonging to J',
       r'\unsure{i_0\ldots i_p|j_0\ldots j_p}\in J',
       r'j_1\ldots j_p\in J', r'i_{\unsure{0|q}}\ldots i_p\in J',
       'Both base letters have short upright strokes with detached dots; neither has the long descending return of the j forms in the flag to the left. The first subscript is a closed loop with a thick descending right return: it is not the capped upright 1, but the crop does not securely distinguish 0 from q. The final subscript has an upright and right bowl, p. M0706 is narrowed at i/j, not wholly resolved.',
       'formula80_right_indices', 'medium', 'misread symbol or index', 1,
       against_C=True, against_H=True, consequential=True)
change('C03', 'Formula (80), punctuation after the right-hand J and L conditions',
       r'\in J\\ l_1\ldots l_q\in L\\',
       r'\in J,\quad l_1\ldots l_q\in L,\quad',
       r'\in J\\ l_1\ldots l_q\in L\\',
       'The two conditions occupy successive manuscript lines. Blank paper follows the right foot of J and the foot of L; neither line has a comma. H supplies commas in its one-line arrangement.',
       'formula80', 'high', 'text not on the page', 9, against_H=True)
change('C04', 'Bridge after (80), canceled word between et and on',
       r'\deleted{\unsure{ensuite}}', r'\struck{\ill{}}',
       r'\deleted{\unsure{ensuite}}',
       'A long rising strike crosses the word. Rounded low runs and the terminal uite-like sequence remain, supporting the narrow candidate ensuite, but the initial/middle joins are crossed and not every letter is plain. The C doubt is retained; the ink is more informative than an undifferentiated illegible span.',
       'canceled_ensuite', 'medium', r'readable ink left as \ill{}', 5,
       against_H=True, marked_in_H=True)
change('C05', 'Diagram (81), lower object, commas around the ellipsis',
       r'\Sigma_{j_1,\ldots,j_p}', r'\Sigma_{j_1\ldots j_p}',
       r'\Sigma_{j_1,\ldots,j_p}',
       'Two short descending strokes flank the central ellipsis, one after the 1 and one before the last j. Their descents distinguish them from the smaller, higher ellipsis dots. They are present in C and missing in H.',
       'diagram81', 'high', 'omission', 3, against_H=True)
change('C06', 'Underlined heading Remarque',
       r'\uline{Remarque}', r'\emph{Remarque}.', r'\uline{Remarque}',
       'The final e is followed by white space before Les. There is no point after the word; the long low stroke is its underline, and the q descender crosses it.',
       'remarque_heading', 'high', 'text not on the page', 9, against_H=True)
change('C07', 'Encircled insertion after un sens, last word',
       r'\inserted{(dans une catégorie isotopique convenable)}',
       r'\add{(dans une catégorie isotopique \ill{})}',
       r'\inserted{(dans une catégorie isotopique convenable)}',
       'The second short line of the insertion reads convenable: the low con-ve-na run is followed by the taller b/l strokes and final e before the closing parenthesis. Its enclosing oval has a leader to the gap after sens, before indépendamment. The word remains live.',
       'remark_insertion', 'high', r'readable ink left as \ill{}', 5,
       against_H=True, consequential=False, marked_in_H=True)
change('C08', 'Remark, indépendamment des rétractions',
       'des', 'de', 'des',
       'After the looped d and low e run, the ending rises slightly and turns down in a reduced final return. This supports des, although the s is compressed into that terminal turn. The choice is not made from grammatical agreement; C is retained at medium confidence.',
       'des_retractions', 'medium', 'misread word', 2, against_H=True)
change('C09', 'Remark, ainsi que les Sigma',
       'les', 'ces', 'les',
       'The initial open curve rises well above the following low e/s run, matching a tall cursive l rather than the short c shape. The final low return supplies s. The word is les.',
       'les_sigma', 'high', 'misread word', 2, against_H=True)
change('C10', 'Remark, la description que j\'en ai donné ici',
       'donné', 'donnée', 'donné',
       'After the d loop and compressed on-n run, one final short e stroke sits below an accent. The next detached upright and dot belong to ici. There is no second e between the accented ending and ici; the written agreement is preserved.',
       'donne', 'high', 'misread word', 2, against_H=True)
change('C11', 'Remark, live replacement above canceled structures',
       r'\inserted{\unsure{fibrations|rétractions}}', r'\add{rétractions}',
       r'\inserted{fibrations}',
       'The live word begins with a tall crossed f, a dotted short i, and a tall b, followed by r-a-t-i-o-n-s. It does not begin with the low r and accented e of rétractions earlier on the page. It sits directly over the canceled structures and replaces that word. M0707 resolves on the first reading.',
       'revision_block', 'high', 'misread word', 2,
       against_C=True, against_H=True, consequential=True)
change('C12', 'Remark, separately inserted and then canceled short phrase above côniques',
       r'\inserted{\deleted{\unsure{de ri.}}}', '',
       r'\inserted{\deleted{\unsure{de ri.}}}',
       'A distinct raised line of small writing sits above the canceled côniques and is crossed by its own rising horizontal stroke. The first looped d and the dotted short second group support de ri., but the cross-out obscures joins and merges with the possible terminal stop. Retain the narrow C doubt and both insertion/deletion states. H omits this ink from its transcription, though its editorial note acknowledges two unread canceled words.',
       'canceled_insert', 'low', 'omission', 3,
       against_H=True, marked_in_H=True)
change('C13', 'Remark, canceled côniques below the small canceled insertion',
       r'\deleted{coniques}', r'\struck{structures côniques}',
       r'\deleted{côniques}',
       'A separate curved circumflex sits above the o area, below the d of the raised insertion. It is spatially distinct from both cancellation strokes. The original word is crossed through, including its q-descender area, and retains the written circumflex.',
       'revision_block', 'high', 'misread word', 2, against_C=True)
change('C14', 'Remark, sign between dispose and des',
       r'dispose $=$ des', 'dispose de', r'dispose $=$ des',
       'Two short parallel horizontal strokes stand alone between dispose and the following word. They form the prose abbreviation =, not a strike or a leader; H drops it.',
       'disposal', 'high', 'omission', 3, against_H=True)
change('C15', 'Remark, word after the = sign',
       'des structures', 'de structures', 'des structures',
       'The word after = has a looped d, low e run and terminal downward turn before structures. The compressed closing return supports the final s. Retain des as written.',
       'disposal', 'medium', 'misread word', 2, against_H=True)
change('C16', 'Remark, live structures côniques near the foot',
       'structures coniques', 'structures côniques', 'structures côniques',
       'A separate short curved cap is visible above the o of the live côniques. It is not attached to the tall q descender or the neighboring line. Unlike the earlier live rétractions coniques, this occurrence has the circumflex.',
       'disposal', 'high', 'misread word', 2, against_C=True)
change('C17', 'Remark, phrase split across the two lower lines, le cas équisingulier',
       r'\unsure{le cas équisingulier|la géom. algéb.}',
       'le cas équisingulier', 'le cas équisingulier',
       'The preceding line ends with a tall l and low e. The next begins cas, followed by an accented é, long q descender, dotted i sequence, the long lower g loop, and the terminal l-i-er run. No géom. or algéb. abbreviation is present. M0708 resolves on the first reading.',
       'equisingulier', 'high', 'misread word', 2,
       against_C=True, change_type='doubt resolution')
change('C18', 'Remark, quoted word after donnée supplémentaire',
       "``anodine''", r'« \ill{} »', "``anodine''",
       'Between the paired high quotation ticks, the writing shows a-n-o, the tall looped d, a dotted i, and low n-e ending. All the letters of anodine are legible.',
       'anodine', 'high', r'readable ink left as \ill{}', 5,
       against_H=True, marked_in_H=True)
change('C19', 'Remark, quotation glyphs around anodine',
       "``anodine''", r'« \ill{} »', "``anodine''",
       'There are two small upright high ticks before a and two high ticks after the final e. No angled chevrons are drawn. Preserve the two opening backticks and two closing apostrophes.',
       'anodine', 'high', 'misread symbol or index', 1, against_H=True)
change('C20', 'Remark, H extra illegible span before the opening quotation ticks',
       "supplémentaire ``anodine''", r'supplémentaire \ill{} « \ill{} »',
       "supplémentaire ``anodine''",
       'The manuscript proceeds from supplémentaire at the end of the preceding line directly to the opening quotation ticks and anodine on the final line. There is no intervening written word corresponding to H\'s first illegible placeholder.',
       'anodine', 'high', 'text not on the page', 9,
       against_H=True, marked_in_H=True)
change('C21', 'Bottom-left thin foliation', r'\margin{87}', '', r'\margin{87}',
       'A thin grey 8, with two loops, is followed by an angular 7 with a long descending stroke at the extreme lower left. It belongs to another hand and is retained as a margin item, not as the author\'s page number. H does not transcribe this foliation.',
       'folio87', 'high', 'omission', 3, against_H=True)

coverage_spec = {
 'D0393': ('editorial-only', [], 'Scan marker 88 is editorial apparatus; H\'s note about authorial numbering and another folio is not page text. The original has no authorial number at its head.'),
 'D0394': ('macro-only', [], 'The tokenized comma is H\'s TeX thin-space command between the j and l parts of the flag, not a punctuation comma.'),
 'D0395': ('reading', ['C02'], 'The row mixes gathered syntax with the substantive i/j alternative in the right-hand condition; C02 records the narrowed reading.'),
 'D0396': ('reading', ['C02'], 'The first right-hand subscript is looped, incompatible with H\'s simple 1; 0/q remains narrowly uncertain.'),
 'D0397': ('reading', ['C03'], 'No comma follows the right-hand J in the manuscript.'),
 'D0398': ('reading', ['C03'], 'No comma follows the right-hand L in the manuscript.'),
 'D0399': ('macro-only', [], 'End of gathered environment versus a one-line math arrangement; no different ink.'),
 'D0400': ('reading', ['C04'], 'Canceled ink supports a narrow ensuite candidate; the C doubt remains, while H has only an illegible span.'),
 'D0401': ('macro-only', [], 'Tikz-cd options versus an array representation of the same three-object diagram. Candidate uses tikz-cd and places (81) to the left.'),
 'D0402': ('macro-only', [], 'C\'s tokenized comma is a thin math space between the j and l index groups in the top diagram object.'),
 'D0403': ('macro-only', [], 'C encodes the right hooked arrow and downward arrow as Tikz-cd commands; H supplies the same visible arrows in its array. Both arrowheads and the left hook were checked.'),
 'D0404': ('reading', ['C05'], 'Two genuine low commas flank the lower object\'s ellipsis; H omits them.'),
 'D0405': ('editorial-only', [], 'Diagram environment endings are macro syntax; H\'s comment on numbering continuity is editorial, not ink.'),
 'D0406': ('reading', ['C06'], 'H adds a period after the underlined heading; no period is written.'),
 'D0407': ('reading', ['C07'], 'Convenable is legible inside the encircled insertion, where H leaves an illegible span.'),
 'D0408': ('reading', ['C08'], 'Reduced terminal return favors des over H de; retained at medium confidence and boxed for blind reread.'),
 'D0409': ('reading', ['C09'], 'Tall initial cursive l gives les, not H ces.'),
 'D0410': ('macro-only', [], 'Two versus three TeX hyphens represent the single written horizontal dash after Sigma_L; no text change.'),
 'D0411': ('reading', ['C10'], 'Only one final accented e occurs before ici; preserve donné.'),
 'D0412': ('macro-only', [], 'Tokenized dash-length difference after cas; both witnesses represent the same written dash.'),
 'D0413': ('reading', ['C11'], 'The inserted word is aligned before the deleted phrase in H and after structures in C; this is the same replacement site. The substantive reading is fibrations, not rétractions.'),
 'D0414': ('reading', ['C11', 'C12', 'C13'], 'The live replacement reads fibrations; the raised canceled short phrase is preserved with doubt; the lower canceled côniques has a circumflex.'),
 'D0415': ('reading', ['C14', 'C15'], 'The separate = abbreviation and the compressed final s of des are present.'),
 'D0416': ('reading', ['C16'], 'Live côniques has a visible circumflex, agreeing with H against C.'),
 'D0417': ('reading', ['C17'], 'The C alternative is resolved to le cas équisingulier on its crop; H already has that reading.'),
 'D0418': ('reading', ['C18', 'C19', 'C20'], 'Anodine is legible between paired high ticks; no guillemets or extra intervening illegible word are written.'),
 'D0419': ('reading', ['C21'], 'The physical other-hand foliation 87 is retained. H\'s long concluding editorial note is excluded from the transcription and is not a reading change.'),
}
diff_coverage = [dict(diff_id=d['diff_id'], classification=coverage_spec[d['diff_id']][0],
                      change_ids=coverage_spec[d['diff_id']][1], reason=coverage_spec[d['diff_id']][2])
                 for d in packet['differences']]

def decision(mid, verdict, reading, ink, crop, confidence):
    return dict(id=mid, cote='150', scan='88', decision=verdict, reading=reading, ink=ink,
                crop=f'crops/{PAGE}_{crop}.png', box=crop_map[crop][1], confidence=confidence)

decisions = [
 decision('M0705', 'first', '1', 'The first j index has a capped upright, with no closed loop. The full flag and neighboring l_1, j_p and l_q were reread.', 'formula80_left_indices', 'high'),
 decision('M0706', 'undecided', r'i_{\unsure{0|q}}\ldots i_p', 'Partially narrowed: the short dotted base strokes are i, contrasting with long descending j in the same formula. The first subscript has a closed loop and descending right return, leaving 0/q unresolved. It is not securely 1.', 'formula80_right_indices', 'medium'),
 decision('M0707', 'first', 'fibrations', 'Tall crossed f, dotted i and tall b begin the live insertion; the following compressed run is rations. It replaces the canceled structures.', 'revision_block', 'high'),
 decision('M0708', 'first', 'le cas équisingulier', 'Le closes the upper line; cas opens the next. The following accented é, q descender, dotted i forms, g loop and l-ier ending read équisingulier.', 'equisingulier', 'high'),
]

def inv(element, kind, position, words, hand='author'):
    return dict(sheet_kind='text', hand=hand, element=element, kind=kind, position=position,
                first_words_or_objects=words, transcribed='yes')

inventory = [
 inv('Opening continuation paragraph', 'text', 'Upper page, three sloping main baselines, approximately x325–1575 y65–380', 'qui s\'explicitent en termes de (78)'),
 inv('Insertion in opening paragraph and its curved attachment leader', 'insertion', 'Between second and third main lines, approximately x515–1035 y235–365; leader attaches after J union L', 'intervenant dans (78)'),
 inv('Numbered flag display', 'display', 'Upper-middle page, x295–1510 y345–570; label (80) at left, three condition lines at right', r'(80) (j_1...j_p l_1...l_q); i_{\unsure{0|q}}...i_p in J'),
 inv('Short bridge to diagram', 'text', 'Below (80), x335–1065 y575–645', r'et \deleted{\unsure{ensuite}} on a des'),
 inv('Canceled word in bridge', 'deletion', 'Between et and on, approximately x465–680 y585–630', r'\unsure{ensuite}'),
 inv('Three-object diagram and left formula number', 'diagram', 'Middle page, x285–1380 y670–1005; top-left object to top-right by a hooked right arrow, and down to the third object', r'(81) Sigma_{j_1...j_p l_1...l_q}, Sigma_{l_1...l_q}, Sigma_{j_1,...,j_p}'),
 inv('Encircled parenthetical insertion with a short leader', 'insertion', 'Above the remark at upper right, two short writing rows in x965–1665 y950–1145; attaches after un sens', '(dans une catégorie isotopique convenable)'),
 inv('Underlined remark heading', 'text', 'Left of first remark line, x270–610 y1110–1235', 'Remarque'),
 inv('Remark body', 'text', 'Eleven sloping main lines, approximately x220–1655 y1095–2130, ending at plus commode,', 'Les Sigma_{J,L} ont un sens'),
 inv('Canceled original noun', 'deletion', 'Remark revision site, x1020–1300 y1615–1695, crossed by a long rising stroke', 'structures'),
 inv('Live noun replacement', 'insertion', 'Immediately above canceled structures, x1050–1300 y1565–1650', 'fibrations'),
 inv('Raised short phrase, later canceled', 'insertion', 'Above canceled côniques, x1340–1530 y1575–1640', r'\deleted{\unsure{de ri.}}'),
 inv('Cancellation of the raised short phrase', 'deletion', 'Separate rising stroke through the small inserted line above côniques', r'\unsure{de ri.}'),
 inv('Canceled original adjective with accent', 'deletion', 'To the right of canceled structures, approximately x1340–1625 y1605–1675', 'côniques'),
 inv('Thin lower foliation', 'margin note', 'Extreme bottom-left corner, x20–100 y2280–2356', '87', 'another hand; thin grey foliation, not authorial numbering'),
]

deletion_insertion_review = [
 dict(C_item=r'\inserted{intervenant dans (78)}', state='live insertion',
      bounds='One raised text line; its long curved underline/leader is not a cancellation.',
      attachment='After J union L, before s\'écrit; leader curves down into that gap.', crop=f'crops/{PAGE}_opening_insertion.png', box=crop_map['opening_insertion'][1]),
 dict(C_item=r'\deleted{\unsure{ensuite}}', state='canceled; narrow doubt retained',
      bounds='The rising stroke starts within the word after et and ends at its terminal letters; et and on a des remain live.',
      attachment='No replacement is indicated; the live sentence continues on a des.', crop=f'crops/{PAGE}_canceled_ensuite.png', box=crop_map['canceled_ensuite'][1]),
 dict(C_item=r'\inserted{(dans une catégorie isotopique convenable)}', state='live insertion, enclosed by an oval',
      bounds='Two writing rows inside a large enclosing oval; the parenthesis marks are text, distinct from the outer oval.',
      attachment='Short descending leader reaches the gap after sens and before indépendamment.', crop=f'crops/{PAGE}_remark_insertion.png', box=crop_map['remark_insertion'][1]),
 dict(C_item=r'\deleted{structures}', state='canceled original word',
      bounds='Long horizontal/rising strike crosses structures and continues toward the separately struck adjective; les before it and locales on the next line remain live.',
      attachment='The live replacement fibrations is immediately above structures.', crop=f'crops/{PAGE}_revision_block.png', box=crop_map['revision_block'][1]),
 dict(C_item=r'\inserted{\unsure{fibrations|rétractions}}', state='live insertion; resolved to fibrations',
      bounds='Raised word above structures is not crossed by the lower cancellation stroke.',
      attachment='Replaces the original structures after utilise les.', crop=f'crops/{PAGE}_revision_block.png', box=crop_map['revision_block'][1]),
 dict(C_item=r'\inserted{\deleted{\unsure{de ri.}}}', state='inserted and then canceled; narrow doubt retained',
      bounds='Small raised phrase above côniques has its own rising strike. The possible terminal point is inseparable from the strike ending.',
      attachment='Inserted between fibrations and the original adjective region; no live replacement for this raised phrase is legible.', crop=f'crops/{PAGE}_canceled_insert.png', box=crop_map['canceled_insert'][1]),
 dict(C_item=r'\deleted{coniques}', state='canceled; read côniques with visible circumflex',
      bounds='Adjective on the original baseline is crossed through. The curved cap above its o remains visible between this word and the raised canceled phrase.',
      attachment='Part of the canceled original structures côniques; locales remains live on the next line.', crop=f'crops/{PAGE}_revision_block.png', box=crop_map['revision_block'][1]),
]

opening = r"qui s'explicitent en termes de (78) en notant que tout drapeau de $J\cup L$ \inserted{intervenant dans (78)} s'écrit de façon unique"
formula80 = r'''\[
(80)\qquad(j_1\ldots j_p\ l_1\ldots l_q)\qquad
\begin{gathered}[t]
i_{\unsure{0|q}}\ldots i_p\in J\\
l_1\ldots l_q\in L\\
p,q\geq1
\end{gathered}
\]'''
diagram81 = r'''\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
(81)\&\Sigma_{j_1\ldots j_p\,l_1\ldots l_q}\arrow[r,hook]\arrow[d]\&\Sigma_{l_1\ldots l_q}\\
\&\Sigma_{j_1,\ldots,j_p}\&
\end{tikzcd}}'''
revision = r'\deleted{structures} \inserted{fibrations} \inserted{\deleted{\unsure{de ri.}}} \deleted{côniques}'
second_spec = [
 ('B01', 'Opening paragraph, insertion and both handwritten (78) references', [325,65,1575,380], opening),
 ('B02', 'Whole formula with C/final doubts, all indices, inequality and formula label (80)', [295,345,1510,570], formula80),
 ('B03', 'Canceled bridge word and its live neighbors', [335,575,1065,645], r'et \deleted{\unsure{ensuite}} on a des'),
 ('B04', 'Whole diagram, number (81), all mathematical digits, arrows and lower commas', [285,670,1380,1005], diagram81),
 ('B05', 'Encircled insertion after sens, including convenable and attachment', [965,950,1665,1145], r'\inserted{(dans une catégorie isotopique convenable)}'),
 ('B06', 'Heading punctuation and underline', [270,1110,610,1235], r'\uline{Remarque}'),
 ('B07', 'Different word: des, compressed terminal s', [620,1200,1025,1305], 'des rétractions'),
 ('B08', 'Different word: les before the inclusion', [840,1360,1375,1460], r'les $\Sigma_{J,L}\hookrightarrow\Sigma_L$'),
 ('B09', 'Different word: donné with neighboring ici est', [1300,1410,1650,1515], 'donné ici est'),
 ('B10', 'Complete remark revision: live replacement, two original canceled words, inserted-then-canceled phrase', [1010,1540,1625,1700], revision),
 ('B11', 'Prose abbreviation =, des and the live accented côniques', [475,1710,1655,1855], r'Quand on dispose $=$ des structures côniques'),
 ('B12', 'Resolved C phrase: le at the right end of one line, cas équisingulier at the start of the next', [220,1780,1655,2055], 'le cas équisingulier'),
 ('B13', 'Quoted word and paired high ticks at the start of the final line', [235,2020,635,2130], "``anodine''),"),
 ('B14', 'Other-hand lower foliation', [20,2280,100,2356], r'\margin{87}'),
]
second_boxes = [dict(box=n, kind=k, x0=b[0], y0=b[1], x1=b[2], y1=b[3], reading=r)
                for n,k,b,r in second_spec]

notes = r'''## Content and page state
The opening continuation says that each flag of J union L intervening in (78) has a unique displayed form (80). The following numbered diagram (81) places the object indexed by both flag parts above the object indexed by the j part and to the left of the object indexed by the l part. The upper map is a rightward hooked arrow with an arrowhead; the downward map has a plain arrowhead.

The underlined Remarque states that the Sigma_{J,L} objects, in a suitable isotopic category, and their inclusions into Sigma_L have a meaning independent of the local conical retractions in moderate topological theory. The map to Sigma_J is said to use local fibrations. The paragraph then discusses the additional local conical structures in the equisingular case and stops after “il est plus commode,”. This is a transcription summary, not a proof verification.

## Formula and notation rereading
Both C marks in (80) prompted a reread of the entire display, including its label, parentheses, ellipses, both flag parts, all four first/final indices, the membership relations, p,q and the >= sign and 1. The first j index is a capped upright 1. The right condition uses short dotted i forms, whereas the parenthesized flag has long descending j forms. That written mismatch is preserved. Its first right-hand index is a closed loop with a descending right return: 0 and q remain possible, so i_{\unsure{0|q}} is retained. Mathematics did not supply a replacement j or 1. The p index, l_1...l_q and p,q>=1 are readable. No commas follow the terminal J and L. The initial l_1 in the flag is heavily reinforced, with overlapping low strokes; no distinct underlying deleted letter can be separated, so no extra deleted symbol is asserted.

The whole diagram was reread independently. It has three objects and exactly two arrows. The upper arrow has a left hook and a right arrowhead; the lower arrow has a downward arrowhead and no hook. The lower object's two low comma strokes around the ellipsis remain. The j forms there are less dotted and more angular than in (80); their difference alone does not justify changing them to capital J. All diagram digits and the left-hand (81) label have blind reread coverage.

## Revisions, words and punctuation
The opening insertion “intervenant dans (78)” is attached by a curved leader after J union L. Its long baseline is not a deletion. The canceled ensuite is still only a narrow candidate: the strike obscures joins, so the C doubt is retained. The encircled parenthesis after sens is live; its second line convenable is readable. The enclosing oval and its leader were distinguished from the actual parentheses.

At the lower revision, structures and côniques are canceled. Fibrations is live above structures. The small raised de ri. is separately canceled; both its letter joins and possible final stop remain uncertain. The circumflex above the original canceled adjective is visible. The later live côniques also has a circumflex, but the earlier live rétractions coniques has none. These occurrences are kept distinct.

The two des readings have reduced final returns and are retained at medium confidence, with dedicated blind regions. Les has a tall open cursive l. Donné has one accented final e, without an extra e for grammatical agreement. The full tout in the opening was checked on a tight crop: two low intermediate strokes occur between the t stems, so it is not reduced to tt. The prose = is written as two parallel strokes and is retained as the usual abbreviation for même. “Le cas équisingulier” is legible across its line break. Anodine is fully legible between paired high quotation ticks, with no extra word before the opening ticks. No guillemets are written.

## Numbering and editorial limits
There is no authorial page number at the head, no date, and no title beyond the underlined heading Remarque. Formula numbers (80) and (81) stand at the left; (78) is cited twice. The extreme lower-left 87 is thin grey foliation in another hand and is preserved as \margin{87}, not \mspage{87}. H's introductory and concluding editorial notes, including claims about neighboring leaves, are not manuscript text and were not checked against any other page. No explicit authorial question mark or stated mathematical doubt occurs on this leaf. The only surviving uncertainties listed here are editorial readings of ink. No proof, computation or mathematical validity check was performed.'''

notation = [
 dict(sign=r'i_{\unsure{0|q}}...i_p versus j_1...j_p', reading='Preserve short dotted i in the right-hand condition and long descending j in the flag; first i index remains 0/q.', evidence='Formula (80), broad and two tight index crops; clear difference in stem length and descender, unresolved looped index.'),
 dict(sign='=', reading='Prose abbreviation for même; transcribe the sign.', evidence='Two standalone parallel horizontal strokes between dispose and des.'),
 dict(sign='hooked right arrow and plain downward arrow', reading='Retain actual hooks and arrowheads separately.', evidence='Diagram (81): left hook plus right arrowhead on the upper map; simple downward arrowhead below the top-left object.'),
 dict(sign='`` ... \'\'', reading='Paired high quotation ticks, not guillemets.', evidence='Two high marks before and two after anodine.'),
 dict(sign='coniques / côniques', reading='Retain occurrence-specific accent: first live coniques unaccented, canceled and later live côniques accented.', evidence='Visible curved cap over o in the revision and lower live occurrence; no cap at the earlier rétractions coniques.'),
]
hand_log = [
 dict(habit='Short dotted i is distinguishable from the long descending j on this leaf.', places='(80), right condition versus the parenthesized flag', scope='Secure for these formula occurrences; the index 0/q is a separate unresolved issue.', witness_errors='H gives j in the right condition; C had i/j alternatives.'),
 dict(habit='Compressed final s can merge into a low terminal return after e.', places='indépendamment des rétractions; dispose = des structures', scope='Both retained at medium confidence; not a universal rule that every terminal return is s.', witness_errors='H gives de at both places.'),
 dict(habit='The cursive lowercase l may be an open tall curve resembling an enlarged c.', places='ainsi que les Sigma', scope='Local comparison with the low e and s within this word.', witness_errors='H reads ces.'),
 dict(habit='The ending of donné is reduced to short low strokes under a detached accent.', places='j\'en ai donné ici', scope='The next i is clearly separated; no additional e is supplied for agreement.', witness_errors='H reads donnée.'),
 dict(habit='Dotted i after tall f and b distinguishes fibrations from the outline of rétractions.', places='Live replacement over structures', scope='The initial three letters are particularly clear in the raised replacement.', witness_errors='H reads rétractions; C offers fibrations/rétractions.'),
 dict(habit='Mathematical j can be undotted and angular in small diagram indices.', places='Diagram (81), upper-left and lower objects', scope='Record locally; do not convert an angular form to capital J from absence of a dot alone.', witness_errors='No new witness error asserted at these diagram letters.'),
 dict(habit='Written tout has separate low intermediate strokes; tall end stems alone do not establish an abbreviation.', places='en notant que tout drapeau', scope='One occurrence examined on a tight crop.', witness_errors='Both witnesses retained tout; confirmed visually.'),
]

doubts = [
 dict(place='(80), first subscript in right-hand i condition', reading=r'i_{\unsure{0|q}}', alternatives=['0','q'], confidence='medium', reason='Closed loop and long right return do not securely distinguish the two; the i base letter is clear and H\'s upright 1 is unsupported.'),
 dict(place='Canceled word after et below (80)', reading=r'\deleted{\unsure{ensuite}}', alternatives=['ensuite','unresolved crossed initial/middle joins'], confidence='medium', reason='A candidate word remains visible, but the rising strike prevents every letter from being read; the C doubt stays.'),
 dict(place='Inserted-then-canceled short phrase above côniques', reading=r'\inserted{\deleted{\unsure{de ri.}}}', alternatives=['de ri.','de ri with no distinct final stop','unresolved letters under the strike'], confidence='low', reason='Small letter joins and possible terminal stop merge with the strike. No expansion is supplied and the C doubt is retained.'),
]

data = dict(
 page=PAGE, cote='150', scan='88', reader='reader_a; GPT-6 Astra Pro; effort not exposed; run SP92',
 line_count=26,
 line_count_note='Counted writing rows, not TeX lines: 15 main prose baselines (3 opening, 1 bridge, 11 remark); 5 added/raised rows (1 opening insertion, 2 in the encircled parenthesis, 1 fibrations, 1 canceled de ri.); 3 rows of (80); 2 labeled-object rows of (81); 1 other-hand foliation row. Subscripts and arrow shafts are not separate lines.',
 half_review='Whole original reviewed for layout. Both supplied native-resolution overlapping halves were inspected and every prose line, formula, diagram, number, agreed reading, accent and revision was read against C and H. The halves were revisited for coordinate scope. All 18 saved crops were inspected; formula80 and diagram81 were reframed upward to remove clipped top glyphs, and the final versions were inspected. No OCR, external research or TeX compilation was used.',
 deletion_insertion_review=deletion_insertion_review,
 changes=changes, diff_coverage=diff_coverage, decisions=decisions, inventory=inventory,
 notes=notes, check_events=[], notation=notation, hand_log=hand_log,
 abbreviations=[dict(form='=', expansion='même')], doubts=doubts, second_boxes=second_boxes,
 crops=[dict(path=f'crops/{PAGE}_{n}.png', box=b, rotation_degrees=r, output_width=w, inspected=True)
        for n,b,r,w in crop_rows],
)

assert len(diff_coverage) == len(packet['differences']) == 27
assert [d['id'] for d in decisions] == [m['id'] for m in packet['marks']]
assert len({c['id'] for c in changes}) == len(changes)
valid_kinds = {'misread word','misread symbol or index','omission','text not on the page',
               'deletion state (struck given live or live given struck)','insertion or placement',
               'abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(c['kind'] in valid_kinds for c in changes)
assert all((ROOT/c['crop']).exists() for c in changes)
assert len(data['crops']) == 18
text = (ROOT/'records'/f'{PAGE}.tex').read_text()
assert opening in text and formula80 in text and diagram81 in text and revision in text
out = ROOT/'records'/f'{PAGE}.json'
out.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(dict(page=PAGE, changes=len(changes), differences=len(diff_coverage), decisions=len(decisions), inventory=len(inventory), second_boxes=len(second_boxes), crops=len(data['crops']), unresolved=len(doubts)), ensure_ascii=False))
