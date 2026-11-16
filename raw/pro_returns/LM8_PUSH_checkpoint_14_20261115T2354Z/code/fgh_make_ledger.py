"""Build the F/G/H result ledger from the explicitly reviewed statement inventory."""
from pathlib import Path
import json

rows=[]
def row(i,s,status,dep,ans,note='',where=None):
 rows.append(dict(id=i,statement=s,status=status,where_proved=where or f'sections/{i[0]}.tex',depends_on=dep,answers=ans,notes=note))
row('F.1','The full arbitrary-germ characterization is not obtained; exact point-germ, residual, stability and surjective-tower cases are proved separately.','Open','F.7–F.18','Task F.1; Lead 14','The unrestricted replacement assertion in Lead 14 is refuted by F.8.')
row('F.2','For a small cofiltered coherent system with coherent transition morphisms, finite locally constant objects descend; the characteristic-zero strict henselian normal-crossings étale limit and its finite fundamental group are identified.','Known','SGA 4 VI 8.2.3,8.3.6,8.3.13; SGA 1 XIII 5.3; Stacks 0EYL,0GL2','Task F.2; Lead 21 scheme assertions','All finite trivializing data and their finite covering condition are descended explicitly. Local dimension one gives a classifying topos; higher dimension does not.')
row('F.3','The two manuscript readings are decided in the proved subclasses, but a characterization for every germ remains open.','Open','F.7–F.18; Leroy 1979','Task F.3','Leroy supplies the locally Galois replacement and precise groupoid-limit results; he does not assert the false unrestricted comparison.')
row('F.4','The complex normal-crossings homotopy limit is the tangent torus; a rational cusp over a number field gives a completed-Kummer torsor of homotopy fixed points with trivial fundamental groups.','Proved','Stix Theorem 14, supplied version; Kummer theory and finite Mittag-Leffler systems','Task F.4; Lead 17(a); Lead 17(b)','Rational tangent vectors inject densely and properly. Packet injection uses proper-point injectivity over finite extensions.')
row('F.5','The literal disjunction in the proposed homotopy reformulation is automatic for the hyperbolic K(pi,1); the non-tautological cuspidal section conjecture remains a surjectivity problem.','Open','Schmidt–Stix Lemma 2.7(a); F.4','Task F.5','Automaticity is proved, but alone does not refute logical equivalence with a conjecture that may itself be true. Identifying all curve homotopy fixed points with rational points is false in the presence of a rational cusp.')
row('F.6','The unrestricted étale-stack torus and geometric-fibre assertions in Lead 21 are false.','Refuted','Explicit stack BC2 times a disk; fgh_topology_checks.py','Task F.6; Lead 21(B,C), unrestricted stacks','The punctured germ retains BC2, so H1 is Z plus Z/2. The same counterexample has an effective bidisc quotient realization. Intrinsic residual-gerbe and geometric point fibres differ.')
row('F.7','The inverse limit of open-subspace sheaf topoi is the sheaf topos of the intersection sublocale; for a closed subset of a regular Hausdorff space the ordinary germ is the closed subset and the residual germ is empty.','Proved','Open-subtopos and sublocale correspondence','Task F.1; Task F.3; Lead 14, localic assertions')
row('F.8','There are locally connected, semilocally simply connected covering germs which cannot be the locally constant objects of any Grothendieck topos.','Refuted','Discrete tails of N and diagonal argument','Task F.1; Task F.3; Lead 14, replacement assertion','The covering-germ category lacks a countable coproduct of its terminal object. Representatives are chosen simultaneously after filling their individually finite undefined prefixes.')
row('F.9','Normal-crossings covering germs are Z^r-sets; nested closed blow-up stages have the closed fibre as limit, and tubular neighbourhood germs of closed submanifolds have the expected coverings.','Proved','Coordinate polydiscs; closed-subtopos intersections','Task F.1; Task F.2; Task F.3; Lead 21(B), manifolds','The arbitrary Z^r-action category differs from the finite continuous profinite-action category.')
row('F.10','For a countable surjective tower of discrete groups, the inverse limit of classifying topoi is the classifying topos of the prodiscrete limit and its locally constant objects are the stagewise colimit.','Proved','Leroy Proposition 3.3.3; common-open-kernel criterion','Task F.1; Task F.3; Lead 14, corrected replacement','All continuous actions need not be locally constant: the disjoint union of Z/2^n is a counterexample for Z2.')
row('F.11','Compactness of a closed subset alone does not give full faithfulness for arbitrary covering descent.','Refuted','Cantor subset of R and the family of digit functions','Task F.1; Task F.3','Every finite family of digit functions descends; the countable family does not descend to one neighbourhood.')
row('F.12','For a decreasing coordinate neighbourhood basis at a complex normal-crossings point, the strict singular-chain limit is zero and the degreewise lim1 complex recovers torus homology with the stated shift.','Proved','Roos complex and Milnor exact sequence','Task F.6; Lead 21(C), manifolds','For stacks the torus must be replaced by the actual isotropy-retaining homotopy fibre.')
row('F.13','Leroy proves the locally Galois sum-completion theorem, precise classifying-topos limits and a van Kampen theorem, with hypotheses distinct from arbitrary covering-germ descent.','Known','Leroy Theorem 2.4; 3.3.2–3.3.4; 3.4.1; 4.1.1; section 4.5','Task F.3','Original scan and provisional transcription were read together; no theorem is inferred from the title alone.')
row('F.14','Under connected classical covering hypotheses and surjective maps from the limit fundamental group, arbitrary covering descent is equivalent to eventual fundamental-group stability.','Proved','Regular action detects the kernel','Task F.1; Task F.3','The surjectivity and connected, locally path connected, semilocally simply connected hypotheses are explicit.')
row('F.15','A countable intersection of open subspaces of a locally compact Hausdorff space is spatial as a sublocale intersection, with its subspace topology.','Proved','Direct compact nested-neighbourhood proof','Task F.6; Lead 21(A), manifolds','The intersection K need not be closed or compact; the ambient local compactness and countability are used.')
row('F.16','The intrinsic étale-stack version of the countable-open intersection theorem holds with a locally compact Hausdorff atlas; nested closed substacks have the expected intrinsic intersection limit.','Proved','F.15 and étale atlas descent','Task F.6; Lead 21(A,B), corrected stacks','Neighbourhoods must be intrinsic open substacks; a residual-gerbe fibre also needs a downstairs family actually shrinking to that gerbe. A locally compact Hausdorff atlas alone does not guarantee a Hausdorff orbit space. The geometric point 2-fibre differs.')
row('F.17','For every Hausdorff point germ, arbitrary covering descent and existence of any locally-constant-topos realization are equivalent to every neighbourhood quasi-component being a neighbourhood.','Proved','Clopen-indicator family; terminal-coproduct criterion','Task F.1; Task F.3; Lead 14','The convergent sequence at its limit point gives an explicit failure. This is an exact characterization for all Hausdorff point germs.')
row('F.18','For a closed subset Y of a regular Hausdorff space, the residual covering germ agrees with its literal limit exactly when Y is open.','Proved','F.7 and persistence of empty versus terminal covers','Task F.1; Task F.3; Lead 14','This is an exact residual closed-subset criterion.')
row('F.19','For every compact subset of a locally compact Hausdorff space, finite coverings and their morphisms descend to one open neighbourhood, without local connectivity assumptions.','Proved','Finite frame-bundle join construction; neighbourhood retraction; properness of finite covers','Task F.1; Task F.2; Task F.3','The ordinary finite-cover comparison is an equivalence for the Cantor germ, while arbitrary-cover full faithfulness fails.')
row('G.1','The actual arithmetic scalar lambda and its asserted rationality are not determined.','Open','G.4–G.7; Enriquez Proposition 4.19','Task G.1; Lead 15','Universal geometric and CM constraints admit every 5-adic scalar; this does not refute rationality of the actual arithmetic value.')
row('G.2','The actual alpha-image ideal, nu values, and arithmetic lattice index are not measured.','Open','G.6,G.7','Task G.2','The exact conditional index formula distinguishes the finite index in the saturation from infinite index in the ambient rank-two lattice.')
row('G.3','The embedded arithmetic generators and integral lattices in all repeated-character spaces of degrees eight through fourteen are not determined.','Open','G.1,G.2','Task G.3','Ambient dimensions and metabelian characters do not specify these embeddings.')
row('G.4','The degree-eight ambient vectors, word coordinates, metabelian projection, and saturated Z5 lattice are independently certified.','Proved','code/fgh_degree8.py, JSON and stdout','Task G.1; Task G.2; Task G.3','C8=A8+(31/20)B8 and B8 form the saturated integral basis; alpha,nu are the dual integral coordinates.')
row('G.5','Every 5-adic scalar gives an allowed universal geometric degree-eight direction; these constraints do not force rationality.','Proved','Enriquez Proposition 4.19 and inclusion after (49); G.4','Task G.1; Lead 15, proposed inference','The Hensel root sqrt(6) in Q5 is an explicit irrational allowed scalar, not an arithmetic Galois counterexample.')
row('G.6','For delta=lambda-31/20, m=max(0,-v5(delta)), and alpha-image 5^a Z5, the arithmetic index in its saturated line is exactly 5^(a-m).','Proved','G.4 and rank-one lattice algebra','Task G.2','Conditional formula; neither delta nor a has been determined for the actual Galois action.')
row('G.7','A degree-nine finite Magnus quotient measures alpha and nu of an actual eighth-Johnson automorphism without logarithmic division.','Proved','Truncated noncommutative power series over Z/5^r','Task G.1; Task G.2','The recipe is finite and explicit; an actual arithmetic automorphism remains to be supplied and evaluated.')
row('H.1','The images of the five retained normalizer/conjugator sources on every higher relative stage are not determined.','Open','H.4,H.7,H.8','Task H.1','Ambient scheme automorphisms are not identified with the actual profinite source images.')
row('H.2','The individual kernels for the five retained sources at every stage are not determined.','Open','H.7','Task H.2','A general affine action criterion and the joint full-prime abelian-stage kernel are proved separately.')
row('H.3','Extension of every additive-polynomial first-stage lift to the unspecified integral nonabelian tower remains open.','Open','H.5,H.6','Task H.3','All abelian Fermat stages admit the same lift. A specific class-two quotient obstructs it, but its canonical integral comparison at 2 is not established.')
row('H.4','The first integral q2 model and its dual-number idempotence obstruction have been rerun and verified.','Known','code/fgh_q2_recheck.py and attached standalone source','Task H.1; Task H.2; Task H.3','110592 cocycle identities and 2304 projection identities checked; epsilon is not idempotent and the corresponding minimal automorphism does not lift.')
row('H.5','Every additive-polynomial automorphism f over an F2-algebra with f(1)=1 acts compatibly on every abelian Fermat stage.','Proved','Integral cocycle and matrix formulas; code/fgh_additive_lifts.py','Task H.3, abelian stages','The polynomial T+epsilon(T^2-T) is detected on F4[epsilon], not on F2[epsilon]-points.')
row('H.6','A coordinatewise additive automorphism on a Heisenberg abelianization extends to a group automorphism only if it is multiplicative; the displayed nonlinear example fails.','Proved','Explicit class-two commutator identity; code/fgh_additive_lifts.py','Task H.3, conditional nonabelian obstruction','This is a complete counterexample for the stated Heisenberg model. It is not asserted to settle the canonical Fermat nonabelian model at 2.')
row('H.7','Actual profinite actions on each integral abelian stage are affine linear with a precise identity criterion, and the joint full-prime abelian-stage kernel is the kernel on the full metabelian quotient.','Proved','Intersection of closed commutators of K_n equals F second derived group','Task H.1; Task H.2','The criterion is genuine-action and choice-dependent; it is not an unqualified outer-action assertion.')
row('H.8','The nonlinear additive-polynomial direction is outside the actual profinite signed-action image on the integral abelian stages.','Proved','H.7 and nonzero quadratic coefficient','Task H.1; Task H.3','Ambient group-scheme kernel directions and retained profinite source images are different objects.')

