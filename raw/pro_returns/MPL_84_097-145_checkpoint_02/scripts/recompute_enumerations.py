#!/usr/bin/env python3
"""Recompute declared counts/models from frozen text without editing it.

Requires Python 3 and SymPy for universal symbolic checks. No image/OCR,
network, archive, upload, transcription-combine or freeze operations occur.
"""
from pathlib import Path
from collections import Counter
from itertools import product, permutations, combinations
import json, re
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'
PAGES={int(re.search(r'scan(\d+)',p.name).group(1)):p.read_text() for p in sorted((ROOT/'pages').glob('*.tex'))}
CATALOG=json.loads((OUT/'enumerations.json').read_text())
REPORT={'scope':'Counts, source layout checks, and explicitly declared algebraic models. A verified model is not a proof of every manuscript assertion, and no uncertain glyph is corrected.', 'sympy_version':sp.__version__, 'checks':{},'limitations':[]}

def group(text, start):
    assert text[start]=='{'
    depth=1;i=start+1
    while depth:
        if i>=len(text):raise ValueError('unbalanced group')
        if text[i]=='\\' and i+1<len(text) and text[i+1] in '{}\\':i+=2;continue
        if text[i]=='{':depth+=1
        elif text[i]=='}':depth-=1
        i+=1
    return text[start+1:i-1],i

def live_text(text):
    while True:
        match=re.search(r'\\deleted\s*\{',text)
        if not match:return text
        _,end=group(text,match.end()-1)
        old=text[match.start():end]
        text=text[:match.start()]+''.join('\n' if c=='\n' else ' ' for c in old)+text[end:]

def split_array(body):
    rows=[];row=[];cell=[];depth=0;i=0
    while i<len(body):
        if body[i]=='\\' and i+1<len(body):
            if body[i+1]=='\\' and depth==0:
                row.append(''.join(cell).strip());rows.append(row);row=[];cell=[];i+=2
                while i<len(body) and body[i].isspace():i+=1
                if i<len(body) and body[i]=='[':
                    end=body.find(']',i)
                    if end>=0:i=end+1
                continue
            if body[i+1] in '{}\\&':cell.extend(body[i:i+2]);i+=2;continue
        c=body[i]
        if c=='{':depth+=1
        elif c=='}':depth-=1
        if c=='&' and depth==0:row.append(''.join(cell).strip());cell=[]
        else:cell.append(c)
        i+=1
    row.append(''.join(cell).strip())
    if any(row):rows.append(row)
    return rows

arrays=[]
for scan,text in PAGES.items():
    for match in re.finditer(r'\\begin\{array\}',text):
        pos=match.end()
        while text[pos].isspace():pos+=1
        spec,pos=group(text,pos)
        end=text.index(r'\end{array}',pos)
        rows=split_array(text[pos:end])
        declared_spec=re.sub(r'@\{.*?\}','',spec)
        declared=sum(c in 'clr' for c in declared_spec)
        arrays.append({'scan':scan,'source_line':text[:match.start()].count('\n')+1,'declared_columns':declared,'rows':len(rows),'explicit_row_widths':[len(r) for r in rows],'nonblank_cells':sum(bool(c) for r in rows for c in r),'cells':rows})
expected_shapes={97:[(3,1)],99:[(2,1)],103:[(5,1)],107:[(2,2)],115:[(3,3)],132:[(2,3)],138:[(2,2)],144:[(2,3),(2,2)]}
actual={scan:[(a['rows'],max(a['explicit_row_widths'])) for a in arrays if a['scan']==scan] for scan in sorted({a['scan'] for a in arrays})}
assert actual==expected_shapes,(actual,expected_shapes)
REPORT['checks']['source_arrays']={'passed':True,'array_count':len(arrays),'arrays':arrays,'qualification':'Scan107 declares three layout columns but populates two; scan132 includes one blank cell. Equality marks are retained as rows, not counted mathematical objects.'}

labels110=re.findall(r'\\textcircled\{([1-6])\}',live_text(PAGES[110]))
assert labels110==list('123456'),labels110
labels111=re.findall(r'^([abcd])\)',live_text(PAGES[111]),re.M)
assert labels111==list('abcd'),labels111
labels105=re.findall(r'^([12])\)',live_text(PAGES[105]),re.M)
assert labels105==['1','2'],labels105
labels106=re.findall(r'\\text\{([ab])\)\}',live_text(PAGES[106]))
assert labels106==['a','b'],labels106
assert '6 diagrammes' in PAGES[112]
labels142=re.findall(r'^([12])°\)',live_text(PAGES[142]),re.M)
assert labels142==['1','2'],labels142
REPORT['checks']['condition_labels']={'passed':True,'scan105_main_parts':labels105,'scan106_norm_conditions':labels106,'scan110_recap':labels110,'scan110_mandatory':labels110[:5],'scan110_optional':labels110[5:],'scan111_data_groups':labels111,'scan142_F11_constraints':labels142,'qualification':'This verifies literal labels. It does not prove existence, independence, or completeness of the mathematical assertions.'}

