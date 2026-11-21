#!/usr/bin/env python3
"""Build scan025 source correspondence only; every ink outcome remains pending."""
from __future__ import annotations
from pathlib import Path
from collections import defaultdict
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "out/checks"
POOL_PATH = OUT / "scan025_source_pool_v01.json"
POOL = json.loads(POOL_PATH.read_text())
FILES = {f["path"]: f for f in POOL["files"]}
SPANS = {s["id"]: s for s in POOL["spans"]}
SOURCE = {p: (ROOT / p).read_text() for p in FILES}
JSON = {p: json.loads(SOURCE[p]) for p in FILES if FILES[p]["kind"] == "json"}
POOL_HASH = hashlib.sha256(POOL_PATH.read_bytes()).hexdigest()
SPAN_LOOKUP = {(s["source_path"], s["char_start"], s["char_end_exclusive"]): s["id"] for s in POOL["spans"]}


def sha(s):
    return hashlib.sha256(s.encode("utf-8") if isinstance(s, str) else s).hexdigest()


def exact(path, a, b):
    s = SOURCE[path]
    assert 0 <= a <= b <= len(s), (path, a, b)
    return {
        "source_path": path, "source_file": FILES[path]["id"], "source_sha256_utf8": sha(s),
        "char_start": a, "char_end_exclusive": b,
        "utf8_byte_start": len(s[:a].encode("utf-8")), "utf8_byte_end_exclusive": len(s[:b].encode("utf-8")),
        "line_start_1based": s.count("\n", 0, a)+1, "line_end_1based": s.count("\n", 0, max(a, b-1))+1,
        "literal": {"file_slice": FILES[path]["id"], "char_start": a, "char_end_exclusive": b},
        "literal_sha256_utf8": sha(s[a:b]),
        "existing_pool_span": SPAN_LOOKUP.get((path, a, b)),
    }


def getptr(obj, ptr):
    for k in ptr[1:].split("/") if ptr else []:
        k = k.replace("~1", "/").replace("~0", "~")
        obj = obj[int(k)] if isinstance(obj, list) else obj[k]
    return obj


def jref(path, pointer):
    fid = FILES[path]["id"]
    return {"file": fid, "source_path": path, "source_sha256_utf8": FILES[path]["sha256_utf8"],
            "json_pointer": pointer, "span_ref": POOL["json_pointer_spans"][fid][pointer],
            "value": {"json_value": fid, "pointer": pointer}}


def literal(path, text, region=None, occurrence=0):
    s = SOURCE[path]
    a, b = region or (0, len(s))
    hits = [m.start()+a for m in re.finditer(re.escape(text), s[a:b])]
    assert len(hits) > occurrence, (path, text, region, hits)
    pos = hits[occurrence]
    return exact(path, pos, pos+len(text))


