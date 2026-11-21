"""First-reading metadata for scan123. Ink observations only; no OCR or proof check."""
import csv
import importlib.util
import json
from pathlib import Path

ROOT = Path('/workspace/scratch/0cab6a548abb')
HERE = ROOT / 'edition/review'
PAGE = '149_scan123'
spec = importlib.util.spec_from_file_location('scan123_crops', HERE / f'{PAGE}_crop.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
CROPS = module.CROPS

def change(place_id, place, C, H, final, evidence, confidence, vs_C, kind,
           category, H_marked=False, consequential=False, crop=None):
    crop = crop or place_id
    return {'id': place_id, 'place': place, 'C': C, 'H': H, 'final': final,
            'evidence': evidence, 'crop': f'crops/{PAGE}_{crop}.png',
            'bbox': CROPS[crop], 'confidence': confidence, 'vs_C': vs_C,
            'vs_H': True, 'kind': kind, 'error_category': category,
            'H_marked': H_marked, 'consequential': consequential}

changes = [
    change('p01', 'Main lines1–2: opening continuation and f,g phrase',
           r'en ces paramètres, et en se ramenant à un $f,g$ premiers entre eux,',
           r'un \uncertain{sys.} de paramètres, et on se ramène au cas où $f$, $g$ premiers entre eux, —',
           r'en ces paramètres, et en se ramenant à un $f,g$ premiers entre eux,',
           'The first two low words read en ces, followed directly by paramètres and a comma; no sys. de phrase is visible. After et is en se ramenant, whose final t has a tall triangular return. The next line begins à un, not au cas où. The two mathematical letters f,g and their comma are written, followed by premiers entre eux and a low comma; there is no following dash before the next line begins on.',
           'high', False, 'misread word', 'Words', True),
    change('p02', 'Main line3: on est and the first dash',
           r'\unsure{on est|on voit} --- faisant encore éclater',
           r'on peut — faisant encore éclater',
           r'on est --- faisant encore éclater',
           'After the small on, the next word starts with a low e-loop, continues with a low s-like connection and ends in a tall t return. It lacks the separate o/i strokes of voit and the p descender of peut. A separate horizontal dash precedes faisant encore éclater. On est is retained literally despite the awkward following que construction. This resolves C to its first reading and does not count as a correction against C.',
           'medium', False, 'misread word', 'Words'),
    change('p03', 'Main line4: isolated a, dash and diviseurs phrase',
           r'$a$ --- que les diviseurs de $f,g$',
           r'— \uncertain{supposer} que les diviseurs de $f$, $g$',
           r'$a$ --- que les diviseurs de $f,g$',
           'A small a-shaped loop and exit stroke stand alone at the left of the line, followed by a separate short dash. Que les diviseurs de f,g follows. There are no letters for supposer between the dash and que; the mathematical a must not be omitted.',
           'high', False, 'omission', 'Omissions', True, True),
    change('p04', 'Main line5: crossed word, live séparent and three dots',
           r'\deleted{\unsure{sont|se}} \unsure{séparent}\ldots',
           r'\struck{\ill{}} \uncertain{se séparent}…',
           r'\deleted{\unsure{sont|se}} séparent\ldots',
           'The left word is crossed by an independent horizontal line. Its tall initial loop and small following strokes remain insufficient to distinguish sont from se. The live word has s/é, a detached accent, a long p descender and an arent ending with the tall t return; it reads séparent. Three distinct dots follow. There is no additional live se before it. The descending stroke from que above belongs to that q, not to a new letter or cancellation. Resolving séparent to C’s first reading changes certainty only.',
           'medium', False, 'deletion state', 'Struck text', True),
    change('p05', 'Main line6: b) heading, val contraction and crossed qui',
           r'b) Un anneau de val $V$ \deleted{qui}',
           r'b) Un anneau de val.\ $V$ \struck{qui}',
           r'b) Un anneau de val $V$ \deleted{qui}',
           'The contraction val is followed by a wide blank before the large V, with no separate full stop. The crossed qui remains readable from its q loop/descender, u and dotted i. The written b) is retained as the item label.',
           'high', False, 'abbreviation expanded or spelling modernised',
           'Abbreviations expanded, spelling modernised'),
    change('p06', 'Main line8: raised x after bien déterminé',
           r'pt bien déterminé de chaque $X$,',
           r'p\supplied{oin}t bien déterminé \add{$x$} de chaque $X$,',
           r'pt bien déterminé \inserted{$x$} de chaque $X$,',
           'Two small intersecting oblique strokes form a separate raised x in the gap between déterminé and de chaque X. Its placement supplies the point name after déterminé, not an index on the following X. It is not merely a detached single accent. The baseline abbreviation is pt, without the supplied oin letters. The later large X is followed by a comma.',
           'high', True, 'omission', 'Omissions', consequential=True),
    change('p08', 'Main lines10–11: local ring and equality explanation',
           r'domine $\underline{O}_{\mathfrak X,x}$, donc lui est égal puisque ce dernier est un anneau',
           r'domine $\underline{O}_{\mathfrak{X},x}$, donc lui est égal puisque \ill{} \uncertain{dominant} \ill{} \uncertain{est un} \ill{}',
           r'domine $\underline{O}_{\mathfrak X,x}$, donc lui est égal puisque ce dernier est un anneau',
           'The underlined open O-like bowl has the written fraktur X,x index. The following words are donc lui est égal. The next baseline reads puisque ce dernier est un anneau: ce is a small connected curve, dernier has the initial d and its following rn/ier sequence, and anneau is visible at the right. No dominant occurs in that position. The contextual repair p16 restores the ascenders of lui/égal clipped in p08; it was made only to provide a complete target, not to repeat a settled reading.',
           'high', False, r'readable ink left as \ill{}',
           'Readable ink left as illegible', True, True, crop='p16'),
    change('p09', 'NB first main line and raised model qualification',
           r'\uline{NB} Tout \inserted{modèle $U$ de $L/K$ définit un} \uline{ouvert} de $\mathfrak X$ \deleted{\unsure{correspondant}}',
           r'\textbf{NB} Tout \add{\uncertain{modèle} $U$ de $L/K$ \uncertain{définit un}} ouvert\supplied{s} de $\mathfrak{X}$ \struck{correspondant}',
           r"\uline{NB} Tout \inserted{modèle $U$ de $\unsure{L|L'}/K$ définit un} \uline{ouvert} de $\mathfrak X$ \deleted{\unsure{correspondant}}",
           'The raised text reads modèle U de L/K définit un and its long leader curves down between Tout and ouvert. A tiny dark mark above/right of L could be a prime or a nib/entry trace; L remains first and the narrow L/L-prime uncertainty is documented without inferring a new field. The word ouvert is separately underlined; the terminal return of t does not supply an additional s. NB has its own underline. The crossed correspondant has several recognizable lower strokes but not every letter is secure, so its doubt remains. The new L uncertainty alone is not counted against C.',
           'medium', False, 'text not on the page', 'Text that is not on the page', True),
    change('p10', 'NB second main line: crossed évidemment and raised replacement',
           r'\deleted{\unsure{évidemment}} \inserted{(en le plongeant} dans un modèle propre $X$,',
           r'(\struck{\ill{}} \uncertain{plonge} dans un modèle propre $X$,',
           r'\deleted{\unsure{évidemment}} \inserted{(en le plongeant} dans un modèle propre $X$,',
           'A lower word is crossed horizontally; its e/v/i/d and following compressed strokes support évidemment tentatively, but the cancellation prevents letter-by-letter certainty. Above it, a genuine opening parenthesis and en le plongeant are visible, including the final ant. The p/g descenders in the live insertion overlap the old crossed line and are not evidence that the replacement itself is deleted. The marked insertion is confined to this raised prefix over the cancelled word: dans un modèle propre X continues to its right on the ordinary slanting main baseline, and c’est clair) occupies the next main baseline. No separate leader encloses those following words as a raised addition. This is a record of visible placement, not a claim to reconstruct the full writing chronology. The opening parenthesis is a separate curve, not the long leader from the earlier model insertion. The supplied packet C likewise marks only the prefix (en le plongeant as inserted.',
           'medium', False, 'insertion or placement',
           'Insertions put in the wrong place', True),
    change('p11', 'NB third and fourth main lines: repeated et and corres-/pondent',
           r"c'est clair) et \deleted{et} les modèles correspondent à \uline{certains} ouverts de $\mathfrak X$",
           r"c'est clair) et \struck{et} les modèles \uncertain{conven}- \ill{} à \emph{certains} ouverts de $\mathfrak{X}$",
           r"c'est clair) et \deleted{et} les modèles corres-\\ pondent à \uline{certains} ouverts de $\mathfrak X$",
           'The first et is live; the following et has an independent cancellation stroke. After les modèles the line ends with corres and a short horizontal hyphen; the next line begins pondent. These are readable letters, not conven plus an unreadable continuation. The candidate retains the written corres-/pondent break rather than silently dropping the actual hyphen. Certains has a distinct underline; ouverts ends with a separate s-like curve. The departure counted against C here is the preserved written hyphen/break, not a different reading of the word’s letters.',
           'high', True, 'other', 'Other', True),
    change('p12', 'NB last parenthesis: pas stables/stable par réunion finie',
           r'(\uline{pas} stables par réunion finie).',
           r'(pas stable par réunion finie).',
           r'(\uline{pas} \unsure{stables|stable} par réunion finie).',
           'Pas has a separate short underline. The next word has the st/ab/l outline and a compressed final return; no independent final s is secure enough to exclude stable, so stables|stable remains in place. Par réunion finie, the closing parenthesis and following full stop are clear. Repair crop p17 includes the full tall f ascender of finie that p12 clipped; it adds complete context without a new substantive decision. C’s preferred stables remains first, so the new doubt is not counted against C.',
           'medium', False, 'misread word', 'Words', crop='p17'),
    change('p13', 'Last paragraph first line: loc/norm contractions and first O',
           r'Pour tt anneau \unsure{loc\textsuperscript{l}|local} \inserted{\unsure{norm\textsuperscript{l}|normal}} $O\subset L$ de',
           r'Pour tt anneau local \add{\uncertain{normal}} $\underline{O} \subset L$ de',
           r'Pour tt anneau loc\textsuperscript{l} \inserted{norm\textsuperscript{l}} $O\subset L$ de',
           'Loc is followed by a separate small elevated l-like hook; the intervening a of expanded local is not written. The raised addition likewise has norm and a small final l, not a full al ending. Its curved leader attaches after the contraction and before O; the curve is not an opening parenthesis. The first O has no independent underline, unlike the O in the following Spec expression. The inclusion sign is a single left-opening curve without an equality bar. The tt contraction remains unexpanded. Resolving both contractions to C’s first forms does not count against C.',
           'medium', False, 'abbreviation expanded or spelling modernised',
           'Abbreviations expanded, spelling modernised', True),
    change('p14', 'Final line: Spec expression, point name and cut word',
           r'$\operatorname{Spec}\underline{O}=S$, son pt fermé $\unsure{x|s}$, le \unsure{normali-}',
           r'$\operatorname{Spec} \underline{O} = S$, son p\supplied{oin}t fermé $s$, \uncertain{le normalisé}-',
           r'$\operatorname{Spec}\underline{O}=S$, son pt fermé $\unsure{x|s}$, le normali-',
           'Spec is followed by an O with a separate short underline, two equality strokes and S. The written short form is pt. The small point letter after fermé has a bent cross/return that still permits x or s; it is not resolved from the mathematical role. The last visible word ends normali with a tall l, a dotted i and a separate terminal hyphen at the right paper edge. There is no additional sé sequence. Resolving C’s preferred normali- does not count against C.',
           'medium', False, 'misread word', 'Words', True),
    change('p15', 'Extreme lower-left foliation',
           r'\margin{122}', '[absent]', r'\margin{122}',
           'The thin writing contains a first1 with its rising entry and upright, then two2 forms with rounded upper turns, diagonals and low feet. The number is separate from the author’s61 above and is retained in the lower margin.',
           'high', False, 'omission', 'Omissions'),
]

def decision(mark_id, outcome, reading, evidence, crop, confidence):
    return {'id': mark_id, 'cote': '149', 'scan': '123', 'decision': outcome,
            'reading': reading, 'evidence': evidence,
            'crop': f'crops/{PAGE}_{crop}.png', 'bbox': CROPS[crop],
            'confidence': confidence}

decisions = [
    decision('M0129', 'first', 'on est',
             'The second word has a low e-loop and s connection before the tall final t return, without a p descender or a separate o/i sequence. The awkward syntax is not corrected.', 'p02', 'medium'),
    decision('M0130', 'first', 'séparent',
             'The detached accent, p descender and arent ending are visible in the single live word after the cancelled word.', 'p04', 'high'),
    decision('M0131', 'first', r'loc\textsuperscript{l}',
             'Loc and a separate small elevated final l-like hook are written; the a of expanded local is absent.', 'p13', 'medium'),
    decision('M0132', 'first', r'\inserted{norm\textsuperscript{l}}',
             'The raised addition consists of norm with a small terminal l-like hook. No full al ending is written, and the curved line beneath is its attachment leader.', 'p13', 'medium'),
    decision('M0133', 'undecided', r'\unsure{x|s}',
             'The small bent/cross-shaped point letter after fermé does not securely distinguish x from s. No choice is inferred from the object’s role.', 'p14', 'low'),
    decision('M0134', 'first', 'normali-',
             'The right-edge prefix has a tall l, a dotted i and a separate hyphen; no written sé extension appears before the edge.', 'p14', 'high'),
]

def element(n, kind, position, words, hand='his hand'):
    return {'sheet_kind': 'text', 'hand': hand, 'element': f'e{n:02d}',
            'kind': kind, 'position': position,
            'first_words_or_objects': words, 'transcribed': 'yes'}

inventory = [
    element(1, 'margin note', 'Top centre', '61'),
    element(2, 'text', 'Opening five main lines', 'en ces paramètres ... séparent...'),
    element(3, 'deletion', 'Beginning of main line5', r'\unsure{sont|se}'),
    element(4, 'text', 'Seven-line paragraph beginning with item b)', 'b) Un anneau de val V ... de valuation.'),
    element(5, 'deletion', 'End of main line6 after V', 'qui'),
    element(6, 'insertion', 'Raised between déterminé and de chaque X, main line8', r'$x$'),
    element(7, 'text', 'Main line9 inline formula', r'x\in\mathfrak X=\varprojlim X'),
    element(8, 'text', 'Main line10 indexed local ring, with underline', r'\underline O_{\mathfrak X,x}'),
    element(9, 'text', 'Five main lines of the NB paragraph', 'NB Tout ouvert ... par réunion finie).'),
    element(10, 'text', 'NB heading and first-line underlined word', r'\uline{NB};\ \uline{ouvert}'),
    element(11, 'insertion', 'Above first NB line, leader after Tout', r"modèle U de \unsure{L|L'}/K définit un"),
    element(12, 'deletion', 'After fraktur X in first NB line', r'\unsure{correspondant}'),
    element(13, 'deletion', 'Beginning of the next NB line, below the replacement', r'\unsure{évidemment}'),
    element(14, 'insertion', 'Above the crossed évidemment', '(en le plongeant'),
    element(15, 'deletion', 'Second et after c’est clair)', 'et'),
    element(16, 'text', 'Across the third/fourth NB lines', r'corres-\\ pondent à \uline{certains} ouverts de \mathfrak X'),
    element(17, 'text', 'Final NB parenthesis', r'(\uline{pas} \unsure{stables|stable} par réunion finie).'),
    element(18, 'text', 'Last three main lines', r'Pour tt anneau loc\textsuperscript{l} ... le normali-'),
    element(19, 'insertion', 'Raised before the first O, with curved leader', r'norm\textsuperscript{l}'),
    element(20, 'text', 'Last-line Spec formula, point label and cut word', r'\operatorname{Spec}\underline O=S;\ \unsure{x|s};\ normali-'),
    element(21, 'margin note', 'Extreme lower-left corner', '122', 'thin foliation hand'),
]

doubts = [
    {'place': 'Opening paragraph, crossed word before séparent',
     'reading': r'\deleted{\unsure{sont|se}}',
     'alternatives': 'The strike merges the small middle/final strokes; neither sont nor se is fully secure.', 'confidence': 'low'},
    {'place': 'NB raised model phrase, L of L/K',
     'reading': r"\unsure{L|L'}/K",
     'alternatives': 'The tiny upper-right mark may be a prime or a nib/entry trace; the base L reading remains first.', 'confidence': 'low'},
    {'place': 'NB first crossed word',
     'reading': r'\deleted{\unsure{correspondant}}',
     'alternatives': 'Several cursive letters survive, but the crossing line prevents a secure reading of every letter.', 'confidence': 'medium'},
    {'place': 'NB lower crossed word beneath the replacement',
     'reading': r'\deleted{\unsure{évidemment}}',
     'alternatives': 'Tentative évidemment; the replacement’s descenders and strike obscure individual middle/final letters and the accent.', 'confidence': 'low'},
    {'place': 'NB final parenthesis',
     'reading': r'\unsure{stables|stable}',
     'alternatives': 'No independent final s is sufficiently distinct from the compressed terminal return.', 'confidence': 'medium'},
    {'place': 'Last line after pt fermé',
     'reading': r'\unsure{x|s}',
     'alternatives': 'x and s remain compatible with the small bent/cross-shaped glyph.', 'confidence': 'low'},
]

tex = (HERE / f'{PAGE}.tex').read_text()
upper, lower = tex.split('de valuation.', 1)
upper_reading = upper.replace('\\scanpage{123}\n', '', 1).strip()
lower_reading = ('de valuation.' + lower).replace('\\margin{122}', '').strip()
audit_boxes = [
    {'box': 'b01', 'kind': 'insertion; deletion; handwritten number; doubtful formula; C/H word difference; less-than-high C departure',
     'bbox': [290, 40, 1681, 1318], 'reading': upper_reading},
    {'box': 'b02', 'kind': 'insertion; deletion; doubtful formula; C/H word difference; less-than-high C departure',
     'bbox': [290, 1325, 1681, 2339], 'reading': lower_reading},
    {'box': 'b03', 'kind': 'margin note; handwritten number; C/H word difference',
     'bbox': CROPS['p15'], 'reading': r'\margin{122}'},
]

data = {
    'page': PAGE, 'scan': 123, 'reader': 'reader_b',
    'line_count': 26,
    'line_count_detail': {'main': 20, 'diagram': 0, 'margin': 0, 'insertion': 4, 'standalone_numbers': 2},
    'changes': changes, 'decisions': decisions, 'inventory': inventory,
    'doubts': doubts, 'audit_boxes': audit_boxes,
    'notes': [
        'The opening continues a discussion of two written parameters/functions f,g and successive blow-ups. The literal on est ... que construction is retained even though its syntax is awkward; neither on voit nor on peut/supposer is supplied.',
        'Paragraph b) describes a valuation ring dominating a specified point of each model, the written inverse-limit point x, and an indexed local ring that the source says equals V. This is a description of the source text, not an independently verified construction or proof.',
        'The raised x after déterminé is genuine ink in the gap before de chaque X and is restored where C omitted it. The point label is not inferred only from the later formula.',
        'The NB paragraph has two separate replacements: modèle U de L/K définit un is attached after Tout by a long leader; (en le plongeant stands over the crossed lower word. The first insertion’s leader is distinct from the genuine opening parenthesis of the second. Only that raised prefix is marked inserted: dans un modèle propre X continues along the main slanting baseline and c’est clair) is on the next main line, without a separate enclosing insertion leader. This preserves visible placement without asserting the chronology of the whole parenthesis. The supplied packet C has the same narrow insertion extent. Crossed correspondant and évidemment retain their uncertainties.',
        'The tiny mark above/right of the insertion’s L is left as L|L-prime. No field distinction is inferred. The final s of stables likewise remains open; both are new doubts without changed base C readings.',
        'The written corres-/pondent break is retained explicitly in the candidate and audit reading. The vs_C flag at p11 records the restored ink hyphen/break, not changed letters in correspondant/correspondent.',
        'The first O in O subset L has no underline; the O in the later Spec expression has a separate short underline. The curved stroke before the first O is the norm-contraction’s leader, not punctuation or an underline.',
        'The final normali- is only the written prefix ending at the right paper edge. Nothing from another page is used to complete it. The loc and norm contractions retain their small final l forms, and pt, val and tt remain unexpanded.',
        'Twenty main baselines were counted: opening5, item b)7, NB5 and final paragraph3. Four independent raised additions are x, the model phrase, (en le plongeant and norm-l. The author’s61 and thin folio122 each count as a separate numbering line. Item b) is already on a counted main line.',
        'The full page and each native half were inspected once. Crops p01–p15 were each inspected. Two declared contextual repairs were then made and inspected: p16 replaces the clipped ascender context of p08’s target, and p17 supplies the full f ascender in p12’s target. The original crops were not overwritten and no other decided place was recropped.',
        'The broad audit regions contain complete actual text rather than English summaries. The lower region includes the whole overlapping NB paragraph and the final paragraph; the upper region includes the complete opening and the item-b text through un anneau. The lower region begins with the actual next words de valuation. and extends through the final cut word. Folio122 has its own isolated box.',
        'Only this assigned packet, the common reading rules/protocol, the supplied current notation table and this reader’s own files were used. No OCR, external source, other-page witness, TeX compilation or independent mathematical proof check was performed.',
        'Static checks validate exact supplied mark ids, unique change ids, existing crop references, bounded original-image coordinates, balanced candidate braces and the line-count sum.',
    ],
    'checks': [],
    'hand_observations': [
        {'habit': 'Final t often returns as a tall triangular bend rather than a separate upright cross.',
         'places': 'ramenant; est; faisant; séparent; ouvert; pondent',
         'holds': 'These local endings share the raised return; it must not automatically become an extra s.',
         'witness_errors': 'H misread on est and supplied plural s after ouvert.'},
        {'habit': 'A tiny raised point-name x can be missed among accents and compressed endings.',
         'places': 'After bien déterminé in item b)',
         'holds': 'Two intersecting strokes and its position in the following gap distinguish this local x.',
         'witness_errors': 'C omitted the raised x; H retained it.'},
        {'habit': 'Small final l contractions are elevated or hooked and can resemble a question-like stroke.',
         'places': 'loc-l; raised norm-l',
         'holds': 'Neither local contraction has the full written al ending.',
         'witness_errors': 'H expanded local and normal; C left both as choices.'},
        {'habit': 'Insertion leaders and new-letter descenders overlap old cancelled text.',
         'places': 'NB model phrase; (en le plongeant above évidemment; norm-l before O',
         'holds': 'Leaders and strike extent were traced separately. The live replacement is retained despite its descenders crossing the old line.',
         'witness_errors': 'H lost en le and the ant ending and moved/obscured the earlier crossed word.'},
        {'habit': 'An O-like symbol may be open at the top, with an underline only when separately drawn.',
         'places': 'Indexed local ring in item b); first O subset L; final Spec O',
         'holds': 'The indexed local ring and Spec O have independent lower strokes; the first O of the last paragraph does not.',
         'witness_errors': 'H underlined the first O as well.'},
        {'habit': 'Small terminal returns can leave number or case undecidable without an independent stroke.',
         'places': 'stables/stable; tiny mark on the raised L; final x/s',
         'holds': 'All three remain local doubts; agreement with a grammatical or mathematical expectation does not resolve them.',
         'witness_errors': 'C and H differ on the terminal s and point name; both omit a doubt on the small L mark.'},
    ],
    'notation': [
        {'written': 'f,g; a', 'meaning_or_use': 'Literal mathematical letters in the opening continuation; no replacement by expected symbols.', 'places': 'Main lines2–4'},
        {'written': r'x\in\mathfrak X=\varprojlim X', 'meaning_or_use': 'Written inverse-limit point and space; the arrow beneath lim points left.', 'places': 'Main line9'},
        {'written': r'\underline O_{\mathfrak X,x}', 'meaning_or_use': 'Indexed local ring stated in the manuscript to be dominated by and then equal to V.', 'places': 'Main line10'},
        {'written': r"U\text{ de }\unsure{L|L'}/K", 'meaning_or_use': 'Model notation in the raised NB addition, with the small possible prime unresolved.', 'places': 'Raised text above the first NB line'},
        {'written': r'O\subset L;\ \operatorname{Spec}\underline O=S', 'meaning_or_use': 'The first O is un-underlined and the second is underlined, as written.', 'places': 'Last paragraph first and final main lines'},
        {'written': r'\unsure{x|s}', 'meaning_or_use': 'Unresolved name of the closed point in the final line.', 'places': 'After son pt fermé'},
    ],
    'abbreviations': [
        {'written': 'val', 'expansion': 'valuation'},
        {'written': 'pt', 'expansion': 'point'},
        {'written': 'NB', 'expansion': 'nota bene'},
        {'written': 'tt', 'expansion': 'tout'},
        {'written': r'loc\textsuperscript{l}', 'expansion': 'local'},
        {'written': r'norm\textsuperscript{l}', 'expansion': 'normal'},
    ],
    'inspection': {'whole': True, 'halves': ['top', 'bottom'],
                   'crops': [f'crops/{PAGE}_{p}.png' for p in CROPS],
                   'deletions_insertions_checked': True,
                   'contextual_repairs': [
                       {'original': f'crops/{PAGE}_p08.png', 'repair': f'crops/{PAGE}_p16.png', 'reason': 'Complete lui/égal ascenders in the intended two-line target'},
                       {'original': f'crops/{PAGE}_p12.png', 'repair': f'crops/{PAGE}_p17.png', 'reason': 'Complete tall f ascender in finie within the intended whole parenthesis'},
                   ]},
}

if __name__ == '__main__':
    with (ROOT / 'packets/149_scan123/marks.tsv').open(newline='') as stream:
        supplied = {row['id'] for row in csv.DictReader(stream, delimiter='\t')}
    assert supplied == {d['id'] for d in decisions}
    assert len({c['id'] for c in changes}) == len(changes)
    assert sum(data['line_count_detail'].values()) == data['line_count']
    for item in changes + decisions:
        assert (ROOT / 'edition' / item['crop']).is_file()
    for item in changes + decisions + audit_boxes:
        x0, y0, x1, y1 = item['bbox']
        assert 0 <= x0 < x1 <= 1681 and 0 <= y0 < y1 <= 2364
    depth = 0
    for pos, char in enumerate(tex):
        if char not in '{}':
            continue
        preceding = 0
        cursor = pos - 1
        while cursor >= 0 and tex[cursor] == '\\':
            preceding += 1
            cursor -= 1
        if preceding % 2:
            continue
        depth += 1 if char == '{' else -1
        assert depth >= 0
    assert depth == 0
    target = HERE / f'{PAGE}.json'
    if target.exists():
        raise FileExistsError(f'Refusing to overwrite frozen metadata: {target}')
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(f'{PAGE}: {len(changes)} change places ({sum(c["vs_C"] for c in changes)} vs C), '
          f'{len(CROPS)} inspected crops including2 declared context repairs, '
          f'{len(doubts)} doubts, {len(decisions)} supplied-mark decisions, '
          f'{len(audit_boxes)} audit boxes; line_count={data["line_count"]}.')
