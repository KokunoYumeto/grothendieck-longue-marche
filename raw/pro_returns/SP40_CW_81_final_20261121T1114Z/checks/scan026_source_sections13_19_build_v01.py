"""Cumulative, reversible source proposal through root section19."""
from pathlib import Path
import copy,difflib,json,re,runpy,sys
sys.dont_write_bytecode=True
BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
api=runpy.run_path(str(OUT/'scan026_source_authority_tools.py'));save=api['save'];sha=api['sha']
captures,root,auth,helper=api['capture']('sections13_19_v01',[f'{n:02d}' for n in range(13,20)])
exact=helper['exact'];pack=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'))
T={w:(BASE/f'out/readers/026/{w}/reading.tex').read_text() for w in 'ABC'}
M={w:json.loads((BASE/f'out/readers/026/{w}/source_map.json').read_bytes()) for w in 'ABC'}
G={w:{g['id']:g for g in M[w][{'A':'local_groups','B':'source_groups','C':'groups'}[w]]} for w in 'ABC'}
oldplan=json.loads((OUT/'scan026_source_sections01_12_plan_v01.json').read_bytes());edits=copy.deepcopy(oldplan['edits'])
selected={};donor_mutations=[]
def gtext(w,gid):
 g=G[w][gid]
 if w=='A':a,b=g['source_char_start'],g['source_char_end_exclusive'];literal=g['source_excerpt']
 elif w=='B':a,b=g['start_char'],g['end_char'];literal=g['literal_source']
 else:a,b=g['source_span']['start_character'],g['source_span']['end_character_exclusive'];literal=g['source_exact']
 assert T[w][a:b]==literal
 return literal,exact(f'out/readers/026/{w}/reading.tex',T[w],a,b)
def replace_once(text,old,new,changes,purpose):
 assert text.count(old)==1,(purpose,old,text.count(old));a=text.index(old)
 changes.append({'start':a,'old':old,'new':new,'purpose':purpose})
 return text[:a]+new+text[a+len(old):]
def insert_at(text,a,new,changes,purpose):
 changes.append({'start':a,'old':'','new':new,'purpose':purpose});return text[:a]+new+text[a:]
def inverse_changes(text,changes):
 for change in reversed(changes):
  a=change['start'];assert text[a:a+len(change['new'])]==change['new'];text=text[:a]+change['old']+text[a+len(change['new']):]
 return text
def comment_value(text,values,changes,purpose):
 a=text.index('% complete candidates: ');b=text.index('\n',a)
 return replace_once(text,text[a:b],'% complete candidates: '+json.dumps(values,ensure_ascii=False),changes,purpose)
def add(eid,a,b,new,sections,purpose,donors=(),changes=()):
 refs=[r for section in sections for r in auth[section]]
 edits.append({'edit_id':eid,'base_char_start':a,'base_char_end':b,'before':T['A'][a:b],
  'root_sections':sections,'root_authority_refs':refs,'replacement_pieces':[{'literal':new,'purpose':purpose,'root_authority_refs':refs}],
  'exact_donor_sources':list(donors),'bounded_donor_changes':list(changes),'main_approved':False})
def add_group(gid,new,sections,purpose,donors=(),changes=()):
 g=G['A'][gid];add('E026-'+sections[-1]+'-'+gid,g['source_char_start'],g['source_char_end_exclusive'],new,sections,purpose,donors,changes)
def literal_in_A(old,new,section,eid,purpose,within=None,donors=()):
 a,b=(0,len(T['A'])) if within is None else within
 hits=[a+m.start() for m in re.finditer(re.escape(old),T['A'][a:b])];assert len(hits)==1,(eid,hits)
 add(eid,hits[0],hits[0]+len(old),new,[section],purpose,donors)

