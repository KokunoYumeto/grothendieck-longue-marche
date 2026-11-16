search_torsion()={
plist=[5,7,11,13,17,19];
for(ii=1,#plist,
 pp=plist[ii]; found=0;
 for(tt=1,100,
  kk=3*pp*tt; qq=kk^2-kk+1; if(!isprime(qq),next);
  EE=ellinit([0,0,1,0,-1],qq); GG=ellgroup(EE,,1);
  if(#GG[2]<2 || GG[2][2]%(3*pp),next);
  br=polrootsmod(x^3-3,qq); zr=polrootsmod(x^2+x+1,qq);
  if(#br!=3 || #zr!=2,error("full3 inconsistency"));
  bb=br[1];zz=zr[1];
  S1=ellmul(EE,GG[3][1],GG[2][1]/pp);
  S2=ellmul(EE,GG[3][2],GG[2][2]/pp);
  for(aa=0,pp-1,for(cc=0,pp-1,
   if(aa==0 && cc==0,next);
   SS=elladd(EE,ellmul(EE,S1,aa),ellmul(EE,S2,cc));
   if(#SS==1,next);
   val=(bb^2*zz^2*SS[1]-SS[2]-2)/(bb^2*SS[1]-SS[2]-2);
   if(kronecker(lift(val),qq)==-1,
    print("p=",pp," q=",qq," group=",GG[2]," b=",lift(bb)," zeta=",lift(zz)," S=",lift(SS)," gS=",lift(val)," orderS=",ellorder(EE,SS));found=1;break(2)
   )
  ));
  if(found,break)
 );
 if(!found,print("NO_WITNESS_IN_SEARCH p=",pp))
);

};
search_torsion();
