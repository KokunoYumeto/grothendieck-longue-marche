from pathlib import Path
import csv,json,datetime
r=Path(__file__).resolve().parents[1]; rec=r/'records'
fields=['statement_id','date','who','type','outcome']
rows=[]
date='2026-11-17'
rootwho='GPT-6 Astra Pro; effort not exposed; /root; run MPL_64_002-039'
groupwho='GPT-6 Astra Pro; effort inherited/not separately exposed; /root/delivery_tooling; run MPL_64_002-039'
congwho='GPT-6 Astra Pro; effort inherited/not separately exposed; /root/congruence_context; run MPL_64_002-039'
connectionswho='GPT-6 Astra Pro; effort inherited/not separately exposed; /root/connections_context; run MPL_64_002-039'
def event(id,type,outcome,who=rootwho,day=date):
 rows.append(dict(statement_id=id,date=day,who=who,type=type,outcome=outcome))
mapid={'C64.CX01':'C64-Q01','C64.CX02':'C64-Q02','C64.CX03':'C64-N30','C64.CX04':'C64-N34','C64.CX05':'C64-Q03','C64.CX06':'C64-Q04','C64.CX07':'C64-N32','C64.CX08':'C64-Q04','MPL64-G01':'C64-N23','MPL64-G02':'C64-N25','MPL64-G03':'C64-N27','MPL64-G04':'C64-N30','MPL64-G05':'C64-N35','MPL64-G06':'C64-Q03','LM_P057 R17':'LM140-2 LM_P057api R17','LM_P057api R17':'LM140-2 LM_P057api R17','LM_P057 R18 group-isomorphism component':'LM140-2 LM_P057api R18: finite-group component'}
for fn in ['congruence_context_events.tsv','group_checks_events.tsv']:
 with (rec/fn).open() as f:
  for row in csv.DictReader(f,delimiter='\t'):
   original=row['statement_id']; id=mapid.get(original,original)
   if original=='LM4_SUCCESSOR B.38/E.10':
    for single in ['LM4_SUCCESSOR B.38','LM4_SUCCESSOR E.10']:
     event(single,row['type'],row['outcome']+' [Source event fragment: '+fn+']',row['who'],row['date'])
   else:
    event(id,row['type'],row['outcome']+' [Original event '+original+'; fragment '+fn+']',row['who'],row['date'])
cm={'CC01':'C64-Q05','CC02':'C64-Q06','CC03':'C64-Q07','CC04':'C64-Q08','CC05':'C64-Q09','CC06':'C64-Q10','HQ01':'C64-N14','HQ02':'C64-N28'}
for line in (rec/'connections_check_events.jsonl').read_text().splitlines():
 e=json.loads(line)
 event(cm[e['statement_id']],e['type'],e['claim']+': '+e['actual_check']+' Limit: '+e['limits']+' [Original '+e['statement_id']+'; connections_check_events.jsonl]',e['who'],e['time_utc'])

notes=[x for fn in ['root_note_items.json','question_note_items.json','apparatus_note_items.json'] for x in json.loads((rec/fn).read_text())]
for n in notes:
 event(n['id'],'used and rechecked in this run','Documentary source/wording/scope check for this note, against frozen cote64 scan(s) '+n['scans']+' and '+n['context']+'. Actual targeted search logged under this ID in root_context_searches.json. This row is not a proof check of every mathematical claim in the cited context; substantive finite checks are recorded separately.')

