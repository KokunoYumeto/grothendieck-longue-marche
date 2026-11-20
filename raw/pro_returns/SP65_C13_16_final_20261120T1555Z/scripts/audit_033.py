"""Root reader's second-pass corrections on scan 033."""
import json
from record import ROOT,RECORDS,build
path=ROOT/'pages/16_scan033.tex';s=path.read_text()
a=r'\uline{Corollaire} $(A(X\times X)';b=r'\uline{Corollaire} $(A(X\mathrm{x}X)'
assert a in s;s=s.replace(a,b)
assert r'\qquadL_X' in s;s=s.replace(r'\qquadL_X',r'\qquad L_X')
path.write_text(s)
rp=RECORDS/'033.json';p=json.loads(rp.read_text())
p['changes'].append(dict(place='Typed corollary product',c=r'X\times X',h=r'X\times X',final=r'X\mathrm{x}X',ink='Second full-image reading: a lower-case serifed typewriter x stands at the text baseline between the two capitals. The handwritten products in the margin retain their drawn crossing sign.',dc=True,dh=True,confidence='high',kind='misread symbol or index',error=1,marked_h='no',consequence=''))
p['notation'].append(['Roman product x','Lower-case serifed typewriter x','033','Typed corollary; handwritten margin crossings remain as drawn'])
rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n');build()
