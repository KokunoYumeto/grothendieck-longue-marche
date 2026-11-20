#!/usr/bin/env python3
"""Exact report/TeX all-locus source crosswalk. No root outcomes are inferred."""
from pathlib import Path
import copy
import hashlib
import json
import re
import sys
sys.dont_write_bytecode = True
from scan019_prepare_sources import span, json_spans

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'
U = json.loads((OUT / 'scan019_source_union.json').read_text())
assert U['released_readers'] == list('ABC')

TEXT = {r: (BASE / f'out/readers/019/{r}/reading.tex').read_text() for r in 'ABC'}
REPORT = {r: json.loads((BASE / f'out/readers/019/{r}/report.json').read_text()) for r in 'ABC'}
INDEX = {r: json_spans(f'out/readers/019/{r}/report.json', (BASE / f'out/readers/019/{r}/report.json').read_text()) for r in 'ABC'}


def source(r, literal, occurrence=0):
    text = TEXT[r]
    starts = [m.start() for m in re.finditer(re.escape(literal), text)]
    assert len(starts) > occurrence, (r, literal)
    start = starts[occurrence]
    return span(f'out/readers/019/{r}/reading.tex', text, start, start + len(literal))


def block(r, ordinal):
    return copy.deepcopy(U['reader_sources'][r]['tex_index']['complete_blocks'][ordinal]['source'])


def rows(r, field, ids):
    out = []
    for item in U['reader_sources'][r]['raw_rows'].get(field, []):
        value = item['value']
        if isinstance(value, dict) and (value.get('id') in ids or value.get('decision_id') in ids):
            out.append(copy.deepcopy(item))
    return out


def obj(r, pointer):
    value = REPORT[r]
    for part in pointer.strip('/').split('/'):
        value = value[int(part)] if isinstance(value, list) else value[part]
    return dict(value=copy.deepcopy(value), source=copy.deepcopy(INDEX[r][pointer]))


LOCI = []


def add(key, location, ids, block_id, c_rows=(), text_choices=None, supplemental=None, component_scope=None):
    ids = dict(zip('ABC', ids))
    text_choices = text_choices or {}
    supplemental = supplemental or {}
    item = dict(source_locus_id=key, location=location,
        source_C_doubt_rows=list(c_rows), readers={}, readers_report_only={},
        reader_difference_rows={}, reader_doubt_rows={}, reader_tex_scopes={}, reader_provenance={},
        reader_supplemental_sources={}, report_silent_choices=[],
        root_decision_id=None, root_status=None, diff_C=None, diff_H=None,
        count_status='Pending root; this source locus is not a physical-count instruction.',main_approved=False)
    for r in 'ABC':
        ds = rows(r, 'differences', ids[r])
        qs = rows(r, 'doubts', ids[r])
        if r == 'B':
            BQ = {'B01':['Q01'],'B04':['Q02'],'B06':['Q03'],'B07':['Q04'],'B08':['Q05'],
                  'B09':['Q06'],'B10':['Q07'],'B11':['Q08'],'B12':['Q09'],'B13':['Q10'],
                  'B14':['Q11'],'B15':['Q12'],'B16':['Q13'],'B17':['Q14'],'B18':['Q15']}
            qs = rows(r,'doubts',[q for x in ids[r] for q in BQ.get(x,[])])
        if key == 'SRC019-JOIN2' and r == 'C':
            qs = rows(r,'doubts',['N-JOIN2'])
        bs = block(r, block_id)
        item['reader_tex_scopes'][r] = bs
        item['reader_difference_rows'][r] = ds
        item['reader_doubt_rows'][r] = qs
        item['readers_report_only'][r] = [x['value']['reading'] for x in ds]
        public = [x['value']['reading'] for x in ds]
        if r in text_choices:
            choice = text_choices[r]
            public.append(choice['description'])
            item['report_silent_choices'].append(dict(reader=r,**copy.deepcopy(choice),
                complete_inspected_tex_scope=bs,
                scope='Literal source reading/absence within this complete span; no statement about uninspected ink.'))
        for q in qs:
            value = q['value']
            if value.get('alternatives'):
                public.append('Local alternatives retained in original doubt record: ' + json.dumps(value['alternatives'],ensure_ascii=False))
        supplements = supplemental.get(r,[])
        item['reader_supplemental_sources'][r] = supplements
        for extra in supplements:
            if isinstance(extra['value'],str):
                public.append(extra['value'])
            elif isinstance(extra['value'],dict) and 'reading' in extra['value']:
                public.append(extra['value']['reading'])
                if extra['value'].get('alternatives'):
                    public.append('Locally retained alternatives: '+json.dumps(extra['value']['alternatives'],ensure_ascii=False))
        assert public,(key,r)
        item['readers'][r] = public
        item['reader_provenance'][r] = [x['source'] for x in ds+qs+supplements]+[bs]
    if component_scope:
        item['component_scope'] = component_scope
    LOCI.append(item)


