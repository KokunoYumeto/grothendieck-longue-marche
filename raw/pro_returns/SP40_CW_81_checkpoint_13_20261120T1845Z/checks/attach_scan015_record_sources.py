"""Attach the root-selected scan015 draft to every union record; no image/TeX processing."""
import json,re,hashlib,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent;CHECK=ROOT/'checks'
p=CHECK/'scan015_record_draft.json';d=json.loads(p.read_text());by={x['id']:x for x in d['decisions']}
draft_path=CHECK/'scan015_final_draft.tex';t=draft_path.read_text();ls=t.splitlines(keepends=True)
mapping_path=CHECK/'scan015_final_source_map.json';mapping=json.loads(mapping_path.read_text());blocks={x['id']:(i,x) for i,x in enumerate(mapping['component_manifest'])}
offsets=[0]
for line in ls:offsets.append(offsets[-1]+len(line))
def ref(block,token=None,ranges=None,occ=0,scope=None):
 bi,b=blocks[block];a0,b0=b['draft_lines_inclusive'];a,bend=offsets[a0-1],offsets[b0]
 if ranges is not None:
  a0,b0=ranges;a,bend=offsets[a0-1],offsets[b0]
 if token is not None:
  found=[m.start() for m in re.finditer(re.escape(token),t[a:bend])]
  assert found,(block,token)
  a=a+found[occ];bend=a+len(token);a0=t.count('\n',0,a)+1;b0=t.count('\n',0,bend)+1
 return {'manifest':'root.final_draft.tex','path':'checks/scan015_final_draft.tex','char_start':a,'char_end':bend,'line_start':a0,'line_end':b0,'group_anchor':block,'assembly_map':{'manifest':'root.final_source_map.json','pointer':f'/component_manifest/{bi}'},'scope':scope or ('selected exact literal' if token is not None else 'explicit selected group or component range')}
def pathrefs(block,ids):
 bi,b=blocks[block];ans=[]
 for i in ids:
  q=b['literal_path_sources'][i];z=ref(block,ranges=q['draft_lines_inclusive']);z['assembly_path_pointer']=f'/component_manifest/{bi}/literal_path_sources/{i}';ans.append(z)
 return ans
def put(key,block,token=None,ranges=None,paths=None,scope=None):
 x=by['015-'+key];r=pathrefs(block,paths) if paths is not None else [ref(block,token,ranges,scope=scope)]
 x['root_page_sources']=r;x['final_source_attachment']=r;x['root_source_attachment_status']='complete selected draft attachment; main record approval remains with root'

