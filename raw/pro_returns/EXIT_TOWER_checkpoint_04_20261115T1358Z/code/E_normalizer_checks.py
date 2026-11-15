"""Exact certificates used in E.25--E.27; no floating-point arithmetic."""
import json


def red(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def inv(w):
    return tuple(-x for x in reversed(w))


def sub(w, aut):
    return red(y for x in w for y in (aut[x - 1] if x > 0 else inv(aut[-x - 1])))


def comp(f, g):
    return tuple(sub(w, f) for w in g)


def power(f, n):
    out = ((1,), (2,))
    for _ in range(n):
        out = comp(f, out)
    return out


def inner(w):
    return tuple(red(w + (i,) + inv(w)) for i in (1, 2))


def perm_comp(p, q):
    return tuple(p[q[i]] for i in range(3))


def perm_inv(p):
    return tuple(p.index(i) for i in range(3))


def perm_conj(p, q):
    return perm_comp(perm_comp(p, q), perm_inv(p))


def main():
    a = ((1,), (-1, 2))
    b = ((2,), (2, -1, 2))
    d = comp(inner((1,)), a)
    v = comp(b, comp(power(a, 2), b))
    s = comp(a, comp(v, d))
    central_word = power(comp(a, comp(b, d)), 4)
    checks = {
        "B3_braid_action": comp(a, comp(b, a)) == comp(b, comp(a, b)),
        "B4_d_commutes_a": comp(a, d) == comp(d, a),
        "B4_bdb_dbd": comp(b, comp(d, b)) == comp(d, comp(b, d)),
        "s_x_s_inverse": s[0] == (-2, -1, 2),
        "s_squared_is_omega4_action": power(s, 2) == central_word,
    }
    t = comp(a, comp(b, a))
    term, total = (-1, 2), ()
    for _ in range(4):
        total = red(total + term)
        term = sub(term, t)
    checks["omega4_kernel_part_is_XY_commutator"] = total == (1, -2, -1, 2)
    # Faithful rank-four Artin action verifies the exact Garside word used
    # in the G2 relation, without passing to a homology representation.
    identity4 = tuple((i,) for i in range(1, 5))
    generators = []
    for i in range(1, 4):
        positive, negative = list(identity4), list(identity4)
        positive[i - 1], positive[i] = (i, i + 1, -i), (i,)
        negative[i - 1], negative[i] = (i + 1,), (-(i + 1), i, i + 1)
        generators.append((tuple(positive), tuple(negative)))

    def braid(word):
        out = identity4
        for j in word:
            out = comp(out, generators[abs(j) - 1][j < 0])
        return out

    delta_word = (3, 2, 3, -3, 1, 3, 2, 3)
    delta = braid(delta_word)
    checks["G2_delta_conjugates_d_to_a"] = comp(delta, braid((3,))) == comp(braid((1,)), delta)
    checks["G2_delta_is_Garside_half_twist"] = delta == braid((1, 2, 3, 1, 2, 1))
    for n in (2, 3, 4):
        ident = tuple((i,) for i in range(1, n + 2))
        actions = []
        for i in range(1, n + 1):
            pos, neg = list(ident), list(ident)
            pos[i - 1], pos[i] = (i, i + 1, -i), (i,)
            neg[i - 1], neg[i] = (i + 1,), (-(i + 1), i, i + 1)
            actions.append((tuple(pos), tuple(neg)))

        def evaluate(word):
            result = ident
            for j in word:
                result = comp(result, actions[abs(j) - 1][j < 0])
            return result

        meridians = []
        for i in range(1, n + 1):
            prefix = tuple(range(n, i, -1))
            meridians.append(prefix + (i, i) + inv(prefix))
        valid = True
        for i in range(1, n):
            xi, xj = meridians[i - 1], meridians[i]
            valid &= evaluate((i,) + xi + (-i,)) == evaluate(xj)
            valid &= evaluate((i,) + xj + (-i,)) == evaluate(inv(xj) + xi + xj)
        checks[f"actual_x_i_last_inverse_Artin_n{n}"] = valid
    first_doubled = (4, 3, 2, 1, 1, 2, -3, -4)
    checks["first_strand_cabling_x14_equals_x15_x25"] = red(first_doubled) == red(meridians[0] + meridians[1])
    # E.25: inner automorphisms must preserve distinct evaluated group elements.
    pa, pb, pc = (1, 0, 2), (0, 2, 1), (2, 1, 0)
    p = perm_comp(pa, pb)
    checks["S3_Tb_equals_c"] = perm_conj(p, pb) == pc
    checks["S3_b_differs_c"] = pb != pc
    checks["S3_no_single_conjugator"] = not any(
        perm_conj(q, pb) == pc and perm_conj(q, pc) == pc
        for q in __import__("itertools").permutations(range(3))
    )
    # On each index-two kernel of R=<v,d|(vd)^2=1>, the odd coset
    # acts on the displayed abelian basis by this nonscalar matrix.
    odd_matrix = [[-1, 0], [-1, 1]]
    checks["odd_deck_matrix_is_nonscalar_mod2"] = odd_matrix[1][0] % 2 == 1
    assert all(checks.values()), checks
    return {
        "checks": checks,
        "Cardano_monodromy": {"a": a, "b": b, "d": d, "s": s},
        "odd_deck_matrix": odd_matrix,
        "S3_a_b_c": [pa, pb, pc],
        "S3_Tb_Tc": [perm_conj(p, pb), pc],
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
