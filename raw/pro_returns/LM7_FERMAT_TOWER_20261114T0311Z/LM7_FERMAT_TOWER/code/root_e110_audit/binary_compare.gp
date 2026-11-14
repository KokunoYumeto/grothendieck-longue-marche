default(realprecision, 100);
a=read("/workspace/scratch/e34c61ec5a35/research_e110/code/e_pure_tower_base.bin");
b=read("/workspace/scratch/e34c61ec5a35/root_e110_audit/fresh/code/e_pure_tower_base.bin");
if(a!=b,error("Full deserialized PARI object mismatch"));
print("Full readbin vectors equal: ",a==b);
print("Exact identity test: ",a===b);
print("Top-level components: ",#a);
for(i=1,#a,print("Component ",i,": ",type(a[i]),"; equal=",a[i]==b[i],"; identical=",a[i]===b[i]));
quit;
