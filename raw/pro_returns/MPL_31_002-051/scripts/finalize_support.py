from pathlib import Path
import sys,json,re,shutil
base=Path('/workspace/scratch/74077fe5e995/MPL_31_002-051_work')
sys.path.insert(0,str(base/'scripts'))
from save_page import extract_macros,rebuild,utc
notation=r'''| Visible recurring form | LaTeX treatment | Evidence / caution after the complete second reading |
|---|---|---|
| Cohomological-dimension notation | `\mathrm{cd}_p`, `\mathrm{cd}'_p` | 003–009: the short exponent strokes in the body are primes. Cover 002 has a vertical stroke with a lower dot and remains `\unsure{!\|'}'; its lower letter remains `\unsure{p\|\ell}`. Each occurrence was checked individually. |
| Étale, multiplicative, radicial and additive qualifiers | `^{\text{ét}}`, `^{\text{t.m.}}`, `^{\substack{\text{rad}\\\text{add}}}` | 003, 005, 009. The source abbreviations and their placement are retained. |
| Primes and repeated primes | `G'`, `G''`, `k'`, `X'` | Throughout. The doubtful superscript in 051 Corollary 1 remains `\unsure{a\|'}`; the apparent prime on the final K remains a local doubt. |
| Superscript zero and subscript zero | `G^0`, `G_0`, `G_k^0`, `G_k^{0S}` | 003, 045, 048. Placement is read locally; these forms have not been interchanged. |
| Greek group letters | `\mu_p`, `\alpha_p`, `G_m`, `G_a` | 003–009, 047–051. Source subscripts are retained; the overwritten 051 coefficient is `\unsure{U_m\|G_m}`. |
| Integer letters with a visible doubled stroke | `\mathbb Z` | 005, 022, 025, 047, 051. Both Z/l occurrences on 047 have a doubled diagonal in the enlargements. The heavy letter on 020 remains `\unsure{\mathbb Z\|\mathbf Z}`. |
| Plain handwritten integer letter | `Z` | 042–043 and 045 retain the visible plain letter, including the group-ring expressions and Z_2. No additional stroke has been supplied from its mathematical use. |
| Natural-number exponent in the module calculation | `\unsure{\mathbb N\|\mathbf N}` | 011 and 017, compared in the second reading; the dark/doubled form does not securely choose between these alphabets. |
| Typed underlined integer/natural letters | `\underline Z`, `\underline{\underline N}`, `\underline{\underline Z}` | 006, 016, 028. The two separate typed underline strokes on 028 are retained explicitly. |
| Doubled rational and real field letters | `\mathbb Q`, `\mathbb R` | 020–023. The C in X(C) remains plain where the ink has no doubled stroke. |
| Gothic ideal and looping Galois-action letter | `\mathfrak p`; `\unsure{\mathfrak g}`, `\unsure{\mathfrak g_k}` | Prime ideal in 023; tall looped action letter repeatedly checked on 047–050. The latter alphabet remains uncertain throughout. Radical notation in 042 retains its local r/rad doubt. |
| Site letter with doubled stem | `\mathbb T` or `\unsure{\mathbb T\|T}` | 025, 029. The live Ob occurrence on 025 has a clear doubled stem; other compressed occurrences retain doubt. |
| Cursive collection and covering letters | `\mathcal M`, `\mathcal U`, `\mathcal V` | 025–031. The covering letter is compressed on 031, where each occurrence is `\unsure{\mathcal U\|U}`. These local doubts are kept beside the clear calligraphic examples. |
| Plain, checked, barred and underlined cohomology H | `H^i`, `\check H^i`, `\overline H^i`, `\underline H^i` | Checks on 025; bars on 029/031; underlines on 048. Bare H on 027 and other positions remains bare. |
| Hatted cohomology H | `\widehat H` | 042–044, 051. The final H under the overbar on 044 is plain as written; the overwritten hat in 051 Corollary 2 is doubtful. |
| Spectral-sequence term and degree | `E_2^{pq}`, `H^{p+q}`, local `\unsure` forms | 027, 031. The uncertain E subscript and degree strokes are registered individually; no spectral-sequence identity supplies missing ink. |
| Direct and unspecified limits | `\varinjlim`, `\lim` | Handwritten arrow limits on 017, 027, 029, 031, 048; bare typed lim on 030/032. The index m/n on 048–049 remains doubtful at every occurrence. |
| Typed sheaf/module underlines and formal hats | `\underline O`, `\underline F`, `\underline{\operatorname{Hom}}`, `\widehat X`, `\widehat F`, `\widehat f` | Reused typed sheets, especially 026–032. Each visible underline/hat is recorded on its own object. |
| Product and bottom-bar coproduct-shaped signs | `\prod`, `\coprod` | 007–009 and 028 respectively. The symbol drawn in the typed associated-graded formulas is retained. |
| Fundamental group and path endpoints | `\pi_1`, `\partial_0`, `\partial_1` | 035–039; the first d-shaped endpoint operator on 035 remains `\unsure{d_1\|\partial_1}`. |
| Path and action-map letters | `\gamma`, `\beta`, `\lambda`, `\chi` | 035–039. Primes, minus signs and the two arguments within p(...) were checked separately. |
| Transfer, trace, norm and power-map letters | `t(G,G')`, `\operatorname{Tr}`, `T`, `N`, `\wp` | 042–045, 050–051. T is the source form on 044; overwritten labels on 043 remain doubtful. N subscripts A/bar k and A/k on 050 remain as written. |
| Single and double underlines | `\uline{…}`, `\uuline{…}` | Scope checked in every page audit. Source module underlines use standard math underlining; prose emphasis uses the requested macros. |
| Double quotation marks | two backticks and two apostrophes | 009, 014, 023, 026, 028, 043. Opening/closing source marks retained. |
| Drawn guillemets | `« … »` | 035, around mise bout à bout. |
| Arrowheads, bare connectors and inequalities | TikZ arrows, `dash`/`no head`, `\unsure{-\|\to}`, `\leq`, `\geq`, `<`, `>` | Checked against each display. Particularly uncertain connectors occur on 005/007, 042 and 045; 047 and 051 include headless strokes. The strict first bound at the foot of 020 is retained. |
| Blank typed or handwritten relation slots | spacing, unconnected objects, or an empty right-hand side | 004, 006, 030, 032 and condition c) on 047. No missing sign or term is supplied. |
| Manuscript and pencil page numbers | `\mspage{…}` | Visible numbers retained independently of scan order, including the reordered typed pagination and repeated 27 on 018. Counts and other uncertain cover numerals remain marginal marks. |
'''
(base/'records/notation.md').write_text(notation)
abbr=r'''| Written form | Proposed expansion (only in this list) | Scan / confidence |
|---|---|---|
| `cd` | dimension cohomologique | 002–009, 019–023; high |
| `car.`, `Car.` | caractéristique | 002–003, 042, 049, 051; high where the letters are clear |
| `topolog.` | topologie | 002; medium reading |
| `fppf` | fidèlement plate de présentation finie | 002; high expansion |
| `fid. plate` | fidèlement plate | 003; high |
| `comm.` | commutatif(s), commutative(s) | 003, 047; high expansion |
| `puiss.` | puissance | 003; high |
| `t. un.` | type unipotent | 003; high |
| `t. multiplicatif`, `t. m.`, `t.m.` | type multiplicatif | 003, 005, 009; high |
| `ét` | étale | 003, 005; high |
| `rad`, `add` | radiciel, additif | 009; high |
| `NB`, `NB.`, `N. B.` | nota bene | 009, 023, 045; high |
| `i.e.` | id est | throughout, including 003, 031, 043; high |
| `il f. et s.` | il faut et suffit | 005, 044; high |
| `tte`, `ttes`, `tt` | toute, toutes, tout | 005, 007, 025, 029, 045, 051; high expansion, local reading doubts retained |
| `sép.` | séparable | 005; medium reading |
| `gr.` | groupe(s) | 007; high expansion |
| `hom.`, `hom` | homomorphisme | 007, 043–044, 050; high |
| `can.` | canonique | 007; medium reading |
| `épim.` | épimorphisme | 007; medium reading |
| `st.ble` | stable | 007; medium reading |
| `noeth.` | noethérien | 011; high |
| `dim` | dimension | 011, 020, 023, 044, 050; high |
| `inv.` | inversible | 015; high |
| `isom` | isomorphisme | 015; high |
| `Th.`, `Th`, `th.` | théorème | 020, 035–039, 043, 048; high |
| `pt`, `pts` | point, points | 020; high |
| `tr.` | transcendance | 020; high |
| `top.` | topologie; topologique in groupe de Galois top. | 020, 045; high |
| `resp.`, `resp`, `resp` with superscript `t` | respectivement | typed sheets, 020, 042; high |
| `suiv.` | suivantes | 022; high |
| `univ.` | universellement | 023; medium in overwritten passage |
| `Ob` | objets | 025; high |
| `ens`, `ens.`, `sous-ens` | ensemble, sous-ensemble | 025, 043–044, 048; high |
| `rec.`, `rec` | recouvrement(s) | 025, 029; high |
| `hyp.` | hypothèse(s) | 027, 044; high |
| `cqfd.`, `qfd.` | ce qu'il fallait démontrer; qu'il fallait démontrer | 027, 031; medium where overwritten |
| `cf.`, `cf` | confer, compare | 026, 028, 048; high |
| `EGA`, `E.G.A.` | Éléments de géométrie algébrique | 026, 028, 032; high |
| `Dém`, `Dém.` | démonstration | 035–039; high |
| `Déf.`, `Def` | définition | 021, 035; high |
| `im`, `Im` | image | 035–036, 045; high; case retained locally |
| `mod` | modulo | 036, 043, 051; high |
| `p` with superscript `o` | proposition | 037; medium |
| `Tr` | trace / transfert, as used locally | 042–043; high; 043 explicitly writes transfert |
| `mb.` | membre(s) | 042, 051; high |
| `inj` | injectif | 044; medium reading |
| `abs.` | absolument / absolu | 045; low, cancelled reading |
| `alg.` | algébrique; algébriquement in quasi-alg. clos | 047, 051; high |
| `déf/k`, `déf/` followed by k | défini sur k | 047, 050; high |
| `comp.` | composante | 048; high |
| `qqp` | quelque part | 048; low reading |
| `dét.`, `dét` | déterminant | 050; high where live |
| `op.` | opérée | 050; medium expansion |
| `polycop` (doubtful) | polycopié(es) | 033; low |
| `p` in cover counts | page(s) | 010, 019, 033; medium, count readings retained separately |
| `M.` | Monsieur | 019; high |
| `Univ.` | Université | 035–039 letterhead; high |
'''
(base/'records/abbreviations.md').write_text(abbr)
(base/'records/legibility.md').write_text('''All 46 retained scans were read directly in one sequence, using the whole images, both supplied halves and additional enlarged or rotated crops; no OCR was used. A second visual reading of every page was completed before any context archive was opened. The reused typescripts are often readable, but overtyping, handwritten renumbering, clipped edges and unfilled mathematical slots require care. The handwriting ranges from clear propositions to very compressed connected prose; mathematical familiarity has not been used to complete a missing term or repair a surprising statement.

The least secure material is the faint cover wording/counts (002, 010, 019, 033), the heavily overwritten additions on 012–018, the rapid prose and cancelled diagrams on 031, the cancelled formula at the foot of 036, the margins and overlapping corollary on 042, both margins and the bottom-edge formula on 043, parts of the cancelled idelic draft on 045, and overwritten coefficients/superscripts on 051. The long cancellation strokes on reused sheets 012, 014, 016 and 018 cross the main typed block; their encoding as whole-block deletion records the apparent scope, which remains less secure than the readable words. Local deletion and insertion states inside those blocks are retained separately.

Doubts are deliberately occurrence-specific. Medium means a plausible visual reading with unresolved strokes; low identifies weak wording, deeply overwritten material or physically obscured words. A high reading-confidence entry, where used, would still carry its source doubt; it would not certify the mathematical claim. The register includes every unsure/illegible occurrence in the fragments. Unreadable word counts are estimates after zoom attempts; unreadable mathematical symbols instead receive a proposed reading with unsure. Unmarked text is the reader's best direct transcription and is not a claim of error-free reading. First-pass observations are historical records; the second-audit record and final fragments show the later visual corrections.
''')
# Confidence selection describes visual weakness, not mathematical plausibility.
low_scans={33}
low_args={
 2:{'topolog.','4','1'},10:{'proobjets|protopos'},
 12:{'encore','5.11','5.14',r'\check H|\check M'},
 31:{'On a la','Car','faut le prouver pour'},
 36:{r'\pi_1(B)'},
 38:{'en'},
 42:{'Commencer','Voir ça','Voir','dans le livre de','puis au corollaire','étant premier à la','égale caractéristique','plus trivialement s\'il existe un'},
 43:{'On voit l’intérêt','On voit l\'intérêt','énoncé','ramené','dans d\'autres','termes','déterminer','un',r'$G/H$-covariance','coimage','par les relations','imposées par','Une explication par les','coefficients'},
 44:{'car','annule'},45:{'restriction','idèles','complexe|complète','ttes','abs.','quel',r'S^\infty',r'(\underline S^0)k'},
 48:{'dire qqp','dégager'},50:{'donc','G|\\Gamma'},51:{"un|d'un",r'\widehat H^i(K,G)','n\'a que','en déduit'}
}
ratings={}
for p in sorted((base/'pages').glob('*.tex')):
 n=int(re.search(r'scan(\d+)',p.name).group(1))
 for macro,arg,line in extract_macros(p.read_text()):
  if macro=='illegible' or n in low_scans or arg in low_args.get(n,set()):ratings[f'{n:03}:L{line}:{arg}']='low'
  if n in (36,38) and ('pi_1' in arg or 'p_*' in arg):ratings[f'{n:03}:L{line}:{arg}']='low'