READERS = {}
FRAMES = {}
GROUPS = {}
PARTITIONS = {}
COMMANDS = []
GAPS = []
for r in "ABC":
    base = f"out/readers/025/{r}"
    texpath, mappath, reportpath = f"{base}/reading.tex", f"{base}/source_map.json", f"{base}/report.json"
    t, sm, report = SOURCE[texpath], JSON[mappath], JSON[reportpath]
    READERS[r] = {"texpath": texpath, "mappath": mappath, "reportpath": reportpath, "text": t, "map": sm, "report": report}
    display_starts = [m.start() for m in re.finditer(re.escape("\\["), t)]
    display_ends = [m.end() for m in re.finditer(re.escape("\\]"), t)]
    assert len(display_starts) == len(display_ends) == 2
    archive = t.index("% archive sheet number: 24")
    regions = {
        "whole": (0, len(t)), "opening": (t.index("\n")+1, display_starts[0]),
        "display": (display_starts[0], display_ends[0]),
        "prose": (display_ends[0], display_starts[1]),
        "final": (display_starts[1], display_ends[1]),
        "lower": (display_ends[1], archive), "archive": (archive, len(t)),
    }
    READERS[r]["regions"] = regions
    for name, (a,b) in regions.items():
        fid = f"{r}:{name}"
        FRAMES[fid] = {"id": fid, "reader": r, "scope": name, "complete_source": exact(texpath,a,b), "groups": []}
    for i,g in enumerate(sm["groups"]):
        a,b = (g["start_char"],g["end_char_exclusive"]) if "start_char" in g else g["char_offsets"]
        assert t[a:b] == g["literal_source"], (r,g["id"])
        gid=g["id"]
        GROUPS[gid] = {
            "id":gid,"reader":r,"original_map_index":i,"raw_group":jref(mappath,f"/groups/{i}"),
            "complete_source":exact(texpath,a,b),
            "candidate_and_scope_fields":{k:jref(mappath,f"/groups/{i}/{k}") for k in g if k not in ["literal_source","components","path_components"]},
            "original_component_fields":{k:jref(mappath,f"/groups/{i}/{k}") for k in ["components","path_components"] if k in g},
            "containing_groups":[],"contained_groups":[],"literal_command_ids":[],
            "selected":None,"main_approved":False,
        }
        for name,(c,d) in regions.items():
            if c<=a and b<=d:FRAMES[f"{r}:{name}"]["groups"].append(gid)
    own=[x for x in GROUPS.values() if x["reader"]==r]
    for g in own:
        a,b=g["complete_source"]["char_start"],g["complete_source"]["char_end_exclusive"]
        for other in own:
            c,d=other["complete_source"]["char_start"],other["complete_source"]["char_end_exclusive"]
            if g["id"]!=other["id"] and c<=a and b<=d:
                g["containing_groups"].append(other["id"])
                other["contained_groups"].append(g["id"])
    tops=sorted([g for g in own if not g["containing_groups"]],key=lambda g:g["complete_source"]["char_start"])
    parts=[];p=0
    for g in tops:
        a,b=g["complete_source"]["char_start"],g["complete_source"]["char_end_exclusive"]
        assert a>=p
        if a>p:parts.append({"kind":"owned_companion_source","complete_source":exact(texpath,p,a)})
        parts.append({"kind":"complete_top_group","group":g["id"],"complete_source":g["complete_source"]})
        p=b
    if p<len(t):parts.append({"kind":"owned_companion_source","complete_source":exact(texpath,p,len(t))})
    assert "".join(t[x["complete_source"]["char_start"]:x["complete_source"]["char_end_exclusive"]] for x in parts)==t
    PARTITIONS[r]={"source_path":texpath,"parts":parts,"exact_concatenation_sha256_utf8":sha(t),"entire_source_covered":True}
    # Exact lexical source commands. Braces delimit outer nodes containing
    # child pictures; semicolons inside those braces do not end the outer node.
    for n,m in enumerate(re.finditer(r"\\(?:draw|fill|path|coordinate|node|useasboundingbox)\b",t),1):
        a=m.start();i=m.end();depth=0
        while i<len(t):
            ch=t[i]
            bs=0;j=i-1
            while j>=0 and t[j]=="\\":bs+=1;j-=1
            escaped=bs%2==1
            if ch=="{" and not escaped:depth+=1
            elif ch=="}" and not escaped:depth-=1
            elif ch==";" and depth==0:break
            i+=1
        assert i<len(t),(r,a)
        b=i+1
        containing=[g for g in own if g["complete_source"]["char_start"]<=a and b<=g["complete_source"]["char_end_exclusive"]]
        containing.sort(key=lambda g:g["complete_source"]["char_end_exclusive"]-g["complete_source"]["char_start"])
        cid=f"{r}:CMD:{n:03d}"
        owner=containing[0]["id"] if containing else None
        if owner:GROUPS[owner]["literal_command_ids"].append(cid)
        COMMANDS.append({"id":cid,"reader":r,"command_token":m.group(),"source":exact(texpath,a,b),
                         "smallest_complete_source_group":owner,"all_containing_groups":[g["id"] for g in containing],
                         "containing_frame":f"{r}:lower" if regions["lower"][0]<=a<regions["lower"][1] else f"{r}:whole",
                         "ownership_kind":"source_group" if owner else "outer_source_placement",
                         "physical_count":None})

