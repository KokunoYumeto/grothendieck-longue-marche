# Diagnostic only: constructs a prime-two central refinement of the exact source.
# A Schur cover is not assumed to be the relative B-central cover.
DESCENT_CONTINUE:=true;
Read("work/centralizer_code/check_descent_source_frames.g");
Print("Starting prime-two Schur refinement at runtime ",Runtime(),".\n");
SetInfoLevel(InfoWarning,1);
schur:=EpimorphismSchurCover(pcD,[2]);
Print("Prime-two Schur map constructed at runtime ",Runtime(),".\n");
Print("Cover size: ",Size(Source(schur)),"; source size: ",Size(pcD),".\n");
Print("Kernel invariants: ",AbelianInvariants(Kernel(schur)),"\n");
QUIT_GAP(0);
