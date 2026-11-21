"""Build a complete textual crosswalk of released scan022 proposals.

All alignments are source bookkeeping. Counts, physical loci and ink outcomes
remain for root. No image access or coordinate calculation occurs here.
"""
from collections import defaultdict
import json
import re
from scan022_source_support_prepare import (BASE, OUT, read, file_ref, json_ref,
                                           line_span, json_object, write)

# These are complete textual context ranges in immutable reader sources. Exact
# graphical envelopes, paths and declared source placements are in tex022's bank.
REGIONS = {
 'opening': {'A':[(9,25)],'B':[(8,32)],'C':[(2,2)]},
 'top': {'A':[(26,101)],'B':[(33,131)],'C':[(3,74)]},
 'conditions': {'A':[(102,161)],'B':[(132,192)],'C':[(75,145)]},
 'precise': {'A':[(163,174)],'B':[(194,194)],'C':[(147,147)]},
 'equality': {'A':[(175,247)],'B':[(197,279)],'C':[(148,260)]},
 'cancelled_upper': {'A':[(249,313)],'B':[(280,318)],'C':[(261,317)]},
 'soit': {'A':[(314,344)],'B':[(319,344)],'C':[(318,341)]},
 'or_noun': {'A':[(346,374)],'B':[(345,355),(437,451)],'C':[(342,350)]},
 'old_variable': {'A':[(375,413)],'B':[(356,397)],'C':[(351,398)]},
 'cancelled_lower': {'A':[(415,435)],'B':[(398,465)],'C':[(399,434)]},
 'frame': {'A':[(422,435)],'B':[(405,422)],'C':[(405,420)]},
 'live_lower': {'A':[(437,470)],'B':[(466,502)],'C':[(401,446)]},
 'bottom': {'A':[(472,522)],'B':[(503,563)],'C':[(447,513)]},
 'final': {'A':[(524,529)],'B':[(565,570)],'C':[(514,519)]},
}

