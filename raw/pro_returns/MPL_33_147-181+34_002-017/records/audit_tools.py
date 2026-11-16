from pathlib import Path
import sys,csv
sys.path.insert(0,str(Path(__file__).parent))
from workflow import ROOT,PREFIX,FIELDS,utc

def page(cote,scan):
    return ROOT/'pages'/f'{PREFIX}_{cote}_scan{scan:03d}.tex'
def revise(cote,scan,old,new):
    p=page(cote,scan);t=p.read_text();assert old in t,(cote,scan,old);p.write_text(t.replace(old,new))
def add_element(cote,scan,kind,position,words,sheet_kind='text'):
    p=ROOT/f'{PREFIX}_inventory.csv'
    rows=list(csv.DictReader(p.open()))
    n=sum(r['cote']==str(cote) and int(r['scan'])==scan for r in rows)+1
    with p.open('a',newline='') as f:csv.writer(f).writerow([cote,f'{scan:03d}',sheet_kind,f'{cote}-{scan:03d}-{n:02d}',kind,position,words,'yes'])
def audit(cote,scan,note):
    with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03d} audited {utc()} [cote {cote}]\n')
    with (ROOT/'records/audit_observations.md').open('a') as f:f.write(f'\n## {cote}/{scan:03d}\n\n{note}\n')
