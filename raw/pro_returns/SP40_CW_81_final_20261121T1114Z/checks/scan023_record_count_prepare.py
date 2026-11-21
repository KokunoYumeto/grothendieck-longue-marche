"""Text-only proposed counts and qualifiers; root approval remains pending."""
from pathlib import Path
import hashlib,json,re
ROOT=Path('/workspace/scratch/94548b74fbe0')
OUT=ROOT/'out/checks'
u=json.loads((OUT/'scan023_source_union.json').read_text())
jp=OUT/'scan023_main_decisions.md'
jt=jp.read_text()
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
assert sha(jt)=='e47c66e9ceb1a9823bfa73ee6544e6068d84def3a91dee1547ab2e83ab4f07af'
# n, proposed C, proposed H, confidence, physical parent, local qualification.
raw=r'''
1|1|0|medium|1|Complete prouvons newly qualified; no invented alternative. Same H primary gives no H count.
2|1|1|medium|2|Primary a versus independent point-shaped mark; role, hand and origin open. H proposal concerns literal lozenge geometry.
3|0|0|high|3|Complete barred-V target unchanged.
4|0|1|high|4|Live ne precedes cancelled contient and raised rencontre. One whole correction/placement parent.
5|1|1|high|5|Detached triangular left trace; role, hand and origin undetermined.
6|1|1|low|6|Complete deleted-vee/live-cup versus retraced-cup states, with alpha-in-K limit. R14 retained; proposed C count is literal overlap geometry.
7|1|1|low|7|Full hatted deleted-I/Sigma, deleted-E/Sigma, and live-Sigma/retrace states, all plus/alpha. R01 retained; proposed C count is literal upright geometry.
8|0|1|medium|8|Cancelled whole donc si remains qualified; R02 retained. Extra H ill-word unsupported; marker only on that placeholder.
9|1|1|medium|9|Whole on a qualified; final a can be a point-shaped mark. Phrase and ochre scopes separate. H proposal concerns literal reduced-a geometry.
10|1|1|high|10|Separate ochre oblique; role, hand and origin undetermined.
11|1|1|high|11|Complete E_beta with lower closed loop/retrace; no predecessor or cancellation inferred.
12|0|0|high|12|S02 joined head/body, plus and alpha; full parenthetical unchanged.
13|0|1|high|13|Capital C in the full slanted note; this count concerns case only.
14|0|1|low|14|Cancelled illegible item retained as one whole unreadable word; R03 retained.
15|0|0|low|15|Complete parenthetical I/J; R04 retained. Same H primary I gives zero H count.
16|1|1|medium|16|Complete ce qui versus qui; crowded attachment unresolved. H qui remains an alternative.
17|0|1|medium|17|Complete prouvera versus prouve; R05 retained. H prouve remains an alternative.
18|1|1|high|18|Separate assertion point; role, hand and origin undetermined.
19|0|0|high|19|Complete upper inclusion with ordinary S03; source-only agreement.
20|0|1|high|20|Cela revient against H résulte.
21|0|1|medium|21|Au remains qualified; R06 retained; H reads du.
22|0|0|high|22|Whole lemma introduction; local component counts remain separate.
23|0|0|high|23|Whole tel que les remains cancelled in both witnesses.
24|0|1|high|24|Only et cancelled; des live. H has et live.
25|1|1|medium|25|Complete S04 plus/alpha with pale bridge versus separate upper run; first recurring role qualifier.
26|1|0|medium|26|Tels firm; actual R07 resolved. Root journal medium-high is the finer confidence.
27|1|1|high|27|Isolated lemma point; role, hand, attachment and origin undetermined.
28|1|1|low|28|Complete alpha-ne-beta-in-K versus alpha-deleted-ne/comma-beta-in-K. R15 retained; proposed C count is curved-hook geometry.
29|0|0|high|29|Repeated relation, implication and full endpoint retained; S05/S06 have their own parents.
30|1|1|medium|30|Complete S05 plus/alpha with detached return and shared alpha; local head/independent-run role remains open.
31|1|1|medium|31|Joined head/shared beta; complete Sigma_beta-plus versus Sigma_beta-top. No extra upper arm.
32|0|0|high|32|Complete lemma antecedent; S07 counted separately.
33|1|1|medium|33|Complete S07 plus/alpha with detached head and terminal point; point attachment, hand and origin separately open.
34|1|1|medium|34|Whole correction: four contenu/contenue and raised live/deleted-que states; R08 retained. One parent includes missing H dans un/comma and raised placement.
35|0|0|high|34|No separate dans un after cancelled clause; shared correction parent U34.
36|0|0|medium|34|Raised que primary live, deleted alternative; new C target qualifier counted once at U34.
37|0|0|high|34|Open gap after raised K, no comma; shared correction parent U34.
38|0|0|high|38|Complete live final inclusion and period; S08 counted separately.
39|1|1|medium|39|Complete S08 plus/continuous alpha with separate upper bar; local head role remains qualified.
40|0|0|high|40|Cela and cancelled signifie que retained; source-only unchanged wording.
41|1|1|low|41|Primary precise; alternatives précise, provient, precise le, précise le. R09 retains full compound scope; primary changed from C/H provient.
42|1|1|medium|42|Du firm; R10 resolved. H's separate last-word ill marker applies. Root journal medium-high is the finer confidence.
43|1|1|high|43|One two-point far-right group; roles, hand and origin undetermined; separate from H word placeholder.
44|1|1|high|44|Pale oblique left of Corollaire; role, hand, attachment and origin undetermined.
45|0|0|high|45|Complete heading and lead; no new full-heading image claim.
46|0|0|high|46|Written hyp. retained; probable expansion only in abbreviation list.
47|1|1|high|47|Written préc. firm; R11 resolved; H expands précédentes.
48|1|1|low|48|Whole family: four K/I and deleted-I-K/deleted-K-I states; i-hook/dot attachment versus foot-retrace/independent-point; shared parent.
49|0|0|low|48|R12 retained; all four complete external-index family states under U48.
50|0|0|high|48|Both parentheses, hook/dot, raised alpha, external-alpha junction, final cluster and comma owned once; no duplicate count.
51|1|1|medium|51|Complete Pi_K-circle versus Pi_K-zero, hooked K and ring entry. R13 retained; proposed C count is literal body geometry.
52|0|0|high|52|Full two-line corollary frame; all selected components once, each local count parent separate.
53|1|1|high|53|One interrupted rule, six runs and one bead; segmentation confidence medium; parent-unit declaration carries no metric claim.
54|1|1|low|54|Whole S10 plus/alpha versus deleted-i-then-alpha state; both points and short extra plus run retain independent role/hand scopes.
55|1|1|high|55|Shared full formée/cup, interrupted upper-left stalk, definite cross and full limit; includes R16 presence resolution once.
56|0|0|high|55|R16 resolved on cross presence; operation/attachment role remains qualified; no duplicate count.
57|1|1|medium|57|Complete final hatted Sigma plus/alpha with separate roof and detached short head; head role remains open.
58|1|0|medium|58|Whole Immédiat/Immèdiat/Immediat alternatives; accent direction/attachment low-confidence; same H primary.
59|1|0|medium|59|Whole récurrence/rècurrence/recurrence alternatives; same H primary.
60|1|1|high|60|Faint capital-side hook; role, hand and origin undetermined; separate physical target from word accent.
61|0|0|high|61|Root directed zero C/H counts: geqslant is selected source shape of same relation. Literal command and section31 evidence retained.
62|0|0|high|62|Archive comment22 source-only; all reader attributions undetermined; no new root image claim.
'''
rows=[]
for line in raw.strip().splitlines():
 n,c,h,confidence,parent,qual=line.split('|',5); n=int(n)
 locus=u['loci'][n-1]; assert locus['locus_id']==f'U023-{n:02d}'
 rows.append(dict(locus_id=locus['locus_id'],location=locus['location'],
  proposed_diff_C=bool(int(c)),proposed_diff_H=bool(int(h)),
  proposed_confidence=confidence,proposed_count_parent=f'U023-{int(parent):02d}',
  qualifier_and_count_basis=qual,count_approved=False,main_approved=False,
  reader_source_row_ids={r:[x['id'] for x in locus['readers'][r]['reported_difference_rows']] for r in 'ABC'}))
