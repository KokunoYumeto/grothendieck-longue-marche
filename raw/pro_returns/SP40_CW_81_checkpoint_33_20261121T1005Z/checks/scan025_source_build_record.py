#!/usr/bin/env python3
"""Bind pending scan025 record to the root journal and exact selected source.

Source-only assembly: no image, ink inference, count decision, or approval.
"""
from pathlib import Path
from collections import Counter
from copy import deepcopy
import hashlib,json,re,sys
sys.dont_write_bytecode=True
from scan025_source_record_values import SPECS,CANDIDATE_SUFFIX,QUALIFIED,DOUBT_CONFIDENCE,H_BASIS

ROOT=Path(__file__).resolve().parents[2]
O=ROOT/'out/checks'
sha=lambda s:hashlib.sha256(s.encode('utf-8') if isinstance(s,str) else s).hexdigest()
dump=lambda x:json.dumps(x,ensure_ascii=False,indent=2)+'\n'
compact=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'))
def read(p):return (ROOT/p).read_text()
def load(p):return json.loads(read(p))
def write(p,obj):
    text=dump(obj); temp=ROOT/(p+'.tmp');temp.write_text(text);temp.replace(ROOT/p);return sha(text)
UP='out/checks/scan025_source_union_v01.json';U=load(UP)
PP='out/checks/scan025_source_pool_v01.json';POOL=load(PP)
MP='out/checks/scan025_final_source_map.json'
BASEMP='out/checks/scan025_source_assembly_map_v02.json';M=load(BASEMP)
DP='out/checks/scan025_final_draft.tex';PAGE=read(DP)
JP='out/checks/scan025_root_journal.md';J=read(JP)
AP='out/checks/scan025_root_crop_audit.json';AUD=load(AP)
assert sha(PAGE)=='e5098e342952e5103022ef30641cdda851e5d74203913db9f2060661e50297ad'
assert sha(J)=='74d43b997bb80adecb31a7bf6cb6b7f81b3af350955475c6d87b0d2ad858afb1'
assert sha(read(BASEMP))=='7edf4da01314025441637026c22e8f6b3b7c585f79332e2f7238816572e8fc38'
FROZEN=load('out/checks/scan025_reader_fingerprints.json')
for p,h in FROZEN['files'].items():assert sha((ROOT/p).read_bytes())==h,(p,'frozen source changed')

FILES={f['id']:f for f in POOL['files']};FP={f['path']:f for f in POOL['files']}
STR={s['id']:s for s in POOL['strings']};SP={s['id']:s for s in POOL['spans']}
S_SCOPE=load('out/checks/scan025_S_scope.json')
SOURCE={p:read(p) for p in FP if p!=S_SCOPE['source']}
sf=FP[S_SCOPE['source']]
SOURCE[sf['path']]=''.join(STR[c['string_ref']]['literal'] for c in sf['payload']['text_chunks'])
assert sha(SOURCE[sf['path']])==sf['sha256_utf8']
SOURCE.update({DP:PAGE,JP:J,AP:read(AP),UP:read(UP),BASEMP:read(BASEMP)})
JSON={p:json.loads(t) for p,t in SOURCE.items() if p.endswith('.json')}
def at(obj,ptr):
    for k in ptr[1:].split('/') if ptr else []:
        k=k.replace('~1','/').replace('~0','~');obj=obj[int(k)] if isinstance(obj,list) else obj[k]
    return obj
def exact(p,a=0,b=None):
    t=SOURCE.get(p)
    if t is None:t=read(p);SOURCE[p]=t
    if b is None:b=len(t)
    assert 0<=a<=b<=len(t),(p,a,b)
    return dict(path=p,sha256=sha(t),char_start=a,char_end=b,
                utf8_byte_start=len(t[:a].encode()),utf8_byte_end=len(t[:b].encode()),
                line_start=t.count('\n',0,a)+1,line_end=t.count('\n',0,max(a,b-1))+1,
                body_sha256=sha(t[a:b]),literal=t[a:b])
def from_union(x):return exact(x['source_path'],x['char_start'],x['char_end_exclusive'])
def rawval(ref):return at(JSON[ref['source_path']],ref['json_pointer'])
def oldref(ref):
    s=SP[ref['span_ref']];v=from_union(s);v['json_pointer']=ref['json_pointer'];v['original_pool_span']=s['id'];return v
def jref(p,ptr):
    fid=FP[p]['id'];s=SP[POOL['json_pointer_spans'][fid][ptr]];v=from_union(s);v['json_pointer']=ptr;v['original_pool_span']=s['id'];return v
REFS={};RKEY={}
def register(x):
    k=compact(x)
    if k not in RKEY:
        rid=f'R25-{len(REFS)+1:04d}';RKEY[k]=rid;REFS[rid]=x
    return RKEY[k]
def uregister(x):return register(from_union(x))
def rregister(x):return register(oldref(x))
HEAD=list(re.finditer(r'^## (\d\d) — .+$',J,re.M))
SECS={m.group(1):exact(JP,m.start(),HEAD[i+1].start() if i+1<len(HEAD) else len(J)) for i,m in enumerate(HEAD)}
assert list(SECS)==[f'{i:02d}' for i in range(1,22)]
SECTION_REF={k:register(v) for k,v in SECS.items()}

