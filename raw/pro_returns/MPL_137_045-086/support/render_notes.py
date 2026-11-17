#!/usr/bin/env python3
"""Render research notes and perform a separate context search for every item.

Only the notes and research support records are written. The 43 frozen
transcription hashes are checked before and after; page text is never changed.
"""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib, json, re, runpy, subprocess

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
CONTEXT=BASE/'context'
MANIFEST=json.loads((ROOT/'support/frozen_hashes.json').read_text())
def hashes_ok():
    for rel,digest in MANIFEST.items():
        assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==digest, rel
hashes_ok()
items=runpy.run_path(str(ROOT/'support/main_notes_data.py'))['ITEMS']
standing=json.loads((ROOT/'support/standing_register.json').read_text())['entries']
relations={
'U01':'restates','U02':'qualifies','U03':'adds cancelled drafting evidence','U04':'qualifies',
'U05':'restates','U06':'restates','U07':'differs','U08':'adds cancelled drafting evidence',
'U09':'adds proof and image questions','U10':'adds a marginal qualification','U11':'differs',
'U12':'differs','U13':'restates','U14':'qualifies','U15':'restates','U16':'qualifies',
'U17':'adds coherence obligations','U18':'restates','U19':'restates','U20':'differs',
'U21':'restates','U22':'adds an explicit omission','U23':'restates','U24':'restates',
'U25':'adds a proposed reduction','U26':'restates','U27':'qualifies','U28':'adds an unscoped question',
'U29':'restates the abstract question; adds the manuscript assertion for the example',
'U30':'restates','T01':'differs','T02':'restates','T03':'adds a bounded negative finding',
'T04':'adds a pagination distinction'}
for row in standing:
    row['section']='Standing register: authorial flags, abbreviated proofs and later resolutions' if row['id'].startswith('U') else 'Standing register: titles, covers and page counts'
    row['title']=row['kind'][0].upper()+row['kind'][1:]
    row['confidence']=''
    row['relation']=relations[row['id']]
    if row['id'].startswith('U'):
        original=row['kind']
        if 'withdrawn' in original: row['kind']='withdrawn in the same text'
        elif row['id'] in {'U05','U09','U13','U17','U20','U24','U25','U27'}: row['kind']='unproved claim / abbreviated verification'
        elif row['id'] in {'U18','U19'}:row['kind']='unpursued implication / explicit scope qualification'
        else:row['kind']='self-flagged: '+original
    row['context']='Context comparison — '+row['relation']+': '+row['context']
    row['ids']='; '.join(row['ids']) if row['ids'] else 'No directly matching result entry; the contextual comparison is local.'
    row['body']=row['body'].replace('context_comparison.md','support/context_comparison.md')
    row['body']=re.sub(r'\bScan(?=\d)', 'Scan ',row['body'])
    row['body']=re.sub(r'\bscans(?=\d)', 'scans ',row['body'])
    row['body']=re.sub(r'\bscan(?=\d)', 'scan ',row['body'])
    row['body']=re.sub(r'\bon(?=\d)', 'on ',row['body'])
    row['body']=row['body'].replace('42 scans,045','42 scans, 045').replace('foliation44','foliation 44')
    row['context']=row['context'].replace('two137','two 137').replace('page47','page 47')
    row['context']=row['context'].replace('pp.506','pp. 506').replace('p.521','p. 521')
    if row['id']=='U29':
        row['context']='Context comparison — qualifies: Hua, “Questions ouvertes” (lines 1940–1952), leaves the abstract question open, but labels its module answer as his own; existence and canonicity in that example are already asserted on 086, while his explanation adds a positive-degree restriction.'
