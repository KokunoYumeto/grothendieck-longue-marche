\\ Bounded positive-only unit discovery with documented nonnegative weights.
\\ Every displayed candidate retains literal ideal and factor maps.
default(parisizemax,1500000000);default(parisize,128000000);
default(realprecision,700);setrand(187);
d=649;walkPol=x^27-3^8*d^3;walkNf=nfinit([walkPol,[3,11,59]]);
walkOne=matid(27);walkTwo=idealprimedec(walkNf,2);walkStart=idealhnf(walkNf,walkTwo[1]);if(walkTwo[1].f!=1,error("two-prime label"));walkCache=Map();mapput(walkCache,walkStart,[[],[0,0],0]);
walkQ11=idealprimedec(walkNf,11);walkQ59=idealprimedec(walkNf,59);
walkP11=walkQ11[2];walkP59=walkQ59[2];
if(walkP11.f!=2 || walkP59.f!=2,error("quadratic prime labels"));
walkM11=nfmodprinit(walkNf,walkP11,'z);walkM59=nfmodprinit(walkNf,walkP59,'z);
walkAlpha=Mod(x^18/(243*d^2),walkPol);walkRoot=Mod(x,walkPol);
walkOm11=nfmodpr(walkNf,walkAlpha,walkM11)^40;
walkOm59=nfmodpr(walkNf,walkAlpha,walkM59)^1160;
walkP=12583;walkResidue=261;walkGen=znprimroot(walkP);walkZ9=walkGen^((walkP-1)/9);
walkAlphaP=Mod(walkResidue,walkP)^18/(243*d^2);walkUP=walkAlphaP^2-2;
walkOm27=walkUP^((walkP-1)/27);
if(walkOm27^9==1,error("order27"));
walkQlog(a,pr,mp,om,p)={my(k=nfeltval(walkNf,a,pr),u=a/walkRoot^k,ch=nfmodpr(walkNf,u,mp)^((p^2-1)/3));for(e=0,2,if(om^e==ch,return(e)));error("q log")};
walkNormlog(a)={my(z=Mod(1,walkP),pol=lift(a),ch);for(j=0,8,z*=subst(pol,x,Mod(walkResidue,walkP)*walkZ9^j));if(z==0,return(-1));ch=z^((walkP-1)/27);for(e=0,26,if(walkOm27^e==ch,return(e)));error("norm log")};
walkIdeal=walkStart;walkPath=[];walkChars=[0,0];walkLog=0;walkCollisions=0;
print("START ",getwalltime());
for(trial=1,120,if(trial%40==1,walkIdeal=walkStart;walkPath=[];walkChars=[0,0];walkLog=0);walkDir=if(trial<=28,vector(14,j,if(j==(trial-1)%14+1,if(trial<=14,900,0),if(trial<=14,0,900))),vector(14,j,random(700)));walkRed=idealred(walkNf,[walkIdeal,1],walkDir);walkNext=walkRed[1];walkA=nfbasistoalg(walkNf,walkRed[2]);if(idealhnf(walkNf,idealmul(walkNf,walkA,walkNext))!=walkIdeal,error("literal ideal map"));walkPath=concat(walkPath,[Vecrev(lift(walkA))]);walkChars=lift(Mod(walkChars+[walkQlog(walkA,walkP11,walkM11,walkOm11,11),walkQlog(walkA,walkP59,walkM59,walkOm59,59)],3));walkE=walkNormlog(walkA);if(walkE<0,print("SPECIAL NORM PRIME AT ",trial);walkIdeal=walkStart;walkPath=[];walkChars=[0,0];walkLog=0;next);walkLog=(walkLog+walkE)%27;walkIdeal=walkNext;if(!mapisdefined(walkCache,walkNext,&walkOld),mapput(walkCache,walkNext,[walkPath,walkChars,walkLog]),walkCollisions++;walkC=lift(Mod(walkChars-walkOld[2],3));walkE=lift(Mod(walkLog-walkOld[3],27));if(walkE%9,error("unit norm exponent"));walkDiff=lift(Mod(walkC-[2,2]*(walkE/9),3));print("COLLISION ",trial," QCHAR ",walkC," NORMLOG ",walkE," SECONDARY ",walkDiff," PATHLENS ",[#walkPath,#walkOld[1]]);if(walkDiff!=[0,0],print("POSITIVE NUMERATOR FACTORS ",walkPath);print("POSITIVE DENOMINATOR FACTORS ",walkOld[1]);print("POSITIVE SECONDARY DISCREPANCY REQUIRES INDEPENDENT CERTIFICATE");quit));if(trial%20==0,print("PROGRESS ",trial," CACHE ",matsize(Mat(walkCache))[1]," COLLISIONS ",walkCollisions," TIME ",getwalltime())));
print("FINITE SEARCH COMPLETE ",walkCollisions," TIME ",getwalltime());
print("No full unit-lattice assertion or negative arithmetic inference.");
quit;
