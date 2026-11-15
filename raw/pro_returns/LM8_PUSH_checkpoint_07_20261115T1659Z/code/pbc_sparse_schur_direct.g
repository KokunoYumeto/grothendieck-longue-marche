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

PBC_SparseSchurDirect:=function(G)
 local g,n,r,y,coll,k,i,j,e,zero,ps,a,w1,w2,piv,rank,nrank,
       rows,reduce,insert,relation,nn,p,t,c,unit,oldrows,oldrank,
       free,pos,m,coll2,translate,sys,ext,eg,images,epi,ker,
       makevec,relcount,outfile,pcp,pow,conj,pcword,basecomm;
 g:=Igs(G);n:=Length(g);r:=List(g,RelativeOrderPcp);
 Assert(0,ForAll(r,e->e>0));
 if n=0 then return IdentityMapping(G); fi;
 if n=1 then
  ext:=AbelianPcpGroup(1,[0]);
  return GroupHomomorphismByImagesNC(ext,G,GeneratorsOfGroup(ext),g);
 fi;
 y:=n*(n+1)/2;
 Print("sparse_schur_setup ",n," generators ",y," tails\n");
 coll:=FromTheLeftCollector(n+y);k:=n;
 for i in [1..n] do
  SetRelativeOrder(coll,i,r[i]);
  e:=ObjByExponents(coll,ExponentsByIgs(g,g[i]^r[i]));
  k:=k+1;Append(e,[k,1]);SetPower(coll,i,e);
  for j in [1..i-1] do
   e:=ObjByExponents(coll,ExponentsByIgs(g,g[i]^g[j]));
   k:=k+1;Append(e,[k,1]);SetConjugate(coll,i,j,e);
  od;
 od;
 # Exact specialized update for a finite pc quotient with central free tails.
 # CompleteConjugate has no work: its two tests require an infinite-order
 # conjugating/conjugated generator with a nontrivial assigned conjugate.
 # Every such infinite-order generator here is a central tail.  Calling the
 # generic routine nevertheless creates all dense pcp generator vectors.
 # Every base pair has an assigned central tail, so its commute bound is n;
 # each tail commutes from its own position onward.
 coll![PC_COMMUTE]:=Concatenation(ListWithIdenticalEntries(n,n),[n+1..n+y]);
 SetFilterObj(coll,IsUpToDatePolycyclicCollector);
 FromTheLeftCollector_CompletePowers(coll);
 zero:=ListWithIdenticalEntries(n+y,0);
 makevec:=function(word)
  local v,jj;
  v:=ShallowCopy(zero);
  for jj in [1,3..Length(word)-1] do v[word[jj]]:=word[jj+1];od;
  return v;
 end;
 # The stored defining conjugate is already collected.  For j<i,
 # g_i g_j = g_j (g_i^g_j), with all letters of the conjugate >=i.
 # Thus adjoining g_j produces a collected word without any further
 # power reduction.  The diagonal product is the assigned power word.
 ps:=List([1..n],i->[]);
 for i in [1..n] do
  ps[i][i]:=ShallowCopy(GetPower(coll,i));
  for j in [1..i-1] do
   ps[i][j]:=Concatenation([j,1],GetConjugate(coll,i,j));
  od;
 od;
 Print("sparse_pairs_stored runtime ",Runtime(),"\n");
 piv:=[];rank:=[];nrank:=0;rows:=[];relcount:=0;
 reduce:=function(v)
  local ii,chosen,best,coef,rest;
  while true do
   chosen:=fail;best:=nrank+1;
   for ii in [1,3..Length(v)-1] do
    if IsBound(rank[v[ii]]) and rank[v[ii]]<best then
     chosen:=ii;best:=rank[v[ii]];
    fi;
   od;
   if chosen=fail then return v; fi;
   coef:=v[chosen+1];
   rest:=Concatenation(v{[1..chosen-1]},v{[chosen+2..Length(v)]});
   v:=PBC_SparseAdd(rest,piv[v[chosen]],coef);
  od;
 end;
 insert:=function(v)
  local ii,chosen,coef,repl;
  v:=reduce(v);
  if Length(v)=0 then return; fi;
  chosen:=fail;
  for ii in [1,3..Length(v)-1] do
   if AbsInt(v[ii+1])=1 then chosen:=ii;break;fi;
  od;
  if chosen=fail then Add(rows,v);return;fi;
  coef:=v[chosen+1];
  repl:=Concatenation(v{[1..chosen-1]},v{[chosen+2..Length(v)]});
  for ii in [2,4..Length(repl)] do repl[ii]:=-coef*repl[ii];od;
  piv[v[chosen]]:=repl;nrank:=nrank+1;rank[v[chosen]]:=nrank;
 end;
 relation:=function(v,w)
  local tail,ii,diff;
  Assert(0,v{[1..n]}=w{[1..n]});
  if v=w then return;fi;
  tail:=[];
  for ii in [n+1..n+y] do
   diff:=v[ii]-w[ii];
   if diff<>0 then Add(tail,ii-n);Add(tail,diff);fi;
  od;
  relcount:=relcount+1;insert(tail);
 end;

 # If all three base generators commute, the three lifted pair
 # commutators are central formal tails.  There is no power reduction
 # (each distinct generator occurs once), and both associative products
 # agree literally.  These identically zero instances can be skipped.
 basecomm:=List([1..n],i->List([1..i-1],j->g[i]^g[j]=g[i]));
 # k(ji)=(kj)i, exactly Polycyclic consistency family 1.
 for i in [n,n-1..1] do
  for j in [n,n-1..i+1] do
   for k in [n,n-1..j+1] do
    if basecomm[j][i] and basecomm[k][i] and basecomm[k][j] then continue;fi;
    w1:=ShallowCopy(zero);w1[k]:=1;
    CollectWordOrFail(coll,w1,ps[j][i]);
    w2:=makevec(ps[k][j]);CollectWordOrFail(coll,w2,[i,1]);
    relation(w1,w2);
   od;
  od;
  if i mod 5=0 then
   Print("sparse_consistency_remaining ",i," unit_pivots ",nrank," deferred ",Length(rows)," runtime ",Runtime(),"\n");
  fi;
 od;
 # j^(p-1)(ji)=j^p i, family 2.
 for i in [n,n-1..1] do
  for j in [n,n-1..i+1] do
   w1:=ShallowCopy(zero);w1[j]:=r[j]-1;
   CollectWordOrFail(coll,w1,ps[j][i]);
   w2:=makevec(ps[j][j]);CollectWordOrFail(coll,w2,[i,1]);
   relation(w1,w2);
  od;
 od;
 # k i^p=(ki)i^(p-1), family 3.
 for i in [n,n-1..1] do
  for k in [n,n-1..i+1] do
   w1:=ShallowCopy(zero);w1[k]:=1;
   CollectWordOrFail(coll,w1,ps[i][i]);
   w2:=makevec(ps[k][i]);CollectWordOrFail(coll,w2,[i,r[i]-1]);
   relation(w1,w2);
  od;
 od;
 # i^p i=i i^p, family 4.
 for i in [n,n-1..1] do
  w1:=makevec(ps[i][i]);CollectWordOrFail(coll,w1,[i,1]);
  w2:=ShallowCopy(zero);w2[i]:=1;
  CollectWordOrFail(coll,w2,ps[i][i]);relation(w1,w2);
 od;
 # Input is finite: families 5--7 have no instances.
 repeat
  oldrank:=nrank;oldrows:=rows;rows:=[];
  for a in oldrows do insert(a);od;
 until nrank=oldrank;
 rows:=Set(rows);
 free:=Filtered([1..y],i->not IsBound(piv[i]));m:=Length(free);
 pos:=[];for i in [1..m] do pos[free[i]]:=i;od;
 Print("sparse_integral_reduction ",relcount," relations ",nrank," unit_pivots ",m," remaining_variables ",Length(rows)," remaining_rows\n");
 coll2:=FromTheLeftCollector(n+m);
 translate:=function(word)
  local base,tail,ii,jj,res;
  base:=[];tail:=[];
  for ii in [1,3..Length(word)-1] do
   if word[ii]<=n then Append(base,word{[ii,ii+1]});
   else tail:=PBC_SparseAdd(tail,[word[ii]-n,word[ii+1]],1);fi;
  od;
  tail:=reduce(tail);
  for ii in [1,3..Length(tail)-1] do Append(base,[n+pos[tail[ii]],tail[ii+1]]);od;
  return base;
 end;
 for i in [1..n] do
  SetRelativeOrder(coll2,i,r[i]);
  SetPower(coll2,i,translate(GetPower(coll,i)));
  for j in [1..i-1] do SetConjugate(coll2,i,j,translate(GetConjugate(coll,i,j)));od;
 od;
 UpdatePolycyclicCollector(coll2);
 sys:=CRSystem(1,m,0);
 for a in rows do
  e:=ListWithIdenticalEntries(m,0);
  for i in [1,3..Length(a)-1] do e[pos[a[i]]]:=a[i+1];od;
  Add(sys.base,e);
 od;
 ext:=QuotientBySystem(coll2,sys,n);
 eg:=Igs(ext);images:=ListWithIdenticalEntries(Length(eg),One(G));
 images{[1..n]}:=g;
 epi:=GroupHomomorphismByImagesNC(ext,G,eg,images);
 SetIsSurjective(epi,true);
 ker:=Subgroup(ext,eg{[n+1..Length(eg)]});
 SetKernelOfMultiplicativeGeneralMapping(epi,ker);
 Print("sparse_schur_completed ",Length(eg)," extension_generators\n");
 return epi;
end;;
