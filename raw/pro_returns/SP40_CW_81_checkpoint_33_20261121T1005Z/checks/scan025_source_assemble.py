#!/usr/bin/env python3
"""Pending exact source assembly from root's scan025 journal. No images."""
from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'out/checks'
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes)else x.encode('utf-8')).hexdigest()
T={r:(ROOT/f'out/readers/025/{r}/reading.tex').read_text()for r in 'ABC'}
SM={r:json.loads((ROOT/f'out/readers/025/{r}/source_map.json').read_text())for r in 'ABC'}
JPATH='out/checks/scan025_root_journal.md'
J=(ROOT/JPATH).read_text()
AUDITPATH='out/checks/scan025_root_crop_audit.json'
AUDIT=json.loads((ROOT/AUDITPATH).read_text())
FROZEN=json.loads((OUT/'scan025_reader_fingerprints.json').read_text())
for path,h in FROZEN['files'].items():assert sha((ROOT/path).read_bytes())==h


def exact(path,t,a=0,b=None):
    if b is None:b=len(t)
    return dict(path=path,sha256=sha(t),sha256_utf8=sha(t),char_start=a,char_end=b,
                utf8_byte_start=len(t[:a].encode()),utf8_byte_end=len(t[:b].encode()),
                line_start=t[:a].count('\n')+1,line_end=t[:max(a,b-1)].count('\n')+1,
                body_sha256=sha(t[a:b]),literal=t[a:b])


sections={}
headings=list(re.finditer(r'^## (\d\d) — .+$',J,re.M))
for i,m in enumerate(headings):
    b=headings[i+1].start()if i+1<len(headings)else len(J)
    sections[m.group(1)]=exact(JPATH,J,m.start(),b)
assert all(f'{i:02d}'in sections for i in range(1,20))
assert '20' in sections, 'Root recurring-qualifier supersession must be frozen before assembly.'


def own(r,a,b):return exact(f'out/readers/025/{r}/reading.tex',T[r],a,b)
def group(gid):
    r=gid[0];g=next(g for g in SM[r]['groups']if g['id']==gid)
    a,b=(g['start_char'],g['end_char_exclusive'])if 'start_char'in g else g['char_offsets']
    assert T[r][a:b]==g['literal_source']
    return dict(id=gid,raw_map=g,source=own(r,a,b))


EDITS=[]
def edit(eid,old,new,secs,donors=None,changes=None):
    assert T['C'].count(old)==1,(eid,'ambiguous base span')
    a=T['C'].index(old);b=a+len(old)
    assert not any(a<e['original_end']and b>e['original_start']for e in EDITS),(eid,'overlap')
    EDITS.append(dict(edit_id=eid,original_start=a,original_end=b,original_source=own('C',a,b),replacement=new,
                      root_sections=secs,root_authority=[sections[x]for x in secs],
                      donor_sources=donors or [],bounded_source_changes=changes or [],main_approved=False))


for eid,cgid,agid,sec in [('E01-hatted-Sigma','C025-S02','A025-S02','06'),('E02-K-revision','C025-G09','A025-G09','11'),('E03-final-Sigma','C025-S08','A025-S08','16')]:
    cg,ag=group(cgid),group(agid)
    edit(eid,cg['source']['literal'],ag['source']['literal'],[sec],[ag['source']])
# Root section 20 supersedes only the five former added outer wrappers.
# Their exact original C source groups now pass unchanged through the C base.
recurring_groups=['C025-E02','C025-S04','C025-S05','C025-S06','C025-S07']

edit('E09-participle',r'\unsure{determinés|déterminés|determines}',r'\unsure{determinés|determines}',['13'],
     changes=[dict(kind='remove only middle whole-word candidate',old=r'\unsure{determinés|déterminés|determines}',new=r'\unsure{determinés|determines}',
                   unchanged='First and final candidates retain exact bytes and order; all three original candidates remain in the raw reader provenance.')])

que=group('B025-G09')
edit('E10-final-que', 'Je dis que', 'Je dis $\n'+que['source']['literal']+'\n$',['15','19'],[que['source']],
     [dict(kind='math-context and marker boundaries',before='Je dis ',opening='$\n',closing='\n$',
           basis='B complete own prose uses Je dis followed by this mathord group inside dollar delimiters; added physical newlines keep both group markers on their own lines.')])

