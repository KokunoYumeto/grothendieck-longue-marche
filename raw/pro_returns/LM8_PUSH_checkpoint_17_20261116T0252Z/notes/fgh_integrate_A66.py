#!/usr/bin/env python3
"""Register A66 only after complete root and DE independent approval."""
from pathlib import Path
import json
import shutil
import sys

r=Path(__file__).resolve().parents[1]
assert '--root-approved' in sys.argv
assert (r/'notes/root_A66_audit.md').exists()
assert (r/'notes/de_A66_audit.md').exists()
assert json.loads((r/'notes/fgh_A66_certificate.json').read_text())['status']=='PASS'
text=(r/'notes/fgh_A66_draft.tex').read_text()
text=text.replace('% A.66 candidate. NOTES ONLY, UNREGISTERED; independent audits required.',
                  '% A.66: full root and DE independent proof/source/certificate audits PASS.')
text=text.replace(r'\begin{statement}{A.66}{Open}{Candidate: Heisenberg times prime-to-prime abelian closure}',
                  r'\begin{statement}{A.66}{Proved}{Heisenberg times prime-to-prime abelian closure}')
text=text.replace(r'\begin{proof}[Candidate proof, pending independent audits]',r'\begin{proof}')
text=text.replace(r'\end{proof}',r'''The exact certificate
\path{code/a_heisenberg_abelian_products.py}
exhausts the subgroups in three actual coprime product groups
and checks the degree, genus, cusp and copied-tree identities.
The actual model comparison is the proof above.
\end{proof}''')
(r/'sections/A_heisenberg_abelian_products.tex').write_text(text)
code=(r/'notes/fgh_A66_certificate.py').read_text().replace(
    "'statement':'A66 candidate, unregistered'","'statement':'A66, fully independently audited'")
(r/'code/a_heisenberg_abelian_products.py').write_text(code)
for suffix in ('.json','.out'):
    shutil.copyfile(r/('notes/fgh_A66_certificate'+suffix),
                    r/('code/a_heisenberg_abelian_products'+suffix))
for owner in ('root','de'):
    shutil.copyfile(r/f'notes/{owner}_A66_certificate_rerun.out',
                   r/f'code/a_heisenberg_abelian_products_{owner}_rerun.out')
p=r/'sections/A.tex';s=p.read_text()
anchor=r'\input{sections/A_heisenberg_intermediates.tex}'
assert anchor in s and 'A_heisenberg_abelian_products.tex' not in s
p.write_text(s.replace(anchor,anchor+'\n'+r'\input{sections/A_heisenberg_abelian_products.tex}'))
row={
 'id':'A.66','statement':'Every Heisenberg times prime-to-p abelian closure has both all-prime cusp assertions',
 'status':'Proved','where_proved':'sections/A_heisenberg_abelian_products.tex',
 'depends_on':['A.40','A.41','A.42','A.59','A.61','A.62','A.65'],
 'answers':['Task A.5'],
 'notes':'Registered after full root and DE proof/source/certificate audits PASS. Every subgroup of H_p times a prime-to-p abelian group splits into its two coprime factors. Actual coprime Galois function fields identify the cover with a connected elliptic-isogeny base change of an A65 intermediate. The ordinary noncentral quotient has a radicial main by total/separable degrees; compact type follows explicitly from the Jacobian norm. The good prime-to-p isogeny extends finite étale; its pullback has one connected radicial main and disjoint copies of every constant subtree and rational marked path. A42 gives full fixed inertia; A59 separately gives normalizers. This does not treat products of two nonabelian Sylows or universal nilpotent fixedness.'
}
(r/'notes/fgh_A66_row.json').write_text(json.dumps(row,indent=2)+'\n')
p=r/'notes/a_results.json';rows=json.loads(p.read_text())
assert not any(x['id']=='A.66' for x in rows)
rows.append(row);p.write_text(json.dumps(rows,indent=2)+'\n')
p=r/'sections/A_general_cover_frontier.tex';s=p.read_text()
anchor='transferring fixedness through a surjective pro-prime quotient.'
assert s.count(anchor)==1
addition=r'''
A.66 allows an additional abelian geometric factor of order prime to
the Heisenberg prime, including all nonnormal intermediate subgroups.
The actual elliptic-isogeny base change preserves one connected
radicial main and copies each rational marked joining path.
Products of two nonabelian Sylow factors are still outside this
argument; no general nilpotent fixed-group assertion follows.
'''
p.write_text(s.replace(anchor,anchor+'\n'+addition))
p=r/'notes/root_cover_frontier_results.json';rows=json.loads(p.read_text())
for x in rows:
    if x['id']=='A.45':
        assert x['status']=='Open'
        if isinstance(x['depends_on'],list):
            if 'A.66' not in x['depends_on']:x['depends_on'].append('A.66')
        else:x['depends_on']+='; A.66'
        x['notes']+=' A66 adds every closure quotient of H_p times a prime-to-p abelian group, through actual connected elliptic-isogeny base change and copied rational cusp paths. Two nonabelian Sylow products and universal nilpotent fixedness remain outside this result.'
p.write_text(json.dumps(rows,indent=2)+'\n')
p=r/'notes/fgh_A66_sources.md';s=p.read_text().replace(
 'Status: complete notes-only candidate, unregistered and awaiting full root/secondary audits.',
 'Status: registered after full root and DE proof/source/executed-certificate audits PASS; original candidate retained.')
s+='\nCanonical proof: sections/A_heisenberg_abelian_products.tex; canonical certificate: code/a_heisenberg_abelian_products.py. Independent audit ledgers: notes/root_A66_audit.md, notes/de_A66_audit.md.\n'
p.write_text(s)
(r/'notes/fgh_A66_audit.md').write_text('''# A66 registration record

Registered after complete root and DE independent proof/source/exact-certificate audits PASS and explicit root integration authorization following the22:00 checkpoint save. Full ledgers are notes/root_A66_audit.md and notes/de_A66_audit.md; both independent reruns are retained canonically with the certificate. The original notes candidate, exact outputs and source ledger remain intact.

The ordinary noncentral compact-type condition is explicitly justified by the actual surjective Jacobian norm and Serre–Tate good-reduction invariance. Its main radicial map is proved by total and separable degrees. The actual prime-to-p elliptic base change preserves the connected main and copies entire constant subtrees, so every selected cusp retains a rational marked companion. All closure and intermediate claims are derived from the actual coprime function-field compositum and subgroup decomposition.

A45 remains Open. This adds one nonabelian exponent-p Heisenberg factor with a coprime abelian factor, not two nonabelian Sylows, a cofinal family, or all nilpotent fixed subgroups.
''')
with (r/'notes/fgh.md').open('a') as f:
    f.write('\n\n## A.66: one Heisenberg factor and a coprime abelian factor\n\nRegistered after root and DE full proof/source/certificate PASS. Every closure quotient of H_p×B, p odd and B abelian of order prime to p, has both all-prime cusp assertions, including all intermediate subgroups. The actual proper elliptic-isogeny base change preserves the unique connected radicial main, the compact-type tree and every rational cusp joining path. Two nonabelian Sylow products and the universal TaskA5 remain outside the theorem.\n')
print('A66 integrated after full root/DE approval; A45 remains Open.')
