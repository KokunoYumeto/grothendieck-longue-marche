#!/usr/bin/env python3
"""Check every printed F33 pivot and the displayed terminal block against exact data."""
from pathlib import Path
from hashlib import sha256
import json,re
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
TEX='work/part_a/f_quadratic_sign_pair_restriction.tex'
CERT='work/part_a/code/affine_nonproduct_sign_pair_rank_certificate_stage_output.json'
text=(ROOT/TEX).read_text()
assert sha256((ROOT/TEX).read_bytes()).hexdigest()=='8a2cd87d9139c6e2bccd99cc9bb8db53883d064da5653fd804e2e2457ab96037'
certificate=json.loads((ROOT/CERT).read_text())
checks=[]
def check(name,value):
    assert value,name
    checks.append({'name':name,'passed':True})
tags=re.findall(r'\\tag\{F\.33\.(\d+)\}',text)
check('all_nineteen_exact_display_labels',tags==[str(i) for i in range(1,20)])
table=text.split('The following table prints every single',1)[1].split(r'\tag{F.33.14}',1)[0]
lines=[line.strip() for line in table.splitlines() if re.match(r'^\d+&',line.strip())]
check('thirteen_printed_table_rows',len(lines)==13)
printed=[[] for _ in range(4)]
variables=['R','s','t','u','v','w','z']
for expected,line in enumerate(lines,1):
    cells=line.rstrip('\\').split('&')
    check('table_row_number_%d'%expected,cells[0]==str(expected) and len(cells)==5)
    for j,cell in enumerate(cells[1:]):
        cell=cell.rstrip('.')
        if cell==r'\text{block below}':
            check('explicit_terminal_block_reference_%d'%expected,j==1 and expected in [12,13]);continue
        match=re.fullmatch(r'\((\d+),(\d+);(-?[A-Za-z0-9]+)\)',cell)
        assert match,cell
        row,column,coefficient=match.groups()
        sign=-1 if coefficient.startswith('-') else 1
        body=coefficient.lstrip('-')
        exponents=[0]*7
        if body!='1':
            assert set(body)<=set(variables)
            for character in body:exponents[variables.index(character)]+=1
        printed[j].append({'row':int(row),'column_zero_based':int(column),'coefficient':[[sign,exponents]]})
for j,chart in enumerate(certificate['charts']):
    check('printed_single_pivot_count_chart_%d'%j,len(printed[j])==len(chart['pivots']))
    for i,(actual,recorded) in enumerate(zip(printed[j],chart['pivots'])):
        check('printed_pivot_chart_%d_number_%d'%(j,i+1),all(actual[k]==recorded[k] for k in actual))
R,s,t,u,v,w,z=sp.symbols('R s t u v w z')
symbols=[R,s,t,u,v,w,z]
def polynomial(serial):return sp.Add(*(c*sp.prod(a**n for a,n in zip(symbols,e)) for c,e in serial))
block=re.search(r'M=\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}',text,re.S).group(1)
lines=[x.strip() for x in block.strip().split(r'\\')]
def parse_printed(expression):
    expression=re.sub(r'(?<=[A-Za-z0-9)])(?=[A-Za-z0-9(])','*',expression)
    return sp.sympify(expression,locals={str(a):a for a in symbols})
matrix=sp.Matrix([[parse_printed(x.strip()) for x in row.split('&')] for row in lines])
recorded=certificate['charts'][1]['terminal_two_by_two_block']
expected=sp.Matrix([[polynomial(x) for x in row] for row in recorded['entries']])
for i in range(2):
    for j in range(2):check('printed_terminal_entry_%d_%d'%(i,j),sp.expand(matrix[i,j]-expected[i,j])==0)
check('printed_terminal_determinant',sp.expand(matrix.det()+s*s*t)==0)
swap=sp.Matrix([[0,1],[1,0]])
check('printed_exact_row_swap',swap*swap==sp.eye(2) and sp.expand((swap*matrix).det()-s*s*t)==0)
def binding(name):
    raw=(ROOT/name).read_bytes();return {'path':name,'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
result={'status':'PASS_ROOT_ACTUAL_F33_TEX_COEFFICIENT_AUDIT','producer':binding(str(Path(__file__).relative_to(ROOT))),
 'input_bindings':[binding(TEX),binding(CERT)],'checks':checks,'check_count':len(checks),
 'printed_pivots':50,'displayed_terminal_entries':4,'matched_display_labels':19,
 'scope':'The actual frozen TeX, all printed single-pivot coordinates and coefficients, terminal matrix and row-order determinant transport. Proof topology and cochain maps are assessed in the written root review; this checker is not a PDF visual audit.'}
output=Path(__file__).with_name('check_f33_actual_tex_output.json');output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks':len(checks),'output':binding(str(output.relative_to(ROOT)))},indent=2))
