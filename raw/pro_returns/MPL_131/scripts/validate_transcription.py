#!/usr/bin/env python3
"""Read-only structural checks; never substitutes for visual manuscript review.

Usage: python scripts/validate_transcription.py [WORK_DIRECTORY] [--partial]
Frozen hash record format (one per page and combined fragment):
    sha256 <64 hexadecimal characters> <relative/path>
Ordinary sha256sum records and ``sha256 <relative/path> <digest>`` also work.
Only standard TeX, common mathematical commands, TikZ commands, and the specified
editorial macros are recognized. Unclassified commands produce warnings, because
an exhaustive standard/package command whitelist would be unsafe.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

SCANS = [n for n in range(2, 43) if n not in {11, 19, 22}]
FIELDS = ['cote', 'scan', 'sheet_kind', 'element', 'kind', 'position',
          'first_words_or_objects', 'transcribed']
SHEET_KINDS = {'text', 'reused_typed', 'cancelled_draft', 'cover'}
KINDS = {'text', 'display', 'diagram', 'drawing', 'margin note', 'insertion', 'deletion'}
EDITORIAL = set('cotefile scanpage mspage deleted inserted margin uline uuline '
                'diagram figure unsure illegible'.split())
STANDARD = set('''begin end text textrm textsf texttt textbf textit textnormal
emph rm sf tt bf it normalfont small scriptsize tiny large Large LARGE huge Huge
mathcal mathscr mathfrak mathbb mathbf mathrm mathsf mathtt mathit mathnormal
boldsymbol bm operatorname DeclareMathOperator overset underset stackrel
frac dfrac tfrac binom dbinom tbinom sqrt left right middle big Big bigg Bigg
bigl bigr Bigl Bigr biggl biggr Biggl Biggr overline underline widehat widetilde
hat tilde bar vec dot ddot dddot breve check acute grave mathring overbrace
underbrace substack limits nolimits displaystyle textstyle scriptstyle
scriptscriptstyle ensuremath mbox hbox vbox phantom hphantom vphantom smash
quad qquad enspace thinspace medspace thickspace hspace vspace kern mkern
noindent indent par linebreak newline pagebreak newpage clearpage centering
multicolumn multirow arraystretch tabcolsep hline cline vline leq geq le ge
ne neq equiv sim simeq cong approx asymp propto ll gg lesssim gtrsim
subset supset subseteq supseteq subsetneq supsetneq subsetneqq supsetneqq
in notin ni owns not neg land lor wedge vee cap cup bigcap bigcup setminus
smallsetminus emptyset varnothing forall exists nexists therefore because
to gets mapsto longmapsto hookrightarrow hookleftarrow rightarrow leftarrow
longrightarrow longleftarrow leftrightarrow longleftrightarrow Rightarrow
Leftarrow Longrightarrow Longleftarrow Leftrightarrow Longleftrightarrow
implies impliedby iff nearrow searrow swarrow nwarrow uparrow downarrow
Uparrow Downarrow updownarrow Updownarrow rightrightarrows leftleftarrows
rightrightarrows rightleftarrows leftrightarrows twoheadrightarrow
twoheadleftarrow rightsquigarrow leadsto dashrightarrow dashleftarrow
rightarrowtail leftarrowtail circlearrowleft circlearrowright xrightarrow
xleftarrow xmapsto xhookrightarrow xhookleftarrow xRightarrow xLeftarrow
relbar Relbar mid parallel perp models vdash dashv Vdash Vvdash smile frown
longleftrightarrow multimap colon coloneqq eqcolon triangleleft triangleright
unlhd unrhd trianglelefteq trianglerighteq times otimes oplus odot oslash ominus
bigotimes bigoplus bigodot coprod amalg sqcap sqcup bigsqcup circ bullet cdot
ast star dagger ddagger pm mp div cdots ldots dots vdots ddots bot top infty
partial nabla prime backprime sum prod int iint iiint oint sqsubset sqsupset
sqsubseteq sqsupseteq lceil rceil lfloor rfloor langle rangle lvert rvert
lVert rVert vert Vert lbrace rbrace backslash ell hbar imath jmath Re Im
aleph beth gimel daleth wp angle measuredangle sphericalangle triangle
square Box Diamond diamondsuit heartsuit clubsuit spadesuit checkmark
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau
upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma
Upsilon Phi Psi Omega min max inf sup lim liminf limsup injlim projlim
varinjlim varprojlim colim det dim deg ker hom Hom coker im image rank tr
sin cos tan cot sec csc log ln exp gcd lcm Pr arg diag id Spec Spf Proj
ar arrow arrows node draw path fill filldraw coordinate clip foreach scope
pgfmathsetmacro tikzset tikzcdset matrix pgfextra pgfsetlinewidth
mathrm mathchar char romannumeral pmod bmod mod pod label ref eqref tag notag
nonumber newcommand renewcommand providecommand def let relax protect
textbackslash textasciitilde textasciicircum textbar textless textgreater
textdegree textquotedblleft textquotedblright textquoteleft textquoteright
guillemotleft guillemotright oe OE ae AE aa AA o O ss S P copyright
upshape slshape scshape strut mathstrut null hfill vfill rule raisebox
shortstack rotatebox resizebox scalebox multimapsto qedsymbol qed
cdotp ldotp mathbin mathrel mathord mathop mathopen mathclose mathpunct
mathinner bmod pmod cfrac genfrac displaybreak allowdisplaybreaks
intertext shortintertext cases aligned gathered split smallmatrix
textcircled item bigwedge fbox d
textsuperscript textsubscript'''.split())
FORBIDDEN = {'documentclass', 'usepackage', 'includegraphics', 'input', 'include'}


def clean_tex(text: str) -> str:
    """Remove comments without treating escaped percent signs as comments."""
    lines = []
    for line in text.splitlines():
        for i, char in enumerate(line):
            if char == '%':
                backslashes = len(line[:i]) - len(line[:i].rstrip('\\'))
                if backslashes % 2 == 0:
                    line = line[:i]
                    break
        lines.append(line)
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path,
                        default=Path(__file__).resolve().parents[1])
    parser.add_argument('--partial', action='store_true',
                        help='allow missing pages, final files, audit/freeze records')
    args = parser.parse_args()
    root = args.root.resolve()
    errors, warnings = [], []
    pages = {}

    def check_tex(name: str, text: str) -> str:
        source = clean_tex(text)
        stack = []
        for match in re.finditer(r'\\(?:[A-Za-z@]+|[^\n])|[{}]', source):
            token = match.group()
            line = source.count('\n', 0, match.start()) + 1
            if token == '{':
                stack.append(line)
            elif token == '}':
                if stack:
                    stack.pop()
                else:
                    errors.append(f'{name}:{line}: unmatched closing brace')
        if stack:
            errors.append(f'{name}: unmatched opening braces at lines {stack}')
        environments = []
        for match in re.finditer(r'\\(begin|end)\s*\{([^{}]+)\}', source):
            action, env = match.groups()
            if action == 'begin':
                environments.append(env)
            elif not environments or environments.pop() != env:
                errors.append(f'{name}: mismatched environment end {env!r}')
        if environments:
            errors.append(f'{name}: unclosed environments {environments}')
        # Tokenize control symbols as well as control words, so ``\\\\d`` is
        # a row separator followed by the letter d, not an occurrence of \\d.
        commands = {match.group()[1:]
                    for match in re.finditer(r'\\(?:[A-Za-z@]+|[^\n])', source)
                    if len(match.group()) > 1 and match.group()[1].isalpha()}
        for command in sorted(commands & FORBIDDEN):
            errors.append(f'{name}: forbidden fragment command \\{command}')
        unknown = commands - STANDARD - EDITORIAL - FORBIDDEN
        if unknown:
            warnings.append(f'{name}: review unclassified commands: ' +
                            ', '.join('\\' + c for c in sorted(unknown)))
        if re.search(r'\\illegible\s*\{(?!\d+\s*\})', source):
            errors.append(f'{name}: illegible macro needs a word-count integer')
        if re.search(r'\\begin\s*\{document\}', source):
            errors.append(f'{name}: document environment in fragment')
        return source

    expected_names = {f'MPL_131_131_scan{scan:03d}.tex' for scan in SCANS}
    for path in (root / 'pages').glob('*.tex'):
        if path.name not in expected_names:
            errors.append(f'Unexpected page filename: {path.name}')
    for scan in SCANS:
        path = root / 'pages' / f'MPL_131_131_scan{scan:03d}.tex'
        if not path.exists():
            if not args.partial:
                errors.append(f'Missing page: {path.relative_to(root)}')
            continue
        pages[scan] = path.read_text(encoding='utf-8')
        source = check_tex(path.name, pages[scan])
        markers = re.findall(r'\\scanpage\s*\{\s*(\d+)\s*\}', source)
        if markers != [str(scan)]:
            errors.append(f'{path.name}: scan markers {markers!r}, expected [{scan}]')
        cotes = re.findall(r'\\cotefile\s*\{\s*([^{}]+?)\s*\}', source)
        if cotes != (['131'] if scan == SCANS[0] else []):
            errors.append(f'{path.name}: cotefile marker misplaced or incorrect: {cotes}')
        start = (r'\cotefile{131}' if scan == SCANS[0] else r'\scanpage{' + str(scan) + '}')
        if not source.lstrip().startswith(start):
            errors.append(f'{path.name}: expected first substantive macro {start}')

    combined = root / 'MPL_131_transcription.tex'
    if combined.exists():
        actual = combined.read_text(encoding='utf-8')
        expected = ''.join(pages[n] for n in SCANS if n in pages)
        if actual != expected:
            errors.append('Combined transcription differs from exact ordered concatenation of page files')
    elif not args.partial:
        errors.append('Missing MPL_131_transcription.tex')

    inventory = root / 'MPL_131_inventory.csv'
    count = Counter()
    if inventory.exists():
        with inventory.open(encoding='utf-8-sig', newline='') as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != FIELDS:
                errors.append(f'Inventory header differs from required schema: {reader.fieldnames}')
            seen = set()
            for line, row in enumerate(reader, start=2):
                label = f'inventory row {line}'
                if None in row or any(value is None for value in row.values()):
                    errors.append(f'{label}: malformed CSV row')
                    continue
                try:
                    scan = int(row.get('scan', ''))
                except ValueError:
                    errors.append(f'{label}: nonnumeric scan')
                    continue
                count[scan] += 1
                if row.get('cote') != '131' or scan not in SCANS:
                    errors.append(f'{label}: unexpected cote/scan')
                if row.get('sheet_kind') not in SHEET_KINDS:
                    errors.append(f'{label}: invalid sheet_kind')
                if row.get('kind') not in KINDS:
                    errors.append(f'{label}: invalid kind')
                if row.get('transcribed') != 'yes':
                    errors.append(f'{label}: transcribed is not yes')
                for field in ('element', 'position', 'first_words_or_objects'):
                    if not row.get(field, '').strip():
                        errors.append(f'{label}: empty {field}')
                key = (scan, row.get('element'))
                if key in seen:
                    errors.append(f'{label}: duplicate page element identifier {key}')
                seen.add(key)
        for scan in (pages if args.partial else SCANS):
            if not count[scan]:
                errors.append(f'scan {scan:03d}: no inventory elements')
        for scan in count:
            if scan not in pages:
                errors.append(f'scan {scan:03d}: inventory exists without page file')
    elif not args.partial:
        errors.append('Missing MPL_131_inventory.csv')

    for filename in ('MPL_131_doubts.md', 'MPL_131_notes.md', 'progress.log'):
        if not (root / filename).is_file() and not args.partial:
            errors.append(f'Missing {filename}')

    log_path = root / 'progress.log'
    hash_count = 0
    if log_path.exists():
        log = log_path.read_text(encoding='utf-8')
        freeze = log.find('transcription frozen ')
        context = log.find('context opened ')
        if context >= 0 and (freeze < 0 or context < freeze):
            errors.append('Context-open record precedes transcription freeze record')
        if not args.partial:
            for scan in SCANS:
                if not re.search(rf'(?m)^131 scan {scan:03d} done .+$', log):
                    errors.append(f'Missing page-done log record: scan {scan:03d}')
                if not re.search(rf'(?m)^scan {scan:03d} audited .+$', log):
                    errors.append(f'Missing audit log record: scan {scan:03d}')
            if freeze < 0:
                errors.append('Missing transcription frozen log record')
        hashes = {}
        for line in log.splitlines():
            match = re.match(r'^(?:sha256\s+)?([0-9a-fA-F]{64})\s+[* ]?(.+?)\s*$', line, re.I)
            reverse = re.match(r'^sha256\s+(.+?)\s+([0-9a-fA-F]{64})\s*$', line, re.I)
            if match:
                digest, name = match.groups()
            elif reverse:
                name, digest = reverse.groups()
            else:
                continue
            name = name.strip().strip('`')
            target = (root / name).resolve()
            if root not in target.parents:
                errors.append(f'Hash path outside deliverable directory: {name}')
                continue
            if name in hashes and hashes[name] != digest.lower():
                errors.append(f'Conflicting frozen hashes for {name}')
            hashes[name] = digest.lower()
            if not target.is_file():
                errors.append(f'Frozen hash names missing file: {name}')
            elif hashlib.sha256(target.read_bytes()).hexdigest() != digest.lower():
                errors.append(f'Frozen SHA-256 mismatch: {name}')
        hash_count = len(hashes)
        if freeze >= 0:
            expected_hashes = {str(Path('pages') / name) for name in expected_names}
            expected_hashes.add('MPL_131_transcription.tex')
            for name in sorted(expected_hashes - hashes.keys()):
                errors.append(f'Missing frozen SHA-256 record: {name}')
        elif not hashes:
            warnings.append('No frozen SHA-256 records found; comparison not performed')

    for message in warnings:
        print('WARNING:', message)
    for message in errors:
        print('ERROR:', message)
    print(f'Checked {len(pages)}/{len(SCANS)} pages; {sum(count.values())} inventory rows; '
          f'{hash_count} recorded hashes; {len(errors)} errors; {len(warnings)} warnings.')
    print('These structural checks cannot establish reading accuracy or visual completeness.')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