basic={
1:'Verified the regular Klein subgroup and the four-set affine model; choosing an origin gives a vector identification, with no preferred origin.',
2:'Enumerated normalizer(V)=S4 of order24 and centralizer(V)=V of order4; conjugation is faithful on S4/V, not on S4.',
3:'Enumerated all Coxeter-generator images satisfying the S4 presentation and generating S4:24 automorphisms; center trivial, so all are inner; four Sylow3 subgroups.',
4:'Enumerated exactly four Sylow3 subgroups. This does not adjudicate the doubtful word trois on006.',
6:'Computed the three nonidentity V-element centralizers, each D8 of order8, and the three cyclic order4 subgroups. Full centralizer is not the rotation subgroup.',
10:'Using ordinary functional composition with r=(1234),c=(12)(34),d=(24), obtained rcd=(13)(24) and dcr=1; action convention matters.',
11:'Enumerated eight automorphisms of D8, a faithful eight-element action on its noncentral involutions, and a two-element kernel for the inner automorphism map.',
14:'Enumerated all30 S4 subgroups,11 conjugacy classes,three nonnormal V4 subgroups,four Sylow3 groups and19 nonidentity2-subgroups. Numerical correctness does not decide the disputed ink19/17.',
15:'Computed all30 actual subgroups and66 cover inclusions, with exact indices; CSV data is not merely conjugacy-class data.',
16:'Checked all24 permutations on both six-point covers; circular cover gives trivial spatial-orientation character, two-subset cover gives sign on I. This is an equivariant orientation distinction.',
17:'Checked the four-set image in the eight-element product of pair-partition blocks:one parity fibre; contracted quotient has two elements.',
18:'The same exact torsor sizes show product8 versus contracted product2; the wedge caption cannot have the product structure group as a torsor.',
19:'Checked all10 transitive cube-object actions and their stabilizers, using24 signed-coordinate rotations; the full cube group has48 elements.',
20:'Checked that the face-diagonal stabilizer is a double transposition inside V; edge stabilizer is a transposition outside V, and full versus oriented automorphism orders are48 versus24.'}
for n,out in basic.items(): event(f'C64-N{n:02d}','computation or formal certificate',out+' Evidence: records/basic_permutation_checks.py and basic_permutation_results.json.')

proofs={
3:'For connected groupoids, the isomorphism on automorphism groups given by the checked inner-automorphism action implies full faithfulness; every S4-type group is represented. This does not apply to arbitrary group homomorphisms.',
5:'Two C2-torsors with the same character have two equivariant bijections; equality of characters alone picks neither. The manuscript explicitly specifies a first/last convention.',
7:'From an antipodal four-set, the non-diagonal2-subsets give four edges and incidence; cyclic order4 torsor descriptions retain the orientation doublet rather than a chosen global generator. Automorphisms are preserved.',
8:'For D8=<r,s|r^4=s^2=1,srs=r^-1>, the derived subgroup is<r^2>, so D8_ab=C2^2 while the rotation subgroup C4 is already abelian; the superscript-plus ambiguity is consequential.',
11:'The faithful full eight-element automorphism action on the reflection square, and connectedness of both groupoids, prove the abstract-group-to-square equivalence; Q->Aut(Q) has its central two-element kernel instead.',
12:'Symbolic countermodel, not a formal-computer proof: send each displayed generator x to1 in additive Z and a to0. All displayed commutator relations hold with infinite cyclic image; involution conditions from prose are excluded from this literal-presentation test.',
13:'A section of the two opposite-edge fibres selects adjacent edges and their unique vertex; simultaneous reversal is antipodism. Quotienting by it gives the two diagonals, with the stated contracted torsor structure.',
17:'The coordinate parity calculation is independent of temporary labels because relabelling translates the parity quotient; the four-set image intrinsically selects one quotient point.',
22:'P_M is a V_J(M0)-torsor; extension of structure group must use pr_i restricted to that group. Each restriction is surjective. The printed M0^J subscript is retained as a reading/type question.',
24:'I+2 times a lift of u is independent of lift modulo4; reduction is I, and multiplication is addition in End(M0). This repairs the source/target interpretation in prose, not the frozen text.',
25:'Reviewed the natural-construction proof and actual quotient-action certificate:full faithful standard-object map and connected finite groupoids imply equivalence over sets; descent is needed for locally constant families.',
33:'The antipodism reverses spatial orientation. Twisting by Or(Delta) multiplies the orientation character by itself, giving the new object trivial orientation; it does not choose an orientation of the original object.',
35:'Reviewed explicit central section equation and pullback of its factor set. For a specified topos, constant finite central extension and fixed quotient torsor identification, obstruction is c cup d; vanishing gives an H1(C2)-torsor of lifts and H0(C2) automorphisms over that identification.',
38:'The central matrix minus I is invisible on the six projective vertices but remains the antipodism on the four square vertices; hence the complete square functor cannot descend unchanged through the central projective quotient.'}
for n,out in proofs.items():
 typ='independent re-proof' if n==12 else 'targeted proof check'
 event(f'C64-N{n:02d}',typ,out)

