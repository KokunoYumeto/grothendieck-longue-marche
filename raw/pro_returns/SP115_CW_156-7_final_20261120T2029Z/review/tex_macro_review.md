# Static TeX macro compatibility review

## Current final result

**No concrete macro or syntax defect was identified in the final eight page fragments at 2026-11-20 20:27:25 UTC.** The final hashes below agree with the subsequent transcription freeze at 20:27:43 UTC. This is a static review only; no compilation or source-image reading was performed.

The earlier scan009 `\inM` defect and the later transient `\LongrightarrowZ` concatenation have both been repaired to distinct control words and following symbols. All 1,457 current control-word occurrences belong to the supplied preamble or its standard LaTeX/AMS/mathrsfs/ulem/TikZ/tikz-cd interfaces. All 317 calls to the supplied one-argument transcription macros have balanced braced arguments. The changed scan006,008,009 contexts were reread, including nested state/doubt macros, display/aligned structures, and TikZ graphics. No external math superscript collision with `\unsure` was found; the two quotation ticks after text-mode `\unsure{s}` on008 are ordinary source punctuation.

`edition_tools.py verify` reports eight page fragments, ordered scan markers002–009, one `\cotefile`, zero brace/environment/math-delimiter errors, and exact equality between the combined transcription and the prescribed concatenation of the fragments.

| Scan | Final reviewed page SHA-256 |
|---|---|
| 002 | `117aa6458bc330e149d20a53e4131f0364b6051933abe476cd81fede41bd83ba` |
| 003 | `53b94d6ebf40be70862d37ccd09206f14f5daa04fa5a0cae248626e3519f9aa7` |
| 004 | `90181e8a84b859c602ae371d278908fb7d354ee0d8da3b63a9d38743793f6ef0` |
| 005 | `beb00da309ce969a517be848163af8ec55f579e90f5d55d2bf6b46c64b49c797` |
| 006 | `268817bc4186f5e48297353aed32aaf4916c47b7c44c2a21da8a2447cf310430` |
| 007 | `ceb5de05a8b5b933f25de8e3473958b742d001201e9dd85d54f1a1ff589ebfae` |
| 008 | `55a3872da2206b770473290ec83cf0079c4ce7e3b4fcb9e792b47d3509b4b17d` |
| 009 | `1446d1135a0ecf30e7eb39ece913bb2d29a0ebc20a42abe6733875709437e77a` |

Combined transcription SHA-256: `ebc1c33a1b92d82243e4c88b782bc66aa4eba221da4b9664db935e881db1b815`.

Supplied preamble SHA-256: `aa8f0b2c36d63a886bae7e8fc7b68697fdb378a0d7d391ab09480f11d785a1bf`.

This review cannot certify runtime package expansion, page layout, or visual placement. Those were not tested by invoking a TeX engine. No page was edited by this reviewer.

## Initial review history — superseded by the current result above

Full page text read: **2026-11-20 20:02:02 UTC**. Command/argument recheck: **2026-11-20 20:03:09 UTC**. Metadata report written: **2026-11-20 20:03:45 UTC**.

Scope: all eight current `out/pages/*.tex` files, against `packets/PREAMBLE.tex` and the interfaces of its loaded LaTeX, AMS, mathrsfs, ulem, TikZ and tikz-cd facilities. No compilation, source-image consultation, ink decision or page edit was performed.

## Concrete defect

1. **scan009, physical TeX line 4:** the fragment `$X,Y\inM$` contains the undefined control word `\inM`. TeX consumes all alphabetic characters in that control word; neither the supplied preamble nor the loaded standard interfaces define it. Preserve the same symbols by introducing a token boundary: `$X,Y\in M$` (or `$X,Y\in{}M$`). This occurrence was still present at the 20:03:09 UTC recheck and was reported immediately to root. The page was not edited.

No other concrete unknown/concatenated control sequence or malformed required-macro argument was identified in these snapshots. Required arguments, the supplied state/doubt macro interfaces, and the inline/display, array/aligned, TikZ and tikz-cd contexts were inspected statically. No `\unsure{...}` occurrence was immediately followed by an external superscript/prime that would clash with its automatic question-mark superscript.

## Snapshot hashes

| Scan | SHA-256 of reviewed page |
|---|---|
| 002 | `117aa6458bc330e149d20a53e4131f0364b6051933abe476cd81fede41bd83ba` |
| 003 | `53b94d6ebf40be70862d37ccd09206f14f5daa04fa5a0cae248626e3519f9aa7` |
| 004 | `90181e8a84b859c602ae371d278908fb7d354ee0d8da3b63a9d38743793f6ef0` |
| 005 | `beb00da309ce969a517be848163af8ec55f579e90f5d55d2bf6b46c64b49c797` |
| 006 | `ac10295a550ab3de910fbd7b5a74d35d65e2c2b08b5810aba188e1c453bc3238` |
| 007 | `ceb5de05a8b5b933f25de8e3473958b742d001201e9dd85d54f1a1ff589ebfae` |
| 008 | `4c4020de2ecc04c946c762002fecd5957f93c95434d3c9c33111010fe613fe2b` |
| 009 | `f2b59d9af15c50fb79bfb44bf8f799f73dd82f62f1d283d2abdd2492c5007b8f` |

Supplied preamble SHA-256: `aa8f0b2c36d63a886bae7e8fc7b68697fdb378a0d7d391ab09480f11d785a1bf`.

## Final recheck

All eight page hashes still matched the reviewed snapshots when this report was written.

The initial review requested a later check of the scan009 token-boundary repair and every page changed during root adjudication, particularly006,008,009. That request was completed in the final review reported above. This report does not certify runtime package expansion or layout; no TeX engine was invoked.

## Final closure

At **2026-11-20 20:28:59 UTC**, all eight page hashes and the combined-transcription hash still matched the **20:27:43 UTC** freeze and the final hashes listed at the top of this report. Scan009 is `1446d1135a0ecf30e7eb39ece913bb2d29a0ebc20a42abe6733875709437e77a`; the combined transcription is `ebc1c33a1b92d82243e4c88b782bc66aa4eba221da4b9664db935e881db1b815`. Both concatenated-control-word repairs are present. The final macro/structure review is complete, with no concrete syntax blocker identified and no compilation performed.
