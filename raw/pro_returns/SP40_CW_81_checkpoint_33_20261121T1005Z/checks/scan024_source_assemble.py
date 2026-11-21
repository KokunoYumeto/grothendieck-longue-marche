"""Exact source-only assembly authorized by the frozen root journal.

No image, metric, mathematical, count, or approval decision is made here.
"""
from pathlib import Path
import json, hashlib, re, sys
sys.dont_write_bytecode=True
BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes) else x.encode()).hexdigest()
read=lambda p:(BASE/p).read_text()
def put(p,x):
    (BASE/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n' if not isinstance(x,str) else x)
S=json.loads(read('out/checks/scan024_source_row_skeleton_v01.json'))
POOL=S['source_reference_pool']
J=json.loads(read('out/checks/scan024_root_decisions.json'))
T={r:read(f'out/readers/024/{r}/reading.tex') for r in 'ABC'}
def pool_ref(r):return POOL[r]['exact_source_ref']
def literal(f):return read(f['source_path'])[f['character_start']:f['character_end_exclusive']]
def group(role,gid):return literal(pool_ref(S['complete_own_group_candidate_scopes'][role][gid]['complete_own_TeX_ref']))
def ref(path,t,a=0,b=None):
    if b is None:b=len(t)
    return dict(path=path,sha256_utf8=sha(t),char_start=a,char_end=b,
      character_start=a,character_end_exclusive=b,utf8_byte_start=len(t[:a].encode()),
      utf8_byte_end_exclusive=len(t[:b].encode()),line_start=t[:a].count('\n')+1,
      line_end=t[:max(a,b-1)].count('\n')+1,span_sha256_utf8=sha(t[a:b]),literal=t[a:b])
def own_ref(role,a,b):return ref(f'out/readers/024/{role}/reading.tex',T[role],a,b)
edits=[]
def edit(eid,old,new,sections,donors=(),needle_start=0):
    assert old in T['A'][needle_start:],eid
    a=T['A'].index(old,needle_start); b=a+len(old)
    assert not any(a<x['original_end'] and b>x['original_start'] for x in edits),eid
    edits.append(dict(edit_id=eid,original_start=a,original_end=b,replacement=new,
       original_source=own_ref('A',a,b),root_sections=list(sections),donor_group_ids=list(donors),
       main_approved=False))
header=T['A'][T['A'].index('% Manual'):T['A'].index('% BEGIN UNIT P1')]
edit('E01-editorial-header',header,
 '% Selected source assembly from the frozen scan024 root journal.\n'
 '% Every graphical donor retains its declared coordinate labels, units,\n'
 '% origin and baseline; combined groups are identified in the source map.\n'
 '% Manual approximations receive no rendering, alignment or metric claim.\n'
 '% Invisible candidate annotations supply no second visible inscription.\n',[])
edit('E02-opening-word',r'\unsure{Considérons|Considerons}',r'\unsure{Considerons|Considérons}',['01'])
edit('E03-soit-point',r', soit $S$',',\n'+group('C','C024-M01')+'$S$',['04'],['C024-M01'])
edit('E04-definition-arrow',r'\ \overset{\text{def}}{\Longleftrightarrow}\ ',
 '\\ \n'+group('C','C024-G05')+'\\ ',['08'],['C024-G05'])
edit('E05-lemma-owner-comment',
 '% Complete word-bearing marked lemma block. Nested G08 owns only Le/Ce;\n% G09 owns only .); G10 is mark-only. Other words occur once in the nodes.\n',
 '% Complete selected word-bearing lemma block. A024-G08 owns Le/Ce;\n'
 '% B024-G06 owns sommets and its high point; A024-G10 owns the pale trace.\n'
 '% The complete qualified noun phrase is followed by the literal endpoint .).\n', ['10','11','12','13','28'])
edit('E06-sommets',r'\unsure{ens des|ens de} sommets, $I$ comme ens.',
 r'\unsure{ens des|ens de}'+'\n'+group('B','B024-G06')+r', $I$ comme ens.', ['11'],['B024-G06'])
edit('E07-noun-six-states',r"d'\unsure{aretes|arêtes|arètes}",
 r"\unsure{de aretes|d'aretes|de arêtes|d'arêtes|de arètes|d'arètes}).",['12'])
edit('E08-replaced-endpoint',group('A','A024-G09'),'', ['12'],['A024-G09'])
# The literal endpoint is .).: keep its initial point after the noun wrapper.
e=next(e for e in edits if e['edit_id']=='E07-noun-six-states')
e['replacement']=e['replacement'].replace('}).','}.).')
old_start=T['A'].index(' Il\n% BEGIN GROUP A024-G12')
old_end=T['A'].index(' exactement deux',old_start)
c=group('C','C024-G11')
tail_start=c.index(r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (65,0) {y};')
tail_end=c.rindex('\\end{tikzpicture}')
prefix=c[:tail_start]+c[tail_end:]
prefix=prefix.replace('(0,-7) rectangle (89,18)','(0,-7) rectangle (65,18)',1)
prefix=prefix.replace(r'\phantom{Il \deleted{\unsure{existe|ex}} y a}',r'\phantom{Il \deleted{\unsure{existe|ex}}}',1)
prefix=prefix.replace('% BEGIN C024-G11','% BEGIN GROUP R024-GEX\n% C024-G11 Il/cancelled-word prefix; complete B024-G09 y/a continuation.\n% Prefix reservation ends at the copied former y-anchor label 65.\n% The prefix pt units and continuation ex units remain separately declared.',1)
prefix=prefix.replace('% END C024-G11','% END C024-G11 selected prefix',1)
hybrid=prefix+group('B','B024-G09')+'% END GROUP R024-GEX\n'
edit('E09-Il-existe-ya-complete',T['A'][old_start:old_end],'\n'+hybrid,['15'],['C024-G11','B024-G09'])
edit('E10-condition-b',"par l'ens de ces deux",r"par \unsure{l'ens|l'une} de ces deux",['16'])
edit('E11-conn-order',r'\unsure{connexes|conn}',r'\unsure{conn|connexes}',['19'],['A024-G15'])
edit('E12-precise-candidates',r'\unsure{précise|prècise|precise}',r'\unsure{prècise|précise|prêcise|precise}',['20'])
edit('E13-U-patch-comment',
 '% remnants are retained once. Patch glyph, attachment and hand remain qualified.\n',
 '% remnants are retained once. Patch glyph, attachment, hand and correction state\n% remain qualified; each pale neighbour has its own undetermined hand and role.\n',['22'],['A024-G17'])
edit('E14-Sigma-order-comment',
 '% Complete local candidates Sigma_i^+ | Sigma_i^- | Sigma_{prime}^+ |\n% Sigma_{prime}^-. Separate original C row14 sign scope and new index scope.\n',
 '% Complete local candidates Sigma_i^- | Sigma_i^+ | Sigma_{prime}^- |\n% Sigma_{prime}^+. Separate original C row14 sign scope and new index scope.\n',['22'],['A024-G18'])
edit('E15-edge-word-order',r'\unsure{qui|dé|de}',r'\unsure{de|dé|qui}',['24'])
edit('E16-definit',group('A','A024-G21'),group('B','B024-G11'),['25'],['B024-G11'])
edit('E17-final-Sigma',r'un $U_{s_-}\subset\Sigma_i^-$ tel que',
 r'un $U_{s_-}\subset$'+'\n% Joined head/body retained; local intended head/retrace role remains qualified.\n'+group('C','C024-S05')+'tel que',['26'],['C024-S05'])
edits.sort(key=lambda e:e['original_start'])
pieces=[];partition=[];at=0;pos=0
for e in edits:
    a,b=e['original_start'],e['original_end']
    if a>at:
        x=T['A'][at:a];pieces.append(x);partition.append(dict(kind='unchanged_A',source=own_ref('A',at,a),selected_start=pos,selected_end=pos+len(x)));pos+=len(x)
    x=e['replacement'];pieces.append(x);e.update(selected_start=pos,selected_end=pos+len(x));partition.append(dict(kind='root_authorized_literal_replacement',edit_id=e['edit_id'],selected_start=pos,selected_end=pos+len(x)));pos+=len(x);at=b
if at<len(T['A']):
    x=T['A'][at:];pieces.append(x);partition.append(dict(kind='unchanged_A',source=own_ref('A',at,len(T['A'])),selected_start=pos,selected_end=pos+len(x)))
PAGE=''.join(pieces)
DP='out/checks/scan024_final_draft.tex'
put(DP,PAGE)
def selected_ref(a,b):return ref(DP,PAGE,a,b)
def boundaries(p):
    return dict(char_offset=p,preceding_character=PAGE[p-1:p],following_character=PAGE[p:p+1],
      preceding_last_byte_hex=PAGE[:p].encode()[-1:].hex(),following_first_byte_hex=PAGE[p:].encode()[:1].hex(),
      literal_before=PAGE[max(0,p-65):p],literal_after=PAGE[p:p+65])
for e in edits:
    e['selected_source']=selected_ref(e['selected_start'],e['selected_end'])
    e['splice_boundaries']={k:boundaries(e[f'selected_{k}']) for k in ['start','end']}
    e['root_authority']=dict(path='out/checks/scan024_root_decisions.json',sha256=sha(read('out/checks/scan024_root_decisions.json')),sections=e['root_sections'])
for p in partition:p['selected_source']=selected_ref(p['selected_start'],p['selected_end'])
# Each marker is a whole line. Stack-based ranges preserve nested ownership.
groups=[];stack=[]
for m in re.finditer(r'^% (BEGIN|END) (?:GROUP )?([ABCR]024-[A-Z0-9]+)\s*$',PAGE,re.M):
    action,gid=m.groups()
    if action=='BEGIN':stack.append((gid,m.start(),m.end()))
    else:
        g,a,inner=stack.pop();assert g==gid,(g,gid)
        b=m.end()+int(PAGE[m.end():m.end()+1]=='\n')
        donor=[gid] if gid!='R024-GEX' else ['C024-G11','B024-G09']
        groups.append(dict(id=gid,source=selected_ref(a,b),donor_group_ids=donor,
          contained_in=[x[0] for x in stack],main_approved=False))
assert not stack
groups.sort(key=lambda g:g['source']['char_start'])
def containers(a,b):return [g['id'] for g in groups if g['source']['char_start']<=a and b<=g['source']['char_end']]
def end_command(start):
    depth=0;skip=False
    for i in range(start,len(PAGE)):
        c=PAGE[i]
        if c=='%' and (i==0 or PAGE[i-1]!='\\'):skip=True
        if c=='\n':skip=False
        if skip:continue
        if c in '{}' and (i==0 or PAGE[i-1]!='\\'):depth+=1 if c=='{' else -1
        if c==';' and depth==0:return i+1
    raise ValueError(start)
commands=[]
for m in re.finditer(r'\\(draw|fill|path|node)\b',PAGE):
    # Every path/node command, including nested child commands, is retained.
    line=PAGE[PAGE.rfind('\n',0,m.start())+1:m.start()]
    if '%' in line:continue
    b=end_command(m.start());text=PAGE[m.start():b];con=containers(m.start(),b)
    owner=min((g for g in groups if g['id'] in con),key=lambda g:g['source']['char_end']-g['source']['char_start'])['id'] if con else None
    donors=[]
    roles=[owner[0]] if owner and owner[0] in 'ABC' else ['C','B'] if owner=='R024-GEX' else ['A','B','C']
    for r in roles:
        for hit in re.finditer(re.escape(text),T[r]):donors.append(own_ref(r,hit.start(),hit.end()))
    commands.append(dict(id=f'R024-CMD{len(commands)+1:03d}',command=m.group(1),selected_source=selected_ref(m.start(),b),owner_group=owner,containing_groups=con,exact_donor_matches=donors,root_authorized_composite=not bool(donors),main_approved=False))
# Source syntax review uses lexical source only, never rendering/compilation.
clean=re.sub(r'(?<!\\)%[^\n]*','',PAGE)
br=[]
for m in re.finditer(r'(?<!\\)[{}]',clean):
    if m.group()=='{':br.append(m.start())
    else:assert br,'unmatched closing brace';br.pop()
assert not br,'unmatched opening brace'
assert len(re.findall(r'(?<!\\)\$',clean))%2==0
assert clean.count(r'\[')==clean.count(r'\]')
for display in re.finditer(r'\\\[([\s\S]*?)\\\]',PAGE):
    assert not re.search(r'\n[ \t]*\n',display.group(1))
assert not re.search(r'% END[^\n]*% BEGIN',PAGE)
inverse=PAGE
for e in reversed(edits):inverse=inverse[:e['selected_start']]+e['original_source']['literal']+inverse[e['selected_end']:]
assert inverse==T['A']
MAP=dict(schema='scan024-selected-source-map-v1',scan=24,source_only=True,main_adjudicated=False,main_approved=False,
 draft_path=DP,draft_sha256_utf8=sha(PAGE),final_draft_sha256=sha(PAGE),
 authority=dict(root_journal_path='out/checks/scan024_root_decisions.json',root_journal_sha256=sha(read('out/checks/scan024_root_decisions.json')),brief='out/briefs/source_record_brief_v07.md',brief_sha256=sha(read('out/briefs/source_record_brief_v07.md'))),
 frozen_source_files={r:dict(path=f'out/readers/024/{r}/reading.tex',sha256=sha(T[r])) for r in 'ABC'},
 selected_groups=groups,exact_command_ownership=commands,literal_replacements=edits,complete_selected_source_partition=partition,
 source_locus_coverage=[],limits='Exact source assembly only; no images, coordinates computed, metric/render validation, mathematical transformation, physical counts or approval.')
put('out/checks/scan024_final_source_map.json',MAP)
audit=dict(scan=24,draft_sha256_utf8=sha(PAGE),source_map_sha256=sha(read('out/checks/scan024_final_source_map.json')),main_approved=False,
 exact_inverse_to_A=True,source_braces_balanced=True,inline_math_delimiter_count=len(re.findall(r'(?<!\\)\$',clean)),display_pairs=clean.count(r'\['),
 physical_blank_paragraphs_outside_display=True,marker_line_boundaries=True,selected_groups=len(groups),literal_commands=len(commands),
 commands_with_exact_donor=len([c for c in commands if c['exact_donor_matches']]),root_authorized_composite_commands=[c['id'] for c in commands if c['root_authorized_composite']],
    pending=['Physical counts and record approval remain root-owned.'])
put('out/checks/scan024_source_assembly_audit_v01.json',audit)
print(json.dumps(audit,ensure_ascii=False,indent=2))
