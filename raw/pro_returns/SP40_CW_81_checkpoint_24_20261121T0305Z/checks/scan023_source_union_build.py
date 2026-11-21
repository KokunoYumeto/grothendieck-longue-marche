"""All-reader source-locus union. No selected transcription or physical counts."""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path('/workspace/scratch/94548b74fbe0')
OUT=ROOT/'out/checks'
coverage={r:json.loads((OUT/f'scan023_{r}_source_coverage.json').read_text()) for r in 'ABC'}
tex={r:(ROOT/f'out/readers/023/{r}/reading.tex').read_text() for r in 'ABC'}
sha={r:hashlib.sha256(tex[r].encode('utf-8')).hexdigest() for r in 'ABC'}
groups={r:{g['id']:g for g in coverage[r]['graphical_groups']} for r in 'ABC'}
named={r:coverage[r]['named_complete_source_spans'] for r in 'ABC'}
named['B']['lemma_correction']=groups['B']['B023-G07']['tex_ref']
witness_path='out/checks/scan023_witness_source_coverage.json'
witness=json.loads((ROOT/witness_path).read_text())
cat_path='out/checks/scan023_C_doubt_catalog.json'
catalog=json.loads((ROOT/cat_path).read_text())

def source(r,s,e):
    t=tex[r]
    return dict(path=f'out/readers/023/{r}/reading.tex',sha256_utf8=sha[r],
                char_start_zero_based=s,char_end_exclusive=e,
                utf8_byte_start=len(t[:s].encode('utf-8')),utf8_byte_end_exclusive=len(t[:e].encode('utf-8')),
                line_start_one_based=t.count('\n',0,s)+1,line_end_one_based=t.count('\n',0,max(s,e-1))+1,literal=t[s:e])

def exact(r,literal,within=None):
    lo,hi=(0,len(tex[r])) if within is None else (within['char_start_zero_based'],within['char_end_exclusive'])
    at=[m.start()+lo for m in re.finditer(re.escape(literal),tex[r][lo:hi])]
    assert len(at)==1,(r,literal,at)
    return source(r,at[0],at[0]+len(literal))

def spanning(r,first,last):
    a=named[r][first];b=named[r][last]
    return source(r,a['char_start_zero_based'],b['char_end_exclusive'])

def gr(r,g):return groups[r][g]['tex_ref']
def n(r,name):return named[r][name]
def alln(name):return {r:[n(r,name)] for r in 'ABC'}
def ex3(a,b=None,c=None):
    return {'A':[exact('A',a)],'B':[exact('B',a if b is None else b)],'C':[exact('C',a if c is None else c)]}
def gg(a,b,c):return {'A':[gr('A',a)],'B':[gr('B',b)],'C':[gr('C',c)]}

specs=[]
def add(key,label,diff_nums,refs,scope,notation=None,absence=None,note='',Hmarkers=None):
    specs.append(dict(key=key,label=label,diff_nums=dict(zip('ABC',diff_nums)),refs=refs,witness_scope=scope,
                      notation=notation or {},absence=absence or {},note=note,Hmarkers=Hmarkers or []))

add('opening_prouvons','Opening prose and prouvons',([], [1], []),
    ex3("Soit maintenant $\\beta\\in I\\setminus K$, prouvons que l'on",
        "Soit maintenant $\\beta\\in I\\setminus K$, \\unsure{prouvons} que l'on",
        "Soit maintenant $\\beta\\in I\\setminus K$, prouvons que l'on"),'opening',note='A/C source choices are supplied by their complete actual TeX excerpts.')
add('opening_a','Opening reduced a or mark',([1],[2],[]),
    {'A':[gr('A','A023-G01')],'B':[gr('B','B023-G01')],'C':[exact('C',"que l'on a $\\overline V")]},'opening',notation={'C':[0],'B':['N16']},note='B D02 also reports its separately inspected recurrence; that whole raw record remains intact.')
add('opening_target','Complete opening barred-V target',([],[],[]),alln('opening'),'opening',notation={'A':[11],'B':['N14'],'C':[1]})
add('opening_correction','ne, cancelled contient and inserted rencontre',([2],[3],[1]),
    ex3('V$ ne \\deleted{contient} \\inserted{rencontre}'),'opening')
