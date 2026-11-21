"""Role-aware record and reversible public review projection; source only."""
from pathlib import Path
import json,hashlib,re,sys,copy
sys.dont_write_bytecode=True
BASE=Path('/workspace/scratch/94548b74fbe0'); OUT=BASE/'out/checks'
sys.path.insert(0,str(OUT))
import scan024_source_support as support
from scan024_source_public_values import FINAL,DOUBT_LOCUS
FINAL={k:v.replace("\\'", "'") for k,v in FINAL.items()}
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes) else x.encode()).hexdigest()
texts={}
def txt(path):
    if path not in texts:texts[path]=(BASE/path).read_text()
    return texts[path]
def js(path):return json.loads(txt(path))
def put(path,x):
    value=x if isinstance(x,str) else json.dumps(x,ensure_ascii=False,indent=2)+'\n'
    (BASE/path).write_text(value);texts[path]=value
def ref(path,a=0,b=None):
    t=txt(path); b=len(t) if b is None else b
    return dict(path=path,sha256=sha(t),char_start=a,char_end=b,
      utf8_byte_start=len(t[:a].encode()),utf8_byte_end=len(t[:b].encode()),
      line_start=t[:a].count('\n')+1,line_end=t[:max(a,b-1)].count('\n')+1,
      body_sha256=sha(t[a:b]),literal=t[a:b])
def at(path,s,start=0):
    a=txt(path).index(s,start);return ref(path,a,a+len(s))
SK='out/checks/scan024_source_row_skeleton_v01.json';S=js(SK);POOL=S['source_reference_pool']
JP='out/checks/scan024_root_decisions.json';J=js(JP);JSP=support.JSONSpans(txt(JP))
AP='out/checks/scan024_root_count_authorization_v2.json';AUTH=js(AP);ASP=support.JSONSpans(txt(AP))
MP='out/checks/scan024_final_source_map.json';M=js(MP)
DP='out/checks/scan024_final_draft.tex';PAGE=txt(DP);assert M['draft_sha256_utf8']==sha(PAGE)
assert sha(txt(AP))=='b4737cf6e63fbbf8a2976138444968498bf5237d85cd0662643f5681adb66c06'
REPORT={r:js(f'out/readers/024/{r}/report.json') for r in 'ABC'}
def pooled(rid):
    f=POOL[rid]['exact_source_ref'];return ref(f['source_path'],f['character_start'],f['character_end_exclusive'])
def raw(rid):return json.loads(pooled(rid)['literal'])
def jp_ref(path,parser,pointer):
    a,b=parser.spans[pointer] if hasattr(parser,'spans') else parser.value[pointer]
    q=ref(path,a,b);q['json_pointer']=pointer;return q
def json_ref(path,pointer):
    parser=support.JSONSpans(txt(path));a,b=parser.spans[pointer]
    f=ref(path,a,b);f['json_pointer']=pointer;return f
def attach(f):
    q=copy.deepcopy(f);q['workspace_path']=DP;q['path']='checks/scan024_final_draft.tex';q['manifest']='scan024_final_source_map.json';return q
G={g['id']:g for g in M['selected_groups']}
def gs(g):return [ref(DP,G[g]['source']['char_start'],G[g]['source']['char_end'])]
def ps(s,start=0):return [at(DP,s,start)]
def unit(uid):
    a=PAGE.index('% BEGIN UNIT '+uid);b=PAGE.index('% END UNIT '+uid,a)+len('% END UNIT '+uid)
    return ref(DP,a,b)
UNITS={u:unit(u) for u in ['P1','D1','P2','P3','P4','P5','ARCHIVE']}
def node_with(s):
    hit=PAGE.index(s)
    nodes=[c['selected_source'] for c in M['exact_command_ownership'] if c['command']=='node' and c['selected_source']['char_start']<=hit<c['selected_source']['char_end']]
    f=min(nodes,key=lambda n:n['char_end']-n['char_start']);return [ref(DP,f['char_start'],f['char_end'])]
