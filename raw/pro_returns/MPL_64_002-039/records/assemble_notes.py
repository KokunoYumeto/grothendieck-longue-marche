from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
def load(n): return json.loads((root/'records'/n).read_text())
rootnotes=load('root_note_items.json'); questions=load('question_note_items.json'); apparatus=load('apparatus_note_items.json')
# Preserve notation in source fields; make prose spacing readable without changing any frozen file.
def prose(s):
 s=re.sub(r'\b(scans?|pages?|cotes?|on|at|all|order|orders|Table|from|before|after|formula|formulas|Part|Theorem|Corollary|Remark|Definition|Corollaire|lines?|rg|modulo|and|levels?|especially|labell?ing|rank|of|to|sections?)(?=\d)',r'\1 ',s,flags=re.I)
 s=re.sub(r'(?<!\w)(§§?)(?=\d)',r'\1 ',s)
 s=re.sub(r',(?=\S)',', ',s)
 s=re.sub(r';(?=\S)','; ',s)
 s=re.sub(r':(?=\d)',': ',s)
 s=re.sub(r'\bTable(?=[A-Z]\b)','Table ',s)
 s=s.replace('determinant+1','determinant +1').replace('modulo±1','modulo ±1')
 s=re.sub(r'(?<=\d)\((?=Katz|Ledet|Hoshi|Ogus|Bouw)',' (',s)
 s=s.replace('characteristicp','characteristic p').replace('and159','and 159').replace('PartI','Part I')
 s=s.replace('Sylow2','Sylow 2').replace('two-sous','two-sous')
 for name in ['Katz','Ledet','Wewers','Vologodsky','Hoshi']:
  s=s.replace(name+'(',name+' (')
 s=s.replace('equations(Katz','equations (Katz').replace('nilpotence(Ogus','nilpotence (Ogus')
 s=s.replace('isomorphism(Hoshi','isomorphism (Hoshi').replace('curves(2006','curves (2006')
 s=s.replace('conclusions(Bouw','conclusions (Bouw').replace('change(for','change (for')
 s=s.replace('above(1','above (1').replace('Theorem10','Theorem 10')
 return s
# Keep cohomology classes distinct from section coordinates.
for x in rootnotes:
 if x['id']=='C64-N35':
  x['body']=x['body'].replace('section q(c,d)=b^d a^c','section q(x,y)=b^y a^x')
(root/'records/root_note_items.json').write_text(json.dumps(rootnotes,ensure_ascii=False,indent=2)+'\n')

def render(n):
 out=[f"### {n['id']} — {prose(n['title'])}",'',f"**Cote 64, scans:** {prose(n['scans'])}  ",f"**Kind:** {n['kind']}  ",f"**Anchor:** {prose(n['quote'])}",'',prose(n['body']),'',f"**Context searched and compared:** {prose(n['context'])}  ",f"**Results-state relation:** {prose(n['ledger'])}  ",f"**Search/check key:** {n['id']} in records/root_context_searches.json and CHECK_EVENTS.tsv"]
 if n.get('related'): out.append('**Related notes:** '+n['related'].replace(';','; '))
 return '\n'.join(out)+'\n\n'