# Row syntax: ID | descriptive source scope | context region | witness block(s)
# | original A difference suffixes | B suffixes | C IDs | canonical C row.
# Repeated report associations preserve compound scope; they create no count.
SPEC = r'''
L01|opening initial word|opening|W01|D01|D01|D01|
L02|opening verb and local accents|opening|W01|D02|D02|D02|
L03|opening interlinear insertion|opening|W01|D03|D03|D03|
L04|two opening cancellation rules|opening|W01||D04||
L05|short slash below pour|opening|W01||D05||
L06|opening setminus source form|top|W01||||
L07|opening union operator and complete limit|top|W01||D10||
L08|Sigma 01 in opening union|top|W01|GD01||DS01|
L09|Sigma 02 after les|top|W01|GD02|D11|DS02|
L10|small opening curve before alpha in K|top|W01|D04|D06|D04|C022-R01
L11|right-edge closing components and complete closing-state candidates|top|W01|D05|D08|D05|
L12|etant or étant source spelling|top|W01|D06|||
L13|disjoints or disjointes ending|top|W01|D07|D07|D06|C022-R02
L14|lower guide and descending equality ticks|top|W01|D08|D09|D07|
L15|lower intersection insertion and Sigma 03|top|W01||||
L16|first-condition brace|conditions|W02|D09|D12|D08|
L17|trivial word and crossing arrow|conditions|W02|D09|D13|D12|
L18|old crossed relation before replacement|conditions|W02|D10,D11|D14,D15|D09|C022-R03
L19|old empty-set component and cancellation|conditions|W02|D12,D13|D14,D15|D10|
L20|Sigma 04 in second condition|conditions|W02|GD03|D16|DS04|
L21|alors que prose|conditions|W02|D14|D17|D11|
L22|Sigma 05 in right empty-intersection condition|conditions|W02|GD04||DS05|
L23|précise source word and adjoining short tick|precise|W03|MD01|||
L24|main equality with Sigma 06 and nonemptiness parenthesis|equality|W04||||
L25|complete lower left and right annotation states|equality|W04|D15|D18,D19|D13,D15|
L26|Sigma 07 in lower left annotation|equality|W04|GD05|D22|DS07|
L27|right connector glyph, state and shared run|equality|W04|D16,D17|D20,D21|D14|C022-R04
L28|Sigma 08 in lower right annotation|equality|W04|GD06|D23|DS08|
L29|Sigma 09 in lower right annotation|equality|W04|||DS09|
L30|complete cancellation frame and local runs|frame|W05,W06,W07,W08,W09,W10|D30|D24|D16|
L31|cancelled Comme prose, plain V and live continuation wording|cancelled_upper|W05||||
L32|Sigma 10 after cancelled Comme V subset|cancelled_upper|W05|||DS10|
L33|Sigma 11 head and shared upper frame or closure run|cancelled_upper|W05|D18,GD07|D38|D31,DS11|
L34|small trace left of cancellation frame|cancelled_upper|W05|MD02|D25|D28|
L35|cancelled inverse-inclusion display endpoint|cancelled_upper|W06|D19|D26|D17|
L36|Sigma 12 in cancelled inverse display|cancelled_upper|W06||||
L37|Sigma 13 in cancelled Soit line|soit|W07|GD08|D39|DS13|
L38|literal i.e. and complete neighbourhood continuation|soit|W07||||
L39|endpoint after rencontre and H ill scope|soit|W07|D20|D27|D18|
L40|cancelled on after Or and H ill scope|or_noun|W08|D21|D28|D19|C022-R05
L41|cancelled peut|or_noun|W08|D22|D29|D20|
L42|cancelled considérer|or_noun|W08|D23|D30|D21|
L43|old noun under inserted égalité|or_noun|W08|D24|D31|D22|C022-R06
L44|small point beside old noun|or_noun|W08||D45||
L45|inserted égalité and its state in cancelled passage|or_noun|W08||||
L46|second égalité or egalité after comme|or_noun|W08||D32||
L47|complete old-variable candidates and crossings|old_variable|W09|D25,D26|D33,D34|D23|C022-R07
L48|Sigma 14 in old-variable equation|old_variable|W09|GD09|D40|DS14|
L49|Sigma 15 in old-variable equation|old_variable|W09|GD10|D41|DS15|
L50|cancelled relative pronoun lequel|cancelled_lower|W10|D27|D35|D24|
L51|cancelled fermées accent and full continuation|cancelled_lower|W10|D28|||
L52|two right-edge points by lower cancelled/live transition|cancelled_lower|W10,W11||D47||
L53|live fermées underline|live_lower|W11|D29|D36|D25|
L54|live fermées word and adjoining upper tick|live_lower|W11|MD03|||
L55|live disjointes word and independent underline|live_lower|W11||||
L56|detached lower slash above-right of disjointes|live_lower|W11|MD04|D37|D27|
L57|Sigma 16 in Y definition|bottom|W12|||DS16|
L58|relation after bottom Z|bottom|W12|||D30|
L59|Sigma 17 in Z definition|bottom|W12|GD11|D42|DS17|
L60|point inside Sigma 17|bottom|W12|MD05|D43|D29|
L61|point below-right of final beta|bottom|W12|MD06|D44||
L62|lower union and complete beta-in-K-setminus-alpha limit|bottom|W12||||
L63|final instruction and complete closure equality|final|W13||||
L64|final immédiat endpoint|final|W13|D31|D46|D26|
L65|archive numeral and source administrative label|final|W14||||
'''

