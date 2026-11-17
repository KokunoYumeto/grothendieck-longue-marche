# Exact finite necessary source-frame test for C_P.
# This tests finite coboundaries, and never asserts that a survivor lifts.
# Run with GAP -q check_descent_source_frames.g.

SetInfoLevel(InfoWarning,0);
Mmul := function(A,B,n)
 return List([1..4],function(k)
  local i,j; i:=QuoInt(k-1,2)+1;j:=(k-1) mod 2+1;
  return Sum([1..2],l->A[2*(i-1)+l]*B[2*(l-1)+j]) mod n;
 end);
end;
Minv := function(A,n) return [A[4] mod n,(-A[2]) mod n,(-A[3]) mod n,A[1] mod n]; end;
Mpow := function(A,e,n)
 local ans,k; if e<0 then return Mpow(Minv(A,n),-e,n);fi;
 ans:=[1,0,0,1];for k in [1..e] do ans:=Mmul(ans,A,n);od;return ans;
end;
S:=[0,1,11,0];U:=[1,1,0,1];T:=Minv(U,12);
R0:=[0,11,1,11];I2:=[1,0,0,1];
negI:=[11,0,0,11];
v4:=Filtered(Tuples([0..3],2),v->Gcd(Gcd(v[1],v[2]),4)=1);
v3:=Filtered(Tuples([0..2],2),v->v<>[0,0]);
Canon12:=v->Minimum(v,List(v,a->(-a) mod 12));
v12:=Set(List(Filtered(Tuples([0..11],2),v->Gcd(Gcd(v[1],v[2]),12)=1),Canon12));
if Length(v4)<>12 or Length(v3)<>8 or Length(v12)<>48 then Error("vector dimensions");fi;
RowAction:=function(v,A,n) return [(v[1]*A[1]+v[2]*A[3]) mod n,(v[1]*A[2]+v[2]*A[4]) mod n];end;
MatPerm:=function(A,n,vs,projective)
 local images,v,w;images:=[];
 for v in vs do w:=RowAction(v,A,n);if projective then w:=Canon12(w);fi;
 Add(images,Position(vs,w));od;return PermList(images);
end;
Block20:=function(A)
 local p4,p3; p4:=ListPerm(MatPerm(A,4,v4,false),12);
 p3:=ListPerm(MatPerm(A,3,v3,false),8);
 return Concatenation(p4,List(p3,j->12+j));
end;

# Right-coset transversal 1,s,r,r^2,sr,sr^2 for F in B.
# The nonidentity Schreier weights at s are y^-1,x,x^-1,y.
sb:=(1,2);rb:=(1,2,3);
reps:=[(),sb,rb,rb^2,sb*rb,sb*rb^2];
weightsS:=[I2,I2,Minv(T,12),S,Minv(S,12),T];
InducedGenerator:=function(bar,weights,Qmat)
 local images,i,j,block,k;images:=[];
 for i in [1..6] do
  j:=Position(reps,reps[i]*bar);block:=Block20(weights[i]);
  for k in [1..20] do Add(images,20*(j-1)+block[k]);od;
 od;
 block:=ListPerm(MatPerm(Qmat,12,v12,true),48);
 Append(images,List(block,k->120+k));return PermList(images);
end;
sB:=InducedGenerator(sb,weightsS,S);
rB:=InducedGenerator(rb,List([1..6],i->I2),R0);
if Order(sB)<>2 or Order(rB)<>3 then Error("source presentation");fi;
xB:=(sB*rB)^-2;yB:=sB*xB*sB;
if List([1..20],i->i^xB)<>Block20(S) then Error("x Schreier marking");fi;
if List([1..20],i->i^yB)<>Block20(T) then Error("y Schreier marking");fi;
D:=Group(sB,rB);PureImage:=Group(xB,yB);
Print("Source permutation degree ",LargestMovedPoint(D),"\n");
Print("|D|=",Size(D),"; |PureImage|=",Size(PureImage),"\n");
Ep:=DerivedSubgroup(PureImage);Print("|PureImage'|=",Size(Ep),"\n");
qS:=MatPerm(S,12,v12,true);qR:=MatPerm(R0,12,v12,true);
Q:=Group(qS,qR);qh:=GroupHomomorphismByImages(D,Q,[sB,rB],[qS,qR]);
if qh=fail then Error("original modular map");fi;
qhE:=RestrictedMapping(qh,PureImage);K:=Kernel(qh);
Print("|Q|=",Size(Q),"; |K|=",Size(K),"\n");
Hs:=ClosureGroup(K,sB);Hr:=ClosureGroup(K,rB);

# Convert the two solvable conjugacy problems to pc groups once.
isoS:=IsomorphismPcGroup(Hs);isoR:=IsomorphismPcGroup(Hr);
pcS:=Range(isoS);pcR:=Range(isoR);
ss:=Image(isoS,sB);rr:=Image(isoR,rB);
isoD:=IsomorphismPcGroup(D);pcD:=Range(isoD);
ssD:=Image(isoD,sB);rrD:=Image(isoD,rB);
Print("PC groups for the source-frame and presentation problems built.\n");

