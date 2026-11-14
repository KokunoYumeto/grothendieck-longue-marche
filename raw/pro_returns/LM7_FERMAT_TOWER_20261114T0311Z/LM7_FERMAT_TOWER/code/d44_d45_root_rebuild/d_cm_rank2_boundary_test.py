#!/usr/bin/env python3
"""Exact nonlinear test of the retained D39 seed on both rank-two quotients.

Reconstruct the actual D33 words from the saved certificates without
running any preceding program, apply D39's retained global gauge, and
evaluate every six-state path through Magnus degree9.  A small C++
integer helper performs the long word pass; Python independently forms
the peripheral equations and both free-generator substitutions.
"""
from pathlib import Path
from collections import deque
from functools import lru_cache
from itertools import product
import argparse,ast,hashlib,importlib.util,json,subprocess,tempfile,time

ap=argparse.ArgumentParser()
ap.add_argument('--source-code',type=Path,
                default=Path(__file__).resolve().parents[2]/'LM7_FERMAT_TOWER'/'code')
ap.add_argument('--elliptic-correction',action='store_true',
                help='apply the exhaustive centralizer certificate and check its literal elliptic word')
ap.add_argument('--output-stem',default='d_cm_rank2_boundary_test')
args=ap.parse_args();SRC=args.source_code;OUT=Path(__file__).resolve().parent;started=time.time()
read=lambda n:json.loads((SRC/(n+'.json')).read_text())
D=read('d_cm_fermat_joint_base');Q=[tuple(q) for q in D['Q']];ix={q:i for i,q in enumerate(Q)}
I=(1,0,0,1)
def canon(a):return min(a,tuple(-x%12 for x in a))
def qm(a,b):
    return canon(((a[0]*b[0]+a[1]*b[2])%12,(a[0]*b[1]+a[1]*b[3])%12,
                  (a[2]*b[0]+a[3]*b[2])%12,(a[2]*b[1]+a[3]*b[3])%12))
qt=[[ix[qm(a,b)] for b in Q] for a in Q]
qi=ix[I];qs=ix[canon((0,1,11,0))];qr=ix[canon((0,11,1,11))]

# Only these pure function definitions are loaded.  In particular none
# of the previous script's imports, calculations or output writes run.
pure_names={'inverse','comm','graph','degree2','multiply','bracket','lyndon','lieword','nw','central'}
pure_source=SRC/'d_cm_fermat_homology_image.py'
ns={'deque':deque,'lru_cache':lru_cache,'product':product}
tree=ast.parse(pure_source.read_text())
nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in pure_names]
assert {n.name for n in nodes}==pure_names
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(pure_source),'exec'),ns)
Nwords,chN,_=ns['graph'](list(range(576)),lambda a,b:qt[a][b],qi,qs,qr)
assert len(Nwords)==97;ns['Nwords']=Nwords
reps={qi:b''};queue=deque([qi])
while queue:
    q=queue.popleft()
    for a,g in [(0,qs),(1,qr)]:
        h=qt[q][g]
        if h not in reps:reps[h]=reps[q]+bytes([a]);queue.append(h)
O=[i for i,q in enumerate(Q) if tuple(a%2 for a in q)==I
   and tuple(a%3 for a in qm(q,q)) in [(1,0,0,1),(2,0,0,2)]]
q0=[min(qt[q][o] for o in O) for q in range(576)];Q0=sorted(set(q0))
m0=lambda a,b:q0[qt[a][b]]
e,s,r=q0[qi],q0[qs],q0[qr];r2=m0(r,r)
Kwords,chK,ixK=ns['graph'](Q0,m0,e,s,r);ns['Kwords']=Kwords
saved=read('d_cm_rank4_refine')
assert [list(w) for w in Kwords]==saved['K_basis_words']
chord={j:i for i,j in enumerate(chK)}
def collapse(w):
    q=e;out=[]
    def add(j,z):
        i=chord.get(j)
        if i is None:return
        a=z*(i+1)
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    for a in w:
        if a==0:q=m0(q,s)
        else:
            h=m0(q,r if a==1 else r2);add(ixK[q],1);add(ixK[h],-1);q=h
    return q,out
