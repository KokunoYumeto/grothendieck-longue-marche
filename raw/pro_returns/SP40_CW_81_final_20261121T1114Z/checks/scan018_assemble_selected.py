#!/usr/bin/env python3
"""Assemble only root's scan018 journal choices; source text only."""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import re

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
DRAFT='out/checks/scan018_final_draft.tex'
MAP='out/checks/scan018_final_source_map.json'
JOURNAL='out/checks/scan018_main_decisions.md'
spec=importlib.util.spec_from_file_location('scan018_candidates',OUT/'scan018_prepare_tex_candidates.py')
candidate_module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(candidate_module)
span=candidate_module.span
sha=candidate_module.sha
command_end=candidate_module.command_end


def read(path):return (BASE/path).read_text(encoding='utf-8')
def jread(path):return json.loads(read(path))


tex={r:read(f'out/readers/018/{r}/reading.tex') for r in 'ABC'}
paths={r:f'out/readers/018/{r}/reading.tex' for r in 'ABC'}
candidates=jread('out/checks/scan018_tex_candidates.json')
groups={g['candidate_id']:g for g in candidates['group_candidates']}
journal=read(JOURNAL)
sections={}
heads=list(re.finditer(r'^## (\d+) —.*$',journal,re.M))
for i,h in enumerate(heads):
    end=heads[i+1].start() if i+1<len(heads) else len(journal)
    sections[int(h.group(1))]=span(JOURNAL,journal,h.start(),end,reader='root')

blocks=[]


def original(reader,a,b,**extra):return span(paths[reader],tex[reader],a,b,reader=reader,**extra)
def unique(reader,literal):
    a=tex[reader].index(literal)
    if tex[reader].find(literal,a+1)>=0:raise ValueError(('nonunique requested source',reader,literal))
    return original(reader,a,a+len(literal))


def add(block_id,reader,a,b,root_sections,decision_ids=(),edit=None,extra_sources=()):
    src=original(reader,a,b);emitted=src['literal_tex'];transforms=[]
    if edit:
        old,new,description=edit
        if emitted.count(old)!=1:raise ValueError(('edit must identify one exact source',block_id,old))
        k=emitted.index(old)
        emitted=emitted[:k]+new+emitted[k+len(old):]
        transforms=[{'description':description,'before_block_character_start':k,
            'before_block_character_end_exclusive':k+len(old),'old_literal_tex':old,
            'new_literal_tex':new,'old_sha256_utf8':sha(old),'new_sha256_utf8':sha(new),
            'original_source':original(reader,a+k,a+k+len(old))}]
    obj={'id':block_id,'source':src,'emitted_literal_tex':emitted,
         'emitted_literal_sha256_utf8':sha(emitted),'transformations':transforms,
         'additional_selected_sources':list(extra_sources),'decision_ids':list(decision_ids),
         'root_decision_sources':[sections[i] for i in root_sections],
         'main_approved':False,'literal_path_sources':[]}
    blocks.append(obj);return obj


def addgroup(cid,root_sections,decision_ids):
    g=groups[cid];s=g['source'];obj=add(cid,g['reader'],s['character_start'],s['character_end_exclusive'],root_sections,decision_ids)
    obj['selected_candidate_id']=cid
    obj['complete_group_copied_without_changes']=True
    obj['word_boundaries']={'included':g['included_word_state_boundaries'],'outside':g['external_word_boundaries']}
    obj['wrapper_state_dependencies']=copy.deepcopy(g['wrapper_state_dependencies'])
    obj['coordinate_declarations']=copy.deepcopy(g['literal_coordinate_declarations'])
    obj['literal_path_sources']=copy.deepcopy(g['literal_path_components'])
    return obj


def a(cid):return groups[cid]['source']['character_start']
def b(cid):return groups[cid]['source']['character_end_exclusive']