G4:=Group(MatPerm(S,4,v4,false),MatPerm(T,4,v4,false));
G4p:=DerivedSubgroup(G4);
H4s:=Filtered(Tuples([0..3],4),A->(A[1]*A[4]-A[2]*A[3]) mod 4=1 and MatPerm(A,4,v4,false) in G4p);
if Length(H4s)<>12 then Error("signed order-four derived group");fi;
CRT:=function(A4,A3)
 return List([1..4],i->First([0..11],a->a mod 4=A4[i] mod 4 and a mod 3=A3[i] mod 3));
end;
TuplePerm:=function(mats,Qmat)
 local images,i,block;images:=[];
 for i in [1..6] do block:=Block20(mats[i]);Append(images,List(block,j->20*(i-1)+j));od;
 block:=ListPerm(MatPerm(Qmat,12,v12,true),48);Append(images,List(block,j->120+j));
 return PermList(images);
end;
counts:=List([1..2],i->[0,0,0,0,0]);
survivors:=[];sourceCandidates:=[];tested:=0;
H:=I2;l:=0;
for apar in [0,1] do
 C4:=Mpow(Mmul(negI,Mpow(U,2,12),12),apar,4);
 for j in [0..3] do
  C3:=Mpow(S,j,3);C:=CRT(C4,C3);
  for e in [0,1] do
   H3:=Mmul(Minv(C3,3),Mpow(negI,e,3),3);
   for H4 in H4s do
    H:=CRT(H4,H3);
    l:=First([0..2],k->Mpow(R0,k,2)=List(H,a->a mod 2));
    if l=fail then Error("cubic permutation residue");fi;
    a0:=First([0..5],a->a mod 2=apar and a mod 3=l);
    V:=Mpow(U,8*a0,12);
    fQ:=Mmul(Mmul(Mmul(Minv(S,12),V,12),S,12),Minv(V,12),12);
    mats:=[C,Minv(C,12),Mmul(Minv(H,12),Minv(C,12),12),H,
     Mmul(Mmul(Minv(S,12),Minv(H,12),12),S,12),
     Mmul(Mmul(Mmul(T,C,12),H,12),Minv(T,12),12)];
    f:=TuplePerm(mats,fQ);tested:=tested+1;
    bit:=(apar+e+j) mod 2;
    if not f in Ep then continue;fi;
    if f^sB*f<>One(D) or f^(rB^-2)*f^(rB^-1)*f<>One(D) then continue;fi;
    counts[bit+1][1]:=counts[bit+1][1]+1;
    betaM:=Mmul(Mpow(U,2*a0,12),C,12);
    AM:=Mmul(Mmul(betaM,H,12),Mpow(R0,-l,12),12);
    betaQ:=MatPerm(betaM,12,v12,true);AQ:=MatPerm(AM,12,v12,true);
    beta0:=PreImagesRepresentative(qhE,betaQ);A0:=PreImagesRepresentative(qhE,AQ);
    if beta0=fail or A0=fail then Error("pure frames missing residue");fi;
    targetS:=(sB*f)^beta0;targetR:=(f^-1*rB)^A0;
    if not targetS in Hs or not targetR in Hr then Error("frame targets outside exact groups");fi;
    passS:=IsConjugate(pcS,ss,Image(isoS,targetS));
    passR:=IsConjugate(pcR,rr,Image(isoR,targetR));
    if passS then counts[bit+1][2]:=counts[bit+1][2]+1;fi;
    if passR then counts[bit+1][3]:=counts[bit+1][3]+1;fi;
    if passS and passR then
      counts[bit+1][4]:=counts[bit+1][4]+1;
      fpc:=Image(isoD,f);
      action:=GroupHomomorphismByImages(pcD,pcD,[ssD,rrD],[ssD*fpc,fpc^-1*rrD]);
      passAction:=action<>fail and IsBijective(action);
      if passAction then counts[bit+1][5]:=counts[bit+1][5]+1;fi;
      Add(survivors,[bit,apar,j,e,l,C,H,passAction]);
      if passAction then Add(sourceCandidates,rec(bit:=bit,f:=f,a0:=a0,C:=C,H:=H));fi;
    fi;
   od;
  od;
 od;
od;
Print("Tested raw coefficient choices: ",tested,"\n");
Print("Columns: cycles+membership; positive s frame; positive r frame; both; actual finite automorphism.\n");
Print("Delta 0: ",counts[1],"\nDelta 1: ",counts[2],"\n");
Print("Survivors [Delta,a mod2,j,e,l,C,H,finite automorphism]: ",survivors,"\n");
Print("FINITE NECESSARY TEST COMPLETE; no profinite lift inferred.\n");
if not IsBound(DESCENT_CONTINUE) or not DESCENT_CONTINUE then QUIT_GAP(0);fi;
