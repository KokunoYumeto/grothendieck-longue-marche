"""Mechanical, text-only scan013 record assembly. Never commits a main record.

Reads the assigned witnesses, preserved reader returns, schema conventions and
the supplied root decision log. Writes only the two named provisional outputs.
All ink choices require a literal, cited entry in ROOT_CHOICES.
"""
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "out"
CHECKS = OUT / "checks"
REPORTS = {r: json.loads((OUT / "readers/013" / r / "report.json").read_text()) for r in "ABC"}
TEX = {r: (OUT / "readers/013" / r / "reading.tex").read_text().splitlines() for r in "ABC"}
SOURCE_INV = json.loads((ROOT / "packets/013/C_inventory.json").read_text())
META = json.loads((ROOT / "packets/013/metadata.json").read_text())
EXPECTED = json.loads((CHECKS / "scan013_reader_fingerprints.json").read_text())
ROOT_LOG_PATH = "out/checks/scan013_main_decisions.md"
ROOT_LOG = (ROOT / ROOT_LOG_PATH).read_text()
ASSEMBLY_DATE = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

# Only explicit root instructions may populate this dictionary. Each value must
# carry a root_log_entry and exact root excerpt. Empty means no ink adjudication.
ROOT_CHOICES = {}
ROOT_PAGE_SOURCE = None
root_grid_section = re.search(r"(?ms)^## 01–10\..*?(?=^## |\Z)", ROOT_LOG)
if root_grid_section:
    ROOT_CHOICES["grid"] = {
      "root_log_entry":"01–10",
      "root_exact_excerpt":root_grid_section.group(0).rstrip(),
      "final":"A R01–R12, R03 first run ending at (620,288); A V01/V02; B proposed x792/x1186/x1967 divisions locally qualified with empty alternatives",
      "evidence":"Root selected A's uneven horizontal paths, amended only the first R03 endpoint, retained A's two curved long traces, and kept the other three B proposals at black!8 with local presence/continuity doubt. Local rule darkenings await separate decisions.",
      "diff_C":True,"diff_H":False,"kind":"drawing or diagram",
      "confidence":"medium",
      "confidence_status":"root aggregate medium, with separate local low/medium qualifications",
      "diff_C_status":"root explicitly counts the full grid as one changed cluster",
      "main_counting_decision_pending":False,
      "crop":"crops/013/01_rules_top.png",
      "root_crops":[f"crops/013/{name}" for name in [
        "01_rules_top.png","02_rules_middle.png","03_rules_subdivisions.png","04_rules_lower.png",
        "05_rule_foot.png","06_vertical_first.png","07_vertical_second.png",
        "08_vertical_third.png","09_vertical_fourth.png","10_vertical_fifth.png"]],
      "pending_fields":["final page attachment","root overall approval"],
      "root_local_components":[
        {"id":"R03","location":"pale y286 rule: first run (30,286)–(620,288), right run (1134,287)–(2340,292)","confidence":"low","qualification":"intervening continuation and exact pale endpoints"},
        {"id":"R08","location":"pale y928–934 rule: A's three separate spans","confidence":"medium","qualification":"continuity"},
        {"id":"V01","location":"curved long trace near x400, A line 40","confidence":"medium","qualification":"extent; surface origin, hand and function undetermined"},
        {"id":"V02","location":"curved long trace near x1570, A line 41, continuing above headings","confidence":"medium","qualification":"extent; surface origin, hand and function undetermined"},
        {"id":"B-vertical-792","location":"proposed trace from (792,207) to (790,1667)","confidence":"low","qualification":"presence/continuity; empty alternative","alternatives":[""]},
        {"id":"B-vertical-1186","location":"proposed trace from (1186,207) to (1184,1667)","confidence":"low","qualification":"presence/continuity; empty alternative","alternatives":[""]},
        {"id":"B-vertical-1967","location":"proposed trace from (1967,207) to (1970,1667)","confidence":"low","qualification":"presence/continuity; empty alternative","alternatives":[""]},
      ]}

def root_entry(number):
    m = re.search(rf"(?m)^{number}\. .*?(?=\n\n|\Z)",ROOT_LOG)
    return m.group(0) if m else None

def root_choice(key, number, final, confidence, *, status=None, diff=True, kind=None,
                remaining=None, components=None, additional=None, **extra):
    exact=root_entry(number)
    if not exact: return
    ROOT_CHOICES[key]={
      "root_log_entry":str(number),"root_exact_excerpt":exact,"final":final,
      "confidence":confidence,"confidence_status":"root reading/shape confidence; independent local qualifications retained",
      "evidence":exact.split(": ",1)[-1],
      "diff_C":diff,"diff_H":False,"diff_C_status":"root-selected source reading or visible geometry",
      "C_doubt_status":status,"main_counting_decision_pending":False,
      "crop":None,"root_crops":[],"root_local_components":components or [],
      "root_remaining_doubt":remaining,"pending_fields":["final page attachment","root overall approval"],
      **extra}
    cp=re.search(chr(96)+r"([ABC]/[\w./-]+\.png)"+chr(96),exact)
    if cp:
        ROOT_CHOICES[key]["crop"]="readers/013/"+cp.group(1)
        ROOT_CHOICES[key]["root_crops"]=["readers/013/"+cp.group(1)]
    if kind: ROOT_CHOICES[key]["kind"]=kind
    if additional: ROOT_CHOICES[key]["root_additional_source_note"]=additional

identity_addendum = re.search(r"(?m)^The C doubt table has now.*$",ROOT_LOG)
identity_addendum = identity_addendum.group(0) if identity_addendum else None
arrow_addendum = re.search(r"(?m)^At entry15,.*$",ROOT_LOG)
arrow_addendum = arrow_addendum.group(0) if arrow_addendum else None
root_choice("pale_A",11,r"\unsure{\deleted{A}|A}; two exterior pale curves",
 "medium",status="resolved",kind="deletion state (struck given live or live given struck)",
 components=[
  {"id":"glyph","location":"pale A below dark A","reading":"A","confidence":"high","source_doubt_status":"resolved"},
  {"id":"state","location":"same pale A","reading":"deleted/overwritten | live","confidence":"medium","qualification":"new state doubt; selected A qualification"},
  {"id":"left_curve","location":"A curve x178, y555–585","confidence":"medium","qualification":"role/hand/surface origin undetermined"},
  {"id":"right_curve","location":"A curve x230, y555–585","confidence":"medium","qualification":"role/hand/surface origin undetermined"}],
 remaining={"reading":r"\unsure{\deleted{A}|A}; exterior pale curves",
   "alternatives":["live A"],"confidence":"medium",
   "reason":"Pale A glyph is resolved, high. Its deleted/live state remains open at the same lower position, medium from the selected A qualification. Left curve near x178 and right curve near x230, y555–585, each have medium shape confidence and unresolved role, hand and surface origin."},
 additional=identity_addendum)
root_choice("meditation",12,"Méditation","high",status="resolved",kind="other")
root_choice("meditation_residuals",12,"Five pale runs, A A04 with first two upper continuations amended by root",
 "medium",kind="omission",
 components=[
  {"id":"first","location":"(137,749)–(141,790)–(149,837)","confidence":"medium","qualification":"upper crop boundary; continuation beyond undetermined"},
  {"id":"second","location":"(160,749)–(164,792)–(168,823)","confidence":"medium","qualification":"upper crop boundary; continuation beyond undetermined"},
  {"id":"remaining_three","location":"A A04 paths at x208–214,243–248,287–292","confidence":"medium","qualification":"literal A coordinates retained"},
  {"id":"interpretation","location":"all five pale runs behind first title","confidence":"low","qualification":"character, state and origin unresolved; no further word/line inferred"}],
 remaining={"reading":"Five pale residual runs","alternatives":[],"confidence":"low",
   "reason":"First run (137,749)–(141,790)–(149,837) and second (160,749)–(164,792)–(168,823) meet the upper boundary; continuation beyond remains undetermined. Three other A A04 paths at x208–214,243–248,287–292 are retained. Each has medium visible-shape confidence; character/state/origin remain low. R07 supplies the horizontal rule once."})
root_choice("cascades",13,r"\deleted{\unsure{C|Ca}}Cascades; A entrance/return curve",
 "medium",status="retained",kind="insertion or placement",
 remaining={"reading":r"\deleted{\unsure{C|Ca}}","alternatives":["Ca"],"confidence":"medium",
 "reason":"At the opening of Cascades the C curve is visible, but the following crowded low loop does not settle the predecessor a. A's entrance/return curve at (497,833)–(514,839) is retained in the same cluster."})
root_choice("reveil_residuals",13,"A B01: wedge, interrupted obliques, inner turn and two lower slants; Réveil live",
 "medium",kind="omission",remaining={"reading":"A B01 local graphic","alternatives":[],"confidence":"medium",
 "reason":"Initial Réveil R vicinity: broad upper mark (500,694)–(509,703), slash (513,706)–(517,710), pale continuation (518,711)–(529,721), inner wedge near (533,728)–(541,734), and lower fragments (549,739)–(558,749). A's medium shape proposal is retained; cancellation role, hand and origin remain undetermined. Réveil stays live."})
root_choice("crossed_A",14,r"\deleted{(\unsure{i})}; A XA.H1–H5","medium",status="retained",
 kind="drawing or diagram",remaining={"reading":r"\deleted{(\unsure{i})}","alternatives":[],"confidence":"medium",
 "reason":"Crossed A subdivision, full-scan approximately (165,875)–(248,953): parentheses survive while diagonals merge with the inner upright. Five A approximation paths do not establish five original pen strokes."})
root_choice("lower_question",14,"?","high",status="resolved",kind="other")
root_choice("lower_A_arrow",14,"A L01: hooked upper entry, descending shaft and downward point","medium",
 kind="drawing or diagram",remaining={"reading":"A L01 arrow geometry","alternatives":[],"confidence":"medium",
 "reason":"Full-scan (146,909)–(181,1018): hooked upper entry, curved shaft and downward head have medium geometry confidence. Role and hand remain undetermined."})
root_choice("crossed_B",15,r"\deleted{(ii)}; A XB.H1–H4","medium",status="resolved",kind="drawing or diagram")
root_choice("lower_B_arrow",15,"C G30: two exact extended-shaft/terminal commands, beginning (526,984)","medium",
 kind="drawing or diagram",additional=arrow_addendum,
 remaining={"reading":"C G30 long pale curved arrow and darker terminal","alternatives":[],"confidence":"medium",
 "reason":"The selected first path begins at (526,984), passes through control points (526,1008)/(526,1023), reaches (533,1042) and (538,1051). The second starts (529,1047), curves via (533,1051)/(536,1050), then reaches (538,1050)–(542,1055). Geometry medium; role/hand undetermined. The initial y937 estimate is withdrawn by the root addendum."})
root_choice("crossed_C",16,r"\deleted{(\unsure{i|ii})}; B hatch-C-1–4 and terminal hook",
 "medium",status="retained",kind="drawing or diagram",
 remaining={"reading":r"\deleted{(\unsure{i|ii})}","alternatives":["ii"],"confidence":"medium",
 "reason":"Crossed C subdivision, approximately (928,879)–(1017,949): diagonals merge with the central surviving foot. B's four hatch paths and separate low terminal hook are retained; the upper-left gray patch has its own decision."})
root_choice("crossed_C_patch",16,"B G-cancel-C-gray-point","medium",kind="omission",
 remaining={"reading":"Small upper-left gray patch","alternatives":[],"confidence":"low",
 "reason":"Full-scan box (938,892)–(950,904), above-left of crossed C subdivision: visible shape medium; role, hand and origin low."})
root_choice("crossed_D",17,r"\deleted{(i)}; A XD.H1–H4","medium",status="resolved",kind="drawing or diagram")
root_choice("crossed_E20",18,r"\deleted{(\unsure{i|ii})}; A XE20.H1–H4",
 "medium",status="retained",kind="drawing or diagram",
 remaining={"reading":r"\deleted{(\unsure{i|ii})}","alternatives":["ii"],"confidence":"medium",
 "reason":"Notes20 crossed subdivision, approximately (1696,882)–(1789,949): central upright and lower loops remain crossed, so the interior count is unresolved. A's low fourth slant remains among its four hatch approximation paths."})
root_choice("crossed_E23",19,r"\deleted{(\unsure{iii|iv})}; B hatch-E23-1–4 and terminal hook",
 "low",status="retained",kind="misread symbol or index",
 remaining={"reading":r"\deleted{(\unsure{iii|iv})}","alternatives":["iv"],"confidence":"low",
 "reason":"Notes23 crossed subdivision, approximately (2107,885)–(2225,947): upright/loop remnants and separate right interior dot weakly favor iii. Crossings leave iv viable. The primary reversal is qualified; B's four hatch paths and extra rightward/downward terminal remain."})
