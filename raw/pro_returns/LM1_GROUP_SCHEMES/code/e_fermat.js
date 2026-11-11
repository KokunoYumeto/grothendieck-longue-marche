/* Exact Schreier graph checks for F2 -> (Z/n)^2. No dependencies. */
function reduceWord(word) {
  const result=[];
  for (const letter of word) {
    if(result.length && result[result.length-1]===-letter) result.pop();
    else result.push(letter);
  }
  return result;
}
function inverseWord(w) { return w.slice().reverse().map(a=>-a); }
function displayWord(w) {
  if(!w.length) return "1";
  return w.map(a=>({1:"x","-1":"x^-1",2:"y","-2":"y^-1"})[a]).join(" ");
}
function quotientWord(w,n) {
  let a=0,b=0;
  for(const z of w) {
    if(Math.abs(z)===1) a+=Math.sign(z); else b+=Math.sign(z);
  }
  return [((a%n)+n)%n,((b%n)+n)%n];
}
function checkFermat(n) {
  const key=v=>v.join(",");
  const reps=new Map([["0,0",[]]]);
  const queue=[[0,0]];
  const tree=new Set();
  for(let i=0;i<queue.length;i++) {
    const v=queue[i], r=reps.get(key(v));
    for(const z of [1,2]) {
      const t=[(v[0]+(z===1?1:0))%n,(v[1]+(z===2?1:0))%n];
      if(!reps.has(key(t))) {
        reps.set(key(t),r.concat(z)); queue.push(t);
        tree.add(key(v)+":"+z);
      }
    }
  }
  const generators=[];
  for(const v of queue) for(const z of [1,2]) {
    const t=[(v[0]+(z===1?1:0))%n,(v[1]+(z===2?1:0))%n];
    const w=reduceWord(reps.get(key(v)).concat([z],inverseWord(reps.get(key(t)))));
    if(tree.has(key(v)+":"+z)) {
      if(w.length) throw new Error("tree word not trivial");
    } else {
      if(!w.length) throw new Error("non-tree word trivial");
      const q=quotientWord(w,n);
      if(q[0]||q[1]) throw new Error("generator not in kernel");
      generators.push(w);
    }
  }
  if(reps.size!==n*n || tree.size!==n*n-1 || generators.length!==n*n+1)
    throw new Error("Euler/Schreier count failed");
  return {n,vertices:reps.size,positive_edges:2*n*n,tree_edges:tree.size,
          kernel_rank:generators.length,generators_n2:n===2?generators.map(displayWord):undefined};
}
const checks=Array.from({length:12},(_,i)=>checkFermat(i+1));
const lines=checks.map(o=>"n="+o.n+" vertices="+o.vertices+" edges="+o.positive_edges+
  " spanning_tree="+o.tree_edges+" kernel_rank="+o.kernel_rank);
lines.push("n=2 Schreier basis: "+checks[1].generators_n2.join(" ; "));
lines.push("ALL SCHREIER GRAPH ASSERTIONS PASSED.");
const rendered=lines.join("\n")+"\n";
if(typeof text==="function") text(rendered); else console.log(rendered);
if(typeof store==="function") store("E_fermat_output",rendered);
