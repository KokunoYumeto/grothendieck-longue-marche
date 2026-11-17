# Post-checkpoint08 investigation: retain the actual full canonical source frame.
SizeScreen([4096,4096]);;
CERTIFICATE_REPLAY_CONTINUE:=true;;
Read("work/centralizer_code/check_central_certificate_replay.g");;
Read("work/centralizer_code/cap216_genuine_source_data.g");;
modBase:=Group(capQS,capQR);;
if Size(modBase)<>576 then Error("marked modular base order");fi;
modMap:=GroupHomomorphismByImages(certGroup,modBase,[certS,certR],[capQS,capQR]);;
if modMap=fail or not IsSurjective(modMap) then Error("actual canonical source to modular base");fi;
savedHarmonicVector:=[0,1,1,0,1,1,2,0,1,0,0,0,1,0,1,1,1,0,1,1,2,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,0,0,2];;
savedHarmonic:=CertElement(savedHarmonicVector);;
if not savedHarmonic in certPure or Comm(savedHarmonic,certS)<>One(certGroup) then Error("full canonical harmonic frame");fi;
modHarmonic:=Image(modMap,savedHarmonic);;
modX:=(capQS*capQR)^-2;;modY:=capQS*modX*capQS;;modZ:=(modX*modY)^-1;;
modPure:=Group(modX,modY);;
if not modHarmonic in modPure or Comm(modHarmonic,capQS)<>One(modBase) or Order(modHarmonic)<>4 then Error("pure harmonic residue");fi;
mycomm:=function(a,b)return a*b*a^-1*b^-1;end;;
modW4:=mycomm(mycomm(modX^4,modY^4),modZ^4);;
modFour:=modX^3*modY^3;;
frameChoices:=[];;
for k in [0,1] do
 for j in [1,3] do
  if modFour^k*modW4^j=modHarmonic then Add(frameChoices,[k,j]);fi;
 od;
od;
if Length(frameChoices)<>1 then Error("exact signed frame dictionary");fi;
Print("PASS actual source map full canonical D^c -> modular base576\n");
Print("PASS saved pure harmonic frame commutes with source s before projection\n");
Print("PASS projected frame has order4 and exact form (x^3 y^3)^k w4^j: ",frameChoices[1],"\n");
Print("MODULAR BASE abelian invariants: ",AbelianInvariants(modBase),"; pure image order=",Size(modPure),"\n");
Print("The full canonical commutator vanishes by the actual quotient B/[B,K_D] -> B/[B,K_Q], not by an elementary central test.\n");
QUIT_GAP(0);
