\\ Targeted sparse integral L2 elements, with all relation algebra in certified L1.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
check(b,s)=if(!b,error(s));
run()={
 my(old=read("research_h_after_e97/cross_conjugate_norms.bin"),L=old[1],B=old[2],F=B.nf,E=old[3],C=old[4],A=old[5],z=Mod(x^3/17,F.pol));
 my(seen=Map(),prindex=Map(),prs=List(),vals=List(),cands=List(),norms=List(),tested=0,smooth=0);
 for(i=1,18,for(j=i+1,18,for(k=j+1,18,for(sj=0,1,for(sk=0,1,
   my(u=vector(18)~);u[i]=1;u[j]=(-1)^sj;u[k]=(-1)^sk;tested++;
   my(nv=nfeltmul(L,nfeltmul(L,u,A*u),A^2*u),nl=C*nv);check(E*nl==nv,"exact relative norm contraction");
   my(n=nfbasistoalg(F,nl));if(n==0 || mapisdefined(seen,Str(n)) || mapisdefined(seen,Str(-n)),next);
   mapput(seen,Str(n),1);my(nn=abs(nfeltnorm(F,n)),ff=factor(nn));
   if(matsize(ff)[1] && ff[matsize(ff)[1],1]>10000,next);
   my(fa=idealfactor(F,n),row=List());
   for(jj=1,matsize(fa)[1],my(key=Str(idealhnf(F,fa[jj,1])),ix);if(!mapisdefined(prindex,key,&ix),listput(prs,fa[jj,1]);ix=#prs;mapput(prindex,key,ix));listput(row,[ix,fa[jj,2]]));
   listput(cands,u);listput(norms,n);listput(vals,Vec(row));smooth++;
 )))));
 print("SPARSE_CANDIDATE_COUNTS ",[tested,#seen,smooth,#prs]);
 my(M=matrix(#prs,#vals));for(j=1,#vals,for(k=1,#vals[j],M[vals[j][k][1],j]=vals[j][k][2]));
 my(K=matkerint(M));check(M*K==matrix(#prs,matsize(K)[2]),"exact principal-divisor relation lattice");
 print("SPARSE_RELATION_DIMENSIONS ",matsize(M)," ",matsize(K));
 my(tu=bnfisunit(B,z),tinv=lift(Mod(tu[3],3)^-1),uc=matrix(3,matsize(K)[2]),hit=0);
 for(j=1,matsize(K)[2],
   my(factors=matrix(#norms,2,i,k,if(k==1,norms[i],K[i,j])),u=bnfisunit(B,factors));
   check(#u==3,"actual factored unit norm");uc[,j]=[u[1],u[2],lift(Mod(tinv*u[3],3))]~;
   if((u[1]%3 || u[2]%3) && !hit,hit=j;print("NEW_FREE_UNIT_NORM ",j," COORDINATES ",uc[,j]," SUPPORT ",select(i->K[i,j]!=0,vector(#norms,i,i))));
 );
 print("SPARSE_UNIT_NORM_MOD3_RANK ",matrank(Mod(uc,3))," FIRST_NEW_COLUMN ",hit);
 writebin("research_h_after_e97/sparse_norm_relations.bin",[B,L,Vec(cands),Vec(norms),Vec(prs),M,K,uc,hit]);
 print("DONE_EXACT_SPARSE_NORM_RELATIONS; absent new columns give no nonexistence conclusion");
};
run();
quit;
