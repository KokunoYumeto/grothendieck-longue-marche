#!/usr/bin/env python3
"""Run a separate, reproducible supplied-context search for every research item."""
from pathlib import Path
import subprocess, sys

base = Path(__file__).resolve().parent
queries = [
('N001', r'1977|1978|Les feuillets', 'hua_project/138.modern.tex'),
('N002', r'460|page count|page counts', ''),
('N003', r'abélien universel|seconde tour', 'hua_project/138.modern.tex'),
('N004', r'tour diédrale|ramification.*2, 2, n', 'hua_project/138.modern.tex'),
('N005', r'mu_\{?infty|varprojlim.*mu|module de Tate', 'hua_project/138.modern.tex'),
('N006', r'endomorphismes de la conique|divisible par', 'hua_project/138.modern.tex'),
('N007', r'valeurs critiques|p.*lambda q', 'hua_project/138.modern.tex'),
('N008', r'paramétrisation rationnelle|forme.*z', 'hua_project/138.modern.tex'),
('N009', r'fonctions rationnelles|coordonnée répond', 'hua_project/138.modern.tex'),
('N010', r'52--53|surchargé', 'hua_project/138.modern.tex'),
('N011', r'52--53|étiquettes', 'hua_project/138.modern.tex'),
('N012', r'foncteurs|existe un.*f.*au-dessus', 'hua_project/138.modern.tex'),
('N013', r'premier produit|distincts des', 'hua_project/138.modern.tex'),
('N014', r'pleinement fidèle|est fidèle', 'hua_project/138.modern.tex'),
('N015', r'corollaires|C.*groupoïde', 'hua_project/138.modern.tex'),
('N016', r'connexité|Toute permutation', 'hua_project/138.modern.tex'),
('N017', r'commutant|torseur à droite', 'hua_project/138.modern.tex'),
('N018', r'K\(I\)|n = 2.*demande', 'hua_project/138.modern.tex'),
('N019', r'normalisateur de.*D|commutant', 'hua_project/138.modern.tex'),
('N020', r'rho_\{?[012]|permutations de produit', 'hua_project/138.modern.tex'),
('N021', r'indices.*surchargés|modèle des deux autres', 'hua_project/138.modern.tex'),
('N022', r'2, 3, 5|Riemann--Hurwitz', 'hua_project/138.modern.tex'),
('N023', r'4.*impossible|argument d.une ligne', 'hua_project/138.modern.tex'),
('N024', r'ramification n.est plus|page est barrée', 'hua_project/138.modern.tex'),
('N025', r'extension.*kummérienne de degré.*2|cyclique d.indice', 'hua_project/138.modern.tex'),
('N026', r'orientation|orientations', 'LM_140-2_text.tex'),
('N027', r'compactifié pur|compactification par les bouts', ''),
('N028', r'dissymétrie|points marqués et trous', 'hua_project/138.modern.tex'),
('N029', r'H\^2|Homext|structure à lacets', 'LM_140-2_text.tex'),
('N030', r'K\(.*mathbb Z|contractile', 'LM_140-2_text.tex'),
('N031', r'J.*varnothing|même dans les cas', 'hua_project/138.modern.tex'),
('N032', r'C\.12|infinite operator', 'RESULTS_STATE.md'),
('N033', r'drapeaux|sigma_0|sigma_2', 'Esquisse_cote119_copy1_API_transcription.tex'),
('N034', r'courbe algébrique complexe|clôture', 'Esquisse_cote119_copy1_API_transcription.tex'),
('N035', r'points spéciaux|deux points fixes|transpositions', 'hua_project/138.modern.tex'),
('N036', r'Sigma_|groupe profini spécial|rang', 'hua_project/138.modern.tex'),
('N037', r'nu = 1|injectivité demande', 'hua_project/138.modern.tex'),
('N038', r'prouve que.*surjectif|surjectivement', 'hua_project/138.modern.tex'),
('N039', r'première suite exacte|exposant.*circ', 'hua_project/138.modern.tex'),
('N040', r'classes d.inertie|Kummer|Tate', 'hua_project/138.modern.tex'),
('N041', r'forme tordue|foncteur fibre', 'hua_project/138.modern.tex'),
('N042', r'B\.27|sections', 'RESULTS_STATE.md'),
('N043', r'lacets.*issus|P.*trivial|exponentielle', 'hua_project/138.modern.tex'),
('N044', r'groupe des unités|chi_\{?n', 'hua_project/138.modern.tex'),
('N045', r'permute circulairement|rotation induit', 'hua_project/138.modern.tex'),
('N046', r'vérifier|produit des images|formule ne définit', 'hua_project/138.modern.tex'),
('N047', r'déplace le point base|classe dans|conjuguer une rotation', 'hua_project/138.modern.tex'),
('N048', r'sous-groupe des éléments|surjectivité.*chi|Gamma.*!.*subset', 'hua_project/138.modern.tex'),
('N049', r'centralisateur de|exceptionnel.*nu = 2', 'hua_project/138.modern.tex'),
('N050', r'isomorphismes canoniques|N075|P3', ''),
('N051', r'Homext.*L|Hyp|on prouve', 'hua_project/138.modern.tex'),
('N052', r'élucider|quotients.*Pi', 'hua_project/138.modern.tex'),
('N053', r'cursif|curly|normalis|réserve', 'hua_project/138.modern.tex'),
('N054', r'problèmes spéciaux|prolibres', 'hua_project/138.modern.tex'),
('N055', r'groupe cartographique|dictionnaire', 'Esquisse_cote119_copy1_API_transcription.tex'),
('N056', r'obtiendrait-on|Bielyi|toute courbe algébrique', 'Esquisse_cote119_copy1_API_transcription.tex'),
('N057', r'Белый|injectif|Lemme 2', 'LM_140-2_text.tex'),
('N058', r'fidèlement|regular|régulières|B6', ''),
('N059', r'C\.r[1-5]|C\.d1|B\.38', ''),
('N060', r'bi.?icosa|polyhedron|polyèdre|polyèdres|B\.12', ''),
('N061', r'Précartes|Opérations|moduli|modules', 'hua_project/138.modern.tex'),
('N062', r'11\.2|E\.65|E\.3|B\.12', 'RESULTS_STATE.md'),
]

root = base.parent
for note, pattern, filter_name in queries:
    with (root / 'research_searches.log').open('a') as f:
        f.write(f'\n### Note-specific search {note}\n')
    result = subprocess.run([sys.executable, str(base / 'context_search.py'), pattern, filter_name, '4'], text=True, capture_output=True, check=True)
    count = next(line for line in result.stdout.splitlines() if line.startswith('Hits:'))
    print(note, count)

