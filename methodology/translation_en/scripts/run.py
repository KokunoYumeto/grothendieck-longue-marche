"""Translate the units of La Longue Marche, one batch at a time (budget checked before each batch).

Model: GPT-6.1 Sol (gpt-6.1-sol), reasoning effort max, OpenAI Responses API, Flex tier (service_tier "flex"),
background mode, max_output_tokens 128,000, no tools; the prompt of prepare.py (prompt/system/<unit>.txt as the
instructions, prompt/user/<unit>.txt as the user message). The key is read only by enr_pilot.call
(enriques_api_pilot_20261106), from the user's note (the first OpenAI account, Untitled 1936.md), at each call; it is
never printed, copied, logged or stored.

Adapted from derivateurs_translation_20261111/scripts/run.py (the same request body, price arithmetic, retries, Flex
refusal handling and a row per batch in the cost ledger). What changed for this work:
  - the cap is the user's limit for the whole translation (CAP: $35 in the brief; $40 since 12 Nov 2026, 19:43 UTC,
    approved by the user after the pilot's projection of $35.41); before a batch, the dollars billed so far plus the
    batch's worst case (estimated input at the input price plus 128,000 output tokens per request at the output price)
    must stay within it;
  - after the pilot, the projection: dollars billed so far plus the French characters still to translate at the
    measured cost per character must stay within CAP, or the batch is not submitted (stop and report);
  - the source of record: before a batch, each package's current text still has the sha256 of source/MANIFEST.json,
    and each unit is still the same slice of it;
  - pages are scans; the ledger rows are lmtr-<batch>; Batch API never used (the user's rule: one batch job at a
    time, and another is running on the second account).

usage (from scripts/):
  python -I -B run.py plan
  python -I -B run.py batch NAME --next N            the next N units (manuscript order) without a translation
  python -I -B run.py batch NAME --units U1 U2 ...   these units (one already translated is re-run; its earlier output
                                                     goes to runs/out/attempts/)
  python -I -B run.py batch NAME --packages P1 P2    all units of these packages
  python -I -B run.py collect NAME                   wait for and collect a batch whose submitter stopped
"""
import json
import os
import shutil
import sys
import time
import urllib.error
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_lm as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
R = os.path.join(T.ROOT, "runs")
OUT = os.path.join(R, "out")
RUNS = os.path.join(R, "RUNS.jsonl")
MODEL, EFFORT, TIER = "gpt-6.1-sol", "max", "flex"
MAX_OUT = 128000
PRICE = (1.0, 5.0)    # billed per million tokens in/out at the Flex price
LIST = (2.0, 10.0)    # list price
CAP = 40.0            # the user's limit, raised from 35 on 12 Nov 2026 after the pilot's projection of $35.41
FINAL = ("completed", "incomplete", "failed", "cancelled")


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def runs():
    if not os.path.exists(RUNS):
        return []
    return [json.loads(x) for x in T.read(RUNS).splitlines() if x.strip()]


