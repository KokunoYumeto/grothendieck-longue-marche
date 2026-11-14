a=read("/workspace/scratch/e34c61ec5a35/research_e111/code/e_nonunit_seventeen_base.bin");
b=read("/workspace/scratch/e34c61ec5a35/a_e111_audit/fresh/code/e_nonunit_seventeen_base.bin");
if(a!=b,error("complete deserialized GEN differs"));
if(#a!=5,error("unexpected full binary shape"));
for(i=1,5,if(a[i]!=b[i],error("component differs")));
print("PASS: complete deserialized GEN identity, all five components");
quit;
