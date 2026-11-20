from pathlib import Path
import json

root = Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
pkt = json.loads(Path('/workspace/scratch/8f839dff4bf0/reader_packets/143_scan024.json').read_text())
Csrc, Hsrc = pkt['witness_C'], pkt['witness_H']
key = '143_scan024'

candidate = r'''\scanpage{24}
\mspage{12}
Inversement, donnons-nous \inserted{un groupe $T$ abélien} un $T$-groupoïde \deleted{\unsure{connexe}} $\Lambda$, une opération de $\unsure{\mathcal E|\Sigma}$ sur $(T,\Lambda)$, et un hom de groupoïdes
\diagram{\begin{tikzcd}[ampersand replacement=\&]
\Lambda \arrow[r,"\text{foncteur \uuline{fidèle}}"] \& \begin{gathered}\text{groupoïde \unsure{à|:} un seul objet}\\\text{des rev. universels de}\\\Pi\text{ égaux à }\widetilde\Pi\\\text{dont les autom sont }\pi\end{gathered}
\end{tikzcd}}
compatible avec action de $\unsure{\mathcal E|\Sigma}$.
Soit $\unsure{\tau|\mathcal T}=\operatorname{Ob}\Lambda$ [donc $\unsure{\tau|\mathcal T}$ est un $\unsure{\mathcal E|\Sigma}$ ens,] et pour $\forall\,t,t'\in\unsure{\tau|\mathcal T}$, on a un hom \uline{injectif}
\diagram{\begin{tikzcd}[ampersand replacement=\&]
\underbrace{\operatorname{Isom}_\Lambda(t,t')}_{\pi_{t,t'}} \arrow[r,hook,"\unsure{\vphantom{\to}}"] \& \pi
\end{tikzcd}}
compatible avec composition des isom.

On a exprimé la donnée d'un foncteur fidèle d'un groupoïde $\Lambda$ dans $\langle\pi\rangle$ \deleted{Mais \unsure{on}} [il faut se donner une famille de sous groupes $(\pi_t)_{t\in\unsure{\tau|\mathcal T}}$ de $\pi$ et d'ens vides ou bitorseurs sous les $\pi_{t'},\pi_t\ldots$] On va maintenant introduire les op. de
\mspage{23}
'''

boxes = {
    'opening_attachment': [700, 90, 1662, 421],
    'cancelled_adjective': [590, 224, 859, 289],
    'codomain_and_action': [883, 553, 1658, 927],
    'object_set': [282, 930, 1585, 1167],
    'injection': [571, 1274, 1254, 1460],
    'mais_and_bracket': [517, 1740, 1470, 1878],
    'family_and_bitorsors': [295, 1986, 1457, 2196],
}

def loc(crop):
    if crop is None:
        return 'page', None
    return f'crops/{key}_readerB_{crop}.png', boxes[crop]

def row(place, C, H, final, ac, ah, kind, ink, confidence='high', crop=None, marked=False, consequential=False):
    assert C == '[no witness]' or C in Csrc, ('C excerpt is not literal', place, C)
    assert H == '[no witness]' or H in Hsrc, ('H excerpt is not literal', place, H)
    assert final == '' or final in candidate, ('Final excerpt is not literal', place, final)
    path, box = loc(crop)
    return {'place': place, 'C': C, 'H': H, 'final': final, 'against_C': ac, 'against_H': ah,
            'kind': kind, 'ink': ink, 'confidence': confidence, 'crop': path, 'box': box,
            'marked_in_H': marked, 'consequential': consequential}

changes = []
changes.append(row('Opening, alleged two words after donnons-nous (M0704)',
    r'\illegible{2}', '[no witness]', '', True, False, 'text not on the page',
    'The scattered short strokes above the second line complete donnons-nous. After the last horizontal return there is only the apex of the large insertion call; no separate two-word passage can be localized. The placeholder is omitted, subject to main-reader review of this newly rejected locus.',
    'medium', 'opening_attachment'))
changes.append(row('Opening, upper-right insertion and its attachment',
    r'\inserted{un groupe $T$ abélien}', '(un\ngroupoïde $T$-\\uncertain{fidèle})',
    r'\inserted{un groupe $T$ abélien}', False, True, 'insertion or placement',
    'A broad call surrounds the words un groupe T abélien and rises to the end of the opening line, before the continuing un T-groupoïde. The word after T has the tall b/l strokes and dotted i of abélien; it is not a second groupoïde T-fidèle parenthesis after Lambda.',
    'high', 'opening_attachment', True))
