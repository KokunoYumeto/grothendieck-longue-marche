#!/usr/bin/env python3
"""Record locations already established by the main reader's visual checks.

This script records those editorial conclusions. It does not inspect handwriting,
change transcription bytes, or verify the full catalogue ranges or attributions.
"""
import json
from review import D, now, rebuild

ADDITIONS = {
    'L737': 'Main-reader location confirmation: the co-Lie heading and boxed formulas (1.3) and (1.4) were directly inspected on the supplied cote 8 scan 078, manuscript page 77. This is the verified local formula-bearing leaf. The complete cote-7 inventory is not among the supplied inputs and its asserted scan count is not re-established here.',
    'L742': 'Main-reader cross-location check among the supplied and visually reviewed leaves: cote 8 scan 019 is the Tribu n. 66 integration sheet; scan 021 is typescript page 65 on holomorphic functions; scan 030 is handwritten chart-family material; scans 035 and 037 visibly carry n. 382 and typed pages 84 and 83, with jets sections 7.2.7 and 7.2.4 respectively; scan 058 is the squared-paper table with fractions and line diagrams; scan 061 is the handwritten Tannakian page. The separate page reports and named crops document these local identifications. This does not verify the unsupplied intervening leaves or every bibliographic attribution in the proposed range.',
    'L743': 'Main-reader cross-location check: cote 8 scan 032 is the corrected typescript leaf marked 55 ter with the proof and Remarque 5.13.1; scan 062 is typed page 35 with the smooth-pair construction, base change, and descent; scan 074 is typed page 31 with the Kummer sequence, formula (3.9), and Théorème (3.10); scan 072 is typed page 35 explicitly numbered 357, with convolution formulas and a paragraph naming Bourbaki. These are directly inspected local loci, documented in their separate crop reports. The complete SGA attributions, printed-book correspondences, and unsupplied intervening pages remain supplied catalogue information.',
    'L744': 'Main-reader cross-location check: the supplied cote 8 scan 017 is the visibly cancelled note with the uniqueness assertion and mu_2 discussion; scan 032 is the typescript marked 55 ter; scan 061 expressly names a catégorie tannakienne and a fibre functor over Q_p; scan 063 contains the full-faithfulness and algebraic-envelope assertion. These leaves were directly reviewed. Their separate reports establish the local distinctions without checking every scan in the proposed external range.',
    'L745': 'Main-reader cross-location check: cote 8 scan 025 has the ordinary Barsotti–Tate heading and category C; scan 031 contains the differential/gauge formulas; scans 044, 046, and 050 contain the reviewed filtered-module, divided-power, and lifting/lattice formulas; scan 058 is instead the squared-paper table of fractions and line diagrams. These are verified local contents in the supplied scans, not an independently established bibliographic identification of the whole proposed Lubin–Tate range.',
    'L747': 'Main-reader cross-location check: cote 8 scan 002 visibly presents the paired site maps and phi epsilon = F_S; scan 004 contains the crystalline-complex material and related maps; scan 019 is the actual Tribu n. 66 integration sheet. The reports and retained crops for those pages document these local distinctions. No claim is made about absent or unsupplied leaves of the proposed range.',
    'L748': 'Main-reader cross-location check: cote 8 scan 037 visibly bears redaction n. 382 and typed page 83, with jets material; scan 078 has the coLie heading and boxed formulas (1.3) and (1.4); scan 081 has the explicit Illusie attribution and the lifting-obstruction discussion. These directly inspected leaves distinguish the local subjects. Scans 079–080 and the complete cote-7 inventory are not supplied and are not declared checked.',
    'L749': 'Main-reader cross-location check: the related Mazur-Roberts name and boxed co-Lie formulas are visibly on cote 8 scan 078, documented under L752 and L753 and its formula crop. The explicit Illusie attribution is on the current scan 081. These are manuscript locations only; this run has not opened or independently verified the cited Bergh–Rydh or Illusie publications.',
    'L750': 'Main-reader cross-location check: cote 8 scan 001 is the supplied cover; scan 019 is the separate sheet explicitly headed Tribu n. 66 and Décisions sur l’Intégration. Both were directly inspected. A cover label does not establish the identity of every leaf in the supplied cote.',
    'L751': 'Main-reader cross-location check among the supplied leaves: cote 8 scan 073 bears manuscript number 72 and the handwritten connection/Frobenius/Betti list; scan 078 bears manuscript number 77 and the co-Lie heading and formulas; scan 081 contains the Illusie attribution and obstruction discussion. These local identifications were directly inspected. The external PLACEMENT table is not supplied, and the claimed duplicated-cote parsing and complete catalogue lists have not been independently reconstructed.',
    'L1366': 'Main-reader cross-location check: both nominated supplied cote-8 leaves were inspected. Scan 004 contains crystalline-complex material, and scan 074 is the mathematical typescript numbered 31 with the Kummer sequence and Théorème (3.10). Neither supplies the quoted Lodève date or Lettres Breen cover. No alternative location for that letter target has been found in the reviewed material.',
}

for path in sorted((D / 'reviews').glob('8_scan*.json')):
    report = json.loads(path.read_text())
    changed = False
    for row in report['rows']:
        addition = ADDITIONS.get(row['id'])
        if row['decision'] != 'd' or not addition or addition in row['note']:
            continue
        row['note'] += ' ' + addition
        row.setdefault('events', []).append({
            'date': now(),
            'who': 'GPT-6 Astra Pro; effort not exposed; main reader; run IM02_6-9_20261120',
            'type': 'used and rechecked in this run',
            'outcome': f'Cote {row["cote"]}, scan {int(row["scan"]):03d}: ' + addition,
        })
        changed = True
    if changed:
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(rebuild())