gchecks={
21:'Built16 sum-zero triples, their End(M0) regular action, and the evaluation isomorphism.',
23:'Checked all16 endomorphisms,6 conjugators,orthogonal canonical summands,trace-zero decomposition and the earlier R17 formula.',
24:'Checked the16-element mod2 reduction kernel I+2End(M0).',
25:'Constructed actual I=P/W and square S=P/A; joint natural action is faithful with96 images, exactly the fibre product.',
26:'Checked image in S4×D8 has the codiagonal/sign matching condition, order96, and both stated kernels.',
27:'Generated all commutators; [SL,SL]=A4(order12),[GL,GL]=A4×Z(order24), abelianizationsC4/C2², centersZ and determinant action on SL_ab.',
28:'Checked all five actual subgroup intersections and displayed indices, and the chosen-point GL semidirect decompositions.',
29:'All eight SL elements with square one lie in the mod2 kernel, preventing an S3 section; GL has an explicit six-element complement after choosing a torsor point.',
30:'Enumerated12 primitive vectors,6 sign classes,12 edges,8 faces; GL image48 with kernel±I, SL image24=S4 on bifaces.',
31:'Verified every face fibre in P has exactly two points, differing by simultaneous negation; induced quotient has8 points.',
32:'Verified reduction-sign,codiagonal,diagonal/face-color and spatial-orientation characters for all96 matrices.',
33:'Verified orientation twist has rotational image and the stated kernel.',
35:'Verified all16 D8 quotient products and all2304 projective quotient pairs with factor set chi_c(g)chi_d(h).',
37:'Verified central quotient has order48; a further quotient of full octahedral group by its center would have order24. This does not decide whether the frozen mark is a prime.',
38:'Verified minus I acts trivially on Delta and as nontrivial square antipodism.'}
for n,out in gchecks.items(): event(f'C64-N{n:02d}','computation or formal certificate',out+' Evidence: records/group_checks.py and group_checks_results.json; natural constructions, no group database.',groupwho)
event('C64-N36','targeted proof check','Direct check in targeted review: T=[[0,3],[1,0]] has T²=(-T)²=-I,detT=1,and mod2 direction sign-1; its projective class has order2 and both lifts order4. The certificate JSON stores a different valid witness, not this exact T.',groupwho)
event('C64-N15','computation or formal certificate','Generated30-node,66-edge actual-subgroup SVG from the checked CSV; every listed generator set regenerates its subgroup, all cover edges and indices match, and all SVG edges point upward. Evidence:s4_subgroup_inclusions_check.json and generator-key/render scripts.',congwho)

for id,n,out in [
('64 scan003: deleted normalizer assertion',2,'The normalizer of the normal Klein subgroup has24 elements,not4; the manuscript itself replaces the word by centralizer.'),
('64 scan007: cyclic-target centralizer arrow; scan020: D-plus full-centralizer clause',6,'Full centralizers of nonidentity elements of V have order8,not4; corrected target is the Sylow2 group,with C4 its rotation subgroup.'),
('64 scan017: displayed relations alone',12,'The literal displayed presentation has an infinite cyclic quotient; full involution/antipodal relations are needed. This does not refute the prose-qualified groupoid equivalence.'),
('64 scan025: face-diagonal stabilizer outside V',20,'In the stated rotation S4 model,the stabilizer lies inside V. Refined orbit/stabilizer table is C64-N19.'),
('Hua section4: second cover does not define a cube without orientation qualification',16,'Both covers define abstract cubes;only the circular cover has orientation-preserving S4 action. The unqualified assertion is too strong.')]:
 refine='C64-N19' if n==20 else f'C64-N{n:02d}'
 event(id,'refuted, refined statement '+refine,out)

