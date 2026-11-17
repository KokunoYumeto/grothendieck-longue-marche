"""One smaller encoding of the authorized actual S5 separation question.

Use the certified swap-quotient bundle F7 semidirect F6.  The six source
base lifts and four actual cross-collision words fix point0.  The ambient
action is transitive of degree5, with some killed fiber meridian nontrivial.
All42 equivariance equations are imposed.  The two finite covers extend
after U filling, so their characters kill the full deletion kernel; a SAT
witness restricts to the original marginal.  UNKNOWN is not an exclusion.
"""
from pathlib import Path
import ctypes as C
from ctypes.util import find_library
import hashlib,json,time

ROOT=Path(__file__).resolve().parents[2]
INPUT=ROOT/'work_DE/next_marginal_source/tangent_bundle_fiber_data.json'
DATA=json.loads(INPUT.read_text())
STEM=ROOT/'work_CE/tangent_bundle_S5_smt'
LIMIT_MS=300000
lines=['(set-logic QF_UFBV)']
def point(k):return f'(_ bv{k} 3)'
def app(f,k):return f'({f} {k})'
def eq(a,b):lines.append(f'(assert (= {a} {b}))')
def word(w,k):
    for letter in reversed(w):k=app(f'g{letter}' if letter>0 else f'gi{-letter}',k)
    return k
for i in range(1,14):
    f,fi=f'g{i}',f'gi{i}'
    for h in (f,fi):
        lines.append(f'(declare-fun {h} ((_ BitVec 3)) (_ BitVec 3))')
        lines.append('(assert (distinct '+' '.join(app(h,point(k)) for k in range(5))+'))')
        for k in range(5):lines.append(f'(assert (bvule {app(h,point(k))} {point(4)}))')
    for k in range(5):eq(app(f,app(fi,point(k))),point(k))

for i in range(6):
    for j in range(1,8):
        w=DATA['old_actions'][str(i)][str(j)]
        for k in range(5):eq(app(f'g{i+8}',app(f'g{j}',app(f'gi{i+8}',point(k)))),word(w,point(k)))
    eq(app(f'g{i+8}',point(0)),point(0))
for w in DATA['new_fiber_words'].values():eq(word(w,point(0)),point(0))

for k in range(5):lines.append(f'(declare-fun d{k} () (_ BitVec 3))')
for k in range(5):
    if k==0:eq('d0',point(0))
    else:
        lines.append(f'(assert (and (bvuge d{k} {point(1)}) (bvule d{k} {point(4)})))')
        terms=[]
        for j in range(5):
            if j==k:continue
            edges='(or '+' '.join(f'(= {app(f"g{i}",point(j))} {point(k)})' for i in range(1,14))+')'
            terms.append(f'(and (bvult d{j} d{k}) {edges})')
        lines.append('(assert (or '+' '.join(terms)+'))')
U=DATA['killed_basis']
lines.append('(assert (or '+' '.join(f'(not (= {app(f"g{i}",point(k))} {point(k)}))' for i in U for k in range(5))+'))')
script='\n'.join(lines)+'\n';STEM.with_suffix('.smt2').write_text(script)
print('All42 actual equivariance equations; all6 source lifts and4 cross-seeds fix0.',flush=True)
print('SMT input bytes',len(script),'assertions',sum(x.startswith('(assert') for x in lines)),flush=True)

lib=C.CDLL(find_library('z3'))
ptr=C.c_void_p;uint=C.c_uint;strp=C.c_char_p
def api(name,args,ret):
    f=getattr(lib,name);f.argtypes=args;f.restype=ret;return f
mkcfg=api('Z3_mk_config',[],ptr);delcfg=api('Z3_del_config',[ptr],None)
mkctx=api('Z3_mk_context',[ptr],ptr);delctx=api('Z3_del_context',[ptr],None)
api('Z3_global_param_set',[strp,strp],None)(b'memory_max_size',b'2048')
cfg=mkcfg();ctx=mkctx(cfg);delcfg(cfg)
solver=api('Z3_mk_solver',[ptr],ptr)(ctx)
api('Z3_solver_inc_ref',[ptr,ptr],None)(ctx,solver)
params=api('Z3_mk_params',[ptr],ptr)(ctx)
api('Z3_params_inc_ref',[ptr,ptr],None)(ctx,params)
sym=api('Z3_mk_string_symbol',[ptr,strp],ptr)
api('Z3_params_set_uint',[ptr,ptr,ptr,uint],None)(ctx,params,sym(ctx,b'timeout'),LIMIT_MS)
api('Z3_solver_set_params',[ptr,ptr,ptr],None)(ctx,solver,params)
start=time.monotonic()
api('Z3_solver_from_string',[ptr,ptr,strp],None)(ctx,solver,script.encode())
print('Parsed in',round(time.monotonic()-start,3),'seconds; bounded check starts',flush=True)
status=api('Z3_solver_check',[ptr,ptr],C.c_int)(ctx,solver)
result={'scope':__doc__,'solver':'installed libz3 C API','timeout_ms':LIMIT_MS,
        'input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        'smt_sha256':hashlib.sha256(script.encode()).hexdigest(),
        'status':{-1:'unsat',0:'unknown',1:'sat'}[status],
        'elapsed_seconds':time.monotonic()-start,'smt_bytes':len(script)}
if status==0:result['reason_unknown']=api('Z3_solver_get_reason_unknown',[ptr,ptr],strp)(ctx,solver).decode()
if status==1:
    model=api('Z3_solver_get_model',[ptr,ptr],ptr)(ctx,solver)
    api('Z3_model_inc_ref',[ptr,ptr],None)(ctx,model)
    sort=api('Z3_mk_bv_sort',[ptr,uint],ptr)(ctx,3)
    mkdecl=api('Z3_mk_func_decl',[ptr,ptr,uint,C.POINTER(ptr),ptr],ptr)
    mkapp=api('Z3_mk_app',[ptr,ptr,uint,C.POINTER(ptr)],ptr)
    numeral=api('Z3_mk_numeral',[ptr,strp,ptr],ptr)
    evaluate=api('Z3_model_eval',[ptr,ptr,ptr,C.c_bool,C.POINTER(ptr)],C.c_bool)
    numstr=api('Z3_get_numeral_string',[ptr,ptr],strp)
    perms=[]
    for i in range(1,14):
        decli=mkdecl(ctx,sym(ctx,f'g{i}'.encode()),1,(ptr*1)(sort),sort);vals=[]
        for k in range(5):
            ast=mkapp(ctx,decli,1,(ptr*1)(numeral(ctx,str(k).encode(),sort)));out=ptr()
            assert evaluate(ctx,model,ast,True,C.byref(out))
            vals.append(int(numstr(ctx,out).decode()))
        assert sorted(vals)==list(range(5));perms.append(vals)
    result['fiber_permutations']=perms[:7];result['source_base_permutations']=perms[7:]
STEM.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
delctx(ctx)