changes.append(row('Opening, cancelled adjective after T-groupoïde',
    r'\deleted{\unsure{connexe}}', r'\struck{\ill{}}', r'\deleted{\unsure{connexe}}',
    False, True, 'other',
    'The heavy horizontal cancellation leaves a small initial rounded opening, several low humps, and two raised terminal traces. These admit connexe but do not securely disclose all letters. The word remains explicitly doubtful inside the deletion.',
    'low', 'cancelled_adjective', True))
changes.append(row('Opening operation, action-group alphabet',
    r'\mathcal E', r'\Sigma', r'\unsure{\mathcal E|\Sigma}', True, True,
    'misread symbol or index',
    'The isolated glyph has an upper returning curve, a central turn, and a lower rightward foot. It belongs to the shared E/Sigma uncertainty; this row records the unresolved alphabet encoding only, not a consequential mathematical correction.',
    'low', 'opening_attachment'))
changes.append(row('Opening, hom before de groupoïdes',
    'hom de groupoïdes', 'hom.\\ de groupoïdes', 'hom de groupoïdes', False, True,
    'text not on the page',
    'After the low final stroke of hom, the page passes through blank space directly to de. There is no independent abbreviation point at this occurrence.'))
changes.append(row('First diagram, marks before un seul objet',
    'groupoïde à un seul objet', r': un seul \uncertain{objet}',
    r'groupoïde \unsure{à|:} un seul objet', True, True, 'misread symbol or index',
    'Two compact dark marks stand one above the other. They can be a compressed a with its accent, comparable to the equally compressed à before the covered Pi, or a colon. Both readings are retained; this is not a settled correction of either witness.',
    'low', 'codomain_and_action', True))
C_order = r'\text{des rev. universels de}\\\Pi\text{ égaux à }\widetilde\Pi\\\text{dont les autom sont }\pi'
H_order = ', dont les \\uncertain{autom.} sont $\\pi$ ; des revêt.\\\nuniversels de $\\Pi$ égaux à $\\widetilde{\\Pi}$ \\ldots'
changes.append(row('First diagram, order and placement of codomain lines',
    C_order, H_order, C_order, False, True, 'insertion or placement',
    'The right-hand object occupies four consecutive manuscript lines. Below groupoïde ... un seul objet come des rev. universels de, then Pi égaux à covered Pi, then dont les autom sont pi. The automorphism clause is the bottom line, not a clause inserted before des rev.; all belong to the diagram codomain.',
    'high', 'codomain_and_action', True))
changes.append(row('First diagram codomain, rev. abbreviation',
    'rev.', 'revêt.\\', 'rev.', False, True, 'abbreviation expanded or spelling modernised',
    'The short word has the opening r/e movement, a low v return, and a distinct final dot. There is no following tall t or extra syllable to support revêt.',
    'high', 'codomain_and_action'))
changes.append(row('First diagram codomain, autom without a final point',
    'autom sont', r'\uncertain{autom.} sont', 'autom sont', False, True, 'text not on the page',
    'The small internal dot belongs within the compressed autom letter sequence. After its final m stroke there is a gap before sont, with no separate terminal abbreviation point.',
    'high', 'codomain_and_action', True))
changes.append(row('First diagram codomain, no ellipsis after covered Pi',
    r'\Pi\text{ égaux à }\widetilde\Pi', r'$\Pi$ égaux à $\widetilde{\Pi}$ \ldots',
    r'\Pi\text{ égaux à }\widetilde\Pi', False, True, 'text not on the page',
    'The line ends at the capital Pi under its tilde. Its right side is blank before the next manuscript line begins dont; no ellipsis is written there.',
    'high', 'codomain_and_action'))
changes.append(row('Line beneath first diagram, action rather than les opérations',
    'compatible avec action de', 'compatible avec les\nopérations de',
    'compatible avec action de', False, True, 'misread word',
    'After avec there is one word: a small initial a/c movement, the tall crossed t, the i dot, and the low on return of action. No preceding les and no initial long p descender are present.',
    'high', 'codomain_and_action'))
