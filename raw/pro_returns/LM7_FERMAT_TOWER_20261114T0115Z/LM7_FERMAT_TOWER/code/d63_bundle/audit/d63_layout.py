from pathlib import Path
import os, subprocess, json, hashlib, re
import fitz
BASE=Path('/workspace/scratch/e34c61ec5a35');OWN=BASE/'D63_EXPERIMENTS';QA=OWN/'qa'
R=BASE/'.lm7_tex_runtime';env=os.environ.copy()
dist=subprocess.check_output(['kpsewhich','-var-value=TEXMFDIST'],text=True).strip()
env.update(TEXMF='{.,'+str(R)+',/usr/share/texmf,'+dist+'}',TEXMFVAR=str(R),TEXMFCONFIG=str(R),TEXFORMATS=str(R),TEXINPUTS=str(R)+'//:',TEXFONTMAPS=str(R)+':')
for i in (1,2):
 with (OWN/'audit'/f'd63_latex_pass{i}.out').open('w') as stream:
  p=subprocess.run(['lualatex','--fmt=lualatex_type1','--interaction=nonstopmode','--halt-on-error','d63_check.tex'],cwd=QA,env=env,stdout=stream,stderr=subprocess.STDOUT)
 assert p.returncode==0,i
log=(QA/'d63_check.log').read_text(errors='replace')
warnings=[x for x in log.splitlines() if any(w in x for w in ['Overfull','Underfull','Missing character','Undefined control sequence'])]
doc=fitz.open(QA/'d63_check.pdf');images=[]
for i,p in enumerate(doc):
 target=QA/f'd63_page_{i+1}.jpg';p.get_pixmap(dpi=110).save(target)
 images.append({'path':str(target),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
source=OWN/'sections/D_compact_orthogonal_cross.tex';text=source.read_text();tags=re.findall(r'\\tag\{([^}]+)\}',text)
assert len(tags)==len(set(tags))
assert not [ord(c) for c in text if ord(c)<32 and c not in '\n\t']
assert not re.search(r'(?<!\\)\b(?:qquad|quad)\b',text)
result={'compile_status':'PASS','page_count':len(doc),'warnings':warnings,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'pdf_sha256':hashlib.sha256((QA/'d63_check.pdf').read_bytes()).hexdigest(),'images':images,'unique_equation_tags':len(tags),'control_display_lint':'PASS','actual_visual_review':'pending'}
(OWN/'audit/d63_layout_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
