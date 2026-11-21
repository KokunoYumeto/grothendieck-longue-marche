"""Build the reviewable scan022 record from immutable source and root choices.

Only source strings, references and clerical record counts are processed here.
No image, geometry, mathematical, compilation or rendering operation is used.
"""
from pathlib import Path
import copy, hashlib, json, re
from collections import Counter
from scan022_source_support_prepare import BASE, file_ref, json_ref, span, write
from scan022_source_support_record_specs import SIGMA,WITNESSES,SILENT,NODE_SCOPES,GROUP_OVERRIDES,ALT,KIND,S_STATUS,NOTES

U='out/checks/scan022_source_support_union.json'
L='out/checks/scan022_source_support_record_candidates.json'
W='out/checks/scan022_source_support_witness_catalog.json'
B='out/checks/scan022_candidate_sources.json'
M='out/checks/scan022_final_source_map.json'
D='out/checks/scan022_final_draft.tex'
C='out/checks/scan022_root_count_authorization.json'
J='out/checks/scan022_main_decisions.md'
F='out/checks/scan022_source_support_fingerprints_ABC.json'
read=lambda p:json.loads((BASE/p).read_text())
union,ledger,witness,bank,source_map,counts=map(read,[U,L,W,B,M,C])
draft=(BASE/D).read_text();draft_sha=hashlib.sha256(draft.encode()).hexdigest()
assert draft_sha==source_map['draft_sha256_utf8']
map_sha=file_ref(M)['sha256']
reports={r:read(f'out/readers/022/{r}/report.json') for r in 'ABC'}

def unique(values):return list(dict.fromkeys(values))
def resolve(value,pointer):
 for part in pointer.split('/')[1:]:
  part=part.replace('~1','/').replace('~0','~')
  value=value[int(part)] if isinstance(value,list) else value[part]
 return value
def attach(s,pointer=None):
 a=s.get('start_char',s.get('char_start'));z=s.get('end_char_exclusive',s.get('char_end'))
 assert 0<=a<z<=len(draft)
 literal=draft[a:z]
 expected=s.get('sha256_utf8',s.get('body_sha256'))
 body=hashlib.sha256(literal.encode()).hexdigest()
 if expected:assert body==expected,(a,z,pointer)
 out={'path':'checks/scan022_final_draft.tex','workspace_path':D,'manifest':'checks/scan022_final_source_map.json','workspace_manifest_path':M,'char_start':a,'char_end':z,'byte_start':len(draft[:a].encode()),'byte_end':len(draft[:z].encode()),'line_start':draft.count('\n',0,a)+1,'line_end':draft.count('\n',0,z-1)+1,'literal_sha256_utf8':body,'final_file_sha256':draft_sha,'draft_sha256_utf8':draft_sha,'source_map_sha256':map_sha}
 if pointer:out['source_map_pointer']=pointer
 return out
def literal_attach(text):
 assert draft.count(text)==1,(text,draft.count(text))
 a=draft.index(text);return attach({'start_char':a,'end_char_exclusive':a+len(text)})
def group_attach(g):return attach(source_map['graphical_group_final_spans'][g]['final_span'],f'/graphical_group_final_spans/{g}/final_span')
def node_attach(n):return attach(source_map['A_label_final_spans'][n],f'/A_label_final_spans/{n}')
def group_ref(g):
 role=g[0]
 return json_ref(B,f'/readers/{role}/groups/{g}') if role in 'ABC' else json_ref(M,f'/graphical_group_final_spans/{g}')
def key_of(s):return int(s.split('-L')[1]) if '-L' in s else 'ROOT-M01'

def source_witnesses(row):
 result={r:[] for r in ['C','H']}
 for link in row['witness_blocks']:
  block=resolve(witness,link['json_pointer'])
  for r in result:result[r].extend(block[r])
 return result