add('upper_left_trace','Detached trace left of first formula',([3],[],[2]),
    {'A':[gr('A','A023-M01')],'B':[n('B','upper_paragraph')],'C':[gr('C','C023-G01')]},'opening',
    absence={'B':'The complete attached B upper-paragraph source has no dedicated left-margin trace group at this location. This is a source-encoding observation within that span.'})
add('first_union','First indexed union, complete operator states and limit',([4],[4],[3]),gg('A023-G02','B023-G02','C023-G02'),'opening',notation={'A':[12]})
add('sigma01','First hatted Sigma, predecessor/retrace, roof, index and plus',([5],[5],[4]),gg('A023-S01','B023-S01','C023-G03'),'opening',notation={'A':['S01'],'B':['S01'],'C':[3]})
add('cancelled_donc_si','Cancelled donc si and endpoint covered by H ill marker',([6],[6],[5]),
    ex3('\\deleted{\\unsure{donc si}}'),'opening',Hmarkers=['H023-ILL01'],
    note='The exact H marker is the extra ill placeholder after si. Raw A/B/C marker flags and full row scopes are preserved; no final local flag or count is selected.')
add('on_a','Whole on a and the second reduced a',([7],[2],[]),
    {'A':[gr('A','A023-G03')],'B':[n('B','continued_assertion')],'C':[gr('C','C023-G04')]},'opening',notation={'B':['N16'],'C':[0]},
    note='A qualifies the complete on a phrase. B preserves the reduced-a point alternative at the recurrence. C supplies actual on a text in its own word-bearing group.')
add('ochre_mark','Detached ochre/brown mark above on a',([8],[7],[6]),gg('A023-M02','B023-M01','C023-G04'),'opening',note='C G04 owns on a and the mark; adjacent words and all nested declarations remain in its exact source.')
add('display_E','Displayed E_beta and its lower-foot representation',([],[8],[]),
    {'A':[n('A','first_display')],'B':[gr('B','B023-G05'),n('B','first_display')],'C':[n('C','first_display')]},'display')
add('sigma02','First displayed Sigma and complete parenthetical',([],[],[]),alln('first_display'),'display',notation={'A':['S02'],'B':['S02'],'C':[4]})
add('margin_capital','Complete slanted note and initial capital',([9],[9],[7]),alln('margin'),'margin')
add('margin_cancelled_item','Cancelled unreadable compact marginal item',([10],[10],[8]),ex3('\\deleted{\\illegible{1}}'),'margin')
add('margin_IJ','Marginal parenthetical I/J',([11],[11],[9]),alln('margin'),'margin')
add('ce_qui','Main onset ce qui or qui and attachment scope',([12],[12],[10]),
    ex3('\\unsure{qui|ce qui}','\\unsure{ce|} qui','ce qui \\unsure{prouvera}'),'upper',
    note='Each reader retains its own candidate order and whole-word or empty-alternative scope.')
add('prouvera','Verb before l’assertion',([13],[13],[11]),ex3('\\unsure{prouvera|prouve}',None,'\\unsure{prouvera}'),'upper')
add('assertion_point','Point below-right of l’assertion',([14],[],[12]),
    {'A':[gr('A','A023-G04')],'B':[n('B','upper_argument')],'C':[gr('C','C023-G05')]},'upper',
    absence={'B':'The attached complete B upper-argument span has l’assertion in ordinary text and no dedicated lower point group at this locus.'})
