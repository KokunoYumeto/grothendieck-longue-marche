#!/usr/bin/env python3
"""Exact collision-free deformation of the rational B99 base to zeta^2."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / 'work_CE/next_symmetric_nodes/retained_section_kernel_braids.json'
OUTPUT = ROOT / 'work_CE/next_symmetric_nodes/B99_deformation_margin.json'
j = json.loads(INPUT.read_text())
x, y = map(Q, j['base_v'])
eps = Q(1, 10**28)
r = -x
# Re(zeta^2)=-(1+sqrt(5))/4; Im(zeta^2)>0 and |zeta^2|=1.
assert 4*(r-eps)-1 > 0
assert (4*(r-eps)-1)**2 < 5 < (4*(r+eps)-1)**2
assert y-eps > 0
assert (y-eps)**2 < 1-(r+eps)**2
assert 1-(r-eps)**2 < (y+eps)**2

segments = {}
for loop in j['loops']:
    for s in loop['forward_segments'] + loop['local_segments']:
        a, b = tuple(map(Q, s['start'])), tuple(map(Q, s['end']))
        segments[(a, b)] = s
assert len(segments) == 17
checks = []
for a, b in segments:
    delta = tuple(b[i]-a[i] for i in range(2))
    norm = sum(t*t for t in delta)
    for critical in (-1, 0, 1):
        e = (a[0]-critical, a[1])
        parameter = max(Q(0), min(Q(1),
            -sum(e[i]*delta[i] for i in range(2))/norm)) if norm else Q(0)
        distance2 = sum((e[i]+parameter*delta[i])**2 for i in range(2))
        assert distance2 >= Q(1, 10**6)
        checks.append({'start': list(map(str,a)), 'end': list(map(str,b)),
                       'critical': critical, 'parameter': str(parameter),
                       'distance_squared': str(distance2)})
    assert sum(t*t for t in a) < 4 and sum(t*t for t in b) < 4

# The initial cut basis is constant throughout the endpoint deformation.
rho = Q(371,1000)
points = [(Q(0),Q(0)),(Q(1),Q(0)),(x,y),(x*x-y*y,2*x*y)]
projection = [a-rho*b for a,b in points]
order = j['initial_order']
gaps = [projection[order[i+1]]-projection[order[i]] for i in range(3)]
assert all(g > Q(1,3) for g in gaps)

result = {
    'status': 'PASS', 'input_sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'cyclotomic_coordinate_error_bound': str(eps),
    'cyclotomic_euclidean_error_bound_strict': str(2*eps),
    'segment_count': len(segments), 'distance_checks': checks,
    'minimum_distance_squared': '1/1000000',
    'initial_adjacent_projection_gaps': list(map(str,gaps)),
    'initial_gap_lower_bound_strict': '1/3',
    'argument': 'Only the initial endpoint moves. Linear interpolation moves every affected v-segment point by <2e-28. All v-paths avoid the complete collision set {0,1,-1} by >=1/1000, so the polynomial q configurations remain isotopic. The initial cut ordering is unchanged by the >1/3 projection gaps. The same far point remains outside since |v|<2 and |q punctures|<4.'
}
OUTPUT.write_text(json.dumps(result, indent=2)+'\n')
print('PASS exact zeta^2 coordinate enclosure, all 17 segments / 51 distance checks,')
print('v-critical margin >=1/1000, deformation <2e-28, initial cut gaps >1/3.')
