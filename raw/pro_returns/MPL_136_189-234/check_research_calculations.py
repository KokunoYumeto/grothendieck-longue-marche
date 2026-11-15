"""Independent small integral chain calculations for research note R037; no OCR."""
from pathlib import Path
from itertools import combinations_with_replacement, combinations
from math import gcd, lcm
import sympy as s

ROOT = Path(__file__).resolve().parent

def basis(kind, n):
    return list(combinations(range(n),2) if kind == 'exterior' else combinations_with_replacement(range(n),2))

def face(kind, n, index):
    src, dst = basis(kind,n), basis(kind,n-1)
    out = s.zeros(len(dst),len(src))
    def image(j):
        if index == 0:
            return None if j == 0 else j-1
        if index == n:
            return None if j == n-1 else j
        return j if j < index else j-1
    for col,(i,j) in enumerate(src):
        a,b = image(i),image(j)
        if a is None or b is None:
            continue
        if kind == 'exterior' and a == b:
            continue
        coefficient = 2 if kind == 'divided' and i != j and a == b else 1
        out[dst.index((a,b)),col] = coefficient
    return out

def primitive(v):
    den = lcm(*(int(x.q) for x in v)) if len(v) else 1
    vals = [int(x*den) for x in v]
    div = 0
    for x in vals:
        div = gcd(div,abs(x))
    return s.Matrix([x//div for x in vals]) if div else v

lines = [
    'Conditional interpretation used: Psi_* is the standard simplicial K(Z,1).',
    'Faces drop the first/last coordinate or merge adjacent coordinates.',
    'N_n is the intersection of kernels of d_1,...,d_n; its differential is d_0.',
    'These are small exact integral checks, not an interpretation of the ambiguous Psi^* on scan 229.',
    '',
]
for kind in ['divided','symmetric','exterior']:
    normalized = {0:s.zeros(0,0)}
    for n in range(1,6):
        stacked = s.Matrix.vstack(*(face(kind,n,i) for i in range(1,n+1)))
        vectors = [primitive(v) for v in stacked.nullspace()]
        normalized[n] = s.Matrix.hstack(*vectors) if vectors else s.zeros(len(basis(kind,n)),0)
    ranks = [normalized[n].cols for n in range(6)]
    expected = [0,0,1,0,0,0] if kind == 'exterior' else [0,1,1,0,0,0]
    assert ranks == expected
    lines.append(f'{kind} square: normalized ranks in degrees 0 through 5 = {ranks}')
    n2 = normalized[2]
    lines.append(f'  degree-two basis order = {basis(kind,2)}')
    lines.append(f'  primitive normalized generator = {list(n2)}')
    image = face(kind,2,0)*n2
    if kind != 'exterior':
        coefficient = normalized[1].gauss_jordan_solve(image)[0][0,0]
        assert abs(coefficient) == (2 if kind == 'divided' else 1)
        lines.append(f'  differential N_2 -> N_1 = multiplication by {coefficient}')
    else:
        assert image.rows == 0
        lines.append('  N_1=0, so the degree-two homology is Z')
    lines.append('')
lines.extend([
    'Conclusion over Z: Gamma^2 K(Z,1) has H_1=Z/2 and H_2=0;',
    'Sym^2 K(Z,1) is acyclic; Lambda^2 K(Z,1) has H_2=Z.',
    'Higher normalized terms vanish by the binomial-rank decomposition for the quadratic rank sequence.',
    '',
    'Rank-one four-complex check in total weight N:',
    '  ordinary de Rham: coefficient N from d(x^N)=N*x^(N-1)*dx;',
    '  ordinary Koszul: coefficient 1 from delta(x^(N-1)*dx)=x^N;',
    '  PD de Rham: coefficient 1 from d(gamma_N(x))=gamma_(N-1)(x)*dx;',
    '  PD Koszul: coefficient N from x*gamma_(N-1)(x)=N*gamma_N(x).',
])
text = '\n'.join(lines)+'\n'
(ROOT/'research_calculations.txt').write_text(text,encoding='utf-8')
print(text)
