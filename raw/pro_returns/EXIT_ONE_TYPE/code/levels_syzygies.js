/* Exact expanded first-identity checker. Also runs in functions.exec.
 * Node: node levels_syzygies.js
 * Term [w,j,e] means w R_j^e w^-1; indices one-based.
 * Completeness is proved in P5c3--P5c4.
 */
const output = typeof text === "function" ? text : v => console.log(JSON.stringify(v));
const red = word => {
  const a=[];
  for(const x of word) {
    if(a.length && a[a.length-1]===-x)a.pop(); else a.push(x);
  }
  return a;
};
const inv=w=>[...w].reverse().map(x=>-x);
const mul=(...ws)=>red(ws.flat());
const sub=(w,a)=>mul(...w.map(x=>x>0?a[x-1]:inv(a[-x-1])));
const comm=(u,v)=>mul(inv(v),inv(u),v,u);
const conjugate=(w,v)=>mul(w,v,inv(w));
const identity=n=>Array.from({length:n},(_,i)=>[i+1]);
const compose=(a,b)=>b.map(w=>sub(w,a));
function artinGenerator(n,t) {
  const a=identity(n),i=Math.abs(t);
  if(t>0){a[i-1]=[i,i+1,-i];a[i]=[i];}
  else{a[i-1]=[i+1];a[i]=[-(i+1),i,i+1];}
  return a;
}
const artin=(n,w)=>w.reduce((a,t)=>compose(a,artinGenerator(n,t)),identity(n));
const pure=(i,j)=>[
  ...Array.from({length:j-i-1},(_,a)=>j-1-a),i,i,
  ...Array.from({length:j-i-1},(_,a)=>-(i+1+a))
];
function expandFamily(nb,nf,baseRelators,actions,inverseActions) {
  const embed=w=>w.map(x=>Math.sign(x)*(Math.abs(x)+nb));
  const relators=[...baseRelators];
  for(let h=1;h<=nb;h++)for(let u=1;u<=nf;u++)
    relators.push(mul([h],embed([u]),[-h],inv(embed(actions[h-1][u-1]))));
  const invertTerms=terms=>[...terms].reverse().map(t=>[t[0],t[1],-t[2]]);
  const conjugateTerms=(w,terms)=>terms.map(t=>[mul(w,t[0]),t[1],t[2]]);
  function letterD(h,v) {
    if(h<0)return conjugateTerms([h],invertTerms(letterD(-h,sub(v,inverseActions[-h-1]))));
    const terms=[],action=actions[h-1];let prefix=[];
    for(const u of v) {
      const image=action[Math.abs(u)-1],local=u>0?[]:inv(image);
      terms.push([embed(mul(prefix,local)),baseRelators.length+(h-1)*nf+Math.abs(u),Math.sign(u)]);
      prefix=mul(prefix,u>0?image:inv(image));
    }
    return terms;
  }
  function wordD(w,v) {
    let terms=[],image=v;
    for(const h of [...w].reverse()) {
      terms=[...conjugateTerms([h],terms),...letterD(h,image)];
      image=sub(image,h>0?actions[h-1]:inverseActions[-h-1]);
    }
    return {terms,image};
  }
  const identities=[];
  for(let i=0;i<baseRelators.length;i++)for(let u=1;u<=nf;u++) {
    const d=wordD(baseRelators[i],[u]);
    if(JSON.stringify(d.image)!==JSON.stringify([u]))throw Error("Nonidentity action");
    const terms=[[[],i+1,1],[embed([u]),i+1,-1],...invertTerms(d.terms)];
    let evaluated=[];
    for(const [w,j,sign] of terms) {
      const r=relators[j-1];
      evaluated=mul(evaluated,w,sign>0?r:inv(r),inv(w));
    }
    if(evaluated.length)throw Error("Expanded identity failed");
    identities.push({base_relator:i+1,fibre_generator:u,terms});
  }
  return {base_generators:nb,fibre_generators:nf,relators,identities};
}
const [x,y,z]=[[3],[4],[5]],cxz=comm(x,z),cyz=comm(y,z);
const images5=[[mul(inv(z),x,z),conjugate(cxz,y),mul(cxz,z)],
               [x,mul(inv(z),y,z),mul(cyz,z)]];
const relators5=[];
for(let h=1;h<=2;h++)for(let u=3;u<=5;u++)
  relators5.push(mul([h,u,-h],inv(images5[h-1][u-3])));
const braids5=[pure(1,3),pure(2,3),pure(1,4),pure(2,4),pure(3,4)];
const actions6=braids5.map(w=>artin(4,w.map(t=>-t)));
const inverse6=braids5.map(w=>artin(4,inv(w.map(t=>-t))));
const cubeBase=[];
for(const a of [1,2])for(const b of [3,4])cubeBase.push([a,b,-a,-b]);
const data={
  Gamma06:expandFamily(5,4,relators5,actions6,inverse6),
  Gamma05_times_F2:expandFamily(5,2,relators5,
    Array.from({length:5},()=>identity(2)),Array.from({length:5},()=>identity(2))),
  F2_cubed:expandFamily(4,2,cubeBase,
    Array.from({length:4},()=>identity(2)),Array.from({length:4},()=>identity(2)))
};
data.Gamma06.generator_names=[..."abxyzpqrs"];
data.Gamma05_times_F2.generator_names=["a","b","x","y","z","t1","t2"];
data.F2_cubed.generator_names=["a1","a2","b1","b2","c1","c2"];
const expected={
 Gamma06:[26,24,[36,64,16,26,366,640,168,144,92,178,44,52,18,42,36,12,8,36,16,26,10,92,44,52],171],
 Gamma05_times_F2:[16,12,[8,8,14,14,10,10,6,6,8,8,10,10],11],
 F2_cubed:[12,8,[6,6,6,6,6,6,6,6],4]
};
const summaries=[];
for(const [name,f] of Object.entries(data)) {
 const counts=f.identities.map(x=>x.terms.length);
 const longest=Math.max(...f.identities.flatMap(x=>x.terms.map(t=>t[0].length)));
 const actual=[f.relators.length,f.identities.length,counts,longest];
 if(JSON.stringify(actual)!==JSON.stringify(expected[name]))throw Error("Unexpected counts");
 const summary={name,relators:actual[0],checked_identities:actual[1],
   conjugate_factor_counts:counts,maximum_conjugator_length:longest,
   all_freely_reduce_to_identity:true};
 summaries.push(summary);output(summary);
}
if(typeof store==="function") {
 store("levels_expanded_syzygies",data);store("levels_syzygies_js_output",summaries);
}
if(typeof process!=="undefined" && typeof require==="function") {
 const fs=require("fs"),path=require("path");
 fs.writeFileSync(path.join(__dirname,"levels_syzygies_expanded.json"),JSON.stringify(data,null,2)+"\n");
 fs.writeFileSync(path.join(__dirname,"levels_syzygies_js_output.json"),JSON.stringify(summaries,null,2)+"\n");
}