triples=list(product((0,1),repeat=3))
even=[t for t in triples if sum(t)%2==0]
nonzero=[t for t in even if any(t)]
source_live=[tuple(map(int,m)) for m in re.findall(r'\(([01]),([01]),([01])\)',live_text(PAGES[116]))]
assert source_live==nonzero,(source_live,nonzero)
ordered=list(permutations((1,2,3),2));assert len(ordered)==6
pair_indices=[(0,1),(1,2),(2,0)]
fibers={epsilon:[t for t in triples if sum(t)%2==epsilon] for epsilon in (0,1)}
fiber_checks=[]
for epsilon,J in fibers.items():
    bijections=[]
    for pair in pair_indices:
        image=[tuple(t[i] for i in pair) for t in J]
        bijections.append(len(set(image))==4 and set(image)==set(product((0,1),repeat=2)))
    for point in J:
        orbit={tuple(a^b for a,b in zip(point,g)) for g in even}
        assert orbit==set(J)
    assert all(bijections)
    fiber_checks.append({'epsilon':epsilon,'members':J,'pair_projection_bijections':bijections,'orbit_size':4,'stabilizer_size':1})
bad=[t for t in triples if sum(t)>=2]
assert len(even)==4 and len(nonzero)==3 and len(bad)==4
labels122=re.findall(r'"((?:2|4|8)(?:\(!\))?)"',PAGES[122])
assert Counter(labels122)==Counter({'8':1,'2':2,'4(!)':1,'2(!)':1}),labels122
REPORT['checks']['binary_group']={'passed':True,'ambient_triples':triples,'ambient_order':8,'even_subgroup':even,'subgroup_order':4,'nonzero_live_source_triples':source_live,'deleted_source_candidate':[0,0,1],'ordered_pairs':ordered,'ordered_pair_count':6,'trace_norm_instances_derived':12,'fibers':fiber_checks,'three_unordered_index_pairs':list(combinations((1,2,3),2)),'bad_nonetale_status_patterns':bad,'bad_pattern_count':4,'rank_labels_scan122':labels122,'etale_model_ranks':{'B':8,'B0':2,'B1':4},'qualification':'The bit model is an editorial encoding. Rank ratios4 and2 in scan122 pass only in this split etale model; the manuscript explicitly denies general flatness, so no general relative-rank assertion is certified.'}

perms=[(1,0,3,2),(2,3,0,1),(3,2,1,0)]
def compose(a,b):return tuple(a[b[i]] for i in range(4))
identity=(0,1,2,3)
assert all(compose(p,p)==identity for p in perms)
assert compose(perms[0],perms[1])==perms[2]
assert all(compose(a,b)==compose(b,a) for a in perms for b in perms)
pairings=[[(i,p[i]) for i in range(4) if i<p[i]] for p in perms]
edges=[edge for pairs in pairings for edge in pairs]
assert len(edges)==6 and set(edges)==set(combinations(range(4),2))
x0,x1,x2,x3=sp.symbols('x0 x1 x2 x3');xs=[x0,x1,x2,x3]
norm_product=sp.prod(xs)
assert sp.expand(sp.prod(x0*x for x in xs[1:])-x0**2*norm_product)==0
assert sp.expand(sum(x0+x for x in xs[1:])-sum(xs)-2*x0)==0
REPORT['checks']['four_conjugates']={'passed':True,'completed_editorial_permutations':perms,'three_pairings':pairings,'distinct_edges':6,'pair_incidences':12,'norm_product':str(norm_product),'triple_relative_norm_product':str(sp.prod(x0*x for x in xs[1:])),'qualification':'This completes each pair to an involution as a declared model. It does not replace the literal one-way or doubtful arrowheads in scan115, or the doubtful Ti/sigmai readings.'}

