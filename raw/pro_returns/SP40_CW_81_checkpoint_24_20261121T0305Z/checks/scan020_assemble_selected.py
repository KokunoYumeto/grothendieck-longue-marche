"""Assemble only root-selected scan020 source, retaining exact provenance.

This script opens text sources only. It does not render, compile, inspect images,
calculate geometry or verify any mathematical assertion.
"""
from pathlib import Path
import copy
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "out/checks"
FINAL = "out/checks/scan020_final_draft.tex"
MAP = "out/checks/scan020_final_source_map.json"
ATTACHMENT_PATH = "checks/scan020_final_draft.tex"
ROOT_GRAPHICS = "out/checks/scan020_root_graphics.tex"
JOURNAL = "out/checks/scan020_main_decisions.md"
ROOT_GRAPHICS_SHA = "96adf87c927e356989b13670dd27a8fecca782c8072c4e460fa133980b1f53e6"
sha = lambda b: hashlib.sha256(b).hexdigest()
source_texts = {}


def text(path):
    if path not in source_texts:
        source_texts[path] = (ROOT / path).read_text(encoding="utf-8")
    return source_texts[path]


def source_ref(path, a=0, b=None):
    t = text(path)
    b = len(t) if b is None else b
    assert 0 <= a < b <= len(t)
    s = t[a:b]
    return dict(path=path, manifest=path, char_start=a, char_end=b,
                byte_start=len(t[:a].encode()), byte_end=len(t[:b].encode()),
                line_start=t.count("\n", 0, a)+1,
                line_end=t.count("\n", 0, b-1)+1,
                excerpt=s, literal=s, literal_sha256_utf8=sha(s.encode()),
                source_sha256_utf8=sha(t.encode()))


def locate(path, value, occurrence=0):
    t, start = text(path), 0
    for _ in range(occurrence+1):
        a = t.index(value, start)
        start = a+len(value)
    return source_ref(path, a, a+len(value))


def source_piece(ref):
    return dict(text=ref["excerpt"], source_path=ref["path"],
                source_char_start=ref["char_start"], source_char_end=ref["char_end"])


def syntax_piece(value, purpose):
    return dict(text=value, source_path=None, source_kind="source-only assembly syntax",
                purpose=purpose)


def slice_piece(p, a, b):
    q = dict(p)
    q["text"] = p["text"][a:b]
    if p["source_path"]:
        q["source_char_start"] = p["source_char_start"]+a
        q["source_char_end"] = p["source_char_start"]+b
    return q


def range_pieces(items, a, b):
    out, cursor = [], 0
    for p in items:
        end = cursor+len(p["text"])
        left, right = max(cursor,a), min(end,b)
        if left < right:
            out.append(slice_piece(p,left-cursor,right-cursor))
        cursor = end
    assert sum(len(p["text"]) for p in out) == b-a
    return out


def piece_provenance(p):
    if p["source_path"]:
        return source_ref(p["source_path"],p["source_char_start"],p["source_char_end"])
    return dict(path=None, source_kind=p["source_kind"], purpose=p["purpose"],
                excerpt=p["text"],literal=p["text"],literal_sha256_utf8=sha(p["text"].encode()))


base = "out/readers/020/A/reading.tex"
pieces = [source_piece(source_ref(base))]
replacements = []


def current():
    return "".join(p["text"] for p in pieces)


def replace(old, new_pieces, rid, decisions, reason, occurrence=0, expected=1):
    global pieces
    before = current()
    assert before.count(old) == expected, (rid,before.count(old),expected)
    start = 0
    for _ in range(occurrence+1):
        a = before.index(old,start)
        start = a+len(old)
    b = a+len(old)
    removed = range_pieces(pieces,a,b)
    pieces = range_pieces(pieces,0,a) + copy.deepcopy(new_pieces) + range_pieces(pieces,b,len(before))
    new = "".join(p["text"] for p in new_pieces)
    replacements.append(dict(id=rid,decision_ids=decisions,reason=reason,
        stage_char_start=a,stage_char_end=b,old_text=old,new_text=new,
        stage_before_sha256_utf8=sha(before.encode()),stage_after_sha256_utf8=sha(current().encode()),
        removed_source_pieces=[piece_provenance(p) for p in removed],
        inserted_source_pieces=[piece_provenance(p) for p in new_pieces]))


candidates = json.loads((OUT / "scan020_tex_candidates.json").read_text())
candidate_groups = {g["id"]:g for g in candidates["graphic_groups"]}


def candidate_ref(gid):
    r = candidate_groups[gid]["full_source"]
    return source_ref(r["path"],r["char_start"],r["char_end"])


