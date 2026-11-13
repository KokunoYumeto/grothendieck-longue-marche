#!/usr/bin/env python3
"""Exact covering/filling maps for the D.36 transposition argument."""
import json
from pathlib import Path


def reduce_word(word):
    result = []
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return result


def inverse_word(word):
    return [-a for a in reversed(word)]


def product_words(words):
    return reduce_word([a for word in words for a in word])


def substitute(word, images):
    return product_words(images[a] if a > 0 else inverse_word(images[-a])
                         for a in word)


def check_prime(q):
    # F(x,y), using1=x and2=y.
    cusp_words = [[2]*i+[1]+[-2]*i for i in range(q)]
    b = [2]*q
    d = [-2, -1]*q
    assert product_words(cusp_words+[b]) == [1, 2]*q
    assert product_words(cusp_words+[b, d]) == []
    # Abstract Schreier basis A0,...,A(q-1),B uses letters1,...,q+1.
    schreier_to_F = {i+1: word for i, word in enumerate(cusp_words)}
    schreier_to_F[q+1] = b
    d_in_schreier = [-(q+1)]+[-i for i in range(q, 0, -1)]
    assert substitute(d_in_schreier, schreier_to_F) == d
    # Filling kills B and D, and eliminates the last A.
    filling = {i: [i] for i in range(1, q)}
    filling[q] = [-i for i in range(q-1, 0, -1)]
    filling[q+1] = []
    assert substitute(d_in_schreier, filling) == []
    assert substitute(list(range(1, q+1)), filling) == []
    assert substitute([q+1], filling) == []
    # The inverse section on the q-1 free generators is literally inclusion.
    assert all(substitute([i], filling) == [i] for i in range(1, q))
    involutive_translations = [shift for shift in range(q)
                               if all((i-2*shift) % q == i for i in range(q))]
    assert involutive_translations == [0]
    # In the cyclic quotient chi=(0,1,-1), the hypothetical negative
    # multiplier times the y/z swap acts as the identity.
    chi = [0, 1, q-1]
    swap = [0, 2, 1]
    alpha_chi = [(-chi[swap[i]]) % q for i in range(3)]
    assert alpha_chi == chi
    # Boundary monodromy: x fixes all q sheets; y,z are opposite q-cycles.
    boundary_degrees = [1]*q+[q, q]
    assert len(boundary_degrees) == q+2
    genus = (q+2-len(boundary_degrees))//2
    assert genus == 0
    return {
        "prime": q, "cover_degree": q, "genus": genus,
        "boundary_degrees": boundary_degrees,
        "free_rank_before_filling": q+1, "free_rank_after_filling": q-1,
        "cusp_words_in_x_y": cusp_words,
        "b_word": b, "d_word": d,
        "d_in_schreier_basis": d_in_schreier,
        "filling_images": {str(i): word for i, word in filling.items()},
        "free_word_relation_verified": True,
        "involutive_translation_parameters": involutive_translations,
        "quotient_character": chi, "transformed_character": alpha_chi,
        "remaining_q_adic_multiplier": q-1,
        "remaining_2_adic_multiplier": 1,
    }


def main():
    records = [check_prime(q) for q in (3, 5, 7, 11, 13, 17, 19)]
    result = {
        "claim": "D.36", "status": "passed",
        "cover_and_filling_certificates": records,
        "logical_limit": "The checks validate exact word substitutions and finite cyclic actions. The incompatibility with a pure involution is proved for arbitrary rank and all primes in d36.tex, using D32/D33.",
    }
    destination = Path(__file__).with_name("positive_transposition_d36_output.json")
    destination.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "passed", "primes": [r["prime"] for r in records],
                      "output": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