# Preserve the old authority as an exact prefix, while current metadata names §21.
old_journal=M['authority']['root_journal_sha256']
prefix=J[:HEAD[-1].start()]
assert sha(prefix)==old_journal
prefixpath='out/checks/scan025_source_journal_through20_snapshot.md'
if (ROOT/prefixpath).exists():assert read(prefixpath)==prefix
else:(ROOT/prefixpath).write_text(prefix)
M['authority_history']=[dict(role='completed assembly v02 execution; retained unchanged',map_path=BASEMP,map_sha256=sha(read(BASEMP)),journal_sha256=old_journal,journal_exact_prefix_snapshot=prefixpath)]
M['authority']['root_journal_sha256']=sha(J)
M['authority']['journal_sections']=deepcopy(SECS)
M['authority']['source_record_builder_scope']='Current record/attachment binding through §21; no page bytes or v02 execution result changed.'

RAW={x['id']:x for x in U['raw_row_correspondence']}
LOC={x['id']:x for x in U['source_locus_union']}
REPORT={r:JSON[f'out/readers/025/{r}/report.json'] for r in 'ABC'}
GM={g:rawval(x['raw_group']) for g,x in U['complete_own_groups'].items()}
SG={g['id']:g for g in M['selected_groups']}
GROUP_META=['id','ownership','owns','complete_candidates','semantic_annotation','qualified_here','proposal','qualification','alternatives','complete_qualified_candidates','reading','printed_qualifier','role','role_and_attachment','hand','local_hand_scopes']
FI={
 'A':{'opening':[0,1,2,3,4,5,9],'display':[6,7,8,10,11,12,13,14,15,16],'prose':list(range(17,25)),'final':[25,26],'lower':[27],'archive':[28]},
 'B':{'opening':[0,1,2,3,4,5,6,9],'display':[7,8,10,11,12,13,14,15,16],'prose':list(range(17,26)),'final':[26,27,28],'lower':[29,30],'archive':[31]},
 'C':{'opening':list(range(8)),'display':list(range(8,18)),'prose':list(range(18,26)),'final':[26,27],'lower':[28,29],'archive':[30]},
}
for r in 'ABC':
    assert sorted(i for v in FI[r].values() for i in v)==list(range(len(REPORT[r]['inventory'])))
    FI[r]['whole']=list(range(len(REPORT[r]['inventory'])))

FRAMES={}
def frame(r,name):
    key=f'{r}:{name}'
    if key in FRAMES:return FRAMES[key]
    f=U['reader_frames'][key];src=from_union(f['complete_source']);t=SOURCE[src['path']]
    gids=f['groups'];tops=[g for g in gids if not any(p in gids for p in U['complete_own_groups'][g]['containing_groups'])]
    tops.sort(key=lambda g:U['complete_own_groups'][g]['complete_source']['char_start'])
    parts=[];public=[];pos=src['char_start']
    for gid in tops:
        g=U['complete_own_groups'][gid];gs=from_union(g['complete_source']);a,b=gs['char_start'],gs['char_end']
        if pos<a:
            lit=t[pos:a];public.append(lit);parts.append(dict(kind='literal_companion',public_literal=lit,source_ref=register(exact(src['path'],pos,a))))
        own=[gid]+g['contained_groups'];descriptions=[]
        for q in own:
            qg=GM[q];meta={k:deepcopy(qg[k]) for k in GROUP_META if k in qg}
            qsrc=from_union(U['complete_own_groups'][q]['complete_source'])
            meta['exact_source_comments']=[ln for ln in qsrc['literal'].splitlines() if ln.startswith('%')]
            meta['original_map_ref']=rregister(U['complete_own_groups'][q]['raw_group'])
            descriptions.append(meta)
        text='[Reader '+r+' complete own graphical group '+gid+'; editorial descriptor of original fields: '+compact(descriptions)+']'
        public.append(text);parts.append(dict(kind='complete_own_group_descriptor',public_literal=text,source_ref=register(gs),group_ids=own,metadata=descriptions))
        pos=b
    if pos<src['char_end']:
        lit=t[pos:src['char_end']];public.append(lit);parts.append(dict(kind='literal_companion',public_literal=lit,source_ref=register(exact(src['path'],pos,src['char_end']))))
    assert ''.join(REFS[p['source_ref']]['literal'] for p in parts)==src['literal']
    inventories=[dict(original_json_pointer=f'/inventory/{i}',value=deepcopy(REPORT[r]['inventory'][i])) for i in FI[r][name]]
    invrefs=[register(jref(f'out/readers/025/{r}/report.json',f'/inventory/{i}')) for i in FI[r][name]]
    text='Reader '+r+' complete own '+name+' frame, in original source order. Bracketed graphical descriptors below contain only this reader\'s own fields; every replaced source group is exactly recoverable from its source reference.\n'+''.join(public)+'\nComplete own inventory fields in this frame, with their original hand and local candidate scopes:\n'+compact(inventories)
    FRAMES[key]=dict(id=key,reader=r,scope=name,public=text,complete_source_ref=register(src),parts=parts,group_ids=gids,original_inventory_refs=invrefs,source_reconstruction_sha256=sha(src['literal']))
    return FRAMES[key]