def public_reader(row,role,key):
 original=row['readers'][role]
 reported=[x['reported_reading'] for x in original['reported_rows']]
 pieces=reported[:]
 if role in SILENT.get(key,{}):pieces.append(SILENT[key][role])
 if key in SIGMA:
  number,formula=SIGMA[key]
  if role=='B' and number in [7,8,9]:gid='B022-G11' if number==7 else 'B022-G12'
  else:gid=f'{role}022-S{number:02d}'
  if gid in bank['readers'][role]['groups']:
   meta=bank['readers'][role]['groups'][gid]['raw_reader_metadata']
   pieces.append(f'Complete {formula}; original source group {gid}.')
   for k in ['complete_candidates_or_state','candidate_readings','role_or_state','role']:
    if isinstance(meta.get(k),str) and meta[k] not in pieces:pieces.append(meta[k])
 if not pieces:raise AssertionError(('missing actual public reader choice',key,role))
 # The report's short ) proposal does not exhaust A's complete group.
 if key==11 and role=='A':pieces.append('The full A022-G04 group retains inner and outer edge-closing paths and the alpha-in-K label.')
 if key==23 and role=='A':pieces.append('précise retains its own clear acute; A022-M01 is a separate short upper tick.')
 if key==54 and role=='A':pieces.append('Live fermées retains its clear acute; A022-M03 is a separate adjacent upper tick.')
 if key==60 and role=='A':pieces.append('A022-M05-sigma-inner-point is the separate point-shaped fill; it owns neither Sigma paths nor beta.')
 if key==61 and role in 'AB':pieces.append('The point-only group below/right of beta owns neither beta nor the Sigma.')
 return ' '.join(unique(pieces))

