# Exact finite homology-cover refinements of the universal base.
# SMALL_P is set by the two wrappers.  No identification with the full
# infinite reduced kernel is made by this finite calculation.
UNIVERSAL_CONTINUE:=true;;
Read("work/centralizer_code/check_universal_six_source.g");;
HomologyCover:=function(q,qs,qr,p)
 local els,n,id,mi,g,per,mat,delta,gens,sg,rg,hg,iso;
 els:=Elements(q);n:=Length(els);id:=Position(els,One(q));gens:=[];
 for g in [qs,qr] do
  per:=List(els,t->Position(els,g^-1*t));
  mat:=NullMat(n+1,n+1,GF(p));
  for mi in [1..n] do mat[mi][per[mi]]:=One(GF(p));od;
  mat[n+1][n+1]:=One(GF(p));
  if g=qr then
   mat[n+1][id]:=mat[n+1][id]+One(GF(p));
   mi:=Position(els,qr^-1);
   mat[n+1][mi]:=mat[n+1][mi]-One(GF(p));
  fi;
  Add(gens,mat);
 od;
 sg:=gens[1];rg:=gens[2];hg:=Group(sg,rg);
 if Order(sg)<>2 or Order(rg)<>3 then Error("graph cover torsion marking");fi;
 Print("HOMOLOGY COVER: quotient=",n,"; p=",p,"; expected rank=",1+n/6,"; size=",Size(hg),"\n");
 if Size(hg)<>n*p^(1+n/6) then Error("graph homology cover order");fi;
 iso:=IsomorphismPermGroup(hg);
 return [Image(iso),Image(iso,sg),Image(iso,rg)];
end;;
covers:=[];;
if SMALL_P=2 then
 for ker in [nn2] do
  nq:=NaturalHomomorphismByNormalSubgroup(gg,ker);;
  Add(covers,HomologyCover(Image(nq),Image(nq,markedS),Image(nq,markedR),2));
 od;
 if IsBound(SMALL_EXPANDED) and SMALL_EXPANDED then
  nq:=NaturalHomomorphismByNormalSubgroup(gg,PCore(gg,3));;
  Add(covers,HomologyCover(Image(nq),Image(nq,markedS),Image(nq,markedR),2));
 elif IsBound(SMALL_FULL) and SMALL_FULL then
  T3_COVER_CONTINUE:=true;;
  Read("work/centralizer_code/construct_universal_T3_cover.g");;
  ti:=IsomorphismPermGroup(T3cover);;
  Add(covers,[Image(ti),Image(ti,T3coverS),Image(ti,T3coverR)]);
 else
  nq:=NaturalHomomorphismByNormalSubgroup(gg,nn3);;
  Add(covers,HomologyCover(Image(nq),Image(nq,markedS),Image(nq,markedR),2));
 fi;
else
 o2:=PCore(gg,2);;
 if Size(o2)<>8 then Error("T O2 order");fi;
 nq:=NaturalHomomorphismByNormalSubgroup(gg,o2);;
 Add(covers,HomologyCover(Image(nq),Image(nq,markedS),Image(nq,markedR),3));
fi;
pr:=DirectProduct(Concatenation([gg],List(covers,z->z[1])));;
newS:=Image(Embedding(pr,1),markedS);;newR:=Image(Embedding(pr,1),markedR);;
for i in [1..Length(covers)] do
 newS:=newS*Image(Embedding(pr,i+1),covers[i][2]);;
 newR:=newR*Image(Embedding(pr,i+1),covers[i][3]);;
od;
newTarget:=Group(newS,newR);;
if IsBound(SMALL_PC_SOURCE) and SMALL_PC_SOURCE then
 Read("work/centralizer_code/build_six_pc_source.g");;
 pcs:=BuildSixPcSource(newTarget,newS,newR);;
 source:=pcs.group;;ss:=pcs.s;;rr:=pcs.r;;
 Print("SMALL HOMOLOGY PC source: prime=",SMALL_P,"; target order=",Size(newTarget),"; source order=",Size(source),"\n");
else
it:=IsomorphismPermGroup(newTarget);;targetPerm:=Image(it);;
sourceTargetX:=Image(it,newS);;sourceTargetY:=Image(it,newS*newR);;
targetDegree:=LargestMovedPoint(targetPerm);;
barS:=(1,2);;barR:=(1,2,3);;
transversal:=[(),barS,barR,barR^2,barS*barR,barS*barR^2];;
weights:=[(),(),sourceTargetY^-1,sourceTargetX,sourceTargetX^-1,sourceTargetY];;
InducedSmall:=function(bar,ws)
 local imgs,i,j,k,block;
 imgs:=[];
 for i in [1..6] do
  j:=Position(transversal,transversal[i]*bar);
  block:=ListPerm(ws[i],targetDegree);
  for k in [1..targetDegree] do Add(imgs,targetDegree*(j-1)+block[k]);od;
 od;
 return PermList(imgs);