LOC={1:ps(r'\unsure{Considerons|Considérons} la partition'),2:ps(r'\Pi_I^{\unsure{\circ|0}}'),3:gs('A024-G01'),4:gs('A024-G02'),5:gs('C024-M01'),6:ps("$S$ l'ens des classes"),7:ps(r'\unsure{notées|notèes|notees} $U_s$'),8:gs('A024-G03')+ps('Considérons la'),9:ps('Considérons la'),10:gs('A024-G04'),11:gs('A024-G04'),12:gs('A024-G04'),13:gs('A024-G05'),14:gs('A024-G05'),15:gs('C024-G05'),16:gs('C024-G05'),17:[UNITS['D1']],18:ps(r'\uline{Lemme} Cette relation fait de'),19:gs('A024-G06'),20:gs('A024-G07'),21:gs('A024-G10'),22:node_with(r'\unsure{ens des|ens de}'),23:gs('B024-G06'),24:node_with(r"\unsure{de aretes|d'aretes"),25:node_with(r"\unsure{de aretes|d'aretes"),26:ps('}.).'),27:node_with(r'\rlap{Cette relation}'),28:gs('A024-G08')+node_with('at (1229,1035)'),29:node_with(r'est un \uline{arbre}'),30:ps(r'\unsure{le|Le}'),31:gs('A024-G11'),32:gs('A024-G11'),33:gs('R024-GEX'),34:gs('B024-G09'),35:ps(r'exactement deux $U_s$ tels que $\overline{U_s}\cap E_i\ne\varnothing$'),36:ps(r"par \unsure{l'ens|l'une} de ces deux $U_s$"),37:ps(r'\unsure{Soient|Soit}'),38:gs('A024-G13'),39:gs('A024-G14'),40:gs('A024-G15'),41:gs('A024-G15'),42:ps(r'\unsure{prècise|précise|prêcise|precise}'),43:ps('en :'),44:gs('A024-G16'),45:ps(r'\unsure{exactemt|exactement}'),46:ps(r'\uline{un}'),47:gs('A024-G17'),48:gs('A024-G17'),49:ps('contenu dans'),50:gs('A024-G18'),51:ps('tel que',G['A024-G18']['source']['char_end']),52:gs('A024-G19'),53:gs('A024-G19'),54:ps('(et de $=$ pour'),55:gs('A024-G20'),56:ps(r'\unsure{de|dé|qui}'),57:gs('B024-G11'),58:gs('B024-G11'),59:ps(r'un $U_{s_-}\subset$'),60:ps(r'$U_{s_-}\subset$')+gs('C024-S05'),61:ps('tel que',G['C024-S05']['source']['char_end']),62:ps(r'$\overline{U_{s_-}}\cap E_i\ne\varnothing$'),63:gs('A024-G22'),64:ps(r'\scanpage{24}')+ps('% archive sheet number: 23')}
LOC['33a']=LOC[33]
# The exact source frame projection uses explicit editorial group placeholders.
# Its token stream reconstructs every original byte; no candidate field changes.
FRAMES={};FRAME_REPLAY=[];PUBLIC_PARTS={}
def group_description(role,gid):
    st=S['complete_own_group_candidate_scopes'][role][gid]
    f=pooled(st['complete_own_TeX_ref']); comments='\n'.join(x for x in f['literal'].splitlines() if x.startswith('%') and 'BEGIN' not in x and 'END' not in x)
    content='Own candidate/state fields: '+json.dumps(st['raw_own_state_fields'],ensure_ascii=False,separators=(',',':'))
    if comments:content+='\nOwn literal source comments: '+comments
    # Include separately owned children, whose candidate scopes survive the parent.
    children=[]
    for cg,cs in S['complete_own_group_candidate_scopes'][role].items():
        cf=pooled(cs['complete_own_TeX_ref'])
        if cg!=gid and f['char_start']<=cf['char_start'] and cf['char_end']<=f['char_end']:
            children.append(cg)
    for cg in children:
        cs=S['complete_own_group_candidate_scopes'][role][cg]
        content+='\nOwn contained group '+cg+': '+json.dumps(cs['raw_own_state_fields'],ensure_ascii=False,separators=(',',':'))
    return '[Editorial own-source group description '+gid+'; '+content+'; exact literal group '+f['path']+' chars['+str(f['char_start'])+','+str(f['char_end'])+'), SHA '+f['sha256']+'.]'
def frame(rid,role):
    key=role+':'+rid
    if key in FRAMES:return FRAMES[key]['public']
    f=pooled(rid);t=f['literal'];candidates=[]
    for gid,st in S['complete_own_group_candidate_scopes'][role].items():
        if re.match(r'[ABC]024-(?:P\d|ADMIN|ARCHIVE|DISPLAY)',gid):continue
        gf=pooled(st['complete_own_TeX_ref'])
        if gf['path']==f['path'] and f['char_start']<=gf['char_start'] and gf['char_end']<=f['char_end']:
            candidates.append((gf['char_start']-f['char_start'],gf['char_end']-f['char_start'],gid,gf))
    candidates.sort(key=lambda x:(x[0],-x[1])); chosen=[];end=-1
    for x in candidates:
        if x[0]>=end:chosen.append(x);end=x[1]
    parts=[];cursor=0;replay=[]
    for a,b,gid,gf in chosen:
        parts.append(t[cursor:a]);d=group_description(role,gid);parts.append(d)
        replay.append(dict(original_start=a,original_end=b,public_start=sum(len(x) for x in parts[:-1]),public_end=sum(len(x) for x in parts),original_literal=gf['literal'],public_value=d,group_id=gid));cursor=b
    parts.append(t[cursor:]);p=''.join(parts);back=p
    for x in reversed(replay):back=back[:x['public_start']]+x['original_literal']+back[x['public_end']:]
    assert back==t,key
    public='Complete own containing source frame (graphical blocks use explicitly editorial own-source descriptions; other words/macros retain source order):\n'+p+'\nExact own frame: '+f['path']+' chars['+str(f['char_start'])+','+str(f['char_end'])+'), SHA '+f['sha256']+'. Other local qualifications in this containing frame retain their own scopes.'
    FRAMES[key]=dict(public=public,exact_source=f,group_projection=replay,reconstruction_exact=True)
    return public