row('G.8','Malkin’s cited depth-two Hodge results do not provide the unconditional motivic-to-5-adic comparison required by Lead15.','Known','Malkin Theorems11,16 and conditional discussion before Lemma3','Task G.1; Lead15','The primary source explicitly conditions the realization transfer on motivic formalism and regulator injectivity.')
row('H.9','The rank-five naive Hall class-two group scheme cannot carry the verified modular rho action after reduction modulo2.','Proved','H.4; code/fgh_hall_models.py','Task H.3, integral model obstruction','rho sends e2 to e1+e4; their squares are incompatible, for every central lift.')
row('H.10','The same rational class-two group and designated abelian quotient admit integral models with opposite nonlinear-lift behaviour at2.','Proved','H.6; code/fgh_hall_models.py','Task H.3, model specification','The laws with central terms ab-prime and 2ab-prime are rationally isomorphic; their characteristic-two fibres differ.')

row('Lead 14','The localic intersection and Hausdorff point/residual assertions are true, but the unrestricted classifying-topos replacement assertion is false.','Refuted','F.7,F.8,F.10,F.17,F.18','Lead 14; Task F.1; Task F.3','Discrete tails have no countable terminal coproduct.',where='sections/F.tex')
row('Lead 15','Rationality of the actual degree-eight arithmetic scalar remains unproved and unrefuted.','Open','G.1,G.4–G.7','Lead 15; Task G.1','The stated universal constraints alone are insufficient.',where='sections/G.tex')
row('Lead 17(a)','The complex normal-crossings punctured homotopy limit is the tangent torus, despite an empty strict intersection.','Proved','F.4,F.9','Lead 17(a); Task F.4','Coordinate polydisc cofinality is stated.',where='sections/F.tex')
row('Lead 17(b)','The number-field rational-cusp homotopy fixed points form the completed Kummer torsor, with no lim1 term, trivial pi1, and dense proper rational tangent subset.','Proved','F.4; Stix Theorem 14, supplied version','Lead 17(b); Task F.4','Point/cusp packet injectivity hypotheses are checked.',where='sections/F.tex')
for suffix,statement,status,dep,note in [
 ('A-manifold','The countable open-neighbourhood inverse limit is Sh(K minus Z).','Proved','F.15','Locally compact Hausdorff manifold; K need not be closed.'),
 ('B-manifold','Nested closed compact blow-up stages have the blow-up fibre as their sheaf-topos limit.','Proved','F.9','Stages must be closed in one fixed ambient blow-up; merely saying compact in a non-Hausdorff setting is insufficient.'),
 ('C-manifold','The zero strict chain limit and shifted lim1 torus-homology identities hold.','Proved','F.12','A decreasing basis at a normal-crossings point is used.'),
 ('A-stack','The intrinsic open-substack version holds for an étale stack with locally compact Hausdorff atlas.','Proved','F.16','Chartwise neighbourhood choices not defining open substacks are excluded.'),
 ('B-stack','The unrestricted identification with a geometric point fibre is false; the intrinsic residual-gerbe version is true for closed nested stages.','Refuted','F.6,F.16','BC2 times a disk distinguishes the fibres.'),
 ('C-stack','The unrestricted torus-homology formula is false for stacks with isotropy.','Refuted','F.6,F.12','The actual homotopy fibre retains BC2 and H1 torsion.'),
 ('scheme-limit','The strict henselian normal-crossings punctured scheme has the inverse-limit étale topos.','Known','F.2; Stacks 0EYL','Regular strict henselian local ring in characteristic zero.'),
 ('scheme-finite','Its finite coverings are finite continuous Zhat(1)^r-sets.','Known','F.2; SGA 1 XIII 5.3','r is the number of geometric branches.'),
 ('scheme-classifying','At a point on the divisor, the limit is a classifying topos exactly in local dimension one.','Proved','F.2','Dimension greater than one supplies a proper nonempty open subterminal.')
]:
 row('Lead 21 '+suffix,statement,status,dep,'Lead 21; Task F.6',note,where='sections/F.tex')
