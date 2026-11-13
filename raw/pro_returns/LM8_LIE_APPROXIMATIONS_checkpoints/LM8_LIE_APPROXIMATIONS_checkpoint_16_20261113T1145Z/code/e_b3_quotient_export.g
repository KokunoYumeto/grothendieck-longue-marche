# GAP 4.15.1 and LINS 0.9. Exhaustive marked B3 quotients of order <=1000.
# LINS enumerates normal kernels, not just abstract target isomorphism types.
if LoadPackage("LINS")<>true then Error("LINS is required"); fi;
if LoadPackage("SmallGrp")<>true then Error("SmallGrp is required"); fi;
SetInfoLevel(InfoLINS,0);
f:=FreeGroup("a","b");;
g:=f/[f.1*f.2*f.1/(f.2*f.1*f.2)];;
started:=Runtime();;
Print("LINS version ",PackageInfo("LINS")[1].Version,
      "; GAP ",GAPInfo.Version,"; bound 1000\n");
graph:=LowIndexNormalSubgroupsSearchForAll(g,1000);;
nodes:=List(graph);;
Print("COMPLETE_KERNEL_ENUMERATION count=",Length(nodes),
      " milliseconds=",Runtime()-started,"\n");
Print("INDEX_COUNTS ",Collected(List(nodes,Index)),"\n");
out:=OutputTextFile("LM8_LIE_APPROXIMATIONS/code/e_b3_quotients_complete.json",false);;
SetPrintFormattingStatus(out,false);
PrintTo(out,"{\"bound\":1000,\"GAP\":\"",GAPInfo.Version,
    "\",\"LINS\":\"",PackageInfo("LINS")[1].Version,
    "\",\"kernel_count\":",Length(nodes),",\"quotients\":[");
for j in [1..Length(nodes)] do
  h:=Grp(nodes[j]);;
  tab:=CosetTable(g,h);;
  CheckCosetTableFpGroup(g,tab);
  aa:=PermList(tab[1]);; bb:=PermList(tab[3]);;
  q:=Group(aa,bb);;
  Assert(0,Size(q)=Index(nodes[j]));
  Assert(0,aa*bb*aa=bb*aa*bb);
  pure:=Subgroup(q,[aa^2,bb^2,bb*aa^2/bb]);;
  Assert(0,IsNormal(q,pure));
  if IdGroupsAvailable(Size(q)) then qid:=String(IdGroup(q)); else qid:="null"; fi;
  if j>1 then PrintTo(out,","); fi;
  PrintTo(out,"{\"index\":",Size(q),",\"smallgroup_id\":",qid,
    ",\"pure_image_order\":",Size(pure),
    ",\"kernel_contained_in_PB3\":",Index(q,pure)=6,
    ",\"a_permutation\":",tab[1],
    ",\"b_permutation\":",tab[3],"}");
  if j mod 100=0 then Print("exported ",j," kernels\n");fi;
od;
PrintTo(out,"]}");CloseStream(out);
Print("FINISHED milliseconds=",Runtime()-started,"\n");
QUIT_GAP(0);
