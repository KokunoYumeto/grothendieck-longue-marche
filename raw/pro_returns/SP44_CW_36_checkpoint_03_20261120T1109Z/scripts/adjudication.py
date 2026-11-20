"""Small formatter for explicit main-reader choices; no automatic collation decisions."""
from pathlib import Path
from datetime import datetime,timezone
import json,copy
O=Path(__file__).resolve().parents[1]
VALID_TYPES={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found','refuted, with the refined statement\'s id'}

class Page:
    def __init__(self,n,brief='v02'):
        self.n=n;self.brief=brief
        self.R={r:json.loads((O/f'readers/scan{n:03d}/{r}/result.json').read_text()) for r in ('R1','R2','R3')}
        self.byid={x['id']:x for d in self.R.values() for x in d['differences']}
        self.folder='A36-01' if n<=18 else 'A36-02'
        self.filename=f'{self.folder}_36_scan{n:03d}.tex'
    def text(self,reader,replacements=()):
        s=(O/f'readers/scan{self.n:03d}/{reader}/reading.tex').read_text()
        for before,after in replacements:
            if before not in s:raise ValueError('Replacement not found: '+repr(before))
            s=s.replace(before,after)
        (O/'pages'/self.filename).write_text(s)
        return s
    def row(self,source,variants,**updates):
        x=copy.deepcopy(self.byid[source])
        r={k:x.get(k) for k in ('place','C','H','against_C','against_H','kind','marked_in_H','confidence','ink','evidence')}
        r['final']=x['reading']
        r['readers']=[self.byid[v]['reading'] if isinstance(v,str) and v in self.byid else v for v in variants]
        if len(r['readers'])!=3:raise ValueError('Three reader variants required')
        r['decision']='Main reader compared the three returns and inspected the cited crop.'
        r.update(updates);return r
    def inventory(self,reader,changes=None,extras=()):
        inv=copy.deepcopy(self.R[reader]['inventory'])
        for x in inv:
            if changes and x['element'] in changes:x.update(changes[x['element']])
        inv.extend(copy.deepcopy(extras))
        return inv
    def checks(self,include_readers=True):
        result=[]
        if not include_readers:return result
        for rr,d in self.R.items():
            for ev in d.get('check_events',[]):
                ev=copy.deepcopy(ev)
                if ev['type'] not in VALID_TYPES:raise ValueError('Classify actual check explicitly: '+str(ev))
                ev['who']=f'GPT-6 Astra Pro (inherited model); effort not exposed; {rr}, scan{self.n:03d} independent run'
                ev['statement_id']=ev['statement_id']+'-'+rr
                result.append(ev)
        return result
    def write(self,rows,inventory,unresolved,notation,notes,views,**kwargs):
        d=dict(scan=self.n,folder=self.folder,filename=self.filename,brief=self.brief,decided_utc='',rows=rows,inventory=inventory,unresolved=unresolved,notation=notation,notes=notes)
        d.update(kwargs)
        (O/f'decisions/scan{self.n:03d}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
        (O/f'decisions/scan{self.n:03d}_main_views.json').write_text(json.dumps(dict(scan=self.n,viewed_once=views),ensure_ascii=False,indent=2)+'\n')
        print('Explicit decision file written:',self.n,'rows',len(rows))
