#!/usr/bin/env python3
"""Record the fully profinite completed-old construction after root review."""
from pathlib import Path
import json
w=Path(__file__).resolve().parents[1]
p=w/'notes/register_metadata.json'
m=json.loads(p.read_text())
m['A.90']={
 'answers':'A5; A9; A12; A15; L2; L9; L14; L20',
 'depends_on':'A.57; A.69; A.80; A.83; A.85; A.88; mixed-exponent root stabilizers; exact local root-symbol invariant; Chebotarev; Hasse-Weil; global Brauer reciprocity',
 'notes':'Constructs actual three-coordinate ordinary data in the full power completion, with each coordinate infinitely supported, t2=16/17, and the prescribed old quartic classes. Refinements Xi=uYi^h retain exact local points and zero root-symbol evaluations; exponent4h! is cofinal among all integers. The fixed new puncture c=-11/68 has no compatible global squareclass, hence no completed coordinate. The obstruction now concerns completed old data, not only finite-level points. It asserts no failure of a full-section puncture lift and no nonexistence of tuples for all rational punctures.',
 'uses_local_theorem':'no; local points and global completed classes are constructed directly',
 'manuscript_passages':'cote149; scans54–58,79–85,120–130; L2 and L20 exact puncture extension maps'}
p.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md'
s=p.read_text(); lines=s.splitlines()
scope={'A5':' The A.90 completed three-coordinate ghost has a specified fourth coordinate obstructed already modulo2.',
'A9':' A.90 now constructs actual completed old data with a prescribed rational puncture obstructed modulo2; this concerns completed coordinates and does not establish failure of a full-section puncture lift.',
'A12':' A.90 constructs an ordinary, infinitely supported completed old tuple through the finite Brauer-obstructed neighborhoods; the specified additional puncture has no global squareclass.',
'A15':' A.90 realizes the finite puncture obstruction on actual completed old data with a fully cofinal exponent tower.',
'L14':' A.88 gives its explicit Jacobian cocycle, and A.90 now realizes the obstruction on completed old data.',
'L20':' A.90 shows that a compatible completed old tuple need not acquire one specified rational coordinate, already modulo2. Its realization by a full section is not asserted.'}
for i,line in enumerate(lines[:50]):
 for key,extra in scope.items():
  if line.startswith('| '+key+' |'):
   columns=line.split(' | ')
   if 'A.90' not in columns[1]:columns[1]+=', A.90'
   line=' | '.join(columns)
   if extra not in line:line=line[:-2]+extra+' |'
   lines[i]=line
s='\n'.join(lines)+'\n'
heading='## Completed old-coordinate obstruction at05:38 UTC'
if heading not in s:
 s+='\n'+heading+'\n\nA.90 closes the outstanding completed-old-coordinate step from A.85 and A.88 for the explicit fixed example. It constructs three classes in the full power completion, not merely its two-primary factor, with exact ordinary local coordinates and infinite support. The cofinality is4h! after cycleh. At each refinement Xi=uYi^h, the new coefficient changes by an old-exponent power, so the old global class is preserved. Every controlled prime retains its exact T-coordinate; all local root-symbol evaluations remain individually zero. Mixed-exponent common fields, the ray-product choice and every local prime case are proved explicitly.\n\nThe fourth rational puncture c=-11/68 has no global squareclass with these local values: the normalized quaternion has invariant1/2 at2 and zero at every other place. Global Brauer reciprocity gives the contradiction. This provides actual completed old data through the earlier obstructed neighborhoods. It proves failure of extension for that tuple, while neither the all-rational-puncture ordinary problem nor either full assertion A1 is settled. The old open curve has four punctures including infinity, and its comparison with the tripod forgets the third finite puncture.\n'
p.write_text(s)
audit='05:38 UTC root audit A90: read mixed-exponent root-field lemma, specified parities and odd correction; checked stable boundary squareclasses and individual initial root-symbol zeros; checked ray inverse, principal idele and generated stabilizers; checked exact Xi=uYi^h map, Hensel precisions, geometric degree/genus and all unit-point bounds; checked every controlled/new/uncontrolled prime and T!=c; checked4h! full cofinality and fixed local T; checked infinite stable valuations and direct mod2 global Brauer contradiction. Passed. Independent audit and finite certificate are recorded separately.\n'
with (w/'notes/hour5_root_audits.md').open('a') as f:f.write(audit)
with (w/'notes/root_progress.md').open('a') as f:f.write('\n'+audit)
out='A90 full completed-old construction and exact obstruction integrated.\n'
Path(__file__).with_name('integrate_a90_output.txt').write_text(out)
print(out,end='')
