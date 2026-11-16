#!/usr/bin/env python3
"""Reproduce the independent A54 certificate and addition-law audit.

The originating certificate's JSON is preserved.  The retained stdout is
code/de_A54_independent_audit.out.  No arithmetic Galois-image inference
is made by this finite algebra check; see notes/de_A54_audit.md.
"""
from pathlib import Path
import runpy
import sympy as s
ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'notes/fgh_A54_certificate.py'
certificate = source.with_suffix('.json')
old = certificate.read_bytes() if certificate.exists() else None
try:
    runpy.run_path(str(source), run_name='__main__')
    x = s.symbols('x')
    I = s.I
    yy = x**3-x
    x2 = (x*x+1)**2/(4*x*(x*x-1))
    slope_num = (3*x*x-1)*(x-x2)/2+(I-1)*yy
    xalpha = slope_num**2/(yy*(x2+x)**2)-x2+x
    claimed = x*(3+4*I)*(x*x-1-2*I)**2/(25*(x*x-(1-2*I)/5)**2)
    assert s.cancel(xalpha-claimed, extension=I) == 0
    print('PASS independent addition-law derivation x((2-i)P).')
    lamH = (1-2*I)/5
    assert s.simplify(2*lamH/(lamH-1)-I) == 0
    print('PASS kernel label: x(2P)=-x(P), y(2P)=i y(P) selects lambda_H.')
finally:
    if old is not None:
        certificate.write_bytes(old)
