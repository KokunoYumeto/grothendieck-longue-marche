#!/usr/bin/env python3
"""Retain the first nf-only run and strengthen literal prime membership checks."""
from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parents[1]
D=R/'code/history/standalone_prime_membership'
assert not D.exists();D.mkdir(parents=True)
saved=[]
for name in ['e53_positional_make_ideals.py','e53_positional_make_ideals.out',
             'e53_positional_ideals.gp','e53_positional_ideals.out','e53_positional_ideals.err',
             'e53_positional_maps.py','e53_positional_maps.out','e53_positional_maps.err','e53_positional_maps.json']:
 p=R/'code'/name
 if p.exists():
  shutil.copy2(p,D/name);saved.append({'path':str((D/name).relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
p=R/'code/e53_positional_make_ideals.py';s=p.read_text()
old="f'check(idealnorm(L,J)=={p} && idealval(L,beta-{b1},idealprimedec(L,{p})[1])>=0,\"lower prime norm\");',"
new="f'check(nfisideal(L,J) && idealnorm(L,J)=={p} && idealadd(L,J,beta-{b1})==J,\"literal lower prime and chosen residue\");',"
assert old in s;s=s.replace(old,new)
old="elif t=='upper_pivot_relation':\n  target="
new="""elif t=='upper_pivot_relation':
  lines.append('check(nfisideal(F,'+gm(a['prime_HNF'])+') && idealnorm(F,'+gm(a['prime_HNF'])+')=='+str(a['prime'])+' && idealadd(F,'+gm(a['prime_HNF'])+',Mod(x-'+str(a['beta_residue'])+',F.pol))=='+gm(a['prime_HNF'])+',\"literal upper prime and chosen residue\");')
  target="""
assert old in s;s=s.replace(old,new);p.write_text(s)
p=R/'code/e53_positional_maps.py';s=p.read_text()
old="upper=records('e53_positional_presentation')"
new="""upper=records('e53_positional_presentation')
standalone=records('e53_positional_ideals')
st=row(standalone,'standalone_literal_ideal_verification')
assert st['upper_ideal_equalities']==7 and st['lower_ideal_equalities']==2
assert st['actual_projected_classes']==[[4,1],[4,0]]
assert st['unconditional_maximal_orders'] is True"""
assert old in s;s=s.replace(old,new)
old="HERE/'e53_positional_presentation.gp',HERE/'e53_positional_presentation.out',"
new=old+"\n    HERE/'e53_positional_ideals.gp',HERE/'e53_positional_ideals.out',"
assert old in s;s=s.replace(old,new);p.write_text(s)
out={'status':'PASS','preserved':saved,
 'change':'The nf-only verifier now checks the literal lower and upper HNF ideals are ideals of prime norm and contain the exact beta-minus-residue element. The earlier nonnegative valuation check at an arbitrary listed lower prime was redundant and is replaced.',
 'mathematical_values_changed':False,'all_old_runs_retained':True}
(D/'amendment.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

