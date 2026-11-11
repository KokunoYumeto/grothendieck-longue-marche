"use strict";
function verifyEgroups(){
  const mod=(a,n)=>((a%n)+n)%n;
  const id=[0,0,0,0],rho=[-1,0,1,0],sigma=[0,0,0,1];
  function act(a,b,v){let [x,y]=v;if(b)[x,y]=[y,x];for(let i=0;i<a;i++)[x,y]=[-y,x-y];return [x,y];}
  function mul(g,h,n=0){const w=act(g[2],g[3],h),v=[g[0]+w[0],g[1]+w[1]];if(n)v.forEach((x,i)=>v[i]=mod(x,n));return [...v,mod(g[2]+(g[3]?-h[2]:h[2])+3*g[3]*h[3],6),(g[3]+h[3])%2];}
  function inv(g,n=0){for(let a=0;a<6;a++)for(let b=0;b<2;b++)if(mod(g[2]+(g[3]?-a:a)+3*g[3]*b,6)===0&&(g[3]+b)%2===0){const v=act(a,b,[-g[0],-g[1]]);if(n)v.forEach((x,i)=>v[i]=mod(x,n));return [...v,a,b];}}
  const key=g=>g.join(",");
  function generated(gs,n){const out=[id],seen=new Set([key(id)]);for(let i=0;i<out.length;i++)for(const g of gs){const h=mul(out[i],g,n),k=key(h);if(!seen.has(k)){seen.add(k);out.push(h);}}return out;}
  const prod=(...xs)=>xs.reduce((a,b)=>mul(a,b),id);
  const comm=(a,b,n)=>mul(mul(mul(a,b,n),inv(a,n),n),inv(b,n),n);
  function commsub(A,B,n){const gs=new Map();for(const a of A)for(const b of B){const c=comm(a,b,n);gs.set(key(c),c);}return generated([...gs.values()],n);}
  const orders=[1,2,3,4,8,9].map(n=>({n,generated:generated([rho,sigma],n).length,expected:12*n*n}));
  const G=generated([rho,sigma],2),derived=[G.length],lower=[G.length];let D=G,L=G;
  for(let i=0;i<3;i++){D=commsub(D,D,2);derived.push(D.length);L=commsub(G,L,2);lower.push(L.length);}
  const mm=(A,B)=>[mod(A[0]*B[0]+A[1]*B[2],4),mod(A[0]*B[1]+A[1]*B[3],4),mod(A[2]*B[0]+A[3]*B[2],4),mod(A[2]*B[1]+A[3]*B[3],4)];
  const mi=A=>[A[3],mod(-A[1],4),mod(-A[2],4),A[0]];
  const I=[1,0,0,1],r=[0,1,3,1],s=[0,3,1,0];
  function mg(gs){const out=[I],seen=new Set([key(I)]);for(let i=0;i<out.length;i++)for(const g of gs){const h=mm(out[i],g),k=key(h);if(!seen.has(k)){seen.add(k);out.push(h);}}return out;}
  const l0=[3,2,0,3],l1=[3,0,2,3],K=mg([l0,l1]),SL=mg([r,s]),ks=new Set(K.map(key));
  const normal=SL.every(g=>K.every(h=>ks.has(key(mm(mm(g,h),mi(g))))));
  const j=[3,0,0,1],jinverts=[l0,l1].every(l=>key(mm(mm(j,l),j))===key(mi(l)));
  const pc=(a,b)=>b.map(x=>a[x]),pi=a=>{const b=[];a.forEach((x,i)=>b[x]=i);return b;};
  const x=[1,0,2],y=[2,1,0],fy=pc(y,pc(pc(pc(x,y),pi(x)),pi(y)));
  function pg(gs){const out=[[0,1,2]],seen=new Set(["0,1,2"]);for(let i=0;i<out.length;i++)for(const g of gs){const h=pc(out[i],g),k=key(h);if(!seen.has(k)){seen.add(k);out.push(h);}}return out.length;}
  return {lambda0:prod(sigma,rho,inv(sigma),rho),lambda1:prod(rho,sigma,rho,inv(sigma)),rho_cubed:prod(rho,rho,rho),sigma_squared:prod(sigma,sigma),finite_generation:orders,derived_orders_mod2:derived,lower_central_orders_mod2:lower,mod4:{SL2_order:SL.length,K_order:K.length,K_normal:normal,index:SL.length/K.length,K,J_inverts_lambdas:jinverts},BISITE:{x,y,f_y:fy,original_image:pg([x,y]),composed_image:pg([x,fy])}};
}
const groupResult=verifyEgroups();
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
if(!equal(groupResult.lambda0,[1,0,0,0])||!equal(groupResult.lambda1,[0,1,0,0]))throw Error("lattice marking");
if(!equal(groupResult.rho_cubed,groupResult.sigma_squared)||!equal(groupResult.rho_cubed,[0,0,3,0]))throw Error("modular relation");
if(!groupResult.finite_generation.every(x=>x.generated===x.expected))throw Error("generation");
if(!equal(groupResult.derived_orders_mod2,[48,12,4,1])||!equal(groupResult.lower_central_orders_mod2,[48,12,12,12]))throw Error("commutator series");
if(groupResult.mod4.SL2_order!==48||groupResult.mod4.K_order!==4||!groupResult.mod4.K_normal||groupResult.mod4.index!==12||!groupResult.mod4.J_inverts_lambdas)throw Error("mod-four subgroup");
if(groupResult.BISITE.original_image!==6||groupResult.BISITE.composed_image!==2||!equal(groupResult.BISITE.x,groupResult.BISITE.f_y))throw Error("BISITE");
const groupOutput=JSON.stringify(groupResult);
if(typeof text==="function")text(groupOutput);else console.log(groupOutput);
if(typeof store==="function")store("e_groups_replacement.out",groupOutput);
