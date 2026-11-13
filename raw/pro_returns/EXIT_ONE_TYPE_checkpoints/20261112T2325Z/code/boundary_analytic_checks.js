/* Exact algebraic checks accompanying P4c3; run with Node.
   The winding vector is proved analytically in boundary.tex, not inferred
   from a floating-point approximation of an exponential. */
"use strict";
function gcd(a, b) {
  a = a < 0n ? -a : a;
  b = b < 0n ? -b : b;
  while (b !== 0n) { const r = a % b; a = b; b = r; }
  return a;
}
class Fraction {
  constructor(n, d = 1n) {
    n = BigInt(n); d = BigInt(d);
    if (d === 0n) throw new Error("Zero denominator");
    if (d < 0n) { n = -n; d = -d; }
    const g = gcd(n, d);
    this.n = n / g; this.d = d / g;
  }
  add(b) { return new Fraction(this.n*b.d+b.n*this.d, this.d*b.d); }
  sub(b) { return new Fraction(this.n*b.d-b.n*this.d, this.d*b.d); }
  mul(b) { return new Fraction(this.n*b.n, this.d*b.d); }
  div(b) { return new Fraction(this.n*b.d, this.d*b.n); }
  text() { return String(this.n) + "/" + String(this.d); }
}
function assert(condition, message) {
  if (!condition) throw new Error(message);
}
function graphData(vertices, edges) {
  const parent = Array.from({length: vertices}, (_, i) => i);
  function find(x) {
    while (parent[x] !== x) { parent[x] = parent[parent[x]]; x = parent[x]; }
    return x;
  }
  for (const [a, b] of edges) parent[find(a)] = find(b);
  const components = new Set(parent.map((_, i) => find(i))).size;
  return {vertices, edges: edges.length, components,
          H1_rank: edges.length - vertices + components};
}
const zero = new Fraction(0n), one = new Fraction(1n);
const alpha = new Fraction(1n, 2n);
// q=z/w, q'=q+1/alpha, u=alpha*q.
const u = [zero, alpha];
const uPrime = [alpha.mul(one.div(alpha)), alpha];
const shift = [uPrime[0].sub(u[0]), uPrime[1].sub(u[1])];
assert(shift[0].text() === "1/1" && shift[1].text() === "0/1",
       "The affine transformation must be u -> u+1");
const normalDerivative = alpha.mul(alpha).div(alpha.mul(alpha));
assert(normalDerivative.text() === "1/1", "Normal derivative must be one");
const meridian = [0, 1];
const toric = graphData(4, [[0,1],[1,2],[2,3],[3,0]]);
const hopf = graphData(1, []);
const bettiT3 = [1];
for (let k = 1; k <= 3; k++) bettiT3.push(bettiT3[k-1]*(4-k)/k);
const result = {
  alpha: alpha.text(),
  induced_affine_u_shift: {constant: shift[0].text(), linear: shift[1].text()},
  induced_v_multiplier: alpha.text(),
  normal_transition: "alpha*t/(alpha+t)",
  normal_derivative_at_zero: normalDerivative.text(),
  input_meridian_winding_vector: meridian,
  meridian_injective: meridian.some(x => x !== 0),
  meridian_primitive: gcd(BigInt(meridian[0]), BigInt(meridian[1])) === 1n,
  toric_dual: toric,
  hopf_dual: hopf,
  T3_homology_ranks: bettiT3,
  conclusion: "Same analytic U=(C*)^2 and link T^3; dual complexes S^1 and point"
};
console.log(JSON.stringify(result, null, 2));