standing.append(dict(id='T05',scan='045–086',location='all whole-page and half-page audits; local headings 058, 072, 075, 078',kind='unpursued implication / documentary scope',status='no cover, authorial total count or date identified in this range',quote='',body='No title sheet, cover, author-written total page count or author-written date was identified in the 42 supplied scans. The catalogue title and approximate 1975–1976 dating belong to the supplied task description, not to a newly found title or date on these sheets.',context='Context comparison — differs in scope: the context README and Hua’s folder title describe the whole cote, whereas the present range contains local headings on 058, 072, 075 and 078, together with the numbering distinctions in T03–T04.',ids='WG2 §Week #3 (unchecked plan); no numerical page-count result entry applies.',terms='(?i)(foldertitle|1975|1976|title|titre|pages|count)',section='Standing register: titles, covers and page counts',title='No cover or authorial total page count in this excerpt',confidence=''))
standing.extend([
    dict(id='T06',scan='058',location='top; TeX line 3',kind='reading question / local heading',status='heading retained with its lexical and alphabet doubts',quote=r'Construction \unsure{intrinsèque} de $\unsure{\mathcal P|P}$ ($k$-lin.)',body='This local heading opens the intrinsic construction and its ensuing conditions, with the adjective and category alphabet left uncertain. It supplies no separate cover title, date or page count.',context='Context comparison — differs: Hua, “Les conditions a) à e)” (lines 1427–1429), prints “Construction canonique”; this is a competing reading, not additional visible text on the scan.',ids='137-perfect-complexes-universal-sigma-exact (candidate; not independently reviewed)',terms=r'intrinsèque|Construction canonique|conditions a|137-perfect',section='Standing register: titles, covers and page counts',title='Heading of the intrinsic construction',confidence=''),
    dict(id='T07',scan='072',location='opening; TeX line 3',kind='unpursued implication / local heading',status='surviving thematic heading',quote=r'\uline{Applications}',body='The heading introduces applications of the universal multiplicative constructions, followed by Ex. 1 on 072 and Ex 2 on 073. These examples belong under this local heading within the excerpt.',context='Context comparison — restates with different subdivisions: Hua places the corresponding material under “Le cup-produit” (line 1666) and “Le complexe de De Rham à puissances divisées” (line 1693), which are editorial section titles rather than replacements for the source wording.',ids='MPL_133 B06 (first-pass lead); 137-perfect-complexes-universal-sigma-exact (candidate; not independently reviewed)',terms=r'Applications|cup-produit|complexe de De Rham|B06',section='Standing register: titles, covers and page counts',title='Applications heading',confidence=''),
    dict(id='T08',scan='078',location='top; TeX line 3',kind='unpursued implication / local heading',status='surviving thematic heading within the polynomial-category discussion',quote=r'\uline{Relations avec op.} $\otimes$ \uline{et} $\Gamma^p$.',body='This heading introduces the relations of the polynomial-category structure with tensor products and divided powers. Its abbreviation “op.” and exponent $p$ remain as transcribed.',context='Context comparison — restates: Hua’s corresponding subsection is “Produits tensoriels et puissances divisées” (line 1788), a modernized heading for the same local subject.',ids='137-polynomial-categories-pd-tensor-categories (candidate; not independently reviewed)',terms=r'Produits tensoriels et puissances|Relations|137-polynomial',section='Standing register: titles, covers and page counts',title='Heading on tensor products and divided powers',confidence=''),
    dict(id='T09',scan='052',location='TeX line 5; heading within the cancelled block',kind='withdrawn in the same text / cancelled subheading',status='proof-outline heading struck out with its block',quote=r'\uline{Indications sur dém.}',body='The heading belongs to a cancelled outline following the theorem, whose drafting status is recorded in U03. It is a subordinate proof heading and gives no title or extent for a separate packet.',context='Context comparison — adds cancelled drafting evidence: Hua’s “Le théorème” and its “Démonstration” organize the live argument but do not preserve this cancelled heading as a separate documentary item.',ids='137-perfect-complexes-universal-sigma-exact (candidate; not independently reviewed)',terms=r'Indications|Démonstration|Le théorème|137-perfect',section='Standing register: titles, covers and page counts',title='Cancelled proof-outline heading',confidence='')
])
items.extend(standing)
assert len(items)==len({x['id'] for x in items})
for item in items:
    for field in ('body','context','location','title'):
        item[field]=re.sub(r'\b(in|on|cote|Cote|scan|pages|the|all|of|lines|examples|headings)(?=\d)',r'\1 ',item[field])
    item['location']=re.sub(r'([;,])(?=\S)',r'\1 ',item['location'])

