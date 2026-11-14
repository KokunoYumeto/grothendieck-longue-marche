default(parisize,256000000);
default(parisizemax,2000000000);
run()={
 my(d=read("research_e97/code/e_cyclic_norm_switch.bin"),u=d[17],a=read("research_e97/code/e_zeta_unit_defect.bin"));
 print("HORIZONTAL_RELATIVE_WITNESS ",u);
 print("HORIZONTAL_COEFFICIENTS ",vector(3,i,Vec(lift(polcoef(lift(u),i-1,variable(u.mod))))));
 print("LOWER_CLASS_FORWARD ",a[7]," MODULI ",a[8]);
 print("WITNESS_SUPPORT ",vector(#a[5],i,vector(6,j,a[5][i][j])));
 print("GENUS_AND_CLASS ",a[6]," ",a[9]);
 print("LOWER_GENUS_DATA ",read("research_e86/code/e_stable_lower_genus.bin")[6]);
};
run();
quit;
