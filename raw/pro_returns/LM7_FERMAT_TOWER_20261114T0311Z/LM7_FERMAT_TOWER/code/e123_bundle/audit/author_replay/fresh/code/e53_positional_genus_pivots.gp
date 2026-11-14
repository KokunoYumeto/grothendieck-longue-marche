\\ Actual surviving-prime columns through the certified L1 idele presentation.
\\ No BNF reconstruction or certification is performed.
default(parisize,128000000);default(parisizemax,1000000000);
check(a,s)=if(!a,error(s));
jmat(A)=vector(matsize(A)[1],i,Vec(A[i,]));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
lc(L,beta,z,Q,T,u)={
 my(v=idealval(L,u,Q),nu=nfeltnorm(L,u)/2757^v,pr=nfmodprinit(L,T,'t),rr=nfmodpr(L,u/beta^idealval(L,u,T),pr)^((53^2-1)/3),zz=nfmodpr(L,z,pr));
 check(valuation(nu,3)==0 && valuation(nu-1,3)>=2,"exact wild character domain");
 [lift(Mod(-(nu-1)/9,3)),if(rr==1,0,if(rr==zz,2,if(rr==zz^2,1,error("tame phase"))))];
};
{
 my(D=read("../inputs/e119_positional_genus_transition.bin"),L=D[1][4],SS=D[1][5],G=D[2],H=D[8],K=D[10],KS=D[12]);
 my(beta=Mod(x,L.pol),z=beta^3/53,row=[1,1,1,1],out=List(),piv=List(),columns=matrix(2,0));
 check(L.pol==x^6+53*x^3+2809 && L.cyc==[9,3],"literal certified lower field");
 check(K*D[11]==H && KS[1]*D[11]*KS[2]==KS[3],"exact retained lower Smith maps");
 forprime(p=5,3000,
  if(p!=53 && p%9==4 && Mod(53,p)^((p-1)/3)!=1,
   my(m=(p-1)/3,bp=lift(Mod(53,p)^(3*lift(Mod(27,m)^-1))),b1=lift(Mod(bp,p)^3),PP=idealprimedec(L,p),hit=0);
   check(Mod(bp,p)^m==1 && Mod(bp,p)^27==Mod(53,p)^3,"unique prime-to-three positional residue");
   for(i=1,#PP,if(PP[i][4]==1 && idealval(L,beta-b1,PP[i])>0,check(!hit,"unique chosen lower prime");hit=i));
   check(hit,"chosen lower prime exists");
   my(P=PP[hit],cl=bnfisprincipal(L,P,0),I=idealdiv(L,P,idealfactorback(L,G,cl)),pr=bnfisprincipal(L,I,3));
   check(pr[1]==[0,0]~,"exact lower principal correction");
   my(a=nfbasistoalg(L,pr[2]));check(idealhnf(L,a)==idealhnf(L,I),"complete ideal correction verified");
   my(ch=lc(L,beta,z,SS[1],SS[2],a),raw=concat(-Col(ch),cl),back=KS[1]*K^-1*raw);
   check(denominator(back)==1 && lift(Mod(row*raw,3))==0,"actual Frobenius lies in norm-coinvariant subgroup");
   my(sc=[lift(Mod(back[1],9)),lift(Mod(back[2],3))],cb=[lift(Mod(2*(sc[2]-sc[1]),3)),sc[1]%3]);
   check(cb[2]==1,"positive horizontal Artin coordinate agrees with p=4 mod9");
   my(rec=[p,bp,b1,jmat(idealhnf(L,P)),Vec(cl),cf(a,6),ch,Vec(raw),sc,cb]);
   listput(out,rec);
   my(nc=concat(columns,Col(cb)));
   if(matrank(Mod(nc,3))>matsize(columns)[2],listput(piv,rec);columns=nc);
   if(#piv==2,break);
  )
 );
 check(#piv==2 && matrank(Mod(columns,3))==2,"two actual prime classes form a full C9-square basis");
 print("{\"type\":\"actual_surviving_pivot_primes\",\"record_fields\":[\"p\",\"beta2_residue\",\"beta1_residue\",\"lower_prime_HNF\",\"lower_class\",\"principal_correction_coefficients\",\"local_characters\",\"raw_idele\",\"projected_L2_class\",\"full_L2_class_mod3\"],\"records\":",Vec(out),",\"pivot_records\":",Vec(piv),",\"basis_mod3\":",jmat(columns),",\"positive_horizontal_character\":1}");
 writebin("e53_positional_genus_pivots.bin",[D,Vec(out),Vec(piv),columns]);
 print("{\"type\":\"completion\",\"status\":\"PASS\",\"scope\":\"literal lower ideals and principal corrections; actual projected Artin coordinates; full upper basis by proved C9-square type\"}");
}
quit;
