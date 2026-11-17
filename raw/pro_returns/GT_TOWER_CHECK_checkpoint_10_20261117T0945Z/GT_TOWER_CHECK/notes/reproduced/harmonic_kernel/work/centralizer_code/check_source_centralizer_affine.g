# Test every pure torsion centralizer in the executed full source certificate.
# This retains the actual A4 map, and makes no claim of a kernel-D lift.
CERTIFICATE_REPLAY_CONTINUE:=true;;
Read("work/centralizer_code/check_central_certificate_replay.g");;
affineS:=(1,2)(3,4);;affineR:=(1,2,3);;affineQ:=Group(affineS,affineR);;
affineMap:=GroupHomomorphismByImages(certGroup,affineQ,[certS,certR],[affineS,affineR]);;
if affineMap=fail or not IsSurjective(affineMap) then Error("actual affine quotient map");fi;
sourceCentralS:=Centralizer(certPure,certS);;
sourceCentralR:=Centralizer(certPure,certR);;
imageCentralS:=Image(affineMap,sourceCentralS);;
imageCentralR:=Image(affineMap,sourceCentralR);;
Print("FULL SOURCE PURE S CENTRALIZER: order=",Size(sourceCentralS),"; A4 image=",Elements(imageCentralS),"; image order=",Size(imageCentralS),"\n");
Print("FULL SOURCE PURE R CENTRALIZER: order=",Size(sourceCentralR),"; A4 image=",Elements(imageCentralR),"; image order=",Size(imageCentralR),"\n");
if affineS in imageCentralS then
 element:=PreImagesRepresentative(RestrictedMapping(affineMap,sourceCentralS),affineS);;
 Print("ODD HARMONIC CENTRALIZER WITNESS PC COORDINATES: ",ExponentsOfPcElement(certPc,element),"\n");
 savedVector:=[0,1,1,0,1,1,2,0,1,0,0,0,1,0,1,1,1,0,1,1,2,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,0,0,2];;
 savedElement:=CertElement(savedVector);;
 if not savedElement in certPure or Comm(savedElement,certS)<>One(certGroup) or Image(affineMap,savedElement)<>affineS then Error("saved odd frame vector");fi;
 Print("SAVED ODD FRAME VECTOR independently satisfies purity, centralizing, and image equations.\n");
else
 Print("NO ODD HARMONIC CENTRALIZER RESIDUE AT THIS FULL SOURCE\n");
fi;
Print("ALL PURE-CENTRALIZER IMAGE TESTS COMPLETED\n");
QUIT_GAP(0);
