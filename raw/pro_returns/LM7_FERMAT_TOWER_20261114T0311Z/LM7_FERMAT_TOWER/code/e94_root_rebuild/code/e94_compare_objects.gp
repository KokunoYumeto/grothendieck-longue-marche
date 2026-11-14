default(parisize,256000000);
default(parisizemax,2000000000);
names=["e_mu27_base_bnf","e_mu27_local","e_mu27_genus"];
for(i=1,#names,a=read(Str("research_e94/code/",names[i],".bin"));b=read(Str("root_e94_audit/code/",names[i],".bin"));if(a!=b,error(Str("Full PARI object differs: ",names[i])));print("PASS full PARI object equality: ",names[i]));
print("PASS all3 full objects; no field or precision exclusions.");
quit;