# A real independent rg invocation for each note, against every supplied md/tex.
# Preserve counts and concise file/line examples without copying source files.
searches=[]
for item in items:
    pattern=item['terms']
    args=['rg','--json','-i','--glob','*.md','--glob','*.tex',pattern,str(CONTEXT)]
    result=subprocess.run(args,capture_output=True,text=True,check=False)
    assert result.returncode in (0,1), (item['id'],result.stderr)
    by_file=defaultdict(list)
    for line in result.stdout.splitlines():
        obj=json.loads(line)
        if obj['type']!='match':continue
        data=obj['data']; file=str(Path(data['path']['text']).relative_to(BASE))
        by_file[file].append(dict(line=data['line_number'],text=data['lines']['text'].strip()))
    samples={}
    scans=[int(x) for x in re.findall(r'\d{3}',item['scan'])]
    for file,hits in by_file.items():
        selected=hits[:3]
        if file.endswith('137.modern.tex') and scans:
            n=min(scans)
            lo,hi= ((1141,1273) if n<=48 else (1274,1424) if n<=57 else
                    (1425,1546) if n<=64 else (1547,1692) if n<=72 else
                    (1693,1717) if n<=74 else (1718,1939) if n<=84 else (1940,1968))
            focused=[h for h in hits if lo<=h['line']<=hi]
            selected=(focused[:6] or hits[:6])
        samples[file]=selected
    searches.append(dict(id=item['id'],pattern=pattern,files_searched='all supplied context *.md and *.tex',match_counts={k:len(v) for k,v in sorted(by_file.items())},samples=samples,comparison=item['context'],result='matches' if by_file else 'no matches'))
(ROOT/'support/context_searches.jsonl').write_text(''.join(json.dumps(v,ensure_ascii=False)+'\n' for v in searches))
(ROOT/'support/research_items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')

