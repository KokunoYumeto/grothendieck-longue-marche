"""Exact source proposals authorized by root sections 01, 02 and 03 only."""
from pathlib import Path
import copy, hashlib, json, re, runpy, sys
sys.dont_write_bytecode=True
BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
sha=lambda b:hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
dump=lambda v:(json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
def save(name,value,raw=False):
 assert name.startswith('scan026_source_') and '/' not in name
 b=value if raw else dump(value);p=OUT/name
 if p.exists():assert p.read_bytes()==b,('immutable output differs',name)
 else:p.write_bytes(b)
 return {'path':'out/checks/'+name,'sha256':sha(b),'bytes':len(b)}
def load(path):return json.loads((BASE/path).read_bytes())

captures={}
for kind,suffix in [('decisions','json'),('journal','md')]:
 original=f'out/checks/scan026_root_{kind}.{suffix}'
 name=f'scan026_source_authority_sections01_03_root_{kind}_v01.{suffix}'
 p=OUT/name
 if not p.exists():save(name,(BASE/original).read_bytes(),True)
 b=p.read_bytes()
 captures[kind]={'path':'out/checks/'+name,'sha256':sha(b),'bytes':len(b),'original_root_path':original,'capture_scope':'Complete root-file bytes at capture; this proposal uses sections 01–03 only.'}

D=(BASE/captures['decisions']['path']).read_text();J=(BASE/captures['journal']['path']).read_text();decisions=json.loads(D)
actual=load('out/checks/scan026_root_decisions.json')
selected={d['section']:d for d in decisions['decisions'] if d['section'] in ['01','02','03']}
assert list(selected)==['01','02','03']
assert all(next(d for d in actual['decisions'] if d['section']==s)==v for s,v in selected.items())
H=list(re.finditer(r'^## (\d\d) — .+$',J,re.M));sections={}
for i,m in enumerate(H):
 if m.group(1) in selected:sections[m.group(1)]=(m.start(),H[i+1].start() if i+1<len(H) else len(J))
assert set(sections)==set(selected)
for s,(a,b) in sections.items():assert selected[s]['body'] in J[a:b]

helper=runpy.run_path(str(OUT/'scan026_source_splice.py'));exact=helper['exact']
def root_ref(kind,a,b,pointer=None):
 c=captures[kind];text=D if kind=='decisions' else J
 r=exact(c['path'],text,a,b)
 r.update(original_root_path=c['original_root_path'],original_root_sha256_at_capture=c['sha256'])
 if pointer is not None:r['original_json_pointer']=pointer
 return r
json_decoder=json.JSONDecoder();start=D.index('[',D.index('"decisions"'))+1;decision_spans={};idx=0
while True:
 while D[start] in ' \r\n\t,':start+=1
 if D[start]==']':break
 value,end=json_decoder.raw_decode(D,start)
 if value['section'] in selected:decision_spans[value['section']]=(idx,start,end)
 start=end;idx+=1
auth={}
for s in selected:
 i,a,b=decision_spans[s];ja,jb=sections[s]
 auth[s]=[root_ref('decisions',a,b,f'/decisions/{i}'),root_ref('journal',ja,jb)]

T={w:(BASE/f'out/readers/026/{w}/reading.tex').read_text() for w in 'ABC'}
M={w:load(f'out/readers/026/{w}/source_map.json') for w in 'ABC'}
smA=next(g for g in M['A']['local_groups'] if g['id']=='A026-S01')
efam=next(g for g in M['B']['source_groups'] if g['id']=='B026-EFAM')
assert sha(T['A'])=='c5079dace4d580a4695749bb745d382e3828681f98e8c037785fc6ac985b5513'
assert sha(T['B'])=='1c36f765e58e84962435ac4afe055eb55e561b9f6927f8d09cc139d0562e7289'
old=r'\unsure{\mathcal E|\mathscr E|\varepsilon}'
assert T['A'].count(old)==1;a=T['A'].index(old);b=a+len(old)
donor=exact('out/readers/026/B/reading.tex',T['B'],efam['start_char'],efam['end_char'])
assert donor['literal']==efam['literal_source'] and sha(donor['literal'])==efam['source_sha256']
assert selected['03']['locus_decisions']['L003']['assembly']=="Replace A's single family-alphabet unsure macro with exact B026-EFAM source group; retain its full candidate qualification and local hand scope."
plan={'scope':'Only root sections 01–03. L001/L002/S01 keep exact A; L003 imports exact B026-EFAM.',
 'base':{'path':'out/checks/scan026_source_A_spine_v01.tex','sha256':sha(T['A'])},
 'edits':[{'edit_id':'E026-03-L003-EFAM','base_char_start':a,'base_char_end':b,'before':old,
 'root_authority_refs':auth['03'],'replacement_pieces':[{'source':donor}],
 'root_locus':'L003','root_section':'03','main_approved':False}]}
plan_file=save('scan026_source_sections01_03_plan_v01.json',plan)
result=helper['stage'](plan,'scan026_source_sections01_03_proposal_v01')
proposal=Path(result['proposal_path']).read_text();mapping=json.loads(Path(result['map_path']).read_bytes())
edit=mapping['literal_replacements'][0];shift=len(donor['literal'])-len(old)
assert proposal[:a]==T['A'][:a] and proposal[a+len(donor['literal']):]==T['A'][b:]
assert proposal[smA['source_char_start']:smA['source_char_end_exclusive']]==smA['source_excerpt']
assert proposal.count(smA['source_excerpt'])==1 and proposal.count(efam['literal_source'])==1

# Literal command bindings: all A commands retain their exact original text;
# exactly the three commands of the complete donor group are inserted.
catalog=load('out/checks/scan026_source_state_catalog_v01.json');commands=[]
for cmd in catalog['literal_source_commands']:
 w=cmd['reader'];s=cmd['exact_source'];ca,cb=s['char_start'],s['char_end']
 if w=='A':
  assert cb<=a or ca>=b,('A command overlaps replaced non-graphical alphabet macro',cmd['command_id'])
  pa,pb=(ca,cb) if cb<=a else (ca+shift,cb+shift)
 elif w=='B' and efam['start_char']<=ca and cb<=efam['end_char']:
  pa,pb=a+ca-efam['start_char'],a+cb-efam['start_char']
 else:continue
 literal=T[w][ca:cb];assert proposal[pa:pb]==literal
 commands.append({'original_command_id':cmd['command_id'],'reader':w,'donor_source':copy.deepcopy(s),
  'proposal_source':exact('out/checks/scan026_source_sections01_03_proposal_v01.tex',proposal,pa,pb),
  'root_authority_refs':auth['03'] if w=='B' else [],'status':'Exact donor bytes present; no ink or metric validation by source helper.'})
assert len([x for x in commands if x['reader']=='A'])==374
assert len([x for x in commands if x['reader']=='B'])==3

def without_comments(text):
 lines=[]
 for line in text.splitlines(keepends=True):
  cut=None
  for i,ch in enumerate(line):
   if ch!='%':continue
   j=i-1
   while j>=0 and line[j]=='\\':j-=1
   if (i-j-1)%2==0:cut=i;break
  lines.append(line if cut is None else line[:cut]+('\n' if line.endswith('\n') else ''))
 return ''.join(lines)
clean=without_comments(proposal);stack=[]
for i,ch in enumerate(clean):
 j=i-1
 while j>=0 and clean[j]=='\\':j-=1
 if (i-j-1)%2:continue
 if ch=='{':stack.append(i)
 elif ch=='}':assert stack;stack.pop()
assert not stack
env=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
 if m.group(1)=='begin':env.append(m.group(2))
 else:assert env.pop()==m.group(2)
assert not env
assert len(re.findall(r'(?<!\\)\$',clean))%2==0
assert clean.count(r'\[')==clean.count(r'\]')
for m in re.finditer(r'\\\[([\s\S]*?)\\\]',proposal):assert not re.search(r'\n[ \t]*\n',m.group(1))

union=load('out/checks/scan026_source_union_v01.json');slots=load('out/checks/scan026_source_record_scaffold_v01.json')['pending_decision_slots']
bindings=[]
for section,locus in [('01','L001'),('02','L002'),('03','S01'),('03','L003')]:
 root=selected[section]['locus_decisions'][locus]
 if locus=='L001':literal=root['reading'];start=proposal.index(literal);end=start+len(literal);source_group=None
 elif locus=='L002':literal=root['reading'];start=proposal.index(literal);end=start+len(literal);source_group=None
 elif locus=='S01':start,end=smA['source_char_start'],smA['source_char_end_exclusive'];source_group='A026-S01'
 else:start,end=edit['proposal_char_start'],edit['proposal_char_end'];source_group='B026-EFAM'
 slot=next(x for x in slots if x['source_locus_id']==locus)
 chosen={'complete_candidates':copy.deepcopy(smA['complete_candidates']),'hand':copy.deepcopy(smA['hand']),'role':copy.deepcopy(smA['role'])} if locus=='S01' else ({k:copy.deepcopy(efam[k]) for k in ['reading','candidates','role','hand','qualifier_printed','coordinate_map','native_units','full_origin']} if locus=='L003' else {'exact_root_reading':root['reading'],'root_hand':root['hand']})
 bindings.append({'source_locus_id':locus,'root_section':section,'exact_root_locus_value':copy.deepcopy(root),
  'root_authority_refs':auth[section],'selected_source_group':source_group,'selected_complete_state_fields':chosen,
  'proposal_source':exact('out/checks/scan026_source_sections01_03_proposal_v01.tex',proposal,start,end),
  'all_three_raw_reader_states':copy.deepcopy(slot['reader_source_bundles']),
  'C_source_row_ids':copy.deepcopy(slot['C_source_row_ids']),'C_source_part_ids':copy.deepcopy(slot['C_source_part_ids']),
  'C_status_from_root':selected[section].get('original_C_rows',{}),'diff_C':None,'diff_H':None,'physical_count_parent':None,'marked_in_H':None,
  'count_and_local_H_flag_status':'Pending explicit root scalar/source-audit authority; no helper choice.',
  'root_ink_choice_applied_to_proposal':True,'main_approved':False})
records=save('scan026_source_sections01_03_record_proposal_v01.json',{'scope':'Four local bindings from root sections 01–03 only; unselected reader states remain frozen. Public record/count closure is pending.','bindings':bindings})
command_file=save('scan026_source_sections01_03_command_bindings_v01.json',commands)
audit={'scope':'Source-only proposal for root §§01–03; no section04 or later applied.',
 'authority_captures':captures,'exact_A_spine_sha256':sha(T['A']),'proposal_sha256':sha(proposal),
 'literal_replacements':1,'B_EFAM_full_group_exact':True,'A_S01_entire_group_exact':True,
 'all_A_bytes_outside_single_macro_unchanged':True,'forward_and_inverse_restore_exact_A':mapping['forward_and_inverse_restore_exact_A_bytes'],
 'preserved_A_literal_commands':374,'inserted_exact_B_literal_commands':3,
 'source_braces_balanced':True,'source_environment_stack_balanced':True,'math_delimiters_balanced':True,'physical_blank_paragraphs_outside_displays':True,
 'new_candidate_choices':0,'new_count_or_H_flag_choices':0,'root_or_final_files_written':0,'image_bytes_read':0,
 'main_approved':False,'artifacts':[plan_file,records,command_file,result],
 'limitations':'Literal source and attachment checks only; no rendering, metric comparison, image viewing or mathematical check.'}
save('scan026_source_sections01_03_audit_v01.json',audit)
print(json.dumps(audit,ensure_ascii=False,indent=2))
