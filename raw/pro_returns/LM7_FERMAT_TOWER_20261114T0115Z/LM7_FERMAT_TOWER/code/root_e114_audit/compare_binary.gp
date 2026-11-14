default(parisize,128000000);
{
 my(A=read("/workspace/scratch/e34c61ec5a35/research_e114/code/e_inert_tail_orbit.bin"),B=read("/workspace/scratch/e34c61ec5a35/root_e114_audit/replay/code/e_inert_tail_orbit.bin"));
 my(eq=(A===B),ce=vector(#A,i,A[i]===B[i]),base=vector(#A[1],i,A[1][i]===B[1][i]));
 print("{\"full_GEN_equal\":",eq,",\"component_count\":",#A,",\"component_equal\":",ce,",\"entire_base_GEN_equal\":",A[1]===B[1],",\"base_component_equal\":",base,"}");
 if(!eq || #A!=4,error("full PARI object mismatch"));
}
quit;

