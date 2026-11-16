"""Idempotently integrate reviewed sixth-hour results; preserve all open tasks."""
from pathlib import Path
import csv

P = Path(__file__).resolve().parents[1]
path = P/'task_coverage.csv'
with path.open() as f:
    reader = csv.DictReader(f)
    fields, rows = reader.fieldnames, list(reader)
assert len(rows)==49
index = {r['task']:r for r in rows}
formal = {r['id']:r['status'] for r in csv.DictReader((P/'LM4_SUCCESSOR_results.csv').open())}
assert all(formal.get(k)=='Proved' for k in ['A.50','A.51','A.52','A.53','B.62','B.63','C.37','C.38','C.39','C.40'])
extra_a = formal.get('A.54')=='Proved'
extra_b = formal.get('B.64')=='Proved'

def update(task, ids, state, obstruction=None, next_step=None, approaches=None):
    row = index[task]
    row['statement_ids'], row['state'] = ids, state
    for key,value in [('obstruction',obstruction),('next_step',next_step),('approaches',approaches)]:
        if value is not None:
            row[key] = value

scalar = ('For every finite abelian residual layer over an actual relative-pronilpotent base, '
          'the scalar central refinements stabilize at a proved bounded depth, determined by '
          'the dyadic and triadic exponents. A concrete filiform layer requires two steps. ')
if extra_a:
    scalar += ('After adjoining a stabilized layer, the new H1 is exactly Hom_C(V,T) under the '
               'stated acyclicity hypothesis; an actual repeated-module next layer shows that '
               'automatic vanishing need not persist. ')
a_ids = 'A.3;A.34;A.43;A.47–A.53'+(';A.54' if extra_a else '')
update('Lead 2',a_ids,
       'The closed-normal central-quotient lifting criterion is proved. '+scalar+
       'This supplies scalar-depth control, not an unrestricted finite-order lifting theorem.',
       '', 'Continue the separately required equivariant action and norm construction.')

tower = ('The compatible parity-one quotient family now includes the nonzero-frame Heisenberg '
         'layer and the c-paired filiform layer with its two actual scalar refinements, while '
         'retaining the earlier congruence, perfect and mixed layers. ')
for task,prefix in [('Lead 3','A.12;A.16–A.35;'),('A.5','A.7–A.8;A.12;A.23–A.35;'),('A.6','A.13;A.19;A.25–A.35;')]:
    state = tower+scalar+'No cofinal family or full order-two negative lift is proved.'
    if task=='A.5':
        state = 'The previously stated continuum-size cohomology conclusion is retained. '+state
    if task=='A.6':
        state += ' Parity on all full involutions remains undecided.'
    update(task,prefix+'A.40–A.41;A.43;A.47–A.53'+(';A.54' if extra_a else ''),state,
           'The stabilized quotient still needs an equivariant peripheral action with its retained frames; the full negative norm equation and cofinality remain unproved.',
           'Use the bounded scalar theorem to isolate and solve the remaining action or norm obstruction at a genuinely general finite layer.',
           'Actual residual quotients; nonzero torsion-frame cohomology; paired central covers; finite Pontryagin duality; bounded scalar refinement; retained full frames.')

generation = ('For every peripheral involution the canonical substitution generates in every S4 '
              'quotient and is automorphic on the relative pro-two completion over each S3 head. '
              'For GT0 involutions it also generates in every individual A5 quotient, satisfies '
              'the correctly normalized d-third-cusp identity in every S4 quotient, and is '
              'automorphic on the actual joint S4 finite head. ')
coinvariant = ('For the auxiliary negative involution, the full twisted-commutator normal subgroup '
               'is exactly the normal closure of the third cusp, and the coinvariant quotient is Zhat. ')
update('A.3','A.4–A.8;A.15;A.37–A.39;A.42;A.44–A.46;C.29–C.40',
       'The prescribed multiplier-one third cusp is false. The canonical GT word satisfies the full pentagon and all maximal pro-p conjugacy tests. Only the global pair ±d can solve its full third cusp. '+generation,
       'The full d-third-cusp equation and the joint A5 marking remain unproved.',
       'Prove the fixed full third-cusp identity or identify an actual canonical full-word obstruction.')
update('A.4','A.9–A.10;A.12;A.17;A.23–A.35;A.38;A.40–A.53;C.35–C.40'+(';A.54' if extra_a else ''),
       'Odd-prime results and all maximal pro-p canonical GT conjugators remain proved. '+generation+tower+scalar,
       'General relative marked conjugacy and a cofinal involutory family are not established.',
       'Control marking and the negative norm at general mixed finite bases.')
update('A.7','A.11;A.22;A.27;A.29;A.37–A.39;A.42;A.44–A.46;C.29–C.40',
       'The all-level generation and reflection criteria are proved; the exact full criterion is the third-cusp equation at d or -d. '+generation+coinvariant,
       '', 'The universal existence question remains task A.8.')
