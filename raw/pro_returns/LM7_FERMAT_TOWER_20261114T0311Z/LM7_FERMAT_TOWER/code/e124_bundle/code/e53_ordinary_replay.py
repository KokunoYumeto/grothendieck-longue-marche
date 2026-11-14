#!/usr/bin/env python3
"""Nine complete fresh E124 stages, exact text/JSON and whole GEN comparison."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys

R = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument("--gp", required=True)
ap.add_argument("--label", default="author_replay")
a = ap.parse_args()
gp = str(Path(a.gp).resolve())
D = R / "audit" / a.label
assert not D.exists(), str(D)
C = D / "fresh" / "code"
C.mkdir(parents=True)
I = C.parent / "inputs"
I.mkdir()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
immutable = ["e119_lower.bin", "e122_witnesses.json", "e122_witness_verify.out", "e123_presentation.out"]
for n in immutable:
    shutil.copy2(R / "inputs" / n, I / n)
W = json.loads((I / "e122_witnesses.json").read_text())
V = [json.loads(x) for x in (I / "e122_witness_verify.out").read_text().splitlines() if x.startswith("{")][0]
assert V["cube_identities"] == V["relative_norm_identities"] == 22
(I / "e53_ordinary_kernel_input.txt").write_text(json.dumps([W["root_exponents"], V["root_character_matrix"]]) + "\n")
assert (I / "e53_ordinary_kernel_input.txt").read_bytes() == (R / "inputs/e53_ordinary_kernel_input.txt").read_bytes()
sources = [
    "e53_ordinary_kernel.gp", "e53_ordinary_summary.py",
    "e53_positional_residues.py", "e53_ordinary_saturation.py",
    "e53_ordinary_frobenius_input.py", "e53_ordinary_frobenius.gp",
    "e53_ordinary_genus_chars.py", "e53_ordinary_genus.gp",
    "e53_ordinary_maps.py",
]
before = {n: sha(R / "code" / n) for n in sources}
for n in sources:
    shutil.copy2(R / "code" / n, C / n)
steps, jsons = [], []
for n in sources:
    stem = Path(n).stem
    cmd = [gp, "-q", "-f", n] if n.endswith(".gp") else [sys.executable, n]
    r = subprocess.run(cmd, cwd=C, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (C / (stem + ".out")).write_bytes(r.stdout)
    (C / (stem + ".err")).write_bytes(r.stderr)
    row = {
        "source": n, "exit_code": r.returncode,
        "stdout_byte_identity": r.stdout == (R / "code" / (stem + ".out")).read_bytes(),
        "stderr_byte_identity": r.stderr == (R / "code" / (stem + ".err")).read_bytes(),
        "stdout_sha256": sha(C / (stem + ".out")), "stderr_sha256": sha(C / (stem + ".err")),
    }
    steps.append(row)
    (D / "progress.json").write_text(json.dumps(steps, indent=2) + "\n")
    assert r.returncode == 0 and row["stdout_byte_identity"] and row["stderr_byte_identity"], row
    ref = R / "code" / (stem + ".json")
    if ref.exists():
        assert (C / ref.name).read_bytes() == ref.read_bytes(), ref.name
        jsons.append(ref.name)
for n in ["e53_ordinary_frobenius_input.txt", "e53_ordinary_genus_input.txt"]:
    assert (I / n).read_bytes() == (R / "inputs" / n).read_bytes(), n
assert all(sha(R / "code" / n) == h for n, h in before.items())
bins = ["e53_ordinary_kernel.bin", "e53_ordinary_genus.bin"]
lines = ["default(parisize,128000000);default(parisizemax,1000000000);",
         "check(a,s)=if(!a,error(s));", "{"]
for i, n in enumerate(bins):
    lines += [
        f'my(a{i}=read({json.dumps(str(R / "code" / n))}),b{i}=read({json.dumps(str(C / n))}));',
        f'check(a{i}===b{i},"complete decoded GEN equality");',
        f'print("{{\\"file\\":\\"{n}\\",\\"complete_GEN_identity\\":true,\\"components\\":",#a{i},"}}");',
    ]
lines += ['print("{\\"status\\":\\"PASS\\",\\"scope\\":\\"complete objects, zero exclusions\\"}");', "}", "quit;", ""]
(D / "compare_binary.gp").write_text("\n".join(lines))
r = subprocess.run([gp, "-q", "-f", "compare_binary.gp"], cwd=D, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(D / "compare_binary.out").write_bytes(r.stdout)
(D / "compare_binary.err").write_bytes(r.stderr)
bad = [x for x in r.stderr.decode().splitlines() if x.strip() and not
       x.strip().startswith("***   Warning: new stack size = ") and not
       x.strip().startswith("***   Warning: new maximum stack size = ")]
assert r.returncode == 0 and not bad, (r.returncode, bad)
rr = [json.loads(x) for x in r.stdout.decode().splitlines() if x.startswith("{")]
assert len(rr) == 3 and rr[-1]["status"] == "PASS"
out = {
    "status": "PASS", "steps": steps, "mathematical_source_hashes": before,
    "immutable_input_hashes": {n: sha(R / "inputs" / n) for n in immutable},
    "JSON_byte_identity": jsons, "generated_input_byte_identity": True,
    "complete_GEN_comparisons": rr[:-1],
    "raw_binary_comparisons": {
        n: {"reference_sha256": sha(R / "code" / n), "fresh_sha256": sha(C / n),
            "byte_identity": (R / "code" / n).read_bytes() == (C / n).read_bytes()} for n in bins
    },
    "excluded_fields": [], "upper_BNF_computation": False,
}
s = json.dumps(out, indent=2) + "\n"
(D / "verification.json").write_text(s)
(R / "code/e53_ordinary_replay.json").write_text(s)
print(s, end="")
