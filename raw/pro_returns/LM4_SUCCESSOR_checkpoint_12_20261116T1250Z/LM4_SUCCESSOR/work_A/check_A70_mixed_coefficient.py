"""Exact multiplicity actions for the proposed32 mixed ordinary chiefs."""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
with redirect_stdout(StringIO()):O=runpy.run_path(str(HERE/'check_Q6_central_cover.py'))
fm=O['fm'];flin=O['flin'];frank=O['frank'];fsolve=O['fsolve']
E=json.loads((ROOT/'work_CE/Q6_integral_affine_data.json').read_text())['new_basis_columns_in_old_EB']
def tr(m):return list(map(list,zip(*m)))
def mm(a,b):return [list(flin(b,v))for v in a]
def ident(n):return [[int(i==j)for j in range(n)]for i in range(n)]
I=ident(8);Einv=tr([fsolve(tr(E),tuple(v))for v in I])
assert mm(E,Einv)==I
P=mm(mm(E,O['POS']),Einv);C=mm(mm(E,O['CE']),Einv);B=mm(P,C)
assert mm(P,P)==mm(C,C)==mm(B,B)==I and mm(P,C)==mm(C,P)
assert all(P[i][j]==I[i][j]and C[i][j]==I[i][j]for i in range(4)for j in range(8))
assert all(P[i][j]==C[i][j]==0 for i in range(4,8)for j in range(4))
slots=[(i,j)for i in range(8)for j in range(8)if (i<4)^(j<4)]
def ordinary(m):return [[fm(fm(m[i][r],m[i][r]),m[j][s])for r,s in slots]for i,j in slots]
PM,CM,BM=[ordinary(m)for m in(P,C,B)]
IM=ident(32)
assert mm(PM,CM)==BM and mm(BM,BM)==IM
rank=lambda m:frank(tr([[a^b for a,b in zip(row,rr)]for row,rr in zip(m,ident(len(m)))]))
print('Normalized positive8 matrix:',P)
print('Normalized canonical-c8 matrix:',C)
print('Normalized negative8 matrix:',B)
print('Binary-s block ranks(P-1,C-1,B-1):',*[rank([r[4:]for r in m[4:]])for m in(P,C,B)])
print('Mixed32 ranks(P-1,C-1,B-1):',rank(PM),rank(CM),rank(BM))
print('Mixed32 C2 H1 multiplicity:',32-2*rank(BM),'overF8')
(HERE/'A70_mixed_coefficient_actions.json').write_text(json.dumps(dict(
 scope='Exact coefficient actions only; no actual next-quotient norm result',
 normalized_positive=P,normalized_canonical_c=C,normalized_negative=B,
 mixed_slots=slots,positive_mixed=PM,canonical_c_mixed=CM,negative_mixed=BM,
 negative_rank=rank(BM),negative_H1_dimension=32-2*rank(BM)),indent=2)+'\n')
