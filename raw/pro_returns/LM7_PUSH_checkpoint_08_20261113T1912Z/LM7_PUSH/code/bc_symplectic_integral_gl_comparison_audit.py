#!/usr/bin/env python3
"""Read-only isolated replay of the uniform signed congruence comparison."""
from contextlib import redirect_stdout
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import shutil
import time
import sympy as sp

HERE = Path(__file__).resolve().parent
STEM = 'bc_symplectic_integral_gl_comparison_audit'
ROOT = 'e_symplectic_integral_gl_comparison_root'


def main():
    start = time.time()
    dependencies = ['de_ferrari_sl2_5_model.py','de_ferrari_sl2_5_model.npz',
                    'de_ferrari_sl2_5_source.json','de_ferrari_a6_source_data.py',
                    'de_ferrari_sl2_5_N.json','e_symplectic_five_integral_probe_root.json',
                    'e_symplectic_five_integral_residual_root.json']
    protected = [ROOT+suffix for suffix in ('.py','.json','.out')] + dependencies
    before = {n:sha256((HERE/n).read_bytes()).hexdigest() for n in protected}
    outdir = HERE.parent/'research'/'audit_geometry_integral_gl_comparison'
    outdir.mkdir(parents=True,exist_ok=True)
    for name in dependencies:
        shutil.copy2(HERE/name,outdir/name)
    spec = importlib.util.spec_from_file_location('geometry_integral_gl_root_replay',HERE/(ROOT+'.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.HERE = outdir
    with (outdir/(ROOT+'.out')).open('w') as output,redirect_stdout(output):
        mod.main()
    original = json.loads((HERE/(ROOT+'.json')).read_text())
    replay = json.loads((outdir/(ROOT+'.json')).read_text())
    mathematical = lambda d:{k:v for k,v in d.items() if k != 'seconds'}
    assert mathematical(original) == mathematical(replay)
    assert [r['exact_order'] for r in original['complete_signed_source_power_relations']] == [30,30]
    # Independent commutator multiplication, preserving the stated orientation.
    t = sp.Symbol('t')
    lower = sp.Matrix([[1,0],[t,1]])
    upper = sp.Matrix([[1,1],[0,1]])
    comm = lower*upper*lower.inv()*upper.inv()
    assert sp.simplify(comm - sp.Matrix([[1-t,t],[-t*t,t*t+t+1]])) == sp.zeros(2)
    actual = comm.subs(t,120)
    assert actual.applyfunc(lambda z:int(z)%25) == sp.Matrix([[6,20],[0,21]])
    rows = sp.Matrix([r['coordinates'] for r in original['normal_conjugate_Lie_basis']])
    determinant = int(rows.det())
    assert determinant % 5 != 0
    # The abelian kernel used in the full common quotient is exactly 60R=5R.
    assert sp.factorint(60//5) == {2:2,3:1}
    after = {n:sha256((HERE/n).read_bytes()).hexdigest() for n in protected}
    assert before == after
    result = {'status':'PASS_ISOLATED_SIGNED_INTEGRAL_COMMON_QUOTIENT_AUDIT',
              'all_mathematical_JSON_entries_identical':True,
              'complete_signed_x_y_orders':[30,30],
              'actual_modular_basis_comparisons':len(original['canonical_signed_modular_comparisons']),
              'independent_commutator_formula':[['1-t','t'],['-t^2','t^2+t+1']],
              'first_congruence_layer_basis_determinant':determinant,
              'abelian_kernel_identity':'60R=5R for R=product_{p>=5} Z_p',
              'protected_input_sha256':before,'all_originals_unchanged':True,
              'seconds':round(time.time()-start,3)}
    (HERE/(STEM+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__ == '__main__':
    main()
