# Export exact Bass--Serre graph and the finite groups needed by Shapiro.
UNIVERSAL_CONTINUE:=true;;
Read("work/centralizer_code/check_universal_six_source.g");;
te:=Elements(gg);;nt:=Length(te);;
edgeS:=List(te,t->Set(List([0..1],i->Position(te,t*markedS^i))));;
edgeR:=List(te,t->Set(List([0..2],i->Position(te,t*markedR^i))));;
verticesS:=Set(edgeS);;verticesR:=Set(edgeR);;
endpoints:=List([1..nt],i->[Position(verticesS,edgeS[i]),Length(verticesS)+Position(verticesR,edgeR[i])]);;
leftInverseActions:=List(te,g->List(te,t->Position(te,g^-1*t)));;
inverseIndices:=List(te,g->Position(te,g^-1));;
PCGroupDataWithTarget:=function(gr,targetMap)
 local iso,pg,pgrp,conj,i,j;
 iso:=IsomorphismPcGroup(gr);pgrp:=Image(iso);pg:=Pcgs(pgrp);conj:=[];
 for i in [1..Length(pg)] do for j in [1..i-1] do Add(conj,[i,j,ExponentsOfConjugate(pg,i,j)]);od;od;
 return [Size(gr),RelativeOrders(pg),List([1..Length(pg)],i->ExponentsOfRelativePower(pg,i)),conj,List(pg,g->Position(te,Image(targetMap,PreImagesRepresentative(iso,g))))];
end;;
proj1:=RestrictedMapping(Projection(product6,1),joint);;
targetId:=IdentityMapping(gg);;
stream:=OutputTextFile("work/centralizer_code/universal_relation_module_data.json",false);;
SetPrintFormattingStatus(stream,false);
PrintTo(stream,"{\"target_order\":",nt,",\"vertex_counts\":[",Length(verticesS),",",Length(verticesR),"],\"edge_endpoints\":",endpoints,",\"left_inverse_actions\":",leftInverseActions,",\"inverse_indices\":",inverseIndices,",\"s_index\":",Position(te,markedS),",\"r_index\":",Position(te,markedR),",\"T2_indices\":",List(Elements(nn2),g->Position(te,g)),",\"T3_indices\":",List(Elements(nn3),g->Position(te,g)),",\"O2_indices\":",List(Elements(PCore(gg,2)),g->Position(te,g)),",\"O3_indices\":",List(Elements(PCore(gg,3)),g->Position(te,g)),",\"T_pc\":",PCGroupDataWithTarget(gg,targetId),",\"J_pc\":",PCGroupDataWithTarget(joint,proj1),"}\n");
CloseStream(stream);
Print("Exported exact 144-edge,120-vertex Bass--Serre graph and T/J_T PC presentations.\n");
QUIT_GAP(0);
