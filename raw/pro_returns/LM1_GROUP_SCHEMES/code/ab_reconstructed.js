/* Reconstructed A/B verification; no external packages.
   Actually executed in the V8 tool runtime on 2026-11-11.
   Node: node ab_reconstructed.js */
const output=[];
function log(s){output.push(String(s));}
function assert(b,s){if(!b)throw new Error(s);}
const names=["a","b","c","d","e","t","m","n","v"],nv=names.length;
function mon(c,ex=[]){const a=Array(nv).fill(0);ex.forEach((z,i)=>a[i]=z);return c===0n?new Map():new Map([[a.join(","),BigInt(c)]]);}
const zero=()=>new Map(),one=()=>mon(1n);
function variable(i,k=1){const a=Array(nv).fill(0);a[i]=k;return mon(1n,a);}
function add(...ps){const r=new Map();for(const p of ps)for(const[k,c]of p){const v=(r.get(k)||0n)+c;if(v)r.set(k,v);else r.delete(k);}return r;}
function neg(p){return new Map([...p].map(([k,c])=>[k,-c]));}
function sub(a,b){return add(a,neg(b));}
function mul(...ps){let r=one();for(const p of ps){const s=new Map();for(const[ka,ca]of r)for(const[kb,cb]of p){const aa=ka.split(",").map(Number),bb=kb.split(",").map(Number),cc=aa.map((x,i)=>x+bb[i]);cc[4]=((cc[4]%2)+2)%2;cc[5]=((cc[5]%2)+2)%2;const k=cc.join(","),z=(s.get(k)||0n)+ca*cb;if(z)s.set(k,z);else s.delete(k);}r=s;}return r;}
function eq(a,b){return sub(a,b).size===0;}
function matrix(a,b,c,d){return[a,b,c,d];}
function mm(A,B){return[add(mul(A[0],B[0]),mul(A[1],B[2])),add(mul(A[0],B[1]),mul(A[1],B[3])),add(mul(A[2],B[0]),mul(A[3],B[2])),add(mul(A[2],B[1]),mul(A[3],B[3]))];}
function ma(A,B){return A.map((v,i)=>add(v,B[i]));}
function scale(c,A){return A.map(v=>mul(c,v));}
function meq(A,B){return A.every((v,i)=>eq(v,B[i]));}
function determinant(A){return sub(mul(A[0],A[3]),mul(A[1],A[2]));}
const[a,b,c,d,e,t,m,n,v]=names.map((_,i)=>variable(i));
const I=matrix(one(),zero(),zero(),one());
const rv=matrix(zero(),one(),v,one()),sv=matrix(zero(),neg(one()),neg(v),zero());
const xv=ma(scale(a,I),scale(b,rv)),yv=matrix(c,d,mul(e,v,d),mul(e,c));
assert(meq(mm(rv,rv),ma(rv,scale(v,I))),"r quadratic");
assert(meq(mm(sv,sv),scale(v,I)),"s quadratic");
assert(meq(ma(rv,sv),matrix(zero(),zero(),zero(),one())),"pinning sum");
assert(meq(mm(xv,rv),mm(rv,xv)),"rho centralizer");
assert(eq(determinant(xv),sub(add(mul(a,a),mul(a,b)),mul(v,b,b))),"rho norm");
assert(meq(mm(yv,sv),scale(e,mm(sv,yv))),"signed sigma normalizer");
assert(eq(determinant(yv),mul(e,sub(mul(c,c),mul(v,d,d)))),"sigma norm");
const r=matrix(zero(),one(),neg(one()),one()),s=matrix(zero(),neg(one()),one(),zero());
const ri=matrix(one(),neg(one()),one(),zero()),si=matrix(zero(),one(),neg(one()),zero());
const mi=variable(6,-1),U=matrix(m,n,zero(),one()),Ui=matrix(mi,neg(mul(n,mi)),zero(),one());
assert(meq(mm(U,Ui),I),"Borel inverse");
const xi=mm(mm(mm(U,r),Ui),ri),eta=mm(mm(mm(U,s),Ui),si);
const expectedXi=matrix(add(m,n,mul(sub(mul(n,n),n),mi)),mul(n,mi),add(one(),mul(sub(n,one()),mi)),mi);
const expectedEta=matrix(add(m,mul(n,n,mi)),mul(n,mi),mul(n,mi),mi);
assert(meq(xi,expectedXi)&&meq(eta,expectedEta),"universal commutators");
assert(eq(determinant(xi),one())&&eq(determinant(eta),one()),"commutator determinants");
const arbitrary=matrix(a,b,c,d),complement=matrix(neg(a),neg(b),neg(c),sub(m,d));
assert(eq(sub(determinant(complement),determinant(arbitrary)),neg(mul(m,a))),"pinning determinant difference");
log("UNIVERSAL LAURENT-POLYNOMIAL ASSERTIONS PASSED over Z[a,b,c,d,e,t,m^+-1,n,v]/(e^2-1,t^2-1).");
function gcd(a,b){while(b)[a,b]=[b,a%b];return a;}
function mod(a,n){return((a%n)+n)%n;}
function matmul(A,B,n){return[mod(A[0]*B[0]+A[1]*B[2],n),mod(A[0]*B[1]+A[1]*B[3],n),mod(A[2]*B[0]+A[3]*B[2],n),mod(A[2]*B[1]+A[3]*B[3],n)];}
function det(A,n){return mod(A[0]*A[3]-A[1]*A[2],n);}
function invint(a,n){for(let x=0;x<n;x++)if(mod(a*x,n)===1)return x;throw new Error("not unit");}
function inverse(A,n){const q=invint(det(A,n),n);return[q*A[3],-q*A[1],-q*A[2],q*A[0]].map(z=>mod(z,n));}
function same(A,B){return A.every((z,i)=>z===B[i]);}
function finite(n){
 const units=Array.from({length:n},(_,i)=>i).filter(x=>gcd(x,n)===1),roots=units.filter(x=>mod(x*x,n)===1);
 const nr=Array(n).fill(0),ns=Array(n).fill(0),Tr=[],Ns=[],SL=[],GL=[],R=[],S=[];
 for(let a=0;a<n;a++)for(let b=0;b<n;b++){
  const q=mod(a*a+a*b+b*b,n);if(gcd(q,n)===1){nr[q]++;Tr.push([a,b,mod(-b,n),mod(a+b,n)]);}
  const z=mod(a*a+b*b,n);if(gcd(z,n)===1){ns[z]++;for(const e of roots)Ns.push([a,b,mod(-e*b,n),mod(e*a,n)]);}
 }
 for(let a=0;a<n;a++)for(let b=0;b<n;b++)for(let c=0;c<n;c++)for(let d=0;d<n;d++){
  const A=[a,b,c,d],q=det(A,n);if(gcd(q,n)===1)GL.push(A);
  if(q===1){SL.push(A);if(mod(a+d,n)===1)R.push(A);if(mod(a+d,n)===0)S.push(A);}
 }
 let H=0,H00=0;
 for(const q of units){H00+=ns[q]*nr[q];for(const e of roots)for(const t of roots)H+=ns[q]*nr[mod(e*t*q,n)];}
 let triples=0;
 for(const r of R)for(const s of S)if(det(r.map((x,i)=>mod(x+s[i],n)),n)===0)triples++;
 assert(triples===SL.length,"triple count "+n);
 const squares=new Set(units.map(x=>mod(x*x,n))),orbitCount=units.length/squares.size,orbitSize=SL.length/roots.length;
 assert(orbitCount*orbitSize===triples,"orbit partition "+n);
 let signed="not-enumerated";
 if([2,3,4].includes(n)){
  const images=new Set();
  for(const m of units)for(let h=0;h<n;h++){const U=[m,h,0,1];for(const x of Tr)for(const y of Ns)images.add(matmul(U,inverse(x,n),n).join(",")+"|"+matmul(U,inverse(y,n),n).join(","));}
  assert(images.size===units.length*n*Tr.length*Ns.length,"signed parametrization injective "+n);
  signed=images.size;
 }
 let finer=0;
 for(let i=0;i<2;i++)for(let j=0;j<2;j++)for(let w=0;w<n;w++){
  const multiplier=1-12*w+6*i+4*j;if(gcd(mod(multiplier,n),n)!==1)continue;
  for(let c=0;c<n;c++)for(let d=0;d<n;d++){
   const b=mod(i+j-2*w,n),h=mod(i+j-3*w,n),a=mod(c-d-i-j+2*w,n);
   assert(mod(a+b-c+d,n)===0&&mod(3*b-2*h-i-j,n)===0,"finer chart equations");
   assert(mod(4*h+2*i+1-multiplier,n)===0,"finer multiplier");finer++;
  }
 }
 log([n,H,SL.length,H*SL.length,H00*SL.length,triples,orbitCount,orbitSize,signed,finer].join("\t"));
}
log("n\tH\tSL2\tM\tM00\ttriples\tSLorbits\torbit_size\tsigned_image\tfiner_scheme");
for(const n of[2,3,5,7,11,13,4,8,9])finite(n);
const f5=[0,1,1,2];assert(det(f5,5)===4&&mod(f5[2]**2+f5[3]**2,5)===0,"weak pair counterexample");
log("F5 weak-pair witness: det(alpha)=4; lower-row Gaussian norm=0.");
const g=[1,0,1,1],g3=g.map(x=>mod(3*x,4));
assert(det(g,4)===1&&det(g3,4)===1&&mod(g[0]+g[3],4)===2&&mod(g3[0]+g3[3],4)===2&&!same(g,g3),"Z4 lift ambiguity");
log("Z/4 lift ambiguity: [[1,0],[1,1]] and [[3,0],[3,3]], determinant1 and trace2.");
log("ALL RECONSTRUCTED A/B ASSERTIONS PASSED.");
const rendered=output.join("\n")+"\n";
if(typeof text==="function")text(rendered);else console.log(rendered);
if(typeof store==="function")store("ab_reconstructed_output",rendered);