LOCUS_DEFS = [
 (1,"opening cancelled phrase","opening"),(2,"opening live wording and inclusion context","opening"),
 (3,"first corrected Sigma: predecessor, index and upper-run scopes","opening"),
 (4,"barred U, old relation/live cap, complete opening E and nonemptiness","opening"),
 (5,"cancelled connective and live alors","opening"),(6,"reduced on a continuation","opening"),
 (7,"main equality and complete large-operator/limit state","display"),
 (8,"complete hatted Sigma and two local upper-index traces","display"),
 (9,"où and complete right membership condition","display"),
 (10,"quantifier and complete component-condition Sigma","display"),
 (11,"pi-zero argument and complete E-alpha","display"),
 (12,"far-right deleted cluster and endpoint comma scope","display"),
 (13,"whole pre-les cluster with all reader-local state candidates","display"),
 (14,"live les and complete disjointness Sigma","display"),
 (15,"mut abbreviation, disjoints and physical-edge punctuation scope","display"),
 (16,"Il faut voir que and complete K replacement/crossing/guide group","prose"),
 (17,"prose Sigma and following complete parenthetical","prose"),
 (18,"whole word after sont and all accent/attachment scopes","prose"),
 (19,"complete positive signed Sigma before i.e.","prose"),(20,"i.e. and its source punctuation","prose"),
 (21,"complete negative signed Sigma and following point","prose"),
 (22,"Je dis que, complete que/descender and reader B local point","prose"),
 (23,"final set prefix, left brace and complete condition","final"),
 (24,"final Sigma-alpha-minus and right endpoint","final"),
 (25,"reported faint lower-sheet curve","lower"),(26,"reported two dark lower-right marks","lower"),
 (27,"archive/source page numeral","archive"),(28,"complete page-region containers and source-level metadata","whole"),
]
GROUP_LOCUS={
 "A":{"G00":1,"S01":3,"G01":4,"G02":4,"G03":5,"G04":6,"G05":7,"S02":8,"M01":8,"G06":9,"S03":10,"G07":12,"G08":13,"S04":14,"G09":16,"M02":16,"S05":17,"S06":19,"S07":21,"S08":24,"M03":26},
 "B":{"S01":3,"G02":4,"G03":6,"G04":7,"S02":8,"S03":10,"G05":12,"G06":13,"S04":14,"G07":16,"S05":17,"S06":19,"S07":21,"G08":23,"S08":24,"M01":25,"M02":26,"G09":22},
 "C":{"G01":1,"S01":3,"G02":4,"E01":4,"G03":5,"G04":6,"G05":7,"S02":8,"G06":9,"S03":10,"E02":11,"G07":12,"G08":13,"S04":14,"G09":16,"S05":17,"S06":19,"S07":21,"S08":24,"M01":25,"M02":26},
}
GROUP_LOCUS={f"{r}025-{g}":l for r,mp in GROUP_LOCUS.items() for g,l in mp.items()}
assert set(GROUP_LOCUS)==set(GROUPS)
DIFF_LOCUS={
 "A":[1,3,4,4,5,6,7,8,9,12,13,14,15,15,16,17,18,19,21,24,26],
 "B":[3,4,4,7,12,13,15,18,5,6,3,13,15,24,3,4,7,12,13,16,14,17,19,21,8,22,25,26],
 "C":[3,4,4,7,12,13,15,18,1,3,4,4,5,6,7,8,9,11,12,14,15,16,17,19,21,24,25,26],
}
INVENTORY_LOCAL={
 "A":{2:2,6:28,14:15,21:28,22:18,25:23,28:27},
 "B":{0:1,3:2,6:5,10:28,16:15,21:28,28:23,31:27},
 "C":{1:2,8:28,12:10,16:15,18:28,23:18,26:23,30:27},
}
ROWS={n:{"id":f"L025-{n:02d}","location":name,"source_frame_kind":frame,
         "status":"pending root source/ink adjudication","readers":{},"C_original_source_ids":[],
         "witnesses":{},"H_exact_apparatus_attachments":[],
         "final":None,"alternatives":None,"confidence":None,"count_C":None,"count_H":None,
         "physical_count_parent":None,"marked_in_H":None,"root_evidence":None,
         "main_adjudicated":False,"main_approved":False} for n,name,frame in LOCUS_DEFS}

