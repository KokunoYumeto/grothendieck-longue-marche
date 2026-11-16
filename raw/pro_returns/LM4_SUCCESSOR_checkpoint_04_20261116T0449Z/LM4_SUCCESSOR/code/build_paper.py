"""Build with installed LuaLaTeX, or --env pointing to a private TeX environment JSON."""
import argparse,json,os,subprocess,re
from pathlib import Path
p=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('--env');o=a.parse_args()
env=os.environ.copy()
if o.env:env.update(json.loads(Path(o.env).read_text()))
subprocess.run(['python3','code/assemble_register.py'],cwd=p,check=True)
# A stale bibliography can contain an error corrected in the current source.
# Regenerate it after the first pass instead of reading that stale version.
(p/'LM4_SUCCESSOR_paper.bbl').unlink(missing_ok=True)
for i,cmd in enumerate([['lualatex','-interaction=nonstopmode','-halt-on-error','LM4_SUCCESSOR_paper.tex'],['bibtex','LM4_SUCCESSOR_paper'],['lualatex','-interaction=nonstopmode','-halt-on-error','LM4_SUCCESSOR_paper.tex'],['lualatex','-interaction=nonstopmode','-halt-on-error','LM4_SUCCESSOR_paper.tex']]):
 r=subprocess.run(cmd,cwd=p,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 (p/'records'/f'build_{i}.log').write_text(r.stdout)
 if r.returncode:raise SystemExit(r.stdout[-3000:])
s=(p/'LM4_SUCCESSOR_paper.log').read_text();bad=[float(x) for x in re.findall(r'Overfull \\hbox \((\d+\.?\d*)pt',s) if float(x)>2]
assert not bad,bad
assert 'undefined' not in s,'Undefined references/citations in final log'
print('Build passes: no overflow greater than2pt and no undefined references. Render and visually inspect changed pages separately.')