assert sha((ROOT / ROOT_GRAPHICS).read_bytes()) == ROOT_GRAPHICS_SHA
root_groups = {}
for n in range(1,7):
    gid = f"R020-G{n:02d}"
    t = text(ROOT_GRAPHICS)
    a = t.index(f"% BEGIN {gid}")
    b = t.index(f"% END {gid}",a)+len(f"% END {gid}")
    root_groups[gid] = source_ref(ROOT_GRAPHICS,a,b)

replace(r"\unsure{clas.|deux.}",
        [source_piece(locate(JOURNAL,r"\unsure{clas|deux}."))],
        "REP020-01",["L020-04","L020-05"],"Root-selected word candidates and separate terminal point.")
replace(r"\Sigma_{\unsure{j|\deleted{J}i|i}}^+",
        [syntax_piece("\n","Place the complete root source comment and math group on separate physical lines."),
         source_piece(root_groups["R020-G01"]),syntax_piece("\n","End source comment before the existing comma.")],
        "REP020-02",["L020-06","L020-07"],"Replace the complete positive Sigma/index/plus with the exact root group.")
replace(r"\Sigma_i^-",
        [syntax_piece("\n","Place the complete root source comment and math group on separate physical lines."),
         source_piece(root_groups["R020-G02"])],
        "REP020-03",["L020-08"],"Replace the first paired negative Sigma/index/minus with the exact root group.",expected=2)
replace(candidate_ref("A020-G01")["excerpt"],
        [syntax_piece("$\n","The selected root mathord glyph requires the existing inline mathematical context."),
         source_piece(root_groups["R020-G03"]),syntax_piece("\n$","Close inline math after the complete root group.")],
        "REP020-04",["L020-09","L020-10"],"Replace the whole cancelled Sigma group; no generic Sigma or cancellation is retained beside it.")
replace(r"\overline{\Sigma_i^+}",
        [source_piece(root_groups["R020-G04"]),syntax_piece("\n","End source comment before the existing cap expression.")],
        "REP020-05",["L020-16","L020-17"],"Replace the entire first overlined Sigma with the complete long-rule/head/body/index/plus root group.")
replace(candidate_ref("A020-G03")["excerpt"],[source_piece(root_groups["R020-G05"])],
        "REP020-06",["L020-23"],"Use exact root-selected interrupted second cancellation run with A's complete word-bearing group.")
replace(r"\unsure{dém.|dem.}",[source_piece(locate("out/readers/020/B/reading.tex",r"\unsure{dèm.|dém.|dem.}"))],
        "REP020-07",["L020-26"],"Root-selected grave/acute/unaccented abbreviation candidates.")
replace(candidate_ref("A020-G05")["excerpt"],[source_piece(candidate_ref("B_G03"))],
        "REP020-08",["L020-29","L020-30","L020-31","L020-32"],"Transplant B's complete source block, with X setminus outside its inner TikZ.")
replace(r"\alpha\in\unsure{\deleted{I}K|K}",[source_piece(locate(base,r"\alpha\in\deleted{I}K"))],
        "REP020-09",["L020-30"],"Resolve only the union-index node to the root-selected deleted I followed by K.")
old = "où $K$ est une partie\n"+candidate_ref("A020-G06")["excerpt"]
csp = candidate_ref("C_G03--G04")
c_start = text(csp["path"]).rfind("où $K$ est une\n",0,csp["char_start"])
assert c_start >= 0
replace(old,[source_piece(source_ref(csp["path"],c_start,csp["char_end"]))],
        "REP020-10",["L020-33","L020-34"],"Select C's complete word-bearing figure, owning partie/non vide/de I comma, with et outside.")
old_margin = "% slanted\n"+text(base).split("% slanted\n",1)[1].split("\n$\\forall",1)[0]
c_margin_start = text(csp["path"]).index("% slanted;")
c_margin_end = text(csp["path"]).index("\n$\\forall",c_margin_start)
margin_source = source_ref(csp["path"],c_margin_start,c_margin_end)
replace(old_margin,[source_piece(margin_source)],
        "REP020-11",["L020-38"],"Use C's complete two-line rotatebox{23} margin source, with its exact words and symbols.")
replace(candidate_ref("A020-G07")["excerpt"],[source_piece(root_groups["R020-G06"])],
        "REP020-12",["L020-36"],"Use B's selected relation paths with root's exact overlay phantom complete-state annotation.")

final_text = current()
final_sha = sha(final_text.encode())
(ROOT / FINAL).write_text(final_text,encoding="utf-8")


