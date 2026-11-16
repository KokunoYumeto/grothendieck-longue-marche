"""Direct witness verification; preserve every stored input witness.
Imported historical model initialization still executes its old exploratory checks.
This verifier does not solve or modify the new2631-bit witness.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
source=HERE/'mixed_scalar_action_frame_system.json';raw=source.read_bytes();data=json.loads(raw)
model=HERE/'check_mixed_scalar_action.py'
D={'__file__':str(model),'__name__':'__mixed704_verify__'}
with redirect_stdout(StringIO()):exec(compile(model.read_text().split('out=dict(scope=')[0],str(model),'exec'),D)
globals().update({k:v for k,v in D.items()if k not in('__file__','__name__')})
aa=tup(data['action_inner']);kc=tup(data['cusp_character']);AI=(A0,M0,aa,U0,H0)
def ph_new(g):
 a,m,z,u,h=gin(AI,ph(g))
 if O['eps'](g[4]):u=fva(u,kc)
 return a,m,z,u,h
def na_new(g):return ph_new(ca(g))
assert ph_new(T)==T
assert na_new(na_new(S))==S and na_new(na_new(R))==R
Q=(A0,oldm(tup(data['old_center_correction'])),tup(data['ordinary_correction']),tup(data['new_scalar_correction']),H0)
Bnew=gm(gm(AI,B),Q);assert Bnew==tup(data['corrected_scalar_frame'])
assert gin(Bnew,S)==ph_new(S)and gm(gi(Bnew),na_new(gi(Bnew)))==ONE
assert all(Q[1][mi[i,j]]==0 for i in range(4)for j in range(i+1,4))
assert all(not any(aa[zi[i,j]])for i in range(4)for j in range(4))
assert all(not kc[i]for i,t in enumerate(triples)if all(j<4 for j in t))
print('Stored704 witness: original cusp, square, s-conjugacy and norm PASS.',flush=True)
# Independent original full20 projection, including all old central coordinates.
path=HERE/'check_A66_W0_twenty_sframe.py';E20={'__file__':str(path),'__name__':'__mixed_full20_verify__'}
with redirect_stdout(StringIO()):exec(compile(path.read_text().split('out=dict(scope=')[0],str(path),'exec'),E20)
a69=json.loads((HERE/'A69_integral_scalar_frame_solution.json').read_text());B20=tup(a69['corrected_full20_BFRAME'])
freeZ=tuple(tup(data['ordinary_correction'])[zi[i,j]]for i in range(4)for j in range(4))
oldq=(E20['O']['AA0'],tup(data['old_center_correction']),E20['O']['HN0'])
Q20=((oldq,tup(data['T_correction'])),tuple(tup(data['U_correction'])+freeZ))
B20new=E20['em'](B20,Q20)
assert E20['ein'](B20new,E20['SS'])==E20['ph'](E20['SS'])
assert E20['em'](E20['ei'](B20new),E20['na'](E20['ei'](B20new)))==E20['ONE']
assert old_project(B20new[0][0])==project(Bnew)
assert tuple(Bnew[2][zi[i,j]]for i in range(4)for j in range(4))==B20new[1][4:]
print('Independent original full20 law: exact s-conjugacy/norm and literal common projection PASS.',flush=True)
full=dict(scope='Mixed704 scalar witness projected to the prior full20/free128 model; old frame coordinates may vary, old action retained.',
 old_center_correction=fva(tup(a69['old_center_correction']),tup(data['old_center_correction'])),
 T_correction=av(tup(a69['T_correction']),tup(data['T_correction'])),
 U_correction=av(tup(a69['U_correction']),tup(data['U_correction'])),
 ordinary_correction=av(tup(a69['ordinary_correction']),freeZ),
 corrected_full20_BFRAME=B20new,
 six_integral_free_offdiagonal_changes=tuple(Q[1][mi[i,j]]for i in range(4)for j in range(i+1,4)),
 binary_free_diagonal_changes=tuple(Q[1][mi[i,i]]for i in range(4)))
(HERE/'mixed_scalar_free_projection_witness.json').write_text(json.dumps(full,indent=2)+'\n')
assert source.read_bytes()==raw
(HERE/'mixed_scalar_witness_verified.json').write_text(json.dumps(dict(scope='Direct original704 and independent full20 witness verification; no new solution search',
 witness_sha256=hashlib.sha256(raw).hexdigest(),actual704='PASS',actual_full20='PASS',common_projection='PASS',
 integral_offdiagonal_retention='PASS',binary_diagonal_changes=full['binary_free_diagonal_changes']),indent=2)+'\n')
print('Input witness preserved; integral free offdiagonal values unchanged.',flush=True)