brace=group('B025-G08')
edit('E11-final-left-brace',r'\bigl\{','\n'+brace['source']['literal']+'\n',['16'],[brace['source']],
     [dict(kind='marker line boundaries only',prefix='\n',suffix='\n',basis='Complete B mathord group retained exactly; surrounding final-set companions remain from C.')])

def lower_frame(r):
    t=T[r];a=t.rindex(r'\]')+len(r'\]');b=t.index('% archive sheet number: 24')
    return own(r,a,b)
clow,blow=lower_frame('C'),lower_frame('B')
lower=blow['literal'];insertions=[]
for gid in ['B025-M01','B025-M02']:
    marker='% BEGIN '+gid
    p=lower.index(marker)
    if p and lower[p-1]!='\n':
        insertions.append(dict(marker=marker,original_donor_relative_offset=blow['literal'].index(marker),text='\n'))
        lower=lower[:p]+'\n'+lower[p:]
inverse_lower=lower
for ins in reversed(insertions):
    pos=inverse_lower.index(ins['marker']);assert inverse_lower[pos-1]=='\n'
    inverse_lower=inverse_lower[:pos-1]+inverse_lower[pos:]
assert inverse_lower==blow['literal']
edit('E12-lower-sheet-whole-placement',clow['literal'],lower,['17','18','19'],[blow],
     [dict(kind='two BEGIN-marker physical newlines only',insertions=insertions,
           exact_native_placement='Entire B outer frame retained, including x=0.01em,y=-0.01em, full bounding path and both original containing nodes. Child group units are unchanged.')])

EDITS.sort(key=lambda e:e['original_start'])
pieces=[];partition=[];at=pos=0
for e in EDITS:
    a,b=e['original_start'],e['original_end']
    if a>at:
        x=T['C'][at:a];pieces.append(x);partition.append(dict(kind='unchanged_C',source=own('C',at,a),selected_start=pos,selected_end=pos+len(x)));pos+=len(x)
    x=e['replacement'];pieces.append(x);e['selected_start']=pos;e['selected_end']=pos+len(x)
    partition.append(dict(kind='root_authorized_literal_replacement',edit_id=e['edit_id'],selected_start=pos,selected_end=pos+len(x)))
    pos+=len(x);at=b
if at<len(T['C']):
    x=T['C'][at:];pieces.append(x);partition.append(dict(kind='unchanged_C',source=own('C',at,len(T['C'])),selected_start=pos,selected_end=pos+len(x)))
PAGE=''.join(pieces)
DP='out/checks/scan025_final_draft.tex';(ROOT/DP).write_text(PAGE)
def selected(a,b):return exact(DP,PAGE,a,b)
def boundary(p):
    return dict(char_offset=p,preceding_character=PAGE[p-1:p],following_character=PAGE[p:p+1],
                preceding_last_byte_hex=PAGE[:p].encode()[-1:].hex(),following_first_byte_hex=PAGE[p:].encode()[:1].hex(),
                literal_before=PAGE[max(0,p-70):p],literal_after=PAGE[p:p+70])
for e in EDITS:
    e['selected_source']=selected(e['selected_start'],e['selected_end'])
    e['splice_boundaries']={k:boundary(e['selected_'+k])for k in ['start','end']}
for p in partition:p['selected_source']=selected(p['selected_start'],p['selected_end'])

# Recognize each donor's literal marker syntax; preserve nested A ownership.
markers=[]
for m in re.finditer(r'^% (?:(BEGIN|END) ([ABC]025-[A-Z0-9]+)|([ABC]025-[A-Z0-9]+) (begin|end))[ \t]*$',PAGE,re.M):
    action=m.group(1)or m.group(4).upper();gid=m.group(2)or m.group(3)
    markers.append((m,action,gid))
