DESCENT_CONTINUE:=true;
Read("work/centralizer_code/check_descent_source_frames.g");
Print("EXACT ABELIAN INVARIANTS OF D: ",AbelianInvariants(pcD),"\n");
Print("EXACT ABELIAN INVARIANTS OF Q12: ",AbelianInvariants(Q),"\n");
Print("Orders of s,r,tau in D abelianization: ");
ab:=NaturalHomomorphismByNormalSubgroup(pcD,DerivedSubgroup(pcD));
Print(List([ssD,rrD,ssD*rrD],g->Order(Image(ab,g))),"\n");
QUIT_GAP(0);
