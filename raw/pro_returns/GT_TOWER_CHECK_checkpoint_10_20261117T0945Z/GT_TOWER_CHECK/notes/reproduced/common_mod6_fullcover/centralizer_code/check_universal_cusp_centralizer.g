# The actual pure cusp-centralizer image, using full target centralizers.
UNIVERSAL_CONTINUE:=true;;
Read("work/centralizer_code/check_universal_six_source.g");;
cuspRows:=[];;
for ei in [0..1] do
 for ti in [0..11] do
  for li in [0..2] do
   values:=[markedS^ei,tt^ti,tt^ti,markedR^li,markedS^ei,tt*markedR^li*tt^-1];;
   element:=Product([1..6],i->Image(Embedding(product6,i),values[i]));;
   if element in joint then Add(cuspRows,[ei,ti,li]);fi;
  od;
 od;
od;
if Length(cuspRows)<>12 or not ForAll(cuspRows,v->v[1]=v[2] mod 2 and v[3]=(-v[2]) mod 3) then Error("exact full cusp-centralizer residues");fi;
Print("ACTUAL CUSP-CENTRALIZER coordinate residues [e,t,l]: ",cuspRows,"\n");
Print("Residue count=",Length(cuspRows),"; precisely source x powers=",Length(cuspRows)=12 and ForAll(cuspRows,v->v[1]=v[2] mod 2 and v[3]=(-v[2]) mod 3),"\n");
QUIT_GAP(0);