end;;
ss:=InducedSmall(barS,weights);;rr:=InducedSmall(barR,List([1..6],i->()));;
source:=Group(ss,rr);;
Print("SMALL HOMOLOGY source: prime=",SMALL_P,"; target order=",Size(newTarget),"; source order=",Size(source),"; degree=",LargestMovedPoint(source),"\n");
fi;
if Size(source)<>11943936*(Size(newTarget)/144)^6 then Error("small full product kernel");fi;
iso:=IsomorphismPcGroup(source);;gp:=Image(iso);;sp:=Image(iso,ss);;rp:=Image(iso,rr);;
if IsBound(SMALL_DROP_PPRIME) and SMALL_DROP_PPRIME then
 other:=6/SMALL_P;;normalOther:=PCore(gp,other);;
 Print("SMALL COPRIME REDUCTION: p=",SMALL_P,"; normal other-prime core order=",Size(normalOther),"; original order=",Size(gp),"\n");
 qq:=NaturalHomomorphismByNormalSubgroup(gp,normalOther);;
 sp:=Image(qq,sp);;rp:=Image(qq,rp);;gp:=Image(qq);;
 if AbelianInvariants(gp)<>[2,3] then Error("small quotient abelianization");fi;
fi;
if not IsBound(SMALL_BUILD_ONLY) or not SMALL_BUILD_ONLY then
pc:=Pcgs(gp);;n:=Length(pc);;
Print("SMALL HOMOLOGY H2 START: prime=",SMALL_P,"; pc length=",n,"; runtime=",Runtime(),"\n");
modu:=GModuleByMats(List(pc,g->IdentityMat(1,GF(SMALL_P))),GF(SMALL_P));;
co:=TwoCohomology(gp,modu);;
basis:=BasisVectors(Basis(Range(co.cohom)));;
coc:=List(basis,v->PreImagesRepresentative(co.cohom,v));;
restrictions:=[];;
for v in coc do
 ext:=Extension(gp,modu,v);;ep:=Pcgs(ext);;z:=ep[n+1];;
 if SMALL_P=2 then t:=sp;else t:=rp;fi;
 tl:=MappedPcElement(t,pc,ep{[1..n]});;
 Add(restrictions,First([0..SMALL_P-1],i->z^i=tl^SMALL_P));
od;
allowed:=NullspaceMat(List(restrictions,i->[i*One(GF(SMALL_P))]));;
Print("SMALL HOMOLOGY H2: dimension=",Length(coc),"; source restrictions=",restrictions,"; allowed=",Length(allowed),"; runtime=",Runtime(),"\n");
combined:=List(allowed,row->Sum([1..Length(coc)],i->row[i]*coc[i]));;
d:=Length(combined);;
if not IsBound(SMALL_LABEL) then SMALL_LABEL:=String(SMALL_P);fi;
stream:=OutputTextFile(Concatenation("work/centralizer_code/small_homology_cover_",SMALL_LABEL,".json"),false);;
SetPrintFormattingStatus(stream,false);
PrintTo(stream,"{\"p\":",SMALL_P,",\"source_order\":",Size(gp),",\"pc\":",PCData(gp,sp,rp),",\"cocycles\":",List(combined,v->List(v,IntFFE)),",\"source_restrictions\":",restrictions,"}\n");
CloseStream(stream);
jointCoc:=Concatenation(List([1..Length(combined[1])],i->List([1..d],j->combined[j][i])));;
moduall:=GModuleByMats(List(pc,g->IdentityMat(d,GF(SMALL_P))),GF(SMALL_P));;
cover:=Extension(gp,moduall,jointCoc);;cpg:=Pcgs(cover);;
cs:=MappedPcElement(sp,pc,cpg{[1..n]});;cr:=MappedPcElement(rp,pc,cpg{[1..n]});;
if SMALL_P=2 then cr:=cr^4;else cs:=cs^3;fi;
Print("SMALL MARKED COVER CHECK: orders=",Order(cs),",",Order(cr),"; image order=",Size(Group(cs,cr)),"; full order=",Size(cover),"\n");
if cs^2<>One(cover) or cr^3<>One(cover) or Size(Group(cs,cr))<>Size(cover) then Error("small marked cover");fi;
pure:=Group((sp*rp)^-2,sp*(sp*rp)^-2*sp);;
centS:=Centralizer(pure,sp);;centR:=Centralizer(pure,rp);;
lift:=g->MappedPcElement(g,pc,cpg{[1..n]});;
ks:=List(GeneratorsOfGroup(centS),g->Comm(lift(g),cs));;
kr:=List(GeneratorsOfGroup(centR),g->Comm(lift(g),cr));;
Print("SMALL HOMOLOGY KAPPA: prime=",SMALL_P,"; elementary kernel order=",SMALL_P^d,"; kappa_s=",Size(Group(ks)),"; kappa_r=",Size(Group(kr)),"; joint=",Size(Group(Concatenation(ks,kr))),"; reduced order=",SMALL_P^d/Size(Group(Concatenation(ks,kr))),"\n");
Print("Finite refinement only; the full infinite reduced-kernel comparison is separate.\n");
QUIT_GAP(0);
fi;
