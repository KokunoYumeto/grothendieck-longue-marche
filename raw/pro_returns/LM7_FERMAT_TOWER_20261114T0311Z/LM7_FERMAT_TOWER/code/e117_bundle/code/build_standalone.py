"""Compile the actual E117 proof with the paper's LuaLaTeX typography."""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess

root=Path(__file__).resolve().parents[1]
workspace=root.parent
qa=root/'qa'
qa.mkdir(exist_ok=True)
paper=workspace/'LM7_FERMAT_TOWER'/'LM7_FERMAT_TOWER_paper.tex'
preamble=paper.read_text().split('\\begin{document}',1)[0]
tex=preamble+'\\begin{document}\n\\input{../sections/E_quartic_three.tex}\n\\bibliographystyle{plain}\n\\bibliography{E117_refs}\n\\end{document}\n'
(qa/'E117_check.tex').write_text(tex)
(qa/'E117_refs.bib').write_text((workspace/'LM7_FERMAT_TOWER'/'LM7_FERMAT_TOWER_references.bib').read_text()+'\n'+(root/'ledger'/'e_quartic_three_refs.bib').read_text())
runtime=workspace/'.lm7_tex_runtime'
dist=subprocess.check_output(['kpsewhich','-var-value=TEXMFDIST'],text=True).strip()
env=os.environ.copy()
env.update(TEXMF='{.,'+str(runtime)+',/usr/share/texmf,'+dist+'}',
           TEXMFVAR=str(runtime),TEXMFCONFIG=str(runtime),TEXFORMATS=str(runtime),
           TEXINPUTS=str(runtime)+'//:',TEXFONTMAPS=str(runtime)+':')
commands=[(['lualatex','--interaction=nonstopmode','--halt-on-error',
            '--fmt=lualatex_type1','E117_check.tex'],'E117_pass1.out'),
          (['bibtex','E117_check'],'E117_bibtex.out'),
          (['lualatex','--interaction=nonstopmode','--halt-on-error',
            '--fmt=lualatex_type1','E117_check.tex'],'E117_pass2.out'),
          (['lualatex','--interaction=nonstopmode','--halt-on-error',
            '--fmt=lualatex_type1','E117_check.tex'],'E117_pass3.out')]
actual=[]
for command,name in commands:
    with (qa/name).open('w') as output:
        result=subprocess.run(command,cwd=qa,env=env,stdout=output,stderr=subprocess.STDOUT)
    actual.append({'output':name,'actual_exit_code':result.returncode})
    print(name,'exit',result.returncode,flush=True)
    assert result.returncode==0,(name,result.returncode)
log=(qa/'E117_check.log').read_text(errors='replace')
bad=re.findall(r'^.*(?:Undefined control sequence|undefined citations|undefined references|Citation .* undefined|Reference .* undefined|Overfull \\[hv]box|Missing character:).*$',log,re.M)
result={'status':'PASS' if not bad else 'LAYOUT_REQUIRES_REPAIR','runs':actual,
        'issues':bad,'proof_sha256':hashlib.sha256((root/'sections'/'E_quartic_three.tex').read_bytes()).hexdigest(),
        'pdf_sha256':hashlib.sha256((qa/'E117_check.pdf').read_bytes()).hexdigest()}
(qa/'build_status.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
assert not bad,bad
