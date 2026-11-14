\\ Exact ideal/class obstruction of the retained zeta norm witness.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
check(b,s)=if(!b,error(s));
red(v,d)=vector(#d,i,lift(Mod(v[i],d[i])))~;
run()={
  my(dat=read("research_e97/code/e_cyclic_norm_switch.bin"),L=dat[22],w=dat[23],fac=dat[24],t=Mod(x,L.pol),z=t^9/17,s=nfalgtobasis(L,z*t));
  my(lo=read("research_e86/code/e_stable_lower_genus.bin"),B=lo[1],F=B.nf,Ray=lo[2],U=lo[5][1],ds=lo[6],rl=read("research_e86/code/e_stable_class_coordinates.bin")[2],CF=rl[4][1]*rl[2]^-1,cd=vector(#rl[4][3],i,rl[4][3][i,i]));
  my(done=Map(),D=matid(18),arts=vector(#ds,i,0)~,records=List());
  for(j=1,matsize(fac)[1],
    my(P=fac[j,1],I=idealhnf(L,P),key=Str(I));
    if(mapisdefined(done,key),next);
    my(I1=idealhnf(L,nfgaloisapply(L,s,I)),I2=idealhnf(L,nfgaloisapply(L,s,I1)),orb=[I,I1,I2],v=vector(3,i,sum(jj=1,matsize(fac)[1],if(idealhnf(L,fac[jj,1])==orb[i],fac[jj,2],0))));
    check(I!=I1 && I!=I2 && I1!=I2,"each nonzero support orbit is split");
    check(idealhnf(L,nfgaloisapply(L,s,I2))==I && sum(i=1,3,v[i])==0,"cyclic support and norm zero");
    for(i=1,3,mapput(done,Str(orb[i]),1));
    my(dc=[0,-v[2],v[1]],DD=idealmul(L,idealpow(L,I1,dc[2]),idealpow(L,I2,dc[3])));
    D=idealmul(L,D,DD);
    my(mp=nfmodprinit(L,P,'u),rr=nfmodpr(L,t,mp));
    check(P[4]==1,"degree-one support prime");
    my(root=lift(rr.pol),pl=P[1],lower=idealhnf(F,pl,x-lift(Mod(root,pl)^3)),av=red(U*bnrisprincipal(Ray,lower,0),ds),total=sum(i=1,3,dc[i]));
    check(idealnorm(F,lower)==pl,"actual contracted prime");
    arts+=total*av;
    listput(records,[pl,root,v,dc,Vec(av),total,idealhnf(F,lower)]);
    print("ORBIT ",[pl,root,v,dc,Vec(av),total]);
  );
  check(idealdiv(L,nfgaloisapply(L,s,D),D)==idealhnf(L,w),"literal Hilbert90 divisor equation");
  my(k=#cd,a=red(arts,ds),small=vector(k,i,a[i])~,cl=red(CF*small,cd));
  check(denominator(CF*small)==1,"relative class-kernel coordinates");
  print("GENUS_CLASS ",a," CLASS_CYCLIC ",cd," IDEAL_CLASS ",cl);
  my(qq=red(CF*vector(k,i,lo[7][i,1])~,cd),Dmod=concat(matdiagonal(cd),qq),H=mathnf(Dmod),defect=H^-1*cl);
  print("RAMIFIED_SUBGROUP_GENERATOR ",qq," DEFECT_LATTICE ",H," DEFECT_COORDINATE ",defect," ZERO ",denominator(defect)==1);
  writebin("research_e97/code/e_zeta_unit_defect.bin",[L,w,s,D,Vec(records),a,CF,cd,cl,qq,H,defect]);
  print("DONE_EXACT_UNIT_NORM_DEFECT");
};
run();
quit;
