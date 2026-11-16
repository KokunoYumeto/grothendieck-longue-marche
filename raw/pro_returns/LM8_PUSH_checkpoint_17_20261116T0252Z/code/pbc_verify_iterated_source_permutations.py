#!/usr/bin/env python3
"""Replay the finite marked source in its actual degree-2592 permutation group.

This stops before every Schur-extension calculation.  The original cached
pc presentation and its triangular adapted basis are checked directly as
permutations, including all marked frames and chosen pure centralizers.
No older source, output, or restoration input is changed.
"""
from pathlib import Path
import hashlib,json,subprocess,time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
old_path=HERE/'pbc_iterated_joint_pc.json'
adapt_path=HERE/'pbc_iterated_adapted_pc.json'
source_path=HERE/'pbc_iterated_shortcut_v2_original_source.json'
program_path=HERE/'pbc_hopf_iterated_joint_sparse.g'
old=json.loads(old_path.read_text())
adapt=json.loads(adapt_path.read_text())
source=json.loads(source_path.read_text())
assert len(old['relative_orders'])==176
assert old['order']==adapt['order']==source['order']
for field in ('relative_orders','powers','conjugates','s','r','f','left_s_frame','left_r_frame'):
    if field in adapt:
        assert source[field]==adapt[field],field
for label in ('s','r'):
    assert source[label+'_centralizers']==[adapt[label+'_centralizers'][i-1]
        for i in source['original_'+label+'_centralizer_indices']]

def gap(x):return json.dumps(x,separators=(',',':'))
prefix=program_path.read_text().split('PBC_CacheVector:=',1)[0]
# The prefix has constructed the actual group and its pcp isomorphism,
# and ends immediately after assigning PBC_CacheGens.  It has no writes.
assert 'PrintTo(' not in prefix and 'SparseSchur(' not in prefix
lines=[prefix,
 'Assert(0,IsBijective(iso));',
 'Assert(0,PBC_FiniteAuto<>fail and IsBijective(PBC_FiniteAuto));',
 'Assert(0,bs<>fail and br<>fail);',
 'PBC_Perms:=List(PBC_CacheGens,g->PreImagesRepresentative(iso,g));;',
 'Assert(0,Group(PBC_Perms)=G);',
 'PBC_Word:=function(gens,w) local v,i;v:=();'
 'for i in [1,3..Length(w)-1] do v:=v*gens[w[i]]^w[i+1];od;return v;end;;',
 f'PBC_OldOrders:={gap(old["relative_orders"])};;',
 f'PBC_OldPowers:={gap(old["powers"])};;',
 f'PBC_OldConjugates:={gap(old["conjugates"])};;',
 'Assert(0,List(PBC_CacheGens,RelativeOrderPcp)=PBC_OldOrders);',
 'for i in [1..176] do Assert(0,PBC_Perms[i]^PBC_OldOrders[i]=PBC_Word(PBC_Perms,PBC_OldPowers[i]));od;',
 'for a in PBC_OldConjugates do Assert(0,PBC_Perms[a[1]]^PBC_Perms[a[2]]=PBC_Word(PBC_Perms,a[3]));od;',
 'Print("old_pc_all_literal_permutation_clauses_PASS runtime ",Runtime(),"\\n");',
]
for field,actual in [('s','s'),('r','r'),('f','f'),('bs','bs'),('br','br')]:
    lines.append(f'Assert(0,PBC_Word(PBC_Perms,{gap(old[field])})={actual});')
lines += [
 f'PBC_BasisVectors:={gap(adapt["basis_old_vectors"])};;',
 'PBC_Adapt:=List(PBC_BasisVectors,v->Product([1..176],i->PBC_Perms[i]^v[i]));;',
 'Assert(0,Group(PBC_Adapt)=G);',
 f'PBC_Powers:={gap(source["powers"])};;',
 f'PBC_Conjugates:={gap(source["conjugates"])};;',
 'for i in [1..176] do Assert(0,PBC_Adapt[i]^PBC_OldOrders[i]=PBC_Word(PBC_Adapt,PBC_Powers[i]));od;',
 'for a in PBC_Conjugates do Assert(0,PBC_Adapt[a[1]]^PBC_Adapt[a[2]]=PBC_Word(PBC_Adapt,a[3]));od;',
 'Print("adapted_pc_all_literal_permutation_clauses_PASS runtime ",Runtime(),"\\n");',
]
for field,actual in [('s','s'),('r','r'),('f','f'),('left_s_frame','bs^-1'),('left_r_frame','br^-1')]:
    lines.append(f'Assert(0,PBC_Word(PBC_Adapt,{gap(source[field])})={actual});')
for field,actual in [('s_image','s*f^-1'),('r_image','f*r')]:
    lines.append(f'Assert(0,PBC_Word(PBC_Adapt,{gap(source[field])})={actual});')
lines += [
 f'PBC_CS:=List({gap(source["s_centralizers"])},w->PBC_Word(PBC_Adapt,w));;',
 f'PBC_CR:=List({gap(source["r_centralizers"])},w->PBC_Word(PBC_Adapt,w));;',
 'Assert(0,ForAll(PBC_CS,g->g in Fg and Comm(g,s)=()));',
 'Assert(0,ForAll(PBC_CR,g->g in Fg and Comm(g,r)=()));',
 'Assert(0,bs in Fg and br in Fg);',
 'Assert(0,PBC_Adapt[1]=r and PBC_Adapt[2]=s);',
 'Assert(0,PBC_Adapt[7]=bs^-1 and PBC_Adapt[5]=br^-1);',
 'Print("marked_frames_and_pure_centralizers_PASS ",Length(PBC_CS)," ",Length(PBC_CR)," runtime ",Runtime(),"\\n");',
 'Print("FINITE_ONLY_SOURCE_REPLAY_PASS degree ",LargestMovedPoint(G)," generators ",Length(PBC_Adapt)," runtime ",Runtime(),"\\n");',
 'QUIT;'
]
out_g=HERE/'pbc_iterated_source_permutation_replay.g'
out_g.write_text('\n'.join(lines)+'\n')
out_log=HERE/'pbc_iterated_source_permutation_replay.out'
gap_exe=ROOT/'gap-runtime/gap-4.14.0/gap'
if not gap_exe.exists():
    candidates=list(ROOT.glob('gap*/gap-*/gap'))+list(ROOT.glob('gap*/gap'))
    gap_exe=next((p for p in candidates if p.is_file()),gap_exe)
assert gap_exe.exists(),str(gap_exe)
cmd=[str(gap_exe),'-q','-m','128m','-o','2g',str(out_g)]
t=time.time()
with out_log.open('wb') as out:
    result=subprocess.run(cmd,cwd=ROOT,stdout=out,stderr=subprocess.STDOUT)
log=out_log.read_text()
assert result.returncode==0 and 'FINITE_ONLY_SOURCE_REPLAY_PASS' in log,log[-3000:]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'status':'PASS','scope':'Actual finite permutation source and complete marked pc comparison only; no Schur calculation invoked',
 'degree':2592,'generators':176,'power_clauses_per_presentation':176,'conjugation_clauses_per_presentation':15400,
 's_pure_centralizers':71,'r_pure_centralizers':9,'elapsed_seconds':time.time()-t,
 'command':cmd,'inputs':{str(p.relative_to(HERE.parent)):sha(p) for p in (old_path,adapt_path,source_path,program_path)},
 'checker_sha256':sha(Path(__file__)),'generated_gap_sha256':sha(out_g),'stdout_sha256':sha(out_log)}
(HERE/'pbc_iterated_source_permutation_replay.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
