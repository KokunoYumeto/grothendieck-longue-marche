from pathlib import Path
import re, html

ROOT = Path(__file__).resolve().parents[1]

HEADER = r'''# Notation table

This register belongs to the image-only transcription. Cote 152 was read before cote 120; the same reader transcribed and audited all 38 pages. The comparative notation audit preceded opening the contextual archive. Different visible marks have been retained, with an explicit doubt where the ink does not settle the reading.

| Recurring sign or alphabet | LaTeX used | Image comparison and caution |
|---|---|---|
| Drawn double quotation marks | Two backticks and two apostrophes | Used consistently throughout the package. Printer apostrophes in JCL strings are literal printer characters. |
| Single and double underlining | `\uline{...}`, `\uuline{...}` | Both levels are retained; the double underline is in the crowded upper addition of 120 scan 6. |
| Written equality shorthand in prose | `$=$` | 152 scan 7; 120 scans 14–16 and 22. The sign has not been expanded in the transcription. |
| Barred m shorthand | `$\overline{\mathrm m}$` | 120 scans 3 and 5; the doubtful inserted occurrence in scan 3 remains marked. The word read as “même” in scan 7 remains separately doubtful. |
| Prime and inverse exponent | Apostrophe, `^{-1}` | 152 manuscript folios 1′, 2′, 3′ and primed contour notation; 120 inverse functions and Y′. No secure exclamation-mark exponent was encountered. The exclamation mark after “infinies” is ordinary punctuation. |
| Vector arrow over A and a | `\vec A`, `\vec a` | Compared in 152 scans 7–11; the arrow is retained on the visible occurrences. |
| Arc and contour involutions | `\sigma_\Gamma`, `\sigma_C`, `\sigma_0^C`, `\sigma_1^C` | 152 scans 7–11. The uncertain rho/sigma and subscript readings are exposed locally; identities were not repaired. |
| Rotations and their exponents | `\rho_\Gamma`, `\rho_C` | 152 scans 7–10. The overwritten inverse exponents in scan 8 and the raised sigma-like mark in scan 10 remain visible and doubtful. |
| Compact right/left labels | `\mathrm{rd}`, `\mathrm{rg}` | 152 scan 8. All three overwritten d/g letters in the boxed formulas are represented as cancellations. |
| Loop label resembling w | `\unsure{w|\omega}` | 152 scan 2. Comparison with the orientation omega of scan 3 did not securely resolve the small loop labels. |
| Graph, region and boundary symbols | `\Gamma`, `D`, `\dot D`, `K`, `S`, `S_0`, `R_0` | 152 scans 3–13. The dot over D and the indices are retained. R_0 in this portion is read in its own local notation. |
| Field and coordinate powers | `R`, `R^I`, `R^n`, `R_0` | 120 scans 3–25. The same plain R is used for the field/set glyph throughout; the earlier real-number glyph in 152 scan 5 remains locally doubtful. |
| Families of moderate parts | `\mathcal M_n`, `\mathcal M_I`, `\mathcal M_*` | 120 throughout. The star is retained as a subscript. Axiom labels M1–M11 retain their written placement and amendments. |
| Permutation alphabet | `\mathfrak S_n` | 120 scans 3–4. The uncertain compact glyph in scan 3 remains marked. |
| Pullback and inverse-image decorations | `u^*`, `u^{*-1}`, `\alpha_n^*`, `\beta_n^{*-1}` | 120 scans 3–4. Star and minus-one positions were checked individually. |
| Ind-category arrow | `\underrightarrow{\operatorname{Esp}}` | 120 scans 15–17 and 20. The arrow lies under Esp. Two occurrences in scan 15 also have a separate upper mark, retained as `\unsure{\sim|\leftrightarrow}`. |
| Two-level decoration over/under M | `\underrightarrow{\widetilde{\mathcal M}}` as the first doubtful reading | 120 scan 16. Both visible levels are retained; the alternative is left in the local doubt macro. |
| Calligraphic space letters | `\mathcal X`, `\mathcal Y`, `\mathcal Z` | 120 scans 16–17. Overwritten letters are uncertain; the two angular source Z letters in scan 17 are transcribed as plain Z. |
| Empty-set glyph | `\varnothing` | 120 throughout. Slashed loops were checked against numerical zeros, especially scans 4–10. |
| Universal sign and compressed words | `\forall`; local alternatives as marked | 120 scan 24 retains the reading `\unsure{$\forall$|tte}`; it has not been silently expanded. |
| Short function strokes and hooked inclusions | `-`, `\longrightarrow`, TikZ `no head`, or `\lhook\joinrel\relbar` | Heads and hooks were checked from the images. Doubtful short strokes remain explicit; visible headless hooks in 120 scans 14 and 16 are preserved. |
| OPS shorthand | `\unsure{OPS}` and the local crowded alternatives | Compared in 120 scans 13, 21 and 23. It remains abbreviated in the transcription. |
| Closure bar and restriction stroke | `\overline U_i`, `X|U_i` | 120 scan 25. The first bar over U_i remains doubtful; the later bar is clear. |

# Doubt register

The line references below are **page-file source lines**, not a new numbering of the handwritten lines. The nearby fragment locates the approximate manuscript passage after paragraph reflow. Every `\unsure` and `\illegible` occurrence is listed, including those in cancellations, diagrams and drawings. “Medium” means a tentative reading; “low” marks unresolved alternatives, heavily overwritten material or the least legible additions. No row is labelled high merely because its mathematical content is plausible.

'''

