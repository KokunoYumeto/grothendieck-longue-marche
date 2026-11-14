# Complete finite-action catalogue index for 2g + ν ≤ 6

This index joins the proved catalogues in B.26–B.29, B.33, B.36–B.41. It contains all 16 surface types, with **882 conjugacy classes of finite mapping-class subgroups** and **889 injective realization classes**. The seven extra realization rows are the explicitly classified fibers of the mapping-class projection in the four exceptional types. The source proofs, exact finite models, and section posets remain in their original files.

## Files and counts

All paths in the CSV and JSON files are relative to the root of the deliverable ZIP.

| File under `code/part_b/` | Content |
|---|---|
| `low_complexity_catalogue_index.csv` | One row for each of the 16 surface types, with counts and all source-data paths. |
| `low_complexity_all_realizations.csv` | 889 action rows, including the actual realization-to-mapping-class map and exact section-record routes. |
| `low_complexity_mapping_class_subgroups.csv` | 882 subgroup rows; each row lists every realization in its fiber and the sets of section counts occurring there. |
| `type_3_0_master_catalogue.csv` | The 292 genus-three rows of the all-types index, with the same schema. |
| `low_complexity_catalogue_routes.json` | Machine-readable record of every detailed-data route. |
| `type_3_0_positive_class_routing.json` | Exact routing through the colored-braid orbits for the five source signature pairs containing several positive action classes. |
| `low_complexity_catalogue_validation.json` | Executed counts, route checks, independent genus-three comparison, and SHA-256 hashes of every input. |
| `low_complexity_packaged_layout_validation.json` | Independent execution from a fresh ZIP-layout directory, with byte-for-byte comparison of all eight generated outputs. |
| `low_complexity_catalogue_required_paths.json` | Exact input paths needed to rerun the assembler and all output filenames. |
| `assemble_low_complexity_catalogues.py` | Reproducible assembler and validator; Python standard library plus the included root census module. |

| Surface type (g,ν) | Mapping-class subgroup classes | Injective realization classes | Proof |
|---|---:|---:|---|
| (0,0) | 2 | 3 | B.36 |
| (0,1) | 2 | 2 | B.36 |
| (0,2) | 5 | 7 | B.36 |
| (0,3) | 10 | 10 | B.26 |
| (0,4) | 30 | 30 | B.26 |
| (0,5) | 20 | 20 | B.26 |
| (0,6) | 57 | 57 | B.26 |
| (1,0) | 13 | 17 | B.36 |
| (1,1) | 13 | 13 | B.27 |
| (1,2) | 40 | 40 | B.27 |
| (1,3) | 38 | 38 | B.27 |
| (1,4) | 115 | 115 | B.27 |
| (2,0) | 92 | 92 | B.28 |
| (2,1) | 32 | 32 | B.29 |
| (2,2) | 121 | 121 | B.29 |
| (3,0) | 292 | 292 | B.33, B.37–B.41 |
| **Total** | **882** | **889** | |

## The realization map

For an action represented by a finite subgroup `Γ ≤ Homeo(U)`, the map used here is the restriction of the component projection

`ρ: Homeo(U) → π₀ Homeo(U)`, `Γ ↦ ρ(Γ)`.

The exceptional rows classify the actions for which `ρ|Γ` is an isomorphism onto the represented finite mapping-class subgroup. B.36 proves this comparison and gives every fiber. The remaining finite actions with a kernel in this projection are the families classified in B.14.

`realization_id → mapping_class_subgroup_id` is the actual forgetful map in the tables. The latter identifier is formed from the source's explicitly classified subgroup identifier; it is never reconstructed by comparing numerical invariants. Every hyperbolic row has a singleton fiber by the action-realization comparison proved in Part B. In the exceptional types there are 29 realization rows over 22 subgroup rows.

For example, `g0n0:sphere_reflection` and `g0n0:sphere_antipodal` both map to `g0n0:C2_negative`. Their lift extensions are both `C₂`, since `π₁(S²)=1`, and each has one algebraic full section. Their fixed loci have one and zero components, respectively. The antipodal section has no fixed-point local multiplier. Its record retains the undefined local entry and the separate formal orientation-half value. No section or multiplier is transferred between these two realizations by the table join.

The subgroup table records each fiber as a JSON array in `realization_ids`. Its columns ending in `_counts_in_fiber` are JSON arrays of the distinct integer counts occurring in that fiber. They preserve variation in the data attached to a single mapping-class subgroup.

## Main row schema

The two realization CSVs use the same schema. Counts and orders are decimal integers. Identifiers, source paths, and pointers are strings. An empty string in a routing field means that this additional route is not used for that row.

