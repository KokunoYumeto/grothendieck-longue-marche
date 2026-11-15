"""Render only copied TeX fragments for technical layout inspection.

Run validate_tex.py first.  No source scan, crop, archive, or contextual file is
read.  PDFs and PNGs stay outside the deliverable directory in the compilation
snapshot; only the JSON report is written beside this script.  The state-macro
definitions are those of the compilation harness, without editorial styling.
"""
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess

from PIL import Image, ImageChops
from validate_tex import PREAMBLE, ROOT


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--pages', nargs='+', type=int,
                        help='Optional scan numbers; default: all diagram/figure fragments.')
    args = parser.parse_args()
    compilation = json.loads((ROOT / 'records/tex_validation.json').read_text())
    snapshot = Path(compilation['snapshot_root'])
    env = os.environ.copy()
    env['TEXMF'] = '{/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf,/var/lib/texmf}'
    env['TEXFORMATS'] = str(snapshot) + os.pathsep
    selected = []
    for item in compilation['pages']:
        run_dir = Path(item['temporary_run_directory'])
        name = Path(item['file']).name
        raw = (run_dir / name).read_bytes()
        if hashlib.sha256(raw).hexdigest() != item['sha256']:
            raise RuntimeError('Copied fragment hash changed: ' + item['file'])
        scan = int(re.search(r'_scan(\d+)\.tex$', name).group(1))
        if args.pages is not None:
            include = scan in args.pages
        else:
            include = b'\\diagram{' in raw or b'\\figure{' in raw
        if include:
            selected.append(item)

    def render(item):
        run_dir = Path(item['temporary_run_directory'])
        name = Path(item['file']).name
        result = {'file': item['file'], 'sha256': item['sha256'],
                  'pngs': [], 'harness_font': 'Computer Modern'}

        def compile_pdf(latin_modern=False):
            preamble = PREAMBLE.replace(r'\begin{document}',
                (r'\usepackage{lmodern}' + '\n' if latin_modern else '')
                + r'\pagestyle{empty}' + '\n' + r'\begin{document}')
            maps = ['cm', 'cmextra', 'symbols', 'latxfont']
            if latin_modern:
                maps += ['lm-rm', 'lm-math', 'lm-ts1']
            wrapper = preamble + ''.join('\\pdfmapfile{+' + m + '.map}\n' for m in maps)
            wrapper += '\\input{' + name + '}\n\\end{document}\n'
            (run_dir / 'render_wrapper.tex').write_text(wrapper, encoding='utf-8')
            proc = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                 '-file-line-error', 'render_wrapper.tex'], cwd=run_dir, env=env,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, timeout=60)
            suffix = '_font_retry' if latin_modern else ''
            (run_dir / ('render' + suffix + '_stdout.txt')).write_text(proc.stdout)
            return proc

        proc = compile_pdf()
        if proc.returncode and 'tcrm' in proc.stdout:
            # The runtime's CM TS1 bitmap font setup is incomplete.  The
            # substitute is restricted to the temporary rendering harness.
            proc = compile_pdf(latin_modern=True)
            result['harness_font'] = 'Latin Modern (runtime CM TS1 fallback)'
        result['returncode'] = proc.returncode
        if proc.returncode:
            result['error'] = proc.stdout[-5000:]
            return result
        raster = subprocess.run(
            ['pdftoppm', '-r', '130', '-png', 'render_wrapper.pdf', 'render'],
            cwd=run_dir, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
            text=True, timeout=60)
        if raster.returncode:
            result['returncode'] = raster.returncode
            result['error'] = raster.stderr
            return result
        for png in sorted(run_dir.glob('render-*.png')):
            if not re.fullmatch(r'render-\d+\.png', png.name):
                continue
            im = Image.open(png).convert('RGB')
            mask = ImageChops.difference(im, Image.new('RGB', im.size, 'white'))
            bbox = mask.convert('L').point(lambda z: 255 if z > 30 else 0).getbbox()
            if bbox:
                padded = (max(0, bbox[0]-25), max(0, bbox[1]-25),
                          min(im.width, bbox[2]+25), min(im.height, bbox[3]+25))
                dest = png.with_name(png.stem + '-body.png')
                im.crop(padded).save(dest)
                result['pngs'].append(str(dest))
        result['pdf_page_count'] = len(result['pngs'])
        return result

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(render, selected))
    report = {
        'utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'source_compilation_snapshot': str(snapshot),
        'note': 'Generated output only. No original source images or context read. '
                'PDFs and PNGs are temporary technical QA material, not deliverables. '
                'Identity-style state macros display both uncertainty alternatives.',
        'harness_page_size': '50 cm by 70 cm; 1 cm margins; no page footer',
        'visual_inspection': 'Rendering success alone does not imply visual review.',
        'pages': results,
    }
    dest = ROOT / 'records/tex_render_validation.json'
    dest.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    failed = [r['file'] for r in results if r['returncode']]
    print(f'Rendered {len(results)} copied fragments; {len(failed)} failed.')
    for name in failed:
        print(name)
    print('Report:', dest)


if __name__ == '__main__':
    main()
