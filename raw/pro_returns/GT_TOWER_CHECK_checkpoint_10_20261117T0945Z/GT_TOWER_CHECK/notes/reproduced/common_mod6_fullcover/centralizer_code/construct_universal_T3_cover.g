# Construct B/[T3,L]L^2 with its exact marked rank-three module.
UNIVERSAL_CONTINUE:=true;;
Read("work/centralizer_code/check_universal_six_source.g");;
Read("work/centralizer_code/universal_T3_module.g");;
te:=Elements(gg);;ip:=IsomorphismPcGroup(gg);;gp:=Image(ip);;pc:=Pcgs(gp);;n:=Length(pc);;
sm:=Image(ip,markedS);;rm:=Image(ip,markedR);;
mm:=List(pc,g->T3AllMats[Position(te,PreImagesRepresentative(ip,g))]*One(GF(2)));;
modu:=GModuleByMats(mm,GF(2));;
co:=TwoCohomology(gp,modu);;bas:=BasisVectors(Basis(Range(co.cohom)));;
Print("T3 rank-three extension cohomology dimension=",Length(bas),"\n");
coeffs:=Tuples(GF(2),Length(bas));;found:=false;;
for coeff in coeffs do
 v:=PreImagesRepresentative(co.cohom,Sum([1..Length(bas)],i->coeff[i]*bas[i]));;
 ext:=Extension(gp,modu,v);;ep:=Pcgs(ext);;
 ls:=MappedPcElement(sm,pc,ep{[1..n]});;lr:=MappedPcElement(rm,pc,ep{[1..n]});;
 ker:=Group(AsList(ep){[n+1..Length(ep)]});;
 poss:=Filtered(List(Elements(ker),k->ls*k),g->g^2=One(ext));;
 posr:=Filtered(List(Elements(ker),k->lr*k),g->g^3=One(ext));;
 for cs in poss do for cr in posr do
  if Size(Group(cs,cr))=Size(ext) then
   found:=true;T3cover:=ext;T3coverS:=cs;T3coverR:=cr;
   Print("FOUND full T3 cover: order=",Size(ext),"; class=",List(coeff,IntFFE),"; frames=",ExponentsOfPcElement(ep,cs),",",ExponentsOfPcElement(ep,cr),"\n");
   break;
  fi;
 od;if found then break;fi;od;
 if found then break;fi;
od;
if not found then Error("no full T3 marked cover found");fi;
if not IsBound(T3_COVER_CONTINUE) or not T3_COVER_CONTINUE then QUIT_GAP(0);fi;
