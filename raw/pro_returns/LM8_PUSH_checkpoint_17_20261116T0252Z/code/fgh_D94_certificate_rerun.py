#!/usr/bin/env python3
"""Independent read-only whole-result replay of the D94 certificate."""
from pathlib import Path
import hashlib, importlib.util, json
ROOT=Path(__file__).resolve().parents[1]
OWNER=ROOT/'notes/de_ordinary_two_parameter_certificate.py'
EXPECTED=OWNER.with_suffix('.json')
def run():
    before={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (OWNER,EXPECTED,OWNER.with_suffix('.out'))}
    spec=importlib.util.spec_from_file_location('fgh_d94_owner_readonly',OWNER)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    result=mod.run()
    actual=json.dumps(result,indent=2)+'\n'
    assert actual.encode()==EXPECTED.read_bytes(), 'Whole result differs from owner JSON'
    after={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (OWNER,EXPECTED,OWNER.with_suffix('.out'))}
    assert before==after, 'Owner artifact changed'
    return actual,before
if __name__=='__main__':
    actual,hashes=run()
    (ROOT/'notes/fgh_D94_certificate_rerun.json').write_text(actual)
    print(actual,end='')
    meta={'status':'PASS','whole_json_byte_equal':True,'owner_files_unchanged':True,'owner_hashes':hashes,'result_sha256':hashlib.sha256(actual.encode()).hexdigest()}
    (ROOT/'notes/fgh_D94_certificate_rerun_metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
