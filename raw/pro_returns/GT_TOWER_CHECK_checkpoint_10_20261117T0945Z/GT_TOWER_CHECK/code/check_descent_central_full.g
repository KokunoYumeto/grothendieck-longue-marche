# Determine the full canonical central kernel using exact PC cohomology.
CENTRAL_CONTINUE:=true;
Read("work/centralizer_code/check_descent_central2_joint.g");
e2:=cen;se2:=se;re2:=re;proj2:=proj;pe2:=Pcgs(e2);
central2gens:=GeneratorsOfGroup(Kernel(proj2));

# Every prime divisor of M divides |D|, so only 2 and 3 occur.
trivial3:=GModuleByMats(List(pd,g->IdentityMat(1,GF(3))),GF(3));
coh3:=TwoCohomology(pcD,trivial3);
basis3:=BasisVectors(Basis(Range(coh3.cohom)));
cocycles3:=List(basis3,v->PreImagesRepresentative(coh3.cohom,v));
restriction3:=[];
for v in cocycles3 do
 extCurrent:=Extension(pcD,trivial3,v);ep:=Pcgs(extCurrent);
 rr:=MappedPcElement(rrD,pd,ep{[1..Length(pd)]});
 c3:=ep[Length(pd)+1];
 Add(restriction3,First([0..2],j->c3^j=rr^3));
od;
eval3:=List(restriction3,t->[t*One(GF(3))]);
ker3:=NullspaceMat(eval3);
Print("FULL CENTRAL THREE TEST: H2 dimension=",Length(cocycles3),"; r restrictions=",restriction3,"; admissible dimension=",Length(ker3),"\n");

# Refine E2 by C2, retaining centrality over the ORIGINAL D.
n2:=Length(pe2);
trivial22:=GModuleByMats(List(pe2,g->IdentityMat(1,GF(2))),GF(2));
coh22:=TwoCohomology(e2,trivial22);
basis22:=BasisVectors(Basis(Range(coh22.cohom)));
cocycles22:=List(basis22,v->PreImagesRepresentative(coh22.cohom,v));
Print("Second central layer H2 dimension=",Length(cocycles22),"; evaluating exact centrality constraints.\n");
eval22:=[];
for v in cocycles22 do
 extCurrent:=Extension(e2,trivial22,v);ep:=Pcgs(extCurrent);nz:=Length(ep);
 ce:=ep[nz];
 lift:=g->MappedPcElement(g,pe2,ep{[1..n2]});
 ss:=lift(se2);vals:=[First([0..1],j->ce^j=ss^2)];
 for ag in central2gens do
  al:=lift(ag);
  for bg in pe2 do
   bl:=lift(bg);comm:=Comm(al,bl);
   if not comm in Group(ce) then Error("old central kernel not central modulo new kernel");fi;
   Add(vals,First([0..1],j->ce^j=comm));
  od;
 od;
 Add(eval22,List(vals,j->j*One(GF(2))));
od;
ker22:=NullspaceMat(eval22);
Print("FULL CENTRAL TWO TEST: original kernel generators=",Length(central2gens),"; H2 dimension=",Length(cocycles22),"; central-and-source admissible dimension=",Length(ker22),"\n");
if Length(ker3)=0 and Length(ker22)=0 then
 Print("CERTIFIED FULL CANONICAL COVER: M=C2^3; E2=B/[B,K]. Every candidate passed all full-cover tests.\n");
else
 Print("FURTHER CENTRAL LAYERS REQUIRED: three dimension=",Length(ker3),"; two refinement dimension=",Length(ker22),".\n");
