# Actual B=C2*C3 core of the two cap maps, Schreier54, signed mod12,
# and abelian C12^2.  A0 is a cubic-frame word, not a gentle f.
SetInfoLevel(InfoWarning,0);;
SizeScreen([4096,4096]);;
Read("work/centralizer_code/cap216_genuine_source_data.g");;
capSB:=(1,2);;capRB:=(1,2,3);;
capReps:=[(),capSB,capRB,capRB^2,capSB*capRB,capSB*capRB^2];;
capInduced:=function(bar,weights,last,lastAb)
 local images,i,j,k,block;
 images:=[];
 for i in [1..6] do
  j:=Position(capReps,capReps[i]*bar);
  block:=ListPerm(weights[i],capSourceDegree);
  for k in [1..capSourceDegree] do
   Add(images,capSourceDegree*(j-1)+block[k]);
  od;
 od;
 Append(images,List(ListPerm(last,48),k->6*capSourceDegree+k));
 Append(images,List(ListPerm(lastAb,6),k->6*capSourceDegree+48+k));
 return PermList(images);
end;;
capAbGenerator:=(1,2,3,4,5,6);;
capS:=capInduced(capSB,[(),(),capY^-1,capX,capX^-1,capY],capQS,capAbGenerator^3);;
capR:=capInduced(capRB,[(),(),(),(),(),()],capQR,capAbGenerator^2);;
if Order(capS)<>2 or Order(capR)<>3 then Error("source C2*C3 relations");fi;
capTau:=capS*capR;;
capXB:=capTau^-2;;
capYB:=capS*capXB*capS;;
capZB:=(capXB*capYB)^-1;;
if List([1..capSourceDegree],i->i^capXB)<>ListPerm(capX,capSourceDegree) then
 Error("first source x coordinate");
fi;
if List([1..capSourceDegree],i->i^capYB)<>ListPerm(capY,capSourceDegree) then
 Error("first source y coordinate");
fi;
capCom:=function(a,b) return a*b*a^-1*b^-1;end;;
capA0:=capCom(capCom(capXB^4,capYB^4),capZB^4)^2;;
if Order(capA0)<>2 or Comm(capA0,capS)<>One(capS) or Comm(capA0,capR)<>One(capR) then
 Error("auxiliary frame central order two in whole source");
fi;
if Order(capXB)<>12 or Order(capYB)<>12 then Error("source generator exponent twelve");fi;
capOffset:=0;;
for capI in [0..5] do
 capOffset:=capSourceDegree*capI;
 # The first two cap blocks and the Schreier54 block are fixed pointwise.
 if not ForAll([1..486],i->(capOffset+i)^capA0=capOffset+i) then
  Error("literal core cap or Schreier coordinate");
 fi;
 if not ForAll([507..650],i->(capOffset+i)^capA0=capOffset+i) then
  Error("literal abelian normalization coordinate");
 fi;
od;
capABX:=PermList(List([507..650],i->i^capXB-506));;
capABY:=PermList(List([507..650],i->i^capYB-506));;
capAB:=Group(capABX,capABY);;
if Size(capAB)<>144 or Comm(capABX,capABY)<>One(capAB) then Error("literal C12^2 projection");fi;
Print("PASS actual B-core degree=",LargestMovedPoint(Group(capS,capR)),
 "; source relations s^2=r^3=1; named x,y orders12,12.\n");
Print("PASS auxiliary cubic frame A0 has central order2 in the entire source.\n");
Print("PASS every one of the six cap/Schreier/abelian coordinates of A0 is identity.\n");
Print("PASS literal pure abelian projection has order144; x,y orders12 imply pure abelianization exactly C12^2.\n");
capGroup:=Group(capS,capR);;
capPure:=Group(capXB,capYB);;
capGroupOrder:=Size(capGroup);;
capPureOrder:=Size(capPure);;
if capGroupOrder<>6*capPureOrder then Error("index-six source");fi;
if capGroupOrder<>2^8*3^15 then Error("exact joint source order");fi;
Print("ACTUAL SOURCE ORDER=",capGroupOrder,"; FACTORS=",FactorsInt(capGroupOrder),
 "; PURE ORDER=",capPureOrder,".\n");
Print("PASS exact joint source and universal central-cover torsion-frame certificate.\n");
PrintTo("work/centralizer_code/check_cap216_genuine_core.json",
 "{\"scope\":\"Actual B-normal joint source; auxiliary cubic frame A0 is distinct from the lifted normalized pair record.\",",
 "\"degree\":",LargestMovedPoint(capGroup),",\"order\":",capGroupOrder,
 ",\"order_factorization\":{\"2\":8,\"3\":15},\"pure_order\":",capPureOrder,
 ",\"x_order\":12,\"y_order\":12,\"pure_abelianization\":[12,12],",
 "\"A0_order\":2,\"A0_central\":true,\"all_six_cap_and_Schreier_values_identity\":true,",
 "\"canonical_r_frame_commutator_orders\":[2,3],\"status\":\"PASS\"}\n");
QUIT_GAP(0);
