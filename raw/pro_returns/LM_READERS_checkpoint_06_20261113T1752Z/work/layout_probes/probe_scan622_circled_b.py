from pathlib import Path
import sys,json,subprocess,hashlib
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial,fitz
from texenv import environment
D=Path('work/layout_probes');records=[];jobs=[]
for lang in ['fr','en']:
 pkg='LM_C3-606-624';variants=[]
 for mech in [False,True]:
  txt=build_readers.raw_package(pkg,lang)
  if mech:txt,_=mechanical_repairs.repair(txt,pkg,lang)
  txt=layout_repairs.repair(txt,pkg,lang,include_pagination=False)[0]
  start=txt.index(r'\textcircled{b}');end=txt.index(r'\]',start)+2;old=txt[start:end]
  assert old.count(r'\margin')==1 and '(6)' in old
  new=r'\Needspace{8\baselineskip}'+'\n'+r'\begin{samepage}'+'\n'+old+'\n'+r'\end{samepage}'
  if not any(v['old']==old for v in variants):variants.append(dict(old=old,new=new))
  if mech:before=old;after=new
 records.append(dict(id='140-3-622-Kb',language=lang,package=pkg,scan=622,tag='b',kind='section-heading pagination',source_pattern='Visually confirmed circled-b subsection with only On a/We have at the foot, immediately before its first definition6',reason='Keep the unchanged circled-b label, introductory words, slash marginal mark and complete first definition6 together with a local eight-baseline reservation and samepage group; preserve all mathematical/editorial content.',variants=variants))
 for form in [0,1,2]:
  parts=[build_readers.preamble(lang,form),r'\begin{document}\LMcote{140-3}']
  for label,frag in [('BEFORE',before),('AFTER',after)]:
   body,_,_=editorial.annotate(r'\scanpage{622}'+frag,pkg,lang)
   parts += [r'\clearpage\noindent '+label+r' constrained-foot probe.',r'\par\vspace*{\dimexpr\textheight-70pt\relax}\par\penalty0',body]
  parts+=[r'\end{document}'];target=D/f'scan622_circled_b_{lang}_{form}.tex';target.write_text('\n'.join(parts))
  jobs.append((lang,form,target,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=D,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
(D/'scan622_circled_b_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
results=[]
for lang,form,target,job in jobs:
 stdout,_=job.communicate();target.with_suffix('.console.txt').write_text(stdout);log=target.with_suffix('.log').read_text(errors='replace');counts=dict(exit=job.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character'))
 if job.returncode:print(stdout[-2000:]);raise SystemExit(job.returncode)
 pdf=fitz.open(target.with_suffix('.pdf'));tags=[]
 for i,p in enumerate(pdf):
  if '(6)' in p.get_text():
   out=D/f'scan622_circled_b_{lang}_{form}_p{i+1}.png';p.get_pixmap(matrix=fitz.Matrix(1.8,1.8)).save(out)
   tags.append(dict(page=i+1,image=str(out),image_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),text=p.get_text()))
 results.append(dict(language=lang,form=form,compile=counts,pdf=str(target.with_suffix('.pdf')),pdf_sha256=hashlib.sha256(target.with_suffix('.pdf').read_bytes()).hexdigest(),pages=len(pdf),definition_pages=tags,status='PENDING_ACTUAL_VISUAL'))
 print(lang,form,counts,len(pdf),'definition pages',[t['page'] for t in tags],flush=True)
(D/'scan622_circled_b_validation.json').write_text(json.dumps(dict(status='PENDING_ACTUAL_VISUAL',forms=results),ensure_ascii=False,indent=2)+'\n')