# Source-place pointers record the scope of actual checks, not additional independent runs.
source_checks=[
('64 scan003: affine and centralizer assertions','C64-N01,C64-N02','computation or formal certificate'),
('64 scans004-006: fully faithful groupoid and Sylow reconstruction','C64-N03','targeted proof check'),
('64 scans008-010: five square descriptions','C64-N07','targeted proof check'),
('64 scans012-014: orientation product under specified convention','C64-N10','computation or formal certificate'),
('64 scans015-017: reflection-square equivalence','C64-N11','targeted proof check'),
('64 scans018-020: fibre products and contracted quotients','C64-N13','targeted proof check'),
('64 scans021-022: subgroup enumeration','C64-N14','computation or formal certificate'),
('64 scans023-025: cube actions and parity torsor','C64-N16,C64-N17,C64-N19','computation or formal certificate'),
('64 scans026-027: zero-sum lift torsor','C64-N21','computation or formal certificate'),
('64 scans027-028 (10)-(17): canonical End decomposition','C64-N23','computation or formal certificate'),
('64 scans028-029 (18)-(22): canonical equivalence and fibre product','C64-N25,C64-N26','targeted proof check'),
('64 scans030-032: derived groups and five subgroup squares','C64-N27,C64-N28','computation or formal certificate'),
('64 scans033-035: projective octahedron and face torsor','C64-N30,C64-N31','computation or formal certificate'),
('64 scans035-037: characters and orientation twist','C64-N32,C64-N33','computation or formal certificate'),
('64 scans037-038: posed lifting problem','C64-N34','used and rechecked in this run'),
('64 scan039: projectivization forgets square datum','C64-N38','targeted proof check')]
for id,notes_id,typ in source_checks:
 event(id,typ,'Source-place pointer to actual check(s) recorded under '+notes_id+'; see those rows for method, checker, evidence and restrictions. This is the same check indexed by primary-text place, not another independent run.', groupwho if notes_id.startswith(('C64-N21','C64-N23','C64-N25','C64-N27','C64-N30','C64-N32')) else rootwho)

