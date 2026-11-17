#!/usr/bin/env python3
"""Apply the post-freeze research citation audit; never touches transcription."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
path = root / 'MPL_12_002-050_notes.md'
text = path.read_text(encoding='utf-8')

# These remove word-level register parallels that do not substantively bear
# on the local assertion. Context locators in the final notes remain explicit.
rs = {
    6: 'no direct RS entry settles this twist-sign reading.',
    8: 'WG2 §2.4 #3 is the broader singular-hypersurface plan; no direct settled coniveau identification.',
    10: 'no direct settled entry for this cancelled assertion.',
    12: 'WG2 §2.4 #3; MPL_15_087-138 §2 and L01; the context README B9 supplies the relative-motives planning link.',
    14: 'MPL_15_087-138 T26 is only a comparison-torsor/period evidence lead, not a base-point identification theorem.',
    16: 'no direct settled entry for the association datum.',
    19: 'no direct settled descent theorem in RS; the context README B9 identifies the general relative programme.',
    23: 'no direct settled entry for this rational central Frobenius assertion.',
    28: 'no direct settled entry for the construction of this filtration-splitting torsor.',
    33: 'MPL_14_002-044 M01 (existing-category/effectivity lead); MPL_15_195-228+18_002-017 S15 (bounded modern-category comparison); context README B9 (relative-motives plan).',
    34: 'no direct settled entry; context README B9 is the relevant planning reference.',
    35: 'no direct settled entry; context README B9 is the relative six-operation planning reference.',
    36: 'no direct settled continuity result; context README B9 gives the broader programme.',
    38: 'MPL_15_195-228+18_002-017 S15 is a bounded modern realization/construction comparison; no general lifting theorem is supplied.',
    39: 'no direct settled entry for this consistency safeguard.',
    40: 'no direct settled entry for this cancelled realization.',
    41: 'no direct settled Tate-object construction in RS.',
    42: 'no direct settled top-degree trace entry; context README B9 supplies the general programme.',
    43: 'no direct settled purity result in RS.',
    44: 'no direct settled localization or sign-resolution entry.',
    45: 'no direct settled construction of these relative operations; context README B9 is the planning link.',
    46: 'no direct settled lissité-independence result in RS.',
    47: 'WG2 §2.3 #7 and MPL_15_087-138 §2 are broader semisimplicity/construction leads, not registered proofs of rational traces.',
    48: 'WG2 §2.3 #7 and MPL_15_087-138 §2 are broader semisimplicity/construction leads; the direct conditional calculation is CN S11.',
    49: 'no direct settled fibrewise Frobenius criterion in RS.',
    50: 'no direct settled relative weight bound in RS.',
    51: 'WG2 §2.4 #3 is only the broader singular-hypersurface planning question; no settled generation assertion is supplied.',
    52: 'no direct settled extension-of-weights result in RS.',
    53: 'no direct settled entry for this strict-inclusion assertion.',
    54: 'no direct RS entry resolves this local parity/subscript issue.',
    55: 'no direct settled identification of these two notions of level.',
    56: 'no direct settled direct-image bound in RS.',
    57: 'no direct settled internal-Ext bound in RS.',
    58: 'no direct settled Ext-vanishing result; LM7 C.5 is only a scope comparison, since its torsion extension splits up to isogeny and is not a nonzero rational-motivic Ext witness.',
    59: 'no direct settled result about this particular finite-length Grothendieck group.',
    60: 'no direct settled non-zero-divisor result for this ring in RS.',
    61: 'no direct settled product-purity rule for this constant-twisted ring in RS.',
    62: 'no direct RS entry resolves this local degree/Laurent convention.',
    63: 'no direct RS entry resolves the written lower bound.',
    64: 'no direct settled entry for this primitive-class multiplication data.',
    65: 'no direct settled classification of these primitive sets in RS.',
    67: 'MPL_11_043-058+56 N031 is an idempotent-splitting lead only, not a construction of these lambda operations.',
    68: 'WG2 §2.4 #3 motivates keeping the Lefschetz and categorical gradings separate, as in N026; no local notation table is supplied.',
    69: 'no direct settled motivic coniveau spectral sequence in RS.',
    70: 'no direct RS entry resolves the conflicting hypothesis and index readings.',
    71: 'no direct settled implication corresponding to the cancelled paragraph.',
    72: 'no direct settled scissors-measure construction in RS; context README B9 supplies only the formalism agenda.',
    73: 'no direct settled virtual-Betti entry in RS.',
    75: 'no direct settled entry about this revised filtration.',
    76: 'no direct settled normalization result in RS.',
}
context = {
    28: "H7 **adds** a modern parabolic/unipotent construction to the manuscript's deferred task; the particular Fermat weight-splitting statements elsewhere in RS do not identify this torsor with all arithmetic splittings.",
    35: 'H9/H10 **restate** the requested additional operations; the supplied older correspondence text gives no construction in this relative generality.',
    41: 'H10 **restates and regularizes** the construction; the explicit earlier projective-line anchor is T12 12/002.',
    42: 'H10 **recasts** the top-degree trace statement in modern notation; CT 16/048–049 concerns a different inverse-correspondence argument, used concretely in N047–N048.',
    45: 'H10 **restates and explains** the formalism; the supplied CT material does not construct these general relative operations.',
    51: 'H12 **reconstructs** the programme by adding an index bound and changing the subobject/subquotient wording; CT 16/047 **differs** by its separate failed smooth-hypersurface reduction.',
    56: "H13 **preserves** the dimension-type doubt but calls the weight estimate certain, unlike the frozen “!?”; H16 **adds** a different dense-open argument. Hua, modernised reading of cote 12, “Le cas d'une immersion : les feuilles de calcul (pages 115, 117 et 119)”, is an **outside-range lead**.",
    58: 'H14 **adds** the Kummer/scope objection; it must not be conflated with the specific torsion extension in LM7 C.5.',
    64: 'H14 **reconstructs** the quotient basis and **restates** the separate need for multiplicative coefficients.',
    67: 'H14 **restates** the plan and H3 **supplies** its earlier version; degree projectors in CT 16/017 are not the symmetric-group idempotents needed for this proposed construction.',
    70: 'H15 **differs** on both hypothesis and index; the singular-hypersurface programme is a separate comparison in N092.',
}

blocks = re.split(r'(?=^#### N\d{3} —)', text, flags=re.M)
changed = []
for index, block in enumerate(blocks):
    match = re.match(r'#### N(\d{3}) —', block)
    if not match:
        continue
    number = int(match.group(1))
    if number in rs:
        block, count = re.subn(r'\*\*RS:\*\* .*? (?=\*\*Search:\*\*)',
                               lambda _: '**RS:** ' + rs[number] + ' ', block, count=1)
        if count != 1:
            raise RuntimeError(f'N{number:03d}: RS field not found')
    if number in context:
        block, count = re.subn(r'\*\*Context relation:\*\* .*? (?=\*\*RS:\*\*)',
                               lambda _: '**Context relation:** ' + context[number] + ' ', block, count=1)
        if count != 1:
            raise RuntimeError(f'N{number:03d}: context field not found')
    if block != blocks[index]:
        changed.append(f'N{number:03d}')
    blocks[index] = block

path.write_text(''.join(blocks), encoding='utf-8')
print(f'Research citation audit applied to {len(changed)} notes; transcription untouched.')
