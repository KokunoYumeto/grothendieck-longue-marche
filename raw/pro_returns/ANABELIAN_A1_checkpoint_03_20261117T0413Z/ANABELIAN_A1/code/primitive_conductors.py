"""Exhaustive conductor and difference-packet tests for the F_(2^38) curve."""
from pathlib import Path
from math import gcd
from collections import Counter
import json

OUT = Path(__file__).with_suffix(".json")
BOUND = 10*19**3

def factors(n):
    result = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            result[d] = result.get(d, 0)+1
            n //= d
        d += 1
    if n > 1:
        result[n] = result.get(n, 0)+1
    return result

def phi(n):
    ans = n
    for p in factors(n):
        ans = ans//p*(p-1)
    return ans

def order2(n):
    o = phi(n)
    for p in factors(o):
        while o % p == 0 and pow(2,o//p,n) == 1:
            o //= p
    assert pow(2,o,n) == 1
    return o

def subgroup(n, generators):
    found = {1}
    queue = [1]
    for x in queue:
        for g in generators:
            y = x*g % n
            if y not in found:
                found.add(y)
                queue.append(y)
    return found

def diffs(S,n):
    return Counter((a-b)%n for a in S for b in S if a != b)

records = []
survive = []
for n in range(3,BOUND,2):
    ph = phi(n)
    o = order2(n)
    d = gcd(o,19)
    M = ph//d
    if M*(M+1) > 2*(n-1):
        continue
    H = subgroup(n, [pow(2,19,n),n-1])
    S = {0}|H
    counts = diffs(S,n)
    worst = max(counts.values())
    bad = min((x for x in counts if counts[x] > 2),default=None)
    row = {"n":n,"factorization":factors(n),"phi":ph,"ord2":o,
           "gcd_ord_19":d,"minimum_primitive_points":M,
           "H":sorted(H),"max_difference_multiplicity":worst,
           "bad_difference":bad}
    if bad is not None:
        row["bad_pairs"] = [[a,b] for a in sorted(S) for b in sorted(S)
                            if (a-b)%n == bad]
    else:
        survive.append(n)
    records.append(row)

assert [x["n"] for x in records] == [
    191,229,361,419,457,571,573,647,687,955,1083,1257,1371]
assert survive == [191,229,457,1257]
print("Bound:",BOUND)
print("Conductor candidates:",[x["n"] for x in records])
print("Survivors of single-packet test:",survive)

# For 457, normalize one chosen primitive theta point to residue 1.
n = 457
H = subgroup(n,[pow(2,19,n),n-1])
U = subgroup(n,[2,n-1])
remaining = set(range(1,n))
cosets = []
while remaining:
    a = min(remaining)
    c = {(a*u)%n for u in U}
    cosets.append(sorted(c))
    remaining -= c
assert len(cosets) == 6 and 1 in cosets[0]

packet_groups = []
for c in cosets[1:]:
    remaining = set(c)
    packets = []
    while remaining:
        a = min(remaining)
        packet = {(a*h)%n for h in H}
        packets.append(sorted(packet))
        remaining -= packet
    assert len(packets) == 19
    packet_groups.append(packets)

start = {0}|H
base_counts = diffs(start,n)
candidate_counts = []
filtered = []
for packets in packet_groups:
    good = [p for p in packets if max(diffs(start|set(p),n).values()) <= 2]
    candidate_counts.append(len(good))
    filtered.append(good)

levels = [1,0,0,0,0,0]
complete = []
def dfs(depth,S,counts,chosen):
    if depth == 5:
        complete.append(chosen)
        return
    for packet in filtered[depth]:
        P = set(packet)
        new = Counter((a-b)%n for a in P for b in P if a!=b)
        new.update((a-b)%n for a in P for b in S)
        new.update((a-b)%n for a in S for b in P)
        if any(counts[d]+v>2 for d,v in new.items()):
            continue
        levels[depth+1] += 1
        dfs(depth+1,S|P,counts+new,chosen+[packet])
dfs(0,start,base_counts,[sorted(H)])
assert not complete
print("457 first-filter candidate counts:",candidate_counts)
print("457 surviving depths:",levels)

# For 1257, two packets are necessary; count differences divisible by 3.
H1257=subgroup(1257,[pow(2,19,1257),1257-1])
U1257=subgroup(1257,[2,1257-1])
assert len(H1257)==22 and len(U1257)==418 and phi(1257)==836
packet_occupancies=Counter(h%3 for h in H1257)
assert packet_occupancies == {1:11,2:11}
forced = 2*22*21
permitted = 2*(1257//3-1)
assert forced>permitted
print("1257 forced/permitted differences:",forced,permitted)
record={"bound":BOUND,"scalar_exponent":19,"records":records,
        "single_packet_survivors":survive,
        "457":{"H":sorted(H),"U":sorted(U),"U_cosets":cosets,
               "H_packets":packet_groups,"filtered_counts":candidate_counts,
               "surviving_partial_sets":levels,"full_solutions":complete},
        "1257":{"H_order":22,"U_order":418,"phi":836,
                "packet_occupancies":dict(packet_occupancies),
                "forced_differences":forced,"permitted_differences":permitted},
        "remaining_conductors":[191,229]}
OUT.write_text(json.dumps(record,indent=2)+"\n")
print("Exhaustive reduction to {191,229}: PASS")
