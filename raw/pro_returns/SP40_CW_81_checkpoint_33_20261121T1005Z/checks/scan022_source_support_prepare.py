"""Source-only scan022 catalog; no image access, geometry or ink decisions."""
from pathlib import Path
import hashlib
import json
import re

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'

EXPECTED = {
    'C': {
        'reading.tex': '87afac463f08e2c689a501d71572b33de43996a9c285fdea20b4ee0b446a26d9',
        'report.json': '6f571c4e494d87048135df4ab6de96a72a5296dbcf3e813db1e68135a530e3d3',
        'reading.md': '5f50e4f451ade2583e6ed486974d633b2f6a262f5ea84fea9759cf7fa95df9e3',
        'return_manifest.json': '4045f9077f9e1b0232a35d67d2cade17059e838bb4b965d52ed3d3cfd578dbb8',
    },
    'A': {
        'reading.tex': 'a3c0703526396b6f051d7848d124239ae8c982a16216087d8d0c9ce3c38ba21a',
        'report.json': 'f48a1b4ba7ad9f5282b7cbd88060ce5e2f8a88571545a9ce17fe926221e6b7f4',
        'reading.md': '179d5d1cdcddfdf242b7de1a54965570293563b80780a877974a0fc03697035a',
        'final_immutable.json': '83a21af3704afce201622138b3d42eae953bf86d285990fed2c4663ced297424',
    },
    'B': {
        'reading.tex': 'b7fe0dd99b386b2d82088258c562b6fec6e7bc32d98e609cda893fd0f95c97de',
        'report.json': '3405958c3ff67dfa90de79e3371c10aba2e5fe4f07de03d5b7fbaee744c57b30',
        'reading.md': 'ccbf12fa6fff12833458ac1a1ea12688af5a8d1b2b9fd5bf567b27a30947e8e4',
        'manifest.json': '32ae2aa61c47fe38ad4c59c33ca9fd1643b22a836519b123ac4145739b7f41f5',
    },
}

SUPPORT = {
    'C': ['source_groups.json', 'group_ownership.json', 'path_components.json',
          'node_anchors.json', 'sigma_groups.json', 'C_doubt_source_map.json',
          'H_local_marker_audit.json', 'source_audit.json', 'FINAL_STATUS.json',
          'processing_state.json', 'working_audit.md'],
    'A': ['source_audit.json', 'graphical_audit.json', 'C_doubt_map.json',
          'H_marker_audit.json', 'S_audit.json', 'count_proposal.json',
          'structural_validation.json', 'progress.json', 'checkpoint_findings.json'],
    'B': ['source_groups.json', 'text_ownership.json', 'C_doubt_audit.json',
          'H_marker_audit.json', 'source_validation.json', 'final_state.json',
          'processing_state.json', 'reading.draft.tex', 'report.draft.json'],
}

_texts = {}
def read(path):
    if path not in _texts:
        _texts[path] = (BASE / path).read_bytes().decode('utf-8')
    return _texts[path]

def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def file_ref(path):
    s = read(path)
    return {'path': path, 'sha256': digest(s), 'encoding': 'UTF-8',
            'bytes': len(s.encode('utf-8')), 'characters': len(s),
            'lines': len(s.splitlines())}

def json_ref(path, pointer=''):
    return {'path': path, 'sha256': file_ref(path)['sha256'], 'json_pointer': pointer}

def span(path, start, end, literal=False):
    s = read(path)
    assert 0 <= start <= end <= len(s)
    v = {'path': path, 'sha256': digest(s), 'char_start': start, 'char_end': end,
         'utf8_byte_start': len(s[:start].encode('utf-8')),
         'utf8_byte_end': len(s[:end].encode('utf-8')),
         'line_start': s.count('\n', 0, start) + 1,
         'line_end': s.count('\n', 0, max(start, end-1)) + 1,
         'body_sha256': digest(s[start:end])}
    if literal:
        v['literal'] = s[start:end]
    return v

def line_span(path, first, last, literal=False):
    s = read(path)
    lines = s.splitlines(keepends=True)
    start = sum(map(len, lines[:first-1]))
    end = sum(map(len, lines[:last]))
    while end > start and s[end-1] in '\r\n':
        end -= 1
    return span(path, start, end, literal)

def literal_spans(path, text):
    s = read(path)
    return [span(path, m.start(), m.end(), True) for m in re.finditer(re.escape(text), s)]

