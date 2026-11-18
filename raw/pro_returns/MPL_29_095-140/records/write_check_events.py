#!/usr/bin/env python3
"""Write the exact mathematical check events completed in this research run."""
from pathlib import Path
import csv,json,datetime
R=Path(__file__).resolve().parents[1]
DAY='2026-11-18'
MODEL='GPT-6 Astra Pro; effort setting not exposed; run MPL_29_095-140'
events=[]
def add(s,who,typ,outcome):
 events.append([s,DAY,MODEL+'; '+who,typ,outcome])
refuted="refuted, with the refined statement's id"
add('N002','notes_inertia',refuted,'Hua unrestricted arithmetic centrality refuted by F4((u))/F2((t)), u^3=t, with inertia C3 and Frobenius inversion; refinement N002.R1 retains the cyclotomic action. Scan096 itself does not assert centrality. Proof C1.')
add('29-formal-tame-pi1-self-intersection','root',refuted,'Only the unrestricted arithmetic centrality clause of the Hua findings-register entry is refuted by proof C1, also recorded under N002. Refinement N002.R1 retains the cyclotomic action on inertia and restricts centrality to a trivial action on the relevant quotient. This event does not refute or prove the remaining Chern-class classification or its geometric hypotheses.')
add('N003','notes_inertia','targeted proof check','The implication Pi2=0 implies split central extension fails for the explicit integral Heisenberg extension of Z^2. No full formal-geometric counterexample is claimed. Proof C2.')
add('N004','notes_inertia','computation or formal certificate','Elementary cokernel computation: for tame Tate group T, coker[d]=T if d=0, and has order equal to the prime-to-p part of |d| if d is nonzero. Conditional on the source exact sequence and degree map; no machine certificate. Proof C3.')
add('N010','notes_inertia','targeted proof check','Invariant cyclic subgroups need not commute: the two order-four subgroups of Q8. This is only a group-theoretic hypothesis diagnostic, not a geometric refutation. Proof C4.')
add('N011','notes_inertia','independent re-proof','For finite-dimensional E over any field, automorphisms F,G and integer q>1 with FGF^-1=G^q imply G quasi-unipotent, by the finite nonzero spectrum and Cayley-Hamilton. Not the complete geometric monodromy theorem or LM1 E.2/E.11. Proof C5.')
add('N012','notes_inertia','targeted proof check','H2 on finite constant abelian coefficients preserves kernels and finite products if H1 vanishes for every such coefficient. No right exactness, universal-cover continuity, or homotopy comparison asserted. Proof C6.')
add('N025.R1','notes_torsors','independent re-proof','With geometrically injective kernels and finite étale quotients, the infinitesimal kernel is unique over arbitrary S: a clopen identity preimage contains all geometric points. Reducedness and connectedness unused. Supports N025; proof A.')
add('N027','notes_torsors',refuted,'The contextual two-sections assertion for arbitrary reduced connected P is refuted by sections 0,t of A1 over k[t]. Refined statement N027.R1 restores the admissible torsor hypothesis. Proof B.')
add('N027.R1','notes_torsors','independent re-proof','For reduced connected S and a finite locally free admissible G with finite étale quotient, two sections of a G-torsor agreeing at one geometric point coincide; inner twisting gives pointed automorphism rigidity. Proof C.')
add('N019','root','used and rechecked in this run','Uses only the qualified rigidity statement N027.R1, independently rechecked through the clopen étale quotient and reduced-base equalizer arguments. The full exactness and pro-representability claims are not proved here.')
add('N032','notes_torsors',refuted,'All admissible finite flat S-groups are not closed under equalizers: Eq(0,[t]) in alpha_p over k[t] has algebra k[t,T]/(T^p,tT), hence is nonflat. Refinement N032.R1 requires separate equalizer flatness/closure. Proof D1.')
add('N033','notes_torsors',refuted,'Broad minimality-injectivity assertion for all admissible S-group morphisms fails on A=k[t^p,t^(p+1)]: pointed z^p=x is minimal, but 0 and [x] both have pointed-trivial pushforward. Refined N033.R1: reduced connectedness is insufficient and a valid argument must supply an admissible flat reduction; no full sufficiency theorem claimed. Proof D2.')
add('N030','root','targeted proof check','The minimality inference needs admissible H=Eq(u,v) and a pointed H-torsor reduction R; D1 and D2 directly exhibit failures of those flatness steps. Does not verify the later context-only categorical proof.')
add('N036','notes_local',refuted,'Hua converse I intersection J=IJ implies I+J=A refuted by (x),(y) in k[x,y]. Refined N036.R1 is the correct CRT chain in scan108. Proof P1.')
add('N036.R1','notes_local','independent re-proof','A/IJ to A/I times A/J is surjective iff I+J=A; then I intersection J=IJ and the map is bijective, without a finiteness hypothesis. Proof P1.')
add('N037','notes_local',refuted,'Monic-factor assertion without constant ranks is refuted over k times k by ideals k[T] times (T) and (T) times k[T]. Refined N037.R1 retains nonzero connected base (or constant quotient ranks). Proof P2.')
add('N037.R1','notes_local','independent re-proof','Over a nonzero ring A with connected spectrum, comaximal ideals J,Jprime with JJprime=(P), P monic, have unique monic generators Q,Qprime with P=QQprime. Characteristic polynomials on finite projective quotient summands prove it without noetherian or completeness assumptions. Proof P3.')
add('N038','root','used and rechecked in this run','Uses N037.R1 as an independent completion, not as a recovery of scan110 missing words; root checked the constant-rank, Cayley-Hamilton, equal-rank-surjection, and uniqueness steps.')
add('N039','notes_local','targeted proof check','Spec C over R distinguishes invariance between algebraically closed fields from invariance under all algebraic separable extensions: F(R) empty, F(C) has two points. Does not resolve the source wording, establish an implication between general conditions, or refute the full representability criterion. Proof P5.')
add('N041','notes_local',refuted,'Cartesian cocycle-compatible localization data alone need not glue: the Q[t] example would force an étale image with infinite non-open complement. Refined N041.R1: additional neighborhood compatibility of appropriate geometric models is necessary; sufficiency of the source insertion is not proved. Proof P4.')
add('N051','root','targeted proof check','For A=C[[x,y]], finite étale algebras split into copies of A by henselian idempotent lifting and rank-one factors. Thus full Spec A has trivial pi1; no proof of the intended punctured/formal patching diagram is claimed. Proof R1.')
add('N052','root','targeted proof check','For D=(x) on A1 and invertible n>1, [Spec k[z]/mu_n], x=z^n, has trivial off-divisor stabilizers, whereas the root gerbe of O(D) has mu_n everywhere. Distinguishes these constructions; no full archival-category equivalence asserted. Proof R2.')
add('N053','root','used and rechecked in this run','Stacks03PK Kummer argument rechecked: A[T]/(T^n-a) for a unit a is finite free faithfully flat; it is étale when n is invertible because nT^(n-1) is a unit. Topology distinction only; no Chern cocycle comparison proved. Proof R3.')
add('N056','root',refuted,'Pointed rigidity without reducedness fails for trivial alpha_p over k[epsilon]/epsilon^2: sections 0,epsilon and translation by epsilon agree at the geometric marking. Refined N056.R1 retains reducedness and the hypotheses of N027.R1. Proof R7.')
for s,proof in [('N002','C1'),('N003','C2'),('N004','C3'),('N010','C4'),('N011','C5'),('N012','C6'),('N025.R1','A'),('N027.R1','C'),('N032','D1'),('N033','D2'),('N036.R1','P1'),('N037.R1','P3'),('N041','P4')]:
 add(s,'root','used and rechecked in this run',f'Root independently examined the written argument {proof}, its assumptions and the scoped conclusion recorded above; no larger theorem or novelty conclusion is added. See root support and the relevant full proof.')
review=R/'records/review_torsor_checks.md'
if review.exists():
 for s,proof in [('N025.R1','A'),('N027.R1','C'),('N032','D1'),('N033','D2')]:
  add(s,'notes_inertia peer review','targeted proof check',f'Independent review of torsor proof {proof}: no defect under the stated hypotheses; variable S-group maps, geometric pointing, repaired proper-subgroup minimality and flatness scope retained. records/review_torsor_checks.md.')
review=R/'records/review_local_checks.md'
if review.exists():
 for s,proof in [('N036.R1','P1'),('N037','P2'),('N037.R1','P3'),('N041','P4'),('N039','P5')]:
  add(s,'notes_torsors peer review','targeted proof check',f'Independent review of local proof {proof}; no defect with stated scope. P4 requires the weakened-statement target and appropriate geometric neighborhood models; P5 distinguishes quantifiers without proving a global implication. records/review_local_checks.md.')
with (R/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)
(R/'records/check_events_data.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
print(f'{len(events)} actual mathematical check events recorded')