decisions=[]
for row in ledger['scope_candidates']:
 key=key_of(row['scope_id']);chosen=next(x for x in counts['rows'] if x['union_id']==row['scope_id'])
 gids=unique(GROUP_OVERRIDES.get(key,row.get('root_selected_source_group_ids') or []))
 attachments=[group_attach(g) for g in gids]
 attachments.extend(node_attach(n) for n in NODE_SCOPES.get(key,[]) if n in source_map['A_label_final_spans'])
 if key==63:attachments=[attach(source_map['attributed_content_note']['final_prose_and_display'],'/attributed_content_note/final_prose_and_display')]
 if key==64:attachments=[literal_attach('ce qui est immédiat')]
 if key==65:attachments=[literal_attach('% archive sheet number: 21')]
 assert attachments,('missing final attachment',row['scope_id'])
 c,h=WITNESSES[key]
 readers={r:public_reader(row,r,key) for r in 'ABC'}
 provenance={r:{**copy.deepcopy(row['readers'][r]),'report_silent_choice':not bool(row['readers'][r]['reported_rows']),'public_complete_source_choice':readers[r],'source_scope':'Complete stored local source and original group registry; silence statements concern the source, without an image-absence claim.'} for r in 'ABC'}
 remaining=chosen['confidence']=='low'
 alternative=ALT.get(key,'')
 assert not remaining or alternative,('missing complete doubt scope',key)
 basis=('Actual H marker '+chosen['H_local_marker_id']+' at this exact locus; neighbouring wording does not inherit the flag.' if chosen['marked_in_H'] else 'The complete attached H locus has no uncertainty or illegibility macro. Plain struck text and descriptive apparatus supply no local doubt flag; the two ill placeholders remain confined to L39/L40.')
 d={'id':row['scope_id'],'source_locus_id':row['scope_id'],'location':row['location'],'C':c,'H':h,'final':row['root_selected_reading'],'readers':readers,'readers_report_only':{r:[x['reported_reading'] for x in row['readers'][r]['reported_rows']] for r in 'ABC'},'reader_provenance':provenance,'confidence':chosen['confidence'],'kind':KIND[key],'evidence':row['root_selected_reading'],'qualification':alternative if remaining else '', 'diff_C':chosen['diff_C'],'diff_H':chosen['diff_H'],'marked_in_H':chosen['marked_in_H'],'marked_in_H_basis':basis,'H_local_marker_id':chosen['H_local_marker_id'],'H_local_marker_provenance':json_ref(W,'/H_actual_local_markers') if chosen['marked_in_H'] else None,'witness_provenance':source_witnesses(row),'C_doubt_status':row.get('root_selected_C_doubt_outcome',{}).get('status') if row.get('root_selected_C_doubt_outcome') else None,'source_C_doubt_rows':[row['canonical_C_doubt_source_id']] if row['canonical_C_doubt_source_id'] else [],'source_C_doubt_parts':[row['canonical_C_doubt_part_id']] if row['canonical_C_doubt_part_id'] else [],'remaining_doubt':remaining,'alternatives':alternative,'root_authorization_sources':row['root_journal_authorizations'],'root_decision_section':chosen['root_decision_section'],'root_count_authorization':json_ref(C,f"/rows/{counts['rows'].index(chosen)}"),'root_ink_choice_applied':bool(row.get('root_ink_choice_applied')),'root_source_audit_choice_applied':bool(row.get('root_source_audit_choice_applied')),'component_confidences':row.get('root_component_confidences',{}),'selected_source_groups':gids,'actual_final_group_ids':gids,'C_count_parent':chosen['C_count_parent'],'H_count_parent':chosen['H_count_parent'],'physical_count_parent':{'C':chosen['C_count_parent'],'H':chosen['H_count_parent']},'final_source_attachment':attachments,'main_approved':False,'selected':True,'log_decision':True,'mathematical_consequence':None,'count_status':'Exact root-authorized physical count flags; final approval pending.','root_source_attachment_status':'Bound to the frozen selected source; final approval pending.'}
 if key==25:d['complete_state_candidates']=source_map['selected_state_metadata']['A022-G10-lower-annotations']['complete_candidates_or_state']
 if key==33:d['complete_state_candidates']=source_map['selected_state_metadata']['A022-S11']['complete_candidates_or_state']
 if key==47:d['mathematical_consequence']=r'The cancelled manuscript variable is recorded as qualified Y with Z and X alternatives; H’s apparatus names a struck X. This states the attributed local readings and supplies no mathematical result.'
 if key==27:d['mathematical_consequence']='The manuscript connector is retained as qualified deleted vertical equals, live equals or arrow-like form, with the shared horizontal drawn once; no equality or implication is inferred from the glyph.'
 if key==65:
  d.update(S_id='SA01-K81-06',S_status=S_STATUS,root_ink_choice_applied=False,root_source_audit_choice_applied=True,S_source=json_ref(W,'/S_rows'))
  d['final']+=' '+S_STATUS;d['evidence']=d['final']
  for role in 'ABC':
   d['readers'][role]+=' S range SA01-K81-06: the report records no exact quoted Sigma_1/U_s example on this page and no added bar from that range.'
   d['reader_provenance'][role]['S_report_source']=json_ref(f'out/readers/022/{role}/report.json','/S_audit' if role=='B' else '/S_coverage')
  d['root_S_public_row_authorization']='Root message: attach exact S_id/S_status to zero-count L65 under section 15, retain authorized high confidence and 66 decisions.'
 decisions.append(d)

by_id={d['id']:d for d in decisions}
group_to_decisions={g:[] for g in source_map['graphical_group_final_spans']}
for d in decisions:
 for g in d['selected_source_groups']:group_to_decisions[g].append(d['id'])

replace_groups={
 'A022-G03-initial-union':['B022-G02'], 'A022-G04-alpha-parentheses':['B022-G03','B022-G04'],
 'A022-G05-underformula-guide':['B022-G05'], 'A022-G06-intersection-insertion':['B022-G06'],
 'A022-S03':['B022-S03'], 'A022-G08-old-relation':['B022-G08'], 'A022-G09-old-emptyset':['B022-G08'],
 'A022-S10':['C022-S10'],'A022-S12':['B022-S12'],'A022-M05-sigma-inner-point':['B022-M04']}
