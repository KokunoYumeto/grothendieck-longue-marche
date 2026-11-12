"""Assemble the statement, requirement and editorial ledgers without inference.

The mathematical entries are authored below and in sections/*_results.json.
This script checks identifier coverage and emits the requested CSV files and
report; it makes no mathematical proof claim of its own.
"""
import csv
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FIELDS=['id','statement','status','where_proved','depends_on',
 'manuscript_passages (section; page; scan)',
 'depends_on_doubtful_reading (scan, alternatives)','notes']

def row(i,statement,status,dependencies,passages,tasks,notes='',reading='none'):
    return dict(zip(FIELDS,[i,statement,status,'CYCLOTOMIC_KERNEL_paper.tex; res:'+i,
                           dependencies,passages,reading,notes]),tasks=tasks)

ROOT_ROWS=[
 row('A9','The tangential U03 centralizer is <x>; y and [x,y] are not fixed. The commutator has a nonzero Fermat-cubic Jacobian image and a nonconstant Ihara multiplier.','Proved','A1;A6;SGA1 XII.5.1;Kodani2017 Lemma4.3.1,(4.3.2)','3;27;55–56 | LM34;245;483',['A(f)'],'Exact Fermat incidence and boundary matrices run for n=2,3,4,5.'),
 row('C1','The cusp decomposition extension is the arithmetic normalizer; its centralizer is its cyclotomic-kernel preimage. Splitting classes form the completed Kummer H1 torsor.','Proved','A2;Hilbert90 argument','3;26;53–54',['C(a)','5'],'The visible word centralisateur is retained as evidence; normalizer is the proved mathematical correction.','54: centralisateur versus normalisateur; completed K* versus K*'),
 row('C2','Hyperbolic cusp packets embed in section classes and are pairwise disjoint and disjoint from point sections, including type(0,3).','Proved','A1;A6;Stix2008 Theorem14;EsnaultHai2008 Theorem5.5,Lemma5.6','3;26–27;54–55',['C(a)','5']),
 row('C3','The first Proposition54 assertion fails for type(0,2): on Gm each cusp packet is the whole Kummer section space and includes every point section.','Refuted','C1;Gm Kummer covers','3;26;54',['C(a)','5'],'The other exceptional geometric types are computed explicitly.'),
 row('C4','Point sections have cyclotomic centralizer 1 and cuspidal sections have precisely their inertia; the assertions hold for germs.','Proved','A6;A7;C2','3;27;55–56',['C(b)','6','11'],'The converse from trivial centralizer to a point is not asserted.'),
 row('C5','Elementary hyperbolic fibrations have injective geometric homotopy exact sequences and the rational-fibre arithmetic pullback identification.','Proved','SGA1 XII.5.1;Bresciani2021 Lemmas10.9–10.11,A.22;B_Hoshi2014 Prop2.4','2;24;49',['C(c)','4','E(a)'],'Finite-kernel proof of completion exactness included.'),
 row('C6','Point-section centralizers vanish in every dimension of an elementary hyperbolic tower; morphisms satisfy condition b for every open H in E_V°.','Proved','C4;C5;B1;B6','2;23–24;48–49',['C(c)','3','4','E(a)'],'Quantifier over H preserved by choosing a closed point on the corresponding finite cover.'),
 row('C7','The point case of condition b identifies exactly the noncuspidal section subset; its exhaustion by point sections has exactly the Conjecture A surjectivity defect.','Proved','A6;A7;C2;C4','2;23–24;48–49 | 3;27;56',['C(d)','3','6'],'Unresolved existence already for an arbitrary noncuspidal U03 section over Q.'),
 row('C8','Boundary-local sections of elementary hyperbolic polycurves have nonzero cyclotomic centralizer. Local inertia injectivity fails after a blowup, with map(m,n)->m+n.','Proved','B_Hoshi2014 Lemma2.8,Prop2.4;C5;local Kummer covers','4;63–65;128–131',['C(d)','E(a)'],'The converse requires a boundary-local factorization; its product case already forces curve section surjectivity. Exact blowup matrix checks attached.','130: injectivity claim explicitly withdrawn;131: geometric target subscript'),
 row('C9','Admissible germs are exactly noncuspidal germs, with an equivariant injection of U03(Qbar); equality is the section-surjectivity assertion over all number fields.','Proved','A6;A7;C2;D0b','3;32;66',['C(g)','9'],'Whole-G_Q section classes carry trivial transport; the required action is on germs.','66: à deux? cas près; whole sections versus germs'),
 row('C10','Inertia groups are precisely the nonzero C(s) for germs and the maximal procyclic groups with open cyclotomic normalizer. The unqualified maximal-subgroup criterion is false.','Proved','A6;Stix2008 Theorem20,Cor21;E2;E3','LM34;245;483 | 3;27–28;55–57',['C(h)','11'],'The character-free maximal-procyclic full-group criterion remains unresolved. Explicit S3 quotient checked.'),
 row('D0a','The finite-fibre/rational-function topology identifies continuous sections with compatible semilinear actions over U; fixed pro-points give point or cusp stabilizers.','Proved','Galois-category construction;A2','3;29–30;59–61',['D(a)','7']),
 row('D0b','Over finite cyclotomic closures and their finitely generated extensions every section fixes at most one completed-cover pro-point. For a full arithmetic section the Γ° and Γ fixed sets coincide.','Proved','A1;AE1;EsnaultHai2008 Lemma5.6;Jacobian Kummer comparison','3;29–30;59–61',['D(b)','7'],'This proves uniqueness in all cases, including affine interior points; it does not establish existence.'),
 row('E1','For the CM punctured elliptic curve over Q(i), the actual Δ=G_Kab action fixes all of N2, while the Γ° fixed subgroup is its centre. The full centralizer maps to zero in abelianization and to the centre in N2.','Proved','A1;A6;SGA1 XII.5.1;explicit [-1] tangential involution','LM34;245;483 | 3;27,30;55–56,61–62',['A(f)','E(c)'],'No guessed arithmetic matrix is used; the rational pro5 involution kills the class-two shear.'),
 row('E2','A primitive CM eigenline in N2 is maximal procyclic, has normalizer surjecting onto G_K, and has nonzero abelian image while cusp inertia has zero abelian image.','Proved','E1;Heisenberg conjugation identity','LM34;245;483 | LM3b;D.5;not a manuscript scan',['E(c)','C(h)'],'Checked all conjugations modulo5,25,125; no lift to the full group asserted.'),
 row('E3','Every nilpotent quotient of finite class N_r has its last central layer fixed by Δ and nonperipheral fixed elements for r>=3; the full compatible fixed subgroup remains undetermined.','Open','E1;Magnus finite-quotient certificate','LM34;245;483 | LM3b;D.4–D.5;not a manuscript scan',['E(c)','C(h)'],'Lyndon bracket calculations through degree10; exact first obstruction in H1(Δ,γ3/γ4) and compatible inverse-limit condition stated.'),
]

