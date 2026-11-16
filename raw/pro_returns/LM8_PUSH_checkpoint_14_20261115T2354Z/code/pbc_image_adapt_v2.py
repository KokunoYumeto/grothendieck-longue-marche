"""Rewrite the exact cached finite source in a boundary-adapted pc basis.

The triangular basis change preserves every subgroup of the original pc
chain.  This uses GAP's native finite pc collector only to compute the new
finite defining words; it does not compute or assert any central lift.
"""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
source_path = HERE / "pbc_iterated_joint_pc.json"
centralizers_path = HERE / "pbc_iterated_centralizers_kernel.json"
source = json.loads(source_path.read_text())
centralizers = json.loads(centralizers_path.read_text())
n = len(source["relative_orders"])

def gap(value):
    return json.dumps(value, separators=(",", ":"))

lines = [
    'LoadPackage("polycyclic");;',
    f'PBC_orders:={gap(source["relative_orders"])};;',
    f'PBC_free:=FreeGroup({n});;',
    'PBC_family:=FamilyObj(PBC_free.1);;',
    'PBC_rws:=SingleCollector(PBC_free,PBC_orders);;',
]
for i, word in enumerate(source["powers"], 1):
    lines.append(f'SetPower(PBC_rws,{i},ObjByExtRep(PBC_family,{gap(word)}));;')
for i, j, word in source["conjugates"]:
    lines.append(f'SetConjugate(PBC_rws,{i},{j},ObjByExtRep(PBC_family,{gap(word)}));;')
lines += [
    'PBC_Native:=GroupByRwsNC(PBC_rws);;',
    'PBC_old:=Pcgs(PBC_Native);;',
    f'Assert(0,Size(PBC_Native)={source["order"]});',
    'Assert(0,RelativeOrders(PBC_old)=PBC_orders);',
    'PBC_eval:=function(w) local e,i;e:=ListWithIdenticalEntries(Length(PBC_old),0);'
    'for i in [1,3..Length(w)-1] do e[w[i]]:=w[i+1];od;'
    'return PcElementByExponents(PBC_old,e);end;;',
]
for key in ["s", "r", "f", "bs", "br"]:
    lines.append(f'PBC_{key}:=PBC_eval({gap(source[key])});;')