relwords=[bytes(w) for w in saved['degree2_relation_words']];rel=[]
for w in relwords:
    q,ww=collapse(w);v,z=ns['degree2'](ww);assert q==e and v==0;rel.append(z)
Wwords=[];piv={}
for i,j,k in product(range(9),repeat=3):
    z=ns['bracket'](rel[i],2,ns['bracket'](rel[j],2,rel[k],2),4);v=z
    for p in sorted(piv,reverse=True):
        if (v>>p)&1:v^=piv[p]
    if v:piv[v.bit_length()-1]=v;Wwords.append(ns['comm'](relwords[i],ns['comm'](relwords[j],relwords[k])))
assert len(Wwords)==240
ns['pairs']=[(i,j) for i in range(97) for j in range(i,97)]
J=read('d_cm_quadratic_search')['witness']
fixed=[int(v,16) for v in read('d_cm_class2_two')['s_centralizer_basis']]
wa=ns['central'](int(J['central_A_coefficients'],16))+ns['nw'](int(J['homology_A_cycles'],16))+reps[qi]
qb=ix[canon(tuple(J['beta']))]
wb=ns['central'](int(J['central_beta_coefficients'],16))+ns['nw'](int(J['homology_beta_cycles'],16))+reps[qb]
for j,v in enumerate(fixed):
    if (int(J['beta_right_s_centralizer_coefficients'],16)>>j)&1:wb+=ns['nw'](v)
J4=read('d_cm_exponent4')['witness']
wa=ns['central'](int(J4['upper_A_correction'],16),2)+ns['central'](int(J4['previous_A_central_change'],16))+wa
wb=ns['central'](int(J4['upper_beta_correction'],16),2)+ns['central'](int(J4['previous_beta_central_change'],16))+wb
L3=[w for w in product(range(4),repeat=3) if ns['lyndon'](w)]
namespace={'Nwords':Nwords,'Kwords':Kwords,'relwords':relwords,'Wwords':Wwords,
           'L3':L3,'lieword':ns['lieword'],'lyndon':ns['lyndon'],'wa':wa,'wb':wb}
spec=importlib.util.spec_from_file_location('readonly_D33_reconstruct',SRC/'d_cm_degree8_reconstruct.py')
reconstruct=importlib.util.module_from_spec(spec);spec.loader.exec_module(reconstruct)
words=reconstruct.joint_words(namespace)
expected=json.loads((SRC/'d_cm_degree8_reconstruct.out').read_text())
for name in ['A','beta']:assert hashlib.sha256(words[name]).hexdigest()==expected[name+'_sha256']
assert 2*(len(words['A'])+len(words['beta']))+4==12921196
print('Exact D33 source hashes verified.',flush=True)

small=json.loads((OUT/'d_cm_solvable_even_boundary.json').read_text())
graphs=[]
for name in ['sphere','elliptic']:
    G=[tuple(q) for q in small[name+'_quotient_states']];gi={q:i for i,q in enumerate(G)}
    if name=='sphere':
        mul=lambda a,b:tuple(a[b[i]] for i in range(3));e0=(0,1,2);s0=(1,0,2);r0=(1,2,0)
    else:
        mul=lambda a,b:((a[0]+b[0])%2,(a[1]+b[1])%3);e0=(0,0);s0=(1,0);r0=(0,1)
    rs=[gi[mul(q,s0)] for q in G];rr=[gi[mul(q,r0)] for q in G]
    ch=[0]*6
    for j,h in enumerate(small[name+'_cycle_chords']):ch[h]=j+1
    graphs.append({'name':name,'G':G,'e':gi[e0],'rs':rs,'rr':rr,'rr2':[rr[h] for h in rr],'ch':ch,
                   'basis':small['sphere_F_basis_B_words' if name=='sphere' else 'elliptic_Bprime_basis_B_words']})