def final_span(a,b,identity=None):
    assert 0 <= a < b <= len(final_text),(identity,a,b)
    s=final_text[a:b]
    ref=dict(path=ATTACHMENT_PATH,workspace_path=FINAL,
             manifest="checks/scan020_final_source_map.json",workspace_manifest_path=MAP,
             char_start=a,char_end=b,byte_start=len(final_text[:a].encode()),byte_end=len(final_text[:b].encode()),
             line_start=final_text.count("\n",0,a)+1,line_end=final_text.count("\n",0,b-1)+1,
             excerpt=s,literal=s,literal_sha256_utf8=sha(s.encode()),
             body_sha256=sha(s.encode()),final_file_sha256=final_sha,
             draft_sha256_utf8=final_sha)
    if identity:ref["attachment_id"]=identity
    return ref


def find_final(value,identity=None,within=None,occurrence=0):
    low=0 if within is None else within["char_start"]
    high=len(final_text) if within is None else within["char_end"]
    start=low
    for _ in range(occurrence+1):
        a=final_text.index(value,start,high)
        start=a+len(value)
    return final_span(a,a+len(value),identity)


def between_final(first,last,identity=None,include_last=False,occurrence=0):
    a=find_final(first,occurrence=occurrence)["char_start"]
    b=final_text.index(last,a+len(first))
    if include_last:b+=len(last)
    return final_span(a,b,identity)


def statement_end(t,a):
    depth=0
    for i in range(a,len(t)):
        ch=t[i]
        if ch=="{" and (i==0 or t[i-1]!="\\"):depth+=1
        elif ch=="}" and (i==0 or t[i-1]!="\\"):depth-=1
        elif ch==";" and depth==0:return i+1
    raise ValueError("No end of source command")


def macro_end(t,a):
    opening=t.index("{",a)
    depth=0
    for i in range(opening,len(t)):
        if t[i]=="{" and (i==0 or t[i-1]!="\\"):depth+=1
        elif t[i]=="}" and (i==0 or t[i-1]!="\\"):
            depth-=1
            if depth==0:return i+1
    raise ValueError("No end of source macro")


segments=[]
cursor=0
for i,p in enumerate(pieces,1):
    end=cursor+len(p["text"])
    segments.append(dict(id=f"SEG020-{i:03d}",final=final_span(cursor,end),source=piece_provenance(p)))
    cursor=end
assert cursor==len(final_text)


def provenance_for_final(a,b):
    selected=[]
    for seg in segments:
        fa,fb=seg["final"]["char_start"],seg["final"]["char_end"]
        lo,hi=max(a,fa),min(b,fb)
        if lo>=hi:continue
        src=seg["source"]
        if src["path"]:
            selected.append(source_ref(src["path"],src["char_start"]+lo-fa,src["char_start"]+hi-fa))
        else:
            selected.append(dict(path=None,source_kind=src["source_kind"],purpose=src["purpose"],
                                 excerpt=final_text[lo:hi],literal=final_text[lo:hi]))
    assert "".join(s["excerpt"] for s in selected)==final_text[a:b]
    return selected


group_specs=[(gid,root_groups[gid],ids) for gid,ids in [
    ("R020-G01",["L020-06","L020-07"]),("R020-G02",["L020-08"]),
    ("R020-G03",["L020-09","L020-10"]),("R020-G04",["L020-16","L020-17"]),
    ("R020-G05",["L020-23"]),("R020-G06",["L020-36"])]]
group_specs += [("A020-G02",candidate_ref("A020-G02"),["L020-11"]),
                ("A020-G04",candidate_ref("A020-G04"),["L020-25"]),
                ("B_G03",candidate_ref("B_G03"),["L020-29","L020-30","L020-31","L020-32"]),
                ("C_G03--G04",candidate_ref("C_G03--G04"),["L020-33","L020-34"]),
                ("C_MARGIN",margin_source,["L020-38"])]
selected_groups=[]
for gid,src,ids in group_specs:
    value=src["excerpt"]
    if gid=="B_G03":value=value.replace(r"\alpha\in\unsure{\deleted{I}K|K}",r"\alpha\in\deleted{I}K")
    f=find_final(value,gid)
    literal_components=[]
    structure=[]
    annotations=[]
    for m in re.finditer(r"\\(draw|fill|path|useasboundingbox|node|phantom)\b",value):
        a=f["char_start"]+m.start()
        line=final_text[final_text.rfind("\n",0,a)+1:a]
        if "%" in line:continue
        command=m.group(1)
        b=macro_end(final_text,a) if command=="phantom" else statement_end(final_text,a)
        assert b<=f["char_end"]
        target=annotations if command=="phantom" else literal_components if command in ["draw","fill"] else structure
        identity=f"{gid}-{command.upper()}-{len(target)+1:02d}"
        target.append(dict(id=identity,command=command,
                           final_source_attachment=final_span(a,b,identity),
                           exact_source_pieces=provenance_for_final(a,b)))
    comments=[]
    declarations=[]
    for m in re.finditer(r"(?m)^.*$",value):
        if m.group().startswith("%"):
            comments.append(final_span(f["char_start"]+m.start(),f["char_start"]+m.end()))
        if "\\begin{tikzpicture}" in m.group():
            declarations.append(final_span(f["char_start"]+m.start(),f["char_start"]+m.end()))
    selected_groups.append(dict(id=gid,decision_ids=ids,source=src,final_source_attachment=f,
        selected_exact_source=value,source_comments=comments,tikz_declaration_lines=declarations,
        literal_components=literal_components,structural_components=structure,annotation_support=annotations,
        exact_source_pieces=provenance_for_final(f["char_start"],f["char_end"]),
        source_metadata=candidate_groups.get(gid,{}).get("raw_report_group"),
        source_modification_ids=["REP020-09"] if gid=="B_G03" else [],
        main_approved=False))
