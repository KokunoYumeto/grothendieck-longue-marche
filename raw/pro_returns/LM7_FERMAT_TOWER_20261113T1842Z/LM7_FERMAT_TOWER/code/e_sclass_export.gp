default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
rows(M)=vector(matsize(M)[1],i,Vec(M[i,]));
ratvec(v)=vector(#v,i,[numerator(v[i]),denominator(v[i])]);
polcoords(z)=ratvec(vector(18,i,polcoef(lift(z),i-1)));
smrecord(kind,n,H,S)={
  print("{\"type\":\"",kind,"\",\"n\":",n,",\"hnf\":",rows(H),",\"left\":",rows(S[1]),",\"right\":",rows(S[2]),",\"left_inverse\":",rows(S[1]^-1),",\"right_inverse\":",rows(S[2]^-1),",\"diagonal\":",vector(matsize(S[3])[1],i,S[3][i,i]),"}");
};
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,xi=dat[2],a=dat[3],beta=a*xi,pi=beta+1,c1=beta+3*xi^3+1);
  my(saved=read("research_norm_index/code/cyclotomic_sclass_coordinates.bin"),ps=concat(idealprimedec(F,3),idealprimedec(F,17)),SU=saved[4],units=concat([xi],B.fu),gens=concat(units,SU[1]),V=saved[3]);
  if(SU[5][2]!=[3] || abs(matdet(V))!=3,error("base S-class group"));
  my(valuations=matrix(6,#gens,i,j,idealval(F,gens[j],ps[i])));
  for(j=1,#gens,
    my(I=idealhnf(F,1));
    for(k=1,6,I=idealmul(F,I,idealpow(F,ps[k],valuations[k,j])));
    if(I!=idealhnf(F,gens[j]),error("actual S-unit divisor identity"));
  );
  print("{\"type\":\"base\",\"certified\":",bnfcertify(B),",\"class_group\":",B.cyc,",\"s_class_group\":",SU[5][2],",\"polynomial_ascending\":",Vecrev(F.pol),",\"xi\":",polcoords(xi),",\"a\":",polcoords(a),",\"integral_basis\":",vector(18,j,polcoords(F.zk[j])),",\"generators\":",vector(#gens,j,polcoords(gens[j])),",\"valuation_matrix\":",rows(valuations),",\"s_valuation_basis\":",rows(V),",\"s_prime_classes\":",vector(6,j,Vec(bnfisprincipal(B,ps[j],0))),",\"s_generator_norms\":",vector(6,j,norm(Mod(SU[1][j],F.pol))),"}");
  for(nn=1,2,
    my(n=3^nn,rec=saved[1][nn],U=rec[2],C=rec[3],M=concat(U,C),H=mathnf(concat(n*matid(6),M)),HS=matsnf(H,1),Kfull=mathnf(matsolvemod(M,n,0,1)[2]),Sfull=matsnf(Kfull,1));
    my(Kunit=mathnf(matsolvemod(U,n,0,1)[2]),Sunit=matsnf(Kunit,1),K=rec[5],VK=rec[7]);
    if(lift(Mod(M*Kfull,n))!=matrix(6,15) || matdet(Kfull)!=n^5,error("complete S-unit field-norm kernel"));
    print("{\"type\":\"norm_characters\",\"n\":",n,",\"matrix\":",rows(M),",\"unit_matrix\":",rows(U),",\"nonunit_matrix\":",rows(C),",\"ordinary_unit_correction\":",rows(rec[9]),"}");
    smrecord("s_image",n,H,HS);
    smrecord("s_norm_kernel",n,Kfull,Sfull);
    smrecord("unit_norm_kernel",n,Kunit,Sunit);
    smrecord("correctable_exponents",n,K,rec[6]);
    smrecord("correctable_divisors",n,VK,rec[8]);
    my(loc=if(n==3,read("research_norm_index/code/cyclotomic_base1_local_norms.bin"),read("research_norm_index/code/cyclotomic_base1_ninth_norms.bin")),CM=matrix(6,10),all=concat(units,[c1]));
    for(j=1,3,
      my(ch=if(n==3,loc[2][j]~,loc[3][j][1][1,]));
      for(k=1,#all,
        my(v=idealval(F,all[k],ps[j]),u=nfeltdiv(F,all[k],pi^v));
        CM[j,k]=lift(Mod(ch*ideallog(F,u,loc[1][j]),n));
      );
    );
    for(j=4,6,
      my(bid=idealstar(F,ps[j],2,n));
      for(k=1,#all,
        my(v=idealval(F,all[k],ps[j]),u=nfeltdiv(F,all[k],beta^v));
        CM[j,k]=ideallog(F,u,bid)[1];
      );
    );
    my(CU=vecextract(CM,"..","1..9"),sc=vector(6,j,lift(Mod(CU[j,1]/U[j,1],n))),cor=if(n==3,[1,0,0,0,0,0,0,0,0]~,[1,0,0,0,1,1,0,6,6]~));
    if(lift(Mod(CU-matdiagonal(sc)*U,n))!=matrix(6,9) || lift(Mod(CU*cor+CM[,10],n))!=vector(6,j,0)~,error("actual c1 correction and coordinate comparison"));
    print("{\"type\":\"c1_correction\",\"n\":",n,",\"unit_matrix\":",rows(CU),",\"comparison_scalars\":",sc,",\"c1_character\":",Vec(CM[,10]),",\"correction_exponents\":",Vec(cor),",\"c1_valuations\":",vector(6,j,idealval(F,c1,ps[j])),"}");
  );
  my(pr=saved[2][1][4],mp=nfmodprinit(F,pr),p=pr.p,eval=vector(18,j,nfmodpr(F,F.zk[j],mp)),cl=bnfisprincipal(B,pr,0));
  if(p!=73 || pr.f!=1 || cl!=[2,1]~ || nfmodpr(F,beta,mp)!=22,error("actual coherent prime73"));
  print("{\"type\":\"prime73\",\"rational_prime\":",p,",\"degree\":",pr.f,",\"ideal\":",rows(idealhnf(F,pr)),",\"class\":",Vec(cl),",\"integral_basis_residues\":",eval,",\"primitive_residue\":",nfmodpr(F,Mod(x,F.pol),mp),",\"xi_residue\":",nfmodpr(F,xi,mp),",\"a_residue\":",nfmodpr(F,a,mp),",\"beta_residue\":",nfmodpr(F,beta,mp),",\"cubic_root\":63,\"ninth_root\":22}");
  my(coeff=List());
  for(j=4,6,
    my(mp=nfmodprinit(F,ps[j]),rr=nfmodpr(F,c1,mp),zz=nfmodpr(F,xi^3,mp));
    if(rr^96!=zz || zz==1,error("literal c1 nonnorm at17"));
    listput(coeff,[j,17,2,96,1]);
  );
  print("{\"type\":\"c1_tame_obstruction\",\"checks\":",Vec(coeff),"}");
  print("{\"type\":\"completion\",\"status\":\"PASS\"}");
};
run();
quit;
