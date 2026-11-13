default(parisize,128000000);
default(parisizemax,1000000000);
setrand(1772);
run()={
  forprime(p=2,97,
    if(p==3 || p==17,next);
    my(g=znprimroot(p),b=znlog(Mod(17,p),g),logs,q);
    if(p%3==1,
      q=p;
      my(z=g^((p-1)/3));
      logs=[znlog(Mod(17,p)*z,g),znlog(Mod(17,p)*z^2,g)];
      if(g^logs[1]!=Mod(17,p)*z || g^logs[2]!=Mod(17,p)*z^2,error("split logarithm")),
      q=p^2;
      my(F=ffgen(ffinit(p,2,'t),'t),gg=ffprimroot(F),z=gg^((q-1)/3));
      logs=[fflog(17*z,gg)];
      if(gg^logs[1]!=17*z,error("inert logarithm"));
    );
    for(d=1,3,
      my(m=3^d,A=factormod(x^m-17,p),B=factormod(x^(2*m)+17*x^m+289,p));
      my(af=vecsort(vector(matsize(A)[1],j,poldegree(A[j,1]))));
      my(bf=vecsort(vector(matsize(B)[1],j,poldegree(B[j,1]))));
      if(vecsum(af)!=m || vecsum(bf)!=2*m,error("degree sum"));
      print("DATA ",[p,d,b,q,logs,af,bf]);
    );
  );
};
run();
quit;
