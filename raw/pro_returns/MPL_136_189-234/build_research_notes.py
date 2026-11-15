"""Render research notes and record a context search for every individual note.

This tool never modifies page files, the combined transcription, or their hashes.
"""
from pathlib import Path
import csv
import re
from datetime import datetime, timezone
from research_items import ITEMS

ROOT = Path(__file__).resolve().parent
CONTEXT = ROOT.parent / 'context'
PREFIX = 'MPL_136_189-234'
SECTIONS = [
    'Answers to the package questions',
    'Endomorphisms and universal operations',
    'The four complexes and divided powers',
    'Normalization and the homotopy argument',
    'Earlier findings and the literature',
    'Research points on reused typescript',
    'Standing question: steps marked as unverified',
    'Standing question: titles, foliation, and page counts',
]

HEADER = r"""# Research notes — MPL_136_189-234

## Scope, status, and citation conventions

These notes were written after the 45 per-page transcriptions and the combined fragment were audited and frozen with SHA-256 hashes. They are independent mathematical and documentary commentary: a proposed reading, correction, proof, or counterexample here has not been inserted into the frozen transcription. The retained range is cote **136**, PDF scans **189–234**, excluding the omitted blank scan **214**. Approximate locations use the displayed proposition, paragraph, or formula; exact searchable wording remains in the page files.

The context examined comprises `README.md`, `notes/RESULTS_STATE.md`, `PURSUING_STACKS_CONTENTS.md`, and `ps_chapters_VI_VII/ps6.tex` and `ps7.tex`. The earlier cote-136 probe return, the full text of *Pursuing Stacks* §94, the original research returns behind the register, and the missing continuations of the reused typescript are **not** included. References below to `ps6.tex` or `ps7.tex` mean the files in `ps_chapters_VI_VII/`; their page numbers are the original manuscript pagination marked by `\pspage`, **not** PDF scan numbers in cote 136. When the supplied context has no matching scan-based source, that absence is stated rather than inventing a scan reference.

The register’s status labels are treated as claims of the corresponding runs, subject to its explicit review annotations; its PRETOT/TOTEX review record does not confer reviewed status on the Hua findings or the war-game questions. The two Hua entries are independently assessed in R043–R044. A note marked **own idea** supplies a confidence level and a reason, and makes no novelty claim. An **unproved claim** label means that the needed proof is not complete in these retained leaves, not that the assertion is false or unknown in the literature. Reused typescript is identified as such, and the Stoia article retains its explicit authorship.

`context_search_log.csv` records regex searches against every supplied context text for every note, with counts and short locators. Negative findings are limited to this corpus and these scans. The external literature is cited in author–date form, with primary publication, author-hosted, or official documentation links in the references; the access-status table distinguishes inspected arguments from bibliographical leads.

## Answers at a glance

| Question | Finding and detailed notes |
|---|---|
| Functorial integral cochains? | The manuscript explicitly claims a functorial **weightwise truncated additive comparison** for every base ring, including the integers; see R001–R002 and R034–R041. |
| Ordinary cup products and divided powers without qualification? | The weight and PD ideal are essential: already at a point, products have binomial coefficients, and the stronger unweighted PD interpretation fails; see R003–R004, R022, and R046–R047. |
| “Topos de De Rham” and its “faisceautisation”? | No definition is present in this packet; later PS material offers related topos questions, not an identification; see R005. |
| “Constructions universelles” and lecture plan? | Concrete free-PD and normalization constructions are present, together with a local sequence of working headings, but no full lecture plan or dated title leaf; see R006–R007 and TC04–TC08. |
| Abelian varieties or Chern classes of a Fourier transform? | Abelian schemes occur on reused typescript; no such handwritten lecture example or Fourier-transform Chern-class example is present; see R008 and R055–R065. |

In the formulas below, $p$ denotes the manuscript’s total weight and $i$ its exterior/cohomological degree unless a note explicitly discusses a different convention. The phrase “characteristic zero” in the relevant manuscript calculation is interpreted using its own explicit gloss “a $\mathbb Q$-algebra”; R028 explains why that qualification matters.
"""

def search_context():
    paths = [CONTEXT/'README.md', CONTEXT/'PURSUING_STACKS_CONTENTS.md',
             CONTEXT/'notes/RESULTS_STATE.md', CONTEXT/'ps_chapters_VI_VII/ps6.tex',
             CONTEXT/'ps_chapters_VI_VII/ps7.tex']
    texts = {}
    for p in paths:
        page = None
        lines = []
        for lineno, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            tags = re.findall(r'\\pspage\{([^}]+)\}', line)
            if tags:
                page = tags[-1]
            lines.append((lineno, page, line))
        texts[p.relative_to(CONTEXT).as_posix()] = lines
    total = 0
    with (ROOT/'context_search_log.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['note_id','regex','context_file','matching_lines','first_locators','short_matching_text'])
        for item in sorted(ITEMS, key=lambda x:x['id']):
            for query in item['queries']:
                regex = re.compile(query, re.I)
                for name, lines in texts.items():
                    matches = [row for row in lines if regex.search(row[2])]
                    locators = '; '.join(f'line {n}'+(f', ms p. {page}' if page else '') for n,page,_ in matches[:3])
                    snippets = ' || '.join(line.strip()[:160] for _,_,line in matches[:3])
                    writer.writerow([item['id'],query,name,len(matches),locators,snippets])
                    total += 1
    return total

def render():
    ids = [item['id'] for item in ITEMS]
    assert len(ids) == len(set(ids)), 'duplicate IDs'
    assert set(i['section'] for i in ITEMS) == set(SECTIONS)
    assert set(f'R{i:03}' for i in range(1,68)).issubset(ids)
    out = [HEADER.rstrip()]
    for section in SECTIONS:
        out.append('\n## '+section+'\n')
        for item in sorted((x for x in ITEMS if x['section']==section), key=lambda x:x['id']):
            out.append(f"### {item['id']} — {item['title']}\n")
            out.append(f"**File/scan:** cote 136, scan(s) {item['scans']}. **Location:** {item['anchor']}.  ")
            out.append(f"**Kind:** {item['kind']}. **RESULTS_STATE connection:** {item['results']}."+
                       (f" **Confidence:** {item['confidence']}." if item['confidence'] else '')+'\n')
            for sentence in item['sentences']:
                out.append(sentence+'\n')
    out.append((ROOT/'research_references.md').read_text(encoding='utf-8'))
    target = ROOT/f'{PREFIX}_notes.md'
    target.write_text('\n'.join(out).rstrip()+'\n', encoding='utf-8')
    searches = search_context()
    with (ROOT/'progress.log').open('a', encoding='utf-8') as f:
        f.write(f"research notes rendered {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}; {len(ITEMS)} items; {searches} context query/file records; no transcription writes\n")
    print(f'{len(ITEMS)} notes; {searches} query/file records; {len(target.read_text().split())} whitespace-delimited words')

if __name__ == '__main__':
    render()
