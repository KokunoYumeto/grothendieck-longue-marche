from pathlib import Path
import hashlib,json,difflib
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
ledger={'status':'PASS','authorization':'Root final authorization after full root, DE and PBC proof/source audits on 2026-11-16; no numerical premise or numerical replay applies.','files':[],'candidates':{},'editorial_changes':[]}
for n,name in [(78,'A_single_branch_kummer'),(79,'A_cyclic_derived_closures')]:
 src=R/f'notes/fgh_A{n}_draft.tex'; dst=R/f'sections/{name}.tex'
 assert not dst.exists(),dst
 old=src.read_text(); new=old.replace(f'% A.{n} candidate. Unregistered; full root/independent audits required.',f'% A.{n}: full root, DE and PBC proof/source audits PASS.')
 new=new.replace(f'{{A.{n}}}{{Open}}',f'{{A.{n}}}{{Proved}}')
 if n==78:
  for a,b in [('SB.2a','A.78.3'),('SB.1','A.78.1'),('SB.2','A.78.2'),('SB.3','A.78.4'),('SB.4','A.78.5')]:new=new.replace(a,b)
  new=new.replace('see the Stacks Project, Tag~0BRM.',r'see \cite[Lemma 15.116.4, Tag 0BRM]{fghStacksKummerModels}.')
  new=new.replace('see the Stacks Project, Tags~0CD9 and~0CDG.',r'see \cite[Lemmas 55.8.5 and 55.14.5, Tags 0CD9 and 0CDG]{fghStacksKummerModels}.')
  new=new.replace('Stacks Tags~0C5H and~0C5Q, or',r'\cite[Lemma 54.4.3 and \S54.17, Tags 0C5H and 0C5Q]{fghStacksKummerModels}, or')
  new=new.replace('By Stacks Tag~0C5H this requires',r'By \cite[Lemma 54.4.3, Tag 0C5H]{fghStacksKummerModels} this requires')
 else:
  new=new.replace('to the actual nilpotent Galois closure over the good',r'\cite[Theorem 6.13]{fghLehrMatignon2005} to the actual nilpotent Galois closure over the good')
 dst.write_text(new)
 diff=R/f'notes/fgh_A{n}_registration_editorial.diff';diff.write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=str(src.relative_to(R)),tofile=str(dst.relative_to(R)))))
 ledger['candidates'][str(n)]={'path':str(src.relative_to(R)),'sha256':sha(src),'canonical_path':str(dst.relative_to(R)),'canonical_sha256':sha(dst),'diff':str(diff.relative_to(R))}
 ledger['files'] += [str(dst.relative_to(R)),str(diff.relative_to(R))]
 ledger['editorial_changes'].append(f'A{n}: candidate status to Proved; exact opened-source citation markup; A78 SB display labels renamed A.78.1–5. No mathematical change.')
 assert new.count('\\[')==new.count('\\]'),n
