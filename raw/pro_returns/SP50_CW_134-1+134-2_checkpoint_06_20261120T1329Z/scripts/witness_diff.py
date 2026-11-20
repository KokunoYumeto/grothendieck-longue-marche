"""Mechanical comparison aid for an already-read page. No reading decision is automated."""
from pathlib import Path
import re,argparse,difflib,json
O=Path(__file__).resolve().parents[1];R=O.parent
p=argparse.ArgumentParser();p.add_argument('key');a=p.parse_args()
row=next(p for p in json.loads((O/'page_order.json').read_text()) if f"{p['cote']}_scan{int(p['our_scan']):03d}"==a.key)
packet=Path(row['packet'])
def remove_commands(s,names):
    for name in names:
        pattern=re.compile(r'\\'+name+r'\*?(?:\[[^\]]*\])?\{')
        while (m:=pattern.search(s)):
            depth=1;i=m.end()
            while i<len(s) and depth:
                if s[i]=='{' and s[i-1]!='\\':depth+=1
                elif s[i]=='}' and s[i-1]!='\\':depth-=1
                i+=1
            s=s[:m.start()]+' '+s[i:]
    return s
def normalize(s):
    s=re.sub(r'(?<!\\)%[^\n]*','',s)
    s=remove_commands(s,['note','page','scanpage','cotefile','mspage','section'])
    for old,new in [('uncertain','unsure'),('struck','deleted'),('add','inserted'),('marginal','margin'),('emph','uline')]:
        s=re.sub(r'\\'+old+r'(?![A-Za-z])',lambda m:'\\'+new,s)
    s=re.sub(r'\\(?:noindent|hfill|quad|qquad)\b',' ',s)
    s=re.sub(r'\\(?:,|;|!| |\[|\]|\\)',' ',s)
    s=s.replace('~',' ').replace('$','')
    s=re.sub(r'\s+',' ',s).strip()
    return re.findall(r'\\[A-Za-z]+|[\wÀ-ÿ]+|[^\w\s]',s)
f=(O/'pages'/Path(row['codex_file']).name).read_text()
out=['Mechanical comparison aid. Syntax, display layout and equivalent mathematical encodings can produce false differences. Only the recorded ink decisions are authoritative.\n']
for w in ['C','H']:
    if w=='H' and row['hua_has']!='text':continue
    old=normalize((packet/(w+'.tex')).read_text());new=normalize(f)
    sm=difflib.SequenceMatcher(None,old,new,autojunk=False)
    out.append('\n'+w+' -> consolidated\n')
    for tag,i,j,k,l in sm.get_opcodes():
        if tag=='equal':continue
        out.append(f'{tag}: context '+ ' '.join(old[max(0,i-5):i])+'\n W: '+' '.join(old[i:j])+'\n F: '+' '.join(new[k:l])+'\n')
dest=O/'decisions'/(a.key+'_mechanical_diff.txt');dest.write_text('\n'.join(out));print(dest.read_text())
