#!/usr/bin/env python3
"""Assemble the post-freeze research register; never touch transcription files."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REC = ROOT / 'records'
KEYS = {
    'H': 'Haar|ultrafiltre|mesures invariantes',
    'D': 'injecti[fv]|injective hull|K/A|anneau principal|dualit',
    'F': 'Fitting|Filting|déterminantiel|annulateur',
    'T': 'différente|codifférente|conducteur|trace',
    'S': 'socle|primaire|irréductible',
    'V': 'puissance symbolique|pseudo.inversible|degré|déterminantiel',
    'P': 'plat|platitude|annulateur|nilpotent',
    'M': 'monogène|monogene|homogènes|discriminant|polynôme',
    'B': 'Tribu|n°57|Décembre 62|397|398|392',
}

front = (REC / 'notes_frontmatter.md').read_text()
guide = '''## Item register

The register contains **129 separately identified items**: F01–F55 on the handwritten argument, C01–C10 on contextual and published comparisons, and RT01–RT64 on the reused typescripts. Each item distinguishes a source claim, a withdrawn statement, a reading question, or an editorial implication/example; the short prose body is kept separate from its witness, context and status metadata. Mathematical notation in explanatory quotes is rendered typographically in these notes only; the diplomatic source remains unchanged.

**Principal results to inspect first:** F31 (the author's boundary-shift question); F33–F35 and F51 (the determinant normalizations); F23–F24 (normalized Frobenius and the projective-plane test); F43–F46 and F55 (the curve defect, its support, and derived-image scope); RT09–RT11 (symbolic degree versus length); RT19–RT21 (locality in the socle argument); RT35–RT36 (flatness and the meaning of radical); RT39 (signed relative divisors); C04–C06 (the bounded Oda comparisons).

The per-item searches of CT, CN, CD and RS were actually run and recorded in `records/item_context_searches.md`. A keyword hit is not treated as a matching assertion; the comparison field states the relevant passage and its limits. The extended research records preserve calculations and bibliographic checks, while this register is the consolidated statement of the findings. No novelty, independent archival dating, or blanket verification of an earlier research return is claimed.

'''
core = (REC / 'core_notes.md').read_text()
context = (REC / 'context_items.md').read_text()
typed = (REC / 'reused_items.md').read_text()
typed = typed.replace('# Research register on the reused typescripts', '## G. Reused typescripts')
typed = typed.replace('## Scope, evidence, and context status', '### Scope, evidence, and context status')
typed = re.sub(r'^## (?!G\.)(.+)$', r'### \1', typed, flags=re.M)
typed = re.sub(r'^### RT', '#### RT', typed, flags=re.M)

def enrich(match):
    heading, block = match.group(1), match.group(2)
    meta = re.search(r'\*\*Context:\*\*\s*([^.;\n]+)', block)
    if meta is None:
        raise ValueError('Missing context key: ' + heading)
    keys = list(dict.fromkeys(re.findall(r'\b[HDFTSVPMB]\b', meta.group(1))))
    if not keys:
        raise ValueError('No context keys: ' + heading)
    query = '|'.join(KEYS[k] for k in keys)
    if 'RT61 ' in heading:
        query += '|Chern'
    first, rest = block.split('\n\n', 1)
    first += f' **Context query:** `{query}`.'
    if re.search(r'\bR01\b|§136', first):
        first = re.sub(r'(?<!\S)R01\b', 'MPL_15_195-228+18_002-017 R01', first)
        first = first.replace('register §136', 'register MPL_15_195-228+18_002-017 §136')
    else:
        first += ' **RS:** no directly matching mathematical entry; the general provenance and negative-scope limits in this section apply.'
    return heading + first + '\n\n' + rest

typed = re.sub(r'(?ms)(^#### RT\d+ — [^\n]+\n\n)(.*?)(?=^#### RT\d+|^### |\Z)', enrich, typed)
refs = (REC / 'references.md').read_text()
text = front + guide + core + '\n\n' + context + '\n\n' + typed + '\n\n' + refs
ids = re.findall(r'^#{3,4} ((?:F|C|RT)\d+) — ', text, re.M)
assert len(ids) == 129 and len(set(ids)) == 129, (len(ids), len(set(ids)))
assert 'Research work is in progress' not in text
assert len(re.findall(r'\*\*Context query:\*\* `', text)) == 129
(ROOT / 'MPL_60_002-035_notes.md').write_text(text)
print(f'Assembled {len(ids)} notes, {len(text.split())} words, {len(text.encode())} bytes')
