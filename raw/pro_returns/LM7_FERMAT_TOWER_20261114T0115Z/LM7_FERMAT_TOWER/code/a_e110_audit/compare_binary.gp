a=read("/workspace/scratch/e34c61ec5a35/research_e110/code/e_pure_tower_base.bin");
b=read("/workspace/scratch/e34c61ec5a35/a_e110_audit/rebuild/code/e_pure_tower_base.bin");
if(a!=b,error("complete GEN comparison failed"));
print("PASS: complete deserialized GEN identity, all ",#a," components");
quit;
