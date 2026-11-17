"""Conditional free-word checks for the frozen alternatives on scan 085.

This is a research calculation, not a handwriting decision or a transcription edit.
Generators are lambda_0,...,lambda_(nu-1); lambda_nu is their inverse product.
No external algebra package is used.  Output records the actual reduced words.
"""
from pathlib import Path
import json


def reduce_word(word):
    out = []
    for a in word:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def mul(*words):
    return reduce_word(a for word in words for a in word)


def inv(word):
    return tuple(-a for a in word[::-1])


def subst(word, images):
    return mul(*(images[abs(a)-1] if a > 0 else inv(images[-a-1]) for a in word))


def display(word):
    return "1" if not word else " ".join(f"lambda_{abs(a)-1}" + ("^-1" if a < 0 else "") for a in word)


rows = []
for nu in range(2, 9):
    lam = [(i+1,) for i in range(nu)]
    lam.append(inv(mul(*lam)))
    for lower in [0, 1]:
        q = {j: mul(*lam[lower:j]) for j in range(2, nu+1)}
        proposed = [lam[0]] + [mul(q[j], lam[j], inv(q[j])) for j in range(nu, 1, -1)] + [lam[1]]
        relator_image = mul(*proposed)
        row = {"nu": nu, "lower_index": lower, "product_of_proposed_images": display(relator_image)}
        if lower == 0:
            expected = mul(lam[0], inv(lam[1]), inv(lam[0]), lam[1])
            assert relator_image == expected and relator_image
            row["matches_Hua_conditional_obstruction"] = True
        else:
            assert not relator_image
            images = proposed[:nu]
            assert subst(lam[nu], images) == proposed[nu]
            squared = [subst(im, images) for im in images]
            inner = [mul(inv(lam[0]), w, lam[0]) for w in lam[:nu]]
            assert squared == inner
            row["square_images"] = [display(w) for w in squared]
            row["square_is_inner_conjugation_by_lambda_0_inverse"] = True
        rows.append(row)

result = {
    "purpose": "Conditional algebra only; frozen q_i lower index remains unsure{0|1}.",
    "scope": "Direct finite free-word checks for ranks 2 through 8; not a general proof or proof of the profinite/continuous assertion.",
    "rows": rows,
}
path = Path(__file__).with_name("reversal_word_check.json")
path.write_text(json.dumps(result, indent=2) + "\n")
print(f"Wrote {path.name}: {len(rows)} conditional cases passed.")