simple={
 'D01a':('page_and_heading',r'\deleted{\unsure{I|V}}'),'D01b':('page_and_heading','Version'),
 'D02':('opening_prose',r'\deleted{\unsure{\Sigma|S}}E_i'),'D03':('opening_tail_and_upper_note',r'\unsure{tte|toute|tt}'),'D04':('opening_tail_and_upper_note','non'),
 'D05':('upper_right_nb',r'\Sigma_i^{\unsure{+|-|\ast}}'),'D06':('upper_right_nb',r'X\setminus\Sigma_i'),
 'D07':('condition_b_and_main_nb',r'X\setminus\deleted{\Sigma}E_i.'),'D08':('condition_b_and_main_nb','automatiquement'),
 'D09a':('case_heading',r'\deleted{\unsure{(\mathrm{de})}}'),'D09b':('case_heading',r'\deleted{\unsure{\leq|=}}='),
 'D10':('main_drawing',r'\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}'),'D11':('main_drawing',r'\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}'),
 'D11-old':('main_drawing',r'\deleted{\unsure{+}}'),'D11-live':('main_drawing',r'\unsure{-}'),
 'D12':('cancelled_inclusions_and_equivalence',r'\unsure{équivaut|èquivaut}'),'D12-accent':('cancelled_inclusions_and_equivalence',r'\unsure{équivaut|èquivaut}'),
 'D14':('symmetry_and_equation_2_prime',r'\unsure{et}'),'D15':('lower_correction_group',r'\deleted{\unsure{vois. ouvert}}'),
 'D16':('lower_slanted_note',r'\unsure{à sign.ler|à signaler}'),'D17':('final_un_and_connector',r'\inserted{un}'),'D18':('final_un_and_connector',r'\unsure{donc|puis}'),
 'D19-glyph':('final_cancelled_group_and_ending',r'\deleted{\unsure{\Sigma_1^+\text{ serait}|\Sigma_1^+\ne\varnothing}}'),
 'D20':('opening_guide',r'\inserted{\unsure{fermés|fermées}}'),'D21a':('opening_tail_and_upper_note','conn.'),'D21b':('opening_tail_and_upper_note',r'\unsure{\Sigma_i|\Sigma}'),
 'H01':('opening_tail_and_upper_note','On suppose de plus que'),'H02':('condition_a',r'\operatorname{Card}'),'H03':('condition_a',r'\deleted{\Sigma}E_i'),
 'H04':('upper_right_nb',r'\uline{NB}'),'H05':('condition_b_and_main_nb',r'\deleted{\Sigma}E_j'),'H06':('condition_b_and_main_nb','Cette'),
 'H07':('condition_b_and_main_nb','automatiquement les'),'H08':('condition_b_and_main_nb',r'\deleted{\Sigma}E_i$'),'H09':('condition_b_and_main_nb','mutuellement'),
 'H10':('case_heading',r'\operatorname{Card}'),'H11':('cancelled_inclusions_and_equivalence',r'\text{\unsure{équivaut|èquivaut} à}'),
 'P02':('si_on_avait_through_equation_2',r'\deleted{Si on avait} comme'),'H12':('si_on_avait_through_equation_2','aussi à'),
 'H13':('symmetry_and_equation_2_prime',r'\unsure{symètriquement|symétriquement}, à'),'H14':('lower_correction_group',r'\uline{vois}.'),
 'H15':('lower_correction_group',r'on \unsure{a}'),'H15-colon':('lower_correction_group',r'on \unsure{a}'),'H18':('lower_display_and_car_formula','Car'),
 'P09-apostrophe':('final_insertion_group',r"\inserted{\unsure{l'ouvert|louvert}}"),
 'H-TITLE':('page_and_heading',r'\uline{\deleted{\unsure{I|V}}Version I}'),'H-ARROW':('opening_tail_and_upper_note',r'\nearrow'),
 'H-COMMA':('opening_tail_and_upper_note',r'\overline{\Sigma}_i\ne\Sigma_i$ i.e.'),
 'G-NB-RULE':('upper_right_nb',r'\overset{\unsure{\rule{.8em}{.35pt}}}{\Sigma}_i^+'),
 'G-SYM-ACCENT':('symmetry_and_equation_2_prime',r'\unsure{symètriquement|symétriquement}'),
 'S-NOTE-FIRST':('lower_slanted_note',r'\overline{\Sigma_1^+}\cap E_1\ne\varnothing'),'S-NOTE-SECOND':('lower_slanted_note',r'\overline{\Sigma_1^+}\ne\Sigma_1^+'),
 'S-FINAL':('lower_display_and_car_formula',r'\overline{\Sigma_1^+}\cap E_1')}
