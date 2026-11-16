#!/usr/bin/env python3
"""Print and reparse the literal three anti-unit roots used in A175."""
from pathlib import Path
from fractions import Fraction as F
import json,re
base=Path(__file__).resolve().parent
data=json.loads((base/'two_inert_level2_anti_cube_root_certificate_data.json').read_text())
d=649;D=2*d**5;B=10**40
roots=[[F(x) for x in rr] for rr in data['roots']]
out=[r'\subsection*{Literal anti-unit roots used in A.175}',
     r'Put $d=649$, $B=10^{40}$ and $w^{18}=-3d^6$ as in A.175.4.',
     r'The following integers specify the three elements without root-choice ambiguity:',
     r'\[r_i=\frac1{2d^5}\sum_{j=0}^{17}n_{i,j}w^j,\qquad',
     r'n_{i,j}=\epsilon_{i,j}\sum_{k\geq0}b_{i,j,k}B^k\quad(i=2,3,4).\]',
     r'Each row gives two successive forty-digit blocks; unlisted blocks are zero.',
     r'The sign is repeated on every row. Exact multiplication proves',
     r'$r_i^3\sigma^2(u_i)=\sigma(u_i)$ and $r_i\tau(r_i)=1$.',
     r'\begingroup\setlength{\tabcolsep}{3pt}\fontsize{7.6}{9.2}\selectfont\ttfamily']
count=0
for i,rr in enumerate(roots,2):
    nums=[x*D for x in rr];assert all(x.denominator==1 for x in nums)
    out += [r'\par\medskip\normalfont\normalsize Root $r_'+str(i)+r'$\par\smallskip',
            r'\fontsize{7.6}{9.2}\selectfont\ttfamily',
            r'\begin{longtable}{rrrll}',
            r'$j$ & $k$ & $\epsilon$ & $b_{i,j,k}$ & $b_{i,j,k+1}$ \\ \hline\endhead']
    for j,n in enumerate(nums):
        n=int(n);sign='+' if n>=0 else '-';a=abs(n);blocks=[]
        while a:blocks.append(a%B);a//=B
        if not blocks:blocks=[0]
        if len(blocks)%2:blocks.append(0)
        for k in range(0,len(blocks),2):
            out.append(f'{j} & {k} & {sign} & {blocks[k]:040d} & {blocks[k+1]:040d} '+r'\\')
            count+=1
    out.append(r'\end{longtable}')
out.append(r'\endgroup')
text='\n'.join(out)+'\n'
target=base.parent/'sections/two_inert_level2_anti_coefficients.tex'
target.write_text(text)
# Independently read the literal output rows back to rational coefficients.
pieces=text.split('Root $r_')[1:]
assert len(pieces)==3
for i,piece in enumerate(pieces,2):
    rec=[0]*18
    for j,k,sign,a,b in re.findall(r'^(\d+) & (\d+) & ([+-]) & (\d+) & (\d+) \\\\',piece,re.M):
        j=int(j);k=int(k);sgn=1 if sign=='+' else -1
        rec[j]+=sgn*(int(a)*B**k+int(b)*B**(k+1))
    assert [F(x,D) for x in rec]==roots[i-2]
print('PASS: all54 literal rational coefficients reconstruct exactly;',count,'two-block rows')
print('Denominator',D,'=2*649^5; output',target)