# Each complete selected graphical block is copied intact. Prose is partitioned
# at the actual reader word boundaries, with every root combination explicit.
add('opening_and_definition_lead','B',0,a('B.G01'),[1,2,3,4],['L018-01','L018-02','L018-03'])
addgroup('B.G01',[4],['L018-04','L018-05','L018-06'])
add('definition_continuation','B',b('B.G01'),a('B.G02'),[5,6],['L018-44','L018-07'])
addgroup('B.G02',[7],['L018-08','L018-09','L018-10','L018-11'])
add('proof_lead','B',b('B.G02'),a('B.G03'),[8],['L018-12'])
addgroup('C.G03',[9],['L018-13'])
add('between_C_G03_G04','C',b('C.G03'),a('C.G04'),[9])
addgroup('C.G04',[9],['L018-14','L018-15','L018-16','L018-17','L018-18'])
contient_source=unique('C','contient pas $\\deleted{\\Sigma}\\overline{E_i}$')
contient_source=original('C',contient_source['character_start'],contient_source['character_start']+len('contient '),purpose='Exact word outside selected C G04, retained once in combined prose.')
add('first_E_predecessor_and_continuation','B',b('B.G03'),a('B.G04'),[9,10],['L018-18','L018-19'],
    edit=('\npas','\ncontient pas','Root §09 selects C G04, whose baseline node is ne. The following source word contient is placed once before the exact B pas/deleted-Sigma span.'),
    extra_sources=[contient_source])
addgroup('B.G04',[10],['L018-20'])
add('through_second_E','B',b('B.G04'),a('B.G05'),[10,11,12],['L018-21','L018-22','L018-23','L018-24'])
addgroup('A.G05',[12,21],['L018-25','L018-26','L018-27'])
b_singular=tex['B'].index("l'\\unsure{élêment|élément}",b('B.G05'))
add('lower_quote_and_est','B',b('B.G05'),b_singular,[13,14],['L018-28','L018-29'])
c_singular_literal="l'\\unsure{é|e}l\\unsure{é|ê}ment"
c_singular=tex['C'].index(c_singular_literal,b('C.G05'))
add('singular_element_combination','C',c_singular,c_singular+len(c_singular_literal),[15,22],['L018-30','L018-31'],
    edit=('\\unsure{é|ê}','\\unsure{ê|é}','Root §15 retains C first-accent é/e and reverses only C second-accent alternatives to ê/é, using B’s supported second-accent primary.'),
    extra_sources=[unique('B',"l'\\unsure{élêment|élément}")])
add('singular_element_continuation','C',c_singular+len(c_singular_literal),a('C.G06'),[15],['L018-32'])
addgroup('C.G06',[16],['L018-33','L018-34'])
add('before_cas','C',b('C.G06'),a('C.G07'),[16,17])
addgroup('C.G07',[17],['L018-35','L018-36','L018-37'])
add('bottom_comma','C',b('C.G07'),b('C.G07')+1,[17])
add('bottom_word_and_conclusion','A',b('A.G07'),a('A.G08'),[18,19,22],['L018-38','L018-39','L018-40'],
    edit=('\\deleted{\\unsure{cela|OK}}','\\deleted{\\unsure{cela|OK|et}}','Root §18 retains A cela-first order and adds B’s supported et alternative while preserving the deleted state.'),
    extra_sources=[unique('B','\\deleted{\\unsure{OK|cela|et}}')])
addgroup('A.G08',[19],['L018-41','L018-42','L018-43'])
add('archive_comment','A',b('A.G08'),len(tex['A']),[20])

