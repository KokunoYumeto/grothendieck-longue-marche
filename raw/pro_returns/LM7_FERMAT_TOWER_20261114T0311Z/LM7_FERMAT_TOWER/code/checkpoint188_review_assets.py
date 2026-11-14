"""Retain exact executed GP output aliases and render selected 188-result pages."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import shutil
import subprocess

BASE = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
pdf = BASE / 'LM7_FERMAT_TOWER_paper.pdf'
expected = '5cd216f8733c964f0fdb6516dcbc92b2221681a075a569851f5091a5c93f9e75'
assert sha(pdf) == expected
code = BASE / 'code/e94_root_rebuild/code'
aliases = []
for stem in ['e_basechange_field', 'e_basechange_ninth_genus', 'e_basechange_ninth_norms']:
    source = code / ('e_mu27_dependency_' + stem + '.out')
    target = code / (stem + '.out')
    assert source.is_file() and source.stat().st_size
    assert not target.exists()
    shutil.copyfile(source, target)
    assert source.read_bytes() == target.read_bytes()
    aliases.append({'program': str((code / (stem + '.gp')).relative_to(BASE)),
                    'actual_driver_stage_output': str(source.relative_to(BASE)),
                    'same_stem_output_alias': str(target.relative_to(BASE)),
                    'sha256': sha(target)})
details = BASE / 'qa/details188'
details.mkdir(exist_ok=True)
pages = [43, 46, 50, 53, 169, 170, 171, 172, 185, 190,
         473, 474, 475, 476, 478, 479, 480, 481, 483, 486,
         487, 488, 489, 491, 492, 493, 498]
def render(page):
    prefix = details / ('page_' + str(page).zfill(3))
    run = subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page),
                          '-singlefile', '-r', '110', '-jpeg', str(pdf), str(prefix)],
                         text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    assert run.returncode == 0, (page, run.stdout)
    image = prefix.with_suffix('.jpg')
    return {'page': page, 'file': str(image.relative_to(BASE)), 'sha256': sha(image),
            'command_returncode': run.returncode, 'actual_stdout_stderr': run.stdout}
with ThreadPoolExecutor(max_workers=3) as pool:
    renders = list(pool.map(render, pages))
record = {'status': 'PASS', 'pdf_sha256': expected,
          'executed_output_aliases': aliases, 'detail_renders': renders,
          'visual_inspection_claimed_by_program': False}
(details / 'manifest.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