# Own proposal fields are projected separately from raw witness/count roles.
OWN_KEYS={'id','location','reading','alternatives','confidence','evidence','reason','scope','local_decisions','source_groups','source_group','group_id','reader_complete_alternatives','reader_semantic_annotation','reader_source_qualification','complete_alternatives','reader_complete_candidates','reader_hand','reader_ownership','reader_printed_qualifier','reader_role_and_attachment','local_hand_scopes','printed_qualifier','kind'}
def reader_fields(locus):
    texts={};details={}
    for r in 'ABC':
        own=locus['readers'][r];fid=own['reading']['complete_frame_ref'];fr=frame(r,fid.split(':')[1])
        local=[];refs={}
        for label,key in [('differences','raw_report_differences'),('doubts','raw_doubts'),('inventory','raw_inventory')]:
            refs[label]=[]
            for rid in own[key]:
                rr=RAW[rid];val=rawval(rr['raw']);ref=rregister(rr['raw']);refs[label].append(ref)
                if label!='inventory':local.append(dict(original_row_id=rid,original_json_pointer=rr['raw']['json_pointer'],own_proposal_fields={k:deepcopy(v) for k,v in val.items() if k in OWN_KEYS}))
        original_C_report_refs=[]
        for canonical in U['canonical_original_C_rows']:
            if canonical['locus']!=locus['id']:continue
            cr=canonical['reader_reported_scopes'][r];cv=rawval(cr);original_C_report_refs.append(rregister(cr))
            excluded={'raw_source_row','literal_source_row','original_row_literal','source_file','source_heading'}
            local.append(dict(original_C_row_identity=canonical['source_id'],original_json_pointer=cr['json_pointer'],original_reader_scope_and_status_fields={k:deepcopy(v) for k,v in cv.items() if k not in excluded}))
        suffix='\nLocal original own-proposal report and doubt fields (their original field roles and order are retained):\n'+compact(local)
        texts[r]=fr['public']+suffix
        details[r]=dict(semantic_role=f'reader_{r}_complete_own_reading_and_own_candidates',complete_own_frame_id=fid,complete_own_literal_source_ref=fr['complete_source_ref'],public_frame_value=fr['public'],public_local_suffix=suffix,
            complete_own_group_ids=own['complete_own_groups'],own_group_refs=[rregister(U['complete_own_groups'][g]['raw_group']) for g in own['complete_own_groups']],
            raw_own_difference_refs=refs['differences'],raw_own_doubt_refs=refs['doubts'],raw_own_local_inventory_refs=refs['inventory'],complete_frame_inventory_refs=fr['original_inventory_refs'],
            report_silent=own['report_silent'],scope_rule='Every candidate and hand/role/attachment scope belongs to this reader and its exact field. Original witness/count flags remain in the raw row references. Report silence supplies no reading.',
            original_C_reader_scope_refs=original_C_report_refs,stage1_locus_reader_mapping=deepcopy(own))
    return texts,details

def attachment(a,b):
    x=exact(DP,a,b);x['workspace_path']=DP;x['path']='checks/scan025_final_draft.tex';x['manifest']='scan025_final_source_map.json';return x
def findspan(lit,start=0,end=None):
    end=len(PAGE) if end is None else end;hits=[m.start()+start for m in re.finditer(re.escape(lit),PAGE[start:end])]
    assert len(hits)==1,(lit,start,end,hits);return attachment(hits[0],hits[0]+len(lit))
def group_attach(gid):
    s=SG[gid]['source'];return attachment(s['char_start'],s['char_end'])
ds=[m.start() for m in re.finditer(re.escape('\\['),PAGE)];de=[m.end() for m in re.finditer(re.escape('\\]'),PAGE)]
archive=PAGE.index('% archive sheet number: 24')
BOUNDS={'whole':(0,len(PAGE)),'opening':(PAGE.index('\n')+1,ds[0]),'display':(ds[0],de[0]),'prose':(de[0],ds[1]),'final':(ds[1],de[1]),'lower':(de[1],archive),'archive':(archive,len(PAGE))}
def region(name):return attachment(*BOUNDS[name])
def observation(sec,start,stop):
    text=SECS[sec]['literal'];a=text.index(start);b=text.index(stop,a);return text[a:b].rstrip()
def crops_for(sec):
    lookup='10' if sec=='19' else sec
    out=[x for x in AUD['viewed_once'] if lookup in x['decision_sections']]
    assert out,(sec,'no once-viewed crop');return out
def group_candidates(gid):
    g=GM[gid]
    return deepcopy(g.get('complete_candidates',g.get('complete_qualified_candidates',g.get('alternatives',[]))))
def final_reading(spec):
    n=spec[0];s=spec[-1]
    if s.startswith('CANDIDATES:'):
        gid=s.split(':')[1];cand=group_candidates(gid);assert cand
        return 'Complete selected states in source order: '+' | '.join(x if isinstance(x,str) else compact(x) for x in cand)+'. '+CANDIDATE_SUFFIX[n]
    return s

