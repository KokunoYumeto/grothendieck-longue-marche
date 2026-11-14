default(parisize,128000000);default(parisizemax,1000000000);
check(a,s)=if(!a,error(s));
{
my(a0=read("/workspace/scratch/e34c61ec5a35/research_e123/code/e53_positional_genus_pivots.bin"),b0=read("/workspace/scratch/e34c61ec5a35/research_e123/audit/author_replay_complete/fresh/code/e53_positional_genus_pivots.bin"));
check(a0===b0,"complete GEN equality");
print("{\"file\":\"e53_positional_genus_pivots.bin\",\"complete_GEN_identity\":true,\"components\":",#a0,"}");
my(a1=read("/workspace/scratch/e34c61ec5a35/research_e123/code/e53_positional_presentation.bin"),b1=read("/workspace/scratch/e34c61ec5a35/research_e123/audit/author_replay_complete/fresh/code/e53_positional_presentation.bin"));
check(a1===b1,"complete GEN equality");
print("{\"file\":\"e53_positional_presentation.bin\",\"complete_GEN_identity\":true,\"components\":",#a1,"}");
print("{\"status\":\"PASS\",\"scope\":\"whole decoded objects; no component exclusions\"}");
}
quit;
