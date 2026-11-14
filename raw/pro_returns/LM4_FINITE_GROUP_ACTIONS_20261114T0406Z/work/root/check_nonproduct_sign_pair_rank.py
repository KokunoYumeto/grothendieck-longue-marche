#!/usr/bin/env python3
"""Root replay of every localized sign-pair row operation with independent arithmetic.

No producer or producer-helper module is imported. The original-word audit is
bound separately; this checker verifies the full coefficient transport and all
four exact row certificates from the specified original-row input.
"""
from pathlib import Path
from collections import defaultdict
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[2]
SOURCE='work/part_a/code/affine_rank_one_certificate_stage_output.json'
CERT='work/part_a/code/affine_nonproduct_sign_pair_rank_certificate_stage_output.json'
EXPECTED='b8ef6433853cae33e767d0f450729df2ded1ee0976cb9bfc0d0823502f4f5a36'
Z=(0,)*7
E=[tuple(int(i==j) for i in range(7)) for j in range(7)]
ONE={Z:1}
counts=defaultdict(int)
def check(kind,condition):
    assert condition,kind
    counts[kind]+=1
def tidy(value):return {e:c for e,c in value.items() if c}
def parse(value):
    result=defaultdict(int)
    for c,e in value:result[tuple(e)]+=c
    return tidy(result)
def plus(*values):
    result=defaultdict(int)
    for value in values:
        for e,c in value.items():result[e]+=c
    return tidy(result)
def negative(value):return {e:-c for e,c in value.items()}
def shift(value,by):return {tuple(a+b for a,b in zip(e,by)):c for e,c in value.items()}
def times(left,right):
    result=defaultdict(int)
    for a,c in left.items():
        for b,d in right.items():result[tuple(x+y for x,y in zip(a,b))]+=c*d
    return tidy(result)
def delta(j):return {E[j]:1,Z:-1}
def divide_difference(value,j):
    """Synthetic division from the constant coefficient upwards, by fibers."""
    groups=defaultdict(dict)
    for e,c in value.items():
        assert e[j]>=0
        rest=e[:j]+e[j+1:]
        groups[rest][e[j]]=c
    result={}
    for rest,coefficients in groups.items():
        total=0
        for n in range(max(coefficients)):
            total+=coefficients.get(n,0)
            if total:result[rest[:j]+(n,)+rest[j:]]=-total
        total+=coefficients.get(max(coefficients),0)
        assert total==0
    check('exact_difference_division_inverse',times(result,delta(j))==value)
    return result
