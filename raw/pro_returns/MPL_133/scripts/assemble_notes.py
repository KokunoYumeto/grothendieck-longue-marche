#!/usr/bin/env python3
"""Assemble the post-freeze research report; never read or write a TeX file.

This records the integration step from the research drafts. After integration,
the drafts are reduced to proof/source supplements, so this historical script
must not be rerun on the reduced supplements. Use validate_package.py for final
read-only package checks.
"""
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / 'research'

def read(name):
    return (R / name).read_text()

def cut(text, start, end=None):
    out = text.split(start, 1)[1]
    return out.split(end, 1)[0] if end else out

def portable(text):
    text = re.sub(r'genui.*?', '', text)
    text = text.replace('proposed by root and checked here', 'calculated and independently checked for this report')
    text = text.replace('The independent root check', 'The independent check')
    return text.strip()

s = read('synthesis_and_registers.md')
w = read('quadratic_and_misc.md')
f = read('finite_sets.md')
b = read('binomial_bridge.md')
g = read('formal_groups.md')

intro = s[s.index('## Scope and evidentiary conventions'):s.index('## Standing register I')]
registers = s[s.index('## Standing register I'):]
intro = intro.replace('What do the two Hua findings survive?', 'How do the two Hua findings fare?')
intro += '''
## How to use the notes

There are **76 numbered notes**: W01–W16 on quadratic Witt theory and adjacent calculations; P01–P05 on the printed Laborde offprints; F01–F16 on finite sets and representation rings; B01–B11 on the binomial/cochain comparison; G01–G21 on formal and algebraic groups; J01–J05 on Go; and M01–M02 on reused material. Each numbered item's explanatory body is limited to one to four sentences; source, kind, confidence, context, and register fields are metadata. “Own idea” and “own verification” identify calculations made for this report, with their hypotheses and confidence, without any claim of historical novelty.

Longer checks are in [quadratic proof checks](research/quadratic_proof_checks.md), [finite-set calculations](research/finite_sets.md), and [formal/algebraic-group proofs](research/formal_groups.md). The binomial supplement preserves context-search and source-version details. All context paths are relative to the supplied context archive; those source files are intentionally not reproduced in this package. In particular **PS §137 is a section of Pursuing Stacks, not Montpellier cote 137**.

'''

w_main = cut(w, '## Quadratic Witt theory and its qualifications', '## Primary references used in these notes')
w_core, w_misc = w_main.split('## Go calculations and other reused material', 1)
w_core = '## Quadratic Witt theory and adjacent calculations\n' + w_core

f_main = cut(f, '### F01', '## Independent calculations and precise limits')
f_main = '### F01' + f_main
fkind = {
'F01':'unpursued implication / literature comparison',
'F02':'own idea / counterexample',
'F03':'own idea / reconstruction of the surviving decomposition',
'F04':'own idea / counterexample',
'F05':'own idea / counterexample',
'F06':'unpursued implication / literature comparison',
'F07':'own idea / scope check',
'F08':'unpursued implication',
'F09':'unpursued implication / context comparison',
'F10':'reading question / notation distinction',
'F11':'own idea / counterexample',
'F12':'unpursued implication / own integral-lattice check',
'F13':'own idea / obstruction to a proposed splitting',
'F14':'own idea / proof of the closure assertions',
'F15':'reading question / grading clarification',
'F16':'own idea / register scope check',
}
for ident, kind in fkind.items():
    f_main = re.sub(rf'^### {ident} — .*? — (scans? .+)$',
                    lambda m: f'### {ident} — {kind} — cote 133, {m.group(1)}',
                    f_main, flags=re.M)
f_main = f_main.replace('as detailed below', 'as detailed in the finite-set supplement, Appendix C')
f_main = f_main.replace('as verified below', 'as verified in the finite-set supplement, Appendix D')
f_main = f_main.replace('the integral-lattice check is recalled below', 'the integral-lattice check is in the finite-set supplement, Appendix E')
f_main = f_main.replace('This characteristic-zero comparison is compatible with the coefficient extraction on scan 029, while F11 prevents its unrestricted extension to local base rings.', 'This characteristic-zero comparison is compatible with the coefficient extraction on scan 029, while F11 prevents its unrestricted extension to local base rings; **confidence: high for the complex case**, by the Schur-basis and Jacobi–Trudi calculation in the supplement.')

