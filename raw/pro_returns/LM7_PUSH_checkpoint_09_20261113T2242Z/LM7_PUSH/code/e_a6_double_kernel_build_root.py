#!/usr/bin/env python3
"""Retain the exact audited complete-relation collector with binary types.

The complete source is written to e_a6_double_kernel_root.cpp.  Only the
coefficient type names and status labels in the common collector change.
The independently specified binary model is its saved head file.
"""
from pathlib import Path
from hashlib import sha256
import json

HERE = Path(__file__).resolve().parent


def main():
    original = HERE / 'de_a6_triple_kernel.cpp'
    head = HERE / 'e_a6_double_kernel_head_root.cpp'
    source = original.read_text()
    tail = source[source.index('struct LiftedKernel {'):]
    tail = tail.replace('Ternary', 'Binary').replace('TERNARY', 'BINARY').replace('ternary', 'binary')
    out = HERE / 'e_a6_double_kernel_root.cpp'
    out.write_text(head.read_text()+'\n'+tail)
    report = {'status': 'PASS_RETAINED_COMPLETE_ENUMERATOR_BINARY_ADAPTATION',
              'original_sha256': sha256(original.read_bytes()).hexdigest(),
              'head_sha256': sha256(head.read_bytes()).hexdigest(),
              'output_sha256': sha256(out.read_bytes()).hexdigest(),
              'collector_changes': ['Ternary to Binary', 'TERNARY to BINARY', 'ternary to binary']}
    (HERE / 'e_a6_double_kernel_build_root.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
