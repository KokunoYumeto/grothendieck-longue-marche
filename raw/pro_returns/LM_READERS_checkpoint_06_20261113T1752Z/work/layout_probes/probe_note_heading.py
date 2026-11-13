"""Stress the real three orphan-note starts and a breakable long note."""
from pathlib import Path
import json, sys, subprocess
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers, editorial, mechanical_repairs, layout_repairs
from texenv import environment
out=Path('work/layout_probes')
cases=[('LM_P050',492,'582'),('LM_P051',508,'599'),('LM_P066',73,'725'),('LM_C3-416-434',416,'1108')]
notes=[]
for package,scan,ref in cases:
    text=build_readers.raw_package(package,'fr')
    text,_=mechanical_repairs.repair(text,package,'fr')
    text,_=layout_repairs.repair(text,package,'fr')
    marks=list(editorial.spans(text,{'margin','scanpage'}));current=None
    for m in marks:
        if m['name']=='scanpage':current=int(m['argument'])
        elif current==scan and m['argument'].startswith(('\\diagram{','\\figure{')):
            notes.append((package,scan,ref,m['argument']));break
    else:raise AssertionError((package,scan))
pre=build_readers.preamble('fr',0)
new=r'\parindent=0pt\@beginparpenalty=10000\relax'+'\n '+r'\noindent'
assert pre.count(new)==1
oldpre=pre.replace(new,r'\parindent=0pt\noindent')
for label,preamble in [('before',oldpre),('after',pre)]:
    body=r'\begin{document}\LMcote{140-2}'+'\n'
    for package,scan,ref,note in notes:
        body+=r'\clearpage\noindent Probe '+ref+r' preceding material.\par'+'\n'
        body+='\n'.join(r'\noindent Ordinary preceding paragraph line '+str(i)+r'.\par' for i in range(1,44))+'\n'
        body+=r'\LMinblock{\textsuperscript{m'+ref+'} '+note+'}\n'
        body+=r'\noindent End of probe '+ref+r'.\par'+'\n'
    body+=r'\clearpage\noindent Long note must span pages.\par'+'\n'
    body+=r'\LMinblock{\textsuperscript{mLONG} '
    body+='\n'.join('Paragraph '+str(i)+r'. This is a deliberately long marginal note. Its prose must remain breakable across pages, while the heading stays attached to its first line.\par' for i in range(1,101))
    body+='}\n'+r'\end{document}'+'\n'
    p=out/('note_heading_'+label+'.tex');p.write_text(preamble+'\n'+body)
    r=subprocess.run(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',p.name],cwd=out,env=environment(),capture_output=True,text=True)
    (out/('note_heading_'+label+'.console.txt')).write_text(r.stdout)
    print(label,r.returncode,'overfull',r.stdout.count('Overfull'),'missing',r.stdout.count('Missing character'),flush=True)
    if r.returncode:raise SystemExit(r.returncode)
    import fitz
    pdf=fitz.open(p.with_suffix('.pdf'));proof=[]
    for i,pg in enumerate(pdf):
        t=pg.get_text()
        proof.append({'page':i+1,'text':t})
        if i<8:pg.get_pixmap(matrix=fitz.Matrix(1.3,1.3),alpha=False).save(out/('note_heading_'+label+'_'+str(i+1)+'.png'))
    (out/('note_heading_'+label+'.json')).write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
    print(label,'pages',len(pdf),flush=True)
