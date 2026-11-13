"""Prepare the exact C3:695 uncertain-tag binding without changing frozen inputs."""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import subprocess
import sys
sys.path.insert(0, str(Path('work/scripts').resolve()))
import fitz
import build_readers
import editorial
import mechanical_repairs
from texenv import environment
from verify_pdf import parse_log

ROOT = Path.cwd()
OUT = ROOT / 'work/layout_probes'
PACKAGE = 'LM_C3-682-696'
START = r'\noindent \deleted{\unsure{(17)}}\inserted{\unsure{(15)}}\quad'

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def rel(path): return path.relative_to(ROOT).as_posix()
def fragment(text):
    start = text.index(START, text.index(r'\scanpage{695}'))
    diagram = text.index(r'\diagram{', start)
    end = editorial.brace_end(text, diagram + len(r'\diagram'))
    return start, end, text[start:end]
def bound(old): return '\\begin{samepage}\n' + old + '\n\\end{samepage}'

def run(job):
    language, form, tex = job
    proc = subprocess.run(['lualatex', '--no-shell-escape', '-interaction=nonstopmode',
                           '-halt-on-error', tex.name], cwd=OUT, env=environment(),
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    tex.with_suffix('.console.txt').write_text(proc.stdout)
    counts = parse_log(tex.with_suffix('.log'))
    if proc.returncode:
        raise RuntimeError(tex.name + '\n' + proc.stdout[-2000:])
    pdfpath = tex.with_suffix('.pdf')
    images = []
    with fitz.open(pdfpath) as pdf:
        for page in pdf:
            boxes = page.search_for('(15)')
            if not boxes: continue
            box = boxes[0]
            out = tex.with_name(tex.stem + '_tagpage' + str(page.number + 1) + '_native3x.png')
            clip = fitz.Rect(45, max(0, box.y0 - 24), page.rect.width,
                             min(page.rect.height, box.y0 + 250))
            page.get_pixmap(matrix=fitz.Matrix(3,3), clip=clip, alpha=False).save(out)
            images.append({'path': rel(out), 'sha256': sha(out), 'page': page.number+1,
                           'tag_bbox': list(box), 'clip': list(clip),
                           'path_objects_on_tag_page': len(page.get_drawings()),
                           'basis': 'Native3x tag and complete immediate display region'})
        row = {'language': language, 'form': form, 'pdf': rel(pdfpath), 'pdf_sha256': sha(pdfpath),
               'probe_pdf_delivery_status': 'HISTORICAL_PROBE_NOT_DELIVERED_AS_PUBLICATION',
               'pages': len(pdf), 'images': images, 'compile_exit_code': proc.returncode,
               'error_count': counts['error_count'], 'overfull_count': counts['overfull_count'],
               'missing_character_count': counts['missing_character_count'],
               'log': rel(tex.with_suffix('.log')), 'log_sha256': sha(tex.with_suffix('.log')),
               'status': 'PENDING_ACTUAL_VISUAL_REVIEW'}
    print(language, form, 'tagpages', [(x['page'], x['path_objects_on_tag_page']) for x in images],
          'errors', row['error_count'], 'overfull', row['overfull_count'],
          'missing', row['missing_character_count'], flush=True)
    return row

def main():
    candidates, jobs = [], []
    for language in ('fr', 'en'):
        path = ROOT / 'sources' / ('fr/texts' if language == 'fr' else 'en/packages') / (PACKAGE + ('_en' if language == 'en' else '') + '.tex')
        source = path.read_bytes().decode('utf-8')
        a, b, source_old = fragment(source)
        old = source_old.replace('\r\n', '\n')
        repaired, _ = mechanical_repairs.repair(source.replace('\r\n', '\n'), PACKAGE, language)
        _, _, compile_old = fragment(repaired)
        variants = [{'old': old, 'new': bound(old)}]
        if compile_old != old:
            variants.append({'old': compile_old, 'new': bound(compile_old)})
        candidates.append({'id': '140-3-695-K15variant', 'language': language, 'package': PACKAGE,
                           'cote': '140-3', 'scan': 695, 'tag': '15', 'previous_cancelled_tag': '17',
                           'source_path': rel(path).removeprefix('sources/'), 'source_sha256': sha(path),
                           'source_line': source[:a].count('\n')+1, 'source_offset_start': a,
                           'source_offset_end': b, 'source_byte_start': len(source[:a].encode()),
                           'source_byte_end': len(source[:b].encode()), 'source_old': source_old,
                           'old': old, 'new': bound(old), 'variants': variants,
                           'expected_match_count': 1, 'original_content_unchanged': True,
                           'kind': 'equation-tag pagination',
                           'reason': 'Keep the unchanged cancelled uncertain tag(17), inserted uncertain tag(15), and their directly following complete Ni/Gi/SNi/G square together using a local samepage group. All variant wrappers, words, mathematical tokens, arrow endpoints and type sizes remain unchanged; only page-break penalties are added.'})
        for form in (0,1,2):
            parts = [build_readers.preamble(language, form), r'\begin{document}\LMcote{140-3}']
            for label, text in [('BEFORE', compile_old), ('AFTER', bound(compile_old))]:
                body, _, _ = editorial.annotate(r'\scanpage{695}' + '\n' + text + '\n', PACKAGE, language)
                body = body.replace(r'\scanpage{695}', '', 1)
                parts += [r'\clearpage\noindent ' + label + r' constrained-foot probe.\par',
                          r'\vspace*{\dimexpr\textheight-62pt\relax}\par\penalty0',
                          body, r'\par Following paragraph remains outside the binding.']
            parts.append(r'\end{document}')
            tex = OUT / f'scan695_tag15_{language}_{form}.tex'
            tex.write_text('\n'.join(parts))
            jobs.append((language, form, tex))
    (OUT / 'scan695_tag15_candidate.json').write_text(json.dumps(candidates, ensure_ascii=False, indent=2)+'\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        forms = list(pool.map(run, jobs))
    report = {'status': 'PENDING_ACTUAL_VISUAL_REVIEW', 'forms': forms,
              'candidate_file': 'work/layout_probes/scan695_tag15_candidate.json',
              'actual_before_publication_image': 'work/visual_repair_proofs/pagination_final/e70c983a802b8ac0/LM_FR_texte_de_lecture_p0777_15.png',
              'frozen_dependencies_modified': False, 'source_files_unchanged': True,
              'observations_generated_by_script': False}
    (OUT / 'scan695_tag15_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')

if __name__ == '__main__': main()