def reader_value(row,role):
    r=row['readers'][role];chunks=[]
    # Merge exact contexts by containment, preserving standalone adjacent groups.
    ids=[]
    for rid in r['complete_own_literal_scope_refs']:
        f=pooled(rid)
        if any(pooled(x)['path']==f['path'] and pooled(x)['char_start']<=f['char_start'] and f['char_end']<=pooled(x)['char_end'] for x in ids):continue
        ids.append(rid)
    for rid in ids:chunks.append(frame(rid,role))
    local=[]
    for rid in r['raw_own_difference_refs']:
        v=raw(rid);own={k:v[k] for k in ['id','reading','alternatives','qualification','C_doubt_status','source_group','source_groups'] if k in v}
        local.append(own)
    for rid in r['raw_own_doubt_refs']:
        v=raw(rid);own={k:v[k] for k in ['id','reading','alternatives','qualification','source_group','source_groups'] if k in v}
        if own not in local:local.append(own)
    if local:chunks.append('Own local report/doubt fields (verbatim values; complete source/group scopes above remain controlling): '+json.dumps(local,ensure_ascii=False,separators=(',',':')))
    else:chunks.append('The inspected complete difference list has no row for this source correspondence; the exact own TeX frame above supplies this reader’s actual text. This absence statement is bounded by that complete report and frame.')
    PUBLIC_PARTS[(row['id'],role)]=chunks
    return '\n\n'.join(chunks)
ROOT_BY_LOC={loc:(i,d) for i,d in enumerate(J['decisions']) for loc in d['source_loci']}
def root_evidence(lid):
    if lid in ROOT_BY_LOC:
        i,d=ROOT_BY_LOC[lid]
        return d['evidence']+' Once-viewed crop: '+d['crop_path']+'.',d,[dict(journal=json_ref(JP,f'/decisions/{i}'),crop=d['crop_path'],crop_sha256=d['crop_sha256'],successful_display_count=1,observation=d['evidence'])]
    return 'Source-only complete shared context inspected in all three released reader TeX returns and both witness texts. Root authorized its retention without a new local image; no crop observation is asserted for this correspondence.',None,[]
def selected_groups(fs):
    result=[]
    for gid,g in G.items():
        a,b=g['source']['char_start'],g['source']['char_end']
        if any(f['char_start']<b and a<f['char_end'] for f in fs):result.append(gid)
    return result
def witness_value(row,role,key):
    fs=[pooled(x) for x in row[role]['complete_own_literal_scope_refs']]
    v='\n'.join(x['literal'] for x in fs)
    if key==4 and role=='C':
        p='packets/024/C_doubts.txt';notation=txt(p).splitlines(keepends=True)[3];nr=at(p,notation)
        v+='\n[Editorial own-source scope note: witness C’s notation explicitly gives alpha-prime/i both under the union and after E; its unwrapped repeated E index retains that recurring qualification. Complete local witness states E_{\\alpha\'} | E_i. Exact notation row: '+notation.rstrip()+'.]'
        fs.append(nr)
    if key in {5,14,21,23,31,34,41,48,58}:
        v+='\n[Editorial local-scope note: this exact witness context supplies no separate mark/trace inscription for the target identified by this row; its printed word/formula context is quoted above.]'
    return v,fs
