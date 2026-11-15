#!/usr/bin/env python3
"""Prepare three explicit TikZ-cd conversions for principal-reader review.

This script reads existing TeX markup only. It does not read any manuscript
image or context source, infer a manuscript reading, or edit the live pages.
Every object/label expression is retained. Existing right-arrow and plain-line
commands map to right-arrow and no-head TikZ-cd edges; brace coverage is recorded
explicitly for the long chain. Original and proposed bodies are preserved in
the review manifest, and proposed full-page copies live only in scratch.
"""
from pathlib import Path
import difflib
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
MIRROR = ROOT.parent / 'texqa-cache' / 'remaining-diagram-proposal'

CONVERSIONS = {
    '051': {
        'old': r'''\diagram{\fbox{$\begin{gathered}F\otimes\xi\longrightarrow F\otimes\eta\end{gathered}$}}''',
        'new': r'''\diagram{\fbox{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
F\otimes\xi\arrow[r]\&F\otimes\eta
\end{tikzcd}}}''',
        'objects': [r'F\otimes\xi', r'F\otimes\eta'],
        'edges': [{'from': 1, 'to': 2, 'old': r'\longrightarrow', 'new': r'\arrow[r]'}],
        'box': 'Existing fbox retained around the complete diagram.',
    },
    '052': {
        'old': r'''\diagram{\fbox{$\beta_i:P_i\longrightarrow L'_i$}}''',
        'new': r'''\diagram{\fbox{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
\beta_i:P_i\arrow[r]\&L'_i
\end{tikzcd}}}''',
        'objects': [r'\beta_i:P_i', r"L'_i"],
        'edges': [{'from': 1, 'to': 2, 'old': r'\longrightarrow', 'new': r'\arrow[r]'}],
        'box': 'Existing fbox retained. The beta_i colon prefix stays at the left of P_i on the same baseline.',
    },
    '062': {
        'old': r'''\diagram{$0\mathbin{\text{---}}\overbrace{k\longrightarrow\Theta\longrightarrow k[1]}
\mathbin{\underbrace{\longrightarrow\Theta[1]\mathbin{\text{---}}k[2]}}
\mathbin{\text{---}}\Theta[2]\mathbin{\text{---}}k[3]\longrightarrow\cdots$}''',
        'new': r'''\diagram{\begin{tikzcd}[column sep=small,
execute at end picture={
\draw[decorate,decoration={brace,amplitude=3pt}]
([yshift=3pt]\tikzcdmatrixname-1-2.north west)--([yshift=3pt]\tikzcdmatrixname-1-4.north east);
\draw[decorate,decoration={brace,amplitude=3pt,mirror}]
([yshift=-4pt]\tikzcdmatrixname-1-4.south east)--([yshift=-4pt]\tikzcdmatrixname-1-6.south east);
}]
0\arrow[r,dash]&k\arrow[r]&\Theta\arrow[r]&k[1]\arrow[r]&\Theta[1]\arrow[r,dash]&k[2]\arrow[r,dash]&\Theta[2]\arrow[r,dash]&k[3]\arrow[r]&\cdots
\end{tikzcd}}''',
        'objects': ['0', 'k', r'\Theta', 'k[1]', r'\Theta[1]', 'k[2]', r'\Theta[2]', 'k[3]', r'\cdots'],
        'edges': [{'from': a, 'to': a+1,
                   'old': r'\mathbin{\text{---}}' if a in (1, 5, 6, 7) else r'\longrightarrow',
                   'new': r'\arrow[r,dash]' if a in (1, 5, 6, 7) else r'\arrow[r]'}
                  for a in range(1, 9)],
        'braces': [
            {'kind': 'overbrace', 'coverage': 'From the left edge of object 2 (k) to the right edge of object 4 (k[1]); includes both intervening arrows.'},
            {'kind': 'underbrace', 'coverage': 'From the right edge of object 4 (k[1]) to the right edge of object 6 (k[2]); includes the outgoing arrow, Theta[1], the following plain line, and k[2].'}
        ],
        'rendering_dependency': 'The standard TikZ decorations.pathreplacing library draws the braces; it is loaded by the QA preamble.',
    },
}


def main():
    MIRROR.mkdir(parents=True, exist_ok=True)
    patch, manifest = [], []
    for scan, conversion in CONVERSIONS.items():
        path = ROOT / 'pages' / f'MPL_134-8_043-087_134-8_scan{scan}.tex'
        original_bytes = path.read_bytes()
        original = original_bytes.decode('utf-8')
        old, new = conversion['old'], conversion['new']
        if old not in original:
            if new in original:
                print('Scan', scan, 'already carries the proposed body; no patch needed.')
                (MIRROR / path.name).write_bytes(original_bytes)
                continue
            raise ValueError('Scan ' + scan + ' no longer matches the reviewed source body; principal-reader review is required.')
        if original.count(old) != 1:
            raise ValueError('Non-unique source body in scan ' + scan)
        for expression in conversion['objects']:
            if expression not in old or expression not in new:
                raise AssertionError('An object expression was not retained exactly')
        updated = original.replace(old, new, 1)
        if updated.replace(new, old, 1) != original:
            raise AssertionError('The explicit source-body substitution did not reverse exactly')
        (MIRROR / path.name).write_text(updated)
        record = dict(conversion)
        record.update({'scan': scan, 'file': 'pages/' + path.name,
                       'line': original.count('\n', 0, original.index(old)) + 1,
                       'source_sha256': hashlib.sha256(original_bytes).hexdigest(),
                       'proposed_sha256': hashlib.sha256(updated.encode('utf-8')).hexdigest(),
                       'all_object_label_expressions_retained': True,
                       'explicit_substitution_reverses_exactly': True})
        manifest.append(record)
        label = 'pages/' + path.name
        patch.extend(difflib.unified_diff(original.splitlines(keepends=True),
                                        updated.splitlines(keepends=True),
                                        fromfile='a/' + label, tofile='b/' + label))
    (ROOT / 'records' / 'proposed_remaining_diagrams.patch').write_text(''.join(patch))
    (ROOT / 'records' / 'proposed_remaining_diagrams.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print('Prepared', len(manifest), 'diagram conversions; live pages unchanged.')


if __name__ == '__main__':
    main()