config='\n'.join(' '.join(map(str,g[k])) for g in graphs for k in ['rs','rr','ch'])+'\n'
k=read('d_cm_fermat_homology_seed')['summary']['finite_gauge_exponent']
assert k==-438
gauge=bytes([0,1,0,1])*(-k)
normalized={name:gauge+words[name] for name in ['A','beta']}
correction_record=None
if args.elliptic_correction:
    cc=json.loads((OUT/'d_cm_rank2_centralizers.json').read_text())['certificates'][1]
    jj=json.loads((OUT/'d_cm_rank2_degree9.json').read_text())
    assert cc['name']=='elliptic' and cc['full_remainder']=='0x0'
    mask=int(cc['solution_mask'],16)
    def freduce(w):
        out=[]
        for a in w:
            if out and out[-1]==-a:out.pop()
            else:out.append(a)
        return tuple(out)
    def finverse(w):return tuple(-a for a in reversed(w))
    @lru_cache(None)
    def lyndon_free(w):
        if len(w)==1:return (w[0]+1,)
        cut=next(j for j in range(1,len(w)) if ns['lyndon'](w[j:]))
        a,b=lyndon_free(w[:cut]),lyndon_free(w[cut:])
        return freduce(a+b+finverse(a)+finverse(b))
    central_words=[lyndon_free(tuple(w)) for w in jj['Lyndon_words']]
    def chosen_free(bits,basis):
        return freduce(tuple(a for j,w in enumerate(basis) if (bits>>j)&1 for a in w))
    beta_central=chosen_free(mask&((1<<56)-1),central_words)
    A_central=chosen_free((mask>>56)&((1<<56)-1),central_words)
    beta_right=chosen_free(mask>>112,cc['centralizer_free_words'])
    bb=[bytes(w) for w in small['elliptic_Bprime_basis_B_words']]
    def to_B(w):
        return b''.join(bb[a-1] if a>0 else ns['inverse'](bb[-a-1]) for a in w)
    normalized['A']=to_B(A_central)+normalized['A']
    normalized['beta']=to_B(beta_central)+normalized['beta']+to_B(beta_right)
    correction_record={'solution_mask':hex(mask),
        'central_A_Lyndon_mask':hex((mask>>56)&((1<<56)-1)),
        'central_beta_Lyndon_mask':hex(mask&((1<<56)-1)),
        'right_beta_centralizer_mask':hex(mask>>112),
        'elliptic_free_basis_B_words':[list(w) for w in bb],
        'A_left_correction_free_word':list(A_central),
        'beta_left_correction_free_word':list(beta_central),
        'beta_right_correction_free_word':list(beta_right),
        'A_left_correction_B_word':list(to_B(A_central)),
        'beta_left_correction_B_word':list(to_B(beta_central)),
        'beta_right_correction_B_word':list(to_B(beta_right)),
        'corrected_source_words':{name:{'B_letter_length':len(w),
             'sha256':hashlib.sha256(w).hexdigest()} for name,w in normalized.items()}}
