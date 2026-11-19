#!/usr/bin/env python3
"""Focused n=4 enumeration and exact proposed-component-partition check only.

Uses the independently written finite-set definitions in finite_figures_check.
No scans, witnesses, context, sweep implementation, or research notes are read.
No refinement pairs, transitivity tests, or other conjecture tests are run.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from finite_figures_check import Family, family_id, lower_subfamily, points, utc_now


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1]/'records/finite_figures_n4_components.json')
    args = parser.parse_args()
    started = utc_now()
    n = 4
    ground = (1 << n) - 1
    counts = {
        'all_families': 1 << (1 << n),
        'preadmissible_families': 0,
        'admissible_families': 0,
        'full_L_support_admissible_families': 0,
    }
    multistrates = []
    for ident in range(counts['all_families']):
        f = Family(n, ident)
        counts['preadmissible_families'] += int(f.preadmissible)
        counts['admissible_families'] += int(f.admissible)
        counts['full_L_support_admissible_families'] += int(f.admissible and f.support == ground)
        if f.multistrate:
            multistrates.append(f)
    ids = {f.id for f in multistrates}
    adjacency = {ident: set() for ident in ids}
    for i, f in enumerate(multistrates):
        for g in multistrates[i + 1:]:
            if lower_subfamily(f, g) or lower_subfamily(g, f):
                adjacency[f.id].add(g.id)
                adjacency[g.id].add(f.id)
    unseen = set(ids)
    components = []
    while unseen:
        pending = [min(unseen)]
        component = set()
        while pending:
            a = pending.pop()
            if a not in component:
                component.add(a)
                pending.extend(adjacency[a] - component)
        unseen -= component
        components.append(sorted(component))

    exceptional = [
        {'subset': a, 'subset_points': points(a, n), 'members': sorted([family_id([a]), family_id([a, ground])])}
        for a in range(1 << n) if a.bit_count() == n - 1
    ]
    isolated = family_id([ground])
    other_ids = ids - {isolated} - {ident for item in exceptional for ident in item['members']}
    predicted = [sorted(other_ids)] + [item['members'] for item in exceptional] + [[isolated]]
    actual_partition = {frozenset(c) for c in components}
    predicted_partition = {frozenset(c) for c in predicted}
    counts.update(
        nonempty_admissible_families=counts['admissible_families']-1,
        multistrates=len(multistrates),
        multistrate_comparability_components=len(components),
        component_sizes=[len(c) for c in components],
    )
    result = {
        'n': n,
        'executed_started_utc': started,
        'executed_finished_utc': utc_now(),
        'scope': 'Only n=4 family classification, multistrate comparability components, and exact comparison with the stated proposed partition.',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'definitions_script_sha256': hashlib.sha256((Path(__file__).parent/'finite_figures_check.py').read_bytes()).hexdigest(),
        'encoding': {
            'subset': 'Integer bitmask; bit i means point i.',
            'family_id': 'Integer bitmask on subset masks: bit a means subset a is a member.',
            'comparability': 'An undirected edge joins distinct multistrates F,G exactly when F<=G or G<=F.',
        },
        'counts': counts,
        'multistrate_catalogue': [{'id':f.id, 'members':list(f.members)} for f in multistrates],
        'actual_components': components,
        'predicted_partition': {
            'large_remaining_component': sorted(other_ids),
            'exceptional_two_node_components': exceptional,
            'isolated_greatest_singleton_family': isolated,
            'predicted_component_count': n+2,
        },
        'exact_predicted_partition_matches': actual_partition == predicted_partition,
        'predicted_components_missing_from_actual': [sorted(c) for c in sorted(predicted_partition-actual_partition,key=lambda c:min(c))],
        'actual_components_not_in_prediction': [sorted(c) for c in sorted(actual_partition-predicted_partition,key=lambda c:min(c))],
        'qualification': 'An exhaustive check for n=4, not a proof of the prediction for every finite n>=3.',
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({
        'executed_started_utc':result['executed_started_utc'],
        'executed_finished_utc':result['executed_finished_utc'],
        'counts':counts,
        'exact_predicted_partition_matches':result['exact_predicted_partition_matches'],
        'exceptional_two_node_components':exceptional,
        'isolated_family_id':isolated,
        'output':str(args.output),
    },indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