HEADER=r'''# Research notes — cote 137, scans 045–086

These English notes were written only after the diplomatic transcription was frozen at **2026-11-17 21:38:33 UTC**, and after the context archive was opened at that recorded time following the freeze. All42 page fragments and their ordered concatenation remain unchanged; their43 SHA-256 values are checked again at the end of the work. No interpretation below changes a letter, formula, deletion, diagram or doubt mark in the transcription.

## Scope and how to use the notes

The report contains **65 main notes**, **30 entries in the authorial-flags register**, and **nine title/page-count entries**. Each item is a separate short note with a cote/scan locator, kind, contextual comparison and relevant RESULTS_STATE identifiers; own ideas carry a confidence and reason, and none is claimed to be new. The authorial-flags register also records questions subsequently answered, withdrawn routes, compressed verifications and explicit scope qualifications: it is not a list of30 still-open conjectures.

Locations such as “TeX line” refer to the frozen per-page fragment, while “top/middle/bottom” refers approximately to the physical page; the very long paragraphs on063,064,073 occupy one source line each. Research formulas use readable mathematical notation for explanation, including plain P and Q where appropriate; they do not resolve the recurring P/font doubts in the diplomatic text. Exact short quotations in the standing register retain the source macros where they matter, and an editorial doubt marker is never treated by itself as an authorial question.

| Requested issue | Relevant notes |
|---|---|
| Meaning of “structures multiplicatives”; strict cosimplicial versus cochain commutativity | M01–M10 |
| Integral homotopy reconstruction and bridge B7 | M11–M14; R01–R07; R12–R16 |
| What “Witt” in cote133 may mean, and the finite-set comparison | R09–R11 |
| Abelian varieties, Fourier transforms and Chern classes | R08 |
| Manuscript's own unverified steps and retractions | U01–U30 |
| Titles, covers, page counts and pagination | T01–T09 |

## Sources and status conventions

The full supplied RESULTS_STATE file and the full Hua modernised reading were read before writing these notes. The two supplied PS chapters were searched throughout, and the relevant passages cited below were read in context; this is not a claim to have read every line of both chapters. A separate search was performed for every one of the 104 notes, using its objects, notation or words; the patterns, file/line samples and match counts are recorded in support/context_searches.jsonl.

| Short reference | Exact supplied file and convention |
|---|---|
| **Hua** | context/hua_project/137.modern.tex, always credited to **Hua, modernised reading of cote137**, an AI-produced modern interpretation, not a transcription or a result of this report; read together with hua_project/README.md |
| **PS VI / PS VII** | context/ps_chapters_VI_VII/ps6.tex and ps7.tex; § is the text's numbered section and pp. are the original PS page markers |
| **RESULTS_STATE** | context/notes/RESULTS_STATE.md, the complete505-line supplied status register |
| **README / planning question** | context/README.md; questions and proposed bridges are plans, not established identifications |

Hua's manuscript page n corresponds here to our scan n+1; this does not turn the archive foliation into authorial pagination. Abbreviated mentions of Hua's “La réciproque” mean the subsection **“La réciproque : les ⊗-catégories à puissances divisées”**; “Caractérisation intrinsèque” means the section beginning at line1425. No Lean source was included in the supplied context or executed in this investigation: the reported formalizations are used only with the scope and exclusions stated in Hua's own footnotes.

| Relevant supplied ID | Status actually supplied; use in this report |
|---|---|
| **137-perfect-complexes-universal-sigma-exact** | Hua's candidate finding, with an intake that calls it new to the project, not a reviewed theorem; compared against045 and049–064, especially the qualification on056 |
| **137-polynomial-categories-pd-tensor-categories** | Hua's candidate finding; the reported homogeneous-core formalization does not cover the complete tensor/product/multigrading equivalence |
| **MPL_133 B01, B05, B06** | Titles of first-pass research leads; their full notes and the133 scans were not supplied |
| **MPL_133 §2, §88** | Truncated earlier-return summaries, including a report of quadratic Witt theory on133/006–009; not independently checked against those images |
| **MPL_136_047-094 §2; MPL_136_189-234 §2; MPL_136_235-281 §86** | First-pass leads on functorial cochains, bounded comparisons and literature; the complete reports were not supplied |
| **WG2 §Week #3; WG2 §2.4 #5** | Unchecked programme/questions; the present notes contribute evidence and limits, not a declaration that the plans are completed |
| **WG H6** | Unchecked local-system/schematization hunch, not settled by these pages |

No unrelated settled entry is re-proved or claimed to be resolved by a loose keyword analogy. “Adds”, “restates”, “differs” and “qualifies” below describe a comparison with the supplied material, not an endorsement of every claim in it. Negative findings are restricted to the assigned excerpt and supplied files.
'''
HEADER=HEADER.replace('All42','All 42').replace('their43','their 43').replace('of30','of 30').replace('on063,064,073','on 063, 064, 073').replace('cote133','cote 133').replace('the100','the 100').replace('cote137','cote 137').replace('complete505','complete 505').replace('line1425','line 1425').replace('against045 and049','against 045 and 049').replace('on056','on 056').replace('the133','the 133').replace('on133','on 133')

