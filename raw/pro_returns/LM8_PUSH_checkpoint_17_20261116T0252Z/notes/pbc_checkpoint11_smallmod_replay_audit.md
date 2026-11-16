# Checkpoint11 small-modulus replay and prefix audit — PASS

The exact replay regenerated **3,367,409,098 decoded bytes**,
**75,422,138 records**, and compared every byte with the
immutable paused native-v6 capture. SHA256:
`6c617ac9bfccae7694f520218f9fb5c94d0df00cc23a7abb3ac99da5eafa0583`. The original valid gzip wrapper had
1,131,552,701 bytes and SHA256 `982d8f097bdaa673669a54abaac004e36f8181481450291fe3b3702c69693460`.

The retained original source/leaf records occupy 305,540,502
decoded bytes. Their exact reversible codec occupies **28,897,004
bytes**, SHA256 `7502d8796b075d439203e87edc4cae3734547f04b66ba7f4125c67cfe4560021`. Its complete round trip passed.
The native-v6 reducer was copied unchanged. Phase-end target checks match
the original power, exterior and triple phases; the full comparison spans
both phase transitions. No probabilistic hash-only comparison replaced
the direct byte comparison.

The entire older GMP log is an exact decoded prefix: 501,122,419 bytes and
11,735,720 records, SHA256 `a23633273ff60f215762eb4d254bdf2af5a0fec48dbf15da38377282fa54194d`. This was rechecked
against the immutable v2 capture, independently of the earlier live-prefix
comparison. The actual portable prefix restoration helper was then run,
and every decoded output byte was compared with the original old log.

## Self-contained restoration

The two generic ledgers are `pbc_smallmod_v2_replay_transform.json` and
`pbc_smallmod_v1_prefix_transform.json` in `checkpoint11_smallmod_replay/`;
copies are retained under `code/`. They contain the original and decoded
counts/hashes, explicit complete-verification flags, stored-recipe hashes,
and argument-array restore commands. The v2 recipe uses only included
relative paths. The decoder first restores all original source leaves,
derives and verifies the identity-row DAT, and uses the matching included
binary or recompiles the included C++ source and header. It verifies the
complete regenerated stream before returning. The prefix helper uses that
restored v2 source in the selected output destination.

Compiler: `g++ (Debian 14.2.0-19) 14.2.0`. The exact compile command and every restore
dependency hash are retained in the accompanying JSON. Standard runtime
requirements are Python3, a C++17 compiler, GMP and zlib. The original
absolute scratch/capture paths are provenance and are never required by
the archive's restoration commands.

Original compression wrappers are explicitly superseded, not represented
as byte-identical gzip files. **Every mathematical/proof record byte is
retained or exactly reconstructable.** Both old bases and the new live
basis remain paused intact. The checkpoint compression proves no lifting
statement: **C31 remains Open** until a positive DAG certificate and all
used ORIGINAL source relations pass their separate mathematical replay.