def log_run(rec):
    os.makedirs(R, exist_ok=True)
    with open(RUNS, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def spent():
    return sum(r["billed_usd"] for r in runs() if r["event"] == "done")


def in_flight():
    rs = runs()
    done = {r["batch"] for r in rs if r["event"] == "done"}
    return [r for r in rs if r["event"] == "submitted" and r["batch"] not in done]


def translated():
    return {u for r in runs() if r["event"] == "done" for u, q in r["units"].items() if q.get("text_chars")}


def chars_done():
    m = T.unit_map()
    return sum(m[q["unit"]]["chars"] for r in runs() if r["event"] == "done" for q in r["requests"]
               if q.get("text_chars"))


def projection():
    """(billed so far, cost per French character so far, projected total for all units not yet translated)."""
    m = T.unit_map()
    s, cd = spent(), chars_done()
    if not cd:
        return s, None, None
    left = sum(u["chars"] for uid, u in m.items() if uid not in translated())
    return s, s / cd, s + left * s / cd


def check_sources(units):
    man = T.manifest()
    pk = {p["package"]: p for p in man["packages"]}
    m = T.unit_map()
    for uid in units:
        u = m[uid]
        p = pk[u["package"]]
        path = os.path.join(T.LM, p["current_text"].replace("/", os.sep))
        if T.sha256(path) != p["sha256"]:
            raise SystemExit("%s changed since prepare.py: check the source of record" % p["current_text"])
        if T.sha256_text(T.read(path)[u["start"]:u["end"]]) != u["sha256"]:
            raise SystemExit("unit %s is no longer the same slice of its current text" % uid)


def openai_mod():
    sys.path.insert(0, r"C:\Users\user\Documents\enriques_api_pilot_20261106")
    import enr_pilot  # noqa: E402  (call(): the key is read from the user's note at each call, never printed)
    return enr_pilot


def api(P, method, url, body=None, tries=8):
    """enr_pilot.call with retries on network errors, unreadable answers and server errors."""
    for k in range(tries):
        try:
            code, r = P.call(method, url, body)
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError, ValueError) as e:
            print(time.strftime("%H:%M:%S"), "network error (%s), retry" % type(e).__name__, flush=True)
            time.sleep(min(30 * (k + 1), 300))
            continue
        if code >= 500 and k < tries - 1:
            print(time.strftime("%H:%M:%S"), "HTTP %d, retry" % code, flush=True)
            time.sleep(min(30 * (k + 1), 300))
            continue
        return code, r
    return 0, {"error": {"message": "no answer after %d tries" % tries}}


def body_for(unit):
    return {"model": MODEL, "instructions": T.read(os.path.join(T.ROOT, "prompt", "system", unit + ".txt")),
            "input": [{"role": "user", "content": [{"type": "input_text",
                                                    "text": T.read(os.path.join(T.ROOT, "prompt", "user",
                                                                                unit + ".txt"))}]}],
            "reasoning": {"effort": EFFORT}, "max_output_tokens": MAX_OUT, "background": True, "service_tier": TIER}


def est_input(body):
    return (len(body["instructions"]) + len(body["input"][0]["content"][0]["text"])) // 3


def worst_case(units):
    return sum(est_input(body_for(u)) * PRICE[0] / 1e6 + MAX_OUT * PRICE[1] / 1e6 for u in units)


def credit_exhausted(code, r):
    e = r.get("error") or {}
    return code == 429 and (e.get("code") == "insufficient_quota" or e.get("type") == "insufficient_quota")


def submit(P, unit, state, state_path):
    body = body_for(unit)
    for k in range(12):
        code, r = api(P, "POST", P.API, body)
        if code < 300 and r.get("id"):
            state["ids"].setdefault(unit, []).append(r["id"])
            T.write(state_path, json.dumps(state, ensure_ascii=False, indent=1))
            print(time.strftime("%H:%M:%S"), unit, "submitted", r["id"], r.get("status"), flush=True)
            return r["id"]
        err = json.dumps(r.get("error"))[:300]
        print(time.strftime("%H:%M:%S"), unit, "submit refused", code, err, flush=True)
        if credit_exhausted(code, r):
            raise SystemExit("the API reports exhausted credit (insufficient_quota): stopped")
        if code in (400, 401, 403):
            raise SystemExit("request rejected (%d): %s" % (code, err))
        time.sleep(min(60 * (k + 1), 600))
    raise SystemExit("could not submit " + unit)


