#!/usr/bin/env python3
"""Integrate the independently accepted unnumbered original transporter result."""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[2]
gate=json.loads((ROOT/'work/root/actual_transporter_acceptance_269.json').read_text())
assert gate['status']=='PASS_ROOT_AND_PEER' and not gate['numbered_claim_added']
changes=[]
def once(text,old,new):
 assert text.count(old)==1,(old,text.count(old))
 return text.replace(old,new)
def edit(name,fn):
 p=ROOT/name;old=p.read_bytes();new=fn(old.decode()).encode()
 assert new!=old
 p.write_bytes(new)
 changes.append({'path':name,'old_sha256':sha256(old).hexdigest(),'new_sha256':sha256(new).hexdigest()})

table_note=(' The independently reviewed original transporter reduction identifies the complete '
 'D74.40 solution space with T times Zhat using the unique original endpoint transporters. '
 'Its exact defect is D(k)=x^k u1^-1 z^k u2 Y^(k+1), k=(mu-1)/2. '
 'It proves both parametrization maps, reflection independence, the sign identity, '
 'the precise inclusion into the folded parameter space, and actual finite refinement '
 'arrows. A faithful mod-two homology quotient of the standard extension, of parity '
 'order60*2^61, removes four extra coarse unit residues by a complete binary-chain '
 'calculation. Nonemptiness of the original T and full realization remain unresolved.')
def report(text):
 anchor='rows=[(label, current_269[label][0], current_269[label][1])'
 addition="_refs, _state = current_269['D.b']\ncurrent_269['D.b'] = (_refs, _state + "+repr(table_note)+')\n'
 text=once(text,anchor,addition+anchor)
 anchor="add_report('work/root/research_update_269.md')"
 return once(text,anchor,anchor+"\nadd_report('work/part_d_attack/actual_transporter_single_parameter_reduction.txt',title='Original transporter solution spaces and an actual finite homology refinement')")
edit('work/root/make_report.py',report)
addition=r'''### Original transporter continuation: complete solution-space maps

The separate unnumbered continuation retains the original \(F=\widehat F(x,y)\), \(z=(xy)^{-1}\), involution, coboundary \(h\), and \(Y=hyh^{-1}\). For an original \(z\)-reflection \(r\) in the first endpoint class, the two unique actual transporters satisfy

\[
r=u_1(xs)u_1^{-1},\qquad zr=u_2(Ys)u_2^{-1}.
\]

Define \(k=(\mu-1)/2\) using the proved inverse map on \(2\widehat{\mathbb Z}\), and retain the original word

\[
D(k)=x^k u_1^{-1}z^k u_2Y^{k+1},\qquad
T=\{\mu\in\widehat{\mathbb Z}^{\times}:D((\mu-1)/2)=1\}.
\]

The complete original boundary-equation solution space is homeomorphic to \(T\times\widehat{\mathbb Z}\). The forward map sends \((\mu,\lambda)\) to the solution with conjugator \(x^ku_1^{-1}z^\lambda\); the inverse extracts its exponent with the original \(x\)-coordinate character. Both composites are proved. The two actual full section-centralizer equalities supply the unique transporter comparison, and the original endpoint labels prove that the correcting reflection exponent is even.

The word is independent of the chosen reflection under the explicit simultaneous transporter change. It lies in \(F'\), and its actual sign identity is \(\alpha(D(k))=D(-k-1)\). The folded solution-space map becomes inclusion of the original parameter set into the folded parameter set, times the identity of \(\widehat{\mathbb Z}\). Its additional parameter values are exactly the nonidentity values of this same \(D(k)\) in the actual kernel of the folded map.

The finite comparisons also retain the original maps. There is a displayed same-level injection \(T_N\to B_N\). Two compactness refinements of the actual full centralizer and inverter equalities construct a finer quotient with the reverse unit-coordinate map \(B_{N'}\to T_N\). These refinements are proved without asserting nonemptiness of any parameter space.

For the actual standard extension, the explicit quotient \(A_5\times C_2^3\) has coarse unit sets

\[
\operatorname{pr}(B_{N_0})=\{1,11,19,29,31,41,49,59\},\quad
T_{N_0}=\{1,19,41,59\}\pmod {60}.
\]

The note constructs the actual refinement \(F/\overline{[N_G,N_G]N_G^2}\) from binary chains on the labelled 60-vertex Cayley graph, with an explicit quotient map to the coarse parity kernel. The spanning tree and all 61 Schreier cycle vectors prove that this is the entire original quotient, whose order is \(60\cdot2^{61}\). Exact binary linear algebra determines every conjugator fiber. Its successful unit residues modulo 120 are \(1,19,41,59,61,79,101,119\), whose reductions modulo 60 are exactly the coarse \(T_{N_0}\). Thus this particular actual refinement removes all four additional coarse residues. The difference between the two finite equations at the refined level is also retained.

Root and peer read the complete 391-line note and 361-line canonical program. Each isolated replay passed all 24 named checks and the full-group substitutions for all 40 retained chain witnesses. The complete JSON output and stdout reproduce the original bytes, SHA-256 `43f8ceef3d62899e624a99b3699fcc17256c9dae49f8599d6c45a43c5b52b92d`. The acceptance record binds both full reviews, both replays and the original dependencies without editing historical author metadata. The nonemptiness of the actual \(T\), full generation and the original realization remain unresolved; this continuation adds no numbered claim.

'''
edit('work/root/research_update_269.md',lambda text:once(text,'### Final document and archive verification',addition+'### Final document and archive verification'))
edit('work/root/package_deliverable.py',lambda text:once(text,
 '`code/part_a`, `code/part_b`, `code/part_c`, and `code/root` contain every\nmathematical program, its captured outputs, the finite presentation caches,',
 '`code/part_a`, `code/part_b`, `code/part_c`, and `code/root` contain the\nmain mathematical programs and their captured outputs. The original\ntransporter and finite-generation continuations are retained under\n`work/part_d_attack/code`; isolated independent replays are retained in their\nexplicit `work/` directories. The archive also includes the finite presentation caches,'))
(ROOT/'work/root/transporter_report_integration_269.json').write_text(json.dumps({'status':'PASS','changes':changes,'numbered_claim_added':False},indent=2)+'\n')
print(json.dumps({'status':'PASS','changed_files':len(changes),'numbered_claim_added':False},indent=2))