RAW_ROWS=[]
for r,d in READERS.items():
    report=d["report"];path=d["reportpath"]
    for n,row in ROWS.items():
        gids=[g for g,k in GROUP_LOCUS.items() if k==n and g.startswith(r)]
        row["readers"][r]={
            "role":"this reader's complete own proposal, with original candidate and inventory scopes",
            "reading":{"complete_frame_ref":f"{r}:{row['source_frame_kind']}"},
            "complete_own_groups":gids,
            "raw_report_differences":[],"raw_doubts":[],"raw_inventory":[],
            "candidate_scope_sources":[GROUPS[g]["raw_group"] for g in gids],
            "raw_witness_fields_policy":"C and H fields inside raw report rows retain their reported witness role; the own reading binds only this reader's TeX and own proposal fields.",
            "report_silent":None,
        }
    assert len(DIFF_LOCUS[r])==len(report["differences"])
    for section in ["differences","doubts","inventory"]:
        for i,obj in enumerate(report[section]):
            ptr=f"/{section}/{i}"
            groups=obj.get("source_groups",[])
            if not groups:
                gg=obj.get("source_group") or obj.get("group_id")
                if gg:groups=[gg]
            candidates=sorted(set(GROUP_LOCUS[g] for g in groups))
            if section=="differences":locus=DIFF_LOCUS[r][i]
            elif candidates:
                assert len(candidates)==1,(r,ptr,candidates)
                locus=candidates[0]
            elif section=="inventory":locus=INVENTORY_LOCAL[r].get(i)
            elif obj.get("location")=="after sont":locus=18
            else:locus=None
            if locus is None:
                GAPS.append({"type":"raw_row_has_no_source_correspondence","reader":r,"raw_ref":jref(path,ptr)})
                continue
            rid=f"{r}:{section}:{i:02d}"
            fields={k:jref(path,ptr+"/"+k.replace("~","~0").replace("/","~1")) for k in obj}
            rr={"id":rid,"reader":r,"section":section,"original_index":i,
                "original_identity":obj.get("id") or obj.get("element") or obj.get("location"),
                "raw":jref(path,ptr),"all_original_fields":fields,
                "locus":ROWS[locus]["id"],"explicit_source_groups":groups,
                "correspondence_basis":"supplied group identity" if candidates else "exact source wording and complete reader frame",
                "selected":None}
            RAW_ROWS.append(rr)
            target={"differences":"raw_report_differences","doubts":"raw_doubts","inventory":"raw_inventory"}[section]
            ROWS[locus]["readers"][r][target].append(rid)
            if section=="inventory":
                ROWS[locus]["readers"][r]["candidate_scope_sources"].append(jref(path,ptr))
    for row in ROWS.values():
        row["readers"][r]["report_silent"]=not bool(row["readers"][r]["raw_report_differences"])
        row["readers"][r]["report_silent_rule"]="The complete own source frame and own groups carry this reader's proposal; silence in a difference list supplies no reading."

# Literal text companions are bound independently of report headlines.
TEXT_ANCHORS={
 "A":{1:r"\\deleted{Soit en effet}",2:"Si on a $U_s\\subset",4:r"\overline{U_s}",5:"alors\n",7:r"U_s=X\setminus",9:r"i\in K\subset I",10:r"\forall\alpha\in K",11:r"\pi_0(X\setminus E_\alpha)",14:r"\text{les }",15:r"\text{mut\textsuperscript{t}. disjoints}",16:"Il faut voir que",17:r"$(\alpha\in K\setminus\{i\})$",18:"determinés",20:"i.e.",22:"Je dis que",23:r"K\setminus\{i\}=\bigl\{\alpha\in I\mid E_\alpha\subset",27:"% archive sheet number: 24"},
 "B":{1:r"\deleted{Soit en effet}",2:"Si on a $U_s\\subset",4:r"\overline{U_s}",5:r"\deleted{et si} alors",7:r"U_s=X\setminus",9:r"\text{où}\quad i\in K\subset I",10:r"\forall\alpha\in K",11:r"\pi_0(X\setminus E_\alpha)",14:r"\text{les }",15:r"\text{mut\textsuperscript{t}. disjoints}",16:"Il faut voir que",17:r"$(\alpha\in K\setminus\{i\})$",18:r"\unsure{determinés|déterminés|determines}",20:"i.e.",22:"Je dis",23:r"K\setminus\{i\}=",27:"% archive sheet number: 24"},
 "C":{2:"Si on a $U_s\\subset",4:r"\overline{U_s}",5:"alors\n",7:r"U_s=X\setminus",9:r"i\in K\subset I",10:r"\forall\alpha\in K",11:r"\pi_0(X\setminus",14:r"\text{les }",15:r"\text{mut\textsuperscript{t}. disjoints}",16:"Il faut voir que",17:r"$(\alpha\in K\setminus\{i\})$",18:r"\unsure{determinés|déterminés|determines}",20:"i.e.",22:"Je dis que",23:r"K\setminus\{i\}=\bigl\{\alpha\in I\mid E_\alpha\subset",27:"% archive sheet number: 24"},
}
# A's deleted phrase is literal node text, while its complete state is in G00.
TEXT_ANCHORS["A"][1]="Soit en effet"
for r,mp in TEXT_ANCHORS.items():
    for n,txt in mp.items():
        region=READERS[r]["regions"][ROWS[n]["source_frame_kind"]]
        ROWS[n]["readers"][r].setdefault("own_literal_companions",[]).append(literal(READERS[r]["texpath"],txt,region))

