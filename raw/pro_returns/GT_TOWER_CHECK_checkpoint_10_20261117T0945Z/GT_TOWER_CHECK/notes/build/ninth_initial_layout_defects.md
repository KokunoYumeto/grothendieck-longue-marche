# First ninth-hour build: exact defects and repairs

The three-pass LuaLaTeX build completed. Its retained log reported one
overfull display,5.168pt, at SVM.2 in the common-source proof. The display
has been split into two rows in the authoritative source.

The same build reported the undefined key Fresse2017. The bibliography
merge had omitted that previously checked entry because it existed only
in the merged file. Its exact checkpoint08 bytes were restored to the
authoritative root bibliography, and the opened primary location remains
unchanged. The checked statement itself was not changed.

The run-together bibliographical metadata observed in checkpoint08 was
repaired by adding the missing spaces. Every preedit source is preserved.
A fresh complete build and full-page inspection are still required.
