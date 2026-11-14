#!/usr/bin/env python3
"""Record the exact frozen GPD proof's claim-wrapper and tag transport."""
from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[2]
def binding(p):
    b=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
source=ROOT/'work/part_c/general_pointed_descent_comparison.tex'
assert binding(source)['sha256']=='71d95a8bcb21e20e7118f8a0f07ba9caadbefbb5d89796d6475aab0e63b8a620'
text=source.read_text()
prefix='% Unnumbered continuation note. This file does not modify C.91 or its scope.\n\\paragraph{Arbitrary actual pointed descents and their exact lift topology.}\n'
assert text.startswith(prefix)
text=text[len(prefix):]
intro,body=text.split('\\emph{Literal descent and the original orbit labels.}',1)
body='\\emph{Literal descent and the original orbit labels.}'+body
metric_anchor='Use the original radial disk coordinate\n'
metric_assignment=('In this example $\\overline D$ is the closed unit disk with its\n'
                   'Euclidean metric $d$. Use the original radial disk coordinate\n')
assert body.count(metric_anchor)==1
numbered_body=body.replace(metric_anchor,metric_assignment)
tag_map={f'GPD.{i}':f'C.92.{i}' for i in range(1,22)}
def transport(s):
    return re.sub(r'GPD\.([0-9]+)',lambda m:tag_map[m.group(0)],s)
statement_addition=r'''
More precisely, let $\lambda(b)$ be the unique lift of $b\pi$
fixing $x$ for $b\in\mathscr I_p$. The image of $D$ is exactly
the subgroup $\mathscr B_p$ defined by
$\delta_b(\pi z)=d_Q(\lambda(b)z,z)\in C_0(N)$.
Descent and extension of this lift are inverse group maps and
are isometric for the original sum metric and the lifted sum
metric in (C.92.15). On a compact parameter space their exact
continuity criterion is the uniform tail (C.92.17).
The explicit noncompact example (C.92.18)--(C.92.21) gives a
sequence in this exact image converging in the quotient
compact-open topology whose pointed lifts stay more than
$2/5$ from the identity in the original metric.
'''
claim_header=r'\begin{claim}{C.92}{Proved}{Arbitrary pointed descents and the exact original lift topology}'+'\n'
numbered=claim_header+transport(intro)+statement_addition+'\n\\end{claim}\n\n\\begin{proof}\n'+transport(numbered_body)+'\n\\end{proof}\n'
target=ROOT/'work/part_c/c92.tex';target.write_text(numbered)
# Inverting exactly the tag map on the proof body recovers every source byte.
proof_body=numbered.split('\\begin{proof}\n',1)[1].rsplit('\n\\end{proof}\n',1)[0]
inverse=re.sub(r'C\.92\.([0-9]+)',lambda m:'GPD.'+m.group(1),proof_body)
assert inverse.count(metric_assignment)==1
inverse=inverse.replace(metric_assignment,metric_anchor)
assert inverse==body
assert len(re.findall(r'\\tag\{C\.92\.[0-9]+\}',numbered))==21
assert numbered.count('\\[')==numbered.count('\\]')
row={
 'id':'C.92','status':'Proved',
 'statement':'Under all actual C81 hypotheses, with arbitrary compact or noncompact quotient N=O/Q, every element of the entire original point stabilizer descends into the pointed compact-open identity path component. Descent and the unique x-fixed lift identify the stabilizer exactly with the subgroup whose actual lift displacement belongs to C0(N), isometrically for the original metric and the displayed lifted map-and-inverse metric. A compact family has precisely the uniform C0 tail criterion. An explicit original radial-disk example has quotient compact-open convergence to identity while each unique pointed lift stays more than 2/5 from identity.',
 'where_proved':'Part C, statement C.92; work/part_c/c92.tex',
 'depends_on':'C81 actual original-disk group, invariant metric and quotient; C82 locally finite quotient triangulation; C88 exact C0 boundary-extension and compact-family criterion; Epstein1966 Theorem6.4(b), Lemma6.5, actual homeomorphism constructions in5.1-5.2 and6.4, and AppendixA4.',
 'manuscript_passages':'Section 23, folios 140-141, scans 279-281; Part C(b), exact original-boundary pointed descent, lift topology and the remaining noncompact level-zero kernel.',
 'depends_on_doubtful_reading':'None. All actual C81 hypotheses, original operators, quotient, original circle and map-and-inverse topology are retained.',
 'notes':'The explicit locally finite based homotopy meets the exact Epstein6.4(b) hypotheses; local-homology isomorphisms check every exceptional orientation qualification. The source isotopies are verified to have homeomorphism levels and jointly continuous inverses. The radial path formula gives the unique pointed lift continuously in the quotient compact-open topology. The exact lifted topology and escaping sequence retain deck labels. No noncompact contraction or solution of general C12 is asserted. C91 remains unchanged.',
 'proof_sha256':binding(target)['sha256'],
 'frozen_precursor':binding(source),
 'source_and_topology_audit':'work/root/review_general_pointed_descent.txt',
 'provenance':'work/part_c/c92_provenance.json'
}
(ROOT/'work/part_c/c92_result.json').write_text(json.dumps(row,indent=2)+'\n')
report_source=ROOT/'work/part_c/general_pointed_descent_comparison_report.txt'
report=('C.92: arbitrary pointed descents and the exact original lift topology\n'
        'Numbered promotion of the frozen complete GPD comparison.\n'
        'The proof body is transported by the exact GPD.n to C.92.n map.\n'
        'The radial unit-disk example explicitly takes d to be its Euclidean metric.\n'
        'Removing that recorded metric assignment and inverting the tag map recovers every source proof byte.\n'
        'The claim wrapper states the image, isometry, uniform-tail criterion and explicit sequence.\n'
        'General noncompact contraction and C12 remain unresolved.\n\n'+report_source.read_text())
(ROOT/'work/part_c/c92_report.txt').write_text(report)
record={'status':'EXACT_PROOF_TRANSPORT_PASS','source':binding(source),'target':binding(target),
        'removed_prefix':prefix,'equation_and_reference_map':tag_map,
        'added_claim_header':claim_header,'added_statement':statement_addition,
        'explicit_example_metric_assignment':{'source_text':metric_anchor,'numbered_text':metric_assignment},
        'added_wrappers':['\\end{claim}','\\begin{proof}','\\end{proof}'],
        'proof_body_inverse_transport_byte_identical':True,
        'tag_count':21,'balanced_display_pairs':numbered.count('\\['),
        'metadata':binding(ROOT/'work/part_c/c92_result.json'),
        'report_precursor':binding(report_source),'report':binding(ROOT/'work/part_c/c92_report.txt'),
        'root_review':binding(ROOT/'work/root/review_general_pointed_descent.txt'),
        'peer_review':'Pending independent D-agent completion; not yet registered in assembly.'}
(ROOT/'work/part_c/c92_provenance.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'source':record['source'],'target':record['target'],'tags':21,'displays':record['balanced_display_pairs']}))
