#!/usr/bin/env python3
"""Independent positive-word GAP verification of every section relation.

Uses the actual finite pc presentation directly, without constructing all
inverse collector tables. All tested equalities involve only positive words.
"""
from pathlib import Path
import hashlib,json,subprocess,time
CODE=Path(__file__).resolve().parent;WORK=CODE.parents[1]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
compact=lambda v:json.dumps(v,separators=(',',':'))
source=CODE/'pbc_iterated_shortcut_v2_original_source.json';s=json.loads(source.read_text())
section=CODE/'pbc_top_two_section.json';a=json.loads(section.read_text());assert a['source_sha256']==sha(source)
words=[]
for i in range(1,105):
    v=int(a['quotient_generator_corrections_hex'][str(i)],16)
    words.append([i,1]+[x for k in range(72) if v>>k&1 for x in (105+k,1)])
data=dict(orders=s['relative_orders'],powers=s['powers'],conjugates=s['conjugates'],section=words)
gap=CODE/'pbc_top_two_section_positive_replay.g';out=gap.with_suffix('.out')
gap.write_text('LoadPackage("polycyclic");;\nD:=rec('+','.join(k+':='+compact(v) for k,v in data.items())+');;\n'+r'''
col:=FromTheLeftCollector(176);;
for i in [1..176] do SetRelativeOrder(col,i,D.orders[i]);SetPower(col,i,D.powers[i]);od;
for row in D.conjugates do SetConjugate(col,row[1],row[2],row[3]);od;
col![PC_COMMUTE]:=ListWithIdenticalEntries(176,176);;
SetFilterObj(col,IsUpToDatePolycyclicCollector);
pc:=function(w) local v;v:=ListWithIdenticalEntries(176,0);
 while CollectWordOrFail(col,v,w)=fail do v:=ListWithIdenticalEntries(176,0);od;return v;end;;
evs:=function(w) local v,k,j;v:=[];
 for k in [1,3..Length(w)-1] do if w[k]<=104 then
  for j in [1..w[k+1]] do Append(v,D.section[w[k]]);od;
 fi;od;return v;end;;
zero:=ListWithIdenticalEntries(176,0);;
for i in [87..104] do Assert(0,pc(Concatenation(D.section[i],D.section[i],D.section[i]))=zero);od;
for i in [87..104] do for j in [87..i-1] do
 Assert(0,pc(Concatenation(D.section[i],D.section[j]))=pc(Concatenation(D.section[j],D.section[i])));
od;od;
Print("POSITIVE_HALL_THREE_VERIFIED 18 powers 153 commutators runtime ",Runtime(),"\n");
ct:=0;;
for row in D.conjugates do
 if row[1]>=87 and row[1]<=104 and row[2]<=86 then
  Assert(0,pc(Concatenation(D.section[row[1]],D.section[row[2]]))=
   pc(Concatenation(D.section[row[2]],evs(row[3]))));ct:=ct+1;
 fi;
od;
Print("POSITIVE_NORMALIZER_VERIFIED ",ct," runtime ",Runtime(),"\n");
for i in [1..104] do Assert(0,pc(evs([i,D.orders[i]]))=pc(evs(D.powers[i])));od;
ct:=0;;
for row in D.conjugates do
 if row[1]<=104 then
  Assert(0,pc(Concatenation(D.section[row[1]],D.section[row[2]]))=
   pc(Concatenation(D.section[row[2]],evs(row[3]))));ct:=ct+1;
 fi;
od;
Print("POSITIVE_SECTION_ALL_RELATORS_VERIFIED 104 powers ",ct," conjugates runtime ",Runtime(),"\n");
QUIT;
''')
cmd=[str(WORK/'gap-runtime/gap-4.16.1/gap'),'-q','-m','128m','-o','2g',str(gap)]
start=time.time()
with out.open('w') as f:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT)
log=out.read_text();assert r.returncode==0 and 'POSITIVE_SECTION_ALL_RELATORS_VERIFIED 104 powers 5356 conjugates' in log
assert 'Error,' not in log
result=dict(status='PASS',source_sha256=sha(source),section_sha256=sha(section),
            generator_sha256=sha(__file__),gap_program_sha256=sha(gap),gap_output_sha256=sha(out),
            actual_positive_power_relators=104,actual_positive_conjugate_relators=5356,
            actual_normalizer_relators=18*86,gap_command=cmd,seconds=time.time()-start,
            scope='Actual section only. No central-cover target values or full C31 conclusion.')
(CODE/'pbc_top_two_section_positive_replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
