r"""Faithful transcriptions of three typescripts by collation, over the Anthropic Message Batches API (12 Nov 2026).

Model: Claude Opus 5.5 (claude-opus-5-5), adaptive thinking, effort high, Message Batches API (batch price $2 / $10
per million input / output tokens). One request per page: the system prompt (prompt_system.txt), then a short
context paragraph for the text and the page, the page's two images (work/img/<key>_a.jpg, _b.jpg, made by
prep_images.py), and the draft passage (alignment/drafts/<key>.txt) where there is one.

One batch at a time. Every batch is logged in RUNS.jsonl and gets a row in compute_cost_ledger/LEDGER.jsonl. The
requests are saved in batches/<name>/requests.jsonl with each image replaced by its file name, byte count and
SHA-256 (the images themselves are in work/img); the raw results in batches/<name>/results.jsonl.

Run through the key wrapper (stdlib only; the key is never printed or stored):
  set KEY_NOTE=<path of the local note that holds the API key>
  python -I C:\Users\user\Documents\claude_tools\run_with_note_key.py batch.py submit NAME KEYFILE_OR_SET [LIMIT]
  python -I ...run_with_note_key.py batch.py collect NAME
  python -I batch.py dry NAME KEYFILE_OR_SET          (build only, print sizes and the cost estimate; no key needed)
KEYFILE_OR_SET: a JSON list of page keys, or one of ps, esq, ega25, ega24 (every page of that text not yet answered).
"""
import base64
import hashlib
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

BASE = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS = BASE / "scripts"
IMG = BASE / "work" / "img"
BATCHES = BASE / "batches"
RUNS = BASE / "RUNS.jsonl"
LEDGER = pathlib.Path(r"C:\Users\user\Documents\compute_cost_ledger\LEDGER.jsonl")
MODEL, EFFORT, MAX_TOKENS = "claude-opus-5-5", "high", 32000
PRICE_IN, PRICE_OUT, LIST_IN, LIST_OUT = 2.0, 10.0, 4.0, 20.0
JOB_CAP_USD = 70.0          # the user's limit for this job
CREDIT_LEFT_START = 118.0   # the account's credit before this job (user, 12 Nov: "about $118")
EST_IN, EST_OUT = 9000, 6000  # per page, for the guard before the pilot; replaced by measured means afterwards
MAX_BODY = 200_000_000

TEXT_CONTEXT = {
    "ps": ("This page is from the typescript of Pursuing Stacks by A. Grothendieck (1983; English, with some letters "
           "in French), archive cote {cote}, site page {site} (PDF page {pdf}){ts}. The handwriting on it is "
           "Grothendieck's own unless the page shows otherwise."),
    "esq": ("This page is from the typescript of Esquisse d'un programme by A. Grothendieck (1984, French), first "
            "copy in archive cote 119, site page {site} (PDF page {pdf}){ts}."),
    "ega25": ("This page is from archive cote 25, \"Nouveau EGA V\": Grothendieck's French prenotes for the EGA "
              "(chapters IV 16, 17, 20 and 21, with a letter to Dieudonné), typed, with many handwritten "
              "corrections; site page {site} (PDF page {pdf}). The notation is that of the EGA: script letters "
              "(\\mathcal{{O}}_X, \\mathcal{{F}}), \"Module\" with a capital M, numbers such as (20.1.3); write "
              "them as typed or written. No draft is given for this text: transcribe the page."),
    "ega24": ("This page is from archive cote 24: P. Blass's English translation (1987) of Grothendieck's notes for "
              "EGA V (IV 20, \"Hyperplane sections and conic projections\"), typed, with typed translator's queries "
              "in brackets and handwritten notes (by the translator or another hand); site page {site} (PDF page "
              "{pdf}). No draft is given for this text: transcribe the page."),
}
DRAFT_CONTEXT = {
    "ps": ("The draft is the corresponding passage of the LaTeX source of the edition of Pursuing Stacks by M. Carmona "
           "with U. Buchholtz (arXiv 2111.01000 v2, 2021, made from the 2015 edition by \"the scrivener\"), {loc}. "
           "Its macros render as follows: \\Cat = Cat, \\Hot = Hot, \\HotOf(\\scrW) = Hot(W), \\scrW = W, \\Simplex = "
           "the simplex category, \\uphat = a hat (presheaves), \\op = op; \\pspage{{n}} or \\namedpspage{{..}}{{n}} "
           "is its marker for the beginning of typescript page n (placed by the editors; it can be off by a few "
           "words); \\scrcomment{{...}} and \\scrcommentinline{{...}} are the editors' own comments (marked as such, do "
           "not list them). Its margin notes and notes from the end of chapters are set as \\footnote{{...}}."),
    "esq": ("The draft is the corresponding passage of the Grothendieck Circle's typeset French text (EsquisseFr.pdf, "
            "2008, which follows the printed edition of 1997), as extracted from the PDF's text layer, {loc}. The "
            "extraction keeps the words but loses the layout: it breaks and hyphenates lines where the typesetting "
            "did, mixes running heads and the typescript page numbers printed in the margin (bare numbers on lines "
            "of their own) into the text, and scrambles formulas and diagrams; accents were recomposed by script. "
            "Ignore these artefacts; list differences in words, letters, accents, punctuation, numbers, footnote "
            "markers, and in formulas where the content clearly differs."),
}


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def pages():
    return {p["key"]: p for p in json.load(open(BASE / "PAGES.json", encoding="utf-8"))}


