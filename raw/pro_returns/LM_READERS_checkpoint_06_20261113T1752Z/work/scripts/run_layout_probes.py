"""Compile the isolated measurement documents with standard or restored TeX Live."""
from pathlib import Path
import sys,subprocess,concurrent.futures
from texenv import environment,RUNTIME
ROOT=Path(__file__).resolve().parents[2]
D=ROOT/'work/layout_probes'
def run(name):
    cmd=['lualatex']
    if (RUNTIME/'formats/lualatex.fmt').exists():cmd+=['--fmt='+str(RUNTIME/'formats/lualatex.fmt')]
    cmd+=['--no-shell-escape','-interaction=nonstopmode','-halt-on-error',name+'.tex']
    with (D/(name+'.console.txt')).open('w') as f:
        p=subprocess.run(cmd,cwd=D,env=environment(),stdout=f,stderr=subprocess.STDOUT)
    print(name,p.returncode,flush=True)
    return p.returncode
if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        rs=list(ex.map(run,sys.argv[1:] or ['measure_en','measure_fr']))
    if any(rs):sys.exit(1)