# §13: exact B drawing commands, specified root comments and qualifier wrapper.
diagram,diagram_source=gtext('B','B026-DIAG');original_diagram=diagram;changes=[]
diagram=replace_once(diagram,'% Crossed label candidates: deleted E | deleted B | deleted Sigma.','% Root crossed label candidates: deleted B | deleted E | deleted Sigma.',changes,'Root ordered cancelled-letter states only.')
diagram=replace_once(diagram,r'\unsure{$E$|$B$|$\Sigma$}',r'\unsure{$B$|$E$|$\Sigma$}',changes,'Same root letter order in the invisible crossed-label annotation.')
diagram=replace_once(diagram,'% Lower E candidates: E_alpha | E with hooked lower-arm return; the shared stroke is drawn once.','% Root E states: '+root['13']['locus_decisions']['L017']['reading']+'; the shared stroke is drawn once.',changes,'Four exact root E states; literal E drawing unchanged.')
codec_comments=(OUT/'scan026_source_diagram96_comments_v01.txt').read_text()
diagram=insert_at(diagram,diagram.index(r'\reversemarginpar'),codec_comments,changes,'Complete finite 96-tuple component codec in source comments.')
diagram=replace_once(diagram,r'\margin{',r'\margin{\unsure{',changes,'Root in-place diagram qualification inside the margin.')
diagram=insert_at(diagram,diagram.index(r'\normalmarginpar'),'}',changes,'Close only the root diagram qualifier; existing margin placement stays.')
assert inverse_changes(diagram,changes)==original_diagram
add_group('A026-D01',diagram,['13'],'Complete B026-DIAG literal drawing with root ordered state annotations and wrapper.',[diagram_source],changes)
donor_mutations.append({'group':'B026-DIAG','original_source':diagram_source,'changes':changes,'inverse_exact_original':True})

# Exact ring expansion preserves each complete A field except its reading token.
ring_states={};ring_sources={};ring_changes={}
for gid,section in [('A026-S09','14'),('A026-S10','16'),('A026-S11','16'),('A026-S12','16'),('A026-S13','17')]:
 original=G['A'][gid]['complete_candidates'];values=[];maps=[]
 for head_index,candidate in enumerate(original):
  for ring in ['0',r'\circ','o']:
   item=copy.deepcopy(candidate);old=item['reading'];assert old.count(r'\alpha,0}')==1
   item['reading']=old.replace(r'\alpha,0}',r'\alpha,'+ring+'}',1)
   assert all(pack(item[k])==pack(candidate[k]) for k in item if k!='reading')
   values.append(item);maps.append({'original_candidate_index':head_index,'ring':ring,'old_reading':old,'new_reading':item['reading']})
  assert values[-3]==candidate
 text,source=gtext('A',gid);changes=[]
 text=comment_value(text,values,changes,'Complete ordered head/oval states with original local fields intact.')
 text=replace_once(text,r'{$\alpha,0$}',r'{$\alpha,\unsure{0|\circ|o}$}',changes,'Only the visible oval gets the root three-way qualifier.')
 # Match the only phantom node containing this group's primary full glyph.
 lines=[line for line in text.splitlines() if r'\node[overlay' in line and r'\phantom' in line and r'\alpha,0}' in line]
 assert len(lines)==1,(gid,lines)
 oldline=lines[0];newline=oldline.replace(r'\alpha,0}',r'\alpha,\unsure{0|\circ|o}}',1)
 text=replace_once(text,oldline,newline,changes,'Same oval qualifier in this exact phantom annotation; roof/body/index syntax remains literal.')
 assert inverse_changes(text,changes)==source['literal']
 ring_states[gid]={'original_complete_candidates':copy.deepcopy(original),'exact_selected_candidates':values,'ordered_reading_maps':maps,'root_authority_refs':auth[section]}
 ring_sources[gid]=text;ring_changes[gid]=changes
 if gid!='A026-S09':add_group(gid,text,[section],'Preserve every literal geometry path and expand only the recorded oval states.',[source],changes)

# §15 copied coordinate map: A S09, converted-unit B arc, independent root fleck.
arc,arc_source=gtext('B','B026-M03');arc_original=arc;arc_changes=[]
assert arc.count('0.085mm')==4
for old,new in [('x=0.085mm, y=-0.085mm','x=0.10mm, y=-0.10mm'),('x=0.085mm,y=-0.085mm','x=0.10mm,y=-0.10mm')]:
 arc=replace_once(arc,old,new,arc_changes,'Root §15 local unit map 0.085mm to0.10mm, factor20/17; coordinates and line widths unchanged.')
