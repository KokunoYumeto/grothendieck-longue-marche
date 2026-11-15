"""Finalize post-freeze research metadata; never touches transcription files."""
from pathlib import Path
import json

R=Path(__file__).resolve().parent
def read(name): return json.loads((R/name).read_text())
def write(name, rows): (R/name).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')

rows=read('research_structure_notes.json')
for n in rows:
    if n['id']=='M07': n['quote']=r'\(G(X,\xi)=\underline{\operatorname{Aut}}(\xi)\)'
write('research_structure_notes.json',rows)

rows=read('research_period_notes.json')
for n in rows:
    if n['id']=='P12':
        n['body']=n['body'].replace('the unfinished independence sentence','the partly illegible independence sentence')
write('research_period_notes.json',rows)

rows=read('research_notes_seed.json')
for n in rows:
    if n['id']=='A37':
        n['body']=n['body'].replace('The deleted reduction through the projective line is a discarded route, not a proof of reconstruction.','The deleted reduction through the projective line supplies no proof of the general reconstruction; X02–X03 give a separate conditional argument for ordinary complex points and chosen field embeddings when the integral Hodge lattice is retained.')
    if n['id']=='A38':
        n['body']=n['body'].replace('integral polarization data','integral lattice data').replace('X01 gives an explicit family test.','X01–X03 give an explicit family and the precise injectivity test it supports.')
write('research_notes_seed.json',rows)

rows=read('research_additional_notes.json')
rows=[n for n in rows if n['id'] not in ['X02','X03']]
rows.extend([
dict(id='X02',title='The integral Hodge structure separates points in the test family',kind='own idea',location='15/225:L3,16',quote=r'foncteur dans les structures de Hodge ?; d’invariant l’indéterminée \(j\)',terms=['Hodge','elliptique','VA','Z-modules'],context='Adds an explicit integral test to CT54/003,005 and CT44/008’s abelian realization framework; no chosen-point injectivity argument of this form was located in the supplied context',ledger='MPL_14_002-044 M24a [first-pass lead]; WG2 §2.4 #3 [unchecked plan; this is a conditional test, not a status change]',body=r'For an elliptic curve, recover its analytic torus as \(E(\mathbf C)\simeq(F^1H^1(E,\mathbf C))^\vee/\iota H_1(E,\mathbf Z)\), where \(\iota(\gamma)(\omega)=\int_\gamma\omega\); the integral Hodge structure determines this construction (Milne, 2005/2017, Theorem 6.8). An integral Hodge isomorphism therefore induces a holomorphic group isomorphism of the elliptic curves, so for the family X01 it implies \(1728t_1=1728t_2\) and hence \(t_1=t_2\). Confidence: high, because the period embedding of the actual lattice, together with the exact j-calculation, gives the implication without an additional chosen polarization. Replacing the integral lattice by rational cohomology retains only the isogeny class, so this proof does not establish equality of j in that variant (Milne, 2005/2017, Corollary 6.9).'),
dict(id='X03',title='A conditional separation of chosen complex embeddings',kind='own idea',location='15/225:L3,9,16;15/227:L3',quote=r'Attention, il faut parler des pl. complexes',terms=['Hodge','plongement','place','elliptique'],context='Adds an objectwise integral criterion to CT54/003,005 and the abelian comparisons in CT44/008–009; the supplied materials do not state this chosen-embedding separation argument',ledger='MPL_14_002-044 M24a and §3 [first-pass leads]; WG2 §2.4 #3 [unchecked plan; restricted injectivity evidence only]',body=r'Let \(\sigma,\tau:k\hookrightarrow\mathbf C\) be chosen field embeddings, and suppose their Betti–Hodge realizations are isomorphic on an integral category containing \(h^1(E_a)\) for every \(a\in k\setminus\{0,1\}\), with the X01 family defined over k. Applying X02 objectwise gives \(1728\sigma(a)=1728\tau(a)\) for every such a, hence \(\sigma=\tau\), since embeddings also fix 0 and 1. Confidence: high for this conditional implication, because it uses only the reconstructed elliptic curves and the explicit invariant; even objectwise integral Hodge isomorphisms suffice. The hypotheses require preservation of the integral lattice and ordinary Hodge type over the identity of \(\mathbf C\); they do not settle the rational-functor variant, the essential image, or a formulation that identifies conjugate Hodge structures.')
])
write('research_additional_notes.json',rows)
print('Updated research quotations and added X02–X03; no transcription files accessed')