DEC=[];BYNUM={};LOCS={};SPEC_BY_N={x[0]:x for x in SPECS}
for spec in SPECS:
    n,loc,sec,gids,conf,kind,cid,start,stop,_=spec;lid=f'L025-{loc:02d}';l=LOC[lid];did=f'SRC025-P{n:02d}'
    reading=final_reading(spec);ev=observation(sec,start,stop);crops=crops_for(sec);readers,details=reader_fields(l)
    source_attachments=[group_attach(g) for g in gids]
    if n==15:source_attachments=[findspan(r'mut\textsuperscript{t}. disjoints')]
    if n==18:source_attachments=[findspan(r'sont \unsure{determinés|determines} en')]
    if n==26:source_attachments=[region('final')]
    if n==27:source_attachments=[findspan(r'disjoints')]
    if n in (24,25):source_attachments.append(region('lower'))
    if n==18:source_attachments.append(region('prose'))
    witness={};wrefs={}
    for w in 'CH':
        wobj=l['witnesses'][w];src=from_union(wobj['source']);wrefs[w]=[src]
        witness[w]=wobj.get('local_graphic_claim') or src['literal']
        if n==21:witness[w]=src['literal']+' [Editorial source scope: this inspected witness phrase supplies no separate point group beside the q descender.]'
    if n==26:
        for w in 'CH':
            t=SOURCE[f'packets/025/{w}.tex'];a=t.rindex(r'\[');b=t.index(r'\]',a)+2;src=exact(f'packets/025/{w}.tex',a,b);wrefs[w]=[src];witness[w]=src['literal']
    if n==27:
        for w in 'CH':
            t=SOURCE[f'packets/025/{w}.tex'];lit='disjoints.' if w=='H' else 'disjoints';a=t.index(lit);src=exact(f'packets/025/{w}.tex',a,a+len(lit));wrefs[w]=[src];witness[w]=lit
    alt=[]
    for g in gids:alt.extend(group_candidates(g))
    if n==18:alt=[r'determinés',r'determines']
    if not alt and n in QUALIFIED:alt=[reading]
    cr=[dict(journal=SECS[sec],crop=x['path'],crop_sha256=x['sha256'],successful_display_count=x['successful_display_count'],observation=ev,original_audit_entry=x,additional_display=False if sec=='19' else None) for x in crops]
    hreason=H_BASIS.get(n,'The exact local H source has no uncertainty or illegibility marker for this selected target; H apparatus from other loci is not propagated here.')
    d=dict(id=did,source_locus_id=lid,location=l['location'],C=witness['C'],H=witness['H'],final=reading,alternatives=alt,readers=readers,
        evidence=ev+' Once-viewed crop: '+', '.join(x['path'] for x in crops)+'.',qualification=reading if n in QUALIFIED else 'Firm selected scope as recorded in the exact root journal section.',confidence=conf,kind=kind,
        diff_C=n<=25,diff_H=True,physical_count_parent=did,root_count_basis='One physical cluster/end-point exactly as authorized in root journal §'+sec+'.',root_count_authorization=SECS[sec],count_status='Root-authorized C25/H27 scalar flags; final record approval pending.',
        marked_in_H=False,H_marker_ids=[],H_marker_basis=dict(local_witness_refs=wrefs['H'],source_catalog='out/checks/scan025_H_marker_catalog.json',scope=hreason,exact_local_apparatus=deepcopy(l['H_exact_apparatus_attachments'])),
        C_doubt_status=('resolved' if n==15 else 'retained') if cid else None,C_source_row_ids=[cid] if cid else [],C_source_part_ids=[cid+'-1'] if cid else [],original_C_contextual_row_ids=[],
        crop=[x['path'] for x in crops],root_crop_evidence=cr,root_ink_choice_applied=True,root_source_audit_choice_applied=True,main_approved=False,log_decision=True,
        selected_group_ids=gids,source_attachments=source_attachments,root_source_attachment_status='Exact selected source attached; final root approval pending.',witness_source_references=wrefs,reader_source_details=details,
        source_printing_authority=SECS['20'] if any(g in ['C025-E02','C025-S04','C025-S05','C025-S06','C025-S07'] for g in gids) else None,
        provenance=dict(stage1_union_path=UP,stage1_union_sha256=sha(SOURCE[UP]),stage1_locus_json_pointer=f'/source_locus_union/{loc-1}',root_journal_section=sec,source_role='C/H literal witness roles; A/B/C complete own-frame roles; selected final and evidence bind only root authority.'))
    DEC.append(d);BYNUM[n]=d;LOCS.setdefault(lid,[]).append(did)

for i,s in enumerate(U['S_source_only_rows'],1):
    raw=rawval(s['raw_scope_ref']);did=f'SRC025-S{i:02d}';readers,details=reader_fields(LOC['L025-28'])
    d=dict(id=did,source_locus_id=f'S025-{i:02d}',location='Supplied source-only S row '+s['S_id'],C='No local scan025 correction is assigned by this source row.',H='No local scan025 correction is assigned by this source row.',
        final='Source-only coverage of '+s['S_id']+'; supplied scope '+raw['where']+' contains no directly quoted local scan025 correction.',alternatives=[],readers=readers,
        evidence='Verified supplied source-scope assignment only. '+S_SCOPE['scope_result'],qualification='Confidence high concerns this source-scope assignment alone; it does not assess ink or mathematics.',
        confidence='high',kind='other',diff_C=False,diff_H=False,physical_count_parent=None,root_count_basis='Root journal §19 explicitly assigns C0/H0 to each of the seven S source-only rows.',root_count_authorization=SECS['19'],count_status='Source-only C0/H0.',
        marked_in_H=False,H_marker_ids=[],H_marker_basis=dict(scope='Nonapplicable: this source-only row has no local H ink locus.'),C_doubt_status=None,C_source_row_ids=[],C_source_part_ids=[],original_C_contextual_row_ids=[],crop=[],root_crop_evidence=[],
        root_ink_choice_applied=False,root_source_audit_choice_applied=True,main_approved=False,log_decision=False,selected_group_ids=[],source_attachments=[region('whole')],root_source_attachment_status='Complete selected page source supplied for scope coverage; no local ink correction attached.',
        witness_source_references={w:[from_union(LOC['L025-28']['witnesses'][w]['source'])] for w in 'CH'},reader_source_details=details,S_id=s['S_id'],S_status=s['S_status'],source_only_scope=deepcopy(raw),proof_event=False,
        provenance=dict(original_S_row_ref=uregister(s['original_tsv_row']),scope_catalog_ref=rregister(s['raw_scope_ref']),root_journal_section_ref=SECTION_REF['19']))
    DEC.append(d)

DOUBTS=[dict(id=f'D025-{n:02d}',decision_id=BYNUM[n]['id'],location=BYNUM[n]['location'],reading=BYNUM[n]['final'],alternatives=BYNUM[n]['alternatives'],confidence=DOUBT_CONFIDENCE[n],reason=BYNUM[n]['evidence']+' '+BYNUM[n]['qualification'],selected_group_ids=BYNUM[n]['selected_group_ids'],source_attachments=deepcopy(BYNUM[n]['source_attachments']),root_crop_evidence=BYNUM[n]['root_crop_evidence'],main_approved=False) for n in sorted(QUALIFIED)]

