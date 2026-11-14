\\ Literal S-split genus field, without an upper BNF.
default(parisize,128000000);default(parisizemax,1000000000);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
{
 my(D=read("e53_horizontal_base.bin"),F=D[1],L=D[4],xi=Mod(x,F.pol),z=xi^3,theta=xi+xi^-1);
 my(R=bnfinit(x^3-3*x+1,1),rc=bnfcertify(R),RP=idealprimedec(R,53));
 check(rc==1 && R.no==1,"fully certified real cyclotomic base");
 my(q=bnfisprincipal(R,RP[1],1),pi=nfbasistoalg(R,q[2]));
 if(nfeltnorm(R,pi)==-53,pi=-pi);
 check(nfeltnorm(R,pi)==53,"literal norm 53");
 my(base=Mod(subst(lift(pi),x,theta),F.pol),Q3=idealprimedec(F,3)[1],found=List());
 for(i=0,2,for(j=0,2,
  my(u=base*subst(lift(R.fu[1]^i*R.fu[2]^j),x,theta));
  if(nfislocalpower(F,Q3,u,3),listput(found,[i,j,u]));
 ));
 check(#found>0,"actual local cube correction exists");
 my(pi0=found[1][3],pis=vector(3,i,subst(lift(pi0),x,xi^(4^(i-1)))),sg=1);
 if(prod(i=1,3,pis[i])==-53,pi0=-pi0;pis=-pis;sg=-1);
 check(prod(i=1,3,pis[i])==53,"exact cyclic product");
 my(Q=idealprimedec(F,53),vals=matrix(3,3,i,j,idealval(F,pis[j],Q[i])));
 check(abs(matdet(vals))==1,"independent prime valuations");
 my(local=matrix(3,3));
 for(i=1,3,for(j=1,3,
  my(pr=nfmodprinit(F,Q[i],'t));
  local[i,j]=(nfmodpr(F,pis[j]/53^vals[i,j],pr)^((53^2-1)/3)==1);
  check(local[i,j]==1,"local extension equals root53");
 ));
 print("{\"type\":\"actual_genus_radicals\",\"real_base_flag0\":",rc,",\"real_base_polynomial\":\"",R.pol,"\",\"real_prime_generator\":",cf(pi,3),",\"real_unit_correction\":[",found[1][1],",",found[1][2],"],\"sign_correction\":",sg,",\"radicals\":",vector(3,i,cf(pis[i],6)),",\"valuation_matrix\":",vector(3,i,Vec(vals[i,])),",\"local_cube_at_three\":",vector(3,i,nfislocalpower(F,Q3,pis[i],3)),",\"local_cube_units_at_53\":",vector(3,i,Vec(local[i,])),"}");
 my(records=List(),vecs=List());
 forprime(p=7,300,
  if(p%9!=1,next);
  my(roots=polrootsmod(x^3-53,p));if(#roots==0,next);
  my(P=idealprimedec(F,p));
  for(ii=1,#P,
   if(P[ii][4]!=1,next);
   my(pr=nfmodprinit(F,P[ii],'t),rr=-1,aa=lift(roots[1]));
   for(r=0,p-1,if(nfmodpr(F,xi,pr)==r,rr=r;break));
   check(rr>=0,"literal degree-one residue");
   my(bb=lift(Mod(aa*rr,p)));
   my(Js=idealprimedec(L,p),JJ=0);
   for(jj=1,#Js,if(Js[jj][4]==1 && idealval(L,Mod(x-bb,L.pol),Js[jj])>0,JJ=Js[jj]));
   check(JJ!=0,"literal contraction prime found");
   my(v=vector(3,j,
     my(r=nfmodpr(F,pis[j],pr)^((p-1)/3),zz=nfmodpr(F,z,pr));
     if(r==1,0,if(r==zz,1,if(r==zz^2,2,error("Kummer residue"))))
   ));
   check(sum(j=1,3,v[j])%3==0,"root53 prime sum");
   my(cl=Vec(bnfisprincipal(L,JJ,0)),scl=vector(2,j,lift(Mod(cl[j],3))));
   if(v!=[0,0,0],
    listput(records,[p,rr,aa,bb,v,cl,scl]);listput(vecs,v);
    if(matrank(Mod(matrix(#vecs,3,i,j,vecs[i][j]),3))==2,break(2));
   );
  );
 );
 check(#records>=2 && matrank(Mod(matrix(#vecs,3,i,j,vecs[i][j]),3))==2,"two actual genus basis primes");
 print("{\"type\":\"actual_prime_norms\",\"records_p_xi_alpha_beta_genus_class_Sclass\":",Vec(records),"}");
 writebin("e53_genus_kummer.bin",[D,R,pis,vals,Vec(records)]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
