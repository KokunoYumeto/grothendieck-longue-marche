# Test the actual inclusion A* -> V* on H2(J_T,-).
UNIVERSAL_CONTINUE:=true;;
Read("work/centralizer_code/check_universal_six_source.g");;
if not IsBound(RELATION_SUFFIX) then RELATION_SUFFIX:="";fi;
Read(Concatenation("work/centralizer_code/relation_cohomology_modules_",String(RELATION_P),RELATION_SUFFIX,".g"));;
te:=Elements(gg);;iso:=IsomorphismPcGroup(joint);;jp:=Image(iso);;pc:=Pcgs(jp);;
proj:=RestrictedMapping(Projection(product6,1),joint);;
indices:=List(pc,g->Position(te,Image(proj,PreImagesRepresentative(iso,g))));;
smallmod:=GModuleByMats(List(indices,i->RelationSmallMats[i]*One(GF(RELATION_P))),GF(RELATION_P));;
bigmod:=GModuleByMats(List(indices,i->RelationFullMats[i]*One(GF(RELATION_P))),GF(RELATION_P));;
Print("RELATION H2 START: p=",RELATION_P,"; PC=",Length(pc),"; small=",Length(RelationEmbed),"; full=25; runtime=",Runtime(),"\n");
smallco:=TwoCohomology(jp,smallmod);;
sb:=BasisVectors(Basis(Range(smallco.cohom)));;
Print("RELATION H2 small dimension=",Length(sb),"; runtime=",Runtime(),"\n");
bigco:=TwoCohomology(jp,bigmod);;
bb:=BasisVectors(Basis(Range(bigco.cohom)));;
Print("RELATION H2 full dimension=",Length(bb),"; runtime=",Runtime(),"\n");
emb:=RelationEmbed*One(GF(RELATION_P));;ds:=Length(emb);;images:=[];;
for v in sb do
 coc:=PreImagesRepresentative(smallco.cohom,v);;
 if Length(coc) mod ds<>0 then Error("module block alignment");fi;
 included:=Concatenation(List([0..Length(coc)/ds-1],i->coc{[i*ds+1..(i+1)*ds]}*emb));;
 if not included in Source(bigco.cohom) then Error("included H2 cocycle failed");fi;
 Add(images,Image(bigco.cohom,included));
od;
Print("RELATION H2 MAP: p=",RELATION_P,"; small dimension=",Length(sb),"; full dimension=",Length(bb),"; image rank=",RankMat(images),"; injective=",RankMat(images)=Length(sb),"; runtime=",Runtime(),"\n");
QUIT_GAP(0);