selected_groups.sort(key=lambda g:g["final_source_attachment"]["char_start"])
gmap={g["id"]:g for g in selected_groups}


def GF(gid):return copy.deepcopy(gmap[gid]["final_source_attachment"])
def PC(gid,n):return copy.deepcopy(gmap[gid]["literal_components"][n]["final_source_attachment"])
def NODE(gid,n):
    return copy.deepcopy([x["final_source_attachment"] for x in gmap[gid]["structural_components"] if x["command"]=="node"][n])
def PH(gid,n=0):return copy.deepcopy(gmap[gid]["annotation_support"][n]["final_source_attachment"])

pair=between_final("\\[","\\]","BLOCK020-PAIRED",True)
nonempty=between_final("\\[","\\]","BLOCK020-NONEMPTY",True,1)
upper=between_final("qui sont non vides.","\\[","BLOCK020-UPPER-PROSE")
count_paragraph=between_final("On sait donc", "\n\n\\uline{Lemme}","BLOCK020-COUNT-PARAGRAPH")
lemma_heading=find_final(r"\uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme","BLOCK020-LEMMA-HEADING")
lemma_prose=between_final("où $K$ est une","% slanted;","BLOCK020-LEMMA-PROSE")
final_clauses=between_final("tels que","\n% archive","BLOCK020-FINAL-CLAUSES")
whole_lemma=between_final(r"\uline{Lemme}","\n% archive","BLOCK020-LEMMA")
top=final_span(0,pair["char_start"],"BLOCK020-TOP")
archive=find_final("% archive sheet number: 19","BLOCK020-ARCHIVE")
blocks=[top,pair,upper,nonempty,count_paragraph,lemma_heading,GF("B_G03"),lemma_prose,GF("C_MARGIN"),final_clauses,archive]

atts={}
def put(n,refs):
    did=f"L020-{n:02d}"
    atts[did]=copy.deepcopy(refs)
    for i,r in enumerate(atts[did],1):
        r["attachment_id"]=f"{did}-{i:02d}"

put(1,[find_final(r"\Pi_I^{\unsure{\circ|0}}")])
put(2,[find_final(r"\Pi_J^\circ")])
put(3,[find_final(r"$\deleted{\Pi}U_{J,i}$,")])
put(4,[find_final(r"\unsure{clas|deux}")])
word=atts["L020-04"][0]
put(5,[final_span(word["char_end"],word["char_end"]+1)])
put(6,[GF("R020-G01"),PH("R020-G01")])
put(7,[GF("R020-G01"),PC("R020-G01",0)])
put(8,[GF("R020-G02"),PC("R020-G02",0),PH("R020-G02")])
put(9,[GF("R020-G03"),PH("R020-G03")])
put(10,[GF("R020-G03"),PC("R020-G03",0)])
put(11,[GF("A020-G02"),PC("A020-G02",0)])
put(12,[find_final(r"E_{\unsure{i|j}}",within=upper)])
put(13,[find_final(r"\deleted{\Sigma}E_{\unsure{i|j}}",within=upper)])
ec=find_final(r"E_{\unsure{i|j}}$, et",within=upper)
comma=ec["char_start"]+len(r"E_{\unsure{i|j}}$")
put(14,[final_span(comma,comma+1)])
put(15,[find_final(r"\deleted{\Sigma}E_i",within=nonempty)])
put(16,[GF("R020-G04"),PC("R020-G04",0),PH("R020-G04")])
put(17,[GF("R020-G04"),PC("R020-G04",1)])
put(18,[find_final(r"\overline{\deleted{E}\Sigma_i^-}",within=nonempty)])
put(19,[find_final(r"\deleted{\Sigma}E_i",within=nonempty,occurrence=1)])
put(20,[find_final(r"\overline{\deleted{E}\Sigma_i^-}",within=nonempty)])
put(21,[find_final("sait",within=count_paragraph)])
lead=find_final("On sait donc que le nb des classes est en",within=count_paragraph)
put(22,[final_span(lead["char_end"]-2,lead["char_end"])])
put(23,[GF("R020-G05"),NODE("R020-G05",0)])
put(24,[find_final(r"\unsure{aussi|ainsi}")])
put(25,[GF("A020-G04"),PC("A020-G04",0)])
put(26,[find_final(r"\unsure{dèm.|dém.|dem.}")])
put(27,[find_final(r"\unsure{par|p}")])
put(28,[find_final(r"\Pi_I^\circ",within=lemma_heading)])
put(29,[GF("B_G03"),PC("B_G03",0),PC("B_G03",1),PC("B_G03",2)])
put(30,[NODE("B_G03",0),find_final(r"\alpha\in\deleted{I}K",within=GF("B_G03"))])
put(31,[GF("B_G03"),PC("B_G03",3),PC("B_G03",4),PC("B_G03",5)])
put(32,[NODE("B_G03",2)])
put(33,[GF("C_G03--G04"),NODE("C_G03--G04",2),PC("C_G03--G04",0)])
put(34,[GF("C_G03--G04"),PC("C_G03--G04",1)])
put(35,[find_final(r"\deleted{on a}")])
put(36,[GF("R020-G06"),PH("R020-G06")])
put(37,[find_final(r"{\unsure{E|\deleted{\Sigma}E}}_\alpha")])
put(38,[GF("C_MARGIN")])
put(39,[archive])
put(40,[find_final(r"\scanpage{20}"),archive,find_final(r"\uline{Lemme}")])
put(41,[nonempty])

