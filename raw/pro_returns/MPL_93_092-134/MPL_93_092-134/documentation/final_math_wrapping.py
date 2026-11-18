from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
fixes={
112:[(r'\deleted{\unsure{\varphi}}',r'\deleted{$\unsure{\varphi}$}')],
113:[(r'\deleted{\unsure{\longrightarrow}}',r'\deleted{$\unsure{\longrightarrow}$}'),(r'\deleted{\unsure{\triangle}}',r'\deleted{$\unsure{\triangle}$}')],
121:[(r'\deleted{\unsure{H\backslash}}',r'\deleted{$\unsure{H\backslash}$}')],
124:[(r'\deleted{\unsure{d_0=d_1=0}}',r'\deleted{$\unsure{d_0=d_1=0}$}')],
129:[(r'\deleted{\unsure{\mathbb R}\text{ les}}',r'\deleted{$\unsure{\mathbb R}\text{ les}$}')]
}
for n,pairs in fixes.items():
 p=root/'pages'/f'MPL_93_092-134_93_scan{n:03d}.tex'; s=p.read_text()
 for a,b in pairs:
  assert a in s,(n,a)
  s=s.replace(a,b)
 p.write_text(s)
with (root/'progress.log').open('a') as f:f.write('final mechanical math-delimiter repair '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'; six cancelled formula fragments wrapped; readings unchanged\n')
print('Six fragments wrapped.')
