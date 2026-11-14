"""Staged exact nine-strand source certificate for the F22 membership map.

All source paths use explicitly listed rational square centers.  Exact
number-field distance and Rouche inequalities certify their punctures;
Bernstein subdivision certifies every nine-strand crossing.  No floating
point arithmetic or discovery output is read by this producer.  This
file is research staging until the entire geometric and based-group
comparison has passed independent review.
"""

from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from functools import cmp_to_key
import hashlib
import json

import cross_divisor_monodromy_f20 as gr

nf, C, R = gr.nf, gr.C, gr.R
BASE, ZETA, ROOTS = C(2, 2), gr.ZETA, gr.ROOTS
HALF = Q(1, 10000)
ROOT_RADIUS = HALF / 2
ERROR_BOUND = Q(1, 100000)
PROJECTION_OFFSET = Q(1, 10**14)
POSITIVE_REFERENCE, NEGATIVE_REFERENCE = C(8, 3), C(12, 6)
RAW = [
    ("old0", 0, 0),
    ("old_1_0", 1000000, 0),
    ("old_1_1", 309017, 951057),
    ("old_1_2", -809017, 587785),
    ("old_1_3", -809017, -587785),
    ("old_1_4", 309017, -951057),
    ("old_-1_0", -1000000, 0),
    ("old_-1_1", -309017, -951057),
    ("old_-1_2", 809017, -587785),
    ("old_-1_3", 809017, 587785),
    ("old_-1_4", -309017, 951057),
    ("cross_0_1_1", 882644, 1077509),
    ("cross_0_1_-1", -882644, -1077509),
    ("cross_0_-1_1", 454951, 555393),
    ("cross_0_-1_-1", -454951, -555393),
    ("cross_2_1_1", 80730, -1390528),
    ("cross_2_1_-1", -80730, 1390528),
    ("cross_2_-1_1", 41611, -716735),
    ("cross_2_-1_-1", -41611, 716735),
    ("cross_3_1_1", 1260728, -1131556),
    ("cross_3_1_-1", -1260728, 1131556),
    ("cross_3_-1_1", 439300, -394290),
    ("cross_3_-1_-1", -439300, 394290),
    ("cross_4_1_1", 1685063, 174411),
    ("cross_4_1_-1", -1685063, -174411),
    ("cross_4_-1_1", 587159, 60773),
    ("cross_4_-1_-1", -587159, -60773),
]
CENTERS = [C(Q(x, 1000000), Q(y, 1000000)) for _, x, y in RAW]


def norm2(z):
    return (z*z.conjugate()).re


def certify_boxes():
    rows = []
    directions = []
    for i, ((label, _, _), center) in enumerate(zip(RAW, CENTERS)):
        assert (BASE.re-center.re-HALF).sign() > 0
        assert (BASE.im-center.im-HALF).sign() > 0
        direction = center+C(HALF, HALF)-BASE
        directions.append(direction)
        if label.startswith("old"):
            if label == "old0":
                root = C(0)
            else:
                _, sign, j = label.split("_")
                root = int(sign)*ROOTS[int(j)]
            clearance = ROOT_RADIUS**2-norm2(center-root)
            assert clearance.sign() > 0
            proof = {"type": "exact_known_root_distance", "clearance": clearance.encoded()}
        else:
            _, j, eps, _ = label.split("_")
            u = ROOTS[int(j)]
            square = u*(2*ZETA-u) if int(eps) == 1 else ZETA*u*u*gr.cinv(2*u-ZETA)
            norm_margin = norm2(center)-Q(1, 4)
            error_margin = ERROR_BOUND**2-norm2(center*center-square)
            assert norm_margin.sign() > 0 and error_margin.sign() > 0
            assert ROOT_RADIUS**2+ERROR_BOUND < ROOT_RADIUS
            proof = {
                "type": "exact_Rouche_one_simple_quadratic_root",
                "square": square.encoded(),
                "center_norm_squared_minus_one_quarter": norm_margin.encoded(),
                "squared_error_margin": error_margin.encoded(),
                "root_disk_radius": str(ROOT_RADIUS),
                "linear_lower_bound": str(ROOT_RADIUS),
                "remainder_upper_bound": str(ROOT_RADIUS**2+ERROR_BOUND),
            }
        clearance_rows = []
        end = center+C(HALF, HALF)
        denominator = norm2(direction)
        for j, other in enumerate(CENTERS):
            if j == i:
                continue
            product = (other-BASE)*direction.conjugate()
            t = product.re/denominator
            if t.sign() < 0:
                distance = norm2(other-BASE)
                location = "start"
            elif (t-1).sign() > 0:
                distance = norm2(other-end)
                location = "end"
            else:
                distance = product.im*product.im/denominator
                location = "interior"
            margin = distance-2*HALF*HALF
            assert margin.sign() > 0
            clearance_rows.append({"other": j, "nearest": location,
                                   "squared_clearance": margin.encoded()})
        rows.append({"label": label, "center": center.encoded(),
                     "root_proof": proof, "tail_clearances": clearance_rows})
    pairs = []
    for i, j in combinations(range(len(CENTERS)), 2):
        square_margin = norm2(CENTERS[i]-CENTERS[j])-8*HALF*HALF
        tail_cross = (directions[i]*directions[j].conjugate()).im
        assert square_margin.sign() > 0 and tail_cross.sign() != 0
        pairs.append({"pair": [i, j], "square_separation": square_margin.encoded(),
                      "tail_direction_cross": tail_cross.encoded()})
    return {"half_side": str(HALF), "root_disk_radius": str(ROOT_RADIUS),
            "squares": rows, "pairwise": pairs,
            "conclusion": "Twenty-seven isolated punctures with disjoint square meridians and an embedded common-base star."}


