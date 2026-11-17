#!/usr/bin/env python3
"""Retained isolated A87/A88 component build; no assembled source edits."""
from pathlib import Path
import os,sys,json,shutil,subprocess,hashlib,re

ROOT=Path(__file__).resolve().parents[2]
stage=sys.argv[1] if len(sys.argv)>1 else 'initial'
selected=sys.argv[2:] or ['A87','A88']
sources={'A87':'A87_marked_three_cycle_cusp_frame_proposed.tex',
         'A88':'A88_Alexander_dihedral_coefficient_proposed.tex'}
env=os.environ.copy()
env.update(json.loads((ROOT/'records/checkpoint25_tex_env.json').read_text()))
template=(ROOT/'work_A/qa_templates/component_article.tex').read_text()

for name in selected:
    qa=ROOT/'work_A'/f'{name}_QA'
    qa.mkdir(exist_ok=True)
    source=ROOT/'work_A'/sources[name]
    wrapper=template.replace('B102',name)
    if name=='A88':
        wrapper=wrapper.replace('\\bibliographystyle{plainnat}\n','').replace(f'\\bibliography{{{name}_reference}}\n','')
    else:
        shutil.copy2(ROOT/'work_A/A_references.bib',qa/f'{name}_reference.bib')
    (qa/f'{name}_qa.tex').write_text(wrapper)
    shutil.copy2(source,qa/f'{name}.tex')
    commands=[['lualatex','-interaction=nonstopmode','-halt-on-error',f'{name}_qa.tex']]
    if name=='A87': commands.append(['bibtex',f'{name}_qa'])
    commands.extend([['lualatex','-interaction=nonstopmode','-halt-on-error',f'{name}_qa.tex'] for _ in range(2)])
    for n,command in enumerate(commands):
        out=ROOT/'work_A'/f'{name}_component_{stage}_pass{n}.out'
        with out.open('wb') as f:
            result=subprocess.run(command,cwd=qa,env=env,stdout=f,stderr=subprocess.STDOUT)
        print(f'{name} {command[0]} pass{n}: exit {result.returncode}; {out.relative_to(ROOT)}',flush=True)
        if result.returncode: raise SystemExit(result.returncode)
    pdf=qa/f'{name}_qa.pdf'
    shutil.copy2(pdf,ROOT/'work_A'/f'{name}_component.pdf')
    subprocess.run(['pdftoppm','-r','100','-png',str(pdf),str(qa/'page')],check=True)
    (qa/'build_provenance.json').write_text(json.dumps({
        'stage':stage,'source':str(source.relative_to(ROOT)),
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'wrapper':f'{name}_qa.tex','clean_environment':'records/checkpoint25_tex_env.json',
        'clean_environment_sha256':hashlib.sha256((ROOT/'records/checkpoint25_tex_env.json').read_bytes()).hexdigest(),
        'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'visual_QA':'pending actual image inspection'},indent=2)+'\n')
    print(f'BUILT {name}: reusable source/wrapper/bibliography/logs/PDF and all page PNGs retained; visual QA pending.',flush=True)
