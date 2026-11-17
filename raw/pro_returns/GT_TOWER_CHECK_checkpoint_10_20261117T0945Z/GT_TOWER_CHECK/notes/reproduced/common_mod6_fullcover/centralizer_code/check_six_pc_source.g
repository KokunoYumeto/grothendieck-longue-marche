UNIVERSAL_CONTINUE:=true;;
Read("work/centralizer_code/check_universal_six_source.g");;
Read("work/centralizer_code/build_six_pc_source.g");;
pcsource:=BuildSixPcSource(gg,markedS,markedR);;
Print("PC INDUCED SOURCE: order=",Size(pcsource.group),"; pure order=",Size(Group((pcsource.s*pcsource.r)^-2,pcsource.s*(pcsource.s*pcsource.r)^-2*pcsource.s)),"\n");
if Size(pcsource.group)<>11943936 then Error("pc source size");fi;
QUIT_GAP(0);