def normalize(value,operation,active):
    original=value
    value=shift(value,tuple(operation['shift']))
    for j,key in [(0,'R_minus_one_divisions'),(active,'active_difference_divisions')]:
        for _ in range(operation[key]):value=divide_difference(value,j)
    denominator=2**operation['two_divisions']
    assert all(c%denominator==0 for c in value.values())
    value={e:c//denominator for e,c in value.items()}
    restored={e:c*denominator for e,c in value.items()}
    for j,key in [(0,'R_minus_one_divisions'),(active,'active_difference_divisions')]:
        for _ in range(operation[key]):restored=times(restored,delta(j))
    restored=shift(restored,tuple(-n for n in operation['shift']))
    check('normalization_forward_inverse',restored==original)
    return value
def unit(value,description,active):
    normalized=normalize(value,description['normalization'],active)
    expected={tuple(description['final_monomial']):description['sign']}
    check('recorded_localized_unit',normalized==expected and description['sign'] in [-1,1])
def specialize(value,indices):
    result=defaultdict(int)
    for e,c in value.items():result[tuple(0 if j in indices else n for j,n in enumerate(e))]+=c
    return tidy(result)
def matmul(left,right):
    return [[plus(*(times(left[i][k],right[k][j]) for k in range(len(right))))
             for j in range(len(right[0]))] for i in range(len(left))]
def identity(n,diagonal=ONE):return [[diagonal if i==j else {} for j in range(n)] for i in range(n)]
def binding(name):
    raw=(ROOT/name).read_bytes()
    return {'path':name,'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

assert binding(CERT)['sha256']==EXPECTED
source=json.loads((ROOT/SOURCE).read_text())
certificate=json.loads((ROOT/CERT).read_text())
check('source_input_hash',binding(SOURCE)['sha256']==certificate['input_sha256'])
helper_bindings=[]
for name,digest in certificate['helper_bindings'].items():
    p=Path(name);name=str(p.relative_to(ROOT)) if p.is_absolute() else name
    check('producer_helper_hash_only_no_import',binding(name)['sha256']==digest)
    helper_bindings.append(binding(name))
rows=[]
assert len(source['source_rows'])==64 and len(source['source_row_labels'])==64
for original in source['source_rows']:
    even,odd=[],[]
    for serialized in original:
        value=parse(serialized)
        A,B=defaultdict(int),defaultdict(int)
        for e,c in value.items():
            power,parity=divmod(e[0],2)
            (B if parity else A)[(power,)+e[1:]]+=c
        A,B=tidy(A),tidy(B)
        restored=plus({(2*e[0],)+e[1:]:c for e,c in A.items()},
                      {(2*e[0]+1,)+e[1:]:c for e,c in B.items()})
        check('original_Laurent_even_odd_bijection',restored==value)
        even.append(A);odd.append(B)
    relation=plus(negative(odd[0]),even[0],*(times(odd[j],delta(j)) for j in range(1,7)))
    check('actual_principal_line_annihilation',not relation)
    rows.append(odd+even[1:])

# Coordinate order: x1,...,x7,y2,...,y7,lambda=y1.
forward=identity(14)
inverse=identity(14)
for j in range(7):
    correction=ONE if j==0 else negative(delta(j))
    forward[j][13]=correction
    inverse[j][13]=negative(correction)
check('principal_gauge_forward_inverse',matmul(forward,inverse)==identity(14))
check('principal_gauge_inverse_forward',matmul(inverse,forward)==identity(14))
# M takes (c,cprime) to (r(c-cprime),c+cprime). Its inverse numerator is N.
formal_r={E[0]:1}
M=[[formal_r,negative(formal_r)],[ONE,ONE]]
N=[[ONE,formal_r],[negative(ONE),formal_r]]
diagonal={E[0]:2}
check('paired_coordinate_inverse_numerator_left',matmul(M,N)==identity(2,diagonal))
check('paired_coordinate_inverse_numerator_right',matmul(N,M)==identity(2,diagonal))

chart_records=[]
assert [(x['active_deleted_index_zero_based'],x['specialized_to_one']) for x in certificate['charts']]==[(3,[]),(4,[3]),(5,[3,4]),(6,[3,4,5])]
for chart in certificate['charts']:
    active=chart['active_deleted_index_zero_based']
    current=[[specialize(p,chart['specialized_to_one']) for p in row] for row in rows]
    pivots=chart['pivots']
    positions={p['row']:i for i,p in enumerate(pivots)}
    last_position=-1
    maximum_terms=0
    for number,operation in enumerate(chart['operations']):
        row=operation['row']
        if operation['operation']=='normalize':
            check('initial_normalization_order',number<64 and row==number)
            raw=current[row]
        else:
            assert number>=64 and operation['operation']=='eliminate_then_normalize'
            pivot,column=operation['pivot_row'],operation['column_zero_based']
            position=positions[pivot]
            check('pivot_operation_order',position>=last_position)
            last_position=position
            check('previous_pivot_row_never_modified',row not in positions or positions[row]>position)
            P,C=current[pivot][column],current[row][column]
            check('exact_recorded_pivot_coefficient',P==parse(operation['pivot_coefficient']))
            check('exact_recorded_old_coefficient',C==parse(operation['old_coefficient']))
            raw=[plus(times(P,x),negative(times(C,y))) for x,y in zip(current[row],current[pivot])]
            check('eliminated_column_is_zero',not raw[column])
        current[row]=[normalize(p,operation,active) for p in raw]
        maximum_terms=max(maximum_terms,sum(len(p) for p in current[row]))
    used_columns=[]
    for pivot in pivots:
        row,column=pivot['row'],pivot['column_zero_based']
        check('original_source_row_label',pivot['label']==source['source_row_labels'][row])
        check('triangular_previous_pivot_columns_zero',all(not current[row][j] for j in used_columns))
        coefficient=current[row][column]
        check('final_pivot_matches_record',coefficient==parse(pivot['coefficient']))
        unit(coefficient,pivot['unit'],active)
        used_columns.append(column)
    for row in chart['remaining_rows']:
        check('complete_remaining_row_identity',current[row['row']]==[parse(x) for x in row['coefficients']])
    block=chart['terminal_two_by_two_block']
    if block is not None:
        rr=block['rows'];cc=block['columns_zero_based']
        entries=[[current[i][j] for j in cc] for i in rr]
        check('terminal_block_entries',entries==[[parse(x) for x in row] for row in block['entries']])
        determinant=plus(times(entries[0][0],entries[1][1]),negative(times(entries[0][1],entries[1][0])))
        check('terminal_determinant',determinant==parse(block['determinant']))
        unit(determinant,block['unit'],active)
        adjugate=[[parse(x) for x in row] for row in block['adjugate']]
        check('terminal_adjugate_left',matmul(adjugate,entries)==identity(2,determinant))
        check('terminal_adjugate_right',matmul(entries,adjugate)==identity(2,determinant))
        coordinates=matmul(adjugate,[current[i] for i in rr])
        check('terminal_full_coordinate_rows',coordinates==[[parse(x) for x in row] for row in block['resulting_coordinate_rows']])
        check('terminal_exact_coordinate_support',coordinates==[[determinant if j==k else {} for j in range(13)] for k in cc])
        check('terminal_recorded_row_order_and_sign',rr==[35,51] and determinant=={(0,2,1,0,0,0,0):-1})
        swap=[[{},ONE],[ONE,{}]]
        swapped=matmul(swap,entries)
        reversed_det=plus(times(swapped[0][0],swapped[1][1]),negative(times(swapped[0][1],swapped[1][0])))
        check('explicit_row_swap_determinant_transport',reversed_det==negative(determinant))
    check('full_rank_thirteen_count',len(pivots)+(2 if block else 0)==13==chart['pivot_count'])
    chart_records.append({'active_deleted_index_zero_based':active,
        'specialized_to_one':chart['specialized_to_one'],'operations_checked':len(chart['operations']),
        'single_pivots':len(pivots),'terminal_block_rows':block['rows'] if block else None,
        'full_rank':13,'maximum_terms_in_one_replayed_row':maximum_terms})

result={'status':'PASS_ROOT_INDEPENDENT_COMPLETE_SIGN_PAIR_ROW_REPLAY',
 'producer':binding(str(Path(__file__).relative_to(ROOT))),
 'input_bindings':[binding(SOURCE),binding(CERT),*helper_bindings],
 'producer_or_helper_imports':[],
 'check_counts':dict(sorted(counts.items())),'total_exact_checks':sum(counts.values()),
 'charts':chart_records,
 'accepted_divisors':['Character monomials including R','2','R-1','The active deleted character minus1'],
 'coordinate_inverse':'(x,y)=(r(c-cprime),c+cprime); c=(y+x/r)/2, cprime=(y-x/r)/2. The gauge adds y1 to x1, subtracts (chi_j-1)y1 from xj for j>1, and records lambda=y1; the inverse restores those terms.',
 'terminal_row_order':'The serialized [35,51] determinant is -s^2*t. Left multiplication by the explicit row-swap matrix sends it to the displayed [51,35] order with determinant +s^2*t.',
 'scope':'Complete exact source-row coefficient and localized-operation audit. Original negative braid reconstruction is a separately bound audit, not silently assumed to have been re-executed here. No general many-factor Frobenius conclusion is asserted.'}
output=Path(__file__).with_name('check_nonproduct_sign_pair_rank_output.json')
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'total_exact_checks':result['total_exact_checks'],
                  'charts':chart_records,'output':binding(str(output.relative_to(ROOT)))},indent=2))
