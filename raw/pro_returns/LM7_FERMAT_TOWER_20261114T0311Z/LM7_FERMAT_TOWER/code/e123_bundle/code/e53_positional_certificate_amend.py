#!/usr/bin/env python3
"""Preserve actual first outputs and make two certificate-only clarifications."""
from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parents[1]
H=R/'code/history/first_finite_checker'
assert not H.exists()
H.mkdir(parents=True)
saved=[]
for stem in ('e53_positional_maps','e53_positional_presentation'):
 for ext in ('.py','.gp','.out','.err','.bin'):
  p=R/'code'/(stem+ext)
  if p.exists():
   q=H/p.name;shutil.copy2(p,q)
   saved.append({'path':str(q.relative_to(R)),'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
p=R/'code/e53_positional_maps.py'
s=p.read_text()
old="gp_unit=records('e53_positional_verify')"
new="""gp_unit=(HERE/'e53_positional_verify.out').read_text().splitlines()
assert len(gp_unit)==8 and all(s.startswith('PASS ') for s in gp_unit)
assert gp_unit[-1]=='PASS complete no-input polynomial and residue verification'
gp_err=(HERE/'e53_positional_verify.err').read_text().splitlines()
assert all(not s.strip() or s.strip().startswith('***   Warning: new stack size = ') for s in gp_err)"""
assert old in s
p.write_text(s.replace(old,new))
p=R/'code/e53_positional_presentation.gp'
s=p.read_text()
old='full actual S-class group, using E121 order'
new='full actual three-primary S-class group, using E121 order'
assert old in s
p.write_text(s.replace(old,new))
out={'status':'PASS','preserved':saved,
 'initial_checker_exit':1,
 'initial_checker_failure':'The independent no-input GP verifier prints eight PASS lines, not JSON. The strict reader now checks that exact text format.',
 'presentation_wording':'Explicitly types the certified group as the entire three-primary S-class subgroup. All ideal identities and matrices are unchanged.',
 'no_arithmetic_change':True}
(H/'amendment.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

