"""Page128 first reading, based only on its assigned packet and inspected crops."""
from pathlib import Path
import csv
import importlib.util
import json

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan128'
spec = importlib.util.spec_from_file_location('crop128', ROOT / f'edition/review/{PAGE}_crop.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
CROPS = module.CROPS

def change(id, crop, place, C, H, final, evidence, confidence='high',
           vs_C=False, vs_H=True, kind='misread word', error_category='Words',
           H_marked=False, consequential=False):
    return dict(id=id, place=place, C=C, H=H, final=final, evidence=evidence,
                crop=f'crops/{PAGE}_{crop}.png', bbox=CROPS[crop]['bbox'],
                confidence=confidence, vs_C=vs_C, vs_H=vs_H, kind=kind,
                error_category=error_category, H_marked=H_marked,
                consequential=consequential)

changes = [
    change('p01', 'p01', 'Main lines3–4 and raised b)',
           r'deuxième partie \inserted{b)}', r'dernière \add{b)}, partie',
           r'deuxi\unsure{è|e}me partie \inserted{b)}',
           'The word has a d/e/u run followed by a crossed x and the i/eme ending, supporting deuxième rather than dernière. A short upper stroke beside the i cannot be securely separated as the accent over the following e; only that accent is left doubtful. The raised b has its own closing parenthesis. A separate curved leader ends between partie and de, placing b) after partie. There is no independent comma after b). The new accent doubt alone is not counted as a textual correction against C.',
           confidence='medium'),
    change('p02', 'p02', 'Main line6, complete first E expression',
           r'\mathcal E_L^{\bar L}\mathrel{\text{---}}\mathcal E_U^{\bar L}',
           r'\mathcal{E}_L^{\overline{L}} \to \mathcal{E}_U^{\overline{L}}',
           r'\mathcal E_L^{\bar L}\mathrel{\text{---}}\mathcal E_U^{\bar L}',
           'Both E terms, lower L/U and upper barred L forms are visible. Between them is one short almost horizontal stroke. Its left end is plain; its right end thickens with a minute downward terminal, but no separate two-arm arrowhead is visible. The written shaft is retained as C’s dash; a map may be intended by the prose, but no head is supplied from that interpretation.',
           kind='misread symbol or index', error_category='Symbols and indices'),
    change('p04a', 'p04', 'Main lines8–9, placement of raised Delta_V',
           r'étudier le sous-groupe \inserted{$\Delta_V$} de',
           r'étudier le \add{$\Delta_V$,} sous-groupe de',
           r'étudier le sous-groupe \inserted{$\Delta_V$} de',
           'The raised triangular Delta has a complete lower bar and a separate lower V. Its long continuous leader descends to the gap after sous-groupe and before de. No comma is written with the inserted label. The leader is not an opening parenthesis.',
           kind='insertion or placement', error_category='Insertions put in the wrong place'),
    change('p04b', 'p04', 'Main line9, image de I_V',
           r'I_V', r'\overline{I}_V', r'I_V',
           'The I has a long upper horizontal, a central upright and a shorter lower foot. There is only one upper horizontal, serving as the top of I, not a further overbar above a complete I. The lower V is separate and the following dash remains. The uppercase I in the later i∈I insertion supplies a local comparison for the two-bar form.',
           kind='misread symbol or index', error_category='Symbols and indices', consequential=True),
    change('p05a', 'p05', 'Main line10, immediately after qui,',
           'on le devine', r'en le \uncertain{devine}', 'on le devine',
           'The first short word has a compact o-like dot/curve followed by the low n stroke. Devine has its initial d loop, following e/v trace, dotted i and terminal n/e strokes. There is no initial e loop supporting en.', H_marked=True),
    change('p05b', 'p05', 'Main line10, after the comma following devine',
           'jouera un rôle analogue',
           r'\uncertain{donne} une \uncertain{réalisation} algébrique \uncertain{de} \ill{}',
           'jouera un rôle analogue',
           'The first word begins with a long descending j and has the o/u/e/r/a run. The following word is the short un. Rôle has a circumflex, a tall l and low final e; analogue has its a/n/a trace, tall l, descending g and final u/e strokes. The complete two-line clause reaches the paper’s right edge in p05. H’s longer wording and residual illegibility have no corresponding words here.',
           H_marked=True),
    change('p05c', 'p05', 'Main line11, compound after à un',
           'groupe-bout', 'groupe-lacet', 'groupe-bout',
           'After groupe and a separate short hyphen, the second element has a tall b with low turn, the short o/u trace and a tall terminal t. The lacet sequence is not present.'),
    change('p06a', 'p06', 'Main line12, after the isolated V',
           'distinctes', 'distincts', 'distinctes',
           'After the second tall t, a small low e trace leads into a separate final s-shaped hook. The written feminine ending -tes is retained even though the grammatical gender might invite a repair.'),
    change('p06b', 'p06', 'Main line12, first word of definissent-elles',
           'définissent-elles', 'définissent-elles', 'definissent-elles',
           'The initial d and following low e are followed by a tall f. The available space above that first e is blank: there is no detached accent. The later i dot is farther to the right and is not reassigned. The literal unaccented word is retained against both witnesses.',
           vs_C=True, kind='abbreviation expanded or spelling modernised',
           error_category='Abbreviations expanded, spelling modernised'),
    change('p08a', 'p08', 'Main line17, raised D_i (i∈I) and attachment',
           r'diviseurs réguliers \inserted{$D_i$ $(i\in I)$}',
           r'comp.\ irréd.\ \add{$D_i$ ($i \in I$)}',
           r'diviseurs réguliers \inserted{$D_i$ $(i\in I)$}',
           'D_i and the parenthesized i∈I are on a single rising inserted baseline. Their continuous curved leader reaches the end of réguliers, not comp. irréd. on the preceding main line. The independent comma is treated separately in p08b. The separate D= insertion above the first X-U attaches after de.',
           kind='insertion or placement', error_category='Insertions put in the wrong place'),
    change('p08b', 'p08', 'Main line17, comma beside the insertion leader after réguliers',
           '[absent]', ',', ',',
           'A distinct dark curved comma sits below the final s of réguliers, beside rather than on the long insertion leader. The leader attaches at the end of réguliers before this delimiter, so the comma is rendered after the inserted D_i (i∈I) clause and before et.',
           vs_C=True, vs_H=False, kind='omission', error_category='Omissions'),
    change('p08c', 'p08', 'Main line16, first X-U after inserted D=',
           r'X-U', r'X \setminus U', r'X-U',
           'The two capital letters are separated by a short slanted dash, much shorter than their strokes, not a full-height set-minus slash. The written minus form is retained. D= is separately raised immediately before it.',
           kind='misread symbol or index', error_category='Symbols and indices'),
    change('p08d', 'p08', 'Main line17, second X-U before à croisements',
           r'X-U', r'X \setminus U', r'X-U',
           'Here again a short dash sits between X and U. Its size and placement match a minus separator rather than a full set-minus stroke; the source form is retained without changing its intended set-difference meaning.',
           kind='misread symbol or index', error_category='Symbols and indices'),
    change('p09a', 'p09', 'Raised parenthesis above hensélisé, M0161',
           r'\inserted{(\unsure{pas|non} strict)}',
           r'\add{(\uncertain{ou strict})}', r'\inserted{(pas strict)}',
           'Both outer parentheses are independently visible. The first word has a real descending p followed by a short a/s trace. It cannot be the all-low strokes of non or ou. Strict has its tall crossed letters and low ending. The raised parenthesis belongs after hensélisé and before tilde O_x.',
           H_marked=True),
    change('p09b', 'p09', 'Main line19, the first decorated O and following indexed O',
           r'\tilde O_x', r'\widetilde{\underline{O}}_x', r'\tilde O_x',
           'The first O has a separate two-bend tilde above it and a lower x, but no horizontal underline. The second O in O_{X,x} has a dark horizontal underline, providing a direct local contrast. Both complete ring expressions are included in p09.',
           kind='misread symbol or index', error_category='Symbols and indices'),
    change('p09c', 'p09', 'Main line18, support notation in x∈supp D',
           r'\operatorname{supp}D', r'\operatorname{Supp} D', r'\operatorname{supp}D',
           'The initial s is a small low curved stroke followed by the low u and two descending p strokes. It is not a full-height capital S. The following D and comma are distinct.',
           kind='abbreviation expanded or spelling modernised',
           error_category='Abbreviations expanded, spelling modernised'),
    change('p10a', 'p10', 'Main line20, whole final decorated U_x expression, M0162',
           r'\unsure{\bar U_x|\tilde U_x}', r'\widetilde{U}_x', r'\bar U_x',
           'The decoration over U is one shallow curved horizontal stroke with no second lobe. It differs from the clear two-bend wave over the preceding O on p09. The lower x and whole U are visible. Bar U is retained at medium confidence; no tilde is supplied from the expected relationship with the henselization.',
           confidence='medium', kind='misread symbol or index', error_category='Symbols and indices'),
    change('p10b', 'p10', 'Main line20, final two words',
           'On a', 'On a', 'On à',
           'A short detached dark stroke is directly above the final a and has the same ink strength as the letter. It is separate from On and from any leader or preceding descender. The written accented à is preserved despite the expected grammatical a.',
           vs_C=True, kind='abbreviation expanded or spelling modernised',
           error_category='Abbreviations expanded, spelling modernised'),
    change('p11', 'p11', 'Thin bottom-left foliation',
           r'\margin{127}', '[absent]', r'\margin{127}',
           'The thin digits are 1,2,7; the final 7 has a long top and a separate crossbar through the descending stem. No author page number appears at the head.',
           kind='omission', error_category='Omissions'),
]

upper = r"""de la conjecture analogue déjà faite pour la dim relative $1$.

Pour mieux appréhender cette deuxi\unsure{è|e}me partie \inserted{b)} de la conjecture, il faudrait examiner de plus près ce que deviennent, par composition avec $\mathcal E_L^{\bar L}\mathrel{\text{---}}\mathcal E_U^{\bar L}$, les sections de $\mathcal E_L^{\bar L}$ sur $\mathcal E_K$ associées à un $V$, et pour commencer, étudier le sous-groupe \inserted{$\Delta_V$} de $\unsure{\pi|\Pi}_{U/K}^{\bar L}$ image de $I_V$ --- qui, on le devine, jouera un rôle analogue à un groupe-bout. Dans quelle mesure des $V$ distinctes definissent-elles des $\Delta_V$ distinctes ?"""
lower = r"""Pour étudier cette question, introduisons un modèle $X$ de $L/K$ contenant $U$, $X$ propre, les comp. irréd. de \inserted{$D=$} $X-U$ des diviseurs réguliers \inserted{$D_i$ $(i\in I)$}, et $X-U$ à croisements normaux. Pour $x\in\operatorname{supp}D$, considérons le hensélisé \inserted{(pas strict)} $\tilde O_x$ de $\underline{O}_{X,x}$, et l'image inverse $\bar U_x$ de $U$ dessus. On à"""

data = {
    'page': PAGE, 'scan': 128, 'reader': 'reader_b',
    'line_count': 26,
    'line_count_detail': {'main': 20, 'diagram': 0, 'margin': 0, 'insertion': 5, 'standalone_numbers': 1},
    'changes': changes,
    'decisions': [
        {'id': 'M0160', 'cote': '149', 'scan': '128', 'decision': 'first', 'reading': r'\Delta_V',
         'evidence': 'The two oblique legs are heavily retraced, but a faint complete lower connecting stroke survives between them. That base distinguishes Delta from Lambda. It is retained as live ink; there is no independent cancellation through the base. The entire Delta_V distinctes ? passage was inspected.',
         'crop': f'crops/{PAGE}_p07.png', 'bbox': CROPS['p07']['bbox'], 'confidence': 'medium'},
        {'id': 'M0161', 'cote': '149', 'scan': '128', 'decision': 'first', 'reading': 'pas',
         'evidence': 'A genuine p descender precedes the short a/s strokes inside independently visible parentheses; this excludes non and H’s ou. The complete parenthesis and its hensélisé/O context were inspected.',
         'crop': f'crops/{PAGE}_p09.png', 'bbox': CROPS['p09']['bbox'], 'confidence': 'high'},
        {'id': 'M0162', 'cote': '149', 'scan': '128', 'decision': 'first', 'reading': r'\bar U_x',
         'evidence': 'The whole U_x carries a single shallow curved horizontal bar rather than the two-bend wave seen above the preceding O. The final line supplies the complete expression and context. The first C alternative is selected at medium confidence, without regularizing it to the expected tilde.',
         'crop': f'crops/{PAGE}_p10.png', 'bbox': CROPS['p10']['bbox'], 'confidence': 'medium'},
    ],
    'inventory': [
        {'sheet_kind': 'text', 'hand': 'his hand', 'element': 'e01', 'kind': 'text', 'position': 'Main lines1–2 at the head', 'first_words_or_objects': 'de la conjecture analogue déjà faite', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'his hand', 'element': 'e02', 'kind': 'text', 'position': 'Main lines3–13', 'first_words_or_objects': 'Pour mieux appréhender cette', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'his hand', 'element': 'e03', 'kind': 'insertion', 'position': 'Above main line4; leader after partie', 'first_words_or_objects': 'b)', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'his hand', 'element': 'e04', 'kind': 'insertion', 'position': 'Above main line9; leader between sous-groupe and de', 'first_words_or_objects': r'\Delta_V', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'his hand', 'element': 'e05', 'kind': 'text', 'position': 'Main lines14–20', 'first_words_or_objects': 'Pour étudier cette question, introduisons', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'his hand', 'element': 'e06', 'kind': 'insertion', 'position': 'Above main line16; leader between de and first X-U', 'first_words_or_objects': 'D=', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'his hand', 'element': 'e07', 'kind': 'insertion', 'position': 'One rising baseline above main line17; leader after réguliers and before its comma', 'first_words_or_objects': r'D_i (i\in I)', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'his hand', 'element': 'e08', 'kind': 'insertion', 'position': 'Above main line19, after hensélisé', 'first_words_or_objects': '(pas strict)', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'thin foliation hand', 'element': 'e09', 'kind': 'margin note', 'position': 'Bottom-left corner', 'first_words_or_objects': '127', 'transcribed': 'yes'},
    ],
    'doubts': [
        {'place': 'Main line3, accent in deuxième', 'reading': r'deuxi\unsure{è|e}me', 'alternatives': 'è; e', 'confidence': 'low'},
        {'place': 'Main line9, relative group symbol', 'reading': r'\unsure{\pi|\Pi}_{U/K}^{\bar L}', 'alternatives': r'\pi; \Pi', 'confidence': 'medium'},
    ],
    'audit_boxes': [
        {'box': 'b01', 'kind': 'insertion; handwritten number; doubtful formula; C/H word difference', 'bbox': [285, 80, 1670, 1575], 'reading': upper},
        {'box': 'b02', 'kind': 'insertion; doubtful formula; C/H word difference', 'bbox': [285, 1590, 1645, 2340], 'reading': lower},
        {'box': 'b03', 'kind': 'margin note; handwritten number', 'bbox': CROPS['p11']['bbox'], 'reading': r'\margin{127}'},
    ],
    'notes': [
        'The initial two lines continue the conjecture discussion. The next paragraph proposes studying images of inertia groups under passage from L to a model U; the final paragraph introduces a proper model and local henselization notation. This description does not verify the conjecture or the geometric construction.',
        'There is no written author page number at the head. The thin lower-left foliation is127, in a hand distinct from the main mathematical text.',
        'All20 main baselines were read, with5 independent raised insertion baselines and1 standalone foliation element, giving26 logical lines. D_i and its parenthesized indexing phrase share one rising inserted baseline. Ordinary superscripts/subscripts remain part of their containing line.',
        'The word identity deuxième is supported by the crossed x and ending, while the separate accent over the following e cannot be distinguished confidently from the neighbouring i strokes. Only the accent is marked: deuxi unsure(è|e) me. The accented alternative remains first; this is a new uncertainty with unchanged preferred C reading, not a counted correction against C.',
        'The first connecting stroke is retained as a dash. Its tiny thickened downward right terminal does not establish an arrowhead. Composition may indicate an intended map, but that interpretation does not add ink.',
        'The lower letter after the second E on main line7 has a compressed n-like outline. The page’s L/K notation and the supplied established E_K notation identify the base-field symbol as K; this is treated as an ambiguous hand convention, not a clear wrong-letter slip and not a new independent field n. The complete expression was inspected in p03 and is included in auditb01.',
        'The relative pi sign has a flat cap and a curled right foot, and is smaller than the nearby I. These features favour lowercase pi; the case is still not decisive, so pi|Pi remains in place. This added case doubt alone is not counted as a correction against either witness.',
        'The top horizontal of I_V is the upper stroke of I, with a central upright and bottom foot. No additional bar above a complete I is present. The later inserted i∈I supplies the local capital-I comparison.',
        'The final Delta_V has black retraced oblique legs and a faint complete lower connecting stroke. That surviving base resolves M0160 to the first reading at medium confidence. No erased underletter or cancellation layer is invented. The first inserted Delta_V has a clearer complete base.',
        'The raised b), Delta_V, D= and D_i(i∈I) each have their own traced attachment. The curved leaders are not parentheses, commas or underlines. In contrast, the comma below the final s of réguliers is a separate dark curve; it is retained after the inserted label and before et.',
        'The literal feminine distinctes is retained. The first e of definissent lacks a detached accent; both witnesses normalize it to définissent. No grammatical or orthographic repair is supplied.',
        'The hensélisé addition has two real outer parentheses and reads pas strict, resolving M0161. The first O has a true two-bend tilde and no underline. The following O_{X,x} is underlined. The last U_x carries a single shallow curved bar, resolving M0162 at medium confidence despite a possible expected tilde.',
        'The final a has a real detached dark accent, so the candidate ends On à. This is retained as a literal source form despite the grammatical expectation On a. The sentence is not completed beyond this page.',
        'The two X-U separators are short dash forms and are not silently modernized to set-minus glyphs. Lowercase supp is retained. Written abbreviations dim, comp. and irréd. remain unexpanded with only their actual stops.',
        'The complete first doubtful Delta expression, the relative pi expression, and the ring/U expressions are included with their full surrounding text in the audit readings. The only ink digit in the body is the opening dimension1; all indices elsewhere are letters. The foliation127 has its own complete box.',
        'The whole page and each native half were visually inspected once. Eleven saved crops were then inspected once each; no contextual repair or repeated crop was required. No deletion was found when the insertions, retraced Delta and possible punctuation were checked separately.',
        'No OCR, external sources, other-page witnesses or images, TeX compilation, independent audit or mathematical proof check was used. Only the current assigned notation table and the common rules supplemented this page packet.',
    ],
    'checks': [],
    'hand_observations': [
        {'habit': 'Small sloping insertion leaders can resemble punctuation.', 'places': 'b), Delta_V, D= and D_i(i∈I); p01,p04,p08', 'holds': 'Each leader is continuously traceable; the comma below réguliers is independently written.', 'witness_errors': 'H misplaces b), Delta_V and D_i; C omits the independent comma.'},
        {'habit': 'A compressed mathematical K subscript can have an n-like outline.', 'places': 'E_K in main line7; p03', 'holds': 'One local compressed occurrence; K is identified by the page’s base-field notation and current notation table, not by an asserted clear K-shaped stroke.', 'witness_errors': 'Both witnesses identify K; no correction counted.'},
        {'habit': 'Relative pi has a flat cap and curled right leg; case cannot be decided from the cap alone.', 'places': 'Main line9; p04', 'holds': 'Lowercase preferred locally, with uppercase still open.', 'witness_errors': 'Both witnesses print lowercase without this case doubt.'},
        {'habit': 'A long detached top stroke can still be the upper part of capital I rather than an overbar.', 'places': 'I_V on main line9 and I in the raised i∈I; p04,p08', 'holds': 'Only the ordinary upper and lower I strokes are present.', 'witness_errors': 'H adds an overbar to I_V.'},
        {'habit': 'Heavy retracing can obscure but does not necessarily cancel a faint triangular base.', 'places': 'Final Delta_V on main line13; p07', 'holds': 'The lower connecting stroke survives; Delta is read at medium confidence.', 'witness_errors': 'C leaves Delta/Lambda unresolved; H gives Delta.'},
        {'habit': 'A shallow curved bar and a two-bend tilde coexist on adjacent expressions.', 'places': 'Tilde O_x and final bar U_x; p09,p10', 'holds': 'The O decoration is a true wave; the U decoration is a single shallow curve.', 'witness_errors': 'H regularizes U to a tilde; C first bar reading is selected.'},
        {'habit': 'Accent presence can depart from expected French spelling.', 'places': 'deuxième, definissent and final On à; p01,p06,p10', 'holds': 'First accent unresolved; no detached accent over first e of definissent; clear detached mark over final a.', 'witness_errors': 'Both witnesses supply the accent in définissent and omit the final accent in On à.'},
    ],
    'notation': [
        {'written': r'\mathcal E_L^{\bar L}\mathrel{\text{---}}\mathcal E_U^{\bar L}', 'meaning_or_use': 'The source and target named in the composition phrase, joined by a written plain shaft.', 'places': 'Main line6; p02'},
        {'written': r'\mathcal E_K', 'meaning_or_use': 'Base-field expression; its compressed K is n-like in the local hand, identified by established notation.', 'places': 'Main line7; p03'},
        {'written': r'\Delta_V', 'meaning_or_use': 'Inserted name of the subgroup, repeated in the question; the second occurrence has a faint surviving triangular base.', 'places': 'Insertion above main line9 and main line13; p04,p07'},
        {'written': r'\unsure{\pi|\Pi}_{U/K}^{\bar L}', 'meaning_or_use': 'Relative group in which the image of I_V is considered; pi case remains unresolved.', 'places': 'Main line9; p04'},
        {'written': r'I_V', 'meaning_or_use': 'Unbarred group expression after image de; the long top horizontal is part of I.', 'places': 'Main line9; p04'},
        {'written': r'D=X-U;\ D_i\ (i\in I)', 'meaning_or_use': 'The D= and component labels are raised additions attached at different places.', 'places': 'Main lines16–17 and their insertions; p08'},
        {'written': r'x\in\operatorname{supp}D', 'meaning_or_use': 'Condition on the point in the local construction; supp begins with a small s.', 'places': 'Main line18; p09'},
        {'written': r'\tilde O_x;\ \underline O_{X,x};\ \bar U_x', 'meaning_or_use': 'The three distinct written decorations are preserved: tilde over plain O, underline under the second O, bar over final U.', 'places': 'Main lines19–20; p09,p10'},
    ],
    'abbreviations': [
        {'written': 'dim', 'expansion': 'dimension'},
        {'written': 'comp.', 'expansion': 'composantes'},
        {'written': 'irréd.', 'expansion': 'irréductibles'},
        {'written': 'supp', 'expansion': 'support'},
    ],
    'inspection': {
        'whole': True, 'halves': ['top', 'bottom'],
        'crops': [f'crops/{PAGE}_{name}.png' for name in CROPS],
        'deletions_insertions_checked': True,
        'whole_image_visual_inspections': 1,
        'native_half_visual_inspections': {'top': 1, 'bottom': 1},
        'contextual_repairs': [],
    },
}

def main():
    expected = {r['id'] for r in csv.DictReader((ROOT / f'packets/{PAGE}/marks.tsv').open(), delimiter='\t')}
    assert {r['id'] for r in data['decisions']} == expected
    assert sum(data['line_count_detail'].values()) == data['line_count']
    for name, item in CROPS.items():
        assert (ROOT / f'edition/crops/{PAGE}_{name}.png').exists()
        x0,y0,x1,y1 = item['bbox']
        assert 0 <= x0 < x1 <= 1680 and 0 <= y0 < y1 <= 2360
    out = ROOT / f'edition/review/{PAGE}.json'
    if out.exists():
        raise FileExistsError(f'Refusing to overwrite completed metadata: {out}')
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(f'{PAGE}: {len(changes)} collation places, {sum(x["vs_C"] for x in changes)} against C, {len(CROPS)} inspected crops, {len(data["doubts"])} open doubts, {data["line_count"]} logical lines')

if __name__ == '__main__':
    main()
