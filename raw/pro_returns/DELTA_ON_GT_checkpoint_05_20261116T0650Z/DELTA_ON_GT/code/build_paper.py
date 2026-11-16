"""Reproducible LuaLaTeX/BibTeX build with preserved pass logs and overflow audit.

Use a working TeX Live installation. In this workspace the missing Lua package
and format were supplied in ../runtime_tex; --runtime-dir overrides that path.
Third-party runtime binaries are not redistributed with the research package.
"""
from pathlib import Path
import argparse,datetime,json,os,re,shutil,subprocess
p=argparse.ArgumentParser()
p.add_argument('--tag',default=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
p.add_argument('--runtime-dir',type=Path)
a=p.parse_args()
root=Path(__file__).resolve().parents[1]
dest=root/'records'/('build_'+a.tag)
dest.mkdir(parents=True,exist_ok=False)
env=os.environ.copy()
runtime=a.runtime_dir or root.parent/'runtime_tex'
cmd=['lualatex','-interaction=nonstopmode','-halt-on-error']
if (runtime/'lualatex.fmt').exists():
    env['TEXMFHOME']=str(runtime/'local/usr/share/texlive/texmf-dist')
    cmd.insert(1,'--fmt='+str(runtime/'lualatex.fmt'))
cmd.append('DELTA_ON_GT_paper.tex')
results=[]
def run(argv,name):
    r=subprocess.run(argv,cwd=root,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (dest/(name+'.stdout')).write_text(r.stdout)
    if name.startswith('latex') and (root/'DELTA_ON_GT_paper.log').exists():
        shutil.copy2(root/'DELTA_ON_GT_paper.log',dest/(name+'.log'))
    results.append({'name':name,'argv':argv,'returncode':r.returncode})
    if r.returncode:
        print(r.stdout[-8000:])
        (dest/'commands.json').write_text(json.dumps(results,indent=2)+'\n')
        raise SystemExit(r.returncode)
run(cmd,'latex1')
run(['bibtex','DELTA_ON_GT_paper'],'bibtex')
run(cmd,'latex2')
run(cmd,'latex3')
log=(root/'DELTA_ON_GT_paper.log').read_text(errors='replace')
over=[{'points':float(m.group(1)),'context':log[max(0,m.start()-80):m.end()+180]}
      for m in re.finditer(r'Overfull \\[hv]box \(([0-9.]+)pt too (?:wide|high)\)',log)]
warnings=[line for line in log.splitlines() if 'Warning:' in line or 'Missing character:' in line]
result={'tag':a.tag,'commands':results,'overfull':over,'overfull_above_2pt':sum(x['points']>2 for x in over),'warnings':warnings}
(dest/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'records/latest_build.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'tag':a.tag,'overfull_above_2pt':result['overfull_above_2pt'],'overfull_total':len(over),'warnings':warnings},indent=2))
if result['overfull_above_2pt'] or any('undefined' in w.lower() or 'Missing character' in w for w in warnings):
    raise SystemExit(2)
