#!/usr/bin/env python3
"""Initialize only local TeX format/font-map assets; no manuscript access."""
import argparse
import importlib.util
import os
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assets-dir',type=Path,required=True)
    args = parser.parse_args()
    assets = args.assets_dir.resolve()
    for subdirectory in ['formats','maps','tex','var','config','cache']:
        (assets/subdirectory).mkdir(parents=True,exist_ok=True)
    (assets/'tex'/'language.dat').write_text('english hyphen.tex\n',encoding='utf-8')
    map_paths = sorted(Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts').glob('*.map'))
    map_paths.append(Path('/usr/share/texmf/fonts/map/dvips/lm/lm.map'))
    if not all(p.is_file() for p in map_paths) or len(map_paths)<2:
        parser.error('installed Debian TeX font maps were not found at expected paths')
    (assets/'maps'/'pdftex.map').write_text('\n'.join(p.read_text() for p in map_paths),encoding='utf-8')
    harness_path = Path(__file__).resolve().with_name('compile_harness.py')
    spec = importlib.util.spec_from_file_location('mpl_compile_harness',harness_path)
    harness = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(harness)
    os.environ['MPL_TEX_ASSETS'] = str(assets)
    env = harness.lookup_environment()
    command = ['pdftex','-ini','-etex','-jobname=pdflatex','-progname=pdflatex',
               '-interaction=nonstopmode','-halt-on-error','pdflatex.ini']
    result = subprocess.run(command,cwd=assets/'formats',env=env,text=True,capture_output=True)
    (assets/'format-build.stdout.txt').write_text(result.stdout,encoding='utf-8')
    (assets/'format-build.stderr.txt').write_text(result.stderr,encoding='utf-8')
    print(f'Local TeX assets: {assets}')
    print(f'Format build exit: {result.returncode}')
    if result.returncode:
        print(result.stdout[-5000:])
        print(result.stderr[-2000:])
    else:
        print('Set MPL_TEX_ASSETS to this absolute directory when running compile_harness.py.')
    return result.returncode


if __name__ == '__main__':
    raise SystemExit(main())
