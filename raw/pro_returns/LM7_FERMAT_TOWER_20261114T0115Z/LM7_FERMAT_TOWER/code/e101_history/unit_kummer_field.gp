\\ Field-only inspection of a distinct unit Kummer extension; no BNF is started.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
 my(B=read("research_e86/code/e_stable_lower_genus.bin")[1],F=B.nf,eps=B.fu[1]*B.fu[2],Y=varhigher("Y",x));
 my(eq=rnfequation(F,Y^3-eps,1));
 print("UNIT_KUMMER_ABSOLUTE ",eq[1]);
 my(red=polredbest(eq[1],1));print("UNIT_KUMMER_REDUCED ",red);
 my(NF=nfinit(red[1]));
 print("UNIT_KUMMER_DISCRIMINANT ",NF.disc," FACTORS ",factor(abs(NF.disc)));
 print("UNIT_KUMMER_PRIMES ",vector(2,j,apply(p->[p.e,p.f],idealprimedec(NF,if(j==1,3,17)))));
 writebin("research_h_after_e97/unit_kummer_field.bin",[B,eps,eq,red,NF]);
 print("DONE_UNIT_KUMMER_FIELD_ONLY; no BNF was started");
};
run();
quit;