root_choice("pale_sub_A",20,r"\unsure{\deleted{(i)}|(i)} below dark (i)",
 "medium",status="retained",diff=False,kind="deletion state (struck given live or live given struck)",
 additional=identity_addendum,local_C_glyph_doubt_status="resolved",source_C_row_status="retained",
 count_parent_key="pale_sub_C",count_locus_key="scan013-C-source-row13",
 diff_C_status="local glyph/state change is counted once with compound source row13 at pale_sub_C",
 remaining={"reading":r"\unsure{\deleted{(i)}|(i)}","alternatives":["live (i)"],"confidence":"medium",
 "reason":"First-column pale lower group, approximately (151,1042)–(221,1137): parentheses, central short upright and lower foot resolve the glyph (i), medium. Cancellation/live state remains open using A's deletion-first qualification and below-position. This is local13a within compound C source row13."})
root_choice("pale_sub_C",21,r"\unsure{\deleted{\unsure{(i)|(}}|\unsure{(i)|(}}",
 "low",status="retained",kind="misread symbol or index",additional=identity_addendum,
 source_C_row_status="retained",count_locus_key="scan013-C-source-row13",
 diff_C_status="single root C count for compound source row13, with pale_sub_A as noncounting local sibling",
 components=[
  {"id":"opening","location":"pale opening before third live (i), around x940–953,y1055–1086","confidence":"medium"},
  {"id":"full_extent","location":"raised gray dot, partial central upright and gray right curve, x961–993,y1047–1088","confidence":"low","qualification":"full (i) versus opening-only"},
  {"id":"state","location":"same full/partial pale form","confidence":"low","qualification":"cancelled/overwritten versus live"}],
 remaining={"reading":r"\unsure{\deleted{\unsure{(i)|(}}|\unsure{(i)|(}}","alternatives":["opening parenthesis only","live state"],"confidence":"low",
 "reason":"Third live subdivision: opening at x940–953,y1055–1086 has medium confidence. Raised dot/short stroke and right curve at x961–993,y1047–1088 support fuller (i), but its full extent and cancelled/live state remain low. B's dot and right-curve commands are component evidence of A's full form and must not be drawn twice. This is local13b within compound C source row13."})
root_choice("pale_D",22,r"\unsure{\deleted{(i)}|(i)} above dark (i)",
 "medium",status="resolved",kind="deletion state (struck given live or live given struck)",
 additional=identity_addendum,
 components=[
  {"id":"glyph","location":"upper displaced D subdivision","reading":"(i)","confidence":"high","source_doubt_status":"resolved"},
  {"id":"state","location":"same upper pale group","reading":"cancelled/overwritten | live","confidence":"medium"}],
 remaining={"reading":r"\unsure{\deleted{(i)}|(i)}","alternatives":["live (i)"],"confidence":"medium",
 "reason":"Upper displaced D group, approximately (1304,1026)–(1394,1107), has its own dot, short upright and both parentheses: glyph confidence high. Cancelled/live state remains medium because no independent crossing stroke is settled. Source C row11 glyph doubt is resolved; the new state doubt remains."})
root_choice("plus",23,"plus","high",status="resolved",kind="other")
root_choice("long_dash",23,"A G01: filled detached dash below long","high",kind="omission",
 remaining={"reading":"Detached dark dash","alternatives":[],"confidence":"medium",
 "reason":"Full-scan (587,1235)–(599,1245), below the tail of long: A's small filled shape has high visible-shape confidence. Role, hand and origin remain undetermined, with local uncertainty medium."})
root_choice("top_cancellation",24,r"\deleted{A (1976/77)}; A T01.H01–H14 with curved lower turns",
 "medium",kind="drawing or diagram",
 components=[
  {"id":"words_state","location":"early first-column A/date","reading":r"\deleted{A (1976/77)}","confidence":"high"},
  {"id":"hatch_geometry","location":"A T01.H01–H14","confidence":"medium","qualification":"fourteen approximation commands, no count of independent pen strokes"}])
root_choice("margin",25,"A M01–M03 paths; B upper-question node",
 "medium",kind="drawing or diagram",
 components=[
  {"id":"dark_geometry","location":"bar/shaft/brace/loop/opposed-arrow group x24–145,y391–861","confidence":"high"},
  {"id":"pale_retracing","location":"thin head arm, long parallel trace, pale brace and small down-arrow beside main head","confidence":"medium","qualification":"exact pale retracing"},
  {"id":"question","location":"B upper-question at (86,616)","reading":"?","confidence":"high","qualification":"B baseline/position; A question node not duplicated"}],
 remaining={"reading":"Margin cluster pale retracing","alternatives":[],"confidence":"medium",
 "reason":"Within x24–145,y391–861, main dark bar, arrow, brace, inner loop and opposed-arrow geometry are high confidence. The thin left arm under the bar, long pale parallel trace, pale brace return and tiny downward head beside the main downward head have medium exact-geometry confidence. A M01–M03 paths are integrated with B's question node at (86,616)."})
root_choice("margin_point",25,"A M04: isolated gray oval above bar","medium",kind="omission",
 remaining={"reading":"Gray oval-like point","alternatives":[],"confidence":"medium",
 "reason":"Near (47,404), above the upper-left bar: medium visible-shape confidence; role, hand and origin undetermined."})
root_choice("bent_arrows",26,"A A02: three paths for two bent arrows and repeated lower rule","medium",
 kind="drawing or diagram",
 components=[
  {"id":"bends_heads","location":"first-column date/title interval x239–346,y632–750","confidence":"high"},
  {"id":"curvature","location":"A A02 three draw commands","confidence":"medium","qualification":"detailed curvature"}],
 remaining={"reading":"Bent-arrow detailed curvature","alternatives":[],"confidence":"medium",
 "reason":"Two bends and main arrowheads in x239–346,y632–750 are high confidence; detailed curvature remains medium. A's third draw path preserves the lower repeated horizontal run converging at the bend."})
root_choice("bent_residuals",26,"A A03: upper arch, oblique dash and lower point","medium",kind="omission",
 components=[
  {"id":"arch","location":"(257,665) to (278,661), with controls (265,662)/(273,657)","confidence":"medium"},
  {"id":"slash","location":"(307,652)–(311,654)","confidence":"medium"},
  {"id":"point","location":"ellipse at (304,673)","confidence":"medium"}],
 remaining={"reading":"Arch, slash and point beside upper bent arrow","alternatives":[],"confidence":"medium",
 "reason":"Arch above the upper shaft's left start, (257,665)–(278,661); slash left of upper head, (307,652)–(311,654); point below shaft at (304,673). Each shape medium; role, hand and origin undetermined."})
root_choice("date_hook",27,"B G-date-hook two components plus root foot thickening (404,639)–(417,640)",
 "medium",kind="omission",
 components=[
  {"id":"hook","location":"full box (401,616)–(418,641)","confidence":"medium"},
  {"id":"root_foot_thickening","location":"(404,639)–(417,640) on existing pale rule","confidence":"medium",
   "root_path":r"\draw[black!70,line width=.50pt] (404,639)--(417,640);"}],
 remaining={"reading":"Date hook and connected foot thickening","alternatives":[],"confidence":"medium",
 "reason":"First/second date boundary, full box (401,616)–(418,641): B's two hook components are medium confidence with character/role/hand/origin undetermined. Root's medium approximation (404,639)–(417,640) records the local dark foot on the existing rule. One connected cluster."})
for key,label,conf,loc in [
 ("Baumeister_upper_gray","B G-Baumeister-upper-gray","medium","(1789,697)–(1799,709)"),
 ("Baumeister_upper_dark","B G-Baumeister-upper-black and pale tip","high","(1850,695)–(1864,709)"),
 ("Baumeister_left","B G-Baumeister-left-gray","medium","(1689,730)–(1698,740)"),
 ("Baumeister_right","B G-Baumeister-right-gray","low","(1897,736)–(1909,749)")]:
    root_choice(key,28,label,conf,kind="omission",
      remaining={"reading":label,"alternatives":[],"confidence":conf,
        "reason":f"Full-scan {loc}: {conf} shape confidence; character, role, hand and origin undetermined. Exact B path and fixed local origin retained."})
for key,label,loc in [
 ("Jeu_overmark","B G-Jeu-overmark","(1612,1255)–(1624,1267), above J"),
 ("Spiel_spot","B G-Spiel-lower-spot","(1695,1223)–(1707,1236), below Spiel")]:
    root_choice(key,29,label,"medium",kind="omission",
      remaining={"reading":label,"alternatives":[],"confidence":"low",
       "reason":f"Full-scan {loc}: shape medium; function, hand and origin low. The literal words and hyphens remain as agreed."})
root_choice("lower_A_trace",30,"B G-A-blank-trace: five separated components","medium",kind="omission",
 remaining={"reading":"Dark upper trace, point and three pale fragments","alternatives":[],"confidence":"low",
 "reason":"Full-scan (224,1404)–(241,1443): five B components form one interrupted descending cluster. Visible shape medium; function, hand and origin low."})
root_choice("foot_A_trace",31,"B G-A-foot-trace: seven spot components","medium",kind="omission",
 remaining={"reading":"Seven-spot descending slant","alternatives":[],"confidence":"medium",
 "reason":"Full-scan (329,1578)–(346,1615), beneath the first foot cell: seven separated B spot components have medium shape confidence. No character or surface origin is assigned."})
root_choice("lower_E23_dash",32,"A G05: (2252,1343)–(2268,1344)","high",kind="omission",
 remaining={"reading":"Slightly sloping detached dash","alternatives":[],"confidence":"medium",
 "reason":"Below last lower title, exact path (2252,1343)–(2268,1344): high shape confidence; role, hand and origin medium uncertainty."})
root_choice("rule_thickening_1303",32,"A G06: filled wedge near (2227,1303)","high",
 diff=False,kind="drawing or diagram",count_parent_key="grid",count_locus_key="scan013-grid",
 diff_C_status="local grid component; one grid count occurs at grid decision",
 remaining_qualification="High visible-shape confidence; role and hand undetermined. Included in grouped grid doubt.",
 components=[{"id":"wedge","location":"(2221,1304) via controls (2226,1300)/(2231,1302) to (2235,1305)",
              "confidence":"high","qualification":"role and hand undetermined; replaces B thick straight segment"}])
root_choice("Fringale_spot",33,"B G-E20-blot: irregular polygon at fixed origin","medium",kind="omission",
 remaining={"reading":"Irregular gray patch","alternatives":[],"confidence":"low",
 "reason":"Full-scan (1926,1353)–(1941,1372), below Fringale: B's filled polygon preserves the compact irregular shape, medium. Function, hand and origin low."})
root_choice("SchI_point",34,"B G-D-point: isolated compact point","medium",kind="omission",
 remaining={"reading":"Tiny dark isolated point","alternatives":[],"confidence":"low",
 "reason":"Full-scan (1490,1517)–(1500,1528), above the rule right of Sch I: medium shape confidence amid enhanced texture; function, hand and origin low. No punctuation reading."})
root_choice("A_lower_slant",35,"B G-A-edge-slant: six local components","medium",kind="omission",
 remaining={"reading":"Pale/dark oblique fragments and upper-right point","alternatives":[],"confidence":"low",
 "reason":"Full-scan (368,1013)–(392,1044), near the first-column boundary: B's six components preserve the separated cluster. Visible shape medium; character, role, hand and origin low."})
root_choice("Decouverte_point",36,"C G29: ellipse at local (1,2), fixed full origin (240,751)","medium",kind="omission",
 remaining={"reading":"Small pale point below Découverte","alternatives":[],"confidence":"low",
 "reason":"Fixed full-scan origin (240,751), local ellipse at (1,2), radii 1.3/1.8 original-coordinate units. Medium shape confidence; role, hand and origin low. No accent or title correction."})
root_choice("right_edge",37,"A E01–E10 literal paths, including local returns, interruptions and bent terminals",
 "medium",kind="drawing or diagram",
 components=[
  {"id":f"E{i:02d}","location":loc,"confidence":"medium","qualification":"exact geometry; function beyond edge undetermined"}
  for i,loc in enumerate([
   "(2333,113)–(2351,132)","(2329,197)–(2351,212)","(2327,362)–(2351,379)",
   "(2326,414)–(2351,432)","(2322,548)–(2347,568)","(2328,635)–(2350,654)",
   "(2332,962)–(2351,981)","(2327,1078)–(2345,1096)","(2331,1195)–(2347,1211)",
   "(2327,1560)–(2340,1579)"],1)],
 remaining={"reading":"Ten surviving edge groups E01–E10","alternatives":[],"confidence":"medium",
 "reason":"Each exact-geometry confidence is medium: E01 (2333,113)–(2351,132); E02 (2329,197)–(2351,212); E03 (2327,362)–(2351,379); E04 (2326,414)–(2351,432); E05 (2322,548)–(2347,568); E06 (2328,635)–(2350,654); E07 (2332,962)–(2351,981); E08 (2327,1078)–(2345,1096); E09 (2331,1195)–(2347,1211); E10 (2327,1560)–(2340,1579). A paths preserve convergences, curved returns, interrupted E07, downturned E05 and terminal-bent E10. Function beyond the edge remains undetermined; no manuscript word is supplied."},
 additional="\n\n".join(root_entry(n) for n in (38,39,40) if root_entry(n)))
