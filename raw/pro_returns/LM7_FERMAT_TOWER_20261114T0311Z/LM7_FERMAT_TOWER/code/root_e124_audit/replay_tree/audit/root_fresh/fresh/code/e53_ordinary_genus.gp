\\ Actual ordinary genus presentation for L3/L2, with every lattice map.
default(parisize,64000000);
check(a,s)=if(!a,error(s));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
{
 my(D=read("../inputs/e53_ordinary_genus_input.txt"),R=matrix(5,5));
 R[1,1]=3;R[2,2]=3;
 for(i=1,3,R[1,i+2]=D[2][i][1];R[2,i+2]=D[2][i][2];R[i+2,i+2]=D[2][i][3]);
 my(phi=concat([1,1],D[1]),K=matid(5));
 K[1,1]=3;for(i=2,5,K[1,i]=-phi[i]);
 my(KR=K^-1*R,S=matsnf(KR,1),sg=vector(5,i,S[3][i,i]));
 check(denominator(KR)==1 && S[1]*KR*S[2]==S[3],"restriction kernel and full Smith maps");
 my(Q=Col(concat(-D[4],D[3])),qq=S[1]*K^-1*Q,q=Col(vector(5,i,lift(Mod(qq[i],sg[i])))));
 my(N=matrix(3,5,i,j,(K*S[1]^-1)[i+2,j]),mods=[9,9,3],Nm=matrix(3,5,i,j,lift(Mod(N[i,j],mods[i]))));
 check(lift(Mod(phi*R,3))==vector(5),"all principal relations restrict to zero");
 check(denominator(K^-1*Q)==1,"actual three-prime norm-uniformizer class in restriction kernel");
 print("{\"type\":\"ordinary_L3_genus\",\"idele_relations\":",jmat(R),",\"restriction\":",phi,",\"kernel_lattice\":",jmat(K),",\"kernel_relations\":",jmat(KR),",\"smith_left\":",jmat(S[1]),",\"smith_right\":",jmat(S[2]),",\"smith_diagonal\":",sg,",\"three_prime_raw\":",Vec(Q),",\"three_prime_smith\":",Vec(q),",\"actual_norm_full\":",jmat(Nm),",\"order\":",abs(matdet(KR)),"}");
 writebin("e53_ordinary_genus.bin",[R,phi,K,KR,S,Q,q,Nm]);
 print("{\"status\":\"PASS\"}");
}
quit;
