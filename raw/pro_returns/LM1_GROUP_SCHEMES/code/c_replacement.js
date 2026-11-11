function verifyC(){
const mod=(a,n)=>((a%n)+n)%n;
function tc(signed,n){
const rel=[Array(signed?4:2).fill(0),Array(signed?6:3).fill(2)];
if(signed)rel.push([0,0,3,3,3]);rel.push(Array.from({length:n},()=>[0,2]).flat());
const parent=[0],edges=[];let tab=[[-1,-1,-1,-1]],version=0;
const find=x=>{while(parent[x]!==x){parent[x]=parent[parent[x]];x=parent[x];}return x;};
function join(a,b){a=find(a);b=find(b);if(a===b)return false;parent[Math.max(a,b)]=Math.min(a,b);version++;return true;}
function rebuild(){for(;;){const t=parent.map(()=>[-1,-1,-1,-1]);let changed=false;for(const[x,g,y]of edges){const a=find(x),b=find(y);if(t[a][g]<0)t[a][g]=b;else if(join(t[a][g],b))changed=true;}if(!changed){tab=t;return;}}}
function edge(a,g,b){edges.push([a,g,b],[b,g^1,a]);version++;rebuild();}
function scan(c,w){let a=find(c),b=a,i=0,j=w.length-1;while(i<=j&&tab[find(a)][w[i]]>=0)a=find(tab[find(a)][w[i++]]);while(j>=i&&tab[find(b)][w[j]^1]>=0)b=find(tab[find(b)][w[j--]^1]);if(i>j){if(join(a,b))rebuild();}else if(i===j)edge(a,w[i],b);}
for(;;){let old;do{old=version;for(let c=0;c<parent.length;c++)if(find(c)===c)for(const w of rel)scan(c,w);}while(version!==old);
let gap=null;for(let c=0;c<parent.length&&!gap;c++)if(find(c)===c)for(let g=0;g<4;g++)if(tab[c][g]<0){gap=[c,g];break;}
if(!gap)break;if(parent.length>5000)throw Error("Coset cap; no conclusion");const d=parent.length;parent.push(d);tab.push([-1,-1,-1,-1]);edge(gap[0],gap[1],d);}
const reps=parent.map((_,i)=>i).filter(i=>find(i)===i),ix=new Map(reps.map((x,i)=>[x,i]));
const perms=[0,2].map(g=>reps.map(c=>ix.get(find(tab[c][g]))));let verified=true;
for(const c of reps)for(const w of rel){let d=c;for(const g of w)d=find(tab[d][g]);if(d!==c)verified=false;}
return{kind:signed?"signed":"projective",n,order:reps.length,allocated:parent.length,relators_verified:verified,s:perms[0],r:perms[1]};}
function ring(q,kind="residue"){
const add=kind==="F4"?(a,b)=>a^b:(a,b)=>mod(a+b,q),neg=kind==="F4"?a=>a:a=>mod(-a,q);
const mul=kind==="F4"?(a,b)=>{let x=0;for(let j=0;j<2;j++)if((b>>j)&1)x^=a<<j;if(x&4)x^=7;return x;}:(a,b)=>mod(a*b,q);
const units=Array.from({length:q},(_,a)=>a).filter(a=>Array.from({length:q},(_,b)=>b).some(b=>mul(a,b)===1));return{q,add,neg,mul,units};}
function matrixOps(R){
const{q,add,neg,mul,units}=R,key=A=>A.reduce((v,a,j)=>v+a*q**j,0);
const times=(A,B)=>[add(mul(A[0],B[0]),mul(A[1],B[2])),add(mul(A[0],B[1]),mul(A[1],B[3])),add(mul(A[2],B[0]),mul(A[3],B[2])),add(mul(A[2],B[1]),mul(A[3],B[3]))];
const det=A=>add(mul(A[0],A[3]),neg(mul(A[1],A[2]))),canon=A=>units.map(u=>A.map(a=>mul(u,a))).sort((A,B)=>key(A)-key(B))[0];
const enumerate=()=>{let all=[];for(let a=0;a<q;a++)for(let b=0;b<q;b++)for(let c=0;c<q;c++)for(let d=0;d<q;d++)all.push([a,b,c,d]);return all;};
function generated(gs,projective=false){const I=[1,0,0,1],out=[I],seen=new Set([key(I)]);for(let i=0;i<out.length;i++)for(const g of gs){let A=times(out[i],g);if(projective)A=canon(A);const k=key(A);if(!seen.has(k)){seen.add(k);out.push(A);}}return out;}
return{key,times,det,canon,enumerate,generated};}
const cosets=[];for(const signed of[false,true])for(const n of[2,3,4,5])cosets.push(tc(signed,n));
const counts=[],missed={};
for(const[name,q,kind]of[["F2",2],["F3",3],["F4",4,"F4"],["F5",5],["F7",7],["Z4",4],["Z9",9]]){
const R=ring(q,kind),O=matrixOps(R),all=O.enumerate(),sl=all.filter(A=>O.det(A)===1),gl=all.filter(A=>R.units.includes(O.det(A)));
const pgl=new Map(gl.map(A=>{const B=O.canon(A);return[O.key(B),B];})),psl=new Set(sl.map(A=>O.key(O.canon(A))));
const gs=[[0,R.neg(1),1,0],...Array.from({length:q},(_,t)=>[1,R.neg(t),0,1])],gen=O.generated(gs),missing=[...pgl.keys()].filter(k=>!psl.has(k)).sort((a,b)=>a-b);
counts.push({ring:name,SL2:sl.length,GL2:gl.length,PSL_word_image:psl.size,PGL2:pgl.size,elementary_image:gen.length,missed:missing.length});
missed[name]={base:q,encoding:"a+q*b+q^2*c+q^3*d; least scalar representative",codes:missing};}
const split=t=>[t%4,Math.floor(t/4)];
const add16=(a,b)=>{a=split(a);b=split(b);return mod(a[0]+b[0],4)+4*mod(a[1]+b[1],4);};
const neg16=a=>{a=split(a);return mod(-a[0],4)+4*mod(-a[1],4);};
const mul16=(a,b)=>{a=split(a);b=split(b);return mod(a[0]*b[0]-a[1]*b[1],4)+4*mod(a[0]*b[1]+a[1]*b[0]-a[1]*b[1],4);};
const tau=a=>{a=split(a);return mod(a[0]-a[1],4)+4*mod(-a[1],4);};
const R16={q:16,add:add16,neg:neg16,mul:mul16,units:Array.from({length:16},(_,a)=>a).filter(a=>Array.from({length:16},(_,b)=>b).some(b=>mul16(a,b)===1))};
const R4=ring(4),O4=matrixOps(R4),O16=matrixOps(R16),U4=a=>[1,mod(-a,4),0,1],U16=a=>[1,neg16(a),0,1];
const H=O4.generated([[0,3,1,0],U4(1)],true),C=new Set([0,1,2,3].map(a=>O4.key(O4.canon(U4(a)))));
const hs=H.filter(h=>!C.has(O4.key(h))),as=Array.from({length:12},(_,i)=>i+4),target=new Map(H.map(h=>[O16.key(O16.canon(h)),O4.key(h)]));
const records=[],image=new Set();let checked=0;
for(const a of as)for(const h of hs)for(const b of as){checked++;const ca=add16(tau(a),neg16(a)),cb=add16(tau(b),neg16(b));if(ca>=4||cb>=4)continue;const hh=O4.canon(O4.times(O4.times(U4(ca),h),U4(cb)));if(O4.key(hh)!==O4.key(h))continue;
const A=O16.canon(O16.times(O16.times(U16(a),h),U16(b)));if(!target.has(O16.key(A)))throw Error("Descended target not in listed PSL2(Z4)");records.push([a,O4.key(h),b]);image.add(target.get(O16.key(A)));}
const aset=[...new Set(records.map(x=>x[0]))].sort((a,b)=>a-b),hset=[...new Set(records.map(x=>x[1]))].sort((a,b)=>a-b),bset=[...new Set(records.map(x=>x[2]))].sort((a,b)=>a-b);
const descent={ring:"Z4[x]/(x^2+x+1)",tested:checked,fixed_words:records.length,a_codes:aset,h_matrix_codes:hset,b_codes:bset,cartesian_product_complete:records.length===aset.length*hset.length*bset.length,target_PSL_codes:[...image].sort((a,b)=>a-b),all_targets_square_determinant:true};
return{cosets,counts,missed,descent,limits:["Coset enumeration concerns abstract word pushouts, not fppf sheaf points.","Z4 descent search covers only U(a)hU(b) over the specified quadratic étale ring.","The Z4 full projective sheaf image remains 24 or 48."]};}
console.log(JSON.stringify(verifyC()));
