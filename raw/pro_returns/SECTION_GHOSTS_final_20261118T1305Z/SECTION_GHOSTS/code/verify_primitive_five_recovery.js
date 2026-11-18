function verifyPrimitiveFiveRecovery() {
  const assert = (condition, label) => { if (!condition) throw new Error(label); };
  const valuation = (x, p) => {
    x = x < 0n ? -x : x;
    assert(x !== 0n, "valuation of zero");
    let v = 0;
    while (x % p === 0n) { x /= p; v++; }
    return v;
  };
  const prime = n => {
    if (n < 2) return false;
    for (let d = 2; d*d <= n; d++) if (n % d === 0) return false;
    return true;
  };
  const inverse25 = a => {
    for (let b = 1; b < 25; b++) if ((a*b)%25 === 1) return b;
    throw new Error("nonunit modulo25");
  };
  const mod5 = n => ((n%5)+5)%5;
  const digit = a => mod5((a**4-1)/5);
  const allowed = [];
  for (let a=1; a<25; a++)
    if ((a%5===2 || a%5===3) && (a**4-1)%25!==0) allowed.push(a);
  assert(JSON.stringify(allowed)===JSON.stringify([2,3,8,12,13,17,22,23]), "allowed residues");
  const base=[2,83,173].map(p=>{
    assert(prime(p),"base prime");
    const q=BigInt(p);
    const row={prime:p,mod9:p%9,mod25:p%25,
      v5_p4_minus1:valuation(q**4n-1n,5n),
      v3_p2_minus1:valuation(q**2n-1n,3n)};
    if (p!==2) {
      row.v2_p_minus1=valuation(q-1n,2n);
      row.v2_p2_minus1=valuation(q*q-1n,2n);
    }
    assert(row.mod9===2 && row.v5_p4_minus1===1 && row.v3_p2_minus1===1,"base congruences");
    return row;
  });
  assert(83+173===256,"rational base sum");
  let factorizations=0;
  for (const target of [1,6,11,16,21]) {
    const a=allowed.find(v=>v%5===2 && digit(v)!==0 && digit(v)!==digit(target));
    assert(a!==undefined,"first factor");
    const b=target*inverse25(a)%25;
    assert(allowed.includes(b),"second factor");
    assert(mod5(digit(a)+digit(b))===digit(target),"Fermat digit additivity");
    for (const length of [6,8,10]) {
      const factors=[a,b];
      while (factors.length<length) factors.push(2,inverse25(2));
      assert(factors.reduce((u,v)=>u*v%25,1)===target,"target product");
      assert(factors.every(v=>allowed.includes(v)),"factor shells");
      factorizations++;
    }
  }
  const samples=[];
  for(let p=2;samples.length<128;p++)
    if(prime(p) && allowed.includes(p%25)) samples.push(p);
  let cases=0;
  for(const p of samples) {
    const q=BigInt(p);
    for(let w=2;w<=200;w++) {
      const expected=w%4===0 ? 1+valuation(BigInt(w),5n) : 0;
      assert(valuation(q**BigInt(w)-1n,5n)===expected,"weight valuation");
      cases++;
    }
  }
  assert(factorizations===15 && cases===25472,"case counts");
  return {
    statement:"primitive-five-support reinitialization and all-weight gate",
    status:"PASS",
    provenance:"Recovery verifier newly executed in JavaScript after workspace loss; not the original Python file.",
    base:base,
    allowed_mod25:allowed,
    local_factorizations_checked:factorizations,
    support_sample_primes:samples.length,
    sample_selection:"The first128 primes with allowed residue modulo25.",
    weight_valuation_checks:cases,
    weights_tested:[2,200],
    first_gate_parameter_count:25,
    first_gate_place_bound:4,
    scope:"Finite arithmetic and valuation checks only; no affine-gate consistency or infinite section is asserted."
  };
}
console.log(JSON.stringify(verifyPrimitiveFiveRecovery(),null,2));
