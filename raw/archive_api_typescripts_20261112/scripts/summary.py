"""Summaries for the report: pages done per text, cost per batch and per text, difference counts by class, the
pages flagged for the in-app route. usage: python summary.py"""
import csv
import json
import pathlib
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
BASE = pathlib.Path(__file__).resolve().parent.parent
DIRS = {"ps": "pursuing_stacks", "esq": "esquisse", "ega25": "ega_v_cote25", "ega24": "ega_v_cote24_blass"}


def main():
    P = json.load(open(BASE / "PAGES.json", encoding="utf-8"))
    runs = [json.loads(l) for l in (BASE / "RUNS.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    done = [r for r in runs if r["event"] == "done"]
    per_text = defaultdict(lambda: [0, 0, 0, 0.0])
    for r in done:
        for q in r["requests"]:
            if q.get("ok"):
                t = q["key"].split("_")[0]
                c = (q["input_tokens"] * 2 + q["output_tokens"] * 10) / 1e6
                per_text[t][0] += 1
                per_text[t][1] += q["input_tokens"]
                per_text[t][2] += q["output_tokens"]
                per_text[t][3] += c
    total = Counter(p["text"] for p in P)
    print("## batches")
    for r in done:
        print(f"{r['name']}\t{r['batch_id']}\t{len(r['requests'])} pages\tin {r['input_tokens']}\tout {r['output_tokens']}"
              f"\t${r['billed_usd']:.2f}\t({r['wall_minutes']} min)")
    print("total billed $%.2f" % sum(r["billed_usd"] for r in done))
    print("## per text")
    for t in DIRS:
        n, i, o, c = per_text[t]
        print(f"{t}\t{n}/{total[t]} pages\t${c:.2f}\t${c / max(1, n):.4f}/page")
    print("## differences")
    for t in ("ps", "esq"):
        f = BASE / DIRS[t] / "DIFFERENCES.tsv"
        if f.exists():
            d = list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
            print(t, len(d), Counter(x["class"] for x in d).most_common())
    print("## long handwriting / many doubts")
    for t, dn in DIRS.items():
        f = BASE / dn / "NOTES.tsv"
        if not f.exists():
            continue
        rows = list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
        lh = [r["key"] for r in rows if r["long_handwriting"] == "yes"]
        many = [r["key"] for r in rows if int(r["n_illegible"]) >= 4 or int(r["n_unsure"]) >= 12]
        print(t, "long handwriting:", len(lh), lh)
        print(t, "illegible>=4 or unsure>=12:", len(many), many)


if __name__ == "__main__":
    main()
