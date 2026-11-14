"""Independent E98 residue and finite quotient-coordinate checks.

The Heisenberg check is an algebraic check of the general quotient maps;
it is not substituted for the actual arithmetic source presentation.
"""
from pathlib import Path
from itertools import product
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
explore_path = ROOT / 'research_e98/code/e_global_split7_explore.json'
residue_path = ROOT / 'research_e98/code/e_global_split7_residues.json'
explore = json.loads(explore_path.read_text())
residues = json.loads(residue_path.read_text())
assert residues['input_sha256'] == hashlib.sha256(explore_path.read_bytes()).hexdigest()
labels = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'C1', 'C2']
blocks = [[[int(a) for a in row] for row in explore['coefficient_blocks'][name]]
          for name in labels]
moduli = explore['moduli']
digits = list(product(range(3), repeat=8))
found = set()
checks = 0
for rec in residues['relative_image']:
    v0 = rec['first_digit']
    for index, horizontal in zip(rec['admissible_second_digits'],
                                 rec['all_horizontal_witnesses'], strict=True):
        v = tuple(a + 3*b for a, b in zip(v0, digits[index]))
        assert v not in found
        found.add(v)
        p = [1] + horizontal
        for r, modulus in enumerate(moduli):
            value = sum(v[d]*sum(blocks[d][r][j]*p[j] for j in range(10))
                        for d in range(8))
            assert value % modulus == 0
            checks += 1
cusps = [tuple(int(i == j) for i in range(8)) for j in range(8)]
cusps.append((-1,)*8)
rays = {tuple(a*x % 9 for x in v) for v in cusps for a in range(9)}
assert found == rays
assert len(found) == 73
print('PASS all 73 retained inverse witnesses; 2190 original congruences')
print('PASS the actual relative mod-nine image is exactly the nine cusp lines')

# U_3(Z/9), written (x,y,z) with cross term x*y'.
n = 9
one = (0, 0, 0)
group = list(product(range(n), repeat=3))
def mul(a, b):
    x, y, z = a
    u, v, w = b
    return ((x+u) % n, (y+v) % n, (z+w+x*v) % n)
def inv(a):
    x, y, z = a
    return (-x % n, -y % n, (x*y-z) % n)
def power(a, k):
    out = one
    for _ in range(k):
        out = mul(out, a)
    return out
def J(a):
    x, y, z = a
    return (-x % n, y, -z % n)
fixed = [a for a in group if J(a) == a]
anti = [a for a in group if J(a) == inv(a)]
coordinate = {a: mul(inv(a), J(a)) for a in group}
assert set(coordinate.values()) == set(anti)
for x in anti:
    g = power(x, 4)  # -1/2 mod 9
    assert coordinate[g] == x
    fiber = {a for a in group if coordinate[a] == x}
    assert fiber == {mul(h, g) for h in fixed}
assert len(fixed) == 9 and len(anti) == 81
for x in anti:
    assert len({a for a in anti if a[:2] == x[:2]}) == 9
print('PASS 729 nonabelian coset coordinates, 81 inverse square-root coordinates')
print('PASS the projected anti-fixed map has nine-element central fibers')

result = {
    'status': 'PASS',
    'inputs': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in (explore_path, residue_path)},
    'inverse_witnesses': len(found),
    'original_congruences': checks,
    'relative_mod9_image': sorted(map(list, found)),
    'cusp_ray_comparison': 'exact equality, all nine positive peripheral lines',
    'finite_group': 'U3(Z/9), solely a quotient-coordinate verification',
    'finite_group_order': len(group),
    'fixed_subgroup_order': len(fixed),
    'anti_fixed_coordinates': len(anti),
    'central_projection_fiber_size': 9,
    'arithmetic_transfer': 'proved separately from E56 and Wingberg; not inferred from this finite model',
}
(HERE / 'bc_split7_packets.json').write_text(json.dumps(result, indent=2)+'\n')
