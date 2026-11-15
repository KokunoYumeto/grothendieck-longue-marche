"""Build the current doubt register from balanced in-place macro arguments.

Confidence assignments below are the reader's conservative assessments after
the visual audits. This script performs indexing and formatting, not OCR.
"""
from pathlib import Path
from collections import defaultdict
import json

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_15_087-138'

def cell(s):
    return str(s).replace('|', '&#124;').replace('\n', ' ')

def split_alternative(s):
    depth = 0
    for i, ch in enumerate(s):
        if ch == '{' and (i == 0 or s[i-1] != '\\'):
            depth += 1
        elif ch == '}' and (i == 0 or s[i-1] != '\\'):
            depth -= 1
        elif ch == '|' and depth == 0:
            return s[:i], s[i+1:]
    return s, 'No competing reading supplied; the literal reading remains uncertain.'

# Visual uncertainty in these compact glyphs is moderate. Heavily cancelled
# words, long phrases, and other unresolved readings receive low confidence.
MEDIUM = {
    r'\mathscr G|G', r"\mathscr G'|G'", r'\circ|0', r':|=',
    r'0|O', r'\Phi|\phi', r'\epsilon|e', r'P\'|P',
    r'\mathbb R|R', r'\mathbb K|K', r'K|\mathbb K',
    r'\text{—}|\longrightarrow', r'\sim|\longmapsto',
    r'\Downarrow|\Updownarrow', r'\Updownarrow|\Downarrow',
    r'*', r'**', r'p^\nu|p^n', r'i_1|i_2', r'\{F\}|[F]',
    r"f_m'|f_{m'}", r'\ell|p', r'T^2|T', r'n|\bullet',
    r'\overline{\mathrm m}|=', r'La|la', r'\lambda\'|\lambda',
    r'\mathfrak F|\mathcal F', r'p.r.|par.', r'j|\mu',
}
MEDIUM_BY_SCAN = {
    88: {'hom'}, 89: {'Jawobson|Jacobson'}, 91: {"qr'il|qu'il"},
    94: {'+', 'ii bis', 'Riemann', 'A'}, 95: {'0|O'},
    100: {'frobénius', '2', 'n'}, 101: {'the'},
    106: {'Les|Soit', 'probablement'}, 107: {'i_1|i_2'},
    110: {'can.', 'hensélisé'}, 112: {'L_0', 'q'},
    114: {'=', 'non un|un non'}, 117: {'2', 'I'},
    119: {'1|2', 'U'}, 125: {'ne|me', 'corresponde', 'conjectural', 'divisant'},
    128: {'x|a', 'f. et s.'}, 129: {'expos.'},
    131: {'Q', r'\alpha'}, 132: {'*+', 'K'}, 133: {'sera'},
    135: {'can.', 'U', 'vectoriels'}, 137: {"M'|M''", 'i|-i'},
    138: {"P'|P"},
}

