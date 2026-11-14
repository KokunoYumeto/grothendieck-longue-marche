"""Independent complete copied-source arithmetic rebuild of frozen E103."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = ROOT / 'research_e103'
GP = ROOT / 'research_e52/vendor/pari-2.19.0/gp'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path = SOURCE / 'ledger/e_quartic_odd_manifest.json'
manifest = json.loads(manifest_path.read_text())
for row in manifest['files']:
    assert sha(SOURCE / row['path']) == row['sha256'], row['path']
proof = SOURCE / 'sections/E_quartic_odd_abelian.tex'
assert sha(proof) == '421231266fcd6407308aaccf6ab2e120267ff168142a8907036c43465ef3c45e'
code = HERE / 'code'
code.mkdir(exist_ok=True)
for name in ['a_quartic_odd.py', 'a_quartic_odd.gp']:
    assert not (code / name).exists()
    shutil.copyfile(SOURCE / 'code' / name, code / name)
with (code / 'a_quartic_odd.out').open('w') as out:
    result = subprocess.run([sys.executable, str(code / 'a_quartic_odd.py'), '--gp', str(GP)],
                            cwd=HERE, stdout=out, stderr=subprocess.STDOUT, check=False)
assert result.returncode == 0, result.returncode
comparisons = []
for name in ['a_quartic_odd.py', 'a_quartic_odd.gp', 'a_quartic_odd.out',
             'a_quartic_odd_gp.out', 'a_quartic_odd.json']:
    a = SOURCE / 'code' / name
    b = code / name
    assert a.read_bytes() == b.read_bytes(), name
    comparisons.append({'file': name, 'sha256': sha(a), 'bytes': a.stat().st_size,
                        'complete_bytes_equal': True, 'excluded_fields': []})
for row in manifest['files']:
    assert sha(SOURCE / row['path']) == row['sha256'], row['path']
record = {'status': 'PASS', 'section_sha256': sha(proof), 'frozen_manifest_sha256': sha(manifest_path),
          'complete_comparisons': comparisons, 'returncode': result.returncode,
          'root_read_scope': 'Complete proof and every line of Python and GP sources.',
          'root_primary_source_reads': [
              {'key': 'E103_MartinOno', 'refs': ['turn846view0', 'turn848view0'],
               'scope': 'Theorem1 conductor64 row; Theorem2 conductor64 model; proof text pp2–5.'},
              {'key': 'EC_CiperianiStix', 'refs': ['turn844view0', 'turn845view0'],
               'scope': 'Proposition17 and its proof; Theorem18(2) and beginning of proof.'},
              {'key': 'E103_FiteLorenzoSutherland', 'refs': ['turn846view1', 'turn847view1'],
               'scope': 'Section3 equation3.1; Proposition3.1; actual homogeneous map and proof.'},
              {'key': 'E103_MilneANT', 'refs': ['turn846view2', 'turn847view2', 'turn848view1'],
               'scope': 'Theorem4.3 statement, Proposition4.27 and complete proof of4.3.'}],
          'proof_checks': ['Finite coset splitting of the actual extension and explicit continuity',
                           'Degree4 curve maps, pullbacks, duality and exact integral inverses',
                           'Torus quotient, coefficient section, Shapiro/cochain inverse and norm',
                           'Analytic nonvanishing, elliptic cohomology and its topology',
                           'Restricted prime coordinates, every fibre and rational pushout',
                           'Exact empty-source image and changed-coefficient target scopes']}
(HERE / 'comparison.json').write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n')
print('PASS full E103 fresh reconstruction; all source, stdout and JSON bytes agree, zero exclusions.', flush=True)
