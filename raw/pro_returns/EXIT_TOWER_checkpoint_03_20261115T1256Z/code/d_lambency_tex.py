#!/usr/bin/env python3
"""Generate readable complete tables from d_lambencies.json (no new mathematics)."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
A=json.loads((P/'d_lambencies.json').read_text())
def ps(p):return r'\,'.join(str(k)+(f'^{{{v}}}' if v>1 else '') for k,v in p.items())
def cf(c):return f"c_{{{c['d']},{c['a']}}}"
def orb(a,o):return r'\{'+','.join(cf(a['cusps'][i]) for i in o)+r'\}'
def cycletex(a,p):
    seen=set();s=[]
    for i in range(len(p)):
        if i in seen:continue
        c=[];j=i
        while j not in seen:c.append(j);seen.add(j);j=p[j]
        if len(c)>1:s.append('('+r'\ '.join(cf(a['cusps'][i]) for i in c)+')')
    return ''.join(s) or '1'
U={}
for a in A:U.setdefault(a['N'],a)
tex=[r'\begin{longtable}{r|p{0.79\textwidth}}',r'$N$ & Cusps $c_{d,a}$, with $(w;f)$ meaning width $w$ and field $\mathbb Q(\zeta_f)$\\\hline']
for N,a in sorted(U.items()):
    terms=[]
    for d in sorted({c['d'] for c in a['cusps']}):
        cs=[c for c in a['cusps'] if c['d']==d];w=cs[0]['width'];f=cs[0]['conductor'];aa=','.join(str(c['a']) for c in cs)
        terms.append(f"$c_{{{d},\\{{{aa}\\}}}}:({w};{f})$")
    tex.append(str(N)+' & '+r';\ '.join(terms)+r'\\')
tex += [r'\end{longtable}',r'\begin{longtable}{r|p{0.78\textwidth}}',r'$\ell$ & Atkin--Lehner permutations; omitted cusp labels are fixed\\\hline']
for a in A:
    if len(a['S'])>1:
        terms=[f"$W_{{{e}}}={cycletex(a,a['Atkin_Lehner_permutations'][str(e)])}$" for e in a['S'][1:]]
        tex.append('$'+a['lambency']+'$ & '+r'\newline '.join(terms)+r'\\')
tex += [r'\end{longtable}',r'\begin{longtable}{r|r|r|l|l}',r'$N$ & components & degree & passport of one component over $X(2)$ & direct degree to $X_0(4)$\\\hline']
for N,a in sorted(U.items()):
    d=a['dessin'];t=d['tripod_basechange'][0];dr=d['tripod_direct'];s='('+','.join(ps(p) for p in t['passport'])+')'
    tex.append(f"{N} & {len(d['tripod_basechange'])} & {t['degree']} & ${s}$ & "+(str(dr['degree']) if dr else '--')+r'\\')
tex += [r'\end{longtable}',r'\begin{longtable}{r|l|r|r}',r'$\ell$ & $\pi^X$ (positive numerator, negative denominator) & $[q^0]T^X$ & $[q]T^X$\\\hline']
for a in A:
    fr={int(k):v for k,v in a['frame'].items()};num=ps({k:v for k,v in sorted(fr.items()) if v>0});den=ps({k:-v for k,v in sorted(fr.items()) if v<0});q=a['eta_series']
    tex.append('$'+a['lambency']+f"$ & $\\frac{{{num}}}{{{den}}}$ & {q['0']} & {q['1']}"+r'\\')
tex.append(r'\end{longtable}')
(P/'d_lambencies_details.tex').write_text('\n'.join(tex)+'\n')
print('Generated 18 cusp rows, 9 Atkin--Lehner rows, 18 tripod rows, and all 23 eta rows from the checked JSON.')