for r in "AC":
    ROWS[22]["readers"][r]["bounded_source_presence"]={"scope":f"{r}:prose","own_local_literal":"Je dis que", "graphic_group_for_point_in_this_scope":[], "basis":"Complete inspected source frame and complete map groups; no independent-point group is supplied in this frame."}
ROWS[25]["readers"]["A"]["bounded_source_presence"]={"scope":"A:lower","own_groups_in_scope":["A025-M03"],"faint_curve_group_in_this_scope":[],"basis":"The complete inspected lower-source frame contains the dark-pair group and its surrounding source. No faint-curve proposal is supplied in this frame."}

# C/H readings always come from their actual packet text; raw report witness
# strings remain separately reachable through the corresponding raw rows.
Cpath,Hpath="packets/025/C.tex","packets/025/H.tex"
WIT_LITERALS={
 1:(r"\deleted{Soit en effet}",r"\struck{Soit en effet}"),
 2:(r"Si on a $U_s\subset\deleted{\unsure{E|I}}\Sigma_i^-$",r"Si on a $U_{s}\subset\Sigma_{i}^{-}$"),
 3:(r"\deleted{\unsure{E|I}}\Sigma_i^-",r"\Sigma_{i}^{-}"),
 4:(r"$\overline{U_s}\deleted{\unsure{=}}\cap E_{\unsure{i|j}}\ne\varnothing$",r"$\overline{U_{s}}\cap E_{i}\neq\emptyset$"),
 5:(r"\deleted{et si} alors on a",r"\struck{ainsi} alors on a"),
 6:("on a\n\\[","on a\n\\["),
 7:(r"U_s=X\setminus\mathop{\unsure{\rlap{\raisebox{.65ex}{$\scriptstyle-$}}\bigcup|\deleted{\bigcap}\bigcup}}\limits_{\alpha\in K}\widehat{\Sigma}_\alpha^+",r"U_{s}=X\smallsetminus\bigcup_{\alpha\in K}\widehat{\Sigma}_{\alpha}^{+}"),
 8:(r"\widehat{\Sigma}_\alpha^+",r"\widehat{\Sigma}_{\alpha}^{+}"),
 9:(r"\text{où}\quad i\in K\subset I",r"\text{où } i\in K\subset I"),
 10:(r"\forall\alpha\in K\qquad\Sigma_\alpha^+", "$\\forall\\alpha\\in K$\n$\\Sigma_{\\alpha}^{+}"),
 11:(r"\pi_0(X\setminus E_\alpha)",r"\pi_{0}(X\smallsetminus E_{\alpha})"),
 12:(r"\deleted{\unsure{\text{les}|K}}",r"\struck{tel},"),
 13:(r"\deleted{\unsure{U\Sigma|\bigcup\Sigma|U}}\ \text{les }",r"et les"),
 14:(r"\text{les }\Sigma_\alpha^+",r"les $\Sigma_{\alpha}^{+}$"),
 15:(r"\text{\unsure{mut\textsuperscript{t}.|mut.} disjoints}",r"mut\supplied{uellemen}t disjoints."),
 16:(r"\deleted{K}\inserted{K\setminus\{i\}}",r"\struck{$K$} $K\smallsetminus\{i\}$"),
 17:(r"et les $\Sigma_\alpha^+$ $(\alpha\in K\setminus\{i\})$", "et les\n$\\Sigma_{\\alpha}^{+}$ ($\\alpha\\in K\\smallsetminus\\{i\\}$)"),
 18:(r"\unsure{determinés|déterminés|determines}","déterminés"),
 19:(r"\Sigma_i^+",r"\Sigma_{i}^{+}"),
 20:("i.e.","i.e.\\"),
 21:(r"\Sigma_i^-",r"\Sigma_{i}^{-}"),
 22:("Je dis que","Je dis que"),
 23:(r"K\setminus\{i\}=\bigl\{\alpha\in I\mid E_\alpha\subset",r"K\smallsetminus\{i\}=\{\alpha\in I\mid E_{\alpha}\subset"),
 24:(r"\bigl\{\alpha\in I\mid E_\alpha\subset\Sigma_\alpha^-",r"\{\alpha\in I\mid E_{\alpha}\subset\Sigma_{\alpha}^{-}\}"),
 27:("% archive sheet number: 24",r"\page{24}"),
}
for n,pair in WIT_LITERALS.items():
    for w,path,txt in zip("CH",[Cpath,Hpath],pair):
        region=None
        if n in [17,18,19,20,21,22]:region=(SOURCE[path].index("Il faut voir que"),len(SOURCE[path]))
        ROWS[n]["witnesses"][w]={"role":f"actual supplied {w} witness source","source":literal(path,txt,region)}