inventory=[]
for index,raw in enumerate(reports['A']['inventory']):
 element=raw['element'];srcs=raw.get('source_refs',[])
 gids=unique([g for x in srcs for g in replace_groups.get(x,[x]) if g in source_map['graphical_group_final_spans']])
 labels=[x for x in srcs if x in source_map['A_label_final_spans']]
 if element=='022.28':gids.append('C022-G09')
 attached=[group_attach(g) for g in unique(gids)]+[node_attach(n) for n in labels]
 if element in ['022.29','022.30']:
  attached=[attach(source_map['attributed_content_note']['final_prose_and_display'],'/attributed_content_note/final_prose_and_display')]
 if element=='022.31':attached=[literal_attach('ce qui est immédiat')]
 if element=='A022-archive':attached=[literal_attach('% archive sheet number: 21')]
 assert attached,('inventory attachment',element)
 related=unique([d['id'] for d in decisions if any(g in d['selected_source_groups'] for g in gids) or any(n in NODE_SCOPES.get(key_of(d['id']),[]) for n in labels)])
 if element in ['022.29','022.30']:related=['U022-L63']
 if element=='022.31':related=['U022-L64']
 if element=='A022-archive':related=['U022-L65']
 item={k:copy.deepcopy(raw[k]) for k in ['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']}
 item.update(selected=True,main_approved=False,original_inventory_element=element,original_inventory_source=json_ref('out/readers/022/A/report.json',f'/inventory/{index}'),original_inventory_value_scope='Unchanged original row remains at the exact immutable source pointer.',original_C_inventory_identity=copy.deepcopy(raw.get('original_C_inventory')),original_source_refs=srcs,selected_source_groups=unique(gids),selected_text_labels=labels,related_decision_ids=related,final_source_attachment=attached,root_inventory_authorization=json_ref(C,'/inventory_authorization'),root_hand_authorization=json_ref(C,'/hand_authorization'),source_order_provenance={'reader':'A','original_index':index,'page_order_y_as_reported':raw.get('page_order_y')},selection_status='Root-selected content; final approval pending.')
 # Keep component rows and whole-region rows visible, without another drawing.
 item['scope_role']='component source reference' if element.startswith('A022-') else 'containing textual region'
 if element.startswith('A022-') and element!='A022-archive':
  local=[by_id[x]['final'] for x in related]
  item['first_words_or_objects']='; '.join(unique(local)) if local else raw['first_words_or_objects']
  item['position']='; '.join(unique(by_id[x]['location'] for x in related)) or raw['position']
  item['components']=unique(gids)
  item['original_position']=raw['position']
  item['original_components_ref']=json_ref('out/readers/022/A/report.json',f'/inventory/{index}')
 if element=='022.01':item['first_words_or_objects']=r'\unsure{Un|On} \unsure{procède|procéde|procédé|procede} par récurrence sur card K,; cancelled opening'
 if element=='022.04':item['first_words_or_objects']='Complete parenthetical V/X/union line, hatted Sigma groups, firm opener and alpha-in-K, firm etant and disjoints; complete qualified one-spanning/two-separate edge-closer candidates.'
 if element=='022.05':item['first_words_or_objects']='Flat guide with upturned ends, two descending equality strokes, inserted intersection and connected minus-alpha Sigma; B022-G05/G06/S03.'
 if element=='022.21':item['first_words_or_objects']='Deleted formule, resolved; local noun strike retained.'
 if element=='022.23':item['first_words_or_objects']=r'comme \unsure{égalité|egalité} dans l’espace; cancelled passage'
 if element=='022.26':item['first_words_or_objects']=r'dans lequel on a deux parties ferm\unsure{è|é|e}es disjointes; cancelled clause'
 if element=='022.28':item['first_words_or_objects']='Y equals complete hatted plus-alpha Sigma; comma; Z with sole qualified returning C022-G09 equals; full beta-in-K-setminus-braced-alpha union and complete S17 with its two separately owned points.'
 if element in ['A022-G04-alpha-parentheses','022.04']:
  item['hand']='mixed: his hand for words, alpha label and opener; undetermined hand/surface origin for thin edge-closing fragments'
 if element=='022.14':
  item['hand']='mixed: his hand for the cancelled Comme wording/formulas; undetermined hand/surface origin for the separate point adjacent to plain V'
  item['contained_qualified_mark_groups']=['R022-M01-plain-V-adjacent-point']
 if element=='022.27':
  item['hand']='mixed: his hand for words and underlines; undetermined hand/surface origin for the adjacent upper tick'
  item['contained_qualified_mark_groups']=['A022-M03-fermees-upper-tick']
 if element=='022.28':
  item['hand']='mixed: his hand for formula glyphs; undetermined hand/surface origin for the interior and below-beta points'
  item['contained_qualified_mark_groups']=['B022-M04','A022-M06-below-beta-point']
 if element=='A022-archive':item.update(hand='undetermined; administrative comment only',first_words_or_objects='Archive label 21 retained only in the source comment; no visible manuscript numeral asserted.',position='source administrative comment after the endpoint',scope_role='administrative source reference')
 inventory.append(item)

