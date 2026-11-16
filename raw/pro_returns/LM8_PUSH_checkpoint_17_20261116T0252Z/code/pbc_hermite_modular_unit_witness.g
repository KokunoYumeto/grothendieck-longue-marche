# Original-presentation modular Hopf-torsion witness.
# Exact targeted source-centralization test.  The central tail module is
# reduced by integer Euclidean row operations, including nonunit pivots.
# Extra rows are s^2, r^3, and centralizer commutators.  Sparse labels retain
# their integer coefficients, so successful reduction supplies actual frame
# correction words.  No finite-field or rational linear algebra is used.
Read("LM8_PUSH/code/pbc_sparse_schur.g");;
Read("LM8_PUSH/code/pbc_central_collector_v2.g");;
PBC_HermiteModularUnitWitness:=function(data)
 local g,n,orders,m,coll,zero,ps,baseconjs,basecomm,abelStart,
       powers,conjs,k,i,j,e,a,word,inverse,centralTail,sw,rw,bsw,brw,
       extras,weights,basis,basisweights,pivots,relcount,target,targetw,
       reduce,insert,check,found,result,relation,sparseRelation,
       exteriorRelation,w1,w2,makevec,profile,t0,initialTarget,initialExtras,normalizeWeights,cs,cr,traceStream,traceId,newLeaf,newOp,newNeg,basisproof,targetproof,currentRelation,centralDifference,centralConj,originalConjugates,collectShortcut,baseCommute,zz,hh,modulus,newMul;

 orders:=data.orders;n:=Length(orders);m:=n*(n+1)/2;modulus:=data.modulus;
 cs:=data.cs;cr:=data.cr;
 traceStream:=OutputTextFile(Concatenation(data.trace_stem,".jsonl"),false);
 SetPrintFormattingStatus(traceStream,false);
 PrintTo(traceStream,"[\"source\",\"",data.source_sha256,"\",",n,",",m,",",modulus,"]\n");
 traceId:=0;
 newLeaf:=function(kind,meta,v)
  traceId:=traceId+1;
  PrintTo(traceStream,"[\"leaf\",",traceId,",\"",kind,"\",",meta,",",v,"]\n");
  return traceId;
 end;
 newOp:=function(a,q,b)
  traceId:=traceId+1;
  PrintTo(traceStream,"[\"sub\",",traceId,",",a,",",q,",",b,"]\n");
  return traceId;
 end;
 newNeg:=function(a)
  traceId:=traceId+1;PrintTo(traceStream,"[\"neg\",",traceId,",",a,"]\n");
  return traceId;
 end;
 newMul:=function(u,a)
  traceId:=traceId+1;PrintTo(traceStream,"[\"mul\",",traceId,",",u,",",a,"]\n");
  return traceId;
 end;
 coll:=FromTheLeftCollector(n+m);baseconjs:=List([1..n],i->[]);k:=n;
 for i in [1..n] do
  SetRelativeOrder(coll,i,orders[i]);e:=ShallowCopy(data.powers[i]);k:=k+1;Append(e,[k,1]);SetPower(coll,i,e);
  for j in [1..i-1] do
   e:=ShallowCopy(data.conjugates[i][j]);baseconjs[i][j]:=ShallowCopy(e);k:=k+1;Append(e,[k,1]);SetConjugate(coll,i,j,e);
  od;
  if i mod 10=0 then Print("witness_source_build ",i," runtime ",Runtime(),"\n");fi;
 od;

 # This is exactly the usual commutation bound of the FINITE base
 # presentation.  Deleted formal commutators are accounted for by
 # PBC_CentralCollectV2, including in the class-two suffix.
 baseCommute:=ListWithIdenticalEntries(n,n);
 for zz in [n-1,n-2..1] do
  hh:=n;
  while hh>baseCommute[zz+1] and baseconjs[hh][zz]=[hh,1] do hh:=hh-1;od;
  if hh=zz+1 and baseconjs[hh][zz]=[hh,1] then baseCommute[zz]:=zz;
  else baseCommute[zz]:=hh;fi;
 od;
 coll![PC_COMMUTE]:=Concatenation(baseCommute,[n+1..n+m]);
 SetFilterObj(coll,IsUpToDatePolycyclicCollector);
 zero:=ListWithIdenticalEntries(n+m,0);
 ps:=List([1..n],i->[]);
 for i in [1..n] do
  ps[i][i]:=ShallowCopy(GetPower(coll,i));
  for j in [1..i-1] do ps[i][j]:=Concatenation([j,1],GetConjugate(coll,i,j));od;
 od;

 centralConj:=List([1..n],i->[]);
 originalConjugates:=List([1..n],i->[]);
 for i in [1..n] do for j in [1..i-1] do
  e:=ShallowCopy(GetConjugate(coll,i,j));originalConjugates[i][j]:=e;
  if baseconjs[i][j]=[i,1] then
   Assert(0,e{[1,2]}=[i,1] and ForAll([3,5..Length(e)-1],k->e[k]>n));
   centralConj[i][j]:=e{[3..Length(e)]};
   SetConjugate(coll,i,j,[i,1]);
  fi;
 od;od;
 coll![PC_COMMUTE]:=Concatenation(baseCommute,[n+1..n+m]);
 SetFilterObj(coll,IsUpToDatePolycyclicCollector);
 collectShortcut:=function(v,w)
  return PBC_CentralCollectV2(coll,v,w,n,centralConj);
 end;
 makevec:=function(w)
  local v,ii;v:=ShallowCopy(zero);for ii in [1,3..Length(w)-1] do v[w[ii]]:=w[ii+1];od;return v;
 end;
 centralTail:=function(w)
  local v,tail,ii,retry;v:=ShallowCopy(zero);retry:=0;while collectShortcut(v,w)=fail do v:=ShallowCopy(zero);retry:=retry+1;od;if retry>0 then Print("collector_stack_retries ",retry,"\n");fi;
  if not ForAll(v{[1..n]},a->a=0) then Print("unexpected_base_word ",w," collected_base ",v{[1..n]},"\n");Error("initial base collection");fi;tail:=[];
  for ii in [1..m] do if v[n+ii]<>0 then Append(tail,[ii,v[n+ii]]);fi;od;return tail;
 end;

 centralDifference:=function(a,b)
  local va,vb,tail,ii;
  va:=ShallowCopy(zero);vb:=ShallowCopy(zero);
  while collectShortcut(va,a)=fail do va:=ShallowCopy(zero);od;
  while collectShortcut(vb,b)=fail do vb:=ShallowCopy(zero);od;
  Assert(0,va{[1..n]}=vb{[1..n]});tail:=[];
  for ii in [1..m] do
   if va[n+ii]<>vb[n+ii] then Append(tail,[ii,va[n+ii]-vb[n+ii]]);fi;
  od;
  return tail;
 end;
 sw:=data.s;rw:=data.r;bsw:=data.bs;brw:=data.br;
 Print("witness_source ",n," generators ",m," central tails runtime ",Runtime(),"\n");
 extras:=List(data.initial_extras,ShallowCopy);
 target:=ShallowCopy(data.initial_target);
 initialTarget:=ShallowCopy(target);initialExtras:=List(extras,ShallowCopy);
 Print("witness_initial_words ",Length(extras)," extras target_support ",Length(target)/2," runtime ",Runtime(),"\n");
 basis:=[];basisweights:=[];basisproof:=[];pivots:=0;relcount:=0;profile:=[0,0];found:=false;targetw:=[];targetproof:=newLeaf("target",[],target);currentRelation:=[];
 # If c centralizes s modulo the central kernel, [c,s] is central
 # and [c,s]^2=[c,s^2]=1; similarly the r-commutators have order|3.
 # Reducing only these labelled coefficients modulo2 or3 therefore uses
 # proved exact group relations.  The two power-word coefficients remain
 # integral and unreduced.
 normalizeWeights:=function(w)
  local out,ii,cc;out:=[];
  for ii in [1,3..Length(w)-1] do
   cc:=w[ii+1];
   if w[ii]>2 and w[ii]<=2+Length(cs) then cc:=cc mod 2;
   elif w[ii]>2+Length(cs) then cc:=cc mod 3;fi;
   if cc<>0 then Append(out,[w[ii],cc]);fi;
  od;return out;
 end;
 reduce:=function(v,w,proof)
  local acc,touched,active,ii,idx,row,d,q,ww,out,coef,pr;
  acc:=[];touched:=[];active:=[];ww:=ShallowCopy(w);pr:=proof;
  for ii in [1,3..Length(v)-1] do idx:=v[ii];acc[idx]:=v[ii+1];Add(touched,idx);AddSet(active,idx);od;
  while Length(active)>0 do
   idx:=active[1];Remove(active,1);coef:=acc[idx];
   if coef=0 or not IsBound(basis[idx]) then continue;fi;
   row:=basis[idx];d:=row[2];q:=(coef-(coef mod d))/d;
   if q=0 then continue;fi;
   acc[idx]:=coef-q*d;
   for ii in [3,5..Length(row)-1] do
    idx:=row[ii];if not IsBound(acc[idx]) then acc[idx]:=0;Add(touched,idx);fi;
    acc[idx]:=(acc[idx]-q*row[ii+1]) mod modulus;if acc[idx]<>0 then AddSet(active,idx);fi;
   od;
   ww:=normalizeWeights(PBC_SparseAdd(ww,basisweights[row[1]],-q));pr:=newOp(pr,q,basisproof[row[1]]);
  od;
  Sort(touched);out:=[];
  for idx in touched do if acc[idx]<>0 then Append(out,[idx,acc[idx]]);fi;od;
  return [out,ww,pr];
 end;
 insert:=function(v,w,proof)
  local reduced,idx,old,oldw,oldproof,ii,eg,u,step,tries,vv,ww,cc;
  while Length(v)>0 do
   reduced:=reduce(v,w,proof);v:=reduced[1];w:=reduced[2];proof:=reduced[3];
   if Length(v)=0 then return;fi;
   if v[2]<0 then
    for ii in [2,4..Length(v)] do v[ii]:=-v[ii];od;
    for ii in [2,4..Length(w)] do w[ii]:=-w[ii];od;proof:=newNeg(proof);
   fi;
   # Multiplication by a unit of Z/N preserves the row module.
   # Normalize c to gcd(c,N) in one explicit, replayable operation.
   eg:=Gcdex(v[2],modulus);step:=modulus/eg.gcd;u:=eg.coeff1 mod modulus;
   tries:=0;
   while GcdInt(u,modulus)<>1 do
    u:=(u+step) mod modulus;tries:=tries+1;
    Assert(0,tries<=6);
   od;
   Assert(0,(u*v[2]) mod modulus=eg.gcd);
   if u<>1 then
    vv:=[];
    for ii in [1,3..Length(v)-1] do
     cc:=(u*v[ii+1]) mod modulus;if cc<>0 then Append(vv,[v[ii],cc]);fi;
    od;
    v:=vv;
    for ii in [2,4..Length(w)] do w[ii]:=u*w[ii];od;
    proof:=newMul(u,proof);
   fi;
   w:=normalizeWeights(w);idx:=v[1];
   if not IsBound(basis[idx]) then
    basis[idx]:=v;basisweights[idx]:=w;basisproof[idx]:=proof;pivots:=pivots+1;return;
   fi;
   Assert(0,v[2]<basis[idx][2]);if basis[idx][2]=modulus then pivots:=pivots+1;fi;old:=basis[idx];oldw:=basisweights[idx];oldproof:=basisproof[idx];basis[idx]:=v;basisweights[idx]:=w;basisproof[idx]:=proof;v:=old;w:=oldw;proof:=oldproof;
  od;
 end;
 check:=function()
  local red,coeffs,ii;
  red:=reduce(target,targetw,targetproof);target:=red[1];targetw:=red[2];targetproof:=red[3];
  if Length(target)>0 then return false;fi;
  coeffs:=ListWithIdenticalEntries(Length(extras),0);
  for ii in [1,3..Length(targetw)-1] do coeffs[targetw[ii]]:=targetw[ii+1];od;
  Assert(0,coeffs[1]=0 and coeffs[2]=0);result:=rec(success:=true,coefficients:=coeffs,relations:=relcount,pivots:=pivots,
    s_count:=Length(cs),r_count:=Length(cr),initial_target:=initialTarget,initial_extras:=initialExtras,proof_node:=targetproof);
  PrintTo(traceStream,"[\"success\",",targetproof,",",coeffs,"]\n");CloseStream(traceStream);found:=true;Print("witness_found after_relations ",relcount," pivots ",pivots," coefficients ",coeffs," runtime ",Runtime(),"\n");return true;
 end;
 # N times each ORIGINAL tail is zero in K/NK. Hopf torsion embeds
 # in that quotient. Only genuine centralizer commutators are inserted;
 # the two power words are deliberately excluded.
 for i in [1..m] do
  basis[i]:=[i,modulus];basisweights[i]:=[];
  basisproof[i]:=newLeaf("modulus",[i],[i,modulus]);
 od;
 for i in [3..Length(extras)] do insert(extras[i],[i,1],newLeaf("extra",[i],extras[i]));od;
 if check() then return result;fi;
 sparseRelation:=function(tail)
  local tt;if Length(tail)=0 then return;fi;
  relcount:=relcount+1;tt:=Runtime();insert(tail,[],newLeaf("identity",currentRelation,tail));profile[1]:=profile[1]+Runtime()-tt;
  if relcount mod 250=0 then
   if check() then return;fi;
   Print("witness_relations ",relcount," pivots ",pivots," target_support ",Length(target)/2," runtime ",Runtime()," profile ",profile,"\n");
  fi;
 end;
 relation:=function(v,w)
  local tail,ii,diff;Assert(0,v{[1..n]}=w{[1..n]});if v=w then return;fi;
  tail:=[];for ii in [1..m] do diff:=v[n+ii]-w[n+ii];if diff<>0 then Append(tail,[ii,diff]);fi;od;sparseRelation(tail);
 end;
 basecomm:=List([1..n],i->List([1..i-1],j->baseconjs[i][j]=[i,1]));abelStart:=n;
 while abelStart>1 and ForAll([abelStart..n],jj->basecomm[jj][abelStart-1]) do abelStart:=abelStart-1;od;
 exteriorRelation:=function(ii,jj,kk)
  local acc,touched,addcomm,aa,bb,wa,wb,coef,tail,pos0,tt;
  tt:=Runtime();acc:=[];touched:=[];
  addcomm:=function(ll,mm,cc)
   local cw,t,idx;if cc=0 then return;fi;cw:=originalConjugates[ll][mm];
   for t in [1,3..Length(cw)-1] do if cw[t]>n then
    idx:=cw[t]-n;if not IsBound(acc[idx]) then acc[idx]:=0;Add(touched,idx);fi;acc[idx]:=acc[idx]+cc*cw[t+1];fi;
   od;
  end;
  addcomm(kk,jj,1);wa:=baseconjs[kk][ii];wb:=baseconjs[jj][ii];
  for aa in [1,3..Length(wa)-1] do
   Assert(0,wa[aa]>=abelStart);
   for bb in [1,3..Length(wb)-1] do
    Assert(0,wb[bb]>=abelStart);coef:=wa[aa+1]*wb[bb+1];
    if wa[aa]>wb[bb] then addcomm(wa[aa],wb[bb],-coef);elif wa[aa]<wb[bb] then addcomm(wb[bb],wa[aa],coef);fi;
   od;
  od;
  Sort(touched);tail:=[];for pos0 in touched do if acc[pos0]<>0 then Append(tail,[pos0,acc[pos0]]);fi;od;
  profile[2]:=profile[2]+Runtime()-tt;sparseRelation(tail);
 end;
 for i in [n,n-1..1] do
  for j in [n,n-1..i+1] do
   for k in [n,n-1..j+1] do
    if basecomm[j][i] and basecomm[k][i] and basecomm[k][j] then continue;fi;
    if j>=abelStart then currentRelation:=[2,i,j,k];exteriorRelation(i,j,k);if found then return result;fi;continue;fi;
    currentRelation:=[1,i,j,k];w1:=ShallowCopy(zero);w1[k]:=1;Assert(0,collectShortcut(w1,ps[j][i])<>fail);w2:=makevec(ps[k][j]);Assert(0,collectShortcut(w2,[i,1])<>fail);relation(w1,w2);if found then return result;fi;
   od;
  od;
  if i mod 5=0 then Print("witness_triples_remaining ",i," pivots ",pivots," runtime ",Runtime(),"\n");fi;
 od;
 for i in [n,n-1..1] do for j in [n,n-1..i+1] do
  currentRelation:=[3,i,j];w1:=ShallowCopy(zero);w1[j]:=orders[j]-1;Assert(0,collectShortcut(w1,ps[j][i])<>fail);w2:=makevec(ps[j][j]);Assert(0,collectShortcut(w2,[i,1])<>fail);relation(w1,w2);if found then return result;fi;
 od;od;
 for i in [n,n-1..1] do for k in [n,n-1..i+1] do
  currentRelation:=[4,i,k];w1:=ShallowCopy(zero);w1[k]:=1;Assert(0,collectShortcut(w1,ps[i][i])<>fail);w2:=makevec(ps[k][i]);Assert(0,collectShortcut(w2,[i,orders[i]-1])<>fail);relation(w1,w2);if found then return result;fi;
 od;od;
 for i in [n,n-1..1] do
  currentRelation:=[5,i];w1:=makevec(ps[i][i]);Assert(0,collectShortcut(w1,[i,1])<>fail);w2:=ShallowCopy(zero);w2[i]:=1;Assert(0,collectShortcut(w2,ps[i][i])<>fail);relation(w1,w2);if found then return result;fi;
 od;
 if check() then return result;fi;
 PrintTo(traceStream,"[\"failure\",",targetproof,",",target,"]\n");CloseStream(traceStream);Print("witness_complete_nonzero_remainder ",target,"\n");return rec(success:=false,relations:=relcount,remainder:=target);
end;;