CS=[]
C_PART_CONF={'C025-R01':'low','C025-R02':'low','C025-R03':'low','C025-R04':'medium','C025-R05':'low','C025-R06':'low','C025-R07':'high','C025-R08':'low'}
catalog=JSON['out/checks/scan025_C_doubt_catalog.json']['canonical_doubt_rows']
for i,raw in enumerate(catalog):
    row=deepcopy(raw);d=next(d for d in DEC if raw['source_id'] in d['C_source_row_ids']);row['original_source_parts']=deepcopy(raw['source_parts']);row['selected_outcome']=d['C_doubt_status'];row['decision_ids']=[d['id']]
    row['source_parts']=[dict(**deepcopy(part),original_decision_status=part['decision_status'],selected_outcome=d['C_doubt_status'],decision_ids=[d['id']],final=d['final'],confidence=C_PART_CONF[raw['source_id']],source_attachments=deepcopy(d['source_attachments']),root_authority=d['root_count_authorization'],main_approved=False) for part in raw['source_parts']]
    row['original_row_reference']=rregister(U['canonical_original_C_rows'][i]['canonical_catalog_ref']);row['reader_reported_scopes']={r:rregister(x) for r,x in U['canonical_original_C_rows'][i]['reader_reported_scopes'].items()}
    if raw['source_id']=='C025-R08':row['selected_local_outcomes']=[dict(scope='initial e acute',outcome='settled absent in both surviving selected whole-word states',authority=SECS['13']),dict(scope='final short oblique trace',outcome='retained as final-acute versus preceding-q-terminal-trace allocation',confidence='low',authority=SECS['13'])]
    CS.append(row)

# Selected inventory: complete source containers coexist with owned child rows.
INV=[]
def inv(position,kind,hand,nums=(),gids=(),sources=None,text=None,original_ids=()):
    iid=f'025.S.{len(INV)+1:02d}';ds=[BYNUM[n] for n in nums]
    if text is None:text=' '.join(d['final'] for d in ds)
    if sources is None:sources=[group_attach(g) for g in gids] or [a for d in ds for a in d['source_attachments']]
    row=dict(sheet_kind='text',hand=hand,element=iid,kind=kind,position=position,first_words_or_objects=text,transcribed='yes',main_approved=False,
        selection_status='Selected source attached; final root record approval pending.',hand_status='Local component and candidate scopes retained exactly.',decision_ids=[d['id'] for d in ds],selected_group_ids=list(gids),source_attachments=deepcopy(sources),source_inventory_identity=iid,source_inventory_role='root-selected',
        source_original_C_inventory_ids=list(original_ids),page_order=len(INV)+1,provenance=dict(root_journal_sections=sorted({SPEC_BY_N[n][2] for n in nums}) or ['19'],original_reader_inventory_rows=[rregister(x['raw']) for x in U['raw_row_correspondence'] if x['section']=='inventory' and x['locus'] in {d['source_locus_id'] for d in ds}]))
    INV.append(row);return row
mixed='his hand for the ordinary writing; candidate-specific independent runs and separately identified local marks retain the undetermined-hand scopes printed in the component descriptions'
def container(name,nums,original_ids=()):
    gids=[g['id'] for g in M['selected_groups'] if BOUNDS[name][0]<=g['source']['char_start'] and g['source']['char_end']<=BOUNDS[name][1]]
    return inv('complete '+name+' source region','display' if name in ['display','final'] else 'text',mixed,nums,gids,[region(name)],'Complete selected '+name+' source, including every intervening word, formula, sign and owned graphical component. '+' '.join(BYNUM[n]['final'] for n in nums),original_ids)
