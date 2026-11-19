#!/usr/bin/env python3
"""Independent exhaustive finite-set computation from the supplied definitions.

No scans, witnesses, context, notes, or other implementation are read. The only
read is this script's own bytes, for its reproducibility hash. All families of
subsets of {0,...,n-1}, n=1,2,3, are generated from scratch.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def contained(a: int, b: int) -> bool:
    return a & ~b == 0


def union(members) -> int:
    result = 0
    for member in members:
        result |= member
    return result


def points(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if mask & (1 << i)]


def family_id(members) -> int:
    return sum(1 << member for member in set(members))


def least(candidates: tuple[int, ...]) -> int | None:
    """Least by subset inclusion, not an arbitrarily selected minimal member."""
    found = [a for a in candidates if all(contained(a, b) for b in candidates)]
    assert len(found) <= 1
    return found[0] if found else None


class Family:
    def __init__(self, n: int, ident: int):
        self.n = n
        self.id = ident
        self.members = tuple(a for a in range(1 << n) if ident & (1 << a))
        self.member_set = set(self.members)
        self.support = union(self.members)
        self.interiors = {
            a: a & ~union(b for b in self.members if b != a and contained(b, a))
            for a in self.members
        }
        self.least_at_point = {
            x: least(tuple(a for a in self.members if a & (1 << x)))
            for x in points(self.support, n)
        }
        self.preadmissible = all(a is not None for a in self.least_at_point.values())
        self.admissible = self.preadmissible and all(self.interiors.values())
        self.greatest = self.support if self.members and self.support in self.member_set else None
        self.multistrate = self.admissible and bool(self.members) and self.greatest is not None

    def serial(self) -> dict:
        return {
            'id': self.id,
            'members': list(self.members),
            'member_point_sets': [points(a, self.n) for a in self.members],
            'support': self.support,
            'support_points': points(self.support, self.n),
            'interiors': [{'member': a, 'interior': self.interiors[a]} for a in self.members],
            'least_member_at_support_points': [
                {'point': x, 'least_member': a} for x, a in self.least_at_point.items()
            ],
            'preadmissible': self.preadmissible,
            'admissible': self.admissible,
            'greatest_member': self.greatest,
            'multistrate': self.multistrate,
        }


def lower_subfamily(f: Family, g: Family) -> bool:
    if not f.member_set <= g.member_set:
        return False
    return all(
        b in f.member_set
        for a in f.members
        for b in g.members
        if contained(b, a)
    )


def refinement_a(f: Family, g: Family) -> dict:
    mapping = {
        a: least(tuple(b for b in g.members if contained(a, b)))
        for a in f.members
    }
    least_containers = all(b is not None for b in mapping.values())
    intersections = all(
        union(c for c in f.members if contained(c, a & b)) == a & b
        for a in f.members for b in g.members
    )
    return {
        'value': least_containers and intersections,
        'least_containers_exist': least_containers,
        'least_container_map': [{'from': a, 'to': b} for a, b in mapping.items()],
        'all_intersections_are_unions': intersections,
    }


def refinement_b(f: Family, g: Family) -> dict:
    mapping = {}
    for a in f.members:
        candidates = [b for b in g.members if contained(f.interiors[a], g.interiors[b])]
        # Admissibility makes the nonempty G-interiors pairwise disjoint.
        assert len(candidates) <= 1
        mapping[a] = candidates[0] if candidates else None
    exists = all(b is not None for b in mapping.values())
    increasing = None
    if exists:
        increasing = all(
            contained(mapping[a], mapping[b])
            for a in f.members for b in f.members if contained(a, b)
        )
    return {
        'value': exists and increasing is True,
        'stratum_containers_exist': exists,
        'stratum_container_map': [{'from': a, 'to': b} for a, b in mapping.items()],
        'map_is_increasing': increasing,
    }


def relation_checks(ids: list[int], relation: set[tuple[int, int]]) -> dict:
    outgoing = {a: {b for x, b in relation if x == a} for a in ids}
    reflexivity_failures = [a for a in ids if (a, a) not in relation]
    antisymmetry_failures = [
        [a, b] for a, b in sorted(relation) if a < b and (b, a) in relation
    ]
    chains = 0
    transitivity_failures = []
    for a in ids:
        for b in sorted(outgoing[a]):
            for c in sorted(outgoing[b]):
                chains += 1
                if (a, c) not in relation:
                    transitivity_failures.append([a, b, c])
    return {
        'reflexive': not reflexivity_failures,
        'reflexivity_failures': reflexivity_failures,
        'antisymmetric': not antisymmetry_failures,
        'antisymmetry_failures': antisymmetry_failures,
        'transitive': not transitivity_failures,
        'transitivity_failures': transitivity_failures,
        'ordered_pairs_in_domain': len(ids) ** 2,
        'potential_ordered_triples': len(ids) ** 3,
        'composable_chains_checked': chains,
    }


def run_n(n: int) -> dict:
    all_families = [Family(n, ident) for ident in range(1 << (1 << n))]
    admissible = [f for f in all_families if f.admissible]
    ids = [f.id for f in admissible]
    multistrates = [f for f in admissible if f.multistrate]
    pair_results = []
    leq_relation = set()
    compatibility_relation = set()
    ra_relation = set()
    rb_relation = set()
    for f in admissible:
        # Independently check the partition property used by refinement-b.
        parts = list(f.interiors.values())
        assert union(parts) == f.support
        assert all(not(a & b) for i, a in enumerate(parts) for b in parts[i + 1:])
        for g in admissible:
            u = all_families[f.id | g.id]
            leq = lower_subfamily(f, g)
            compatible = u.admissible and lower_subfamily(f, u) and lower_subfamily(g, u)
            ra = refinement_a(f, g)
            rb = refinement_b(f, g)
            pair_results.append({
                'f': f.id, 'g': g.id,
                'f_leq_g': leq,
                'union_family': u.id,
                'union_admissible': u.admissible,
                'f_leq_union': lower_subfamily(f, u),
                'g_leq_union': lower_subfamily(g, u),
                'compatible': compatible,
                'refinement_a': ra,
                'refinement_b': rb,
            })
            if leq:
                leq_relation.add((f.id, g.id))
            if compatible:
                compatibility_relation.add((f.id, g.id))
            if ra['value']:
                ra_relation.add((f.id, g.id))
            if rb['value']:
                rb_relation.add((f.id, g.id))

    multi_ids = [f.id for f in multistrates]
    adjacency = {
        a: {b for b in multi_ids if a != b and ((a, b) in leq_relation or (b, a) in leq_relation)}
        for a in multi_ids
    }
    unseen = set(multi_ids)
    components = []
    while unseen:
        start = min(unseen)
        pending = [start]
        component = set()
        while pending:
            a = pending.pop()
            if a in component:
                continue
            component.add(a)
            pending.extend(sorted(adjacency[a] - component))
        unseen -= component
        components.append(sorted(component))
    component_of = {a: index for index, component in enumerate(components) for a in component}
    different_component_pairs = [
        (a, b) for a in multi_ids for b in multi_ids if component_of[a] != component_of[b]
    ]
    incompatible_different = [p for p in different_component_pairs if p not in compatibility_relation]
    compatible_different = [p for p in different_component_pairs if p in compatibility_relation]
    incompatible_same = [
        (a, b) for a in multi_ids for b in multi_ids
        if component_of[a] == component_of[b] and (a, b) not in compatibility_relation
    ]

    maximality_results = []
    for g in admissible:
        refinements = [a for a in ids if (a, g.id) in ra_relation]
        full_support = [a for a in refinements if all_families[a].support == g.support]
        maximal = [
            a for a in refinements
            if not any(a != b and (a, b) in leq_relation for b in refinements)
        ]
        maximality_results.append({
            'target_g': g.id,
            'all_refinements_f': refinements,
            'full_support_refinements_f': full_support,
            'maximal_refinements_f_under_leq': maximal,
            'equal': set(full_support) == set(maximal),
            'full_support_not_maximal': sorted(set(full_support) - set(maximal)),
            'maximal_not_full_support': sorted(set(maximal) - set(full_support)),
        })

    counterexamples = []
    if n == 2:
        for label, f_id, g_id in [
            ('union_not_admissible', family_id([1, 3]), family_id([2, 3])),
            ('admissible_union_but_not_down_closed', family_id([3]), family_id([1])),
        ]:
            f, g = all_families[f_id], all_families[g_id]
            u = all_families[f_id | g_id]
            assert f.multistrate and g.multistrate
            assert component_of[f_id] != component_of[g_id]
            assert (f_id, g_id) not in compatibility_relation
            counterexamples.append({
                'label': label,
                'f': f.serial(), 'g': g.serial(), 'union': u.serial(),
                'f_component': component_of[f_id], 'g_component': component_of[g_id],
                'f_leq_union': lower_subfamily(f, u),
                'g_leq_union': lower_subfamily(g, u),
                'compatible': False,
            })

    summary = {
        'n': n,
        'all_families': len(all_families),
        'preadmissible_families': sum(f.preadmissible for f in all_families),
        'admissible_families': len(admissible),
        'nonempty_admissible_families': len(admissible) - 1,
        'full_L_support_admissible_families': sum(f.support == (1 << n) - 1 for f in admissible),
        'multistrates': len(multistrates),
        'multistrate_comparability_components': len(components),
        'component_sizes': [len(component) for component in components],
        'different_component_ordered_pairs': len(different_component_pairs),
        'incompatible_ordered_pairs_in_different_components': len(incompatible_different),
        'compatible_ordered_pairs_in_different_components': len(compatible_different),
        'incompatible_ordered_pairs_in_same_component': len(incompatible_same),
        'admissible_ordered_pairs_checked': len(pair_results),
        'refinement_a_pairs': len(ra_relation),
        'refinement_b_pairs': len(rb_relation),
        'refinement_a_b_disagreements': len(ra_relation ^ rb_relation),
        'full_support_maximality_target_failures': sum(not r['equal'] for r in maximality_results),
    }
    return {
        'summary': summary,
        'families': [f.serial() for f in all_families],
        'admissible_family_ids': ids,
        'multistrate_family_ids': multi_ids,
        'all_admissible_pair_results': pair_results,
        'multistrate_comparability_components': components,
        'multistrate_comparability_edges': [
            [a, b] for a in multi_ids for b in sorted(adjacency[a]) if a < b
        ],
        'incompatible_ordered_pairs_in_different_components': incompatible_different,
        'compatible_ordered_pairs_in_different_components': compatible_different,
        'incompatible_ordered_pairs_in_same_component': incompatible_same,
        'refinement_a_b_disagreement_pairs': sorted(ra_relation ^ rb_relation),
        'refinement_a_relation_checks': relation_checks(ids, ra_relation),
        'refinement_b_relation_checks': relation_checks(ids, rb_relation),
        'leq_relation_checks': relation_checks(ids, leq_relation),
        'refinement_support_inclusion_failures': [
            [a, b] for a, b in sorted(ra_relation)
            if not contained(all_families[a].support, all_families[b].support)
        ],
        'full_support_vs_maximal_refinements': maximality_results,
        'n2_counterexamples': counterexamples,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1]/'records/finite_figures_check.json')
    args = parser.parse_args()
    started = utc_now()
    runs = [run_n(n) for n in (1, 2, 3)]
    result = {
        'provenance': {
            'implementation': 'Independent exhaustive finite-set enumeration from the definitions supplied for this task; no other source implementation consulted.',
            'executed_started_utc': started,
            'executed_finished_utc': utc_now(),
            'python_version': platform.python_version(),
            'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'external_inputs_read': [],
        },
        'encoding': {
            'ground_set': 'L={0,...,n-1}',
            'subset_mask': 'Subset A is encoded by the integer sum(2**i for i in A).',
            'family_id': 'Family F is encoded by the integer sum(2**a for subset masks a in F). Bit 0 denotes the empty-set member.',
            'family_catalogue': 'Every one of the 2**(2**n) families is listed, including the empty family and families containing the empty set.',
            'pair_domain': 'All ordered pairs of admissible families; all true and false outcomes are retained.',
            'component_domain': 'Nonempty admissible families with greatest member, with undirected edges when either F<=G or G<=F.',
            'full_support_interpretation': 'For each fixed admissible G, full support means support(F)=support(G); maximality is within {admissible F : refinement_a(F,G)} under <=.',
            'finite_scope': 'Exhaustive for n=1,2,3 only. Absence of a finite counterexample is not a proof for arbitrary ground sets.',
        },
        'runs': runs,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'provenance': result['provenance'], 'summaries': [r['summary'] for r in runs], 'output':str(args.output)}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
