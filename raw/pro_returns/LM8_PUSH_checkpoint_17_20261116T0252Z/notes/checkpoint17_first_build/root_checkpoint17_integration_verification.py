#!/usr/bin/env python3
"""Bind reviewed editorial integrations to the complete audited proofs."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
rows = []

def read(name):
    return (root / name).read_text()

def section(text, heading):
    start = text.index('\\subsection{' + heading + '}')
    end = text.index('\\end{proof}', start) + len('\\end{proof}')
    return text[start:end].strip()

def equal(label, left, right):
    assert left == right, label
    rows.append({'check': label, 'status': 'PASS',
                 'compared_text_sha256': hashlib.sha256(left.encode()).hexdigest()})

c = read('sections/C.tex')
heading = 'The actual framed images at levels twenty-four and sixty'
equal('C49 canonical equals the fully audited proposed full-character integration',
      section(c, heading), section(read('notes/pbc_C49_full_character_proposed.tex'), heading))
heading = 'An explicit finite outer detector from two peripheral coset modules'
expected = read('notes/pbc_explicit_outer_detector_draft.tex').replace(
    '{C.50}{Open}', '{C.50}{Proved}').replace('\\begin{proof}[Complete candidate proof]', '\\begin{proof}')
equal('C50 canonical equals the audited draft after status/proof-heading edits',
      section(c, heading), section(expected, heading))

heading = 'A genus-two intermediate with a noncyclic derived closure'
expected = read('notes/fgh_A80_draft.tex').replace('{A.80}{Open}', '{A.80}{Proved}')
for key in ('frontier', 'map', 'prym'):
    expected = expected.replace(f'notes/fgh_wreath64_{key}_certificate.py', f'code/a_wreath64_{key}.py')
    equal('A80 canonical ' + key + ' source is byte-identical to audited source',
          read(f'code/a_wreath64_{key}.py'), read(f'notes/fgh_wreath64_{key}_certificate.py'))
    equal('A80 canonical ' + key + ' complete output matches audited output',
          read(f'code/a_wreath64_{key}.json'), read(f'notes/fgh_wreath64_{key}_certificate.json'))
expected = expected.replace('Their JSON and stdout are retained. The additional exact',
                            'Their JSON and stdout are retained; the read-only aggregate replay is\n\\path{code/a_wreath64_genus_two.py}. The additional exact')
equal('A80 canonical equals the fully audited proof after approved path/status edits',
      section(read('sections/A_wreath64_genus_two.tex'), heading), section(expected, heading))

heading = 'Double covers with a non-CM elliptic Prym'
expected = read('notes/fgh_A81_draft.tex').replace('{A.81}{Open}', '{A.81}{Proved}')
equal('A81 canonical equals the final fully audited proof after status edit',
      section(read('sections/A_noncm_prym_double_covers.tex'), heading), section(expected, heading))

start = '\\paragraph{An exact extension by one order-five factor.}'
end = 'This closes the all-depth elementary-divisor calculation.'
smith = read('notes/de_ordinary_kernel_smith_addendum.tex')
smith = smith[smith.index(start):smith.index(end)]
smith = re.sub(r'D93S\.(\d+)', lambda m: 'D.93.' + str(3 if int(m[1]) == 1 else int(m[1]) + 20), smith)
canonical = read('sections/D_alexander_ordinary_finite_kernels.tex')
canonical_smith = canonical[canonical.index(start):canonical.index(end)]
equal('D93 entire integrated Smith proof equals the audited addendum after tag renumbering',
      smith, canonical_smith)

for original, current in (
    ('notes/de_ordinary_unbounded_finite_kernel_certificate.json', 'code/de_ordinary_finite_kernel.json'),
    ('notes/de_ordinary_kernel_smith_certificate.json', 'code/de_ordinary_kernel_smith.json')):
    a, b = json.loads(read(original)), json.loads(read(current))
    for obj in (a, b):
        for key in ('candidate', 'statement', 'source_sha256'):
            obj.pop(key, None)
    assert a == b, current
    rows.append({'check': 'D93 full canonical mathematical output equality: ' + current,
                 'status': 'PASS', 'excluded_metadata': ['candidate', 'statement', 'source_sha256']})

result = {'status': 'PASS', 'checks': rows,
          'scope': 'Exact integration comparisons supplement the complete root proof/source/code audits. No new numerical theorem is inferred from editorial equality.'}
(root / 'notes/root_checkpoint17_integration_verification.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
