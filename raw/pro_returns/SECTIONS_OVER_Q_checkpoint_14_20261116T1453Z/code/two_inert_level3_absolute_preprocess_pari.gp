\\ Exact model preprocessing for the level-three balanced ideal class.
\\ v=rho3^8/d^7 gives v^27=3^8*d^3 and t=3*d/v^3.
\\ The original polynomial discriminant is supported on3,11,59.
default(parisizemax,1500000000);
default(parisize,256000000);
default(realprecision,100);setrand(3);
d=649;P=x^27-3^8*d^3;
print("ORIGINAL POLYNOMIAL ",P);
N=nfinit([P,[3,11,59]]);
print("NF READY DISC ",factor(N.disc));
R=polredbest(N,1);
print("REDUCED POLYNOMIAL ",R[1]);
print("EXACT ROOT MAP ",R[2]);
print("ROOT MAP CHECK ",subst(P,x,R[2]));
write("/tmp/birational-pari-runtime/level3_reduced_model.gp",Str("reduced_poly=",R[1],";root_v=",R[2],";"));
quit;