direct_map={
"RING1":1,"RING2":2,"PI-PREDECESSOR":3,"CLAS-WORD":4,"CLAS-POINT":5,
"PAIR-INDEX":6,"POSITIVE-SIGMA-HEAD":7,"NEGATIVE-SIGMA-HEAD":8,
"CANCELLED-SIGMA":9,"CANCELLED-SIGMA-HEAD":10,"VOISINAGE-POINT":11,
"E-INDEX":12,"E-PREDECESSOR":13,"E-COMMA":14,"BAR1-E-PREDECESSOR":15,
"BAR1":16,"BAR1-SIGMA-HEAD":17,"BAR2-SIGMA-PREDECESSOR":18,"BAR2-E-PREDECESSOR":19,
"BAR2":20,"VOIT":21,"EN":22,"COUNT-WORD":23,"AUSSI":24,"LA-POINT":25,
"DEM":26,"PAR":27,"RING3":28,"UNION":29,"UNION-INDEX":30,"BRACE":31,
"HAT-LABEL":32,"NONVIDE":33,"GUIDE":34,"ONA":35,"MEMBERSHIP":36,
"MEMBERSHIP-E":37,"MARGIN":38,"ARCHIVE":39,"CONVENTION":40,"S-AUDIT":41}
by_source={f"SRC020-{key}":copy.deepcopy(atts[f"L020-{n:02d}"]) for key,n in direct_map.items()}
remainder={
"PAIRED-REMAINDER":[pair],"UPPER-PROSE":[upper],"NONEMPTY-ENDPOINTS":[nonempty],
"COUNT":[count_paragraph],"ACHEVE":[find_final("ce qui achève",within=count_paragraph)],
"RECURRENCE":[find_final("récurrence",within=count_paragraph)],
"NB1":[find_final("nb",within=count_paragraph)],"NB2":[find_final("nb",within=count_paragraph,occurrence=1)],
"CARD":[find_final(r"\operatorname{card}",within=count_paragraph)],
"LEMMA-HEADING":[lemma_heading],"LEMMA-PROSE":[lemma_prose],"FINAL-CLAUSES":[final_clauses]}
for name,refs in remainder.items():by_source[f"SRC020-{name}"]=copy.deepcopy(refs)
put(42,[ref for refs in remainder.values() for ref in refs])
by_source["SRC020-AGREED-REMAINDER"]=copy.deepcopy(atts["L020-42"])