ABBREVIATIONS = r'''
# Abbreviations and shorthand

These expansions are reading aids in this English register only. They have not been substituted in the French transcription. A question mark records an unresolved expansion.

| Written form | Expansion or reading aid | Occurrences / limitation |
|---|---|---|
| `$=$`, barred m | même | 152 scan 7; 120 scans 3, 5, 14–16, 22. Literal sign/letter retained. |
| cat., Cat | catégorie | 152 scans 3, 13; 120 scans 7, 17. The crowded Cat f fragment in 120 scan 7 remains uncertain. |
| gr. | graphe | Cancelled abbreviation in 152 scan 3; tentative. |
| ens, ens. | ensemble(s) | Both cotes; punctuation follows the manuscript. |
| esp., Esp. | espace(s) | Especially 120 scans 10, 17, 20, 24. |
| pt, pts | point, points | Both cotes. |
| can., can raised t, canoniq raised t | canonique / canoniquement | 152 scans 3, 7, 11; 120 scans 4, 9, 12. Endings remain as written. |
| comb. | combinatoire | 152 scans 5, 7, 10. |
| comp. connexe | composante connexe | 152 scan 3. |
| cpt., cpt, cpts | composante in the disk discussion; compact / compact(s) in the topological discussion | 152 scan 3 and 120 scans 17–20. The local usage must be checked; there is no single expansion for all occurrences. |
| inv., involuti. | involution; invertible for “est inv.” | 152 scans 3–4, 11; 120 scan 22. |
| id. | identité | Diagram/operation label in 152 scan 2; also standard function notation. |
| isom. | isomorphisme | 152 scan 7; 120 scan 8. |
| homéo. | homéomorphisme / homéomorphe | 152 scan 5; grammatical expansion depends on its local phrase. |
| néc. | nécessairement | 152 scans 7, 13; 120 scan 17. |
| n.p. | non pénétrante | 152 scan 10; spelled out immediately before the abbreviation. |
| or. | orienté / orientés | Insertions in 152 scan 3. |
| réc | récurrence | 152 scan 4. |
| adm. | admissible | 152 scan 4 margin. |
| réal. | réalisation | 152 scan 5. |
| quelq. | quelconque | 152 scan 3 drawing label. |
| seult | seulement | 152 scan 3; uncertain reading. |
| lin. | linéaire / linéarisé ? | 152 scan 3 cancelled diagram; unresolved. |
| rd, rg | rive droite, rive gauche ? | 152 scan 8; the manuscript also writes côté droite/gauche. The label expansion remains tentative. |
| circ raised on | circularisation ? | 152 scan 10 margin; the whole phrase is doubtful. |
| op., op raised os/o | opération(s) | 120 scan 3; the raised letters are uncertain and retained. |
| app., appl. | application(s) | Both cotes, including cancellations. |
| top. | topologique / topologie | Both cotes. |
| str. mod. | structure modérée | 120 scan 9. |
| mod. | modéré(e)(s) | 120 scans 9–10, 21, 24; exact ending is supplied only by the local word being abbreviated. |
| loc., loc raised t | local / localement | 120 scans 16–20 and the cancellation in scan 25. |
| ind-, Ind | inductif / inductive | 120 scans 15–20, 22. |
| syst. | système | Both cotes; especially 120 scans 12, 18–20. |
| fond. | fondamental | 120 scans 18–20. |
| Prop, Proposition | proposition | Headings, both cotes. Prop remains abbreviated where written. |
| Cor, Cor. | corollaire | 120 scans 12, 23. |
| NB | nota bene | Both cotes. |
| i.e. | id est / that is | Both cotes. |
| cf | confer / compare | 120 scan 13. |
| p.ex. | par exemple | 120 scan 22. |
| hyp. | hypothèse | 120 scan 24. |
| ssi | si et seulement si | 120 scans 10–11, 22. |
| f. et s.; faut s. | faut et suffit | 120 scans 11, 19; these compressed readings remain doubtful. |
| OPS | on peut supposer | 120 scans 13, 21, 23; the letter reading is still doubtful. |
| amalg. | amalgamée | 120 scan 13 margin. |
| supplém. | supplémentaire(s) | 120 scan 15. |
| ess raised t | essentiellement | 120 scan 25; uncertain raised-letter reading. |
| tte | toute | Alternative to the universal sign in 120 scan 24, not the adopted first reading. |
| transfont | transforment | 120 scan 22 marginal addition; retained literally, including the cancelled occurrence. |
| biject. | bijection / bijective ? | Cancelled word in 120 scan 12, uncertain. |
| abs.; Aristyp.; p.; Alrt | unresolved | 120 scan 7; 152 scan 8; 120 scan 21. These fragments have not been expanded by mathematical expectation. |

## Reused computer printouts

The printer pages in 152 scans 6, 9 and 12, and the upside-down strip on scan 3, contain abbreviations and program/data-set identifiers. Their literal spellings are part of the transcription; the unresolved 0/O, 3/5 and identifier readings are in the doubt register. The following reading aids were checked against IBM documentation after the transcription was frozen; later IBM documentation supplies terminology, without identifying the exact historical software release of the printout.

| Printed form | Expansion or function | Caution / source |
|---|---|---|
| STMT NO.; ALLOC.; COND CODE | statement number; allocation; condition code | Ordinary labels of the printed messages. |
| VOL SER NOS | volume serial numbers | A label followed by storage-volume identifiers. |
| JCL; JES2 | job control language; Job Entry Subsystem 2 | IBM glossary [P1]. |
| SMF; CPU; SRB | System Management Facilities; central processing unit; service request block | CPU and SRB report execution times; [P2], [P3]. |
| VIO; VIRT; SYS | virtual input/output; virtual storage; system storage in the displayed accounting fields | [P2], [P4]; SYS elsewhere is the system identifier label. |
| MIN; SEC; K | minutes; seconds; kilobytes in the storage fields | [P2]; not a mathematical use of K. |
| INIT | initiator | The numbered job initiator in the start message; interpretation of the printed field. |
| EXEC; PROC; PGM | execute statement; procedure; program-name parameter | [P5]. |
| REG; REGION; PARM | local symbolic parameter supplying REGION; requested storage region; program parameters | REG and P are procedure-defined names here, not separately expanded system keywords; [P5]. |
| DD; DDNAME; DSN | data definition; data-definition name; data-set name | [P6]. |
| DISP; SHR; TRK | disposition; shared-use status; tracks | [P4], [P6]; ordinary explanations of the listed JCL operands. |
| MSGLEVEL | message-listing level | Controls the job-control and processing information printed; [P7]. |
| SYSIN; SYSOUT | system input; system output | Conventional data-definition names or output-class parameters; [P6]. |
| STEPLIB; SYSUT1; SYSUDUMP | step program library; utility/work data set; user-area diagnostic dump data set | Functional reading aids for conventional DD names; the precise use is program-dependent. |
| PREDONTA; CSSBATCH; CRBATCH; CRJIF; CRAYIN; E333; CISI.PROD.CSSBATCH.V1.YY01 | job, procedure, program, DD, system or data-set identifiers | No expansion asserted for these local names. IEF…, CSS2090 and HASP373 remain message identifiers. |
| SYSTSO / SYSTS0 | unresolved unit-name reading | The last character is a reading doubt, not an expansion to TSO. |

Documentation consulted, 14 November 2026: [P1, IBM glossary](https://www.ibm.com/docs/en/zos-basic-skills?topic=glossary-zos-terms-abbreviations); [P2, IEF374I](https://www.ibm.com/docs/en/zos/3.1.0?topic=messages-ief374i); [P3, SRB-mode callers](https://www.ibm.com/docs/en/zos/2.5.0?topic=systems-srb-mode-callers); [P4, allocation of virtual I/O](https://www.ibm.com/docs/en/zos/2.5.0?topic=allocation-virtual-io); [P5, EXEC parameters](https://www.ibm.com/docs/en/zos-basic-skills?topic=do-jcl-exec-statements-positional-frequently-used-parameters); [P6, DD parameters](https://www.ibm.com/docs/en/zos-basic-skills?topic=do-jcl-dd-statements-positional-frequently-used-parameters); [P7, MSGLEVEL](https://www.ibm.com/docs/en/zos/3.1.0?topic=statement-msglevel-parameter). Indexed primary-document excerpts were available; several full IBM HTML opens returned HTTP 403. IBM's [MVS System Messages, volume 8](https://publib.boulder.ibm.com/epubs/pdf/iea2m8c1.pdf) also opened as a PDF. None of these checks changed a transcription reading.

# Legibility assessment

All 38 supplied whole-page images and their supplied halves were inspected by the same reader during transcription, without OCR. All 38 pages then received a second image-to-text audit. The inventories include the covers, reused printouts, cancelled blocks, diagrams, freehand drawings, page numbers, marginalia and additions; the TikZ drawings are geometric reconstructions from the visible strokes, with uncertainty attached to doubtful labels.

The least secure readings are the overlapping diagonal additions on **120 scans 6–8**, the oblique annotations on **120 scans 13 and 15**, and the heavily rewritten portions of **152 scan 8**. Some labels and cancelled phrases on **152 scans 2–3 and 10**, and the compressed amendments on **120 scan 21**, also warrant renewed examination of the originals. Small machine-print identifiers on **152 scans 3, 6, 9 and 12** retain alternatives. The physical overlap in 120 scans 6–7 still leaves the word-count illegibility marks listed above; none is being used as a substitute for a mathematical symbol.

The transcription preserves surprising or unfinished text, including the final M_1 in 120 scan 22, the unclosed set-builder in scan 23, the underbrace position and final X in scan 24, and the equality of indexed families in scan 25. These are not corrections or endorsements of mathematical assertions. Every unresolved reading remains reviewable in its page file; complete page coverage does not imply certainty about every stroke.
'''