def configurations(start, end):
    s = [start, end-start]
    points = [([C(0)], [C(1)]), ([C(1)], [C(1)])]
    for root in ROOTS:
        numerator, denominator = gr.psub([root], s), gr.padd([root], s)
        points.append((gr.pmul(numerator, numerator), gr.pmul(denominator, denominator)))
    numerator, denominator = gr.psub([ZETA], s), gr.padd([ZETA], s)
    points += [(numerator, denominator), (gr.pscale(numerator, -1), denominator)]
    return points


def fixed_points():
    values = [C(0), C(1)]
    for root in ROOTS:
        c = (root-BASE)*gr.cinv(root+BASE)
        values.append(c*c)
    return values


def transport_configurations():
    fixed = [([point], [C(1)]) for point in fixed_points()]
    a = (ZETA-BASE)*gr.cinv(ZETA+BASE)
    first = fixed + [([POSITIVE_REFERENCE, a-POSITIVE_REFERENCE], [C(1)]),
                     ([NEGATIVE_REFERENCE], [C(1)])]
    second = fixed + [([a], [C(1)]),
                      ([NEGATIVE_REFERENCE, -a-NEGATIVE_REFERENCE], [C(1)])]
    return [first, second]


def positive_polynomial(polynomial):
    todo = [(Q(0), Q(1), gr.bernstein(polynomial))]
    leaves = []
    nodes = 0
    while todo:
        a, b, coefficients = todo.pop()
        nodes += 1
        assert nodes < 100000
        signs = gr.signs(coefficients)
        if all(sign > 0 for sign in signs):
            leaves.append({"interval": [str(a), str(b)], "bernstein_signs": signs})
            continue
        assert gr.peval(polynomial, a).sign() > 0
        assert gr.peval(polynomial, b).sign() > 0
        left, right = gr.split(coefficients)
        midpoint = (a+b)/2
        todo.extend([(a, midpoint, left), (midpoint, b, right)])
    return {"nodes": nodes, "positive_leaves": leaves}


def norm_polynomial(polynomial):
    real = [z.re for z in polynomial]
    imag = [z.im for z in polynomial]
    return gr.padd(gr.pmul(real, real), gr.pmul(imag, imag))


def certify_projection_perturbation(configuration):
    checks = []
    for i, j in combinations(range(len(configuration)), 2):
        ni, di = configuration[i]
        nj, dj = configuration[j]
        numerator = gr.pscale(gr.psub(gr.pmul(ni, dj), gr.pmul(nj, di)), gr.PROJECTION)
        denominator = gr.pmul(di, dj)
        displacement = PROJECTION_OFFSET*(i*i-j*j)
        margin = gr.psub(norm_polynomial(numerator),
                        gr.pscale(norm_polynomial(denominator), displacement*displacement))
        checks.append({"pair": [i, j], "projected_offset_difference": str(displacement),
                       "positive_margin_polynomial": [x.encoded() for x in margin],
                       **positive_polynomial(margin)})
    inverse_projection = gr.cinv(gr.PROJECTION)
    perturbed = [(gr.padd(n, gr.pscale(d, inverse_projection*(PROJECTION_OFFSET*i*i))), d)
                 for i, (n, d) in enumerate(configuration)]
    return perturbed, checks


