default(parisize,512000000);
default(realprecision,100);
run()={
  my(K=nfinit(y^6+y^3+1),z=Mod(y,K.pol),u=-z^2*(1-z)^2,
     su=-z^8*(1-z^4)^2,s2u=-z^14*(1-z^7)^2);
  my(gamma=su*s2u^2,ratio=(3-u^3)/(3-su^3),rr=ratio*gamma);
  print("NORM_PHI ",ratio," GAMMA ",gamma," PRODUCT ",rr);
  for(i=0,2,
    my(roots=nfroots(K,x^3-rr/3^i));
    if(#roots,print("CUBE_IDENTITY exponent3=",i," ROOT ",roots[1]))
  );
  my(d=read("research_prime17/frattini_field.bin"),F=d[1],R=d[2],P=F.pol);
  my(zz=rnfeltreltoabs(R,z),r=rnfeltreltoabs(R,Mod(x,R.pol)));
  my(a=zz^2*(1-zz)^2,b=zz^8*(1-zz^4)^2,o=zz^3);
  my(h=(r+a)*(o^2*r+b)/((o^2*r+a)*(r+b)));
  my(h0=F.fu[1]*F.fu[6]*F.fu[7]^2*F.fu[8]/zz);
  my(exps=bnfisunit(F,h/h0));
  print("CROSS_RATIO_VECTOR_DIFFERENCE ",exps);
  print("CROSS_RATIO ",h);
};
run();
quit;