def addition(gid,locus,after):
 decision=by_id[locus]
 item={'sheet_kind':'text','hand':'undetermined hand and surface origin','element':gid,'kind':'drawing','position':decision['location'],'first_words_or_objects':decision['final'],'transcribed':'yes','selected':True,'main_approved':False,'original_inventory_element':gid,'source_rows':[], 'selected_source_groups':[gid],'selected_text_labels':[],'related_decision_ids':[locus],'final_source_attachment':[group_attach(gid)],'root_inventory_authorization':json_ref(C,'/inventory_authorization'),'root_hand_authorization':json_ref(C,'/hand_authorization'),'source_order_provenance':{'root_authorized_insertion_after_original_A_element':after,'ordering_basis':'Root journal and existing ordered inventory regions; no coordinate calculation.'},'scope_role':'added physical cluster','selection_status':'Root-selected content; final approval pending.'}
 if gid.startswith('B'):
  originals=[i for i,r in enumerate(reports['B']['inventory']) if gid==r.get('element') or gid in r.get('source_refs',[]) or gid==r.get('id') or gid in str(r.get('graphical_group',''))]
  item['source_rows']=[json_ref('out/readers/022/B/report.json',f'/inventory/{i}') for i in originals]
  item['original_group_source']=group_ref(gid)
 else:item['root_added_group_source']=json_ref(M,f'/graphical_group_final_spans/{gid}')
 pos=next(i for i,x in enumerate(inventory) if x['element']==after)+1
 inventory.insert(pos,item)

addition('B022-M01','U022-L05','022.03')
addition('R022-M01-plain-V-adjacent-point','U022-ROOT-M01','A022-S10')
addition('B022-M06','U022-L44','022.21')
addition('B022-M07','U022-L52','022.26')
assert len(inventory)==len(reports['A']['inventory'])+4
assert len({x['element'] for x in inventory})==len(inventory)

# Whole-region entries explicitly reference their separately owned marks.
for item in inventory:
 for gid in item.get('contained_qualified_mark_groups',[]):
  if gid not in item['selected_source_groups']:item['selected_source_groups'].append(gid)
  item['final_source_attachment'].append(group_attach(gid))
  item['related_decision_ids']=unique(item['related_decision_ids']+group_to_decisions[gid])

group_to_inventory={g:[i['element'] for i in inventory if g in i['selected_source_groups']] for g in source_map['graphical_group_final_spans']}
for gid in group_to_decisions:assert group_to_decisions[gid],('unlinked selected group decision',gid)
for gid in group_to_inventory:assert group_to_inventory[gid],('unlinked selected group inventory',gid)

def path_inventory_owner(gid):
 if gid=='B022-G08':return '022.08'
 if gid=='C022-G09':return '022.28'
 choices=group_to_inventory[gid]
 return next((x for x in choices if x==gid),next((x for x in choices if x.startswith('A022-')),choices[0]))

