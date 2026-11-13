"""The run record: batches, tokens, costs (runs/RUNS.jsonl), check verdicts (checks/CHECKS*.json), fixes and waivers,
the compile results (build/COMPILE.tsv). Writes checks/REPORT.md and prints the totals.
usage: python -I -B report.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_lm as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")


def jl(p):
    return [json.loads(x) for x in T.read(p).splitlines() if x.strip()] if os.path.exists(p) else []


runs = [r for r in jl(os.path.join(T.ROOT, "runs", "RUNS.jsonl")) if r["event"] == "done"]
m = T.unit_map()
L = ["# Run record of the English translation of La Longue Marche", "",
     "| Batch | Ended (UTC) | Requests | Completed | Scans | Tokens in | Tokens out | Reasoning | Billed (Flex) | "
     "List price | Per scan | Wall min |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
tot = dict(req=0, ok=0, scans=0, tin=0, tout=0, treas=0, usd=0.0, lst=0.0, fa=0)
for r in runs:
    ok = sum(1 for q in r["requests"] if q["status"] == "completed" and q["text_chars"])
    L.append("| %s | %s | %d | %d | %d | %d | %d | %d | $%.4f | $%.4f | $%.4f | %.1f |" % (
        r["batch"], r["ended"][:16].replace("T", " "), len(r["requests"]) + len(r["failed_attempts"]), ok, r["scans"],
        r["input_tokens"], r["output_tokens"], r["reasoning_tokens"], r["billed_usd"], r["list_price_usd"],
        r["per_scan_billed_usd"] or 0, r["wall_minutes"]))
    tot["req"] += len(r["requests"]) + len(r["failed_attempts"])
    tot["fa"] += len(r["failed_attempts"])
    tot["ok"] += ok
    tot["scans"] += r["scans"]
    tot["tin"] += r["input_tokens"]
    tot["tout"] += r["output_tokens"]
    tot["treas"] += r["reasoning_tokens"]
    tot["usd"] += r["billed_usd"]
    tot["lst"] += r["list_price_usd"]
L.append("| **All** | | %d | %d | %d | %d | %d | %d | **$%.4f** | $%.4f | $%.4f | |" % (
    tot["req"], tot["ok"], tot["scans"], tot["tin"], tot["tout"], tot["treas"], tot["usd"], tot["lst"],
    tot["usd"] / tot["scans"] if tot["scans"] else 0))
done = {q["unit"] for r in runs for q in r["requests"] if q["text_chars"] and q["status"] == "completed"}
L += ["", "Units translated: %d of %d (%d scans of %d). Requests %d, of which %d failed or refused attempts that were "
      "resubmitted." % (len(done), len(m), sum(m[u]["n_scans"] for u in done), sum(u["n_scans"] for u in m.values()),
                        tot["req"], tot["fa"]), ""]
for name, label in (("CHECKS_raw.json", "output as it came back"), ("CHECKS.json", "English units (output + fixes)")):
    p = os.path.join(T.ROOT, "checks", name)
    if os.path.exists(p):
        c = json.loads(T.read(p))
        n = len(c)
        f = sum(1 for r in c.values() if r["verdict"] == "FAIL")
        L.append("Checks of the %s: %d units, %d pass, %d fail." % (label, n, n - f, f))
fx = jl(os.path.join(T.ROOT, "checks", "FIXES.jsonl"))
wv = jl(os.path.join(T.ROOT, "checks", "WAIVERS.jsonl"))
L += ["Fixes: %d in %d units (checks/FIXES.jsonl). Waivers: %d (checks/WAIVERS.jsonl)." % (
    len(fx), len({x["unit"] for x in fx}), len(wv)), ""]
p = os.path.join(T.ROOT, "build", "COMPILE.tsv")
if os.path.exists(p):
    rows = [x.split("\t") for x in T.read(p).splitlines()[1:]]
    from collections import Counter
    c = Counter(x[2] for x in rows)
    L.append("Compile of the English packages (build/COMPILE.tsv): %s." % "; ".join("%s: %d" % kv for kv in c.items()))
T.write(os.path.join(T.ROOT, "checks", "REPORT.md"), "\n".join(L) + "\n")
print("\n".join(L[-12:]))
