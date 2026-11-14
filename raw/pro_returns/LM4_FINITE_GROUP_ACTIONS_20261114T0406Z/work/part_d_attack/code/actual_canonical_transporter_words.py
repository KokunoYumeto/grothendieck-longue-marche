"""Universal word identities and the original standard transporter frame.

Formal H,a,L,W letters test identities only; they are not actual new h inputs.
The extended-group calculation uses the full original standard h=1.
"""
from pathlib import Path
import json

orders = {0: 2, 1: 3, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
one = ()
T, X, S, H, aa, LL, WW, gg = [((i, 1),) for i in range(8)]


def normal(syllables):
    out = []
    for factor, exponent in syllables:
        order = orders[factor]
        if order:
            exponent %= order
        if not exponent:
            continue
        if out and out[-1][0] == factor:
            exponent += out.pop()[1]
            if order:
                exponent %= order
        if exponent:
            out.append((factor, exponent))
    return tuple(out)


def mul(*values):
    return normal(s for value in values for s in value)


def inv(value):
    return normal((f, -e) for f, e in reversed(value))


def power(value, exponent):
    if exponent < 0:
        return power(inv(value), -exponent)
    result = one
    while exponent:
        if exponent & 1:
            result = mul(result, value)
        value = mul(value, value)
        exponent >>= 1
    return result


def conj(a, b):
    return mul(a, b, inv(a))


checks = []


def check(name, condition):
    assert condition, name
    checks.append({'name': name, 'status': 'PASS'})


p = mul(inv(X), T, inv(X))
z = power(p, -2)
kappa = conj(LL, X)
b = mul(inv(LL), H, conj(T, LL))
qword = mul(inv(kappa), H, T, inv(kappa))
qrewrite = mul(LL, conj(inv(X), b), p, inv(LL))
h_transport = mul(LL, conj(T, inv(aa)), conj(T, conj(S, inv(LL))))
check('exact tau-a-inverse-s ordering in the transporter equation',
      mul(LL, T, inv(aa), S, inv(LL)) == mul(h_transport, T, S))
check('canonical kappa has order three', power(kappa, 3) == one)
check('canonical F-component expression',
      mul(kappa, inv(X)) == mul(LL, conj(X, inv(LL))))
check('full positive cusp word rewrite', qword == qrewrite)
Az = mul(WW, inv(kappa), X)
check('A equals w L omega-square(L inverse)',
      Az == mul(WW, LL, conj(inv(X), inv(LL))))
tp_formal = mul(inv(gg), inv(p))
check('B stays in the displayed original-word form',
      mul(tp_formal, Az, inv(p)) == mul(inv(gg), conj(inv(p), Az), z))

# This identity needs only t^2=1, with t=T in this universal word test.
km = conj(T, kappa)
tr = conj(inv(X), T)
raw = mul(WW, inv(km), X)
check('negative-epsilon raw conjugator ordering',
      mul(raw, tr, inv(p)) == mul(conj(WW, T), Az, inv(p)))

universal_exponents = 0
for kk in range(-8, 9):
    nu = 2 * kk + 1
    uu = mul(WW, LL)
    lhs = mul(WW, qword, inv(WW), power(p, -nu))
    rhs = mul(uu, conj(inv(X), b), conj(p, inv(uu)), power(z, kk))
    assert lhs == rhs
    universal_exponents += 1
check('universal odd-exponent cusp rewrite', universal_exponents == 17)


def delta(value):
    images = {0: T, 1: mul(T, inv(X), T)}
    return mul(*(power(images[f], e) for f, e in value))


# Exact standard extension M semidirect_delta <s>.
E1 = (one, 0)


def emul(*values):
    w, parity = E1
    for v, e in values:
        w = mul(w, delta(v) if parity else v)
        parity ^= e
    return w, parity


def einv(value):
    w, e = value
    return (delta(inv(w)) if e else inv(w), e)


def epower(value, n):
    if n < 0:
        return epower(einv(value), -n)
    out = E1
    for _ in range(n):
        out = emul(out, value)
    return out


def econj(a, value):
    return emul(a, value, einv(a))


tau, xi, ss = (T, 0), (X, 0), (one, 1)
xx = (power(mul(T, X), -2), 0)
yy = econj(xi, xx)
zz = einv(emul(xx, yy))
pp, gw, ww = (p, 0), einv(xx), xx
tt, jj = tau, emul(tau, ss)
rr = econj(einv(xi), ss)
vv = emul(pp, rr)
tp = econj(ww, tt)
kp, km = xi, econj(tt, xi)
AA = emul(ww, einv(kp), xi)
BB = emul(tp, AA, einv(pp))
check('standard delta is an involution', delta(delta(T)) == T and delta(delta(X)) == X)
check('original standard cusp square', epower(pp, 2) == einv(zz))
check('literal original reflection identity', rr == emul(xx, ss))
check('original standard J transporter', econj(ww, jj) == vv)
check('original t-prime frame', tp == emul(einv(gw), einv(pp)))
check('original reflection inverts the original cusp', econj(rr, zz) == einv(zz))
check('standard canonical A is x and B is one', AA == xx and BB == E1)
check('standard even branch R(0) is A', AA == einv(gw))
Qp = emul(einv(kp), tt, einv(kp))
Qm = emul(einv(km), tt, einv(km))
Cp = emul(Qp, einv(ww), einv(pp), ww)
Cm = emul(Qm, einv(ww), einv(pp), ww)
check('standard positive-epsilon cusp word does not vanish', Cp != E1)
check('standard negative-epsilon cusp word vanishes', Cm == E1)
check('inverse kappa sends its Q word to the inverse',
      emul(km, tt, km) == einv(Qm))

branches = []
for kk in range(-9, 10):
    target = emul(epower(zz, -kk - 1), rr)
    if kk % 2:
        aa0 = epower(zz, -(kk + 1) // 2)
        assert econj(aa0, rr) == target
        branches.append({'k': kk, 'branch': 'A', 'z_exponent': -(kk + 1) // 2})
    else:
        bb0 = epower(zz, -kk // 2)
        aa0 = emul(einv(gw), bb0)
        assert econj(bb0, emul(einv(zz), rr)) == target
        assert emul(tp, aa0, einv(pp)) == bb0
        branches.append({'k': kk, 'branch': 'B', 'z_exponent': -kk // 2})
check('both exact integral branch conjugations', len(branches) == 19)

result = {
    'status': 'PASS',
    'scope': 'Universal word identities and the full original standard input; no new nonstandard h assigned',
    'named_check_count': len(checks),
    'universal_odd_exponent_cases': universal_exponents,
    'standard_input': {'h': '1', 'a': '1', 'L': '1', 'k': 0, 'nu0': 1,
                       'kappa_plus': 'xi', 'A': 'x', 'B': '1',
                       'T_parameters': [-1, 1]},
    'checks': checks,
    'integral_branch_cases': branches,
}
raw = json.dumps(result, indent=2) + '\n'
Path(__file__).with_name('actual_canonical_transporter_words_output.json').write_text(raw)
print(raw, end='')
