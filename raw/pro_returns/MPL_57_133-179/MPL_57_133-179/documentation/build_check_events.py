#!/usr/bin/env python3
"""Record research checks actually performed; transcription alone is not a check."""
from pathlib import Path
import json,csv

ROOT=Path(__file__).resolve().parents[1]
notes=json.loads((ROOT/'documentation/research_items.json').read_text())
DATE='2026-11-18'
rows=[]
def who(agent='root'):
    return f'GPT-6 Astra Pro; effort inherited/not exposed; run MPL_57_133-179; {agent}'
def event(statement,typ,outcome,agent='root'):
    rows.append([statement,DATE,who(agent),typ,outcome])

proofs={
 'FW05':'Checked chain condition for (x,1):[R--x^2-->R] to [R--x-->R], degrees 0,1, and residue-field maps (0,1). Equal fibre dimensions and top identity do not verify this map. Not a Poincare-theorem counterexample.',
 'FW06':'For a geometric point, invertible n>1 and Y empty, checked U=X proper and H_c^0(X,mu_n)=mu_n nonzero. The two-row description requires nonempty boundary fibres; Kummer identity not proved.',
 'P02':'Checked the constant integer-group monomorphism into G_a in characteristic zero by distinct fibres; its non-quasi-compact domain makes it nonaffine. Tests the warning, not the Picard-kernel theorem.',
 'P03':'Restricted the written tensor formula to the identity section of P^1 with L=O(1): it gives O(2), not a trivial bundle. Verified that inserting the inverse canonically trivializes the restriction; no source edit.',
 'P07':'Computed the diagonal unit quotient for one and two labelled sections, and the ratio map with diagonal kernel. H^1(S,G_m)=Pic(S) supplies the split two-point control case.',
 'P09':'Counted the three F_2-points of P^1 and removed 0,1,infinity; the complement has no section. Conditional test under the source vanishing conclusions only; no independent proof of xi_n=delta_n(eta) or of xi_n vanishing.',
 'C02':'Computed node/cusp normalization defects and the three-branch planar normalization quotient degree by degree; dimensions 2+1+0+... give defect3, while coordinate axes give defect2. Reviewed independently by fourier_witness_research.',
 'C03':'Applied the explicit one-branch cusp defect to the source decomposition: graph rank zero but additive dimension one. Refutes a graph-only properness inference, not the combined source criterion.',
 'C05':'Substituted rho=c1-c0+1 into the displayed polynomial for a connected unmarked nodal graph and obtained 3g-3-c1+lambda. No moduli, smoothness, product, or arithmetic theorem checked.',
 'D02':'Used X=P^1, L=O(1), j=id: postcomposition stabilizer is trivial but Aut(X)=PGL_2. Conditional objection to the literal uncertain parenthesis, not to a correctly specified framed datum.',
 'D04':'Applied cohomology to the effective-Cartier sequence with L=O_X(Y); verified the connecting degree H^1(L|Y) to H^2(O_X). No resolution of the ink exponent or proof of relative representability.',
 'N01':'Checked the doubled-origin counterexample to dense-open uniqueness for nonseparated targets and the closed-equalizer/schematic-density argument for separated targets.',
 'N03':'Verified A=k+(x,y)^2 finite type, dimension2, finite normalization k[x,y], punctured two-open regularity, and x outside A_m despite nonnegative height-one valuations. Explicit proof reviewed independently; only the first NB in its unqualified reading is refuted.',
 'N04':'Separated the height-one intersection criterion (normality) from proper-target local extension at DVRs (R1). Verified applicability of Stacks0BX7 to integral varieties; no arithmetic-section assertion checked.',
 'Q02':'Checked low-degree Leray and the retraction supplied by a section, making H^2 pullback injective; related uniqueness of rigidified descent on the stated site. No representability or site-comparison theorem proved.',
 'Q05':'Checked O(1) and O on P^1 agree in Pic on the two standard affine charts but differ globally in degree; the absolute Picard presheaf is not a Zariski sheaf.',
 'U01':'Substituted a basis vector or a Bezout vector in the source Koszul homotopy to verify annihilation by generators and contraction for a unit ideal.',
 'U03':'Checked dim=depth=0 for k over k[[t]] and nonfreeness from t-torsion. Historical codim-coh terminology checked in SGA1 I9. No omitted full-support hypothesis supplied.',
 'U05':'Assuming the source estimates, divided its inequality by h^2 and used a>0 and positive integral m to obtain m=1. The analytic surface inputs were not independently proved.'
}
for n in notes:
    ident=n['id']
    if ident in proofs:
        event('MPL_57_133-179 '+ident,'targeted proof check',proofs[ident],n['researcher'])
    elif n['event']=='proposal':
        event('MPL_57_133-179 '+ident,'carried as background without fault found',
              'Editorial proposal only: '+n['title']+'. Source and context scope were compared, but the proposed cocycle identification and sign were not proved.',n['researcher'])
    else:
        event('MPL_57_133-179 '+ident,'used and rechecked in this run',
              'Documentary/interpretive scope check, not a theorem proof: '+n['title']+'. Frozen locator: '+n['where']+'. Compared with '+n['comparison'],n['researcher'])

