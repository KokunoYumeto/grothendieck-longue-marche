\\ Exact local input and class-number checks for B.27.
\\ Run with the independently built PARI/GP 2.19.1.
must(ok,msg)=if(!ok,error(msg));
print("PARI version: ",version());
E=ellinit([0,0,1,0,-7]);
z=elllocalred(E,3);
must(E.disc==-3^9,"wrong cubic discriminant");
must(z==[3,-4,[1,0,0,0],3],"unexpected cubic local reduction");
print("E27: discriminant=",E.disc,"; elllocalred at 3=",z);
print("Kodaira IV*, minimal model, Tamagawa number 3: PASS");
cnt=1;
for(X=0,2,for(Y=0,2,if((Y^2+Y-X^3+7)%3==0 && ((2*Y+1)%3!=0 || (3*X^2)%3!=0),cnt++)));
must(cnt==3,"wrong nonsingular additive reduction size");
print("Nonsingular reduction group has ",cnt," points; formal and component factors are 3-primary: PASS");
checkfield(ell)={
  my(P=polcyclo(ell),B=bnfinit(P,1),c=bnfcertify(B),D=idealprimedec(B,ell));
  must(c==1 && B.no==1 && #D==1 && D[1].e==ell-1 && D[1].f==1,"cyclotomic class/local certificate failed");
  print("K=Q(zeta",ell,"): h=1, certificate=1, unique coefficient prime with (e,f)=(",D[1].e,",",D[1].f,"): PASS")
};
checkfield(3);
checkfield(5);
print("All local/group arithmetic inputs passed; the general pro-ell proof is B.27.");
quit;