def choice(r,literal,description=None,occurrence=0):
    return dict(description=description or literal,literal_source=source(r,literal,occurrence))


add('SRC019-CONVENTION','Opening metadata convention',([],['B00'],['D00']),0,
    text_choices={'A':choice('A',r'\scanpage{19}',r'\scanpage{19}; no cotefile wrapper in the complete reader source.')},
    supplemental={'A':[obj('A','/notes/metadata_conventions')]})
add('SRC019-ACCENT','Opening Dém. accent',([],['B01'],[]),0,
    text_choices={'A':choice('A','Dém.'),'C':choice('C','Dém.')})
add('SRC019-EDGE','Post-1 punctuation at the physical right edge',(['A18'],['B02'],['D01']),0,
    component_scope='Post-1 punctuation only; Le has its own source locus. Raw wider report readings remain unchanged.')
add('SRC019-LE','Capital Le at line two',(['A17'],['B03'],['D02']),0)
add('SRC019-CARD-POINT','Faint point above initial side of second card, root-added source locus',([],[],[]),0,
    text_choices={r:choice(r,r'Le cas $\operatorname{card} I=2$',
        r'The complete opening source prints Le cas $\operatorname{card} I=2$ with no separately represented point above this second card.') for r in 'ABC'},
    component_scope='Root journal section 01 introduces this locus. Reader absence is established only in each inspected complete opening TeX span; no reader ink decision is inferred.')
add('SRC019-AVEC','avec before card',(['A09'],['B04'],['D03']),0,['C019-R09'])
add('SRC019-INEQUALITY','Typographic source form of the existing cardinality inequality',([],[],[]),0,
    text_choices={r:choice(r,r'\geqslant' if r=='A' else r'\geq') for r in 'ABC'},
    supplemental={'A':[obj('A','/notation/0')],'B':[obj('B','/notation/0')],'C':[obj('C','/notation/0')]},
    component_scope='Root L019-06 selects A geqslant as a noncount source-form decision. Actual witness macro spellings remain distinct and exact.')
add('SRC019-ENS','ens. before paired display',(['A01'],['B05'],['D04']),0,['C019-R01'])
add('SRC019-U','Complete first U entrance/body group',(['A10'],['B06'],['D05']),1,['C019-R10'])
add('SRC019-LUNE','l’une/l’un word',(['A11'],['B07'],['D06']),2,['C019-R11'],
    component_scope='Word reading; lower marks have their own source component loci.')
add('SRC019-LOWER-POINT','Dark point beneath l’une/l’un',(['A15'],['B08'],['D07']),2,
    component_scope='Dark point component; raw B08/D07 retain the whole dark-point/pale-trace group. Root chooses the physical count parent.')
add('SRC019-LOWER-TRACE','Pale lower-left trace beneath l’une/l’un',([],['B08'],['D07']),2,
    text_choices={'A':choice('A',r"\(\underset{\phantom{\text{l'un}}\unsure{\cdot}}{\text{\unsure{l'une|l'un}}}\)",
        'One qualified dark point is printed with the word; no separate pale lower-left trace is emitted in this complete source span.')},
    supplemental={'A':[obj('A','/notes/point_scope')]},
    component_scope='Pale trace component; raw B08/D07 include the dark point too. Root chooses the physical count parent.')
