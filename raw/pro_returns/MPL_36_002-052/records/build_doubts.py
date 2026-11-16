from pathlib import Path
import re,json,collections,datetime
ROOT=Path(__file__).resolve().parents[1]
manual=[json.loads(s) for s in (ROOT/'records/doubts_rows.jsonl').read_text().splitlines() if s.strip()]
def group(s,start):
 depth=1;i=start
 while i<len(s):
  if s[i]=='\\':
   if i+1<len(s) and not s[i+1].isalpha():i+=2;continue
   m=re.match(r'\\[A-Za-z]+',s[i:]);i+=len(m.group(0)) if m else 1;continue
  if s[i]=='{':depth+=1
  elif s[i]=='}':
   depth-=1
   if depth==0:return s[start:i],i+1
  i+=1
 raise ValueError('Unclosed macro')
def split_reading(s):
 depth=0
 for i,c in enumerate(s):
  if c=='{':depth+=1
  elif c=='}':depth-=1
  elif c=='|' and depth==0:return s[:i],s[i+1:]
 return s,''
def norm(s):
 s=s.replace('\\ell','ell').replace('\\eta','eta').replace('\\omega','omega')
 s=s.replace('\\mathbb','').replace('\\mathbf','').replace('\\operatorname','')
 return re.sub(r'[^a-z0-9]', '',s.lower())
def cell(s):return str(s).replace('|','\\|').replace('\n',' ')
def code(s):return '`'+cell(s).replace('`','&#96;')+'`'
entries=[]
for p in sorted((ROOT/'pages').glob('*.tex')):
 scan=int(p.stem[-3:]);s=p.read_text()
 for m in re.finditer(r'\\(unsure|illegible)\{',s):
  body,end=group(s,m.end());reading,alternative=split_reading(body)
  line=s.count('\n',0,m.start())+1
  candidates=[r for r in manual if r['scan']==scan and norm(r['reading'])==norm(reading)]
  if candidates:
   row=candidates[-1];confidence=row['confidence'];location=row['line']
  else:
   confidence='low' if scan in (29,31,33,37,42,48,50,52) else 'medium'
   location=''
  if m[1]=='illegible':confidence='low';reading='unreadable prose ('+body+' word'+('s' if body!='1' else '')+')';alternative='no recoverable reading after enlargement'
  entries.append({'cote':36,'scan':scan,'tex_line':line,'location':location,'macro':m[1],'reading':reading,'alternatives':alternative,'confidence':confidence,'token':m.group(0)+body+'}'})