REQUIREMENTS={
 '1':('B1 B2 B4 B5 B6','proved','The stated centralizer assertion holds; all arithmetic-to-geometric and inverse-limit maps are supplied.'),
 '2':('B7 B9','partly settled','Relative transcendence degree one: exact equivalence with birational section surjectivity. An arbitrary section for Q(t)/Q is the smallest unresolved instance; higher transcendence degrees are not exhausted.'),
 '3':('C5 C6 C7 C8','partly settled','Necessity proved for all open subgroups and all elementary towers. Sufficiency already contains the unresolved point case for U03/Q.'),
 '4':('C5 C6','proved','Point sections have centralizer 1 in every dimension of an elementary hyperbolic tower.'),
 '5':('A6 C1 C2 C3','refuted','The type(0,2) assertion is false. The normalizer extension and all hyperbolic packet assertions, including(0,3), are proved.'),
 '6':('A6 A7 C4 C7 AE1','partly settled','All centralizer precisions and germ versions proved; exhaustion of sections by points and cusps remains unresolved over finitely generated fields over Q.'),
 '7':('D0a D0b C7','partly settled','The topology/dictionary and full Γ° uniqueness are proved. Existence remains the section-surjectivity problem, already for U03/Q.'),
 '8':('A7 D1 D2 D5 D6 D7 D8 D9 D10 D11 D12 D13','refuted','The blanket cyclotomic extension has an explicit proper genus 4 counterexample even for continuous actions. True uniqueness, centralizer and continuity comparisons are proved; see the unfinished D(e) row.'),
 '9':('C9','partly settled','Admissible germs identified exactly; equality with U03(Qbar) remains the section-surjectivity statement. The doubtful phrase does not repair the domain of whole-group sections.'),
 '10':('B6 B7 B8','refuted','The L formulas have value I_v for decomposition sections. Their equivalence is proved; replacing L by a model U containing the point gives value 1.'),
 '11':('C4 C6 C7 C10 E2 E3','partly settled','Cyclotomic loop recognition and necessity in the Faltings PS proved; unqualified subgroup criterion refuted; character-free maximal-procyclic lifting and point-section sufficiency remain.'),
 'R2':('A1 A2 A3 A4 A5 A6 A7','proved','Both requested uniqueness routes are complete; the direct route repairs the orbit-separation and covering gap.'),
 'R3':('B1 B2 B3 B4 B5 B6','proved','Independent valuation/Kummer proof and stronger Hilbertian proof; the auxiliary prime is also unramified in k.'),
 'H1':('AE2 AE3 AE4','refuted','The all-or-nothing cyclotomic-character conclusion fails. Correct primewise formula proved for nonzero centralizers and the full normal-subgroup case.'),
 'A(a)':('A1','proved','All four arithmetic consequences, including the two divisibility assertions, proved from the opened Ribet theorem.'),
 'A(b)':('A2 A3','unfinished','Inertia criterion and theorem comparisons proved; original Nakamura, Stix2008 and author2012 texts opened. The literal publisher PDF of Stix2012 remained security-blocked, so the requested published-text collation is incomplete.'),
 'A(c)':('A4 A8','proved','Characteristic-cover reduction, compact Jacobian vanishing, and all proper genera treated.'),
 'A(d)':('A5 A6','proved','Direct proof separates C-orbits and creates a cover with three cusps; Stix route verifies its arithmetic hypothesis.'),
 'A(e)':('A6 A7','proved','Full theorem, germs, open cyclotomic subgroups and arbitrary containing closed subgroups with explicit χ-fixed factors.'),
 'A(f)':('A9 E1 E2','proved','Fermat/Ihara commutator obstruction and actual CM class-two action proved; exact computations run.'),
 'B(a)':('B1 B2','proved','R3 audited line by line and compared with opened Hilbertian sources.'),
 'B(b)':('B4 B5','proved','Finitely generated fields, projective limits and all three à-vérifier assertions addressed with the rank qualification.'),
 'B(c)':('B2 B3','proved','Criterion for every proper Galois M/Q; all six named examples verified, including properness certificates.'),
 'B(d)':('B6 B8','proved','Arithmetic/geometric centralizers coincide; the two zero-formulas are equivalent but false with L for decomposition sections.'),
 'C(a)':('C1 C2 C3','refuted','Correct extension and Kummer torsor, injection, disjointness and(0,3) proved; printed type(0,2) claim refuted.'),
 'C(b)':('A6 A7 C4','proved','The precisions hold for sections and germs without assuming exhaustion.'),
 'C(c)':('C5 C6','proved','Homotopy exactness and the closed-point reduction with the universal open-subgroup quantifier are proved.'),
 'C(d)':('C7 C8','proved','Curve predicates are exactly equivalent; all boundary-local sections of elementary polycurves have nonzero centralizer. Exact remaining converse factorization obligation stated.'),
 'C(e)':('B7 B8 B9','proved','Compatible-cusp limit constructs the unique valuation; inertia equality and the model/function-field correction are proved.'),
 'C(f)':('B10 B11','proved','Nonzero-centralizer fibres are packets; germs and model quotients reconstruct points and opens, with the Isom input stated.'),
 'C(g)':('C9','proved','Unconditional germ description and precise section-conjecture exhaustion equivalence; both doubtful readings retained as editorial uncertainty.'),
 'C(h)':('C10 E2 E3','partly settled','Cyclotomic characterization proved; full character-free maximal-procyclic assertion remains at the explicit compatible-lift obstruction.'),
 'D(a)':('D0a','proved','Topology and exact stabilizer dictionary defined and proved.'),
 'D(b)':('D0b','proved','At most one fixed pro-point in all, and equality of the Γ° and Γ fixed sets.'),
 'D(c)':('D1 D2 D3 D4','proved','Exact abelianized pairs, 7800 two-step branch checks, degree 81 separating cover, and full point injectivity for all hyperbolic curves.'),
 'D(d)':('B12 D5 D6 D7 D8 D9 AE1','refuted','Separate outcomes for every named theorem are recorded below. Conjecture A and Theorem3 fail in explicit cyclotomic examples.'),
 'D(e)':('D10 D11 D12 D13','unfinished','Common-cover equivalence, functorial completion and continuous descent proved; proper commensurator completion described. No unrestricted number-field action normalizing no deck group is constructed or excluded, and the affine automorphism description is not proved.'),
 'E(a)':('AE1 A6 A7 B4 B5 B7 C1 C2 C4 C5 C6 C7 C8','proved','Specialization proves torsion finiteness and divisibility vanishing; each required transfer uses the same explicitly described maps.'),
 'E(b)':('AE2 AE3 AE4','partly settled','Original normal H1 and all nonzero-centralizer cases proved, with exact arithmetic field criteria. For arbitrary nonnormal Δ with all χ_l nontrivial, uniqueness of fixed cusps from the stated Tate hypothesis alone remains undecided.'),
 'E(c)':('E1 E2 E3','partly settled','Actual N2 fixed group computed; all last layers fixed, calculations through degree10. Full compatible non-inertia invariant and full character-free normalizer remain undetermined.'),
 'E(d)':('D14 D15','unfinished','Good marked reduction prime-to-p groups computed for integral points and all cusp twists. Full-group calculations and bad marked reduction remain missing, with explicit Q5 instances and the nonabelian H1 lift obstruction.'),
 'D(d)-Theorem1':('B12 D8','proved','Centralizers of open subgroups vanish over F and finitely generated extensions, including the geometric group.'),
 'D(d)-Theorem2':('D6','proved','Kummer pullbacks and comparisons of a,a+1,a+i prove faithfulness of F-embeddings.'),
 'D(d)-Theorem3':('D1 D2 D7','refuted','Gm points 1 and ζ6 have the same section over F. Exact divisibility criterion and hyperbolic full injectivity replace it.'),
 'D(d)-Proposition54':('C1 C2 C3 D9','refuted','Hyperbolic packet assertion persists; type(0,2) remains a counterexample.'),
 'D(d)-Conjecture A':('D5','refuted','Proper genus 4 curve t6+2y3+4=0 has no F-points and has a continuous arithmetic section; the example persists over pure transcendental extensions.'),
 'D(d)-precisions':('A6 D9 AE1','proved','Point and cusp centralizer values persist; they do not classify every section over F.'),
}

