"""Finite-prefix checks for two explicit compact shift examples.

These are examples about the logical strength of surjectivity and character
independence; they are not claimed to be images or models of actual GT.
The complete proof for the infinite product is in the companion audit note.
"""
from itertools import product
import json
from pathlib import Path

records = []
for n in range(1, 10):
    words = list(product((0, 1), repeat=n + 1))
    for kind in (0, 1):
        outputs = {(a[1:], a[0] if kind == 0 else a[0] ^ a[1])
                   for a in words}
        assert len(outputs) == 2 ** (n + 1)
        fixed_bits = {(v if kind == 0 else v ^ v) for v in (0, 1)}
        assert fixed_bits == ({0, 1} if kind == 0 else {0})
        # Characters chi_j use x_j, respectively x_j+x_(j+1).
        character_rows = [(1 << j) if kind == 0
                          else (1 << j) | (1 << (j + 1))
                          for j in range(n)]
        pivots = {}
        for row in character_rows:
            while row:
                lead = row.bit_length() - 1
                if lead not in pivots:
                    pivots[lead] = row
                    break
                row ^= pivots[lead]
        assert len(pivots) == n
        records.append(dict(prefix=n, character="x0" if kind == 0 else "x0+x1",
                            joint_image_size=len(outputs), character_rank=n,
                            fixed_parities=sorted(fixed_bits)))

output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(records, indent=2) + "\n")
for row in records:
    print(row)
print("ALL FINITE PREFIX CHECKS PASSED; infinite assertions proved by coordinates.")