notation=r'''# Notation and reading doubts

## Package notation table — reconciled before the transcription was frozen

Readings in this table and in the transcription were made from the supplied images alone, in one continuous stream, without OCR or sub-agents. All 31 whole images and their 62 supplied halves were inspected; every page then received a separate second visual audit. A question mark without an editorial macro belongs to the source; `\unsure{...}` records the transcriber's uncertainty. The first alternative is the reading of the ink, not a proposed mathematical correction.

| Form or distinction | LaTeX retained | Locations checked and decision |
|---|---|---|
| Lowercase ell; line references | `\ell` | 003–008, 030–034, 036, 039, 046. The handwritten looped ell and the typescript's corrected ell are distinguished from the numeral 1; line references are not expanded. |
| Primes and exclamation marks | `'`; `^!`, `_!` | Primes on `A`, `M`, `G`, `n` throughout. The dotted exclamation in `f_!` on 037 and in `f^!`, `f_!` on 043 is retained; none is converted to a prime or a star. |
| Pullback star | `^*` | 005, 037, 043, 052. Read independently of the exclamation marks. The star missing after the first `pr_2` on 052 is not supplied; the later star/alpha-shaped marks remain doubtful. |
| Picard exponents | `^0`, `^{\unsure{\tau\|2}}`, `^\tau` | 039–040. Round zeroes remain zeroes. The hooked exponent in 039 (**) is primarily tau with 2 as an alternative; the clearer hooked sign on 040 is tau. They are not normalized to the connected Picard functor. |
| Underlined operators | `\underline{\operatorname{Hom}}`, `Ext`, `Pic`, `Alb`, `Tors`, etc. | 029, 031, 036–044, 048–052. Underlines are retained where drawn, including differences between underlined and un-underlined occurrences. No missing internal-functor underline or cohomological degree is supplied. |
| Cohomology alphabets | `H`, `\mathcal H`, `\check{\mathcal H}` | 036–045, 049, 051. The flourished and checked functors in the reused cohomology typescripts are distinguished from ordinary cohomology groups. The added check is retained. |
| Blackboard or bold integers | `\mathbb Z`; `\unsure{\mathbb Z\|\mathbf Z}` | 031, 033, 036–039, 045–046. Clearly doubled strokes are blackboard bold; the less decisive forms on 031 and 033 retain the alternative. |
| Rational coefficients | `\mathbb Q` | 039, 045–046. In 039 the written coefficient is Q, without an added quotient by Z. The cancelled coefficient on 045 remains explicitly doubtful. |
| Witt-family and Witt-ring letters | `\mathbb W`, `W_n`, `W_\infty(k)` | 045. The doubled family letter is distinguished from ordinary indexed W. The first ambiguous family occurrence retains both readings. Subscript `s` and superscript `(\varphi)` are not interchanged. |
| Lie-algebra Gothic letters | `\mathfrak g`, `\unsure{\mathfrak r\|r}`, `\unsure{\mathfrak h\|h}` | 038. The uncertainty about the small radical and subalgebra letters is propagated through the sheet; the clear Gothic g is retained. |
| G/C and lattice notation | `G`, `M`, `M'`, `D(M)` with local alternatives | 028–033, 052. C-like G forms are not silently replaced by a different group. Explicit local ambiguities remain marked. |
| Gamma/sigma-shaped group letter | `\gamma`, initially `\unsure{\gamma\|\sigma}` | 041, 044. The repeated looped form is consistently gamma as the primary reading; its initial ambiguity is recorded locally. |
| Torsion and quotient indices | `{}_nP`, `P_n`, `P^{(n)}` | 005–008, 028–034, 036, 039, 045–050. Left subscripts, right subscripts and parenthesized superscripts remain distinct; surprising n/n′ indices are not repaired. |
| Tate notation | `T_\ell`, `T_p`, `T_\Pi`, `T_{\unsure{\cdot}}` | 031–033, 039, 045–046, 050. The lower dot on 039 is not silently read as ell. The same T notation is not taken to establish an identification of a projective system with its limit. |
| Prime-set letter | `\Pi` | 048, 050. Retained as capital Pi. The compressed notation under the direct limits is kept locally, rather than rewritten as a modern indexing category. |
| Pairing phi forms | `\phi`, `\varphi` | 030–034 versus 045, 048–050. The typed/slanted and looped handwritten forms are retained. This is a glyph distinction, not a claim that they denote different pairings. |
| Xi | `\xi` | 030–034, 042, 052. The first circled membership on 034 alone receives an enclosure; the second membership is not circled. |
| Coefficient zeta | `\zeta_\ell`, `\zeta_p` | 036. The three-shaped zigzag is not replaced by an expected mu. |
| U-shaped root-of-unity notation | `U_\ell`, initially `\unsure{U_\ell\|\mu_\ell}` | 036, 046. The primary U reading is consistent across both sheets; the less clear first occurrence retains its alternative. |
| Dotted i-like p coefficient | `\unsure{i_p\|\alpha_p}`, later `\unsure{i_p}` | 036. An alpha interpretation is a possible mathematical identification, not a silent transcription correction. |
| Frobenius notation | `F`, left/right `F` indices, `(\varphi)`, `s` | 036, 045. Kernel/cokernel positions and fixed/stable notation are retained separately. |
| Arrowheads, plain strokes and maps-to bars | TikZ arrows, `no head`, `\mathbin{-}`, `\vdash` with local doubt | All diagram sheets, especially 028, 031, 033, 039, 042, 046, 048, 050. A connection is not given an arrowhead merely because it is a morphism. The upper terminal arrow on 028 points left. |
| Double implication arrows | `\Longleftarrow`, `\Rightarrow` | 037, 043, 049. Direction and doubled shafts are retained. They do not license completion of a spectral sequence. |
| Vertical isomorphism-like signs | `\wr`, rotated `\simeq`, with local doubt | 033, 040, 052. The curly lower sign on 052 is not silently promoted to an upward arrow. |
| Zero and dot-shaped zero | `0`, `\unsure{\bullet\|0}` | 028–029 and exact-sequence sheets. A filled dot whose role is unclear remains doubtful. |
| Double quotation marks and ditto marks | two backticks / two apostrophes; `\text{''}` for ditto | 003–008, 036, 044, 051–052. No typographic guillemets are substituted. An unclosed source quotation is not closed editorially. |
| Authorial spelling and typing slips | literal forms, e.g. `ps`, `tu affirme`, `droitsseront`, `Ppour`, `resulte` | 007–008, 049, 051. Inserted letters such as the s in “sections” and le in “fonctorielle” are marked as insertions, not silently absorbed. |
| Abbreviated m with circumflex | `\hat{\mathrm m}` / `\widehat{\mathrm m}` | 006, 008, 031. The abbreviation is not expanded in the transcription. |
| Circles, boxes, brackets and leaders | TikZ paths; `\boxed`, `\fbox` where appropriate | Throughout. Ellipses stay ellipses; the oval on 043 and the enclosing rectangle on 041 are attached to their contents. Editorial cancellation is carried by `\deleted`. |
| Numbering | `\scanpage`, `\mspage`, marginal numerals | Scan numbers are the supplied PDF scan numbers. Manuscript 1–6 and handwritten 13 are kept separately from the lower pencil sequence. The reused typescript 15 and printed “98” are not silently made scan numbers. |
| Unfinished clauses and formulas | literal stops and incomplete delimiters | Especially 030–031, 041–044, 048, 051. No right-hand side, missing index, proof, or closing mathematical phrase is supplied. |

## Current local doubts

The table below indexes **every current occurrence** of `\unsure` and `\illegible` in the page files, including repetitions. “L” is the exact line of the corresponding `pages/MPL_36_002-052_36_scanNNN.tex` file; a manuscript block locator is added where it can be matched securely to the reading record. This avoids fictitious physical line numbers for marginal and interlinear writing. The current table supersedes provisional readings in the chronological records; those records are retained to document corrections.

Confidence is qualitative: **medium** means a preferred reading has visible support but a stroke or ending remains uncertain; **low** means the writing is compressed, faint, overwritten, truncated, or permits materially different readings. No “high” label is used to conceal an unresolved local doubt. A blank alternative means no better alternative could be read, not that the primary reading is certain.

| File | Scan | Location | Reading retained | Alternative(s) | Confidence |
|---|---:|---|---|---|---|
'''
rows=[]
for e in entries:
 loc='L'+str(e['tex_line'])+('; '+e['location'] if e['location'] else '')
 rows.append('| 36.pdf | '+str(e['scan'])+' | '+cell(loc)+' | '+code(e['reading'])+' | '+(code(e['alternatives']) if e['alternatives'] else '—')+' | '+e['confidence']+' |')
