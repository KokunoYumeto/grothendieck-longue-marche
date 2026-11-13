\\ Search the literal cubic norm form with all three coefficients in K=Q(zeta3).
\\ Every retained hit is verified as an actual integral L2 unit and exact norm.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
check(b,s)=if(!b,error(s));
run()={
 my(B=read("research_e86/code/e_stable_lower_genus.bin")[1],b=Mod(x,B.pol),z=b^3/17,K=nfinit(y^2+y+1),zz=Mod(y,K.pol),Z=varhigher("Z",x));
 my(L=read("research_norm_index/code/prime3_field2.bin")[1],bb=Mod(x,L.pol),zl=bb^9/17,aut=nfalgtobasis(L,zl*bb),targets=0,cubepairs=0,hits=List());
 for(a=-4,4,for(c=-4,4,
   if((a-c)%3 || a%3==0,next);
   for(t=0,2,
     targets++;
     my(n=B.fu[1]^a*B.fu[2]^c*z^t,nn=lift(n),co=vector(3,i,polcoef(nn,i-1)+17*zz*polcoef(nn,i+2)));
     my(rr=nfroots(K,Z^3-co[1]),pp=nfroots(K,Z^3-co[3]));
     if(!#rr || !#pp,next);
     cubepairs++;
     for(ir=1,#rr,for(ip=1,#pp,
       my(r=rr[ir],p=pp[ip],qq=nfroots(K,Z^3-3*p*r*Z-co[2]));
       for(iq=1,#qq,
         my(q=qq[iq],u=subst(lift(r),y,zl)+subst(lift(q),y,zl)*bb+subst(lift(p),y,zl)*bb^2,uv=nfalgtobasis(L,u));
         check(denominator(uv)==1 && idealhnf(L,u)==matid(18),"actual integral upper unit");
         my(su=nfgaloisapply(L,aut,uv),s2u=nfgaloisapply(L,aut,su),nu=nfeltmul(L,nfeltmul(L,uv,su),s2u),expected=nfalgtobasis(L,subst(nn,x,bb^3)));
         check(nu==expected,"literal relative norm identity");
         print("UNIT_NORM_HIT ",a," ",c," ",t," COEFFICIENTS ",[r,q,p]," UPPER ",lift(u));
         listput(hits,[a,c,t,r,q,p,u]);
       );
     ));
   );
 ));
 print("EXACT_CUBIC_FORM_COUNTS ",[targets,cubepairs,#hits]);
 writebin("research_h_after_e97/relative_unit_cubic_form.bin",Vec(hits));
 print("DONE_EXACT_CUBIC_FORM_SEARCH; no inference from missing hits");
};
run();
quit;
