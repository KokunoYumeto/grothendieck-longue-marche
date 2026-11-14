#!/usr/bin/env python3
"""Derive and retain the exact binary query collector from read source."""
from pathlib import Path
from hashlib import sha256
import json

HERE = Path(__file__).resolve().parent


def main():
    central_path = HERE / 'e_a6_double_central_root.cpp'
    template_path = HERE / 'de_a6_triple_query.cpp'
    central = central_path.read_text()
    core = central[:central.index('int main(int argc')]
    (HERE / 'e_a6_double_query_core_root.hpp').write_text(core)
    text = template_path.read_text()
    changes = [
        ('de_a6_triple_query_core.hpp', 'e_a6_double_query_core_root.hpp', 1),
        ('0xA63C0033', '0xA62C0032', 1),
        ('79', '128', 3),
        ('TernarySpan', 'BinarySpan', 2),
        ('%3', '%2', 1),
    ]
    for old, new, count in changes:
        assert text.count(old) == count, (old, text.count(old), count)
        text = text.replace(old, new)
    target = HERE / 'e_a6_double_query_root.cpp'
    target.write_text(text)
    out = {'status': 'PASS_EXACT_BINARY_QUERY_COLLECTOR_DERIVATION',
           'central_source_sha256': sha256(central_path.read_bytes()).hexdigest(),
           'query_template_sha256': sha256(template_path.read_bytes()).hexdigest(),
           'new_query_sha256': sha256(target.read_bytes()).hexdigest(),
           'core_is_exact_entire_central_source_before_main': True,
           'substitutions': changes}
    (HERE / 'e_a6_double_query_build_root.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