b_main = '### B01' + cut(b, '### B01', '## Context-search record')
bkind = {
'source observation / boundary on the planning inference':'reading question / scope of the assertion',
'context comparison / correction of a possible historical overreading':'unpursued implication / contextual withdrawal and replacement question',
'literature comparison / scope qualification':'unpursued implication / literature comparison',
'literature comparison, with a bounded historical inference':'unpursued implication / literature comparison',
'source boundary / results-state reconciliation':'reading question / results-state reconciliation',
}
for old, new in bkind.items():
    b_main = b_main.replace(f'**Kind:** {old}.', f'**Kind:** {new}.')
b_main = b_main.replace('**Kind:** literature comparison.', '**Kind:** unpursued implication / literature comparison.')

# Context fields are metadata, kept next to each B note as well as in the ledger.
b_context = {}
for line in b.splitlines():
    m = re.match(r'\| (B\d\d) \| (.*?) \| (.*?) \|$', line)
    if m:
        b_context[m.group(1)] = (m.group(2), m.group(3))
parts = re.split(r'(?=^### B\d\d )', b_main, flags=re.M)
for i, part in enumerate(parts):
    m = re.match(r'### (B\d\d)', part)
    if m and m.group(1) in b_context:
        loc, rel = b_context[m.group(1)]
        parts[i] = part.rstrip() + '\n\n**Context-search metadata:** ' + loc + ' — ' + rel.rstrip('.') + '\n\n'
b_main = ''.join(parts)

g_main = '### G01' + cut(g, '### G01', '## Context search record')
gkind = {
'literature comparison; conditional diagnostic':'own idea / conditional counterexample',
'observation; evidence boundary':'self-flagged / unproved claim',
'observation; reading question':'reading question / unproved claim',
'supplied-context comparison':'unpursued implication / context comparison',
'literature comparison; notation':'reading question / literature comparison',
'own verification; literature comparison':'own idea / verification',
'literature comparison; notation question':'reading question / literature comparison',
'literature comparison; own distinction':'own idea / distinction between subgroup objects',
'evidence boundary':'unproved claim / scope question',
'own verification from primary-source inputs':'own idea / family construction',
'register correction; own verification':'own idea / correction of the supplied register gloss',
'own counterexample, proposed by root and checked here':'own idea / counterexample',
'literature comparison':'unpursued implication / literature comparison',
'own verification; observation':'self-flagged / own verification',
'own diagnostic example; source-status observation':'withdrawn in the same text / own counterexample',
'own verification; notation caution':'own idea / counterexample to automatic surjectivity',
'own verification':'own idea / verification',
'own consequence':'own idea / consequence',
}
for old, new in sorted(gkind.items(), key=lambda kv: -len(kv[0])):
    g_main = g_main.replace(f'**Kind:** {old}.', f'**Kind:** {new}.')
g_main = g_main.replace('the crossed-module entry', '**Hua: 133-centre-and-derived-group-from-two-crossed-modules**')
g_main = g_main.replace('the crossed-module twisting formula', 'the twisting formula in **Hua: 133-centre-and-derived-group-from-two-crossed-modules**')
g_main = g_main.replace('the affine-quotient entry', '**Hua: 133-affine-quotient-not-constructible**')
g_main = g_main.replace('Appendix B', 'the formal-group supplement, Appendix B')
g_main = g_main.replace('Appendix C', 'the formal-group supplement, Appendix C')
g_main = g_main.replace('Appendix D', 'the formal-group supplement, Appendix D')
g_main = g_main.replace('**Register:** structural background, not a novelty claim.', '**Register:** structural background for **Hua: 133-affine-quotient-not-constructible**; no novelty claim')
g_main = g_main.replace('**Register:** consequence of the live formulas, not a new status claim.', '**Register:** consequence within **Hua: 133-centre-and-derived-group-from-two-crossed-modules**; no new status claim')
g_main = g_main.replace('**Register:** related background, not an additional established Hua claim.', '**Register:** related background to **Hua: 133-centre-and-derived-group-from-two-crossed-modules**; no formal-group theorem established')

