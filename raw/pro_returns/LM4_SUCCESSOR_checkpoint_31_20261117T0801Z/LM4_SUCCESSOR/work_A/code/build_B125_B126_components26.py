#!/usr/bin/env python3
"""Reproducible isolated component QA using the retained clean map environment."""
from pathlib import Path
import json, os, shutil, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
number=sys.argv[1];stage=sys.argv[2] if len(sys.argv)>2 else 'initial'
name={'B125':'ordinary_star_single_cross','B126':'final_prefix_axes'}[number]
qa=ROOT/'work_A'/f'{number}_QA';qa.mkdir(exist_ok=True)
wrapper=(ROOT/'work_A/qa_templates/component_article.tex').read_text().replace('B102',number)
wrapper=wrapper.replace('\\bibliographystyle{plainnat}\n','').replace(f'\\bibliography{{{number}_reference}}\n','')
(qa/f'{number}_qa.tex').write_text(wrapper)
shutil.copy2(ROOT/'work_A'/f'{number}_{name}_proposed.tex',qa/f'{number}.tex')
env=os.environ.copy();env.update(json.loads((ROOT/'records/checkpoint25_tex_env.json').read_text()))
for n in range(3):
    out=ROOT/'work_A'/f'{number}_component_{stage}_pass{n}.out'
    with out.open('wb') as f:
        p=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',f'{number}_qa.tex'],cwd=qa,env=env,stdout=f,stderr=subprocess.STDOUT)
    print(f'{number} pass{n}: exit{p.returncode}; {out.relative_to(ROOT)}',flush=True)
    if p.returncode:raise SystemExit(p.returncode)
shutil.copy2(qa/f'{number}_qa.pdf',ROOT/'work_A'/f'{number}_component.pdf')
subprocess.run(['pdftoppm','-r','100','-png',str(qa/f'{number}_qa.pdf'),str(qa/'page')],check=True)
print(f'PASS {number}: PDF, reusable wrapper, logs, source and all page images retained in {qa.relative_to(ROOT)}',flush=True)
