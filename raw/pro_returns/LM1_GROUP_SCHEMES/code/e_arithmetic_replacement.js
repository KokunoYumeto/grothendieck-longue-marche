"use strict";
function verifyEArithmetic() {
  const check=(c,m)=>{if(!c)throw Error(m);};
  const abs=n=>n<0n?-n:n;
  const gcd=(a,b)=>{a=abs(a);b=abs(b);while(b){const c=a%b;a=b;b=c;}return a;};
  const Q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);check(b!==0n,"zero denominator");if(b<0n){a=-a;b=-b;}const d=gcd(a,b);return [a/d,b/d];};
  const qa=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const qn=a=>[-a[0],a[1]];
  const qs=(a,b)=>qa(a,qn(b));
  const qm=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
  const qd=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const qe=(a,b)=>a[0]===b[0]&&a[1]===b[1];
  const qstr=a=>a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);
  const fact=n=>{let f=1n;for(let i=2;i<=n;i++)f*=BigInt(i);return f;};
  const zero=n=>Array.from({length:n},()=>Array.from({length:n},()=>Q(0)));
  const eye=n=>{const A=zero(n);for(let i=0;i<n;i++)A[i][i]=Q(1);return A;};
  const ma=(A,B)=>A.map((r,i)=>r.map((a,j)=>qa(a,B[i][j])));
  const ms=(A,c)=>A.map(r=>r.map(a=>qm(a,c)));
  const mm=(A,B)=>A.map((r,i)=>B[0].map((_,j)=>r.reduce((s,a,k)=>qa(s,qm(a,B[k][j])),Q(0))));
  const mp=(A,n)=>{let B=eye(A.length);for(let j=0;j<n;j++)B=mm(B,A);return B;};
  const me=(A,B)=>A.every((r,i)=>r.every((a,j)=>qe(a,B[i][j])));
  const integral=A=>A.every(r=>r.every(a=>a[1]===1n));
  const mstr=A=>A.map(r=>r.map(qstr));
  const exp=A=>{let B=eye(A.length);for(let j=1;j<A.length;j++)B=ma(B,ms(mp(A,j),Q(1,fact(j))));check(me(mp(A,A.length),zero(A.length)),"nilpotence for exp");return B;};
  const log1=N=>{let A=zero(N.length);for(let j=1;j<N.length;j++)A=ma(A,ms(mp(N,j),Q(j%2?1:-1,j)));return A;};
  const X=zero(4);X[0][1]=Q(3,2);X[0][2]=Q(-2);X[1][2]=Q(4);X[2][3]=Q(1,2);
  const A=ms(mp(X,2),Q(1,2)),B=ms(mp(X,3),Q(1,6));
  check(integral(ma(A,B))&&integral(ma(A,ms(B,Q(-1)))),"signed integral combinations");
  check(!integral(A)&&!integral(B)&&!integral(exp(X)),"signed example scope");
  const twice=ms(X,Q(2));
  let content=0n;for(const r of twice)for(const a of r){check(a[1]===1n,"2X integral");content=gcd(content,a[0]);}
  check(content===1n,"2X primitive");
  const signed={X:mstr(X),X2_over_2:mstr(A),X3_over_6:mstr(B),
    plus_integral:integral(ma(A,B)),minus_integral:integral(ma(A,ms(B,Q(-1)))),
    plus_with_X3_over_2_integral:integral(ma(A,ms(mp(X,3),Q(1,2)))),
    minus_with_X3_over_2_integral:integral(ma(A,ms(mp(X,3),Q(-1,2)))),
    exp_X_integral:integral(exp(X)),content_2X:String(content)};
  let witnesses=[];
  for(let a=1;a<=7;a++)for(let b=1;b<=12;b++)for(let c=1;c<=7;c++)for(let d=-4;d<=4;d++){
    if(a*b%4===0&&b*c%4===0&&(6*d*c+a*b*c)%24===0&&(6*d*c-a*b*c)%24===0&&(d*c%4!==0||a*b*c%24!==0))
      witnesses.push([Math.max(a,2*b,c,2*Math.abs(d)),a,b,c,d]);
  }
  witnesses.sort((a,b)=>{for(let i=0;i<a.length;i++)if(a[i]!==b[i])return a[i]-b[i];return 0;});
  check(witnesses.length===46,"signed-family count");
  const J=zero(3);J[0][1]=J[1][2]=Q(1);
  const X3=log1(J);
  check(me(exp(X3),ma(eye(3),J)),"rank-three exponential");
  check(integral(exp(X3))&&integral(exp(ms(X3,Q(-1)))),"rank-three exponentials integral");
  const N=zero(5);[1,6,1,6].forEach((w,i)=>N[i][i+1]=Q(w));
  const X5=log1(N),dp5=Array.from({length:5},(_,j)=>integral(ms(mp(X5,j),Q(1,fact(j)))));
  check(integral(X5)&&me(exp(X5),ma(eye(5),N)),"rank-five integral logarithm");
  check(JSON.stringify(dp5)==="[true,true,false,true,false]","rank-five divided powers");
  const divisible=(M,p)=>M.every(r=>r.every(a=>a[1]===1n&&a[0]%BigInt(p)===0n));
  check(divisible(mp(N,2),2)&&divisible(mp(N,3),3)&&me(mp(N,5),zero(5)),"geometric-fibre tests");
  const rank_examples={rank3_log:mstr(X3),rank3_exp_integral:true,rank3_inverse_exp_integral:true,
    rank3_divided_power_flags:Array.from({length:3},(_,j)=>integral(ms(mp(X3,j),Q(1,fact(j))))),
    rank5_log:mstr(X5),rank5_divided_power_flags:dp5,rank5_top_divided_power:qstr(ms(mp(X5,4),Q(1,24))[0][4]),
    rank5_N2_divisible_by_2:true,rank5_N3_divisible_by_3:true,rank5_N5_zero:true};
  const trim=a=>{while(a.length>1&&a[a.length-1][0]===0n)a.pop();return a;};
  const pa=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>qa(a[i]||Q(0),b[i]||Q(0))));
  const ps=(a,c)=>trim(a.map(x=>qm(x,c)));
  const pm=(a,b)=>{const c=Array.from({length:a.length+b.length-1},()=>Q(0));a.forEach((x,i)=>b.forEach((y,j)=>c[i+j]=qa(c[i+j],qm(x,y))));return trim(c);};
  const pe=(a,b)=>{a=trim(a.slice());b=trim(b.slice());return a.length===b.length&&a.every((x,i)=>qe(x,b[i]));};
  const binomials=[[Q(1)]],formalExp=[[Q(1)]];
  for(let n=1;n<=12;n++){
    binomials.push(ps(pm(binomials[n-1],[Q(-(n-1)),Q(1)]),Q(1,n)));
    let sum=[Q(0)];
    for(let k=1;k<=n;k++)sum=pa(sum,ps(pm([Q(0),Q(1)],formalExp[n-k]),Q(k%2?1:-1,n)));
    formalExp.push(sum);check(pe(binomials[n],formalExp[n]),"independent exp/binomial recurrence degree "+n);
  }
  const vp=(n,p)=>{n=abs(n);check(n!==0n,"valuation of zero");let v=0;while(n%BigInt(p)===0n){n/=BigInt(p);v++;}return v;};
  const vq=(a,p)=>a[0]===0n?Infinity:vp(a[0],p)-vp(a[1],p);
  const valuations=[2,3,5].map(p=>({p,minimum_binomial_coefficient_valuations:binomials.map(b=>Math.min(...b.map(a=>vq(a,p))))}));
  const searches=[];
  for(const p of [2,3,5]){
    let tested=0,admissible=0,failures=0,first=null,by_degree=[];
    for(let d=1;d<=12;d++){
      let a=0,f=0;
      for(let mask=0;mask<(1<<d);mask++){
        tested++;let ok=true,ones=0;
        for(let i=0;i<d;i++)ones+=(mask>>i)&1;
        for(let i=0;i+p<=d;i++){let sum=0;for(let j=0;j<p;j++)sum+=(mask>>(i+j))&1;if(sum===0){ok=false;break;}}
        if(!ok)continue;a++;admissible++;
        if(ones-vp(fact(d),p)<0){f++;failures++;if(first===null)first=d;}
      }
      by_degree.push({degree:d,admissible:a,failures:f});
    }
    searches.push({p,tested,admissible,failures,first_failure_degree:first,by_degree});
  }
  check(searches[0].admissible===984&&searches[0].failures===604&&searches[0].first_failure_degree===4,"p=2 weighted search");
  check(searches[1].admissible===3734&&searches[1].failures===30&&searches[1].first_failure_degree===9,"p=3 weighted search");
  check(searches[2].admissible===7172&&searches[2].failures===0,"p=5 weighted search");
  const sharp=[2,3,5].map(p=>({p,degree:p*p,rank:p*p+1,top_valuation:p-vp(fact(p*p),p)}));
  check(sharp.every(a=>a.top_valuation===-1),"all sharp top valuations");
  function Ring(modulus,nv,truncateIndex=-1){
    const m=BigInt(modulus),norm=c=>m?((c%m)+m)%m:c,zero=()=>new Map(),key=e=>e.join(",");
    function put(P,e,c){if(truncateIndex>=0&&e[truncateIndex]>=2)return;const k=key(e),v=norm((P.get(k)||0n)+c);if(v)P.set(k,v);else P.delete(k);}
    const constant=c=>{const P=zero();put(P,Array(nv).fill(0),BigInt(c));return P;};
    const variable=i=>{const P=zero(),e=Array(nv).fill(0);e[i]=1;put(P,e,1n);return P;};
    const add=(P,Q)=>{const R=new Map(P);for(const [k,c] of Q)put(R,k.split(",").map(Number),c);return R;};
    const scale=(P,c)=>{const R=zero();for(const [k,a] of P)put(R,k.split(",").map(Number),a*BigInt(c));return R;};
    const neg=P=>scale(P,-1);
    const sub=(P,Q)=>add(P,neg(Q));
    const mul=(P,Q)=>{const R=zero();for(const [k,a] of P)for(const [l,b] of Q){const e=k.split(",").map(Number),f=l.split(",").map(Number);put(R,e.map((v,i)=>v+f[i]),a*b);}return R;};
    const pow=(P,n)=>{let R=constant(1);for(let i=0;i<n;i++)R=mul(R,P);return R;};
    const eq=(P,Q)=>sub(P,Q).size===0;
    const display=(P,names)=>[...P].sort((a,b)=>{const e=a[0].split(",").map(Number),f=b[0].split(",").map(Number);for(let i=0;i<nv;i++)if(e[i]!==f[i])return f[i]-e[i];return 0;}).map(([k,c])=>String(c)+"*"+k.split(",").map((e,i)=>Number(e)?names[i]+"^"+e:"").filter(Boolean).join("*")).join(" + ")||"0";
    return {zero,constant,variable,add,sub,scale,mul,pow,eq,display};
  }
  const choose=(n,k)=>{let a=1;for(let i=1;i<=k;i++)a=a*(n-i+1)/i;check(Number.isInteger(a),"binomial integer");return a;};
  const cp=(R,p,a,b)=>{let P=R.zero();for(let i=1;i<p;i++)P=R.add(P,R.scale(R.mul(R.pow(a,i),R.pow(b,p-i)),choose(p,i)/p));return P;};
  const mod=(a,m)=>((a%m)+m)%m;
  const deformations=[],witt=[];
  for(const p of [2,3,5]){
    const Z=Ring(0,3),zx=Z.variable(0),zy=Z.variable(1),zz=Z.variable(2);
    const cocycle=Z.sub(Z.add(cp(Z,p,zx,zy),cp(Z,p,Z.add(zx,zy),zz)),Z.add(cp(Z,p,zy,zz),cp(Z,p,zx,Z.add(zy,zz))));
    check(cocycle.size===0,"integral cocycle p="+p);
    const R=Ring(p*p,3),x=R.variable(0),y=R.variable(1),z=R.variable(2);
    const law=(a,b)=>R.add(R.add(a,b),R.scale(cp(R,p,a,b),p));
    check(R.eq(law(law(x,y),z),law(x,law(y,z))),"symbolic associativity p="+p);
    const inverse=R.sub(R.scale(x,-1),R.scale(cp(R,p,x,R.scale(x,-1)),p));
    check(law(x,inverse).size===0&&law(inverse,x).size===0,"symbolic inverse p="+p);
    let multiple=R.zero();for(let i=0;i<p;i++)multiple=law(multiple,x);
    check(R.eq(multiple,R.scale(R.sub(x,R.pow(x,p)),p)),"symbolic p multiple p="+p);
    const F=Ring(p,1),t=F.variable(0),degrees=[];for(let d=1;d<=12;d*=p)degrees.push(d);
    let candidates=0,survivors=0;
    for(let code=0;code<p**degrees.length;code++){
      let q=code,B=F.zero(),coeffs=[],sum=0;
      for(const d of degrees){const c=q%p;q=Math.floor(q/p);coeffs.push(c);sum+=c;B=F.add(B,F.scale(F.pow(t,d),c));}
      if(sum%p!==1)continue;candidates++;
      if(F.sub(F.sub(B,F.pow(B,p)),F.scale(t,coeffs[0])).size===0)survivors++;
    }
    check(survivors===0,"no normalized additive survivors p="+p);
    const cpnum=(a,b)=>{let c=0;for(let i=1;i<p;i++)c+=(choose(p,i)/p)*a**i*b**(p-i);return c;};
    const star=(a,b)=>mod(a+b+p*cpnum(a,b),p*p);
    let finiteTriples=0;
    for(let a=0;a<p*p;a++)for(let b=0;b<p*p;b++)for(let c=0;c<p*p;c++){check(star(star(a,b),c)===star(a,star(b,c)),"finite deformation associativity");finiteTriples++;}
    let g=0,order=0;for(let i=1;i<=p*p;i++){g=star(g,1);if(g===0){order=i;break;}}
    check(order===p,"deformation section order");
    deformations.push({p,cocycle_integral:true,associativity_symbolic:true,inverse_symbolic:true,
      p_multiple:R.display(multiple,["T","U","V"]),finite_associativity_triples:finiteTriples,
      section_1_order:order,additive_degrees:degrees,normalized_candidates:candidates,survivors});
    const plus=(a,b)=>[mod(a[0]+b[0],p),mod(a[1]+b[1]-cpnum(a[0],b[0]),p)];
    const veq=(a,b)=>a[0]===b[0]&&a[1]===b[1],els=[];
    for(let a=0;a<p;a++)for(let b=0;b<p;b++)els.push([a,b]);
    let triples=0;for(const a of els)for(const b of els)for(const c of els){check(veq(plus(plus(a,b),c),plus(a,plus(b,c))),"Witt associativity");triples++;}
    let v=[0,0],atp=null,wittorder=0;for(let j=1;j<=p*p;j++){v=plus(v,[1,0]);if(j===p)atp=v.slice();if(veq(v,[0,0])){wittorder=j;break;}}
    check(veq(atp,[0,1])&&wittorder===p*p,"Witt section order");
    witt.push({p,p_times_1_0:atp,order:wittorder,associativity_triples:triples,wound_coefficient_t_valuation:1-p,
      valuation_not_divisible_by_p:mod(1-p,p)!==0});
  }
  const D=Ring(0,3,2),t=D.variable(0),u=D.variable(1),epsilon=D.variable(2),one=D.constant(1);
  const diagonal=v=>D.add(one,D.mul(epsilon,v));
  const twiceUpper=v=>D.add(D.scale(v,2),D.mul(epsilon,D.sub(D.pow(v,2),v)));
  check(D.eq(diagonal(D.add(t,u)),D.mul(diagonal(t),diagonal(u))),"dual diagonal group law");
  check(D.eq(twiceUpper(D.add(t,u)),D.add(D.mul(diagonal(t),twiceUpper(u)),twiceUpper(t))),"dual upper group law");
  check(D.eq(diagonal(one),D.add(one,epsilon))&&D.eq(twiceUpper(one),D.constant(2)),"dual value at one");
  return {signed_counterexample:signed,signed_family:{tested:7*12*7*9,witnesses:witnesses.length,
      first_by_height_then_parameters:witnesses[0],height_definition:"max(a,2*b,c,2*abs(d))"},
    rank_examples,formal_exponential_equals_binomial_through_degree:12,binomial_valuations:valuations,
    weighted_searches:searches,sharp_examples:sharp,deformations,witt,
    dual_numbers:{scalar_group_law:true,matrix_group_law:true,value_at_one:true},
    result:"ALL EXACT ARITHMETIC ASSERTIONS PASSED."};
}
const arithmeticResult=verifyEArithmetic();
const arithmeticOutput=JSON.stringify(arithmeticResult);
if(typeof text==="function")text(arithmeticOutput);else console.log(arithmeticOutput);
if(typeof store==="function")store("e_arithmetic_replacement.out",arithmeticOutput);