add('sigma03','Upper E_beta inclusion and its Sigma',([],[],[]),alln('upper_argument'),'upper',notation={'A':['S03'],'B':['S03'],'C':[5]})
add('revient','Cela revient',([15],[14],[13]),ex3('Cela revient \\unsure{au}','Cela revient au','Cela revient \\unsure{au}'),'upper')
add('au','Last word before Lemme',([16],[15],[14]),ex3('\\unsure{au}','Cela revient au','\\unsure{au}'),'upper')
add('lemma_heading','Lemme heading and complete introduction',([],[],[]),alln('lemma_intro'),'lemma_intro')
add('cancelled_tel_que_les','Cancelled tel que les',([],[],[]),ex3('\\deleted{tel que les}'),'lemma_intro')
add('cancelled_et','Cancelled et before live des',([17],[16],[15]),ex3('\\deleted{et}'),'lemma_intro')
add('sigma04','Lemma family Sigma, full local head/bridge roles',([],[],[16]),
    {'A':[exact('A','des $\\Sigma_\\alpha^+$')],'B':[exact('B','des $\\Sigma_\\alpha^+$')],'C':[gr('C','C023-G06')]},'lemma_intro',notation={'A':['S04'],'B':['S04'],'C':[6]},
    note='C prints its first recurring role qualification at S04; A and B describe their own local connection in notation and use their own ordinary source glyphs.')
add('tels','Lemma tels que',([18],[17],[17]),ex3('\\unsure{tels} que','tels que','\\unsure{tels} que'),'lemma_intro')
add('lemma_left_point','Isolated left-margin point beside lemma',([],[36],[]),
    {'A':[spanning('A','lemma_intro','lemma_condition')],'B':[gr('B','B023-M02')],'C':[spanning('C','lemma_intro','lemma_condition')]},'lemma_intro',
    absence={'A':'The complete attached A lemma-introduction/condition span contains no dedicated isolated left-margin point group.','C':'The complete attached C lemma-introduction/condition span contains no dedicated isolated left-margin point group.'})
add('first_relation','First alpha/beta relation and whole cancellation/comma states',([19],[18],[18]),gg('A023-G05','B023-G06','C023-G07'),'lemma_condition')
add('repeated_relation','Repeated alpha-ne-beta, implication and equation endpoint',([],[],[]),alln('lemma_condition'),'lemma_condition',notation={'A':[13],'B':['N15']})
add('sigma05','First intersection Sigma, detached return and shared alpha',([20],[19],[19]),gg('A023-S05','B023-S05','C023-G08'),'lemma_condition',notation={'A':['S05'],'B':['S05'],'C':[7]})
add('sigma06','Second intersection Sigma, local head role, beta and raised sign',([21],[20],[20]),gg('A023-S06','B023-S06','C023-G09'),'lemma_condition',notation={'A':['S06'],'B':['S06'],'C':[8]},
    note='A retains a pale-break head-role question. B has joined-head source plus complete plus/top alternatives. C has its own joined-head/plus source with empty alternatives. None is imported into another reader.')
add('lemma_antecedent','Complete lemma antecedent prose and union',([],[],[]),alln('lemma_hypothesis'),'lemma_conclusion',notation={'C':[2]})
add('sigma07','Antecedent Sigma, local head role and alpha-point attachment',([22],[21],[21]),gg('A023-S07','B023-S07','C023-G10'),'lemma_conclusion',notation={'A':['S07'],'B':['S07'],'C':[9]},
    note='C retains an additional separate alpha-point attachment question and trace-hand scope. A/B complete own sources remain attached without borrowing that candidate.')
add('cancelled_conclusion','Complete cancelled E_i est contenu/contenue',([23],[22],[22]),alln('lemma_correction'),'lemma_conclusion')
add('cancelled_clause_tail','Tail of cancelled clause, compared with H dans un',([24],[22],[22]),alln('lemma_correction'),'lemma_conclusion',
    note='B D22 and C D22 have compound report scope. Their original rows remain intact; this source cross-reference supplies no duplicate physical count.')
add('raised_insertion','Complete raised existential and que state',([26],[22],[23]),alln('lemma_correction'),'lemma_conclusion',
    note='C retains four complete participle/raised-que states; A/B have their own live inserted-que source. All invisible state annotations and actual cancellation paths remain attached.')
