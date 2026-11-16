#!/usr/bin/env python3
"""Record the independently reviewed Picard and local divisor calculations."""
from pathlib import Path
import json
w=Path(__file__).resolve().parents[1]
p=w/'notes/register_metadata.json'
m=json.loads(p.read_text())
data={
'A.88':('A9; A12; A15; L2; L14; L20','A.69; A.80; A.85; Colliot-Thelene-Skorobogatov Propositions4.3.2/4, Remarks4.3.3/5 and4.5.2; exact divisor complex and Hilbert norm symbols','The fixed genus33 old curve has an explicit nonzero Jacobian cocycle from the joint quaternion. Residues reduce every putative coordinate-character expression to64 quadratic possibilities, all with equal evaluation at the two chosen dyadic points, while the joint class differs by1/2. This excludes the exact coordinate-symbol image, with no claim about other functions or completed old data.'),
'A.89':('A5; A15; L10; L14','A.77; A.86; actual affine root-torsor decomposition action; integral ideal norm maps; levelwise cofinite convergence','Computes every local inverse divisor norm kernel away from the coefficient prime, and the coefficient-prime kernels at2 and3 plus real signs. The global image retains the exact levelwise cofinite convergence condition. For the stated2/3 range compatible corrections can be supported only at nonzero valuations ofA. The general dyadic proof uses the full local holomorph and its unique ramified quadratic subfield; the shifted-Eisenstein proof is restricted to v2(A)=0.')}
for key,(answers,depends,notes) in data.items():
 m[key]={'answers':answers,'depends_on':depends,'notes':notes,
 'uses_local_theorem':'no; explicit local points, divisors, root towers and character maps',
 'manuscript_passages':'cote149; scans54–58,79–85,120–130; precise item and lead scope in answers column'}
m['A.87']['notes']+=' The coefficient-three weighted congruence also fixes the dyadic pair for every lambda=4u with lambda=0 or1mod9. Thus every lambda=3^n+1, n>=1, is recognized with arbitrary labeled integral comparison.'
p.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md'
s=p.read_text()
heading='## Picard and divisor refinements at05:30 UTC'
if heading not in s:
 s+='\n'+heading+'\n\nA.88 gives a literal divisor cocycle for the nonconstant joint quaternion on the fixed genus33 curve of A.69. The Hochschild–Serre comparison identifies it with a nonzero class in H1(Q,J). Boundary residues force every possible finite-order coordinate character into a fixed quadratic field. All64 resulting coordinate-symbol combinations evaluate equally at the two chosen dyadic points; the joint quaternion differs by1/2. This proves the exact failure of that coordinate-symbol repair, while completed old-coordinate initialization is still under investigation.\n\nA.89 computes the actual inverse ideal-norm kernels prime by prime. At q distinct from the coefficient prime and vq(A)=0 the kernel is zero. At nonzero valuation it is the kernel of the residue-degree weighted sum on the stable prime branches. The coefficient kernels at2 and3 and the real sign kernel are zero in the stated range. The global map retains its levelwise cofinite-convergence image. An initial dyadic Eisenstein argument was narrowed to v2(A)=0; the full asserted range is proved using the unique ramified quadratic subfield of the local holomorph. No class-generation or compatible correction is inferred merely from these local kernels.\n\nA.87 now also uses the coefficient-three logarithm to remove the alternate dyadic labels for lambda=0 or1mod9 at dyadic valuation two. In particular the entire family3^n+1, n>=1, has arbitrary labeled integral recognition. The weighted congruence includes exponents divisible by3 and has an independent audit.\n'
lines=s.splitlines()
scope={'A5':'A.89','A12':'A.88','A15':'A.88–A.89','L10':'A.89','L14':'A.88–A.89','L20':'A.88'}
for i,line in enumerate(lines[:50]):
 for key,ids in scope.items():
  if line.startswith('| '+key+' |'):
   columns=line.split(' | ')
   if ids not in columns[1]:columns[1]+=', '+ids
   lines[i]=' | '.join(columns)
p.write_text('\n'.join(lines)+'\n')
audit='05:30 UTC root audits A88/A89: A88 divisor degrees32,32,16, cyclic total-complex sign and explicit coboundary checked; opened CT–Skoro exact HS statements and Remark4.5.2. Checked all boundary fields, valuations and dyadic norm argument. A89 affine finite-orbit proof, uniform orbit-length growth, actual residue-degree norms, stable ramified branches, real sign transition and exact global c0 image checked. Replaced overbroad dyadic power-removal step by full holomorph/unique ramified quadratic-subfield proof; shifted-Eisenstein certificate retains its valid v2A0 scope. Both statements independently reviewed. A87 weighted mod9 extension also passed root and birational-agent audits.\n'
with (w/'notes/hour5_root_audits.md').open('a') as f:f.write(audit)
with (w/'notes/root_progress.md').open('a') as f:f.write('\n'+audit)
output='A88/A89 and the strengthened A87 integrated with exact scope and corrected dyadic argument.\n'
Path(__file__).with_name('integrate_a88_a89_output.txt').write_text(output)
print(output,end='')
