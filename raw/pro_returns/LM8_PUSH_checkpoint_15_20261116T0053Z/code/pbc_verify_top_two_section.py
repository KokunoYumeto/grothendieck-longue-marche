#!/usr/bin/env python3
"""Replay the proposed Hall-three subgroup and normalizer in actual GAP G176."""
from pathlib import Path
import hashlib,json,subprocess,time
CODE=Path(__file__).resolve().parent;WORK=CODE.parents[1]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
compact=lambda v:json.dumps(v,separators=(',',':'))
source=CODE/'pbc_iterated_shortcut_v2_original_source.json';s=json.loads(source.read_text())
section=CODE/'pbc_top_two_section.json';a=json.loads(section.read_text())
assert a['source_sha256']==sha(source)
words=[]
for i in range(1,105):
    v=int(a['quotient_generator_corrections_hex'][str(i)],16)
    words.append([i,1]+[x for k in range(72) if v>>k&1 for x in (105+k,1)])
data=dict(orders=s['relative_orders'],powers=s['powers'],conjugates=s['conjugates'],section=words)
gap=CODE/'pbc_top_two_section_original_replay.g';out=gap.with_suffix('.out')
gap.write_text('LoadPackage("polycyclic");;\nD:=rec('+','.join(k+':='+compact(v) for k,v in data.items())+');;\n'+r'''
col:=FromTheLeftCollector(176);;
for i in [1..176] do SetRelativeOrder(col,i,D.orders[i]);SetPower(col,i,D.powers[i]);od;
for row in D.conjugates do SetConjugate(col,row[1],row[2],row[3]);od;
UpdatePolycyclicCollector(col);;
G:=PcpGroupByCollectorNC(col);;gs:=Igs(G);;
ev:=function(w) local z,k;z:=One(G);for k in [1,3..Length(w)-1] do z:=z*gs[w[k]]^w[k+1];od;return z;end;;
hs:=List(D.section,ev);;
evs:=function(w) local z,k;z:=One(G);for k in [1,3..Length(w)-1] do if w[k]<=104 then z:=z*hs[w[k]]^w[k+1];fi;od;return z;end;;
for i in [87..104] do Assert(0,hs[i]^3=One(G));od;
for i in [87..104] do for j in [87..i-1] do Assert(0,Comm(hs[i],hs[j])=One(G));od;od;
Print("ACTUAL_HALL_THREE_LIFTS_VERIFIED 18 powers 153 commutators runtime ",Runtime(),"\n");
ct:=0;;
for row in D.conjugates do
 if row[1]>=87 and row[1]<=104 and row[2]<=86 then
  Assert(0,hs[row[1]]^hs[row[2]]=evs(row[3]));ct:=ct+1;
 fi;
od;
Print("ACTUAL_NORMALIZER_LIFTS_VERIFIED ",ct," runtime ",Runtime(),"\n");
# These additional checks are redundant for the normalizer proof, and make
# the actual quotient section directly inspectable in every original relator.
for i in [1..104] do Assert(0,hs[i]^D.orders[i]=evs(D.powers[i]));od;
ct:=0;;
for row in D.conjugates do
 if row[1]<=104 then Assert(0,hs[row[1]]^hs[row[2]]=evs(row[3]));ct:=ct+1;fi;
od;
Print("ACTUAL_SECTION_ALL_RELATORS_VERIFIED 104 powers ",ct," conjugates runtime ",Runtime(),"\n");
QUIT;
''')
cmd=[str(WORK/'gap-runtime/gap-4.16.1/gap'),'-q','-m','128m','-o','2g',str(gap)]
start=time.time()
with out.open('w') as f:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT)
log=out.read_text();assert r.returncode==0 and 'ACTUAL_SECTION_ALL_RELATORS_VERIFIED 104 powers 5356 conjugates' in log
assert 'Error,' not in log
result=dict(status='PASS',source_sha256=sha(source),section_sha256=sha(section),
            generator_sha256=sha(__file__),gap_program_sha256=sha(gap),gap_output_sha256=sha(out),
            original_section_power_relators=104,original_section_conjugate_relators=5356,
            normalizer_relators=18*86,gap_command=cmd,seconds=time.time()-start,
            scope='Actual section only. No central-cover target values or full C31 conclusion.')
(CODE/'pbc_top_two_section_original_replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
