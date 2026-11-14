default(parisize,256000000);default(parisizemax,1000000000);
{
 my(a=read("../../code/e53_positional_presentation.bin"),b=read("fresh/code/e53_positional_presentation.bin"));
 print("outer components ",#a," ",#b);
 for(i=1,#a,print("component ",i," ",a[i]===b[i]," types ",type(a[i])," ",type(b[i])));
 for(i=1,#a[1],print("B component ",i," ",a[1][i]===b[1][i]," types ",type(a[1][i])," ",type(b[1][i])));
}
quit;
