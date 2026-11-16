"""Rigorous degree-four central-value certificate for Jac(y^2+y=x^5).

Exact finite-field Euler factors are computed by PARI/GP 2.19.1, separately
expanded in Python, and compared with PARI's exact lfunan output.  No guessed
root number, lfun value, analytic rank, or database value enters the proof.

The CM Hecke-character theorem supplies analytic continuation and a functional
equation with conductor 5^5 and sign in {+1,-1}.  Positivity of the certified
inverse Mellin transform at t=1 proves that the sign is +1.  Arb evaluates the
Bessel series and the explicit elementary bound for its entire omitted tail.
"""
import ast
import gzip
import json
import math
import os
from pathlib import Path
import subprocess
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[2]
GP = Path(os.environ.get("A_MAIN_GP", str(ROOT / "work/pari-2.19.1/gp")))
OUT = ROOT / "deliverable/code"
M = 4096
ctx.prec = 192

code = f"""
G=genus2red([x^5,1]); print(G[1]);
L=lfungenus2([x^5,1]); print(lfunan(L,{M}));
forprime(p=2,{M}, if(p==5, print([p,[1]]), print([p,Vec(hyperellcharpoly([Mod(1,p)*x^5,Mod(1,p)]))])));
"""
run = subprocess.run([str(GP), "-fq", "-s", "128000000"], input=code+"\nquit;\n",
                     text=True, capture_output=True, timeout=180)
if run.returncode or "***" in run.stderr:
    raise RuntimeError(run.stderr)
(OUT / "a_main_quintic_gp.out").write_text(run.stdout)
raw = [ast.literal_eval(line) for line in run.stdout.splitlines() if line.strip()]
N, gp_coeffs, factors = raw[0], raw[1], raw[2:]
assert N == 3125

# Reconstruct all Dirichlet coefficients solely from the exact Euler factors.
coeff = [0] * (M + 1)
coeff[1] = 1
for p, den in factors:
    pk = p
    powers = [1]
    while pk <= M:
        k = len(powers)
        powers.append(-sum(den[j] * powers[k-j] for j in range(1, min(k, len(den)-1)+1)))
        for m in range(1, M//pk+1):
            if m % p:
                coeff[m*pk] = coeff[m] * powers[k]
        pk *= p
assert coeff[1:] == gp_coeffs

# Weil's bound gives |a_n| <= d_4(n)*sqrt(n) <= n^(7/2).
assert all(a*a <= n**7 for n,a in enumerate(coeff[1:],1))
c = 4 * arb.pi()**2 / arb(N).sqrt()
k = 2*c.sqrt()
theta = arb(0)
central = arb(0)
for n, a in enumerate(coeff[1:], 1):
    if a:
        x = k*arb(n).sqrt()
        theta += 2*a*x.bessel_k(0)
        central += 4*c.sqrt()*a/arb(n).sqrt()*x.bessel_k(1)

# K_0(x), K_1(x) <= sqrt(pi/x)*exp(-x), x>=2.  Replacing
# n^(11/4), n^(13/4) by n^4, then integrating the decreasing tail,
# gives integral_M^infty x^4 exp(-k sqrt(x)) dx = 2 Gamma(10,k sqrt(M))/k^10.
z = k*arb(M).sqrt()
assert z > 8
gamma10 = (-z).exp()*math.factorial(9)*sum((z**j)/math.factorial(j) for j in range(10))
integral_tail = 2*gamma10/k**10
theta_tail = 2*(arb.pi()/k).sqrt()*integral_tail
central_tail = 4*c.sqrt()*(arb.pi()/k).sqrt()*integral_tail
theta += arb(0,theta_tail.upper())
central += arb(0,central_tail.upper())
assert theta > 0
assert central > 0

data = {
    "curve": "y^2+y=x^5", "N": N, "M": M, "arb_bits":ctx.prec,
    "a_n":coeff[1:], "Euler_factors_ascending":factors,
    "theta_at_1_ball":str(theta), "theta_tail_bound":str(theta_tail),
    "root_number_certified":1, "L1_ball":str(central),
    "L1_tail_bound":str(central_tail),
    "root_number_proof":"theta(1)=w*theta(1), theta(1)>0",
    "tail_proof":"|a_n|<=n^(7/2); K0,K1<=sqrt(pi/x)exp(-x) for x>=2; decreasing integral bound"
}
with gzip.open(OUT / "a_main_quintic_data.json.gz", "wt") as f:
    json.dump(data,f,separators=(",",":"))
summary = {key:value for key,value in data.items() if key not in ("a_n","Euler_factors_ascending")}
(OUT / "a_main_quintic_certificate.json").write_text(json.dumps(summary,indent=2)+"\n")
print(json.dumps(summary,indent=2))
print("PASS: exact Euler reconstruction, coefficient bounds, positive theta, positive L(1)")
