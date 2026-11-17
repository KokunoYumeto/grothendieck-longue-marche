#!/usr/bin/env python3
"""Assemble reviewed research components; never modify frozen transcription."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research'

def read(name):
    return (RESEARCH / name).read_text(encoding='utf-8').strip()

def without_title(s):
    return re.sub(r'^# [^\n]*\n+', '', s, count=1)

front = read('notes_front.md')
algebra = without_title(read('algebra_notes.md'))
algebra = algebra.replace('## Status and conventions', '### Source and context conventions', 1)
algebra = '## A. Quadratic algebras, relative norms and three-cover configurations\n\n' + algebra

extensions = without_title(read('extension_notes.md'))
bnotes, tail = extensions.split('## Standing register of author-marked checks, qualifications and unfinished assertions', 1)
bstanding, bscope = tail.split('## Register-scope checklist for integration', 1)
bnotes = re.sub(r'^## (B\d\d —)', r'### \1', bnotes, flags=re.M)
bnotes = '## B. Products and comparisons of χ-split extensions\n\n' + bnotes.strip()

astanding = without_title(read('algebra_unverified_steps.md'))
astanding = re.sub(r'^(#{2,5}) ', lambda m: '#'+m.group(1)+' ', astanding, flags=re.M)
standing = ('## E. Standing question: author-marked checks and unfinished steps\n\n'
            'Authorial reservations, cancelled attempts and completed local checks are distinguished below from editorial reading doubts. The A/B/D item references supply the individual context searches and comparisons.\n\n'
            '### E.1. Mathematical scans 097–122\n\n' + astanding + '\n\n'
            '### E.2. Extension worksheets 124–144\n\n' + bstanding.strip() + '\n\n'
            + read('standing_typed.md'))

catalog = read('enumerations.md')
catalog = re.sub(r'^(#{1,5}) ', lambda m: '#'+m.group(1)+' ', catalog, flags=re.M)
catalog = re.sub(r'^## [^\n]*', '## G. Tables and enumerations', catalog, count=1)

ledger = read('results_ledger.md').replace('## G. Changes', '## H. Changes', 1).replace('## H. Reference', '## I. Reference', 1)
ledger = ledger.replace('\n## I. Reference', '\n### H.1. Components of the extension-product claim\n\n' + bscope.strip() + '\n\n## I. Reference', 1)

parts = [front, algebra, bnotes, read('root_notes.md'), standing,
         read('standing_archival.md'), catalog, ledger]
result = '\n\n'.join(parts) + '\n'
target = ROOT / 'MPL_84_097-145_notes.md'
target.write_text(result, encoding='utf-8')
ids = re.findall(r'^### ([ABCDP]\d{2}) —', result, re.M)
assert len(ids) == len(set(ids)) == 100, (len(ids), len(set(ids)))
print(f'Assembled {len(ids)} short research items; {len(result.split())} whitespace-separated words; {target.name}')
