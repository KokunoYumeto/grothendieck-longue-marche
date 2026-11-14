\\ Exact cyclic character subfields of the two fifth-division fields.
\\ Their complete class groups are certified with default bnfcertify flag0.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,96);
check(c,m)={if(!c,print("FAILED: ",m);quit(1));};
vectors=[[1,0],[0,1],[1,1],[1,2],[1,3],[2,1]];
allcert=List();
{
for(case=1,2,
  sg=if(case==1,-1,1);
  pp=x^8-2*sg*x^4+5;
  cc=polcompositum(pp,x^4-5,1);
  check(#cc==1 && poldegree(cc[1][1])==32,"degree32 compositum");
  C=cc[1]; R=C[1]; aa=C[2]; tt=C[3]; bb=tt/aa;
  ii=(aa^4/sg-1)/2;
  check(ii^2==-1 && aa^4==sg*(1+2*ii) && bb^4==sg*(1-2*ii),"literal radicals");
  check(Mod(x,R)==tt+C[4]*aa,"primitive compositum map");
  if(case==1,
    yy=(1+ii)/(2-ii)*aa;
    zz=(1-ii)/(2+ii)*bb;
    xx=yy^2/((4+2*ii)/5);
    ww=zz^2/((4-2*ii)/5);
    EC=ellinit([0,0,0,1,0]);
  ,
    yy=4/(2-ii)*aa;
    zz=4/(2+ii)*bb;
    xx=yy^2/(4*(4+2*ii)/5);
    ww=zz^2/(4*(4-2*ii)/5);
    EC=ellinit([0,0,0,4,0]);
  );
  PP=[xx,yy]; PM=[ww,zz];
  check(ellisoncurve(EC,PP) && ellisoncurve(EC,PM),"actual curve equations");
  check(ellmul(EC,PP,5)==[0] && ellmul(EC,PM,5)==[0],"actual fifth torsion");
  check(ellmul(EC,PP,2)==[-xx,ii*yy],"first CM eigenspace");
  check(ellmul(EC,PM,2)==[-ww,-ii*zz],"second CM eigenspace");
  loc=elllocalred(EC,2);
  print("{\"stage\":\"division_field\",\"case\":",case,",\"curve_a4\":",if(case==1,1,4),",\"degree\":32,\"point_maps_verified\":true,\"local2\":\"",loc,"\",\"point_count_at5\":",ellcard(ellinit([0,0,0,if(case==1,1,4),0],5)),"}");
  ii_gauss=Mod(y,y^2+1);
  for(j=1,#vectors,
    uv=vectors[j]; u=uv[1]; v=uv[2];
    rad=(sg*(1+2*ii_gauss))^u*(sg*(1-2*ii_gauss))^v;
    re=polcoef(lift(rad),0,y); im=polcoef(lift(rad),1,y);
    mm=aa^u*bb^v;
    check(mm^4==re+im*ii,"monomial fourth power");
    if(im!=0,
      SS=x^8-2*re*x^4+re^2+im^2;
      subtheta=mm;
      sub_i=(Mod(x,SS)^4-re)/im;
    ,
      cs=polcompositum(x^4-re,x^2+1,1);
      check(#cs==1 && poldegree(cs[1][1])==8,"real-radical subfield degree");
      SS=cs[1][1];
      subtheta=ii+cs[1][4]*mm;
      sub_i=cs[1][3];
      check(subst(lift(cs[1][2]),x,subtheta)==mm,"real radical embedding");
    );
    check(polisirreducible(SS),"character subfield irreducibility");
    check(poldegree(SS)==8 && subst(SS,x,subtheta)==0,"actual degree8 inclusion");
    check(sub_i^2==-1 && subst(lift(sub_i),x,subtheta)==ii,"actual inclusion of K");
    BB=bnfinit(SS,1);
    ce=bnfcertify(BB);
    check(ce==1,"unconditional subfield class certification");
    check(BB.no%5!=0,"five-primary class vanishing");
    pr2=idealprimedec(BB,2); pr5=idealprimedec(BB,5);
    print("{\"stage\":\"character_subfield\",\"case\":",case,",\"vector\":",uv,",\"polynomial\":\"",SS,"\",\"radicand_gaussian\":",[re,im],",\"class_number\":",BB.no,",\"class_invariants\":",BB.cyc,",\"certify_flag\":0,\"certify_return\":",ce,",\"discriminant\":\"",BB.disc,"\",\"prime2_ef\":",vector(#pr2,k,[pr2[k].e,pr2[k].f]),",\"prime5_ef\":",vector(#pr5,k,[pr5[k].e,pr5[k].f]),"}");
    listput(allcert,[case,uv,BB,subtheta,sub_i,ce,C,ii,aa,bb,PP,PM,loc]);
  );
);
}
check(#allcert==12,"complete twelve-field count");
writebin("research_e112/code/quartic_five_character_fields.bin",Vec(allcert));
print("{\"stage\":\"completion\",\"status\":\"PASS\",\"certified_character_fields\":",#allcert,"}");
quit(0);