(base/'records/doubt_confidence.json').write_text(json.dumps(ratings,ensure_ascii=False,indent=2)+'\n')
(base/'records/notation_audit.md').write_text('''# Final notation audit

Completed after all 46 second visual readings and before opening the context archive. The full set of recurring font, accent, exponent, limit, quotation and arrow forms was reviewed against the page audits and the images already inspected. Local changes include the exclamation/prime doubt on cover 002, doubled Z on 005 and 047, natural-number alphabet doubts on 011/017, removal of unsupported comma-like strokes in the typed exponents on 016, doubled T on 025, covering-letter doubts on 031, and explicit connector doubts on 042/045. The manuscript's locally different or unclear forms remain locally different or doubtful. The final notation table is copied to the head of the doubts file.

The comparison preserves the following specific evidence: plain C in the real/complex comparison on 022; the two visibly separate typewriter underlines on N/Z in 028; bare H beside checked/barred forms in 025–031; hatted versus plain H at the foot of 044; differing norm subscripts A/bar k and A/k on 050; uncertain K superscripts and the overwritten coefficient in 051. All quotation occurrences were checked for the source's double quotation marks or guillemets. No wholesale mathematical normalization was performed.

Completed UTC: '''+utc()+'\n')
obs=base/'records/reading_observations.md'
s=obs.read_text()
if not s.startswith('# First-pass'):
 obs.write_text('# First-pass visual observations\n\nThese entries record the first reading at the time each page was saved. They are historical; subsequent visual corrections are itemized in second_audit.md and incorporated in the final fragments.\n'+s)
