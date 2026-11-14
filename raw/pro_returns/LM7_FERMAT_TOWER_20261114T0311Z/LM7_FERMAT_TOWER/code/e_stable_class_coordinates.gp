default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(860173);
jmat(M)=Str(vector(matsize(M)[1],i,vector(matsize(M)[2],j,M[i,j])));
jfrac(q)=[numerator(q),denominator(q)];
jmatq(M)=Str(vector(matsize(M)[1],i,vector(matsize(M)[2],j,jfrac(M[i,j]))));
jpoly(p,n)=vector(n,i,jfrac(polcoef(lift(p),i-1)));
redvec(v,ds)=vector(#ds,i,lift(Mod(v[i],ds[i])))~;
smithrec(name,H,S)={
  if(S[1]*H*S[2]!=S[3] || denominator(S[1]^-1)!=1 || denominator(S[2]^-1)!=1,error("Smith inverse"));
  print("{\"type\":\"smith\",\"name\":\"",name,"\",\"matrix\":",jmat(H),",\"left\":",jmat(S[1]),",\"right\":",jmat(S[2]),",\"left_inverse\":",jmat(S[1]^-1),",\"right_inverse\":",jmat(S[2]^-1),",\"diagonal\":",vector(matsize(H)[1],i,S[3][i,i]),"}");
};
onefield(label,B,Ray,U,ds,beta,zeta,C)={
  my(F=B.nf,k=sum(i=1,#ds,ds[i]>1),D=matdiagonal(vector(k,i,ds[i])),rr=List(),basis=List(),BV=matrix(k,0),bc=List());
  forprime(p=2,149,if(p!=3 && p!=17,
    my(Ps=idealprimedec(F,p));
    for(j=1,#Ps,
      my(P=Ps[j],mp=nfmodprinit(F,P),q=p^P[4],br=nfmodpr(F,beta,mp),zr=nfmodpr(F,zeta,mp),v=redvec(U*bnrisprincipal(Ray,P,0),ds),ee=-1);
      for(e=0,2,if(br^((q-1)/3)==zr^e,ee=e));
      if(ee<0,error("actual Kummer Frobenius"));
      my(vv=vector(k,i,v[i])~);
      if(matrank(Mod(concat(BV,vv),3))>matsize(BV)[2],BV=concat(BV,vv);listput(basis,[p,j]);listput(bc,ee));
      my(root=-1,rb=-1,rz=-1,uproot=-1);
      if(P[4]==1,
        for(t=0,p-1,
          if(nfmodpr(F,Mod(variable(F.pol),F.pol),mp)==t,root=t);
          if(br==t,rb=t);if(zr==t,rz=t)
        );
        if(ee==0,for(t=0,p-1,if(Mod(t,p)^3==Mod(rb,p),uproot=t;break)));
        if(root<0 || rb<0 || rz<0 || (ee==0 && uproot<0),error("degree-one residue map"));
      );
      listput(rr,[p,j,P[4],Vec(vv),ee,root,rb,rz,uproot,idealhnf(F,P)]);
    );
  ));
  if(matsize(BV)!=[k,k],error("finite Frobenius basis incomplete"));
  my(ch=lift(Mod(Mat(Vec(bc)),3)*Mod(BV,3)^-1),ker=matsolvemod(ch,[3]~,0,1)[2],H=mathnf(ker),Q=H^-1*D,SM=matsnf(Q,1));
  if(denominator(Q)!=1 || abs(matdet(H))!=3,error("actual character kernel"));
  for(i=1,#rr,if(lift(Mod((ch*Col(rr[i][4]))[1],3))!=rr[i][5],error("all Frobenius samples")));
  print("{\"type\":\"restriction\",\"name\":\"",label,"\",\"cyclic\":",vector(k,i,ds[i]),",\"row\":",jmat(ch),",\"prime_basis\":",Vec(basis),",\"basis_vectors\":",jmat(BV),",\"basis_values\":",Vec(bc),",\"kernel_lattice\":",jmat(H),",\"kernel_inverse\":",jmatq(H^-1),",\"kernel_relation\":",jmat(Q),",\"ramified_artin\":",jmat(matrix(k,matsize(C)[2],i,j,lift(Mod(C[i,j],ds[i])))),"}");
  smithrec(Str(label,"_class_group"),Q,SM);
  my(image=D,selected=List(),allchecks=#rr);
  for(i=1,#rr,
    my(z=rr[i]);
    if(z[3]==1 && z[5]==0,
      my(v=Col(z[4]),im=mathnf(concat(image,v)));
      if(abs(matdet(im))<abs(matdet(image)),image=im;listput(selected,i));
    );
  );
  if(image!=H,error("degree-one primes do not generate entire class kernel"));
  print("{\"type\":\"prime_coordinates\",\"name\":\"",label,"\",\"total_checked\":",allchecks,",\"selected_indices\":",Vec(selected),",\"class_embedding\":",jmat(H*SM[1]^-1),",\"class_forward\":",jmatq(SM[1]*H^-1),",\"class_cyclic\":",vector(k,i,SM[3][i,i]),"}");
  for(i=1,#rr,
    my(z=rr[i]);
    if(i<=18 || setsearch(Set(Vec(selected)),i) || z[1]==73,
      print("{\"type\":\"frobenius_prime\",\"name\":\"",label,"\",\"index\":",i,",\"p\":",z[1],",\"prime_number\":",z[2],",\"residue_degree\":",z[3],",\"genus_coordinate\":",z[4],",\"kummer\":",z[5],",\"primitive_residue\":",z[6],",\"beta_residue\":",z[7],",\"zeta_residue\":",z[8],",\"upper_root\":",z[9],",\"ideal\":",jmat(z[10]),"}");
    );
  );
  return([ch,H,Q,SM,Vec(rr),Vec(selected)]);
};
run()={
  my(up=read("research_e81/code/e_prime73_field.bin"),ar=read("research_e81/code/e_prime73_artin.bin"));
  my(lo=read("research_e86/code/e_stable_lower_genus.bin"));
  my(RU=onefield("B2",up[1],ar[1],ar[3],ar[5],up[11],up[10]^3,ar[6]));
  my(RL=onefield("L2",lo[1],lo[2],lo[5][1],lo[6],Mod(x,lo[1].pol),Mod(x,lo[1].pol)^3/17,lo[7]));
  my(C=ar[6],D=ar[4],ds=ar[5],H=mathnf(matsolvemod(C,ds~,0,1)[2]),S=matsnf(H,1));
  if(abs(matdet(H))!=27,error("full principal S-divisor index"));
  smithrec("B2_principal_S_divisors",H,S);
  print("{\"type\":\"s_principal_map\",\"matrix\":[[1,1,1,0,0,0],[0,0,0,1,1,1],[0,0,0,0,1,2]],\"moduli\":[3,3,3]}");
  writebin("research_e86/code/e_stable_class_coordinates.bin",[RU,RL,H,S]);
  print("{\"type\":\"completion\",\"status\":\"PASS\"}");
};
run();
quit;