for n in [25,26,28]:
    for w,path in [("C",Cpath),("H",Hpath)]:
        ROWS[n]["witnesses"][w]={"role":f"actual supplied {w} witness complete inspected source","source":exact(path,0,len(SOURCE[path])),"local_graphic_claim":"No separate lower trace group occurs in this complete supplied source; this is a bounded source statement only." if n in [25,26] else None}

CANON=[]
catalog=JSON["out/checks/scan025_C_doubt_catalog.json"]
canon_loci=[3,4,4,7,12,13,15,18]
for i,o in enumerate(catalog["canonical_doubt_rows"]):
    n=canon_loci[i];ROWS[n]["C_original_source_ids"].append(o["source_id"])
    rec={"source_id":o["source_id"],"source_parts":o["source_parts"],"canonical_catalog_ref":jref("out/checks/scan025_C_doubt_catalog.json",f"/canonical_doubt_rows/{i}"),
         "original_source":exact("packets/025/C_doubts.txt",o["char_start"],o["char_end"]),"locus":ROWS[n]["id"],"reader_reported_scopes":{},"root_outcome":"pending","main_approved":False}
    for r in "ABC":
        key="original_C_doubts" if r=="B" else "C_doubt_rows"
        rec["reader_reported_scopes"][r]=jref(READERS[r]["reportpath"],f"/{key}/{i}")
    CANON.append(rec)
CONTEXT=[]
for i,o in enumerate(catalog["other_source_rows"]):
    CONTEXT.append({"id":f"C025-context-{i+1:02d}","original_section":o["section"],"original_source":exact("packets/025/C_doubts.txt",o["char_start"],o["char_end"]),"catalog_ref":jref("out/checks/scan025_C_doubt_catalog.json",f"/other_source_rows/{i}"),"original_doubt_row_identity":None})

HM=JSON["out/checks/scan025_H_marker_catalog.json"]
HATT=[]
for kind,entries in [("editorial_supplies",HM["editorial_supplies"]),("notes",HM["notes"])]:
    for i,o in enumerate(entries):
        att={"id":f"H025-{kind}-{i+1}","kind":kind,"catalog_ref":jref("out/checks/scan025_H_marker_catalog.json",f"/{kind}/{i}"),"whole_exact_source":exact(Hpath,o["char_start"],o["char_end"]),"local_scopes":[]}
        if kind=="editorial_supplies":
            att["local_scopes"]=[{"locus":"L025-15","scope":"only the supplied letters uellemen in the actual mut...t source token","exact_source":att["whole_exact_source"]}]
        elif i==0:
            h=SOURCE[Hpath];a=o["char_start"];split=h.index(";",a)
            att["local_scopes"]=[{"locus":"L025-03","scope":"note clause naming the opening U subset Sigma, retracing and exponent","exact_source":exact(Hpath,a,split+1)},
                                 {"locus":"L025-07","scope":"note clause naming the union sign","exact_source":exact(Hpath,split+1,o["char_end"])}]
        else:
            h=SOURCE[Hpath];a=o["char_start"];split=h.index("La page",a)
            att["local_scopes"]=[{"locus":"L025-24","scope":"note naming final alpha and its editorial expectation","exact_source":exact(Hpath,a,split)},
                                 {"locus":"L025-28","scope":"note describing the page ending and lower blank area","exact_source":exact(Hpath,split,o["char_end"])}]
        att["marker_decision"]="pending root; no propagation beyond the literal local scope"
        HATT.append(att)
        for loc in att["local_scopes"]:ROWS[int(loc["locus"][-2:])]["H_exact_apparatus_attachments"].append({"attachment":att["id"],"local_scope":loc})

