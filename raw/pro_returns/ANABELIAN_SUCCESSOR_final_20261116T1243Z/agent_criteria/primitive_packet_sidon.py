#!/usr/bin/env python3
"""Exact necessary theta-packet tests, e=19, genus 2 in characteristic 2.

Only this agent's output path is written. No finite-field arithmetic or
external package is used. A solution means this necessary test is inconclusive.
"""
import itertools
import json
import math
from pathlib import Path


def subgroup(n, gens):
    out = {1}
    todo = [1]
    while todo:
        a = todo.pop()
        for b in gens:
            c = a*b % n
            if c not in out:
                out.add(c)
                todo.append(c)
    return frozenset(out)


def cosets(n, group, ambient):
    todo = set(ambient)
    out = []
    while todo:
        a = min(todo)
        c = frozenset(a*b % n for b in group)
        assert c <= todo
        out.append(c)
        todo -= c
    return out


def differences(n, values):
    counts = [0]*n
    for a in values:
        for b in values:
            if a != b:
                counts[(a-b) % n] += 1
    return counts


def solve(n):
    units = {a for a in range(n) if math.gcd(a, n) == 1}
    double = subgroup(n, [2])
    packet = subgroup(n, [pow(2, 19, n), n-1])
    # Symmetry links a doubling orbit and its negative. At n=191 these are
    # distinct; using <2,-1> handles that case without double counting.
    double_sign = subgroup(n, [2, n-1])
    assert packet <= double_sign
    orbits = cosets(n, double_sign, units)
    assert orbits[0] == double_sign
    packets = [cosets(n, packet, orbit) for orbit in orbits]
    assert packets[0][0] == packet
    initial = set(packet) | {0}
    counts = differences(n, initial)
    assert max(counts) <= 2
    stats = {"nodes_by_depth": [0]*len(orbits),
             "tested_by_depth": [0]*len(orbits),
             "rejected_by_depth": [0]*len(orbits)}
    # Testing every candidate against the initial normalized packet gives a
    # particularly compact complete certificate when there are two orbits.
    first_rejections = []
    candidates = []
    for oi in range(1, len(orbits)):
        good = []
        for pi, part in enumerate(packets[oi]):
            ds = differences(n, initial | set(part))
            bad = next((d for d in range(1,n) if ds[d] > 2), None)
            if bad is None:
                good.append(pi)
            else:
                first_rejections.append({
                    "orbit_index": oi, "packet_index": pi,
                    "representative": min(part), "difference": bad,
                    "ordered_pairs": [[a,b] for a in sorted(initial | set(part))
                                      for b in sorted(initial | set(part))
                                      if (a-b) % n == bad]})
        candidates.append(good)

    def dfs(oi, selected, values, ds):
        stats["nodes_by_depth"][oi-1] += 1
        if oi == len(orbits):
            return selected, sorted(values), ds
        for pi in candidates[oi-1]:
            stats["tested_by_depth"][oi] += 1
            part = packets[oi][pi]
            inc = [0]*n
            for a in part:
                for b in values:
                    inc[(a-b) % n] += 1
                    inc[(b-a) % n] += 1
                for b in part:
                    if a != b:
                        inc[(a-b) % n] += 1
            if any(ds[d] + inc[d] > 2 for d in range(1,n)):
                stats["rejected_by_depth"][oi] += 1
                continue
            next_ds = [ds[d]+inc[d] for d in range(n)]
            ans = dfs(oi+1, selected+[pi], values | set(part), next_ds)
            if ans is not None:
                return ans
        return None

    ans = dfs(1, [0], initial, counts)
    result = {
        "n": n, "doubling_order": len(double),
        "doubling_sign_order": len(double_sign),
        "packet_size": len(packet), "doubling_sign_orbit_count": len(orbits),
        "packets_per_doubling_sign_orbit": [len(row) for row in packets],
        "normalized_first_packet": sorted(packet),
        "initially_compatible_packet_indices": candidates,
        "first_pair_rejections": first_rejections,
        "stats": stats,
        "excluded_by_union_test": ans is None,
    }
    if ans is not None:
        selected, values, ds = ans
        # Independently recompute the full final set, not the incremental array.
        assert ds == differences(n, values)
        assert len(values) == 1+len(orbits)*len(packet)
        assert max(ds) <= 2
        result["compatible_selected_indices"] = selected
        result["compatible_set"] = values
        result["compatible_max_difference_multiplicity"] = max(ds)
    return result


def main():
    results = [solve(n) for n in [191,229,457,1257]]
    payload = {
        "status": "exact finite necessary-condition tests complete",
        "scope": "Only impossibility of a full required packet union excludes a conductor; a compatible set does not assert a theta configuration or a cyclic-cover witness.",
        "results": results,
    }
    out = Path(__file__).with_name("primitive_packet_sidon_output.json")
    out.write_text(json.dumps(payload, indent=2)+"\n")
    for r in results:
        print(json.dumps({k:r[k] for k in ["n","doubling_sign_orbit_count","packet_size","excluded_by_union_test","stats"]}))


if __name__ == "__main__":
    main()
