\\ Positive relation search only. A missing relation proves nothing.
default(parisizemax,1000000000);default(parisize,256000000);
default(realprecision,100);setrand(171);
d=649;P=x^27-3^8*d^3;N=nfinit([P,[3,11,59]]);
Ptwo=idealprimedec(N,2);Pthree=idealprimedec(N,3);
Qeleven=idealprimedec(N,11);Qfiftynine=idealprimedec(N,59);
Sp=concat(concat(Ptwo,Pthree),concat(Qeleven,Qfiftynine));
Beleven=idealdiv(N,Qeleven[2],idealpow(N,Qeleven[1],2));
Bfiftynine=idealdiv(N,Qfiftynine[2],idealpow(N,Qfiftynine[1],2));
targets=vector(9,j,my(b=j-5,c=centerlift(Mod(4*b+3,9)));idealmul(N,Ptwo[1],idealmul(N,idealpow(N,Beleven,b),idealpow(N,Bfiftynine,c))));
cache=Map();seen=Set([]);count=0;tried=0;large=0;
prindex(pr)={my(pp=pr[1],pl);if(!mapisdefined(cache,pp,&pl),pl=idealprimedec(N,pp);mapput(cache,pp,pl));for(kk=1,#pl,if(pl[kk]==pr,return(kk)));error("prime index mismatch")};
for(trial=1,1500,jj=1+(trial%9);II=targets[jj];red=idealred(N,[II,1],vector(14,j,random(10)));JJ=red[1];nn=idealnorm(N,JJ);ff=factor(nn);tried++;if(ff[#ff~,1]>5000,large++;next);fac=idealfactor(N,JJ);row=vector(#fac~,j,[fac[j,1][1],prindex(fac[j,1]),fac[j,2]]);key=[jj,row];if(setsearch(seen,key),next);seen=setunion(seen,[key]);aa=nfbasistoalg(N,red[2]);if(idealmul(N,idealhnf(N,aa),JJ)!=II,error("reduction orientation mismatch"));count++;print("REL ",count," TARGET ",jj," JFACT ",row," COEFF ",Vecrev(lift(aa)));if(count%20==0,print("PROGRESS ",[tried,count,large])));
print("SEARCH SUMMARY ",[tried,count,large]);
print("Every saved row is a literal principal relation; no class-group completeness is asserted.");
quit;
