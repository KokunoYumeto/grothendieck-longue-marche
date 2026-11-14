default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
jmat(M)=Str(vector(matsize(M)[1],i,vector(matsize(M)[2],j,M[i,j])));
jfrac(q)=[numerator(q),denominator(q)];
jpoly(p,n)=vector(n,i,jfrac(polcoef(lift(p),i-1)));
jmatq(M)=Str(vector(matsize(M)[1],i,vector(matsize(M)[2],j,jfrac(M[i,j]))));
smithrec(name,H,S)={
  if(S[1]*H*S[2]!=S[3] || denominator(S[1]^-1)!=1 || denominator(S[2]^-1)!=1,error("full Smith inverses"));
  print("{\"type\":\"smith\",\"name\":\"",name,"\",\"hnf\":",jmat(H),",\"left\":",jmat(S[1]),",\"right\":",jmat(S[2]),",\"left_inverse\":",jmat(S[1]^-1),",\"right_inverse\":",jmat(S[2]^-1),",\"diagonal\":",vector(matsize(H)[1],i,S[3][i,i]),"}");
};
run()={
  my(dat=read("research_e81/code/e_prime73_field.bin"),B=dat[1],F=dat[2],R=dat[3],E=dat[4],P=dat[5],PS=dat[7],S=dat[8],xi=dat[10],beta=dat[11]);
  my(ac=read("research_e84/code/e_ramified_class_action.bin"),ar=read("research_e81/code/e_prime73_artin.bin"),gn=read("research_norm_index/code/cyclotomic_base1_genus.bin"));
  print("{\"type\":\"automorphisms\",\"h_base\":",jpoly(ac[1],18),",\"g_base\":",jpoly(ac[2],18),",\"h_class\":",jmat(ac[3]),",\"g_class\":",jmat(ac[4]),",\"h_prime73_class\":",Vec(ac[5]),",\"g_prime73_class\":",Vec(ac[6]),",\"h_prime_permutation\":",ac[10],",\"g_prime_permutation\":",ac[11],",\"xi\":",jpoly(xi,18),",\"beta1\":",jpoly(beta,18),",\"class_generator_ideals\":",vector(2,i,vector(18,j,vector(18,k,idealhnf(F,B.gen[i])[j,k]))),"}");
  for(k=1,2,
    my(aut=ac[k],label=if(k==1,"h","g"));
    for(j=1,3,
      my(J=if(j<=2,B.gen[j],P),im=idealhnf(F,nfgaloisapply(F,aut,J)),ans=bnfisprincipal(B,im,1),ref=matid(18));
      for(i=1,2,ref=idealmul(F,ref,idealpow(F,B.gen[i],ans[1][i])));
      if(idealmul(F,ref,ans[2])!=im,error("literal base class image"));
      print("{\"type\":\"literal_class_image\",\"automorphism\":\"",label,"\",\"input\":",j,",\"image_ideal\":",jmatq(im),",\"reference_ideal\":",jmatq(ref),",\"class\":",Vec(ans[1]),",\"principal_generator\":",jpoly(nfbasistoalg(F,ans[2]),18),"}");
    );
    my(AM=bnrgaloismatrix(gn[1],lift(aut)),H=gn[4],U=gn[5],D=gn[7],GA=U*AM*U^-1,perm=ac[9+k]);
    if(denominator(H^-1*AM*H)!=1,error("actual genus relation stability"));
    for(i=1,6,for(j=1,#ar[5],if((GA*ar[6][,i]-ar[6][,perm[i]])[j]%ar[5][j],error("Artin equivariance"))));
    print("{\"type\":\"genus_action\",\"automorphism\":\"",label,"\",\"ray_action\":",jmat(AM),",\"relation_lattice\":",jmat(H),",\"relation_action\":",jmat(H^-1*AM*H),",\"smith_left\":",jmat(U),",\"smith_left_inverse\":",jmat(U^-1),",\"genus_action\":",jmat(GA),",\"cyclic\":",ar[5],"}");
  );
  my(qsum=[1,1,1,0,0,0]~,tsum=[0,0,0,1,1,1]~,M=concat(concat(3*matid(6),qsum),tsum),H=mathnf(M),SM=matsnf(H,1),delta=[-1,1,0,0,0,0]~);
  if(abs(matdet(H))!=81 || denominator(H^-1*delta)==1,error("new principal divisor quotient"));
  print("{\"type\":\"new_s_relations\",\"generators\":",jmat(M),",\"delta\":",Vec(delta),",\"genus_map\":",jmat(ar[6]),",\"genus_cyclic\":",ar[5],",\"candidate_origin\":",Vec(ar[8]),"}");
  smithrec("new_s_relations",H,SM);
  my(L=nfinit(x^18+17*x^9+289));
  if(L.disc!=-3^45*17^16 || L.disc^3!=E.disc,error("unramified h-fixed field discriminant"));
  print("{\"type\":\"fixed_field\",\"polynomial\":[289,0,0,0,0,0,0,0,0,17,0,0,0,0,0,0,0,0,1],\"discriminant\":",L.disc,",\"upper_discriminant\":",E.disc,",\"relative_discriminant_norm\":1}");
  my(zeta=xi^3,c1=beta+1+3*zeta,target=xi*c1,ctests=vector(3),corrtests=vector(3));
  if((1+3*zeta)^3!=1-18*zeta || beta^3!=17*zeta,error("literal downward cubic norm"));
  for(i=1,3,my(mp=nfmodprinit(F,PS[i+3]));ctests[i]=(nfmodpr(F,c1,mp)^96==nfmodpr(F,zeta,mp));corrtests[i]=(nfmodpr(F,target,mp)^96==1));
  if(vecmin(ctests)!=1 || vecmin(corrtests)!=1,error("actual local17 norm obstruction"));
  print("{\"type\":\"norm_target\",\"c1_valuations\":",vector(6,i,idealval(F,c1,PS[i])),",\"absolute_norm\":",nfeltnorm(F,c1),",\"c1_cubic_residue_equals_zeta\":",ctests,",\"corrected_cubic_residue_equals_one\":",corrtests,"}");
  print("{\"type\":\"completion\",\"status\":\"PASS\"}");
};
run();
quit;
