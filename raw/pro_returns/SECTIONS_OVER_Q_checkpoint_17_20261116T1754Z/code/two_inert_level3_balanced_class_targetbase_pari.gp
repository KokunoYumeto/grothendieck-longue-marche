\\ Discovery only: the output must not be used as a completeness assertion.
\\ Direct absolute degree27 model avoids the timed-out relative-norm setup.
default(parisizemax,2000000000);
default(parisize,512000000);
default(realprecision,100);setrand(3);
d=649;P=x^27-3^8*d^3;
N=nfinit([P,[3,11,59]]);
print("ABSOLUTE NF READY DISC ",factor(N.disc));
setdebug("bnf",1);
B=bnfinit(N,1,[0.002,0]);
print("CANDIDATE CLASS STRUCTURE NOT CERTIFIED ",B.cyc);
for(j=1,4,q=[2,3,11,59][j]; Ps=idealprimedec(B,q);for(k=1,#Ps,print("PRIME ",q," ",k," e ",Ps[k][3]," f ",Ps[k][4]," candidate class ",bnfisprincipal(B,Ps[k],0))));
writebin("/tmp/birational-pari-runtime/level3_bnf_targetbase_cache.bin",B);
print("CANDIDATE BNF CACHE SAVED");
quit;
