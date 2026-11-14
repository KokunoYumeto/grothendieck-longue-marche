"""Record the completed root proof, dependency and copied-execution audit."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'research_e107'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
enc = lambda x: json.dumps(x, indent=2, ensure_ascii=False) + '\n'
fresh = json.loads((HERE / 'comparison.json').read_text())
assert fresh['status'] == 'PASS' and fresh['exit_code'] == 0
assert fresh['excluded_fields'] == []
manifest = AUTHOR / 'ledger/e_stable_ordinary_manifest.json'
assert sha(manifest) == fresh['manifest_sha256']
for relative, digest in fresh['frozen_input_and_source_sha256'].items():
    assert sha(AUTHOR / relative) == digest, relative
for row in fresh['comparisons']:
    assert row['entire_file_byte_identical']
    assert (HERE / row['path']).read_bytes() == (AUTHOR / row['path']).read_bytes()

checks = [
 'The actual cyclic-nine norm/inclusion square sends the subgroup generator to the third power of the chosen ninth generator. The injection Z/3 -> Z/9 is used only after both exponent values lie in its image, proving equality of the consecutive arithmetic characters on included units.',
 'The residue field F289 calculation fixes the sign from xi, gives eta character2 at17, and uses global reciprocity to give character1 at3. E106 supplies an actual ordinary-unit norm preimage in B3. The three split horizontal completions have residue degree1 and the same radical generator, so their two triple sums are exactly(1,2).',
 'This fifth vector adds to the entire rank4 image. Global reciprocity bounds the image by the fixed dimension5 hyperplane. The actual inclusion square preserves these five unit characters at every later stage; no finite class-number extrapolation is used.',
 'The ambiguous formula uses the FIELD-norm index3^5 and E91 actual triviality of the entire vertical three-class action. The ordinary ideal norm is proved onto by disjointness from the Hilbert three-class field and the explicit Frobenius(1,a) norm construction. These maps, with equal finite orders, transport all class coordinates.',
 'The named S-prime ideals have unique residue-degree1 vertical prolongations. Their actual class columns and principal divisor lattice transport through the norm isomorphisms. The horizontal norm and the nonzero L2 prime class prove exact prime3 order3 in all later L fields.',
 'The horizontal extension and norm squares retain their precise coefficients. Hilbert90 for principal ideals and the unit Herbrand quotient give horizontal ordinary-unit norm surjectivity. The strongly ambiguous divisor quotients supply the additional vertical ordinary-unit defects, giving C3^6 and C3^3 and the stated norm-one kernel ranks.',
 'E72.9 identifies each finite coherent three-unit base norm image with lambda^(3Z3), now that the prime class order is3. E69.16 fixes the root-of-unity coordinate. Compact finite intersection uses actual adjacent norm equations to produce a coherent tuple e with e0=lambda^3; the opposite inclusion follows from every finite projection. Thus h=1.',
 'The product coordinates of U_infinity^0 use E69.6 and its actual recursive forward/inverse maps. The new splitting U_infinity=Z3 x U_infinity^0 extracts the normalized base valuation and removes e to that power.',
 'The E88 divisor kernel and original phase congruence are retained. Theta_star(t)=-sum ell_p*t_p/3 is integral on that precise kernel and continuous for restricted coefficients. Multiplication by e^((Theta_star-Theta)/3) changes precisely the base3 phase and preserves every outside divisor and the17 valuation. The full ambiguity is Hom_cts(K,U_infinity^0).',
 'The norm formula is evaluated prime by prime. E46.7 divides the actual total-norm exponents by3 only on its cube locus. The raw beta exponent is b=3*B17/2; the finite inverse test was corrected to this convention with its prior source/output retained. Both forward and inverse toric maps have exactly U_infinity^0 as the remaining coordinate and use the explicitly fixed pure component1.'
]
audit = {
 'status':'PASS', 'statement':'E.107',
 'complete_proof_read':True,
 'proof_lines':len((AUTHOR / 'sections/E_stable_ordinary_phase.tex').read_text().splitlines()),
 'proof_sha256':fresh['proof_sha256'],
 'complete_mathematical_program_read':True,
 'program_sha256':fresh['program_sha256'],
 'author_manifest_sha256':fresh['manifest_sha256'],
 'manifest_files_checked':22,
 'complete_fresh_rebuild':fresh,
 'proof_checks':checks,
 'exact_internal_comparisons_read':['E69.6','E69.16','E72.9 and its full proof','E72.10','E88.7','E88.10','E46.7','E101.20--24','E106 complete root audit'],
 'primary_source_reading':[
   {'key':'E_MilneCFT','url':'https://www.jmilne.org/math/CourseNotes/CFT.pdf',
    'scope':'The E106 root audit already reads the proved local Res/Cor cup compatibility, III4 Hilbert symbol proof, VII3.1 complete unit-Herbrand proof, and VIII3.1 cyclic Hasse norm proof. This audit additionally reads V3.3 with its ideal-norm/Frobenius argument, V3.6 as stated, and VIII7.4 through the end of its complete proof.',
    'fresh_root_refs':['turn903view0','turn903view1','turn903view2','turn903view3'],
    'precision':'No complete printed proof is claimed for the omitted III3.2 lemma. The actual local square is supported by the preceding proved cup-product compatibility.'},
   {'key':'E_LemmermeyerAmbiguous','url':'https://arxiv.org/pdf/1309.1071',
    'scope':'Complete Theorem1, Proposition1, Lemma1 and ideal/index derivation through section3 were read in the E106 root audit; the exact strongly ambiguous quotient is applied in E107. The recorded Am_st/Am notation slip is resolved by its explicit ideal Hilbert90 map.'}
 ],
 'correction_provenance':json.loads((AUTHOR / 'ledger/e_stable_ordinary_toric_test_amendment.json').read_text()),
 'integration_routing':'Keep this exact source with its three immutable inputs in an isolated bundle. The source includes hashes of every sibling input; merging its inputs with E106 inputs would change metadata. No mathematical source change is needed.',
 'remaining_original_scope':['separate pure-field norm system','unrestricted intrinsic lifting','other-primary and mixed sources']
}
(HERE / 'audit.json').write_text(enc(audit))
lines = ['# Completed root audit: E.107', '', 'Result: PASS.', '',
         'The complete proof, final mathematical program, actual internal comparisons and source evidence were read. The copied execution completed with exit0; both entire outputs match byte for byte with no exclusions. All22 frozen manifest files remained unchanged.', '',
         '## Proof and map checks', '']
for item in checks:
    lines.extend(['- ' + item, ''])
lines.extend(['## Preserved scope', '',
 'This proves the all-level exponent h=1 and the complete complex positional component with pure component1, with the actual toric forward and inverse maps. The separate pure-field system and intrinsic source lifting remain active.', '',
 'The exact three-input layout is preserved in the reproducible bundle; the raw-exponent test amendment and its complete original files are retained.', ''])
(HERE / 'README.md').write_text('\n'.join(lines))
print(enc({'status':'PASS','statement':'E.107','proof_lines':audit['proof_lines'],
           'manifest_files_checked':22,'audit_sha256':sha(HERE / 'audit.json'),
           'full_output_byte_equality':True,'excluded_fields':[]}))
