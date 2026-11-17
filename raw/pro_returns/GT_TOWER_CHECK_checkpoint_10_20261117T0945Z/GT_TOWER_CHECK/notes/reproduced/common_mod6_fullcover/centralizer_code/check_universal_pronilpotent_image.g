# Exact pronilpotent image of the universal pure source.
UNIVERSAL_CONTINUE:=true;;
Read("work/centralizer_code/check_universal_six_source.g");;
lower:=LowerCentralSeriesOfGroup(joint);;
nilres:=lower[Length(lower)];;
nilq:=FactorGroup(joint,nilres);;
Print("PURE UNIVERSAL SOURCE LOWER CENTRAL SERIES ORDERS: ",List(lower,Size),"\n");
Print("NILPOTENT QUOTIENT: order=",Size(nilq),"; abelian invariants=",AbelianInvariants(nilq),"; class=",NilpotencyClassOfGroup(nilq),"\n");
Print("TARGET T144 LOWER CENTRAL SERIES ORDERS: ",List(LowerCentralSeriesOfGroup(gg),Size),"\n");
Print("ALL EXACT FINITE CALCULATIONS COMPLETED\n");
QUIT_GAP(0);
