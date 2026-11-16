"""Render every exact unit coordinate in a compact integral-basis block table."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parent
raw=json.loads((base/'two_inert_relative_unit_repair_certificate_data.json').read_text())
d=raw['d'];B=10**40
out=[r'\subsection*{Complete unit coordinates for A.159}',
r'The four units in A.159 have the following literal definitions.  Put',
r'\[B=10^{40},\qquad e_i=t^i/d^{\lfloor2i/3\rfloor}\quad(0\leq i\leq8).\]',
r'Each $e_i$ is integral, since its ninth power is the integer',
r'$3^i d^{6i-9\lfloor2i/3\rfloor}$.  Set $u_1=\alpha^2-2$.',
r'For $j=2,3,4$, the tables define $u_j=\sum_{i=0}^8 a_{j,i}e_i$ by',
r'\[a_{j,i}=\epsilon_{j,i}\sum_{k\geq0}b_{j,i,k}B^k.\]',
r'A row labelled $(i,k,\epsilon)$ supplies the two successive blocks',
r'$b_{j,i,k},b_{j,i,k+1}$.  Unlisted blocks are zero.',
r'The sign is repeated for readability.  The tables are generated from the',
r'exact candidate coordinates and reconstruct them without rounding.',
r'\begingroup\setlength{\tabcolsep}{3pt}\fontsize{7.6}{9.2}\selectfont\ttfamily']
count=0
for row in raw['units'][1:]:
 j=row['index'];out.append(r'\par\medskip\normalfont\normalsize Unit $u_'+str(j)+r'$\par\smallskip')
 out.append(r'\fontsize{7.6}{9.2}\selectfont\ttfamily')
 out.append(r'\begin{longtable}{rrrll}')
 out.append(r'$i$ & $k$ & $\epsilon$ & $b_{j,i,k}$ & $b_{j,i,k+1}$ \\ \hline\endhead')
 for i,c in enumerate(row['candidate']):
  integer=F(c)*d**(2*i//3);assert integer.denominator==1
  v=integer.numerator;sgn='-'if v<0 else '+';a=abs(v);blocks=[]
  while a:blocks.append(a%B);a//=B
  if not blocks:blocks=[0]
  recovered=sum(x*B**k for k,x in enumerate(blocks))*(-1 if v<0 else 1)
  assert recovered==v
  for k in range(0,len(blocks),2):
   vals=[blocks[l]if l<len(blocks)else 0 for l in range(k,k+2)]
   out.append(f'{i} & {k} & {sgn} & '+ ' & '.join(f'{x:040d}'for x in vals)+r' \\')
   count+=1
 out.append(r'\end{longtable}')
out.append(r'\endgroup')
target=base.parent/'sections/two_inert_unit_coefficients_supplement.tex'
target.write_text('\n'.join(out)+'\n')
print('Complete coefficient rows',count)
print('Every integer-basis coordinate exactly reconstructed; every basis element has an explicit monic integral equation.')
print('PASS: complete literal definitions of u2,u3,u4; u1=alpha^2-2.')