inv={
"020.01":[top],"020.02":atts["L020-03"],"020.03":[pair],"020.04":atts["L020-06"],
"020.05":[upper],"020.06":atts["L020-09"],"020.07":atts["L020-13"],"020.08":[nonempty],
"020.09":atts["L020-15"],"020.10":atts["L020-18"],"020.11":atts["L020-19"],
"020.12":[count_paragraph],"020.13":atts["L020-23"],"020.14":[whole_lemma],
"020.15":atts["L020-30"],"020.16":atts["L020-32"],"020.17":atts["L020-33"],
"020.18":atts["L020-33"],"020.19":atts["L020-38"],"020.20":atts["L020-35"],"020.21":atts["L020-36"]}
inv_groups={
"TOP":[top],"PI-PREDECESSOR":atts["L020-03"],"PAIRED":[pair],"PAIR-INDEX":atts["L020-06"],
"UPPER-PROSE":[upper],"CANCELLED-SIGMA":atts["L020-09"],"VOISINAGE-POINT":atts["L020-11"],
"E-PREDECESSOR":atts["L020-13"],"NONEMPTY":[nonempty],"BAR1-E-PREDECESSOR":atts["L020-15"],
"BAR2-SIGMA-PREDECESSOR":atts["L020-18"],"BAR2-E-PREDECESSOR":atts["L020-19"],
"COUNT":[count_paragraph],"COUNT-WORD":atts["L020-23"],"LA-POINT":atts["L020-25"],
"LEMMA-PROSE":[whole_lemma],"LEMMA-FORMULA":[GF("B_G03")],"UNION":atts["L020-29"],
"UNION-INDEX":atts["L020-30"],"HAT-LABEL":atts["L020-32"],"BRACE":atts["L020-31"],
"NONVIDE":atts["L020-33"],"GUIDE":atts["L020-34"],"MARGIN":atts["L020-38"],
"ONA":atts["L020-35"],"MEMBERSHIP":atts["L020-36"],"MEMBERSHIP-E":atts["L020-37"],
"FINAL":[final_clauses],"ARCHIVE":[archive]}
inv_groups={"SRC020-INV-"+k:copy.deepcopy(v) for k,v in inv_groups.items()}

c_parts={"C020-R01-1":1,"C020-R01-2":2,"C020-R01-3":28,
"C020-R02-1":4,"C020-R03-1":6,"C020-R04-1":9,"C020-R05-1":12,
"C020-R06-1":23,"C020-R07-1":26,"C020-R08-1":30,"C020-R09-1":36,
"C020-R10-1":21,"C020-R11-1":24}
c_doubts={part:dict(decision_id=f"L020-{n:02d}",final_source_attachment=copy.deepcopy(atts[f"L020-{n:02d}"])) for part,n in c_parts.items()}
c_rows={}
for part,item in c_doubts.items():
    row=part.rsplit("-",1)[0]
    c_rows.setdefault(row,dict(source_parts=[],final_source_attachment=[]))
    c_rows[row]["source_parts"].append(part)
    c_rows[row]["final_source_attachment"].extend(copy.deepcopy(item["final_source_attachment"]))

journal=text(JOURNAL)
root_decisions={}
for n in range(1,43):
    did=f"L020-{n:02d}"
    m=re.search(r"(?m)^"+did+r"(?=[ /\.:,])",journal)
    assert m,did
    stop=re.search(r"(?m)^(?:L020-\d\d(?=[ /\.:,])|## )",journal[m.end():])
    b=m.end()+stop.start() if stop else len(journal)
    root_decisions[did]=dict(root_journal_source=source_ref(JOURNAL,m.start(),b),
         root_ink_choice_applied=n<=39,root_source_audit_choice_applied=n>=40,main_approved=False)

note_entries=[
dict(id="CONTENT020-01",text="Grothendieck identifies the classes in the opening sentence and follows the paired intersections with the words ‘qui sont non vides.’ The selected source retains the local qualifications of the glyphs and their states.",
     source_attachments=[top,pair,upper,nonempty]),
dict(id="CONTENT020-02",text="The manuscript writes the class count and the parenthesis containing ‘ce qui achève’ and ‘récurrence sur le nb des classes’. The abbreviation and compressed par/p retain the selected qualifications.",
     quoted_tex=r"(n-1)+2=n+1=\operatorname{card} I+1",
     source_attachments=[find_final(r"$(n-1)+2=n+1=\operatorname{card} I+1$"),
                         between_final("(ce qui achève", "\n\n\\uline{Lemme}")]),
dict(id="CONTENT020-03",text="Under the underlined Lemme, Grothendieck gives the displayed complement and union expression with its raised hatted label, then the written statement about K. The selected source preserves the cancelled insertion non vide and its guide with the adjoining words.",
     source_attachments=[lemma_heading,GF("B_G03"),lemma_prose,GF("C_MARGIN")]),
dict(id="CONTENT020-04",text="The manuscript continues with the qualified relation before pi_0 and the conditions ending in hatted-set disjointness. Its final parenthesis writes a double implication with the following unhatted intersection statement. These are attributed manuscript assertions; no equivalence or proof check was performed.",
     source_attachments=[between_final(r"$\forall\alpha\in K$,", "tels que"),final_clauses],
     final_parenthetical_source=find_final(r"$(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.",within=final_clauses))]
