# E.124 author bundle

The theorem is in sections/E_fiftythree_ordinary_valuation.tex, with a seven-page standalone PDF in qa/e124_standalone.pdf. Results, coverage, exact source scopes, actual visual review and the final manifest are under ledger/.

Complete source-only reconstruction:

~~~text
python code/e53_ordinary_replay.py --gp /absolute/path/to/gp --label independent_replay
~~~

The command needs Python with SymPy and PARI/GP 2.19.0. It copies nine mathematical sources and four immutable inputs, regenerates all derived inputs, checks whole text and JSON outputs and compares both complete decoded PARI objects. It does not run an upper BNF.

| Stage | Exact scope |
|---|---|
| e53_ordinary_kernel.gp | Ordinary subgroup of the retained 37-unit system, without an upper-basis inference |
| e53_ordinary_summary.py | Exact subgroup and character summary |
| e53_positional_residues.py | Literal positional units and positive tame characters |
| e53_ordinary_saturation.py | Full nine-prime ordinary-unit saturation and inverse |
| e53_ordinary_frobenius_input.py | Literal ideal input generation |
| e53_ordinary_frobenius.gp | Maximal-order factors and Frobenius characters |
| e53_ordinary_genus_chars.py | Power-relation and prime-correction characters |
| e53_ordinary_genus.gp | Full idelic and Smith maps |
| e53_ordinary_maps.py | Independent enumeration, both map inverses, trace and kernels |

Every source has its actual output and error file. Failed attempts are retained under history/, and the complete fresh reconstruction under audit/author_replay/. Binary files are data certificates compared through actual PARI decoding.

The precise next arithmetic task is the numerical bounded exponent h, beginning with the actual ordinary-unit character at level three. The present theorem retains its defined actual supremum.
