#!/usr/bin/env python3
"""Replay all finite target and frame equalities in the original G176."""
from pathlib import Path
import hashlib,json,subprocess,time
CODE=Path(__file__).resolve().parent;WORK=CODE.parents[1]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
source=CODE/'pbc_iterated_shortcut_v2_original_source.json';s=json.loads(source.read_text())
old=CODE/'pbc_top_two_section_positive_replay.g'
prefix=old.read_text().split('zero:=ListWithIdenticalEntries(176,0);;')[0]
assert prefix.count('pc:=function')==1 and 'POSITIVE_HALL' not in prefix
ss,rr=s['s'],s['r'];aa,bb=s['s_image'],s['r_image'];bs,br=s['left_s_frame'],s['left_r_frame']
pairs=[['target_s',bs+ss,aa+bs],['target_r',br+rr,bb+br],['target_product',aa+bb,ss+rr]]
pairs += [[f's_frame_{i+1}',w+ss,ss+w] for i,w in enumerate(s['s_centralizers'])]
pairs += [[f'r_frame_{i+1}',w+rr,rr+w] for i,w in enumerate(s['r_centralizers'])]
assert len(pairs)==83
gap=CODE/'pbc_top_two_cover_source_replay.g';out=gap.with_suffix('.out')
gap.write_text(prefix+'\nPBC_pairs:='+json.dumps(pairs,separators=(',',':'))+';;\n'+r'''
for row in PBC_pairs do
 Assert(0,pc(row[2])=pc(row[3]));
od;
Print("ACTUAL_ORIGINAL_TARGET_FRAME_EQUALITIES_VERIFIED ",Length(PBC_pairs)," runtime ",Runtime(),"\n");
QUIT;
''')
cmd=[str(WORK/'gap-runtime/gap-4.16.1/gap'),'-q','-m','128m','-o','2g',str(gap)]
start=time.time()
with out.open('w') as f:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT)
log=out.read_text();assert r.returncode==0 and 'ACTUAL_ORIGINAL_TARGET_FRAME_EQUALITIES_VERIFIED 83' in log
assert 'Error,' not in log
report=dict(status='PASS',source_sha256=sha(source),generator_sha256=sha(__file__),
            finite_source_pairs=len(pairs),target_pairs=3,s_frame_pairs=71,r_frame_pairs=9,
            gap_program_sha256=sha(gap),gap_output_sha256=sha(out),gap_command=cmd,seconds=time.time()-start,
            scope='Actual finite source equalities only; they justify that the evaluated discrepancies lie in the central cover kernel.')
(CODE/'pbc_top_two_cover_source_replay.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
