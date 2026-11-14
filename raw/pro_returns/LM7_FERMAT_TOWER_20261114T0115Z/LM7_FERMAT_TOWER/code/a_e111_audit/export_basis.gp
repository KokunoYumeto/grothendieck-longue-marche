a=read("/workspace/scratch/e34c61ec5a35/research_e111/code/e_nonunit_seventeen_base.bin");
F=a[1].nf;
print(vector(#F.zk,i,vector(6,j,polcoef(F.zk[i],j-1))));
quit;