background={
'LM2 C.d5':'Supplied return marks simultaneous realization/image problem Open; no solution claimed.',
'LM4_SUCCESSOR B.38':'Supplied register marks higher congruence kernels Open; finite levels2/4 do not decide them.',
'LM4_SUCCESSOR E.10':'Supplied register marks six fixed-subgroup and H1(C2,K_c) computations Open; none completed here.',
'EXIT_TOWER E.24':'Supplied register marks arithmetic image problem Open; no arithmetic realization checked.',
'LM7_PUSH E.3':'Supplied register marks full-GT extra-coset question Open; no resolution adopted.',
'EXIT_TOWER E.49':'Explicitly unrefereed/under check in supplied register; not treated as settling E.3.',
'LM6 F.43':'Prior-return Proved claim about boundary/normal-line data,not independently reviewed here; only a scope comparison.',
'LM7 D.45':'Prior-return Proved claim involving order24 marked bases and relative pro2 completions; finite cube homogeneous spaces do not verify its marked completion assertions.',
'MPL_93_002-046 E14':'Only title and conjecture status supplied; actual deformation/coarse-invariant statement unavailable.',
'MPL_93_002-046 E16':'Only title and earlier own-idea high-confidence label supplied; no orders or families reconstructed.',
'MPL_93_002-046 C29':'Only title and earlier own-idea status supplied; unseen first-order map not verified.',
'MPL_93_002-046 P09':'Only future-comparison title supplied; Q09 is this run’s necessary-test proposal,not recovery of unseen content.',
'MPL_93_002-046 C35':'Register says withdrawn in same text; retained as withdrawn without reconstructing the missing explanation.',
'Planning S20':'A planning guess in README,not attributed to Grothendieck as a stated conjecture; not established by this packet.',
'MPL_149_091-136 RN099-03':'Supplied prior notes report a modular cusp/Tate calculation proposal; no original149 scans or proof checked here.',
'MPL_149_091-136 RN101-04':'Supplied prior notes report structure at infinity; documentary lead only.',
'LM140-3 scan019 R30; scan050 R26-R28':'Prior notes used as navigation to the inspected lattice/analytic modular passages; no independent uniformization proof.',
'LM140-2 LM_P057api R19':'Modular/Fermat-conic geometric assertion left unverified here; finite group model does not prove it.',
'LM140-2 LM_P057api S6: geometric correspondence':'Finite complement count checked separately; proposed relation to geometric lifts not proved.',
'Hua modernised reading cote64 sections1-6':'Modern interpretation used with specific corrections and attribution; not treated as a diplomatic source or a globally verified result.'}
for id,out in background.items(): event(id,'used and rechecked in this run' if id.startswith('Hua modernised') else 'carried as background without fault found',out)
event('LM140-2 LM_P057api R14','computation or formal certificate','Kernel identity det(I+2A)=1+2tr(A) and16-element GL/8-element SL reduction kernels independently checked within the finite matrix certificate.',groupwho)
event('LM140-2 LM_P057api R17','independent re-proof','The basis-free alternating-form proof and exhaustive48 equivariance/64 additivity checks verify the already recorded quotient identification; eight formula comparisons agree with phi_A(v)=det(v,Av). No geometric0,1,infinity labelling fixed.',congwho)
event('LM140-2 LM_P057api S6: finite complement count','computation or formal certificate','Four complements to the scalar line in sl2(F2),with conjugation orbits1+3; unique invariant complement is the manuscript’s reflection summand. No claimed correspondence with geometric lifts.',groupwho)
for id,out in [
('Katz1970 introduction; Theorem7.4,Corollary7.5,Theorem10.0','Inspected primary text and relevant hypotheses; Gauss-Manin/Picard-Fuchs and Cartier/conjugate nilpotence results used as published background,not independently reproved.'),
('Ogus-Vologodsky2007 Remark2.2','Inspected primary statement of Cartier descent for zero p-curvature; no claim that nilpotent implies zero.'),
('Bouw-Wewers2006 Definition2.1; sections3.1,5','Inspected author preprint and publisher metadata; marked-curve filtration/monodromy hypotheses and p-curvature definition used as background.'),
('Hoshi2015 introduction and section5','Inspected author preprint and publisher metadata; indigenous-bundle definition and Cartier comparison kept at stated odd-characteristic/characteristic-three scope.'),
('Ledet2001 section0.4','Inspected publisher PDF,pp283-284; compared classical dihedral obstruction after coordinate change; field interpretation requires characteristic different from2,while finite cocycle proof is independent.')]:
 event(id,'carried as background without fault found',out)

# Review events are targeted claim/scope reviews, not new scan readings.
event('C64-N01-C64-N20: research review','targeted proof check','Independent review of text/code/results supported groupoid,cover-orientation,subgroup and cube claims; corrected N02 faithful quotient wording,N10 verbal quote,N14 synthesized quote,N15 transporter distinction,N17 label dependence. Presentation countermodel classified as symbolic proof,not a formal execution.',congwho)
event('C64-N21-C64-N38: research review','targeted proof check','Independent review confirmed finite counts and lifting logic; corrected N22 attribution,N27 derived-group notation,N28 splitting wording,N31 quote,N32 locator and N35 prescribed-data/section conventions; direct T-witness check recorded separately.',groupwho)
event('C64-Q05-C64-Q10: research review','used and rechecked in this run','Reviewed source scope and hypotheses; corrected catalogue locator,Katz base and E_r>=2 qualifications,Hua attribution and projective-connection settings. No differential theorem independently reproved.',connectionswho)

event('C64-U01-C64-U12; C64-T01-C64-T03: apparatus review','used and rechecked in this run','Compared all authorial flags and pagination/headings with frozen text; added explicit012 warning,007 forward reference,009 conversion programme and020 enumeration announcement; clarified closure of023 face correspondence and avoided assigning authorship to pencil40. All18 body-page number marks match; no19 supplied.',congwho)

with (r/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
(rec/'event_id_map.json').write_text(json.dumps({'research_report_to_final_note':mapid,'connections_report_to_final_note':cm,'notice':'Source-place pointer rows index the same actual checks by primary location; row count is not independent-check count.'},indent=2)+'\n')
print(json.dumps({'events':len(rows),'unique_statement_ids':len({x['statement_id'] for x in rows}),'note_ids_covered':len({x['statement_id'] for x in rows}&{x['id'] for x in notes})}))
