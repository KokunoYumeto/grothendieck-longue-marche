#!/usr/bin/env python3
"""Preserve and repair three typesetting-only passages after build eight-six."""
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parent.parent


def digest(text):
    return sha256(text.encode()).hexdigest()


def main():
    changes = [
        ('sections/D_v4_refinement_agent.tex',
         r'{m_\delta\choose2}', r'\binom{m_\delta}{2}',
         'Use the amsmath binomial command for the identical coefficient.'),
        ('sections/E_a6_joint_agent.tex',
         r'\subsection{The exact common $A_6$ and double-cover source and its full boundary fibre}',
         r'\subsection{The exact common \texorpdfstring{$A_6$}{A6} and double-cover source and its full boundary fibre}',
         'Give the bookmark the literal A6 text while retaining the displayed mathematical heading.'),
        ('sections/E_a6_uniform_agent.tex',
         r'\subsection{The full $A_6$ refinement through the entire congruence system}',
         r'\subsection{The full \texorpdfstring{$A_6$}{A6} refinement through the entire congruence system}',
         'Give the bookmark the literal A6 text while retaining the displayed mathematical heading.')]
    output = ROOT / 'research/checkpoint08_sixth_format_repairs.json'
    assert not output.exists()
    updates, records = {}, []
    for name, old, new, reason in changes:
        path = ROOT / name
        text = path.read_text()
        frozen = (ROOT / 'build/checkpoint08_sixth_complete' / name).read_text()
        assert text == frozen and text.count(old) == 1
        changed = text.replace(old, new)
        records.append({'source': name, 'old_passage': old, 'new_passage': new,
                        'old_sha256': digest(text), 'new_sha256': digest(changed),
                        'reason': reason,
                        'complete_old_source': 'build/checkpoint08_sixth_complete/' + name})
        updates[path] = changed
    output.write_text(json.dumps({'before': {'overfull_boxes': 0,
                                            'amsmath_warnings': 1,
                                            'bookmark_warnings': 6},
                                 'mathematical_formulas_and_proofs_retained': True,
                                 'repairs': records}, indent=2) + '\n')
    for path, text in updates.items():
        path.write_text(text)
    print(output.read_text())


if __name__ == '__main__':
    main()
