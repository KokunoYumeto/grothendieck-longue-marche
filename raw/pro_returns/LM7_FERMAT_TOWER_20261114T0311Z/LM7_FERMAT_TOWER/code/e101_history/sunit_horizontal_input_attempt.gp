\\ Exact horizontal S-unit norms from certified B1 to certified L1.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
check(b,s)=if(!b,error(s));
jm(A)=vector(matsize(A)[1],i,vector(matsize(A)[2],j,lift(A[i,j])));
emit(n,v)=print("{\"name\":\"",n,"\",\"value\":",v,"}");
run()={
 my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,xi=dat[2],a=dat[3],z=xi^3,be=a*xi,dd=read("research_h_after_e97/sunit_symmetry.bin"),un=dd[1],Q=dd[5]);
 my(lo=read("research_e86/code/e_stable_lower_genus.bin"),BL=lo[1],L=BL.nf,b=Mod(x,L.pol),zz=b^3/17,c1=b+1+3*zz,lp=concat(idealprimedec(L,3),idealprimedec(L,17)));
 my(E=matrix(18,6,i,j,nfalgtobasis(F,subst(lift(L.zk[j]),x,be))[i]),inv=(E~*E)^-1*E~,ha=nfalgtobasis(F,z^2*a-z*xi),rr=matrix(5,15),tu=bnfisunit(BL,zz),tinv=lift(Mod(tu[3],3)^-1));
 for(j=1,15,
   my(u=nfalgtobasis(F,un[j]),hu=nfgaloisapply(F,ha,u),hhu=nfgaloisapply(F,ha,hu),nn=nfeltmul(F,nfeltmul(F,u,hu),hhu),nv=inv*nn);
   check(E*nv==nn,"exact horizontal contraction");
   my(nu=nfbasistoalg(L,nv),v3=idealval(L,nu,lp[1]),v17=idealval(L,nu,lp[2]));
   check(v17%2==0,"seventeen principal exponent");
   my(ou=nu/(c1^v3*b^(v17/2)),uc=bnfisunit(BL,ou));
   check(#uc==3,"lower ordinary unit coordinates");
   rr[,j]=[lift(Mod(tinv*uc[3],3)),uc[1],uc[2],v3,v17/2]~;
   my(rec=zz^rr[1,j]*BL.fu[1]^rr[2,j]*BL.fu[2]^rr[3,j]*c1^rr[4,j]*b^rr[5,j]);
   check(nu/rec==1 || nu/rec==-1,"lower reconstruction");
 );
 my(NQ=Mod(rr,3)*Q);
 emit("horizontal_unit_norm",jm(rr));emit("norm_on_field_norm_kernel",jm(NQ));
 emit("horizontal_dimensions",[matrank(NQ),matrank(NQ[1..3,]),matrank(NQ[4..5,])]);
 emit("image_basis",jm(matimage(NQ)));emit("known_xic1_image",Vec(lift(Mod(rr,3)*dd[7])));
 writebin("research_h_after_e97/sunit_horizontal.bin",[rr,NQ,matimage(NQ),E,inv]);
 print("DONE_EXACT_HORIZONTAL_UNIT_NORM");
};
run();
quit;
