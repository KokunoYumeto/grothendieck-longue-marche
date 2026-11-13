default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(1765);
check(a,s)=if(!a,error(s));
jpoly(v)=Str(vector(poldegree(lift(v))+1,i,Str(polcoef(lift(v),i-1))));
run()={
  my(B=bnfinit(y^3-17,1),R=rnfinit(B,x^3-y),C=bnfinit(x^9-17,1));
  check(bnfcertify(B)==1 && bnfcertify(C)==1,"unconditional fields");
  print("{\"type\":\"fields\",\"base_class\":",B.cyc,",\"source_class\":",C.cyc,",\"base_unit\":",jpoly(B.fu[1]),",\"source_units\":[",concat(vector(#C.fu,i,concat([if(i>1,",",""),jpoly(C.fu[i])]))),"]}");
  my(row=vector(#C.fu),signs=vector(#C.fu));
  for(i=1,#C.fu,
    my(n=rnfeltnorm(R,Mod(lift(C.fu[i]),R.pol)),v=bnfisunit(B,n));
    check(#v==2,"unit norm in certified basis");
    row[i]=v[1];signs[i]=v[2];
    print("{\"type\":\"norm\",\"index\":",i,",\"element\":",jpoly(C.fu[i]),",\"norm\":",jpoly(n),",\"coordinates\":",Vec(v),"}");
  );
  print("{\"type\":\"completion\",\"status\":\"PASS\",\"norm_row\":",row,",\"signs\":",signs,",\"norm_index\":",gcd(row),"}");
};
run();
quit;
