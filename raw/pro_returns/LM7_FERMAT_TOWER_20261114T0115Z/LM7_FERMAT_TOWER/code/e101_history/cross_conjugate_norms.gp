\\ Targeted principal sigma-orbit differences in L2; no upper BNF.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(971791);
check(b,s)=if(!b,error(s));
avec(F,u)=if(type(u)=="t_COL",u,nfalgtobasis(F,u));
red(v,d)=vector(#d,i,lift(Mod(v[i],d[i])))~;
run()={
  my(lo=read("research_e86/code/e_stable_lower_genus.bin"),BL=lo[1],FL=BL.nf);
  my(dat=read("research_norm_index/code/prime3_field2.bin"),F=dat[1],t=Mod(x,F.pol),z=t^9/17);
  my(aut=nfalgtobasis(F,z*t),A=matrix(18,18,i,j,nfalgtobasis(F,nfgaloisapply(F,aut,F.zk[j]))[i]));
  check(A^3==matid(18),"actual sigma action");
  my(E=matrix(18,6,i,j,nfalgtobasis(F,subst(lift(FL.zk[j]),x,t^3))[i]),D=(E~*E)^-1*E~);
  check(D*E==matid(6),"actual lower-field coordinate inverse");
  my(CF=[1,-3,-3;0,1,0;1/3,-2/3,-2/3],recs=List(),vectors=List(),classes=List(),seen=Map());
  my(zl=Mod(x^3/17,FL.pol),zc=red(bnfisunit(BL,zl),[3,3,3]));
  listput(vectors,zc);listput(classes,[0,1]~);
  print("SEED_ZETA_UNIT_COORDINATE ",zc," DEFECT ",[0,1]~);
  for(target=1,2,
    my(p=if(target==1,7,73),r=if(target==1,-1,63),P=idealhnf(F,p,x-r),LP=idealhnf(FL,p,x-r^3));
    check(idealnorm(F,P)==p && idealnorm(FL,LP)==p,"actual chosen degree-one prime");
    my(ar=red(lo[5][1]*bnrisprincipal(lo[2],LP,0),lo[6]),cl=red(CF*vector(3,i,ar[i])~,[9,3,1]),M=Map(),collisions=0,cross=0);
    print("TARGET ",[p,r]," ORDINARY_CLASS ",cl);
    for(k=1,500,
      my(weights=if(k==1,vector(9),vector(9,j,random(40))),rr=idealred(F,[P,1],weights));
      my(J=idealhnf(F,rr[1]),g=avec(F,if(type(rr[2])=="t_MAT",nffactorback(F,rr[2]),rr[2])),Pi=P);
      check(idealmul(F,J,g)==Pi,"actual reduction orientation");
      for(j=0,2,
        my(key=Str(J),prev);
        if(mapisdefined(M,key,&prev),
          collisions++;
          if(j!=prev[2],
            cross++;
            my(u=nfeltdiv(F,g,prev[1]),nu=nfeltmul(F,nfeltmul(F,u,A*u),A^2*u),nv=D*nu);
            check(E*nv==nu && idealhnf(FL,nv)==matid(6),"ordinary lower unit norm");
            my(uc=bnfisunit(BL,nv),v=red(uc,[3,3,3]),c=vector(2,i,lift(Mod((j-prev[2])*cl[i],3)))~,kk=Str(v));
            check(#uc==3,"literal lower ordinary unit coordinates");
            check(idealhnf(F,u)==idealdiv(F,Pi,prev[3]),"exact conjugate-prime divisor");
            if(!mapisdefined(seen,kk),
              mapput(seen,kk,1);listput(vectors,v);listput(classes,c);
              listput(recs,[p,r,k,j,prev[2],u,nv,uc,v,c]);
              print("NEW_EXACT_NORM_DEFECT ",[p,r,k,j,prev[2]]," UNIT_COORDINATES ",uc," MOD3 ",v," CLASS ",c);
              print("INPUT_RANK ",matrank(Mod(Mat(Vec(vectors)),3))," AUGMENTED_RANK ",matrank(Mod(concat(Mat(Vec(vectors))~,Mat(Vec(classes))~),3)));
            );
          );
        ,
          mapput(M,key,[g,j,Pi])
        );
        J=idealhnf(F,nfgaloisapply(F,aut,J));g=A*g;Pi=idealhnf(F,nfgaloisapply(F,aut,Pi));
      );
      if(k%100==0,print("PROGRESS ",target," ",k," IDEALS ",#M," COLLISIONS ",collisions," CROSS ",cross));
      if(matrank(Mod(Mat(Vec(vectors)),3))==3,break);
    );
    print("TARGET_COMPLETE ",target," IDEALS ",#M," COLLISIONS ",collisions," CROSS ",cross);
    if(matrank(Mod(Mat(Vec(vectors)),3))==3,break);
  );
  my(V=Mat(Vec(vectors)),C=Mat(Vec(classes)));
  check(matrank(Mod(concat(V~,C~),3))==matrank(Mod(V,3)),"all exact defect records define one linear map");
  print("FINAL_INPUT_RANK ",matrank(Mod(V,3))," RECORDS ",#recs);
  writebin("research_h_after_e97/cross_conjugate_norms.bin",[F,BL,E,D,A,Vec(recs),V,C]);
  print("DONE_TARGETED_IDEAL_ORBIT_CALCULATION; no conclusion is inferred from absent collisions");
};
run();
quit;