stack=[];groups=[]
for m,action,gid in markers:
    if action=='BEGIN':stack.append((gid,m.start()))
    else:
        old,a=stack.pop();assert old==gid,(old,gid)
        orig=group(gid)
        b=m.end()+int(orig['source']['literal'].endswith('\n'))
        secs=[]
        for e in EDITS:
            if e['selected_start']<=a and b<=e['selected_end']:secs=e['root_sections'];break
        groups.append(dict(id=gid,source=selected(a,b),donor_group_ids=[gid],donor_source=orig['source'],
                           donor_map=orig['raw_map'],contained_in=[v[0]for v in stack],root_sections=secs,
                           exact_donor_group=PAGE[a:b]==orig['source']['literal'],
                           local_outer_unsure_added=False,
                           recurring_primary_printing_authority=sections['20']if gid in recurring_groups else None,main_approved=False))
assert not stack
groups.sort(key=lambda g:g['source']['char_start'])
expected={'C025-G01','C025-S01','C025-G02','C025-E01','C025-G03','C025-G04','C025-G05','C025-G06','C025-S03','C025-E02','C025-G07','C025-G08','C025-S04','C025-S05','C025-S06','C025-S07','A025-S02','A025-M01','A025-G09','A025-M02','A025-S08','B025-G09','B025-G08','B025-M01','B025-M02'}
assert {g['id']for g in groups}==expected

def command_end(start):
    depth=0;comment=False
    for i in range(start,len(PAGE)):
        c=PAGE[i];bs=0;j=i-1
        while j>=0 and PAGE[j]=='\\':bs+=1;j-=1
        escaped=bool(bs%2)
        if c=='%'and not escaped:comment=True
        if c=='\n':comment=False
        if comment:continue
        if c=='{'and not escaped:depth+=1
        elif c=='}'and not escaped:depth-=1
        elif c==';'and depth==0:return i+1
    raise ValueError(start)
commands=[]
for m in re.finditer(r'\\(draw|fill|path|coordinate|node|useasboundingbox)\b',PAGE):
    prefix=PAGE[PAGE.rfind('\n',0,m.start())+1:m.start()]
    if re.search(r'(?<!\\)%',prefix):continue
    a=m.start();b=command_end(a);text=PAGE[a:b]
    containers=[g for g in groups if g['source']['char_start']<=a and b<=g['source']['char_end']]
    owner=min(containers,key=lambda g:g['source']['char_end']-g['source']['char_start'])['id']if containers else None
    matches=[]
    for r in 'ABC':
        for hit in re.finditer(re.escape(text),T[r]):matches.append(own(r,hit.start(),hit.end()))
    normalized_donor=None
    if not matches:
        # Only the two whole outer nodes include the authorized BEGIN newline.
        back=text.replace('$\n% BEGIN B025-M','$% BEGIN B025-M')
        if back in T['B']:
            p=T['B'].index(back);normalized_donor=own('B',p,p+len(back))
    assert matches or normalized_donor,(m.group(),a,'unbound command')
    commands.append(dict(id=f'R025-CMD{len(commands)+1:03d}',command=m.group(1),selected_source=selected(a,b),owner_group=owner,
                         containing_groups=[g['id']for g in containers],exact_donor_matches=matches,
                         donor_with_only_authorized_marker_newline=normalized_donor,main_approved=False))

clean=re.sub(r'(?<!\\)%[^\n]*','',PAGE)
stack=[]
for m in re.finditer(r'(?<!\\)[{}]',clean):
    if m.group()=='{':stack.append(m.start())
    else:assert stack,('unmatched closing',m.start());stack.pop()
assert not stack
assert len(re.findall(r'(?<!\\)\$',clean))%2==0
assert clean.count(r'\[')==clean.count(r'\]')==2
for m in re.finditer(r'\\\[([\s\S]*?)\\\]',PAGE):assert not re.search(r'\n[ \t]*\n',m.group(1))
assert not re.search(r'% (?:END|[ABC]025-[A-Z0-9]+ end)[^\n]*% (?:BEGIN|[ABC]025-[A-Z0-9]+ begin)',PAGE)
inverse=PAGE
for e in reversed(EDITS):inverse=inverse[:e['selected_start']]+e['original_source']['literal']+inverse[e['selected_end']:]
assert inverse==T['C']
assert PAGE.count('% archive sheet number: 24')==1

