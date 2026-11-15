#!/usr/bin/env python3
"""Compile a fragment using an isolated scratch wrapper; never alter its bytes."""
import argparse
import os
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('fragment', type=Path)
    parser.add_argument('--timeout', type=int, default=300)
    args = parser.parse_args()
    fragment = args.fragment.resolve(strict=True)
    base = Path(__file__).resolve().parent
    output = base / 'runs' / fragment.stem
    output.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env['TEXMF'] = '{/etc/texmf,/var/lib/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}'
    env['TEXMFVAR'] = str(base / 'texmf-var')
    env['TEXMFCONFIG'] = str(base / 'texmf-config')
    env['TEXMFCACHE'] = str(base / 'texmf-cache')
    # Avoid implicit dependency downloads or any shell execution from TeX.
    env['MKTEXFMT'] = '0'
    fmt = base / 'xelatex.fmt'
    if not fmt.is_file():
        command = ['xetex', '-ini', '-etex', '-no-shell-escape',
                   '-interaction=nonstopmode', '-halt-on-error',
                   '-jobname=xelatex', '-output-directory=' + str(base), 'xelatex.ini']
        result = subprocess.run(command, cwd=base, env=env, capture_output=True,
                                text=True, timeout=args.timeout)
        (base / 'format_build.stdout').write_text(result.stdout + result.stderr)
        if result.returncode:
            print('Isolated format build failed; see', base / 'format_build.stdout')
            return result.returncode
    wrapper = output / 'wrapper.tex'
    # detokenize permits spaces; reject characters with TeX grouping semantics.
    for path in (base, fragment):
        if any(character in str(path) for character in '{}%\n\r'):
            raise ValueError('Unsafe path characters for TeX input')
    wrapper.write_text(
        '\\input{\\detokenize{' + str(base / 'validation_preamble.tex') + '}}\n'
        '\\begin{document}\n'
        '\\input{\\detokenize{' + str(fragment) + '}}\n'
        '\\end{document}\n', encoding='utf-8')
    command = ['xetex', '-fmt=' + str(fmt), '-no-shell-escape',
               '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
               '-output-directory=' + str(output), str(wrapper)]
    result = subprocess.run(command, cwd=output, env=env, capture_output=True,
                            text=True, timeout=args.timeout)
    stdout = output / 'compile.stdout'
    stdout.write_text(result.stdout + result.stderr, encoding='utf-8')
    print('Exit status:', result.returncode)
    print('Full compiler output:', stdout)
    print('TeX log:', output / 'wrapper.log')
    if result.returncode == 0:
        print('Technical PDF:', output / 'wrapper.pdf')
    else:
        print((result.stdout + result.stderr)[-5000:])
    print('Wrapper checks syntax, not source accuracy or diplomatic layout.')
    return result.returncode


if __name__ == '__main__':
    raise SystemExit(main())
