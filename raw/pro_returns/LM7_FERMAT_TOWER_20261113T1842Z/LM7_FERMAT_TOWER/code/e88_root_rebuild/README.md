# Independent E88 reconstruction

Run `python code/e_global_sdivisors.py --gp /absolute/path/to/gp` from this directory. Python requires SymPy. The driver rebuilds its degree-six arithmetic from the retained source and reconstructs every output. The author binary in `inputs/author_binary` is used only by `code/e_global_sdivisors_binary_compare.gp` for the independent complete-object equality check; it is not a rebuild input.
