"""Index only the manually written transcription; no scan-image text recognition."""
from pathlib import Path
import re
from record_page import ROOT
notation=[
('Simplicial grading star',r'L_*,\Phi_{*k},\Psi_{*k}','002, 007–028, 037–043: star-shaped index; initial bullet candidates were rejected during the visual audit.'),
('Solid cochain degree dot',r'C^\bullet,C^\bullet_*,B^\bullet_k','040–044: filled round raised marks; in C^bullet_* the star below is a separate simplicial grading.'),
('Associated chain-complex exclamation mark',r'L^!_*,L^!_i','007–021: short upright stem with a separate dot. A prime was not substituted.'),
('Genuine prime on another object',r"L'_q,L'_*,n',m',D'",'004, 011, 015, 021–025, 035–036: slanted separate stroke. The prime in 004 is retained locally; it has not been changed merely because later pages use !.'),
('Cochain star plus exclamation',r'C^{*!}(X_*,k)','038: enlarged original shows both the star and the separate stem/dot of !; C* also occurs without ! and remains so.'),
('Alpha with degree dot',r'\alpha^\bullet','042 and 044: original enlargement confirms a filled raised dot; 042 initial prime reading is superseded. Where 043 is overstruck, bullet/prime remains in-place uncertainty.'),
('Alternative normalization sign',r'L^{\unsure{\natural|\sharp}}_n','014: local sign unresolved; not normalized to !.'),
('Half-simplicial qualifier',r'\frac12\text{ simplicial}','002, 004, 008, 028, 037, 041: visible fraction retained; in 028 the provisional k was rejected.'),
('Boundary-perfection prefix',r'\partial\text{-}','Title terminology and 009, 013–015, 028, 037–041: curled partial sign, separate from differential d.'),
('Capital Greek generators',r'\Phi,\Psi,\Omega','002–028: shapes distinguished locally; uncertainty remains in the very faded final diagram of 004.'),
('Exterior, divided and symmetric powers',r'\Lambda^i,\Gamma^i,\operatorname{Sym}^i','002–013, 028, 038: Γ with right-angle upper stroke differs from the looped diagram-type letter below.'),
('Looped diagram-type letter',r'\unsure{\mathcal{T}|\tau},\unsure{\mathcal{T}|\tau}\prime','032–034: a looped capital-like T is preferred; tau is retained as an explicit alphabet alternative. A true prime follows selected occurrences; one prime in 033 remains doubtful.'),
('Differential operator T',r'T_*\wedge','021, 041: ordinary capital T and wedge; not silently identified with the script diagram-type letter.'),
('Ornate ambient-category S',r'\unsure{\mathcal{S}|S}','036–037: looped two-lobed form; alphabet remains uncertain. Superscript opposite and subscript ab are retained separately.'),
('Hand-added script A in typescript',r'\mathcal A','003: distinguished from the Roman A used for a subcategory later.'),
('Plain typed coefficient letters',r'R,Z','005: ordinary typewritten letters; not silently changed to blackboard bold.'),
('Ambiguous additivity coefficient',r'\unsure{k|\mathbf Z}\text{-}add','030, 034–037: oblique stem and low hook; k preferred consistently from ink, Z retained. This is not a contextual assertion that a base ring was supplied.'),
('Upper/lower coefficient letters',r'k,K,k_0','015, 035: upper K, lower k, and small subscript 0 distinguished; the later change from k_0 to k is preserved.'),
('Rank and multiplicity letters',r'\rho(n),\mu_i,\nu_j,\beta_{i\ell}','011–019: Greek letters; spellings rg and rang are not lexically standardized.'),
('Homotopy and Euler signs',r'\pi_i,\chi','002 onward, especially 013, 016–019: local unresolved marks remain in-place doubts.'),
('Point and divisor alphabets',r'\mathfrak p,\unsure{\mathfrak P}','015–016: alphabet where faint remains a reading question, not supplied from the mathematical role.'),
('Cycles, boundaries and saturation',r'Z_i,B_i,\overline P_i','017–018: capital shapes, lower indices, and bars retained.'),
('Elementary torsion objects',r'\Phi(i,n),\Phi(i,\ell)','016–027: scalar n and divisor ell are not interchanged globally; index shifts that appear inconsistent are preserved.'),
('Local generator abbreviations',r'\Phi^i,\Psi^i,\Phi_*^{(i)},\Psi_*^{(i)}','023 onward: superscripts and parenthesized superscripts retained rather than expanded into exterior powers everywhere.'),
('Extension-class operations',r'e_{i,n},q^*,p_*','023–025: star placement retained. The scalar identities and ratio on 024 have unresolved readings; no algebraic correction was imposed.'),
('Presheaf hats and opposite circles',r'\widehat C,\widehat A,\widehat{A^\circ},(\widehat{A^\circ})^\circ','029–037: hats and circles handled independently; plain C versus D remains uncertain in two places on 033.'),
('Restriction/evaluation letters',r'\rho,\omega,\alpha,\beta','029–044: locally written letters retained; rho/r/f and some overwritten alpha/beta decorations remain doubts.'),
('Underlined functor-category Hom',r'\underline{\operatorname{Hom}}','029–044: underline is visible; Hom with a cochain dot on 044 is not rewritten as derived Hom.'),
('Limits and colimits',r'\varprojlim,\varinjlim','029–034: leftward/rightward arrows checked from the source, not inferred from desired variance.'),
('Subset and cap-shaped inclusion signs',r'\subset,\cap','017, 033, 035: bare signs represented with phantom TikZ arrows where appropriate; the hooked downward arrow on 036 remains an arrow.'),
('Plain dashes versus arrows',r'\arrow[r,dash]','022–026: a line without a visible head is retained. The overwritten identity arrow on 042 shows heads at both ends; the lower arrow on 044 remains uncertain and cancelled.'),
('Tensor subscript',r'F\underset{C}{\otimes}G','035: rounded C-like subscript kept; not changed to an expected A.'),
('Duality marker',r'M^\vee','043: vee in the module-dual construction, separate from primes, stars, and opposite circles.'),
('Paired double quotation marks',r"``...''",'010, 013, 030, 035, 038, 040, 044: two backticks and two apostrophes; no guillemets were substituted.'),
('Ditto strokes',r"\overset{\text{''}}{\alpha^\bullet(x)}",'044: two short vertical strokes above the repeated expression, with no added equals sign before that line.'),
('Underline and double underline',r'\uline{...},\uuline{...}','Distinguished where visible; author underlining is separate from editorial uncertainty.'),
('Deletion and insertion layers',r'\deleted{...},\inserted{...},\margin{...}','Kept even for mathematically superseded statements; nested deletions occur inside the large cancelled draft on 041.'),
('Pagination',r'\scanpage{N}; % archive foliation: n','42 retained PDF scans 002–044 excluding 006; archive foliation is not author pagination. No secure author sheet number was identified.'),
]
glossary=[
('ab.','abélien / abélienne / abéliens','Agreement depends on the local noun.'),('add.; additif','additif / additive','Enrichment qualifier; no expansion in transcription.'),('assoc.','associé / associée','Context-dependent ending.'),('bil.','bilinéaire','Usually k-bil.'),('can.','canonique','Map or construction.'),('car','caractéristique','038.'),('cat.; catégor.','catégorie','Also plural categories.'),('cf.','confer; compare','Cross-reference.'),('ch.; coh.','chaîne, cohomologie, or cohomologique','Especially doubtful ch. nulle on 042; no expansion claimed as certain.'),('coeff.','coefficient(s)','Context-dependent.'),('com.; comm.; commut.','commutatif / commutative','Some short forms remain uncertain in the ink.'),('comb.','combinaison(s)','Usually combinaison linéaire.'),('comp.','composante(s), complexe(s), or composition(s)','Meaning varies locally.'),('cond°','condition','Superscript-like terminal mark retained.'),('conséq.','conséquence','Logical continuation.'),('controv.; cov.','contravariant / covariant','The written form controv. is preserved.'),('cor.; Cor.','corollaire','Heading or reference.'),('cqfd.','ce qu’il fallait démontrer','Closing abbreviation.'),('déf.; Déf.','définition, défini, or définie','The parenthesis on 028 is not securely expanded.'),('Dém.','démonstration','Heading.'),('deg; degr','degré','Position labels in displayed complexes.'),('diff.','différentiel / différentielle','Usually opérateur différentiel.'),('endom.','endomorphisme(s)','031.'),('ens','ensemble','032 replacement of catégories pleines.'),('Ens','ensembles','Category name in the functor formulas.'),('épi.','épimorphisme','Contextual expansion.'),('équiv.','équivalence','No claim of strict equality implied.'),('evt.','éventuellement','Only a candidate for the insertion on 038; est remains an alternative.'),('Ex; Ex.; ex.','exemple','Numbered examples on 041–043.'),('ext.','extension','Sequences and extension classes.'),('fact.','facteur','Contextual expansion.'),('fid.','fidèle','Normally with pl.'),('fonct.','foncteur / fonctoriel','Context-dependent.'),('g.','gauche','Sides of module structures.'),('génér.','générateur(s)','Contextual expansion.'),('hom.','homomorphisme','Not expanded into morphisme in the transcription.'),('i.e.','id est; c’est-à-dire','Latin abbreviation retained.'),('id','identité','Operator or map.'),('isom.','isomorphe / isomorphisme','015 ending is isom., not homotopie.'),('Ker','noyau','044 insertion stable par Ker.'),('lin.','linéaire','Often k-lin.'),('nb','nombre','Finiteness qualification.'),('néc.','nécessairement','029 insertion.'),('noeth.','noethérien','014 finiteness discussion.'),('non dég','non dégénérées','038 cochain qualifier; expansion only here.'),('obj.','objet(s)','Category language.'),('Ob','objets','Object collection notation.'),('op.','opérateur','In op. diff.'),('p.d.','puissances divisées','039 comparison and reconstruction question.'),('p.ex.','par exemple','Examples.'),('parf.','parfait / parfaits','Before insertion parfaits on 038.'),('pl.','pleinement / pleine','pl. fidèle or sous-catégorie pleine.'),('pol.','polynomial / polynomiale','Rank discussion.'),('pr.','premier, près, or projectif','Short form requires local reading; no global expansion.'),('proj.','projectif / projectifs','Module qualifications.'),('prop.; Prop.','proposition','Numbered claims.'),('prés.','présentation','044 prés. finie.'),('r.f.','rang fini','Alternative to t.f. in faint passages; not substituted for the audited t.f. readings.'),('repr.; représ.','représentable, représenté, or représentant','Context-dependent.'),('resp.','respectivement','Alternating general/additive cases.'),('rest.','restriction','Functor labels.'),('rg','rang','Separate from written rang.'),('ssi','si et seulement si','014.'),('str.; strict.','strictement / strict','Qualification of special/perfect objects.'),('struct.','structure','Mathematical structure.'),('suff.','suffisant / suffisamment','Context-dependent.'),('supp.','supposons / supposé','Context-dependent.'),('suppl.','supplémentaire','038–039.'),('t.f.','type fini','Audited against r.f. alternatives.'),('t.q.','tel que','Logical qualifier.'),('Th.','théorème','Heading.'),('tot.','total','Contextual expansion.'),('triv.','trivial / trivialement','Contextual expansion.'),('tt; ttes','tout / toute; toutes','042 admitted direct-factor condition.'),('unit.','unitaire','Contextual expansion.')]
def cell(s):return str(s).replace('|',r'\|').replace('\n',' ')
def arg_at(s,start):
 depth=1;i=start
 while i<len(s):
  if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
  elif s[i]=='}' and (i==0 or s[i-1]!='\\'):
   depth-=1
   if not depth:return s[start:i],i
  i+=1
 raise ValueError('Unbalanced macro argument')