g_intro = r'''## Formal groups, affinization, and crossed modules

The checks distinguish the manuscript's **largest affine quotient** from the Chevalley affine **subgroup**. For the ordinary-group calculations, write $N\triangleleft G$, $N'\leq Z(G)$, $C=N\cap N'=\pi_1$, $Q=G/NN'=\pi_0$, $M=G/N'$, $M'=G/N$, and $K=G/C$; conjugation gives $\theta:M\to\operatorname{Aut}(N)$. The derived-subgroup notes G18–G21 additionally assume $G'\subseteq N$, so $Q$ is abelian; the prime in the manuscript's $M'$ names a second quotient and does not mean the derived subgroup of $M$.

'''

# Gather APA entries, retaining version/locator qualifications but no tool IDs.
refs = []
for line in cut(w, '## Primary references used in these notes').splitlines():
    if line.startswith('- '):
        refs.append(line[2:])
f_refs = cut(f, '## Primary literature, APA references, and verification locators', '## Integration priorities')
for block in re.split(r'^### ', f_refs, flags=re.M)[1:]:
    paras = block.split('\n\n')
    if len(paras) > 1:
        refs.append(paras[1].strip())
refs += [p.strip() for p in cut(b, '## APA bibliography').split('\n\n') if p.strip()]
for m in re.finditer(r'^\d+\. \*\*(.*?)\*\*(.*?)(?=^\d+\. \*\*|^\*\*Supplied-source citations|\Z)', cut(g, '## APA references and exact checked locators'), re.M|re.S):
    text = m.group(1) + m.group(2)
    text = re.sub(r'\s+Retrieval:.*?(?=\n\n|\Z)', '', text, flags=re.S)
    refs.append(text.strip())
refs = list(dict.fromkeys(portable(x) for x in refs))
refs.sort(key=lambda x: unicodedata.normalize('NFKD', x).casefold())
reftext = '\n\n'.join('- ' + x.replace('\n', '\n  ') for x in refs)

version_note = '''## Reference and version qualifications

References follow author–date APA conventions, with exact sections or theorem locators in the notes. Horel's journal article was published in 2024; numbered technical statements here were checked in **arXiv:2211.02349v2 (23 March 2025)**, with the publisher's abstract and metadata checked separately, and are cited as Horel (2025). Dress–Siebeneicher (1988, 1989) are used only at the accessible indexed publisher-abstract level, with the one-page 1986 announcement independently read; no numbered theorem in their inaccessible full papers is claimed checked. Other version qualifications are retained in the references and supplements.

The manuscript and supplied context remain the primary evidence for what Grothendieck wrote: **cote 133**, scan numbers in each note; **Pursuing Stacks**, the supplied chapter VI–VII files and original page/section markers; **README.md** and **notes/RESULTS_STATE.md**, named headings and IDs. The externally checked 2021 PS edition record is bibliographic context, not a substitute for the supplied text or its pagination. The two Laborde offprints are cited from the supplied scans. Source PDFs and the supplied archives are not included in the deliverable.

## References

'''

out = '# MPL 133 — Research notes\n\n' + intro + w_core + '\n## Finite-set operations and representation rings\n\n' + f_main + '\n## Binomial operations and integral homotopy\n\n' + b_main + '\n' + g_intro + g_main + '\n## Go calculations and reused material\n\n' + w_misc + '\n' + registers + '\n' + version_note + reftext + '\n'
out = portable(out) + '\n'
ids = re.findall(r'^### ([WPFBGJM]\d\d)\b', out, re.M)
assert len(ids) == len(set(ids)) == 76, (len(ids), len(set(ids)))
assert '\\documentclass' not in out
(ROOT / 'MPL_133_notes.md').write_text(out)
print({'notes':len(ids), 'words':len(out.split()), 'references':len(refs), 'file':'MPL_133_notes.md'})
