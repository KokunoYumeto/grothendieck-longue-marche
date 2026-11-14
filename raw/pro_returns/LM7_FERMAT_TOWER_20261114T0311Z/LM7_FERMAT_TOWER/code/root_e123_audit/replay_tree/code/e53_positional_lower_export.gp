\\ Export literal lower ideal/basis data, without an upper BNF operation.
default(parisize,128000000);
jmat(A)=vector(matsize(A)[1],i,Vec(A[i,]));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
{
 my(D=read("../inputs/e119_positional_genus_transition.bin"),L=D[1][4],S=D[1][5],G=D[2]);
 print("{\"type\":\"literal_lower_data\",\"polynomial\":\"",L.pol,"\",\"discriminant\":\"",L.disc,"\",\"integral_basis\":",vector(6,i,cf(Mod(L.zk[i],L.pol),6)),",\"outside_S_class_generators\":",vector(2,i,jmat(idealhnf(L,G[i]))),",\"S_primes\":",vector(2,i,jmat(idealhnf(L,S[i]))),",\"kernel_lattice\":",jmat(D[10]),",\"kernel_Smith_left\":",jmat(D[12][1]),",\"relation_HNF\":",jmat(D[8]),"}");
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
