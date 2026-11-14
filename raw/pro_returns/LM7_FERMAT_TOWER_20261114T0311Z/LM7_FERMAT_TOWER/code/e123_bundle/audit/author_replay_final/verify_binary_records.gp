default(parisize,256000000);default(parisizemax,1000000000);
check(a,s)=if(!a,error(s));
{
 my(a=read("../../code/e53_positional_presentation.bin"),b=read("fresh/code/e53_positional_presentation.bin"));
 check(#a==2 && #a[1]==13 && #a[2]==13 && #b==13,"actual append-container types");
 check(a[1]===b && a[2]===b,"both complete records equal the fresh complete object");
 check(a==[b,b],"literal diagonal inverse to either record projection");
 print("{\"status\":\"PASS\",\"reference_records\":2,\"components_per_record\":13,\"record1_complete_identity\":true,\"record2_complete_identity\":true,\"exact_map\":\"[B,B] maps to B; inverse B maps to [B,B]\",\"excluded_components\":[]}");
}
quit;