root_choice("rule_thickening_1091",39,"A G07: local filled wedge at live-subdivision rule","medium",
 diff=False,kind="drawing or diagram",count_parent_key="grid",count_locus_key="scan013-grid",
 diff_C_status="local grid component; one grid count occurs at grid decision",
 remaining_qualification="Medium geometry; role/hand undetermined. Included in grouped grid doubt.",
 components=[{"id":"wedge","location":"A G07 from (2308,1090) to (2321,1092), including lower closure",
              "confidence":"medium","qualification":"leftmost part clipped in A23; full relation seen in root crop03; no extra edge group"}],
 root_joint_crop="crops/013/03_rules_subdivisions.png")

# Public evidence follows the latest root wording; superseded wording remains
# available only through its exact log reference and the source-identity addendum.
for key,ch in ROOT_CHOICES.items():
    if ch.get("root_remaining_doubt"):
        ch["evidence"]=ch["root_remaining_doubt"]["reason"]
ROOT_EVIDENCE={
 "pale_A":"Two lower sloping legs, crossbar and feet resolve pale A, high; cancellation/live state remains open. A's two exterior curves have medium shape confidence and undetermined role, hand and origin. The source-identity addendum resolves original C glyph doubt1 while retaining the new state doubt.",
 "meditation":"Terminal n has its exit stroke; no separate supported s. Original C doubt2 resolved, high.",
 "crossed_B":"Two separate lower upright/foot remnants and their upper marks resolve crossed ii, medium, independently of the live lower numeral. A XB.H1–H4 preserve the selected hatch geometry.",
 "crossed_D":"One distinct dot and short upright/foot resolve crossed i between its parentheses, medium. A XD.H1–H4 include the low fourth slant.",
 "lower_question":"Bent hook/stem and distinct detached dot resolve the lower question mark, high.",
 "pale_D":"Own dot, short upright and both parentheses resolve the upper displaced (i), high. The cancelled/live state remains medium because no independent cancelling stroke is settled. Source C glyph doubt11 is resolved under the addendum.",
 "plus":"Visible p descender, tall l, connected u and ending s resolve plus, high.",
 "top_cancellation":"Cancelled A (1976/77) is clear, high for text/cancellation. A's fourteen T01.H01–H14 commands preserve merged hatching and curved lower turns, medium geometry; they do not assert fourteen original pen strokes."
}
for key,value in ROOT_EVIDENCE.items():
    if key in ROOT_CHOICES: ROOT_CHOICES[key]["evidence"]=value
if "grid" in ROOT_CHOICES:
    gr=ROOT_CHOICES["grid"]
    for key in ("rule_thickening_1303","rule_thickening_1091"):
        if key in ROOT_CHOICES: gr["root_local_components"].extend(ROOT_CHOICES[key]["root_local_components"])
    gr["root_remaining_doubt"]={
      "reading":"Qualified pale grid components and two local rule wedges",
      "alternatives":[],"confidence":"medium",
      "reason":"; ".join(c["id"]+" at "+c["location"]+": "+c["confidence"]+" — "+c.get("qualification","")
                         for c in gr["root_local_components"])}
    gr["evidence"]="Root selected A's uneven horizontal paths with the first R03 endpoint amended to (620,288), A's two curved long traces, and three locally qualified B proposals at black!8. A G06 and G07 supply the two local filled wedges, which belong to this one grid count. Individual presence, continuity, extent, role and hand qualifications remain in the local components."
if "reveil_residuals" in ROOT_CHOICES:
    ROOT_CHOICES["reveil_residuals"]["root_remaining_doubt"]["reading"]="Interrupted oblique marks around Réveil R: upper wedge, slash, pale continuation, inner turn and two lower slants"
if "lower_A_arrow" in ROOT_CHOICES:
    ROOT_CHOICES["lower_A_arrow"]["root_remaining_doubt"]["reading"]="Pale downward arrow with hooked upper entry, descending shaft and open head"
if "lower_B_arrow" in ROOT_CHOICES:
    ROOT_CHOICES["lower_B_arrow"]["root_remaining_doubt"]["reading"]="Long pale descending arrow with curved darker terminal, beginning at (526,984)"
if "Jeu_overmark" in ROOT_CHOICES:
    ROOT_CHOICES["Jeu_overmark"]["root_remaining_doubt"]["reading"]="Small triangular overmark above J of Jeu"
if "Spiel_spot" in ROOT_CHOICES:
    ROOT_CHOICES["Spiel_spot"]["root_remaining_doubt"]["reading"]="Small pale oval below Spiel"
for key,reading in [
 ("Baumeister_upper_gray","Small gray point above Baumeister"),
 ("Baumeister_upper_dark","Dark point and short pale continuation above final part of Baumeister"),
 ("Baumeister_left","Small gray point between Der and the B of Baumeister"),
 ("Baumeister_right","Faint short upright after Baumeister")]:
    if key in ROOT_CHOICES: ROOT_CHOICES[key]["root_remaining_doubt"]["reading"]=reading
if "Baumeister_upper_dark" in ROOT_CHOICES:
    ROOT_CHOICES["Baumeister_upper_dark"]["root_remaining_doubt"].update({
      "confidence":"medium",
      "reason":"Above the final part of Baumeister, full-scan box (1850,695)–(1864,709): the dark compact point has high shape confidence. Its pale continuation, local (10,4)–(12,3) at fixed origin (1850,695), has medium shape confidence. Character, role, hand and origin remain undetermined."})
    ROOT_CHOICES["Baumeister_upper_dark"]["root_local_components"]=[
      {"id":"dark_point","location":"full box (1850,695)–(1864,709)","confidence":"high"},
      {"id":"pale_tip","location":"local (10,4)–(12,3) at full origin (1850,695)","confidence":"medium"},
      {"id":"interpretation","location":"same point-and-tip cluster","qualification":"character/role/hand/origin undetermined"}]
    ROOT_CHOICES["Baumeister_upper_dark"]["evidence"]=ROOT_CHOICES["Baumeister_upper_dark"]["root_remaining_doubt"]["reason"]

def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()

MANIFEST = {}
def file_ref(path):
    if path not in MANIFEST:
        MANIFEST[path] = {"path": path, "sha256": sha(path)}
    return dict(MANIFEST[path])

def ref(role, section, index, row=None):
    p = f"out/readers/013/{role}/report.json"
    d = {**file_ref(p), "pointer": f"/{section}/{index}"}
    row = REPORTS[role][section][index] if row is None else row
    if isinstance(row, dict):
        ident = row.get("id", row.get("element"))
        if ident is not None:
            d["row_id"] = ident
    return d

def text_ref(path, first, last=None, anchor=None, excerpt=False):
    last = first if last is None else last
    source_lines=(ROOT/path).read_text().splitlines()
    assert 1<=first<=last<=len(source_lines),(path,first,last,"invalid source range")
    d = {**file_ref(path), "line_start": first, "line_end": last}
    if anchor:
        d["anchor"] = anchor
    if excerpt:
        d["exact_excerpt"] = "\n".join(source_lines[first-1:last])
    return d

def tex_refs(role, ranges):
    return [text_ref(f"out/readers/013/{role}/reading.tex", *rr) for rr in ranges]

def box(row):
    b = row.get("bbox")
    if isinstance(b, dict):
        b = b.get("xyxy")
    return b if isinstance(b, list) and len(b) == 4 else None

def union_box(boxes):
    bs = [b for b in boxes if b is not None]
    return [min(b[0] for b in bs), min(b[1] for b in bs),
            max(b[2] for b in bs), max(b[3] for b in bs)] if bs else None

for role in "ABC":
    for name in ("report.json", "reading.tex", "reading.md"):
        path = f"out/readers/013/{role}/{name}"
        actual = file_ref(path)["sha256"]
        assert actual == EXPECTED[role][name], (role, name, "reader fingerprint changed")
assert (ROOT / "packets/013/H.tex").read_bytes() == b""
for name in ("C.tex", "H.tex", "metadata.json", "C_doubts.txt", "C_notes.txt", "C_inventory.json"):
    file_ref(f"packets/013/{name}")
for path in (ROOT_LOG_PATH, "out/PREAMBLE.tex", "out/briefs/brief_v11_scan013.md",
             "out/briefs/record_clerk_v2_scan013.md", "out/briefs/scan013_shared_reminder.md"):
    file_ref(path)

GROUPS = []
def group(key, location, A="", B="", C="", c_row=None, inventory=(), tex=None, C_lines=()):
    GROUPS.append({"key": key, "location": location,
                   "rows": {r: s.split() for r, s in zip("ABC", (A, B, C))},
                   "C_row": c_row, "inventory": list(inventory), "tex": tex or {},
                   "C_lines": C_lines})

group("pale_A", "First column: pale A below dark A, its state and exterior curves",
      "A-D01", "B-C01", "C013.d01", 1, (11,50),
      {"A":[(85,87)], "B":[(102,107)], "C":[(55,55)]}, [(10,10)])
group("meditation", "First main title: final word", "A-D02", "B-C02", "C013.d02",
      2, (19,), {"A":[(112,112)],"B":[(191,191)],"C":[(120,120)]}, [(16,16)])
group("cascades", "Second main title: C/Ca predecessor, overlap and local hook",
      "A-D03 A-G18", "B-C03", "C013.d03", 3, (20,25),
      {"A":[(115,117)],"B":[(202,204)],"C":[(126,126)]}, [(17,17)])
for col, a, b, c, crow, ino, ar, br, cr, cl in [
    ("A","A-D04 A-G19","B-C04","C013.d04",4,26,(132,142),(240,248),(142,142),19),
    ("B","A-D05","B-C05","C013.d05",5,27,(144,152),(250,258),(144,144),19),
    ("C","A-D06 A-G20","B-C06","C013.d06",6,28,(154,160),(260,268),(146,146),20),
    ("D","A-D07","B-C07","C013.d07",7,29,(162,170),(270,276),(148,148),20),
    ("E20","A-D08 A-G21","B-C08","C013.d08",8,30,(172,180),(278,284),(150,150),21),
    ("E23","A-D09 A-G22","B-C09","C013.d09",9,31,(182,190),(286,294),(152,152),21),
]:
    tr = {"A":[ar], "B":[br], "C":[cr]}
    if col == "C": tr["B"].append((296,296))
    if col == "E23": tr["B"].append((298,298))
    group("crossed_"+col, f"Crossed subdivision in column {col}: glyph and cancellation paths",
          a,b,c,crow,(ino,),tr,[(cl,cl)])
group("lower_question", "First column: lower pale question mark", "A-D10","B-C10","C013.d10",
      10,(32,),{"A":[(191,191)],"B":[(305,305)],"C":[(154,154)]},[(22,22)])
group("pale_D", "Fourth live subdivision: pale upper (i), state and placement",
      "A-D11","B-C11","C013.d11",11,(36,),
      {"A":[(198,198)],"B":[(331,331)],"C":[(171,171)]},[(23,23)])
group("plus", "Second lower title: plus", "A-D12","B-C12","C013.d12",
      12,(38,),{"A":[(206,206)],"B":[(341,341)],"C":[(181,181)]},[(24,24)])
group("pale_sub_A", "First live subdivision: pale lower (i), glyph and state",
      "A-D13a","B-C13a","C013.d13a C013.d15",13,(34,),
      {"A":[(196,196)],"B":[(311,311)],"C":[(161,161)]},[(23,23)])
group("pale_sub_C", "Third live subdivision: pale opening/full form, raised mark, right curve and state",
      "A-D13b","B-C13b","C013.d13b",13,(35,),
      {"A":[(197,197)],"B":[(317,327)],"C":[(167,167)]},[(23,23)])
group("grid","Ruled table: horizontal runs, vertical traces, gaps and placement",
      "A-G01","B-G01","",None,(1,),
      {"A":[(27,41)],"B":[(10,42)],"C":[(10,22)]},[(6,8),(10,10),(18,18),(23,23),(26,26)])
group("top_cancellation","First column: cancelled early A (1976/77), explicit hatching",
      "A-G02","B-G02","",None,(9,),
      {"A":[(55,83)],"B":[(70,100)],"C":[(53,53)]},[(9,9)])
group("margin","Upper-left margin: bar, up arrow, brace, question, opposed arrows and local returns",
      "A-G03","B-G03","C013.g15",None,(10,),
      {"A":[(8,20)],"B":[(134,154)],"C":[(81,94)]},[(2,2)])
group("margin_point","Detached gray mark above upper-left bar",
      "A-G04","B-G07","C013.g15",None,(52,),
      {"A":[(22,22)],"B":[(156,159)],"C":[(96,98)]})
group("bent_arrows","First date/title interval: two bent arrows and repeated lower rule",
      "A-G05","B-G04","C013.g16",None,(18,),
      {"A":[(101,103)],"B":[(161,161),(178,180)],"C":[(100,102)]},[(12,13)])
group("bent_residuals","Beside upper bent arrow: pale arch, detached slash, lower dot",
      "A-G06","B-G04","C013.g16",None,(53,54,55),
      {"A":[(105,107)],"B":[(163,176)],"C":[(104,114)]})