polys={};helper_logs={}
helper_checks=0
with tempfile.TemporaryDirectory(prefix='rank2_exact_',dir=OUT) as tmp:
    tmp=Path(tmp);cfg=tmp/'graph.txt';cfg.write_text(config)
    exe=tmp/'magnus';subprocess.run(['g++','-O3','-std=c++17',str(OUT/'d_cm_rank2_magnus.cpp'),'-o',str(exe)],check=True,capture_output=True)
    # An independent tuple-monomial Cauchy calculation checks the C++
    # shift implementation, both graphs, all starts and both signs.
    def reference(g,w,start):
        q=start;p={()}
        def letter(p,a):
            i=abs(a)-1
            series=[()]+[(i,)*d for d in (range(1,10) if a<0 else [1])]
            out=set()
            for v in p:
                for z in series:
                    if len(v)+len(z)<=9:
                        h=v+z
                        if h in out:out.remove(h)
                        else:out.add(h)
            return out
        for a in w:
            if a==0:q=g['rs'][q]
            else:
                h=(g['rr'] if a==1 else g['rr2'])[q]
                if g['ch'][q]:p=letter(p,g['ch'][q])
                if g['ch'][h]:p=letter(p,-g['ch'][h])
                q=h
        poly=[0]*10
        for w in p:poly[len(w)]^=1<<sum(a<<j for j,a in enumerate(w))
        return q,poly
    samples=[b'',bytes([0,0]),bytes([1,1,1]),bytes([2,2,2]),
             bytes([0,1,2,0,2,1,1,0,2,0,1,0,1,2,2,0,1])]
    samples += [bytes(w) for g in graphs for w in g['basis']]
    for j,w in enumerate(samples):
        wp=tmp/'small.bin';wp.write_bytes(w)
        rr=subprocess.run([str(exe),str(cfg),str(wp)],check=True,capture_output=True,text=True)
        for line in rr.stdout.splitlines():
            vals=line.split();ig,q,end,letters=map(int,vals[:4])
            expected_end,expected_poly=reference(graphs[ig],w,q)
            assert end==expected_end and [1]+[int(z,16) for z in vals[4:]]==expected_poly
            helper_checks+=1
    assert helper_checks==108
    for name in ['A','beta']:
        wp=tmp/(name+'.bin');wp.write_bytes(normalized[name])
        run=subprocess.run([str(exe),str(cfg),str(wp)],check=True,capture_output=True,text=True)
        helper_logs[name]=run.stdout;polys[name]=[[None]*6 for _ in range(2)]
        for line in run.stdout.splitlines():
            vals=line.split();g,q,end,letters=map(int,vals[:4])
            if not args.elliptic_correction or g==1:assert q==end
            polys[name][g][q]=[1]+[int(z,16) for z in vals[4:]]
        assert all(v is not None for row in polys[name] for v in row)
        print('Full normalized',name,'word evaluated at all12 graph starts.',flush=True)

DEG=9;ONE=[1]+[0]*DEG
def tensor(a,b,d):
    z=0
    while b:
        bit=b&-b;j=bit.bit_length()-1;b^=bit;z^=a<<(j<<d)
    return z
def product_poly(a,b):
    c=[1]+[a[d]^b[d] for d in range(1,DEG+1)]
    for d in range(2,DEG+1):
        for i in range(1,d):
            if a[i] and b[d-i]:c[d]^=tensor(a[i],b[d-i],i)
    return c
def inverse_poly(a):
    b=[1]+[0]*DEG
    for d in range(1,DEG+1):
        z=a[d]
        for i in range(1,d):
            if a[i] and b[d-i]:z^=tensor(a[i],b[d-i],i)
        b[d]=z
    assert product_poly(a,b)==ONE and product_poly(b,a)==ONE
    return b
def mulmany(*polys):
    out=ONE
    for p in polys:out=product_poly(out,p)
    return out
def letter_poly(j):
    a=ONE.copy();a[1]=1<<(abs(j)-1)
    return a if j>0 else inverse_poly(a)
def step_poly(g,q,letter):
    if letter==0:return g['rs'][q],ONE
    h=g['rr'][q] if letter==1 else g['rr2'][q]
    out=ONE
    if g['ch'][q]:out=product_poly(out,letter_poly(g['ch'][q]))
    if g['ch'][h]:out=product_poly(out,letter_poly(-g['ch'][h]))
    return h,out
def original_word(g,w,start=None):
    q=g['e'] if start is None else start;v=ONE
    for a in w:q,u=step_poly(g,q,a);v=product_poly(v,u)
    return q,v