def split_alternatives(s):
 depth=0;parts=['']
 for c in s:
  if c=='{':depth+=1
  elif c=='}':depth-=1
  if c=='|' and depth==0:parts.append('')
  else:parts[-1]+=c
 return parts
lines=['# Notation table and doubts','','## Notation table — final pre-context readings','','This table records the final visual decisions. Earlier candidates survive in the working records as reading history; they are not competing authoritative transcriptions. Unresolved alphabet and sign distinctions remain marked in the page files.','','| Recurring sign or convention | LaTeX | Scans and visual cautions |','|---|---|---|']
for a,b,c in notation:lines.append('| '+cell(a)+' | `'+cell(b)+'` | '+cell(c)+' |')
lines+=['','## Complete in-place doubt index','','The table below indexes every `\\unsure{...}` and `\\illegible{n}` occurrence in the final page files, including nested and repeated occurrences. “Line” is the line of that individual page’s LaTeX source, supplied as a reproducible location; it is only an approximate guide to the handwritten line because displays, diagrams, margins and TikZ drawings occupy different numbers of source lines. The first candidate is the reading retained from the ink, not a mathematical correction; confidence is a qualitative assessment, not an error-rate estimate.','','| File | Scan page | Approximate line / place | Reading | Alternatives | Confidence |','|---|---|---|---|---|---|']
counts={'unsure':0,'illegible':0}
for p in sorted((ROOT/'pages').glob('*.tex')):
 scan=int(re.search(r'scan(\d+)',p.name)[1]);s=p.read_text()
 for m in re.finditer(r'\\(unsure|illegible)\{',s):
  kind=m[1];a,end=arg_at(s,m.end());lineno=s[:m.start()].count('\n')+1;counts[kind]+=1
  if kind=='illegible':reading=f'{a} physically unreadable word(s), estimated';alts='No secure reading after visual enlargement';conf='low'
  else:
   parts=split_alternatives(a);reading='`'+cell(parts[0])+'`';alts=' / '.join('`'+cell(v)+'`' for v in parts[1:]) if len(parts)>1 else 'No secure alternative';conf='low'
   if any(t in a for t in [r'\mathcal{T}',r'\mathcal{S}',r'\mathrm{S}_s','correspond|corresponde','Transformant|Transformons','groupes|grps','isom.','linéariser|généraliser','platonisme|platitudes','structure|strictement','reprenons|repartons']):conf='medium'
  lines.append(f'| 137 | {scan:03} | Source line {lineno} | {reading} | {alts} | {conf} |')
