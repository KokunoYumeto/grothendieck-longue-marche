"""Read the literal A159 TeX blocks, independently of their renderer."""
from pathlib import Path
from fractions import Fraction
import json
import re
import sys

sys.set_int_max_str_digits(0)
base = Path(__file__).resolve().parent
source = (base.parent / "sections/two_inert_unit_coefficients_supplement.tex").read_text()
data = json.loads((base / "two_inert_relative_unit_repair_certificate_data.json").read_text())
radical = data["d"]
block_base = 10**40
row_count = 0
coefficient_count = 0
messages = []

for unit in data["units"][1:]:
    unit_index = unit["index"]
    marker = "Unit $u_" + str(unit_index) + "$"
    part = source.split(marker)[1].split(r"\end{longtable}")[0]
    blocks, signs = {}, {}
    pattern = r"^([0-8])\s*&\s*(\d+)\s*&\s*([+-])\s*&\s*(\d+)\s*&\s*(\d+)"
    for i, k, sign, first, second in re.findall(pattern, part, re.M):
        i, k = int(i), int(k)
        sign = 1 if sign == "+" else -1
        assert i not in signs or signs[i] == sign
        signs[i] = sign
        for index, value in ((k, first), (k + 1, second)):
            assert (i, index) not in blocks
            blocks[i, index] = int(value)
            assert 0 <= int(value) < block_base
        row_count += 1
    for i, expected in enumerate(unit["candidate"]):
        integer = signs[i] * sum(
            value * block_base**k
            for (j, k), value in blocks.items()
            if j == i
        )
        reconstructed = Fraction(integer, radical ** (2 * i // 3))
        assert reconstructed == Fraction(expected), (unit_index, i)
        coefficient_count += 1
    messages.append(
        f"PASS: TeX table reconstructs all nine exact rational coordinates of unit {unit_index}."
    )

assert coefficient_count == 27
messages.append(
    f"PASS: {row_count} literal two-block rows, {coefficient_count} exact coefficients; no renderer imported."
)
output = "\n".join(messages) + "\n"
(base / "two_inert_unit_table_independent_audit_output.txt").write_text(output)
print(output, end="")