changes.append(row('Compatibility line, action-group alphabet',
    r'\mathcal E', r'\Sigma', r'\unsure{\mathcal E|\Sigma}', True, True,
    'misread symbol or index',
    'This occurrence has a broad rounded upper bowl and a tighter lower curl. Shared E/Sigma identification remains open; only the alphabet uncertainty is recorded.',
    'low', 'codomain_and_action'))
changes.append(row('Soit definition, object-set letter',
    r'\tau=\operatorname{Ob}\Lambda', r'\mathcal{T} = \mathrm{Ob}\,\Lambda',
    r'\unsure{\tau|\mathcal T}=\operatorname{Ob}\Lambda', True, True, 'misread symbol or index',
    'The set letter has a large triangular or flag-like top and one broad lower curved return. It does not show the two successive lobes of the provisionally established ornate Z. Tau and calligraphic T remain alternatives; the equation and Ob Lambda are otherwise unchanged.',
    'medium', 'object_set'))
changes.append(row('Bracket after Ob Lambda, donc',
    '[donc', '[lequel', '[donc', False, True, 'misread word',
    'Immediately after the opening bracket is a looped tall d followed by a short low connected onc trace. The several tall/descending strokes needed for lequel are absent.',
    'high', 'object_set'))
changes.append(row('Object-set bracket, repeated set letter before est un',
    r'\tau$ est un', r'\mathcal{T}$ est un', r'\unsure{\tau|\mathcal T}$ est un',
    True, True, 'misread symbol or index',
    'The smaller repeated letter again has a compact flag at the top and a single open lower curve. The same tau/T alternatives are retained at this inspected occurrence; no mathematical content is changed by the provisional encoding.',
    'medium', 'object_set'))
changes.append(row('Object-set bracket, action-group alphabet',
    r'\mathcal E', r'\Sigma', r'\unsure{\mathcal E|\Sigma}', True, True,
    'misread symbol or index',
    'The final letter on the upper bracket line has an angular upper return and lower foot, consistent with the other two action-group glyphs on this page. It does not settle E versus Sigma.',
    'low', 'object_set'))
changes.append(row('Object-set bracket, ens compound and abbreviation punctuation',
    '-ens', '-ens.', 'ens', True, True, 'text not on the page',
    'The action-group letter ends its manuscript line, and ens starts the next line. There is no detached compound hyphen after the letter or before ens, and no full stop follows ens; the following dark stroke is a descending comma.',
    'high', 'object_set'))
changes.append(row('Object-set bracket, comma before the closing bracket',
    'ens], et pour', 'ens.], et pour', 'ens,] et pour', True, True, 'insertion or placement',
    'The comma descends to the left of the long closing bracket. After the bracket the text continues et pour without another comma. Both witnesses move this punctuation to the outside.',
    'high', 'object_set'))
changes.append(row('Quantified pair of objects, explicit universal sign',
    r'\forall\,', '[no witness]', r'\forall\,', False, True, 'omission',
    'Between pour and the first t is a separate tall U/V-shaped sign with a joining cross stroke. It is the written universal quantifier, not the thin-space comma produced by raw macro tokenization.',
    'high', 'object_set'))
changes.append(row('Quantified pair, set letter after the membership sign',
    r"t,t'\in\tau", r"t, t' \in \mathcal{T}", r"t,t'\in\unsure{\tau|\mathcal T}",
    True, True, 'misread symbol or index',
    'After the membership sign is a closed triangular flag descending into one short lower curve. It is individually consistent with the set-letter graphs above, while tau/T remains unresolved.',
    'medium', 'object_set'))
changes.append(row('Before second diagram, hom without a point',
    r'hom \uline{injectif}', r'hom.\ \uncertain{injectif}', r'hom \uline{injectif}',
    False, True, 'text not on the page',
    'The low last m stroke of hom is followed by a clear gap before injectif. No dot sits at the abbreviation boundary; the visible dots belong to the following word.',
    'high', None, True))
changes.append(row('Before second diagram, underline of injectif',
    r'\uline{injectif}', r'\uncertain{injectif}', r'\uline{injectif}', False, True, 'other',
    'The dotted i, descending j, crossed t, second dotted i and long final f are readable. A separate horizontal rule runs under the word and through the descender area; the underline is retained.',
    'high', None, True))
changes.append(row('Composition sentence, no la before composition',
    'avec composition', 'avec la composition', 'avec composition', False, True, 'text not on the page',
    'The gap after avec leads directly into the rounded opening of composition. There is no separate tall l or following a between the two words.'))
