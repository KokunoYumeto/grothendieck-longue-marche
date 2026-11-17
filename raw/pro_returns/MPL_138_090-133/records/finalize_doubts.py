"""Reconcile authored apparatus after the primary reader's visual audit.

This edits reading records and the doubts document only, never page TeX.
Run append_doubt_locators.py afterwards to append the exact source locators.
"""
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT))
from records.record_page import rebuild_doubts, utc

updates={
 93:{'table right third row':('les commutants','non; commutatifs; the first-pass enc. reading was rejected in the audit','low')},
 94:{'diagram top left':('mathcal C ≃','mathcal C =; the script category symbol is distinct from a numeral','low')},
 95:{'deleted expression':('n^chi(sigma)','gamma in the exponent argument; both remain locally marked','low')},
 96:{'triangle upper right':('deleted t before tilde pi','small cancelled stroke, read tentatively as t','low')},
 106:{'II, rho_s row5':('4','2; overwritten index compared at enlarged scale','low')},
 123:{'last NB':('de = nature','nature uncertain; the equals-shaped abbreviation is retained literally, not expanded to même','low'),
      'last line':('pas de somm.-gén.; cf] et 1','somm. qui; si] et 1; unresolved reference, with no editorial ellipsis replacing ink','low')},
 125:{'11–13':('aucune des cette carte ne peut contenir au plus qu’un seul','dites cartes; the wording remains uncertain and is not grammatically repaired','low')},
 127:{'middle right':('1/(2−1/2)','1/(2−1/z); the small denominator is visually ambiguous, so the formula is not algebraically corrected','low')},
 128:{'1':('⇐','⇔; enlarged crop has no secure right arrowhead','medium')},
 130:{'Möbius formula':('az−b','az+b; enlarged crop favors a horizontal minus','medium')},
 132:{'d)':('en les pts au dessus de 1 (sauf peut-être en 1)','faint and partially stained qualifier, restored during audit','low')},
}
additions={
 90:[('diagram 2 / question','mathcal T','angular Gamma is a different symbol; the Teichmüller letter has a curved stem','medium')],
 111:[('opening discriminant arithmetic','raised 2 after 32','small raised mark adjoining the parenthesis; retained with doubt','low')],
 125:[('upper line 2 insertion','définissent','surviving rewrite under the cancelled soient définis','low'),('condition a','subscript X on A','small dark subscript, possibly crossed','low')],
 132:[('condition a, representative tuple','K′_C, S′_C','K′_X, S′_X; both small subscripts retain local alternatives','low')],
}
for scan,mapping in updates.items():
 p=ROOT/'records'/f'page{scan:03d}_reading.json'; data=json.loads(p.read_text())
 for row in data['doubts']:
  if row[0] in mapping:
   # Scan123 has two entries labelled last NB; change only the obsolete de même.
   if scan==123 and row[0]=='last NB' and row[1]!='de même':continue
   row[1:]=list(mapping[row[0]])
 p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
for scan,rows in additions.items():
 p=ROOT/'records'/f'page{scan:03d}_reading.json'; data=json.loads(p.read_text())
 for row in rows:
  if list(row) not in data['doubts']:data['doubts'].append(list(row))
 p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
# The rejected reading enc. on93 is not an abbreviation met in the frozen text.
p=ROOT/'records/page093_reading.json'; data=json.loads(p.read_text())
data['abbreviations']=[r for r in data['abbreviations'] if r[0]!='enc.']
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
extra_abbreviations={
 97:[('totᵗ (uncertain)','totalement')],
 98:[('etc.','et cetera'),('Cartcomb','cartes combinatoires'),('Précart','précartes')],
 101:[('gr.','groupe'),('P. ex.','par exemple')],
 102:[('isom.','isomorphisme'),('op.','opération(s)')],
 124:[('top.','topologique(s)')],
 125:[('comp. conn.','composantes connexes'),('topolog.','topologiques')],
 126:[('Th.','théorème'),('ts','tous'),('mil.','milieu(x)'),('combin.','combinatoire'),('tr.','trivialement'),('id','identité')],
 129:[('th.','théorème')],
 130:[('él.','éléments'),('dim','dimension'),('comp.','composante')],
 131:[('hol.','holomorphe(s)')],
 132:[('tte','toute'),('comp. (cancelled)','complexes')],
}
for scan,rows in extra_abbreviations.items():
 p=ROOT/'records'/f'page{scan:03d}_reading.json'; data=json.loads(p.read_text())
 for row in rows:
  if list(row) not in data['abbreviations']:data['abbreviations'].append(list(row))
 p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
