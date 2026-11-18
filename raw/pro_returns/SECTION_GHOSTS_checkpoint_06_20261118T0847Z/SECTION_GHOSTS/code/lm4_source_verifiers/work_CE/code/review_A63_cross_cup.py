"""Independent rerun of the actual six-cup source/square certificate."""
from pathlib import Path
import sys
p=Path(__file__).resolve().parents[2]/'work_A/check_A63_cross_cup.py'
dest='Path('+repr(str(Path(__file__).resolve().parents[1]/'A63_cross_cup_independent_square.json'))+')'
s=p.read_text().replace("(HERE/'A63_cross_cup_square.json')",dest).replace('(HERE/outname)',dest)
G={'__file__':str(p),'__name__':'_CE_A63_review'}
argv=sys.argv
try:
 sys.argv=[str(p)]
 exec(compile(s,str(p),'exec'),G)
finally:sys.argv=argv
assert G['na'](G['na'](G['SS']))==G['SS']
assert G['na'](G['na'](G['RR']))==G['RR']
# Independently solve the actual s-conjugacy residual, without treating
# a cohomology-zero assertion as an already chosen literal frame.
M=G['M'];O=G['O'];CB=[tuple(col[:36])for col in M['square_coboundary_columns']]
base=G['ein'](G['B0'],G['SS']);actual=G['ph'](G['SS']);corr=[]
for a,b in zip(base[1],actual[1]):
 sol=O['fsolve'](CB,G['fva'](a,b));assert sol is not None;corr.append(sol)
# Left multiplication by a kernel element changes conjugacy by(1-S2)z.
B=G['em']((O['ONE'],tuple(corr)),G['B0'])
assert G['ein'](B,G['SS'])==actual
print('INDEPENDENT additional checks: actual b²(s)=s, b²(r)=r and literal s-conjugator existence PASS')
print('No normalizer norm or scalar-refinement realization inferred by this rerun.')