selected_groups=[{'id':gid,'decision_ids':group_to_decisions[gid],'inventory_elements':group_to_inventory[gid],'source':group_ref(gid),'final_source_attachment':group_attach(gid),'complete_selected_source_ref':json_ref(M,f'/graphical_group_final_spans/{gid}'),'selected_state_metadata_ref':json_ref(M,f'/selected_state_metadata/{gid}') if gid in source_map['selected_state_metadata'] else None,'literal_path_ids':[p for p,v in source_map['path_final_spans'].items() if v['owner']==gid],'source_unit_anchor_and_origin_mapping':json_ref(M,'/uniform_mapping_authority'),'selected':True,'main_approved':False} for gid in source_map['graphical_group_final_spans']]
paths=[{'id':pid,'group_id':v['owner'],'inventory_element':path_inventory_owner(v['owner']),'referencing_inventory_elements':group_to_inventory[v['owner']],'decision_ids':group_to_decisions[v['owner']],'final_source_attachment':attach(v['final_span'],f'/path_final_spans/{pid}/final_span'),'exact_source_attribution':copy.deepcopy(v['source_attribution']),'source_map_ref':json_ref(M,f'/path_final_spans/{pid}'),'scope':'One literal selected command with one owner; containing inventory references do not draw it again.'} for pid,v in source_map['path_final_spans'].items()]

doubts=[{'decision_id':d['id'],'location':d['location'],'reading':d['final'],'alternatives':d['alternatives'],'confidence':d['confidence'],'reason':d['evidence']+' '+d['qualification'],'readers':d['readers'],'reader_provenance':d['reader_provenance'],'source_C_doubt_rows':d['source_C_doubt_rows'],'source_C_doubt_parts':d['source_C_doubt_parts'],'root_authorization_sources':d['root_authorization_sources'],'final_source_attachment':d['final_source_attachment'],'selected_source_groups':d['selected_source_groups'],'main_approved':False,'selected':True,'source_locus_id':d['source_locus_id']} for d in decisions if d['remaining_doubt']]
C_rows=copy.deepcopy(ledger['original_C_source_rows'])
for row in C_rows:
 ds=[d for d in decisions if row['source_id'] in d['source_C_doubt_rows']]
 assert len(ds)==1
 d=ds[0];row['root_original_row_status']=d['C_doubt_status'];row['root_decision_ids']=[d['id']];row['final_source_attachment']=d['final_source_attachment']
 for part in row['source_parts']:
  part.update(original_source_decision_status=part['decision_status'],recorded_root_outcome=d['C_doubt_status'],root_decision_ids=[d['id']],main_approved=False)

original_difference_coverage={role:[{'original_id':x.get('id'), 'source':json_ref(f'out/readers/022/{role}/report.json',f'/differences/{i}'),'selected_decision_ids':[d['id'] for d in decisions if any(p['original_id']==x.get('id') for p in d['reader_provenance'][role]['reported_rows'])]} for i,x in enumerate(reports[role]['differences'])] for role in 'ABC'}
# Reader C retains its original Dxx identities rather than a synthesized prefix.
for role,items in original_difference_coverage.items():
 assert all(v['selected_decision_ids'] for v in items),('unmapped original report difference',role)

original_inventory=[]
for role in 'ABC':
 for index,row in enumerate(reports[role]['inventory']):
  original_inventory.append({'reader':role,'original_index':index,'original_identity':row.get('element',row.get('id')),'source':json_ref(f'out/readers/022/{role}/report.json',f'/inventory/{index}'),'source_union_associations':json_ref(U,f'/graphical_source_associations/{role}'),'selected_inventory_entries':[i['element'] for i in inventory if role=='A' and i.get('original_inventory_element')==row.get('element')],'scope':'Every original inventory row remains at its immutable pointer; candidate identities and source associations remain separate from selected inventory.'})

content=copy.deepcopy(source_map['attributed_content_note'])
content.update(note=NOTES,selected=True,main_approved=False,root_authorization=ledger['root_page_level_source_choices'],mathematical_checks_performed=[],exact_selected_source_refs=json_ref(M,'/attributed_content_note/exact_selected_source_refs'),final_source_attachment=[attach(source_map['attributed_content_note']['final_prose_and_display'],'/attributed_content_note/final_prose_and_display')])
content.pop('final_prose_and_display',None)
abbr=[{'form':'card','expansion':'cardinal (cardinality)','source_form':json_ref(W,'/abbreviation_source_forms/0'),'final_source_attachment':[node_attach('T04')],'selected':True,'main_approved':False,'scope':'Probable expansion in the abbreviation list only; literal manuscript form unchanged.','root_authorization':by_id['U022-L01']['root_authorization_sources']}, {'form':'i.e.','expansion':'id est (that is)','source_form':json_ref(W,'/abbreviation_source_forms/1'),'final_source_attachment':[node_attach('T37')],'selected':True,'main_approved':False,'scope':'Both written points retained; expansion appears only in the abbreviation list.','root_authorization':by_id['U022-L38']['root_authorization_sources']}]

