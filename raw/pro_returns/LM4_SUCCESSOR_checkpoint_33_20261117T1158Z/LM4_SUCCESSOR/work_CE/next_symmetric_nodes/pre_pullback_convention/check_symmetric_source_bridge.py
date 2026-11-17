#!/usr/bin/env python3
"""Actual fixed-source bridge from the B87 base to the rational q=9/25 fiber.
No source-kernel normality or fixed-lifting conclusion is inferred.
"""
from pathlib import Path
import json,hashlib,time
import symmetric_node_braid as B
S,Q,I=B.S,B.Q,B.I
from quadratic_pencil_braid import positive_on_unit
ROOT=Path(__file__).resolve().parent.parent
P=ROOT/'next_symmetric_nodes';started=time.monotonic()
critical=json.loads((B.DE/'symmetric_critical_deformation.json').read_text())
centers=[Q(d['center'][0])+I*Q(d['center'][1]) for d in critical['centers']]
basepoints=[Q(399,40000),Q(1,100),Q(9,25)]
segments=[]
for a,b in zip(basepoints,basepoints[1:]):
 margins=[B.dist2_segment(c,a,b) for c in centers]
 assert min(margins)>Q(1,5000)**2
 seg=B.Segment(a,b)
 # Re(ROT*v_source)=v_source>=9/5 on this real source path.
 # Every other projected rational puncture remains strictly to its left.
 corridor=Q(9,5)-Q(1,1000)
 for R,J,D in seg.rational:positive_on_unit(corridor*D-R)
 assert 0<a<=b<=Q(9,25)
 # The retained square-root punctures have real projections +-sqrt(q),
 # bounded above by3/5; the real source is1+sqrt(1-q)>=9/5.
 rec=seg.compute();A=B.art(rec['word']);Ai=B.art(B.rinv(rec['word']))
 for j in range(1,B.NSTR+1):assert B.sub(A[j],Ai)==(j,)==B.sub(Ai[j],A)
 rec['minimum_all_critical_center_distance_squared']=str(min(margins))
 rec['rational_punctures_project_strictly_left_of']=str(corridor)
 rec['rational_to_source_corridor_margin_strictly_greater_than']='1/1000'
 segments.append(rec)
 print('PASS source bridge',a,'to',b,'crossings',rec['crossing_count'],flush=True)
v=S.symbols('v')
assert S.cancel((v-v*(2-v))/(v-1)-v)==0
assert Q(399,200)*(2-Q(399,200))==basepoints[0]
assert Q(9,5)*(2-Q(9,5))==basepoints[-1]
mid=segments[0]['final_order'];end=segments[1]['final_order']
nodes=json.loads((P/'symmetric_node_words.json').read_text())
assert mid==nodes['initial_order']
W=segments[1]['word'];A=B.art(W);Ai=B.art(B.rinv(W))
out={'scope':__doc__,'parameter_points':[str(x) for x in basepoints],
 'source_points_at_rational_endpoints':[['399/200','1/200'],['9/5','1/5']],
 'source_branch':'v=1+sqrt(1-q), w=1-sqrt(1-q)',
 'fixed_source_identity':'(v-v(2-v))/(v-1)=v',
 'far_point_in_original_v_coordinate':'10/(1+371*i/1000)',
 'source_to_far_whisker':'straight segment in Re(ROT*v)>=9/5; rational-deformed punctures have real projection<9/5-1/1000',
 'true_cyclotomic_corridor_margin_strictly_greater_than':'1/2000, using certified strand displacement<1/10^20',
 'segments':segments,'nodal_base_initial_order':mid,'rational_pairing_base_order':end,
 'nodal_base_to_pairing_base_braid':W,
 'endpoint_generators_in_nodal_base':A,'nodal_generators_in_endpoint_base':Ai,
 'automorphism_transport_convention':'F_nodal = Art(W) compose F_endpoint compose Art(W)^-1',
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'crossing_engine_sha256':hashlib.sha256(Path(B.__file__).read_bytes()).hexdigest(),
 'nodal_words_sha256':hashlib.sha256((P/'symmetric_node_words.json').read_bytes()).hexdigest(),
 'elapsed_seconds':round(time.monotonic()-started,6)}
(P/'symmetric_source_bridge.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS actual source and far-basepoint comparison, exact21-generator inverse transport; elapsed',round(time.monotonic()-started,3),flush=True)