update('A.8','A.6;A.14;A.36–A.53;C.28–C.40'+(';A.54' if extra_a else ''),
       'All three universal full involution-conjugacy decisions remain open. '+generation+coinvariant+scalar+
       'The enlarged parity-one family remains noncofinal and the full negative square is undetermined.',
       'The canonical full third-cusp equation at d and the general equivariant negative norm remain unresolved.',
       'Attack the full marking or norm equation using the new joint-head and bounded-scalar structure.',
       'Full duality and one-section cohomology; binary GL2(F3) necessary conditions; actual joint finite heads; bounded central-refinement depth; exact retained-base cohomology.')

symplectic = ('The actual genus-five projective symplectic representation kills K modulo3. '
              'Modulo9 its possible image lies in a proved elementary abelian group of order27. '
              'The preimage M9 is an explicit proper open subgroup of N3, generally nonnormal; '
              'both refined products are closed for every pair of finite-index subgroups containing M9. ')
witnesses = ('All three surviving mod9 directions have matched actual words with exact ambient '
             'homology zero; the tetrahedral words lie in the full rigid normal kernel and the '
             'cyclic words are commutator words. These do not give a common element in the full completion. ')
analytic = ''
if extra_b:
    analytic = ('The actual integral3-adic centralizer and the identity-fibre intersection of the two '
                'symplectic images are determined in B.64, with the natural commuting-order filtration; '
                'this representation-level intersection is not identified with the image of K. ')
for task,ids in [('B.4','B.7;B.18–B.35;B.42–B.63'),('B.4.c','B.28;B.35;B.46–B.49;B.52;B.58–B.63'),('B.4.h','B.20;B.40;B.42–B.45;B.54–B.55;B.58–B.63')]:
    lead = ('K=1 remains undecided. The earlier zero ambient abelianization and primitive class-two bound remain in force. ')
    if task=='B.4.c':
        lead = 'The unrefined product is closed; arbitrary finite-index refinements remain equivalent to the unresolved centralizer decision. '
    if task=='B.4.h':
        lead = 'Universal braid-constrained R2 is false in the stated prime7 example; the complete relative images remain open. '
    update(task,ids+(';B.64' if extra_b else ''),lead+symplectic+witnesses+analytic,
           'Common quotient images and matched source words do not provide equality in the full profinite mapping class group.',
           'Control the kernel of the actual representation or a joint quotient retaining the forgetful tests, rather than infer a full lift from the common image.',
           'Actual branched-double-cover representation; exhaustive finite Schreier images; exact source words and integral homology; full completion comparison; nonnormal open refinements.')
update('B.4.a','B.13;B.19;B.56;B.58–B.63'+(';B.64' if extra_b else ''),
       'The thirteen-generator rigid monodromy and the stated discrete/completed-test kernels remain determined; the embedded-closure comparison remains open. '+witnesses+analytic,
       'Actual rigid-kernel words with matching symplectic images still need not equal the cyclic words in the full completion.',
       'Resolve the embedded closure comparison or impose an actual simultaneous quotient detecting the remaining discrepancy.')

assert index['A.8']['outcome']==index['B.4']['outcome']=='Open'
with path.open('w') as f:
    writer = csv.DictWriter(f,fieldnames=fields)
    writer.writeheader();writer.writerows(rows)
print('Updated49 task rows; A54:',extra_a,'B64:',extra_b,'both main decisions remain Open')

paper = P/'LM4_SUCCESSOR_paper.tex'
s = paper.read_text()
abstract = r'''We study involutions of the full profinite three-cusp group and
the icosahedral centralizer in the full profinite mapping class
group. Both universal full decisions remain open.
For a Grothendieck--Teichm\"uller involution, the canonical
coboundary word satisfies the full pentagon and gives the
prescribed conjugator at every maximal pro-prime quotient.
The remaining full condition is a third-cusp equation at an
explicitly determined dihedral unit. We prove that equation
in every symmetric-four quotient for gentle involutions,
and obtain automorphisms of the actual joint symmetric-four
head. We also prove generation in every individual alternating-five
quotient and specified relative completions. A one-section
argument identifies an exact full coinvariant quotient.
For every finite abelian residual layer over a relative
pronilpotent base, we prove an explicit bound on the depth
of its actual scalar central refinements. A filiform example
requires two steps. The compatible parity-one involutory
quotient family retains these layers and their literal frames;
cofinality and the full negative square are not established.
The actual icosahedral centralizer has zero ambient
abelianization and trivial image in the projective symplectic
representation modulo three. Its first triadic lift is confined
to an explicit three-dimensional subgroup, giving stronger
closed refined products. Actual rigid-kernel and cyclic words
realize every direction in this quotient, without constructing
a nontrivial full centralizer element.
We also give the source audits, torus and real-structure
reductions, controlled noncompact comparisons, and the corrected
five-point census. Every numbered assertion has an explicit
proof status. A gap in a published proof is not treated as a
counterexample to its theorem. This work is incomplete, and
no priority is claimed.'''
a,b=s.index('\\begin{abstract}'),s.index('\\end{abstract}')
s=s[:a]+'\\begin{abstract}\n'+abstract+'\n'+s[b:]
paper.write_text(s)