DEC=[]
for ai,a in enumerate(AUTH['rows']):
    lid=a['source_locus_id'];row=S['rows'][int(lid.rsplit('L',1)[1])-1];k='33a' if a['id'].endswith('33a') else int(lid.rsplit('L',1)[1])
    evidence,rd,rootrefs=root_evidence(lid)
    cv,cf=witness_value(row,'C',k);hv,hf=witness_value(row,'H',k)
    rr={r:reader_value(row,r) for r in 'ABC'}
    cr=[] if k=='33a' else row['original_C_source_row_ids']
    statuses=[]
    for x in cr:
        if x in AUTH['canonical_C_parents']['resolved']:statuses.append(x+': resolved')
        elif x in AUTH['canonical_C_parents']['mixed']:statuses.append(x+(': punctuation scope resolved; accent scope retained' if k==26 else ': accent scope retained; punctuation scope resolved'))
        else:statuses.append(x+': retained')
    d=dict(id=a['id'],source_locus_id=lid,location=a['location'],C=cv,H=hv,final=FINAL[k],alternatives=[],readers=rr,
      evidence=evidence,qualification=rd['decision'] if rd else 'Complete source consensus retained; source-only context.',confidence=a['confidence'],kind='other',
      diff_C=a['diff_C'],diff_H=a['diff_H'],physical_count_parent=a['count_parent'],root_count_basis=a['root_count_basis'],
      root_count_authorization=json_ref(AP,f'/rows/{ai}'),count_status='Exact root-authorized scalar flags and physical parents; final record approval pending.',
      marked_in_H=(k==56),H_marker_ids=['H024-ILL01'] if k==56 else [],H_marker_basis=dict(local_witness_refs=hf,source_catalog='out/checks/scan024_H_marker_catalog.json',scope='Exact local ill marker before definit.' if k==56 else 'No actual H uncertainty/illegibility marker at this target; a marker in containing context retains its own local scope.'),
      C_doubt_status='; '.join(statuses) or None,C_source_row_ids=cr,C_source_part_ids=[x+'-1' for x in cr],original_C_contextual_row_ids=row['original_C_contextual_row_ids'] if k!='33a' else [],
      crop=[rd['crop_path']] if rd else [],root_crop_evidence=rootrefs,root_ink_choice_applied=bool(rd),root_source_audit_choice_applied=True,
      main_approved=False,log_decision=True,selected_group_ids=selected_groups(LOC[k]),source_attachments=[attach(f) for f in LOC[k]],
      root_source_attachment_status='Exact selected source attached; root final record approval pending.',witness_source_references=dict(C=cf,H=hf),
      reader_source_details=copy.deepcopy(row['readers']),
      provenance=dict(source_skeleton_reference=dict(path=SK,sha256=sha(txt(SK)),json_pointer='/rows/'+str(int(lid.rsplit('L',1)[1])-1)),source_role='C/H retain witness-own literals; A/B/C retain reader-own frames and complete candidates; selected/evidence carry only root authority.'))
    if k=='33a':d['provenance']['physical_subrow_scope']='Root-authorized live Il case target under source correspondence L33; actual C R10 remains on cancelled-word L33 only.'
    if k in {2,3,4,19,38,39,47,50,52,53,55,60}:
        d['mathematical_consequence']='Attributed source readings only. Witness C writes '+cv+'; witness H writes '+hv+'; the selected local source records '+FINAL[k]+' No mathematical identity, implication or proof is asserted.'
    DEC.append(d)
# Seven source-only S rows have no invented local quotation or image attachment.
SP='out/checks/scan024_S_scope.json';SC=js(SP)
for i,s in enumerate(SC['row_scopes']):
    sid=f'SRC024-S{i+1:02d}';state='Source-only scope review: '+s['where']+'. No directly quoted scan024 ink locus is supplied by this S row.'
    if s['id']=='SA01-K81-07':state+=' Its broad index range supplies no local scan024 transcription correction.'
    readers={r:'Source-only correspondence. The complete released reader '+r+' source is retained at out/readers/024/'+r+'/reading.tex (SHA '+sha(txt(f'out/readers/024/{r}/reading.tex'))+'); no local reader phrase is invented for this S scope row. This statement is bounded by the supplied S row scope and the complete frozen reader return.' for r in 'ABC'}
    DEC.append(dict(id=sid,source_locus_id=sid,location='Witness S '+s['id'],C='[Editorial source-only field: no local C quotation supplied for this S scope row.]',H='[Editorial source-only field: no local H quotation supplied for this S scope row.]',final=state,alternatives=[],readers=readers,evidence=SC['scope_result'],qualification='Source scope only; S assertions/classifications remain attributed raw source.',confidence='high',kind='other',diff_C=False,diff_H=False,physical_count_parent=sid,root_count_basis='Root authorization: each supplied S row is C0/H0 with source-scope confidence high.',root_count_authorization=dict(path=AP,sha256=sha(txt(AP)),json_pointer='/scope_rules/4'),count_status='Root-authorized source-only zero counts; final approval pending.',marked_in_H=False,H_marker_ids=[],C_doubt_status=None,C_source_row_ids=[],C_source_part_ids=[],crop=[],root_crop_evidence=[],root_ink_choice_applied=False,root_source_audit_choice_applied=True,S_id=s['id'],S_status=state,main_approved=False,log_decision=True,selected_group_ids=[],source_attachments=[],source_scope_reference=json_ref(SP,f'/row_scopes/{i}'),provenance=dict(raw_S_scope=s,whole_S_scope=ref(SP))))