BIBLIOGRAPHY=r'''## Primary literature consulted

The following sources supply modern comparisons, not readings of the handwriting. Only the specified passages are relied on; the PDFs' mathematical assertions were not formally verified in this project.

- **[B09]** Theo Bühler, *Exact Categories*, arXiv:0811.1480v2 (22April2009), Definition2.1 and Theorem12.4 (plus dual). [Primary preprint](https://arxiv.org/abs/0811.1480v2).
- **[R63]** Norbert Roby, *Lois polynomes et lois formelles en théorie des modules*, Annales scientifiques de l'École Normale Supérieure, série3,80(3) (1963),213–348. [Numdam record](https://numdam.org/articles/10.24033/asens.1124/). Bibliographic verification only: the large PDF did not load through the retrieval tool, so its full proof is not claimed to have been inspected; the attribution of the module comparison to Roby is credited to Hua.
- **[FS97]** Eric M. Friedlander and Andrei Suslin, *Cohomology of finite group schemes over a field* (1997), §2, discussion preceding Definition2.1 and Definition2.1 (consulted PDF pp.12–13). [Author-hosted text](https://dornsife.usc.edu/ericmfriedlander/wp-content/uploads/sites/233/2023/06/10.pdf).
- **[BF04]** Clemens Berger and Benoît Fresse, *Combinatorial operad actions on cochains* (2004); consulted arXiv:math/0109158v2 (21October2002), Theorem2.1.1 and §2.2.8. [Primary preprint](https://arxiv.org/pdf/math/0109158).
- **[M06]** Michael A. Mandell, *Cochains and homotopy type*, Publications Mathématiques de l'IHÉS103 (2006),213–246, Main Theorem and Theorems0.1–0.2. [Full article](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mandell2.pdf).
- **[T20]** Bertrand Toën, *Le problème de la schématisation de Grothendieck revisité*, Épijournal de Géométrie Algébrique4 (2020), Article14, Théorème0.1, Théorème4.1 and §5. [Journal PDF](https://epiga.episciences.org/6822/pdf).
- **[H24]** Geoffroy Horel, *Binomial rings and homotopy theory*, Journal für die reine und angewandte Mathematik813 (2024),283–305; locators here refer to the **undated24-page author PDF consulted17November2026**, Theorems5.4,6.1 and Remarks3.11,8.5. [Author PDF](https://geoffroy.horel.org/binomial.pdf). [arXiv metadata](https://arxiv.org/abs/2211.02349) separately records v2 on23March2025; this report does not identify the current author text or its theorem numbering with the uninspected typeset2024 pagination.
- **[DS89]** Andreas W. M. Dress and Christian Siebeneicher, *The Burnside ring of the infinite cyclic group and its relations to the necklace algebra, lambda-rings, and the universal ring of Witt vectors*, Advances in Mathematics78 (1989),1–41, introduction and Theorem(5–4–2). [Author-hosted text](https://www.math.uni-bielefeld.de/~sieben/lothar/burnside_ring_of_cyclic_group.pdf).
- **[Mi14]** Lance Edward Miller, *On the Structure of Witt-Burnside Rings Attached to Pro-p Groups*, Documenta Mathematica19 (2014),1291–1316, introduction. [Journal text](https://emis.de/ft/9833).
- **[Ba05]** Paul Balmer, *Witt Groups*, Handbook of K-Theory (2005),539–576, Definition1.1.27 for the symmetric-space formulation. [Author text](https://www.math.ucla.edu/~balmer/Pubfile/W-handbook.pdf).
- **[L05]** Wolfgang Lück, *The Burnside Ring and Equivariant Stable Cohomotopy for Infinite Groups* (2005), Definition1.1 and Example1.4; consulted arXiv:math/0504051v2, whose header identifies12July2005 although its typesetting date is later. [Primary preprint](https://arxiv.org/pdf/math/0504051).
- **[BW05]** James Borger and Ben Wieland, *Plethystic algebra*, Advances in Mathematics194 (2005),246–283, §2.14. [Author-hosted journal text](https://maths-people.anu.edu.au/~borger/papers/_all/PlethysticAlgebra.pdf).
- **[Stacks]** *Stacks Project*, Definition23.2.1, tag07GL, especially axiom(5); the standard PD iteration identity used in P16. [Definition](https://stacks.math.columbia.edu/tag/07GL).

## Verification and limits of the deliverable

The transcription has42 separately saved fragments,42 recorded second image audits and794 inventory rows marked yes. Its ordered concatenation and all43 frozen hashes are checked mechanically; separate static checks cover braces, environments and editorial-macro structure, and are not an independent assessment of handwriting accuracy. The final progress log records the unchanged hashes after research.

The required file is a LaTeX fragment with no preamble; an optional wrapper and static-check scripts are in support/. A full TeX compilation and rendered-layout review could not be performed because the required formats, classes and packages were unavailable in this execution environment; no successful compilation is claimed. The doubts file identifies the least secure readings, and no external source or research inference was used to alter the frozen transcription.
'''
# Space the bibliographic prose without disturbing URLs or arithmetic expressions.
for a,b in [('22April2009','22 April 2009'),('Definition2.1','Definition 2.1'),('Theorem12.4','Theorem 12.4'),('série3,80(3)','série 3, 80(3)'),('pp.12–13','pp. 12–13'),('21October2002','21 October 2002'),('Theorem2.1.1','Theorem 2.1.1'),("IHÉS103","IHÉS 103"),('Theorems0.1','Theorems 0.1'),('Algébrique4','Algébrique 4'),('Article14','Article 14'),('Théorème0.1','Théorème 0.1'),('Théorème4.1','Théorème 4.1'),('Mathematik813','Mathematik 813'),('undated24','undated 24'),('consulted17November2026','consulted 17 November 2026'),('Theorems5.4,6.1','Theorems 5.4, 6.1'),('Remarks3.11,8.5','Remarks 3.11, 8.5'),('on23March2025','on 23 March 2025'),('typeset2024','typeset 2024'),('Mathematics78','Mathematics 78'),('Theorem(5','Theorem (5'),('Mathematica19','Mathematica 19'),('Definition1.1','Definition 1.1'),('Example1.4','Example 1.4'),('identifies12July2005','identifies 12 July 2005'),('Mathematics194','Mathematics 194'),('Definition23.2.1','Definition 23.2.1'),('tag07GL','tag 07GL'),('axiom(5)','axiom (5)'),('has42','has 42'),('fragments,42','fragments, 42'),('and794','and 794'),('all43','all 43')]:
    BIBLIOGRAPHY=BIBLIOGRAPHY.replace(a,b)

