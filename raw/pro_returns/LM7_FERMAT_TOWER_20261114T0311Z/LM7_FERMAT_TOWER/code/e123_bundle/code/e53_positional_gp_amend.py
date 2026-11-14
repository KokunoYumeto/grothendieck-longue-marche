#!/usr/bin/env python3
"""Preserve the actual first GP verification failure and fix two API uses."""
from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parent
H=R/'history/initial_gp_verify';H.mkdir(parents=True,exist_ok=True)
for suffix in ['.gp','.out','.err']:
 p=R/('e53_positional_verify'+suffix);q=H/p.name
 assert not q.exists()
 shutil.copyfile(p,q)
p=R/'e53_positional_verify.gp';old=p.read_text()
new=old.replace('test(denominator(W),2809,"power basis denominator");','test(lcm(vector(#c,i,denominator(c[i]))),2809,"power basis denominator");')
new=new.replace("F=ffinit(53,2,z);\nzz=ffgen(F,'a);\nroots=polrootsff(z^2+z+1,zz);",'rr0=Mod(z,Mod(1,53)*(z^2+z+1));\nroots=[rr0,rr0^2];')
assert new!=old
p.write_text(new)
record={'status':'preserved and corrected','original_gp_exit_code':0,
 'actual_error_record':'initial_gp_verify/e53_positional_verify.err',
 'original_run_not_counted_as_PASS':True,
 'correction':['Use the lcm of scalar coefficient denominators.','Use literal quotient-ring finite-field elements, avoiding the wrong polrootsff call.'],
 'unchanged_mathematical_values':['Literal W and V','absolute norms','vertical resultant norm','norm to K','positive tame exponent936'],
 'old_sha256':hashlib.sha256(old.encode()).hexdigest(),'new_sha256':hashlib.sha256(new.encode()).hexdigest()}
(H/'amendment.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
