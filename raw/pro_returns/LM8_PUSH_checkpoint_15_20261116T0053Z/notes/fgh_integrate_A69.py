#!/usr/bin/env python3
"""Integrate A69 only after root final approval; preserve all candidate files."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys
r=Path(__file__).resolve().parents[1]
assert '--root-approved' in sys.argv
for f in ['root_A69_audit.md','de_A69_audit.md','pbc_A69_audit.md']:
    assert (r/'notes'/f).exists(),f
s=(r/'notes/fgh_A69_draft.tex').read_text()
assert hashlib.sha256(s.encode()).hexdigest()=='ffa4f8fda611e071253a9275f015c2b3e26266481d968e45257c1fd82f4453f2'
s=s.replace('% A.69 candidate: not integrated pending independent proof/source audit.',
 '% A.69: full root, DE and PBC proof/source/exact-certificate audits PASS.')
s=s.replace('proof for every intermediate and both signs.\n',
 'proof for every intermediate and both signs.\nThe retained exact support is \\path{code/a_dihedral_two_power_fixed.py};\nits finite identities do not replace the unbounded geometric induction.\n')
assert s.count('\\[')==s.count('\\]')
name='A_dihedral_two_power_fixed'
(r/f'sections/{name}.tex').write_text(s)
p=r/'sections/A.tex';s=p.read_text();anchor=r'\input{sections/A_dihedral_eight_fixed.tex}'
assert s.count(anchor)==1 and name not in s
p.write_text(s.replace(anchor,anchor+'\n'+rf'\input{{sections/{name}.tex}}'))
# Copy exact executed program with registration-only metadata update, then rerun.
source=(r/'notes/fgh_A69_certificate.py').read_text()
source=source.replace("'candidate':'A.69, unregistered'","'statement':'A.69, Proved'")
code=r/'code/a_dihedral_two_power_fixed.py';code.write_text(source)
with code.with_suffix('.out').open('w') as out:
    subprocess.run([sys.executable,str(code)],stdout=out,stderr=subprocess.STDOUT,check=True)
old=json.loads((r/'notes/fgh_A69_certificate.json').read_text())
new=json.loads(code.with_suffix('.json').read_text())
old.pop('candidate');new.pop('statement');assert old==new
row=json.loads((r/'notes/fgh_A69_row.json').read_text())
row['notes']=row['notes'].replace('Unregistered candidate pending final independent audits.',
 'Registered after full independent root, DE and PBC proof/source/exact-certificate audits PASS.')
(r/'notes/fgh_A69_row.json').write_text(json.dumps(row,indent=2,ensure_ascii=False)+'\n')
p=r/'notes/a_results.json';rows=json.loads(p.read_text());assert not any(x['id']=='A.69' for x in rows)
rows.append(row);p.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
refs=(r/'notes/fgh_A69_refs.bib').read_text();p=r/'notes/fgh_refs.bib';oldrefs=p.read_text()
for key in ['fghLehrMatignon2005','fghSaidi2007','fghYang2024','fghVonk2021']:
    assert '{'+key+',' not in oldrefs
p.write_text(oldrefs+'\n'+refs)
p=r/'sections/A_general_cover_frontier.tex';s=p.read_text()
anchor='This does not settle arbitrary higher two-power dihedral covers.'
assert s.count(anchor)==1
s=s.replace(anchor,r'''A.69 now extends this conclusion uniformly to
\(v^2=w^{2m}\pm6w^m+1\) for every two-power \(m\),
including every actual intermediate. The primitive cyclotomic
new factor has special \(2\)-rank zero or is ordinary. The ordinary
alternative contradicts the actual cyclic component action,
finite-flat lifting of smooth fixed points, and the genus of the
rooted marked tree. This proves the displayed uniform family;
a classification of all possible dihedral closures is not asserted.''')
p.write_text(s)
p=r/'notes/root_cover_frontier_results.json';rows=json.loads(p.read_text())
for x in rows:
    if x['id']=='A.45':
        assert x['status']=='Open'
        if isinstance(x['depends_on'],list):x['depends_on'].append('A.69')
        else:x['depends_on']+='; A.69'
        x['notes']+=' A69 supersedes the preceding higher-level limitation for the displayed nonstable families: every two-power m in v²=w^(2m)±6w^m+1 and every actual intermediate now satisfy both all-prime assertions. The new proof combines the ramified nilpotent tree theorem with an ordinary-Prym exclusion, actual smooth fixed-point lifting and a rooted-tree genus contradiction. No classification of all possible dihedral closures or universal TaskA5 result is asserted.'
p.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
with (r/'notes/fgh.md').open('a') as f:
    f.write('\n\n## A69: uniform nonstable two-power dihedral family\n\nIntegrated after full root, DE and PBC proof/source/exact-code audits PASS. The actual C_m cover has D_(2m) closure, four cusps of indexm/2 and m-primary cusp differences. Potential good Jacobian comes from the precise ramified nilpotent-cover theorem. The primitive cyclotomic anti-Prym has special rank0 or is ordinary; the latter forces a full orbit of ordinary elliptic components, whose smooth fixed points cannot lift to the individually fixed generic cusps, and whose remaining branches force genus at leastm rather thanm−1. Actual norm maps and Frattini inertia give all intermediates. A41/A42 prove all-prime full fixed groups, A59 all normalizers. Universal A45 remains Open. No pattern extrapolation, marked-fibre slope extrapolation or arbitrary dihedral classification is used.\n')
p=r/'notes/fgh_A69_sources.md';s=p.read_text();s=s.replace('Status: complete written candidate, not registered pending final root and independent audits.',
 'Status: registered after full independent root, DE and PBC proof/source/exact-certificate audits PASS. Canonical proof: sections/A_dihedral_two_power_fixed.tex; canonical code and executed outputs: code/a_dihedral_two_power_fixed.py/.json/.out. Original candidate files remain preserved.')
p.write_text(s)
changed=[f'sections/{name}.tex','sections/A.tex','sections/A_general_cover_frontier.tex','notes/a_results.json','notes/fgh_refs.bib','notes/root_cover_frontier_results.json','notes/fgh_A69_row.json','notes/fgh_A69_sources.md','notes/fgh.md','code/a_dihedral_two_power_fixed.py','code/a_dihedral_two_power_fixed.json','code/a_dihedral_two_power_fixed.out']
record={'status':'PASS','statement':'A.69','audits':['notes/root_A69_audit.md','notes/de_A69_audit.md','notes/pbc_A69_audit.md'],'canonical_exact_rerun':'PASS, all mathematical fields equal candidate JSON','changed':[{'path':f,'sha256':hashlib.sha256((r/f).read_bytes()).hexdigest()} for f in changed],'scope':'Owner section/rows and narrow A45 update only; no assembled register/report/PDF rebuilt.'}
(r/'notes/fgh_A69_integration.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