add('raised_comma_gap','Gap after K in raised existential',([25],[23],[24]),alln('lemma_correction'),'lemma_conclusion')
add('lemma_live_endpoint','Complete live final lemma inclusion and full stop',([],[],[]),alln('lemma_endpoint'),'lemma_conclusion')
add('sigma08','Final lemma Sigma, local detached-head role',([27],[24],[25]),gg('A023-S08','B023-S08','C023-G12'),'lemma_conclusion',notation={'A':['S08'],'B':['S08'],'C':[10]})
add('cancelled_signifie_que','Cela and cancelled signifie que',([],[],[]),ex3('Cela \\deleted{signifie que}'),'unfinished')
add('unfinished_verb','Unfinished verb and complete two-word alternatives',([28],[25],[26]),
    ex3('\\unsure{precise|précise|provient|precise le|précise le}',None,'\\unsure{précise|precise|provient|précise le|precise le}'),'unfinished',Hmarkers=['H023-UNC01'],
    note='All five complete candidates, candidate order and accents remain source-specific. The compound le stays within original C row R09.')
add('unfinished_final_word','Following du/des/sens group',([29],[26],[27]),
    {'A':[n('A','unfinished')],'B':[n('B','unfinished')],'C':[gr('C','C023-G13')]},'unfinished',Hmarkers=['H023-ILL02'])
add('far_right_points','Detached two-point group by unfinished line',([30],[27],[28]),gg('A023-M04','B023-M03','C023-G13'),'unfinished')
add('corollary_left_mark','Detached pale oblique left of Corollaire',([],[37],[]),
    {'A':[spanning('A','unfinished','corollary_heading')],'B':[gr('B','B023-M04')],'C':[spanning('C','unfinished','corollary_heading')]},'corollary_heading',
    absence={'A':'The complete attached A unfinished-line/corollary-heading span has no dedicated detached pale oblique group left of Corollaire.','C':'The complete attached C unfinished-line/corollary-heading span has no dedicated detached pale oblique group left of Corollaire.'})
add('corollary_heading','Corollaire heading and full lead',([],[],[]),alln('corollary_heading'),'corollary_heading')
add('hyp_abbreviation','Written hyp. abbreviation',([],[],[]),
    ex3('Avec les hyp. \\unsure{préc.} sur','Avec les hyp. préc. sur','Avec les hyp. préc. sur'),'corollary_heading',notation={'A':[16],'B':['N13']})
add('prec_abbreviation','Abbreviated préc. and local qualification',([31],[28],[29]),
    ex3('hyp. \\unsure{préc.} sur','hyp. préc. sur','hyp. préc. sur'),'corollary_heading',notation={'C':[15]})
add('sigma09','Family Sigma, i-like hook/dot, head role and adjoining delimiter',([32],[29],[31]),gg('A023-S09','B023-G08','C023-G14'),'corollary_heading',notation={'A':['S09'],'B':['S09'],'C':[11]},
    note='A/B attach their one dot to i in their own descriptions. C retains its dot/hook-or-retrace attachment and separate trace-hand qualification.')
add('family_index','External family K/I and complete predecessor/live states',([33],[30],[30]),alln('corollary_heading'),'corollary_heading',notation={'A':[14]},
    note='A has K. B preserves K / deleted-I then K / I. C preserves K / I / deleted-I then K / deleted-K then I. The complete parenthesized formulas and comma are supplied from each own source.')
add('whole_family','Complete family ownership, parentheses and comma',([],[],[]),alln('corollary_heading'),'corollary_heading')
add('pi_ring','Complete Pi_K ring/zero and literal body',([34],[31],[32]),gg('A023-G07','B023-P01','C023-G16'),'corollary_statement',notation={'A':[15],'B':['N12'],'C':[14]})
add('whole_corollary','Complete two-line corollary statement and labels',([],[],[]),alln('corollary_statement'),'corollary_statement',
    note='Whole-region sources include every adjoining word, node, formula, punctuation mark, nested group, declared unit, origin, baseline and local hand qualification through the linked raw component records.')
add('left_rule','Interrupted left rule beside corollary',([36],[35],[33]),gg('A023-G07','B023-G10','C023-G15'),'corollary_statement',
    note='Each literal path sequence stays separate: A two runs; B six runs plus a bead; C four runs. These are copied source descriptions, not a selected physical count.')
add('sigma10','Corollary constituent Sigma, complete local states and points',([35],[32],[34]),gg('A023-S10','B023-S10','C023-G18'),'corollary_statement',notation={'A':['S10'],'B':['S10'],'C':[12]},
    note='A’s report row is the upper point; its complete S10 source and notation carry the surrounding glyph. B retains the predecessor-i/alpha state. C retains both local point attachments and the additional plus-run roles in local_parts.')
