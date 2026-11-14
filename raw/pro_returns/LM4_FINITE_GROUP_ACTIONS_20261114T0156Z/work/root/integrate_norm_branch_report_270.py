#!/usr/bin/env python3
"""Add the accepted norm continuation to the exact original-obligation report."""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[2]
gate=ROOT/'work/root/norm_branch_acceptance_270.json'
assert json.loads(gate.read_text())['status']=='PASS_ROOT_AND_PEER'
changes=[]
def edit(name,old,new):
    p=ROOT/name;before=p.read_bytes();text=before.decode()
    assert text.count(old)==1,(name,old,text.count(old))
    p.write_text(text.replace(old,new,1))
    changes.append({'path':name,'old_sha256':sha256(before).hexdigest(),
                    'new_sha256':sha256(p.read_bytes()).hexdigest()})
note=(' The separately accepted norm continuation gives the exact inverse isomorphisms '
      'F semidirect_omega C3 <-> C3*C3 and D(k)^-1=(h y^-k eta)^3. '
      'Its two residue-labelled compact conjugator branches map homeomorphically onto the original T, retaining the original boundary-conjugator fiber. '
      'The explicit odd-prime midpoint and coefficient maps construct a continuous local solution family through h_p, while the original full solution space maps exactly to {h_p}. '
      'An actual3125-element pro-5 image verifies a coefficient-one local obstruction; original T nonemptiness and its actual all-prime coefficient constraints remain unresolved.')
anchor="rows=[(label, current_270[label][0], current_270[label][1])"
replacement="_refs, _state = current_270['D.b']\ncurrent_270['D.b'] = (_refs, _state + "+repr(note)+')\n'+anchor
edit('work/root/make_report.py',anchor,replacement)
anchor="add_report('work/root/research_update_270.md')"
edit('work/root/make_report.py',anchor,anchor+"\nadd_report('work/part_d_attack/actual_norm_branches_and_odd_local_coefficients.txt',title='Actual full norm branches and the original-to-local coefficient image')")
anchor='### Accepted finite surface operations'
addition='''### Accepted actual norm branches and local coefficient maps

The complete 287-line norm continuation, its 195-line program, all primary source clauses used there, and both unchanged isolated replays passed root and independent peer review. Both replays pass 27 named checks in the actual 3,125-element finite pro-5 image, including all five local coefficients and all twenty unit-parameter rows. Their entire JSON outputs and stdout are raw byte-identical to both frozen author outputs. The acceptance records the complete read scope and exact bindings.

The specified full extension `L=F semidirect_omega C3` has explicit inverse continuous homomorphisms to `C3(A)*C3(B)`, with `A=eta` and `B=x eta`. The actual original word satisfies `D(k)^-1=(h y^-k eta)^3`. The two factor classes give residue-labelled compact conjugator branches, with unique original F-conjugators; their map `(k,w)->2k+1` is a homeomorphism onto the original unit zero set. The inverse retains the residue branch, orbit-map inverse and original right cusp-centralizer fiber. Existence of a point in those branches remains the original problem.

For each odd prime, the named maximal pro-p quotient has the explicit midpoint retraction `M_p(g)=g(g^-1 alpha_p(g))^(1/2)` onto its fixed subgroup. The central coefficient map splits by powers of the single element `M_p(c_p)`. The original full fixed group maps to coefficient zero. An explicit continuous family `H_r` through the actual original image `h_p` solves the local coboundary and first-symmetry equations and has every prescribed p-adic central coefficient; the unique full solution maps exactly to `h_p`. At the standard involution and p=5, the constructed local coefficient-one member has no unit zero, already in the retained actual finite image. The original full `h=1` maps to the coefficient-zero member. These exact image comparisons preserve the outstanding original nonemptiness and all-prime constraints.

'''+anchor
edit('work/root/research_update_270.md',anchor,addition)
record={'status':'INTEGRATED_ACCEPTED_NORM_BRANCH_CONTINUATION','numbered_claim_added':False,
        'acceptance_sha256':sha256(gate.read_bytes()).hexdigest(),'changes':changes}
(ROOT/'work/root/norm_branch_report_integration_270.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','source_edits':len(changes),'numbered_claim_added':False},indent=2))