inv('top opening cancelled phrase','deletion','his hand',[1],['C025-G01'],original_ids=['025.01'])
container('opening',range(1,7),['025.02'])
for n,g,cids in [(2,'C025-S01',['025.03']),(3,'C025-G02',['025.04']),(4,'C025-E01',[]),(5,'C025-G03',['025.05']),(6,'C025-G04',[])]:inv(BYNUM[n]['location'],'deletion' if n==5 else 'drawing',GM[g].get('hand','undetermined hand'),[n],[g],original_ids=cids)
container('display',range(7,16),['025.06'])
for n,g,cids in [(7,'C025-G05',['025.07']),(8,'A025-S02',[])]:inv(BYNUM[n]['location'],'drawing',GM[g].get('hand','undetermined hand'),[n],[g],original_ids=cids)
inv('two upper-index traces within selected hatted Sigma','drawing','undetermined hand',[8],['A025-M01'],text='A025-M01 within A025-S02 once: one faint short slash and one dark angular point above alpha. Attachment, role, hand and surface origin remain undetermined; the complete parent glyph is '+BYNUM[8]['final'])
for n,g in [(9,'C025-G06'),(10,'C025-S03'),(11,'C025-E02'),(12,'C025-G07'),(13,'C025-G08'),(14,'C025-S04')]:inv(BYNUM[n]['location'],'deletion' if n==12 else 'drawing',GM[g].get('hand','undetermined hand'),[n],[g],original_ids=['025.08'] if n==12 else ['025.09'] if n==13 else [])
inv('abbreviated mut and disjoints at right edge','text','his hand',[15,27],sources=[findspan(r'mut\textsuperscript{t}. disjoints')])
container('prose',range(16,22),['025.10'])
inv('K revision after Il faut voir que','drawing','his hand',[16],['A025-G09','A025-M02'],original_ids=['025.11','025.12'])
kg=SG['A025-G09']['source'];ktext=PAGE[kg['char_start']:kg['char_end']]
knodes=[m.group() for m in re.finditer(r'\\node[^\n]*;',ktext) if r'\inserted' in m.group()]
assert len(knodes)==1
inv('raised inserted K setminus braced i','insertion','his hand',[16],['A025-G09'],sources=[findspan(knodes[0],kg['char_start'],kg['char_end'])],text=r'Firm raised \inserted{K\setminus\{i\}} within A025-G09; complete parent correction state and long-run scope: '+BYNUM[16]['final'],original_ids=['025.12'])
inv('lower deleted K and looped cancellation','deletion','his hand',[16],['A025-G09'],text=r'Firm \deleted{K} with the parent-owned looped cancellation, preserving the complete replacement state: '+BYNUM[16]['final'],original_ids=['025.11'])
inv('long guide/strike run nested in K revision','drawing','his hand',[16],['A025-M02'],text='The complete curved long run is owned once by A025-M02 inside A025-G09; guide/strike role remains low confidence. '+BYNUM[16]['final'])
inv(BYNUM[17]['location'],'drawing',GM['C025-S05']['hand'],[17],['C025-S05'])
inv('participle after sont with preceding que-descender evidence','text','his hand',[18],sources=BYNUM[18]['source_attachments'])
inv(BYNUM[19]['location'],'drawing',GM['C025-S06']['hand'],[19],['C025-S06'])
ie_source=findspan(' i.e. ',SG['C025-S06']['source']['char_end'],SG['C025-S07']['source']['char_start'])
inv('i.e. between the two lower signed Sigmas','text','his hand',sources=[ie_source],text='i.e. with its dotted i and both written points, ordinary and unexpanded on the selected page. The abbreviation apparatus gives id est under root §21.')
inv(BYNUM[20]['location'],'drawing',GM['C025-S07']['hand'],[20],['C025-S07'])
inv('final que, full q descender and adjacent separate point','drawing','his hand for que and its descender; undetermined hand for the separate point',[21],['B025-G09'])
qg=SG['B025-G09']['source'];qtext=PAGE[qg['char_start']:qg['char_end']];fills=[m.group() for m in re.finditer(r'\\fill[^\n]*;',qtext)];assert len(fills)==1
inv('separate triangular point beside final q descender','drawing','undetermined hand',[21],['B025-G09'],sources=[findspan(fills[0],qg['char_start'],qg['char_end']),group_attach('B025-G09')],text='One separate triangular point to the right of the q descender, with clear separation from the letter paths; its hand, role, attachment and surface origin remain undetermined. '+BYNUM[21]['final'])
container('final',[22,23,26],['025.13'])
inv('left set brace in final display','drawing','his hand',[22],['B025-G08'])
inv('joined-head final Sigma-alpha-minus','drawing','his hand',[23],['A025-S08'])
inv('faint lower-sheet curved mark with detached left foot','drawing','undetermined hand',[24],['B025-M01'],sources=[group_attach('B025-M01'),region('lower')])
inv('two isolated lower-right points','drawing','undetermined hand',[25],['B025-M02'],sources=[group_attach('B025-M02'),region('lower')])
inv('lower-left archive sheet number','text','undetermined hand',sources=[region('archive')],text='Archive sheet number 24, represented by the exact agreed comment % archive sheet number: 24; no printed numeral or additional correction count is introduced.')
assert len(INV)==36,len(INV)

# All selected groups receive complete reciprocal selected relationships.
for g in M['selected_groups']:
    gid=g['id'];dids=[d['id'] for d in DEC if gid in d['selected_group_ids']];assert dids,(gid,'no selected decision')
    g['decision_ids']=dids;g['inventory_ids']=[v['element'] for v in INV if gid in v['selected_group_ids']];assert g['inventory_ids']
    g['selected_readings']=[d['final'] for d in DEC if d['id'] in dids];g['root_sections']=sorted({SPEC_BY_N[n][2] for n,d in BYNUM.items() if d['id'] in dids})
    g['source_attachments']=[group_attach(gid)]
    if gid in ['B025-M01','B025-M02']:g['source_attachments'].append(region('lower'))
    g['role']='current selected complete graphical group; donor fields remain raw provenance'

COVER=[]
for l in U['source_locus_union']:
    lid=l['id'];dids=LOCS.get(lid,[]);ds=[d for d in DEC if d['id'] in dids];name=l['source_frame_kind'];readers,details=reader_fields(l)
    source_attachments=[region(name)];gids=[g['id'] for g in M['selected_groups'] if any(g['id'] in d['selected_group_ids'] for d in ds)]
    if not ds:
        text={'L025-02':'Remaining live opening wording and inclusion companions retained in the complete selected opening source.',
              'L025-20':'The written i.e. remains ordinary and unexpanded between the two complete signed Sigma groups; apparatus expansion id est is authorized by §21.',
              'L025-27':'Archive sheet number 24 remains the exact comment % archive sheet number: 24, hand undetermined.',
              'L025-28':'Complete selected page-region containers, every ordinary companion and all native placement commands are covered by exact source partitions; no new physical count.'}[lid]
        selected=[text]
    else:selected=[d['final'] for d in ds]
    COVER.append(dict(source_locus_id=lid,location=l['location'],decision_ids=dids,selected_readings=selected,source_attachments=source_attachments,selected_group_ids=gids,readers=readers,reader_source_details=details,
        original_main_row_ids=[x['id'] for x in U['raw_row_correspondence'] if x['locus']==lid],root_ink_choice_applied=bool(ds),root_source_audit_choice_applied=True,main_approved=False,root_authority_sections=sorted({SPEC_BY_N[n][2] for n,d in BYNUM.items() if d['id'] in dids}) or ['19']))