out=['# Research notes — MPL_64_002–039','',
'**Alexander Grothendieck, cote 64, PDF scans 002–039. Research run: 17 November 2026.**','',
'The diplomatic transcription was frozen at 22:58:22 UTC before the context archive was opened. These notes discuss the frozen reading; subsequent context comparisons, mathematical corrections and reading questions have not changed any page or the combined transcription. The manuscript sources are Grothendieck (n.d.-a, cote 64) and the supplied Longue Marche transcriptions (n.d.-b), with exact scan and formula locators given per item.','',
'The principal evidence is finite: the four-set and square constructions, the rank-two module over Z/4Z, its octahedron, and its central lifting problem. The requested modular place at infinity is not constructed in this selection, and planning conjecture S20 is not established here. Sections I and II distinguish these scope conclusions from independently checked finite statements and from the supplied context’s previous-run claims.','',
'## Reading these notes','',
'Each numbered item contains a one-to-four-sentence note; its anchor is a short verbal excerpt or a compact formula, with deletion-to-insertion arrows used editorially. Mathematical notation is normalized only in these research notes: D8 means the dihedral group of order eight, called D4 in the manuscript, and derived subgroups are written as commutator subgroups because the manuscript uses a prime for quotienting by {±I}. The kind unproved claim identifies an assertion or brief sketch in the manuscript, even when this run subsequently verifies it. The 333 current unsure markers and four illegible spans remain in the separate doubts apparatus; none is treated as an authorial conjecture.','',
'Every item has an actual context-search record and an event entry. A source/wording comparison, a prior claim carried as background, a mathematical proof check and an executable finite computation are recorded as different activities; reading a manuscript assertion during transcription is not counted as proving it. The source code and compact proof reports in records document what was checked, and published results below are used with inspected hypotheses rather than independently reproved.','',
'Current scan numbers refer to the PDF 64.pdf numbering; the author’s numbers are listed separately in Table B. Hua’s page n corresponds to the present scan n+1, as stated in notes/RESULTS_STATE.md, so each current-scan locator also identifies the leaf being compared with his subsection unless another context scan is specified.','',
'## I. Answers to the requested research questions','']
for n in questions: out.append(render(n))
out+=['## II. Local mathematical, textual and interpretive notes','']
for n in rootnotes:
 out.append(render(n))
 if n['id']=='C64-N20':
  out+=['#### Table A. The ten nontrivial transitive sets of the cube rotation group','',
'Associated with C64-N19–N20. The group is the orientation-preserving S4, acting on four body diagonals; this table is a checked interpretation of the objects, not a replacement for the manuscript’s shorter list. Hua’s §4 supplies the interpretive list, and records/basic_permutation_checks.py verifies all rows.','',
'| Cube object | Orbit size | Stabilizer in S4 | Verification |',
'|---|---:|---|---|',
'| Vertices | 8 | C3 | Transitive; stabilizer order 3 |',
'| Edges | 12 | C2 generated by a transposition | Transitive; generator outside V |',
'| Faces | 6 | C4 | Rotations about the face axis |',
'| Body diagonals | 4 | S3 | Stabilizer of one of the four diagonal labels |',
'| Opposite-edge pairs | 6 | Nonnormal V4 | Distinct from the normal translation subgroup |',
'| Opposite-face pairs | 3 | D8 | Stabilizer of one face-direction |',
'| Directed edges | 24 | Trivial | Regular action |',
'| Two inscribed tetrahedra | 2 | A4 | The index-two orbit |',
'| Face diagonals | 12 | C2 generated by a double transposition | Generator lies in V |',
'| Ordered pairs of distinct face-directions | 6 | Normal V4 | Quotient action is the regular S3 action |','',
'The separate file records/s4_subgroup_inclusions.svg supplies the actual thirty-node subgroup diagram, with its generator key and exact CSV data beside it. It is supplemental research, not a diagram added to the frozen transcription.','']
 if n['id']=='C64-N28':
  out+=['#### Table D. The five checked subgroup intersections on scan 032','',
'Associated with C64-N28. Here G=GL2(Λ), G1=SL2(Λ), K is the mod-two reduction kernel, K0=K∩G1, A is the canonical copy of M0 in End(M0), W is the complementary orientation module, K_A=1+2A, K_W=1+2W, and ε is the reduction-sign bit. A4 denotes the actual kernel of G→D8 in the verified natural model.','',
'| Top group | Two intermediate subgroups | Their intersection | Orders |',
'|---|---|---|---|',
'| G | ker ε and G1 | [G,G] | 96; 48,48; 24 |',
'| ker ε | K and [G,G] | K0 | 48; 16,24; 8 |',
'| [G,G] | K0 and A4 | K_A | 24; 8,12; 4 |',
'| K | K_W and K0 | Z={±I} | 16; 4,8; 2 |',
'| K0 | Z and K_A | 1 | 8; 2,4; 1 |','',
'The certificate checks the groups as sets of matrices, not only their orders; the corresponding inclusion indices are stored in records/group_checks_results.json.','']

out+=['## III. Steps the manuscript itself flags, and their disposition','',
'This section lists the identifiable authorial reservations, questions and requests for further work in the packet, including those answered a page later. A choice of convention and a resolved apparent contradiction are distinguished from an argument still left open. The poorly legible margin on scan 035 is explicitly provisional.','']
for n in apparatus:
 if n['id'].startswith('C64-U'): out.append(render(n))
out+=['## IV. Title sheets, headings and page counts','']
for n in apparatus:
 if n['id'].startswith('C64-T'): out.append(render(n))
out+=['#### Table B. Visible manuscript page or sheet numbers','',
'Associated with C64-T02. These are the marks actually transcribed in mspage; the Roman I on the cover is reported separately as a part mark.','',
'| Scan | Visible Arabic manuscript number |',
'|---:|---|']
for n in range(1,19):
 scan=2*n+1
 val=str(n)
 if n==1: val='1, doubtful'
 if n in (13,15): val+=', circled'
 out.append(f'| {scan:03d} | {val} |')
