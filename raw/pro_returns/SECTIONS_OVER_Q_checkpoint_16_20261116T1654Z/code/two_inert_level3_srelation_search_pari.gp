\\ Positive-only principal S-relation discovery. No class-group claim.
default(parisizemax,1000000000);default(parisize,256000000);
default(realprecision,120);setrand(170);
d=649;P=x^27-3^8*d^3;N=nfinit([P,[3,11,59]]);
Ptwo=idealprimedec(N,2);Pthree=idealprimedec(N,3);
Qeleven=idealprimedec(N,11);Qfiftynine=idealprimedec(N,59);
Sp=concat(concat(Ptwo,Pthree),concat(Qeleven,Qfiftynine));
print("S EF ",vector(#Sp,j,[Sp[j][1],Sp[j][3],Sp[j][4]]));
Beleven=idealdiv(N,Qeleven[2],idealpow(N,Qeleven[1],2));
Bfiftynine=idealdiv(N,Qfiftynine[2],idealpow(N,Qfiftynine[1],2));
seen=Set([]);count=0;nonS=0;
for(b=-4,4,c=centerlift(Mod(4*b+3,9));II=idealmul(N,Ptwo[1],idealmul(N,idealpow(N,Beleven,b),idealpow(N,Bfiftynine,c)));iv=vector(#Sp,j,idealval(N,II,Sp[j]));for(trial=0,100,red=if(trial==0,idealred(N,[II,1]),idealred(N,[II,1],vector(14,j,random(90))));JJ=red[1];jv=vector(#Sp,j,idealval(N,JJ,Sp[j]));nn=prod(j=1,#Sp,Sp[j][1]^(Sp[j][4]*jv[j]));if(nn!=idealnorm(N,JJ),nonS++;next);vv=iv-jv;if(setsearch(seen,vv),next);seen=setunion(seen,[vv]);aa=nfbasistoalg(N,red[2]);if(idealmul(N,idealhnf(N,aa),JJ)!=II,error("principal reduction direction mismatch"));count++;print("REL ",count," PAIR ",[b,c]," TRIAL ",trial," VAL ",vv," COEFF ",Vecrev(lift(aa)))));
print("DISCOVERY SUMMARY ",[count,nonS]);
print("Only the displayed literal principal relations are asserted; no completeness or nonprincipality claim.");
quit;
