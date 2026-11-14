\\ Exact field, eigenunit and finite Frobenius witness for E.118.
\\ Run from a fresh directory; this program needs no binary input.
default(parisize,128000000);
default(parisizemax,1000000000);
check(c,m)=if(!c,error(m));
cf(a,n)=vector(n,j,Str(polcoef(lift(a),j-1)));
{
 my(P=x^8+2*x^4+5,b0=Mod(x,P),i0=(b0^4+1)/2);
 check(polisirreducible(P) && i0^2==-1,"actual degree-eight field");
 my(U=(x^7-4*x^6-7*x^5-2*x^4+9*x^3+2*x^2-11*x-16)/4,
     W=(3*x^7-3*x^6+3*x^5-x^4+5*x^3-x^2-3*x+9)/4);
 my(u=Mod(U,P),w=Mod(W,P),mu=minpoly(u),mw=minpoly(w));
 check(pollead(mu)==1 && denominator(mu)==1 && abs(polcoef(mu,0))==1,"u is an algebraic unit");
 check(pollead(mw)==1 && denominator(mw)==1 && abs(polcoef(mw,0))==1,"w is an algebraic unit");
 check(subst(U,x,i0*b0)==u^3*w^5,"literal Kummer character identity");
 check(u*Mod(1/u,P)==1,"literal unit inverse");
 print("{\"type\":\"eigenunit\",\"field\":\"",P,"\",\"unit_coefficients\":",cf(u,8),",\"correction_coefficients\":",cf(w,8),",\"unit_minpoly\":\"",mu,"\",\"correction_minpoly\":\"",mw,"\",\"inverse_coefficients\":",cf(1/u,8),",\"tau_character\":3,\"identity_verified\":true}");

 my(CC=polcompositum(P,x^4-5,1));
 check(#CC==1 && poldegree(CC[1][1])==32,"actual full division compositum");
 my(C=CC[1],R=C[1],b=C[2],t=C[3],a=t/b,ii=(b^4+1)/2,theta=Mod(x,R));
 check(ii^2==-1 && b^4==-1+2*ii && a^4==-1-2*ii,"literal field inclusions");
 check(theta==a*b+C[4]*b,"literal inverse primitive-element map");
 my(yp=(1+ii)/(2-ii)*a,ym=(1-ii)/(2+ii)*b);
 my(PP=[yp^2/((4+2*ii)/5),yp],PM=[ym^2/((4-2*ii)/5),ym],EC=ellinit([0,0,0,1,0]));
 check(ellisoncurve(EC,PP) && ellisoncurve(EC,PM),"actual torsion curve equations");
 check(ellmul(EC,PP,5)==[0] && ellmul(EC,PM,5)==[0],"actual fifth torsion");
 check(ellmul(EC,PP,2)==[-PP[1],ii*PP[2]],"first eigenline");
 check(ellmul(EC,PM,2)==[-PM[1],-ii*PM[2]],"second eigenline");
 my(ta=ii*t+C[4]*b,tb=ii*theta,cc=t+C[4]*a,images=List());
 check(subst(lift(b),x,ta)==b && subst(lift(a),x,ta)==ii*a,"tau_a field map");
 check(subst(lift(b),x,tb)==ii*b && subst(lift(a),x,tb)==a,"tau_b field map");
 check(subst(lift(b),x,cc)==a && subst(lift(a),x,cc)==b && subst(lift(ii),x,cc)==-ii,"actual conjugation");
 check(subst(lift(ta),x,cc)==subst(lift(cc),x,subst(lift(tb),x,subst(lift(tb),x,tb))),"c tau_a equals tau_b inverse c");
 for(r=0,3,for(s=0,3,
   my(v=ii^(r+s)*t+C[4]*ii^s*b);
   check(subst(R,x,v)==0,"every diagonal embedding");listput(images,v);
   v=subst(lift(v),x,cc);check(subst(R,x,v)==0,"every conjugate embedding");listput(images,v);
 ));
 check(#Set(Vec(images))==32,"all32 literal embeddings are distinct");
 my(gens=[ta,tb,cc],wanted=[[ellmul(EC,PP,2),PM],[PP,ellmul(EC,PM,3)],[PM,PP]]);
 for(j=1,3,
   check(vector(2,k,subst(lift(PP[k]),x,gens[j]))==wanted[j][1],"actual first point action");
   check(vector(2,k,subst(lift(PM[k]),x,gens[j]))==wanted[j][2],"actual second point action");
 );
 print("{\"type\":\"division_field\",\"degree\":32,\"polynomial\":\"",R,"\",\"primitive_constant\":",C[4],",\"a_coefficients\":",cf(a,32),",\"b_coefficients\":",cf(b,32),",\"i_coefficients\":",cf(ii,32),",\"generator_images\":",vector(3,j,cf(gens[j],32)),",\"residual_matrices\":[[[2,0],[0,1]],[[1,0],[0,3]],[[0,1],[1,0]]],\"all_embeddings_count\":32,\"all_point_actions_verified\":true}");

 my(p=3121,ip=Mod(79,p),ap=Mod(1285,p),bp=Mod(339,p));
 check(isprime(p) && p%40==1 && valuation(p-1,5)==1,"prime and tame precision");
 check(ip^2==-1 && ap^4==-1-2*ip && bp^4==-1+2*ip,"actual degree-one specialization");
 check(Mod(2,p)^((p-1)/5)==1,"two is a fifth power");
 my(root2=polrootsmod(x^5-2,p)[1],root8=znprimroot(p)^((p-1)/8));
 check(root2^5==2 && root8^4==-1,"literal fifth and eighth roots");
 my(up=subst(U,x,bp),ucp=subst(U,x,ap),EP=ellinit([0,0,0,1,0],p),card=ellcard(EP));
 yp=(1+ip)/(2-ip)*ap;ym=(1-ip)/(2+ip)*bp;
 PP=[yp^2/((4+2*ip)/5),yp];PM=[ym^2/((4-2*ip)/5),ym];
 check(ellisoncurve(EP,PP) && ellisoncurve(EP,PM),"specialized curve equations");
 check(ellmul(EP,PP,5)==[0] && ellmul(EP,PM,5)==[0],"specialized fifth torsion");
 my(eta=ellweilpairing(EP,PP,PM,5),z=up^((p-1)/5),zc=ucp^((p-1)/5));
 check(eta!=1 && eta^5==1,"primitive specialized Weil pairing");
 my(e=znlog(z,eta,5),ec=znlog(zc,eta,5));
 check(card==3200 && valuation(card,5)==2 && e==3 && ec==4,"exact Frobenius and local order witness");
 print("{\"type\":\"numerical_prime\",\"p\":",p,",\"i_a_b\":[79,1285,339],\"fifth_root_of_two\":",lift(root2),",\"primitive_eighth_root\":",lift(root8),",\"unit_values\":[",lift(up),",",lift(ucp),"],\"fifth_residues\":[",lift(z),",",lift(zc),"],\"Weil_pairing\":",lift(eta),",\"Kummer_logarithms\":[",e,",",ec,"],\"global_cocycle_coordinates\":[",e,",",lift(Mod(-ec,5)),"],\"points\":",[lift(PP),lift(PM)],",\"elliptic_order\":",card,",\"exact_local_Kummer_order\":5}");
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit(0);
