from pathlib import Path
import json,re,datetime
r=Path(__file__).resolve().parents[1];rec=r/'records'
p=rec/'assemble_notes.py';s=p.read_text()
s=s.replace("text='\\n'.join(out)","text='\\n'.join(out)\n# APA URL text remains visible while Markdown provides explicit links.\ndef link_url(m):\n value=m.group(0); core=value.rstrip('.,;'); return '['+core+']('+core+')'+value[len(core):]\ntext=re.sub(r'https?://[^\\s]+',link_url,text)")
s=s.replace('The 333 current unsure markers','The kind unproved claim identifies an assertion or brief sketch in the manuscript, even when this run subsequently verifies it. The 333 current unsure markers')
p.write_text(s)
# Keep research-process documentation while directing duplicated draft literature prose to its reviewed final form.
p=rec/'connections_context_report.md';s=p.read_text()
for item,final in [('CC03','C64-Q07'),('CC04','C64-Q08'),('CC05','C64-Q09')]:
 pattern=rf'(### {item}[^\n]*\n)(.*?)(?=\n### |\n## )'
 def repl(m):
  return m.group(1)+'\nThe reviewed literature comparison/proposal is presented in '+final+' of MPL_64_002-039_notes.md. Its original source-scope check is retained in connections_check_events.jsonl and the search log; no independent proof of the published theorems was performed.\n'
 s=re.sub(pattern,repl,s,flags=re.S)
start=s.index('## Primary literature checked, in APA form')
end=s.index('## Verification classification',start)
s=s[:start]+'''## Primary literature checked

Full APA entries and inspected-version links are in the final notes. The source locations checked were Katz(1970), introduction and §§5,7,10; Ogus–Vologodsky(2007), Remark2.2; Bouw–Wewers(2006), author preprint §§2–3,5; and Hoshi(2015), author revised preprint introduction and §5. Published metadata was checked separately; no novelty or historical-dependence claim is made.

'''+s[end:]
s=s.replace('This is an intermediate research record','This is a research-process record').replace('not an alteration of the diplomatic transcription.','not an alteration of the diplomatic transcription. The duplicated literature recommendations below now point to their reviewed final notes; source and check provenance are retained.')
p.write_text(s)

sources=[
 {'author':'Katz, N. M.','year':1970,'title':'Nilpotent connections and the monodromy theorem: Applications of a result of Turrittin','doi':'10.1007/BF02684688','url':'https://web.math.princeton.edu/~nmk/old/nilpconn.pdf','locations':['Introduction','Theorem5.1','Theorem7.4','Corollary7.5','Theorem10.0'],'treatment':'Published background; base-change/Frobenius-flatness and arithmetic/local-freeness assumptions inspected; no independent proof'},
 {'author':'Ogus, A., and Vologodsky, V.','year':2007,'title':'Nonabelian Hodge theory in characteristic p','doi':'10.1007/s10240-007-0010-z','url':'https://www.numdam.org/item/10.1007/s10240-007-0010-z.pdf','locations':['Remark2.2'],'treatment':'Published background; zero-p-curvature scope inspected'},
 {'author':'Bouw, I. I., and Wewers, S.','year':2006,'title':'Indigenous bundles with nilpotent p-curvature','doi':'10.1155/IMRN/2006/89254','url':'https://arxiv.org/pdf/math/0505275','metadata_url':'https://academic.oup.com/imrn/article-abstract/doi/10.1155/IMRN/2006/89254/684757','locations':['Definition2.1','Section3.1','Section5'],'inspected_version':'Author preprint v2,2005-08-18; publication metadata checked separately','treatment':'Published background; marked-curve hypotheses and definitions inspected'},
 {'author':'Hoshi, Y.','year':2015,'title':'Nilpotent admissible indigenous bundles via Cartier operators in characteristic three','doi':'10.2996/kmj/1446210603','url':'https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1811revised.pdf','metadata_url':'https://www.jstage.jst.go.jp/article/kodaimath/38/3/38_690/_article/-char/en','locations':['Introduction','Section5'],'treatment':'Published background; genus/characteristic hypotheses inspected'},
 {'author':'Ledet, A.','year':2001,'title':'Embedding problems and equivalence of quadratic forms','doi':'10.7146/math.scand.a-14327','url':'https://journals.msp.org/mscand/article/download/878/877/909','locations':['Section0.4,pp283-284'],'treatment':'Classical comparison only; exact finite cocycle independently calculated in this run; field comparison requires characteristic not2'}]
