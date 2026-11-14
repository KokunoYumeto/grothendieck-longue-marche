\\ One bounded computation in the distinct unit-radical field, not in L2.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(1011713);
run()={
 my(dat=read("research_h_after_e97/unit_kummer_field.bin"),F=dat[5]);
 print("START_DISTINCT_UNIT_KUMMER_BNF ",F.pol," DISC ",F.disc);
 my(B=bnfinit(F,1));
 print("UNIT_KUMMER_BNF_CLASS ",B.cyc," REGULATOR ",B.reg);
 writebin("research_h_after_e97/unit_kummer_bnf.bin",concat(dat,[B]));
 print("UNIT_KUMMER_BNF_CERTIFICATION ",bnfcertify(B));
 print("DONE_DISTINCT_UNIT_KUMMER_BNF");
};
run();
quit;