group("meditation_residuals","Behind first main title: pale residual runs",
      "A-G07","","C013.g02",None,(51,),
      {"A":[(111,111)],"C":[(25,27)]})
group("reveil_residuals","Initial R of Réveil: interrupted oblique marks and pale local components",
      "A-G08","B-G09","",None,(56,),
      {"A":[(119,123)],"B":[(195,198)]})
group("long_dash","Below long: detached dark mark","A-G09","B-G15","C013.g12",
      None,(57,),{"A":[(215,215)],"B":[(357,360)],"C":[(220,222)]})
group("lower_A_trace","Blank first column above foot: interrupted trace","A-G10","B-G18","C013.g23",
      None,(58,),{"A":[(217,219)],"B":[(372,375)],"C":[(224,228)]})
group("foot_A_trace","Below first foot: interrupted descending trace","A-G11","B-G19","C013.g24",
      None,(59,),{"A":[(221,224)],"B":[(377,380)],"C":[(230,234)]})
group("Fringale_spot","Below Fringale: small irregular gray spot","A-G12","B-G21","C013.g27",
      None,(60,),{"A":[(226,226)],"B":[(387,390)],"C":[(250,253)]})
group("lower_E23_dash","Last column below lower title: detached horizontal dash","A-G13","B-G20","C013.gHalfB",
      None,(61,),{"A":[(227,227)],"B":[(382,385)],"C":[(272,274)]})
group("rule_thickening_1303","Last column: local darkening on translation-level rule","A-G14","B-G01","",
      None,(1,),{"A":[(228,228)],"B":[(44,44)],"C":[(20,20)]})
group("rule_thickening_1091","Near right edge: local darkening on live-subdivision rule","A-G15","","",
      None,(1,),{"A":[(229,229)],"B":[(36,36)],"C":[(18,18)]})
group("right_edge","Ten surviving right-edge components, individually mapped",
      "A-G16","","C013.edge5 C013.edge10",None,(2,),
      {"A":[(237,255)],"B":[(414,432)],"C":[(209,218)]},[(33,42)])
group("lower_A_arrow","First column: curved-top downward arrow","A-G17","B-G05","C013.g10",
      None,(32,),{"A":[(193,193)],"B":[(307,307)],"C":[(156,156)]},[(22,22)])
group("lower_B_arrow","Before second live subdivision: pale curved descending arrow","A-G17","B-G06","C013.g30",
      None,(33,),{"A":[(195,195)],"B":[(309,309)],"C":[(158,159)]},[(22,22)])
group("date_hook","First/second column date boundary: short curved hook","","B-G08","C013.g26",
      None,(62,),{"B":[(182,185)],"C":[(245,248)]})
group("Baumeister_upper_gray","Above Baumeister: upper gray point","","B-G10","C013.g28a",
      None,(63,),{"B":[(220,223)],"C":[(255,257)]})
group("Baumeister_upper_dark","Above Baumeister: dark point and pale tip","","B-G11","C013.g28b",
      None,(64,),{"B":[(225,228)],"C":[(259,262)]})
group("Baumeister_left","Just left of Baumeister B: small gray point","","B-G12","C013.g28c",
      None,(65,),{"B":[(230,233)],"C":[(264,266)]})
group("Baumeister_right","After Baumeister: faint short upright","","B-G13","",
      None,(66,),{"B":[(235,238)]})
group("crossed_C_patch","Above-left of crossed C subdivision: separate gray patch","","B-G14","",
      None,(67,),{"B":[(300,303)]})
group("Jeu_overmark","Above J of Jeu: small triangular mark","","B-G16","",
      None,(68,),{"B":[(362,365)]})
group("Spiel_spot","Below Spiel: gray spot","","B-G17","",
      None,(69,),{"B":[(367,370)]})
group("SchI_point","To right of Sch I: isolated point","","B-G22","",
      None,(70,),{"B":[(392,395)]})
group("A_lower_slant","First column near right boundary: pale oblique cluster","","B-G23","C013.g25",
      None,(71,),{"B":[(397,400)],"C":[(236,243)]})
group("Decouverte_point","Immediately below Découverte: small pale point","","","C013.g29",
      None,(72,),{"C":[(268,270)]})

KEY_TO_GROUP = {g["key"]: g for g in GROUPS}
for i,g in enumerate(GROUPS,1):
    g["id"] = f"013-D{i:02d}"
DIFF_MAP = {r: defaultdict(list) for r in "ABC"}
for g in GROUPS:
    for r,ids in g["rows"].items():
        for row_id in ids: DIFF_MAP[r][row_id].append(g["key"])
DIFF_INDEX = {r:{d["id"]:i for i,d in enumerate(REPORTS[r]["differences"])} for r in "ABC"}
for r in "ABC":
    assert set(DIFF_MAP[r]) == set(DIFF_INDEX[r]), (r,"unmapped or invented difference")

DOUBT_MAP = {
 "A": [
  "pale_A","cascades","crossed_A","crossed_C","crossed_E20","crossed_E23",
  "pale_D","pale_sub_A","pale_sub_C","grid","margin_point","bent_residuals",
  "meditation_residuals","reveil_residuals","long_dash","lower_A_trace","foot_A_trace",
  "Fringale_spot","lower_E23_dash","rule_thickening_1303","rule_thickening_1091","right_edge"],
 "B": [
  "cascades","crossed_A","crossed_B","crossed_C","crossed_D","crossed_E20","crossed_E23",
  "pale_sub_A","pale_sub_C","pale_A","margin_point","bent_residuals","bent_residuals",
  "bent_residuals","date_hook","reveil_residuals","Baumeister_upper_gray","Baumeister_upper_dark",
  "Baumeister_left","Baumeister_right","crossed_C_patch","pale_sub_C","pale_sub_C","long_dash",
  "Jeu_overmark","Spiel_spot","lower_A_trace","foot_A_trace","lower_E23_dash","Fringale_spot",
  "SchI_point","A_lower_slant"],
 "C": [
  "pale_A","cascades","crossed_A","crossed_C","crossed_E20","crossed_E23","pale_D",
  "pale_sub_A","pale_sub_A","pale_sub_C","margin margin_point","bent_arrows bent_residuals",
  "meditation_residuals","long_dash","lower_A_trace","foot_A_trace","A_lower_slant",
  "date_hook","Fringale_spot","Decouverte_point","Baumeister_upper_gray","Baumeister_upper_dark",
  "Baumeister_left","lower_E23_dash"]
}
for r in "ABC": assert len(DOUBT_MAP[r]) == len(REPORTS[r]["doubts"])

# A convenient source-inventory backbone, with separate local component entries
# where a reader subdivided a source item. Every source inventory row is linked.
EXTRAS = [
 ("archive","text","lower-right, sideways","Archive numeral 12; TeX comment only"),
 ("old_A_curves","drawing","around pale A below dark A","Left and right exterior pale curves"),
 ("meditation_residuals","drawing","behind first main title","Pale residual runs"),
 ("margin_point","drawing","above upper-left bar","Detached gray point"),
 ("bent_arch","drawing","above left of upper bent arrow","Pale arch"),
 ("bent_slash","drawing","left of upper arrowhead","Detached short slash"),
 ("bent_dot","drawing","below upper bent-arrow shaft","Small detached dot"),
 ("reveil_residuals","drawing","around initial R of Réveil","Interrupted oblique and pale components"),
 ("long_dash","drawing","below long","Detached dark mark"),
 ("lower_A_trace","drawing","above first foot","Interrupted descending trace"),
 ("foot_A_trace","drawing","below first foot","Interrupted slanted trace"),
 ("Fringale_spot","drawing","below Fringale","Small irregular gray spot"),
 ("lower_E23_dash","drawing","last column below lower title","Detached horizontal dash"),
 ("date_hook","drawing","first/second date boundary","Curved upright with pale continuation"),
 ("Baumeister_upper_gray","drawing","above Baumeister","Upper gray point"),
 ("Baumeister_upper_dark","drawing","above final part of Baumeister","Dark point and pale tip"),
 ("Baumeister_left","drawing","left of Baumeister B","Small gray point"),
 ("Baumeister_right","drawing","right of Baumeister","Faint short upright"),
 ("crossed_C_patch","drawing","above-left of crossed C subdivision","Gray patch"),
 ("Jeu_overmark","drawing","above J of Jeu","Small triangular overmark"),
 ("Spiel_spot","drawing","below Spiel","Gray spot"),
 ("SchI_point","drawing","right of Sch I","Isolated point"),
 ("A_lower_slant","drawing","first column, near right boundary below crossed row","Pale oblique cluster"),
 ("Decouverte_point","drawing","immediately below Découverte","Small pale point"),
]
assert len(EXTRAS) == 24
INV_MAP = {"witness_C": [[i] for i in range(1,49)],
           "A": [[i] for i in range(1,49)] + [[49],[1],[1],[50],[51],[52],[10],[53,54,55],[56],[57],[58],[59],[60],[61],[1],[1]],
           "C": [[i] for i in range(1,49)] + [[49],[51],[52],[53],[54],[55],[57],[58],[59],[71],[62],[60],[63],[64],[65],[72],[61]],
           "B": [[1],[3],[4],[5],[6],[7],[8],[9],[50],[12],[13],[14],[15],[16],[17],[11],[10],
                 [52],[53],[54],[55],[18],[62],[19],[56],[20],[25],[21],[22],[23],[24],
                 [63],[64],[65],[66],[26],[27],[28],[29],[30],[31],[28],[31],[67],[32],
                 [33],[35],[35],[37],[38],[39],[40],[41],[42],[34],[35],[36],
                 [37],[38],[39],[40],[41],[42],[57],[68],[69],[58],[59],[61],[60],[70],[71],
                 [43],[44],[45],[46],[47],[48],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[49]]}
for r in "ABC": assert len(INV_MAP[r]) == len(REPORTS[r]["inventory"]), (r,"inventory length")

INV_SCOPE = {}
for r in ("witness_C","A","C"):
    for i in range(48): INV_SCOPE[(r,i)] = "complete source inventory item; local components listed separately"
INV_SCOPE.update({
 ("A",49):"horizontal rules R01–R12 only", ("A",50):"vertical traces V01–V02 only",
 ("A",54):"pale parallel, inner-loop and intervening arrow components within margin cluster",
 ("A",55):"arch / slash / dot, assigned respectively to I53 / I54 / I55",
 ("A",62):"grid component rule_thickening_1303", ("A",63):"grid component rule_thickening_1091",
 ("B",0):"rule network and rule_thickening_1303 only; text has its own entries",
 ("B",41):"crossed_C terminal-hook component", ("B",42):"crossed_E23 terminal-hook component",
 ("B",46):"pale_sub_C raised gray stroke component", ("B",47):"pale_sub_C right curve component",
})
for i in range(48,54): INV_SCOPE[("B",i)] = "live subdivision label only"
for i in range(57,63): INV_SCOPE[("B",i)] = "lower title and any translation only"
for i in range(78,88): INV_SCOPE[("B",i)] = f"right-edge component {i-77:02d} only"

# Source and reader text anchors for the 48 original inventory elements.
BASE_TEX = {
 1:{"A":[(27,41),(228,229)],"B":[(10,44)],"C":[(10,22)]},
 2:{"A":[(237,255)],"B":[(414,432)],"C":[(209,218)]},
 9:{"A":[(55,83)],"B":[(70,100)],"C":[(53,53)]},
 10:{"A":[(8,20)],"B":[(134,154)],"C":[(81,94)]},
 11:{"A":[(85,85)],"B":[(102,102)],"C":[(55,55)]},
 18:{"A":[(101,103)],"B":[(161,161),(178,180)],"C":[(100,102)]},
 19:{"A":[(108,109),(112,112)],"B":[(187,191)],"C":[(116,120)]},
 20:{"A":[(113,116)],"B":[(193,193),(200,204)],"C":[(122,126)]},
 21:{"A":[(124,125)],"B":[(206,208)],"C":[(128,130)]},
 22:{"A":[(126,127)],"B":[(210,212)],"C":[(132,134)]},
 23:{"A":[(128,129)],"B":[(214,216)],"C":[(136,138)]},
 24:{"A":[(130,130)],"B":[(218,218)],"C":[(140,140)]},
 25:{"A":[(115,117)],"B":[(202,202)],"C":[(126,126)]},
 32:{"A":[(191,193)],"B":[(305,307)],"C":[(154,156)]},
 33:{"A":[(195,195)],"B":[(309,309)],"C":[(158,159)]},
 34:{"A":[(196,196)],"B":[(311,311)],"C":[(161,161)]},
 35:{"A":[(197,197)],"B":[(317,327)],"C":[(167,167)]},
 36:{"A":[(198,198)],"B":[(331,331)],"C":[(171,171)]},
 37:{"A":[(199,199),(205,205)],"B":[(313,313),(339,339)],"C":[(163,163),(179,179)]},
 38:{"A":[(200,200),(206,206)],"B":[(315,315),(341,341)],"C":[(165,165),(181,181)]},
 39:{"A":[(201,201),(207,208)],"B":[(329,329),(343,345)],"C":[(169,169),(183,185)]},
 40:{"A":[(202,202),(209,210)],"B":[(333,333),(347,349)],"C":[(173,173),(187,189)]},
 41:{"A":[(203,203),(211,212)],"B":[(335,335),(351,353)],"C":[(175,175),(191,193)]},
 42:{"A":[(204,204),(213,213)],"B":[(337,337),(355,355)],"C":[(177,177),(195,195)]},
}
for i in range(6):
    BASE_TEX[3+i]={"A":[(42+i,42+i),(48+i,48+i)],"B":[(46+4*i,48+4*i)],"C":[(29+2*i,29+2*i),(41+2*i,41+2*i)]}
    BASE_TEX[12+i]={"A":[(88+i,88+i),(94+i,94+i)],"B":[(109+4*i,111+4*i)],"C":[(56+2*i,56+2*i),(68+2*i,68+2*i)]}
    BASE_TEX[43+i]={"A":[(230+i,230+i)],"B":[(402+2*i,402+2*i)],"C":[(197+2*i,197+2*i)]}
