# Isolated exact-preamble TeX validation

## Official package provenance

The official `ulem.sty` source was retrieved on 2026-11-17 through CTAN's normal
mirror service, using HTTPS certificate verification and its ordinary redirect.

- Package page: https://ctan.org/pkg/ulem
- Directory: https://ctan.org/tex-archive/macros/latex/contrib/ulem
- Requested source: https://mirrors.ctan.org/macros/latex/contrib/ulem/ulem.sty
- Final CTAN mirror source: https://mirror.math.princeton.edu/pub/CTAN/macros/latex/contrib/ulem/ulem.sty
- Retrieval: 2026-11-17 15:04:54–15:05:06 UTC; HTTP 200.
- Bytes: 15,682.
- SHA-256: `c97c15736b46cf13071c52070c07aa933fc8253748422d0df56e97286b563685`.
- Source version: `\ProvidesPackage{ulem}[2019/11/18]`.

The original source and its copyright/license notice are retained unchanged.
The license permits redistribution with that notice intact. The returned HTTP
metadata is in `ulem_retrieval.json`; `setup.log` records retrieval and the
subsequent exact environment overrides, commands, working directories, hashes,
and observed process results.

The retrieval operation used the standard library call:

```python
with urllib.request.urlopen(
    'https://mirrors.ctan.org/macros/latex/contrib/ulem/ulem.sty',
    timeout=45,
) as response:
    data = response.read()
```

The retrieved byte array was written directly to `ulem.sty`; no source edits,
HTTP proxies, authentication workarounds, or system installation were used.

## Reproduce the validation

Run from the project workspace:

```bash
python out/scripts/tex_support/run_synthetic.py
```

This command accepts no manuscript input. It uses three invented probes for:

1. Diplomatic macros, inline/display mathematics, and underlining.
2. Nested deletions in text and mathematics, including insertion inside deletion.
3. TikZ-CD diagrams and TikZ drawings with diplomatic macros in labels.

It copies the supplied `out/PREAMBLE.tex` and official `ulem.sty` byte-for-byte
into a fresh temporary directory, builds a local `pdflatex.fmt` from the already
installed TeX sources, and compiles each probe to DVI. Shell escape and automatic
format/font generation are disabled. All generated configurations, caches, and
output files are confined to the temporary directory. No system file changes.

The explicit recursive `TEXMF` search avoids the runtime's broken `ls-R`
database links. DVI compilation supplies the tested syntax-validation route
without requiring the runtime's missing PDF font maps. This run does not
establish PDF production or the validity of manuscript content.

## Observed result

The run completed successfully in `/tmp/sp04_exact_tex_d8q_ktyn`.
All three probes returned exit code 0 and created DVI output. The supplied
preamble's source and staged hashes agreed. `synthetic_result.json` records the
results; `synthetic_evidence/` retains the generated probe sources and logs.
No manuscript pages, witnesses, images, or context contents were read or
compiled. Actual manuscript compilation remains unperformed.

The temporary format can be regenerated at any time using the exact command
and environment in `setup.log`, or by rerunning the synthetic helper. The
format is deliberately left in the temporary directory rather than included
as a required binary dependency.

## Later mechanical corpus check

The general checker now accepts the validated isolated DVI setup directly:

```bash
python out/scripts/tex_check.py --isolated-dvi --preflight
python out/scripts/tex_check.py --isolated-dvi --probes
```

The first command checks readiness without opening manuscript content. The
second command is reserved for the root's later corpus-validation stage: it
mechanically compiles the default combined transcription, using a byte copy
and the unchanged preamble in a fresh temporary directory. It also runs the
three synthetic probes separately. It never edits transcription files.

The default source is `out/SP04_CW_156-4+156-6_transcription.tex`; `--source`
accepts an explicit replacement path when needed. The returned report lists
exit codes, DVI creation, and log locations without printing manuscript
excerpts. Success requires every requested job to finish with exit code 0 and
create its DVI output. A lost temporary format is reported at preflight;
rerun the synthetic setup to regenerate it. This corpus command was prepared
but has not yet been run.
