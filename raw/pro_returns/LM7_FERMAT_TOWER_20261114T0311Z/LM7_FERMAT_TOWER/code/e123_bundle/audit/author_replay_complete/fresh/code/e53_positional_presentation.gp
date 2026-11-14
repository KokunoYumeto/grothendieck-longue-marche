\\ Certify a proposed S-class presentation by literal ideals and independent pivots.
\\ No bnfcertify or bnfinit is used.  The independent C9^2 theorem and
\\ lower-idele pivot computation prove surjectivity and the order lower bound.
default(parisize,256000000);default(parisizemax,1000000000);
check(a,s)=if(!a,error(s));
jmat(A)=vector(matsize(A)[1],i,Vec(A[i,]));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
literal(B,I)={
 my(pr=bnfisprincipal(B,I,5));check(pr[1]==Col(vector(#B.cyc)),"candidate supplied a principal relation");
 my(a=nfbasistoalg(B,nffactorback(B,pr[2])));
 check(idealhnf(B,a)==idealhnf(B,I),"independent full ideal equality");a;
};
{
 my(B=read("../inputs/e122_L2_candidate_bnf.bin"),beta=Mod(x,B.pol),S=concat(idealprimedec(B,3),idealprimedec(B,53)),C=matrix(#B.cyc,#S),powers=vector(#B.cyc),sr=vector(#S));
 check(B.pol==x^18+53*x^9+2809 && B.cyc==[9,9,3],"literal proposed field and presentation");
 print("{\"type\":\"start\",\"method\":\"literal ideal relations plus independent generating primes; no BNF certification\"}");
 for(i=1,#B.cyc,
  powers[i]=literal(B,idealpow(B,B.gen[i],B.cyc[i]));
  print("{\"type\":\"class_power_relation\",\"index\":",i,",\"exponent\":",B.cyc[i],",\"generator_coefficients\":",cf(powers[i],18),"}");
 );
 for(i=1,#S,
  C[,i]=bnfisprincipal(B,S[i],0);sr[i]=literal(B,idealdiv(B,S[i],idealfactorback(B,B.gen,C[,i])));
  print("{\"type\":\"S_prime_relation\",\"index\":",i,",\"prime\":",S[i][1],",\"class_column\":",Vec(C[,i]),",\"prime_HNF\":",jmat(idealhnf(B,S[i])),",\"generator_coefficients\":",cf(sr[i],18),"}");
 );
 my(Rel=concat(matdiagonal(B.cyc),C),H=mathnf(Rel),SN=matsnf(H,1),UF=SN[1],Diag=SN[3],ds=vector(#B.cyc,i,Diag[i,i]));
 check(ds==[9,9,1] && UF*H*SN[2]==Diag,"actual proposed S-presentation order81 and Smith inverse");
 my(pp=[31,103],bb=[27,80],piv=vector(2),cols=matrix(3,2),sc=matrix(2,2));
 for(j=1,2,
  my(PP=idealprimedec(B,pp[j]),hit=0);
  for(i=1,#PP,if(PP[i][4]==1 && idealval(B,beta-bb[j],PP[i])>0,check(!hit,"unique actual pivot ideal");hit=i));
  check(hit,"actual pivot ideal found");my(P=PP[hit],c=bnfisprincipal(B,P,0),a=literal(B,idealdiv(B,P,idealfactorback(B,B.gen,c))),ss=UF*c);
  cols[,j]=c;sc[,j]=[lift(Mod(ss[1],9)),lift(Mod(ss[2],9))]~;piv[j]=[P,c,a];
  print("{\"type\":\"upper_pivot_relation\",\"prime\":",pp[j],",\"beta_residue\":",bb[j],",\"prime_HNF\":",jmat(idealhnf(B,P)),",\"class_column\":",Vec(c),",\"Smith_column\":",Vec(sc[,j]),",\"generator_coefficients\":",cf(a,18),"}");
 );
 check(lift(Mod(matdet(sc),3))!=0,"actual certified prime classes generate the entire proposed presentation");
 my(inv=lift(Mod(sc,9)^-1),coord=lift(Mod(inv*UF[1..2,],9)));
 check(lift(Mod(coord*cols,9))==matid(2) && lift(Mod(coord*Rel,9))==matrix(2,matsize(Rel)[2]),"full exact prime-basis maps");
 print("{\"type\":\"full_S_class_presentation\",\"relation_matrix\":",jmat(Rel),",\"relation_HNF\":",jmat(H),",\"Smith_left\":",jmat(UF),",\"Smith_right\":",jmat(SN[2]),",\"Smith_diagonal\":",jmat(Diag),",\"pivot_Smith_matrix\":",jmat(sc),",\"pivot_Smith_inverse\":",jmat(inv),",\"generator_to_prime_basis\":",jmat(coord),",\"prime_basis_to_generator\":",jmat(cols),",\"class_generator_HNF\":",vector(#B.gen,i,jmat(idealhnf(B,B.gen[i]))),",\"field_integral_basis\":",vector(18,i,cf(Mod(B.zk[i],B.pol),18)),",\"field_discriminant\":\"",B.disc,"\"}");
 writebin("e53_positional_presentation.bin",[B,S,C,powers,sr,Rel,H,SN,piv,cols,sc,inv,coord]);
 print("{\"type\":\"completion\",\"status\":\"PASS\",\"basis\":[31,103],\"orders\":[9,9],\"literal_equalities\":",#B.cyc+#S+2,",\"certification_scope\":\"full actual three-primary S-class group, using E121 order and the independently computed E119 Artin columns; no unit-group assertion\"}");
}
quit;
