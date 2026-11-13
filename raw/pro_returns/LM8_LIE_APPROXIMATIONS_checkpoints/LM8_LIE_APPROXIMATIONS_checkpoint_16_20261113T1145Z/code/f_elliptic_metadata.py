#!/usr/bin/env python3
"""Write the status and source ledgers for the elliptic F(c) supplement."""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / 'sections'
passages = ['C4 §51, f.734, scan173: successive approximations and splittings',
            'C4 §51, f.736, scan178: inadequacy of the abelian approximation',
            'C4 §52, ff.743-746, scans191-197: type (1,1), multiplicities and arithmetic extensions']
results = [
 dict(id='F.6', status='Proved',
      statement='E1:y²=x³−x has rank zero and E6:y²=x³−36x has rank one; both have a5=−2, finite Sha, and ordinary Bloch–Kato Selmer rank equal to Mordell–Weil rank.',
      where_proved='sections/F_elliptic.tex, Statement F.6 and proof; code/f_elliptic_dimensions.py',
      depends_on=['Monsky descent formula, Das–Saikia 2024 equations (2.1)–(2.3)',
                  'LMFDB 32.a3 and 576.c3 rigorous analytic ranks and reliability statement',
                  'Kolyvagin 1990 MPI/90-69, Theorem 1'],
      notes='Ranks also checked by exact descent and non-torsion point arithmetic. Finite Sha uses the separate rigorous analytic-rank input, not the 2-descent and not a rounded analytic Sha order.'),
 dict(id='F.7', status='Proved',
      statement='Exact local dimensions through classes 1–8 are 1,2,4,7,13,22,40,70 for the full free tower and 1,2,4,7,11,16,22,29 for its free metabelian quotient; all graded dimensions, conjugation traces and CM bidegree multiplicities are exactly computed.',
      where_proved='sections/F_elliptic.tex, Statement F.7 and proof; code/f_elliptic_dimensions.json and .csv',
      depends_on=['Free Lie Witt character formula', 'Betts 2023, Corollary 3.1.11'],
      notes='Program exhausts all binary words through length 8 and verifies Lyndon counts against Witt formulas. Metabelian basis is explicit. No Galois cohomology is sampled.'),
 dict(id='F.8', status='Proved',
      statement='With the specified refined integral local conditions, maximal global Selmer dimensions at classes one and two are exactly r and r+|S|. Rank zero gives a strict inequality at class one for |S|=0,1,2; rank one with S empty gives a strict inequality at class two and finiteness.',
      where_proved='sections/F_elliptic.tex, Statement F.8 and proof',
      depends_on=['F.6','F.7','Kim–Tamagawa 2008 Theorem 0.1 and Corollaries 0.2–0.3',
                  'Kim 2009 Theorem 1 and §3'],
      notes='Dimension means the maximum over nonempty reduction-type components; choosing the cuspidal component at every denominator prime attains r+|S|. Bad primes outside S have finite integral local conditions. Old Kim U3 is present class two.'),
 dict(id='F.9', status='Proved',
      statement='All full and metabelian global Selmer dimensions through class eight for E1 and E6, with the specified refined local conditions and |S|=0,1,2, equal the displayed exact numerical tables. The dual Selmer defects in degrees3–8 vanish by F.18. The first strict levels are1 for E1 and2,3,4 for E6 with |S|=0,1,2.',
      where_proved='sections/F_elliptic.tex, Statement F.9 and structural reduction proof, together with arithmetic vanishing in sections/F_advanced.tex, F.18',
      depends_on=['F.6','F.7','F.8','F.16','F.17','F.18','Poitou–Tate formula (LLM 2023 equation (5.6))',
                  'Central nonabelian cocycle obstruction sequence'],
      notes='δn is dual to H²(G_Q,T,Lie_n(V)); F.18 proves its vanishing in every required degree and both towers, so each higher transition is surjective with the predicted vector-space fibre. Thus the entire table, not only an upper bound or first threshold, is unconditional. Exact modulo25 CM modular-symbol specializations and Kato divisibility prove the arithmetic vanishing; no geometric-regularity assumption is imported. Finite reduction-type, integral/cuspidal local conditions and crystallinity at5 remain part of the statement.')
]
for item in results:
    item['manuscript_passages'] = passages
    item['depends_on_doubtful_reading'] = False
(SEC / 'F_elliptic_results.json').write_text(json.dumps(results, indent=2, ensure_ascii=False) + '\n')

coverage = [
 dict(task='F.c.examples', requested='One type (1,1) example of rank zero and one of rank one', status='complete',
      results=['F.6'], remaining=[]),
 dict(task='F.c.local', requested='Local dimensions by program through class/weight eight', status='complete',
      results=['F.7'], remaining=[]),
 dict(task='F.c.global_low', requested='Exact global dimensions and integral finiteness at the first usable levels', status='complete',
      results=['F.8'], remaining=[]),
 dict(task='F.c.global_high', requested='Exact numerical global Selmer dimensions through class eight for |S|=0,1,2', status='complete',
      results=['F.9','F.16','F.17','F.18'], remaining=[]),
 dict(task='F.c.metabelian', requested='Repeat for the free metabelian approximation', status='complete',
      results=['F.7','F.8','F.9','F.16','F.17','F.18'], remaining=[]),
 dict(task='F.c.first_level', requested='First strict global–local dimension inequality for |S|=0,1,2', status='complete',
      results=['F.8','F.9','F.16','F.17'], remaining=[]),
 dict(task='F.e.elliptic_transfer', requested='Lemmas with all hypotheses for LM6 Part E', status='complete',
      results=['F.6','F.7','F.8','F.9','F.18'], remaining=[],
      conditions_to_retain=['The named curves and p=5','The refined integral/cuspidal local conditions','Crystallinity at5','Degree bound n≤8','The finite-Sha rank input in F.6'])
]
(SEC / 'F_elliptic_coverage.json').write_text(json.dumps(coverage, indent=2, ensure_ascii=False) + '\n')

with (SEC / 'F_elliptic_readings.csv').open('w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['cote','scan','folio','equation','reading','resolution','used_by','doubtful'])
    writer.writerow(['140-4','173','734','371','Each finer Lie approximation requires reconsideration of splittings',
                     'Checked transcript read. Used as programmatic motivation, not as a Selmer theorem.','F.6-F.9','no'])
    writer.writerow(['140-4','178','736','379','Abelian approximation loses the Fermat equation',
                     'Checked transcript read. Elliptic calculation similarly separates class one from higher obstructions.','F.8;F.9','no'])
    writer.writerow(['140-4','191-197','743-746','arithmetic extensions','Type (1,1) Teichmüller and modular structures',
                     'Uses explicit modern once-punctured elliptic curve and Galois action; no doubtful letter affects the computations.','F.6-F.9','no'])
    writer.writerow(['primary-source','Kim2009','93','Theorem1','U2 denotes the abelian quotient',
                     'Present class n is Kim2009 level n+1; Kim–Tamagawa U3 is class two.','F.8','no'])
    writer.writerow(['primary-source','Kolyvagin1990','4','Theorem1','Analytic rank at most one',
                     'Author manuscript theorem read; OCR omits the inequality sign in some extraction, inequality sign verified directly in the rendered original page.','F.6','no'])

print('Wrote F_elliptic results, coverage and reading ledgers.')
