# E.62: exact GL2(F3)/SL2(F3) common-source replay

## Scope and mathematical result

The statement is `sections/E_gl23_ferrari_agent.tex`.  It treats all literal
GL2(F3) epimorphism kernels, the exact universal Ferrari target, its actual
induced B source, and the common source and target with E.59.  It retains
the entire original G6 point and every actual F' correction.

For each of the 24 retained multiplier-one G6 points:

| Fibre | All corrections | Gentle values | Full pentagon/braid values |
| --- | ---: | ---: | ---: |
| GL2(F3) alone | 2^21 | 16 | 4 |
| Actual common GL2/SL2 source | 2^24 | 32 | 4 |

All source and final target maps generate their specified full groups.
The four common final values project two-to-one onto only two of the four
GL-only final values, and two-to-one onto both E.59 final values.  Every
CM matrix pair survives.  This statement does not prove a compatible full
profinite pentagon lift.

## Frozen files

`research/E62_authoritative_manifest.json` is the authoritative hash list.
It protects the complete proof, all new programs, outputs, prior failed
attempts, typesetting records, and all old comparison inputs.  E.59 files
are read only.  The manifest script refuses to replace an existing manifest.

Check the complete protected list without rerunning mathematics:

```bash
python code/a_cm_gl23_replay.py --check-only
```

Run the entire batch in a destination that does not yet exist:

```bash
python code/a_cm_gl23_replay.py --destination research/root_E62_replay
```

The driver copies the exact listed inputs, recompiles the retained C++
Schreier engine, and executes the following sequence:

1. Literal matrix group, complete Aut/epikernel enumeration, universal target,
   full original N-word source fingerprint, and faithful induced action.
2. Complete original and smaller source/derived chains, then the actual
   common block source and target with E.59 and their chains.
3. Exact class-two coordinate bases, every prefix subgroup certificate,
   the complete gentle equations, and all remaining full pentagon/braid/twist
   evaluations in the single and common targets.
4. Every generation certificate, every actual F' word map, and the full
   projection multiplicities.
5. Full C++ replay of every saved certificate, including all 960 generation
   certificates and all 40 coordinate certificates.  Each generating word
   was independently evaluated by the NumPy reader during construction.
6. Exact comparison of all mathematical JSON fields, every NPZ array, and
   the complete subgroup-chain data.  Only elapsed-time fields are omitted.
7. A second hash check proving every authoritative original is unchanged.

The driver saves its command log and final result in the fresh destination.
The expected total is approximately eight to twelve minutes, depending on
CPU contention.  The original most expensive steps were the source
fingerprint (92.675 seconds), common generation (221.490 seconds), and
GL-only target generation (27.119 seconds).  No network or external algebra
system is required.  Python needs NumPy and SymPy; the exact C++ engine
requires a C++17 compiler.

## Actual maps and preserved failures

The C++ chain and all coordinate/preimage data are evaluated on the original
based words.  The smaller N lists are selected indices of the original
97-element N_B basis, with their complete equality checks.  The common
target uses the same word in both components; it is not assembled from
independent solutions.  The complete subgroup-order argument in E.62 proves
the two nonfactorization assertions only for the specified quotient maps.

The first projection comparison requested an incorrect old stdout filename.
Its program, empty stdout, and FileNotFoundError are retained under
`a_cm_gl23_projections_failed_old_output_path.*`.  The repair changes only
that read-only filename.  The first reviewed TeX fragment and initial
overflow build are retained in the research directory.  See
`research/A_GL23_Ferrari.md` for the full ledger.
