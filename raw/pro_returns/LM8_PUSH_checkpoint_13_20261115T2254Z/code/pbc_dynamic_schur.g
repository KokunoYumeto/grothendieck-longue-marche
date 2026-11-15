# Exact memory-reduced implementation of the finite-input part of Polycyclic
# 2.18 SchurExtensionEpimorphism.  It evaluates the SAME four consistency
# families.  Stored pair products are sparse collected words.  Integral
# coefficient-one relations are eliminated by unimodular substitutions before
# the unchanged Polycyclic QuotientBySystem performs the remaining Smith step.
# No modular reduction or rationalization is used.

PBC_SparseAdd:=function(a,b,m)
 local i,j,out,c;
 i:=1;j:=1;out:=[];
 while i<=Length(a) or j<=Length(b) do
  if j>Length(b) or (i<=Length(a) and a[i]<b[j]) then
   Add(out,a[i]);Add(out,a[i+1]);i:=i+2;
  elif i>Length(a) or b[j]<a[i] then
   c:=m*b[j+1];
   if c<>0 then Add(out,b[j]);Add(out,c); fi;
   j:=j+2;
  else
   c:=a[i+1]+m*b[j+1];
   if c<>0 then Add(out,a[i]);Add(out,c); fi;
   i:=i+2;j:=j+2;
  fi;
 od;
 return out;
end;;

