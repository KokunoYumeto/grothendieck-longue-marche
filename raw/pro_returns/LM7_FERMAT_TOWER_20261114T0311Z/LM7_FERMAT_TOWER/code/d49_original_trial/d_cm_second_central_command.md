# Exact original command

This is the executed historical command, with its original workspace paths. The copied source has SHA256 556a0bf97bc4e760d4c4fd0e68c4487e4897b9f90dc5d12f7817be3b5c955d11 and is archived at `../d_cm_central_mixed.py`. The actual JSON output and the actual helper certificate are retained here. The helper stdout was discarded in the original execution; none is reconstructed.

```bash
python - <<'PY'
from pathlib import Path
from contextlib import redirect_stdout
import io,sys,sympy as sp,json,time
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path('D49_EXPERIMENTS/code');base=p/'d_cm_central_base.py';base.write_text(Path('D48_EXPERIMENTS/code/d_cm_central_mixed.py').read_text())
sys.argv=[str(base),'--source-code',str(Path('LM7_FERMAT_TOWER/code').resolve())]
D={'__file__':str(base.resolve()),'__name__':'__main__'}
with redirect_stdout(io.StringIO()):exec(compile(base.read_text(),str(base),'exec'),D)
Ewords,rs,rr=D['Ewords'],D['es'],D['er'];C=D['GE']['cycles'];ch=D['ce'];n=len(ch)
def right_word(q,w):
 for a in w:q=rs[q] if a==0 else rr[q] if a==1 else rr[rr[q]]
 return q
lefts=[right_word(rs[0],Ewords[q]) for q in range(1152)]
leftr=[right_word(rr[0],Ewords[q]) for q in range(1152)]
assert sorted(lefts)==list(range(1152)) and sorted(leftr)==list(range(1152))
ivs=[0]*1152;ivr=[0]*1152
for q in range(1152):ivs[lefts[q]]=q;ivr[leftr[q]]=q
cols=[]
for j,c in enumerate(C):
 cols.append([int(i==j)-c.get(ivs[e],0) for i,e in enumerate(ch)])
 cols.append([int(i==j)-c.get(ivr[e],0) for i,e in enumerate(ch)])
A=sp.Matrix(n,2*n,lambda i,j:cols[j][i]);started=time.time();S=smith_normal_form(A,domain=ZZ)
diag=[abs(int(S[i,i])) for i in range(n)]
res={'shape':[n,2*n],'smith_multiplicities':{str(d):diag.count(d) for d in sorted(set(diag))},'elapsed_seconds':time.time()-started}
(p/'d_cm_second_central.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
PY
```
