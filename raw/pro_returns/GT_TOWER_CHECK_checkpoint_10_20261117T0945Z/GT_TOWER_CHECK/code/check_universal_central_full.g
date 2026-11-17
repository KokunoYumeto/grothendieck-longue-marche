# Determine the complete canonical central cover of the fixed FINITE E.
UNIVERSAL_CENTRAL_CONTINUE:=true;;
Read("work/centralizer_code/check_universal_central_cover.g");;
refinementRows:=[];;
for dat in univCentralGroups do
 prime:=dat.prime;;base:=dat.group;;pg:=Pcgs(base);;npg:=Length(pg);;
 modu:=GModuleByMats(List(pg,g->IdentityMat(1,GF(prime))),GF(prime));;
 co:=TwoCohomology(base,modu);;basis:=BasisVectors(Basis(Range(co.cohom)));;
 cscc:=List(basis,v->PreImagesRepresentative(co.cohom,v));;
 conditions:=[];;
 for v in cscc do
  extn:=Extension(base,modu,v);;epg:=Pcgs(extn);;centralNew:=epg[npg+1];;
  liftCurrent:=g->MappedPcElement(g,pg,epg{[1..npg]});;
  if prime=2 then relValue:=liftCurrent(dat.s)^2;else relValue:=liftCurrent(dat.r)^3;fi;
  vv:=[First([0..prime-1],j->centralNew^j=relValue)];;
  for ag in dat.central do
   for bg in pg do
    commValue:=Comm(liftCurrent(ag),liftCurrent(bg));;
    Add(vv,First([0..prime-1],j->centralNew^j=commValue));
   od;
  od;
  Add(conditions,List(vv,z->z*One(GF(prime))));
 od;
 nullity:=Length(cscc)-RankMat(conditions);;
 Add(refinementRows,[prime,Length(cscc),RankMat(conditions),nullity]);
 Print("FINITE UNIVERSAL SOURCE higher central row=",Last(refinementRows),"\n");
od;
Print("FINITE UNIVERSAL SOURCE complete refinement rows: ",refinementRows,"\n");
if not ForAll(refinementRows,z->z[4]=0) then Print("Full finite kernel not yet determined.\n");QUIT_GAP(0);fi;
Print("FULL finite E canonical kernel=C2 x C3. This is the cover over finite E, not yet the whole central kernel over infinite U.\n");
g2:=First(univCentralGroups,z->z.prime=2);;g3:=First(univCentralGroups,z->z.prime=3);;
dd:=DirectProduct(g2.group,g3.group);;ee2:=Embedding(dd,1);;ee3:=Embedding(dd,2);;
fullS:=Image(ee2,g2.s)*Image(ee3,g3.s);;fullR:=Image(ee2,g2.r)*Image(ee3,g3.r);;
fullGroup:=Group(fullS,fullR);;
projectionFull:=GroupHomomorphismByImages(fullGroup,univPc,[fullS,fullR],[ups,upr]);;
if projectionFull=fail or Size(fullGroup)<>6*Size(univPc) or AbelianInvariants(Kernel(projectionFull))<>[2,3] then Error("full finite universal source cover");fi;
completeRows:=[];;
for idx in [1..Length(sourceFrameCandidates)] do
 datum:=sourceFrameCandidates[idx];;fbase:=Image(ipc,TupleUniversal(datum.values));;
 ff0:=PreImagesRepresentative(projectionFull,fbase);;
 aa:=(fullS*ff0)^2;;bb:=(ff0^-1*fullR)^3;;
 if aa^3*bb^2<>One(fullGroup) then Error("full finite cycle obstruction");fi;
 ff0:=ff0*aa*bb;;
 goodS:=IsConjugate(fullGroup,fullS,fullS*ff0);;
 goodR:=IsConjugate(fullGroup,fullR,ff0^-1*fullR);;
 Add(completeRows,[idx,goodS,goodR]);
od;
Print("FULL FINITE UNIVERSAL SOURCE positive rows: ",completeRows,"\n");
pureBase:=Group(Image(ipc,univX),Image(ipc,univY));;
cents:=Centralizer(pureBase,ups);;centr:=Centralizer(pureBase,upr);;
kappas:=List(GeneratorsOfGroup(cents),g->Comm(PreImagesRepresentative(projectionFull,g),fullS));;
kappar:=List(GeneratorsOfGroup(centr),g->Comm(PreImagesRepresentative(projectionFull,g),fullR));;
Print("FINITE CANONICAL cusp corrections: |C_P(s)|=",Size(cents),"; |C_P(r)|=",Size(centr),"; |im kappa_s|=",Size(Group(kappas)),"; |im kappa_r|=",Size(Group(kappar)),"; combined=",Size(Group(Concatenation(kappas,kappar))),"\n");
centtau:=Centralizer(pureBase,ups*upr);;
kappatau:=List(GeneratorsOfGroup(centtau),g->Comm(PreImagesRepresentative(projectionFull,g),fullS*fullR));;
Print("FINITE cusp centralizer: order=",Size(centtau),"; image kappa_tau order=",Size(Group(kappatau)),". The actual U centralizer is separately computed by its target-coordinate restrictions.\n");
if not IsBound(UNIVERSAL_FULL_CONTINUE) or not UNIVERSAL_FULL_CONTINUE then QUIT_GAP(0);fi;