draft=''.join(x['emitted_literal_tex'] for x in blocks)
offset=0
byid={}
for obj in blocks:
    length=len(obj['emitted_literal_tex'])
    obj['draft']=span(DRAFT,draft,offset,offset+length)
    obj['source_to_draft_segments']=[]
    source=obj['source'];start=source['character_start']
    transforms=obj['transformations']
    if not transforms:
        obj['source_to_draft_segments'].append({'kind':'unchanged','source':source,'draft':obj['draft']})
    else:
        tr=transforms[0];p=tr['before_block_character_start'];q=tr['before_block_character_end_exclusive'];n=len(tr['new_literal_tex'])
        if p:
            obj['source_to_draft_segments'].append({'kind':'unchanged','source':original(source['reader'],start,start+p),'draft':span(DRAFT,draft,offset,offset+p)})
        tr['draft']=span(DRAFT,draft,offset+p,offset+p+n)
        obj['source_to_draft_segments'].append({'kind':'root_selected_replacement','source':tr['original_source'],'draft':tr['draft']})
        if q<len(source['literal_tex']):
            obj['source_to_draft_segments'].append({'kind':'unchanged','source':original(source['reader'],start+q,source['character_end_exclusive']),'draft':span(DRAFT,draft,offset+p+n,offset+length)})
    for component in obj['literal_path_sources']:
        for source_key,draft_key in [('source','draft'),('complete_support_source','complete_support_draft')]:
            s=component[source_key];x=offset+s['character_start']-start;y=offset+s['character_end_exclusive']-start
            component[draft_key]=span(DRAFT,draft,x,y)
        for qualifier in component['enclosing_qualifier_state_sources']:
            s=qualifier['source'];qualifier['draft']=span(DRAFT,draft,offset+s['character_start']-start,offset+s['character_end_exclusive']-start)
    for extra in obj['additional_selected_sources']:
        literal=extra['literal_tex']
        if obj['id']=='first_E_predecessor_and_continuation':
            k=obj['emitted_literal_tex'].index(literal);extra['draft']=span(DRAFT,draft,offset+k,offset+k+len(literal))
        else:
            extra['relationship']='Supported candidate source for root-directed combination; no separate copy of this complete alternate word is emitted.'
    byid[obj['id']]=obj;offset+=length


def attach(block_id,needle=None,occurrence=0,note=None):
    obj=byid[block_id];value=obj['emitted_literal_tex']
    if needle is None:k=0;end=len(value)
    else:
        k=-1
        for _ in range(occurrence+1):k=value.index(needle,k+1)
        end=k+len(needle)
    start=obj['draft']['character_start']
    return {'block_id':block_id,'note':note,'draft':span(DRAFT,draft,start+k,start+end)}


def attach_node(block_id,needle,note=None):
    obj=byid[block_id];value=obj['emitted_literal_tex'];target=value.index(needle)
    nodes=[]
    for m in re.finditer(r'\\node\b',value):
        end=command_end(value,m.start())
        if m.start()<=target and target+len(needle)<=end:nodes.append((m.start(),end))
    start,end=min(nodes,key=lambda x:x[1]-x[0]);base=obj['draft']['character_start']
    return {'block_id':block_id,'note':note,'draft':span(DRAFT,draft,base+start,base+end)}


def attach_path(block_id,component_id,support=False,note=None):
    component=next(p for p in byid[block_id]['literal_path_sources'] if p['component_id']==component_id)
    return {'block_id':block_id,'component_id':component_id,'note':note,
            'source':component['complete_support_source' if support else 'source'],
            'draft':component['complete_support_draft' if support else 'draft']}


def page_range(start,end,note=None):
    return {'block_ids':[o['id'] for o in blocks if o['draft']['character_start']<end and start<o['draft']['character_end_exclusive']],
            'note':note,'draft':span(DRAFT,draft,start,end)}