add('formee_cup','Complete formée and shared f/cup group',([37],[33],[36]),gg('A023-G07','B023-G09','C023-G17'),'corollary_statement',
    note='A includes literal f and the ormée node. B/C supply literal word paths. C explicitly includes interrupted upper-left stalk runs. Every source’s full word, accent, cup, limit and local roles stay attached.')
add('final_cross','Final union high cross-stroke presence and role',([38],[33],[35]),gg('A023-G07','B023-G09','C023-G17'),'corollary_statement',
    note='Original C R16 scope is preserved. C separately qualifies the cross role; A/B own raw statements remain. H’s complete body and disjoint-union note are attached literally. No final counts are derived.')
add('sigma11','Final hatted Sigma, roof, separate head, body and decorations',([39],[34],[37]),gg('A023-S11','B023-S11','C023-G19'),'corollary_statement',notation={'A':['S11'],'B':['S11'],'C':[13]})
add('immediat','Final Immédiat complete accent candidates',([40],[],[38]),
    {'A':[exact('A','\\unsure{Immédiat|Immèdiat|Immediat}')],'B':[n('B','last_sentence')],'C':[gr('C','C023-G20')]},'last')
add('recurrence','Final récurrence complete accent candidates',([41],[],[39]),
    ex3('\\unsure{récurrence|rècurrence|recurrence}','récurrence','\\unsure{récurrence|rècurrence|recurrence}'),'last')
add('final_faint_hook','Faint hook by final initial capital',([],[],[40]),
    {'A':[n('A','last_sentence')],'B':[n('B','last_sentence')],'C':[gr('C','C023-G20')]},'last',
    absence={'A':'The attached complete A last-sentence source has no dedicated faint hook group at this location.','B':'The attached complete B last-sentence source has no dedicated faint hook group at this location.'})
add('final_count','Written card K comparison and full sentence endpoint',([],[],[]),alln('last_sentence'),'last',notation={'A':[17],'B':['N13'],'C':[16]})
add('archive_number','Archive sheet-number comment',([],[],[]),alln('archive_comment'),'last',
    note='All three actual comments are preserved. Manuscript numbering is not inferred from H’s editorial page selector.')

differences_by_num={r:{int(d['id'].split('D')[-1]):d for d in coverage[r]['differences']} for r in 'ABC'}
seen={r:set() for r in 'ABC'}
group_seen={r:set() for r in 'ABC'}
inventory_seen={r:set() for r in 'ABC'}

def overlap(a,b):
    return a['char_start_zero_based']<b['char_end_exclusive'] and b['char_start_zero_based']<a['char_end_exclusive']
def resolve_notation(r,ids):
    out=[]
    for ident in ids:
        x=coverage[r]['notation'][ident] if isinstance(ident,int) else next(n for n in coverage[r]['notation'] if n['id']==ident)
        out.append(dict(raw=x['raw'],source_ref=x['source_ref'],own_tex_refs=x['own_tex_refs']))
    return out

