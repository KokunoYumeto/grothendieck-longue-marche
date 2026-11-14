default(parisize,128000000);
a=read("/workspace/scratch/e34c61ec5a35/research_e117/code/a_quartic_three_fields.bin");
b=read("/workspace/scratch/e34c61ec5a35/root_e117_audit/fresh/code/a_quartic_three_fields.bin");
if(a!=b,print("FAIL complete GEN equality");quit(1));
for(k=1,#a,if(a[k]!=b[k],print("FAIL component ",k);quit(1)));
print("PASS complete GEN equality; all ",#a," field records and every nested BNF component equal");
quit(0);
