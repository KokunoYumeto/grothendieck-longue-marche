default(parisize,128000000);
a=read("research_e117/code/a_quartic_three_fields.bin");
b=read("research_e117/replay/code/a_quartic_three_fields.bin");
print("complete_objects_equal=",a==b);
for(i=1,#a, print("field",i,"_equal=",a[i]==b[i]);for(j=1,#a[i],if(a[i][j]!=b[i][j],print("different_component=",i,"/",j," ",type(a[i][j])))));
if(a!=b,quit(1));
print("PASS full exact deserialized PARI objects, no fields omitted");
quit(0);
