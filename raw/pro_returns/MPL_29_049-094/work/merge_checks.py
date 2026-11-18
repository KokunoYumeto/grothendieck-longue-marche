"""Merge mathematical check records without touching any transcription file."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work'
HEADER = ['statement_id', 'date', 'who', 'type', 'outcome']
rows = []
for name in ['birational_checks.tsv', 'picard_checks.tsv', 'formal_checks.tsv']:
    with (WORK / name).open(newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            row['type'] = row['type'].replace('refuted, refined statement', 'refuted, with refined statement')
            row['type'] = row['type'].replace('P17-unit-lifting-condition', 'FORMAL-17')
            if row['statement_id'] == 'scan072:bare-tangent-isomorphism-criterion':
                row['outcome'] = row['outcome'].replace('proper surjective closed immersion', 'proper closed immersion surjective on underlying points')
            if row['statement_id'] == 'scan076:rank-equality-with-unrestricted-ell':
                row['outcome'] = row['outcome'].replace('give pro-3 rank zero', 'give geometric pro-3 rank zero after base change to the algebraic closure of F3')
            if row['statement_id'].startswith('Source:S'):
                row['statement_id'] = row['statement_id'].replace('Source:S', 'Source:F-S', 1)
            rows.append(row)

date = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
who = 'GPT-6 Astra Pro; reasoning effort not exposed; MPL_29_049-094 /root'

def add(ident, kind, outcome, person=who):
    rows.append(dict(zip(HEADER, [ident, date, person, kind, outcome])))

add('N-FIN-04:finite-Hom', 'independent re-proof',
    'Common finite constructible stratification and finitely many connected strata reduce each sheaf map to finitely many maps between finite geometric stalks; these detect equality. Does not prove the neighbouring pushforward or gluing lemmas.')
add('Hua29:Le-pont-entre-H1-et-pi1:finite-H1-iff-finitely-generated', 'refuted, with refined statement N-FIN-06',
    'P=product over primes ell of (F_ell)^(d_ell), with finite unbounded d_ell, has finitely many continuous maps to each fixed finite target but no finite generating set. This refutes the abstract converse in context, not the geometric theorem.')
add('N-FIN-06:small-profinite-example', 'independent re-proof',
    'A finite target kills all prime factors not dividing its order; continuity kills the product of those factors. The remaining source is finite. Elementary-abelian quotients require unbounded generating ranks.')
add('N-FIN-07:Artin-Schreier-affine-line', 'independent re-proof',
    'For m positive and prime to p, highest-degree comparison proves the classes x^m independent modulo h^p-h; derivative -1 makes the corresponding covers finite etale. This checks failure of unrestricted finite-degree counting.')
add('N-FIN-04:Stacks05BE', 'carried as background without fault found',
    'Read the finite constructible-stratification convention; used it in the independent finite-Hom argument without treating the full etale-cohomology finiteness theory as proved.')
add('N-FIN-07:Stacks0A3J', 'used and rechecked in this run',
    'Used Artin-Schreier exactness and affine quasi-coherent vanishing to identify H1(A1,Fp) with the polynomial quotient by F-1; the polynomial independence was checked separately.')
add('N-FIN-06:Helbig-smallness-definition', 'carried as background without fault found',
    'Read the primary preprint definition of a small profinite group and its distinction from finite generation. The counterexample is proved in this run, not quoted from that source.')
add('N-ED-03:Esnault-Kindler-tame-Lefschetz', 'carried as background without fault found',
    'Read the authors abstract with regular/projective, normal-crossings and ample transverse-section hypotheses: equivalence in dimension at least three, full faithfulness in dimension two. No independent proof claimed.')
add('N-ED-05:geometric-specialization-stalk-direction', 'carried as background without fault found',
    'Stacks0GJ2 supplies the strict-localization lift and natural transformation from special stalk to general stalk. No bijection for every finite-etale fibre-functor path or product-of-fields assertion was established.')
add('N-ED-08:unramified-object-lift-nonuniqueness', 'independent re-proof',
    'Spec k -> Spec k[epsilon]/epsilon^2 and the identity of Spec k[epsilon]/epsilon^2 are distinct unramified objects with the same special-fibre identity. This concerns lifting objects, not uniqueness of maps into a fixed formally unramified target.')
add('N-TYP-02:finite-jet-coalgebra-model', 'targeted proof check',
    'For a finite local jet algebra, the dual of multiplication is coassociative and the dual of m/m^2 gives tangent vectors. Used only as a qualified interpretive model; the doubtful differentiability-class symbol was not resolved.')
add('N-TYP-05:mu-p-length-versus-points', 'independent re-proof',
    'Computed k[t]/(t^p-1)=k[t]/(t-1)^p over an algebraically closed field of characteristic p, giving length p and one geometric point; derivative gives n distinct roots for n prime to p.')
add('N-TYP-06:diagonalizable-faithful-flatness', 'independent re-proof',
    'Coset representatives for M/Mprime decompose O[M] freely over O[Mprime], proving faithful flatness; the induced morphism is affine and quasi-compact. Hom of the quotient identifies its kernel, with no claim of surjectivity on ordinary R-points.')
add('BR13-BR14:root-independent-obstruction-review', 'used and rechecked in this run',
    'Checked the simultaneous-sign invariant chart ac=b^2, its isolated singularity, the invariant field C(a,t), the valuation v(a)=1, and the Eisenstein extension sqrt(a). Properness supplies a centre, so finite etale pullback would contradict ramification. No conclusion about general essential constancy.')
add('P04:root-scope-review', 'used and rechecked in this run',
    'Checked alpha_p -> alpha_(p^2) is surjective only in the underlying-point sense used by the diagnostic, with equal tangent dimension and unequal finite length; not asserted to be faithfully flat or to occur in the birational Picard setting.')
add('P05:root-semilinear-review', 'used and rechecked in this run',
    'Computed fixed vectors and first/second kernels for F(e1)=0, F(e2)=e1. The ambiguous manuscript exponent remains frozen; only the ker-F-only interpretation is refuted.')
add('FORMAL-01:root-S3-review', 'used and rechecked in this run',
    'Verified Frobenius conjugation takes the order-three inertia generator to its square in F4((s))/F2((t)), t=s^3. Centrality needs trivial action on the actual inertia quotient.')
add('FORMAL-10:root-Picard-kernel-review', 'used and rechecked in this run',
    'Independently followed the full global-unit boundary: Gamma(X0,O*)=C* z^Z maps to Z a in H1(E x Gm,O), so a/n modulo Z a has exact order n. Local transition and exponential formal constructions preserve nontriviality; nilpotent Kummer cohomology invariance leaves a changing units/n term.')
add('FORMAL-11:root-root-pair-review', 'targeted proof check',
    'Checked local nth-power transition errors lie in principal units; the unique principal-unit root repairs the transitions and forces triple products to one. This proves root-pair lifting when n is invertible, not uniqueness of underlying Picard classes.')
add('FORMAL-17:external-discrepancy-review', 'targeted proof check',
    'Read Stacks0C6Q/0C6S and its preceding exact sequence; compared the claimed Pic[n] injectivity with the explicit nonzero torsion example. Retained the exact sequence, documented the conflict for expert follow-up, and made no external communication.')
add('BR09:published-finite-presentation-correction', 'carried as background without fault found',
    'Root opened ESS2021 Theorem1.1 and Lara-Srinivas-Stix2023 abstract and verified their stated conclusions contradict the context footnote about proper curves. The published proofs were not independently audited.')

# Record the second review as a separate event, without calling it a new re-proof.
reviewer = 'GPT-6 Astra Pro; reasoning effort not exposed; MPL_29_049-094 /root/packaging_checks'
for ident in ['N-FIN-04', 'N-FIN-06', 'N-FIN-07', 'N-ED-08', 'N-TYP-05', 'N-TYP-06']:
    add(ident + ':independent-scope-review', 'targeted proof check',
        'Reviewed the explicit argument and its context comparison from the frozen-text research memo; no substantive flaw found. N-ED-08 was clarified to distinguish lifting objects from maps into a fixed formally unramified target.', reviewer)

with (ROOT / 'CHECK_EVENTS.tsv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=HEADER, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print(f'Wrote {len(rows)} mathematical check events')
