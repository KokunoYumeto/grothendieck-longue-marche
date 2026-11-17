# Joint elementary central quotient of B/[B,ker(B->D)].
# Exact necessary tests only; no full profinite lifting assertion.
DESCENT_CONTINUE:=true;
Read("work/centralizer_code/check_descent_source_frames.g");
pd:=Pcgs(pcD);nd:=Length(pd);
trivial2:=GModuleByMats(List(pd,g->IdentityMat(1,GF(2))),GF(2));
coh2:=TwoCohomology(pcD,trivial2);
hbasis:=BasisVectors(Basis(Range(coh2.cohom)));
cocycles:=List(hbasis,v->PreImagesRepresentative(coh2.cohom,v));
SourceLift:=function(E,g)
 return MappedPcElement(g,pd,Pcgs(E){[1..nd]});
end;
sbits:=[];
for i in [1..Length(cocycles)] do
 ce0:=Extension(pcD,trivial2,cocycles[i]);se0:=SourceLift(ce0,ssD);
 if se0^2=One(ce0) then Add(sbits,0);else Add(sbits,1);fi;
od;
bad:=Position(sbits,1);allowed:=[];
for i in [1..Length(cocycles)] do
 if i=bad then continue;fi;
 v:=cocycles[i];if sbits[i]=1 then v:=v+cocycles[bad];fi;
 Add(allowed,v);
od;
e:=Length(allowed);
if e=0 then Error("no elementary central direction");fi;
triviale:=GModuleByMats(List(pd,g->IdentityMat(e,GF(2))),GF(2));
joint:=Concatenation(List([1..Length(allowed[1])],k->List([1..e],j->allowed[j][k])));
cen:=Extension(pcD,triviale,joint);
pe:=Pcgs(cen);se:=SourceLift(cen,ssD);re:=SourceLift(cen,rrD);
re:=re*re^3;
if se^2<>One(cen) or re^3<>One(cen) then Error("B generators missing");fi;
if Size(Group(se,re))<>Size(cen) then Error("joint extension not B-generated");fi;
proj:=GroupHomomorphismByImages(cen,pcD,AsList(pe),Concatenation(AsList(pd),List([1..e],i->One(pcD))));
if proj=fail or Size(Kernel(proj))<>2^e then Error("bad central projection");fi;
qimgs:=List(pd,g->Image(qh,PreImagesRepresentative(isoD,g)));
qe:=GroupHomomorphismByImages(cen,Q,AsList(pe),Concatenation(qimgs,List([1..e],i->One(Q))));
if qe=fail then Error("bad modular projection");fi;
xe:=(se*re)^-2;ye:=se*xe*se;
pureE:=Group(xe,ye);derivedE:=DerivedSubgroup(pureE);
qePure:=RestrictedMapping(qe,pureE);ke:=Kernel(qe);
hse:=ClosureGroup(ke,se);hre:=ClosureGroup(ke,re);
Print("JOINT CENTRAL COVER: dimension=",e,"; |E|=",Size(cen),"; |PureE|=",Size(pureE),"; |PureE'|=",Size(derivedE),"; kernel order=",Size(Kernel(proj)),"\n");
records:=[];
for i in [1..Length(sourceCandidates)] do
 cand:=sourceCandidates[i];fe:=SourceLift(cen,Image(isoD,cand.f));
 aa:=(se*fe)^2;bb:=(fe^-1*re)^3;
 obstruction:=aa^3*bb^2;
 passCycle:=obstruction=One(cen);
 passDerived:=false;passGlobal:=false;passS:=false;passR:=false;
 if passCycle then
  fe:=fe*aa*bb;
  if (se*fe)^2<>One(cen) or (fe^-1*re)^3<>One(cen) then Error("central correction failed");fi;
  passDerived:=fe in derivedE;
  passGlobal:=IsConjugate(cen,se,se*fe) and IsConjugate(cen,re,fe^-1*re);
  betaM:=Mmul(Mpow(U,2*cand.a0,12),cand.C,12);
  l:=cand.a0 mod 3;
  AM:=Mmul(Mmul(betaM,cand.H,12),Mpow(R0,-l,12),12);
  betaQ:=MatPerm(betaM,12,v12,true);AQ:=MatPerm(AM,12,v12,true);
  beta0:=PreImagesRepresentative(qePure,betaQ);A0:=PreImagesRepresentative(qePure,AQ);
  if beta0=fail or A0=fail then Error("missing pure frames");fi;
  targetS:=(se*fe)^beta0;targetR:=(fe^-1*re)^A0;
  if not targetS in hse or not targetR in hre then Error("frame target outside exact subgroup");fi;
  passS:=IsConjugate(hse,se,targetS);passR:=IsConjugate(hre,re,targetR);
 fi;
 Add(records,[i,cand.bit,passCycle,passDerived,passGlobal,passS,passR]);
od;
Print("JOINT RECORDS [candidate,Delta,cycle,derived,global positive,s residue frame,r residue frame]: ",records,"\n");
Print("JOINT SURVIVORS: ",Filtered(records,r->ForAll(r{[3..7]},b->b)),"\n");
Print("Exact necessary central quotient test only; no full lift inferred.\n");
if not IsBound(CENTRAL_CONTINUE) or not CENTRAL_CONTINUE then QUIT_GAP(0);fi;