fi;
if Length(ker3)<>1 or Length(ker22)<>0 then Error("unexpected primary ranks for next exact step");fi;
centralCocycle3:=0*cocycles3[1];
for i in [1..Length(cocycles3)] do centralCocycle3:=centralCocycle3+ker3[1][i]*cocycles3[i];od;
e3:=Extension(pcD,trivial3,centralCocycle3);pe3:=Pcgs(e3);n3:=Length(pe3);
se3:=MappedPcElement(ssD,pd,pe3{[1..Length(pd)]});se3:=se3^3;
re3:=MappedPcElement(rrD,pd,pe3{[1..Length(pd)]});
if se3^2<>One(e3) or re3^3<>One(e3) or Size(Group(se3,re3))<>Size(e3) then Error("bad marked three-cover");fi;
proj3:=GroupHomomorphismByImages(e3,pcD,AsList(pe3),Concatenation(AsList(pd),[One(pcD)]));
central3gens:=GeneratorsOfGroup(Kernel(proj3));
trivial33:=GModuleByMats(List(pe3,g->IdentityMat(1,GF(3))),GF(3));
coh33:=TwoCohomology(e3,trivial33);
basis33:=BasisVectors(Basis(Range(coh33.cohom)));
cocycles33:=List(basis33,v->PreImagesRepresentative(coh33.cohom,v));
eval33:=[];
for v in cocycles33 do
 extCurrent:=Extension(e3,trivial33,v);ep:=Pcgs(extCurrent);ce:=ep[Length(ep)];
 lift:=g->MappedPcElement(g,pe3,ep{[1..n3]});
 rr:=lift(re3);vals:=[First([0..2],j->ce^j=rr^3)];
 for ag in central3gens do
  al:=lift(ag);
  for bg in pe3 do
   comm:=Comm(al,lift(bg));
   if not comm in Group(ce) then Error("old central three-kernel not central modulo new kernel");fi;
   Add(vals,First([0..2],j->ce^j=comm));
  od;
 od;
 Add(eval33,List(vals,j->j*One(GF(3))));
od;
ker33:=NullspaceMat(eval33);
Print("FULL CENTRAL THREE EXPONENT TEST: H2 dimension=",Length(cocycles33),"; central-and-source admissible dimension=",Length(ker33),"\n");
if Length(ker33)<>0 then Error("further three-central layers required");fi;

# The two primary covers now jointly give the FULL canonical source cover.
prodCover:=DirectProduct(e2,e3);inc2:=Embedding(prodCover,1);inc3:=Embedding(prodCover,2);
sf:=Image(inc2,se2)*Image(inc3,se3);rf:=Image(inc2,re2)*Image(inc3,re3);
fullCover:=Group(sf,rf);fullPi:=GroupHomomorphismByImages(fullCover,pcD,[sf,rf],[ssD,rrD]);
if fullPi=fail or Size(fullCover)<>24*Size(pcD) then Error("bad full central cover");fi;
mf:=Kernel(fullPi);
if AbelianInvariants(mf)<>[2,2,2,3] or not IsCentral(fullCover,mf) then Error("bad full multiplier structure");fi;
qf:=GroupHomomorphismByImages(fullCover,Q,[sf,rf],[qS,qR]);
xf:=(sf*rf)^-2;yf:=sf*xf*sf;pf:=Group(xf,yf);pdf:=DerivedSubgroup(pf);
qfp:=RestrictedMapping(qf,pf);kf:=Kernel(qf);hsf:=ClosureGroup(kf,sf);hrf:=ClosureGroup(kf,rf);
Print("FULL CANONICAL SOURCE COVER: |Dc|=",Size(fullCover),"; M invariants=",AbelianInvariants(mf),"; |pure derived|=",Size(pdf),"\n");
fullRecords:=[];
for i in [1..Length(sourceCandidates)] do
 cand:=sourceCandidates[i];ff:=PreImagesRepresentative(fullPi,Image(isoD,cand.f));
 aa:=(sf*ff)^2;bb:=(ff^-1*rf)^3;obs:=aa^3*bb^2;
 cyc:=obs=One(fullCover);der:=false;frs:=false;frr:=false;aut:=false;
 if cyc then
  ff:=ff*aa*bb;
  if (sf*ff)^2<>One(fullCover) or (ff^-1*rf)^3<>One(fullCover) then Error("full central correction failed");fi;
  der:=ff in pdf;
  betaM:=Mmul(Mpow(U,2*cand.a0,12),cand.C,12);
  AM:=Mmul(Mmul(betaM,cand.H,12),Mpow(R0,-(cand.a0 mod 3),12),12);
  beta0:=PreImagesRepresentative(qfp,MatPerm(betaM,12,v12,true));
  A0:=PreImagesRepresentative(qfp,MatPerm(AM,12,v12,true));
  frs:=IsConjugate(hsf,sf,(sf*ff)^beta0);
  frr:=IsConjugate(hrf,rf,(ff^-1*rf)^A0);
  homf:=GroupHomomorphismByImages(fullCover,fullCover,[sf,rf],[sf*ff,ff^-1*rf]);
  aut:=homf<>fail and IsBijective(homf);
  if i=14 and frs and frr then
   hsWitness:=RepresentativeAction(hsf,sf,(sf*ff)^beta0);
   hrWitness:=RepresentativeAction(hrf,rf,(ff^-1*rf)^A0);
   esWitness:=First([0..1],j->qS^j=Image(qf,hsWitness));
   erWitness:=First([0..2],j->qR^j=Image(qf,hrWitness));
   hsWitness:=sf^-esWitness*hsWitness;hrWitness:=rf^-erWitness*hrWitness;
   betaWitness:=beta0*hsWitness^-1;AWitness:=A0*hrWitness^-1;fWitness:=ff;
   if not betaWitness in pf or not AWitness in pf then Error("witness frames not pure");fi;
   if betaWitness*sf*betaWitness^-1<>sf*ff or AWitness*rf*AWitness^-1<>ff^-1*rf then Error("witness frames fail literal equality");fi;
   if Image(qf,betaWitness)<>MatPerm([5,0,0,5],12,v12,true) or Image(qf,AWitness)<>MatPerm([5,0,0,5],12,v12,true) then Error("wrong witness frame residues");fi;
  fi;
 fi;
 Add(fullRecords,[i,cand.bit,cyc,der,frs,frr,aut]);