bib=R/'notes/fgh_refs.bib';entry=(R/'notes/fgh_single_branch_kummer_refs.bib').read_text();assert 'fghStacksKummerModels' not in bib.read_text();bib.write_text(bib.read_text()+'\n'+entry);ledger['files'].append('notes/fgh_refs.bib')
a=R/'sections/A.tex';s=a.read_text();needle='\\input{sections/A_commutator_order_two.tex}';assert s.count(needle)==1;s=s.replace(needle,needle+'\n\\input{sections/A_single_branch_kummer.tex}\n\\input{sections/A_cyclic_derived_closures.tex}');a.write_text(s);ledger['files'].append('sections/A.tex')
rows=[{'id':'A.78','statement':'A single horizontal branch section in mixed characteristic gives rank-zero positive-genus vertical components after an actual Kummer base change; a p-group one-point cover of a good positive-genus rank-zero base has potential good Jacobian reduction of special p-rank zero.','status':'Proved','where_proved':'sections/A_single_branch_kummer.tex','depends_on':[],'answers':['Task A.5'],'notes':'Full root, DE and PBC proof/source audits PASS. Horizontal characteristic-zero Abhyankar is separate from vertical ramification. Actual semistable-model map and positive-component domination are proved. Global main components use Raynaud Proposition 1 only away from the horizontal section, followed by smooth Deuring–Shafarevich. No generic cusp-path conclusion follows without further hypotheses.'},{'id':'A.79','statement':'Both all-prime cusp assertions for every actual closure that is a quotient of P×B, with P a finite p-group having cyclic derived subgroup, B abelian of order prime to p, and p=2 or odd p congruent to 3 modulo 4; all intermediates are included.','status':'Proved','where_proved':'sections/A_cyclic_derived_closures.tex','depends_on':['A.40','A.41','A.42','A.59','A.66','A.76','A.78'],'answers':['Task A.5'],'notes':'Full root, DE and PBC proof/source audits PASS. Actual inertia equals the cyclic derived group; the actual elliptic quotient gives p-primary cusp differences and Frattini gives companions. The coprime abelian extension uses the actual connected isogeny pullback, extended Abel map, independently proved compact type and literal rational-path copies. Supersingular reduction places are explicit. Universal A.45 remains Open; no cofinality or arbitrary p-group fixedness claim.'}]
p=R/'notes/a_results.json';old=json.loads(p.read_text());assert not any(x['id'] in {'A.78','A.79'} for x in old);p.write_text(json.dumps(old+rows,indent=2,ensure_ascii=False)+'\n');ledger['files'].append('notes/a_results.json')
for row in rows:
 n=row['id'][2:];p=R/f'notes/fgh_A{n}_row.json';p.write_text(json.dumps(row,indent=2,ensure_ascii=False)+'\n');ledger['files'].append(str(p.relative_to(R)))
f=R/'sections/A_general_cover_frontier.tex';s=f.read_text();needle='these conclusions.\n';assert s.count(needle)==1;s=s.replace(needle,needle+r'''
A.78 now proves potential good Jacobian reduction of special
rank zero for every prime-power Galois cover of a good
positive-genus rank-zero curve branched at most at one
horizontal section in mixed characteristic. A.79 combines
this with the actual cusp-divisor relation for cyclic-derived
closures: for \(p=2\) or odd \(p\equiv3\pmod4\),
every quotient of a cyclic-derived \(p\)-group times a
prime-to-\(p\) abelian group satisfies both assertions,
including all intermediates. Its actual connected isogeny
pullback preserves each rational companion path.
The rank theorem alone does not give cusp torsion or a
rational companion path for an arbitrary prime-power group;
that fixed-group frontier and the universal question remain
open.
''');f.write_text(s);ledger['files'].append('sections/A_general_cover_frontier.tex')
p=R/'notes/fgh.md';p.write_text(p.read_text()+'''\n\n## A.78–A.79 registration, 2026-11-16 01:34 UTC\n\nRegistered after full root, DE and PBC proof/source audits. A.78 proves the actual mixed-characteristic single-section Kummer comparison and global rank-zero consequence. A.79 proves the cyclic-derived arithmetic family and full actual coprime abelian preservation. All candidate sources, exact editorial diffs and source ledgers are preserved. No numerical premise is used. Universal A.45 remains Open. See notes/fgh_A78_A79_integration.json and the root/DE/PBC audit ledgers.\n''');ledger['files'].append('notes/fgh.md')
p=R/'notes/fgh_single_branch_kummer_sources.md';p.write_text(p.read_text()+'''\n\n## Registration update\n\nA.78 and A.79 were authorized by root after full root, DE and PBC proof/source audits and registered on 2026-11-16. Candidate status and SB display labels were changed editorially in the canonical copies; precise Stacks citations were attached. Exact source/canonical hashes and diffs are in notes/fgh_A78_A79_integration.json. No numerical computation is a premise.\n''');ledger['files'].append('notes/fgh_single_branch_kummer_sources.md')
ledger['hashes']={q:sha(R/q) for q in ledger['files']}
(R/'notes/fgh_A78_A79_integration.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'status':'PASS','candidates':ledger['candidates'],'files':ledger['files']},indent=2))