for key,ino in zip(["crossed_A","crossed_B","crossed_C","crossed_D","crossed_E20","crossed_E23"],range(26,32)):
    BASE_TEX[ino]=KEY_TO_GROUP[key]["tex"]
BASE_TEX.update({
49:{"A":[(257,258)],"B":[(434,434)],"C":[(3,4)]},
50:{"A":[(86,87)],"B":[(104,107)]},
53:{"A":[(105,105)],"B":[(163,166)],"C":[(104,106)]},
54:{"A":[(106,106)],"B":[(168,171)],"C":[(108,110)]},
55:{"A":[(107,107)],"B":[(173,176)],"C":[(112,114)]},
})
for g in GROUPS:
    for ino in g["inventory"]:
        if ino >= 49 and ino not in BASE_TEX:
            BASE_TEX[ino] = g["tex"]

SOURCE_LINES = {
 1:[(6,8),(10,10),(18,18),(23,23),(26,26)], 2:[(33,42)],
 9:[(9,9)],10:[(2,2)],11:[(10,10)],18:[(12,13)],
 19:[(14,16)],20:[(14,17)],21:[(14,18)],22:[(14,18)],23:[(14,18)],
 24:[(14,14)],25:[(17,17)],26:[(19,19)],27:[(19,19)],28:[(20,20)],29:[(20,20)],
 30:[(21,21)],31:[(21,21)],32:[(22,22)],33:[(22,22)],
 34:[(23,23)],35:[(23,23)],36:[(23,23)],
 37:[(23,24)],38:[(23,24)],39:[(23,26)],40:[(23,26)],41:[(23,26)],42:[(23,25)],
 43:[(27,27)],44:[(27,27)],45:[(27,27)],46:[(28,28)],47:[(28,28)],48:[(29,29)],
 49:[(46,46)]
}
for i in range(3,9): SOURCE_LINES[i]=[(7,8)]
for i in range(12,18): SOURCE_LINES[i]=[(10,11)]
source_archive_line=next(i for i,line in enumerate((ROOT/"packets/013/C.tex").read_text().splitlines(),1)
                         if line=="% archive sheet number: 12")
SOURCE_LINES[49]=[(source_archive_line,source_archive_line)]

EXPLICIT_BBOX = {
 "margin_point":[43,398,53,411], "bent_residuals":[250,644,315,680],
 "rule_thickening_1303":[2217,1298,2239,1309], "rule_thickening_1091":[2308,1086,2324,1096],
 "lower_A_arrow":[146,909,181,1018], "lower_B_arrow":[497,937,552,1067],
 "right_edge":[2322,113,2351,1580],
}

def compact_components(role, index, row):
    comps = row.get("components")
    if not isinstance(comps,list): return []
    result=[]
    for j,comp in enumerate(comps):
        rr=ref(role,"differences",index)
        rr["pointer"]+=f"/components/{j}"
        if isinstance(comp,dict):
            d={"source":rr}
            for name in ("id","component","tex","description","reading","confidence","shape_confidence",
                         "bbox","role","hand","role_hand_origin"):
                if name in comp: d[name]=comp[name]
        else:
            d={"source":rr,"source_component_label":str(comp)}
        result.append(d)
    return result

DECISIONS=[]
DIFF_CROSSWALK=[]
DOUBT_CROSSWALK=[]
CROP_ISSUES=[]
for role in "ABC":
    for i,row in enumerate(REPORTS[role]["differences"]):
        DIFF_CROSSWALK.append({"reader":role,"source":ref(role,"differences",i),
          "decision_ids":[KEY_TO_GROUP[k]["id"] for k in DIFF_MAP[role][row["id"]]],
          "physical_keys":DIFF_MAP[role][row["id"]]})
    for i,row in enumerate(REPORTS[role]["doubts"]):
        DOUBT_CROSSWALK.append({"reader":role,"source":ref(role,"doubts",i),
          "decision_ids":[KEY_TO_GROUP[k]["id"] for k in DOUBT_MAP[role][i].split()],
          "physical_keys":DOUBT_MAP[role][i].split(),
          "location":row["location"],"reading":row["reading"],"alternatives":row.get("alternatives",[]),
          "confidence":row["confidence"],"reason_source_pointer":f"/doubts/{i}/reason"})

for g in GROUPS:
    recs={};readings={};crops=[];boxes=[];comps=[];rows=[]
    for role in "ABC":
        rr=[]
        for rid in g["rows"][role]:
            idx=DIFF_INDEX[role][rid];row=REPORTS[role]["differences"][idx];rows.append(row)
            rr.append({"source":ref(role,"differences",idx),"reading":row["reading"],
                       "original_flags":{k:row.get(k) for k in ("confidence","kind","diff_C","diff_H","C_doubt_status")},
                       "evidence_pointer":f"/differences/{idx}/evidence",
                       "bbox_exact":row.get("bbox"),
                       "qualification":row.get("qualification")})
            boxes.append(box(row))
            comps.extend(compact_components(role,idx,row))
            for name in ([row.get("readers_crop")]+row.get("additional_crops",[])):
                if name:
                    cp=f"readers/013/{role}/{name}"
                    if not (OUT / cp).is_file(): CROP_ISSUES.append(cp)
                    crops.append(cp)
        tr=tex_refs(role,g["tex"].get(role,[]))
        recs[role]={"report_rows":rr,"tex_sources":tr,
                    "source_status":"report reading with exact source links" if rr else
                        ("complete TeX only; no separate report difference row" if tr else
                         "no explicit corresponding report row or TeX component identified; no claim about ink absence")}
        readings[role]=list(dict.fromkeys(x["reading"] for x in rr)) if rr else (
            ["See literal TeX component(s) cited in reader_provenance"] if tr else [])
    first=next(iter(rows),{})
    cvalue=first.get("C")
    if not g["C_lines"]: cvalue=None
    if g["key"]=="grid": cvalue="Six-column array: five vertical separators; six explicit hline row boundaries"
    if g["key"]=="right_edge": cvalue="Ten local subpaths in packets/013/C.tex, lines 33–42"
    dd={"id":g["id"],"key":g["key"],"location":g["location"],"C":cvalue,"H":None,
        "final":None,"readers":readings,"reader_provenance":recs,
        "evidence":"Pending root ink adjudication. Literal reader evidence remains at the cited report pointers.",
        "crop":None,"candidate_crop_references":list(dict.fromkeys(crops)),
        "root_crop_requirement":"Root must inspect the relevant local crop(s); reader crop links are supplied.",
        "bbox":EXPLICIT_BBOX.get(g["key"],union_box(boxes)),
        "confidence":first.get("confidence","low"),
        "confidence_status":"provisional source proposal; root confidence pending",
        "confidence_candidates":{r:list(dict.fromkeys(x["original_flags"]["confidence"] for x in recs[r]["report_rows"])) for r in "ABC"},
        "kind":first.get("kind","drawing or diagram"),"diff_C":False,"diff_H":False,
        "diff_C_status":"awaiting root physical-locus decision; source flags preserved without adoption",
        "C_doubt_status":None,"source_C_doubt_row":g["C_row"],"marked_in_H":"not applicable",
        "mathematical_consequence":None,"root_decided":False,"main_approval_pending":True,
        "main_counting_decision_pending":True,"count_locus_key":"scan013-"+g["key"],
        "inventory_elements":[f"013.I{i:02d}" for i in g["inventory"]],
        "component_mapping":comps,
        "witness_C_sources":[text_ref("packets/013/C.tex",*rr) for rr in g["C_lines"]],
        "remaining_doubt_source_refs":[x["source"] for x in DOUBT_CROSSWALK if g["key"] in x["physical_keys"]],
        "pending_fields":["root final reading","root crop","root confidence","root count","final page attachment"],
        "proposed_page_sources":[],"root_page_sources":[]}
    choice=ROOT_CHOICES.get(g["key"])
    if choice:
        assert choice["root_exact_excerpt"] in ROOT_LOG, (g["key"],"choice lacks exact root source")
        dd.update({k:v for k,v in choice.items() if k not in ("root_exact_excerpt",)})
        dd["root_decision_source"]={**file_ref(ROOT_LOG_PATH),"anchor":choice["root_log_entry"],
                                    "exact_excerpt":choice["root_exact_excerpt"]}
        dd["root_decided"]=True
        dd["main_approval_pending"]=True
        if choice.get("root_additional_source_note"):
            note=choice["root_additional_source_note"]
            dd["root_additional_decision_source"]={**file_ref(ROOT_LOG_PATH),
               "anchor":"Source identity and arrow-coordinate addendum" if g["key"]!="right_edge" else "entries 38–40",
               "exact_excerpt":note}
        if choice.get("count_parent_key"):
            dd["count_parent_decision"]=KEY_TO_GROUP[choice["count_parent_key"]]["id"]
        for cp in choice.get("root_crops",[]):
            if not (OUT/cp).is_file(): CROP_ISSUES.append(cp)
    DECISIONS.append(dd)

# Attach explicit local paths rather than duplicating source command strings.
PATH_COMPONENTS=[]
for j in range(10):
    PATH_COMPONENTS.append({"physical_key":f"edge_{j+1:02d}","parent_inventory":"013.I02",
      "parent_decision":KEY_TO_GROUP["right_edge"]["id"],
      "witness_C":text_ref("packets/013/C.tex",33+j,33+j),
      "reader_paths":{"A":tex_refs("A",[(237+2*j,237+2*j)]),
                      "B":tex_refs("B",[(414+2*j,414+2*j)]),
                      "C":tex_refs("C",[(209+j,209+j)])},
      "reader_component_ids":{"A":f"E{j+1:02d}","B":f"G-edge-{j+1:02d}","C":f"Gedge{j+1}"},
      "bbox_source":ref("A","differences",DIFF_INDEX["A"]["A-G16"]),
      "bbox":REPORTS["A"]["differences"][DIFF_INDEX["A"]["A-G16"]]["components"][j]["bbox"],
      "root_status":"awaiting component selection"})
for j in range(12):
    PATH_COMPONENTS.append({"physical_key":f"horizontal_rule_{j+1:02d}","parent_inventory":"013.I01",
       "parent_decision":KEY_TO_GROUP["grid"]["id"],
       "reader_paths":{"A":tex_refs("A",[(27+j,27+j)]),"B":tex_refs("B",[(20+2*j,20+2*j)]),
                       "C":tex_refs("C",[(10+j,10+j)])},
       "reader_component_ids":{"A":f"R{j+1:02d}","B":f"horizontal rule at line {20+2*j}","C":f"horizontal rule at line {10+j}"},
       "root_status":"awaiting component selection; endpoints/gaps vary across literal paths"})
for j in range(5):
    PATH_COMPONENTS.append({"physical_key":f"vertical_trace_{j+1}","parent_inventory":"013.I01",
       "parent_decision":KEY_TO_GROUP["grid"]["id"],
       "reader_paths":{"A":tex_refs("A",[(40 if j==0 else 41,40 if j==0 else 41)]) if j in (0,3) else [],
                       "B":tex_refs("B",[(10+2*j,10+2*j)]),"C":tex_refs("C",[(22,22)])},
       "reader_component_ids":{"A":("V01" if j==0 else "V02") if j in (0,3) else None,
                               "B":f"vertical division {j+1}","C":f"subpath {j+1} of line 22"},
       "root_status":"A has two explicit traces; B and C have five; root to select local geometry"})
for key,ino in [("rule_thickening_1303",1),("rule_thickening_1091",1)]:
    PATH_COMPONENTS.append({"physical_key":key,"parent_inventory":f"013.I{ino:02d}",
      "parent_decision":KEY_TO_GROUP[key]["id"],
      "reader_paths":{r:tex_refs(r,rr) for r,rr in KEY_TO_GROUP[key]["tex"].items()},
      "root_status":"Explicit local thickening paths only in A/B at y1303 and A at y1091; other cited paths are adjoining rules"})