READINGS=[
 ('MPL_149_001-090_transcription.tex','13–15','Three à vérifier; free profinite rank','B4–B5 give the limit passage. Torsion freeness holds in rank1, whereas centre/centralizer claims require nonabelian free rank.','Mathematical qualification proved; no silent alteration of the manuscript.'),
 ('MPL_149_001-090_transcription.tex','22','Théorème2: outer versus actual homomorphism','D6 uses the induced maps on H1, invariant under inner conjugacy; the statement is meaningful with the written outer ambiguity.','Strong mathematical support; the source map is specified.'),
 ('MPL_149_001-090_transcription.tex','32','Théorème3: abelianized point separation','D1/D7 identify the exact Kummer comparison and refute a blanket cyclotomic extension using roots of unity.','Proved correction to base-field scope; not an emendation of the number-field text.'),
 ('MPL_149_001-090_transcription.tex','45','E°_K′ defined as kernel of a composite beginning at E°_K′','The definition uses E_K′ -> Γ_Q -> Zhat*. With E°_K′ as the source it repeats the object being defined.','Strong mathematical support; upper-half scan inspected; manuscript symbol retained as evidence.'),
 ('MPL_149_001-090_transcription.tex','45','Margin: à vérifier, centralizer of Γ′°','B1 proves precisely the cyclotomic-kernel version. The auxiliary prime must be unramified in k as well as split in the selected auxiliary extension.','The statement is proved; this does not erase the author’s verification mark.'),
 ('MPL_149_001-090_transcription.tex','48–49','Direction of morphism and centralizer ambient group','E_V -> E_U is induced by V -> U. C6 preserves every open subgroup of E_V° and proves both arithmetic and geometric ambient readings.','The morphism comparison and both conclusions are proved; scan inspected.'),
 ('MPL_149_001-090_transcription.tex','54','son centralisateur Z(L_i); possible intended normalisateur','The surjective extension is N_E(I_c)=D_c. The actual centralizer projects onto kerχ. Over a cyclotomic base these coincide by the explicit action map.','Word appears centralisateur on scan; mathematical correction proved. Authorial intention is not declared settled.'),
 ('MPL_149_001-090_transcription.tex','54','K* versus completed Khat* in(3)','Splitting torsor is lim K*/K*^n, not merely the image of K*. C1 constructs the continuous cohomology comparison.','Strong mathematical support for the completion mark; no change to the scan.'),
 ('MPL_149_001-090_transcription.tex','54','Type(0,2) in the first Proposition assertion','Gm has both cusp packets equal to its entire Kummer section space, including its point sections.','Printed mathematical scope refuted; a missing exclusion cannot be silently supplied.'),
 ('MPL_149_001-090_transcription.tex','55','Formula(3), exponent Γ° and L_i','A6 proves π^{Γ°}=I_c for each cuspidal section, including type(0,3).','Strong: displayed exponent inspected and exact theorem proved.'),
 ('MPL_149_001-090_transcription.tex','56','Marginal précisions; conjectural exhaustion','C4 proves the two centralizer values. C7 separates the remaining surjectivity assertion by an exact equality of predicates.','Both margin values are theorems; the main Conjecture A is not proved here.'),
 ('MPL_149_001-090_transcription.tex','59','continue dans un sens convenable; conv. simple-discrète','D0a gives finite-fibre and rational-function topologies; D11 proves descent under open stabilizers.','Proved realization of the proposed topology, without inferring continuity where the manuscript omits it.'),
 ('MPL_149_001-090_transcription.tex','61','Γ° fixed point necessarily Γ-fixed','D0b proves at most one fixed pro-point in all. Normality sends its singleton to itself, giving equality of the two fixed sets.','Strong; the implication is proved directly and the scan inspected.'),
 ('MPL_149_001-090_transcription.tex','62','tous nos beaux énoncés; cyclotomic base','D5 supplies a proper genus 4 counterexample to existence, while D1–D2,D6–D9 identify surviving assertions and the toric failure.','Mathematical scope corrected by explicit examples; no doubtful word resolves this failure.'),
 ('MPL_149_001-090_transcription.tex','66','à ⟨deux ?⟩ cas près; sections versus germs','C9 proves the Galois-equivariant formulation for germs. Whole-G_Q section classes have trivial transport. Neither deux nor unspecified exceptional cases repairs this arithmetic-domain mismatch.','Word remains doubtful after scan inspection. Mathematics does not identify the intended exceptions.'),
 ('MPL_149_091-136_transcription.tex','127','Subscripts L in(32),(33), versus proposed U','B8 proves both L groups equalI_v for decomposition sections; the quotient E_L -> E_U killsI_v when the point lies inU, giving both zero formulas forU.','Both letters readL in the scan. Replacement of the mathematical assertion is proved; authorial intention is not settled.'),
 ('MPL_149_091-136_transcription.tex','128–130','T^{I(x)} and injectivity withdrawn in the margin','C8 computes the blowup map(m,n)->m+n with nonzero kernel, while proving nonzero image for elementary polycurves by the trait-extension criterion.','Exact counterexample confirms the withdrawal; the notation retains the actual image map.'),
 ('MPL_149_091-136_transcription.tex','131','Geometric target written π_{L/K} in boundary discussion','The local map from the punctured henselian neighbourhood lands in the model groupπ_U. The function-field and model maps are compared explicitly inB7–B8 andC8.','Mathematical target specified; visibleL is not silently emended.'),
 ('La_Longue_Marche_140-2','433','π^{Γ+}=1','For full arithmetic sections, the cyclotomic computation and the nontrivial cyclotomic action on each inertia factor give the corresponding trivial full fixed group. Germ and group domains are kept explicit.','Supports the fixed-group prediction in its stated hyperbolic number-field setting; scan inspected.'),
 ('La_Longue_Marche_140-2','483','Maximal subgroups with normalizer of open arithmetic image','π itself satisfies the unqualified condition; its S3 quotient proves it is not procyclic. C10 proves the maximal-procyclic cyclotomic repair; E2/E3 specify the character-free quotient evidence and lift obstruction.','Original unqualified assertion refuted; no character condition is inserted into the transcription.'),
 ('grothendieck_brief_an_faltings_GanF.pdf','PS','hinreichend und genügend; fixed group contains only1','C6 proves necessity for point sections. C7 identifies sufficiency on curves with the remaining section-surjectivity defect.','The two German words are retained as printed; mathematical directions are stated independently.'),
]