union=[]
for i,spec in enumerate(specs):
    entry=dict(locus_id=f'U023-{i+1:02}',key=spec['key'],location=spec['label'],readers={},
               witness_contexts={w:witness['C_and_H_named_contexts'][w][spec['witness_scope']] for w in ['C','H']},
               H_source_marker_candidates=spec['Hmarkers'],source_scope_note=spec['note'],
               source_selected=False,selected_counts=None,main_approved=False)
    for r in 'ABC':
        refs=spec['refs'][r]
        ds=[differences_by_num[r][n] for n in spec['diff_nums'][r]]
        seen[r].update(d['id'] for d in ds)
        ids={d['id'] for d in ds}
        qs=[d for d in coverage[r]['doubts'] if (d.get('difference_id',d['id']).removeprefix('Q-')) in ids]
        gs=[g for g in groups[r].values() if any(overlap(g['tex_ref'],x) for x in refs)]
        group_seen[r].update(g['id'] for g in gs)
        ins=[v for v in coverage[r]['inventory'] if any(overlap(vref,x) for vref in v['complete_tex_refs'] for x in refs)]
        inventory_seen[r].update(v['id'] for v in ins)
        entry['readers'][r]=dict(
            actual_complete_source_spans=refs,
            reported_difference_rows=[dict(id=d['id'],raw=d['raw'],source_ref=d['source_ref']) for d in ds],
            reported_doubt_rows=[dict(id=d['id'],raw=d['raw'],source_ref=d['source_ref']) for d in qs],
            own_notation_rows=resolve_notation(r,spec['notation'].get(r,[])),
            graphical_source_groups=[dict(id=g['id'],raw=g['raw'],source_map_ref=g['map_ref'],complete_tex_ref=g['tex_ref']) for g in gs],
            inventory_source_rows=[dict(id=v['id'],raw=v['raw'],source_ref=v['source_ref']) for v in ins],
            difference_list_silent_for_this_locus=not bool(ds),
            source_encoding_observation=spec['absence'].get(r),
            provenance_rule='Every source excerpt and raw qualification above belongs to this reader. A silent difference-list slot supplies no reading. Text-span overlap adds a containing reference and confers no physical ownership or hand attribution.')
    union.append(entry)

missing_diff={r:sorted(set(d['id'] for d in coverage[r]['differences'])-seen[r]) for r in 'ABC'}
missing_groups={r:sorted(set(groups[r])-group_seen[r]) for r in 'ABC'}
missing_inventory={r:sorted(set(x['id'] for x in coverage[r]['inventory'])-inventory_seen[r]) for r in 'ABC'}
assert not any(missing_diff.values()),missing_diff
assert not any(missing_groups.values()),missing_groups
assert not any(missing_inventory.values()),missing_inventory
for row in union:
    for r in 'ABC':
        for p in row['readers'][r]['actual_complete_source_spans']:
            assert p['literal']==tex[r][p['char_start_zero_based']:p['char_end_exclusive']]

c_rows=[]
for c in catalog['rows']:
    cid=c['source_id'];readers={}
    for r in 'ABC':
        raw=next(x for x in coverage[r]['original_C_rows'] if x['id']==cid)
        readers[r]=raw
    c_rows.append(dict(id=cid,canonical_parts=[p['part_id'] for p in c['source_parts']],actual_C_row=c,reader_returns=readers,selected_outcome=None))

support_hashes={r:hashlib.sha256((OUT/f'scan023_{r}_source_coverage.json').read_bytes()).hexdigest() for r in 'ABC'}
result=dict(scan='023',stage='complete released A/B/C source union',source_only=True,source_selected=False,
            main_adjudicated=False,main_approved=False,selected_record=None,selected_counts=None,
            limits='All rows are source bookkeeping. No image opened or interpreted, no geometric or mathematical calculation, no source chosen, no approval, no physical count determined. Literal coordinates, source descriptions and raw reader count/marker proposals remain provenance.',
            provenance=dict(B_manifest_exposure=coverage['B']['process_deviation'],write_pause='B extraction completed before root raw checkpoint pause; A/C were read while paused; A/C extraction and this union were written only after root explicitly released the pause.',
                            input_support={r:dict(path=f'out/checks/scan023_{r}_source_coverage.json',sha256_utf8=support_hashes[r]) for r in 'ABC'},
                            witness_support=dict(path=witness_path,sha256_utf8=hashlib.sha256((ROOT/witness_path).read_bytes()).hexdigest()),
                            diff_generation='No TeX diff files generated; root owns exact pairwise diff preparation and reading.'),
            loci=union,actual_C_doubt_rows=c_rows,
            H_marker_source_metadata=witness['H_markers'],S_scope_source_metadata=witness['S_scope'],
            supplied_table_scopes=witness['actual_C_sections'],
            complete_reader_source_partitions={r:coverage[r]['complete_TeX_partition'] for r in 'ABC'},
            complete_literal_command_indexes={r:coverage[r]['exact_graphical_commands'] for r in 'ABC'},
            complete_raw_component_maps={r:coverage[r]['graphical_component_records'] for r in 'ABC'},
            coverage_check=dict(source_locus_rows=len(union),all_difference_rows_referenced=True,all_graphical_groups_referenced=True,
                                all_inventory_rows_referenced=True,every_locus_has_A_B_C_actual_source=True,exact_local_source_spans_match=True,
                                missing_differences=missing_diff,missing_graphical_groups=missing_groups,missing_inventory=missing_inventory),
            next_authority='Root supplies all actual image decisions, count parents, C outcomes, confidence and exact selected groups before record assembly.')
