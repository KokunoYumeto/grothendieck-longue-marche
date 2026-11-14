\\ Complete actual B1/L1 S-unit map in the displayed first positional field.
default(parisize,256000000);default(parisizemax,2000000000);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
{
 my(D=read("e53_six_character_witness.bin"),Hd=read("e53_horizontal_base.bin"),B=D[1],alpha=D[2],xi=D[3],beta=D[4],U=D[7],L=Hd[4],S=Hd[5],US=bnfunits(L,S),lower=vector(#US[1],i,nfbasistoalg(L,nffactorback(L,US[1][i]))),z=Mod(x^3/53,L.pol),tz=bnfisunit(L,z,US)[5]);
 my(tensor=vector(18,j,alpha^((j-1)%3)*xi^((j-1)\3)),TC=matrix(18,18,i,j,polcoef(lift(tensor[j]),i-1)),NM=matrix(5,#U),norms=vector(#U),inds=[1,5,9,10,14,18]);
 for(j=1,#U,
  my(nu=prod(k=0,2,subst(lift(U[j]),x,xi^(4^k)-alpha*xi^(-3*k))),nc=matsolve(TC,Col(vector(18,i,polcoef(lift(nu),i-1)))));
  for(k=1,18,if(!setsearch(Set(inds),k),check(nc[k]==0,"actual horizontal fixed field")));
  my(nn=Mod(sum(k=1,6,nc[inds[k]]/if(k<=3,1,53)*x^(k-1)),L.pol),ex=bnfisunit(L,nn,US));
  check(#ex==5,"actual positional S-unit norm");
  norms[j]=nn;NM[1,j]=lift(Mod(ex[5],3)/Mod(tz,3));NM[2,j]=ex[3];NM[3,j]=ex[4];NM[4,j]=ex[1];NM[5,j]=ex[2];
 );
 my(Rel=concat(NM,Mat([3,0,0,0,0]~)),H=mathnf(Rel));
 check(abs(matdet(H))==1,"actual full S-unit norm surjectivity");
 print("{\"type\":\"positional_horizontal_norm\",\"basis_order\":\"zeta,fu1,fu2,firstSunit,secondSunit\",\"lower_basis\":",concat([cf(z,6)],vector(4,i,cf(lower[[3,4,1,2][i]],6))),",\"norm_matrix\":",jmat(NM),",\"image_HNF\":",jmat(H),",\"full_index\":1}");
 writebin("e53_positional_horizontal_norm.bin",[D,Hd,lower,NM,H,norms]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
