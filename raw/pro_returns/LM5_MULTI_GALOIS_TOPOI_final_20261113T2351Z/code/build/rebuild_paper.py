"""Build the integrated paper from an extracted archive with LuaLaTeX/BibTeX.

Usage: python code/build/rebuild_paper.py
Optional --runtime-format and --texmf support the restricted authoring runtime.
No network access is needed. A normal TeX Live installation needs neither option.
"""
from pathlib import Path
import argparse, json, os, re, shutil, subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--package', type=Path)
parser.add_argument('--runtime-format', type=Path)
parser.add_argument('--texmf')
args = parser.parse_args()
package = args.package or Path(__file__).resolve().parents[2]
stem = 'LM5_MULTI_GALOIS_TOPOI_paper'
assert (package / f'{stem}.tex').is_file(), package
env = dict(os.environ)
if args.runtime_format:
    env['TEXFORMATS'] = str(args.runtime_format.resolve()) + ':'
if args.texmf:
    env['TEXMF'] = args.texmf
logs = package / 'verification' / 'rebuild'
logs.mkdir(parents=True, exist_ok=True)
commands = [
    ('build_01.log', ['lualatex', '-interaction=nonstopmode', '-halt-on-error', f'{stem}.tex']),
    ('bibtex.log', ['bibtex', stem]),
    ('build_02.log', ['lualatex', '-interaction=nonstopmode', '-halt-on-error', f'{stem}.tex']),
    ('build_final.log', ['lualatex', '-interaction=nonstopmode', '-halt-on-error', f'{stem}.tex']),
]
execution = []
for name, command in commands:
    with (logs / name).open('w') as output:
        result = subprocess.run(command, cwd=package, env=env, stdout=output, stderr=subprocess.STDOUT)
    execution.append({'command': command, 'exit_code': result.returncode, 'log': str(Path('verification/rebuild') / name)})
    if result.returncode:
        raise SystemExit(f'Build failed: {name}, exit {result.returncode}')
text = (logs / 'build_final.log').read_text()
overflows = [float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt', text)]
undefined = len(re.findall(r'(?:undefined|Rerun to get cross-references right)', text))
missing = len(re.findall(r'Missing character:', text))
pages = int(re.search(r'Output written on .*?\((\d+) pages', text, re.S).group(1))
record = {'commands': execution, 'pdf_pages': pages,
          'overfull_boxes_final': len(overflows), 'overfull_above_2pt': sum(x > 2 for x in overflows),
          'undefined_diagnostics': undefined, 'missing_characters': missing,
          'optional_luaotfload_fallback': 'Error in luaotfload: reverting to OT1' in text}
(logs / 'rebuild_output.json').write_text(json.dumps(record, indent=2) + '\n')
shutil.copy2(logs / 'build_final.log', package / 'build_final.log')
shutil.copy2(logs / 'bibtex.log', package / 'bibtex.log')
print(json.dumps(record, indent=2))
assert not record['overfull_above_2pt'], 'Overfull box exceeds the requested 2 pt limit'
assert not undefined, 'Undefined or unstable cross-reference remains'
assert not missing, 'Missing glyph remains'