assert inverse_changes(arc,arc_changes)==arc_original
placement=root['15']['assembly']['main_composite']
assert placement['origin']==[440,1222] and placement['baseline_full_y']==1295
assert placement['S09_anchor']==[33,73] and placement['M03_anchor']==[0,93]
assert placement['L052_center']==[128,106] and placement['L052_native_radii']==[1.3,1.5]
fleck=r'''% BEGIN R026-L052
% Root section14 only: approximate native center (568,1328), radii (1.3,1.5); all interpretive fields undetermined.
\unsure{\tikz[x=0.10mm,y=-0.10mm,baseline=(b)]{
\path[use as bounding box] (-1.3,-1.5) rectangle (1.3,1.5);
\coordinate (b) at (0,0);
\fill[gray] (0,0) ellipse (1.3 and 1.5);
}}
% END R026-L052
'''
composite=(r'''% BEGIN R026-GMAIN
% Root section15 copied native map: x=.10mm*(native_x-440), y=-.10mm*(native_y-1222), baseline native y1295.
% B M03 units only: .085mm to .10mm, recorded factor20/17. The old coordinate values and line widths remain unchanged.
% The display bounding rectangle (0,0)-(174,110) contains all declared child rectangles and the independently placed root fleck; it is not an ink-boundary claim.
\mathord{\begin{tikzpicture}[x=0.10mm,y=-0.10mm,baseline=(base)]
\coordinate (base) at (0,73);
\path[use as bounding box] (0,0) rectangle (174,110);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (33,73) {$
'''+ring_sources['A026-S09']+r'''$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,93) {$
'''+arc+r'''
$};
\node[anchor=center,inner sep=0pt,outer sep=0pt] at (128,106) {$
'''+fleck+r'''$};
\end{tikzpicture}}
% END R026-GMAIN
''')
ma,sg=G['A']['A026-M01'],G['A']['A026-S09'];assert ma['source_char_end_exclusive']==sg['source_char_start']
add('E026-15-main-composite',ma['source_char_start'],sg['source_char_end_exclusive'],composite,['14','15'],
 'Root common native-coordinate composite; same A S09 geometry, complete B arc and independent root L052 once.',
 [gtext('A','A026-S09')[1],arc_source],
 [{'group':'A026-S09','changes':ring_changes['A026-S09']},{'group':'B026-M03','changes':arc_changes},{'new_root_mark':'L052','sole_ink_authority':'14','literal_source':fleck}])
selected['main_composite']={'exact_root_coordinate_map':copy.deepcopy(placement),'source_bounding_rectangle':[0,0,174,110],
 'bounds_scope':'Display bookkeeping only; extra outside space introduces no mark.',
 'L052_display_colour':'gray','L052_colour_scope':'Literal display convention for the root-described faint mark; no measured shade or pixel match claimed.',
 'source_ownership':['A026-S09 once','B026-M03 once','R026-L052 once'],'root_authority_refs':auth['14']+auth['15']}

# §17: eighteen explicit upper-pair/head states with candidate-local hand fields.
original14=G['A']['A026-S14']['complete_candidates'];assert len(original14)==9
states14=[];map14=[]
for i,base in enumerate(original14):
 for head in ['head/retrace','independent upper run']:
  item=copy.deepcopy(base);item['reading']=base['reading']+' with '+head
  item['hand']={'body_upper_pair_low_comma':'his hand','short_upper_run':'his hand' if head=='head/retrace' else 'undetermined hand'}
  item['root_upper_run_role']=head
  item['original_A_candidate_index']=i
  states14.append(item);map14.append({'original_candidate_index':i,'root_head_role':head,'original_hand':copy.deepcopy(base['hand']),'selected_hand':copy.deepcopy(item['hand'])})
  assert item['role']==base['role'] and item['attachment']==base['attachment'] and base['reading'].endswith(',')
assert len(states14)==18
s14,source14=gtext('A','A026-S14');changes14=[];s14=comment_value(s14,states14,changes14,'Root nine upper-pair states by two explicit head-role states; baseline comma stays in every reading.')
assert inverse_changes(s14,changes14)==source14['literal']
add_group('A026-S14',s14,['17'],'Only complete state metadata changes; all S14 paths and low comma remain exact.',[source14],changes14)
selected['S14']={'original_A_candidates':original14,'exact_root_candidates':states14,'explicit_field_maps':map14,'root_hand_scope_quote':'The independent short upper run alone has undetermined hand in that candidate; body, upper pair and low comma are his hand.','root_authority_refs':auth['17']}