BY_ID={d['id']:d for d in DEC}
DOUBTS=[]
for n in sorted(DOUBT_LOCUS):
    d=BY_ID[f'SRC024-L{n:02d}']
    DOUBTS.append(dict(id=f'Q024-L{n:02d}',decision_id=d['id'],location=d['location'],reading=d['final'],alternatives=d['alternatives'],confidence=d['confidence'],reason=d['evidence']+' Selected local scope: '+d['final'],selected_group_ids=d['selected_group_ids'],source_attachments=copy.deepcopy(d['source_attachments']),root_crop_evidence=copy.deepcopy(d['root_crop_evidence']),main_approved=False))
# Keep original C row/part identities; add typed component outcomes separately.
CAT=js('out/checks/scan024_C_doubt_catalog.json');CROWS=[]
for row in CAT['rows']:
    x=copy.deepcopy(row);cid=x['source_id'];ids=[d['id'] for d in DEC if cid in d.get('C_source_row_ids',[])]
    outcome='resolved' if cid in AUTH['canonical_C_parents']['resolved'] else 'mixed' if cid in AUTH['canonical_C_parents']['mixed'] else 'retained'
    for p in x['source_parts']:
        p.update(selected_outcome=outcome,decision_ids=ids,main_approved=False,source_attachments=[a for did in ids for a in BY_ID[did]['source_attachments']])
    x.update(selected_outcome=outcome,decision_ids=ids,main_approved=False)
    if cid=='C024-R02':x['component_scopes']=[dict(scope='union index',decision_ids=['SRC024-L03'],outcome='retained'),dict(scope='E index',decision_ids=['SRC024-L04'],outcome='retained',original_recurring_qualification=True)]
    if cid=='C024-R09':x['component_scopes']=[dict(scope='noun accents',decision_ids=['SRC024-L25'],outcome='retained'),dict(scope='endpoint',decision_ids=['SRC024-L26'],outcome='resolved',reading='.).')]
    if cid=='C024-R13':x['contextual_occurrences']=[dict(decision_id='SRC024-L52',scope='Later barred-U occurrence; contextual in original row, without an additional original part identity.')]
    CROWS.append(x)
# Retain A inventory identities; current descriptions refer to selected content.
INV=[]
inventory_loci={1:list(range(1,10)),2:[3],3:[3],4:[4],5:[4],6:[8],7:[8],8:[11],9:[10],10:[12],11:list(range(13,18)),12:[13],13:[14],14:[18,19],15:[19],16:list(range(20,30)),17:[20],18:[21],19:[26],20:[27],21:[28],22:[29],23:list(range(30,37)),24:[32],25:[31],26:[32],27:[33],28:list(range(37,64)),29:[38],30:[39],31:[40],32:[41],33:[44],34:[46],35:[47],36:[47],37:[48],38:[50],39:[50],40:[52,53],41:[53],42:[53],43:[54],44:[55],45:[56],46:[57,58],47:[59,60,61,62],48:[63],49:[64]}
whole_units={1:'P1',11:'D1',14:'P2',16:'P3',23:'P4',28:'P5',49:'ARCHIVE'}
def add_inv(role,index,loci,whole=None,component_scope=None):
    old=REPORT[role]['inventory'][index];x={k:copy.deepcopy(old[k]) for k in ['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']}
    dids=[f'SRC024-L{n:02d}' for n in loci];ds=[BY_ID[i] for i in dids]
    x['first_words_or_objects']=' '.join(d['final'] for d in ds)
    if component_scope:x['first_words_or_objects']=component_scope+' Containing selected state: '+x['first_words_or_objects']
    # Whole regions and word-bearing groups explicitly retain attached unknown hands.
    mixed=whole is not None and whole not in {'P2','ARCHIVE'} or (role=='A' and index+1 in {6,12,16,21,24,27,29,30,31,35,38,40,41,44,46,47})
    if mixed and x['hand']=='his hand':x['hand']='his hand; separately identified local marks/traces: undetermined hand'
    x.update(main_approved=False,selection_status='Selected source attached; root final record approval pending.',hand_status='Local selected component scopes retained; root final approval pending.',decision_ids=dids,selected_group_ids=list(dict.fromkeys(g for d in ds for g in d['selected_group_ids'])),source_inventory_identity=old['element'],source_inventory_role=role,source_attachments=[attach(UNITS[whole])] if whole else [copy.deepcopy(a) for d in ds for a in d['source_attachments']],provenance=dict(raw_inventory=old,exact_original=json_ref(f'out/readers/024/{role}/report.json',f'/inventory/{index}')))
    INV.append(x)