for key,ino,role,ranges,scope in [
    ("crossed_C_terminal",28,"B",[(296,296)],"additional low terminal hook"),
    ("crossed_E23_terminal",31,"B",[(298,298)],"additional low terminal hook"),
    ("pale_sub_C_raised_mark",35,"B",[(319,322)],"raised pale stroke over i"),
    ("pale_sub_C_right_curve",35,"B",[(324,327)],"pale curve beside right parenthesis")]:
    PATH_COMPONENTS.append({"physical_key":key,"parent_inventory":f"013.I{ino:02d}",
      "reader_paths":{role:tex_refs(role,ranges)},"scope":scope,
      "root_status":"local component retained in source crosswalk; final choice pending"})
if "date_hook" in ROOT_CHOICES:
    PATH_COMPONENTS.append({"physical_key":"date_hook_foot_thickening","parent_inventory":"013.I62",
      "parent_decision":KEY_TO_GROUP["date_hook"]["id"],"bbox":[404,639,417,640],
      "root_source":{**file_ref(ROOT_LOG_PATH),"anchor":"entry 27"},
      "root_path":r"\draw[black!70,line width=.50pt] (404,639)--(417,640);",
      "confidence":"medium","scope":"connected foot of date hook over the existing pale rule",
      "root_status":"selected within the date-hook cluster; no separate full rule or count"})

INVENTORY=[]
INV_CROSSWALK=[]
for role in ["witness_C","A","B","C"]:
    source_rows=SOURCE_INV if role=="witness_C" else REPORTS[role]["inventory"]
    for i,row in enumerate(source_rows):
        sr=({**file_ref("packets/013/C_inventory.json"),"pointer":f"/{i}","row_id":row["element"]}
            if role=="witness_C" else ref(role,"inventory",i))
        INV_CROSSWALK.append({"reader":role,"source":sr,
          "inventory_elements":[f"013.I{n:02d}" for n in INV_MAP[role][i]],
          "physical_component_scope":INV_SCOPE.get((role,i),"complete local item"),
          "source_hand":row["hand"],"source_kind":row["kind"],"source_sheet_kind":row["sheet_kind"],
          "source_transcribed":row["transcribed"]})
for ino in range(1,73):
    old=SOURCE_INV[ino-1] if ino<=48 else None
    if old:
        kind=old["kind"] if ino!=1 else "drawing"
        location=old["position"];words=old["first_words_or_objects"];pkey=f"source_{ino:02d}"
    else:
        pkey,kind,location,words=EXTRAS[ino-49]
    inv_id=f"013.I{ino:02d}"
    sources=[s for s in INV_CROSSWALK if inv_id in s["inventory_elements"]]
    hands=sorted(set(s["source_hand"] for s in sources))
    known_hand = ino<=48 and ino not in (1,2)
    proposed_hand="his hand" if known_hand else "undetermined hand"
    ds=[d for d in DECISIONS if inv_id in d["inventory_elements"]]
    bbs=[d["bbox"] for d in ds if d["bbox"] is not None]
    upper=union_box(bbs)
    if ino in (1,2,10,18,19,20,32,35,37,38,39,40,41,42):
        upper=None  # broad report crops/compound text spans do not establish exact upper ink extent
    inv={"sheet_kind":"list","sheet_kind_status":"proposed from A/C; witness C and reader B use cover",
      "hand":proposed_hand,"hand_status":"proposed only; root attribution pending",
      "source_hand_candidates":hands,"element":inv_id,"physical_key":pkey,"kind":kind,
      "position":location,"first_words_or_objects":words,"transcribed":"pending",
      "transcribed_basis":"All linked source returns say yes; final proposed-page attachment awaits root text selection.",
      "source_inventory":[s["source"] for s in sources],
      "source_inventory_scopes":[{"source":s["source"],"scope":s["physical_component_scope"]} for s in sources],
      "decision_ids":[d["id"] for d in ds],
      "reader_tex_sources":{r:tex_refs(r,rr) for r,rr in BASE_TEX.get(ino,{}).items()},
      "witness_C_sources":[text_ref("packets/013/C.tex",*rr) for rr in SOURCE_LINES.get(ino,[])],
      "local_components":[c for c in PATH_COMPONENTS if c["parent_inventory"]==inv_id],
      "sort_full_scan_xy":[upper[0],upper[1]] if upper else None,
      "sort_coordinate_basis":"upper extent of the cited reader locus bbox; no fresh image measurement" if upper else
                              "no exact upper ink extent returned; reader coordinate anchors retained in source links",
      "proposed_page_sources":[],"root_page_sources":[],"main_approval_pending":True}
    INVENTORY.append(inv)

# Actual C source rows, excluding notation and abbreviation sections.
C_DOUBT_LINES=(ROOT/"packets/013/C_doubts.txt").read_text().splitlines()
actual=[];in_doubts=False
for lineno,line in enumerate(C_DOUBT_LINES,1):
    if line=="## Doubtful readings": in_doubts=True;continue
    if line.startswith("## ") and in_doubts: break
    if in_doubts and line.startswith("| 13 |"):
        actual.append((lineno,line))
assert len(actual)==13
ACTUAL_C_MAP=[]
for n,(lineno,line) in enumerate(actual,1):
    gg=[g for g in GROUPS if g["C_row"]==n]
    ACTUAL_C_MAP.append({"source_row":n,"source_section":"Doubtful readings",
       "source":text_ref("packets/013/C_doubts.txt",lineno,lineno,excerpt=True),
       "local_subloci":[{"physical_key":g["key"],"decision_id":g["id"],
          "reader_statuses":{r:[REPORTS[r]["differences"][DIFF_INDEX[r][rid]].get("C_doubt_status")
             for rid in g["rows"][r] if REPORTS[r]["differences"][DIFF_INDEX[r][rid]].get("C_doubt_status")]
             for r in "ABC"}} for g in gg],
       "local_locus_count":len(gg),"root_source_row_status":
         ("resolved" if n in (1,2,5,7,10,11,12) else "retained") if identity_addendum else "pending"})
    for loc in ACTUAL_C_MAP[-1]["local_subloci"]:
        choice=ROOT_CHOICES.get(loc["physical_key"],{})
        loc["root_local_glyph_status"]=choice.get("local_C_glyph_doubt_status",choice.get("C_doubt_status"))
        loc["root_state_qualification"]=bool(choice.get("root_remaining_doubt")) and loc["physical_key"] in ("pale_A","pale_D","pale_sub_A","pale_sub_C")
assert sum(x["local_locus_count"] for x in ACTUAL_C_MAP)==14

DOUBTS=[]
for g in GROUPS:
    raw=[x for x in DOUBT_CROSSWALK if g["key"] in x["physical_keys"]]
    choice=ROOT_CHOICES.get(g["key"])
    remaining=choice.get("root_remaining_doubt") if choice else None
    if choice and not remaining: continue
    if not choice and not raw: continue
    DOUBTS.append({"location":g["location"],"decision_id":g["id"],
        "count_locus_key":"scan013-"+g["key"],
        "C_difference_count_group":choice.get("count_locus_key","scan013-"+g["key"]) if choice else "scan013-"+g["key"],
        "reading":remaining["reading"] if remaining else None,
        "alternatives":remaining["alternatives"] if remaining else [],
        "confidence":remaining["confidence"] if remaining else raw[0]["confidence"],
        "confidence_status":"root local doubt confidence" if remaining else "source proposal only; root pending",
        "reason":remaining["reason"] if remaining else "Root final doubt decision pending. Every local source candidate, position and confidence remains in source_components.",
        "source_components":[{"reader":x["reader"],"source":x["source"],"location":x["location"],
          "reading":x["reading"],"alternatives":x["alternatives"],"confidence":x["confidence"]} for x in raw],
        "root_components":choice.get("root_local_components",[]) if choice else [],
        "root_decision_source":{**file_ref(ROOT_LOG_PATH),"anchor":choice["root_log_entry"]} if choice else None,
        "root_decided":bool(choice),"main_approval_pending":True})

ATTENTION = [
 {"key":"pale_A","issue":"A/B resolve the glyph; C retains it. A separately qualifies deleted/live state; B/C retain deletion. A/B add exterior curves omitted from C-reader TeX."},
 {"key":"meditation","issue":"All return Méditation; A confidence medium, B/C high. Root still must inspect before adoption."},
 {"key":"crossed_B","issue":"A/C resolve ii; B retains ii|i. Hatching is explicit in A/B and generic deleted macro in C-reader."},
 {"key":"crossed_D","issue":"A/C resolve i; B retains i uncertainty. Hatching is explicit in A/B and generic deleted macro in C-reader."},
 {"key":"crossed_E23","issue":"A/C retain iv|iii; B gives iii|iv. B adds a terminal hook; all literal source commands remain cited."},
 {"key":"pale_D","issue":"All resolve the glyph. A/C retain deleted/live state qualification; B gives overwritten deletion only. Upper placement retained in source links."},
 {"key":"pale_sub_A","issue":"A/B resolve glyph; C retains glyph doubt. A/C give deleted-first state, B live-first. C TeX uses one outer unsure for both state alternatives; its report independently says glyph remains doubtful."},
 {"key":"pale_sub_C","issue":"A offers full (i)|opening-parenthesis with glyph/state doubt; B/C resolve opening parenthesis only. B retains raised mark and right curve graphically. State candidate order differs A/C deleted-first, B live-first."},
 {"key":"grid","issue":"A draws two pale vertical traces; B/C draw five. Twelve horizontal paths differ in endpoints/gaps: A interrupted y286/y932; C y932 only first-column segment; B continuous paths."},
 {"key":"top_cancellation","issue":"A draws 14 hatching approximation paths, B 15; C-reader uses generic deleted macro. Stroke counts describe source commands only."},
 {"key":"crossed_hatches","issue":"A/B hatch path counts: A 5/4; B 4/4; C 3/4 plus B terminal hook; D 4/3; E20 4/3; E23 4/4 plus B terminal hook. C-reader uses generic deleted macros for all six."},
 {"key":"margin","issue":"A keeps cluster in separate margin macro; B/C place it in connected page figure. A has tiny pale opposed-arrow head at x112; literal local paths differ."},
 {"key":"bent_residuals","issue":"All three preserve arch/slash/dot with varied component boxes. B doubt rows label slash medium while B difference component says high shape confidence; both exact qualifications retained."},
 {"key":"meditation_residuals","issue":"A draws five residual runs; C four longer/differently located runs; B has no explicit retained paths. A discloses upper crop boundary limitation."},
 {"key":"reveil_residuals","issue":"A/B preserve different interrupted components; A includes an inner wedge and two lower fragments. B explicitly leaves cancellation role open. C-reader has no corresponding explicit graphic."},
 {"key":"right_edge","issue":"All ten map one-for-one to witness C. A reports group changes for all; C reports changes at 5 and 10 only; B has no difference row, but all ten literal TeX paths are cited. Terminal bends/returns and pale E07 differ."},
 {"key":"lower_B_arrow","issue":"Shaft begins around y1000 in A, y1029 in B, y984 in C. Exact head and continuation paths vary. B report crop encloses more context than its rendered shaft."},
 {"key":"rule_thickenings","issue":"A y1303 wedge maps to B grid thickening; C retains only ordinary adjoining rule. A y1091 wedge has no separate B/C thickening command. Root must distinguish retained contour from additional doubtful mark."},
 {"key":"additional_graphics","issue":"B/C date hook, three Baumeister points and A lower slant; B-only Baumeister right upright, crossed-C patch, Jeu overmark, Spiel spot and Sch-I point; C-only point below Découverte. No unanimous reading inferred from missing rows."},
 {"key":"confidence","issue":"Several B graphic difference rows have high shape confidence while their corresponding doubt rows give medium. Both levels are retained at their exact pointers; none is silently collapsed."},
 {"key":"inventory_metadata","issue":"A/C sheet_kind=list, B/source C cover. Table/edge/archive hands differ or remain undetermined. Proposed hand values await root."},
 {"key":"final_attachment","issue":"Every inventory item has witness/reader text or path anchors. Proposed final page and upper ink-extent metadata for ordinary labels remain to attach from tex013/root."},
]

# Synchronize the exact, text-only final proposal supplied by tex013. No source
# reading or path is selected here; all selections remain in the cited map.
TEX_MAP_PATH="out/checks/scan013_tex_mapping.json"
TEX_MAP=json.loads((ROOT/TEX_MAP_PATH).read_text())
file_ref(TEX_MAP_PATH)
ROOT_PAGE_SOURCE="out/checks/scan013_final_draft.tex"
PAGE_TEXT=(ROOT/ROOT_PAGE_SOURCE).read_text()
PAGE_LINES=PAGE_TEXT.splitlines()
file_ref(ROOT_PAGE_SOURCE)
assert TEX_MAP["root_log_sha256"]==sha(ROOT_LOG_PATH), "tex map root-log snapshot needs refresh"
assert not TEX_MAP["pending_root_actions"], "tex selection remains pending"
assert not TEX_MAP["structural_validation"]["errors"], "tex clerk reports structural errors"
TEX_GROUP_INDEX={g["id"]:i for i,g in enumerate(TEX_MAP["groups"])}
TEX_GROUPS={g["id"]:g for g in TEX_MAP["groups"]}