# Selected bounded report-silent source checks. These are literal source facts,
# not conclusions about image content. Complete source references stay attached.
SILENT = [
 ('L12','B',[(89,89)],'The complete node writes étant disjoints without an accent qualifier.'),
 ('L12','C',[(74,74)],'The source continuation writes étant; the adjacent disjoints/disjointes qualifier is separate.'),
 ('L23','B',[(194,194)],'The complete prose line writes De façon précise, je dis que.'),
 ('L23','C',[(147,147)],'The complete prose line writes De façon précise, je dis que.'),
 ('L31','A',[(249,289)],'The complete cancelled Comme source writes V subset and the following V cap E without an overline on that V.'),
 ('L31','B',[(280,307)],'The complete cancelled Comme source writes V subset and the following V cap E without an overline on that V.'),
 ('L31','C',[(261,298)],'The complete cancelled Comme source writes V subset and the following V cap E without an overline on that V.'),
 ('L38','A',[(332,344)],'The complete Soit continuation retains literal i.e. with both points.'),
 ('L38','B',[(334,344)],'The complete Soit continuation retains literal i.e. with both points.'),
 ('L38','C',[(334,341)],'The complete Soit continuation retains literal i.e. with both points.'),
 ('L45','A',[(358,364)],'The inserted égalité state is encoded within the surrounding cancelled passage; complete following words are retained.'),
 ('L45','B',[(351,354)],'The inserted égalité state and following comme/égalité/dans nodes are retained with their own qualifications.'),
 ('L45','C',[(346,349)],'The inserted égalité state and following comme/égalité dans nodes are retained.'),
 ('L46','A',[(360,364)],'The following node writes égalité without a local accent qualifier.'),
 ('L46','C',[(347,349)],'The following node writes égalité dans without a local accent qualifier.'),
 ('L51','B',[(398,404)],'The complete cancelled continuation writes fermées without a local accent qualifier.'),
 ('L51','C',[(399,400)],'The complete cancelled continuation writes fermées without a local accent qualifier.'),
 ('L54','B',[(466,480)],'The complete live wording writes fermées and its underline; the referenced scope supplies the actual source surrounding this word.'),
 ('L54','C',[(401,404)],'The complete live wording writes uline{fermées} and uline{disjointes}; the referenced scope supplies both source nodes.'),
 ('L58','A',[(483,489)],'The complete Z source node writes Z= without a local relation qualifier.'),
 ('L58','B',[(514,520)],'The complete Z source node writes Z= without a local relation qualifier.'),
 ('L61','C',[(487,508)],'The complete S17 source contains its beta/sign, roof/head/body and nested M03 interior-point group. This is the full stored local source to compare with the other readers’ below-beta points.'),
 ('L63','A',[(524,527)],'Complete final instruction and equality preserved literally.'),
 ('L63','B',[(565,568)],'Complete final instruction and equality preserved literally.'),
 ('L63','C',[(514,517)],'Complete final instruction and equality preserved literally.'),
]

SUPPLEMENTARY_GROUP_SCOPES = {
 'A': {
  'A022-G01-opening-cancellations':['L04'], 'A022-G02-initial-separator':['L06'],
  'A022-G03-initial-union':['L07'], 'A022-G06-intersection-insertion':['L15'],
  'A022-S03':['L15'], 'A022-S06':['L24'], 'A022-S09':['L29'],
  'A022-S10':['L32'], 'A022-S12':['L36'],
  'A022-G12-local-on-and-noun-cancellations':['L40','L43','L45'],
  'A022-G15-live-underlines':['L53','L55'], 'A022-S16':['L57'],
  'A022-G16-final-union':['L62'],
 },
 'B': {
  'B022-S01':['L08'], 'B022-G06':['L15'], 'B022-S03':['L15'],
  'B022-S05':['L22'], 'B022-S06':['L24'], 'B022-G10':['L25'],
  'B022-G12':['L25','L28','L29'], 'B022-S10':['L32'],
  'B022-S12':['L36'], 'B022-G16':['L53','L55'],
  'B022-S16':['L57'], 'B022-G17':['L62'],
 },
 'C': {
  'C022-G01':['L06','L07','L14','L15'], 'C022-S03':['L15'],
  'C022-G04':['L16','L17','L18','L19','L20','L21','L22'],
  'C022-G05':['L24','L25','L27','L30','L31','L35','L38','L40','L43','L45','L46','L50','L51','L53','L55','L56'],
  'C022-S06':['L24'], 'C022-S12':['L36'], 'C022-G08':['L57','L58','L59','L60','L61','L62'],
 },
}

