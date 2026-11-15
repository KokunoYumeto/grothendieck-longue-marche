#!/usr/bin/env python3
"""Assemble post-freeze research notes only; never opens or writes page files."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
target = ROOT / 'MPL_60_036-070_notes.md'
scaffold = target.read_text()
if 'Research entries and verified primary references are being assembled' not in scaffold:
 raise SystemExit('Finished notes detected: this historical first-assembly script will not overwrite them.')
intro = scaffold.split('## Research register')[0]
standing = '## Standing question I' + scaffold.split('## Standing question I', 1)[1]
lf = (ROOT / 'records/lfunctions_research.md').read_text().split('## Draft items\n', 1)[1].split('## Assessment of the supplied Hua entry', 1)[0].strip()
alg = (ROOT / 'records/algebra_research.md').read_text().split('## Draft research items\n', 1)[1].split('## Exact primary references', 1)[0].strip()

queries = {
 'LF01':'inerti|moyenn|semi.simple|category of motives',
 'LF02':'inerti|unipoten|foncteur exact|semi.simple',
 'LF03':'tensor|tenseur|convol|foncteur fibre|category of motives',
 'LF04':'trace|Frobenius|inerti|moyenn',
 'LF05':'inerti|moyenn|alpha|mu_|faisceau virtuel',
 'LF06':r'virtuel|dualité|check|\[2\]',
 'LF07':'inerti|unipoten|alpha|mu_|monodrom',
 'LF08':'inerti|unipoten|monodrom|semi.simple',
 'LF09':'poids|polarisa|autoduali|dual',
 'LF10':'Tate|twist|fonctionnelle|poids',
 'LF11':'Artin|Ogg|conducteur|Swan',
 'LF12':'Frobenius|degré|déterminant|determinant',
 'LF13':'signe|fonctionnelle|delta|varepsilon',
 'LF14':'signe|fonctionnelle|delta|varepsilon',
 'LF15':'additif|epsilon|varepsilon|semi.simple',
 'LF16':'fonctionnelle|constante|Artin|Fourier',
 'LF17':'compact|infini|local cohomology|cohomologie local|dualité',
 'LF18':'involution|Hilbert|cocycle|fonctionnelle',
 'LF19':'Hilbert|niveau|fonctionnelle|involution',
 'LF20':'niveau|gradu|Lefschetzien|fonctionnelle',
 'LF21':'niveau|point fixe|involution|fonctionnelle',
 'LF22':'Tate|twist|poids|signe',
}

def sections(text):
 return [p for p in re.split(r'(?=^### [A-Z]+\d+ —)', text, flags=re.M) if p.strip()]

parts=[]
for part in sections(lf):
 key=re.match(r'### (LF\d+)',part)[1]
 lines=part.strip().splitlines()
 lines.insert(3, f'**Context search:** `{queries[key]}` in CT, CN and RESULTS_STATE; the relevant matches or absence are specified below.')
 parts.append('\n'.join(lines))
lf='\n\n'.join(parts)

# One primary kind per item. Supporting questions and tests remain in the prose.
for a,b in {
 'self-flagged / withdrawn approach':'withdrawn in the same text',
 'reading question / unpursued implication':'reading question',
 'own idea / unpursued implication':'own idea',
 'own idea / reading question':'own idea',
 'self-flagged / unpursued implication':'self-flagged',
 'unpursued implication / reading question':'reading question',
}.items(): lf=lf.replace('**Kind:** '+a+'.','**Kind:** '+b+'.')

def replace_body(text,key,new):
 pattern=rf'(### {key} —.*?\n\n)(.*?)(?=\n\n### |\Z)'
 m=re.search(pattern,text,re.S)
 if not m: raise ValueError(key)
 old=m[2]
 meta,body=old.split('\n\n',1)
 return text[:m.start(2)]+meta+'\n\n'+new.strip()+text[m.end(2):]

lf=replace_body(lf,'LF03',r'''**Confidence: high**, because if \(I=C_2\) and \(\varepsilon\) is its nontrivial one-dimensional character over a characteristic-zero field, then \(\varepsilon^I=0\) but \((\varepsilon\otimes\varepsilon)^I=1\).
Thus the additive map of representation groups is neither generally a ring map nor a faithful tensor fibre functor, although it respects dual classes.
This **differs from** CT 16/049's conditional semisimplicity and CT 47/004's explicit convolution–tensor calculation; it **adds** a separating example to **MPL_7_061-072+8_001-078 Scan 061 (§66)**, internal T.01, whose first-pass lead keeps exactness, faithfulness and tensor compatibility separate.
It supports the additivity clause of Hua **60-inertia-average-duality**, while supplying no motive-category construction for **WG2 §2.4 #3**.''')

lf=replace_body(lf,'LF07',r'''**Confidence: high under two explicit premises:** on051 interpret \(E_\eta(x)=E^I\) as in LF05, and require the stated additivity of \(\mu_x\) on the local continuous \(D\)-representation category, not merely on globally arising exact sequences.
The \(D\)-stable filtration of039–043 then has \(U\)-trivial factors \(S\), for which \(S^\natural=S^I\), \(\alpha(S)=\alpha(S^\vee)=0\), and hence \(\mu(S)=0\); additivity gives \(\mu(E)=0\) in \(K_0(D/I)\).
The local scope is justified under049's usual cohomological interpretation by \(\mu(E)=(E^\vee)^\natural(1-\mathbf Q_\ell(1))+[R\Gamma(I,E^\vee)](1)\), whose two summands are additive, with \([R\Gamma(I,S)]=[S^I]-[S^I(-1)]\) on finite-inertia factors.
This **adds** a conditional consistency test absent from CT and qualifies any nonzero-correction interpretation of Hua **60-inertia-average-duality**; it is neither a novelty claim nor evidence that the author explicitly withdrew \(\mu\).''')

lf=replace_body(lf,'LF08',r'''**Confidence: high**, by the tame two-dimensional model with geometric Frobenius \(F=\operatorname{diag}(Q_x^{-1},1)\), \(N(e_2)=e_1\), \(N(e_1)=0\), and \(Q_x=|k(x)|\): \(E^\natural=[\mathbf Q_\ell(1)]+[\mathbf Q_\ell]\), \(E^I=[\mathbf Q_\ell(1)]\), \(\alpha(E)=[\mathbf Q_\ell]\), and \(\alpha(E^\vee)=[\mathbf Q_\ell(-1)]\), so \(\mu(E)=0\) although \(\alpha\) is not additive on its filtration.
More generally, after taking finite-inertia invariants of the Weil–Deligne representation, put \(K=\ker N\) and \(C=V/NV\) with their ordinary Frobenius actions; the equivariant map \(N:V\to V(-1)\) has categorical cokernel \(C(-1)\), giving \([K](1)-[C]=[V](1)-[V]\) and, on dualizing, the same cancellation of \(\mu\).
This **adds** a diagnostic example to Hua **60-inertia-average-duality** and **differs from** CT 16/049's semisimple correspondence setting; Deligne (1973, Theorem 8.2 and §10.7) supplies the later local framework, not evidence that the manuscript executed this check.''')

lf=lf.replace('**WG2 §2.4 #3**, **WG H9**, **WG2 §2.3 #12**','**MPL_15_195-228+18_002-017 B03**, **WG H9**, **WG2 §2.3 #12**')
lf=lf.replace('Deligne (1973, §10.6, p.583) is a published comparison for the !/* duality.', 'Deligne (1973, §10.6, p.583) is a published comparison for the !/* duality, and the Stacks Project Authors (n.d., Tag09XP) provide the local-cohomology triangle with its cohomological grading.')

# Standardize bibliographic citations and distinguish hypotheses from typography.
alg=alg.replace('Stacks Project Authors, 2026','Stacks Project Authors, n.d.').replace('Stacks Project Authors,2026','Stacks Project Authors, n.d.')
alg=alg.replace('Stacks Tags07Z8 and07ZA','the Stacks Project Authors (n.d., Tags07Z8 and07ZA)')
alg=alg.replace('Stacks Tags07ZA and0AUW','the Stacks Project Authors, n.d., Tags07ZA and0AUW')
alg=alg.replace('Stacks Tag0EB9, Lemma15.24.7','the Stacks Project Authors (n.d., Tag0EB9, Lemma15.24.7)')
alg=alg.replace('Stacks Tags0AVB–0AVC','The Stacks Project Authors (n.d., Tags0AVB–0AVC)')
alg=alg.replace('Stacks Tag0AUW','the Stacks Project Authors (n.d., Tag0AUW)')
alg=alg.replace('Stacks Tag0BVZ','the Stacks Project Authors (n.d., Tag0BVZ)')
alg=alg.replace('**Kind:** reading question; own idea (counterexample).','**Kind:** own idea (counterexample).')
alg=alg.replace('**Kind:** own idea (construction); reading question for “corps des fractions \\(K\\) de \\(L\\)”.','**Kind:** own idea (construction).')
alg=alg.replace('**Kind:** unproved claim (exercise); unpursued implication.','**Kind:** unproved claim (exercise).')
alg=alg.replace('Relation:** supplies the concrete example promised on046;', 'Relation:** adds the concrete example promised on046;')
alg=alg.replace('If its source is reflexive, comparing it to the reflexive hull of \\(\\operatorname{End}(E)\\) makes evaluation surjective,', 'If its source is reflexive, the induced isomorphism with \\(\\operatorname{End}(E)^{**}\\), together with the injection of the torsion-free \\(\\operatorname{End}(E)\\) into that hull, makes evaluation surjective,')

scope=r'''## Scope of this return and the supplied plans

The selected handwritten pages substantiate the README's **L-function** heading through local averaging (037–047), virtual duality and determinants (049–059), boundary cohomology (061), and restricted rational normalizations (063–069). They contain no height-pairing calculation, local-symbol formula, construction of motives from Lefschetz rings, or descent theorem for a fibre functor over a field extension; the 18 interleaved algebra typescripts have their own source pagination and must be assessed separately.

| Supplied plan or claim | Status supplied | What these scans contribute |
|---|---|---|
| WG2 §2.4 #3; README's S16 fibre-functor question | Unchecked planning questions | 60/041 gives an exact additive operation; LF03 shows why that does not supply the required tensor fibre functor or motive category. No standard-conjecture lettering is fixed here. |
| WG H9; WG2 §2.3 #12 | Unchecked hunch / plan | LF09 separates purity from self-duality and polarization; no height or Mordell–Weil formula is proved. |
| WG2 §2.3 #2; WG2 §6. #9 | Unchecked plans | No universal Lefschetz-algebra calculation or integral-operator computation is present. |
| WG2 §2.3 #7 | Unchecked plan | Exact finite-group invariants and a virtual filtration do not establish semisimplicity of motives. |
| WG2 §2.2 #4 | Unchecked plan | No extension of hyperplane-section induction is supplied. |
| LM7 E.23 | Open, the prior return's claim | No image or fibre of an arithmetic section map is computed by the local linear representation argument. |
| LM7_PUSH D.44 | Proved in the register, with its expressly limited referee statement | The modular-descent problem is separate; no part is re-proved or used to validate the present formulas. |
| Hua, findings register, 60-inertia-average-duality | AI-produced conjecture, unsearched; intake “new to us” | Directly assessed in LF01–LF16 and the dedicated comparison below; the supplied excerpt is truncated. |

For abbreviated first-pass IDs in the register below, **M03, P09, P14** mean the entries in **MPL_15_195-228+18_002-017**, and all such labels retain the supplied first-pass/lead status. “Adds” always means relative to the supplied context, not historical novelty. Search queries in each item were run against CT, CN and RESULTS_STATE, with hits and archive locators recorded in `records/research_context_search.json`; a broad keyword hit is not by itself a mathematical precedent.

'''

main=intro+scope+'## Research register I — Local representations, duality and L-functions\n\n'+lf+'\n\n## Research register II — Reused commutative-algebra sheets\n\n'+alg+'\n\n'+standing
target.write_text(main)
print(f'Wrote {target.name}: {len(main.split())} whitespace-delimited words before supplementary items and bibliography')