def output_ref(group_id):
    g=TEX_GROUPS[group_id]
    oo=g.get("output")
    assert oo is not None, (group_id,"missing proposed-page output")
    body=PAGE_TEXT[oo["char_start"]:oo["char_end"]]
    assert hashlib.sha256(body.encode()).hexdigest()==oo["body_sha256"], (group_id,"output span hash")
    rr={**file_ref(ROOT_PAGE_SOURCE),"line_start":oo["line_start"],"line_end":oo["line_end"],
        "char_start":oo["char_start"],"char_end":oo["char_end"],
        "body_sha256":oo["body_sha256"],"group":group_id,"status":oo["status"],
        "selection_source":{**file_ref(TEX_MAP_PATH),"pointer":f"/groups/{TEX_GROUP_INDEX[group_id]}/selection"}}
    selection=g.get("selection") or {}
    if selection.get("represented_within"):
        rr["represented_within"]=selection["represented_within"]
        parent=TEX_GROUPS[selection["represented_within"]]["output"]
        rr["actual_representation_source"]={**file_ref(ROOT_PAGE_SOURCE),
           "line_start":parent["line_start"],"line_end":parent["line_end"],
           "body_sha256":parent["body_sha256"]}
    return rr

def selected_geometry_anchors(group_id):
    """Literal full-scan draw coordinates and outer node anchors only."""
    gg=TEX_GROUPS[group_id]
    if (gg.get("selection") or {}).get("represented_within"):
        return selected_geometry_anchors(gg["selection"]["represented_within"])
    oo=gg["output"];chunk=PAGE_TEXT[oo["char_start"]:oo["char_end"]]
    points=[];depth=0
    for line in chunk.splitlines():
        before=depth
        if before==0:
            if line.lstrip().startswith(r"\node"):
                matches=re.findall(r"\bat\s*\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)",line)
            elif line.lstrip().startswith((r"\draw",r"\fill",r"\path")) and "bounding box" not in line:
                matches=re.findall(r"\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)",line)
            else: matches=[]
            points.extend([float(x),float(y)] for x,y in matches)
        depth+=line.count(r"\begin{tikzpicture}")-line.count(r"\end{tikzpicture}")
    return points

INVENTORY_TEX_GROUPS={}
for x in TEX_MAP["crosswalk"]["packet_inventory"]:
    INVENTORY_TEX_GROUPS[int(x["source_id"].split(".")[1])]=list(x["groups"])
INVENTORY_TEX_GROUPS[1]+=["rule-lower-thickening","rule-live-thickening"]
INVENTORY_TEX_GROUPS[11]=["old-A"]  # exterior curves have their own physical entry I50
INVENTORY_TEX_GROUPS[28].append("cancel-C-terminal-hook")
INVENTORY_TEX_GROUPS[31].append("cancel-E23-terminal-hook")
extra_groups=[
 ["archive-comment"],["G-old-A-curves"],["title1-residuals"],["G-margin-point"],
 ["G-bent-upper-arch"],["G-bent-upper-dash"],["G-bent-upper-dot"],["G-Reveil-diagonal"],
 ["G-long-dot"],["G-A-blank-trace"],["G-A-foot-trace"],["G-E20-blot"],["G-E23-dash"],
 ["G-date-hook"],["G-Baumeister-upper-gray"],["G-Baumeister-upper-black"],["G-Baumeister-left-gray"],
 ["G-Baumeister-right-gray"],["G-cancel-C-gray-point"],["G-Jeu-overmark"],["G-Spiel-lower-spot"],
 ["G-D-point"],["G-A-edge-slant"],["G-Decouverte-point"]]
for ino,gg in enumerate(extra_groups,49): INVENTORY_TEX_GROUPS[ino]=gg

for d in DECISIONS:
    gids=list(TEX_MAP["record_key_crosswalk"][d["key"]])
    if d["key"]=="crossed_C":
        gids=[x for x in gids if x!="G-cancel-C-gray-point"]
    if d["key"]=="grid": gids+=["rule-lower-thickening","rule-live-thickening"]
    d["proposed_page_sources"]=[output_ref(gid) for gid in gids]
    d["tex_selection_source"]={**file_ref(TEX_MAP_PATH),"pointer":"/record_key_crosswalk/"+d["key"]}
    d["final_source_attachment_status"]="complete proposed source; root overall approval pending"
    d["pending_fields"]=["root overall approval"]
    if d["key"]=="right_edge":
        d["root_crops"]=["readers/013/A/"+n for n in ("21_edge_top.png","22_edge_middle.png","23_edge_lower.png","24_edge_foot.png")]
    if d["key"]=="rule_thickening_1091":
        d["root_crops"].append("crops/013/03_rules_subdivisions.png")

# Context links cannot be mistaken for independent contour readings.
BY_KEY={d["key"]:d for d in DECISIONS}
BY_KEY["rule_thickening_1303"]["readers"]={
 "A":["G06: filled local wedge (reading.tex line 228)"],
 "B":["G-grid-thickening-2227: thick straight segment (reading.tex line 44)"],
 "C":["Horizontal rule at reading.tex line 20; positional context only"]}
BY_KEY["rule_thickening_1091"]["readers"]={
 "A":["G07: filled local wedge (reading.tex line 229)"],
 "B":["Plain horizontal rule at reading.tex line 36; positional context only"],
 "C":["Plain horizontal rule at reading.tex line 18; positional context only"]}
for key,roles in [("rule_thickening_1303",["C"]),("rule_thickening_1091",["B","C"])]:
    for role in roles:
        BY_KEY[key]["reader_provenance"][role]["source_status"]="positional rule context only; this cited command supplies no local wedge contour"
        BY_KEY[key]["reader_provenance"][role]["tex_role"]="context_only"
BY_KEY["grid"]["readers"]["C"]=["Twelve horizontal draw paths and five vertical subpaths, reading.tex lines 10–22"]
BY_KEY["top_cancellation"]["readers"]["C"]=[r"\deleted{A (1976/77)}"]
BY_KEY["right_edge"]["readers"]["B"]=["Ten literal G-edge-01–G-edge-10 paths, reading.tex lines 414–432"]
for c in PATH_COMPONENTS:
    if c["physical_key"] in ("rule_thickening_1303","rule_thickening_1091"):
        c["context_only_readers"]=["C"] if c["physical_key"]=="rule_thickening_1303" else ["B","C"]
        c["exact_selected_contour_source"]=tex_refs("A",[(228,228)] if c["physical_key"]=="rule_thickening_1303" else [(229,229)])
    if c["physical_key"].startswith("edge_"):
        c["root_status"]="A exact local path selected by root entries37–40; geometry medium"
    elif c["parent_inventory"]=="013.I01":
        c["root_status"]="selected by root grid decision, with local qualifications and exact map"
    elif c["physical_key"] in ("crossed_C_terminal","crossed_E23_terminal"):
        c["root_status"]="B exact terminal-hook path selected by root"
    elif c["physical_key"] in ("pale_sub_C_raised_mark","pale_sub_C_right_curve"):
        c["root_status"]="component evidence represented within selected A fuller pale form, without duplicate path"

for inv in INVENTORY:
    ino=int(inv["element"].split("I")[1]);gids=INVENTORY_TEX_GROUPS[ino]
    if ino==49:
        lineno=next(i for i,line in enumerate(PAGE_LINES,1) if line=="% archive sheet number: 12")
        inv["proposed_page_sources"]=[text_ref(ROOT_PAGE_SOURCE,lineno,lineno,anchor="archive-comment",excerpt=True)]
        inv["hand"]="undetermined hand"
        inv["hand_status"]="root-selected in final provenance addendum"
    else:
        inv["proposed_page_sources"]=[output_ref(gid) for gid in gids]
    inv["transcribed"]="yes"
    inv["transcribed_basis"]="All required text/path/comment components are present in the attached proposed source; root overall approval remains pending."
    inv["final_source_attachment_status"]="complete proposed source"
    inv["tex_group_ids"]=gids
    inv["main_approval_pending"]=True
    if ino>=50 or ino in (1,2):
        inv["hand"]="undetermined hand"
        inv["hand_status"]="supported unresolved attribution retained; source candidates remain traceable"
    if ino in (11,34,35,36):
        inv["first_words_or_objects"]={
         11:"Pale A below dark A; glyph resolved, deleted/live state qualified",
         34:"Pale lower (i); glyph resolved, deleted/live state qualified",
         35:"Pale full (i) or opening parenthesis, with cancelled/live state; raised mark/right curve represented within the form",
         36:"Upper displaced (i); glyph resolved, deleted/live state qualified"}[ino]
        inv["hand"]="undetermined hand"
        inv["hand_status"]="root-selected for pale glyph/state components"
        inv["reading_state"]="deleted/overwritten first candidate; live alternative retained; exact glyph uncertainty remains in final reading"
    inv["sheet_kind"]="list"
    inv["sheet_kind_status"]="root-approved list; source cover/list alternatives preserved in inventory crosswalk"
    if ino<=48 and ino not in (1,2,11,34,35,36):
        inv["hand"]="his hand"
        inv["hand_status"]="root-approved for main text and clear author cancellations from returned agreement"
    if ino==28: inv["first_words_or_objects"]=r"\deleted{(\unsure{i|ii})}; B hatch paths and terminal hook"
    if ino==30: inv["first_words_or_objects"]=r"\deleted{(\unsure{i|ii})}; A hatch paths"
    if ino==31: inv["first_words_or_objects"]=r"\deleted{(\unsure{iii|iv})}; B hatch paths and terminal hook"
    if ino==36: inv["position"]="D live subdivision: upper pale displaced (i) above dark (i)"
    if ino==42: inv["first_words_or_objects"]="(iv) Le "+chr(96)*2+"Maître"+chr(39)*2+"; paired quote ticks"
    if ino==47: inv["first_words_or_objects"]="Sch VI; common top and bottom bars"
    if ino==48: inv["first_words_or_objects"]="Sch IX; common top and bottom bars"
    # Ordinary text anchors are preserved as anchors, without fabricating ink
    # extents from typography. Actual source bbox upper extents remain separate.
    anchors=[]
    if ino!=49:
        for gid in gids: anchors.extend(selected_geometry_anchors(gid))
    inv["source_position_anchors_full_scan"]=anchors
    inv["proposed_sort_anchor_xy"]=min(anchors,key=lambda xy:(xy[1],xy[0])) if anchors else None
    inv["proposed_sort_anchor_note"]="literal selected-source anchor; not asserted as upper ink extent"
    inv["reader_bbox_upper_extent_xy"]=inv["sort_full_scan_xy"]
    inv["sort_full_scan_xy"]=inv["proposed_sort_anchor_xy"]
    inv["sort_coordinate_basis"]="minimum ordinate among literal selected path coordinates / outer node anchors; text baseline anchors are not measured upper ink extents"
    inv["root_hand_decision_pending"]=False
    if ino==49:
        inv["sort_full_scan_xy"]=[2354,1668]
        inv["proposed_sort_anchor_xy"]=[2354,1668]
        inv["sort_coordinate_basis"]="root-approved lower-right selected-frame layout anchor for conservative end-of-page order; no archive ink pixel precision is claimed"
        inv["proposed_sort_anchor_note"]="layout-only proxy, explicitly approved by root; archive numeral remains comment-only"
assert next(i for i in INVENTORY if i["element"]=="013.I33")["sort_full_scan_xy"]==[526.0,984.0]
assert all(i["sort_full_scan_xy"] is not None for i in INVENTORY)
INVENTORY.sort(key=lambda i:(i["sort_full_scan_xy"][1],i["sort_full_scan_xy"][0],i["element"]))

BY_KEY["reveil_residuals"]["source_command_component_count"]={
 "reader":"A","commands":5,"components":6,
 "source":tex_refs("A",[(119,123)]),
 "note":"Last draw command contains two disconnected lower slants; corrected by root final provenance addendum."}
for d in DOUBTS:
    d["proposed_page_sources"]=BY_KEY[next(g["key"] for g in GROUPS if g["id"]==d["decision_id"])]["proposed_page_sources"]
    d["crop"]=BY_KEY[next(g["key"] for g in GROUPS if g["id"]==d["decision_id"])]["crop"]
for x in ATTENTION: x["status"]="source differences preserved; root choice recorded in corresponding decision"
for x in ATTENTION:
    if x["key"]=="meditation":
        x["issue"]="Readers all return Méditation, with A medium and B/C high. Root resolved the ending at high confidence in entry12."
    elif x["key"]=="final_attachment":
        x["issue"]="Every inventory item and decision now has exact proposed-page spans and body hashes. The pale-C raised mark/right curve retain represented_within links to the selected fuller form."
    elif x["key"]=="inventory_metadata":
        x["issue"]="Original sheet-kind and hand candidates remain traceable. The draft uses list and retains undetermined hand for unresolved graphical attribution. Root explicitly chose undetermined hand for archive12 in the final provenance addendum."