add('SRC019-ONA1','on a after Par hyp.',(['A02'],['B09'],['D08']),2,['C019-R02'])
add('SRC019-JOIN1','First footed join',(['A03'],['B10'],['D09']),3,['C019-R03'])
add('SRC019-J-PREDECESSOR','Cancelled predecessor before first lower-limit K0',(['A04'],['B11'],['D10']),3,['C019-R04'],
    component_scope='Predecessor glyph/body; C D10 includes its separate high point. Root chooses count scope.')
add('SRC019-J-POINT','High point at first lower-limit predecessor',(['A04'],[],['D10']),3,
    text_choices={
        'A':choice('A',r'\deleted{\unsure{J|j}}K_0',
            r'\deleted{\unsure{J|j}}K_0; a nearby point is reported in A04, but this source emits no separate \cdot. The j alternative includes its ordinary dot.'),
        'B':choice('B',r'\deleted{\unsure{J}}K_0',
            r'\deleted{\unsure{J}}K_0; no separate high-point command in the complete first-equality source.')},
    component_scope='High-point component under the source R04 predecessor context. C D10 is one raw predecessor/point cluster; no extra original C doubt row.')
add('SRC019-SIGMA-PREDECESSOR','Brace Sigma predecessor and lower alpha/zero',(['A12'],['B12'],['D11']),5,['C019-R12'])
add('SRC019-BRACE-TRACE','Pale trace to the left of brace',([],[],['D12']),5,
    text_choices={r:dict(description='No separate left-of-brace trace is represented in this complete brace display.',literal_source=block(r,5)) for r in 'AB'})
add('SRC019-MAIN-BRACE','Complete main brace source form',([],[],[]),5,
    text_choices={r:choice(r,r'\left\{\begin{aligned}',
        r'The main brace is represented by \left\{\begin{aligned}...\end{aligned}\right.; no separate literal main-brace path is supplied in this complete display.') for r in 'ABC'},
    component_scope='Root section 09 identifies the complete main brace for a later distinct local inspection. This is source representation only; no root outcome/count is inferred.')
add('SRC019-E-INDEX','Terminal E_alpha in third brace condition',([],[],[]),5,
    text_choices={r:choice(r,r'\widehat{\Sigma}_\alpha^+=\Sigma_\alpha^+\cup E_\alpha.') for r in 'ABC'},
    supplemental={'A':[obj('A','/notes/mathematics_led_reading'),obj('A','/notation/4')]})
add('SRC019-ONA2','On a before donc, complete live/cancelled state',(['A05'],['B13'],['D13']),6,['C019-R05'])
add('SRC019-PRE-X-POINT','Detached point immediately before lower X',([],[],['D14']),7,
    text_choices={r:choice(r,r'U=U_{J,i}\cap\Sigma_i^-=X\setminus',
        r'The literal sequence is U=U_{J,i}\cap\Sigma_i^-=X\setminus; no separate point occurs between the equality and X in this complete display.') for r in 'AB'})
add('SRC019-JOIN2','Second footed join with its locally retained alternative',(['A16'],['B14'],[]),7,
    text_choices={'C':choice('C',r'\coprod_{\alpha\in K_0}',r'\coprod is printed without another unsure wrapper; the local \bigsqcup alternative remains in N-JOIN2 and notation/3.')},
    supplemental={'C':[obj('C','/notation/3')]})
add('SRC019-ENDPOINT','Detached two-point group at lower display end',([],['B15'],['D15']),7,
    text_choices={'A':dict(description='No separate endpoint-point group is represented between the closing parenthesis and the end of this complete display.',literal_source=block('A',7))})
add('SRC019-AU','Au after cancelled Soit',([],[],[]),8,
    text_choices={r:choice(r,r'\deleted{Soit} Au ','Au') for r in 'ABC'},
    component_scope='Au alone; the cancelled Soit and ordinal remain contextual source words. Root section 14 selects this noncount source reading.')