for key,args in simple.items():put(key,*args)
groups={'D13':'car_si','D19':'final_cancelled_group_and_ending','P01':'cancelled_inclusions_and_equivalence','P07':'lower_correction_group','P08':'lower_correction_group','H17':'lower_slanted_note','P09':'final_insertion_group','P09-commas':'final_insertion_group','H-DRAW':'main_drawing','G10-GROUP':'lower_slanted_note','G01':'opening_detached_mark','G08':'right_detached_pair'}
for key,block in groups.items():put(key,block)
paths={'G02':('opening_guide',[0]),'G03':('case_heading',[0,1]),'G04':('main_drawing',[13,14]),'G06':('car_si',[0,1]),'G11':('lower_display_and_car_formula',[0]),'G12':('final_cancelled_group_and_ending',[0,1,2]),'G13':('main_drawing',list(range(9))),'G14':('cancelled_inclusions_and_equivalence',[0]),'G-LOUVERT':('final_insertion_group',[0]),'G-VOIS-CANCEL':('lower_correction_group',[0]),'G-IL-CANCEL':('lower_correction_group',[2]),'G-REMNANT-ANGULAR':('final_cancelled_group_and_ending',[1]),'DRAW-upper-right':('main_drawing',[0,1]),'DRAW-left-edge':('main_drawing',[6,7,8]),'DRAW-left-brace1':('main_drawing',[10]),'DRAW-left-brace2':('main_drawing',[11]),'DRAW-right-brace':('main_drawing',[12]),'DRAW-chord1':('main_drawing',[9]),'DRAW-chord2':('main_drawing',[9])}
for key,(block,ids) in paths.items():put(key,block,paths=ids)
for key,block,rng in [('G05','main_drawing',[100,103]),('G07','cancelled_inclusions_and_equivalence',[120,123]),('G09','lower_correction_group',[164,167]),('G10a','lower_slanted_note',[186,193]),('G10b','lower_slanted_note',[196,200]),('G-REMNANT','final_cancelled_group_and_ending',[235,238])]:put(key,block,ranges=rng)
labels={'E1':r'\node at (139,116) {$E_1$};','E2':r'\node at (150,247) {$E_2$};','Sigma1plus':r'\node at (430,68) {$\Sigma_1^+$};','Sigma1minus':r'\node at (501,193) {$\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}$};','Sigma2minus':r'\node at (23,135) {$\Sigma_2^-$};','Sigma2plus':r'\node at (131,308) {$\Sigma_2^+$};'}
for key,tok in labels.items():put('DRAW-label-'+key,'main_drawing',tok)
assert all(x.get('root_page_sources') for x in d['decisions'])

inv={int(x['element'].split('I')[-1]):x for x in d['inventory']}
def iput(n,refs):
 inv[n]['root_page_sources']=refs;inv[n]['transcribed']='yes';inv[n]['final_source_attachment_status']='complete selected-source attachment';inv[n]['root_ink_choice_status']='all choices complete through section26; common text retained as selected'
