from pathlib import Path
import json
import re

root = Path('/workspace/scratch/94548b74fbe0')
out = root / 'out/readers/007/A'
reading = (root / 'packets/007/C.tex').read_text()
(out / 'reading.tex').write_text(reading)

report = {
  'scan': 7,
  'reader': 'A',
  'start_utc': '2026-11-20 11:08:02 UTC',
  'end_utc': '2026-11-20 11:14:26 UTC',
  'full_image_viewed': True,
  'halves_viewed': True,
  'complete_visual_read': True,
  'differences': [
    {
      'id': '007-A-01',
      'location': 'Opening blacked-out mark immediately before Soit, upper left',
      'C': r'\deleted{\illegible{1}}',
      'H': None,
      'reading': r'\deleted{\illegible{1}}',
      'evidence': 'The enlargement shows a densely blackened compact patch with overlapping loops and short projections. The internal pale gaps do not yield a recoverable character sequence. The full height of the patch and the following Soit are present in the crop.',
      'confidence': 'high',
      'kind': 'other',
      'diff_C': False,
      'diff_H': False,
      'C_doubt_status': 'retained',
      'readers_crop': 'crops/01_opening_deletion.png',
      'bbox': {'coordinate_system': 'original full scan, top-left origin', 'xyxy': [20,18,180,88]},
    },
    {
      'id': '007-A-02',
      'location': 'Pale two-line marginal note at right of divisibility pairs, first character',
      'C': r'\unsure{a|\alpha}',
      'H': None,
      'reading': r'\unsure{a|\alpha}',
      'evidence': 'A small closed loop joins a rightward falling tail. Its short top contact and tail support a as the first candidate; the same visible form also supports alpha in this small pale hand. The crop supplies no separate longer stem that settles the choice. No character is inferred from the adjacent main-hand formulas.',
      'confidence': 'medium',
      'kind': 'other',
      'diff_C': False,
      'diff_H': False,
      'C_doubt_status': 'retained',
      'readers_crop': 'crops/02_pale_note.png',
      'bbox': {'coordinate_system': 'original full scan, top-left origin', 'xyxy': [990,950,1348,1064]},
    },
    {
      'id': '007-A-03',
      'location': 'Pale marginal note, ending of n\u2019exist / n\u2019existe',
      'C': r"\unsure{n'exist|n'existe}",
      'H': None,
      'reading': r"\unsure{n'exist|n'existe}",
      'evidence': 'After the low angular s-like turn, the final tall stroke descends and bends right. No independent final e is securely separated from that bend. The first candidate n\u2019exist is retained, with n\u2019existe preserved as the supported alternative. The continuation pas si and the complete second line on avait p=1 are within the crop.',
      'confidence': 'medium',
      'kind': 'other',
      'diff_C': False,
      'diff_H': False,
      'C_doubt_status': 'retained',
      'readers_crop': 'crops/02_pale_note.png',
      'bbox': {'coordinate_system': 'original full scan, top-left origin', 'xyxy': [990,950,1348,1064]},
    }
  ],
  'doubts': [
    {'location': 'Opening deletion', 'reading': r'\deleted{\illegible{1}}', 'alternatives': [], 'confidence': 'low', 'reason': 'Physically blacked out; no recoverable original sequence after the single enlargement.', 'crop': 'crops/01_opening_deletion.png'},
    {'location': 'Pale note, first character', 'reading': 'a', 'alternatives': [r'\alpha'], 'confidence': 'medium', 'reason': 'Small loop with rightward falling tail; Latin a and alpha remain supported.', 'crop': 'crops/02_pale_note.png'},
    {'location': 'Pale note, first-line verb ending', 'reading': "n'exist", 'alternatives': ["n'existe"], 'confidence': 'medium', 'reason': 'Terminal bend merges with tall last stroke; no independent e is securely separated.', 'crop': 'crops/02_pale_note.png'}
  ],
  'inventory': [],
  'notes': {
    'page_content': 'Handwritten French number-theoretic working. The page states positive-integer and pairwise-coprimality conditions, inserts a^q+b^q=c^q, expands (a+b\u2032)^q, then writes divisibility statements involving p, alpha and alpha prime. These are descriptions of the transcribed writing.',
    'authors_own_uncertainty': [],
    'title_date_page_counts': 'No title or date is written. Pencilled archive sheet number 6 appears at the bottom left and is retained solely as a TeX comment. No manuscript page number is assigned.',
    'mathematics_led_reading_decisions': 'No mathematical computation or proof check was performed. Formula glyphs, indices, exponents, divisibility strokes and inequalities were compared directly with their visible ink. The crowded penultimate summation was enlarged because its small curled body and bounds were compressed; the upper q-1 and lower i=1 are legible and the C reading is retained.',
    'witness_scope': 'H status is nothing for this page. All H values are null and diff_H is false. No H collation rows are invented.',
    'C_doubt_accounting': 'The actual C uncertainties comprise three unique loci: the opening blacked-out mark, the pale initial a/alpha, and the ending n\u2019exist/n\u2019existe. The last locus is listed twice in C_doubts.txt and is covered by 007-A-03. The six preceding notation-table rows are recorded as notation, without creating C-doubt rows.',
    'view_attestation': 'The whole image was opened once, then supplied half a once, then supplied half b once. All three created crops were opened once each. No other image, other page or reader was inspected. No OCR, recognition tool, internet or external source was used. All remaining uncertain loci are retained explicitly.',
    'image_geometry': 'Whole scan dimensions are 1405 by 1720 pixels. Both supplied halves are 1405 by 940. Half a starts at full-scan y=0; the bottom-aligned half b starts at y=1720-940=780. All crop boxes use original full-scan coordinates.',
    'physical_states': 'The insertion et a^q+b^q=c^q lies between the pairwise-coprimality sentence and On a c>a. The phrase ou p=1 is crossed by two close rising diagonal strokes; its text and deleted state are retained. The opening mark is heavily blacked out. No diagram or separate drawing is present.',
    'hand_attribution': 'The main text uses the upright segmented hand identified as another hand in the supplied inventory; no personal identity is assigned. The pale marginal note remains of undetermined hand.',
    'crop_bounds': 'The three target loci are complete within their crops. The crowded-sum crop includes nearby fragments of adjacent lines at its top and bottom edges; the entire target summation, its bounds, factors and right parenthesis are present.',
    'collation_outcome': 'No changed C reading was established. All three unique original C doubts remain; the complete proposed text has the same reading as C.'
  },
  'notation': [
    {'location': 'Top conditions; conditions on b prime, a prime and both alphas', 'sign_or_abbreviation': 'N with doubled left strokes and raised asterisk', 'proposed_latex': r'\mathbb N^*', 'evidence': 'Two upright/oblique strokes at the N left and a separate small raised crossed asterisk.'},
    {'location': 'Pairwise-coprimality line; posons line; final reason', 'sign_or_abbreviation': 'Shallow bowl with small hooked 1 below', 'proposed_latex': r'\mathrel{\underset{1}{\smile}}', 'evidence': 'Bowl and lower hooked numeral are separately visible at each occurrence.'},
    {'location': 'All binomial sums', 'sign_or_abbreviation': 'C with upper i and lower q; indexed summation', 'proposed_latex': r'C_q^i,\sum_{i=0}^{q},\sum_{i=1}^{q-1}', 'evidence': 'Dotted upper i and descending lower q are visible. The first lower bound is i=0; all subsequent lower bounds read i=1. The crowded penultimate sum is resolved by crop 03.'},
    {'location': 'c=a+b prime=b+a prime onward', 'sign_or_abbreviation': 'Prime and double prime', 'proposed_latex': r"a',b',b''", 'evidence': 'Separate short raised strokes occur above a and b; b double prime has two raised strokes.'},
    {'location': 'Alpha conditions and all subsequent p exponents', 'sign_or_abbreviation': 'Main-hand alpha and alpha prime', 'proposed_latex': r"\alpha,\alpha',p^{q\alpha-\alpha'}", 'evidence': 'Rounded curled head with continuing tail; prime is a separate upper stroke. The pale-note initial remains independently doubtful.'},
    {'location': 'Divisibility pairs and implication chain', 'sign_or_abbreviation': 'Vertical and crossed vertical; broad double-line arrows; angled inequalities', 'proposed_latex': r'\mid,\nmid,\Longrightarrow,\geqslant,\leqslant', 'evidence': 'Plain upright divisibility strokes, crossing diagonal on the two negative divisibility strokes, and two arrow shafts are visible. Inequalities include their short second slant.'}
  ],
  'check_events': [],
  'crops': [
    {'path': 'crops/01_opening_deletion.png', 'bbox': [20,18,180,88], 'rotation': 0, 'purpose': 'Opening original C illegibility; complete black patch with following Soit; width 2800, LANCZOS, autocontrast, unsharp mask.'},
    {'path': 'crops/02_pale_note.png', 'bbox': [990,950,1348,1064], 'rotation': 0, 'purpose': 'Both original C pale-note uncertainties, with both complete note lines; width 3400, LANCZOS, autocontrast, unsharp mask.'},
    {'path': 'crops/03_crowded_sum.png', 'bbox': [390,1490,990,1590], 'rotation': 0, 'purpose': 'Penultimate implication: compressed summation glyph and both bounds, with the full following expression; width 3600, LANCZOS, autocontrast, unsharp mask.'}
  ],
  'brief_feedback': 'The supplied C doubt list repeats the n\u2019exist/n\u2019existe locus. A single local decision with an explicit duplicate-accounting note was used. No other convention ambiguity arose.'
}

