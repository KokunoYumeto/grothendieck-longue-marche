\\ Positive-only LLL search on the nine permitted balanced ideal classes.
\\ A nonunit reduced ideal is not a nonprincipality conclusion.
default(parisizemax,1000000000);default(parisize,256000000);
default(realprecision,100);setrand(13);
d=649;P=x^27-3^8*d^3;N=nfinit([P,[3,11,59]]);
Ptwo=idealprimedec(N,2);Qeleven=idealprimedec(N,11);Qfiftynine=idealprimedec(N,59);
print("TWO DEGREES ",vector(#Ptwo,j,Ptwo[j][4]));
print("ELEVEN DEGREES ",vector(#Qeleven,j,Qeleven[j][4]));
print("FIFTYNINE DEGREES ",vector(#Qfiftynine,j,Qfiftynine[j][4]));
Beleven=idealdiv(N,Qeleven[2],idealpow(N,Qeleven[1],2));
Bfiftynine=idealdiv(N,Qfiftynine[2],idealpow(N,Qfiftynine[1],2));
for(b=-4,4,c=centerlift(Mod(4*b+3,9));JJ=idealmul(N,Ptwo[1],idealmul(N,idealpow(N,Beleven,b),idealpow(N,Bfiftynine,c)));print("BALANCED PAIR ",b," ",c," NORM ",idealnorm(N,JJ));for(trial=0,12,red=if(trial==0,idealred(N,[JJ,1]),idealred(N,[JJ,1],vector(14,j,random(40))));if(red[1]==matid(27),print("POSITIVE PRINCIPAL CANDIDATE ",b," ",c," ",trial," ",Vecrev(lift(nfbasistoalg(N,red[2]))));quit);if(trial==0,print("INITIAL REDUCED NORM ",idealnorm(N,red[1])))));
print("NO POSITIVE CANDIDATE IN THIS FINITE SEARCH; NO NONPRINCIPALITY INFERENCE");
quit;