for p in Path('/tmp').glob('save[0-9]*.py'):
 d=base/'scripts/first_pass';d.mkdir(exist_ok=True);shutil.copy2(p,d/p.name)
shutil.copy2('/tmp/finalize_support.py',base/'scripts/finalize_support.py')
rebuild()
(base/'records/work_state.md').write_text('''# Current work state

All 46 retained scans have completed the sequential first reading and the second visual audit. The omissions supplied with the source are 034, 040, 041 and 046. The primary reader personally read every whole image and both supplied halves; no manuscript OCR or delegation of manuscript/context reading was used. Mechanical validation is delegated only for generated-file syntax and package structure.

The notation table, abbreviations, low-confidence overrides and final legibility account have been completed. The context ZIP remains unopened at this record's writing. Per-page and combined SHA-256 freeze must occur before appending context opened and extracting the context. No transcription change is permitted thereafter. Research notes remain to be written after README and RESULTS_STATE are read, with an actual context search for each note and explicit status attribution. The final hash check and package check are also outstanding.

Checkpoint 01 was saved at 22:42:34 UTC. Checkpoint 02 is due 2026-11-16 23:41:56 UTC; subsequent hourly checkpoints follow the original start time, 21:41:56 UTC. Checkpoints contain all deliverable/support work, never the supplied scans or source archives. The final download must be one ZIP, MPL_31_002-051.zip.

Updated UTC: '''+utc()+'\n')
print('Updated notation, abbreviations, confidence, legibility, audit record and work state; copied first-pass scripts. Low-confidence overrides:',len(ratings))
