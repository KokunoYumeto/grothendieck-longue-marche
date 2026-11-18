# MPL_98 — Research notes

## Evidence, scope, and status

**Research phase in progress.** The diplomatic transcription of `98.pdf`, scans002–044, was frozen at **2026-11-18 01:36:35 UTC**, after all43 second visual audits and a successful full LaTeX syntax compile. The44 SHA-256 values cover the43 individual page fragments and the combined fragment; subsequent context comparisons do not alter them.

The supplied context consists of `README.md`, `notes/RESULTS_STATE.md` (RS), `hua_project/README.md`, and Michel Hua’s project’s `hua_project/98.modern.tex` (Hua98). Hua98 is explicitly an AI-produced modernised interpretation, not a diplomatic transcription or an established result; its page numbers are one less than our scan numbers. RS statuses are the originating runs’ claims unless the supplied entry expressly records a review; the original result files listed by RS are not present here and have not been independently inspected.

The research notes distinguish manuscript assertions, proposed mathematical reconstructions, reading questions raised by context, and our own checks. The75 separate context searches already performed are recorded in `research/context_searches.jsonl`; the note plan is in `research/note_plan.json`. Detailed proof checks and source references are being assembled in the research memos, and actual check events will be consolidated into `CHECK_EVENTS.tsv` before delivery.

## Initial checked findings (to be integrated into the numbered notes)

### MPL98.P01 — Scope of the folder

**File/scans:**98.pdf,002–044. **Kind:**unpursued implication / planning comparison. **Context:**README, “This package in our plan”; RS, “Orientation for this package”; Hua98, “Les stations.”

The two covers, “Formalisation [or Formulation] des Normes” and “Familles limitées,” and the intervening arguments substantiate the norms, group-cohomology and bounded-family strands identified by Hua’s project. The scans provide finiteness tools relevant to constructing moduli spaces, but do not by themselves establish the planning guesses concerning Néron models, Greenberg transforms, residues or the named open section/GT problems. The ten reused typescript faces add topology and abelian-variety material which Hua98 explicitly omits; those faces must remain separate from the handwritten line of argument.

### MPL98.B19 — Module flatness is genuinely needed in the intended Tor lemma

**File/scans:**98.pdf,039–040. **Kind:**own idea / counterexample to an omitted-hypothesis formulation. **Quote:**“comme $M_i$ est plat sur $A$.” **Context:**Hua98, “Changement de base pour les Tor,” which supplies the missing sheaf-flatness hypothesis; RS has no settled result on this lemma. **Confidence:**high, by the explicit two-term resolution below, independently checked by the boundedness research worker.

For $A=k[t]$, $B=A[x]$, $M_1=B/(tx)$ and $M_2=B/(x)$, the resolution $0\to B\xrightarrow{tx}B\to M_1\to0$ gives $\operatorname{Tor}_0^B(M_1,M_2)=\operatorname{Tor}_1^B(M_1,M_2)=A$ and higher Tor zero, although $M_1$ is not $A$-flat. After $A'=A/(t)$, the modules become $k[x]$ and $k$, so the new first Tor is zero while the old first Tor tensored with $A'$ is $k$. Thus flatness of the schemes and of all the displayed Tor groups does not substitute for the module-flatness assumption used in the proof; this tests the intended relative-Tor statement and does not resolve the manuscript’s coefficient-ring reading doubts.

### MPL98.B24 — “En tt degré” can be correct for the truncated complex

**File/scans:**98.pdf,042–043. **Kind:**unpursued implication / correction to a contextual interpretation. **Quote:**“est un isom en tt degré”; “en particulier pour $p\leq N$.” **Context:**Hua98, “Changement de base pour les Ext,” final footnote, which restricts the first phrase as well as the Ext comparison. **Register:**no matching settled result; RS orientation is an unrefereed lead.

The proof first considers the cohomology of the truncated Hom complex, whose terms are flat and whose top cohomology is the explicitly imposed flat terminal cokernel. With flat cohomology in the remaining degrees, base change for that complex holds in every degree, while its identification with Ext is asserted only for $p\leq N$. The manuscript’s separation of the two conclusions therefore need not be a mathematical overstatement; the modernised reading’s restriction is stronger than this particular argument requires.

## Remaining work in this research phase

Complete the75 concise, individually located notes; add the authorial self-flag and title/count inventories; verify the primary-literature locators; consolidate the proof and computation events; and verify the frozen hashes again. This paragraph is a checkpoint status, not a final conclusion.