add('SRC019-ORDINAL','Word between Au and equality',(['A13'],['B16'],['D16']),8)
add('SRC019-STRUCK-SOMME','Cancelled word after dans la',(['A06'],['B17'],['D17']),8,['C019-R06'])
add('SRC019-BORNER-SIGN','Mark between borner and sommer',(['A14'],['B18'],['D18']),8)
add('SRC019-SOMMER','sommer after the borner mark',(['A07'],['B19'],['D19']),8,['C019-R07'])
add('SRC019-CET','cet after K1',(['A08'],['B20'],['D20']),8,['C019-R08'])
add('SRC019-Q-DESCENDER','Attachment of upright to q in existing tels que',([],[],[]),8,
    text_choices={r:choice(r,'tels que','tels que; no separate adjacent-upright graphic is emitted in the complete reader source.') for r in 'ABC'},
    supplemental={'A':[obj('A','/notes/boundary_limits')],'C':[obj('C','/notes/crop_boundaries')]},
    component_scope='Root section 18 identifies the full connected q descender. A explicitly attributed the crop13-entering descender to que; C recorded a preceding-line descender without naming its word; B supplied the existing word without a separate attachment statement. No extra inventory mark is inferred.')
add('SRC019-FINAL-INDEX','Final display lower limit at physical bottom edge',([],['B21'],[]),9,
    text_choices={r:choice(r,r'\bigcup_{\alpha\in K_1}') for r in 'AC'},
    supplemental={'A':[obj('A','/notation/6')],'C':[obj('C','/notation/8')]})
add('SRC019-ARCHIVE','Archive numeral 18 as comment',([],[],[]),10,
    text_choices={r:choice(r,'% archive sheet number: 18') for r in 'ABC'},
    supplemental={'A':[obj('A','/inventory/21')],'B':[obj('B','/inventory/21')],'C':[obj('C','/inventory/23')]})
add('SRC019-S-AUDIT','S page source scope and local roofs',([],[],[]),0,
    supplemental={'A':[obj('A','/S_page_scope')],
                  'B':[obj('B','/notes/S_row_scope'),obj('B','/notation/4')],
                  'C':[obj('C','/notes/S_row_handling'),obj('C','/notation/5')]},
    text_choices={r:dict(description='Current reader complete TeX preserves the source roofed Sigma occurrences; exact S review is separately retained.',literal_source=span(f'out/readers/019/{r}/reading.tex',TEXT[r])) for r in 'ABC'})

row_map = {r:{} for r in 'ABC'}
for locus in LOCI:
    for r in 'ABC':
        for raw in locus['reader_difference_rows'][r]:
            row_map[r].setdefault(raw['value']['id'],[]).append(locus['source_locus_id'])
for r in 'ABC':
    expected={x['id'] for x in REPORT[r]['differences']}
    assert set(row_map[r])==expected,(r,expected-set(row_map[r]),set(row_map[r])-expected)

# Inventory identities are grouped by declared source scope only. Selection,
# hand/confidence and whether a group is transcribed remain root decisions.
INVENTORY_SPECS = [
    ('TOP','Top prose', [0],[0],[0],[0]),
    ('PAIRED','Paired display', [1],[1],[1],[1]),
    ('FIRST-U','First U complete group and possible predecessor state', [2],[2],[2,3],[2]),
    ('BELOW-PAIRED','Prose below paired display', [3],[3],[4],[3]),
    ('LOWER-MARKS','Lower point/trace group at l’une/l’un', [],[4],[5],[4]),
    ('PAR-HYP','Par hyp. lead-in', [4],[5],[6],[5]),
    ('FIRST-EQUALITY','First single equality', [5],[6],[7],[6]),
    ('FIRST-JOIN','Literal first-join graphical candidate', [],[7],[],[]),
    ('J-PREDECESSOR','First lower-limit predecessor', [6],[8],[8],[7]),
    ('J-POINT','High point at first predecessor', [],[],[],[8]),
    ('OU','où', [7],[9],[9],[9]),
    ('BRACE','Complete brace conditions', [8],[10],[10],[11]),
    ('SIGMA-PREDECESSOR','Brace predecessor', [9],[11],[11],[12]),
    ('BRACE-TRACE','Pale trace left of brace', [],[],[],[10]),
    ('ONA2','On a donc lead-in', [10],[12],[12],[13]),
    ('ONA2-STATE','Possible cancelled initial O/On state', [],[13],[13],[14]),
    ('LOWER-EQUALITY','Lower U equality', [11],[14],[14],[15]),
    ('SECOND-JOIN','Literal second-join graphical candidate', [],[15],[],[]),
    ('X-POINT','Point immediately before lower X', [],[],[],[16]),
    ('ENDPOINT','Lower display endpoint-point pair', [],[],[15],[17]),
    ('SOIT','Cancelled Soit', [12],[16],[16],[18]),
    ('LOWER-PROSE','Last prose paragraph', [13],[17],[17],[19]),
    ('SOMME','Cancelled somme/réunion', [14],[18],[18],[20]),
    ('CANCELLED-SIGMA','Cancelled Sigma after sur les', [15],[19],[19],[21]),
    ('FINAL-DISPLAY','Final display', [16],[20],[20],[22]),
    ('ARCHIVE','Archive numeral comment', [],[21],[21],[23]),
]
inventory_groups=[]
inventory_seen={r:[] for r in ['witness C','A','B','C']}
for key,scope,c,a,b,cr in INVENTORY_SPECS:
    group=dict(source_inventory_id='SRC019-INV-'+key,scope=scope,source_rows={},selected=None,main_approved=False)
    for reader,indices in [('witness C',c),('A',a),('B',b),('C',cr)]:
        candidate=[x for x in U['candidate_inventory'] if x['reader']==reader]
        group['source_rows'][reader]=[copy.deepcopy(candidate[i]) for i in indices]
        inventory_seen[reader].extend(indices)
    inventory_groups.append(group)
