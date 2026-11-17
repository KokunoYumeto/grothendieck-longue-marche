# A uniform finite word-membership test, with both free frame exponents.
UNIVERSAL_CONTINUE:=true;;
Read("work/centralizer_code/check_universal_six_source.g");;
targetX:=tt^-2;;targetY:=markedS*targetX*markedS;;
targetPure:=Group(targetX,targetY);;
targetDerived:=DerivedSubgroup(targetPure);;
Print("Target pure image: order=",Size(targetPure),"; derived order=",Size(targetDerived),"; abelian invariants=",AbelianInvariants(targetPure),"\n");
if Size(targetPure)<>24 or Size(targetDerived)<>8 then Error("target pure image orders");fi;
if not targetX*targetY^-1 in targetDerived then Error("target pure abelian generators");fi;
printfail:=[];;recordsFrames:=[];;targetFrameCount:=0;;sourceFrameCandidates:=[];;
for beta in Elements(targetPure) do
 for AA in Elements(targetDerived) do
  ssimage:=beta*markedS*beta^-1;;rrimage:=AA*markedR*AA^-1;;
  if ssimage*rrimage<>tt then continue;fi;
  aut:=GroupHomomorphismByImages(gg,gg,[markedS,markedR],[ssimage,rrimage]);;
  if aut=fail or not IsBijective(aut) then continue;fi;
  targetFrameCount:=targetFrameCount+1;
  uu:=First([0..2],i->beta*targetX^(-2*i) in targetDerived);;
  if uu=fail then Error("target harmonic abelianization");fi;
  residue:=(3-uu) mod 3;;passes:=[];;
  for apar in [residue,residue+3] do
   CC:=targetX^-apar*beta;;JJ:=beta^-1*AA*markedR^residue;;
   vals:=[CC,CC^-1,JJ^-1*CC^-1,JJ,markedS*JJ^-1*markedS,tt*CC*JJ*tt^-1];;
   tuple:=Product([1..6],i->Image(Embedding(product6,i),vals[i]));;
   Add(passes,tuple in jointDerived);
   if tuple in jointDerived then Add(sourceFrameCandidates,rec(beta:=beta,A:=AA,a:=apar,l:=residue,values:=vals));fi;
  od;
  Add(recordsFrames,[targetFrameCount,uu,residue,passes]);
  if not ForAny(passes,b->b) then Add(printfail,targetFrameCount);fi;
 od;
od;
if targetFrameCount<>24 then Error("finite target frame count");fi;
if not ForAll(recordsFrames,z->Number(z[4],b->b)=1) then Error("unique exponent membership");fi;
if Number(recordsFrames,z->z[4][1])<>12 or Number(recordsFrames,z->z[4][2])<>12 then Error("exponent parity counts");fi;
if not ForAll([0..2],u->Number(recordsFrames,z->z[2]=u)=8) then Error("target residue counts");fi;
Print("UNIFORM FINITE FRAME MEMBERSHIP: target positive normalized frame count=",targetFrameCount,"; no-exponent survivors=",Length(printfail),"; exact records=",recordsFrames,"\n");
Print("Only the actual six-word commutator membership has been tested; no full positive source lift is asserted.\n");
if not IsBound(UNIVERSAL_FRAMES_CONTINUE) or not UNIVERSAL_FRAMES_CONTINUE then QUIT_GAP(0);fi;
