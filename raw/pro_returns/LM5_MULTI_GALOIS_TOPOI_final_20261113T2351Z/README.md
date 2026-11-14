# LM5: Multi-Galois topoi

**INCOMPLETE.** The integrated report begins with the exhaustive prompt-coverage table and records the exact unresolved items. The paper is **AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode)**. No priority is claimed.

## Reading order

1. `LM5_MULTI_GALOIS_TOPOI_report.md`: coverage, principal findings, source checks, remaining obligations, and verification.
2. `LM5_MULTI_GALOIS_TOPOI_paper.pdf`: the complete integrated mathematical text in Parts A–F.
3. `LM5_MULTI_GALOIS_TOPOI_results.csv`: one row per numbered statement, with status, dependencies, proof location, and manuscript coordinates.
4. `LM5_MULTI_GALOIS_TOPOI_readings.csv`: mathematical evidence about the provisional manuscript readings.

The main TeX file loads the complete sources in `sections/`. The bibliography and APA-style BibTeX support are included. `source_parts/` retains component drafts and independent audits; it is subordinate to the integrated paper. `source_audit/` contains the recovered comparison texts and integrity record. `verification/` contains build logs, numerical package audits and the visual-inspection record. `code/` contains the executed programs and their outputs.

In the final return, `history/` contains the six immutable checkpoint ZIPs. These preserve every earlier file and passage; the report identifies superseded claims and scope corrections. The current integrated files are authoritative for this return.

## Rebuilding the PDF

With a normal TeX Live installation providing LuaLaTeX, BibTeX and the packages declared in the preamble, run from the extracted archive:

```sh
python code/build/rebuild_paper.py
```

The script performs the LaTeX/BibTeX/LaTeX/LaTeX sequence, saves its logs, and checks the requested 2 pt overflow limit, undefined references and missing glyphs. It needs no network access. Its optional runtime arguments were used only to locate the authoring environment's existing TeX format and font trees; the exact executed commands and output are retained.

Mathematical check programs can be read independently of the assembly scripts. Historical register-generation and integration scripts retain their authoring-workspace paths so that their executed output has an exact provenance; the portable rebuild script uses only files in this archive. The source-integrity check `code/root/source_recovery_checks.py` is also relative to the extracted archive.

`MANIFEST_SHA256.json` lists the size and SHA-256 hash of every other packaged file. The archive was read back and all those hashes were checked after creation.
