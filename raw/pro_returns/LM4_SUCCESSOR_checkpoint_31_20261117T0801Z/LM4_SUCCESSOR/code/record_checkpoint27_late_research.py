"""Bind fully reviewed late mathematical notes without changing formal counts."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,shutil

root=Path(__file__).resolve().parents[1]
sha=lambda rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()
sources={
 'work_A/actual_GT0_V4_Fox_defect27.md':'99a0b83621cb24d8fe2f2386cf330244e87ff47906b63d9400f79d02bc05cda9',
 'work_A/actual_GT0_third_cusp_half_rotation27.md':'85782cde831119925111cc589aace37c7126af79e41bc3992f64266c79c09d16',
 'work_A/actual_GT0_canonical_cusp_frame27.md':'4b415cab71ac49b4de0af2de00512c3b94a6360f4b0e01195fc4a6e6dee8b794',
 'work_A/actual_GT0_cusp_coefficient_comparison27.md':'44f002a17ec1e54d199d7921005332327b6dbd1e6e59ec16a58617b5832b4794',
 'work_A/chi_sum_core_deletion_barrier27.md':'2e6722d30e3faf71639da6c0170be5b44ec09b14a039b36b4769f98a6f0a5a05',
 'work_CE/whole_node_m_star_presentation27.txt':'5da0fb85d70d77e59c30f8b2e51363389ebc7588aebcc1b167c84e5676a0e95d',
 'work_CE/inner_star_actual_kernel27.txt':'f812a80ffa29cb5b7844310bae8165e005eabe4e43363755b3c79a5fb9d059f8',
 'work_CE/inner_star_face_exact_kernel27.txt':'c45469f6c108ed88abb1d3e51cd8822b122f5c0433d009fd9ca277677d3ee0ac',
 'work_DE/next_marginal_source/unfilled_edge_map_structure27.md':'44ab5dfe0a76ff981c20a787bfe6010c5314e959bc7b86eb6f46f2c398ce8f28',
}
reviews=[
 'work_CE/review_actual_GT0_V4_Fox_defect27.txt','work_CE/review_actual_GT0_V4_Fox_defect27.json',
 'work_CE/review_GT0_third_cusp_half_rotation27.txt','work_CE/review_GT0_third_cusp_half_rotation27.json',
 'work_CE/review_GT0_canonical_cusp_frame27.txt','work_CE/review_GT0_canonical_cusp_frame27.json',
 'work_CE/review_GT0_cusp_coefficient_comparison27.txt','work_CE/review_GT0_cusp_coefficient_comparison27.json',
 'work_CE/review_core_deletion_barrier27.txt','work_CE/review_core_deletion_barrier27.json',
 'work_A/review_whole_node_m_star27.md','work_A/review_whole_node_m_star27.json',
 'work_DE/next_marginal_source/review_m_star_and_actual_face27.md','work_DE/next_marginal_source/review_m_star_and_actual_face27.json',
 'work_DE/next_marginal_source/review_inner_star_actual_kernel27.md','work_DE/next_marginal_source/review_inner_star_actual_kernel27.json',
 'work_DE/next_marginal_source/review_inner_star_face_exact_kernel27.md','work_DE/next_marginal_source/review_inner_star_face_exact_kernel27.json',
 'work_CE/review_unfilled_edge_map_structure27.txt','work_CE/review_unfilled_edge_map_structure27.json',
]
review_text='\n'.join((root/p).read_text() for p in reviews)
for p,h in sources.items():
    assert sha(p)==h,p
    assert h in review_text,p
programs=[
 'work_CE/code/compile_m_star_relative_presentation27.py',
 'work_CE/code/check_m_star_relative_face27.py',
 'work_CE/code/check_inner_star_kernel27.py',
 'work_DE/next_marginal_source/check_unfilled_edge_maps27.py',
 'work_A/code/check_core_deletion_A_marking27.py',
]
record={
 'recorded_at':datetime.now(timezone.utc).isoformat(),
 'status':'PASS_COMPLETE_LATE_PROOF_REVIEW_WITH_EXPLICIT_REMAINING_GATES',
 'proof_sources':sources,'independent_reviews':{p:sha(p) for p in reviews},
 'root_complete_producer_and_genuine_stdout_reads':{
     p:{'producer_sha256':sha(p),'stdout_sha256':sha(str(Path(p).with_suffix('.out')))} for p in programs},
 'root_scope':'All nine complete proofs read, including final local-symmetry Section5 and the canonical-frame/Alexander coefficient notes. The corrected A_s marking is supported by the complete literal checker and final scoped text. No new producer execution by root is claimed. Complete formal A45 and C44 proofs were reread at this use; the entire containing A file is not represented as newly reread.',
 'at_use_formal_dependencies':{
     'A45':{'source':'work_A/A_involutions.tex','scope':'Complete statement A.45 and proof, equations A.45.1--3, including the unchanged odd-prime limitation.'},
     'C44':{'source':'work_CE/C44_regular_Alexander.tex','sha256':sha('work_CE/C44_regular_Alexander.tex'),'scope':'Entire formal statement and proof, with full head retained and original-marking limitation.'}},
 'formal_promotion':False,'formal_statement_count':303,'main_A':'Open','main_B':'Open',
 'remaining_gates':[
     'Actual full-word Omega_alpha=1; its first coefficient compares a_reg with d_alpha, two proved actual full units whose equality remains unproved.',
     'Kappa-invariance of the actual local amalgam map kernel and the full ordinary/compact matching comparison.',
     'Whole fixed-source equality and global transfer. The exact one-commutator kernel and fixed-source creation are proved only on the specified actual retracted block.'
 ]
}
dest=root/'records/checkpoint27_root_late_reviews.json';assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n')

backup=root/'records/checkpoint27_before_late_status'
backup.mkdir(exist_ok=False)
for rel in ['task_coverage.csv','LM4_SUCCESSOR_report.md','records/twenty_seventh_hour_research_report.md']:
    out=backup/rel;out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/rel,out)

late='''
## Later actual comparisons retained at checkpoint27

For Main A, the actual regular cusp reflection now has a unique
zero-abelianization frame h0 and a unique conjugator q, with q_ab=(t,-t).
The full third-cusp condition is exactly the single literal word equality
Omega_alpha=(x^d v)(q^-1 (xu)v q)^(-d)=1. The known actual dihedral unit
d=d_alpha has dyadic residue1 modulo4, which removes the other normalized
branch by the actual mod-two semidirect homology quotient. A literal
solution of the existing C44 equation identifies a second actual full
unit a_reg=1-4t. The first abelian coefficient of Omega is
((d-a_reg)/2,-(d-a_reg)/2). Equality of these two units and full nonlinear
vanishing remain unproved. This is a comparison of actual canonical data,
not a generic ring example, an all-P claim or a finite conjugacy census.

For Main B, the actual unfilled edge groups are now identified: one is
E1*Z by an all-exponent ordinary branch normal form; the target free-six
part has full induced profinite topology by actual zero edge intersections.
The complete target group is the mirror of the first. Their two local
fillings give a proper known amalgam Dloc of two B117 groups, with an
explicit involution kappa. Writing a_loc for its actual map into V_*, the
other map is theta a_loc kappa. Thus initial ordinary kernel matching is
exactly kappa-invariance of ker(a_loc); matching finite normal subgroups
admit cofinal theta-stable refinements with the corresponding explicit
preimage-invariance condition. Neither ambient survival nor that kernel
invariance is asserted.

The complete actual m-star presentation retains all seven v equations,
all twenty orbifold node words and every signed translate. Its pre-outer
selected centralizer is explicit, but the final map definitely kills the
nontrivial word [a,tau a tau]. A single specified S3 homomorphism checks
every inner defining relation and detects that word, proving nontriviality
also in the full inner completion. This is a fixed exact witness, not a
finite-target search.

More strongly, the entire actual retracted block
(Z(a)*C2(tau)) x Z(m) maps onto the actual retracted image
(Z2(a,tau a tau) semidirect C2(tau)) x Z(m). Its exact internal kernel is
the normal closure of that one commutator, and its completed kernel is
the corresponding closed normal closure, justified by the two actual
retractions and the quotient-completion universal property. Its ordinary
fixed subgroup grows from <m> to the known source <A_s,m>, in both
categories. This explains one exact source-direction creation mechanism;
it supplies no fixed element outside the source and determines no full
ambient filling kernel.

All these late notes have complete root and independent reviews bound to
their exact source bytes. They remain research notes in this checkpoint,
without extra formal IDs or an altered 303-statement count. Both main
decisions, the entire fixed-source equality and global transfer remain Open.
'''
p=root/'records/twenty_seventh_hour_research_report.md';p.write_text(p.read_text()+late)
p=root/'task_coverage.csv'
with p.open(newline='') as f:
    rd=csv.DictReader(f);fields=rd.fieldnames;rows=list(rd)
assert len(rows)==49
for row in rows:
    if row['task']=='A.8':
        assert row['outcome']=='Open'
        row['state']+=' Checkpoint27 actual negative-GT0 research proves the full V4 induced-defect description and reduces the third cusp to a single uniquely framed full-word obstruction Omega. Its first coefficient is the difference of two proved actual full units, a_reg and d_alpha; their equality and Omega vanishing remain Open. No all-P extension is asserted.'
        row['approaches']+=' Complete coupled full-ring Jacobians; actual three-involution coset comparison; closed pointed transversal; uniquely normalized regular cusp reflection and full primitive-cusp centralizer; explicit C44 solution and actual two-unit comparison.'
        row['obstruction']+=' Constant Z_p[V4] induction gives no Lambda_F splitting. The actual Alexander unit and dihedral unit are not identified, and coefficient agreement would still not prove the nonlinear word.'
        row['next_step']='Compare the actual canonical units a_reg and d_alpha and then the full word Omega_alpha, retaining the entire profinite group and original peripheral marking. The full P and GT descent obligations remain.'
    if row['task'] in {'B.4','B.4.a','B.4.b','B.4.c','B.4.h'}:
        assert row['outcome']=='Open'
        row['state']+=' Late checkpoint27 research identifies the embedded unfilled edge groups and proper symmetric local amalgam; the initial compatibility gate is kappa-invariance of its actual map kernel. An exact actual inner-star retracted block has one-commutator discrete and compact kernels and creates precisely the known source fixed direction.'
        row['approaches']+=' Actual cyclic branch all-exponent normal form and compact zero-edge intersections; symmetric local amalgam; complete relative inner-star presentation; exact equivariant retractions before and after filling.'
        row['obstruction']+=' Properness of the local amalgam does not prove its survival in V_*. The entire inner-star map is explicitly noninjective, so its former centralizer formula cannot transfer automatically.'
        row['next_step']='Resolve kappa-invariance of the actual local map kernel and the full matching/source intersection; compare all fixed elements with the actual source. Retain all signed v/m relations, other necks, global transfer and the final joint-source condition.'
with p.open('w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=fields);wr.writeheader();wr.writerows(rows)
p=root/'LM4_SUCCESSOR_report.md';s=p.read_text();lines=s.splitlines(True)
start=next(i for i,x in enumerate(lines) if x.startswith('| Task or lead |'));end=start
while end<len(lines) and lines[end].startswith('|'):end+=1
cell=lambda s:s.replace('|','\\|').replace('\n',' ')
lines[start:end]=['| Task or lead | Statements | Outcome and exact state |\n','|---|---|---|\n']+[
 '| '+cell(r['task'])+' | '+cell(r['statement_ids'])+' | **'+cell(r['outcome'])+'** — '+cell(r['state'])+' |\n' for r in rows]
p.write_text(''.join(lines)+late)
print('PASS nine complete late proofs bound;49 task rows synchronized;303 formal statements unchanged;both main decisions Open.')
