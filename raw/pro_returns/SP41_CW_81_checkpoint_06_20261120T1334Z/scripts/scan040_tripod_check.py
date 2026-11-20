"""Exact finite certificate for the six oriented cuts of the four-vertex tripod.

No OCR, outside sources, symbolic guessing or general theorem proving.
The written claim and the sweep identification are collated separately against ink.
"""
from pathlib import Path
import datetime,itertools,json
w=Path(__file__).resolve().parents[1]
U=frozenset(range(4))
labels=['1L','1R','2L','2R','3L','3R']
sets={f'{i}{side}':(frozenset([i]) if side=='L' else U-{i}) for i in (1,2,3) for side in ('L','R')}
graph_edges=[frozenset((0,i)) for i in (1,2,3)]
def component_after_cut(i,start):
 remaining=[e for e in graph_edges if e!=frozenset((0,i))]
 seen={start};frontier=[start]
 while frontier:
  vertex=frontier.pop()
  for e in remaining:
   if vertex in e:
    for neighbour in e-seen:
     seen.add(neighbour);frontier.append(neighbour)
 return frozenset(seen)
components={f'{i}{side}':component_after_cut(i,i if side=='L' else 0) for i in (1,2,3) for side in ('L','R')}
assert components==sets
edge={label:int(label[0]) for label in labels}
sigma={label:label[0]+('R' if label[1]=='L' else 'L') for label in labels}
inverse={tuple(sorted(v)):k for k,v in sets.items()}
assert len(inverse)==6
assert all(inverse[tuple(sorted(sets[k]))]==k for k in labels)
assert all(sets[inverse[tuple(sorted(v))]]==v for v in sets.values())
lt=lambda a,b:sets[a]<sets[b]
le=lambda a,b:sets[a]<=sets[b]
comp=lambda a,b:le(a,b) or le(b,a)
rel26=lambda a,b:edge[a]!=edge[b] and not(sets[a]&sets[sigma[b]])
pairs=list(itertools.product(labels,repeat=2))
triples=list(itertools.product(labels,repeat=3))
assert all(sigma[sigma[a]]==a and sigma[a]!=a and sets[sigma[a]]==U-sets[a] for a in labels)
assert all(not lt(a,a) for a in labels)
assert all(not(lt(a,b) and lt(b,a)) for a,b in pairs)
assert all(not(lt(a,b) and lt(b,c)) or lt(a,c) for a,b,c in triples)
source_mapping=[{'left':a,'right':b,'source_26_relation':rel26(a,b),'strict_inclusion':lt(a,b),'equal':rel26(a,b)==lt(a,b)} for a,b in pairs]
assert all(r['equal'] for r in source_mapping)
clauses=[{'x':a,'y':b,'comparable_xy':comp(a,b),'comparable_sigma_x_y':comp(sigma[a],b),'a_equivalence':comp(a,b)==(not comp(sigma[a],b)),'b_implication':not lt(a,b) or lt(sigma[b],sigma[a])} for a,b in pairs]
assert all(r['a_equivalence'] and r['b_implication'] for r in clauses)
def chain(items):return all(comp(a,b) for a,b in itertools.product(items,repeat=2))
cones=[]
for a in labels:
 upper=[b for b in labels if le(a,b)];lower=[b for b in labels if le(b,a)]
 cones.append({'x':a,'upper':upper,'upper_is_chain':chain(upper),'lower':lower,'lower_is_chain':chain(lower)})
x,y,z='1L','2R','3R'
assert lt(x,y) and lt(x,z) and not comp(y,z)
assert lt(sigma[y],z) and lt(sigma[z],y)
assert not lt(sigma[z],x)
assert not chain([b for b in labels if le(x,b)])
lower_x='1R'
assert le('2L',lower_x) and le('3L',lower_x) and not comp('2L','3L')
intervals=[{'lower':a,'upper':b,'members':[c for c in labels if le(a,c) and le(c,b)],'is_chain':chain([c for c in labels if le(a,c) and le(c,b)])} for a,b in pairs if le(a,b)]
assert len(intervals)==12 and all(i['is_chain'] for i in intervals)
cert={
'certificate_id':'SP41-scan040-tripod-finite-certificate',
'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
'source_statement':'Scan040 proposition: the two principal upper/lower sets are totally ordered.',
'sweep_row':'SA01-K81-02',
'vertices':sorted(U),'edges':[[0,1],[0,2],[0,3]],
'construction':'For edge 0-i, delete that edge in this explicitly listed graph. The component containing i is iL; the component containing 0 is iR.',
'component_bijection':[{'oriented_cut':a,'hemisphere':sorted(sets[a]),'inverse_oriented_cut':inverse[tuple(sorted(sets[a]))],'edge_index':edge[a],'sigma':sigma[a]} for a in labels],
'graph_component_checks':{'method':'Traverse the remaining two graph edges from each selected endpoint after deleting edge 0-i.','computed_components':{a:sorted(components[a]) for a in labels},'all_six_equal_displayed_subsets':True},
'bijection_verification':'The six displayed sets are distinct. Both explicit inverse identities were checked on all six entries.',
'order_definition':'a<b means proper subset between the displayed finite subsets; a<=b means subset; comparable means a<=b or b<=a, including equality.',
'source26_to_inclusion_correspondence':source_mapping,
'clause_28_pair_checks':clauses,
'finite_order_checks':{'irreflexive_6_entries':True,'asymmetric_36_pairs':True,'transitive_216_triples':True,'sigma_fixed_point_free_involution_6_entries':True,'a_equivalence_36_pairs':True,'b_implication_36_pairs':True},
'principal_sets':cones,
'upper_failure':{'x':x,'x_set':sorted(sets[x]),'y':y,'y_set':sorted(sets[y]),'z':z,'z_set':sorted(sets[z]),'x_lt_y':True,'x_lt_z':True,'y_z_comparable':False,'y_minus_z':sorted(sets[y]-sets[z]),'z_minus_y':sorted(sets[z]-sets[y])},
'lower_failure':{'x':lower_x,'x_set':sorted(sets[lower_x]),'y':'2L','z':'3L','y_set':[2],'z_set':[3],'y_le_x':True,'z_le_x':True,'y_z_comparable':False},
'last_line_related_values':{'sigma_y':sigma[y],'sigma_y_set':sorted(sets[sigma[y]]),'sigma_y_lt_z':True,'sigma_z':sigma[z],'sigma_z_set':sorted(sets[sigma[z]]),'sigma_z_lt_y':True,'sigma_z_lt_x':False},
'intervals_in_this_specific_example':intervals,
'outcome':'The explicit six-element structure passes the enumerated order, involution and written clause (28) checks with inclusion comparability. Its principal upper set at 1L and principal lower set at 1R each contain two incomparable entries. This concrete certificate refutes the total-order assertion for this structure.',
'limits':'No general refined theorem or full 18,247-tree sweep was verified. The sweep mentions c81checks.py, which is absent from the supplied package. No continuation of the unfinished manuscript operand is inferred from this certificate.'
}
p=w/'validation/scan040_tripod_certificate.json';p.write_text(json.dumps(cert,ensure_ascii=False,indent=2))
print(json.dumps({'certificate':str(p),'oriented_cuts':6,'source26_comparisons':36,'clause28_pairs':36,'transitivity_triples':216,'intervals':len(intervals),'upper_failure':cert['upper_failure'],'lower_failure':cert['lower_failure']}))
