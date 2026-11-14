\\ Extract a literal upper ordinary unit from the now-evaluated principal defect ideal.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,120);
setrand(10117139);
check(b,s)=if(!b,error(s));
run()={
 my(ne=read("research_h_after_e97/unit_product_defect.bin"),old=read("research_e97/code/e_unit_norm_coset.bin"),F=ne[2],OF=old[2],aut=ne[12],z=Mod(x^9/17,F.pol),p3=idealprimedec(F,3)[1]);
 my(C=matrix(18,18,i,j,nfalgtobasis(F,OF.zk[j])[i]));
 check(abs(matdet(C))==1 && denominator(C^-1)==1,"literal integral-basis comparison");
 my(OD=idealhnf(F,C*old[14]),rr=idealred(F,[OD,1]),Jz=rr[1],gz=if(type(rr[2])=="t_MAT",nffactorback(F,rr[2]),rr[2]));
 check(idealmul(F,Jz,gz)==OD,"zeta defect ideal reduction");
 my(Je=ne[15],ge=if(type(ne[16][2])=="t_MAT",nffactorback(F,ne[16][2]),ne[16][2]),I=idealdiv(F,idealmul(F,Je,Jz),p3));
 my(best=10^200,hit=0,g);
 print("ORDINARY_UNIT_PRINCIPAL_TARGET_NORM ",idealnorm(F,I)," ZETA_REDUCED_NORM ",idealnorm(F,Jz));
 for(k=1,160,
   my(R=idealred(F,[I,1],if(k==1,vector(9),vector(9,j,random(32)))),nn=idealnorm(F,R[1]));
   if(nn<best,best=nn;print("ORDINARY_UNIT_REDUCTION ",k," NORM ",nn));
   if(nn==1,g=if(type(R[2])=="t_MAT",nffactorback(F,R[2]),R[2]);check(idealhnf(F,g)==I,"exact principal generator");hit=k;break);
 );
 if(!hit,writebin("research_h_after_e97/ordinary_unit_preimage.bin",[C,OD,Jz,gz,Je,ge,I,best,hit]);print("DONE_ORDINARY_UNIT_PREIMAGE_SEARCH_NO_HIT; principality is already proved, search absence adds no claim");return);
 my(we=nfalgtobasis(F,ne[11]),wz=nfalgtobasis(F,old[11]));
 we=nfeltmul(F,we,nfeltdiv(F,ge,nfgaloisapply(F,aut,ge)));
 wz=nfeltmul(F,wz,nfeltdiv(F,gz,nfgaloisapply(F,aut,gz)));
 my(eta=nfeltmul(F,nfeltmul(F,we,wz),nfeltdiv(F,g,nfgaloisapply(F,aut,g))),BL=ne[1],eps=BL.fu[1]*BL.fu[2],target=nfalgtobasis(F,subst(lift(eps),x,Mod(x,F.pol)^3)*z));
 check(idealhnf(F,eta)==matid(18),"actual ordinary unit");
 check(nfeltmul(F,nfeltmul(F,eta,nfgaloisapply(F,aut,eta)),nfgaloisapply(F,aut,nfgaloisapply(F,aut,eta)))==target,"actual ordinary unit norm epsilon*zeta");
 my(P=idealprimedec(F,17)[1],mp=nfmodprinit(F,P,'t),res=nfmodpr(F,eta,mp));
 check(res^96!=1,"actual noncube unit residue at seventeen");
 print("ORDINARY_UNIT_FOUND ",hit," POLYNOMIAL ",lift(nfbasistoalg(F,eta)));
 print("ORDINARY_UNIT_RESIDUE ",res," CUBE_TEST ",res^96," NORM_RESIDUE ",res^3);
 writebin("research_h_after_e97/ordinary_unit_preimage.bin",[C,OD,Jz,gz,Je,ge,I,best,hit,g,eta,target,mp,res]);
 print("DONE_LITERAL_ORDINARY_UNIT_PREIMAGE");
};
run();
quit;