rebuild_doubts()
p=ROOT/'MPL_138_090-133_doubts.md'; s=p.read_text()
table=r'''## Package notation table

The primary reader compared recurring signs across the whole package before the transcription was frozen. Differences supported by the ink remain differences; uncertain alternatives are not regularized to the expected mathematics. This table records notation, not a mathematical identification of the objects.

| Manuscript sign | LaTeX rendering | Scans and comparison |
|---|---|---|
| Curved script T / angular Gamma | `\mathcal T`, `\Gamma` | 90; compared with the arithmetic Gamma on94–96,103–104. The two letters remain distinct. |
| Hats, bars and tildes | `\widehat B`, `\overline B`, `\widetilde\pi` | 90,93–96: flat bars and wavy tildes are not exchanged for completion hats. |
| Raised open circle | `^\circ` | 90 orientation kernels;122–126 isotopy groups. Same sign, distinct local meanings. |
| Script cartographic group | `\mathcal G_2^\circ` | 99,123; rounded script capital, subscript2 and circle. |
| Capital/lowercase Galois and symmetry letters | `\Gamma`, `\gamma` | 99–105: plain capital arithmetic group versus looped lowercase symmetry group. |
| Script pre-map and moduli letters | `\mathcal C_0`, `M_{\mathcal C_0}`, `C^\alpha_{\mathcal C_0}` | 98–104; the font distinction and all indices are retained. |
| Contracted product | `\wedge_\Gamma`, `\wedge_\pi` | 93–96: the subscript actually read is retained; no correction of its mathematical role. |
| Inertia character / generator | `\chi_i`, `l_i` | 93–96: thin lowercase l is distinguished from1. A pi-shaped character domain on95 has a Gamma alternative locally. |
| Rho and sigma generators | `\rho_s`, `\rho_f`, `\sigma` | 102,106; subscripts s/f and1/2 are kept separately. |
| Indexed rays | `r_i` | 106; not replaced by rho. |
| Epsilon and eta | `\varepsilon`, `\eta` | 91;117,119 have explicit eta/epsilon alternatives where the strokes do not settle the choice. |
| Mathematical primes | `\alpha'_i`, `\pi'`, `f'`, `K'`, `S'`, `\varphi'` | 96,104–112,122–132: short primes checked against exclamation-like strokes. |
| Factorials / standalone exclamations | `a_n!`, `\delta!`, `!` | 99–103 factorials;116 uncertain standalone exclamation after Z₂;117 bracket label. No secure exclamation-mark exponent was identified in this package. |
| Numbered examples with raised marks | `\unsure{3'\vert3^a}`, `\unsure{3''\vert3^b}` | 104: these examples retain prime/letter alternatives; not silently made factorials or exclamation exponents. In the actual TeX, the alternatives are separated by a literal vertical bar. |
| Angular superscript on F | `F^\natural` | 122–123: enlarged occurrences compared side by side. First occurrence retains `\natural`/`\sharp` doubt; the repeated sign is rendered consistently as natural. |
| Direct-limit arrow | `\varinjlim` | 123: the visible arrow points right. The mathematical variance is discussed only in research notes. |
| Power-set P versus polynomial P | `\mathcal P`, `P` | 123 versus107–112: different drawn forms and distinct typography retained. |
| Ornate symmetric-group S | `\mathfrak S_n` | 104–105,115,119; distinguished from the plain surface/vertex letter S. |
| Double-stroked integers and fields | `\mathbb Z`, `\mathbb Q`, `\mathbb R`, `\mathbb C` | Throughout;130 real coefficients and C-looking group labels are not normalized to one field. |
| Stacked passport entries | `smallmatrix` arrays | 114–120: vertical lists, not fractions; multiplicities remain subscripts. |
| Coordinate labels and multiplicities | `\underline0`, `\underline1`, `\underline\infty` plus separate integers | 104: underlined coordinates are kept separate from local degrees. |
| Underlined conjugation c | `\uline c` | 123: the underline belongs to the letter. |
| Quotient/reduction marks | `_{\mathrm{réd}}`, `_{\mathrm{ét}}` | 100; overwritten/cancelled variants carry local doubt. |
| Delta polynomial | `\delta(c)` | 111–112; discriminant label and printed polynomial retained without arithmetic repair. |
| Phi and psi | `\varphi`, `\psi` | 112,124–132: closed-loop phi versus psi; cancelled exchanges kept. |
| Greek operation Omega | `\Omega` | 122–132, including above-line132 insertion. |
| Headless lines versus arrows | TikZ `no head`/`dash`; local `\unsure` | 90,93–96,129: no arrowhead supplied merely to complete an expected diagram. |
| Inclusions and inequalities | `\subset`, `\supset`, `\leq`, `\geq` | 91,93–96,124–125,128,131–132: direction read from each occurrence, including131 n≥2. |
| Double quotation marks | two backticks and two apostrophes | 99,121–123,132–133; retained consistently, including the typed film title. |
| Equals-shaped abbreviation | `$=$` | 123, final NB: retained literally in “de = nature”; not expanded in transcription. |
| Manuscript numbering / archive foliation | `\mspage` reserved; `% archive foliation:` for later numbers | No secure authorial page number identified; faint98 mark remains a reading doubt. |

'''
start=s.index('## Package notation table'); end=s.index('## Reading doubts')
s=s[:start]+table+s[end:]
s=s.replace('The final assessment follows the full audit.',
'''All43 retained scans received a first transcription pass and a separate second visual comparison by the same primary reader; no OCR or parallel transcription was used. The earlier reading table is an authored selection of difficult places; the exhaustive locator supplement below covers every uncertainty macro in the final page files.

The least secure passages are the overlapped cancellations and margin on93–100, the short heading on97, the numerical and polynomial overwriting on106–112, ink-obscured passports on120, the marginal and final phrases on122–125, and the stained revisions on132. Scan127 mixes densely placed calculations, graphs and pictorial doodles; the TikZ drawings are hand-built approximations of their visible geometry, and fine incidental pen strokes are less trustworthy than the graph connectivity and written labels. The typed sheets106,110,133 are more legible, apart from transfer marks and signatures.

Local uncertainty remains after audit. Mathematical plausibility has not been treated as evidence for a reading: examples include the discriminant roots on111, the rightward limit arrow on123, S¹ on125, the small denominator on127, field labels on130, and n≥2 on131. Any later mathematical correction or context-suggested reading belongs only in the research notes. No claim of error-free transcription or pixel-exact drawing reproduction is made.''')
p.write_text(s)
with (ROOT/'progress.log').open('a') as f:f.write('notation and authored doubts reconciled '+utc()+'\n')
print('Authored doubts, abbreviations and notation table reconciled.')
