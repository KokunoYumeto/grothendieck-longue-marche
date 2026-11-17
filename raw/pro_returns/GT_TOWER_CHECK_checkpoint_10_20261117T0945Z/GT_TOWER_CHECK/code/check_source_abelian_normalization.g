DESCENT_CONTINUE:=true;
Read("work/centralizer_code/check_descent_source_frames.g");
sourceAb:=NaturalHomomorphismByNormalSubgroup(PureImage,Ep);
Print("SOURCE ABELIAN NORMALIZATION: pure abelian invariants=",AbelianInvariants(PureImage),"; order(xbar-ybar)=",Order(Image(sourceAb,xB*yB^-1)),"; order(x_D)=",Order(xB),"\n");
if Order(Image(sourceAb,xB*yB^-1)) mod Order(xB)<>0 then Error("inner normalization may change D");fi;
Print("Every full cusp-fixed positive lift with f_D in pure-derived normalizes without changing its literal D-action or D-frame residues.\n");
QUIT_GAP(0);
