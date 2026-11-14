default(parisize,256000000);
run()={
 my(B=read("research_e86/code/e_stable_lower_genus.bin")[1],b=Mod(x,B.pol),z=b^3/17);
 print("LOWER_UNITS ",B.fu);
 print("PRODUCT ",B.fu[1]*B.fu[2]);
 for(t=0,2,print("TARGET ",t," ",lift(z^t*B.fu[1]*B.fu[2])));
 print("DONE_EXACT_LOWER_UNIT_TARGETS");
};
run();
quit;
