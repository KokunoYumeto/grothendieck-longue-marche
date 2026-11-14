\\ E106 actual prime-seven and prime-73 Frobenii in the certified B1 ray field.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
ck(b,s)=if(!b,error(s));
rows(A)=vector(matsize(A)[1],i,Vec(A[i,]));
run()={
 my(dat=read("e106_B1_bnf.bin"),B=dat[1],F=B.nf,xi=dat[2],a=dat[3],beta=a*xi);
 my(G9=read("e106_ninth_genus.bin"),T=read("e106_ninth_transfer.bin"),R=G9[1],U=G9[5]);
 ck(bnfcertify(B)==1,"certified B1 input");
 my(P7=idealadd(F,7,beta+1));
 ck(idealnorm(F,P7)==343,"actual degree-three prime seven");
 my(fac=idealfactor(F,P7));ck(matsize(fac)==[1,2] && fac[1,2]==1 && fac[1,1].p==7 && fac[1,1].f==3,"prime seven factorization");
 my(cl=bnrisprincipal(R,P7,0),sh=U*cl,rel=[lift(Mod(sh[2],9)),lift(Mod(sh[3],9)),lift(Mod(sh[4],3))]);
 ck(lift(Mod(Mat(T[1])*cl,9))==[0]~,"prime seven splits in B3");
 print("{\"name\":\"prime7\",\"ideal_hnf\":",rows(P7),",\"norm\":343,\"relative_class\":",rel,",\"ray_class\":",Vec(cl),",\"smith_class\":",Vec(sh),"}");
 my(ps=idealprimedec(F,73),P73=0);
 for(i=1,#ps,if(idealval(F,xi-55,ps[i])>0 && idealval(F,beta-22,ps[i])>0,P73=ps[i]));
 ck(P73!=0 && P73.f==1,"actual prime73");
 cl=bnrisprincipal(R,P73,0);sh=U*cl;rel=[lift(Mod(sh[2],9)),lift(Mod(sh[3],9)),lift(Mod(sh[4],3))];
 ck(rel==[1,8,2] && lift(Mod(Mat(T[1])*cl,9))==[0]~,"actual prime73 class");
 print("{\"name\":\"prime73\",\"ideal_hnf\":",rows(idealhnf(F,P73)),",\"norm\":73,\"relative_class\":",rel,",\"ray_class\":",Vec(cl),",\"smith_class\":",Vec(sh),"}");
 print("{\"type\":\"completion\",\"status\":\"PASS\",\"statement\":\"E.106\"}");
};
run();
quit;