def runs():
    if not RUNS.exists():
        return []
    return [json.loads(l) for l in RUNS.read_text(encoding="utf-8").splitlines() if l.strip()]


def log_run(rec):
    with open(RUNS, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def billed_total():
    return sum(r.get("billed_usd", 0) for r in runs() if r["event"] == "done")


def answered_keys():
    out = set()
    for r in runs():
        if r["event"] == "done":
            out |= {q["key"] for q in r["requests"] if q.get("ok")}
    return out


def measured_means(text=None):
    """mean input and output tokens per page, over the pages of one text when given (measured in earlier batches)"""
    tin = tout = n = 0
    for r in runs():
        if r["event"] == "done":
            for q in r["requests"]:
                if q.get("input_tokens") and (text is None or q["key"].split("_")[0] == text):
                    tin += q["input_tokens"]
                    tout += q["output_tokens"]
                    n += 1
    return (tin / n, tout / n) if n else (EST_IN, EST_OUT)


def user_content(p):
    ts = ""
    if p["ts_page"]:
        ts = f"; by the alignment it is typescript page {p['ts_page']}"
    if p["text"] == "esq" and p["site"] == 2:
        ts = "; it is the sommaire (contents)"
    head = TEXT_CONTEXT[p["text"]].format(cote=p["cote"], site=p["site"], pdf=p["pdf_page"], ts=ts)
    if p["text"] == "ps" and not p["draft"]:
        head += (" No draft is given for this page (the edition does not contain it): transcribe the page.")
    content = [{"type": "text", "text": head + "\n\nThe upper part of the page:"}]
    meta = []
    for part, label in (("a", None), ("b", "The lower part of the page (it overlaps the upper part by a few lines):")):
        f = IMG / f"{p['key']}_{part}.jpg"
        data = f.read_bytes()
        if label:
            content.append({"type": "text", "text": label})
        content.append({"type": "image", "source": {"type": "base64", "media_type": "image/jpeg",
                                                     "data": base64.standard_b64encode(data).decode("ascii")}})
        meta.append({"file": f"work/img/{f.name}", "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    if p["draft"]:
        d = (BASE / "alignment" / "drafts" / f"{p['key']}.txt").read_text(encoding="utf-8")
        content.append({"type": "text", "text": DRAFT_CONTEXT[p["text"]].format(loc=p["draft_location"]) +
                        "\n\n<draft>\n" + d + "\n</draft>"})
        content.append({"type": "text", "text": "Transcribe the page from the images, then compare with the draft, "
                                                "and write the three sections."})
    else:
        content.append({"type": "text", "text": "Transcribe the page from the images, and write the sections "
                                                "TRANSCRIPTION and NOTES (no DIFFERENCES section)."})
    return content, meta


def build(keys):
    system = (SCRIPTS / "prompt_system.txt").read_text(encoding="utf-8")
    P = pages()
    reqs, saved, size = [], [], 0
    for k in keys:
        p = P[k]
        content, meta = user_content(p)
        params = {"model": MODEL, "max_tokens": MAX_TOKENS, "thinking": {"type": "adaptive"},
                  "output_config": {"effort": EFFORT}, "system": system,
                  "messages": [{"role": "user", "content": content}]}
        r = {"custom_id": k.replace("-", "_").replace(".", "_")[:64], "params": params}
        s = len(json.dumps(r))
        if size + s > MAX_BODY:
            break
        size += s
        reqs.append(r)
        sv = json.loads(json.dumps(r))
        imgs = [c for c in sv["params"]["messages"][0]["content"] if c["type"] == "image"]
        for c, m in zip(imgs, meta):
            c["source"] = {"type": "base64-omitted", "media_type": "image/jpeg", **m}
        sv["params"]["system"] = "scripts/prompt_system.txt (sha256 %s)" % hashlib.sha256(
            system.encode("utf-8")).hexdigest()
        sv["page_key"] = k
        saved.append(sv)
    return reqs, saved, size


def select(spec):
    P = pages()
    done = answered_keys()
    if spec.endswith(".json"):
        keys = json.load(open(BASE / spec if not os.path.isabs(spec) else spec, encoding="utf-8"))
    else:
        keys = [k for k, p in P.items() if p["text"] == spec]
    return [k for k in keys if k not in done]


def a_api(method, url, body=None):
    h = {"x-api-key": os.environ.get("ANTHROPIC_API_KEY", ""), "anthropic-version": "2023-06-01",
         "content-type": "application/json"}
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=body, headers=h, method=method),
                                        timeout=1800) as r:
                return r.status, r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode("utf-8", "replace")
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            print(time.strftime("%H:%M:%S"), "network error", str(e)[:120], "- retrying", flush=True)
            time.sleep(30 * (attempt + 1))
    return 0, "network error"


def guard(n, text=None):
    mi, mo = measured_means(text)
    est = n * (mi * PRICE_IN + mo * PRICE_OUT) / 1e6
    spent = billed_total()
    left_job = JOB_CAP_USD - spent
    left_credit = CREDIT_LEFT_START - spent
    return est, spent, left_job, left_credit


def cmd_dry(name, spec, limit=None):
    keys = select(spec)
    if limit:
        keys = keys[:int(limit)]
    reqs, saved, size = build(keys)
    texts = {k.split("_")[0] for k in keys}
    est, spent, lj, lc = guard(len(reqs), texts.pop() if len(texts) == 1 else None)
    print(f"{name}: {len(reqs)} requests ({len(keys)} selected), {size / 1e6:.1f} MB; estimate ${est:.2f}; "
          f"billed so far ${spent:.2f}; job cap left ${lj:.2f}; credit left about ${lc:.2f}")
    return reqs, saved, size, est


def cmd_submit(name, spec, limit=None):
    assert os.environ.get("ANTHROPIC_API_KEY"), "run through run_with_note_key.py with KEY_NOTE"
    open_ = {r["batch_id"] for r in runs() if r["event"] == "submitted"} - {
        r["batch_id"] for r in runs() if r["event"] == "done"}
    if open_:
        raise SystemExit(f"a batch is still open: {open_}; collect it first (one batch at a time)")
    reqs, saved, size, est = cmd_dry(name, spec, limit)
    if not reqs:
        raise SystemExit("nothing to send")
    _, spent, lj, lc = guard(0)
    if est * 1.3 > lj or est * 1.3 > lc - 10:
        raise SystemExit(f"STOP: estimate ${est:.2f} (x1.3) exceeds the job cap left ${lj:.2f} or the credit "
                         f"left about ${lc:.2f} less a $10 margin")
    d = BATCHES / name
    d.mkdir(parents=True, exist_ok=False)
    with open(d / "requests.jsonl", "w", encoding="utf-8") as f:
        for s in saved:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    code, body = a_api("POST", "https://api.anthropic.com/v1/messages/batches",
                       json.dumps({"requests": reqs}).encode("utf-8"))
    if code != 200:
        raise SystemExit("batch submit %d: %s" % (code, body[:800]))
    bt = json.loads(body)
    log_run({"event": "submitted", "name": name, "batch_id": bt["id"], "submitted": now(),
             "keys": [s["page_key"] for s in saved], "requests": len(reqs), "mb": round(size / 1e6, 1),
             "estimate_usd": round(est, 2), "billed_before_usd": round(spent, 2)})
    print("submitted", bt["id"], flush=True)
    cmd_collect(name)


def cmd_collect(name):
    sub = [r for r in runs() if r["event"] == "submitted" and r["name"] == name][-1]
    bid = sub["batch_id"]
    while True:
        code, r = a_api("GET", "https://api.anthropic.com/v1/messages/batches/" + bid)
        if code != 200:
            print(time.strftime("%H:%M:%S"), "status", code, r[:200], flush=True)
            time.sleep(60)
            continue
        s = json.loads(r)
        print(time.strftime("%H:%M:%S"), s["processing_status"], json.dumps(s["request_counts"]), flush=True)
        if s["processing_status"] == "ended":
            break
        time.sleep(60)
    code, body = a_api("GET", s["results_url"])
    assert code == 200, (code, body[:300])
    d = BATCHES / name
    (d / "results.jsonl").write_text(body, encoding="utf-8")
    idmap = {k.replace("-", "_").replace(".", "_")[:64]: k for k in sub["keys"]}
    reqs, tin, tout = [], 0, 0
    for line in body.splitlines():
        if not line.strip():
            continue
        x = json.loads(line)
        key = idmap[x["custom_id"]]
        if x["result"]["type"] != "succeeded":
            reqs.append({"key": key, "ok": False, "result": x["result"]["type"]})
            continue
        m = x["result"]["message"]
        u = m.get("usage") or {}
        i_t = (u.get("input_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0) + (
            u.get("cache_read_input_tokens") or 0)
        o_t = u.get("output_tokens") or 0
        tin += i_t
        tout += o_t
        text = "".join(c.get("text", "") for c in m["content"] if c.get("type") == "text")
        ok = m.get("stop_reason") == "end_turn" and "%%% TRANSCRIPTION" in text
        reqs.append({"key": key, "ok": ok, "stop_reason": m.get("stop_reason"), "input_tokens": i_t,
                     "output_tokens": o_t, "chars": len(text)})
    cost = (tin * PRICE_IN + tout * PRICE_OUT) / 1e6
    lp = (tin * LIST_IN + tout * LIST_OUT) / 1e6
    t0 = datetime.fromisoformat(s["created_at"].replace("Z", "+00:00"))
    t1 = datetime.fromisoformat(s["ended_at"].replace("Z", "+00:00"))
    n_ok = sum(1 for q in reqs if q["ok"])
    rec = {"event": "done", "name": name, "batch_id": bid, "ended": s["ended_at"],
           "wall_minutes": round((t1 - t0).total_seconds() / 60, 1), "input_tokens": tin, "output_tokens": tout,
           "billed_usd": round(cost, 4), "list_usd": round(lp, 4), "pages_ok": n_ok,
           "requests": sorted(reqs, key=lambda q: q["key"])}
    log_run(rec)
    texts = sorted({k.split("_")[0] for k in sub["keys"]})
    row = {"id": f"typescripts-api-{name}", "date": s["ended_at"][:10],
           "project": "Faithful transcriptions of three typescripts (Pursuing Stacks, Esquisse d'un programme, "
                      "EGA V cotes 24 and 25) by collation (grothendieck_archive_transcription_20261110/"
                      "api_typescripts_20261112)",
           "work": f"batch {name}: {len(reqs)} pages, one request per page ({', '.join(texts)}): diplomatic LaTeX "
                   f"transcription from two page images, with the list of differences against the draft where "
                   f"there is one",
           "method": "Message Batches API, scripts/batch.py", "model": MODEL, "effort": EFFORT,
           "requests": len(reqs), "pages": len(reqs), "input_tokens": tin, "output_tokens": tout,
           "usd_batch_price": round(cost, 2), "list_price_usd": round(lp, 2),
           "per_page_billed_usd": round(cost / max(1, len(reqs)), 4),
           "key": "the user's API account",
           "basis": "measured: usage of each answer; price 2.0/10.0 per million (batch)",
           "wall_minutes": rec["wall_minutes"], "result": f"{n_ok} of {len(reqs)} pages answered in full",
           "batch": bid}
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"{name}: {n_ok}/{len(reqs)} ok; tokens in {tin}, out {tout}; ${cost:.2f} at batch price "
          f"(${cost / max(1, len(reqs)):.4f}/page); job total ${billed_total():.2f}", flush=True)


if __name__ == "__main__":
    cmd, *args = sys.argv[1:]
    {"dry": cmd_dry, "submit": cmd_submit, "collect": cmd_collect}[cmd](*args)
