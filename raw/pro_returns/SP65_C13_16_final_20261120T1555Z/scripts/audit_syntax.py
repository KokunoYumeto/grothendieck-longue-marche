"""Syntax-only separation of control words found by a lexical scan; no TeX run."""
from record import ROOT,build
for n,a,b in [(38,r'\leqn+1',r'\leq n+1'),(42,r'\timesY',r'\times Y')]:
 p=ROOT/'pages'/f'16_scan{n:03}.tex';s=p.read_text();assert a in s;s=s.replace(a,b);p.write_text(s)
build()
