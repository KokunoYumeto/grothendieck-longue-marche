UNIVERSAL_CONTINUE:=true;;
Read("work/centralizer_code/check_universal_six_source.g");;
proj:=RestrictedMapping(Projection(product6,1),joint);;
for p in [2,3] do
 normalTarget:=PCore(gg,6/p);;
 normalProduct:=Group(Concatenation(List([1..6],i->List(GeneratorsOfGroup(normalTarget),g->Image(Embedding(product6,i),g)))));;
 normalJoint:=Intersection(joint,normalProduct);;
 image:=Image(proj,normalJoint);;
 Print("RELATION COPRIME CORE: coefficient p=",p,"; target core order=",Size(normalTarget),"; joint normal subgroup order=",Size(normalJoint),"; first image order=",Size(image),"; full=",image=normalTarget,"\n");
 if not IsNormal(joint,normalJoint) or image<>normalTarget then Error("coprime module comparison");fi;
od;
QUIT_GAP(0);
