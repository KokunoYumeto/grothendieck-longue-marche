"""Literal quartic maps and standalone proof data for A.154.

The retained discovery output is parsed by the separately audited Fisher
certificate; this program verifies the covariant maps by rational polynomial
arithmetic and exports every input coefficient independently as JSON and TeX.
No Selmer-group or rank assertion from software is used.
"""
from contextlib import redirect_stdout
from fractions import Fraction as Q
from pathlib import Path
import importlib.util, io, json, math

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fisher_literal',BASE/'harmonic_prym_fisher_local_certificate.py')
f=importlib.util.module_from_spec(spec)
with redirect_stdout(io.StringIO()): spec.loader.exec_module(f)
Z=f.ZERO

def trim(a):
    while len(a)>1 and a[-1]==Z: a.pop()
    return a
def pa(a,b):
    return trim([f.add(a[i] if i<len(a) else Z,b[i] if i<len(b) else Z) for i in range(max(len(a),len(b)))])
def pn(a): return [f.neg(x) for x in a]
def ps(a,b): return pa(a,pn(b))
def pm(a,b):
    c=[Z]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=f.add(c[i+j],f.mul(x,y))
    return trim(c)
def pc(c,a): return trim([f.mul(c,x) for x in a])
def pp(a,n):
    r=[f.ONE]
    for _ in range(n):r=pm(r,a)
    return r
def pd(a): return trim([f.mul(i,a[i]) for i in range(1,len(a))] or [Z])

for name,g in [('g1',f.g1),('g2',f.g2),('g3',f.g3),('small',f.small)]:
    gp=pd(g); H=ps(pc(3,pp(gp,2)),pc(4,pm(g,pd(gp))))
    R=pc(4,ps(pm(gp,H),pm(g,pd(H))))
    identity=ps(ps(pc(3,pp(R,2)),pc(16,pp(H,3))),pc(f.mul(36864,f.b),pm(H,pp(g,2))))
    assert identity==[Z],name
    # Pullback of dx/(2y) is -2 du/N: differentiate H/(48 N^2).
    assert pa(pc(4,ps(pm(pd(H),g),pm(H,gp))),R)==[Z]
    if name=='small':
        assert H==[Z,Z,f.mul(192,f.b)]
        expected=[Z,f.mul(-1536*f.r,f.b),Z,Z,Z,f.div(f.mul(-6144,f.power(f.b,2)),f.r)]
        assert R==expected
    print(name,': covariant map, curve identity and differential PASS')

# Translation by (0,0) of the direct isogeny-composition coordinates.
# x_old=N^2/(4u^2), y_old=N(r^2+4b u^4)/(8r u^3).
# Its translate is (b/x_old,-b*y_old/x_old^2), exactly the small-map formula.
assert ps(H,pc(f.mul(192,f.b),[Z,Z,f.ONE]))==[Z]
assert pa(pc(f.r,R),pc(f.mul(1536,f.b),pm([Z,f.ONE],[f.k(f.r*f.r),Z,Z,Z,f.mul(4,f.b)])))==[Z]
print('Small cover: exact T0-translation of the dual-isogeny composition PASS')
assert f.sign(f.polyval(f.g2,Z),1)>0
assert f.sign(f.polyval(f.g2,f.k(Q(-1,f.M))),-1)>0
assert all(f.sign(f.polyval(f.g3,Z),emb)>0 for emb in [1,-1])
print('Real witnesses g2(0,+), g2(-1/M,-), g3(0,+/-): PASS')

data={
  'field_polynomial':'t^2-2','M':f.M,'r':f.r,'b':f.ser(f.b),'I':f.ser(f.I),'J':['0','0'],
  'quartic_convention':'g_i(X,Z)=sum_{j=0}^4 c[i,j] X^j Z^(4-j)',
  'g1':[f.ser(x) for x in f.g1], 'g2':[f.ser(x) for x in f.g2], 'g3':[f.ser(x) for x in f.g3],
  'cubic_polynomial':'phi^3-3I*phi','triple_square_root':[f.ser(x) for x in f.mroot],
  'binary_gamma':[f.ser(x) for x in f.binary_gamma], 'small_gamma':[f.ser(x) for x in f.gamma],
  'primitive_small_gamma':[f.ser(x) for x in f.prim], 'hilbert_character':f.ser(f.char),
  'cubic_map_to_theta':'phi=-12theta; theta^3+btheta=0',
  'cover_map':'H=3fprime^2-4f*fsecond; R=4(fprime*H-f*Hprime); x=H/(48N^2), y=R/(768N^3)',
}
(BASE/'harmonic_prym_fisher_exact_data.json').write_text(json.dumps(data,indent=2)+'\n')

def tex_pair(x):
    den=math.lcm(*(a.denominator for a in x)); a,b=[int(c*den) for c in x]
    if not b: num=str(a)
    else:
        sign='+' if b>=0 else '-'
        num=r'\begin{gathered}\scriptstyle '+str(a)+r'\\[-2pt]\scriptstyle {}'+sign+str(abs(b))+r't\end{gathered}'
    return num if den==1 else r'\frac{'+num+'}{'+str(den)+'}'

tex=[r'''\paragraph{The literal Fisher input coefficients.}
Here \(t=\sqrt2\), \(r=1119169\), and
\(g_i(X,Z)=\sum_{j=0}^4 c_{i,j}X^jZ^{4-j}\).
The first polynomial is
\(g_1=r(X+Z)^4-(4b/r)X^4\).
The remaining coefficients, and the chosen square root
\(m=m_0+m_1\varphi+m_2\varphi^2\), are as follows.
Every displayed integer is an exact input, and the same
rational pairs are retained in
\path{code/harmonic_prym_fisher_exact_data.json}.
''']
for i,g in [(2,f.g2),(3,f.g3)]:
    for j,c in enumerate(g):
        tex.append('\\[\nc_{%d,%d}=%s.\n\\tag{A.154.D%d%d}\n\\]\n'%(i,j,tex_pair(c),i,j))
for j,c in enumerate(f.mroot):
    tex.append('\\[\nm_%d=%s.\n\\tag{A.154.Dm%d}\n\\]\n'%(j,tex_pair(c),j))
(BASE.parent/'sections'/'harmonic_prym_fisher_exact_data.tex').write_text('\n'.join(tex))
print('Standalone JSON and complete TeX input coefficients saved; all identities PASS.')
