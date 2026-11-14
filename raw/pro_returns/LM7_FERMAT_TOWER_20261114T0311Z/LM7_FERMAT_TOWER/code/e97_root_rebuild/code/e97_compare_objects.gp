\\ Compare complete actual PARI objects; raw writebin headers are noncanonical.
default(parisize,256000000);
names=["e_unit_norm_coset","e_unit_norm_coset_lower"];
for(i=1,#names,a=read(Str("research_e97/code/",names[i],".bin"));b=read(Str("root_e97_audit/code/",names[i],".bin"));if(a!=b,error(Str("Full PARI object differs: ",names[i])));print("PASS full PARI object equality: ",names[i]));
print("DONE_COMPLETE_E97_OBJECT_COMPARISON");
quit;
