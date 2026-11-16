"""Read-only intake diff of two results.csv files of a Pro run (id, statement, status, ...): new ids, removed ids,
status changes, and statements whose text changed. Usage: results_diff.py OLD.csv NEW.csv [max_chars]"""
import csv
import sys

sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10**9)


def load(p):
    with open(p, encoding="utf-8", errors="replace", newline="") as f:
        return {r["id"]: r for r in csv.DictReader(f)}


old, new = load(sys.argv[1]), load(sys.argv[2])
w = int(sys.argv[3]) if len(sys.argv) > 3 else 300
added = [k for k in new if k not in old]
removed = [k for k in old if k not in new]
status = [k for k in new if k in old and (old[k].get("status") or "") != (new[k].get("status") or "")]
text = [k for k in new if k in old and k not in status and (old[k].get("statement") or "") != (new[k].get("statement") or "")]
counts = {}
for r in new.values():
    counts[r.get("status") or ""] = counts.get(r.get("status") or "", 0) + 1
print(f"old {len(old)} rows, new {len(new)} rows; new statuses: {counts}")
print(f"added {len(added)}, removed {len(removed)}, status changed {len(status)}, statement changed {len(text)}")
for k in status:
    print(f"STATUS {k}: {old[k].get('status')} -> {new[k].get('status')} | {' '.join((new[k].get('statement') or '').split())[:w]}")
for k in added:
    print(f"NEW {k} [{new[k].get('status')}] {' '.join((new[k].get('statement') or '').split())[:w]}")
for k in removed:
    print(f"REMOVED {k} [{old[k].get('status')}]")
for k in text[:15]:
    print(f"TEXT {k} [{new[k].get('status')}] {' '.join((new[k].get('statement') or '').split())[:w]}")