def main():
    rows=[]
    for name in ('A_agent_results.json','B_agent_results.json','D_agent_results.json'):
        p=ROOT/'sections'/name
        if not p.exists():raise RuntimeError('Required agent ledger not ready: '+str(p))
        rows.extend(json.loads(p.read_text()))
    rows.extend(ROOT_ROWS)
    byid={r['id']:r for r in rows}
    assert len(byid)==len(rows),'duplicate statement identifiers'
    for r in rows:
        r['where_proved']='CYCLOTOMIC_KERNEL_paper.tex; res:'+r['id']
        for short,full in (
            ('manuscript_passages','manuscript_passages (section; page; scan)'),
            ('depends_on_doubtful_reading','depends_on_doubtful_reading (scan, alternatives)')):
            if full not in r and short in r:
                r[full]=r[short]
        for f in FIELDS:r.setdefault(f,'')
        assert r[FIELDS[5]],('missing manuscript/source passage',r['id'])
        if r['id'] in {'D13','D15'}:r['status']='Open'
    ordered=[]
    for filename in ['A_agent.tex','A_root.tex','B_agent.tex','C_root.tex','B_birational.tex','D_root.tex','D_agent.tex','E_arithmetic_agent.tex','E_root.tex','E_local_agent.tex','E4_prior_hunches.tex']:
        p=ROOT/'sections'/filename
        if p.exists():
            for ident in re.findall(r'\\label\{res:([^}]+)\}',p.read_text()):
                assert ident in byid,('missing row',ident)
                ordered.append(byid[ident])
    assert len(ordered)==len(rows),(len(ordered),len(rows))
    with (ROOT/'CYCLOTOMIC_KERNEL_results.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS,extrasaction='ignore');w.writeheader();w.writerows(ordered)
    with (ROOT/'CYCLOTOMIC_KERNEL_readings.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['file','scan','the \\unsure or \\illegible place','what the mathematics supports','how strongly']);w.writerows(READINGS)
    coverage=[]
    for key,(ids,outcome,detail) in REQUIREMENTS.items():
        ids=ids.split()
        assert all(i in byid for i in ids),(key,ids)
        coverage.append(dict(task=key,statements=ids,outcome=outcome,missing=detail))
    (ROOT/'coverage.json').write_text(json.dumps(coverage,indent=2,ensure_ascii=False)+'\n')
    report=['| Required item | Statements | Outcome | Scope / remaining obligation |','|---|---|---|---|']
    for c in coverage:
        report.append('| '+c['task']+' | '+', '.join(c['statements'])+' | '+c['outcome']+' | '+c['missing']+' |')
    narrative=ROOT/'sections/report_narrative.md'
    if narrative.exists():report+=['',narrative.read_text()]
    (ROOT/'CYCLOTOMIC_KERNEL_report.md').write_text('\n'.join(report)+'\n')
    counts={x:sum(c['outcome']==x for c in coverage) for x in ('proved','refuted','partly settled','unfinished')}
    output=dict(numbered_statements=len(rows),required_items=len(coverage),outcomes=counts,
                editorial_readings=len(READINGS),identifier_coverage='passed',all_required_items_have_statements=True)
    (ROOT/'code/assemble_ledgers_output.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
