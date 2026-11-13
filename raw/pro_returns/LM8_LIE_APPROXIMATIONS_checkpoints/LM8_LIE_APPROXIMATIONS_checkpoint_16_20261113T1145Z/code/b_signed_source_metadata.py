"""Write the independently reviewed B31--B34 ledgers and source concordance."""
from pathlib import Path
import csv
import json

ROOT=Path(__file__).resolve().parents[1]
SEC=ROOT/'sections'
anchor=('Cote140-3 §49.IV–V; visible folios568,570,578,583 and intervening '
        'unnumbered versos; physical scans530,534,549,550,559,560; '
        'linked-source(7), enlarged-source(6), fibre products(50)–(59)')
entries=[
 ('B.31','Proved',
  'For the full profinite modular group the linked and independently signed actual sources coincide; all numerical data are recovered from the automorphism. They preserve F and every Fermat kernel K_n and act on the actual relative pro-prime groups, continuous Q_l prounipotent completions, and integral abelian stages over Z_l. The retained signed normalizers and fibre products have explicitly typed strict and outer actions.',
  ['B.24a','E.2','GrothendieckLM1403Original'],
  'The proof establishes preservation before invoking completion. The radical rank is n²+1 and the finite quotient has order12n². Full profinite multipliers are evaluated locally, not treated as rational numbers; the rational-base obstruction is B34.'),
 ('B.32','Proved',
  'The intersection of [K_n,K_n] over the entire Fermat tower is F-double-prime, and C/F-double-prime is its equivariant inverse limit. The complete relative pro-prime Fermat family detects precisely finite F-quotients with nilpotent derived subgroup, a proper pro-formation quotient. Action kernels on the abelian tower are given by two explicit generator congruences.',
  ['B.31','code/b_signed_source.py'],
  'Finite metabelian separation proves the first intersection; compactness proves inverse-limit surjectivity. Sylow quotients of a nilpotent derived group prove the second equality. Exact A5 enumeration verifies order60, perfection and trivial centre. The kernel criterion is not a classification of every liftable quotient automorphism.'),
 ('B.33','Proved',
  'The exact actual signed-source image on Delta=C/F-prime is Zhat semidirect Zhat^times, with unique automorphisms Int(e0^r)s_mu and law (r,mu)(s,nu)=(r+mu*s,mu*nu). Its kernel is the based congruence subgroup acting trivially on the two modular generators modulo F-prime.',
  ['B.31','E.6','code/b_signed_source.py'],
  'Every multiplier is supplied by the actual cyclotomic Galois image. The standard braid correction vanishes on Delta, giving canonical s_mu. A direct integral cocycle computation proves the entire multiplier-one image. All elements and generator edges are checked in reductions n1 through8; these are not all isolated finite signed solutions.'),
 ('B.34','Refuted',
  'The whole profinite signed source has no action by Q-defined automorphisms of the first modular Lie stage compatible with its actual continuous Q5 action, and hence no compatible integral Z-model action. An actual Galois element with fifth-adic multiplier sqrt6 and other local multipliers1 gives the counterexample. The local and profinite actions in B31 are the correct replacement.',
  ['B.31','B.33','code/b_signed_source.py'],
  'The first Lie-layer matrix is sqrt6 times the identity, whose irrational trace cannot come from Q. Hensel existence and rational irrationality are proved; compatible roots through5^12 are checked. This does not deny constant profinite scheme actions or the rational fine-data existence of B24c.')
]
rows=[]
for sid,status,statement,deps,notes in entries:
 rows.append(dict(id=sid,statement=statement,status=status,
  where_proved='sections/B_signed_source.tex, Statement '+sid,
  depends_on=deps,manuscript_passages=[anchor,'Explicit prompt PartB follow-up(3), relative Fermat actions and signed conjugators'],
  depends_on_doubtful_reading=False,notes=notes))