def segment(configuration, label):
    configuration, perturbation_checks = certify_projection_perturbation(configuration)
    n = len(configuration)
    pairs, events, endpoint_signs = [], [], {}
    for i, j in combinations(range(n), 2):
        real, height = gr.projected_difference(configuration, i, j)
        s0, s1 = gr.peval(real, Q(0)).sign(), gr.peval(real, Q(1)).sign()
        assert s0 and s1, (label, i, j, "projected endpoint")
        endpoint_signs[i, j] = (s0, s1)
        roots, tree = gr.isolate(real)
        record = {"pair": [i, j], "projected_numerator": [x.encoded() for x in real],
                  "height_numerator": [x.encoded() for x in height],
                  "endpoint_signs": [s0, s1], **tree, "roots": []}
        for root in roots:
            while root["hi"]-root["lo"] > Q(1, 2**36):
                gr.refine(root)
            for _ in range(100):
                heights = gr.bernstein(height, root["lo"], root["hi"])
                derivative = [(b-a)*(len(root["bernstein"])-1)/(root["hi"]-root["lo"])
                              for a, b in zip(root["bernstein"], root["bernstein"][1:])]
                hs, ds = gr.one_sign(heights), gr.one_sign(derivative)
                if hs is not None and ds is not None:
                    break
                gr.refine(root)
            else:
                raise AssertionError((label, i, j, "height or derivative"))
            root.update({"pair": (i, j), "height_sign": hs,
                         "derivative_sign": ds, "record": record})
            events.append(root)
        pairs.append(record)
    for _ in range(100):
        events.sort(key=lambda e: e["lo"])
        bad = [i for i in range(len(events)-1) if events[i]["hi"] >= events[i+1]["lo"]]
        if not bad:
            break
        for i in sorted(set(bad+[i+1 for i in bad])):
            gr.refine(events[i])
    else:
        raise AssertionError((label, "crossing times"))
    def comparison(i, j, endpoint):
        return endpoint_signs[i, j][endpoint] if i < j else -endpoint_signs[j, i][endpoint]
    initial = sorted(range(n), key=cmp_to_key(lambda i, j: comparison(i, j, 0)))
    final = sorted(range(n), key=cmp_to_key(lambda i, j: comparison(i, j, 1)))
    order, word = initial[:], []
    for event in events:
        i, j = event["pair"]
        ii, jj = order.index(i), order.index(j)
        assert abs(ii-jj) == 1, (label, event)
        letter = (min(ii, jj)+1)*(event["height_sign"] if ii < jj else -event["height_sign"])
        word.append(letter)
        order[ii], order[jj] = order[jj], order[ii]
        event["record"]["roots"].append({
            "interval": [str(event["lo"]), str(event["hi"])],
            "bernstein_signs": gr.signs(event["bernstein"]),
            "height_sign": event["height_sign"],
            "derivative_sign": event["derivative_sign"], "braid_letter": letter})
    assert order == final
    return {"label": label, "initial_order": initial, "final_order": final,
            "crossing_count": len(events), "braid": nf.red(word), "pair_checks": pairs,
            "collision_free_projection_perturbation": perturbation_checks}


def main():
    producer = Path(__file__).resolve()
    folder = producer.with_name("full_cross_source_stage")
    folder.mkdir(exist_ok=True)
    starting_signs = nf.SIGN_COUNT
    basis = certify_boxes()
    (folder/"source_basis.json").write_text(json.dumps(basis, indent=2)+"\n")
    transport = [segment(c, f"reference_transport_{i}")
                 for i, c in enumerate(transport_configurations())]
    assert transport[0]["initial_order"][-2:] == [7, 8]
    reference_word = nf.red(transport[0]["braid"]+transport[1]["braid"])
    (folder/"reference_transport.json").write_text(json.dumps(transport, indent=2)+"\n")
    initial_order = transport[0]["initial_order"]
    records = []
    total_segments = len(transport)
    total_crossings = sum(row["crossing_count"] for row in transport)
    for i, (raw, center) in enumerate(zip(RAW, CENTERS)):
        corner = center+C(HALF, HALF)
        route = [BASE, corner, center+C(-HALF, HALF), center+C(-HALF, -HALF),
                 center+C(HALF, -HALF), corner]
        pieces = [segment(configurations(a, b), f"{raw[0]}_segment_{j}")
                  for j, (a, b) in enumerate(zip(route, route[1:]))]
        loop = [letter for piece in pieces for letter in piece["braid"]]
        loop += nf.wi(pieces[0]["braid"])
        based = nf.red(reference_word+loop+nf.wi(reference_word))
        payload = {"index": i, "label": raw[0], "reference_initial_order": initial_order,
                   "route": [c.encoded() for c in route], "based_braid": based,
                   "segments": pieces}
        output = folder/f"meridian_{i:02d}.json"
        output.write_text(json.dumps(payload, indent=2)+"\n")
        records.append({"index": i, "label": raw[0], "based_braid": based,
                        "file": output.name, "sha256": hashlib.sha256(output.read_bytes()).hexdigest()})
        total_segments += len(pieces)
        total_crossings += sum(piece["crossing_count"] for piece in pieces)
        print(json.dumps({"completed": i, "label": raw[0], "braid_length": len(based),
                          "forward_crossings": sum(piece["crossing_count"] for piece in pieces)}), flush=True)
    summary = {
        "status": "PASS_GEOMETRIC_STAGE_PENDING_GROUP_AUDIT",
        "producer_sha256": hashlib.sha256(producer.read_bytes()).hexdigest(),
        "source_basepoint": BASE.encoded(), "half_side": str(HALF),
        "projection_perturbation": {"epsilon": str(PROJECTION_OFFSET),
                                     "weights": [i*i for i in range(9)],
                                     "direction": gr.cinv(gr.PROJECTION).encoded()},
        "reference_initial_order": initial_order,
        "reference_word": reference_word, "meridians": records,
        "certified_forward_segments": total_segments,
        "projected_pair_checks": 36*total_segments,
        "certified_crossings": total_crossings,
        "number_field_sign_calls": nf.SIGN_COUNT-starting_signs,
    }
    output = folder/"summary.json"
    output.write_text(json.dumps(summary, indent=2)+"\n")
    print(json.dumps({k: v for k, v in summary.items()
                      if k not in ("meridians", "reference_word")}, indent=2), flush=True)


if __name__ == "__main__":
    main()
