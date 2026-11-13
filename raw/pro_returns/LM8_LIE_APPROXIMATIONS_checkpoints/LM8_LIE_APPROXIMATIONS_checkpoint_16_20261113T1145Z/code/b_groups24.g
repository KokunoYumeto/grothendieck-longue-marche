# Exact SmallGroups catalogue and every ordered generating pair, orders 1..24.
LoadPackage("smallgrp");;
SetPrintFormattingStatus("*stdout*",false);;
output := "b_groups24_catalogue.json";;
PrintTo(output,"{\"gap_version\":\"",GAPInfo.Version,
        "\",\"smallgrp_version\":\"",PackageInfo("smallgrp")[1].Version,
        "\",\"groups\":[");
first := true;;
for n in [1..24] do
 for k in [1..NumberSmallGroups(n)] do
  g := SmallGroup(n,k);;
  el := Elements(g);;
  if el[1] <> One(g) then Error("identity index"); fi;
  mult := List(el,a->List(el,b->Position(el,a*b)));;
  pairs := [];;
  for i in [1..n] do
   for j in [1..n] do
    if Size(Group([el[i],el[j]]))=n then Add(pairs,[i,j]); fi;
   od;
  od;
  nc := -1;;
  if IsNilpotentGroup(g) then nc:=NilpotencyClassOfGroup(g); fi;
  if not first then AppendTo(output,","); fi;
  first:=false;;
  AppendTo(output,"\n{\"order\":",n,",\"id\":",k,
    ",\"structure\":\"",StructureDescription(g),
    "\",\"derived_length\":",Length(DerivedSeriesOfGroup(g))-1,
    ",\"derived_order\":",Size(DerivedSubgroup(g)),
    ",\"nilpotence_class\":",nc,
    ",\"multiplication\":",mult,
    ",\"generating_pairs\":",pairs,"}");
 od;
od;
AppendTo(output,"]}\n");
Print("Completed all 74 groups of order at most 24 and all ordered generating pairs.\n");
QUIT;
