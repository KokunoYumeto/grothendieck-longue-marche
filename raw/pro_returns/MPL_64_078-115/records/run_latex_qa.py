#!/usr/bin/env python3
"""Compile an explicitly selected fragment with the QA wrapper.

Uses only installed TeX files, generating a private format and caches under the
output directory. Does not install/download anything or modify the fragment.
Root should run this only after finishing the relevant transcription edits.
"""
from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path


def main(argv=None):
    package = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fragment', type=Path, default=package/'MPL_64_078-115_transcription.tex')
    parser.add_argument('--wrapper', type=Path, default=package/'records'/'qa_wrapper.tex')
    parser.add_argument('--output-dir', type=Path, default=package.parent/'work'/'latex_qa')
    parser.add_argument('--jobname', default='qa_transcription')
    args = parser.parse_args(argv)
    fragment = args.fragment.resolve()
    wrapper = args.wrapper.resolve()
    output = args.output_dir.resolve()
    if not fragment.is_file() or not wrapper.is_file():
        parser.error('The selected fragment and wrapper must both exist.')
    for path in (fragment, wrapper):
        if any(c in str(path) for c in '{}%\n\r'):
            parser.error('The selected paths contain characters unsafe in a TeX input command.')
    output.mkdir(parents=True, exist_ok=True)
    directories = {name: output/name for name in ['formats', 'texmf-var', 'texmf-config', 'texmf-cache']}
    for path in directories.values():
        path.mkdir(exist_ok=True)

    environment = os.environ.copy()
    # Debian's default !! database-only tree paths do not resolve packages in
    # this container. Ordinary recursive tree paths locate the installed files.
    environment.update({
        'TEXMF': '{/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}',
        'TEXMFVAR': str(directories['texmf-var']),
        'TEXMFCONFIG': str(directories['texmf-config']),
        'TEXMFCACHE': str(directories['texmf-cache']),
        'TEXFORMATS': str(directories['formats']) + '//:',
    })

    def run(command, log_name):
        result = subprocess.run(
            command, cwd=output, env=environment,
            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        log = output/log_name
        log.write_text(result.stdout, encoding='utf-8')
        print(f'Exit {result.returncode}; output: {log}')
        if result.returncode:
            print(result.stdout[-12000:])
        return result.returncode

    if not (directories['formats']/'xelatex.fmt').is_file():
        result = run([
            '/usr/bin/xetex', '-ini', '-etex', '-interaction=nonstopmode',
            '-halt-on-error', '-no-shell-escape', '-jobname=xelatex',
            '-output-directory=' + str(directories['formats']), 'xelatex.ini',
        ], 'format_build.stdout.log')
        if result:
            return result

    source = r'\def\TranscriptionInput{' + str(fragment) + r'}\input{' + str(wrapper) + '}'
    result = run([
        '/usr/bin/xelatex', '-interaction=nonstopmode', '-halt-on-error',
        '-file-line-error', '-no-shell-escape', '-jobname=' + args.jobname,
        '-output-directory=' + str(output), source,
    ], args.jobname + '.stdout.log')
    if result == 0:
        print('PDF: ' + str(output/(args.jobname + '.pdf')))
        print('Compilation succeeded. This is not a visual or transcription-accuracy certificate.')
    return result


if __name__ == '__main__':
    raise SystemExit(main())
