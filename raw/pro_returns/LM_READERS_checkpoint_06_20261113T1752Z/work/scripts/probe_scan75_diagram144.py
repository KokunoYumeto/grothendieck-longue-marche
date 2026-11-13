#!/usr/bin/env python3
"""Exact paired local parenthesis-anchor probe, C4:75 equation144."""
from pathlib import Path
import argparse
import concurrent.futures
import hashlib
import json
import subprocess
import fitz
import build_readers
import editorial
import mechanical_repairs
from texenv import environment
from verify_pdf import parse_log

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'work/layout_probes'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p): return p.relative_to(ROOT).as_posix()

def run(job):
    language,form,variant,tex=job
    proc=subprocess.run(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',tex.name],cwd=OUT,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    tex.with_suffix('.console.txt').write_text(proc.stdout)
    log=parse_log(tex.with_suffix('.log'))
    if proc.returncode: raise RuntimeError('Equation144 probe failed: '+tex.name)
    pdf=tex.with_suffix('.pdf')
    with fitz.open(pdf) as doc:
        page=doc[0]
        native=tex.with_name(tex.stem+'_native6x.png')
        page.get_pixmap(matrix=fitz.Matrix(6,6),clip=fitz.Rect(65,65,545,260),alpha=False).save(native)
        bounds=fitz.Rect()
        for kind,box in page.get_bboxlog():
            r=fitz.Rect(box)
            if r.y0<400 and not r.is_empty: bounds|=r
        row={'language':language,'form':form,'variant':variant,'pdf':rel(pdf),'pdf_sha256':sha(pdf),'pages':len(doc),
             'image':rel(native),'image_sha256':sha(native),'ink_bbox_without_footer':list(bounds),
             'ink_width':bounds.width,'ink_height':bounds.height,'log':rel(tex.with_suffix('.log')),'log_sha256':sha(tex.with_suffix('.log')),
             'compile_exit_code':proc.returncode,'error_count':log['error_count'],'overfull_count':log['overfull_count'],
             'missing_character_count':log['missing_character_count'],'status':'PENDING_ACTUAL_VISUAL_REVIEW'}
    print(language,form,variant,'errors',row['error_count'],'overfull',row['overfull_count'],'missing',row['missing_character_count'],flush=True)
    return row

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reuse-before',help='Optional prior probe report containing unchanged source-before fixtures; hashes are checked before reuse.')
    args=parser.parse_args()
    candidates=[];jobs=[];prior=[]
    if args.reuse_before:
        prior=[r for r in json.loads(Path(args.reuse_before).read_text())['forms'] if r['variant']=='before']
        assert len(prior)==6
        for r in prior:
            assert sha(ROOT/r['pdf'])==r['pdf_sha256'] and sha(ROOT/r['image'])==r['image_sha256']
    for language in ('fr','en'):
        package='LM_C4-058-076'
        path=ROOT/'sources'/('fr/texts' if language=='fr' else 'en/packages')/(package+('_en' if language=='en' else '')+'.tex')
        source=path.read_text();start=source.index(r'\((144)\)');end=source.index(r'\end{tikzcd}}',start)+len(r'\end{tikzcd}}')
        old=source[start:end]
        old_option=r'"\bigl("{description,pos=0,anchor=east}'
        new_option=r'"\bigl("{description,pos=0,anchor=east,inner xsep=.3pt,outer sep=0pt}'
        assert old.count(old_option)==1
        new=old.replace(old_option,new_option)
        candidates.append({'id':'140-4-75-E144','language':language,'package':package,'cote':'140-4','scan':75,'tag':'144',
                           'source_path':rel(path),'source_sha256':sha(path),'source_line':source[:start].count('\n')+1,
                           'source_offset_start':start,'source_offset_end':end,'source_byte_start':len(source[:start].encode()),
                           'source_byte_end':len(source[:end].encode()),'old':old,'new':new,'expected_match_count':1,
                           'only_layout_option_changed':{'old':old_option,'new':new_option},
                           'kind':'local arrow annotation placement','reason':'Reduce only the existing opening-parenthesis annotation horizontal padding to .3pt and outer separation to0, keeping its east anchor at the start of the arrow. Its opaque description box then fits in the existing arrow gap without masking the preceding Z object or leaving an isolated shaft fragment. Preserve both parentheses, every mathematical token and uncertainty wrapper, both matrix rows, arrow endpoints and all node positions.'})
        for form in (0,1,2):
            for variant,text in (('before',old),('after',new)):
                if variant=='before' and prior: continue
                compile_text,mechanical=mechanical_repairs.repair('\\scanpage{75}\n'+text+'\n',package,language)
                body,_,_=editorial.annotate(compile_text,package,language)
                tex=OUT/f'scan75_diagram144_padding_{language}_{form}_{variant}.tex'
                tex.write_text(build_readers.preamble(language,form)+'\n'+r'\begin{document}\LMcote{140-4}'+'\n'+body+'\n'+r'\end{document}')
                jobs.append((language,form,variant,tex))
    (OUT/'scan75_diagram144_candidate.json').write_text(json.dumps(candidates,ensure_ascii=False,indent=2)+'\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor: rows=prior+list(executor.map(run,jobs))
    comparisons=[]
    for language in ('fr','en'):
        for form in (0,1,2):
            b=next(r for r in rows if (r['language'],r['form'],r['variant'])==(language,form,'before'))
            a=next(r for r in rows if (r['language'],r['form'],r['variant'])==(language,form,'after'))
            comparisons.append({'language':language,'form':form,'ink_width_delta':a['ink_width']-b['ink_width'],'ink_height_delta':a['ink_height']-b['ink_height']})
    report={'status':'PENDING_ACTUAL_VISUAL_REVIEW','forms':rows,'comparisons':comparisons,'before_evidence':'work/data/scan75_diagram144_mask_before.json',
            'candidate_file':'work/layout_probes/scan75_diagram144_candidate.json','source_files_unchanged':all(sha(ROOT/r['source_path'])==r['source_sha256'] for r in candidates),
            'shared_repair_module_modified':False,'observations_generated_by_script':False}
    (OUT/'scan75_diagram144_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__': main()
