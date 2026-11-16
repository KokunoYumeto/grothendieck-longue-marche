"""Print the three exact principal S-prime generators in integral coordinates."""
from pathlib import Path
from fractions import Fraction as F
import json
import sys

sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parent
raw=json.loads((base/'two_inert_short_sunit_principal_certificate_data.json').read_text())
d=raw['d'];B=10**40
names={'6':r'\sigma_{11}','7':r'\sigma_{\Sigma}','8':r'\sigma_{59}'}
out=[r'\subsection*{Literal principal generators used in A.165}',
r'Put $B=10^{40}$ and $e_i=t^i/d^{\lfloor2i/3\rfloor}$ for $0\leq i\leq8$.',
r'The three elements below are defined by the displayed integer coordinates:',
r'\[\sigma_j=\sum_{i=0}^8 a_{j,i}e_i,\qquad',
r'a_{j,i}=\epsilon_{j,i}\sum_{k\geq0}b_{j,i,k}B^k.',
r'\]',
r'Each row supplies two successive forty-digit blocks; unlisted blocks are zero.',
r'The sign is repeated on each row.  Every $e_i$ is integral because',
r'$e_i^9=3^i d^{6i-9\lfloor2i/3\rfloor}\in\Z$.',
r'Their exact rational norms are $-121,-649,-3481$, respectively,',
r'and their exact prime divisors are certified in A.165.',
r'\begingroup\setlength{\tabcolsep}{3pt}\fontsize{7.6}{9.2}\selectfont\ttfamily']
count=0
for j,row in raw['generators'].items():
    out.append(r'\par\medskip\normalfont\normalsize Generator $'+names[j]+r'$\par\smallskip')
    out.append(r'\fontsize{7.6}{9.2}\selectfont\ttfamily')
    out.append(r'\begin{longtable}{rrrll}')
    out.append(r'$i$ & $k$ & $\epsilon$ & $b_{j,i,k}$ & $b_{j,i,k+1}$ \\ \hline\endhead')
    for i,c in enumerate(row['coefficients']):
        integer=F(c)*d**(2*i//3)
        assert integer.denominator==1
        value=integer.numerator;sign='-' if value<0 else '+'
        a=abs(value);blocks=[]
        while a:blocks.append(a%B);a//=B
        if not blocks:blocks=[0]
        assert (-1 if value<0 else 1)*sum(b*B**k for k,b in enumerate(blocks))==value
        for k in range(0,len(blocks),2):
            pair=[blocks[l] if l<len(blocks) else 0 for l in range(k,k+2)]
            out.append(f'{i} & {k} & {sign} & '+' & '.join(f'{a:040d}' for a in pair)+r' \\')
            count+=1
    out.append(r'\end{longtable}')
out.append(r'\endgroup')
target=base.parent/'sections/two_inert_short_sunit_coefficients.tex'
target.write_text('\n'.join(out)+'\n')
print('PASS: all27 integral coordinates reconstructed from',count,'two-block rows.')
print('Literal definitions:',target)
