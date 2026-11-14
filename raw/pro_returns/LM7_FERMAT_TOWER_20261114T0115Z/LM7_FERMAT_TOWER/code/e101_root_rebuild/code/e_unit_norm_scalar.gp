\\ E101: exact scalar in the ordinary-unit norm defect. No upper BNF input.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(101973);
check(b,s)=if(!b,error(s));
red(v,d)=vector(#d,i,lift(Mod(v[i],d[i])))~;
jfrac(q)=[numerator(q),denominator(q)];
jpoly(p,n)=vector(n,i,jfrac(polcoef(lift(p),i-1)));
jmat(M)=vector(matsize(M)[1],i,vector(matsize(M)[2],j,lift(M[i,j])));
jrat(M)=vector(matsize(M)[1],i,vector(matsize(M)[2],j,jfrac(M[i,j])));
emit(n,v)=print("{\"name\":\"",n,"\",\"value\":",v,"}");
run()={
 my(lo=read("research_e86/code/e_stable_lower_genus.bin"),BL=lo[1],F=BL.nf,b=Mod(x,F.pol),z=b^3/17,eps=BL.fu[1]*BL.fu[2]);
 my(cc=[-727515263/325069,1483832284/975207,-337829378/975207,-372446152/5526173,415980086/16578519,-548768638/16578519,
 9498802579/975207,-1383497124/325069,-187770724/975207,5646166658/16578519,-2093309222/5526173,1260332509/16578519,
 -32443820446/975207,-6380139610/975207,517553942/325069,-53737480949/16578519,14839765429/16578519,-734246879/5526173]~);
 my(uu=vector(3,j,sum(i=0,5,cc[6*(j-1)+i+1]*b^i)),Y=varhigher("Y",x),u=Mod(sum(j=0,2,uu[j+1]*Y^j),Y^3-eps));
 check(norm(u)==b,"literal reversed norm beta1");
 my(A=[0,0,eps;1,0,0;0,1,0],S=matdiagonal([1,z,z^2]),B=sum(j=0,2,uu[j+1]*A^j)*S);
 check(A^3==eps*matid(3) && B^3==b*matid(3) && B*A==z*A*B,"split cyclic algebra");
 my(Z=varhigher("Z",Y),t=Mod(Z,Z^3-b),ker=matker(B-t*matid(3)));
 check(matsize(ker)==[3,1] && ker[3,1]!=0,"one-dimensional normalized eigenline");
 my(v=ker[,1]/ker[3,1],sv=vector(3,i,Mod(subst(lift(v[i]),Z,z*Z),Z^3-b))~,w=v[2]);
 check(A*v==w*sv && norm(w)==eps,"switched norm");
 my(P=x^18+17*x^9+289,bas=concat(vector(9,i,x^(i-1)),vector(9,i,x^(i+8)/17)),L=nfinit([P,bas,[3,17]]),aa=Mod(x,P),za=aa^9/17,va=vector(3,i,Mod(0,P))~);
 check(L.disc==-3^45*17^16,"exact upper discriminant");
 for(i=1,3,for(j=0,2,va[i]+=subst(lift(polcoef(lift(v[i]),j,Z)),x,aa^3)*aa^j));
 my(wa=va[2],aut=nfalgtobasis(L,za*aa),wv=nfalgtobasis(L,wa));
 check(nfeltmul(L,nfeltmul(L,wv,nfgaloisapply(L,aut,wv)),nfgaloisapply(L,aut,nfgaloisapply(L,aut,wv)))==nfalgtobasis(L,subst(lift(eps),x,aa^3)),"absolute norm");
 my(I=idealhnf(L,va[1]));for(i=2,3,I=idealadd(L,I,va[i]));
 my(D=idealinv(L,I));
 check(idealdiv(L,nfgaloisapply(L,aut,D),D)==idealhnf(L,wa),"eigenline ideal sigma(D)/D=(w)");
 my(J=D,best=10^100,chosen,fac,reductions=List());
 for(k=1,16,
   my(rr=idealred(L,[D,1],if(k==1,vector(9),vector(9,j,random(20)))),nn=idealnorm(L,rr[1]));
   listput(reductions,[k,nn]);
   if(nn<best,best=nn;J=rr[1];chosen=rr;print("DEFECT_CLASS_REDUCTION ",k," NORM ",best));
 );
 my(mult=if(type(chosen[2])=="t_MAT",nffactorback(L,chosen[2]),chosen[2]));
 check(idealmul(L,J,mult)==D,"exact reduced-ideal multiplier");
 fac=idealfactor(L,J);my(arts=vector(#lo[6],i,0)~,rows=List(),emb=matrix(18,6,i,j,nfalgtobasis(L,subst(lift(F.zk[j]),x,aa^3))[i]));
 for(i=1,matsize(fac)[1],
   my(Qup=fac[i,1],power=fac[i,2],p=Qup[1]);check(isprime(p),"certified rational prime");
   check(p!=3 && p!=17,"retained reduced divisor has no S support");
   my(qs=idealprimedec(F,p),found=0);
   for(j=1,#qs,
     my(Q=qs[j],ext=idealhnf(L,p,emb*Q[2]));
     if(idealval(L,ext,Qup)==0,next);
     check(found==0 && Qup.f%Q.f==0,"unique actual contraction");found=j;
     my(f=Qup.f/Q.f,ar=red(lo[5][1]*bnrisprincipal(lo[2],Q,0),lo[6]));
     arts+=power*f*ar;listput(rows,[p,Qup.f,power,Q.f,f,Vec(ar)]);
   );
   check(found!=0,"actual contracted prime exists");
 );
 my(ga=red(arts,lo[6]),CF=[1,-3,-3;0,1,0;1/3,-2/3,-2/3],CI=CF^-1,cl=red(CF*vector(3,i,ga[i])~,[9,3,1]),defect=red(cl,[3,3,1]));
 check(defect==[0,2,0]~,"evaluated exact defect");
 my(c1=b+1+3*z);
 check(3==-c1^6*eps^2,"literal radical comparison");
 emit("lower_units",vector(2,i,jpoly(BL.fu[i],6)));
 emit("reversed_norm_coefficients",vector(3,j,vector(6,i,jfrac(cc[6*(j-1)+i]))));
 emit("absolute_eigenvector",vector(3,i,jpoly(va[i],18)));
 emit("absolute_witness",jpoly(wa,18));
 emit("exact_reduction_multiplier",jpoly(nfbasistoalg(L,mult),18));
 emit("reduced_ideal_hnf",jmat(J));
 emit("reduced_ideal_norm",best);
 emit("actual_contracted_prime_rows",Vec(rows));
 emit("genus_coordinate",Vec(ga));
 emit("class_forward",jrat(CF));emit("class_inverse",jmat(CI));
 emit("full_ordinary_ideal_class",Vec(cl));emit("ordinary_unit_defect",Vec(defect));
 emit("weighted_reductions",Vec(reductions));
 writebin("research_e101/code/e_unit_norm_scalar.bin",[BL,L,cc,u,A,S,B,v,w,va,wa,aut,I,D,J,chosen,fac,Vec(rows),ga,cl,defect]);
 print("{\"type\":\"completion\",\"status\":\"PASS\",\"statement\":\"E.101\",\"unit_product_defect\":[0,2]}");
};
run();
quit;