ORIGINAL_INVENTORY_SCOPES = {
 '022.01':['L01','L02','L04'], '022.02':['L03'], '022.03':['L04','L05'],
 '022.04':['L06','L07','L08','L09','L10','L11','L12','L13'],
 '022.05':['L14','L15'], '022.06':['L16','L18','L19','L20','L21','L22'],
 '022.07':['L17'], '022.08':['L18','L19'], '022.09':['L23'],
 '022.10':['L24'], '022.11':['L25','L26'], '022.12':['L25','L28','L29'],
 '022.13':['L27'], '022.14':['L30','L31','L32','L33','L34'],
 '022.15':['L35','L36'], '022.16':['L35','L36'], '022.17':['L37','L38','L39'],
 '022.18':['L40'], '022.19':['L40'], '022.20':['L41','L42'],
 '022.21':['L43'], '022.22':['L45'], '022.23':['L46'],
 '022.24':['L47','L48','L49'], '022.25':['L47','L48','L49'],
 '022.26':['L50','L51','L52'], '022.27':['L53','L54','L55','L56'],
 '022.28':['L57','L58','L59','L60','L61','L62'],
 '022.29':['L63'], '022.30':['L63'], '022.31':['L64'],
}

def graphical_associations(reports, report_to_loci):
    bank_path='out/checks/scan022_candidate_sources.json'
    bank=json_object(bank_path)
    result={}
    for role in 'ABC':
        source=bank['readers'][role]
        groups=source['groups']
        original_labels=defaultdict(list)
        for nid,node in source['nodes'].items():
            if node.get('original_reader_node_id'):
                original_labels[node['original_reader_node_id']].append(nid)
        group_rows=defaultdict(list)
        group_loci=defaultdict(set)
        for gid,loci in SUPPLEMENTARY_GROUP_SCOPES[role].items():
            assert gid in groups,gid
            group_loci[gid].update('U022-'+x for x in loci)
        difference_backlinks=[]
        for i,d in enumerate(reports[role]['differences']):
            ids=d.get('source_group_ids',d.get('source_groups',[]))
            gs=[];ns=[];other=[]
            for identity in ids:
                if identity in groups:
                    gs.append(json_ref(bank_path,f'/readers/{role}/groups/{identity}'))
                    group_rows[identity].append(json_ref(f'out/readers/022/{role}/report.json',f'/differences/{i}'))
                    group_loci[identity].update(report_to_loci[role][d['id']])
                elif identity in original_labels:
                    ns.extend(json_ref(bank_path,f'/readers/{role}/nodes/{x}') for x in original_labels[identity])
                else:
                    other.append(identity)
            difference_backlinks.append({'original_difference_id':d['id'],
                'original_reference_values':ids,'candidate_group_refs':gs,'candidate_node_refs':ns,
                'original_nongroup_source_scopes':other})
        inventory=[]
        inv_by_group=defaultdict(list)
        for i,entry in enumerate(reports[role]['inventory']):
            ids=list(entry.get('source_refs',[]))
            if entry.get('source_group'): ids.append(entry['source_group'])
            ids.extend(x['id'] for x in entry.get('literal_component_groups',[]))
            if entry['element'] in groups: ids.append(entry['element'])
            # Preserve abbreviated source-owner text literally. Exact full group
            # IDs are resolved only from the reader's supplied component records.
            ids=list(dict.fromkeys(ids))
            gs=[x for x in ids if x in groups]
            ns=[n for x in ids for n in original_labels.get(x,[])]
            loci=set('U022-'+x for x in ORIGINAL_INVENTORY_SCOPES.get(entry['element'],[]))
            if entry['element'] in ['A022-archive','B022-ARCHIVE','I_ARCHIVE']:
                loci.add('U022-L65')
            for gid in gs:
                loci.update(group_loci[gid])
                inv_by_group[gid].append(json_ref(f'out/readers/022/{role}/report.json',f'/inventory/{i}'))
            inventory.append({'original_inventory_identity':entry['element'],
                'source_ref':json_ref(f'out/readers/022/{role}/report.json',f'/inventory/{i}'),
                'original_source_references':ids,
                'original_source_owner':entry.get('source_owner'),
                'original_hand':entry['hand'],
                'original_hand_parts':entry.get('hand_attribution_parts'),
                'candidate_group_refs':[json_ref(bank_path,f'/readers/{role}/groups/{x}') for x in gs],
                'candidate_node_refs':[json_ref(bank_path,f'/readers/{role}/nodes/{x}') for x in ns],
                'aligned_union_ids':sorted(loci),
                'reported_difference_refs':[json_ref(f'out/readers/022/{role}/report.json',f'/differences/{j}')
                    for j,d in enumerate(reports[role]['differences'])
                    if loci.intersection(report_to_loci[role][d['id']])],
                'source_scope_policy':'Reader inventory identity and original order retained; these source associations assign no selected content or hand.'})
        group_registry=[]
        for gid,entry in groups.items():
            group_registry.append({'original_group_id':gid,
                'complete_candidate_ref':json_ref(bank_path,f'/readers/{role}/groups/{gid}'),
                'literal_path_refs':entry['direct_path_refs'],
                'literal_node_refs':entry['leaf_node_refs'],
                'reported_difference_refs':group_rows[gid],
                'reader_inventory_refs':inv_by_group[gid],
                'aligned_union_ids':sorted(group_loci[gid]),
                'complete_enclosing_source_ref':entry.get('complete_enclosing_node_ref'),
                'parent_group_identity':entry.get('immediate_source_parent_group'),
                'contained_group_identities':entry['contained_group_ids'],
                'declarations_and_origins_ref':json_ref(bank_path,f'/readers/{role}/groups/{gid}'),
                'selection_status':'Unselected immutable candidate; root source choice pending.'})
        result[role]={'all_groups':group_registry,
                      'difference_to_source':difference_backlinks,
                      'inventory_to_source_in_original_order':inventory,
                      'all_complete_compositions':json_ref(bank_path,f'/readers/{role}/complete_compositions'),
                      'all_literal_paths':json_ref(bank_path,f'/readers/{role}/paths'),
                      'all_source_nodes':json_ref(bank_path,f'/readers/{role}/nodes')}
    return result

