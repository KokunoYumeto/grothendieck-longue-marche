\\ Exact natural coordinates of the positive cube-root candidate.
default(parisizemax,2000000000);default(parisize,128000000);
cc=read("/tmp/birational_ninth_root_nfinit_cache.bin");
nn=cc[1];tt=cc[2];zz=cc[3];
rr=read("/tmp/birational_ninth_root_cube13.bin")[2];
mm=vector(54,j,tt^((j-1)\6)*zz^((j-1)%6));
mtx=matrix(54,54,i,j,polcoef(lift(mm[j]),i-1));
rv=vector(54,i,polcoef(lift(rr),i-1))~;
print("START_COORDINATES ",getwalltime());
cv=matsolve(mtx,rv);
if(sum(j=1,54,cv[j]*mm[j])!=rr,error("natural coordinates"));
print("NATURAL_ROOT ",Vec(cv));
print("DONE ",getwalltime());
quit;
