#!/usr/bin/env python3
"""Keep the unchanged C3:519 introduction79 with its immediate diagram80."""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import subprocess
import fitz
import build_readers
import editorial
from texenv import environment
from verify_pdf import parse_log

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'work/layout_probes'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p): return p.relative_to(ROOT).as_posix()

def run(job):
    language,tex=job
    p=subprocess.run(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',tex.name],cwd=OUT,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    tex.with_suffix('.console.txt').write_text(p.stdout);log=parse_log(tex.with_suffix('.log'))
    if p.returncode: raise RuntimeError('Tag79 probe failed: '+language)
    pdf=tex.with_suffix('.pdf');rows=[]
    with fitz.open(pdf) as doc:
        hits=[(page.number+1,box) for page in doc for box in page.search_for('(79)')]
        assert len(hits)==3
        for form,(physical,box) in enumerate(hits):
            page=doc[physical-1];native=OUT/f'scan519_tag79_{language}_{form}_native3x.png'
            page.get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(45,max(0,box.y0-25),page.rect.width,min(page.rect.height,box.y0+260)),alpha=False).save(native)
            rows.append({'language':language,'form':form,'pdf':rel(pdf),'pdf_sha256':sha(pdf),'pages':len(doc),'tag_page':physical,
                         'diagram80_on_tag_page':bool(page.search_for('(80)')),'image':rel(native),'image_sha256':sha(native),
                         'log':rel(tex.with_suffix('.log')),'log_sha256':sha(tex.with_suffix('.log')),'compile_exit_code':p.returncode,
                         'error_count':log['error_count'],'overfull_count':log['overfull_count'],'missing_character_count':log['missing_character_count'],
                         'status':'PENDING_ACTUAL_VISUAL_REVIEW'})
    print(language,'forms3','errors',log['error_count'],'overfull',log['overfull_count'],'missing',log['missing_character_count'],flush=True)
    return rows

def main():
    candidates=[];jobs=[]
    for language in ('fr','en'):
        package='LM_C3-511-529';path=ROOT/'sources'/('fr/texts' if language=='fr' else 'en/packages')/(package+('_en' if language=='en' else '')+'.tex')
        source=path.read_text();start=source.index('\n(79) ',source.index(r'\scanpage{519}'))+1
        diagram=source.index(r'\diagram{',start);end=editorial.brace_end(source,diagram+len(r'\diagram'))
        old=source[start:end];assert '(80)' in old
        new='\\begin{samepage}\n'+old+'\n\\end{samepage}'
        candidates.append({'id':'140-3-519-K79INTRO','language':language,'package':package,'cote':'140-3','scan':519,'tag':'79','associated_diagram_tag':'80',
                           'source_path':rel(path),'source_sha256':sha(path),'source_line':source[:start].count('\n')+1,
                           'source_offset_start':start,'source_offset_end':end,'source_byte_start':len(source[:start].encode()),'source_byte_end':len(source[:end].encode()),
                           'old':old,'new':new,'expected_match_count':1,'original_content_unchanged':True,'kind':'tagged introduction pagination',
                           'reason':'Keep the unchanged numbered introduction (79), ending in a commutativity-in phrase, with the immediately following complete commutative square (80). Only samepage break penalties are added; preserve every source word, mathematical token, uncertainty and cancellation wrapper, and both tags. The subsequent ellipsis and manuscript-page marker stay outside.'})
        body,_,_=editorial.annotate('\\scanpage{519}\n'+new+'\n',package,language)
        parts=[build_readers.preamble(language,0),r'\begin{document}\LMcote{140-3}']
        for form in (0,1,2):
            parts.extend([r'\clearpage',f'\\LMform={form}',r'\noindent Preceding body text.\par\vspace{\dimexpr\textheight-6\baselineskip\relax}',body])
        parts.append(r'\end{document}');tex=OUT/f'scan519_tag79_bound_{language}.tex';tex.write_text('\n'.join(parts));jobs.append((language,tex))
    (OUT/'scan519_tag79_candidate.json').write_text(json.dumps(candidates,ensure_ascii=False,indent=2)+'\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor: rows=[r for group in executor.map(run,jobs) for r in group]
    report={'status':'PENDING_ACTUAL_VISUAL_REVIEW','forms':rows,'before_evidence':'work/data/scan519_tag79_before.json','candidate_file':'work/layout_probes/scan519_tag79_candidate.json',
            'source_files_unchanged':all(sha(ROOT/r['source_path'])==r['source_sha256'] for r in candidates),'shared_repair_module_modified':False,'observations_generated_by_script':False}
    (OUT/'scan519_tag79_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':main()
