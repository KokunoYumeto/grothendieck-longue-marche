"""Root's pre-context notation/syntax pass; never run after freezing."""
from pathlib import Path
import re,csv
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
assert 'transcription frozen' not in (ROOT/'progress.log').read_text()

def group(s,start):
    assert s[start]=='{'
    depth=1;i=start+1
    while i<len(s):
        if s[i]=='\\':
            m=re.match(r'\\(?:[A-Za-z]+|.)',s[i:]); i+=len(m.group()); continue
        if s[i]=='{':depth+=1
        elif s[i]=='}':
            depth-=1
            if not depth:return s[start+1:i],i+1
        i+=1
    raise ValueError('Unclosed group')

changes=[]
for p in sorted((ROOT/'pages').glob('*.tex')):
    scan=int(re.search(r'scan(\d+)',p.name).group(1));s=p.read_text();old=s
    # The first scan alone carries the cote marker.
    if scan!=78:s=s.replace(r'\cotefile{64}','')
    s=re.sub(r'% [Aa]rchive foliation: (\d+)\.?',r'% archive foliation: \1',s)
    # Macro arguments are braced for the supplied editorial interface.
    s=re.sub(r'\\unsure\s+([A-Za-z0-9])',lambda m:r'\unsure{'+m[1]+'}',s)
    out=[];last=0
    for m in list(re.finditer(r'\\margin\s*\{',s)):
        if m.start()<last:continue
        a,end=group(s,s.index('{',m.start()));j=end
        while j<len(s) and s[j].isspace():j+=1
        if j<len(s) and s[j]=='{' and not any(c in a for c in '$\\{}'):
            b,end2=group(s,j)
            out.append(s[last:m.start()]);out.append('% margin position: '+a+'\n'+r'\margin{'+b+'}')
            last=end2
    if out:s=''.join(out)+s[last:]
    # The repeated group-scheme mu has a visibly doubled initial stem.
    # Bold is the closest standard-LaTeX alphabet, explicitly marked as doubtful.
    if 81<=scan<=96:
        s=re.sub(r'\\mu(?![A-Za-z])',lambda m:r'\unsure{\boldsymbol{\mu}|\mu}',s)
    elif scan==80:
        k=s.index('Je reviens')
        s=s[:k]+re.sub(r'\\mu(?![A-Za-z])',lambda m:r'\unsure{\boldsymbol{\mu}|\mu}',s[k:])
    elif scan==97:
        s=s.replace(r'\mu_4^*=\mu_4^*(k)',r'\mu_4^*=\unsure{\boldsymbol{\mu}|\mu}_4^*(k)')
    # The same principal-part epsilon in section IV, checked against 102,105,106,115.
    if 102<=scan<=115:s=s.replace(r'\epsilon',r'\varepsilon')
    if s!=old:
        p.write_text(s);changes.append(scan)
combined=''.join(p.read_text()+'\n' for p in sorted((ROOT/'pages').glob('*.tex')))
(ROOT/'MPL_64_078-115_transcription.tex').write_text(combined)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:
    f.write(f'notation comparison completed {now}: recurring mu/omega/O, permutation glyph, twist superscript, T/D alphabets, dual accents, primes, epsilon and torsion/root labels compared across the scans; explicit alphabet doubts retained.\n')
    f.write(f'pre-freeze syntax pass {now}: one-argument margin macros, only first cotefile, braced unsure arguments, archive foliation comments; scans touched {changes}.\n')
print('Combined 38 pages; touched',changes)