def build_union():
    reports={r:json_object(f'out/readers/022/{r}/report.json') for r in 'ABC'}
    dictionaries={r:{d['id']:(i,d) for i,d in enumerate(reports[r]['differences'])} for r in 'ABC'}
    rows=[]
    seen={r:set() for r in 'ABC'}
    report_to_loci={r:defaultdict(list) for r in 'ABC'}
    wc='out/checks/scan022_source_support_witness_catalog.json'
    witness=json_object(wc)
    blocks={d['id']:i for i,d in enumerate(witness['source_blocks'])}
    for line in SPEC.strip().splitlines():
        lid,location,region,wblocks,a,b,c,actual=line.split('|')
        readers={}
        for role,ids in [('A',a),('B',b),('C',c)]:
            ids=[(role+'022-'+x if role in 'AB' else x) for x in ids.split(',') if x]
            refs=[]
            for identity in ids:
                i,d=dictionaries[role][identity]
                refs.append({'original_id':identity,
                             'report_ref':json_ref(f'out/readers/022/{role}/report.json',f'/differences/{i}'),
                             'reported_reading':d['reading'],
                             'original_group_or_label_ids':d.get('source_group_ids',d.get('source_groups',[]))})
                seen[role].add(identity)
                report_to_loci[role][identity].append('U022-'+lid)
            readers[role]={
                'reported_rows':refs,
                'complete_source_context':[line_span(f'out/readers/022/{role}/reading.tex',*rg) for rg in REGIONS[region][role]],
                'all_node_and_line_choices_ref':json_ref(f'out/checks/scan022_source_support_{role}_catalog.json','/report_silent_choices'),
                'report_silence_policy':'The source context supplies the reading. An empty reported_rows list supplies no reading or image-absence claim.'}
        marker_id={'L39':'H022-ILL01','L40':'H022-ILL02'}.get(lid)
        rows.append({'id':'U022-'+lid,'location':location,'source_context_region':region,
                     'witness_blocks':[json_ref(wc,f'/source_blocks/{blocks[x]}') for x in wblocks.split(',')],
                     'readers':readers,
                     'canonical_C_doubt_source_id':actual or None,
                     'canonical_C_doubt_part_id':actual+'-1' if actual else None,
                     'H_local_marker_source_fact':{'marked_in_H':bool(marker_id),'actual_marker_id':marker_id,
                         'source_basis':json_ref(wc,'/H_actual_local_markers/'+('0' if lid=='L39' else '1')) if marker_id else
                         'The attached local wording/shape scope has no H uncertainty macro. Broader attached context and descriptive notes do not transfer the two distinct ill scopes.'},
                     'root_selected_reading':None,'root_selected_counts':None,
                     'scope_status':'Textual alignment only; compound report scope and original component identities remain explicit.'})
    omitted={r:sorted(set(dictionaries[r])-seen[r]) for r in 'ABC'}
    assert not any(omitted.values()),omitted
    silent=[]
    for lid,role,ranges,statement in SILENT:
        silent.append({'union_id':'U022-'+lid,'reader':role,'source_statement':statement,
                       'complete_exact_source':[line_span(f'out/readers/022/{role}/reading.tex',*rg, literal=True) for rg in ranges],
                       'status':'Source-only statement. No image interpretation or physical count assigned.'})
    source_rows=[]
    for i,wrow in enumerate(witness['C_actual_doubt_rows']):
        rid=wrow['source_id']
        outcomes={}
        for role in 'ABC':
            key='original_C_doubt_map' if role=='B' else 'C_doubt_source_map'
            raw=reports[role][key][i]
            rawid=raw.get('source_id',raw.get('source_row_id',raw.get('id')))
            assert rawid==rid,(role,rawid,rid)
            outcomes[role]={'source_ref':json_ref(f'out/readers/022/{role}/report.json',f'/{key}/{i}'),
                            'reported_status':raw.get('return_status',raw.get('status')),
                            'reader_local_parts_ref':json_ref(f'out/readers/022/{role}/report.json',f'/{key}/{i}/'+('parts' if role=='B' else 'local_parts')),
                            'original_difference_ids':raw.get('difference_ids',raw.get('decision_ids'))}
        source_rows.append({'source_id':rid,'source_parts':wrow['source_parts'],
                            'exact_source_ref':json_ref(wc,f'/C_actual_doubt_rows/{i}'),
                            'reader_outcomes':outcomes,'root_outcome':None})
    scopes={}
    for role in 'ABC':
        rp=f'out/readers/022/{role}/report.json'
        ck=next(x for x in ['count_proposal','counts_proposal','counts_proposed'] if x in reports[role])
        scopes[role]={
            'report':file_ref(rp),
            'source_catalog':file_ref(f'out/checks/scan022_source_support_{role}_catalog.json'),
            'every_difference_row':[{'original_id':d['id'],'source_ref':json_ref(rp,f'/differences/{i}'),
                                     'aligned_union_ids':report_to_loci[role][d['id']]} for i,d in enumerate(reports[role]['differences'])],
            'every_doubt_row':[{'original_id':d.get('id'),'source_ref':json_ref(rp,f'/doubts/{i}')} for i,d in enumerate(reports[role]['doubts'])],
            'every_inventory_row_in_original_order':[{'original_identity':d['element'],'source_ref':json_ref(rp,f'/inventory/{i}'),
                                                       'source_order_ordinal':i+1} for i,d in enumerate(reports[role]['inventory'])],
            'every_notation_row':[json_ref(rp,f'/notation/{i}') for i,_ in enumerate(reports[role]['notation'])],
            'all_notes':json_ref(rp,'/notes'),
            'all_raw_counts_and_physical_count_proposals':json_ref(rp,'/'+ck),
            'all_remaining_report_fields':json_ref(f'out/checks/scan022_source_support_{role}_catalog.json','/report_top_level_fields'),
            'all_report_silent_source_choices':json_ref(f'out/checks/scan022_source_support_{role}_catalog.json','/report_silent_choices'),
        }
    bank='out/checks/scan022_candidate_sources.json'
    return {
        'scan':22,'status':'Complete released-source union; root ink choices, physical counts and selected-source assembly pending.',
        'main_adjudicated':False,'main_approved':False,
        'scope':'Every final A/B/C report row, exact C/H source, every reader source line/node, graphical source registry and original C identity retained. Earlier drafts remain separate historical records.',
        'immutable_reader_fingerprints':file_ref('out/checks/scan022_source_support_fingerprints_ABC.json'),
        'witness_catalog':file_ref(wc),'reader_source_scopes':scopes,
        'textual_locus_crosswalk':rows,'explicit_report_silent_source_checks':silent,
        'graphical_source_associations':graphical_associations(reports,report_to_loci),
        'original_C_source_rows':source_rows,
        'graphical_candidate_bank':file_ref(bank) if (BASE/bank).exists() else {'path':bank,'status':'tex022 bank pending'},
        'source_alignment_validation':{'every_original_difference_id_present':not any(omitted.values()),'unmapped_original_difference_ids':omitted,
            'C_canonical_source_rows':7,'C_canonical_parts':7,
            'scope':'Exact identity coverage only. No ink locus or physical-count calculation.'},
        'phase_history':[
            {'reader':'A','checkpoint_ref':file_ref('out/readers/022/A/checkpoint_findings.json'),
             'complete_provenance':json_ref('out/readers/022/A/report.json','/provenance'),
             'status':'Historical findings, superseded by final reading/report. One A reading.'},
            {'reader':'B','checkpoint_source':file_ref('out/readers/022/B/reading.draft.tex'),
             'checkpoint_report':file_ref('out/readers/022/B/report.draft.json'),
             'complete_provenance':json_ref('out/readers/022/B/report.json','/provenance'),
             'status':'Historical unfinished drafts, superseded by final reading/report. One B reading.'},
            {'reader':'C','checkpoint_ref':file_ref('out/readers/022/C/working_audit.md'),
             'complete_provenance':json_ref('out/readers/022/C/report.json','/processing_provenance'),
             'status':'Checkpoint and final-return sections remain distinct in the original history. One C reading.'},
            {'source_clerk_partial_fingerprints':file_ref('out/checks/scan022_source_support_fingerprints_AC.json'),
             'status':'Earlier A/C-only release phase; superseded for current coverage by ABC fingerprints. No additional reading.'},
        ],
        'source_audit_notes':[
            'All root-released main hashes matched; every reported witness excerpt/anchor matched its attached packet source.',
            'B reports eight reader-local doubt parts; canonical actual source identity remains seven rows and seven -1 parts. R04 glyph/state subdivisions are retained in B provenance.',
            'C S08 owns a stale G04 comment while C G06 and ownership records own the shared rule. The immutable text and competing references are retained in tex022 source notes.',
            'A report lower-annotation row covers both formulas; B and C retain separate local rows. Crosswalk membership does not assign a joint physical count.',
            'A brace/arrow row and B old-relation/empty-set rows occur in each applicable textual scope. Their original report identities are counted once in source coverage.',
        ],
        'awaiting':'Root crop journal and selected source/count instructions. No final page, approval or commit created.'
    }

if __name__=='__main__':
    result=build_union()
    print(json.dumps(write('scan022_source_support_union.json',result),ensure_ascii=False))