# Complete B word/flecks group, complete two-stroke group, and exact C word/mark scopes.
peut,peut_source=gtext('B','B026-GPEUT');at=T['A'].index('ne peut être')+3
assert T['A'][at:at+4]=='peut';add('E026-17-peut',at,at+4,peut,['17'],'Complete B026-GPEUT including B026-M04 exactly once.',[peut_source])
etre=r'\unsure{être|etre}';assert T['C'].count(etre)==1;cs=T['C'].index(etre)
literal_in_A('être',etre,'17','E026-17-etre','Exact C accent qualifier only.',within=(at,at+50),donors=[exact('out/readers/026/C/reading.tex',T['C'],cs,cs+len(etre))])
atwo,atwo_source=gtext('B','B026-ATWO');atwo_old=atwo;changes_atwo=[]
atwo=replace_once(atwo,'% selected reading: à primary; colon alternative','% root selected reading: colon primary; à alternative',changes_atwo,'Root primary order only.')
atwo=replace_once(atwo,'% complete candidates: à || :','% root complete candidates: : || à',changes_atwo,'Root complete candidate order; original B order remains frozen.')
assert inverse_changes(atwo,changes_atwo)==atwo_old
literal_in_A('à',atwo,'17','E026-17-atwo','Exact B two-stroke source with root comment order only.',within=(at,at+50),donors=[atwo_source])
cmark,cmark_source=gtext('C','C026-M02');ca=cmark_source['char_start'];cb=cmark_source['char_end']
frame_start=T['C'].rfind(r'$\underset{\text{',0,ca);closing=r'}}{\text{un}}$';frame_end=T['C'].index(closing,cb)+len(closing)
assert frame_start>=0;un_frame=T['C'][frame_start:frame_end];assert un_frame.count(cmark)==1
u=T['A'].index('est un ouvert')+4;assert T['A'][u:u+2]=='un'
add('E026-17-un-marks',u,u+2,un_frame,['17'],'Complete original C underset construction, un and four mark components once.',[exact('out/readers/026/C/reading.tex',T['C'],frame_start,frame_end)])
selected['imports']={'B026-GPEUT':peut_source,'B026-ATWO':{'source':atwo_source,'comment_changes':changes_atwo},'C026-M02_complete_un_frame':exact('out/readers/026/C/reading.tex',T['C'],frame_start,frame_end)}

# §19 preserves A complete pair placement and all local child groups.
pair,pair_source=gtext('A','A026-G08');pair_old=pair;pair_changes=[]
start=pair.index('% complete candidates: ');end=pair.index('\n',start)
pair_codec=(OUT/'scan026_source_pair16_comments_v01.txt').read_text()
pair=replace_once(pair,pair[start:end],pair_codec.rstrip('\n'),pair_changes,'Exact complete 16-tuple parent codec; original A parent fields remain provenance.')
pair=replace_once(pair,r'{\deleted{\unsure{distinctes}}}',r'{\deleted{distinctes}}',pair_changes,'Only the selected visible distinctes qualifier is removed; deletion remains.')
assert inverse_changes(pair,pair_changes)==pair_old
add_group('A026-G08',pair,['19'],'Complete A pair arrangement with exact root sixteen-state parent codec and resolved cancelled word.',[pair_source],pair_changes)

plan={'scope':'Cumulative source proposal through root §19 only. All original reader inputs remain frozen.',
 'base':copy.deepcopy(oldplan['base']),'edits':edits,'previous_plan':{'path':'out/checks/scan026_source_sections01_12_plan_v01.json','sha256':sha((OUT/'scan026_source_sections01_12_plan_v01.json').read_bytes())},
 'state_codecs':{'diagram':'out/checks/scan026_source_diagram96_codec_v01.json','pair':'out/checks/scan026_source_pair16_codec_v01.json'},
 'root_count_and_marker_booleans':'Not chosen by this source proposal.'}
plan_file=save('scan026_source_sections01_19_plan_v01.json',plan)
result=helper['stage'](plan,'scan026_source_sections01_19_proposal_v01');P=Path(result['proposal_path']).read_text();mapping=json.loads(Path(result['map_path']).read_bytes())