def main():
    readings = [json.loads(x) for x in (ROOT/'records/readings.jsonl').read_text().splitlines()]
    index = json.loads((ROOT/'records/doubt_occurrences.json').read_text())
    lines = ['# Notation table', '',
             'The readings below were compared across the page images before the transcription was frozen. Small round superscripts retain an explicit circle/zero alternative; the looped gerbe letter uses `\\mathscr G` throughout. Abbreviation expansions appear only in the separate list below.', '',
             '| Manuscript sign | LaTeX | Scans | Reading observations |',
             '|---|---|---|---|']
    for d in readings:
        for n in d['notation']:
            lines.append('| ' + ' | '.join(cell(x) for x in [n[0], n[1], d['scan'], n[2]]) + ' |')
    lines += ['', '# Current doubt register', '',
              f"This table indexes all {index['occurrence_count']} in-place doubt marks in the final page files: {index['counts']['unsure']} `\\unsure` occurrences and {index['counts']['illegible']} `\\illegible` occurrences. Nested marks receive separate rows. Locations use one-based **page-file LaTeX line and character column**, which locate the exact passage even where a handwritten paragraph has been joined into one source line.", '',
              'The first reading is the literal reading selected from the ink. Confidence concerns that reading and, where relevant, its cancellation or insertion state. Medium confidence still requires caution; low confidence identifies a reading for renewed inspection. Earlier working readings and their corrections remain documented in the audit records, while this table follows the current page files.', '',
              '| File | Scan | Approximate line / position | Reading | Alternatives | Confidence |',
              '|---|---|---|---|---|---|']
    confidence_records=[]
    for o in index['occurrences']:
        arg=o['argument']
        if o['macro']=='illegible':
            reading='\\illegible{'+arg+'}'
            alternative=f'Approximately {arg} physically unreadable words; no recoverable reading retained.'
            confidence='low'
        else:
            reading, alternative=split_alternative(arg)
            confidence='medium' if arg in MEDIUM or arg in MEDIUM_BY_SCAN.get(o['scan'],set()) else 'low'
        loc=f"TeX {o['source_line']}:{o['source_column']}"
        lines.append('| '+' | '.join(cell(x) for x in [o['page_filename'],o['scan'],loc,reading,alternative,confidence])+' |')
        confidence_records.append({**o,'primary_reading':reading,'alternative':alternative,'confidence':confidence})
    lines += ['', '# Local reading observations', '',
              '- **Scans 88, 90, 92, 104 and 129:** crossed and overwritten draft passages contain the least recoverable ink. The four unreadable spans occur in cancelled prose on scans 88, 90 and 129; no mathematical symbol is replaced by an unreadable-word count.',
              '- **Scans 96, 110, 117 and 121:** small marginal writing, crowded insertions, and labels require particular care. The note beside the valuation construction on scan 121 remains a low-confidence reading after enlargement and rotation.',
              '- **Scans 111, 113 and 115:** the typescripts contain awkward or incomplete parentheses and restriction subscripts. The files retain the forms supported by the image, including the explicitly doubtful long cohomology formula on scan 111.',
              '- **Scans 120, 122, 124 and 126:** the typed phi glyph, handwritten circular Phi/phi forms, and cursive divisor subscripts were compared together. Case and the unusual raised equation on scan 120 remain marked where unresolved.',
              '- **Scans 128–133:** generic field letters and distinguished fields with doubled stems were compared directly. The cancelled lemma and small insertion on scan 130 retain alphabet alternatives.',
              '- **Scan 135:** eight faint `D R` stamps and the vertical separator beside the lower diagram are transcribed. These faint front-side marks were checked separately from reverse-side bleed-through.',
              '- **Scan 138:** the sheet was read after rotation. The double underlining below N and R is reproduced literally; the sum starts at the visible index zero, and the final sentence remains unfinished.',
              '', '# Abbreviations', '',
              'These are proposed expansions for reference only. They have not been inserted into the transcription. Where the literal abbreviation is doubtful, the proposal preserves that uncertainty.', '',
              '| Written form | Proposed expansion | Scans |', '|---|---|---|']
    abbreviations=defaultdict(list)
    for d in readings:
        for written, expansion in d['abbreviations']:
            abbreviations[(written,expansion)].append(d['scan'])
    for (written,expansion),scans in sorted(abbreviations.items(),key=lambda x:x[0][0].casefold()):
        lines.append('| '+' | '.join(cell(x) for x in [written,expansion,', '.join(str(n) for n in sorted(set(scans)))])+' |')
    lines += ['', '# Legibility and limits', '',
              'All 48 supplied scan pages were read visually in order by one reader, using the whole images and their supplied halves, then reread against the saved transcription in a second page-by-page audit. Enlargements and rotations were used for small writing; no OCR was used. Mathematical oddities, missing visible signs, abbreviations, unfinished text, and surviving cancelled material were preserved rather than completed from mathematical expectation.', '',
              'The reused typescripts are generally the most legible portions, although faint impressions and handwritten formula insertions complicate some indices. Confidence is lowest in the heavily cancelled drafts, the marginal note on scan 121, and the six-line note on scan 125. The explicit doubt marks are intended to make these limits inspectable; unmarked text is a reading judgment, not a claim of error-free transcription. The TeX fragment received structural checks, but this environment lacked the TeX distribution and packages needed for a successful typeset compilation.', '']
    (ROOT/f'{PREFIX}_doubts.md').write_text('\n'.join(lines),encoding='utf-8')
    (ROOT/'records/doubt_confidence.json').write_text(json.dumps(confidence_records,ensure_ascii=False,indent=2)+'\n')
    print(f'Finalized {len(confidence_records)} current doubt rows and {len(abbreviations)} abbreviation entries.')

if __name__ == '__main__':
    main()