def first_nonzero(p):return next((d for d in range(1,DEG+1) if p[d]),None)
results=[];details=[]
for ig,g in enumerate(graphs):
    if args.elliptic_correction and g['name']!='elliptic':continue
    A=polys['A'][ig];B=polys['beta'][ig]
    Ai=[inverse_poly(p) for p in A];Bi=[inverse_poly(p) for p in B]
    ss=[];rr=[]
    for q in range(6):
        ss.append(product_poly(B[q],Bi[g['rs'][q]]))
        h,p=step_poly(g,q,1);rr.append(mulmany(A[q],p,Ai[h]))
    rrinv=[inverse_poly(rr[g['rr2'][q]]) for q in range(6)]
    def actual_word(w,start=None):
        q=g['e'] if start is None else start;p=ONE
        for a in w:
            p=product_poly(p,(ss if a==0 else rr if a==1 else rrinv)[q])
            q=(g['rs'] if a==0 else g['rr'] if a==1 else g['rr2'])[q]
        return q,p
    cusp=[]
    for q in range(6):
        end,p=actual_word([0,1],q);ee,old=original_word(g,[0,1],q);assert end==ee
        defect=product_poly(p,inverse_poly(old))
        assert not any(defect[1:9])
        cusp.append(defect)
    images=[];differences=[]
    for j,w in enumerate(g['basis']):
        q,p=actual_word(w);assert q==g['e'] and p[1]==1<<j
        q,old=original_word(g,w);assert old==letter_poly(j+1)
        images.append(p);differences.append(product_poly(p,inverse_poly(old)))
    width=2 if g['name']=='sphere' else 6
    q,peripheral=actual_word([0,1]*width);qq,old=original_word(g,[0,1]*width)
    assert q==qq==g['e'];boundary=product_poly(peripheral,inverse_poly(old))
    result={'graph':g['name'],'free_rank':2,'degree':DEG,
            'all_six_relative_cusp_defects_vanish_through_degree8':True,
            'relative_cusp_degree9_supports':[p[9].bit_count() for p in cusp],
            'relative_cusp_degree9_at_identity':hex(cusp[g['e']][9]),
            'recorded_word_is_peripheral_through_degree9':not any(p[9] for p in cusp),
            'free_generator_action_first_difference_degrees':[first_nonzero(p) for p in differences],
            'free_kernel_cusp_width':width,
            'free_kernel_cusp_defect_first_degree':first_nonzero(boundary),
            'free_kernel_cusp_degree9':hex(boundary[9]),
            'Frattini_action_is_identity':True}
    results.append(result)
    details.append({'name':g['name'],'A_polynomials':[[hex(x) for x in p] for p in A],
                    'beta_polynomials':[[hex(x) for x in p] for p in B],
                    'relative_cusp_defect_polynomials':[[hex(x) for x in p] for p in cusp],
                    'free_generator_images':[[hex(x) for x in p] for p in images],
                    'free_cusp_defect':[hex(x) for x in boundary]})
summary={'actual_D33_source_hashes_verified':True,'raw_B_cusp_word_length':12921196,
         'retained_D39_gauge':k,'all12_graph_starts_for_each_conjugator_checked':True,
         'independent_tuple_Cauchy_helper_checks':helper_checks,
         'exact_integer_mod2_Magnus_degree':DEG,'results':results,
         'scope':'Exact recorded-word test and induced free-generator substitutions. A nonzero degree9 defect is a failure of this representative, not an exclusion of other same-action conjugators or of the CM pair.',
         'elapsed_seconds':round(time.time()-started,3)}
if args.elliptic_correction:
    assert all(r['recorded_word_is_peripheral_through_degree9'] for r in results)
    original=json.loads((OUT/'d_cm_rank2_boundary_test.json').read_text())['graphs'][1]
    assert all(p[:9]==q[:9] for p,q in zip(details[0]['free_generator_images'],original['free_generator_images']))
    summary['same_elliptic_action_retained_modulo_D9']=True
    summary['scope']='Literal corrected elliptic action through degree9, with the complete recorded elliptic action moduloD9 retained. No simultaneous sphere or full D39 homology lift is asserted.'
(OUT/(args.output_stem+'.json')).write_text(json.dumps({'summary':summary,'graphs':details,
      'literal_correction':correction_record,
      'source_hashes':{k:expected[k] for k in ['A_sha256','beta_sha256']},
      'pure_function_source_sha256':hashlib.sha256(pure_source.read_bytes()).hexdigest(),
      'cpp_helper_sha256':hashlib.sha256((OUT/'d_cm_rank2_magnus.cpp').read_bytes()).hexdigest(),
      'exact_helper_output':helper_logs},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
