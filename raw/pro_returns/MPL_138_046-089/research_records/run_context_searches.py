"""Reproducible, post-freeze context search for each numbered research item.

Uses rg on supplied text only.  Records counts and line locators, without copying
the supplied context into the deliverable or changing any transcription.
"""
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone
import csv
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CONTEXT = ROOT.parent / 'context'
queries = {
 'N01': r'1976|1977|1978|1979|Mumford|Zariski|réutilis',
 'N02': r'diédral|dihedral|ramification|cartograph',
 'N03': r'mu_.*infty|varprojlim|Tate|tour.*Fermat|pro-rev',
 'N04': r'endomorphismes de la conique|carrés des|a \+ b \+ c|conique',
 'N05': r'conique|impair|puissance|descend|conjugu',
 'N06': r'paramétrisation|conique|forme.*z|équivalente.*mathbb',
 'N07': r'valeurs critiques|critique|ramification|polynômes',
 'N08': r'fonctions rationnelles|conique|rationnal|rationnel',
 'N09': r'surchargé|diagramme de revêtements|Fermat|Pi_',
 'N10': r'groupo[iïî]de|foncteur|multigaloisien',
 'N11': r'groupo[iïî]de|catégorie|pleinement fidèle|corollaires',
 'N12': r'connexité|groupoïde connexe|permutation.*objet|types d.isomorphie',
 'N13': r'K\(I\)|orange|normalisateur|commutant|polygone',
 'N14': r'double pyramide|rho_.*rho_|cartograph|triangles',
 'N15': r'tame|modéré|icosa|tétra|octa|Klein|congruence',
 'N16': r'Card.*I|chaque terme|entièrement barrée|impossible',
 'N17': r'inséparable|sauvage|Borel|abélien élémentaire|exposant.*douteux',
 'N18': r'kummérienne|genre.*0|cyclique.*indice|justifier|vérifier',
 'N19': r'paradigme|orient.*omega|orientation|Čech|Freudenthal',
 'N20': r'dissymétrie|points marqués|lacets|forgett|capping|Boundary compatibility',
 'N21': r'bigwedge|orientation|H\^2|otimes-1|forme.*altern',
 'N22': r'isotopi|contractil|contractib|K\(.*mathbb|cas.*exception',
 'N23': r'Trop brutal|C\.12|simply connected|simplement connexe|opérateurs',
 'N24': r'à lacets|à.*lcts|structure.*lac|structure.*bouts',
 'N25': r'Quelques problèmes spéciaux|problèmes spéciaux|prolibres spéciaux',
 'N26': r'drapeaux|times_A|times_\{A\}|indices douteux|pyramide',
 'N27': r'z\^2\(z-1\)|z\^\{2\}|bar.*j|méridiens|grands.*cercles',
 'N28': r'injectivité|abélien|nu = 1|nu.*geqslant 2|intérieurs',
 'N29': r'surjectif|surjectivement|cyclotomique|on prouve',
 'N30': r'première suite exacte|sans l.exposant|Gamma.*circ|conoyau',
 'N31': r'foncteur.*fibre|fiber|torseur|extérieure|extérieurs',
 'N32': r'Kummer|cyclotomique|transport de structure|arithmétique|congruence',
 'N33': r'notations|cursi|Teichmüller|collisions|lettre.*Gamma',
 'N34': r'cyclotomique|mu_.*Aut|mathbb.*Z.*n|automorphismes.*racines',
 'N35': r'renverse|renversement|lambda_\{0\}|commutateur|inversion',
 'N36': r'inversion|renversement|représentant|automorphisme intérieur|h_\{i\}',
 'N37': r'conjugaison complexe|réflexions|diédral|D\.12|rho_',
 'N38': r'Gamma.*!|surjectivité|cyclotomique|sous-groupe des éléments',
 'N39': r'commutant|centralisateur|mathfrak.*S.*3|GT.*0|11\.2',
 'N40': r'iso can|isomorphismes canoniques|Conjectural|tower|E\.24|E\.45',
 'N41': r'injectivité|injectif|fidèle|Белый|cale sur|pas vérifié',
 'N42': r'obtiendrait-on|Bely|Bielyi|Белый|toute courbe|corps de nombres',
 'N43': r'réguli|regular|fidèle|faithful|González|Jaikin',
 'N44': r'Précartes|moduli|modules|rigidité|Hua|No findings',
 'N45': r'Boundary compatibility|N075|forgett|sewing|relabel|générisation|E\.39',
 'N46': r'Fermat|E\.58|E\.65|E\.3|E\.49|A\.22|CM.parity|Delta',
}

notes = (ROOT / 'MPL_138_046-089_notes.md').read_text()
sections = dict(re.findall(r'^### (N\d+)\s+—[^\n]*\n(.*?)(?=^### N\d+\s+—|^## |\Z)', notes, re.M|re.S))
assert set(queries) == set(sections), (set(queries)-set(sections), set(sections)-set(queries))
files = subprocess.run(['rg','--files',str(CONTEXT)],check=True,text=True,capture_output=True).stdout.splitlines()
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
rows = []
for note, query in queries.items():
    proc = subprocess.run(['rg','-n','--no-heading','-i','--color','never','-e',query,*files],text=True,capture_output=True)
    if proc.returncode not in (0,1):
        raise RuntimeError(f'{note}: {proc.stderr}')
    hits = defaultdict(list)
    for hit in proc.stdout.splitlines():
        match = re.match(r'(.+?):(\d+):', hit)
        if match:
            hits[str(Path(match.group(1)).relative_to(CONTEXT))].append(int(match.group(2)))
    metadata = sections[note].split('\n\n',1)[0].strip()
    context_match = re.search(r'\*\*Context/relation:\*\* (.*?)(?= \*\*Register:)',metadata)
    register_match = re.search(r'\*\*Register:\*\* (.*)',metadata)
    rows.append({
      'note_id':note, 'searched_utc':stamp, 'rg_query':query,
      'scope':f'all {len(files)} supplied context text files',
      'matching_lines':sum(len(v) for v in hits.values()),
      'counts_and_first_20_line_numbers_by_file':json.dumps({k:{'count':len(v),'first_lines':v[:20]} for k,v in sorted(hits.items())},ensure_ascii=False),
      'selected_context_and_relation':context_match.group(1) if context_match else metadata,
      'register_connection':register_match.group(1) if register_match else '',
    })

out=HERE/'context_searches.tsv'
with out.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys(),delimiter='\t')
    w.writeheader();w.writerows(rows)
(HERE/'context_search_scope.json').write_text(json.dumps({
  'created_utc':stamp,'method':'rg -n --no-heading -i; text only; no OCR',
  'files':[str(Path(p).relative_to(CONTEXT)) for p in sorted(files)],
  'numbered_notes':list(queries),
  'interpretation':'Broad search counts are not evidence of relevance. Selected exact context locators and relations are stated in the notes; direct text excerpts were separately read. No supplied source contents are copied here.',
},indent=2,ensure_ascii=False)+'\n')
print(f'Recorded {len(rows)} actual searches across {len(files)} context files; each note has a query, locators, and status connection.')
