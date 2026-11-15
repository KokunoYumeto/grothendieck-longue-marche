#!/usr/bin/env python3
"""Check another correction in the same retained original complete cover."""
import argparse,hashlib,json,re
from pathlib import Path
ap=argparse.ArgumentParser()
ap.add_argument('result_stem',type=Path)
ap.add_argument('--stem',type=Path,required=True)
args=ap.parse_args()
b=Path(__file__).parent
result=args.result_stem.with_name(args.result_stem.name+'_certificate.json')
d=json.loads(result.read_text())
assert d['coefficients'][:2]==[0,0] and d['s_count']==10
original=b/'pbc_modular_validation_cover.g'
t=original.read_text()
t,n=re.subn(r'^coefficients:=.*?;;$',
    'coefficients:='+json.dumps(d['coefficients'][2:],separators=(',',':'))+';;',t,flags=re.M)
assert n==1
out=args.stem.with_suffix('.g');out.write_text(t)
meta={'correction':d['coefficients'],'source_cover':'pbc_hopf_difference_hermite_validation_certificate.json',
      'hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),result,original,out)}}
args.stem.with_suffix('.inputs.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
