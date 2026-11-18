#!/usr/bin/env python3
"""Apply the final independent-review corrections to research files only.

Does not read or write the frozen LaTeX, inventory, or doubts.
"""
from pathlib import Path
import json
import re

R = Path(__file__).resolve().parent

def prose_spacing(s):
    s = re.sub(r'\b(scans?|pages?|lines|length|cote|Proposition|condition)(?=\d)', r'\1 ', s, flags=re.I)
    s = re.sub(r'\band(?=\d)', 'and ', s)
    return s

for group in ['inertia', 'torsors', 'local', 'root']:
    p = R / f'notes_{group}_candidates.json'
    entries = json.loads(p.read_text())
    for n in entries:
        key = n['key']
        if group == 'inertia' and key == 'M':
            n['kind'] = 'unpursued implication'
        if group == 'torsors' and key == 'T04':
            sentence = ' Only this qualified rigidity ingredient is independently rechecked here.'
            if sentence.strip() not in n['body']:
                n['body'] += sentence
        if group == 'torsors' and key == 'T09':
            n['body'] = n['body'].replace('The parent separately verified publisher metadata', 'Publisher metadata was separately verified')
            n['body'] = n['body'].replace("metadata was separately verified for Nori's", "metadata for Nori's")
            # Retain a grammatical third sentence, with the verification limit explicit.
            n['body'] = n['body'].replace("Publisher metadata for Nori's 1976, 1982, and 1983 publications;", "Publisher metadata for Nori's 1976, 1982, and 1983 publications was separately verified;")
            n['context'] = n['context'].replace('The contextual dating page125 is outside supplied evidence.', 'The contextual dating leaf is archive scan 125 (Hua p.124), outside the supplied evidence.')
            n['context'] = n['context'].replace('Parent separately verified publisher metadata;', 'Publisher metadata was separately verified;')
        if group == 'torsors' and key == 'T13':
            n['body'] = n['body'].replace('That is the mathematically intended reading used in the checks below', 'That is the repaired mathematical definition used in the checks below')
        if group == 'local' and key == 'L02':
            n['body'] = n['body'].replace('For connected \\(A\\),', 'For a nonzero ring \\(A\\) with connected spectrum,')
        if group == 'local' and key == 'L03':
            n['body'] = n['body'].replace('supplied in L02', 'supplied for N037 in proof P3')
        if group == 'local' and key == 'L04':
            n['body'] = n['body'].replace('under its stronger hypothesis', 'under its differently formulated hypothesis')
        if group == 'local' and key == 'L06':
            n['body'] = n['body'].replace('compatible maps to all the other local objects', 'compatible maps to \\(X(t)\\) for every \\(t\\in U\\)')
            sentence = (' The explanation that this extra hypothesis excludes the example uses quasi-finite étale neighborhood models in the intended geometric category; the full sufficiency of the source insertion is not proved here.')
            if sentence.strip() not in n['body']:
                n['body'] += sentence
        if group == 'local' and key == 'L07':
            n['context'] = n['context'].replace("those source pages were outside this agent's assigned source-reading subset.", 'scans 125 and 127 are outside the supplied package, while scan 126 is supplied.')
        if group == 'local' and key == 'L11':
            n['context'] = n['context'].replace('no direct source reading there by this agent.', 'no source image from that earlier scan is supplied.')
        if group == 'local' and key == 'L13':
            # A reading discrepancy is not itself a proof check of P4.
            n['check_refs'] = []
        if group == 'root' and key == 'R1':
            n['context'] = n['context'].replace('Le groupe fondamental local à deux branches', 'Le π₁ local le long de deux branches')
        if group == 'root' and key == 'R3':
            n['body'] = n['body'].replace('its usual étale surjectivity requires n invertible', 'the usual étale Kummer statement applies when n is invertible')
        for field in ['title', 'place', 'body', 'context', 'relation', 'reason']:
            if isinstance(n.get(field), str):
                n[field] = prose_spacing(n[field])
        if isinstance(n.get('reason'), str):
            n['reason'] = n['reason'].replace('the parent independently rechecked it', 'the argument received independent proof review')
        prefix = 'context/hua_project/29.modern.tex'
        if n['context'].startswith(prefix + ':'):
            n['context'] = n['context'].replace(prefix + ':', prefix + ' — Hua, modernised reading of cote 29:', 1)
        n['context'] = n['context'].replace('Hua, modernised reading of cote 29: Hua, modernised reading of cote 29,', 'Hua, modernised reading of cote 29,')
    p.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + '\n')

for name in ['notes_frontmatter.md', 'notes_endmatter.md']:
    p = R / name
    s = prose_spacing(p.read_text())
    for a,b in {
        'pages1,3,4':'pages 1, 3, 4', '5,6':'5, 6', '2,5,6':'2, 5, 6',
        'Pages1–67':'Pages 1–67', 'août1959':'août 1959',
        'accessed2026':'accessed 2026', 'Mathematica33(1976),29–41':'Mathematica 33 (1976), 29–41',
        'Sciences)91(1982),73–122':'Sciences) 91 (1982), 73–122',
        'Annalen263(1983),263–266':'Annalen 263 (1983), 263–266',
        'DOI10.':'DOI 10.', 'complete1982 and1983':'complete 1982 and 1983',
        'Tag03PK':'Tag 03PK', 'Tag04V8':'Tag 04V8',
        'Lemmas59.28.1 and59.28.3':'Lemmas 59.28.1 and 59.28.3',
        'the31':'the 31', 'the521':'the 521', 'these56':'these 56', 'all32':'all 32',
    }.items():
        s = s.replace(a,b)
    if name == 'notes_frontmatter.md':
        old = 'A check of a local algebra example, a conditional cokernel, or a logical implication is not labelled as a proof or refutation of a larger geometric theorem.'
        addition = ' The refined IDs used by refutation events are defined with their precise hypotheses and limits in [checked_statements.md](records/checked_statements.md).'
        if addition.strip() not in s:
            s = s.replace(old, old + addition)
        s = s.replace('pages 1,3,4', 'pages 1, 3, 4')
        s = s.replace('Text pagination 2,5, 6', 'Text pagination 2, 5, 6')
    p.write_text(s)

# Preserve the review's refinement in the detailed preliminary support record too.
p = R / 'notes_local_support.md'
s = p.read_text().replace('under its stronger hypothesis', 'under its differently formulated hypothesis')
s = s.replace("with Hua's stronger condition", "with Hua's differently formulated condition")
s = s.replace('compatible maps to all the other local objects', 'compatible maps to \\(X(t)\\) for every \\(t\\in U\\)')
p.write_text(s)
p = R / 'notes_root_support.md'
s = p.read_text().replace('Le groupe fondamental local à deux branches', 'Le π₁ local le long de deux branches')
s = s.replace('on the étale site its standard surjectivity argument requires n invertible on the base', 'on the étale site the standard Kummer statement applies when n is invertible on the base')
p.write_text(s)
print('Final research corrections applied; frozen source files untouched.')
