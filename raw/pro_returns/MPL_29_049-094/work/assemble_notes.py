"""Assemble the research apparatus; never reads or rewrites the frozen TeX."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work'

intro = r'''# Research notes — MPL_29_049-094

**Cote 29; scans 049–094, excluding 079–081 and 083: 42 retained sheets.** These notes were written after the transcription was frozen at **2026-11-18 04:03:52 UTC** and the context was opened at **04:03:58 UTC**. They do not change any diplomatic reading. The primary reader alone transcribed and audited the images; the specialist collaborators worked only on research after the freeze, from the frozen text, the context and primary mathematical literature.

## How to read the evidence

Every item distinguishes a manuscript claim, an explicitly author-marked question, a contextual interpretation, and this run's own inference. “High confidence” records the strength of a displayed calculation or argument, not a claim of novelty or external review. The main note text is limited to one to four sentences per item; the complete proof calculations, source locators and review records are retained in the `work/` memoranda named below.

**Context convention.** All references to Hua mean **Hua, modernised reading of cote 29**, the AI-produced interpretation in the supplied `context/hua_project/29.modern.tex`, credited as required by its README. Its modern page number is one less than the scan number used in this package: modern 59 = scan 060 and modern 87 = scan 088. References to absent scans are explicitly contextual reports; no image verification of those leaves is claimed. The supplied `context/README.md` places the dossier at package 238, rank 24; `context/notes/RESULTS_STATE.md` was read before research integration, and its statuses remain the earlier runs' claims unless explicitly described there as reviewed.

**Results-state scope.** The direct formal-neighbourhood match is **29-formal-tame-pi1-self-intersection**; the notes test and refine components of that entry rather than accepting it wholesale. **LM1 E.11**, **LM1 E.2**, and the cote-56 entries **MPL_11_043-058+56 N063/N100** were compared, but the present material does not settle them. There is no directly matching registered theorem or open-item ID for the birational fundamental-group/Picard questions, and the individual notes state that absence rather than invent a connection.

## Findings and their exact scope

| Notes | Checked finding | Limit of the finding |
|---|---|---|
| N-FIN-06 | Finite torsor counts for every finite target do not imply topological finite generation of an arbitrary profinite group. | Corrects a converse in Hua's context; does not refute the separate geometric finiteness theorem. |
| BR04, BR06, BR11 | Arbitrary proper pullback can lower codimension; the arbitrary-field Bertini statement needs a geometric hypothesis; a fixed projective model repairs the birational limit argument. | The repairs are separated from the manuscript's original assertions. |
| BR13–BR14 | An explicit normal projective surface has a finite étale cover of its regular locus whose function-field extension cannot be étale on any proper model. | Answers the regular-locus extension question negatively; does not answer general essential constancy. |
| P04–P05, P11 | Tangent spaces alone, one Frobenius kernel alone, and the three numerical bounds alone are insufficient abstract criteria. | The counterexamples are not claimed to occur as the Picard schemes of the manuscript's fixed function field. |
| FORMAL-01, FORMAL-04, FORMAL-07 | Unconditional centrality, the all-positive-cohomology assertion for every curve, and the inference π₂=0 ⇒ splitting all fail in explicit examples. | The action, the P¹ exception, and the extension class must be retained separately. |
| FORMAL-10–FORMAL-12 | The unrestricted unique-divisibility claim for the Picard kernel fails; a root with its power isomorphism can still be lifted through nilpotent thickenings. | The full formal tame comparison and a blanket Picard inverse-limit isomorphism remain unproved here. |

Detailed arguments are in `work/birational_research.md`, `work/picard_research.md`, and `work/formal_research.md`; the last counterexample was separately challenged in `work/picard_formal_counterexample_check.md`. `CHECK_EVENTS.tsv` records actual proof checks, re-proofs, uses of background and refutations, with their scope; ordinary visual transcription is not counted as a mathematical check.

'''

def between(text, start, end):
    return text.split(start, 1)[1].split(end, 1)[0].strip()

def source_prefix(text, prefix):
    def replace(m):
        first = f'[{prefix}-S{m[1]}]'
        last = f'–[{prefix}-S{m[2]}]' if m[2] else ''
        locus = ', ' + m[3] if m[3] else ''
        return first + last + locus
    return re.sub(r'\[S(\d+)(?:–S(\d+))?(?:,\s*([^\]]+))?\]', replace, text)

root = (WORK / 'root_research.md').read_text()
root = root[root.index('## Orientation and scope'):]
root_head, root_tail = root.split('## Murre\'s exposition', 1)

br_full = (WORK / 'birational_research.md').read_text()
br = between(br_full, '## Suggested notes, each with a short final-note-sized text', '## Verification details')
br = source_prefix(br, 'BR')

p_full = (WORK / 'picard_research.md').read_text()
p = between(p_full, '## Proposed notes', '## Explicit checks')
p = source_prefix(p, 'P')
p = p.replace('A surjective closed immersion of proper group schemes',
              'A closed immersion of proper group schemes, surjective on underlying points,')

f_full = (WORK / 'formal_research.md').read_text()
f = between(f_full, '## Suggested notes for the final notes file', '## Appendix A')
f = f.split('### FORMAL-01', 1)[1]
f = '### FORMAL-01' + f
f = source_prefix(f, 'F')
f = re.sub(r'(?<!`work/formal_research.md`, )Appendix ([A-E])',
           r'`work/formal_research.md`, Appendix \1', f)
f = f.replace('For a finite constant coefficient group of order',
              'For a finite constant abelian coefficient group of order')
f = f.replace("**context:** Hua's diagonalizable-group material adjacent to the formal-neighbourhood sections;",
              '**context:** no dedicated treatment of the interleaved diagonalizable typescript was found in Hua; compare his formal-neighbourhood section, modern pp.87–93 / scans088–094;')

discrepancy = r'''### FORMAL-17 — An external torsion-invariance claim requires independent follow-up

**Witness:** cote 29, scan 094, “uniquement divisibles par n”. **Kind:** own idea / source discrepancy. **Context:** Hua, “Le cas où la classe s'annule : Picard formel”, modern p.93 / scan094. **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection. **Confidence:** high for the explicit example, checked independently twice; the external-source discrepancy is submitted for further expert review.

The version of [Stacks Lemma37.4.2, Tag0C6S](https://stacks.math.columbia.edu/tag/0C6S) retrieved in this run asserts an unqualified isomorphism on Pic[n] for thickenings, but FORMAL-10 gives a nonzero n-torsion element in its kernel. The full units–Picard exact sequence in the preceding lemma exposes the issue: H¹(I) is divided by the global-unit boundary, and in the example that image is Za, which is not n-saturated. Nilpotent invariance of H¹(μₙ) does not contradict this calculation, because the preceding units-modulo-nth-powers term in the Kummer sequence changes. The example, its regular formal extension and the independent challenge are supplied in full in the two formal-Picard work records; no claim of novelty is made and the disputed external statement is not used as a verified input.

'''

def table_sources(text, prefix):
    rows = []
    definitions = []
    for line in text.splitlines():
        if not re.match(r'\| S\d+ \|', line):
            continue
        cells = [x.strip() for x in line.strip('|').split('|')]
        key, title, url = cells[:3]
        scope = cells[4] if len(cells) >= 5 else 'Exact source locus inspected; scope is specified in the corresponding note.'
        ident = f'{prefix}-{key}'
        rows.append(f'| [{ident}] | {title} | {scope} |')
        definitions.append(f'[{ident}]: {url}')
    return '\n'.join(rows), '\n'.join(definitions)

br_rows, br_defs = table_sources(br_full, 'BR')
p_rows, p_defs = table_sources(p_full, 'P')
f_sources = between(f_full, '## Primary sources consulted and exact scope of use', '## Checks versus outstanding work')
f_sources = source_prefix(f_sources, 'F')
f_sources = f_sources.replace('Appendix D', '`work/formal_research.md`, Appendix D')
f_defs = []
for m in re.finditer(r'\*\*\[F-S(\d+)\]\*\*(.*?)(?=\n\n\*\*\[F-S|\Z)', f_sources, re.S):
    urls = re.findall(r'https?://[^\s;]+', m[2])
    if urls:
        f_defs.append(f'[F-S{m[1]}]: {urls[0].rstrip(".;") }')

standing_path = WORK / 'standing_sections.md'
standing = standing_path.read_text() if standing_path.exists() else '## Standing sections\n\nDraft integration pending.\n'
if standing.startswith('# '):
    standing = standing.split('\n', 1)[1].lstrip()
standing = standing[standing.index('## Standing section 1'):]

sources = '''## Primary-source register and verification limits

The links below point to the primary mathematical texts actually consulted. A theorem read and used as background is not represented as independently proved; the corresponding event says which occurred. References to the supplied context are evidence of that context's claims, not substitutes for a proof. The unverified distribution-source number385 is deliberately left unidentified.

### Birational references

| Key | Source and locus | Scope |
|---|---|---|
''' + br_rows + '\n\n### Picard references\n\n| Key | Source and locus | Scope |\n|---|---|---|\n' + p_rows + '\n\n### Formal-neighbourhood references\n\n' + f_sources + '\n\n' + br_defs + '\n' + p_defs + '\n' + '\n'.join(f_defs) + '\n'

final = (intro + root_head.strip() + '\n\n## Birational fundamental groups\n\n' + br +
         '\n\n## Birational Picard schemes\n\n' + p +
         '\n\n## Murre\'s exposition' + root_tail.split('## Context-only reading questions', 1)[0] +
         '\n\n## Formal tame inertia and Picard lifting\n\n' + f + '\n\n' + discrepancy +
         '## Context-only reading questions' + root_tail.split('## Context-only reading questions', 1)[1] +
         '\n\n' + standing.strip() + '\n\n' + sources)

# Metadata at the top defines the full path for every abbreviated Hua reference.
# Keep ordinary spacing in prose and note IDs, leaving mathematical strings intact.
final = final.replace('date30April1969', 'date 30 April 1969')
final = final.replace('LM1E.11', 'LM1 E.11').replace('LM1E.2', 'LM1 E.2')
final = final.replace('finding29-formal', 'finding 29-formal')
(ROOT / 'MPL_29_049-094_notes.md').write_text(final)
print(f'Wrote research notes: {len(final.split())} whitespace-delimited words; '
      f'{len(re.findall(r"^### (?:N-|BR|P\d|FORMAL-)", final, re.M))} main notes')
