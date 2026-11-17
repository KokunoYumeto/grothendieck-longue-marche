#!/usr/bin/env python3
"""Post-freeze, conditional checks of scans 126–144; never edits source files.

Requires SymPy. These are editorial calculations under the conventions named
in extension_notes.md, not corrections of the diplomatic transcription.
Run from any directory. Prints a Markdown report to standard output.
"""
from sympy import Matrix, eye, expand, factor, kronecker_product, symbols

c, g, b, b1, b2, u1, u2, v1, v2, U, l1, l2 = symbols(
    'chi gamma b b1 b2 u1 u2 v1 v2 U lambda1 lambda2')

def t(a1, a2, x1, x2):
    return a1*x2+x1*a2+c*x1*x2

shift=t(b1,b2,u1,u2)
actual=expand((b1+c*u1)*(b2+c*u2)-b1*b2)
missing=factor(actual-shift)
assert expand(missing-(c-1)*shift)==0

total=t(b1,b2,u1+v1,u2+v2)
plus=expand(total-shift-t(b1+c*u1,b2+c*u2,v1,v2))
minus=factor(total-shift-t(b1-c*u1,b2-c*u2,v1,v2))
assert plus==0
assert expand(minus-2*c*(u1*v2+u2*v1))==0

square=factor((U-g*(b+c*U))-(-U-g*b))
assert expand(square-(2-g*c)*U)==0

# The order of coordinates in the source is (eta,zeta).
translation=Matrix([[1,0],[U,1]])
minus_translation=Matrix([[1,0],[-U,1]])
literal_difference=-minus_translation-translation.inv()

# Explicit failed descent at chi=1. L is span(e_L), pi=(1,0).
# Tensor basis: e_L e_L, e_L e_M, e_M e_L, e_M e_M.
f=Matrix([[1,1],[0,1]])
q=Matrix([[1,0,0,0],[0,0,0,1]])
relation=Matrix([0,0,1,0])
assert q*relation==Matrix([0,0])
failed=q*kronecker_product(f,eye(2))*relation
assert failed==Matrix([1,0])

# Auxiliary gamma can be nonunique. No assertion that chi=2 lacks the
# distinguished available choice gamma=1: this only compares two choices.
choices=[(gamma,(-gamma)%4) for gamma in range(4) if (2*gamma)%4==2]
assert choices==[(1,3),(3,1)]

normalization=expand(2*c*l1*l2-c*l1*l2)
assert normalization==c*l1*l2

print('# Conditional checks for the extension worksheets')
print()
print('These computations use the frozen transcription only as a source of questions.')
print('They do not select a doubtful reading or assert a global categorical theorem.')
print()
print('| Source / note | Exact result | Interpretation |')
print('|---|---|---|')
print(f'| 126 / B04 | `{square}` | Residual in the displayed translation square; zero if gamma*chi=2. |')
print(f'| 128 / B05 | `{list(literal_difference)}` | Row-major entries of -T_-U minus inverse(T_U); the extra scalar minus is different from inversion. |')
print(f'| 128 / B08 | `{choices}` | Pairs (gamma,v) modulo 4 for chi=2 and b=1; both shift b to -b, but the translations differ. |')
print(f'| 130 / B09 | `{missing}` | Same-coordinate residual if the final increment is read as U instead of chi*U. |')
print(f'| 132 / B11 | plus convention: `{plus}`; minus convention: `{minus}` | The two sign conventions cannot be mixed in the displayed cocycle calculation. |')
print(f'| 140 / B19 | `{normalization}` | The three terms on L1 tensor L2 simplify without imposing chi=1. |')
print(f'| 144 / B24 | Q(relation)=0; Q((f tensor id)(relation))=`{list(failed)}` | An endomorphism preserving L need not preserve the pushout relation. |')
print()
print('The scalar polynomial cocycle check is a bookkeeping check of the new draft signs;')
print('the later context already claims the positive local groupoid composition identity (R11).')