def cmd_batch(name, units):
    if any(r["batch"] == name for r in runs()):
        raise SystemExit("batch %s exists (use collect)" % name)
    if in_flight():
        raise SystemExit("another batch is in flight: %s" % in_flight()[0]["batch"])
    m = T.unit_map()
    for u in units:
        if u not in m:
            raise SystemExit("unknown unit " + u)
    check_sources(units)
    s, w = spent(), worst_case(units)
    scans = sum(m[u]["n_scans"] for u in units)
    _, per_char, proj = projection()
    print("%s: %d units, %d scans, %d characters; worst case $%.2f; billed so far $%.4f%s; cap $%.2f" % (
        name, len(units), scans, sum(m[u]["chars"] for u in units), w, s,
        ("; projection for the whole translation $%.2f" % proj) if proj else "", CAP), flush=True)
    if s + w > CAP:
        raise SystemExit("billed so far plus the worst case of this batch would pass $%.2f: not submitted" % CAP)
    if proj and proj > CAP:
        raise SystemExit("the projection $%.2f passes the cap $%.2f: not submitted (stop and report)" % (proj, CAP))
    P = openai_mod()
    state_path = os.path.join(R, "state_%s.json" % name)
    state = {"batch": name, "units": units, "ids": {}, "t_start": time.time()}
    T.write(state_path, json.dumps(state, ensure_ascii=False, indent=1))
    log_run({"event": "submitted", "batch": name, "model": MODEL, "effort": EFFORT, "tier": TIER,
             "submitted": now(), "t_start": state["t_start"], "units": units, "scans": scans,
             "max_output_tokens": MAX_OUT, "worst_case_usd": round(w, 4), "billed_before_usd": round(s, 4),
             "cap_usd": CAP, "state": os.path.basename(state_path)})
    for u in units:
        submit(P, u, state, state_path)
    collect(name, P)


def save_attempt(unit):
    """Move an earlier output of the unit to runs/out/attempts/<unit>_a<k>.*"""
    a = os.path.join(OUT, "attempts")
    os.makedirs(a, exist_ok=True)
    k = 1
    while os.path.exists(os.path.join(a, "%s_a%d_result.json" % (unit, k))):
        k += 1
    for ext in (".tex", "_result.json"):
        p = os.path.join(OUT, unit + ext)
        if os.path.exists(p):
            shutil.move(p, os.path.join(a, "%s_a%d%s" % (unit, k, ext)))


def usage_cost(r):
    u = r.get("usage") or {}
    i_t, o_t = u.get("input_tokens") or 0, u.get("output_tokens") or 0
    return i_t, o_t, (i_t * PRICE[0] + o_t * PRICE[1]) / 1e6


