from pathlib import Path
import json,sys
from save_page import ROOT,PREFIX,refresh,utc

def audited(n,note):
 p=ROOT/'records'/f'scan{n:03d}.json'
 d=json.loads(p.read_text())
 d['text']=(ROOT/'pages'/f'{PREFIX}_121_scan{n:03d}.tex').read_text()
 d['second_pass_audit']={'utc':utc(),'reader':'root','note':note}
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 refresh()
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {n:03d} audited {utc()}\n')
 print(f'Audited {n:03d}')
if __name__=='__main__':audited(int(sys.argv[1]),sys.argv[2])