(rec/'literature_sources.json').write_text(json.dumps({'accessed_utc_date':'2026-11-17','sources':sources,'full_APA_reference_location':'MPL_64_002-039_notes.md,References'},ensure_ascii=False,indent=2)+'\n')
(rec/'RESEARCH_REVIEW.md').write_text('''# Research review and final assembly record

The primary reader finished and froze the transcription before opening context. Research delegation was restricted to frozen text, contextual sources and mathematical verification; no research agent read manuscript images.

## Targeted reviews completed

- Local notes N01–N20: verified the groupoid scope, exact subgroup/orbit counts, two cover orientation characters and literal-presentation countermodel; corrected the S4/V faithfulness wording and the scan013 quotation; distinguished actual-subgroup inclusion data from transporter-coset morphisms.
- Module notes N21–N38: reviewed natural quotient actions and the finite certificate; corrected a Hua attribution, kept derived-group brackets distinct from the manuscript’s projective primes, and made the fixed-torsor/cohomology and section-order conventions explicit.
- Question notes Q05–Q10: inspected the final source scope and published hypotheses; corrected the Katz spectral-sequence page/base qualifications, the cote159 catalogue locator and attribution to Hua’s interpretation.
- Apparatus U01–U12/T01–T03: matched all authorial requests and their local dispositions, adding the explicit012 warning and007/009/020 programme markers; matched all18 visible Arabic page marks and the uncertain cover title; did not assign authorship to the pencil40 annotation.

## Final evidence hierarchy

The final notes and current page files are authoritative for this package. Research reports preserve proof details and provenance; draft-construction scripts are historical workflow records and may precede the targeted corrections. The final note data are root_note_items.json, question_note_items.json and apparatus_note_items.json; assemble_notes.py renders them, search_each_note.py records their context queries, and assemble_check_events.py maps report events to final IDs.

The executable finite checks are mathematical computations, not OCR or theorem-prover formalizations. The literal-presentation infinite-cyclic countermodel is a written proof; its explanatory JSON string is not mislabelled as a formal execution. Source-place event rows point to the same actual checks as note-ID rows, so row count is not a count of independent verifications.

The inclusion SVG was checked against all30 actual subgroups and66 cover edges and visually inspected. Its lower ranks have dense crossings; the generator key and exact CSV remain the unambiguous data.
''')
(r/'README.md').write_text('''# MPL_64_002–039

Complete diplomatic transcription of cote64 PDF scans002–039, with research notes and an audit trail.

## Main deliverables

- MPL_64_002-039_transcription.tex: all38 pages, one LaTeX fragment without a preamble.
- pages/: one fragment per scan, in the same frozen reading.
- MPL_64_002-039_doubts.md: notation table,333 current unsure occurrences,four illegible spans,abbreviations and legibility assessment.
- MPL_64_002-039_inventory.csv:761 inventoried elements,all marked transcribed=yes.
- MPL_64_002-039_notes.md:63 research/apparatus items,with contextual comparisons,exact finite checks,self-flagged steps,title/pagination evidence and references.
- CHECK_EVENTS.tsv: event-level statement provenance and verification scope.
- progress.log: page completions,audits,freeze hashes and final integrity assertion.

## Evidence and supplementary research

records/ contains the visual-workflow records,freeze manifest,read-only validator,LaTeX syntax harness,research search logs,proof reports,finite computation scripts/results,and a checked30-node S4 subgroup-inclusion SVG with its generator key and CSV data. The supplied scans and contextual source archive are not redistributed.

The 38 page files and combined transcription were frozen before context access. Mathematical corrections and different contextual readings appear only in the notes. A successful syntax check is not a claim that every handwriting doubt has disappeared.

## Reproducible read-only structural check

From this directory:

    python3 records/validate_package.py --require-frozen --json

The finite mathematics can separately be reproduced with the three certificate scripts identified in the notes. They do not inspect images. Historical transcription-editing scripts are retained as process documentation; the delivered frozen files and hash manifest define the final transcription.
''')
print('Research provenance,references and package guide completed')
