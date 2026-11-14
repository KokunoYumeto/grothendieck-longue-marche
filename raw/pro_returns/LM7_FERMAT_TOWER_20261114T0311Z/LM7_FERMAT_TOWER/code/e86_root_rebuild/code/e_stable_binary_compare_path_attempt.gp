\\ Independent semantic comparison of every retained PARI object.
default(parisize, 1000000000);
names=["e_stable_lower_genus","e_stable_class_coordinates","e_stable_class_maps"];
for(i=1,#names, a=read(Str("../../research_e86/code/",names[i],".bin")); b=read(Str("code/",names[i],".bin")); if(a!=b,error(Str("different complete PARI values: ",names[i]))); print(names[i]," COMPLETE_VALUE_EQUAL ",type(a)," length ",#a));
print("PASS: all three complete binary certificate values are equal.");
quit;
