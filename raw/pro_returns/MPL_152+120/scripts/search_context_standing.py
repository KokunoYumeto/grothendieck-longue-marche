#!/usr/bin/env python3
"""Run and preserve context searches for the two standing-question sections."""
import json
import re
import subprocess
from pathlib import Path

base = Path(__file__).resolve().parents[2]
files = sorted(p for p in (base / 'context').rglob('*') if p.is_file())
contents = {p: p.read_text() for p in files}
queries = {
    'U01': ['amalgam', 'somme', 'inclusion'],
    'U02': ['graphe', 'réunion', 'amalgam'],
    'U03': ['compact', 'continu', 'voisinage'],
    'U04': ['voisinage', 'locale trivialité'],
    'U05': ['trivial', 'fibration', 'rare'],
    'U06': ['diagramme', 'morphismes', 'recollement'],
    'U07': ['produit', 'trivial', 'Z'],
    'U08': ['postuler', 'proposition', 'admet'],
    'U09': ['à vérifier', 'sauf erreur', 'je présume', 'Remords', 'Admettant'],
    'T01': ['IMAG', 'INSTITUT MONTPELLIERAIN ALEXANDER GROTHENDIECK'],
    'T02': ['Arbres plans', 'types de mots', 'page', 'folio'],
    'T03': ['Topologie modérée', 'Structures modérées', "Eloge", 'Éloge'],
    'T04': ['page', 'folio', r'\mspage{85}', r'\mspage{66}'],
    'T05': ['types de mots', 'Topologie modérée', '12 pages', '24 pages'],
    'T06': ['19 MAY 82', 'PREDONTA', 'CSSBATCH'],
}
report = {}
for note, terms in queries.items():
    cmd = ['rg', '--json', '-i', '-F']
    for term in terms:
        cmd += ['-e', term]
    cmd += [str(p) for p in files]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    assert proc.returncode in (0, 1), proc.stderr
    matches = []
    for line in proc.stdout.splitlines():
        item = json.loads(line)
        if item['type'] != 'match':
            continue
        data = item['data']
        path = Path(data['path']['text'])
        n = data['line_number']
        preceding = '\n'.join(contents[path].splitlines()[:n])
        scans = re.findall(r'\\scanpage\{(\d+)\}', preceding)
        matches.append({
            'file': path.relative_to(base).as_posix(),
            'line': n,
            'scan': int(scans[-1]) if scans else None,
            'excerpt': data['lines']['text'].strip()[:700],
        })
    report[note] = {'terms': terms, 'matches': matches}
    print(note, len(matches))
(base / 'work/research/context_search_standing.json').write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + '\n')