note=dict(scan=20,scope="Attributed description of selected manuscript content; no mathematical verification.",
          draft_path=ATTACHMENT_PATH,workspace_draft_path=FINAL,draft_sha256_utf8=final_sha,
          entries=note_entries,mathematical_check_performed=False,main_approved=False)
(OUT/"scan020_attributed_content_note.json").write_text(json.dumps(note,ensure_ascii=False,indent=2)+"\n")
note_md=["# Scan020 — attributed manuscript content", "", "The statements below describe the selected manuscript source. No mathematical verification was performed.", ""]
for e in note_entries:
    note_md += ["## "+e["id"],"",e["text"],""]
    for sp in e["source_attachments"]:
        note_md += [f"Exact selected source: `{ATTACHMENT_PATH}` characters `[{sp['char_start']},{sp['char_end']})`.",""]
note_md += [f"Selected draft UTF-8 SHA-256: `{final_sha}`.",""]
(OUT/"scan020_attributed_content_note.md").write_text("\n".join(note_md))

source_map=dict(schema="scan020 exact selected-source map v02",status="root-selected draft; final root approval pending",
 main_adjudicated=False,main_approved=False,
 scope="Current-page source-only assembly; exact selected bytes and attachments; no rendering, image work, metric result or theorem check.",
 offset_convention="Zero-based half-open Unicode character offsets; byte offsets refer to UTF-8.",
 final_path=FINAL,attachment_path_relative_to_out=ATTACHMENT_PATH,final_sha256=final_sha,
 draft_sha256_utf8=final_sha,final_sha256_utf8=final_sha,base_source=base,base_sha256=sha(text(base).encode()),
 source_files={p:dict(path=p,sha256=sha(t.encode()),utf8_byte_length=len(t.encode())) for p,t in source_texts.items()},
 source_segments=segments,replacements=replacements,selected_groups=selected_groups,
 final_blocks=[dict(id=s["attachment_id"],final_source_attachment=s) for s in blocks],
 attachments_by_decision=atts,attachments_by_source_locus=by_source,
 original_inventory_source_attachments=copy.deepcopy(inv),attachments_by_inventory_source_group=inv_groups,
 selected_graphic_inventory_source_attachments={g["id"]:[g["final_source_attachment"]] for g in selected_groups},
 archive_inventory_source_attachment=[archive],original_C_doubt_attachments=c_rows,
 original_C_doubt_part_attachments=c_doubts,root_authorizations=root_decisions,
 root_journal=dict(path=JOURNAL,sha256=sha(journal.encode())),
 root_graphics=dict(path=ROOT_GRAPHICS,sha256=ROOT_GRAPHICS_SHA),
 preamble=dict(path="out/PREAMBLE.tex",sha256=sha((ROOT/"out/PREAMBLE.tex").read_bytes())),
 component_count_scope="Counts below describe literal source commands only; physical correction and confidence choices remain the root's recorded choices.",
 attributed_content_note=note,
 processing_provenance=["A reading.tex is the exact unchanged-source base.",
 "All 12 replacements have exact old/new literals and source pieces; selected source parts are copied without coordinate calculation.",
 "The added math delimiters and line boundaries serve the complete root group's TeX context and contain no manuscript content.",
 "Raw A/B/C source files remain unchanged; original C row/part and inventory identities retain separate attachments."])

# One targeted source pass: exact coverage, source identities, selected paths,
# delimiters and required attachment keys. This does not execute TeX.
errors=[]
if set(atts)!={f"L020-{i:02d}" for i in range(1,43)}:errors.append("Decision attachment coverage")
crosswalk=json.loads((OUT/"scan020_source_crosswalk.json").read_text())
crosswalk_ids={l["source_locus_id"] for l in crosswalk["loci"]}
missing=sorted(crosswalk_ids-set(by_source))
if missing:errors.append("Missing source-locus attachments: "+repr(missing))
if set(inv)!={f"020.{i:02d}" for i in range(1,22)}:errors.append("Original inventory coverage")
if len(c_doubts)!=13 or len(c_rows)!=11:errors.append("Original C row/part coverage")
selected_command_count=sum(len(g["literal_components"]) for g in selected_groups)
code="\n".join(line.split("%",1)[0] for line in final_text.splitlines())
all_commands=list(re.finditer(r"\\(?:draw|fill)\b",code))
if len(all_commands)!=selected_command_count:errors.append("Literal command coverage")
brace_stack=[]
for m in re.finditer(r"\\[{}]|[{}]",code):
    if m.group()=="{":brace_stack.append(m.start())
    elif m.group()=="}":
        if not brace_stack:errors.append("Unmatched closing brace")
        else:brace_stack.pop()
if brace_stack:errors.append("Unclosed braces")
env_stack=[]
for m in re.finditer(r"\\(begin|end)\{([^}]+)\}",code):
    if m.group(1)=="begin":env_stack.append(m.group(2))
    elif not env_stack or env_stack.pop()!=m.group(2):errors.append("Environment mismatch")
