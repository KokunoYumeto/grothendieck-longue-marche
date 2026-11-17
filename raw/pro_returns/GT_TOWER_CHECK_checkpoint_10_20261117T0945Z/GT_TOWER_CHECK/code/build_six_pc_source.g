# Actual induced six-coordinate source, entirely in pc groups.
BuildSixPcSource:=function(tg,ts,tr)
 local iso,tpc,a,b,base,bgens,topi,top,bs,br,trans,pi,as,ar,
       imgs,perm,i,j,g,auts,action,wreath,et,eb,weights,ws,ss,rr,source,sx,sy,vx,vy;
 iso:=IsomorphismPcGroup(tg);tpc:=Image(iso);a:=Image(iso,ts);b:=Image(iso,tr);
 base:=DirectProduct(List([1..6],i->tpc));
 bgens:=Concatenation(List([1..6],i->List(GeneratorsOfGroup(tpc),z->Image(Embedding(base,i),z))));
 topi:=IsomorphismPcGroup(Group((1,2),(1,2,3)));top:=Image(topi);
 bs:=Image(topi,(1,2));br:=Image(topi,(1,2,3));
 trans:=[One(top),bs,br,br^2,bs*br,bs*br^2];auts:=[];
 for g in [bs,br] do
  imgs:=[];
  for i in [1..6] do
   j:=Position(trans,trans[i]*g);
   Append(imgs,List(GeneratorsOfGroup(tpc),z->Image(Embedding(base,j),z)));
  od;
  Add(auts,GroupHomomorphismByImages(base,base,bgens,imgs));
 od;
 if not ForAll(auts,a->a<>fail and IsBijective(a)) then Error("pc coordinate automorphisms");fi;
 action:=GroupHomomorphismByImages(top,Group(auts),[bs,br],auts);
 if action=fail then Error("pc coordinate action");fi;
 wreath:=SemidirectProduct(top,action,base);
 et:=Embedding(wreath,1);eb:=Embedding(wreath,2);
 weights:=[One(tpc),One(tpc),(a*b)^-1,a,a^-1,a*b];
 ws:=Product([1..6],i->Image(Embedding(base,i),weights[i]));
 ss:=Image(eb,ws)*Image(et,bs);rr:=Image(et,br);
 source:=Group(ss,rr);
 if ss^2<>One(wreath) or rr^3<>One(wreath) then Error("pc induced torsion marking");fi;
 sx:=PreImagesRepresentative(eb,(ss*rr)^-2);
 sy:=PreImagesRepresentative(eb,ss*(ss*rr)^-2*ss);
 vx:=List([1..6],i->Image(Projection(base,i),sx));
 vy:=List([1..6],i->Image(Projection(base,i),sy));
 if vx<>[a,a*b,a*b,b^-1,a,a*b^-1*a] or vy<>[a*b,a,b^-1,a,a*b^-1*a,a*b] then Error("pc source six exact coordinate markings");fi;
 return rec(group:=source,s:=ss,r:=rr,ambient:=wreath,base:=base,base_embedding:=eb,target:=tpc,target_s:=a,target_r:=b);
end;;
