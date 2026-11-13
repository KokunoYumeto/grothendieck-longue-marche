"""Recompile regenerated pagination probe TeX and bind prior raster evidence.

Only an exact per-page pixel match carries a previous actual inspection.  A
changed page leaves the refreshed validation pending; the tool cannot create
new visual observations.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import json, hashlib, subprocess, shutil, re, sys
import fitz
from texenv import environment

ROOT=Path(__file__).resolve().parents[2]
D=ROOT/'work/layout_probes'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()


def pixels(path):
    with fitz.open(path) as doc:
        return [hashlib.sha256(p.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).samples).hexdigest() for p in doc]


def main():
    path=D/'tag_pattern_stress_validation.json'
    prior=json.loads(path.read_text())
    history=D/'tag_stress_revision512_historical'
    history.mkdir(exist_ok=False)
    shutil.copyfile(path,history/path.name)
    snapshots={}
    for row in prior:
        pdf=ROOT/row['pdf'];assert sha(pdf)==row['pdf_sha256']
        for source in (pdf,pdf.with_suffix('.log')):
            shutil.copyfile(source,history/source.name)
        snapshots[row['pdf']]=dict(pdf_sha256=sha(pdf),page_pixel_sha256=pixels(pdf),
            historical_pdf=str((history/pdf.name).relative_to(ROOT)))
    def compile_one(row):
        pdf=ROOT/row['pdf'];tex=pdf.with_suffix('.tex')
        result=subprocess.run(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',tex.name],
            cwd=D,env=environment(),text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        tex.with_suffix('.console.txt').write_text(result.stdout)
        log=pdf.with_suffix('.log').read_text(errors='replace')
        gate=dict(exit=result.returncode,errors=len(re.findall(r'^!',log,re.M)),
            overfull_hboxes=log.count('Overfull \\hbox'),overfull_vboxes=log.count('Overfull \\vbox'),missing=log.count('Missing character:'))
        assert not any(gate.values()),(tex,gate)
        current=pixels(pdf);old=snapshots[row['pdf']]
        identical=len(current)==len(old['page_pixel_sha256']) and current==old['page_pixel_sha256']
        print(row['language'],row['form'],gate,'all_page_pixels_identical',identical,flush=True)
        return row,dict(language=row['language'],form=row['form'],pdf=row['pdf'],
            previous_pdf=old['historical_pdf'],previous_pdf_sha256=old['pdf_sha256'],
            pdf_sha256=sha(pdf),tex=str(tex.relative_to(ROOT)),tex_sha256=sha(tex),
            log_sha256=sha(pdf.with_suffix('.log')),compile=gate,
            previous_page_pixel_sha256=old['page_pixel_sha256'],current_page_pixel_sha256=current,
            all_pages_pixel_identical=identical,
            status='PASS_EXACT_PIXEL_IDENTITY' if identical else 'PENDING_ACTUAL_CHANGED_PAGE_REVIEW')
    results=[]
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures=[pool.submit(compile_one,row) for row in prior]
        for future in as_completed(futures):
            row,result=future.result();results.append(result)
    results.sort(key=lambda r:(r['language'],r['form']))
    all_identical=all(r['all_pages_pixel_identical'] for r in results)
    if all_identical:
        lookup={(r['language'],r['form']):r for r in results}
        refreshed=[]
        for row in prior:
            r=lookup[row['language'],row['form']]
            row['pdf_sha256']=r['pdf_sha256'];row['source_tex_sha256']=r['tex_sha256'];row['log_sha256']=r['log_sha256']
            row['pixel_identity_carryover']=dict(status='PASS',historical_pdf=r['previous_pdf'],
                historical_pdf_sha256=r['previous_pdf_sha256'],pixel_scale=2,all_pages_identical=True,
                prior_actual_inspected_pages=row.get('inspected_image_pages',[]),
                reason='Every current rendered page is pixel-identical to its preserved historical PDF page; only the explicitly listed prior actual-image observations are carried.')
            refreshed.append(row)
        path.write_text(json.dumps(refreshed,ensure_ascii=False,indent=2)+'\n')
    report=dict(status='PASS' if all_identical else 'PENDING_ACTUAL_CHANGED_PAGE_REVIEW',
        publication_sources_modified=False,probe_only=True,
        previous_validation=str((history/path.name).relative_to(ROOT)),
        previous_validation_sha256=sha(history/path.name),
        actual_visual_observations_created_by_script=False,forms=results)
    (D/'tag_pattern_stress_revision578_refresh.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(report['status'],flush=True)


if __name__=='__main__':main()