lines=[HEADER.strip()+'\n']
last=None
for item in items:
    if item['section']!=last:
        lines.append('\n## '+item['section']+'\n')
        if item['id']=='U01':lines.append('These are the manuscript’s own visible flags or explicit abbreviations of proof, with their later status; editorial uncertainty alone is excluded.\n')
        last=item['section']
    lines.append('\n### '+item['id']+' — '+item['title']+'\n')
    lines.append('**Cote/scan:** 137/'+item['scan']+'; '+item['location']+'. **Kind:** '+item['kind']+'.\n')
    lines.append('**Bears on:** '+item['ids']+'\n')
    if item.get('confidence'):lines.append('**Confidence and reason:** '+item['confidence']+'\n')
    if item.get('status'):lines.append('**Status within the text:** '+item['status']+'.\n')
    if item.get('quote'):
        quote=item['quote'].replace('\n',' ')
        longest=max([len(v) for v in re.findall('`+',quote)] or [0])
        tick='`'*(longest+1)
        lines.append('**Words on the page:** '+tick+' '+quote+' '+tick+'\n')
    lines.append('\n'+item['body']+' '+item['context']+'\n')
lines.append('\n'+BIBLIOGRAPHY.strip()+'\n')
text='\n'.join(lines)
(ROOT/'MPL_137_045-086_notes.md').write_text(text)
counts=Counter(x['section'] for x in items)
summary=dict(items=len(items),section_counts=dict(counts),words=len(text.split()),searches=len(searches),zero_match_items=[x['id'] for x in searches if x['result']=='no matches'],frozen_hashes_unchanged=len(MANIFEST))
(ROOT/'support/notes_build_report.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
hashes_ok()
print(json.dumps(summary,ensure_ascii=False,indent=2))
