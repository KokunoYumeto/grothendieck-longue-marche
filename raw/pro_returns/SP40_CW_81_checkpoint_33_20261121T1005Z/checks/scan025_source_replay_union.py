#!/usr/bin/env python3
"""Exact source-only union audit, using frozen original text as authority."""
from pathlib import Path
from collections import Counter
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"out/checks"
u_path=OUT/"scan025_source_union_v01.json"
s_path=OUT/"scan025_source_row_skeleton_v01.json"
u=json.loads(u_path.read_text());s=json.loads(s_path.read_text())
pool_path=ROOT/u["shared_pool"]["path"]
pool=json.loads(pool_path.read_text())
files={f["id"]:f for f in pool["files"]}
source={f["path"]:(ROOT/f["path"]).read_text() for f in files.values()}
sources={f["id"]:source[f["path"]] for f in files.values()}
json_sources={fid:json.loads(t) for fid,t in sources.items() if files[fid]["kind"]=="json"}
spans={x["id"]:x for x in pool["spans"]}


def sha(x):
    return hashlib.sha256(x.encode("utf-8") if isinstance(x,str) else x).hexdigest()


def ptr(v,p):
    for k in p[1:].split("/") if p else []:
        k=k.replace("~1","/").replace("~0","~")
        v=v[int(k)] if isinstance(v,list) else v[k]
    return v


checked_exact=set();checked_json=set()


def walk(o):
    if isinstance(o,dict):
        if {"source_path","char_start","char_end_exclusive","literal_sha256_utf8"}<=set(o):
            p=o["source_path"];t=source[p];a=o["char_start"];b=o["char_end_exclusive"]
            assert o["source_sha256_utf8"]==sha(t)
            assert sources[o["source_file"]]==t
            assert o["literal"]=={"file_slice":o["source_file"],"char_start":a,"char_end_exclusive":b}
            assert sha(t[a:b])==o["literal_sha256_utf8"]
            assert len(t[:a].encode())==o["utf8_byte_start"]
            assert len(t[:b].encode())==o["utf8_byte_end_exclusive"]
            assert t.count("\n",0,a)+1==o["line_start_1based"]
            assert t.count("\n",0,max(a,b-1))+1==o["line_end_1based"]
            if o.get("existing_pool_span"):
                sp=spans[o["existing_pool_span"]]
                assert (p,a,b)==(sp["source_path"],sp["char_start"],sp["char_end_exclusive"])
            checked_exact.add((p,a,b))
        if {"file","json_pointer","span_ref","source_sha256_utf8","value"}<=set(o):
            fid=o["file"];p=o["json_pointer"];v=ptr(json_sources[fid],p)
            assert o["value"]=={"json_value":fid,"pointer":p}
            assert pool["json_pointer_spans"][fid][p]==o["span_ref"]
            sp=spans[o["span_ref"]]
            assert json.loads(sources[fid][sp["char_start"]:sp["char_end_exclusive"]])==v
            assert files[fid]["path"]==o["source_path"]
            assert files[fid]["sha256_utf8"]==o["source_sha256_utf8"]
            checked_json.add((fid,p))
        for v in o.values():walk(v)
    elif isinstance(o,list):
        for v in o:walk(v)


assert sha(pool_path.read_bytes())==u["shared_pool"]["sha256_utf8"]
walk(u)
assert s["rows"]==u["source_locus_union"]
assert s["canonical_original_C_rows"]==u["canonical_original_C_rows"]
assert s["source_union"]["sha256_utf8"]==sha(u_path.read_bytes())
assert not u["main_adjudicated"] and not u["main_approved"]
raw={r["id"]:r for r in u["raw_row_correspondence"]}
rows={r["id"]:r for r in u["source_locus_union"]}
groups=u["complete_own_groups"]
coverage=Counter()
for row in rows.values():
    assert set(row["readers"])==set("ABC")
    for k in ["final","alternatives","confidence","count_C","count_H","physical_count_parent","marked_in_H","root_evidence"]:
        assert row[k] is None,(row["id"],k)
    assert not row["main_adjudicated"] and not row["main_approved"]
    for r,binding in row["readers"].items():
        frame=u["reader_frames"][binding["reading"]["complete_frame_ref"]]
        assert frame["reader"]==r
        for gid in binding["complete_own_groups"]:
            assert groups[gid]["reader"]==r
            assert gid in frame["groups"]
        for key,sec in [("raw_report_differences","differences"),("raw_doubts","doubts"),("raw_inventory","inventory")]:
            for rid in binding[key]:
                rr=raw[rid]
                assert rr["reader"]==r and rr["section"]==sec and rr["locus"]==row["id"]
                coverage[rid]+=1
        assert binding["report_silent"]==(not binding["raw_report_differences"])