def collect(name, P=None):
    P = P or openai_mod()
    state_path = os.path.join(R, "state_%s.json" % name)
    state = json.loads(T.read(state_path))
    units, t_start = state["units"], state["t_start"]
    for u in units:  # units whose submission was cut off by a stop
        if u not in state["ids"]:
            submit(P, u, state, state_path)
    final, t_end, failed_attempts, resubmits, retry_at = {}, {}, [], {}, {}
    last_note = 0
    while len(final) < len(units):
        time.sleep(60)
        for u in units:
            if u in final:
                continue
            if u in retry_at:  # a Flex refusal waiting for its resubmission
                if time.time() < retry_at[u]:
                    continue
                del retry_at[u]
                submit(P, u, state, state_path)
                continue
            rid = state["ids"][u][-1]
            code, r = api(P, "GET", "%s/%s" % (P.API, rid))
            st = r.get("status")
            if code != 200 or st not in FINAL:
                continue
            i_t, o_t, c = usage_cost(r)
            # Flex "server_is_overloaded" (nothing billed): resubmitted up to 8 times, after 4, 8, 16, 30 minutes;
            # any other failure: resubmitted at once, up to twice (the Dérivateurs rule from its batch b04).
            err = r.get("error") or {}
            if err.get("code") == "insufficient_quota":
                raise SystemExit("the API reports exhausted credit (insufficient_quota): stopped")
            overload = st == "failed" and err.get("code") == "server_is_overloaded" and not o_t
            limit = 8 if overload else 2
            if st in ("failed", "cancelled") and resubmits.get(u, 0) < limit:
                failed_attempts.append({"unit": u, "response_id": rid, "status": st, "error": r.get("error"),
                                        "input_tokens": i_t, "output_tokens": o_t, "billed_usd": round(c, 6)})
                k = resubmits.get(u, 0)
                resubmits[u] = k + 1
                if overload:
                    wait = min(240 * 2 ** k, 1800)
                    retry_at[u] = time.time() + wait
                    print(time.strftime("%H:%M:%S"), u, st, json.dumps(r.get("error"))[:200],
                          "-> resubmitted in %d min" % (wait // 60), flush=True)
                    continue
                print(time.strftime("%H:%M:%S"), u, st, json.dumps(r.get("error"))[:300], "-> resubmitted",
                      flush=True)
                submit(P, u, state, state_path)
                continue
            final[u] = r
            t_end[u] = time.time()
            print(time.strftime("%H:%M:%S"), u, st, "tier", r.get("service_tier"), "in", i_t, "out", o_t,
                  "$%.4f" % c, "(%d of %d done)" % (len(final), len(units)), flush=True)
        if time.time() - last_note > 900:
            last_note = time.time()
            print(time.strftime("%H:%M:%S"), "%d of %d done, %.0f min" % (len(final), len(units),
                                                                       (time.time() - t_start) / 60), flush=True)
    os.makedirs(OUT, exist_ok=True)
    m = T.unit_map()
    reqs, tin, tout, treas, billed = [], 0, 0, 0, 0.0
    for u in units:
        r = final[u]
        i_t, o_t, c = usage_cost(r)
        u_ = r.get("usage") or {}
        reasoning = (u_.get("output_tokens_details") or {}).get("reasoning_tokens")
        text = "".join(cc.get("text", "") for o in r.get("output", []) if o.get("type") == "message"
                       for cc in o.get("content", []) if cc.get("type") == "output_text")
        if os.path.exists(os.path.join(OUT, u + "_result.json")):
            save_attempt(u)
        meta = {"unit": u, "batch": name, "model": r.get("model"), "effort": EFFORT, "status": r.get("status"),
                "incomplete_details": r.get("incomplete_details"), "error": r.get("error"),
                "service_tier": r.get("service_tier"), "usage": u_, "input_tokens": i_t, "output_tokens": o_t,
                "reasoning_tokens": reasoning,
                "visible_output_tokens": (o_t - reasoning) if reasoning is not None else None,
                "billed_usd": round(c, 6), "text_chars": len(text), "response_id": r.get("id"),
                "scans": m[u]["n_scans"], "chars_french": m[u]["chars"],
                "minutes": round((t_end[u] - t_start) / 60, 1),
                "system_sha256": T.sha256(os.path.join(T.ROOT, "prompt", "system", u + ".txt")),
                "user_sha256": T.sha256(os.path.join(T.ROOT, "prompt", "user", u + ".txt")),
                "source_sha256": m[u]["sha256"]}
        if text:
            T.write(os.path.join(OUT, u + ".tex"), text)
        T.write(os.path.join(OUT, u + "_result.json"), json.dumps(meta, ensure_ascii=False, indent=1))
        tin += i_t
        tout += o_t
        treas += reasoning or 0
        billed += c
        reqs.append({k: meta[k] for k in ("unit", "status", "input_tokens", "output_tokens", "reasoning_tokens",
                                          "billed_usd", "text_chars", "scans", "chars_french", "minutes")})
    for fa in failed_attempts:
        tin += fa["input_tokens"]
        tout += fa["output_tokens"]
        billed += fa["billed_usd"]
    scans = sum(q["scans"] for q in reqs if q["text_chars"])
    rec = {"event": "done", "batch": name, "model": MODEL, "effort": EFFORT, "tier": TIER, "ended": now(),
           "wall_minutes": round((max(t_end.values()) - t_start) / 60, 1), "scans": scans,
           "scans_requested": sum(m[u]["n_scans"] for u in units), "input_tokens": tin,
           "output_tokens": tout, "reasoning_tokens": treas, "billed_usd": round(billed, 6),
           "list_price_usd": round((tin * LIST[0] + tout * LIST[1]) / 1e6, 6),
           "per_scan_billed_usd": round(billed / scans, 6) if scans else None, "requests": reqs,
           "failed_attempts": failed_attempts,
           "units": {q["unit"]: {"status": q["status"], "text_chars": q["text_chars"]} for q in reqs}}
    log_run(rec)
    ledger_row(rec)
    print("%s: %d units, %d scans translated; tokens in %d, out %d (reasoning %d); $%.4f at the Flex price ($%.4f a "
          "scan); %.1f min" % (name, len(units), scans, tin, tout, treas, billed, billed / scans if scans else 0,
                               rec["wall_minutes"]), flush=True)
    s, per_char, proj = projection()
    print("billed in all so far $%.4f; cost per French character $%.8f; projection for all 245 units $%.2f" % (
        s, per_char or 0, proj or 0), flush=True)


def ledger_row(rec):
    ok = sum(1 for q in rec["requests"] if q["status"] == "completed" and q["text_chars"])
    row = {"id": "lmtr-" + rec["batch"], "date": rec["ended"][:10],
           "project": "English translation of Grothendieck, La Longue Marche à travers la théorie de Galois (the "
                      "closed second pass of the transcription, second_pass/CURRENT_TEXT_INDEX.tsv of 12 Nov 2026)",
           "work": "%d units (runs of consecutive scans of one package), %d scans: %s" % (
               len(rec["requests"]), rec["scans"], ", ".join(q["unit"] for q in rec["requests"])),
           "method": "Responses API, Flex tier, background, "
                     "longue_marche_pro_pilot_20261104/translation_en_20261112/scripts/run.py",
           "model": "GPT-6.1 Sol (OpenAI)", "effort": EFFORT, "tier": TIER, "requests": len(rec["requests"]),
           "pages": rec["scans"], "scans": rec["scans"], "input_tokens": rec["input_tokens"],
           "output_tokens": rec["output_tokens"], "reasoning_tokens": rec["reasoning_tokens"],
           "usd_batch_price": round(rec["billed_usd"], 4), "cost_usd": round(rec["billed_usd"], 4),
           "list_price_usd": round(rec["list_price_usd"], 4),
           "per_page_billed_usd": round(rec["per_scan_billed_usd"], 4) if rec["per_scan_billed_usd"] else None,
           "key": "OpenAI project key (Untitled 1936.md)",
           "basis": "measured: usage of each answer; price %s/%s per million (Flex); pages are scans" % PRICE,
           "wall_minutes": rec["wall_minutes"],
           "result": "%d of %d translations completed%s; outputs in "
                     "longue_marche_pro_pilot_20261104/translation_en_20261112/runs/out" % (
                         ok, len(rec["requests"]),
                         (", %d failed attempts resubmitted" % len(rec["failed_attempts"]))
                         if rec["failed_attempts"] else "")}
    with open(T.LEDGER, "rb") as f:
        f.seek(0, 2)
        lead = ""
        if f.tell():
            f.seek(-1, 2)
            lead = "" if f.read(1) == b"\n" else "\n"
    with open(T.LEDGER, "a", encoding="utf-8") as f:
        f.write(lead + json.dumps(row, ensure_ascii=False) + "\n")


def cmd_plan():
    m = T.unit_map()
    done = translated()
    todo = [u for u in m if u not in done]
    s, per_char, proj = projection()
    print("units %d, translated %d, to do %d (%d scans, %d characters)" % (
        len(m), len(done), len(todo), sum(m[u]["n_scans"] for u in todo), sum(m[u]["chars"] for u in todo)))
    print("billed so far $%.4f; cap $%.2f; projection for all units %s; in flight: %s" % (
        s, CAP, ("$%.2f" % proj) if proj else "(none yet)", [r["batch"] for r in in_flight()] or "none"))
    if todo:
        n = 0  # the next units in order, each with its own worst case (its input differs)
        while n < len(todo) and s + worst_case(todo[:n + 1]) <= CAP:
            n += 1
        print("worst case of one more unit $%.3f; units that fit under the cap now: %d" % (worst_case(todo[:1]), n))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "plan":
        cmd_plan()
    elif a[0] == "batch":
        name = a[1]
        if "--next" in a:
            n = int(a[a.index("--next") + 1])
            done = translated()
            units = [u for u in T.unit_map() if u not in done][:n]
        elif "--packages" in a:
            want = [x for x in a[a.index("--packages") + 1:] if not x.startswith("--")]
            units = [u["id"] for u in T.units() if u["package"] in want]
        else:
            units = [u for u in a[a.index("--units") + 1:] if not u.startswith("--")]
        cmd_batch(name, units)
    elif a[0] == "collect":
        collect(a[1])
