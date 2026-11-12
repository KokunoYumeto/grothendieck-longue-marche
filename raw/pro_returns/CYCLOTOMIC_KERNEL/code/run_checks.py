"""Re-run every finite mathematical certificate and preserve its stdout."""
import json
import platform
import subprocess
import sys
from pathlib import Path
import sympy

CODE=Path(__file__).resolve().parent
PROGRAMS=[
 ('A_boundary_checks.py','A_boundary_checks.out'),
 ('B_field_certificates.py','B_field_certificates.out'),
 ('D_coverings.py','D_coverings_output.txt'),
 ('D_cyclotomic_counterexample.py','D_cyclotomic_counterexample_output.txt'),
 ('root_math_checks.py','root_math_checks_output.json'),
]
records=[]
for script,output in PROGRAMS:
    result=subprocess.run([sys.executable,str(CODE/script)],capture_output=True,text=True)
    if result.returncode:
        raise RuntimeError(f'{script} failed:\n{result.stdout}\n{result.stderr}')
    (CODE/output).write_text(result.stdout)
    records.append({'program':script,'output':output,'exit_code':result.returncode,
                    'stderr':result.stderr})
summary={'python':platform.python_version(),'sympy':sympy.__version__,
         'all_checks_passed':True,'programs':records}
(CODE/'run_checks_output.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
