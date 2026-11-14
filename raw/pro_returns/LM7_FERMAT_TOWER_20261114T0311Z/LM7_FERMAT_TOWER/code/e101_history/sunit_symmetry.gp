\\ Exact finite ordinary/S-unit action calculation; uses the existing certified B1 BNF only.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
check(b,s)=if(!b,error(s));
jm(A)=vector(matsize(A)[1],i,vector(matsize(A)[2],j,lift(A[i,j])));
emit(n,v)=print("{\"name\":\"",n,"\",\"value\":",v,"}");
sdcoord(B,F,SU,V,ps,un,tors,u)={
    my(v=vector(6,j,idealval(F,u,ps[j]))~,se=V^-1*v);
    check(denominator(se)==1,"principal S-divisor coordinate");
    my(w=u/prod(j=1,6,SU[1][j]^se[j]),q=bnfisunit(B,w));
    check(#q==9,"ordinary unit coordinate");
    my(vv=concat(concat([lift(Mod(tors*q[9],9))],vector(8,j,q[j])),Vec(se))~);
    my(rec=prod(j=1,15,un[j]^vv[j]));
    check(u/rec==1 || u/rec==-1,"exact three-primary coordinate reconstruction");
    vv;
  };

run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,xi=dat[2],a=dat[3],z=xi^3,beta=a*xi);
  check(Mod(x,F.pol)==a-xi,"literal primitive element");
  my(old=read("research_norm_index/code/cyclotomic_sclass_coordinates.bin"),SU=old[4],V=old[3],ps=concat(idealprimedec(F,3),idealprimedec(F,17)));
  my(un=concat(concat([xi],B.fu),SU[1]),xu=bnfisunit(B,xi),tors=lift(Mod(xu[#xu],9)^-1));
  my(ga=nfalgtobasis(F,z*a-xi),ha=nfalgtobasis(F,z^2*a-z*xi));
  my(G=matrix(15,15),H=matrix(15,15));
  for(j=1,15,G[,j]=sdcoord(B,F,SU,V,ps,un,tors,nfbasistoalg(F,nfgaloisapply(F,ga,nfalgtobasis(F,un[j]))));H[,j]=sdcoord(B,F,SU,V,ps,un,tors,nfbasistoalg(F,nfgaloisapply(F,ha,nfalgtobasis(F,un[j])))));
  my(M=Mod(concat(old[1][1][2],old[1][1][3]),3),Q=matker(M),gm=Mod(G,3),hm=Mod(H,3));
  check(gm^3==matid(15) && hm^3==matid(15) && gm*hm==hm*gm,"actual normalizer mod-cube actions");
  check(M*gm*Q==matrix(6,matsize(Q)[2]) && M*hm*Q==matrix(6,matsize(Q)[2]),"field-norm kernel is stable");
  my(bv=Mod(sdcoord(B,F,SU,V,ps,un,tors,beta),3),cv=Mod(sdcoord(B,F,SU,V,ps,un,tors,xi*(beta+1+3*z)),3));
  check(M*bv==vector(6)~ && M*cv==vector(6)~,"literal norm and evaluated nonnorm lie in field-norm kernel");
  my(R=concat(concat((gm-1)*Q,(hm-1)*Q),bv),rk=matrank(R),rk1=matrank(concat(R,cv)));
  emit("sunit_generators",vector(15,j,Str(un[j])));
  emit("g_action",jm(G));emit("h_action",jm(H));
  emit("field_norm_matrix",jm(M));emit("field_norm_kernel",jm(Q));
  emit("known_beta_norm",Vec(lift(bv)));emit("known_xic1_defect",Vec(lift(cv)));
  emit("symmetry_relations",jm(R));emit("dimensions",[matsize(Q)[2],rk,rk1]);
  writebin("research_h_after_e97/sunit_symmetry.bin",[un,G,H,M,Q,bv,cv,R,rk,rk1]);
  print("DONE_EXACT_NORMALIZER_ACTION; quotient dimension ",matsize(Q)[2]-rk);
};
run();
quit;
