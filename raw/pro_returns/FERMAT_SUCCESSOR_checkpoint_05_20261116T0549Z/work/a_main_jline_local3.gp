comp=polcompositum(x^3-3,x^2+x+1,1)[1];
pol=comp[1]; bb=comp[2]; zz=comp[3];
nf=nfinit(pol); pr=idealprimedec(nf,3)[1];
E=ellinit([0,0,1,0,-1],nf); P=[1,0];
g(Q)={if(#Q==1,return(1));return((bb^2*zz^2*Q[1]-Q[2]-2)/(bb^2*Q[1]-Q[2]-2))};
print("field=",pol," b=",bb," zeta=",zz," e3=",pr.e);
print("v(zeta+2)=",nfeltval(nf,zz+2,pr));
for(n=1,12,Q=ellmul(E,P,n);T=[bb*zz,1];QT=elladd(E,Q,T);h=g(QT)/g(Q);print("n=",n," val_g=",nfeltval(nf,g(Q),pr)," val_ratio=",nfeltval(nf,h,pr)," local_square=",nfislocalpower(nf,pr,h,2)));
