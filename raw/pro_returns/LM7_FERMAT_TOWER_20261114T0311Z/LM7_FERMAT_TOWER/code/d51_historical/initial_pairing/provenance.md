# Initial pairing diagnostic provenance

The original d_class2_diagnostic.py executed the byte-identical copied D.50 helper with runpy, captured its actual stdout, and retained both that output and the helper's generated JSON in the same directory. It then computed the pairing using NumPy. The files here are the actual retained source/output/certificates from that execution.

The final code/d_class2_diagnostic.py is a separate input-only standard-library implementation. It rebuilds the graph, reads the exact frozen D.50 JSON, and never executes or modifies that input. Its whole pairing and defect matrices agree with the original computation.

Original command from the workspace root: python D51_EXPERIMENTS/code/d_class2_diagnostic.py > D51_EXPERIMENTS/code/d_class2_diagnostic.out
