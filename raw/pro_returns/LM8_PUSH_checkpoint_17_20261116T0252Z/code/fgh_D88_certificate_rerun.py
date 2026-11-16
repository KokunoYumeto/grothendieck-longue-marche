#!/usr/bin/env python3
"""Independent retained execution of the complete D88 owner certificate."""
from pathlib import Path
import hashlib
import json
import runpy

root = Path(__file__).resolve().parents[1]
source = root/'notes/de_sha_cusp_finite_depth_certificate.py'
namespace = runpy.run_path(str(source), run_name='fgh_independent_D88_audit')
result = namespace['run']()
original = json.loads(source.with_suffix('.json').read_text())
assert result == original and result['status'] == 'PASS'
out = {'status':'PASS','entire_owner_JSON_equal':True,
       'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
       'original_JSON_sha256':hashlib.sha256(source.with_suffix('.json').read_bytes()).hexdigest(),
       'owner_files_modified':False,'result':result}
(root/'notes/fgh_D88_certificate_rerun.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','entire_owner_JSON_equal':True,
                  'norm_rows':len(result['distinguished_relative_norms']),
                  'shell_rows':len(result['weighted_shell_functions']),
                  'orbit_transitions':len(result['literal_invariant_orbit_pushforwards']),
                  'actual_kernel_zero_rows':len(result['actual_infinite_kernel_generator']),
                  'tangent_rows':len(result['actual_rational_tangents'])},indent=2))