lines += [
    'PBC_bs:=PBC_bs^-1;;PBC_br:=PBC_br^-1;;',
    'PBC_s_image:=PBC_s*PBC_f^-1;;PBC_r_image:=PBC_f*PBC_r;;',
    'PBC_hs:=PBC_s^-1*PBC_s_image;;PBC_hr:=PBC_r^-1*PBC_r_image;;',
    f'PBC_cs:=List({gap(centralizers["s_generators"])},PBC_eval);;',
    f'PBC_cr:=List({gap(centralizers["r_generators"])},PBC_eval);;',
    'Assert(0,PBC_bs*PBC_s*PBC_bs^-1=PBC_s*PBC_f^-1);',
    'Assert(0,PBC_br*PBC_r*PBC_br^-1=PBC_f*PBC_r);',
    'Assert(0,ForAll(PBC_cs,g->Comm(g,PBC_s)=One(PBC_Native)));',
    'Assert(0,ForAll(PBC_cr,g->Comm(g,PBC_r)=One(PBC_Native)));',
    'Print("native_source_and_frames_verified ",Size(PBC_Native)," runtime ",Runtime(),"\\n");',
    'PBC_new:=ShallowCopy(AsList(PBC_old));;PBC_used:=[];;PBC_changes:=[];;',
    'PBC_replace:=function(h,label) local v,i,u;'
    'v:=ExponentsOfPcElement(PBC_old,h);i:=PositionProperty(v,a->a<>0);'
    'if i=fail or i in PBC_used then return;fi;'
    'u:=First([1..PBC_orders[i]-1],q->q*v[i] mod PBC_orders[i]=1);'
    'Assert(0,u<>fail);PBC_new[i]:=h^u;AddSet(PBC_used,i);'
    'Add(PBC_changes,[i,label,u]);end;;',
    'PBC_replace(PBC_r,1);PBC_replace(PBC_s,2);'
    'PBC_replace(PBC_bs,3);PBC_replace(PBC_br,4);',
    'PBC_replace(PBC_hr,5);PBC_replace(PBC_hs,6);',
    'for PBC_i in [1..Length(PBC_cs)] do PBC_replace(PBC_cs[PBC_i],1000+PBC_i);od;',
    'for PBC_i in [1..Length(PBC_cr)] do PBC_replace(PBC_cr[PBC_i],2000+PBC_i);od;',
    'PBC_old_vectors:=List(PBC_new,g->ExponentsOfPcElement(PBC_old,g));;',
    f'for PBC_i in [1..{n}] do PBC_v:=PBC_old_vectors[PBC_i];'
    'Assert(0,PBC_v[PBC_i]=1 and ForAll(PBC_v{[1..PBC_i-1]},a->a=0));od;',
    'PBC_newpc:=InducedPcgsByPcSequenceNC(PBC_old,PBC_new);;',
    'Assert(0,RelativeOrders(PBC_newpc)=PBC_orders);',
    'PBC_invs:=List([1..Length(PBC_new)],i->List([0..PBC_orders[i]-1],e->PBC_new[i]^-e));;',
    'PBC_word:=function(el) local h,d,e,w;h:=el;w:=[];'
    'while not IsOne(h) do d:=DepthOfPcElement(PBC_old,h);'
    'e:=ExponentOfPcElement(PBC_old,h,d);'
    'Assert(0,e>0 and e<PBC_orders[d]);Append(w,[d,e]);'
    'h:=PBC_invs[d][e+1]*h;od;return w;end;;',
    'Print("native_triangular_basis_verified ",Length(PBC_changes)," runtime ",Runtime(),"\\n");',
    'PBC_powers:=[];;PBC_conjugates:=[];;',
    'for PBC_i in [1..Length(PBC_new)] do',
    ' Add(PBC_powers,PBC_word(PBC_new[PBC_i]^PBC_orders[PBC_i]));',
    ' for PBC_j in [1..PBC_i-1] do',
    '  Add(PBC_conjugates,[PBC_i,PBC_j,'
    'PBC_word(PBC_invs[PBC_j][2]*PBC_new[PBC_i]*PBC_new[PBC_j])]);',
    ' od;',
    ' if PBC_i mod 10=0 then Print("native_adapted_relations ",PBC_i," runtime ",Runtime(),"\\n");fi;',
    'od;',
    'PrintTo("LM8_PUSH/code/pbc_iterated_image_adapted_v2_pc.json",'
    '"{\\n\\"order\\":",Size(PBC_Native),'
    '",\\n\\"relative_orders\\":",PBC_orders,'
    '",\\n\\"powers\\":",PBC_powers,'
    '",\\n\\"conjugates\\":",PBC_conjugates,'
    '",\\n\\"s\\":",PBC_word(PBC_s),'
    '",\\n\\"r\\":",PBC_word(PBC_r),'
    '",\\n\\"f\\":",PBC_word(PBC_f),'
    '",\\n\\"left_s_frame\\":",PBC_word(PBC_bs),'
    '",\\n\\"left_r_frame\\":",PBC_word(PBC_br),'
    '",\\n\\"s_centralizers\\":",List(PBC_cs,PBC_word),'
    '",\\n\\"r_centralizers\\":",List(PBC_cr,PBC_word),'
    '",\\n\\"basis_old_vectors\\":",PBC_old_vectors,'
    '",\\n\\"basis_changes\\":",PBC_changes,'
    '",\\n\\"s_image\\":",PBC_word(PBC_s_image),'
    '",\\n\\"r_image\\":",PBC_word(PBC_r_image),"\\n}\\n");',
    'Print("native_adapted_source_saved runtime ",Runtime(),"\\n");',
    'QUIT;',
]
(HERE / "pbc_image_adapt_v2.g").write_text("\n".join(lines) + "\n")
metadata = {
    "purpose": "exact finite pc-basis change only; no central-lift assertion",
    "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
    "centralizers_sha256": hashlib.sha256(centralizers_path.read_bytes()).hexdigest(),
    "generated_gap_sha256": hashlib.sha256((HERE / "pbc_image_adapt_v2.g").read_bytes()).hexdigest(),
}
(HERE / "pbc_image_adapt_v2_inputs.json").write_text(json.dumps(metadata, indent=2) + "\n")
print(json.dumps(metadata, indent=2))
