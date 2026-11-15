"""Search supplied textual context, retaining cote/scan and line anchors."""
from pathlib import Path
import re,json,argparse

BASE=Path(__file__).resolve().parents[2]
CTX=BASE/'context'

def scan_blocks():
    path=CTX/'MPL_16+47+54+44_transcription.tex'
    cote=None;scan=None;blocks=[];lines=[];start=1
    for n,line in enumerate(path.read_text().splitlines(),1):
        c=re.match(r'\\cotefile\{(\d+)\}',line)
        p=re.match(r'\\scanpage\{(\d+)\}',line)
        if c or p:
            if lines and scan is not None:blocks.append({'file':path.name,'cote':cote,'scan':scan,'start_line':start,'text':'\n'.join(lines)})
            lines=[];start=n
            if c:cote=int(c.group(1));scan=None
            if p:scan=int(p.group(1))
        lines.append(line)
    if scan is not None:blocks.append({'file':path.name,'cote':cote,'scan':scan,'start_line':start,'text':'\n'.join(lines)})
    return blocks

def search(pattern,cap=30):
    rx=re.compile(pattern,re.I)
    hits=[]
    for b in scan_blocks():
        matched=[{'line':b['start_line']+i,'text':line} for i,line in enumerate(b['text'].splitlines()) if rx.search(line)]
        if matched:hits.append({k:v for k,v in b.items() if k!='text'}|{'matches':matched})
    return {'pattern':pattern,'matching_scans':len(hits),'hits':hits[:cap]}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('pattern');p.add_argument('--cap',type=int,default=20);p.add_argument('--output')
    a=p.parse_args();r=search(a.pattern,a.cap)
    if a.output:Path(a.output).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(r,ensure_ascii=False,indent=2))
