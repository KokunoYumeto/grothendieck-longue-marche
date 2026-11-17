#!/usr/bin/env python3
"""Isolated reproducible B131 QA; frozen source and external labels retained."""
from pathlib import Path
import hashlib,json,os,re,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[2]
stage=sys.argv[1] if len(sys.argv)>1 else 'initial'
qa=ROOT/'work_A/B131_QA';qa.mkdir(exist_ok=True)
source=ROOT/'work_A/B131_D_source_noncommutation_proposed.tex'
wrapper=(ROOT/'work_A/qa_templates/component_article.tex').read_text().replace('B102','B131')
wrapper=wrapper.replace('\\bibliographystyle{plainnat}\n','').replace('\\bibliography{B131_reference}\n','')
wrapper=wrapper.replace('\\usepackage{hyperref}','\\usepackage{xr-hyper}\n\\usepackage{hyperref}')
wrapper=wrapper.replace('\\begin{document}','\\externaldocument{B131_external_refs}[../../LM4_SUCCESSOR_paper.pdf]\n\\begin{document}')
(qa/'B131_qa.tex').write_text(wrapper)
shutil.copy2(source,qa/'B131.tex')
aux=ROOT/'LM4_SUCCESSOR_paper.aux'
labels=[line for line in aux.read_text().splitlines() if re.match(r'\\newlabel\{eq:B128-(?:head-table|retained-actions)\}',line)]
assert len(labels)==2
(qa/'B131_external_refs.aux').write_text('\n'.join(labels)+'\n')
(qa/'external_reference_provenance.json').write_text(json.dumps({'actual_aux':str(aux.relative_to(ROOT)),
 'aux_sha256':hashlib.sha256(aux.read_bytes()).hexdigest(),'retained_lines':labels,
 'scope':'Two exact external equation labels only; source bytes unchanged. Hyperlinks point to the actual parent PDF.'},indent=2)+'\n')
env=os.environ.copy();env.update(json.loads((ROOT/'records/checkpoint25_tex_env.json').read_text()))
for n in range(3):
    out=ROOT/'work_A'/f'B131_component_{stage}_pass{n}.out'
    with out.open('wb') as f:
        p=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','B131_qa.tex'],cwd=qa,env=env,stdout=f,stderr=subprocess.STDOUT)
    print(f'B131 pass{n}: exit{p.returncode}; {out.relative_to(ROOT)}',flush=True)
    if p.returncode:raise SystemExit(p.returncode)
shutil.copy2(qa/'B131_qa.pdf',ROOT/'work_A/B131_component.pdf')
subprocess.run(['pdftoppm','-r','100','-png',str(qa/'B131_qa.pdf'),str(qa/'page')],check=True)
print('PASS: B131 source, reusable wrapper, external labels/provenance, PDF, logs, and every page image retained.',flush=True)
