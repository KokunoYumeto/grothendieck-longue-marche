\\ Complete actual author/root PARI-object comparison. Run from the paper directory.
default(parisize,256000000);
a=read("code/e_ordinary_refinement.bin");
b=read("code/e91_root_rebuild/code/e_ordinary_refinement.bin");
if(a!=b,error("Complete E91 PARI objects differ"));
print("PASS: all ",#a," complete PARI objects agree; no exclusions.");
quit;