# Verify each imported whole B primitive drawing command remains byte-identical.
catalog=json.loads((OUT/'scan026_source_state_catalog_v01.json').read_bytes());primitive=[]
for group_id,new_text in [('B026-DIAG',diagram),('B026-M03',arc),('B026-GPEUT',peut),('B026-ATWO',atwo)]:
 original,source=gtext('B',group_id);a,b=source['char_start'],source['char_end']
 for cmd in catalog['literal_source_commands']:
  s=cmd['exact_source']
  if cmd['reader']=='B' and cmd['command']!='node' and a<=s['char_start'] and s['char_end']<=b:
   literal=T['B'][s['char_start']:s['char_end']]
   assert original.count(literal)==new_text.count(literal),(group_id,cmd['command_id'])
   primitive.append({'group':group_id,'command_id':cmd['command_id'],'exact_original_source':s,'same_occurrence_count':original.count(literal)})

def clean_source(text):
 lines=[]
 for line in text.splitlines(keepends=True):
  for i,ch in enumerate(line):
   if ch!='%':continue
   j=i-1
   while j>=0 and line[j]=='\\':j-=1
   if (i-j-1)%2==0:line=line[:i]+('\n' if line.endswith('\n') else '');break
  lines.append(line)
 return ''.join(lines)
clean=clean_source(P);braces=[]
for i,ch in enumerate(clean):
 j=i-1
 while j>=0 and clean[j]=='\\':j-=1
 if (i-j-1)%2:continue
 if ch=='{':braces.append(i)
 elif ch=='}':assert braces; braces.pop()
assert not braces
env=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
 if m.group(1)=='begin':env.append(m.group(2))
 else:assert env.pop()==m.group(2)
assert not env and len(re.findall(r'(?<!\\)\$',clean))%2==0 and clean.count(r'\[')==clean.count(r'\]')
for m in re.finditer(r'\\\[([\s\S]*?)\\\]',P):assert not re.search(r'\n[ \t]*\n',m.group(1))
prior=(OUT/'scan026_source_sections01_12_proposal_v01.tex').read_text()
diff=''.join(difflib.unified_diff(prior.splitlines(keepends=True),P.splitlines(keepends=True),fromfile='out/checks/scan026_source_sections01_12_proposal_v01.tex',tofile='out/checks/scan026_source_sections01_19_proposal_v01.tex',n=3))
diff_file=save('scan026_source_sections13_19_delta_v01.diff',diff.encode(),True)
states_file=save('scan026_source_sections13_19_selected_states_v01.json',{'ring_states':ring_states,'other_selected_scopes':selected,'diagram_codec':'out/checks/scan026_source_diagram96_codec_v01.json','pair_codec':'out/checks/scan026_source_pair16_codec_v01.json'})
bindings_file=save('scan026_source_sections13_19_donor_mutations_v01.json',{'mutations':donor_mutations,'B_primitive_command_preservation':primitive,'composite_source':composite,'root_coordinate_map':placement})
audit={'scope':'Source-only proposal through root §19; no root/final files changed.','authority_captures':captures,
 'cumulative_literal_replacements':len(mapping['literal_replacements']),'exact_inverse_to_frozen_A':mapping['forward_and_inverse_restore_exact_A_bytes'],
 'diagram_states':96,'pair_states':16,'ring_state_counts':{g:len(x['exact_selected_candidates']) for g,x in ring_states.items()},'S14_states':len(states14),
 'B_primitive_drawing_commands_preserved':len(primitive),'S15_S16_original_C_fields_changed':0,
 'new_L052_source_count':P.count('% BEGIN R026-L052'),'root_native_map_copied':placement,
 'root_locus_L052_sole_image_authority':'section14; source binding closure section15',
 'source_braces_and_environments_balanced':True,'math_delimiters_balanced':True,'physical_blank_paragraphs_outside_displays':True,
 'new_ink_or_count_choices':0,'image_bytes_read':0,'main_approved':False,'proposal':result,'artifacts':[plan_file,diff_file,states_file,bindings_file]}
save('scan026_source_sections13_19_audit_v01.json',audit)
print(json.dumps(audit,ensure_ascii=False,indent=2))