iranges={1:('page_and_heading',[6,6]),3:('opening_detached_mark',[8,12]),8:('opening_tail_and_upper_note',[25,25]),10:('condition_a',[27,30]),12:('upper_right_nb',[33,33]),14:('condition_b_and_main_nb',[34,40]),17:('condition_b_and_main_nb',[42,42]),19:('purpose',[44,44]),20:('case_heading',[49,50]),24:('case_setup',[58,58]),25:('main_drawing',[65,86]),26:('main_drawing',[92,95]),27:('main_drawing',[89,89]),30:('main_drawing',[100,103]),31:('equation_1_and_ce_qui',[105,108]),34:('cancelled_inclusions_and_equivalence',[114,115]),36:('cancelled_inclusions_and_equivalence',[120,123]),40:('car_si',[132,133]),44:('si_on_avait_through_equation_2',[139,142]),45:('right_detached_pair',[143,148]),46:('symmetry_and_equation_2_prime',[149,149]),47:('symmetry_and_equation_2_prime',[150,153]),49:('lower_correction_group',[159,159]),50:('lower_correction_group',[164,167]),51:('lower_correction_group',[168,168]),52:('lower_correction_group',[170,170]),54:('lower_slanted_note',[178,182]),55:('lower_slanted_note',[186,193]),56:('lower_slanted_note',[196,200]),57:('lower_display_and_car_formula',[203,205]),60:('final_insertion_group',[219,219]),63:('final_cancelled_group_and_ending',[229,229]),65:('final_cancelled_group_and_ending',[241,241])}
for n,(block,rng) in iranges.items():iput(n,[ref(block,ranges=rng)])
itokens={2:('page_and_heading',r'\deleted{\unsure{I|V}}'),5:('opening_prose',r'\deleted{\unsure{\Sigma|S}}E_i'),6:('opening_guide',r'\inserted{\unsure{fermés|fermées}}'),9:('opening_tail_and_upper_note',r'\nearrow'),11:('condition_a',r'\deleted{\Sigma}E_i'),13:('upper_right_nb',r'\uline{NB}'),15:('condition_b_and_main_nb',r'\deleted{\Sigma}E_j'),16:('condition_b_and_main_nb',r'X\setminus\deleted{\Sigma}E_i.'),18:('condition_b_and_main_nb',r'\deleted{\Sigma}E_i$'),21:('case_heading',r'\deleted{\unsure{(\mathrm{de})}}'),22:('case_heading',r'\deleted{\unsure{\leq|=}}='),29:('main_drawing',r'\deleted{\unsure{+}}\unsure{-}'),32:('equation_1_and_ce_qui','ce qui'),33:('equation_1_and_ce_qui',r'\deleted{résulte de}'),37:('cancelled_inclusions_and_equivalence',r'\text{\unsure{équivaut|èquivaut} à}'),38:('cancelled_inclusions_and_equivalence',r'\deleted{\Sigma_2^-\supset\Sigma_1^+}'),39:('cancelled_inclusions_and_equivalence',r'\Sigma_1^+\subset\Sigma_2^-\cup E_2,\quad\text{et}'),42:('si_on_avait_through_equation_2',r'\deleted{Si on avait}'),43:('si_on_avait_through_equation_2',r'comme $\Sigma_1^+\cap E_2=\varnothing$, cela équivaut aussi à'),53:('lower_correction_group',r'\uline{vois}.'),62:('final_un_and_connector',r'\inserted{un}'),66:('upper_right_nb',r'\overset{\unsure{\rule{.8em}{.35pt}}}{\Sigma}_i^+')}
for n,args in itokens.items():iput(n,[ref(*args)])
ipaths={7:('opening_guide',[0]),23:('case_heading',[0,1]),28:('main_drawing',[13,14]),35:('cancelled_inclusions_and_equivalence',[0]),41:('car_si',[0,1]),59:('lower_display_and_car_formula',[0]),61:('final_insertion_group',[0]),64:('final_cancelled_group_and_ending',[0,1,2,3])}
for n,(block,ids) in ipaths.items():iput(n,pathrefs(block,ids))
iput(4,[ref('opening_prose'),ref('opening_guide',r'{de $X$}'),ref('opening_tail_and_upper_note',ranges=[22,22])])
iput(48,[ref('lower_correction_group',ranges=[158,158]),ref('lower_correction_group',ranges=[161,161]),ref('lower_correction_group',ranges=[171,171])])
iput(58,[ref('lower_display_and_car_formula'),ref('final_insertion_group',ranges=[218,220]),ref('final_un_and_connector'),ref('final_cancelled_group_and_ending',r'$X$ serait disconnexe),')])
assert all(x.get('root_page_sources') for x in inv.values())
for n in [49,51]:
 for lc in inv[n].get('local_components',[]):lc['root_page_sources']=by[lc['decision_id']]['root_page_sources']
for lc in inv[64].get('local_components',[]):
 lc.update(description='Selected B G07 second upright only; angular first region overlaps the retained C angular path',root_page_sources=by['015-G-REMNANT']['root_page_sources'],selected_command=r'\draw (24,6) -- (26,16);',declared_full_origin=[932,2239])
updates={25:'C DRAW01: nine oval paths, two chords, two left-brace runs and one right brace',27:r'deleted unsure Sigma_1^+|Sigma_2^+',30:'C MARK01: detached spot above drawing exponent',37:'équivaut|èquivaut à',40:'Car si|car si, cancelled',46:'unsure et; symètriquement|symétriquement, à',48:'Comme Sigma_2^- superset E_1, … on unsure a',49:'deleted unsure vois. ouvert',50:'C MARK02 short detached curved stroke',53:'underline under vois, excluding the following point',54:'barred Sigma_1^+ cap E_1 nonempty; i.e. barred Sigma_1^+ neq Sigma_1^+; à sign.ler|à signaler avant',55:'A GUIDE02 short arrow, locally unsure',56:'C GUIDE02 longer curve, locally unsure',60:"inserted unsure l'ouvert|louvert",61:'B GUIDE02 hooked insertion guide',63:'deleted unsure Sigma_1^+ serait|Sigma_1^+ neq emptyset',64:'C CANCEL03 three overstrikes plus selected B G07 upper upright'}
for n,val in updates.items():inv[n]['first_words_or_objects']=val
for n in [30,50,55,56,61,64]:
 if 'component' in inv[n]:inv[n]['source_baseline_component']=inv[n].pop('component')