assert len(rows)==62
result=dict(scan=23,stage='proposal pending root count/confidence review',main_approved=False,
 root_journal=dict(path='out/checks/scan023_main_decisions.md',sha256=sha(jt)),
 root_plan=dict(path='out/checks/scan023_root_assembly_plan.md',sha256=sha((OUT/'scan023_root_assembly_plan.md').read_text())),
 source_union=dict(path='out/checks/scan023_source_union.json',sha256=sha((OUT/'scan023_source_union.json').read_text())),
 rows=rows,proposed_counts=dict(C=sum(x['proposed_diff_C'] for x in rows),H=sum(x['proposed_diff_H'] for x in rows)),
 C_outcomes={f'C023-R{i:02d}':('resolved' if i in (7,10,11,16) else 'retained') for i in range(1,17)},
 questions=['U06/U07/U28/U51 retain original C doubts while proposing counts for literal geometry; please decide expressly.',
 'U02/U09 proposed H counts concern reduced-a geometry; same-primary qualifier alone contributes zero.',
 'Whole correction U34 includes U35–37; whole family U48 includes U49–50; shared formée/cup U55 includes U56.',
 'U58 word accent and U60 detached hook are proposed as separate physical targets.',
 'Scalar confidence categories are proposed; the frozen journal retains the full geometry/identity/role confidence distinctions.'],
 S_scope='All seven supplied S rows: source-only scope; zero C/H counts; no local scan023 correction.',
 check_events=[])
(OUT/'scan023_record_count_proposal.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
md=['# Scan023 proposed physical counts and confidence','',
 'All values except the explicitly directed U023-61 zero counts remain proposals for root review. No approval is claimed.','',
 '| Locus | Scope | C | H | Parent | Confidence | Complete qualification / count basis |',
 '| --- | --- | --- | --- | --- | --- | --- |']
for x in rows:
 values=[x['locus_id'],x['location'],int(x['proposed_diff_C']),int(x['proposed_diff_H']),x['proposed_count_parent'],x['proposed_confidence'],x['qualifier_and_count_basis']]
 md.append('| '+' | '.join(str(v).replace('|','\\|') for v in values)+' |')
md.extend(['','## Explicit review points',''])
md.extend('- '+q for q in result['questions'])
md.extend(['',f"Proposed totals: C {result['proposed_counts']['C']}; H {result['proposed_counts']['H']}. Actual C outcomes: R07/R10/R11/R16 resolved; the other twelve retained. All seven S rows are source-only, with zero counts. No mathematical check event."])
(OUT/'scan023_record_count_proposal.md').write_text('\n'.join(md)+'\n')
print(json.dumps(dict(path='out/checks/scan023_record_count_proposal.md',sha256=sha((OUT/'scan023_record_count_proposal.md').read_text()),proposed_counts=result['proposed_counts'],root_approved=False)))