changes.append(row('Composition sentence, lower-case isom.',
    'isom.', 'Isom.', 'isom.', False, True, 'other',
    'The prose abbreviation begins with a short dotted or ticked lower-case i, unlike the tall ruled capital I of Isom in the display above. The terminal point is visible.'))
changes.append(row('Final paragraph opening, On a exprimé',
    'On a exprimé', 'Ceci exprime', 'On a exprimé', False, True, 'misread word',
    'The line begins with a tall closed O followed by n. A detached small a precedes the x and descending p of exprimé, whose final accented e is visible. It is not the continuous word Ceci.'))
changes.append(row('After angle-bracket pi, cancellation and possible final on',
    r'--- \deleted{Mais}', r'\struck{Mais on}', r'\deleted{Mais \unsure{on}}',
    True, False, 'deletion state',
    'A single horizontal strike begins before Mais, passes through its letters, and continues to the right. There is no independent dash before the deletion. After the legible Mais, a small raised remnant and a dark low return could be on, but the strike prevents a secure reading; this possible second word is localized in an unsure mark.',
    'low', 'mais_and_bracket'))
changes.append(row('Final bracket opening, se donner',
    'se donner', 'en donner', 'se donner', False, True, 'misread word',
    'After the long final stroke of faut, the short separate word has the small rising s movement and low terminal e return of se. The next manuscript line starts donner.',
    'high', 'mais_and_bracket'))
changes.append(row('Final bracket, sous groupes',
    'sous groupes', r'\ill{} groupes', 'sous groupes', False, True, 'readable ink left as \\ill{}',
    'Before groupes are a small initial s turn, low ou movement, and separate final s return. The word sous is legible, and no hyphen joins it to groupes.',
    'high', None, True))
changes.append(row('Family of subgroups, indexing set letter',
    r'(\pi_t)_{t\in\tau}', r'(\pi_t)_{t \in \mathcal{T}}',
    r'(\pi_t)_{t\in\unsure{\tau|\mathcal T}}', True, True, 'misread symbol or index',
    'In the small index after the membership sign the set letter again has a triangular top and one hooked lower return. The family index t and the lower t on pi are retained. This fourth set graph is inspected separately; the tau/T encoding remains provisional.',
    'medium', 'family_and_bitorsors'))
changes.append(row('Final bracket, abbreviation d\'ens',
    "d'ens", "d'ensembles", "d'ens", False, True, 'abbreviation expanded or spelling modernised',
    'After the apostrophe the source has only the compact ens sequence. The next separated word begins with v, so ensembles is an expansion rather than written text.',
    'high', 'family_and_bitorsors'))
changes.append(row('Final bracket, vides ou (M0705 continuation)',
    'vides ou', r'\ill{}', 'vides ou', False, True, 'readable ink left as \\ill{}',
    'Vides shows a low v, dotted i, tall looped d and connected es. The following two small separated traces are the compact o and flattened u; there is no cancellation over the words. The first H illegibility after d\'ensembles is thus recoverable.',
    'medium', 'family_and_bitorsors', True))
changes.append(row('Final bracket, bitorseurs sous',
    'bitorseurs sous', r'\ill{}', 'bitorseurs sous', False, True, 'readable ink left as \\ill{}',
    'The next line begins with a tall b, dotted i and crossed t, followed by the low orseur sequence and a separate final s. The following short word has the same flattened sous outline. These occupy the second H illegible passage before ces.',
    'high', 'family_and_bitorsors', True))
changes.append(row('Final bracket, les before the two pi groups',
    'les', 'ces', 'les', False, True, 'misread word',
    'The first letter before the pi pair rises into a tall open loop, as l in les elsewhere on this page. It is followed by connected es; it is not the short c of ces.',
    'high', 'family_and_bitorsors'))
changes.append(row('Bottom-left pencil pagination',
    r'\mspage{23}', '[no witness]', r'\mspage{23}', False, True, 'omission',
    'Two pale pencil digits at the lower-left edge read 23: an angular descending 2 and a two-lobed 3. Their hand is not identified.'))

