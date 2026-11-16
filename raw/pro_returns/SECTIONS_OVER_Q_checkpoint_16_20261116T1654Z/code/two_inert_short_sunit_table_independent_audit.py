"""Read the A165 literal block tables independently of their renderer."""
from pathlib import Path
from fractions import Fraction as Q
import json
import re
import sys

sys.set_int_max_str_digits(0)
base = Path(__file__).resolve().parent
source = (base.parent / "sections/two_inert_short_sunit_coefficients.tex").read_text()
data = json.loads((base / "two_inert_short_sunit_principal_certificate_data.json").read_text())
B = 10**40
d = data["d"]
labels = {"6": r"\sigma_{11}", "7": r"\sigma_{\Sigma}", "8": r"\sigma_{59}"}
count = 0
messages = []
for key, label in labels.items():
    fragment = source.split("Generator $" + label + "$")[1].split(r"\end{longtable}")[0]
    blocks, signs = {}, {}
    for i, k, sign, first, second in re.findall(
        r"^([0-8])\s*&\s*(\d+)\s*&\s*([+-])\s*&\s*(\d+)\s*&\s*(\d+)",
        fragment, re.M
    ):
        i, k = int(i), int(k)
        sign = 1 if sign == "+" else -1
        assert i not in signs or signs[i] == sign
        signs[i] = sign
        for index, value in ((k, first), (k + 1, second)):
            assert (i, index) not in blocks
            blocks[i, index] = int(value)
            assert 0 <= int(value) < B
        count += 1
    for i, expected in enumerate(data["generators"][key]["coefficients"]):
        integer = signs[i] * sum(value * B**k for (j, k), value in blocks.items() if j == i)
        assert Q(integer, d**(2 * i // 3)) == Q(expected)
        assert (Q(expected) * d**(2 * i // 3)).denominator == 1
    messages.append(f"PASS: all nine literal integral-basis coordinates of {label}.")
assert count == 558
messages.append("PASS: 558 two-block rows and 27 exact rational coefficients; no renderer imported.")
output = "\n".join(messages) + "\n"
(base / "two_inert_short_sunit_table_independent_audit_output.txt").write_text(output)
print(output, end="")