out+=['','Scans 004, 006, 008, 010, 012, 014, 016, 018, 020, 022, 024, 026, 028, 030, 032, 034, 036, 038 and 039 carry no authorial Arabic page number in the frozen transcription. No number is inferred for 039.','',
'#### Table C. Internal headings','',
'Associated with C64-T03. Uncertainties and the deletion in the third heading are retained here in words; exact diplomatic encoding is in the page files.','',
'| Scan | Heading or structural mark |',
'|---:|---|',
'| 002 | I — Fourbis combinatoires; Fourbis doubtful |',
'| 003 | 1. Ens. à quatre éléments. |',
'| 008 | 2. Structures [alternative: Structure] de carré combinatoire. |',
'| 020 | 3. Complément sur les 2 [alternative: 3]-ss-groupes; de Sylow deleted; d’un groupe G=… (card I=4). |',
'| 023 | 4. Relations avec le cube orienté |',
'| 026 | 5. Modules libres de rang 2 sur Λ=Z/4Z. |',
'| 033 | 6. Relations avec l’octaèdre non orienté Δ_M. |',
'| 039 | Récapitulation partielle |','',
'## V. Results-state crosswalk and retained status','',
'This table summarizes the relations already stated per item; it is not a promotion of every entry mentioned in the supplied register. A prior-run label such as Proved, Known or Refuted retains that provenance unless the finite component was actually rechecked here.','',
'| Register or context identifier | Supplied status or evidence | Effect of this packet/run |',
'|---|---|---|',
'| 64-gl2-z4-combinatorial-model | Hua project’s modern interpretation | The manuscript states the model on 028–029; natural actions and the groupoid argument independently checked in N21–N28 |',
'| LM140-2, LM_P057api R14, R16–R17 | R16 records an exercise; R17 an earlier-run checked model idea | Existing equivariant quotient solution credited and rechecked; canonical summand/torsor role identified in N23 and Q02 |',
'| LM140-2, LM_P057api R18–R19 | Group expectation and modular/Fermat-conic expectations | Finite PSL2(Z/4)≃S4 component checked; geometric cover and descent not established here |',
'| LM140-2, LM_P057api S6 | Four scalar-line complements and a proposed relation to lifts | Finite count and conjugation orbits checked in group report; proposed geometric correspondence not checked |',
'| LM2 C.r1–C.r3 | Unreviewed prior-return claims concerning genuine and outer congruence actions | Background typing distinctions only; current finite characters do not prove those arithmetic claims |',
'| LM2 C.d1 | Unreviewed previous-return Known claim | No all-level GT-kernel preservation proof supplied by these leaves |',
'| LM2 C.d5 | Open simultaneous realization/image problem | Remains untouched |',
'| LM4_SUCCESSOR B.38 | Open higher-level kernels | No resolution from levels 2 and 4 |',
'| LM4_SUCCESSOR E.10 | Six open congruence-kernel/involution computations | No resolution; do not conflate with only the finite current groups |',
'| EXIT_TOWER E.24 | Open arithmetic image problem | No arithmetic realization proved by the finite lifting calculation |',
'| LM7_PUSH E.3 | Open full-GT extra-coset question | Remains open at the register’s status |',
'| EXIT_TOWER E.49 | Explicitly unrefereed/under check | Not adopted as closing E.3 |',
'| LM6 F.43 | Prior-run boundary/normal-line claim | Background only; square lifting is not its geometric construction |',
'| MPL_93_002-046 E14 | Title-level conjecture: formal deformation versus coarse invariant | Actual statement unavailable; not adjudicated |',
'| MPL_93_002-046 E16 | Title-level own idea, earlier confidence high | No missing orders or families reconstructed |',
'| MPL_93_002-046 C29 | Title-level own idea: first-order bridge | No unseen map inferred or checked |',
'| MPL_93_002-046 P09 | Title-level future comparison with cotes 159 and 64 | Q09 is this run’s proposed necessary test, not a reconstruction of P09 |',
'| MPL_93_002-046 C35 | Withdrawn in the same text | Kept withdrawn; no revival without its missing explanation |',
'| Planning S20 | Planning guess in README | Mathematically coherent published comparisons identified; historical/documentary identity not established here |','',
'## VI. Evidence, reproducibility and limits','',
'The main reproducible finite checks are records/basic_permutation_checks.py, records/group_checks.py and records/congruence_context_checks.py; their JSON outputs and the subgroup CSV/SVG files are included. They use exact finite sets, permutations and integer arithmetic rather than a small-groups database; they are executable certificates with assertions, not theorem-prover formalizations. The group report supplies the categorical and cohomological arguments beyond the enumerations.','',
'The direct visual transcription and both complete image readings were performed in one primary stream before context access. Research agents subsequently compared the frozen text and context and checked mathematics; none read manuscript images or changed a transcription file. The final hash check records unchanged hashes for all thirty-eight pages and the combined fragment in progress.log.','',
'The LaTeX harness checks syntax and reaches all thirty-eight scan markers, while the inventory accounts for 761 elements with transcribed=yes. This mechanical check is not a new visual reading or a claim that every doubtful word is now certain; the current uncertainty inventory and the least-trusted margins remain in MPL_64_002-039_doubts.md. Contextual disagreements, including the subgroup numeral on022 and the product sign on032, remain research reading questions.','',
'## References','',
'Bouw, I. I., & Wewers, S. (2006). Indigenous bundles with nilpotent p-curvature. *International Mathematics Research Notices, 2006*, Article 89254. https://doi.org/10.1155/IMRN/2006/89254. Section references were checked in the author preprint, version 2, 18 August 2005: https://arxiv.org/pdf/math/0505275. Relevant locations: Definition 2.1, §§3.1 and 5.','',
'Grothendieck, A. (n.d.-a). *Modules courbes elliptiques en caractéristiques ≠2: Notes manuscrites*, cote 64, PDF scans 002–039 [Unpublished manuscript; Montpellier archive]. The supplied catalogue gives an approximate dating from 1980–1982; current quotations follow the frozen diplomatic transcription, not the modernized interpretation.','',
'Grothendieck, A. (n.d.-b). *Longue Marche*, cotes 140-2 and 140-3 [Unpublished manuscript; supplied contextual transcriptions]. Exact source files: LM_140-2_text.tex and LM_140-3_text.tex; cited scans and formulas are given in each note. The accompanying research-note files are separate previous-run interpretations.','',
'Hoshi, Y. (2015). Nilpotent admissible indigenous bundles via Cartier operators in characteristic three. *Kodai Mathematical Journal, 38*(3), 690–731. https://doi.org/10.2996/kmj/1446210603. Author revised preprint inspected: https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1811revised.pdf; relevant locations: introduction and §5.','',
'Katz, N. M. (1970). Nilpotent connections and the monodromy theorem: Applications of a result of Turrittin. *Publications Mathématiques de l’IHÉS, 39*, 175–232. https://doi.org/10.1007/BF02684688. Primary text inspected: https://web.math.princeton.edu/~nmk/old/nilpconn.pdf; relevant locations: introduction, Theorems 5.1, 7.4 and 10.0, and Corollary 7.5.','',
'Ledet, A. (2001). Embedding problems and equivalence of quadratic forms. *Mathematica Scandinavica, 88*(2), 279–302. https://doi.org/10.7146/math.scand.a-14327. Relevant passage: §0.4, pp.283–284; primary PDF inspected at https://journals.msp.org/mscand/article/download/878/877/909.','',
'Michel Hua’s project. (2026). *Modernised reading of cote 64* [AI-assisted project interpretation; supplied snapshot downloaded 14 November 2026]. Source: hua_project/64.modern.tex, with provenance and use conditions in hua_project/README.md. Project URL supplied with the context: https://github.com/Commutator-IO/grothendieck-project.','',
'Ogus, A., & Vologodsky, V. (2007). Nonabelian Hodge theory in characteristic p. *Publications Mathématiques de l’IHÉS, 106*, 1–138. https://doi.org/10.1007/s10240-007-0010-z. Primary text inspected: https://www.numdam.org/item/10.1007/s10240-007-0010-z.pdf; relevant passage: Remark 2.2.','',
'Supplied research context. (n.d.). *README, RESULTS_STATE, SECTIONS_STATE, LM2 congruence rows, and accompanying research notes* [Unpublished working materials supplied with this task]. Exact files, statement IDs and scan locators appear per item; these materials’ claims retain their recorded review status.','']
text='\n'.join(out)
# APA URL text remains visible while Markdown provides explicit links.
def link_url(m):
 value=m.group(0); core=value.rstrip('.,;'); return '['+core+']('+core+')'+value[len(core):]
text=re.sub(r'https?://[^\s]+',link_url,text)
(root/'MPL_64_002-039_notes.md').write_text(text)
allnotes=rootnotes+questions+apparatus
(root/'records/notes_assembly_report.json').write_text(json.dumps({'items':len(allnotes),'local_notes':len(rootnotes),'question_notes':len(questions),'author_flag_notes':sum(x['id'].startswith('C64-U') for x in apparatus),'title_records':sum(x['id'].startswith('C64-T') for x in apparatus),'word_count_approx':len(text.split()),'bytes':len(text.encode()),'IDs':[x['id'] for x in allnotes]},indent=2)+'\n')
print(json.dumps({'note_items':len(allnotes),'approx_words':len(text.split()),'bytes':len(text.encode())}))
