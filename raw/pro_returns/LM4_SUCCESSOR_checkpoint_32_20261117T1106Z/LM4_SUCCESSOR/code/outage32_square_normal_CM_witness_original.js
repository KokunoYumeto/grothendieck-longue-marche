function checkSquareNormalCMWitness() {
  const mod3 = n => ((n % 3) + 3) % 3;
  const mul = (a,b) => [
    mod3(a[0]*b[0]+a[1]*b[2]),
    mod3(a[0]*b[1]+a[1]*b[3]),
    mod3(a[2]*b[0]+a[3]*b[2]),
    mod3(a[2]*b[1]+a[3]*b[3])
  ];
  const det = a => mod3(a[0]*a[3]-a[1]*a[2]);
  const inv = a => {
    if(det(a)!==1) throw new Error("Matrix is not in SL(2,F3)");
    return [a[3],mod3(-a[1]),mod3(-a[2]),a[0]];
  };
  const comm = (a,b) => mul(mul(mul(a,b),inv(a)),inv(b));
  const equal = (a,b) => a.every((v,i)=>v===b[i]);
  const x=[1,2,0,1], y=[1,0,1,1];
  const z=inv(mul(x,y));
  const x2=mul(x,x), y2=mul(y,y), z2=mul(z,z);
  const u=comm(x2,y2);
  const v=comm(u,z2);
  const xvxInverse=mul(mul(x,v),inv(x));
  const w=comm(v,xvxInverse);
  const identity=[1,0,0,1], negativeIdentity=[2,0,0,2];
  const matrices={x,y,z,x2,y2,z2,u,v,xvxInverse,w};
  const determinantChecks=Object.fromEntries(Object.entries(matrices).map(([k,a])=>[k,det(a)]));
  return {
    computation:"One prescribed word in the previously fixed SL(2,F3) frame; no target search or census",
    commutator_convention:"[a,b]=a b a^-1 b^-1",
    word_z:"(xy)^-1",
    word_u:"[x^2,y^2]",
    word_v:"[[x^2,y^2],z^2]",
    word_w:"[v,x v x^-1]",
    matrices,
    determinantChecks,
    all_matrices_in_SL2: Object.values(determinantChecks).every(d=>d===1),
    w_is_negative_identity:equal(w,negativeIdentity),
    w_is_nonidentity:!equal(w,identity),
    w_squared_is_identity:equal(mul(w,w),identity),
    scope:"Algebraic boundary witness only; not a canonical-u/H_d evaluation and not an actual CM frame determination",
    filesystem_saved:false
  };
}