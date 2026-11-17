# Strengthen the first-stage fixed-point test by keeping the exact same-word
# pair ( f(x_D,y_D), f(s_D,tau_D) ) in the next actual finite image.
# No new quotient is treated as a full profinite lift.
DESCENT_CONTINUE:=true;
Read("work/centralizer_code/check_descent_source_frames.g");
degreeD:=168;
PairPerm:=function(A,B)
 return PermList(Concatenation(ListPerm(A,degreeD),List(ListPerm(B,degreeD),i->degreeD+i)));
end;
WX:=PairPerm(xB,sB);WY:=PairPerm(yB,sB*rB);
Joint:=Group(WX,WY);JointPrime:=DerivedSubgroup(Joint);
proj1:=GroupHomomorphismByImages(Joint,D,[WX,WY],[xB,yB]);
proj2:=GroupHomomorphismByImages(Joint,D,[WX,WY],[sB,sB*rB]);
if proj1=fail or proj2=fail then Error("two actual projection maps");fi;
proj1p:=RestrictedMapping(proj1,JointPrime);
fiberKernel:=Image(proj2,Kernel(proj1p));
Print("SECOND STAGE: |joint|=",Size(Joint),"; |joint'|=",Size(JointPrime),"\n");
Print("Second-coordinate fiber kernel order = ",Size(fiberKernel),"\n");
fiberS:=ClosureGroup(fiberKernel,sB);
isoFiberS:=IsomorphismPcGroup(fiberS);pcFiberS:=Range(isoFiberS);
pcFiberGenerator:=Image(isoFiberS,sB);
secondCounts:=[0,0];secondSurvivors:=[];
orderX:=Order(xB);Print("Exact order of x in D = ",orderX,"\n");
for candidate in sourceCandidates do
 wordLift:=PreImagesRepresentative(proj1p,candidate.f);
 if wordLift=fail then Error("first coordinate must cover its derived subgroup");fi;
 Cbase:=Image(proj2,wordLift);
 allowedA:=Filtered([0..orderX-1],a->a mod 6=candidate.a0);
 passingA:=[];
 for aa in allowedA do
  # C=Cbase*k, beta=x^aa*C.  The fixed equation is beta*s*beta^-1=s*f.
  target:=(sB*candidate.f)^(xB^aa*Cbase);
  if target in fiberS and IsConjugate(pcFiberS,pcFiberGenerator,Image(isoFiberS,target)) then
   Add(passingA,aa);
  fi;
 od;
 if Length(passingA)>0 then
  secondCounts[candidate.bit+1]:=secondCounts[candidate.bit+1]+1;
  Add(secondSurvivors,[candidate.bit,candidate.a0,candidate.C,candidate.H,passingA]);
 fi;
od;
Print("Second-stage survivors by Delta 0,1: ",secondCounts,"\n");
Print("Survivors [Delta,a mod6,C,H,allowed a mod order(x)]: ",secondSurvivors,"\n");
Print("SECOND FINITE NECESSARY TEST COMPLETE; no profinite lift inferred.\n");
QUIT;
