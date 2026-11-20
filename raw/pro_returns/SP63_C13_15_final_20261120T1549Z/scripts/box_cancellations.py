"""Box paragraph-level cancelled arguments without changing their contents.

No compilation is performed. Existing PREAMBLE.tex macros remain unchanged.
"""
from workflow import ROOT, assemble, utc
import re

def argument_end(text, opening):
    depth = 1
    i = opening + 1
    while i < len(text):
        if text[i] == '\\':
            if i + 1 < len(text) and text[i + 1] in '{}%':
                i += 2
                continue
        elif text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError('unbalanced macro argument')

rows = []
for p in sorted((ROOT / 'pages').glob('*.tex')):
    t = p.read_text()
    replacements = []
    start = 0
    while True:
        a = t.find(r'\deleted{', start)
        if a < 0:
            break
        opening = a + len(r'\deleted')
        end = argument_end(t, opening)
        body = t[opening + 1:end]
        if any(x in body for x in [r'\[', r'\diagram{', r'\figure{', '\n\n']):
            assert not body.startswith(r'\mbox{'), p.name
            boxed = '\\par\\noindent\n\\deleted{\\mbox{\\begin{minipage}[c]{\\linewidth}\n' + body + '\n\\end{minipage}}}\n\\par'
            replacements.append((a, end + 1, boxed))
            rows.append((p.name, t[:a].count('\n') + 1, body.count(r'\deleted{')))
            start = end + 1
        else:
            start = opening + 1
    for a, b, replacement in reversed(replacements):
        t = t[:a] + replacement + t[b:]
    p.write_text(t)

doc = '# Structural repairs without compilation\n\n'
doc += ('The supplied deleted macro passes text to ulem strikeout. Paragraphs, displayed formulas, '
        'and the supplied paragraph-level diagram macro need a paragraph container inside that argument. '
        'The listed complete outer arguments were placed, byte-for-byte, inside a standard minipage '
        'and mbox within the existing deleted wrapper. Every nested local deletion, insertion, '
        'formula, and diagram remains inside the same outer cancellation boundary. This is a syntax '
        'change and adds no collation row. Each block is now an unbreakable box with the outer '
        'strike crossing its middle. It does not attempt to reproduce the precise slope of a '
        'manuscript cancellation. No TeX compilation or rendered-layout check was performed.\n\n')
doc += '| Page file | Starting line before repair | Nested local deletions preserved |\n|---|---|---|\n'
doc += ''.join(f'| {name} | {line} | {n} |\n' for name, line, n in rows)
doc += ('\nThe small TikZ fragments in math undersets on scans 173 and 177 use a text box '
        'instead of the paragraph-level figure wrapper; their drawn paths are unchanged.\n')
(ROOT / 'STRUCTURAL_REPAIRS.md').write_text(doc)
assemble()
with (ROOT / 'progress.log').open('a') as f:
    f.write(f'boxed {len(rows)} paragraph-level cancellation arguments without changing their contents ' + utc() + '\n')
print(rows)
