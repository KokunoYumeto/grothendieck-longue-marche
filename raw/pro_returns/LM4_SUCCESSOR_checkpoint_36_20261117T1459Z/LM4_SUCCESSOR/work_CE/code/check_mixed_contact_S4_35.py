"""One prescribed actual one-sided free-fiber S4 separation; no target search."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "work_CE/next_symmetric_nodes/one_sided_m_normal_form26.json"
TARGET = ROOT / "work_CE/mixed_contact_S4_certificate35.json"


def red(word):
    out = []
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return out


def inv(word):
    return [-letter for letter in reversed(word)]


def mul(*words):
    return red([letter for word in words for letter in word])


def sub(word, images):
    return red([letter for x in word
                for letter in (images[abs(x)] if x > 0 else inv(images[abs(x)]))])


def compose(p, q):
    return tuple(p[q[i] - 1] for i in range(4))


def inverse(p):
    return tuple(p.index(i) + 1 for i in range(1, 5))


ID = (1, 2, 3, 4)


def transposition(a, b):
    out = list(ID)
    out[a - 1], out[b - 1] = out[b - 1], out[a - 1]
    return tuple(out)


def evaluate(word, images):
    value = ID
    for letter in word:
        image = images[abs(letter)]
        value = compose(value, image if letter > 0 else inverse(image))
    return value


def main():
    assert not TARGET.exists()
    basis = json.loads(INPUT.read_text())
    raw_path = ROOT / basis["input"]
    raw_bytes = raw_path.read_bytes()
    assert hashlib.sha256(raw_bytes).hexdigest() == basis["input_sha256"]
    raw = json.loads(raw_bytes)
    to_old = {int(k): v for k, v in basis["new_to_old"].items()}
    to_new = {int(k): v for k, v in basis["old_to_new"].items()}
    signed = {}
    for name in ("m", "m_inverse"):
        old_action = {int(k): v for k, v in raw["all_four_signed_free7_source_actions"][name].items()}
        signed[name] = {i: sub(sub(to_old[i], old_action), to_new) for i in (2, 3)}
        for i in (2, 3):
            assert signed[name][i] == basis["actual_signed_m_actions"][name][str(i)]
        assert signed[name][3] == [3]
    # Bind the literal contact-to-source change to the original whole quotient.
    raw_contacts = {int(k): v for k, v in raw["source_contact_plus_retained_basis"].items()}
    for i in (2, 3):
        actual = sub(sub(basis["four_to_source"][str(i)], raw_contacts), to_new)
        assert actual == [i]
    kappa = [-5, 6]
    assert signed["m"][2] == mul(kappa, [2], inv(kappa))
    bdb = [2, 3, -2]
    word = mul(sub(bdb, signed["m"]), inv(bdb))
    eta = {i: ID for i in range(1, 8)}
    eta[2], eta[3], eta[6] = (transposition(1, 3),
                              transposition(3, 4), transposition(1, 2))
    k = evaluate(kappa, eta)
    d = eta[3]
    conjugate = evaluate(bdb, eta)
    value = evaluate(word, eta)
    assert k == transposition(1, 2)
    assert conjugate == transposition(1, 4)
    assert compose(k, d) == compose(d, k)
    assert compose(d, d) == ID and d != ID
    direct = compose(compose(compose(k, conjugate), inverse(k)), inverse(conjugate))
    assert value == direct == (2, 4, 3, 1)
    assert compose(compose(value, value), value) == ID and value != ID
    assert value not in (ID, d)
    evidence = []
    for path in (INPUT, raw_path, ROOT/"work_A/B131_D_source_noncommutation_proposed.tex",
                 ROOT/"work_CE/one_sided_full_m_source_subgroup26.txt"):
        data = path.read_bytes()
        evidence.append({"path": str(path.relative_to(ROOT)), "bytes": len(data),
                         "sha256": hashlib.sha256(data).hexdigest()})
    out = {"status": "PASS", "target": "The single prescribed S4; no target search",
           "permutation_convention": "tuple images of1,2,3,4; p*q means p after q",
           "basis": basis["new_basis"], "actual_signed_B_d_images": signed,
           "fiber_map": {str(i): p for i, p in eta.items()},
           "kappa_image": k, "d_image": d, "BdB_inverse_image": conjugate,
           "actual_r_free_fiber_word": word, "r_image": value,
           "r_order": 3, "r_outside_cyclic_d": True,
           "inputs": evidence,
           "scope": "Exact marked finite free-fiber calculation only. The complete proof uses the actual B131 whole quotient and a finite characteristic refinement to extend this separation to the entire ambient group; eta itself is not asserted source-equivariant."}
    with TARGET.open("x") as stream:
        json.dump(out, stream, indent=2)
        stream.write("\n")
    print("PASS: actual raw contact B,D markings and both signed B,d rows rebound.")
    print("PASS: kappa=(12), d=(34), B d B^-1=(14).")
    print("PASS: r=[m,B_s D_s B_s^-1] maps to (124), outside {1,(34)}.")
    print("Whole-group and compact separation use the proved characteristic refinement, not an equivariance claim for this S4 map.")
    print(json.dumps({"word": word, "image": value, "certificate": str(TARGET.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
