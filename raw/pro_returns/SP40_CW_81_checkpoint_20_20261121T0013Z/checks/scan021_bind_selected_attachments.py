"""Bind selected scan021 exact text spans to root's 71 source-record identities.

This is source bookkeeping only; no manuscript/image or mathematical decision.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "out/checks"
TEX = "out/checks/scan021_final_draft.tex"
MAP = OUT / "scan021_final_source_map.json"
JOURNAL = "out/checks/scan021_main_decisions.md"
sha = lambda b: hashlib.sha256(b).hexdigest()
t = (ROOT / TEX).read_text(encoding="utf-8")
m = json.loads(MAP.read_text())
spec_path = OUT / "scan021_record_specs.json"
specs = json.loads(spec_path.read_text())["specifications"]
assert sha(t.encode()) == m["draft_sha256_utf8"]
groups = {g["id"]:g for g in m["selected_groups"]}


def ref(a,b,label):
    assert 0 <= a < b <= len(t), (label,a,b)
    s=t[a:b]
    return dict(path="checks/scan021_final_draft.tex",workspace_path=TEX,
        manifest="checks/scan021_final_source_map.json",workspace_manifest_path="out/checks/scan021_final_source_map.json",
        char_start=a,char_end=b,byte_start=len(t[:a].encode()),byte_end=len(t[:b].encode()),
        line_start=t.count("\n",0,a)+1,line_end=t.count("\n",0,b-1)+1,
        excerpt=s,literal=s,literal_sha256_utf8=sha(s.encode()),
        body_sha256=m["draft_sha256_utf8"],final_file_sha256=m["draft_sha256_utf8"],
        draft_sha256_utf8=m["draft_sha256_utf8"],attachment_id=label)


def loc(s,label,occurrence=0):
    start=0
    for _ in range(occurrence+1):
        a=t.index(s,start);start=a+len(s)
    return ref(a,a+len(s),label)


def span(first,last,label,after=0):
    a=t.index(first,after);b=t.index(last,a)+len(last)
    return ref(a,b,label)


def line(first,label,after=0):
    a=t.index(first,after);b=t.index("\n",a)
    return ref(a,b,label)


def G(gid,label=None):
    r=groups[gid]["final_source_attachment"]
    return ref(r["char_start"],r["char_end"],label or gid)


A={}
def put(n,*refs):A[f"L021-{n:02d}"]=list(refs)

opening=line("Soit $", "TXT021-opening")
parenthesis=line("(ce qui ach", "TXT021-parenthesis")
or_passage=span("Or % BEGIN B021-G03", "\n on a", "TXT021-Or-complete")
on_a=loc(" on a\n\\margin", "TXT021-Or-endpoint")
first_verb=line("d'autre part", "TXT021-first-verb")
conclusion_start=t.index("ce qui % BEGIN B021-G08")
conclusion=span("ce qui % BEGIN B021-G08", "$, cqfd.", "TXT021-conclusion")
heading=loc(r"\uline{Corollaire du lemme} Pour une classe", "TXT021-heading")
archive=loc("% archive sheet number: 20", "TXT021-archive")

put(1,opening);put(2,opening)
put(3,line(r"\node at (1090,225)","L021-03-ie"))
put(4,G("C021-G01a"));put(8,G("C021-G01a"))
put(5,span("% second roofed Sigma",r"\node at (804,201) {$\scriptstyle +$};","L021-05-complete-Sigma"))
put(6,span("% right first Sigma:",r"\node at (1306,245) {$\scriptscriptstyle0$};","L021-06-complete-Sigma"))
put(7,span(r"\draw (1347,185)",r"\node at (1386,226) {$\scriptstyle i$};","L021-07-complete-Sigma"))
put(9,parenthesis)
put(10,loc(r"ach\unsure{è|é|e}vera","L021-10-complete-word"))
put(11,loc(r"d\unsure{è|é|e}monstration","L021-11-complete-word"))
put(12,span(r"\draw (1134,419)",r"(1118,630);","L021-12-complete-brace"))
put(13,span(r"\node at (1260,445)",r"\node at (1316,458) {$\scriptstyle1$};","L021-13-complete-second-K"))
put(14,G("B021-G02-cancelled-Sigma"));put(15,G("B021-G02-cancelled-Sigma"))
put(16,G("A021G05"));put(17,G("C021-M01"))
put(18,or_passage);put(19,on_a);put(20,on_a)
put(21,G("C021-M02"))
put(22,span(r"\node at (535,930)",r"\node at (1015,969) {$\scriptstyle\alpha\in K_0$};","L021-22-complete-union"))
put(23,span("% Complete roofed Sigma group:",r"\draw (1210,889)--(1227,886) (1220,881)--(1221,895);","L021-23-complete-Sigma"))
put(24,G("C021-M03"));put(25,G("B021-G05-index"))
put(26,span(r"\draw (925,1104)",r"\draw (978,1114)--(1003,1108) (993,1103)--(995,1124);","L021-26-complete-Sigma"))
put(27,span(r"\draw (1142,1110)",r"\draw (1234,1104) .. controls (1243,1102) and (1254,1100) .. (1261,1105);","L021-27-complete-Sigma"))
put(28,G("A021G20"));put(29,G("A021G20"))
put(30,G("A021DG"));put(31,G("B021-G06-middle-row"));put(32,G("A021D05"))
put(33,G("A021D01"));put(34,G("A021D02"));put(35,G("B021-G06-middle-row"));put(36,G("A021D04"));put(37,G("A021M04"))
rotation=line(r"\begin{scope}[shift={(1435,1285)},cm={0,-1,1,0,(0,0)}]","SCOPE021-sideways")
put(38,rotation,line(r"\draw[line width=.4pt] (58,30)","L021-38-outer-margin-brace"))
put(39,rotation,line(r"\draw[line width=.4pt] (42,77)","L021-39-inner-margin-brace"))
put(40,rotation,span(r"\draw[line width=.4pt] (48,35)",r"\draw[line width=.4pt] (215,56)--(225,61) (221,52)--(219,64);","L021-40-two-complete-sideways-labels"))
put(41,first_verb);put(42,G("A021G10"));put(43,G("A021G12"));put(44,G("A021G11"))
put(45,G("B021-G08"));put(46,G("B021-G08"))
put(47,loc(" signifie aussi que $", "L021-47-live-signifie"))
put(48,span(r"\draw (310,1574)",r"\draw (376,1567)--(399,1568) (385,1556)--(390,1576);","L021-48-complete-Sigma"))
put(49,span(r"\draw (464,1577)",r"\draw (520,1567)--(537,1566) (526,1560)--(532,1574);","L021-49-complete-Sigma"))
put(50,G("C021-G08"),loc("$, cqfd.","L021-50-cqfd-endpoint"))
put(51,G("A021G22"));put(52,G("A021G22"));put(53,G("C021-M05"));put(54,G("C021-G09a"));put(55,G("A021G15"))
accent_word=loc(r"pr\unsure{ê|é|e}c\unsure{é|è|e}dent","TXT021-complete-precedent")
put(56,accent_word);put(57,accent_word)
corollary_prose=span(r"\node at (300,2145)",r"\node at (315,2231) {on a};","TXT021-corollary-prose")
put(58,corollary_prose);put(59,G("C021-G09b"))
outer_bottom=line(r"\draw (489,2227)","L021-61-complete-outer-bottom-brace")
put(60,outer_bottom,G("B021-G10-set-open"),G("B021-G10-set-close"))
put(61,outer_bottom);put(62,G("B021-G10-set-open"));put(63,G("B021-G10-set-close"))
put(64,span("% Final Sigma head/body",r"\draw (600,2306)--(620,2306) (610,2296)--(611,2317);","L021-64-complete-Sigma"))
last_complement=span(r"\node at (1116,2332)",r"\node at (1193,2340) {$\scriptscriptstyle\alpha$};","TXT021-final-complement")
put(65,last_complement);put(66,last_complement)
put(67,loc("cela implique que","TXT021-cela"));put(68,G("A021G25-selected-path"));put(69,G("C021-M06"))
existing_bar=line(r"\node at (521,2281)","L021-70-existing-bar-V")
put(70,*[r for n in [4,5,16,23,26,55] for r in A[f"L021-{n:02d}"]],existing_bar)
remainder=[opening,G("C021-G01"),parenthesis,G("C021-G02"),loc("comme dans le lemme.","TXT021-comme-dans-le-lemme"),
    or_passage,G("C021-G03"),A["L021-67"][0],G("C021-G04"),G("A021G20"),G("A021DG"),first_verb,
    G("A021G10"),G("A021G11"),G("A021G12"),conclusion,heading,G("C021-G09"),archive]
put(71,*remainder)
assert set(A)=={s["id"] for s in specs}
m["attachments_by_decision"]=A

# Preserve complete selected parent sources while supplying precise local attachments.
for group in m["selected_groups"]:
    current_ids=[]
    gr=group["final_source_attachment"]
    for did,attachments in A.items():
        if any(gr["char_start"]<=r["char_start"] and r["char_end"]<=gr["char_end"] for r in attachments):
            current_ids.append(did)
    group["decision_ids"]=current_ids
    group["main_approved"]=False
m["attachments_by_source_locus"]={s["id"]:A[s["id"]] for s in specs}
for s in specs:
    hid=s.get("extra",{}).get("head_crosswalk_id")
    if hid:m["attachments_by_source_locus"][hid]=A[s["id"]]

original_inventory={
    "021.01":[opening],"021.02":[G("C021-G01")],"021.03":[parenthesis],"021.04":[G("C021-G02")],
    "021.05":[G("B021-G02-cancelled-Sigma")],"021.06":[loc("comme dans le lemme.","INV021-06")],
    "021.07":[or_passage],"021.08":[G("C021-G03")],"021.09":A["L021-67"],"021.10":[G("C021-G04")],
    "021.11":[G("A021G20")],"021.12":[G("A021DG")],"021.13":[first_verb],
    "021.14":[G("A021G10"),G("A021G11"),G("A021G12")],"021.15":[conclusion],"021.16":[G("B021-G08")],
    "021.17":[heading,line(r"\node at (300,1915)","INV021-17-first-line"),G("A021G22")],
    "021.18":[span(r"\node at (602,2005)","% A021G15 END\n$};", "INV021-18-expression")],
    "021.19":[corollary_prose],
    "021.20":[span("% Main bottom brace:",r"\node at (1554,2325) {$X\setminus V$};","INV021-20-complete-bottom")],
    "021.21":[G("C021-G09b")],
}
m["original_inventory_source_attachments"]=original_inventory
aliases={gid:[G(gid)] for gid in groups}
aliases["A021G07"]=[line(r"\draw[gray,line width=.2pt] (1155,861)","DONOR021-A-G07-lower-trace")]
aliases["A021G25"]=[G("A021G25-selected-path")]
aliases["B021-G10"]=[G("B021-G10-set-open"),G("B021-G10-set-close")]
m["attachments_by_inventory_source_group"]=aliases
m["selected_graphic_inventory_source_attachments"]={gid:[G(gid)] for gid in groups}
m["archive_inventory_source_attachment"]=[archive]
m["original_C_doubt_attachments"]={s["original_C_row"]:A[s["id"]] for s in specs if s.get("original_C_row")}
m["original_C_doubt_part_attachments"]={rid+"-1":refs for rid,refs in m["original_C_doubt_attachments"].items()}
assert len(m["original_C_doubt_attachments"])==15

j=(ROOT/JOURNAL).read_text()
def journal_ref(section):
    match=re.search(rf"^## {section:02d} — .*",j,re.M);assert match,section
    following=re.search(r"^## \d+ — ",j[match.end():],re.M)
    a=match.start();b=match.end()+following.start() if following else len(j)
    value=j[a:b]
    return dict(path=JOURNAL,manifest=JOURNAL,char_start=a,char_end=b,
        line_start=j.count("\n",0,a)+1,line_end=j.count("\n",0,b-1)+1,
        excerpt=value,literal_sha256_utf8=sha(value.encode()),source_sha256_utf8=sha(j.encode()))
m["root_authorizations"]={s["id"]:[journal_ref(s["section"])]+([journal_ref(26)] if s["id"]=="L021-03" else [journal_ref(27)] if s["section"]==9 else []) for s in specs}
m["root_journal"]={"path":JOURNAL,"sha256_utf8":sha(j.encode())}
m["record_specifications"]={"path":"out/checks/scan021_record_specs.json","sha256_utf8":sha(spec_path.read_bytes())}

content_spans=[
    span("Soit $","% END C021-G01\n\\]","CONTENT021-01-opening-and-written-ie"),
    span("(ce qui ach","comme dans le lemme.","CONTENT021-02-U-expression-and-adjoining-prose"),
    conclusion,
    span(r"\uline{Corollaire du lemme}","% END C021-G09\n}","CONTENT021-04-corollary-and-both-conditions"),
]
note=("The page starts with alpha0 in K1, the two written empty intersections joined by i.e, and the expression "
      "U=X setminus the union of roofed Sigma_alpha^+ with K=K1 union {i}. The proof ends with the written empty "
      "intersection and cqfd. The underlined Corollaire du lemme calls its expression for V unique, gives the K "
      "condition with bar V and dot V, and ends with the complement X setminus Sigma_alpha. The cancelled Sigma "
      "group, impli/impl., recovered V beneath E, and qualified retracing after Or remain in the selected text. "
      "No written date or author page number is transcribed; archive 20 remains a source comment.")
m["attributed_content_note"]={"note":note,"status":"Attributed transcription content; mathematical assertions unverified.",
    "selected_source_spans":content_spans,"source_support":[A["L021-18"],A["L021-45"],A["L021-59"],A["L021-71"][-1:]],
    "root_authorization":journal_ref(25),"mathematical_checks_performed":False,"main_approved":False}

attempts=[]
for name in ["scan021_assembly_attempt_v01.json","scan021_assembly_attempt_v02.json"]:
    p=OUT/name
    attempts.append({"path":"out/checks/"+name,"sha256_utf8":sha(p.read_bytes()),"record":json.loads(p.read_text())})
m["bounded_source_repairs"]=attempts
m["assembly_scripts"]={name:sha((OUT/name).read_bytes()) for name in ["scan021_prepare_tex_candidates.py","scan021_assemble_selected.py","scan021_bind_selected_attachments.py"]}

# Exact attachment/coverage gate: no image, renderer, compiler or theorem check.
attachment_count=0
def check(value):
    global attachment_count
    if isinstance(value,dict):
        if value.get("path")=="checks/scan021_final_draft.tex" and "char_start" in value:
            a,b=value["char_start"],value["char_end"]
            assert t[a:b]==value["excerpt"]
            assert sha(t[a:b].encode())==value["literal_sha256_utf8"]
            assert value["draft_sha256_utf8"]==sha(t.encode())
            attachment_count+=1
        for v in value.values():check(v)
    elif isinstance(value,list):
        for v in value:check(v)
check(m)
assert "".join(s["final"]["excerpt"] for s in m["source_segments"])==t
for segment in m["source_segments"]:
    s=segment["source"]
    if s["path"]:
        original=(ROOT/s["path"]).read_text()
        assert original[s["char_start"]:s["char_end"]]==segment["final"]["excerpt"]
for s in specs:
    assert A[s["id"]],s["id"]
    for gid in s["selected_source_groups"]:assert gid in aliases,(s["id"],gid)
m["assembly_audit"].update(exact_attachment_references_checked=attachment_count,
    decision_attachment_sets=len(A),original_inventory_attachment_sets=len(original_inventory),
    canonical_C_part_attachment_sets=len(m["original_C_doubt_part_attachments"]),
    contiguous_full_source_coverage=True,source_segment_literals_verified=True,
    current_draft_sha256_utf8=sha(t.encode()),main_approved=False)
m["status"]="Complete selected source and attachments frozen for root and one independent source review; approval pending."
m["main_adjudicated"]=False;m["main_approved"]=False
MAP.write_text(json.dumps(m,ensure_ascii=False,indent=2)+"\n")
summary={"draft":TEX,"draft_sha256_utf8":sha(t.encode()),"map":"out/checks/scan021_final_source_map.json",
    "map_sha256_utf8":sha(MAP.read_bytes()),"selected_groups":len(groups),"decision_attachment_sets":len(A),
    "original_inventory_attachment_sets":len(original_inventory),"canonical_C_part_attachment_sets":15,
    "current_approval_flags":False,"source_only":True}
(OUT/"scan021_assembly_handoff.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(summary,ensure_ascii=False))