| Column | Meaning |
|---|---|
| `realization_id` | Globally unique identifier `g{g}n{ν}:{source_row_id}`. |
| `mapping_class_subgroup_id` | Target of the exact component projection described above. |
| `surface_type`, `genus`, `punctures` | The surface type, also retained as separate integer coordinates. |
| `source_claim` | Number of the mathematical claim proving that source block. |
| `source_row_id` | Original, unchanged identifier in the source CSV and detailed JSON. |
| `source_positive_signature_pair_id` | Genus-three primary census group/signature pair, such as `O3.9`; empty for other genera. |
| `positive_class_realization_id` | Exact genus-three positive action class, such as `g3n0:G3N0-O9-2`. |
| `positive_section_json`, `positive_section_pointer` | Exact detailed record of that positive action. |
| `classification_certificate_json`, `classification_certificate_pointer` | Source monodromy/orbit certificate for B.37, B.39, or B.40. |
| `quotient_surface` | Source quotient-surface description when supplied by this index; empty entries retain the description in the source record. |
| `group_order`, `positive_subgroup_order` | Orders of `Γ` and its orientation-preserving subgroup. Equality identifies positive actions. |
| `full_splitting_classes` | Number of full sections of the lift extension, modulo conjugation by the surface group. |
| `nontrivial_partial_splitting_classes` | Number of section classes over all nontrivial subgroups of `Γ`. This includes full sections when `Γ` is nontrivial. |
| `maximal_partial_classes_Phi` | Number of maximal elements in the poset of nontrivial partial section classes. |
| `Gamma_orbits_on_Phi` | Number of orbits for the specified `Γ` action on `Φ`. |
| `oval_section_classes`, `line_section_classes` | Numbers of section records whose actual fixed component is a circle or line. All subgroup levels are counted. |
| `actual_fixed_components` | Number of connected components of the global fixed locus. The sphere antipodal row explicitly has zero, independently of its one algebraic section. |
| `source_table` | Exact source CSV. |
| `section_json`, `section_pointer` | Exact detailed section record. |
| `shared_data_json`, `shared_data_pointer` | Shared affine or hyperelliptic finite model used by the section record. |

For the nonaspherical sphere and plane rows, `geometric_fixed_component_kind` supplies the circle/line labels for the scalar columns. The detailed record keeps the section kind `algebraic section`, its actual geometric locus, and its centralizer separately. A circle in the sphere has trivial image in `π₁(S²)`, as B.36 proves; the index preserves its centralizer `1`.

The trivial subgroup has one full section and contributes no nontrivial partial section or element of `Φ`. The two section counts therefore answer different explicit counting questions. The assembler verifies both against the detailed records.

## Exact detailed-data routing

Pointers use RFC 6901 syntax: `/catalogue/7` selects element 7 of the object's `catalogue` array, while `/19` selects element 19 of a root array. The pointer accompanies its exact file path. Source rows are selected by their original identifiers before a pointer is recorded; array positions are never used to identify unrelated rows across files.

| Source block | Record route | Additional model |
|---|---|---|
| B.36 exceptional actions | `exceptional_sections.json`, `/catalogue/i`, selected by `action_class` | The group, affine data, or extension model is in that record. |
| B.26 punctured spheres | `type_0_ν_orbifold_sections.json`, `/i`, selected by `class_id` | The record contains the exact finite orbifold model. |
| B.27 punctured tori | `type_1_ν_affine_sections.json`, `/catalogue/i` | `torus_affine_normal_forms.json`, `/j`, selected by the exact integer `affine_id`. |
| B.28 closed genus two | `type_2_0_extended_sections.json`, `/catalogue/i` | Same file, `/hyperelliptic_extensions/j`, selected by `extension_id`. |
| B.29 punctured genus two | `type_2_ν_extended_sections.json`, `/catalogue/i` | The exact hyperelliptic model in the closed file, selected by `extension_id`. |
| B.33 positive genus three | `code/root/higher_genus_output/oriented_higher_genus_sections.json`, `/i`, selected by `summary.id` | The record contains the finite group, its generating vector, and all coset actions. |
| B.37, B.39, B.40 mixed genus three | Corresponding `code/part_c/*_sections.json`, `/i` | The record contains the full group; the certificate route retains the classification monodromy. |
| B.38, B.41 mixed genus three | Corresponding `code/part_b/*_sections.json`, `/catalogue/i` | The record contains the multiplication table and quotient monodromy. |

The detailed section records give the image subgroup, local multipliers as exact rational strings, centralizer, strict extensions, maximal extensions, and `Γ` stabilizer. Source-specific names are retained: for example, the sphere models use `mu_by_element_id`, the affine models use `mu`, and the positive census uses `partial_section_classes` and `maximal_sections`. The routing index introduces no change of element numbering. In a shared model, use the element IDs from that exact model.

