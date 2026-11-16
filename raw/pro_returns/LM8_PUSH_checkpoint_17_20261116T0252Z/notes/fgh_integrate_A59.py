#!/usr/bin/env python3
"""Apply the independently approved A59 after root releases checkpoint10 freeze."""
from pathlib import Path
import json,shutil,subprocess,sys
r=Path(__file__).resolve().parents[1]
assert '--root-released' in sys.argv, 'Wait for explicit root release of the included-source freeze.'
assert (r/'notes/de_A59_audit.md').exists()
assert 'Post-checkpoint10 A59 full root audit' in (r/'notes/root_midday_audit.md').read_text()
src=r/'notes/fgh_A59_draft.tex'
dst=r/'sections/A_nilpotent_cover_normalizers.tex'
s=src.read_text().replace('% Candidate A.59. Notes only during the checkpoint freeze.','% A.59: registered after full root and DE proof/source/certificate audits PASS.')
s=s.replace('\\end{proof}', 'The exact certificate \\texttt{code/a_nilpotent_cover_normalizers.py}\nchecks every subgroup and both core formulas in three mixed-prime\nexamples, including nonnormal subgroups. The general proof above\nis independent of that finite sample.\n\\end{proof}')
dst.write_text(s)
for suffix in ['.py','.json','.out']:
 shutil.copyfile(r/('notes/fgh_A59_certificate'+suffix),r/('code/a_nilpotent_cover_normalizers'+suffix))
shutil.copyfile(r/'notes/fgh_A59_certificate_root_rerun.out',r/'code/a_nilpotent_cover_normalizers_root_rerun.out')
p=r/'sections/A.tex'; s=p.read_text(); old='\\input{sections/A_heisenberg_five_fixed.tex}'
assert old in s and 'A_nilpotent_cover_normalizers.tex' not in s
p.write_text(s.replace(old,old+'\n\\input{sections/A_nilpotent_cover_normalizers.tex}'))
row=json.loads((r/'notes/fgh_A59_row.json').read_text()); row['where_proved']='sections/A_nilpotent_cover_normalizers.tex'
row['notes']='Registered after full independent root and DE proof/source audits and certificate reruns PASS. The subgroup of a finite nilpotent group splits across its coprime direct factors even when nonnormal. The exact normal-core formulas give an actual prime-to-ell intermediate and an upper ell-group Galois closure. Good marked reduction of the original elliptic curve, including at2, and A57/A40 settle the intermediate. Induced pro-ell topology gives an actual open arithmetic embedding and exact cusp-inertia intersection. The certificate checks280 factorizations across70 subgroups in three examples, including32 distinct nonnormal subgroups. The unbounded proof does not depend on finite testing. Does not replace an ell-group Galois closure by mere ell-power degree. No full fixed-group or cofinality assertion.'
(r/'notes/fgh_A59_row.json').write_text(json.dumps(row,indent=2)+'\n')
p=r/'notes/a_results.json'; rows=json.loads(p.read_text()); assert not any(z['id']=='A.59' for z in rows); rows.append(row); p.write_text(json.dumps(rows,indent=2)+'\n')
p=r/'sections/A_general_cover_frontier.tex'; s=p.read_text(); anchor='\n\nA.46 supplies a general'
assert anchor in s
addition='\n\nA.59 further completes every coefficient-prime normalizer for\nevery cover whose geometric Galois closure is finite nilpotent,\nincluding all non-Galois covers with such a closure. Its actual\nintermediate cover has prime-to-coefficient Galois closure, while\nthe upper cover has coefficient-prime-group closure and induces\nan open pro-prime embedding. No such factorization is asserted\nfor arbitrary finite groups, and this normalizer theorem does\nnot determine the full fixed groups of all nilpotent covers.\n'
p.write_text(s.replace(anchor,addition+anchor))
p=r/'notes/root_cover_frontier_results.json'; rows=json.loads(p.read_text())
for z in rows:
 if z['id']=='A.45':
  z['depends_on']+='; A.59'
  z['notes']+=' A.59 completes every coefficient-prime normalizer on every finite cover with nilpotent geometric Galois closure, including nonnormal covering subgroups. Remaining universal normalizer cases are outside this entire class as well as the previously proved reduction criteria. This gives no cofinality and no full fixed-subgroup theorem for every nilpotent cover.'
p.write_text(json.dumps(rows,indent=2)+'\n')
(r/'notes/fgh_A59_audit.md').write_text('''# A59 integration and audit record\n\nRegistered after root explicitly released checkpoint10 and after both independent full audits passed. Root read the complete proof, reopened Silverman VII5.5 including its residue-two qualification, and reran the exact certificate. DE read the whole proof, reopened that source and the precise specialization scope, and independently reran the certificate. Full records are `notes/root_midday_audit.md` (Post-checkpoint10 A59) and `notes/de_A59_audit.md`.\n\nThe finite certificate verifies280 coefficient-prime factorizations over70 subgroups of D8×C3, Q8×C5 and H3×C2;32 subgroup examples are nonnormal. The proof itself handles arbitrary finite nilpotent geometric Galois closures. Actual group topologies, arithmetic maps and cusp intersections are proved before applying the reduction criterion. No full fixed-group or cofinality claim is made. Historical draft and output are retained.\n''')
with (r/'notes/fgh.md').open('a') as f:f.write('\n\n## A.59: every nilpotent geometric Galois closure\n\nRegistered after root and DE full proof/source/certificate audits PASS. Every finite cover with nilpotent geometric Galois closure has cuspidal arithmetically normalized procyclic subgroups at every coefficient prime. Arbitrary covering subgroups split across coprime direct factors; the exact normal cores provide the two required actual cover maps. Good reduction and the induced pro-prime topology then give the assertion. No universal fixed-group or cofinality conclusion is asserted.\n')
print('A59 registered, canonical proof/code/results/audits and A45 frontier updated.')