def make_decision_attachments():
    d={}
    def put(n,*values):d[f'L018-{n:02d}']=list(values)
    put(1,attach('opening_and_definition_lead','dernière'))
    put(2,attach('opening_and_definition_lead',r'\unsure{rècurrence|récurrence}'))
    put(3,attach('opening_and_definition_lead',"l'ens des classes",note='The exact endpoint context contains no abbreviation stop.'))
    put(4,attach('B.G01',r'\unsure{des|de}'))
    put(5,attach('B.G01','ces $n$'))
    put(6,attach('B.G01'),attach_path('B.G01','G01'))
    put(44,attach('definition_continuation',"``\\unsure{composante|composant}''"))
    put(7,attach('definition_continuation','considérons'))
    put(8,attach('B.G02',r'\unsure{\circ|0}'))
    put(9,attach('B.G02',r'\unsure{\deleted{j}|\deleted{i}|\deleted{,}|j}'))
    put(10,attach('B.G02'),attach_path('B.G02','G02-underline'),attach_path('B.G02','G02-left-rule'))
    put(11,attach_node('B.G02',r'de $U_{J,i}$, est contenue',note='Complete final lemma node has no terminal full stop.'))
    put(12,attach('proof_lead','Dire'))
    put(13,attach('C.G03'),*[attach_path('C.G03',p) for p in ['G03a','G03b','G03c']])
    put(14,attach('C.G04',r'U_{\unsure{\alpha|x}}'))
    put(15,attach('C.G04',r'\Pi_J^\circ',note='Later occurrence prints primary circle; local circle/zero doubt retained in record.'))
    put(16,attach('C.G04'),attach_path('C.G04','G04a'))
    put(17,attach_path('C.G04','G04b',support=True),attach_path('C.G04','G04b'))
    put(18,attach('C.G04',note='Complete selected guide/name/ne source scope; no second struck word is emitted.'),attach('first_E_predecessor_and_continuation','contient pas'))
    put(19,attach('first_E_predecessor_and_continuation',r'\deleted{\Sigma}'))
    put(20,attach('B.G04'),attach_path('B.G04','G04-upper-rule',support=True),attach_path('B.G04','G04-upper-rule'))
    put(21,attach('through_second_E','que il'))
    put(22,attach('through_second_E',r'tel que le $\Sigma_j^+'))
    put(23,attach('through_second_E',r'\deleted{\Sigma}'))
    put(24,attach('through_second_E',r'E_{\unsure{j|J}}'))
    put(25,attach_node('A.G05',r'\rlap{\unsure{choisi|choisie}}',note='Whole word node retains one visible rlap and the invisible deleted-state copy.'))
    put(26,attach_path('A.G05','G05.P1'))
    put(27,attach_path('A.G05','G05.P2',support=True),attach_path('A.G05','G05.P2'),attach_path('A.G05','G05.P3'))
    put(28,attach('lower_quote_and_est',"``\\unsure{composant|composante}''"))
    put(29,attach('lower_quote_and_est',r'\deleted{est} est'))
    put(30,attach('singular_element_combination',r'\unsure{é|e}'))
    put(31,attach('singular_element_combination',r'\unsure{ê|é}'))
    put(32,attach('singular_element_continuation',r'du $\pi_0$'))
    put(33,attach('C.G06',r'\unsure{é|e}léments'))
    put(34,attach('C.G06'),attach_path('C.G06','G06a'))
    put(35,attach_node('C.G07',r'\rlap{\unsure{deux}}',note='Visible-once word node and its exact invisible deletion-state annotation.'))
    put(36,attach_node('C.G07',r'\inserted{$\operatorname{card}I=2$}'),attach_path('C.G07','G07a'))
    put(37,attach_path('C.G07','G07b',support=True),attach_path('C.G07','G07b'))
    put(38,attach('bottom_word_and_conclusion',r'\deleted{\unsure{cela|OK|et}}'))
    put(39,attach('bottom_word_and_conclusion',r'\unsure{â|à}'))
    put(40,attach('bottom_word_and_conclusion',r'U_\alpha',note='Independently inspected final alpha/x doubt retained in record; first occurrence carries printed qualifier.'))
    put(41,attach_path('A.G08','G08.P1',support=True,note='Complete locally qualified OK group includes the invisible deletion annotation and one rising stroke.'))
    put(42,attach_path('A.G08','G08.P1'))
    put(43,attach_path('A.G08','G08.P2',support=True),attach_path('A.G08','G08.P2'))
    return d


