# First canonical central layers over the fixed universal finite source.
UNIVERSAL_SOURCE_CONTINUE:=true;;
Read("work/centralizer_code/check_universal_positive_source.g");;
upg:=Pcgs(univPc);;un:=Length(upg);;
Print("UNIVERSAL SOURCE CENTRAL TEST: PC length=",un,"\n");
univCentralRecords:=[];;univCentralGroups:=[];;
for prime in [2,3] do
 umod:=GModuleByMats(List(upg,g->IdentityMat(1,GF(prime))),GF(prime));;
 Print("Universal source H2(F",prime,") start.\n");
 uc:=TwoCohomology(univPc,umod);;
 ucb:=BasisVectors(Basis(Range(uc.cohom)));;
 ucc:=List(ucb,v->PreImagesRepresentative(uc.cohom,v));;
 urestr:=[];;
 for v in ucc do
  ee:=Extension(univPc,umod,v);;ep:=Pcgs(ee);;zz:=ep[un+1];;
  if prime=2 then torsion:=ups;else torsion:=upr;fi;
  torsionLift:=MappedPcElement(torsion,upg,ep{[1..un]});;
  Add(urestr,First([0..prime-1],j->zz^j=torsionLift^prime));
 od;
 allowed:=NullspaceMat(List(urestr,z->[z*One(GF(prime))]));;
 dimAllowed:=Length(allowed);;
 Print("Universal source H2(F",prime,") dimension=",Length(ucc),"; restrictions=",urestr,"; marked kernel dimension=",dimAllowed,"\n");
 if dimAllowed=0 then Add(univCentralRecords,[prime,Length(ucc),urestr,0,[]]);continue;fi;
 combined:=List(allowed,row->Sum([1..Length(ucc)],i->row[i]*ucc[i]));;
 jointCocycle:=Concatenation(List([1..Length(combined[1])],i->List([1..dimAllowed],j->combined[j][i])));;
 umodall:=GModuleByMats(List(upg,g->IdentityMat(dimAllowed,GF(prime))),GF(prime));;
 cover:=Extension(univPc,umodall,jointCocycle);;cpg:=Pcgs(cover);;
 cs:=MappedPcElement(ups,upg,cpg{[1..un]});;cr:=MappedPcElement(upr,upg,cpg{[1..un]});;
 if prime=2 then cr:=cr^4;else cs:=cs^3;fi;
 if cs^2<>One(cover) or cr^3<>One(cover) or Size(Group(cs,cr))<>Size(cover) then Error("universal central source marking");fi;
 Add(univCentralGroups,rec(prime:=prime,group:=cover,s:=cs,r:=cr,central:=AsList(cpg){[un+1..Length(cpg)]}));
 coverRows:=[];;
 for idx in [1..Length(sourceFrameCandidates)] do
  datum:=sourceFrameCandidates[idx];;fperm:=TupleUniversal(datum.values);;fbase:=Image(ipc,fperm);;
  flift:=MappedPcElement(fbase,upg,cpg{[1..un]});;
  aa:=(cs*flift)^2;;bb:=(flift^-1*cr)^3;;
  obstruction:=aa^3*bb^2;;
  if obstruction<>One(cover) then Add(coverRows,[idx,false,false,false]);continue;fi;
  flift:=flift*aa*bb;;
  ps:=IsConjugate(cover,cs,cs*flift);;pr:=IsConjugate(cover,cr,flift^-1*cr);;
  Add(coverRows,[idx,true,ps,pr]);
 od;
 Add(univCentralRecords,[prime,Length(ucc),urestr,dimAllowed,coverRows]);
 Print("UNIVERSAL SOURCE CENTRAL F",prime," ROWS: ",coverRows,"\n");
od;
Print("UNIVERSAL SOURCE CENTRAL RECORDS: ",univCentralRecords,"\n");
Print("These are first elementary central layers over the finite source; no assertion about the entire infinite U central cover is made.\n");
if not IsBound(UNIVERSAL_CENTRAL_CONTINUE) or not UNIVERSAL_CENTRAL_CONTINUE then QUIT_GAP(0);fi;
