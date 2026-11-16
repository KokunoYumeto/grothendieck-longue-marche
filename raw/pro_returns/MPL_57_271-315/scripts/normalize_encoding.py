"""One-time, pre-freeze typesetting normalization; no inferred manuscript changes."""
from pathlib import Path
import re,json,subprocess
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent.parent

def argument(s,i):
    while i<len(s) and s[i].isspace():i+=1
    if s[i]=='{':
        start=i+1;depth=1;i+=1
        while i<len(s):
            if s[i]=='\\':
                i+=2;continue
            if s[i]=='{':depth+=1
            if s[i]=='}':
                depth-=1
                if not depth:return s[start:i],i+1
            i+=1
        raise ValueError('unbalanced argument')
    if s[i]=='\\':
        m=re.match(r'\\(?:[A-Za-z]+|.)',s[i:]);return m.group(),i+len(m.group())
    return s[i],i+1

def normalize(s):
    out=[];i=0
    while i<len(s):
        if s[i]=='\\':
            m=re.match(r'\\(?:[A-Za-z]+|.)',s[i:])
            cmd=m.group();i+=len(cmd)
            if cmd=='\\underline':
                body,i=argument(s,i);body=normalize(body)
                if body.startswith('\\uline{'):
                    inner,end=argument(body,6)
                    if end==len(body):out.append('\\uuline{'+inner+'}');continue
                out.append('\\uline{'+body+'}')
            else:out.append(cmd)
        else:out.append(s[i]);i+=1
    return ''.join(out)

def run():
    changed=[]
    for p in sorted((ROOT/'records').glob('scan*.json')):
        d=json.loads(p.read_text());old=d['tex'];t=normalize(old)
        t=t.replace(r'\operatorname{Nér}',r'\operatorname{N\acute{e}r}').replace(r'\mathrm{Néron}',r'\mathrm{N\acute{e}ron}')
        if d['scan']==312:
            t=t.replace("\\uline{de} $A'\\otimes_A G$ \\uline{et}","\\uline{de} $A'\\otimes_A \\uline{G}$ \\uline{et}")
        # Lower manuscript foliation follows all additional graphical marks.
        folio='\\mspage{'+str(d['scan']-1)+'}'
        if folio in t:
            a,b=t.rsplit(folio,1)
            if b.strip():t=a.rstrip()+'\n'+b.strip()+'\n'+folio+'\n'
        if t!=old:
            d['tex']=t;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
            subprocess.run(['python3',str(ROOT/'scripts/manage.py'),'save','--input',str(p)],check=True,stdout=subprocess.DEVNULL)
            changed.append(d['scan'])
    with (ROOT/'progress.log').open('a') as f:
        f.write('encoding consistency pass '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'; required uline/uuline macros, mathematical accented e, lower foliation order; scans '+','.join(map(str,changed))+'\n')
    print({'changed':changed})
if __name__=='__main__':run()
