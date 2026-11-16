"""Integral identities behind the whole-family Burau obstruction.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026.
Run: python -I -B check_burau_integral_identities.py
"""
import sympy as s,json
w=s.symbols('w');mod=w*w+w+1
def red(M):return M.applyfunc(lambda x:s.rem(s.expand(x),mod,w))
A=s.Matrix([[1-w,w,0],[1,0,0],[0,0,1]])
B=s.Matrix([[1,0,0],[0,1-w,w],[0,1,0]])
C=s.Matrix([[1,0,-1],[0,1,-1],[0,0,-w]])
I=s.eye(3);X4=red((A*B*A)**2);X5=red((C*B*C)**2)
v=s.Matrix([1,1,1]);ell=s.Matrix([[1,w,w*w]])
assert red(X4-I)==red((1-w)*v*ell)
assert red((X4-I)**2)==s.zeros(3) and red((X5-I)**2)==s.zeros(3)
assert red(A*v)==v and red(B*v)==v
assert red(ell*A)==red(ell) and red(ell*B)==red(ell) and red(ell*v)==s.zeros(1)
flag=s.Matrix.hstack(v,s.Matrix([-w,1,0]),s.Matrix([1,0,0]))
assert flag.det()==-1
TA=red(flag.inv()*A*flag);TB=red(flag.inv()*B*flag)
assert all(TA[i,j]==TB[i,j]==0 for i,j in ((1,0),(2,0),(2,1)))
XX=[red(A*A),red(B*B),red(C*C),X4,X5]
assert all(M.subs(w,1).applyfunc(lambda x:int(x)%3)==I for M in XX)
def m(a,b):return tuple(sum(a[2*i+k]*b[2*k+j]for k in range(2))%12 for i in range(2)for j in range(2))
def inv(a):return (a[3],-a[1]%12,-a[2]%12,a[0])
def power(a,n):
    out=(1,0,0,1)
    for _ in range(n):out=m(out,a)
    return out
def comm(a,b):return m(m(m(a,b),inv(a)),inv(b))
x=(1,2,0,1);y=(1,0,10,1);z=inv(m(x,y))
res=[]
for k in (2,4,8,10):
    a=comm(comm(power(x,k),power(y,k)),comm(power(y,k),power(z,k)))
    assert a==(5,0,0,5)
    res.append({'even_exponent_mod12':k,'seed_matrix_mod12':a})
print(json.dumps({'X4_minus_I':[[str(x)for x in row]for row in (X4-I).tolist()],
 'X5_minus_I':[[str(x)for x in row]for row in (X5-I).tolist()],
 'both_square_zero_integrally':True,'primitive_flag_determinant':-1,
 'A_in_flag_basis':[[str(x)for x in row]for row in TA.tolist()],
 'B_in_flag_basis':[[str(x)for x in row]for row in TB.tolist()],
 'all_five_Xi_identity_mod_ramified_prime_above3':True,
 'all_even_prime_to3_exponent_classes':res},indent=2))