items = [
('007.A.01','deletion','Top left before Soit','Blacked-out opening mark'),
('007.A.02','text','First line','Soit a in N* ... q nombre premier (q != 1)'),
('007.A.03','text','Second line, including right-hand parenthesis','On suppose que ... (premiers entre eux deux à deux)'),
('007.A.04','insertion','Left between second and third main lines','et a^q+b^q=c^q'),
('007.A.05','text','Upper section','On a c>a et c>b car ...'),
('007.A.06','text','Before first display','On pose c=a+b prime=b+a prime avec ...'),
('007.A.07','display','Upper-middle two-line expansion','alors a^q+b^q=c^q=... (Newton); next expansion line'),
('007.A.08','display','Immediately below expansion','donc b^q=... (1)'),
('007.A.09','text','Three lines above fold','la puissance de b prime ... (b prime divise b^q)'),
('007.A.10','text','Below fold, introductory p line','Soit p un nombre premier ... et tel que :'),
('007.A.11','deletion','Between premier and et tel que','ou p=1, crossed by two close rising diagonal strokes'),
('007.A.12','text','Following physical line','p|b prime donc p|b. Soit alpha in N* et alpha prime in N* tels que'),
('007.A.13','display','Middle-lower, two rows','p^(alpha prime)|b prime ... et p^alpha|b ...'),
('007.A.14','margin note','Right of first divisibility pair, two pale lines','a/alpha n\u2019exist/n\u2019existe pas si / on avait p=1'),
('007.A.15','text','Right of second divisibility pair','On a alpha prime <= q alpha car b prime|b^q'),
('007.A.16','display','Lower third, two implications','(1) implies p^(q alpha)|sum ...; implies p^(q alpha)|b prime(...)'),
('007.A.17','text','Before final three implications','posons b prime=p^(alpha prime)b double prime ... (propriété de alpha prime)'),
('007.A.18','display','Foot, three implications','p^(q alpha)|p^(alpha prime)b double prime(...); two p^(q alpha-alpha prime) rows')
]
for element,kind,position,first in items:
    report['inventory'].append({'sheet_kind':'text','hand':'undetermined hand' if kind=='margin note' else 'another unnamed hand','element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
(out / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')

md = r'''# Scan 007 — independent reader A

Start: 2026-11-20 11:08:02 UTC, recorded before packet and image work.

## View and collation record

The whole scan was viewed once for layout; half a was then viewed once and half b once for the complete line-by-line reading. Three tight crops were made and each was viewed once. No other page or reader was inspected. H has status `nothing`; all H fields are null and no H differences are proposed.

The complete proposed text retains C's reading. Three unique C uncertainty loci remain: the opening blacked-out mark, the pale initial `a|α`, and `n'exist|n'existe`. The ending doubt occurs twice in the supplied doubt list and is covered once as a single local locus. The notation-table entries were checked as notation.

## Line-by-line ink audit

Coordinates below refer to the original 1405 × 1720 scan, with top-left origin. Half a has origin y=0; the bottom-aligned half b has origin y=780 (1720−940).

| Physical line or block | Readable ink and state | Audit result |
| --- | --- | --- |
| Opening and first line, y≈25–90 | Dense deleted mark; `Soit a∈ℕ*, b∈ℕ*, c∈ℕ*, q∈ℕ* q nombre premier (q≠1)` | Membership, raised stars, commas and closing parenthesis read on a. Deletion retains `\deleted{\illegible{1}}` after crop 01. |
| Second line and right parenthesis, y≈90–168 | `On suppose que` and three bowl/1 coprimality signs; `(premiers entre eux deux à deux)` | All three pairs and both parentheses read; grave accent on `à` retained. |
| Small inserted line, y≈150–199 | `et a^q+b^q=c^q` | Read as the inserted line between the surrounding main lines; all three q exponents visible. |
| Next main line, y≈190–239 | `On a c>a et c>b car a∈ℕ* et b∈ℕ*` | Both strict inequalities and the two membership conditions read. |
| Definition line, y≈270–331 | `On pose c=a+b′=b+a′ avec b′∈ℕ* et a′∈ℕ*` | Both primes, both equality signs and all membership signs read. |
| Expansion line, y≈330–424 | `alors a^q+b^q=c^q=(a+b′)^q=∑_{i=0}^q C_q^i a^i b′^{q−i} (Newton)` | First lower bound is `i=0`; upper q, coefficient indices and exponent subtraction read. |
| Expansion continuation, y≈420–518 | `=b′^q+∑_{i=1}^{q−1} C_q^i a^i b′^{q−i}+a^q (car q≥2)` | Two plus signs, lower `i=1`, upper `q−1`, terminal `a^q`, parentheses and second inequality stroke read. |
| Labelled consequence, y≈525–623 | `donc b^q=∑_{i=1}^{q−1} C_q^i a^i b′^{q−i}+b′^q (1)` | Every index, prime and the parenthesized label read. |
| Prose line 1, y≈622–695 | `la puissance de b′ n'étant jamais nulle on peut mettre b′` | Wording and both primed b occurrences read. |
| Prose line 2, y≈691–762 | `en facteur dans le second membre de (1), donc b′|b^q` | Comma after `(1)` and vertical divisibility stroke read. |
| Prose line 3, y≈770–831 | `(b′ divise b^q)` | Both parentheses and q exponent read. |
| First line below fold, y≈823–913 | `Soit p un nombre premier` then deleted `ou p=1`, then `et tel que :` | Deleted words readable. Two close rising diagonal cancellation strokes lie across that phrase; colon retained. |
| Next line, y≈907–981 | `p|b′ donc p|b. Soit α∈ℕ* et α′∈ℕ* tels que` | Both divisibility strokes, full stop, two stars and alpha prime read. |
| First valuation pair, y≈978–1063 | `p^{α′}|b′ et p^{α′+1}∤b′` | Prime on exponent and both b primes read; negative divisibility has crossing diagonal. |
| Second valuation pair, y≈1060–1142 | `et p^α|b et p^{α+1}∤b` | Both plus/1 exponent elements, plain b and crossing diagonal read. |
| Pale note, y≈972–1044 | `a|α n'exist|n'existe pas si` / `on avait p=1` | Both original uncertainties retained after crop 02. The rest of the two-line note is readable. Hand attribution remains undetermined. |
| Main-hand aside, y≈1043–1124 | `On a α′≤qα car b′|b^q` | Alpha prime, both inequality strokes, q alpha, b prime and divisibility read. |
| First implication, y≈1155–1254 | `(1)⇒p^{qα}|∑_{i=1}^{q−1} C_q^i a^i b′^{q−i}+b′^q` | Double arrow shaft, p exponent, sum bounds and final b-prime power read. |
| Second implication, y≈1232–1348 | `⇒p^{qα}|b′(∑_{i=1}^{q−1} C_q^i a^i b′^{q−i−1}+b′^{q−1}) (car q≥2)` | Outer b prime, both exponent minuses, parentheses and inequality strokes read. |
| Posons line, y≈1326–1417 | `posons b′=p^{α′}b″ donc b″` bowl/1 `p (propriété de α′)` | Double primes, lower hooked 1, accents and final alpha prime read. |
| Final chain, row 1, y≈1414–1519 | `⇒p^{qα}|p^{α′}b″(∑_{i=1}^{q−1} C_q^i a^i b′^{q−i−1}+b′^{q−1})` | Distinct exponents q alpha and alpha prime, two b primes, all sum indices and exponents read. |
| Final chain, row 2, y≈1497–1590 | `⇒p^{qα−α′}|b″(∑_{i=1}^{q−1} C_q^i a^i b′^{q−i−1}+b′^{q−1}) car qα≥α′` | Crowded sum enlarged once in crop 03: upper `q−1`, small curled summation body, and lower `i=1` are readable, with no cancellation established. Remaining formula and reason read on b. |
| Final chain, row 3, y≈1584–1658 | `⇒p^{qα−α′}|∑_{i=1}^{q−1} C_q^i a^i b′^{q−i−1}+b′^{q−1} car b″` bowl/1 `p` | Arrow, exponent subtraction, sum bounds, final prime powers and coprimality sign read. |
| Lower-left archive mark, y≈1658–1695 | Pencilled `6` | Recorded only in `% archive sheet number: 6`. |

## Crop audit

| File | Original bounding box | Enlargement | Result |
| --- | --- | --- | --- |
| `crops/01_opening_deletion.png` | `[20,18,180,88]` | Width 2800, rotation 0° | Full black patch and following `Soit`; internal strokes remain unrecoverable. |
| `crops/02_pale_note.png` | `[990,950,1348,1064]` | Width 3400, rotation 0° | Both complete note lines; initial a/alpha and terminal e remain unsettled. |
| `crops/03_crowded_sum.png` | `[390,1490,990,1590]` | Width 3600, rotation 0° | Entire target sum, limits, following factors and closing parenthesis; C retained. Adjacent-line fragments appear at crop edges. |

Each crop used PIL autocontrast, LANCZOS enlargement and the supplied helper's sharpening. No place was recropped. There are no separate drawings or diagrams on this page. The transcription preserves the insertion, both deletions and the pale note with the prescribed macros.

No mathematical computation, asserted correspondence or proof check was performed. `check_events` is empty. The record reports only the visual reading and collation actually completed.
'''
md = md.replace("a|α n'exist|n'existe pas si", "a/α n'exist/n'existe pas si")
md = '\n'.join(
    re.sub(chr(96) + '[^' + chr(96) + ']*' + chr(96), lambda match: match.group(0).replace('|', '∣'), line)
    if line.startswith('|') else line
    for line in md.split('\n')
)
(out / 'reading.md').write_text(md)
print('Wrote reading.tex, report.json, reading.md and build_record.py under out/readers/007/A/.')