(SEC/'B_signed_source_results.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
coverage=[
 dict(task='B.followup(3).actual_signed_source_preservation',status='Proved',results=['B.31'],remaining=[],
      requested='Identify the actual effective signed source and prove preservation of every Fermat kernel.'),
 dict(task='B.followup(3).actual_local_relative_actions',status='Proved',results=['B.31'],remaining=[],
      requested='Construct the entire continuous local and profinite relative actions with retained conjugator sources.'),
 dict(task='B.followup(3).whole_abelian_Fermat_quotient',status='Proved',results=['B.32'],remaining=[],
      requested='Determine exactly what the entire abelian Fermat tower and the relative pro-prime Fermat family detect.'),
 dict(task='B.followup(3).actual_first_modular_image',status='Proved',results=['B.33'],remaining=[],
      requested='Compute the complete actual signed-source image on C/F-prime.'),
 dict(task='B.followup(3).whole_source_rational_base_action',status='Refuted',results=['B.34','B.31'],remaining=[],
      requested='Decide whether the full profinite action can act by Q-defined Lie-stage automorphisms compatibly with local completion.')
]
(SEC/'B_signed_source_coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
head=['package','scan',r'the \unsure or \illegible place','what the mathematics supports','how strongly']
readings=[
 ['140-3 original','530,534','Loop sigma*rho versus sigma^-1*rho, visible central minus sign; linked signed definition(7)',
  'The alternatives differ by the central omega. Both squares give the same x, all units mu are odd, and actual signed automorphisms fix omega. Kernel preservation is independent of this convention.',
  'Original images directly inspected; folios568 and570. The proof does not silently decide doubtful ink.'],
 ['140-3 original','549,550','Definition(6) retains independent signs; possible loss of numerical coordinates',
  'For the full profinite modular group only, C_ab=Z/12 forces both signs from mu, and faithful e0 recovers mu from u. The conclusion need not hold for an arbitrary finite or quotient group C.',
  'Exact proof for the stated source; definition directly inspected on unnumbered preceding verso and folio578.'],
 ['140-3 original','559,560','Fibre products(50)–(59) and their different projections',
  'Normalizers act through their G_D projections, M through its extra G_D coordinate, S0Gamma through its D coordinate, while Gamma and gamma have the canonical outer action. Retained conjugators are not replaced by their minimal images.',
  'Original folio583 and following unnumbered verso directly inspected; all action maps are specified.'],
 ['140-4 / modern task','41; PartB follow-up(3)','Implicit transfer from a profinite multiplier to a rational scalar',
  'A genuine multiplier sqrt6 in Z5 prevents a compatible Q-defined first-stage action. Continuous Q_l and profinite relative actions are constructed instead.',
  'Complete counterexample with genuine Galois source; no claim of a paleographic correction.']
]
with (SEC/'B_signed_source_readings.csv').open('w',newline='') as handle:
 writer=csv.writer(handle);writer.writerow(head);writer.writerows(readings)
concordance=[]
folios={530:'568',534:'570',549:'unnumbered verso immediately preceding visible folio578',
        550:'578',559:'583',560:'unnumbered verso immediately following visible folio583'}
uses={530:'Section49.IV presentation, loop conventions and definition(7)',
      534:'Central-sign proof and loop/conjugator relation(16)',
      549:'Section49.V enlarged actual source definition(6)',
      550:'Numerical recoverability conditions, cyclic factor subgroups',
      559:'Signed normalizers and fibre products(50)–(56)',
      560:'Cartesian comparisons(57)–(59)'}
for p in folios:
 concordance.append(dict(physical_pdf_page=p,archive_footer=p-1,
  folio_as_observed=folios[p],use=uses[p],direct_visual_inspection=True,
  local_pdf=f'pdfpage{p}.pdf',local_image=f'pdfpage{p}.png'))
(ROOT/'source_checks/140-3-signed/concordance.json').write_text(json.dumps(
 dict(source_url='https://grothendieck.umontpellier.fr/140-3.pdf',
      convention='scan=physical PDF page, including modern cover; archive footer=scan-1',
      pages=concordance),ensure_ascii=False,indent=2)+'\n')
print('Saved B31–B34 results, five coverage rows, four readings, and six-page visual concordance.')