Here is a complete lookup from the root of the extracted ZIP:

```python
import csv
import json
from pathlib import Path

root = Path('.')
rows = list(csv.DictReader(
    (root / 'code/part_b/low_complexity_all_realizations.csv').open()))
row = next(r for r in rows if r['realization_id'] == 'g0n0:sphere_antipodal')

def resolve_json_pointer(value, pointer):
    if not pointer:
        return value
    for token in pointer[1:].split('/'):
        token = token.replace('~1', '/').replace('~0', '~')
        value = value[int(token)] if isinstance(value, list) else value[token]
    return value

record = resolve_json_pointer(
    json.loads((root / row['section_json']).read_text()),
    row['section_pointer'])
print(record)
```

## Genus-three completeness and exact positive-class matching

The 292 classes are the disjoint union of the following blocks.

| Block | Classes | Geometric classification |
|---|---:|---|
| B.33 | 55 | Positive actions in the complete Karabáš–Nedela–Skyvová census. |
| B.37 | 145 | Mixed actions with positive quotient a sphere and negative quotient a mirror disc. |
| B.39 | 11 | Mixed actions with positive quotient a sphere and negative quotient a projective plane. |
| B.40 | 57 | Mixed actions with positive quotient a torus and negative quotient an annulus or Möbius band. |
| B.41 | 6 | Mixed actions with positive quotient a torus and negative quotient a Klein bottle. |
| B.38 | 18 | Twelve actions with free positive subgroup `C₂`, and six negative involutions with trivial positive subgroup. |
| **Total** | **292** | **55 positive and 237 mixed.** |

The positive quotient genus and quotient topology establish disjointness of these blocks; B.37–B.41 prove exhaustion and equivalence within each block. The 79 hyperelliptic rows of B.34 are already present: C's independent reconciliation gives an explicit map to 18 positive, 57 mirror-disc, and four projective-plane rows. They are not added to the total again. The independent oriented genus-two tables and the earlier B.25 tables likewise remain cross-checks of the corresponding complete blocks.

The primary genus-three input has 49 group/signature pairs and 55 positive action classes. The pair-to-class fibers are nontrivial for `O3.9`, `O3.11`, `O3.16`, `O3.21`, and `O3.23`. The assembler recomputes the exact colored-braid and mirror orbits on the original `autgreps` array for these pairs, then matches each orbit to the generating vector in the positive section record. Each mixed certificate retains the original `autgreps` indices in `kernel_orbit`. Every such index belongs to one matched positive orbit, so this gives the exact `positive_class_realization_id`.

All **59 mixed rows** above these five pairs pass this orbit-containment check. The actual orbit-index lists and every mixed-row match are recorded in `type_3_0_positive_class_routing.json`. Positive restriction is therefore determined by monodromy and its proved equivalence relation, including the pairs whose numerical signatures coincide.

The primary data and attribution are included in `code/root/research_data/`. The accompanying census is Karabáš–Nedela–Skyvová, *Computing equivalence classes of finite group actions on orientable surfaces*, Journal of Pure and Applied Algebra 228 (2024), 107578, with source data from `https://www.savbb.sk/~karabas/science/discactions.html`; see B.33 for the precise input and independent checks.

## Executed validation and reproduction

From the extracted ZIP root, run:

```sh
python code/part_b/assemble_low_complexity_catalogues.py
```

The same script detects the development workspace layout. It writes the aggregate files beside itself and stops on any failed assertion. It requires the source CSV/JSON files and `code/root/catalogue_higher_genus.py`; no additional census download is needed.

The executed validation confirms:

- Exactly the 16 pairs of nonnegative integers satisfying `2g + ν ≤ 6` occur.
- All 889 realization identifiers are unique, and the explicit realization map has exactly 882 targets.
- Every type has the count in the table above.
- The full and partial section counts and `Φ` counts reconcile with all 889 detailed records.
- All **1,845** section, shared-model, positive-action, and classification-certificate pointers resolve against their exact files.
- Every genus-three source ID, proof block, group order, positive order, and all six scalar section fields agree with C's independent `code/part_c/type_3_0_complete_catalogue.csv`.
- All 59 ambiguous positive-restriction matches follow the recomputed monodromy orbits.
- Every input is identified by its exact package path and SHA-256 hash in the validation JSON.
- A fresh copy containing the exact 44 required input files in the ZIP layout produces all eight aggregate outputs byte-for-byte identically; all 1,845 pointers resolve there as well.

These checks certify the joins, stored finite data, and reproduction routes. The completeness proofs and equivalence arguments are the numbered claims in the paper identified by each row.