# Additional check events on statements, distinguished from documentary reading.
event('MPL_57_133-179 R05','targeted proof check',
      'Identity-section test X=S=P^1: the absolute class O(1) cannot be rigidified, whereas its relative class is zero. Motivates the prime/quotient question; source reading unchanged.')
event('MPL_57_133-179 R11','targeted proof check',
      'Identity X=Sigma=S=P^1 gives last absolute Picard arrow Z to0; it is not an isomorphism, but quotienting by Pic(Sigma) gives the correct zero group.')

refutations=[
 ('P57 57:138 L18; tensor formula without inverse','MPL_57_133-179 P03.corrected',
  'Counterexample O(1) on the identity P^1 section; refined formula is L tensor phi^*(g^*L)^(-1), as stated in P03.'),
 ('P57 57:170 L7; first NB applied without exception to 169 L20-26','MPL_57_133-179 N04',
  'Explicit A=k+(x,y)^2 counterexample. Refined regular-function criterion retains normality/R1+S2; proper-target theorem still uses R1. A possible intended codimension-two exception is not excluded.'),
 ('P57 57:136 L3; unqualified CM implies free over regular local ring','MPL_57_133-179 U04',
  'k over k[[t]] is finite CM but not free. Corrected statement requires maximal CM; scope conditional on the visible definition and no omitted full-dimension assumption.'),
 ('P57 57:138 L11; last unquotiented hom is an isomorphism','MPL_57_133-179 R11.quotient',
  'Identity P^1 gives Z to0. Refined statement is surjectivity followed by the quotient identification displayed on the source; no alteration of isom in the transcription.'),
 ('P57 57:174 L19 read literally for absolute Prepic','MPL_57_133-179 R05.relative_class',
  'The identity-section O(1) example refutes the unprimed absolute-class reading. Relative/primed classes permit the rigidified representative, under the stated hypotheses; intended shorthand remains a reading question.'),
 ('P57 57:162 L8 read as triviality of all Aut_S(X)','MPL_57_133-179 D02.stabilizer',
  'P^1 identity map has trivial postcomposition stabilizer but nontrivial automorphism group. Refinement concerns the automorphisms/stabilizer of the specified framed datum; surrounding manuscript reading is uncertain.'),
 ('P57 57:142 L12-19 if empty puncture fibres are allowed','MPL_57_133-179 FW06.nonempty_boundary',
  'Over a geometric point with Y empty, H_c^0 is nonzero. Refine the two-row setup by nonempty boundary on every fibre, in line with the later surjectivity proviso.')
]
for sid,refined,outcome in refutations:
    event(sid,'refuted, with refined statement ID',outcome+' Refined statement ID: '+refined+'.')

rs_status={
 'WG2 §1.1 #3':'Unchecked dossier/planning orientation; no direct theorem used for unrelated reused leaves or title evidence.',
 'WG2 §2.4 #4':'Exact carry-questions; compared the stated maps/theorems and all current frozen page text; bounded negative findings only.',
 'WG2 §2.3 #12':'Unchecked programme summary; exact theorem targets taken from CT44, not upgraded from the register.',
 'WG H9':'Unchecked height/Hodge reduction hunch; no required pairing, normalization or positivity proof supplied here.',
 'LM7 E.23':'Open full section-class classification; abelian input only, status unchanged.',
 'LM6 E.21':'Open image/fibre classification; current Picard data do not solve it.',
 'ANABELIAN_149_PUSH A.1':'Proved according to the return; used only as a semiabelian Kummer input; not rederived.',
 'SECTIONS_OVER_Q A.198':'Proved according to the return; generalized-Jacobian/norm-one bridge cited, not rederived.',
 'LM6 F.43':'Proved according to the return; normal-line torus comparison only, no independent proof.',
 'CYCLOTOMIC_KERNEL C1':'Proved according to the return; H1 torsor carefully distinguished from the current H2 constructions.',
 'ANABELIAN_149_PUSH B.5':'Known according to the return; degeneration/inertia bridge cited, not proved from graph rank.',
 'SECTIONS_OVER_Q B.15':'Open birational/valuative section assertions; ordinary proper-target map extension does not settle them.',
 'EXIT_TOWER A.5':'Headline checkpoint28 summary claim only; no stratum product/asphericity/fundamental-group theorem checked.',
 'MPL_57_271-315 C04':'First-pass pinching/unit-quotient lead; underlying scans not checked here.',
 'MPL_57_271-315 D07':'First-pass extension-versus-splitting lead; underlying scans/literature not checked here.',
 'MPL_57_271-315 E08':'First-pass torsion/rank distinction lead; no continuity theorem checked.',
 'MPL_57_271-315 J03':'First-pass ordinary-endpoint limitation; independently compared current selection with CT44, but earlier underlying scans not audited.'
}
used_rs=sorted(set(r.strip().rstrip('.') for n in notes for r in n['rs']))
for sid in used_rs:
    assert sid in rs_status, sid
    event(sid,'carried as background without fault found',rs_status[sid])