target=OUT/'scan023_source_union.json'
target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def inline(value):return str(value).replace('|','\\|').replace('\n',' ')
md=['# Scan 023 — complete released source crosswalk','',
    'Source-only crosswalk. A, B and C retain their own exact readings, candidates, role/state qualifications and literal source paths. No transcription, count or ink outcome is selected. Complete raw fields and exact spans are in `scan023_source_union.json`; original files remain unchanged.','',
    'All 41 A difference rows, 37 B difference rows and 40 C difference rows are referenced. The full reader partitions and command indexes preserve every report-silent TeX choice. Actual C has 16 doubtful-table rows and 16 canonical parts; its notation and slip tables remain separate.','',
    '| Locus | Source scope | A report rows | B report rows | C report rows |','| --- | --- | --- | --- | --- |']
for row in union:
    cells=[]
    for r in 'ABC':
        ds=row['readers'][r]['reported_difference_rows']
        cells.append(', '.join(x['id'] for x in ds) or 'actual TeX / notation')
    md.append('| '+row['locus_id']+' | '+inline(row['location'])+' | '+' | '.join(cells)+' |')
md.extend(['','## Full reading and qualification crosswalk',''])
for row in union:
    md.extend([f"### {row['locus_id']} — {row['location']}",''])
    if row['source_scope_note']:md.extend([row['source_scope_note'],''])
    for r in 'ABC':
        ent=row['readers'][r]
        md.append(f'**{r}**')
        md.append('')
        if ent['reported_difference_rows']:
            for d in ent['reported_difference_rows']:
                raw=d['raw']
                md.append(f"- {d['id']}: `{raw['reading']}`")
                md.append(f"  Alternatives exactly as reported: `{json.dumps(raw.get('alternatives',[]),ensure_ascii=False)}`")
                for field in ['qualification','local_head_role','trace_hand','local_parts','recurring_qualification','component_scope','additional_local_changes']:
                    if field in raw:md.append(f"  {field}: `{json.dumps(raw[field],ensure_ascii=False)}`")
        else:
            md.append('Actual TeX and attached own-reader notation supply this locus; there is no difference-list entry for it.')
        for note in ent['own_notation_rows']:
            md.append('')
            md.append('Own notation: `'+json.dumps(note['raw'],ensure_ascii=False)+'`')
        if ent['source_encoding_observation']:
            md.extend(['',ent['source_encoding_observation']])
        md.append('')
        for p in ent['actual_complete_source_spans']:
            md.append(f"Source: `{p['path']}` chars [{p['char_start_zero_based']},{p['char_end_exclusive']}), lines {p['line_start_one_based']}–{p['line_end_one_based']}; SHA-256 `{p['sha256_utf8']}`.")
            if len(p['literal'])<650:
                md.extend(['','```tex',p['literal'],'```'])
        md.append('')
md.extend(['## Provenance limit','',coverage['B']['process_deviation'],'',
           'The complete JSON also retains the raw parent and component hand scopes, every original path/label owner, all whole-group declarations, H marker identities, the broad S source scope, and each reader’s return on the original C table. Physical decisions and counting remain with root.',''])
mdpath=OUT/'scan023_source_union.md'
mdpath.write_text('\n'.join(md),encoding='utf-8')
summary=dict(source_union_path=str(target.relative_to(ROOT)),source_union_sha256_utf8=hashlib.sha256(target.read_bytes()).hexdigest(),
             source_union_markdown_path=str(mdpath.relative_to(ROOT)),source_union_markdown_sha256_utf8=hashlib.sha256(mdpath.read_bytes()).hexdigest(),
             input_support_hashes=support_hashes,coverage_check=result['coverage_check'],source_selected=False,selected_counts=None,main_approved=False)
(OUT/'scan023_source_union_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