b1,b2,c1,c2,u1,u2=sp.symbols('b1 b2 c1 c2 u1 u2')
rel1=u1**2+b1*u1+c1;rel2=u2**2+b2*u2+c2
def reduce_tensor(expr):return sp.expand(sp.rem(sp.rem(sp.expand(expr),rel1,u1),rel2,u2))
def conjugate(expr):return reduce_tensor(expr.subs({u1:-b1-u1,u2:-b2-u2},simultaneous=True))
basis=[sp.Integer(1),u1,u2,u1*u2]
trace=[reduce_tensor(z+conjugate(z)) for z in basis]
norm=[reduce_tensor(z*conjugate(z)) for z in basis]
image_u=2*u1*u2+b1*u2+b2*u1
assert trace==[2,-b1,-b2,sp.expand(image_u+b1*b2)],trace
assert norm==[1,c1,c2,c1*c2],norm
coefficient_b=b1*b2;coefficient_c=b1**2*c2+b2**2*c1-4*c1*c2
remainder=reduce_tensor(image_u**2+coefficient_b*image_u+coefficient_c)
assert remainder==0,remainder
REPORT['checks']['quadratic_basis']={'passed':True,'basis':list(map(str,basis)),'basis_count':4,'trace_tensor_images':list(map(str,trace)),'norm_values':list(map(str,norm)),'product_coefficients':{'b':str(coefficient_b),'c':str(coefficient_c)},'product_relation_remainder':str(remainder),'qualification':'This rechecks the current literal local table in the stated monic model. The same product identity is already claimed checked in earlier L172.1/R05; no novelty or global-category conclusion is asserted, and commutative rank4 is not central Azumaya rank4.'}

chi,gamma,B1,B2,U1,U2,V1,V2,B,U=sp.symbols('chi gamma b1 b2 U1 U2 V1 V2 b U')
def transition(a,b,u,v):return a*v+u*b+chi*u*v
first=transition(B1,B2,U1,U2)
second=transition(B1+chi*U1,B2+chi*U2,V1,V2)
combined=transition(B1,B2,U1+V1,U2+V2)
cocycle=sp.expand(combined-first-second);assert cocycle==0
target_defect=sp.expand((B1+chi*U1)*(B2+chi*U2)-B1*B2-chi*first);assert target_defect==0
square_defect=sp.expand((U-gamma*(B+chi*U))-(-U-gamma*B))
assert sp.expand(square_defect-(2-gamma*chi)*U)==0
mixed_sign_defect=sp.expand(transition(B1-chi*U1,B2-chi*U2,V1,V2)+first-combined)
assert sp.expand(mixed_sign_defect + 2*chi*(U1*V2+U2*V1))==0
unprimed_second_factor_residual=sp.expand((B2+chi*V2)-(B2+chi*U2+chi*V2))
assert unprimed_second_factor_residual==-chi*U2
REPORT['checks']['transition']={'passed':True,'checked_branch':'b_i′=b_i+chi U_i for both i and b_i″=b_i′+chi V_i; this is an explicit consistent model, not a claim that all source rows have these signs/primes.','product_target_residual':str(target_defect),'cocycle_residual':str(cocycle),'mixed_minus_branch_cocycle_residual':str(mixed_sign_defect),'scan132_lower_second_factor_unprimed_base_residual':str(unprimed_second_factor_residual),'comparison_square_defect':str(sp.factor(square_defect)),'qualification':'Earlier R11/E170.5 already claim this local composition/gluing calculation. The source upper minus sign and lower unprimed b2 are retained as separate unresolved source differences.'}
REPORT['checks']['binary_choices']={'passed':True,'four_type_cases':list(product(('f','U'),repeat=2)),'four_shift_cases':list(product(('x','u'),repeat=2)),'qualification':'U factors through M and takes values in L. Counting four cases does not identify the differing product conventions or repair signs.'}

typed={
 'EN127.1':{'declared_periods':3,'members':['childhood','second period','maturity/third period']},
 'EN127.2':{'listed_traits':['volonté','intelligence','contrôle de soi','ascendant sur autrui','intransigeance','Konsequenz','idéalisme'],'exhaustive':False},
 'EN127.3':{'family_roles':['mother','father','sister','self'],'other_nearest_roles':['mother','father','sister']},
 'EN127.4':{'section_numbers':[36,37]},
 'EN129.1':{'questions':['standard conjectures','resolution of singularities']},
 'EN139.1':{'reported_dates':{'father':1942,'mother':1957}},
 'EN141.1':{'subjects':['latin','grec','mathématiques']},
 'EN143.1':{'initials':['M.','J.','S.']},
 'EN145.1':{'declared_forces':2,'explicitly_developed_here':1,'unprovided_named_member':1},
 'EN145.2':{'helped_raise':4,'fifth_last_child':1,'total_derived':4+1}}
