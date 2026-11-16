#!/usr/bin/env python3
"""Metadata and outcome updates for the independently audited A80--86 and B16."""
from pathlib import Path
import json
w=Path(__file__).resolve().parents[1]
p=w/'notes/register_metadata.json'
m=json.loads(p.read_text())
data={
'A.80':('A9; A12; A15; L2; L14; L20','A.57; exact root stabilizers and generated subgroup; quadratic Kummer theory; Steinberg symbols','The complete common abelian fibre field equals the multiquadratic field when -1 is outside the radicand squareclass span. The actual stabilizer maps and reverse inclusion are proved. Every resulting cyclic class on the old cover is an explicit global constant.'),
'A.81':('A5; A15; L10; L14','A.27; A.38; A.75; A.77; continuous Shapiro and Milnor sequences; exact binomial valuations','The norm compatibility class injects into the actual one-variable obstruction with the specified minus sign. The derived kernel is L_n=(X^(ell^n)-1)/(X-1). Under the finite-weight isomorphism it is a compatible family of coefficient-power phantom classes for the same fixed pair; no vanishing is inferred.'),
'A.82':('A1; A7; L15; L19','A.16; A.34; A.37; A.78; A.79; common global Weil multiplier; exact quadratic-form Hensel tests','The one global multiplier gives a homogeneous unit-square form at each candidate cusp. Odd-prime and dyadic unit-zero questions are equivalent to the stated finite tests. Parameter34 is recognized with arbitrary labeled integral comparison, including all dyadic and coefficient3 branches.'),
'A.83':('A9; A12; A15; L2; L14; L20','A.48; A.57; A.80; actual local reciprocity; Chebotarev; Hasse-Weil and Hensel','In the stated squareclass range an additional finite-exponent coordinate can be initialized while preserving every prescribed old local point. Products of primes with fixed fibre roots realize the full generated stabilizer image, and a fresh valuation-one prime is retained. A completed countable-puncture tuple is not claimed.'),
'A.84':('A1; A7; L15; L19','A.16; A.34; A.37; A.63; A.74; A.78; A.82; exact nome logarithms','Parameter35 is recognized with arbitrary labeled integral comparison. A full coefficient17 Tate equation forces every bad place to be cuspidal; two coefficient5 comparisons then give a nonsquare ratio despite the common multiplier. The weaker regular-coordinate form has an actual surviving local solution, explicitly retained.'),
'A.85':('A9; A12; A15; L2; L14; L20','A.57; A.69; A.73; A.80; A.83; exact cyclic reciprocity and generated stabilizers','Necessary and sufficient finite-character condition for initializing one rational puncture at a fixed exponent while lifting prescribed old local points. Every outside-S evaluation is zero. The earlier finite-level obstructions persist on finitely many local neighborhoods; a completed old tuple through those neighborhoods remains unconstructed.'),
'A.86':('A5; A15; L10; L14','A.75; A.77; A.81; actual local norm elements; completed divisor sequences; ordinary and narrow ideal class groups','Ordinary local points construct compatible c0 completed divisors, including real signs at2. Compact unit compatibility vanishes. The same-pair full one-variable lift is equivalent to the explicit compatible finite ideal-class family lying in the image of compatible norm-zero divisor representatives. All connecting maps and signs are given.'),
'B.16':('A4; A11; L3; L6','B.8; Khare-Larsen-Ramakrishna Fact6,Lemmas7-9,Propositions10-11; Khare-Rajan Theorem1; Tate uniformization; Waterhouse and simultaneous integral lattice isogenies','Constructs actual7-adic and11-adic representations with one common local elliptic curve at every prime, integral local comparisons and infinitely many common ramified primes. The ramification sets agree away from7,11, whose cyclotomic exceptions are retained. Exact field disjointness, split-sign element and alternating finite-level construction are proved. No full all-coefficient family or tripod section is asserted.')
}
for key,(answers,depends,notes) in data.items():
 m[key]={'answers':answers,'depends_on':depends,'notes':notes,
 'uses_local_theorem':('no for the stated Selmer result; extending to arbitrary sections uses R1' if key in ('A.82','A.84') else 'no; the named local curves, quotient maps, cocycles or finite Kummer covers are constructed directly'),
 'manuscript_passages':'cote149; scans48,54–58,63,66,79–85,120–130; exact item and lead scope in answers column'}