# Dynamic exact integral Tietze reduction.  Once enough coefficient-one
# central relations have been obtained, substitute them into every defining
# word and every retained relation.  Subsequent consistency identities are
# evaluated in that quotient.  This does not change the subgroup generated
# by all consistency relations: adding R after quotienting by earlier R0
# gives exactly the quotient by <R0,R>.  Only unit integral pivots are used.
PBC_DynamicSchur:=function(G)
 local g,n,r,m,coll,zero,ps,piv,rank,nrank,rows,relcount,
       totalpiv,basecomm,powers,conjs,k,i,j,e,install,makevec,
       reduce,insert,compact,relation,a,w1,w2,free,pos,newrows,
       translate,np,nc,oldrows,oldrank,sys,ext,eg,images,epi,ker;
 g:=Igs(G);n:=Length(g);r:=List(g,RelativeOrderPcp);
 Assert(0,ForAll(r,e->e>0));Assert(0,n>1);
 m:=n*(n+1)/2;k:=n;powers:=[];conjs:=List([1..n],i->[]);
 for i in [1..n] do
  e:=[];
  a:=ExponentsByIgs(g,g[i]^r[i]);
  for j in [1..n] do if a[j]<>0 then Append(e,[j,a[j]]);fi;od;
  k:=k+1;Append(e,[k,1]);powers[i]:=e;
  for j in [1..i-1] do
   e:=[];a:=ExponentsByIgs(g,g[i]^g[j]);
   for k in [1..n] do if a[k]<>0 then Append(e,[k,a[k]]);fi;od;
   # Stable original tail index: power i comes after all earlier rows.
   Append(e,[n+i*(i-1)/2+1+j,1]);conjs[i][j]:=e;
  od;
  k:=n+i*(i+1)/2;
 od;
 install:=function(pp,cc)
  local ii,jj;
  coll:=FromTheLeftCollector(n+m);
  for ii in [1..n] do
   SetRelativeOrder(coll,ii,r[ii]);SetPower(coll,ii,pp[ii]);
   for jj in [1..ii-1] do SetConjugate(coll,ii,jj,cc[ii][jj]);od;
  od;
  coll![PC_COMMUTE]:=Concatenation(ListWithIdenticalEntries(n,n),[n+1..n+m]);
  SetFilterObj(coll,IsUpToDatePolycyclicCollector);
  FromTheLeftCollector_CompletePowers(coll);
  zero:=ListWithIdenticalEntries(n+m,0);ps:=List([1..n],ii->[]);
  for ii in [1..n] do
   ps[ii][ii]:=ShallowCopy(GetPower(coll,ii));
   for jj in [1..ii-1] do ps[ii][jj]:=Concatenation([jj,1],GetConjugate(coll,ii,jj));od;
  od;
 end;
 install(powers,conjs);
 Print("dynamic_schur_setup ",n," generators ",m," tails runtime ",Runtime(),"\n");
 piv:=[];rank:=[];nrank:=0;rows:=[];relcount:=0;totalpiv:=0;
 makevec:=function(word)
  local v,jj;v:=ShallowCopy(zero);
  for jj in [1,3..Length(word)-1] do v[word[jj]]:=word[jj+1];od;return v;
 end;
 reduce:=function(v)
  local ii,chosen,best,coef,rest;
  while true do
   chosen:=fail;best:=nrank+1;
   for ii in [1,3..Length(v)-1] do
    if IsBound(rank[v[ii]]) and rank[v[ii]]<best then chosen:=ii;best:=rank[v[ii]];fi;
   od;
   if chosen=fail then return v;fi;
   coef:=v[chosen+1];rest:=Concatenation(v{[1..chosen-1]},v{[chosen+2..Length(v)]});
   v:=PBC_SparseAdd(rest,piv[v[chosen]],coef);
  od;
 end;
 insert:=function(v)
  local ii,chosen,coef,repl;
  v:=reduce(v);if Length(v)=0 then return;fi;chosen:=fail;
  for ii in [1,3..Length(v)-1] do if AbsInt(v[ii+1])=1 then chosen:=ii;break;fi;od;
  if chosen=fail then Add(rows,v);return;fi;
  coef:=v[chosen+1];repl:=Concatenation(v{[1..chosen-1]},v{[chosen+2..Length(v)]});
  for ii in [2,4..Length(repl)] do repl[ii]:=-coef*repl[ii];od;
  piv[v[chosen]]:=repl;nrank:=nrank+1;rank[v[chosen]]:=nrank;
 end;
 compact:=function(force)
  local ii,jj;
  if not force and nrank<Maximum(256,QuoInt(m,5)) then return;fi;
  repeat
   oldrank:=nrank;oldrows:=rows;rows:=[];
   for a in oldrows do insert(a);od;
  until nrank=oldrank;
  if nrank=0 then rows:=Set(rows);return;fi;
  free:=Filtered([1..m],ii->not IsBound(piv[ii]));pos:=[];
  for ii in [1..Length(free)] do pos[free[ii]]:=ii;od;
  translate:=function(word)
   local base,tail,kk;
   base:=[];tail:=[];
   for kk in [1,3..Length(word)-1] do
    if word[kk]<=n then Append(base,word{[kk,kk+1]});
    else tail:=PBC_SparseAdd(tail,[word[kk]-n,word[kk+1]],1);fi;
   od;
   tail:=reduce(tail);
   for kk in [1,3..Length(tail)-1] do Append(base,[n+pos[tail[kk]],tail[kk+1]]);od;
   return base;
  end;
  np:=List([1..n],ii->translate(GetPower(coll,ii)));
  nc:=List([1..n],ii->List([1..ii-1],jj->translate(GetConjugate(coll,ii,jj))));
  newrows:=[];
  for a in rows do
   e:=[];for ii in [1,3..Length(a)-1] do Append(e,[pos[a[ii]],a[ii+1]]);od;
   Add(newrows,e);
  od;
  totalpiv:=totalpiv+nrank;m:=Length(free);rows:=Set(newrows);piv:=[];rank:=[];nrank:=0;
  install(np,nc);
  Print("dynamic_compaction remaining_tails ",m," retained_rows ",Length(rows)," total_unit_pivots ",totalpiv," runtime ",Runtime(),"\n");
 end;
 relation:=function(v,w)
  local tail,ii,diff;
  Assert(0,v{[1..n]}=w{[1..n]});if v=w then return;fi;
  tail:=[];
  for ii in [n+1..n+m] do diff:=v[ii]-w[ii];if diff<>0 then Append(tail,[ii-n,diff]);fi;od;
  relcount:=relcount+1;insert(tail);compact(false);
  if relcount mod 1000=0 then Print("dynamic_relations ",relcount," tails ",m," pivots ",nrank," rows ",Length(rows)," runtime ",Runtime(),"\n");fi;
 end;
 basecomm:=List([1..n],i->List([1..i-1],j->g[i]^g[j]=g[i]));
 # Four finite-input consistency families, as in Polycyclic2.18.
 for i in [n,n-1..1] do
  for j in [n,n-1..i+1] do
   for k in [n,n-1..j+1] do
    if basecomm[j][i] and basecomm[k][i] and basecomm[k][j] then continue;fi;
    w1:=ShallowCopy(zero);w1[k]:=1;CollectWordOrFail(coll,w1,ps[j][i]);
    w2:=makevec(ps[k][j]);CollectWordOrFail(coll,w2,[i,1]);relation(w1,w2);
   od;
  od;
  if i mod 5=0 then Print("dynamic_triples_remaining ",i," tails ",m," pivots ",nrank," rows ",Length(rows)," runtime ",Runtime(),"\n");fi;
 od;
 for i in [n,n-1..1] do
  for j in [n,n-1..i+1] do
   w1:=ShallowCopy(zero);w1[j]:=r[j]-1;CollectWordOrFail(coll,w1,ps[j][i]);
   w2:=makevec(ps[j][j]);CollectWordOrFail(coll,w2,[i,1]);relation(w1,w2);
  od;
 od;
 for i in [n,n-1..1] do
  for k in [n,n-1..i+1] do
   w1:=ShallowCopy(zero);w1[k]:=1;CollectWordOrFail(coll,w1,ps[i][i]);
   w2:=makevec(ps[k][i]);CollectWordOrFail(coll,w2,[i,r[i]-1]);relation(w1,w2);
  od;
 od;
 for i in [n,n-1..1] do
  w1:=makevec(ps[i][i]);CollectWordOrFail(coll,w1,[i,1]);
  w2:=ShallowCopy(zero);w2[i]:=1;CollectWordOrFail(coll,w2,ps[i][i]);relation(w1,w2);
 od;
 compact(true);rows:=Set(rows);
 Print("dynamic_final_system ",m," variables ",Length(rows)," rows runtime ",Runtime(),"\n");
 sys:=CRSystem(1,m,0);
 for a in rows do
  e:=ListWithIdenticalEntries(m,0);
  for i in [1,3..Length(a)-1] do e[a[i]]:=a[i+1];od;Add(sys.base,e);
 od;
 ext:=QuotientBySystem(coll,sys,n);eg:=Igs(ext);
 images:=ListWithIdenticalEntries(Length(eg),One(G));images{[1..n]}:=g;
 epi:=GroupHomomorphismByImagesNC(ext,G,eg,images);SetIsSurjective(epi,true);
 ker:=Subgroup(ext,eg{[n+1..Length(eg)]});SetKernelOfMultiplicativeGeneralMapping(epi,ker);
 Print("dynamic_schur_completed ",Length(eg)," extension_generators runtime ",Runtime(),"\n");return epi;
end;;
