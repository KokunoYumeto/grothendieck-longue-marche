#!/usr/bin/env python3
"""Render research-only artifacts and a reproducible per-note context search record."""
from pathlib import Path
import importlib.util, json, re, subprocess, csv

DOC = Path(__file__).resolve().parent
ROOT = DOC.parent
WORK = ROOT.parent
spec = importlib.util.spec_from_file_location('research_items', DOC/'build_research_notes.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
root_notes = mod.notes

TERMS = {
 'FW01':['Fourier','Poincar','convolution','compatibilité'],
 'FW02':['Kummer','torseur','Pic','xi'],
 'FW03':['rigidifi','Poincar','dual'],
 'FW04':['Koszul','compatibilité','F7','F8'],
 'FW05':['Koszul','cohomology','fibre'],
 'FW06':['épointée','surjectif','supports propres'],
 'FW07':['Laumon','1.2.5','F4'],
 'JAC01':['Alb','noyau','N(','Th. 1'],
 'JAC02':['Betti','P_','dimension','Th. 2'],
 'JAC03':['dualité','P^','Pic','Th. 3'],
 'JAC04':['polarisation','positive','Th. 4'],
 'JAC05':['Néron','Neron','hauteur','Th. 5'],
 'JAC06':['facteur fixe','hyperplan','Th. 6'],
 'JAC07':['numérique','tau','équivalence','Th. 7'],
 'JAC08':['1964','1966','Programme de travail'],
}

def import_candidates(filename, prefix, section):
    text = (DOC/filename).read_text()
    pattern = rf'^### ({prefix}\d+) — ([^\n]+)\n(.*?)(?=^### {prefix}\d+ — |^## |\Z)'
    ans = []
    for m in re.finditer(pattern,text,re.M|re.S):
        ident,title,raw = m.groups()
        paragraphs = raw.strip().split('\n\n')
        body = paragraphs[-1].strip()
        metadata = '\n\n'.join(paragraphs[:-1])
        if prefix == 'FW':
            kind = re.search(r'\*\*Kind:\*\*\s*(.*)',metadata).group(1)
            where = re.search(r'\*\*Current locator and short quote:\*\*\s*(.*)',metadata).group(1)
            quote = 'See the brief quoted words in the locator above.'
            comp = re.search(r'\*\*Context:\*\*\s*(.*)',metadata).group(1)
            rs = ['WG2 §2.4 #4','WG2 §1.1 #3']
            confidence = re.search(r'\*\*Editorial confidence:\*\*\s*(.*)',metadata)
            confidence = confidence.group(1) if confidence else None
            kind = {'FW01':'unpursued implication','FW02':'unproved claim',
                    'FW03':'unpursued implication','FW04':'reading question',
                    'FW05':'own idea','FW06':'own idea','FW07':'reading question'}[ident]
        else:
            where = re.search(r'\*\*File/scan:\*\*\s*(.*)',metadata).group(1)
            kind = re.search(r'\*\*Kind:\*\*\s*(.*)',metadata).group(1).rstrip('. ')
            quote = re.search(r'\*\*Short quote:\*\*\s*(.*)',metadata).group(1)
            rs = re.search(r'\*\*Bears on:\*\*\s*(.*)',metadata).group(1).rstrip('. ').split('; ')
            comp = re.search(r'\*\*Context:\*\*\s*(.*)',metadata).group(1)
            confidence = None
        # The reference-scope finding is brief here; the memo records its inspection.
        if ident == 'FW07':
            body = ('Laumon (1996), Theorem 1.2.4 and Lemma 1.2.5, states the relative inversion and '
                    'Poincaré direct-image identifications, but its proof paragraph only recalls the canonical map’s construction. '
                    'This verifies the scope of the comparator cited in CN F4, without furnishing a second manuscript witness or a newly checked fibre-compatibility proof.')
        ans.append(dict(section=section,id=ident,title=title,where=where.rstrip(),kind=kind,
                        quote=quote,rs=rs,search=TERMS[ident],comparison=comp,
                        sentences=None,body=body,confidence=confidence,
                        event='proof' if ident in ['FW05','FW06'] else 'documentary',
                        researcher='fourier_witness_research' if prefix=='FW' else 'jacobians_earlier_forms'))
    assert len(ans) == (7 if prefix=='FW' else 8), (filename,len(ans))
    return ans

delegated = import_candidates('research_fourier.md','FW','Carry question: the Fourier compatibility witness')
delegated += import_candidates('research_jacobians.md','JAC','Carry question: cote 44 Theorems 1–7')
all_notes = delegated + root_notes
refinements = {
 'P03':'P03.corrected — L tensor phi^*(g^*L)^(-1)',
 'R05':'R05.relative_class — rigidified representatives for relative/primed classes under the stated section and H0 hypotheses',
 'R11':'R11.quotient — last-arrow surjectivity and the quotient by Pic(Sigma)',
 'D02':'D02.stabilizer — specify automorphisms of the framed datum, or its action stabilizer',
 'FW06':'FW06.nonempty_boundary — nonempty boundary in every geometric fibre for the two-row setup'
}
for n in all_notes:
    n.setdefault('researcher','root')
    if 'body' not in n:
        n['body'] = ' '.join(n['sentences'])
    if n['id'] in refinements:
        n['refinement_id'] = refinements[n['id']]
    if n['id'] in ['R05','R11']:
        n['confidence'] = 'high for the explicit identity-section example; the author’s intended shorthand remains a reading question'
ids = [n['id'] for n in all_notes]
assert len(ids)==len(set(ids))

context_files = [WORK/'context'/'README.md', WORK/'context'/'notes'/'RESULTS_STATE.md',
                 WORK/'context'/'MPL_16+47+54+44_transcription.tex',
                 WORK/'context'/'MPL_16+47+54+44_notes.md',
                 WORK/'context'/'MPL_16+47+54+44_doubts.md',
                 WORK/'context'/'same_cote_57'/'MPL_57_271-315_notes.md',
                 WORK/'context'/'hua_project'/'README.md',
                 WORK/'context'/'hua_project'/'57.modern.tex']
search_records = []
for n in all_notes:
    cmd = ['rg','--line-number','--ignore-case','--fixed-strings','--no-heading','--max-count','30']
    for term in n['search']:
        cmd.extend(['-e',term])
    cmd.extend(str(p.relative_to(WORK)) for p in context_files)
    result = subprocess.run(cmd,cwd=WORK,text=True,capture_output=True)
    assert result.returncode in (0,1), (n['id'],result.stderr)
    matches=[]
    for hit in result.stdout.splitlines():
        path,line,excerpt=hit.split(':',2)
        matches.append(dict(file=path,line=int(line),excerpt=excerpt[:160],excerpt_truncated=len(excerpt)>160))
    search_records.append(dict(note_id=n['id'],terms=n['search'],
        mode='Literal case-insensitive rg; at most 30 matching lines per file; excerpts limited to160characters; navigation aid, not an absence proof',
        command=cmd, matches=matches, context_comparison=n['comparison']))
(DOC/'context_searches.json').write_text(json.dumps(search_records,ensure_ascii=False,indent=2)+'\n')
(DOC/'research_items.json').write_text(json.dumps(all_notes,ensure_ascii=False,indent=2)+'\n')

intro = r'''# Research notes — MPL_57_133–179

## Scope and answers to the carry-forward questions

**No completed second manuscript witness of cote 47’s Fourier compatibility check was identified in these 43 frozen pages.** The expressly unfinished comparison at 57:144 is a different Kummer/transgression identity for a generalized-Jacobian torsor; FW01–FW07 specify the objects, the map still to be checked, and the limits of the earlier proof leads.

**No earlier textual form of any of cote 44’s Theorems 1–7 was identified in this selection.** JAC01–JAC07 compare each exact target separately with its closest current passage; ordinary Picard schemes, curve Jacobians, projective frames, divisor deformation, and surface intersection calculations do not by themselves state that higher-cycle programme, and JAC08 explains why the available dates do not establish priority.

The transcription was frozen at **2026-11-18 08:54:59 UTC**, before the context archive was opened. These notes are research and interpretation only: no page fragment or combined transcription was changed because of the context, a published theorem, or a mathematical correction. Source assertions, corrections already visible on the source, proposed arguments, checked examples, and uncertain readings have separate note kinds; the four-sentence limit applies to each note’s discussion, with its source and search metadata recorded separately.

The root read every whole scan and both supplied halves in one sequential transcription stream and performed the second image audit. Post-freeze research comparisons were delegated in parallel: one researcher compared cote 47, one compared all seven cote 44 targets, and one read the entire supplied Hua file and the later-package notes; the root reviewed their findings and the cited relevant passages, and independently checked the principal counterexamples. No research collaborator read the manuscript scans or changed the transcription.

### Source key and locator convention

| Key | File or source | Status and location convention |
|---|---|---|
| P57 / P57(n) | `pages/MPL_57_133-179_57_scanNNN.tex` | Current frozen diplomatic text; `57:n Lx–y` means the approximate line in that individual page file, not a reconstructed manuscript line. |
| CT | `context/MPL_16+47+54+44_transcription.tex` | Supplied earlier transcription; cited by cote:scan and, where useful, aggregate TeX lines. Its original scans were not re-audited here. |
| CN | `context/MPL_16+47+54+44_notes.md` | Earlier research claims and leads; its F- and D-items retain that status. |
| SN | `context/same_cote_57/MPL_57_271-315_notes.md` | First-pass notes, cited by item and reported scan; their underlying scans were not available in this task. |
| RS | `context/notes/RESULTS_STATE.md` | Read in full before writing the notes; every item below names the entries on which it bears. A registered “Proved” is the return’s claim unless the register says reviewed. |
| HUA | Michel Hua’s project, `context/hua_project/57.modern.tex`, with its README | AI-produced modernization and interpretation, credited by titled section and text lines; it corrects and reorganizes material and is not another diplomatic witness. Its local page numbers here ordinarily equal scan number minus one. |
| L96 | Gérard Laumon, *Transformation de Fourier généralisée* (1996), §1.1 and §1.2 | Primary comparator, especially printed p. 5; bibliographic link below. |

The `context/` paths refer to the supplied context archive and are not duplicated in the returned ZIP. The source-key distinction matters: a reference to SN or CN reports what an earlier run says, not a new verification of its underlying scan or external citation. Oda’s supplied PDF was not needed for either carry-question and was not independently checked in this run; no Oda result is promoted to verified status here.

Each note has a recorded literal search across the supplied context texts in `documentation/context_searches.json`; these searches locate related words and objects, while the comparison field identifies the passages actually relevant and whether the current evidence adds, differs, or fails to supply the point. The complete Hua file was reviewed in the delegated research, with a coverage map in `documentation/research_picard_context.md`; its material outside this selection is not silently treated as newly transcribed or checked source evidence.

`WG2 §1.1 #3` is the broad dossier/Book II planning entry, not a theorem. Where it is the sole relevant RS entry, the link is explicitly only orientation or dossier identification; no unrelated theorem ID is manufactured for a reused leaf, an editorial title, or a local mathematical correction. `EXIT_TOWER A.5` is cited from the headline checkpoint-28 summary in RS, not from a separately reproduced proof.
'''

sections=[]
for n in all_notes:
    if n['section'] not in sections:
        sections.append(n['section'])
out=[intro]
for sec in sections:
    out.append('\n## '+sec+'\n')
    if sec.startswith('Standing question: steps'):
        out.append('\nThe entries distinguish authorial question marks, admitted inputs, future-proof promises, and drafting requests. An editor’s `\\unsure` mark is not itself an authorial doubt; SF08 is tentative because its reading is doubtful, and SF14 is an annotated-source flag whose hand is not securely attributed.\n')
    if sec.startswith('Standing question: title'):
        out.append('\nThese are documentary notes; their RS links concern dossier identity and the limits of chronology, not the truth of the mathematical claims. Printed page numbers, section numbers, archival foliation, scan numbers, and an authorial page count are kept distinct.\n')
    for n in (a for a in all_notes if a['section']==sec):
        out.append(f"\n### {n['id']} — {n['title']}\n")
        out.append(f"\n**File/scan:** P57, {n['where']}  \n**Kind:** {n['kind']}  \n**Brief source quote:** {n['quote']}  \n**Bears on RS:** {'; '.join(n['rs'])}  \n**Context search:** {' | '.join(n['search'])}  \n**Context comparison:** {n['comparison']}\n")
        if n.get('confidence'):
            out.append(f"\n**Own-idea confidence and reason:** {n['confidence']}\n")
        if n.get('refinement_id'):
            out.append(f"\n**Refinement identifier:** {n['refinement_id']}\n")
        out.append('\n'+n['body']+'\n')

out.append(r'''
## Status of the register entries used

| RS entry | Use in these notes | Status preserved |
|---|---|---|
| WG2 §2.4 #4 | Exact Fourier and seven-theorem carry-questions | Planning question; bounded negative findings for this selection. |
| WG2 §1.1 #3; WG2 §2.3 #12 | Dossier orientation and exact programme comparison | Unchecked planning/programme entries; no mathematical status upgrade. |
| WG H9 | Distinguishes a height/polarization conjectural reduction from surface intersection arithmetic | Unchecked hunch; not proved or refuted here. |
| LM7 E.23; LM6 E.21 | Abelian-layer and obstruction leads | Open section-class problems remain open. |
| ANABELIAN_149_PUSH A.1; SECTIONS_OVER_Q A.198; LM6 F.43; CYCLOTOMIC_KERNEL C1 | Kummer, generalized-Jacobian, and normal-line input comparisons | Carried at their claimed proved status; not rederived. |
| ANABELIAN_149_PUSH B.5 | Degeneration/inertia comparison | Known, according to the return; not rechecked as a theorem. |
| SECTIONS_OVER_Q B.15 | Boundary between ordinary rational-map extension and arithmetic sections | Open assertions remain open. |
| EXIT_TOWER A.5 | Stable-graph dimension bookkeeping | Headline claimed result; only the displayed polynomial specialization is checked here. |
| MPL_57_271-315 C04, D07, E08, J03 | Pinching, extension/splitting, torsion, and ordinary-endpoint leads | First-pass research notes; their underlying source pages and cited literature are not re-audited. |

The local refutations concern the unqualified readings specified in P03/N03/U03 and the other explicit tests, with refined statements identified in `CHECK_EVENTS.tsv`; they do not change RS statuses by implication. The check ledger distinguishes a documentary comparison, a targeted mathematical check, and a claim carried as background, and never counts transcription alone as a proof check.

## Primary external references actually consulted

- Gérard Laumon, [*Transformation de Fourier généralisée*](https://arxiv.org/pdf/alg-geom/9603004), 1996, §1.1; Theorem 1.2.4 and Lemma 1.2.5, printed p. 5: the particular comparator used in FW07.
- Uwe Jannsen, [*Continuous étale cohomology*](https://epub.uni-regensburg.de/26684/1/jannsen12.pdf), *Math. Ann.* 280 (1988), 207–245, Proposition 1.6, printed p. 211, and formula (3.1): the inverse-limit qualification in P06.
- A. Grothendieck et al., [*Revêtements étales et groupe fondamental (SGA 1)*](https://arxiv.org/pdf/math/0206203), recomposed edition: Exposé I §9, printed p. 13 (original p. 16; PDF p. 29), for the depth terminology in U03; Exposé X, Corollaries 3.3–3.4, for N06.
- The Stacks Project, [Tag 031S](https://stacks.math.columbia.edu/tag/031S): noetherian normality criterion used in N03–N04.
- The Stacks Project, [Tag 0BX7](https://stacks.math.columbia.edu/tag/0BX7): neighbourhood extension at a valuation local ring, used in N04.
- The Stacks Project, [Tags 0EMH](https://stacks.math.columbia.edu/tag/0EMH) and [0EMF](https://stacks.math.columbia.edu/tag/0EMF): sufficient hypotheses for the usual meromorphic-function sheaf, used only with the definition caveat in N02.
- The Stacks Project, [Tag 00NT](https://stacks.math.columbia.edu/tag/00NT), with [Tag 00N2](https://stacks.math.columbia.edu/tag/00N2) for terminology: maximal Cohen–Macaulay freeness, used in U03–U04.
- The Stacks Project, [Tag 0952](https://stacks.math.columbia.edu/tag/0952): the distinction between the stable Čech/local-cohomology construction and derived module torsion in U02.

The supplied modernized interpretation is credited separately as HUA above. Bibliographies or literature assertions in CN/SN were used as navigation leads only unless a primary source is explicitly listed here and its actual scope is recorded in the check ledger.
''')
(ROOT/'MPL_57_133-179_notes.md').write_text(''.join(out))
print(json.dumps({'notes':len(all_notes),'sections':len(sections),'context_searches':len(search_records),
                  'no_match_notes':[r['note_id'] for r in search_records if not r['matches']],
                  'notes_bytes':(ROOT/'MPL_57_133-179_notes.md').stat().st_size},ensure_ascii=False))
