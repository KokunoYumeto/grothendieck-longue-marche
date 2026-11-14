\\ The exact Kummer class of the rational radical three in L1.
default(parisize,256000000);
run()={
 my(B=read("research_e86/code/e_stable_lower_genus.bin")[1],b=Mod(x,B.pol),z=b^3/17,c1=b+1+3*z,tu=bnfisunit(B,z));
 my(u=3/c1^6,co=bnfisunit(B,u));
 print("RATIONAL_THREE_UNIT ",lift(u));print("RATIONAL_THREE_UNIT_COORDINATES ",co," ZETA_COORDINATES ",tu);
 print("RATIONAL_THREE_MOD_CUBES ",[co[1]%3,co[2]%3,lift(Mod(co[3],3)/Mod(tu[3],3))]);
 print("DONE_EXACT_RATIONAL_RADICAL_UNIT");
};
run();
quit;