assert coverage==Counter({k:1 for k in raw}),coverage
report_totals={}
for r in "ABC":
    path=f"out/readers/025/{r}/report.json"
    report=json.loads(source[path])
    report_totals[r]={}
    for sec in ["differences","doubts","inventory"]:
        actual=[x for x in raw.values() if x["reader"]==r and x["section"]==sec]
        assert sorted(x["original_index"] for x in actual)==list(range(len(report[sec])))
        for rr in actual:
            obj=report[sec][rr["original_index"]]
            assert set(obj)==set(rr["all_original_fields"])
            for k,ref in rr["all_original_fields"].items():assert ptr(json_sources[ref["file"]],ref["json_pointer"])==obj[k]
        report_totals[r][sec]=len(actual)
    partition=u["complete_source_partitions"][r];t=source[partition["source_path"]]
    cursor=0;pieces=[]
    for item in partition["parts"]:
        ref=item["complete_source"];a=ref["char_start"];b=ref["char_end_exclusive"]
        assert a==cursor
        pieces.append(t[a:b]);cursor=b
    assert cursor==len(t) and "".join(pieces)==t
    assert sha(t)==partition["exact_concatenation_sha256_utf8"]
    sm=json.loads(source[f"out/readers/025/{r}/source_map.json"])
    assert {g["id"] for g in sm["groups"]}=={gid for gid,g in groups.items() if g["reader"]==r}
    for i,g in enumerate(sm["groups"]):
        rec=groups[g["id"]];ref=rec["complete_source"]
        assert t[ref["char_start"]:ref["char_end_exclusive"]]==g["literal_source"]
        fields=set(rec["candidate_and_scope_fields"])|set(rec["original_component_fields"])|{"literal_source"}
        assert fields==set(g)

canon=u["canonical_original_C_rows"]
assert [x["source_id"] for x in canon]==[f"C025-R{i:02d}"for i in range(1,9)]
assert [x["source_parts"][0]["part_id"]for x in canon]==[f"C025-R{i:02d}-1"for i in range(1,9)]
for c in canon:
    assert set(c["reader_reported_scopes"])==set("ABC")
    assert c["root_outcome"]=="pending"
assert len(u["other_C_notation_and_slips_context"])==8
assert len(u["S_source_only_rows"])==7
assert all(not x["root_ink_choice_applied"] and x["local_ink_locus"]is None for x in u["S_source_only_rows"])
assert len(u["H_exact_local_apparatus"])==3
assert len(u["original_C_inventory"])==13
assert not u["mapping_gaps"]
for command in u["literal_command_inventory"]:
    ref=command["source"];a,b=ref["char_start"],ref["char_end_exclusive"]
    if command["smallest_complete_source_group"]:
        g=groups[command["smallest_complete_source_group"]]
        assert g["complete_source"]["char_start"]<=a<=b<=g["complete_source"]["char_end_exclusive"]
        assert command["id"]in g["literal_command_ids"]
    assert command["physical_count"]is None

frozen=json.loads((OUT/"scan025_reader_fingerprints.json").read_text())
for path,h in frozen["files"].items():assert sha((ROOT/path).read_bytes())==h
result={"scan":25,"source_only":True,"union_sha256_utf8":sha(u_path.read_bytes()),"row_skeleton_sha256_utf8":sha(s_path.read_bytes()),"pool_sha256_utf8":sha(pool_path.read_bytes()),
        "report_rows":report_totals,"exact_unique_text_spans_checked":len(checked_exact),"exact_unique_json_refs_checked":len(checked_json),
        "complete_source_partitions":3,"complete_reader_frames":len(u["reader_frames"]),"complete_own_groups":len(groups),
        "literal_source_commands":len(u["literal_command_inventory"]),"outer_source_commands":dict(Counter(c["reader"]for c in u["literal_command_inventory"]if c["smallest_complete_source_group"]is None)),
        "canonical_C_rows":8,"C_notation_context_rows":6,"C_slip_context_rows":2,"S_source_only_rows":7,
        "source_loci":len(rows),"mapping_gaps":[],"all_frozen_37_reader_hashes_unchanged":True,"all_checks_passed":True,
        "selected_decisions":0,"ink_views_performed":0,"limits":"Exact source and correspondence validation only; all ink/count/confidence/marker/selection fields remain pending root."}
p=OUT/"scan025_source_union_replay_v01.json";p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(result,ensure_ascii=False,indent=2))
