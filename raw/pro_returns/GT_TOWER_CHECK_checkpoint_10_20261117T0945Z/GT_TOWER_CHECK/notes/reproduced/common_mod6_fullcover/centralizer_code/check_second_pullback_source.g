# Actual source for a possible second pullback; no lifting claim from survival.
FULL_CENTRAL_CONTINUE:=true;
Read("work/centralizer_code/check_descent_central_full.g");
targetBeta:=PreImagesRepresentative(isoD,Image(fullPi,betaWitness));
targetA:=PreImagesRepresentative(isoD,Image(fullPi,AWitness));
if PreImagesRepresentative(isoD,Image(fullPi,fWitness))<>sourceCandidates[14].f then Error("candidate14 projection mismatch");fi;
targetC:=targetBeta;targetH:=targetBeta^-1*targetA;
targetS:=sB;targetT:=sB*rB;degreeTarget:=LargestMovedPoint(D);
IdTarget:=One(D);
InducedNext:=function(bar,weights,Qmat)
 local images,i,j,k,block;
 images:=[];
 for i in [1..6] do
  j:=Position(reps,reps[i]*bar);block:=ListPerm(weights[i],degreeTarget);
  for k in [1..degreeTarget] do Add(images,degreeTarget*(j-1)+block[k]);od;
 od;
 block:=ListPerm(MatPerm(Qmat,12,v12,true),48);
 Append(images,List(block,k->6*degreeTarget+k));return PermList(images);
end;
sNext:=InducedNext(sb,[IdTarget,IdTarget,targetT^-1,targetS,targetS^-1,targetT],S);
rNext:=InducedNext(rb,List([1..6],i->IdTarget),R0);
if Order(sNext)<>2 or Order(rNext)<>3 then Error("next source relations fail");fi;
nextGroup:=Group(sNext,rNext);xNext:=(sNext*rNext)^-2;yNext:=sNext*xNext*sNext;
nextPure:=Group(xNext,yNext);nextDerived:=DerivedSubgroup(nextPure);
Print("NEXT SOURCE degree=",LargestMovedPoint(nextGroup),"; order=",Size(nextGroup),"; pure derived order=",Size(nextDerived),"; runtime=",Runtime(),".\n");
NextTuple:=function(mats,Qmat)
 local images,i,block;
 images:=[];
 for i in [1..6] do block:=ListPerm(mats[i],degreeTarget);Append(images,List(block,j->degreeTarget*(i-1)+j));od;
 block:=ListPerm(MatPerm(Qmat,12,v12,true),48);Append(images,List(block,j->6*degreeTarget+j));
 return PermList(images);
end;
nextMats:=[targetC,targetC^-1,targetH^-1*targetC^-1,targetH,
 targetS^-1*targetH^-1*targetS,targetT*targetC*targetH*targetT^-1];
nextF:=NextTuple(nextMats,I2);
Print("NEXT SOURCE specified target-frame tuple: membership=",nextF in nextGroup,"; pure-derived=",nextF in nextDerived,"; s cycle=",nextF^sNext*nextF=One(nextGroup),"; r cycle=",nextF^(rNext^-2)*nextF^(rNext^-1)*nextF=One(nextGroup),"\n");
Print("This is an exact preliminary source test, not a full lift or a chi2 claim.\n");
if not IsBound(NEXT_SOURCE_CONTINUE) or not NEXT_SOURCE_CONTINUE then QUIT_GAP(0);fi;