for i in range(49):
    n=i+1;add_inv('A',i,inventory_loci[n],whole_units.get(n))
    if n==5:add_inv('C',1,[5],component_scope='One high diamond above soit; undetermined hand, role, attachment and surface origin.')
    if n==16:add_inv('B',14,[23],component_scope='One high triangular sommets point; local attachment, role and hand remain undetermined.')
    if n==21:add_inv('B',17,[28],component_scope='One detached upper Le/Ce return; its local attachment/role and hand remain undetermined.')
    if n==27:add_inv('B',23,[34],component_scope='Two interrupted pale entry pieces in the live y/a continuation; their hand and attachment remain undetermined.')
    if n==29:add_inv('C',30,[38],component_scope='Upper head/retrace or independent run, with locally undetermined hand; selected literal geometry is A024-G13.')
    if n==30:add_inv('C',32,[39],component_scope='Upper head/retrace or independent run, with locally undetermined hand; selected literal geometry is A024-G14.')
    if n==46:add_inv('B',35,[58],component_scope='Final-i upper pair: pale upright/darker top and separate dark fleck; attachment and hand remain undetermined.')
for i,x in enumerate(INV):x['page_order']=i+1
ABBR=[]
for form,expansion,loci in [('ens','ensemble',[6,22,36]),('ens.','ensemble',[22]),('def','définition',[15]),('comp.','composantes',[40]),('conn','connexes',[40]),('exactemt','exactement',[45]),('de $=$','de même',[54])]:
    ABBR.append(dict(form=form,expansion=expansion,scope='Probable expansion in apparatus only; selected manuscript form stays unchanged.',decision_ids=[f'SRC024-L{x:02d}' for x in loci],source_attachments=[a for n in loci for a in BY_ID[f'SRC024-L{n:02d}']['source_attachments']],main_approved=False))
NOTES="The sheet introduces the qualified partition exponent and the classes $U_s$, then writes the defining relation using $\\overline{U_s}\\cap E_i\\ne\\varnothing$. Its underlined Lemme calls the graph strict and an underlined arbre. The next paragraph writes exactly two $U_s$ in condition a), and the complete l'ens/l'une phrase in condition b). The signed-component passage retains the local sign and index alternatives, the written de $=$, and a single live underlined un. These are attributed manuscript statements.\n\nThe upper underlined Lemme and quantified clause are cancelled beneath the raised Relation R entre S et I. The cancelled On a/On, predecessor U/E, three tuple states, cancelled Cette relation and cancelled existe/ex retain their complete visible continuations. The abbreviations remain written as ens, ens., def, comp., conn and exactemt. Archive numeral 23 is retained in a comment with undetermined hand. No mathematical check event was performed."
CONTENT=dict(attributed_only=True,main_approved=False,text=NOTES,source_spans=[attach(UNITS[x]) for x in ['P1','D1','P2','P3','P4','P5','ARCHIVE']],mathematical_check_performed=False)
for g in M['selected_groups']:
    gid=g['id'];ds=[d for d in DEC if gid in d['selected_group_ids']]
    g.update(decision_ids=[d['id'] for d in ds],selected_readings={d['id']:d['final'] for d in ds},inventory_ids=[x['element'] for x in INV if gid in x['selected_group_ids']],root_journal_sections=sorted({ROOT_BY_LOC[d['source_locus_id']][1]['section'] for d in ds if d['source_locus_id'] in ROOT_BY_LOC}),source_attachments=[attach(ref(DP,g['source']['char_start'],g['source']['char_end']))])
COVER=[]
for row in S['rows']:
    ds=[d for d in DEC if d['source_locus_id']==row['id']]
    COVER.append(dict(source_locus_id=row['id'],decision_ids=[d['id'] for d in ds],selected_readings={d['id']:d['final'] for d in ds},source_attachments=[a for d in ds for a in d['source_attachments']],selected_group_ids=list(dict.fromkeys(g for d in ds for g in d['selected_group_ids'])),reader_source_details=copy.deepcopy(row['readers']),root_ink_choice_applied=any(d['root_ink_choice_applied'] for d in ds),root_source_audit_choice_applied=True,main_approved=False))
