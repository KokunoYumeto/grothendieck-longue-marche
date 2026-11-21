"""Apply only root-authorized Q01/Q02 current-map metadata repairs.

No selected TeX, source/path literal, record, approval, image or geometry changes.
The completed source audit is preserved and is not rerun.
"""
from pathlib import Path
import copy
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "out/checks"
MAP = OUT / "scan021_final_source_map.json"
TEX = OUT / "scan021_final_draft.tex"
HISTORY = OUT / "scan021_map_bounded_repair_v01.json"
OLD_MAP_SHA = "79e4b3af563b5ff38df37e3b7b317f7bad9c48f6b1151fe7c2f6046bd367dcf9"
TEX_SHA = "96772b7d5d36792f72827807deffaa39e746d1876f771e9dd498cbcf0238ddce"
AUDIT_SHA = "c575c4567a76c9b588ebf5633e4ab87447d6b12cbcb9d2355ebae5ef79708ac1"
sha = lambda b: hashlib.sha256(b).hexdigest()

before_bytes = MAP.read_bytes()
assert sha(before_bytes) == OLD_MAP_SHA
assert sha(TEX.read_bytes()) == TEX_SHA
assert sha((OUT / "scan021_qa_frozen_final_source_map.json").read_bytes()) == OLD_MAP_SHA
assert sha((OUT / "scan021_source_audit.md").read_bytes()) == AUDIT_SHA
assert not HISTORY.exists(), "Preserve any previous repair history; do not overwrite."
before = json.loads(before_bytes)
after = copy.deepcopy(before)
patches = []


def patch(parts, new, finding):
    target = after
    for part in parts[:-1]:
        target = target[part]
    old = copy.deepcopy(target[parts[-1]])
    target[parts[-1]] = new
    patches.append(dict(op="replace", pointer="/"+"/".join(map(str,parts)),
        finding=finding, before=old, after=copy.deepcopy(new), path_parts=parts))


for gid, did in [("C021-G02a", "L021-13"), ("B021-G03", "L021-18")]:
    index = next(i for i,g in enumerate(after["selected_groups"]) if g["id"] == gid)
    assert after["selected_groups"][index]["decision_ids"] == []
    patch(["selected_groups",index,"decision_ids"],[did],"Q01")

placements = {
    "A021G05": "The supplied child origin (896,469), west/baseline anchor (896,535), and C021-G02 origin (505,385) and baseline (505,555) remain attached with their source pointers.",
    "B021-G02-cancelled-Sigma": "The supplied child origin (1139,484), west/baseline anchor (1139,540), and C021-G02 origin (505,385) and baseline (505,555) remain attached with their source pointers.",
    "B021-G05-index": "The supplied child origin (1207,1132), west/baseline anchor (1207,1165), and C021-G04 origin (600,1070) and baseline (600,1165) remain attached with their source pointers.",
    "B021-G06-middle-row": "The supplied child origin (1534,1090) and west/baseline anchor (1534,1129) remain attached with their source pointers. A021DG retains source origin (1435,948), the A021DGanchor.north west anchor and shift={(-1435,-948)} placement scope with their source pointers.",
    "A021G22": "The supplied child origin (490,1863), west/baseline anchor (490,1907), and C021-G09 origin (180,1810) and baseline (180,2340) remain attached with their source pointers.",
    "A021G15": "The supplied child origin (947,1909), west/baseline anchor (947,1978), and C021-G09 origin (180,1810) and baseline (180,2340) remain attached with their source pointers.",
}
assert len(after["selected_unit_transfers"]) == 6
for index, transfer in enumerate(after["selected_unit_transfers"]):
    assert transfer["scope"] == "Identical declared full-scan coordinate map; no metric or geometric calculation."
    gid, parent = transfer["group"], transfer["parent"]
    scope = (
        "Copied full-scan coordinate pairs satisfy (x_new,y_new)=(x_old,y_old) as a source-literal correspondence. "
        f"For {gid}, the selected nested declaration {transfer['new_literal']} is the named parent {parent}'s declaration. "
        + placements[gid] +
        " The original and selected unit declarations remain explicit in old_literal and new_literal. "
        "This records the selected source construction; no metric, fitting, rescaling calculation or rendered validation is claimed."
    )
    patch(["selected_unit_transfers",index,"scope"],scope,"Q02")

# Bounded comparison: restore only the eight authorized field replacements.
restored = copy.deepcopy(after)
for item in patches:
    target = restored
    for part in item["path_parts"][:-1]:
        target = target[part]
    target[item["path_parts"][-1]] = item["before"]
assert restored == before
assert len(patches) == 8
new_bytes = (json.dumps(after,ensure_ascii=False,indent=2)+"\n").encode()
new_sha = sha(new_bytes)
temporary = OUT / "scan021_final_source_map_q01_q02.tmp"
temporary.write_bytes(new_bytes)
temporary.replace(MAP)
assert sha(MAP.read_bytes()) == new_sha
assert sha(TEX.read_bytes()) == TEX_SHA

history = dict(
    scope="Only Q01/Q02 current-map reverse associations and six unit-transfer descriptions.",
    before_map=dict(path="out/checks/scan021_qa_frozen_final_source_map.json",sha256_utf8=OLD_MAP_SHA),
    after_map=dict(path="out/checks/scan021_final_source_map.json",sha256_utf8=new_sha),
    selected_tex=dict(path="out/checks/scan021_final_draft.tex",sha256_utf8=TEX_SHA,changed=False),
    initial_source_audit=dict(path="out/checks/scan021_source_audit.md",sha256_utf8=AUDIT_SHA,rerun=False),
    root_authorization=dict(path="out/checks/scan021_root_source_review.md",
        sha256_utf8=sha((OUT/"scan021_root_source_review.md").read_bytes()),findings=["Q01","Q02"]),
    field_patches=patches,field_patch_count=len(patches),
    bounded_verification="Reversing these eight field replacements restores the complete prior JSON value; selected TeX hash is unchanged.",
    source_and_path_literal_fields_changed=False,record_changed=False,approval_fields_changed=False,
    main_approved=False,
    repair_script=dict(path="out/checks/scan021_repair_map_q01_q02.py",sha256_utf8=sha(Path(__file__).read_bytes())),
)
HISTORY.write_text(json.dumps(history,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(dict(map_sha256_utf8=new_sha,tex_sha256_utf8=TEX_SHA,
    history_path="out/checks/scan021_map_bounded_repair_v01.json",history_sha256_utf8=sha(HISTORY.read_bytes()),
    field_replacements=len(patches)),ensure_ascii=False))