M['source_locus_coverage']=deepcopy(COVER)
M['selected_inventory_associations']=[dict(element=v['element'],decision_ids=v['decision_ids'],selected_group_ids=v['selected_group_ids'],source_attachments=v['source_attachments']) for v in INV]
M['record_binding_status']='All selected associations assembled; pending final root approval. Page bytes remain the root-read v02 bytes.'
M['current_root_journal_sha256']=sha(J)
M['historical_assembly_audit']=dict(path='out/checks/scan025_source_assembly_audit_v02.json',sha256=sha(read('out/checks/scan025_source_assembly_audit_v02.json')),scope='Historical execution through §20; unchanged.')
authority_rebindings=[]
def rebind_current_authority(x,path=''):
    if isinstance(x,dict):
        if x.get('path')==JP and x.get('sha256')==old_journal:
            assert x['literal']==J[x['char_start']:x['char_end']]
            for k in ['sha256','sha256_utf8']:
                if k in x:
                    authority_rebindings.append(dict(json_pointer=path+'/'+k,old=x[k],new=sha(J),unchanged_literal_sha256=sha(x['literal'])))
                    x[k]=sha(J)
        for k,v in x.items():rebind_current_authority(v,path+'/'+k.replace('~','~0').replace('/','~1'))
    elif isinstance(x,list):
        for i,v in enumerate(x):rebind_current_authority(v,path+'/'+str(i))
rebind_current_authority(M)
M['current_authority_rebindings']=authority_rebindings
MAPHASH=write(MP,M)
def bind(x):
    if isinstance(x,dict):
        if x.get('path')=='checks/scan025_final_draft.tex':x['source_map_reference']=dict(path=MP,sha256=MAPHASH)
        for v in list(x.values()):bind(v)
    elif isinstance(x,list):
        for v in x:bind(v)

ABBR=[dict(form=r'mut\textsuperscript{t}.',expansion='mutuellement',scope='Probable textual expansion in apparatus only; raised t and abbreviation point are firm on the selected page.',decision_ids=['SRC025-P15'],source_attachments=[findspan(r'mut\textsuperscript{t}.')],root_authority=SECS['21'],raw_reader_proposal_refs=[register(jref(f'out/readers/025/{r}/report.json','/notes')) for r in 'ABC'],H_supplied_letters_ref=rregister(U['H_exact_local_apparatus'][0]['catalog_ref']),main_approved=False),
      dict(form='i.e.',expansion='id est',scope='Textual expansion in apparatus only; manuscript form remains unexpanded on the selected page.',decision_ids=[],source_attachments=[ie_source],root_authority=SECS['21'],raw_reader_proposal_refs=[register(jref(f'out/readers/025/{r}/report.json','/notes')) for r in 'ABC'],main_approved=False)]
NOTES=(r'The page begins with cancelled Soit en effet and then Si on a. Its display writes U_s as X minus the qualified large-union state, with limit alpha in K and a hatted Sigma-alpha-plus; the written conditions and disjointness phrase follow. '
       r'Il faut voir que introduces the cancelled K and raised K\setminus\{i\}, followed by the qualified participle determinés|determines. The two lower signed Sigmas retain their complete local head and short-index alternatives around the written i.e. '
       r'Je dis que precedes the final set expression K\setminus\{i\}=\{\alpha\in I\mid E_\alpha\subset\Sigma_\alpha^-, which ends without a closing brace. The final index remains the written alpha. These are manuscript-attributed readings; no mathematical verification is recorded. '
       r'The forms mut with raised t and point and i.e. remain abbreviated on the page; their apparatus expansions are probable mutuellement and id est. Archive sheet number 24 is retained as the agreed source comment, with hand undetermined.')
NOTE=dict(attributed_only=True,main_approved=False,text=NOTES,source_spans=[region('opening'),region('display'),region('prose'),region('final'),region('archive')],mathematical_check_performed=False,
          attributed_reader_and_root_note_sources=[register(jref(f'out/readers/025/{r}/report.json','/notes')) for r in 'ABC']+[SECTION_REF['13'],SECTION_REF['16'],SECTION_REF['19'],SECTION_REF['21']])
