"""Record-writing helpers. They do not read images or make transcription decisions."""
from pathlib import Path
import copy,json

OUT=Path(__file__).resolve().parents[1]

class PageDecision:
    def __init__(self,key,brief,base='r1'):
        self.key=key
        self.readers={r:json.loads((OUT/'readers'/key/r/'report.json').read_text()) for r in ('r1','r2','r3')}
        self.data=copy.deepcopy(self.readers[base])
        scan=key.rsplit('scan',1)[1]
        self.data.update(brief=brief,readers=[f'/root/s{scan}_{r}' for r in ('r1','r2','r3')])
        self.text=(OUT/'readers'/key/base/'reading.tex').read_text()

    def change(self,n,**fields):
        self.data['changes'][n-1].update(fields)

    def crop(self,relative):
        return f'evidence/{self.key}/{relative}'

    def add(self,entry):
        self.data['changes'].append(copy.deepcopy(entry))

    def save(self,main_viewed):
        """Call only after all three returns and every required crop are adjudicated."""
        d=self.data
        for n,x in enumerate(d['changes'],1):
            x['id']=f'{self.key}.{n:02d}'
            if isinstance(x.get('crop'),str):x['crop']=x['crop'].removeprefix('out/').replace('; out/', '; ')
        for x in d.get('doubts',[]):
            if isinstance(x.get('crop'),str):x['crop']=x['crop'].removeprefix('out/').replace('; out/', '; ')
        d['main_viewed']=list(dict.fromkeys(p.removeprefix('out/') for p in main_viewed))
        for p in d['main_viewed']:
            assert (OUT/p).is_file(),p
        d['adjudication_complete']=True
        for k in ('reader','page','started_utc','finished_utc','model','effort','view_log','coverage','notation'):
            d.pop(k,None)
        assert isinstance(d.get('notes'),str),'Main notes must be one Markdown string'
        page=next(p for p in json.loads((OUT/'page_order.json').read_text()) if f"{p['cote']}_scan{int(p['our_scan']):03d}"==self.key)
        target=OUT/'pages'/Path(page['codex_file']).name
        target.write_text(self.text)
        (OUT/'decisions'/f'{self.key}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
        print('Adjudicated',self.key,len(d['changes']),'reviewed loci;',len(d.get('doubts',[])),'doubts;',len(d['main_viewed']),'main crop views')

    def notation(self,rows):
        """Rows are literal Markdown; callers must escape internal table separators."""
        with (OUT/'notation.md').open('a') as f:
            for row in rows:f.write(row.rstrip()+'\n')

    def observation(self,text):
        with (OUT/'workflow_observations.md').open('a') as f:
            f.write(f'\n## {self.key}\n\n{text.strip()}\n')