decision_attachments=make_decision_attachments()
locus_map=jread('out/checks/scan018_locus_map.json')
inventory_map=jread('out/checks/scan018_inventory_map.json')
record=jread('out/checks/scan018_record_draft.json')
decision_coverage=[]
for locus in locus_map['loci']:
    ident=locus['id'];atts=decision_attachments[ident]
    decision_coverage.append({'decision_id':ident,'location':locus['location'],
        'original_reader_ids':locus['readers'],'reader_tex_sources':locus['reader_tex_sources'],
        'source_C_doubt_parts':locus['C_parts'],'final_source_attachments':atts,
        'main_approved':False})
page_audit=next((v for v in record['decisions'] if v['id']=='S018-PAGE'),None)
if page_audit is None:raise ValueError('Final public S018-PAGE record row is not ready; finish clerk selections before binding the map.')
decision_coverage.append({'decision_id':'S018-PAGE','location':page_audit['location'],
    'scope':'Page-level S source identity/scope audit; no extra physical ink locus or correction count.',
    'final_source_attachments':[page_range(0,len(draft),'Whole selected page for the nonphysical S scope audit.')],
    'original_source_provenance':{k:v for k,v in page_audit.items() if any(p in k for p in ['source','provenance','S_'])},
    'main_approved':False})

inventory_att={}
def iput(n,*values):inventory_att[f'018.I{n:02d}']=list(values)
iput(1,page_range(draft.index('cette dernière'),draft.index('\n\nCeci posé'),'Complete selected opening paragraph.'))
iput(2,page_range(draft.index('Ceci posé'),byid['B.G02']['draft']['character_start'],'Complete selected definition paragraph including G01.'))
iput(3,attach_node('B.G01',r'\inserted{(unique)}'))
iput(4,attach('B.G01'),attach_path('B.G01','G01'))
iput(5,attach('B.G02'))
iput(6,attach('B.G02'),attach_path('B.G02','G02-underline'),attach_path('B.G02','G02-left-rule'))
iput(7,*decision_attachments['L018-09'])
iput(8,page_range(draft.index("C'est presque"),byid['A.G08']['draft']['character_end_exclusive'],'Complete selected proof, including every selected local group and final period/spot.'))
iput(9,attach_node('C.G03',r'\rlap{la}\phantom{\deleted{la}}'),attach_path('C.G03','G03c'))
iput(10,attach_node('C.G03',r"\inserted{qu'une}"))
iput(11,*decision_attachments['L018-13'])
iput(12,attach_node('C.G04',r'\inserted{$U_{\unsure{\alpha|x}}$\quad de $\Pi_J^\circ$}'))
iput(13,attach('C.G04'),attach_path('C.G04','G04a'))
iput(14,*decision_attachments['L018-17'])
iput(15,*decision_attachments['L018-19'])
iput(16,*decision_attachments['L018-20'])
iput(17,attach('through_second_E',r'\deleted{\Sigma}E_{\unsure{j|J}}'))
iput(18,*decision_attachments['L018-25'])
iput(19,*decision_attachments['L018-26'])
iput(20,*decision_attachments['L018-27'])
iput(21,attach('lower_quote_and_est',r'\deleted{est}'))
iput(22,attach_node('C.G06',r'\inserted{(soit $\Sigma_i^-$)}'))
iput(23,attach('C.G06'),attach_path('C.G06','G06a'))
iput(24,*decision_attachments['L018-35'])
iput(25,attach_node('C.G07',r'\inserted{$\operatorname{card}I=2$}'))
iput(26,attach_path('C.G07','G07a'))
iput(27,*decision_attachments['L018-37'])
iput(28,*decision_attachments['L018-38'])
iput(29,*decision_attachments['L018-41'],*decision_attachments['L018-42'])
iput(30,*decision_attachments['L018-43'])
iput(31,attach('archive_comment','% archive sheet number: 17'))
inventory_coverage=[{'inventory_id':i['element'],'location':i['position'],'related_decision_ids':i['related_decision_ids'],
    'original_inventory_sources':i['source_rows'],'final_source_attachments':inventory_att[i['element']],
    'selected':True,'main_approved':False} for i in inventory_map['items']]
