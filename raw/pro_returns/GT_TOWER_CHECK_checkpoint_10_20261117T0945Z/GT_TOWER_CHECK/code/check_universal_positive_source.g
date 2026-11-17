# Actual finite quotient U/L^6 and its complete target-frame census.
UNIVERSAL_FRAMES_CONTINUE:=true;;
Read("work/centralizer_code/check_universal_frame_membership.g");;
it:=IsomorphismPermGroup(gg);;targetPerm:=Image(it);;
sourceTargetX:=Image(it,markedS);;sourceTargetY:=Image(it,tt);;
targetDegree:=LargestMovedPoint(targetPerm);;
barS:=(1,2);;barR:=(1,2,3);;
transversal:=[(),barS,barR,barR^2,barS*barR,barS*barR^2];;
weights:=[(),(),sourceTargetY^-1,sourceTargetX,sourceTargetX^-1,sourceTargetY];;
InducedUniversal:=function(bar,ws)
 local imgs,i,j,k,block;
 imgs:=[];
 for i in [1..6] do
  j:=Position(transversal,transversal[i]*bar);
  block:=ListPerm(ws[i],targetDegree);
  for k in [1..targetDegree] do Add(imgs,targetDegree*(j-1)+block[k]);od;
 od;
 return PermList(imgs);
end;;
univS:=InducedUniversal(barS,weights);;
univR:=InducedUniversal(barR,List([1..6],i->()));;
univD:=Group(univS,univR);;
univX:=(univS*univR)^-2;;univY:=univS*univX*univS;;
univPure:=Group(univX,univY);;univDerived:=DerivedSubgroup(univPure);;
if List([1..targetDegree],i->i^univX)<>ListPerm(sourceTargetX,targetDegree) or List([1..targetDegree],i->i^univY)<>ListPerm(sourceTargetY,targetDegree) then Error("universal source marking");fi;
Print("Universal induced source: order=",Size(univD),"; pure=",Size(univPure),"; derived=",Size(univDerived),"; degree=",LargestMovedPoint(univD),"\n");
ipc:=IsomorphismPcGroup(univD);;univPc:=Image(ipc);;
ups:=Image(ipc,univS);;upr:=Image(ipc,univR);;
TupleUniversal:=function(values)
 local imgs,i,block;
 imgs:=[];
 for i in [1..6] do
  block:=ListPerm(Image(it,values[i]),targetDegree);
  Append(imgs,List(block,j->targetDegree*(i-1)+j));
 od;
 return PermList(imgs);
end;;
univResults:=[];;
for idx in [1..Length(sourceFrameCandidates)] do
 datum:=sourceFrameCandidates[idx];;ffinite:=TupleUniversal(datum.values);;
 if not ffinite in univDerived then Error("source commutator membership");fi;
 fp:=Image(ipc,ffinite);;
 cycle:=(ups*fp)^2=One(univPc) and (fp^-1*upr)^3=One(univPc);;
 posS:=IsConjugate(univPc,ups,ups*fp);;
 posR:=IsConjugate(univPc,upr,fp^-1*upr);;
 action:=GroupHomomorphismByImages(univPc,univPc,[ups,upr],[ups*fp,fp^-1*upr]);;
 auto:=action<>fail and IsBijective(action);;
 Add(univResults,[idx,datum.a,datum.l,cycle,posS,posR,auto]);
 Print("Universal source row: ",Last(univResults),"\n");
od;
if Size(univD)<>11943936 or Size(univPure)<>1990656 or Size(univDerived)<>13824 then Error("actual universal source orders");fi;
if Length(univResults)<>24 or not ForAll(univResults,z->ForAll(z{[4..7]},b->b)) then Error("complete universal positive-source census");fi;
Print("UNIVERSAL POSITIVE SOURCE CENSUS: ",univResults,"\n");
Print("These are actual finite automorphisms; a full canonical central-cover assertion is not part of this test.\n");
if not IsBound(UNIVERSAL_SOURCE_CONTINUE) or not UNIVERSAL_SOURCE_CONTINUE then QUIT_GAP(0);fi;
