# A triangular change of the already verified finite pc basis.  Replacing
# g_i by h_i in g_i^u<G_{i+1}> with u a unit modulo the relative prime order
# preserves every subgroup in the pc chain and gives the same finite group.
# Prefer the actual torsion generators, frames and centralizer generators,
# so their formal lifts are short words before consistency is imposed.
PBC_AdaptWitnessBasis:=function(G,s,r,bs,br,cs,cr)
 local old,new,orders,used,chosen,replace,h,e,i,j,u,H;
 old:=Igs(G);new:=ShallowCopy(old);orders:=List(old,RelativeOrderPcp);used:=[];chosen:=[];
 replace:=function(h,label)
  local v,i,u;
  v:=ExponentsByIgs(old,h);i:=PositionProperty(v,a->a<>0);
  if i=fail or i in used then return;fi;
  u:=First([1..orders[i]-1],q->(q*v[i]) mod orders[i]=1);Assert(0,u<>fail);
  new[i]:=h^u;AddSet(used,i);Add(chosen,[i,label,u]);
 end;
 replace(r,1);replace(s,2);replace(bs,3);replace(br,4);
 for i in [1..Length(cs)] do replace(cs[i],1000+i);od;
 for i in [1..Length(cr)] do replace(cr[i],2000+i);od;
 for i in [1..Length(old)] do
  e:=ExponentsByIgs(old,new[i]);Assert(0,e[i]=1 and ForAll(e{[1..i-1]},a->a=0));
 od;
 H:=SubgroupByIgs(G,new);Assert(0,Size(H)=Size(G));
 Print("adapted_pc_basis ",Length(chosen)," replacements runtime ",Runtime(),"\n");
 return rec(group:=H,changes:=chosen,old_vectors:=List(new,h->ExponentsByIgs(old,h)));
end;;