abbrevs=r'''

## Abbreviations encountered

Expansions are interpretive aids in this file only. They are not replacements in the transcription. A doubtful expansion is stated as such; mathematical letters and undefined initials are not silently resolved.

| Form on the page | Possible expansion or function | Scans / qualification |
|---|---|---|
| `SGA` | Séminaire de géométrie algébrique | 003 |
| `p`, `p.`, `pg` | page | 003–008; punctuation varies |
| `ℓ`, `l`, negative line numbers | ligne / line counted from the bottom where negative | 003–008; the reference notation itself is retained |
| `ss` | suivantes | 005–006 |
| `Rmq` | remarque | 003–004 |
| `A. M.` | unresolved initials | 004; no expansion justified by the ink alone |
| `VA`, `V.A.` | variété abélienne | 004, 006, 037, 039 |
| `car` | caractéristique | 006, 046 |
| `hyp`, `hyp.` | hypothèses | 006–007, 031, 052; some endings doubtful |
| `ps` | pas | 007 |
| `nb`, `nbs` | nombre, nombres | 046, 048, 050 |
| `p.e.`, `p.ex.`, `p.ex` | par exemple | 003, 029, 050 |
| `loc cit.` | loco citato | 005; visible spacing is retained |
| `loc.`, `loc` | localement | 033, 048 |
| `Th.`, `théor.` | théorème | 037, 045, 049 |
| `Prop.` | proposition | 033, doubtful against Rmq |
| `dém.`, `Dém.` | démonstration | 006, 050 |
| `déf.` | définition | 031, 033, 048 |
| `cor.`, `Corollaire` | corollaire | 050; repeated number 1 is not changed |
| `resp.` | respectivement | 031 |
| `i.e.`, `ie`, `i.e` | id est / c'est-à-dire | 006, 034, 042, 046, 049, 052 |
| `ssi` | si et seulement si | 029, 048 |
| `p.c.` | parce que, probably | 029 |
| `can.`, `canoniqt` | canoniquement | 029; compressed ending remains doubtful |
| `splitt.` | splittage | 029 |
| `relev.` | relevant | 029 |
| `ext.`, `Ext` | extension / extension functor, according to use | 029 onward; also a doubtful `ext.` in the residue-field phrase on 005 |
| `hom`, `hom.`, `Hom` | homomorphisme / Hom functor | 029 onward |
| `isom`, `isom.` | isomorphisme | 029, 040, 042, 052 |
| `biext.`, `Biext` | biextension / biextension functor | 029–034, 050 |
| `cat.`, `Cat` | catégorie(s) | 044; also full words elsewhere |
| `fonct.` | foncteur | 052 |
| `pl. fid.`, `Pl. fidèle` | pleinement fidèle | 048, 052 |
| `Ess. surj.`, `surj.` | essentiellement surjectif; surjectif | 048; cancelled first phrase |
| `épim.` | épimorphisme | 050 |
| `équiv.` | équivalence | 048 |
| `mbs` | membres, probably | 048; primary reading is doubtful and not expanded in the page |
| `syst.` | système(s) | 050 |
| `gr`, `grs`, `gpe`, `gpes` | groupe(s) | 037, 041, 044, 046, 052; small subscripts remain locally doubtful |
| `rel.` | relativement | 052 |
| `nécessairemt` | nécessairement | 052; handwritten contraction |
| `ts` | tous, probably | 052 |
| `ft` | fait, possibly | 042; competing quantifier-like reading retained |
| `pct`, `pt` | pointés, possibly | 052; do not identify the subscript solely from the expected category |
| `fib` | fibré(s), possibly | 052; inserted and cancelled fragment |
| `birig` | birigidifié(s) | 052 |
| `sym` | symétrique(s) | 052 |
| `NS` | Néron–Severi, probably | 052; no definition is supplied on this sheet |
| `pr_1`, `pr_2` | première et deuxième projections | 052 |
| `lin.` | linéaires, probably | 037, doubtful programme note |
| `T.F.` / `T.F` | probably a reference to a Théorie des faisceaux | 049; bibliographic identification is a research question |
| m with circumflex | même | 006, 008, 031; never expanded in the transcription |
| `NB` | nota bene | 050 |

## Legibility and limits of confidence

The six opening editorial sheets are mostly legible; their compressed endings, pencil replies, and partly overwritten references require more caution than the main lines. The typed pairing sheets are substantially clearer, but their overwritten indices, corrected references, and annotations must be read as distinct layers. The reused Lie-algebra page and cohomology typescripts are legible apart from overtyping and cancellation; their provenance is different from the live handwritten mathematical notes.

The weakest extended passages are the splittings discussion on 029, the abandoned proof and marginal wording on 031, the programme list on 037, the crossed-out birational draft on 042, the cancelled proof on 048, the boxed projective-system qualifications on 050, and several labels and small indices on 052. These are explicitly marked in place. Five physically occluded prose spans, estimated at ten words in total, remain `\illegible`: two on 004, two on 048, and one on 051. No mathematical symbol is represented by `\illegible`.

The TikZ paths preserve the identifiable shapes, enclosures, leaders, isolated marks, and relative groupings. They are an approximation of pen geometry, not a metrically exact facsimile. The LaTeX is a fragment using the requested editorial macros; the separate validation wrapper defines those macros only to check the fragment and is not part of the transcribed manuscript. The final inventory classifies both handwritten fronts and their supplied reused typed versos as `reused_typed`, while the crossed-out own draft on 042 is `cancelled_draft`.

The supplied archive contains 31 retained scans: 003–008 and 028–052. The prompt's later reference to 49 pages does not correspond to additional supplied images. No missing, blank, or previously transcribed scan has been reconstructed.
'''
(ROOT/'MPL_36_002-052_doubts.md').write_text(notation+'\n'.join(rows)+abbrevs)
(ROOT/'records/current_doubts.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
print('Current doubt entries',len(entries),collections.Counter(e['macro'] for e in entries))
