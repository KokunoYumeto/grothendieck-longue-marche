# Preserved editing diagnostic

An initial apply_patch request to add the selected original-cover
corollary failed before mutation because its expected context omitted
the word `embedding` before `and the proved regional retraction`.
The actual tool diagnostic was:

    apply_patch verification failed: Failed to find expected lines in
    sections/b_slit_bad_centralizer.tex:
    and the proved regional retraction. This result retains
    all critical fillings in this model; it does not add the annular
    $q=0$ operator or the other necks.

The full tail was read, the context was corrected, and the next patch
applied. This was an editing-context failure, not a mathematical or
computation failure. No partial mutation occurred.