M['source_locus_coverage']=COVER
M['authority']['root_count_authorization']=dict(path=AP,sha256=sha(txt(AP)))
M['authority']['section15_source_clarification']=ref('out/checks/scan024_source_section15_clarification.json')
M['declared_import_correspondences']=[dict(group='B024-G06',parent='A024-G07',source_anchor='Selected existing A node (329,981), font=\\small; complete B group retains x=1ex,y=1ex, baseline=(sommets.base), own origin (0,0).',coordinate_rule='All coordinate labels copied literally; no physical-scale equality or coordinate transformation is claimed.'),dict(group='R024-GEX',components=['C024-G11 prefix','B024-G09 complete continuation'],source_clarification=ref('out/checks/scan024_source_section15_clarification.json'),coordinate_rule='Separate original pt/ex declarations and baselines are retained; the prefix reservation change and phantom removal are recorded exactly.')]
put(MP,M);M_HASH=sha(txt(MP))
def bind_map(x):
    if isinstance(x,dict):
        if x.get('path')=='checks/scan024_final_draft.tex':x['source_map_reference']=dict(path=MP,sha256=M_HASH)
        for v in list(x.values()):bind_map(v)
    elif isinstance(x,list):
        for v in x:bind_map(v)
R=dict(scan=24,folder='J81-03',their_page='23',hua_has='text',filename='J81-03_81_scan024.tex',brief_version='v07',main_adjudicated=False,main_approved=False,
 decisions=DEC,doubts=DOUBTS,inventory=INV,C_source_rows=CROWS,selected_graphical_groups=copy.deepcopy(M['selected_groups']),source_locus_coverage=copy.deepcopy(COVER),abbreviations=ABBR,notes=NOTES,attributed_content_note=CONTENT,root_selected_content_note=copy.deepcopy(CONTENT),check_events=[],counts=dict(C=sum(d['diff_C'] for d in DEC),H=sum(d['diff_H'] for d in DEC),decision_loci=len(DEC),physical_decision_rows=len(AUTH['rows']),source_only_S_rows=7,inventory_elements=len(INV),remaining_doubt_loci=len(DOUBTS),check_events=0),count_status='Exact root authorization v2 applied; final record approval pending.',root_count_authorization=dict(path=AP,sha256=sha(txt(AP))),pending_root_decision_ids=[],root_actions_pending=['Root final selected-source/map/record review and approval.'],root_approval_status='Unapproved draft.',source_attachment_status='Exact selected-draft attachments prepared; root final approval pending.',selected_draft=dict(path='checks/scan024_final_draft.tex',sha256=sha(PAGE)),selected_source_map=dict(path=MP,sha256=M_HASH),root_crop_audit='checks/scan024_root_crop_audit.json',root_viewing_scope=dict(distinct_once_viewed=30,reused_reader_crops=26,new_root_crops=4,whole_or_halves_seen_by_root=False),workflow_note='All three full returns and full pairwise TeX diffs were read by root before its first image. Root recorded thirty distinct once-only local crop decisions. The source clerk used text and frozen references only.',provenance=dict(frozen_source_union=dict(path='out/checks/scan024_source_union_v01.json',sha256=sha(txt('out/checks/scan024_source_union_v01.json'))),frozen_source_skeleton=dict(path=SK,sha256=sha(txt(SK))),reader_candidate_groups=S['complete_own_group_candidate_scopes'],source_reference_pool=POOL,source_role_cautions=S['source_role_cautions'],original_count_authorization_v1=dict(path='out/checks/scan024_root_count_authorization.json',sha256=sha(txt('out/checks/scan024_root_count_authorization.json'))),source_only_S_scope=SC,complete_reader_reports={r:dict(path=f'out/readers/024/{r}/report.json',sha256=sha(txt(f'out/readers/024/{r}/report.json'))) for r in 'ABC'},complete_own_source_frames='out/checks/scan024_source_reader_frame_projection.json'))
bind_map(R)
assert R['counts']['C']==33 and R['counts']['H']==49
assert all(set(d['readers'])==set('ABC') for d in DEC)
assert [d['id'] for d in DEC if d['marked_in_H']]==['SRC024-L56']
assert len(CROWS)==18 and len({p['part_id'] for c in CROWS for p in c['source_parts']})==18
put('out/checks/scan024_record_draft.json',R)
put('out/checks/scan024_source_reader_frame_projection.json',dict(scan=24,role_separation=True,frames=FRAMES,exact_reconstruction_all=True))
# Reversible public-field projection: shared frame/evidence values occur once.
# Every actual public string and scalar is reconstructed from explicit parts.
PV={};rev={}
def intern(value):
    k=json.dumps(value,ensure_ascii=False,sort_keys=True)
    if k not in rev:
        rid=f'V{len(PV)+1:04d}';rev[k]=rid;PV[rid]=value
    return rev[k]
