default(parisize,128000000);default(parisizemax,1000000000);
check(a,s)=if(!a,error(s));
{
my(a0=read("/workspace/scratch/e34c61ec5a35/root_e124_audit/replay_tree/code/e53_ordinary_kernel.bin"),b0=read("/workspace/scratch/e34c61ec5a35/root_e124_audit/replay_tree/audit/root_fresh/fresh/code/e53_ordinary_kernel.bin"));
check(a0===b0,"complete decoded GEN equality");
print("{\"file\":\"e53_ordinary_kernel.bin\",\"complete_GEN_identity\":true,\"components\":",#a0,"}");
my(a1=read("/workspace/scratch/e34c61ec5a35/root_e124_audit/replay_tree/code/e53_ordinary_genus.bin"),b1=read("/workspace/scratch/e34c61ec5a35/root_e124_audit/replay_tree/audit/root_fresh/fresh/code/e53_ordinary_genus.bin"));
check(a1===b1,"complete decoded GEN equality");
print("{\"file\":\"e53_ordinary_genus.bin\",\"complete_GEN_identity\":true,\"components\":",#a1,"}");
print("{\"status\":\"PASS\",\"scope\":\"complete objects, zero exclusions\"}");
}
quit;
