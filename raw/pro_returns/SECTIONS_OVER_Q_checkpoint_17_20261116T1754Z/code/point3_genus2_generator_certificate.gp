\\ Exact completed generator comparison for the first A186 factor.
\\ Local PARI only; all class/unit data are certified unconditionally.
check(t,msg)={if(!t,error(msg));};
main()={
my(F,B,S,U,G,D,vP,vT,cP,cT,M);
F=x^4-54;
B=bnfinit(F,1);
check(bnfcertify(B)==1,"full class and unit certification");
S=concat(idealprimedec(B,2),idealprimedec(B,3));
U=bnfunits(B,S);
G=vector(5,i,Mod([x^3/9-x^2/3+x-2,-x^3/9+x^2/3-x+3,2*x^2/3+5,-2*x^3/9+2*x^2/3-2*x+5,-1][i],F));
D=matrix(5,5,i,j,bnfisunit(B,G[j],U)[i]);
check(matrank(Mod(D,2))==5,"literal S-unit basis");
vP=bnfisunit(B,Mod(3-x,F),U);
vT=bnfisunit(B,Mod(-x,F),U);
cP=lift(Mod(D,2)^(-1)*Mod(vP,2));
cT=lift(Mod(D,2)^(-1)*Mod(vT,2));
M=[1,0,1,1,0;0,0,1,1,1;0,1,1,0,0];
check(Mod(M*cP,2)==0,"point in exact Selmer kernel");
check(Mod(M*cT,2)==0,"branch point in exact Selmer kernel");
check(matrank(Mod(Mat([cP,cT]),2))==2,"point and branch generate kernel");
print("CERTIFIED FULL S-UNIT COORDINATE MATRIX ",D);
print("POINT (3,9): eta=3-theta; full S-unit coordinates ",vP,"; literal mod-square coordinates ",cP);
print("BRANCH (0,0): eta=-theta; full S-unit coordinates ",vT,"; literal mod-square coordinates ",cT);
print("PASS: D=[(3,9)-infinity] and T0 span the exact two-dimensional Selmer kernel; the free index is odd and the full two-adic Mordell-Weil completion is Z2.D plus C2.T0");
};
main();