Sscope=JSON["out/checks/scan025_S_scope.json"];Spath=Sscope["source"]
SROWS=[]
for i,sr in enumerate(Sscope["row_scopes"]):
    hits=[m for m in re.finditer(r"(?m)^"+re.escape(sr["id"])+r"\t[^\n]*",SOURCE[Spath])]
    assert len(hits)==1
    m=hits[0]
    SROWS.append({"S_id":sr["id"],"S_status":"source-only review; supplied scope contains no directly quoted local scan025 correction", "raw_scope_ref":jref("out/checks/scan025_S_scope.json",f"/row_scopes/{i}"),"original_tsv_row":exact(Spath,m.start(),m.end()),"root_ink_choice_applied":False,"local_ink_locus":None,"counts_C_H":None})

# Container entries retain their exact own hand fields and exact child refs.
# This records source containment without inheriting a child's attribution.
CONTAINERS=[]
for r,d in READERS.items():
    report=d["report"];inv=report["inventory"]
    for i,obj in enumerate(inv):
        own_id=obj.get("element")
        children=[j for j,v in enumerate(inv) if v.get("parent")==own_id]
        if children:
            CONTAINERS.append({"reader":r,"raw_container":jref(d["reportpath"],f"/inventory/{i}"),"raw_children":[jref(d["reportpath"],f"/inventory/{j}") for j in children],"hand_scope_rule":"Each original container and child keeps its complete own hand/candidate fields. No attribution is inherited by source containment."})

# Full packet inventory rows retain their original thirteen identities.
PINV=[]
packet_inv=JSON["packets/025/C_inventory.json"]
pinv_loci=[1,2,3,4,5,28,7,12,13,28,16,16,23]
for i,obj in enumerate(packet_inv):
    PINV.append({"original_element":obj["element"],"raw":jref("packets/025/C_inventory.json",f"/{i}"),"locus":ROWS[pinv_loci[i]]["id"],"root_selection":None})

FULL_METADATA=[]
for path,f in FILES.items():
    if f["kind"]=="json":
        FULL_METADATA.append({"source_path":path,"source_sha256_utf8":f["sha256_utf8"],"complete_source":jref(path,""),"bounded_review_projection":"scan025_source_projection_manifest_v01.json"})

QUALIFIED_FIELDS=[]
for rr in RAW_ROWS:
    for k,ref in rr["all_original_fields"].items():
        if re.search(r"confidence|hand|scope|qualif|alternative|candidate|role|surface|mark|owner|physical|diff_|status|evidence|attachment",k,re.I):
            QUALIFIED_FIELDS.append({"raw_row":rr["id"],"locus":rr["locus"],"semantic_field":k,"source":ref})

CAUTIONS=[
 {"id":"SC025-01","loci":["L025-04"],"source_fact":"B025-G02 owns the complete relation and E/index together. A025-G01/G02 and C025-G02/E01 have separate exact source bounds. All complete own candidates remain attached through the group references."},
 {"id":"SC025-02","loci":["L025-08","L025-16"],"source_fact":"A025-M01 is nested in A025-S02; A025-M02 is nested in A025-G09. Exact source containment and smallest-complete-group command ownership are recorded without duplicate source selection."},
 {"id":"SC025-03","loci":["L025-13"],"source_fact":"C025-G08 explicitly retains live text et. A025-G08 and B025-G06 retain their own four complete states. The three raw candidate lists stay separate."},
 {"id":"SC025-04","loci":["L025-16"],"source_fact":"B025-G07 has qualification null and alternatives []; its ownership names the long bent guide. A025-G09/M02 and C025-G09 supply their own guide/strike or extended-cancellation qualifications."},
 {"id":"SC025-05","loci":["L025-09"],"source_fact":"A and C supply their respective qualified complete word/trace candidates. B retains literal text où in its full display frame and supplies no corresponding graphical group."},
 {"id":"SC025-06","loci":["L025-22","L025-25"],"source_fact":"B supplies the complete que/descender/point group. B and C supply the lower faint curve. Complete source-frame bounds accompany the A/C point scope and A faint-curve source-silence statements."},
 {"id":"SC025-07","loci":["L025-03","L025-07","L025-15","L025-24","L025-28"],"source_fact":"H supplied letters and each note clause have explicit exact local source bounds. All selected marked_in_H fields remain pending; raw reader flags are preserved independently."},
 {"id":"SC025-08","loci":["L025-03","L025-04","L025-07","L025-12","L025-13","L025-15","L025-18"],"source_fact":"Eight canonical C row identities remain independent from six notation and two slips entries. Reader C report IDs matching canonical ID strings have different file/pointer roles."},
 {"id":"SC025-09","loci":[],"source_fact":"B report reader_source_offsets are UTF-8-byte offsets as stated by its source_geometry field. Map char_offsets remain character offsets. Both original field types and exact recomputed references are preserved."},
 {"id":"SC025-10","loci":["L025-25","L025-26"],"source_fact":"Outer lower-sheet nodes, bounding path/box and baseline declarations remain in the exact source partition and lexical command inventory outside child group bounds. No image scale or metric equality is asserted."},
]

