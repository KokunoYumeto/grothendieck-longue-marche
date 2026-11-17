# Next target has Delta=0, chi1=1. This tests its actual next finite source.
NEXT_SOURCE_CONTINUE:=true;
Read("work/centralizer_code/check_second_pullback_source.g");
zTarget:=PermList(Concatenation([1..120],List(ListPerm(MatPerm([5,0,0,5],12,v12,true),48),j->120+j)));
if not zTarget in D or not IsCentral(D,Group(zTarget)) or Order(zTarget)<>2 then Error("specific kernel frame missing");fi;
targetAZero:=targetA*zTarget;
targetHZero:=targetBeta^-1*targetAZero;
zeroMats:=[targetBeta,targetBeta^-1,targetHZero^-1*targetBeta^-1,targetHZero,
 targetS^-1*targetHZero^-1*targetS,targetT*targetBeta*targetHZero*targetT^-1];
zeroF:=NextTuple(zeroMats,I2);
Print("ZERO TARGET tuple: source membership=",zeroF in nextGroup,"; cycles=",zeroF^sNext*zeroF=One(nextGroup),",",zeroF^(rNext^-2)*zeroF^(rNext^-1)*zeroF=One(nextGroup),"\n");
if not zeroF in nextGroup then Print("Exact source membership obstruction for this pinned tuple.\n");QUIT_GAP(0);fi;
normalExponents:=Filtered([0..Order(xNext)-1],a->yNext^a*zeroF*xNext^-a in nextDerived);
Print("Finite commutator-normalization exponents modulo order(x)=",Order(xNext),": ",normalExponents,"\n");
if Length(normalExponents)=0 then Print("No source commutator normalization for this tuple.\n");QUIT_GAP(0);fi;
zeroFNorm:=yNext^normalExponents[1]*zeroF*xNext^-normalExponents[1];
Print("Computing actual next PC presentation at runtime=",Runtime(),".\n");
targetAutoPc:=GroupHomomorphismByImages(pcD,pcD,[ssD,rrD],[ssD*Image(isoD,sourceCandidates[14].f),Image(isoD,sourceCandidates[14].f)^-1*rrD]);
if targetAutoPc=fail or not IsBijective(targetAutoPc) then Error("target automorphism failed");fi;
TargetPsi:=g->targetBeta^-1*PreImagesRepresentative(isoD,Image(targetAutoPc,Image(isoD,g)))*targetBeta;
NextBlock:=function(g,i)
 return PermList(List([1..degreeTarget],j->((degreeTarget*(i-1)+j)^g)-degreeTarget*(i-1)));
end;
repNext:=[One(nextGroup),sNext,rNext,rNext^2,sNext*rNext,sNext*rNext^2];
sImage:=sNext*zeroFNorm;rImage:=zeroFNorm^-1*rNext;
repNextImages:=[One(nextGroup),sImage,rImage,rImage^2,sImage*rImage,sImage*rImage^2];
coordinateChecks:=[];
for i in [1..6] do
 correction:=NextBlock(repNext[i]*repNextImages[i]^-1,1);
 for generator in [xNext,yNext] do
  if generator=xNext then generatorImage:=xNext;else generatorImage:=zeroFNorm^-1*yNext*zeroFNorm;fi;
  ok:=NextBlock(generatorImage,i)=correction*TargetPsi(NextBlock(generator,i))*correction^-1;
  Add(coordinateChecks,ok);
 od;
od;
if not ForAll(coordinateChecks,b->b) then Error("actual coordinate automorphism equality failed");fi;
Print("NEXT AUTOMORPHISM CERTIFICATE: all12 marked coordinate equalities passed; original modular coordinate is fixed. Kernel preservation and injectivity follow on the exact joint source.\n");
nextIso:=IsomorphismPcGroup(nextGroup);nextPc:=Range(nextIso);
ns:=Image(nextIso,sNext);nr:=Image(nextIso,rNext);nf:=Image(nextIso,zeroFNorm);
Print("Next PC length=",Length(Pcgs(nextPc)),"; runtime=",Runtime(),".\n");
passNextS:=IsConjugate(nextPc,ns,ns*nf);
Print("Next positive s class=",passNextS,"; runtime=",Runtime(),".\n");
passNextR:=IsConjugate(nextPc,nr,nf^-1*nr);
Print("ZERO TARGET NORMALIZED FINITE AUTOMORPHISM: positive_s=",passNextS,"; positive_r=",passNextR,"; automorphism=true by marked coordinate certificate; runtime=",Runtime(),".\n");
Print("A full canonical central-cover certificate remains required; no chi2 value is asserted.\n");
if not IsBound(NEXT_ZERO_CONTINUE) or not NEXT_ZERO_CONTINUE then QUIT_GAP(0);fi;