def write(name, value):
    p = OUT / name
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
    return {'path': str(p.relative_to(BASE)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}

def json_object(path):
    return json.loads(read(path))

def witness_catalog():
    c = 'packets/022/C.tex'
    h = 'packets/022/H.tex'
    catalog_path = 'out/checks/scan022_C_doubt_catalog.json'
    root_catalog = json_object(catalog_path)
    source_doubts = 'packets/022/C_doubts.txt'
    rows = []
    for i, row in enumerate(root_catalog['rows']):
        assert read(source_doubts)[row['char_start']:row['char_end']] == row['literal']
        cells = [x.strip() for x in row['literal'].strip('|').split('|')]
        rows.append({
            'source_id': row['source_id'],
            'canonical_catalog_ref': json_ref(catalog_path, f'/rows/{i}'),
            'exact_table_row': span(source_doubts, row['char_start'], row['char_end'], True),
            'table_fields': dict(zip(['scan','location','reading','other_readings','confidence',
                                     'evidence_on_this_sheet','contextual_preference'], cells)),
            'source_parts': row['source_parts'],
            'scope': 'One actual source row and its one canonical -1 part. Reader component subdivisions stay in reader provenance.',
        })
    blocks = [
        ('W01','opening, parenthetical line and lower insertion',[(2,2)],[(2,8)]),
        ('W02','two braced conditions, trivial and arrow',[(3,11)],[(9,20)]),
        ('W03','De façon précise introduction',[(13,13)],[(22,22)]),
        ('W04','main equality and two lower annotations',[(14,20)],[(23,30)]),
        ('W05','cancelled Comme and inverse-inclusion introduction',[(22,22)],[(32,34)]),
        ('W06','cancelled inverse-inclusion display',[(23,25)],[(35,36)]),
        ('W07','cancelled Soit and neighbourhood continuation through rencontre',[(26,26)],[(37,39)]),
        ('W08','cancelled Or, on, peut considérer, old noun and inserted égalité',[(28,28)],[(40,41),(44,46)]),
        ('W09','old variable and cancelled equality',[(29,31)],[(42,42),(44,46)]),
        ('W10','cancelled final relative clause',[(32,32)],[(43,43)]),
        ('W11','live Or sentence with two emphasis spans',[(34,34)],[(48,48)]),
        ('W12','live Y and Z display with complete union limit',[(35,37)],[(49,52)]),
        ('W13','final instruction, display and endpoint',[(38,42)],[(53,58)]),
        ('W14','administrative scan and archive source labels',[(1,1),(43,43)],[(1,1)]),
    ]
    marker_rows=[]
    for i,m in enumerate(re.finditer(re.escape(r'\ill{}'),read(h)),1):
        label = 'after rencontre' if i == 1 else 'after Or'
        marker_rows.append({'id':f'H022-ILL{i:02d}','location':label,
                            'marker':span(h,m.start(),m.end(),True),
                            'complete_line':line_span(h,read(h).count('\n',0,m.start())+1,
                                                      read(h).count('\n',0,m.start())+1,True),
                            'local_scope':'The literal ill marker at this position only; nearby wording and descriptive apparatus retain their own scope.'})
    annotations=[]
    for start,end,label in [(1,8,'Notation table'),(10,19,'Doubtful readings')]:
        annotations.append({'section':label,'source':line_span(source_doubts,start,end,True),
                            'count_scope':'Actual doubtful-reading rows only' if start==10 else 'Notation table; excluded from actual doubtful-reading row count'})
    return {
        'scan':22,'scope':'Exact supplied witness text and canonical source identities; no root ink decisions or selected counts.',
        'main_adjudicated':False,'main_approved':False,
        'sources':{name:file_ref('packets/022/'+name) for name in
                   ['C.tex','H.tex','C_doubts.txt','C_notes.txt','C_inventory.json','S_rows.json','metadata.json','notation.md']},
        'C_notes_exact':read('packets/022/C_notes.txt'),
        'complete_witness_lines':{role:[line_span(path,i,i,True) for i in range(1,len(read(path).splitlines())+1)] for role,path in [('C',c),('H',h)]},
        'source_blocks':[{'id':sid,'scope':label,'C':[line_span(c,*r) for r in cs],
                          'H':[line_span(h,*r) for r in hs]} for sid,label,cs,hs in blocks],
        'C_actual_doubt_rows':rows,
        'C_actual_source_rows_copied':root_catalog['actual_source_rows'],
        'C_actual_source_parts_copied':root_catalog['actual_source_parts'],
        'C_doubt_and_notation_scopes':annotations,
        'C_inventory_rows':[{'original_identity':x['element'],'source_ref':json_ref('packets/022/C_inventory.json',f'/{i}'),
                             'original_row':x} for i,x in enumerate(json_object('packets/022/C_inventory.json'))],
        'H_actual_local_markers':marker_rows,
        'H_descriptive_apparatus':[{'source':line_span(h,a,b,True),'scope':scope} for a,b,scope in
                                  [(6,8,'guide and lower formula description'),(19,20,'trivial position and old relation'),
                                   (27,30,'lower left and lower right expression states'),
                                   (44,46,'connected frame/diagonals, old variable and replaced noun')]],
        'abbreviation_source_forms':[
            {'form':'card','C':literal_spans(c,r'\operatorname{card}'),'H':literal_spans(h,r'\operatorname{card}'),
             'scope':'Literal operator letters; no abbreviation point in these commands. Expansion remains for later selected record.'},
            {'form':'i.e.','C':literal_spans(c,'i.e.'),'H':literal_spans(h,'i.e.'),
             'scope':'Both written points preserved; the immediately following H backslash-space is source syntax.'}],
        'S_rows':{'source_ref':json_ref('packets/022/S_rows.json'),'raw':json_object('packets/022/S_rows.json'),
                  'root_selected_confirmations':[]},
        'notation_snapshot_scope':'Complete supplied notation.md retained by fingerprint. Earlier-page entries remain notation context, without scan022 ink adjudication.',
    }

def command_end(s,start):
    depth=0
    i=start
    while i<len(s):
        ch=s[i]
        if ch=='%' and (i==0 or s[i-1]!='\\'):
            j=s.find('\n',i)
            i=len(s) if j<0 else j+1
            continue
        if ch=='\\':
            if i+1<len(s) and s[i+1] in '{}%':
                i+=2
                continue
        if ch=='{': depth+=1
        elif ch=='}': depth-=1
        elif ch==';' and depth==0: return i+1
        i+=1
    raise ValueError('Unterminated node command at character '+str(start))

def text_choice_index(role):
    path=f'out/readers/022/{role}/reading.tex'
    s=read(path)
    nodes=[]
    for n,m in enumerate(re.finditer(r'\\node\b',s),1):
        end=command_end(s,m.start())
        prior=s[:m.start()].splitlines()[-2:]
        label=None
        for line in prior:
            q=re.search(r'% LABEL ([^:]+):',line)
            if q: label=q.group(1)
        nodes.append({'source_node_id':label or f'{role}022-NODE{n:03d}',
                      'identity_scope':'Original label identity' if label else 'Source-clerk offset index; no new manuscript identity',
                      'source':span(path,m.start(),end),
                      'source_line_exact':line_span(path,s.count('\n',0,m.start())+1,s.count('\n',0,m.start())+1,True),
                      'nested_group_ids':re.findall(r'% BEGIN ([A-Za-z0-9_-]+)',s[m.start():end])})
    prose=[]
    for i,line in enumerate(s.splitlines(),1):
        if line.startswith(('et on doit prouver','ce qui est immédiat',r'\overline{(X',r'\deleted{',
                            'De façon précise',r'}} étant',r'$ ($')):
            prose.append(line_span(path,i,i,True))
    return {'complete_source':file_ref(path),
            'full_line_index':[line_span(path,i,i) for i in range(1,len(s.splitlines())+1)],
            'node_commands':nodes,'direct_prose_and_final_formula':prose,
            'coverage_scope':'All source lines and every complete node command, with original labelled identities retained. Includes report-silent source choices. Graphical components are referenced through the complete candidate bank.'}

def report_catalog(role):
    path=f'out/readers/022/{role}/report.json'
    report=json_object(path)
    rows=[]
    witness_issues=[]
    long_keys={'C_exact_source','H_exact_source','C_source_exact','H_source_exact'}
    for i,d in enumerate(report['differences']):
        wrefs={}
        for wit in ['C','H']:
            actual_key=f'{wit}_exact_source' if f'{wit}_exact_source' in d else f'{wit}_source_exact'
            line_key=f'{wit}_exact_source_lines' if f'{wit}_exact_source_lines' in d else f'{wit}_source_lines'
            if actual_key in d and line_key in d:
                sp=line_span(f'packets/022/{wit}.tex',*d[line_key])
                supplied=d[actual_key]
                actual=read(sp['path'])[sp['char_start']:sp['char_end']]
                matches=supplied==actual
                wrefs[wit]={'literal_report_field':json_ref(path,f'/differences/{i}/{actual_key}'),
                            'actual_packet_span':sp,'exact_agreement':matches,
                            'original_excerpt_field_name':actual_key,'original_line_field_name':line_key}
                if not matches:
                    witness_issues.append({'id':d['id'],'witness':wit,'issue':'Reported excerpt and attached actual line span differ; both originals preserved.',
                                           'report_ref':json_ref(path,f'/differences/{i}/{actual_key}'),'actual_packet_span':sp})
            elif f'{wit}_anchor_offsets' in d and isinstance(d[f'{wit}_anchor_offsets'],list):
                actual_key=f'{wit}_anchor'
                sp=span(f'packets/022/{wit}.tex',*d[f'{wit}_anchor_offsets'])
                supplied=d.get(actual_key,'')
                actual=read(sp['path'])[sp['char_start']:sp['char_end']]
                matches=supplied==actual
                wrefs[wit]={'literal_report_field':json_ref(path,f'/differences/{i}/{actual_key}'),
                            'actual_packet_span':sp,'exact_agreement':matches,
                            'original_excerpt_field_name':actual_key,
                            'original_offset_field_name':f'{wit}_anchor_offsets'}
                if not matches:
                    witness_issues.append({'id':d['id'],'witness':wit,'issue':'Reported anchor and attached actual source span differ; both originals preserved.',
                                           'report_ref':json_ref(path,f'/differences/{i}/{actual_key}'),'actual_packet_span':sp})
        rows.append({'original_id':d['id'],'source_ref':json_ref(path,f'/differences/{i}'),
                     'reported_fields':{k:v for k,v in d.items() if k not in long_keys},
                     'witness_exact_source_refs':wrefs,
                     'status':'Immutable reader proposal; root has not selected this row or its counts.'})
    simple={}
    for key in ['doubts','inventory','notation','notes','brief_feedback','check_events','S_coverage',
                'C_doubt_source_map','H_local_marker_audit','original_C_doubt_map',
                'H_marker_audit','S_audit','counting_provenance']:
        if key in report:
            value=report[key]
            if isinstance(value,list):
                simple[key]=[{'source_ref':json_ref(path,f'/{key}/{i}'),'original':x} for i,x in enumerate(value)]
            else:
                simple[key]={'source_ref':json_ref(path,f'/{key}'),'original':value}
    # C source map embeds duplicate difference records; those remain in their exact stored source.
    if 'C_doubt_source_map' in simple:
        for row in simple['C_doubt_source_map']:
            original=row['original']
            if isinstance(original,dict) and 'local_records' in original:
                original=dict(original)
                original['local_records_ref']={**row['source_ref'],'json_pointer':row['source_ref']['json_pointer']+'/local_records'}
                original.pop('local_records')
                row['original']=original
    counts_key=next(k for k in ['counts_proposed','count_proposal','counts_proposal'] if k in report)
    prov_key='processing_provenance' if 'processing_provenance' in report else 'provenance'
    return {'scan':22,'reader':role,'status':'Final reader return, source-only catalog; root selection pending.',
            'main_adjudicated':False,'main_approved':False,
            'complete_original_report':file_ref(path),'complete_original_reading':file_ref(f'out/readers/022/{role}/reading.tex'),
            'report_top_level_fields':{k:json_ref(path,'/'+k) for k in report},
            'differences':rows,**simple,
            'raw_count_and_physical_count_proposals':{'source_ref':json_ref(path,'/'+counts_key),'original':report[counts_key]},
            'processing_provenance':{'source_ref':json_ref(path,'/'+prov_key),'original':report[prov_key]},
            'witness_excerpt_issues':witness_issues,
            'candidate_bank_path':'out/checks/scan022_candidate_sources.json',
            'graphic_source_scope':'Complete candidate ownership, paths, declared origins and baselines belong to tex022 candidate bank; all original identities remain in this report and its support files.',
            'original_doubt_identity_policy':'Seven actual source table rows and seven canonical -1 parts. Reader glyph/state subparts are preserved within their original source row as provenance.',
            'report_silent_choices':text_choice_index(role)}

def fingerprints(roles):
    files={}
    for role in roles:
        for name,expected in EXPECTED[role].items():
            path=f'out/readers/022/{role}/{name}'
            ref=file_ref(path)
            assert ref['sha256']==expected,(path,ref['sha256'],expected)
            files[f'{role}.{name}']={**ref,'released_expected_sha256':expected,'matches_root_release':True,
                                     'scope':'Final immutable return supplied by root'}
        for name in SUPPORT[role]:
            path=f'out/readers/022/{role}/{name}'
            files[f'{role}.{name}']={**file_ref(path),'scope':
                'Historical checkpoint/progress record; not an additional independent reading' if name in
                ['working_audit.md','checkpoint_findings.json','progress.json','processing_state.json',
                 'reading.draft.tex','report.draft.json'] else
                'Final return source support; original provenance retained'}
    return {'scan':22,'released_readers':roles,'pending_readers':[r for r in 'ABC' if r not in roles],
            'files':files,'scope':'Text-only source fingerprints. No image was opened or hashed. No original file was changed.',
            'main_adjudicated':False,'main_approved':False}

if __name__=='__main__':
    releases=['A','B','C']
    results=[write('scan022_source_support_witness_catalog.json',witness_catalog())]
    for role in releases:
        results.append(write(f'scan022_source_support_{role}_catalog.json',report_catalog(role)))
    results.append(write('scan022_source_support_fingerprints_ABC.json',fingerprints(releases)))
    print(json.dumps({'written':results,'released_readers':releases,'originals_changed':False},ensure_ascii=False))
