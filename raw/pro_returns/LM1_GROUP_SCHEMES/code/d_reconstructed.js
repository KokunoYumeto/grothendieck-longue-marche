const result = (function(){
const out=[], emit=x=>out.push(x);
const gcd=(a,b)=>b?gcd(b,a%b):a, lcm=(a,b)=>a/gcd(a,b)*b;
const mod=(a,n)=>(a%n+n)%n;
const I=[1,0,0,1], key=a=>Array.isArray(a)?a.join(","):String(a);
function matmul(a,b,n){return [mod(a[0]*b[0]+a[1]*b[2],n),mod(a[0]*b[1]+a[1]*b[3],n),mod(a[2]*b[0]+a[3]*b[2],n),mod(a[2]*b[1]+a[3]*b[3],n)];}
function matinv(a,n){return [mod(a[3],n),mod(-a[1],n),mod(-a[2],n),mod(a[0],n)];}
function pow(a,k,mul,one){let z=one;if(k<0)throw Error("negative exponent");while(k){if(k&1)z=mul(z,a);a=mul(a,a);k=Math.floor(k/2);}return z;}
function closure(gens,mul,one){const seen=new Map([[key(one),one]]), queue=[one];for(let j=0;j<queue.length;j++)for(const g of gens){const h=mul(queue[j],g),k=key(h);if(!seen.has(k)){seen.set(k,h);queue.push(h);}}return queue;}
function order(a,mul,one){let b=one;for(let k=1;k<10000;k++){b=mul(b,a);if(key(b)===key(one))return k;}throw Error("order cap");}
function mapCheck(H,X,Y,AX,AY,mul,inv,one){
 const im=new Map([[key(one),one]]), queue=[one];
 const gens=[X,Y,inv(X),inv(Y)], imgs=[AX,AY,inv(AX),inv(AY)];
 for(let j=0;j<queue.length;j++)for(let a=0;a<4;a++){
  const h=mul(queue[j],gens[a]), v=mul(im.get(key(queue[j])),imgs[a]), k=key(h);
  if(im.has(k)){if(key(im.get(k))!==key(v))return false;}
  else{im.set(k,v);queue.push(h);}
 }
 return im.size===H.length && new Set([...im.values()].map(key)).size===H.length;
}
for(const n of [2,3,4,6,12]){
 const mul=(a,b)=>matmul(a,b,n), inv=a=>matinv(a,n), one=I.map(x=>mod(x,n));
 const X=[-1,2,0,-1].map(x=>mod(x,n)), Y=[-1,0,-2,-1].map(x=>mod(x,n));
 const Z=inv(mul(X,Y)), S=[0,-1,1,0].map(x=>mod(x,n)), rho=[0,1,-1,1].map(x=>mod(x,n));
 const R=mul(inv(Y),rho), R2=mul(R,R), conj=(a,b)=>mul(mul(a,b),inv(a));
 const H=closure([X,Y],mul,one);
 const comm=[];for(const a of H)for(const b of H)comm.push(mul(mul(mul(a,b),inv(a)),inv(b)));
 const derived=closure([...new Map(comm.map(x=>[key(x),x])).values()],mul,one);
 const exponent=H.reduce((e,a)=>lcm(e,order(a,mul,one)),1);
 let count=0, automorphisms=0;
 for(let lambda=0;lambda<2*exponent;lambda++)if(gcd(lambda,2*exponent)===1){
  const m=(lambda-1)/2;
  for(const F of derived){
   const dual=mul(conj(S,F),F);
   const hex=[conj(R2,F),pow(Z,m,mul,one),conj(R,F),pow(Y,m,mul,one),F,pow(X,m,mul,one)].reduce(mul,one);
   if(key(dual)!==key(one)||key(hex)!==key(one))continue;
   count++;
   const AX=pow(X,lambda,mul,one), AY=mul(mul(inv(F),pow(Y,lambda,mul,one)),F);
   if(mapCheck(H,X,Y,AX,AY,mul,inv,one))automorphisms++;
  }
 }
 emit({test:"finite_GT_shadows",n,H:H.length,derived:derived.length,exponent,pairs:count,automorphisms});
}
let cocycles=0;const V=[0,1,2,3], nonzeroPairs=[];
for(const a of [1,2,3])for(const b of [1,2,3])nonzeroPairs.push([a,b]);
const cocycleKeys=new Set(), coboundaryKeys=new Set();
for(let bits=0;bits<512;bits++){
 const f=(a,b)=>{if(!a||!b)return 0;return (bits>>nonzeroPairs.findIndex(p=>p[0]===a&&p[1]===b&&p[1]===b))&1;};
 if(V.every(a=>V.every(b=>V.every(c=>(f(a,b)^f(a^b,c)^f(b,c)^f(a,b^c))===0)))){
  cocycles++;cocycleKeys.add(bits);
 }
}
for(let bits=0;bits<8;bits++){
 const f=a=>a?((bits>>(a-1))&1):0;
 let v=0;nonzeroPairs.forEach(([a,b],i)=>{v|=(f(a)^f(b)^f(a^b))<<i;});coboundaryKeys.add(v);
}
emit({test:"H2_C2_squared",normalized_two_cochains:512,cocycles,coboundaries:coboundaryKeys.size,classes:cocycles/coboundaryKeys.size});
const classification=[];
for(let a=0;a<2;a++)for(let b=0;b<2;b++)for(let c=0;c<2;c++){
 const q=[a,b,a^b^c];
 classification.push({a,b,c,squares_on_10_01_11:q,group:c?(a&&b?"Q8":"D8"):(a||b?"C4xC2":"C2^3")});
}
emit({test:"central_extension_table",rows:classification});
const f8mul=(a,b)=>{let c=0;while(b){if(b&1)c^=a;b>>=1;a<<=1;if(a&8)a^=11;}return c;};
const f8mm=(a,b)=>[f8mul(a[0],b[0])^f8mul(a[1],b[2]),f8mul(a[0],b[1])^f8mul(a[1],b[3]),f8mul(a[2],b[0])^f8mul(a[3],b[2]),f8mul(a[2],b[1])^f8mul(a[3],b[3])];
const f8inv=a=>[a[3],a[1],a[2],a[0]];
const A=[0,1,1,0], B=[0,2,5,1], G=closure([A,B],f8mm,I);
const left=new Map(G.map(x=>[key(x),x])), classes=[];
while(left.size){
 const g=left.values().next().value;
 const cls=[...new Map(G.map(h=>{const x=f8mm(f8mm(h,g),f8inv(h));return [key(x),x];})).values()];
 cls.forEach(h=>left.delete(key(h)));
 classes.push({order:order(g,f8mm,I),size:cls.length,normal_closure:closure(cls,f8mm,I).length});
}
classes.sort((a,b)=>a.order-b.order||a.size-b.size);
emit({test:"SL2_F8",field_polynomial:"x^3+x+1",alpha:2,alpha_inverse:5,A,B,A_order:order(A,f8mm,I),B_order:order(B,f8mm,I),AB_order:order(f8mm(A,B),f8mm,I),generated_order:G.length,classes});
const torsion=[];
for(let a=0;a<5;a++)for(let b=0;b<5;b++){
 const x=[a,b,mod(-b,5),mod(a+b,5)], norm=mod(a*a+a*b+b*b,5);
 if(norm && key(pow(x,4,(a,b)=>matmul(a,b,5),I))===key(I))torsion.push({a,b,norm});
}
emit({test:"four_torsion_norm_mod5",elements:torsion,norms:[...new Set(torsion.map(x=>x.norm))].sort()});
const hensel=[];let root=2,modulus=5;
for(let k=1;k<=6;k++){
 hensel.push({k,modulus,root,residual:mod(root*root+1,modulus)});
 if(k<6){let next=null;for(let j=0;j<5;j++){const r=root+j*modulus;if(mod(r*r+1,modulus*5)===0){next=r;break;}}root=next;modulus*=5;}
}
emit({test:"sqrt_minus1_at5",lifts:hensel});
emit({test:"rank_obstruction_at7",rows:[2,3,4].map(r=>({r,ambient_principal_units:7**(2*(r-1)),image_upper_bound:7**(r-1),index_lower_bound:7**(r-1)}))});
const sq4=new Set();
for(let a=0;a<4;a++)for(let b=0;b<4;b++)if((a%2)||(b%2)){
 sq4.add(key([mod(a*a-b*b,4),mod(2*a*b+b*b,4)]));
}
emit({test:"dyadic_unit_squares_mod4",squares:[...sq4].sort(),minus1:"3,0",sqrt_minus3:"3,2",minus_sqrt_minus3:"1,2"});
let points=1;for(let x=0;x<5;x++)for(let y=0;y<5;y++)if(mod(y*y-x*x*x+x,5)===0)points++;
emit({test:"elliptic_E_y2_x3_minus_x",p:5,points,trace:6-points,frobenius_polynomial:[1,points-6,5]});
const rho=[0,1,-1,1],sigma=[0,-1,1,0], P=[1,1,0,1], Pi=[1,-1,0,1];
const intmm=(a,b)=>[a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]];
const rr=intmm(intmm(P,rho),Pi), cusp=intmm(sigma,rr);
emit({test:"nonmotivic_cusp",rho_image:rr,sigma_image:sigma,cusp,trace:cusp[0]+cusp[3],determinant:cusp[0]*cusp[3]-cusp[1]*cusp[2],characteristic_polynomial:[1,-4,1]});
const roots=[];for(let x=-1;x<=1;x+=2)roots.push({x,value:x*x*x-x*x-3*x+1});
const cubic=[1,-1,-3,1], [aa,bb,cc,dd]=cubic, disc=bb*bb*cc*cc-4*aa*cc**3-4*bb**3*dd-27*aa*aa*dd*dd+18*aa*bb*cc*dd;
const H37=[];for(let j=0;j<9;j++)H37.push(pow(16,j,(a,b)=>a*b%37,1));
const cosets=[];for(let j=0;j<4;j++)cosets.push(H37.map(h=>h*pow(2,j,(a,b)=>a*b%37,1)%37).sort((a,b)=>a-b));
const conv=(a,b)=>{const z=Array(37).fill(0);for(let i=0;i<37;i++)for(let j=0;j<37;j++)z[(i+j)%37]+=a[i]*b[j];return z;};
const cycOne=Array(37).fill(0);cycOne[0]=1;
let poly=[cycOne];
for(const coset of cosets){
 const eta=Array(37).fill(0);coset.forEach(i=>eta[i]=1);
 const next=Array.from({length:poly.length+1},()=>Array(37).fill(0));
 poly.forEach((p,i)=>{const q=conv(p,eta);for(let j=0;j<37;j++){next[i][j]-=q[j];next[i+1][j]+=p[j];}});
 poly=next;
}
const coefficients=poly.map(p=>{if(!p.slice(1).every(x=>x===p[1]))throw Error("non-rational coefficient");return p[0]-p[1];});
emit({test:"Dic3_CFT_example",cubic,disc,rational_root_tests:roots,primitive_root2_order:order(2,(a,b)=>a*b%37,1),period_cosets:cosets,quartic_coefficients_descending:coefficients.slice().reverse()});
const phi=n=>{let c=0;for(let a=0;a<n;a++)if(gcd(a,n)===1)c++;return c;};
const generation=[];
for(let n=1;n<=48;n++){
 if(n===1){generation.push({n,SL2_order:1,generated_SL2:1,GL2_index:1});continue;}
 const one=I.map(x=>mod(x,n)),mul=(a,b)=>matmul(a,b,n);
 const gens=[rho.map(x=>mod(x,n)),sigma.map(x=>mod(x,n))];
 const gr=closure(gens,mul,one).length;
 let expected=n**3, q=n;for(let p=2;p<=q;p++)if(q%p===0){expected=expected/p/p*(p*p-1);while(q%p===0)q/=p;}
 if(gr!==expected)throw Error("generation mismatch "+n);
 generation.push({n,SL2_order:gr,generated_SL2:gr,GL2_index:phi(n)/(n>2?2:1)});
}
emit({test:"modular_generation_n_1_to_48",rows:generation});
emit({test:"integral_cover_classes",characters:["1","delta","e","t","delta*e","delta*t","e*t","delta*e*t"],count:8,F5_point:{a:1,b:2,c:1,d:1,e:1,t:1,delta:2},F5_squares:[0,1,4]});
const dicOrders=[];
for(let a=0;a<3;a++)for(const b of [1,3]){
 let x=0,y=0,k=0;
 do{x=mod(x+(y%2?-a:a),3);y=mod(y+b,4);k++;}while(x||y);
 dicOrders.push({a,b,order:k});
}
emit({test:"Dic3_imaginary_obstruction",outside_index2_orders:dicOrders});
const roots37=[];
for(let x=0;x<37;x++)if(mod(x*x*x-x*x-3*x+1,37)===0)
 roots37.push({x,multiple:mod(3*x*x-2*x-3,37)===0});
emit({test:"cubic_reduction_at37",roots:roots37,Eisenstein_shift_coefficients:[1,2,-2,-2]});
return out;
})();
console.log(JSON.stringify(result));
