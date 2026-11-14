\\ Construct one literal reversed norm; no use of an uncertified class-group assertion.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
check(b,s)=if(!b,error(s));
run()={
 my(dat=read("research_h_after_e97/unit_kummer_bnf.bin"),BL=dat[1],FL=BL.nf,eps=dat[2],eq=dat[3],red=dat[4],B=dat[6],F=B.nf,v=variable(eq[1]),vn=variable(F.pol));
 my(oa=red[2],be=subst(lift(eq[2]),v,oa),de=oa-eq[3]*be,z=be^3/17,inv=modreverse(oa));
 check(subst(FL.pol,x,be)==0 && de^3==subst(lift(eps),x,be),"literal unit Kummer generators");
 my(aut=nfalgtobasis(F,subst(lift(inv),v,z*de+eq[3]*be)),A=matrix(18,18,i,j,nfgaloisapply(F,aut,nfalgtobasis(F,F.zk[j]))[i]));
 check(A^3==matid(18) && A*nfalgtobasis(F,be)==nfalgtobasis(F,be) && A*nfalgtobasis(F,de)==nfalgtobasis(F,z*de),"actual cyclic automorphism");
 my(E=matrix(18,6,i,j,nfalgtobasis(F,subst(lift(FL.zk[j]),x,be))[i]),C=(E~*E)^-1*E~);
 my(primes=List([3,7,17,73]));
 for(i=1,#B.gen,my(ff=factor(idealnorm(F,B.gen[i])));for(j=1,matsize(ff)[1],listput(primes,ff[j,1])));
 primes=Set(Vec(primes));print("REVERSED_NORM_RATIONAL_SUPPORT ",primes);
 my(ps=List(),ls=List());for(i=1,#primes,foreach(idealprimedec(F,primes[i]),p,listput(ps,p));foreach(idealprimedec(FL,primes[i]),p,listput(ls,p)));
 my(SU=bnfsunit(B,Vec(ps)),LU=bnfunits(BL,Vec(ls)),uu=concat(concat([B.tu[2]],B.fu),SU[1]),ta=bnfisunit(BL,Mod(x,FL.pol),LU),M=matrix(#ta,#uu));
 print("REVERSED_NORM_GENERATOR_COUNTS ",[#uu,#ta,#ps,#ls]);
 for(j=1,#uu,
   my(u=nfalgtobasis(F,uu[j]),n=nfeltmul(F,nfeltmul(F,u,A*u),A^2*u),nl=C*n);
   check(E*nl==n,"exact norm contraction");
   my(uc=bnfisunit(BL,nl,LU));check(#uc==#ta,"actual lower S-unit coordinates");M[,j]=uc;
 );
 my(moduli=vector(#ta,i,if(i==#ta,BL.tu[1],0))~,sol=matsolvemod(M,moduli,ta,1));
 print("REVERSED_NORM_SOLVABLE ",type(sol)!="t_INT");
 if(type(sol)=="t_INT",writebin("research_h_after_e97/unit_kummer_norm_beta.bin",[dat,be,de,aut,A,E,C,primes,uu,LU,M,ta,moduli,sol]);return);
 my(ex=sol[1],factors=matrix(#uu,2,i,k,if(k==1,uu[i],ex[i])),u=nffactorback(F,factors),nu=nfeltmul(F,nfeltmul(F,u,A*u),A^2*u));
 check(nu==nfalgtobasis(F,be),"literal reversed norm equals beta1");
 my(rel=sconcat(E,E*nfalgtobasis(FL,1))); \\ overwritten by the actual relative power basis below.
 rel=matrix(18,18,i,j,nfalgtobasis(F,be^((j-1)%6)*de^((j-1)\6))[i]);
 my(co=rel^-1*u);check(rel*co==u,"relative polynomial coefficient inverse");
 print("REVERSED_NORM_EXPONENTS ",ex);
 print("REVERSED_NORM_RELATIVE_COEFFICIENTS ",co);
 writebin("research_h_after_e97/unit_kummer_norm_beta.bin",[dat,be,de,aut,A,E,C,primes,uu,LU,M,ta,moduli,sol,u,rel,co]);
 print("DONE_LITERAL_REVERSED_NORM; this identity does not require the unfinished BNF certification");
};
run();
quit;
