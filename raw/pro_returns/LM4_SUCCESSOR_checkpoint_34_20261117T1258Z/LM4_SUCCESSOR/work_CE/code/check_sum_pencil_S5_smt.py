"""One bounded full-presentation S5 separation test, via installed libz3.

All 26 actual braid actions are imposed.  The actual 19-generator source
fixes point zero; the ambient action is transitive of prime degree five;
some deleted meridian is nonidentity.  A SAT model would be a full-group
separator.  UNKNOWN or UNSAT concerns only this degree/source-stabilizer
test and does not decide the actual source-kernel equality.
"""
from pathlib import Path
import ctypes as C
from ctypes.util import find_library
import hashlib,json,time

ROOT=Path(__file__).resolve().parents[2]
INPUT=ROOT/'work_DE/next_marginal_source/sum_pencil_words.json'
DATA=json.loads(INPUT.read_text())
STEM=ROOT/'work_CE/sum_pencil_S5_smt'
LIMIT_MS=300000

lines=['(set-logic QF_UFBV)']
def point(k):return f'(_ bv{k} 3)'
def app(f,k):return f'({f} {k})'
def decl(f):lines.append(f'(declare-fun {f} ((_ BitVec 3)) (_ BitVec 3))')
def eq(a,b):lines.append(f'(assert (= {a} {b}))')
def conj(a,b):
    if a==b or a==tuple(reversed(b)):return b
    key=(a,b)
    if key in conjcache:return conjcache[key]
    j=len(conjcache);f,fi=f'p{j}',f'pi{j}'
    decl(f);decl(fi)
    for k in range(5):
        q=app(a[1],point(k))
        eq(app(f,point(k)),app(a[0],app(b[0],q)))
        eq(app(fi,point(k)),app(a[0],app(b[1],q)))
        lines.append(f'(assert (bvule {app(f,point(k))} {point(4)}))')
        lines.append(f'(assert (bvule {app(fi,point(k))} {point(4)}))')
    out=(f,fi);conjcache[key]=out;return out

initial=[]
for i in range(1,24):
    f,fi=f'g{i}',f'gi{i}';initial.append((f,fi));decl(f);decl(fi)
    for h in (f,fi):
        lines.append('(assert (distinct '+' '.join(app(h,point(k)) for k in range(5))+'))')
        for k in range(5):lines.append(f'(assert (bvule {app(h,point(k))} {point(4)}))')
    for k in range(5):eq(app(f,app(fi,point(k))),point(k))
conjcache={}
for row in DATA['loops']:
    current=list(initial)
    for letter in row['word']:
        i=abs(letter)-1;a,b=current[i],current[i+1]
        current[i:i+2]=[conj(a,b),a] if letter>0 else [b,conj(tuple(reversed(b)),a)]
    for i,p in enumerate(current):
        if p==initial[i]:continue
        for k in range(5):eq(app(p[0],point(k)),app(initial[i][0],point(k)))
    print('Encoded',row['name'],'braid length',len(row['word']),'conjugation gates',len(conjcache),flush=True)

# Literal actual source marking: all outside-cluster generators and C fix 0.
for i in list(range(1,10))+list(range(15,24)):eq(app(f'g{i}',point(0)),point(0))
C0=point(0)
for i in reversed(range(10,15)):C0=app(f'g{i}',C0)
eq(C0,point(0))

# Transitivity is exactly finite reachability from 0: a strictly descending
# predecessor distance reaches 0, and every transitive five-point action
# admits such distances in {0,...,4}.
for k in range(5):lines.append(f'(declare-fun d{k} () (_ BitVec 3))')
for k in range(5):
    if k==0:eq('d0',point(0))
    else:
        lines.append(f'(assert (and (bvuge d{k} {point(1)}) (bvule d{k} {point(4)})))')
        terms=[]
        for j in range(5):
            if j==k:continue
            edges='(or '+' '.join(f'(= {app(f"g{i}",point(j))} {point(k)})' for i in range(1,24))+')'
            terms.append(f'(and (bvult d{j} d{k}) {edges})')
        lines.append('(assert (or '+' '.join(terms)+'))')
U=[1,2,6,9,15,18,22,23]
lines.append('(assert (or '+' '.join(f'(not (= {app(f"g{i}",point(k))} {point(k)}))' for i in U for k in range(1,5))+'))')

script='\n'.join(lines)+'\n'
STEM.with_suffix('.smt2').write_text(script)
print('SMT input bytes',len(script),'gates',len(conjcache),'assertions',sum(x.startswith('(assert') for x in lines),flush=True)

lib=C.CDLL(find_library('z3'))
ptr=C.c_void_p;uint=C.c_uint;strp=C.c_char_p
def api(name,args,ret):
    f=getattr(lib,name);f.argtypes=args;f.restype=ret;return f
mkcfg=api('Z3_mk_config',[],ptr);delcfg=api('Z3_del_config',[ptr],None)
mkctx=api('Z3_mk_context',[ptr],ptr);delctx=api('Z3_del_context',[ptr],None)
glob=api('Z3_global_param_set',[strp,strp],None)
glob(b'memory_max_size',b'2048')
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
print('Parsed input in',round(time.monotonic()-start,3),'seconds; starting bounded check',flush=True)
status=api('Z3_solver_check',[ptr,ptr],C.c_int)(ctx,solver)
names={-1:'unsat',0:'unknown',1:'sat'}
result={'scope':__doc__,'solver':'installed libz3 C API','timeout_ms':LIMIT_MS,
        'input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        'smt_sha256':hashlib.sha256(script.encode()).hexdigest(),
        'status':names[status],'elapsed_seconds':time.monotonic()-start,
        'conjugation_gates':len(conjcache),'smt_bytes':len(script)}
if status==0:
    result['reason_unknown']=api('Z3_solver_get_reason_unknown',[ptr,ptr],strp)(ctx,solver).decode()
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
    for i in range(1,24):
        decli=mkdecl(ctx,sym(ctx,f'g{i}'.encode()),1,(ptr*1)(sort),sort);vals=[]
        for k in range(5):
            ast=mkapp(ctx,decli,1,(ptr*1)(numeral(ctx,str(k).encode(),sort)));out=ptr()
            assert evaluate(ctx,model,ast,True,C.byref(out))
            vals.append(int(numstr(ctx,out).decode()))
        assert sorted(vals)==list(range(5));perms.append(vals)
    result['permutations']=perms
STEM.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
delctx(ctx)
