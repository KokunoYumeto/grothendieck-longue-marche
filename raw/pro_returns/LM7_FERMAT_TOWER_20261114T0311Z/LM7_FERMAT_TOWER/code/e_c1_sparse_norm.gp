default(parisize,256000000);
default(parisizemax,2000000000);
run()={
  my(dat=read("research_e81/code/e_prime73_field.bin"),F=dat[2],R=dat[3],E=dat[4],xi=dat[10],beta=dat[11],zeta=xi^3,target=xi*(beta+1+3*zeta));
  my(roots=vector(18,i,(-xi)^i),mon=vector(9,j,beta^((j-1)\3)),targets=vector(6,i,(-zeta)^i*target),count=0);
  for(i=1,8,for(j=i+1,8,for(a=1,18,for(b=1,18,
    my(v=[Mod(1,F.pol),Mod(0,F.pol),Mod(0,F.pol)]);
    v[1+i%3]+=roots[a]*mon[i+1];v[1+j%3]+=roots[b]*mon[j+1];
    my(nm=v[1]^3+beta*v[2]^3+beta^2*v[3]^3-3*beta*v[1]*v[2]*v[3]);
    count++;
    for(k=1,6,if(nm==targets[k],
      my(b2=Mod(variable(E.pol),E.pol)-R[11][3]*R[11][2],g=1+rnfeltup(R,roots[a])*b2^i+rnfeltup(R,roots[b])*b2^j);
      if(rnfeltnorm(R,rnfeltabstorel(R,g))!=nm,error("literal norm verification"));
      print("SPARSE_NORM_WITNESS ",[i,j,a,b,k]," ELEMENT ",lift(g)," NORM ",lift(nm));
      writebin("research_e84/code/e_c1_sparse_norm_witness.bin",[g,nm,[i,j,a,b,k]]);
      print("DONE: exact norm witness after ",count," candidates.");return(1)
    ));
  ))));
  print("NO_EXACT_TARGET_AFTER ",count," THREE_TERM_CANDIDATES");
  print("DONE: bounded literal norm-form search; no non-norm inference.");
};
run();
quit;
