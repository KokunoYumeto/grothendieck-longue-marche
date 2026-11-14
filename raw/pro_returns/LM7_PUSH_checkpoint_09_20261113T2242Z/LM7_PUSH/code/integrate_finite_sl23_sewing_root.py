#!/usr/bin/env python3
"""Integrate independently audited E.59 and E.61 without changing E.3 status."""
from pathlib import Path
import ast
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
SAVED = ROOT / 'research/checkpoint09_sl23_sewing_prior_passages.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert not SAVED.exists(), 'One-shot integration already performed.'
    e59 = json.loads((ROOT / 'research/root_E59_replay/result.json').read_text())
    e61 = json.loads((ROOT / 'research/root_E61_replay/result.json').read_text())
    assert e59['status'] == 'PASS_ISOLATED_COMPLETE_E59_REPLAY'
    assert e59['all_mathematical_outputs_identical']
    assert e59['protected_original_files_unchanged']
    assert len(e59['complete_generation_certificates_replayed']) == 144
    assert e61['status'] == 'PASS_ISOLATED_COMPLETE_E61_ROOT_REPLAY'
    assert e61['all_output_bytes_identical']
    for manifest_name, expected in [
        ('research/E59_authoritative_manifest.json', e59['manifest_sha256']),
        ('research/E61_authoritative_manifest.json', e61['manifest_sha256']),
    ]:
        path = ROOT / manifest_name
        assert sha(path) == expected, manifest_name
        for name, record in json.loads(path.read_text())['files'].items():
            assert sha(ROOT / name) == record['sha256'], name

    names = ['LM7_PUSH_paper.tex', 'code/assemble_register.py',
             'research/report_body.md', 'LM7_PUSH_references.bib',
             'research/root_searches_02.md']
    old = {name: (ROOT / name).read_text() for name in names}
    new = dict(old)
    anchor = r'\InputIfFileExists{sections/E_relative_cm_lift_agent.tex}{}{}'
    assert new['LM7_PUSH_paper.tex'].count(anchor) == 1
    new['LM7_PUSH_paper.tex'] = new['LM7_PUSH_paper.tex'].replace(anchor, anchor + '\n' +
        r'\InputIfFileExists{sections/E_sl23_ferrari_agent.tex}{}{}' + '\n' +
        r'\InputIfFileExists{sections/E_genus_one_sewing_agent.tex}{}{}')

    lines = new['code/assemble_register.py'].splitlines()
    changed = []
    addition = (
        ' E.59 exhausts the complete 512-element correction image above each '
        'of the 24 specified E.17 G6 points in the universal SL2(F3) Ferrari '
        'source. Each has four generating gentle values and two generating '
        'pentagon values. The actual correction group is Q8^3 through three '
        'specified evaluation maps. All 24 positive CM matrix pairs, including '
        '12 extra pairs, survive; the nontrivial cusp gauges and whole common '
        'G6 source are retained. Every mathematical output and all 144 final '
        'generation certificates pass isolated root replay. E.61 proves the '
        'signed matrix formula q12(f)=[[1,-8rho],[-8rho,1+64rho^2]] for every '
        'normalized full gentle pair of multiplier one. The actual affine '
        'four-strand sewing word has translation (-B-8rho A,A-1); its modulus '
        'twelve value is the identity throughout this entire gentle domain. '
        'All four central braid carries and the exact frame rho are retained. '
        'Arbitrary finite pentagon sources remain unresolved.')
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] != 'E.3':
            continue
        assert row[2] == 'OPEN: full GT image'
        assert row[3].endswith('Arbitrary finite sources remain unresolved.')
        old['E3_coverage_row'] = row
        state = row[3][:-len('Arbitrary finite sources remain unresolved.')].rstrip() + addition
        lines[i] = ' ' + repr((row[0], row[1] + '; E.59; E.61', row[2], state)) + ','
        changed.append(row[0])
    assert changed == ['E.3']
    new['code/assemble_register.py'] = '\n'.join(lines) + '\n'

    body = new['research/report_body.md']
    start = body.index('1. **E.3:**')
    end = body.index('\n', start)
    old['prior_current_E3_paragraph'] = body[start:end]
    current = (
        '1. **E.3:** The full profinite GT CM image remains undecided. E.58 '
        'constructs an actual full gentle pair with positive extra CM bits '
        '(1,0). E.17--E.57 retain the stated finite and full boundary families '
        'through their specified four- and five-strand targets and integral '
        'congruence systems. E.59 now exhausts all 512 corrections over each '
        'of the 24 specified E.17 G6 points in the complete SL2(F3) Ferrari '
        'source: every fibre has four generating gentle points and two '
        'generating pentagon points, preserving all 12 extra CM matrix pairs. '
        'The counts are scoped to these complete finite-value fibres. E.61 '
        'proves that the actual modulus-twelve affine genus-one sewing '
        'projection is the identity for every normalized multiplier-one '
        'gentle pair, with its unique frame coordinate and central braid '
        'factors retained. The central-three A6 and GL2(F3) whole correction '
        'fibres remain active, together with the exact higher-genus sewing '
        'comparison. The revised Boggi v6 source is being checked at its '
        'actual stabilizer, capping, and inner-conjugator maps; its global '
        'conclusion is not used before the required proof and based '
        'comparison are supplied. Compatibility through every finite '
        'pentagon quotient, or a complete finite exclusion of every extra '
        'CM fibre, remains to be proved.')
    body = body[:start] + current + body[end:]
    body += '''

## The complete SL2(F3) fibres and the genus-one projection

E.59 constructs the universal Ferrari target from all 384 ordered generating pairs of the literal matrix group SL2(F3), its 24 automorphisms and 16 epimorphism kernels. Its target has order 43,486,543,872. The complete induced modular source retains six evaluations in each of six B/F cosets; its faithful orbit compression has degree 1956 and order 48,922,361,856. The N_B image has index 576. Its complete derived image has order 512, and three actual evaluation projections give a bijection with Q8 cubed. All 97 sixth powers lie in this image, which is therefore the entire image of K6 and of F-prime intersect K6. Every correction has a retained N_B-prime word.

Every one of the 512 values is tested over each of the 24 specified E.17 G6 points. Each fibre has four gentle values and two values satisfying the pentagon and all three braid relations. The 96 gentle maps generate the complete source, and the 48 pentagon maps generate the complete target and fix both literal full twists. The proof retains the actual common G6 source by the explicit Goursat comparison; it also retains the original nontrivial cusp gauges. The resulting actual frames have 24 distinct positive E.1 CM matrix pairs, including all 12 extra pairs. This statement counts those whole finite-value fibres; it asserts no count of other affine G6 points or other multiplier residues, and no full profinite pentagon lift.

Root and profinite_images read the entire E.59 proof. Root read every new mathematical program and the isolated replay driver. The complete isolated run passed in 322.028 seconds: every mathematical JSON field and every saved NPZ array agrees with the frozen output, all 144 final generation certificates were completely replayed, and all 691 protected originals remain unchanged. The initial 23 failing uncorrected words, interrupted invocation, list/tuple failure and incorrect trivial-gauge assertion remain preserved. Their complete fibres now have the two generating pentagon values just stated; the failed individual words were never treated as fibre exclusions.

E.61 uses the actual unique pure s-frame beta of a normalized multiplier-one gentle pair and sets h=beta-inverse, with h-ab=(rho,rho). This is the exact Nakamura--Schneps Definition 5.1 coordinate. The signed modulus-twelve matrix is [[1,-8rho],[-8rho,1+64rho^2]]. The proof retains the sign by reduction modulo four and checks all 24 SL2(F3) frame values at three; exactly 12 obey the signed cubic relation. The literal homomorphism from B4 to (Z/m)^2 semidirect SL2(Z/m) sends a,b,c to (0,U),(0,L),(e1,U). The sewing word has translation (-B-8rho A,A-1), where [[A,B],[C,D]]=f(U^2,L^2). It is therefore the identity modulo twelve for every such full gentle pair, including E.58's extra pair.

The four actual A3-to-B4 substitutions retain central full-twist coefficients 2,-2,2,-2. These cancel in the complete product. Their use of Nakamura--Schneps relation IV is stated on that source's subgroup; the universal finite projection proof uses only the actual gentle identities. Root independently opened Definition 5.1 and Claim 8.3 in the primary author PDF, the cited Artin representation and Theorem A in Shpilrain's primary PDF, and the BBR v2 theorem used for the sewing comparison. Root and profinite_images read the whole E.61 proof, and root read its full standard-library program. The isolated replay passed in 2.854 seconds, with byte-identical JSON and stdout and all seven frozen originals unchanged. It verifies all 16 literal braid comparisons, every mod-three frame, all 24 saved framed words and the full signed affine calculation.

These two results are integrated after checkpoint 08. Their complete previous active coverage row, report paragraph and edited files are preserved in research/checkpoint09_sl23_sewing_prior_passages.json. The register continues to mark E.3 Open. The ongoing 3.A6 source replay and signed fibre calculation, GL2(F3) correction fibres, and Boggi v6 morphism audit are not promoted to completed global results by this integration.
'''
    new['research/report_body.md'] = body

    bibliography = (ROOT / 'research/E61_references.bib').read_text()
    for key in ('BCBasualdoRobertson2026', 'BCShpilrain2002'):
        assert key not in new['LM7_PUSH_references.bib']
    new['LM7_PUSH_references.bib'] += '\n' + bibliography
    ns_note = 'the exact double-cover and inversion maps are proved in D.5.'
    assert new['LM7_PUSH_references.bib'].count(ns_note) == 1
    new['LM7_PUSH_references.bib'] = new['LM7_PUSH_references.bib'].replace(ns_note,
        ns_note + ' Root reopened Definition 5.1 on author-PDF p. 17 and '
        'the proof of Claim 8.3, relation (R-prime), author-PDF pp. 33--34. '
        'E.61 retains the literal frame coordinate, all four central braid '
        'carries, and the stated relation-IV domain.')

    new['research/root_searches_02.md'] += '''

141. Root opened Collas, arXiv:2603.02848v2, primary PDF, Introduction,
     contents and Theorem1.1 (turn565view0). Its full Section4 was not
     read in that visit. This lead supplies no asserted full-GT CM result.

142. Root opened Hoshi--Mochizuki--Tsujimura, JMS Univ Tokyo32(2025),
     pp.1--125, https://www.ms.u-tokyo.ac.jp/journal/32-1-1.pdf,
     Introduction TheoremsA--C and the COF/RGC/ArBC/QAA/AA hypotheses
     (turn565view1). The stated Belyi/Kummer compatibility data are retained;
     no assertion that every full-GT element satisfies them is used.

143. Root opened Boggi, arXiv:2011.15075v6 (22April2026), primary HTML
     and53-page PDF (turn587view0/1). Theorem6.7 and Corollary6.24 are
     read with the actual full profinite targets. Sections2.1/2.8 allow
     the annular-complement pants embedding, whose two boundary twists
     have the same image. The actual capping map in Proposition6.9
     retains one Weierstrass point. Lemma6.16's based uniqueness has
     the explicit identity/inner-twist alternatives. These particular
     proof issues, exact naturality conjugators and possible repair
     maps are preserved in DE_Boggi_v6_morphisms.md; no falsity of the
     global theorem is inferred. Geometry is checking the repair.

144. Root reopened NS newGT.pdf, Definition5.1 and proof of Claim8.3,
     relation(R-prime), author-PDF pp.17,33--34 (turn595view0/1).
     The actual h=beta-inverse and rho convention agrees exactly.
     The four A3 homomorphisms carry full braid central powers with
     coefficients2,-2,2,-2. RelationIV's subgroup domain is retained.
     Shpilrain's primary braids.pdf was opened at the Artin formula,
     TheoremA and its proof, pp.1--4 (turn592view1,turn595view2).
     The representation(k=1) is exactly the certificate convention.

145. E59 root complete proof/program read and isolated replay PASS,
     322.028seconds. Every mathematical JSON and NPZ array agrees;
     all144 generation certificates fully replayed,691 protected
     originals unchanged. All512 corrections over each24 retained
     G6 points give4 gentle and2 pentagon values, with complete
     actual source/target generation and positive CM gauges.

146. E61 root complete proof/program read and isolated replay PASS,
     2.854seconds. JSON and stdout are byte-identical; all7 protected
     originals unchanged. The signed cubic and exact rho comparison,
     everymod3 frame,16 braid identities,24 framed words, fourcentral
     carries and the affine sewing formula all pass. E59/E61 are
     integrated; the sole unresolved task remains E3.
'''
    SAVED.write_text(json.dumps(old, indent=2) + '\n')
    for name in names:
        (ROOT / name).write_text(new[name])
    accepted = {
        'statements': ['E.59', 'E.61'],
        'root_entire_proofs_and_new_programs_read': True,
        'independent_profinite_images_entire_proof_reviews': True,
        'E59_isolated_complete_replay_seconds': e59['seconds'],
        'E61_isolated_complete_replay_seconds': e61['seconds'],
        'E59_generation_certificates_replayed': 144,
        'E59_protected_files_unchanged': 691,
        'E61_protected_files_unchanged': 7,
        'proof_sha256': {name: sha(ROOT / name) for name in [
            'sections/E_sl23_ferrari_agent.tex', 'sections/E_genus_one_sewing_agent.tex']},
        'preserved_previous_files_and_passages': str(SAVED.relative_to(ROOT)),
        'E3_status': 'Open',
    }
    (ROOT / 'research/checkpoint09_sl23_sewing_acceptance.json').write_text(
        json.dumps(accepted, indent=2) + '\n')
    print(json.dumps(accepted, indent=2))


if __name__ == '__main__':
    main()