def string_parts(value):
    # Split only known exact own-frame values; no altered semantic text.
    matches=[]
    for v in FRAMES.values():
        p=v['public'];a=value.find(p)
        if a>=0:matches.append((a,a+len(p),p))
    matches.sort(key=lambda x:(x[0],-x[1]));out=[];pos=0
    for a,b,p in matches:
        if a<pos:continue
        if a>pos:out.append(intern(value[pos:a]))
        out.append(intern(p));pos=b
    if pos<len(value):out.append(intern(value[pos:]))
    if not out:out=[intern(value)]
    assert ''.join(PV[x] for x in out)==value
    return {'concat':out}
PUBKEYS=['id','source_locus_id','location','C','H','final','alternatives','readers','evidence','qualification','confidence','kind','diff_C','diff_H','physical_count_parent','root_count_basis','marked_in_H','C_doubt_status','C_source_row_ids','C_source_part_ids','original_C_contextual_row_ids','crop','selected_group_ids','S_id','S_status','mathematical_consequence','root_ink_choice_applied','root_source_audit_choice_applied','main_approved']
def project(x):
    if isinstance(x,str):return string_parts(x)
    if isinstance(x,list):return [project(v) for v in x]
    if isinstance(x,dict):return {k:project(v) for k,v in x.items()}
    return x
def restore(x):
    if isinstance(x,dict) and set(x)=={'concat'}:return ''.join(PV[r] for r in x['concat'])
    if isinstance(x,dict):return {k:restore(v) for k,v in x.items()}
    if isinstance(x,list):return [restore(v) for v in x]
    return x
PUBLIC=dict(decisions=[{k:d[k] for k in PUBKEYS if k in d} for d in DEC],doubts=[{k:d[k] for k in ['id','decision_id','location','reading','alternatives','confidence','reason','selected_group_ids','main_approved']} for d in DOUBTS],inventory=[{k:x[k] for k in ['element','sheet_kind','hand','kind','position','first_words_or_objects','transcribed','decision_ids','selected_group_ids','page_order','main_approved']} for x in INV],C_source_rows=[{k:x[k] for k in ['source_id','selected_outcome','decision_ids','source_parts','component_scopes','contextual_occurrences'] if k in x} for x in CROWS],abbreviations=[{k:x[k] for k in ['form','expansion','scope','decision_ids','main_approved']} for x in ABBR],notes=NOTES,counts=R['counts'])
# C current parts omit only attachment bulk in this public view; identity/status stay.
for x in PUBLIC['C_source_rows']:
    x['source_parts']=[{k:v for k,v in p.items() if k!='source_attachments'} for p in x['source_parts']]
PROJ=project(PUBLIC);assert restore(PROJ)==PUBLIC
projection=dict(scan=24,record_path='out/checks/scan024_record_draft.json',record_sha256=sha(txt('out/checks/scan024_record_draft.json')),reconstruction='Replace each {concat:[V...]} object with exact string concatenation of listed values; scalar/list/dict structure otherwise unchanged.',public_field_selection=PUBKEYS,values=PV,public_fields=PROJ,exact_public_reconstruction=True,main_approved=False)
put('out/checks/scan024_source_public_projection.json',projection)
lines=[json.dumps({'kind':'metadata',**{k:v for k,v in projection.items() if k not in ['values','public_fields']}},ensure_ascii=False)]
lines += [json.dumps(dict(kind='value',id=k,value=v),ensure_ascii=False) for k,v in PV.items()]
for section,values in PROJ.items():
    if isinstance(values,list):lines.extend(json.dumps(dict(kind='public_row',section=section,index=i,value=v),ensure_ascii=False) for i,v in enumerate(values))
    else:lines.append(json.dumps(dict(kind='public_field',section=section,value=values),ensure_ascii=False))
put('out/checks/scan024_source_public_projection.jsonl','\n'.join(lines)+'\n')
audit=dict(scan=24,source_only=True,main_approved=False,draft_sha256_utf8=sha(PAGE),source_map_sha256=M_HASH,record_sha256=sha(txt('out/checks/scan024_record_draft.json')),public_projection_sha256=sha(txt('out/checks/scan024_source_public_projection.json')),root_count_authorization_sha256=sha(txt(AP)),counts=R['counts'],canonical_C_outcomes={state:sum(x['selected_outcome']==state for x in CROWS) for state in ['resolved','mixed','retained']},all_public_reader_roles_complete=True,all_own_frames_exactly_reconstruct=True,public_projection_reconstructs_exactly=True,sole_H_marker_row='SRC024-L56',selected_source_attachments_checked=True,actual_C_rows=18,actual_C_parts=18,all_approvals_false=True,remaining_actions=['Independent source QA and root complete public/map/record review; approval remains pending.'])
put('out/checks/scan024_source_record_audit_v01.json',audit)
print(json.dumps(audit,ensure_ascii=False,indent=2))