p_open, b_open = loc('opening_attachment')
p_end, b_end = loc('family_and_bitorsors')
decisions = [
    {'id': 'M0704', 'decision': 'other', 'reading': '',
     'ink': 'No independent two-word ink follows donnons-nous. The last small strokes belong to the opening words, and the remaining large curve is the attachment call for un groupe T abélien. Candidate omits the unlocalized illegible placeholder; main is asked to review this rejection.',
     'crop': p_open, 'box': b_open, 'confidence': 'medium'},
    {'id': 'M0705', 'decision': 'first', 'reading': "d'ens vides ou",
     'ink': 'The d and apostrophe, compact ens, dotted i and tall d in vides, and two small traces of ou are visible in sequence. The abbreviation is not expanded and no extra word is supplied.',
     'crop': p_end, 'box': b_end, 'confidence': 'medium'},
]

inventory = [
    {'sheet_kind':'text', 'hand':'unknown (pencil pagination)', 'element':'E01', 'kind':'margin note', 'position':'upper-right corner', 'first_words_or_objects':'12', 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E02', 'kind':'text', 'position':'opening four manuscript lines', 'first_words_or_objects':'Inversement, donnons-nous ... un T-groupoïde ... une opération ... et un hom de groupoïdes', 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E03', 'kind':'insertion', 'position':'right of opening Lambda; broad call rises to the end of the first line', 'first_words_or_objects':'un groupe T abélien', 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E04', 'kind':'deletion', 'position':'opening second line, between T-groupoïde and Lambda', 'first_words_or_objects':'connexe (doubtful under heavy strike)', 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E05', 'kind':'diagram', 'position':'upper third, below hom de groupoïdes', 'first_words_or_objects':'Lambda -> four-line groupoïde codomain; foncteur fidèle above shaft, fidèle double-underlined; Pi and covered Pi; autom pi', 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E06', 'kind':'text', 'position':'single line beneath first diagram', 'first_words_or_objects':'compatible avec action de E/Sigma.', 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E07', 'kind':'text', 'position':'middle, line beginning Soit', 'first_words_or_objects':'Soit tau/T = Ob Lambda', 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E08', 'kind':'text', 'position':'bracket beginning after Ob Lambda and wrapping to following line', 'first_words_or_objects':'[donc tau/T est un E/Sigma ens,]', 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E09', 'kind':'text', 'position':'following line and continuation to underlined injectif', 'first_words_or_objects':"et pour forall t,t' in tau/T, on a un hom injectif", 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E10', 'kind':'diagram', 'position':'center of page beneath hom injectif', 'first_words_or_objects':"Isom_Lambda(t,t') underbraced as pi_(t,t') -> pi; left hook certain, right head uncertain", 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E11', 'kind':'text', 'position':'line below injection diagram', 'first_words_or_objects':'compatible avec composition des isom.', 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E12', 'kind':'text', 'position':'lower half, first three lines of last paragraph', 'first_words_or_objects':"On a exprimé la donnée d'un foncteur fidèle d'un groupoïde Lambda dans <pi>", 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E13', 'kind':'deletion', 'position':'after <pi>, before opening square bracket', 'first_words_or_objects':'Mais, possibly followed by on; one long cancellation stroke', 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E14', 'kind':'text', 'position':'long square-bracketed passage in last paragraph', 'first_words_or_objects':"il faut se donner une famille de sous groupes (pi_t) indexed by t in tau/T de pi et d'ens vides ou bitorseurs sous les pi_t',pi_t...", 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'his hand', 'element':'E15', 'kind':'text', 'position':'last two manuscript lines, following closing square bracket', 'first_words_or_objects':'On va maintenant introduire les op. de', 'transcribed':'yes'},
    {'sheet_kind':'text', 'hand':'unknown (pencil pagination)', 'element':'E16', 'kind':'margin note', 'position':'bottom-left corner', 'first_words_or_objects':'23', 'transcribed':'yes'},
]

remaining = [
    {'place':'Cancelled adjective after T-groupoïde', 'reading':r'\deleted{\unsure{connexe}}', 'alternatives':'connexe; a different word obscured by the cancellation', 'confidence':'low', 'reason':'Only the initial rounded trace, low humps and terminal raised remnants remain outside the thick strike.'},
    {'place':'First diagram, marks before un seul objet', 'reading':r'\unsure{à|:}', 'alternatives':'à; colon', 'confidence':'low', 'reason':'Two detached dark marks can encode an extremely compressed accented a or punctuation. The comparable à lower in the same codomain also has separated strokes.'},
    {'place':'Action-group glyph, three occurrences', 'reading':r'\unsure{\mathcal E|\Sigma}', 'alternatives':'calligraphic E; Sigma', 'confidence':'low', 'reason':'The shared alphabet uncertainty remains. All three individual graphs were inspected; their angular or rounded bowl forms do not justify harmonizing to a confident letter.'},
    {'place':'Object-set symbol, four occurrences', 'reading':r'\unsure{\tau|\mathcal T}', 'alternatives':'tau; calligraphic T', 'confidence':'medium', 'reason':'Each occurrence has a triangular or flag-like top and a single lower curved return. This differs from the provisionally recorded ornate Z and cannot be harmonized to Z from context.'},
    {'place':'Injection diagram, right terminal of hooked connector', 'reading':r'\arrow[r,hook,"\unsure{\vphantom{\to}}"]', 'alternatives':'hook-arrow with a small filled head; hooked shaft whose right tip is only a terminal blot', 'confidence':'low', 'reason':'The left hook and shaft are unambiguous, but the small dark right terminal has only a weak pointed outline. An editorial unsure question is placed above the connector; no additional source label is inferred.'},
    {'place':'Cancelled word after Mais', 'reading':r'\deleted{Mais \unsure{on}}', 'alternatives':'Mais on; Mais with only non-letter strike remnants following', 'confidence':'low', 'reason':'A short rise and low dark return after Mais could preserve on, but are largely merged with the continuous strike.'},
]

certainty = [
    {'place':'M0705 in final bracket', 'C':r"\unsure{d'ens vides ou}", 'final':"d'ens vides ou", 'ink':'The enlarged line distinguishes the compact abbreviation, vides and two very small ou traces. The original first reading is retained without the broad doubt mark; confidence is medium.'},
    {'place':'Injection connector, newly localized terminal uncertainty', 'C':r'\arrow[r,hook]', 'final':r'\arrow[r,hook,"\unsure{\vphantom{\to}}"]', 'ink':'The hook and shaft are retained. The question above the connector marks only uncertainty about the filled right terminal being an arrowhead; this is a certainty change, not a new source label.'},
]

notation = [
    {'form':r'T', 'meaning':'The abelian group specified by the opening insertion, used in T-groupoïde and (T,Lambda).', 'evidence':'Its three tall upright-and-crossbar forms are inspected in the opening lines.'},
    {'form':r'\Lambda', 'meaning':'The T-groupoid and the subscript of Isom.', 'evidence':'The inverted-V capital is repeated in the opening, first diagram, Ob definition, Isom subscript and last paragraph; no crossbar is present.'},
    {'form':r'\unsure{\mathcal E|\Sigma}', 'meaning':'The group acting on (T,Lambda), on the faithful functor data, and on the object set.', 'evidence':'Three individual glyphs have returning upper and lower strokes; shared E/Sigma identification remains open.'},
    {'form':r'\unsure{\tau|\mathcal T}', 'meaning':'The set Ob Lambda, subsequently used for t,t\' and the subgroup-family index.', 'evidence':'All four set graphs have a flag-like top and one lower return, unlike the ornate Z described in the supplied notation table.'},
    {'form':r'\Pi,\widetilde\Pi;\pi', 'meaning':'Capital Pi and its covered version in the universal-cover description; lower-case pi as the automorphism group and diagram target.', 'evidence':'The two capital forms have separated long vertical legs under a broad bar; the second has a separate tilde. Lower-case pi has a more compact arch and legs, including the final family/group subscripts.'},
    {'form':r'\pi_{t,t\prime};\pi_t,\pi_{t\prime}', 'meaning':'The Isom-set label below the underbrace and the groups in the final bracket.', 'evidence':'The underbrace and its two small indices, the family index and the prime on the first group of the final pair were inspected. The source prime is kept on t in pi_(t\').'},
    {'form':r'\langle\pi\rangle', 'meaning':'The one-object groupoid notation used in the final paragraph.', 'evidence':'Two separate angle strokes enclose pi immediately before the cancellation.'},
]

abbreviations = [
    {'form':'hom', 'expansion':'homomorphisme'},
    {'form':'rev.', 'expansion':'revêtements'},
    {'form':'autom', 'expansion':'automorphismes'},
    {'form':'Ob', 'expansion':'objets'},
    {'form':'Isom', 'expansion':'isomorphismes'},
    {'form':'isom.', 'expansion':'isomorphismes'},
    {'form':'ens', 'expansion':'ensembles'},
    {'form':'op.', 'expansion':'opérations'},
]

hand_log = [
    {'habit':'Small rounded letters and their accents can collapse to detached dots, while u/n returns become nearly horizontal.', 'places':'donnons-nous; the two marks before un seul objet; à before the covered Pi; ou after vides', 'scope':'These occurrences on this page were inspected; not asserted as a universal rule.', 'misreadings':'This contributes to the C à versus H colon difference, H illegibilities in the final bracket, and the unlocalized opening placeholder.'},
    {'habit':'The object-set letter has a triangular or flag-like head and one lower curved return.', 'places':'Soit definition, bracket before est un, membership condition, final family index', 'scope':'All four occurrences on 143_scan024 inspected; this graph is not silently equated with the ornate Z.', 'misreadings':'C tau and H calligraphic T remain explicit alternatives.'},
    {'habit':'The action-group letter varies between angular and rounded returning bowls.', 'places':'Opening opération de; compatible avec action de; object-set bracket', 'scope':'All three occurrences inspected; shared E/Sigma uncertainty retained.', 'misreadings':'C calligraphic E versus H Sigma is an unresolved alphabet choice, not a settled mathematical correction.'},
    {'habit':'Abbreviations can end with a long low letter stroke without a terminal dot.', 'places':'hom twice; autom in the codomain; ens at the bracket line break', 'scope':'Each listed abbreviation inspected; rev., isom. and op. separately retain their written dots.', 'misreadings':'H adds points after hom, autom and ens and expands rev. and d\'ens.'},
    {'habit':'A continuous cancellation can extend well before and after the deleted letters.', 'places':'Mais and possible on after angle-bracket pi', 'scope':'This single cancellation inspected in a tight crop.', 'misreadings':'C separates the left portion as an em dash; the source shows one uninterrupted strike. The possible last word remains doubtful.'},
    {'habit':'A hooked connector may end in a filled terminal blob rather than an easily separable chevron.', 'places':'Isom injection diagram', 'scope':'Both ends and the shaft of this connector inspected; uncertainty localized to its right tip.', 'misreadings':'Both witnesses give a confident hook-arrow. The candidate retains the hook and flags the head.'},
    {'habit':'The prose i can be short and ticked, whereas the display I has a tall vertical and two broad rules.', 'places':'Isom in the display; isom. in the composition sentence', 'scope':'Both occurrences inspected.', 'misreadings':'H capitalizes the prose Isom.; the source lower-case form is retained.'},
]

notes = [
    {'id':key+'-N1', 'text':'The page starts an inverse construction by asking for a T-groupoid Lambda, an action of the unresolved E/Sigma group on (T,Lambda), and a faithful functor to the stated one-object groupoid of universal covers of capital Pi equal to covered Pi. The opening insertion adds the datum of an abelian group T. A heavily cancelled qualifier after T-groupoïde is retained only as doubtful connexe. The codomain ends with the statement that its automorphisms are lower-case pi. This is an account of the written data, not a proof of the construction.'},
    {'id':key+'-N2', 'text':'The author defines the object set, whose tau/T glyph remains unresolved, as Ob Lambda and describes it as an E/Sigma set. For the explicitly quantified pair t,t\', the page writes an injective homomorphism from Isom_Lambda(t,t\') to pi, labels the Isom expression by pi_(t,t\') below an underbrace, and states compatibility with composition. Fidèle is double-underlined, injectif singly underlined. The connector has a definite left hook but an uncertain small right head.'},
    {'id':key+'-N3', 'text':'The last paragraph begins On a exprimé and restates the datum of a faithful functor Lambda into angle-bracket pi. A bracket then calls for a family of subgroups pi_t and for empty sets or bitorsors under pi_(t\') and pi_t. The leading Mais and a possible on are cancelled. The final words promise to introduce les op. de and stop there; no continuation is supplied from another page.'},
    {'id':key+'-N4', 'text':'The light pencil numbers 12 at the upper right and 23 at the lower left are both transcribed. Their hand is unknown; the use of the page-number macro records the written values and does not establish authorship of either number. No other marginal text or independent drawing is present.'},
    {'id':key+'-N5', 'text':'M0704 is removed because no independent two-word passage can be located after the completed opening words; the nearby large curve is the attachment call of the abelian-group insertion. The two marks before un seul objet remain à/colon. The object-set bracket is transcribed with its comma before the closing bracket and without a compound hyphen at the E/ens manuscript line break. No articles, abbreviation points or ellipses have been added to complete the grammar.'},
]

check_events = [
    {'statement_id':key+'-N1', 'type':'carried as background without fault found', 'outcome':'The datum and faithful-functor diagram were visually collated, including labels, capitalization, tildes, arrow direction and line order. No independent mathematical verification of the inverse construction was performed; transcription is not proof.'},
    {'statement_id':key+'-N2', 'type':'carried as background without fault found', 'outcome':'The quantified pair, Isom subscript, underbrace label and hooked connector were checked against the ink. Injectivity and compatibility are the page\'s assertions, not independently proved here. The right arrowhead remains uncertain.'},
    {'statement_id':key+'-N3', 'type':'carried as background without fault found', 'outcome':'The subgroup-family index and the words empty sets/bitorsors were read from the source and compared with both witnesses. No proof, computation or external source was used to establish the classification implicit in the bracket.'},
]

report = {
    'key':key, 'reader':'B', 'stage':'first', 'image_views':['original','half1','half2'],
    'changes':changes, 'decisions':decisions, 'inventory':inventory,
    'remaining_doubts':remaining, 'certainty_resolutions':certainty,
    'notation':notation, 'abbreviations':abbreviations, 'hand_log':hand_log,
    'notes':notes, 'check_events':check_events,
    'unresolved_for_main':[
        'Review rejection of M0704 in crops/143_scan024_readerB_opening_attachment.png, box [700,90,1662,421]; no extra two-word ink was located.',
        'Retain or adjudicate the heavily cancelled connexe in crops/143_scan024_readerB_cancelled_adjective.png, box [590,224,859,289].',
        'Adjudicate à versus colon before un seul objet in crops/143_scan024_readerB_codomain_and_action.png, box [883,553,1658,927].',
        'Review the comma inside the object-set bracket and absent E/ens compound hyphen in crops/143_scan024_readerB_object_set.png, box [282,930,1585,1167].',
        'Keep tau/T open unless cross-page ink comparison settles this flag-like graph; it is not the ornate Z graph. All four occurrences are covered by object_set and family_and_bitorsors crops.',
        'Retain shared E/Sigma uncertainty at low confidence, non-consequential; all three occurrences were inspected in opening_attachment, codomain_and_action and object_set.',
        'Adjudicate the filled terminal of the Isom hook-arrow in crops/143_scan024_readerB_injection.png, box [571,1274,1254,1460]. Candidate uses an editorial unsure question above this connector only.',
        'Adjudicate possible on after cancelled Mais in crops/143_scan024_readerB_mais_and_bracket.png, box [517,1740,1470,1878]; do not restore C\'s separate em dash.',
    ],
    'raw_difference_disposition':'All packet C/H differences and every visible text, mathematical sign, index, underline, cancellation, insertion, diagram and pagination element were inspected. Literal C/H excerpts were checked programmatically against this packet, and final excerpts against the candidate. Alphabet choices are included as requested; E/Sigma-only rows are low confidence and non-consequential, and tau/T encoding rows are medium and non-consequential. Mark decisions use only original IDs M0704 and M0705; new doubts are confined to remaining_doubts. Pure macro syntax, H editorial page-note wording, and raw commas produced by spacing macros are excluded from material rows. The original and each native half were actually viewed once; an earlier truncated original-image emission was not counted as inspection. Seven distinct open-locus crops were each viewed once. No OCR, web research or TeX compilation was used.'
}

assert [d['id'] for d in decisions] == [d['id'] for d in pkt['marks']]
assert len({e['element'] for e in inventory}) == len(inventory)
for change in changes:
    assert change['kind'] in {'misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
for change in changes:
    if 'action-group alphabet' in change['place']:
        assert change['confidence'] == 'low' and not change['consequential']

tex_path = root / 'reviews' / f'{key}_readerB.tex'
json_path = root / 'reviews' / f'{key}_readerB.json'
tex_path.write_text(candidate)
json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(f'Candidate: {tex_path}')
print(f'Report: {json_path}')
print(f'{len(changes)} changes; {len(decisions)} original MARKS decisions; {len(inventory)} inventory entries; {len(boxes)} crops; {len(remaining)} remaining doubts.')
