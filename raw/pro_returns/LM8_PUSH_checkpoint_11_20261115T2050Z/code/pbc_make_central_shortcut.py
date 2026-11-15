"""Prepare a central-commutator shortcut for positive formal collection.

Derived from the Polycyclic 2.18 library collector shipped with GAP 4.16.1;
the upstream source and its hash are recorded below.  The original package
copyright and license apply to the copied collector implementation.

When g_h^g_i = g_h*t with t central, insertion of one g_i contributes
t^(a_h) and leaves the base g_h exponent in place.  These central
contributions commute with every other step of collection.
"""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
upstream = ROOT / "gap-runtime/gap-4.16.1/pkg/polycyclic-2.18/gap/basic/colftl.gi"
raw = upstream.read_text()
end = raw.index("\nend );") + len("\nend );")
collector = raw[:end]
collector = collector.replace(
    'BindGlobal( "CollectPolycyclicGap", function( pcp, ev, w )',
    "PBC_CentralCollect:=function(pcp,ev,w,baseN,centralConj)",
)
collector = collector.rsplit("end );", 1)[0] + "end;;\n"
collector = collector.replace("icnj,  hh;", "icnj,  hh, moveSign, tt;")
collector = collector.replace(
    "est[stp] := est[stp] - 1;",
    "est[stp] := est[stp] - 1;moveSign:=1;",
)
collector = collector.replace(
    "est[stp] := est[stp] + 1;",
    "est[stp] := est[stp] + 1;moveSign:=-1;",
)
needle = "                h := com[g];"
assert needle in collector
collector = collector.replace(needle, r'''
                # The deleted conjugates have unchanged finite base
                # generator and only a central correction.  Insert that
                # correction once for every old higher-generator copy.
                if g<=baseN then
                    for hh in [g+1..baseN] do
                        if ev[hh]<>0 and IsBound(centralConj[hh][g]) then
                            for tt in [1,3..Length(centralConj[hh][g])-1] do
                                ev[centralConj[hh][g][tt]] :=
                                  ev[centralConj[hh][g][tt]] +
                                  moveSign*ev[hh]*centralConj[hh][g][tt+1];
                            od;
                        fi;
                    od;
                fi;
''' + needle)
collector_path = HERE / "pbc_central_collector.g"
collector_path.write_text(
    "# Derived from GAP 4.16.1 / Polycyclic 2.18 colftl.gi.\n"
    "# Original package copyright/license apply; see generation metadata.\n"
    + collector
)

source = HERE / "pbc_hermite_difference_witness.g"
s = source.read_text().replace(
    "PBC_HermiteDifferenceWitness:=function",
    "PBC_HermiteShortcutWitness:=function",
)
s = s.replace(
    'Read("LM8_PUSH/code/pbc_sparse_schur.g");;',
    'Read("LM8_PUSH/code/pbc_sparse_schur.g");;\n'
    'Read("LM8_PUSH/code/pbc_central_collector.g");;',
)
s = s.replace(
    "currentRelation,centralDifference;",
    "currentRelation,centralDifference,centralConj,originalConjugates,collectShortcut;",
)
needle = " makevec:=function(w)"
assert needle in s
s = s.replace(needle, r'''
 centralConj:=List([1..n],i->[]);
 originalConjugates:=List([1..n],i->[]);
 for i in [1..n] do for j in [1..i-1] do
  e:=ShallowCopy(GetConjugate(coll,i,j));originalConjugates[i][j]:=e;
  if baseconjs[i][j]=[i,1] then
   Assert(0,e{[1,2]}=[i,1] and ForAll([3,5..Length(e)-1],k->e[k]>n));
   centralConj[i][j]:=e{[3..Length(e)]};
   SetConjugate(coll,i,j,[i,1]);
  fi;
 od;od;
 coll![PC_COMMUTE]:=Concatenation(ListWithIdenticalEntries(n,n),[n+1..n+m]);
 SetFilterObj(coll,IsUpToDatePolycyclicCollector);
 collectShortcut:=function(v,w)
  return PBC_CentralCollect(coll,v,w,n,centralConj);
 end;
''' + needle)
s = s.replace("CollectWordOrFail(coll,", "collectShortcut(")
s = s.replace("cw:=GetConjugate(coll,ll,mm);", "cw:=originalConjugates[ll][mm];")
destination = HERE / "pbc_hermite_shortcut_witness.g"
destination.write_text(s)
metadata = {
    "upstream": str(upstream.relative_to(ROOT)),
    "upstream_sha256": hashlib.sha256(upstream.read_bytes()).hexdigest(),
    "collector_sha256": hashlib.sha256(collector_path.read_bytes()).hexdigest(),
    "witness_input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "witness_output_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
    "exact_rule": "g_h^g_i=g_h*t central implies g_h^a*g_i=g_i*g_h^a*t^a",
    "scope": "an exact collection path in the original centralized presentation",
}
(HERE / "pbc_central_shortcut_generation.json").write_text(json.dumps(metadata, indent=2) + "\n")
print(json.dumps(metadata, indent=2))
