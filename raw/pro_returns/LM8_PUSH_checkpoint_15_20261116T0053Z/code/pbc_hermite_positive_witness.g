# Exact targeted source-centralization test.  The central tail module is
# reduced by integer Euclidean row operations, including nonunit pivots.
# Extra rows are s^2, r^3, and centralizer commutators.  Sparse labels retain
# their integer coefficients, so successful reduction supplies actual frame
# correction words.  No finite-field or rational linear algebra is used.
Read("LM8_PUSH/code/pbc_sparse_schur.g");;
PBC_HermitePositiveWitness:=function(data)
 local g,n,orders,m,coll,zero,ps,baseconjs,basecomm,abelStart,
       powers,conjs,k,i,j,e,a,word,inverse,centralTail,sw,rw,bsw,brw,
       extras,weights,basis,basisweights,pivots,relcount,target,targetw,
       reduce,insert,check,found,result,relation,sparseRelation,
       exteriorRelation,w1,w2,makevec,profile,t0,initialTarget,initialExtras,normalizeWeights,cs,cr,traceStream,traceId,newLeaf,newOp,newNeg,basisproof,targetproof,currentRelation,basecoll,finiteInverse,inverseWords,iv,vv,ii;

 orders:=data.orders;n:=Length(orders);m:=n*(n+1)/2;
 cs:=data.cs;cr:=data.cr;
 traceStream:=OutputTextFile(Concatenation(data.trace_stem,".jsonl"),false);
 SetPrintFormattingStatus(traceStream,false);
 PrintTo(traceStream,"[\"source\",\"",data.source_sha256,"\",",n,",",m,"]\n");
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

 # The only inverse words used in the formal presentation are explicit
 # positive finite words followed by a central correction.  No inverse
 # power or inverse conjugation is completed in the formal presentation.
 inverse:=function(w)
  local out,ii,jj,ex;out:=[];
  for ii in [Length(w)-1,Length(w)-3..1] do
   if w[ii]>n then Append(out,[w[ii],-w[ii+1]]);
   else
    ex:=w[ii+1];Assert(0,ex>=0);
    for jj in [1..ex] do Append(out,inverseWords[w[ii]]);od;
   fi;
  od;
  return out;
 end;
 basecoll:=FromTheLeftCollector(n);
 for i in [1..n] do
  SetRelativeOrder(basecoll,i,orders[i]);SetPower(basecoll,i,data.powers[i]);
  for j in [1..i-1] do SetConjugate(basecoll,i,j,data.conjugates[i][j]);od;
 od;
 if IsBound(data.finite_inverse) then
  finiteInverse:=data.finite_inverse;
  basecoll![PC_COMMUTE]:=ListWithIdenticalEntries(n,n);
  SetFilterObj(basecoll,IsUpToDatePolycyclicCollector);
  for i in [1..n] do
   vv:=ListWithIdenticalEntries(n,0);vv[i]:=1;
   Assert(0,CollectWordOrFail(basecoll,vv,finiteInverse[i])<>fail);
   Assert(0,ForAll(vv,a->a=0));
  od;
 else
  UpdatePolycyclicCollector(basecoll);
  finiteInverse:=List([1..n],i->FromTheLeftCollector_Inverse(basecoll,[i,1]));
 fi;
 Assert(0,ForAll(finiteInverse,w->ForAll([2,4..Length(w)],i->w[i]>=0)));
 Print("consistent_finite_inverses_ready runtime ",Runtime(),"\n");
 coll:=FromTheLeftCollector(n+m);baseconjs:=List([1..n],i->[]);k:=n;
 for i in [1..n] do
  SetRelativeOrder(coll,i,orders[i]);e:=ShallowCopy(data.powers[i]);k:=k+1;Append(e,[k,1]);SetPower(coll,i,e);
  for j in [1..i-1] do
   e:=ShallowCopy(data.conjugates[i][j]);baseconjs[i][j]:=ShallowCopy(e);k:=k+1;Append(e,[k,1]);SetConjugate(coll,i,j,e);
  od;
  if i mod 10=0 then Print("witness_source_build ",i," runtime ",Runtime(),"\n");fi;
 od;
 coll![PC_COMMUTE]:=Concatenation(ListWithIdenticalEntries(n,n),[n+1..n+m]);
 SetFilterObj(coll,IsUpToDatePolycyclicCollector);
 zero:=ListWithIdenticalEntries(n+m,0);
 ps:=List([1..n],i->[]);
 for i in [1..n] do
  ps[i][i]:=ShallowCopy(GetPower(coll,i));
  for j in [1..i-1] do ps[i][j]:=Concatenation([j,1],GetConjugate(coll,i,j));od;
 od;
 makevec:=function(w)
  local v,ii;v:=ShallowCopy(zero);for ii in [1,3..Length(w)-1] do v[w[ii]]:=w[ii+1];od;return v;
 end;
 centralTail:=function(w)
  local v,tail,ii,retry;v:=ShallowCopy(zero);retry:=0;while CollectWordOrFail(coll,v,w)=fail do v:=ShallowCopy(zero);retry:=retry+1;od;if retry>0 then Print("collector_stack_retries ",retry,"\n");fi;
  if not ForAll(v{[1..n]},a->a=0) then Print("unexpected_base_word ",w," collected_base ",v{[1..n]},"\n");Error("initial base collection");fi;tail:=[];
  for ii in [1..m] do if v[n+ii]<>0 then Append(tail,[ii,v[n+ii]]);fi;od;return tail;
 end;

 inverseWords:=[];
 for i in [1..n] do
  iv:=finiteInverse[i];vv:=ShallowCopy(zero);vv[i]:=1;
  while CollectWordOrFail(coll,vv,iv)=fail do vv:=ShallowCopy(zero);vv[i]:=1;od;
  Assert(0,ForAll(vv{[1..n]},a->a=0));
  inverseWords[i]:=ShallowCopy(iv);
  for ii in [1..m] do
   if vv[n+ii]<>0 then Append(inverseWords[i],[n+ii,-vv[n+ii]]);fi;
  od;
  if i mod 20=0 then Print("formal_positive_inverses ",i," runtime ",Runtime(),"\n");fi;
 od;
 sw:=data.s;rw:=data.r;bsw:=data.bs;brw:=data.br;
 Print("witness_source ",n," generators ",m," central tails runtime ",Runtime(),"\n");
 extras:=[centralTail(Concatenation(sw,sw)),centralTail(Concatenation(rw,rw,rw))];
 for a in cs do e:=a;Add(extras,centralTail(Concatenation(e,sw,inverse(e),inverse(sw))));od;
 for a in cr do e:=a;Add(extras,centralTail(Concatenation(e,rw,inverse(e),inverse(rw))));od;
 target:=centralTail(Concatenation(bsw,sw,inverse(bsw),brw,rw,inverse(brw),inverse(rw),inverse(sw)));
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
    acc[idx]:=acc[idx]-q*row[ii+1];if acc[idx]<>0 then AddSet(active,idx);fi;
   od;
   ww:=normalizeWeights(PBC_SparseAdd(ww,basisweights[row[1]],-q));pr:=newOp(pr,q,basisproof[row[1]]);
  od;
  Sort(touched);out:=[];
  for idx in touched do if acc[idx]<>0 then Append(out,[idx,acc[idx]]);fi;od;
  return [out,ww,pr];
 end;
 insert:=function(v,w,proof)
  local reduced,idx,old,oldw,oldproof,ii;
  while Length(v)>0 do
   reduced:=reduce(v,w,proof);v:=reduced[1];w:=reduced[2];proof:=reduced[3];
   if Length(v)=0 then return;fi;
   if v[2]<0 then
    for ii in [2,4..Length(v)] do v[ii]:=-v[ii];od;
    for ii in [2,4..Length(w)] do w[ii]:=-w[ii];od;proof:=newNeg(proof);
   fi;
   w:=normalizeWeights(w);idx:=v[1];
   if not IsBound(basis[idx]) then
    basis[idx]:=v;basisweights[idx]:=w;basisproof[idx]:=proof;pivots:=pivots+1;return;
   fi;
   Assert(0,v[2]<basis[idx][2]);old:=basis[idx];oldw:=basisweights[idx];oldproof:=basisproof[idx];basis[idx]:=v;basisweights[idx]:=w;basisproof[idx]:=proof;v:=old;w:=oldw;proof:=oldproof;
  od;
 end;
 check:=function()
  local red,coeffs,ii;
  red:=reduce(target,targetw,targetproof);target:=red[1];targetw:=red[2];targetproof:=red[3];
  if Length(target)>0 then return false;fi;
  coeffs:=ListWithIdenticalEntries(Length(extras),0);
  for ii in [1,3..Length(targetw)-1] do coeffs[targetw[ii]]:=targetw[ii+1];od;
  result:=rec(success:=true,coefficients:=coeffs,relations:=relcount,pivots:=pivots,
    s_count:=Length(cs),r_count:=Length(cr),initial_target:=initialTarget,initial_extras:=initialExtras,proof_node:=targetproof);
  PrintTo(traceStream,"[\"success\",",targetproof,",",coeffs,"]\n");CloseStream(traceStream);found:=true;Print("witness_found after_relations ",relcount," pivots ",pivots," coefficients ",coeffs," runtime ",Runtime(),"\n");return true;
 end;
 for i in [1..Length(extras)] do insert(extras[i],[i,1],newLeaf("extra",[i],extras[i]));od;
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
   local cw,t,idx;if cc=0 then return;fi;cw:=GetConjugate(coll,ll,mm);
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
    currentRelation:=[1,i,j,k];w1:=ShallowCopy(zero);w1[k]:=1;Assert(0,CollectWordOrFail(coll,w1,ps[j][i])<>fail);w2:=makevec(ps[k][j]);Assert(0,CollectWordOrFail(coll,w2,[i,1])<>fail);relation(w1,w2);if found then return result;fi;
   od;
  od;
  if i mod 5=0 then Print("witness_triples_remaining ",i," pivots ",pivots," runtime ",Runtime(),"\n");fi;
 od;
 for i in [n,n-1..1] do for j in [n,n-1..i+1] do
  currentRelation:=[3,i,j];w1:=ShallowCopy(zero);w1[j]:=orders[j]-1;Assert(0,CollectWordOrFail(coll,w1,ps[j][i])<>fail);w2:=makevec(ps[j][j]);Assert(0,CollectWordOrFail(coll,w2,[i,1])<>fail);relation(w1,w2);if found then return result;fi;
 od;od;
 for i in [n,n-1..1] do for k in [n,n-1..i+1] do
  currentRelation:=[4,i,k];w1:=ShallowCopy(zero);w1[k]:=1;Assert(0,CollectWordOrFail(coll,w1,ps[i][i])<>fail);w2:=makevec(ps[k][i]);Assert(0,CollectWordOrFail(coll,w2,[i,orders[i]-1])<>fail);relation(w1,w2);if found then return result;fi;
 od;od;
 for i in [n,n-1..1] do
  currentRelation:=[5,i];w1:=makevec(ps[i][i]);Assert(0,CollectWordOrFail(coll,w1,[i,1])<>fail);w2:=ShallowCopy(zero);w2[i]:=1;Assert(0,CollectWordOrFail(coll,w2,ps[i][i])<>fail);relation(w1,w2);if found then return result;fi;
 od;
 if check() then return result;fi;
 PrintTo(traceStream,"[\"failure\",",targetproof,",",target,"]\n");CloseStream(traceStream);Print("witness_complete_nonzero_remainder ",target,"\n");return rec(success:=false,relations:=relcount,remainder:=target);
end;;
