"""Prepare an exact source-centralization witness test from cached finite data."""
from pathlib import Path
import argparse
import hashlib
import json

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--centralizers", choices=["short", "all"], default="short")
parser.add_argument("--method", choices=["data", "positive", "difference", "shortcut", "shortcut_v2"], default="data")
parser.add_argument("--cached-inverses", action="store_true")
parser.add_argument("--reduced-frames", action="store_true")
parser.add_argument("--stem")
args = parser.parse_args()
source_path = HERE / "pbc_iterated_adapted_pc.json"
source = json.loads(source_path.read_text())
orders = json.loads((HERE / "pbc_boundary_orders.json").read_text())
stem = args.stem or f"pbc_iterated_{args.method}_{args.centralizers}"
data = dict(source)
if args.reduced_frames:
    frame_path = HERE / "pbc_reduced_frames.json"
    data.update(json.loads(frame_path.read_text()))
    data["reduced_frame_input_sha256"] = hashlib.sha256(frame_path.read_bytes()).hexdigest()
if args.method in {"difference", "shortcut", "shortcut_v2"}:
    image_path = HERE / "pbc_adapted_images.json"
    images = json.loads(image_path.read_text())
    data.update(images)
    data["image_input_sha256"] = hashlib.sha256(image_path.read_bytes()).hexdigest()
if args.cached_inverses:
    inverse_path = HERE / "pbc_adapted_inverse_words.json"
    inverses = json.loads(inverse_path.read_text())
    data["finite_inverse_words"] = inverses["inverse_words"]
    data["element_orders"] = inverses["element_orders"]
    data["finite_inverse_input_sha256"] = hashlib.sha256(inverse_path.read_bytes()).hexdigest()
if args.centralizers == "short":
    si = [i for i, w in enumerate(source["s_centralizers"])
          if len(w) <= 2]
    ri = [i for i, w in enumerate(source["r_centralizers"])
          if len(w) <= 2 and orders["r"][i] % 3 == 0]
else:
    si = list(range(len(source["s_centralizers"])))
    ri = list(range(len(source["r_centralizers"])))
data["s_centralizers"] = [source["s_centralizers"][i] for i in si]
data["r_centralizers"] = [source["r_centralizers"][i] for i in ri]
data["original_s_centralizer_indices"] = [i + 1 for i in si]
data["original_r_centralizer_indices"] = [i + 1 for i in ri]
data["original_adapted_source_sha256"] = hashlib.sha256(source_path.read_bytes()).hexdigest()
data["scope"] = "a positive witness with these centralizers suffices; a negative result need not"
input_path = HERE / f"{stem}_source.json"
input_path.write_text(json.dumps(data, separators=(",", ":")) + "\n")
input_sha = hashlib.sha256(input_path.read_bytes()).hexdigest()
n = len(data["relative_orders"])
conjugates = [[] for _ in range(n)]
for i, j, word in data["conjugates"]:
    assert len(conjugates[i - 1]) == j - 1
    conjugates[i - 1].append(word)

def gap(value):
    return json.dumps(value, separators=(",", ":"))

fields = {
    "orders": data["relative_orders"],
    "powers": data["powers"],
    "conjugates": conjugates,
    "s": data["s"],
    "r": data["r"],
    "bs": data["left_s_frame"],
    "br": data["left_r_frame"],
    "cs": data["s_centralizers"],
    "cr": data["r_centralizers"],
    "trace_stem": f"LM8_PUSH/code/{stem}_trace",
    "source_sha256": input_sha,
}
if args.cached_inverses:
    fields["finite_inverse"] = data["finite_inverse_words"]
if args.method in {"difference", "shortcut", "shortcut_v2"}:
    fields["s_image"] = data["s_image"]
    fields["r_image"] = data["r_image"]
method_file = f"pbc_hermite_{args.method}_witness.g"
method_name = {
    "positive": "PBC_HermitePositiveWitness",
    "data": "PBC_HermiteDataWitness",
    "difference": "PBC_HermiteDifferenceWitness",
    "shortcut": "PBC_HermiteShortcutWitness",
    "shortcut_v2": "PBC_HermiteShortcutV2Witness",
}[args.method]
lines = [
    'LoadPackage("polycyclic");;',
    f'Read("LM8_PUSH/code/{method_file}");;',
    "PBC_data:=rec(" + ",".join(f"{k}:={gap(v)}" for k, v in fields.items()) + ");;",
    'Print("exact_data_source ",PBC_data.source_sha256,'
    '" centralizers ",Length(PBC_data.cs)," ",Length(PBC_data.cr),"\\n");',
    f"PBC_witness:={method_name}(PBC_data);;",
    'Print("targeted_witness_success ",PBC_witness.success,"\\n");',
    "if PBC_witness.success then",
    f' PrintTo("LM8_PUSH/code/{stem}_certificate.json",'
    '"{\\n\\"success\\":true,\\n\\"coefficients\\":",PBC_witness.coefficients,'
    '",\\n\\"relations\\":",PBC_witness.relations,'
    '",\\n\\"pivots\\":",PBC_witness.pivots,'
    '",\\n\\"s_count\\":",PBC_witness.s_count,'
    '",\\n\\"r_count\\":",PBC_witness.r_count,'
    '",\\n\\"proof_node\\":",PBC_witness.proof_node,'
    '",\\n\\"initial_target\\":",PBC_witness.initial_target,'
    '",\\n\\"initial_extras\\":",PBC_witness.initial_extras,"\\n}\\n");',
    "fi;",
    "QUIT;",
]
(HERE / f"{stem}.g").write_text("\n".join(lines) + "\n")
print(json.dumps({
    "input_sha256": input_sha,
    "finite_source_generators": n,
    "central_tail_generators": n * (n + 1) // 2,
    "s_centralizers": len(si),
    "r_centralizers": len(ri),
    "source_scope": data["scope"],
}, indent=2))
