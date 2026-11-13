\\ Collect exact relations among small relative norms, entirely in the certified L1 field.
\\ This is a bounded targeted relation search, not a new upper class-group computation.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
check(b,s)=if(!b,error(s));
run()={
 my(B=read("research_e86/code/e_stable_lower_genus.bin")[1],F=B.nf,b=Mod(x,F.pol),z=b^3/17,seen=Map(),prindex=Map(),prs=List(),vals=List(),cands=List(),norms=List());
 my(coeff=vector(9,j,(j-1)%3-1+((j-1)\3-1)*z),tested=0,smooth=0);
 for(ir=1,9,for(iq=1,9,for(ip=1,9,
   my(r=coeff[ir],q=coeff[iq],p=coeff[ip]);if(r==0 && q==0 && p==0,next);
   my(n=r^3+b*q^3+b^2*p^3-3*b*p*q*r);tested++;
   if(n==0 || mapisdefined(seen,Str(n)) || mapisdefined(seen,Str(-n)),next);
   mapput(seen,Str(n),1);
   my(nn=abs(nfeltnorm(F,n)),ff=factor(nn));
   if(matsize(ff)[1] && ff[matsize(ff)[1],1]>10000,next);
   my(fa=idealfactor(F,n),row=List());
   for(j=1,matsize(fa)[1],my(key=Str(idealhnf(F,fa[j,1])),ix);if(!mapisdefined(prindex,key,&ix),listput(prs,fa[j,1]);ix=#prs;mapput(prindex,key,ix));listput(row,[ix,fa[j,2]]));
   listput(cands,[r,q,p]);listput(norms,n);listput(vals,Vec(row));smooth++;
 )));
 print("CANDIDATE_COUNTS ",[tested,#seen,smooth,#prs]);
 my(M=matrix(#prs,#vals));for(j=1,#vals,for(k=1,#vals[j],M[vals[j][k][1],j]=vals[j][k][2]));
 my(K=matkerint(M));check(M*K==matrix(#prs,matsize(K)[2]),"exact principal-divisor relation lattice");
 print("RELATION_DIMENSIONS ",matsize(M)," ",matsize(K));
 my(tu=bnfisunit(B,z),tinv=lift(Mod(tu[3],3)^-1),uc=matrix(3,matsize(K)[2]),hit=0);
 for(j=1,matsize(K)[2],
   my(factors=matrix(#norms,2,i,k,if(k==1,norms[i],K[i,j])),u=bnfisunit(B,factors));
   check(#u==3,"actual factored unit norm");uc[,j]=[u[1],u[2],lift(Mod(tinv*u[3],3))]~;
   if((u[1]%3 || u[2]%3) && !hit,hit=j;print("NEW_FREE_UNIT_NORM ",j," COORDINATES ",uc[,j]," SUPPORT ",select(i->K[i,j]!=0,vector(#norms,i,i))));
 );
 print("UNIT_NORM_MOD3_RANK ",matrank(Mod(uc,3))," FIRST_NEW_COLUMN ",hit);
 writebin("research_h_after_e97/simple_norm_relations.bin",[B,Vec(cands),Vec(norms),Vec(prs),M,K,uc,hit]);
 print("DONE_EXACT_SIMPLE_NORM_RELATIONS; absent new columns give no nonexistence conclusion");
};
run();
quit;