inv[30]['selected_component']='C.MARK01';inv[50]['selected_component']='C.MARK02';inv[55]['selected_component']='A.GUIDE02';inv[56]['selected_component']='C.GUIDE02';inv[61]['selected_component']='B.GUIDE02';inv[64]['selected_component']='C.CANCEL03 + B.G07 second command'

# Current source markings are resolved from the actual H locus, not inherited guesses.
marked={'D03':r'\uncertain{toute}','D04':r"\uncertain{n'est pas}",'H07':r'\ill{} si','H17':r'\ill{}','D16':r'\ill{}','G10a':r'\ill{}','G10b':r'\ill{}','G10-GROUP':r'\ill{}','S-NOTE-SECOND':r'\ill{}'}
for x in d['decisions']:
 key=x['id'][4:];x['marked_in_H']='yes' if key in marked else 'no';x['H_marking_basis']=marked.get(key,'No uncertainty/ill mark at this actual H locus; deletion, addition, emphasis and drawing apparatus do not supply a yes flag.')
 x['root_evidence_source']={'manifest':'root.main_decisions.md','section':x['root_decision_section'],'heading':x.get('root_decision_heading')}
 # One compact local evidence entry plus an exact section reference; the authoritative note stays once in its file.
 x['evidence']='Root section '+str(x['root_decision_section'])+' ('+x.get('root_decision_heading','')+'): '+x['final']+'.'+(' '+x['confidence_scope'] if x.get('confidence_scope') else '')
 x.pop('root_confidence_pending',None)
 x['count_status']='complete: exact Boolean physical-locus decision; source approval retained by root'
by['015-P09']['final']=r"\inserted{\unsure{l'ouvert|louvert}}"

# Public alternatives follow the selected candidate order; all original reader alternatives stay in provenance.
alts={'D01a':['V'],'D02':['S'],'D03':['toute','tt'],'D05':['-','\\ast'],'D09a':[],'D09b':['='],'D10':['\\Sigma_2^+'],'D11':[],'D12':['èquivaut'],'D13':['car si'],'D14':[],'D15':[],'D16':['à signaler'],'D18':['puis'],'D19':['\\Sigma_1^+\\ne\\varnothing'],'D20':['fermées'],'D21b':['\\Sigma'],'H15':[],'G01':[],'G05':[],'G07':[],'G08':[],'G09':[],'G-NB-RULE':[],'G-SYM-ACCENT':['symétriquement'],'G10-GROUP':[],'P09':['louvert']}
for z in d['doubts']:
 key=z['decision_id'][4:];assert key in alts,key
 z['alternatives']=list(dict.fromkeys(alts[key]));z['root_page_sources']=by[z['decision_id']]['root_page_sources'];z['final_status']='root-selected uncertainty retained'
 for c in z.get('local_components',[]):
  if c.get('id') in by:c['root_page_sources']=by[c['id']]['root_page_sources']
 # Keep visible-shape certainty separate from unresolved interpretation.
 if key in ['G01','G05','G07','G08','G09','G-NB-RULE','G10-GROUP']:
  z['shape_confidence']=by[z['decision_id']]['confidence'];z['interpretation_status']='role/character/hand/origin or attachment remains undetermined as stated in the local components; visible shape confidence does not resolve attribution'
  z['reason']=by[z['decision_id']].get('confidence_scope','')+' Root-selected local uncertainty retained. '+(' Local component positions and individual confidences are listed separately.' if z.get('local_components') else ' Position: '+str(by[z['decision_id']]['full_scan_boxes']))
