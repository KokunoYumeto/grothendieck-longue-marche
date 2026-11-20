"""Root scan014 consolidation after ten completed local crop inspections."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import hashlib,json,re

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out'
R={role:json.loads((OUT/'readers/014'/role/'report.json').read_text()) for role in 'ABC'}
F=json.loads((OUT/'checks/scan014_reader_fingerprints.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for role in 'ABC':
    for name,value in F[role].items():assert sha(OUT/'readers/014'/role/name)==value
    assert all(R[role][k] for k in ['full_image_viewed','halves_viewed','complete_visual_read'])
    assert not R[role]['check_events']
audit=json.loads((OUT/'checks/scan014_root_crop_audit.json').read_text())
assert audit['successful_distinct_crops']==10 and not audit['root_full_or_half_viewed']
for x in audit['images']:
    assert x['viewed'] and x['successful_display_count']==1 and sha(OUT/x['path'])==x['sha256']
assert (OUT/'checks/scan014_source_audit.md').exists()

A=(OUT/'readers/014/A/reading.tex').read_text()
page=A.replace('% Reader A: complete proposed page; source origin is full-scan top left.',
               '% Consolidated scan014; source origin is full-scan top left.',1)
assert page!=A
page_name='J81-02_81_scan014.tex'
page_ref='pages/'+page_name
page_sha=hashlib.sha256(page.encode()).hexdigest()
def attachment(literal):
    assert page.count(literal)==1,literal
    start=page.index(literal);end=start+len(literal)
    return dict(path=page_ref,sha256=page_sha,char_start=start,char_end=end,
                line_start=page[:start].count('\n')+1,
                line_end=page[:end].count('\n')+1,
                body_sha256=hashlib.sha256(literal.encode()).hexdigest())
def ref(role,kind,i):
    return dict(path=f'readers/014/{role}/report.json',sha256=F[role]['report.json'],
                pointer=f'/{kind}/{i}')
components={x['id']:x for x in R['A']['notes']['final_source_component_map']}
assert len(components)==12
assert sum(x['path_command_count'] for x in components.values())==13
for x in components.values():assert page.count(x['source_command'])==1
nodes={}
for key in ['A014T1','A014I1','A014T2','A014T3']:
    line=next(l for l in page.splitlines() if '('+key+')' in l)
    nodes[key]=dict(literal=line,attachment=attachment(line))
assert [re.search(r' at \([^)]*\) \{(.*)\};$',nodes[k]['literal']).group(1)
        for k in ['A014T1','A014I1','A014T2','A014T3']]==[
        r'\unsure{décompositions}',r'\inserted{et découpages}',r'$n$-aires',
        r"d'\unsure{espaces} topologiques"]
for role in 'BC':
    assert (OUT/'readers/014'/role/'reading.tex').read_text()==(BASE/'packets/014/C.tex').read_text()

root_evidence={
 'GUIDE01':'The continuous line bends downward into the gap before n, rises into a long curved run beneath the insertion and turns upward at its right end. Its exact A path is retained; the inserted words, state and attachment are unchanged.',
 'G01':'A small isolated oblique filled patch lies above/right of the insertion at [1540,54,1544,58]. The contour is qualified, with no supplied character or punctuation attachment.',
 'G02':'A small oblique pale spot lies below n at [1313,164,1318,169]; its outline is retained as a qualified graphic.',
 'G03':"A small detached dark spot lies left of d' at [943,224,947,228]; its compact rounded outline remains locally qualified.",
 'G04':"A pale small point is visible beside the d stem, before the raised apostrophe, at [985,215,989,218]. Its soft boundary remains a low-confidence qualified oval candidate.",
 'G05':'The compact dark core has a nearly upright oval outline and soft gray edge at [1427,728,1430,733]. A\'s exact qualified path is retained.',
 'G06':'A compact center and oval outline rise to the right at [1075,913,1079,917]. A\'s exact qualified path is retained.',
 'G07':'The short dark core at [241,1386,247,1390] is wider than tall, with a slightly rising right end. The exact qualified oval/dash path is retained.',
 'G08':'Two separate dark spots lie within [1570,1793,1580,1805]: the upper-right one has an angular lower-left edge and the lower-left one is rounder. Both A fill commands remain, without a connecting line; one physical pair count.',
 'G09':'After autocontrast, a darker central patch has a soft upright oval outline at [233,1890,236,1896]. Original faint boundary and tonality remain uncertain; retain A\'s black!25 candidate with low shape confidence.',
 'G10':'A small flattened oval with soft edge lies at [1707,2278,1712,2281]. The exact qualified A path remains.',
 'G11':'The pale oblique spot has an upper core and a short lower-right taper within [736,2425,742,2433]. The taper is preserved in A\'s exact path, with low confidence in its faint boundary.'}
observations_B={'G02':1,'G03':0}
observations_C={'G01':0,'G02':1,'G03':2,'G08':3}
decisions=[]
for i,x in enumerate(R['A']['differences']):
    d=dict(x)
    d['source_reader_id']=x['id'];d['id']=f'014-D{i+1:02d}'
    d['final']=x['reading'];d['crop']='readers/014/A/'+x['readers_crop']
    d['reader_provenance']={'A':[ref('A','differences',i)],'B':[],'C':[]}
    d['readers']={'A':x['reading'],'B':'No individual graphical proposal or path in B\'s return.',
                  'C':'No individual graphical proposal or path in C-reader\'s return.'}
    if i<2:
        for role in 'BC':
            d['readers'][role]=R[role]['differences'][i]['reading']
            d['reader_provenance'][role]=[ref(role,'differences',i)]
        d['root_page_sources']=[nodes['A014T1' if i==0 else 'A014T3']['attachment']]
        d['source_C_doubt_row']=i+1
        d['evidence'] += ' Root independently inspected the same locus and retains the source doubt, medium confidence.'
    else:
        key=x['component_ids'][0]
        d['evidence']=root_evidence[key]
        d['root_page_sources']=[attachment(components[key]['source_command'])]
        d['selected_component']=components[key]
        if key=='GUIDE01':
            d['readers']['B']=r'\inserted{et découpages}; guide described as continuous and hooked, represented conventionally without its own path.'
            d['readers']['C']=r'\inserted{et découpages}; long curved lead-in described, no graphical variant.'
            d['reader_provenance']['B']=[dict(path='readers/014/B/report.json',sha256=F['B']['report.json'],pointer='/notes/source_component_map/1')]
            d['reader_provenance']['C']=[dict(path='readers/014/C/report.json',sha256=F['C']['report.json'],pointer='/notes/source_component_map/insertion')]
        else:
            d['evidence']+=' Hand, role and surface origin remain unresolved; no character is supplied.'
            for role,obsmap,field in [('B',observations_B,'small_surface_observations'),('C',observations_C,'surface_observations')]:
                if key in obsmap:
                    j=obsmap[key];obs=R[role]['notes'][field][j]
                    d['readers'][role]=obs.get('description',obs.get('observation'))+' No graphical path in proposed source.'
                    d['reader_provenance'][role]=[dict(path=f'readers/014/{role}/report.json',sha256=F[role]['report.json'],pointer=f'/notes/{field}/{j}')]
    d.update(main_approved=True,marked_in_H='not applicable',mathematical_consequence=None,
             root_decision_log='checks/scan014_main_decisions.md',log_decision=True)
    decisions.append(d)
decisions.append(dict(id='014-D15',location='Lower-left archive numeral and inventory hand attribution',
    C='Archive comment13; no archive inventory entry or hand attribution.',H=None,
    final='Archive comment13 retained; inventory hand undetermined.',
    readers={'A':'Archive13; another unnamed hand.','B':'Archive13; another unnamed hand.','C':'Archive13; undetermined hand.'},
    reader_provenance={'A':[ref('A','inventory',14)],'B':[ref('B','inventory',2)],'C':[ref('C','inventory',2)]},
    evidence='The crop shows an ascending entry and upright1, followed by the upper/lower curves of3. Numeral13 is clear. Writer identity remains unestablished from this local evidence.',
    crop='crops/014/01_archive13.png',confidence='high',kind='other',diff_C=False,diff_H=False,
    C_doubt_status=None,marked_in_H='not applicable',log_decision=True,
    root_page_sources=[attachment('% archive sheet number: 13')]))

inventory=[]
for i,item0 in enumerate(R['A']['inventory']):
    item=dict(item0);item['source_inventory_id']=item['element'];item['element']=f'014-I{i+1:02d}'
    item['source_inventory']=[ref('A','inventory',i)]
    key=(item.get('components') or [None])[0]
    if key:
        item['root_page_sources']=[attachment(components[key]['source_command'])]
        item['observed_locus_bbox']=components[key]['full_scan_bbox']
        item['bounds_note']='Observed locus region; exact path geometry is preserved in selected source commands.'
    elif item0['element']=='014.02':
        item['root_page_sources']=[nodes['A014I1']['attachment']]
        item['source_inventory'] += [ref('B','inventory',0),ref('C','inventory',0),
          dict(path='packets/014/C_inventory.json',pointer='/1')]
    elif item0['element']=='014.01a':
        item['root_page_sources']=[nodes[k]['attachment'] for k in ['A014T1','A014T2']]
        item['source_inventory'] += [dict(**ref('B','inventory',1),scope='first title line'),
          dict(**ref('C','inventory',1),scope='first title line'),
          dict(path='packets/014/C_inventory.json',pointer='/0',scope='first title line')]
    elif item0['element']=='014.01b':
        item['root_page_sources']=[nodes['A014T3']['attachment']]
        item['source_inventory'] += [dict(**ref('B','inventory',1),scope='second title line'),
          dict(**ref('C','inventory',1),scope='second title line'),
          dict(path='packets/014/C_inventory.json',pointer='/0',scope='second title line')]
    else:
        assert item0['element']=='014.A.archive'
        item['hand']='undetermined hand'
        item['root_page_sources']=[attachment('% archive sheet number: 13')]
        item['source_inventory'] += [ref('B','inventory',2),ref('C','inventory',2)]
    assert item['transcribed']=='yes' and item['root_page_sources']
    inventory.append(item)

doubts=[]
for i,x in enumerate(R['A']['doubts']):
    q=dict(x);q['crop']='readers/014/A/'+x['crop']
    decision_index=i if i<2 else i+1
    q['decision_id']=decisions[decision_index]['id']
    q['root_page_sources']=decisions[decision_index]['root_page_sources']
    q['reader_provenance']=[ref('A','doubts',i)]
    if i<2:q['reader_provenance'] += [ref('B','doubts',i),ref('C','doubts',i)]
    doubts.append(q)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
r=dict(scan=14,folder='J81-02',their_page=13,hua_has='nothing',filename=page_name,
    brief_version='v12',main_adjudicated=True,main_approved_utc=now,
    root_page_text_exact=page,decisions=decisions,doubts=doubts,inventory=inventory,
    abbreviations=[],check_events=[dict(
      statement_id='SP40-014-SOURCE-GEOMETRY',date='2026-11-20',
      who='GPT-6 Astra Pro / inherited effort, not separately exposed / qa014_source',
      type='computation or formal certificate',
      outcome=('Finite source-coordinate computation. A standard-library Python script evaluated cubic '
       'endpoints and analytic derivative roots using floating-point arithmetic, with a 1e-12 '
       'degeneracy tolerance; seven observed-locus boxes have the small excesses tabulated in '
       'checks/scan014_source_audit.md, while all selected fill endpoints/control points fit '
       'their fixed local rectangles. GUIDE01 centreline bounds approximately '
       '[1273.244151,81,1497,162]. Separate exact arithmetic illustration: G04 y-controls '
       '(3,1,1,3) at t=1/2 give y=3/2; adding origin213 gives214.5, half a coordinate '
       'unit above the reported locus215. Recorded date only; no clock captured. '
       'Scope is the finite supplied source commands and their declared frames; '
       'no ink inspection, word selection or TeX rendering was performed in this check.'))],reader_fingerprints=F,
    root_crop_audit='checks/scan014_root_crop_audit.json',root_source_audit='checks/scan014_source_audit.md',
    root_decision_log='checks/scan014_main_decisions.md',
    actual_C_doubt_map=[dict(source_row=i+1,decision_id=f'014-D{i+1:02d}',status='retained') for i in range(2)],
    source_counts=dict(differences=18,doubts=17,reader_inventory=22,C_inventory=2),
    counts=dict(C=12,H=0,decision_loci=15,remaining_doubt_loci=13,inventory_elements=16,check_events=1),
    notes=("A cover headed décompositions, with et découpages inserted before n-aires, "
      "followed by d'espaces topologiques. The first main word and espaces retain the "
      "two original editorial doubts because their compressed internal joins remain "
      "unresolved. No authorial question, date or page count is read. Archive13 at "
      "the lower-left foot remains a comment, with undetermined hand. The continuous "
      "insertion guide is reproduced as drawn, including its left descending bend "
      "and upturned right endpoint. Eleven small qualified trace clusters comprise "
      "twelve visible filled components; their roles, hands and surface origins "
      "remain undetermined. No word or punctuation attachment is supplied for them. "
      "The title contains no mathematical statement checked, used or refuted in "
      "this reading. A separate finite source-coordinate check is logged in CHECK_EVENTS: "
      "floating-point cubic extrema were compared with the recorded locus boxes, and "
      "G04's y-controls (3,1,1,3) give3/2 at t=1/2, hence full y=214.5 after "
      "adding origin213. This explains its half-unit excess above the recorded locus215; "
      "the selected source paths remain unchanged. H supplies no text. "
      "Witness S SA01-K81-06 covers scans15–22 and supplies no reading for this sheet."),
    workflow_note=("Three fresh independent readers viewed the whole and both halves "
      "once. A made9 crops; B3; C3. Root inspected9 existing A crops and1 new archive "
      "crop, ten distinct successful displays, without a whole/half view or recrop. "
      "All18 source differences,17 doubts,22 reader inventories and2 C inventory "
      "entries are mapped. A's first UTC record followed initial packet reading "
      "and preceded images, as disclosed. B/C recorded several surface observations "
      "without graphic paths; root selected the locally inspected A candidates. "
      "The common text bodies and both source doubts are unchanged. A source-only "
      "auditor checked13 path commands, fixed origins, four title nodes and inventory "
      "coverage. Observed locus boxes are approximate and are not advertised as "
      "exact Bézier bounds. One finite source-coordinate calculation is logged at its "
      "actual numerical scope. Structural TeX checks only; no compiler, renderer, OCR "
      "or external research. Briefv13 records the representation lesson."))
assert len(decisions)==15 and sum(d['diff_C'] for d in decisions)==12
assert len(doubts)==13 and len(inventory)==16
destination=OUT/page_ref;destination.write_text(page)
vp=OUT/'scripts/validate.py';ns={'__file__':str(vp)}
exec(vp.read_text().split('records=')[0],ns);validation=ns['check_tex'](destination)
assert not validation['errors'],validation
(OUT/'records/scan014.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
mapping=dict(scan=14,page=page_ref,page_sha256=page_sha,selected_source='readers/014/A/reading.tex',source_body_map=components,
             node_map=nodes,source_frame=dict(x_cm=0.006,y_cm=-0.006),
             original_text_qualifications_retained=2,selected_path_commands=13,
             trace_groups=11,trace_components=12,
             source_coverage='All source rows mapped through decisions, doubts, inventory and source audit.')
(OUT/'checks/scan014_final_source_map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
p=OUT/'checks/scan014_source_map.json';s=json.loads(p.read_text());s['status']='Root approved; both original C doubts retained.';p.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
approval=dict(scan=14,approved_utc=now,sha256=page_sha,counts=r['counts'],
              C_confidence=dict(Counter(d['confidence'] for d in decisions if d['diff_C'])),
              structural_result=validation,root_crops=10)
(OUT/'checks/scan014_root_approval.json').write_text(json.dumps(approval,ensure_ascii=False,indent=2)+'\n')
with (OUT/'progress.log').open('a') as f:f.write('scan014 root approval '+now+'; ten crops; title qualifications retained, guide and eleven trace groups included; structural check passed\n')
print(json.dumps(approval,ensure_ascii=False))
