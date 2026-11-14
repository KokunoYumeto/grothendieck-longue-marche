#!/usr/bin/env python3
"""Compile fresh scratch copies of page fragments; never modify source pages."""
from pathlib import Path
import argparse
import concurrent.futures
import hashlib
import json
import os
import shutil
import subprocess
import tempfile


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package-root', type=Path, default=here.parents[1])
    parser.add_argument('--work-dir', type=Path)
    parser.add_argument('--scans', nargs='*', type=int)
    parser.add_argument('--refresh', action='store_true', help='Compatibility option; copies are always refreshed.')
    args = parser.parse_args()
    package = args.package_root.resolve()
    work = (args.work_dir or Path(tempfile.mkdtemp(prefix='mpl_latex_validation_'))).resolve()
    work.mkdir(parents=True, exist_ok=True)
    if work == package or package in work.parents:
        raise SystemExit('Choose a scratch work directory outside the deliverable package.')

    env = os.environ.copy()
    # The supplied environment has package files but lacks lookup databases.
    # Removing database-only markers permits ordinary filesystem lookup.
    resolved = subprocess.run(['kpsewhich','-var-value=TEXMF'], capture_output=True, text=True, check=True).stdout.strip()
    if resolved:
        env['TEXMF'] = resolved.replace('!!','')
    env['TEXFORMATS'] = str(work) + ':'

    if not (work/'pdflatex.fmt').exists():
        fmt = subprocess.run(
            ['pdftex','-ini','-etex','-jobname=pdflatex','-progname=pdflatex',
             '-interaction=nonstopmode','-halt-on-error','pdflatex.ini'],
            cwd=work,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=60,
        )
        (work/'format_build_output.txt').write_bytes(fmt.stdout)
        if fmt.returncode:
            raise SystemExit(f'Format generation failed; see {work}/format_build_output.txt')

    sources = sorted((package/'pages').glob('*.tex'))
    if args.scans:
        wanted = {f'{n:03d}' for n in args.scans}
        sources = [p for p in sources if p.stem.rsplit('scan',1)[1] in wanted]
    if not sources:
        raise SystemExit('No matching page files found.')

    def compile_page(source):
        scan = source.stem.rsplit('scan',1)[1]
        directory = work/('scan'+scan)
        directory.mkdir(exist_ok=True)
        data = source.read_bytes()
        (directory/'source.tex').write_bytes(data)
        shutil.copyfile(here/'harness.tex',directory/'harness.tex')
        result = subprocess.run(
            ['pdflatex','-draftmode','-interaction=nonstopmode','-halt-on-error',
             '-file-line-error','-no-shell-escape','harness.tex'],
            cwd=directory,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=60,
        )
        (directory/'compiler_output.txt').write_bytes(result.stdout)
        return {
            'file':str(source.relative_to(package)), 'scan':scan,
            'sha256':hashlib.sha256(data).hexdigest(), 'returncode':result.returncode,
            'source_matched_compiled_snapshot':source.read_bytes()==data,
            'scratch_log':str(directory/'compiler_output.txt'),
        }

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(compile_page,sources))
    report = {'total':len(results),'passed':sum(r['returncode']==0 for r in results),'pages':results}
    (work/'compile_results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({'total':report['total'],'passed':report['passed'],'report':str(work/'compile_results.json')}))
    if report['passed'] != report['total']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
