#!/usr/bin/env python3
"""Standard crystalline mixed-Tate Selmer dimensions for the tripod, class<=8.

These are dimensions of spaces of torsors, not numbers of rational points.
No unrestricted section set, elliptic Bloch--Kato group, or finite GT shadow
is substituted for this explicitly specified Selmer problem.
"""
from pathlib import Path
import sympy as S
import csv,json
def witt(r,n):return sum(int(S.mobius(d))*r**(n//d) for d in S.divisors(n))//n
def main():
    rows=[];local=0;odd=0
    for n in range(1,9):
        r=witt(2,n);local+=r
        if n>=3 and n%2:odd+=r
        rows.append({'class':n,'graded_rank':r,'local_dimension':local,
                     'global_S0':odd,'global_S1':2+odd,'global_S2':4+odd})
    meta=[]
    for n in range(1,9):
        k=(n-1)//2
        meta.append({'class':n,'graded_rank':2 if n==1 else n-1,'local_dimension':2+n*(n-1)//2,'global_S0':k*(k+1),'global_S1':2+k*(k+1),'global_S2':4+k*(k+1)})
    meta_first={str(s):next(row['class'] for row in meta if row[f'global_S{s}']<row['local_dimension']) for s in range(3)}
    first={str(s):next(row['class'] for row in rows if row[f'global_S{s}']<row['local_dimension']) for s in range(3)}
    assert first==meta_first=={'0':1,'1':2,'2':4}
    out=Path(__file__).parent
    (out/'f_selmer_dimensions.json').write_text(json.dumps({'rows':rows,'metabelian_rows':meta,'first_strict_levels':first,'metabelian_first_strict_levels':meta_first},indent=2))
    with (out/'f_selmer_dimensions.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print(json.dumps({'rows':rows,'metabelian_rows':meta,'first_strict_levels':first,'metabelian_first_strict_levels':meta_first},indent=2))
    t=[r'\begin{center}\begin{tabular}{r|rrrrr}',r'\toprule Class&Graded rank&Local&Global $S=0$&Global $|S|=1$&Global $|S|=2$\\\midrule']
    for r in rows:t.append(' & '.join(str(v) for v in r.values())+r'\\')
    t +=[r'\bottomrule\end{tabular}\end{center}']
    (out.parent/'sections/F_dimension_table.tex').write_text('\n'.join(t))
if __name__=='__main__':main()