# The earlier working register had duplicate, unnumbered lead rows.
# Fold their answers and qualifications into the actual numbered statements.
lead_anchor = {
 'Lead 14':'F.8', 'Lead 15':'G.1',
 'Lead 17(a)':'F.4', 'Lead 17(b)':'F.4',
 'Lead 21 A-manifold':'F.15', 'Lead 21 B-manifold':'F.9',
 'Lead 21 C-manifold':'F.12', 'Lead 21 A-stack':'F.16',
 'Lead 21 B-stack':'F.6', 'Lead 21 C-stack':'F.6',
 'Lead 21 scheme-limit':'F.2', 'Lead 21 scheme-finite':'F.2',
 'Lead 21 scheme-classifying':'F.2'
}
numbered = {r['id']:r for r in rows if not r['id'].startswith('Lead ')}
for r in rows:
 if not r['id'].startswith('Lead '):
  continue
 target=numbered[lead_anchor[r['id']]]
 if r['id'] not in target['answers']:
  target['answers'] += '; '+r['id']
 target['notes'] += (' ' if target['notes'] else '')+r['id']+': '+r['statement']+' '+r['notes']
rows=sorted(numbered.values(),key=lambda r:(r['id'][0],int(r['id'].split('.')[1])))
import re
paper_ids=set()
for part in 'FGH':
 paper_ids.update(re.findall(r'\\begin\{statement\}\{([FGH]\.\d+)\}',
                            Path(f'LM8_PUSH/sections/{part}.tex').read_text()))
assert {r['id'] for r in rows}==paper_ids
Path('LM8_PUSH/notes/fgh_results.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
assert len({r['id'] for r in rows})==len(rows)
assert all(set(r)=={'id','statement','status','where_proved','depends_on','answers','notes'} for r in rows)
print(f'Wrote {len(rows)} numbered F/G/H rows; all 13 lead duplicates merged; paper IDs and required fields validated.')