for reader,indices in inventory_seen.items():
    expected=len([x for x in U['candidate_inventory'] if x['reader']==reader])
    assert sorted(indices)==list(range(expected)),(reader,indices,expected)

output=dict(scan=19,scope='Complete source crosswalk only; root supplies ink/count/approval outcomes.',
    source_union=dict(path='out/checks/scan019_source_union.json',sha256=hashlib.sha256((OUT/'scan019_source_union.json').read_bytes()).hexdigest()),
    loci=LOCI,original_difference_row_crosswalk=row_map,
    original_C_rows=copy.deepcopy(U['C_doubt_crosswalk']),
    inventory_source_groups=inventory_groups,
    helper_identifier_history=[dict(previous='SRC019-X-POINT',current='SRC019-PRE-X-POINT',
        basis='Root section 12 names SRC019-PRE-X-POINT for C_M05 / reader-C D14; both labels point to the same exact before-X source span. Original reader IDs remain unchanged.'),
        dict(previous='SRC019-SOMME',current='SRC019-STRUCK-SOMME',basis='Root section 15 names SRC019-STRUCK-SOMME for A06/B17/D17 at original C019-R06; both labels point to that exact cancelled-word source span. Original reader IDs remain unchanged.'),
        dict(previous='SRC019-BORNER',current='SRC019-BORNER-SIGN',basis='Root section 16 names SRC019-BORNER-SIGN for A14/B18/D18; both labels point to the exact sign between borner and sommer. Original reader IDs remain unchanged.')],
    all_original_difference_rows_mapped=True,main_adjudicated=False,
    count_scope_note='Source components preserve raw identities and alternatives; source-locus number is not a physical difference count.')
path=OUT/'scan019_source_crosswalk.json'
path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
md=['# Scan019 — exact source crosswalk','',
    'All actual source flags remain in the JSON. This table supplies source identities only; root supplies all outcomes and counts.','',
    '| Source locus | Location | A | B | C | Original C row |','| --- | --- | --- | --- | --- | --- |']
for l in LOCI:
    fields=[l['source_locus_id'],l['location']]
    for r in 'ABC':
        ids=[x['value']['id'] for x in l['reader_difference_rows'][r]]
        if not ids:ids=['complete TeX / recorded audit']
        fields.append(', '.join(ids))
    fields.append(', '.join(l['source_C_doubt_rows']) or '—')
    md.append('| '+' | '.join(x.replace('|','\\|') for x in fields)+' |')
md.extend(['','Every reader has an actual public reading and exact report/doubt/complete-TeX pointers. Report-silent choices and literal absences are scoped to the inspected complete source span. C N-JOIN2 and every locally retained alternative remain explicit.'])
(OUT/'scan019_source_crosswalk.md').write_text('\n'.join(md)+'\n')
print(json.dumps(dict(path=str(path.relative_to(BASE)),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
    source_loci=len(LOCI),raw_rows_mapped={r:len(x) for r,x in row_map.items()}),ensure_ascii=False))