assert 'trois périodes' in PAGES[127]
assert 'deux questions les plus fondamentales' in PAGES[129]
assert 'trois êtres les plus proches' in PAGES[131]
assert 'leçons particulières de latin, de grec et de mathématiques' in PAGES[141]
assert 'M., puis de J., puis de S.' in PAGES[143]
assert 'deux grandes forces' in PAGES[145] and 'aux quatre parmi eux' in PAGES[145] and 'cinquième et dernier' in PAGES[145]
REPORT['checks']['typed']={'passed':True,'lists':typed,'qualification':'Literal anchors and list arithmetic only. Authorial psychological, cultural, and historical assertions are not independently validated.'}

expected_scans=set(range(97,146))-{123};assert set(PAGES)==expected_scans
printed={};pencil={}
for scan,text in PAGES.items():
    nums=[int(n) for n in re.findall(r'\\mspage\{(\d+)\}',text)]
    large=[n for n in nums if n>=400]
    if large:assert len(large)==1;printed[scan]=large[0]
    assert scan-1 in nums,(scan,nums)
    pencil[scan]=scan-1
expected_printed={125:465,127:466,129:467,131:468,133:469,135:470,137:471,139:472,141:473,143:480,145:474}
assert printed==expected_printed
earlier_notes=(ROOT.parent/'context/same_cote_84/MPL_84_146-193_notes.md').read_text()
earlier={int(scan):label.strip() for scan,label in re.findall(r'^\| (\d{3}) \| MPL_84_146-193_84_scan\d{3}\.tex \| ([^|]+) \|',earlier_notes,re.M)}
assert len(earlier)==24,len(earlier)
current_labels=set(map(str,printed.values()));earlier_labels=set(earlier.values())
assert not current_labels & earlier_labels
joint=current_labels|earlier_labels
assert len(joint)==35
missing=sorted(set(map(str,range(465,501)))-joint,key=int)
assert missing==['481','485'] and '475 bis' in joint
REPORT['checks']['pagination']={'passed':True,'supplied_scans':len(PAGES),'mathematical_including_cancelled':37,'reused_typed':11,'current_printed_mapping':printed,'earlier_reported_mapping':earlier,'joint_count':35,'ordinary_numbered_joint_count':34,'supplement':'475 bis','missing_ordinary_labels':missing,'qualification':'The earlier24-page mapping is taken only from unreviewed context notes §8.2; no earlier images were inspected.35 is a derived union count, not an authorial total.'}

REPORT['catalog_item_count']=len(CATALOG['items'])
REPORT['per_item']=[{'id':item['id'],'scans':item['scans'],'declared_check':item['check'],'model_result':('verified declared model' if item['check'] in REPORT['checks'] else 'structural/literal inventory only'),'catalog_entry_slots':len(item['entries'])} for item in CATALOG['items']]
REPORT['limitations']=[
 'Every source table/list is catalogued, but a literal inventory is not a completed proof of all its formulas.',
 'No test certifies the arbitrary-base existence of quasi-quadratic norm maps or the questioned F11 lifting.',
 'No general relative degree4/2 claim is made for the nonflat morphism on122.',
 'The scan115 completed involutions and scan132 consistent transition branch are explicitly editorial models.',
 'No source page or frozen combined transcription is written by this script.'
]
(OUT/'recompute_enumerations_output.json').write_text(json.dumps(REPORT,ensure_ascii=False,indent=2)+'\n')
summary=['# Recomputed enumeration checks','',f"Catalog items: {len(CATALOG['items'])}. Source array environments checked: {len(arrays)}. All asserted checks below passed.",'', '| Check | Result |','|---|---|']
for name,result in REPORT['checks'].items():summary.append('| '+name+' | '+('Passed within declared scope' if result['passed'] else 'Failed')+' |')
summary+=['','## Principal counts','', '- Binary triples8; even subgroup4; nonzero even triples3; ordered distinct pairs6.', '- Each of2 parity fibers has4 points and3 bijective pair projections.', '- Three completed involutions pair the4 conjugate labels in3 perfect matchings, covering6 unordered pairs.', '- Rank labels on122 remain8,2,4(!),2,2(!); only the split etale model is verified.', '- The local tensor basis has4 vectors, with4 trace values and4 norm values.', '- The consistent plus-sign transition model has zero cocycle residual; the source’s alternate signs/unprimed second-factor base are reported separately.', '- Current typed pages11; earlier reported typed pages24; disjoint reported union35, missing ordinary labels481/485 and including475bis.','', '## Limits','']+['- '+s for s in REPORT['limitations']]
(OUT/'recompute_enumerations_output.md').write_text('\n'.join(summary)+'\n')
print('PASS: '+', '.join(REPORT['checks']))
print(f"Catalog{len(CATALOG['items'])}; source arrays{len(arrays)}; parity8/4/3; ordered pairs6; joint typed leaves35.")
print(OUT/'recompute_enumerations_output.json')