record={'scan':22,'folder':'J81-03','their_page':'21','hua_has':'text','filename':'J81-03_81_scan022.tex','source_record_brief_version':'v04','main_adjudicated':False,'main_approved':False,'released_readers':['A','B','C'],'pending_readers':[],'decisions':decisions,'doubts':doubts,'inventory':inventory,'candidate_inventory':original_inventory,'notes':NOTES,'abbreviations':abbr,'check_events':[],'C_source_rows':C_rows,'C_doubt_resolution_counts':{'actual_rows':7,'actual_parts':7,'original_rows':7,'resolved_primary_parts':3,'retained_primary_parts':4,'pending_primary_parts':0,'resolved_source_rows':counts['C_original_rows']['resolved'],'retained_source_rows':counts['C_original_rows']['retained']},'counts':{'C':sum(d['diff_C'] for d in decisions),'H':sum(d['diff_H'] for d in decisions),'decision_loci':len(decisions),'remaining_doubt_loci':len(doubts),'inventory_elements':len(inventory),'by_witness_confidence':{r:dict(Counter(d['confidence'] for d in decisions if d['diff_'+r])) for r in ['C','H']},'check_events':0,'status':'Exact root-authorized flags and clerical row totals; final approval pending.'},'source_union_manifest':U,'source_union_sha256':file_ref(U)['sha256'],'root_journal':file_ref(J),'root_count_authorization':file_ref(C),'root_approval_status':'Complete selected choices and attachments prepared for root review; final approval pending.','root_choices_applied_through_section':16,'pending_root_decision_ids':[],'pending_root_confidence_ids':[],'source_attachment_status':'Bound to exact selected draft and source map; targeted independent audit and root approval pending.','reader_raw_rows':{r:copy.deepcopy(union['reader_source_scopes'][r]) for r in 'ABC'},'reader_extra_source_fields':json_ref(U,'/reader_source_scopes'),'immutable_reader_fingerprints':file_ref(F),'candidate_graphical_groups':json_ref(B,'/readers'),'original_reader_difference_coverage':original_difference_coverage,'original_reader_doubt_coverage':{r:{'every_original_row':union['reader_source_scopes'][r]['every_doubt_row'],'scope':'All raw reader doubt identities and candidates preserved independently of root-selected remaining doubts.'} for r in 'ABC'},'original_source_issues':json_ref(B,'/source_notes'),'S_source_rows':copy.deepcopy(witness['S_rows']['raw']),'S_public_audit':[{'decision_id':'U022-L65','S_id':'SA01-K81-06','S_status':S_STATUS,'root_ink_choice_applied':False,'root_source_audit_choice_applied':True}],'processing_provenance':{'clerk_source_only':True,'clerk_image_views':0,'image_hashes_accessed':False,'mathematical_or_coordinate_computations':[],'source_offsets_hashes_and_record_bookkeeping_only':True,'reader_operations_preserved_without_rerun':True,'source_preparation_history':json_ref(U,'/phase_history'),'journal_phase_history':json_ref('out/checks/scan022_source_support_journal_state.json','/history'),'source_assembly_provenance':json_ref(M),'root_crop_audit_path_only':'out/checks/scan022_root_crop_audit.json','root_processing_source_path_only':'out/checks/scan022_processing_audit.json','no_image_or_image_hash_read_by_clerk':True},'source_counting_constraints':{'root_basis':counts['count_basis'],'explicit_parents':[{'decision_id':d['id'],'C_parent':d['C_count_parent'],'H_parent':d['H_count_parent']} for d in decisions if d['C_count_parent'] or d['H_count_parent']]},'selected_literal_path_ownership':paths,'selected_literal_component_ownership':json_ref(M,'/node_final_spans'),'original_inventory_coverage':{'all_original_identities_preserved':True,'rows':original_inventory,'actual_C_rows':json_ref(W,'/C_inventory_rows'),'selected_inventory_entries':len(inventory),'base_A_entries':len(reports['A']['inventory']),'root_added_clusters':4,'scope':'A original order and identities retained; four additions interleaved at authorized local regions; no appended second inventory.'},'source_locus_coverage':[{'source_locus_id':d['source_locus_id'],'root_decision_ids':[d['id']],'readers':d['readers'],'reader_provenance':d['reader_provenance'],'final_source_attachment':d['final_source_attachment'],'selected':True,'main_approved':False} for d in decisions],'original_graphical_group_coverage':json_ref(U,'/graphical_source_associations'),'original_report_silent_source_coverage':json_ref(U,'/explicit_report_silent_source_checks'),'selected_graphical_groups':selected_groups,'complete_selected_source_blocks':[{'id':g['id'],'final_source_attachment':g['final_source_attachment'],'exact_complete_block_ref':g['complete_selected_source_ref']} for g in selected_groups],'attributed_content_note':content,'root_selected_content_note':copy.deepcopy(content),'root_ink_pass':{'successful_crop_views':15,'whole_scan_views':0,'supplied_half_views':0,'source':ledger['root_page_level_source_choices'],'clerk_image_views':0,'scope':'Root journal statement only; clerk did not access images or image hashes.'},'selected_draft':{'path':'checks/scan022_final_draft.tex','workspace_path':D,'sha256':draft_sha},'selected_source_map':{'path':'checks/scan022_final_source_map.json','workspace_path':M,'sha256':map_sha},'source_attachment_path_correspondence':{'record_path':'checks/scan022_final_draft.tex','record_base':'out','original_map_path':D,'original_map_base':'.','exact_absolute_target':str(BASE/D),'relation':'Both resolve to the same selected file; offsets refer to its unchanged UTF-8 text.'},'root_ink_decision_entries':sum(d['root_ink_choice_applied'] for d in decisions),'root_source_audit_entries':sum(d['root_source_audit_choice_applied'] for d in decisions),'root_approved_decision_entries':0,'source_clerk_build_script':file_ref('out/checks/scan022_source_support_build_record.py'),'source_clerk_public_specs':file_ref('out/checks/scan022_source_support_record_specs.py')}