ATTENTION.append({"key":"sort_coordinates","status":"source metadata limitation, no uncovered ink choice",
 "issue":"For ordinary text labels the returns supply literal positioning anchors rather than measured upper ink extents. Both are distinguished; exact upper source bboxes are retained where supplied. Stable inventory IDs are unchanged."})
FINAL_ATTACHMENT_COMPLETE=all(i["proposed_page_sources"] for i in INVENTORY) and all(d["proposed_page_sources"] for d in DECISIONS)
assert FINAL_ATTACHMENT_COMPLETE
assert len(ROOT_CHOICES)==len(DECISIONS)==43
assert len(DOUBTS)==35
assert all(d["root_decided"] for d in DECISIONS)
assert sum(bool(d["diff_C"]) for d in DECISIONS)==40
assert len({d["count_locus_key"] for d in DECISIONS if d["diff_C"]})==40
assert all(d["final"] is not None for d in DECISIONS)
for d in DECISIONS:
    for cp in d.get("root_crops",[]):
        assert (OUT/cp).is_file(),cp
assert not CROP_ISSUES, CROP_ISSUES
assert all(not row.get("diff_H") and row.get("H") is None
           for r in "ABC" for row in REPORTS[r]["differences"])
assert all(REPORTS[r].get("check_events",[])==[] for r in "ABC")
assert all(row.get("mathematical_consequence") is None for r in "ABC" for row in REPORTS[r]["differences"])
assert len(DECISIONS)==43
assert len(INVENTORY)==72
assert len({i["element"] for i in INVENTORY})==72
assert all(i["reader_tex_sources"] for i in INVENTORY)
assert all(any(f"013.I{i:02d}" in x["inventory_elements"] for x in INV_CROSSWALK) for i in range(1,73))
assert set(x["kind"] for x in INVENTORY)<={"text","display","diagram","drawing","margin note","insertion","deletion"}

record={
 "scan":13,"folder":META["folder"],"their_page":META["their_page"],"hua_has":META["hua_has"],
 "filename":"J81-02_81_scan013.tex","brief_version":"v11","main_adjudicated":False,
 "draft_status":"all supplied root ink choices and proposed-source attachments complete; overall root approval pending",
 "decisions":DECISIONS,"doubts":DOUBTS,"inventory":INVENTORY,
 "notes":"Six-column title/reference list headed Notes 1, 5, 7, 15, 20, 23. Main letters are returned as A, B, C, D, E, E, with dates, French and German titles, translations, crossed and live subdivisions, arrows, footer references and ten surviving right-edge groups. The two written question marks remain identified separately. Archive numeral 12 belongs in the TeX comment. The reader returns contain no mathematical check.",
 "abbreviations":[{"form":f,"expansion":"No expansion is supplied on the sheet."} for f in ("M","HS","Sch")],
 "check_events":[],"reader_check_events":[],
 "check_events_note":"A, B and C report empty check_events. Mechanical source comparison is recorded only in workflow/provenance.",
 "workflow_note":"Text-only mechanical assembly after all three final independent returns. The clerk viewed no image, used no OCR, browser, research, compiler or delegation, and made no ink choice. All preserved reader fingerprints match. Every source difference/doubt/inventory row is crosswalked. Root choices 01–40 and the final provenance addendum are applied. The current proposed page is attached at exact spans and hashes. Root reports 40 distinct successfully inspected crops: 10 own ruling strips, 24 B, 5 A and 1 C. Root overall approval remains outstanding.",
 "source_manifest":list(MANIFEST.values()),"source_fingerprints":EXPECTED,
 "reader_completion":{r:{k:REPORTS[r].get(k) for k in ("start_utc","end_utc","full_image_viewed","halves_viewed","complete_visual_read")} for r in "ABC"},
 "reader_note_sources":{r:{**file_ref(f"out/readers/013/{r}/report.json"),"pointer":"/notes"} for r in "ABC"},
 "reader_notation_sources":{r:{**file_ref(f"out/readers/013/{r}/report.json"),"pointer":"/notation"} for r in "ABC"},
 "root_adjudication_log":file_ref(ROOT_LOG_PATH),"root_log_snapshot_fingerprint":sha(ROOT_LOG_PATH),
 "root_choices_recorded":list(ROOT_CHOICES),"proposed_root_page_source":ROOT_PAGE_SOURCE,
 "tex_mapping_source":file_ref(TEX_MAP_PATH),
 "tex_mapping_root_log_fingerprint":TEX_MAP["root_log_sha256"],
 "tex_selection_coverage":{"record_groups":43,"all_record_groups_attached":True,
   "inventory_items":72,"all_inventory_items_attached":True,
   "selected_tex_groups":len(TEX_MAP["selected_groups"]),"pending_tex_groups":TEX_MAP["pending_root_actions"]},
 "actual_C_doubt_map":ACTUAL_C_MAP,
 "C_doubt_source_classification":{"actual_source_rows":13,"local_subloci":14,"compound_source_row":13,
   "notation_rows":5,"abbreviation_rows":3,"classification":"Only the Doubtful readings table supplies source doubts."},
 "source_row_coverage":DIFF_CROSSWALK,"source_doubt_coverage":DOUBT_CROSSWALK,
 "inventory_coverage":INV_CROSSWALK,"source_path_map":PATH_COMPONENTS,
 "H_collation_groups":[],"attention_items":ATTENTION,
 "counts":{"C":sum(bool(d["diff_C"]) for d in DECISIONS),"H":0,
   "count_status":"root choices with prescribed group counts; overall approval pending",
   "C_by_confidence":dict(Counter(d["confidence"] for d in DECISIONS if d["diff_C"])),
   "main_decision_groups":len(DECISIONS),"inventory_items":len(INVENTORY),
   "remaining_doubt_entries":len(DOUBTS),
   "remaining_doubt_physical_count_keys":len({d["count_locus_key"] for d in DOUBTS}),
   "remaining_doubts_status":"all root local choices applied; compound source13 retains separately located13a/13b entries",
   "C_source_doubt_rows_resolved":7,"C_source_doubt_rows_retained":6,
   "C_source_local_glyph_loci_resolved":8,"C_source_local_glyph_loci_retained":6},
 "source_counts":{"differences":{r:len(REPORTS[r]["differences"]) for r in "ABC"},
   "doubts":{r:len(REPORTS[r]["doubts"]) for r in "ABC"},
   "inventory":{r:len(REPORTS[r]["inventory"]) for r in "ABC"},"witness_C_inventory":48},
 "counting_policy":"One physical locus or explicitly stated local cluster per witness. Glyph/state components share their physical count. Existing doubt retention alone contributes no C difference. Actual C doubt resolution and new qualification each require root decision. No H rows. Macro-only variation excluded; literal source strings retained.",
 "coverage_status":{"all_106_difference_rows_mapped":True,"all_78_reader_doubt_rows_mapped":True,
   "all_218_reader_inventory_rows_mapped":True,"all_48_C_inventory_rows_mapped":True,
   "all_13_C_source_doubt_rows_and_14_subloci_mapped":True,"all_10_C_edge_subpaths_mapped":True,
   "all_inventory_items_have_reader_source_anchors":True,"reader_fingerprints_unchanged":True,
   "crop_reference_files_exist":True,"root_ink_choices_applied":True,
   "main_adjudication_complete":False,"final_page_attachment_complete":FINAL_ATTACHMENT_COMPLETE},
 "assembly_timestamp_utc":ASSEMBLY_DATE,"assembly_revision":2,
 "root_actions_required":["Approve the serialized record and proposed page; all supplied reading, count, hand, sheet-kind and ordering decisions are applied",
   "Only root may write the approved main record, final page or cumulative outputs and commit"]
}
record["source_manifest"]=list(MANIFEST.values())
(CHECKS/"scan013_record_draft.json").write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n")

def cell(x):
    if x is None: return "pending"
    if isinstance(x,(list,dict)): x=json.dumps(x,ensure_ascii=False)
    return str(x).replace("|","\\|").replace("\n","<br>")
def table(headers,rows):
    return "| "+" | ".join(headers)+" |\n| "+" | ".join("---" for _ in headers)+" |\n"+"".join("| "+" | ".join(cell(x) for x in row)+" |\n" for row in rows)
md=["# Scan013 — mechanical mapping draft\n",
    "All supplied root choices 01–40 and the final provenance addendum are applied. The clerk makes no ink decision. Reader files are unchanged and all expected SHA-256 fingerprints match. H.tex is empty. Main approval remains false.\n",
    "## Coverage\n",
    table(["Source","Difference rows","Doubt rows","Inventory rows"],
          [[r,len(REPORTS[r]["differences"]),len(REPORTS[r]["doubts"]),len(REPORTS[r]["inventory"])] for r in "ABC"]+
          [["Witness C","13 actual doubt rows / 14 local loci","notation and abbreviations excluded",48]]),
    f"\nThe union has {len(DECISIONS)} decision groups and {len(INVENTORY)} inventory entries. All 106 reader difference rows, 78 reader doubt rows, 218 reader inventory rows and 48 C inventory rows have explicit crosswalks. All ten original edge subpaths are individually mapped. Applied root groupings produce 40 C differences and no H difference: 13a is the noncounting sibling of 13b, and the two ruling wedges belong to the grid count. There are {len(DOUBTS)} remaining-doubt entries, with source row 13's two local positions explicit. All final-source attachments are complete; overall root approval remains false.\n",
    "## Root dispositions\n",
    table(["ID","Key","Final reading / selected component","Confidence","C count","C source status"],
      [[d["id"],d["key"],d["final"],d["confidence"],d["diff_C"],d["C_doubt_status"]] for d in DECISIONS]),
    "## Physical decision crosswalk\n",
    table(["ID","Physical key","Location","A report rows","B report rows","C-reader report rows"],
      [[g["id"],g["key"],g["location"],", ".join(g["rows"]["A"]) or "TeX only / no explicit component",
        ", ".join(g["rows"]["B"]) or "TeX only / no explicit component",
        ", ".join(g["rows"]["C"]) or "TeX only / no explicit component"] for g in GROUPS]),
    "\n## Actual C doubt rows\n",
    table(["Source row","Physical decision(s)","A status","B status","C-reader status"],
      [[x["source_row"],"; ".join(s["decision_id"]+" "+s["physical_key"] for s in x["local_subloci"]),
        *["; ".join(s["physical_key"]+": "+"/".join(s["reader_statuses"][r]) for s in x["local_subloci"]) for r in "ABC"]]
       for x in ACTUAL_C_MAP]),
    "\n## Reader differences and provenance qualifications\n"]
for x in ATTENTION: md.append("- **"+x["key"]+"**: "+x["issue"]+"\n")
md.extend(["\n## Complete inventory crosswalk\n",
    "Source entries that split one physical cluster map to that entry's local components. The grid entries cover rule paths; text entries separately identify their labels. Every ordinary label, deletion, graphic and archive comment has exact reader-source links and verified spans/body hashes in the current proposed page.\n",
    table(["Source","Source element","Canonical element(s)","Component scope"],
      [[s["reader"],s["source"]["row_id"],", ".join(s["inventory_elements"]),s["physical_component_scope"]] for s in INV_CROSSWALK]),
    "\n## Component and source attachment policy\n",
    "The JSON retains exact path, JSON pointer, row ID and file SHA-256 links; whole reports and long coordinate commands are not copied into public reading fields. Source line ranges identify literal TeX commands. Every decision and all 72 inventory entries attach to the current proposed page. B36/C18 and C20 rule links are marked context-only at the wedge decisions. Missing reader report rows are distinguished from TeX-only representation and from a component not explicitly recorded. Root-page fields remain separate from proposed-page attachments until root approval.\n",
    "\n## Root work remaining\n"])
for s in record["root_actions_required"]: md.append("- "+s+"\n")
md.append("\n## Structural checks actually performed\n\n")
md.append("Verified schema-required keys, 43 unique decision IDs, 72 unique inventory IDs, allowed inventory kinds, all source-row maps, 13 source C rows / 14 local subloci, ten edge maps, source and crop file existence, H-null flags, empty mathematical-check lists, reader fingerprints, latest root-log fingerprint, and exact output-span hashes before serialization. All 43 root choices and all 72 inventory attachments are complete. No manuscript image, OCR, external source, compiler or renderer was used. No main record, page or cumulative output was written.\n")
(CHECKS/"scan013_mapping.md").write_text("\n".join(md))
print(json.dumps({"draft":"out/checks/scan013_record_draft.json","mapping":"out/checks/scan013_mapping.md",
 "groups":len(DECISIONS),"inventory":len(INVENTORY),"difference_rows_mapped":len(DIFF_CROSSWALK),
 "doubt_rows_mapped":len(DOUBT_CROSSWALK),"inventory_rows_mapped":len(INV_CROSSWALK),
 "root_choices":len(ROOT_CHOICES),"C_differences":record["counts"]["C"],
 "C_by_confidence":record["counts"]["C_by_confidence"],"H_differences":0,
 "doubts":len(DOUBTS),"all_proposed_page_attachments":FINAL_ATTACHMENT_COMPLETE,
 "main_adjudicated":False},ensure_ascii=False))
