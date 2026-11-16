"""Independently parse the displayed integer blocks before comparing data."""
from pathlib import Path
from fractions import Fraction
import json
import re
import sys

sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parent
text=(base.parent/'sections/two_inert_short_sunit_coefficients.tex').read_text()
data=json.loads((base/'two_inert_short_sunit_principal_certificate_data.json').read_text())
blocks=re.findall(r'\\begin\{longtable\}\{rrrll\}(.*?)\\end\{longtable\}',text,re.S)
assert len(blocks)==3
count=0
for key,block in zip(('6','7','8'),blocks):
    values=[0]*9
    for i,k,sign,a,b in re.findall(r'^([0-8]) & (\d+) & ([+-]) & (\d{40}) & (\d{40}) \\\\$',block,re.M):
        i=int(i);k=int(k);count+=1
        values[i]+=(1 if sign=='+' else -1)*(int(a)*10**(40*k)+int(b)*10**(40*(k+1)))
    expected=[Fraction(c)*649**(2*i//3) for i,c in enumerate(data['generators'][key]['coefficients'])]
    assert all(v==e for v,e in zip(values,expected))
print('PASS: TeX-first parser reconstructs all27 integer coordinates from',count,'rows.')