record['donor_to_selected_label_correspondence']=[
 {'selected_group':'B022-M01','original_donor_label':'B:T03','original_scope':'pour','selected_label':'A:T06','selected_scope':'pour prouver que','selected_source_attachment':node_attach('T06'),'original_group':group_ref('B022-M01'),'relation':'Original donor ownership is preserved; the selected containing label is explicitly identified.'},
 {'selected_group':'B022-G08','original_donor_label':'B:T10','original_scope':r'\ne\varnothing','selected_label':'A:T15','selected_scope':r'\ne\varnothing','selected_source_attachment':node_attach('T15'),'original_group':group_ref('B022-G08'),'relation':'Separate live replacement remains outside the old relation/empty-set group.'},
 {'selected_group':'B022-M06','original_donor_label':'B:T32','original_scope':r'\unsure{formule|relation}','selected_label':'A:T48','selected_scope':'formule','selected_source_attachment':node_attach('T48'),'original_group':group_ref('B022-M06'),'relation':'The donor’s qualified noun remains original provenance; root resolved the selected complete noun.'}]
assert record['counts']['C']==counts['counts']['C'] and record['counts']['H']==counts['counts']['H']
assert len(decisions)==len(counts['rows'])==66
assert all(set(d['readers'])==set('ABC') for d in decisions)
assert [d['id'] for d in decisions if d['marked_in_H']]==['U022-L39','U022-L40']
out=write('scan022_record_draft.json',record)
print(json.dumps({'record':out,'counts':record['counts'],'selected_draft_sha256':draft_sha,'selected_map_sha256':map_sha,'selected_graphical_groups':len(selected_groups),'selected_literal_paths':len(paths),'original_difference_rows':{r:len(v) for r,v in original_difference_coverage.items()},'status':'Prepared for independent source audit and root review; not approved.'},ensure_ascii=False))
