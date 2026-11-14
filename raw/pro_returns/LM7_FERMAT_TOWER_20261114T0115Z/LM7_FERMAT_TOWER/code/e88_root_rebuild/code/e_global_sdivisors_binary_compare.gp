run()={
 my(a=read("inputs/author_binary/e_global_sdivisors.bin"),b=read("code/e_global_sdivisors.bin"));
 if(a!=b,error("complete PARI object differs"));
 print("E88 complete PARI binary object: PASS");
};
run();
quit;