p.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md'
s=p.read_text(); lines=s.splitlines()
updates={
'A4':('B.8','B.8, B.16',' B.16 now gives two coefficient systems,7 and11, with the same local elliptic curves at every prime and infinite common ramification away from the coefficient-prime exceptions. The all-coefficient and actual-section passages remain.'),
'A5':('A.75, A.77 |','A.75, A.77, A.81, A.86 |',' A.81 identifies the coherent-norm class inside the integral finite-weight coefficient phantoms, and A.86 gives its exact representative as a compatible finite ideal-class family; unit and divisor-norm compatibility have been removed in the stated maps.'),
'A7':('A.78–A.79 |','A.78–A.79, A.82, A.84 |',' A.82 retains the one global multiplier in an exact finite quadratic-form test and recognizes34; A.84 recognizes35 using the full Tate logarithms across two bad places. Both use arbitrary labeled integral comparison.'),
'A12':('A.73, A.76 |','A.73, A.76, A.80, A.83, A.85 |',' A.80 computes the full common character field in its squareclass range. A.83 constructs a new coordinate there by products of fibre primes. A.85 proves the necessary and sufficient finite-character initialization condition in general and preserves the obstructions on finite local neighborhoods.'),
'A15':('A.75–A.77;','A.75–A.77, A.80–A.81, A.83, A.85–A.86;',' The finite-character initialization test is now an exact equivalence, and the same-pair coherent-norm obstruction is represented by the explicit ideal-class family.'),
'L10':('A.75, A.77 |','A.75, A.77, A.81, A.86 |',' The precise next condition is A.86: the compatible finite ideal-class family must admit compatible norm-zero divisor representatives.'),
'L14':('A.75–A.77;','A.75–A.77, A.80–A.81, A.83, A.85–A.86;',' A.85 computes the full finite-character initialization equivalence; A.86 supplies the compatible ideal-class obstruction for the actual one-variable quotient.'),
'L15':('A.70 |','A.70, A.78–A.79, A.82, A.84 |',' The cusp-only support equations, additional infinite families, exact unit-square forms and full Tate-logarithm comparisons now recognize34 and35 in the unrestricted labeled integral range.'),
'L20':('B.4–B.7, B.15 |','A.80, A.83, A.85; B.4–B.7, B.15 |',' For a fixed finite Kummer exponent, A.85 now determines exactly when one more rational puncture can be initialized with prescribed local lifts; the compatible full fundamental-group lift remains.')
}
for i,line in enumerate(lines[:50]):
 for key,(old,new,extra) in updates.items():
  if line.startswith('| '+key+' |'):
   line=line.replace(old,new)
   assert line.endswith(' |')
   lines[i]=line[:-2]+extra+' |'
s='\n'.join(lines)+'\n'
s+='\n## Fifth-hour advances recorded at05:16 UTC\n\nA.80–A.86 and B.16 have root and independent-agent audits. A.81 gives the precise derived-kernel and Milnor maps from norm compatibility to coefficient-power phantom classes. A.86 constructs compatible local norm divisors and removes completed-unit compatibility; its remaining condition is the exact inverse ideal-class image. A.83 and A.85 initialize one finite-exponent puncture by products of actual fibre primes, with an exact finite-character obstruction and prescribed local points. A.82 and A.84 recognize34 and35, retaining the common global multiplier and all dyadic cases. B.16 constructs a7-adic and11-adic pair sharing every local elliptic curve, with infinitely many common ramified primes. Its ramification sets agree only away from7 and11: the own-coefficient cyclotomic determinant forces ramification there, whereas the other coefficient sees good reduction. This correction is in the statement and proof.\n\nThe root reopened Khare–Larsen–Ramakrishna, arXiv math/0309283, Definition1, Fact6, Lemmas7–9, Propositions10–11, the Main Theorem and Corollary14; Khare–Rajan, arXiv math/0011272, Theorem1; and Das–Sarkar, arXiv2208.04170v3, Definition3.1 and Lemma6.1. Das–Sarkar assumes a fixed finite m-ramification set and finite inertia of bounded order outside it; the nonzero tame unipotent inertia in the current problem does not supply that hypothesis. B.16 uses the actual simultaneous auxiliary-prime field isomorphism and alternating correction maps instead. It asserts no all-coefficient or section lift.\n'
p.write_text(s)
audit=('Root audits05:16UTC: A80 exact stabilizers and Steinberg constants; A81 derived L_n, continuous cochain splittings and both Milnor sequences; A82 common multiplier, normalized odd/dyadic Hensel equivalences and34; A83 ray-class inverse, generated stabilizers and every local point; A84 full Tate constants256, nome logs and coefficient5/17 squareclasses; A85 general common-field exponent, every outside-S case and principal reciprocity; A86 signed completed divisor sequence, c0 valuation formulas, compact unit lim1 and connecting signs. All passed. B16 independent audit required and incorporated the order-two split-sign element and the exact7/11 ramification exceptions.\n')
(w/'notes/hour5_root_audits.md').write_text(audit)
with (w/'notes/root_progress.md').open('a') as f: f.write('\n'+audit)
out='Integrated metadata and outcome scope for A80–A86 and B16; all main assertions remain unresolved.\n'
Path(__file__).with_name('integrate_hour5_first_output.txt').write_text(out)
print(out,end='')
