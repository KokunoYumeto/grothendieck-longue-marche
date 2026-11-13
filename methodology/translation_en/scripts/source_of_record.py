"""Compare the 116 current texts of the second pass (the input) with the copies published in the repository
KokunoYumeto/grothendieck-longue-marche (raw/second_pass/, the clone raw_publish_20261111/grothendieck-longue-marche,
after `git fetch`). Prints the commit of origin/main and, for each current text, whether the published blob is the same
(git hash-object of the local file against git ls-tree of origin/main). Writes source/SOURCE_OF_RECORD.json.
usage: python -I -B source_of_record.py
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_lm as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
CLONE = r"C:\Users\user\Documents\raw_publish_20261111\grothendieck-longue-marche"


def git(*a):
    return subprocess.run(["git", "-C", CLONE] + list(a), capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=600)


fetch = git("fetch", "origin")
head = git("rev-parse", "origin/main").stdout.strip()
when = git("log", "-1", "--format=%cI %s", "origin/main").stdout.strip()
tree = {}
for line in git("ls-tree", "-r", "origin/main", "raw/second_pass/").stdout.splitlines():
    meta, path = line.split("\t", 1)
    tree[os.path.basename(path)] = meta.split()[2]
rows, same, differ, absent = [], 0, [], []
for r in T.packages():
    name = os.path.basename(r["path"])
    local = subprocess.run(["git", "hash-object", r["path"]], capture_output=True, text=True).stdout.strip()
    pub = tree.get(name)
    st = "same" if pub == local else ("absent" if pub is None else "differs")
    if st == "same":
        same += 1
    elif st == "absent":
        absent.append(name)
    else:
        differ.append(name)
    rows.append({"package": r["package"], "current_text": r["current_text"], "sha256": T.sha256(r["path"]),
                 "git_blob": local, "published_blob": pub, "status": st})
out = {"repository": "KokunoYumeto/grothendieck-longue-marche", "clone": CLONE, "fetch_returncode": fetch.returncode,
       "origin_main": head, "origin_main_commit": when, "compared": len(rows), "same": same, "differs": differ,
       "absent_from_raw_second_pass": absent, "texts": rows}
T.write(os.path.join(T.ROOT, "source", "SOURCE_OF_RECORD.json"), json.dumps(out, ensure_ascii=False, indent=1) + "\n")
print("fetch rc", fetch.returncode, fetch.stderr.strip()[:200])
print("origin/main", head, when)
print("current texts %d: same as published %d; differ %d %s; not in raw/second_pass %d %s" % (
    len(rows), same, len(differ), differ[:10], len(absent), absent[:12]))
