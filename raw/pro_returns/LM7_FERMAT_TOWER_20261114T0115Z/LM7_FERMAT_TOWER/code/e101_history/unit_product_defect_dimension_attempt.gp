\\ Verify the literal reversed norm, switch its split cyclic algebra, and evaluate the ideal defect.
\\ No BNF of either degree-eighteen upper field is used.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(101973);
check(b,s)=if(!b,error(s));
red(v,d)=vector(#d,i,lift(Mod(v[i],d[i])))~;
run()={
 my(lo=read("research_e86/code/e_stable_lower_genus.bin"),BL=lo[1],F=BL.nf,b=Mod(x,F.pol),z=b^3/17,eps=BL.fu[1]*BL.fu[2]);
 my(cc=[-727515263/325069,1483832284/975207,-337829378/975207,-372446152/5526173,415980086/16578519,-548768638/16578519,
 9498802579/975207,-1383497124/325069,-187770724/975207,5646166658/16578519,-2093309222/5526173,1260332509/16578519,
 -32443820446/975207,-6380139610/975207,517553942/325069,-53737480949/16578519,14839765429/16578519,-734246879/5526173]~);
 my(uu=vector(3,j,sum(i=0,5,cc[6*(j-1)+i+1]*b^i)),Y=varhigher("Y",x),u=Mod(sum(j=0,2,uu[j+1]*Y^j),Y^3-eps));
 check(norm(u)==b,"literal reversed unit-radical norm beta1");
 my(A=[0,0,eps;1,0,0;0,1,0],S=matdiagonal([1,z,z^2]),B=sum(j=0,2,uu[j+1]*A^j)*S);
 check(A^3==eps*matid(3) && B^3==b*matid(3) && B*A==z*A*B,"actual split cyclic-algebra identities");
 my(Z=varhigher("Z",Y),t=Mod(Z,Z^3-b),v=matker(B-t*matid(3))[,1]);
 check(v[3]!=0,"specified eigenline normalization");v=v/v[3];
 my(sv=vector(3,i,Mod(subst(lift(v[i]),Z,z*Z),Z^3-b))~,w=v[2]);
 check(A*v==w*sv && norm(w)==eps,"exact switched unit norm");
 my(L=read("research_norm_index/code/prime3_field2.bin")[1],aa=Mod(x,L.pol),za=aa^9/17,va=vector(3,i,Mod(0,L.pol))~);
 for(i=1,3,for(j=0,2,va[i]+=subst(lift(polcoef(lift(v[i]),j,Z)),x,aa^3)*aa^j));
 my(wa=va[2],aut=nfalgtobasis(L,za*aa),wv=nfalgtobasis(L,wa));
 check(nfeltmul(L,nfeltmul(L,wv,nfgaloisapply(L,aut,wv)),nfgaloisapply(L,aut,nfgaloisapply(L,aut,wv)))==nfalgtobasis(L,subst(lift(eps),x,aa^3)),"absolute switched norm");
 my(I=idealhnf(L,va[1]));for(i=2,3,I=idealadd(L,I,va[i]));
 my(D=idealinv(L,I));
 check(idealdiv(L,nfgaloisapply(L,aut,D),D)==idealhnf(L,wa),"exact sigma(D)/D=(w) from eigenline ideal");
 my(J=D,best=10^100,chosen,fac);
 for(k=1,16,
   my(rr=idealred(L,[D,1],if(k==1,vector(9),vector(9,j,random(20)))),nn=idealnorm(L,rr[1]));
   if(nn<best,best=nn;J=rr[1];chosen=rr;print("DEFECT_CLASS_REDUCTION ",k," NORM ",best));
 );
 fac=idealfactor(L,J);my(arts=vector(#lo[6],i,0)~,rows=List(),emb=matrix(18,6,i,j,nfalgtobasis(L,subst(lift(F.zk[j]),x,aa^3))[i]));
 for(i=1,matsize(fac)[1],
   my(P=fac[i,1],power=fac[i,2],p=P[1]);check(isprime(p),"certified divisor prime");
   if(p==3 || p==17,listput(rows,[p,P.f,power,"strongly ambiguous S-prime"]);next);
   my(qs=idealprimedec(F,p),found=0);
   for(j=1,#qs,
     my(Q=qs[j],ext=idealhnf(L,p,emb*Q[2]));
     if(idealval(L,ext,P)==0,next);
     check(found==0 && P.f%Q.f==0,"unique actual contraction");found=j;
     my(f=P.f/Q.f,ar=red(lo[5][1]*bnrisprincipal(lo[2],Q,0),lo[6]));arts+=power*f*ar;
     listput(rows,[p,P.f,power,Q.f,f,Vec(ar)]);
   );
   check(found!=0,"found actual contracted prime");
 );
 my(ga=red(arts,lo[6]),CF=[1,-3,-3;0,1,0;1/3,-2/3,-2/3],cl=red(CF*ga,[9,3,1]),defect=red(cl,[3,3,1]));
 print("UNIT_PRODUCT_GENUS ",ga," CLASS_MOD_STRONG ",defect);
 print("UNIT_PRODUCT_DEFECT_PRIMES ",Vec(rows));
 check(defect[1]==0 && defect[3]==0,"horizontal norm-plane defect constraint");
 writebin("research_h_after_e97/unit_product_defect.bin",[BL,L,cc,u,A,S,B,v,w,va,wa,aut,I,D,J,chosen,fac,Vec(rows),ga,cl,defect]);
 print("DONE_EXACT_UNIT_PRODUCT_DEFECT ",defect[2]);
};
run();
quit;
