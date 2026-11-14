\\ Literal norm image and independent3-saturation; no default upper BNF certification.
default(parisize,256000000);default(parisizemax,2000000000);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
{
 my(D=read("e53_six_character_witness.bin"),B=D[1],alpha=D[2],xi=D[3],beta=D[4],U=D[7],Q=D[5],T=D[6],V=D[9],C=D[10]);
 my(MD=read("../inputs/e116_prime_columns.bin"),M=MD[1][2],ma=MD[1][4],mz=MD[1][5],mq=MD[1][11],mell=MD[1][12][1],qg=MD[2]);
 my(tensor=vector(18,j,alpha^((j-1)%3)*xi^((j-1)\3)),TC=matrix(18,18,i,j,polcoef(lift(tensor[j]),i-1)),UC=matrix(18,#U),NM=matrix(7,#U),norms=vector(#U),tors=bnfisunit(M,mz)[3]);
 check(matdet(TC)!=0,"actual tensor basis");
 for(j=1,#U,
  UC[,j]=matsolve(TC,Col(vector(18,i,polcoef(lift(U[j]),i-1))));
  my(nu=prod(k=0,2,subst(lift(U[j]),x,xi^(4^k)-alpha)),nc=matsolve(TC,Col(vector(18,i,polcoef(lift(nu),i-1)))));
  for(k=1,18,if((k-1)\3!=0 && (k-1)\3!=3,check(nc[k]==0,"actual norm fixed field")));
  my(nn=sum(k=0,2,nc[k+1]*ma^k+nc[k+10]*mz*ma^k),vv=vector(4,k,if(k<=3,idealval(M,nn,mq[k]),idealval(M,nn,mell))));
  my(rest=nn/prod(k=1,3,qg[k]^vv[k])/ma^vv[4],ex=bnfisunit(M,rest));
  check(#ex==3,"literal lower S-unit norm");
  NM[1,j]=lift(Mod(ex[3],3)/Mod(tors,3));NM[2,j]=ex[1];NM[3,j]=ex[2];
  for(k=1,4,NM[k+3,j]=vv[k]);norms[j]=nn;
 );
 my(rel=concat(NM,Mat([3,0,0,0,0,0,0]~)),H=mathnf(rel),ix=abs(matdet(H)));
 check(ix==9,"complete norm image by independent Herbrand index9");
 print("{\"type\":\"norm_index_check\",\"index\":",ix,"}");
 my(rows=List(),labels=List(),rk=0);
 forprime(p=7,2000,
  if(p==53,next);
  my(PP=idealprimedec(B,p));
  for(i=1,#PP,
   my(pr=nfmodprinit(B,PP[i],'t),zz=nfmodpr(B,xi^3,pr),qq=p^PP[i][4]);
   my(row=vector(9,j,
    my(rr=nfmodpr(B,U[j],pr)^((qq-1)/3));
    if(rr==1,0,if(rr==zz,1,if(rr==zz^2,2,error("residual cube root"))))
   ));
   my(new=concat(Vec(rows),[row]),nr=matrank(Mod(matrix(#new,9,r,c,new[r][c]),3)));
   if(nr>rk,listput(rows,row);listput(labels,[p,i,PP[i][4]]);rk=nr);
   if(rk==9,break(2));
  );
 );
 check(rk==9,"all ordinary units and torsion independently3-saturated");
 my(RM=matrix(9,9,i,j,rows[i][j]),RI=lift(Mod(RM,3)^-1));
 check(lift(Mod(RM*RI,3))==matid(9),"literal residual inverse");
 print("{\"type\":\"actual_horizontal_norm\",\"upper_scope\":\"actual elements only; no upper class certification used\",\"candidate_class_cyclic_unused\":",B.cyc,",\"lower_basis\":\"zeta,fu1,fu2,q_PAR1,q_PAR2,q_PAR3,alpha\",\"norm_matrix\":",jmat(NM),",\"image_HNF\":",jmat(H),",\"image_index\":",ix,",\"tensor_unit_columns\":",vector(#U,j,vector(18,i,Str(UC[i,j]))),"}");
 print("{\"type\":\"unit_saturation\",\"prime_labels_p_index_degree\":",Vec(labels),",\"matrix\":",jmat(RM),",\"inverse_mod3\":",jmat(RI),",\"determinant\":",matdet(RM),"}");
 writebin("e53_horizontal_norm_matrix.bin",[D,MD,UC,NM,H,RM,RI,Vec(labels),norms]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
