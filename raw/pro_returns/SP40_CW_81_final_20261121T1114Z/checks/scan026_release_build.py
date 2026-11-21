"""Source-only scan026 review proposals. Writes only scan026_release_* files."""
import collections
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
OUT = BASE / 'out/checks'
PREFIX = 'scan026_release_'

def sha(b):
    return hashlib.sha256(b).hexdigest()

def compact(v):
    return json.dumps(v, ensure_ascii=False, separators=(',', ':'))

def read(name):
    return json.loads((OUT / name).read_text())

def write(name, value):
    assert name.startswith(PREFIX)
    data = (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()
    (OUT / name).write_bytes(data)
    return {'path': 'out/checks/' + name, 'sha256': sha(data), 'bytes': len(data)}

def pointer(value, path):
    for part in path.split('/')[1:] if path else []:
        key = part.replace('~1', '/').replace('~0', '~')
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value

def ref(name, path=''):
    return {'path': 'out/checks/' + name, 'json_pointer': path}

registry = read('scan026_source_union_sources_v01.json')
source_text = {}
source_json = {}
for alias, info in registry.items():
    data = (BASE / info['path']).read_bytes()
    assert sha(data) == info['sha256'] and len(data) == info['bytes'], alias
    source_text[alias] = data.decode()
    if info['path'].endswith('.json'):
        source_json[alias] = json.loads(data)

union = read('scan026_source_union_v01.json')
scaffold = read('scan026_source_record_scaffold_v01.json')
original_pool = read('scan026_source_union_state_pool_v01.json')
roots = read('scan026_root_decisions.json')
supplement = read('scan026_root_locus_supplement_v01.json')
clarifications = read('scan026_root_source_clarifications_v01.json')
notes = read('scan026_root_notes_abbreviation_authority_v01.json')
journal = (OUT / 'scan026_root_journal.md').read_text()
crows = read('scan026_source_union_C_rows_v01.json')
hrows = read('scan026_source_union_H_marker_bindings_v01.json')
inventory_context = read('scan026_source_union_inventory_context_v01.json')

raw_values = {}
raw_refs = {}
for i, row in enumerate(original_pool):
    rr = row['raw_ref']
    target = pointer(source_json[rr['source']], rr['json_pointer'])
    if 'ordered_fields' in row:
        value = {}
        for field in row['ordered_fields']:
            if 'exact_value_ref' in field:
                vr = field['exact_value_ref']
                value[field['key']] = pointer(source_json[vr['source']], vr['json_pointer'])
            else:
                value[field['key']] = field['value']
    else:
        value = row['value']
    assert compact(value).encode() == compact(target).encode(), row['record_id']
    raw_values[row['record_id']] = value
    raw_refs[row['record_id']] = {
        'path': registry[rr['source']]['path'],
        'source_sha256': registry[rr['source']]['sha256'],
        'json_pointer': rr['json_pointer'],
        'ordered_value_sha256': sha(compact(value).encode()),
        'original_pool_pointer': '/' + str(i),
    }

def text_span(alias, start, end, scope):
    source = source_text[alias]
    literal = source[start:end]
    assert literal
    return {
        'path': registry[alias]['path'], 'source_sha256': registry[alias]['sha256'],
        'char_start': start, 'char_end': end,
        'utf8_byte_start': len(source[:start].encode()),
        'utf8_byte_end': len(source[:end].encode()),
        'line_start': source.count('\n', 0, start) + 1,
        'line_end': source.count('\n', 0, end - 1) + 1,
        'literal': literal, 'literal_sha256': sha(literal.encode()), 'scope': scope,
    }

def literal(alias, text, occurrence=0, scope='exact local witness source'):
    source = source_text[alias]
    starts = []
    at = 0
    while True:
        at = source.find(text, at)
        if at < 0:
            break
        starts.append(at)
        at += len(text)
    assert len(starts) > occurrence, (alias, text, occurrence, starts)
    return text_span(alias, starts[occurrence], starts[occurrence] + len(text), scope)

def lines(alias, first, last, scope):
    ll = source_text[alias].splitlines(keepends=True)
    return text_span(alias, len(''.join(ll[:first-1])), len(''.join(ll[:last])), scope)

bindings = {}
def bind(locus, C, H, scope='exact local witness source'):
    bindings[locus] = {
        'C': [literal('witness.C', C, scope=scope)] if isinstance(C, str) else C,
        'H': [literal('witness.H', H, scope=scope)] if isinstance(H, str) else H,
    }

context = 'exact witness context; local graphical component allocation remains for root source audit'
bind('L001', r'\uline{décomposition binaire}', r'\emph{disposition binaire}')
bind('L002', 'est un ens de deux parties', 'est un ens.\\ de deux\nparties')
bind('L003', r'\unsure{\mathcal E|\mathscr E|\varepsilon}', [literal('witness.H', r'\alpha\in\omega'), lines('witness.H', 7, 8, 'exact family-index note')])
bind('L004', "(les ``hémisphères'')", r'(\text{les “hémisphères”})')
bind('L005', "on s'intéresse au cas où les", 'on\n\\uncertain{suppose} \\ill{} \\ill{} que')
bind('L006', r'hémisphères $\Sigma_{\alpha}$', r'\struck{hémisphères} les')
bind('L007', r'\inserted{de}', r'\add{de}')
Ceq = r'\inserted{$\Sigma_{\alpha}^{\alpha}$ et $\Sigma_{\deleted{\unsure{\alpha}}}^{\alpha}\setminus E=\Sigma_{\deleted{\unsure{\alpha}}}^{\deleted{\unsure{\alpha}}\alpha,\unsure{0|\circ|o}}$}'
bind('L008', Ceq, [literal('witness.H', r'\uncertain{connexes}'), lines('witness.H', 21, 24, 'exact interlinear-formula note')])
bind('L009', r'et où $E\ne\varnothing$', r'et \uncertain{si} $E\neq\emptyset$')
bind('L010', r'$E\mathrel{\unsure{\ne|+}}\varnothing$', r'connexes et $E\neq\emptyset$')
bind('L011', r'$X$ est connexe, si \deleted{les $\Sigma_{\alpha}^{\alpha,0}$ connexes}, \inserted{$X$ connexe, \deleted{et}} on conclut', [lines('witness.H', 15, 16, 'exact clause/replacement context')])
bind('L012', r'\deleted{\unsure{aussitôt}}', r'\struck{aussitôt}')
Cclosure = r'que $\overline{\Sigma^{\alpha,0}}\cap E\ne\varnothing$'
Hclosure = r'que $\overline{\Sigma^{\alpha,0}}\cap E\neq\emptyset$'
bind('L013', Cclosure, Hclosure, context)
bind('L014', r'\cap E\ne\varnothing', r'\cap E\neq\emptyset', context)
Cmargin = [lines('witness.C', 3, 8, 'complete literal margin construction')]
Hmargin = [lines('witness.H', 29, 30, 'literal marginal construction'), lines('witness.H', 31, 32, 'literal margin note'), lines('witness.H', 33, 33, 'literal drawing description')]
bind('L015', Cmargin, Hmargin)
bind('L016', r'\deleted{\unsure{E|\Sigma|B}}', r'\marginal{diagramme \struck{\ill{}}')
bind('L017', r'E_{\unsure{\alpha|{}}}', [literal('witness.H', r'\Sigma^{-}\supset E\subset\Sigma^{+}', i, 'complete margin formula, occurrence ' + str(i + 1)) for i in range(3)])
bind('L018', r'\Sigma^{-}\supset E_{\unsure{\alpha|{}}}\subset\Sigma^{+}', Hmargin, context)
bind('L019', Cmargin, Hmargin, context)
Cparent = [lines('witness.C', 9, 9, 'complete explanatory parenthesis')]
Hparent = [lines('witness.H', 17, 20, 'first explanatory parenthesis context'), lines('witness.H', 26, 27, 'later explanatory clause and note')]
bind('L020', Cparent, Hparent, context)
bind('L021', Cparent, Hparent)
bind('L022', 'ne peut être', 'une\npartie à la fois', context)
bind('L023', 'être à la fois', 'à la fois ouverte et fermée', context)
bind('L024', 'à la fois', 'à la fois')
bind('L025', r'car $\Sigma^{\unsure{-,0|\alpha,0|-\alpha,0}}$, est un ouvert $\ne\varnothing$ et $\ne X$', [lines('witness.H', 26, 27, 'exact marked continuation and note')])
bind('L026', r'\Sigma^{\unsure{-,0|\alpha,0|-\alpha,0}}$, est un ouvert', [lines('witness.H', 26, 27, context)], context)
bind('L027', r'est un ouvert $\ne\varnothing$ et $\ne X$', [lines('witness.H', 26, 27, context)], context)
bind('L028', 'Considérons deux décompositions binaires', 'Considérons deux dispositions binaires')
bind('L029', r'$\{\Sigma_1^{+},\Sigma_1^{-}\},\unsure{(|[}\Sigma_2^{+},\Sigma_2^{-}\}$ \deleted{\unsure{distinctes}} \inserted{de $X$,}', [lines('witness.H', 35, 36, 'complete pair/deletion context')])
bind('L030', r'\unsure{(|[}\Sigma_2^{+},\Sigma_2^{-}\}', r'\{\Sigma_{2}^{+},\Sigma_{2}^{-}\}')
bind('L031', r'\deleted{\unsure{distinctes}}', r'\struck{distinctes}')
bind('L032', r'\inserted{de $X$,}', r'\struck{distinctes} de $X$,')
bind('L033', "qu'elles", "qu'elles")
Cadj = r'\uline{non \unsure{panachées|penchées|parallèles}}'
Hadj = r'\emph{non parallèles}'
bind('L034', Cadj, Hadj)
bind('L035', Cadj, Hadj, context)
bind('L036', r'si \inserted{elles sont \uline{distinctes}, et si}', '\\add{si elles sont \\emph{distinctes},\net} si')
bind('L037', 'on peut trouver', 'on peut trouver', context)
bind('L038', r'\Sigma_1^{+}\cap\Sigma_2^{+}=\varnothing', r'\Sigma_{1}^{+}\cap\Sigma_{2}^{+}=\emptyset', context)
bind('L039', r"\text{d'où }", r"\text{d'où }")
bind('L040', r'E_1\cap E_2=\varnothing', 'E_{1}\\cap\n  E_{2}=\\emptyset', context)
bind('L041', r'E_1\cap E_2=\varnothing', 'E_{1}\\cap\n  E_{2}=\\emptyset', context)
bind('L042', 'on a alors', 'on a donc')
bind('L043', 'on a alors', 'on a donc', context)
bind('L044', r'\mathrel{\unsure{\deleted{\cap}\subset|\subset}}', r'\Sigma_{1}^{+}\subset\Sigma_{2}^{-}')
bind('L045', r'\deleted{\unsure{\ne\varnothing}}', [lines('witness.H', 57, 58, 'exact N05 cancellation note')])
bind('L046', r'\text{i.e.}', [literal('witness.H', r'\text{i.e.}', 0)])
bind('L047', r'\text{\unsure{i.e.|ie}}', [literal('witness.H', r'\text{i.e.}', 1)])
bind('L048', r'\overset{\mathrm{def}}{=}', r'\overset{\text{déf}}{=}')
bind('L049', r'\Sigma_1^{-}\cap\Sigma_2^{-}\supset', r'\Sigma_{1}^{-}\cap\Sigma_{2}^{-}\supset', context)
bind('L050', r'\Sigma_1^{-}\cap\Sigma_2^{-}\ne\varnothing', r'\Sigma_{1}^{-}\cap\Sigma_{2}^{-}\neq\emptyset', context)
bind('L051', '% archive sheet number: 25', r'\page{25}', 'exact page/archive source; root agreement authority binds the three reader comments')
bind('L052', Cclosure, Hclosure, context)

root_by_locus = {}
for i, section in enumerate(roots['decisions']):
    body = section['body']
    assert journal.count(body) == 1
    start = journal.index(body)
    for lid, decision in section['locus_decisions'].items():
        assert lid not in root_by_locus
        root_by_locus[lid] = {
            'section': section['section'],
            'decision': decision,
            'decision_ref': ref('scan026_root_decisions.json', f'/decisions/{i}/locus_decisions/{lid}'),
            'body_ref': ref('scan026_root_decisions.json', f'/decisions/{i}/body'),
            'journal_span': {'path': 'out/checks/scan026_root_journal.md', 'char_start': start, 'char_end': start + len(body), 'utf8_byte_start': len(journal[:start].encode()), 'utf8_byte_end': len(journal[:start+len(body)].encode()), 'body_sha256': sha(body.encode())},
            'crop_path': section['crop_path'], 'crop_sha256': section['crop_sha256'],
        }
root_by_locus['L051'] = {'section': 'agreed-source supplement', 'decision': supplement['agreed_locus'], 'decision_ref': ref('scan026_root_locus_supplement_v01.json', '/agreed_locus'), 'crop_path': None}

ordered_union = list(union)
insert_at = next(i for i, row in enumerate(ordered_union) if row['locus_id'] == 'L014') + 1
ordered_union.insert(insert_at, {'locus_id': 'L052', 'location': supplement['new_locus']['reading'], 'reader_sources': {}, 'original_C_source_rows': [], 'H_source_marker_records': [], 'witness_source_spans': [], 'source_observations': []})
assert len(ordered_union) == len(root_by_locus) == 91

scalar_rows = []
witness_binding_rows = []
for i, row in enumerate(ordered_union):
    lid = row['locus_id']
    root = root_by_locus[lid]
    decision = root['decision']
    if lid.startswith('S'):
        wb = {'C': [], 'H': []}
        for span in row['witness_source_spans']:
            alias = span['source']
            value = text_span(alias, span['start_char'], span['end_char_exclusive'], 'exact original union occurrence binding')
            assert value['literal'] == span['literal'] and value['literal_sha256'] == span['sha256']
            wb[alias[-1]].append(value)
    else:
        wb = bindings[lid]
    witness_binding_rows.append({'locus_id': lid, 'witnesses': wb})
    reader_flags = {}
    for role, sources in row['reader_sources'].items():
        rr = []
        for rid in sources['difference_records']:
            raw = raw_values[rid]
            rr.append({'raw_record': rid, 'raw_ref': raw_refs[rid], 'fields': {k: raw[k] for k in ['id', 'confidence', 'kind', 'diff_C', 'diff_H', 'marked_in_H', 'C_doubt_status'] if k in raw}})
        reader_flags[role] = rr
    hs = [x for x in hrows if lid in x['loci']]
    scalar_rows.append({
        'row': i + 1, 'id': 'SOURCE026-' + lid, 'source_locus_id': lid, 'location': row['location'],
        'root_section': root['section'], 'root_decision_ref': root['decision_ref'],
        'final': decision['reading'], 'confidence': decision['confidence'],
        'C': [v['literal'] for v in wb['C']], 'H': [v['literal'] for v in wb['H']],
        'witness_binding_pointer': f'/rows/{i}/witnesses',
        'witness_scope': {'C': [v['scope'] for v in wb['C']], 'H': [v['scope'] for v in wb['H']]},
        'C_source_row_ids': row['original_C_source_rows'],
        'H_source_scope_ids': [h['source_id'] for h in hs],
        'root_H_markers_exact': decision.get('H_markers'),
        'root_C_doubt_status_exact': decision.get('C_doubt_status'),
        'diff_C': None, 'diff_H': None, 'marked_in_H': None, 'kind': None,
        'physical_count_parent': None, 'root_count_authorization': None,
        'flag_status': 'pending root scalar/source-scope assignment',
        'raw_reader_flag_pool_pointer': f'/rows/{i}/raw_reader_flags',
        'L045_clarification_ref': ref('scan026_root_source_clarifications_v01.json', '/clarifications/0') if lid == 'L045' else None,
    })
    row['_release_raw_reader_flags'] = reader_flags

source_names = ['scan026_source_union_v01.json','scan026_source_union_state_pool_v01.json','scan026_source_record_scaffold_v01.json','scan026_source_state_catalog_v01.json','scan026_source_union_sources_v01.json','scan026_root_decisions.json','scan026_root_journal.md','scan026_root_locus_supplement_v01.json','scan026_root_source_clarifications_v01.json','scan026_root_notes_abbreviation_authority_v01.json','scan026_source_union_C_rows_v01.json','scan026_source_union_H_marker_bindings_v01.json','scan026_source_union_inventory_context_v01.json']
source_manifest = [{'path': 'out/checks/' + name, 'sha256': sha((OUT/name).read_bytes()), 'bytes': (OUT/name).stat().st_size} for name in source_names]
scalar_manifest = write('scan026_release_scalar_review_v01.json', {'schema': 'scan026-root-scalar-review-v01', 'source_only': True, 'main_approved': False, 'rows': scalar_rows})
witness_manifest = write('scan026_release_witness_bindings_v01.json', {'schema': 'scan026-exact-witness-bindings-v01', 'rows': witness_binding_rows})
flag_manifest = write('scan026_release_raw_reader_flags_v01.json', {'schema': 'scan026-original-reader-flags-v01', 'scope': 'Exact raw reader fields; each remains bound to its original reader row and field scope.', 'rows': [{'locus_id': x['locus_id'], 'raw_reader_flags': x['_release_raw_reader_flags']} for x in ordered_union]})

chunks = []
current = []
size = 0
for row in scalar_rows:
    data = (compact(row) + '\n').encode()
    assert len(data) <= 11000, row['source_locus_id']
    if current and size + len(data) > 11000:
        chunks.append(current); current = []; size = 0
    current.append(data); size += len(data)
if current:
    chunks.append(current)
chunk_manifest = []
for i, chunk in enumerate(chunks, 1):
    name = PREFIX + f'scalar_review_v01_{i:02d}.jsonl'
    data = b''.join(chunk)
    (OUT / name).write_bytes(data)
    chunk_manifest.append({'path':'out/checks/'+name,'sha256':sha(data),'bytes':len(data),'loci':[json.loads(line)['source_locus_id'] for line in chunk]})
assert [json.loads(line) for chunk in chunks for line in chunk] == scalar_rows

scalar_index = write('scan026_release_scalar_index_v01.json', {
    'status': 'Source-only root review; every scalar count flag remains pending root.',
    'physical_loci': 91, 'sigma_loci': 39, 'other_loci': 52,
    'root_decisions_exact': 90, 'agreed_L051_supplement': 1,
    'source_files': source_manifest,
    'row_order': [x['locus_id'] for x in ordered_union],
    'original_union_old_to_new_index': [{'old_index':i,'new_index':next(j for j,x in enumerate(ordered_union) if x['locus_id']==v['locus_id']),'locus_id':v['locus_id']} for i,v in enumerate(union)],
    'added_row': {'new_index':insert_at,'locus_id':'L052'},
    'scalar_file': scalar_manifest, 'witness_bindings': witness_manifest, 'raw_reader_flags': flag_manifest,
    'chunks': chunk_manifest,
    'full_original_pool_key_order_verified_records': len(raw_values),
    'C_parent_rows': 15, 'R02_actual_parts': 4, 'R15_actual_parts': 1, 'R15_occurrences': 8,
    'pending': ['Root C/H flags, local H marker flag, kind and physical count scope', 'Complete own-reader state projection and inventory/source attachments', 'Final root-selected state expansion bindings from source026'],
    'no_new_ink_decisions': True, 'source_files_unchanged': True,
})
print(json.dumps({'scalar_index':scalar_index,'chunks':len(chunks),'rows':len(scalar_rows),'pool_verified':len(raw_values)},ensure_ascii=False))

# Full source audit remains separate from the pending public scalar assignments.
catalog = read('scan026_source_state_catalog_v01.json')
addendum = read('scan026_source_union_scope_addendum_v02.json')
raw_id_to_index = {v['record_id']:i for i,v in enumerate(original_pool)}
raw_output = []
for rid, value in raw_values.items():
    raw_output.append({'record_id':rid,'source':raw_refs[rid],'value':value})
raw_manifest = write('scan026_release_exact_raw_values_v01.json', {'schema':'scan026-exact-raw-values-v01','records':raw_output})

def escape(key):
    return str(key).replace('~','~0').replace('/','~1')

def walk_nodes(value, path=''):
    yield path, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk_nodes(child, path+'/'+escape(key))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from walk_nodes(child, path+'/'+str(i))

raw_path_mappings = []
candidate_fields = {}
for i, record in enumerate(raw_output):
    rid = record['record_id']
    values = list(walk_nodes(record['value']))
    source = record['source']
    raw_path_mappings.append({
        'record_id':rid,'source_path':source['path'],'source_pointer_prefix':source['json_pointer'],
        'target_path':raw_manifest['path'],'target_pointer_prefix':f'/records/{i}/value',
        'suffixes':[p for p,v in values],
        'identity_at_every_listed_suffix_verified':True,
        'root_ordered_value_sha256':source['ordered_value_sha256'],
    })
    candidates = []
    for path, value in values:
        if not isinstance(value,dict):
            continue
        for key, child in value.items():
            low = key.lower()
            if any(term in low for term in ['candidate','alternative']) or low in ['states','state','reading','complete_reading','proposal','primary','primary_reading','canonical_syntax','hand','role','attachment','surface_origin','local_hand_scopes','component_hands','insertion_state','cancellation_state']:
                child_path = path+'/'+escape(key)
                candidates.append({'field_pointer':child_path,'source_json_pointer':source['json_pointer']+child_path,'ordered_value_sha256':sha(compact(child).encode())})
    candidate_fields[rid] = candidates
path_manifest = write('scan026_release_raw_path_mappings_v01.json', {'rule':'For each listed suffix, concatenate it to both pointer prefixes; the resulting nodes have identical JSON types, scalar values, list order and object key order.','records':raw_path_mappings})
candidate_manifest = write('scan026_release_candidate_field_paths_v01.json', {'scope':'Directory of exact candidate, reading, hand, role and attachment fields. Every complete raw object remains available independently of this directory.','records':[{'record_id':rid,'fields':fields} for rid,fields in candidate_fields.items()]})

source_span_pool = []
source_span_lookup = {}
def add_own_span(alias, start, end, origin):
    value = text_span(alias,start,end,'complete literal own-reader source span')
    key = (alias,start,end)
    if key not in source_span_lookup:
        source_span_lookup[key] = len(source_span_pool)
        source_span_pool.append({'span_id':f'T{len(source_span_pool)+1:04d}','source':alias,'span':value,'origin_refs':[]})
    index = source_span_lookup[key]
    if origin not in source_span_pool[index]['origin_refs']:
        source_span_pool[index]['origin_refs'].append(origin)
    return source_span_pool[index]['span_id']

partition_bindings = {}
for role in 'ABC':
    cursor = 0
    reconstructed = []
    partition_bindings[role] = []
    for i,item in enumerate(catalog['complete_source_partitions'][role]):
        ex = item['exact_source']
        assert ex['char_start'] == cursor
        sid = add_own_span(role+'.tex',ex['char_start'],ex['char_end'],ref('scan026_source_state_catalog_v01.json',f'/complete_source_partitions/{role}/{i}'))
        literal_value = source_text[role+'.tex'][ex['char_start']:ex['char_end']]
        assert sha(literal_value.encode()) == ex['body_sha256']
        reconstructed.append(literal_value)
        cursor = ex['char_end']
        partition_bindings[role].append({'span_id':sid,'original_partition_ref':ref('scan026_source_state_catalog_v01.json',f'/complete_source_partitions/{role}/{i}'),'containing_source_groups':item['containing_source_groups']})
    assert ''.join(reconstructed).encode() == source_text[role+'.tex'].encode()

slot_indices = {x['source_locus_id']:i for i,x in enumerate(scaffold['pending_decision_slots'])}
union_indices = {x['locus_id']:i for i,x in enumerate(union)}
audit_rows = []
inventory_bindings = []
for row_number,row in enumerate(ordered_union):
    lid = row['locus_id']
    own = {}
    for role in 'ABC':
        sources = row['reader_sources'].get(role)
        if sources is None:
            own[role] = {'original_union_binding':None,'source_categories':{},'exact_local_source_span_ids':[],'complete_own_partition_ref':f'/reader_source_partitions/{role}','raw_state_ref_scope':'Root-added L052 has no original reader-union row.'}
            continue
        categories = {key:sources[key] for key in ['source_group_records','difference_records','doubt_records','inventory_records','other_state_records','declared_crop_records']}
        span_ids = []
        for j,ex in enumerate(sources['local_source_spans']):
            sid = add_own_span(ex['source'],ex['start_char'],ex['end_char_exclusive'],ref('scan026_source_union_v01.json',f'/{union_indices[lid]}/reader_sources/{role}/local_source_spans/{j}'))
            literal_value = source_text[ex['source']][ex['start_char']:ex['end_char_exclusive']]
            assert sha(literal_value.encode()) == ex['sha256']
            if 'literal' in ex:
                assert literal_value == ex['literal']
            span_ids.append(sid)
        own[role] = {
            'original_union_binding':ref('scan026_source_union_v01.json',f'/{union_indices[lid]}/reader_sources/{role}'),
            'source_categories':categories,'exact_local_source_span_ids':span_ids,
            'complete_own_partition_ref':f'/reader_source_partitions/{role}',
            'raw_state_ref_scope':'Every referenced R record expands to the complete original object, with its exact key order, own primary/alternative states and candidate-specific component fields. Original witness/count fields remain at their original raw paths.',
        }
        for rid in sources['inventory_records']:
            indices = [i for i,item in enumerate(inventory_context) if item['reader']==role and item['record']==rid]
            inventory_bindings.append({
                'reader':role,'raw_record':rid,'raw_inventory_ref':raw_refs[rid],
                'exact_original_union_locus':lid,
                'original_union_inventory_pointer':f'/{union_indices[lid]}/reader_sources/{role}/inventory_records/{sources["inventory_records"].index(rid)}',
                'broad_scope_context_refs':[ref('scan026_source_union_inventory_context_v01.json','/'+str(i)) for i in indices],
                'raw_hand_field_paths':[x['field_pointer'] for x in candidate_fields[rid] if 'hand' in x['field_pointer'].rsplit('/',1)[-1].lower()],
                'root_locus_decision_ref':root_by_locus[lid]['decision_ref'],
                'selected_public_inventory_assignment':None,
                'scope_status':'Original reader element scope preserved; this union attachment does not allocate every component to a single selected public inventory element.',
            })
    original_slot = scaffold['pending_decision_slots'][slot_indices[lid]] if lid in slot_indices else None
    raw = {
        'row':row_number+1,'id':'SOURCE026-'+lid,'source_locus_id':lid,
        'location':row['location'],
        'original_union_ref':ref('scan026_source_union_v01.json','/'+str(union_indices[lid])) if lid in union_indices else None,
        'original_scaffold_slot_ref':ref('scan026_source_record_scaffold_v01.json',f'/pending_decision_slots/{slot_indices[lid]}') if lid in slot_indices else None,
        'root_authority':root_by_locus[lid],
        'root_source_clarification_refs':[ref('scan026_root_source_clarifications_v01.json','/clarifications/0')] if lid=='L045' else [],
        'scalar_review_ref':ref('scan026_release_scalar_review_v01.json',f'/rows/{row_number}'),
        'exact_witnesses':witness_binding_rows[row_number]['witnesses'],
        'readers':own,
        'C_source_row_ids':row['original_C_source_rows'],
        'C_source_part_ids':original_slot['C_source_part_ids'] if original_slot else [],
        'C_recurrence_binding':original_slot.get('C_recurrence_binding') if original_slot else None,
        'H_source_scope_ids':[x['source_id'] for x in hrows if lid in x['loci']],
        'root_selected_source_contract':None,
        'main_approved':False,
    }
    audit_rows.append(raw)

assert len(inventory_bindings) == 262
assert len({x['raw_record'] for x in inventory_bindings}) == 262
assert collections.Counter(x['reader'] for x in inventory_bindings) == {'A':79,'B':95,'C':88}
all_inventory_pool_ids = {rid for rid,rr in raw_refs.items() if rr['path'].endswith('/report.json') and rr['json_pointer'].startswith('/inventory/') and rr['json_pointer'].count('/')==2}
assert all_inventory_pool_ids == {x['raw_record'] for x in inventory_bindings}

# Preserve the complete original C row/part objects; add finite root mappings.
c_outcomes = []
for i,original in enumerate(scaffold['C_source_rows']):
    cid = original['source_id']
    history = []
    for j,section in enumerate(roots['decisions']):
        if cid in section.get('original_C_rows',{}):
            history.append({'section':section['section'],'value':section['original_C_rows'][cid],'ref':ref('scan026_root_decisions.json',f'/decisions/{j}/original_C_rows/{cid}')})
    assert history
    final = history[-1]
    val = final['value']
    if isinstance(val,str):
        status = val; status_ref = final['ref']; extraction = None
    elif 'status' in val:
        status = val['status']; status_ref = dict(final['ref']); status_ref['json_pointer'] += '/status'; extraction = None
    else:
        assert cid == 'C026-R15'
        text_value = val['parent_status']
        assert text_value.startswith('retained; ')
        status = text_value[:8]
        status_ref = dict(final['ref']); status_ref['json_pointer'] += '/parent_status'
        extraction = {'source_exact_value':text_value,'char_start':0,'char_end':8,'retained_suffix':text_value[8:]}
        assert status + extraction['retained_suffix'] == text_value
    assert status in ['retained','resolved']
    root_mapping = {'status':status,'exact_source_ref':status_ref,'finite_character_projection':extraction}
    parts = []
    for k,part in enumerate(original['source_parts']):
        selected_ref = status_ref
        selected_value = status
        if cid == 'C026-R02':
            selected_ref = dict(final['ref']); selected_ref['json_pointer'] += '/parts/'+str(k+1)
            selected_value = final['value']['parts'][str(k+1)]
        if cid == 'C026-R15':
            selected_value = final['value']['parent_status']
        parts.append({'part_id':part['part_id'],'exact_original_part_ref':ref('scan026_source_record_scaffold_v01.json',f'/C_source_rows/{i}/source_parts/{k}'),'selected_outcome_exact':selected_value,'root_ref':selected_ref})
    recurrences = []
    if cid == 'C026-R15':
        for rb in original['source_bindings']['eight_local_recurrences']:
            target = rb['locus']
            matches = [h for h in history if isinstance(h['value'],dict) and target in h['value']]
            assert len(matches)==1
            h = matches[0]
            recurrence_ref = dict(h['ref']); recurrence_ref['json_pointer'] += '/'+target
            recurrences.append({'original_part_id':original['source_parts'][0]['part_id'],'original_recurrence_binding':rb,'root_value_exact':h['value'][target],'root_ref':recurrence_ref})
    c_outcomes.append({'source_id':cid,'original_row_ref':ref('scan026_source_record_scaffold_v01.json',f'/C_source_rows/{i}'),'original_canonical_pool_record':crows[i]['canonical_record'],'source_binding':crows[i],'root_outcome_history':history,'final_parent_status_projection':root_mapping,'source_parts':parts,'recurrence_outcomes':recurrences})
assert collections.Counter(x['final_parent_status_projection']['status'] for x in c_outcomes)=={'retained':13,'resolved':2}
assert len(c_outcomes[1]['source_parts'])==4 and len(c_outcomes[14]['source_parts'])==1 and len(c_outcomes[14]['recurrence_outcomes'])==8

abbr_bindings = []
for i,item in enumerate(notes['abbreviations']):
    own_spans = {}
    if i == 0:
        for role in 'ABC':
            span = literal(role+'.tex','ens.')
            own_spans[role] = [span]
        witness = {'C':[literal('witness.C','ens.')],'H':[literal('witness.H','ens.')]}
    else:
        lid = item['root_loci'][0]
        witness = bindings[lid]
        u = next(x for x in union if x['locus_id']==lid)
        for role in 'ABC':
            own_spans[role] = [text_span(e['source'],e['start_char'],e['end_char_exclusive'],'exact own-reader abbreviation context') for e in u['reader_sources'][role]['local_source_spans']]
    abbr_bindings.append({'root_item_exact':item,'root_ref':ref('scan026_root_notes_abbreviation_authority_v01.json',f'/abbreviations/{i}'),'witness_sources':witness,'own_reader_sources':own_spans})

span_manifest = write('scan026_release_exact_own_source_spans_v01.json', {'schema':'scan026-complete-own-source-spans-v01','spans':source_span_pool,'reader_source_partitions':partition_bindings})
inventory_manifest = write('scan026_release_inventory_bindings_v01.json', {'scope':'All original reader inventory elements remain source-scoped; final public inventory grouping remains for root.','reader_inventory_bindings':inventory_bindings,'root_added_locus':{'locus_id':'L052','exact_root_decision_ref':root_by_locus['L052']['decision_ref'],'exact_supplement_ref':ref('scan026_root_locus_supplement_v01.json','/new_locus'),'selected_public_inventory_assignment':None},'agreed_archive_locus':'L051'})
c_manifest = write('scan026_release_C_row_outcomes_v01.json', {'source_only':True,'parent_counts':{'retained':13,'resolved':2},'rows':c_outcomes})
notes_manifest = write('scan026_release_notes_abbreviations_v01.json', {'notes':notes['notes'],'notes_exact_ref':ref('scan026_root_notes_abbreviation_authority_v01.json','/notes'),'check_events':notes['check_events'],'check_events_exact_ref':ref('scan026_root_notes_abbreviation_authority_v01.json','/check_events'),'abbreviations':abbr_bindings})
audit_manifest = write('scan026_release_audit_v01.json', {
    'schema':'scan026-complete-source-audit-proposal-v01','scan':26,'source_only':True,'main_adjudicated':False,'main_approved':False,
    'rows':audit_rows,'raw_values':raw_manifest,'raw_path_mappings':path_manifest,'candidate_field_directory':candidate_manifest,
    'complete_own_sources':span_manifest,'inventory_bindings':inventory_manifest,'original_C_outcomes':c_manifest,'notes_and_abbreviations':notes_manifest,
    'exact_scope_addendum_ref':ref('scan026_source_union_scope_addendum_v02.json'),
    'pending_root_fields':['diff_C','diff_H','marked_in_H','kind','physical_count_parent','root_count_authorization','selected_public_inventory_assignment','root_selected_source_contract'],
})
print(json.dumps({'audit':audit_manifest,'raw_values':raw_manifest,'inventory':inventory_manifest,'C_outcomes':c_manifest,'notes':notes_manifest},ensure_ascii=False))
