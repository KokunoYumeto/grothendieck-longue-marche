"""Write only the dedicated signed q2 ledgers; root controls assembly."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT/'sections'
anchors = [
    'Section 51.1–2; folios664–669; cote140-4 scans33–44; equations(15),(18),(21),(28),(30),(31),(38)',
    'Section49.VI as referred to in Section51.2 scan41; full source is distinguished from its minimal specialization',
    'Explicit prompt PartB follow-up(3): signed-conjugator action on the Fermat relative completion, beginning q2'
]
entries = [
    ('B.24a', 'Proved',
     'Constructs the canonical integral modular q2 abelian-kernel stage with radical Ga5, finite quotient SL2(Z/4), and projection to the minimal rank-two stage. Its lattice map has Smith entries2,2 and vanishes modulo2; the characteristic-two scheme-theoretic image is the constant group of order48, cut out by X²−X,Y²−Y on twelve components.',
     ['B.8', 'B.20', 'E.2'],
     'Exact integral Schreier/cocycle construction. All110592 cocycle triples and2304 projection identities verified. This is an integral model constructed before reduction, not Q-to-F2 base change.'),
    ('B.24b', 'Proved',
     'The fine Section51 parameter scheme in characteristic2 acts through U=Ga×constant C2, with fibers Ga²×constant C2 retaining nu3. Its compatible-lift image is exactly t²=t, hence constant C2². The marked first-stage lift kernel is Ga6 semidirect Aut_add(Ga;f(1)=1), represented ind-affinely. Over dual numbers128 of256 fine parameters lift; the degree≤2 identity tangent lift kernel has dimension7, with one invisible Frobenius direction.',
     ['B.24', 'B.24a'],
     'Complete kernel for the stated six labelled boundary vector subgroups; unmarked kernel is also explicitly given by additive-polynomial equivariance and delta b=T(c)−c. Z1 dimension6, H1 dimension1, invariants0 are certified by a four-row reduced matrix on ten generator coordinates. No finite-type claim for the automorphism functor and no claim about full nonabelian stages.'),
    ('B.24c', 'Proved',
     'The inner minimal subgroup has a compatible homomorphic lift over Z[1/2] by t↦Int((t/2)k1), with a Ga3 torsor of rational inner lifts supplied by the identity vector subgroup. Every minimal fine datum over a Q-algebra has a compatible automorphism lift to the first abelian relative stage after rational choices. Actual source automorphisms act functorially; coarser quotient automorphisms are not reverse universal-property input.',
     ['B.24a'],
     'Finite group cocycles are split by the explicit average; compatible splittings and an actual central-twist automorphism produce rational lifts. This is first-stage existence and does not assert a canonical full-tower action.'),
    ('B.24d', 'Open',
     'B31–B34 identify the actual signed source, preserve every Fermat kernel, construct its continuous local and profinite relative actions, identify the whole abelian Fermat quotient, compute its first modular image, and refute a compatible rational-base action. The retained conjugator images on q2 and higher stages, full kernel classification, and realization of arbitrary first-stage polynomial lifts remain unresolved.',
     ['B.24', 'B.24a', 'B.24b', 'B.24c', 'B.31', 'B.32', 'B.33', 'B.34'],
     'Exact residual: compute the retained normalizer/conjugator images on q2 and higher relative stages; classify the complete kernels beyond word-congruence criteria; determine higher realization of arbitrary additive-polynomial lifts. The actual source and existence of its local/profinite actions are no longer missing, and its full rational-base action is false.')
]
rows = []
for sid, status, statement, deps, notes in entries:
    rows.append(dict(id=sid, statement=statement, status=status,
        where_proved='sections/g_signed_fermat2.tex; code/g_signed_fermat2.py; code/g_signed_fermat2.json; code/g_signed_fermat2_model.json',
        depends_on=deps, manuscript_passages=anchors,
        depends_on_doubtful_reading=False, notes=notes))
(SEC/'B_signed2_results.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
coverage = [
    dict(task='B.followup(3).minimal_integral_signed_comparison', status='Refuted',
         results=['B.24','B.24a'], remaining=[],
         notes='The source contains the valid dual-number datum Int(epsilon*x), whose image of rho violates the exact finite-image equation X²−X=0. No compatible lift exists, even fppf-locally.'),
    dict(task='B.followup(3).q2_characteristic2_liftable_functor', status='Proved',
         results=['B.24b'], remaining=[],
         notes='Exact image constant C2²; every nonempty lift fiber is a torsor under the explicit additive-polynomial kernel. With six labelled boundary vector groups the kernel is Ga6 semidirect Aut_add(Ga;f(1)=1).'),
    dict(task='B.followup(3).q2_rational_first_stage', status='Proved',
         results=['B.24a','B.24c'], remaining=[],
         notes='Constructs the integral model and its rational relative-completion meaning; proves rational minimal-data lift existence after fixed choices, without identifying it with every signed source version.'),
    dict(task='B.followup(3).full_signed_relative_tower', status='Open',
         results=['B.24d','B.31','B.32','B.33','B.34'],
         remaining=[
             'Determine the retained normalizer and conjugator images on q2 and higher relative stages; the exact first modular image does not determine these additional data.',
             'Classify the full action kernels beyond the proved word-congruence descriptions on C/F-prime and C/F-double-prime.',
             'Determine higher nonabelian compatibility of arbitrary additive-polynomial first-stage lifts.'
         ], notes='Actual source, preservation, continuous local and profinite actions are proved in B31; the complete abelian Fermat quotient is B32; first image is B33; a compatible whole-source rational-base action is refuted in B34.')
]
(SEC/'B_signed2_coverage.json').write_text(json.dumps(coverage, ensure_ascii=False, indent=2)+'\n')
readings = [
    dict(package='LM_C4-020-038', scan='36–38',
         doubtful_place='Equations(15)–(18): automorphism determined by rho,sigma; epsilon3 recoverability',
         mathematical_support='Both source issues are kept separate. Frobenius polynomial automorphisms are invisible on all discrete words. The constant nu3 sign remains independent data and does not repair a nonliftable minimal automorphism.',
         strength='Exact group-scheme formulas; checked transcription reopened. No claim that the original images of these pages were available locally.'),
    dict(package='LM_C4-039-057', scan='39–41',
         doubtful_place='Signs in(31), and subtraction versus equality chain in(32)',
         mathematical_support='All coherent plus/minus alternatives in(31) agree in characteristic2. The counterexample has nu2=nu3=nu=nu_prime=0 and satisfies the genuine conjugator and loop definitions independently of those signs. Reading(32) as an equality chain would exclude actual inner automorphisms already allowed by(15); it is not used.',
         strength='Supplied original scan041.jpg directly inspected; exact characteristic-two polynomial calculation. No final paleographic decision.'),
    dict(package='LM_C4-039-057', scan='41,43–44',
         doubtful_place='Whether formula(38) is recovered from generator images over arbitrary bases',
         mathematical_support='Scalar linearity on the vector group is explicit extra data in the fine action. It does define the minimal automorphism, but the canonical projection from the next integral Fermat stage has rank zero modulo2 and prevents unrestricted lifting.',
         strength='Complete integral projection and dual-number obstruction; source pushout formulas reopened in transcription.')
]
(SEC/'B_signed2_readings.json').write_text(json.dumps(readings, ensure_ascii=False, indent=2)+'\n')
(SEC/'B_signed2_refs.bib').write_text(r'''@misc{Grothendieck1981FermatStage,
  author={Grothendieck, Alexandre},
  title={La Longue Marche a travers la theorie de Galois: the minimal modular stage and signed conjugators, Section 51.1--2},
  year={1981},
  howpublished={Manuscript, cote 140-4, folios 664--669, scans 33--44},
  url={https://grothendieck.umontpellier.fr/140-4.pdf},
  keywords={verified},
  note={Verified: the supplied original scan 41 was directly inspected, and checked transcriptions of scans 33--47 were reopened. Original-page access is not claimed for the other pages. The coherent sign alternatives are retained; the characteristic-two counterexample is independent of them. No external theorem is invoked for the new finite cocycle and polynomial calculations.}
}
''')
print('Saved B_signed2 results(4), coverage(4), readings(3), and verified manuscript reference.')
