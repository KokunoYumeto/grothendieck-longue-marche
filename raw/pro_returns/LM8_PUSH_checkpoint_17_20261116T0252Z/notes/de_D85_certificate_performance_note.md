# D85 certificate expansion correction

The first execution was interrupted while symbolic expansion used the already expanded polynomial `(1+g_h)^nu`. This caused combinatorial expression growth. The exact identity `1+g_h=(1+y)^(5^h)` now forms the same power directly before expansion. The prior source is preserved as `de_sha_global_independence_certificate_before_expansion_optimization.py`; no mathematical assertion or tested relation changed. The interrupted execution produced no JSON.
