#!/usr/bin/env python3
"""Prepare syntax-only review suggestions and a scratch compilation mirror.

This script NEVER writes to pages/. It records a unified patch for review,
and writes proposed versions only to the sibling scratch texqa-cache/mirror.
No source wording or manuscript reading is inferred by this utility.
"""
from pathlib import Path
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent
MIRROR = ROOT.parent / 'texqa-cache' / 'mirror'

FIXES = {
 '043': [('"(i,i\')"', '"{(i,i\')}"', 'Protect the comma in a TikZ arrow label.')],
 '045': [(r'\uline{dans $Ab$}', r'\text{\uline{dans $Ab$}}', 'Put prose and its inline math in a text box within display math.')],
 '046': [(r'\textcircled{\scriptsize$i\geq0$}', r'\text{\textcircled{\scriptsize$i\geq0$}}', 'Supply text mode for the circled textual annotation inside display math.')],
 '047': [(r'\inserted{$(L_i\varphi)(X)=0$}', r'\inserted{(L_i\varphi)(X)=0}', 'Remove nested math delimiters from a display-math insertion.'),
         (r'\deleted{Ab}\inserted{$M$}', r'\deleted{Ab}\inserted{M}', 'Remove nested math delimiters from a display-math insertion.')],
 '048': [(r'\deleted{\unsure{plat}}\inserted{$\otimes_k$ plat}', r'\text{\deleted{\unsure{plat}}\inserted{$\otimes_k$ plat}}', 'Put prose and its inline math in a text box within display math.'),
         (r'\mathrm{unité}', r'\text{unité}', 'Use text mode for the accented word; math-mode accent handling emits a warning.')],
 '049': [(r'\unsure{\mathcal G} des', r'$\unsure{\mathcal G}$ des', 'Supply math mode for the existing script letter.')],
 '051': [(r'\arrow[d,phantom,"\text{proj}" description]&l_\bullet\arrow[r]&0', r'\arrow[d,phantom,"\text{proj}" description]&l_\bullet\arrow[r]&0\\' + '\n' + r'&&{}&&', 'Create the blank destination node required by the invisible label-placement arrow.')],
 '055': [(r'\textcircled{' + str(i) + '}&', r'\text{\textcircled{' + str(i) + '}}&', 'Supply text mode for the circled table label inside display math.') for i in (1, 2, 3)],
}


def braced_range(text, start):
    """Return the content and closing offset of the braced group at start."""
    assert text[start] == '{'
    depth, i = 1, start + 1
    while i < len(text):
        if text[i] == '\\':
            i += 2
            continue
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if not depth:
                return start + 1, i
        i += 1
    raise ValueError('Unclosed braced argument')


def rotatebox_ranges(text):
    ranges = []
    for match in re.finditer(r'\\rotatebox\s*\{', text):
        _, first_end = braced_range(text, match.end() - 1)
        second_start = first_end + 1
        while text[second_start].isspace():
            second_start += 1
        if text[second_start] == '{':
            ranges.append(braced_range(text, second_start))
    return ranges


def repair_rotated_matrices(text):
    ranges = rotatebox_ranges(text)
    pattern = re.compile(r'\\begin\{tikzcd\}(\[[^\]]*\])?(.*?)\\end\{tikzcd\}', re.S)
    changes = []
    for match in list(pattern.finditer(text))[::-1]:
        if not any(a <= match.start() < b for a, b in ranges):
            continue
        if 'ampersand replacement=' in (match.group(1) or ''):
            continue
        options = match.group(1)
        new_options = '[ampersand replacement=\\&' + (',' + options[1:-1] if options else '') + ']'
        new_body = re.sub(r'(?<!\\)&', r'\\&', match.group(2))
        replacement = r'\begin{tikzcd}' + new_options + new_body + r'\end{tikzcd}'
        changes.append({'line': text.count('\n', 0, match.start()) + 1,
                        'reason': 'Use explicit matrix separators inside the already-tokenized rotatebox argument.'})
        text = text[:match.start()] + replacement + text[match.end():]
    return text, changes


def replace_unfixed(text, old, new):
    """Do not wrap an occurrence already inside the complete proposed form."""
    protected = [(m.start(), m.end()) for m in re.finditer(re.escape(new), text)]
    matches = [m for m in re.finditer(re.escape(old), text)
               if not any(a <= m.start() < b for a, b in protected)]
    lines = [text.count('\n', 0, m.start()) + 1 for m in matches]
    for match in reversed(matches):
        text = text[:match.start()] + new + text[match.end():]
    return text, lines


def main():
    MIRROR.mkdir(parents=True, exist_ok=True)
    diff, report, manifest = [], [], {}
    for path in sorted((ROOT / 'pages').glob('*.tex')):
        original_bytes = path.read_bytes()
        original = original_bytes.decode('utf-8')
        updated = original
        scan = re.search(r'scan(\d+)\.tex$', path.name).group(1)
        changes = []
        for old, new, reason in FIXES.get(scan, []):
            updated, lines = replace_unfixed(updated, old, new)
            changes.extend({'line': line, 'reason': reason, 'old': old, 'new': new}
                           for line in lines)
        updated, matrix_changes = repair_rotated_matrices(updated)
        changes += matrix_changes
        (MIRROR / path.name).write_text(updated)
        manifest[path.name] = {'original_sha256': hashlib.sha256(original_bytes).hexdigest(),
                               'proposed_sha256': hashlib.sha256(updated.encode('utf-8')).hexdigest()}
        if updated != original:
            label = 'pages/' + path.name
            diff.extend(difflib.unified_diff(original.splitlines(keepends=True),
                                           updated.splitlines(keepends=True),
                                           fromfile='a/' + label, tofile='b/' + label))
            report.append({'scan': scan, 'file': label, 'changes': changes})
    (ROOT / 'records' / 'suggested_syntax_fixes.patch').write_text(''.join(diff))
    (ROOT / 'records' / 'suggested_syntax_fixes.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    (MIRROR.parent / 'proposal_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Suggested patch prepared for', len(report), 'pages; originals untouched.')
    print('Scratch mirror:', MIRROR)
    return manifest


if __name__ == '__main__':
    main()