initial_path='out/checks/scan025_source_assembly_initial_draft_v01.tex'
initial=(ROOT/initial_path).read_text();bounded=[];replay=PAGE
for gid in recurring_groups:
    orig=group(gid)['source']['literal'];a=orig.index(r'\tikz[');b=orig.rfind('\n% '+gid+' end')
    before=orig[:a]+r'\unsure{'+orig[a:b]+'}'+orig[b:]
    assert initial.count(before)==1 and PAGE.count(orig)==1
    old_at=initial.index(before);new_at=PAGE.index(orig)
    bounded.append(dict(group=gid,before=exact(initial_path,initial,old_at,old_at+len(before)),after=selected(new_at,new_at+len(orig)),
                        removed_tokens=[dict(original_group_relative_offset=a,text=r'\unsure{'),dict(original_group_relative_offset=b,text='}')],
                        root_authority=sections['20']))
    assert replay.count(orig)==1;replay=replay.replace(orig,before,1)
assert replay==initial
closure=dict(scan=25,source_only=True,reason='Root section20 rescinds only five outer wrappers while retaining all local candidate/hand/role evidence.',
             before_sha256_utf8=sha(initial),after_sha256_utf8=sha(PAGE),exact_changes=bounded,
             inverse_replay_exact=True,all_other_selected_source_bytes_unchanged=True,root_authority=sections['20'],main_approved=False)
cp=OUT/'scan025_source_wrapper_supersession_v01.json';cp.write_text(json.dumps(closure,ensure_ascii=False,indent=2)+'\n')

MAP=dict(schema='scan025-selected-source-map-v1',scan=25,source_only=True,main_adjudicated=False,main_approved=False,
         draft_path=DP,draft_sha256_utf8=sha(PAGE),final_draft_sha256=sha(PAGE),
         authority=dict(root_journal_path=JPATH,root_journal_sha256=sha(J),journal_sections=sections,
                        root_crop_audit_path=AUDITPATH,root_crop_audit_sha256=sha((ROOT/AUDITPATH).read_bytes()),
                        brief='out/briefs/source_record_brief_v07.md',brief_sha256=sha((ROOT/'out/briefs/source_record_brief_v07.md').read_bytes())),
         frozen_source_files={r:dict(path=f'out/readers/025/{r}/reading.tex',sha256=sha(T[r]))for r in 'ABC'},
         selected_groups=groups,exact_command_ownership=commands,literal_replacements=EDITS,complete_selected_source_partition=partition,
         source_printing_supersession=dict(path=cp.relative_to(ROOT).as_posix(),sha256=sha(cp.read_bytes())),
         source_locus_coverage=[],limits='Source-only assembly. Every selected path and declared native unit/coordinate/origin/baseline is copied. No rendering, image matching, rescaling, physical count choice, mathematical transformation or approval is performed.')
mp=OUT/'scan025_final_source_map.json';mp.write_text(json.dumps(MAP,ensure_ascii=False,indent=2)+'\n')
audit=dict(scan=25,draft_sha256_utf8=sha(PAGE),source_map_sha256=sha(mp.read_bytes()),root_journal_sha256=sha(J),
           exact_inverse_to_C=True,source_braces_balanced=True,inline_math_delimiter_count=len(re.findall(r'(?<!\\)\$',clean)),display_pairs=2,
           physical_blank_paragraphs_outside_display=True,marker_line_boundaries=True,selected_groups=len(groups),literal_commands=len(commands),
           exact_donor_commands=sum(bool(c['exact_donor_matches'])for c in commands),
           authorized_outer_node_newline_commands=[c['id']for c in commands if c['donor_with_only_authorized_marker_newline']],
           local_outer_unsure_groups=[g['id']for g in groups if g['local_outer_unsure_added']],
           rescalings=0,images_read=0,main_adjudicated=False,main_approved=False,all_checks_passed=True,
           pending=['Complete selected record, exact attachments and root final approval.'])
(OUT/'scan025_source_assembly_audit_v02.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(audit,ensure_ascii=False,indent=2))
