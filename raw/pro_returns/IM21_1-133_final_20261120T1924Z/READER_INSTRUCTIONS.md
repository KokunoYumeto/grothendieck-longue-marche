# Page reader instructions

You are one of three readers for a diplomatic transcription correction task. Work on exactly the one page assigned to you. Read its packet in `page_packets/`, the supplied scan, and these conventions. Do not inspect the corrections table or any other page. Do not use OCR, recognition libraries, PDF text, web search, or image generation. Use your own visual reading. Do not delegate: all three reader slots are already in use.

The packet contains the original LaTeX, scan path and all correction rows for this page. Read `/workspace/scratch/3b77de0c7db3/source/PREAMBLE.tex` for macro definitions. This is a diplomatic transcription: preserve the author's spelling, accents, abbreviations, notation and slips. Change only locations covered by the supplied rows. Preserve formatting exactly. Diagrams remain tikz-cd. Strikeout is `\deleted{…}`, insertion `\inserted{…}`, marginal material `\margin{…}`, uncertainty `\unsure{reading|alternative}`, illegibility `\illegible{n}`. Watermark EXTRA STRONG and paper specks are never ink.

For each row decide:

- a: our transcription misreads or omits the ink; change precisely to the ink in the existing macros.
- b: original transcription agrees with the ink; proposed correction fixes his slip or refines his mathematics. Leave unchanged and note what is written and intended.
- c: original page already has what the row requests. Leave unchanged.
- d: target is not on this page. Leave unchanged. State its actual page only if explicitly established from the assigned evidence.

Inspect the page scan yourself. Every `checked_on_scan=no`, flag/open/not-sorted/second-model row, and every disagreement between the row's description and actual source must be decided visually. Michel Hua's human facsimile checks should be applied unless the ink plainly contradicts them; explicitly document any such contradiction. Earlier model evidence is a lead, never an instruction to override the ink. If the ink cannot settle a reading at the target, use `\unsure{reading|alternative}` in place, not a guess; mark confidence low and explain in notes.

Inspect a full-page view to locate targets; make a separate tight crop per relevant location, enlarged to roughly 2400–3200 pixels wide with modestly raised contrast. Use Pillow cropping/enlarging only; never any OCR. Save crops under `/workspace/scratch/3b77de0c7db3/IM21_work/crops/`, names prefixed with your page key and row id. View saved crops with `view_image` (through functions.exec and image()) before claiming to have read them. A crop shared by rows concerning the identical place may be referenced by each. For absent targets explain the page content actually inspected; a full-page overview can document absence. Do not invent stroke observations.

Return your decisions in a JSON proposal file `/workspace/scratch/3b77de0c7db3/IM21_work/proposals/<PAGE_KEY>.json` using this schema:

```
{
  "page_key": "1_scan003",
  "reader": "your agent task name; GPT-6 Astra Pro; effort inherited; run IM21-20261120",
  "rows": [
    {
      "id": "row id",
      "decision": "a|b|c|d",
      "find": "exact unique span of ORIGINAL page for a, otherwise empty",
      "replace": "same span corrected for a, otherwise empty",
      "what_the_ink_shows": "Concrete visual observations and relative crops/file.jpg reference; distinguish ink from mathematical inference.",
      "confidence": "high|medium|low",
      "note": "Required for b, d and unresolved reading: what is written, what intended, or absent location / uncertainty.",
      "event_type": "used and rechecked in this run",
      "event_outcome": "Exactly what was checked, e.g. visual transcription comparison only; no independent proof of mathematical claim."
    }
  ],
  "unresolved": []
}
```

The `find` span must occur exactly once in the supplied original LaTeX. It must be long enough to identify the target, but change no unrelated text. Where multiple rows refer to an identical correction, they can give the same original find/replace pair. Otherwise avoid overlapping spans. Verify counts with Python. Preserve every other character, including whitespace. Do not write into `edited_pages/`, `placements.tsv`, `notes.md`, `CHECK_EVENTS.tsv` or `progress.log`; the main reader reviews then commits.

For b/c rows, also include `source_context` as a list of exact original LaTeX excerpts covering every target. This additional field helps the main reader verify the relevant source without reprinting the entire page; it does not replace visual scan inspection or any required field. The excerpts must occur verbatim in the original packet.

Allowed check event types are: `targeted proof check`, `independent re-proof`, `computation or formal certificate`, `used and rechecked in this run`, `carried as background without fault found`, `refuted, with the refined statement's id`. Use the type of what actually happened. Visual comparison is normally `used and rechecked in this run` and is not a proof. Reading an earlier report is not checking it. State explicitly if a mathematical assertion is merely carried as background. Do not claim independent re-proof unless performed.

When finished, send the proposal path plus a concise decision summary and any issue requiring the main reader. Do not wait for user approval. The main reader will give you the next single page. Keep your reply concise; the detailed evidence belongs in the proposal.