cn=['F1','F4','F7','F8','D06','D07','D08','D09','D10','D12','D13','D14']
cn += ['44:2:'+str(i) for i in range(1,6)] + ['44:4:'+str(i) for i in range(1,7)]
sn=['F01','F02','F03','J01','J02','J03','J04','J05','J06','J07','P02','P04','P05','P06','P09','E01','E06','E07','E08','C04','I03','D07','D09','C09','R04','§9']
for key,items in [('CN',cn),('SN',sn)]:
    for sid in items:
        event(f'{key} {sid}','carried as background without fault found',
              'Earlier supplied research lead used at its stated scope in the current notes; its underlying source scans and external bibliography were not independently verified merely by this use. See per-note context comparison and search record.')

primary={
 'Laumon 1996, Theorem1.2.4/Lemma1.2.5':'Primary-reference scope checked; main note FW07. No independent proof or second manuscript witness.',
 'Jannsen 1988, Proposition1.6/formula3.1':'Inspected inverse-limit exact-sequence statement, including lim^1; used to qualify P06, not independently reproved.',
 'SGA1 I9':'Inspected historical depth/cohomological-codimension terminology, printedp13/PDFp29; no reconstruction of missing manuscript hypotheses.',
 'SGA1 X3.3-X3.4':'Inspected regularity/purity and birational fundamental-group statement; used as known comparator in N06, not proved here.',
 'Stacks 031S/033P':'Inspected R1+S2 normality criterion; explicit N03 example supplies the actual counterexample independently.',
 'Stacks 0BX7':'Inspected assumptions and neighbourhood extension at a valuation local ring; verified application to N04.',
 'Stacks 0EMH/0EMF':'Inspected sufficient hypotheses for usual meromorphic-function sheaf; no claim of exact identification with every pseudo-function definition.',
 'Stacks 00N2/00NT':'Inspected CM/maximal-CM distinction and corrected freeness statement; U03 residue-module counterexample checked directly.',
 'Stacks 0952':'Inspected distinction between arbitrary-ring stable Cech R-Gamma_Z and right-derived module torsion R-Gamma_I; no extra noetherianity imposed on the former.'
}
for sid,outcome in primary.items():
    event(sid,'used and rechecked in this run',outcome)

event('HUA 57.modern.tex, complete supplied file','used and rechecked in this run',
      'Research comparison only: package_validation_tools read all2975lines, both context READMEs, full RS and later notes; root reviewed cited relevant sections. Modernization not treated as a diplomatic witness; no transcription changes.',
      'package_validation_tools + root')
event('MPL_57_133-179 N03/U03 independent example review','targeted proof check',
      'jacobians_earlier_forms independently checked the normalization/localization and CM examples and historical terminology; see research_counterexamples_review.md.',
      'jacobians_earlier_forms')
event('MPL_57_133-179 C02/C05/Q02 research review','targeted proof check',
      'fourier_witness_research independently checked triple-point quotient, graph arithmetic and Leray/site scopes; wording corrections incorporated. No manuscript scans read.',
      'fourier_witness_research')

with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    w.writerow(['statement_id','date','who','type','outcome'])
    w.writerows(rows)
print(json.dumps({'events':len(rows),'note_ids':len(notes),'rs_ids':len(used_rs),
                  'types':{t:sum(r[3]==t for r in rows) for t in sorted(set(r[3] for r in rows))}},indent=2))