doubt_coverage=[]
for i,d in enumerate(record['doubts']):
    ident=d['decision_id']
    doubt_coverage.append({'decision_id':ident,'doubt_record_pointer':f'/doubts/{i}',
        'location':d['location'],'reading':d['reading'],'alternatives':d['alternatives'],
        'final_source_attachments':copy.deepcopy(decision_attachments[ident]),
        'original_reader_components':d.get('reader_components',{}),'main_approved':False})

original_C_coverage=[]
for row in record['C_source_rows']:
    item=copy.deepcopy(row)
    item['final_source_attachments_by_part']={}
    for part in row['source_parts']:
        ids=[v['id'] for v in locus_map['loci'] if part['part_id'] in v['C_parts']]
        item['final_source_attachments_by_part'][part['part_id']]=[
            {'decision_id':ident,'attachments':decision_attachments[ident]} for ident in ids]
    original_C_coverage.append(item)

source_file_paths=[paths[r] for r in 'ABC']+[f'out/readers/018/{r}/{name}' for r in 'ABC' for name in ['report.json','reading.md']]+[
    'packets/018/C.tex','packets/018/H.tex','packets/018/C_doubts.txt','packets/018/C_notes.txt','packets/018/S_rows.json',JOURNAL]
result={'scan':18,'status':'Root-selected exact source; pending root final approval and commit.',
    'main_adjudicated':False,'draft_file':DRAFT,'draft_sha256_utf8':sha(draft),
    'root_decision_journal':{'file':JOURNAL,'sha256_utf8':sha(journal),'sections':[int(h.group(1)) for h in heads]},
    'source_files':{p:{'file':p,'sha256_utf8':sha(read(p))} for p in source_file_paths},
    'locator_policy':'Exact zero-based Unicode code-point offsets in UTF-8 decoded source; end-exclusive, with literal excerpts, hashes and line/column positions.',
    'coordinate_policy':'Selected reader declarations and literal paths copied without coordinate changes. Manual approximations; no geometric, metric or rendered validation.',
    'visible_copy_policy':'Each selected whole group preserves original visible rlap text, phantom state annotations and local qualifiers. Adjacent words and physical path components occur once.',
    'blocks':blocks,'decision_coverage':decision_coverage,'inventory_coverage':inventory_coverage,'doubt_coverage':doubt_coverage,
    'original_C_doubt_row_coverage':original_C_coverage,
    'recurring_glyph_source_scope':[
        {'glyph':'Pi upper ring','first':decision_attachments['L018-08'],'later':decision_attachments['L018-15'],'printed_primary':r'\circ','qualification_policy':'First occurrence only; both local doubts remain attached.'},
        {'glyph':'U subscript','first':decision_attachments['L018-14'],'later':decision_attachments['L018-40'],'printed_primary':r'\alpha','qualification_policy':'First occurrence only; final local alpha/x doubt remains attached. Original C R08 primary-part identity remains unchanged.'}],
    'root_combination_edits':[{'block_id':o['id'],'transformations':o['transformations'],'additional_selected_sources':o['additional_selected_sources']} for o in blocks if o['transformations']],
    'structural_source_check':{'status':'pending one targeted assembler pass','compiler_or_renderer':False,'mathematical_or_geometry_validation':False},
    'attachment_counts':{'decisions':len(decision_coverage),'inventory':len(inventory_coverage),'retained_doubts':len(doubt_coverage)},
    'counts_authority':'All ink, count and confidence decisions are root supplied; assembler makes no independent choices.'}
(BASE/DRAFT).write_text(draft,encoding='utf-8')
(BASE/MAP).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'draft':DRAFT,'draft_sha256_utf8':sha(draft),'map':MAP,'map_sha256_utf8':sha(read(MAP)),
    'blocks':len(blocks),'complete_graphical_groups':sum('selected_candidate_id' in x for x in blocks),
    'attachments':result['attachment_counts'],'main_adjudicated':False},ensure_ascii=False))