rawrefs=[dict(id=x['id'],reader=x['reader'],section=x['section'],original_index=x['original_index'],original_identity=x['original_identity'],source_locus_id=x['locus'],selected_decision_ids=LOCS.get(x['locus'],[]),raw_row_ref=rregister(x['raw']),all_original_fields=deepcopy(x['all_original_fields'])) for x in U['raw_row_correspondence']]
allmeta=[dict(source_path=x['source_path'],source_sha256_utf8=x['source_sha256_utf8'],complete_original_ref=rregister(x['complete_source'])) for x in U['all_metadata_coverage']]
counts=dict(C=sum(d['diff_C'] for d in DEC),H=sum(d['diff_H'] for d in DEC),decision_loci=len(DEC),physical_decision_rows=27,source_only_S_rows=7,inventory_elements=len(INV),remaining_doubt_loci=len(DOUBTS),check_events=0)
assert counts['C']==25 and counts['H']==27
record=dict(scan=25,folder='J81-03',their_page='24',hua_has='text',filename='J81-03_81_scan025.tex',brief_version='source-record v07; root journal §§01–21',main_adjudicated=False,main_approved=False,
    decisions=DEC,doubts=DOUBTS,inventory=INV,C_source_rows=CS,selected_graphical_groups=deepcopy(M['selected_groups']),source_locus_coverage=COVER,abbreviations=ABBR,notes=NOTES,attributed_content_note=NOTE,root_selected_content_note=deepcopy(NOTE),check_events=[],counts=counts,
    count_status='All scalar choices copied from root journal; final assembled record approval pending.',root_count_authorization=SECS['19'],pending_root_decision_ids=[],root_actions_pending=['Root complete selected-record review and approval, followed by the structural commit gate.'],root_approval_status='pending root final record approval',source_attachment_status='Complete exact selected-source bindings; no rendered or metric claim.',
    selected_draft=dict(path=DP,sha256=sha(PAGE),root_complete_read_proof='out/checks/scan025_root_selected_page_read.json'),selected_source_map=dict(path=MP,sha256=MAPHASH),root_crop_audit=AP,root_viewing_scope=dict(whole_or_half_views=0,total_distinct_crops=18,each_successfully_viewed_once=True,original_audit_sha256=sha(read(AP))),
    workflow_note='Source-only pending assembly from frozen independent returns and root journal. Original source files, historical audits and root viewing history remain exact. No mathematical check, rendering, approval or commit was performed.',
    provenance=dict(frozen_source_union=dict(path=UP,sha256=sha(SOURCE[UP])),frozen_source_skeleton=dict(path='out/checks/scan025_source_row_skeleton_v01.json',sha256=sha(read('out/checks/scan025_source_row_skeleton_v01.json'))),original_lossless_source_pool=dict(path=PP,sha256=sha(read(PP))),source_reference_pool=REFS,
        complete_own_source_frames=FRAMES,reader_candidate_groups=deepcopy(U['complete_own_groups']),raw_main_row_correspondence=rawrefs,all_original_metadata=allmeta,
        original_C_inventory=deepcopy(U['original_C_inventory']),other_C_notation_and_slips_context=deepcopy(U['other_C_notation_and_slips_context']),source_only_S_scope=deepcopy(U['S_scope_authority']),source_role_cautions=deepcopy(U['source_role_cautions']),
        original_H_exact_local_apparatus=deepcopy(U['H_exact_local_apparatus']),historical_assembly_map=dict(path=BASEMP,sha256=sha(read(BASEMP))),root_authority=dict(path=JP,sha256=sha(J),sections=SECTION_REF),frozen_reader_fingerprints=dict(path='out/checks/scan025_reader_fingerprints.json',sha256=sha(read('out/checks/scan025_reader_fingerprints.json')))))
bind(record)
for g in record['selected_graphical_groups']:g['source']=deepcopy(g['source_attachments'][0])
RP='out/checks/scan025_record_draft.json';RH=write(RP,record)

# One source-only construction check; final independent QA replay follows freeze.
errors=[];attachment_count=0
def check_refs(x):
    global attachment_count
    if isinstance(x,dict):
        if x.get('path')=='checks/scan025_final_draft.tex':
            attachment_count+=1;a,b=x['char_start'],x['char_end'];assert x['literal']==PAGE[a:b];assert x['body_sha256']==sha(PAGE[a:b]);assert x['sha256']==sha(PAGE);assert x['source_map_reference']['sha256']==MAPHASH
        for v in x.values():check_refs(v)
    elif isinstance(x,list):
        for v in x:check_refs(v)
check_refs(record)
assert len(DEC)==34 and len(DOUBTS)==19 and len(CS)==8 and len(INV)==36 and len(M['selected_groups'])==25
assert Counter(r['selected_outcome'] for r in CS)=={'retained':7,'resolved':1}
assert all(set(d['readers'])==set('ABC') for d in DEC)
assert not any(d['marked_in_H'] for d in DEC)
assert [d['physical_count_parent'] for d in DEC[:27]]==[d['id'] for d in DEC[:27]]
assert all(g['source']['literal']==g['donor_source']['literal'] for g in M['selected_groups'])
assert len(rawrefs)==216
for p,h in FROZEN['files'].items():assert sha((ROOT/p).read_bytes())==h
for fid,f in FRAMES.items():assert ''.join(REFS[x['source_ref']]['literal'] for x in f['parts'])==REFS[f['complete_source_ref']]['literal']
AUDIT=dict(scan=25,status='source-only record construction passed; pending independent QA and root approval',current_journal_sha256=sha(J),draft_sha256=sha(PAGE),map_sha256=MAPHASH,record_sha256=RH,
    historical_assembly_audit=M['historical_assembly_audit'],historical_map=M['authority_history'][0],selected_page_bytes_changed_since_v02=False,
    selected_group_count=25,selected_command_count=len(M['exact_command_ownership']),reversible_page_replacements=len(M['literal_replacements']),added_outer_unsure_wrappers=0,
    complete_own_frame_count=len(FRAMES),own_frame_exact_reconstruction_passed=True,original_main_row_count=216,canonical_original_C_rows=8,original_C_outcomes=dict(Counter(r['selected_outcome'] for r in CS)),
    counts=counts,confidence_totals={w:dict(Counter(d['confidence'] for d in DEC if d['diff_'+w])) for w in 'CH'},exact_selected_attachment_count=attachment_count,
    new_ink_or_scalar_choices=0,images_opened=0,render_or_metric_validation=False,mathematical_check_events=0,all_37_reader_hashes_unchanged=True,main_adjudicated=False,main_approved=False)
write('out/checks/scan025_source_record_construction_audit_v01.json',AUDIT)
print(compact(dict(record=RP,record_sha256=RH,record_bytes=(ROOT/RP).stat().st_size,map=MP,map_sha256=MAPHASH,map_bytes=(ROOT/MP).stat().st_size,counts=counts,complete_frames=len(FRAMES),exact_selected_attachments=attachment_count)))