od;
Print("FULL-COVER RECORDS [candidate,Delta,cycles,derived,s residue frame,r residue frame,automorphism]: ",fullRecords,"\n");
Print("FULL-COVER SURVIVORS: ",Filtered(fullRecords,r->ForAll(r{[3..7]},b->b)),"\n");
Print("The exact full-cover lifting theorem applies to these positive automorphisms; commutator normalization changes the source by its stated inner map.\n");
PCData:=function(gr,sg,rg)
 local pg,n,conj,i,j;
 pg:=Pcgs(gr);n:=Length(pg);conj:=[];
 for i in [1..n] do for j in [1..i-1] do Add(conj,[i,j,ExponentsOfConjugate(pg,i,j)]);od;od;
 return [RelativeOrders(pg),List([1..n],i->ExponentsOfRelativePower(pg,i)),conj,ExponentsOfPcElement(pg,sg),ExponentsOfPcElement(pg,rg)];
end;
IntRows:=m->List(m,row->List(row,IntFFE));
pgfull:=Pcgs(fullCover);
certificateStream:=OutputTextFile("work/centralizer_code/check_descent_central_full_certificate.json",false);
SetPrintFormattingStatus(certificateStream,false);
PrintTo(certificateStream,
 "{\"description\":\"PC data: relative orders, power exponent rows, [i,j,conjugate exponent row], s coordinates, r coordinates. All indices in PC relations are one based.\",",
 "\"D_order\":",Size(pcD),",\"full_order\":",Size(fullCover),",\"multiplier_invariants\":",AbelianInvariants(mf),",",
 "\"base_pc\":",PCData(pcD,ssD,rrD),",\"two_cover_pc\":",PCData(e2,se2,re2),",\"three_cover_pc\":",PCData(e3,se3,re3),",\"full_cover_pc\":",PCData(fullCover,sf,rf),",",
 "\"base_H2_F2_cocycles\":",IntRows(cocycles),",\"base_s_restrictions\":",sbits,",",
 "\"base_H2_F3_cocycles\":",IntRows(cocycles3),",\"base_r_restrictions\":",restriction3,",\"base_three_kernel_basis\":",IntRows(ker3),",",
 "\"two_refinement_cocycles\":",IntRows(cocycles22),",\"two_refinement_conditions\":",IntRows(eval22),",\"two_refinement_kernel_basis\":",IntRows(ker22),",",
 "\"three_refinement_cocycles\":",IntRows(cocycles33),",\"three_refinement_conditions\":",IntRows(eval33),",\"three_refinement_kernel_basis\":",IntRows(ker33),",",
 "\"records\":",fullRecords,",\"candidate14_f\":",ExponentsOfPcElement(pgfull,fWitness),",\"candidate14_beta\":",ExponentsOfPcElement(pgfull,betaWitness),",\"candidate14_A\":",ExponentsOfPcElement(pgfull,AWitness),"}\n");
CloseStream(certificateStream);
Print("Saved exact PC presentations, cohomology cocycles, centrality matrices, and literal candidate14 frame witnesses.\n");
if not IsBound(FULL_CENTRAL_CONTINUE) or not FULL_CENTRAL_CONTINUE then QUIT_GAP(0);fi;