def escaped(s, i):
    n=0; i-=1
    while i>=0 and s[i]=='\\': n+=1; i-=1
    return n%2==1

def arguments(s, name):
    for m in re.finditer(r'\\'+name+r'\{',s):
        i=m.end(); start=i; depth=1
        while i<len(s) and depth:
            if s[i]=='{' and not escaped(s,i):depth+=1
            elif s[i]=='}' and not escaped(s,i):depth-=1
            i+=1
        if depth: raise ValueError(f'Unclosed {name}')
        yield m.start(), i, s[start:i-1]

def code(s):
    return '<code>'+html.escape(s).replace('|','&#124;').replace('\n',' ')+'</code>'

rows=[]; counts={'unsure':0,'illegible':0,'words':0}
for cote,n in [(152,13),(120,25)]:
    for scan in range(1,n+1):
        p=ROOT/'pages'/f'MPL_152+120_{cote}_scan{scan:03}.tex'; s=p.read_text()
        margins=list(arguments(s,'margin')); deletions=list(arguments(s,'deleted'))
        marks=sorted([(a,b,v,k) for k in ['unsure','illegible'] for a,b,v in arguments(s,k)])
        for a,b,v,kind in marks:
            counts[kind]+=1
            ln=s.count('\n',0,a)+1
            inmargin=any(x<=a<y for x,y,_ in margins)
            indeleted=any(x<=a<y for x,y,_ in deletions)
            loc=f'source l. {ln}'+('; margin' if inmargin else '')+('; deleted' if indeleted else '')
            near=re.sub(r'\s+',' ',s[max(0,a-55):a]).strip()
            loc += '; after '+code(near)
            if kind=='illegible':
                rd='unreadable ink: estimated '+v+' word(s)'; alt='—'; confidence='low';counts['words']+=int(v)
            else:
                parts=v.split('|',1);rd=parts[0];alt=parts[1] if len(parts)>1 else '—'
                confidence='low' if len(parts)>1 else 'medium'
                if cote==120 and scan in [6,7,8,13,15] and inmargin:confidence='low'
                if cote==120 and scan==21 and indeleted:confidence='low'
                if cote==152 and scan==8 and (inmargin or indeleted or v in ['Le','incidé','sens','Aristyp.']):confidence='low'
                if cote==152 and scan==2 and v in ['Sommet','principal','---']:confidence='low'
            rows.append(f'| {cote} | {scan} | {loc} | {code(rd)} | {code(alt)} | {confidence} |')

summary=f"There are **{counts['unsure']} explicit doubt occurrences** and **{counts['illegible']} word-count illegibility marks** (an estimated **{counts['words']} words**) in the audited fragment.\n\n"
table='| Cote | Scan | Approximate location | Reading | Alternative | Confidence |\n|---|---|---|---|---|---|\n'+'\n'.join(rows)+'\n'
(ROOT/'MPL_152+120_doubts.md').write_text(HEADER+summary+table+ABBREVIATIONS)
print(counts)