if env_stack:errors.append("Unclosed environment")
if code.count("$")%2:errors.append("Uneven dollar delimiter count")
if code.count(r"\[")!=code.count(r"\]"):errors.append("Display delimiter mismatch")
for m in re.finditer(r"\\\[(.*?)\\\]",final_text,re.S):
    if re.search(r"\n[ \t]*\n",m.group(1)):errors.append("Physical blank inside display")
for gid in [f"R020-G{i:02d}" for i in range(1,7)]:
    if final_text.count(root_groups[gid]["excerpt"])!=1:errors.append("Root source group occurrence "+gid)
for gid in ["A020-G02","A020-G04","C_G03--G04"]:
    if final_text.count(candidate_ref(gid)["excerpt"])!=1:errors.append("Exact selected group occurrence "+gid)
if final_text.count(gmap["B_G03"]["selected_exact_source"])!=1:errors.append("Selected B group occurrence")
if r"\alpha\in\unsure{\deleted{I}K|K}" in final_text:errors.append("Unresolved old union-index source remains")
if r"\deleted{\Rightarrow}\in|\deleted{\to}\in|\in" not in PH("R020-G06")["excerpt"]:errors.append("Full relation states missing from phantom")
if r"\figure" not in GF("C_G03--G04")["excerpt"]:errors.append("C full figure wrapper missing")
if final_text[GF("C_G03--G04")["char_end"]:].splitlines()[1]!="et":errors.append("C figure et boundary")
spans_checked=0
def check_refs(value):
    global spans_checked
    if isinstance(value,dict):
        if value.get("path")==ATTACHMENT_PATH and {"char_start","char_end","excerpt"}<=value.keys():
            a,b=value["char_start"],value["char_end"]
            if final_text[a:b]!=value["excerpt"]:errors.append("Final attachment literal mismatch")
            if value.get("final_file_sha256")!=final_sha:errors.append("Final attachment hash mismatch")
            spans_checked+=1
        for v in value.values():check_refs(v)
    elif isinstance(value,list):
        for v in value:check_refs(v)
check_refs(source_map)
for seg in segments:
    if seg["source"]["excerpt"]!=seg["final"]["excerpt"]:errors.append("Provenance segment mismatch")
for p,info in candidates["sources"].items():
    if p.startswith("out/readers/") and sha((ROOT/p).read_bytes())!=info["sha256_utf8"]:
        errors.append("Reader input changed: "+p)
audit=dict(scan=20,scope="One targeted source-only pass over exact selected coverage, provenance pieces, source identities, selected commands, attachment keys, source delimiters and unchanged reader inputs.",
 draft_path=FINAL,draft_sha256_utf8=final_sha,replacements=len(replacements),
 selected_complete_groups=len(selected_groups),literal_draw_fill_commands=selected_command_count,
 final_attachment_spans_checked=spans_checked,decision_attachments=len(atts),source_locus_attachments=len(by_source),
 original_C_inventory_attachments=len(inv),original_C_rows=len(c_rows),original_C_parts=len(c_doubts),
 final_character_length=len(final_text),final_utf8_byte_length=len(final_text.encode()),
 source_partition_complete=True,reader_inputs_unchanged=True,errors=errors,
 images_opened=0,compilation_performed=False,rendering_performed=False,geometry_calculation_performed=False,
 mathematical_check_performed=False,main_adjudicated=False,main_approved=False)
if errors:
    (OUT/"scan020_assembly_audit_failed.json").write_text(json.dumps(audit,ensure_ascii=False,indent=2)+"\n")
    raise AssertionError(errors)
audit_path=OUT/"scan020_assembly_audit.json"
audit_path.write_text(json.dumps(audit,ensure_ascii=False,indent=2)+"\n")
source_map["assembly_audit"]=dict(path="out/checks/scan020_assembly_audit.json",sha256=sha(audit_path.read_bytes()),passed=True)
(ROOT/MAP).write_text(json.dumps(source_map,ensure_ascii=False,indent=2)+"\n")
summary=dict(draft=FINAL,draft_sha256_utf8=final_sha,source_map=MAP,
 source_map_sha256_utf8=sha((ROOT/MAP).read_bytes()),audit_sha256_utf8=sha(audit_path.read_bytes()),
 attributed_note_sha256_utf8=sha((OUT/"scan020_attributed_content_note.json").read_bytes()),
 literal_draw_fill_commands=selected_command_count,decision_attachments=len(atts),source_loci=len(by_source),
 actual_remaining_source_issues=[],main_approved=False)
(OUT/"scan020_assembly_handoff.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(summary,indent=2))
