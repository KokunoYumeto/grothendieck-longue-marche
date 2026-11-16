"""Use the finite-base commutation bound and class-two suffix directly."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
source_collector = HERE / "pbc_central_collector.g"
c = source_collector.read_text().replace(
    "PBC_CentralCollect:=", "PBC_CentralCollectV2:="
)
c = c.replace(
    "if stp > 1 and sst[stp] = 1 and g = com[g] then",
    "if stp > 1 and sst[stp] = 1 and g = com[g] and g > baseN then",
)
a = c.index("                ##  Now reduce.")
b = c.index("                west[ stp ] := 0;", a)
c = c[:a] + (
    "                # Every index in this branch is an infinite-order\n"
    "                # central tail.  There is no exponent to reduce.\n\n"
) + c[b:]
needle = "            elif g = com[g] then\n                # move generator directly"
assert needle in c
c = c.replace(needle, r'''
            elif g = com[g] then
                # The finite suffix commutes modulo the central tails.
                # Insert its whole current exponent using the central
                # bilinear correction, then keep its base exponent.
                if g<=baseN then
                    for hh in [g+1..baseN] do
                        if ev[hh]<>0 and IsBound(centralConj[hh][g]) then
                            for tt in [1,3..Length(centralConj[hh][g])-1] do
                                ev[centralConj[hh][g][tt]] :=
                                  ev[centralConj[hh][g][tt]] +
                                  est[stp]*ev[hh]*centralConj[hh][g][tt+1];
                            od;
                        fi;
                    od;
                fi;
                # move generator directly''')
collector = HERE / "pbc_central_collector_v2.g"
collector.write_text(c)

source_witness = HERE / "pbc_hermite_shortcut_witness.g"
s = source_witness.read_text()
s = s.replace("pbc_central_collector.g", "pbc_central_collector_v2.g")
s = s.replace("PBC_CentralCollect(", "PBC_CentralCollectV2(")
s = s.replace("PBC_HermiteShortcutWitness:=", "PBC_HermiteShortcutV2Witness:=")
s = s.replace(
    "originalConjugates,collectShortcut;",
    "originalConjugates,collectShortcut,baseCommute,zz,hh;",
)
needle = " coll![PC_COMMUTE]:=Concatenation(ListWithIdenticalEntries(n,n),[n+1..n+m]);"
assert s.count(needle) == 2
s = s.replace(needle, r'''
 # This is exactly the usual commutation bound of the FINITE base
 # presentation.  Deleted formal commutators are accounted for by
 # PBC_CentralCollectV2, including in the class-two suffix.
 baseCommute:=ListWithIdenticalEntries(n,n);
 for zz in [n-1,n-2..1] do
  hh:=n;
  while hh>baseCommute[zz+1] and baseconjs[hh][zz]=[hh,1] do hh:=hh-1;od;
  if hh=zz+1 and baseconjs[hh][zz]=[hh,1] then baseCommute[zz]:=zz;
  else baseCommute[zz]:=hh;fi;
 od;
 coll![PC_COMMUTE]:=Concatenation(baseCommute,[n+1..n+m]);''', 1)
s = s.replace(needle, " coll![PC_COMMUTE]:=Concatenation(baseCommute,[n+1..n+m]);")
witness = HERE / "pbc_hermite_shortcut_v2_witness.g"
witness.write_text(s)
metadata = {
    "source_collector_sha256": hashlib.sha256(source_collector.read_bytes()).hexdigest(),
    "source_witness_sha256": hashlib.sha256(source_witness.read_bytes()).hexdigest(),
    "collector_sha256": hashlib.sha256(collector.read_bytes()).hexdigest(),
    "witness_sha256": hashlib.sha256(witness.read_bytes()).hexdigest(),
    "rule": "finite-base commutation plus exact central bilinear correction",
    "central_bulk_branch": "only infinite-order central tails; no unnecessary reduction scan",
}
(HERE / "pbc_central_shortcut_v2_generation.json").write_text(json.dumps(metadata, indent=2) + "\n")
print(json.dumps(metadata, indent=2))
