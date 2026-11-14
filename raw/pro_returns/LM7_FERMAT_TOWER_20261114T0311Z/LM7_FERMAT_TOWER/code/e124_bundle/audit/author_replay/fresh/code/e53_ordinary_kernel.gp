\\ Exact valuation kernel of already verified actual units; no upper BNF.
default(parisize,128000000);default(parisizemax,1000000000);
check(a,s)=if(!a,error(s));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
{
 my(D=read("../inputs/e119_lower.bin")[1],Z=read("../inputs/e53_ordinary_kernel_input.txt"));
 my(B=D[1],Q=D[5],T=D[6],U=D[7],lab=D[8],V=matrix(6,15));
 for(j=1,15,for(i=1,3,V[i,j]=idealval(B,U[j],Q[lab[i]]);V[i+3,j]=idealval(B,U[j],T[i])));
 my(VC=matrix(6,30));
 for(a=1,3,for(i=1,3,VC[i,24+a]=3;VC[i+3,27+a]=1));
 my(V45=concat(3*V,VC),EX=Mat(vector(22,j,Col(Z[1][j]))),RV=V45*EX/3);
 check(denominator(RV)==1,"every actual root has integral six-prime valuations");
 my(C=Mat(vector(22,j,Col(vector(6,i,Z[2][i][j])))),ALLC=concat(D[10],C),ALLV=concat(3*V,RV));
 my(K=matkerint(ALLV),OC=ALLC*K,PO=matindexrank(Mod(OC,3)),A=vector(6,i,1));
 check(ALLV*K==0,"literal ordinary-unit valuation kernel");
 check(lift(Mod(A*ALLC,3))==vector(37),"product formula for all37 actual units");
 my(HS=vector(6,i,if(i>3,1,0))*OC);
 print("{\"type\":\"ordinary_character_kernel\",\"lower_valuations\":",jmat(V),",\"root_valuations\":",jmat(RV),",\"all_valuations\":",jmat(ALLV),",\"ordinary_kernel\":",jmat(K),",\"ordinary_characters\":",jmat(lift(Mod(OC,3))),",\"ordinary_character_rank\":",matrank(Mod(OC,3)),",\"independent_columns\":",Vec(PO[2]),",\"horizontal_character_row\":",lift(Mod(HS,3)),",\"horizontal_rank\":",matrank(Mod(Mat(HS),3)),"}");
 writebin("e53_ordinary_kernel.bin",[V,RV,ALLV,K,OC,PO,HS]);
 print("{\"status\":\"PASS\",\"scope\":\"actual verified subgroup; no ordinary-unit completeness assertion\"}");
}
quit;
