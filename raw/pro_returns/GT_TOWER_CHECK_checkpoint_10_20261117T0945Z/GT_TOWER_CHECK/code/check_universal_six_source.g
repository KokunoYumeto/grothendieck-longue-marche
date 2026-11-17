# Exact small finite groups controlling the universal six-source membership.
SetInfoLevel(InfoWarning,0);
ff:=FreeGroup("s","r");; fs:=ff.1;;fr:=ff.2;;
triangle2:=ff/[fs^2,fr^3,(fs*fr)^2];;
triangle3:=ff/[fs^2,fr^3,(fs*fr)^3];;
Print("Triangle orders: ",Size(triangle2),",",Size(triangle3),"\n");
if Size(triangle2)<>6 or Size(triangle3)<>12 then Error("triangle order");fi;

# Dic_3, represented by right multiplication on a^i b^j,
# a^6=1, b^2=a^3, b a b^-1=a^-1.
pair:=function(i,j) return 1+(i mod 6)+6*j;end;;
bb:=PermList(Concatenation(List([0..5],i->pair(i,1)),List([0..5],i->pair(i+3,0))));;
rr:=PermList(Concatenation(List([0..5],i->pair(i+2,0)),List([0..5],i->pair(i-2,1))));;
dic:=Group(bb,rr);;
mm:=SL(2,3);;im:=IsomorphismPermGroup(mm);;
S:=Image(im,[[0,1],[-1,0]]*One(GF(3)));;
R:=Image(im,[[0,-1],[1,-1]]*One(GF(3)));;
sl:=Image(im);;
prod:=DirectProduct(sl,dic);;
e1:=Embedding(prod,1);;e2:=Embedding(prod,2);;
diag:=Group(Image(e1,S^2)*Image(e2,bb^2));;
quot:=NaturalHomomorphismByNormalSubgroup(prod,diag);;
markedS:=Image(quot,Image(e1,S)*Image(e2,bb));;
markedR:=Image(quot,Image(e1,R)*Image(e2,rr));;
gg:=Group(markedS,markedR);;
Print("Marked central product: |G|=",Size(gg),"; generator orders=",Order(markedS),",",Order(markedR),"; abelian invariants=",AbelianInvariants(gg),"\n");
if Size(gg)<>144 or Order(markedS)<>2 or Order(markedR)<>3 then Error("bad marked product");fi;
tt:=markedS*markedR;;
nn2:=NormalClosure(gg,Group(tt^2));;nn3:=NormalClosure(gg,Group(tt^3));;
Print("Normal peripheral powers: |N2|=",Size(nn2),"; |N3|=",Size(nn3),"; intersection=",Size(Intersection(nn2,nn3)),"; commutator=",Size(CommutatorSubgroup(nn2,nn3)),"\n");
PCData:=function(gr,sg,rg)
 local pg,n,conj,i,j;
 pg:=Pcgs(gr);n:=Length(pg);conj:=[];
 for i in [1..n] do for j in [1..i-1] do Add(conj,[i,j,ExponentsOfConjugate(pg,i,j)]);od;od;
 return [RelativeOrders(pg),List([1..n],i->ExponentsOfRelativePower(pg,i)),conj,ExponentsOfPcElement(pg,sg),ExponentsOfPcElement(pg,rg)];
end;;
q72:=NaturalHomomorphismByNormalSubgroup(gg,Intersection(nn2,nn3));;
group72:=Image(q72);;
records:=[];;pcRecords:=[];;
for datum in [[group72,Image(q72,markedS),Image(q72,markedR)],[gg,markedS,markedR]] do
 ip:=IsomorphismPcGroup(datum[1]);;gp:=Image(ip);;pc:=Pcgs(gp);;
 ss:=Image(ip,datum[2]);;rs:=Image(ip,datum[3]);;
 Add(pcRecords,[Size(gp),PCData(gp,ss,rs)]);
 for prime in [2,3] do
  modul:=GModuleByMats(List(pc,g->IdentityMat(1,GF(prime))),GF(prime));;
  cohom:=TwoCohomology(gp,modul);;
  basis:=BasisVectors(Basis(Range(cohom.cohom)));;
  coc:=List(basis,v->PreImagesRepresentative(cohom.cohom,v));;
  restrictions:=[];;
  for v in coc do
   ext:=Extension(gp,modul,v);;ep:=Pcgs(ext);;central:=ep[Length(pc)+1];;
   if prime=2 then torsion:=ss;else torsion:=rs;fi;
   lifted:=MappedPcElement(torsion,pc,ep{[1..Length(pc)]});;
   Add(restrictions,First([0..prime-1],j->central^j=lifted^prime));
  od;
  rankRestriction:=RankMat(List(restrictions,t->[t*One(GF(prime))]));;
  Print("Base order=",Size(gp),"; H2(F",prime,") dimension=",Length(coc),"; source restrictions=",restrictions,"; admissible dimension=",Length(coc)-rankRestriction,"\n");
  Add(records,[Size(gp),prime,Length(coc),rankRestriction,List(coc,v->List(v,IntFFE)),restrictions]);
 od;
od;
stream:=OutputTextFile("work/centralizer_code/check_universal_six_source_certificate.json",false);;
SetPrintFormattingStatus(stream,false);
PrintTo(stream,"{\"pc_presentations\":",pcRecords,",\"cohomology_source_restrictions\":",records,"}\n");
CloseStream(stream);

# The six actual F-word evaluations modulo the order-144 group.
product6:=DirectProduct(List([1..6],i->gg));;
valsX:=[markedS,tt,tt,markedR^-1,markedS,markedS*markedR^-1*markedS];;
valsY:=[tt,markedS,markedR^-1,markedS,markedS*markedR^-1*markedS,tt];;
jx:=Product([1..6],i->Image(Embedding(product6,i),valsX[i]));;
jy:=Product([1..6],i->Image(Embedding(product6,i),valsY[i]));;
joint:=Group(jx,jy);;jointDerived:=DerivedSubgroup(joint);;
Print("Actual six-coordinate finite image: order=",Size(joint),"; derived order=",Size(jointDerived),"; abelian invariants=",AbelianInvariants(joint),"; ambient index=",Index(product6,joint),"\n");
Print("Finished finite small-source checks.\n");
if not IsBound(UNIVERSAL_CONTINUE) or not UNIVERSAL_CONTINUE then QUIT_GAP(0);fi;
