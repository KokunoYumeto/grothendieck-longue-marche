#!/usr/bin/env python3
"""Build the paper with LuaLaTeX, retaining complete logs.

The supplied sandbox lacks both formats and luaotfload.  Its installed
LaTeX kernel and Type 1 Latin Modern fonts are sufficient.  This script
creates a separately named format whose only kernel modification replaces
the optional OpenType loader with an explicit OT1 startup.  The document
then selects T1.  No OpenType feature is emulated.  A normal full TeX Live
installation can compile LM7_PUSH_paper.tex directly with lualatex.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess

root = Path(__file__).resolve().parent.parent
build = root / 'build'
build.mkdir(exist_ok=True)
texlive = Path('/usr/share/texlive/texmf-dist')
texmf = Path('/usr/share/texmf')
env = os.environ.copy()
env.update({
    'TEXMF': '{' + str(build / 'texmf-var') + ',' + str(texmf) + ',' + str(texlive) + '}',
    'TEXMFVAR': str(build / 'texmf-var'),
    'TEXMFCONFIG': str(build / 'texmf-config'),
    'TEXMFCACHE': str(build / 'texmf-var'),
    'TEXFORMATS': str(build),
    'TEXINPUTS': str(root) + ':' + str(build) + ':',
    'BIBINPUTS': str(root) + ':',
})
for key in ['TEXMFVAR', 'TEXMFCONFIG', 'TEXMFCACHE']:
    Path(env[key]).mkdir(parents=True, exist_ok=True)

kernel = (texlive / 'tex/latex/base/latex.ltx').read_text()
start = kernel.index('\\everyjob\\expandafter{%\n  \\the\\everyjob\n  \\directlua{%\n  if xpcall')
end = kernel.index('\n\\fi\n%%% From File: ltexpl.dtx', start)
original = kernel[start:end]
assert "require('luaotfload-main')" in original
replacement = r'''\everyjob\expandafter{%
  \the\everyjob
  \def\encodingdefault{OT1}%
  \let\f@encoding\encodingdefault
  }
'''.rstrip()
modified = ('% LM7 local Type 1 LuaLaTeX format: modified startup loader only.\n'
            '% Original kernel license and notices follow unchanged.\n'
            + kernel[:start] + replacement + kernel[end:])
(build / 'lm7_latex_type1.ltx').write_text(modified)
ini = (texlive / 'tex/latex/tex-ini-files/lualatex.ini').read_text()
ini = ini.replace('\\input latex.ltx', '\\input lm7_latex_type1.ltx')
(build / 'lm7_lualatex.ini').write_text(ini)
history = []
main_source = root / 'LM7_PUSH_paper.tex'
included_sources = [root / name for name in re.findall(
    r'\\InputIfFileExists\{([^}]+)\}', main_source.read_text())]
source_paths = [main_source, *included_sources, root/'LM7_PUSH_references.bib']
source_hashes = {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
                 for path in source_paths}

def run(args, log):
    with (build / log).open('w') as out:
        result = subprocess.run(args, cwd=root, env=env, stdout=out,
                                stderr=subprocess.STDOUT)
    history.append({'argv': args, 'log': 'build/' + log,
                    'exit_code': result.returncode})
    (build / 'build_commands.json').write_text(json.dumps(history, indent=2) + '\n')
    if result.returncode:
        raise RuntimeError(f'{args[0]} failed; see build/{log}')

run(['luahbtex', '-ini', '-interaction=nonstopmode', '-halt-on-error',
     '-jobname=lm7lualatex', '-output-directory=build',
     str(build / 'lm7_lualatex.ini')], 'format_type1_console.log')
latex = ['lualatex', '-fmt=lm7lualatex', '-interaction=nonstopmode',
         '-halt-on-error', '-recorder', '-output-directory=build', str(main_source)]
run(latex, 'pass1_console.log')
run(['bibtex', 'build/LM7_PUSH_paper'], 'bibtex_console.log')
run(latex, 'pass2_console.log')
run(latex, 'pass3_console.log')
log = (build / 'LM7_PUSH_paper.log').read_text()
input_paths = set()
for line in (build/'LM7_PUSH_paper.fls').read_text().splitlines():
    if line.startswith('INPUT '):
        path = Path(line[6:])
        input_paths.add((path if path.is_absolute() else root/path).resolve())
expected_tex = {main_source.resolve(), *(p.resolve() for p in included_sources)}
assert expected_tex <= input_paths, sorted(str(p) for p in expected_tex-input_paths)
project_tex = {p for p in input_paths if p.suffix == '.tex' and p.is_relative_to(root)}
assert project_tex == expected_tex, sorted(str(p) for p in project_tex^expected_tex)
assert all(hashlib.sha256((root/name).read_bytes()).hexdigest() == value
           for name, value in source_hashes.items()), 'A source changed during the build.'
manifest = {'all_active_tex_sources_read': True,
            'no_preserved_tex_source_read': True,
            'sources_unchanged_during_build': True,
            'source_sha256': source_hashes,
            'actual_project_tex_inputs': sorted(str(p.relative_to(root)) for p in project_tex)}
(build/'source_input_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
overflows = [float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt', log)]
summary = {
    'format': 'lm7lualatex (LuaHBTeX, LaTeX kernel, Type 1 fonts)',
    'optional_opentype_loader_disabled': True,
    'overfull_boxes': len(overflows),
    'overfull_boxes_over_2pt': sum(x > 2 for x in overflows),
    'max_overflow_pt': max(overflows, default=0),
    'undefined_citations': bool(re.search(r'Citation .* undefined', log)),
    'undefined_references': 'There were undefined references' in log,
    'active_source_input_manifest_verified': True,
}
(build / 'typesetting_summary.json').write_text(json.dumps(summary, indent=2) + '\n')
shutil.copy2(build / 'LM7_PUSH_paper.pdf', root / 'LM7_PUSH_paper.pdf')
print(json.dumps(summary, indent=2))