for a in d['abbreviations']:
 if a['form'].startswith('comp. conn.'):a['form']='comp. conn.'
if not any(a['form']=='sign.ler [?]' for a in d['abbreviations']):d['abbreviations'].append({'form':'sign.ler [?]','expansion':'probablement signaler','source':{'manifest':'C.reading.tex','selection':'root section21'},'qualification':'selected instruction retains à sign.ler|à signaler; expansion occurs only in this table'})
d['notes']="The sheet is headed Version I with underlining. No date or authored page count was identified; archive numeral 14 is retained only as a comment, with its hand undetermined. The opening text gives X and an indexed family, displays conditions (a) and (b), and is accompanied by upper marginal notes. The page proceeds to the two-member case, its labelled oval drawing, and relations (1), (2), and (2'). The lower marginal instruction reads à sign.ler|à signaler avant, with the uncertainty and authorial instruction preserved. The final prose continues through X serait disconnexe), and retains the trailing comma.\n\nThe written upper-right complement X\\Sigma_i, its crowded +|-|star superscript, and automatiquement les remain ink readings. Suggested repairs in C's slips table remain source metadata and were not adopted. No explicit authored uncertainty phrase was identified. The three targeted closure bars were confirmed directly from root crops: current C already supplies all three; H supplies the first lower-note bar and the final-prose bar, and covers the lower-note continuation with one ill placeholder. Those confirmations supply no separate bar-error count. No mathematical proof or computation was performed."
d['workflow_note']='Three fresh independent readers A/B/C, fork_turns=none, no model override, brief v13. Their original report/TeX/audit files and actual start/end times are preserved by fingerprint. Root viewed 26 distinct crops once each: 23 reader crops and 3 own crops, with no failed image deliveries or retries, no root whole-scan or supplied-half view, and no recrop. Root choices01–26 are fully applied. Mechanical record and selected-source assembly used no images, OCR, external research, compiler, renderer, numerical curve-bound calculation or mathematical proof. Declared source-coordinate placement maps are not curve-bound certificates. Main-record approval remains with root.'
d['root_ink_pass']={'distinct_crops':26,'reader_crops':23,'root_crops':3,'failed_deliveries':0,'retries_or_recrops':0,'whole_scan_viewed':False,'halves_viewed':False,'decision_log':'checks/scan015_main_decisions.md','complete':True}
d['historical_source_snapshots']=[{'manifest':'scan015_source_map.json','status':'initial pre-adjudication source map; its pending S/status prose is historical, superseded by current explicit S decisions'}, {'manifest':'scan015_witness_attention.md','status':'initial pre-adjudication attention list'}, {'manifest':'scan015_source_geometry_attention.md','status':'preliminary A-source attention note; final A file fingerprint and selected-source manifest supersede its preliminary-source hash'}]
d['source_attachment_map']='checks/scan015_final_source_map.json';d['root_selected_source']='checks/scan015_final_draft.tex'
d['source_attachment_status']='all 96 decisions, all 66 inventory elements and every remaining-doubt entry attached to exact selected-source spans/group anchors'
d['root_actions_pending']=['Root review of the completed record, public tables/notes and independent source-completeness audit; root alone approves/writes the main record and commits.']
d['pending_root_decision_ids']=[];d['main_adjudicated']=False
primary=[x for row in d['actual_C_doubt_map'] for x in row['primary_local_decision_ids']]
resolved=sum(by[k]['C_doubt_status'].startswith('resolved') for k in primary);retained=sum(by[k]['C_doubt_status'].startswith('retained') for k in primary)
assert (len(primary),resolved,retained)==(24,7,17)
d['C_doubt_resolution_counts']={'actual_rows':21,'local_loci':24,'resolved_local':7,'retained_local':17,'mixed_rows':[1,21],'retained_compound_row':9}
d['counts']={w:sum(bool(x['diff_'+w]) for x in d['decisions']) for w in ['C','H']}
d['counts']['by_witness_confidence']={w:dict(collections.Counter(x['confidence'] for x in d['decisions'] if x['diff_'+w])) for w in ['C','H']};d['counts']['remaining_doubt_loci']=len(d['doubts']);d['counts']['inventory_elements']=len(d['inventory'])
d.pop('provisional_counts',None)
d['source_counts']['provisional_remaining_doubt_loci']=len(d['doubts'])
d['mechanical_verification'].update(all_final_decision_spans_attached=True,all_inventory_spans_attached=True,all_remaining_doubt_spans_attached=True,all_ink_choices_complete=True,actual_C_local_statuses='7 resolved / 17 retained',exact_count_booleans=d['counts'])
assert all(x['main_approved'] and x['confidence'] in ['high','medium','low'] and x['marked_in_H'] in ['yes','no'] for x in d['decisions'])
assert not any(x['diff_H'] for x in d['decisions'] if x.get('H_count_parent'))
assert not any(x['diff_C'] for x in d['decisions'] if x.get('C_count_parent'))
assert all((ROOT/r['path']).exists() and 0<=r['char_start']<r['char_end']<=len(t) for x in d['decisions'] for r in x['root_page_sources'])
fp=CHECK/'scan015_reader_fingerprints.json';f=json.loads(fp.read_text())
for key,path in [('root.final_draft.tex',draft_path),('root.final_source_map.json',mapping_path),('root.main_decisions.md',CHECK/'scan015_main_decisions.md')]:f['files'][key]={'path':str(path.relative_to(BASE)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size}
f['historical_snapshot_policy']='The three initial source/attention files remain unchanged; their pending prose is explicitly historical in the completed draft.'
fp.write_text(json.dumps(f,ensure_ascii=False,indent=2)+'\n');p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
u=CHECK/'scan015_union.md';s=u.read_text();s=s.replace('# Scan015 — compact provisional union','# Scan015 — source union and completed root choices')
s=s.replace('Source-only assembly; no manuscript image inspected and no final ink choice made.','Mechanical source union; the clerk inspected no manuscript images. Root ink choices01–26 are complete and applied; exact selected-source attachments are complete. Main-record approval remains with root.')
s=re.sub(r'## Pending root actions\n.*?(?=\n## |\Z)','## Root approval remaining\n\nAll local ink choices, count assignments and confidences are complete. Every decision, inventory item and retained doubt has exact selected-source spans. Root review of the complete record and independent source audit remains before root writes the main record. Initial attention/source-map snapshots retain historical pre-adjudication wording.\n',s,flags=re.S)
s=s.replace('Final-source attachment is still pending root.','Every inventory element is now attached to exact selected-source spans; root main-record approval remains.')
s=s.replace('## Source-level disagreements that require root attention','## Preserved source-level disagreements')
s=s.replace('need their own ink choices.','have their own applied root choices below.')
s=s.replace('Other union rows remain pending; the full record preserves each independent return.','All original and additional union rows now have root choices; the full record preserves each independent return.')
s+='\n## Completed attachment and count summary\n\nAll 181 returned difference rows, 66 returned doubt rows and 217 inventory source rows remain mapped. The final union has 96 local/parent audit decisions and 66 deduplicated inventory elements. Original C doubt identities remain 21 rows / 24 local loci, with 7 resolved and 17 retained. Authoritative Boolean totals: C '+str(d['counts']['C'])+', H '+str(d['counts']['H'])+'; '+str(len(d['doubts']))+' remaining doubt clusters with local components retained. All 96 decisions, 66 inventory elements and remaining doubts cite exact spans in checks/scan015_final_draft.tex through the source manifest. main_adjudicated remains false for root approval.\n'
u.write_text(s)
print(json.dumps({'attached_decisions':len(d['decisions']),'attached_inventory':len(d['inventory']),'doubts':len(d['doubts']),'counts':d['counts'],'C_doubts':[resolved,retained],'main_adjudicated':False},ensure_ascii=False))
