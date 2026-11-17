Print(Filtered(RecNames(GAPInfo.PackagesInfo),x->x in ["recog","recogbase","classicpres","cvec","forms","orb","matrixss","meataxe64","smallgrp"]),"\n");
for x in ["recog","recogbase","forms","orb"] do Print(x," ",LoadPackage(x),"\n"); od;
QUIT;
