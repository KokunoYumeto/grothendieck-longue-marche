#!/usr/bin/env python3
"""Companion B.35 ledgers only; does not assemble or rebuild the project."""
from pathlib import Path
import csv,json
sec=Path(__file__).resolve().parents[1]/'sections'
records=[{
 'id':'B.35','status':'Proved',
 'statement':'The actual first-stage images are N_rho^* -> C3 semidirect Zhat^times and N_sigma^* -> C2 times {(t,mu) in Zhat semidirect Zhat^times: t mod2=(mu_2^2-1)/8 mod2}. The second multiplier extension is nonsplit. G_D and the two M fibre products have image Inn(Delta) semidirect s_units, with exact coordinate kernels.',
 'where_proved':'sections/g_signed_normalizers.tex, B.35; code/g_signed_normalizers.py/.json/.out',
 'depends_on':['B.24a','B.31','B.33','E.6','B35HerfortRibes1984, Theorems1--2, printedp31','FA_Wickelgren2012, Lemma3.16 and the direct Kummer-cover computation'],
 'manuscript_passages':['Section49.IV--V, cote140-3 scans530,534,549,550,559--560; numberedfolios568,570,578,583, with interveningversos kept unnumbered','Explicit prompt PartB follow-up(3): actual M/N source actions and their kernel/image on the Fermat approximations','Explicit follow-up: distinguish full signed source from minimal-stage conjugator data'],
 'depends_on_doubtful_reading':False,
 'notes':'Every image is for the specified strict action on Delta=C/Fprime. The sigma multiplier-one translation image is exactly2Zhat, not the whole quotient centralizer line. The upper bound is the integral class-two equation2q+k^2=0; actual arithmetic realization is the path to1/2 and Kummer2. Basepoint changes add(chi-1)v, so they do not alter the kernel-cyclotomic image or parity. The possible central omega discrepancy upstairs is excluded by the forced sigma sign in C_ab. No claim about all higher Fermat images follows from this first-stage theorem. Exact finite reductions n1..8 and a nonsplitting witness modulo translation4/units8 were executed.'
}]
coverage=[
 {'task':'B.signed_actual.normalizers_minimal','requested':'Determine the actual N_rho and N_sigma images and kernels on the first modular quotient, retaining their conjugator data.','status':'Proved','results':['B.35'],'remaining':[]},
 {'task':'B.signed_actual.M_minimal','requested':'Determine the strict first-stage action of G_D, M_D and S0M_D, with their kernels.','status':'Proved','results':['B.31','B.33','B.35'],'remaining':[]},
 {'task':'B.signed_actual.sigma_midpoint','requested':'Decide whether the sigma centralizer creates a genuinely finer actual conjugator image than the D action alone.','status':'Proved','results':['B.35'],'remaining':[],'notes':'The exact surviving character is Kummer2; its parity coupling to the multiplier makes the resulting extension nonsplit.'},
 {'task':'B.signed_actual.normalizers_higher','requested':'Determine the retained normalizer actions on the full higher Fermat tower.','status':'Open','results':['B.31','B.32','B.35'],'remaining':['The theorem computes strict normalizer images only on Delta=C/Fprime. The full higher relative/pro-ell conjugator images and their coordinate kernels still require further calculation.']}
]
(sec/'B_normalizer_results.json').write_text(json.dumps(records,indent=2)+'\n')
(sec/'B_normalizer_coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
rows=[
 ['Cote140-3','530;534;549;550;559--560','568;570;578;583','Section49.IV--V definitions and fibre products','Actual source D, signed normalizers and retained M fibre products are those typed in B.31.','Images are computed through the specified strict projection, not inferred from minimal parameter schemes.','B.35','no'],
 ['Herfort--Ribes1984','Primary archive PDF','31--34','Theorems1 and2','The original announcement and proof outline were reopened via the indexed primary PDF; the direct URL initially returned403.','Finite-order2 stabilizers in Zhat freeprofiniteproduct C2 are conjugate into C2; an F-conjugator follows because the quotient is C2. Factor centralizers give the required uniqueness.','B.35','no'],
 ['Wickelgren2012','Primary author PDF','printed19--20','Lemma3.16;Section3.10','Rational-point abelian path coordinates are the two Kummer classes of z and1-z.','At1/2 both are the class of1/2; the proof additionally uses the explicit Kummer covers to retain all primes and path-coboundary dependence.','B.35','no'],
 ['Nakamura2013 and E.6','Standard braid action','','Equation5.4.2','The arithmetic GT action on B3 restricts to the standard based action on the two pure meridians.','Its quotient by the centre is identified with the quotient orbifold action; no independent action with the same F restriction exists because the centralizer of F is trivial.','B.35','no']
]
with (sec/'B_normalizer_readings.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['cote','scan','folio','equation','reading','resolution','used_by','doubtful']);w.writerows(rows)
print('Saved B.35 companion ledgers.')