UNION={
 "scan":25,"schema":"scan025-source-union-v01","source_only":True,"status":"pre-image source correspondence only",
 "shared_pool":{"path":POOL_PATH.relative_to(ROOT).as_posix(),"sha256_utf8":POOL_HASH},
 "reference_resolution":"All $s/json_value/file_slice and span_ref references resolve through the frozen shared pool. New exact source refs use that same file_slice recipe; no duplicate source text pool is created.",
 "brief_authority":{"path":"out/briefs/source_record_brief_v07.md","sha256_utf8":sha(SOURCE['out/briefs/source_record_brief_v07.md'])},
 "reader_frames":FRAMES,"complete_own_groups":GROUPS,"complete_source_partitions":PARTITIONS,
 "literal_command_inventory":COMMANDS,"raw_row_correspondence":RAW_ROWS,"scope_field_index":QUALIFIED_FIELDS,
 "source_locus_union":list(ROWS.values()),"canonical_original_C_rows":CANON,"other_C_notation_and_slips_context":CONTEXT,
 "original_C_inventory":PINV,"explicit_inventory_containment":CONTAINERS,
 "H_marker_catalog":jref("out/checks/scan025_H_marker_catalog.json",""),"H_exact_local_apparatus":HATT,
 "S_source_only_rows":SROWS,"S_scope_authority":jref("out/checks/scan025_S_scope.json",""),
 "all_metadata_coverage":FULL_METADATA,"source_role_cautions":CAUTIONS,"mapping_gaps":GAPS,
 "counts":{"actual_source_C_doubt_rows":8,"other_C_notation_rows":6,"other_C_slips_rows":2,"source_loci":len(ROWS),"source_groups":len(GROUPS),"raw_main_report_rows":len(RAW_ROWS),"drawing_source_commands":len(COMMANDS)},
 "selected_counts":None,"selected_confidences":None,"root_crop_journal":None,"main_adjudicated":False,"main_approved":False,
 "limits":"Source correspondences bind exact original text and complete own-reader metadata. Reader observations remain attributed. Ink, hand, source-role decisions, correction counts and selected output await root's once-viewed crop journal.",
}


def dump(name,obj):
    p=OUT/name;p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n")
    return {"path":p.relative_to(ROOT).as_posix(),"sha256_utf8":sha(p.read_bytes()),"bytes":p.stat().st_size}


union_rec=dump("scan025_source_union_v01.json",UNION)
skeleton={"scan":25,"source_only":True,"shared_pool":UNION["shared_pool"],"source_union":union_rec,
          "schema_note":"All three own-reader fields bind their complete own local frame, complete own groups, raw doubts and inventory scopes. Raw C/H witness fields stay in their original role. Every selected field is pending.",
          "rows":list(ROWS.values()),"canonical_original_C_rows":CANON,"source_role_cautions":CAUTIONS,"mapping_gaps":GAPS,
          "main_adjudicated":False,"main_approved":False}
sk_rec=dump("scan025_source_row_skeleton_v01.json",skeleton)
rows_path=OUT/"scan025_source_row_skeleton_v01.jsonl"
rows_path.write_text("".join(json.dumps(row,ensure_ascii=False,separators=(",",":"))+"\n" for row in ROWS.values()))
summary={"scan":25,"source_only":True,"pool":UNION["shared_pool"],"source_union":union_rec,"row_skeleton":sk_rec,
         "counts":UNION["counts"],"mapping_gaps":GAPS,"source_role_cautions":CAUTIONS,
         "read_order":["scan025_source_union_summary_v01.json","scan025_source_row_skeleton_v01.jsonl","scan025_source_union_v01.json (exact frames/groups/commands/raw correspondences as referenced)"],
         "main_adjudicated":False,"main_approved":False}
dump("scan025_source_union_summary_v01.json",summary)
print(json.dumps({"source_union":union_rec,"row_skeleton":sk_rec,"counts":UNION["counts"],"mapping_gaps":GAPS},ensure_ascii=False,indent=2))