lines+=['','## Additional visual cautions','','| File | Scan page | Approximate line / place | Reading | Alternatives | Confidence |','|---|---|---|---|---|---|',
'| 137 | 040 | Left margin | Manual TikZ reconstruction of pen exercises and staff-relative positions | Individual curves are approximations; crop-candidate comment retained | low |',
'| 137 | 043 | Left/lower margin | Manual TikZ reconstruction of pen exercises and enclosing curve | Individual curves are approximations; crop-candidate comment retained | low |',
'| 137 | 042 | Central complex, identity row | Visible heads at both ends | Overwritten direction; the ink does not justify silently choosing the expected direction | medium |',
'| 137 | 044 | End of final line | et les deux | No continuation is supplied by this package | high |',
'','## Abbreviations met — expansions only in this list','','The expansions below are editorial aids, never additions to the diplomatic transcription. An uncertain reading of an abbreviation does not become certain because an expansion is plausible.','','| Written abbreviation | Proposed expansion | Qualification |','|---|---|---|']
for row in glossary:lines.append('| '+' | '.join(cell(v) for v in row)+' |')
lines+=['','## Legibility and limits of confidence','',
'The retained set contains 42 scans: 002–005 and 007–044. All whole images and supplied halves were visually read in the first pass, and every page was visually audited again by the same reader. No OCR or image-based text-recognition system was used. Contrast adjustments and crops were aids to manual inspection, not replacement texts.',
'',
'The two reused typewritten leaves (003 and 005) are substantially easier to read than the pencil and pale-ink notes. Confidence is lowest in the middle and marginal writing of 002, the cancellations and final diagram on 004, the marginal note on 015, overwritten indices and scalar expressions on 023–025, the small type/coefficient signs on 030–037, and the struck or very faint wording on 040–044. Staff ruling frequently intersects letter bodies, primes, exclamation dots, and arrowheads; enlargement cannot recover ink absent from the supplied image.',
'',
'Every physically unreadable word-count marker is retained in place; these estimated counts are not recovered text. Uncertain formulas use best-reading alternatives rather than illegible-word markers. The drawings on 040 and 043 are manual TikZ approximations, explicitly identified by the requested crop-candidate comments. Their inclusion records the visible drawing content but does not warrant a claim of exact graphical facsimile.',
'',
'This is a complete page-by-page transcription attempt with explicit residual uncertainty, not a claim of error-free decipherment. In particular, the faint parenthesis on 012, the scalar ratios on 024, and the pairing at the foot of 043 should not support an argument without consulting the scans. Archive foliation is recorded only in comments; no author pagination was securely identified. The last supplied page ends mid-sentence.',
'',f'Final index counts: {counts["unsure"]} uncertainty-macro occurrences and {counts["illegible"]} unreadable-word-count occurrences. These counts measure editorial markers, not independent manuscript errors.']
(ROOT/'MPL_137_002-044_doubts.md').write_text('\n'.join(lines)+'\n')
print(counts)
